# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-31 |
| **Generated At** | 2026-07-31T06:49:24Z |
| **Shift Time** | 06:49 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **280** |
| Confirmed Threats | **259** |
| False Positives Filtered | **21** (7.5%) |
| Unique Attacker IPs | **84** |
| Countries of Origin | **29** |
| High Severity Cases | **164** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **116** |
| Malware Samples Analyzed | **4** HIGH · **28** MED · 12 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **182** |
| Unique Credential Pairs | **127** |
| Unique Usernames | **30** |
| Unique Passwords | **97** |
| Successful Auth Pairs | **167** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 51 |
| `test` | 33 |
| `admin` | 25 |
| `operator` | 6 |
| `supervisor` | 6 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `admin` | 13 |
| `123456` | 8 |
| `99999` | 6 |
| `` | 5 |
| `1234567890` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `supervisor` | `99999` | 6 |
| `sshd` | `admin` | 6 |
| `admin` | `admin` | 5 |
| `root` | `` | 5 |
| `root` | `smo@@kkklss` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `admin` | `1234567890` | `10.0.0.73` | 2026-07-31T02:55:24 |
| `git` | `qwerty123` | `193.32.162.15` | 2026-07-31T02:56:01 |
| `git` | `123321` | `193.32.162.15` | 2026-07-31T02:57:10 |
| `admin` | `1234567890` | `222.190.110.210` | 2026-07-31T02:57:11 |
| `git` | `321123` | `193.32.162.15` | 2026-07-31T02:58:19 |
| `ubnt` | `ubnt55` | `10.0.0.73` | 2026-07-31T02:59:04 |
| `git` | `p@ssw0rd` | `193.32.162.15` | 2026-07-31T02:59:26 |
| `root` | `123@@@` | `144.22.238.238` | 2026-07-31T02:59:51 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-07-31T02:59:51 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-07-31T02:59:52 |
| `test` | `123456` | `193.32.162.15` | 2026-07-31T03:00:36 |
| `test` | `654321` | `193.32.162.15` | 2026-07-31T03:01:46 |
| `test` | `123` | `193.32.162.15` | 2026-07-31T03:02:57 |
| `test` | `321` | `193.32.162.15` | 2026-07-31T03:04:08 |
| `config` | `config123456789` | `10.0.0.73` | 2026-07-31T03:04:19 |
| `test` | `test123` | `193.32.162.15` | 2026-07-31T03:05:20 |
| `test` | `test321` | `193.32.162.15` | 2026-07-31T03:06:31 |
| `test` | `password` | `193.32.162.15` | 2026-07-31T03:07:43 |
| `test` | `passwd` | `193.32.162.15` | 2026-07-31T03:08:53 |
| `config` | `config123456789` | `187.126.105.42` | 2026-07-31T03:09:31 |
| `config` | `config123456789` | `118.123.116.93` | 2026-07-31T03:09:45 |
| `test` | `pass` | `193.32.162.15` | 2026-07-31T03:10:03 |
| `test` | `P@ssw0rd` | `193.32.162.15` | 2026-07-31T03:11:11 |
| `admin` | `qwe123qwe` | `201.17.146.173` | 2026-07-31T03:12:20 |
| `test` | `qwe123` | `193.32.162.15` | 2026-07-31T03:12:20 |
| `345gs5662d34` | `345gs5662d34` | `201.17.146.173` | 2026-07-31T03:12:23 |
| `admin` | `3245gs5662d34` | `201.17.146.173` | 2026-07-31T03:12:25 |
| `default` | `logon` | `138.219.13.21` | 2026-07-31T03:13:23 |
| `test` | `qwer1234` | `193.32.162.15` | 2026-07-31T03:13:27 |
| `admin` | `1234567890` | `220.122.115.9` | 2026-07-31T03:13:28 |
| `default` | `logon` | `178.178.194.128` | 2026-07-31T03:13:36 |
| `default` | `logon` | `175.100.107.238` | 2026-07-31T03:13:44 |
| `test` | `password123` | `193.32.162.15` | 2026-07-31T03:14:34 |
| `test` | `qwerty123456` | `193.32.162.15` | 2026-07-31T03:15:41 |
| `test` | `1234qwer` | `193.32.162.15` | 2026-07-31T03:16:50 |
| `config` | `config123456789` | `24.142.170.231` | 2026-07-31T03:17:18 |
| `test` | `123qwe` | `193.32.162.15` | 2026-07-31T03:18:00 |
| `test` | `passpass` | `193.32.162.15` | 2026-07-31T03:19:11 |
| `test` | `pass123` | `193.32.162.15` | 2026-07-31T03:20:22 |
| `test` | `pass1234` | `193.32.162.15` | 2026-07-31T03:21:33 |
| `operator` | `qwerty12345` | `103.31.38.92` | 2026-07-31T03:21:38 |
| `operator` | `qwerty12345` | `31.173.66.222` | 2026-07-31T03:21:46 |
| `test` | `wasd` | `193.32.162.15` | 2026-07-31T03:22:44 |
| `test` | `qwerty` | `193.32.162.15` | 2026-07-31T03:23:57 |
| `test` | `q1w2e3` | `193.32.162.15` | 2026-07-31T03:25:06 |
| `test` | `q1w2e3r4` | `193.32.162.15` | 2026-07-31T03:26:14 |
| `test` | `1q2w3e` | `193.32.162.15` | 2026-07-31T03:27:22 |
| `admin` | `admin` | `10.0.0.73` | 2026-07-31T03:28:18 |
| `test` | `1q2w3e4r` | `193.32.162.15` | 2026-07-31T03:28:31 |
| `unknown` | `44444` | `10.0.0.73` | 2026-07-31T03:29:20 |
| `test` | `111111` | `193.32.162.15` | 2026-07-31T03:29:41 |
| `test` | `test5` | `10.0.0.73` | 2026-07-31T03:30:15 |
| `test` | `qwerty123` | `193.32.162.15` | 2026-07-31T03:30:52 |
| `test` | `123321` | `193.32.162.15` | 2026-07-31T03:32:02 |
| `root` | `` | `176.65.132.8` | 2026-07-31T03:32:16 |
| `root` | `` | `91.92.40.18` | 2026-07-31T03:32:56 |
| `test` | `321123` | `193.32.162.15` | 2026-07-31T03:33:13 |
| `test` | `p@ssw0rd` | `193.32.162.15` | 2026-07-31T03:34:25 |
| `support` | `support` | `176.53.159.196` | 2026-07-31T03:35:09 |
| `operator` | `passw0rd` | `10.0.0.73` | 2026-07-31T03:37:35 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-07-31T03:39:57 |
| `root` | `123@@@` | `64.110.90.250` | 2026-07-31T03:39:58 |
| `` | `id` | `31.76.20.19` | 2026-07-31T03:45:43 |
| `bitrix` | `bitrixpassword` | `189.204.230.91` | 2026-07-31T03:46:44 |
| `345gs5662d34` | `345gs5662d34` | `189.204.230.91` | 2026-07-31T03:46:46 |
| `bitrix` | `3245gs5662d34` | `189.204.230.91` | 2026-07-31T03:46:47 |
| `unknown` | `44444` | `115.245.122.146` | 2026-07-31T03:48:28 |
| `unknown` | `44444` | `70.89.116.5` | 2026-07-31T03:48:37 |
| `operator` | `passw0rd` | `207.219.221.101` | 2026-07-31T03:50:56 |
| `operator` | `passw0rd` | `110.14.192.20` | 2026-07-31T03:51:10 |
| `root` | `888888` | `219.128.15.190` | 2026-07-31T03:56:58 |
| `root` | `888888` | `186.239.41.74` | 2026-07-31T03:57:06 |
| `admin` | `admin` | `34.76.133.51` | 2026-07-31T03:59:36 |
| `supervisor` | `99999` | `10.0.0.73` | 2026-07-31T04:04:59 |
| `admin` | `admin` | `171.231.191.101` | 2026-07-31T04:05:48 |
| `supervisor` | `99999` | `175.198.18.3` | 2026-07-31T04:06:49 |
| `supervisor` | `99999` | `103.103.53.44` | 2026-07-31T04:06:59 |
| `root` | `admin` | `171.231.191.101` | 2026-07-31T04:09:51 |
| `sshd` | `admin` | `10.0.0.73` | 2026-07-31T04:10:57 |
| `user` | `user` | `171.231.191.7` | 2026-07-31T04:11:49 |
| `installer` | `installer` | `171.231.191.7` | 2026-07-31T04:12:23 |
| `ubnt` | `ubnt` | `171.231.191.101` | 2026-07-31T04:15:51 |
| `sshd` | `admin` | `107.135.117.245` | 2026-07-31T04:16:08 |
| `sshd` | `admin` | `111.70.6.20` | 2026-07-31T04:16:17 |
| `root` | `` | `85.11.167.228` | 2026-07-31T04:17:11 |
| `root` | `admin` | `85.11.167.228` | 2026-07-31T04:17:14 |
| `root` | `password` | `85.11.167.228` | 2026-07-31T04:17:16 |
| `root` | `1234` | `85.11.167.228` | 2026-07-31T04:17:18 |
| `root` | `toor` | `85.11.167.228` | 2026-07-31T04:17:19 |
| `admin` | `admin` | `85.11.167.228` | 2026-07-31T04:17:21 |
| `admin` | `123456` | `85.11.167.228` | 2026-07-31T04:17:22 |
| `root` | `12345` | `85.11.167.228` | 2026-07-31T04:17:23 |
| `root` | `default` | `85.11.167.228` | 2026-07-31T04:17:25 |
| `admin` | `password` | `85.11.167.228` | 2026-07-31T04:17:26 |
| `root` | `redhat` | `85.11.167.228` | 2026-07-31T04:17:27 |
| `root` | `1qaz@wsx` | `85.11.167.228` | 2026-07-31T04:17:28 |
| `root` | `vizxv` | `85.11.167.228` | 2026-07-31T04:17:30 |
| `root` | `123456789` | `85.11.167.228` | 2026-07-31T04:17:31 |
| `root` | `qwerty` | `85.11.167.228` | 2026-07-31T04:17:33 |
| `root` | `12345678` | `85.11.167.228` | 2026-07-31T04:17:34 |
| `root` | `111111` | `85.11.167.228` | 2026-07-31T04:17:35 |
| `root` | `1234567` | `85.11.167.228` | 2026-07-31T04:17:37 |
| `root` | `1234567890` | `85.11.167.228` | 2026-07-31T04:17:38 |
| `root` | `abc123` | `85.11.167.228` | 2026-07-31T04:17:39 |
| `root` | `123123` | `85.11.167.228` | 2026-07-31T04:17:40 |
| `root` | `password1` | `85.11.167.228` | 2026-07-31T04:17:42 |
| `root` | `000000` | `85.11.167.228` | 2026-07-31T04:17:43 |
| `root` | `iloveyou` | `85.11.167.228` | 2026-07-31T04:17:44 |
| `root` | `qwertyuiop` | `85.11.167.228` | 2026-07-31T04:17:46 |
| `root` | `123321` | `85.11.167.228` | 2026-07-31T04:17:47 |
| `root` | `654321` | `85.11.167.228` | 2026-07-31T04:17:49 |
| `root` | `666666` | `85.11.167.228` | 2026-07-31T04:17:50 |
| `root` | `123456a` | `85.11.167.228` | 2026-07-31T04:17:51 |
| `admin` | `12345` | `85.11.167.228` | 2026-07-31T04:17:52 |
| `admin` | `12345678` | `85.11.167.228` | 2026-07-31T04:17:54 |
| `admin` | `qwerty` | `85.11.167.228` | 2026-07-31T04:17:55 |
| `admin` | `123123` | `85.11.167.228` | 2026-07-31T04:17:57 |
| `admin` | `admin123` | `85.11.167.228` | 2026-07-31T04:17:58 |
| `admin` | `password123` | `85.11.167.228` | 2026-07-31T04:17:59 |
| `squid` | `squid` | `171.231.191.101` | 2026-07-31T04:18:00 |
| `user` | `user` | `85.11.167.228` | 2026-07-31T04:18:01 |
| `user` | `123456` | `85.11.167.228` | 2026-07-31T04:18:02 |
| `user` | `password` | `85.11.167.228` | 2026-07-31T04:18:03 |
| `ubuntu` | `ubuntu` | `85.11.167.228` | 2026-07-31T04:18:05 |
| `ubuntu` | `123456` | `85.11.167.228` | 2026-07-31T04:18:06 |
| `pi` | `raspberry` | `85.11.167.228` | 2026-07-31T04:18:07 |
| `pi` | `123456` | `85.11.167.228` | 2026-07-31T04:18:09 |
| `oracle` | `oracle` | `85.11.167.228` | 2026-07-31T04:18:10 |
| `oracle` | `123456` | `85.11.167.228` | 2026-07-31T04:18:11 |
| `postgres` | `postgres` | `85.11.167.228` | 2026-07-31T04:18:13 |
| `test` | `test` | `85.11.167.228` | 2026-07-31T04:18:14 |
| `guest` | `guest` | `85.11.167.228` | 2026-07-31T04:18:15 |
| `ftp` | `ftp` | `85.11.167.228` | 2026-07-31T04:18:17 |
| `support` | `support` | `85.11.167.228` | 2026-07-31T04:18:18 |
| `config` | `config` | `171.231.191.7` | 2026-07-31T04:19:04 |
| `support` | `support` | `171.231.191.7` | 2026-07-31T04:20:24 |
| `root` | `rAJS4UtNR7` | `8.219.248.7` | 2026-07-31T04:20:54 |
| `blank` | `blank88` | `103.112.224.81` | 2026-07-31T04:22:51 |
| `blank` | `blank88` | `106.245.246.26` | 2026-07-31T04:23:04 |
| `blank` | `blank88` | `113.28.86.1` | 2026-07-31T04:23:09 |
| `supervisor` | `99999` | `170.247.3.14` | 2026-07-31T04:23:11 |
| `supervisor` | `99999` | `179.185.18.67` | 2026-07-31T04:23:19 |
| `root` | `@` | `171.231.191.101` | 2026-07-31T04:23:50 |
| `sshd` | `admin` | `213.154.80.51` | 2026-07-31T04:23:55 |
| `sshd` | `admin` | `78.187.9.111` | 2026-07-31T04:24:02 |
| `root` | `888888` | `24.207.66.154` | 2026-07-31T04:26:33 |
| `admin` | `admin@123` | `171.231.191.7` | 2026-07-31T04:28:52 |
| `root` | `root123` | `171.231.191.7` | 2026-07-31T04:29:41 |
| `system` | `OkwKcECs8qJP2Z` | `171.231.191.101` | 2026-07-31T04:31:43 |
| `guest` | `guest` | `116.110.17.78` | 2026-07-31T04:34:12 |
| `test` | `test` | `171.231.191.101` | 2026-07-31T04:36:28 |
| `admin` | `0l0ctyQh243O63uD` | `171.231.191.101` | 2026-07-31T04:37:12 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `34.52.255.221` | 2026-07-31T04:41:37 |
| `ais` | `ais` | `137.255.13.19` | 2026-07-31T04:41:40 |
| `345gs5662d34` | `345gs5662d34` | `137.255.13.19` | 2026-07-31T04:41:43 |
| `ais` | `3245gs5662d34` | `137.255.13.19` | 2026-07-31T04:41:45 |
| `*1` | `$4` | `34.52.255.221` | 2026-07-31T04:41:45 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 7778` | `34.52.255.221` | 2026-07-31T04:41:47 |
| `admin` | `1234` | `171.231.191.101` | 2026-07-31T04:43:35 |
| `support` | `support123456` | `10.0.0.73` | 2026-07-31T04:43:51 |
| `admin` | `admin01` | `116.110.17.78` | 2026-07-31T04:44:43 |
| `admin` | `123456` | `116.110.17.78` | 2026-07-31T04:47:41 |
| `user` | `1234` | `116.110.17.78` | 2026-07-31T04:50:40 |
| `admin` | `admin123` | `116.110.17.78` | 2026-07-31T04:50:45 |
| `admin` | `default` | `171.231.191.101` | 2026-07-31T04:52:53 |
| `root` | `1qaz@WSX3edc` | `141.253.107.23` | 2026-07-31T04:53:03 |
| `root` | `` | `94.154.43.91` | 2026-07-31T04:53:39 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **280** |
| Sessions with Fingerprint | **15** |
| Unique HASSH Fingerprints | **15** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 90 |
| OpenSSH | 28 |
| AsyncSSH (Python) | 23 |
| libssh | 21 |
| Paramiko (Python) | 10 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `16443846184e...` | Generic scanner | 52 | 2 |
| `2ec37a7cc8da...` | Mirai/variant | 34 | 1 |
| `acaa53e0a7d7...` | Mirai/variant | 28 | 28 |
| `fda360b1b4f4...` | Mirai/variant | 23 | 3 |
| `a2de0f306611...` | Mirai/variant | 10 | 2 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `16443846184e...` | Go SSH scanner | 52 | 2 | Generic scanner |
| `2ec37a7cc8da...` | Go SSH scanner | 34 | 1 | Mirai/variant |
| `acaa53e0a7d7...` | OpenSSH | 28 | 28 | Mirai/variant |
| `fda360b1b4f4...` | AsyncSSH (Python) | 23 | 3 | Mirai/variant |
| `95420f9d932d...` | libssh | 12 | 7 | — |
| `a2de0f306611...` | Paramiko (Python) | 10 | 2 | Mirai/variant |
| `f555226df196...` | libssh | 6 | 2 | Mirai/variant |
| `e788c657d1a2...` | Nmap scanner | 6 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **9** |
| Campaign Clusters | **4** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1105, T1059.004, T1083, T1082` |
| **Recon Loader Script** | 🟡 MEDIUM | 34 | 1 | `T1082, T1592, T1078, T1083` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 2 | 2 | `T1082, T1105, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 3 | 3 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
echo WRITABLE >/tmp/.testfile 2>&1
```
```
ls -l /tmp/.testfile 2>&1
```
```
rm -f /tmp/.testfile
```
```
cd /tmp
```
```
for pid in /proc/[0-9]*; do pid_num="${pid##*/}"; if [ -r "$pid/maps" ]; then suspicious=true; while IFS= read -r line; do case "$line" in *"/lib/"*|*"/lib64/"*|*".so"*) suspicious=false; break;; esac; done < "$pid/maps"; if [ "$suspicious" = true ]; then kill -9 "$pid_num" 2>/dev/null; fi; fi; done;
```
Source IPs: `91.92.40.18`

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
Source IPs: `193.32.162.15`

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
Source IPs: `176.65.132.8`, `94.154.43.91`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **84** |
| Unique ASNs | **55** |
| High-Risk ASNs | **46** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS22773` | Cox Communications Inc. | 8 | MEDIUM |
| `AS396982` | Google LLC | 5 | HIGH |
| `AS46562` | Performive LLC | 4 | MEDIUM |
| `AS31898` | Oracle Corporation | 3 | HIGH |
| `AS4134` | CHINANET BACKBONE | 3 | HIGH |
| `AS197170` | TechTies Inc. | 3 | HIGH |
| `AS35042` | Layer7 Networks GmbH | 2 | HIGH |
| `AS219502` | Storm Industries LLC | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (164)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-ed9c2799170c

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-31 02:56 |
| **Last Seen** | 2026-07-31 02:56 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 02:56:00` | `cowrie.session.connect` |
| `2026-07-31 02:56:00` | `cowrie.client.version` |
| `2026-07-31 02:56:00` | `cowrie.client.kex` |
| `2026-07-31 02:56:01` | `cowrie.login.success` |
| `2026-07-31 02:56:03` | `cowrie.session.params` |
| `2026-07-31 02:56:03` | `cowrie.command.input` |
| `2026-07-31 02:56:03` | `cowrie.command.input` |
| `2026-07-31 02:56:03` | `cowrie.command.input` |
| `2026-07-31 02:56:03` | `cowrie.command.input` |
| `2026-07-31 02:56:03` | `cowrie.command.input` |
| `2026-07-31 02:56:03` | `cowrie.command.success` |
| `2026-07-31 02:56:03` | `cowrie.command.input` |
| `2026-07-31 02:56:03` | `cowrie.command.input` |
| `2026-07-31 02:56:03` | `cowrie.command.input` |
| `2026-07-31 02:56:03` | `cowrie.command.input` |
| `2026-07-31 02:56:03` | `cowrie.log.closed` |
| `2026-07-31 02:56:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b41eaab826e3

| Field | Detail |
|---|---|
| **Source IP** | `222.190.110[.]210` |
| **First Seen** | 2026-07-31 02:57 |
| **Last Seen** | 2026-07-31 02:57 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 02:57:08` | `cowrie.session.connect` |
| `2026-07-31 02:57:09` | `cowrie.client.version` |
| `2026-07-31 02:57:09` | `cowrie.client.kex` |
| `2026-07-31 02:57:11` | `cowrie.login.success` |
| `2026-07-31 02:57:12` | `cowrie.direct-tcpip.request` |
| `2026-07-31 02:57:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.190.110[.]210` to AbuseIPDB if not already reported
- [ ] Block `222.190.110[.]210` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75f05fb4868c

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-31 02:57 |
| **Last Seen** | 2026-07-31 02:57 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 02:57:08` | `cowrie.session.connect` |
| `2026-07-31 02:57:08` | `cowrie.client.version` |
| `2026-07-31 02:57:09` | `cowrie.client.kex` |
| `2026-07-31 02:57:10` | `cowrie.login.success` |
| `2026-07-31 02:57:11` | `cowrie.session.params` |
| `2026-07-31 02:57:11` | `cowrie.command.input` |
| `2026-07-31 02:57:11` | `cowrie.command.input` |
| `2026-07-31 02:57:11` | `cowrie.command.input` |
| `2026-07-31 02:57:11` | `cowrie.command.input` |
| `2026-07-31 02:57:11` | `cowrie.command.input` |
| `2026-07-31 02:57:11` | `cowrie.command.success` |
| `2026-07-31 02:57:11` | `cowrie.command.input` |
| `2026-07-31 02:57:11` | `cowrie.command.input` |
| `2026-07-31 02:57:11` | `cowrie.command.input` |
| `2026-07-31 02:57:11` | `cowrie.command.input` |
| `2026-07-31 02:57:11` | `cowrie.log.closed` |
| `2026-07-31 02:57:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4af8a2636c5

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-31 02:58 |
| **Last Seen** | 2026-07-31 02:58 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 02:58:17` | `cowrie.session.connect` |
| `2026-07-31 02:58:17` | `cowrie.client.version` |
| `2026-07-31 02:58:17` | `cowrie.client.kex` |
| `2026-07-31 02:58:19` | `cowrie.login.success` |
| `2026-07-31 02:58:20` | `cowrie.session.params` |
| `2026-07-31 02:58:20` | `cowrie.command.input` |
| `2026-07-31 02:58:20` | `cowrie.command.input` |
| `2026-07-31 02:58:20` | `cowrie.command.input` |
| `2026-07-31 02:58:20` | `cowrie.command.input` |
| `2026-07-31 02:58:20` | `cowrie.command.input` |
| `2026-07-31 02:58:20` | `cowrie.command.success` |
| `2026-07-31 02:58:20` | `cowrie.command.input` |
| `2026-07-31 02:58:20` | `cowrie.command.input` |
| `2026-07-31 02:58:20` | `cowrie.command.input` |
| `2026-07-31 02:58:20` | `cowrie.command.input` |
| `2026-07-31 02:58:20` | `cowrie.log.closed` |
| `2026-07-31 02:58:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2cc67af0b43

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-31 02:59 |
| **Last Seen** | 2026-07-31 02:59 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 02:59:25` | `cowrie.session.connect` |
| `2026-07-31 02:59:25` | `cowrie.client.version` |
| `2026-07-31 02:59:25` | `cowrie.client.kex` |
| `2026-07-31 02:59:26` | `cowrie.login.success` |
| `2026-07-31 02:59:28` | `cowrie.session.params` |
| `2026-07-31 02:59:28` | `cowrie.command.input` |
| `2026-07-31 02:59:28` | `cowrie.command.input` |
| `2026-07-31 02:59:28` | `cowrie.command.input` |
| `2026-07-31 02:59:28` | `cowrie.command.input` |
| `2026-07-31 02:59:28` | `cowrie.command.input` |
| `2026-07-31 02:59:28` | `cowrie.command.success` |
| `2026-07-31 02:59:28` | `cowrie.command.input` |
| `2026-07-31 02:59:28` | `cowrie.command.input` |
| `2026-07-31 02:59:28` | `cowrie.command.input` |
| `2026-07-31 02:59:28` | `cowrie.command.input` |
| `2026-07-31 02:59:28` | `cowrie.log.closed` |
| `2026-07-31 02:59:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f81ca87974c3

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-31 02:59 |
| **Last Seen** | 2026-07-31 02:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 02:59:50` | `cowrie.session.connect` |
| `2026-07-31 02:59:50` | `cowrie.client.version` |
| `2026-07-31 02:59:50` | `cowrie.client.kex` |
| `2026-07-31 02:59:51` | `cowrie.login.success` |
| `2026-07-31 02:59:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f89659ec7f1

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-31 02:59 |
| **Last Seen** | 2026-07-31 02:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 02:59:50` | `cowrie.session.connect` |
| `2026-07-31 02:59:50` | `cowrie.client.version` |
| `2026-07-31 02:59:50` | `cowrie.client.kex` |
| `2026-07-31 02:59:51` | `cowrie.login.success` |
| `2026-07-31 02:59:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02fbc5b3229a

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-31 02:59 |
| **Last Seen** | 2026-07-31 02:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 02:59:51` | `cowrie.session.connect` |
| `2026-07-31 02:59:51` | `cowrie.client.version` |
| `2026-07-31 02:59:51` | `cowrie.client.kex` |
| `2026-07-31 02:59:52` | `cowrie.login.success` |
| `2026-07-31 02:59:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73de31e7f0e7

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-31 03:00 |
| **Last Seen** | 2026-07-31 03:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 03:00:02` | `cowrie.session.connect` |
| `2026-07-31 03:00:02` | `cowrie.client.version` |
| `2026-07-31 03:00:02` | `cowrie.client.kex` |
| `2026-07-31 03:00:03` | `cowrie.login.success` |
| `2026-07-31 03:00:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-846fb087155e

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-31 03:00 |
| **Last Seen** | 2026-07-31 03:00 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 03:00:35` | `cowrie.session.connect` |
| `2026-07-31 03:00:35` | `cowrie.client.version` |
| `2026-07-31 03:00:35` | `cowrie.client.kex` |
| `2026-07-31 03:00:36` | `cowrie.login.success` |
| `2026-07-31 03:00:37` | `cowrie.session.params` |
| `2026-07-31 03:00:37` | `cowrie.command.input` |
| `2026-07-31 03:00:37` | `cowrie.command.input` |
| `2026-07-31 03:00:37` | `cowrie.command.input` |
| `2026-07-31 03:00:37` | `cowrie.command.input` |
| `2026-07-31 03:00:37` | `cowrie.command.input` |
| `2026-07-31 03:00:37` | `cowrie.command.success` |
| `2026-07-31 03:00:37` | `cowrie.command.input` |
| `2026-07-31 03:00:37` | `cowrie.command.input` |
| `2026-07-31 03:00:37` | `cowrie.command.input` |
| `2026-07-31 03:00:37` | `cowrie.command.input` |
| `2026-07-31 03:00:38` | `cowrie.log.closed` |
| `2026-07-31 03:00:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43b5188c89bf

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-31 03:01 |
| **Last Seen** | 2026-07-31 03:01 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 03:01:45` | `cowrie.session.connect` |
| `2026-07-31 03:01:45` | `cowrie.client.version` |
| `2026-07-31 03:01:45` | `cowrie.client.kex` |
| `2026-07-31 03:01:46` | `cowrie.login.success` |
| `2026-07-31 03:01:48` | `cowrie.session.params` |
| `2026-07-31 03:01:48` | `cowrie.command.input` |
| `2026-07-31 03:01:48` | `cowrie.command.input` |
| `2026-07-31 03:01:48` | `cowrie.command.input` |
| `2026-07-31 03:01:48` | `cowrie.command.input` |
| `2026-07-31 03:01:48` | `cowrie.command.input` |
| `2026-07-31 03:01:48` | `cowrie.command.success` |
| `2026-07-31 03:01:48` | `cowrie.command.input` |
| `2026-07-31 03:01:48` | `cowrie.command.input` |
| `2026-07-31 03:01:48` | `cowrie.command.input` |
| `2026-07-31 03:01:48` | `cowrie.command.input` |
| `2026-07-31 03:01:48` | `cowrie.log.closed` |
| `2026-07-31 03:01:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd12ee1a6ffa

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-31 03:02 |
| **Last Seen** | 2026-07-31 03:02 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 03:02:56` | `cowrie.session.connect` |
| `2026-07-31 03:02:56` | `cowrie.client.version` |
| `2026-07-31 03:02:56` | `cowrie.client.kex` |
| `2026-07-31 03:02:57` | `cowrie.login.success` |
| `2026-07-31 03:02:58` | `cowrie.session.params` |
| `2026-07-31 03:02:58` | `cowrie.command.input` |
| `2026-07-31 03:02:58` | `cowrie.command.input` |
| `2026-07-31 03:02:58` | `cowrie.command.input` |
| `2026-07-31 03:02:58` | `cowrie.command.input` |
| `2026-07-31 03:02:58` | `cowrie.command.input` |
| `2026-07-31 03:02:58` | `cowrie.command.success` |
| `2026-07-31 03:02:58` | `cowrie.command.input` |
| `2026-07-31 03:02:58` | `cowrie.command.input` |
| `2026-07-31 03:02:58` | `cowrie.command.input` |
| `2026-07-31 03:02:58` | `cowrie.command.input` |
| `2026-07-31 03:02:58` | `cowrie.log.closed` |
| `2026-07-31 03:02:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1855d5175133

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-31 03:04 |
| **Last Seen** | 2026-07-31 03:04 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 03:04:07` | `cowrie.session.connect` |
| `2026-07-31 03:04:07` | `cowrie.client.version` |
| `2026-07-31 03:04:07` | `cowrie.client.kex` |
| `2026-07-31 03:04:08` | `cowrie.login.success` |
| `2026-07-31 03:04:09` | `cowrie.session.params` |
| `2026-07-31 03:04:09` | `cowrie.command.input` |
| `2026-07-31 03:04:09` | `cowrie.command.input` |
| `2026-07-31 03:04:09` | `cowrie.command.input` |
| `2026-07-31 03:04:09` | `cowrie.command.input` |
| `2026-07-31 03:04:09` | `cowrie.command.input` |
| `2026-07-31 03:04:09` | `cowrie.command.success` |
| `2026-07-31 03:04:09` | `cowrie.command.input` |
| `2026-07-31 03:04:09` | `cowrie.command.input` |
| `2026-07-31 03:04:09` | `cowrie.command.input` |
| `2026-07-31 03:04:09` | `cowrie.command.input` |
| `2026-07-31 03:04:10` | `cowrie.log.closed` |
| `2026-07-31 03:04:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4033a087128

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-31 03:05 |
| **Last Seen** | 2026-07-31 03:05 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 03:05:17` | `cowrie.session.connect` |
| `2026-07-31 03:05:17` | `cowrie.client.version` |
| `2026-07-31 03:05:19` | `cowrie.client.kex` |
| `2026-07-31 03:05:20` | `cowrie.login.success` |
| `2026-07-31 03:05:21` | `cowrie.session.params` |
| `2026-07-31 03:05:21` | `cowrie.command.input` |
| `2026-07-31 03:05:21` | `cowrie.command.input` |
| `2026-07-31 03:05:21` | `cowrie.command.input` |
| `2026-07-31 03:05:21` | `cowrie.command.input` |
| `2026-07-31 03:05:21` | `cowrie.command.input` |
| `2026-07-31 03:05:21` | `cowrie.command.success` |
| `2026-07-31 03:05:21` | `cowrie.command.input` |
| `2026-07-31 03:05:21` | `cowrie.command.input` |
| `2026-07-31 03:05:21` | `cowrie.command.input` |
| `2026-07-31 03:05:21` | `cowrie.command.input` |
| `2026-07-31 03:05:22` | `cowrie.log.closed` |
| `2026-07-31 03:05:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a37079f7a746

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-31 03:06 |
| **Last Seen** | 2026-07-31 03:06 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 03:06:29` | `cowrie.session.connect` |
| `2026-07-31 03:06:30` | `cowrie.client.version` |
| `2026-07-31 03:06:30` | `cowrie.client.kex` |
| `2026-07-31 03:06:31` | `cowrie.login.success` |
| `2026-07-31 03:06:32` | `cowrie.session.params` |
| `2026-07-31 03:06:32` | `cowrie.command.input` |
| `2026-07-31 03:06:32` | `cowrie.command.input` |
| `2026-07-31 03:06:32` | `cowrie.command.input` |
| `2026-07-31 03:06:32` | `cowrie.command.input` |
| `2026-07-31 03:06:32` | `cowrie.command.input` |
| `2026-07-31 03:06:32` | `cowrie.command.success` |
| `2026-07-31 03:06:32` | `cowrie.command.input` |
| `2026-07-31 03:06:32` | `cowrie.command.input` |
| `2026-07-31 03:06:32` | `cowrie.command.input` |
| `2026-07-31 03:06:32` | `cowrie.command.input` |
| `2026-07-31 03:06:32` | `cowrie.log.closed` |
| `2026-07-31 03:06:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89af86c61102

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-31 03:07 |
| **Last Seen** | 2026-07-31 03:07 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 03:07:42` | `cowrie.session.connect` |
| `2026-07-31 03:07:42` | `cowrie.client.version` |
| `2026-07-31 03:07:42` | `cowrie.client.kex` |
| `2026-07-31 03:07:43` | `cowrie.login.success` |
| `2026-07-31 03:07:44` | `cowrie.session.params` |
| `2026-07-31 03:07:44` | `cowrie.command.input` |
| `2026-07-31 03:07:44` | `cowrie.command.input` |
| `2026-07-31 03:07:44` | `cowrie.command.input` |
| `2026-07-31 03:07:44` | `cowrie.command.input` |
| `2026-07-31 03:07:44` | `cowrie.command.input` |
| `2026-07-31 03:07:44` | `cowrie.command.success` |
| `2026-07-31 03:07:44` | `cowrie.command.input` |
| `2026-07-31 03:07:44` | `cowrie.command.input` |
| `2026-07-31 03:07:44` | `cowrie.command.input` |
| `2026-07-31 03:07:44` | `cowrie.command.input` |
| `2026-07-31 03:07:45` | `cowrie.log.closed` |
| `2026-07-31 03:07:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea2bb0e6ca01

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-31 03:08 |
| **Last Seen** | 2026-07-31 03:08 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 03:08:52` | `cowrie.session.connect` |
| `2026-07-31 03:08:52` | `cowrie.client.version` |
| `2026-07-31 03:08:52` | `cowrie.client.kex` |
| `2026-07-31 03:08:53` | `cowrie.login.success` |
| `2026-07-31 03:08:55` | `cowrie.session.params` |
| `2026-07-31 03:08:55` | `cowrie.command.input` |
| `2026-07-31 03:08:55` | `cowrie.command.input` |
| `2026-07-31 03:08:55` | `cowrie.command.input` |
| `2026-07-31 03:08:55` | `cowrie.command.input` |
| `2026-07-31 03:08:55` | `cowrie.command.input` |
| `2026-07-31 03:08:55` | `cowrie.command.success` |
| `2026-07-31 03:08:55` | `cowrie.command.input` |
| `2026-07-31 03:08:55` | `cowrie.command.input` |
| `2026-07-31 03:08:55` | `cowrie.command.input` |
| `2026-07-31 03:08:55` | `cowrie.command.input` |
| `2026-07-31 03:08:55` | `cowrie.log.closed` |
| `2026-07-31 03:08:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52cf570fd684

| Field | Detail |
|---|---|
| **Source IP** | `187.126.105[.]42` |
| **First Seen** | 2026-07-31 03:09 |
| **Last Seen** | 2026-07-31 03:09 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 03:09:28` | `cowrie.session.connect` |
| `2026-07-31 03:09:28` | `cowrie.client.version` |
| `2026-07-31 03:09:28` | `cowrie.client.kex` |
| `2026-07-31 03:09:31` | `cowrie.login.success` |
| `2026-07-31 03:09:31` | `cowrie.direct-tcpip.request` |
| `2026-07-31 03:09:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.126.105[.]42` to AbuseIPDB if not already reported
- [ ] Block `187.126.105[.]42` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0fe9b5648559

| Field | Detail |
|---|---|
| **Source IP** | `118.123.116[.]93` |
| **First Seen** | 2026-07-31 03:09 |
| **Last Seen** | 2026-07-31 03:09 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 03:09:42` | `cowrie.session.connect` |
| `2026-07-31 03:09:42` | `cowrie.client.version` |
| `2026-07-31 03:09:42` | `cowrie.client.kex` |
| `2026-07-31 03:09:45` | `cowrie.login.success` |
| `2026-07-31 03:09:46` | `cowrie.direct-tcpip.request` |
| `2026-07-31 03:09:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.123.116[.]93` to AbuseIPDB if not already reported
- [ ] Block `118.123.116[.]93` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37693f2b6bb3

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-31 03:10 |
| **Last Seen** | 2026-07-31 03:10 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 03:10:02` | `cowrie.session.connect` |
| `2026-07-31 03:10:02` | `cowrie.client.version` |
| `2026-07-31 03:10:02` | `cowrie.client.kex` |
| `2026-07-31 03:10:03` | `cowrie.login.success` |
| `2026-07-31 03:10:04` | `cowrie.session.params` |
| `2026-07-31 03:10:04` | `cowrie.command.input` |
| `2026-07-31 03:10:04` | `cowrie.command.input` |
| `2026-07-31 03:10:04` | `cowrie.command.input` |
| `2026-07-31 03:10:04` | `cowrie.command.input` |
| `2026-07-31 03:10:04` | `cowrie.command.input` |
| `2026-07-31 03:10:04` | `cowrie.command.success` |
| `2026-07-31 03:10:04` | `cowrie.command.input` |
| `2026-07-31 03:10:04` | `cowrie.command.input` |
| `2026-07-31 03:10:04` | `cowrie.command.input` |
| `2026-07-31 03:10:04` | `cowrie.command.input` |
| `2026-07-31 03:10:04` | `cowrie.log.closed` |
| `2026-07-31 03:10:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6c00595856e

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-31 03:11 |
| **Last Seen** | 2026-07-31 03:11 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 03:11:10` | `cowrie.session.connect` |
| `2026-07-31 03:11:10` | `cowrie.client.version` |
| `2026-07-31 03:11:10` | `cowrie.client.kex` |
| `2026-07-31 03:11:11` | `cowrie.login.success` |
| `2026-07-31 03:11:12` | `cowrie.session.params` |
| `2026-07-31 03:11:12` | `cowrie.command.input` |
| `2026-07-31 03:11:12` | `cowrie.command.input` |
| `2026-07-31 03:11:12` | `cowrie.command.input` |
| `2026-07-31 03:11:12` | `cowrie.command.input` |
| `2026-07-31 03:11:12` | `cowrie.command.input` |
| `2026-07-31 03:11:12` | `cowrie.command.success` |
| `2026-07-31 03:11:12` | `cowrie.command.input` |
| `2026-07-31 03:11:12` | `cowrie.command.input` |
| `2026-07-31 03:11:12` | `cowrie.command.input` |
| `2026-07-31 03:11:12` | `cowrie.command.input` |
| `2026-07-31 03:11:12` | `cowrie.log.closed` |
| `2026-07-31 03:11:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a36a74c59ea

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-31 03:12 |
| **Last Seen** | 2026-07-31 03:12 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 03:12:18` | `cowrie.session.connect` |
| `2026-07-31 03:12:18` | `cowrie.client.version` |
| `2026-07-31 03:12:18` | `cowrie.client.kex` |
| `2026-07-31 03:12:20` | `cowrie.login.success` |
| `2026-07-31 03:12:22` | `cowrie.session.params` |
| `2026-07-31 03:12:22` | `cowrie.command.input` |
| `2026-07-31 03:12:22` | `cowrie.command.input` |
| `2026-07-31 03:12:22` | `cowrie.command.input` |
| `2026-07-31 03:12:22` | `cowrie.command.input` |
| `2026-07-31 03:12:22` | `cowrie.command.input` |
| `2026-07-31 03:12:22` | `cowrie.command.success` |
| `2026-07-31 03:12:22` | `cowrie.command.input` |
| `2026-07-31 03:12:22` | `cowrie.command.input` |
| `2026-07-31 03:12:22` | `cowrie.command.input` |
| `2026-07-31 03:12:22` | `cowrie.command.input` |
| `2026-07-31 03:12:22` | `cowrie.log.closed` |
| `2026-07-31 03:12:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5ce104eea03

| Field | Detail |
|---|---|
| **Source IP** | `201.17.146[.]173` |
| **First Seen** | 2026-07-31 03:12 |
| **Last Seen** | 2026-07-31 03:12 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 03:12:19` | `cowrie.session.connect` |
| `2026-07-31 03:12:19` | `cowrie.client.version` |
| `2026-07-31 03:12:19` | `cowrie.client.kex` |
| `2026-07-31 03:12:20` | `cowrie.login.success` |
| `2026-07-31 03:12:21` | `cowrie.session.params` |
| `2026-07-31 03:12:21` | `cowrie.command.input` |
| `2026-07-31 03:12:21` | `cowrie.command.failed` |
| `2026-07-31 03:12:22` | `cowrie.log.closed` |
| `2026-07-31 03:12:22` | `cowrie.session.params` |
| `2026-07-31 03:12:22` | `cowrie.command.input` |
| `2026-07-31 03:12:22` | `cowrie.session.file_download` |
| `2026-07-31 03:12:22` | `cowrie.log.closed` |
| `2026-07-31 03:12:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.17.146[.]173` to AbuseIPDB if not already reported
- [ ] Block `201.17.146[.]173` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f07a96ffa67

| Field | Detail |
|---|---|
| **Source IP** | `201.17.146[.]173` |
| **First Seen** | 2026-07-31 03:12 |
| **Last Seen** | 2026-07-31 03:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 03:12:22` | `cowrie.session.connect` |
| `2026-07-31 03:12:22` | `cowrie.client.version` |
| `2026-07-31 03:12:23` | `cowrie.client.kex` |
| `2026-07-31 03:12:23` | `cowrie.login.success` |
| `2026-07-31 03:12:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.17.146[.]173` to AbuseIPDB if not already reported
- [ ] Block `201.17.146[.]173` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2a18367f4a4

| Field | Detail |
|---|---|
| **Source IP** | `201.17.146[.]173` |
| **First Seen** | 2026-07-31 03:12 |
| **Last Seen** | 2026-07-31 03:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 03:12:24` | `cowrie.session.connect` |
| `2026-07-31 03:12:24` | `cowrie.client.version` |
| `2026-07-31 03:12:24` | `cowrie.client.kex` |
| `2026-07-31 03:12:25` | `cowrie.login.success` |
| `2026-07-31 03:12:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.17.146[.]173` to AbuseIPDB if not already reported
- [ ] Block `201.17.146[.]173` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2572cd88c68

| Field | Detail |
|---|---|
| **Source IP** | `138.219.13[.]21` |
| **First Seen** | 2026-07-31 03:13 |
| **Last Seen** | 2026-07-31 03:13 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 03:13:21` | `cowrie.session.connect` |
| `2026-07-31 03:13:22` | `cowrie.client.version` |
| `2026-07-31 03:13:22` | `cowrie.client.kex` |
| `2026-07-31 03:13:23` | `cowrie.login.success` |
| `2026-07-31 03:13:24` | `cowrie.direct-tcpip.request` |
| `2026-07-31 03:13:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.219.13[.]21` to AbuseIPDB if not already reported
- [ ] Block `138.219.13[.]21` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4095995c0f8

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-31 03:13 |
| **Last Seen** | 2026-07-31 03:13 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 03:13:25` | `cowrie.session.connect` |
| `2026-07-31 03:13:26` | `cowrie.client.version` |
| `2026-07-31 03:13:26` | `cowrie.client.kex` |
| `2026-07-31 03:13:27` | `cowrie.login.success` |
| `2026-07-31 03:13:28` | `cowrie.session.params` |
| `2026-07-31 03:13:28` | `cowrie.command.input` |
| `2026-07-31 03:13:28` | `cowrie.command.input` |
| `2026-07-31 03:13:28` | `cowrie.command.input` |
| `2026-07-31 03:13:28` | `cowrie.command.input` |
| `2026-07-31 03:13:28` | `cowrie.command.input` |
| `2026-07-31 03:13:28` | `cowrie.command.success` |
| `2026-07-31 03:13:28` | `cowrie.command.input` |
| `2026-07-31 03:13:28` | `cowrie.command.input` |
| `2026-07-31 03:13:28` | `cowrie.command.input` |
| `2026-07-31 03:13:28` | `cowrie.command.input` |
| `2026-07-31 03:13:29` | `cowrie.log.closed` |
| `2026-07-31 03:13:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-504100dfc958

| Field | Detail |
|---|---|
| **Source IP** | `220.122.115[.]9` |
| **First Seen** | 2026-07-31 03:13 |
| **Last Seen** | 2026-07-31 03:13 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 03:13:26` | `cowrie.session.connect` |
| `2026-07-31 03:13:26` | `cowrie.client.version` |
| `2026-07-31 03:13:26` | `cowrie.client.kex` |
| `2026-07-31 03:13:28` | `cowrie.login.success` |
| `2026-07-31 03:13:29` | `cowrie.direct-tcpip.request` |
| `2026-07-31 03:13:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.122.115[.]9` to AbuseIPDB if not already reported
- [ ] Block `220.122.115[.]9` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa646de8f746

| Field | Detail |
|---|---|
| **Source IP** | `178.178.194[.]128` |
| **First Seen** | 2026-07-31 03:13 |
| **Last Seen** | 2026-07-31 03:13 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 03:13:34` | `cowrie.session.connect` |
| `2026-07-31 03:13:35` | `cowrie.client.version` |
| `2026-07-31 03:13:35` | `cowrie.client.kex` |
| `2026-07-31 03:13:36` | `cowrie.login.success` |
| `2026-07-31 03:13:36` | `cowrie.direct-tcpip.request` |
| `2026-07-31 03:13:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.194[.]128` to AbuseIPDB if not already reported
- [ ] Block `178.178.194[.]128` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb7e25ebedab

| Field | Detail |
|---|---|
| **Source IP** | `175.100.107[.]238` |
| **First Seen** | 2026-07-31 03:13 |
| **Last Seen** | 2026-07-31 03:13 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 03:13:41` | `cowrie.session.connect` |
| `2026-07-31 03:13:42` | `cowrie.client.version` |
| `2026-07-31 03:13:42` | `cowrie.client.kex` |
| `2026-07-31 03:13:44` | `cowrie.login.success` |
| `2026-07-31 03:13:45` | `cowrie.direct-tcpip.request` |
| `2026-07-31 03:13:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.100.107[.]238` to AbuseIPDB if not already reported
- [ ] Block `175.100.107[.]238` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a4dc3de5410

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-31 03:14 |
| **Last Seen** | 2026-07-31 03:14 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 03:14:32` | `cowrie.session.connect` |
| `2026-07-31 03:14:32` | `cowrie.client.version` |
| `2026-07-31 03:14:32` | `cowrie.client.kex` |
| `2026-07-31 03:14:34` | `cowrie.login.success` |
| `2026-07-31 03:14:35` | `cowrie.session.params` |
| `2026-07-31 03:14:35` | `cowrie.command.input` |
| `2026-07-31 03:14:35` | `cowrie.command.input` |
| `2026-07-31 03:14:35` | `cowrie.command.input` |
| `2026-07-31 03:14:35` | `cowrie.command.input` |
| `2026-07-31 03:14:35` | `cowrie.command.input` |
| `2026-07-31 03:14:35` | `cowrie.command.success` |
| `2026-07-31 03:14:35` | `cowrie.command.input` |
| `2026-07-31 03:14:35` | `cowrie.command.input` |
| `2026-07-31 03:14:35` | `cowrie.command.input` |
| `2026-07-31 03:14:35` | `cowrie.command.input` |
| `2026-07-31 03:14:35` | `cowrie.log.closed` |
| `2026-07-31 03:14:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a4881d55070

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-31 03:15 |
| **Last Seen** | 2026-07-31 03:15 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 03:15:40` | `cowrie.session.connect` |
| `2026-07-31 03:15:40` | `cowrie.client.version` |
| `2026-07-31 03:15:40` | `cowrie.client.kex` |
| `2026-07-31 03:15:41` | `cowrie.login.success` |
| `2026-07-31 03:15:43` | `cowrie.session.params` |
| `2026-07-31 03:15:43` | `cowrie.command.input` |
| `2026-07-31 03:15:43` | `cowrie.command.input` |
| `2026-07-31 03:15:43` | `cowrie.command.input` |
| `2026-07-31 03:15:43` | `cowrie.command.input` |
| `2026-07-31 03:15:43` | `cowrie.command.input` |
| `2026-07-31 03:15:43` | `cowrie.command.success` |
| `2026-07-31 03:15:43` | `cowrie.command.input` |
| `2026-07-31 03:15:43` | `cowrie.command.input` |
| `2026-07-31 03:15:43` | `cowrie.command.input` |
| `2026-07-31 03:15:43` | `cowrie.command.input` |
| `2026-07-31 03:15:43` | `cowrie.log.closed` |
| `2026-07-31 03:15:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-229abd323e44

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-31 03:16 |
| **Last Seen** | 2026-07-31 03:16 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 03:16:49` | `cowrie.session.connect` |
| `2026-07-31 03:16:49` | `cowrie.client.version` |
| `2026-07-31 03:16:49` | `cowrie.client.kex` |
| `2026-07-31 03:16:50` | `cowrie.login.success` |
| `2026-07-31 03:16:52` | `cowrie.session.params` |
| `2026-07-31 03:16:52` | `cowrie.command.input` |
| `2026-07-31 03:16:52` | `cowrie.command.input` |
| `2026-07-31 03:16:52` | `cowrie.command.input` |
| `2026-07-31 03:16:52` | `cowrie.command.input` |
| `2026-07-31 03:16:52` | `cowrie.command.input` |
| `2026-07-31 03:16:52` | `cowrie.command.success` |
| `2026-07-31 03:16:52` | `cowrie.command.input` |
| `2026-07-31 03:16:52` | `cowrie.command.input` |
| `2026-07-31 03:16:52` | `cowrie.command.input` |
| `2026-07-31 03:16:52` | `cowrie.command.input` |
| `2026-07-31 03:16:52` | `cowrie.log.closed` |
| `2026-07-31 03:16:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7524ee1a4a63

| Field | Detail |
|---|---|
| **Source IP** | `24.142.170[.]231` |
| **First Seen** | 2026-07-31 03:17 |
| **Last Seen** | 2026-07-31 03:17 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 03:17:16` | `cowrie.session.connect` |
| `2026-07-31 03:17:16` | `cowrie.client.version` |
| `2026-07-31 03:17:16` | `cowrie.client.kex` |
| `2026-07-31 03:17:18` | `cowrie.login.success` |
| `2026-07-31 03:17:18` | `cowrie.direct-tcpip.request` |
| `2026-07-31 03:17:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `24.142.170[.]231` to AbuseIPDB if not already reported
- [ ] Block `24.142.170[.]231` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3747fa2ef52f

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-31 03:17 |
| **Last Seen** | 2026-07-31 03:18 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 03:17:59` | `cowrie.session.connect` |
| `2026-07-31 03:17:59` | `cowrie.client.version` |
| `2026-07-31 03:17:59` | `cowrie.client.kex` |
| `2026-07-31 03:18:00` | `cowrie.login.success` |
| `2026-07-31 03:18:02` | `cowrie.session.params` |
| `2026-07-31 03:18:02` | `cowrie.command.input` |
| `2026-07-31 03:18:02` | `cowrie.command.input` |
| `2026-07-31 03:18:02` | `cowrie.command.input` |
| `2026-07-31 03:18:02` | `cowrie.command.input` |
| `2026-07-31 03:18:02` | `cowrie.command.input` |
| `2026-07-31 03:18:02` | `cowrie.command.success` |
| `2026-07-31 03:18:02` | `cowrie.command.input` |
| `2026-07-31 03:18:02` | `cowrie.command.input` |
| `2026-07-31 03:18:02` | `cowrie.command.input` |
| `2026-07-31 03:18:02` | `cowrie.command.input` |
| `2026-07-31 03:18:02` | `cowrie.log.closed` |
| `2026-07-31 03:18:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ffeadf0f2e6f

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-31 03:19 |
| **Last Seen** | 2026-07-31 03:19 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 03:19:10` | `cowrie.session.connect` |
| `2026-07-31 03:19:10` | `cowrie.client.version` |
| `2026-07-31 03:19:10` | `cowrie.client.kex` |
| `2026-07-31 03:19:11` | `cowrie.login.success` |
| `2026-07-31 03:19:12` | `cowrie.session.params` |
| `2026-07-31 03:19:12` | `cowrie.command.input` |
| `2026-07-31 03:19:12` | `cowrie.command.input` |
| `2026-07-31 03:19:12` | `cowrie.command.input` |
| `2026-07-31 03:19:12` | `cowrie.command.input` |
| `2026-07-31 03:19:12` | `cowrie.command.input` |
| `2026-07-31 03:19:12` | `cowrie.command.success` |
| `2026-07-31 03:19:12` | `cowrie.command.input` |
| `2026-07-31 03:19:12` | `cowrie.command.input` |
| `2026-07-31 03:19:12` | `cowrie.command.input` |
| `2026-07-31 03:19:12` | `cowrie.command.input` |
| `2026-07-31 03:19:13` | `cowrie.log.closed` |
| `2026-07-31 03:19:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95fa8ea53063

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-31 03:20 |
| **Last Seen** | 2026-07-31 03:20 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 03:20:21` | `cowrie.session.connect` |
| `2026-07-31 03:20:21` | `cowrie.client.version` |
| `2026-07-31 03:20:21` | `cowrie.client.kex` |
| `2026-07-31 03:20:22` | `cowrie.login.success` |
| `2026-07-31 03:20:24` | `cowrie.session.params` |
| `2026-07-31 03:20:24` | `cowrie.command.input` |
| `2026-07-31 03:20:24` | `cowrie.command.input` |
| `2026-07-31 03:20:24` | `cowrie.command.input` |
| `2026-07-31 03:20:24` | `cowrie.command.input` |
| `2026-07-31 03:20:24` | `cowrie.command.input` |
| `2026-07-31 03:20:24` | `cowrie.command.success` |
| `2026-07-31 03:20:24` | `cowrie.command.input` |
| `2026-07-31 03:20:24` | `cowrie.command.input` |
| `2026-07-31 03:20:24` | `cowrie.command.input` |
| `2026-07-31 03:20:24` | `cowrie.command.input` |
| `2026-07-31 03:20:24` | `cowrie.log.closed` |
| `2026-07-31 03:20:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8a57e43d007

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-31 03:21 |
| **Last Seen** | 2026-07-31 03:21 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 03:21:31` | `cowrie.session.connect` |
| `2026-07-31 03:21:32` | `cowrie.client.version` |
| `2026-07-31 03:21:32` | `cowrie.client.kex` |
| `2026-07-31 03:21:33` | `cowrie.login.success` |
| `2026-07-31 03:21:35` | `cowrie.session.params` |
| `2026-07-31 03:21:35` | `cowrie.command.input` |
| `2026-07-31 03:21:35` | `cowrie.command.input` |
| `2026-07-31 03:21:35` | `cowrie.command.input` |
| `2026-07-31 03:21:35` | `cowrie.command.input` |
| `2026-07-31 03:21:35` | `cowrie.command.input` |
| `2026-07-31 03:21:35` | `cowrie.command.success` |
| `2026-07-31 03:21:35` | `cowrie.command.input` |
| `2026-07-31 03:21:35` | `cowrie.command.input` |
| `2026-07-31 03:21:35` | `cowrie.command.input` |
| `2026-07-31 03:21:35` | `cowrie.command.input` |
| `2026-07-31 03:21:35` | `cowrie.log.closed` |
| `2026-07-31 03:21:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-62cd7da19d62

| Field | Detail |
|---|---|
| **Source IP** | `103.31.38[.]92` |
| **First Seen** | 2026-07-31 03:21 |
| **Last Seen** | 2026-07-31 03:21 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 03:21:36` | `cowrie.session.connect` |
| `2026-07-31 03:21:37` | `cowrie.client.version` |
| `2026-07-31 03:21:37` | `cowrie.client.kex` |
| `2026-07-31 03:21:38` | `cowrie.login.success` |
| `2026-07-31 03:21:39` | `cowrie.direct-tcpip.request` |
| `2026-07-31 03:21:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.31.38[.]92` to AbuseIPDB if not already reported
- [ ] Block `103.31.38[.]92` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df82633b13ed

| Field | Detail |
|---|---|
| **Source IP** | `31.173.66[.]222` |
| **First Seen** | 2026-07-31 03:21 |
| **Last Seen** | 2026-07-31 03:21 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 03:21:44` | `cowrie.session.connect` |
| `2026-07-31 03:21:45` | `cowrie.client.version` |
| `2026-07-31 03:21:45` | `cowrie.client.kex` |
| `2026-07-31 03:21:46` | `cowrie.login.success` |
| `2026-07-31 03:21:47` | `cowrie.direct-tcpip.request` |
| `2026-07-31 03:21:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.173.66[.]222` to AbuseIPDB if not already reported
- [ ] Block `31.173.66[.]222` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5eb6791115d

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-31 03:22 |
| **Last Seen** | 2026-07-31 03:22 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 03:22:43` | `cowrie.session.connect` |
| `2026-07-31 03:22:43` | `cowrie.client.version` |
| `2026-07-31 03:22:43` | `cowrie.client.kex` |
| `2026-07-31 03:22:44` | `cowrie.login.success` |
| `2026-07-31 03:22:46` | `cowrie.session.params` |
| `2026-07-31 03:22:46` | `cowrie.command.input` |
| `2026-07-31 03:22:46` | `cowrie.command.input` |
| `2026-07-31 03:22:46` | `cowrie.command.input` |
| `2026-07-31 03:22:46` | `cowrie.command.input` |
| `2026-07-31 03:22:46` | `cowrie.command.input` |
| `2026-07-31 03:22:46` | `cowrie.command.success` |
| `2026-07-31 03:22:46` | `cowrie.command.input` |
| `2026-07-31 03:22:46` | `cowrie.command.input` |
| `2026-07-31 03:22:46` | `cowrie.command.input` |
| `2026-07-31 03:22:46` | `cowrie.command.input` |
| `2026-07-31 03:22:46` | `cowrie.log.closed` |
| `2026-07-31 03:22:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-748e991c7f68

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-31 03:23 |
| **Last Seen** | 2026-07-31 03:23 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 03:23:56` | `cowrie.session.connect` |
| `2026-07-31 03:23:56` | `cowrie.client.version` |
| `2026-07-31 03:23:56` | `cowrie.client.kex` |
| `2026-07-31 03:23:57` | `cowrie.login.success` |
| `2026-07-31 03:23:58` | `cowrie.session.params` |
| `2026-07-31 03:23:58` | `cowrie.command.input` |
| `2026-07-31 03:23:58` | `cowrie.command.input` |
| `2026-07-31 03:23:58` | `cowrie.command.input` |
| `2026-07-31 03:23:58` | `cowrie.command.input` |
| `2026-07-31 03:23:58` | `cowrie.command.input` |
| `2026-07-31 03:23:58` | `cowrie.command.success` |
| `2026-07-31 03:23:58` | `cowrie.command.input` |
| `2026-07-31 03:23:58` | `cowrie.command.input` |
| `2026-07-31 03:23:58` | `cowrie.command.input` |
| `2026-07-31 03:23:58` | `cowrie.command.input` |
| `2026-07-31 03:23:59` | `cowrie.log.closed` |
| `2026-07-31 03:23:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a4c5cb015a0

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-31 03:25 |
| **Last Seen** | 2026-07-31 03:25 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 03:25:04` | `cowrie.session.connect` |
| `2026-07-31 03:25:05` | `cowrie.client.version` |
| `2026-07-31 03:25:05` | `cowrie.client.kex` |
| `2026-07-31 03:25:06` | `cowrie.login.success` |
| `2026-07-31 03:25:07` | `cowrie.session.params` |
| `2026-07-31 03:25:07` | `cowrie.command.input` |
| `2026-07-31 03:25:07` | `cowrie.command.input` |
| `2026-07-31 03:25:07` | `cowrie.command.input` |
| `2026-07-31 03:25:07` | `cowrie.command.input` |
| `2026-07-31 03:25:07` | `cowrie.command.input` |
| `2026-07-31 03:25:07` | `cowrie.command.success` |
| `2026-07-31 03:25:07` | `cowrie.command.input` |
| `2026-07-31 03:25:07` | `cowrie.command.input` |
| `2026-07-31 03:25:07` | `cowrie.command.input` |
| `2026-07-31 03:25:07` | `cowrie.command.input` |
| `2026-07-31 03:25:07` | `cowrie.log.closed` |
| `2026-07-31 03:25:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8e5a9a052f9

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-31 03:26 |
| **Last Seen** | 2026-07-31 03:26 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 03:26:13` | `cowrie.session.connect` |
| `2026-07-31 03:26:13` | `cowrie.client.version` |
| `2026-07-31 03:26:13` | `cowrie.client.kex` |
| `2026-07-31 03:26:14` | `cowrie.login.success` |
| `2026-07-31 03:26:16` | `cowrie.session.params` |
| `2026-07-31 03:26:16` | `cowrie.command.input` |
| `2026-07-31 03:26:16` | `cowrie.command.input` |
| `2026-07-31 03:26:16` | `cowrie.command.input` |
| `2026-07-31 03:26:16` | `cowrie.command.input` |
| `2026-07-31 03:26:16` | `cowrie.command.input` |
| `2026-07-31 03:26:16` | `cowrie.command.success` |
| `2026-07-31 03:26:16` | `cowrie.command.input` |
| `2026-07-31 03:26:16` | `cowrie.command.input` |
| `2026-07-31 03:26:16` | `cowrie.command.input` |
| `2026-07-31 03:26:16` | `cowrie.command.input` |
| `2026-07-31 03:26:16` | `cowrie.log.closed` |
| `2026-07-31 03:26:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-54df4829f426

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-31 03:27 |
| **Last Seen** | 2026-07-31 03:27 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 03:27:21` | `cowrie.session.connect` |
| `2026-07-31 03:27:21` | `cowrie.client.version` |
| `2026-07-31 03:27:21` | `cowrie.client.kex` |
| `2026-07-31 03:27:22` | `cowrie.login.success` |
| `2026-07-31 03:27:23` | `cowrie.session.params` |
| `2026-07-31 03:27:23` | `cowrie.command.input` |
| `2026-07-31 03:27:23` | `cowrie.command.input` |
| `2026-07-31 03:27:23` | `cowrie.command.input` |
| `2026-07-31 03:27:23` | `cowrie.command.input` |
| `2026-07-31 03:27:23` | `cowrie.command.input` |
| `2026-07-31 03:27:23` | `cowrie.command.success` |
| `2026-07-31 03:27:23` | `cowrie.command.input` |
| `2026-07-31 03:27:23` | `cowrie.command.input` |
| `2026-07-31 03:27:23` | `cowrie.command.input` |
| `2026-07-31 03:27:23` | `cowrie.command.input` |
| `2026-07-31 03:27:23` | `cowrie.log.closed` |
| `2026-07-31 03:27:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66b23f66e67f

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-31 03:28 |
| **Last Seen** | 2026-07-31 03:28 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 03:28:29` | `cowrie.session.connect` |
| `2026-07-31 03:28:29` | `cowrie.client.version` |
| `2026-07-31 03:28:29` | `cowrie.client.kex` |
| `2026-07-31 03:28:31` | `cowrie.login.success` |
| `2026-07-31 03:28:32` | `cowrie.session.params` |
| `2026-07-31 03:28:32` | `cowrie.command.input` |
| `2026-07-31 03:28:32` | `cowrie.command.input` |
| `2026-07-31 03:28:32` | `cowrie.command.input` |
| `2026-07-31 03:28:32` | `cowrie.command.input` |
| `2026-07-31 03:28:32` | `cowrie.command.input` |
| `2026-07-31 03:28:32` | `cowrie.command.success` |
| `2026-07-31 03:28:32` | `cowrie.command.input` |
| `2026-07-31 03:28:32` | `cowrie.command.input` |
| `2026-07-31 03:28:32` | `cowrie.command.input` |
| `2026-07-31 03:28:32` | `cowrie.command.input` |
| `2026-07-31 03:28:32` | `cowrie.log.closed` |
| `2026-07-31 03:28:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e1c83e6d84a

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-31 03:29 |
| **Last Seen** | 2026-07-31 03:29 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 03:29:40` | `cowrie.session.connect` |
| `2026-07-31 03:29:40` | `cowrie.client.version` |
| `2026-07-31 03:29:40` | `cowrie.client.kex` |
| `2026-07-31 03:29:41` | `cowrie.login.success` |
| `2026-07-31 03:29:42` | `cowrie.session.params` |
| `2026-07-31 03:29:42` | `cowrie.command.input` |
| `2026-07-31 03:29:42` | `cowrie.command.input` |
| `2026-07-31 03:29:42` | `cowrie.command.input` |
| `2026-07-31 03:29:42` | `cowrie.command.input` |
| `2026-07-31 03:29:42` | `cowrie.command.input` |
| `2026-07-31 03:29:42` | `cowrie.command.success` |
| `2026-07-31 03:29:42` | `cowrie.command.input` |
| `2026-07-31 03:29:42` | `cowrie.command.input` |
| `2026-07-31 03:29:42` | `cowrie.command.input` |
| `2026-07-31 03:29:42` | `cowrie.command.input` |
| `2026-07-31 03:29:42` | `cowrie.log.closed` |
| `2026-07-31 03:29:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7f8b41455c2

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-31 03:30 |
| **Last Seen** | 2026-07-31 03:30 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 03:30:50` | `cowrie.session.connect` |
| `2026-07-31 03:30:50` | `cowrie.client.version` |
| `2026-07-31 03:30:51` | `cowrie.client.kex` |
| `2026-07-31 03:30:52` | `cowrie.login.success` |
| `2026-07-31 03:30:53` | `cowrie.session.params` |
| `2026-07-31 03:30:53` | `cowrie.command.input` |
| `2026-07-31 03:30:53` | `cowrie.command.input` |
| `2026-07-31 03:30:53` | `cowrie.command.input` |
| `2026-07-31 03:30:53` | `cowrie.command.input` |
| `2026-07-31 03:30:53` | `cowrie.command.input` |
| `2026-07-31 03:30:53` | `cowrie.command.success` |
| `2026-07-31 03:30:53` | `cowrie.command.input` |
| `2026-07-31 03:30:53` | `cowrie.command.input` |
| `2026-07-31 03:30:53` | `cowrie.command.input` |
| `2026-07-31 03:30:53` | `cowrie.command.input` |
| `2026-07-31 03:30:54` | `cowrie.log.closed` |
| `2026-07-31 03:30:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-867212e453a3

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-31 03:32 |
| **Last Seen** | 2026-07-31 03:32 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 03:32:00` | `cowrie.session.connect` |
| `2026-07-31 03:32:01` | `cowrie.client.version` |
| `2026-07-31 03:32:01` | `cowrie.client.kex` |
| `2026-07-31 03:32:02` | `cowrie.login.success` |
| `2026-07-31 03:32:03` | `cowrie.session.params` |
| `2026-07-31 03:32:03` | `cowrie.command.input` |
| `2026-07-31 03:32:03` | `cowrie.command.input` |
| `2026-07-31 03:32:03` | `cowrie.command.input` |
| `2026-07-31 03:32:03` | `cowrie.command.input` |
| `2026-07-31 03:32:03` | `cowrie.command.input` |
| `2026-07-31 03:32:03` | `cowrie.command.success` |
| `2026-07-31 03:32:03` | `cowrie.command.input` |
| `2026-07-31 03:32:03` | `cowrie.command.input` |
| `2026-07-31 03:32:03` | `cowrie.command.input` |
| `2026-07-31 03:32:03` | `cowrie.command.input` |
| `2026-07-31 03:32:04` | `cowrie.log.closed` |
| `2026-07-31 03:32:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-399134fb833d

| Field | Detail |
|---|---|
| **Source IP** | `176.65.132[.]8` |
| **First Seen** | 2026-07-31 03:32 |
| **Last Seen** | 2026-07-31 03:32 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST, /bin/busybox TEST, cat /proc, ./` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 03:32:15` | `cowrie.session.connect` |
| `2026-07-31 03:32:16` | `cowrie.login.success` |
| `2026-07-31 03:32:16` | `cowrie.session.params` |
| `2026-07-31 03:32:17` | `cowrie.command.input` |
| `2026-07-31 03:32:17` | `cowrie.command.input` |
| `2026-07-31 03:32:18` | `cowrie.command.input` |
| `2026-07-31 03:32:18` | `cowrie.command.input` |
| `2026-07-31 03:32:18` | `cowrie.command.failed` |
| `2026-07-31 03:32:19` | `cowrie.log.closed` |
| `2026-07-31 03:32:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.132[.]8` to AbuseIPDB if not already reported
- [ ] Block `176.65.132[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6284586cc345

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]18` |
| **First Seen** | 2026-07-31 03:32 |
| **Last Seen** | 2026-07-31 03:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_OK` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 03:32:55` | `cowrie.session.connect` |
| `2026-07-31 03:32:56` | `cowrie.login.success` |
| `2026-07-31 03:32:56` | `cowrie.session.params` |
| `2026-07-31 03:32:56` | `cowrie.command.input` |
| `2026-07-31 03:32:57` | `cowrie.log.closed` |
| `2026-07-31 03:32:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]18` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]18` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a25dfaad3711

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]18` |
| **First Seen** | 2026-07-31 03:32 |
| **Last Seen** | 2026-07-31 03:33 |
| **Session Duration** | 56s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo WRITABLE >/tmp/.testfile 2>&1, ls -l /tmp/.testfile 2>&1, rm -f /tmp/.testfile, cd /tmp, for pid in /proc/[0-9]*; do pid_num="${pid##*/}"; if [ -r "$pid/maps" ]; then suspicious=true; while IFS= read -r line; do case "$line" in *"/lib/"*|*"/lib64/"*|*".so"*) suspicious=false; break;; esac; done < "$pid/maps"; if [ "$suspicious" = true ]; then kill -9 "$pid_num" 2>/dev/null; fi; fi; done;` |
| **Download Attempts** | hxxp://91.199.133[.]133:8080/deploy.sh, hxxp://91.199.133[.]133:8080/deploy.sh, 0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7 |
| **Malware Analysis** | 0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7 (LOW) |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1105 · T1222.002 · T1489 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 03:32:57` | `cowrie.session.connect` |
| `2026-07-31 03:32:59` | `cowrie.login.success` |
| `2026-07-31 03:32:59` | `cowrie.session.params` |
| `2026-07-31 03:33:00` | `cowrie.command.input` |
| `2026-07-31 03:33:01` | `cowrie.command.input` |
| `2026-07-31 03:33:01` | `cowrie.command.input` |
| `2026-07-31 03:33:01` | `cowrie.command.input` |
| `2026-07-31 03:33:02` | `cowrie.command.input` |
| `2026-07-31 03:33:02` | `cowrie.command.input` |
| `2026-07-31 03:33:03` | `cowrie.command.input` |
| `2026-07-31 03:33:03` | `cowrie.command.failed` |
| `2026-07-31 03:33:03` | `cowrie.command.failed` |
| `2026-07-31 03:33:03` | `cowrie.command.failed` |
| `2026-07-31 03:33:03` | `cowrie.command.failed` |
| `2026-07-31 03:33:03` | `cowrie.command.failed` |
| `2026-07-31 03:33:03` | `cowrie.command.failed` |
| `2026-07-31 03:33:03` | `cowrie.command.failed` |
| `2026-07-31 03:33:03` | `cowrie.command.failed` |
| `2026-07-31 03:33:03` | `cowrie.command.failed` |
| `2026-07-31 03:33:03` | `cowrie.command.failed` |
| `2026-07-31 03:33:03` | `cowrie.command.input` |
| `2026-07-31 03:33:03` | `cowrie.command.input` |
| `2026-07-31 03:33:03` | `cowrie.command.input` |
| `2026-07-31 03:33:03` | `cowrie.command.input` |
| `2026-07-31 03:33:03` | `cowrie.command.input` |
| `2026-07-31 03:33:03` | `cowrie.command.input` |
| `2026-07-31 03:33:03` | `cowrie.command.input` |
| `2026-07-31 03:33:03` | `cowrie.command.input` |
| `2026-07-31 03:33:03` | `cowrie.session.file_download` |
| `2026-07-31 03:33:03` | `cowrie.session.file_download.failed` |
| `2026-07-31 03:33:03` | `cowrie.session.file_download` |
| `2026-07-31 03:33:23` | `cowrie.command.input` |
| `2026-07-31 03:33:25` | `cowrie.command.input` |
| `2026-07-31 03:33:26` | `cowrie.command.input` |
| `2026-07-31 03:33:26` | `cowrie.command.input` |
| `2026-07-31 03:33:26` | `cowrie.command.input` |
| `2026-07-31 03:33:26` | `cowrie.command.input` |
| `2026-07-31 03:33:26` | `cowrie.command.input` |
| `2026-07-31 03:33:26` | `cowrie.command.input` |
| `2026-07-31 03:33:26` | `cowrie.command.input` |
| `2026-07-31 03:33:26` | `cowrie.command.input` |
| `2026-07-31 03:33:26` | `cowrie.command.input` |
| `2026-07-31 03:33:26` | `cowrie.command.failed` |
| `2026-07-31 03:33:26` | `cowrie.command.failed` |
| `2026-07-31 03:33:26` | `cowrie.command.failed` |
| `2026-07-31 03:33:26` | `cowrie.command.failed` |
| `2026-07-31 03:33:51` | `cowrie.session.input` |
| `2026-07-31 03:33:53` | `cowrie.session.file_download` |
| `2026-07-31 03:33:53` | `cowrie.session.file_download` |
| `2026-07-31 03:33:53` | `cowrie.log.closed` |
| `2026-07-31 03:33:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]18` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]18` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8aae183aaa41

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-31 03:33 |
| **Last Seen** | 2026-07-31 03:33 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 03:33:12` | `cowrie.session.connect` |
| `2026-07-31 03:33:12` | `cowrie.client.version` |
| `2026-07-31 03:33:12` | `cowrie.client.kex` |
| `2026-07-31 03:33:13` | `cowrie.login.success` |
| `2026-07-31 03:33:14` | `cowrie.session.params` |
| `2026-07-31 03:33:14` | `cowrie.command.input` |
| `2026-07-31 03:33:14` | `cowrie.command.input` |
| `2026-07-31 03:33:14` | `cowrie.command.input` |
| `2026-07-31 03:33:14` | `cowrie.command.input` |
| `2026-07-31 03:33:14` | `cowrie.command.input` |
| `2026-07-31 03:33:14` | `cowrie.command.success` |
| `2026-07-31 03:33:14` | `cowrie.command.input` |
| `2026-07-31 03:33:14` | `cowrie.command.input` |
| `2026-07-31 03:33:14` | `cowrie.command.input` |
| `2026-07-31 03:33:14` | `cowrie.command.input` |
| `2026-07-31 03:33:14` | `cowrie.log.closed` |
| `2026-07-31 03:33:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae47cbc219a0

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-31 03:34 |
| **Last Seen** | 2026-07-31 03:34 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 03:34:23` | `cowrie.session.connect` |
| `2026-07-31 03:34:23` | `cowrie.client.version` |
| `2026-07-31 03:34:23` | `cowrie.client.kex` |
| `2026-07-31 03:34:25` | `cowrie.login.success` |
| `2026-07-31 03:34:26` | `cowrie.session.params` |
| `2026-07-31 03:34:26` | `cowrie.command.input` |
| `2026-07-31 03:34:26` | `cowrie.command.input` |
| `2026-07-31 03:34:26` | `cowrie.command.input` |
| `2026-07-31 03:34:26` | `cowrie.command.input` |
| `2026-07-31 03:34:26` | `cowrie.command.input` |
| `2026-07-31 03:34:26` | `cowrie.command.success` |
| `2026-07-31 03:34:26` | `cowrie.command.input` |
| `2026-07-31 03:34:26` | `cowrie.command.input` |
| `2026-07-31 03:34:26` | `cowrie.command.input` |
| `2026-07-31 03:34:26` | `cowrie.command.input` |
| `2026-07-31 03:34:26` | `cowrie.log.closed` |
| `2026-07-31 03:34:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e68dafbe277

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-31 03:35 |
| **Last Seen** | 2026-07-31 03:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 03:35:08` | `cowrie.session.connect` |
| `2026-07-31 03:35:08` | `cowrie.client.version` |
| `2026-07-31 03:35:08` | `cowrie.client.kex` |
| `2026-07-31 03:35:09` | `cowrie.login.success` |
| `2026-07-31 03:35:09` | `cowrie.direct-tcpip.request` |
| `2026-07-31 03:35:09` | `cowrie.direct-tcpip.data` |
| `2026-07-31 03:35:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41530d17bde4

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-31 03:38 |
| **Last Seen** | 2026-07-31 03:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 03:38:40` | `cowrie.session.connect` |
| `2026-07-31 03:38:40` | `cowrie.client.version` |
| `2026-07-31 03:38:41` | `cowrie.client.kex` |
| `2026-07-31 03:38:41` | `cowrie.login.success` |
| `2026-07-31 03:38:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86fc77f8237d

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-31 03:38 |
| **Last Seen** | 2026-07-31 03:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 03:38:41` | `cowrie.session.connect` |
| `2026-07-31 03:38:41` | `cowrie.client.version` |
| `2026-07-31 03:38:41` | `cowrie.client.kex` |
| `2026-07-31 03:38:41` | `cowrie.login.success` |
| `2026-07-31 03:38:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-896d6a70e693

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-31 03:38 |
| **Last Seen** | 2026-07-31 03:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 03:38:49` | `cowrie.session.connect` |
| `2026-07-31 03:38:49` | `cowrie.client.version` |
| `2026-07-31 03:38:49` | `cowrie.client.kex` |
| `2026-07-31 03:38:50` | `cowrie.login.success` |
| `2026-07-31 03:38:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0a0ea2ef73e

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-31 03:38 |
| **Last Seen** | 2026-07-31 03:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 03:38:50` | `cowrie.session.connect` |
| `2026-07-31 03:38:50` | `cowrie.client.version` |
| `2026-07-31 03:38:50` | `cowrie.client.kex` |
| `2026-07-31 03:38:51` | `cowrie.login.success` |
| `2026-07-31 03:38:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4334c3bf0656

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-31 03:39 |
| **Last Seen** | 2026-07-31 03:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 03:39:56` | `cowrie.session.connect` |
| `2026-07-31 03:39:56` | `cowrie.client.version` |
| `2026-07-31 03:39:57` | `cowrie.client.kex` |
| `2026-07-31 03:39:57` | `cowrie.login.success` |
| `2026-07-31 03:39:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ad78124c6c3

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-31 03:39 |
| **Last Seen** | 2026-07-31 03:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 03:39:57` | `cowrie.session.connect` |
| `2026-07-31 03:39:57` | `cowrie.client.version` |
| `2026-07-31 03:39:57` | `cowrie.client.kex` |
| `2026-07-31 03:39:58` | `cowrie.login.success` |
| `2026-07-31 03:39:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87113b69306b

| Field | Detail |
|---|---|
| **Source IP** | `31.76.20[.]19` |
| **First Seen** | 2026-07-31 03:45 |
| **Last Seen** | 2026-07-31 03:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 03:45:15` | `cowrie.session.connect` |
| `2026-07-31 03:45:15` | `cowrie.telnet.option` |
| `2026-07-31 03:45:15` | `cowrie.telnet.option` |
| `2026-07-31 03:45:15` | `cowrie.telnet.option` |
| `2026-07-31 03:45:15` | `cowrie.client.var` |
| `2026-07-31 03:45:15` | `cowrie.telnet.exploit_attempt` |
| `2026-07-31 03:45:15` | `cowrie.telnet.option` |
| `2026-07-31 03:45:43` | `cowrie.login.success` |
| `2026-07-31 03:45:43` | `cowrie.session.params` |

**Recommended Actions:**
- [ ] Submit `31.76.20[.]19` to AbuseIPDB if not already reported
- [ ] Block `31.76.20[.]19` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4cde686669fd

| Field | Detail |
|---|---|
| **Source IP** | `189.204.230[.]91` |
| **First Seen** | 2026-07-31 03:46 |
| **Last Seen** | 2026-07-31 03:46 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 03:46:43` | `cowrie.session.connect` |
| `2026-07-31 03:46:43` | `cowrie.client.version` |
| `2026-07-31 03:46:43` | `cowrie.client.kex` |
| `2026-07-31 03:46:44` | `cowrie.login.success` |
| `2026-07-31 03:46:45` | `cowrie.session.params` |
| `2026-07-31 03:46:45` | `cowrie.command.input` |
| `2026-07-31 03:46:45` | `cowrie.command.failed` |
| `2026-07-31 03:46:45` | `cowrie.log.closed` |
| `2026-07-31 03:46:46` | `cowrie.session.params` |
| `2026-07-31 03:46:46` | `cowrie.command.input` |
| `2026-07-31 03:46:46` | `cowrie.session.file_download` |
| `2026-07-31 03:46:46` | `cowrie.log.closed` |
| `2026-07-31 03:46:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.204.230[.]91` to AbuseIPDB if not already reported
- [ ] Block `189.204.230[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf4961f38db5

| Field | Detail |
|---|---|
| **Source IP** | `189.204.230[.]91` |
| **First Seen** | 2026-07-31 03:46 |
| **Last Seen** | 2026-07-31 03:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 03:46:46` | `cowrie.session.connect` |
| `2026-07-31 03:46:46` | `cowrie.client.version` |
| `2026-07-31 03:46:46` | `cowrie.client.kex` |
| `2026-07-31 03:46:46` | `cowrie.login.success` |
| `2026-07-31 03:46:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.204.230[.]91` to AbuseIPDB if not already reported
- [ ] Block `189.204.230[.]91` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84551a3f4616

| Field | Detail |
|---|---|
| **Source IP** | `189.204.230[.]91` |
| **First Seen** | 2026-07-31 03:46 |
| **Last Seen** | 2026-07-31 03:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 03:46:46` | `cowrie.session.connect` |
| `2026-07-31 03:46:46` | `cowrie.client.version` |
| `2026-07-31 03:46:46` | `cowrie.client.kex` |
| `2026-07-31 03:46:47` | `cowrie.login.success` |
| `2026-07-31 03:46:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.204.230[.]91` to AbuseIPDB if not already reported
- [ ] Block `189.204.230[.]91` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09e112580ad4

| Field | Detail |
|---|---|
| **Source IP** | `115.245.122[.]146` |
| **First Seen** | 2026-07-31 03:48 |
| **Last Seen** | 2026-07-31 03:48 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 03:48:25` | `cowrie.session.connect` |
| `2026-07-31 03:48:26` | `cowrie.client.version` |
| `2026-07-31 03:48:26` | `cowrie.client.kex` |
| `2026-07-31 03:48:28` | `cowrie.login.success` |
| `2026-07-31 03:48:29` | `cowrie.direct-tcpip.request` |
| `2026-07-31 03:48:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.245.122[.]146` to AbuseIPDB if not already reported
- [ ] Block `115.245.122[.]146` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57a39272375c

| Field | Detail |
|---|---|
| **Source IP** | `70.89.116[.]5` |
| **First Seen** | 2026-07-31 03:48 |
| **Last Seen** | 2026-07-31 03:48 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 03:48:34` | `cowrie.session.connect` |
| `2026-07-31 03:48:35` | `cowrie.client.version` |
| `2026-07-31 03:48:35` | `cowrie.client.kex` |
| `2026-07-31 03:48:37` | `cowrie.login.success` |
| `2026-07-31 03:48:37` | `cowrie.direct-tcpip.request` |
| `2026-07-31 03:48:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `70.89.116[.]5` to AbuseIPDB if not already reported
- [ ] Block `70.89.116[.]5` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2af753f2157c

| Field | Detail |
|---|---|
| **Source IP** | `207.219.221[.]101` |
| **First Seen** | 2026-07-31 03:50 |
| **Last Seen** | 2026-07-31 03:51 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 03:50:54` | `cowrie.session.connect` |
| `2026-07-31 03:50:55` | `cowrie.client.version` |
| `2026-07-31 03:50:55` | `cowrie.client.kex` |
| `2026-07-31 03:50:56` | `cowrie.login.success` |
| `2026-07-31 03:50:56` | `cowrie.direct-tcpip.request` |
| `2026-07-31 03:51:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.219.221[.]101` to AbuseIPDB if not already reported
- [ ] Block `207.219.221[.]101` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c3193b64fde

| Field | Detail |
|---|---|
| **Source IP** | `110.14.192[.]20` |
| **First Seen** | 2026-07-31 03:51 |
| **Last Seen** | 2026-07-31 03:51 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 03:51:06` | `cowrie.session.connect` |
| `2026-07-31 03:51:07` | `cowrie.client.version` |
| `2026-07-31 03:51:07` | `cowrie.client.kex` |
| `2026-07-31 03:51:10` | `cowrie.login.success` |
| `2026-07-31 03:51:11` | `cowrie.direct-tcpip.request` |
| `2026-07-31 03:51:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.14.192[.]20` to AbuseIPDB if not already reported
- [ ] Block `110.14.192[.]20` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67910a17a5be

| Field | Detail |
|---|---|
| **Source IP** | `219.128.15[.]190` |
| **First Seen** | 2026-07-31 03:56 |
| **Last Seen** | 2026-07-31 03:57 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 03:56:55` | `cowrie.session.connect` |
| `2026-07-31 03:56:56` | `cowrie.client.version` |
| `2026-07-31 03:56:56` | `cowrie.client.kex` |
| `2026-07-31 03:56:58` | `cowrie.login.success` |
| `2026-07-31 03:56:59` | `cowrie.direct-tcpip.request` |
| `2026-07-31 03:57:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `219.128.15[.]190` to AbuseIPDB if not already reported
- [ ] Block `219.128.15[.]190` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9ea0f8a3b09

| Field | Detail |
|---|---|
| **Source IP** | `186.239.41[.]74` |
| **First Seen** | 2026-07-31 03:57 |
| **Last Seen** | 2026-07-31 03:57 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 03:57:04` | `cowrie.session.connect` |
| `2026-07-31 03:57:04` | `cowrie.client.version` |
| `2026-07-31 03:57:04` | `cowrie.client.kex` |
| `2026-07-31 03:57:06` | `cowrie.login.success` |
| `2026-07-31 03:57:07` | `cowrie.direct-tcpip.request` |
| `2026-07-31 03:57:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.239.41[.]74` to AbuseIPDB if not already reported
- [ ] Block `186.239.41[.]74` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bfd49057bc94

| Field | Detail |
|---|---|
| **Source IP** | `34.76.133[.]51` |
| **First Seen** | 2026-07-31 03:59 |
| **Last Seen** | 2026-07-31 03:59 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 03:59:34` | `cowrie.session.connect` |
| `2026-07-31 03:59:34` | `cowrie.client.version` |
| `2026-07-31 03:59:34` | `cowrie.client.kex` |
| `2026-07-31 03:59:36` | `cowrie.login.success` |
| `2026-07-31 03:59:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.76.133[.]51` to AbuseIPDB if not already reported
- [ ] Block `34.76.133[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc2a8f9400c4

| Field | Detail |
|---|---|
| **Source IP** | `171.231.191[.]101` |
| **First Seen** | 2026-07-31 04:05 |
| **Last Seen** | 2026-07-31 04:05 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 04:05:44` | `cowrie.session.connect` |
| `2026-07-31 04:05:44` | `cowrie.client.version` |
| `2026-07-31 04:05:47` | `cowrie.client.kex` |
| `2026-07-31 04:05:48` | `cowrie.login.success` |
| `2026-07-31 04:05:49` | `cowrie.direct-tcpip.request` |
| `2026-07-31 04:05:49` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-31 04:05:49` | `cowrie.direct-tcpip.data` |
| `2026-07-31 04:05:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.231.191[.]101` to AbuseIPDB if not already reported
- [ ] Block `171.231.191[.]101` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-228d3366c22f

| Field | Detail |
|---|---|
| **Source IP** | `175.198.18[.]3` |
| **First Seen** | 2026-07-31 04:06 |
| **Last Seen** | 2026-07-31 04:06 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 04:06:42` | `cowrie.session.connect` |
| `2026-07-31 04:06:43` | `cowrie.client.version` |
| `2026-07-31 04:06:43` | `cowrie.client.kex` |
| `2026-07-31 04:06:49` | `cowrie.login.success` |
| `2026-07-31 04:06:50` | `cowrie.direct-tcpip.request` |
| `2026-07-31 04:06:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.198.18[.]3` to AbuseIPDB if not already reported
- [ ] Block `175.198.18[.]3` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d02d060b86ca

| Field | Detail |
|---|---|
| **Source IP** | `103.103.53[.]44` |
| **First Seen** | 2026-07-31 04:06 |
| **Last Seen** | 2026-07-31 04:07 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 04:06:56` | `cowrie.session.connect` |
| `2026-07-31 04:06:57` | `cowrie.client.version` |
| `2026-07-31 04:06:57` | `cowrie.client.kex` |
| `2026-07-31 04:06:59` | `cowrie.login.success` |
| `2026-07-31 04:07:00` | `cowrie.direct-tcpip.request` |
| `2026-07-31 04:07:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.103.53[.]44` to AbuseIPDB if not already reported
- [ ] Block `103.103.53[.]44` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e265f88b5350

| Field | Detail |
|---|---|
| **Source IP** | `171.231.191[.]101` |
| **First Seen** | 2026-07-31 04:09 |
| **Last Seen** | 2026-07-31 04:09 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 04:09:50` | `cowrie.session.connect` |
| `2026-07-31 04:09:50` | `cowrie.client.version` |
| `2026-07-31 04:09:50` | `cowrie.client.kex` |
| `2026-07-31 04:09:51` | `cowrie.login.success` |
| `2026-07-31 04:09:52` | `cowrie.direct-tcpip.request` |
| `2026-07-31 04:09:52` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-31 04:09:52` | `cowrie.direct-tcpip.data` |
| `2026-07-31 04:09:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.231.191[.]101` to AbuseIPDB if not already reported
- [ ] Block `171.231.191[.]101` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f10a9aa350e4

| Field | Detail |
|---|---|
| **Source IP** | `171.231.191[.]7` |
| **First Seen** | 2026-07-31 04:11 |
| **Last Seen** | 2026-07-31 04:11 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 04:11:48` | `cowrie.session.connect` |
| `2026-07-31 04:11:48` | `cowrie.client.version` |
| `2026-07-31 04:11:48` | `cowrie.client.kex` |
| `2026-07-31 04:11:49` | `cowrie.login.success` |
| `2026-07-31 04:11:50` | `cowrie.direct-tcpip.request` |
| `2026-07-31 04:11:50` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-31 04:11:50` | `cowrie.direct-tcpip.data` |
| `2026-07-31 04:11:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.231.191[.]7` to AbuseIPDB if not already reported
- [ ] Block `171.231.191[.]7` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-35e1f02455d9

| Field | Detail |
|---|---|
| **Source IP** | `171.231.191[.]7` |
| **First Seen** | 2026-07-31 04:12 |
| **Last Seen** | 2026-07-31 04:12 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 04:12:12` | `cowrie.session.connect` |
| `2026-07-31 04:12:12` | `cowrie.client.version` |
| `2026-07-31 04:12:12` | `cowrie.client.kex` |
| `2026-07-31 04:12:23` | `cowrie.login.success` |
| `2026-07-31 04:12:23` | `cowrie.direct-tcpip.request` |
| `2026-07-31 04:12:23` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-31 04:12:23` | `cowrie.direct-tcpip.data` |
| `2026-07-31 04:12:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.231.191[.]7` to AbuseIPDB if not already reported
- [ ] Block `171.231.191[.]7` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2955c203848

| Field | Detail |
|---|---|
| **Source IP** | `171.231.191[.]101` |
| **First Seen** | 2026-07-31 04:15 |
| **Last Seen** | 2026-07-31 04:15 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 04:15:37` | `cowrie.session.connect` |
| `2026-07-31 04:15:37` | `cowrie.client.version` |
| `2026-07-31 04:15:37` | `cowrie.client.kex` |
| `2026-07-31 04:15:51` | `cowrie.login.success` |
| `2026-07-31 04:15:52` | `cowrie.direct-tcpip.request` |
| `2026-07-31 04:15:52` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-31 04:15:52` | `cowrie.direct-tcpip.data` |
| `2026-07-31 04:15:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.231.191[.]101` to AbuseIPDB if not already reported
- [ ] Block `171.231.191[.]101` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5029901ea53

| Field | Detail |
|---|---|
| **Source IP** | `107.135.117[.]245` |
| **First Seen** | 2026-07-31 04:16 |
| **Last Seen** | 2026-07-31 04:16 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 04:16:06` | `cowrie.session.connect` |
| `2026-07-31 04:16:07` | `cowrie.client.version` |
| `2026-07-31 04:16:07` | `cowrie.client.kex` |
| `2026-07-31 04:16:08` | `cowrie.login.success` |
| `2026-07-31 04:16:09` | `cowrie.direct-tcpip.request` |
| `2026-07-31 04:16:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.135.117[.]245` to AbuseIPDB if not already reported
- [ ] Block `107.135.117[.]245` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91f59e94d973

| Field | Detail |
|---|---|
| **Source IP** | `111.70.6[.]20` |
| **First Seen** | 2026-07-31 04:16 |
| **Last Seen** | 2026-07-31 04:16 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 04:16:14` | `cowrie.session.connect` |
| `2026-07-31 04:16:15` | `cowrie.client.version` |
| `2026-07-31 04:16:15` | `cowrie.client.kex` |
| `2026-07-31 04:16:17` | `cowrie.login.success` |
| `2026-07-31 04:16:18` | `cowrie.direct-tcpip.request` |
| `2026-07-31 04:16:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.6[.]20` to AbuseIPDB if not already reported
- [ ] Block `111.70.6[.]20` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-419c8da95cfb

| Field | Detail |
|---|---|
| **Source IP** | `85.11.167[.]228` |
| **First Seen** | 2026-07-31 04:17 |
| **Last Seen** | 2026-07-31 04:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a ; echo 'vT'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 04:17:10` | `cowrie.session.connect` |
| `2026-07-31 04:17:10` | `cowrie.client.version` |
| `2026-07-31 04:17:11` | `cowrie.client.kex` |
| `2026-07-31 04:17:11` | `cowrie.login.success` |
| `2026-07-31 04:17:11` | `cowrie.session.params` |
| `2026-07-31 04:17:11` | `cowrie.command.input` |
| `2026-07-31 04:17:12` | `cowrie.log.closed` |
| `2026-07-31 04:17:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.11.167[.]228` to AbuseIPDB if not already reported
- [ ] Block `85.11.167[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9a70ccdd25f

| Field | Detail |
|---|---|
| **Source IP** | `85.11.167[.]228` |
| **First Seen** | 2026-07-31 04:17 |
| **Last Seen** | 2026-07-31 04:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a ; echo 'vT'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 04:17:13` | `cowrie.session.connect` |
| `2026-07-31 04:17:13` | `cowrie.client.version` |
| `2026-07-31 04:17:13` | `cowrie.client.kex` |
| `2026-07-31 04:17:14` | `cowrie.login.success` |
| `2026-07-31 04:17:14` | `cowrie.session.params` |
| `2026-07-31 04:17:14` | `cowrie.command.input` |
| `2026-07-31 04:17:15` | `cowrie.log.closed` |
| `2026-07-31 04:17:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.11.167[.]228` to AbuseIPDB if not already reported
- [ ] Block `85.11.167[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ea570fff40d

| Field | Detail |
|---|---|
| **Source IP** | `85.11.167[.]228` |
| **First Seen** | 2026-07-31 04:17 |
| **Last Seen** | 2026-07-31 04:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a ; echo 'vT'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 04:17:16` | `cowrie.session.connect` |
| `2026-07-31 04:17:16` | `cowrie.client.version` |
| `2026-07-31 04:17:16` | `cowrie.client.kex` |
| `2026-07-31 04:17:16` | `cowrie.login.success` |
| `2026-07-31 04:17:17` | `cowrie.session.params` |
| `2026-07-31 04:17:17` | `cowrie.command.input` |
| `2026-07-31 04:17:17` | `cowrie.log.closed` |
| `2026-07-31 04:17:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.11.167[.]228` to AbuseIPDB if not already reported
- [ ] Block `85.11.167[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a088026c1b1

| Field | Detail |
|---|---|
| **Source IP** | `85.11.167[.]228` |
| **First Seen** | 2026-07-31 04:17 |
| **Last Seen** | 2026-07-31 04:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a ; echo 'vT'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 04:17:18` | `cowrie.session.connect` |
| `2026-07-31 04:17:18` | `cowrie.client.version` |
| `2026-07-31 04:17:18` | `cowrie.client.kex` |
| `2026-07-31 04:17:18` | `cowrie.login.success` |
| `2026-07-31 04:17:19` | `cowrie.session.params` |
| `2026-07-31 04:17:19` | `cowrie.command.input` |
| `2026-07-31 04:17:19` | `cowrie.log.closed` |
| `2026-07-31 04:17:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.11.167[.]228` to AbuseIPDB if not already reported
- [ ] Block `85.11.167[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02d64f44c778

| Field | Detail |
|---|---|
| **Source IP** | `85.11.167[.]228` |
| **First Seen** | 2026-07-31 04:17 |
| **Last Seen** | 2026-07-31 04:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a ; echo 'vT'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 04:17:19` | `cowrie.session.connect` |
| `2026-07-31 04:17:19` | `cowrie.client.version` |
| `2026-07-31 04:17:19` | `cowrie.client.kex` |
| `2026-07-31 04:17:19` | `cowrie.login.success` |
| `2026-07-31 04:17:20` | `cowrie.session.params` |
| `2026-07-31 04:17:20` | `cowrie.command.input` |
| `2026-07-31 04:17:20` | `cowrie.log.closed` |
| `2026-07-31 04:17:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.11.167[.]228` to AbuseIPDB if not already reported
- [ ] Block `85.11.167[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65661579ce87

| Field | Detail |
|---|---|
| **Source IP** | `85.11.167[.]228` |
| **First Seen** | 2026-07-31 04:17 |
| **Last Seen** | 2026-07-31 04:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a ; echo 'vT'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 04:17:20` | `cowrie.session.connect` |
| `2026-07-31 04:17:20` | `cowrie.client.version` |
| `2026-07-31 04:17:20` | `cowrie.client.kex` |
| `2026-07-31 04:17:21` | `cowrie.login.success` |
| `2026-07-31 04:17:21` | `cowrie.session.params` |
| `2026-07-31 04:17:21` | `cowrie.command.input` |
| `2026-07-31 04:17:21` | `cowrie.log.closed` |
| `2026-07-31 04:17:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.11.167[.]228` to AbuseIPDB if not already reported
- [ ] Block `85.11.167[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3333ba430ef

| Field | Detail |
|---|---|
| **Source IP** | `85.11.167[.]228` |
| **First Seen** | 2026-07-31 04:17 |
| **Last Seen** | 2026-07-31 04:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a ; echo 'vT'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 04:17:22` | `cowrie.session.connect` |
| `2026-07-31 04:17:22` | `cowrie.client.version` |
| `2026-07-31 04:17:22` | `cowrie.client.kex` |
| `2026-07-31 04:17:22` | `cowrie.login.success` |
| `2026-07-31 04:17:23` | `cowrie.session.params` |
| `2026-07-31 04:17:23` | `cowrie.command.input` |
| `2026-07-31 04:17:23` | `cowrie.log.closed` |
| `2026-07-31 04:17:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.11.167[.]228` to AbuseIPDB if not already reported
- [ ] Block `85.11.167[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dcaca762abf0

| Field | Detail |
|---|---|
| **Source IP** | `85.11.167[.]228` |
| **First Seen** | 2026-07-31 04:17 |
| **Last Seen** | 2026-07-31 04:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a ; echo 'vT'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 04:17:23` | `cowrie.session.connect` |
| `2026-07-31 04:17:23` | `cowrie.client.version` |
| `2026-07-31 04:17:23` | `cowrie.client.kex` |
| `2026-07-31 04:17:23` | `cowrie.login.success` |
| `2026-07-31 04:17:24` | `cowrie.session.params` |
| `2026-07-31 04:17:24` | `cowrie.command.input` |
| `2026-07-31 04:17:24` | `cowrie.log.closed` |
| `2026-07-31 04:17:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.11.167[.]228` to AbuseIPDB if not already reported
- [ ] Block `85.11.167[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b361fc19eb45

| Field | Detail |
|---|---|
| **Source IP** | `85.11.167[.]228` |
| **First Seen** | 2026-07-31 04:17 |
| **Last Seen** | 2026-07-31 04:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a ; echo 'vT'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 04:17:24` | `cowrie.session.connect` |
| `2026-07-31 04:17:24` | `cowrie.client.version` |
| `2026-07-31 04:17:24` | `cowrie.client.kex` |
| `2026-07-31 04:17:25` | `cowrie.login.success` |
| `2026-07-31 04:17:25` | `cowrie.session.params` |
| `2026-07-31 04:17:25` | `cowrie.command.input` |
| `2026-07-31 04:17:25` | `cowrie.log.closed` |
| `2026-07-31 04:17:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.11.167[.]228` to AbuseIPDB if not already reported
- [ ] Block `85.11.167[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a278171bf6f3

| Field | Detail |
|---|---|
| **Source IP** | `85.11.167[.]228` |
| **First Seen** | 2026-07-31 04:17 |
| **Last Seen** | 2026-07-31 04:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a ; echo 'vT'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 04:17:25` | `cowrie.session.connect` |
| `2026-07-31 04:17:25` | `cowrie.client.version` |
| `2026-07-31 04:17:25` | `cowrie.client.kex` |
| `2026-07-31 04:17:26` | `cowrie.login.success` |
| `2026-07-31 04:17:27` | `cowrie.session.params` |
| `2026-07-31 04:17:27` | `cowrie.command.input` |
| `2026-07-31 04:17:27` | `cowrie.log.closed` |
| `2026-07-31 04:17:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.11.167[.]228` to AbuseIPDB if not already reported
- [ ] Block `85.11.167[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5486dc35078a

| Field | Detail |
|---|---|
| **Source IP** | `85.11.167[.]228` |
| **First Seen** | 2026-07-31 04:17 |
| **Last Seen** | 2026-07-31 04:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a ; echo 'vT'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 04:17:27` | `cowrie.session.connect` |
| `2026-07-31 04:17:27` | `cowrie.client.version` |
| `2026-07-31 04:17:27` | `cowrie.client.kex` |
| `2026-07-31 04:17:27` | `cowrie.login.success` |
| `2026-07-31 04:17:28` | `cowrie.session.params` |
| `2026-07-31 04:17:28` | `cowrie.command.input` |
| `2026-07-31 04:17:28` | `cowrie.log.closed` |
| `2026-07-31 04:17:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.11.167[.]228` to AbuseIPDB if not already reported
- [ ] Block `85.11.167[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c14b2733b19

| Field | Detail |
|---|---|
| **Source IP** | `85.11.167[.]228` |
| **First Seen** | 2026-07-31 04:17 |
| **Last Seen** | 2026-07-31 04:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a ; echo 'vT'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 04:17:28` | `cowrie.session.connect` |
| `2026-07-31 04:17:28` | `cowrie.client.version` |
| `2026-07-31 04:17:28` | `cowrie.client.kex` |
| `2026-07-31 04:17:28` | `cowrie.login.success` |
| `2026-07-31 04:17:29` | `cowrie.session.params` |
| `2026-07-31 04:17:29` | `cowrie.command.input` |
| `2026-07-31 04:17:29` | `cowrie.log.closed` |
| `2026-07-31 04:17:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.11.167[.]228` to AbuseIPDB if not already reported
- [ ] Block `85.11.167[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4f3222d3863

| Field | Detail |
|---|---|
| **Source IP** | `85.11.167[.]228` |
| **First Seen** | 2026-07-31 04:17 |
| **Last Seen** | 2026-07-31 04:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a ; echo 'vT'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 04:17:29` | `cowrie.session.connect` |
| `2026-07-31 04:17:29` | `cowrie.client.version` |
| `2026-07-31 04:17:29` | `cowrie.client.kex` |
| `2026-07-31 04:17:30` | `cowrie.login.success` |
| `2026-07-31 04:17:31` | `cowrie.session.params` |
| `2026-07-31 04:17:31` | `cowrie.command.input` |
| `2026-07-31 04:17:31` | `cowrie.log.closed` |
| `2026-07-31 04:17:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.11.167[.]228` to AbuseIPDB if not already reported
- [ ] Block `85.11.167[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5fa14a4a4fda

| Field | Detail |
|---|---|
| **Source IP** | `85.11.167[.]228` |
| **First Seen** | 2026-07-31 04:17 |
| **Last Seen** | 2026-07-31 04:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a ; echo 'vT'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 04:17:31` | `cowrie.session.connect` |
| `2026-07-31 04:17:31` | `cowrie.client.version` |
| `2026-07-31 04:17:31` | `cowrie.client.kex` |
| `2026-07-31 04:17:31` | `cowrie.login.success` |
| `2026-07-31 04:17:32` | `cowrie.session.params` |
| `2026-07-31 04:17:32` | `cowrie.command.input` |
| `2026-07-31 04:17:32` | `cowrie.log.closed` |
| `2026-07-31 04:17:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.11.167[.]228` to AbuseIPDB if not already reported
- [ ] Block `85.11.167[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9cc237c3598c

| Field | Detail |
|---|---|
| **Source IP** | `85.11.167[.]228` |
| **First Seen** | 2026-07-31 04:17 |
| **Last Seen** | 2026-07-31 04:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a ; echo 'vT'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 04:17:32` | `cowrie.session.connect` |
| `2026-07-31 04:17:32` | `cowrie.client.version` |
| `2026-07-31 04:17:32` | `cowrie.client.kex` |
| `2026-07-31 04:17:33` | `cowrie.login.success` |
| `2026-07-31 04:17:33` | `cowrie.session.params` |
| `2026-07-31 04:17:33` | `cowrie.command.input` |
| `2026-07-31 04:17:33` | `cowrie.log.closed` |
| `2026-07-31 04:17:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.11.167[.]228` to AbuseIPDB if not already reported
- [ ] Block `85.11.167[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-370001f5ed5e

| Field | Detail |
|---|---|
| **Source IP** | `85.11.167[.]228` |
| **First Seen** | 2026-07-31 04:17 |
| **Last Seen** | 2026-07-31 04:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a ; echo 'vT'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 04:17:33` | `cowrie.session.connect` |
| `2026-07-31 04:17:33` | `cowrie.client.version` |
| `2026-07-31 04:17:34` | `cowrie.client.kex` |
| `2026-07-31 04:17:34` | `cowrie.login.success` |
| `2026-07-31 04:17:35` | `cowrie.session.params` |
| `2026-07-31 04:17:35` | `cowrie.command.input` |
| `2026-07-31 04:17:35` | `cowrie.log.closed` |
| `2026-07-31 04:17:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.11.167[.]228` to AbuseIPDB if not already reported
- [ ] Block `85.11.167[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bfbbe9130d41

| Field | Detail |
|---|---|
| **Source IP** | `85.11.167[.]228` |
| **First Seen** | 2026-07-31 04:17 |
| **Last Seen** | 2026-07-31 04:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a ; echo 'vT'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 04:17:35` | `cowrie.session.connect` |
| `2026-07-31 04:17:35` | `cowrie.client.version` |
| `2026-07-31 04:17:35` | `cowrie.client.kex` |
| `2026-07-31 04:17:35` | `cowrie.login.success` |
| `2026-07-31 04:17:36` | `cowrie.session.params` |
| `2026-07-31 04:17:36` | `cowrie.command.input` |
| `2026-07-31 04:17:36` | `cowrie.log.closed` |
| `2026-07-31 04:17:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.11.167[.]228` to AbuseIPDB if not already reported
- [ ] Block `85.11.167[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37bae351c5ee

| Field | Detail |
|---|---|
| **Source IP** | `85.11.167[.]228` |
| **First Seen** | 2026-07-31 04:17 |
| **Last Seen** | 2026-07-31 04:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a ; echo 'vT'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 04:17:36` | `cowrie.session.connect` |
| `2026-07-31 04:17:36` | `cowrie.client.version` |
| `2026-07-31 04:17:36` | `cowrie.client.kex` |
| `2026-07-31 04:17:37` | `cowrie.login.success` |
| `2026-07-31 04:17:37` | `cowrie.session.params` |
| `2026-07-31 04:17:37` | `cowrie.command.input` |
| `2026-07-31 04:17:37` | `cowrie.log.closed` |
| `2026-07-31 04:17:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.11.167[.]228` to AbuseIPDB if not already reported
- [ ] Block `85.11.167[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-862544fc74d6

| Field | Detail |
|---|---|
| **Source IP** | `85.11.167[.]228` |
| **First Seen** | 2026-07-31 04:17 |
| **Last Seen** | 2026-07-31 04:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a ; echo 'vT'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 04:17:37` | `cowrie.session.connect` |
| `2026-07-31 04:17:37` | `cowrie.client.version` |
| `2026-07-31 04:17:38` | `cowrie.client.kex` |
| `2026-07-31 04:17:38` | `cowrie.login.success` |
| `2026-07-31 04:17:39` | `cowrie.session.params` |
| `2026-07-31 04:17:39` | `cowrie.command.input` |
| `2026-07-31 04:17:39` | `cowrie.log.closed` |
| `2026-07-31 04:17:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.11.167[.]228` to AbuseIPDB if not already reported
- [ ] Block `85.11.167[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09efb714bf8b

| Field | Detail |
|---|---|
| **Source IP** | `85.11.167[.]228` |
| **First Seen** | 2026-07-31 04:17 |
| **Last Seen** | 2026-07-31 04:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a ; echo 'vT'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 04:17:39` | `cowrie.session.connect` |
| `2026-07-31 04:17:39` | `cowrie.client.version` |
| `2026-07-31 04:17:39` | `cowrie.client.kex` |
| `2026-07-31 04:17:39` | `cowrie.login.success` |
| `2026-07-31 04:17:40` | `cowrie.session.params` |
| `2026-07-31 04:17:40` | `cowrie.command.input` |
| `2026-07-31 04:17:40` | `cowrie.log.closed` |
| `2026-07-31 04:17:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.11.167[.]228` to AbuseIPDB if not already reported
- [ ] Block `85.11.167[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ed46a0c49ae

| Field | Detail |
|---|---|
| **Source IP** | `85.11.167[.]228` |
| **First Seen** | 2026-07-31 04:17 |
| **Last Seen** | 2026-07-31 04:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a ; echo 'vT'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 04:17:40` | `cowrie.session.connect` |
| `2026-07-31 04:17:40` | `cowrie.client.version` |
| `2026-07-31 04:17:40` | `cowrie.client.kex` |
| `2026-07-31 04:17:40` | `cowrie.login.success` |
| `2026-07-31 04:17:41` | `cowrie.session.params` |
| `2026-07-31 04:17:41` | `cowrie.command.input` |
| `2026-07-31 04:17:41` | `cowrie.log.closed` |
| `2026-07-31 04:17:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.11.167[.]228` to AbuseIPDB if not already reported
- [ ] Block `85.11.167[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-441ae915500f

| Field | Detail |
|---|---|
| **Source IP** | `85.11.167[.]228` |
| **First Seen** | 2026-07-31 04:17 |
| **Last Seen** | 2026-07-31 04:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a ; echo 'vT'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 04:17:42` | `cowrie.session.connect` |
| `2026-07-31 04:17:42` | `cowrie.client.version` |
| `2026-07-31 04:17:42` | `cowrie.client.kex` |
| `2026-07-31 04:17:42` | `cowrie.login.success` |
| `2026-07-31 04:17:43` | `cowrie.session.params` |
| `2026-07-31 04:17:43` | `cowrie.command.input` |
| `2026-07-31 04:17:43` | `cowrie.log.closed` |
| `2026-07-31 04:17:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.11.167[.]228` to AbuseIPDB if not already reported
- [ ] Block `85.11.167[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f072fddd442

| Field | Detail |
|---|---|
| **Source IP** | `85.11.167[.]228` |
| **First Seen** | 2026-07-31 04:17 |
| **Last Seen** | 2026-07-31 04:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a ; echo 'vT'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 04:17:43` | `cowrie.session.connect` |
| `2026-07-31 04:17:43` | `cowrie.client.version` |
| `2026-07-31 04:17:43` | `cowrie.client.kex` |
| `2026-07-31 04:17:43` | `cowrie.login.success` |
| `2026-07-31 04:17:44` | `cowrie.session.params` |
| `2026-07-31 04:17:44` | `cowrie.command.input` |
| `2026-07-31 04:17:44` | `cowrie.log.closed` |
| `2026-07-31 04:17:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.11.167[.]228` to AbuseIPDB if not already reported
- [ ] Block `85.11.167[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c2c04a4cb3d

| Field | Detail |
|---|---|
| **Source IP** | `85.11.167[.]228` |
| **First Seen** | 2026-07-31 04:17 |
| **Last Seen** | 2026-07-31 04:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a ; echo 'vT'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 04:17:44` | `cowrie.session.connect` |
| `2026-07-31 04:17:44` | `cowrie.client.version` |
| `2026-07-31 04:17:44` | `cowrie.client.kex` |
| `2026-07-31 04:17:44` | `cowrie.login.success` |
| `2026-07-31 04:17:45` | `cowrie.session.params` |
| `2026-07-31 04:17:45` | `cowrie.command.input` |
| `2026-07-31 04:17:45` | `cowrie.log.closed` |
| `2026-07-31 04:17:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.11.167[.]228` to AbuseIPDB if not already reported
- [ ] Block `85.11.167[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6adb28509a59

| Field | Detail |
|---|---|
| **Source IP** | `171.231.191[.]101` |
| **First Seen** | 2026-07-31 04:17 |
| **Last Seen** | 2026-07-31 04:18 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 04:17:46` | `cowrie.session.connect` |
| `2026-07-31 04:17:46` | `cowrie.client.version` |
| `2026-07-31 04:17:58` | `cowrie.client.kex` |
| `2026-07-31 04:18:00` | `cowrie.login.success` |
| `2026-07-31 04:18:01` | `cowrie.direct-tcpip.request` |
| `2026-07-31 04:18:03` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-31 04:18:03` | `cowrie.direct-tcpip.data` |
| `2026-07-31 04:18:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.231.191[.]101` to AbuseIPDB if not already reported
- [ ] Block `171.231.191[.]101` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03b5ea1eb605

| Field | Detail |
|---|---|
| **Source IP** | `85.11.167[.]228` |
| **First Seen** | 2026-07-31 04:17 |
| **Last Seen** | 2026-07-31 04:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a ; echo 'vT'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 04:17:46` | `cowrie.session.connect` |
| `2026-07-31 04:17:46` | `cowrie.client.version` |
| `2026-07-31 04:17:46` | `cowrie.client.kex` |
| `2026-07-31 04:17:46` | `cowrie.login.success` |
| `2026-07-31 04:17:47` | `cowrie.session.params` |
| `2026-07-31 04:17:47` | `cowrie.command.input` |
| `2026-07-31 04:17:47` | `cowrie.log.closed` |
| `2026-07-31 04:17:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.11.167[.]228` to AbuseIPDB if not already reported
- [ ] Block `85.11.167[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5bd1e511c3df

| Field | Detail |
|---|---|
| **Source IP** | `85.11.167[.]228` |
| **First Seen** | 2026-07-31 04:17 |
| **Last Seen** | 2026-07-31 04:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a ; echo 'vT'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 04:17:47` | `cowrie.session.connect` |
| `2026-07-31 04:17:47` | `cowrie.client.version` |
| `2026-07-31 04:17:47` | `cowrie.client.kex` |
| `2026-07-31 04:17:47` | `cowrie.login.success` |
| `2026-07-31 04:17:48` | `cowrie.session.params` |
| `2026-07-31 04:17:48` | `cowrie.command.input` |
| `2026-07-31 04:17:48` | `cowrie.log.closed` |
| `2026-07-31 04:17:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.11.167[.]228` to AbuseIPDB if not already reported
- [ ] Block `85.11.167[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-537b1f8ea719

| Field | Detail |
|---|---|
| **Source IP** | `85.11.167[.]228` |
| **First Seen** | 2026-07-31 04:17 |
| **Last Seen** | 2026-07-31 04:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a ; echo 'vT'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 04:17:48` | `cowrie.session.connect` |
| `2026-07-31 04:17:48` | `cowrie.client.version` |
| `2026-07-31 04:17:48` | `cowrie.client.kex` |
| `2026-07-31 04:17:49` | `cowrie.login.success` |
| `2026-07-31 04:17:49` | `cowrie.session.params` |
| `2026-07-31 04:17:49` | `cowrie.command.input` |
| `2026-07-31 04:17:49` | `cowrie.log.closed` |
| `2026-07-31 04:17:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.11.167[.]228` to AbuseIPDB if not already reported
- [ ] Block `85.11.167[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4fcec5d66405

| Field | Detail |
|---|---|
| **Source IP** | `85.11.167[.]228` |
| **First Seen** | 2026-07-31 04:17 |
| **Last Seen** | 2026-07-31 04:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a ; echo 'vT'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 04:17:50` | `cowrie.session.connect` |
| `2026-07-31 04:17:50` | `cowrie.client.version` |
| `2026-07-31 04:17:50` | `cowrie.client.kex` |
| `2026-07-31 04:17:50` | `cowrie.login.success` |
| `2026-07-31 04:17:51` | `cowrie.session.params` |
| `2026-07-31 04:17:51` | `cowrie.command.input` |
| `2026-07-31 04:17:51` | `cowrie.log.closed` |
| `2026-07-31 04:17:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.11.167[.]228` to AbuseIPDB if not already reported
- [ ] Block `85.11.167[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc6857c231db

| Field | Detail |
|---|---|
| **Source IP** | `85.11.167[.]228` |
| **First Seen** | 2026-07-31 04:17 |
| **Last Seen** | 2026-07-31 04:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a ; echo 'vT'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 04:17:51` | `cowrie.session.connect` |
| `2026-07-31 04:17:51` | `cowrie.client.version` |
| `2026-07-31 04:17:51` | `cowrie.client.kex` |
| `2026-07-31 04:17:51` | `cowrie.login.success` |
| `2026-07-31 04:17:52` | `cowrie.session.params` |
| `2026-07-31 04:17:52` | `cowrie.command.input` |
| `2026-07-31 04:17:52` | `cowrie.log.closed` |
| `2026-07-31 04:17:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.11.167[.]228` to AbuseIPDB if not already reported
- [ ] Block `85.11.167[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-595f97a149f3

| Field | Detail |
|---|---|
| **Source IP** | `85.11.167[.]228` |
| **First Seen** | 2026-07-31 04:17 |
| **Last Seen** | 2026-07-31 04:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a ; echo 'vT'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 04:17:52` | `cowrie.session.connect` |
| `2026-07-31 04:17:52` | `cowrie.client.version` |
| `2026-07-31 04:17:52` | `cowrie.client.kex` |
| `2026-07-31 04:17:52` | `cowrie.login.success` |
| `2026-07-31 04:17:53` | `cowrie.session.params` |
| `2026-07-31 04:17:53` | `cowrie.command.input` |
| `2026-07-31 04:17:53` | `cowrie.log.closed` |
| `2026-07-31 04:17:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.11.167[.]228` to AbuseIPDB if not already reported
- [ ] Block `85.11.167[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2d162a3d5a3

| Field | Detail |
|---|---|
| **Source IP** | `85.11.167[.]228` |
| **First Seen** | 2026-07-31 04:17 |
| **Last Seen** | 2026-07-31 04:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a ; echo 'vT'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 04:17:54` | `cowrie.session.connect` |
| `2026-07-31 04:17:54` | `cowrie.client.version` |
| `2026-07-31 04:17:54` | `cowrie.client.kex` |
| `2026-07-31 04:17:54` | `cowrie.login.success` |
| `2026-07-31 04:17:55` | `cowrie.session.params` |
| `2026-07-31 04:17:55` | `cowrie.command.input` |
| `2026-07-31 04:17:55` | `cowrie.log.closed` |
| `2026-07-31 04:17:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.11.167[.]228` to AbuseIPDB if not already reported
- [ ] Block `85.11.167[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d239433c1f6f

| Field | Detail |
|---|---|
| **Source IP** | `85.11.167[.]228` |
| **First Seen** | 2026-07-31 04:17 |
| **Last Seen** | 2026-07-31 04:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a ; echo 'vT'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 04:17:55` | `cowrie.session.connect` |
| `2026-07-31 04:17:55` | `cowrie.client.version` |
| `2026-07-31 04:17:55` | `cowrie.client.kex` |
| `2026-07-31 04:17:55` | `cowrie.login.success` |
| `2026-07-31 04:17:56` | `cowrie.session.params` |
| `2026-07-31 04:17:56` | `cowrie.command.input` |
| `2026-07-31 04:17:56` | `cowrie.log.closed` |
| `2026-07-31 04:17:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.11.167[.]228` to AbuseIPDB if not already reported
- [ ] Block `85.11.167[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d28c97698f4

| Field | Detail |
|---|---|
| **Source IP** | `85.11.167[.]228` |
| **First Seen** | 2026-07-31 04:17 |
| **Last Seen** | 2026-07-31 04:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a ; echo 'vT'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 04:17:56` | `cowrie.session.connect` |
| `2026-07-31 04:17:56` | `cowrie.client.version` |
| `2026-07-31 04:17:56` | `cowrie.client.kex` |
| `2026-07-31 04:17:57` | `cowrie.login.success` |
| `2026-07-31 04:17:57` | `cowrie.session.params` |
| `2026-07-31 04:17:57` | `cowrie.command.input` |
| `2026-07-31 04:17:57` | `cowrie.log.closed` |
| `2026-07-31 04:17:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.11.167[.]228` to AbuseIPDB if not already reported
- [ ] Block `85.11.167[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ffd548726da

| Field | Detail |
|---|---|
| **Source IP** | `85.11.167[.]228` |
| **First Seen** | 2026-07-31 04:17 |
| **Last Seen** | 2026-07-31 04:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a ; echo 'vT'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 04:17:58` | `cowrie.session.connect` |
| `2026-07-31 04:17:58` | `cowrie.client.version` |
| `2026-07-31 04:17:58` | `cowrie.client.kex` |
| `2026-07-31 04:17:58` | `cowrie.login.success` |
| `2026-07-31 04:17:59` | `cowrie.session.params` |
| `2026-07-31 04:17:59` | `cowrie.command.input` |
| `2026-07-31 04:17:59` | `cowrie.log.closed` |
| `2026-07-31 04:17:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.11.167[.]228` to AbuseIPDB if not already reported
- [ ] Block `85.11.167[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88fb43dd2b62

| Field | Detail |
|---|---|
| **Source IP** | `85.11.167[.]228` |
| **First Seen** | 2026-07-31 04:17 |
| **Last Seen** | 2026-07-31 04:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a ; echo 'vT'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 04:17:59` | `cowrie.session.connect` |
| `2026-07-31 04:17:59` | `cowrie.client.version` |
| `2026-07-31 04:17:59` | `cowrie.client.kex` |
| `2026-07-31 04:17:59` | `cowrie.login.success` |
| `2026-07-31 04:18:00` | `cowrie.session.params` |
| `2026-07-31 04:18:00` | `cowrie.command.input` |
| `2026-07-31 04:18:00` | `cowrie.log.closed` |
| `2026-07-31 04:18:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.11.167[.]228` to AbuseIPDB if not already reported
- [ ] Block `85.11.167[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45c4ea2b347f

| Field | Detail |
|---|---|
| **Source IP** | `85.11.167[.]228` |
| **First Seen** | 2026-07-31 04:18 |
| **Last Seen** | 2026-07-31 04:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a ; echo 'vT'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 04:18:00` | `cowrie.session.connect` |
| `2026-07-31 04:18:00` | `cowrie.client.version` |
| `2026-07-31 04:18:00` | `cowrie.client.kex` |
| `2026-07-31 04:18:01` | `cowrie.login.success` |
| `2026-07-31 04:18:01` | `cowrie.session.params` |
| `2026-07-31 04:18:01` | `cowrie.command.input` |
| `2026-07-31 04:18:01` | `cowrie.log.closed` |
| `2026-07-31 04:18:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.11.167[.]228` to AbuseIPDB if not already reported
- [ ] Block `85.11.167[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e70e9922c66

| Field | Detail |
|---|---|
| **Source IP** | `85.11.167[.]228` |
| **First Seen** | 2026-07-31 04:18 |
| **Last Seen** | 2026-07-31 04:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a ; echo 'vT'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 04:18:01` | `cowrie.session.connect` |
| `2026-07-31 04:18:01` | `cowrie.client.version` |
| `2026-07-31 04:18:02` | `cowrie.client.kex` |
| `2026-07-31 04:18:02` | `cowrie.login.success` |
| `2026-07-31 04:18:03` | `cowrie.session.params` |
| `2026-07-31 04:18:03` | `cowrie.command.input` |
| `2026-07-31 04:18:03` | `cowrie.log.closed` |
| `2026-07-31 04:18:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.11.167[.]228` to AbuseIPDB if not already reported
- [ ] Block `85.11.167[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2540227a0748

| Field | Detail |
|---|---|
| **Source IP** | `85.11.167[.]228` |
| **First Seen** | 2026-07-31 04:18 |
| **Last Seen** | 2026-07-31 04:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a ; echo 'vT'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 04:18:03` | `cowrie.session.connect` |
| `2026-07-31 04:18:03` | `cowrie.client.version` |
| `2026-07-31 04:18:03` | `cowrie.client.kex` |
| `2026-07-31 04:18:03` | `cowrie.login.success` |
| `2026-07-31 04:18:04` | `cowrie.session.params` |
| `2026-07-31 04:18:04` | `cowrie.command.input` |
| `2026-07-31 04:18:04` | `cowrie.log.closed` |
| `2026-07-31 04:18:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.11.167[.]228` to AbuseIPDB if not already reported
- [ ] Block `85.11.167[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-783d5803c6c5

| Field | Detail |
|---|---|
| **Source IP** | `85.11.167[.]228` |
| **First Seen** | 2026-07-31 04:18 |
| **Last Seen** | 2026-07-31 04:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a ; echo 'vT'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 04:18:04` | `cowrie.session.connect` |
| `2026-07-31 04:18:04` | `cowrie.client.version` |
| `2026-07-31 04:18:04` | `cowrie.client.kex` |
| `2026-07-31 04:18:05` | `cowrie.login.success` |
| `2026-07-31 04:18:05` | `cowrie.session.params` |
| `2026-07-31 04:18:05` | `cowrie.command.input` |
| `2026-07-31 04:18:05` | `cowrie.log.closed` |
| `2026-07-31 04:18:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.11.167[.]228` to AbuseIPDB if not already reported
- [ ] Block `85.11.167[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4378f1a5ef9b

| Field | Detail |
|---|---|
| **Source IP** | `85.11.167[.]228` |
| **First Seen** | 2026-07-31 04:18 |
| **Last Seen** | 2026-07-31 04:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a ; echo 'vT'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 04:18:05` | `cowrie.session.connect` |
| `2026-07-31 04:18:05` | `cowrie.client.version` |
| `2026-07-31 04:18:06` | `cowrie.client.kex` |
| `2026-07-31 04:18:06` | `cowrie.login.success` |
| `2026-07-31 04:18:07` | `cowrie.session.params` |
| `2026-07-31 04:18:07` | `cowrie.command.input` |
| `2026-07-31 04:18:07` | `cowrie.log.closed` |
| `2026-07-31 04:18:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.11.167[.]228` to AbuseIPDB if not already reported
- [ ] Block `85.11.167[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70e86653b11a

| Field | Detail |
|---|---|
| **Source IP** | `85.11.167[.]228` |
| **First Seen** | 2026-07-31 04:18 |
| **Last Seen** | 2026-07-31 04:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a ; echo 'vT'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 04:18:07` | `cowrie.session.connect` |
| `2026-07-31 04:18:07` | `cowrie.client.version` |
| `2026-07-31 04:18:07` | `cowrie.client.kex` |
| `2026-07-31 04:18:07` | `cowrie.login.success` |
| `2026-07-31 04:18:08` | `cowrie.session.params` |
| `2026-07-31 04:18:08` | `cowrie.command.input` |
| `2026-07-31 04:18:08` | `cowrie.log.closed` |
| `2026-07-31 04:18:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.11.167[.]228` to AbuseIPDB if not already reported
- [ ] Block `85.11.167[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b660ae5da89e

| Field | Detail |
|---|---|
| **Source IP** | `85.11.167[.]228` |
| **First Seen** | 2026-07-31 04:18 |
| **Last Seen** | 2026-07-31 04:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a ; echo 'vT'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 04:18:08` | `cowrie.session.connect` |
| `2026-07-31 04:18:08` | `cowrie.client.version` |
| `2026-07-31 04:18:08` | `cowrie.client.kex` |
| `2026-07-31 04:18:09` | `cowrie.login.success` |
| `2026-07-31 04:18:09` | `cowrie.session.params` |
| `2026-07-31 04:18:09` | `cowrie.command.input` |
| `2026-07-31 04:18:09` | `cowrie.log.closed` |
| `2026-07-31 04:18:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.11.167[.]228` to AbuseIPDB if not already reported
- [ ] Block `85.11.167[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78c69b5d93b3

| Field | Detail |
|---|---|
| **Source IP** | `85.11.167[.]228` |
| **First Seen** | 2026-07-31 04:18 |
| **Last Seen** | 2026-07-31 04:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a ; echo 'vT'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 04:18:10` | `cowrie.session.connect` |
| `2026-07-31 04:18:10` | `cowrie.client.version` |
| `2026-07-31 04:18:10` | `cowrie.client.kex` |
| `2026-07-31 04:18:10` | `cowrie.login.success` |
| `2026-07-31 04:18:11` | `cowrie.session.params` |
| `2026-07-31 04:18:11` | `cowrie.command.input` |
| `2026-07-31 04:18:11` | `cowrie.log.closed` |
| `2026-07-31 04:18:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.11.167[.]228` to AbuseIPDB if not already reported
- [ ] Block `85.11.167[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4bea912b6280

| Field | Detail |
|---|---|
| **Source IP** | `85.11.167[.]228` |
| **First Seen** | 2026-07-31 04:18 |
| **Last Seen** | 2026-07-31 04:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a ; echo 'vT'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 04:18:11` | `cowrie.session.connect` |
| `2026-07-31 04:18:11` | `cowrie.client.version` |
| `2026-07-31 04:18:11` | `cowrie.client.kex` |
| `2026-07-31 04:18:11` | `cowrie.login.success` |
| `2026-07-31 04:18:12` | `cowrie.session.params` |
| `2026-07-31 04:18:12` | `cowrie.command.input` |
| `2026-07-31 04:18:12` | `cowrie.log.closed` |
| `2026-07-31 04:18:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.11.167[.]228` to AbuseIPDB if not already reported
- [ ] Block `85.11.167[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c05cdd368950

| Field | Detail |
|---|---|
| **Source IP** | `85.11.167[.]228` |
| **First Seen** | 2026-07-31 04:18 |
| **Last Seen** | 2026-07-31 04:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a ; echo 'vT'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 04:18:12` | `cowrie.session.connect` |
| `2026-07-31 04:18:12` | `cowrie.client.version` |
| `2026-07-31 04:18:13` | `cowrie.client.kex` |
| `2026-07-31 04:18:13` | `cowrie.login.success` |
| `2026-07-31 04:18:13` | `cowrie.session.params` |
| `2026-07-31 04:18:13` | `cowrie.command.input` |
| `2026-07-31 04:18:14` | `cowrie.log.closed` |
| `2026-07-31 04:18:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.11.167[.]228` to AbuseIPDB if not already reported
- [ ] Block `85.11.167[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c827736959d3

| Field | Detail |
|---|---|
| **Source IP** | `85.11.167[.]228` |
| **First Seen** | 2026-07-31 04:18 |
| **Last Seen** | 2026-07-31 04:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a ; echo 'vT'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 04:18:14` | `cowrie.session.connect` |
| `2026-07-31 04:18:14` | `cowrie.client.version` |
| `2026-07-31 04:18:14` | `cowrie.client.kex` |
| `2026-07-31 04:18:14` | `cowrie.login.success` |
| `2026-07-31 04:18:15` | `cowrie.session.params` |
| `2026-07-31 04:18:15` | `cowrie.command.input` |
| `2026-07-31 04:18:15` | `cowrie.log.closed` |
| `2026-07-31 04:18:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.11.167[.]228` to AbuseIPDB if not already reported
- [ ] Block `85.11.167[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ccb610b4677e

| Field | Detail |
|---|---|
| **Source IP** | `85.11.167[.]228` |
| **First Seen** | 2026-07-31 04:18 |
| **Last Seen** | 2026-07-31 04:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a ; echo 'vT'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 04:18:15` | `cowrie.session.connect` |
| `2026-07-31 04:18:15` | `cowrie.client.version` |
| `2026-07-31 04:18:15` | `cowrie.client.kex` |
| `2026-07-31 04:18:15` | `cowrie.login.success` |
| `2026-07-31 04:18:16` | `cowrie.session.params` |
| `2026-07-31 04:18:16` | `cowrie.command.input` |
| `2026-07-31 04:18:16` | `cowrie.log.closed` |
| `2026-07-31 04:18:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.11.167[.]228` to AbuseIPDB if not already reported
- [ ] Block `85.11.167[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e985503d054

| Field | Detail |
|---|---|
| **Source IP** | `85.11.167[.]228` |
| **First Seen** | 2026-07-31 04:18 |
| **Last Seen** | 2026-07-31 04:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a ; echo 'vT'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 04:18:16` | `cowrie.session.connect` |
| `2026-07-31 04:18:16` | `cowrie.client.version` |
| `2026-07-31 04:18:16` | `cowrie.client.kex` |
| `2026-07-31 04:18:17` | `cowrie.login.success` |
| `2026-07-31 04:18:17` | `cowrie.session.params` |
| `2026-07-31 04:18:17` | `cowrie.command.input` |
| `2026-07-31 04:18:18` | `cowrie.log.closed` |
| `2026-07-31 04:18:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.11.167[.]228` to AbuseIPDB if not already reported
- [ ] Block `85.11.167[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eec957b18201

| Field | Detail |
|---|---|
| **Source IP** | `85.11.167[.]228` |
| **First Seen** | 2026-07-31 04:18 |
| **Last Seen** | 2026-07-31 04:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a ; echo 'vT'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 04:18:18` | `cowrie.session.connect` |
| `2026-07-31 04:18:18` | `cowrie.client.version` |
| `2026-07-31 04:18:18` | `cowrie.client.kex` |
| `2026-07-31 04:18:18` | `cowrie.login.success` |
| `2026-07-31 04:18:19` | `cowrie.session.params` |
| `2026-07-31 04:18:19` | `cowrie.command.input` |
| `2026-07-31 04:18:19` | `cowrie.log.closed` |
| `2026-07-31 04:18:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.11.167[.]228` to AbuseIPDB if not already reported
- [ ] Block `85.11.167[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1813d4cd532

| Field | Detail |
|---|---|
| **Source IP** | `171.231.191[.]7` |
| **First Seen** | 2026-07-31 04:19 |
| **Last Seen** | 2026-07-31 04:19 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 04:19:01` | `cowrie.session.connect` |
| `2026-07-31 04:19:01` | `cowrie.client.version` |
| `2026-07-31 04:19:01` | `cowrie.client.kex` |
| `2026-07-31 04:19:04` | `cowrie.login.success` |
| `2026-07-31 04:19:04` | `cowrie.direct-tcpip.request` |
| `2026-07-31 04:19:04` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-31 04:19:04` | `cowrie.direct-tcpip.data` |
| `2026-07-31 04:19:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.231.191[.]7` to AbuseIPDB if not already reported
- [ ] Block `171.231.191[.]7` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a892c7daeea

| Field | Detail |
|---|---|
| **Source IP** | `171.231.191[.]7` |
| **First Seen** | 2026-07-31 04:20 |
| **Last Seen** | 2026-07-31 04:20 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 04:20:09` | `cowrie.session.connect` |
| `2026-07-31 04:20:09` | `cowrie.client.version` |
| `2026-07-31 04:20:21` | `cowrie.client.kex` |
| `2026-07-31 04:20:24` | `cowrie.login.success` |
| `2026-07-31 04:20:24` | `cowrie.direct-tcpip.request` |
| `2026-07-31 04:20:24` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-31 04:20:24` | `cowrie.direct-tcpip.data` |
| `2026-07-31 04:20:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.231.191[.]7` to AbuseIPDB if not already reported
- [ ] Block `171.231.191[.]7` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16912f578810

| Field | Detail |
|---|---|
| **Source IP** | `8.219.248[.]7` |
| **First Seen** | 2026-07-31 04:20 |
| **Last Seen** | 2026-07-31 04:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 04:20:52` | `cowrie.session.connect` |
| `2026-07-31 04:20:52` | `cowrie.client.version` |
| `2026-07-31 04:20:52` | `cowrie.client.kex` |
| `2026-07-31 04:20:54` | `cowrie.login.success` |
| `2026-07-31 04:20:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.219.248[.]7` to AbuseIPDB if not already reported
- [ ] Block `8.219.248[.]7` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47203e8f2529

| Field | Detail |
|---|---|
| **Source IP** | `103.112.224[.]81` |
| **First Seen** | 2026-07-31 04:22 |
| **Last Seen** | 2026-07-31 04:22 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 04:22:48` | `cowrie.session.connect` |
| `2026-07-31 04:22:49` | `cowrie.client.version` |
| `2026-07-31 04:22:49` | `cowrie.client.kex` |
| `2026-07-31 04:22:51` | `cowrie.login.success` |
| `2026-07-31 04:22:51` | `cowrie.direct-tcpip.request` |
| `2026-07-31 04:22:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.112.224[.]81` to AbuseIPDB if not already reported
- [ ] Block `103.112.224[.]81` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-abbb597d4f74

| Field | Detail |
|---|---|
| **Source IP** | `106.245.246[.]26` |
| **First Seen** | 2026-07-31 04:23 |
| **Last Seen** | 2026-07-31 04:23 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 04:23:01` | `cowrie.session.connect` |
| `2026-07-31 04:23:02` | `cowrie.client.version` |
| `2026-07-31 04:23:02` | `cowrie.client.kex` |
| `2026-07-31 04:23:04` | `cowrie.login.success` |
| `2026-07-31 04:23:05` | `cowrie.direct-tcpip.request` |
| `2026-07-31 04:23:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.245.246[.]26` to AbuseIPDB if not already reported
- [ ] Block `106.245.246[.]26` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7cac69d83bf

| Field | Detail |
|---|---|
| **Source IP** | `113.28.86[.]1` |
| **First Seen** | 2026-07-31 04:23 |
| **Last Seen** | 2026-07-31 04:23 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 04:23:06` | `cowrie.session.connect` |
| `2026-07-31 04:23:07` | `cowrie.client.version` |
| `2026-07-31 04:23:07` | `cowrie.client.kex` |
| `2026-07-31 04:23:09` | `cowrie.login.success` |
| `2026-07-31 04:23:10` | `cowrie.direct-tcpip.request` |
| `2026-07-31 04:23:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.28.86[.]1` to AbuseIPDB if not already reported
- [ ] Block `113.28.86[.]1` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c93cd241fa3e

| Field | Detail |
|---|---|
| **Source IP** | `170.247.3[.]14` |
| **First Seen** | 2026-07-31 04:23 |
| **Last Seen** | 2026-07-31 04:23 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 04:23:09` | `cowrie.session.connect` |
| `2026-07-31 04:23:10` | `cowrie.client.version` |
| `2026-07-31 04:23:10` | `cowrie.client.kex` |
| `2026-07-31 04:23:11` | `cowrie.login.success` |
| `2026-07-31 04:23:11` | `cowrie.direct-tcpip.request` |
| `2026-07-31 04:23:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.247.3[.]14` to AbuseIPDB if not already reported
- [ ] Block `170.247.3[.]14` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b169bddc4f4

| Field | Detail |
|---|---|
| **Source IP** | `179.185.18[.]67` |
| **First Seen** | 2026-07-31 04:23 |
| **Last Seen** | 2026-07-31 04:23 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 04:23:17` | `cowrie.session.connect` |
| `2026-07-31 04:23:18` | `cowrie.client.version` |
| `2026-07-31 04:23:18` | `cowrie.client.kex` |
| `2026-07-31 04:23:19` | `cowrie.login.success` |
| `2026-07-31 04:23:19` | `cowrie.direct-tcpip.request` |
| `2026-07-31 04:23:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.185.18[.]67` to AbuseIPDB if not already reported
- [ ] Block `179.185.18[.]67` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28424b9ff3d4

| Field | Detail |
|---|---|
| **Source IP** | `171.231.191[.]101` |
| **First Seen** | 2026-07-31 04:23 |
| **Last Seen** | 2026-07-31 04:23 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 04:23:44` | `cowrie.session.connect` |
| `2026-07-31 04:23:44` | `cowrie.client.version` |
| `2026-07-31 04:23:46` | `cowrie.client.kex` |
| `2026-07-31 04:23:50` | `cowrie.login.success` |
| `2026-07-31 04:23:51` | `cowrie.direct-tcpip.request` |
| `2026-07-31 04:23:51` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-31 04:23:51` | `cowrie.direct-tcpip.data` |
| `2026-07-31 04:23:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.231.191[.]101` to AbuseIPDB if not already reported
- [ ] Block `171.231.191[.]101` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-edaf18f6b3c7

| Field | Detail |
|---|---|
| **Source IP** | `213.154.80[.]51` |
| **First Seen** | 2026-07-31 04:23 |
| **Last Seen** | 2026-07-31 04:24 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 04:23:54` | `cowrie.session.connect` |
| `2026-07-31 04:23:54` | `cowrie.client.version` |
| `2026-07-31 04:23:54` | `cowrie.client.kex` |
| `2026-07-31 04:23:55` | `cowrie.login.success` |
| `2026-07-31 04:23:56` | `cowrie.direct-tcpip.request` |
| `2026-07-31 04:24:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.154.80[.]51` to AbuseIPDB if not already reported
- [ ] Block `213.154.80[.]51` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2a3151206e5

| Field | Detail |
|---|---|
| **Source IP** | `78.187.9[.]111` |
| **First Seen** | 2026-07-31 04:24 |
| **Last Seen** | 2026-07-31 04:24 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 04:24:01` | `cowrie.session.connect` |
| `2026-07-31 04:24:01` | `cowrie.client.version` |
| `2026-07-31 04:24:01` | `cowrie.client.kex` |
| `2026-07-31 04:24:02` | `cowrie.login.success` |
| `2026-07-31 04:24:03` | `cowrie.direct-tcpip.request` |
| `2026-07-31 04:24:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `78.187.9[.]111` to AbuseIPDB if not already reported
- [ ] Block `78.187.9[.]111` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a44fd9f97b54

| Field | Detail |
|---|---|
| **Source IP** | `24.207.66[.]154` |
| **First Seen** | 2026-07-31 04:26 |
| **Last Seen** | 2026-07-31 04:26 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 04:26:31` | `cowrie.session.connect` |
| `2026-07-31 04:26:32` | `cowrie.client.version` |
| `2026-07-31 04:26:32` | `cowrie.client.kex` |
| `2026-07-31 04:26:33` | `cowrie.login.success` |
| `2026-07-31 04:26:33` | `cowrie.direct-tcpip.request` |
| `2026-07-31 04:26:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `24.207.66[.]154` to AbuseIPDB if not already reported
- [ ] Block `24.207.66[.]154` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b89e7ad1d356

| Field | Detail |
|---|---|
| **Source IP** | `171.231.191[.]7` |
| **First Seen** | 2026-07-31 04:27 |
| **Last Seen** | 2026-07-31 04:29 |
| **Session Duration** | 151s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 04:27:09` | `cowrie.session.connect` |
| `2026-07-31 04:27:09` | `cowrie.client.version` |
| `2026-07-31 04:27:09` | `cowrie.client.kex` |
| `2026-07-31 04:28:52` | `cowrie.login.success` |
| `2026-07-31 04:29:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.231.191[.]7` to AbuseIPDB if not already reported
- [ ] Block `171.231.191[.]7` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aadf25c4a8eb

| Field | Detail |
|---|---|
| **Source IP** | `171.231.191[.]7` |
| **First Seen** | 2026-07-31 04:29 |
| **Last Seen** | 2026-07-31 04:29 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 04:29:31` | `cowrie.session.connect` |
| `2026-07-31 04:29:31` | `cowrie.client.version` |
| `2026-07-31 04:29:31` | `cowrie.client.kex` |
| `2026-07-31 04:29:41` | `cowrie.login.success` |
| `2026-07-31 04:29:43` | `cowrie.direct-tcpip.request` |
| `2026-07-31 04:29:44` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-31 04:29:44` | `cowrie.direct-tcpip.data` |
| `2026-07-31 04:29:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.231.191[.]7` to AbuseIPDB if not already reported
- [ ] Block `171.231.191[.]7` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4110f9c1dae9

| Field | Detail |
|---|---|
| **Source IP** | `171.231.191[.]101` |
| **First Seen** | 2026-07-31 04:31 |
| **Last Seen** | 2026-07-31 04:33 |
| **Session Duration** | 131s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 04:31:21` | `cowrie.session.connect` |
| `2026-07-31 04:31:21` | `cowrie.client.version` |
| `2026-07-31 04:31:22` | `cowrie.client.kex` |
| `2026-07-31 04:31:43` | `cowrie.login.success` |
| `2026-07-31 04:33:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.231.191[.]101` to AbuseIPDB if not already reported
- [ ] Block `171.231.191[.]101` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f328e3fa2a5d

| Field | Detail |
|---|---|
| **Source IP** | `116.110.17[.]78` |
| **First Seen** | 2026-07-31 04:34 |
| **Last Seen** | 2026-07-31 04:34 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 04:34:08` | `cowrie.session.connect` |
| `2026-07-31 04:34:08` | `cowrie.client.version` |
| `2026-07-31 04:34:09` | `cowrie.client.kex` |
| `2026-07-31 04:34:12` | `cowrie.login.success` |
| `2026-07-31 04:34:13` | `cowrie.direct-tcpip.request` |
| `2026-07-31 04:34:13` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-31 04:34:13` | `cowrie.direct-tcpip.data` |
| `2026-07-31 04:34:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.110.17[.]78` to AbuseIPDB if not already reported
- [ ] Block `116.110.17[.]78` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-508c78fecfc8

| Field | Detail |
|---|---|
| **Source IP** | `171.231.191[.]101` |
| **First Seen** | 2026-07-31 04:36 |
| **Last Seen** | 2026-07-31 04:36 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 04:36:26` | `cowrie.session.connect` |
| `2026-07-31 04:36:26` | `cowrie.client.version` |
| `2026-07-31 04:36:27` | `cowrie.client.kex` |
| `2026-07-31 04:36:28` | `cowrie.login.success` |
| `2026-07-31 04:36:28` | `cowrie.direct-tcpip.request` |
| `2026-07-31 04:36:29` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-31 04:36:29` | `cowrie.direct-tcpip.data` |
| `2026-07-31 04:36:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.231.191[.]101` to AbuseIPDB if not already reported
- [ ] Block `171.231.191[.]101` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec27cc4f780f

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-31 04:37 |
| **Last Seen** | 2026-07-31 04:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 04:37:04` | `cowrie.session.connect` |
| `2026-07-31 04:37:04` | `cowrie.client.version` |
| `2026-07-31 04:37:04` | `cowrie.client.kex` |
| `2026-07-31 04:37:04` | `cowrie.login.success` |
| `2026-07-31 04:37:04` | `cowrie.direct-tcpip.request` |
| `2026-07-31 04:37:05` | `cowrie.direct-tcpip.data` |
| `2026-07-31 04:37:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b14e4da75254

| Field | Detail |
|---|---|
| **Source IP** | `171.231.191[.]101` |
| **First Seen** | 2026-07-31 04:37 |
| **Last Seen** | 2026-07-31 04:37 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 04:37:10` | `cowrie.session.connect` |
| `2026-07-31 04:37:10` | `cowrie.client.version` |
| `2026-07-31 04:37:10` | `cowrie.client.kex` |
| `2026-07-31 04:37:12` | `cowrie.login.success` |
| `2026-07-31 04:37:12` | `cowrie.direct-tcpip.request` |
| `2026-07-31 04:37:13` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-31 04:37:13` | `cowrie.direct-tcpip.data` |
| `2026-07-31 04:37:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.231.191[.]101` to AbuseIPDB if not already reported
- [ ] Block `171.231.191[.]101` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b5d761bec02

| Field | Detail |
|---|---|
| **Source IP** | `34.52.255[.]221` |
| **First Seen** | 2026-07-31 04:41 |
| **Last Seen** | 2026-07-31 04:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 04:41:37` | `cowrie.session.connect` |
| `2026-07-31 04:41:37` | `cowrie.login.success` |
| `2026-07-31 04:41:37` | `cowrie.session.params` |
| `2026-07-31 04:41:37` | `cowrie.command.input` |
| `2026-07-31 04:41:37` | `cowrie.command.input` |
| `2026-07-31 04:41:37` | `cowrie.command.failed` |
| `2026-07-31 04:41:37` | `cowrie.command.input` |
| `2026-07-31 04:41:37` | `cowrie.log.closed` |
| `2026-07-31 04:41:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.52.255[.]221` to AbuseIPDB if not already reported
- [ ] Block `34.52.255[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cabcff38e82c

| Field | Detail |
|---|---|
| **Source IP** | `137.255.13[.]19` |
| **First Seen** | 2026-07-31 04:41 |
| **Last Seen** | 2026-07-31 04:41 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 04:41:39` | `cowrie.session.connect` |
| `2026-07-31 04:41:39` | `cowrie.client.version` |
| `2026-07-31 04:41:39` | `cowrie.client.kex` |
| `2026-07-31 04:41:40` | `cowrie.login.success` |
| `2026-07-31 04:41:41` | `cowrie.session.params` |
| `2026-07-31 04:41:41` | `cowrie.command.input` |
| `2026-07-31 04:41:41` | `cowrie.command.failed` |
| `2026-07-31 04:41:41` | `cowrie.log.closed` |
| `2026-07-31 04:41:42` | `cowrie.session.params` |
| `2026-07-31 04:41:42` | `cowrie.command.input` |
| `2026-07-31 04:41:42` | `cowrie.session.file_download` |
| `2026-07-31 04:41:42` | `cowrie.log.closed` |
| `2026-07-31 04:41:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `137.255.13[.]19` to AbuseIPDB if not already reported
- [ ] Block `137.255.13[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-69dd54fc9b90

| Field | Detail |
|---|---|
| **Source IP** | `137.255.13[.]19` |
| **First Seen** | 2026-07-31 04:41 |
| **Last Seen** | 2026-07-31 04:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 04:41:42` | `cowrie.session.connect` |
| `2026-07-31 04:41:43` | `cowrie.client.version` |
| `2026-07-31 04:41:43` | `cowrie.client.kex` |
| `2026-07-31 04:41:43` | `cowrie.login.success` |
| `2026-07-31 04:41:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `137.255.13[.]19` to AbuseIPDB if not already reported
- [ ] Block `137.255.13[.]19` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5d88ca3d902

| Field | Detail |
|---|---|
| **Source IP** | `137.255.13[.]19` |
| **First Seen** | 2026-07-31 04:41 |
| **Last Seen** | 2026-07-31 04:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 04:41:44` | `cowrie.session.connect` |
| `2026-07-31 04:41:44` | `cowrie.client.version` |
| `2026-07-31 04:41:44` | `cowrie.client.kex` |
| `2026-07-31 04:41:45` | `cowrie.login.success` |
| `2026-07-31 04:41:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `137.255.13[.]19` to AbuseIPDB if not already reported
- [ ] Block `137.255.13[.]19` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f57e193751cb

| Field | Detail |
|---|---|
| **Source IP** | `34.52.255[.]221` |
| **First Seen** | 2026-07-31 04:41 |
| **Last Seen** | 2026-07-31 04:41 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 04:41:45` | `cowrie.session.connect` |
| `2026-07-31 04:41:45` | `cowrie.login.success` |
| `2026-07-31 04:41:46` | `cowrie.session.params` |
| `2026-07-31 04:41:46` | `cowrie.command.input` |
| `2026-07-31 04:41:46` | `cowrie.command.failed` |
| `2026-07-31 04:41:55` | `cowrie.log.closed` |
| `2026-07-31 04:41:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.52.255[.]221` to AbuseIPDB if not already reported
- [ ] Block `34.52.255[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5adede65ae0

| Field | Detail |
|---|---|
| **Source IP** | `34.52.255[.]221` |
| **First Seen** | 2026-07-31 04:41 |
| **Last Seen** | 2026-07-31 04:41 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 04:41:47` | `cowrie.session.connect` |
| `2026-07-31 04:41:47` | `cowrie.login.success` |
| `2026-07-31 04:41:48` | `cowrie.session.params` |
| `2026-07-31 04:41:48` | `cowrie.command.input` |
| `2026-07-31 04:41:55` | `cowrie.log.closed` |
| `2026-07-31 04:41:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.52.255[.]221` to AbuseIPDB if not already reported
- [ ] Block `34.52.255[.]221` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71a61d297604

| Field | Detail |
|---|---|
| **Source IP** | `171.231.191[.]101` |
| **First Seen** | 2026-07-31 04:43 |
| **Last Seen** | 2026-07-31 04:43 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 04:43:32` | `cowrie.session.connect` |
| `2026-07-31 04:43:32` | `cowrie.client.version` |
| `2026-07-31 04:43:33` | `cowrie.client.kex` |
| `2026-07-31 04:43:35` | `cowrie.login.success` |
| `2026-07-31 04:43:35` | `cowrie.direct-tcpip.request` |
| `2026-07-31 04:43:35` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-31 04:43:35` | `cowrie.direct-tcpip.data` |
| `2026-07-31 04:43:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.231.191[.]101` to AbuseIPDB if not already reported
- [ ] Block `171.231.191[.]101` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8260a0ffe89a

| Field | Detail |
|---|---|
| **Source IP** | `116.110.17[.]78` |
| **First Seen** | 2026-07-31 04:44 |
| **Last Seen** | 2026-07-31 04:44 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 04:44:41` | `cowrie.session.connect` |
| `2026-07-31 04:44:41` | `cowrie.client.version` |
| `2026-07-31 04:44:41` | `cowrie.client.kex` |
| `2026-07-31 04:44:43` | `cowrie.login.success` |
| `2026-07-31 04:44:43` | `cowrie.direct-tcpip.request` |
| `2026-07-31 04:44:44` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-31 04:44:44` | `cowrie.direct-tcpip.data` |
| `2026-07-31 04:44:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.110.17[.]78` to AbuseIPDB if not already reported
- [ ] Block `116.110.17[.]78` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-049a12d00388

| Field | Detail |
|---|---|
| **Source IP** | `116.110.17[.]78` |
| **First Seen** | 2026-07-31 04:47 |
| **Last Seen** | 2026-07-31 04:47 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 04:47:37` | `cowrie.session.connect` |
| `2026-07-31 04:47:37` | `cowrie.client.version` |
| `2026-07-31 04:47:39` | `cowrie.client.kex` |
| `2026-07-31 04:47:41` | `cowrie.login.success` |
| `2026-07-31 04:47:41` | `cowrie.direct-tcpip.request` |
| `2026-07-31 04:47:42` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-31 04:47:42` | `cowrie.direct-tcpip.data` |
| `2026-07-31 04:47:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.110.17[.]78` to AbuseIPDB if not already reported
- [ ] Block `116.110.17[.]78` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-abfb877b898d

| Field | Detail |
|---|---|
| **Source IP** | `116.110.17[.]78` |
| **First Seen** | 2026-07-31 04:50 |
| **Last Seen** | 2026-07-31 04:52 |
| **Session Duration** | 152s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 04:50:24` | `cowrie.session.connect` |
| `2026-07-31 04:50:24` | `cowrie.client.version` |
| `2026-07-31 04:50:24` | `cowrie.client.kex` |
| `2026-07-31 04:50:40` | `cowrie.login.success` |
| `2026-07-31 04:52:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.110.17[.]78` to AbuseIPDB if not already reported
- [ ] Block `116.110.17[.]78` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8656cb659b36

| Field | Detail |
|---|---|
| **Source IP** | `116.110.17[.]78` |
| **First Seen** | 2026-07-31 04:50 |
| **Last Seen** | 2026-07-31 04:50 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 04:50:40` | `cowrie.session.connect` |
| `2026-07-31 04:50:40` | `cowrie.client.version` |
| `2026-07-31 04:50:43` | `cowrie.client.kex` |
| `2026-07-31 04:50:45` | `cowrie.login.success` |
| `2026-07-31 04:50:46` | `cowrie.direct-tcpip.request` |
| `2026-07-31 04:50:47` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-31 04:50:47` | `cowrie.direct-tcpip.data` |
| `2026-07-31 04:50:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.110.17[.]78` to AbuseIPDB if not already reported
- [ ] Block `116.110.17[.]78` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c34c7635e751

| Field | Detail |
|---|---|
| **Source IP** | `171.231.191[.]101` |
| **First Seen** | 2026-07-31 04:52 |
| **Last Seen** | 2026-07-31 04:52 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 04:52:50` | `cowrie.session.connect` |
| `2026-07-31 04:52:51` | `cowrie.client.version` |
| `2026-07-31 04:52:51` | `cowrie.client.kex` |
| `2026-07-31 04:52:53` | `cowrie.login.success` |
| `2026-07-31 04:52:53` | `cowrie.direct-tcpip.request` |
| `2026-07-31 04:52:53` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-31 04:52:53` | `cowrie.direct-tcpip.data` |
| `2026-07-31 04:52:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.231.191[.]101` to AbuseIPDB if not already reported
- [ ] Block `171.231.191[.]101` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63ff4ff8e6ef

| Field | Detail |
|---|---|
| **Source IP** | `141.253.107[.]23` |
| **First Seen** | 2026-07-31 04:53 |
| **Last Seen** | 2026-07-31 04:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 04:53:02` | `cowrie.session.connect` |
| `2026-07-31 04:53:02` | `cowrie.client.version` |
| `2026-07-31 04:53:02` | `cowrie.client.kex` |
| `2026-07-31 04:53:03` | `cowrie.login.success` |
| `2026-07-31 04:53:03` | `cowrie.session.params` |
| `2026-07-31 04:53:03` | `cowrie.command.input` |
| `2026-07-31 04:53:04` | `cowrie.log.closed` |
| `2026-07-31 04:53:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `141.253.107[.]23` to AbuseIPDB if not already reported
- [ ] Block `141.253.107[.]23` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55e82cf718cf

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]91` |
| **First Seen** | 2026-07-31 04:53 |
| **Last Seen** | 2026-07-31 04:53 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST, /bin/busybox TEST, cat /proc, ./` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 04:53:39` | `cowrie.session.connect` |
| `2026-07-31 04:53:39` | `cowrie.login.success` |
| `2026-07-31 04:53:40` | `cowrie.session.params` |
| `2026-07-31 04:53:40` | `cowrie.command.input` |
| `2026-07-31 04:53:41` | `cowrie.command.input` |
| `2026-07-31 04:53:42` | `cowrie.command.input` |
| `2026-07-31 04:53:42` | `cowrie.command.input` |
| `2026-07-31 04:53:42` | `cowrie.command.failed` |
| `2026-07-31 04:53:43` | `cowrie.log.closed` |
| `2026-07-31 04:53:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]91` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `34.52.255[.]221` | **30** | 2026-07-31 04:41 | 2026-07-31 04:41 | 4m | 0 | `T1592` | 🟠 MEDIUM |
| `91.233.83[.]203` | **20** | 2026-07-31 02:57 | 2026-07-31 04:49 | 19m | 0 | `T1592` | 🟠 MEDIUM |
| `207.175.174[.]221` | **9** | 2026-07-31 03:59 | 2026-07-31 04:00 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **5** | 2026-07-31 03:11 | 2026-07-31 04:54 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]161` | **4** | 2026-07-31 02:57 | 2026-07-31 03:23 | 0m | 0 | `T1592` | 🟢 LOW |
| `85.11.167[.]228` | **3** | 2026-07-31 04:17 | 2026-07-31 04:17 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `88.214.25[.]121` | **3** | 2026-07-31 04:07 | 2026-07-31 04:07 | 0m | 0 | `T1592` | 🟢 LOW |
| `88.214.25[.]124` | **3** | 2026-07-31 03:40 | 2026-07-31 03:40 | 0m | 0 | `T1592` | 🟢 LOW |
| `132.148.30[.]167` | **2** | 2026-07-31 02:56 | 2026-07-31 03:22 | 1m | 0 | `T1592` | 🟢 LOW |
| `106.246.89[.]69` | 1 | 2026-07-31 03:51 | 2026-07-31 03:51 | 0s | 0 | `T1592` | 🟢 LOW |
| `116.110.17[.]78` | 1 | 2026-07-31 04:41 | 2026-07-31 04:41 | 42s | 0 | `T1592` | 🟢 LOW |
| `166.62.102[.]109` | 1 | 2026-07-31 03:18 | 2026-07-31 03:18 | 32s | 0 | `T1592` | 🟢 LOW |
| `171.231.191[.]101` | 1 | 2026-07-31 04:25 | 2026-07-31 04:25 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `176.65.132[.]8` | 1 | 2026-07-31 03:32 | 2026-07-31 03:32 | 0s | 0 | `T1592` | 🟢 LOW |
| `34.76.133[.]51` | 1 | 2026-07-31 03:59 | 2026-07-31 03:59 | 5s | 0 | `T1592` | 🟢 LOW |
| `45.205.1[.]244` | 1 | 2026-07-31 03:25 | 2026-07-31 03:25 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.211[.]97` | 1 | 2026-07-31 04:43 | 2026-07-31 04:43 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]2` | 1 | 2026-07-31 04:52 | 2026-07-31 04:52 | 2s | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]184` | 1 | 2026-07-31 03:49 | 2026-07-31 03:49 | 17s | 0 | `T1592` | 🟢 LOW |
| `77.90.185[.]16` | 1 | 2026-07-31 04:29 | 2026-07-31 04:29 | 0s | 0 | `T1592` | 🟢 LOW |
| `80.233.77[.]136` | 1 | 2026-07-31 02:57 | 2026-07-31 02:57 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.238.181[.]92` | 1 | 2026-07-31 04:16 | 2026-07-31 04:16 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.92.40[.]18` | 1 | 2026-07-31 03:32 | 2026-07-31 03:32 | 0s | 0 | `T1592` | 🟢 LOW |
| `94.154.43[.]36` | 1 | 2026-07-31 03:12 | 2026-07-31 03:12 | 0s | 0 | `T1592` | 🟢 LOW |
| `94.154.43[.]91` | 1 | 2026-07-31 04:53 | 2026-07-31 04:53 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/74** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | **1/74** 🔴 |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 82/100 | 🔴 HIGH | **32/74** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 43/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 70/100 | 🔴 HIGH | **25/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 50/100 | 🟡 MEDIUM | **27/74** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `1eecf2377d20768c28d741e21affaa53cf26db0d083efdbf43a92fa938b7e4be` | ELF Binary (Linux executable) (ARM 32-bit) | `1eecf2377d20768c...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
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
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `287962211de7bcadb39f7576732438b43ee6aab420ec23c29a9d12a8151a547f` | ELF Binary (Linux executable) (x86 32-bit) | `287962211de7bcad...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `2f206563640dd66a743ffd493ce0e3c31a8fc5a24b9f5d2b540fc22d45c13d66` | ELF Binary (Linux executable) (x86 32-bit) | `2f206563640dd66a...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `31d4181843b1ed10a7e7cb3f108f6d6c50a7a4452ee52ddacabe8ca77260615e` | Bash Script | `31d4181843b1ed10...` | 60/100 | 🟡 MEDIUM | **25/75** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 65/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 86/100 | 🔴 HIGH | **40/74** 🔴 |
| `3eab3901798ec748895b2dca4b8762aec553d2966112999c60061d4599b599a0` | ELF Binary (Linux executable) (x86 32-bit) | `3eab3901798ec748...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `3f3bf218089d1488617d37f8a5116bb2791eb39ce06a1b5bc9a4cdfe5e94dd39` | ELF Binary (Linux executable) (RISC-V 64-bit) | `3f3bf218089d1488...` | 33/100 | 🟢 LOW | **8/75** 🔴 |
| `40db9279ba409757c074048529be5bf8f141fa022489a965792e7f7de2223b78` | ELF Binary (Linux executable) (ARM 32-bit) | `40db9279ba409757...` | 62/100 | 🟡 MEDIUM | **31/74** 🔴 |
| `417e065ee49c19c83c0e9cd99b702efde39d77b6c02d56b69a6c56b93d275ff3` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `417e065ee49c19c8...` | 47/100 | 🟡 MEDIUM | **19/74** 🔴 |
| `44689d3e1a7f460db2ecc14351c171f4910721257f83024c63cbc07f4e2b977c` | ELF Binary (Linux executable) (x86-64 64-bit) | `44689d3e1a7f460d...` | 35/100 | 🟢 LOW | **13/74** 🔴 |

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
| `171.231.191[.]7` | VN | Viettel Group | **100** ⚠️ | 0 |
| `31.173.66[.]222` | RU | PJSC MegaFon | **100** ⚠️ | 50 |
| `91.233.83[.]203` | GB | Andrew Millar Ltd | **100** ⚠️ | 10 |
| `103.103.53[.]44` | IN | Catla IT and Engg.Co.Pvt.Ltd. | **100** ⚠️ | 50 |
| `70.89.116[.]5` | US | Comcast Cable Communications, LLC | **100** ⚠️ | 50 |
| `24.207.66[.]154` | CA | EastLink | **100** ⚠️ | 50 |
| `66.132.186[.]184` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `213.154.80[.]51` | SN | PCCI Internet | **100** ⚠️ | 50 |
| `115.245.122[.]146` | IN | Reliance Jio Infocomm Limited | **100** ⚠️ | 50 |
| `222.190.110[.]210` | CN | LiHui Network Service Centre | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 181 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 164 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 37 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 35 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 35 |

---

## 🔕 False Positive Summary (21 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 3 |
| AbuseIPDB score 17 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 16 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 280 cases |
| Tool 34  | Credential Extractor        | ✅ 182 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 15 fingerprints |
| Tool 36  | Command Clustering          | ✅ 9 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 84 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 21 filtered (7.5%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 55 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 26 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 164 priority case(s) shown individually · 25 recon entry/entries in table (9 group(s) consolidating 79 session(s)).

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
_Report time: 2026-07-31T06:49:24Z_

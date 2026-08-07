# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-07 |
| **Generated At** | 2026-08-07T10:57:13Z |
| **Shift Time** | 10:57 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **479** |
| Confirmed Threats | **447** |
| False Positives Filtered | **32** (6.7%) |
| Unique Attacker IPs | **92** |
| Countries of Origin | **27** |
| High Severity Cases | **151** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **328** |
| Malware Samples Analyzed | **3** HIGH · **23** MED · 20 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **175** |
| Unique Credential Pairs | **133** |
| Unique Usernames | **33** |
| Unique Passwords | **126** |
| Successful Auth Pairs | **164** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 100 |
| `debian` | 12 |
| `admin` | 7 |
| `support` | 6 |
| `unknown` | 6 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `9999999` | 9 |
| `root2023` | 5 |
| `support` | 4 |
| `123456789` | 4 |
| `112233` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `debian` | `9999999` | 5 |
| `root` | `root2023` | 5 |
| `support` | `support` | 4 |
| `root` | `9999999` | 4 |
| `admin` | `112233` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `123!@#qweQWE` | `110.173.190.222` | 2026-08-07T08:55:08 |
| `root` | `Vps@123` | `110.173.190.222` | 2026-08-07T08:55:18 |
| `root` | `Server2016` | `110.173.190.222` | 2026-08-07T08:55:29 |
| `root` | `Zz12345` | `110.173.190.222` | 2026-08-07T08:55:40 |
| `root` | `Pass1234` | `110.173.190.222` | 2026-08-07T08:55:50 |
| `root` | `1.q` | `110.173.190.222` | 2026-08-07T08:56:01 |
| `root` | `12345678aA!` | `110.173.190.222` | 2026-08-07T08:56:11 |
| `root` | `admin123` | `45.148.10.240` | 2026-08-07T08:56:14 |
| `root` | `Aa147258*` | `110.173.190.222` | 2026-08-07T08:56:22 |
| `root` | `localhost.123` | `110.173.190.222` | 2026-08-07T08:56:32 |
| `root` | `123456789@A` | `110.173.190.222` | 2026-08-07T08:56:42 |
| `root` | `Superman@123` | `110.173.190.222` | 2026-08-07T08:56:53 |
| `root` | `Qq123123@` | `110.173.190.222` | 2026-08-07T08:57:03 |
| `root` | `ZXCzxc123.` | `110.173.190.222` | 2026-08-07T08:57:14 |
| `root` | `qweQWE123!` | `110.173.190.222` | 2026-08-07T08:57:24 |
| `root` | `qweASD.123` | `110.173.190.222` | 2026-08-07T08:57:34 |
| `root` | `!qazxsw23edc` | `110.173.190.222` | 2026-08-07T08:57:44 |
| `root` | `!@#QWEqwe` | `110.173.190.222` | 2026-08-07T08:57:54 |
| `root` | `toor` | `45.148.10.240` | 2026-08-07T08:58:01 |
| `root` | `4dmin#123` | `110.173.190.222` | 2026-08-07T08:58:05 |
| `root` | `1234567890Ab` | `110.173.190.222` | 2026-08-07T08:58:15 |
| `root` | `Qq12345678.` | `110.173.190.222` | 2026-08-07T08:58:25 |
| `root` | `test@12345` | `110.173.190.222` | 2026-08-07T08:58:35 |
| `root` | `redhat@123` | `110.173.190.222` | 2026-08-07T08:58:46 |
| `root` | `Mudar123` | `110.173.190.222` | 2026-08-07T08:58:56 |
| `root` | `Founder123` | `110.173.190.222` | 2026-08-07T08:59:07 |
| `root` | `123456789qQ` | `110.173.190.222` | 2026-08-07T08:59:17 |
| `root` | `web12` | `110.173.190.222` | 2026-08-07T08:59:27 |
| `root` | `www.123.com` | `110.173.190.222` | 2026-08-07T08:59:37 |
| `root` | `12345678aA.` | `110.173.190.222` | 2026-08-07T08:59:47 |
| `root` | `root123` | `45.148.10.240` | 2026-08-07T08:59:50 |
| `support` | `git123` | `10.0.0.73` | 2026-08-07T08:59:52 |
| `root` | `123456789-.q` | `110.173.190.222` | 2026-08-07T08:59:58 |
| `root` | `password1234_` | `110.173.190.222` | 2026-08-07T09:00:08 |
| `root` | `tech@1234` | `110.173.190.222` | 2026-08-07T09:00:18 |
| `root` | `Huawei12!@` | `110.173.190.222` | 2026-08-07T09:00:28 |
| `root` | `Aa1234567!` | `110.173.190.222` | 2026-08-07T09:00:39 |
| `root` | `12345678@a` | `110.173.190.222` | 2026-08-07T09:00:49 |
| `root` | `huawei.123` | `110.173.190.222` | 2026-08-07T09:01:00 |
| `root` | `adminpassword` | `110.173.190.222` | 2026-08-07T09:01:09 |
| `root` | `Cisco@1234` | `110.173.190.222` | 2026-08-07T09:01:20 |
| `root` | `Start.123` | `110.173.190.222` | 2026-08-07T09:01:30 |
| `root` | `Qwe12345` | `110.173.190.222` | 2026-08-07T09:01:41 |
| `root` | `12345678` | `45.148.10.240` | 2026-08-07T09:01:42 |
| `root` | `Qq12345678` | `110.173.190.222` | 2026-08-07T09:01:51 |
| `root` | `1234Abcd` | `110.173.190.222` | 2026-08-07T09:02:02 |
| `root` | `P@$$w0rd@123` | `110.173.190.222` | 2026-08-07T09:02:13 |
| `root` | `rootadmin123` | `110.173.190.222` | 2026-08-07T09:02:24 |
| `root` | `Aa112211!` | `110.173.190.222` | 2026-08-07T09:02:34 |
| `root` | `Ab123456@` | `110.173.190.222` | 2026-08-07T09:02:46 |
| `root` | `mudar@123` | `110.173.190.222` | 2026-08-07T09:02:56 |
| `root` | `Work@123` | `110.173.190.222` | 2026-08-07T09:03:07 |
| `support` | `support` | `10.0.0.73` | 2026-08-07T09:03:15 |
| `root` | `1` | `45.148.10.240` | 2026-08-07T09:03:29 |
| `root` | `12345` | `45.148.10.240` | 2026-08-07T09:05:18 |
| `debian` | `qwerty123` | `10.0.0.73` | 2026-08-07T09:07:03 |
| `root` | `abcd1234` | `45.148.10.240` | 2026-08-07T09:07:14 |
| `root` | `default` | `45.148.10.240` | 2026-08-07T09:09:08 |
| `root` | `1qaz@WSX` | `45.148.10.240` | 2026-08-07T09:10:58 |
| `root` | `ubuntu` | `91.219.196.17` | 2026-08-07T09:12:00 |
| `blank` | `blank12345` | `10.0.0.73` | 2026-08-07T09:12:08 |
| `test` | `test` | `31.77.227.120` | 2026-08-07T09:12:43 |
| `root` | `test` | `45.148.10.240` | 2026-08-07T09:12:53 |
| `root` | `abc123` | `45.148.10.240` | 2026-08-07T09:14:46 |
| `root` | `111111` | `45.148.10.240` | 2026-08-07T09:16:34 |
| `root` | `pass` | `45.148.10.240` | 2026-08-07T09:18:23 |
| `root` | `123` | `45.148.10.240` | 2026-08-07T09:20:16 |
| `root` | `qwerty` | `45.148.10.240` | 2026-08-07T09:22:05 |
| `support` | `support55` | `122.176.45.238` | 2026-08-07T09:22:54 |
| `root` | `123456789` | `45.148.10.240` | 2026-08-07T09:23:53 |
| `root` | `1q2w3e4r` | `45.148.10.240` | 2026-08-07T09:25:46 |
| `debian` | `qwerty123` | `117.198.99.18` | 2026-08-07T09:25:55 |
| `debian` | `qwerty123` | `218.248.19.102` | 2026-08-07T09:26:04 |
| `root` | `ubuntu` | `45.148.10.240` | 2026-08-07T09:27:42 |
| `debian` | `9999999` | `10.0.0.73` | 2026-08-07T09:28:42 |
| `root` | `server` | `45.148.10.240` | 2026-08-07T09:29:31 |
| `debian` | `9999999` | `218.13.214.18` | 2026-08-07T09:30:02 |
| `debian` | `9999999` | `124.167.20.113` | 2026-08-07T09:30:16 |
| `root` | `root1234` | `45.148.10.240` | 2026-08-07T09:31:27 |
| `root` | `raspberry` | `45.148.10.240` | 2026-08-07T09:33:25 |
| `college` | `college` | `54.37.235.85` | 2026-08-07T09:33:26 |
| `345gs5662d34` | `345gs5662d34` | `54.37.235.85` | 2026-08-07T09:33:29 |
| `college` | `3245gs5662d34` | `54.37.235.85` | 2026-08-07T09:33:30 |
| `silva` | `12345` | `103.163.117.230` | 2026-08-07T09:34:38 |
| `345gs5662d34` | `345gs5662d34` | `103.163.117.224` | 2026-08-07T09:34:42 |
| `silva` | `3245gs5662d34` | `103.163.117.230` | 2026-08-07T09:34:44 |
| `unknown` | `unknown2025` | `153.37.177.219` | 2026-08-07T09:34:48 |
| `unknown` | `unknown2025` | `10.0.0.73` | 2026-08-07T09:35:10 |
| `root` | `qwe123` | `45.148.10.240` | 2026-08-07T09:35:18 |
| `root` | `q1w2e3r4` | `45.148.10.240` | 2026-08-07T09:37:07 |
| `root` | `123123` | `45.148.10.240` | 2026-08-07T09:39:01 |
| `admin` | `user` | `10.0.0.73` | 2026-08-07T09:39:59 |
| `root` | `P@ssw0rd` | `45.148.10.240` | 2026-08-07T09:40:51 |
| `root` | `123qweasd` | `45.148.10.240` | 2026-08-07T09:42:39 |
| `root` | `123@@@` | `129.153.145.135` | 2026-08-07T09:43:27 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-08-07T09:43:28 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-08-07T09:43:36 |
| `support` | `support` | `176.53.159.196` | 2026-08-07T09:44:11 |
| `root` | `rootroot` | `45.148.10.240` | 2026-08-07T09:44:34 |
| `root` | `1qaz2wsx` | `45.148.10.240` | 2026-08-07T09:46:33 |
| `debian` | `9999999` | `58.17.128.7` | 2026-08-07T09:46:45 |
| `debian` | `9999999` | `201.63.52.54` | 2026-08-07T09:46:53 |
| `root` | `123@@@` | `64.110.90.250` | 2026-08-07T09:48:21 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-08-07T09:48:22 |
| `root` | `qwer1234` | `45.148.10.240` | 2026-08-07T09:48:28 |
| `root` | `test123` | `45.148.10.240` | 2026-08-07T09:50:24 |
| `root` | `sysadmin` | `45.148.10.240` | 2026-08-07T09:52:22 |
| `root` | `root@123` | `45.148.10.240` | 2026-08-07T09:54:15 |
| `unknown` | `123456789` | `187.8.120.90` | 2026-08-07T09:54:34 |
| `unknown` | `123456789` | `80.233.77.136` | 2026-08-07T09:54:41 |
| `root` | `administrator` | `45.148.10.240` | 2026-08-07T09:56:04 |
| `admin` | `user` | `116.114.94.242` | 2026-08-07T09:57:16 |
| `admin` | `user` | `60.12.5.190` | 2026-08-07T09:57:30 |
| `root` | `000000` | `45.148.10.240` | 2026-08-07T09:58:00 |
| `unknown` | `123456789` | `10.0.0.73` | 2026-08-07T09:58:08 |
| `root` | `redhat` | `45.148.10.240` | 2026-08-07T09:59:55 |
| `root` | `9999999` | `10.0.0.73` | 2026-08-07T10:03:11 |
| `root` | `9999999` | `49.124.149.209` | 2026-08-07T10:04:49 |
| `root` | `9999999` | `117.69.255.239` | 2026-08-07T10:05:04 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `34.53.157.23` | 2026-08-07T10:11:05 |
| `*1` | `$4` | `34.53.157.23` | 2026-08-07T10:11:13 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 8664` | `34.53.157.23` | 2026-08-07T10:11:15 |
| `scan` | `scan` | `10.0.0.73` | 2026-08-07T10:14:31 |
| `admin` | `112233` | `10.0.0.73` | 2026-08-07T10:15:54 |
| `debian` | `debian2013` | `187.126.105.42` | 2026-08-07T10:17:42 |
| `debian` | `debian2013` | `14.54.22.11` | 2026-08-07T10:17:56 |
| `sol` | `sol` | `2.57.122.238` | 2026-08-07T10:20:29 |
| `debian` | `debian2013` | `10.0.0.73` | 2026-08-07T10:21:08 |
| `solana` | `solana` | `2.57.122.238` | 2026-08-07T10:22:21 |
| `ethdocker` | `ethdocker` | `2.57.122.238` | 2026-08-07T10:24:23 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `34.79.177.86` | 2026-08-07T10:24:24 |
| `*1` | `$4` | `34.79.177.86` | 2026-08-07T10:24:38 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 3913` | `34.79.177.86` | 2026-08-07T10:24:39 |
| `eth-docker` | `eth-docker` | `2.57.122.238` | 2026-08-07T10:26:15 |
| `eth_docker` | `eth_docker` | `2.57.122.238` | 2026-08-07T10:28:04 |
| `raydium` | `raydium` | `2.57.122.238` | 2026-08-07T10:29:55 |
| `firedancer` | `firedancer` | `2.57.122.238` | 2026-08-07T10:31:46 |
| `node` | `node` | `2.57.122.238` | 2026-08-07T10:33:34 |
| `admin` | `112233` | `182.79.218.164` | 2026-08-07T10:34:35 |
| `admin` | `112233` | `221.10.221.104` | 2026-08-07T10:34:44 |
| `node` | `1234` | `2.57.122.238` | 2026-08-07T10:35:27 |
| `root` | `ubnt` | `218.29.196.162` | 2026-08-07T10:37:08 |
| `node` | `123456` | `2.57.122.238` | 2026-08-07T10:37:28 |
| `leo` | `leo` | `10.0.0.73` | 2026-08-07T10:37:55 |
| `ethereum` | `ethereum` | `2.57.122.238` | 2026-08-07T10:39:24 |
| `root` | `root2023` | `213.33.204.130` | 2026-08-07T10:40:56 |
| `root` | `root2023` | `218.202.143.68` | 2026-08-07T10:41:09 |
| `eth` | `eth` | `2.57.122.238` | 2026-08-07T10:41:18 |
| `polygon` | `polygon` | `2.57.122.238` | 2026-08-07T10:43:13 |
| `testuser` | `password` | `182.93.7.194` | 2026-08-07T10:43:20 |
| `345gs5662d34` | `345gs5662d34` | `182.93.7.194` | 2026-08-07T10:43:24 |
| `testuser` | `3245gs5662d34` | `182.93.7.194` | 2026-08-07T10:43:26 |
| `root` | `root2023` | `222.186.68.153` | 2026-08-07T10:44:19 |
| `root` | `root2023` | `10.0.0.73` | 2026-08-07T10:44:36 |
| `tron` | `tron` | `2.57.122.238` | 2026-08-07T10:45:04 |
| `trx` | `trx` | `2.57.122.238` | 2026-08-07T10:46:53 |
| `validator` | `ethereum` | `2.57.122.238` | 2026-08-07T10:48:47 |
| `root` | `ubnt` | `10.0.0.73` | 2026-08-07T10:48:58 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `34.62.77.102` | 2026-08-07T10:49:52 |
| `*1` | `$4` | `34.62.77.102` | 2026-08-07T10:50:06 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 8807` | `34.62.77.102` | 2026-08-07T10:50:08 |
| `sepolia` | `sepolia` | `2.57.122.238` | 2026-08-07T10:50:44 |
| `avalanche` | `avalanche` | `2.57.122.238` | 2026-08-07T10:52:35 |
| `solv` | `solv` | `2.57.122.238` | 2026-08-07T10:54:16 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **479** |
| Sessions with Fingerprint | **14** |
| Unique HASSH Fingerprints | **14** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 107 |
| OpenSSH | 24 |
| libssh | 14 |
| Paramiko (Python) | 6 |
| Perl Net::SSH | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `16443846184e...` | Generic scanner | 55 | 3 |
| `98ddc5604ef6...` | Modern SSH client | 47 | 1 |
| `acaa53e0a7d7...` | Mirai/variant | 24 | 24 |
| `f555226df196...` | Mirai/variant | 6 | 3 |
| `a2de0f306611...` | Mirai/variant | 6 | 2 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `16443846184e...` | Go SSH scanner | 55 | 3 | Generic scanner |
| `98ddc5604ef6...` | Go SSH scanner | 47 | 1 | Modern SSH client |
| `acaa53e0a7d7...` | OpenSSH | 24 | 24 | Mirai/variant |
| `f555226df196...` | libssh | 6 | 3 | Mirai/variant |
| `a2de0f306611...` | Paramiko (Python) | 6 | 2 | Mirai/variant |
| `95420f9d932d...` | libssh | 5 | 2 | — |
| `03a80b21afa8...` | libssh | 3 | 1 | Modern SSH client |
| `eff4c24daffc...` | Go SSH scanner | 2 | 1 | Modern SSH client |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 3 | 3 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `182.93.7.194`, `103.163.117.230`, `54.37.235.85`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **92** |
| Unique ASNs | **67** |
| High-Risk ASNs | **46** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4837` | CHINA UNICOM China169 Backbone | 7 | HIGH |
| `AS4134` | CHINANET BACKBONE | 4 | HIGH |
| `AS396982` | Google LLC | 4 | HIGH |
| `AS213412` | ONYPHE SAS | 3 | LOW |
| `AS10429` | TELEFÔNICA BRASIL S.A | 2 | HIGH |
| `AS31898` | Oracle Corporation | 2 | HIGH |
| `AS4818` | DiGi Telecommunications Sdn. Bhd. | 2 | HIGH |
| `AS63949` | Akamai Connected Cloud | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (151)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-eccec592dd40

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]222` |
| **First Seen** | 2026-08-07 08:55 |
| **Last Seen** | 2026-08-07 08:55 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 08:55:08` | `cowrie.login.success` |
| `2026-08-07 08:55:12` | `cowrie.session.params` |
| `2026-08-07 08:55:12` | `cowrie.command.input` |
| `2026-08-07 08:55:13` | `cowrie.log.closed` |
| `2026-08-07 08:55:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]222` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]222` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b32b558ed7d7

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]222` |
| **First Seen** | 2026-08-07 08:55 |
| **Last Seen** | 2026-08-07 08:55 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 08:55:11` | `cowrie.session.connect` |
| `2026-08-07 08:55:12` | `cowrie.client.version` |
| `2026-08-07 08:55:12` | `cowrie.client.kex` |
| `2026-08-07 08:55:18` | `cowrie.login.success` |
| `2026-08-07 08:55:22` | `cowrie.session.params` |
| `2026-08-07 08:55:22` | `cowrie.command.input` |
| `2026-08-07 08:55:24` | `cowrie.log.closed` |
| `2026-08-07 08:55:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]222` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]222` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da74448e2fd4

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]222` |
| **First Seen** | 2026-08-07 08:55 |
| **Last Seen** | 2026-08-07 08:55 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 08:55:21` | `cowrie.session.connect` |
| `2026-08-07 08:55:23` | `cowrie.client.version` |
| `2026-08-07 08:55:23` | `cowrie.client.kex` |
| `2026-08-07 08:55:29` | `cowrie.login.success` |
| `2026-08-07 08:55:33` | `cowrie.session.params` |
| `2026-08-07 08:55:33` | `cowrie.command.input` |
| `2026-08-07 08:55:34` | `cowrie.log.closed` |
| `2026-08-07 08:55:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]222` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]222` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b9423abf536

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]222` |
| **First Seen** | 2026-08-07 08:55 |
| **Last Seen** | 2026-08-07 08:55 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 08:55:32` | `cowrie.session.connect` |
| `2026-08-07 08:55:33` | `cowrie.client.version` |
| `2026-08-07 08:55:33` | `cowrie.client.kex` |
| `2026-08-07 08:55:40` | `cowrie.login.success` |
| `2026-08-07 08:55:43` | `cowrie.session.params` |
| `2026-08-07 08:55:43` | `cowrie.command.input` |
| `2026-08-07 08:55:45` | `cowrie.log.closed` |
| `2026-08-07 08:55:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]222` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]222` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37863ca9ad1c

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]222` |
| **First Seen** | 2026-08-07 08:55 |
| **Last Seen** | 2026-08-07 08:55 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 08:55:42` | `cowrie.session.connect` |
| `2026-08-07 08:55:44` | `cowrie.client.version` |
| `2026-08-07 08:55:44` | `cowrie.client.kex` |
| `2026-08-07 08:55:50` | `cowrie.login.success` |
| `2026-08-07 08:55:54` | `cowrie.session.params` |
| `2026-08-07 08:55:54` | `cowrie.command.input` |
| `2026-08-07 08:55:56` | `cowrie.log.closed` |
| `2026-08-07 08:55:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]222` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]222` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c1c8678f6bf

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]222` |
| **First Seen** | 2026-08-07 08:55 |
| **Last Seen** | 2026-08-07 08:56 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 08:55:53` | `cowrie.session.connect` |
| `2026-08-07 08:55:54` | `cowrie.client.version` |
| `2026-08-07 08:55:54` | `cowrie.client.kex` |
| `2026-08-07 08:56:01` | `cowrie.login.success` |
| `2026-08-07 08:56:05` | `cowrie.session.params` |
| `2026-08-07 08:56:05` | `cowrie.command.input` |
| `2026-08-07 08:56:07` | `cowrie.log.closed` |
| `2026-08-07 08:56:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]222` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]222` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-058959f65948

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]222` |
| **First Seen** | 2026-08-07 08:56 |
| **Last Seen** | 2026-08-07 08:56 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 08:56:03` | `cowrie.session.connect` |
| `2026-08-07 08:56:05` | `cowrie.client.version` |
| `2026-08-07 08:56:05` | `cowrie.client.kex` |
| `2026-08-07 08:56:11` | `cowrie.login.success` |
| `2026-08-07 08:56:15` | `cowrie.session.params` |
| `2026-08-07 08:56:15` | `cowrie.command.input` |
| `2026-08-07 08:56:17` | `cowrie.log.closed` |
| `2026-08-07 08:56:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]222` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]222` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0256eaf54ca7

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-07 08:56 |
| **Last Seen** | 2026-08-07 08:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 08:56:13` | `cowrie.session.connect` |
| `2026-08-07 08:56:13` | `cowrie.client.version` |
| `2026-08-07 08:56:13` | `cowrie.client.kex` |
| `2026-08-07 08:56:14` | `cowrie.login.success` |
| `2026-08-07 08:56:14` | `cowrie.session.params` |
| `2026-08-07 08:56:14` | `cowrie.command.input` |
| `2026-08-07 08:56:14` | `cowrie.log.closed` |
| `2026-08-07 08:56:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c67503bc479

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]222` |
| **First Seen** | 2026-08-07 08:56 |
| **Last Seen** | 2026-08-07 08:56 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 08:56:14` | `cowrie.session.connect` |
| `2026-08-07 08:56:15` | `cowrie.client.version` |
| `2026-08-07 08:56:15` | `cowrie.client.kex` |
| `2026-08-07 08:56:22` | `cowrie.login.success` |
| `2026-08-07 08:56:26` | `cowrie.session.params` |
| `2026-08-07 08:56:26` | `cowrie.command.input` |
| `2026-08-07 08:56:28` | `cowrie.log.closed` |
| `2026-08-07 08:56:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]222` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]222` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9445618faab1

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]222` |
| **First Seen** | 2026-08-07 08:56 |
| **Last Seen** | 2026-08-07 08:56 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 08:56:24` | `cowrie.session.connect` |
| `2026-08-07 08:56:26` | `cowrie.client.version` |
| `2026-08-07 08:56:26` | `cowrie.client.kex` |
| `2026-08-07 08:56:32` | `cowrie.login.success` |
| `2026-08-07 08:56:36` | `cowrie.session.params` |
| `2026-08-07 08:56:36` | `cowrie.command.input` |
| `2026-08-07 08:56:38` | `cowrie.log.closed` |
| `2026-08-07 08:56:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]222` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]222` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d97d1ae3c213

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]222` |
| **First Seen** | 2026-08-07 08:56 |
| **Last Seen** | 2026-08-07 08:56 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 08:56:35` | `cowrie.session.connect` |
| `2026-08-07 08:56:36` | `cowrie.client.version` |
| `2026-08-07 08:56:36` | `cowrie.client.kex` |
| `2026-08-07 08:56:42` | `cowrie.login.success` |
| `2026-08-07 08:56:46` | `cowrie.session.params` |
| `2026-08-07 08:56:46` | `cowrie.command.input` |
| `2026-08-07 08:56:48` | `cowrie.log.closed` |
| `2026-08-07 08:56:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]222` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]222` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e882eb690fdc

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]222` |
| **First Seen** | 2026-08-07 08:56 |
| **Last Seen** | 2026-08-07 08:56 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 08:56:45` | `cowrie.session.connect` |
| `2026-08-07 08:56:46` | `cowrie.client.version` |
| `2026-08-07 08:56:46` | `cowrie.client.kex` |
| `2026-08-07 08:56:53` | `cowrie.login.success` |
| `2026-08-07 08:56:56` | `cowrie.session.params` |
| `2026-08-07 08:56:56` | `cowrie.command.input` |
| `2026-08-07 08:56:58` | `cowrie.log.closed` |
| `2026-08-07 08:56:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]222` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]222` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7200411a93c2

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]222` |
| **First Seen** | 2026-08-07 08:56 |
| **Last Seen** | 2026-08-07 08:57 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 08:56:55` | `cowrie.session.connect` |
| `2026-08-07 08:56:57` | `cowrie.client.version` |
| `2026-08-07 08:56:57` | `cowrie.client.kex` |
| `2026-08-07 08:57:03` | `cowrie.login.success` |
| `2026-08-07 08:57:07` | `cowrie.session.params` |
| `2026-08-07 08:57:07` | `cowrie.command.input` |
| `2026-08-07 08:57:09` | `cowrie.log.closed` |
| `2026-08-07 08:57:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]222` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]222` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08182e3980d7

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]222` |
| **First Seen** | 2026-08-07 08:57 |
| **Last Seen** | 2026-08-07 08:57 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 08:57:06` | `cowrie.session.connect` |
| `2026-08-07 08:57:07` | `cowrie.client.version` |
| `2026-08-07 08:57:07` | `cowrie.client.kex` |
| `2026-08-07 08:57:14` | `cowrie.login.success` |
| `2026-08-07 08:57:17` | `cowrie.session.params` |
| `2026-08-07 08:57:17` | `cowrie.command.input` |
| `2026-08-07 08:57:19` | `cowrie.log.closed` |
| `2026-08-07 08:57:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]222` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]222` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19ca559b8049

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]222` |
| **First Seen** | 2026-08-07 08:57 |
| **Last Seen** | 2026-08-07 08:57 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 08:57:16` | `cowrie.session.connect` |
| `2026-08-07 08:57:18` | `cowrie.client.version` |
| `2026-08-07 08:57:18` | `cowrie.client.kex` |
| `2026-08-07 08:57:24` | `cowrie.login.success` |
| `2026-08-07 08:57:28` | `cowrie.session.params` |
| `2026-08-07 08:57:28` | `cowrie.command.input` |
| `2026-08-07 08:57:29` | `cowrie.log.closed` |
| `2026-08-07 08:57:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]222` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]222` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-763fce11e3d0

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]222` |
| **First Seen** | 2026-08-07 08:57 |
| **Last Seen** | 2026-08-07 08:57 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 08:57:27` | `cowrie.session.connect` |
| `2026-08-07 08:57:28` | `cowrie.client.version` |
| `2026-08-07 08:57:28` | `cowrie.client.kex` |
| `2026-08-07 08:57:34` | `cowrie.login.success` |
| `2026-08-07 08:57:38` | `cowrie.session.params` |
| `2026-08-07 08:57:38` | `cowrie.command.input` |
| `2026-08-07 08:57:40` | `cowrie.log.closed` |
| `2026-08-07 08:57:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]222` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]222` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a72fef138d5

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]222` |
| **First Seen** | 2026-08-07 08:57 |
| **Last Seen** | 2026-08-07 08:57 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 08:57:37` | `cowrie.session.connect` |
| `2026-08-07 08:57:38` | `cowrie.client.version` |
| `2026-08-07 08:57:38` | `cowrie.client.kex` |
| `2026-08-07 08:57:44` | `cowrie.login.success` |
| `2026-08-07 08:57:48` | `cowrie.session.params` |
| `2026-08-07 08:57:48` | `cowrie.command.input` |
| `2026-08-07 08:57:50` | `cowrie.log.closed` |
| `2026-08-07 08:57:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]222` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]222` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-abe2c7af2c19

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]222` |
| **First Seen** | 2026-08-07 08:57 |
| **Last Seen** | 2026-08-07 08:58 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 08:57:47` | `cowrie.session.connect` |
| `2026-08-07 08:57:48` | `cowrie.client.version` |
| `2026-08-07 08:57:48` | `cowrie.client.kex` |
| `2026-08-07 08:57:54` | `cowrie.login.success` |
| `2026-08-07 08:57:58` | `cowrie.session.params` |
| `2026-08-07 08:57:58` | `cowrie.command.input` |
| `2026-08-07 08:58:00` | `cowrie.log.closed` |
| `2026-08-07 08:58:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]222` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]222` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fadbc9994a3a

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]222` |
| **First Seen** | 2026-08-07 08:57 |
| **Last Seen** | 2026-08-07 08:58 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 08:57:57` | `cowrie.session.connect` |
| `2026-08-07 08:57:58` | `cowrie.client.version` |
| `2026-08-07 08:57:58` | `cowrie.client.kex` |
| `2026-08-07 08:58:05` | `cowrie.login.success` |
| `2026-08-07 08:58:09` | `cowrie.session.params` |
| `2026-08-07 08:58:09` | `cowrie.command.input` |
| `2026-08-07 08:58:10` | `cowrie.log.closed` |
| `2026-08-07 08:58:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]222` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]222` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d84eb84e098a

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-07 08:58 |
| **Last Seen** | 2026-08-07 08:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 08:58:00` | `cowrie.session.connect` |
| `2026-08-07 08:58:00` | `cowrie.client.version` |
| `2026-08-07 08:58:00` | `cowrie.client.kex` |
| `2026-08-07 08:58:01` | `cowrie.login.success` |
| `2026-08-07 08:58:02` | `cowrie.session.params` |
| `2026-08-07 08:58:02` | `cowrie.command.input` |
| `2026-08-07 08:58:02` | `cowrie.log.closed` |
| `2026-08-07 08:58:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e0fdb4f695a

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]222` |
| **First Seen** | 2026-08-07 08:58 |
| **Last Seen** | 2026-08-07 08:58 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 08:58:07` | `cowrie.session.connect` |
| `2026-08-07 08:58:09` | `cowrie.client.version` |
| `2026-08-07 08:58:09` | `cowrie.client.kex` |
| `2026-08-07 08:58:15` | `cowrie.login.success` |
| `2026-08-07 08:58:19` | `cowrie.session.params` |
| `2026-08-07 08:58:19` | `cowrie.command.input` |
| `2026-08-07 08:58:21` | `cowrie.log.closed` |
| `2026-08-07 08:58:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]222` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]222` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59fa480797af

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]222` |
| **First Seen** | 2026-08-07 08:58 |
| **Last Seen** | 2026-08-07 08:58 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 08:58:18` | `cowrie.session.connect` |
| `2026-08-07 08:58:19` | `cowrie.client.version` |
| `2026-08-07 08:58:19` | `cowrie.client.kex` |
| `2026-08-07 08:58:25` | `cowrie.login.success` |
| `2026-08-07 08:58:29` | `cowrie.session.params` |
| `2026-08-07 08:58:29` | `cowrie.command.input` |
| `2026-08-07 08:58:31` | `cowrie.log.closed` |
| `2026-08-07 08:58:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]222` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]222` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0917e5f9376

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]222` |
| **First Seen** | 2026-08-07 08:58 |
| **Last Seen** | 2026-08-07 08:58 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 08:58:28` | `cowrie.session.connect` |
| `2026-08-07 08:58:30` | `cowrie.client.version` |
| `2026-08-07 08:58:30` | `cowrie.client.kex` |
| `2026-08-07 08:58:35` | `cowrie.login.success` |
| `2026-08-07 08:58:39` | `cowrie.session.params` |
| `2026-08-07 08:58:39` | `cowrie.command.input` |
| `2026-08-07 08:58:41` | `cowrie.log.closed` |
| `2026-08-07 08:58:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]222` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]222` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fcbc2f4ff114

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]222` |
| **First Seen** | 2026-08-07 08:58 |
| **Last Seen** | 2026-08-07 08:58 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 08:58:38` | `cowrie.session.connect` |
| `2026-08-07 08:58:39` | `cowrie.client.version` |
| `2026-08-07 08:58:39` | `cowrie.client.kex` |
| `2026-08-07 08:58:46` | `cowrie.login.success` |
| `2026-08-07 08:58:49` | `cowrie.session.params` |
| `2026-08-07 08:58:49` | `cowrie.command.input` |
| `2026-08-07 08:58:51` | `cowrie.log.closed` |
| `2026-08-07 08:58:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]222` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]222` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1a60a953c92

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]222` |
| **First Seen** | 2026-08-07 08:58 |
| **Last Seen** | 2026-08-07 08:59 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 08:58:48` | `cowrie.session.connect` |
| `2026-08-07 08:58:50` | `cowrie.client.version` |
| `2026-08-07 08:58:50` | `cowrie.client.kex` |
| `2026-08-07 08:58:56` | `cowrie.login.success` |
| `2026-08-07 08:59:00` | `cowrie.session.params` |
| `2026-08-07 08:59:00` | `cowrie.command.input` |
| `2026-08-07 08:59:02` | `cowrie.log.closed` |
| `2026-08-07 08:59:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]222` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]222` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6fa33c775f6

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]222` |
| **First Seen** | 2026-08-07 08:58 |
| **Last Seen** | 2026-08-07 08:59 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 08:58:59` | `cowrie.session.connect` |
| `2026-08-07 08:59:00` | `cowrie.client.version` |
| `2026-08-07 08:59:00` | `cowrie.client.kex` |
| `2026-08-07 08:59:07` | `cowrie.login.success` |
| `2026-08-07 08:59:10` | `cowrie.session.params` |
| `2026-08-07 08:59:10` | `cowrie.command.input` |
| `2026-08-07 08:59:12` | `cowrie.log.closed` |
| `2026-08-07 08:59:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]222` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]222` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9dd3691e498b

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]222` |
| **First Seen** | 2026-08-07 08:59 |
| **Last Seen** | 2026-08-07 08:59 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 08:59:09` | `cowrie.session.connect` |
| `2026-08-07 08:59:11` | `cowrie.client.version` |
| `2026-08-07 08:59:11` | `cowrie.client.kex` |
| `2026-08-07 08:59:17` | `cowrie.login.success` |
| `2026-08-07 08:59:21` | `cowrie.session.params` |
| `2026-08-07 08:59:21` | `cowrie.command.input` |
| `2026-08-07 08:59:22` | `cowrie.log.closed` |
| `2026-08-07 08:59:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]222` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]222` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d50edef5582

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]222` |
| **First Seen** | 2026-08-07 08:59 |
| **Last Seen** | 2026-08-07 08:59 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 08:59:20` | `cowrie.session.connect` |
| `2026-08-07 08:59:21` | `cowrie.client.version` |
| `2026-08-07 08:59:21` | `cowrie.client.kex` |
| `2026-08-07 08:59:27` | `cowrie.login.success` |
| `2026-08-07 08:59:30` | `cowrie.session.params` |
| `2026-08-07 08:59:30` | `cowrie.command.input` |
| `2026-08-07 08:59:32` | `cowrie.log.closed` |
| `2026-08-07 08:59:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]222` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]222` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0be3f031830

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]222` |
| **First Seen** | 2026-08-07 08:59 |
| **Last Seen** | 2026-08-07 08:59 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 08:59:30` | `cowrie.session.connect` |
| `2026-08-07 08:59:31` | `cowrie.client.version` |
| `2026-08-07 08:59:31` | `cowrie.client.kex` |
| `2026-08-07 08:59:37` | `cowrie.login.success` |
| `2026-08-07 08:59:41` | `cowrie.session.params` |
| `2026-08-07 08:59:41` | `cowrie.command.input` |
| `2026-08-07 08:59:42` | `cowrie.log.closed` |
| `2026-08-07 08:59:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]222` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]222` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-531b88e2e482

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]222` |
| **First Seen** | 2026-08-07 08:59 |
| **Last Seen** | 2026-08-07 08:59 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 08:59:40` | `cowrie.session.connect` |
| `2026-08-07 08:59:41` | `cowrie.client.version` |
| `2026-08-07 08:59:41` | `cowrie.client.kex` |
| `2026-08-07 08:59:47` | `cowrie.login.success` |
| `2026-08-07 08:59:51` | `cowrie.session.params` |
| `2026-08-07 08:59:51` | `cowrie.command.input` |
| `2026-08-07 08:59:53` | `cowrie.log.closed` |
| `2026-08-07 08:59:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]222` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]222` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c10826bfe0dd

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-07 08:59 |
| **Last Seen** | 2026-08-07 08:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 08:59:49` | `cowrie.session.connect` |
| `2026-08-07 08:59:49` | `cowrie.client.version` |
| `2026-08-07 08:59:50` | `cowrie.client.kex` |
| `2026-08-07 08:59:50` | `cowrie.login.success` |
| `2026-08-07 08:59:51` | `cowrie.session.params` |
| `2026-08-07 08:59:51` | `cowrie.command.input` |
| `2026-08-07 08:59:51` | `cowrie.log.closed` |
| `2026-08-07 08:59:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76a6bb494c5f

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]222` |
| **First Seen** | 2026-08-07 08:59 |
| **Last Seen** | 2026-08-07 09:00 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 08:59:51` | `cowrie.session.connect` |
| `2026-08-07 08:59:51` | `cowrie.client.version` |
| `2026-08-07 08:59:53` | `cowrie.client.kex` |
| `2026-08-07 08:59:58` | `cowrie.login.success` |
| `2026-08-07 09:00:02` | `cowrie.session.params` |
| `2026-08-07 09:00:02` | `cowrie.command.input` |
| `2026-08-07 09:00:03` | `cowrie.log.closed` |
| `2026-08-07 09:00:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]222` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]222` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d56ca42de445

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]222` |
| **First Seen** | 2026-08-07 09:00 |
| **Last Seen** | 2026-08-07 09:00 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 09:00:01` | `cowrie.session.connect` |
| `2026-08-07 09:00:02` | `cowrie.client.version` |
| `2026-08-07 09:00:02` | `cowrie.client.kex` |
| `2026-08-07 09:00:08` | `cowrie.login.success` |
| `2026-08-07 09:00:12` | `cowrie.session.params` |
| `2026-08-07 09:00:12` | `cowrie.command.input` |
| `2026-08-07 09:00:14` | `cowrie.log.closed` |
| `2026-08-07 09:00:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]222` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]222` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ffc9ee528ff

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]222` |
| **First Seen** | 2026-08-07 09:00 |
| **Last Seen** | 2026-08-07 09:00 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 09:00:11` | `cowrie.session.connect` |
| `2026-08-07 09:00:12` | `cowrie.client.version` |
| `2026-08-07 09:00:12` | `cowrie.client.kex` |
| `2026-08-07 09:00:18` | `cowrie.login.success` |
| `2026-08-07 09:00:22` | `cowrie.session.params` |
| `2026-08-07 09:00:22` | `cowrie.command.input` |
| `2026-08-07 09:00:23` | `cowrie.log.closed` |
| `2026-08-07 09:00:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]222` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]222` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a73e735f94ef

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]222` |
| **First Seen** | 2026-08-07 09:00 |
| **Last Seen** | 2026-08-07 09:00 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 09:00:21` | `cowrie.session.connect` |
| `2026-08-07 09:00:22` | `cowrie.client.version` |
| `2026-08-07 09:00:22` | `cowrie.client.kex` |
| `2026-08-07 09:00:28` | `cowrie.login.success` |
| `2026-08-07 09:00:32` | `cowrie.session.params` |
| `2026-08-07 09:00:32` | `cowrie.command.input` |
| `2026-08-07 09:00:34` | `cowrie.log.closed` |
| `2026-08-07 09:00:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]222` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]222` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74642811fbec

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]222` |
| **First Seen** | 2026-08-07 09:00 |
| **Last Seen** | 2026-08-07 09:00 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 09:00:31` | `cowrie.session.connect` |
| `2026-08-07 09:00:32` | `cowrie.client.version` |
| `2026-08-07 09:00:32` | `cowrie.client.kex` |
| `2026-08-07 09:00:39` | `cowrie.login.success` |
| `2026-08-07 09:00:42` | `cowrie.session.params` |
| `2026-08-07 09:00:42` | `cowrie.command.input` |
| `2026-08-07 09:00:43` | `cowrie.log.closed` |
| `2026-08-07 09:00:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]222` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]222` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c1d88e8d781

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]222` |
| **First Seen** | 2026-08-07 09:00 |
| **Last Seen** | 2026-08-07 09:00 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 09:00:41` | `cowrie.session.connect` |
| `2026-08-07 09:00:43` | `cowrie.client.version` |
| `2026-08-07 09:00:43` | `cowrie.client.kex` |
| `2026-08-07 09:00:49` | `cowrie.login.success` |
| `2026-08-07 09:00:53` | `cowrie.session.params` |
| `2026-08-07 09:00:53` | `cowrie.command.input` |
| `2026-08-07 09:00:54` | `cowrie.log.closed` |
| `2026-08-07 09:00:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]222` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]222` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82bcafcfaba1

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]222` |
| **First Seen** | 2026-08-07 09:00 |
| **Last Seen** | 2026-08-07 09:01 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 09:00:52` | `cowrie.session.connect` |
| `2026-08-07 09:00:53` | `cowrie.client.version` |
| `2026-08-07 09:00:53` | `cowrie.client.kex` |
| `2026-08-07 09:01:00` | `cowrie.login.success` |
| `2026-08-07 09:01:03` | `cowrie.session.params` |
| `2026-08-07 09:01:03` | `cowrie.command.input` |
| `2026-08-07 09:01:04` | `cowrie.log.closed` |
| `2026-08-07 09:01:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]222` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]222` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0cf0aef086cb

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]222` |
| **First Seen** | 2026-08-07 09:01 |
| **Last Seen** | 2026-08-07 09:01 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 09:01:02` | `cowrie.session.connect` |
| `2026-08-07 09:01:04` | `cowrie.client.version` |
| `2026-08-07 09:01:04` | `cowrie.client.kex` |
| `2026-08-07 09:01:09` | `cowrie.login.success` |
| `2026-08-07 09:01:13` | `cowrie.session.params` |
| `2026-08-07 09:01:13` | `cowrie.command.input` |
| `2026-08-07 09:01:14` | `cowrie.log.closed` |
| `2026-08-07 09:01:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]222` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]222` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe687cecb326

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]222` |
| **First Seen** | 2026-08-07 09:01 |
| **Last Seen** | 2026-08-07 09:01 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 09:01:12` | `cowrie.session.connect` |
| `2026-08-07 09:01:13` | `cowrie.client.version` |
| `2026-08-07 09:01:13` | `cowrie.client.kex` |
| `2026-08-07 09:01:20` | `cowrie.login.success` |
| `2026-08-07 09:01:23` | `cowrie.session.params` |
| `2026-08-07 09:01:23` | `cowrie.command.input` |
| `2026-08-07 09:01:25` | `cowrie.log.closed` |
| `2026-08-07 09:01:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]222` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]222` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a133043ad854

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]222` |
| **First Seen** | 2026-08-07 09:01 |
| **Last Seen** | 2026-08-07 09:01 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 09:01:22` | `cowrie.session.connect` |
| `2026-08-07 09:01:24` | `cowrie.client.version` |
| `2026-08-07 09:01:24` | `cowrie.client.kex` |
| `2026-08-07 09:01:30` | `cowrie.login.success` |
| `2026-08-07 09:01:34` | `cowrie.session.params` |
| `2026-08-07 09:01:34` | `cowrie.command.input` |
| `2026-08-07 09:01:35` | `cowrie.log.closed` |
| `2026-08-07 09:01:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]222` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]222` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd5ec59f4f7a

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]222` |
| **First Seen** | 2026-08-07 09:01 |
| **Last Seen** | 2026-08-07 09:01 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 09:01:33` | `cowrie.session.connect` |
| `2026-08-07 09:01:34` | `cowrie.client.version` |
| `2026-08-07 09:01:34` | `cowrie.client.kex` |
| `2026-08-07 09:01:41` | `cowrie.login.success` |
| `2026-08-07 09:01:44` | `cowrie.session.params` |
| `2026-08-07 09:01:44` | `cowrie.command.input` |
| `2026-08-07 09:01:46` | `cowrie.log.closed` |
| `2026-08-07 09:01:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]222` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]222` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3f329df2cfb

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-07 09:01 |
| **Last Seen** | 2026-08-07 09:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 09:01:41` | `cowrie.session.connect` |
| `2026-08-07 09:01:41` | `cowrie.client.version` |
| `2026-08-07 09:01:41` | `cowrie.client.kex` |
| `2026-08-07 09:01:42` | `cowrie.login.success` |
| `2026-08-07 09:01:42` | `cowrie.session.params` |
| `2026-08-07 09:01:42` | `cowrie.command.input` |
| `2026-08-07 09:01:42` | `cowrie.log.closed` |
| `2026-08-07 09:01:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bbca342ecb71

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]222` |
| **First Seen** | 2026-08-07 09:01 |
| **Last Seen** | 2026-08-07 09:01 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 09:01:43` | `cowrie.session.connect` |
| `2026-08-07 09:01:45` | `cowrie.client.version` |
| `2026-08-07 09:01:45` | `cowrie.client.kex` |
| `2026-08-07 09:01:51` | `cowrie.login.success` |
| `2026-08-07 09:01:55` | `cowrie.session.params` |
| `2026-08-07 09:01:55` | `cowrie.command.input` |
| `2026-08-07 09:01:56` | `cowrie.log.closed` |
| `2026-08-07 09:01:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]222` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]222` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-117bbb018029

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]222` |
| **First Seen** | 2026-08-07 09:01 |
| **Last Seen** | 2026-08-07 09:02 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 09:01:54` | `cowrie.session.connect` |
| `2026-08-07 09:01:55` | `cowrie.client.version` |
| `2026-08-07 09:01:55` | `cowrie.client.kex` |
| `2026-08-07 09:02:02` | `cowrie.login.success` |
| `2026-08-07 09:02:05` | `cowrie.session.params` |
| `2026-08-07 09:02:05` | `cowrie.command.input` |
| `2026-08-07 09:02:07` | `cowrie.log.closed` |
| `2026-08-07 09:02:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]222` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]222` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05f112a1b265

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]222` |
| **First Seen** | 2026-08-07 09:02 |
| **Last Seen** | 2026-08-07 09:02 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 09:02:05` | `cowrie.session.connect` |
| `2026-08-07 09:02:07` | `cowrie.client.version` |
| `2026-08-07 09:02:07` | `cowrie.client.kex` |
| `2026-08-07 09:02:13` | `cowrie.login.success` |
| `2026-08-07 09:02:17` | `cowrie.session.params` |
| `2026-08-07 09:02:17` | `cowrie.command.input` |
| `2026-08-07 09:02:19` | `cowrie.log.closed` |
| `2026-08-07 09:02:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]222` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]222` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ace160c80f92

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]222` |
| **First Seen** | 2026-08-07 09:02 |
| **Last Seen** | 2026-08-07 09:02 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 09:02:16` | `cowrie.session.connect` |
| `2026-08-07 09:02:17` | `cowrie.client.version` |
| `2026-08-07 09:02:17` | `cowrie.client.kex` |
| `2026-08-07 09:02:24` | `cowrie.login.success` |
| `2026-08-07 09:02:27` | `cowrie.session.params` |
| `2026-08-07 09:02:27` | `cowrie.command.input` |
| `2026-08-07 09:02:29` | `cowrie.log.closed` |
| `2026-08-07 09:02:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]222` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]222` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb86d0a3ac14

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]222` |
| **First Seen** | 2026-08-07 09:02 |
| **Last Seen** | 2026-08-07 09:02 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 09:02:27` | `cowrie.session.connect` |
| `2026-08-07 09:02:28` | `cowrie.client.version` |
| `2026-08-07 09:02:28` | `cowrie.client.kex` |
| `2026-08-07 09:02:34` | `cowrie.login.success` |
| `2026-08-07 09:02:39` | `cowrie.session.params` |
| `2026-08-07 09:02:39` | `cowrie.command.input` |
| `2026-08-07 09:02:41` | `cowrie.log.closed` |
| `2026-08-07 09:02:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]222` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]222` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5498dab52ad

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]222` |
| **First Seen** | 2026-08-07 09:02 |
| **Last Seen** | 2026-08-07 09:02 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 09:02:37` | `cowrie.session.connect` |
| `2026-08-07 09:02:39` | `cowrie.client.version` |
| `2026-08-07 09:02:39` | `cowrie.client.kex` |
| `2026-08-07 09:02:46` | `cowrie.login.success` |
| `2026-08-07 09:02:49` | `cowrie.session.params` |
| `2026-08-07 09:02:49` | `cowrie.command.input` |
| `2026-08-07 09:02:50` | `cowrie.log.closed` |
| `2026-08-07 09:02:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]222` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]222` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-739bb8430e9d

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]222` |
| **First Seen** | 2026-08-07 09:02 |
| **Last Seen** | 2026-08-07 09:03 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 09:02:48` | `cowrie.session.connect` |
| `2026-08-07 09:02:50` | `cowrie.client.version` |
| `2026-08-07 09:02:50` | `cowrie.client.kex` |
| `2026-08-07 09:02:56` | `cowrie.login.success` |
| `2026-08-07 09:03:00` | `cowrie.session.params` |
| `2026-08-07 09:03:00` | `cowrie.command.input` |
| `2026-08-07 09:03:01` | `cowrie.log.closed` |
| `2026-08-07 09:03:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]222` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]222` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f03b542e7fd

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]222` |
| **First Seen** | 2026-08-07 09:02 |
| **Last Seen** | 2026-08-07 09:03 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 09:02:59` | `cowrie.session.connect` |
| `2026-08-07 09:03:00` | `cowrie.client.version` |
| `2026-08-07 09:03:00` | `cowrie.client.kex` |
| `2026-08-07 09:03:07` | `cowrie.login.success` |
| `2026-08-07 09:03:10` | `cowrie.session.params` |
| `2026-08-07 09:03:10` | `cowrie.command.input` |
| `2026-08-07 09:03:12` | `cowrie.log.closed` |
| `2026-08-07 09:03:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]222` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]222` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7988fcfefbd3

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-07 09:03 |
| **Last Seen** | 2026-08-07 09:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 09:03:28` | `cowrie.session.connect` |
| `2026-08-07 09:03:28` | `cowrie.client.version` |
| `2026-08-07 09:03:28` | `cowrie.client.kex` |
| `2026-08-07 09:03:29` | `cowrie.login.success` |
| `2026-08-07 09:03:29` | `cowrie.session.params` |
| `2026-08-07 09:03:29` | `cowrie.command.input` |
| `2026-08-07 09:03:30` | `cowrie.log.closed` |
| `2026-08-07 09:03:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5f338c876d1

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-07 09:05 |
| **Last Seen** | 2026-08-07 09:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 09:05:17` | `cowrie.session.connect` |
| `2026-08-07 09:05:17` | `cowrie.client.version` |
| `2026-08-07 09:05:18` | `cowrie.client.kex` |
| `2026-08-07 09:05:18` | `cowrie.login.success` |
| `2026-08-07 09:05:18` | `cowrie.session.params` |
| `2026-08-07 09:05:18` | `cowrie.command.input` |
| `2026-08-07 09:05:19` | `cowrie.log.closed` |
| `2026-08-07 09:05:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78f985c922ed

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-07 09:07 |
| **Last Seen** | 2026-08-07 09:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 09:07:13` | `cowrie.session.connect` |
| `2026-08-07 09:07:13` | `cowrie.client.version` |
| `2026-08-07 09:07:14` | `cowrie.client.kex` |
| `2026-08-07 09:07:14` | `cowrie.login.success` |
| `2026-08-07 09:07:15` | `cowrie.session.params` |
| `2026-08-07 09:07:15` | `cowrie.command.input` |
| `2026-08-07 09:07:15` | `cowrie.log.closed` |
| `2026-08-07 09:07:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ba771501135

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-07 09:09 |
| **Last Seen** | 2026-08-07 09:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 09:09:08` | `cowrie.session.connect` |
| `2026-08-07 09:09:08` | `cowrie.client.version` |
| `2026-08-07 09:09:08` | `cowrie.client.kex` |
| `2026-08-07 09:09:08` | `cowrie.login.success` |
| `2026-08-07 09:09:09` | `cowrie.session.params` |
| `2026-08-07 09:09:09` | `cowrie.command.input` |
| `2026-08-07 09:09:09` | `cowrie.log.closed` |
| `2026-08-07 09:09:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aefe352e8355

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-07 09:10 |
| **Last Seen** | 2026-08-07 09:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 09:10:58` | `cowrie.session.connect` |
| `2026-08-07 09:10:58` | `cowrie.client.version` |
| `2026-08-07 09:10:58` | `cowrie.client.kex` |
| `2026-08-07 09:10:58` | `cowrie.login.success` |
| `2026-08-07 09:10:59` | `cowrie.session.params` |
| `2026-08-07 09:10:59` | `cowrie.command.input` |
| `2026-08-07 09:10:59` | `cowrie.log.closed` |
| `2026-08-07 09:10:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e3ba9da09fe

| Field | Detail |
|---|---|
| **Source IP** | `91.219.196[.]17` |
| **First Seen** | 2026-08-07 09:11 |
| **Last Seen** | 2026-08-07 09:12 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 09:11:58` | `cowrie.session.connect` |
| `2026-08-07 09:11:59` | `cowrie.client.version` |
| `2026-08-07 09:11:59` | `cowrie.client.kex` |
| `2026-08-07 09:12:00` | `cowrie.login.success` |
| `2026-08-07 09:12:00` | `cowrie.direct-tcpip.request` |
| `2026-08-07 09:12:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.219.196[.]17` to AbuseIPDB if not already reported
- [ ] Block `91.219.196[.]17` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3764f101c0d6

| Field | Detail |
|---|---|
| **Source IP** | `31.77.227[.]120` |
| **First Seen** | 2026-08-07 09:12 |
| **Last Seen** | 2026-08-07 09:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 09:12:43` | `cowrie.session.connect` |
| `2026-08-07 09:12:43` | `cowrie.client.version` |
| `2026-08-07 09:12:43` | `cowrie.client.kex` |
| `2026-08-07 09:12:43` | `cowrie.login.success` |
| `2026-08-07 09:12:44` | `cowrie.session.params` |
| `2026-08-07 09:12:44` | `cowrie.command.input` |
| `2026-08-07 09:12:44` | `cowrie.log.closed` |
| `2026-08-07 09:12:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.77.227[.]120` to AbuseIPDB if not already reported
- [ ] Block `31.77.227[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-876661e032b2

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-07 09:12 |
| **Last Seen** | 2026-08-07 09:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 09:12:52` | `cowrie.session.connect` |
| `2026-08-07 09:12:52` | `cowrie.client.version` |
| `2026-08-07 09:12:52` | `cowrie.client.kex` |
| `2026-08-07 09:12:53` | `cowrie.login.success` |
| `2026-08-07 09:12:53` | `cowrie.session.params` |
| `2026-08-07 09:12:53` | `cowrie.command.input` |
| `2026-08-07 09:12:53` | `cowrie.log.closed` |
| `2026-08-07 09:12:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f45a0c919882

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-07 09:14 |
| **Last Seen** | 2026-08-07 09:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 09:14:46` | `cowrie.session.connect` |
| `2026-08-07 09:14:46` | `cowrie.client.version` |
| `2026-08-07 09:14:46` | `cowrie.client.kex` |
| `2026-08-07 09:14:46` | `cowrie.login.success` |
| `2026-08-07 09:14:47` | `cowrie.session.params` |
| `2026-08-07 09:14:47` | `cowrie.command.input` |
| `2026-08-07 09:14:47` | `cowrie.log.closed` |
| `2026-08-07 09:14:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac568bb7c432

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-07 09:16 |
| **Last Seen** | 2026-08-07 09:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 09:16:33` | `cowrie.session.connect` |
| `2026-08-07 09:16:33` | `cowrie.client.version` |
| `2026-08-07 09:16:33` | `cowrie.client.kex` |
| `2026-08-07 09:16:34` | `cowrie.login.success` |
| `2026-08-07 09:16:35` | `cowrie.session.params` |
| `2026-08-07 09:16:35` | `cowrie.command.input` |
| `2026-08-07 09:16:35` | `cowrie.log.closed` |
| `2026-08-07 09:16:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-101d62e6f3a8

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-07 09:18 |
| **Last Seen** | 2026-08-07 09:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 09:18:23` | `cowrie.session.connect` |
| `2026-08-07 09:18:23` | `cowrie.client.version` |
| `2026-08-07 09:18:23` | `cowrie.client.kex` |
| `2026-08-07 09:18:23` | `cowrie.login.success` |
| `2026-08-07 09:18:24` | `cowrie.session.params` |
| `2026-08-07 09:18:24` | `cowrie.command.input` |
| `2026-08-07 09:18:24` | `cowrie.log.closed` |
| `2026-08-07 09:18:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c196f993d366

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-07 09:20 |
| **Last Seen** | 2026-08-07 09:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 09:20:16` | `cowrie.session.connect` |
| `2026-08-07 09:20:16` | `cowrie.client.version` |
| `2026-08-07 09:20:16` | `cowrie.client.kex` |
| `2026-08-07 09:20:16` | `cowrie.login.success` |
| `2026-08-07 09:20:17` | `cowrie.session.params` |
| `2026-08-07 09:20:17` | `cowrie.command.input` |
| `2026-08-07 09:20:17` | `cowrie.log.closed` |
| `2026-08-07 09:20:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-674e09e6da60

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-07 09:22 |
| **Last Seen** | 2026-08-07 09:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 09:22:05` | `cowrie.session.connect` |
| `2026-08-07 09:22:05` | `cowrie.client.version` |
| `2026-08-07 09:22:05` | `cowrie.client.kex` |
| `2026-08-07 09:22:05` | `cowrie.login.success` |
| `2026-08-07 09:22:06` | `cowrie.session.params` |
| `2026-08-07 09:22:06` | `cowrie.command.input` |
| `2026-08-07 09:22:06` | `cowrie.log.closed` |
| `2026-08-07 09:22:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d8da52ca5ac

| Field | Detail |
|---|---|
| **Source IP** | `122.176.45[.]238` |
| **First Seen** | 2026-08-07 09:22 |
| **Last Seen** | 2026-08-07 09:22 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 09:22:51` | `cowrie.session.connect` |
| `2026-08-07 09:22:52` | `cowrie.client.version` |
| `2026-08-07 09:22:52` | `cowrie.client.kex` |
| `2026-08-07 09:22:54` | `cowrie.login.success` |
| `2026-08-07 09:22:54` | `cowrie.direct-tcpip.request` |
| `2026-08-07 09:22:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.176.45[.]238` to AbuseIPDB if not already reported
- [ ] Block `122.176.45[.]238` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c02334c95cd

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-07 09:23 |
| **Last Seen** | 2026-08-07 09:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 09:23:53` | `cowrie.session.connect` |
| `2026-08-07 09:23:53` | `cowrie.client.version` |
| `2026-08-07 09:23:53` | `cowrie.client.kex` |
| `2026-08-07 09:23:53` | `cowrie.login.success` |
| `2026-08-07 09:23:54` | `cowrie.session.params` |
| `2026-08-07 09:23:54` | `cowrie.command.input` |
| `2026-08-07 09:23:54` | `cowrie.log.closed` |
| `2026-08-07 09:23:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02e577b057ad

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-07 09:25 |
| **Last Seen** | 2026-08-07 09:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 09:25:46` | `cowrie.session.connect` |
| `2026-08-07 09:25:46` | `cowrie.client.version` |
| `2026-08-07 09:25:46` | `cowrie.client.kex` |
| `2026-08-07 09:25:46` | `cowrie.login.success` |
| `2026-08-07 09:25:47` | `cowrie.session.params` |
| `2026-08-07 09:25:47` | `cowrie.command.input` |
| `2026-08-07 09:25:47` | `cowrie.log.closed` |
| `2026-08-07 09:25:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e4bbb17da03

| Field | Detail |
|---|---|
| **Source IP** | `117.198.99[.]18` |
| **First Seen** | 2026-08-07 09:25 |
| **Last Seen** | 2026-08-07 09:26 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 09:25:51` | `cowrie.session.connect` |
| `2026-08-07 09:25:52` | `cowrie.client.version` |
| `2026-08-07 09:25:52` | `cowrie.client.kex` |
| `2026-08-07 09:25:55` | `cowrie.login.success` |
| `2026-08-07 09:25:56` | `cowrie.direct-tcpip.request` |
| `2026-08-07 09:26:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.198.99[.]18` to AbuseIPDB if not already reported
- [ ] Block `117.198.99[.]18` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55c8b7ead12a

| Field | Detail |
|---|---|
| **Source IP** | `218.248.19[.]102` |
| **First Seen** | 2026-08-07 09:26 |
| **Last Seen** | 2026-08-07 09:26 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 09:26:01` | `cowrie.session.connect` |
| `2026-08-07 09:26:02` | `cowrie.client.version` |
| `2026-08-07 09:26:02` | `cowrie.client.kex` |
| `2026-08-07 09:26:04` | `cowrie.login.success` |
| `2026-08-07 09:26:04` | `cowrie.direct-tcpip.request` |
| `2026-08-07 09:26:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.248.19[.]102` to AbuseIPDB if not already reported
- [ ] Block `218.248.19[.]102` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8334d2e5dd9f

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-07 09:27 |
| **Last Seen** | 2026-08-07 09:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 09:27:41` | `cowrie.session.connect` |
| `2026-08-07 09:27:41` | `cowrie.client.version` |
| `2026-08-07 09:27:41` | `cowrie.client.kex` |
| `2026-08-07 09:27:42` | `cowrie.login.success` |
| `2026-08-07 09:27:42` | `cowrie.session.params` |
| `2026-08-07 09:27:42` | `cowrie.command.input` |
| `2026-08-07 09:27:42` | `cowrie.log.closed` |
| `2026-08-07 09:27:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-778adf5fb505

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-07 09:29 |
| **Last Seen** | 2026-08-07 09:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 09:29:31` | `cowrie.session.connect` |
| `2026-08-07 09:29:31` | `cowrie.client.version` |
| `2026-08-07 09:29:31` | `cowrie.client.kex` |
| `2026-08-07 09:29:31` | `cowrie.login.success` |
| `2026-08-07 09:29:32` | `cowrie.session.params` |
| `2026-08-07 09:29:32` | `cowrie.command.input` |
| `2026-08-07 09:29:32` | `cowrie.log.closed` |
| `2026-08-07 09:29:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3927c46e58e3

| Field | Detail |
|---|---|
| **Source IP** | `218.13.214[.]18` |
| **First Seen** | 2026-08-07 09:29 |
| **Last Seen** | 2026-08-07 09:30 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 09:29:59` | `cowrie.session.connect` |
| `2026-08-07 09:30:00` | `cowrie.client.version` |
| `2026-08-07 09:30:00` | `cowrie.client.kex` |
| `2026-08-07 09:30:02` | `cowrie.login.success` |
| `2026-08-07 09:30:03` | `cowrie.direct-tcpip.request` |
| `2026-08-07 09:30:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.13.214[.]18` to AbuseIPDB if not already reported
- [ ] Block `218.13.214[.]18` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd833d57f49b

| Field | Detail |
|---|---|
| **Source IP** | `124.167.20[.]113` |
| **First Seen** | 2026-08-07 09:30 |
| **Last Seen** | 2026-08-07 09:30 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 09:30:14` | `cowrie.session.connect` |
| `2026-08-07 09:30:14` | `cowrie.client.version` |
| `2026-08-07 09:30:14` | `cowrie.client.kex` |
| `2026-08-07 09:30:16` | `cowrie.login.success` |
| `2026-08-07 09:30:17` | `cowrie.direct-tcpip.request` |
| `2026-08-07 09:30:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.167.20[.]113` to AbuseIPDB if not already reported
- [ ] Block `124.167.20[.]113` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-968bef107222

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-07 09:31 |
| **Last Seen** | 2026-08-07 09:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 09:31:26` | `cowrie.session.connect` |
| `2026-08-07 09:31:26` | `cowrie.client.version` |
| `2026-08-07 09:31:27` | `cowrie.client.kex` |
| `2026-08-07 09:31:27` | `cowrie.login.success` |
| `2026-08-07 09:31:28` | `cowrie.session.params` |
| `2026-08-07 09:31:28` | `cowrie.command.input` |
| `2026-08-07 09:31:28` | `cowrie.log.closed` |
| `2026-08-07 09:31:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ddd69e1e7121

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-07 09:33 |
| **Last Seen** | 2026-08-07 09:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 09:33:25` | `cowrie.session.connect` |
| `2026-08-07 09:33:25` | `cowrie.client.version` |
| `2026-08-07 09:33:25` | `cowrie.client.kex` |
| `2026-08-07 09:33:25` | `cowrie.login.success` |
| `2026-08-07 09:33:26` | `cowrie.session.params` |
| `2026-08-07 09:33:26` | `cowrie.command.input` |
| `2026-08-07 09:33:26` | `cowrie.log.closed` |
| `2026-08-07 09:33:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d915eeac262

| Field | Detail |
|---|---|
| **Source IP** | `54.37.235[.]85` |
| **First Seen** | 2026-08-07 09:33 |
| **Last Seen** | 2026-08-07 09:33 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 09:33:25` | `cowrie.session.connect` |
| `2026-08-07 09:33:25` | `cowrie.client.version` |
| `2026-08-07 09:33:25` | `cowrie.client.kex` |
| `2026-08-07 09:33:26` | `cowrie.login.success` |
| `2026-08-07 09:33:27` | `cowrie.session.params` |
| `2026-08-07 09:33:27` | `cowrie.command.input` |
| `2026-08-07 09:33:27` | `cowrie.command.failed` |
| `2026-08-07 09:33:27` | `cowrie.log.closed` |
| `2026-08-07 09:33:28` | `cowrie.session.params` |
| `2026-08-07 09:33:28` | `cowrie.command.input` |
| `2026-08-07 09:33:28` | `cowrie.session.file_download` |
| `2026-08-07 09:33:28` | `cowrie.log.closed` |
| `2026-08-07 09:33:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `54.37.235[.]85` to AbuseIPDB if not already reported
- [ ] Block `54.37.235[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c9ea4f74ebc

| Field | Detail |
|---|---|
| **Source IP** | `54.37.235[.]85` |
| **First Seen** | 2026-08-07 09:33 |
| **Last Seen** | 2026-08-07 09:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 09:33:28` | `cowrie.session.connect` |
| `2026-08-07 09:33:28` | `cowrie.client.version` |
| `2026-08-07 09:33:28` | `cowrie.client.kex` |
| `2026-08-07 09:33:29` | `cowrie.login.success` |
| `2026-08-07 09:33:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `54.37.235[.]85` to AbuseIPDB if not already reported
- [ ] Block `54.37.235[.]85` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e9621cba148

| Field | Detail |
|---|---|
| **Source IP** | `54.37.235[.]85` |
| **First Seen** | 2026-08-07 09:33 |
| **Last Seen** | 2026-08-07 09:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 09:33:29` | `cowrie.session.connect` |
| `2026-08-07 09:33:29` | `cowrie.client.version` |
| `2026-08-07 09:33:29` | `cowrie.client.kex` |
| `2026-08-07 09:33:30` | `cowrie.login.success` |
| `2026-08-07 09:33:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `54.37.235[.]85` to AbuseIPDB if not already reported
- [ ] Block `54.37.235[.]85` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c16a26f56925

| Field | Detail |
|---|---|
| **Source IP** | `103.163.117[.]230` |
| **First Seen** | 2026-08-07 09:34 |
| **Last Seen** | 2026-08-07 09:34 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 09:34:37` | `cowrie.session.connect` |
| `2026-08-07 09:34:37` | `cowrie.client.version` |
| `2026-08-07 09:34:37` | `cowrie.client.kex` |
| `2026-08-07 09:34:38` | `cowrie.login.success` |
| `2026-08-07 09:34:39` | `cowrie.session.params` |
| `2026-08-07 09:34:39` | `cowrie.command.input` |
| `2026-08-07 09:34:39` | `cowrie.command.failed` |
| `2026-08-07 09:34:39` | `cowrie.log.closed` |
| `2026-08-07 09:34:40` | `cowrie.session.params` |
| `2026-08-07 09:34:40` | `cowrie.command.input` |
| `2026-08-07 09:34:41` | `cowrie.session.file_download` |
| `2026-08-07 09:34:41` | `cowrie.log.closed` |
| `2026-08-07 09:34:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.163.117[.]230` to AbuseIPDB if not already reported
- [ ] Block `103.163.117[.]230` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8a786018e93

| Field | Detail |
|---|---|
| **Source IP** | `103.163.117[.]224` |
| **First Seen** | 2026-08-07 09:34 |
| **Last Seen** | 2026-08-07 09:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 09:34:41` | `cowrie.session.connect` |
| `2026-08-07 09:34:41` | `cowrie.client.version` |
| `2026-08-07 09:34:41` | `cowrie.client.kex` |
| `2026-08-07 09:34:42` | `cowrie.login.success` |
| `2026-08-07 09:34:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.163.117[.]224` to AbuseIPDB if not already reported
- [ ] Block `103.163.117[.]224` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82f2887505fb

| Field | Detail |
|---|---|
| **Source IP** | `103.163.117[.]230` |
| **First Seen** | 2026-08-07 09:34 |
| **Last Seen** | 2026-08-07 09:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 09:34:43` | `cowrie.session.connect` |
| `2026-08-07 09:34:43` | `cowrie.client.version` |
| `2026-08-07 09:34:43` | `cowrie.client.kex` |
| `2026-08-07 09:34:44` | `cowrie.login.success` |
| `2026-08-07 09:34:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.163.117[.]230` to AbuseIPDB if not already reported
- [ ] Block `103.163.117[.]230` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8cd93d206620

| Field | Detail |
|---|---|
| **Source IP** | `153.37.177[.]219` |
| **First Seen** | 2026-08-07 09:34 |
| **Last Seen** | 2026-08-07 09:34 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 09:34:45` | `cowrie.session.connect` |
| `2026-08-07 09:34:46` | `cowrie.client.version` |
| `2026-08-07 09:34:46` | `cowrie.client.kex` |
| `2026-08-07 09:34:48` | `cowrie.login.success` |
| `2026-08-07 09:34:49` | `cowrie.direct-tcpip.request` |
| `2026-08-07 09:34:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `153.37.177[.]219` to AbuseIPDB if not already reported
- [ ] Block `153.37.177[.]219` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61732f30c159

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-07 09:35 |
| **Last Seen** | 2026-08-07 09:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 09:35:18` | `cowrie.session.connect` |
| `2026-08-07 09:35:18` | `cowrie.client.version` |
| `2026-08-07 09:35:18` | `cowrie.client.kex` |
| `2026-08-07 09:35:18` | `cowrie.login.success` |
| `2026-08-07 09:35:19` | `cowrie.session.params` |
| `2026-08-07 09:35:19` | `cowrie.command.input` |
| `2026-08-07 09:35:19` | `cowrie.log.closed` |
| `2026-08-07 09:35:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-97eb6d4ed902

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-07 09:37 |
| **Last Seen** | 2026-08-07 09:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 09:37:07` | `cowrie.session.connect` |
| `2026-08-07 09:37:07` | `cowrie.client.version` |
| `2026-08-07 09:37:07` | `cowrie.client.kex` |
| `2026-08-07 09:37:07` | `cowrie.login.success` |
| `2026-08-07 09:37:08` | `cowrie.session.params` |
| `2026-08-07 09:37:08` | `cowrie.command.input` |
| `2026-08-07 09:37:08` | `cowrie.log.closed` |
| `2026-08-07 09:37:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f6e67e08277

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-07 09:39 |
| **Last Seen** | 2026-08-07 09:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 09:39:00` | `cowrie.session.connect` |
| `2026-08-07 09:39:00` | `cowrie.client.version` |
| `2026-08-07 09:39:00` | `cowrie.client.kex` |
| `2026-08-07 09:39:01` | `cowrie.login.success` |
| `2026-08-07 09:39:02` | `cowrie.session.params` |
| `2026-08-07 09:39:02` | `cowrie.command.input` |
| `2026-08-07 09:39:02` | `cowrie.log.closed` |
| `2026-08-07 09:39:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ba44c7fa31f

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-07 09:40 |
| **Last Seen** | 2026-08-07 09:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 09:40:51` | `cowrie.session.connect` |
| `2026-08-07 09:40:51` | `cowrie.client.version` |
| `2026-08-07 09:40:51` | `cowrie.client.kex` |
| `2026-08-07 09:40:51` | `cowrie.login.success` |
| `2026-08-07 09:40:52` | `cowrie.session.params` |
| `2026-08-07 09:40:52` | `cowrie.command.input` |
| `2026-08-07 09:40:52` | `cowrie.log.closed` |
| `2026-08-07 09:40:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b369755bd60e

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-07 09:42 |
| **Last Seen** | 2026-08-07 09:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 09:42:39` | `cowrie.session.connect` |
| `2026-08-07 09:42:39` | `cowrie.client.version` |
| `2026-08-07 09:42:39` | `cowrie.client.kex` |
| `2026-08-07 09:42:39` | `cowrie.login.success` |
| `2026-08-07 09:42:40` | `cowrie.session.params` |
| `2026-08-07 09:42:40` | `cowrie.command.input` |
| `2026-08-07 09:42:40` | `cowrie.log.closed` |
| `2026-08-07 09:42:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d964de8734e

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-07 09:43 |
| **Last Seen** | 2026-08-07 09:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 09:43:27` | `cowrie.session.connect` |
| `2026-08-07 09:43:27` | `cowrie.client.version` |
| `2026-08-07 09:43:27` | `cowrie.client.kex` |
| `2026-08-07 09:43:27` | `cowrie.login.success` |
| `2026-08-07 09:43:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7433e14a773f

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-07 09:43 |
| **Last Seen** | 2026-08-07 09:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 09:43:28` | `cowrie.session.connect` |
| `2026-08-07 09:43:28` | `cowrie.client.version` |
| `2026-08-07 09:43:28` | `cowrie.client.kex` |
| `2026-08-07 09:43:28` | `cowrie.login.success` |
| `2026-08-07 09:43:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4842f3db39d

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-07 09:43 |
| **Last Seen** | 2026-08-07 09:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 09:43:36` | `cowrie.session.connect` |
| `2026-08-07 09:43:36` | `cowrie.client.version` |
| `2026-08-07 09:43:36` | `cowrie.client.kex` |
| `2026-08-07 09:43:36` | `cowrie.login.success` |
| `2026-08-07 09:43:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-485557729cb9

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-07 09:43 |
| **Last Seen** | 2026-08-07 09:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 09:43:36` | `cowrie.session.connect` |
| `2026-08-07 09:43:36` | `cowrie.client.version` |
| `2026-08-07 09:43:36` | `cowrie.client.kex` |
| `2026-08-07 09:43:36` | `cowrie.login.success` |
| `2026-08-07 09:43:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19464301982d

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-07 09:44 |
| **Last Seen** | 2026-08-07 09:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 09:44:10` | `cowrie.session.connect` |
| `2026-08-07 09:44:10` | `cowrie.client.version` |
| `2026-08-07 09:44:11` | `cowrie.client.kex` |
| `2026-08-07 09:44:11` | `cowrie.login.success` |
| `2026-08-07 09:44:11` | `cowrie.direct-tcpip.request` |
| `2026-08-07 09:44:11` | `cowrie.direct-tcpip.data` |
| `2026-08-07 09:44:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eee65644c8c8

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-07 09:44 |
| **Last Seen** | 2026-08-07 09:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 09:44:34` | `cowrie.session.connect` |
| `2026-08-07 09:44:34` | `cowrie.client.version` |
| `2026-08-07 09:44:34` | `cowrie.client.kex` |
| `2026-08-07 09:44:34` | `cowrie.login.success` |
| `2026-08-07 09:44:35` | `cowrie.session.params` |
| `2026-08-07 09:44:35` | `cowrie.command.input` |
| `2026-08-07 09:44:35` | `cowrie.log.closed` |
| `2026-08-07 09:44:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6dd9f93f04b

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-07 09:46 |
| **Last Seen** | 2026-08-07 09:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 09:46:33` | `cowrie.session.connect` |
| `2026-08-07 09:46:33` | `cowrie.client.version` |
| `2026-08-07 09:46:33` | `cowrie.client.kex` |
| `2026-08-07 09:46:33` | `cowrie.login.success` |
| `2026-08-07 09:46:34` | `cowrie.session.params` |
| `2026-08-07 09:46:34` | `cowrie.command.input` |
| `2026-08-07 09:46:34` | `cowrie.log.closed` |
| `2026-08-07 09:46:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7adacb7f8b39

| Field | Detail |
|---|---|
| **Source IP** | `58.17.128[.]7` |
| **First Seen** | 2026-08-07 09:46 |
| **Last Seen** | 2026-08-07 09:46 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 09:46:42` | `cowrie.session.connect` |
| `2026-08-07 09:46:43` | `cowrie.client.version` |
| `2026-08-07 09:46:43` | `cowrie.client.kex` |
| `2026-08-07 09:46:45` | `cowrie.login.success` |
| `2026-08-07 09:46:46` | `cowrie.direct-tcpip.request` |
| `2026-08-07 09:46:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.17.128[.]7` to AbuseIPDB if not already reported
- [ ] Block `58.17.128[.]7` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d9ef30c76704

| Field | Detail |
|---|---|
| **Source IP** | `201.63.52[.]54` |
| **First Seen** | 2026-08-07 09:46 |
| **Last Seen** | 2026-08-07 09:46 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 09:46:51` | `cowrie.session.connect` |
| `2026-08-07 09:46:52` | `cowrie.client.version` |
| `2026-08-07 09:46:52` | `cowrie.client.kex` |
| `2026-08-07 09:46:53` | `cowrie.login.success` |
| `2026-08-07 09:46:54` | `cowrie.direct-tcpip.request` |
| `2026-08-07 09:46:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.63.52[.]54` to AbuseIPDB if not already reported
- [ ] Block `201.63.52[.]54` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07abcfec4a50

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-07 09:48 |
| **Last Seen** | 2026-08-07 09:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 09:48:20` | `cowrie.session.connect` |
| `2026-08-07 09:48:20` | `cowrie.client.version` |
| `2026-08-07 09:48:21` | `cowrie.client.kex` |
| `2026-08-07 09:48:21` | `cowrie.login.success` |
| `2026-08-07 09:48:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76d46ec08e5e

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-07 09:48 |
| **Last Seen** | 2026-08-07 09:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 09:48:21` | `cowrie.session.connect` |
| `2026-08-07 09:48:21` | `cowrie.client.version` |
| `2026-08-07 09:48:22` | `cowrie.client.kex` |
| `2026-08-07 09:48:22` | `cowrie.login.success` |
| `2026-08-07 09:48:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b57200a11df

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-07 09:48 |
| **Last Seen** | 2026-08-07 09:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 09:48:27` | `cowrie.session.connect` |
| `2026-08-07 09:48:27` | `cowrie.client.version` |
| `2026-08-07 09:48:28` | `cowrie.client.kex` |
| `2026-08-07 09:48:28` | `cowrie.login.success` |
| `2026-08-07 09:48:29` | `cowrie.session.params` |
| `2026-08-07 09:48:29` | `cowrie.command.input` |
| `2026-08-07 09:48:29` | `cowrie.log.closed` |
| `2026-08-07 09:48:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb86a0fb5db1

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-07 09:50 |
| **Last Seen** | 2026-08-07 09:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 09:50:23` | `cowrie.session.connect` |
| `2026-08-07 09:50:23` | `cowrie.client.version` |
| `2026-08-07 09:50:23` | `cowrie.client.kex` |
| `2026-08-07 09:50:24` | `cowrie.login.success` |
| `2026-08-07 09:50:24` | `cowrie.session.params` |
| `2026-08-07 09:50:24` | `cowrie.command.input` |
| `2026-08-07 09:50:25` | `cowrie.log.closed` |
| `2026-08-07 09:50:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78daa6b7363c

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-07 09:52 |
| **Last Seen** | 2026-08-07 09:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 09:52:22` | `cowrie.session.connect` |
| `2026-08-07 09:52:22` | `cowrie.client.version` |
| `2026-08-07 09:52:22` | `cowrie.client.kex` |
| `2026-08-07 09:52:22` | `cowrie.login.success` |
| `2026-08-07 09:52:23` | `cowrie.session.params` |
| `2026-08-07 09:52:23` | `cowrie.command.input` |
| `2026-08-07 09:52:23` | `cowrie.log.closed` |
| `2026-08-07 09:52:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ea22b15d896

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-07 09:54 |
| **Last Seen** | 2026-08-07 09:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 09:54:15` | `cowrie.session.connect` |
| `2026-08-07 09:54:15` | `cowrie.client.version` |
| `2026-08-07 09:54:15` | `cowrie.client.kex` |
| `2026-08-07 09:54:15` | `cowrie.login.success` |
| `2026-08-07 09:54:16` | `cowrie.session.params` |
| `2026-08-07 09:54:16` | `cowrie.command.input` |
| `2026-08-07 09:54:16` | `cowrie.log.closed` |
| `2026-08-07 09:54:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-330cbe6e1ee0

| Field | Detail |
|---|---|
| **Source IP** | `187.8.120[.]90` |
| **First Seen** | 2026-08-07 09:54 |
| **Last Seen** | 2026-08-07 09:54 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 09:54:31` | `cowrie.session.connect` |
| `2026-08-07 09:54:32` | `cowrie.client.version` |
| `2026-08-07 09:54:32` | `cowrie.client.kex` |
| `2026-08-07 09:54:34` | `cowrie.login.success` |
| `2026-08-07 09:54:34` | `cowrie.direct-tcpip.request` |
| `2026-08-07 09:54:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.8.120[.]90` to AbuseIPDB if not already reported
- [ ] Block `187.8.120[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81007387e7cd

| Field | Detail |
|---|---|
| **Source IP** | `80.233.77[.]136` |
| **First Seen** | 2026-08-07 09:54 |
| **Last Seen** | 2026-08-07 09:54 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 09:54:39` | `cowrie.session.connect` |
| `2026-08-07 09:54:40` | `cowrie.client.version` |
| `2026-08-07 09:54:40` | `cowrie.client.kex` |
| `2026-08-07 09:54:41` | `cowrie.login.success` |
| `2026-08-07 09:54:41` | `cowrie.direct-tcpip.request` |
| `2026-08-07 09:54:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.233.77[.]136` to AbuseIPDB if not already reported
- [ ] Block `80.233.77[.]136` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b94bdf92934

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-07 09:56 |
| **Last Seen** | 2026-08-07 09:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 09:56:04` | `cowrie.session.connect` |
| `2026-08-07 09:56:04` | `cowrie.client.version` |
| `2026-08-07 09:56:04` | `cowrie.client.kex` |
| `2026-08-07 09:56:04` | `cowrie.login.success` |
| `2026-08-07 09:56:05` | `cowrie.session.params` |
| `2026-08-07 09:56:05` | `cowrie.command.input` |
| `2026-08-07 09:56:05` | `cowrie.log.closed` |
| `2026-08-07 09:56:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec32da6819cd

| Field | Detail |
|---|---|
| **Source IP** | `116.114.94[.]242` |
| **First Seen** | 2026-08-07 09:57 |
| **Last Seen** | 2026-08-07 09:57 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 09:57:14` | `cowrie.session.connect` |
| `2026-08-07 09:57:14` | `cowrie.client.version` |
| `2026-08-07 09:57:14` | `cowrie.client.kex` |
| `2026-08-07 09:57:16` | `cowrie.login.success` |
| `2026-08-07 09:57:17` | `cowrie.direct-tcpip.request` |
| `2026-08-07 09:57:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.114.94[.]242` to AbuseIPDB if not already reported
- [ ] Block `116.114.94[.]242` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64884921baa2

| Field | Detail |
|---|---|
| **Source IP** | `60.12.5[.]190` |
| **First Seen** | 2026-08-07 09:57 |
| **Last Seen** | 2026-08-07 09:57 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 09:57:26` | `cowrie.session.connect` |
| `2026-08-07 09:57:27` | `cowrie.client.version` |
| `2026-08-07 09:57:27` | `cowrie.client.kex` |
| `2026-08-07 09:57:30` | `cowrie.login.success` |
| `2026-08-07 09:57:31` | `cowrie.direct-tcpip.request` |
| `2026-08-07 09:57:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.12.5[.]190` to AbuseIPDB if not already reported
- [ ] Block `60.12.5[.]190` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01e17b57d508

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-07 09:58 |
| **Last Seen** | 2026-08-07 09:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 09:58:00` | `cowrie.session.connect` |
| `2026-08-07 09:58:00` | `cowrie.client.version` |
| `2026-08-07 09:58:00` | `cowrie.client.kex` |
| `2026-08-07 09:58:00` | `cowrie.login.success` |
| `2026-08-07 09:58:01` | `cowrie.session.params` |
| `2026-08-07 09:58:01` | `cowrie.command.input` |
| `2026-08-07 09:58:01` | `cowrie.log.closed` |
| `2026-08-07 09:58:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db29277477db

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-07 09:59 |
| **Last Seen** | 2026-08-07 09:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 09:59:54` | `cowrie.session.connect` |
| `2026-08-07 09:59:54` | `cowrie.client.version` |
| `2026-08-07 09:59:54` | `cowrie.client.kex` |
| `2026-08-07 09:59:55` | `cowrie.login.success` |
| `2026-08-07 09:59:56` | `cowrie.session.params` |
| `2026-08-07 09:59:56` | `cowrie.command.input` |
| `2026-08-07 09:59:56` | `cowrie.log.closed` |
| `2026-08-07 09:59:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0bc3f2fabc42

| Field | Detail |
|---|---|
| **Source IP** | `49.124.149[.]209` |
| **First Seen** | 2026-08-07 10:04 |
| **Last Seen** | 2026-08-07 10:04 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 10:04:47` | `cowrie.session.connect` |
| `2026-08-07 10:04:48` | `cowrie.client.version` |
| `2026-08-07 10:04:48` | `cowrie.client.kex` |
| `2026-08-07 10:04:49` | `cowrie.login.success` |
| `2026-08-07 10:04:50` | `cowrie.direct-tcpip.request` |
| `2026-08-07 10:04:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.149[.]209` to AbuseIPDB if not already reported
- [ ] Block `49.124.149[.]209` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1cdc3696f07c

| Field | Detail |
|---|---|
| **Source IP** | `117.69.255[.]239` |
| **First Seen** | 2026-08-07 10:05 |
| **Last Seen** | 2026-08-07 10:05 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 10:05:00` | `cowrie.session.connect` |
| `2026-08-07 10:05:01` | `cowrie.client.version` |
| `2026-08-07 10:05:01` | `cowrie.client.kex` |
| `2026-08-07 10:05:04` | `cowrie.login.success` |
| `2026-08-07 10:05:04` | `cowrie.direct-tcpip.request` |
| `2026-08-07 10:05:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.69.255[.]239` to AbuseIPDB if not already reported
- [ ] Block `117.69.255[.]239` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bec71f37a3b9

| Field | Detail |
|---|---|
| **Source IP** | `34.53.157[.]23` |
| **First Seen** | 2026-08-07 10:11 |
| **Last Seen** | 2026-08-07 10:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 10:11:05` | `cowrie.session.connect` |
| `2026-08-07 10:11:05` | `cowrie.login.success` |
| `2026-08-07 10:11:06` | `cowrie.session.params` |
| `2026-08-07 10:11:06` | `cowrie.command.input` |
| `2026-08-07 10:11:06` | `cowrie.command.input` |
| `2026-08-07 10:11:06` | `cowrie.command.failed` |
| `2026-08-07 10:11:06` | `cowrie.command.input` |
| `2026-08-07 10:11:06` | `cowrie.log.closed` |
| `2026-08-07 10:11:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.53.157[.]23` to AbuseIPDB if not already reported
- [ ] Block `34.53.157[.]23` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f10b7836591b

| Field | Detail |
|---|---|
| **Source IP** | `34.53.157[.]23` |
| **First Seen** | 2026-08-07 10:11 |
| **Last Seen** | 2026-08-07 10:11 |
| **Session Duration** | 32s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 10:11:13` | `cowrie.session.connect` |
| `2026-08-07 10:11:13` | `cowrie.login.success` |
| `2026-08-07 10:11:14` | `cowrie.session.params` |
| `2026-08-07 10:11:14` | `cowrie.command.input` |
| `2026-08-07 10:11:14` | `cowrie.command.failed` |
| `2026-08-07 10:11:46` | `cowrie.log.closed` |
| `2026-08-07 10:11:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.53.157[.]23` to AbuseIPDB if not already reported
- [ ] Block `34.53.157[.]23` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18224e04c522

| Field | Detail |
|---|---|
| **Source IP** | `34.53.157[.]23` |
| **First Seen** | 2026-08-07 10:11 |
| **Last Seen** | 2026-08-07 10:11 |
| **Session Duration** | 30s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 10:11:15` | `cowrie.session.connect` |
| `2026-08-07 10:11:15` | `cowrie.login.success` |
| `2026-08-07 10:11:16` | `cowrie.session.params` |
| `2026-08-07 10:11:16` | `cowrie.command.input` |
| `2026-08-07 10:11:46` | `cowrie.log.closed` |
| `2026-08-07 10:11:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.53.157[.]23` to AbuseIPDB if not already reported
- [ ] Block `34.53.157[.]23` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b798d7c80ff9

| Field | Detail |
|---|---|
| **Source IP** | `187.126.105[.]42` |
| **First Seen** | 2026-08-07 10:17 |
| **Last Seen** | 2026-08-07 10:17 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 10:17:39` | `cowrie.session.connect` |
| `2026-08-07 10:17:40` | `cowrie.client.version` |
| `2026-08-07 10:17:40` | `cowrie.client.kex` |
| `2026-08-07 10:17:42` | `cowrie.login.success` |
| `2026-08-07 10:17:43` | `cowrie.direct-tcpip.request` |
| `2026-08-07 10:17:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.126.105[.]42` to AbuseIPDB if not already reported
- [ ] Block `187.126.105[.]42` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-acb5e06e9db3

| Field | Detail |
|---|---|
| **Source IP** | `14.54.22[.]11` |
| **First Seen** | 2026-08-07 10:17 |
| **Last Seen** | 2026-08-07 10:18 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 10:17:53` | `cowrie.session.connect` |
| `2026-08-07 10:17:54` | `cowrie.client.version` |
| `2026-08-07 10:17:54` | `cowrie.client.kex` |
| `2026-08-07 10:17:56` | `cowrie.login.success` |
| `2026-08-07 10:17:57` | `cowrie.direct-tcpip.request` |
| `2026-08-07 10:18:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.54.22[.]11` to AbuseIPDB if not already reported
- [ ] Block `14.54.22[.]11` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6fcbe6c37a35

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-07 10:19 |
| **Last Seen** | 2026-08-07 10:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 10:19:10` | `cowrie.session.connect` |
| `2026-08-07 10:19:10` | `cowrie.client.version` |
| `2026-08-07 10:19:11` | `cowrie.client.kex` |
| `2026-08-07 10:19:11` | `cowrie.login.success` |
| `2026-08-07 10:19:11` | `cowrie.direct-tcpip.request` |
| `2026-08-07 10:19:11` | `cowrie.direct-tcpip.data` |
| `2026-08-07 10:19:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-391ba9471a68

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-07 10:20 |
| **Last Seen** | 2026-08-07 10:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 10:20:29` | `cowrie.session.connect` |
| `2026-08-07 10:20:29` | `cowrie.client.version` |
| `2026-08-07 10:20:29` | `cowrie.client.kex` |
| `2026-08-07 10:20:29` | `cowrie.login.success` |
| `2026-08-07 10:20:30` | `cowrie.session.params` |
| `2026-08-07 10:20:30` | `cowrie.command.input` |
| `2026-08-07 10:20:30` | `cowrie.log.closed` |
| `2026-08-07 10:20:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8bdcb7b86a56

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-07 10:22 |
| **Last Seen** | 2026-08-07 10:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 10:22:20` | `cowrie.session.connect` |
| `2026-08-07 10:22:20` | `cowrie.client.version` |
| `2026-08-07 10:22:21` | `cowrie.client.kex` |
| `2026-08-07 10:22:21` | `cowrie.login.success` |
| `2026-08-07 10:22:22` | `cowrie.session.params` |
| `2026-08-07 10:22:22` | `cowrie.command.input` |
| `2026-08-07 10:22:22` | `cowrie.log.closed` |
| `2026-08-07 10:22:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f77650e06f2

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-07 10:24 |
| **Last Seen** | 2026-08-07 10:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 10:24:22` | `cowrie.session.connect` |
| `2026-08-07 10:24:22` | `cowrie.client.version` |
| `2026-08-07 10:24:22` | `cowrie.client.kex` |
| `2026-08-07 10:24:23` | `cowrie.login.success` |
| `2026-08-07 10:24:24` | `cowrie.session.params` |
| `2026-08-07 10:24:24` | `cowrie.command.input` |
| `2026-08-07 10:24:24` | `cowrie.log.closed` |
| `2026-08-07 10:24:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-839f5d5e8e32

| Field | Detail |
|---|---|
| **Source IP** | `34.79.177[.]86` |
| **First Seen** | 2026-08-07 10:24 |
| **Last Seen** | 2026-08-07 10:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 10:24:24` | `cowrie.session.connect` |
| `2026-08-07 10:24:24` | `cowrie.login.success` |
| `2026-08-07 10:24:25` | `cowrie.session.params` |
| `2026-08-07 10:24:25` | `cowrie.command.input` |
| `2026-08-07 10:24:25` | `cowrie.command.input` |
| `2026-08-07 10:24:25` | `cowrie.command.failed` |
| `2026-08-07 10:24:25` | `cowrie.command.input` |
| `2026-08-07 10:24:25` | `cowrie.log.closed` |
| `2026-08-07 10:24:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.79.177[.]86` to AbuseIPDB if not already reported
- [ ] Block `34.79.177[.]86` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-387b5167ae17

| Field | Detail |
|---|---|
| **Source IP** | `34.79.177[.]86` |
| **First Seen** | 2026-08-07 10:24 |
| **Last Seen** | 2026-08-07 10:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 10:24:38` | `cowrie.session.connect` |
| `2026-08-07 10:24:38` | `cowrie.login.success` |
| `2026-08-07 10:24:38` | `cowrie.session.params` |
| `2026-08-07 10:24:38` | `cowrie.command.input` |
| `2026-08-07 10:24:38` | `cowrie.command.failed` |
| `2026-08-07 10:24:39` | `cowrie.log.closed` |
| `2026-08-07 10:24:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.79.177[.]86` to AbuseIPDB if not already reported
- [ ] Block `34.79.177[.]86` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-54e2bf8e05b4

| Field | Detail |
|---|---|
| **Source IP** | `34.79.177[.]86` |
| **First Seen** | 2026-08-07 10:24 |
| **Last Seen** | 2026-08-07 10:24 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 10:24:39` | `cowrie.session.connect` |
| `2026-08-07 10:24:39` | `cowrie.login.success` |
| `2026-08-07 10:24:40` | `cowrie.session.params` |
| `2026-08-07 10:24:40` | `cowrie.command.input` |
| `2026-08-07 10:24:51` | `cowrie.log.closed` |
| `2026-08-07 10:24:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.79.177[.]86` to AbuseIPDB if not already reported
- [ ] Block `34.79.177[.]86` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ab264d9d1bb

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-07 10:26 |
| **Last Seen** | 2026-08-07 10:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 10:26:14` | `cowrie.session.connect` |
| `2026-08-07 10:26:14` | `cowrie.client.version` |
| `2026-08-07 10:26:15` | `cowrie.client.kex` |
| `2026-08-07 10:26:15` | `cowrie.login.success` |
| `2026-08-07 10:26:16` | `cowrie.session.params` |
| `2026-08-07 10:26:16` | `cowrie.command.input` |
| `2026-08-07 10:26:16` | `cowrie.log.closed` |
| `2026-08-07 10:26:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-924f9d500470

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-07 10:28 |
| **Last Seen** | 2026-08-07 10:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 10:28:03` | `cowrie.session.connect` |
| `2026-08-07 10:28:03` | `cowrie.client.version` |
| `2026-08-07 10:28:03` | `cowrie.client.kex` |
| `2026-08-07 10:28:04` | `cowrie.login.success` |
| `2026-08-07 10:28:05` | `cowrie.session.params` |
| `2026-08-07 10:28:05` | `cowrie.command.input` |
| `2026-08-07 10:28:05` | `cowrie.log.closed` |
| `2026-08-07 10:28:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b0122b5dd91

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-07 10:29 |
| **Last Seen** | 2026-08-07 10:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 10:29:55` | `cowrie.session.connect` |
| `2026-08-07 10:29:55` | `cowrie.client.version` |
| `2026-08-07 10:29:55` | `cowrie.client.kex` |
| `2026-08-07 10:29:55` | `cowrie.login.success` |
| `2026-08-07 10:29:56` | `cowrie.session.params` |
| `2026-08-07 10:29:56` | `cowrie.command.input` |
| `2026-08-07 10:29:56` | `cowrie.log.closed` |
| `2026-08-07 10:29:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-669391b616c9

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-07 10:31 |
| **Last Seen** | 2026-08-07 10:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 10:31:46` | `cowrie.session.connect` |
| `2026-08-07 10:31:46` | `cowrie.client.version` |
| `2026-08-07 10:31:46` | `cowrie.client.kex` |
| `2026-08-07 10:31:46` | `cowrie.login.success` |
| `2026-08-07 10:31:47` | `cowrie.session.params` |
| `2026-08-07 10:31:47` | `cowrie.command.input` |
| `2026-08-07 10:31:47` | `cowrie.log.closed` |
| `2026-08-07 10:31:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e715b28656d

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-07 10:33 |
| **Last Seen** | 2026-08-07 10:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 10:33:33` | `cowrie.session.connect` |
| `2026-08-07 10:33:33` | `cowrie.client.version` |
| `2026-08-07 10:33:33` | `cowrie.client.kex` |
| `2026-08-07 10:33:34` | `cowrie.login.success` |
| `2026-08-07 10:33:35` | `cowrie.session.params` |
| `2026-08-07 10:33:35` | `cowrie.command.input` |
| `2026-08-07 10:33:35` | `cowrie.log.closed` |
| `2026-08-07 10:33:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0f5bbf46397

| Field | Detail |
|---|---|
| **Source IP** | `182.79.218[.]164` |
| **First Seen** | 2026-08-07 10:34 |
| **Last Seen** | 2026-08-07 10:34 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 10:34:33` | `cowrie.session.connect` |
| `2026-08-07 10:34:33` | `cowrie.client.version` |
| `2026-08-07 10:34:33` | `cowrie.client.kex` |
| `2026-08-07 10:34:35` | `cowrie.login.success` |
| `2026-08-07 10:34:36` | `cowrie.direct-tcpip.request` |
| `2026-08-07 10:34:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.79.218[.]164` to AbuseIPDB if not already reported
- [ ] Block `182.79.218[.]164` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a388e23dba48

| Field | Detail |
|---|---|
| **Source IP** | `221.10.221[.]104` |
| **First Seen** | 2026-08-07 10:34 |
| **Last Seen** | 2026-08-07 10:34 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 10:34:41` | `cowrie.session.connect` |
| `2026-08-07 10:34:42` | `cowrie.client.version` |
| `2026-08-07 10:34:42` | `cowrie.client.kex` |
| `2026-08-07 10:34:44` | `cowrie.login.success` |
| `2026-08-07 10:34:45` | `cowrie.direct-tcpip.request` |
| `2026-08-07 10:34:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `221.10.221[.]104` to AbuseIPDB if not already reported
- [ ] Block `221.10.221[.]104` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee7478bc168e

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-07 10:35 |
| **Last Seen** | 2026-08-07 10:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 10:35:27` | `cowrie.session.connect` |
| `2026-08-07 10:35:27` | `cowrie.client.version` |
| `2026-08-07 10:35:27` | `cowrie.client.kex` |
| `2026-08-07 10:35:27` | `cowrie.login.success` |
| `2026-08-07 10:35:28` | `cowrie.session.params` |
| `2026-08-07 10:35:28` | `cowrie.command.input` |
| `2026-08-07 10:35:28` | `cowrie.log.closed` |
| `2026-08-07 10:35:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b53bc577a9b

| Field | Detail |
|---|---|
| **Source IP** | `218.29.196[.]162` |
| **First Seen** | 2026-08-07 10:37 |
| **Last Seen** | 2026-08-07 10:37 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 10:37:06` | `cowrie.session.connect` |
| `2026-08-07 10:37:06` | `cowrie.client.version` |
| `2026-08-07 10:37:06` | `cowrie.client.kex` |
| `2026-08-07 10:37:08` | `cowrie.login.success` |
| `2026-08-07 10:37:09` | `cowrie.direct-tcpip.request` |
| `2026-08-07 10:37:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.29.196[.]162` to AbuseIPDB if not already reported
- [ ] Block `218.29.196[.]162` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aac6f9a17e65

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-07 10:37 |
| **Last Seen** | 2026-08-07 10:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 10:37:28` | `cowrie.session.connect` |
| `2026-08-07 10:37:28` | `cowrie.client.version` |
| `2026-08-07 10:37:28` | `cowrie.client.kex` |
| `2026-08-07 10:37:28` | `cowrie.login.success` |
| `2026-08-07 10:37:29` | `cowrie.session.params` |
| `2026-08-07 10:37:29` | `cowrie.command.input` |
| `2026-08-07 10:37:29` | `cowrie.log.closed` |
| `2026-08-07 10:37:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92fefe0dd481

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-07 10:39 |
| **Last Seen** | 2026-08-07 10:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 10:39:24` | `cowrie.session.connect` |
| `2026-08-07 10:39:24` | `cowrie.client.version` |
| `2026-08-07 10:39:24` | `cowrie.client.kex` |
| `2026-08-07 10:39:24` | `cowrie.login.success` |
| `2026-08-07 10:39:25` | `cowrie.session.params` |
| `2026-08-07 10:39:25` | `cowrie.command.input` |
| `2026-08-07 10:39:25` | `cowrie.log.closed` |
| `2026-08-07 10:39:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd9f4d56ff9e

| Field | Detail |
|---|---|
| **Source IP** | `213.33.204[.]130` |
| **First Seen** | 2026-08-07 10:40 |
| **Last Seen** | 2026-08-07 10:41 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 10:40:54` | `cowrie.session.connect` |
| `2026-08-07 10:40:55` | `cowrie.client.version` |
| `2026-08-07 10:40:55` | `cowrie.client.kex` |
| `2026-08-07 10:40:56` | `cowrie.login.success` |
| `2026-08-07 10:40:56` | `cowrie.direct-tcpip.request` |
| `2026-08-07 10:41:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.33.204[.]130` to AbuseIPDB if not already reported
- [ ] Block `213.33.204[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-13312ca2a3f2

| Field | Detail |
|---|---|
| **Source IP** | `218.202.143[.]68` |
| **First Seen** | 2026-08-07 10:41 |
| **Last Seen** | 2026-08-07 10:41 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 10:41:06` | `cowrie.session.connect` |
| `2026-08-07 10:41:07` | `cowrie.client.version` |
| `2026-08-07 10:41:07` | `cowrie.client.kex` |
| `2026-08-07 10:41:09` | `cowrie.login.success` |
| `2026-08-07 10:41:10` | `cowrie.direct-tcpip.request` |
| `2026-08-07 10:41:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.202.143[.]68` to AbuseIPDB if not already reported
- [ ] Block `218.202.143[.]68` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b70e75bec921

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-07 10:41 |
| **Last Seen** | 2026-08-07 10:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 10:41:18` | `cowrie.session.connect` |
| `2026-08-07 10:41:18` | `cowrie.client.version` |
| `2026-08-07 10:41:18` | `cowrie.client.kex` |
| `2026-08-07 10:41:18` | `cowrie.login.success` |
| `2026-08-07 10:41:19` | `cowrie.session.params` |
| `2026-08-07 10:41:19` | `cowrie.command.input` |
| `2026-08-07 10:41:19` | `cowrie.log.closed` |
| `2026-08-07 10:41:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ae42be47def

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-07 10:43 |
| **Last Seen** | 2026-08-07 10:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 10:43:12` | `cowrie.session.connect` |
| `2026-08-07 10:43:12` | `cowrie.client.version` |
| `2026-08-07 10:43:13` | `cowrie.client.kex` |
| `2026-08-07 10:43:13` | `cowrie.login.success` |
| `2026-08-07 10:43:14` | `cowrie.session.params` |
| `2026-08-07 10:43:14` | `cowrie.command.input` |
| `2026-08-07 10:43:14` | `cowrie.log.closed` |
| `2026-08-07 10:43:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e17c7ecea36

| Field | Detail |
|---|---|
| **Source IP** | `182.93.7[.]194` |
| **First Seen** | 2026-08-07 10:43 |
| **Last Seen** | 2026-08-07 10:43 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 10:43:19` | `cowrie.session.connect` |
| `2026-08-07 10:43:19` | `cowrie.client.version` |
| `2026-08-07 10:43:19` | `cowrie.client.kex` |
| `2026-08-07 10:43:20` | `cowrie.login.success` |
| `2026-08-07 10:43:21` | `cowrie.session.params` |
| `2026-08-07 10:43:21` | `cowrie.command.input` |
| `2026-08-07 10:43:21` | `cowrie.command.failed` |
| `2026-08-07 10:43:22` | `cowrie.log.closed` |
| `2026-08-07 10:43:23` | `cowrie.session.params` |
| `2026-08-07 10:43:23` | `cowrie.command.input` |
| `2026-08-07 10:43:23` | `cowrie.session.file_download` |
| `2026-08-07 10:43:23` | `cowrie.log.closed` |
| `2026-08-07 10:43:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.93.7[.]194` to AbuseIPDB if not already reported
- [ ] Block `182.93.7[.]194` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75d678c266c9

| Field | Detail |
|---|---|
| **Source IP** | `182.93.7[.]194` |
| **First Seen** | 2026-08-07 10:43 |
| **Last Seen** | 2026-08-07 10:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 10:43:23` | `cowrie.session.connect` |
| `2026-08-07 10:43:23` | `cowrie.client.version` |
| `2026-08-07 10:43:23` | `cowrie.client.kex` |
| `2026-08-07 10:43:24` | `cowrie.login.success` |
| `2026-08-07 10:43:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.93.7[.]194` to AbuseIPDB if not already reported
- [ ] Block `182.93.7[.]194` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9b78b6258ea

| Field | Detail |
|---|---|
| **Source IP** | `182.93.7[.]194` |
| **First Seen** | 2026-08-07 10:43 |
| **Last Seen** | 2026-08-07 10:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 10:43:25` | `cowrie.session.connect` |
| `2026-08-07 10:43:25` | `cowrie.client.version` |
| `2026-08-07 10:43:25` | `cowrie.client.kex` |
| `2026-08-07 10:43:26` | `cowrie.login.success` |
| `2026-08-07 10:43:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.93.7[.]194` to AbuseIPDB if not already reported
- [ ] Block `182.93.7[.]194` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-246091caf64e

| Field | Detail |
|---|---|
| **Source IP** | `222.186.68[.]153` |
| **First Seen** | 2026-08-07 10:44 |
| **Last Seen** | 2026-08-07 10:44 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 10:44:15` | `cowrie.session.connect` |
| `2026-08-07 10:44:16` | `cowrie.client.version` |
| `2026-08-07 10:44:16` | `cowrie.client.kex` |
| `2026-08-07 10:44:19` | `cowrie.login.success` |
| `2026-08-07 10:44:20` | `cowrie.direct-tcpip.request` |
| `2026-08-07 10:44:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.186.68[.]153` to AbuseIPDB if not already reported
- [ ] Block `222.186.68[.]153` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25dc801982a8

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-07 10:45 |
| **Last Seen** | 2026-08-07 10:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 10:45:04` | `cowrie.session.connect` |
| `2026-08-07 10:45:04` | `cowrie.client.version` |
| `2026-08-07 10:45:04` | `cowrie.client.kex` |
| `2026-08-07 10:45:04` | `cowrie.login.success` |
| `2026-08-07 10:45:05` | `cowrie.session.params` |
| `2026-08-07 10:45:05` | `cowrie.command.input` |
| `2026-08-07 10:45:05` | `cowrie.log.closed` |
| `2026-08-07 10:45:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-101234071cce

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-07 10:46 |
| **Last Seen** | 2026-08-07 10:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 10:46:52` | `cowrie.session.connect` |
| `2026-08-07 10:46:52` | `cowrie.client.version` |
| `2026-08-07 10:46:53` | `cowrie.client.kex` |
| `2026-08-07 10:46:53` | `cowrie.login.success` |
| `2026-08-07 10:46:54` | `cowrie.session.params` |
| `2026-08-07 10:46:54` | `cowrie.command.input` |
| `2026-08-07 10:46:54` | `cowrie.log.closed` |
| `2026-08-07 10:46:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6c43f5d7773

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-07 10:48 |
| **Last Seen** | 2026-08-07 10:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 10:48:46` | `cowrie.session.connect` |
| `2026-08-07 10:48:46` | `cowrie.client.version` |
| `2026-08-07 10:48:46` | `cowrie.client.kex` |
| `2026-08-07 10:48:47` | `cowrie.login.success` |
| `2026-08-07 10:48:48` | `cowrie.session.params` |
| `2026-08-07 10:48:48` | `cowrie.command.input` |
| `2026-08-07 10:48:48` | `cowrie.log.closed` |
| `2026-08-07 10:48:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7cd60b2e98fd

| Field | Detail |
|---|---|
| **Source IP** | `34.62.77[.]102` |
| **First Seen** | 2026-08-07 10:49 |
| **Last Seen** | 2026-08-07 10:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 10:49:52` | `cowrie.session.connect` |
| `2026-08-07 10:49:52` | `cowrie.login.success` |
| `2026-08-07 10:49:53` | `cowrie.session.params` |
| `2026-08-07 10:49:53` | `cowrie.command.input` |
| `2026-08-07 10:49:53` | `cowrie.command.input` |
| `2026-08-07 10:49:53` | `cowrie.command.failed` |
| `2026-08-07 10:49:53` | `cowrie.command.input` |
| `2026-08-07 10:49:53` | `cowrie.log.closed` |
| `2026-08-07 10:49:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.62.77[.]102` to AbuseIPDB if not already reported
- [ ] Block `34.62.77[.]102` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe22bda9d858

| Field | Detail |
|---|---|
| **Source IP** | `34.62.77[.]102` |
| **First Seen** | 2026-08-07 10:50 |
| **Last Seen** | 2026-08-07 10:50 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 10:50:06` | `cowrie.session.connect` |
| `2026-08-07 10:50:06` | `cowrie.login.success` |
| `2026-08-07 10:50:06` | `cowrie.session.params` |
| `2026-08-07 10:50:06` | `cowrie.command.input` |
| `2026-08-07 10:50:06` | `cowrie.command.failed` |
| `2026-08-07 10:50:19` | `cowrie.log.closed` |
| `2026-08-07 10:50:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.62.77[.]102` to AbuseIPDB if not already reported
- [ ] Block `34.62.77[.]102` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f68c8780ecb4

| Field | Detail |
|---|---|
| **Source IP** | `34.62.77[.]102` |
| **First Seen** | 2026-08-07 10:50 |
| **Last Seen** | 2026-08-07 10:50 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 10:50:08` | `cowrie.session.connect` |
| `2026-08-07 10:50:08` | `cowrie.login.success` |
| `2026-08-07 10:50:08` | `cowrie.session.params` |
| `2026-08-07 10:50:08` | `cowrie.command.input` |
| `2026-08-07 10:50:19` | `cowrie.log.closed` |
| `2026-08-07 10:50:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.62.77[.]102` to AbuseIPDB if not already reported
- [ ] Block `34.62.77[.]102` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-669264e4843a

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-07 10:50 |
| **Last Seen** | 2026-08-07 10:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 10:50:43` | `cowrie.session.connect` |
| `2026-08-07 10:50:43` | `cowrie.client.version` |
| `2026-08-07 10:50:43` | `cowrie.client.kex` |
| `2026-08-07 10:50:44` | `cowrie.login.success` |
| `2026-08-07 10:50:45` | `cowrie.session.params` |
| `2026-08-07 10:50:45` | `cowrie.command.input` |
| `2026-08-07 10:50:45` | `cowrie.log.closed` |
| `2026-08-07 10:50:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f6d74402669

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-07 10:52 |
| **Last Seen** | 2026-08-07 10:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 10:52:35` | `cowrie.session.connect` |
| `2026-08-07 10:52:35` | `cowrie.client.version` |
| `2026-08-07 10:52:35` | `cowrie.client.kex` |
| `2026-08-07 10:52:35` | `cowrie.login.success` |
| `2026-08-07 10:52:36` | `cowrie.session.params` |
| `2026-08-07 10:52:36` | `cowrie.command.input` |
| `2026-08-07 10:52:36` | `cowrie.log.closed` |
| `2026-08-07 10:52:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37293475d0e3

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-07 10:54 |
| **Last Seen** | 2026-08-07 10:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 10:54:15` | `cowrie.session.connect` |
| `2026-08-07 10:54:15` | `cowrie.client.version` |
| `2026-08-07 10:54:16` | `cowrie.client.kex` |
| `2026-08-07 10:54:16` | `cowrie.login.success` |
| `2026-08-07 10:54:17` | `cowrie.session.params` |
| `2026-08-07 10:54:17` | `cowrie.command.input` |
| `2026-08-07 10:54:17` | `cowrie.log.closed` |
| `2026-08-07 10:54:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `164.92.115[.]22` | **168** | 2026-08-07 08:56 | 2026-08-07 10:54 | 108m | 0 | `T1592` | 🟠 MEDIUM |
| `34.53.157[.]23` | **30** | 2026-08-07 10:10 | 2026-08-07 10:11 | 15m | 0 | `T1592` | 🟠 MEDIUM |
| `34.62.77[.]102` | **30** | 2026-08-07 10:49 | 2026-08-07 10:50 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `34.79.177[.]86` | **30** | 2026-08-07 10:24 | 2026-08-07 10:24 | 2m | 0 | `T1592` | 🟠 MEDIUM |
| `139.199.80[.]137` | **4** | 2026-08-07 09:13 | 2026-08-07 10:32 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]164` | **3** | 2026-08-07 10:07 | 2026-08-07 10:07 | 0m | 0 | `T1592` | 🟢 LOW |
| `88.214.25[.]121` | **3** | 2026-08-07 09:33 | 2026-08-07 09:33 | 0m | 0 | `T1592` | 🟢 LOW |
| `91.233.83[.]203` | **2** | 2026-08-07 10:03 | 2026-08-07 10:03 | 1m | 0 | `T1592` | 🟢 LOW |
| `101.126.157[.]138` | 1 | 2026-08-07 09:51 | 2026-08-07 09:53 | 120s | 0 | `T1592` | 🟢 LOW |
| `101.126.69[.]201` | 1 | 2026-08-07 10:22 | 2026-08-07 10:24 | 120s | 0 | `T1592` | 🟢 LOW |
| `109.87.152[.]240` | 1 | 2026-08-07 10:04 | 2026-08-07 10:04 | 11s | 0 | `T1592` | 🟢 LOW |
| `110.173.190[.]222` | 1 | 2026-08-07 09:03 | 2026-08-07 09:03 | 4s | 0 | `T1592` | 🟢 LOW |
| `116.181.10[.]84` | 1 | 2026-08-07 08:55 | 2026-08-07 08:57 | 120s | 0 | `T1592` | 🟢 LOW |
| `144.202.92[.]17` | 1 | 2026-08-07 10:42 | 2026-08-07 10:42 | 0s | 0 | `T1592` | 🟢 LOW |
| `156.238.86[.]2` | 1 | 2026-08-07 10:00 | 2026-08-07 10:00 | 10s | 0 | `T1592` | 🟢 LOW |
| `177.84.17[.]244` | 1 | 2026-08-07 10:06 | 2026-08-07 10:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `178.159.126[.]102` | 1 | 2026-08-07 10:54 | 2026-08-07 10:54 | 12s | 0 | `T1592` | 🟢 LOW |
| `180.76.243[.]197` | 1 | 2026-08-07 10:43 | 2026-08-07 10:45 | 120s | 0 | `T1592` | 🟢 LOW |
| `181.188.32[.]236` | 1 | 2026-08-07 09:02 | 2026-08-07 09:03 | 12s | 0 | `T1592` | 🟢 LOW |
| `194.187.176[.]39` | 1 | 2026-08-07 10:26 | 2026-08-07 10:26 | 0s | 0 | `T1592` | 🟢 LOW |
| `195.95.147[.]49` | 1 | 2026-08-07 10:27 | 2026-08-07 10:27 | 11s | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]238` | 1 | 2026-08-07 10:18 | 2026-08-07 10:18 | 0s | 0 | `T1592` | 🟢 LOW |
| `200.160.95[.]188` | 1 | 2026-08-07 10:23 | 2026-08-07 10:23 | 10s | 0 | `T1592` | 🟢 LOW |
| `212.8.242[.]38` | 1 | 2026-08-07 08:56 | 2026-08-07 08:57 | 31s | 0 | `T1592` | 🟢 LOW |
| `31.77.227[.]120` | 1 | 2026-08-07 09:12 | 2026-08-07 09:12 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]147` | 1 | 2026-08-07 10:04 | 2026-08-07 10:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.33.109[.]8` | 1 | 2026-08-07 09:35 | 2026-08-07 09:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.71.57[.]10` | 1 | 2026-08-07 09:14 | 2026-08-07 09:14 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.124.153[.]59` | 1 | 2026-08-07 10:21 | 2026-08-07 10:21 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]198` | 1 | 2026-08-07 09:09 | 2026-08-07 09:09 | 16s | 0 | `T1592` | 🟢 LOW |
| `66.228.62[.]150` | 1 | 2026-08-07 09:35 | 2026-08-07 09:35 | 1s | 0 | `T1592` | 🟢 LOW |
| `83.255.209[.]245` | 1 | 2026-08-07 09:11 | 2026-08-07 09:13 | 120s | 0 | `T1592` | 🟢 LOW |
| `91.203.63[.]168` | 1 | 2026-08-07 09:54 | 2026-08-07 09:54 | 13s | 0 | `T1592` | 🟢 LOW |
| `95.46.142[.]71` | 1 | 2026-08-07 09:46 | 2026-08-07 09:46 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 87/100 | 🔴 HIGH | **42/74** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 82/100 | 🔴 HIGH | **30/75** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 44/100 | 🟡 MEDIUM | **34/72** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 70/100 | 🔴 HIGH | **26/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 50/100 | 🟡 MEDIUM | **27/74** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
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
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `287962211de7bcadb39f7576732438b43ee6aab420ec23c29a9d12a8151a547f` | ELF Binary (Linux executable) (x86 32-bit) | `287962211de7bcad...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `2f206563640dd66a743ffd493ce0e3c31a8fc5a24b9f5d2b540fc22d45c13d66` | ELF Binary (Linux executable) (x86 32-bit) | `2f206563640dd66a...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `31d4181843b1ed10a7e7cb3f108f6d6c50a7a4452ee52ddacabe8ca77260615e` | Bash Script | `31d4181843b1ed10...` | 60/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |

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

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `34.53.157[.]23` | BE | Google LLC | **100** ⚠️ | 1 |
| `45.71.57[.]10` | AR | Red Intercable Digital S.A. | **100** ⚠️ | 0 |
| `95.46.142[.]71` | UA | Multisystem Technologies Ltd. | **100** ⚠️ | 0 |
| `156.238.86[.]2` | PK | SB Link Network Private Limited | **100** ⚠️ | 50 |
| `218.29.196[.]162` | CN | China Unicom Henan province network | **100** ⚠️ | 50 |
| `195.95.147[.]49` | UA | Branch Enterprise Netgroup-Service | **100** ⚠️ | 2 |
| `213.33.204[.]130` | RU | Interface networks - Msk. | **100** ⚠️ | 50 |
| `80.233.77[.]136` | IE | Three Ireland (Hutchison) limited | **100** ⚠️ | 50 |
| `31.77.227[.]120` | US | ROCKET & MARINICA LTD | **100** ⚠️ | 30 |
| `122.176.45[.]238` | IN | BHARTI TELENET LTD. NEW DELHI | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 154 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 151 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 3 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 3 |

---

## 🔕 False Positive Summary (32 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 6 |
| AbuseIPDB score 17 below threshold 25 | 6 |
| AbuseIPDB score 24 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 18 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 479 cases |
| Tool 34  | Credential Extractor        | ✅ 175 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 14 fingerprints |
| Tool 36  | Command Clustering          | ✅ 6 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 92 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 32 filtered (6.7%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 67 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 22 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 151 priority case(s) shown individually · 34 recon entry/entries in table (8 group(s) consolidating 270 session(s)).

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
_Report time: 2026-08-07T10:57:13Z_

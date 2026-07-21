# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-21 |
| **Generated At** | 2026-07-21T17:26:55Z |
| **Shift Time** | 17:26 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **281** |
| Confirmed Threats | **245** |
| False Positives Filtered | **36** (12.8%) |
| Unique Attacker IPs | **158** |
| Countries of Origin | **38** |
| High Severity Cases | **139** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **142** |
| Malware Samples Analyzed | **2** HIGH · **31** MED · 12 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **206** |
| Unique Credential Pairs | **72** |
| Unique Usernames | **29** |
| Unique Passwords | **63** |
| Successful Auth Pairs | **150** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `support` | 37 |
| `root` | 30 |
| `admin` | 17 |
| `debian` | 15 |
| `default` | 9 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `support` | 30 |
| `` | 10 |
| `debian555` | 6 |
| `1111` | 6 |
| `777777` | 5 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `support` | `support` | 30 |
| `admin` | `` | 8 |
| `debian` | `debian555` | 6 |
| `operator` | `12345678` | 5 |
| `ubnt` | `44444` | 5 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `unknown` | `unknown2003` | `103.230.176.152` | 2026-07-21T12:57:28 |
| `unknown` | `unknown2003` | `202.138.229.190` | 2026-07-21T12:57:41 |
| `unknown` | `unknown2003` | `10.0.0.73` | 2026-07-21T13:01:05 |
| `support` | `support` | `176.53.159.196` | 2026-07-21T13:01:21 |
| `default` | `00000` | `95.79.57.221` | 2026-07-21T13:01:36 |
| `support` | `support` | `10.0.0.73` | 2026-07-21T13:01:37 |
| `default` | `00000` | `111.70.9.143` | 2026-07-21T13:01:44 |
| `testing` | `t3st1ng` | `10.0.0.73` | 2026-07-21T13:02:22 |
| `pi` | `pi` | `46.29.26.195` | 2026-07-21T13:03:06 |
| `windows` | `password` | `102.208.217.175` | 2026-07-21T13:03:19 |
| `345gs5662d34` | `345gs5662d34` | `102.208.217.175` | 2026-07-21T13:03:23 |
| `windows` | `3245gs5662d34` | `102.208.217.175` | 2026-07-21T13:03:25 |
| `testing` | `t3st1ng` | `185.242.3.195` | 2026-07-21T13:03:40 |
| `pi` | `P@ssw0rd` | `41.220.3.101` | 2026-07-21T13:08:18 |
| `pi` | `P@ssw0rd` | `10.0.0.73` | 2026-07-21T13:08:43 |
| `janice` | `janice` | `185.242.3.195` | 2026-07-21T13:10:58 |
| `mysql` | `administrator` | `218.206.136.24` | 2026-07-21T13:14:10 |
| `mysql` | `administrator` | `103.68.22.115` | 2026-07-21T13:17:36 |
| `root` | `` | `94.154.43.164` | 2026-07-21T13:22:21 |
| `config` | `config123456` | `65.181.79.60` | 2026-07-21T13:24:27 |
| `pi` | `raspberry` | `217.250.203.81` | 2026-07-21T13:24:39 |
| `pi` | `raspberryraspberry993311` | `217.250.203.81` | 2026-07-21T13:24:39 |
| `config` | `config123456` | `10.0.0.73` | 2026-07-21T13:24:48 |
| `debian` | `debian555` | `218.146.255.221` | 2026-07-21T13:26:35 |
| `debian` | `debian555` | `65.20.191.231` | 2026-07-21T13:26:48 |
| `user` | `22` | `191.36.152.28` | 2026-07-21T13:29:49 |
| `debian` | `debian555` | `211.53.58.10` | 2026-07-21T13:29:53 |
| `debian` | `debian555` | `117.250.19.91` | 2026-07-21T13:30:08 |
| `debian` | `debian555` | `10.0.0.73` | 2026-07-21T13:30:16 |
| `user` | `22` | `188.168.86.6` | 2026-07-21T13:32:59 |
| `guest` | `777777` | `49.206.194.29` | 2026-07-21T13:39:00 |
| `nobody` | `nobody2012` | `85.105.255.56` | 2026-07-21T13:47:46 |
| `nobody` | `nobody2012` | `203.193.147.75` | 2026-07-21T13:47:56 |
| `support` | `8` | `196.190.180.18` | 2026-07-21T13:51:17 |
| `support` | `8` | `180.76.52.146` | 2026-07-21T13:51:25 |
| `root` | `---fuck_you----` | `111.36.57.69` | 2026-07-21T13:52:51 |
| `janice` | `janice` | `10.0.0.73` | 2026-07-21T13:53:42 |
| `support` | `8` | `65.20.179.251` | 2026-07-21T13:54:47 |
| `support` | `8` | `10.0.0.73` | 2026-07-21T13:55:17 |
| `operator` | `operator2023` | `61.185.30.170` | 2026-07-21T13:57:58 |
| `operator` | `operator2023` | `196.188.93.169` | 2026-07-21T13:58:11 |
| `g` | `123456` | `185.242.3.195` | 2026-07-21T14:02:20 |
| `mongouser` | `mongouser` | `14.103.117.142` | 2026-07-21T14:04:23 |
| `ubnt` | `ubnt333` | `10.0.0.73` | 2026-07-21T14:07:39 |
| `operator` | `12345678` | `210.4.68.73` | 2026-07-21T14:08:08 |
| `operator` | `12345678` | `24.207.66.154` | 2026-07-21T14:11:23 |
| `operator` | `12345678` | `103.147.248.23` | 2026-07-21T14:11:32 |
| `operator` | `12345678` | `10.0.0.73` | 2026-07-21T14:11:45 |
| `root` | `qwerty.123` | `14.103.117.142` | 2026-07-21T14:13:48 |
| `debian` | `00` | `191.36.154.175` | 2026-07-21T14:16:24 |
| `debian` | `00` | `10.0.0.73` | 2026-07-21T14:20:08 |
| `blank` | `77777` | `10.0.0.73` | 2026-07-21T14:23:04 |
| `root` | `admin000` | `14.103.117.142` | 2026-07-21T14:28:01 |
| `test` | `test2014` | `60.174.39.82` | 2026-07-21T14:31:48 |
| `test` | `test2014` | `196.189.126.10` | 2026-07-21T14:31:56 |
| `default` | `4444` | `10.0.0.73` | 2026-07-21T14:32:34 |
| `test` | `test2014` | `10.0.0.73` | 2026-07-21T14:35:25 |
| `ubnt` | `44444` | `122.160.15.31` | 2026-07-21T14:41:11 |
| `ubnt` | `44444` | `196.188.93.169` | 2026-07-21T14:41:19 |
| `test` | `22222` | `150.228.187.139` | 2026-07-21T14:44:19 |
| `test` | `22222` | `188.36.7.196` | 2026-07-21T14:44:27 |
| `ubnt` | `44444` | `186.239.41.74` | 2026-07-21T14:44:41 |
| `ubnt` | `44444` | `178.216.165.187` | 2026-07-21T14:44:48 |
| `ubnt` | `44444` | `10.0.0.73` | 2026-07-21T14:45:05 |
| `g` | `123456` | `10.0.0.73` | 2026-07-21T14:45:13 |
| `root` | `123@@@` | `129.153.145.135` | 2026-07-21T14:48:07 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-07-21T14:48:07 |
| `test` | `22222` | `10.0.0.73` | 2026-07-21T14:48:09 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-07-21T14:48:15 |
| `jennifer` | `jennifer` | `185.242.3.195` | 2026-07-21T14:53:45 |
| `debian` | `debian2006` | `219.128.15.190` | 2026-07-21T14:55:20 |
| `debian` | `debian2006` | `119.247.187.188` | 2026-07-21T14:55:33 |
| `nobody` | `222222` | `10.0.0.73` | 2026-07-21T14:57:29 |
| `debian` | `debian2006` | `27.107.102.154` | 2026-07-21T14:58:28 |
| `debian` | `debian2006` | `10.0.0.73` | 2026-07-21T14:58:46 |
| `root` | `123@@@` | `144.22.238.238` | 2026-07-21T15:05:31 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-07-21T15:05:33 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-07-21T15:05:38 |
| `nobody` | `333` | `177.159.150.111` | 2026-07-21T15:06:15 |
| `nobody` | `333` | `118.183.180.108` | 2026-07-21T15:06:28 |
| `admin` | `admin` | `204.152.195.212` | 2026-07-21T15:07:54 |
| `admin` | `admin` | `130.12.180.51` | 2026-07-21T15:07:55 |
| `frappe` | `frappe12345` | `14.103.117.142` | 2026-07-21T15:10:25 |
| `centos` | `1111111` | `117.2.123.19` | 2026-07-21T15:12:25 |
| `centos` | `1111111` | `60.166.8.174` | 2026-07-21T15:12:34 |
| `config` | `config999` | `81.22.51.64` | 2026-07-21T15:18:22 |
| `config` | `config999` | `78.187.9.111` | 2026-07-21T15:18:28 |
| `default` | `qwerty1234` | `59.93.36.136` | 2026-07-21T15:18:51 |
| `root` | `1225` | `112.197.2.116` | 2026-07-21T15:20:27 |
| `default` | `qwerty1234` | `218.4.156.254` | 2026-07-21T15:22:04 |
| `config` | `config999` | `10.0.0.73` | 2026-07-21T15:22:05 |
| `default` | `qwerty1234` | `200.89.159.59` | 2026-07-21T15:22:13 |
| `default` | `2` | `187.218.57.50` | 2026-07-21T15:30:58 |
| `default` | `2` | `178.178.222.60` | 2026-07-21T15:31:05 |
| `guest` | `8888` | `183.89.208.174` | 2026-07-21T15:34:02 |
| `guest` | `8888` | `61.12.84.172` | 2026-07-21T15:34:11 |
| `default` | `2` | `10.0.0.73` | 2026-07-21T15:34:59 |
| `sonarqube` | `sonarqube@2025` | `173.249.52.138` | 2026-07-21T15:36:06 |
| `345gs5662d34` | `345gs5662d34` | `173.249.52.138` | 2026-07-21T15:36:08 |
| `sonarqube` | `3245gs5662d34` | `173.249.52.138` | 2026-07-21T15:36:09 |
| `jennifer` | `jennifer` | `10.0.0.73` | 2026-07-21T15:36:35 |
| `guest` | `8888` | `10.0.0.73` | 2026-07-21T15:37:51 |
| `root` | `` | `94.154.43.91` | 2026-07-21T15:42:06 |
| `nexus` | `admin` | `117.50.213.249` | 2026-07-21T15:42:24 |
| `admin` | `888` | `95.35.29.192` | 2026-07-21T15:43:12 |
| `root` | `QWERTYasdfgh` | `185.242.3.195` | 2026-07-21T15:45:20 |
| `unknown` | `root` | `80.65.90.155` | 2026-07-21T15:45:34 |
| `unknown` | `root` | `219.144.16.16` | 2026-07-21T15:45:47 |
| `unknown` | `root` | `10.0.0.73` | 2026-07-21T15:46:02 |
| `admin` | `888` | `114.98.63.18` | 2026-07-21T15:46:48 |
| `admin` | `888` | `10.0.0.73` | 2026-07-21T15:47:03 |
| `root` | `root33` | `136.56.34.147` | 2026-07-21T15:56:00 |
| `root` | `root33` | `49.124.151.15` | 2026-07-21T15:56:13 |
| `root` | `root33` | `179.185.227.77` | 2026-07-21T15:59:17 |
| `root` | `root33` | `10.0.0.73` | 2026-07-21T15:59:47 |
| `config` | `999999` | `50.217.40.11` | 2026-07-21T16:02:13 |
| `config` | `999999` | `146.190.215.195` | 2026-07-21T16:02:19 |
| `root` | `ubuntu` | `185.113.9.199` | 2026-07-21T16:05:45 |
| `blank` | `blank2001` | `14.54.22.11` | 2026-07-21T16:05:46 |
| `blank` | `blank2001` | `81.195.152.14` | 2026-07-21T16:05:54 |
| `admin` | `33` | `185.40.122.250` | 2026-07-21T16:08:17 |
| `blank` | `blank2001` | `116.113.241.82` | 2026-07-21T16:08:56 |
| `blank` | `blank2001` | `85.19.195.12` | 2026-07-21T16:09:04 |
| `blank` | `blank2001` | `10.0.0.73` | 2026-07-21T16:09:18 |
| `admin` | `33` | `10.0.0.73` | 2026-07-21T16:11:44 |
| `mysql` | `0987654321` | `212.68.38.69` | 2026-07-21T16:24:14 |
| `mysql` | `0987654321` | `218.13.214.18` | 2026-07-21T16:24:27 |
| `mysql` | `0987654321` | `10.0.0.73` | 2026-07-21T16:24:42 |
| `root` | `QWERTYasdfgh` | `10.0.0.73` | 2026-07-21T16:28:48 |
| `debian` | `debian2025` | `103.68.22.115` | 2026-07-21T16:28:59 |
| `debian` | `debian2025` | `10.0.0.73` | 2026-07-21T16:32:38 |
| `support` | `1111` | `123.52.202.92` | 2026-07-21T16:32:49 |
| `support` | `1111` | `203.252.10.4` | 2026-07-21T16:32:58 |
| `production` | `123456` | `198.98.56.227` | 2026-07-21T16:34:27 |
| `345gs5662d34` | `345gs5662d34` | `198.98.56.227` | 2026-07-21T16:34:29 |
| `production` | `3245gs5662d34` | `198.98.56.227` | 2026-07-21T16:34:29 |
| `support` | `1111` | `124.133.10.66` | 2026-07-21T16:36:12 |
| `admin` | `admin` | `94.154.43.60` | 2026-07-21T16:37:17 |
| `ubuntu` | `user1234567` | `185.242.3.195` | 2026-07-21T16:37:28 |
| `root` | `LeitboGi0ro` | `165.1.75.106` | 2026-07-21T16:40:22 |
| `root` | `123@@@` | `165.1.75.106` | 2026-07-21T16:40:24 |
| `root` | `Password09!` | `94.183.188.148` | 2026-07-21T16:40:52 |
| `345gs5662d34` | `345gs5662d34` | `94.183.188.148` | 2026-07-21T16:41:00 |
| `root` | `3245gs5662d34` | `94.183.188.148` | 2026-07-21T16:41:05 |
| `user` | `1111` | `218.29.231.106` | 2026-07-21T16:45:38 |
| `user` | `1111` | `101.13.5.49` | 2026-07-21T16:45:54 |
| `user` | `777777` | `71.229.1.186` | 2026-07-21T16:48:26 |
| `user` | `777777` | `150.228.187.139` | 2026-07-21T16:48:39 |
| `user` | `1111` | `10.0.0.73` | 2026-07-21T16:49:15 |
| `user` | `777777` | `10.0.0.73` | 2026-07-21T16:52:06 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **281** |
| Sessions with Fingerprint | **20** |
| Unique HASSH Fingerprints | **20** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| OpenSSH | 84 |
| libssh | 57 |
| Go SSH scanner | 40 |
| Paramiko (Python) | 12 |
| PuTTY | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 77 | 73 |
| `f555226df196...` | Mirai/variant | 36 | 7 |
| `eff4c24daffc...` | Modern SSH client | 15 | 1 |
| `16443846184e...` | Generic scanner | 12 | 3 |
| `a2de0f306611...` | Mirai/variant | 12 | 3 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 77 | 73 | Mirai/variant |
| `f555226df196...` | libssh | 36 | 7 | Mirai/variant |
| `95420f9d932d...` | libssh | 18 | 4 | — |
| `eff4c24daffc...` | Go SSH scanner | 15 | 1 | Modern SSH client |
| `16443846184e...` | Go SSH scanner | 12 | 3 | Generic scanner |
| `a2de0f306611...` | Paramiko (Python) | 12 | 3 | Mirai/variant |
| `a984ff804585...` | OpenSSH | 5 | 1 | libssh-based |
| `f1e5e9d24e5e...` | Go SSH scanner | 4 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **6** |
| Campaign Clusters | **3** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Mirai/IoT Botnet** | 🔴 HIGH | 2 | 2 | `T1082, T1105, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 4 | 4 | `T1021.004, T1078, T1070, T1140` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1070, T1140` |

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
Source IPs: `94.154.43.164`, `94.154.43.91`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `94.183.188.148`, `173.249.52.138`, `198.98.56.227`, `102.208.217.175`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `14.103.117.142`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **158** |
| Unique ASNs | **94** |
| High-Risk ASNs | **84** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS22773` | Cox Communications Inc. | 15 | MEDIUM |
| `AS4134` | CHINANET BACKBONE | 12 | HIGH |
| `AS46562` | Performive LLC | 10 | MEDIUM |
| `AS4837` | CHINA UNICOM China169 Backbone | 5 | HIGH |
| `AS63949` | Akamai Connected Cloud | 4 | HIGH |
| `AS398324` | Censys, Inc. | 4 | HIGH |
| `AS24757` | Ethio Telecom | 3 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 3 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (137)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-d51ba5b4b47f

| Field | Detail |
|---|---|
| **Source IP** | `103.230.176[.]152` |
| **First Seen** | 2026-07-21 12:57 |
| **Last Seen** | 2026-07-21 12:57 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 12:57:25` | `cowrie.session.connect` |
| `2026-07-21 12:57:25` | `cowrie.client.version` |
| `2026-07-21 12:57:25` | `cowrie.client.kex` |
| `2026-07-21 12:57:28` | `cowrie.login.success` |
| `2026-07-21 12:57:28` | `cowrie.direct-tcpip.request` |
| `2026-07-21 12:57:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.230.176[.]152` to AbuseIPDB if not already reported
- [ ] Block `103.230.176[.]152` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f0621ac9f87

| Field | Detail |
|---|---|
| **Source IP** | `202.138.229[.]190` |
| **First Seen** | 2026-07-21 12:57 |
| **Last Seen** | 2026-07-21 12:57 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 12:57:38` | `cowrie.session.connect` |
| `2026-07-21 12:57:38` | `cowrie.client.version` |
| `2026-07-21 12:57:38` | `cowrie.client.kex` |
| `2026-07-21 12:57:41` | `cowrie.login.success` |
| `2026-07-21 12:57:41` | `cowrie.direct-tcpip.request` |
| `2026-07-21 12:57:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.138.229[.]190` to AbuseIPDB if not already reported
- [ ] Block `202.138.229[.]190` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e8b938c659b

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-21 13:01 |
| **Last Seen** | 2026-07-21 13:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 13:01:21` | `cowrie.session.connect` |
| `2026-07-21 13:01:21` | `cowrie.client.version` |
| `2026-07-21 13:01:21` | `cowrie.client.kex` |
| `2026-07-21 13:01:21` | `cowrie.login.success` |
| `2026-07-21 13:01:22` | `cowrie.direct-tcpip.request` |
| `2026-07-21 13:01:22` | `cowrie.direct-tcpip.data` |
| `2026-07-21 13:01:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11558160020b

| Field | Detail |
|---|---|
| **Source IP** | `95.79.57[.]221` |
| **First Seen** | 2026-07-21 13:01 |
| **Last Seen** | 2026-07-21 13:01 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 13:01:35` | `cowrie.session.connect` |
| `2026-07-21 13:01:35` | `cowrie.client.version` |
| `2026-07-21 13:01:35` | `cowrie.client.kex` |
| `2026-07-21 13:01:36` | `cowrie.login.success` |
| `2026-07-21 13:01:36` | `cowrie.direct-tcpip.request` |
| `2026-07-21 13:01:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.79.57[.]221` to AbuseIPDB if not already reported
- [ ] Block `95.79.57[.]221` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55dae62c1cdb

| Field | Detail |
|---|---|
| **Source IP** | `111.70.9[.]143` |
| **First Seen** | 2026-07-21 13:01 |
| **Last Seen** | 2026-07-21 13:01 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 13:01:42` | `cowrie.session.connect` |
| `2026-07-21 13:01:42` | `cowrie.client.version` |
| `2026-07-21 13:01:42` | `cowrie.client.kex` |
| `2026-07-21 13:01:44` | `cowrie.login.success` |
| `2026-07-21 13:01:45` | `cowrie.direct-tcpip.request` |
| `2026-07-21 13:01:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.9[.]143` to AbuseIPDB if not already reported
- [ ] Block `111.70.9[.]143` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c20ff672113

| Field | Detail |
|---|---|
| **Source IP** | `46.29.26[.]195` |
| **First Seen** | 2026-07-21 13:03 |
| **Last Seen** | 2026-07-21 13:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 13:03:05` | `cowrie.session.connect` |
| `2026-07-21 13:03:05` | `cowrie.client.version` |
| `2026-07-21 13:03:05` | `cowrie.client.kex` |
| `2026-07-21 13:03:06` | `cowrie.login.success` |
| `2026-07-21 13:03:06` | `cowrie.direct-tcpip.request` |
| `2026-07-21 13:03:06` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-21 13:03:06` | `cowrie.direct-tcpip.data` |
| `2026-07-21 13:03:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.29.26[.]195` to AbuseIPDB if not already reported
- [ ] Block `46.29.26[.]195` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe38b339c48e

| Field | Detail |
|---|---|
| **Source IP** | `102.208.217[.]175` |
| **First Seen** | 2026-07-21 13:03 |
| **Last Seen** | 2026-07-21 13:03 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 13:03:18` | `cowrie.session.connect` |
| `2026-07-21 13:03:18` | `cowrie.client.version` |
| `2026-07-21 13:03:18` | `cowrie.client.kex` |
| `2026-07-21 13:03:19` | `cowrie.login.success` |
| `2026-07-21 13:03:20` | `cowrie.session.params` |
| `2026-07-21 13:03:20` | `cowrie.command.input` |
| `2026-07-21 13:03:20` | `cowrie.command.failed` |
| `2026-07-21 13:03:20` | `cowrie.log.closed` |
| `2026-07-21 13:03:21` | `cowrie.session.params` |
| `2026-07-21 13:03:21` | `cowrie.command.input` |
| `2026-07-21 13:03:22` | `cowrie.session.file_download` |
| `2026-07-21 13:03:22` | `cowrie.log.closed` |
| `2026-07-21 13:03:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.208.217[.]175` to AbuseIPDB if not already reported
- [ ] Block `102.208.217[.]175` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa48fc5164cc

| Field | Detail |
|---|---|
| **Source IP** | `102.208.217[.]175` |
| **First Seen** | 2026-07-21 13:03 |
| **Last Seen** | 2026-07-21 13:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 13:03:22` | `cowrie.session.connect` |
| `2026-07-21 13:03:22` | `cowrie.client.version` |
| `2026-07-21 13:03:22` | `cowrie.client.kex` |
| `2026-07-21 13:03:23` | `cowrie.login.success` |
| `2026-07-21 13:03:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.208.217[.]175` to AbuseIPDB if not already reported
- [ ] Block `102.208.217[.]175` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41cc328c7beb

| Field | Detail |
|---|---|
| **Source IP** | `102.208.217[.]175` |
| **First Seen** | 2026-07-21 13:03 |
| **Last Seen** | 2026-07-21 13:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 13:03:23` | `cowrie.session.connect` |
| `2026-07-21 13:03:23` | `cowrie.client.version` |
| `2026-07-21 13:03:24` | `cowrie.client.kex` |
| `2026-07-21 13:03:25` | `cowrie.login.success` |
| `2026-07-21 13:03:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.208.217[.]175` to AbuseIPDB if not already reported
- [ ] Block `102.208.217[.]175` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c02514842fde

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-21 13:03 |
| **Last Seen** | 2026-07-21 13:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 13:03:40` | `cowrie.session.connect` |
| `2026-07-21 13:03:40` | `cowrie.client.version` |
| `2026-07-21 13:03:40` | `cowrie.client.kex` |
| `2026-07-21 13:03:40` | `cowrie.login.success` |
| `2026-07-21 13:03:41` | `cowrie.session.params` |
| `2026-07-21 13:03:41` | `cowrie.command.input` |
| `2026-07-21 13:03:41` | `cowrie.log.closed` |
| `2026-07-21 13:03:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e7cd894ddbc

| Field | Detail |
|---|---|
| **Source IP** | `41.220.3[.]101` |
| **First Seen** | 2026-07-21 13:08 |
| **Last Seen** | 2026-07-21 13:08 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 13:08:14` | `cowrie.session.connect` |
| `2026-07-21 13:08:16` | `cowrie.client.version` |
| `2026-07-21 13:08:16` | `cowrie.client.kex` |
| `2026-07-21 13:08:18` | `cowrie.login.success` |
| `2026-07-21 13:08:18` | `cowrie.direct-tcpip.request` |
| `2026-07-21 13:08:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.220.3[.]101` to AbuseIPDB if not already reported
- [ ] Block `41.220.3[.]101` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3e3b23b1842

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-21 13:10 |
| **Last Seen** | 2026-07-21 13:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 13:10:58` | `cowrie.session.connect` |
| `2026-07-21 13:10:58` | `cowrie.client.version` |
| `2026-07-21 13:10:58` | `cowrie.client.kex` |
| `2026-07-21 13:10:58` | `cowrie.login.success` |
| `2026-07-21 13:10:59` | `cowrie.session.params` |
| `2026-07-21 13:10:59` | `cowrie.command.input` |
| `2026-07-21 13:10:59` | `cowrie.log.closed` |
| `2026-07-21 13:10:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f9434060a38

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-21 13:11 |
| **Last Seen** | 2026-07-21 13:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 13:11:07` | `cowrie.session.connect` |
| `2026-07-21 13:11:07` | `cowrie.client.version` |
| `2026-07-21 13:11:07` | `cowrie.client.kex` |
| `2026-07-21 13:11:08` | `cowrie.login.success` |
| `2026-07-21 13:11:08` | `cowrie.direct-tcpip.request` |
| `2026-07-21 13:11:08` | `cowrie.direct-tcpip.data` |
| `2026-07-21 13:11:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4604526f63b6

| Field | Detail |
|---|---|
| **Source IP** | `218.206.136[.]24` |
| **First Seen** | 2026-07-21 13:14 |
| **Last Seen** | 2026-07-21 13:14 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 13:14:06` | `cowrie.session.connect` |
| `2026-07-21 13:14:06` | `cowrie.client.version` |
| `2026-07-21 13:14:06` | `cowrie.client.kex` |
| `2026-07-21 13:14:10` | `cowrie.login.success` |
| `2026-07-21 13:14:11` | `cowrie.direct-tcpip.request` |
| `2026-07-21 13:14:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.206.136[.]24` to AbuseIPDB if not already reported
- [ ] Block `218.206.136[.]24` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04c83b250419

| Field | Detail |
|---|---|
| **Source IP** | `103.68.22[.]115` |
| **First Seen** | 2026-07-21 13:17 |
| **Last Seen** | 2026-07-21 13:17 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 13:17:32` | `cowrie.session.connect` |
| `2026-07-21 13:17:33` | `cowrie.client.version` |
| `2026-07-21 13:17:33` | `cowrie.client.kex` |
| `2026-07-21 13:17:36` | `cowrie.login.success` |
| `2026-07-21 13:17:38` | `cowrie.direct-tcpip.request` |
| `2026-07-21 13:17:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.68.22[.]115` to AbuseIPDB if not already reported
- [ ] Block `103.68.22[.]115` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cfea3bf6686e

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-21 13:22 |
| **Last Seen** | 2026-07-21 13:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 13:22:18` | `cowrie.session.connect` |
| `2026-07-21 13:22:18` | `cowrie.client.version` |
| `2026-07-21 13:22:19` | `cowrie.client.kex` |
| `2026-07-21 13:22:19` | `cowrie.login.success` |
| `2026-07-21 13:22:19` | `cowrie.direct-tcpip.request` |
| `2026-07-21 13:22:19` | `cowrie.direct-tcpip.data` |
| `2026-07-21 13:22:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-979b1f8c2206

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]164` |
| **First Seen** | 2026-07-21 13:22 |
| **Last Seen** | 2026-07-21 13:22 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST, /bin/busybox TEST, cat /proc, ./` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 13:22:20` | `cowrie.session.connect` |
| `2026-07-21 13:22:21` | `cowrie.login.success` |
| `2026-07-21 13:22:22` | `cowrie.session.params` |
| `2026-07-21 13:22:22` | `cowrie.command.input` |
| `2026-07-21 13:22:23` | `cowrie.command.input` |
| `2026-07-21 13:22:24` | `cowrie.command.input` |
| `2026-07-21 13:22:24` | `cowrie.command.input` |
| `2026-07-21 13:22:24` | `cowrie.command.failed` |
| `2026-07-21 13:22:25` | `cowrie.log.closed` |
| `2026-07-21 13:22:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]164` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b73f8501716

| Field | Detail |
|---|---|
| **Source IP** | `65.181.79[.]60` |
| **First Seen** | 2026-07-21 13:24 |
| **Last Seen** | 2026-07-21 13:24 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 13:24:24` | `cowrie.session.connect` |
| `2026-07-21 13:24:25` | `cowrie.client.version` |
| `2026-07-21 13:24:25` | `cowrie.client.kex` |
| `2026-07-21 13:24:27` | `cowrie.login.success` |
| `2026-07-21 13:24:29` | `cowrie.direct-tcpip.request` |
| `2026-07-21 13:24:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.181.79[.]60` to AbuseIPDB if not already reported
- [ ] Block `65.181.79[.]60` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-577a46d315bb

| Field | Detail |
|---|---|
| **Source IP** | `218.146.255[.]221` |
| **First Seen** | 2026-07-21 13:26 |
| **Last Seen** | 2026-07-21 13:26 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 13:26:30` | `cowrie.session.connect` |
| `2026-07-21 13:26:31` | `cowrie.client.version` |
| `2026-07-21 13:26:31` | `cowrie.client.kex` |
| `2026-07-21 13:26:35` | `cowrie.login.success` |
| `2026-07-21 13:26:36` | `cowrie.direct-tcpip.request` |
| `2026-07-21 13:26:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.146.255[.]221` to AbuseIPDB if not already reported
- [ ] Block `218.146.255[.]221` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a050f9dc241

| Field | Detail |
|---|---|
| **Source IP** | `65.20.191[.]231` |
| **First Seen** | 2026-07-21 13:26 |
| **Last Seen** | 2026-07-21 13:26 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 13:26:46` | `cowrie.session.connect` |
| `2026-07-21 13:26:46` | `cowrie.client.version` |
| `2026-07-21 13:26:46` | `cowrie.client.kex` |
| `2026-07-21 13:26:48` | `cowrie.login.success` |
| `2026-07-21 13:26:48` | `cowrie.direct-tcpip.request` |
| `2026-07-21 13:26:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.191[.]231` to AbuseIPDB if not already reported
- [ ] Block `65.20.191[.]231` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d73ab15e993

| Field | Detail |
|---|---|
| **Source IP** | `191.36.152[.]28` |
| **First Seen** | 2026-07-21 13:29 |
| **Last Seen** | 2026-07-21 13:34 |
| **Session Duration** | 304s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 13:29:44` | `cowrie.session.connect` |
| `2026-07-21 13:29:46` | `cowrie.client.version` |
| `2026-07-21 13:29:46` | `cowrie.client.kex` |
| `2026-07-21 13:29:49` | `cowrie.login.success` |
| `2026-07-21 13:29:49` | `cowrie.direct-tcpip.request` |
| `2026-07-21 13:34:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `191.36.152[.]28` to AbuseIPDB if not already reported
- [ ] Block `191.36.152[.]28` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-768acedd6268

| Field | Detail |
|---|---|
| **Source IP** | `211.53.58[.]10` |
| **First Seen** | 2026-07-21 13:29 |
| **Last Seen** | 2026-07-21 13:30 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 13:29:48` | `cowrie.session.connect` |
| `2026-07-21 13:29:49` | `cowrie.client.version` |
| `2026-07-21 13:29:49` | `cowrie.client.kex` |
| `2026-07-21 13:29:53` | `cowrie.login.success` |
| `2026-07-21 13:29:55` | `cowrie.direct-tcpip.request` |
| `2026-07-21 13:30:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.53.58[.]10` to AbuseIPDB if not already reported
- [ ] Block `211.53.58[.]10` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5e134d1b598

| Field | Detail |
|---|---|
| **Source IP** | `117.250.19[.]91` |
| **First Seen** | 2026-07-21 13:30 |
| **Last Seen** | 2026-07-21 13:30 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 13:30:05` | `cowrie.session.connect` |
| `2026-07-21 13:30:06` | `cowrie.client.version` |
| `2026-07-21 13:30:06` | `cowrie.client.kex` |
| `2026-07-21 13:30:08` | `cowrie.login.success` |
| `2026-07-21 13:30:09` | `cowrie.direct-tcpip.request` |
| `2026-07-21 13:30:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.250.19[.]91` to AbuseIPDB if not already reported
- [ ] Block `117.250.19[.]91` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d555dd307c2c

| Field | Detail |
|---|---|
| **Source IP** | `188.168.86[.]6` |
| **First Seen** | 2026-07-21 13:32 |
| **Last Seen** | 2026-07-21 13:33 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 13:32:56` | `cowrie.session.connect` |
| `2026-07-21 13:32:57` | `cowrie.client.version` |
| `2026-07-21 13:32:57` | `cowrie.client.kex` |
| `2026-07-21 13:32:59` | `cowrie.login.success` |
| `2026-07-21 13:33:00` | `cowrie.direct-tcpip.request` |
| `2026-07-21 13:33:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `188.168.86[.]6` to AbuseIPDB if not already reported
- [ ] Block `188.168.86[.]6` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f44af850ab68

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-21 13:37 |
| **Last Seen** | 2026-07-21 13:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 13:37:08` | `cowrie.session.connect` |
| `2026-07-21 13:37:08` | `cowrie.client.version` |
| `2026-07-21 13:37:08` | `cowrie.client.kex` |
| `2026-07-21 13:37:09` | `cowrie.login.success` |
| `2026-07-21 13:37:09` | `cowrie.direct-tcpip.request` |
| `2026-07-21 13:37:09` | `cowrie.direct-tcpip.data` |
| `2026-07-21 13:37:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-049026ebb0db

| Field | Detail |
|---|---|
| **Source IP** | `49.206.194[.]29` |
| **First Seen** | 2026-07-21 13:38 |
| **Last Seen** | 2026-07-21 13:39 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 13:38:57` | `cowrie.session.connect` |
| `2026-07-21 13:38:58` | `cowrie.client.version` |
| `2026-07-21 13:38:58` | `cowrie.client.kex` |
| `2026-07-21 13:39:00` | `cowrie.login.success` |
| `2026-07-21 13:39:01` | `cowrie.direct-tcpip.request` |
| `2026-07-21 13:39:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.206.194[.]29` to AbuseIPDB if not already reported
- [ ] Block `49.206.194[.]29` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1fa3d4e3a1be

| Field | Detail |
|---|---|
| **Source IP** | `85.105.255[.]56` |
| **First Seen** | 2026-07-21 13:47 |
| **Last Seen** | 2026-07-21 13:47 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 13:47:45` | `cowrie.session.connect` |
| `2026-07-21 13:47:45` | `cowrie.client.version` |
| `2026-07-21 13:47:45` | `cowrie.client.kex` |
| `2026-07-21 13:47:46` | `cowrie.login.success` |
| `2026-07-21 13:47:46` | `cowrie.direct-tcpip.request` |
| `2026-07-21 13:47:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.105.255[.]56` to AbuseIPDB if not already reported
- [ ] Block `85.105.255[.]56` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1dad055e4a23

| Field | Detail |
|---|---|
| **Source IP** | `203.193.147[.]75` |
| **First Seen** | 2026-07-21 13:47 |
| **Last Seen** | 2026-07-21 13:48 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 13:47:52` | `cowrie.session.connect` |
| `2026-07-21 13:47:52` | `cowrie.client.version` |
| `2026-07-21 13:47:52` | `cowrie.client.kex` |
| `2026-07-21 13:47:56` | `cowrie.login.success` |
| `2026-07-21 13:48:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.193.147[.]75` to AbuseIPDB if not already reported
- [ ] Block `203.193.147[.]75` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5622362137f7

| Field | Detail |
|---|---|
| **Source IP** | `196.190.180[.]18` |
| **First Seen** | 2026-07-21 13:51 |
| **Last Seen** | 2026-07-21 13:51 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 13:51:15` | `cowrie.session.connect` |
| `2026-07-21 13:51:15` | `cowrie.client.version` |
| `2026-07-21 13:51:15` | `cowrie.client.kex` |
| `2026-07-21 13:51:17` | `cowrie.login.success` |
| `2026-07-21 13:51:17` | `cowrie.direct-tcpip.request` |
| `2026-07-21 13:51:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.190.180[.]18` to AbuseIPDB if not already reported
- [ ] Block `196.190.180[.]18` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a79b7dc7a4f4

| Field | Detail |
|---|---|
| **Source IP** | `180.76.52[.]146` |
| **First Seen** | 2026-07-21 13:51 |
| **Last Seen** | 2026-07-21 13:51 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 13:51:22` | `cowrie.session.connect` |
| `2026-07-21 13:51:23` | `cowrie.client.version` |
| `2026-07-21 13:51:23` | `cowrie.client.kex` |
| `2026-07-21 13:51:25` | `cowrie.login.success` |
| `2026-07-21 13:51:25` | `cowrie.direct-tcpip.request` |
| `2026-07-21 13:51:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.76.52[.]146` to AbuseIPDB if not already reported
- [ ] Block `180.76.52[.]146` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-026f5f180c9e

| Field | Detail |
|---|---|
| **Source IP** | `111.36.57[.]69` |
| **First Seen** | 2026-07-21 13:52 |
| **Last Seen** | 2026-07-21 13:52 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 13:52:35` | `cowrie.session.connect` |
| `2026-07-21 13:52:35` | `cowrie.client.version` |
| `2026-07-21 13:52:50` | `cowrie.client.kex` |
| `2026-07-21 13:52:51` | `cowrie.login.success` |
| `2026-07-21 13:52:52` | `cowrie.session.params` |
| `2026-07-21 13:52:52` | `cowrie.command.input` |
| `2026-07-21 13:52:52` | `cowrie.log.closed` |
| `2026-07-21 13:52:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.36.57[.]69` to AbuseIPDB if not already reported
- [ ] Block `111.36.57[.]69` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c48eed8fba8

| Field | Detail |
|---|---|
| **Source IP** | `65.20.179[.]251` |
| **First Seen** | 2026-07-21 13:54 |
| **Last Seen** | 2026-07-21 13:54 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 13:54:45` | `cowrie.session.connect` |
| `2026-07-21 13:54:46` | `cowrie.client.version` |
| `2026-07-21 13:54:46` | `cowrie.client.kex` |
| `2026-07-21 13:54:47` | `cowrie.login.success` |
| `2026-07-21 13:54:48` | `cowrie.direct-tcpip.request` |
| `2026-07-21 13:54:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.179[.]251` to AbuseIPDB if not already reported
- [ ] Block `65.20.179[.]251` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-947d8f74e67d

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-21 13:55 |
| **Last Seen** | 2026-07-21 13:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 13:55:05` | `cowrie.session.connect` |
| `2026-07-21 13:55:05` | `cowrie.client.version` |
| `2026-07-21 13:55:05` | `cowrie.client.kex` |
| `2026-07-21 13:55:05` | `cowrie.login.success` |
| `2026-07-21 13:55:06` | `cowrie.session.params` |
| `2026-07-21 13:55:06` | `cowrie.command.input` |
| `2026-07-21 13:55:06` | `cowrie.log.closed` |
| `2026-07-21 13:55:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff97b1cadee1

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-21 13:57 |
| **Last Seen** | 2026-07-21 13:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 13:57:25` | `cowrie.session.connect` |
| `2026-07-21 13:57:25` | `cowrie.client.version` |
| `2026-07-21 13:57:25` | `cowrie.client.kex` |
| `2026-07-21 13:57:26` | `cowrie.login.success` |
| `2026-07-21 13:57:26` | `cowrie.direct-tcpip.request` |
| `2026-07-21 13:57:26` | `cowrie.direct-tcpip.data` |
| `2026-07-21 13:57:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d67da375945

| Field | Detail |
|---|---|
| **Source IP** | `61.185.30[.]170` |
| **First Seen** | 2026-07-21 13:57 |
| **Last Seen** | 2026-07-21 13:58 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 13:57:53` | `cowrie.session.connect` |
| `2026-07-21 13:57:54` | `cowrie.client.version` |
| `2026-07-21 13:57:54` | `cowrie.client.kex` |
| `2026-07-21 13:57:58` | `cowrie.login.success` |
| `2026-07-21 13:58:00` | `cowrie.direct-tcpip.request` |
| `2026-07-21 13:58:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.185.30[.]170` to AbuseIPDB if not already reported
- [ ] Block `61.185.30[.]170` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ebcfbcff4fc

| Field | Detail |
|---|---|
| **Source IP** | `196.188.93[.]169` |
| **First Seen** | 2026-07-21 13:58 |
| **Last Seen** | 2026-07-21 13:58 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 13:58:10` | `cowrie.session.connect` |
| `2026-07-21 13:58:10` | `cowrie.client.version` |
| `2026-07-21 13:58:10` | `cowrie.client.kex` |
| `2026-07-21 13:58:11` | `cowrie.login.success` |
| `2026-07-21 13:58:12` | `cowrie.direct-tcpip.request` |
| `2026-07-21 13:58:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.188.93[.]169` to AbuseIPDB if not already reported
- [ ] Block `196.188.93[.]169` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b51149ab48ac

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-21 14:00 |
| **Last Seen** | 2026-07-21 14:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 14:00:54` | `cowrie.session.connect` |
| `2026-07-21 14:00:54` | `cowrie.client.version` |
| `2026-07-21 14:00:54` | `cowrie.client.kex` |
| `2026-07-21 14:00:54` | `cowrie.login.success` |
| `2026-07-21 14:00:54` | `cowrie.direct-tcpip.request` |
| `2026-07-21 14:00:54` | `cowrie.direct-tcpip.data` |
| `2026-07-21 14:00:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-073a2d4d1a67

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-21 14:02 |
| **Last Seen** | 2026-07-21 14:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 14:02:19` | `cowrie.session.connect` |
| `2026-07-21 14:02:19` | `cowrie.client.version` |
| `2026-07-21 14:02:19` | `cowrie.client.kex` |
| `2026-07-21 14:02:20` | `cowrie.login.success` |
| `2026-07-21 14:02:20` | `cowrie.session.params` |
| `2026-07-21 14:02:20` | `cowrie.command.input` |
| `2026-07-21 14:02:21` | `cowrie.log.closed` |
| `2026-07-21 14:02:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a5ad2df55b7

| Field | Detail |
|---|---|
| **Source IP** | `14.103.117[.]142` |
| **First Seen** | 2026-07-21 14:04 |
| **Last Seen** | 2026-07-21 14:04 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 14:04:18` | `cowrie.session.connect` |
| `2026-07-21 14:04:18` | `cowrie.client.version` |
| `2026-07-21 14:04:22` | `cowrie.client.kex` |
| `2026-07-21 14:04:23` | `cowrie.login.success` |
| `2026-07-21 14:04:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.117[.]142` to AbuseIPDB if not already reported
- [ ] Block `14.103.117[.]142` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd9e90e0bbfc

| Field | Detail |
|---|---|
| **Source IP** | `210.4.68[.]73` |
| **First Seen** | 2026-07-21 14:08 |
| **Last Seen** | 2026-07-21 14:08 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 14:08:06` | `cowrie.session.connect` |
| `2026-07-21 14:08:06` | `cowrie.client.version` |
| `2026-07-21 14:08:06` | `cowrie.client.kex` |
| `2026-07-21 14:08:08` | `cowrie.login.success` |
| `2026-07-21 14:08:09` | `cowrie.direct-tcpip.request` |
| `2026-07-21 14:08:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.4.68[.]73` to AbuseIPDB if not already reported
- [ ] Block `210.4.68[.]73` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca7834e7c252

| Field | Detail |
|---|---|
| **Source IP** | `24.207.66[.]154` |
| **First Seen** | 2026-07-21 14:11 |
| **Last Seen** | 2026-07-21 14:11 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 14:11:21` | `cowrie.session.connect` |
| `2026-07-21 14:11:21` | `cowrie.client.version` |
| `2026-07-21 14:11:21` | `cowrie.client.kex` |
| `2026-07-21 14:11:23` | `cowrie.login.success` |
| `2026-07-21 14:11:23` | `cowrie.direct-tcpip.request` |
| `2026-07-21 14:11:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `24.207.66[.]154` to AbuseIPDB if not already reported
- [ ] Block `24.207.66[.]154` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2fee2bdde286

| Field | Detail |
|---|---|
| **Source IP** | `103.147.248[.]23` |
| **First Seen** | 2026-07-21 14:11 |
| **Last Seen** | 2026-07-21 14:11 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 14:11:28` | `cowrie.session.connect` |
| `2026-07-21 14:11:29` | `cowrie.client.version` |
| `2026-07-21 14:11:29` | `cowrie.client.kex` |
| `2026-07-21 14:11:32` | `cowrie.login.success` |
| `2026-07-21 14:11:32` | `cowrie.direct-tcpip.request` |
| `2026-07-21 14:11:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.147.248[.]23` to AbuseIPDB if not already reported
- [ ] Block `103.147.248[.]23` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a02b3b800ad9

| Field | Detail |
|---|---|
| **Source IP** | `14.103.117[.]142` |
| **First Seen** | 2026-07-21 14:13 |
| **Last Seen** | 2026-07-21 14:18 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 14:13:46` | `cowrie.session.connect` |
| `2026-07-21 14:13:46` | `cowrie.client.version` |
| `2026-07-21 14:13:46` | `cowrie.client.kex` |
| `2026-07-21 14:13:48` | `cowrie.login.success` |
| `2026-07-21 14:14:04` | `cowrie.session.params` |
| `2026-07-21 14:14:04` | `cowrie.command.input` |
| `2026-07-21 14:14:04` | `cowrie.session.file_download` |
| `2026-07-21 14:14:04` | `cowrie.log.closed` |
| `2026-07-21 14:18:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.117[.]142` to AbuseIPDB if not already reported
- [ ] Block `14.103.117[.]142` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-077ed8be6acf

| Field | Detail |
|---|---|
| **Source IP** | `191.36.154[.]175` |
| **First Seen** | 2026-07-21 14:16 |
| **Last Seen** | 2026-07-21 14:21 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 14:16:21` | `cowrie.session.connect` |
| `2026-07-21 14:16:22` | `cowrie.client.version` |
| `2026-07-21 14:16:22` | `cowrie.client.kex` |
| `2026-07-21 14:16:24` | `cowrie.login.success` |
| `2026-07-21 14:16:24` | `cowrie.direct-tcpip.request` |
| `2026-07-21 14:21:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `191.36.154[.]175` to AbuseIPDB if not already reported
- [ ] Block `191.36.154[.]175` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d6d09b88f6d

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-21 14:20 |
| **Last Seen** | 2026-07-21 14:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 14:20:27` | `cowrie.session.connect` |
| `2026-07-21 14:20:27` | `cowrie.client.version` |
| `2026-07-21 14:20:27` | `cowrie.client.kex` |
| `2026-07-21 14:20:27` | `cowrie.login.success` |
| `2026-07-21 14:20:28` | `cowrie.direct-tcpip.request` |
| `2026-07-21 14:20:28` | `cowrie.direct-tcpip.data` |
| `2026-07-21 14:20:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ad8a0e8f886

| Field | Detail |
|---|---|
| **Source IP** | `14.103.117[.]142` |
| **First Seen** | 2026-07-21 14:27 |
| **Last Seen** | 2026-07-21 14:33 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 14:27:58` | `cowrie.session.connect` |
| `2026-07-21 14:27:58` | `cowrie.client.version` |
| `2026-07-21 14:27:58` | `cowrie.client.kex` |
| `2026-07-21 14:28:01` | `cowrie.login.success` |
| `2026-07-21 14:33:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.117[.]142` to AbuseIPDB if not already reported
- [ ] Block `14.103.117[.]142` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ea51a207dd0

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-21 14:28 |
| **Last Seen** | 2026-07-21 14:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 14:28:21` | `cowrie.session.connect` |
| `2026-07-21 14:28:21` | `cowrie.client.version` |
| `2026-07-21 14:28:21` | `cowrie.client.kex` |
| `2026-07-21 14:28:21` | `cowrie.login.success` |
| `2026-07-21 14:28:21` | `cowrie.direct-tcpip.request` |
| `2026-07-21 14:28:22` | `cowrie.direct-tcpip.data` |
| `2026-07-21 14:28:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb6c0ed4861f

| Field | Detail |
|---|---|
| **Source IP** | `60.174.39[.]82` |
| **First Seen** | 2026-07-21 14:31 |
| **Last Seen** | 2026-07-21 14:31 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 14:31:45` | `cowrie.session.connect` |
| `2026-07-21 14:31:45` | `cowrie.client.version` |
| `2026-07-21 14:31:45` | `cowrie.client.kex` |
| `2026-07-21 14:31:48` | `cowrie.login.success` |
| `2026-07-21 14:31:49` | `cowrie.direct-tcpip.request` |
| `2026-07-21 14:31:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.174.39[.]82` to AbuseIPDB if not already reported
- [ ] Block `60.174.39[.]82` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6f44a2c6f35

| Field | Detail |
|---|---|
| **Source IP** | `196.189.126[.]10` |
| **First Seen** | 2026-07-21 14:31 |
| **Last Seen** | 2026-07-21 14:32 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 14:31:54` | `cowrie.session.connect` |
| `2026-07-21 14:31:54` | `cowrie.client.version` |
| `2026-07-21 14:31:54` | `cowrie.client.kex` |
| `2026-07-21 14:31:56` | `cowrie.login.success` |
| `2026-07-21 14:31:56` | `cowrie.direct-tcpip.request` |
| `2026-07-21 14:32:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.189.126[.]10` to AbuseIPDB if not already reported
- [ ] Block `196.189.126[.]10` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b2e2b38aecc

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-21 14:36 |
| **Last Seen** | 2026-07-21 14:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 14:36:08` | `cowrie.session.connect` |
| `2026-07-21 14:36:08` | `cowrie.client.version` |
| `2026-07-21 14:36:08` | `cowrie.client.kex` |
| `2026-07-21 14:36:09` | `cowrie.login.success` |
| `2026-07-21 14:36:09` | `cowrie.direct-tcpip.request` |
| `2026-07-21 14:36:09` | `cowrie.direct-tcpip.data` |
| `2026-07-21 14:36:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e332feac9c6

| Field | Detail |
|---|---|
| **Source IP** | `122.160.15[.]31` |
| **First Seen** | 2026-07-21 14:41 |
| **Last Seen** | 2026-07-21 14:41 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 14:41:09` | `cowrie.session.connect` |
| `2026-07-21 14:41:09` | `cowrie.client.version` |
| `2026-07-21 14:41:09` | `cowrie.client.kex` |
| `2026-07-21 14:41:11` | `cowrie.login.success` |
| `2026-07-21 14:41:12` | `cowrie.direct-tcpip.request` |
| `2026-07-21 14:41:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.160.15[.]31` to AbuseIPDB if not already reported
- [ ] Block `122.160.15[.]31` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c5aa2ee710b

| Field | Detail |
|---|---|
| **Source IP** | `196.188.93[.]169` |
| **First Seen** | 2026-07-21 14:41 |
| **Last Seen** | 2026-07-21 14:41 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 14:41:17` | `cowrie.session.connect` |
| `2026-07-21 14:41:18` | `cowrie.client.version` |
| `2026-07-21 14:41:18` | `cowrie.client.kex` |
| `2026-07-21 14:41:19` | `cowrie.login.success` |
| `2026-07-21 14:41:19` | `cowrie.direct-tcpip.request` |
| `2026-07-21 14:41:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.188.93[.]169` to AbuseIPDB if not already reported
- [ ] Block `196.188.93[.]169` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c823a94fc221

| Field | Detail |
|---|---|
| **Source IP** | `150.228.187[.]139` |
| **First Seen** | 2026-07-21 14:44 |
| **Last Seen** | 2026-07-21 14:44 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 14:44:16` | `cowrie.session.connect` |
| `2026-07-21 14:44:17` | `cowrie.client.version` |
| `2026-07-21 14:44:17` | `cowrie.client.kex` |
| `2026-07-21 14:44:19` | `cowrie.login.success` |
| `2026-07-21 14:44:20` | `cowrie.direct-tcpip.request` |
| `2026-07-21 14:44:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `150.228.187[.]139` to AbuseIPDB if not already reported
- [ ] Block `150.228.187[.]139` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8aab63942838

| Field | Detail |
|---|---|
| **Source IP** | `188.36.7[.]196` |
| **First Seen** | 2026-07-21 14:44 |
| **Last Seen** | 2026-07-21 14:44 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 14:44:25` | `cowrie.session.connect` |
| `2026-07-21 14:44:26` | `cowrie.client.version` |
| `2026-07-21 14:44:26` | `cowrie.client.kex` |
| `2026-07-21 14:44:27` | `cowrie.login.success` |
| `2026-07-21 14:44:27` | `cowrie.direct-tcpip.request` |
| `2026-07-21 14:44:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `188.36.7[.]196` to AbuseIPDB if not already reported
- [ ] Block `188.36.7[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ae4f1e0a607

| Field | Detail |
|---|---|
| **Source IP** | `186.239.41[.]74` |
| **First Seen** | 2026-07-21 14:44 |
| **Last Seen** | 2026-07-21 14:44 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 14:44:39` | `cowrie.session.connect` |
| `2026-07-21 14:44:40` | `cowrie.client.version` |
| `2026-07-21 14:44:40` | `cowrie.client.kex` |
| `2026-07-21 14:44:41` | `cowrie.login.success` |
| `2026-07-21 14:44:42` | `cowrie.direct-tcpip.request` |
| `2026-07-21 14:44:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.239.41[.]74` to AbuseIPDB if not already reported
- [ ] Block `186.239.41[.]74` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff0cb38201f1

| Field | Detail |
|---|---|
| **Source IP** | `178.216.165[.]187` |
| **First Seen** | 2026-07-21 14:44 |
| **Last Seen** | 2026-07-21 14:44 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 14:44:47` | `cowrie.session.connect` |
| `2026-07-21 14:44:47` | `cowrie.client.version` |
| `2026-07-21 14:44:47` | `cowrie.client.kex` |
| `2026-07-21 14:44:48` | `cowrie.login.success` |
| `2026-07-21 14:44:48` | `cowrie.direct-tcpip.request` |
| `2026-07-21 14:44:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.216.165[.]187` to AbuseIPDB if not already reported
- [ ] Block `178.216.165[.]187` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45a900f2ea11

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-21 14:46 |
| **Last Seen** | 2026-07-21 14:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 14:46:27` | `cowrie.session.connect` |
| `2026-07-21 14:46:27` | `cowrie.client.version` |
| `2026-07-21 14:46:27` | `cowrie.client.kex` |
| `2026-07-21 14:46:28` | `cowrie.login.success` |
| `2026-07-21 14:46:28` | `cowrie.session.params` |
| `2026-07-21 14:46:28` | `cowrie.command.input` |
| `2026-07-21 14:46:29` | `cowrie.log.closed` |
| `2026-07-21 14:46:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d9c75cfdc125

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-21 14:48 |
| **Last Seen** | 2026-07-21 14:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 14:48:07` | `cowrie.session.connect` |
| `2026-07-21 14:48:07` | `cowrie.client.version` |
| `2026-07-21 14:48:07` | `cowrie.client.kex` |
| `2026-07-21 14:48:07` | `cowrie.login.success` |
| `2026-07-21 14:48:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eaa57ee87e79

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-21 14:48 |
| **Last Seen** | 2026-07-21 14:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 14:48:07` | `cowrie.session.connect` |
| `2026-07-21 14:48:07` | `cowrie.client.version` |
| `2026-07-21 14:48:07` | `cowrie.client.kex` |
| `2026-07-21 14:48:07` | `cowrie.login.success` |
| `2026-07-21 14:48:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f5c72a6ca9bf

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-21 14:48 |
| **Last Seen** | 2026-07-21 14:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 14:48:15` | `cowrie.session.connect` |
| `2026-07-21 14:48:15` | `cowrie.client.version` |
| `2026-07-21 14:48:15` | `cowrie.client.kex` |
| `2026-07-21 14:48:15` | `cowrie.login.success` |
| `2026-07-21 14:48:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74f943764703

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-21 14:48 |
| **Last Seen** | 2026-07-21 14:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 14:48:15` | `cowrie.session.connect` |
| `2026-07-21 14:48:15` | `cowrie.client.version` |
| `2026-07-21 14:48:15` | `cowrie.client.kex` |
| `2026-07-21 14:48:15` | `cowrie.login.success` |
| `2026-07-21 14:48:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-532ce4afcfb4

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-21 14:52 |
| **Last Seen** | 2026-07-21 14:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 14:52:06` | `cowrie.session.connect` |
| `2026-07-21 14:52:06` | `cowrie.client.version` |
| `2026-07-21 14:52:06` | `cowrie.client.kex` |
| `2026-07-21 14:52:07` | `cowrie.login.success` |
| `2026-07-21 14:52:07` | `cowrie.direct-tcpip.request` |
| `2026-07-21 14:52:07` | `cowrie.direct-tcpip.data` |
| `2026-07-21 14:52:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6fadc495d78

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-21 14:53 |
| **Last Seen** | 2026-07-21 14:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 14:53:45` | `cowrie.session.connect` |
| `2026-07-21 14:53:45` | `cowrie.client.version` |
| `2026-07-21 14:53:45` | `cowrie.client.kex` |
| `2026-07-21 14:53:45` | `cowrie.login.success` |
| `2026-07-21 14:53:46` | `cowrie.session.params` |
| `2026-07-21 14:53:46` | `cowrie.command.input` |
| `2026-07-21 14:53:46` | `cowrie.log.closed` |
| `2026-07-21 14:53:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08a63eaf8f97

| Field | Detail |
|---|---|
| **Source IP** | `219.128.15[.]190` |
| **First Seen** | 2026-07-21 14:55 |
| **Last Seen** | 2026-07-21 14:55 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 14:55:16` | `cowrie.session.connect` |
| `2026-07-21 14:55:17` | `cowrie.client.version` |
| `2026-07-21 14:55:17` | `cowrie.client.kex` |
| `2026-07-21 14:55:20` | `cowrie.login.success` |
| `2026-07-21 14:55:21` | `cowrie.direct-tcpip.request` |
| `2026-07-21 14:55:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `219.128.15[.]190` to AbuseIPDB if not already reported
- [ ] Block `219.128.15[.]190` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08b8f9348b3c

| Field | Detail |
|---|---|
| **Source IP** | `119.247.187[.]188` |
| **First Seen** | 2026-07-21 14:55 |
| **Last Seen** | 2026-07-21 14:55 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 14:55:31` | `cowrie.session.connect` |
| `2026-07-21 14:55:32` | `cowrie.client.version` |
| `2026-07-21 14:55:32` | `cowrie.client.kex` |
| `2026-07-21 14:55:33` | `cowrie.login.success` |
| `2026-07-21 14:55:34` | `cowrie.direct-tcpip.request` |
| `2026-07-21 14:55:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.247.187[.]188` to AbuseIPDB if not already reported
- [ ] Block `119.247.187[.]188` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e1ed604c2e8

| Field | Detail |
|---|---|
| **Source IP** | `27.107.102[.]154` |
| **First Seen** | 2026-07-21 14:58 |
| **Last Seen** | 2026-07-21 14:58 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 14:58:26` | `cowrie.session.connect` |
| `2026-07-21 14:58:27` | `cowrie.client.version` |
| `2026-07-21 14:58:27` | `cowrie.client.kex` |
| `2026-07-21 14:58:28` | `cowrie.login.success` |
| `2026-07-21 14:58:29` | `cowrie.direct-tcpip.request` |
| `2026-07-21 14:58:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.107.102[.]154` to AbuseIPDB if not already reported
- [ ] Block `27.107.102[.]154` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-183b175bbdce

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-21 15:05 |
| **Last Seen** | 2026-07-21 15:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 15:05:31` | `cowrie.session.connect` |
| `2026-07-21 15:05:31` | `cowrie.client.version` |
| `2026-07-21 15:05:31` | `cowrie.client.kex` |
| `2026-07-21 15:05:31` | `cowrie.login.success` |
| `2026-07-21 15:05:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03434face614

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-21 15:05 |
| **Last Seen** | 2026-07-21 15:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 15:05:33` | `cowrie.session.connect` |
| `2026-07-21 15:05:33` | `cowrie.client.version` |
| `2026-07-21 15:05:33` | `cowrie.client.kex` |
| `2026-07-21 15:05:33` | `cowrie.login.success` |
| `2026-07-21 15:05:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1baa2672395

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-21 15:05 |
| **Last Seen** | 2026-07-21 15:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 15:05:37` | `cowrie.session.connect` |
| `2026-07-21 15:05:37` | `cowrie.client.version` |
| `2026-07-21 15:05:38` | `cowrie.client.kex` |
| `2026-07-21 15:05:38` | `cowrie.login.success` |
| `2026-07-21 15:05:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c7467b8e22d

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-21 15:05 |
| **Last Seen** | 2026-07-21 15:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 15:05:38` | `cowrie.session.connect` |
| `2026-07-21 15:05:38` | `cowrie.client.version` |
| `2026-07-21 15:05:39` | `cowrie.client.kex` |
| `2026-07-21 15:05:39` | `cowrie.login.success` |
| `2026-07-21 15:05:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fefc6c2c6fbd

| Field | Detail |
|---|---|
| **Source IP** | `177.159.150[.]111` |
| **First Seen** | 2026-07-21 15:06 |
| **Last Seen** | 2026-07-21 15:06 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 15:06:13` | `cowrie.session.connect` |
| `2026-07-21 15:06:14` | `cowrie.client.version` |
| `2026-07-21 15:06:14` | `cowrie.client.kex` |
| `2026-07-21 15:06:15` | `cowrie.login.success` |
| `2026-07-21 15:06:16` | `cowrie.direct-tcpip.request` |
| `2026-07-21 15:06:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.159.150[.]111` to AbuseIPDB if not already reported
- [ ] Block `177.159.150[.]111` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6acf28150757

| Field | Detail |
|---|---|
| **Source IP** | `118.183.180[.]108` |
| **First Seen** | 2026-07-21 15:06 |
| **Last Seen** | 2026-07-21 15:06 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 15:06:26` | `cowrie.session.connect` |
| `2026-07-21 15:06:27` | `cowrie.client.version` |
| `2026-07-21 15:06:27` | `cowrie.client.kex` |
| `2026-07-21 15:06:28` | `cowrie.login.success` |
| `2026-07-21 15:06:30` | `cowrie.direct-tcpip.request` |
| `2026-07-21 15:06:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.183.180[.]108` to AbuseIPDB if not already reported
- [ ] Block `118.183.180[.]108` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf5f55dd992a

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-21 15:07 |
| **Last Seen** | 2026-07-21 15:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 15:07:09` | `cowrie.session.connect` |
| `2026-07-21 15:07:09` | `cowrie.client.version` |
| `2026-07-21 15:07:09` | `cowrie.client.kex` |
| `2026-07-21 15:07:09` | `cowrie.login.success` |
| `2026-07-21 15:07:09` | `cowrie.direct-tcpip.request` |
| `2026-07-21 15:07:10` | `cowrie.direct-tcpip.data` |
| `2026-07-21 15:07:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a04f9d908add

| Field | Detail |
|---|---|
| **Source IP** | `204.152.195[.]212` |
| **First Seen** | 2026-07-21 15:07 |
| **Last Seen** | 2026-07-21 15:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 15:07:54` | `cowrie.session.connect` |
| `2026-07-21 15:07:54` | `cowrie.client.version` |
| `2026-07-21 15:07:54` | `cowrie.client.kex` |
| `2026-07-21 15:07:54` | `cowrie.login.success` |
| `2026-07-21 15:07:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `204.152.195[.]212` to AbuseIPDB if not already reported
- [ ] Block `204.152.195[.]212` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ff054f013b8

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-07-21 15:07 |
| **Last Seen** | 2026-07-21 15:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 15:07:55` | `cowrie.session.connect` |
| `2026-07-21 15:07:55` | `cowrie.client.version` |
| `2026-07-21 15:07:55` | `cowrie.client.kex` |
| `2026-07-21 15:07:55` | `cowrie.login.success` |
| `2026-07-21 15:07:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26323b2c617c

| Field | Detail |
|---|---|
| **Source IP** | `14.103.117[.]142` |
| **First Seen** | 2026-07-21 15:10 |
| **Last Seen** | 2026-07-21 15:15 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 15:10:23` | `cowrie.session.connect` |
| `2026-07-21 15:10:23` | `cowrie.client.version` |
| `2026-07-21 15:10:24` | `cowrie.client.kex` |
| `2026-07-21 15:10:25` | `cowrie.login.success` |
| `2026-07-21 15:15:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.117[.]142` to AbuseIPDB if not already reported
- [ ] Block `14.103.117[.]142` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-000da30657de

| Field | Detail |
|---|---|
| **Source IP** | `117.2.123[.]19` |
| **First Seen** | 2026-07-21 15:12 |
| **Last Seen** | 2026-07-21 15:12 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 15:12:22` | `cowrie.session.connect` |
| `2026-07-21 15:12:23` | `cowrie.client.version` |
| `2026-07-21 15:12:23` | `cowrie.client.kex` |
| `2026-07-21 15:12:25` | `cowrie.login.success` |
| `2026-07-21 15:12:26` | `cowrie.direct-tcpip.request` |
| `2026-07-21 15:12:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.2.123[.]19` to AbuseIPDB if not already reported
- [ ] Block `117.2.123[.]19` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5259aed7fe0a

| Field | Detail |
|---|---|
| **Source IP** | `60.166.8[.]174` |
| **First Seen** | 2026-07-21 15:12 |
| **Last Seen** | 2026-07-21 15:12 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 15:12:31` | `cowrie.session.connect` |
| `2026-07-21 15:12:31` | `cowrie.client.version` |
| `2026-07-21 15:12:31` | `cowrie.client.kex` |
| `2026-07-21 15:12:34` | `cowrie.login.success` |
| `2026-07-21 15:12:35` | `cowrie.direct-tcpip.request` |
| `2026-07-21 15:12:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.166.8[.]174` to AbuseIPDB if not already reported
- [ ] Block `60.166.8[.]174` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d70fcd94c84

| Field | Detail |
|---|---|
| **Source IP** | `81.22.51[.]64` |
| **First Seen** | 2026-07-21 15:18 |
| **Last Seen** | 2026-07-21 15:18 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 15:18:21` | `cowrie.session.connect` |
| `2026-07-21 15:18:21` | `cowrie.client.version` |
| `2026-07-21 15:18:21` | `cowrie.client.kex` |
| `2026-07-21 15:18:22` | `cowrie.login.success` |
| `2026-07-21 15:18:22` | `cowrie.direct-tcpip.request` |
| `2026-07-21 15:18:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.22.51[.]64` to AbuseIPDB if not already reported
- [ ] Block `81.22.51[.]64` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e47d1c48ef3e

| Field | Detail |
|---|---|
| **Source IP** | `78.187.9[.]111` |
| **First Seen** | 2026-07-21 15:18 |
| **Last Seen** | 2026-07-21 15:18 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 15:18:27` | `cowrie.session.connect` |
| `2026-07-21 15:18:27` | `cowrie.client.version` |
| `2026-07-21 15:18:27` | `cowrie.client.kex` |
| `2026-07-21 15:18:28` | `cowrie.login.success` |
| `2026-07-21 15:18:29` | `cowrie.direct-tcpip.request` |
| `2026-07-21 15:18:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `78.187.9[.]111` to AbuseIPDB if not already reported
- [ ] Block `78.187.9[.]111` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37ae53e20f16

| Field | Detail |
|---|---|
| **Source IP** | `59.93.36[.]136` |
| **First Seen** | 2026-07-21 15:18 |
| **Last Seen** | 2026-07-21 15:18 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 15:18:48` | `cowrie.session.connect` |
| `2026-07-21 15:18:49` | `cowrie.client.version` |
| `2026-07-21 15:18:49` | `cowrie.client.kex` |
| `2026-07-21 15:18:51` | `cowrie.login.success` |
| `2026-07-21 15:18:53` | `cowrie.direct-tcpip.request` |
| `2026-07-21 15:18:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.93.36[.]136` to AbuseIPDB if not already reported
- [ ] Block `59.93.36[.]136` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d173adbef2e

| Field | Detail |
|---|---|
| **Source IP** | `112.197.2[.]116` |
| **First Seen** | 2026-07-21 15:20 |
| **Last Seen** | 2026-07-21 15:20 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 15:20:26` | `cowrie.session.connect` |
| `2026-07-21 15:20:26` | `cowrie.client.version` |
| `2026-07-21 15:20:27` | `cowrie.client.kex` |
| `2026-07-21 15:20:27` | `cowrie.login.success` |
| `2026-07-21 15:20:28` | `cowrie.session.params` |
| `2026-07-21 15:20:28` | `cowrie.command.input` |
| `2026-07-21 15:20:29` | `cowrie.log.closed` |
| `2026-07-21 15:20:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.197.2[.]116` to AbuseIPDB if not already reported
- [ ] Block `112.197.2[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7eb25ea4dad5

| Field | Detail |
|---|---|
| **Source IP** | `218.4.156[.]254` |
| **First Seen** | 2026-07-21 15:22 |
| **Last Seen** | 2026-07-21 15:22 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 15:22:00` | `cowrie.session.connect` |
| `2026-07-21 15:22:02` | `cowrie.client.version` |
| `2026-07-21 15:22:02` | `cowrie.client.kex` |
| `2026-07-21 15:22:04` | `cowrie.login.success` |
| `2026-07-21 15:22:05` | `cowrie.direct-tcpip.request` |
| `2026-07-21 15:22:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.4.156[.]254` to AbuseIPDB if not already reported
- [ ] Block `218.4.156[.]254` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-940703fe623a

| Field | Detail |
|---|---|
| **Source IP** | `200.89.159[.]59` |
| **First Seen** | 2026-07-21 15:22 |
| **Last Seen** | 2026-07-21 15:22 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 15:22:11` | `cowrie.session.connect` |
| `2026-07-21 15:22:11` | `cowrie.client.version` |
| `2026-07-21 15:22:11` | `cowrie.client.kex` |
| `2026-07-21 15:22:13` | `cowrie.login.success` |
| `2026-07-21 15:22:13` | `cowrie.direct-tcpip.request` |
| `2026-07-21 15:22:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.89.159[.]59` to AbuseIPDB if not already reported
- [ ] Block `200.89.159[.]59` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6dd702d55349

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-21 15:24 |
| **Last Seen** | 2026-07-21 15:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 15:24:00` | `cowrie.session.connect` |
| `2026-07-21 15:24:00` | `cowrie.client.version` |
| `2026-07-21 15:24:00` | `cowrie.client.kex` |
| `2026-07-21 15:24:00` | `cowrie.login.success` |
| `2026-07-21 15:24:01` | `cowrie.direct-tcpip.request` |
| `2026-07-21 15:24:01` | `cowrie.direct-tcpip.data` |
| `2026-07-21 15:24:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b76352d46672

| Field | Detail |
|---|---|
| **Source IP** | `187.218.57[.]50` |
| **First Seen** | 2026-07-21 15:30 |
| **Last Seen** | 2026-07-21 15:31 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 15:30:57` | `cowrie.session.connect` |
| `2026-07-21 15:30:57` | `cowrie.client.version` |
| `2026-07-21 15:30:57` | `cowrie.client.kex` |
| `2026-07-21 15:30:58` | `cowrie.login.success` |
| `2026-07-21 15:30:59` | `cowrie.direct-tcpip.request` |
| `2026-07-21 15:31:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.218.57[.]50` to AbuseIPDB if not already reported
- [ ] Block `187.218.57[.]50` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3651f3ef58d7

| Field | Detail |
|---|---|
| **Source IP** | `178.178.222[.]60` |
| **First Seen** | 2026-07-21 15:31 |
| **Last Seen** | 2026-07-21 15:31 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 15:31:04` | `cowrie.session.connect` |
| `2026-07-21 15:31:04` | `cowrie.client.version` |
| `2026-07-21 15:31:04` | `cowrie.client.kex` |
| `2026-07-21 15:31:05` | `cowrie.login.success` |
| `2026-07-21 15:31:05` | `cowrie.direct-tcpip.request` |
| `2026-07-21 15:31:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.222[.]60` to AbuseIPDB if not already reported
- [ ] Block `178.178.222[.]60` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-229cdabc3092

| Field | Detail |
|---|---|
| **Source IP** | `183.89.208[.]174` |
| **First Seen** | 2026-07-21 15:33 |
| **Last Seen** | 2026-07-21 15:34 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 15:33:59` | `cowrie.session.connect` |
| `2026-07-21 15:34:00` | `cowrie.client.version` |
| `2026-07-21 15:34:00` | `cowrie.client.kex` |
| `2026-07-21 15:34:02` | `cowrie.login.success` |
| `2026-07-21 15:34:03` | `cowrie.direct-tcpip.request` |
| `2026-07-21 15:34:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.89.208[.]174` to AbuseIPDB if not already reported
- [ ] Block `183.89.208[.]174` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-770093bd404b

| Field | Detail |
|---|---|
| **Source IP** | `61.12.84[.]172` |
| **First Seen** | 2026-07-21 15:34 |
| **Last Seen** | 2026-07-21 15:34 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 15:34:09` | `cowrie.session.connect` |
| `2026-07-21 15:34:09` | `cowrie.client.version` |
| `2026-07-21 15:34:09` | `cowrie.client.kex` |
| `2026-07-21 15:34:11` | `cowrie.login.success` |
| `2026-07-21 15:34:12` | `cowrie.direct-tcpip.request` |
| `2026-07-21 15:34:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.12.84[.]172` to AbuseIPDB if not already reported
- [ ] Block `61.12.84[.]172` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae54d42d2516

| Field | Detail |
|---|---|
| **Source IP** | `173.249.52[.]138` |
| **First Seen** | 2026-07-21 15:36 |
| **Last Seen** | 2026-07-21 15:36 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 15:36:05` | `cowrie.session.connect` |
| `2026-07-21 15:36:05` | `cowrie.client.version` |
| `2026-07-21 15:36:06` | `cowrie.client.kex` |
| `2026-07-21 15:36:06` | `cowrie.login.success` |
| `2026-07-21 15:36:07` | `cowrie.session.params` |
| `2026-07-21 15:36:07` | `cowrie.command.input` |
| `2026-07-21 15:36:07` | `cowrie.command.failed` |
| `2026-07-21 15:36:07` | `cowrie.log.closed` |
| `2026-07-21 15:36:08` | `cowrie.session.params` |
| `2026-07-21 15:36:08` | `cowrie.command.input` |
| `2026-07-21 15:36:08` | `cowrie.session.file_download` |
| `2026-07-21 15:36:08` | `cowrie.log.closed` |
| `2026-07-21 15:36:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `173.249.52[.]138` to AbuseIPDB if not already reported
- [ ] Block `173.249.52[.]138` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9503cbd731d

| Field | Detail |
|---|---|
| **Source IP** | `173.249.52[.]138` |
| **First Seen** | 2026-07-21 15:36 |
| **Last Seen** | 2026-07-21 15:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 15:36:08` | `cowrie.session.connect` |
| `2026-07-21 15:36:08` | `cowrie.client.version` |
| `2026-07-21 15:36:08` | `cowrie.client.kex` |
| `2026-07-21 15:36:08` | `cowrie.login.success` |
| `2026-07-21 15:36:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `173.249.52[.]138` to AbuseIPDB if not already reported
- [ ] Block `173.249.52[.]138` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d726540d90d8

| Field | Detail |
|---|---|
| **Source IP** | `173.249.52[.]138` |
| **First Seen** | 2026-07-21 15:36 |
| **Last Seen** | 2026-07-21 15:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 15:36:09` | `cowrie.session.connect` |
| `2026-07-21 15:36:09` | `cowrie.client.version` |
| `2026-07-21 15:36:09` | `cowrie.client.kex` |
| `2026-07-21 15:36:09` | `cowrie.login.success` |
| `2026-07-21 15:36:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `173.249.52[.]138` to AbuseIPDB if not already reported
- [ ] Block `173.249.52[.]138` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b4552e79e4e

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-21 15:37 |
| **Last Seen** | 2026-07-21 15:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 15:37:54` | `cowrie.session.connect` |
| `2026-07-21 15:37:54` | `cowrie.client.version` |
| `2026-07-21 15:37:54` | `cowrie.client.kex` |
| `2026-07-21 15:37:54` | `cowrie.login.success` |
| `2026-07-21 15:37:55` | `cowrie.session.params` |
| `2026-07-21 15:37:55` | `cowrie.command.input` |
| `2026-07-21 15:37:55` | `cowrie.log.closed` |
| `2026-07-21 15:37:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4e881b14a6b

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-21 15:40 |
| **Last Seen** | 2026-07-21 15:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 15:40:17` | `cowrie.session.connect` |
| `2026-07-21 15:40:17` | `cowrie.client.version` |
| `2026-07-21 15:40:17` | `cowrie.client.kex` |
| `2026-07-21 15:40:17` | `cowrie.login.success` |
| `2026-07-21 15:40:17` | `cowrie.direct-tcpip.request` |
| `2026-07-21 15:40:17` | `cowrie.direct-tcpip.data` |
| `2026-07-21 15:40:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e36b8337942

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]91` |
| **First Seen** | 2026-07-21 15:42 |
| **Last Seen** | 2026-07-21 15:42 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST, /bin/busybox TEST, cat /proc, ./` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 15:42:05` | `cowrie.session.connect` |
| `2026-07-21 15:42:06` | `cowrie.login.success` |
| `2026-07-21 15:42:07` | `cowrie.session.params` |
| `2026-07-21 15:42:07` | `cowrie.command.input` |
| `2026-07-21 15:42:08` | `cowrie.command.input` |
| `2026-07-21 15:42:08` | `cowrie.command.input` |
| `2026-07-21 15:42:09` | `cowrie.command.input` |
| `2026-07-21 15:42:09` | `cowrie.command.failed` |
| `2026-07-21 15:42:10` | `cowrie.log.closed` |
| `2026-07-21 15:42:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]91` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d0bfb88d4ba

| Field | Detail |
|---|---|
| **Source IP** | `117.50.213[.]249` |
| **First Seen** | 2026-07-21 15:42 |
| **Last Seen** | 2026-07-21 15:47 |
| **Session Duration** | 300s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 15:42:20` | `cowrie.session.connect` |
| `2026-07-21 15:42:20` | `cowrie.client.version` |
| `2026-07-21 15:42:21` | `cowrie.client.kex` |
| `2026-07-21 15:42:24` | `cowrie.login.success` |
| `2026-07-21 15:47:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.50.213[.]249` to AbuseIPDB if not already reported
- [ ] Block `117.50.213[.]249` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53969fdbcbda

| Field | Detail |
|---|---|
| **Source IP** | `95.35.29[.]192` |
| **First Seen** | 2026-07-21 15:43 |
| **Last Seen** | 2026-07-21 15:43 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 15:43:10` | `cowrie.session.connect` |
| `2026-07-21 15:43:10` | `cowrie.client.version` |
| `2026-07-21 15:43:10` | `cowrie.client.kex` |
| `2026-07-21 15:43:12` | `cowrie.login.success` |
| `2026-07-21 15:43:12` | `cowrie.direct-tcpip.request` |
| `2026-07-21 15:43:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.35.29[.]192` to AbuseIPDB if not already reported
- [ ] Block `95.35.29[.]192` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5adc4b864b29

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-21 15:45 |
| **Last Seen** | 2026-07-21 15:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 15:45:20` | `cowrie.session.connect` |
| `2026-07-21 15:45:20` | `cowrie.client.version` |
| `2026-07-21 15:45:20` | `cowrie.client.kex` |
| `2026-07-21 15:45:20` | `cowrie.login.success` |
| `2026-07-21 15:45:21` | `cowrie.session.params` |
| `2026-07-21 15:45:21` | `cowrie.command.input` |
| `2026-07-21 15:45:21` | `cowrie.log.closed` |
| `2026-07-21 15:45:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb6aad7c2c7e

| Field | Detail |
|---|---|
| **Source IP** | `80.65.90[.]155` |
| **First Seen** | 2026-07-21 15:45 |
| **Last Seen** | 2026-07-21 15:45 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 15:45:33` | `cowrie.session.connect` |
| `2026-07-21 15:45:33` | `cowrie.client.version` |
| `2026-07-21 15:45:33` | `cowrie.client.kex` |
| `2026-07-21 15:45:34` | `cowrie.login.success` |
| `2026-07-21 15:45:34` | `cowrie.direct-tcpip.request` |
| `2026-07-21 15:45:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.65.90[.]155` to AbuseIPDB if not already reported
- [ ] Block `80.65.90[.]155` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36fb406c9851

| Field | Detail |
|---|---|
| **Source IP** | `219.144.16[.]16` |
| **First Seen** | 2026-07-21 15:45 |
| **Last Seen** | 2026-07-21 15:45 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 15:45:40` | `cowrie.session.connect` |
| `2026-07-21 15:45:43` | `cowrie.client.version` |
| `2026-07-21 15:45:43` | `cowrie.client.kex` |
| `2026-07-21 15:45:47` | `cowrie.login.success` |
| `2026-07-21 15:45:48` | `cowrie.direct-tcpip.request` |
| `2026-07-21 15:45:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `219.144.16[.]16` to AbuseIPDB if not already reported
- [ ] Block `219.144.16[.]16` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3b6b413c6ac

| Field | Detail |
|---|---|
| **Source IP** | `114.98.63[.]18` |
| **First Seen** | 2026-07-21 15:46 |
| **Last Seen** | 2026-07-21 15:46 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 15:46:44` | `cowrie.session.connect` |
| `2026-07-21 15:46:46` | `cowrie.client.version` |
| `2026-07-21 15:46:46` | `cowrie.client.kex` |
| `2026-07-21 15:46:48` | `cowrie.login.success` |
| `2026-07-21 15:46:49` | `cowrie.direct-tcpip.request` |
| `2026-07-21 15:46:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.98.63[.]18` to AbuseIPDB if not already reported
- [ ] Block `114.98.63[.]18` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30cbb76fd007

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-21 15:54 |
| **Last Seen** | 2026-07-21 15:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 15:54:14` | `cowrie.session.connect` |
| `2026-07-21 15:54:14` | `cowrie.client.version` |
| `2026-07-21 15:54:14` | `cowrie.client.kex` |
| `2026-07-21 15:54:14` | `cowrie.login.success` |
| `2026-07-21 15:54:14` | `cowrie.direct-tcpip.request` |
| `2026-07-21 15:54:14` | `cowrie.direct-tcpip.data` |
| `2026-07-21 15:54:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5da6a8f785e6

| Field | Detail |
|---|---|
| **Source IP** | `136.56.34[.]147` |
| **First Seen** | 2026-07-21 15:55 |
| **Last Seen** | 2026-07-21 15:56 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 15:55:58` | `cowrie.session.connect` |
| `2026-07-21 15:55:59` | `cowrie.client.version` |
| `2026-07-21 15:55:59` | `cowrie.client.kex` |
| `2026-07-21 15:56:00` | `cowrie.login.success` |
| `2026-07-21 15:56:00` | `cowrie.direct-tcpip.request` |
| `2026-07-21 15:56:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `136.56.34[.]147` to AbuseIPDB if not already reported
- [ ] Block `136.56.34[.]147` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a2db7659763

| Field | Detail |
|---|---|
| **Source IP** | `49.124.151[.]15` |
| **First Seen** | 2026-07-21 15:56 |
| **Last Seen** | 2026-07-21 15:56 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 15:56:11` | `cowrie.session.connect` |
| `2026-07-21 15:56:11` | `cowrie.client.version` |
| `2026-07-21 15:56:11` | `cowrie.client.kex` |
| `2026-07-21 15:56:13` | `cowrie.login.success` |
| `2026-07-21 15:56:14` | `cowrie.direct-tcpip.request` |
| `2026-07-21 15:56:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.151[.]15` to AbuseIPDB if not already reported
- [ ] Block `49.124.151[.]15` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7643e1801cb

| Field | Detail |
|---|---|
| **Source IP** | `179.185.227[.]77` |
| **First Seen** | 2026-07-21 15:59 |
| **Last Seen** | 2026-07-21 15:59 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 15:59:15` | `cowrie.session.connect` |
| `2026-07-21 15:59:16` | `cowrie.client.version` |
| `2026-07-21 15:59:16` | `cowrie.client.kex` |
| `2026-07-21 15:59:17` | `cowrie.login.success` |
| `2026-07-21 15:59:18` | `cowrie.direct-tcpip.request` |
| `2026-07-21 15:59:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.185.227[.]77` to AbuseIPDB if not already reported
- [ ] Block `179.185.227[.]77` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb62a7ce7887

| Field | Detail |
|---|---|
| **Source IP** | `50.217.40[.]11` |
| **First Seen** | 2026-07-21 16:02 |
| **Last Seen** | 2026-07-21 16:02 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 16:02:12` | `cowrie.session.connect` |
| `2026-07-21 16:02:12` | `cowrie.client.version` |
| `2026-07-21 16:02:12` | `cowrie.client.kex` |
| `2026-07-21 16:02:13` | `cowrie.login.success` |
| `2026-07-21 16:02:13` | `cowrie.direct-tcpip.request` |
| `2026-07-21 16:02:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.217.40[.]11` to AbuseIPDB if not already reported
- [ ] Block `50.217.40[.]11` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a401fbde4e13

| Field | Detail |
|---|---|
| **Source IP** | `146.190.215[.]195` |
| **First Seen** | 2026-07-21 16:02 |
| **Last Seen** | 2026-07-21 16:02 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 16:02:18` | `cowrie.session.connect` |
| `2026-07-21 16:02:18` | `cowrie.client.version` |
| `2026-07-21 16:02:18` | `cowrie.client.kex` |
| `2026-07-21 16:02:19` | `cowrie.login.success` |
| `2026-07-21 16:02:19` | `cowrie.direct-tcpip.request` |
| `2026-07-21 16:02:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `146.190.215[.]195` to AbuseIPDB if not already reported
- [ ] Block `146.190.215[.]195` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de0a0a9695e7

| Field | Detail |
|---|---|
| **Source IP** | `185.113.9[.]199` |
| **First Seen** | 2026-07-21 16:05 |
| **Last Seen** | 2026-07-21 16:10 |
| **Session Duration** | 305s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 16:05:39` | `cowrie.session.connect` |
| `2026-07-21 16:05:39` | `cowrie.client.version` |
| `2026-07-21 16:05:40` | `cowrie.client.kex` |
| `2026-07-21 16:05:45` | `cowrie.login.success` |
| `2026-07-21 16:10:45` | `cowrie.session.file_upload` |
| `2026-07-21 16:10:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.113.9[.]199` to AbuseIPDB if not already reported
- [ ] Block `185.113.9[.]199` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dfa924bc4f9e

| Field | Detail |
|---|---|
| **Source IP** | `14.54.22[.]11` |
| **First Seen** | 2026-07-21 16:05 |
| **Last Seen** | 2026-07-21 16:05 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 16:05:43` | `cowrie.session.connect` |
| `2026-07-21 16:05:44` | `cowrie.client.version` |
| `2026-07-21 16:05:44` | `cowrie.client.kex` |
| `2026-07-21 16:05:46` | `cowrie.login.success` |
| `2026-07-21 16:05:47` | `cowrie.direct-tcpip.request` |
| `2026-07-21 16:05:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.54.22[.]11` to AbuseIPDB if not already reported
- [ ] Block `14.54.22[.]11` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b86ec04ee74

| Field | Detail |
|---|---|
| **Source IP** | `81.195.152[.]14` |
| **First Seen** | 2026-07-21 16:05 |
| **Last Seen** | 2026-07-21 16:05 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 16:05:52` | `cowrie.session.connect` |
| `2026-07-21 16:05:53` | `cowrie.client.version` |
| `2026-07-21 16:05:53` | `cowrie.client.kex` |
| `2026-07-21 16:05:54` | `cowrie.login.success` |
| `2026-07-21 16:05:55` | `cowrie.direct-tcpip.request` |
| `2026-07-21 16:05:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.195.152[.]14` to AbuseIPDB if not already reported
- [ ] Block `81.195.152[.]14` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-846529604568

| Field | Detail |
|---|---|
| **Source IP** | `185.40.122[.]250` |
| **First Seen** | 2026-07-21 16:08 |
| **Last Seen** | 2026-07-21 16:08 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 16:08:15` | `cowrie.session.connect` |
| `2026-07-21 16:08:15` | `cowrie.client.version` |
| `2026-07-21 16:08:15` | `cowrie.client.kex` |
| `2026-07-21 16:08:17` | `cowrie.login.success` |
| `2026-07-21 16:08:18` | `cowrie.direct-tcpip.request` |
| `2026-07-21 16:08:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.40.122[.]250` to AbuseIPDB if not already reported
- [ ] Block `185.40.122[.]250` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a9af919996e

| Field | Detail |
|---|---|
| **Source IP** | `116.113.241[.]82` |
| **First Seen** | 2026-07-21 16:08 |
| **Last Seen** | 2026-07-21 16:09 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 16:08:53` | `cowrie.session.connect` |
| `2026-07-21 16:08:54` | `cowrie.client.version` |
| `2026-07-21 16:08:54` | `cowrie.client.kex` |
| `2026-07-21 16:08:56` | `cowrie.login.success` |
| `2026-07-21 16:08:57` | `cowrie.direct-tcpip.request` |
| `2026-07-21 16:09:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.113.241[.]82` to AbuseIPDB if not already reported
- [ ] Block `116.113.241[.]82` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d55f83a073c0

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-21 16:08 |
| **Last Seen** | 2026-07-21 16:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 16:08:54` | `cowrie.session.connect` |
| `2026-07-21 16:08:54` | `cowrie.client.version` |
| `2026-07-21 16:08:54` | `cowrie.client.kex` |
| `2026-07-21 16:08:55` | `cowrie.login.success` |
| `2026-07-21 16:08:55` | `cowrie.direct-tcpip.request` |
| `2026-07-21 16:08:55` | `cowrie.direct-tcpip.data` |
| `2026-07-21 16:08:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c67382425e6

| Field | Detail |
|---|---|
| **Source IP** | `85.19.195[.]12` |
| **First Seen** | 2026-07-21 16:09 |
| **Last Seen** | 2026-07-21 16:09 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 16:09:03` | `cowrie.session.connect` |
| `2026-07-21 16:09:03` | `cowrie.client.version` |
| `2026-07-21 16:09:03` | `cowrie.client.kex` |
| `2026-07-21 16:09:04` | `cowrie.login.success` |
| `2026-07-21 16:09:05` | `cowrie.direct-tcpip.request` |
| `2026-07-21 16:09:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.19.195[.]12` to AbuseIPDB if not already reported
- [ ] Block `85.19.195[.]12` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8536b2d4d2ba

| Field | Detail |
|---|---|
| **Source IP** | `212.68.38[.]69` |
| **First Seen** | 2026-07-21 16:24 |
| **Last Seen** | 2026-07-21 16:24 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 16:24:12` | `cowrie.session.connect` |
| `2026-07-21 16:24:12` | `cowrie.client.version` |
| `2026-07-21 16:24:12` | `cowrie.client.kex` |
| `2026-07-21 16:24:14` | `cowrie.login.success` |
| `2026-07-21 16:24:14` | `cowrie.direct-tcpip.request` |
| `2026-07-21 16:24:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.68.38[.]69` to AbuseIPDB if not already reported
- [ ] Block `212.68.38[.]69` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f99039d63b0a

| Field | Detail |
|---|---|
| **Source IP** | `218.13.214[.]18` |
| **First Seen** | 2026-07-21 16:24 |
| **Last Seen** | 2026-07-21 16:24 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 16:24:23` | `cowrie.session.connect` |
| `2026-07-21 16:24:25` | `cowrie.client.version` |
| `2026-07-21 16:24:25` | `cowrie.client.kex` |
| `2026-07-21 16:24:27` | `cowrie.login.success` |
| `2026-07-21 16:24:28` | `cowrie.direct-tcpip.request` |
| `2026-07-21 16:24:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.13.214[.]18` to AbuseIPDB if not already reported
- [ ] Block `218.13.214[.]18` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b06f2b57f080

| Field | Detail |
|---|---|
| **Source IP** | `103.68.22[.]115` |
| **First Seen** | 2026-07-21 16:28 |
| **Last Seen** | 2026-07-21 16:29 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 16:28:56` | `cowrie.session.connect` |
| `2026-07-21 16:28:57` | `cowrie.client.version` |
| `2026-07-21 16:28:57` | `cowrie.client.kex` |
| `2026-07-21 16:28:59` | `cowrie.login.success` |
| `2026-07-21 16:29:00` | `cowrie.direct-tcpip.request` |
| `2026-07-21 16:29:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.68.22[.]115` to AbuseIPDB if not already reported
- [ ] Block `103.68.22[.]115` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89d82891ea29

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-21 16:30 |
| **Last Seen** | 2026-07-21 16:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 16:30:06` | `cowrie.session.connect` |
| `2026-07-21 16:30:06` | `cowrie.client.version` |
| `2026-07-21 16:30:06` | `cowrie.client.kex` |
| `2026-07-21 16:30:06` | `cowrie.login.success` |
| `2026-07-21 16:30:07` | `cowrie.session.params` |
| `2026-07-21 16:30:07` | `cowrie.command.input` |
| `2026-07-21 16:30:07` | `cowrie.log.closed` |
| `2026-07-21 16:30:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83d010607698

| Field | Detail |
|---|---|
| **Source IP** | `123.52.202[.]92` |
| **First Seen** | 2026-07-21 16:32 |
| **Last Seen** | 2026-07-21 16:32 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 16:32:44` | `cowrie.session.connect` |
| `2026-07-21 16:32:46` | `cowrie.client.version` |
| `2026-07-21 16:32:46` | `cowrie.client.kex` |
| `2026-07-21 16:32:49` | `cowrie.login.success` |
| `2026-07-21 16:32:50` | `cowrie.direct-tcpip.request` |
| `2026-07-21 16:32:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `123.52.202[.]92` to AbuseIPDB if not already reported
- [ ] Block `123.52.202[.]92` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7dfc6f6da66

| Field | Detail |
|---|---|
| **Source IP** | `203.252.10[.]4` |
| **First Seen** | 2026-07-21 16:32 |
| **Last Seen** | 2026-07-21 16:33 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 16:32:55` | `cowrie.session.connect` |
| `2026-07-21 16:32:56` | `cowrie.client.version` |
| `2026-07-21 16:32:56` | `cowrie.client.kex` |
| `2026-07-21 16:32:58` | `cowrie.login.success` |
| `2026-07-21 16:32:59` | `cowrie.direct-tcpip.request` |
| `2026-07-21 16:33:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.252.10[.]4` to AbuseIPDB if not already reported
- [ ] Block `203.252.10[.]4` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-418d6417311d

| Field | Detail |
|---|---|
| **Source IP** | `198.98.56[.]227` |
| **First Seen** | 2026-07-21 16:34 |
| **Last Seen** | 2026-07-21 16:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 16:34:27` | `cowrie.session.connect` |
| `2026-07-21 16:34:27` | `cowrie.client.version` |
| `2026-07-21 16:34:27` | `cowrie.client.kex` |
| `2026-07-21 16:34:27` | `cowrie.login.success` |
| `2026-07-21 16:34:28` | `cowrie.session.params` |
| `2026-07-21 16:34:28` | `cowrie.command.input` |
| `2026-07-21 16:34:28` | `cowrie.command.failed` |
| `2026-07-21 16:34:28` | `cowrie.log.closed` |
| `2026-07-21 16:34:28` | `cowrie.session.params` |
| `2026-07-21 16:34:28` | `cowrie.command.input` |
| `2026-07-21 16:34:28` | `cowrie.session.file_download` |
| `2026-07-21 16:34:28` | `cowrie.log.closed` |
| `2026-07-21 16:34:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `198.98.56[.]227` to AbuseIPDB if not already reported
- [ ] Block `198.98.56[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1418a5c44ee4

| Field | Detail |
|---|---|
| **Source IP** | `198.98.56[.]227` |
| **First Seen** | 2026-07-21 16:34 |
| **Last Seen** | 2026-07-21 16:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 16:34:28` | `cowrie.session.connect` |
| `2026-07-21 16:34:28` | `cowrie.client.version` |
| `2026-07-21 16:34:28` | `cowrie.client.kex` |
| `2026-07-21 16:34:29` | `cowrie.login.success` |
| `2026-07-21 16:34:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `198.98.56[.]227` to AbuseIPDB if not already reported
- [ ] Block `198.98.56[.]227` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1231599a9428

| Field | Detail |
|---|---|
| **Source IP** | `198.98.56[.]227` |
| **First Seen** | 2026-07-21 16:34 |
| **Last Seen** | 2026-07-21 16:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 16:34:29` | `cowrie.session.connect` |
| `2026-07-21 16:34:29` | `cowrie.client.version` |
| `2026-07-21 16:34:29` | `cowrie.client.kex` |
| `2026-07-21 16:34:29` | `cowrie.login.success` |
| `2026-07-21 16:34:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `198.98.56[.]227` to AbuseIPDB if not already reported
- [ ] Block `198.98.56[.]227` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5705c760a0e5

| Field | Detail |
|---|---|
| **Source IP** | `124.133.10[.]66` |
| **First Seen** | 2026-07-21 16:36 |
| **Last Seen** | 2026-07-21 16:36 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 16:36:10` | `cowrie.session.connect` |
| `2026-07-21 16:36:10` | `cowrie.client.version` |
| `2026-07-21 16:36:10` | `cowrie.client.kex` |
| `2026-07-21 16:36:12` | `cowrie.login.success` |
| `2026-07-21 16:36:13` | `cowrie.direct-tcpip.request` |
| `2026-07-21 16:36:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.133.10[.]66` to AbuseIPDB if not already reported
- [ ] Block `124.133.10[.]66` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-925f9b124429

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]60` |
| **First Seen** | 2026-07-21 16:37 |
| **Last Seen** | 2026-07-21 16:37 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 16:37:14` | `cowrie.session.connect` |
| `2026-07-21 16:37:17` | `cowrie.login.success` |
| `2026-07-21 16:37:18` | `cowrie.session.params` |
| `2026-07-21 16:37:20` | `cowrie.log.closed` |
| `2026-07-21 16:37:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]60` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]60` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8bf82018f936

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-21 16:37 |
| **Last Seen** | 2026-07-21 16:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 16:37:28` | `cowrie.session.connect` |
| `2026-07-21 16:37:28` | `cowrie.client.version` |
| `2026-07-21 16:37:28` | `cowrie.client.kex` |
| `2026-07-21 16:37:28` | `cowrie.login.success` |
| `2026-07-21 16:37:29` | `cowrie.session.params` |
| `2026-07-21 16:37:29` | `cowrie.command.input` |
| `2026-07-21 16:37:29` | `cowrie.log.closed` |
| `2026-07-21 16:37:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d47e3fe26bba

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-07-21 16:40 |
| **Last Seen** | 2026-07-21 16:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 16:40:22` | `cowrie.session.connect` |
| `2026-07-21 16:40:22` | `cowrie.client.version` |
| `2026-07-21 16:40:22` | `cowrie.client.kex` |
| `2026-07-21 16:40:22` | `cowrie.login.success` |
| `2026-07-21 16:40:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2dc5edce2be3

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-07-21 16:40 |
| **Last Seen** | 2026-07-21 16:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 16:40:24` | `cowrie.session.connect` |
| `2026-07-21 16:40:24` | `cowrie.client.version` |
| `2026-07-21 16:40:24` | `cowrie.client.kex` |
| `2026-07-21 16:40:24` | `cowrie.login.success` |
| `2026-07-21 16:40:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00ef991be460

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-07-21 16:40 |
| **Last Seen** | 2026-07-21 16:42 |
| **Session Duration** | 126s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 16:40:45` | `cowrie.session.connect` |
| `2026-07-21 16:40:45` | `cowrie.client.version` |
| `2026-07-21 16:40:45` | `cowrie.client.kex` |
| `2026-07-21 16:40:45` | `cowrie.login.success` |
| `2026-07-21 16:40:46` | `cowrie.session.file_upload` |
| `2026-07-21 16:40:47` | `cowrie.session.params` |
| `2026-07-21 16:40:47` | `cowrie.command.input` |
| `2026-07-21 16:40:47` | `cowrie.command.input` |
| `2026-07-21 16:40:47` | `cowrie.command.input` |
| `2026-07-21 16:40:47` | `cowrie.command.failed` |
| `2026-07-21 16:40:47` | `cowrie.log.closed` |
| `2026-07-21 16:40:48` | `cowrie.session.params` |
| `2026-07-21 16:40:48` | `cowrie.command.input` |
| `2026-07-21 16:40:48` | `cowrie.log.closed` |
| `2026-07-21 16:40:48` | `cowrie.session.params` |
| `2026-07-21 16:40:48` | `cowrie.command.input` |
| `2026-07-21 16:40:49` | `cowrie.log.closed` |
| `2026-07-21 16:40:49` | `cowrie.session.params` |
| `2026-07-21 16:40:49` | `cowrie.command.input` |
| `2026-07-21 16:40:49` | `cowrie.command.failed` |
| `2026-07-21 16:40:49` | `cowrie.command.failed` |
| `2026-07-21 16:41:50` | `cowrie.session.params` |
| `2026-07-21 16:41:50` | `cowrie.command.input` |
| `2026-07-21 16:42:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe12b6558b2e

| Field | Detail |
|---|---|
| **Source IP** | `94.183.188[.]148` |
| **First Seen** | 2026-07-21 16:40 |
| **Last Seen** | 2026-07-21 16:41 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 16:40:49` | `cowrie.session.connect` |
| `2026-07-21 16:40:50` | `cowrie.client.version` |
| `2026-07-21 16:40:50` | `cowrie.client.kex` |
| `2026-07-21 16:40:52` | `cowrie.login.success` |
| `2026-07-21 16:40:54` | `cowrie.session.params` |
| `2026-07-21 16:40:54` | `cowrie.command.input` |
| `2026-07-21 16:40:54` | `cowrie.command.failed` |
| `2026-07-21 16:40:56` | `cowrie.log.closed` |
| `2026-07-21 16:40:57` | `cowrie.session.params` |
| `2026-07-21 16:40:57` | `cowrie.command.input` |
| `2026-07-21 16:40:57` | `cowrie.session.file_download` |
| `2026-07-21 16:40:57` | `cowrie.log.closed` |
| `2026-07-21 16:41:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.183.188[.]148` to AbuseIPDB if not already reported
- [ ] Block `94.183.188[.]148` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11b36f0f1067

| Field | Detail |
|---|---|
| **Source IP** | `94.183.188[.]148` |
| **First Seen** | 2026-07-21 16:40 |
| **Last Seen** | 2026-07-21 16:41 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 16:40:57` | `cowrie.session.connect` |
| `2026-07-21 16:40:57` | `cowrie.client.version` |
| `2026-07-21 16:40:58` | `cowrie.client.kex` |
| `2026-07-21 16:41:00` | `cowrie.login.success` |
| `2026-07-21 16:41:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.183.188[.]148` to AbuseIPDB if not already reported
- [ ] Block `94.183.188[.]148` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-484343f44a08

| Field | Detail |
|---|---|
| **Source IP** | `94.183.188[.]148` |
| **First Seen** | 2026-07-21 16:41 |
| **Last Seen** | 2026-07-21 16:41 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 16:41:01` | `cowrie.session.connect` |
| `2026-07-21 16:41:03` | `cowrie.client.version` |
| `2026-07-21 16:41:03` | `cowrie.client.kex` |
| `2026-07-21 16:41:05` | `cowrie.login.success` |
| `2026-07-21 16:41:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.183.188[.]148` to AbuseIPDB if not already reported
- [ ] Block `94.183.188[.]148` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-388cbd21a5fc

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-07-21 16:43 |
| **Last Seen** | 2026-07-21 16:45 |
| **Session Duration** | 126s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 16:43:06` | `cowrie.session.connect` |
| `2026-07-21 16:43:06` | `cowrie.client.version` |
| `2026-07-21 16:43:06` | `cowrie.client.kex` |
| `2026-07-21 16:43:06` | `cowrie.login.success` |
| `2026-07-21 16:43:07` | `cowrie.session.file_upload` |
| `2026-07-21 16:43:08` | `cowrie.session.params` |
| `2026-07-21 16:43:08` | `cowrie.command.input` |
| `2026-07-21 16:43:08` | `cowrie.command.input` |
| `2026-07-21 16:43:08` | `cowrie.command.input` |
| `2026-07-21 16:43:08` | `cowrie.command.failed` |
| `2026-07-21 16:43:08` | `cowrie.log.closed` |
| `2026-07-21 16:43:09` | `cowrie.session.params` |
| `2026-07-21 16:43:09` | `cowrie.command.input` |
| `2026-07-21 16:43:09` | `cowrie.log.closed` |
| `2026-07-21 16:43:10` | `cowrie.session.params` |
| `2026-07-21 16:43:10` | `cowrie.command.input` |
| `2026-07-21 16:43:10` | `cowrie.log.closed` |
| `2026-07-21 16:43:11` | `cowrie.session.params` |
| `2026-07-21 16:43:11` | `cowrie.command.input` |
| `2026-07-21 16:43:11` | `cowrie.command.failed` |
| `2026-07-21 16:43:11` | `cowrie.command.failed` |
| `2026-07-21 16:44:12` | `cowrie.session.params` |
| `2026-07-21 16:44:12` | `cowrie.command.input` |
| `2026-07-21 16:45:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da937196048b

| Field | Detail |
|---|---|
| **Source IP** | `218.29.231[.]106` |
| **First Seen** | 2026-07-21 16:45 |
| **Last Seen** | 2026-07-21 16:45 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 16:45:35` | `cowrie.session.connect` |
| `2026-07-21 16:45:36` | `cowrie.client.version` |
| `2026-07-21 16:45:36` | `cowrie.client.kex` |
| `2026-07-21 16:45:38` | `cowrie.login.success` |
| `2026-07-21 16:45:39` | `cowrie.direct-tcpip.request` |
| `2026-07-21 16:45:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.29.231[.]106` to AbuseIPDB if not already reported
- [ ] Block `218.29.231[.]106` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba1352dc73ac

| Field | Detail |
|---|---|
| **Source IP** | `101.13.5[.]49` |
| **First Seen** | 2026-07-21 16:45 |
| **Last Seen** | 2026-07-21 16:46 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 16:45:49` | `cowrie.session.connect` |
| `2026-07-21 16:45:50` | `cowrie.client.version` |
| `2026-07-21 16:45:50` | `cowrie.client.kex` |
| `2026-07-21 16:45:54` | `cowrie.login.success` |
| `2026-07-21 16:45:56` | `cowrie.direct-tcpip.request` |
| `2026-07-21 16:46:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.13.5[.]49` to AbuseIPDB if not already reported
- [ ] Block `101.13.5[.]49` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-097c2fcaedad

| Field | Detail |
|---|---|
| **Source IP** | `71.229.1[.]186` |
| **First Seen** | 2026-07-21 16:48 |
| **Last Seen** | 2026-07-21 16:48 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 16:48:24` | `cowrie.session.connect` |
| `2026-07-21 16:48:25` | `cowrie.client.version` |
| `2026-07-21 16:48:25` | `cowrie.client.kex` |
| `2026-07-21 16:48:26` | `cowrie.login.success` |
| `2026-07-21 16:48:26` | `cowrie.direct-tcpip.request` |
| `2026-07-21 16:48:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `71.229.1[.]186` to AbuseIPDB if not already reported
- [ ] Block `71.229.1[.]186` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d64f1a67fb4

| Field | Detail |
|---|---|
| **Source IP** | `150.228.187[.]139` |
| **First Seen** | 2026-07-21 16:48 |
| **Last Seen** | 2026-07-21 16:48 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 16:48:36` | `cowrie.session.connect` |
| `2026-07-21 16:48:37` | `cowrie.client.version` |
| `2026-07-21 16:48:37` | `cowrie.client.kex` |
| `2026-07-21 16:48:39` | `cowrie.login.success` |
| `2026-07-21 16:48:40` | `cowrie.direct-tcpip.request` |
| `2026-07-21 16:48:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `150.228.187[.]139` to AbuseIPDB if not already reported
- [ ] Block `150.228.187[.]139` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `14.103.117[.]142` | **26** | 2026-07-21 13:07 | 2026-07-21 15:59 | 48m | 0 | `T1592` | 🟠 MEDIUM |
| `139.199.80[.]137` | **9** | 2026-07-21 13:18 | 2026-07-21 16:49 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.227.254[.]156` | **6** | 2026-07-21 15:06 | 2026-07-21 16:26 | 0m | 0 | `T1592` | 🟢 LOW |
| `51.158.205[.]203` | **6** | 2026-07-21 13:44 | 2026-07-21 13:49 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.19.117[.]129` | **4** | 2026-07-21 13:13 | 2026-07-21 16:10 | 0m | 8 | `T1110.001 · T1592` | 🟢 LOW |
| `172.105.128[.]11` | **3** | 2026-07-21 13:38 | 2026-07-21 13:38 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]163` | **3** | 2026-07-21 13:39 | 2026-07-21 13:39 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]164` | **3** | 2026-07-21 14:12 | 2026-07-21 14:12 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]143` | **3** | 2026-07-21 16:54 | 2026-07-21 16:54 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]193` | **3** | 2026-07-21 13:59 | 2026-07-21 13:59 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]184` | **3** | 2026-07-21 16:54 | 2026-07-21 16:54 | 0m | 0 | `T1592` | 🟢 LOW |
| `88.214.25[.]121` | **3** | 2026-07-21 15:28 | 2026-07-21 15:28 | 0m | 0 | `T1592` | 🟢 LOW |
| `172.210.9[.]231` | **2** | 2026-07-21 14:57 | 2026-07-21 14:57 | 0m | 0 | `T1592` | 🟢 LOW |
| `47.254.230[.]85` | **2** | 2026-07-21 13:12 | 2026-07-21 13:12 | 0m | 0 | `T1592` | 🟢 LOW |
| `64.89.162[.]15` | **2** | 2026-07-21 13:52 | 2026-07-21 13:52 | 0m | 0 | `T1592` | 🟢 LOW |
| `64.89.162[.]15` | **2** | 2026-07-21 15:54 | 2026-07-21 16:09 | 0m | 0 | `T1592` | 🟢 LOW |
| `90.224.175[.]26` | **2** | 2026-07-21 16:40 | 2026-07-21 16:41 | 0m | 0 | `T1592` | 🟢 LOW |
| `103.182.234[.]231` | 1 | 2026-07-21 13:03 | 2026-07-21 13:05 | 120s | 0 | `T1592` | 🟢 LOW |
| `104.152.52[.]240` | 1 | 2026-07-21 15:16 | 2026-07-21 15:16 | 0s | 0 | `T1592` | 🟢 LOW |
| `106.228.31[.]216` | 1 | 2026-07-21 13:11 | 2026-07-21 13:11 | 12s | 0 | `T1592` | 🟢 LOW |
| `111.36.57[.]69` | 1 | 2026-07-21 13:52 | 2026-07-21 13:52 | 1s | 0 | `T1592` | 🟢 LOW |
| `115.86.227[.]79` | 1 | 2026-07-21 13:17 | 2026-07-21 13:17 | 0s | 0 | `T1592` | 🟢 LOW |
| `115.86.227[.]79` | 1 | 2026-07-21 16:08 | 2026-07-21 16:08 | 0s | 0 | `T1592` | 🟢 LOW |
| `117.70.94[.]155` | 1 | 2026-07-21 14:19 | 2026-07-21 14:19 | 7s | 0 | `T1592` | 🟢 LOW |
| `120.48.17[.]175` | 1 | 2026-07-21 14:49 | 2026-07-21 14:49 | 10s | 0 | `T1592` | 🟢 LOW |
| `122.155.174[.]20` | 1 | 2026-07-21 15:46 | 2026-07-21 15:46 | 30s | 0 | `T1592` | 🟢 LOW |
| `173.255.221[.]189` | 1 | 2026-07-21 13:36 | 2026-07-21 13:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `180.76.172[.]156` | 1 | 2026-07-21 13:31 | 2026-07-21 13:33 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.171.15[.]149` | 1 | 2026-07-21 15:37 | 2026-07-21 15:37 | 2s | 0 | `T1592` | 🟢 LOW |
| `212.8.242[.]38` | 1 | 2026-07-21 15:29 | 2026-07-21 15:30 | 31s | 0 | `T1592` | 🟢 LOW |
| `213.66.197[.]199` | 1 | 2026-07-21 16:36 | 2026-07-21 16:38 | 120s | 0 | `T1592` | 🟢 LOW |
| `219.144.16[.]16` | 1 | 2026-07-21 16:02 | 2026-07-21 16:04 | 120s | 0 | `T1592` | 🟢 LOW |
| `222.139.245[.]137` | 1 | 2026-07-21 14:08 | 2026-07-21 14:08 | 3s | 0 | `T1592` | 🟢 LOW |
| `27.204.236[.]176` | 1 | 2026-07-21 15:23 | 2026-07-21 15:24 | 13s | 0 | `T1592` | 🟢 LOW |
| `37.238.45[.]202` | 1 | 2026-07-21 16:24 | 2026-07-21 16:24 | 8s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]151` | 1 | 2026-07-21 16:07 | 2026-07-21 16:07 | 0s | 0 | `T1592` | 🟢 LOW |
| `52.142.44[.]95` | 1 | 2026-07-21 13:49 | 2026-07-21 13:51 | 120s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]179` | 1 | 2026-07-21 14:49 | 2026-07-21 14:49 | 16s | 0 | `T1592` | 🟢 LOW |
| `66.228.62[.]150` | 1 | 2026-07-21 14:35 | 2026-07-21 14:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.240.223[.]208` | 1 | 2026-07-21 15:01 | 2026-07-21 15:01 | 10s | 0 | `T1592` | 🟢 LOW |
| `94.154.43[.]164` | 1 | 2026-07-21 13:22 | 2026-07-21 13:22 | 0s | 0 | `T1592` | 🟢 LOW |
| `94.154.43[.]60` | 1 | 2026-07-21 16:37 | 2026-07-21 16:37 | 5s | 1 | `T1110.001` | 🟢 LOW |
| `94.154.43[.]91` | 1 | 2026-07-21 15:42 | 2026-07-21 15:42 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 42/100 | 🟡 MEDIUM | **32/74** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/74** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **17/74** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **24/74** 🔴 |
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
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `31d4181843b1ed10a7e7cb3f108f6d6c50a7a4452ee52ddacabe8ca77260615e` | Bash Script | `31d4181843b1ed10...` | 60/100 | 🟡 MEDIUM | **26/74** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 65/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 86/100 | 🔴 HIGH | **40/74** 🔴 |
| `40db9279ba409757c074048529be5bf8f141fa022489a965792e7f7de2223b78` | ELF Binary (Linux executable) (ARM 32-bit) | `40db9279ba409757...` | 62/100 | 🟡 MEDIUM | **32/74** 🔴 |
| `44689d3e1a7f460db2ecc14351c171f4910721257f83024c63cbc07f4e2b977c` | ELF Binary (Linux executable) (x86-64 64-bit) | `44689d3e1a7f460d...` | 35/100 | 🟢 LOW | **13/74** 🔴 |
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 51/100 | 🟡 MEDIUM | **29/74** 🔴 |
| `4756c00dfa749f3fdf3a687a464632d692da370fd159c78b3ed70cad32192555` | ELF Binary (Linux executable) (ARM 32-bit) | `4756c00dfa749f3f...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `47b268c21591069bfe4099833ad66b8138a53ab2dcb866e040d466aee1f8624c` | ELF Binary (Linux executable) (x86-64 64-bit) | `47b268c21591069b...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `494ab0439cd9a373aca71bf5107e0718a9e14b9b805632835c99c42b88a50984` | ELF Binary (Linux executable) (x86 32-bit) | `494ab0439cd9a373...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `51228996cf0280efc9b4c45d499e8527029667335b7b26951990feac7f22595a` | ELF Binary (Linux executable) (x86 32-bit) | `51228996cf0280ef...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `526c830542c17e6883da850de8dc2c3c2ffc35b446f33c61892b193e50f8d8ed` | ELF Binary (Linux executable) (x86-64 64-bit) | `526c830542c17e68...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `5348b12f049d86c5306ad9ea227b8483155183cb2a535c25b5c587c4c2491923` | ELF Binary (Linux executable) (x86-64 64-bit) | `5348b12f049d86c5...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `5850b6e589ea496b093b3c162dab126789ea118276bc3c23ff4cf75c6c19c8d5` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `5850b6e589ea496b...` | 52/100 | 🟡 MEDIUM | **30/74** 🔴 |
| `59691617d4c9bfe4a9202c318e632faa7c8a2d5dfdb46297e27c1a33971f3530` | ELF Binary (Linux executable) (unknown (e_machine=0x2a) 32-bit) | `59691617d4c9bfe4...` | 54/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `59b756899825573563cd53ae62bcd1f703a765f85797c352964e5246f04a85c0` | ELF Binary (Linux executable) (MIPS 32-bit) | `59b7568998255735...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `59c29436755b0778e968d49feeae20ed65f5fa5e35f9f7965b8ed93420db91e5` | ELF Binary (Linux executable) (x86-64 64-bit) | `59c29436755b0778...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `59da60e031a1bc0cadb4d5b62a9b3047c40c490738b5ca7ed367f4a8440561a3` | Unknown binary | `59da60e031a1bc0c...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `5b7b9a6449dcf0b779dd72210926d4567453aa40f16b473343a3aa4372798884` | ELF Binary (Linux executable) (AArch64 64-bit) | `5b7b9a6449dcf0b7...` | 38/100 | 🟢 LOW | **22/74** 🔴 |

**Suspicious Indicators — HIGH Severity Samples:**

_`09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` (09591253a95411d60c2b0d53...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Download via TFTP` — `tftp`
- `Download via ftpget` — `ftpget`
- `Execution from /tmp` — `/tmp/condi`
- `IP:Port (possible C2)` — `255.255.255[.]255:1900`

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
| `94.154.43[.]91` | TR | Storm Industries LLC | **100** ⚠️ | 0 |
| `218.146.255[.]221` | KR | Korea Telecom | **100** ⚠️ | 50 |
| `117.70.94[.]155` | CN | CHINANET anhui province network | **100** ⚠️ | 50 |
| `117.250.19[.]91` | IN | L malini devi high garden resort kailashpuri udaipur | **100** ⚠️ | 37 |
| `180.76.52[.]146` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 50 |
| `81.22.51[.]64` | RU | Region Svyaz Konsalt LLC | **100** ⚠️ | 50 |
| `117.2.123[.]19` | VN | Viettel Group | **100** ⚠️ | 50 |
| `46.29.26[.]195` | FI | FortiCore Digital SAS | **100** ⚠️ | 36 |
| `61.185.30[.]170` | CN | CHINANET Shanxi(SN) province network | **100** ⚠️ | 50 |
| `118.183.180[.]108` | CN | CHINANET Gansu province network | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 196 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 139 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 9 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 5 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 5 |

---

## 🔕 False Positive Summary (36 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| AbuseIPDB score 4 below threshold 25 | 2 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 31 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 281 cases |
| Tool 34  | Credential Extractor        | ✅ 206 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 20 fingerprints |
| Tool 36  | Command Clustering          | ✅ 6 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 158 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 36 filtered (12.8%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 94 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 28 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 137 priority case(s) shown individually · 43 recon entry/entries in table (17 group(s) consolidating 82 session(s)).

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
_Report time: 2026-07-21T17:26:55Z_

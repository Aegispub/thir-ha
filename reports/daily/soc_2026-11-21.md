# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-11-21 |
| **Generated At** | 2026-11-21T18:27:37Z |
| **Shift Time** | 18:27 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **384** |
| Confirmed Threats | **318** |
| False Positives Filtered | **66** (17.2%) |
| Unique Attacker IPs | **163** |
| Countries of Origin | **40** |
| High Severity Cases | **196** |
| Medium Severity Cases | **1** |
| Low Severity Cases | **187** |
| Malware Samples Analyzed | **9** HIGH · **26** MED · 0 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **1842** |
| Unique Credential Pairs | **1491** |
| Unique Usernames | **527** |
| Unique Passwords | **1008** |
| Successful Auth Pairs | **1642** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 623 |
| `admin` | 93 |
| `ubuntu` | 47 |
| `support` | 44 |
| `deploy` | 30 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 86 |
| `root` | 53 |
| `123` | 49 |
| `admin` | 48 |
| `1234` | 42 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `root` | 34 |
| `admin` | `admin` | 34 |
| `support` | `support` | 26 |
| `nobody` | `` | 21 |
| `rootssssss23424123123` | `rootssssss23424123123` | 17 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `jhf` | `jhf` | `109.160.32.153` | 2026-11-21T02:55:07 |
| `florida1` | `florida1` | `109.160.32.153` | 2026-11-21T02:55:12 |
| `root` | `cx123...` | `109.160.32.153` | 2026-11-21T02:55:16 |
| `milad` | `milad` | `109.160.32.153` | 2026-11-21T02:55:21 |
| `root` | `00008888` | `109.160.32.153` | 2026-11-21T02:55:26 |
| `bob` | `bob` | `109.160.32.153` | 2026-11-21T02:55:31 |
| `root` | `741852963` | `109.160.32.153` | 2026-11-21T02:55:35 |
| `root` | `123123asd` | `109.160.32.153` | 2026-11-21T02:55:40 |
| `ftpuser` | `ftpuser` | `109.160.32.153` | 2026-11-21T02:55:45 |
| `key1` | `Qwerty123?` | `109.160.32.153` | 2026-11-21T02:55:49 |
| `user10` | `user10` | `109.160.32.153` | 2026-11-21T02:55:54 |
| `root1` | `123456` | `109.160.32.153` | 2026-11-21T02:55:59 |
| `pi` | `1234` | `109.160.32.153` | 2026-11-21T02:56:04 |
| `app` | `app` | `109.160.32.153` | 2026-11-21T02:56:09 |
| `root` | `linux` | `109.160.32.153` | 2026-11-21T02:56:14 |
| `oot` | `4545` | `109.160.32.153` | 2026-11-21T02:56:19 |
| `zfh` | `!@` | `109.160.32.153` | 2026-11-21T02:56:24 |
| `root` | `nPSpP4PBW0` | `109.160.32.153` | 2026-11-21T02:56:28 |
| `root1` | `qwe123!@` | `109.160.32.153` | 2026-11-21T02:56:33 |
| `root` | `Adc123456` | `109.160.32.153` | 2026-11-21T02:56:39 |
_… 1622 more successful pair(s) in credentials.json_

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **384** |
| Sessions with Fingerprint | **30** |
| Unique HASSH Fingerprints | **30** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 151 |
| libssh | 25 |
| OpenSSH | 9 |
| Unknown | 5 |
| PuTTY | 4 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `2ec37a7cc8da...` | Mirai/variant | 93 | 3 |
| `7d01d047ace6...` | Mirai/variant | 20 | 3 |
| `f555226df196...` | Mirai/variant | 18 | 10 |
| `eff4c24daffc...` | Modern SSH client | 7 | 1 |
| `16443846184e...` | Generic scanner | 7 | 4 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `2ec37a7cc8da...` | Go SSH scanner | 93 | 3 | Mirai/variant |
| `7d01d047ace6...` | Go SSH scanner | 20 | 3 | Mirai/variant |
| `f555226df196...` | libssh | 18 | 10 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 7 | 1 | Modern SSH client |
| `95420f9d932d...` | OpenSSH | 7 | 6 | — |
| `16443846184e...` | Go SSH scanner | 7 | 4 | Generic scanner |
| `0a07365cc01f...` | Go SSH scanner | 4 | 2 | Generic scanner |
| `98f63c4d9c87...` | Go SSH scanner | 4 | 4 | Generic scanner |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **104** |
| Campaign Clusters | **5** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Mirai/IoT Botnet** | 🔴 HIGH | 2 | 1 | `T1105, T1083, T1140, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1082, T1592` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 8 | 3 | `T1082, T1105, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 17 | 9 | `T1021.004, T1078, T1070, T1140` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 2 | 1 | `T1105, T1140, T1059.004` |

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
enable
```
```
linuxshell
```
```
system
```
```
sh
```
```
ls /home; /bin/busybox BOTNET
```
Source IPs: `160.119.66.206`

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
echo "root:y8r0YcBHjNoS"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `106.227.75.197`

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
Source IPs: `179.254.92.3`, `147.90.214.201`, `169.128.70.53`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **163** |
| Unique ASNs | **74** |
| High-Risk ASNs | **49** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 38 | HIGH |
| `AS398324` | Censys, Inc. | 9 | HIGH |
| `AS4766` | Korea Telecom | 7 | HIGH |
| `AS16509` | Amazon.com, Inc. | 5 | HIGH |
| `AS45102` | Alibaba (US) Technology Co., Ltd. | 4 | HIGH |
| `AS396982` | Google LLC | 4 | LOW |
| `AS21859` | Zenlayer Inc | 4 | HIGH |
| `AS6939` | Hurricane Electric LLC | 4 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (187)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-4ff6e75f2bb5

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]153` |
| **First Seen** | 2026-11-21 02:55 |
| **Last Seen** | 2026-11-21 02:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-21 02:55:06` | `cowrie.session.connect` |
| `2026-11-21 02:55:06` | `cowrie.client.version` |
| `2026-11-21 02:55:06` | `cowrie.client.kex` |
| `2026-11-21 02:55:07` | `cowrie.login.success` |
| `2026-11-21 02:55:07` | `cowrie.session.params` |
| `2026-11-21 02:55:07` | `cowrie.command.input` |
| `2026-11-21 02:55:07` | `cowrie.log.closed` |
| `2026-11-21 02:55:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]153` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3ba26fcdc66

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]252` |
| **First Seen** | 2026-11-21 03:00 |
| **Last Seen** | 2026-11-21 03:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-21 03:00:36` | `cowrie.session.connect` |
| `2026-11-21 03:00:36` | `cowrie.login.success` |
| `2026-11-21 03:00:37` | `cowrie.session.params` |
| `2026-11-21 03:00:37` | `cowrie.log.closed` |
| `2026-11-21 03:00:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]252` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]252` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01ef6069f3c2

| Field | Detail |
|---|---|
| **Source IP** | `138.226.239[.]233` |
| **First Seen** | 2026-11-21 03:04 |
| **Last Seen** | 2026-11-21 03:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-21 03:04:04` | `cowrie.session.connect` |
| `2026-11-21 03:04:04` | `cowrie.client.version` |
| `2026-11-21 03:04:04` | `cowrie.client.kex` |
| `2026-11-21 03:04:04` | `cowrie.login.success` |
| `2026-11-21 03:04:04` | `cowrie.direct-tcpip.request` |
| `2026-11-21 03:04:05` | `cowrie.direct-tcpip.ja4` |
| `2026-11-21 03:04:05` | `cowrie.direct-tcpip.data` |
| `2026-11-21 03:04:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.226.239[.]233` to AbuseIPDB if not already reported
- [ ] Block `138.226.239[.]233` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad14b6f38563

| Field | Detail |
|---|---|
| **Source IP** | `138.226.239[.]234` |
| **First Seen** | 2026-11-21 03:04 |
| **Last Seen** | 2026-11-21 03:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-21 03:04:07` | `cowrie.session.connect` |
| `2026-11-21 03:04:07` | `cowrie.client.version` |
| `2026-11-21 03:04:07` | `cowrie.client.kex` |
| `2026-11-21 03:04:07` | `cowrie.login.success` |
| `2026-11-21 03:04:07` | `cowrie.direct-tcpip.request` |
| `2026-11-21 03:04:07` | `cowrie.direct-tcpip.ja4` |
| `2026-11-21 03:04:07` | `cowrie.direct-tcpip.data` |
| `2026-11-21 03:04:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.226.239[.]234` to AbuseIPDB if not already reported
- [ ] Block `138.226.239[.]234` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ff675bed311

| Field | Detail |
|---|---|
| **Source IP** | `80.94.95[.]118` |
| **First Seen** | 2026-11-21 03:06 |
| **Last Seen** | 2026-11-21 03:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-21 03:06:29` | `cowrie.session.connect` |
| `2026-11-21 03:06:29` | `cowrie.client.version` |
| `2026-11-21 03:06:29` | `cowrie.client.kex` |
| `2026-11-21 03:06:30` | `cowrie.login.success` |
| `2026-11-21 03:06:30` | `cowrie.direct-tcpip.request` |
| `2026-11-21 03:06:30` | `cowrie.direct-tcpip.ja4` |
| `2026-11-21 03:06:30` | `cowrie.direct-tcpip.data` |
| `2026-11-21 03:06:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.95[.]118` to AbuseIPDB if not already reported
- [ ] Block `80.94.95[.]118` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a95ca1799d0

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-11-21 03:07 |
| **Last Seen** | 2026-11-21 03:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-21 03:07:21` | `cowrie.session.connect` |
| `2026-11-21 03:07:21` | `cowrie.client.version` |
| `2026-11-21 03:07:21` | `cowrie.client.kex` |
| `2026-11-21 03:07:22` | `cowrie.login.success` |
| `2026-11-21 03:07:22` | `cowrie.direct-tcpip.request` |
| `2026-11-21 03:07:22` | `cowrie.direct-tcpip.data` |
| `2026-11-21 03:07:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c8c23b02fe0

| Field | Detail |
|---|---|
| **Source IP** | `35.210.163[.]9` |
| **First Seen** | 2026-11-21 03:14 |
| **Last Seen** | 2026-11-21 03:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip, Connection: close` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-21 03:14:15` | `cowrie.session.connect` |
| `2026-11-21 03:14:15` | `cowrie.login.success` |
| `2026-11-21 03:14:16` | `cowrie.session.params` |
| `2026-11-21 03:14:16` | `cowrie.command.input` |
| `2026-11-21 03:14:16` | `cowrie.command.input` |
| `2026-11-21 03:14:16` | `cowrie.command.failed` |
| `2026-11-21 03:14:16` | `cowrie.command.input` |
| `2026-11-21 03:14:16` | `cowrie.command.failed` |
| `2026-11-21 03:14:16` | `cowrie.command.input` |
| `2026-11-21 03:14:16` | `cowrie.log.closed` |
| `2026-11-21 03:14:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.210.163[.]9` to AbuseIPDB if not already reported
- [ ] Block `35.210.163[.]9` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f7adbcbe995

| Field | Detail |
|---|---|
| **Source IP** | `209.38.219[.]74` |
| **First Seen** | 2026-11-21 03:23 |
| **Last Seen** | 2026-11-21 03:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Go-http-client/1.1, Connection: close` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-21 03:23:31` | `cowrie.session.connect` |
| `2026-11-21 03:23:31` | `cowrie.login.success` |
| `2026-11-21 03:23:32` | `cowrie.session.params` |
| `2026-11-21 03:23:32` | `cowrie.command.input` |
| `2026-11-21 03:23:32` | `cowrie.command.failed` |
| `2026-11-21 03:23:32` | `cowrie.command.input` |
| `2026-11-21 03:23:32` | `cowrie.command.failed` |
| `2026-11-21 03:23:32` | `cowrie.command.input` |
| `2026-11-21 03:23:32` | `cowrie.log.closed` |
| `2026-11-21 03:23:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.38.219[.]74` to AbuseIPDB if not already reported
- [ ] Block `209.38.219[.]74` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89032c955703

| Field | Detail |
|---|---|
| **Source IP** | `35.210.18[.]235` |
| **First Seen** | 2026-11-21 03:27 |
| **Last Seen** | 2026-11-21 03:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip, Connection: close` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-21 03:27:01` | `cowrie.session.connect` |
| `2026-11-21 03:27:01` | `cowrie.login.success` |
| `2026-11-21 03:27:01` | `cowrie.session.params` |
| `2026-11-21 03:27:01` | `cowrie.command.input` |
| `2026-11-21 03:27:01` | `cowrie.command.input` |
| `2026-11-21 03:27:01` | `cowrie.command.failed` |
| `2026-11-21 03:27:01` | `cowrie.command.input` |
| `2026-11-21 03:27:01` | `cowrie.command.failed` |
| `2026-11-21 03:27:01` | `cowrie.command.input` |
| `2026-11-21 03:27:01` | `cowrie.log.closed` |
| `2026-11-21 03:27:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.210.18[.]235` to AbuseIPDB if not already reported
- [ ] Block `35.210.18[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73c4edb78e38

| Field | Detail |
|---|---|
| **Source IP** | `35.210.18[.]235` |
| **First Seen** | 2026-11-21 03:27 |
| **Last Seen** | 2026-11-21 03:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-21 03:27:01` | `cowrie.session.connect` |
| `2026-11-21 03:27:01` | `cowrie.login.success` |
| `2026-11-21 03:27:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.210.18[.]235` to AbuseIPDB if not already reported
- [ ] Block `35.210.18[.]235` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-413321bba4d5

| Field | Detail |
|---|---|
| **Source IP** | `36.107.225[.]185` |
| **First Seen** | 2026-11-21 03:33 |
| **Last Seen** | 2026-11-21 03:33 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-21 03:33:29` | `cowrie.session.connect` |
| `2026-11-21 03:33:29` | `cowrie.client.version` |
| `2026-11-21 03:33:29` | `cowrie.client.kex` |
| `2026-11-21 03:33:30` | `cowrie.login.success` |
| `2026-11-21 03:33:31` | `cowrie.session.params` |
| `2026-11-21 03:33:31` | `cowrie.command.input` |
| `2026-11-21 03:33:31` | `cowrie.log.closed` |
| `2026-11-21 03:33:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.107.225[.]185` to AbuseIPDB if not already reported
- [ ] Block `36.107.225[.]185` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-537146ff93e7

| Field | Detail |
|---|---|
| **Source IP** | `169.128.70[.]53` |
| **First Seen** | 2026-11-21 03:42 |
| **Last Seen** | 2026-11-21 03:42 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST, /bin/busybox TEST, cat /proc, ./` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-21 03:42:39` | `cowrie.session.connect` |
| `2026-11-21 03:42:40` | `cowrie.login.success` |
| `2026-11-21 03:42:40` | `cowrie.session.params` |
| `2026-11-21 03:42:41` | `cowrie.command.input` |
| `2026-11-21 03:42:41` | `cowrie.command.input` |
| `2026-11-21 03:42:42` | `cowrie.command.input` |
| `2026-11-21 03:42:42` | `cowrie.command.input` |
| `2026-11-21 03:42:42` | `cowrie.command.failed` |
| `2026-11-21 03:42:43` | `cowrie.log.closed` |
| `2026-11-21 03:42:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `169.128.70[.]53` to AbuseIPDB if not already reported
- [ ] Block `169.128.70[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af3031b89c88

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]78` |
| **First Seen** | 2026-11-21 04:05 |
| **Last Seen** | 2026-11-21 04:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-21 04:05:38` | `cowrie.session.connect` |
| `2026-11-21 04:05:38` | `cowrie.login.success` |
| `2026-11-21 04:05:39` | `cowrie.session.params` |
| `2026-11-21 04:05:39` | `cowrie.log.closed` |
| `2026-11-21 04:05:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]78` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]78` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1cfdbc3e5fc

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-11-21 04:16 |
| **Last Seen** | 2026-11-21 04:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-21 04:16:59` | `cowrie.session.connect` |
| `2026-11-21 04:16:59` | `cowrie.client.version` |
| `2026-11-21 04:16:59` | `cowrie.client.kex` |
| `2026-11-21 04:17:00` | `cowrie.login.success` |
| `2026-11-21 04:17:00` | `cowrie.direct-tcpip.request` |
| `2026-11-21 04:17:00` | `cowrie.direct-tcpip.data` |
| `2026-11-21 04:17:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bdc7f2e3cd90

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]252` |
| **First Seen** | 2026-11-21 04:18 |
| **Last Seen** | 2026-11-21 04:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-21 04:18:38` | `cowrie.session.connect` |
| `2026-11-21 04:18:38` | `cowrie.login.success` |
| `2026-11-21 04:18:39` | `cowrie.session.params` |
| `2026-11-21 04:18:39` | `cowrie.log.closed` |
| `2026-11-21 04:18:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]252` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]252` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5fd629f2aaf

| Field | Detail |
|---|---|
| **Source IP** | `35.210.94[.]212` |
| **First Seen** | 2026-11-21 04:18 |
| **Last Seen** | 2026-11-21 04:18 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-21 04:18:41` | `cowrie.session.connect` |
| `2026-11-21 04:18:41` | `cowrie.client.version` |
| `2026-11-21 04:18:41` | `cowrie.client.kex` |
| `2026-11-21 04:18:44` | `cowrie.login.success` |
| `2026-11-21 04:18:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.210.94[.]212` to AbuseIPDB if not already reported
- [ ] Block `35.210.94[.]212` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c36207f1d76

| Field | Detail |
|---|---|
| **Source IP** | `78.128.112[.]74` |
| **First Seen** | 2026-11-21 04:24 |
| **Last Seen** | 2026-11-21 04:24 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo 'SSH check'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-21 04:24:57` | `cowrie.session.connect` |
| `2026-11-21 04:24:57` | `cowrie.client.version` |
| `2026-11-21 04:24:57` | `cowrie.client.kex` |
| `2026-11-21 04:24:58` | `cowrie.login.success` |
| `2026-11-21 04:24:59` | `cowrie.session.params` |
| `2026-11-21 04:24:59` | `cowrie.command.input` |
| `2026-11-21 04:24:59` | `cowrie.log.closed` |
| `2026-11-21 04:24:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `78.128.112[.]74` to AbuseIPDB if not already reported
- [ ] Block `78.128.112[.]74` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e79cd21c4ad

| Field | Detail |
|---|---|
| **Source IP** | `138.226.239[.]234` |
| **First Seen** | 2026-11-21 05:13 |
| **Last Seen** | 2026-11-21 05:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-21 05:13:39` | `cowrie.session.connect` |
| `2026-11-21 05:13:39` | `cowrie.client.version` |
| `2026-11-21 05:13:39` | `cowrie.client.kex` |
| `2026-11-21 05:13:39` | `cowrie.login.success` |
| `2026-11-21 05:13:39` | `cowrie.direct-tcpip.request` |
| `2026-11-21 05:13:39` | `cowrie.direct-tcpip.ja4` |
| `2026-11-21 05:13:39` | `cowrie.direct-tcpip.data` |
| `2026-11-21 05:13:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.226.239[.]234` to AbuseIPDB if not already reported
- [ ] Block `138.226.239[.]234` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-559f64cec7d5

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]64` |
| **First Seen** | 2026-11-21 05:16 |
| **Last Seen** | 2026-11-21 05:16 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_4eb8520247bccef0ae67630ff124104f_small_control'"'"' '"'"'check_4eb8520247bccef0ae67630ff124104f'"'"'', printf '\n%s|%s\n' 'check_4eb8520247bccef0ae67630ff124104f_small_control' 'check_4eb8520247bccef0ae67630ff124104f', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_4eb8520247bccef0ae67630ff124104f_small_math'"'"' "$((213*184+74))"', (213*184+74, printf '\n%s|%s\n' 'check_4eb8520247bccef0ae67630ff124104f_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-21 05:16:09` | `cowrie.session.connect` |
| `2026-11-21 05:16:10` | `cowrie.client.version` |
| `2026-11-21 05:16:10` | `cowrie.client.kex` |
| `2026-11-21 05:16:15` | `cowrie.login.success` |
| `2026-11-21 05:16:20` | `cowrie.client.size` |
| `2026-11-21 05:16:20` | `cowrie.session.params` |
| `2026-11-21 05:16:21` | `cowrie.command.input` |
| `2026-11-21 05:16:21` | `cowrie.command.input` |
| `2026-11-21 05:16:21` | `cowrie.command.input` |
| `2026-11-21 05:16:21` | `cowrie.command.input` |
| `2026-11-21 05:16:21` | `cowrie.command.input` |
| `2026-11-21 05:16:21` | `cowrie.command.input` |
| `2026-11-21 05:16:21` | `cowrie.command.input` |
| `2026-11-21 05:16:21` | `cowrie.command.input` |
| `2026-11-21 05:16:21` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]64` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca0f9fd45b1d

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]64` |
| **First Seen** | 2026-11-21 05:19 |
| **Last Seen** | 2026-11-21 05:19 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_d2143eb98180a2a1a655cba6a3944486_small_control'"'"' '"'"'check_d2143eb98180a2a1a655cba6a3944486'"'"'', printf '\n%s|%s\n' 'check_d2143eb98180a2a1a655cba6a3944486_small_control' 'check_d2143eb98180a2a1a655cba6a3944486', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_d2143eb98180a2a1a655cba6a3944486_small_math'"'"' "$((940*202+43))"', (940*202+43, printf '\n%s|%s\n' 'check_d2143eb98180a2a1a655cba6a3944486_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-21 05:19:00` | `cowrie.session.connect` |
| `2026-11-21 05:19:01` | `cowrie.client.version` |
| `2026-11-21 05:19:01` | `cowrie.client.kex` |
| `2026-11-21 05:19:07` | `cowrie.login.success` |
| `2026-11-21 05:19:10` | `cowrie.client.size` |
| `2026-11-21 05:19:12` | `cowrie.session.params` |
| `2026-11-21 05:19:13` | `cowrie.command.input` |
| `2026-11-21 05:19:13` | `cowrie.command.input` |
| `2026-11-21 05:19:13` | `cowrie.command.input` |
| `2026-11-21 05:19:13` | `cowrie.command.input` |
| `2026-11-21 05:19:13` | `cowrie.command.input` |
| `2026-11-21 05:19:13` | `cowrie.command.input` |
| `2026-11-21 05:19:13` | `cowrie.command.input` |
| `2026-11-21 05:19:13` | `cowrie.command.input` |
| `2026-11-21 05:19:13` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]64` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2893cdadc781

| Field | Detail |
|---|---|
| **Source IP** | `80.94.95[.]118` |
| **First Seen** | 2026-11-21 05:20 |
| **Last Seen** | 2026-11-21 05:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-21 05:20:01` | `cowrie.session.connect` |
| `2026-11-21 05:20:01` | `cowrie.client.version` |
| `2026-11-21 05:20:01` | `cowrie.client.kex` |
| `2026-11-21 05:20:02` | `cowrie.login.success` |
| `2026-11-21 05:20:02` | `cowrie.direct-tcpip.request` |
| `2026-11-21 05:20:02` | `cowrie.direct-tcpip.ja4` |
| `2026-11-21 05:20:02` | `cowrie.direct-tcpip.data` |
| `2026-11-21 05:20:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.95[.]118` to AbuseIPDB if not already reported
- [ ] Block `80.94.95[.]118` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b19dc99c6de1

| Field | Detail |
|---|---|
| **Source IP** | `138.226.239[.]233` |
| **First Seen** | 2026-11-21 05:20 |
| **Last Seen** | 2026-11-21 05:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-21 05:20:15` | `cowrie.session.connect` |
| `2026-11-21 05:20:15` | `cowrie.client.version` |
| `2026-11-21 05:20:15` | `cowrie.client.kex` |
| `2026-11-21 05:20:15` | `cowrie.login.success` |
| `2026-11-21 05:20:15` | `cowrie.direct-tcpip.request` |
| `2026-11-21 05:20:15` | `cowrie.direct-tcpip.ja4` |
| `2026-11-21 05:20:15` | `cowrie.direct-tcpip.data` |
| `2026-11-21 05:20:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.226.239[.]233` to AbuseIPDB if not already reported
- [ ] Block `138.226.239[.]233` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bbca51c1e611

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]64` |
| **First Seen** | 2026-11-21 05:21 |
| **Last Seen** | 2026-11-21 05:21 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_6f007306d4500a66cf9f5c8f11f989ac_small_control'"'"' '"'"'check_6f007306d4500a66cf9f5c8f11f989ac'"'"'', printf '\n%s|%s\n' 'check_6f007306d4500a66cf9f5c8f11f989ac_small_control' 'check_6f007306d4500a66cf9f5c8f11f989ac', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_6f007306d4500a66cf9f5c8f11f989ac_small_math'"'"' "$((501*708+93))"', (501*708+93, printf '\n%s|%s\n' 'check_6f007306d4500a66cf9f5c8f11f989ac_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-21 05:21:35` | `cowrie.session.connect` |
| `2026-11-21 05:21:36` | `cowrie.client.version` |
| `2026-11-21 05:21:36` | `cowrie.client.kex` |
| `2026-11-21 05:21:42` | `cowrie.login.success` |
| `2026-11-21 05:21:45` | `cowrie.client.size` |
| `2026-11-21 05:21:47` | `cowrie.session.params` |
| `2026-11-21 05:21:48` | `cowrie.command.input` |
| `2026-11-21 05:21:48` | `cowrie.command.input` |
| `2026-11-21 05:21:48` | `cowrie.command.input` |
| `2026-11-21 05:21:48` | `cowrie.command.input` |
| `2026-11-21 05:21:48` | `cowrie.command.input` |
| `2026-11-21 05:21:48` | `cowrie.command.input` |
| `2026-11-21 05:21:48` | `cowrie.command.input` |
| `2026-11-21 05:21:48` | `cowrie.command.input` |
| `2026-11-21 05:21:48` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]64` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a1085e11e28

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]64` |
| **First Seen** | 2026-11-21 05:24 |
| **Last Seen** | 2026-11-21 05:24 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_224abf3828553ad13f9d6557cc89d717_small_control'"'"' '"'"'check_224abf3828553ad13f9d6557cc89d717'"'"'', printf '\n%s|%s\n' 'check_224abf3828553ad13f9d6557cc89d717_small_control' 'check_224abf3828553ad13f9d6557cc89d717', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_224abf3828553ad13f9d6557cc89d717_small_math'"'"' "$((803*394+49))"', (803*394+49, printf '\n%s|%s\n' 'check_224abf3828553ad13f9d6557cc89d717_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-21 05:24:07` | `cowrie.session.connect` |
| `2026-11-21 05:24:08` | `cowrie.client.version` |
| `2026-11-21 05:24:08` | `cowrie.client.kex` |
| `2026-11-21 05:24:14` | `cowrie.login.success` |
| `2026-11-21 05:24:17` | `cowrie.client.size` |
| `2026-11-21 05:24:18` | `cowrie.session.params` |
| `2026-11-21 05:24:20` | `cowrie.command.input` |
| `2026-11-21 05:24:20` | `cowrie.command.input` |
| `2026-11-21 05:24:20` | `cowrie.command.input` |
| `2026-11-21 05:24:20` | `cowrie.command.input` |
| `2026-11-21 05:24:20` | `cowrie.command.input` |
| `2026-11-21 05:24:20` | `cowrie.command.input` |
| `2026-11-21 05:24:20` | `cowrie.command.input` |
| `2026-11-21 05:24:20` | `cowrie.command.input` |
| `2026-11-21 05:24:20` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]64` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b3971cc1395

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]64` |
| **First Seen** | 2026-11-21 05:39 |
| **Last Seen** | 2026-11-21 05:40 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_3e4b4674fba3d610d4b3e751ec3aa35e_small_control'"'"' '"'"'check_3e4b4674fba3d610d4b3e751ec3aa35e'"'"'', printf '\n%s|%s\n' 'check_3e4b4674fba3d610d4b3e751ec3aa35e_small_control' 'check_3e4b4674fba3d610d4b3e751ec3aa35e', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_3e4b4674fba3d610d4b3e751ec3aa35e_small_math'"'"' "$((993*199+40))"', (993*199+40, printf '\n%s|%s\n' 'check_3e4b4674fba3d610d4b3e751ec3aa35e_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-21 05:39:50` | `cowrie.session.connect` |
| `2026-11-21 05:39:51` | `cowrie.client.version` |
| `2026-11-21 05:39:51` | `cowrie.client.kex` |
| `2026-11-21 05:39:56` | `cowrie.login.success` |
| `2026-11-21 05:40:00` | `cowrie.client.size` |
| `2026-11-21 05:40:02` | `cowrie.session.params` |
| `2026-11-21 05:40:04` | `cowrie.command.input` |
| `2026-11-21 05:40:04` | `cowrie.command.input` |
| `2026-11-21 05:40:04` | `cowrie.command.input` |
| `2026-11-21 05:40:04` | `cowrie.command.input` |
| `2026-11-21 05:40:04` | `cowrie.command.input` |
| `2026-11-21 05:40:04` | `cowrie.command.input` |
| `2026-11-21 05:40:04` | `cowrie.command.input` |
| `2026-11-21 05:40:04` | `cowrie.command.input` |
| `2026-11-21 05:40:04` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]64` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### Additional priority cases (162) — compact view

| Case | Severity | Source IP | First Seen | Auth | Cmds | DL | TTPs |
|---|---|---|---|---|---|---|---|
| IR-53a3970141c1 | HIGH | `92.118.39[.]64` | 2026-11-21 05:45 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-b50fda6f8512 | HIGH | `92.118.39[.]64` | 2026-11-21 05:50 | Y | 0 | 0 | `T1078 · T1592` |
| IR-dc6b318d5a02 | HIGH | `179.254.92[.]3` | 2026-11-21 05:54 | Y | 4 | 0 | `T1078 · T1083` |
| IR-dd2080f45bd9 | HIGH | `77.239.124[.]252` | 2026-11-21 06:06 | Y | 0 | 0 | `T1078` |
| IR-a61f0ab18f28 | HIGH | `195.178.110[.]78` | 2026-11-21 06:14 | Y | 0 | 0 | `T1078` |
| IR-54628c853905 | HIGH | `176.53.159[.]196` | 2026-11-21 06:30 | Y | 0 | 0 | `T1078 · T1592` |
| IR-6ba42fbdf402 | HIGH | `156.225.1[.]88` | 2026-11-21 07:08 | Y | 1 | 0 | `T1078` |
| IR-96a55b30a054 | HIGH | `170.231.236[.]98` | 2026-11-21 07:09 | Y | 4 | 0 | `T1078` |
| IR-ffafe44179b9 | HIGH | `170.231.237[.]214` | 2026-11-21 07:09 | Y | 2 | 0 | `T1078` |
| IR-778716124223 | HIGH | `3.151.181[.]143` | 2026-11-21 07:10 | Y | 4 | 0 | `T1078` |
| IR-fb11b1f2d618 | HIGH | `3.151.181[.]143` | 2026-11-21 07:10 | Y | 2 | 0 | `T1078` |
| IR-2224eb45f419 | HIGH | `138.226.239[.]233` | 2026-11-21 07:22 | Y | 0 | 0 | `T1078 · T1592` |
| IR-50cbefdd1e8b | HIGH | `80.94.95[.]118` | 2026-11-21 07:25 | Y | 0 | 0 | `T1078 · T1592` |
| IR-2b9895deca0e | HIGH | `199.165.159[.]201` | 2026-11-21 07:39 | Y | 3 | 0 | `T1078` |
| IR-33d6c8441caf | HIGH | `169.128.70[.]53` | 2026-11-21 08:01 | Y | 4 | 0 | `T1078 · T1083` |
| IR-20223e25f1d1 | HIGH | `193.32.162[.]15` | 2026-11-21 08:09 | Y | 0 | 0 | `T1078 · T1592` |
| IR-cd1bf7293416 | HIGH | `77.239.124[.]252` | 2026-11-21 08:12 | Y | 0 | 0 | `T1078` |
| IR-21a325cd2bc4 | HIGH | `195.178.110[.]78` | 2026-11-21 08:33 | Y | 0 | 0 | `T1078` |
| IR-823a97ef57e9 | HIGH | `117.250.24[.]115` | 2026-11-21 08:40 | Y | 1 | 0 | `T1078 · T1592` |
| IR-19dbb0bc0f60 | HIGH | `92.118.39[.]64` | 2026-11-21 08:42 | Y | 0 | 0 | `T1078 · T1592` |
| IR-55c640e183a1 | HIGH | `129.150.32[.]71` | 2026-11-21 08:45 | Y | 1 | 0 | `T1078 · T1592` |
| IR-e51c875ab76d | HIGH | `176.53.159[.]196` | 2026-11-21 08:48 | Y | 0 | 0 | `T1078 · T1592` |
| IR-85cea3ec7230 | HIGH | `78.128.112[.]74` | 2026-11-21 08:56 | Y | 1 | 0 | `T1078 · T1592` |
| IR-4202b860df39 | HIGH | `156.232.10[.]218` | 2026-11-21 09:17 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-6eb808fb9f42 | HIGH | `156.232.10[.]218` | 2026-11-21 09:18 | Y | 0 | 0 | `T1078 · T1592` |
| IR-06453552b98c | HIGH | `138.226.239[.]234` | 2026-11-21 09:31 | Y | 0 | 0 | `T1078 · T1592` |
| IR-4871d0a72ecb | HIGH | `138.226.239[.]233` | 2026-11-21 09:32 | Y | 0 | 0 | `T1078 · T1592` |
| IR-91386bd9b87f | HIGH | `80.94.95[.]118` | 2026-11-21 09:34 | Y | 0 | 0 | `T1078 · T1592` |
| IR-f62a9c6831c3 | HIGH | `183.233.149[.]100` | 2026-11-21 09:44 | Y | 1 | 0 | `T1021.004 · T1078 · T1592` |
| IR-7c19002be971 | HIGH | `195.178.110[.]78` | 2026-11-21 10:00 | Y | 0 | 0 | `T1078` |
| IR-8f93d89d39c4 | HIGH | `77.239.124[.]252` | 2026-11-21 10:30 | Y | 0 | 0 | `T1078` |
| IR-bb5dcfd6bf80 | HIGH | `51.254.136[.]153` | 2026-11-21 10:32 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-4e6b5fdb0b33 | HIGH | `51.254.136[.]153` | 2026-11-21 10:32 | Y | 0 | 0 | `T1078 · T1592` |
| IR-7f1ecb87ab7b | HIGH | `160.119.66[.]206` | 2026-11-21 10:32 | Y | 6 | 3 | `T1059.004 · T1078 · T1105` |
| IR-5246aa4385d9 | HIGH | `160.119.66[.]206` | 2026-11-21 10:32 | Y | 1 | 3 | `T1059.004 · T1078 · T1105` |
| IR-205ae2e0f464 | HIGH | `92.118.39[.]50` | 2026-11-21 10:34 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-d4caef28353e | HIGH | `20.219.91[.]90` | 2026-11-21 10:40 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-b7c9ef4ad3af | HIGH | `20.219.91[.]90` | 2026-11-21 10:41 | Y | 0 | 0 | `T1078 · T1592` |
| IR-e9e1ae73915b | HIGH | `92.118.39[.]50` | 2026-11-21 10:43 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-1dc60b2b7d19 | HIGH | `92.118.39[.]50` | 2026-11-21 10:54 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-8cec830ef46b | HIGH | `92.118.39[.]50` | 2026-11-21 10:56 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-8c0001694d1d | HIGH | `92.118.39[.]50` | 2026-11-21 10:59 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-f47e9ba8da88 | HIGH | `92.118.39[.]50` | 2026-11-21 11:02 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-90cf5ba6618e | HIGH | `88.214.23[.]100` | 2026-11-21 11:03 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-126944b44766 | HIGH | `88.214.23[.]100` | 2026-11-21 11:03 | Y | 0 | 0 | `T1078 · T1592` |
| IR-845ae8c08da1 | HIGH | `171.25.158[.]58` | 2026-11-21 11:13 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-8993f1cea7b7 | HIGH | `171.25.158[.]58` | 2026-11-21 11:13 | Y | 0 | 0 | `T1078 · T1592` |
| IR-708f11aaa22b | HIGH | `107.150.105[.]153` | 2026-11-21 11:31 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-cf8f4982baf2 | HIGH | `176.53.159[.]196` | 2026-11-21 11:31 | Y | 0 | 0 | `T1078 · T1592` |
| IR-bb5b2f9b028b | HIGH | `169.128.70[.]53` | 2026-11-21 11:31 | Y | 4 | 0 | `T1078 · T1083` |
| IR-364ba3b96081 | HIGH | `107.150.105[.]153` | 2026-11-21 11:31 | Y | 0 | 0 | `T1078 · T1592` |
| IR-f95366669c8f | HIGH | `80.94.95[.]118` | 2026-11-21 11:40 | Y | 0 | 0 | `T1078 · T1592` |
| IR-fd689b828cdf | HIGH | `138.226.239[.]234` | 2026-11-21 11:41 | Y | 0 | 0 | `T1078 · T1592` |
| IR-5eea43b59d3a | HIGH | `147.90.214[.]201` | 2026-11-21 12:01 | Y | 4 | 0 | `T1078 · T1083` |
| IR-701d327ab635 | HIGH | `195.178.110[.]78` | 2026-11-21 12:06 | Y | 0 | 0 | `T1078` |
| IR-fd2be3cee719 | HIGH | `176.53.159[.]196` | 2026-11-21 12:14 | Y | 0 | 0 | `T1078 · T1592` |
| IR-969be628ab47 | HIGH | `109.105.210[.]64` | 2026-11-21 12:14 | Y | 3 | 0 | `T1078` |
| IR-0744c2fbea4b | HIGH | `77.239.124[.]252` | 2026-11-21 12:33 | Y | 0 | 0 | `T1078` |
| IR-5db9e5060399 | HIGH | `177.185.141[.]2` | 2026-11-21 12:56 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-34e27a9bf302 | HIGH | `177.185.141[.]2` | 2026-11-21 12:56 | Y | 0 | 0 | `T1078 · T1592` |
| IR-6de5c792bcac | HIGH | `195.178.110[.]227` | 2026-11-21 13:04 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-14649e6062fe | HIGH | `195.178.110[.]227` | 2026-11-21 13:05 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-2b97d0983db6 | HIGH | `195.178.110[.]227` | 2026-11-21 13:07 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-3bb5d3f89303 | HIGH | `195.178.110[.]227` | 2026-11-21 13:10 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-d36d487bf1c1 | HIGH | `195.178.110[.]227` | 2026-11-21 13:12 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-deadc6d36cd4 | HIGH | `195.178.110[.]227` | 2026-11-21 13:14 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-1b8725371f5a | HIGH | `195.178.110[.]227` | 2026-11-21 13:15 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-a21c65b432c5 | HIGH | `195.178.110[.]227` | 2026-11-21 13:17 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-8375c721ed47 | HIGH | `195.178.110[.]227` | 2026-11-21 13:19 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-d43e8b185d37 | HIGH | `195.178.110[.]227` | 2026-11-21 13:21 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-cb6c521f92c6 | HIGH | `195.178.110[.]227` | 2026-11-21 13:22 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-cc33e6674a19 | HIGH | `195.178.110[.]227` | 2026-11-21 13:24 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-73e7e7a729ec | HIGH | `195.178.110[.]227` | 2026-11-21 13:26 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-69a27871a89c | HIGH | `78.128.112[.]74` | 2026-11-21 13:26 | Y | 1 | 0 | `T1078 · T1592` |
| IR-b780437da164 | HIGH | `195.178.110[.]227` | 2026-11-21 13:27 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-260a7c7b90e3 | HIGH | `195.178.110[.]227` | 2026-11-21 13:29 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-42744398064b | HIGH | `195.178.110[.]227` | 2026-11-21 13:31 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-51479cd7b5f3 | HIGH | `195.178.110[.]227` | 2026-11-21 13:33 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-c612a4389529 | HIGH | `195.178.110[.]227` | 2026-11-21 13:34 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-e0c162db4f51 | HIGH | `104.244.79[.]113` | 2026-11-21 13:35 | Y | 0 | 0 | `T1078 · T1592` |
| IR-baeb0723bdc4 | HIGH | `195.178.110[.]227` | 2026-11-21 13:36 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-0ead37ada446 | HIGH | `195.178.110[.]227` | 2026-11-21 13:38 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-4fde58f6a8be | HIGH | `195.178.110[.]227` | 2026-11-21 13:39 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-6672c3ee786e | HIGH | `195.178.110[.]227` | 2026-11-21 13:41 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-35bdd5d11359 | HIGH | `195.178.110[.]227` | 2026-11-21 13:43 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-de92d7288395 | HIGH | `195.178.110[.]227` | 2026-11-21 13:44 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-9d1f445639ad | HIGH | `195.178.110[.]227` | 2026-11-21 13:46 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-92897c6575de | HIGH | `195.178.110[.]227` | 2026-11-21 13:48 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-c500a3efe584 | HIGH | `138.226.239[.]234` | 2026-11-21 13:49 | Y | 0 | 0 | `T1078 · T1592` |
| IR-06d2a24762f1 | HIGH | `195.178.110[.]227` | 2026-11-21 13:49 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-40bac5e823f3 | HIGH | `116.140.208[.]145` | 2026-11-21 13:50 | Y | 1 | 0 | `T1078 · T1592` |
| IR-c7215d6110c4 | HIGH | `80.94.95[.]118` | 2026-11-21 13:50 | Y | 0 | 0 | `T1078 · T1592` |
| IR-54f50d0bc1e9 | HIGH | `195.178.110[.]227` | 2026-11-21 13:51 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-2c1e813e7f20 | HIGH | `138.226.239[.]233` | 2026-11-21 13:52 | Y | 0 | 0 | `T1078 · T1592` |
| IR-376c6233128a | HIGH | `195.178.110[.]227` | 2026-11-21 13:53 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-b53928bb2430 | HIGH | `195.178.110[.]227` | 2026-11-21 13:54 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-c5a13c05f81f | HIGH | `195.178.110[.]227` | 2026-11-21 13:56 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-e79a59a47ba1 | HIGH | `195.178.110[.]227` | 2026-11-21 13:58 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-437568d9acd9 | HIGH | `195.178.110[.]227` | 2026-11-21 13:59 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-b845dca729cd | HIGH | `195.178.110[.]227` | 2026-11-21 14:01 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
_… 62 more priority case(s) in ir_cases.json_

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `77.239.124[.]252` | **3** | 2026-11-21 03:00 | 2026-11-21 06:06 | 0m | 3 | `T1110.001` | 🟢 LOW |
| `109.160.32[.]139` | **2** | 2026-11-21 15:01 | 2026-11-21 16:19 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `195.178.110[.]227` | **2** | 2026-11-21 13:09 | 2026-11-21 15:09 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `195.178.110[.]78` | **2** | 2026-11-21 08:33 | 2026-11-21 10:00 | 0m | 2 | `T1110.001` | 🟢 LOW |
| `77.239.124[.]130` | **2** | 2026-11-21 03:55 | 2026-11-21 05:37 | 0m | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]132` | **2** | 2026-11-21 05:22 | 2026-11-21 06:51 | 0m | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]252` | **2** | 2026-11-21 12:33 | 2026-11-21 14:08 | 0m | 2 | `T1110.001` | 🟢 LOW |
| `103.203.57[.]19` | 1 | 2026-11-21 16:06 | 2026-11-21 16:06 | 5s | 0 | `T1592` | 🟢 LOW |
| `103.73.75[.]127` | 1 | 2026-11-21 10:24 | 2026-11-21 10:24 | 0s | 0 | `T1592` | 🟢 LOW |
| `106.227.75[.]197` | 1 | 2026-11-21 16:06 | 2026-11-21 16:08 | 120s | 0 | `T1592` | 🟢 LOW |
| `107.11.72[.]36` | 1 | 2026-11-21 13:11 | 2026-11-21 13:11 | 0s | 0 | `T1592` | 🟢 LOW |
| `107.155.48[.]46` | 1 | 2026-11-21 12:15 | 2026-11-21 12:15 | 0s | 0 | `T1592` | 🟢 LOW |
| `109.105.210[.]62` | 1 | 2026-11-21 12:14 | 2026-11-21 12:14 | 4s | 0 | `T1592` | 🟢 LOW |
| `109.105.210[.]63` | 1 | 2026-11-21 12:15 | 2026-11-21 12:15 | 0s | 0 | `T1592` | 🟢 LOW |
| `109.105.210[.]64` | 1 | 2026-11-21 12:15 | 2026-11-21 12:15 | 0s | 0 | `T1592` | 🟢 LOW |
| `109.105.210[.]65` | 1 | 2026-11-21 12:15 | 2026-11-21 12:15 | 7s | 0 | `T1592` | 🟢 LOW |
| `111.33.71[.]238` | 1 | 2026-11-21 04:17 | 2026-11-21 04:17 | 0s | 0 | `T1592` | 🟢 LOW |
| `111.33.71[.]238` | 1 | 2026-11-21 14:43 | 2026-11-21 14:43 | 0s | 0 | `T1592` | 🟢 LOW |
| `112.168.176[.]15` | 1 | 2026-11-21 05:51 | 2026-11-21 05:51 | 16s | 0 | `T1592` | 🟢 LOW |
| `112.5.89[.]227` | 1 | 2026-11-21 14:16 | 2026-11-21 14:17 | 30s | 0 | `T1592` | 🟢 LOW |
| `112.74.242[.]167` | 1 | 2026-11-21 04:33 | 2026-11-21 04:34 | 33s | 0 | `T1592` | 🟢 LOW |
| `117.250.24[.]115` | 1 | 2026-11-21 08:40 | 2026-11-21 08:40 | 5s | 0 | `T1592` | 🟢 LOW |
| `118.47.255[.]44` | 1 | 2026-11-21 11:38 | 2026-11-21 11:39 | 28s | 0 | `T1592` | 🟢 LOW |
| `13.49.36[.]97` | 1 | 2026-11-21 07:10 | 2026-11-21 07:10 | 2s | 0 | `T1592` | 🟢 LOW |
| `137.184.5[.]188` | 1 | 2026-11-21 04:33 | 2026-11-21 04:34 | 30s | 0 | `T1592` | 🟢 LOW |
| `137.184.5[.]188` | 1 | 2026-11-21 08:10 | 2026-11-21 08:10 | 31s | 0 | `T1592` | 🟢 LOW |
| `137.184.5[.]188` | 1 | 2026-11-21 14:55 | 2026-11-21 14:56 | 32s | 0 | `T1592` | 🟢 LOW |
| `14.57.186[.]60` | 1 | 2026-11-21 11:47 | 2026-11-21 11:47 | 22s | 0 | `T1592` | 🟢 LOW |
| `147.90.214[.]201` | 1 | 2026-11-21 12:01 | 2026-11-21 12:01 | 0s | 0 | `T1592` | 🟢 LOW |
| `151.243.11[.]141` | 1 | 2026-11-21 12:41 | 2026-11-21 12:41 | 4s | 0 | `T1592` | 🟢 LOW |
| `151.243.11[.]188` | 1 | 2026-11-21 10:06 | 2026-11-21 10:06 | 3s | 0 | `T1592` | 🟢 LOW |
| `156.225.1[.]88` | 1 | 2026-11-21 07:07 | 2026-11-21 07:07 | 9s | 0 | `T1592` | 🟢 LOW |
| `156.225.1[.]90` | 1 | 2026-11-21 12:23 | 2026-11-21 12:23 | 15s | 0 | `T1592` | 🟢 LOW |
| `160.3.5[.]133` | 1 | 2026-11-21 05:34 | 2026-11-21 05:36 | 120s | 0 | `T1592` | 🟢 LOW |
| `161.22.68[.]23` | 1 | 2026-11-21 15:51 | 2026-11-21 15:51 | 0s | 0 | `T1592` | 🟢 LOW |
| `165.22.105[.]175` | 1 | 2026-11-21 05:30 | 2026-11-21 05:30 | 20s | 0 | `T1592` | 🟢 LOW |
| `165.22.105[.]175` | 1 | 2026-11-21 09:08 | 2026-11-21 09:10 | 120s | 0 | `T1592` | 🟢 LOW |
| `165.227.55[.]4` | 1 | 2026-11-21 09:36 | 2026-11-21 09:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `169.128.70[.]53` | 1 | 2026-11-21 03:42 | 2026-11-21 03:42 | 0s | 0 | `T1592` | 🟢 LOW |
| `169.128.70[.]53` | 1 | 2026-11-21 08:01 | 2026-11-21 08:01 | 0s | 0 | `T1592` | 🟢 LOW |
| `169.128.70[.]53` | 1 | 2026-11-21 11:31 | 2026-11-21 11:31 | 0s | 0 | `T1592` | 🟢 LOW |
| `169.128.70[.]53` | 1 | 2026-11-21 14:19 | 2026-11-21 14:19 | 0s | 0 | `T1592` | 🟢 LOW |
| `170.231.236[.]98` | 1 | 2026-11-21 07:09 | 2026-11-21 07:09 | 11s | 0 | `T1592` | 🟢 LOW |
| `170.231.237[.]214` | 1 | 2026-11-21 07:09 | 2026-11-21 07:10 | 32s | 0 | `T1592` | 🟢 LOW |
| `172.236.228[.]220` | 1 | 2026-11-21 13:09 | 2026-11-21 13:09 | 0s | 0 | `T1592` | 🟢 LOW |
| `175.202.194[.]168` | 1 | 2026-11-21 06:46 | 2026-11-21 06:46 | 26s | 0 | `T1592` | 🟢 LOW |
| `175.206.251[.]46` | 1 | 2026-11-21 14:25 | 2026-11-21 14:25 | 25s | 0 | `T1592` | 🟢 LOW |
| `179.254.92[.]3` | 1 | 2026-11-21 05:54 | 2026-11-21 05:54 | 0s | 0 | `T1592` | 🟢 LOW |
| `18.116.101[.]220` | 1 | 2026-11-21 05:31 | 2026-11-21 05:31 | 0s | 0 | `T1592` | 🟢 LOW |
| `18.218.118[.]203` | 1 | 2026-11-21 07:45 | 2026-11-21 07:45 | 9s | 0 | `T1592` | 🟢 LOW |
| `18.225.206[.]49` | 1 | 2026-11-21 07:10 | 2026-11-21 07:10 | 32s | 0 | `T1592` | 🟢 LOW |
| `180.184.61[.]83` | 1 | 2026-11-21 16:04 | 2026-11-21 16:06 | 120s | 0 | `T1592` | 🟢 LOW |
| `185.191.236[.]38` | 1 | 2026-11-21 08:33 | 2026-11-21 08:33 | 6s | 0 | `T1592` | 🟢 LOW |
| `189.5.22[.]163` | 1 | 2026-11-21 03:30 | 2026-11-21 03:32 | 120s | 0 | `T1592` | 🟢 LOW |
| `193.106.63[.]45` | 1 | 2026-11-21 10:33 | 2026-11-21 10:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.32.162[.]15` | 1 | 2026-11-21 08:09 | 2026-11-21 08:09 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.32.162[.]15` | 1 | 2026-11-21 15:23 | 2026-11-21 15:23 | 0s | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]78` | 1 | 2026-11-21 04:05 | 2026-11-21 04:05 | 1s | 1 | `T1110.001` | 🟢 LOW |
| `195.178.110[.]78` | 1 | 2026-11-21 06:14 | 2026-11-21 06:14 | 1s | 1 | `T1110.001` | 🟢 LOW |
| `195.178.110[.]78` | 1 | 2026-11-21 12:06 | 2026-11-21 12:06 | 1s | 1 | `T1110.001` | 🟢 LOW |
| `195.178.110[.]78` | 1 | 2026-11-21 14:37 | 2026-11-21 14:37 | 1s | 1 | `T1110.001` | 🟢 LOW |
| `195.96.139[.]137` | 1 | 2026-11-21 15:26 | 2026-11-21 15:26 | 0s | 0 | `T1592` | 🟢 LOW |
| `200.138.46[.]86` | 1 | 2026-11-21 06:06 | 2026-11-21 06:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `200.59.191[.]225` | 1 | 2026-11-21 14:04 | 2026-11-21 14:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `201.79.0[.]92` | 1 | 2026-11-21 08:16 | 2026-11-21 08:16 | 0s | 0 | `T1592` | 🟢 LOW |
| `210.123.158[.]112` | 1 | 2026-11-21 15:39 | 2026-11-21 15:39 | 13s | 0 | `T1592` | 🟢 LOW |
| `211.185.81[.]244` | 1 | 2026-11-21 12:54 | 2026-11-21 12:54 | 0s | 0 | `T1592` | 🟢 LOW |
| `216.218.206[.]69` | 1 | 2026-11-21 12:16 | 2026-11-21 12:16 | 0s | 0 | `T1592` | 🟢 LOW |
| `218.158.190[.]6` | 1 | 2026-11-21 11:48 | 2026-11-21 11:48 | 29s | 0 | `T1592` | 🟢 LOW |
| `23.132.164[.]185` | 1 | 2026-11-21 15:23 | 2026-11-21 15:23 | 0s | 0 | `T1592` | 🟢 LOW |
| `35.210.163[.]9` | 1 | 2026-11-21 03:14 | 2026-11-21 03:14 | 0s | 0 | `T1592` | 🟢 LOW |
| `35.210.18[.]235` | 1 | 2026-11-21 03:26 | 2026-11-21 03:26 | 0s | 0 | `T1592` | 🟢 LOW |
| `35.210.94[.]212` | 1 | 2026-11-21 04:18 | 2026-11-21 04:18 | 3s | 0 | `T1592` | 🟢 LOW |
| `36.107.225[.]185` | 1 | 2026-11-21 03:33 | 2026-11-21 03:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `36.231.135[.]128` | 1 | 2026-11-21 11:52 | 2026-11-21 11:52 | 22s | 0 | `T1592` | 🟢 LOW |
| `40.124.83[.]225` | 1 | 2026-11-21 08:32 | 2026-11-21 08:32 | 10s | 0 | `T1592` | 🟢 LOW |
| `43.103.47[.]152` | 1 | 2026-11-21 07:37 | 2026-11-21 07:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.156.129[.]156` | 1 | 2026-11-21 03:58 | 2026-11-21 03:58 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.77.61[.]56` | 1 | 2026-11-21 03:45 | 2026-11-21 03:45 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.115[.]134` | 1 | 2026-11-21 08:44 | 2026-11-21 08:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `46.236.65[.]252` | 1 | 2026-11-21 05:47 | 2026-11-21 05:47 | 34s | 0 | `T1592` | 🟢 LOW |
| `47.251.31[.]157` | 1 | 2026-11-21 05:57 | 2026-11-21 05:57 | 0s | 0 | `T1592` | 🟢 LOW |
| `47.90.218[.]75` | 1 | 2026-11-21 06:00 | 2026-11-21 06:00 | 0s | 0 | `T1592` | 🟢 LOW |
| `54.149.204[.]90` | 1 | 2026-11-21 07:10 | 2026-11-21 07:10 | 12s | 0 | `T1592` | 🟢 LOW |
| `62.108.202[.]22` | 1 | 2026-11-21 03:20 | 2026-11-21 03:20 | 21s | 0 | `T1592` | 🟢 LOW |
| `62.60.130[.]148` | 1 | 2026-11-21 07:06 | 2026-11-21 07:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `62.60.130[.]148` | 1 | 2026-11-21 13:09 | 2026-11-21 13:09 | 0s | 0 | `T1592` | 🟢 LOW |
| `62.60.130[.]148` | 1 | 2026-11-21 16:10 | 2026-11-21 16:10 | 0s | 0 | `T1592` | 🟢 LOW |
| `62.60.130[.]219` | 1 | 2026-11-21 04:09 | 2026-11-21 04:09 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]182` | 1 | 2026-11-21 07:29 | 2026-11-21 07:29 | 2s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]216` | 1 | 2026-11-21 04:57 | 2026-11-21 04:57 | 4s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]62` | 1 | 2026-11-21 06:32 | 2026-11-21 06:32 | 2s | 0 | `T1592` | 🟢 LOW |
| `65.49.1[.]80` | 1 | 2026-11-21 07:02 | 2026-11-21 07:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.159[.]87` | 1 | 2026-11-21 12:33 | 2026-11-21 12:33 | 4s | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]176` | 1 | 2026-11-21 06:35 | 2026-11-21 06:35 | 14s | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]206` | 1 | 2026-11-21 06:34 | 2026-11-21 06:34 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]102` | 1 | 2026-11-21 12:00 | 2026-11-21 12:00 | 1s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]103` | 1 | 2026-11-21 09:18 | 2026-11-21 09:18 | 2s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]160` | 1 | 2026-11-21 06:35 | 2026-11-21 06:35 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]213` | 1 | 2026-11-21 16:51 | 2026-11-21 16:51 | 1s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]240` | 1 | 2026-11-21 07:37 | 2026-11-21 07:38 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]241` | 1 | 2026-11-21 10:32 | 2026-11-21 10:32 | 0s | 0 | `T1592` | 🟢 LOW |
| `71.6.146[.]130` | 1 | 2026-11-21 04:44 | 2026-11-21 04:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-11-21 10:56 | 2026-11-21 10:56 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-11-21 14:44 | 2026-11-21 14:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]132` | 1 | 2026-11-21 12:13 | 2026-11-21 12:13 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]132` | 1 | 2026-11-21 15:33 | 2026-11-21 15:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]252` | 1 | 2026-11-21 08:12 | 2026-11-21 08:12 | 1s | 1 | `T1110.001` | 🟢 LOW |
| `77.239.124[.]252` | 1 | 2026-11-21 10:30 | 2026-11-21 10:30 | 1s | 1 | `T1110.001` | 🟢 LOW |
| `78.128.112[.]74` | 1 | 2026-11-21 04:24 | 2026-11-21 04:24 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `78.128.112[.]74` | 1 | 2026-11-21 08:56 | 2026-11-21 08:56 | 6s | 0 | `T1592` | 🟢 LOW |
| `78.128.112[.]74` | 1 | 2026-11-21 13:26 | 2026-11-21 13:26 | 6s | 0 | `T1592` | 🟢 LOW |
| `82.147.85[.]98` | 1 | 2026-11-21 16:30 | 2026-11-21 16:32 | 120s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]16` | 1 | 2026-11-21 04:43 | 2026-11-21 04:43 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]57` | 1 | 2026-11-21 11:46 | 2026-11-21 11:46 | 0s | 0 | `T1592` | 🟢 LOW |
| `86.54.31[.]32` | 1 | 2026-11-21 13:08 | 2026-11-21 13:08 | 0s | 0 | `T1592` | 🟢 LOW |
| `89.138.98[.]100` | 1 | 2026-11-21 07:38 | 2026-11-21 07:38 | 13s | 0 | `T1592` | 🟢 LOW |
| `91.144.21[.]210` | 1 | 2026-11-21 12:55 | 2026-11-21 12:55 | 4s | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]50` | 1 | 2026-11-21 10:37 | 2026-11-21 10:37 | 14s | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]64` | 1 | 2026-11-21 05:26 | 2026-11-21 05:26 | 6s | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]64` | 1 | 2026-11-21 08:28 | 2026-11-21 08:28 | 9s | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]75` | 1 | 2026-11-21 06:55 | 2026-11-21 06:55 | 0s | 0 | `T1592` | 🟢 LOW |
| `95.37.2[.]162` | 1 | 2026-11-21 10:52 | 2026-11-21 10:52 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `0056cc09cf81211b753d79839e3399935a2aa6dd0217232a294f3953b9a7fc26` | ELF Binary (Linux executable) (AArch64 64-bit) | `0056cc09cf81211b...` | 30/100 | 🟢 LOW | **2/75** 🔴 |
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `00deea7003eef2f30f2c84d1497a42c1f375d802ddd17bde455d5fde2a63631f` | ELF Binary (Linux executable) (x86-64 64-bit) | `00deea7003eef2f3...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 64/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `026cc4f630776e0c9d42905bf3e9b048fda4da68d58c66e4a2e5bb3d8a9d787c` | ELF Binary (Linux executable) (x86-64 64-bit) | `026cc4f630776e0c...` | 31/100 | 🟢 LOW | **4/75** 🔴 |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 42/100 | 🟡 MEDIUM | **30/75** 🔴 |
| `04fcb4584d4de9deb015261bed95adfe0ac7e399503cff848908c1675e196148` | Bash Script | `04fcb4584d4de9de...` | 57/100 | 🟡 MEDIUM | **18/75** 🔴 |
| `0583d9e18684b6297a1219d34dd99c1045658f58c3e9a74ca060d8499a5a0439` | Shell Script | `0583d9e18684b629...` | 70/100 | 🔴 HIGH | **2/75** 🔴 |
| `05af569c3595b01e0724bc96c989105467952fd22a8681a716cfa22ec070d78c` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `05af569c3595b01e...` | 84/100 | 🔴 HIGH | **37/75** 🔴 |
| `062ba629c7b2b914b289c8da0573c179fe86f2cb1f70a31f9a1400d563c3042a` | ELF Binary (Linux executable) (x86-64 64-bit) | `062ba629c7b2b914...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `06901d0a279cc5a062c5de6903102edbcface166424935b01d984580c3d7a928` | Bash Script | `06901d0a279cc5a0...` | 50/100 | 🟡 MEDIUM | Not in VT |
| `072cdf382cce83bc1a59d196a09b6dd1beca38a7a697f30f826633c836952442` | Bash Script | `072cdf382cce83bc...` | 57/100 | 🟡 MEDIUM | **19/75** 🔴 |
| `07c0a0af63dde8dc2e36dc58b630dcad6563263e992877aaa704530afb8a5656` | ELF Binary (Linux executable) (ARM 32-bit) | `07c0a0af63dde8dc...` | 86/100 | 🔴 HIGH | **40/75** 🔴 |
| `0886e17b38d09ef7b0855a2394dd33454939edb3f33a43096c93e0dccfe6a81c` | ELF Binary (Linux executable) (x86-64 64-bit) | `0886e17b38d09ef7...` | 34/100 | 🟢 LOW | **10/75** 🔴 |
| `094d2147548839ba5ed36d884983aaf14bd7ae650095dec96a1cf537d3b23b48` | ELF Binary (Linux executable) (x86-64 64-bit) | `094d2147548839ba...` | 45/100 | 🟡 MEDIUM | **39/74** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/75** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0c082e5b76630d08145c7badd020060e0ce50e333a9f28d39fe15ad6afc49d77` | Bash Script | `0c082e5b76630d08...` | 57/100 | 🟡 MEDIUM | **18/75** 🔴 |
| `0c99433c7d433d65ab890dcee20b330f262379d532bc76f91e18f09ecfa5fb54` | Shell Script | `0c99433c7d433d65...` | 30/100 | 🟢 LOW | 0/75 ✅ |
| `0cd01e621dce7d42e6d6db50ef3e16170e3b737586863ec600826c7b0d3ed423` | Unknown binary | `0cd01e621dce7d42...` | 0/100 | 🟢 LOW | Not in VT |
| `0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca` | Unknown binary | `0db4656687a425c4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0de787cffbec4dcc42e0ecd9491795c7dfe8fe4a955cb67a87544d5c36070982` | ELF Binary (Linux executable) (x86-64 64-bit) | `0de787cffbec4dcc...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `0fad00ddec16b67f3131aa4efffbe32d78fca178407895920b7549667d7bbfbf` | Bash Script | `0fad00ddec16b67f...` | 70/100 | 🔴 HIGH | **25/75** 🔴 |
| `107a9bfb3d0bb71a33ae17a9eac844a7a7562270a09b5ccce608a78316df0222` | ELF Binary (Linux executable) (x86 32-bit) | `107a9bfb3d0bb71a...` | 35/100 | 🟢 LOW | **13/75** 🔴 |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `13960b7e69159907f67f84ce6398d29f73686602ef2c36d837237288f4fe8785` | Bash Script | `13960b7e69159907...` | 58/100 | 🟡 MEDIUM | **20/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16254f69dc7011bdd51beb489af5e9825959e4098e565332da99f8cb58b7a76e` | ELF Binary (Linux executable) (x86 32-bit) | `16254f69dc7011bd...` | 30/100 | 🟢 LOW | **1/75** 🔴 |
| `163cb287fd8f81c13901eb4ddaea2db326213f4d2095e0e64321b9afd8300480` | ELF Binary (Linux executable) (x86 32-bit) | `163cb287fd8f81c1...` | 36/100 | 🟢 LOW | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 83/100 | 🔴 HIGH | **31/70** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `187b67e5e2116293144f4009b1f224ed09eea924dd4ade00741a66792a63b45a` | ELF Binary (Linux executable) (x86-64 64-bit) | `187b67e5e2116293...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `1913ed2ad175632b1b75e99bf5e291f551302b16dea51df318379e77a36f1ce9` | ELF Binary (Linux executable) (MIPS 32-bit) | `1913ed2ad175632b...` | 86/100 | 🔴 HIGH | **42/75** 🔴 |
| `1946ee7ec655de32199ce87390699db1e18d80438bdf01f3b813a929e5cce4e6` | ELF Binary (Linux executable) (MIPS 32-bit) | `1946ee7ec655de32...` | 58/100 | 🟡 MEDIUM | **45/75** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 70/100 | 🔴 HIGH | **27/75** 🔴 |
| `19e78c00d07f011fcb708ffb12f8dd2fd0f1e57faaf21129b53c7f68ae611e60` | ELF Binary (Linux executable) (x86-64 64-bit) | `19e78c00d07f011f...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `1bc1c784057dc4e36fcc913fe03b1f0cae8474063b486ae3443b9ef8bced9548` | Bash Script | `1bc1c784057dc4e3...` | 50/100 | 🟡 MEDIUM | Not in VT |
| `1bd3745a4f9043ead807d7777669b0dbf5b56985e5b3dd9d7cff8384154ea4a8` | ELF Binary (Linux executable) (x86-64 64-bit) | `1bd3745a4f9043ea...` | 45/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `1c847d3bd3ef4bf7e21a7091f1479e0e2ca432585ebea996653845b9adfb150e` | ELF Binary (Linux executable) (x86-64 64-bit) | `1c847d3bd3ef4bf7...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `1d64be0ba1bd9924c3e29ae460db9407e4e33afeb864c9e39377ae4a87fa09db` | Shell Script | `1d64be0ba1bd9924...` | 72/100 | 🔴 HIGH | **7/75** 🔴 |
| `1e5e56d2ffc990b1dd966e12a02d89d7dcad92c2f23c34834fbfa8c792d56520` | Unknown binary | `1e5e56d2ffc990b1...` | 22/100 | 🟢 LOW | **30/75** 🔴 |
| `1e70b63472772e3f5092ffe9c3573470e73590e6ab6d93fdcede1d368a5fd72d` | Bash Script | `1e70b63472772e3f...` | 60/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 54/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `1ec20680994f17b88492809aa5d135fb463c04ec5868639c5515126e2149a240` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ec20680994f17b8...` | 34/100 | 🟢 LOW | **10/75** 🔴 |

**Suspicious Indicators — HIGH Severity Samples:**

_`0583d9e18684b6297a1219d34dd99c1045658f58c3e9a74ca060d8499a5a0439` (0583d9e18684b6297a1219d3...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Download via TFTP` — `tftp`
- `Hardware recon` — `cat /proc/cpuinfo`

_`05af569c3595b01e0724bc96c989105467952fd22a8681a716cfa22ec070d78c` (05af569c3595b01e0724bc96...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Execution from /tmp` — `/tmp/.kworker`
- `chmod +x (make executable)` — `chmod +x`
- `Cron persistence` — `crontab`
- `RC script persistence` — `/etc/rc.`
- `Systemd persistence` — `systemctl enable`
- `IP:Port (possible C2)` — `64.89.161[.]96:55487`

_`07c0a0af63dde8dc2e36dc58b630dcad6563263e992877aaa704530afb8a5656` (07c0a0af63dde8dc2e36dc58...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Execution from /tmp` — `/tmp/bot`
- `chmod +x (make executable)` — `chmod +x`
- `Cron persistence` — `crontab`
- `RC script persistence` — `/etc/rc.`
- `Systemd persistence` — `systemctl enable`
- `IP:Port (possible C2)` — `64.89.160[.]222:55487`

_`09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` (09591253a95411d60c2b0d53...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Download via TFTP` — `tftp`
- `Download via ftpget` — `ftpget`
- `Execution from /tmp` — `/tmp/condi`
- `IP:Port (possible C2)` — `255.255.255[.]255:1900`

_`0fad00ddec16b67f3131aa4efffbe32d78fca178407895920b7549667d7bbfbf` (0fad00ddec16b67f3131aa4e...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `chmod +x (make executable)` — `chmod +x`

_`183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` (183fb8e38eeb1160f392f6d3...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Download via TFTP` — `tftp`
- `Download via ftpget` — `ftpget`
- `chmod +x (make executable)` — `chmod +x`

_`1913ed2ad175632b1b75e99bf5e291f551302b16dea51df318379e77a36f1ce9` (1913ed2ad175632b1b75e99b...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Download via TFTP` — `tftp`
- `chmod +x (make executable)` — `chmod +x`
- `Cron persistence` — `crontab`
- `IP:Port (possible C2)` — `255.255.255[.]255:1900`
- `Crypto miner binary` — `xmrig`

_`197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` (197c74408e15bd1168105f56...)_
- `Execution from /tmp` — `/tmp/clean_file`
- `Base64 decode (obfuscation)` — `base64 -d`
- `Cron persistence` — `crontab`

_`1d64be0ba1bd9924c3e29ae460db9407e4e33afeb864c9e39377ae4a87fa09db` (1d64be0ba1bd9924c3e29ae4...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Hardware recon` — `cat /proc/cpuinfo`
- `IP:Port (possible C2)` — `198.144.179[.]82:80`

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `151.243.11[.]188` | DE | LLC VASH KREDIT BANK | **100** ⚠️ | 21 |
| `71.6.146[.]130` | US | CariNet, Inc. | **100** ⚠️ | 0 |
| `111.33.71[.]238` | CN | China Mobile Communications Corporation | **100** ⚠️ | 50 |
| `66.132.195[.]213` | US | Censys, Inc. | **100** ⚠️ | 10 |
| `200.138.46[.]86` | NL | Triathlon Trading FZCO | **100** ⚠️ | 11 |
| `195.178.110[.]227` | NL | TECHOFF SRV LIMITED | **100** ⚠️ | 50 |
| `66.132.195[.]160` | US | Censys, Inc. | **100** ⚠️ | 11 |
| `54.149.204[.]90` | US | Amazon Technologies Inc. | **100** ⚠️ | 2 |
| `35.210.18[.]235` | BE | Google LLC | **100** ⚠️ | 2 |
| `95.37.2[.]162` | RU | PJSC Rostelecom | **100** ⚠️ | 2 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 198 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 196 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 88 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 16 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 12 |

---

## 🔕 False Positive Summary (66 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 8 |
| AbuseIPDB score 11 below threshold 25 | 4 |
| AbuseIPDB score 15 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 4 |
| AbuseIPDB score 17 below threshold 25 | 1 |
| AbuseIPDB score 19 below threshold 25 | 3 |
| AbuseIPDB score 20 below threshold 25 | 1 |
| AbuseIPDB score 21 below threshold 25 | 6 |
| AbuseIPDB score 23 below threshold 25 | 5 |
| AbuseIPDB score 24 below threshold 25 | 5 |
| AbuseIPDB score 4 below threshold 25 | 3 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 24 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 384 cases |
| Tool 34  | Credential Extractor        | ✅ 1842 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 30 fingerprints |
| Tool 36  | Command Clustering          | ✅ 104 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 163 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 66 filtered (17.2%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 74 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 39 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 187 priority case(s) shown individually · 123 recon entry/entries in table (7 group(s) consolidating 15 session(s)).

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
| CIS-2 | Software Inventory | MONITORING | data/tool_manifest.json (pipeline.yml tools) + data/tool_manifest_enriched.json (enriched_corpus.yml tools) — both auto-generated each run, together tracking all active tools across both workflows, languages, and I/O paths |
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
_Report time: 2026-11-21T18:27:37Z_

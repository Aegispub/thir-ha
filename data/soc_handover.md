# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-12 |
| **Generated At** | 2026-06-12T23:22:12Z |
| **Shift Time** | 23:22 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **275** |
| Confirmed Threats | **262** |
| False Positives Filtered | **13** (4.7%) |
| Unique Attacker IPs | **26** |
| Countries of Origin | **13** |
| High Severity Cases | **18** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **257** |
| Malware Samples Analyzed | **0** HIGH · **20** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **23** |
| Unique Credential Pairs | **12** |
| Unique Usernames | **3** |
| Unique Passwords | **11** |
| Successful Auth Pairs | **13** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 21 |
| `user` | 1 |
| `admin` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `` | 4 |
| `smo@@kkklss` | 4 |
| `LeitboGi0ro` | 3 |
| `123@@@` | 3 |
| `admin` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `` | 4 |
| `root` | `smo@@kkklss` | 4 |
| `root` | `LeitboGi0ro` | 3 |
| `root` | `123@@@` | 3 |
| `root` | `AA123321` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `user` | `user` | `31.56.209.125` | 2026-06-12T20:57:52 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-06-12T21:01:48 |
| `root` | `123@@@` | `64.110.90.250` | 2026-06-12T21:01:49 |
| `root` | `admin` | `176.65.139.130` | 2026-06-12T21:21:10 |
| `root` | `123@@@` | `129.153.145.135` | 2026-06-12T21:50:21 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-06-12T21:50:22 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-06-12T21:50:27 |
| `admin` | `admin` | `14.103.10.167` | 2026-06-12T22:21:46 |
| `root` | `admin123` | `176.65.139.130` | 2026-06-12T22:21:51 |
| `root` | `AA123321` | `128.199.225.7` | 2026-06-12T22:31:45 |
| `root` | `AA123321` | `130.12.180.51` | 2026-06-12T22:31:45 |
| `root` | `---fuck_you----` | `182.92.183.213` | 2026-06-12T22:48:21 |
| `root` | `﻿------fuck------` | `36.111.80.93` | 2026-06-12T22:51:19 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **275** |
| Sessions with Fingerprint | **10** |
| Unique HASSH Fingerprints | **10** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Paramiko (Python) | 10 |
| Go SSH scanner | 8 |
| Unknown | 3 |
| PuTTY | 1 |
| libssh | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `a2de0f306611...` | Mirai/variant | 10 | 2 |
| `4c20a8895324...` | Mirai/variant | 2 | 1 |
| `f1e5e9d24e5e...` | Mirai/variant | 2 | 1 |
| `98f63c4d9c87...` | Generic scanner | 2 | 2 |
| `5bd26477da54...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `a2de0f306611...` | Paramiko (Python) | 10 | 2 | Mirai/variant |
| `4c20a8895324...` | Go SSH scanner | 2 | 1 | Mirai/variant |
| `f1e5e9d24e5e...` | Go SSH scanner | 2 | 1 | Mirai/variant |
| `95420f9d932d...` | Unknown | 2 | 1 | — |
| `98f63c4d9c87...` | Go SSH scanner | 2 | 2 | Generic scanner |
| `5bd26477da54...` | PuTTY | 1 | 1 | Mirai/variant |
| `dd9bcf093c35...` | Unknown | 1 | 1 | Mirai/variant |
| `0a07365cc01f...` | Go SSH scanner | 1 | 1 | Generic scanner |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **3** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1082, T1592, T1105, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
echo SHELL_TEST
```
```
busybox TEST
```
```
cat /proc
```
```
cat /proc/1/root
```
Source IPs: `31.56.209.125`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
chmod +x clean.sh; sh clean.sh; rm -rf clean.sh; chmod +x setup.sh; sh setup.sh; rm -rf setup.sh; mkdir -p ~/.ssh; chattr -ia ~/.ssh/authorized_keys; echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCqHrvnL6l7rT/mt1AdgdY9tC1GPK216q0q/7neNVqm7AgvfJIM3ZKniGC3S5x6KOEApk+83GM4IKjCPfq007SvT07qh9AscVxegv66I5yuZTEaDAG6cPXxg3/0oXHTOTvxelgbRrMzfU5SEDAEi8+ByKMefE+pDVALgSTBYhol96hu1GthAMtPAFahqxrvaRR4nL4ijxOsmSLREoAb1lxiX7yvoYLT45/1c5dJdrJrQ60uKyieQ6FieWpO2xF6tzfdmHbiVdSmdw0BiCRwe+fuknZYQxIC1owAj2p5bc+nzVTi3mtBEk9rGpgBnJ1h
```
Source IPs: `130.12.180.51`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **26** |
| Unique ASNs | **21** |
| High-Risk ASNs | **16** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS396982` | Google LLC | 3 | LOW |
| `AS14061` | DigitalOcean, LLC | 2 | HIGH |
| `AS63949` | Akamai Connected Cloud | 2 | HIGH |
| `AS31898` | Oracle Corporation | 2 | HIGH |
| `AS23724` | IDC, China Telecommunications Corporation | 1 | HIGH |
| `AS202412` | Omegatech LTD | 1 | HIGH |
| `AS4134` | CHINANET BACKBONE | 1 | MEDIUM |
| `AS680` | Verein zur Foerderung eines Deutschen Forschungsnetzes e.V. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (17)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-2f85c58d81b0

| Field | Detail |
|---|---|
| **Source IP** | `31.56.209[.]125` |
| **First Seen** | 2026-06-12 20:57 |
| **Last Seen** | 2026-06-12 20:57 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST, busybox TEST, cat /proc, cat /proc/1/root` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 20:57:52` | `cowrie.session.connect` |
| `2026-06-12 20:57:52` | `cowrie.login.success` |
| `2026-06-12 20:57:53` | `cowrie.session.params` |
| `2026-06-12 20:57:53` | `cowrie.command.input` |
| `2026-06-12 20:57:54` | `cowrie.command.input` |
| `2026-06-12 20:57:55` | `cowrie.command.input` |
| `2026-06-12 20:57:56` | `cowrie.command.input` |
| `2026-06-12 20:57:56` | `cowrie.log.closed` |
| `2026-06-12 20:57:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.56.209[.]125` to AbuseIPDB if not already reported
- [ ] Block `31.56.209[.]125` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa9185c7e2f7

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-06-12 21:01 |
| **Last Seen** | 2026-06-12 21:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 21:01:47` | `cowrie.session.connect` |
| `2026-06-12 21:01:47` | `cowrie.client.version` |
| `2026-06-12 21:01:47` | `cowrie.client.kex` |
| `2026-06-12 21:01:48` | `cowrie.login.success` |
| `2026-06-12 21:01:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98734809f0ba

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-06-12 21:01 |
| **Last Seen** | 2026-06-12 21:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 21:01:48` | `cowrie.session.connect` |
| `2026-06-12 21:01:48` | `cowrie.client.version` |
| `2026-06-12 21:01:48` | `cowrie.client.kex` |
| `2026-06-12 21:01:49` | `cowrie.login.success` |
| `2026-06-12 21:01:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88212937d357

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]130` |
| **First Seen** | 2026-06-12 21:21 |
| **Last Seen** | 2026-06-12 21:21 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 21:21:05` | `cowrie.session.connect` |
| `2026-06-12 21:21:05` | `cowrie.client.version` |
| `2026-06-12 21:21:05` | `cowrie.client.kex` |
| `2026-06-12 21:21:10` | `cowrie.login.success` |
| `2026-06-12 21:21:11` | `cowrie.direct-tcpip.request` |
| `2026-06-12 21:21:11` | `cowrie.direct-tcpip.ja4` |
| `2026-06-12 21:21:11` | `cowrie.direct-tcpip.data` |
| `2026-06-12 21:21:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]130` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48a575bf4194

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-12 21:50 |
| **Last Seen** | 2026-06-12 21:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 21:50:21` | `cowrie.session.connect` |
| `2026-06-12 21:50:21` | `cowrie.client.version` |
| `2026-06-12 21:50:21` | `cowrie.client.kex` |
| `2026-06-12 21:50:21` | `cowrie.login.success` |
| `2026-06-12 21:50:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18018491db93

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-12 21:50 |
| **Last Seen** | 2026-06-12 21:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 21:50:21` | `cowrie.session.connect` |
| `2026-06-12 21:50:21` | `cowrie.client.version` |
| `2026-06-12 21:50:21` | `cowrie.client.kex` |
| `2026-06-12 21:50:22` | `cowrie.login.success` |
| `2026-06-12 21:50:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ff9121d60ac

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-12 21:50 |
| **Last Seen** | 2026-06-12 21:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 21:50:27` | `cowrie.session.connect` |
| `2026-06-12 21:50:27` | `cowrie.client.version` |
| `2026-06-12 21:50:27` | `cowrie.client.kex` |
| `2026-06-12 21:50:27` | `cowrie.login.success` |
| `2026-06-12 21:50:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7439490fa36d

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-12 21:50 |
| **Last Seen** | 2026-06-12 21:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 21:50:27` | `cowrie.session.connect` |
| `2026-06-12 21:50:27` | `cowrie.client.version` |
| `2026-06-12 21:50:27` | `cowrie.client.kex` |
| `2026-06-12 21:50:27` | `cowrie.login.success` |
| `2026-06-12 21:50:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc432af40603

| Field | Detail |
|---|---|
| **Source IP** | `14.103.10[.]167` |
| **First Seen** | 2026-06-12 22:20 |
| **Last Seen** | 2026-06-12 22:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 22:20:44` | `cowrie.session.connect` |
| `2026-06-12 22:20:46` | `cowrie.telnet.option` |
| `2026-06-12 22:20:48` | `cowrie.telnet.option` |
| `2026-06-12 22:21:46` | `cowrie.login.success` |
| `2026-06-12 22:21:47` | `cowrie.session.params` |

**Recommended Actions:**
- [ ] Submit `14.103.10[.]167` to AbuseIPDB if not already reported
- [ ] Block `14.103.10[.]167` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36e715e14b3a

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]130` |
| **First Seen** | 2026-06-12 22:21 |
| **Last Seen** | 2026-06-12 22:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 22:21:51` | `cowrie.session.connect` |
| `2026-06-12 22:21:51` | `cowrie.client.version` |
| `2026-06-12 22:21:51` | `cowrie.client.kex` |
| `2026-06-12 22:21:51` | `cowrie.login.success` |
| `2026-06-12 22:21:51` | `cowrie.direct-tcpip.request` |
| `2026-06-12 22:21:52` | `cowrie.direct-tcpip.ja4` |
| `2026-06-12 22:21:52` | `cowrie.direct-tcpip.data` |
| `2026-06-12 22:21:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]130` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08d1bcd2e442

| Field | Detail |
|---|---|
| **Source IP** | `128.199.225[.]7` |
| **First Seen** | 2026-06-12 22:31 |
| **Last Seen** | 2026-06-12 22:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 22:31:43` | `cowrie.session.connect` |
| `2026-06-12 22:31:44` | `cowrie.client.version` |
| `2026-06-12 22:31:44` | `cowrie.client.kex` |
| `2026-06-12 22:31:45` | `cowrie.login.success` |
| `2026-06-12 22:31:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `128.199.225[.]7` to AbuseIPDB if not already reported
- [ ] Block `128.199.225[.]7` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3cc9c2cbb10

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-06-12 22:31 |
| **Last Seen** | 2026-06-12 22:32 |
| **Session Duration** | 20s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `chmod +x clean.sh; sh clean.sh; rm -rf clean.sh; chmod +x setup.sh; sh setup.sh; rm -rf setup.sh; mkdir -p ~/.ssh; chattr -ia ~/.ssh/authorized_keys; echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCqHrvnL6l7rT/mt1AdgdY9tC1GPK216q0q/7neNVqm7AgvfJIM3ZKniGC3S5x6KOEApk+83GM4IKjCPfq007SvT07qh9AscVxegv66I5yuZTEaDAG6cPXxg3/0oXHTOTvxelgbRrMzfU5SEDAEi8+ByKMefE+pDVALgSTBYhol96hu1GthAMtPAFahqxrvaRR4nL4ijxOsmSLREoAb1lxiX7yvoYLT45/1c5dJdrJrQ60uKyieQ6FieWpO2xF6tzfdmHbiVdSmdw0BiCRwe+fuknZYQxIC1owAj2p5bc+nzVTi3mtBEk9rGpgBnJ1h` |
| **TTPs (MITRE)** | T1021.004 · T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 22:31:45` | `cowrie.session.connect` |
| `2026-06-12 22:31:45` | `cowrie.client.version` |
| `2026-06-12 22:31:45` | `cowrie.client.kex` |
| `2026-06-12 22:31:45` | `cowrie.login.success` |
| `2026-06-12 22:32:06` | `cowrie.session.params` |
| `2026-06-12 22:32:06` | `cowrie.command.input` |
| `2026-06-12 22:32:06` | `cowrie.log.closed` |
| `2026-06-12 22:32:06` | `cowrie.session.file_upload` |
| `2026-06-12 22:32:06` | `cowrie.session.file_upload` |
| `2026-06-12 22:32:06` | `cowrie.session.file_upload` |
| `2026-06-12 22:32:06` | `cowrie.session.file_upload` |
| `2026-06-12 22:32:06` | `cowrie.session.file_upload` |
| `2026-06-12 22:32:06` | `cowrie.session.file_upload` |
| `2026-06-12 22:32:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38b84901234a

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-12 22:35 |
| **Last Seen** | 2026-06-12 22:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 22:35:59` | `cowrie.session.connect` |
| `2026-06-12 22:35:59` | `cowrie.client.version` |
| `2026-06-12 22:35:59` | `cowrie.client.kex` |
| `2026-06-12 22:35:59` | `cowrie.login.success` |
| `2026-06-12 22:35:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c983f44eefb

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-12 22:35 |
| **Last Seen** | 2026-06-12 22:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 22:35:59` | `cowrie.session.connect` |
| `2026-06-12 22:35:59` | `cowrie.client.version` |
| `2026-06-12 22:35:59` | `cowrie.client.kex` |
| `2026-06-12 22:36:00` | `cowrie.login.success` |
| `2026-06-12 22:36:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36cb95f64450

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-12 22:36 |
| **Last Seen** | 2026-06-12 22:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 22:36:08` | `cowrie.session.connect` |
| `2026-06-12 22:36:08` | `cowrie.client.version` |
| `2026-06-12 22:36:08` | `cowrie.client.kex` |
| `2026-06-12 22:36:08` | `cowrie.login.success` |
| `2026-06-12 22:36:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c38d92129dec

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-12 22:36 |
| **Last Seen** | 2026-06-12 22:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 22:36:08` | `cowrie.session.connect` |
| `2026-06-12 22:36:08` | `cowrie.client.version` |
| `2026-06-12 22:36:08` | `cowrie.client.kex` |
| `2026-06-12 22:36:08` | `cowrie.login.success` |
| `2026-06-12 22:36:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6209b6a3a1b2

| Field | Detail |
|---|---|
| **Source IP** | `36.111.80[.]93` |
| **First Seen** | 2026-06-12 22:51 |
| **Last Seen** | 2026-06-12 22:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 22:51:17` | `cowrie.session.connect` |
| `2026-06-12 22:51:18` | `cowrie.client.version` |
| `2026-06-12 22:51:18` | `cowrie.client.kex` |
| `2026-06-12 22:51:19` | `cowrie.login.success` |
| `2026-06-12 22:51:20` | `cowrie.session.params` |
| `2026-06-12 22:51:20` | `cowrie.command.input` |

**Recommended Actions:**
- [ ] Submit `36.111.80[.]93` to AbuseIPDB if not already reported
- [ ] Block `36.111.80[.]93` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `154.16.146[.]65` | **221** | 2026-06-12 20:55 | 2026-06-12 22:54 | 123m | 0 | `T1592` | 🟠 MEDIUM |
| `188.166.223[.]22` | **11** | 2026-06-12 21:02 | 2026-06-12 22:51 | 9m | 0 | `T1592` | 🟠 MEDIUM |
| `139.19.117[.]129` | **2** | 2026-06-12 21:43 | 2026-06-12 22:43 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `31.56.209[.]125` | **2** | 2026-06-12 20:57 | 2026-06-12 20:57 | 0m | 1 | `T1110.001` | 🟢 LOW |
| `95.215.0[.]144` | **2** | 2026-06-12 22:11 | 2026-06-12 22:11 | 0m | 0 | `T1592` | 🟢 LOW |
| `172.104.210[.]105` | 1 | 2026-06-12 21:37 | 2026-06-12 21:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `176.32.193[.]16` | 1 | 2026-06-12 22:10 | 2026-06-12 22:10 | 0s | 0 | `T1592` | 🟢 LOW |
| `194.187.176[.]145` | 1 | 2026-06-12 22:34 | 2026-06-12 22:34 | 4s | 0 | `T1592` | 🟢 LOW |
| `220.133.207[.]164` | 1 | 2026-06-12 20:59 | 2026-06-12 21:00 | 31s | 0 | `T1592` | 🟢 LOW |
| `36.111.80[.]93` | 1 | 2026-06-12 22:51 | 2026-06-12 22:51 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.227.254[.]170` | 1 | 2026-06-12 22:03 | 2026-06-12 22:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.90.185[.]16` | 1 | 2026-06-12 21:52 | 2026-06-12 21:52 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (35 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0d3d2e513043f33923c8538f0d40b246730eb64d685628c28b89b04b6efcabf3` | ELF Binary (Linux executable) (x86-64 64-bit) | `0d3d2e513043f339...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `20260429-011658-3f1992b60e9d-0-redir__root_a6s87d6as8zdgtdyas_ini` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260430-003018-0cc07f4bf950-0-redir__dev_watchdog` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `235596e7fb00cc04e95c500b5d02891e4b5d5ee54d063553a62c93b6bbd3eb9a` | ELF Binary (Linux executable) (ARM 32-bit) | `235596e7fb00cc04...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `2495e33392ef58d29cef5077b77c6c9164ad3f4cfb2c433b344df7e674542664` | Unknown binary | `2495e33392ef58d2...` | 0/100 | 🟢 LOW | Not in VT |
| `2b78990584d601289f89026783af9871061dc18c4e52a49d0b4caad6a7d3143a` | ELF Binary (Linux executable) (MIPS 32-bit) | `2b78990584d60128...` | 30/100 | 🟢 LOW | Not in VT |
| `321bfd80417496f99f32183c73d0a46b42900a8ae9d87b4079740b9297bc3cb4` | ELF Binary (Linux executable) (ARM 32-bit) | `321bfd80417496f9...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `6b3a55e0261b0304143f805a24924d0c1c44524821305f31d9277843b8a10f4e` | Unknown binary | `6b3a55e0261b0304...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `80c3fe2ae1062abf56456f52518bd670f9ec3917b7f85e152b347ac6b6faf880` | Unknown binary | `80c3fe2ae1062abf...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `99ac78541bb555b05a2c82d6c191d62e639b9fefd26ddee1f813b79cc6baf4f0` | ELF Binary (Linux executable) (MIPS 32-bit) | `99ac78541bb555b0...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `a2f3d6d2bd82a65939f4e939bce242e8e246014fb3a9a9d5c3769ed7dcfffe24` | Unknown binary | `a2f3d6d2bd82a659...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **32/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `fc6f8ae5f64e4f17481f7e3be29a1c56949f216a998414188003eae1db20c9e5` | GZip Archive | `fc6f8ae5f64e4f17...` | 14/100 | 🟢 LOW | **35/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `220.133.207[.]164` | TW | Chunghwa Telecom Data Communication Business Group | **100** ⚠️ | 50 |
| `176.32.193[.]16` | AM | Ucom CJSC | **100** ⚠️ | 50 |
| `154.16.146[.]65` | US | OC1-HostForWeb, LLC | **100** ⚠️ | 2 |
| `64.110.90[.]250` | KR | Oracle Corporation | **100** ⚠️ | 2 |
| `172.104.210[.]105` | US | Linode | **100** ⚠️ | 50 |
| `194.187.176[.]145` | DE | Alpha Strike Labs GmbH | **100** ⚠️ | 50 |
| `139.19.117[.]129` | DE | Max-Planck-Institut fuer Informatik | **100** ⚠️ | 50 |
| `130.12.180[.]51` | DE | Virtualine Technologies | **100** ⚠️ | 50 |
| `31.56.209[.]125` | NL | SWISSNET LLC | **100** ⚠️ | 24 |
| `176.65.139[.]130` | NL | Storm Industries | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 23 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 18 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 3 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 1 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 1 |

---

## 🔕 False Positive Summary (13 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 9 |
| AbuseIPDB score 24 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 2 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 275 cases |
| Tool 34  | Credential Extractor        | ✅ 23 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 10 fingerprints |
| Tool 36  | Command Clustering          | ✅ 3 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 26 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 13 filtered (4.7%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 21 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 35 files |
| Tool 33  | YARA Classifier             | ✅ 10 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 17 priority case(s) shown individually · 12 recon entry/entries in table (5 group(s) consolidating 238 session(s)).

---

## 📋 Standing Orders for Next Shift

- [ ] Verify honeypot is HEALTHY (Tool 05 green)
- [ ] Review any new HIGH/CRITICAL priority cases above
- [ ] Check AbuseIPDB for newly reported IPs from this shift
- [ ] If Cowrie captures a download, verify Tool 31 ran and check malware section
- [ ] Integrity baseline auto-recreates every 2 hours via pipeline

---

_Generated by THIR · Tool 28 v2.3 · SOC Handover Report Generator_  
_Pipeline: `Aegispub/thir-ha · Oracle Cloud HA_  
_Report time: 2026-06-12T23:22:12Z_

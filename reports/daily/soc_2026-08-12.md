# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-12 |
| **Generated At** | 2026-08-12T17:00:32Z |
| **Shift Time** | 17:00 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **159** |
| Confirmed Threats | **112** |
| False Positives Filtered | **47** (29.6%) |
| Unique Attacker IPs | **82** |
| Countries of Origin | **32** |
| High Severity Cases | **46** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **113** |
| Malware Samples Analyzed | **2** HIGH · **23** MED · 20 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **63** |
| Unique Credential Pairs | **27** |
| Unique Usernames | **19** |
| Unique Passwords | **21** |
| Successful Auth Pairs | **49** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `nobody` | 9 |
| `admin` | 8 |
| `root` | 7 |
| `unknown` | 5 |
| `user` | 5 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `Host: 129.80.119.236:23` | 10 |
| `` | 7 |
| `unknown11` | 5 |
| `asdfgh` | 5 |
| `webadmin` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `unknown` | `unknown11` | 5 |
| `user` | `asdfgh` | 5 |
| `admin` | `` | 4 |
| `centos` | `webadmin` | 4 |
| `debian` | `abc123` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `config` | `Password` | `10.0.0.73` | 2026-08-12T14:58:11 |
| `config` | `Password` | `124.160.45.26` | 2026-08-12T14:59:53 |
| `root` | `12341234` | `10.0.0.73` | 2026-08-12T15:02:06 |
| `root` | `ubuntu` | `121.125.67.137` | 2026-08-12T15:16:56 |
| `root` | `12341234` | `103.29.185.162` | 2026-08-12T15:19:34 |
| `unknown` | `unknown11` | `87.225.108.138` | 2026-08-12T15:24:47 |
| `unknown` | `unknown11` | `65.20.205.197` | 2026-08-12T15:24:55 |
| `nobody` | `P@ssword` | `58.226.255.240` | 2026-08-12T15:34:19 |
| `unknown` | `unknown11` | `10.0.0.73` | 2026-08-12T15:36:33 |
| `GET / HTTP/1.0` | `` | `167.172.161.8` | 2026-08-12T15:45:03 |
| `OPTIONS / HTTP/1.0` | `` | `167.172.161.8` | 2026-08-12T15:45:08 |
| `OPTIONS / RTSP/1.0` | `` | `167.172.161.8` | 2026-08-12T15:45:13 |
| `OPTIONS sip:nm SIP/2.0` | `Via: SIP/2.0/TCP nm;branch=foo` | `167.172.161.8` | 2026-08-12T15:45:51 |
| `GET /solr/admin/info/system HTTP/1.1` | `Host: 129.80.119.236:23` | `165.227.139.79` | 2026-08-12T15:45:59 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `159.223.18.78` | 2026-08-12T15:46:00 |
| `GET /solr/admin/cores?action=STATUS&wt=json HTTP/1.1` | `Host: 129.80.119.236:23` | `165.227.139.79` | 2026-08-12T15:46:02 |
| `root` | `---fuck_you----` | `117.149.196.165` | 2026-08-12T15:47:57 |
| `centos` | `webadmin` | `46.201.247.21` | 2026-08-12T15:48:01 |
| `centos` | `webadmin` | `196.189.59.226` | 2026-08-12T15:48:12 |
| `centos` | `webadmin` | `117.191.83.250` | 2026-08-12T15:48:17 |
| `centos` | `webadmin` | `202.138.229.190` | 2026-08-12T15:48:31 |
| `nobody` | `P@ssword` | `183.196.144.45` | 2026-08-12T15:50:45 |
| `nobody` | `P@ssword` | `120.224.15.67` | 2026-08-12T15:50:55 |
| `unknown` | `unknown11` | `121.178.185.141` | 2026-08-12T15:53:54 |
| `unknown` | `unknown11` | `125.36.68.227` | 2026-08-12T15:54:04 |
| `GET /query?q=SHOW+DIAGNOSTICS HTTP/1.1` | `Host: 129.80.119.236:23` | `165.22.74.170` | 2026-08-12T15:57:00 |
| `user` | `asdfgh` | `117.250.250.2` | 2026-08-12T15:59:23 |
| `user` | `asdfgh` | `178.178.194.134` | 2026-08-12T15:59:30 |
| `nobody` | `passw0rd` | `10.0.0.73` | 2026-08-12T16:03:54 |
| `root` | `debian` | `120.48.22.91` | 2026-08-12T16:05:40 |
| `support` | `support` | `176.53.159.196` | 2026-08-12T16:06:09 |
| `nobody` | `123456` | `10.0.0.73` | 2026-08-12T16:07:18 |
| `user` | `asdfgh` | `10.0.0.73` | 2026-08-12T16:11:07 |
| `root` | `kmi` | `45.154.244.193` | 2026-08-12T16:13:39 |
| `vpn` | `P@ssw0rd` | `52.168.141.47` | 2026-08-12T16:13:48 |
| `345gs5662d34` | `345gs5662d34` | `52.168.141.47` | 2026-08-12T16:13:51 |
| `vpn` | `3245gs5662d34` | `52.168.141.47` | 2026-08-12T16:13:51 |
| `nobody` | `passw0rd` | `96.56.228.149` | 2026-08-12T16:22:39 |
| `nobody` | `passw0rd` | `197.251.193.6` | 2026-08-12T16:22:45 |
| `nobody` | `123456` | `14.33.95.62` | 2026-08-12T16:25:14 |
| `user` | `asdfgh` | `92.126.223.175` | 2026-08-12T16:28:31 |
| `support` | `support` | `10.0.0.73` | 2026-08-12T16:30:56 |
| `debian` | `abc123` | `170.233.29.175` | 2026-08-12T16:33:45 |
| `debian` | `abc123` | `111.70.7.189` | 2026-08-12T16:33:54 |
| `admin` | `zaq1@WSX` | `10.0.0.73` | 2026-08-12T16:41:41 |
| `admin` | `zaq1@WSX` | `118.163.145.175` | 2026-08-12T16:43:15 |
| `admin` | `zaq1@WSX` | `222.174.184.86` | 2026-08-12T16:43:32 |
| `debian` | `abc123` | `10.0.0.73` | 2026-08-12T16:45:26 |
| `root` | `kmi` | `10.0.0.73` | 2026-08-12T16:54:42 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **159** |
| Sessions with Fingerprint | **11** |
| Unique HASSH Fingerprints | **11** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| OpenSSH | 23 |
| libssh | 9 |
| Go SSH scanner | 7 |
| PuTTY | 1 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 23 | 23 |
| `f555226df196...` | Mirai/variant | 3 | 1 |
| `f1e5e9d24e5e...` | Mirai/variant | 2 | 1 |
| `98ddc5604ef6...` | Modern SSH client | 2 | 2 |
| `16443846184e...` | Generic scanner | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 23 | 23 | Mirai/variant |
| `95420f9d932d...` | libssh | 5 | 2 | — |
| `f555226df196...` | libssh | 3 | 1 | Mirai/variant |
| `f1e5e9d24e5e...` | Go SSH scanner | 2 | 1 | Mirai/variant |
| `98ddc5604ef6...` | Go SSH scanner | 2 | 2 | Modern SSH client |
| `16443846184e...` | Go SSH scanner | 1 | 1 | Generic scanner |
| `98f63c4d9c87...` | Go SSH scanner | 1 | 1 | Generic scanner |
| `5bd26477da54...` | PuTTY | 1 | 1 | Mirai/variant |

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
Source IPs: `52.168.141.47`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **82** |
| Unique ASNs | **61** |
| High-Risk ASNs | **45** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS14061` | DigitalOcean, LLC | 7 | HIGH |
| `AS46562` | Performive LLC | 5 | MEDIUM |
| `AS4837` | CHINA UNICOM China169 Backbone | 3 | HIGH |
| `AS12389` | PJSC Rostelecom | 3 | HIGH |
| `AS4134` | CHINANET BACKBONE | 3 | HIGH |
| `AS9318` | SK Broadband Co Ltd | 2 | HIGH |
| `AS4766` | Korea Telecom | 2 | HIGH |
| `AS11427` | Charter Communications Inc | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (46)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-b5863179e415

| Field | Detail |
|---|---|
| **Source IP** | `124.160.45[.]26` |
| **First Seen** | 2026-08-12 14:59 |
| **Last Seen** | 2026-08-12 14:59 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 14:59:50` | `cowrie.session.connect` |
| `2026-08-12 14:59:50` | `cowrie.client.version` |
| `2026-08-12 14:59:50` | `cowrie.client.kex` |
| `2026-08-12 14:59:53` | `cowrie.login.success` |
| `2026-08-12 14:59:54` | `cowrie.direct-tcpip.request` |
| `2026-08-12 14:59:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.160.45[.]26` to AbuseIPDB if not already reported
- [ ] Block `124.160.45[.]26` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b1f35c8761f

| Field | Detail |
|---|---|
| **Source IP** | `121.125.67[.]137` |
| **First Seen** | 2026-08-12 15:16 |
| **Last Seen** | 2026-08-12 15:17 |
| **Session Duration** | 59s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 15:16:55` | `cowrie.session.connect` |
| `2026-08-12 15:16:55` | `cowrie.client.version` |
| `2026-08-12 15:16:56` | `cowrie.client.kex` |
| `2026-08-12 15:16:56` | `cowrie.login.success` |
| `2026-08-12 15:17:54` | `cowrie.session.file_upload` |
| `2026-08-12 15:17:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.125.67[.]137` to AbuseIPDB if not already reported
- [ ] Block `121.125.67[.]137` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0f66b61491b

| Field | Detail |
|---|---|
| **Source IP** | `103.29.185[.]162` |
| **First Seen** | 2026-08-12 15:19 |
| **Last Seen** | 2026-08-12 15:19 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 15:19:31` | `cowrie.session.connect` |
| `2026-08-12 15:19:32` | `cowrie.client.version` |
| `2026-08-12 15:19:32` | `cowrie.client.kex` |
| `2026-08-12 15:19:34` | `cowrie.login.success` |
| `2026-08-12 15:19:34` | `cowrie.direct-tcpip.request` |
| `2026-08-12 15:19:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.29.185[.]162` to AbuseIPDB if not already reported
- [ ] Block `103.29.185[.]162` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf17f79e7926

| Field | Detail |
|---|---|
| **Source IP** | `87.225.108[.]138` |
| **First Seen** | 2026-08-12 15:24 |
| **Last Seen** | 2026-08-12 15:24 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 15:24:45` | `cowrie.session.connect` |
| `2026-08-12 15:24:45` | `cowrie.client.version` |
| `2026-08-12 15:24:45` | `cowrie.client.kex` |
| `2026-08-12 15:24:47` | `cowrie.login.success` |
| `2026-08-12 15:24:47` | `cowrie.direct-tcpip.request` |
| `2026-08-12 15:24:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `87.225.108[.]138` to AbuseIPDB if not already reported
- [ ] Block `87.225.108[.]138` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-97d1c60f1c19

| Field | Detail |
|---|---|
| **Source IP** | `65.20.205[.]197` |
| **First Seen** | 2026-08-12 15:24 |
| **Last Seen** | 2026-08-12 15:25 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 15:24:53` | `cowrie.session.connect` |
| `2026-08-12 15:24:53` | `cowrie.client.version` |
| `2026-08-12 15:24:53` | `cowrie.client.kex` |
| `2026-08-12 15:24:55` | `cowrie.login.success` |
| `2026-08-12 15:24:55` | `cowrie.direct-tcpip.request` |
| `2026-08-12 15:25:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.205[.]197` to AbuseIPDB if not already reported
- [ ] Block `65.20.205[.]197` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-218dd36aa9fd

| Field | Detail |
|---|---|
| **Source IP** | `58.226.255[.]240` |
| **First Seen** | 2026-08-12 15:34 |
| **Last Seen** | 2026-08-12 15:34 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 15:34:17` | `cowrie.session.connect` |
| `2026-08-12 15:34:17` | `cowrie.client.version` |
| `2026-08-12 15:34:17` | `cowrie.client.kex` |
| `2026-08-12 15:34:19` | `cowrie.login.success` |
| `2026-08-12 15:34:20` | `cowrie.direct-tcpip.request` |
| `2026-08-12 15:34:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.226.255[.]240` to AbuseIPDB if not already reported
- [ ] Block `58.226.255[.]240` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86a985b0ae8c

| Field | Detail |
|---|---|
| **Source IP** | `167.172.161[.]8` |
| **First Seen** | 2026-08-12 15:44 |
| **Last Seen** | 2026-08-12 15:44 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 15:44:47` | `cowrie.session.connect` |
| `2026-08-12 15:44:53` | `cowrie.login.success` |
| `2026-08-12 15:44:53` | `cowrie.session.params` |
| `2026-08-12 15:44:58` | `cowrie.log.closed` |
| `2026-08-12 15:44:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `167.172.161[.]8` to AbuseIPDB if not already reported
- [ ] Block `167.172.161[.]8` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d953540094b8

| Field | Detail |
|---|---|
| **Source IP** | `167.172.161[.]8` |
| **First Seen** | 2026-08-12 15:45 |
| **Last Seen** | 2026-08-12 15:45 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 15:45:03` | `cowrie.session.connect` |
| `2026-08-12 15:45:03` | `cowrie.login.success` |
| `2026-08-12 15:45:03` | `cowrie.session.params` |
| `2026-08-12 15:45:08` | `cowrie.log.closed` |
| `2026-08-12 15:45:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `167.172.161[.]8` to AbuseIPDB if not already reported
- [ ] Block `167.172.161[.]8` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1bdd24f173df

| Field | Detail |
|---|---|
| **Source IP** | `167.172.161[.]8` |
| **First Seen** | 2026-08-12 15:45 |
| **Last Seen** | 2026-08-12 15:45 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 15:45:08` | `cowrie.session.connect` |
| `2026-08-12 15:45:08` | `cowrie.login.success` |
| `2026-08-12 15:45:08` | `cowrie.session.params` |
| `2026-08-12 15:45:13` | `cowrie.log.closed` |
| `2026-08-12 15:45:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `167.172.161[.]8` to AbuseIPDB if not already reported
- [ ] Block `167.172.161[.]8` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e300ebc30550

| Field | Detail |
|---|---|
| **Source IP** | `167.172.161[.]8` |
| **First Seen** | 2026-08-12 15:45 |
| **Last Seen** | 2026-08-12 15:45 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 15:45:13` | `cowrie.session.connect` |
| `2026-08-12 15:45:13` | `cowrie.login.success` |
| `2026-08-12 15:45:14` | `cowrie.session.params` |
| `2026-08-12 15:45:18` | `cowrie.log.closed` |
| `2026-08-12 15:45:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `167.172.161[.]8` to AbuseIPDB if not already reported
- [ ] Block `167.172.161[.]8` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-714939ca6b97

| Field | Detail |
|---|---|
| **Source IP** | `167.172.161[.]8` |
| **First Seen** | 2026-08-12 15:45 |
| **Last Seen** | 2026-08-12 15:45 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `From: <sip:nm@nm>;tag=root, To: <sip:nm2@nm2>, Call-ID: 50000, CSeq: 42 OPTIONS, Max-Forwards: 70` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 15:45:51` | `cowrie.session.connect` |
| `2026-08-12 15:45:51` | `cowrie.login.success` |
| `2026-08-12 15:45:52` | `cowrie.session.params` |
| `2026-08-12 15:45:52` | `cowrie.command.input` |
| `2026-08-12 15:45:52` | `cowrie.command.failed` |
| `2026-08-12 15:45:52` | `cowrie.command.input` |
| `2026-08-12 15:45:52` | `cowrie.command.failed` |
| `2026-08-12 15:45:52` | `cowrie.command.input` |
| `2026-08-12 15:45:52` | `cowrie.command.failed` |
| `2026-08-12 15:45:52` | `cowrie.command.input` |
| `2026-08-12 15:45:52` | `cowrie.command.failed` |
| `2026-08-12 15:45:52` | `cowrie.command.input` |
| `2026-08-12 15:45:52` | `cowrie.command.failed` |
| `2026-08-12 15:45:52` | `cowrie.command.input` |
| `2026-08-12 15:45:52` | `cowrie.command.failed` |
| `2026-08-12 15:45:52` | `cowrie.command.input` |
| `2026-08-12 15:45:52` | `cowrie.command.failed` |
| `2026-08-12 15:45:52` | `cowrie.command.input` |
| `2026-08-12 15:45:52` | `cowrie.command.failed` |
| `2026-08-12 15:45:52` | `cowrie.command.input` |
| `2026-08-12 15:45:59` | `cowrie.log.closed` |
| `2026-08-12 15:45:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `167.172.161[.]8` to AbuseIPDB if not already reported
- [ ] Block `167.172.161[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8210fe36658

| Field | Detail |
|---|---|
| **Source IP** | `165.227.139[.]79` |
| **First Seen** | 2026-08-12 15:45 |
| **Last Seen** | 2026-08-12 15:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Go-http-client/1.1, Connection: close` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 15:45:59` | `cowrie.session.connect` |
| `2026-08-12 15:45:59` | `cowrie.login.success` |
| `2026-08-12 15:46:00` | `cowrie.session.params` |
| `2026-08-12 15:46:00` | `cowrie.command.input` |
| `2026-08-12 15:46:00` | `cowrie.command.failed` |
| `2026-08-12 15:46:00` | `cowrie.command.input` |
| `2026-08-12 15:46:00` | `cowrie.command.failed` |
| `2026-08-12 15:46:00` | `cowrie.command.input` |
| `2026-08-12 15:46:00` | `cowrie.log.closed` |
| `2026-08-12 15:46:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.227.139[.]79` to AbuseIPDB if not already reported
- [ ] Block `165.227.139[.]79` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-283d48ba9f09

| Field | Detail |
|---|---|
| **Source IP** | `159.223.18[.]78` |
| **First Seen** | 2026-08-12 15:46 |
| **Last Seen** | 2026-08-12 15:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (compatible; Odin; hxxps://docs.getodin.com/), Accept: */*, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 15:46:00` | `cowrie.session.connect` |
| `2026-08-12 15:46:00` | `cowrie.login.success` |
| `2026-08-12 15:46:00` | `cowrie.session.params` |
| `2026-08-12 15:46:00` | `cowrie.command.input` |
| `2026-08-12 15:46:00` | `cowrie.command.input` |
| `2026-08-12 15:46:00` | `cowrie.command.failed` |
| `2026-08-12 15:46:00` | `cowrie.command.input` |
| `2026-08-12 15:46:00` | `cowrie.command.failed` |
| `2026-08-12 15:46:00` | `cowrie.command.input` |
| `2026-08-12 15:46:01` | `cowrie.log.closed` |
| `2026-08-12 15:46:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.18[.]78` to AbuseIPDB if not already reported
- [ ] Block `159.223.18[.]78` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-042ea73b4a53

| Field | Detail |
|---|---|
| **Source IP** | `165.227.139[.]79` |
| **First Seen** | 2026-08-12 15:46 |
| **Last Seen** | 2026-08-12 15:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Go-http-client/1.1, Connection: close` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 15:46:00` | `cowrie.session.connect` |
| `2026-08-12 15:46:00` | `cowrie.login.success` |
| `2026-08-12 15:46:01` | `cowrie.session.params` |
| `2026-08-12 15:46:01` | `cowrie.command.input` |
| `2026-08-12 15:46:01` | `cowrie.command.failed` |
| `2026-08-12 15:46:01` | `cowrie.command.input` |
| `2026-08-12 15:46:01` | `cowrie.command.failed` |
| `2026-08-12 15:46:01` | `cowrie.command.input` |
| `2026-08-12 15:46:01` | `cowrie.log.closed` |
| `2026-08-12 15:46:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.227.139[.]79` to AbuseIPDB if not already reported
- [ ] Block `165.227.139[.]79` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cee8460d162c

| Field | Detail |
|---|---|
| **Source IP** | `165.227.139[.]79` |
| **First Seen** | 2026-08-12 15:46 |
| **Last Seen** | 2026-08-12 15:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Go-http-client/1.1, Connection: close` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 15:46:01` | `cowrie.session.connect` |
| `2026-08-12 15:46:01` | `cowrie.login.success` |
| `2026-08-12 15:46:02` | `cowrie.session.params` |
| `2026-08-12 15:46:02` | `cowrie.command.input` |
| `2026-08-12 15:46:02` | `cowrie.command.failed` |
| `2026-08-12 15:46:02` | `cowrie.command.input` |
| `2026-08-12 15:46:02` | `cowrie.command.failed` |
| `2026-08-12 15:46:02` | `cowrie.command.input` |
| `2026-08-12 15:46:02` | `cowrie.log.closed` |
| `2026-08-12 15:46:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.227.139[.]79` to AbuseIPDB if not already reported
- [ ] Block `165.227.139[.]79` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94fd8abce31e

| Field | Detail |
|---|---|
| **Source IP** | `165.227.139[.]79` |
| **First Seen** | 2026-08-12 15:46 |
| **Last Seen** | 2026-08-12 15:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Go-http-client/1.1, Connection: close` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 15:46:02` | `cowrie.session.connect` |
| `2026-08-12 15:46:02` | `cowrie.login.success` |
| `2026-08-12 15:46:03` | `cowrie.session.params` |
| `2026-08-12 15:46:03` | `cowrie.command.input` |
| `2026-08-12 15:46:03` | `cowrie.command.failed` |
| `2026-08-12 15:46:03` | `cowrie.command.input` |
| `2026-08-12 15:46:03` | `cowrie.command.failed` |
| `2026-08-12 15:46:03` | `cowrie.command.input` |
| `2026-08-12 15:46:03` | `cowrie.log.closed` |
| `2026-08-12 15:46:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.227.139[.]79` to AbuseIPDB if not already reported
- [ ] Block `165.227.139[.]79` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-246ee983a679

| Field | Detail |
|---|---|
| **Source IP** | `165.227.139[.]79` |
| **First Seen** | 2026-08-12 15:46 |
| **Last Seen** | 2026-08-12 15:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Go-http-client/1.1, Connection: close` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 15:46:03` | `cowrie.session.connect` |
| `2026-08-12 15:46:03` | `cowrie.login.success` |
| `2026-08-12 15:46:04` | `cowrie.session.params` |
| `2026-08-12 15:46:04` | `cowrie.command.input` |
| `2026-08-12 15:46:04` | `cowrie.command.failed` |
| `2026-08-12 15:46:04` | `cowrie.command.input` |
| `2026-08-12 15:46:04` | `cowrie.command.failed` |
| `2026-08-12 15:46:04` | `cowrie.command.input` |
| `2026-08-12 15:46:04` | `cowrie.log.closed` |
| `2026-08-12 15:46:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.227.139[.]79` to AbuseIPDB if not already reported
- [ ] Block `165.227.139[.]79` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4bcc98bc76b7

| Field | Detail |
|---|---|
| **Source IP** | `165.227.139[.]79` |
| **First Seen** | 2026-08-12 15:46 |
| **Last Seen** | 2026-08-12 15:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Go-http-client/1.1, Connection: close` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 15:46:04` | `cowrie.session.connect` |
| `2026-08-12 15:46:04` | `cowrie.login.success` |
| `2026-08-12 15:46:04` | `cowrie.session.params` |
| `2026-08-12 15:46:04` | `cowrie.command.input` |
| `2026-08-12 15:46:04` | `cowrie.command.failed` |
| `2026-08-12 15:46:04` | `cowrie.command.input` |
| `2026-08-12 15:46:04` | `cowrie.command.failed` |
| `2026-08-12 15:46:04` | `cowrie.command.input` |
| `2026-08-12 15:46:04` | `cowrie.log.closed` |
| `2026-08-12 15:46:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.227.139[.]79` to AbuseIPDB if not already reported
- [ ] Block `165.227.139[.]79` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66b24915cb52

| Field | Detail |
|---|---|
| **Source IP** | `117.149.196[.]165` |
| **First Seen** | 2026-08-12 15:47 |
| **Last Seen** | 2026-08-12 15:48 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 15:47:50` | `cowrie.session.connect` |
| `2026-08-12 15:47:51` | `cowrie.client.version` |
| `2026-08-12 15:47:51` | `cowrie.client.kex` |
| `2026-08-12 15:47:57` | `cowrie.login.success` |
| `2026-08-12 15:48:02` | `cowrie.session.params` |
| `2026-08-12 15:48:02` | `cowrie.command.input` |
| `2026-08-12 15:48:04` | `cowrie.log.closed` |
| `2026-08-12 15:48:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.149.196[.]165` to AbuseIPDB if not already reported
- [ ] Block `117.149.196[.]165` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ea125014100

| Field | Detail |
|---|---|
| **Source IP** | `46.201.247[.]21` |
| **First Seen** | 2026-08-12 15:47 |
| **Last Seen** | 2026-08-12 15:48 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 15:47:59` | `cowrie.session.connect` |
| `2026-08-12 15:48:00` | `cowrie.client.version` |
| `2026-08-12 15:48:00` | `cowrie.client.kex` |
| `2026-08-12 15:48:01` | `cowrie.login.success` |
| `2026-08-12 15:48:01` | `cowrie.direct-tcpip.request` |
| `2026-08-12 15:48:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.201.247[.]21` to AbuseIPDB if not already reported
- [ ] Block `46.201.247[.]21` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7cf6ed64dc75

| Field | Detail |
|---|---|
| **Source IP** | `196.189.59[.]226` |
| **First Seen** | 2026-08-12 15:48 |
| **Last Seen** | 2026-08-12 15:48 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 15:48:10` | `cowrie.session.connect` |
| `2026-08-12 15:48:11` | `cowrie.client.version` |
| `2026-08-12 15:48:11` | `cowrie.client.kex` |
| `2026-08-12 15:48:12` | `cowrie.login.success` |
| `2026-08-12 15:48:13` | `cowrie.direct-tcpip.request` |
| `2026-08-12 15:48:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.189.59[.]226` to AbuseIPDB if not already reported
- [ ] Block `196.189.59[.]226` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-099d9623e255

| Field | Detail |
|---|---|
| **Source IP** | `117.191.83[.]250` |
| **First Seen** | 2026-08-12 15:48 |
| **Last Seen** | 2026-08-12 15:48 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 15:48:13` | `cowrie.session.connect` |
| `2026-08-12 15:48:14` | `cowrie.client.version` |
| `2026-08-12 15:48:14` | `cowrie.client.kex` |
| `2026-08-12 15:48:17` | `cowrie.login.success` |
| `2026-08-12 15:48:18` | `cowrie.direct-tcpip.request` |
| `2026-08-12 15:48:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.191.83[.]250` to AbuseIPDB if not already reported
- [ ] Block `117.191.83[.]250` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d62fe545d416

| Field | Detail |
|---|---|
| **Source IP** | `202.138.229[.]190` |
| **First Seen** | 2026-08-12 15:48 |
| **Last Seen** | 2026-08-12 15:48 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 15:48:28` | `cowrie.session.connect` |
| `2026-08-12 15:48:28` | `cowrie.client.version` |
| `2026-08-12 15:48:28` | `cowrie.client.kex` |
| `2026-08-12 15:48:31` | `cowrie.login.success` |
| `2026-08-12 15:48:31` | `cowrie.direct-tcpip.request` |
| `2026-08-12 15:48:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.138.229[.]190` to AbuseIPDB if not already reported
- [ ] Block `202.138.229[.]190` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-675ad4235754

| Field | Detail |
|---|---|
| **Source IP** | `183.196.144[.]45` |
| **First Seen** | 2026-08-12 15:50 |
| **Last Seen** | 2026-08-12 15:50 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 15:50:42` | `cowrie.session.connect` |
| `2026-08-12 15:50:43` | `cowrie.client.version` |
| `2026-08-12 15:50:43` | `cowrie.client.kex` |
| `2026-08-12 15:50:45` | `cowrie.login.success` |
| `2026-08-12 15:50:46` | `cowrie.direct-tcpip.request` |
| `2026-08-12 15:50:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.196.144[.]45` to AbuseIPDB if not already reported
- [ ] Block `183.196.144[.]45` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a82ecc3afb3a

| Field | Detail |
|---|---|
| **Source IP** | `120.224.15[.]67` |
| **First Seen** | 2026-08-12 15:50 |
| **Last Seen** | 2026-08-12 15:51 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 15:50:52` | `cowrie.session.connect` |
| `2026-08-12 15:50:52` | `cowrie.client.version` |
| `2026-08-12 15:50:52` | `cowrie.client.kex` |
| `2026-08-12 15:50:55` | `cowrie.login.success` |
| `2026-08-12 15:50:56` | `cowrie.direct-tcpip.request` |
| `2026-08-12 15:51:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.224.15[.]67` to AbuseIPDB if not already reported
- [ ] Block `120.224.15[.]67` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a78ee04710bf

| Field | Detail |
|---|---|
| **Source IP** | `121.178.185[.]141` |
| **First Seen** | 2026-08-12 15:53 |
| **Last Seen** | 2026-08-12 15:54 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 15:53:51` | `cowrie.session.connect` |
| `2026-08-12 15:53:52` | `cowrie.client.version` |
| `2026-08-12 15:53:52` | `cowrie.client.kex` |
| `2026-08-12 15:53:54` | `cowrie.login.success` |
| `2026-08-12 15:53:55` | `cowrie.direct-tcpip.request` |
| `2026-08-12 15:54:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.178.185[.]141` to AbuseIPDB if not already reported
- [ ] Block `121.178.185[.]141` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-674f7042124e

| Field | Detail |
|---|---|
| **Source IP** | `125.36.68[.]227` |
| **First Seen** | 2026-08-12 15:54 |
| **Last Seen** | 2026-08-12 15:54 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 15:54:01` | `cowrie.session.connect` |
| `2026-08-12 15:54:02` | `cowrie.client.version` |
| `2026-08-12 15:54:02` | `cowrie.client.kex` |
| `2026-08-12 15:54:04` | `cowrie.login.success` |
| `2026-08-12 15:54:04` | `cowrie.direct-tcpip.request` |
| `2026-08-12 15:54:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.36.68[.]227` to AbuseIPDB if not already reported
- [ ] Block `125.36.68[.]227` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16e07f4cb9cf

| Field | Detail |
|---|---|
| **Source IP** | `165.22.74[.]170` |
| **First Seen** | 2026-08-12 15:57 |
| **Last Seen** | 2026-08-12 15:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Go-http-client/1.1, Connection: close` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 15:57:00` | `cowrie.session.connect` |
| `2026-08-12 15:57:00` | `cowrie.login.success` |
| `2026-08-12 15:57:00` | `cowrie.session.params` |
| `2026-08-12 15:57:00` | `cowrie.command.input` |
| `2026-08-12 15:57:00` | `cowrie.command.failed` |
| `2026-08-12 15:57:00` | `cowrie.command.input` |
| `2026-08-12 15:57:00` | `cowrie.command.failed` |
| `2026-08-12 15:57:00` | `cowrie.command.input` |
| `2026-08-12 15:57:00` | `cowrie.log.closed` |
| `2026-08-12 15:57:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.22.74[.]170` to AbuseIPDB if not already reported
- [ ] Block `165.22.74[.]170` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52520a70c9ca

| Field | Detail |
|---|---|
| **Source IP** | `165.22.74[.]170` |
| **First Seen** | 2026-08-12 15:57 |
| **Last Seen** | 2026-08-12 15:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Go-http-client/1.1, Connection: close` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 15:57:01` | `cowrie.session.connect` |
| `2026-08-12 15:57:01` | `cowrie.login.success` |
| `2026-08-12 15:57:01` | `cowrie.session.params` |
| `2026-08-12 15:57:01` | `cowrie.command.input` |
| `2026-08-12 15:57:01` | `cowrie.command.failed` |
| `2026-08-12 15:57:01` | `cowrie.command.input` |
| `2026-08-12 15:57:01` | `cowrie.command.failed` |
| `2026-08-12 15:57:01` | `cowrie.command.input` |
| `2026-08-12 15:57:01` | `cowrie.log.closed` |
| `2026-08-12 15:57:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.22.74[.]170` to AbuseIPDB if not already reported
- [ ] Block `165.22.74[.]170` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6aa0e68e15e5

| Field | Detail |
|---|---|
| **Source IP** | `165.22.74[.]170` |
| **First Seen** | 2026-08-12 15:57 |
| **Last Seen** | 2026-08-12 15:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Go-http-client/1.1, Connection: close` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 15:57:01` | `cowrie.session.connect` |
| `2026-08-12 15:57:01` | `cowrie.login.success` |
| `2026-08-12 15:57:02` | `cowrie.session.params` |
| `2026-08-12 15:57:02` | `cowrie.command.input` |
| `2026-08-12 15:57:02` | `cowrie.command.failed` |
| `2026-08-12 15:57:02` | `cowrie.command.input` |
| `2026-08-12 15:57:02` | `cowrie.command.failed` |
| `2026-08-12 15:57:02` | `cowrie.command.input` |
| `2026-08-12 15:57:02` | `cowrie.log.closed` |
| `2026-08-12 15:57:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.22.74[.]170` to AbuseIPDB if not already reported
- [ ] Block `165.22.74[.]170` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f4241b85c2b

| Field | Detail |
|---|---|
| **Source IP** | `117.250.250[.]2` |
| **First Seen** | 2026-08-12 15:59 |
| **Last Seen** | 2026-08-12 15:59 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 15:59:20` | `cowrie.session.connect` |
| `2026-08-12 15:59:21` | `cowrie.client.version` |
| `2026-08-12 15:59:21` | `cowrie.client.kex` |
| `2026-08-12 15:59:23` | `cowrie.login.success` |
| `2026-08-12 15:59:23` | `cowrie.direct-tcpip.request` |
| `2026-08-12 15:59:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.250.250[.]2` to AbuseIPDB if not already reported
- [ ] Block `117.250.250[.]2` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-639b423c136e

| Field | Detail |
|---|---|
| **Source IP** | `178.178.194[.]134` |
| **First Seen** | 2026-08-12 15:59 |
| **Last Seen** | 2026-08-12 15:59 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 15:59:28` | `cowrie.session.connect` |
| `2026-08-12 15:59:29` | `cowrie.client.version` |
| `2026-08-12 15:59:29` | `cowrie.client.kex` |
| `2026-08-12 15:59:30` | `cowrie.login.success` |
| `2026-08-12 15:59:30` | `cowrie.direct-tcpip.request` |
| `2026-08-12 15:59:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.194[.]134` to AbuseIPDB if not already reported
- [ ] Block `178.178.194[.]134` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-029d039368f1

| Field | Detail |
|---|---|
| **Source IP** | `120.48.22[.]91` |
| **First Seen** | 2026-08-12 16:05 |
| **Last Seen** | 2026-08-12 16:10 |
| **Session Duration** | 325s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 16:05:15` | `cowrie.session.connect` |
| `2026-08-12 16:05:15` | `cowrie.client.version` |
| `2026-08-12 16:05:39` | `cowrie.client.kex` |
| `2026-08-12 16:05:40` | `cowrie.login.success` |
| `2026-08-12 16:10:40` | `cowrie.session.file_upload` |
| `2026-08-12 16:10:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.22[.]91` to AbuseIPDB if not already reported
- [ ] Block `120.48.22[.]91` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-389558114ab5

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-12 16:06 |
| **Last Seen** | 2026-08-12 16:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 16:06:08` | `cowrie.session.connect` |
| `2026-08-12 16:06:08` | `cowrie.client.version` |
| `2026-08-12 16:06:09` | `cowrie.client.kex` |
| `2026-08-12 16:06:09` | `cowrie.login.success` |
| `2026-08-12 16:06:09` | `cowrie.direct-tcpip.request` |
| `2026-08-12 16:06:09` | `cowrie.direct-tcpip.data` |
| `2026-08-12 16:06:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0161c693615

| Field | Detail |
|---|---|
| **Source IP** | `45.154.244[.]193` |
| **First Seen** | 2026-08-12 16:13 |
| **Last Seen** | 2026-08-12 16:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 16:13:39` | `cowrie.session.connect` |
| `2026-08-12 16:13:39` | `cowrie.client.version` |
| `2026-08-12 16:13:39` | `cowrie.client.kex` |
| `2026-08-12 16:13:39` | `cowrie.login.success` |
| `2026-08-12 16:13:39` | `cowrie.direct-tcpip.request` |
| `2026-08-12 16:13:39` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-12 16:13:39` | `cowrie.direct-tcpip.data` |
| `2026-08-12 16:13:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.154.244[.]193` to AbuseIPDB if not already reported
- [ ] Block `45.154.244[.]193` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0b94a6c9d9d

| Field | Detail |
|---|---|
| **Source IP** | `52.168.141[.]47` |
| **First Seen** | 2026-08-12 16:13 |
| **Last Seen** | 2026-08-12 16:13 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 16:13:46` | `cowrie.session.connect` |
| `2026-08-12 16:13:47` | `cowrie.client.version` |
| `2026-08-12 16:13:47` | `cowrie.client.kex` |
| `2026-08-12 16:13:48` | `cowrie.login.success` |
| `2026-08-12 16:13:49` | `cowrie.session.params` |
| `2026-08-12 16:13:49` | `cowrie.command.input` |
| `2026-08-12 16:13:49` | `cowrie.command.failed` |
| `2026-08-12 16:13:49` | `cowrie.log.closed` |
| `2026-08-12 16:13:49` | `cowrie.session.params` |
| `2026-08-12 16:13:49` | `cowrie.command.input` |
| `2026-08-12 16:13:50` | `cowrie.session.file_download` |
| `2026-08-12 16:13:50` | `cowrie.log.closed` |
| `2026-08-12 16:13:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `52.168.141[.]47` to AbuseIPDB if not already reported
- [ ] Block `52.168.141[.]47` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a2e5e453dac

| Field | Detail |
|---|---|
| **Source IP** | `52.168.141[.]47` |
| **First Seen** | 2026-08-12 16:13 |
| **Last Seen** | 2026-08-12 16:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 16:13:50` | `cowrie.session.connect` |
| `2026-08-12 16:13:50` | `cowrie.client.version` |
| `2026-08-12 16:13:50` | `cowrie.client.kex` |
| `2026-08-12 16:13:51` | `cowrie.login.success` |
| `2026-08-12 16:13:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `52.168.141[.]47` to AbuseIPDB if not already reported
- [ ] Block `52.168.141[.]47` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1aafeb67bb5f

| Field | Detail |
|---|---|
| **Source IP** | `52.168.141[.]47` |
| **First Seen** | 2026-08-12 16:13 |
| **Last Seen** | 2026-08-12 16:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 16:13:51` | `cowrie.session.connect` |
| `2026-08-12 16:13:51` | `cowrie.client.version` |
| `2026-08-12 16:13:51` | `cowrie.client.kex` |
| `2026-08-12 16:13:51` | `cowrie.login.success` |
| `2026-08-12 16:13:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `52.168.141[.]47` to AbuseIPDB if not already reported
- [ ] Block `52.168.141[.]47` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-847e3d9830cc

| Field | Detail |
|---|---|
| **Source IP** | `96.56.228[.]149` |
| **First Seen** | 2026-08-12 16:22 |
| **Last Seen** | 2026-08-12 16:22 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 16:22:37` | `cowrie.session.connect` |
| `2026-08-12 16:22:38` | `cowrie.client.version` |
| `2026-08-12 16:22:38` | `cowrie.client.kex` |
| `2026-08-12 16:22:39` | `cowrie.login.success` |
| `2026-08-12 16:22:39` | `cowrie.direct-tcpip.request` |
| `2026-08-12 16:22:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `96.56.228[.]149` to AbuseIPDB if not already reported
- [ ] Block `96.56.228[.]149` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c0050002ff1

| Field | Detail |
|---|---|
| **Source IP** | `197.251.193[.]6` |
| **First Seen** | 2026-08-12 16:22 |
| **Last Seen** | 2026-08-12 16:22 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 16:22:44` | `cowrie.session.connect` |
| `2026-08-12 16:22:44` | `cowrie.client.version` |
| `2026-08-12 16:22:44` | `cowrie.client.kex` |
| `2026-08-12 16:22:45` | `cowrie.login.success` |
| `2026-08-12 16:22:46` | `cowrie.direct-tcpip.request` |
| `2026-08-12 16:22:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.251.193[.]6` to AbuseIPDB if not already reported
- [ ] Block `197.251.193[.]6` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14232726718d

| Field | Detail |
|---|---|
| **Source IP** | `14.33.95[.]62` |
| **First Seen** | 2026-08-12 16:25 |
| **Last Seen** | 2026-08-12 16:25 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 16:25:11` | `cowrie.session.connect` |
| `2026-08-12 16:25:12` | `cowrie.client.version` |
| `2026-08-12 16:25:12` | `cowrie.client.kex` |
| `2026-08-12 16:25:14` | `cowrie.login.success` |
| `2026-08-12 16:25:15` | `cowrie.direct-tcpip.request` |
| `2026-08-12 16:25:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.33.95[.]62` to AbuseIPDB if not already reported
- [ ] Block `14.33.95[.]62` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7770c8b05698

| Field | Detail |
|---|---|
| **Source IP** | `92.126.223[.]175` |
| **First Seen** | 2026-08-12 16:28 |
| **Last Seen** | 2026-08-12 16:28 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 16:28:29` | `cowrie.session.connect` |
| `2026-08-12 16:28:29` | `cowrie.client.version` |
| `2026-08-12 16:28:29` | `cowrie.client.kex` |
| `2026-08-12 16:28:31` | `cowrie.login.success` |
| `2026-08-12 16:28:31` | `cowrie.direct-tcpip.request` |
| `2026-08-12 16:28:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.126.223[.]175` to AbuseIPDB if not already reported
- [ ] Block `92.126.223[.]175` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93b32d098a29

| Field | Detail |
|---|---|
| **Source IP** | `170.233.29[.]175` |
| **First Seen** | 2026-08-12 16:33 |
| **Last Seen** | 2026-08-12 16:33 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 16:33:42` | `cowrie.session.connect` |
| `2026-08-12 16:33:43` | `cowrie.client.version` |
| `2026-08-12 16:33:43` | `cowrie.client.kex` |
| `2026-08-12 16:33:45` | `cowrie.login.success` |
| `2026-08-12 16:33:46` | `cowrie.direct-tcpip.request` |
| `2026-08-12 16:33:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.233.29[.]175` to AbuseIPDB if not already reported
- [ ] Block `170.233.29[.]175` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e14395d47cc

| Field | Detail |
|---|---|
| **Source IP** | `111.70.7[.]189` |
| **First Seen** | 2026-08-12 16:33 |
| **Last Seen** | 2026-08-12 16:33 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 16:33:51` | `cowrie.session.connect` |
| `2026-08-12 16:33:52` | `cowrie.client.version` |
| `2026-08-12 16:33:52` | `cowrie.client.kex` |
| `2026-08-12 16:33:54` | `cowrie.login.success` |
| `2026-08-12 16:33:55` | `cowrie.direct-tcpip.request` |
| `2026-08-12 16:33:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.7[.]189` to AbuseIPDB if not already reported
- [ ] Block `111.70.7[.]189` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c16c3329d5e

| Field | Detail |
|---|---|
| **Source IP** | `118.163.145[.]175` |
| **First Seen** | 2026-08-12 16:43 |
| **Last Seen** | 2026-08-12 16:43 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 16:43:12` | `cowrie.session.connect` |
| `2026-08-12 16:43:13` | `cowrie.client.version` |
| `2026-08-12 16:43:13` | `cowrie.client.kex` |
| `2026-08-12 16:43:15` | `cowrie.login.success` |
| `2026-08-12 16:43:16` | `cowrie.direct-tcpip.request` |
| `2026-08-12 16:43:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.163.145[.]175` to AbuseIPDB if not already reported
- [ ] Block `118.163.145[.]175` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c449537892b8

| Field | Detail |
|---|---|
| **Source IP** | `222.174.184[.]86` |
| **First Seen** | 2026-08-12 16:43 |
| **Last Seen** | 2026-08-12 16:43 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 16:43:26` | `cowrie.session.connect` |
| `2026-08-12 16:43:28` | `cowrie.client.version` |
| `2026-08-12 16:43:28` | `cowrie.client.kex` |
| `2026-08-12 16:43:32` | `cowrie.login.success` |
| `2026-08-12 16:43:33` | `cowrie.direct-tcpip.request` |
| `2026-08-12 16:43:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.174.184[.]86` to AbuseIPDB if not already reported
- [ ] Block `222.174.184[.]86` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `210.16.100[.]120` | **20** | 2026-08-12 14:58 | 2026-08-12 16:46 | 14m | 0 | `T1592` | 🟠 MEDIUM |
| `139.199.80[.]137` | **4** | 2026-08-12 15:16 | 2026-08-12 16:39 | 0m | 0 | `T1592` | 🟢 LOW |
| `97.98.5[.]22` | **4** | 2026-08-12 15:21 | 2026-08-12 15:22 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]121` | **3** | 2026-08-12 15:10 | 2026-08-12 15:10 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]166` | **3** | 2026-08-12 15:37 | 2026-08-12 15:37 | 0m | 0 | `T1592` | 🟢 LOW |
| `88.214.25[.]125` | **3** | 2026-08-12 16:33 | 2026-08-12 16:33 | 0m | 0 | `T1592` | 🟢 LOW |
| `91.233.83[.]203` | **3** | 2026-08-12 16:13 | 2026-08-12 16:55 | 0m | 0 | `T1592` | 🟢 LOW |
| `107.150.146[.]69` | **2** | 2026-08-12 15:55 | 2026-08-12 16:07 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.19.117[.]129` | **2** | 2026-08-12 15:03 | 2026-08-12 16:03 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `164.92.189[.]151` | **2** | 2026-08-12 15:46 | 2026-08-12 15:46 | 0m | 0 | `T1592` | 🟢 LOW |
| `195.96.139[.]32` | **2** | 2026-08-12 15:02 | 2026-08-12 15:02 | 0m | 0 | `T1592` | 🟢 LOW |
| `117.149.196[.]165` | 1 | 2026-08-12 15:47 | 2026-08-12 15:47 | 0s | 0 | `T1592` | 🟢 LOW |
| `120.48.22[.]91` | 1 | 2026-08-12 15:50 | 2026-08-12 15:52 | 120s | 0 | `T1592` | 🟢 LOW |
| `153.37.177[.]219` | 1 | 2026-08-12 16:25 | 2026-08-12 16:27 | 120s | 0 | `T1592` | 🟢 LOW |
| `159.223.18[.]78` | 1 | 2026-08-12 15:46 | 2026-08-12 15:46 | 0s | 0 | `T1592` | 🟢 LOW |
| `161.35.201[.]29` | 1 | 2026-08-12 15:46 | 2026-08-12 15:46 | 0s | 0 | `T1592` | 🟢 LOW |
| `165.232.72[.]89` | 1 | 2026-08-12 15:46 | 2026-08-12 15:46 | 20s | 0 | `T1592` | 🟢 LOW |
| `177.67.156[.]50` | 1 | 2026-08-12 16:50 | 2026-08-12 16:52 | 120s | 0 | `T1592` | 🟢 LOW |
| `181.189.17[.]152` | 1 | 2026-08-12 15:45 | 2026-08-12 15:47 | 120s | 0 | `T1592` | 🟢 LOW |
| `190.97.239[.]58` | 1 | 2026-08-12 15:57 | 2026-08-12 15:58 | 10s | 0 | `T1592` | 🟢 LOW |
| `192.248.206[.]92` | 1 | 2026-08-12 16:08 | 2026-08-12 16:08 | 13s | 0 | `T1592` | 🟢 LOW |
| `199.229.254[.]131` | 1 | 2026-08-12 16:38 | 2026-08-12 16:40 | 120s | 0 | `T1592` | 🟢 LOW |
| `31.8.2[.]79` | 1 | 2026-08-12 15:38 | 2026-08-12 15:38 | 10s | 0 | `T1592` | 🟢 LOW |
| `42.248.129[.]234` | 1 | 2026-08-12 16:34 | 2026-08-12 16:35 | 11s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]141` | 1 | 2026-08-12 16:05 | 2026-08-12 16:05 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]110` | 1 | 2026-08-12 15:33 | 2026-08-12 15:33 | 1s | 0 | `T1592` | 🟢 LOW |
| `47.110.155[.]130` | 1 | 2026-08-12 15:41 | 2026-08-12 15:43 | 120s | 0 | `T1592` | 🟢 LOW |
| `70.32.86[.]195` | 1 | 2026-08-12 16:23 | 2026-08-12 16:24 | 30s | 0 | `T1592` | 🟢 LOW |
| `87.97.36[.]47` | 1 | 2026-08-12 15:30 | 2026-08-12 15:30 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 64/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/75** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca` | Unknown binary | `0db4656687a425c4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 83/100 | 🔴 HIGH | **33/75** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 41/100 | 🟡 MEDIUM | **29/75** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **24/75** 🔴 |
| `1e70b63472772e3f5092ffe9c3573470e73590e6ab6d93fdcede1d368a5fd72d` | Bash Script | `1e70b63472772e3f...` | 60/100 | 🟡 MEDIUM | **25/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 50/100 | 🟡 MEDIUM | **27/74** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `1eecf2377d20768c28d741e21affaa53cf26db0d083efdbf43a92fa938b7e4be` | ELF Binary (Linux executable) (ARM 32-bit) | `1eecf2377d20768c...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
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
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `287962211de7bcadb39f7576732438b43ee6aab420ec23c29a9d12a8151a547f` | ELF Binary (Linux executable) (x86 32-bit) | `287962211de7bcad...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `2f206563640dd66a743ffd493ce0e3c31a8fc5a24b9f5d2b540fc22d45c13d66` | ELF Binary (Linux executable) (x86 32-bit) | `2f206563640dd66a...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `31d4181843b1ed10a7e7cb3f108f6d6c50a7a4452ee52ddacabe8ca77260615e` | Bash Script | `31d4181843b1ed10...` | 60/100 | 🟡 MEDIUM | **26/75** 🔴 |

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
| `58.226.255[.]240` | KR | SK Broadband Co Ltd | **100** ⚠️ | 50 |
| `196.189.59[.]226` | ET | To__BRAS_DHCP_AD_10800E | **100** ⚠️ | 50 |
| `118.163.145[.]175` | TW | Chunghwa Telecom Data Communication Business Group | **100** ⚠️ | 50 |
| `164.92.189[.]151` | DE | DigitalOcean, LLC | **100** ⚠️ | 3 |
| `125.36.68[.]227` | CN | China Unicom Tianjin province network | **100** ⚠️ | 50 |
| `190.97.239[.]58` | VE | VIGINET C.A | **100** ⚠️ | 2 |
| `222.174.184[.]86` | CN | CHINANET SHANDONG PROVINCE NETWORK | **100** ⚠️ | 50 |
| `45.154.244[.]193` | FI | Shereverov Marat Ahmedovich | **100** ⚠️ | 44 |
| `46.201.247[.]21` | UA | JSC Ukrtelecom | **100** ⚠️ | 50 |
| `195.96.139[.]32` | GB | Driftnet Ltd | **100** ⚠️ | 7 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1078](https://attack.mitre.org/techniques/T1078) | 46 |
| [T1592](https://attack.mitre.org/techniques/T1592) | 41 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 3 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 2 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 1 |

---

## 🔕 False Positive Summary (47 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 7 |
| AbuseIPDB score 14 below threshold 25 | 3 |
| AbuseIPDB score 15 below threshold 25 | 2 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 17 below threshold 25 | 2 |
| AbuseIPDB score 19 below threshold 25 | 2 |
| AbuseIPDB score 24 below threshold 25 | 2 |
| AbuseIPDB score 3 below threshold 25 | 3 |
| AbuseIPDB score 4 below threshold 25 | 3 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 22 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 159 cases |
| Tool 34  | Credential Extractor        | ✅ 63 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 11 fingerprints |
| Tool 36  | Command Clustering          | ✅ 5 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 82 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 47 filtered (29.6%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 61 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 21 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 46 priority case(s) shown individually · 29 recon entry/entries in table (11 group(s) consolidating 48 session(s)).

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
_Report time: 2026-08-12T17:00:32Z_

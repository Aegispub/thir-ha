# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-20 |
| **Generated At** | 2026-08-20T02:59:58Z |
| **Shift Time** | 02:59 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **320** |
| Confirmed Threats | **297** |
| False Positives Filtered | **23** (7.2%) |
| Unique Attacker IPs | **66** |
| Countries of Origin | **28** |
| High Severity Cases | **103** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **217** |
| Malware Samples Analyzed | **2** HIGH · **22** MED · 20 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **128** |
| Unique Credential Pairs | **89** |
| Unique Usernames | **15** |
| Unique Passwords | **65** |
| Successful Auth Pairs | **114** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 41 |
| `admin` | 15 |
| `guest` | 10 |
| `postgres` | 10 |
| `user` | 10 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 7 |
| `unknown2002` | 6 |
| `password321` | 5 |
| `guest2003` | 5 |
| `root2000` | 5 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `unknown` | `unknown2002` | 6 |
| `default` | `password321` | 5 |
| `guest` | `guest2003` | 5 |
| `root` | `root2000` | 5 |
| `guest` | `guest2014` | 5 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Aa123456.` | `110.173.190.221` | 2026-08-20T00:55:54 |
| `default` | `password321` | `117.253.130.123` | 2026-08-20T00:56:37 |
| `default` | `password321` | `179.181.133.153` | 2026-08-20T00:56:46 |
| `guest` | `guest2003` | `10.0.0.73` | 2026-08-20T00:58:03 |
| `orange` | `orange` | `85.158.145.129` | 2026-08-20T00:59:12 |
| `guest` | `guest2003` | `122.166.253.226` | 2026-08-20T00:59:41 |
| `guest` | `guest2003` | `62.97.214.11` | 2026-08-20T00:59:49 |
| `support` | `support` | `176.53.159.196` | 2026-08-20T01:03:02 |
| `postfix` | `1234` | `85.158.145.129` | 2026-08-20T01:05:07 |
| `default` | `password321` | `10.0.0.73` | 2026-08-20T01:07:58 |
| `root` | `root@123` | `110.173.190.221` | 2026-08-20T01:08:13 |
| `postfix` | `12345` | `85.158.145.129` | 2026-08-20T01:11:03 |
| `ubnt` | `ubnt2018` | `10.0.0.73` | 2026-08-20T01:14:18 |
| `guest` | `guest2003` | `197.242.170.10` | 2026-08-20T01:15:32 |
| `postfix` | `123456` | `85.158.145.129` | 2026-08-20T01:16:58 |
| `root` | `Qwe123456` | `110.173.190.221` | 2026-08-20T01:20:34 |
| `postfix` | `admin` | `85.158.145.129` | 2026-08-20T01:22:53 |
| `default` | `password321` | `112.28.73.142` | 2026-08-20T01:24:28 |
| `default` | `password321` | `178.178.222.55` | 2026-08-20T01:24:36 |
| `support` | `support` | `10.0.0.73` | 2026-08-20T01:27:46 |
| `postfix` | `postfix` | `85.158.145.129` | 2026-08-20T01:28:49 |
| `root` | `root2000` | `120.194.50.39` | 2026-08-20T01:29:35 |
| `root` | `root2000` | `183.104.220.84` | 2026-08-20T01:29:44 |
| `guest` | `guest2014` | `10.0.0.73` | 2026-08-20T01:31:32 |
| `root` | `Admin123@` | `110.173.190.221` | 2026-08-20T01:32:57 |
| `guest` | `guest2014` | `192.34.128.202` | 2026-08-20T01:32:59 |
| `root` | `` | `91.92.40.233` | 2026-08-20T01:33:32 |
| `postgers` | `123456` | `85.158.145.129` | 2026-08-20T01:34:45 |
| `postgers` | `postgres` | `85.158.145.129` | 2026-08-20T01:40:40 |
| `root` | `root2000` | `10.0.0.73` | 2026-08-20T01:40:57 |
| `root` | `123456Abc` | `110.173.190.221` | 2026-08-20T01:45:21 |
| `postgres01` | `123456` | `85.158.145.129` | 2026-08-20T01:46:35 |
| `unknown` | `unknown2002` | `10.0.0.73` | 2026-08-20T01:47:21 |
| `guest` | `guest2014` | `103.29.185.162` | 2026-08-20T01:48:49 |
| `guest` | `guest2014` | `222.86.168.224` | 2026-08-20T01:48:59 |
| `postgres01` | `postgres01` | `85.158.145.129` | 2026-08-20T01:52:31 |
| `root` | `root2000` | `188.168.86.6` | 2026-08-20T01:57:37 |
| `root` | `root123` | `110.173.190.221` | 2026-08-20T01:57:46 |
| `root` | `admin` | `92.118.39.14` | 2026-08-20T01:58:10 |
| `postgres` | `1` | `85.158.145.129` | 2026-08-20T01:58:27 |
| `root` | `password` | `92.118.39.14` | 2026-08-20T01:59:18 |
| `root` | `toor` | `92.118.39.14` | 2026-08-20T02:01:40 |
| `root` | `root2010` | `218.58.73.238` | 2026-08-20T02:02:47 |
| `root` | `qwerty` | `92.118.39.14` | 2026-08-20T02:02:48 |
| `root` | `root2010` | `20.46.45.121` | 2026-08-20T02:02:55 |
| `root` | `12345` | `92.118.39.14` | 2026-08-20T02:03:55 |
| `postgres` | `111111` | `85.158.145.129` | 2026-08-20T02:04:23 |
| `ubnt` | `ubnt2024` | `10.0.0.73` | 2026-08-20T02:04:31 |
| `root` | `letmein` | `92.118.39.14` | 2026-08-20T02:05:01 |
| `unknown` | `unknown2002` | `117.32.132.170` | 2026-08-20T02:05:17 |
| `unknown` | `unknown2002` | `71.229.1.186` | 2026-08-20T02:05:26 |
| `unknown` | `unknown2002` | `182.60.128.241` | 2026-08-20T02:05:30 |
| `unknown` | `unknown2002` | `188.168.86.6` | 2026-08-20T02:05:41 |
| `root` | `123456789` | `92.118.39.14` | 2026-08-20T02:06:07 |
| `root` | `admin123` | `92.118.39.14` | 2026-08-20T02:07:13 |
| `root` | `welcome` | `92.118.39.14` | 2026-08-20T02:08:21 |
| `root` | `P@ssw0rd` | `92.118.39.14` | 2026-08-20T02:09:31 |
| `root` | `Root1234` | `110.173.190.221` | 2026-08-20T02:10:08 |
| `postgres` | `12` | `85.158.145.129` | 2026-08-20T02:10:18 |
| `root` | `passw0rd` | `92.118.39.14` | 2026-08-20T02:10:42 |
| `root` | `root123` | `92.118.39.14` | 2026-08-20T02:11:52 |
| `root` | `alpine` | `92.118.39.14` | 2026-08-20T02:13:05 |
| `root` | `changeme` | `92.118.39.14` | 2026-08-20T02:14:17 |
| `root` | `default` | `92.118.39.14` | 2026-08-20T02:15:28 |
| `postgres` | `123` | `85.158.145.129` | 2026-08-20T02:16:13 |
| `root` | `r00t` | `92.118.39.14` | 2026-08-20T02:16:38 |
| `root` | `root@123` | `92.118.39.14` | 2026-08-20T02:17:51 |
| `root` | `Root123` | `92.118.39.14` | 2026-08-20T02:18:57 |
| `root` | `!root` | `92.118.39.14` | 2026-08-20T02:20:05 |
| `nobody` | `nobody2018` | `10.0.0.73` | 2026-08-20T02:20:16 |
| `root` | `rootme` | `92.118.39.14` | 2026-08-20T02:21:13 |
| `ubnt` | `ubnt2024` | `65.20.161.126` | 2026-08-20T02:22:01 |
| `postgres` | `123123` | `85.158.145.129` | 2026-08-20T02:22:09 |
| `admin` | `admin` | `92.118.39.14` | 2026-08-20T02:22:19 |
| `root` | `AAAaaa123` | `110.173.190.221` | 2026-08-20T02:22:34 |
| `admin` | `password` | `92.118.39.14` | 2026-08-20T02:23:26 |
| `admin` | `123456` | `92.118.39.14` | 2026-08-20T02:24:32 |
| `admin` | `admin123` | `92.118.39.14` | 2026-08-20T02:25:40 |
| `admin` | `letmein` | `92.118.39.14` | 2026-08-20T02:26:45 |
| `admin` | `qwerty` | `92.118.39.14` | 2026-08-20T02:27:50 |
| `postgres` | `123&123` | `85.158.145.129` | 2026-08-20T02:28:05 |
| `admin` | `12345` | `92.118.39.14` | 2026-08-20T02:28:55 |
| `admin` | `admin@123` | `92.118.39.14` | 2026-08-20T02:30:01 |
| `root` | `root2010` | `182.75.197.174` | 2026-08-20T02:30:51 |
| `admin` | `Admin123` | `92.118.39.14` | 2026-08-20T02:31:06 |
| `admin` | `P@ssw0rd` | `92.118.39.14` | 2026-08-20T02:32:10 |
| `admin` | `welcome` | `92.118.39.14` | 2026-08-20T02:33:14 |
| `postgres` | `1234` | `85.158.145.129` | 2026-08-20T02:34:01 |
| `admin` | `passw0rd` | `92.118.39.14` | 2026-08-20T02:34:15 |
| `root` | `hao123.com` | `110.173.190.221` | 2026-08-20T02:34:58 |
| `admin` | `administrator` | `92.118.39.14` | 2026-08-20T02:35:20 |
| `support` | `support2025` | `60.249.252.94` | 2026-08-20T02:35:48 |
| `admin` | `adminroot` | `92.118.39.14` | 2026-08-20T02:36:22 |
| `admin` | `adminadmin` | `92.118.39.14` | 2026-08-20T02:37:25 |
| `nobody` | `nobody2018` | `65.20.179.251` | 2026-08-20T02:38:21 |
| `user` | `user` | `92.118.39.14` | 2026-08-20T02:38:30 |
| `nobody` | `nobody2018` | `177.135.206.10` | 2026-08-20T02:38:34 |
| `nobody` | `nobody2018` | `58.22.255.28` | 2026-08-20T02:38:44 |
| `user` | `password` | `92.118.39.14` | 2026-08-20T02:39:43 |
| `postgres` | `123456` | `85.158.145.129` | 2026-08-20T02:39:56 |
| `user` | `123456` | `92.118.39.14` | 2026-08-20T02:41:04 |
| `user` | `qwerty` | `92.118.39.14` | 2026-08-20T02:42:28 |
| `user` | `12345` | `92.118.39.14` | 2026-08-20T02:43:35 |
| `user` | `letmein` | `92.118.39.14` | 2026-08-20T02:44:40 |
| `user` | `welcome` | `92.118.39.14` | 2026-08-20T02:45:48 |
| `postgres` | `1234567` | `85.158.145.129` | 2026-08-20T02:45:52 |
| `support` | `support2025` | `10.0.0.73` | 2026-08-20T02:47:01 |
| `user` | `passw0rd` | `92.118.39.14` | 2026-08-20T02:47:01 |
| `root` | `abc123` | `110.173.190.221` | 2026-08-20T02:47:26 |
| `user` | `user123` | `92.118.39.14` | 2026-08-20T02:48:19 |
| `user` | `user1` | `92.118.39.14` | 2026-08-20T02:49:38 |
| `pi` | `abcd1234` | `10.0.0.73` | 2026-08-20T02:49:41 |
| `postgres` | `12345678` | `85.158.145.129` | 2026-08-20T02:51:47 |
| `ubnt` | `ubnt2021` | `10.0.0.73` | 2026-08-20T02:53:26 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **320** |
| Sessions with Fingerprint | **11** |
| Unique HASSH Fingerprints | **11** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 82 |
| OpenSSH | 28 |
| libssh | 6 |
| Paramiko (Python) | 2 |
| PuTTY | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `2ec37a7cc8da...` | Mirai/variant | 47 | 1 |
| `acaa53e0a7d7...` | Mirai/variant | 28 | 27 |
| `98f63c4d9c87...` | Generic scanner | 20 | 1 |
| `98ddc5604ef6...` | Modern SSH client | 10 | 1 |
| `eff4c24daffc...` | Modern SSH client | 2 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `2ec37a7cc8da...` | Go SSH scanner | 47 | 1 | Mirai/variant |
| `acaa53e0a7d7...` | OpenSSH | 28 | 27 | Mirai/variant |
| `98f63c4d9c87...` | Go SSH scanner | 20 | 1 | Generic scanner |
| `98ddc5604ef6...` | Go SSH scanner | 10 | 1 | Modern SSH client |
| `95420f9d932d...` | libssh | 6 | 2 | — |
| `eff4c24daffc...` | Go SSH scanner | 2 | 1 | Modern SSH client |
| `a704be057881...` | Paramiko (Python) | 2 | 1 | Mirai/variant |
| `5bd26477da54...` | PuTTY | 1 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **4** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 45 | 1 | `T1082, T1592, T1078, T1083` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1082, T1105, T1059.004` |

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
Source IPs: `92.118.39.14`

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
Source IPs: `91.92.40.233`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **66** |
| Unique ASNs | **50** |
| High-Risk ASNs | **40** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 4 | HIGH |
| `AS203214` | Hulum Almustakbal Company for Communication Engineering and Services Ltd | 4 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 3 | HIGH |
| `AS63949` | Akamai Connected Cloud | 3 | HIGH |
| `AS398324` | Censys, Inc. | 3 | HIGH |
| `AS25369` | Hydra Communications Ltd | 2 | HIGH |
| `AS9829` | National Internet Backbone | 2 | HIGH |
| `AS18881` | TELEFÔNICA BRASIL S.A | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (103)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-0a6a42c416a3

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]221` |
| **First Seen** | 2026-08-20 00:55 |
| **Last Seen** | 2026-08-20 00:55 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 00:55:46` | `cowrie.session.connect` |
| `2026-08-20 00:55:47` | `cowrie.client.version` |
| `2026-08-20 00:55:47` | `cowrie.client.kex` |
| `2026-08-20 00:55:54` | `cowrie.login.success` |
| `2026-08-20 00:55:58` | `cowrie.session.params` |
| `2026-08-20 00:55:58` | `cowrie.command.input` |
| `2026-08-20 00:55:59` | `cowrie.log.closed` |
| `2026-08-20 00:55:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]221` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f0e4922ae76

| Field | Detail |
|---|---|
| **Source IP** | `117.253.130[.]123` |
| **First Seen** | 2026-08-20 00:56 |
| **Last Seen** | 2026-08-20 00:56 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 00:56:34` | `cowrie.session.connect` |
| `2026-08-20 00:56:35` | `cowrie.client.version` |
| `2026-08-20 00:56:35` | `cowrie.client.kex` |
| `2026-08-20 00:56:37` | `cowrie.login.success` |
| `2026-08-20 00:56:38` | `cowrie.direct-tcpip.request` |
| `2026-08-20 00:56:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.253.130[.]123` to AbuseIPDB if not already reported
- [ ] Block `117.253.130[.]123` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b79c82335a3

| Field | Detail |
|---|---|
| **Source IP** | `179.181.133[.]153` |
| **First Seen** | 2026-08-20 00:56 |
| **Last Seen** | 2026-08-20 00:56 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 00:56:43` | `cowrie.session.connect` |
| `2026-08-20 00:56:44` | `cowrie.client.version` |
| `2026-08-20 00:56:44` | `cowrie.client.kex` |
| `2026-08-20 00:56:46` | `cowrie.login.success` |
| `2026-08-20 00:56:46` | `cowrie.direct-tcpip.request` |
| `2026-08-20 00:56:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.181.133[.]153` to AbuseIPDB if not already reported
- [ ] Block `179.181.133[.]153` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8894ff75494c

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-20 00:59 |
| **Last Seen** | 2026-08-20 00:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 00:59:11` | `cowrie.session.connect` |
| `2026-08-20 00:59:11` | `cowrie.client.version` |
| `2026-08-20 00:59:11` | `cowrie.client.kex` |
| `2026-08-20 00:59:12` | `cowrie.login.success` |
| `2026-08-20 00:59:12` | `cowrie.session.params` |
| `2026-08-20 00:59:12` | `cowrie.command.input` |
| `2026-08-20 00:59:13` | `cowrie.log.closed` |
| `2026-08-20 00:59:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aac402ee5ba4

| Field | Detail |
|---|---|
| **Source IP** | `122.166.253[.]226` |
| **First Seen** | 2026-08-20 00:59 |
| **Last Seen** | 2026-08-20 00:59 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 00:59:37` | `cowrie.session.connect` |
| `2026-08-20 00:59:38` | `cowrie.client.version` |
| `2026-08-20 00:59:38` | `cowrie.client.kex` |
| `2026-08-20 00:59:41` | `cowrie.login.success` |
| `2026-08-20 00:59:42` | `cowrie.direct-tcpip.request` |
| `2026-08-20 00:59:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.166.253[.]226` to AbuseIPDB if not already reported
- [ ] Block `122.166.253[.]226` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24a1d7c5dcb1

| Field | Detail |
|---|---|
| **Source IP** | `62.97.214[.]11` |
| **First Seen** | 2026-08-20 00:59 |
| **Last Seen** | 2026-08-20 00:59 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 00:59:47` | `cowrie.session.connect` |
| `2026-08-20 00:59:48` | `cowrie.client.version` |
| `2026-08-20 00:59:48` | `cowrie.client.kex` |
| `2026-08-20 00:59:49` | `cowrie.login.success` |
| `2026-08-20 00:59:49` | `cowrie.direct-tcpip.request` |
| `2026-08-20 00:59:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.97.214[.]11` to AbuseIPDB if not already reported
- [ ] Block `62.97.214[.]11` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5a95b15c008

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-20 01:03 |
| **Last Seen** | 2026-08-20 01:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 01:03:02` | `cowrie.session.connect` |
| `2026-08-20 01:03:02` | `cowrie.client.version` |
| `2026-08-20 01:03:02` | `cowrie.client.kex` |
| `2026-08-20 01:03:02` | `cowrie.login.success` |
| `2026-08-20 01:03:02` | `cowrie.direct-tcpip.request` |
| `2026-08-20 01:03:02` | `cowrie.direct-tcpip.data` |
| `2026-08-20 01:03:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7972fa5957e

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-20 01:05 |
| **Last Seen** | 2026-08-20 01:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 01:05:07` | `cowrie.session.connect` |
| `2026-08-20 01:05:07` | `cowrie.client.version` |
| `2026-08-20 01:05:07` | `cowrie.client.kex` |
| `2026-08-20 01:05:07` | `cowrie.login.success` |
| `2026-08-20 01:05:08` | `cowrie.session.params` |
| `2026-08-20 01:05:08` | `cowrie.command.input` |
| `2026-08-20 01:05:08` | `cowrie.log.closed` |
| `2026-08-20 01:05:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6cd994a3e25

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]221` |
| **First Seen** | 2026-08-20 01:08 |
| **Last Seen** | 2026-08-20 01:08 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 01:08:05` | `cowrie.session.connect` |
| `2026-08-20 01:08:06` | `cowrie.client.version` |
| `2026-08-20 01:08:06` | `cowrie.client.kex` |
| `2026-08-20 01:08:13` | `cowrie.login.success` |
| `2026-08-20 01:08:17` | `cowrie.session.params` |
| `2026-08-20 01:08:17` | `cowrie.command.input` |
| `2026-08-20 01:08:18` | `cowrie.log.closed` |
| `2026-08-20 01:08:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]221` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1bb343f61dc4

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-20 01:11 |
| **Last Seen** | 2026-08-20 01:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 01:11:02` | `cowrie.session.connect` |
| `2026-08-20 01:11:02` | `cowrie.client.version` |
| `2026-08-20 01:11:02` | `cowrie.client.kex` |
| `2026-08-20 01:11:03` | `cowrie.login.success` |
| `2026-08-20 01:11:04` | `cowrie.session.params` |
| `2026-08-20 01:11:04` | `cowrie.command.input` |
| `2026-08-20 01:11:04` | `cowrie.log.closed` |
| `2026-08-20 01:11:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad1eed09d8cb

| Field | Detail |
|---|---|
| **Source IP** | `197.242.170[.]10` |
| **First Seen** | 2026-08-20 01:15 |
| **Last Seen** | 2026-08-20 01:15 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 01:15:29` | `cowrie.session.connect` |
| `2026-08-20 01:15:30` | `cowrie.client.version` |
| `2026-08-20 01:15:30` | `cowrie.client.kex` |
| `2026-08-20 01:15:32` | `cowrie.login.success` |
| `2026-08-20 01:15:33` | `cowrie.direct-tcpip.request` |
| `2026-08-20 01:15:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.242.170[.]10` to AbuseIPDB if not already reported
- [ ] Block `197.242.170[.]10` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ddc533200ce

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-20 01:16 |
| **Last Seen** | 2026-08-20 01:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 01:16:58` | `cowrie.session.connect` |
| `2026-08-20 01:16:58` | `cowrie.client.version` |
| `2026-08-20 01:16:58` | `cowrie.client.kex` |
| `2026-08-20 01:16:58` | `cowrie.login.success` |
| `2026-08-20 01:16:59` | `cowrie.session.params` |
| `2026-08-20 01:16:59` | `cowrie.command.input` |
| `2026-08-20 01:16:59` | `cowrie.log.closed` |
| `2026-08-20 01:16:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02f30412f69c

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]221` |
| **First Seen** | 2026-08-20 01:20 |
| **Last Seen** | 2026-08-20 01:20 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 01:20:27` | `cowrie.session.connect` |
| `2026-08-20 01:20:28` | `cowrie.client.version` |
| `2026-08-20 01:20:28` | `cowrie.client.kex` |
| `2026-08-20 01:20:34` | `cowrie.login.success` |
| `2026-08-20 01:20:38` | `cowrie.session.params` |
| `2026-08-20 01:20:38` | `cowrie.command.input` |
| `2026-08-20 01:20:40` | `cowrie.log.closed` |
| `2026-08-20 01:20:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]221` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ecc87229f69

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-20 01:22 |
| **Last Seen** | 2026-08-20 01:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 01:22:53` | `cowrie.session.connect` |
| `2026-08-20 01:22:53` | `cowrie.client.version` |
| `2026-08-20 01:22:53` | `cowrie.client.kex` |
| `2026-08-20 01:22:53` | `cowrie.login.success` |
| `2026-08-20 01:22:54` | `cowrie.session.params` |
| `2026-08-20 01:22:54` | `cowrie.command.input` |
| `2026-08-20 01:22:54` | `cowrie.log.closed` |
| `2026-08-20 01:22:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52907a1e78ca

| Field | Detail |
|---|---|
| **Source IP** | `112.28.73[.]142` |
| **First Seen** | 2026-08-20 01:24 |
| **Last Seen** | 2026-08-20 01:24 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 01:24:25` | `cowrie.session.connect` |
| `2026-08-20 01:24:26` | `cowrie.client.version` |
| `2026-08-20 01:24:26` | `cowrie.client.kex` |
| `2026-08-20 01:24:28` | `cowrie.login.success` |
| `2026-08-20 01:24:29` | `cowrie.direct-tcpip.request` |
| `2026-08-20 01:24:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.28.73[.]142` to AbuseIPDB if not already reported
- [ ] Block `112.28.73[.]142` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6480075a231

| Field | Detail |
|---|---|
| **Source IP** | `178.178.222[.]55` |
| **First Seen** | 2026-08-20 01:24 |
| **Last Seen** | 2026-08-20 01:24 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 01:24:35` | `cowrie.session.connect` |
| `2026-08-20 01:24:35` | `cowrie.client.version` |
| `2026-08-20 01:24:35` | `cowrie.client.kex` |
| `2026-08-20 01:24:36` | `cowrie.login.success` |
| `2026-08-20 01:24:37` | `cowrie.direct-tcpip.request` |
| `2026-08-20 01:24:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.222[.]55` to AbuseIPDB if not already reported
- [ ] Block `178.178.222[.]55` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-926ee9c7d2ee

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-20 01:28 |
| **Last Seen** | 2026-08-20 01:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 01:28:49` | `cowrie.session.connect` |
| `2026-08-20 01:28:49` | `cowrie.client.version` |
| `2026-08-20 01:28:49` | `cowrie.client.kex` |
| `2026-08-20 01:28:49` | `cowrie.login.success` |
| `2026-08-20 01:28:50` | `cowrie.session.params` |
| `2026-08-20 01:28:50` | `cowrie.command.input` |
| `2026-08-20 01:28:50` | `cowrie.log.closed` |
| `2026-08-20 01:28:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d11d6e6d3f0d

| Field | Detail |
|---|---|
| **Source IP** | `120.194.50[.]39` |
| **First Seen** | 2026-08-20 01:29 |
| **Last Seen** | 2026-08-20 01:29 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 01:29:32` | `cowrie.session.connect` |
| `2026-08-20 01:29:33` | `cowrie.client.version` |
| `2026-08-20 01:29:33` | `cowrie.client.kex` |
| `2026-08-20 01:29:35` | `cowrie.login.success` |
| `2026-08-20 01:29:35` | `cowrie.direct-tcpip.request` |
| `2026-08-20 01:29:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.194.50[.]39` to AbuseIPDB if not already reported
- [ ] Block `120.194.50[.]39` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a8ab3c140cd

| Field | Detail |
|---|---|
| **Source IP** | `183.104.220[.]84` |
| **First Seen** | 2026-08-20 01:29 |
| **Last Seen** | 2026-08-20 01:29 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 01:29:41` | `cowrie.session.connect` |
| `2026-08-20 01:29:42` | `cowrie.client.version` |
| `2026-08-20 01:29:42` | `cowrie.client.kex` |
| `2026-08-20 01:29:44` | `cowrie.login.success` |
| `2026-08-20 01:29:44` | `cowrie.direct-tcpip.request` |
| `2026-08-20 01:29:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.104.220[.]84` to AbuseIPDB if not already reported
- [ ] Block `183.104.220[.]84` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e46a25841f5

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]221` |
| **First Seen** | 2026-08-20 01:32 |
| **Last Seen** | 2026-08-20 01:33 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 01:32:50` | `cowrie.session.connect` |
| `2026-08-20 01:32:51` | `cowrie.client.version` |
| `2026-08-20 01:32:51` | `cowrie.client.kex` |
| `2026-08-20 01:32:57` | `cowrie.login.success` |
| `2026-08-20 01:33:02` | `cowrie.session.params` |
| `2026-08-20 01:33:02` | `cowrie.command.input` |
| `2026-08-20 01:33:03` | `cowrie.log.closed` |
| `2026-08-20 01:33:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]221` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d212eaafaf89

| Field | Detail |
|---|---|
| **Source IP** | `192.34.128[.]202` |
| **First Seen** | 2026-08-20 01:32 |
| **Last Seen** | 2026-08-20 01:33 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 01:32:57` | `cowrie.session.connect` |
| `2026-08-20 01:32:57` | `cowrie.client.version` |
| `2026-08-20 01:32:57` | `cowrie.client.kex` |
| `2026-08-20 01:32:59` | `cowrie.login.success` |
| `2026-08-20 01:32:59` | `cowrie.direct-tcpip.request` |
| `2026-08-20 01:33:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `192.34.128[.]202` to AbuseIPDB if not already reported
- [ ] Block `192.34.128[.]202` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-009b459c4795

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-08-20 01:33 |
| **Last Seen** | 2026-08-20 01:33 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST, /bin/busybox TEST, cat /proc, ./` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 01:33:31` | `cowrie.session.connect` |
| `2026-08-20 01:33:32` | `cowrie.login.success` |
| `2026-08-20 01:33:32` | `cowrie.session.params` |
| `2026-08-20 01:33:33` | `cowrie.command.input` |
| `2026-08-20 01:33:33` | `cowrie.command.input` |
| `2026-08-20 01:33:34` | `cowrie.command.input` |
| `2026-08-20 01:33:34` | `cowrie.command.input` |
| `2026-08-20 01:33:34` | `cowrie.command.failed` |
| `2026-08-20 01:33:35` | `cowrie.log.closed` |
| `2026-08-20 01:33:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-412cd8bfa739

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-20 01:34 |
| **Last Seen** | 2026-08-20 01:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 01:34:44` | `cowrie.session.connect` |
| `2026-08-20 01:34:44` | `cowrie.client.version` |
| `2026-08-20 01:34:44` | `cowrie.client.kex` |
| `2026-08-20 01:34:45` | `cowrie.login.success` |
| `2026-08-20 01:34:45` | `cowrie.session.params` |
| `2026-08-20 01:34:45` | `cowrie.command.input` |
| `2026-08-20 01:34:45` | `cowrie.log.closed` |
| `2026-08-20 01:34:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2dedc55190eb

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-20 01:40 |
| **Last Seen** | 2026-08-20 01:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 01:40:40` | `cowrie.session.connect` |
| `2026-08-20 01:40:40` | `cowrie.client.version` |
| `2026-08-20 01:40:40` | `cowrie.client.kex` |
| `2026-08-20 01:40:40` | `cowrie.login.success` |
| `2026-08-20 01:40:41` | `cowrie.session.params` |
| `2026-08-20 01:40:41` | `cowrie.command.input` |
| `2026-08-20 01:40:41` | `cowrie.log.closed` |
| `2026-08-20 01:40:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18af998eb94e

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]221` |
| **First Seen** | 2026-08-20 01:45 |
| **Last Seen** | 2026-08-20 01:45 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 01:45:13` | `cowrie.session.connect` |
| `2026-08-20 01:45:14` | `cowrie.client.version` |
| `2026-08-20 01:45:14` | `cowrie.client.kex` |
| `2026-08-20 01:45:21` | `cowrie.login.success` |
| `2026-08-20 01:45:24` | `cowrie.session.params` |
| `2026-08-20 01:45:24` | `cowrie.command.input` |
| `2026-08-20 01:45:26` | `cowrie.log.closed` |
| `2026-08-20 01:45:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]221` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86fb9ab77a9c

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-20 01:46 |
| **Last Seen** | 2026-08-20 01:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 01:46:35` | `cowrie.session.connect` |
| `2026-08-20 01:46:35` | `cowrie.client.version` |
| `2026-08-20 01:46:35` | `cowrie.client.kex` |
| `2026-08-20 01:46:35` | `cowrie.login.success` |
| `2026-08-20 01:46:36` | `cowrie.session.params` |
| `2026-08-20 01:46:36` | `cowrie.command.input` |
| `2026-08-20 01:46:36` | `cowrie.log.closed` |
| `2026-08-20 01:46:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01e9e7fefadd

| Field | Detail |
|---|---|
| **Source IP** | `103.29.185[.]162` |
| **First Seen** | 2026-08-20 01:48 |
| **Last Seen** | 2026-08-20 01:48 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 01:48:43` | `cowrie.session.connect` |
| `2026-08-20 01:48:44` | `cowrie.client.version` |
| `2026-08-20 01:48:44` | `cowrie.client.kex` |
| `2026-08-20 01:48:49` | `cowrie.login.success` |
| `2026-08-20 01:48:57` | `cowrie.direct-tcpip.request` |
| `2026-08-20 01:48:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.29.185[.]162` to AbuseIPDB if not already reported
- [ ] Block `103.29.185[.]162` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d1e3a2758d7

| Field | Detail |
|---|---|
| **Source IP** | `222.86.168[.]224` |
| **First Seen** | 2026-08-20 01:48 |
| **Last Seen** | 2026-08-20 01:49 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 01:48:55` | `cowrie.session.connect` |
| `2026-08-20 01:48:56` | `cowrie.client.version` |
| `2026-08-20 01:48:56` | `cowrie.client.kex` |
| `2026-08-20 01:48:59` | `cowrie.login.success` |
| `2026-08-20 01:49:00` | `cowrie.direct-tcpip.request` |
| `2026-08-20 01:49:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.86.168[.]224` to AbuseIPDB if not already reported
- [ ] Block `222.86.168[.]224` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1aca2183cd5

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-20 01:52 |
| **Last Seen** | 2026-08-20 01:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 01:52:31` | `cowrie.session.connect` |
| `2026-08-20 01:52:31` | `cowrie.client.version` |
| `2026-08-20 01:52:31` | `cowrie.client.kex` |
| `2026-08-20 01:52:31` | `cowrie.login.success` |
| `2026-08-20 01:52:32` | `cowrie.session.params` |
| `2026-08-20 01:52:32` | `cowrie.command.input` |
| `2026-08-20 01:52:32` | `cowrie.log.closed` |
| `2026-08-20 01:52:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d8ae44f038c

| Field | Detail |
|---|---|
| **Source IP** | `188.168.86[.]6` |
| **First Seen** | 2026-08-20 01:57 |
| **Last Seen** | 2026-08-20 01:57 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 01:57:35` | `cowrie.session.connect` |
| `2026-08-20 01:57:36` | `cowrie.client.version` |
| `2026-08-20 01:57:36` | `cowrie.client.kex` |
| `2026-08-20 01:57:37` | `cowrie.login.success` |
| `2026-08-20 01:57:39` | `cowrie.direct-tcpip.request` |
| `2026-08-20 01:57:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `188.168.86[.]6` to AbuseIPDB if not already reported
- [ ] Block `188.168.86[.]6` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-413e4273726f

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]221` |
| **First Seen** | 2026-08-20 01:57 |
| **Last Seen** | 2026-08-20 01:57 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 01:57:39` | `cowrie.session.connect` |
| `2026-08-20 01:57:40` | `cowrie.client.version` |
| `2026-08-20 01:57:40` | `cowrie.client.kex` |
| `2026-08-20 01:57:46` | `cowrie.login.success` |
| `2026-08-20 01:57:49` | `cowrie.session.params` |
| `2026-08-20 01:57:49` | `cowrie.command.input` |
| `2026-08-20 01:57:52` | `cowrie.log.closed` |
| `2026-08-20 01:57:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]221` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0f7100aa7d2

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-20 01:58 |
| **Last Seen** | 2026-08-20 01:58 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 01:58:07` | `cowrie.session.connect` |
| `2026-08-20 01:58:07` | `cowrie.client.version` |
| `2026-08-20 01:58:07` | `cowrie.client.kex` |
| `2026-08-20 01:58:10` | `cowrie.login.success` |
| `2026-08-20 01:58:11` | `cowrie.session.params` |
| `2026-08-20 01:58:11` | `cowrie.command.input` |
| `2026-08-20 01:58:11` | `cowrie.command.input` |
| `2026-08-20 01:58:11` | `cowrie.command.input` |
| `2026-08-20 01:58:11` | `cowrie.command.input` |
| `2026-08-20 01:58:11` | `cowrie.command.input` |
| `2026-08-20 01:58:11` | `cowrie.command.success` |
| `2026-08-20 01:58:11` | `cowrie.command.input` |
| `2026-08-20 01:58:11` | `cowrie.command.input` |
| `2026-08-20 01:58:11` | `cowrie.command.input` |
| `2026-08-20 01:58:11` | `cowrie.command.input` |
| `2026-08-20 01:58:12` | `cowrie.log.closed` |
| `2026-08-20 01:58:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4b55e0dbd9f

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-20 01:58 |
| **Last Seen** | 2026-08-20 01:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 01:58:13` | `cowrie.session.connect` |
| `2026-08-20 01:58:13` | `cowrie.client.version` |
| `2026-08-20 01:58:13` | `cowrie.client.kex` |
| `2026-08-20 01:58:13` | `cowrie.login.success` |
| `2026-08-20 01:58:13` | `cowrie.direct-tcpip.request` |
| `2026-08-20 01:58:14` | `cowrie.direct-tcpip.data` |
| `2026-08-20 01:58:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f78dcbccf2c9

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-20 01:58 |
| **Last Seen** | 2026-08-20 01:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 01:58:27` | `cowrie.session.connect` |
| `2026-08-20 01:58:27` | `cowrie.client.version` |
| `2026-08-20 01:58:27` | `cowrie.client.kex` |
| `2026-08-20 01:58:27` | `cowrie.login.success` |
| `2026-08-20 01:58:28` | `cowrie.session.params` |
| `2026-08-20 01:58:28` | `cowrie.command.input` |
| `2026-08-20 01:58:28` | `cowrie.log.closed` |
| `2026-08-20 01:58:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ed3be8a50e8

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-20 01:59 |
| **Last Seen** | 2026-08-20 01:59 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 01:59:16` | `cowrie.session.connect` |
| `2026-08-20 01:59:16` | `cowrie.client.version` |
| `2026-08-20 01:59:16` | `cowrie.client.kex` |
| `2026-08-20 01:59:18` | `cowrie.login.success` |
| `2026-08-20 01:59:20` | `cowrie.session.params` |
| `2026-08-20 01:59:20` | `cowrie.command.input` |
| `2026-08-20 01:59:20` | `cowrie.command.input` |
| `2026-08-20 01:59:20` | `cowrie.command.input` |
| `2026-08-20 01:59:20` | `cowrie.command.input` |
| `2026-08-20 01:59:20` | `cowrie.command.input` |
| `2026-08-20 01:59:20` | `cowrie.command.success` |
| `2026-08-20 01:59:20` | `cowrie.command.input` |
| `2026-08-20 01:59:20` | `cowrie.command.input` |
| `2026-08-20 01:59:20` | `cowrie.command.input` |
| `2026-08-20 01:59:20` | `cowrie.command.input` |
| `2026-08-20 01:59:21` | `cowrie.log.closed` |
| `2026-08-20 01:59:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-921882b84384

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-20 02:01 |
| **Last Seen** | 2026-08-20 02:01 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 02:01:36` | `cowrie.session.connect` |
| `2026-08-20 02:01:37` | `cowrie.client.version` |
| `2026-08-20 02:01:37` | `cowrie.client.kex` |
| `2026-08-20 02:01:40` | `cowrie.login.success` |
| `2026-08-20 02:01:41` | `cowrie.session.params` |
| `2026-08-20 02:01:41` | `cowrie.command.input` |
| `2026-08-20 02:01:41` | `cowrie.command.input` |
| `2026-08-20 02:01:41` | `cowrie.command.input` |
| `2026-08-20 02:01:41` | `cowrie.command.input` |
| `2026-08-20 02:01:41` | `cowrie.command.input` |
| `2026-08-20 02:01:41` | `cowrie.command.success` |
| `2026-08-20 02:01:41` | `cowrie.command.input` |
| `2026-08-20 02:01:41` | `cowrie.command.input` |
| `2026-08-20 02:01:41` | `cowrie.command.input` |
| `2026-08-20 02:01:41` | `cowrie.command.input` |
| `2026-08-20 02:01:42` | `cowrie.log.closed` |
| `2026-08-20 02:01:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa06f4e4389a

| Field | Detail |
|---|---|
| **Source IP** | `218.58.73[.]238` |
| **First Seen** | 2026-08-20 02:02 |
| **Last Seen** | 2026-08-20 02:02 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 02:02:43` | `cowrie.session.connect` |
| `2026-08-20 02:02:44` | `cowrie.client.version` |
| `2026-08-20 02:02:44` | `cowrie.client.kex` |
| `2026-08-20 02:02:47` | `cowrie.login.success` |
| `2026-08-20 02:02:48` | `cowrie.direct-tcpip.request` |
| `2026-08-20 02:02:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.58.73[.]238` to AbuseIPDB if not already reported
- [ ] Block `218.58.73[.]238` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b451efc735d4

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-20 02:02 |
| **Last Seen** | 2026-08-20 02:02 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 02:02:46` | `cowrie.session.connect` |
| `2026-08-20 02:02:46` | `cowrie.client.version` |
| `2026-08-20 02:02:46` | `cowrie.client.kex` |
| `2026-08-20 02:02:48` | `cowrie.login.success` |
| `2026-08-20 02:02:49` | `cowrie.session.params` |
| `2026-08-20 02:02:49` | `cowrie.command.input` |
| `2026-08-20 02:02:49` | `cowrie.command.input` |
| `2026-08-20 02:02:49` | `cowrie.command.input` |
| `2026-08-20 02:02:49` | `cowrie.command.input` |
| `2026-08-20 02:02:49` | `cowrie.command.input` |
| `2026-08-20 02:02:49` | `cowrie.command.success` |
| `2026-08-20 02:02:49` | `cowrie.command.input` |
| `2026-08-20 02:02:49` | `cowrie.command.input` |
| `2026-08-20 02:02:49` | `cowrie.command.input` |
| `2026-08-20 02:02:49` | `cowrie.command.input` |
| `2026-08-20 02:02:50` | `cowrie.log.closed` |
| `2026-08-20 02:02:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd3cc0da58e6

| Field | Detail |
|---|---|
| **Source IP** | `20.46.45[.]121` |
| **First Seen** | 2026-08-20 02:02 |
| **Last Seen** | 2026-08-20 02:03 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 02:02:53` | `cowrie.session.connect` |
| `2026-08-20 02:02:54` | `cowrie.client.version` |
| `2026-08-20 02:02:54` | `cowrie.client.kex` |
| `2026-08-20 02:02:55` | `cowrie.login.success` |
| `2026-08-20 02:02:56` | `cowrie.direct-tcpip.request` |
| `2026-08-20 02:03:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.46.45[.]121` to AbuseIPDB if not already reported
- [ ] Block `20.46.45[.]121` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c72a407f582b

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-20 02:03 |
| **Last Seen** | 2026-08-20 02:03 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 02:03:53` | `cowrie.session.connect` |
| `2026-08-20 02:03:53` | `cowrie.client.version` |
| `2026-08-20 02:03:53` | `cowrie.client.kex` |
| `2026-08-20 02:03:55` | `cowrie.login.success` |
| `2026-08-20 02:03:56` | `cowrie.session.params` |
| `2026-08-20 02:03:56` | `cowrie.command.input` |
| `2026-08-20 02:03:56` | `cowrie.command.input` |
| `2026-08-20 02:03:56` | `cowrie.command.input` |
| `2026-08-20 02:03:56` | `cowrie.command.input` |
| `2026-08-20 02:03:56` | `cowrie.command.input` |
| `2026-08-20 02:03:56` | `cowrie.command.success` |
| `2026-08-20 02:03:56` | `cowrie.command.input` |
| `2026-08-20 02:03:56` | `cowrie.command.input` |
| `2026-08-20 02:03:56` | `cowrie.command.input` |
| `2026-08-20 02:03:56` | `cowrie.command.input` |
| `2026-08-20 02:03:57` | `cowrie.log.closed` |
| `2026-08-20 02:03:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f22e119aba10

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-20 02:04 |
| **Last Seen** | 2026-08-20 02:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 02:04:22` | `cowrie.session.connect` |
| `2026-08-20 02:04:22` | `cowrie.client.version` |
| `2026-08-20 02:04:22` | `cowrie.client.kex` |
| `2026-08-20 02:04:23` | `cowrie.login.success` |
| `2026-08-20 02:04:24` | `cowrie.session.params` |
| `2026-08-20 02:04:24` | `cowrie.command.input` |
| `2026-08-20 02:04:24` | `cowrie.log.closed` |
| `2026-08-20 02:04:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-410076b3fdf7

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-20 02:04 |
| **Last Seen** | 2026-08-20 02:05 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 02:04:59` | `cowrie.session.connect` |
| `2026-08-20 02:04:59` | `cowrie.client.version` |
| `2026-08-20 02:04:59` | `cowrie.client.kex` |
| `2026-08-20 02:05:01` | `cowrie.login.success` |
| `2026-08-20 02:05:02` | `cowrie.session.params` |
| `2026-08-20 02:05:02` | `cowrie.command.input` |
| `2026-08-20 02:05:02` | `cowrie.command.input` |
| `2026-08-20 02:05:02` | `cowrie.command.input` |
| `2026-08-20 02:05:02` | `cowrie.command.input` |
| `2026-08-20 02:05:02` | `cowrie.command.input` |
| `2026-08-20 02:05:02` | `cowrie.command.success` |
| `2026-08-20 02:05:02` | `cowrie.command.input` |
| `2026-08-20 02:05:02` | `cowrie.command.input` |
| `2026-08-20 02:05:02` | `cowrie.command.input` |
| `2026-08-20 02:05:02` | `cowrie.command.input` |
| `2026-08-20 02:05:03` | `cowrie.log.closed` |
| `2026-08-20 02:05:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53b95a74d7b9

| Field | Detail |
|---|---|
| **Source IP** | `117.32.132[.]170` |
| **First Seen** | 2026-08-20 02:05 |
| **Last Seen** | 2026-08-20 02:05 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 02:05:14` | `cowrie.session.connect` |
| `2026-08-20 02:05:15` | `cowrie.client.version` |
| `2026-08-20 02:05:15` | `cowrie.client.kex` |
| `2026-08-20 02:05:17` | `cowrie.login.success` |
| `2026-08-20 02:05:18` | `cowrie.direct-tcpip.request` |
| `2026-08-20 02:05:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.32.132[.]170` to AbuseIPDB if not already reported
- [ ] Block `117.32.132[.]170` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d88f8668b1b

| Field | Detail |
|---|---|
| **Source IP** | `71.229.1[.]186` |
| **First Seen** | 2026-08-20 02:05 |
| **Last Seen** | 2026-08-20 02:05 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 02:05:24` | `cowrie.session.connect` |
| `2026-08-20 02:05:25` | `cowrie.client.version` |
| `2026-08-20 02:05:25` | `cowrie.client.kex` |
| `2026-08-20 02:05:26` | `cowrie.login.success` |
| `2026-08-20 02:05:27` | `cowrie.direct-tcpip.request` |
| `2026-08-20 02:05:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `71.229.1[.]186` to AbuseIPDB if not already reported
- [ ] Block `71.229.1[.]186` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b61abd6d4baf

| Field | Detail |
|---|---|
| **Source IP** | `182.60.128[.]241` |
| **First Seen** | 2026-08-20 02:05 |
| **Last Seen** | 2026-08-20 02:05 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 02:05:28` | `cowrie.session.connect` |
| `2026-08-20 02:05:28` | `cowrie.client.version` |
| `2026-08-20 02:05:28` | `cowrie.client.kex` |
| `2026-08-20 02:05:30` | `cowrie.login.success` |
| `2026-08-20 02:05:31` | `cowrie.direct-tcpip.request` |
| `2026-08-20 02:05:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.60.128[.]241` to AbuseIPDB if not already reported
- [ ] Block `182.60.128[.]241` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c351e12c280c

| Field | Detail |
|---|---|
| **Source IP** | `188.168.86[.]6` |
| **First Seen** | 2026-08-20 02:05 |
| **Last Seen** | 2026-08-20 02:05 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 02:05:37` | `cowrie.session.connect` |
| `2026-08-20 02:05:38` | `cowrie.client.version` |
| `2026-08-20 02:05:38` | `cowrie.client.kex` |
| `2026-08-20 02:05:41` | `cowrie.login.success` |
| `2026-08-20 02:05:42` | `cowrie.direct-tcpip.request` |
| `2026-08-20 02:05:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `188.168.86[.]6` to AbuseIPDB if not already reported
- [ ] Block `188.168.86[.]6` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e47c637e58f

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-20 02:06 |
| **Last Seen** | 2026-08-20 02:06 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 02:06:05` | `cowrie.session.connect` |
| `2026-08-20 02:06:05` | `cowrie.client.version` |
| `2026-08-20 02:06:05` | `cowrie.client.kex` |
| `2026-08-20 02:06:07` | `cowrie.login.success` |
| `2026-08-20 02:06:08` | `cowrie.session.params` |
| `2026-08-20 02:06:08` | `cowrie.command.input` |
| `2026-08-20 02:06:08` | `cowrie.command.input` |
| `2026-08-20 02:06:08` | `cowrie.command.input` |
| `2026-08-20 02:06:08` | `cowrie.command.input` |
| `2026-08-20 02:06:08` | `cowrie.command.input` |
| `2026-08-20 02:06:08` | `cowrie.command.success` |
| `2026-08-20 02:06:08` | `cowrie.command.input` |
| `2026-08-20 02:06:08` | `cowrie.command.input` |
| `2026-08-20 02:06:08` | `cowrie.command.input` |
| `2026-08-20 02:06:08` | `cowrie.command.input` |
| `2026-08-20 02:06:08` | `cowrie.log.closed` |
| `2026-08-20 02:06:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e1ba698a219

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-20 02:07 |
| **Last Seen** | 2026-08-20 02:07 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 02:07:12` | `cowrie.session.connect` |
| `2026-08-20 02:07:12` | `cowrie.client.version` |
| `2026-08-20 02:07:12` | `cowrie.client.kex` |
| `2026-08-20 02:07:13` | `cowrie.login.success` |
| `2026-08-20 02:07:15` | `cowrie.session.params` |
| `2026-08-20 02:07:15` | `cowrie.command.input` |
| `2026-08-20 02:07:15` | `cowrie.command.input` |
| `2026-08-20 02:07:15` | `cowrie.command.input` |
| `2026-08-20 02:07:15` | `cowrie.command.input` |
| `2026-08-20 02:07:15` | `cowrie.command.input` |
| `2026-08-20 02:07:15` | `cowrie.command.success` |
| `2026-08-20 02:07:15` | `cowrie.command.input` |
| `2026-08-20 02:07:15` | `cowrie.command.input` |
| `2026-08-20 02:07:15` | `cowrie.command.input` |
| `2026-08-20 02:07:15` | `cowrie.command.input` |
| `2026-08-20 02:07:15` | `cowrie.log.closed` |
| `2026-08-20 02:07:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19adc932c1c9

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-20 02:08 |
| **Last Seen** | 2026-08-20 02:08 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 02:08:20` | `cowrie.session.connect` |
| `2026-08-20 02:08:20` | `cowrie.client.version` |
| `2026-08-20 02:08:20` | `cowrie.client.kex` |
| `2026-08-20 02:08:21` | `cowrie.login.success` |
| `2026-08-20 02:08:22` | `cowrie.session.params` |
| `2026-08-20 02:08:22` | `cowrie.command.input` |
| `2026-08-20 02:08:22` | `cowrie.command.input` |
| `2026-08-20 02:08:22` | `cowrie.command.input` |
| `2026-08-20 02:08:22` | `cowrie.command.input` |
| `2026-08-20 02:08:22` | `cowrie.command.input` |
| `2026-08-20 02:08:22` | `cowrie.command.success` |
| `2026-08-20 02:08:22` | `cowrie.command.input` |
| `2026-08-20 02:08:22` | `cowrie.command.input` |
| `2026-08-20 02:08:22` | `cowrie.command.input` |
| `2026-08-20 02:08:22` | `cowrie.command.input` |
| `2026-08-20 02:08:23` | `cowrie.log.closed` |
| `2026-08-20 02:08:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc3d14a030b8

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-20 02:09 |
| **Last Seen** | 2026-08-20 02:09 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 02:09:30` | `cowrie.session.connect` |
| `2026-08-20 02:09:30` | `cowrie.client.version` |
| `2026-08-20 02:09:30` | `cowrie.client.kex` |
| `2026-08-20 02:09:31` | `cowrie.login.success` |
| `2026-08-20 02:09:32` | `cowrie.session.params` |
| `2026-08-20 02:09:32` | `cowrie.command.input` |
| `2026-08-20 02:09:32` | `cowrie.command.input` |
| `2026-08-20 02:09:32` | `cowrie.command.input` |
| `2026-08-20 02:09:33` | `cowrie.command.input` |
| `2026-08-20 02:09:33` | `cowrie.command.input` |
| `2026-08-20 02:09:33` | `cowrie.command.success` |
| `2026-08-20 02:09:33` | `cowrie.command.input` |
| `2026-08-20 02:09:33` | `cowrie.command.input` |
| `2026-08-20 02:09:33` | `cowrie.command.input` |
| `2026-08-20 02:09:33` | `cowrie.command.input` |
| `2026-08-20 02:09:33` | `cowrie.log.closed` |
| `2026-08-20 02:09:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d9f56abf08d

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]221` |
| **First Seen** | 2026-08-20 02:10 |
| **Last Seen** | 2026-08-20 02:10 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 02:10:01` | `cowrie.session.connect` |
| `2026-08-20 02:10:02` | `cowrie.client.version` |
| `2026-08-20 02:10:02` | `cowrie.client.kex` |
| `2026-08-20 02:10:08` | `cowrie.login.success` |
| `2026-08-20 02:10:13` | `cowrie.session.params` |
| `2026-08-20 02:10:13` | `cowrie.command.input` |
| `2026-08-20 02:10:14` | `cowrie.log.closed` |
| `2026-08-20 02:10:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]221` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df2e57055d7d

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-20 02:10 |
| **Last Seen** | 2026-08-20 02:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 02:10:17` | `cowrie.session.connect` |
| `2026-08-20 02:10:17` | `cowrie.client.version` |
| `2026-08-20 02:10:18` | `cowrie.client.kex` |
| `2026-08-20 02:10:18` | `cowrie.login.success` |
| `2026-08-20 02:10:19` | `cowrie.session.params` |
| `2026-08-20 02:10:19` | `cowrie.command.input` |
| `2026-08-20 02:10:19` | `cowrie.log.closed` |
| `2026-08-20 02:10:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-836ad9621856

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-20 02:10 |
| **Last Seen** | 2026-08-20 02:10 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 02:10:41` | `cowrie.session.connect` |
| `2026-08-20 02:10:41` | `cowrie.client.version` |
| `2026-08-20 02:10:41` | `cowrie.client.kex` |
| `2026-08-20 02:10:42` | `cowrie.login.success` |
| `2026-08-20 02:10:43` | `cowrie.session.params` |
| `2026-08-20 02:10:43` | `cowrie.command.input` |
| `2026-08-20 02:10:43` | `cowrie.command.input` |
| `2026-08-20 02:10:43` | `cowrie.command.input` |
| `2026-08-20 02:10:43` | `cowrie.command.input` |
| `2026-08-20 02:10:43` | `cowrie.command.input` |
| `2026-08-20 02:10:43` | `cowrie.command.success` |
| `2026-08-20 02:10:43` | `cowrie.command.input` |
| `2026-08-20 02:10:43` | `cowrie.command.input` |
| `2026-08-20 02:10:43` | `cowrie.command.input` |
| `2026-08-20 02:10:43` | `cowrie.command.input` |
| `2026-08-20 02:10:43` | `cowrie.log.closed` |
| `2026-08-20 02:10:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18adf413b530

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-20 02:11 |
| **Last Seen** | 2026-08-20 02:11 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 02:11:51` | `cowrie.session.connect` |
| `2026-08-20 02:11:51` | `cowrie.client.version` |
| `2026-08-20 02:11:51` | `cowrie.client.kex` |
| `2026-08-20 02:11:52` | `cowrie.login.success` |
| `2026-08-20 02:11:54` | `cowrie.session.params` |
| `2026-08-20 02:11:54` | `cowrie.command.input` |
| `2026-08-20 02:11:54` | `cowrie.command.input` |
| `2026-08-20 02:11:54` | `cowrie.command.input` |
| `2026-08-20 02:11:54` | `cowrie.command.input` |
| `2026-08-20 02:11:54` | `cowrie.command.input` |
| `2026-08-20 02:11:54` | `cowrie.command.success` |
| `2026-08-20 02:11:54` | `cowrie.command.input` |
| `2026-08-20 02:11:54` | `cowrie.command.input` |
| `2026-08-20 02:11:54` | `cowrie.command.input` |
| `2026-08-20 02:11:54` | `cowrie.command.input` |
| `2026-08-20 02:11:54` | `cowrie.log.closed` |
| `2026-08-20 02:11:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a9169ab09fc

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-20 02:13 |
| **Last Seen** | 2026-08-20 02:13 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 02:13:04` | `cowrie.session.connect` |
| `2026-08-20 02:13:04` | `cowrie.client.version` |
| `2026-08-20 02:13:04` | `cowrie.client.kex` |
| `2026-08-20 02:13:05` | `cowrie.login.success` |
| `2026-08-20 02:13:06` | `cowrie.session.params` |
| `2026-08-20 02:13:06` | `cowrie.command.input` |
| `2026-08-20 02:13:06` | `cowrie.command.input` |
| `2026-08-20 02:13:06` | `cowrie.command.input` |
| `2026-08-20 02:13:06` | `cowrie.command.input` |
| `2026-08-20 02:13:06` | `cowrie.command.input` |
| `2026-08-20 02:13:06` | `cowrie.command.success` |
| `2026-08-20 02:13:06` | `cowrie.command.input` |
| `2026-08-20 02:13:06` | `cowrie.command.input` |
| `2026-08-20 02:13:06` | `cowrie.command.input` |
| `2026-08-20 02:13:06` | `cowrie.command.input` |
| `2026-08-20 02:13:06` | `cowrie.log.closed` |
| `2026-08-20 02:13:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-22fa363b311d

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-20 02:14 |
| **Last Seen** | 2026-08-20 02:14 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 02:14:15` | `cowrie.session.connect` |
| `2026-08-20 02:14:15` | `cowrie.client.version` |
| `2026-08-20 02:14:15` | `cowrie.client.kex` |
| `2026-08-20 02:14:17` | `cowrie.login.success` |
| `2026-08-20 02:14:18` | `cowrie.session.params` |
| `2026-08-20 02:14:18` | `cowrie.command.input` |
| `2026-08-20 02:14:18` | `cowrie.command.input` |
| `2026-08-20 02:14:18` | `cowrie.command.input` |
| `2026-08-20 02:14:18` | `cowrie.command.input` |
| `2026-08-20 02:14:18` | `cowrie.command.input` |
| `2026-08-20 02:14:18` | `cowrie.command.success` |
| `2026-08-20 02:14:18` | `cowrie.command.input` |
| `2026-08-20 02:14:18` | `cowrie.command.input` |
| `2026-08-20 02:14:18` | `cowrie.command.input` |
| `2026-08-20 02:14:18` | `cowrie.command.input` |
| `2026-08-20 02:14:18` | `cowrie.log.closed` |
| `2026-08-20 02:14:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0d00f396ad5

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-20 02:15 |
| **Last Seen** | 2026-08-20 02:15 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 02:15:26` | `cowrie.session.connect` |
| `2026-08-20 02:15:26` | `cowrie.client.version` |
| `2026-08-20 02:15:27` | `cowrie.client.kex` |
| `2026-08-20 02:15:28` | `cowrie.login.success` |
| `2026-08-20 02:15:29` | `cowrie.session.params` |
| `2026-08-20 02:15:29` | `cowrie.command.input` |
| `2026-08-20 02:15:29` | `cowrie.command.input` |
| `2026-08-20 02:15:29` | `cowrie.command.input` |
| `2026-08-20 02:15:29` | `cowrie.command.input` |
| `2026-08-20 02:15:29` | `cowrie.command.input` |
| `2026-08-20 02:15:29` | `cowrie.command.success` |
| `2026-08-20 02:15:29` | `cowrie.command.input` |
| `2026-08-20 02:15:29` | `cowrie.command.input` |
| `2026-08-20 02:15:29` | `cowrie.command.input` |
| `2026-08-20 02:15:29` | `cowrie.command.input` |
| `2026-08-20 02:15:29` | `cowrie.log.closed` |
| `2026-08-20 02:15:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4bfdad16842e

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-20 02:16 |
| **Last Seen** | 2026-08-20 02:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 02:16:13` | `cowrie.session.connect` |
| `2026-08-20 02:16:13` | `cowrie.client.version` |
| `2026-08-20 02:16:13` | `cowrie.client.kex` |
| `2026-08-20 02:16:13` | `cowrie.login.success` |
| `2026-08-20 02:16:14` | `cowrie.session.params` |
| `2026-08-20 02:16:14` | `cowrie.command.input` |
| `2026-08-20 02:16:14` | `cowrie.log.closed` |
| `2026-08-20 02:16:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64afc32f1f79

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-20 02:16 |
| **Last Seen** | 2026-08-20 02:16 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 02:16:37` | `cowrie.session.connect` |
| `2026-08-20 02:16:37` | `cowrie.client.version` |
| `2026-08-20 02:16:37` | `cowrie.client.kex` |
| `2026-08-20 02:16:38` | `cowrie.login.success` |
| `2026-08-20 02:16:39` | `cowrie.session.params` |
| `2026-08-20 02:16:39` | `cowrie.command.input` |
| `2026-08-20 02:16:39` | `cowrie.command.input` |
| `2026-08-20 02:16:39` | `cowrie.command.input` |
| `2026-08-20 02:16:39` | `cowrie.command.input` |
| `2026-08-20 02:16:39` | `cowrie.command.input` |
| `2026-08-20 02:16:39` | `cowrie.command.success` |
| `2026-08-20 02:16:39` | `cowrie.command.input` |
| `2026-08-20 02:16:39` | `cowrie.command.input` |
| `2026-08-20 02:16:39` | `cowrie.command.input` |
| `2026-08-20 02:16:39` | `cowrie.command.input` |
| `2026-08-20 02:16:39` | `cowrie.log.closed` |
| `2026-08-20 02:16:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea82208d05e1

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-20 02:17 |
| **Last Seen** | 2026-08-20 02:17 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 02:17:50` | `cowrie.session.connect` |
| `2026-08-20 02:17:50` | `cowrie.client.version` |
| `2026-08-20 02:17:50` | `cowrie.client.kex` |
| `2026-08-20 02:17:51` | `cowrie.login.success` |
| `2026-08-20 02:17:52` | `cowrie.session.params` |
| `2026-08-20 02:17:52` | `cowrie.command.input` |
| `2026-08-20 02:17:52` | `cowrie.command.input` |
| `2026-08-20 02:17:52` | `cowrie.command.input` |
| `2026-08-20 02:17:52` | `cowrie.command.input` |
| `2026-08-20 02:17:52` | `cowrie.command.input` |
| `2026-08-20 02:17:52` | `cowrie.command.success` |
| `2026-08-20 02:17:52` | `cowrie.command.input` |
| `2026-08-20 02:17:52` | `cowrie.command.input` |
| `2026-08-20 02:17:52` | `cowrie.command.input` |
| `2026-08-20 02:17:52` | `cowrie.command.input` |
| `2026-08-20 02:17:52` | `cowrie.log.closed` |
| `2026-08-20 02:17:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ec9e7ddd195

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-20 02:18 |
| **Last Seen** | 2026-08-20 02:18 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 02:18:56` | `cowrie.session.connect` |
| `2026-08-20 02:18:56` | `cowrie.client.version` |
| `2026-08-20 02:18:56` | `cowrie.client.kex` |
| `2026-08-20 02:18:57` | `cowrie.login.success` |
| `2026-08-20 02:18:58` | `cowrie.session.params` |
| `2026-08-20 02:18:58` | `cowrie.command.input` |
| `2026-08-20 02:18:58` | `cowrie.command.input` |
| `2026-08-20 02:18:58` | `cowrie.command.input` |
| `2026-08-20 02:18:58` | `cowrie.command.input` |
| `2026-08-20 02:18:58` | `cowrie.command.input` |
| `2026-08-20 02:18:58` | `cowrie.command.success` |
| `2026-08-20 02:18:58` | `cowrie.command.input` |
| `2026-08-20 02:18:58` | `cowrie.command.input` |
| `2026-08-20 02:18:58` | `cowrie.command.input` |
| `2026-08-20 02:18:58` | `cowrie.command.input` |
| `2026-08-20 02:18:59` | `cowrie.log.closed` |
| `2026-08-20 02:18:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-660157e03c62

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-20 02:20 |
| **Last Seen** | 2026-08-20 02:20 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 02:20:03` | `cowrie.session.connect` |
| `2026-08-20 02:20:03` | `cowrie.client.version` |
| `2026-08-20 02:20:04` | `cowrie.client.kex` |
| `2026-08-20 02:20:05` | `cowrie.login.success` |
| `2026-08-20 02:20:06` | `cowrie.session.params` |
| `2026-08-20 02:20:06` | `cowrie.command.input` |
| `2026-08-20 02:20:06` | `cowrie.command.input` |
| `2026-08-20 02:20:06` | `cowrie.command.input` |
| `2026-08-20 02:20:06` | `cowrie.command.input` |
| `2026-08-20 02:20:06` | `cowrie.command.input` |
| `2026-08-20 02:20:06` | `cowrie.command.success` |
| `2026-08-20 02:20:06` | `cowrie.command.input` |
| `2026-08-20 02:20:06` | `cowrie.command.input` |
| `2026-08-20 02:20:06` | `cowrie.command.input` |
| `2026-08-20 02:20:06` | `cowrie.command.input` |
| `2026-08-20 02:20:07` | `cowrie.log.closed` |
| `2026-08-20 02:20:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-629d406749dd

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-20 02:21 |
| **Last Seen** | 2026-08-20 02:21 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 02:21:11` | `cowrie.session.connect` |
| `2026-08-20 02:21:11` | `cowrie.client.version` |
| `2026-08-20 02:21:11` | `cowrie.client.kex` |
| `2026-08-20 02:21:13` | `cowrie.login.success` |
| `2026-08-20 02:21:14` | `cowrie.session.params` |
| `2026-08-20 02:21:14` | `cowrie.command.input` |
| `2026-08-20 02:21:14` | `cowrie.command.input` |
| `2026-08-20 02:21:14` | `cowrie.command.input` |
| `2026-08-20 02:21:14` | `cowrie.command.input` |
| `2026-08-20 02:21:14` | `cowrie.command.input` |
| `2026-08-20 02:21:14` | `cowrie.command.success` |
| `2026-08-20 02:21:14` | `cowrie.command.input` |
| `2026-08-20 02:21:14` | `cowrie.command.input` |
| `2026-08-20 02:21:14` | `cowrie.command.input` |
| `2026-08-20 02:21:14` | `cowrie.command.input` |
| `2026-08-20 02:21:14` | `cowrie.log.closed` |
| `2026-08-20 02:21:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4efdb263121

| Field | Detail |
|---|---|
| **Source IP** | `65.20.161[.]126` |
| **First Seen** | 2026-08-20 02:21 |
| **Last Seen** | 2026-08-20 02:22 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 02:21:58` | `cowrie.session.connect` |
| `2026-08-20 02:21:59` | `cowrie.client.version` |
| `2026-08-20 02:21:59` | `cowrie.client.kex` |
| `2026-08-20 02:22:01` | `cowrie.login.success` |
| `2026-08-20 02:22:02` | `cowrie.direct-tcpip.request` |
| `2026-08-20 02:22:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.161[.]126` to AbuseIPDB if not already reported
- [ ] Block `65.20.161[.]126` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-35b41e6de2da

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-20 02:22 |
| **Last Seen** | 2026-08-20 02:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 02:22:09` | `cowrie.session.connect` |
| `2026-08-20 02:22:09` | `cowrie.client.version` |
| `2026-08-20 02:22:09` | `cowrie.client.kex` |
| `2026-08-20 02:22:09` | `cowrie.login.success` |
| `2026-08-20 02:22:10` | `cowrie.session.params` |
| `2026-08-20 02:22:10` | `cowrie.command.input` |
| `2026-08-20 02:22:10` | `cowrie.log.closed` |
| `2026-08-20 02:22:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5bafaa09f47b

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-20 02:22 |
| **Last Seen** | 2026-08-20 02:22 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 02:22:18` | `cowrie.session.connect` |
| `2026-08-20 02:22:18` | `cowrie.client.version` |
| `2026-08-20 02:22:18` | `cowrie.client.kex` |
| `2026-08-20 02:22:19` | `cowrie.login.success` |
| `2026-08-20 02:22:20` | `cowrie.session.params` |
| `2026-08-20 02:22:20` | `cowrie.command.input` |
| `2026-08-20 02:22:20` | `cowrie.command.input` |
| `2026-08-20 02:22:20` | `cowrie.command.input` |
| `2026-08-20 02:22:20` | `cowrie.command.input` |
| `2026-08-20 02:22:20` | `cowrie.command.input` |
| `2026-08-20 02:22:20` | `cowrie.command.success` |
| `2026-08-20 02:22:20` | `cowrie.command.input` |
| `2026-08-20 02:22:20` | `cowrie.command.input` |
| `2026-08-20 02:22:20` | `cowrie.command.input` |
| `2026-08-20 02:22:20` | `cowrie.command.input` |
| `2026-08-20 02:22:21` | `cowrie.log.closed` |
| `2026-08-20 02:22:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be2860dc827e

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]221` |
| **First Seen** | 2026-08-20 02:22 |
| **Last Seen** | 2026-08-20 02:22 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 02:22:25` | `cowrie.session.connect` |
| `2026-08-20 02:22:27` | `cowrie.client.version` |
| `2026-08-20 02:22:27` | `cowrie.client.kex` |
| `2026-08-20 02:22:34` | `cowrie.login.success` |
| `2026-08-20 02:22:37` | `cowrie.session.params` |
| `2026-08-20 02:22:37` | `cowrie.command.input` |
| `2026-08-20 02:22:38` | `cowrie.log.closed` |
| `2026-08-20 02:22:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]221` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d54b1ccbacb

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-20 02:23 |
| **Last Seen** | 2026-08-20 02:23 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 02:23:24` | `cowrie.session.connect` |
| `2026-08-20 02:23:24` | `cowrie.client.version` |
| `2026-08-20 02:23:24` | `cowrie.client.kex` |
| `2026-08-20 02:23:26` | `cowrie.login.success` |
| `2026-08-20 02:23:27` | `cowrie.session.params` |
| `2026-08-20 02:23:27` | `cowrie.command.input` |
| `2026-08-20 02:23:27` | `cowrie.command.input` |
| `2026-08-20 02:23:27` | `cowrie.command.input` |
| `2026-08-20 02:23:27` | `cowrie.command.input` |
| `2026-08-20 02:23:27` | `cowrie.command.input` |
| `2026-08-20 02:23:27` | `cowrie.command.success` |
| `2026-08-20 02:23:27` | `cowrie.command.input` |
| `2026-08-20 02:23:27` | `cowrie.command.input` |
| `2026-08-20 02:23:27` | `cowrie.command.input` |
| `2026-08-20 02:23:27` | `cowrie.command.input` |
| `2026-08-20 02:23:27` | `cowrie.log.closed` |
| `2026-08-20 02:23:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3debcd71d260

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-20 02:24 |
| **Last Seen** | 2026-08-20 02:24 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 02:24:30` | `cowrie.session.connect` |
| `2026-08-20 02:24:30` | `cowrie.client.version` |
| `2026-08-20 02:24:31` | `cowrie.client.kex` |
| `2026-08-20 02:24:32` | `cowrie.login.success` |
| `2026-08-20 02:24:33` | `cowrie.session.params` |
| `2026-08-20 02:24:33` | `cowrie.command.input` |
| `2026-08-20 02:24:33` | `cowrie.command.input` |
| `2026-08-20 02:24:33` | `cowrie.command.input` |
| `2026-08-20 02:24:33` | `cowrie.command.input` |
| `2026-08-20 02:24:33` | `cowrie.command.input` |
| `2026-08-20 02:24:33` | `cowrie.command.success` |
| `2026-08-20 02:24:33` | `cowrie.command.input` |
| `2026-08-20 02:24:33` | `cowrie.command.input` |
| `2026-08-20 02:24:33` | `cowrie.command.input` |
| `2026-08-20 02:24:33` | `cowrie.command.input` |
| `2026-08-20 02:24:33` | `cowrie.log.closed` |
| `2026-08-20 02:24:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7096a81f565b

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-20 02:25 |
| **Last Seen** | 2026-08-20 02:25 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 02:25:38` | `cowrie.session.connect` |
| `2026-08-20 02:25:39` | `cowrie.client.version` |
| `2026-08-20 02:25:39` | `cowrie.client.kex` |
| `2026-08-20 02:25:40` | `cowrie.login.success` |
| `2026-08-20 02:25:41` | `cowrie.session.params` |
| `2026-08-20 02:25:41` | `cowrie.command.input` |
| `2026-08-20 02:25:41` | `cowrie.command.input` |
| `2026-08-20 02:25:41` | `cowrie.command.input` |
| `2026-08-20 02:25:41` | `cowrie.command.input` |
| `2026-08-20 02:25:41` | `cowrie.command.input` |
| `2026-08-20 02:25:41` | `cowrie.command.success` |
| `2026-08-20 02:25:41` | `cowrie.command.input` |
| `2026-08-20 02:25:41` | `cowrie.command.input` |
| `2026-08-20 02:25:41` | `cowrie.command.input` |
| `2026-08-20 02:25:41` | `cowrie.command.input` |
| `2026-08-20 02:25:41` | `cowrie.log.closed` |
| `2026-08-20 02:25:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d01efcd65ebe

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-20 02:26 |
| **Last Seen** | 2026-08-20 02:26 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 02:26:44` | `cowrie.session.connect` |
| `2026-08-20 02:26:44` | `cowrie.client.version` |
| `2026-08-20 02:26:44` | `cowrie.client.kex` |
| `2026-08-20 02:26:45` | `cowrie.login.success` |
| `2026-08-20 02:26:47` | `cowrie.session.params` |
| `2026-08-20 02:26:47` | `cowrie.command.input` |
| `2026-08-20 02:26:47` | `cowrie.command.input` |
| `2026-08-20 02:26:47` | `cowrie.command.input` |
| `2026-08-20 02:26:47` | `cowrie.command.input` |
| `2026-08-20 02:26:47` | `cowrie.command.input` |
| `2026-08-20 02:26:47` | `cowrie.command.success` |
| `2026-08-20 02:26:47` | `cowrie.command.input` |
| `2026-08-20 02:26:47` | `cowrie.command.input` |
| `2026-08-20 02:26:47` | `cowrie.command.input` |
| `2026-08-20 02:26:47` | `cowrie.command.input` |
| `2026-08-20 02:26:47` | `cowrie.log.closed` |
| `2026-08-20 02:26:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c34bfc2eac4

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-20 02:27 |
| **Last Seen** | 2026-08-20 02:27 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 02:27:49` | `cowrie.session.connect` |
| `2026-08-20 02:27:49` | `cowrie.client.version` |
| `2026-08-20 02:27:49` | `cowrie.client.kex` |
| `2026-08-20 02:27:50` | `cowrie.login.success` |
| `2026-08-20 02:27:51` | `cowrie.session.params` |
| `2026-08-20 02:27:51` | `cowrie.command.input` |
| `2026-08-20 02:27:51` | `cowrie.command.input` |
| `2026-08-20 02:27:51` | `cowrie.command.input` |
| `2026-08-20 02:27:51` | `cowrie.command.input` |
| `2026-08-20 02:27:51` | `cowrie.command.input` |
| `2026-08-20 02:27:51` | `cowrie.command.success` |
| `2026-08-20 02:27:51` | `cowrie.command.input` |
| `2026-08-20 02:27:51` | `cowrie.command.input` |
| `2026-08-20 02:27:51` | `cowrie.command.input` |
| `2026-08-20 02:27:51` | `cowrie.command.input` |
| `2026-08-20 02:27:52` | `cowrie.log.closed` |
| `2026-08-20 02:27:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4592b732953

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-20 02:28 |
| **Last Seen** | 2026-08-20 02:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 02:28:05` | `cowrie.session.connect` |
| `2026-08-20 02:28:05` | `cowrie.client.version` |
| `2026-08-20 02:28:05` | `cowrie.client.kex` |
| `2026-08-20 02:28:05` | `cowrie.login.success` |
| `2026-08-20 02:28:06` | `cowrie.session.params` |
| `2026-08-20 02:28:06` | `cowrie.command.input` |
| `2026-08-20 02:28:06` | `cowrie.log.closed` |
| `2026-08-20 02:28:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66c1060b7230

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-20 02:28 |
| **Last Seen** | 2026-08-20 02:28 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 02:28:54` | `cowrie.session.connect` |
| `2026-08-20 02:28:54` | `cowrie.client.version` |
| `2026-08-20 02:28:54` | `cowrie.client.kex` |
| `2026-08-20 02:28:55` | `cowrie.login.success` |
| `2026-08-20 02:28:56` | `cowrie.session.params` |
| `2026-08-20 02:28:56` | `cowrie.command.input` |
| `2026-08-20 02:28:56` | `cowrie.command.input` |
| `2026-08-20 02:28:56` | `cowrie.command.input` |
| `2026-08-20 02:28:56` | `cowrie.command.input` |
| `2026-08-20 02:28:56` | `cowrie.command.input` |
| `2026-08-20 02:28:56` | `cowrie.command.success` |
| `2026-08-20 02:28:56` | `cowrie.command.input` |
| `2026-08-20 02:28:56` | `cowrie.command.input` |
| `2026-08-20 02:28:56` | `cowrie.command.input` |
| `2026-08-20 02:28:56` | `cowrie.command.input` |
| `2026-08-20 02:28:57` | `cowrie.log.closed` |
| `2026-08-20 02:28:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9fcc292f073

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-20 02:29 |
| **Last Seen** | 2026-08-20 02:30 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 02:29:59` | `cowrie.session.connect` |
| `2026-08-20 02:29:59` | `cowrie.client.version` |
| `2026-08-20 02:29:59` | `cowrie.client.kex` |
| `2026-08-20 02:30:01` | `cowrie.login.success` |
| `2026-08-20 02:30:02` | `cowrie.session.params` |
| `2026-08-20 02:30:02` | `cowrie.command.input` |
| `2026-08-20 02:30:02` | `cowrie.command.input` |
| `2026-08-20 02:30:02` | `cowrie.command.input` |
| `2026-08-20 02:30:02` | `cowrie.command.input` |
| `2026-08-20 02:30:02` | `cowrie.command.input` |
| `2026-08-20 02:30:02` | `cowrie.command.success` |
| `2026-08-20 02:30:02` | `cowrie.command.input` |
| `2026-08-20 02:30:02` | `cowrie.command.input` |
| `2026-08-20 02:30:02` | `cowrie.command.input` |
| `2026-08-20 02:30:02` | `cowrie.command.input` |
| `2026-08-20 02:30:03` | `cowrie.log.closed` |
| `2026-08-20 02:30:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6af3629acd8

| Field | Detail |
|---|---|
| **Source IP** | `182.75.197[.]174` |
| **First Seen** | 2026-08-20 02:30 |
| **Last Seen** | 2026-08-20 02:30 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 02:30:48` | `cowrie.session.connect` |
| `2026-08-20 02:30:49` | `cowrie.client.version` |
| `2026-08-20 02:30:49` | `cowrie.client.kex` |
| `2026-08-20 02:30:51` | `cowrie.login.success` |
| `2026-08-20 02:30:52` | `cowrie.direct-tcpip.request` |
| `2026-08-20 02:30:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.75.197[.]174` to AbuseIPDB if not already reported
- [ ] Block `182.75.197[.]174` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e96072daaee0

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-20 02:31 |
| **Last Seen** | 2026-08-20 02:31 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 02:31:04` | `cowrie.session.connect` |
| `2026-08-20 02:31:04` | `cowrie.client.version` |
| `2026-08-20 02:31:04` | `cowrie.client.kex` |
| `2026-08-20 02:31:06` | `cowrie.login.success` |
| `2026-08-20 02:31:07` | `cowrie.session.params` |
| `2026-08-20 02:31:07` | `cowrie.command.input` |
| `2026-08-20 02:31:07` | `cowrie.command.input` |
| `2026-08-20 02:31:07` | `cowrie.command.input` |
| `2026-08-20 02:31:07` | `cowrie.command.input` |
| `2026-08-20 02:31:07` | `cowrie.command.input` |
| `2026-08-20 02:31:07` | `cowrie.command.success` |
| `2026-08-20 02:31:07` | `cowrie.command.input` |
| `2026-08-20 02:31:07` | `cowrie.command.input` |
| `2026-08-20 02:31:07` | `cowrie.command.input` |
| `2026-08-20 02:31:07` | `cowrie.command.input` |
| `2026-08-20 02:31:07` | `cowrie.log.closed` |
| `2026-08-20 02:31:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ea41dbb74f8

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-20 02:32 |
| **Last Seen** | 2026-08-20 02:32 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 02:32:08` | `cowrie.session.connect` |
| `2026-08-20 02:32:08` | `cowrie.client.version` |
| `2026-08-20 02:32:08` | `cowrie.client.kex` |
| `2026-08-20 02:32:10` | `cowrie.login.success` |
| `2026-08-20 02:32:11` | `cowrie.session.params` |
| `2026-08-20 02:32:11` | `cowrie.command.input` |
| `2026-08-20 02:32:11` | `cowrie.command.input` |
| `2026-08-20 02:32:11` | `cowrie.command.input` |
| `2026-08-20 02:32:11` | `cowrie.command.input` |
| `2026-08-20 02:32:11` | `cowrie.command.input` |
| `2026-08-20 02:32:11` | `cowrie.command.success` |
| `2026-08-20 02:32:11` | `cowrie.command.input` |
| `2026-08-20 02:32:11` | `cowrie.command.input` |
| `2026-08-20 02:32:11` | `cowrie.command.input` |
| `2026-08-20 02:32:11` | `cowrie.command.input` |
| `2026-08-20 02:32:11` | `cowrie.log.closed` |
| `2026-08-20 02:32:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-547d959c353a

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-20 02:33 |
| **Last Seen** | 2026-08-20 02:33 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 02:33:11` | `cowrie.session.connect` |
| `2026-08-20 02:33:11` | `cowrie.client.version` |
| `2026-08-20 02:33:13` | `cowrie.client.kex` |
| `2026-08-20 02:33:14` | `cowrie.login.success` |
| `2026-08-20 02:33:15` | `cowrie.session.params` |
| `2026-08-20 02:33:15` | `cowrie.command.input` |
| `2026-08-20 02:33:15` | `cowrie.command.input` |
| `2026-08-20 02:33:15` | `cowrie.command.input` |
| `2026-08-20 02:33:15` | `cowrie.command.input` |
| `2026-08-20 02:33:15` | `cowrie.command.input` |
| `2026-08-20 02:33:15` | `cowrie.command.success` |
| `2026-08-20 02:33:15` | `cowrie.command.input` |
| `2026-08-20 02:33:15` | `cowrie.command.input` |
| `2026-08-20 02:33:15` | `cowrie.command.input` |
| `2026-08-20 02:33:15` | `cowrie.command.input` |
| `2026-08-20 02:33:16` | `cowrie.log.closed` |
| `2026-08-20 02:33:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4df2361d6644

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-20 02:34 |
| **Last Seen** | 2026-08-20 02:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 02:34:00` | `cowrie.session.connect` |
| `2026-08-20 02:34:00` | `cowrie.client.version` |
| `2026-08-20 02:34:00` | `cowrie.client.kex` |
| `2026-08-20 02:34:01` | `cowrie.login.success` |
| `2026-08-20 02:34:02` | `cowrie.session.params` |
| `2026-08-20 02:34:02` | `cowrie.command.input` |
| `2026-08-20 02:34:02` | `cowrie.log.closed` |
| `2026-08-20 02:34:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b5cd0d7c9ea

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-20 02:34 |
| **Last Seen** | 2026-08-20 02:34 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 02:34:14` | `cowrie.session.connect` |
| `2026-08-20 02:34:14` | `cowrie.client.version` |
| `2026-08-20 02:34:14` | `cowrie.client.kex` |
| `2026-08-20 02:34:15` | `cowrie.login.success` |
| `2026-08-20 02:34:16` | `cowrie.session.params` |
| `2026-08-20 02:34:16` | `cowrie.command.input` |
| `2026-08-20 02:34:16` | `cowrie.command.input` |
| `2026-08-20 02:34:16` | `cowrie.command.input` |
| `2026-08-20 02:34:16` | `cowrie.command.input` |
| `2026-08-20 02:34:16` | `cowrie.command.input` |
| `2026-08-20 02:34:16` | `cowrie.command.success` |
| `2026-08-20 02:34:16` | `cowrie.command.input` |
| `2026-08-20 02:34:16` | `cowrie.command.input` |
| `2026-08-20 02:34:16` | `cowrie.command.input` |
| `2026-08-20 02:34:16` | `cowrie.command.input` |
| `2026-08-20 02:34:17` | `cowrie.log.closed` |
| `2026-08-20 02:34:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58206a8d6836

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]221` |
| **First Seen** | 2026-08-20 02:34 |
| **Last Seen** | 2026-08-20 02:35 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 02:34:51` | `cowrie.session.connect` |
| `2026-08-20 02:34:52` | `cowrie.client.version` |
| `2026-08-20 02:34:52` | `cowrie.client.kex` |
| `2026-08-20 02:34:58` | `cowrie.login.success` |
| `2026-08-20 02:35:02` | `cowrie.session.params` |
| `2026-08-20 02:35:02` | `cowrie.command.input` |
| `2026-08-20 02:35:03` | `cowrie.log.closed` |
| `2026-08-20 02:35:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]221` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f5a397ef1d6e

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-20 02:35 |
| **Last Seen** | 2026-08-20 02:35 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 02:35:19` | `cowrie.session.connect` |
| `2026-08-20 02:35:19` | `cowrie.client.version` |
| `2026-08-20 02:35:19` | `cowrie.client.kex` |
| `2026-08-20 02:35:20` | `cowrie.login.success` |
| `2026-08-20 02:35:22` | `cowrie.session.params` |
| `2026-08-20 02:35:22` | `cowrie.command.input` |
| `2026-08-20 02:35:22` | `cowrie.command.input` |
| `2026-08-20 02:35:22` | `cowrie.command.input` |
| `2026-08-20 02:35:22` | `cowrie.command.input` |
| `2026-08-20 02:35:22` | `cowrie.command.input` |
| `2026-08-20 02:35:22` | `cowrie.command.success` |
| `2026-08-20 02:35:22` | `cowrie.command.input` |
| `2026-08-20 02:35:22` | `cowrie.command.input` |
| `2026-08-20 02:35:22` | `cowrie.command.input` |
| `2026-08-20 02:35:22` | `cowrie.command.input` |
| `2026-08-20 02:35:22` | `cowrie.log.closed` |
| `2026-08-20 02:35:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-904a29a1dd3e

| Field | Detail |
|---|---|
| **Source IP** | `60.249.252[.]94` |
| **First Seen** | 2026-08-20 02:35 |
| **Last Seen** | 2026-08-20 02:35 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 02:35:44` | `cowrie.session.connect` |
| `2026-08-20 02:35:45` | `cowrie.client.version` |
| `2026-08-20 02:35:45` | `cowrie.client.kex` |
| `2026-08-20 02:35:48` | `cowrie.login.success` |
| `2026-08-20 02:35:48` | `cowrie.direct-tcpip.request` |
| `2026-08-20 02:35:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.249.252[.]94` to AbuseIPDB if not already reported
- [ ] Block `60.249.252[.]94` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49046cbd64d9

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-20 02:36 |
| **Last Seen** | 2026-08-20 02:36 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 02:36:20` | `cowrie.session.connect` |
| `2026-08-20 02:36:21` | `cowrie.client.version` |
| `2026-08-20 02:36:21` | `cowrie.client.kex` |
| `2026-08-20 02:36:22` | `cowrie.login.success` |
| `2026-08-20 02:36:23` | `cowrie.session.params` |
| `2026-08-20 02:36:23` | `cowrie.command.input` |
| `2026-08-20 02:36:23` | `cowrie.command.input` |
| `2026-08-20 02:36:23` | `cowrie.command.input` |
| `2026-08-20 02:36:23` | `cowrie.command.input` |
| `2026-08-20 02:36:23` | `cowrie.command.input` |
| `2026-08-20 02:36:23` | `cowrie.command.success` |
| `2026-08-20 02:36:23` | `cowrie.command.input` |
| `2026-08-20 02:36:23` | `cowrie.command.input` |
| `2026-08-20 02:36:23` | `cowrie.command.input` |
| `2026-08-20 02:36:23` | `cowrie.command.input` |
| `2026-08-20 02:36:24` | `cowrie.log.closed` |
| `2026-08-20 02:36:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3c880fda990

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-20 02:37 |
| **Last Seen** | 2026-08-20 02:37 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 02:37:23` | `cowrie.session.connect` |
| `2026-08-20 02:37:23` | `cowrie.client.version` |
| `2026-08-20 02:37:23` | `cowrie.client.kex` |
| `2026-08-20 02:37:25` | `cowrie.login.success` |
| `2026-08-20 02:37:26` | `cowrie.session.params` |
| `2026-08-20 02:37:26` | `cowrie.command.input` |
| `2026-08-20 02:37:26` | `cowrie.command.input` |
| `2026-08-20 02:37:26` | `cowrie.command.input` |
| `2026-08-20 02:37:26` | `cowrie.command.input` |
| `2026-08-20 02:37:26` | `cowrie.command.input` |
| `2026-08-20 02:37:26` | `cowrie.command.success` |
| `2026-08-20 02:37:26` | `cowrie.command.input` |
| `2026-08-20 02:37:26` | `cowrie.command.input` |
| `2026-08-20 02:37:26` | `cowrie.command.input` |
| `2026-08-20 02:37:26` | `cowrie.command.input` |
| `2026-08-20 02:37:27` | `cowrie.log.closed` |
| `2026-08-20 02:37:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a744b0cc3d8c

| Field | Detail |
|---|---|
| **Source IP** | `65.20.179[.]251` |
| **First Seen** | 2026-08-20 02:38 |
| **Last Seen** | 2026-08-20 02:38 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 02:38:19` | `cowrie.session.connect` |
| `2026-08-20 02:38:19` | `cowrie.client.version` |
| `2026-08-20 02:38:19` | `cowrie.client.kex` |
| `2026-08-20 02:38:21` | `cowrie.login.success` |
| `2026-08-20 02:38:21` | `cowrie.direct-tcpip.request` |
| `2026-08-20 02:38:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.179[.]251` to AbuseIPDB if not already reported
- [ ] Block `65.20.179[.]251` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f46ef33ffae5

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-20 02:38 |
| **Last Seen** | 2026-08-20 02:38 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 02:38:29` | `cowrie.session.connect` |
| `2026-08-20 02:38:29` | `cowrie.client.version` |
| `2026-08-20 02:38:30` | `cowrie.client.kex` |
| `2026-08-20 02:38:30` | `cowrie.login.success` |
| `2026-08-20 02:38:32` | `cowrie.session.params` |
| `2026-08-20 02:38:32` | `cowrie.command.input` |
| `2026-08-20 02:38:32` | `cowrie.command.input` |
| `2026-08-20 02:38:32` | `cowrie.command.input` |
| `2026-08-20 02:38:32` | `cowrie.command.input` |
| `2026-08-20 02:38:32` | `cowrie.command.input` |
| `2026-08-20 02:38:32` | `cowrie.command.success` |
| `2026-08-20 02:38:32` | `cowrie.command.input` |
| `2026-08-20 02:38:32` | `cowrie.command.input` |
| `2026-08-20 02:38:32` | `cowrie.command.input` |
| `2026-08-20 02:38:32` | `cowrie.command.input` |
| `2026-08-20 02:38:32` | `cowrie.log.closed` |
| `2026-08-20 02:38:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95e2d211f99e

| Field | Detail |
|---|---|
| **Source IP** | `177.135.206[.]10` |
| **First Seen** | 2026-08-20 02:38 |
| **Last Seen** | 2026-08-20 02:38 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 02:38:32` | `cowrie.session.connect` |
| `2026-08-20 02:38:32` | `cowrie.client.version` |
| `2026-08-20 02:38:32` | `cowrie.client.kex` |
| `2026-08-20 02:38:34` | `cowrie.login.success` |
| `2026-08-20 02:38:35` | `cowrie.direct-tcpip.request` |
| `2026-08-20 02:38:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.135.206[.]10` to AbuseIPDB if not already reported
- [ ] Block `177.135.206[.]10` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-668261528df4

| Field | Detail |
|---|---|
| **Source IP** | `58.22.255[.]28` |
| **First Seen** | 2026-08-20 02:38 |
| **Last Seen** | 2026-08-20 02:38 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 02:38:41` | `cowrie.session.connect` |
| `2026-08-20 02:38:42` | `cowrie.client.version` |
| `2026-08-20 02:38:42` | `cowrie.client.kex` |
| `2026-08-20 02:38:44` | `cowrie.login.success` |
| `2026-08-20 02:38:44` | `cowrie.direct-tcpip.request` |
| `2026-08-20 02:38:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.22.255[.]28` to AbuseIPDB if not already reported
- [ ] Block `58.22.255[.]28` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4adc48f28ee

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-20 02:39 |
| **Last Seen** | 2026-08-20 02:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 02:39:42` | `cowrie.session.connect` |
| `2026-08-20 02:39:42` | `cowrie.client.version` |
| `2026-08-20 02:39:42` | `cowrie.client.kex` |
| `2026-08-20 02:39:43` | `cowrie.login.success` |
| `2026-08-20 02:39:44` | `cowrie.session.params` |
| `2026-08-20 02:39:44` | `cowrie.command.input` |
| `2026-08-20 02:39:44` | `cowrie.command.input` |
| `2026-08-20 02:39:44` | `cowrie.command.input` |
| `2026-08-20 02:39:44` | `cowrie.command.input` |
| `2026-08-20 02:39:44` | `cowrie.command.input` |
| `2026-08-20 02:39:44` | `cowrie.command.success` |
| `2026-08-20 02:39:44` | `cowrie.command.input` |
| `2026-08-20 02:39:44` | `cowrie.command.input` |
| `2026-08-20 02:39:44` | `cowrie.command.input` |
| `2026-08-20 02:39:44` | `cowrie.command.input` |
| `2026-08-20 02:39:44` | `cowrie.log.closed` |
| `2026-08-20 02:39:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc6a86dfefc6

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-20 02:39 |
| **Last Seen** | 2026-08-20 02:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 02:39:56` | `cowrie.session.connect` |
| `2026-08-20 02:39:56` | `cowrie.client.version` |
| `2026-08-20 02:39:56` | `cowrie.client.kex` |
| `2026-08-20 02:39:56` | `cowrie.login.success` |
| `2026-08-20 02:39:57` | `cowrie.session.params` |
| `2026-08-20 02:39:57` | `cowrie.command.input` |
| `2026-08-20 02:39:57` | `cowrie.log.closed` |
| `2026-08-20 02:39:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2645f0c92fd2

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-20 02:41 |
| **Last Seen** | 2026-08-20 02:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 02:41:04` | `cowrie.session.connect` |
| `2026-08-20 02:41:04` | `cowrie.client.version` |
| `2026-08-20 02:41:04` | `cowrie.client.kex` |
| `2026-08-20 02:41:04` | `cowrie.login.success` |
| `2026-08-20 02:41:05` | `cowrie.session.params` |
| `2026-08-20 02:41:05` | `cowrie.command.input` |
| `2026-08-20 02:41:05` | `cowrie.command.input` |
| `2026-08-20 02:41:05` | `cowrie.command.input` |
| `2026-08-20 02:41:05` | `cowrie.command.input` |
| `2026-08-20 02:41:05` | `cowrie.command.input` |
| `2026-08-20 02:41:05` | `cowrie.command.success` |
| `2026-08-20 02:41:05` | `cowrie.command.input` |
| `2026-08-20 02:41:05` | `cowrie.command.input` |
| `2026-08-20 02:41:05` | `cowrie.command.input` |
| `2026-08-20 02:41:05` | `cowrie.command.input` |
| `2026-08-20 02:41:05` | `cowrie.log.closed` |
| `2026-08-20 02:41:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-abd50bfba5e3

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-20 02:42 |
| **Last Seen** | 2026-08-20 02:42 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 02:42:27` | `cowrie.session.connect` |
| `2026-08-20 02:42:27` | `cowrie.client.version` |
| `2026-08-20 02:42:27` | `cowrie.client.kex` |
| `2026-08-20 02:42:28` | `cowrie.login.success` |
| `2026-08-20 02:42:29` | `cowrie.session.params` |
| `2026-08-20 02:42:29` | `cowrie.command.input` |
| `2026-08-20 02:42:29` | `cowrie.command.input` |
| `2026-08-20 02:42:29` | `cowrie.command.input` |
| `2026-08-20 02:42:29` | `cowrie.command.input` |
| `2026-08-20 02:42:29` | `cowrie.command.input` |
| `2026-08-20 02:42:29` | `cowrie.command.success` |
| `2026-08-20 02:42:29` | `cowrie.command.input` |
| `2026-08-20 02:42:29` | `cowrie.command.input` |
| `2026-08-20 02:42:29` | `cowrie.command.input` |
| `2026-08-20 02:42:29` | `cowrie.command.input` |
| `2026-08-20 02:42:29` | `cowrie.log.closed` |
| `2026-08-20 02:42:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29e2fe4cce97

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-20 02:43 |
| **Last Seen** | 2026-08-20 02:43 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 02:43:33` | `cowrie.session.connect` |
| `2026-08-20 02:43:33` | `cowrie.client.version` |
| `2026-08-20 02:43:33` | `cowrie.client.kex` |
| `2026-08-20 02:43:35` | `cowrie.login.success` |
| `2026-08-20 02:43:36` | `cowrie.session.params` |
| `2026-08-20 02:43:36` | `cowrie.command.input` |
| `2026-08-20 02:43:36` | `cowrie.command.input` |
| `2026-08-20 02:43:36` | `cowrie.command.input` |
| `2026-08-20 02:43:36` | `cowrie.command.input` |
| `2026-08-20 02:43:36` | `cowrie.command.input` |
| `2026-08-20 02:43:36` | `cowrie.command.success` |
| `2026-08-20 02:43:36` | `cowrie.command.input` |
| `2026-08-20 02:43:36` | `cowrie.command.input` |
| `2026-08-20 02:43:36` | `cowrie.command.input` |
| `2026-08-20 02:43:36` | `cowrie.command.input` |
| `2026-08-20 02:43:37` | `cowrie.log.closed` |
| `2026-08-20 02:43:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83eee0817378

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-20 02:44 |
| **Last Seen** | 2026-08-20 02:44 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 02:44:39` | `cowrie.session.connect` |
| `2026-08-20 02:44:39` | `cowrie.client.version` |
| `2026-08-20 02:44:39` | `cowrie.client.kex` |
| `2026-08-20 02:44:40` | `cowrie.login.success` |
| `2026-08-20 02:44:41` | `cowrie.session.params` |
| `2026-08-20 02:44:41` | `cowrie.command.input` |
| `2026-08-20 02:44:41` | `cowrie.command.input` |
| `2026-08-20 02:44:41` | `cowrie.command.input` |
| `2026-08-20 02:44:41` | `cowrie.command.input` |
| `2026-08-20 02:44:41` | `cowrie.command.input` |
| `2026-08-20 02:44:41` | `cowrie.command.success` |
| `2026-08-20 02:44:41` | `cowrie.command.input` |
| `2026-08-20 02:44:41` | `cowrie.command.input` |
| `2026-08-20 02:44:41` | `cowrie.command.input` |
| `2026-08-20 02:44:41` | `cowrie.command.input` |
| `2026-08-20 02:44:42` | `cowrie.log.closed` |
| `2026-08-20 02:44:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d541206afe6

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-20 02:45 |
| **Last Seen** | 2026-08-20 02:45 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 02:45:47` | `cowrie.session.connect` |
| `2026-08-20 02:45:47` | `cowrie.client.version` |
| `2026-08-20 02:45:47` | `cowrie.client.kex` |
| `2026-08-20 02:45:48` | `cowrie.login.success` |
| `2026-08-20 02:45:49` | `cowrie.session.params` |
| `2026-08-20 02:45:49` | `cowrie.command.input` |
| `2026-08-20 02:45:49` | `cowrie.command.input` |
| `2026-08-20 02:45:49` | `cowrie.command.input` |
| `2026-08-20 02:45:49` | `cowrie.command.input` |
| `2026-08-20 02:45:49` | `cowrie.command.input` |
| `2026-08-20 02:45:49` | `cowrie.command.success` |
| `2026-08-20 02:45:49` | `cowrie.command.input` |
| `2026-08-20 02:45:49` | `cowrie.command.input` |
| `2026-08-20 02:45:49` | `cowrie.command.input` |
| `2026-08-20 02:45:49` | `cowrie.command.input` |
| `2026-08-20 02:45:49` | `cowrie.log.closed` |
| `2026-08-20 02:45:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ff7c3e6cb9d

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-20 02:45 |
| **Last Seen** | 2026-08-20 02:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 02:45:51` | `cowrie.session.connect` |
| `2026-08-20 02:45:51` | `cowrie.client.version` |
| `2026-08-20 02:45:51` | `cowrie.client.kex` |
| `2026-08-20 02:45:52` | `cowrie.login.success` |
| `2026-08-20 02:45:53` | `cowrie.session.params` |
| `2026-08-20 02:45:53` | `cowrie.command.input` |
| `2026-08-20 02:45:53` | `cowrie.log.closed` |
| `2026-08-20 02:45:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-354f0410271c

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-20 02:47 |
| **Last Seen** | 2026-08-20 02:47 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 02:47:00` | `cowrie.session.connect` |
| `2026-08-20 02:47:00` | `cowrie.client.version` |
| `2026-08-20 02:47:00` | `cowrie.client.kex` |
| `2026-08-20 02:47:01` | `cowrie.login.success` |
| `2026-08-20 02:47:02` | `cowrie.session.params` |
| `2026-08-20 02:47:02` | `cowrie.command.input` |
| `2026-08-20 02:47:02` | `cowrie.command.input` |
| `2026-08-20 02:47:02` | `cowrie.command.input` |
| `2026-08-20 02:47:02` | `cowrie.command.input` |
| `2026-08-20 02:47:02` | `cowrie.command.input` |
| `2026-08-20 02:47:02` | `cowrie.command.success` |
| `2026-08-20 02:47:02` | `cowrie.command.input` |
| `2026-08-20 02:47:02` | `cowrie.command.input` |
| `2026-08-20 02:47:02` | `cowrie.command.input` |
| `2026-08-20 02:47:02` | `cowrie.command.input` |
| `2026-08-20 02:47:02` | `cowrie.log.closed` |
| `2026-08-20 02:47:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8fd4ab06401

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]221` |
| **First Seen** | 2026-08-20 02:47 |
| **Last Seen** | 2026-08-20 02:47 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 02:47:19` | `cowrie.session.connect` |
| `2026-08-20 02:47:20` | `cowrie.client.version` |
| `2026-08-20 02:47:20` | `cowrie.client.kex` |
| `2026-08-20 02:47:26` | `cowrie.login.success` |
| `2026-08-20 02:47:30` | `cowrie.session.params` |
| `2026-08-20 02:47:30` | `cowrie.command.input` |
| `2026-08-20 02:47:32` | `cowrie.log.closed` |
| `2026-08-20 02:47:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]221` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a528a8bd20ac

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-20 02:48 |
| **Last Seen** | 2026-08-20 02:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 02:48:19` | `cowrie.session.connect` |
| `2026-08-20 02:48:19` | `cowrie.client.version` |
| `2026-08-20 02:48:19` | `cowrie.client.kex` |
| `2026-08-20 02:48:19` | `cowrie.login.success` |
| `2026-08-20 02:48:20` | `cowrie.session.params` |
| `2026-08-20 02:48:20` | `cowrie.command.input` |
| `2026-08-20 02:48:20` | `cowrie.command.input` |
| `2026-08-20 02:48:20` | `cowrie.command.input` |
| `2026-08-20 02:48:20` | `cowrie.command.input` |
| `2026-08-20 02:48:20` | `cowrie.command.input` |
| `2026-08-20 02:48:20` | `cowrie.command.success` |
| `2026-08-20 02:48:20` | `cowrie.command.input` |
| `2026-08-20 02:48:20` | `cowrie.command.input` |
| `2026-08-20 02:48:20` | `cowrie.command.input` |
| `2026-08-20 02:48:20` | `cowrie.command.input` |
| `2026-08-20 02:48:21` | `cowrie.log.closed` |
| `2026-08-20 02:48:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-440fdf306d47

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-20 02:49 |
| **Last Seen** | 2026-08-20 02:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 02:49:37` | `cowrie.session.connect` |
| `2026-08-20 02:49:37` | `cowrie.client.version` |
| `2026-08-20 02:49:37` | `cowrie.client.kex` |
| `2026-08-20 02:49:38` | `cowrie.login.success` |
| `2026-08-20 02:49:38` | `cowrie.session.params` |
| `2026-08-20 02:49:38` | `cowrie.command.input` |
| `2026-08-20 02:49:38` | `cowrie.command.input` |
| `2026-08-20 02:49:38` | `cowrie.command.input` |
| `2026-08-20 02:49:38` | `cowrie.command.input` |
| `2026-08-20 02:49:38` | `cowrie.command.input` |
| `2026-08-20 02:49:38` | `cowrie.command.success` |
| `2026-08-20 02:49:38` | `cowrie.command.input` |
| `2026-08-20 02:49:38` | `cowrie.command.input` |
| `2026-08-20 02:49:38` | `cowrie.command.input` |
| `2026-08-20 02:49:38` | `cowrie.command.input` |
| `2026-08-20 02:49:39` | `cowrie.log.closed` |
| `2026-08-20 02:49:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9bc81c8f2c0d

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-20 02:51 |
| **Last Seen** | 2026-08-20 02:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 02:51:47` | `cowrie.session.connect` |
| `2026-08-20 02:51:47` | `cowrie.client.version` |
| `2026-08-20 02:51:47` | `cowrie.client.kex` |
| `2026-08-20 02:51:47` | `cowrie.login.success` |
| `2026-08-20 02:51:48` | `cowrie.session.params` |
| `2026-08-20 02:51:48` | `cowrie.command.input` |
| `2026-08-20 02:51:48` | `cowrie.log.closed` |
| `2026-08-20 02:51:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `80.251.153[.]178` | **155** | 2026-08-20 00:55 | 2026-08-20 02:54 | 183m | 0 | `T1592` | 🟠 MEDIUM |
| `139.199.80[.]137` | **5** | 2026-08-20 01:11 | 2026-08-20 02:49 | 0m | 0 | `T1592` | 🟢 LOW |
| `31.43.59[.]54` | **3** | 2026-08-20 01:40 | 2026-08-20 01:48 | 0m | 0 | `T1592` | 🟢 LOW |
| `71.6.146[.]186` | **3** | 2026-08-20 01:55 | 2026-08-20 01:55 | 0m | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]14` | **3** | 2026-08-20 01:53 | 2026-08-20 02:00 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `116.11.120[.]204` | **2** | 2026-08-20 01:01 | 2026-08-20 01:03 | 2m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]183` | **2** | 2026-08-20 02:31 | 2026-08-20 02:32 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]31` | **2** | 2026-08-20 02:46 | 2026-08-20 02:46 | 0m | 0 | `T1592` | 🟢 LOW |
| `111.179.187[.]35` | 1 | 2026-08-20 02:40 | 2026-08-20 02:41 | 10s | 0 | `T1592` | 🟢 LOW |
| `118.123.116[.]93` | 1 | 2026-08-20 02:42 | 2026-08-20 02:42 | 14s | 0 | `T1592` | 🟢 LOW |
| `176.10.203[.]54` | 1 | 2026-08-20 01:15 | 2026-08-20 01:17 | 120s | 0 | `T1592` | 🟢 LOW |
| `202.79.188[.]54` | 1 | 2026-08-20 00:59 | 2026-08-20 00:59 | 12s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]141` | 1 | 2026-08-20 01:02 | 2026-08-20 01:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.56.79[.]53` | 1 | 2026-08-20 01:44 | 2026-08-20 01:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.115[.]59` | 1 | 2026-08-20 01:44 | 2026-08-20 01:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `52.91.27[.]64` | 1 | 2026-08-20 01:22 | 2026-08-20 01:22 | 1s | 0 | `T1592` | 🟢 LOW |
| `60.173.105[.]206` | 1 | 2026-08-20 02:55 | 2026-08-20 02:55 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]137` | 1 | 2026-08-20 01:56 | 2026-08-20 01:56 | 2s | 0 | `T1592` | 🟢 LOW |
| `65.20.141[.]202` | 1 | 2026-08-20 02:30 | 2026-08-20 02:30 | 1s | 0 | `T1592` | 🟢 LOW |
| `65.20.202[.]4` | 1 | 2026-08-20 01:32 | 2026-08-20 01:33 | 8s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]139` | 1 | 2026-08-20 01:21 | 2026-08-20 01:22 | 16s | 0 | `T1592` | 🟢 LOW |
| `66.228.62[.]150` | 1 | 2026-08-20 02:42 | 2026-08-20 02:42 | 0s | 0 | `T1592` | 🟢 LOW |
| `69.5.169[.]43` | 1 | 2026-08-20 02:32 | 2026-08-20 02:32 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]14` | 1 | 2026-08-20 01:34 | 2026-08-20 01:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `89.21.67[.]147` | 1 | 2026-08-20 02:33 | 2026-08-20 02:33 | 10s | 0 | `T1592` | 🟢 LOW |
| `91.233.83[.]203` | 1 | 2026-08-20 02:00 | 2026-08-20 02:00 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.92.40[.]233` | 1 | 2026-08-20 01:33 | 2026-08-20 01:33 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
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
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **24/75** 🔴 |
| `1e70b63472772e3f5092ffe9c3573470e73590e6ab6d93fdcede1d368a5fd72d` | Bash Script | `1e70b63472772e3f...` | 61/100 | 🟡 MEDIUM | **28/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 54/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `1eecf2377d20768c28d741e21affaa53cf26db0d083efdbf43a92fa938b7e4be` | ELF Binary (Linux executable) (ARM 32-bit) | `1eecf2377d20768c...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
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
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `287962211de7bcadb39f7576732438b43ee6aab420ec23c29a9d12a8151a547f` | ELF Binary (Linux executable) (x86 32-bit) | `287962211de7bcad...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |

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
| `65.20.179[.]251` | IQ | Earthlink Telecommunications Equipment Trading & Services DMCC | **100** ⚠️ | 50 |
| `66.228.62[.]150` | US | Linode | **100** ⚠️ | 50 |
| `118.123.116[.]93` | CN | CHINANET Sichuan province network | **100** ⚠️ | 50 |
| `71.229.1[.]186` | US | Comcast Cable Communications, Inc. | **100** ⚠️ | 50 |
| `197.242.170[.]10` | MZ | IS - Internet Solutions Mozambique, Limitada | **100** ⚠️ | 50 |
| `117.32.132[.]170` | CN | CHINANET Shanxi(SN) province network | **100** ⚠️ | 50 |
| `85.217.149[.]14` | CA | NL MODAT | **100** ⚠️ | 50 |
| `20.46.45[.]121` | AE | Microsoft Corporation | **100** ⚠️ | 50 |
| `103.29.185[.]162` | ID | PT Pascal Indonesia | **100** ⚠️ | 50 |
| `31.43.59[.]54` | UA | Ukrainian Telecommunication Group LLC | **100** ⚠️ | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 119 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 103 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 46 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 45 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 45 |

---

## 🔕 False Positive Summary (23 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| AbuseIPDB score 12 below threshold 25 | 1 |
| AbuseIPDB score 15 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 18 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 320 cases |
| Tool 34  | Credential Extractor        | ✅ 128 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 11 fingerprints |
| Tool 36  | Command Clustering          | ✅ 4 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 66 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 23 filtered (7.2%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 50 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 20 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 103 priority case(s) shown individually · 27 recon entry/entries in table (8 group(s) consolidating 175 session(s)).

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
_Report time: 2026-08-20T02:59:58Z_

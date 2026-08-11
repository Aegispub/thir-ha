# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-11 |
| **Generated At** | 2026-08-11T03:51:34Z |
| **Shift Time** | 03:51 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **187** |
| Confirmed Threats | **138** |
| False Positives Filtered | **49** (26.2%) |
| Unique Attacker IPs | **65** |
| Countries of Origin | **24** |
| High Severity Cases | **33** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **154** |
| Malware Samples Analyzed | **2** HIGH · **24** MED · 20 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **49** |
| Unique Credential Pairs | **27** |
| Unique Usernames | **12** |
| Unique Passwords | **27** |
| Successful Auth Pairs | **40** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 13 |
| `test` | 9 |
| `support` | 5 |
| `admin` | 5 |
| `dns` | 4 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `p@ssw0rd` | 5 |
| `support` | 4 |
| `p@ssword` | 4 |
| `dns` | 4 |
| `abcd1234` | 3 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `test` | `p@ssw0rd` | 5 |
| `support` | `support` | 4 |
| `test` | `p@ssword` | 4 |
| `dns` | `dns` | 4 |
| `pi` | `abcd1234` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `pi` | `abcd1234` | `10.0.0.73` | 2026-08-11T00:55:17 |
| `blank` | `123qwe` | `49.124.133.102` | 2026-08-11T00:58:24 |
| `root` | `Password1` | `92.118.39.71` | 2026-08-11T01:00:44 |
| `root` | `Root123` | `92.118.39.71` | 2026-08-11T01:03:15 |
| `root` | `admin` | `92.118.39.71` | 2026-08-11T01:06:14 |
| `nobody` | `1q2w3e` | `121.178.185.141` | 2026-08-11T01:09:03 |
| `test` | `p@ssw0rd` | `10.0.0.73` | 2026-08-11T01:09:24 |
| `root` | `admin123` | `92.118.39.71` | 2026-08-11T01:10:57 |
| `test` | `p@ssw0rd` | `211.184.53.155` | 2026-08-11T01:11:09 |
| `test` | `p@ssw0rd` | `153.37.177.219` | 2026-08-11T01:11:18 |
| `blank` | `password` | `10.0.0.73` | 2026-08-11T01:13:41 |
| `root` | `alpine` | `92.118.39.71` | 2026-08-11T01:22:44 |
| `support` | `support` | `176.53.159.196` | 2026-08-11T01:25:48 |
| `test` | `p@ssw0rd` | `122.170.99.195` | 2026-08-11T01:27:29 |
| `root` | `changeme` | `92.118.39.71` | 2026-08-11T01:29:38 |
| `root` | `ubuntu` | `154.241.31.235` | 2026-08-11T01:33:52 |
| `nobody` | `1q2w3e` | `117.247.239.202` | 2026-08-11T01:37:51 |
| `root` | `default` | `92.118.39.71` | 2026-08-11T01:38:27 |
| `test` | `p@ssword` | `78.187.9.111` | 2026-08-11T01:42:58 |
| `dns` | `dns` | `10.0.0.73` | 2026-08-11T01:43:45 |
| `dns` | `dns` | `60.166.8.174` | 2026-08-11T01:45:24 |
| `dns` | `dns` | `59.46.182.10` | 2026-08-11T01:45:39 |
| `root` | `letmein` | `92.118.39.71` | 2026-08-11T01:45:42 |
| `admin` | `MODEMadmin` | `10.0.0.73` | 2026-08-11T01:48:05 |
| `test` | `p@ssword` | `10.0.0.73` | 2026-08-11T01:54:38 |
| `root` | `123@@@` | `64.110.90.250` | 2026-08-11T01:55:53 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-08-11T01:55:53 |
| `test` | `p@ssword` | `197.251.193.6` | 2026-08-11T02:11:46 |
| `test` | `p@ssword` | `34.41.211.48` | 2026-08-11T02:11:52 |
| `admin` | `passw0rd` | `10.0.0.73` | 2026-08-11T02:18:06 |
| `root` | `---fuck_you----` | `182.92.204.91` | 2026-08-11T02:18:30 |
| `support` | `support` | `10.0.0.73` | 2026-08-11T02:32:10 |
| `admin` | `passw0rd` | `213.55.79.195` | 2026-08-11T02:35:57 |
| `root` | `ubuntu` | `185.221.21.17` | 2026-08-11T02:37:27 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `130.211.76.1` | 2026-08-11T02:49:29 |
| `*1` | `$4` | `130.211.76.1` | 2026-08-11T02:49:38 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 4883` | `130.211.76.1` | 2026-08-11T02:49:40 |
| `support` | `911911` | `14.54.22.11` | 2026-08-11T02:51:11 |
| `config` | `123654` | `10.0.0.73` | 2026-08-11T02:52:11 |
| `config` | `123654` | `124.160.45.26` | 2026-08-11T02:53:52 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **187** |
| Sessions with Fingerprint | **11** |
| Unique HASSH Fingerprints | **11** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 17 |
| OpenSSH | 14 |
| libssh | 7 |
| Paramiko (Python) | 4 |
| PuTTY | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 14 | 14 |
| `2ec37a7cc8da...` | Mirai/variant | 8 | 1 |
| `eff4c24daffc...` | Modern SSH client | 3 | 1 |
| `873a5fb5fedc...` | Mirai/variant | 2 | 2 |
| `98ddc5604ef6...` | Modern SSH client | 2 | 2 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 14 | 14 | Mirai/variant |
| `2ec37a7cc8da...` | Go SSH scanner | 8 | 1 | Mirai/variant |
| `95420f9d932d...` | libssh | 7 | 2 | — |
| `eff4c24daffc...` | Go SSH scanner | 3 | 1 | Modern SSH client |
| `873a5fb5fedc...` | Go SSH scanner | 2 | 2 | Mirai/variant |
| `98ddc5604ef6...` | Go SSH scanner | 2 | 2 | Modern SSH client |
| `a2de0f306611...` | Paramiko (Python) | 2 | 1 | Mirai/variant |
| `a704be057881...` | Paramiko (Python) | 2 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **4** |
| Campaign Clusters | **1** |
| Highest Severity | **MEDIUM** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 8 | 1 | `T1082, T1592, T1078, T1083` |

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
Source IPs: `92.118.39.71`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **65** |
| Unique ASNs | **44** |
| High-Risk ASNs | **35** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS398324` | Censys, Inc. | 5 | HIGH |
| `AS63949` | Akamai Connected Cloud | 4 | HIGH |
| `AS46562` | Performive LLC | 4 | MEDIUM |
| `AS22773` | Cox Communications Inc. | 3 | MEDIUM |
| `AS48721` | Flyservers S.A. | 3 | HIGH |
| `AS396982` | Google LLC | 3 | HIGH |
| `AS4766` | Korea Telecom | 3 | HIGH |
| `AS4134` | CHINANET BACKBONE | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (33)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-ee1b6a304e9e

| Field | Detail |
|---|---|
| **Source IP** | `49.124.133[.]102` |
| **First Seen** | 2026-08-11 00:58 |
| **Last Seen** | 2026-08-11 00:58 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 00:58:21` | `cowrie.session.connect` |
| `2026-08-11 00:58:22` | `cowrie.client.version` |
| `2026-08-11 00:58:22` | `cowrie.client.kex` |
| `2026-08-11 00:58:24` | `cowrie.login.success` |
| `2026-08-11 00:58:25` | `cowrie.direct-tcpip.request` |
| `2026-08-11 00:58:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.133[.]102` to AbuseIPDB if not already reported
- [ ] Block `49.124.133[.]102` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c841380c3a92

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-11 01:00 |
| **Last Seen** | 2026-08-11 01:00 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 01:00:43` | `cowrie.session.connect` |
| `2026-08-11 01:00:43` | `cowrie.client.version` |
| `2026-08-11 01:00:43` | `cowrie.client.kex` |
| `2026-08-11 01:00:44` | `cowrie.login.success` |
| `2026-08-11 01:00:45` | `cowrie.session.params` |
| `2026-08-11 01:00:45` | `cowrie.command.input` |
| `2026-08-11 01:00:45` | `cowrie.command.input` |
| `2026-08-11 01:00:45` | `cowrie.command.input` |
| `2026-08-11 01:00:45` | `cowrie.command.input` |
| `2026-08-11 01:00:45` | `cowrie.command.input` |
| `2026-08-11 01:00:45` | `cowrie.command.success` |
| `2026-08-11 01:00:45` | `cowrie.command.input` |
| `2026-08-11 01:00:45` | `cowrie.command.input` |
| `2026-08-11 01:00:45` | `cowrie.command.input` |
| `2026-08-11 01:00:45` | `cowrie.command.input` |
| `2026-08-11 01:00:45` | `cowrie.log.closed` |
| `2026-08-11 01:00:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-54923c4b2063

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-11 01:03 |
| **Last Seen** | 2026-08-11 01:03 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 01:03:14` | `cowrie.session.connect` |
| `2026-08-11 01:03:14` | `cowrie.client.version` |
| `2026-08-11 01:03:14` | `cowrie.client.kex` |
| `2026-08-11 01:03:15` | `cowrie.login.success` |
| `2026-08-11 01:03:17` | `cowrie.session.params` |
| `2026-08-11 01:03:17` | `cowrie.command.input` |
| `2026-08-11 01:03:17` | `cowrie.command.input` |
| `2026-08-11 01:03:17` | `cowrie.command.input` |
| `2026-08-11 01:03:17` | `cowrie.command.input` |
| `2026-08-11 01:03:17` | `cowrie.command.input` |
| `2026-08-11 01:03:17` | `cowrie.command.success` |
| `2026-08-11 01:03:17` | `cowrie.command.input` |
| `2026-08-11 01:03:17` | `cowrie.command.input` |
| `2026-08-11 01:03:17` | `cowrie.command.input` |
| `2026-08-11 01:03:17` | `cowrie.command.input` |
| `2026-08-11 01:03:17` | `cowrie.log.closed` |
| `2026-08-11 01:03:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed3328ebe13d

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-11 01:06 |
| **Last Seen** | 2026-08-11 01:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 01:06:13` | `cowrie.session.connect` |
| `2026-08-11 01:06:13` | `cowrie.client.version` |
| `2026-08-11 01:06:13` | `cowrie.client.kex` |
| `2026-08-11 01:06:14` | `cowrie.login.success` |
| `2026-08-11 01:06:15` | `cowrie.session.params` |
| `2026-08-11 01:06:15` | `cowrie.command.input` |
| `2026-08-11 01:06:15` | `cowrie.command.input` |
| `2026-08-11 01:06:15` | `cowrie.command.input` |
| `2026-08-11 01:06:15` | `cowrie.command.input` |
| `2026-08-11 01:06:15` | `cowrie.command.input` |
| `2026-08-11 01:06:15` | `cowrie.command.success` |
| `2026-08-11 01:06:15` | `cowrie.command.input` |
| `2026-08-11 01:06:15` | `cowrie.command.input` |
| `2026-08-11 01:06:15` | `cowrie.command.input` |
| `2026-08-11 01:06:15` | `cowrie.command.input` |
| `2026-08-11 01:06:15` | `cowrie.log.closed` |
| `2026-08-11 01:06:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a39cbfab6d2b

| Field | Detail |
|---|---|
| **Source IP** | `121.178.185[.]141` |
| **First Seen** | 2026-08-11 01:08 |
| **Last Seen** | 2026-08-11 01:09 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 01:08:59` | `cowrie.session.connect` |
| `2026-08-11 01:09:00` | `cowrie.client.version` |
| `2026-08-11 01:09:00` | `cowrie.client.kex` |
| `2026-08-11 01:09:03` | `cowrie.login.success` |
| `2026-08-11 01:09:04` | `cowrie.direct-tcpip.request` |
| `2026-08-11 01:09:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.178.185[.]141` to AbuseIPDB if not already reported
- [ ] Block `121.178.185[.]141` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ea1e2179376

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-11 01:10 |
| **Last Seen** | 2026-08-11 01:11 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 01:10:55` | `cowrie.session.connect` |
| `2026-08-11 01:10:55` | `cowrie.client.version` |
| `2026-08-11 01:10:55` | `cowrie.client.kex` |
| `2026-08-11 01:10:57` | `cowrie.login.success` |
| `2026-08-11 01:10:59` | `cowrie.session.params` |
| `2026-08-11 01:10:59` | `cowrie.command.input` |
| `2026-08-11 01:10:59` | `cowrie.command.input` |
| `2026-08-11 01:10:59` | `cowrie.command.input` |
| `2026-08-11 01:10:59` | `cowrie.command.input` |
| `2026-08-11 01:10:59` | `cowrie.command.input` |
| `2026-08-11 01:10:59` | `cowrie.command.success` |
| `2026-08-11 01:10:59` | `cowrie.command.input` |
| `2026-08-11 01:10:59` | `cowrie.command.input` |
| `2026-08-11 01:10:59` | `cowrie.command.input` |
| `2026-08-11 01:10:59` | `cowrie.command.input` |
| `2026-08-11 01:11:00` | `cowrie.log.closed` |
| `2026-08-11 01:11:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cdf087c75831

| Field | Detail |
|---|---|
| **Source IP** | `211.184.53[.]155` |
| **First Seen** | 2026-08-11 01:11 |
| **Last Seen** | 2026-08-11 01:11 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 01:11:06` | `cowrie.session.connect` |
| `2026-08-11 01:11:07` | `cowrie.client.version` |
| `2026-08-11 01:11:07` | `cowrie.client.kex` |
| `2026-08-11 01:11:09` | `cowrie.login.success` |
| `2026-08-11 01:11:10` | `cowrie.direct-tcpip.request` |
| `2026-08-11 01:11:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.184.53[.]155` to AbuseIPDB if not already reported
- [ ] Block `211.184.53[.]155` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5af06adf0402

| Field | Detail |
|---|---|
| **Source IP** | `153.37.177[.]219` |
| **First Seen** | 2026-08-11 01:11 |
| **Last Seen** | 2026-08-11 01:11 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 01:11:15` | `cowrie.session.connect` |
| `2026-08-11 01:11:16` | `cowrie.client.version` |
| `2026-08-11 01:11:16` | `cowrie.client.kex` |
| `2026-08-11 01:11:18` | `cowrie.login.success` |
| `2026-08-11 01:11:18` | `cowrie.direct-tcpip.request` |
| `2026-08-11 01:11:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `153.37.177[.]219` to AbuseIPDB if not already reported
- [ ] Block `153.37.177[.]219` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e49ea28c1f1

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-11 01:22 |
| **Last Seen** | 2026-08-11 01:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 01:22:44` | `cowrie.session.connect` |
| `2026-08-11 01:22:44` | `cowrie.client.version` |
| `2026-08-11 01:22:44` | `cowrie.client.kex` |
| `2026-08-11 01:22:44` | `cowrie.login.success` |
| `2026-08-11 01:22:45` | `cowrie.session.params` |
| `2026-08-11 01:22:45` | `cowrie.command.input` |
| `2026-08-11 01:22:45` | `cowrie.command.input` |
| `2026-08-11 01:22:45` | `cowrie.command.input` |
| `2026-08-11 01:22:45` | `cowrie.command.input` |
| `2026-08-11 01:22:45` | `cowrie.command.input` |
| `2026-08-11 01:22:45` | `cowrie.command.success` |
| `2026-08-11 01:22:45` | `cowrie.command.input` |
| `2026-08-11 01:22:45` | `cowrie.command.input` |
| `2026-08-11 01:22:45` | `cowrie.command.input` |
| `2026-08-11 01:22:45` | `cowrie.command.input` |
| `2026-08-11 01:22:45` | `cowrie.log.closed` |
| `2026-08-11 01:22:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e2889c99c3b

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-11 01:25 |
| **Last Seen** | 2026-08-11 01:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 01:25:47` | `cowrie.session.connect` |
| `2026-08-11 01:25:47` | `cowrie.client.version` |
| `2026-08-11 01:25:47` | `cowrie.client.kex` |
| `2026-08-11 01:25:48` | `cowrie.login.success` |
| `2026-08-11 01:25:48` | `cowrie.direct-tcpip.request` |
| `2026-08-11 01:25:48` | `cowrie.direct-tcpip.data` |
| `2026-08-11 01:25:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00d51af3eefb

| Field | Detail |
|---|---|
| **Source IP** | `122.170.99[.]195` |
| **First Seen** | 2026-08-11 01:27 |
| **Last Seen** | 2026-08-11 01:27 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 01:27:26` | `cowrie.session.connect` |
| `2026-08-11 01:27:27` | `cowrie.client.version` |
| `2026-08-11 01:27:27` | `cowrie.client.kex` |
| `2026-08-11 01:27:29` | `cowrie.login.success` |
| `2026-08-11 01:27:29` | `cowrie.direct-tcpip.request` |
| `2026-08-11 01:27:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.170.99[.]195` to AbuseIPDB if not already reported
- [ ] Block `122.170.99[.]195` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e62138a77e9

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-11 01:29 |
| **Last Seen** | 2026-08-11 01:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 01:29:37` | `cowrie.session.connect` |
| `2026-08-11 01:29:37` | `cowrie.client.version` |
| `2026-08-11 01:29:37` | `cowrie.client.kex` |
| `2026-08-11 01:29:38` | `cowrie.login.success` |
| `2026-08-11 01:29:39` | `cowrie.session.params` |
| `2026-08-11 01:29:39` | `cowrie.command.input` |
| `2026-08-11 01:29:39` | `cowrie.command.input` |
| `2026-08-11 01:29:39` | `cowrie.command.input` |
| `2026-08-11 01:29:39` | `cowrie.command.input` |
| `2026-08-11 01:29:39` | `cowrie.command.input` |
| `2026-08-11 01:29:39` | `cowrie.command.success` |
| `2026-08-11 01:29:39` | `cowrie.command.input` |
| `2026-08-11 01:29:39` | `cowrie.command.input` |
| `2026-08-11 01:29:39` | `cowrie.command.input` |
| `2026-08-11 01:29:39` | `cowrie.command.input` |
| `2026-08-11 01:29:39` | `cowrie.log.closed` |
| `2026-08-11 01:29:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cabfa345fdb7

| Field | Detail |
|---|---|
| **Source IP** | `154.241.31[.]235` |
| **First Seen** | 2026-08-11 01:33 |
| **Last Seen** | 2026-08-11 01:35 |
| **Session Duration** | 88s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 01:33:51` | `cowrie.session.connect` |
| `2026-08-11 01:33:51` | `cowrie.client.version` |
| `2026-08-11 01:33:51` | `cowrie.client.kex` |
| `2026-08-11 01:33:52` | `cowrie.login.success` |
| `2026-08-11 01:35:19` | `cowrie.session.file_upload` |
| `2026-08-11 01:35:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.241.31[.]235` to AbuseIPDB if not already reported
- [ ] Block `154.241.31[.]235` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d80a29a3df4

| Field | Detail |
|---|---|
| **Source IP** | `117.247.239[.]202` |
| **First Seen** | 2026-08-11 01:37 |
| **Last Seen** | 2026-08-11 01:37 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 01:37:49` | `cowrie.session.connect` |
| `2026-08-11 01:37:49` | `cowrie.client.version` |
| `2026-08-11 01:37:49` | `cowrie.client.kex` |
| `2026-08-11 01:37:51` | `cowrie.login.success` |
| `2026-08-11 01:37:52` | `cowrie.direct-tcpip.request` |
| `2026-08-11 01:37:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.247.239[.]202` to AbuseIPDB if not already reported
- [ ] Block `117.247.239[.]202` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d76f8da9edbe

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-11 01:38 |
| **Last Seen** | 2026-08-11 01:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 01:38:26` | `cowrie.session.connect` |
| `2026-08-11 01:38:26` | `cowrie.client.version` |
| `2026-08-11 01:38:27` | `cowrie.client.kex` |
| `2026-08-11 01:38:27` | `cowrie.login.success` |
| `2026-08-11 01:38:28` | `cowrie.session.params` |
| `2026-08-11 01:38:28` | `cowrie.command.input` |
| `2026-08-11 01:38:28` | `cowrie.command.input` |
| `2026-08-11 01:38:28` | `cowrie.command.input` |
| `2026-08-11 01:38:28` | `cowrie.command.input` |
| `2026-08-11 01:38:28` | `cowrie.command.input` |
| `2026-08-11 01:38:28` | `cowrie.command.success` |
| `2026-08-11 01:38:28` | `cowrie.command.input` |
| `2026-08-11 01:38:28` | `cowrie.command.input` |
| `2026-08-11 01:38:28` | `cowrie.command.input` |
| `2026-08-11 01:38:28` | `cowrie.command.input` |
| `2026-08-11 01:38:28` | `cowrie.log.closed` |
| `2026-08-11 01:38:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b65c184dcda4

| Field | Detail |
|---|---|
| **Source IP** | `78.187.9[.]111` |
| **First Seen** | 2026-08-11 01:42 |
| **Last Seen** | 2026-08-11 01:43 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 01:42:57` | `cowrie.session.connect` |
| `2026-08-11 01:42:57` | `cowrie.client.version` |
| `2026-08-11 01:42:57` | `cowrie.client.kex` |
| `2026-08-11 01:42:58` | `cowrie.login.success` |
| `2026-08-11 01:42:59` | `cowrie.direct-tcpip.request` |
| `2026-08-11 01:43:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `78.187.9[.]111` to AbuseIPDB if not already reported
- [ ] Block `78.187.9[.]111` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af6eeea99b17

| Field | Detail |
|---|---|
| **Source IP** | `60.166.8[.]174` |
| **First Seen** | 2026-08-11 01:45 |
| **Last Seen** | 2026-08-11 01:45 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 01:45:21` | `cowrie.session.connect` |
| `2026-08-11 01:45:22` | `cowrie.client.version` |
| `2026-08-11 01:45:22` | `cowrie.client.kex` |
| `2026-08-11 01:45:24` | `cowrie.login.success` |
| `2026-08-11 01:45:24` | `cowrie.direct-tcpip.request` |
| `2026-08-11 01:45:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.166.8[.]174` to AbuseIPDB if not already reported
- [ ] Block `60.166.8[.]174` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3edf8cf65795

| Field | Detail |
|---|---|
| **Source IP** | `59.46.182[.]10` |
| **First Seen** | 2026-08-11 01:45 |
| **Last Seen** | 2026-08-11 01:45 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 01:45:34` | `cowrie.session.connect` |
| `2026-08-11 01:45:36` | `cowrie.client.version` |
| `2026-08-11 01:45:36` | `cowrie.client.kex` |
| `2026-08-11 01:45:39` | `cowrie.login.success` |
| `2026-08-11 01:45:40` | `cowrie.direct-tcpip.request` |
| `2026-08-11 01:45:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.46.182[.]10` to AbuseIPDB if not already reported
- [ ] Block `59.46.182[.]10` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef0317d6f719

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-11 01:45 |
| **Last Seen** | 2026-08-11 01:45 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 01:45:41` | `cowrie.session.connect` |
| `2026-08-11 01:45:41` | `cowrie.client.version` |
| `2026-08-11 01:45:42` | `cowrie.client.kex` |
| `2026-08-11 01:45:42` | `cowrie.login.success` |
| `2026-08-11 01:45:43` | `cowrie.session.params` |
| `2026-08-11 01:45:43` | `cowrie.command.input` |
| `2026-08-11 01:45:43` | `cowrie.command.input` |
| `2026-08-11 01:45:43` | `cowrie.command.input` |
| `2026-08-11 01:45:43` | `cowrie.command.input` |
| `2026-08-11 01:45:43` | `cowrie.command.input` |
| `2026-08-11 01:45:43` | `cowrie.command.success` |
| `2026-08-11 01:45:43` | `cowrie.command.input` |
| `2026-08-11 01:45:43` | `cowrie.command.input` |
| `2026-08-11 01:45:43` | `cowrie.command.input` |
| `2026-08-11 01:45:43` | `cowrie.command.input` |
| `2026-08-11 01:45:44` | `cowrie.log.closed` |
| `2026-08-11 01:45:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4a5f7b7e896

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-11 01:55 |
| **Last Seen** | 2026-08-11 01:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 01:55:52` | `cowrie.session.connect` |
| `2026-08-11 01:55:52` | `cowrie.client.version` |
| `2026-08-11 01:55:52` | `cowrie.client.kex` |
| `2026-08-11 01:55:53` | `cowrie.login.success` |
| `2026-08-11 01:55:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf1903d9d8e8

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-11 01:55 |
| **Last Seen** | 2026-08-11 01:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 01:55:52` | `cowrie.session.connect` |
| `2026-08-11 01:55:52` | `cowrie.client.version` |
| `2026-08-11 01:55:52` | `cowrie.client.kex` |
| `2026-08-11 01:55:53` | `cowrie.login.success` |
| `2026-08-11 01:55:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7009d21b903

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-11 02:08 |
| **Last Seen** | 2026-08-11 02:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 02:08:42` | `cowrie.session.connect` |
| `2026-08-11 02:08:42` | `cowrie.client.version` |
| `2026-08-11 02:08:42` | `cowrie.client.kex` |
| `2026-08-11 02:08:43` | `cowrie.login.success` |
| `2026-08-11 02:08:43` | `cowrie.direct-tcpip.request` |
| `2026-08-11 02:08:43` | `cowrie.direct-tcpip.data` |
| `2026-08-11 02:08:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-466e7dcd6a3d

| Field | Detail |
|---|---|
| **Source IP** | `197.251.193[.]6` |
| **First Seen** | 2026-08-11 02:11 |
| **Last Seen** | 2026-08-11 02:11 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 02:11:44` | `cowrie.session.connect` |
| `2026-08-11 02:11:44` | `cowrie.client.version` |
| `2026-08-11 02:11:44` | `cowrie.client.kex` |
| `2026-08-11 02:11:46` | `cowrie.login.success` |
| `2026-08-11 02:11:46` | `cowrie.direct-tcpip.request` |
| `2026-08-11 02:11:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.251.193[.]6` to AbuseIPDB if not already reported
- [ ] Block `197.251.193[.]6` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5820b7d6a4f2

| Field | Detail |
|---|---|
| **Source IP** | `34.41.211[.]48` |
| **First Seen** | 2026-08-11 02:11 |
| **Last Seen** | 2026-08-11 02:11 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 02:11:51` | `cowrie.session.connect` |
| `2026-08-11 02:11:51` | `cowrie.client.version` |
| `2026-08-11 02:11:51` | `cowrie.client.kex` |
| `2026-08-11 02:11:52` | `cowrie.login.success` |
| `2026-08-11 02:11:53` | `cowrie.direct-tcpip.request` |
| `2026-08-11 02:11:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.41.211[.]48` to AbuseIPDB if not already reported
- [ ] Block `34.41.211[.]48` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de4d4c340582

| Field | Detail |
|---|---|
| **Source IP** | `182.92.204[.]91` |
| **First Seen** | 2026-08-11 02:18 |
| **Last Seen** | 2026-08-11 02:18 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 02:18:28` | `cowrie.session.connect` |
| `2026-08-11 02:18:28` | `cowrie.client.version` |
| `2026-08-11 02:18:29` | `cowrie.client.kex` |
| `2026-08-11 02:18:30` | `cowrie.login.success` |
| `2026-08-11 02:18:31` | `cowrie.session.params` |
| `2026-08-11 02:18:31` | `cowrie.command.input` |
| `2026-08-11 02:18:32` | `cowrie.log.closed` |
| `2026-08-11 02:18:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.92.204[.]91` to AbuseIPDB if not already reported
- [ ] Block `182.92.204[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d28af8be7c6

| Field | Detail |
|---|---|
| **Source IP** | `213.55.79[.]195` |
| **First Seen** | 2026-08-11 02:35 |
| **Last Seen** | 2026-08-11 02:36 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 02:35:55` | `cowrie.session.connect` |
| `2026-08-11 02:35:56` | `cowrie.client.version` |
| `2026-08-11 02:35:56` | `cowrie.client.kex` |
| `2026-08-11 02:35:57` | `cowrie.login.success` |
| `2026-08-11 02:35:57` | `cowrie.direct-tcpip.request` |
| `2026-08-11 02:36:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.55.79[.]195` to AbuseIPDB if not already reported
- [ ] Block `213.55.79[.]195` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c31d0c23407a

| Field | Detail |
|---|---|
| **Source IP** | `185.221.21[.]17` |
| **First Seen** | 2026-08-11 02:37 |
| **Last Seen** | 2026-08-11 02:37 |
| **Session Duration** | 31s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 02:37:26` | `cowrie.session.connect` |
| `2026-08-11 02:37:26` | `cowrie.client.version` |
| `2026-08-11 02:37:26` | `cowrie.client.kex` |
| `2026-08-11 02:37:27` | `cowrie.login.success` |
| `2026-08-11 02:37:58` | `cowrie.session.file_upload` |
| `2026-08-11 02:37:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.221.21[.]17` to AbuseIPDB if not already reported
- [ ] Block `185.221.21[.]17` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5a9fb8385b8

| Field | Detail |
|---|---|
| **Source IP** | `130.211.76[.]1` |
| **First Seen** | 2026-08-11 02:49 |
| **Last Seen** | 2026-08-11 02:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 02:49:29` | `cowrie.session.connect` |
| `2026-08-11 02:49:29` | `cowrie.login.success` |
| `2026-08-11 02:49:30` | `cowrie.session.params` |
| `2026-08-11 02:49:30` | `cowrie.command.input` |
| `2026-08-11 02:49:30` | `cowrie.command.input` |
| `2026-08-11 02:49:30` | `cowrie.command.failed` |
| `2026-08-11 02:49:30` | `cowrie.command.input` |
| `2026-08-11 02:49:30` | `cowrie.log.closed` |
| `2026-08-11 02:49:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.211.76[.]1` to AbuseIPDB if not already reported
- [ ] Block `130.211.76[.]1` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-243732286739

| Field | Detail |
|---|---|
| **Source IP** | `130.211.76[.]1` |
| **First Seen** | 2026-08-11 02:49 |
| **Last Seen** | 2026-08-11 02:49 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 02:49:38` | `cowrie.session.connect` |
| `2026-08-11 02:49:38` | `cowrie.login.success` |
| `2026-08-11 02:49:39` | `cowrie.session.params` |
| `2026-08-11 02:49:39` | `cowrie.command.input` |
| `2026-08-11 02:49:39` | `cowrie.command.failed` |
| `2026-08-11 02:49:42` | `cowrie.log.closed` |
| `2026-08-11 02:49:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.211.76[.]1` to AbuseIPDB if not already reported
- [ ] Block `130.211.76[.]1` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e86e51c88875

| Field | Detail |
|---|---|
| **Source IP** | `130.211.76[.]1` |
| **First Seen** | 2026-08-11 02:49 |
| **Last Seen** | 2026-08-11 02:49 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 02:49:40` | `cowrie.session.connect` |
| `2026-08-11 02:49:40` | `cowrie.login.success` |
| `2026-08-11 02:49:40` | `cowrie.session.params` |
| `2026-08-11 02:49:40` | `cowrie.command.input` |
| `2026-08-11 02:49:42` | `cowrie.log.closed` |
| `2026-08-11 02:49:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.211.76[.]1` to AbuseIPDB if not already reported
- [ ] Block `130.211.76[.]1` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31b0daf7854e

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-11 02:50 |
| **Last Seen** | 2026-08-11 02:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 02:50:45` | `cowrie.session.connect` |
| `2026-08-11 02:50:45` | `cowrie.client.version` |
| `2026-08-11 02:50:45` | `cowrie.client.kex` |
| `2026-08-11 02:50:45` | `cowrie.login.success` |
| `2026-08-11 02:50:46` | `cowrie.direct-tcpip.request` |
| `2026-08-11 02:50:46` | `cowrie.direct-tcpip.data` |
| `2026-08-11 02:50:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-859add1d2217

| Field | Detail |
|---|---|
| **Source IP** | `14.54.22[.]11` |
| **First Seen** | 2026-08-11 02:51 |
| **Last Seen** | 2026-08-11 02:51 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 02:51:08` | `cowrie.session.connect` |
| `2026-08-11 02:51:08` | `cowrie.client.version` |
| `2026-08-11 02:51:08` | `cowrie.client.kex` |
| `2026-08-11 02:51:11` | `cowrie.login.success` |
| `2026-08-11 02:51:12` | `cowrie.direct-tcpip.request` |
| `2026-08-11 02:51:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.54.22[.]11` to AbuseIPDB if not already reported
- [ ] Block `14.54.22[.]11` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5afc103b7e0b

| Field | Detail |
|---|---|
| **Source IP** | `124.160.45[.]26` |
| **First Seen** | 2026-08-11 02:53 |
| **Last Seen** | 2026-08-11 02:53 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 02:53:47` | `cowrie.session.connect` |
| `2026-08-11 02:53:49` | `cowrie.client.version` |
| `2026-08-11 02:53:49` | `cowrie.client.kex` |
| `2026-08-11 02:53:52` | `cowrie.login.success` |
| `2026-08-11 02:53:54` | `cowrie.direct-tcpip.request` |
| `2026-08-11 02:53:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.160.45[.]26` to AbuseIPDB if not already reported
- [ ] Block `124.160.45[.]26` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `164.92.115[.]22` | **52** | 2026-08-11 00:55 | 2026-08-11 02:52 | 35m | 0 | `T1592` | 🟠 MEDIUM |
| `139.199.80[.]137` | **5** | 2026-08-11 00:57 | 2026-08-11 02:41 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]121` | **4** | 2026-08-11 00:57 | 2026-08-11 01:13 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]163` | **3** | 2026-08-11 01:31 | 2026-08-11 01:31 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]164` | **3** | 2026-08-11 02:35 | 2026-08-11 02:35 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]103` | **3** | 2026-08-11 02:06 | 2026-08-11 02:07 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]35` | **3** | 2026-08-11 02:07 | 2026-08-11 02:07 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]82` | **3** | 2026-08-11 02:05 | 2026-08-11 02:06 | 0m | 0 | `T1592` | 🟢 LOW |
| `107.150.146[.]69` | **2** | 2026-08-11 01:05 | 2026-08-11 01:36 | 1m | 0 | `T1592` | 🟢 LOW |
| `172.236.228[.]245` | **2** | 2026-08-11 01:08 | 2026-08-11 01:08 | 0m | 0 | `T1592` | 🟢 LOW |
| `190.104.36[.]189` | **2** | 2026-08-11 02:12 | 2026-08-11 02:13 | 0m | 0 | `T1592` | 🟢 LOW |
| `196.251.121[.]142` | **2** | 2026-08-11 01:14 | 2026-08-11 01:15 | 1m | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]167` | **2** | 2026-08-11 02:20 | 2026-08-11 02:20 | 0m | 0 | `T1592` | 🟢 LOW |
| `71.6.146[.]185` | **2** | 2026-08-11 02:24 | 2026-08-11 02:24 | 0m | 0 | `T1592` | 🟢 LOW |
| `100.55.74[.]174` | 1 | 2026-08-11 01:21 | 2026-08-11 01:21 | 1s | 0 | `T1592` | 🟢 LOW |
| `138.255.206[.]231` | 1 | 2026-08-11 02:54 | 2026-08-11 02:55 | 11s | 0 | `T1592` | 🟢 LOW |
| `172.104.131[.]24` | 1 | 2026-08-11 01:22 | 2026-08-11 01:22 | 0s | 0 | `T1592` | 🟢 LOW |
| `183.243.126[.]46` | 1 | 2026-08-11 01:50 | 2026-08-11 01:52 | 120s | 0 | `T1592` | 🟢 LOW |
| `184.181.217[.]198` | 1 | 2026-08-11 02:12 | 2026-08-11 02:14 | 120s | 0 | `T1592` | 🟢 LOW |
| `194.195.210[.]47` | 1 | 2026-08-11 01:42 | 2026-08-11 01:42 | 0s | 0 | `T1592` | 🟢 LOW |
| `220.180.249[.]165` | 1 | 2026-08-11 01:52 | 2026-08-11 01:52 | 14s | 0 | `T1592` | 🟢 LOW |
| `31.40.134[.]78` | 1 | 2026-08-11 01:46 | 2026-08-11 01:46 | 13s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]157` | 1 | 2026-08-11 01:10 | 2026-08-11 01:10 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.198.224[.]26` | 1 | 2026-08-11 02:28 | 2026-08-11 02:28 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.5[.]11` | 1 | 2026-08-11 02:43 | 2026-08-11 02:43 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]200` | 1 | 2026-08-11 01:02 | 2026-08-11 01:02 | 17s | 0 | `T1592` | 🟢 LOW |
| `71.6.232[.]30` | 1 | 2026-08-11 00:57 | 2026-08-11 00:58 | 7s | 0 | `T1592` | 🟢 LOW |
| `81.236.211[.]54` | 1 | 2026-08-11 00:58 | 2026-08-11 01:00 | 120s | 0 | `T1592` | 🟢 LOW |
| `84.54.70[.]7` | 1 | 2026-08-11 01:01 | 2026-08-11 01:03 | 120s | 0 | `T1592` | 🟢 LOW |
| `91.210.248[.]194` | 1 | 2026-08-11 01:32 | 2026-08-11 01:32 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.233.83[.]203` | 1 | 2026-08-11 01:34 | 2026-08-11 01:35 | 40s | 0 | `T1592` | 🟢 LOW |

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
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 84/100 | 🔴 HIGH | **36/75** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 41/100 | 🟡 MEDIUM | **29/75** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **24/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 50/100 | 🟡 MEDIUM | **27/74** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
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
| `287962211de7bcadb39f7576732438b43ee6aab420ec23c29a9d12a8151a547f` | ELF Binary (Linux executable) (x86 32-bit) | `287962211de7bcad...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
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
| `49.124.133[.]102` | MY | DiGi Telecommunications Sdn Bhd | **100** ⚠️ | 21 |
| `81.236.211[.]54` | SE | Telia Network Services | **100** ⚠️ | 50 |
| `66.132.195[.]82` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `121.178.185[.]141` | KR | Korea Telecom | **100** ⚠️ | 50 |
| `78.187.9[.]111` | TR | Turk Telekomunikasyon Anonim Sirketi | **100** ⚠️ | 50 |
| `197.251.193[.]6` | GH | Ghana Telecommunications Company Limited | **100** ⚠️ | 50 |
| `66.132.186[.]167` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `194.165.16[.]164` | LT | Flyservers S.A. | **100** ⚠️ | 50 |
| `124.160.45[.]26` | CN | YINGYUTOUZI,HANGZHOU,ZHEJIANG | **100** ⚠️ | 50 |
| `71.6.232[.]30` | US | CariNet, Inc. | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 43 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 33 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 8 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 8 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 8 |

---

## 🔕 False Positive Summary (49 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 5 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 43 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 187 cases |
| Tool 34  | Credential Extractor        | ✅ 49 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 11 fingerprints |
| Tool 36  | Command Clustering          | ✅ 4 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 65 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 49 filtered (26.2%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 44 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 22 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 33 priority case(s) shown individually · 31 recon entry/entries in table (14 group(s) consolidating 88 session(s)).

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
_Report time: 2026-08-11T03:51:34Z_

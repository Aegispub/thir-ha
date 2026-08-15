# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-15 |
| **Generated At** | 2026-08-15T12:42:55Z |
| **Shift Time** | 12:42 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **6328** |
| Confirmed Threats | **6299** |
| False Positives Filtered | **29** (0.5%) |
| Unique Attacker IPs | **77** |
| Countries of Origin | **31** |
| High Severity Cases | **108** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **6220** |
| Malware Samples Analyzed | **2** HIGH · **23** MED · 20 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **139** |
| Unique Credential Pairs | **100** |
| Unique Usernames | **10** |
| Unique Passwords | **73** |
| Successful Auth Pairs | **124** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 55 |
| `admin` | 30 |
| `ubnt` | 14 |
| `support` | 10 |
| `centos` | 7 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `12345` | 8 |
| `letmein` | 6 |
| `p@ssw0rd` | 6 |
| `password123` | 5 |
| `qwer1234` | 5 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `centos` | `letmein` | 6 |
| `root` | `password123` | 5 |
| `ubnt` | `qwer1234` | 5 |
| `user` | `p@ssw0rd` | 5 |
| `admin` | `444444` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `centos` | `qwerty1` | `181.212.174.164` | 2026-08-15T08:55:58 |
| `root` | `qwe123` | `217.165.22.192` | 2026-08-15T08:59:50 |
| `debian` | `12345` | `10.0.0.73` | 2026-08-15T09:03:54 |
| `nobody` | `112233` | `10.0.0.73` | 2026-08-15T09:05:25 |
| `nobody` | `Password` | `178.132.144.161` | 2026-08-15T09:07:03 |
| `nobody` | `Password` | `59.46.182.10` | 2026-08-15T09:07:17 |
| `root` | `1` | `195.178.110.227` | 2026-08-15T09:07:48 |
| `root` | `12` | `195.178.110.227` | 2026-08-15T09:09:29 |
| `admin` | `admin` | `10.0.0.73` | 2026-08-15T09:09:43 |
| `root` | `000000000` | `45.142.193.164` | 2026-08-15T09:09:53 |
| `root` | `123` | `195.178.110.227` | 2026-08-15T09:11:14 |
| `root` | `password123` | `10.0.0.73` | 2026-08-15T09:11:19 |
| `root` | `1234` | `195.178.110.227` | 2026-08-15T09:13:01 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-08-15T09:14:13 |
| `root` | `123@@@` | `64.110.90.250` | 2026-08-15T09:14:13 |
| `root` | `12345` | `195.178.110.227` | 2026-08-15T09:14:43 |
| `root` | `1234567` | `195.178.110.227` | 2026-08-15T09:18:04 |
| `root` | `1qaz@WSX3edc` | `217.165.22.192` | 2026-08-15T09:19:03 |
| `root` | `12345678` | `195.178.110.227` | 2026-08-15T09:19:45 |
| `root` | `123456789` | `195.178.110.227` | 2026-08-15T09:21:20 |
| `root` | `1234567890` | `195.178.110.227` | 2026-08-15T09:22:59 |
| `admin` | `444444` | `10.0.0.73` | 2026-08-15T09:23:24 |
| `root` | `123qwe` | `195.178.110.227` | 2026-08-15T09:24:36 |
| `admin` | `444444` | `124.239.129.2` | 2026-08-15T09:25:11 |
| `root` | `123qwerty` | `195.178.110.227` | 2026-08-15T09:26:15 |
| `centos` | `letmein` | `148.227.91.88` | 2026-08-15T09:27:44 |
| `root` | `21` | `195.178.110.227` | 2026-08-15T09:27:52 |
| `centos` | `letmein` | `178.178.222.58` | 2026-08-15T09:27:57 |
| `ubnt` | `ubnt2022` | `10.0.0.73` | 2026-08-15T09:29:22 |
| `root` | `321` | `195.178.110.227` | 2026-08-15T09:29:31 |
| `root` | `password123` | `78.187.9.111` | 2026-08-15T09:29:34 |
| `root` | `password123` | `85.19.195.12` | 2026-08-15T09:29:41 |
| `root` | `password123` | `171.217.70.151` | 2026-08-15T09:29:49 |
| `root` | `password123` | `182.76.36.62` | 2026-08-15T09:29:59 |
| `support` | `support` | `10.0.0.73` | 2026-08-15T09:30:57 |
| `root` | `4321` | `195.178.110.227` | 2026-08-15T09:31:12 |
| `root` | `0000000000` | `45.142.193.164` | 2026-08-15T09:32:45 |
| `root` | `54321` | `195.178.110.227` | 2026-08-15T09:32:52 |
| `root` | `654321` | `195.178.110.227` | 2026-08-15T09:34:23 |
| `root` | `P4ssw0rd` | `195.178.110.227` | 2026-08-15T09:35:57 |
| `root` | `P4ssword` | `195.178.110.227` | 2026-08-15T09:37:32 |
| `root` | `Apple@123` | `217.165.22.192` | 2026-08-15T09:38:16 |
| `root` | `P@ssw0rd` | `195.178.110.227` | 2026-08-15T09:39:08 |
| `centos` | `letmein` | `10.0.0.73` | 2026-08-15T09:39:15 |
| `root` | `Passw0rd` | `195.178.110.227` | 2026-08-15T09:40:41 |
| `admin` | `444444` | `196.188.93.169` | 2026-08-15T09:41:20 |
| `root` | `p4ssword` | `195.178.110.227` | 2026-08-15T09:42:10 |
| `root` | `p@ssw0rd` | `195.178.110.227` | 2026-08-15T09:43:44 |
| `ftp` | `123` | `10.0.0.73` | 2026-08-15T09:44:27 |
| `support` | `qwerty12345` | `10.0.0.73` | 2026-08-15T09:45:13 |
| `root` | `passw0rd` | `195.178.110.227` | 2026-08-15T09:45:15 |
| `root` | `password` | `195.178.110.227` | 2026-08-15T09:46:45 |
| `root` | `qwerty` | `195.178.110.227` | 2026-08-15T09:48:17 |
| `root` | `root1` | `195.178.110.227` | 2026-08-15T09:51:27 |
| `root` | `root12` | `195.178.110.227` | 2026-08-15T09:53:04 |
| `root` | `root123` | `195.178.110.227` | 2026-08-15T09:54:48 |
| `root` | `Qazwsxedc123` | `45.142.193.164` | 2026-08-15T09:55:37 |
| `centos` | `letmein` | `182.53.52.68` | 2026-08-15T09:56:11 |
| `centos` | `letmein` | `103.93.37.178` | 2026-08-15T09:56:20 |
| `root` | `root1234` | `195.178.110.227` | 2026-08-15T09:56:47 |
| `ubnt` | `webmaster` | `10.0.0.73` | 2026-08-15T09:57:11 |
| `root` | `pgj-heu05HQM=bMvz` | `217.165.22.192` | 2026-08-15T09:57:29 |
| `root` | `root12345` | `195.178.110.227` | 2026-08-15T09:58:53 |
| `root` | `root123456` | `195.178.110.227` | 2026-08-15T10:00:20 |
| `ubnt` | `qwer1234` | `67.85.146.216` | 2026-08-15T10:01:28 |
| `ubnt` | `qwer1234` | `27.107.102.154` | 2026-08-15T10:01:36 |
| `root` | `root1234567` | `195.178.110.227` | 2026-08-15T10:01:48 |
| `root` | `root123456789` | `195.178.110.227` | 2026-08-15T10:03:21 |
| `support` | `qwerty12345` | `58.245.210.70` | 2026-08-15T10:03:49 |
| `root` | `root1234567890` | `195.178.110.227` | 2026-08-15T10:04:57 |
| `admin` | `1` | `195.178.110.227` | 2026-08-15T10:06:28 |
| `admin` | `12` | `195.178.110.227` | 2026-08-15T10:07:58 |
| `admin` | `123` | `195.178.110.227` | 2026-08-15T10:09:26 |
| `support` | `support` | `176.53.159.196` | 2026-08-15T10:10:46 |
| `admin` | `1234` | `195.178.110.227` | 2026-08-15T10:10:54 |
| `admin` | `12345` | `195.178.110.227` | 2026-08-15T10:12:24 |
| `ubnt` | `qwer1234` | `10.0.0.73` | 2026-08-15T10:12:49 |
| `admin` | `123456` | `195.178.110.227` | 2026-08-15T10:13:58 |
| `ubnt` | `webmaster` | `39.164.94.190` | 2026-08-15T10:15:02 |
| `ubnt` | `webmaster` | `200.58.83.79` | 2026-08-15T10:15:11 |
| `admin` | `1234567` | `195.178.110.227` | 2026-08-15T10:15:43 |
| `root` | `Ab123456` | `217.165.22.192` | 2026-08-15T10:16:42 |
| `admin` | `12345678` | `195.178.110.227` | 2026-08-15T10:17:37 |
| `root` | `smart@123` | `45.142.193.164` | 2026-08-15T10:18:34 |
| `user` | `p@ssw0rd` | `10.0.0.73` | 2026-08-15T10:18:55 |
| `admin` | `123456789` | `195.178.110.227` | 2026-08-15T10:19:31 |
| `admin` | `1234567890` | `195.178.110.227` | 2026-08-15T10:21:00 |
| `admin` | `123qwe` | `195.178.110.227` | 2026-08-15T10:22:24 |
| `admin` | `123qwerty` | `195.178.110.227` | 2026-08-15T10:23:41 |
| `root` | `---fuck_you----` | `223.166.28.16` | 2026-08-15T10:23:53 |
| `admin` | `21` | `195.178.110.227` | 2026-08-15T10:24:59 |
| `admin` | `321` | `195.178.110.227` | 2026-08-15T10:26:22 |
| `admin` | `654321` | `195.178.110.227` | 2026-08-15T10:27:46 |
| `admin` | `Password` | `195.178.110.227` | 2026-08-15T10:29:12 |
| `ubnt` | `qwer1234` | `213.230.124.17` | 2026-08-15T10:30:08 |
| `admin` | `admin` | `195.178.110.227` | 2026-08-15T10:30:40 |
| `support` | `12345` | `10.0.0.73` | 2026-08-15T10:31:07 |
| `admin` | `admin1` | `195.178.110.227` | 2026-08-15T10:32:10 |
| `support` | `12345` | `183.82.108.109` | 2026-08-15T10:32:51 |
| `admin` | `admin12` | `195.178.110.227` | 2026-08-15T10:33:44 |
| `admin` | `admin123` | `195.178.110.227` | 2026-08-15T10:35:21 |
| `ubnt` | `asdfgh` | `116.114.94.242` | 2026-08-15T10:35:22 |
| `ubnt` | `asdfgh` | `65.20.204.41` | 2026-08-15T10:35:30 |
| `root` | `123abc` | `217.165.22.192` | 2026-08-15T10:35:54 |
| `admin` | `pa$w0rd` | `195.178.110.227` | 2026-08-15T10:37:00 |
| `user` | `p@ssw0rd` | `166.130.176.136` | 2026-08-15T10:37:26 |
| `user` | `p@ssw0rd` | `179.189.85.66` | 2026-08-15T10:37:34 |
| `user` | `p@ssw0rd` | `187.218.57.50` | 2026-08-15T10:37:46 |
| `admin` | `passw0rd` | `195.178.110.227` | 2026-08-15T10:38:40 |
| `admin` | `password` | `195.178.110.227` | 2026-08-15T10:40:27 |
| `root` | `Dell@1234` | `45.142.193.164` | 2026-08-15T10:41:31 |
| `admin` | `qwerty` | `195.178.110.227` | 2026-08-15T10:41:53 |
| `backup` | `123qwe` | `195.178.110.227` | 2026-08-15T10:43:17 |
| `backup` | `54321` | `195.178.110.227` | 2026-08-15T10:44:42 |
| `backup` | `backup` | `195.178.110.227` | 2026-08-15T10:46:09 |
| `ubnt` | `asdfgh` | `10.0.0.73` | 2026-08-15T10:46:48 |
| `backup` | `backup1` | `195.178.110.227` | 2026-08-15T10:47:37 |
| `support` | `12345` | `81.22.51.64` | 2026-08-15T10:48:56 |
| `backup` | `backup12` | `195.178.110.227` | 2026-08-15T10:49:07 |
| `backup` | `backup123` | `195.178.110.227` | 2026-08-15T10:50:35 |
| `backup` | `wasd` | `195.178.110.227` | 2026-08-15T10:52:00 |
| `debian` | `qwerty1234` | `10.0.0.73` | 2026-08-15T10:52:58 |
| `debian` | `123qwe` | `195.178.110.227` | 2026-08-15T10:53:24 |
| `debian` | `54321` | `195.178.110.227` | 2026-08-15T10:54:48 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **6328** |
| Sessions with Fingerprint | **13** |
| Unique HASSH Fingerprints | **13** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 88 |
| OpenSSH | 30 |
| libssh | 6 |
| Paramiko (Python) | 2 |
| Unknown | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `2ec37a7cc8da...` | Mirai/variant | 69 | 1 |
| `acaa53e0a7d7...` | Mirai/variant | 30 | 30 |
| `e45f2d6d7f79...` | Mirai/variant | 6 | 1 |
| `98ddc5604ef6...` | Modern SSH client | 5 | 1 |
| `4e066189c3bb...` | Generic scanner | 3 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `2ec37a7cc8da...` | Go SSH scanner | 69 | 1 | Mirai/variant |
| `acaa53e0a7d7...` | OpenSSH | 30 | 30 | Mirai/variant |
| `e45f2d6d7f79...` | Go SSH scanner | 6 | 1 | Mirai/variant |
| `95420f9d932d...` | libssh | 6 | 2 | — |
| `98ddc5604ef6...` | Go SSH scanner | 5 | 1 | Modern SSH client |
| `4e066189c3bb...` | Go SSH scanner | 3 | 1 | Generic scanner |
| `a2de0f306611...` | Paramiko (Python) | 2 | 1 | Mirai/variant |
| `dd9bcf093c35...` | Unknown | 2 | 2 | Mirai/variant |

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
| **Recon Loader Script** | 🟡 MEDIUM | 67 | 1 | `T1082, T1592, T1078, T1083` |

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
Source IPs: `195.178.110.227`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **77** |
| Unique ASNs | **66** |
| High-Risk ASNs | **53** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 4 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 3 | HIGH |
| `AS396982` | Google LLC | 3 | HIGH |
| `AS63949` | Akamai Connected Cloud | 3 | HIGH |
| `AS271922` | LEIRIA HUGO LEANDRO (GEO FIBER) | 2 | LOW |
| `AS48721` | Flyservers S.A. | 2 | HIGH |
| `AS24444` | Shandong Mobile Communication Company Limited | 1 | MEDIUM |
| `AS27747` | Telecentro S.A. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (107)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-3e76390a3317

| Field | Detail |
|---|---|
| **Source IP** | `181.212.174[.]164` |
| **First Seen** | 2026-08-15 08:55 |
| **Last Seen** | 2026-08-15 08:56 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 08:55:55` | `cowrie.session.connect` |
| `2026-08-15 08:55:56` | `cowrie.client.version` |
| `2026-08-15 08:55:56` | `cowrie.client.kex` |
| `2026-08-15 08:55:58` | `cowrie.login.success` |
| `2026-08-15 08:55:58` | `cowrie.direct-tcpip.request` |
| `2026-08-15 08:56:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.212.174[.]164` to AbuseIPDB if not already reported
- [ ] Block `181.212.174[.]164` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64eb94b9fee8

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-15 08:59 |
| **Last Seen** | 2026-08-15 08:59 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 08:59:49` | `cowrie.session.connect` |
| `2026-08-15 08:59:49` | `cowrie.client.version` |
| `2026-08-15 08:59:49` | `cowrie.client.kex` |
| `2026-08-15 08:59:50` | `cowrie.login.success` |
| `2026-08-15 08:59:51` | `cowrie.session.params` |
| `2026-08-15 08:59:51` | `cowrie.command.input` |
| `2026-08-15 08:59:51` | `cowrie.log.closed` |
| `2026-08-15 08:59:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-603647143dfc

| Field | Detail |
|---|---|
| **Source IP** | `178.132.144[.]161` |
| **First Seen** | 2026-08-15 09:07 |
| **Last Seen** | 2026-08-15 09:07 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 09:07:01` | `cowrie.session.connect` |
| `2026-08-15 09:07:02` | `cowrie.client.version` |
| `2026-08-15 09:07:02` | `cowrie.client.kex` |
| `2026-08-15 09:07:03` | `cowrie.login.success` |
| `2026-08-15 09:07:04` | `cowrie.direct-tcpip.request` |
| `2026-08-15 09:07:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.132.144[.]161` to AbuseIPDB if not already reported
- [ ] Block `178.132.144[.]161` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-166d890845ed

| Field | Detail |
|---|---|
| **Source IP** | `59.46.182[.]10` |
| **First Seen** | 2026-08-15 09:07 |
| **Last Seen** | 2026-08-15 09:07 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 09:07:11` | `cowrie.session.connect` |
| `2026-08-15 09:07:13` | `cowrie.client.version` |
| `2026-08-15 09:07:13` | `cowrie.client.kex` |
| `2026-08-15 09:07:17` | `cowrie.login.success` |
| `2026-08-15 09:07:19` | `cowrie.direct-tcpip.request` |
| `2026-08-15 09:07:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.46.182[.]10` to AbuseIPDB if not already reported
- [ ] Block `59.46.182[.]10` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a45fffcaa31a

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-15 09:07 |
| **Last Seen** | 2026-08-15 09:07 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 09:07:46` | `cowrie.session.connect` |
| `2026-08-15 09:07:46` | `cowrie.client.version` |
| `2026-08-15 09:07:46` | `cowrie.client.kex` |
| `2026-08-15 09:07:48` | `cowrie.login.success` |
| `2026-08-15 09:07:50` | `cowrie.session.params` |
| `2026-08-15 09:07:50` | `cowrie.command.input` |
| `2026-08-15 09:07:50` | `cowrie.command.input` |
| `2026-08-15 09:07:50` | `cowrie.command.input` |
| `2026-08-15 09:07:50` | `cowrie.command.input` |
| `2026-08-15 09:07:50` | `cowrie.command.input` |
| `2026-08-15 09:07:50` | `cowrie.command.success` |
| `2026-08-15 09:07:50` | `cowrie.command.input` |
| `2026-08-15 09:07:50` | `cowrie.command.input` |
| `2026-08-15 09:07:50` | `cowrie.command.input` |
| `2026-08-15 09:07:50` | `cowrie.command.input` |
| `2026-08-15 09:07:51` | `cowrie.log.closed` |
| `2026-08-15 09:07:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af6dc8941a03

| Field | Detail |
|---|---|
| **Source IP** | `45.142.193[.]164` |
| **First Seen** | 2026-08-15 09:09 |
| **Last Seen** | 2026-08-15 09:10 |
| **Session Duration** | 45s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 09:09:25` | `cowrie.session.connect` |
| `2026-08-15 09:09:30` | `cowrie.client.version` |
| `2026-08-15 09:09:30` | `cowrie.client.kex` |
| `2026-08-15 09:09:53` | `cowrie.login.success` |
| `2026-08-15 09:10:06` | `cowrie.session.params` |
| `2026-08-15 09:10:06` | `cowrie.command.input` |
| `2026-08-15 09:10:10` | `cowrie.log.closed` |
| `2026-08-15 09:10:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.142.193[.]164` to AbuseIPDB if not already reported
- [ ] Block `45.142.193[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-803f235c6a7e

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-15 09:09 |
| **Last Seen** | 2026-08-15 09:09 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 09:09:27` | `cowrie.session.connect` |
| `2026-08-15 09:09:27` | `cowrie.client.version` |
| `2026-08-15 09:09:27` | `cowrie.client.kex` |
| `2026-08-15 09:09:29` | `cowrie.login.success` |
| `2026-08-15 09:09:30` | `cowrie.session.params` |
| `2026-08-15 09:09:30` | `cowrie.command.input` |
| `2026-08-15 09:09:30` | `cowrie.command.input` |
| `2026-08-15 09:09:30` | `cowrie.command.input` |
| `2026-08-15 09:09:30` | `cowrie.command.input` |
| `2026-08-15 09:09:30` | `cowrie.command.input` |
| `2026-08-15 09:09:30` | `cowrie.command.success` |
| `2026-08-15 09:09:30` | `cowrie.command.input` |
| `2026-08-15 09:09:30` | `cowrie.command.input` |
| `2026-08-15 09:09:30` | `cowrie.command.input` |
| `2026-08-15 09:09:30` | `cowrie.command.input` |
| `2026-08-15 09:09:31` | `cowrie.log.closed` |
| `2026-08-15 09:09:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42b2988312ef

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-15 09:11 |
| **Last Seen** | 2026-08-15 09:11 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 09:11:12` | `cowrie.session.connect` |
| `2026-08-15 09:11:12` | `cowrie.client.version` |
| `2026-08-15 09:11:12` | `cowrie.client.kex` |
| `2026-08-15 09:11:14` | `cowrie.login.success` |
| `2026-08-15 09:11:15` | `cowrie.session.params` |
| `2026-08-15 09:11:15` | `cowrie.command.input` |
| `2026-08-15 09:11:15` | `cowrie.command.input` |
| `2026-08-15 09:11:15` | `cowrie.command.input` |
| `2026-08-15 09:11:15` | `cowrie.command.input` |
| `2026-08-15 09:11:15` | `cowrie.command.input` |
| `2026-08-15 09:11:15` | `cowrie.command.success` |
| `2026-08-15 09:11:15` | `cowrie.command.input` |
| `2026-08-15 09:11:15` | `cowrie.command.input` |
| `2026-08-15 09:11:15` | `cowrie.command.input` |
| `2026-08-15 09:11:15` | `cowrie.command.input` |
| `2026-08-15 09:11:16` | `cowrie.log.closed` |
| `2026-08-15 09:11:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-328d371c423c

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-15 09:12 |
| **Last Seen** | 2026-08-15 09:13 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 09:12:58` | `cowrie.session.connect` |
| `2026-08-15 09:12:59` | `cowrie.client.version` |
| `2026-08-15 09:12:59` | `cowrie.client.kex` |
| `2026-08-15 09:13:01` | `cowrie.login.success` |
| `2026-08-15 09:13:02` | `cowrie.session.params` |
| `2026-08-15 09:13:02` | `cowrie.command.input` |
| `2026-08-15 09:13:02` | `cowrie.command.input` |
| `2026-08-15 09:13:02` | `cowrie.command.input` |
| `2026-08-15 09:13:02` | `cowrie.command.input` |
| `2026-08-15 09:13:02` | `cowrie.command.input` |
| `2026-08-15 09:13:02` | `cowrie.command.success` |
| `2026-08-15 09:13:02` | `cowrie.command.input` |
| `2026-08-15 09:13:02` | `cowrie.command.input` |
| `2026-08-15 09:13:02` | `cowrie.command.input` |
| `2026-08-15 09:13:02` | `cowrie.command.input` |
| `2026-08-15 09:13:03` | `cowrie.log.closed` |
| `2026-08-15 09:13:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd2b42f6305d

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-15 09:14 |
| **Last Seen** | 2026-08-15 09:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 09:14:12` | `cowrie.session.connect` |
| `2026-08-15 09:14:12` | `cowrie.client.version` |
| `2026-08-15 09:14:12` | `cowrie.client.kex` |
| `2026-08-15 09:14:13` | `cowrie.login.success` |
| `2026-08-15 09:14:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c459829c978b

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-15 09:14 |
| **Last Seen** | 2026-08-15 09:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 09:14:12` | `cowrie.session.connect` |
| `2026-08-15 09:14:12` | `cowrie.client.version` |
| `2026-08-15 09:14:12` | `cowrie.client.kex` |
| `2026-08-15 09:14:13` | `cowrie.login.success` |
| `2026-08-15 09:14:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-065b9300f1ed

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-15 09:14 |
| **Last Seen** | 2026-08-15 09:14 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 09:14:41` | `cowrie.session.connect` |
| `2026-08-15 09:14:41` | `cowrie.client.version` |
| `2026-08-15 09:14:41` | `cowrie.client.kex` |
| `2026-08-15 09:14:43` | `cowrie.login.success` |
| `2026-08-15 09:14:45` | `cowrie.session.params` |
| `2026-08-15 09:14:45` | `cowrie.command.input` |
| `2026-08-15 09:14:45` | `cowrie.command.input` |
| `2026-08-15 09:14:45` | `cowrie.command.input` |
| `2026-08-15 09:14:45` | `cowrie.command.input` |
| `2026-08-15 09:14:45` | `cowrie.command.input` |
| `2026-08-15 09:14:45` | `cowrie.command.success` |
| `2026-08-15 09:14:45` | `cowrie.command.input` |
| `2026-08-15 09:14:45` | `cowrie.command.input` |
| `2026-08-15 09:14:45` | `cowrie.command.input` |
| `2026-08-15 09:14:45` | `cowrie.command.input` |
| `2026-08-15 09:14:45` | `cowrie.log.closed` |
| `2026-08-15 09:14:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec415a86aee2

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-15 09:18 |
| **Last Seen** | 2026-08-15 09:18 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 09:18:03` | `cowrie.session.connect` |
| `2026-08-15 09:18:03` | `cowrie.client.version` |
| `2026-08-15 09:18:03` | `cowrie.client.kex` |
| `2026-08-15 09:18:04` | `cowrie.login.success` |
| `2026-08-15 09:18:06` | `cowrie.session.params` |
| `2026-08-15 09:18:06` | `cowrie.command.input` |
| `2026-08-15 09:18:06` | `cowrie.command.input` |
| `2026-08-15 09:18:06` | `cowrie.command.input` |
| `2026-08-15 09:18:06` | `cowrie.command.input` |
| `2026-08-15 09:18:06` | `cowrie.command.input` |
| `2026-08-15 09:18:06` | `cowrie.command.success` |
| `2026-08-15 09:18:06` | `cowrie.command.input` |
| `2026-08-15 09:18:06` | `cowrie.command.input` |
| `2026-08-15 09:18:06` | `cowrie.command.input` |
| `2026-08-15 09:18:06` | `cowrie.command.input` |
| `2026-08-15 09:18:06` | `cowrie.log.closed` |
| `2026-08-15 09:18:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7531b2d26ed

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-15 09:19 |
| **Last Seen** | 2026-08-15 09:19 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 09:19:02` | `cowrie.session.connect` |
| `2026-08-15 09:19:02` | `cowrie.client.version` |
| `2026-08-15 09:19:02` | `cowrie.client.kex` |
| `2026-08-15 09:19:03` | `cowrie.login.success` |
| `2026-08-15 09:19:04` | `cowrie.session.params` |
| `2026-08-15 09:19:04` | `cowrie.command.input` |
| `2026-08-15 09:19:04` | `cowrie.log.closed` |
| `2026-08-15 09:19:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57041cf2ed49

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-15 09:19 |
| **Last Seen** | 2026-08-15 09:19 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 09:19:43` | `cowrie.session.connect` |
| `2026-08-15 09:19:43` | `cowrie.client.version` |
| `2026-08-15 09:19:43` | `cowrie.client.kex` |
| `2026-08-15 09:19:45` | `cowrie.login.success` |
| `2026-08-15 09:19:47` | `cowrie.session.params` |
| `2026-08-15 09:19:47` | `cowrie.command.input` |
| `2026-08-15 09:19:47` | `cowrie.command.input` |
| `2026-08-15 09:19:47` | `cowrie.command.input` |
| `2026-08-15 09:19:47` | `cowrie.command.input` |
| `2026-08-15 09:19:47` | `cowrie.command.input` |
| `2026-08-15 09:19:47` | `cowrie.command.success` |
| `2026-08-15 09:19:47` | `cowrie.command.input` |
| `2026-08-15 09:19:47` | `cowrie.command.input` |
| `2026-08-15 09:19:47` | `cowrie.command.input` |
| `2026-08-15 09:19:47` | `cowrie.command.input` |
| `2026-08-15 09:19:47` | `cowrie.log.closed` |
| `2026-08-15 09:19:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73f224d4aafe

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-15 09:21 |
| **Last Seen** | 2026-08-15 09:21 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 09:21:18` | `cowrie.session.connect` |
| `2026-08-15 09:21:19` | `cowrie.client.version` |
| `2026-08-15 09:21:19` | `cowrie.client.kex` |
| `2026-08-15 09:21:20` | `cowrie.login.success` |
| `2026-08-15 09:21:22` | `cowrie.session.params` |
| `2026-08-15 09:21:22` | `cowrie.command.input` |
| `2026-08-15 09:21:22` | `cowrie.command.input` |
| `2026-08-15 09:21:22` | `cowrie.command.input` |
| `2026-08-15 09:21:22` | `cowrie.command.input` |
| `2026-08-15 09:21:22` | `cowrie.command.input` |
| `2026-08-15 09:21:22` | `cowrie.command.success` |
| `2026-08-15 09:21:22` | `cowrie.command.input` |
| `2026-08-15 09:21:22` | `cowrie.command.input` |
| `2026-08-15 09:21:22` | `cowrie.command.input` |
| `2026-08-15 09:21:22` | `cowrie.command.input` |
| `2026-08-15 09:21:22` | `cowrie.log.closed` |
| `2026-08-15 09:21:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1d73b18dd58

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-15 09:22 |
| **Last Seen** | 2026-08-15 09:23 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 09:22:56` | `cowrie.session.connect` |
| `2026-08-15 09:22:57` | `cowrie.client.version` |
| `2026-08-15 09:22:57` | `cowrie.client.kex` |
| `2026-08-15 09:22:59` | `cowrie.login.success` |
| `2026-08-15 09:23:01` | `cowrie.session.params` |
| `2026-08-15 09:23:01` | `cowrie.command.input` |
| `2026-08-15 09:23:01` | `cowrie.command.input` |
| `2026-08-15 09:23:01` | `cowrie.command.input` |
| `2026-08-15 09:23:01` | `cowrie.command.input` |
| `2026-08-15 09:23:01` | `cowrie.command.input` |
| `2026-08-15 09:23:01` | `cowrie.command.success` |
| `2026-08-15 09:23:01` | `cowrie.command.input` |
| `2026-08-15 09:23:01` | `cowrie.command.input` |
| `2026-08-15 09:23:01` | `cowrie.command.input` |
| `2026-08-15 09:23:01` | `cowrie.command.input` |
| `2026-08-15 09:23:01` | `cowrie.log.closed` |
| `2026-08-15 09:23:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3fbaf8619174

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-15 09:24 |
| **Last Seen** | 2026-08-15 09:24 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 09:24:34` | `cowrie.session.connect` |
| `2026-08-15 09:24:35` | `cowrie.client.version` |
| `2026-08-15 09:24:35` | `cowrie.client.kex` |
| `2026-08-15 09:24:36` | `cowrie.login.success` |
| `2026-08-15 09:24:38` | `cowrie.session.params` |
| `2026-08-15 09:24:38` | `cowrie.command.input` |
| `2026-08-15 09:24:38` | `cowrie.command.input` |
| `2026-08-15 09:24:38` | `cowrie.command.input` |
| `2026-08-15 09:24:38` | `cowrie.command.input` |
| `2026-08-15 09:24:38` | `cowrie.command.input` |
| `2026-08-15 09:24:38` | `cowrie.command.success` |
| `2026-08-15 09:24:38` | `cowrie.command.input` |
| `2026-08-15 09:24:38` | `cowrie.command.input` |
| `2026-08-15 09:24:38` | `cowrie.command.input` |
| `2026-08-15 09:24:38` | `cowrie.command.input` |
| `2026-08-15 09:24:38` | `cowrie.log.closed` |
| `2026-08-15 09:24:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-256572d61c52

| Field | Detail |
|---|---|
| **Source IP** | `124.239.129[.]2` |
| **First Seen** | 2026-08-15 09:25 |
| **Last Seen** | 2026-08-15 09:25 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 09:25:07` | `cowrie.session.connect` |
| `2026-08-15 09:25:08` | `cowrie.client.version` |
| `2026-08-15 09:25:08` | `cowrie.client.kex` |
| `2026-08-15 09:25:11` | `cowrie.login.success` |
| `2026-08-15 09:25:12` | `cowrie.direct-tcpip.request` |
| `2026-08-15 09:25:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.239.129[.]2` to AbuseIPDB if not already reported
- [ ] Block `124.239.129[.]2` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-62f51bdf159e

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-15 09:26 |
| **Last Seen** | 2026-08-15 09:26 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 09:26:14` | `cowrie.session.connect` |
| `2026-08-15 09:26:14` | `cowrie.client.version` |
| `2026-08-15 09:26:14` | `cowrie.client.kex` |
| `2026-08-15 09:26:15` | `cowrie.login.success` |
| `2026-08-15 09:26:17` | `cowrie.session.params` |
| `2026-08-15 09:26:17` | `cowrie.command.input` |
| `2026-08-15 09:26:17` | `cowrie.command.input` |
| `2026-08-15 09:26:17` | `cowrie.command.input` |
| `2026-08-15 09:26:17` | `cowrie.command.input` |
| `2026-08-15 09:26:17` | `cowrie.command.input` |
| `2026-08-15 09:26:17` | `cowrie.command.success` |
| `2026-08-15 09:26:17` | `cowrie.command.input` |
| `2026-08-15 09:26:17` | `cowrie.command.input` |
| `2026-08-15 09:26:17` | `cowrie.command.input` |
| `2026-08-15 09:26:17` | `cowrie.command.input` |
| `2026-08-15 09:26:17` | `cowrie.log.closed` |
| `2026-08-15 09:26:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-208557e6c62a

| Field | Detail |
|---|---|
| **Source IP** | `148.227.91[.]88` |
| **First Seen** | 2026-08-15 09:27 |
| **Last Seen** | 2026-08-15 09:32 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 09:27:41` | `cowrie.session.connect` |
| `2026-08-15 09:27:42` | `cowrie.client.version` |
| `2026-08-15 09:27:42` | `cowrie.client.kex` |
| `2026-08-15 09:27:44` | `cowrie.login.success` |
| `2026-08-15 09:27:44` | `cowrie.direct-tcpip.request` |
| `2026-08-15 09:32:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `148.227.91[.]88` to AbuseIPDB if not already reported
- [ ] Block `148.227.91[.]88` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b272da1053a8

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-15 09:27 |
| **Last Seen** | 2026-08-15 09:27 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 09:27:50` | `cowrie.session.connect` |
| `2026-08-15 09:27:51` | `cowrie.client.version` |
| `2026-08-15 09:27:51` | `cowrie.client.kex` |
| `2026-08-15 09:27:52` | `cowrie.login.success` |
| `2026-08-15 09:27:54` | `cowrie.session.params` |
| `2026-08-15 09:27:54` | `cowrie.command.input` |
| `2026-08-15 09:27:54` | `cowrie.command.input` |
| `2026-08-15 09:27:54` | `cowrie.command.input` |
| `2026-08-15 09:27:54` | `cowrie.command.input` |
| `2026-08-15 09:27:54` | `cowrie.command.input` |
| `2026-08-15 09:27:54` | `cowrie.command.success` |
| `2026-08-15 09:27:54` | `cowrie.command.input` |
| `2026-08-15 09:27:54` | `cowrie.command.input` |
| `2026-08-15 09:27:54` | `cowrie.command.input` |
| `2026-08-15 09:27:54` | `cowrie.command.input` |
| `2026-08-15 09:27:54` | `cowrie.log.closed` |
| `2026-08-15 09:27:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-567a68b5c48f

| Field | Detail |
|---|---|
| **Source IP** | `178.178.222[.]58` |
| **First Seen** | 2026-08-15 09:27 |
| **Last Seen** | 2026-08-15 09:28 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 09:27:54` | `cowrie.session.connect` |
| `2026-08-15 09:27:55` | `cowrie.client.version` |
| `2026-08-15 09:27:55` | `cowrie.client.kex` |
| `2026-08-15 09:27:57` | `cowrie.login.success` |
| `2026-08-15 09:27:57` | `cowrie.direct-tcpip.request` |
| `2026-08-15 09:28:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.222[.]58` to AbuseIPDB if not already reported
- [ ] Block `178.178.222[.]58` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ec5983fcac0

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-15 09:29 |
| **Last Seen** | 2026-08-15 09:29 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 09:29:29` | `cowrie.session.connect` |
| `2026-08-15 09:29:29` | `cowrie.client.version` |
| `2026-08-15 09:29:29` | `cowrie.client.kex` |
| `2026-08-15 09:29:31` | `cowrie.login.success` |
| `2026-08-15 09:29:32` | `cowrie.session.params` |
| `2026-08-15 09:29:32` | `cowrie.command.input` |
| `2026-08-15 09:29:32` | `cowrie.command.input` |
| `2026-08-15 09:29:32` | `cowrie.command.input` |
| `2026-08-15 09:29:32` | `cowrie.command.input` |
| `2026-08-15 09:29:32` | `cowrie.command.input` |
| `2026-08-15 09:29:32` | `cowrie.command.success` |
| `2026-08-15 09:29:32` | `cowrie.command.input` |
| `2026-08-15 09:29:32` | `cowrie.command.input` |
| `2026-08-15 09:29:32` | `cowrie.command.input` |
| `2026-08-15 09:29:32` | `cowrie.command.input` |
| `2026-08-15 09:29:33` | `cowrie.log.closed` |
| `2026-08-15 09:29:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a569762ff2fe

| Field | Detail |
|---|---|
| **Source IP** | `78.187.9[.]111` |
| **First Seen** | 2026-08-15 09:29 |
| **Last Seen** | 2026-08-15 09:29 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 09:29:32` | `cowrie.session.connect` |
| `2026-08-15 09:29:33` | `cowrie.client.version` |
| `2026-08-15 09:29:33` | `cowrie.client.kex` |
| `2026-08-15 09:29:34` | `cowrie.login.success` |
| `2026-08-15 09:29:34` | `cowrie.direct-tcpip.request` |
| `2026-08-15 09:29:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `78.187.9[.]111` to AbuseIPDB if not already reported
- [ ] Block `78.187.9[.]111` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb01da7c78a0

| Field | Detail |
|---|---|
| **Source IP** | `85.19.195[.]12` |
| **First Seen** | 2026-08-15 09:29 |
| **Last Seen** | 2026-08-15 09:29 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 09:29:39` | `cowrie.session.connect` |
| `2026-08-15 09:29:40` | `cowrie.client.version` |
| `2026-08-15 09:29:40` | `cowrie.client.kex` |
| `2026-08-15 09:29:41` | `cowrie.login.success` |
| `2026-08-15 09:29:41` | `cowrie.direct-tcpip.request` |
| `2026-08-15 09:29:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.19.195[.]12` to AbuseIPDB if not already reported
- [ ] Block `85.19.195[.]12` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33575b2d833a

| Field | Detail |
|---|---|
| **Source IP** | `171.217.70[.]151` |
| **First Seen** | 2026-08-15 09:29 |
| **Last Seen** | 2026-08-15 09:29 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 09:29:46` | `cowrie.session.connect` |
| `2026-08-15 09:29:46` | `cowrie.client.version` |
| `2026-08-15 09:29:46` | `cowrie.client.kex` |
| `2026-08-15 09:29:49` | `cowrie.login.success` |
| `2026-08-15 09:29:50` | `cowrie.direct-tcpip.request` |
| `2026-08-15 09:29:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.217.70[.]151` to AbuseIPDB if not already reported
- [ ] Block `171.217.70[.]151` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5546749cafd1

| Field | Detail |
|---|---|
| **Source IP** | `182.76.36[.]62` |
| **First Seen** | 2026-08-15 09:29 |
| **Last Seen** | 2026-08-15 09:30 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 09:29:56` | `cowrie.session.connect` |
| `2026-08-15 09:29:57` | `cowrie.client.version` |
| `2026-08-15 09:29:57` | `cowrie.client.kex` |
| `2026-08-15 09:29:59` | `cowrie.login.success` |
| `2026-08-15 09:30:00` | `cowrie.direct-tcpip.request` |
| `2026-08-15 09:30:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.76.36[.]62` to AbuseIPDB if not already reported
- [ ] Block `182.76.36[.]62` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-69448ccc2e57

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-15 09:31 |
| **Last Seen** | 2026-08-15 09:31 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 09:31:10` | `cowrie.session.connect` |
| `2026-08-15 09:31:10` | `cowrie.client.version` |
| `2026-08-15 09:31:10` | `cowrie.client.kex` |
| `2026-08-15 09:31:12` | `cowrie.login.success` |
| `2026-08-15 09:31:13` | `cowrie.session.params` |
| `2026-08-15 09:31:13` | `cowrie.command.input` |
| `2026-08-15 09:31:13` | `cowrie.command.input` |
| `2026-08-15 09:31:13` | `cowrie.command.input` |
| `2026-08-15 09:31:13` | `cowrie.command.input` |
| `2026-08-15 09:31:13` | `cowrie.command.input` |
| `2026-08-15 09:31:13` | `cowrie.command.success` |
| `2026-08-15 09:31:13` | `cowrie.command.input` |
| `2026-08-15 09:31:13` | `cowrie.command.input` |
| `2026-08-15 09:31:13` | `cowrie.command.input` |
| `2026-08-15 09:31:13` | `cowrie.command.input` |
| `2026-08-15 09:31:13` | `cowrie.log.closed` |
| `2026-08-15 09:31:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5da4eeb6a09

| Field | Detail |
|---|---|
| **Source IP** | `45.142.193[.]164` |
| **First Seen** | 2026-08-15 09:32 |
| **Last Seen** | 2026-08-15 09:33 |
| **Session Duration** | 46s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 09:32:16` | `cowrie.session.connect` |
| `2026-08-15 09:32:23` | `cowrie.client.version` |
| `2026-08-15 09:32:23` | `cowrie.client.kex` |
| `2026-08-15 09:32:45` | `cowrie.login.success` |
| `2026-08-15 09:32:57` | `cowrie.session.params` |
| `2026-08-15 09:32:57` | `cowrie.command.input` |
| `2026-08-15 09:33:03` | `cowrie.log.closed` |
| `2026-08-15 09:33:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.142.193[.]164` to AbuseIPDB if not already reported
- [ ] Block `45.142.193[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74f53fcf4eee

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-15 09:32 |
| **Last Seen** | 2026-08-15 09:32 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 09:32:50` | `cowrie.session.connect` |
| `2026-08-15 09:32:50` | `cowrie.client.version` |
| `2026-08-15 09:32:50` | `cowrie.client.kex` |
| `2026-08-15 09:32:52` | `cowrie.login.success` |
| `2026-08-15 09:32:53` | `cowrie.session.params` |
| `2026-08-15 09:32:53` | `cowrie.command.input` |
| `2026-08-15 09:32:53` | `cowrie.command.input` |
| `2026-08-15 09:32:53` | `cowrie.command.input` |
| `2026-08-15 09:32:53` | `cowrie.command.input` |
| `2026-08-15 09:32:53` | `cowrie.command.input` |
| `2026-08-15 09:32:53` | `cowrie.command.success` |
| `2026-08-15 09:32:53` | `cowrie.command.input` |
| `2026-08-15 09:32:53` | `cowrie.command.input` |
| `2026-08-15 09:32:53` | `cowrie.command.input` |
| `2026-08-15 09:32:53` | `cowrie.command.input` |
| `2026-08-15 09:32:53` | `cowrie.log.closed` |
| `2026-08-15 09:32:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4ad99a3800f

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-15 09:34 |
| **Last Seen** | 2026-08-15 09:34 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 09:34:21` | `cowrie.session.connect` |
| `2026-08-15 09:34:21` | `cowrie.client.version` |
| `2026-08-15 09:34:21` | `cowrie.client.kex` |
| `2026-08-15 09:34:23` | `cowrie.login.success` |
| `2026-08-15 09:34:24` | `cowrie.session.params` |
| `2026-08-15 09:34:24` | `cowrie.command.input` |
| `2026-08-15 09:34:24` | `cowrie.command.input` |
| `2026-08-15 09:34:24` | `cowrie.command.input` |
| `2026-08-15 09:34:24` | `cowrie.command.input` |
| `2026-08-15 09:34:24` | `cowrie.command.input` |
| `2026-08-15 09:34:24` | `cowrie.command.success` |
| `2026-08-15 09:34:24` | `cowrie.command.input` |
| `2026-08-15 09:34:24` | `cowrie.command.input` |
| `2026-08-15 09:34:24` | `cowrie.command.input` |
| `2026-08-15 09:34:24` | `cowrie.command.input` |
| `2026-08-15 09:34:24` | `cowrie.log.closed` |
| `2026-08-15 09:34:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0709f4dc18c

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-15 09:35 |
| **Last Seen** | 2026-08-15 09:35 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 09:35:55` | `cowrie.session.connect` |
| `2026-08-15 09:35:56` | `cowrie.client.version` |
| `2026-08-15 09:35:56` | `cowrie.client.kex` |
| `2026-08-15 09:35:57` | `cowrie.login.success` |
| `2026-08-15 09:35:58` | `cowrie.session.params` |
| `2026-08-15 09:35:58` | `cowrie.command.input` |
| `2026-08-15 09:35:58` | `cowrie.command.input` |
| `2026-08-15 09:35:58` | `cowrie.command.input` |
| `2026-08-15 09:35:58` | `cowrie.command.input` |
| `2026-08-15 09:35:58` | `cowrie.command.input` |
| `2026-08-15 09:35:58` | `cowrie.command.success` |
| `2026-08-15 09:35:58` | `cowrie.command.input` |
| `2026-08-15 09:35:58` | `cowrie.command.input` |
| `2026-08-15 09:35:58` | `cowrie.command.input` |
| `2026-08-15 09:35:58` | `cowrie.command.input` |
| `2026-08-15 09:35:58` | `cowrie.log.closed` |
| `2026-08-15 09:35:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84cdd393c387

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-15 09:37 |
| **Last Seen** | 2026-08-15 09:37 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 09:37:31` | `cowrie.session.connect` |
| `2026-08-15 09:37:31` | `cowrie.client.version` |
| `2026-08-15 09:37:31` | `cowrie.client.kex` |
| `2026-08-15 09:37:32` | `cowrie.login.success` |
| `2026-08-15 09:37:33` | `cowrie.session.params` |
| `2026-08-15 09:37:33` | `cowrie.command.input` |
| `2026-08-15 09:37:33` | `cowrie.command.input` |
| `2026-08-15 09:37:33` | `cowrie.command.input` |
| `2026-08-15 09:37:33` | `cowrie.command.input` |
| `2026-08-15 09:37:33` | `cowrie.command.input` |
| `2026-08-15 09:37:33` | `cowrie.command.success` |
| `2026-08-15 09:37:33` | `cowrie.command.input` |
| `2026-08-15 09:37:33` | `cowrie.command.input` |
| `2026-08-15 09:37:33` | `cowrie.command.input` |
| `2026-08-15 09:37:33` | `cowrie.command.input` |
| `2026-08-15 09:37:34` | `cowrie.log.closed` |
| `2026-08-15 09:37:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-641d653bc292

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-15 09:38 |
| **Last Seen** | 2026-08-15 09:38 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 09:38:15` | `cowrie.session.connect` |
| `2026-08-15 09:38:15` | `cowrie.client.version` |
| `2026-08-15 09:38:15` | `cowrie.client.kex` |
| `2026-08-15 09:38:16` | `cowrie.login.success` |
| `2026-08-15 09:38:17` | `cowrie.session.params` |
| `2026-08-15 09:38:17` | `cowrie.command.input` |
| `2026-08-15 09:38:17` | `cowrie.log.closed` |
| `2026-08-15 09:38:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c47c568adefb

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-15 09:39 |
| **Last Seen** | 2026-08-15 09:39 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 09:39:06` | `cowrie.session.connect` |
| `2026-08-15 09:39:06` | `cowrie.client.version` |
| `2026-08-15 09:39:06` | `cowrie.client.kex` |
| `2026-08-15 09:39:08` | `cowrie.login.success` |
| `2026-08-15 09:39:10` | `cowrie.session.params` |
| `2026-08-15 09:39:10` | `cowrie.command.input` |
| `2026-08-15 09:39:10` | `cowrie.command.input` |
| `2026-08-15 09:39:10` | `cowrie.command.input` |
| `2026-08-15 09:39:10` | `cowrie.command.input` |
| `2026-08-15 09:39:10` | `cowrie.command.input` |
| `2026-08-15 09:39:10` | `cowrie.command.success` |
| `2026-08-15 09:39:10` | `cowrie.command.input` |
| `2026-08-15 09:39:10` | `cowrie.command.input` |
| `2026-08-15 09:39:10` | `cowrie.command.input` |
| `2026-08-15 09:39:10` | `cowrie.command.input` |
| `2026-08-15 09:39:10` | `cowrie.log.closed` |
| `2026-08-15 09:39:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c00135b9113

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-15 09:40 |
| **Last Seen** | 2026-08-15 09:40 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 09:40:39` | `cowrie.session.connect` |
| `2026-08-15 09:40:39` | `cowrie.client.version` |
| `2026-08-15 09:40:39` | `cowrie.client.kex` |
| `2026-08-15 09:40:41` | `cowrie.login.success` |
| `2026-08-15 09:40:42` | `cowrie.session.params` |
| `2026-08-15 09:40:42` | `cowrie.command.input` |
| `2026-08-15 09:40:42` | `cowrie.command.input` |
| `2026-08-15 09:40:42` | `cowrie.command.input` |
| `2026-08-15 09:40:42` | `cowrie.command.input` |
| `2026-08-15 09:40:42` | `cowrie.command.input` |
| `2026-08-15 09:40:42` | `cowrie.command.success` |
| `2026-08-15 09:40:42` | `cowrie.command.input` |
| `2026-08-15 09:40:42` | `cowrie.command.input` |
| `2026-08-15 09:40:42` | `cowrie.command.input` |
| `2026-08-15 09:40:42` | `cowrie.command.input` |
| `2026-08-15 09:40:43` | `cowrie.log.closed` |
| `2026-08-15 09:40:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-027b532eaf92

| Field | Detail |
|---|---|
| **Source IP** | `196.188.93[.]169` |
| **First Seen** | 2026-08-15 09:41 |
| **Last Seen** | 2026-08-15 09:41 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 09:41:18` | `cowrie.session.connect` |
| `2026-08-15 09:41:18` | `cowrie.client.version` |
| `2026-08-15 09:41:18` | `cowrie.client.kex` |
| `2026-08-15 09:41:20` | `cowrie.login.success` |
| `2026-08-15 09:41:20` | `cowrie.direct-tcpip.request` |
| `2026-08-15 09:41:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.188.93[.]169` to AbuseIPDB if not already reported
- [ ] Block `196.188.93[.]169` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e08a4c6311d

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-15 09:42 |
| **Last Seen** | 2026-08-15 09:42 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 09:42:09` | `cowrie.session.connect` |
| `2026-08-15 09:42:09` | `cowrie.client.version` |
| `2026-08-15 09:42:09` | `cowrie.client.kex` |
| `2026-08-15 09:42:10` | `cowrie.login.success` |
| `2026-08-15 09:42:12` | `cowrie.session.params` |
| `2026-08-15 09:42:12` | `cowrie.command.input` |
| `2026-08-15 09:42:12` | `cowrie.command.input` |
| `2026-08-15 09:42:12` | `cowrie.command.input` |
| `2026-08-15 09:42:12` | `cowrie.command.input` |
| `2026-08-15 09:42:12` | `cowrie.command.input` |
| `2026-08-15 09:42:12` | `cowrie.command.success` |
| `2026-08-15 09:42:12` | `cowrie.command.input` |
| `2026-08-15 09:42:12` | `cowrie.command.input` |
| `2026-08-15 09:42:12` | `cowrie.command.input` |
| `2026-08-15 09:42:12` | `cowrie.command.input` |
| `2026-08-15 09:42:13` | `cowrie.log.closed` |
| `2026-08-15 09:42:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a72832b473f

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-15 09:43 |
| **Last Seen** | 2026-08-15 09:43 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 09:43:41` | `cowrie.session.connect` |
| `2026-08-15 09:43:42` | `cowrie.client.version` |
| `2026-08-15 09:43:42` | `cowrie.client.kex` |
| `2026-08-15 09:43:44` | `cowrie.login.success` |
| `2026-08-15 09:43:45` | `cowrie.session.params` |
| `2026-08-15 09:43:45` | `cowrie.command.input` |
| `2026-08-15 09:43:45` | `cowrie.command.input` |
| `2026-08-15 09:43:45` | `cowrie.command.input` |
| `2026-08-15 09:43:45` | `cowrie.command.input` |
| `2026-08-15 09:43:45` | `cowrie.command.input` |
| `2026-08-15 09:43:45` | `cowrie.command.success` |
| `2026-08-15 09:43:45` | `cowrie.command.input` |
| `2026-08-15 09:43:45` | `cowrie.command.input` |
| `2026-08-15 09:43:45` | `cowrie.command.input` |
| `2026-08-15 09:43:45` | `cowrie.command.input` |
| `2026-08-15 09:43:45` | `cowrie.log.closed` |
| `2026-08-15 09:43:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b3c4aeb9306

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-15 09:45 |
| **Last Seen** | 2026-08-15 09:45 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 09:45:13` | `cowrie.session.connect` |
| `2026-08-15 09:45:13` | `cowrie.client.version` |
| `2026-08-15 09:45:13` | `cowrie.client.kex` |
| `2026-08-15 09:45:15` | `cowrie.login.success` |
| `2026-08-15 09:45:16` | `cowrie.session.params` |
| `2026-08-15 09:45:16` | `cowrie.command.input` |
| `2026-08-15 09:45:16` | `cowrie.command.input` |
| `2026-08-15 09:45:16` | `cowrie.command.input` |
| `2026-08-15 09:45:16` | `cowrie.command.input` |
| `2026-08-15 09:45:16` | `cowrie.command.input` |
| `2026-08-15 09:45:16` | `cowrie.command.success` |
| `2026-08-15 09:45:16` | `cowrie.command.input` |
| `2026-08-15 09:45:16` | `cowrie.command.input` |
| `2026-08-15 09:45:16` | `cowrie.command.input` |
| `2026-08-15 09:45:16` | `cowrie.command.input` |
| `2026-08-15 09:45:17` | `cowrie.log.closed` |
| `2026-08-15 09:45:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72a942bbe6a1

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-15 09:46 |
| **Last Seen** | 2026-08-15 09:46 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 09:46:44` | `cowrie.session.connect` |
| `2026-08-15 09:46:44` | `cowrie.client.version` |
| `2026-08-15 09:46:44` | `cowrie.client.kex` |
| `2026-08-15 09:46:45` | `cowrie.login.success` |
| `2026-08-15 09:46:47` | `cowrie.session.params` |
| `2026-08-15 09:46:47` | `cowrie.command.input` |
| `2026-08-15 09:46:47` | `cowrie.command.input` |
| `2026-08-15 09:46:47` | `cowrie.command.input` |
| `2026-08-15 09:46:47` | `cowrie.command.input` |
| `2026-08-15 09:46:47` | `cowrie.command.input` |
| `2026-08-15 09:46:47` | `cowrie.command.success` |
| `2026-08-15 09:46:47` | `cowrie.command.input` |
| `2026-08-15 09:46:47` | `cowrie.command.input` |
| `2026-08-15 09:46:47` | `cowrie.command.input` |
| `2026-08-15 09:46:47` | `cowrie.command.input` |
| `2026-08-15 09:46:47` | `cowrie.log.closed` |
| `2026-08-15 09:46:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52b605dc0724

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-15 09:48 |
| **Last Seen** | 2026-08-15 09:48 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 09:48:15` | `cowrie.session.connect` |
| `2026-08-15 09:48:15` | `cowrie.client.version` |
| `2026-08-15 09:48:15` | `cowrie.client.kex` |
| `2026-08-15 09:48:17` | `cowrie.login.success` |
| `2026-08-15 09:48:18` | `cowrie.session.params` |
| `2026-08-15 09:48:18` | `cowrie.command.input` |
| `2026-08-15 09:48:18` | `cowrie.command.input` |
| `2026-08-15 09:48:18` | `cowrie.command.input` |
| `2026-08-15 09:48:18` | `cowrie.command.input` |
| `2026-08-15 09:48:18` | `cowrie.command.input` |
| `2026-08-15 09:48:18` | `cowrie.command.success` |
| `2026-08-15 09:48:18` | `cowrie.command.input` |
| `2026-08-15 09:48:18` | `cowrie.command.input` |
| `2026-08-15 09:48:18` | `cowrie.command.input` |
| `2026-08-15 09:48:18` | `cowrie.command.input` |
| `2026-08-15 09:48:18` | `cowrie.log.closed` |
| `2026-08-15 09:48:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-330cf8493a1d

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-15 09:51 |
| **Last Seen** | 2026-08-15 09:51 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 09:51:26` | `cowrie.session.connect` |
| `2026-08-15 09:51:26` | `cowrie.client.version` |
| `2026-08-15 09:51:26` | `cowrie.client.kex` |
| `2026-08-15 09:51:27` | `cowrie.login.success` |
| `2026-08-15 09:51:28` | `cowrie.session.params` |
| `2026-08-15 09:51:28` | `cowrie.command.input` |
| `2026-08-15 09:51:28` | `cowrie.command.input` |
| `2026-08-15 09:51:28` | `cowrie.command.input` |
| `2026-08-15 09:51:28` | `cowrie.command.input` |
| `2026-08-15 09:51:28` | `cowrie.command.input` |
| `2026-08-15 09:51:28` | `cowrie.command.success` |
| `2026-08-15 09:51:28` | `cowrie.command.input` |
| `2026-08-15 09:51:28` | `cowrie.command.input` |
| `2026-08-15 09:51:28` | `cowrie.command.input` |
| `2026-08-15 09:51:28` | `cowrie.command.input` |
| `2026-08-15 09:51:29` | `cowrie.log.closed` |
| `2026-08-15 09:51:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-428f0befec49

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-15 09:53 |
| **Last Seen** | 2026-08-15 09:53 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 09:53:03` | `cowrie.session.connect` |
| `2026-08-15 09:53:03` | `cowrie.client.version` |
| `2026-08-15 09:53:03` | `cowrie.client.kex` |
| `2026-08-15 09:53:04` | `cowrie.login.success` |
| `2026-08-15 09:53:05` | `cowrie.session.params` |
| `2026-08-15 09:53:05` | `cowrie.command.input` |
| `2026-08-15 09:53:05` | `cowrie.command.input` |
| `2026-08-15 09:53:05` | `cowrie.command.input` |
| `2026-08-15 09:53:05` | `cowrie.command.input` |
| `2026-08-15 09:53:05` | `cowrie.command.input` |
| `2026-08-15 09:53:05` | `cowrie.command.success` |
| `2026-08-15 09:53:05` | `cowrie.command.input` |
| `2026-08-15 09:53:05` | `cowrie.command.input` |
| `2026-08-15 09:53:05` | `cowrie.command.input` |
| `2026-08-15 09:53:05` | `cowrie.command.input` |
| `2026-08-15 09:53:05` | `cowrie.log.closed` |
| `2026-08-15 09:53:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dde791ff0b5e

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-15 09:54 |
| **Last Seen** | 2026-08-15 09:54 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 09:54:48` | `cowrie.session.connect` |
| `2026-08-15 09:54:48` | `cowrie.client.version` |
| `2026-08-15 09:54:48` | `cowrie.client.kex` |
| `2026-08-15 09:54:48` | `cowrie.login.success` |
| `2026-08-15 09:54:49` | `cowrie.session.params` |
| `2026-08-15 09:54:49` | `cowrie.command.input` |
| `2026-08-15 09:54:49` | `cowrie.command.input` |
| `2026-08-15 09:54:49` | `cowrie.command.input` |
| `2026-08-15 09:54:49` | `cowrie.command.input` |
| `2026-08-15 09:54:49` | `cowrie.command.input` |
| `2026-08-15 09:54:49` | `cowrie.command.success` |
| `2026-08-15 09:54:49` | `cowrie.command.input` |
| `2026-08-15 09:54:49` | `cowrie.command.input` |
| `2026-08-15 09:54:49` | `cowrie.command.input` |
| `2026-08-15 09:54:49` | `cowrie.command.input` |
| `2026-08-15 09:54:50` | `cowrie.log.closed` |
| `2026-08-15 09:54:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a109e456e55e

| Field | Detail |
|---|---|
| **Source IP** | `45.142.193[.]164` |
| **First Seen** | 2026-08-15 09:55 |
| **Last Seen** | 2026-08-15 09:55 |
| **Session Duration** | 46s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 09:55:07` | `cowrie.session.connect` |
| `2026-08-15 09:55:14` | `cowrie.client.version` |
| `2026-08-15 09:55:14` | `cowrie.client.kex` |
| `2026-08-15 09:55:37` | `cowrie.login.success` |
| `2026-08-15 09:55:47` | `cowrie.session.params` |
| `2026-08-15 09:55:47` | `cowrie.command.input` |
| `2026-08-15 09:55:54` | `cowrie.log.closed` |
| `2026-08-15 09:55:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.142.193[.]164` to AbuseIPDB if not already reported
- [ ] Block `45.142.193[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-22e21f9d6560

| Field | Detail |
|---|---|
| **Source IP** | `182.53.52[.]68` |
| **First Seen** | 2026-08-15 09:56 |
| **Last Seen** | 2026-08-15 09:56 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 09:56:08` | `cowrie.session.connect` |
| `2026-08-15 09:56:09` | `cowrie.client.version` |
| `2026-08-15 09:56:09` | `cowrie.client.kex` |
| `2026-08-15 09:56:11` | `cowrie.login.success` |
| `2026-08-15 09:56:12` | `cowrie.direct-tcpip.request` |
| `2026-08-15 09:56:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.53.52[.]68` to AbuseIPDB if not already reported
- [ ] Block `182.53.52[.]68` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd30df6b858d

| Field | Detail |
|---|---|
| **Source IP** | `103.93.37[.]178` |
| **First Seen** | 2026-08-15 09:56 |
| **Last Seen** | 2026-08-15 09:56 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 09:56:17` | `cowrie.session.connect` |
| `2026-08-15 09:56:18` | `cowrie.client.version` |
| `2026-08-15 09:56:18` | `cowrie.client.kex` |
| `2026-08-15 09:56:20` | `cowrie.login.success` |
| `2026-08-15 09:56:21` | `cowrie.direct-tcpip.request` |
| `2026-08-15 09:56:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.93.37[.]178` to AbuseIPDB if not already reported
- [ ] Block `103.93.37[.]178` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b56619290e5e

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-15 09:56 |
| **Last Seen** | 2026-08-15 09:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 09:56:47` | `cowrie.session.connect` |
| `2026-08-15 09:56:47` | `cowrie.client.version` |
| `2026-08-15 09:56:47` | `cowrie.client.kex` |
| `2026-08-15 09:56:47` | `cowrie.login.success` |
| `2026-08-15 09:56:48` | `cowrie.session.params` |
| `2026-08-15 09:56:48` | `cowrie.command.input` |
| `2026-08-15 09:56:48` | `cowrie.command.input` |
| `2026-08-15 09:56:48` | `cowrie.command.input` |
| `2026-08-15 09:56:48` | `cowrie.command.input` |
| `2026-08-15 09:56:48` | `cowrie.command.input` |
| `2026-08-15 09:56:48` | `cowrie.command.success` |
| `2026-08-15 09:56:48` | `cowrie.command.input` |
| `2026-08-15 09:56:48` | `cowrie.command.input` |
| `2026-08-15 09:56:48` | `cowrie.command.input` |
| `2026-08-15 09:56:48` | `cowrie.command.input` |
| `2026-08-15 09:56:48` | `cowrie.log.closed` |
| `2026-08-15 09:56:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb4b2c0df4e7

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-15 09:57 |
| **Last Seen** | 2026-08-15 09:57 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 09:57:28` | `cowrie.session.connect` |
| `2026-08-15 09:57:28` | `cowrie.client.version` |
| `2026-08-15 09:57:28` | `cowrie.client.kex` |
| `2026-08-15 09:57:29` | `cowrie.login.success` |
| `2026-08-15 09:57:30` | `cowrie.session.params` |
| `2026-08-15 09:57:30` | `cowrie.command.input` |
| `2026-08-15 09:57:30` | `cowrie.log.closed` |
| `2026-08-15 09:57:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0e2dded9ab9

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-15 09:58 |
| **Last Seen** | 2026-08-15 09:58 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 09:58:52` | `cowrie.session.connect` |
| `2026-08-15 09:58:52` | `cowrie.client.version` |
| `2026-08-15 09:58:52` | `cowrie.client.kex` |
| `2026-08-15 09:58:53` | `cowrie.login.success` |
| `2026-08-15 09:58:54` | `cowrie.session.params` |
| `2026-08-15 09:58:54` | `cowrie.command.input` |
| `2026-08-15 09:58:54` | `cowrie.command.input` |
| `2026-08-15 09:58:54` | `cowrie.command.input` |
| `2026-08-15 09:58:54` | `cowrie.command.input` |
| `2026-08-15 09:58:54` | `cowrie.command.input` |
| `2026-08-15 09:58:54` | `cowrie.command.success` |
| `2026-08-15 09:58:54` | `cowrie.command.input` |
| `2026-08-15 09:58:54` | `cowrie.command.input` |
| `2026-08-15 09:58:54` | `cowrie.command.input` |
| `2026-08-15 09:58:54` | `cowrie.command.input` |
| `2026-08-15 09:58:54` | `cowrie.log.closed` |
| `2026-08-15 09:58:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e7d0b23efbd

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-15 10:00 |
| **Last Seen** | 2026-08-15 10:00 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 10:00:18` | `cowrie.session.connect` |
| `2026-08-15 10:00:19` | `cowrie.client.version` |
| `2026-08-15 10:00:19` | `cowrie.client.kex` |
| `2026-08-15 10:00:20` | `cowrie.login.success` |
| `2026-08-15 10:00:22` | `cowrie.session.params` |
| `2026-08-15 10:00:22` | `cowrie.command.input` |
| `2026-08-15 10:00:22` | `cowrie.command.input` |
| `2026-08-15 10:00:22` | `cowrie.command.input` |
| `2026-08-15 10:00:22` | `cowrie.command.input` |
| `2026-08-15 10:00:22` | `cowrie.command.input` |
| `2026-08-15 10:00:22` | `cowrie.command.success` |
| `2026-08-15 10:00:22` | `cowrie.command.input` |
| `2026-08-15 10:00:22` | `cowrie.command.input` |
| `2026-08-15 10:00:22` | `cowrie.command.input` |
| `2026-08-15 10:00:22` | `cowrie.command.input` |
| `2026-08-15 10:00:23` | `cowrie.log.closed` |
| `2026-08-15 10:00:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4038d4b8619d

| Field | Detail |
|---|---|
| **Source IP** | `67.85.146[.]216` |
| **First Seen** | 2026-08-15 10:01 |
| **Last Seen** | 2026-08-15 10:01 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 10:01:26` | `cowrie.session.connect` |
| `2026-08-15 10:01:27` | `cowrie.client.version` |
| `2026-08-15 10:01:27` | `cowrie.client.kex` |
| `2026-08-15 10:01:28` | `cowrie.login.success` |
| `2026-08-15 10:01:29` | `cowrie.direct-tcpip.request` |
| `2026-08-15 10:01:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `67.85.146[.]216` to AbuseIPDB if not already reported
- [ ] Block `67.85.146[.]216` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef7d1750230e

| Field | Detail |
|---|---|
| **Source IP** | `27.107.102[.]154` |
| **First Seen** | 2026-08-15 10:01 |
| **Last Seen** | 2026-08-15 10:01 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 10:01:34` | `cowrie.session.connect` |
| `2026-08-15 10:01:35` | `cowrie.client.version` |
| `2026-08-15 10:01:35` | `cowrie.client.kex` |
| `2026-08-15 10:01:36` | `cowrie.login.success` |
| `2026-08-15 10:01:37` | `cowrie.direct-tcpip.request` |
| `2026-08-15 10:01:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.107.102[.]154` to AbuseIPDB if not already reported
- [ ] Block `27.107.102[.]154` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6668a4d96ab

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-15 10:01 |
| **Last Seen** | 2026-08-15 10:01 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 10:01:46` | `cowrie.session.connect` |
| `2026-08-15 10:01:46` | `cowrie.client.version` |
| `2026-08-15 10:01:46` | `cowrie.client.kex` |
| `2026-08-15 10:01:48` | `cowrie.login.success` |
| `2026-08-15 10:01:49` | `cowrie.session.params` |
| `2026-08-15 10:01:49` | `cowrie.command.input` |
| `2026-08-15 10:01:49` | `cowrie.command.input` |
| `2026-08-15 10:01:49` | `cowrie.command.input` |
| `2026-08-15 10:01:49` | `cowrie.command.input` |
| `2026-08-15 10:01:49` | `cowrie.command.input` |
| `2026-08-15 10:01:49` | `cowrie.command.success` |
| `2026-08-15 10:01:49` | `cowrie.command.input` |
| `2026-08-15 10:01:49` | `cowrie.command.input` |
| `2026-08-15 10:01:49` | `cowrie.command.input` |
| `2026-08-15 10:01:49` | `cowrie.command.input` |
| `2026-08-15 10:01:49` | `cowrie.log.closed` |
| `2026-08-15 10:01:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e3836be07ae

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-15 10:03 |
| **Last Seen** | 2026-08-15 10:03 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 10:03:20` | `cowrie.session.connect` |
| `2026-08-15 10:03:20` | `cowrie.client.version` |
| `2026-08-15 10:03:20` | `cowrie.client.kex` |
| `2026-08-15 10:03:21` | `cowrie.login.success` |
| `2026-08-15 10:03:22` | `cowrie.session.params` |
| `2026-08-15 10:03:22` | `cowrie.command.input` |
| `2026-08-15 10:03:22` | `cowrie.command.input` |
| `2026-08-15 10:03:22` | `cowrie.command.input` |
| `2026-08-15 10:03:22` | `cowrie.command.input` |
| `2026-08-15 10:03:22` | `cowrie.command.input` |
| `2026-08-15 10:03:22` | `cowrie.command.success` |
| `2026-08-15 10:03:22` | `cowrie.command.input` |
| `2026-08-15 10:03:22` | `cowrie.command.input` |
| `2026-08-15 10:03:22` | `cowrie.command.input` |
| `2026-08-15 10:03:22` | `cowrie.command.input` |
| `2026-08-15 10:03:22` | `cowrie.log.closed` |
| `2026-08-15 10:03:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca72c2f3851a

| Field | Detail |
|---|---|
| **Source IP** | `58.245.210[.]70` |
| **First Seen** | 2026-08-15 10:03 |
| **Last Seen** | 2026-08-15 10:03 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 10:03:46` | `cowrie.session.connect` |
| `2026-08-15 10:03:47` | `cowrie.client.version` |
| `2026-08-15 10:03:47` | `cowrie.client.kex` |
| `2026-08-15 10:03:49` | `cowrie.login.success` |
| `2026-08-15 10:03:50` | `cowrie.direct-tcpip.request` |
| `2026-08-15 10:03:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.245.210[.]70` to AbuseIPDB if not already reported
- [ ] Block `58.245.210[.]70` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0270571cf9a1

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-15 10:04 |
| **Last Seen** | 2026-08-15 10:04 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 10:04:55` | `cowrie.session.connect` |
| `2026-08-15 10:04:56` | `cowrie.client.version` |
| `2026-08-15 10:04:56` | `cowrie.client.kex` |
| `2026-08-15 10:04:57` | `cowrie.login.success` |
| `2026-08-15 10:04:58` | `cowrie.session.params` |
| `2026-08-15 10:04:58` | `cowrie.command.input` |
| `2026-08-15 10:04:58` | `cowrie.command.input` |
| `2026-08-15 10:04:58` | `cowrie.command.input` |
| `2026-08-15 10:04:58` | `cowrie.command.input` |
| `2026-08-15 10:04:58` | `cowrie.command.input` |
| `2026-08-15 10:04:58` | `cowrie.command.success` |
| `2026-08-15 10:04:58` | `cowrie.command.input` |
| `2026-08-15 10:04:58` | `cowrie.command.input` |
| `2026-08-15 10:04:58` | `cowrie.command.input` |
| `2026-08-15 10:04:58` | `cowrie.command.input` |
| `2026-08-15 10:04:58` | `cowrie.log.closed` |
| `2026-08-15 10:04:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b135b24402b

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-15 10:06 |
| **Last Seen** | 2026-08-15 10:06 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 10:06:26` | `cowrie.session.connect` |
| `2026-08-15 10:06:27` | `cowrie.client.version` |
| `2026-08-15 10:06:27` | `cowrie.client.kex` |
| `2026-08-15 10:06:28` | `cowrie.login.success` |
| `2026-08-15 10:06:29` | `cowrie.session.params` |
| `2026-08-15 10:06:29` | `cowrie.command.input` |
| `2026-08-15 10:06:29` | `cowrie.command.input` |
| `2026-08-15 10:06:29` | `cowrie.command.input` |
| `2026-08-15 10:06:29` | `cowrie.command.input` |
| `2026-08-15 10:06:29` | `cowrie.command.input` |
| `2026-08-15 10:06:29` | `cowrie.command.success` |
| `2026-08-15 10:06:29` | `cowrie.command.input` |
| `2026-08-15 10:06:29` | `cowrie.command.input` |
| `2026-08-15 10:06:29` | `cowrie.command.input` |
| `2026-08-15 10:06:29` | `cowrie.command.input` |
| `2026-08-15 10:06:30` | `cowrie.log.closed` |
| `2026-08-15 10:06:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25ccf2d2e454

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-15 10:07 |
| **Last Seen** | 2026-08-15 10:08 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 10:07:56` | `cowrie.session.connect` |
| `2026-08-15 10:07:57` | `cowrie.client.version` |
| `2026-08-15 10:07:57` | `cowrie.client.kex` |
| `2026-08-15 10:07:58` | `cowrie.login.success` |
| `2026-08-15 10:08:00` | `cowrie.session.params` |
| `2026-08-15 10:08:00` | `cowrie.command.input` |
| `2026-08-15 10:08:00` | `cowrie.command.input` |
| `2026-08-15 10:08:00` | `cowrie.command.input` |
| `2026-08-15 10:08:00` | `cowrie.command.input` |
| `2026-08-15 10:08:00` | `cowrie.command.input` |
| `2026-08-15 10:08:00` | `cowrie.command.success` |
| `2026-08-15 10:08:00` | `cowrie.command.input` |
| `2026-08-15 10:08:00` | `cowrie.command.input` |
| `2026-08-15 10:08:00` | `cowrie.command.input` |
| `2026-08-15 10:08:00` | `cowrie.command.input` |
| `2026-08-15 10:08:00` | `cowrie.log.closed` |
| `2026-08-15 10:08:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57d1702e7844

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-15 10:09 |
| **Last Seen** | 2026-08-15 10:09 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 10:09:25` | `cowrie.session.connect` |
| `2026-08-15 10:09:25` | `cowrie.client.version` |
| `2026-08-15 10:09:25` | `cowrie.client.kex` |
| `2026-08-15 10:09:26` | `cowrie.login.success` |
| `2026-08-15 10:09:28` | `cowrie.session.params` |
| `2026-08-15 10:09:28` | `cowrie.command.input` |
| `2026-08-15 10:09:28` | `cowrie.command.input` |
| `2026-08-15 10:09:28` | `cowrie.command.input` |
| `2026-08-15 10:09:28` | `cowrie.command.input` |
| `2026-08-15 10:09:28` | `cowrie.command.input` |
| `2026-08-15 10:09:28` | `cowrie.command.success` |
| `2026-08-15 10:09:28` | `cowrie.command.input` |
| `2026-08-15 10:09:28` | `cowrie.command.input` |
| `2026-08-15 10:09:28` | `cowrie.command.input` |
| `2026-08-15 10:09:28` | `cowrie.command.input` |
| `2026-08-15 10:09:28` | `cowrie.log.closed` |
| `2026-08-15 10:09:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da1ec7c24dd6

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-15 10:10 |
| **Last Seen** | 2026-08-15 10:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 10:10:45` | `cowrie.session.connect` |
| `2026-08-15 10:10:45` | `cowrie.client.version` |
| `2026-08-15 10:10:45` | `cowrie.client.kex` |
| `2026-08-15 10:10:46` | `cowrie.login.success` |
| `2026-08-15 10:10:46` | `cowrie.direct-tcpip.request` |
| `2026-08-15 10:10:46` | `cowrie.direct-tcpip.data` |
| `2026-08-15 10:10:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f145fca7727d

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-15 10:10 |
| **Last Seen** | 2026-08-15 10:10 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 10:10:53` | `cowrie.session.connect` |
| `2026-08-15 10:10:53` | `cowrie.client.version` |
| `2026-08-15 10:10:53` | `cowrie.client.kex` |
| `2026-08-15 10:10:54` | `cowrie.login.success` |
| `2026-08-15 10:10:56` | `cowrie.session.params` |
| `2026-08-15 10:10:56` | `cowrie.command.input` |
| `2026-08-15 10:10:56` | `cowrie.command.input` |
| `2026-08-15 10:10:56` | `cowrie.command.input` |
| `2026-08-15 10:10:56` | `cowrie.command.input` |
| `2026-08-15 10:10:56` | `cowrie.command.input` |
| `2026-08-15 10:10:56` | `cowrie.command.success` |
| `2026-08-15 10:10:56` | `cowrie.command.input` |
| `2026-08-15 10:10:56` | `cowrie.command.input` |
| `2026-08-15 10:10:56` | `cowrie.command.input` |
| `2026-08-15 10:10:56` | `cowrie.command.input` |
| `2026-08-15 10:10:56` | `cowrie.log.closed` |
| `2026-08-15 10:10:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3062c2d6f8b2

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-15 10:12 |
| **Last Seen** | 2026-08-15 10:12 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 10:12:22` | `cowrie.session.connect` |
| `2026-08-15 10:12:23` | `cowrie.client.version` |
| `2026-08-15 10:12:23` | `cowrie.client.kex` |
| `2026-08-15 10:12:24` | `cowrie.login.success` |
| `2026-08-15 10:12:25` | `cowrie.session.params` |
| `2026-08-15 10:12:25` | `cowrie.command.input` |
| `2026-08-15 10:12:25` | `cowrie.command.input` |
| `2026-08-15 10:12:25` | `cowrie.command.input` |
| `2026-08-15 10:12:25` | `cowrie.command.input` |
| `2026-08-15 10:12:25` | `cowrie.command.input` |
| `2026-08-15 10:12:25` | `cowrie.command.success` |
| `2026-08-15 10:12:25` | `cowrie.command.input` |
| `2026-08-15 10:12:25` | `cowrie.command.input` |
| `2026-08-15 10:12:25` | `cowrie.command.input` |
| `2026-08-15 10:12:25` | `cowrie.command.input` |
| `2026-08-15 10:12:25` | `cowrie.log.closed` |
| `2026-08-15 10:12:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38b5e6ef5f54

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-15 10:13 |
| **Last Seen** | 2026-08-15 10:13 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 10:13:57` | `cowrie.session.connect` |
| `2026-08-15 10:13:57` | `cowrie.client.version` |
| `2026-08-15 10:13:57` | `cowrie.client.kex` |
| `2026-08-15 10:13:58` | `cowrie.login.success` |
| `2026-08-15 10:13:59` | `cowrie.session.params` |
| `2026-08-15 10:13:59` | `cowrie.command.input` |
| `2026-08-15 10:13:59` | `cowrie.command.input` |
| `2026-08-15 10:13:59` | `cowrie.command.input` |
| `2026-08-15 10:13:59` | `cowrie.command.input` |
| `2026-08-15 10:13:59` | `cowrie.command.input` |
| `2026-08-15 10:13:59` | `cowrie.command.success` |
| `2026-08-15 10:13:59` | `cowrie.command.input` |
| `2026-08-15 10:13:59` | `cowrie.command.input` |
| `2026-08-15 10:13:59` | `cowrie.command.input` |
| `2026-08-15 10:13:59` | `cowrie.command.input` |
| `2026-08-15 10:13:59` | `cowrie.log.closed` |
| `2026-08-15 10:13:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed35f579d3fe

| Field | Detail |
|---|---|
| **Source IP** | `39.164.94[.]190` |
| **First Seen** | 2026-08-15 10:14 |
| **Last Seen** | 2026-08-15 10:15 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 10:14:59` | `cowrie.session.connect` |
| `2026-08-15 10:15:00` | `cowrie.client.version` |
| `2026-08-15 10:15:00` | `cowrie.client.kex` |
| `2026-08-15 10:15:02` | `cowrie.login.success` |
| `2026-08-15 10:15:03` | `cowrie.direct-tcpip.request` |
| `2026-08-15 10:15:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `39.164.94[.]190` to AbuseIPDB if not already reported
- [ ] Block `39.164.94[.]190` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d9b2e931ed7

| Field | Detail |
|---|---|
| **Source IP** | `200.58.83[.]79` |
| **First Seen** | 2026-08-15 10:15 |
| **Last Seen** | 2026-08-15 10:15 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 10:15:09` | `cowrie.session.connect` |
| `2026-08-15 10:15:09` | `cowrie.client.version` |
| `2026-08-15 10:15:09` | `cowrie.client.kex` |
| `2026-08-15 10:15:11` | `cowrie.login.success` |
| `2026-08-15 10:15:12` | `cowrie.direct-tcpip.request` |
| `2026-08-15 10:15:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.58.83[.]79` to AbuseIPDB if not already reported
- [ ] Block `200.58.83[.]79` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63e004e33a81

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-15 10:15 |
| **Last Seen** | 2026-08-15 10:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 10:15:42` | `cowrie.session.connect` |
| `2026-08-15 10:15:42` | `cowrie.client.version` |
| `2026-08-15 10:15:42` | `cowrie.client.kex` |
| `2026-08-15 10:15:43` | `cowrie.login.success` |
| `2026-08-15 10:15:44` | `cowrie.session.params` |
| `2026-08-15 10:15:44` | `cowrie.command.input` |
| `2026-08-15 10:15:44` | `cowrie.command.input` |
| `2026-08-15 10:15:44` | `cowrie.command.input` |
| `2026-08-15 10:15:44` | `cowrie.command.input` |
| `2026-08-15 10:15:44` | `cowrie.command.input` |
| `2026-08-15 10:15:44` | `cowrie.command.success` |
| `2026-08-15 10:15:44` | `cowrie.command.input` |
| `2026-08-15 10:15:44` | `cowrie.command.input` |
| `2026-08-15 10:15:44` | `cowrie.command.input` |
| `2026-08-15 10:15:44` | `cowrie.command.input` |
| `2026-08-15 10:15:44` | `cowrie.log.closed` |
| `2026-08-15 10:15:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a816a13d7a5

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-15 10:16 |
| **Last Seen** | 2026-08-15 10:16 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 10:16:41` | `cowrie.session.connect` |
| `2026-08-15 10:16:41` | `cowrie.client.version` |
| `2026-08-15 10:16:41` | `cowrie.client.kex` |
| `2026-08-15 10:16:42` | `cowrie.login.success` |
| `2026-08-15 10:16:43` | `cowrie.session.params` |
| `2026-08-15 10:16:43` | `cowrie.command.input` |
| `2026-08-15 10:16:43` | `cowrie.log.closed` |
| `2026-08-15 10:16:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53473a67e940

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-15 10:17 |
| **Last Seen** | 2026-08-15 10:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 10:17:36` | `cowrie.session.connect` |
| `2026-08-15 10:17:36` | `cowrie.client.version` |
| `2026-08-15 10:17:36` | `cowrie.client.kex` |
| `2026-08-15 10:17:37` | `cowrie.login.success` |
| `2026-08-15 10:17:38` | `cowrie.session.params` |
| `2026-08-15 10:17:38` | `cowrie.command.input` |
| `2026-08-15 10:17:38` | `cowrie.command.input` |
| `2026-08-15 10:17:38` | `cowrie.command.input` |
| `2026-08-15 10:17:38` | `cowrie.command.input` |
| `2026-08-15 10:17:38` | `cowrie.command.input` |
| `2026-08-15 10:17:38` | `cowrie.command.success` |
| `2026-08-15 10:17:38` | `cowrie.command.input` |
| `2026-08-15 10:17:38` | `cowrie.command.input` |
| `2026-08-15 10:17:38` | `cowrie.command.input` |
| `2026-08-15 10:17:38` | `cowrie.command.input` |
| `2026-08-15 10:17:38` | `cowrie.log.closed` |
| `2026-08-15 10:17:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9136fabb493

| Field | Detail |
|---|---|
| **Source IP** | `45.142.193[.]164` |
| **First Seen** | 2026-08-15 10:18 |
| **Last Seen** | 2026-08-15 10:18 |
| **Session Duration** | 44s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 10:18:06` | `cowrie.session.connect` |
| `2026-08-15 10:18:12` | `cowrie.client.version` |
| `2026-08-15 10:18:12` | `cowrie.client.kex` |
| `2026-08-15 10:18:34` | `cowrie.login.success` |
| `2026-08-15 10:18:46` | `cowrie.session.params` |
| `2026-08-15 10:18:46` | `cowrie.command.input` |
| `2026-08-15 10:18:51` | `cowrie.log.closed` |
| `2026-08-15 10:18:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.142.193[.]164` to AbuseIPDB if not already reported
- [ ] Block `45.142.193[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d308381d96d

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-15 10:19 |
| **Last Seen** | 2026-08-15 10:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 10:19:31` | `cowrie.session.connect` |
| `2026-08-15 10:19:31` | `cowrie.client.version` |
| `2026-08-15 10:19:31` | `cowrie.client.kex` |
| `2026-08-15 10:19:31` | `cowrie.login.success` |
| `2026-08-15 10:19:32` | `cowrie.session.params` |
| `2026-08-15 10:19:32` | `cowrie.command.input` |
| `2026-08-15 10:19:32` | `cowrie.command.input` |
| `2026-08-15 10:19:32` | `cowrie.command.input` |
| `2026-08-15 10:19:32` | `cowrie.command.input` |
| `2026-08-15 10:19:32` | `cowrie.command.input` |
| `2026-08-15 10:19:32` | `cowrie.command.success` |
| `2026-08-15 10:19:32` | `cowrie.command.input` |
| `2026-08-15 10:19:32` | `cowrie.command.input` |
| `2026-08-15 10:19:32` | `cowrie.command.input` |
| `2026-08-15 10:19:32` | `cowrie.command.input` |
| `2026-08-15 10:19:32` | `cowrie.log.closed` |
| `2026-08-15 10:19:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0aae20adac5

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-15 10:20 |
| **Last Seen** | 2026-08-15 10:21 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 10:20:58` | `cowrie.session.connect` |
| `2026-08-15 10:20:59` | `cowrie.client.version` |
| `2026-08-15 10:20:59` | `cowrie.client.kex` |
| `2026-08-15 10:21:00` | `cowrie.login.success` |
| `2026-08-15 10:21:01` | `cowrie.session.params` |
| `2026-08-15 10:21:01` | `cowrie.command.input` |
| `2026-08-15 10:21:01` | `cowrie.command.input` |
| `2026-08-15 10:21:01` | `cowrie.command.input` |
| `2026-08-15 10:21:01` | `cowrie.command.input` |
| `2026-08-15 10:21:01` | `cowrie.command.input` |
| `2026-08-15 10:21:01` | `cowrie.command.success` |
| `2026-08-15 10:21:01` | `cowrie.command.input` |
| `2026-08-15 10:21:01` | `cowrie.command.input` |
| `2026-08-15 10:21:01` | `cowrie.command.input` |
| `2026-08-15 10:21:01` | `cowrie.command.input` |
| `2026-08-15 10:21:02` | `cowrie.log.closed` |
| `2026-08-15 10:21:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02501f3427c6

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-15 10:22 |
| **Last Seen** | 2026-08-15 10:22 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 10:22:23` | `cowrie.session.connect` |
| `2026-08-15 10:22:23` | `cowrie.client.version` |
| `2026-08-15 10:22:23` | `cowrie.client.kex` |
| `2026-08-15 10:22:24` | `cowrie.login.success` |
| `2026-08-15 10:22:26` | `cowrie.session.params` |
| `2026-08-15 10:22:26` | `cowrie.command.input` |
| `2026-08-15 10:22:26` | `cowrie.command.input` |
| `2026-08-15 10:22:26` | `cowrie.command.input` |
| `2026-08-15 10:22:26` | `cowrie.command.input` |
| `2026-08-15 10:22:26` | `cowrie.command.input` |
| `2026-08-15 10:22:26` | `cowrie.command.success` |
| `2026-08-15 10:22:26` | `cowrie.command.input` |
| `2026-08-15 10:22:26` | `cowrie.command.input` |
| `2026-08-15 10:22:26` | `cowrie.command.input` |
| `2026-08-15 10:22:26` | `cowrie.command.input` |
| `2026-08-15 10:22:26` | `cowrie.log.closed` |
| `2026-08-15 10:22:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9c18d1b4874

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-15 10:23 |
| **Last Seen** | 2026-08-15 10:23 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 10:23:39` | `cowrie.session.connect` |
| `2026-08-15 10:23:40` | `cowrie.client.version` |
| `2026-08-15 10:23:40` | `cowrie.client.kex` |
| `2026-08-15 10:23:41` | `cowrie.login.success` |
| `2026-08-15 10:23:43` | `cowrie.session.params` |
| `2026-08-15 10:23:43` | `cowrie.command.input` |
| `2026-08-15 10:23:43` | `cowrie.command.input` |
| `2026-08-15 10:23:43` | `cowrie.command.input` |
| `2026-08-15 10:23:43` | `cowrie.command.input` |
| `2026-08-15 10:23:43` | `cowrie.command.input` |
| `2026-08-15 10:23:43` | `cowrie.command.success` |
| `2026-08-15 10:23:43` | `cowrie.command.input` |
| `2026-08-15 10:23:43` | `cowrie.command.input` |
| `2026-08-15 10:23:43` | `cowrie.command.input` |
| `2026-08-15 10:23:43` | `cowrie.command.input` |
| `2026-08-15 10:23:44` | `cowrie.log.closed` |
| `2026-08-15 10:23:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-182caae66523

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-15 10:24 |
| **Last Seen** | 2026-08-15 10:25 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 10:24:56` | `cowrie.session.connect` |
| `2026-08-15 10:24:57` | `cowrie.client.version` |
| `2026-08-15 10:24:57` | `cowrie.client.kex` |
| `2026-08-15 10:24:59` | `cowrie.login.success` |
| `2026-08-15 10:25:00` | `cowrie.session.params` |
| `2026-08-15 10:25:00` | `cowrie.command.input` |
| `2026-08-15 10:25:00` | `cowrie.command.input` |
| `2026-08-15 10:25:00` | `cowrie.command.input` |
| `2026-08-15 10:25:00` | `cowrie.command.input` |
| `2026-08-15 10:25:00` | `cowrie.command.input` |
| `2026-08-15 10:25:00` | `cowrie.command.success` |
| `2026-08-15 10:25:00` | `cowrie.command.input` |
| `2026-08-15 10:25:00` | `cowrie.command.input` |
| `2026-08-15 10:25:00` | `cowrie.command.input` |
| `2026-08-15 10:25:00` | `cowrie.command.input` |
| `2026-08-15 10:25:00` | `cowrie.log.closed` |
| `2026-08-15 10:25:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4cc1a39c837

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-15 10:26 |
| **Last Seen** | 2026-08-15 10:26 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 10:26:20` | `cowrie.session.connect` |
| `2026-08-15 10:26:20` | `cowrie.client.version` |
| `2026-08-15 10:26:20` | `cowrie.client.kex` |
| `2026-08-15 10:26:22` | `cowrie.login.success` |
| `2026-08-15 10:26:24` | `cowrie.session.params` |
| `2026-08-15 10:26:24` | `cowrie.command.input` |
| `2026-08-15 10:26:24` | `cowrie.command.input` |
| `2026-08-15 10:26:24` | `cowrie.command.input` |
| `2026-08-15 10:26:24` | `cowrie.command.input` |
| `2026-08-15 10:26:24` | `cowrie.command.input` |
| `2026-08-15 10:26:24` | `cowrie.command.success` |
| `2026-08-15 10:26:24` | `cowrie.command.input` |
| `2026-08-15 10:26:24` | `cowrie.command.input` |
| `2026-08-15 10:26:24` | `cowrie.command.input` |
| `2026-08-15 10:26:24` | `cowrie.command.input` |
| `2026-08-15 10:26:25` | `cowrie.log.closed` |
| `2026-08-15 10:26:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-033addc8ec10

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-15 10:27 |
| **Last Seen** | 2026-08-15 10:27 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 10:27:44` | `cowrie.session.connect` |
| `2026-08-15 10:27:44` | `cowrie.client.version` |
| `2026-08-15 10:27:44` | `cowrie.client.kex` |
| `2026-08-15 10:27:46` | `cowrie.login.success` |
| `2026-08-15 10:27:47` | `cowrie.session.params` |
| `2026-08-15 10:27:47` | `cowrie.command.input` |
| `2026-08-15 10:27:47` | `cowrie.command.input` |
| `2026-08-15 10:27:47` | `cowrie.command.input` |
| `2026-08-15 10:27:47` | `cowrie.command.input` |
| `2026-08-15 10:27:47` | `cowrie.command.input` |
| `2026-08-15 10:27:47` | `cowrie.command.success` |
| `2026-08-15 10:27:47` | `cowrie.command.input` |
| `2026-08-15 10:27:47` | `cowrie.command.input` |
| `2026-08-15 10:27:47` | `cowrie.command.input` |
| `2026-08-15 10:27:47` | `cowrie.command.input` |
| `2026-08-15 10:27:47` | `cowrie.log.closed` |
| `2026-08-15 10:27:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6504487a196

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-15 10:29 |
| **Last Seen** | 2026-08-15 10:29 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 10:29:10` | `cowrie.session.connect` |
| `2026-08-15 10:29:10` | `cowrie.client.version` |
| `2026-08-15 10:29:10` | `cowrie.client.kex` |
| `2026-08-15 10:29:12` | `cowrie.login.success` |
| `2026-08-15 10:29:13` | `cowrie.session.params` |
| `2026-08-15 10:29:13` | `cowrie.command.input` |
| `2026-08-15 10:29:13` | `cowrie.command.input` |
| `2026-08-15 10:29:13` | `cowrie.command.input` |
| `2026-08-15 10:29:13` | `cowrie.command.input` |
| `2026-08-15 10:29:13` | `cowrie.command.input` |
| `2026-08-15 10:29:13` | `cowrie.command.success` |
| `2026-08-15 10:29:13` | `cowrie.command.input` |
| `2026-08-15 10:29:13` | `cowrie.command.input` |
| `2026-08-15 10:29:13` | `cowrie.command.input` |
| `2026-08-15 10:29:13` | `cowrie.command.input` |
| `2026-08-15 10:29:13` | `cowrie.log.closed` |
| `2026-08-15 10:29:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f0a847dc387

| Field | Detail |
|---|---|
| **Source IP** | `213.230.124[.]17` |
| **First Seen** | 2026-08-15 10:30 |
| **Last Seen** | 2026-08-15 10:30 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 10:30:06` | `cowrie.session.connect` |
| `2026-08-15 10:30:07` | `cowrie.client.version` |
| `2026-08-15 10:30:07` | `cowrie.client.kex` |
| `2026-08-15 10:30:08` | `cowrie.login.success` |
| `2026-08-15 10:30:09` | `cowrie.direct-tcpip.request` |
| `2026-08-15 10:30:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.230.124[.]17` to AbuseIPDB if not already reported
- [ ] Block `213.230.124[.]17` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-932d9b531300

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-15 10:30 |
| **Last Seen** | 2026-08-15 10:30 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 10:30:39` | `cowrie.session.connect` |
| `2026-08-15 10:30:39` | `cowrie.client.version` |
| `2026-08-15 10:30:39` | `cowrie.client.kex` |
| `2026-08-15 10:30:40` | `cowrie.login.success` |
| `2026-08-15 10:30:42` | `cowrie.session.params` |
| `2026-08-15 10:30:42` | `cowrie.command.input` |
| `2026-08-15 10:30:42` | `cowrie.command.input` |
| `2026-08-15 10:30:42` | `cowrie.command.input` |
| `2026-08-15 10:30:42` | `cowrie.command.input` |
| `2026-08-15 10:30:42` | `cowrie.command.input` |
| `2026-08-15 10:30:42` | `cowrie.command.success` |
| `2026-08-15 10:30:42` | `cowrie.command.input` |
| `2026-08-15 10:30:42` | `cowrie.command.input` |
| `2026-08-15 10:30:42` | `cowrie.command.input` |
| `2026-08-15 10:30:42` | `cowrie.command.input` |
| `2026-08-15 10:30:42` | `cowrie.log.closed` |
| `2026-08-15 10:30:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a41608d5931d

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-15 10:32 |
| **Last Seen** | 2026-08-15 10:32 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 10:32:09` | `cowrie.session.connect` |
| `2026-08-15 10:32:09` | `cowrie.client.version` |
| `2026-08-15 10:32:09` | `cowrie.client.kex` |
| `2026-08-15 10:32:10` | `cowrie.login.success` |
| `2026-08-15 10:32:11` | `cowrie.session.params` |
| `2026-08-15 10:32:11` | `cowrie.command.input` |
| `2026-08-15 10:32:11` | `cowrie.command.input` |
| `2026-08-15 10:32:11` | `cowrie.command.input` |
| `2026-08-15 10:32:11` | `cowrie.command.input` |
| `2026-08-15 10:32:11` | `cowrie.command.input` |
| `2026-08-15 10:32:11` | `cowrie.command.success` |
| `2026-08-15 10:32:11` | `cowrie.command.input` |
| `2026-08-15 10:32:11` | `cowrie.command.input` |
| `2026-08-15 10:32:11` | `cowrie.command.input` |
| `2026-08-15 10:32:11` | `cowrie.command.input` |
| `2026-08-15 10:32:12` | `cowrie.log.closed` |
| `2026-08-15 10:32:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e59e6f309b3e

| Field | Detail |
|---|---|
| **Source IP** | `183.82.108[.]109` |
| **First Seen** | 2026-08-15 10:32 |
| **Last Seen** | 2026-08-15 10:32 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 10:32:48` | `cowrie.session.connect` |
| `2026-08-15 10:32:49` | `cowrie.client.version` |
| `2026-08-15 10:32:49` | `cowrie.client.kex` |
| `2026-08-15 10:32:51` | `cowrie.login.success` |
| `2026-08-15 10:32:52` | `cowrie.direct-tcpip.request` |
| `2026-08-15 10:32:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.82.108[.]109` to AbuseIPDB if not already reported
- [ ] Block `183.82.108[.]109` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-babcee3fa276

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-15 10:33 |
| **Last Seen** | 2026-08-15 10:33 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 10:33:43` | `cowrie.session.connect` |
| `2026-08-15 10:33:43` | `cowrie.client.version` |
| `2026-08-15 10:33:43` | `cowrie.client.kex` |
| `2026-08-15 10:33:44` | `cowrie.login.success` |
| `2026-08-15 10:33:45` | `cowrie.session.params` |
| `2026-08-15 10:33:45` | `cowrie.command.input` |
| `2026-08-15 10:33:45` | `cowrie.command.input` |
| `2026-08-15 10:33:45` | `cowrie.command.input` |
| `2026-08-15 10:33:45` | `cowrie.command.input` |
| `2026-08-15 10:33:45` | `cowrie.command.input` |
| `2026-08-15 10:33:45` | `cowrie.command.success` |
| `2026-08-15 10:33:45` | `cowrie.command.input` |
| `2026-08-15 10:33:45` | `cowrie.command.input` |
| `2026-08-15 10:33:45` | `cowrie.command.input` |
| `2026-08-15 10:33:45` | `cowrie.command.input` |
| `2026-08-15 10:33:45` | `cowrie.log.closed` |
| `2026-08-15 10:33:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4eb25830966e

| Field | Detail |
|---|---|
| **Source IP** | `116.114.94[.]242` |
| **First Seen** | 2026-08-15 10:35 |
| **Last Seen** | 2026-08-15 10:35 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 10:35:19` | `cowrie.session.connect` |
| `2026-08-15 10:35:20` | `cowrie.client.version` |
| `2026-08-15 10:35:20` | `cowrie.client.kex` |
| `2026-08-15 10:35:22` | `cowrie.login.success` |
| `2026-08-15 10:35:23` | `cowrie.direct-tcpip.request` |
| `2026-08-15 10:35:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.114.94[.]242` to AbuseIPDB if not already reported
- [ ] Block `116.114.94[.]242` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-342926df83d5

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-15 10:35 |
| **Last Seen** | 2026-08-15 10:35 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 10:35:21` | `cowrie.session.connect` |
| `2026-08-15 10:35:21` | `cowrie.client.version` |
| `2026-08-15 10:35:21` | `cowrie.client.kex` |
| `2026-08-15 10:35:21` | `cowrie.login.success` |
| `2026-08-15 10:35:22` | `cowrie.session.params` |
| `2026-08-15 10:35:22` | `cowrie.command.input` |
| `2026-08-15 10:35:22` | `cowrie.command.input` |
| `2026-08-15 10:35:22` | `cowrie.command.input` |
| `2026-08-15 10:35:22` | `cowrie.command.input` |
| `2026-08-15 10:35:22` | `cowrie.command.input` |
| `2026-08-15 10:35:22` | `cowrie.command.success` |
| `2026-08-15 10:35:22` | `cowrie.command.input` |
| `2026-08-15 10:35:22` | `cowrie.command.input` |
| `2026-08-15 10:35:22` | `cowrie.command.input` |
| `2026-08-15 10:35:22` | `cowrie.command.input` |
| `2026-08-15 10:35:22` | `cowrie.log.closed` |
| `2026-08-15 10:35:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7afa38319ef

| Field | Detail |
|---|---|
| **Source IP** | `65.20.204[.]41` |
| **First Seen** | 2026-08-15 10:35 |
| **Last Seen** | 2026-08-15 10:35 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 10:35:28` | `cowrie.session.connect` |
| `2026-08-15 10:35:28` | `cowrie.client.version` |
| `2026-08-15 10:35:28` | `cowrie.client.kex` |
| `2026-08-15 10:35:30` | `cowrie.login.success` |
| `2026-08-15 10:35:30` | `cowrie.direct-tcpip.request` |
| `2026-08-15 10:35:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.204[.]41` to AbuseIPDB if not already reported
- [ ] Block `65.20.204[.]41` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f498ddc28a72

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-15 10:35 |
| **Last Seen** | 2026-08-15 10:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 10:35:54` | `cowrie.session.connect` |
| `2026-08-15 10:35:54` | `cowrie.client.version` |
| `2026-08-15 10:35:54` | `cowrie.client.kex` |
| `2026-08-15 10:35:54` | `cowrie.login.success` |
| `2026-08-15 10:35:55` | `cowrie.session.params` |
| `2026-08-15 10:35:55` | `cowrie.command.input` |
| `2026-08-15 10:35:56` | `cowrie.log.closed` |
| `2026-08-15 10:35:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eddeeb9c3408

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-15 10:36 |
| **Last Seen** | 2026-08-15 10:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 10:36:59` | `cowrie.session.connect` |
| `2026-08-15 10:36:59` | `cowrie.client.version` |
| `2026-08-15 10:36:59` | `cowrie.client.kex` |
| `2026-08-15 10:37:00` | `cowrie.login.success` |
| `2026-08-15 10:37:00` | `cowrie.session.params` |
| `2026-08-15 10:37:00` | `cowrie.command.input` |
| `2026-08-15 10:37:00` | `cowrie.command.input` |
| `2026-08-15 10:37:00` | `cowrie.command.input` |
| `2026-08-15 10:37:00` | `cowrie.command.input` |
| `2026-08-15 10:37:00` | `cowrie.command.input` |
| `2026-08-15 10:37:00` | `cowrie.command.success` |
| `2026-08-15 10:37:00` | `cowrie.command.input` |
| `2026-08-15 10:37:00` | `cowrie.command.input` |
| `2026-08-15 10:37:00` | `cowrie.command.input` |
| `2026-08-15 10:37:00` | `cowrie.command.input` |
| `2026-08-15 10:37:01` | `cowrie.log.closed` |
| `2026-08-15 10:37:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99dab5c8517b

| Field | Detail |
|---|---|
| **Source IP** | `166.130.176[.]136` |
| **First Seen** | 2026-08-15 10:37 |
| **Last Seen** | 2026-08-15 10:37 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 10:37:25` | `cowrie.session.connect` |
| `2026-08-15 10:37:25` | `cowrie.client.version` |
| `2026-08-15 10:37:25` | `cowrie.client.kex` |
| `2026-08-15 10:37:26` | `cowrie.login.success` |
| `2026-08-15 10:37:27` | `cowrie.direct-tcpip.request` |
| `2026-08-15 10:37:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `166.130.176[.]136` to AbuseIPDB if not already reported
- [ ] Block `166.130.176[.]136` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-adbd53b1afe5

| Field | Detail |
|---|---|
| **Source IP** | `179.189.85[.]66` |
| **First Seen** | 2026-08-15 10:37 |
| **Last Seen** | 2026-08-15 10:37 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 10:37:31` | `cowrie.session.connect` |
| `2026-08-15 10:37:32` | `cowrie.client.version` |
| `2026-08-15 10:37:32` | `cowrie.client.kex` |
| `2026-08-15 10:37:34` | `cowrie.login.success` |
| `2026-08-15 10:37:34` | `cowrie.direct-tcpip.request` |
| `2026-08-15 10:37:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.189.85[.]66` to AbuseIPDB if not already reported
- [ ] Block `179.189.85[.]66` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3dccb5461fe

| Field | Detail |
|---|---|
| **Source IP** | `187.218.57[.]50` |
| **First Seen** | 2026-08-15 10:37 |
| **Last Seen** | 2026-08-15 10:37 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 10:37:44` | `cowrie.session.connect` |
| `2026-08-15 10:37:45` | `cowrie.client.version` |
| `2026-08-15 10:37:45` | `cowrie.client.kex` |
| `2026-08-15 10:37:46` | `cowrie.login.success` |
| `2026-08-15 10:37:47` | `cowrie.direct-tcpip.request` |
| `2026-08-15 10:37:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.218.57[.]50` to AbuseIPDB if not already reported
- [ ] Block `187.218.57[.]50` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81042db549fd

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-15 10:38 |
| **Last Seen** | 2026-08-15 10:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 10:38:39` | `cowrie.session.connect` |
| `2026-08-15 10:38:39` | `cowrie.client.version` |
| `2026-08-15 10:38:39` | `cowrie.client.kex` |
| `2026-08-15 10:38:40` | `cowrie.login.success` |
| `2026-08-15 10:38:41` | `cowrie.session.params` |
| `2026-08-15 10:38:41` | `cowrie.command.input` |
| `2026-08-15 10:38:41` | `cowrie.command.input` |
| `2026-08-15 10:38:41` | `cowrie.command.input` |
| `2026-08-15 10:38:41` | `cowrie.command.input` |
| `2026-08-15 10:38:41` | `cowrie.command.input` |
| `2026-08-15 10:38:41` | `cowrie.command.success` |
| `2026-08-15 10:38:41` | `cowrie.command.input` |
| `2026-08-15 10:38:41` | `cowrie.command.input` |
| `2026-08-15 10:38:41` | `cowrie.command.input` |
| `2026-08-15 10:38:41` | `cowrie.command.input` |
| `2026-08-15 10:38:41` | `cowrie.log.closed` |
| `2026-08-15 10:38:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af8c7749b7c7

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-15 10:40 |
| **Last Seen** | 2026-08-15 10:40 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 10:40:26` | `cowrie.session.connect` |
| `2026-08-15 10:40:26` | `cowrie.client.version` |
| `2026-08-15 10:40:26` | `cowrie.client.kex` |
| `2026-08-15 10:40:27` | `cowrie.login.success` |
| `2026-08-15 10:40:27` | `cowrie.session.params` |
| `2026-08-15 10:40:27` | `cowrie.command.input` |
| `2026-08-15 10:40:27` | `cowrie.command.input` |
| `2026-08-15 10:40:27` | `cowrie.command.input` |
| `2026-08-15 10:40:27` | `cowrie.command.input` |
| `2026-08-15 10:40:27` | `cowrie.command.input` |
| `2026-08-15 10:40:27` | `cowrie.command.success` |
| `2026-08-15 10:40:27` | `cowrie.command.input` |
| `2026-08-15 10:40:27` | `cowrie.command.input` |
| `2026-08-15 10:40:27` | `cowrie.command.input` |
| `2026-08-15 10:40:27` | `cowrie.command.input` |
| `2026-08-15 10:40:28` | `cowrie.log.closed` |
| `2026-08-15 10:40:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8782d6016903

| Field | Detail |
|---|---|
| **Source IP** | `45.142.193[.]164` |
| **First Seen** | 2026-08-15 10:41 |
| **Last Seen** | 2026-08-15 10:41 |
| **Session Duration** | 47s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 10:41:02` | `cowrie.session.connect` |
| `2026-08-15 10:41:08` | `cowrie.client.version` |
| `2026-08-15 10:41:08` | `cowrie.client.kex` |
| `2026-08-15 10:41:31` | `cowrie.login.success` |
| `2026-08-15 10:41:44` | `cowrie.session.params` |
| `2026-08-15 10:41:44` | `cowrie.command.input` |
| `2026-08-15 10:41:49` | `cowrie.log.closed` |
| `2026-08-15 10:41:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.142.193[.]164` to AbuseIPDB if not already reported
- [ ] Block `45.142.193[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79ed94ab3125

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-15 10:41 |
| **Last Seen** | 2026-08-15 10:41 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 10:41:51` | `cowrie.session.connect` |
| `2026-08-15 10:41:51` | `cowrie.client.version` |
| `2026-08-15 10:41:51` | `cowrie.client.kex` |
| `2026-08-15 10:41:53` | `cowrie.login.success` |
| `2026-08-15 10:41:54` | `cowrie.session.params` |
| `2026-08-15 10:41:54` | `cowrie.command.input` |
| `2026-08-15 10:41:54` | `cowrie.command.input` |
| `2026-08-15 10:41:54` | `cowrie.command.input` |
| `2026-08-15 10:41:54` | `cowrie.command.input` |
| `2026-08-15 10:41:54` | `cowrie.command.input` |
| `2026-08-15 10:41:54` | `cowrie.command.success` |
| `2026-08-15 10:41:54` | `cowrie.command.input` |
| `2026-08-15 10:41:54` | `cowrie.command.input` |
| `2026-08-15 10:41:54` | `cowrie.command.input` |
| `2026-08-15 10:41:54` | `cowrie.command.input` |
| `2026-08-15 10:41:54` | `cowrie.log.closed` |
| `2026-08-15 10:41:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0eda7ebeb3d

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-15 10:43 |
| **Last Seen** | 2026-08-15 10:43 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 10:43:14` | `cowrie.session.connect` |
| `2026-08-15 10:43:15` | `cowrie.client.version` |
| `2026-08-15 10:43:15` | `cowrie.client.kex` |
| `2026-08-15 10:43:17` | `cowrie.login.success` |
| `2026-08-15 10:43:19` | `cowrie.session.params` |
| `2026-08-15 10:43:19` | `cowrie.command.input` |
| `2026-08-15 10:43:19` | `cowrie.command.input` |
| `2026-08-15 10:43:19` | `cowrie.command.input` |
| `2026-08-15 10:43:19` | `cowrie.command.input` |
| `2026-08-15 10:43:19` | `cowrie.command.input` |
| `2026-08-15 10:43:19` | `cowrie.command.success` |
| `2026-08-15 10:43:19` | `cowrie.command.input` |
| `2026-08-15 10:43:19` | `cowrie.command.input` |
| `2026-08-15 10:43:19` | `cowrie.command.input` |
| `2026-08-15 10:43:19` | `cowrie.command.input` |
| `2026-08-15 10:43:19` | `cowrie.log.closed` |
| `2026-08-15 10:43:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36e78a84a9b5

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-15 10:44 |
| **Last Seen** | 2026-08-15 10:44 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 10:44:39` | `cowrie.session.connect` |
| `2026-08-15 10:44:40` | `cowrie.client.version` |
| `2026-08-15 10:44:40` | `cowrie.client.kex` |
| `2026-08-15 10:44:42` | `cowrie.login.success` |
| `2026-08-15 10:44:43` | `cowrie.session.params` |
| `2026-08-15 10:44:43` | `cowrie.command.input` |
| `2026-08-15 10:44:43` | `cowrie.command.input` |
| `2026-08-15 10:44:43` | `cowrie.command.input` |
| `2026-08-15 10:44:43` | `cowrie.command.input` |
| `2026-08-15 10:44:43` | `cowrie.command.input` |
| `2026-08-15 10:44:43` | `cowrie.command.success` |
| `2026-08-15 10:44:43` | `cowrie.command.input` |
| `2026-08-15 10:44:43` | `cowrie.command.input` |
| `2026-08-15 10:44:43` | `cowrie.command.input` |
| `2026-08-15 10:44:43` | `cowrie.command.input` |
| `2026-08-15 10:44:44` | `cowrie.log.closed` |
| `2026-08-15 10:44:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3fa7ed5bf2c

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-15 10:46 |
| **Last Seen** | 2026-08-15 10:46 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 10:46:06` | `cowrie.session.connect` |
| `2026-08-15 10:46:07` | `cowrie.client.version` |
| `2026-08-15 10:46:07` | `cowrie.client.kex` |
| `2026-08-15 10:46:09` | `cowrie.login.success` |
| `2026-08-15 10:46:10` | `cowrie.session.params` |
| `2026-08-15 10:46:10` | `cowrie.command.input` |
| `2026-08-15 10:46:10` | `cowrie.command.input` |
| `2026-08-15 10:46:10` | `cowrie.command.input` |
| `2026-08-15 10:46:10` | `cowrie.command.input` |
| `2026-08-15 10:46:10` | `cowrie.command.input` |
| `2026-08-15 10:46:10` | `cowrie.command.success` |
| `2026-08-15 10:46:10` | `cowrie.command.input` |
| `2026-08-15 10:46:10` | `cowrie.command.input` |
| `2026-08-15 10:46:10` | `cowrie.command.input` |
| `2026-08-15 10:46:10` | `cowrie.command.input` |
| `2026-08-15 10:46:11` | `cowrie.log.closed` |
| `2026-08-15 10:46:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f2a2ae4c66b

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-15 10:47 |
| **Last Seen** | 2026-08-15 10:47 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 10:47:34` | `cowrie.session.connect` |
| `2026-08-15 10:47:35` | `cowrie.client.version` |
| `2026-08-15 10:47:35` | `cowrie.client.kex` |
| `2026-08-15 10:47:37` | `cowrie.login.success` |
| `2026-08-15 10:47:38` | `cowrie.session.params` |
| `2026-08-15 10:47:38` | `cowrie.command.input` |
| `2026-08-15 10:47:38` | `cowrie.command.input` |
| `2026-08-15 10:47:38` | `cowrie.command.input` |
| `2026-08-15 10:47:38` | `cowrie.command.input` |
| `2026-08-15 10:47:38` | `cowrie.command.input` |
| `2026-08-15 10:47:38` | `cowrie.command.success` |
| `2026-08-15 10:47:38` | `cowrie.command.input` |
| `2026-08-15 10:47:38` | `cowrie.command.input` |
| `2026-08-15 10:47:38` | `cowrie.command.input` |
| `2026-08-15 10:47:38` | `cowrie.command.input` |
| `2026-08-15 10:47:39` | `cowrie.log.closed` |
| `2026-08-15 10:47:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f27d3673b754

| Field | Detail |
|---|---|
| **Source IP** | `81.22.51[.]64` |
| **First Seen** | 2026-08-15 10:48 |
| **Last Seen** | 2026-08-15 10:49 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 10:48:54` | `cowrie.session.connect` |
| `2026-08-15 10:48:55` | `cowrie.client.version` |
| `2026-08-15 10:48:55` | `cowrie.client.kex` |
| `2026-08-15 10:48:56` | `cowrie.login.success` |
| `2026-08-15 10:48:56` | `cowrie.direct-tcpip.request` |
| `2026-08-15 10:49:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.22.51[.]64` to AbuseIPDB if not already reported
- [ ] Block `81.22.51[.]64` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d428a7fd1203

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-15 10:49 |
| **Last Seen** | 2026-08-15 10:49 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 10:49:05` | `cowrie.session.connect` |
| `2026-08-15 10:49:05` | `cowrie.client.version` |
| `2026-08-15 10:49:05` | `cowrie.client.kex` |
| `2026-08-15 10:49:07` | `cowrie.login.success` |
| `2026-08-15 10:49:08` | `cowrie.session.params` |
| `2026-08-15 10:49:08` | `cowrie.command.input` |
| `2026-08-15 10:49:08` | `cowrie.command.input` |
| `2026-08-15 10:49:08` | `cowrie.command.input` |
| `2026-08-15 10:49:08` | `cowrie.command.input` |
| `2026-08-15 10:49:08` | `cowrie.command.input` |
| `2026-08-15 10:49:08` | `cowrie.command.success` |
| `2026-08-15 10:49:08` | `cowrie.command.input` |
| `2026-08-15 10:49:08` | `cowrie.command.input` |
| `2026-08-15 10:49:08` | `cowrie.command.input` |
| `2026-08-15 10:49:08` | `cowrie.command.input` |
| `2026-08-15 10:49:09` | `cowrie.log.closed` |
| `2026-08-15 10:49:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e215858cd55f

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-15 10:50 |
| **Last Seen** | 2026-08-15 10:50 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 10:50:33` | `cowrie.session.connect` |
| `2026-08-15 10:50:33` | `cowrie.client.version` |
| `2026-08-15 10:50:33` | `cowrie.client.kex` |
| `2026-08-15 10:50:35` | `cowrie.login.success` |
| `2026-08-15 10:50:36` | `cowrie.session.params` |
| `2026-08-15 10:50:36` | `cowrie.command.input` |
| `2026-08-15 10:50:36` | `cowrie.command.input` |
| `2026-08-15 10:50:36` | `cowrie.command.input` |
| `2026-08-15 10:50:36` | `cowrie.command.input` |
| `2026-08-15 10:50:36` | `cowrie.command.input` |
| `2026-08-15 10:50:36` | `cowrie.command.success` |
| `2026-08-15 10:50:36` | `cowrie.command.input` |
| `2026-08-15 10:50:36` | `cowrie.command.input` |
| `2026-08-15 10:50:36` | `cowrie.command.input` |
| `2026-08-15 10:50:36` | `cowrie.command.input` |
| `2026-08-15 10:50:37` | `cowrie.log.closed` |
| `2026-08-15 10:50:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c2ddbd9e44eb

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-15 10:51 |
| **Last Seen** | 2026-08-15 10:52 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 10:51:59` | `cowrie.session.connect` |
| `2026-08-15 10:51:59` | `cowrie.client.version` |
| `2026-08-15 10:51:59` | `cowrie.client.kex` |
| `2026-08-15 10:52:00` | `cowrie.login.success` |
| `2026-08-15 10:52:02` | `cowrie.session.params` |
| `2026-08-15 10:52:02` | `cowrie.command.input` |
| `2026-08-15 10:52:02` | `cowrie.command.input` |
| `2026-08-15 10:52:02` | `cowrie.command.input` |
| `2026-08-15 10:52:02` | `cowrie.command.input` |
| `2026-08-15 10:52:02` | `cowrie.command.input` |
| `2026-08-15 10:52:02` | `cowrie.command.success` |
| `2026-08-15 10:52:02` | `cowrie.command.input` |
| `2026-08-15 10:52:02` | `cowrie.command.input` |
| `2026-08-15 10:52:02` | `cowrie.command.input` |
| `2026-08-15 10:52:02` | `cowrie.command.input` |
| `2026-08-15 10:52:02` | `cowrie.log.closed` |
| `2026-08-15 10:52:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e937b45f887

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-15 10:53 |
| **Last Seen** | 2026-08-15 10:53 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 10:53:22` | `cowrie.session.connect` |
| `2026-08-15 10:53:22` | `cowrie.client.version` |
| `2026-08-15 10:53:22` | `cowrie.client.kex` |
| `2026-08-15 10:53:24` | `cowrie.login.success` |
| `2026-08-15 10:53:25` | `cowrie.session.params` |
| `2026-08-15 10:53:25` | `cowrie.command.input` |
| `2026-08-15 10:53:25` | `cowrie.command.input` |
| `2026-08-15 10:53:25` | `cowrie.command.input` |
| `2026-08-15 10:53:25` | `cowrie.command.input` |
| `2026-08-15 10:53:25` | `cowrie.command.input` |
| `2026-08-15 10:53:25` | `cowrie.command.success` |
| `2026-08-15 10:53:25` | `cowrie.command.input` |
| `2026-08-15 10:53:25` | `cowrie.command.input` |
| `2026-08-15 10:53:25` | `cowrie.command.input` |
| `2026-08-15 10:53:25` | `cowrie.command.input` |
| `2026-08-15 10:53:25` | `cowrie.log.closed` |
| `2026-08-15 10:53:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8bc6b6e2878c

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-15 10:54 |
| **Last Seen** | 2026-08-15 10:54 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 10:54:46` | `cowrie.session.connect` |
| `2026-08-15 10:54:47` | `cowrie.client.version` |
| `2026-08-15 10:54:47` | `cowrie.client.kex` |
| `2026-08-15 10:54:48` | `cowrie.login.success` |
| `2026-08-15 10:54:49` | `cowrie.session.params` |
| `2026-08-15 10:54:49` | `cowrie.command.input` |
| `2026-08-15 10:54:49` | `cowrie.command.input` |
| `2026-08-15 10:54:49` | `cowrie.command.input` |
| `2026-08-15 10:54:49` | `cowrie.command.input` |
| `2026-08-15 10:54:49` | `cowrie.command.input` |
| `2026-08-15 10:54:49` | `cowrie.command.success` |
| `2026-08-15 10:54:49` | `cowrie.command.input` |
| `2026-08-15 10:54:49` | `cowrie.command.input` |
| `2026-08-15 10:54:49` | `cowrie.command.input` |
| `2026-08-15 10:54:49` | `cowrie.command.input` |
| `2026-08-15 10:54:49` | `cowrie.log.closed` |
| `2026-08-15 10:54:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `80.251.153[.]178` | **6135** | 2026-08-15 08:55 | 2026-08-15 10:55 | 7239m | 0 | `T1592` | 🟠 MEDIUM |
| `210.16.100[.]120` | **9** | 2026-08-15 09:40 | 2026-08-15 10:32 | 8m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **4** | 2026-08-15 09:12 | 2026-08-15 10:32 | 0m | 0 | `T1592` | 🟢 LOW |
| `152.32.190[.]84` | **4** | 2026-08-15 09:32 | 2026-08-15 09:33 | 0m | 0 | `T1592` | 🟢 LOW |
| `170.239.205[.]221` | **3** | 2026-08-15 10:19 | 2026-08-15 10:20 | 0m | 0 | `T1592` | 🟢 LOW |
| `172.236.228[.]229` | **3** | 2026-08-15 09:40 | 2026-08-15 09:40 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]161` | **3** | 2026-08-15 09:04 | 2026-08-15 09:04 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]167` | **3** | 2026-08-15 09:25 | 2026-08-15 09:25 | 0m | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]227` | **3** | 2026-08-15 09:03 | 2026-08-15 09:49 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `135.222.40[.]122` | **2** | 2026-08-15 10:12 | 2026-08-15 10:12 | 0m | 0 | `T1592` | 🟢 LOW |
| `136.116.129[.]132` | **2** | 2026-08-15 10:36 | 2026-08-15 10:37 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.79.181[.]179` | **2** | 2026-08-15 10:41 | 2026-08-15 10:41 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]199` | **2** | 2026-08-15 10:35 | 2026-08-15 10:35 | 0m | 0 | `T1592` | 🟢 LOW |
| `104.238.110[.]208` | 1 | 2026-08-15 10:12 | 2026-08-15 10:13 | 38s | 0 | `T1592` | 🟢 LOW |
| `107.150.146[.]69` | 1 | 2026-08-15 09:24 | 2026-08-15 09:24 | 35s | 0 | `T1592` | 🟢 LOW |
| `121.40.84[.]227` | 1 | 2026-08-15 10:32 | 2026-08-15 10:32 | 0s | 0 | `T1592` | 🟢 LOW |
| `125.69.76[.]148` | 1 | 2026-08-15 10:37 | 2026-08-15 10:39 | 120s | 0 | `T1592` | 🟢 LOW |
| `181.225.32[.]48` | 1 | 2026-08-15 09:38 | 2026-08-15 09:38 | 11s | 0 | `T1592` | 🟢 LOW |
| `181.46.39[.]138` | 1 | 2026-08-15 09:24 | 2026-08-15 09:24 | 0s | 0 | `T1592` | 🟢 LOW |
| `185.40.122[.]250` | 1 | 2026-08-15 08:55 | 2026-08-15 08:55 | 9s | 0 | `T1592` | 🟢 LOW |
| `2.55.85[.]4` | 1 | 2026-08-15 09:41 | 2026-08-15 09:41 | 10s | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]238` | 1 | 2026-08-15 09:53 | 2026-08-15 09:53 | 0s | 0 | `T1592` | 🟢 LOW |
| `203.110.233[.]225` | 1 | 2026-08-15 10:18 | 2026-08-15 10:20 | 120s | 0 | `T1592` | 🟢 LOW |
| `210.4.68[.]72` | 1 | 2026-08-15 08:56 | 2026-08-15 08:56 | 2s | 0 | `T1592` | 🟢 LOW |
| `217.150.37[.]249` | 1 | 2026-08-15 10:51 | 2026-08-15 10:52 | 25s | 0 | `T1592` | 🟢 LOW |
| `220.180.166[.]214` | 1 | 2026-08-15 09:41 | 2026-08-15 09:41 | 22s | 0 | `T1592` | 🟢 LOW |
| `39.183.162[.]243` | 1 | 2026-08-15 10:49 | 2026-08-15 10:49 | 22s | 0 | `T1592` | 🟢 LOW |
| `45.33.14[.]5` | 1 | 2026-08-15 09:40 | 2026-08-15 09:40 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.245.113[.]7` | 1 | 2026-08-15 10:03 | 2026-08-15 10:03 | 13s | 0 | `T1592` | 🟢 LOW |
| `95.59.110[.]78` | 1 | 2026-08-15 09:52 | 2026-08-15 09:53 | 13s | 0 | `T1592` | 🟢 LOW |

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
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 81/100 | 🔴 HIGH | **28/75** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 41/100 | 🟡 MEDIUM | **29/75** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **23/75** 🔴 |
| `1e70b63472772e3f5092ffe9c3573470e73590e6ab6d93fdcede1d368a5fd72d` | Bash Script | `1e70b63472772e3f...` | 60/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 54/100 | 🟡 MEDIUM | **35/75** 🔴 |
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
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `287962211de7bcadb39f7576732438b43ee6aab420ec23c29a9d12a8151a547f` | ELF Binary (Linux executable) (x86 32-bit) | `287962211de7bcad...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `2f206563640dd66a743ffd493ce0e3c31a8fc5a24b9f5d2b540fc22d45c13d66` | ELF Binary (Linux executable) (x86 32-bit) | `2f206563640dd66a...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `31d4181843b1ed10a7e7cb3f108f6d6c50a7a4452ee52ddacabe8ca77260615e` | Bash Script | `31d4181843b1ed10...` | 58/100 | 🟡 MEDIUM | **20/75** 🔴 |

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
| `95.59.110[.]78` | KZ | JSC Kazakhtelecom, Astana Affiliate, Metro Ethernet Network | **100** ⚠️ | 2 |
| `217.150.37[.]249` | RU | Joint Stock Company TransTeleCom | **100** ⚠️ | 50 |
| `121.40.84[.]227` | CN | Aliyun Computing Co., LTD | **100** ⚠️ | 50 |
| `45.33.14[.]5` | US | Linode | **100** ⚠️ | 50 |
| `67.85.146[.]216` | US | Optimum Online (Cablevision Systems) | **100** ⚠️ | 50 |
| `136.116.129[.]132` | US | Google LLC | **100** ⚠️ | 3 |
| `64.110.90[.]250` | KR | Oracle Corporation | **100** ⚠️ | 6 |
| `103.93.37[.]178` | IN | Ngc Broadband Pvt. Ltd. | **100** ⚠️ | 50 |
| `2.55.85[.]4` | IL | Partner Communications Ltd. | **100** ⚠️ | 7 |
| `107.150.146[.]69` | US | Internap Network Services Corporation | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 128 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 108 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 67 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 67 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 67 |

---

## 🔕 False Positive Summary (29 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 3 |
| AbuseIPDB score 15 below threshold 25 | 2 |
| AbuseIPDB score 16 below threshold 25 | 3 |
| AbuseIPDB score 19 below threshold 25 | 1 |
| AbuseIPDB score 24 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 17 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 6328 cases |
| Tool 34  | Credential Extractor        | ✅ 139 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 13 fingerprints |
| Tool 36  | Command Clustering          | ✅ 4 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 77 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 29 filtered (0.5%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 66 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 21 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 107 priority case(s) shown individually · 30 recon entry/entries in table (13 group(s) consolidating 6175 session(s)).

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
_Report time: 2026-08-15T12:42:55Z_

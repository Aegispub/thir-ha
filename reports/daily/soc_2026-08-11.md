# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-11 |
| **Generated At** | 2026-08-11T17:00:18Z |
| **Shift Time** | 17:00 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **194** |
| Confirmed Threats | **166** |
| False Positives Filtered | **28** (14.4%) |
| Unique Attacker IPs | **75** |
| Countries of Origin | **25** |
| High Severity Cases | **93** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **101** |
| Malware Samples Analyzed | **3** HIGH · **23** MED · 20 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **126** |
| Unique Credential Pairs | **90** |
| Unique Usernames | **39** |
| Unique Passwords | **70** |
| Successful Auth Pairs | **112** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 33 |
| `admin` | 22 |
| `centos` | 9 |
| `support` | 7 |
| `ubnt` | 6 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `nutanix/4u` | 12 |
| `123123123` | 7 |
| `123321` | 6 |
| `1q2w3e` | 5 |
| `123456` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `ubnt` | `123321` | 5 |
| `support` | `123123123` | 5 |
| `centos` | `1q2w3e` | 5 |
| `nutanix` | `nutanix/4u` | 4 |
| `admin` | `nutanix/4u` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `server` | `server` | `45.148.10.183` | 2026-08-11T14:56:14 |
| `ubnt` | `123321` | `10.0.0.73` | 2026-08-11T14:56:28 |
| `test` | `6666666` | `10.0.0.73` | 2026-08-11T14:57:26 |
| `root` | `1234567` | `92.118.39.71` | 2026-08-11T14:57:38 |
| `ubnt` | `123321` | `120.224.15.67` | 2026-08-11T14:58:09 |
| `ubnt` | `123321` | `178.216.165.187` | 2026-08-11T14:58:20 |
| `server` | `server@123` | `45.148.10.183` | 2026-08-11T14:58:59 |
| `root` | `12345678` | `92.118.39.71` | 2026-08-11T14:59:35 |
| `exx` | `exx@123` | `45.148.10.183` | 2026-08-11T15:01:44 |
| `root` | `123456789` | `92.118.39.71` | 2026-08-11T15:02:19 |
| `rosmadinor` | `rosmadinor` | `45.148.10.183` | 2026-08-11T15:04:38 |
| `root` | `1234567890` | `92.118.39.71` | 2026-08-11T15:05:42 |
| `radar` | `radar` | `45.148.10.183` | 2026-08-11T15:07:18 |
| `root` | `123456a` | `92.118.39.71` | 2026-08-11T15:07:49 |
| `root` | `123456b` | `92.118.39.71` | 2026-08-11T15:10:01 |
| `konica` | `konica` | `45.148.10.183` | 2026-08-11T15:10:10 |
| `root` | `123abc` | `92.118.39.71` | 2026-08-11T15:11:58 |
| `justin` | `justin` | `45.148.10.183` | 2026-08-11T15:12:53 |
| `root` | `123qwe` | `92.118.39.71` | 2026-08-11T15:13:54 |
| `ubnt` | `123321` | `93.241.232.14` | 2026-08-11T15:14:22 |
| `sybase` | `sybase` | `45.148.10.183` | 2026-08-11T15:15:37 |
| `root` | `1q2w3e4r` | `92.118.39.71` | 2026-08-11T15:15:49 |
| `test` | `6666666` | `186.215.107.189` | 2026-08-11T15:16:22 |
| `test` | `6666666` | `110.227.215.90` | 2026-08-11T15:16:33 |
| `root` | `555555` | `92.118.39.71` | 2026-08-11T15:17:47 |
| `delta` | `delta` | `45.148.10.183` | 2026-08-11T15:18:26 |
| `root` | `654321` | `92.118.39.71` | 2026-08-11T15:19:38 |
| `centos` | `123` | `37.46.160.175` | 2026-08-11T15:21:17 |
| `centos` | `123` | `58.56.128.190` | 2026-08-11T15:21:30 |
| `root` | `7777777` | `92.118.39.71` | 2026-08-11T15:21:38 |
| `root` | `abc123` | `92.118.39.71` | 2026-08-11T15:23:39 |
| `super` | `super` | `45.148.10.183` | 2026-08-11T15:24:00 |
| `root` | `LeitboGi0ro` | `140.245.50.204` | 2026-08-11T15:24:09 |
| `root` | `123@@@` | `140.245.50.204` | 2026-08-11T15:24:10 |
| `root` | `admin` | `92.118.39.71` | 2026-08-11T15:25:41 |
| `support` | `123123123` | `123.212.9.122` | 2026-08-11T15:26:41 |
| `support` | `123123123` | `211.247.127.250` | 2026-08-11T15:26:55 |
| `root` | `admin123` | `92.118.39.71` | 2026-08-11T15:27:39 |
| `sniper` | `sniper` | `45.148.10.183` | 2026-08-11T15:29:38 |
| `root` | `passw0rd` | `92.118.39.71` | 2026-08-11T15:29:43 |
| `root` | `password` | `92.118.39.71` | 2026-08-11T15:31:39 |
| `eve` | `eve` | `45.148.10.183` | 2026-08-11T15:32:26 |
| `config` | `p@ssw0rd` | `65.20.202.4` | 2026-08-11T15:32:30 |
| `root` | `password1` | `92.118.39.71` | 2026-08-11T15:33:32 |
| `ripple` | `ripple` | `45.148.10.183` | 2026-08-11T15:35:15 |
| `root` | `qwerty` | `92.118.39.71` | 2026-08-11T15:35:58 |
| `node` | `1234` | `45.148.10.183` | 2026-08-11T15:37:58 |
| `support` | `123123123` | `10.0.0.73` | 2026-08-11T15:38:29 |
| `root` | `welcome` | `92.118.39.71` | 2026-08-11T15:39:37 |
| `node` | `123456` | `45.148.10.183` | 2026-08-11T15:40:46 |
| `admin` | `000000` | `92.118.39.71` | 2026-08-11T15:41:31 |
| `xrpl` | `xrpl` | `45.148.10.183` | 2026-08-11T15:42:57 |
| `admin` | `111111` | `92.118.39.71` | 2026-08-11T15:43:24 |
| `nutanix` | `nutanix/4u` | `10.0.0.73` | 2026-08-11T15:44:51 |
| `claude` | `claude` | `45.148.10.183` | 2026-08-11T15:45:06 |
| `oneadmin` | `oneadmin` | `10.0.0.73` | 2026-08-11T15:45:15 |
| `admin` | `123` | `92.118.39.71` | 2026-08-11T15:45:35 |
| `oneadmin` | `opennebula` | `10.0.0.73` | 2026-08-11T15:45:37 |
| `nutanix` | `Nutanix/4u` | `10.0.0.73` | 2026-08-11T15:45:58 |
| `codex` | `codex` | `45.148.10.183` | 2026-08-11T15:47:15 |
| `admin` | `nutanix/4u` | `10.0.0.73` | 2026-08-11T15:47:21 |
| `admin` | `Nutanix/4u` | `10.0.0.73` | 2026-08-11T15:47:41 |
| `admin` | `123123` | `92.118.39.71` | 2026-08-11T15:48:21 |
| `root` | `nutanix/4u` | `10.0.0.73` | 2026-08-11T15:49:01 |
| `config` | `p@ssw0rd` | `178.178.194.192` | 2026-08-11T15:49:19 |
| `root` | `Nutanix/4u` | `10.0.0.73` | 2026-08-11T15:49:21 |
| `gemini` | `gemini` | `45.148.10.183` | 2026-08-11T15:49:25 |
| `admin` | `123321` | `92.118.39.71` | 2026-08-11T15:50:32 |
| `osmc` | `osmc` | `10.0.0.73` | 2026-08-11T15:50:41 |
| `cms` | `cms` | `10.0.0.73` | 2026-08-11T15:51:01 |
| `Admin` | `0000` | `70.89.116.5` | 2026-08-11T15:51:02 |
| `Admin` | `0000` | `31.173.2.182` | 2026-08-11T15:51:09 |
| `cims` | `cims` | `10.0.0.73` | 2026-08-11T15:51:21 |
| `validate` | `validate` | `45.148.10.183` | 2026-08-11T15:51:34 |
| `admin` | `1234` | `92.118.39.71` | 2026-08-11T15:53:05 |
| `deepseek` | `deepseek` | `45.148.10.183` | 2026-08-11T15:53:44 |
| `admin` | `12345` | `92.118.39.71` | 2026-08-11T15:54:51 |
| `support` | `123123123` | `61.2.44.54` | 2026-08-11T15:55:53 |
| `xrp` | `xrp` | `45.148.10.183` | 2026-08-11T15:55:55 |
| `support` | `123123123` | `125.20.207.154` | 2026-08-11T15:56:01 |
| `admin` | `123456` | `92.118.39.71` | 2026-08-11T15:56:41 |
| `devuser` | `devuser` | `45.148.10.183` | 2026-08-11T15:58:05 |
| `admin` | `1234567` | `92.118.39.71` | 2026-08-11T15:58:41 |
| `vyos` | `vyos` | `45.148.10.183` | 2026-08-11T16:00:17 |
| `default` | `Default2014` | `128.185.12.179` | 2026-08-11T16:01:12 |
| `admin` | `12345678` | `92.118.39.71` | 2026-08-11T16:01:16 |
| `default` | `Default2014` | `65.20.211.96` | 2026-08-11T16:01:21 |
| `harmony` | `harmony` | `45.148.10.183` | 2026-08-11T16:02:26 |
| `admin` | `123456789` | `92.118.39.71` | 2026-08-11T16:04:22 |
| `pool` | `pool` | `45.148.10.183` | 2026-08-11T16:04:34 |
| `support` | `support` | `10.0.0.73` | 2026-08-11T16:06:17 |
| `centos` | `1q2w3e` | `10.0.0.73` | 2026-08-11T16:06:25 |
| `admin` | `1234567890` | `92.118.39.71` | 2026-08-11T16:06:40 |
| `tt` | `tt` | `45.148.10.183` | 2026-08-11T16:06:44 |
| `centos` | `123123123` | `196.216.81.126` | 2026-08-11T16:07:20 |
| `centos` | `123123123` | `191.210.73.33` | 2026-08-11T16:07:32 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-08-11T16:08:02 |
| `root` | `123@@@` | `129.153.145.135` | 2026-08-11T16:08:03 |
| `admin` | `123456a` | `92.118.39.71` | 2026-08-11T16:08:27 |
| `admin` | `123qwe` | `92.118.39.71` | 2026-08-11T16:10:17 |
| `admin` | `1q2w3e4r` | `92.118.39.71` | 2026-08-11T16:12:32 |
| `default` | `Default2014` | `10.0.0.73` | 2026-08-11T16:12:51 |
| `admin` | `654321` | `92.118.39.71` | 2026-08-11T16:15:20 |
| `admin` | `7777777` | `92.118.39.71` | 2026-08-11T16:18:39 |
| `root` | `admin` | `94.154.43.99` | 2026-08-11T16:22:39 |
| `centos` | `1q2w3e` | `208.109.38.143` | 2026-08-11T16:25:06 |
| `centos` | `1q2w3e` | `186.215.107.189` | 2026-08-11T16:25:13 |
| `centos` | `1q2w3e` | `49.124.151.58` | 2026-08-11T16:25:21 |
| `test` | `555555` | `223.75.156.89` | 2026-08-11T16:35:38 |
| `ubnt` | `66666` | `10.0.0.73` | 2026-08-11T16:40:55 |
| `support` | `support` | `176.53.159.196` | 2026-08-11T16:46:54 |
| `root` | `12345678` | `10.0.0.73` | 2026-08-11T16:47:43 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **194** |
| Sessions with Fingerprint | **8** |
| Unique HASSH Fingerprints | **8** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 67 |
| OpenSSH | 24 |
| libssh | 6 |
| Paramiko (Python) | 4 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `2ec37a7cc8da...` | Mirai/variant | 38 | 1 |
| `16443846184e...` | Generic scanner | 27 | 1 |
| `acaa53e0a7d7...` | Mirai/variant | 24 | 23 |
| `a2de0f306611...` | Mirai/variant | 4 | 2 |
| `e37f354a101a...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `2ec37a7cc8da...` | Go SSH scanner | 38 | 1 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 27 | 1 | Generic scanner |
| `acaa53e0a7d7...` | OpenSSH | 24 | 23 | Mirai/variant |
| `95420f9d932d...` | libssh | 5 | 2 | — |
| `a2de0f306611...` | Paramiko (Python) | 4 | 2 | Mirai/variant |
| `e37f354a101a...` | libssh | 1 | 1 | Mirai/variant |
| `2aec6b44b06b...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 1 | 1 | Modern SSH client |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **2** |
| Campaign Clusters | **1** |
| Highest Severity | **MEDIUM** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 37 | 1 | `T1082, T1592, T1078, T1083` |

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
| Total IPs Analysed | **75** |
| Unique ASNs | **60** |
| High-Risk ASNs | **38** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS48721` | Flyservers S.A. | 4 | HIGH |
| `AS398324` | Censys, Inc. | 3 | HIGH |
| `AS9498` | BHARTI Airtel Ltd. | 2 | HIGH |
| `AS203214` | Hulum Almustakbal Company for Communication Engineering and Services Ltd | 2 | HIGH |
| `AS22773` | Cox Communications Inc. | 2 | MEDIUM |
| `AS136442` | Ocean Wave Communication Co., Ltd | 2 | LOW |
| `AS4134` | CHINANET BACKBONE | 2 | HIGH |
| `AS9808` | China Mobile Communications Group Co., Ltd. | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (93)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-a6445bac35ce

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-08-11 14:56 |
| **Last Seen** | 2026-08-11 14:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 14:56:14` | `cowrie.session.connect` |
| `2026-08-11 14:56:14` | `cowrie.client.version` |
| `2026-08-11 14:56:14` | `cowrie.client.kex` |
| `2026-08-11 14:56:14` | `cowrie.login.success` |
| `2026-08-11 14:56:15` | `cowrie.session.params` |
| `2026-08-11 14:56:15` | `cowrie.command.input` |
| `2026-08-11 14:56:15` | `cowrie.log.closed` |
| `2026-08-11 14:56:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1cdf65653133

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-11 14:57 |
| **Last Seen** | 2026-08-11 14:57 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 14:57:36` | `cowrie.session.connect` |
| `2026-08-11 14:57:36` | `cowrie.client.version` |
| `2026-08-11 14:57:36` | `cowrie.client.kex` |
| `2026-08-11 14:57:38` | `cowrie.login.success` |
| `2026-08-11 14:57:40` | `cowrie.session.params` |
| `2026-08-11 14:57:40` | `cowrie.command.input` |
| `2026-08-11 14:57:40` | `cowrie.command.input` |
| `2026-08-11 14:57:40` | `cowrie.command.input` |
| `2026-08-11 14:57:40` | `cowrie.command.input` |
| `2026-08-11 14:57:40` | `cowrie.command.input` |
| `2026-08-11 14:57:40` | `cowrie.command.success` |
| `2026-08-11 14:57:40` | `cowrie.command.input` |
| `2026-08-11 14:57:40` | `cowrie.command.input` |
| `2026-08-11 14:57:40` | `cowrie.command.input` |
| `2026-08-11 14:57:40` | `cowrie.command.input` |
| `2026-08-11 14:57:41` | `cowrie.log.closed` |
| `2026-08-11 14:57:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a869df121da

| Field | Detail |
|---|---|
| **Source IP** | `120.224.15[.]67` |
| **First Seen** | 2026-08-11 14:58 |
| **Last Seen** | 2026-08-11 14:58 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 14:58:05` | `cowrie.session.connect` |
| `2026-08-11 14:58:07` | `cowrie.client.version` |
| `2026-08-11 14:58:07` | `cowrie.client.kex` |
| `2026-08-11 14:58:09` | `cowrie.login.success` |
| `2026-08-11 14:58:10` | `cowrie.direct-tcpip.request` |
| `2026-08-11 14:58:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.224.15[.]67` to AbuseIPDB if not already reported
- [ ] Block `120.224.15[.]67` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dda34e2885ae

| Field | Detail |
|---|---|
| **Source IP** | `178.216.165[.]187` |
| **First Seen** | 2026-08-11 14:58 |
| **Last Seen** | 2026-08-11 14:58 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 14:58:19` | `cowrie.session.connect` |
| `2026-08-11 14:58:19` | `cowrie.client.version` |
| `2026-08-11 14:58:19` | `cowrie.client.kex` |
| `2026-08-11 14:58:20` | `cowrie.login.success` |
| `2026-08-11 14:58:21` | `cowrie.direct-tcpip.request` |
| `2026-08-11 14:58:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.216.165[.]187` to AbuseIPDB if not already reported
- [ ] Block `178.216.165[.]187` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-674932b28f0f

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-08-11 14:58 |
| **Last Seen** | 2026-08-11 14:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 14:58:59` | `cowrie.session.connect` |
| `2026-08-11 14:58:59` | `cowrie.client.version` |
| `2026-08-11 14:58:59` | `cowrie.client.kex` |
| `2026-08-11 14:58:59` | `cowrie.login.success` |
| `2026-08-11 14:59:00` | `cowrie.session.params` |
| `2026-08-11 14:59:00` | `cowrie.command.input` |
| `2026-08-11 14:59:00` | `cowrie.log.closed` |
| `2026-08-11 14:59:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29b2f3c445a2

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-11 14:59 |
| **Last Seen** | 2026-08-11 14:59 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 14:59:34` | `cowrie.session.connect` |
| `2026-08-11 14:59:34` | `cowrie.client.version` |
| `2026-08-11 14:59:34` | `cowrie.client.kex` |
| `2026-08-11 14:59:35` | `cowrie.login.success` |
| `2026-08-11 14:59:37` | `cowrie.session.params` |
| `2026-08-11 14:59:37` | `cowrie.command.input` |
| `2026-08-11 14:59:37` | `cowrie.command.input` |
| `2026-08-11 14:59:37` | `cowrie.command.input` |
| `2026-08-11 14:59:37` | `cowrie.command.input` |
| `2026-08-11 14:59:37` | `cowrie.command.input` |
| `2026-08-11 14:59:37` | `cowrie.command.success` |
| `2026-08-11 14:59:37` | `cowrie.command.input` |
| `2026-08-11 14:59:37` | `cowrie.command.input` |
| `2026-08-11 14:59:37` | `cowrie.command.input` |
| `2026-08-11 14:59:37` | `cowrie.command.input` |
| `2026-08-11 14:59:37` | `cowrie.log.closed` |
| `2026-08-11 14:59:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc65b40dde9a

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-08-11 15:01 |
| **Last Seen** | 2026-08-11 15:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 15:01:44` | `cowrie.session.connect` |
| `2026-08-11 15:01:44` | `cowrie.client.version` |
| `2026-08-11 15:01:44` | `cowrie.client.kex` |
| `2026-08-11 15:01:44` | `cowrie.login.success` |
| `2026-08-11 15:01:45` | `cowrie.session.params` |
| `2026-08-11 15:01:45` | `cowrie.command.input` |
| `2026-08-11 15:01:45` | `cowrie.log.closed` |
| `2026-08-11 15:01:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f26d60a2d66

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-11 15:02 |
| **Last Seen** | 2026-08-11 15:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 15:02:18` | `cowrie.session.connect` |
| `2026-08-11 15:02:18` | `cowrie.client.version` |
| `2026-08-11 15:02:19` | `cowrie.client.kex` |
| `2026-08-11 15:02:19` | `cowrie.login.success` |
| `2026-08-11 15:02:20` | `cowrie.session.params` |
| `2026-08-11 15:02:20` | `cowrie.command.input` |
| `2026-08-11 15:02:20` | `cowrie.command.input` |
| `2026-08-11 15:02:20` | `cowrie.command.input` |
| `2026-08-11 15:02:20` | `cowrie.command.input` |
| `2026-08-11 15:02:20` | `cowrie.command.input` |
| `2026-08-11 15:02:20` | `cowrie.command.success` |
| `2026-08-11 15:02:20` | `cowrie.command.input` |
| `2026-08-11 15:02:20` | `cowrie.command.input` |
| `2026-08-11 15:02:20` | `cowrie.command.input` |
| `2026-08-11 15:02:20` | `cowrie.command.input` |
| `2026-08-11 15:02:20` | `cowrie.log.closed` |
| `2026-08-11 15:02:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c62c6fcae877

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-08-11 15:04 |
| **Last Seen** | 2026-08-11 15:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 15:04:38` | `cowrie.session.connect` |
| `2026-08-11 15:04:38` | `cowrie.client.version` |
| `2026-08-11 15:04:38` | `cowrie.client.kex` |
| `2026-08-11 15:04:38` | `cowrie.login.success` |
| `2026-08-11 15:04:39` | `cowrie.session.params` |
| `2026-08-11 15:04:39` | `cowrie.command.input` |
| `2026-08-11 15:04:39` | `cowrie.log.closed` |
| `2026-08-11 15:04:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3666e1b1d2ca

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-11 15:05 |
| **Last Seen** | 2026-08-11 15:05 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 15:05:40` | `cowrie.session.connect` |
| `2026-08-11 15:05:40` | `cowrie.client.version` |
| `2026-08-11 15:05:40` | `cowrie.client.kex` |
| `2026-08-11 15:05:42` | `cowrie.login.success` |
| `2026-08-11 15:05:43` | `cowrie.session.params` |
| `2026-08-11 15:05:43` | `cowrie.command.input` |
| `2026-08-11 15:05:43` | `cowrie.command.input` |
| `2026-08-11 15:05:43` | `cowrie.command.input` |
| `2026-08-11 15:05:43` | `cowrie.command.input` |
| `2026-08-11 15:05:43` | `cowrie.command.input` |
| `2026-08-11 15:05:43` | `cowrie.command.success` |
| `2026-08-11 15:05:43` | `cowrie.command.input` |
| `2026-08-11 15:05:43` | `cowrie.command.input` |
| `2026-08-11 15:05:43` | `cowrie.command.input` |
| `2026-08-11 15:05:43` | `cowrie.command.input` |
| `2026-08-11 15:05:43` | `cowrie.log.closed` |
| `2026-08-11 15:05:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc638478546a

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-08-11 15:07 |
| **Last Seen** | 2026-08-11 15:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 15:07:17` | `cowrie.session.connect` |
| `2026-08-11 15:07:17` | `cowrie.client.version` |
| `2026-08-11 15:07:17` | `cowrie.client.kex` |
| `2026-08-11 15:07:18` | `cowrie.login.success` |
| `2026-08-11 15:07:18` | `cowrie.session.params` |
| `2026-08-11 15:07:18` | `cowrie.command.input` |
| `2026-08-11 15:07:18` | `cowrie.log.closed` |
| `2026-08-11 15:07:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b59e9240fcf

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-11 15:07 |
| **Last Seen** | 2026-08-11 15:07 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 15:07:48` | `cowrie.session.connect` |
| `2026-08-11 15:07:48` | `cowrie.client.version` |
| `2026-08-11 15:07:48` | `cowrie.client.kex` |
| `2026-08-11 15:07:49` | `cowrie.login.success` |
| `2026-08-11 15:07:50` | `cowrie.session.params` |
| `2026-08-11 15:07:50` | `cowrie.command.input` |
| `2026-08-11 15:07:50` | `cowrie.command.input` |
| `2026-08-11 15:07:50` | `cowrie.command.input` |
| `2026-08-11 15:07:50` | `cowrie.command.input` |
| `2026-08-11 15:07:50` | `cowrie.command.input` |
| `2026-08-11 15:07:50` | `cowrie.command.success` |
| `2026-08-11 15:07:50` | `cowrie.command.input` |
| `2026-08-11 15:07:50` | `cowrie.command.input` |
| `2026-08-11 15:07:50` | `cowrie.command.input` |
| `2026-08-11 15:07:50` | `cowrie.command.input` |
| `2026-08-11 15:07:51` | `cowrie.log.closed` |
| `2026-08-11 15:07:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce474aa61698

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-11 15:09 |
| **Last Seen** | 2026-08-11 15:10 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 15:09:59` | `cowrie.session.connect` |
| `2026-08-11 15:09:59` | `cowrie.client.version` |
| `2026-08-11 15:09:59` | `cowrie.client.kex` |
| `2026-08-11 15:10:01` | `cowrie.login.success` |
| `2026-08-11 15:10:02` | `cowrie.session.params` |
| `2026-08-11 15:10:02` | `cowrie.command.input` |
| `2026-08-11 15:10:02` | `cowrie.command.input` |
| `2026-08-11 15:10:02` | `cowrie.command.input` |
| `2026-08-11 15:10:02` | `cowrie.command.input` |
| `2026-08-11 15:10:02` | `cowrie.command.input` |
| `2026-08-11 15:10:02` | `cowrie.command.success` |
| `2026-08-11 15:10:02` | `cowrie.command.input` |
| `2026-08-11 15:10:02` | `cowrie.command.input` |
| `2026-08-11 15:10:02` | `cowrie.command.input` |
| `2026-08-11 15:10:02` | `cowrie.command.input` |
| `2026-08-11 15:10:03` | `cowrie.log.closed` |
| `2026-08-11 15:10:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-acdb26d1b82d

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-08-11 15:10 |
| **Last Seen** | 2026-08-11 15:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 15:10:10` | `cowrie.session.connect` |
| `2026-08-11 15:10:10` | `cowrie.client.version` |
| `2026-08-11 15:10:10` | `cowrie.client.kex` |
| `2026-08-11 15:10:10` | `cowrie.login.success` |
| `2026-08-11 15:10:11` | `cowrie.session.params` |
| `2026-08-11 15:10:11` | `cowrie.command.input` |
| `2026-08-11 15:10:11` | `cowrie.log.closed` |
| `2026-08-11 15:10:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a10e9d8a229

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-11 15:11 |
| **Last Seen** | 2026-08-11 15:12 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 15:11:56` | `cowrie.session.connect` |
| `2026-08-11 15:11:57` | `cowrie.client.version` |
| `2026-08-11 15:11:57` | `cowrie.client.kex` |
| `2026-08-11 15:11:58` | `cowrie.login.success` |
| `2026-08-11 15:12:00` | `cowrie.session.params` |
| `2026-08-11 15:12:00` | `cowrie.command.input` |
| `2026-08-11 15:12:00` | `cowrie.command.input` |
| `2026-08-11 15:12:00` | `cowrie.command.input` |
| `2026-08-11 15:12:00` | `cowrie.command.input` |
| `2026-08-11 15:12:00` | `cowrie.command.input` |
| `2026-08-11 15:12:00` | `cowrie.command.success` |
| `2026-08-11 15:12:00` | `cowrie.command.input` |
| `2026-08-11 15:12:00` | `cowrie.command.input` |
| `2026-08-11 15:12:00` | `cowrie.command.input` |
| `2026-08-11 15:12:00` | `cowrie.command.input` |
| `2026-08-11 15:12:00` | `cowrie.log.closed` |
| `2026-08-11 15:12:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95109848dd17

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-08-11 15:12 |
| **Last Seen** | 2026-08-11 15:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 15:12:52` | `cowrie.session.connect` |
| `2026-08-11 15:12:52` | `cowrie.client.version` |
| `2026-08-11 15:12:52` | `cowrie.client.kex` |
| `2026-08-11 15:12:53` | `cowrie.login.success` |
| `2026-08-11 15:12:54` | `cowrie.session.params` |
| `2026-08-11 15:12:54` | `cowrie.command.input` |
| `2026-08-11 15:12:54` | `cowrie.log.closed` |
| `2026-08-11 15:12:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9df8ad1eaee1

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-11 15:13 |
| **Last Seen** | 2026-08-11 15:13 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 15:13:53` | `cowrie.session.connect` |
| `2026-08-11 15:13:53` | `cowrie.client.version` |
| `2026-08-11 15:13:53` | `cowrie.client.kex` |
| `2026-08-11 15:13:54` | `cowrie.login.success` |
| `2026-08-11 15:13:55` | `cowrie.session.params` |
| `2026-08-11 15:13:55` | `cowrie.command.input` |
| `2026-08-11 15:13:55` | `cowrie.command.input` |
| `2026-08-11 15:13:55` | `cowrie.command.input` |
| `2026-08-11 15:13:55` | `cowrie.command.input` |
| `2026-08-11 15:13:55` | `cowrie.command.input` |
| `2026-08-11 15:13:55` | `cowrie.command.success` |
| `2026-08-11 15:13:55` | `cowrie.command.input` |
| `2026-08-11 15:13:55` | `cowrie.command.input` |
| `2026-08-11 15:13:55` | `cowrie.command.input` |
| `2026-08-11 15:13:55` | `cowrie.command.input` |
| `2026-08-11 15:13:56` | `cowrie.log.closed` |
| `2026-08-11 15:13:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b335a4116c6

| Field | Detail |
|---|---|
| **Source IP** | `93.241.232[.]14` |
| **First Seen** | 2026-08-11 15:14 |
| **Last Seen** | 2026-08-11 15:14 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 15:14:21` | `cowrie.session.connect` |
| `2026-08-11 15:14:21` | `cowrie.client.version` |
| `2026-08-11 15:14:21` | `cowrie.client.kex` |
| `2026-08-11 15:14:22` | `cowrie.login.success` |
| `2026-08-11 15:14:22` | `cowrie.direct-tcpip.request` |
| `2026-08-11 15:14:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.241.232[.]14` to AbuseIPDB if not already reported
- [ ] Block `93.241.232[.]14` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3f47ea3799d

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-08-11 15:15 |
| **Last Seen** | 2026-08-11 15:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 15:15:37` | `cowrie.session.connect` |
| `2026-08-11 15:15:37` | `cowrie.client.version` |
| `2026-08-11 15:15:37` | `cowrie.client.kex` |
| `2026-08-11 15:15:37` | `cowrie.login.success` |
| `2026-08-11 15:15:38` | `cowrie.session.params` |
| `2026-08-11 15:15:38` | `cowrie.command.input` |
| `2026-08-11 15:15:38` | `cowrie.log.closed` |
| `2026-08-11 15:15:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c2649f53cf8

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-11 15:15 |
| **Last Seen** | 2026-08-11 15:15 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 15:15:47` | `cowrie.session.connect` |
| `2026-08-11 15:15:47` | `cowrie.client.version` |
| `2026-08-11 15:15:47` | `cowrie.client.kex` |
| `2026-08-11 15:15:49` | `cowrie.login.success` |
| `2026-08-11 15:15:50` | `cowrie.session.params` |
| `2026-08-11 15:15:50` | `cowrie.command.input` |
| `2026-08-11 15:15:50` | `cowrie.command.input` |
| `2026-08-11 15:15:50` | `cowrie.command.input` |
| `2026-08-11 15:15:51` | `cowrie.command.input` |
| `2026-08-11 15:15:51` | `cowrie.command.input` |
| `2026-08-11 15:15:51` | `cowrie.command.success` |
| `2026-08-11 15:15:51` | `cowrie.command.input` |
| `2026-08-11 15:15:51` | `cowrie.command.input` |
| `2026-08-11 15:15:51` | `cowrie.command.input` |
| `2026-08-11 15:15:51` | `cowrie.command.input` |
| `2026-08-11 15:15:51` | `cowrie.log.closed` |
| `2026-08-11 15:15:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-62b2a9d4e67a

| Field | Detail |
|---|---|
| **Source IP** | `186.215.107[.]189` |
| **First Seen** | 2026-08-11 15:16 |
| **Last Seen** | 2026-08-11 15:16 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 15:16:19` | `cowrie.session.connect` |
| `2026-08-11 15:16:20` | `cowrie.client.version` |
| `2026-08-11 15:16:20` | `cowrie.client.kex` |
| `2026-08-11 15:16:22` | `cowrie.login.success` |
| `2026-08-11 15:16:22` | `cowrie.direct-tcpip.request` |
| `2026-08-11 15:16:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.215.107[.]189` to AbuseIPDB if not already reported
- [ ] Block `186.215.107[.]189` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7eceb661ce51

| Field | Detail |
|---|---|
| **Source IP** | `110.227.215[.]90` |
| **First Seen** | 2026-08-11 15:16 |
| **Last Seen** | 2026-08-11 15:16 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 15:16:32` | `cowrie.session.connect` |
| `2026-08-11 15:16:32` | `cowrie.client.version` |
| `2026-08-11 15:16:32` | `cowrie.client.kex` |
| `2026-08-11 15:16:33` | `cowrie.login.success` |
| `2026-08-11 15:16:34` | `cowrie.direct-tcpip.request` |
| `2026-08-11 15:16:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.227.215[.]90` to AbuseIPDB if not already reported
- [ ] Block `110.227.215[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09a66d35e35e

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-11 15:17 |
| **Last Seen** | 2026-08-11 15:17 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 15:17:45` | `cowrie.session.connect` |
| `2026-08-11 15:17:45` | `cowrie.client.version` |
| `2026-08-11 15:17:45` | `cowrie.client.kex` |
| `2026-08-11 15:17:47` | `cowrie.login.success` |
| `2026-08-11 15:17:48` | `cowrie.session.params` |
| `2026-08-11 15:17:48` | `cowrie.command.input` |
| `2026-08-11 15:17:48` | `cowrie.command.input` |
| `2026-08-11 15:17:48` | `cowrie.command.input` |
| `2026-08-11 15:17:48` | `cowrie.command.input` |
| `2026-08-11 15:17:48` | `cowrie.command.input` |
| `2026-08-11 15:17:48` | `cowrie.command.success` |
| `2026-08-11 15:17:48` | `cowrie.command.input` |
| `2026-08-11 15:17:48` | `cowrie.command.input` |
| `2026-08-11 15:17:48` | `cowrie.command.input` |
| `2026-08-11 15:17:48` | `cowrie.command.input` |
| `2026-08-11 15:17:49` | `cowrie.log.closed` |
| `2026-08-11 15:17:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08bb22b3782c

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-08-11 15:18 |
| **Last Seen** | 2026-08-11 15:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 15:18:25` | `cowrie.session.connect` |
| `2026-08-11 15:18:25` | `cowrie.client.version` |
| `2026-08-11 15:18:26` | `cowrie.client.kex` |
| `2026-08-11 15:18:26` | `cowrie.login.success` |
| `2026-08-11 15:18:27` | `cowrie.session.params` |
| `2026-08-11 15:18:27` | `cowrie.command.input` |
| `2026-08-11 15:18:27` | `cowrie.log.closed` |
| `2026-08-11 15:18:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4a189933973

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-11 15:19 |
| **Last Seen** | 2026-08-11 15:19 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 15:19:36` | `cowrie.session.connect` |
| `2026-08-11 15:19:36` | `cowrie.client.version` |
| `2026-08-11 15:19:36` | `cowrie.client.kex` |
| `2026-08-11 15:19:38` | `cowrie.login.success` |
| `2026-08-11 15:19:39` | `cowrie.session.params` |
| `2026-08-11 15:19:39` | `cowrie.command.input` |
| `2026-08-11 15:19:39` | `cowrie.command.input` |
| `2026-08-11 15:19:39` | `cowrie.command.input` |
| `2026-08-11 15:19:39` | `cowrie.command.input` |
| `2026-08-11 15:19:39` | `cowrie.command.input` |
| `2026-08-11 15:19:39` | `cowrie.command.success` |
| `2026-08-11 15:19:39` | `cowrie.command.input` |
| `2026-08-11 15:19:39` | `cowrie.command.input` |
| `2026-08-11 15:19:39` | `cowrie.command.input` |
| `2026-08-11 15:19:39` | `cowrie.command.input` |
| `2026-08-11 15:19:40` | `cowrie.log.closed` |
| `2026-08-11 15:19:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b53a62c6a199

| Field | Detail |
|---|---|
| **Source IP** | `37.46.160[.]175` |
| **First Seen** | 2026-08-11 15:21 |
| **Last Seen** | 2026-08-11 15:21 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 15:21:16` | `cowrie.session.connect` |
| `2026-08-11 15:21:16` | `cowrie.client.version` |
| `2026-08-11 15:21:16` | `cowrie.client.kex` |
| `2026-08-11 15:21:17` | `cowrie.login.success` |
| `2026-08-11 15:21:17` | `cowrie.direct-tcpip.request` |
| `2026-08-11 15:21:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `37.46.160[.]175` to AbuseIPDB if not already reported
- [ ] Block `37.46.160[.]175` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d7f6374c558

| Field | Detail |
|---|---|
| **Source IP** | `58.56.128[.]190` |
| **First Seen** | 2026-08-11 15:21 |
| **Last Seen** | 2026-08-11 15:21 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 15:21:27` | `cowrie.session.connect` |
| `2026-08-11 15:21:27` | `cowrie.client.version` |
| `2026-08-11 15:21:27` | `cowrie.client.kex` |
| `2026-08-11 15:21:30` | `cowrie.login.success` |
| `2026-08-11 15:21:31` | `cowrie.direct-tcpip.request` |
| `2026-08-11 15:21:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.56.128[.]190` to AbuseIPDB if not already reported
- [ ] Block `58.56.128[.]190` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71f2aa6de91a

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-11 15:21 |
| **Last Seen** | 2026-08-11 15:21 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 15:21:36` | `cowrie.session.connect` |
| `2026-08-11 15:21:36` | `cowrie.client.version` |
| `2026-08-11 15:21:36` | `cowrie.client.kex` |
| `2026-08-11 15:21:38` | `cowrie.login.success` |
| `2026-08-11 15:21:39` | `cowrie.session.params` |
| `2026-08-11 15:21:39` | `cowrie.command.input` |
| `2026-08-11 15:21:39` | `cowrie.command.input` |
| `2026-08-11 15:21:39` | `cowrie.command.input` |
| `2026-08-11 15:21:39` | `cowrie.command.input` |
| `2026-08-11 15:21:39` | `cowrie.command.input` |
| `2026-08-11 15:21:39` | `cowrie.command.success` |
| `2026-08-11 15:21:39` | `cowrie.command.input` |
| `2026-08-11 15:21:39` | `cowrie.command.input` |
| `2026-08-11 15:21:39` | `cowrie.command.input` |
| `2026-08-11 15:21:39` | `cowrie.command.input` |
| `2026-08-11 15:21:39` | `cowrie.log.closed` |
| `2026-08-11 15:21:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4326926e5216

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-11 15:23 |
| **Last Seen** | 2026-08-11 15:23 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 15:23:37` | `cowrie.session.connect` |
| `2026-08-11 15:23:37` | `cowrie.client.version` |
| `2026-08-11 15:23:37` | `cowrie.client.kex` |
| `2026-08-11 15:23:39` | `cowrie.login.success` |
| `2026-08-11 15:23:40` | `cowrie.session.params` |
| `2026-08-11 15:23:40` | `cowrie.command.input` |
| `2026-08-11 15:23:40` | `cowrie.command.input` |
| `2026-08-11 15:23:40` | `cowrie.command.input` |
| `2026-08-11 15:23:40` | `cowrie.command.input` |
| `2026-08-11 15:23:40` | `cowrie.command.input` |
| `2026-08-11 15:23:40` | `cowrie.command.success` |
| `2026-08-11 15:23:40` | `cowrie.command.input` |
| `2026-08-11 15:23:40` | `cowrie.command.input` |
| `2026-08-11 15:23:40` | `cowrie.command.input` |
| `2026-08-11 15:23:40` | `cowrie.command.input` |
| `2026-08-11 15:23:41` | `cowrie.log.closed` |
| `2026-08-11 15:23:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7ba7e961df5

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-08-11 15:24 |
| **Last Seen** | 2026-08-11 15:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 15:24:00` | `cowrie.session.connect` |
| `2026-08-11 15:24:00` | `cowrie.client.version` |
| `2026-08-11 15:24:00` | `cowrie.client.kex` |
| `2026-08-11 15:24:00` | `cowrie.login.success` |
| `2026-08-11 15:24:01` | `cowrie.session.params` |
| `2026-08-11 15:24:01` | `cowrie.command.input` |
| `2026-08-11 15:24:01` | `cowrie.log.closed` |
| `2026-08-11 15:24:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15b705fc86d3

| Field | Detail |
|---|---|
| **Source IP** | `140.245.50[.]204` |
| **First Seen** | 2026-08-11 15:24 |
| **Last Seen** | 2026-08-11 15:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 15:24:08` | `cowrie.session.connect` |
| `2026-08-11 15:24:08` | `cowrie.client.version` |
| `2026-08-11 15:24:08` | `cowrie.client.kex` |
| `2026-08-11 15:24:09` | `cowrie.login.success` |
| `2026-08-11 15:24:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.245.50[.]204` to AbuseIPDB if not already reported
- [ ] Block `140.245.50[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78a1a03f4ddb

| Field | Detail |
|---|---|
| **Source IP** | `140.245.50[.]204` |
| **First Seen** | 2026-08-11 15:24 |
| **Last Seen** | 2026-08-11 15:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 15:24:09` | `cowrie.session.connect` |
| `2026-08-11 15:24:09` | `cowrie.client.version` |
| `2026-08-11 15:24:09` | `cowrie.client.kex` |
| `2026-08-11 15:24:10` | `cowrie.login.success` |
| `2026-08-11 15:24:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.245.50[.]204` to AbuseIPDB if not already reported
- [ ] Block `140.245.50[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34cb21cd58d1

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-11 15:25 |
| **Last Seen** | 2026-08-11 15:25 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 15:25:40` | `cowrie.session.connect` |
| `2026-08-11 15:25:40` | `cowrie.client.version` |
| `2026-08-11 15:25:40` | `cowrie.client.kex` |
| `2026-08-11 15:25:41` | `cowrie.login.success` |
| `2026-08-11 15:25:42` | `cowrie.session.params` |
| `2026-08-11 15:25:42` | `cowrie.command.input` |
| `2026-08-11 15:25:42` | `cowrie.command.input` |
| `2026-08-11 15:25:42` | `cowrie.command.input` |
| `2026-08-11 15:25:42` | `cowrie.command.input` |
| `2026-08-11 15:25:42` | `cowrie.command.input` |
| `2026-08-11 15:25:42` | `cowrie.command.success` |
| `2026-08-11 15:25:42` | `cowrie.command.input` |
| `2026-08-11 15:25:42` | `cowrie.command.input` |
| `2026-08-11 15:25:42` | `cowrie.command.input` |
| `2026-08-11 15:25:42` | `cowrie.command.input` |
| `2026-08-11 15:25:42` | `cowrie.log.closed` |
| `2026-08-11 15:25:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe8c2c968d6b

| Field | Detail |
|---|---|
| **Source IP** | `123.212.9[.]122` |
| **First Seen** | 2026-08-11 15:26 |
| **Last Seen** | 2026-08-11 15:26 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 15:26:38` | `cowrie.session.connect` |
| `2026-08-11 15:26:39` | `cowrie.client.version` |
| `2026-08-11 15:26:39` | `cowrie.client.kex` |
| `2026-08-11 15:26:41` | `cowrie.login.success` |
| `2026-08-11 15:26:42` | `cowrie.direct-tcpip.request` |
| `2026-08-11 15:26:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `123.212.9[.]122` to AbuseIPDB if not already reported
- [ ] Block `123.212.9[.]122` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e5b809ffec6

| Field | Detail |
|---|---|
| **Source IP** | `211.247.127[.]250` |
| **First Seen** | 2026-08-11 15:26 |
| **Last Seen** | 2026-08-11 15:27 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 15:26:52` | `cowrie.session.connect` |
| `2026-08-11 15:26:52` | `cowrie.client.version` |
| `2026-08-11 15:26:52` | `cowrie.client.kex` |
| `2026-08-11 15:26:55` | `cowrie.login.success` |
| `2026-08-11 15:26:55` | `cowrie.direct-tcpip.request` |
| `2026-08-11 15:27:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.247.127[.]250` to AbuseIPDB if not already reported
- [ ] Block `211.247.127[.]250` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51d914bc87f8

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-11 15:27 |
| **Last Seen** | 2026-08-11 15:27 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 15:27:37` | `cowrie.session.connect` |
| `2026-08-11 15:27:38` | `cowrie.client.version` |
| `2026-08-11 15:27:38` | `cowrie.client.kex` |
| `2026-08-11 15:27:39` | `cowrie.login.success` |
| `2026-08-11 15:27:40` | `cowrie.session.params` |
| `2026-08-11 15:27:40` | `cowrie.command.input` |
| `2026-08-11 15:27:40` | `cowrie.command.input` |
| `2026-08-11 15:27:40` | `cowrie.command.input` |
| `2026-08-11 15:27:40` | `cowrie.command.input` |
| `2026-08-11 15:27:40` | `cowrie.command.input` |
| `2026-08-11 15:27:40` | `cowrie.command.success` |
| `2026-08-11 15:27:40` | `cowrie.command.input` |
| `2026-08-11 15:27:40` | `cowrie.command.input` |
| `2026-08-11 15:27:40` | `cowrie.command.input` |
| `2026-08-11 15:27:40` | `cowrie.command.input` |
| `2026-08-11 15:27:41` | `cowrie.log.closed` |
| `2026-08-11 15:27:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9270300715a1

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-08-11 15:29 |
| **Last Seen** | 2026-08-11 15:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 15:29:38` | `cowrie.session.connect` |
| `2026-08-11 15:29:38` | `cowrie.client.version` |
| `2026-08-11 15:29:38` | `cowrie.client.kex` |
| `2026-08-11 15:29:38` | `cowrie.login.success` |
| `2026-08-11 15:29:39` | `cowrie.session.params` |
| `2026-08-11 15:29:39` | `cowrie.command.input` |
| `2026-08-11 15:29:39` | `cowrie.log.closed` |
| `2026-08-11 15:29:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-390a2f9018d8

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-11 15:29 |
| **Last Seen** | 2026-08-11 15:29 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 15:29:41` | `cowrie.session.connect` |
| `2026-08-11 15:29:41` | `cowrie.client.version` |
| `2026-08-11 15:29:41` | `cowrie.client.kex` |
| `2026-08-11 15:29:43` | `cowrie.login.success` |
| `2026-08-11 15:29:45` | `cowrie.session.params` |
| `2026-08-11 15:29:45` | `cowrie.command.input` |
| `2026-08-11 15:29:45` | `cowrie.command.input` |
| `2026-08-11 15:29:45` | `cowrie.command.input` |
| `2026-08-11 15:29:45` | `cowrie.command.input` |
| `2026-08-11 15:29:45` | `cowrie.command.input` |
| `2026-08-11 15:29:45` | `cowrie.command.success` |
| `2026-08-11 15:29:45` | `cowrie.command.input` |
| `2026-08-11 15:29:45` | `cowrie.command.input` |
| `2026-08-11 15:29:45` | `cowrie.command.input` |
| `2026-08-11 15:29:45` | `cowrie.command.input` |
| `2026-08-11 15:29:45` | `cowrie.log.closed` |
| `2026-08-11 15:29:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e31d1c4fa56

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-11 15:31 |
| **Last Seen** | 2026-08-11 15:31 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 15:31:37` | `cowrie.session.connect` |
| `2026-08-11 15:31:37` | `cowrie.client.version` |
| `2026-08-11 15:31:37` | `cowrie.client.kex` |
| `2026-08-11 15:31:39` | `cowrie.login.success` |
| `2026-08-11 15:31:40` | `cowrie.session.params` |
| `2026-08-11 15:31:40` | `cowrie.command.input` |
| `2026-08-11 15:31:40` | `cowrie.command.input` |
| `2026-08-11 15:31:40` | `cowrie.command.input` |
| `2026-08-11 15:31:40` | `cowrie.command.input` |
| `2026-08-11 15:31:40` | `cowrie.command.input` |
| `2026-08-11 15:31:40` | `cowrie.command.success` |
| `2026-08-11 15:31:40` | `cowrie.command.input` |
| `2026-08-11 15:31:40` | `cowrie.command.input` |
| `2026-08-11 15:31:40` | `cowrie.command.input` |
| `2026-08-11 15:31:40` | `cowrie.command.input` |
| `2026-08-11 15:31:40` | `cowrie.log.closed` |
| `2026-08-11 15:31:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c3f676489a7

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-08-11 15:32 |
| **Last Seen** | 2026-08-11 15:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 15:32:26` | `cowrie.session.connect` |
| `2026-08-11 15:32:26` | `cowrie.client.version` |
| `2026-08-11 15:32:26` | `cowrie.client.kex` |
| `2026-08-11 15:32:26` | `cowrie.login.success` |
| `2026-08-11 15:32:27` | `cowrie.session.params` |
| `2026-08-11 15:32:27` | `cowrie.command.input` |
| `2026-08-11 15:32:27` | `cowrie.log.closed` |
| `2026-08-11 15:32:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82808f3313d6

| Field | Detail |
|---|---|
| **Source IP** | `65.20.202[.]4` |
| **First Seen** | 2026-08-11 15:32 |
| **Last Seen** | 2026-08-11 15:32 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 15:32:28` | `cowrie.session.connect` |
| `2026-08-11 15:32:29` | `cowrie.client.version` |
| `2026-08-11 15:32:29` | `cowrie.client.kex` |
| `2026-08-11 15:32:30` | `cowrie.login.success` |
| `2026-08-11 15:32:30` | `cowrie.direct-tcpip.request` |
| `2026-08-11 15:32:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.202[.]4` to AbuseIPDB if not already reported
- [ ] Block `65.20.202[.]4` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1fc91af6da93

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-11 15:33 |
| **Last Seen** | 2026-08-11 15:33 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 15:33:31` | `cowrie.session.connect` |
| `2026-08-11 15:33:31` | `cowrie.client.version` |
| `2026-08-11 15:33:31` | `cowrie.client.kex` |
| `2026-08-11 15:33:32` | `cowrie.login.success` |
| `2026-08-11 15:33:33` | `cowrie.session.params` |
| `2026-08-11 15:33:33` | `cowrie.command.input` |
| `2026-08-11 15:33:33` | `cowrie.command.input` |
| `2026-08-11 15:33:33` | `cowrie.command.input` |
| `2026-08-11 15:33:33` | `cowrie.command.input` |
| `2026-08-11 15:33:33` | `cowrie.command.input` |
| `2026-08-11 15:33:33` | `cowrie.command.success` |
| `2026-08-11 15:33:33` | `cowrie.command.input` |
| `2026-08-11 15:33:33` | `cowrie.command.input` |
| `2026-08-11 15:33:33` | `cowrie.command.input` |
| `2026-08-11 15:33:33` | `cowrie.command.input` |
| `2026-08-11 15:33:34` | `cowrie.log.closed` |
| `2026-08-11 15:33:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17733f1f7ef3

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-08-11 15:35 |
| **Last Seen** | 2026-08-11 15:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 15:35:15` | `cowrie.session.connect` |
| `2026-08-11 15:35:15` | `cowrie.client.version` |
| `2026-08-11 15:35:15` | `cowrie.client.kex` |
| `2026-08-11 15:35:15` | `cowrie.login.success` |
| `2026-08-11 15:35:16` | `cowrie.session.params` |
| `2026-08-11 15:35:16` | `cowrie.command.input` |
| `2026-08-11 15:35:16` | `cowrie.log.closed` |
| `2026-08-11 15:35:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec49c1031ca1

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-11 15:35 |
| **Last Seen** | 2026-08-11 15:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 15:35:58` | `cowrie.session.connect` |
| `2026-08-11 15:35:58` | `cowrie.client.version` |
| `2026-08-11 15:35:58` | `cowrie.client.kex` |
| `2026-08-11 15:35:58` | `cowrie.login.success` |
| `2026-08-11 15:35:59` | `cowrie.session.params` |
| `2026-08-11 15:35:59` | `cowrie.command.input` |
| `2026-08-11 15:35:59` | `cowrie.command.input` |
| `2026-08-11 15:35:59` | `cowrie.command.input` |
| `2026-08-11 15:35:59` | `cowrie.command.input` |
| `2026-08-11 15:35:59` | `cowrie.command.input` |
| `2026-08-11 15:35:59` | `cowrie.command.success` |
| `2026-08-11 15:35:59` | `cowrie.command.input` |
| `2026-08-11 15:35:59` | `cowrie.command.input` |
| `2026-08-11 15:35:59` | `cowrie.command.input` |
| `2026-08-11 15:35:59` | `cowrie.command.input` |
| `2026-08-11 15:35:59` | `cowrie.log.closed` |
| `2026-08-11 15:35:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb538bb673ac

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-08-11 15:37 |
| **Last Seen** | 2026-08-11 15:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 15:37:57` | `cowrie.session.connect` |
| `2026-08-11 15:37:57` | `cowrie.client.version` |
| `2026-08-11 15:37:58` | `cowrie.client.kex` |
| `2026-08-11 15:37:58` | `cowrie.login.success` |
| `2026-08-11 15:37:59` | `cowrie.session.params` |
| `2026-08-11 15:37:59` | `cowrie.command.input` |
| `2026-08-11 15:37:59` | `cowrie.log.closed` |
| `2026-08-11 15:37:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c849d07e24f8

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-11 15:39 |
| **Last Seen** | 2026-08-11 15:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 15:39:37` | `cowrie.session.connect` |
| `2026-08-11 15:39:37` | `cowrie.client.version` |
| `2026-08-11 15:39:37` | `cowrie.client.kex` |
| `2026-08-11 15:39:37` | `cowrie.login.success` |
| `2026-08-11 15:39:38` | `cowrie.session.params` |
| `2026-08-11 15:39:38` | `cowrie.command.input` |
| `2026-08-11 15:39:38` | `cowrie.command.input` |
| `2026-08-11 15:39:38` | `cowrie.command.input` |
| `2026-08-11 15:39:38` | `cowrie.command.input` |
| `2026-08-11 15:39:38` | `cowrie.command.input` |
| `2026-08-11 15:39:38` | `cowrie.command.success` |
| `2026-08-11 15:39:38` | `cowrie.command.input` |
| `2026-08-11 15:39:38` | `cowrie.command.input` |
| `2026-08-11 15:39:38` | `cowrie.command.input` |
| `2026-08-11 15:39:38` | `cowrie.command.input` |
| `2026-08-11 15:39:38` | `cowrie.log.closed` |
| `2026-08-11 15:39:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-721b7b86889b

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-08-11 15:40 |
| **Last Seen** | 2026-08-11 15:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 15:40:45` | `cowrie.session.connect` |
| `2026-08-11 15:40:45` | `cowrie.client.version` |
| `2026-08-11 15:40:45` | `cowrie.client.kex` |
| `2026-08-11 15:40:46` | `cowrie.login.success` |
| `2026-08-11 15:40:46` | `cowrie.session.params` |
| `2026-08-11 15:40:46` | `cowrie.command.input` |
| `2026-08-11 15:40:46` | `cowrie.log.closed` |
| `2026-08-11 15:40:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34824e4b4ddc

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-11 15:41 |
| **Last Seen** | 2026-08-11 15:41 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 15:41:29` | `cowrie.session.connect` |
| `2026-08-11 15:41:29` | `cowrie.client.version` |
| `2026-08-11 15:41:29` | `cowrie.client.kex` |
| `2026-08-11 15:41:31` | `cowrie.login.success` |
| `2026-08-11 15:41:33` | `cowrie.session.params` |
| `2026-08-11 15:41:33` | `cowrie.command.input` |
| `2026-08-11 15:41:33` | `cowrie.command.input` |
| `2026-08-11 15:41:33` | `cowrie.command.input` |
| `2026-08-11 15:41:33` | `cowrie.command.input` |
| `2026-08-11 15:41:33` | `cowrie.command.input` |
| `2026-08-11 15:41:33` | `cowrie.command.success` |
| `2026-08-11 15:41:33` | `cowrie.command.input` |
| `2026-08-11 15:41:33` | `cowrie.command.input` |
| `2026-08-11 15:41:33` | `cowrie.command.input` |
| `2026-08-11 15:41:33` | `cowrie.command.input` |
| `2026-08-11 15:41:34` | `cowrie.log.closed` |
| `2026-08-11 15:41:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-97400de95129

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-08-11 15:42 |
| **Last Seen** | 2026-08-11 15:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 15:42:57` | `cowrie.session.connect` |
| `2026-08-11 15:42:57` | `cowrie.client.version` |
| `2026-08-11 15:42:57` | `cowrie.client.kex` |
| `2026-08-11 15:42:57` | `cowrie.login.success` |
| `2026-08-11 15:42:58` | `cowrie.session.params` |
| `2026-08-11 15:42:58` | `cowrie.command.input` |
| `2026-08-11 15:42:58` | `cowrie.log.closed` |
| `2026-08-11 15:42:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81cbae82d5db

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-11 15:43 |
| **Last Seen** | 2026-08-11 15:43 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 15:43:23` | `cowrie.session.connect` |
| `2026-08-11 15:43:23` | `cowrie.client.version` |
| `2026-08-11 15:43:23` | `cowrie.client.kex` |
| `2026-08-11 15:43:24` | `cowrie.login.success` |
| `2026-08-11 15:43:26` | `cowrie.session.params` |
| `2026-08-11 15:43:26` | `cowrie.command.input` |
| `2026-08-11 15:43:26` | `cowrie.command.input` |
| `2026-08-11 15:43:26` | `cowrie.command.input` |
| `2026-08-11 15:43:26` | `cowrie.command.input` |
| `2026-08-11 15:43:26` | `cowrie.command.input` |
| `2026-08-11 15:43:26` | `cowrie.command.success` |
| `2026-08-11 15:43:26` | `cowrie.command.input` |
| `2026-08-11 15:43:26` | `cowrie.command.input` |
| `2026-08-11 15:43:26` | `cowrie.command.input` |
| `2026-08-11 15:43:26` | `cowrie.command.input` |
| `2026-08-11 15:43:26` | `cowrie.log.closed` |
| `2026-08-11 15:43:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bfe860ed8fc3

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-08-11 15:45 |
| **Last Seen** | 2026-08-11 15:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 15:45:05` | `cowrie.session.connect` |
| `2026-08-11 15:45:05` | `cowrie.client.version` |
| `2026-08-11 15:45:05` | `cowrie.client.kex` |
| `2026-08-11 15:45:06` | `cowrie.login.success` |
| `2026-08-11 15:45:06` | `cowrie.session.params` |
| `2026-08-11 15:45:06` | `cowrie.command.input` |
| `2026-08-11 15:45:06` | `cowrie.log.closed` |
| `2026-08-11 15:45:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59660865a47e

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-11 15:45 |
| **Last Seen** | 2026-08-11 15:45 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 15:45:34` | `cowrie.session.connect` |
| `2026-08-11 15:45:34` | `cowrie.client.version` |
| `2026-08-11 15:45:34` | `cowrie.client.kex` |
| `2026-08-11 15:45:35` | `cowrie.login.success` |
| `2026-08-11 15:45:36` | `cowrie.session.params` |
| `2026-08-11 15:45:36` | `cowrie.command.input` |
| `2026-08-11 15:45:36` | `cowrie.command.input` |
| `2026-08-11 15:45:36` | `cowrie.command.input` |
| `2026-08-11 15:45:36` | `cowrie.command.input` |
| `2026-08-11 15:45:36` | `cowrie.command.input` |
| `2026-08-11 15:45:36` | `cowrie.command.success` |
| `2026-08-11 15:45:36` | `cowrie.command.input` |
| `2026-08-11 15:45:36` | `cowrie.command.input` |
| `2026-08-11 15:45:36` | `cowrie.command.input` |
| `2026-08-11 15:45:36` | `cowrie.command.input` |
| `2026-08-11 15:45:36` | `cowrie.log.closed` |
| `2026-08-11 15:45:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74db46ce0e8c

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-08-11 15:47 |
| **Last Seen** | 2026-08-11 15:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 15:47:15` | `cowrie.session.connect` |
| `2026-08-11 15:47:15` | `cowrie.client.version` |
| `2026-08-11 15:47:15` | `cowrie.client.kex` |
| `2026-08-11 15:47:15` | `cowrie.login.success` |
| `2026-08-11 15:47:16` | `cowrie.session.params` |
| `2026-08-11 15:47:16` | `cowrie.command.input` |
| `2026-08-11 15:47:16` | `cowrie.log.closed` |
| `2026-08-11 15:47:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c497a66d1a55

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-11 15:48 |
| **Last Seen** | 2026-08-11 15:48 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 15:48:19` | `cowrie.session.connect` |
| `2026-08-11 15:48:19` | `cowrie.client.version` |
| `2026-08-11 15:48:20` | `cowrie.client.kex` |
| `2026-08-11 15:48:21` | `cowrie.login.success` |
| `2026-08-11 15:48:22` | `cowrie.session.params` |
| `2026-08-11 15:48:22` | `cowrie.command.input` |
| `2026-08-11 15:48:22` | `cowrie.command.input` |
| `2026-08-11 15:48:22` | `cowrie.command.input` |
| `2026-08-11 15:48:22` | `cowrie.command.input` |
| `2026-08-11 15:48:22` | `cowrie.command.input` |
| `2026-08-11 15:48:22` | `cowrie.command.success` |
| `2026-08-11 15:48:22` | `cowrie.command.input` |
| `2026-08-11 15:48:22` | `cowrie.command.input` |
| `2026-08-11 15:48:22` | `cowrie.command.input` |
| `2026-08-11 15:48:22` | `cowrie.command.input` |
| `2026-08-11 15:48:22` | `cowrie.log.closed` |
| `2026-08-11 15:48:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63821ac5d3b7

| Field | Detail |
|---|---|
| **Source IP** | `178.178.194[.]192` |
| **First Seen** | 2026-08-11 15:49 |
| **Last Seen** | 2026-08-11 15:49 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 15:49:16` | `cowrie.session.connect` |
| `2026-08-11 15:49:16` | `cowrie.client.version` |
| `2026-08-11 15:49:16` | `cowrie.client.kex` |
| `2026-08-11 15:49:19` | `cowrie.login.success` |
| `2026-08-11 15:49:19` | `cowrie.direct-tcpip.request` |
| `2026-08-11 15:49:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.194[.]192` to AbuseIPDB if not already reported
- [ ] Block `178.178.194[.]192` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4777bf802c6f

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-08-11 15:49 |
| **Last Seen** | 2026-08-11 15:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 15:49:25` | `cowrie.session.connect` |
| `2026-08-11 15:49:25` | `cowrie.client.version` |
| `2026-08-11 15:49:25` | `cowrie.client.kex` |
| `2026-08-11 15:49:25` | `cowrie.login.success` |
| `2026-08-11 15:49:26` | `cowrie.session.params` |
| `2026-08-11 15:49:26` | `cowrie.command.input` |
| `2026-08-11 15:49:26` | `cowrie.log.closed` |
| `2026-08-11 15:49:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9653c55c2fd2

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-11 15:50 |
| **Last Seen** | 2026-08-11 15:50 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 15:50:32` | `cowrie.session.connect` |
| `2026-08-11 15:50:32` | `cowrie.client.version` |
| `2026-08-11 15:50:32` | `cowrie.client.kex` |
| `2026-08-11 15:50:32` | `cowrie.login.success` |
| `2026-08-11 15:50:33` | `cowrie.session.params` |
| `2026-08-11 15:50:33` | `cowrie.command.input` |
| `2026-08-11 15:50:33` | `cowrie.command.input` |
| `2026-08-11 15:50:33` | `cowrie.command.input` |
| `2026-08-11 15:50:33` | `cowrie.command.input` |
| `2026-08-11 15:50:33` | `cowrie.command.input` |
| `2026-08-11 15:50:33` | `cowrie.command.success` |
| `2026-08-11 15:50:33` | `cowrie.command.input` |
| `2026-08-11 15:50:33` | `cowrie.command.input` |
| `2026-08-11 15:50:33` | `cowrie.command.input` |
| `2026-08-11 15:50:33` | `cowrie.command.input` |
| `2026-08-11 15:50:34` | `cowrie.log.closed` |
| `2026-08-11 15:50:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ddbff48e5bc

| Field | Detail |
|---|---|
| **Source IP** | `70.89.116[.]5` |
| **First Seen** | 2026-08-11 15:50 |
| **Last Seen** | 2026-08-11 15:51 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 15:50:59` | `cowrie.session.connect` |
| `2026-08-11 15:51:00` | `cowrie.client.version` |
| `2026-08-11 15:51:00` | `cowrie.client.kex` |
| `2026-08-11 15:51:02` | `cowrie.login.success` |
| `2026-08-11 15:51:02` | `cowrie.direct-tcpip.request` |
| `2026-08-11 15:51:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `70.89.116[.]5` to AbuseIPDB if not already reported
- [ ] Block `70.89.116[.]5` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a447a24100b8

| Field | Detail |
|---|---|
| **Source IP** | `31.173.2[.]182` |
| **First Seen** | 2026-08-11 15:51 |
| **Last Seen** | 2026-08-11 15:51 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 15:51:07` | `cowrie.session.connect` |
| `2026-08-11 15:51:08` | `cowrie.client.version` |
| `2026-08-11 15:51:08` | `cowrie.client.kex` |
| `2026-08-11 15:51:09` | `cowrie.login.success` |
| `2026-08-11 15:51:09` | `cowrie.direct-tcpip.request` |
| `2026-08-11 15:51:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.173.2[.]182` to AbuseIPDB if not already reported
- [ ] Block `31.173.2[.]182` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5851666cbc70

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-08-11 15:51 |
| **Last Seen** | 2026-08-11 15:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 15:51:33` | `cowrie.session.connect` |
| `2026-08-11 15:51:33` | `cowrie.client.version` |
| `2026-08-11 15:51:34` | `cowrie.client.kex` |
| `2026-08-11 15:51:34` | `cowrie.login.success` |
| `2026-08-11 15:51:35` | `cowrie.session.params` |
| `2026-08-11 15:51:35` | `cowrie.command.input` |
| `2026-08-11 15:51:35` | `cowrie.log.closed` |
| `2026-08-11 15:51:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-862e93fe944d

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-11 15:53 |
| **Last Seen** | 2026-08-11 15:53 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 15:53:03` | `cowrie.session.connect` |
| `2026-08-11 15:53:03` | `cowrie.client.version` |
| `2026-08-11 15:53:03` | `cowrie.client.kex` |
| `2026-08-11 15:53:05` | `cowrie.login.success` |
| `2026-08-11 15:53:06` | `cowrie.session.params` |
| `2026-08-11 15:53:06` | `cowrie.command.input` |
| `2026-08-11 15:53:06` | `cowrie.command.input` |
| `2026-08-11 15:53:06` | `cowrie.command.input` |
| `2026-08-11 15:53:06` | `cowrie.command.input` |
| `2026-08-11 15:53:06` | `cowrie.command.input` |
| `2026-08-11 15:53:06` | `cowrie.command.success` |
| `2026-08-11 15:53:06` | `cowrie.command.input` |
| `2026-08-11 15:53:06` | `cowrie.command.input` |
| `2026-08-11 15:53:06` | `cowrie.command.input` |
| `2026-08-11 15:53:06` | `cowrie.command.input` |
| `2026-08-11 15:53:07` | `cowrie.log.closed` |
| `2026-08-11 15:53:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b83dd7f8c773

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-08-11 15:53 |
| **Last Seen** | 2026-08-11 15:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 15:53:43` | `cowrie.session.connect` |
| `2026-08-11 15:53:43` | `cowrie.client.version` |
| `2026-08-11 15:53:43` | `cowrie.client.kex` |
| `2026-08-11 15:53:44` | `cowrie.login.success` |
| `2026-08-11 15:53:44` | `cowrie.session.params` |
| `2026-08-11 15:53:44` | `cowrie.command.input` |
| `2026-08-11 15:53:44` | `cowrie.log.closed` |
| `2026-08-11 15:53:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-659b41a7aab5

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-11 15:54 |
| **Last Seen** | 2026-08-11 15:54 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 15:54:49` | `cowrie.session.connect` |
| `2026-08-11 15:54:49` | `cowrie.client.version` |
| `2026-08-11 15:54:49` | `cowrie.client.kex` |
| `2026-08-11 15:54:51` | `cowrie.login.success` |
| `2026-08-11 15:54:53` | `cowrie.session.params` |
| `2026-08-11 15:54:53` | `cowrie.command.input` |
| `2026-08-11 15:54:53` | `cowrie.command.input` |
| `2026-08-11 15:54:53` | `cowrie.command.input` |
| `2026-08-11 15:54:53` | `cowrie.command.input` |
| `2026-08-11 15:54:53` | `cowrie.command.input` |
| `2026-08-11 15:54:53` | `cowrie.command.success` |
| `2026-08-11 15:54:53` | `cowrie.command.input` |
| `2026-08-11 15:54:53` | `cowrie.command.input` |
| `2026-08-11 15:54:53` | `cowrie.command.input` |
| `2026-08-11 15:54:53` | `cowrie.command.input` |
| `2026-08-11 15:54:54` | `cowrie.log.closed` |
| `2026-08-11 15:54:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a925bd646341

| Field | Detail |
|---|---|
| **Source IP** | `61.2.44[.]54` |
| **First Seen** | 2026-08-11 15:55 |
| **Last Seen** | 2026-08-11 15:55 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 15:55:51` | `cowrie.session.connect` |
| `2026-08-11 15:55:51` | `cowrie.client.version` |
| `2026-08-11 15:55:51` | `cowrie.client.kex` |
| `2026-08-11 15:55:53` | `cowrie.login.success` |
| `2026-08-11 15:55:54` | `cowrie.direct-tcpip.request` |
| `2026-08-11 15:55:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.2.44[.]54` to AbuseIPDB if not already reported
- [ ] Block `61.2.44[.]54` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c60657a921cd

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-08-11 15:55 |
| **Last Seen** | 2026-08-11 15:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 15:55:54` | `cowrie.session.connect` |
| `2026-08-11 15:55:54` | `cowrie.client.version` |
| `2026-08-11 15:55:54` | `cowrie.client.kex` |
| `2026-08-11 15:55:55` | `cowrie.login.success` |
| `2026-08-11 15:55:56` | `cowrie.session.params` |
| `2026-08-11 15:55:56` | `cowrie.command.input` |
| `2026-08-11 15:55:56` | `cowrie.log.closed` |
| `2026-08-11 15:55:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8b7db13c245

| Field | Detail |
|---|---|
| **Source IP** | `125.20.207[.]154` |
| **First Seen** | 2026-08-11 15:55 |
| **Last Seen** | 2026-08-11 15:56 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 15:55:59` | `cowrie.session.connect` |
| `2026-08-11 15:55:59` | `cowrie.client.version` |
| `2026-08-11 15:55:59` | `cowrie.client.kex` |
| `2026-08-11 15:56:01` | `cowrie.login.success` |
| `2026-08-11 15:56:02` | `cowrie.direct-tcpip.request` |
| `2026-08-11 15:56:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.20.207[.]154` to AbuseIPDB if not already reported
- [ ] Block `125.20.207[.]154` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25162a836cbb

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-11 15:56 |
| **Last Seen** | 2026-08-11 15:56 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 15:56:39` | `cowrie.session.connect` |
| `2026-08-11 15:56:40` | `cowrie.client.version` |
| `2026-08-11 15:56:40` | `cowrie.client.kex` |
| `2026-08-11 15:56:41` | `cowrie.login.success` |
| `2026-08-11 15:56:42` | `cowrie.session.params` |
| `2026-08-11 15:56:42` | `cowrie.command.input` |
| `2026-08-11 15:56:42` | `cowrie.command.input` |
| `2026-08-11 15:56:42` | `cowrie.command.input` |
| `2026-08-11 15:56:42` | `cowrie.command.input` |
| `2026-08-11 15:56:42` | `cowrie.command.input` |
| `2026-08-11 15:56:42` | `cowrie.command.success` |
| `2026-08-11 15:56:42` | `cowrie.command.input` |
| `2026-08-11 15:56:42` | `cowrie.command.input` |
| `2026-08-11 15:56:42` | `cowrie.command.input` |
| `2026-08-11 15:56:42` | `cowrie.command.input` |
| `2026-08-11 15:56:43` | `cowrie.log.closed` |
| `2026-08-11 15:56:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-452c7a9e44ee

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-08-11 15:58 |
| **Last Seen** | 2026-08-11 15:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 15:58:05` | `cowrie.session.connect` |
| `2026-08-11 15:58:05` | `cowrie.client.version` |
| `2026-08-11 15:58:05` | `cowrie.client.kex` |
| `2026-08-11 15:58:05` | `cowrie.login.success` |
| `2026-08-11 15:58:06` | `cowrie.session.params` |
| `2026-08-11 15:58:06` | `cowrie.command.input` |
| `2026-08-11 15:58:06` | `cowrie.log.closed` |
| `2026-08-11 15:58:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0eb4be2640c0

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-11 15:58 |
| **Last Seen** | 2026-08-11 15:58 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 15:58:40` | `cowrie.session.connect` |
| `2026-08-11 15:58:40` | `cowrie.client.version` |
| `2026-08-11 15:58:40` | `cowrie.client.kex` |
| `2026-08-11 15:58:41` | `cowrie.login.success` |
| `2026-08-11 15:58:42` | `cowrie.session.params` |
| `2026-08-11 15:58:42` | `cowrie.command.input` |
| `2026-08-11 15:58:42` | `cowrie.command.input` |
| `2026-08-11 15:58:42` | `cowrie.command.input` |
| `2026-08-11 15:58:42` | `cowrie.command.input` |
| `2026-08-11 15:58:42` | `cowrie.command.input` |
| `2026-08-11 15:58:42` | `cowrie.command.success` |
| `2026-08-11 15:58:42` | `cowrie.command.input` |
| `2026-08-11 15:58:42` | `cowrie.command.input` |
| `2026-08-11 15:58:42` | `cowrie.command.input` |
| `2026-08-11 15:58:42` | `cowrie.command.input` |
| `2026-08-11 15:58:42` | `cowrie.log.closed` |
| `2026-08-11 15:58:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7ded0f0542c

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-08-11 16:00 |
| **Last Seen** | 2026-08-11 16:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 16:00:16` | `cowrie.session.connect` |
| `2026-08-11 16:00:16` | `cowrie.client.version` |
| `2026-08-11 16:00:16` | `cowrie.client.kex` |
| `2026-08-11 16:00:17` | `cowrie.login.success` |
| `2026-08-11 16:00:17` | `cowrie.session.params` |
| `2026-08-11 16:00:17` | `cowrie.command.input` |
| `2026-08-11 16:00:17` | `cowrie.log.closed` |
| `2026-08-11 16:00:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e308297c3244

| Field | Detail |
|---|---|
| **Source IP** | `128.185.12[.]179` |
| **First Seen** | 2026-08-11 16:01 |
| **Last Seen** | 2026-08-11 16:01 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 16:01:10` | `cowrie.session.connect` |
| `2026-08-11 16:01:10` | `cowrie.client.version` |
| `2026-08-11 16:01:10` | `cowrie.client.kex` |
| `2026-08-11 16:01:12` | `cowrie.login.success` |
| `2026-08-11 16:01:13` | `cowrie.direct-tcpip.request` |
| `2026-08-11 16:01:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `128.185.12[.]179` to AbuseIPDB if not already reported
- [ ] Block `128.185.12[.]179` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a57e0a2466b2

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-11 16:01 |
| **Last Seen** | 2026-08-11 16:01 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 16:01:15` | `cowrie.session.connect` |
| `2026-08-11 16:01:15` | `cowrie.client.version` |
| `2026-08-11 16:01:15` | `cowrie.client.kex` |
| `2026-08-11 16:01:16` | `cowrie.login.success` |
| `2026-08-11 16:01:17` | `cowrie.session.params` |
| `2026-08-11 16:01:17` | `cowrie.command.input` |
| `2026-08-11 16:01:17` | `cowrie.command.input` |
| `2026-08-11 16:01:17` | `cowrie.command.input` |
| `2026-08-11 16:01:17` | `cowrie.command.input` |
| `2026-08-11 16:01:17` | `cowrie.command.input` |
| `2026-08-11 16:01:17` | `cowrie.command.success` |
| `2026-08-11 16:01:17` | `cowrie.command.input` |
| `2026-08-11 16:01:17` | `cowrie.command.input` |
| `2026-08-11 16:01:17` | `cowrie.command.input` |
| `2026-08-11 16:01:17` | `cowrie.command.input` |
| `2026-08-11 16:01:17` | `cowrie.log.closed` |
| `2026-08-11 16:01:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6cdc8f0fae67

| Field | Detail |
|---|---|
| **Source IP** | `65.20.211[.]96` |
| **First Seen** | 2026-08-11 16:01 |
| **Last Seen** | 2026-08-11 16:01 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 16:01:18` | `cowrie.session.connect` |
| `2026-08-11 16:01:19` | `cowrie.client.version` |
| `2026-08-11 16:01:19` | `cowrie.client.kex` |
| `2026-08-11 16:01:21` | `cowrie.login.success` |
| `2026-08-11 16:01:21` | `cowrie.direct-tcpip.request` |
| `2026-08-11 16:01:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.211[.]96` to AbuseIPDB if not already reported
- [ ] Block `65.20.211[.]96` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07e89433aabd

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-08-11 16:02 |
| **Last Seen** | 2026-08-11 16:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 16:02:26` | `cowrie.session.connect` |
| `2026-08-11 16:02:26` | `cowrie.client.version` |
| `2026-08-11 16:02:26` | `cowrie.client.kex` |
| `2026-08-11 16:02:26` | `cowrie.login.success` |
| `2026-08-11 16:02:27` | `cowrie.session.params` |
| `2026-08-11 16:02:27` | `cowrie.command.input` |
| `2026-08-11 16:02:27` | `cowrie.log.closed` |
| `2026-08-11 16:02:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8fd1784518f6

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-11 16:04 |
| **Last Seen** | 2026-08-11 16:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 16:04:21` | `cowrie.session.connect` |
| `2026-08-11 16:04:21` | `cowrie.client.version` |
| `2026-08-11 16:04:21` | `cowrie.client.kex` |
| `2026-08-11 16:04:22` | `cowrie.login.success` |
| `2026-08-11 16:04:22` | `cowrie.session.params` |
| `2026-08-11 16:04:22` | `cowrie.command.input` |
| `2026-08-11 16:04:22` | `cowrie.command.input` |
| `2026-08-11 16:04:22` | `cowrie.command.input` |
| `2026-08-11 16:04:22` | `cowrie.command.input` |
| `2026-08-11 16:04:22` | `cowrie.command.input` |
| `2026-08-11 16:04:22` | `cowrie.command.success` |
| `2026-08-11 16:04:22` | `cowrie.command.input` |
| `2026-08-11 16:04:22` | `cowrie.command.input` |
| `2026-08-11 16:04:22` | `cowrie.command.input` |
| `2026-08-11 16:04:22` | `cowrie.command.input` |
| `2026-08-11 16:04:23` | `cowrie.log.closed` |
| `2026-08-11 16:04:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-960a710b4832

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-08-11 16:04 |
| **Last Seen** | 2026-08-11 16:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 16:04:33` | `cowrie.session.connect` |
| `2026-08-11 16:04:33` | `cowrie.client.version` |
| `2026-08-11 16:04:33` | `cowrie.client.kex` |
| `2026-08-11 16:04:34` | `cowrie.login.success` |
| `2026-08-11 16:04:35` | `cowrie.session.params` |
| `2026-08-11 16:04:35` | `cowrie.command.input` |
| `2026-08-11 16:04:35` | `cowrie.log.closed` |
| `2026-08-11 16:04:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a0104adb638

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-11 16:06 |
| **Last Seen** | 2026-08-11 16:06 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 16:06:37` | `cowrie.session.connect` |
| `2026-08-11 16:06:38` | `cowrie.client.version` |
| `2026-08-11 16:06:38` | `cowrie.client.kex` |
| `2026-08-11 16:06:40` | `cowrie.login.success` |
| `2026-08-11 16:06:41` | `cowrie.session.params` |
| `2026-08-11 16:06:41` | `cowrie.command.input` |
| `2026-08-11 16:06:41` | `cowrie.command.input` |
| `2026-08-11 16:06:41` | `cowrie.command.input` |
| `2026-08-11 16:06:41` | `cowrie.command.input` |
| `2026-08-11 16:06:41` | `cowrie.command.input` |
| `2026-08-11 16:06:41` | `cowrie.command.success` |
| `2026-08-11 16:06:41` | `cowrie.command.input` |
| `2026-08-11 16:06:41` | `cowrie.command.input` |
| `2026-08-11 16:06:41` | `cowrie.command.input` |
| `2026-08-11 16:06:41` | `cowrie.command.input` |
| `2026-08-11 16:06:42` | `cowrie.log.closed` |
| `2026-08-11 16:06:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d31243255b07

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-08-11 16:06 |
| **Last Seen** | 2026-08-11 16:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 16:06:43` | `cowrie.session.connect` |
| `2026-08-11 16:06:43` | `cowrie.client.version` |
| `2026-08-11 16:06:43` | `cowrie.client.kex` |
| `2026-08-11 16:06:44` | `cowrie.login.success` |
| `2026-08-11 16:06:45` | `cowrie.session.params` |
| `2026-08-11 16:06:45` | `cowrie.command.input` |
| `2026-08-11 16:06:45` | `cowrie.log.closed` |
| `2026-08-11 16:06:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba9360b2c26e

| Field | Detail |
|---|---|
| **Source IP** | `196.216.81[.]126` |
| **First Seen** | 2026-08-11 16:07 |
| **Last Seen** | 2026-08-11 16:07 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 16:07:17` | `cowrie.session.connect` |
| `2026-08-11 16:07:18` | `cowrie.client.version` |
| `2026-08-11 16:07:18` | `cowrie.client.kex` |
| `2026-08-11 16:07:20` | `cowrie.login.success` |
| `2026-08-11 16:07:20` | `cowrie.direct-tcpip.request` |
| `2026-08-11 16:07:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.216.81[.]126` to AbuseIPDB if not already reported
- [ ] Block `196.216.81[.]126` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76f626428ee1

| Field | Detail |
|---|---|
| **Source IP** | `191.210.73[.]33` |
| **First Seen** | 2026-08-11 16:07 |
| **Last Seen** | 2026-08-11 16:07 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 16:07:30` | `cowrie.session.connect` |
| `2026-08-11 16:07:30` | `cowrie.client.version` |
| `2026-08-11 16:07:30` | `cowrie.client.kex` |
| `2026-08-11 16:07:32` | `cowrie.login.success` |
| `2026-08-11 16:07:33` | `cowrie.direct-tcpip.request` |
| `2026-08-11 16:07:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `191.210.73[.]33` to AbuseIPDB if not already reported
- [ ] Block `191.210.73[.]33` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49b93cee50ff

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-11 16:08 |
| **Last Seen** | 2026-08-11 16:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 16:08:02` | `cowrie.session.connect` |
| `2026-08-11 16:08:02` | `cowrie.client.version` |
| `2026-08-11 16:08:02` | `cowrie.client.kex` |
| `2026-08-11 16:08:02` | `cowrie.login.success` |
| `2026-08-11 16:08:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0791668961c1

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-11 16:08 |
| **Last Seen** | 2026-08-11 16:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 16:08:02` | `cowrie.session.connect` |
| `2026-08-11 16:08:02` | `cowrie.client.version` |
| `2026-08-11 16:08:02` | `cowrie.client.kex` |
| `2026-08-11 16:08:03` | `cowrie.login.success` |
| `2026-08-11 16:08:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b10d497777f

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-11 16:08 |
| **Last Seen** | 2026-08-11 16:08 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 16:08:24` | `cowrie.session.connect` |
| `2026-08-11 16:08:25` | `cowrie.client.version` |
| `2026-08-11 16:08:25` | `cowrie.client.kex` |
| `2026-08-11 16:08:27` | `cowrie.login.success` |
| `2026-08-11 16:08:28` | `cowrie.session.params` |
| `2026-08-11 16:08:28` | `cowrie.command.input` |
| `2026-08-11 16:08:28` | `cowrie.command.input` |
| `2026-08-11 16:08:28` | `cowrie.command.input` |
| `2026-08-11 16:08:28` | `cowrie.command.input` |
| `2026-08-11 16:08:28` | `cowrie.command.input` |
| `2026-08-11 16:08:28` | `cowrie.command.success` |
| `2026-08-11 16:08:28` | `cowrie.command.input` |
| `2026-08-11 16:08:28` | `cowrie.command.input` |
| `2026-08-11 16:08:28` | `cowrie.command.input` |
| `2026-08-11 16:08:28` | `cowrie.command.input` |
| `2026-08-11 16:08:28` | `cowrie.log.closed` |
| `2026-08-11 16:08:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3aa74a09eb5

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-11 16:10 |
| **Last Seen** | 2026-08-11 16:10 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 16:10:16` | `cowrie.session.connect` |
| `2026-08-11 16:10:16` | `cowrie.client.version` |
| `2026-08-11 16:10:16` | `cowrie.client.kex` |
| `2026-08-11 16:10:17` | `cowrie.login.success` |
| `2026-08-11 16:10:18` | `cowrie.session.params` |
| `2026-08-11 16:10:18` | `cowrie.command.input` |
| `2026-08-11 16:10:18` | `cowrie.command.input` |
| `2026-08-11 16:10:18` | `cowrie.command.input` |
| `2026-08-11 16:10:18` | `cowrie.command.input` |
| `2026-08-11 16:10:18` | `cowrie.command.input` |
| `2026-08-11 16:10:18` | `cowrie.command.success` |
| `2026-08-11 16:10:18` | `cowrie.command.input` |
| `2026-08-11 16:10:18` | `cowrie.command.input` |
| `2026-08-11 16:10:18` | `cowrie.command.input` |
| `2026-08-11 16:10:18` | `cowrie.command.input` |
| `2026-08-11 16:10:19` | `cowrie.log.closed` |
| `2026-08-11 16:10:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-922d413bdc32

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-11 16:12 |
| **Last Seen** | 2026-08-11 16:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 16:12:32` | `cowrie.session.connect` |
| `2026-08-11 16:12:32` | `cowrie.client.version` |
| `2026-08-11 16:12:32` | `cowrie.client.kex` |
| `2026-08-11 16:12:32` | `cowrie.login.success` |
| `2026-08-11 16:12:33` | `cowrie.session.params` |
| `2026-08-11 16:12:33` | `cowrie.command.input` |
| `2026-08-11 16:12:33` | `cowrie.command.input` |
| `2026-08-11 16:12:33` | `cowrie.command.input` |
| `2026-08-11 16:12:33` | `cowrie.command.input` |
| `2026-08-11 16:12:33` | `cowrie.command.input` |
| `2026-08-11 16:12:33` | `cowrie.command.success` |
| `2026-08-11 16:12:33` | `cowrie.command.input` |
| `2026-08-11 16:12:33` | `cowrie.command.input` |
| `2026-08-11 16:12:33` | `cowrie.command.input` |
| `2026-08-11 16:12:33` | `cowrie.command.input` |
| `2026-08-11 16:12:33` | `cowrie.log.closed` |
| `2026-08-11 16:12:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-afb4e81c3400

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-11 16:15 |
| **Last Seen** | 2026-08-11 16:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 16:15:20` | `cowrie.session.connect` |
| `2026-08-11 16:15:20` | `cowrie.client.version` |
| `2026-08-11 16:15:20` | `cowrie.client.kex` |
| `2026-08-11 16:15:20` | `cowrie.login.success` |
| `2026-08-11 16:15:21` | `cowrie.session.params` |
| `2026-08-11 16:15:21` | `cowrie.command.input` |
| `2026-08-11 16:15:21` | `cowrie.command.input` |
| `2026-08-11 16:15:21` | `cowrie.command.input` |
| `2026-08-11 16:15:21` | `cowrie.command.input` |
| `2026-08-11 16:15:21` | `cowrie.command.input` |
| `2026-08-11 16:15:21` | `cowrie.command.success` |
| `2026-08-11 16:15:21` | `cowrie.command.input` |
| `2026-08-11 16:15:21` | `cowrie.command.input` |
| `2026-08-11 16:15:21` | `cowrie.command.input` |
| `2026-08-11 16:15:21` | `cowrie.command.input` |
| `2026-08-11 16:15:21` | `cowrie.log.closed` |
| `2026-08-11 16:15:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3f400ab6f5f

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-11 16:18 |
| **Last Seen** | 2026-08-11 16:18 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 16:18:38` | `cowrie.session.connect` |
| `2026-08-11 16:18:38` | `cowrie.client.version` |
| `2026-08-11 16:18:38` | `cowrie.client.kex` |
| `2026-08-11 16:18:39` | `cowrie.login.success` |
| `2026-08-11 16:18:40` | `cowrie.session.params` |
| `2026-08-11 16:18:40` | `cowrie.command.input` |
| `2026-08-11 16:18:40` | `cowrie.command.input` |
| `2026-08-11 16:18:40` | `cowrie.command.input` |
| `2026-08-11 16:18:40` | `cowrie.command.input` |
| `2026-08-11 16:18:40` | `cowrie.command.input` |
| `2026-08-11 16:18:40` | `cowrie.command.success` |
| `2026-08-11 16:18:40` | `cowrie.command.input` |
| `2026-08-11 16:18:40` | `cowrie.command.input` |
| `2026-08-11 16:18:40` | `cowrie.command.input` |
| `2026-08-11 16:18:40` | `cowrie.command.input` |
| `2026-08-11 16:18:41` | `cowrie.log.closed` |
| `2026-08-11 16:18:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-13a77bd5284a

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]99` |
| **First Seen** | 2026-08-11 16:22 |
| **Last Seen** | 2026-08-11 16:25 |
| **Session Duration** | 180s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 16:22:39` | `cowrie.session.connect` |
| `2026-08-11 16:22:39` | `cowrie.login.success` |
| `2026-08-11 16:22:40` | `cowrie.session.params` |
| `2026-08-11 16:25:40` | `cowrie.log.closed` |
| `2026-08-11 16:25:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]99` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]99` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4fa1c742378

| Field | Detail |
|---|---|
| **Source IP** | `208.109.38[.]143` |
| **First Seen** | 2026-08-11 16:25 |
| **Last Seen** | 2026-08-11 16:25 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 16:25:04` | `cowrie.session.connect` |
| `2026-08-11 16:25:04` | `cowrie.client.version` |
| `2026-08-11 16:25:04` | `cowrie.client.kex` |
| `2026-08-11 16:25:06` | `cowrie.login.success` |
| `2026-08-11 16:25:06` | `cowrie.direct-tcpip.request` |
| `2026-08-11 16:25:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `208.109.38[.]143` to AbuseIPDB if not already reported
- [ ] Block `208.109.38[.]143` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e453a206547

| Field | Detail |
|---|---|
| **Source IP** | `186.215.107[.]189` |
| **First Seen** | 2026-08-11 16:25 |
| **Last Seen** | 2026-08-11 16:25 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 16:25:11` | `cowrie.session.connect` |
| `2026-08-11 16:25:11` | `cowrie.client.version` |
| `2026-08-11 16:25:11` | `cowrie.client.kex` |
| `2026-08-11 16:25:13` | `cowrie.login.success` |
| `2026-08-11 16:25:13` | `cowrie.direct-tcpip.request` |
| `2026-08-11 16:25:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.215.107[.]189` to AbuseIPDB if not already reported
- [ ] Block `186.215.107[.]189` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da33ce2677ee

| Field | Detail |
|---|---|
| **Source IP** | `49.124.151[.]58` |
| **First Seen** | 2026-08-11 16:25 |
| **Last Seen** | 2026-08-11 16:25 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 16:25:18` | `cowrie.session.connect` |
| `2026-08-11 16:25:19` | `cowrie.client.version` |
| `2026-08-11 16:25:19` | `cowrie.client.kex` |
| `2026-08-11 16:25:21` | `cowrie.login.success` |
| `2026-08-11 16:25:22` | `cowrie.direct-tcpip.request` |
| `2026-08-11 16:25:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.151[.]58` to AbuseIPDB if not already reported
- [ ] Block `49.124.151[.]58` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f491c5384207

| Field | Detail |
|---|---|
| **Source IP** | `223.75.156[.]89` |
| **First Seen** | 2026-08-11 16:35 |
| **Last Seen** | 2026-08-11 16:35 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 16:35:35` | `cowrie.session.connect` |
| `2026-08-11 16:35:36` | `cowrie.client.version` |
| `2026-08-11 16:35:36` | `cowrie.client.kex` |
| `2026-08-11 16:35:38` | `cowrie.login.success` |
| `2026-08-11 16:35:38` | `cowrie.direct-tcpip.request` |
| `2026-08-11 16:35:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.75.156[.]89` to AbuseIPDB if not already reported
- [ ] Block `223.75.156[.]89` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-697704f71bb6

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-11 16:46 |
| **Last Seen** | 2026-08-11 16:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 16:46:54` | `cowrie.session.connect` |
| `2026-08-11 16:46:54` | `cowrie.client.version` |
| `2026-08-11 16:46:54` | `cowrie.client.kex` |
| `2026-08-11 16:46:54` | `cowrie.login.success` |
| `2026-08-11 16:46:54` | `cowrie.direct-tcpip.request` |
| `2026-08-11 16:46:54` | `cowrie.direct-tcpip.data` |
| `2026-08-11 16:46:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `164.92.115[.]22` | **25** | 2026-08-11 14:58 | 2026-08-11 16:54 | 15m | 0 | `T1592` | 🟠 MEDIUM |
| `94.154.43[.]76` | **8** | 2026-08-11 15:46 | 2026-08-11 15:49 | 5m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **4** | 2026-08-11 15:20 | 2026-08-11 16:43 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]121` | **3** | 2026-08-11 16:41 | 2026-08-11 16:41 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]123` | **3** | 2026-08-11 16:09 | 2026-08-11 16:09 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]167` | **3** | 2026-08-11 14:58 | 2026-08-11 14:58 | 0m | 0 | `T1592` | 🟢 LOW |
| `210.16.100[.]120` | **3** | 2026-08-11 15:29 | 2026-08-11 16:26 | 2m | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]204` | **3** | 2026-08-11 15:02 | 2026-08-11 15:02 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]117` | **3** | 2026-08-11 14:55 | 2026-08-11 14:56 | 0m | 0 | `T1592` | 🟢 LOW |
| `88.214.25[.]123` | **3** | 2026-08-11 15:06 | 2026-08-11 15:06 | 0m | 0 | `T1592` | 🟢 LOW |
| `124.207.135[.]77` | **2** | 2026-08-11 15:52 | 2026-08-11 15:53 | 0m | 0 | `T1592` | 🟢 LOW |
| `112.26.99[.]93` | 1 | 2026-08-11 15:22 | 2026-08-11 15:22 | 12s | 0 | `T1592` | 🟢 LOW |
| `181.78.3[.]229` | 1 | 2026-08-11 16:05 | 2026-08-11 16:07 | 120s | 0 | `T1592` | 🟢 LOW |
| `184.185.2[.]254` | 1 | 2026-08-11 15:44 | 2026-08-11 15:46 | 120s | 0 | `T1592` | 🟢 LOW |
| `185.242.226[.]17` | 1 | 2026-08-11 16:32 | 2026-08-11 16:32 | 10s | 0 | `T1592` | 🟢 LOW |
| `193.217.0[.]16` | 1 | 2026-08-11 15:49 | 2026-08-11 15:49 | 1s | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]122` | 1 | 2026-08-11 16:48 | 2026-08-11 16:48 | 0s | 0 | `T1592` | 🟢 LOW |
| `218.188.194[.]70` | 1 | 2026-08-11 15:42 | 2026-08-11 15:42 | 12s | 0 | `T1592` | 🟢 LOW |
| `27.21.27[.]171` | 1 | 2026-08-11 14:58 | 2026-08-11 14:58 | 14s | 0 | `T1592` | 🟢 LOW |
| `43.156.212[.]6` | 1 | 2026-08-11 15:38 | 2026-08-11 15:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.182.24[.]26` | 1 | 2026-08-11 16:28 | 2026-08-11 16:29 | 12s | 0 | `T1592` | 🟢 LOW |
| `5.129.178[.]196` | 1 | 2026-08-11 16:27 | 2026-08-11 16:27 | 13s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]180` | 1 | 2026-08-11 14:55 | 2026-08-11 14:55 | 10s | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]71` | 1 | 2026-08-11 14:55 | 2026-08-11 14:55 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |

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
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 70/100 | 🔴 HIGH | **25/75** 🔴 |
| `1e70b63472772e3f5092ffe9c3573470e73590e6ab6d93fdcede1d368a5fd72d` | Bash Script | `1e70b63472772e3f...` | 57/100 | 🟡 MEDIUM | **19/75** 🔴 |
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
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `287962211de7bcadb39f7576732438b43ee6aab420ec23c29a9d12a8151a547f` | ELF Binary (Linux executable) (x86 32-bit) | `287962211de7bcad...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `2f206563640dd66a743ffd493ce0e3c31a8fc5a24b9f5d2b540fc22d45c13d66` | ELF Binary (Linux executable) (x86 32-bit) | `2f206563640dd66a...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `31d4181843b1ed10a7e7cb3f108f6d6c50a7a4452ee52ddacabe8ca77260615e` | Bash Script | `31d4181843b1ed10...` | 60/100 | 🟡 MEDIUM | **26/75** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |

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
| `140.245.50[.]204` | SG | Oracle Corporation | **100** ⚠️ | 1 |
| `120.224.15[.]67` | CN | China Mobile Communications Corporation | **100** ⚠️ | 50 |
| `66.132.172[.]180` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `211.247.127[.]250` | KR | SK Broadband Co Ltd | **100** ⚠️ | 50 |
| `193.217.0[.]16` | LT | Tele2 Lithuania | **100** ⚠️ | 39 |
| `5.129.178[.]196` | RU | Ediniy Operator Svyazi LLC | **100** ⚠️ | 0 |
| `66.132.195[.]117` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `181.78.3[.]229` | CO | UFINET COLOMBIA, S. A. | **100** ⚠️ | 4 |
| `194.165.16[.]122` | LT | Flyservers S.A. | **100** ⚠️ | 13 |
| `129.153.145[.]135` | US | Oracle Corporation | **100** ⚠️ | 8 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 101 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 93 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 37 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 37 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 37 |

---

## 🔕 False Positive Summary (28 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 6 |
| AbuseIPDB score 12 below threshold 25 | 1 |
| AbuseIPDB score 13 below threshold 25 | 1 |
| AbuseIPDB score 15 below threshold 25 | 1 |
| AbuseIPDB score 22 below threshold 25 | 1 |
| AbuseIPDB score 3 below threshold 25 | 4 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 13 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 194 cases |
| Tool 34  | Credential Extractor        | ✅ 126 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 8 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 75 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 28 filtered (14.4%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 60 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 22 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 93 priority case(s) shown individually · 24 recon entry/entries in table (11 group(s) consolidating 60 session(s)).

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
_Report time: 2026-08-11T17:00:18Z_

